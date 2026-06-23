TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

content = r"""

---

# PART 6 — LEVEL 7: APACHE SPARK & PYSPARK MASTERY

**Domain Color:** `#f97316` (Orange) | **Prerequisites:** Level 6 | **Est. Hours:** 80+

---

## MODULE 7.1 — Spark Architecture

### TOPIC 7.1.1 — Spark Execution Model

**Subtopic: Cluster Architecture**
- ALU: Driver: JVM process; runs main program; creates SparkSession; submits jobs to cluster manager
- ALU: Executor: JVM process on worker node; runs tasks; stores data in memory/disk
- ALU: Cluster manager: YARN, Kubernetes, Mesos, Standalone, Databricks (custom)
- ALU: SparkContext: low-level API entry point (Spark 1.x); still used internally
- ALU: SparkSession: unified entry point (Spark 2.0+); wraps SparkContext + SQLContext + HiveContext
- ALU: SparkSession.builder.appName("name").config("key","val").getOrCreate()
- ALU: Deploy mode: client (driver on submitter machine) vs cluster (driver on cluster)
- ALU: Client mode: driver co-located with spark-submit; good for interactive
- ALU: Cluster mode: driver on cluster node; survives submitter disconnect; production

**Subtopic: Jobs, Stages, Tasks**
- ALU: Job: triggered by an action; corresponds to one DAG
- ALU: Stage: set of tasks with no shuffle boundary; within-stage = pipelined
- ALU: Shuffle: data exchange across partitions; marks stage boundary; costly
- ALU: Task: unit of work on one partition; one JVM thread; one executor slot
- ALU: Wide transformation: shuffle required; groupBy, join, repartition, distinct
- ALU: Narrow transformation: no shuffle; filter, map, select, withColumn, union
- ALU: Pipelining: multiple narrow transforms fused into one task pass
- ALU: Whole-stage code generation (WSCG): Catalyst generates bytecode for fused stages
- ALU: Stage retry: failed stage re-executed from shuffle files of previous stage
- ALU: Task retry: spark.task.maxFailures=4; task retried before stage fails

**Subtopic: Catalyst Optimizer**
- ALU: Unresolved logical plan: parsed SQL/DataFrame API → unresolved AST
- ALU: Resolved logical plan: look up catalog; resolve column references and types
- ALU: Optimized logical plan: rule-based optimizations (predicate pushdown, column pruning, constant folding)
- ALU: Predicate pushdown: move filter as close to source as possible; reduce rows early
- ALU: Column pruning: project only needed columns from scan; reduce bytes read
- ALU: Constant folding: 1+2 → 3 at compile time; WHERE date > DATE_ADD('2024-01-01', 0) → WHERE date > '2024-01-01'
- ALU: Physical plan: multiple physical strategies; cost model selects cheapest
- ALU: Broadcast hash join: small table broadcast to all executors; no shuffle
- ALU: Sort-merge join: both sides sorted and merged; default for large-large joins
- ALU: Shuffle hash join: small-ish table hashed; probe with larger side; without sorting
- ALU: Code generation: final physical plan compiled to JVM bytecode; eliminates virtual dispatch
- ALU: AQE (Adaptive Query Execution): re-plans at runtime based on shuffle statistics
- ALU: AQE: auto coalesces shuffle partitions; converts to broadcast join if size qualifies; handles skew

**ANIMATION SPEC 7.1.1 — Spark DAG:**
```
DataFrame operations shown as nodes
Arrows show data flow
Stage boundaries: dashed red lines at shuffle points
Stage 1 tasks: animate running in parallel across partitions
Shuffle: partition data streams across network to new partitions
Stage 2 tasks: run on shuffled data
Gantt chart below: task timeline per executor
AQE toggle: show pre-AQE vs post-AQE plan side by side
```

---

### TOPIC 7.1.2 — Partitioning and Shuffling

**Subtopic: Partitioning**
- ALU: Partition: fundamental unit of parallelism; one partition per task
- ALU: Default shuffle partitions: spark.sql.shuffle.partitions=200; tune for cluster
- ALU: Too many partitions: task overhead > actual work; use for large data
- ALU: Too few partitions: each task too large; spill to disk; stragglers
- ALU: Rule of thumb: 2-4 partitions per CPU core; 100-200 MB per partition after shuffle
- ALU: spark.default.parallelism: RDD API parallelism; default 2x cores
- ALU: repartition(n): full shuffle; redistributes evenly across n partitions
- ALU: repartition(n, col): shuffle by column hash; co-locates rows by key
- ALU: coalesce(n): reduce partitions without full shuffle; one-directional
- ALU: coalesce can create skewed partitions; use only to merge small partitions
- ALU: partitionBy("col") on write: write Parquet partitioned by column value

**Subtopic: Shuffle Internals**
- ALU: Map side: each task writes shuffle data to local disk; one file per reducer partition
- ALU: Index file: .index file for each shuffle data file; byte ranges per partition
- ALU: Reduce side: fetch shuffle data from multiple map tasks; deserialize and process
- ALU: Sort-shuffle: sorts map output by partition key; enables merge on reduce side
- ALU: Shuffle spill: map output too large for memory → spill to disk → merge on reduce
- ALU: spark.reducer.maxSizeInFlight: max data fetched from one reducer at a time (48MB default)
- ALU: External shuffle service: off-load shuffle data from executor memory to shuffle service
- ALU: External shuffle service: required for dynamic executor allocation (executors release early)
- ALU: Push-based shuffle: Spark 3.2+; pre-merge map output; reduces random I/O on reduce side
- ALU: Sort-merge join shuffle: both sides partitioned by join key + sorted; merge scan

**Subtopic: Data Skew**
- ALU: Skew: one partition has significantly more data than others; straggler task
- ALU: Detect skew: Spark UI tasks tab; sort by duration; identify outlier long tasks
- ALU: Cause: hotspot key (e.g., NULL values all in one partition; popular user ID)
- ALU: Salting: append random suffix to skewed key; join with exploded suffix on other side
- ALU: Broadcast hint: BROADCAST(small_table); skips join shuffle entirely
- ALU: AQE skew handling: spark.sql.adaptive.skewJoin.enabled=true; splits skewed partitions
- ALU: AQE skew threshold: spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes=256MB
- ALU: Isolation: process skewed keys separately; union with non-skewed results

**ANIMATION SPEC 7.1.2 — Shuffle Visualization:**
```
Left side: 4 map tasks with data bars
Shuffle lines: colored by destination partition; cross-hatch pattern
Right side: 4 reduce partitions receiving data from all maps
Skew demo: one key dominates; one reduce partition bar much taller
Salting fix: key+random suffix; data redistributes evenly
Task completion timeline: skewed vs salted comparison
```

---

### TOPIC 7.1.3 — Memory Management

**Subtopic: Unified Memory Manager**
- ALU: Executor JVM heap: -Xmx based on spark.executor.memory
- ALU: Reserved memory: 300MB fixed; JVM overhead
- ALU: Usable memory: executor.memory - 300MB
- ALU: spark.memory.fraction (default 0.6): fraction of usable memory for Spark
- ALU: Execution memory: shuffle, sort, aggregation buffers; dynamic size
- ALU: Storage memory: RDD/DataFrame cache; dynamic size; evicts on memory pressure
- ALU: User memory (1 - fraction = 0.4): user data structures, UDFs, libraries
- ALU: spark.memory.storageFraction (default 0.5): storage gets 50% of Spark memory pool
- ALU: Dynamic occupancy: execution can borrow from storage (evicts cache); storage cannot evict execution
- ALU: Off-heap memory: spark.memory.offHeap.enabled=true; spark.memory.offHeap.size
- ALU: Off-heap benefits: no GC pressure; faster for large datasets; Arrow format
- ALU: Overhead: spark.executor.memoryOverhead = max(384MB, 10% executor memory); JVM overhead, Python worker

**Subtopic: GC Tuning**
- ALU: G1GC recommended: -XX:+UseG1GC; handles mixed young/old collection; lower pause
- ALU: GC pause = task stall; Spark UI shows GC time per task
- ALU: High GC time (>30% task time): reduce data structures in User memory; reduce executor memory per core
- ALU: GC log: -Xloggc:/tmp/gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps
- ALU: Eden size: -XX:G1NewSizePercent=20; larger Eden reduces minor GC frequency
- ALU: spark.cleaner.referenceTracking: true; clean broadcast/shuffle files via weak references

**Subtopic: Caching and Persistence**
- ALU: df.cache(): store in memory with MEMORY_AND_DISK; lazy (first action triggers computation)
- ALU: df.persist(StorageLevel.MEMORY_ONLY): fail on OOM (no disk fallback)
- ALU: df.persist(StorageLevel.MEMORY_AND_DISK): spill to disk if OOM
- ALU: df.persist(StorageLevel.DISK_ONLY): disk only; slower but no memory pressure
- ALU: df.persist(StorageLevel.MEMORY_AND_DISK_SER): serialized rows; less memory; more CPU
- ALU: df.unpersist(): explicitly free cache; important in loop-based processing
- ALU: Broadcast variable: bc = spark.sparkContext.broadcast(large_dict); avoid resending per task
- ALU: Accumulator: distributed counter/sum; accum = spark.sparkContext.accumulator(0)
- ALU: When to cache: DataFrame reused 2+ times in same job; expensive computation

---

## MODULE 7.2 — PySpark Complete API

### TOPIC 7.2.1 — DataFrame Operations

**Subtopic: Creating DataFrames**
- ALU: spark.read.parquet/csv/json/orc/delta/jdbc/format() + .load(path)
- ALU: spark.createDataFrame(pandas_df): from pandas; small data only
- ALU: spark.createDataFrame(rows, schema): from list of Row/tuple + StructType
- ALU: StructType([StructField("name", StringType(), nullable=True)]): explicit schema
- ALU: spark.read.schema(schema).parquet(path): enforce schema on read; no schema inference
- ALU: spark.table("catalog.schema.table"): read registered table or view

**Subtopic: Transformations Reference**
- ALU: select(*cols): project columns; supports string names or Column expressions
- ALU: selectExpr("col1", "col2 + 1 as col3"): SQL expressions in select
- ALU: filter(condition) / where(condition): filter rows; Column expression or SQL string
- ALU: withColumn(name, expr): add or replace column
- ALU: withColumnRenamed(old, new): rename column
- ALU: drop(*cols): remove columns
- ALU: distinct(): deduplicate rows
- ALU: dropDuplicates([cols]): dedup on subset of columns
- ALU: orderBy(*cols, ascending=True): global sort; requires shuffle; expensive
- ALU: sort(*cols): alias for orderBy
- ALU: limit(n): take first n rows after sort; requires action to materialize
- ALU: union(other): combine schemas must match; UNION ALL semantics
- ALU: unionByName(other, allowMissingColumns=True): match by name not position
- ALU: sample(fraction, seed): random sample; withReplacement=False default
- ALU: randomSplit([0.8, 0.2], seed): split into train/test DataFrames

**Subtopic: Column Expressions**
- ALU: col("name") / df["name"] / df.name: column reference
- ALU: lit(value): literal value as Column
- ALU: col("a") + col("b"): arithmetic; also -, *, /, %
- ALU: col("a").cast(IntegerType()): type cast
- ALU: col("a").alias("new_name"): rename
- ALU: col("a").isNull() / isNotNull() / isnan(): null checks
- ALU: col("a").isin(list): membership test
- ALU: when(condition, value).otherwise(default): CASE equivalent
- ALU: coalesce(col("a"), col("b"), lit(0)): first non-null
- ALU: array(col("a"), col("b")): create array column
- ALU: struct(col("a"), col("b")): create struct column
- ALU: col("struct.field"): access struct field
- ALU: col("array")[0]: index array
- ALU: col("map")["key"]: map lookup

**Subtopic: Functions Library**
- ALU: from pyspark.sql import functions as F
- ALU: F.count, F.sum, F.avg, F.min, F.max, F.stddev, F.variance, F.collect_list, F.collect_set
- ALU: F.concat, F.concat_ws, F.split, F.regexp_replace, F.regexp_extract, F.substring, F.trim, F.upper, F.lower
- ALU: F.to_date, F.to_timestamp, F.date_add, F.date_sub, F.datediff, F.date_trunc, F.year, F.month, F.dayofmonth, F.hour, F.minute
- ALU: F.from_unixtime, F.unix_timestamp, F.current_timestamp, F.current_date
- ALU: F.row_number, F.rank, F.dense_rank, F.lag, F.lead, F.first, F.last, F.ntile, F.percent_rank
- ALU: F.explode(col): one row per array element; null arrays = 0 rows
- ALU: F.explode_outer(col): null arrays = one row with null
- ALU: F.posexplode(col): includes position index
- ALU: F.flatten(col): flatten nested array one level
- ALU: F.array_contains, F.array_distinct, F.array_except, F.array_intersect, F.array_union, F.array_size
- ALU: F.map_keys, F.map_values, F.map_from_arrays, F.map_concat, F.element_at
- ALU: F.struct, F.array, F.create_map
- ALU: F.get_json_object(col, "$.field"): extract JSON field from string
- ALU: F.from_json(col, schema): parse JSON string to struct/array
- ALU: F.to_json(col): convert struct/array to JSON string
- ALU: F.schema_of_json(json_string): infer schema from sample JSON string
- ALU: F.sha2(col, 256): SHA-256 hash; F.md5(col): MD5 hash
- ALU: F.hash(col): deterministic hash for bucketing
- ALU: F.rand(seed): random float 0-1; F.randn(seed): random normal

**Subtopic: Aggregations**
- ALU: df.groupBy("col").agg(F.sum("amount").alias("total"))
- ALU: Multiple aggs: .agg(F.sum("a"), F.avg("b"), F.count("*"))
- ALU: groupBy with Window: use Window.partitionBy not groupBy for window functions
- ALU: cube(*cols): all combinations including totals
- ALU: rollup(*cols): hierarchical subtotals
- ALU: pivot(col, values): values become columns
- ALU: df.groupBy("dept").pivot("year", [2022,2023,2024]).sum("revenue")

**Subtopic: Joins**
- ALU: df.join(other, on, how): how = inner/left/right/full/left_semi/left_anti/cross
- ALU: on = column name string: equality on same-named column; keeps one copy
- ALU: on = list of columns: multiple equality conditions
- ALU: on = condition: df.col == other.col; keeps both columns (may have duplicate names)
- ALU: left_semi: keep left rows where match exists in right; no right columns in output
- ALU: left_anti: keep left rows with NO match in right
- ALU: Broadcast hint: F.broadcast(small_df) or /*+ BROADCAST(t) */ in SQL
- ALU: spark.sql.autoBroadcastJoinThreshold: default 10MB; set -1 to disable
- ALU: Avoid joining on nullable columns without is_not_null filter; NULLs never match

**ANIMATION SPEC 7.2.1 — DataFrame Operations:**
```
Live DataFrame rendered as table
User selects operation from menu
filter: non-matching rows animate fading out with red overlay
groupBy+agg: rows animate grouping into clusters; aggregate value appears
join: two tables shown; matching rows draw connection lines; result builds below
explode: array cell expands into multiple rows with bounce animation
window function: partition brackets shown; rank numbers appear per row
```

---

### TOPIC 7.2.2 — UDFs and Performance

**Subtopic: Python UDFs**
- ALU: @udf(returnType=StringType()): register function as UDF
- ALU: Python UDF overhead: serialize/deserialize rows via Pickle; JVM→Python→JVM per row
- ALU: Python UDF cost: 100x slower than native Spark functions
- ALU: Always prefer built-in Spark functions; use UDF only when no built-in exists
- ALU: pandas_udf (Vectorized UDF): uses Apache Arrow; 10-100x faster than Python UDF
- ALU: @pandas_udf(returnType, functionType): function receives pandas Series or DataFrame
- ALU: SCALAR pandas_udf: one pandas Series → one pandas Series; row-by-row vectorized
- ALU: GROUPED_MAP pandas_udf: one group as pandas DataFrame → pandas DataFrame
- ALU: GROUPED_AGG pandas_udf: one group as pandas Series → scalar
- ALU: Spark 3.x pandas_udf simplified: just annotate with return type; no PandasUDFType

**Subtopic: Spark SQL Functions vs UDF Performance**
- ALU: Catalyst cannot optimize UDFs: treated as black box; no predicate pushdown inside
- ALU: Native functions: Catalyst + Tungsten + WSCG; optimal JVM bytecode generated
- ALU: Profile first: Spark UI → SQL → Physical Plan → look for Python UDF nodes
- ALU: Higher-order functions (HOF): transform_values, filter, aggregate, exists, forall on arrays without UDF

**Subtopic: Spark SQL**
- ALU: spark.sql("SELECT ...FROM ...WHERE ..."): execute SQL directly
- ALU: createOrReplaceTempView("name"): register df as SQL-queryable view; session scope
- ALU: createOrReplaceGlobalTempView("name"): global_temp.name; cross-session
- ALU: SQL and DataFrame API: identical semantics; same optimizer; interchangeable
- ALU: spark.catalog.listTables(): list registered tables and views
- ALU: spark.catalog.cacheTable("name"): cache via Spark SQL
- ALU: Spark SQL supports: CTE, window functions, MERGE, LATERAL VIEW, ROLLUP, CUBE, pivot

---

### TOPIC 7.2.3 — Streaming with Spark

**Subtopic: Structured Streaming Model**
- ALU: Treat stream as unbounded table; new rows append as data arrives
- ALU: Micro-batch: collect N seconds of data; process as batch; default mode
- ALU: Continuous processing: experimental; sub-millisecond latency; limited operations
- ALU: Trigger modes: default (ASAP after previous), fixed interval, once, available-now
- ALU: Output modes: append (only new rows), complete (full result table), update (changed rows)
- ALU: Watermark: maximum event time lag tolerated; df.withWatermark("timestamp", "10 minutes")
- ALU: Late data: data arriving after watermark dropped from state; tradeoff latency vs completeness
- ALU: State store: stores aggregation state per key; RocksDB or in-memory

**Subtopic: Sources and Sinks**
- ALU: Kafka source: spark.readStream.format("kafka").option("kafka.bootstrap.servers", ...).option("subscribe", "topic")
- ALU: Kafka columns: key (binary), value (binary), topic, partition, offset, timestamp, timestampType
- ALU: Delta source: spark.readStream.format("delta").load(path): reads Delta change feed
- ALU: Rate source: generate test data; rows/second; for development/testing
- ALU: File source: monitors directory; picks up new files; CSV/JSON/Parquet/Avro
- ALU: Kafka sink: .writeStream.format("kafka").option("topic", "output").start()
- ALU: Delta sink: .writeStream.format("delta").outputMode("append").option("checkpointLocation", path).start(path)
- ALU: Console sink: for testing; prints micro-batch output to console
- ALU: foreachBatch: apply arbitrary DataFrame operations per micro-batch; most flexible sink
- ALU: foreach: apply function per row; less efficient than foreachBatch

**Subtopic: Checkpoint and Fault Tolerance**
- ALU: Checkpoint: write-ahead log of offsets + state to ADLS/HDFS; exactly-once guarantee
- ALU: checkpoint location: must be persistent; cannot reuse across different queries
- ALU: Restart: reads checkpoint; restores offsets; re-processes from last committed offset
- ALU: Schema evolution in streaming: Delta + streaming; new columns auto-handled with mergeSchema
- ALU: Query termination: query.awaitTermination(); query.stop(); query.exception()
- ALU: Multiple streaming queries: SparkSession can run N concurrent streaming queries

**ANIMATION SPEC 7.2.3 — Structured Streaming:**
```
Event timeline: events arriving with timestamps
Watermark line: moves right as time advances
Micro-batch boundary: dashed vertical lines every 30s
Late event: arrives after watermark; shown in gray; dropped from state
Window aggregation: 5-minute windows shown as rectangles
Final result: event counts per window animate updating
State store: keys shown with running counts; state evicted past watermark
```

---

## MODULE 7.3 — Performance Engineering

### TOPIC 7.3.1 — Spark Tuning Reference

**Subtopic: Resource Configuration**
- ALU: spark.executor.cores: typically 4-5 for HDFS; 2 for I/O-bound; higher for in-memory
- ALU: spark.executor.memory: depends on data; start 8GB per executor; tune by GC/spill
- ALU: spark.executor.memoryOverhead: 10% executor memory minimum; Python: extra overhead
- ALU: spark.driver.memory: enough for collect() results + broadcast tables
- ALU: spark.dynamicAllocation.enabled: true; scale executors based on task queue
- ALU: spark.dynamicAllocation.minExecutors / maxExecutors / initialExecutors
- ALU: Dynamic allocation requires external shuffle service (retains shuffle data after executor removed)

**Subtopic: Query Tuning**
- ALU: Explain plan: df.explain(mode="extended") or df.explain(True)
- ALU: Mode "formatted": most readable; shows each operator in detail
- ALU: Look for: BroadcastHashJoin (good for small table), SortMergeJoin (large+large), HashAggregate
- ALU: FileScan: check pushed filters; "PushedFilters: [IsNotNull, GreaterThan]" means pushdown working
- ALU: Exchange (shuffle): note estimated bytes; large shuffle = opportunity to reduce
- ALU: SparkUI SQL tab: physical plan with runtime metrics; hover nodes for details
- ALU: Spill metrics: "bytes spilled to disk" in task metrics; increase executor memory or reduce partitions
- ALU: Skew indicators: one task 10x slower than others in same stage

**Subtopic: AQE Tuning**
- ALU: spark.sql.adaptive.enabled=true (default Spark 3.2+)
- ALU: spark.sql.adaptive.coalescePartitions.enabled=true: merge small post-shuffle partitions
- ALU: spark.sql.adaptive.coalescePartitions.minPartitionSize=1MB: minimum merged size
- ALU: spark.sql.adaptive.advisoryPartitionSizeInBytes=64MB: target partition size
- ALU: spark.sql.adaptive.skewJoin.enabled=true: split skewed partitions
- ALU: AQE limitations: cannot help pre-shuffle operations; cannot fix bad data distribution

**Subtopic: File Optimization**
- ALU: Target file size: 128MB-1GB Parquet files for Spark reads (matches row group default)
- ALU: Small files: coalesce/repartition before write; or OPTIMIZE in Delta Lake
- ALU: Z-ordering: sort data by frequently-filtered columns in Parquet; improves range scan
- ALU: Delta OPTIMIZE + ZORDER: compacts + Z-orders in one operation
- ALU: Bloom filters: per-column Parquet/Delta bloom filter; faster point lookups
- ALU: maxFilesPerTrigger / maxBytesPerTrigger: control streaming batch size from Delta source

""".lstrip()

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 6 written!")
