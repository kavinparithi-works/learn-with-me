TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

content = r"""

---

# PART 5 — LEVEL 6: CLOUD & AZURE FUNDAMENTALS TO EXPERT

**Domain Color:** `#0ea5e9` (Sky Blue) | **Prerequisites:** Level 5 | **Est. Hours:** 80+

---

## MODULE 6.1 — Cloud Computing Fundamentals

### TOPIC 6.1.1 — Cloud Models and Service Tiers

- ALU: IaaS: Infrastructure as a Service; you manage OS, runtime, data; cloud manages hardware/network/virtualization
- ALU: PaaS: Platform as a Service; you manage code and data; cloud manages OS, runtime, scaling
- ALU: SaaS: Software as a Service; cloud manages everything; you just use the application
- ALU: Shared responsibility model: security responsibilities split between cloud provider and customer
- ALU: Cloud provider owns: physical security, hypervisor, network infrastructure, storage hardware
- ALU: Customer owns: identity management, data classification, application security, OS patching (IaaS)
- ALU: Public cloud: shared physical infrastructure; isolated by virtualization; Azure/AWS/GCP
- ALU: Private cloud: dedicated infrastructure; higher cost; regulatory requirements
- ALU: Hybrid cloud: on-premises + public cloud connected; Azure Arc; Azure VPN Gateway
- ALU: Multi-cloud: workloads across Azure + AWS or GCP; vendor lock-in mitigation

**Subtopic: Azure Regions and Availability**
- ALU: Azure region: geographic area containing one or more datacenters; 60+ regions globally
- ALU: Region pair: each region paired with another in same geography for DR; 300+ miles apart
- ALU: Availability Zone: physically separate datacenter within a region; independent power/cooling/network
- ALU: Zone-redundant: service spans multiple AZs; survives single AZ failure
- ALU: Locally redundant (LRS): 3 copies within single datacenter; protects hardware failure
- ALU: Zone-redundant storage (ZRS): 3 copies across AZs; survives AZ failure
- ALU: Geo-redundant storage (GRS): LRS in primary + LRS in paired region; survives region outage
- ALU: Geo-zone-redundant (GZRS): ZRS in primary + LRS in paired region; highest durability
- ALU: SLA: Azure Storage 99.9% read; 99.99% with RA-GRS; measured monthly per service
- ALU: Azure Sovereign: Azure Government (US), Azure China (21Vianet operated), Azure Germany

**ANIMATION SPEC 6.1.1 — Azure Global Infrastructure:**
```
World map showing Azure regions as dots
Click region: show AZs as inner circles
Replication arrows: LRS within DC, ZRS across AZs, GRS across regions
Failure simulation: fade one AZ; show data still available from others
```

---

## MODULE 6.2 — Azure Core Services

### TOPIC 6.2.1 — Azure Storage Complete

**Subtopic: Blob Storage**
- ALU: Blob = Binary Large Object; object storage for unstructured data
- ALU: Account → Container → Blob (3-level hierarchy)
- ALU: Blob types: Block blob (up to 190.7 TB; file data); Append blob (logs); Page blob (VHD/disks)
- ALU: Block blob: composed of blocks (max 4000 MB each); max 50,000 blocks = 190.7 TB
- ALU: Access tiers: Hot (frequent access; highest storage cost), Cool (infrequent; 30-day min), Cold (90-day min), Archive (offline; 180-day min; hours to rehydrate)
- ALU: Lifecycle management: auto-tier or delete blobs based on age/last-modified rules
- ALU: Soft delete: recover deleted blobs within retention period (1-365 days)
- ALU: Versioning: auto-create version on every blob write; point-in-time restore
- ALU: Snapshots: read-only point-in-time copy of blob; parent-child relationship
- ALU: Immutable storage: WORM (Write Once Read Many); compliance requirement
- ALU: Static website hosting: serve HTML/JS/CSS from $web container; no compute needed
- ALU: CDN integration: Azure Front Door / CDN for global caching
- ALU: Public access levels: Private (auth required), Blob (public read), Container (list + read)

**Subtopic: ADLS Gen2**
- ALU: Azure Data Lake Storage Gen2: Blob Storage + Hierarchical Namespace (HNS) enabled
- ALU: HNS: directories are first-class objects; atomic rename/delete of directories
- ALU: Why HNS matters: Hive/Spark partitioning patterns rely on atomic directory rename for commit
- ALU: Without HNS: rename = copy all blobs + delete originals (not atomic; partial failure risk)
- ALU: ADLS Gen2 protocol: ABFS driver (abfs://container@account.dfs.core.windows.net/path)
- ALU: WASB driver (wasbs://): older Blob driver; not recommended for ADLS Gen2
- ALU: Access control: Azure RBAC (coarse-grained) + POSIX ACLs (fine-grained per path)
- ALU: Storage Blob Data Contributor: read/write/delete blobs (no ACL management)
- ALU: Storage Blob Data Owner: full access including setting ACLs
- ALU: Service principal + OAuth: recommended auth for Databricks/ADF
- ALU: SAS token: Shared Access Signature; time-limited URL with encoded permissions
- ALU: Account key: master key; full access; do not use in production code
- ALU: Performance: optimize file size 256MB–1GB; avoid small files problem
- ALU: Small files problem: millions of files <1MB; Spark task overhead dominates
- ALU: Compaction: periodically merge small files; Delta Lake OPTIMIZE handles this

**Subtopic: Azure Files**
- ALU: Fully managed SMB and NFS file shares in cloud
- ALU: SMB 3.0: Windows/Linux mount; drive letter mapped
- ALU: NFS 4.1: Linux mount; requires premium tier
- ALU: Azure File Sync: replicate on-premises Windows file servers to Azure Files
- ALU: Use cases: lift-and-shift legacy apps; shared config files; home directories

**Subtopic: Azure Queue and Table Storage**
- ALU: Queue Storage: simple messaging; 64 KB per message; 7-day TTL default
- ALU: Table Storage: key-value NoSQL; PartitionKey + RowKey; no joins; cheap
- ALU: Table Storage alternative: Azure Cosmos DB for Table API (same API, more features)

---

### TOPIC 6.2.2 — Azure Networking

**Subtopic: Virtual Network (VNet)**
- ALU: VNet: isolated network boundary in Azure; assign address space (CIDR blocks)
- ALU: Subnet: segment of VNet address space; place resources in subnets
- ALU: Network Security Group (NSG): stateful firewall rules; allow/deny by source IP/port/protocol
- ALU: NSG on subnet: applies to all resources in subnet
- ALU: NSG on NIC: applies to specific VM NIC
- ALU: Application Security Group (ASG): logical grouping of NICs; reference in NSG rules
- ALU: Route table (UDR): override default system routes; force traffic through NVA or VPN
- ALU: VNet peering: connect two VNets; low latency; uses Azure backbone
- ALU: Global VNet peering: across regions; slightly higher latency
- ALU: Transit routing: peering is not transitive by default; hub-spoke requires route tables
- ALU: VPN Gateway: site-to-site IPsec VPN to on-premises; max 1 Gbps per tunnel (policy-based)
- ALU: ExpressRoute: private dedicated circuit to Azure; up to 100 Gbps; no public internet traversal
- ALU: Azure Bastion: browser-based RDP/SSH to VMs without public IP; secure jump host

**Subtopic: Private Endpoints**
- ALU: Private endpoint: NIC with private IP in VNet for Azure PaaS service
- ALU: Private DNS zone: resolves service FQDN to private IP within VNet
- ALU: Traffic to storage.core.windows.net stays on private network; never crosses internet
- ALU: Databricks cluster to ADLS: use private endpoint to avoid public internet data transfer
- ALU: Azure SQL, Cosmos DB, Event Hub, Key Vault: all support private endpoints
- ALU: Service endpoint: older alternative; routes traffic via Azure backbone but uses public IP
- ALU: Private endpoint vs service endpoint: private endpoint preferred; NIC in VNet; true private IP

**Subtopic: Azure DNS**
- ALU: Azure DNS: host DNS zones in Azure; public or private zones
- ALU: Private DNS zone: name resolution within VNet; linked to VNet
- ALU: DNS resolver: inbound/outbound endpoints for hybrid DNS scenarios
- ALU: Custom DNS server: point VNet to custom resolver for conditional forwarding

---

### TOPIC 6.2.3 — Azure Identity and Security

**Subtopic: Azure Active Directory (Entra ID)**
- ALU: Azure AD (now Entra ID): cloud identity service; users, groups, service principals, managed identities
- ALU: Tenant: dedicated instance of Azure AD; represents organization; identified by tenant ID
- ALU: Service principal: application identity; client ID + client secret or certificate
- ALU: Managed identity: system-managed service principal; no credentials to store or rotate
- ALU: System-assigned managed identity: tied to resource lifecycle; deleted with resource
- ALU: User-assigned managed identity: independent lifecycle; reusable across resources
- ALU: RBAC: Role-Based Access Control; principal + role + scope
- ALU: Scope hierarchy: Management Group → Subscription → Resource Group → Resource
- ALU: Built-in roles: Owner, Contributor, Reader, Storage Blob Data Contributor, etc.
- ALU: Custom roles: JSON definition with actions/notActions/dataActions/notDataActions
- ALU: Conditional Access: enforce MFA/compliant device based on risk signals
- ALU: PIM (Privileged Identity Management): just-in-time privileged role activation

**Subtopic: Azure Key Vault**
- ALU: Key Vault: managed secrets, keys, and certificates store
- ALU: Secret: named opaque value with version; connection strings, API keys, passwords
- ALU: Key: RSA or EC key; operations: encrypt, decrypt, sign, verify, wrapKey, unwrapKey
- ALU: Certificate: manages TLS certificate lifecycle; auto-renew integration
- ALU: Access policies (legacy): per-principal get/list/set/delete permissions on secrets
- ALU: RBAC mode (preferred): standard Azure RBAC on Key Vault plane
- ALU: Soft delete + purge protection: required for compliance; prevents permanent deletion
- ALU: Key Vault references: App Service / Functions / Databricks secret scopes reference KV directly
- ALU: Databricks secret scope backed by Key Vault: dbutils.secrets.get('scope', 'key')
- ALU: AKV firewall: restrict access to specific VNet subnets or IP ranges
- ALU: HSM-backed keys: FIPS 140-2 Level 3; more expensive; compliance requirements

**Subtopic: Azure Policy**
- ALU: Azure Policy: enforce organizational standards; audit or deny non-compliant resources
- ALU: Policy definition: rule + effect (Deny, Audit, Append, Modify, DeployIfNotExists)
- ALU: Initiative: collection of related policies; assign as unit
- ALU: Compliance dashboard: shows compliant vs non-compliant resources
- ALU: Built-in policies: hundreds of pre-defined policies; require tags, allowed locations, SKU restrictions
- ALU: Custom policy JSON: conditions + effect; support aliases for resource properties
- ALU: Deny effect: prevents non-compliant resource creation
- ALU: DeployIfNotExists: auto-remediate by deploying missing resource (e.g., enable diagnostics)

---

### TOPIC 6.2.4 — Azure SQL Family

**Subtopic: Azure SQL Database**
- ALU: Fully managed SQL Server engine; PaaS; no OS/patching responsibility
- ALU: DTU model: blended CPU/memory/IO units; Simple; less flexible
- ALU: vCore model: choose vCores, memory, storage independently; preferred
- ALU: Service tiers: General Purpose (remote storage), Business Critical (local SSD, read replicas), Hyperscale (up to 100TB, rapid scale)
- ALU: Serverless: auto-pause when idle; billing per second; cold start latency
- ALU: Elastic Pool: share DTUs/vCores across multiple databases; cost-efficient for multi-tenant
- ALU: Geo-replication: up to 4 read replicas in different regions; failover groups for auto-failover
- ALU: Long-term backup retention: weekly/monthly backups up to 10 years
- ALU: Point-in-time restore: any point in last 7-35 days
- ALU: Always Encrypted: client-side encryption; DB server never sees plaintext
- ALU: Transparent Data Encryption (TDE): at-rest encryption; on by default
- ALU: Advanced Threat Protection: SQL injection detection, anomalous access alerts

**Subtopic: Azure SQL Managed Instance**
- ALU: Near 100% SQL Server compatibility; VNet-injected; no public endpoint by default
- ALU: Support for SQL Agent, linked servers, CLR, Service Broker, SSRS/SSAS
- ALU: Lift-and-shift for on-premises SQL Server with minimal code changes
- ALU: Instance Pool: multiple MIs share compute; cost reduction
- ALU: Business Critical tier: local SSD; built-in read replica; 3 nodes Always On

**Subtopic: Azure Synapse Analytics (SQL Pools)**
- ALU: Dedicated SQL pool: MPP (Massively Parallel Processing); formerly SQL DW
- ALU: Distribution: HASH (evenly distribute by column), ROUND_ROBIN, REPLICATE (small dims)
- ALU: HASH distribution: choose column with high cardinality used in most joins
- ALU: Data skew: one distribution has disproportionate data; DBCC PDW_SHOWSPACEUSED
- ALU: Control node: receives queries; generates distributed plan
- ALU: Compute nodes: 60 distributions across N nodes (DW100c → DW30000c)
- ALU: Data movement service (DMS): shuffle data between distributions for joins
- ALU: Clustered columnstore index: default; excellent compression + vectorized scan
- ALU: Result set cache: cache query results for 48 hrs; repeated identical queries instant
- ALU: Workload groups: resource isolation by group; resource_pool pattern
- ALU: Pause/resume: stop billing for compute when idle; storage billed continuously
- ALU: Serverless SQL pool: pay-per-query; query ADLS files directly with T-SQL
- ALU: OPENROWSET: query Parquet/CSV/Delta from Synapse serverless without loading
- ALU: External table: schema over ADLS file; query via SQL without data movement

---

## MODULE 6.3 — Azure Data Factory (ADF)

### TOPIC 6.3.1 — ADF Architecture

**Subtopic: Core Components**
- ALU: Pipeline: logical grouping of activities; unit of execution
- ALU: Activity: single step; Data movement (Copy), Data transformation (Databricks/HDInsight/Synapse), Control flow
- ALU: Dataset: named reference to data store with schema definition
- ALU: Linked service: connection definition to data store or compute (credentials, URL)
- ALU: Integration Runtime (IR): execution engine where activities run
- ALU: Azure IR: serverless; managed by Microsoft; for cloud-to-cloud pipelines
- ALU: Self-hosted IR (SHIR): installed on on-premises or IaaS VM; access private networks
- ALU: Azure-SSIS IR: lift-and-shift SSIS packages to cloud
- ALU: Triggers: schedule, tumbling window, event-based (blob arrival), manual
- ALU: Parameters: pipeline and dataset parameters for reusability
- ALU: Variables: pipeline-scope variables; set with Set Variable activity
- ALU: Global parameters: workspace-level constants; promote from dev to prod

**Subtopic: Copy Activity Deep Dive**
- ALU: Source connectors: 90+ connectors (SQL Server, Oracle, SAP, Salesforce, REST, ADLS, S3, etc.)
- ALU: Sink connectors: Parquet, Delta, SQL, Synapse, Cosmos DB, etc.
- ALU: Mapping: column-to-column; computed columns; type conversions
- ALU: Data flow integration: Copy followed by Mapping Data Flow for transformations
- ALU: Parallel copy: parallelism degree; partitioned reads (physical/logical/dynamic range)
- ALU: Staged copy: use Azure Blob as staging area; PolyBase bulk load for SQL DW sink
- ALU: Fault tolerance: skip/log incompatible rows; continue on data consistency error
- ALU: Binary copy: pass-through without deserialization; fastest for file migration

**Subtopic: Control Flow Activities**
- ALU: If Condition: branch on expression
- ALU: Switch: multi-branch on expression value
- ALU: ForEach: iterate over array; sequential or parallel; parallelism degree 1-50
- ALU: Until: loop until condition true; timeout setting essential
- ALU: Wait: pause pipeline execution for N seconds
- ALU: Execute Pipeline: invoke child pipeline; synchronous or asynchronous
- ALU: Web Activity: HTTP call to REST API; parse response for subsequent activities
- ALU: Lookup Activity: read from dataset; returns rows as pipeline variable
- ALU: Get Metadata Activity: check file existence, size, structure
- ALU: Delete Activity: delete files/blobs; use with validation before delete
- ALU: Fail Activity: explicitly fail pipeline with custom message and error code
- ALU: Set Variable: assign expression result to variable
- ALU: Append Variable: add item to array variable

**Subtopic: Mapping Data Flows**
- ALU: Visual ETL; runs on Databricks cluster automatically provisioned
- ALU: Source → transformation chain → sink; each node is a visual operator
- ALU: Transformations: Filter, Select, Derived Column, Aggregate, Join, Lookup, Conditional Split, Union, Pivot, Unpivot, Sort, Window, Rank, Exists, Alter Row, Flatten, Parse, Stringify
- ALU: Derived column: define expressions using Data Flow expression language
- ALU: Alter Row: set INSERT/UPDATE/DELETE/UPSERT policy per row; required for DML sink
- ALU: Schema drift: allow source schema changes to flow through automatically
- ALU: Data flow debug: interactive test with sample data; no prod cluster needed
- ALU: Debug TTL: keep debug cluster alive for N minutes; cost consideration
- ALU: Parameterize: dataset, source, sink, expressions all parameterizable
- ALU: Cluster type: general purpose vs memory-optimized; node count; core count

**ANIMATION SPEC 6.3.1 — ADF Pipeline Execution:**
```
Pipeline canvas: activities as nodes connected by arrows
Run trigger fires: pipeline highlighted
Activities execute in order with status badges (running=blue, success=green, failed=red)
ForEach: expands to show N parallel iterations with progress
Copy activity: source icon → animated data stream → sink icon
Data bytes counter updates live
Duration per activity shown as horizontal bar
Retry indicator: activity fails, retries with backoff
```

---

## MODULE 6.4 — Azure Cosmos DB

### TOPIC 6.4.1 — Cosmos DB Architecture

**Subtopic: Core Concepts**
- ALU: Globally distributed; multi-model; multiple APIs (NoSQL, MongoDB, Cassandra, Gremlin, Table, PostgreSQL)
- ALU: Account → Database → Container → Item
- ALU: Container: schema-agnostic; partition key defines partitioning
- ALU: Logical partition: all items with same partition key; max 20 GB per logical partition
- ALU: Physical partition: one or more logical partitions; 10 GB max; 10,000 RU/s max
- ALU: Request Unit (RU): normalized throughput unit; 1 RU = 1KB point read
- ALU: Provisioned throughput: fixed RU/s; pay regardless of usage
- ALU: Autoscale: max RU/s defined; scales 10%-100% dynamically; higher cost/RU
- ALU: Serverless: per-RU billing; good for sporadic workloads; max 5000 RU/s burst
- ALU: 1 KB point read = 1 RU; 1 KB write = ~5 RU; cross-partition query = many RU

**Subtopic: Partition Key Strategy**
- ALU: Partition key choice is critical; cannot be changed after container creation
- ALU: Good partition key: high cardinality, evenly distributed writes, included in most queries
- ALU: Hot partition: one key has disproportionate traffic; throttling on that key
- ALU: Synthetic partition key: combine two fields (userId + month) for even distribution
- ALU: Hierarchical partition keys: up to 3 levels; further sub-partition logical partitions

**Subtopic: Consistency Levels**
- ALU: Strong: linearizability; reads always see latest write; highest latency; single-region or read same region
- ALU: Bounded staleness: reads lag writes by K versions or T time; globally; second-lowest latency
- ALU: Session (default): consistent within client session; reads own writes; most practical
- ALU: Consistent prefix: never see out-of-order writes; no staleness guarantee
- ALU: Eventual: lowest latency; lowest cost; temporary divergence between replicas
- ALU: SLA guarantees: bounded staleness and strong have tighter SLAs for staleness

**Subtopic: Change Feed**
- ALU: Ordered log of all inserts and updates per partition key; immutable; no deletes*
- ALU: Delete mode: soft delete + TTL trick; or enable preview delete change feed
- ALU: Change feed processor: library; distributed lease-based consumption; auto-scale
- ALU: Pull model: explicit page fetching; simpler; single consumer
- ALU: Azure Functions trigger: event-driven processing of change feed items
- ALU: ADF change feed source: read incremental changes in Copy activity
- ALU: Use cases: event sourcing, real-time analytics, cache invalidation, downstream replication

---

## MODULE 6.5 — Azure Event Hub

### TOPIC 6.5.1 — Event Hub Architecture

**Subtopic: Core Concepts**
- ALU: Event Hub: managed event streaming service; Kafka-compatible protocol
- ALU: Namespace → Event Hub → Consumer Group → Partition
- ALU: Partition: ordered sequence of events; immutable log; retention up to 90 days
- ALU: Partition count: set at creation; cannot be reduced; throughput unit scales with partitions
- ALU: Throughput unit (TU): 1 MB/s ingress + 2 MB/s egress; scale 1-40 TU (standard)
- ALU: Premium tier: CUs (Capacity Units); higher limits; dedicated resources
- ALU: Consumer group: independent view of the event stream; separate offset per group
- ALU: Offset: position within partition; committed by consumer; auto-offset reset policy
- ALU: Checkpointing: consumer stores offset in Azure Blob; survives restart
- ALU: Event Hubs Capture: auto-save events to Azure Blob/ADLS as Avro files
- ALU: Capture Avro schema: SequenceNumber, Offset, EnqueuedTimeUtc, SystemProperties, Body

**Subtopic: Kafka Protocol Compatibility**
- ALU: Event Hub namespace endpoint: namespace.servicebus.windows.net:9093
- ALU: SASL/PLAIN auth: connection string as password
- ALU: Topic = Event Hub; Consumer group = Consumer group
- ALU: Kafka producer/consumer libraries work without code changes (just change broker/auth)
- ALU: Spark Structured Streaming: read from Event Hub via Kafka connector
- ALU: Databricks: com.microsoft.azure.eventhubs:azure-eventhubs-spark connector or Kafka connector

**Subtopic: Event Hub Partitioning Strategy**
- ALU: No partition key: round-robin assignment; no ordering guarantee across partitions
- ALU: Partition key: hash determines partition; ordering guaranteed within partition
- ALU: Use case: device ID as partition key ensures ordered events per device
- ALU: Ordering across partitions: impossible by design; use watermarking for stream processing

**ANIMATION SPEC 6.5.1 — Event Hub Stream:**
```
Producers on left sending events with partition keys
Hashing: key → partition number shown
Partitions shown as horizontal lanes
Events flow right: append-only within lane
Consumer groups: multiple readers each at their own offset position
Capture: events also copying to ADLS Avro files
Throughput meter: MB/s in vs out
```

---

## MODULE 6.6 — Azure Monitor and Observability

### TOPIC 6.6.1 — Azure Monitor Stack

**Subtopic: Log Analytics Workspace**
- ALU: Central log repository; structured logs ingested from all Azure resources
- ALU: KQL (Kusto Query Language): query language for Log Analytics
- ALU: Tables: AzureActivity, AzureDiagnostics, ContainerLog, AppInsights custom, custom tables
- ALU: Data retention: 30 days free; 730 days with additional cost; archive to storage cheaper
- ALU: Diagnostic settings: enable on each resource to route logs to Log Analytics
- ALU: Azure Activity Log: subscription-level operations (who created/deleted what, when)

**Subtopic: KQL Essentials**
- ALU: KQL pipe syntax: Table | where col > 5 | project col1, col2 | summarize count() by col1
- ALU: where: filter rows; ==, !=, contains, startswith, has, in, between, isempty, isnotempty
- ALU: project: select/rename columns (like SQL SELECT)
- ALU: extend: add computed column without removing others
- ALU: summarize: aggregate; count(), sum(), avg(), max(), min(), percentile(), dcount()
- ALU: summarize by: group by columns
- ALU: bin(TimeGenerated, 1h): round to hour for time-bucket aggregations
- ALU: render timechart: render result as chart in Azure Portal
- ALU: join: leftouter/inner/rightanti; join hint.strategy=shuffle for large tables
- ALU: let: variable assignment; let threshold = 100;
- ALU: parse: extract fields from string with pattern matching
- ALU: extract(regex, group, string): extract regex capture group
- ALU: mv-expand: expand array/bag column into multiple rows
- ALU: top N by col: return top N rows sorted by column

**Subtopic: Azure Monitor Metrics**
- ALU: Metrics: numerical time-series; 1-minute granularity; 93-day retention
- ALU: Platform metrics: auto-collected; no configuration needed
- ALU: Custom metrics: application-pushed metrics via SDK or REST API
- ALU: Metric alerts: trigger when metric exceeds threshold; dimension filtering supported
- ALU: Autoscale: scale resources based on metric thresholds (CPU, queue length, custom)

**Subtopic: Azure Application Insights**
- ALU: APM (Application Performance Monitoring) for applications
- ALU: SDK instrumentation: automatically collect requests, dependencies, exceptions, traces
- ALU: Live metrics: real-time 1-second resolution stream
- ALU: Smart detection: ML-based anomaly detection on failure rate/performance
- ALU: Application Map: visualize service dependencies and failure rates
- ALU: Custom telemetry: TrackEvent, TrackMetric, TrackException, TrackTrace

**ANIMATION SPEC 6.6.1 — KQL Query Builder:**
```
Log table shown with rows
User types KQL query step by step
After each pipe: table updates showing filtered/projected result
summarize: rows collapse into aggregated result
render timechart: switches to line chart visualization
Timestamp column: bins animate grouping by hour
Error rate calculation: show formula building
```

""".lstrip()

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 5 written!")
