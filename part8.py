TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

content = r"""

---

# PART 8 — LEVEL 9: PRODUCTION ENGINEERING, DEVOPS, ARCHITECTURE, INTERVIEW PREP

**Domain Color:** `#8b5cf6` (Purple) | **Prerequisites:** Level 8 | **Est. Hours:** 80+

---

## MODULE 9.1 — Data Engineering Architecture

### TOPIC 9.1.1 — System Design for Data Engineers

**Subtopic: Batch Architecture Patterns**
- ALU: Lambda architecture: batch layer (accuracy) + speed layer (latency) + serving layer
- ALU: Lambda complexity: maintain two code paths; difficult to keep in sync; largely deprecated
- ALU: Kappa architecture: streaming only; replay historical data through same streaming pipeline
- ALU: Kappa advantage: single code path; simpler operations; Kafka/Event Hub as replayable store
- ALU: Data mesh: domain-oriented; decentralized ownership; data as product; federated governance
- ALU: Data mesh principles: domain ownership, data as product, self-serve platform, federated governance
- ALU: Data fabric: automated metadata-driven integration; AI-assisted; centralized governance
- ALU: Lakehouse: Delta Lake/Iceberg on object storage; ACID + BI + ML in one platform
- ALU: Lakehouse vs data warehouse: DW = structured only + expensive; Lakehouse = all formats + cheap
- ALU: Modern data stack: Fivetran (ingest) + Snowflake/Databricks (store/transform) + dbt (transform) + Looker/Power BI (serve)

**Subtopic: Data Modeling Paradigms**
- ALU: Kimball (dimensional modeling): star schema; fact + dimension tables; optimized for analytics
- ALU: Fact table: measures + foreign keys to dimensions; typically large; append-only
- ALU: Dimension table: descriptive attributes; slowly changing; surrogate keys
- ALU: Grain: finest level of detail in fact table; define before design
- ALU: Conformed dimensions: shared dimensions across fact tables; enable cross-subject-area queries
- ALU: Inmon (3NF data warehouse): normalized EDW; data marts derived; consistency first
- ALU: One Big Table (OBT): denormalized wide table; fast queries; data duplication; gold layer
- ALU: Activity schema: one record per event; wide columns for properties; flexible analytics
- ALU: Anchor modeling: ultra-normalized; each attribute in own table; handles change well
- ALU: Data vault: hub + satellite + link; auditable; append-only; good for raw vault

**Subtopic: Partitioning Strategies**
- ALU: Date partitioning: YEAR/MONTH/DAY hierarchy; align with query patterns
- ALU: Over-partitioning: too many small partitions; Spark metadata overhead
- ALU: Under-partitioning: single large partitions; no pruning benefit
- ALU: Partition pruning: WHERE event_date = '2024-01-15' reads only one partition directory
- ALU: Z-ordering within partition: secondary sort for multi-column filters
- ALU: Multi-dimensional partitioning: partition by date AND region; more aggressive pruning
- ALU: Delta Lake liquid clustering (Databricks 13.3+): auto-cluster without partition columns
- ALU: Clustering replaces Z-ordering and partitioning with dynamic maintenance

**ANIMATION SPEC 9.1.1 — System Design Whiteboard:**
```
Interactive diagram builder
Drag components: source, ingestion, storage, processing, serving
Draw data flow arrows
Latency labels: batch (hours) vs streaming (seconds) vs real-time (ms)
Cost indicator: cost scales with component choice
Trade-off panel: shows latency vs cost vs complexity triangle
```

---

## MODULE 9.2 — DevOps for Data Engineering

### TOPIC 9.2.1 — CI/CD for Data Pipelines

**Subtopic: GitHub Actions for Data Engineering**
- ALU: Workflow file: .github/workflows/deploy.yml
- ALU: Trigger: on push to main, pull_request, schedule, workflow_dispatch
- ALU: Jobs: checkout → setup Python → install deps → lint → test → deploy
- ALU: Databricks CLI in Actions: uses: databricks/setup-cli@main
- ALU: DATABRICKS_HOST and DATABRICKS_TOKEN as GitHub secrets
- ALU: Bundle deployment: databricks bundle deploy --target prod
- ALU: ADF deployment: ARM template export + az deployment group create
- ALU: Environment protection: require reviewer approval for prod deployments
- ALU: Branch strategy: feature → dev (auto-deploy) → staging (on PR) → prod (manual approval)
- ALU: Self-hosted runner: runner in customer VNet for private endpoint access
- ALU: Matrix strategy: test against multiple Python/DBR versions simultaneously

**Subtopic: Testing Data Pipelines**
- ALU: Unit tests: test transformation logic with small in-memory DataFrames
- ALU: pytest + pyspark: SparkSession fixture; conftest.py setup
- ALU: Test fixture: SparkSession.builder.master("local[*]").appName("test").getOrCreate()
- ALU: Delta table test: create temp Delta table; run transformation; assert result
- ALU: Schema test: assert output schema matches expected StructType
- ALU: Data quality test: assert no nulls in key columns; assert row count > 0
- ALU: Great Expectations: declarative data quality; expectations suites; validation results
- ALU: dbt tests: not_null, unique, accepted_values, relationships (FK) in YAML
- ALU: Integration tests: run actual pipeline end-to-end on dev environment
- ALU: Contract testing: source provides data contract; consumer validates against it

**Subtopic: Infrastructure as Code**
- ALU: Terraform for Azure: provider azurerm; manage storage accounts, ADF, Databricks workspace
- ALU: Terraform state: remote state in Azure Blob; state locking via Azure Blob lease
- ALU: Terraform workspace: separate state per environment (dev/staging/prod)
- ALU: ARM templates: Azure Resource Manager JSON; verbose but comprehensive
- ALU: Bicep: ARM DSL; cleaner syntax; compiles to ARM JSON
- ALU: Databricks Terraform provider: manage clusters, jobs, notebooks, secrets, permissions
- ALU: Databricks Asset Bundles: native DAB YAML; Databricks-native IaC for jobs/pipelines
- ALU: Pulumi: Python/TypeScript IaC; programmatic; good for complex conditional logic

**Subtopic: Monitoring and Alerting**
- ALU: Databricks alerts: SQL query result triggers email/Slack/Teams/PagerDuty notification
- ALU: ADF monitoring: Azure Monitor alerts on pipeline failure; Log Analytics for run history
- ALU: Custom metrics: emit from Spark jobs via Dropwizard metrics; push to Prometheus/Graphite
- ALU: SLA monitoring: track job duration; alert if duration > N× baseline (anomaly detection)
- ALU: Data freshness monitoring: SELECT MAX(updated_at) FROM table; alert if too old
- ALU: Row count validation: compare row count to expected range; alert on anomaly
- ALU: Column null rate: alert if null_rate > threshold for critical columns
- ALU: Duplicate detection: count vs count(distinct key); alert on high duplicate ratio

---

## MODULE 9.3 — Performance and Optimization Patterns

### TOPIC 9.3.1 — Advanced Optimization

**Subtopic: Photon Engine (Databricks)**
- ALU: Photon: native C++ vectorized query engine; replaces JVM code generation for SQL/DataFrame
- ALU: SIMD vectorization: processes 4-16 values per CPU instruction; 2-12x faster for scans/aggregations
- ALU: Photon-compatible operations: scan, filter, aggregation, join, sort, window functions
- ALU: Photon limitations: complex Python UDFs fall back to JVM; some nested types
- ALU: DBU multiplier: Photon clusters cost 2x DBU but often execute 4-10x faster = net cheaper
- ALU: SQL warehouse: all SQL workloads use Photon automatically
- ALU: Enable on compute: select "Photon acceleration" in cluster config

**Subtopic: Query Result Caching**
- ALU: Delta cache (Databricks): caches remote ADLS Parquet data on local NVMe SSD
- ALU: Delta cache auto-populates on first read; subsequent reads served from SSD
- ALU: Delta cache differs from Spark cache: Spark cache = memory; Delta cache = disk
- ALU: spark.databricks.io.cache.enabled=true (default on cache-accelerated node types)
- ALU: Synapse dedicated SQL pool result cache: exact query result cached 48 hours
- ALU: Spark SQL result caching: spark.sql.cache.serializer; df.cache() explicit
- ALU: Query store (SQL Server/Azure SQL): cache execution plans + query statistics

**Subtopic: Cost Optimization**
- ALU: Spot/preemptible workers: 60-80% cheaper; tolerate interruptions; use for batch jobs
- ALU: Auto-scaling: avoid over-provisioning for variable workloads
- ALU: Serverless SQL warehouse: no idle cost; per-query billing; good for BI tools
- ALU: Job clusters: terminate after job; don't pay for idle all-purpose cluster time
- ALU: Storage tier: archive old data to Cool/Archive tier; significant cost reduction
- ALU: Parquet compression: ZSTD reduces storage 30-50% vs SNAPPY; cheaper storage
- ALU: VACUUM regularly: remove old files; reduce storage cost
- ALU: Photon for SQL: even at 2x DBU price, faster execution often = lower total cost
- ALU: Reserved instances: 1-year or 3-year commit; 40-60% cheaper than pay-as-you-go

---

## MODULE 9.4 — Interview and Certification Prep

### TOPIC 9.4.1 — Data Engineering Interview Guide

**Subtopic: SQL Interview Questions (Must Know)**
- ALU: Find second highest salary: SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp)
- ALU: Running total: SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING AND CURRENT ROW)
- ALU: Deduplicate keeping latest: ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) = 1
- ALU: Month-over-month growth: (current - LAG(current,1) OVER (ORDER BY month)) / LAG(current,1)...
- ALU: Customers who bought product A and B: intersect on customer_id filtered by product
- ALU: Sessions from events: use LAG to detect gaps > 30 min; cumsum of gap flags = session id
- ALU: Consecutive days: date - ROW_NUMBER() OVER (ORDER BY date) = constant for consecutive dates
- ALU: Most common value per group: ROW_NUMBER() OVER (PARTITION BY group ORDER BY count DESC) = 1
- ALU: Pivot without PIVOT: SUM(CASE WHEN category='A' THEN amount END) AS A
- ALU: Self-referencing hierarchy: recursive CTE traversal

**Subtopic: PySpark Interview Questions**
- ALU: Explain DAG: how transformations chain lazily; action triggers execution; stages at shuffle
- ALU: Difference repartition vs coalesce: repartition = full shuffle, balanced; coalesce = no shuffle, can skew
- ALU: Why avoid collect(): pulls all data to driver; OOM for large datasets
- ALU: Broadcast join: small table broadcast to all executors; avoids shuffle; set via hint or threshold
- ALU: How to handle skew: salting, broadcast hint, AQE skew join, isolation of hot keys
- ALU: Difference cache vs persist: cache() = MEMORY_AND_DISK; persist() = any StorageLevel
- ALU: Explain Catalyst: AST → logical plan → optimized logical → physical → code gen
- ALU: How to tune shuffle.partitions: 128-200MB per partition target; count(rows)/expected_partition_bytes
- ALU: Window vs GroupBy: GroupBy collapses rows; Window adds column to every row
- ALU: foreachBatch vs foreach in streaming: foreachBatch receives full micro-batch as DataFrame (more efficient)

**Subtopic: Delta Lake Interview Questions**
- ALU: How Delta achieves ACID: JSON transaction log; optimistic concurrency; schema enforcement
- ALU: Time travel mechanism: read from _delta_log JSON files for specific version
- ALU: MERGE performance optimization: partition by merge key; low-shuffle merge; filter source
- ALU: VACUUM risk: deletes files needed for time travel; set appropriate retention
- ALU: Schema evolution: mergeSchema for adds; overwriteSchema for replacements
- ALU: CDF use cases: downstream sync, audit trail, SCD2 updates, CDC propagation
- ALU: Difference managed vs external table: managed = UC controls data lifecycle; external = user manages files

**Subtopic: Azure Architecture Questions**
- ALU: Why ADLS Gen2 over Blob Storage: hierarchical namespace; atomic rename; POSIX ACLs; better Spark performance
- ALU: Private endpoint vs service endpoint: private endpoint gives NIC in VNet + true private IP; preferred
- ALU: ADF vs Databricks: ADF = orchestration + simple copy; Databricks = complex transformation + ML
- ALU: Event Hub vs Service Bus: Event Hub = high-throughput event streaming; Service Bus = message queue with ordering/sessions
- ALU: Key Vault secret rotation: auto-rotate with Key Vault certificates; app fetches latest version on each call
- ALU: Synapse dedicated vs serverless: dedicated = provisioned capacity + columnstore; serverless = pay-per-query on ADLS

**Subtopic: System Design Interview**
- ALU: Design real-time fraud detection: Event Hub ingest → Spark Streaming → ML model scoring → Cosmos DB output → alert API
- ALU: Design data warehouse migration: assess current schema → ETL refactor → parallel run validation → cutover
- ALU: Design multi-tenant data platform: Unity Catalog per tenant catalog, or per-tenant schema with row-level security
- ALU: Handle late-arriving data: watermark in streaming; reprocessing window in batch; upsert to idempotent target
- ALU: Design for 10TB daily ingestion: ADLS partitioned by date + source; ADF or Event Hub ingest; DLT Bronze→Gold; dedicated SQL pool or Databricks for serving
- ALU: Idempotent pipeline design: MERGE with upsert; checkpoint for streaming; dedup on business key

---

### TOPIC 9.4.2 — Certification Preparation

**Subtopic: DP-203: Azure Data Engineer Associate**
- ALU: Exam domains: Design and implement data storage (25-30%), Develop data processing (25-30%), Secure monitor and optimize (30-35%)
- ALU: Key services: Azure Data Lake Gen2, Azure Synapse Analytics, Azure Databricks, ADF, Event Hubs, Stream Analytics, Azure SQL, Cosmos DB
- ALU: Storage focus: partitioning strategies, file formats, compression, ADLS ACLs, lifecycle management
- ALU: Synapse focus: dedicated vs serverless pool, distribution strategies, PolyBase, column store
- ALU: Streaming focus: Azure Stream Analytics job query syntax; windowing functions; reference data
- ALU: Security focus: managed identities, RBAC, Key Vault integration, network isolation, TDE, CMK
- ALU: Performance focus: data skipping, caching, distribution, auto-scale, AQE
- ALU: Study resources: Microsoft Learn paths; practice exams; hands-on labs in Azure sandbox

**Subtopic: Databricks Certified Data Engineer Professional**
- ALU: Exam focus: Delta Lake internals, DLT, Databricks SQL, Unity Catalog, streaming, production patterns
- ALU: Delta deep: transaction log, ACID, time travel, MERGE, OPTIMIZE, VACUUM, CDF, schema evolution
- ALU: DLT: @dlt.table, @dlt.expect, Auto Loader, pipeline types, medallion with DLT
- ALU: Unity Catalog: three-level namespace, privilege model, lineage, external tables, volumes
- ALU: Streaming: Structured Streaming, watermarks, triggers, checkpointing, foreachBatch
- ALU: Production patterns: cluster configuration, job clusters, auto-scaling, secret management, CI/CD
- ALU: Practice: Databricks learning paths; Partner Training; community edition Databricks

**Subtopic: DP-900: Azure Data Fundamentals**
- ALU: Entry-level; covers data concepts, relational databases, non-relational, analytics workloads in Azure
- ALU: Key concepts: batch vs streaming, structured vs unstructured, OLTP vs OLAP, NoSQL types
- ALU: Azure services overview: Azure SQL, Cosmos DB, Azure Storage, Synapse, Databricks, Power BI
- ALU: Recommended for: beginners; stepping stone to DP-203

**Subtopic: Study Strategy**
- ALU: Build hands-on: theory without practice = fail; create Azure free account + Databricks Community
- ALU: Implement projects: ingest CSV to Bronze → transform to Silver → aggregate to Gold → dashboard
- ALU: Use Microsoft Learn: official modules with sandbox environments; free
- ALU: Flashcard the ALUs: each ALU point is a potential exam question; know all definitions
- ALU: Practice exams: MeasureUp, Whizlabs, Udemy practice tests; target 80%+ before scheduling
- ALU: Exam day: manage time; flag uncertain questions; no negative marking

---

## MODULE 9.5 — Enterprise Patterns

### TOPIC 9.5.1 — Production Data Platform Patterns

**Subtopic: Data Contracts**
- ALU: Data contract: schema + semantics + SLAs agreed between producer and consumer
- ALU: Schema: column names, types, required/optional; versioned and backward-compatible
- ALU: Semantics: definition of each field; business logic; NULL meaning
- ALU: SLA: freshness (data available by T+N), completeness (% of expected rows), quality (% meeting expectations)
- ALU: Contract enforcement: schema registry; Great Expectations; dbt tests; Delta constraints
- ALU: Consumer-driven contracts: consumer defines what they need; producer ensures it
- ALU: Contract versioning: semantic versioning; BREAKING changes require major version bump

**Subtopic: Idempotency Patterns**
- ALU: Idempotent operation: applying it multiple times has same effect as once
- ALU: INSERT idempotent via MERGE: upsert by natural key; safe to re-run
- ALU: Overwrite partition idempotent: overwriting same partition always yields same result
- ALU: Checkpoint for streaming: resume from last committed offset; no duplicate processing
- ALU: Job dedup: use job_run_id as idempotency key; ADF passes pipeline run ID
- ALU: At-least-once + idempotent sink = effectively exactly-once end-to-end

**Subtopic: Error Handling Patterns**
- ALU: Dead letter queue: failed messages routed to separate queue for investigation
- ALU: Retry with exponential backoff: 1s, 2s, 4s, 8s... with jitter; avoid thundering herd
- ALU: Circuit breaker: after N failures, stop retrying for duration T; prevent cascade
- ALU: Quarantine table: rows failing data quality routed to separate table; don't block pipeline
- ALU: Alert on quarantine growth: quarantine growing = systemic source issue
- ALU: Saga pattern: long-running transaction across services; compensating transactions on failure

**Subtopic: Observability**
- ALU: Three pillars: logs (events), metrics (counters/gauges/histograms), traces (request lifecycle)
- ALU: Structured logging: JSON format; key-value pairs; machine-readable; queryable in Log Analytics
- ALU: Spark metrics: Dropwizard metrics; expose via Prometheus sink; visualize in Grafana
- ALU: Pipeline metadata table: log pipeline_run_id, start_time, end_time, rows_processed, status
- ALU: Lineage tracking: source file + processing timestamp + target table stored as metadata
- ALU: SLA dashboard: track pipeline duration percentiles; p50/p90/p99; trend charts
- ALU: Data quality dashboard: per-table quality score over time; regression detection
- ALU: On-call runbook: documented steps to diagnose and resolve common failures

---

# APPENDIX A — COMPLETE DESIGN SYSTEM TOKENS (EXTENDED)

```css
/* ── Pastel Extended Palette ─────────────────────── */
:root {
  /* Brand Blues */
  --color-blue-50:  #eff6ff;
  --color-blue-100: #dbeafe;
  --color-blue-200: #bfdbfe;
  --color-blue-300: #93c5fd;
  --color-blue-400: #60a5fa;
  --color-blue-500: #4f8ef7;  /* PRIMARY */
  --color-blue-600: #2563eb;
  --color-blue-700: #1d4ed8;
  --color-blue-800: #1e40af;
  --color-blue-900: #1e3a8a;

  /* Purples */
  --color-purple-50:  #faf5ff;
  --color-purple-100: #f3e8ff;
  --color-purple-200: #e9d5ff;
  --color-purple-300: #d8b4fe;
  --color-purple-400: #c084fc;
  --color-purple-500: #8b5cf6;  /* SECONDARY */
  --color-purple-600: #7c3aed;
  --color-purple-700: #6d28d9;

  /* Greens */
  --color-green-50:  #f0fdf4;
  --color-green-100: #dcfce7;
  --color-green-500: #22c55e;  /* SUCCESS */
  --color-green-600: #16a34a;

  /* Ambers */
  --color-amber-50:  #fffbeb;
  --color-amber-100: #fef3c7;
  --color-amber-500: #f59e0b;  /* WARNING */
  --color-amber-600: #d97706;

  /* Reds */
  --color-red-50:  #fff1f2;
  --color-red-100: #ffe4e6;
  --color-red-500: #ef4444;   /* DANGER */
  --color-red-600: #dc2626;

  /* Neutrals */
  --color-gray-50:  #f8fafc;
  --color-gray-100: #f1f5f9;
  --color-gray-200: #e2e8f0;
  --color-gray-300: #cbd5e1;
  --color-gray-400: #94a3b8;
  --color-gray-500: #64748b;
  --color-gray-600: #475569;
  --color-gray-700: #334155;
  --color-gray-800: #1e293b;
  --color-gray-900: #0f172a;

  /* Semantic */
  --color-bg:           var(--color-gray-50);
  --color-surface:      #ffffff;
  --color-surface-2:    var(--color-gray-100);
  --color-border:       var(--color-gray-200);
  --color-text-primary: var(--color-gray-900);
  --color-text-muted:   var(--color-gray-500);
  --color-text-xmuted:  var(--color-gray-400);

  /* Domain accent colors */
  --domain-fundamentals:  var(--color-blue-500);
  --domain-data:          #06b6d4;   /* cyan-500 */
  --domain-database:      #10b981;   /* emerald-500 */
  --domain-sql:           var(--color-amber-500);
  --domain-python:        #3b82f6;   /* blue-500 */
  --domain-linux:         #84cc16;   /* lime-500 */
  --domain-git:           #f97316;   /* orange-500 */
  --domain-cloud:         #0ea5e9;   /* sky-500 */
  --domain-azure:         #0078d4;   /* Azure brand blue */
  --domain-spark:         #f97316;   /* orange-500 */
  --domain-delta:         #ef4444;   /* red-500 */
  --domain-databricks:    #ff3621;   /* Databricks brand red */
  --domain-streaming:     #8b5cf6;   /* purple-500 */
  --domain-devops:        #06b6d4;   /* cyan-500 */
  --domain-architecture:  #64748b;   /* gray-500 */

  /* Typography */
  --font-heading: 'Space Grotesk', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-code:    'JetBrains Mono', 'Fira Code', monospace;

  --font-size-xs:   0.75rem;   /* 12px */
  --font-size-sm:   0.875rem;  /* 14px */
  --font-size-base: 1rem;      /* 16px */
  --font-size-lg:   1.125rem;  /* 18px */
  --font-size-xl:   1.25rem;   /* 20px */
  --font-size-2xl:  1.5rem;    /* 24px */
  --font-size-3xl:  1.875rem;  /* 30px */
  --font-size-4xl:  2.25rem;   /* 36px */
  --font-size-5xl:  3rem;      /* 48px */

  --font-weight-regular: 400;
  --font-weight-medium:  500;
  --font-weight-semibold:600;
  --font-weight-bold:    700;
  --font-weight-extrabold:800;

  --line-height-tight:  1.25;
  --line-height-snug:   1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed:1.625;
  --line-height-loose:  2;

  /* Spacing (4px grid) */
  --space-1:  0.25rem;  /* 4px */
  --space-2:  0.5rem;   /* 8px */
  --space-3:  0.75rem;  /* 12px */
  --space-4:  1rem;     /* 16px */
  --space-5:  1.25rem;  /* 20px */
  --space-6:  1.5rem;   /* 24px */
  --space-8:  2rem;     /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */

  /* Border Radius */
  --radius-sm:  0.25rem;  /* 4px */
  --radius-md:  0.5rem;   /* 8px */
  --radius-lg:  0.75rem;  /* 12px */
  --radius-xl:  1rem;     /* 16px */
  --radius-2xl: 1.5rem;   /* 24px */
  --radius-full:9999px;

  /* Shadows */
  --shadow-sm:  0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md:  0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05);
  --shadow-lg:  0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.05);
  --shadow-xl:  0 20px 25px -5px rgb(0 0 0 / 0.10), 0 8px 10px -6px rgb(0 0 0 / 0.05);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.15);
  --shadow-blue: 0 4px 14px 0 rgb(79 142 247 / 0.25);
  --shadow-purple:0 4px 14px 0 rgb(139 92 246 / 0.25);

  /* Transitions */
  --transition-fast:   150ms cubic-bezier(0.4,0,0.2,1);
  --transition-base:   250ms cubic-bezier(0.4,0,0.2,1);
  --transition-slow:   400ms cubic-bezier(0.4,0,0.2,1);
  --transition-bounce: 500ms cubic-bezier(0.34,1.56,0.64,1);

  /* Z-index */
  --z-base:    0;
  --z-raised:  1;
  --z-dropdown:100;
  --z-sticky:  200;
  --z-overlay: 300;
  --z-modal:   400;
  --z-toast:   500;
  --z-tooltip: 600;
}
```

---

# APPENDIX B — INTERACTION SPEC LIBRARY

```
COMPONENT: CodePlayground
  - Monaco Editor (same as VS Code) with syntax highlighting
  - Language: SQL/Python/Bash selectable via tabs
  - Run button: execute against in-browser SQLite (SQL) or Pyodide (Python)
  - Output panel: table view for SELECT results; console for print/errors
  - Reset button: restore to lesson starter code
  - Share button: generate URL with encoded snippet
  - Autocomplete: keyword completion; table/column completion for SQL
  - Error highlighting: red underline with hover tooltip
  - Dark/light mode toggle

COMPONENT: AnimationPlayer
  - PLAY/PAUSE button (space key shortcut)
  - STEP FORWARD / STEP BACKWARD (arrow keys)
  - SPEED control: 0.5x / 1x / 2x / 4x
  - PROGRESS BAR: scrubable timeline
  - Restart button
  - Step counter: "Step 3 of 12"
  - Caption area: text description of current animation step
  - Keyboard shortcuts shown in corner

COMPONENT: KnowledgeCheck
  - Multiple choice (single or multi-select)
  - Code completion (fill in blank)
  - Drag-to-order (sort steps)
  - Match columns (draw connections)
  - After answer: explanation shown; "Why this is correct" callout
  - XP earned: +50 XP correct, +10 XP attempt
  - Retry limit: 3 attempts; reveal answer after 3rd

COMPONENT: ProgressRing
  - SVG circle with stroke-dashoffset animation
  - Center: percentage number counts up
  - Color: green 80%+, amber 50-79%, blue <50%
  - Hover: tooltip shows X/Y lessons complete

COMPONENT: StreakTracker
  - 7 circles for days of week
  - Filled = studied that day; unfilled = missed
  - Flame icon with streak count
  - "Best streak: N days" shown below
  - Daily goal: 3 ALUs minimum to count day

COMPONENT: XPBar
  - Horizontal progress bar filling current level
  - Level badge on left; next level on right
  - XP numbers: current/required
  - Level-up animation: flash, particle burst, new level badge
  - XP sources: lesson completion, quiz correct, streak bonus, challenge

COMPONENT: AchievementCard
  - Badge icon (SVG illustration per achievement)
  - Name and description
  - Progress bar if not yet earned
  - Earned date if completed
  - Rarity indicator: Common/Rare/Epic/Legendary
  - Share button: LinkedIn/Twitter share card

COMPONENT: ConceptCard
  - Front: concept name + icon
  - Back: definition + example + "how it relates to data engineering"
  - Flip animation: 3D card flip on click
  - Self-rating: "Got it" / "Almost" / "Review again" → spaced repetition queue
  - Keyboard: space to flip, 1/2/3 for rating
```

---

# APPENDIX C — FIREBASE FIRESTORE COMPLETE SCHEMA

```
/users/{uid}
  displayName: string
  email: string
  photoURL: string | null
  createdAt: timestamp
  lastSeenAt: timestamp
  currentLevel: number (1-9)
  totalXP: number
  currentStreak: number
  longestStreak: number
  lastStudyDate: string (YYYY-MM-DD)
  preferences: {
    theme: 'light' | 'dark'
    defaultSpeed: 0.5 | 1 | 2 | 4
    emailNotifications: boolean
    dailyGoal: number (ALUs per day)
  }

/users/{uid}/progress/{lessonId}
  lessonId: string
  status: 'not_started' | 'in_progress' | 'completed'
  startedAt: timestamp | null
  completedAt: timestamp | null
  xpEarned: number
  quizAttempts: number
  quizBestScore: number (0-100)
  animationProgress: number (0-100, last step reached)
  notes: string | null (user's personal notes on lesson)

/users/{uid}/bookmarks/{bookmarkId}
  lessonId: string
  lessonTitle: string
  domainColor: string
  createdAt: timestamp
  note: string | null

/users/{uid}/achievements/{achievementId}
  achievementId: string
  earnedAt: timestamp
  xpBonusEarned: number

/users/{uid}/streakLog/{dateStr}
  date: string (YYYY-MM-DD)
  alusCompleted: number
  xpEarned: number

/lessons/{lessonId}
  id: string
  title: string
  level: number (1-9)
  domain: string
  module: string
  topic: string
  subtopic: string
  subsubtopic: string
  subsubsubtopic: string
  aluText: string (the ALU content)
  estimatedMinutes: number
  xpReward: number
  prerequisites: string[] (lessonIds)
  animationSpec: string | null
  diagramSpec: string | null
  interactionSpec: string | null
  quizQuestions: [
    {
      id: string
      type: 'mcq' | 'code_fill' | 'drag_order' | 'match'
      question: string
      options: string[] | null
      correctAnswer: string | number | number[]
      explanation: string
      xpReward: number
    }
  ]
  relatedLessons: string[]
  tags: string[]
  createdAt: timestamp
  updatedAt: timestamp

/domains/{domainId}
  id: string
  name: string
  level: number
  color: string
  icon: string
  description: string
  totalLessons: number
  estimatedHours: number
  prerequisiteDomains: string[]
  certificateAvailable: boolean

Security Rules:
  match /users/{uid}/{document=**} {
    allow read, write: if request.auth != null && request.auth.uid == uid;
  }
  match /lessons/{lessonId} {
    allow read: if request.auth != null;
    allow write: if false; // admin SDK only
  }
  match /domains/{domainId} {
    allow read: if request.auth != null;
    allow write: if false;
  }
```

---

# APPENDIX D — GITHUB ACTIONS COMPLETE CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy Learn-With-Me Platform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npm run type-check

      - name: Unit tests
        run: npm run test:unit

      - name: Build
        run: npm run build
        env:
          VITE_FIREBASE_API_KEY: ${{ secrets.FIREBASE_API_KEY }}
          VITE_FIREBASE_AUTH_DOMAIN: ${{ secrets.FIREBASE_AUTH_DOMAIN }}
          VITE_FIREBASE_PROJECT_ID: ${{ secrets.FIREBASE_PROJECT_ID }}
          VITE_FIREBASE_STORAGE_BUCKET: ${{ secrets.FIREBASE_STORAGE_BUCKET }}
          VITE_FIREBASE_MESSAGING_SENDER_ID: ${{ secrets.FIREBASE_MESSAGING_SENDER_ID }}
          VITE_FIREBASE_APP_ID: ${{ secrets.FIREBASE_APP_ID }}

  deploy:
    runs-on: ubuntu-latest
    needs: validate
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
          cname: learn.dataengineer.dev  # custom domain if configured

  seed-firestore:
    runs-on: ubuntu-latest
    needs: deploy
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Seed lesson data to Firestore
        run: node scripts/seed-lessons.js
        env:
          FIREBASE_PROJECT_ID: ${{ secrets.FIREBASE_PROJECT_ID }}
          GOOGLE_APPLICATION_CREDENTIALS_JSON: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
```

---

*END OF MASTER DATA ENGINEERING LEARNING PLATFORM SPECIFICATION*

*Version: 1.0 | Generated: 2026-06-23 | Estimated Implementation: 6-12 months*
*Stack: React + TypeScript + Vite + Firebase + GitHub Pages*
*Target: Junior → Senior Azure Data Engineer + Databricks Certified Professional*

""".lstrip()

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 8 + Appendices written!")
