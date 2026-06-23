TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

content = r"""

---

# PART 7 — LEVEL 8: DELTA LAKE, DATABRICKS, UNITY CATALOG, DLT, LAKEFLOW

**Domain Color:** `#ef4444` (Red) | **Prerequisites:** Level 7 | **Est. Hours:** 100+

---

## MODULE 8.1 — Delta Lake Internals

### TOPIC 8.1.1 — Transaction Log Architecture

**Subtopic: _delta_log Structure**
- ALU: Every Delta table has _delta_log/ directory at table root
- ALU: JSON files: 0-padded 20-digit sequence numbers; 000...0000.json, 000...0001.json, ...
- ALU: Each JSON commit file: one JSON object per line (action types)
- ALU: Action types: add, remove, metaData, protocol, commitInfo, cdc, txn
- ALU: add action: path, size, stats (min/max/null counts), partitionValues, modificationTime, dataChange
- ALU: remove action: path, deletionTimestamp, dataChange, extendedFileMetadata
- ALU: metaData action: schemaString (JSON), partitionColumns, configuration, createdTime
- ALU: protocol action: minReaderVersion, minWriterVersion; controls feature compatibility
- ALU: commitInfo action: timestamp, userId, operation, operationParameters, notebook, clusterId
- ALU: Checkpoint: every 10 commits (default); Parquet snapshot of log; avoids replaying all JSON
- ALU: Checkpoint naming: 000...00010.checkpoint.parquet; 000...00010.json contains checkpoint metadata
- ALU: last_checkpoint: _delta_log/_last_checkpoint JSON file; points to latest checkpoint
- ALU: Read protocol: reader reads last_checkpoint → load checkpoint Parquet → replay JSON files since checkpoint

**Subtopic: ACID Properties in Delta Lake**
- ALU: Atomicity: each write creates a new commit JSON atomically (object store PUT); either full commit or nothing
- ALU: Consistency: schema enforcement; constraint checks; consistent view after every commit
- ALU: Isolation: optimistic concurrency; conflict detection at commit time
- ALU: Durability: committed files persist in ADLS/S3/GCS; transaction log is ground truth
- ALU: Optimistic concurrency: writers read current version, make changes, attempt to commit
- ALU: Conflict resolution: writer checks if any conflicting writes occurred since their read version
- ALU: Conflict types: append-only never conflicts; blind insert never conflicts; update/delete may conflict
- ALU: Retry on conflict: Delta SDK retries with exponential backoff; application-level idempotency needed

**Subtopic: Time Travel**
- ALU: Version-based: SELECT * FROM table VERSION AS OF 5
- ALU: Timestamp-based: SELECT * FROM table TIMESTAMP AS OF '2024-01-15 10:00:00'
- ALU: Python: spark.read.format("delta").option("versionAsOf", 5).load(path)
- ALU: RESTORE TABLE table TO VERSION AS OF 5: revert table to old version
- ALU: DESCRIBE HISTORY table: show all commits with operation details
- ALU: Data retention: VACUUM removes files older than retention threshold (default 7 days)
- ALU: Time travel limited to vacuum retention period; cannot go before last VACUUM
- ALU: spark.databricks.delta.retentionDurationCheck.enabled=false: skip safety check (dangerous)

**Subtopic: Schema Management**
- ALU: Schema on write: schema stored in metaData action; enforced on every write
- ALU: Schema mismatch: DataFrameWriter raises AnalysisException by default
- ALU: mergeSchema=True: allow adding new columns; existing data gets NULL for new columns
- ALU: overwriteSchema=True: completely replace schema; use with overwrite mode only
- ALU: Column mapping mode: id-based mapping allows rename/drop without rewriting data
- ALU: Delta column mapping: ALTER TABLE RENAME COLUMN; ALTER TABLE DROP COLUMN
- ALU: Type widening: INT → LONG; FLOAT → DOUBLE allowed with schema evolution
- ALU: Generated columns: GENERATED ALWAYS AS (expr); auto-computed from other columns

**ANIMATION SPEC 8.1.1 — Delta Transaction Log:**
```
Table shown with _delta_log directory
Write operation: new JSON file appears in _delta_log
JSON file content shown: add actions with file paths and stats
Time travel: slider moves version number; file list updates
VACUUM: old remove files older than threshold fade and disappear
Checkpoint: every 10 commits; Parquet file appears; JSON files consolidated
Concurrent writers: two writers shown; conflict detection animation
Winner commits; loser retries with updated state
```

---

### TOPIC 8.1.2 — Delta Lake Operations

**Subtopic: MERGE**
- ALU: Full MERGE syntax with matched/unmatched clauses
- ALU: Performance: larger target table → longer conflict check; partition by merge key
- ALU: Low-shuffle merge: spark.databricks.delta.merge.enableLowShuffle.merge=true
- ALU: Low-shuffle merge: only reads/rewrites partitions that have matched rows
- ALU: MERGE with DELETE: WHEN NOT MATCHED BY SOURCE THEN DELETE
- ALU: Insert-only merge: WHEN NOT MATCHED THEN INSERT (common for dedup upsert)
- ALU: Upsert best practice: filter source to only changed/new records before merge

**Subtopic: OPTIMIZE**
- ALU: OPTIMIZE table_name: compact small files into target file size (default 1GB)
- ALU: OPTIMIZE ... ZORDER BY (col1, col2): compact + sort data spatially
- ALU: Z-ordering: multidimensional sorting; good for multi-column range queries
- ALU: Z-order effectiveness: best for <=4 columns; more columns = diminishing returns
- ALU: Auto-optimize: spark.databricks.delta.autoOptimize.optimizeWrite=true: optimize on write
- ALU: Auto-compaction: spark.databricks.delta.autoOptimize.autoCompact=true: background compaction
- ALU: Predictive optimization: Databricks feature; automatic OPTIMIZE + VACUUM scheduling

**Subtopic: VACUUM**
- ALU: VACUUM table_name RETAIN 168 HOURS: delete files older than 7 days
- ALU: Default retention: 7 days (168 hours); minimum enforced by default
- ALU: DRY RUN: VACUUM RETAIN 0 HOURS DRY RUN: shows what would be deleted without deleting
- ALU: Risk: vacuuming too aggressively breaks time travel for queries using old snapshots
- ALU: VACUUM safety: ensure no active streaming queries or long-running reads reference old versions

**Subtopic: Delta Table Properties**
- ALU: ALTER TABLE SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name')
- ALU: delta.logRetentionDuration: how long to keep log files (default 30 days)
- ALU: delta.deletedFileRetentionDuration: how long to keep data files after removal (default 7 days)
- ALU: delta.autoOptimize.optimizeWrite: write-time file compaction
- ALU: delta.enableChangeDataFeed=true: enable CDC; stores row-level changes
- ALU: delta.dataSkippingNumIndexedCols=32: number of columns with stats for data skipping

**Subtopic: Change Data Feed (CDF)**
- ALU: Enabled via: ALTER TABLE SET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true')
- ALU: CDF columns: _change_type (insert/update_preimage/update_postimage/delete), _commit_version, _commit_timestamp
- ALU: Read CDF: spark.read.format("delta").option("readChangeData", "true").option("startingVersion", 5).load(path)
- ALU: Streaming CDF: readStream.format("delta").option("readChangeData", "true")
- ALU: CDF storage: extra data files in _change_data/ directory; adds ~10-20% storage overhead
- ALU: Use cases: downstream sync, SCD2 updates, audit trails, CDC pipelines

---

## MODULE 8.2 — Databricks Platform

### TOPIC 8.2.1 — Databricks Architecture

**Subtopic: Control Plane and Data Plane**
- ALU: Control plane: managed by Databricks; hosted in Databricks cloud account
- ALU: Control plane contains: web UI, REST API, job scheduler, metastore manager, cluster manager
- ALU: Data plane: customer's cloud subscription; compute (VMs) and storage (ADLS)
- ALU: Classic data plane: VMs in customer VNet; network traffic passes through control plane tunnel
- ALU: Serverless data plane: compute in Databricks-managed VNet; network proxy for security
- ALU: VNet injection: classic data plane VMs placed in customer-specified VNet
- ALU: Private link: encrypt/isolate control-plane-to-data-plane communication

**Subtopic: Cluster Types**
- ALU: All-purpose cluster: interactive; persistent; shared by users; dev/exploration
- ALU: Job cluster: created for specific job run; terminated after completion; cheaper; prod use
- ALU: SQL warehouse (SQL endpoint): optimized for SQL analytics; Photon-enabled
- ALU: Classic SQL warehouse: shared compute; classic Spark SQL
- ALU: Pro SQL warehouse: Photon; better performance; serverless option
- ALU: Serverless SQL warehouse: instantly available; no provisioning; per-second billing
- ALU: Single-node cluster: driver only; no workers; good for development/pandas
- ALU: Multi-node: driver + N workers; production workloads; auto-scaling

**Subtopic: Cluster Configuration**
- ALU: Node type: Standard_DS3_v2 (14GB, 4 core) to Standard_L32s_v3 (NVMe, high I/O)
- ALU: Driver node: often same size as workers; store broadcast tables + driver data
- ALU: Auto-scaling: min/max workers; scale based on task queue depth
- ALU: Spot instances (preemptible): 60-80% cheaper; may be terminated; use for fault-tolerant jobs
- ALU: Databricks runtime: DBR 14.3 LTS = Spark 3.5.x + Delta 3.1.x + specific libraries
- ALU: LTS runtime: Long-Term Support; 2-year support; prefer for production
- ALU: GPU runtime: for ML/DL workloads; CUDA drivers included
- ALU: Init scripts: run on every cluster node at start; install libraries, configure settings
- ALU: Cluster policies: admin-defined templates; restrict node types, autoscale, libraries

**Subtopic: Databricks Jobs**
- ALU: Job: scheduled or triggered execution of notebook/Python/JAR/SQL/DLT/dbt
- ALU: Task dependencies: A → B → C; parallel: A → [B, C] → D
- ALU: Job cluster: dedicated cluster per run; fresh state; terminates on complete
- ALU: Shared cluster: reuse existing all-purpose cluster; skip startup time
- ALU: Schedule: cron syntax or continuous trigger
- ALU: Retry: max retries + retry interval; exponential backoff option
- ALU: Timeout: per-task and per-run timeout
- ALU: Notification: email/webhook on success/failure/start
- ALU: Repair run: re-run only failed/skipped tasks; preserve successful outputs
- ALU: Job parameters: pass key-value parameters to notebook widgets or dbutils.widgets
- ALU: DBFS vs Unity Catalog: use Unity Catalog volumes for data; avoid DBFS for new code

**Subtopic: Databricks Notebooks**
- ALU: Cells: Python, SQL, Scala, R, Markdown, Shell (%sh), FileSystem (%fs)
- ALU: Magic commands: %python, %sql, %scala, %r, %md, %sh, %fs, %run, %pip, %conda
- ALU: %run ./notebook_path: execute another notebook inline; share variables
- ALU: dbutils.fs: list/cp/mv/rm DBFS and ADLS; dbutils.fs.ls("abfss://...")
- ALU: dbutils.widgets: job parameter inputs; dropdown/text/combobox/multiselect
- ALU: dbutils.secrets.get("scope", "key"): retrieve secret from Key Vault backed scope
- ALU: dbutils.notebook.exit("value"): return value from notebook to caller
- ALU: display(df): render DataFrame as formatted interactive table; show charts
- ALU: Notebook-scoped library: %pip install package: installs in current session only
- ALU: Revision history: auto-saved every few minutes; restore any revision
- ALU: Co-authoring: multiple users editing same notebook; last write wins (no merge)

**ANIMATION SPEC 8.2.1 — Databricks Cluster Lifecycle:**
```
Timeline from cluster creation to termination
Pending → Starting (VM provisioning, init scripts) → Running → Terminating
Worker nodes scale out during load: animated addition
Worker nodes scale in when idle: animated removal
Job cluster variant: created on demand, terminates after task
Cost meter: $ per DBU per hour
Spot instance interruption: worker disappears; new worker added
```

---

## MODULE 8.3 — Unity Catalog

### TOPIC 8.3.1 — Unity Catalog Architecture

**Subtopic: Three-Level Namespace**
- ALU: catalog.schema.table: three-part fully qualified name
- ALU: Catalog: top-level namespace; maps to one or more ADLS storage locations
- ALU: Schema (database): namespace within catalog; groups related tables
- ALU: Table: registered object in Unity Catalog metastore
- ALU: Managed table: Unity Catalog manages data lifecycle; stored in catalog/schema storage root
- ALU: External table: data managed externally; UC registers metadata only; user manages files
- ALU: View: virtual table defined by SQL query; no physical storage
- ALU: Materialized view (MV): DLT-powered; computed result stored; auto-refreshed
- ALU: Function: SQL/Python UDF registered in Unity Catalog; shareable across workspaces
- ALU: Volume: non-tabular data governance; files in ADLS governed by UC ACLs
- ALU: External location: registered ADLS path + credential; base for external tables and volumes

**Subtopic: Metastore**
- ALU: Unity Catalog metastore: one per Azure region; shared across multiple Databricks workspaces
- ALU: Account-level metastore: managed at Databricks account level, not workspace level
- ALU: Legacy Hive metastore: per-workspace; not shareable; no fine-grained ACLs
- ALU: Migration: SYNC command or UPGRADE to migrate Hive metastore tables to UC
- ALU: Storage credential: Azure managed identity or service principal for storage access
- ALU: External location: ABFSS path + storage credential = governed ADLS access
- ALU: Delta Sharing: share data cross-org or cross-cloud via open Delta Sharing protocol

**Subtopic: Privilege Model**
- ALU: Principal types: user, service principal, group
- ALU: Account groups vs workspace groups: account groups sync across workspaces
- ALU: Privileges: USE CATALOG, USE SCHEMA, SELECT, MODIFY, CREATE TABLE, CREATE SCHEMA, etc.
- ALU: GRANT SELECT ON TABLE catalog.schema.table TO user@domain.com
- ALU: GRANT ALL PRIVILEGES ON SCHEMA catalog.schema TO group_name
- ALU: Inherited privileges: grant on catalog propagates to schemas and tables within
- ALU: Column-level security: GRANT SELECT ON TABLE (col1, col2): limit to specific columns
- ALU: Row-level security: CREATE VIEW with WHERE clause; GRANT SELECT on view; deny on table
- ALU: Dynamic views: current_user() in view WHERE clause; personalized access
- ALU: Data masking: mask sensitive columns based on user group membership
- ALU: Audit logs: all data access logged; Unity Catalog system tables (system.access.audit)

**Subtopic: Lineage and Discovery**
- ALU: Automatic lineage: UC captures table-to-table lineage from SQL/DataFrame operations
- ALU: Column-level lineage: tracks which source columns feed which target columns
- ALU: Lineage API: REST API and UI; show upstream sources and downstream consumers
- ALU: Tags: key-value metadata on catalogs/schemas/tables/columns; searchable
- ALU: Search: catalog explorer search by name, tag, owner, type
- ALU: Data classification: scan and tag PII columns automatically (Databricks partner)
- ALU: Quality metrics: Delta Sharing + quality expectations visible in catalog

---

## MODULE 8.4 — Delta Live Tables (DLT)

### TOPIC 8.4.1 — DLT Concepts

**Subtopic: Core Architecture**
- ALU: DLT: declarative ETL framework; you define what; DLT manages how and when
- ALU: Pipeline: collection of notebooks/Python files defining tables and flows
- ALU: Triggered pipeline: runs once and terminates; like a batch job
- ALU: Continuous pipeline: runs continuously; reprocesses new data as it arrives
- ALU: Development mode: shorter cluster startup; retains cluster; uses subset of data
- ALU: Production mode: full data; dedicated cluster; terminates on complete
- ALU: @dlt.table: define a materialized view or incremental table
- ALU: @dlt.view: temporary view; not materialized; used as intermediate transformation
- ALU: LIVE. prefix in SQL: references DLT-managed tables; triggers dependency tracking

**Subtopic: Python DLT API**
- ALU: import dlt
- ALU: @dlt.table(name="bronze_orders", comment="Raw orders from source")
  def bronze_orders(): return spark.readStream.format("cloudFiles").option("cloudFiles.format", "json").load(path)
- ALU: @dlt.table(name="silver_orders") def silver_orders(): return dlt.read_stream("bronze_orders").filter(...)
- ALU: dlt.read("table"): batch read of DLT-managed table
- ALU: dlt.read_stream("table"): streaming read
- ALU: @dlt.expect("valid_id", "order_id IS NOT NULL"): data quality constraint; soft constraint
- ALU: @dlt.expect_or_drop("valid_amount", "amount > 0"): drop rows violating constraint
- ALU: @dlt.expect_or_fail("no_nulls", "id IS NOT NULL"): fail pipeline on violation
- ALU: @dlt.expect_all(expectations_dict): multiple expectations at once
- ALU: table_properties: {"pipelines.reset.allowed": "false"} to prevent full refresh

**Subtopic: Auto Loader (cloudFiles)**
- ALU: Auto Loader: incrementally ingest files as they land in ADLS/S3
- ALU: File notification mode: subscribe to ADLS event notifications; scales to millions of files
- ALU: Directory listing mode: list ADLS directory periodically; simpler; slower for large dirs
- ALU: cloudFiles.schemaLocation: path to store inferred schema; schema evolution support
- ALU: cloudFiles.inferColumnTypes=true: infer types (slower); false = all strings
- ALU: cloudFiles.schemaEvolutionMode: addNewColumns/rescue/failOnNewColumns/none
- ALU: rescue column: unexpected columns go to _rescued_data JSON string column
- ALU: spark.readStream.format("cloudFiles").option("cloudFiles.format", "parquet").schema(schema).load(path)
- ALU: Exactly-once: checkpoint + file notification ensures no file missed or double-processed

**Subtopic: DLT Data Quality**
- ALU: Expectations: named boolean conditions per row; logged in pipeline event log
- ALU: Quality metrics in UI: % rows passing/failing per expectation per table update
- ALU: Event log: DLT system table; stores all pipeline events including quality metrics
- ALU: SELECT * FROM event_log(table_name) WHERE event_type = 'flow_progress'
- ALU: Quarantine pattern: route failed rows to separate quarantine table for investigation
- ALU: @dlt.table with two outputs: valid + invalid (anti-join or CASE-based routing)

**Subtopic: DLT Medallion Pipeline**
- ALU: Bronze: Auto Loader source → append-only Delta table; raw data preserving all fields
- ALU: Silver: streaming read from Bronze → filter, deduplicate, validate → Silver Delta table
- ALU: Gold: batch read from Silver → aggregations, joins, business metrics → Gold Delta table
- ALU: Pipeline graph: visual DAG showing Bronze→Silver→Gold data lineage
- ALU: Selective refresh: re-run only specific tables in pipeline
- ALU: Full refresh: recompute all tables from scratch; required for logic changes

**ANIMATION SPEC 8.4.1 — DLT Pipeline:**
```
Pipeline graph: Bronze, Silver, Gold nodes connected by arrows
File lands in ADLS: event triggers Auto Loader
Bronze table receives row: append animation
Silver transformation: rows flow Bronze→Silver; invalid rows branch to quarantine
Gold aggregation: Silver rows collapse into aggregate value
Quality metrics: passing/failing percentage badges on each table
Pipeline run timeline: stages with duration bars
```

---

## MODULE 8.5 — Lakeflow (Databricks Workflows 2.0)

### TOPIC 8.5.1 — Lakeflow Pipelines

**Subtopic: Lakeflow Architecture**
- ALU: Lakeflow: next-gen orchestration within Databricks; successor to Databricks Workflows
- ALU: Declarative pipelines: define dependencies; Lakeflow determines execution order
- ALU: Task types: DLT pipeline, notebook, SQL, Python script, dbt, Spark JAR, condition
- ALU: Dependency graph: DAG of tasks; parallel execution where possible
- ALU: Dynamic task values: task A produces value; task B uses value.taskValues("A", "key")
- ALU: For-each task: iterate task over dynamic list produced by upstream task
- ALU: Repair and rerun: failed tasks marked; rerun only failed + downstream tasks
- ALU: Run history: full audit of runs; task-level status and logs

**Subtopic: Integration with Unity Catalog**
- ALU: Lakeflow pipelines produce Unity Catalog tables: full lineage tracked
- ALU: Scheduled Lakeflow + DLT: ADF-like orchestration within Databricks ecosystem
- ALU: Cross-workspace pipelines: share data via Unity Catalog; cross-workspace task dependencies via Delta Sharing
- ALU: Serverless Lakeflow: no cluster management; instant start; DBU-per-second billing
- ALU: Bundles: Databricks Asset Bundles (DAB); define jobs, clusters, notebooks as YAML; deploy via CI/CD
- ALU: databricks bundle deploy: deploy bundle to workspace
- ALU: databricks bundle run job_name: trigger job from CLI
- ALU: Bundle environments: dev/staging/prod with different parameter sets

""".lstrip()

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 7 written!")
