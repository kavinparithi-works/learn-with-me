"""
Master Spec Writer — appends all curriculum parts to the spec file.
Run: python spec_writer.py
"""
import os

TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

def append(text):
    with open(TARGET, "a", encoding="utf-8") as f:
        f.write(text)

# ─── PART 2: LEVELS 1-3 ──────────────────────────────────────────────────────

append("""

---

# PART 2 — CURRICULUM LEVELS 1–3: EXHAUSTIVE DEPTH

---

## LEVEL 1 — COMPUTER FUNDAMENTALS

**Domain Color:** `#4f8ef7` | **Prerequisites:** None | **Est. Hours:** 20+

---

### MODULE 1.1 — Binary, Number Systems & Data Representation

#### TOPIC 1.1.1 — Binary Number System

**Subtopic: What Is a Bit?**
- ALU: Physical meaning — transistor on (1) vs. off (0), maps to electrical voltage levels
- ALU: 0V = logical 0; 3.3V or 5V = logical 1 (depends on logic family)
- ALU: 1 bit = 1 binary decision; Shannon: 1 bit = 1 yes/no answer
- ALU: Why binary not decimal: transistors have two stable states, not ten
- ALU: Noise immunity: binary thresholds far apart, less error-prone than analogue

**Subtopic: Bytes and Multiples**
- ALU: Byte = 8 bits; values 0–255 unsigned
- ALU: Nibble = 4 bits (one hex digit); Word = 16 bits; DWORD = 32 bits; QWORD = 64 bits
- ALU: KB = 1,024 bytes (binary/IEC) vs 1,000 bytes (SI/decimal marketing)
- ALU: IEC standard: KiB (kibibyte), MiB (mebibyte), GiB (gibibyte) — unambiguous
- ALU: Scale: KB → MB → GB → TB → PB → EB → ZB → YB with binary multiples
- ALU: Why your 1 TB SSD shows 931 GiB in Windows: OS uses binary, manufacturer uses SI
- ALU: Data engineering: always clarify whether TB means TiB when discussing storage capacity

**Subtopic: Binary Counting and Arithmetic**
- ALU: Positional notation: rightmost bit = 2^0=1, next = 2^1=2, then 2^2=4, etc.
- ALU: MSB (Most Significant Bit) on left, LSB (Least Significant Bit) on right
- ALU: Count 0–7: 000, 001, 010, 011, 100, 101, 110, 111
- ALU: Binary addition rules: 0+0=0; 0+1=1; 1+0=1; 1+1=10 (sum=0, carry=1)
- ALU: Carry propagation: 1111 + 0001 = 10000 (all bits carry)
- ALU: Two's complement for signed integers: invert all bits then add 1
- ALU: Why two's complement: zero has single representation; addition hardware is same for signed/unsigned
- ALU: 8-bit signed range: -128 to +127; unsigned range: 0 to 255
- ALU: Overflow: 127 + 1 = -128 in signed 8-bit (wraps around silently)
- ALU: Real incidents: Ariane 5 rocket (1996) — 64-bit float to 16-bit int overflow; $500M loss
- ALU: Year 2038 problem: Unix timestamps stored as signed 32-bit int overflow on 2038-01-19

**Subtopic: Bitwise Operations**
- ALU: AND: 1100 AND 1010 = 1000 — both bits must be 1; use for masking/clearing
- ALU: OR:  1100 OR  1010 = 1110 — at least one bit is 1; use for setting bits
- ALU: XOR: 1100 XOR 1010 = 0110 — exactly one bit is 1; use for toggling, difference
- ALU: NOT: NOT 1100 = 0011 — inverts all bits
- ALU: Left shift (<<n): multiply by 2^n; fast multiply for powers of 2
- ALU: Right shift (>>n): divide by 2^n; arithmetic vs logical for signed
- ALU: Bit masking: value & 0x0F extracts lower 4 bits
- ALU: Setting bit n: value | (1 << n)
- ALU: Clearing bit n: value & ~(1 << n)
- ALU: Toggling bit n: value ^ (1 << n)
- ALU: Data engineering uses: partition bucket = hash & (numPartitions - 1) when numPartitions is power of 2
- ALU: Bloom filter: uses multiple hash functions and bitwise OR to set bits

**ANIMATION SPEC 1.1.1 — Binary Register:**
```
8 LED-style boxes representing a byte, MSB left to LSB right
Each box shows 0 or 1; pastel blue when 1, gray when 0
Click any box to toggle (flip between 0 and 1)
Below: decimal value updates live; hex value updates live
Addition demo: two rows of 8 boxes, carry bit shown between additions
Step-through button: advance one addition step at a time
Two's complement demo: enter value → click Negate → watch bits invert → +1 applied
Play/Pause/Reset controls; speed 0.5x/1x/2x
```

**DIAGRAM SPEC 1.1.1:**
```
Powers of 2 chart: positions 7-0 with values 128,64,32,16,8,4,2,1
Byte structure: labeled bit positions
Number line: signed (-128 to +127) vs unsigned (0 to 255)
Two's complement conversion walkthrough diagram
```

**INTERACTION SPEC 1.1.1 — Base Converter:**
```
Input: any number + source base (2–16)
Output: binary, octal, decimal, hexadecimal shown simultaneously
Division algorithm animation on demand
chmod octal calculator: enter rwxr-xr-x → shows 755
```

---

#### TOPIC 1.1.2 — Hexadecimal (Base 16)

**Subtopic: Hex Fundamentals**
- ALU: Digits 0–9 then A(10), B(11), C(12), D(13), E(14), F(15)
- ALU: 1 hex digit = exactly 4 bits (nibble); 2 hex digits = exactly 1 byte
- ALU: Hex compresses binary: 11111111 = FF (2 chars vs 8)
- ALU: Notation conventions: 0xFF (C/Python), #FF (CSS), FFh (assembly)
- ALU: Binary ↔ Hex: group binary in 4 bits from right, convert each group independently
- ALU: Hex ↔ Decimal: positional sum or repeated division by 16

**Subtopic: Hex in Computing**
- ALU: Memory addresses: 0x0000000000000000 to 0x7FFFFFFFFFFFFFFF (user space 64-bit)
- ALU: HTML/CSS colors: #4F8EF7 = R:79 G:142 B:247
- ALU: File magic bytes: JPEG = FF D8 FF; PNG = 89 50 4E 47; PDF = 25 50 44 46
- ALU: MAC address: 00:1A:2B:3C:4D:5E — 6 hex bytes
- ALU: UUID format: 550e8400-e29b-41d4-a716-446655440000 (8-4-4-4-12 hex with dashes)
- ALU: Delta Lake file checksums stored as hex strings
- ALU: Hex dumps: debugging binary files, network packets

---

#### TOPIC 1.1.3 — Octal (Base 8)

**Subtopic: Octal**
- ALU: Digits 0–7; 1 octal digit = 3 bits
- ALU: chmod 755 = 111 101 101 binary = rwxr-xr-x
- ALU: chmod 644 = 110 100 100 binary = rw-r--r--
- ALU: chmod 777 = full permissions; chmod 000 = no permissions
- ALU: chmod 4755 = setuid + 755; 2755 = setgid + 755; 1777 = sticky + 777
- ALU: Octal number prefix in C/Python: 0o755

---

### MODULE 1.2 — CPU Architecture

#### TOPIC 1.2.1 — CPU Internal Components

**Subtopic: Arithmetic Logic Unit (ALU)**
- ALU: Executes integer arithmetic: ADD, SUB, MUL, DIV, MOD
- ALU: Logical operations: AND, OR, XOR, NOT, shifts
- ALU: Comparisons: sets Zero Flag (ZF), Carry Flag (CF), Overflow Flag (OF), Sign Flag (SF)
- ALU: FPU: Floating-Point Unit — dedicated hardware for IEEE 754 operations
- ALU: SIMD (Single Instruction Multiple Data): SSE2 (128-bit), AVX2 (256-bit), AVX-512 (512-bit)
- ALU: SIMD processes 4/8/16 float values in one clock cycle
- ALU: Data engineering benefit: columnar processing exploits SIMD (Arrow, Photon engine)

**Subtopic: Control Unit**
- ALU: Fetches instruction from memory at Program Counter address
- ALU: Decodes opcode and operand fields
- ALU: Issues control signals to ALU, registers, memory controller
- ALU: Updates Program Counter to next instruction address
- ALU: Branch prediction: 95%+ accuracy on modern CPUs (bimodal, tournament predictors)
- ALU: Misprediction penalty: flush 15-20 pipeline stages ≈ 5-8 ns at 3 GHz

**Subtopic: Registers**
- ALU: x86-64 GPRs: RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP, R8–R15 (16 total)
- ALU: Sub-registers: RAX (64-bit) contains EAX (32-bit) → AX (16-bit) → AH/AL (8-bit)
- ALU: Special: RIP (instruction pointer), RFLAGS (status flags)
- ALU: XMM0–XMM15: 128-bit SIMD registers; YMM: 256-bit; ZMM: 512-bit
- ALU: Access time: sub-nanosecond (single clock cycle)
- ALU: Register file: typically 16–32 visible, hundreds of physical registers (register renaming)

**Subtopic: CPU Cache Hierarchy**
- ALU: L1 I-cache: ~32KB per core; decoded instructions; ~1-2 cycle access (~0.4ns at 3GHz)
- ALU: L1 D-cache: ~32KB per core; hot data; ~1-2 cycle access
- ALU: L2 cache: ~256KB–1MB per core; unified; ~4-12 cycle access
- ALU: L3 cache: ~4–64MB shared across all cores on die; ~30-40 cycle access
- ALU: Cache line: 64 bytes = smallest unit moved between cache levels
- ALU: Spatial locality: loading address X also loads 63 adjacent bytes into cache line
- ALU: Temporal locality: recently accessed data likely accessed again soon
- ALU: Cache miss types: compulsory (first access), capacity (too large), conflict (set associativity)
- ALU: Write-back policy: write to cache; flush dirty line to memory only on eviction
- ALU: Write-through policy: write to cache AND memory simultaneously (simpler coherence)
- ALU: MESI coherence protocol: Modified/Exclusive/Shared/Invalid state per cache line per core
- ALU: False sharing: two threads modify different variables sharing a cache line → constant invalidation
- ALU: False sharing fix: pad structs to 64-byte boundary
- ALU: Spark Tungsten: off-heap binary rows designed for cache-line-friendly columnar access

**Subtopic: Instruction Pipeline**
- ALU: Classic 5-stage: Fetch → Decode → Execute → Memory Access → Write-back
- ALU: Modern: 10–20 stages (deeper pipeline = higher clock frequency possible)
- ALU: Data hazard: instruction needs result not yet written by preceding instruction
- ALU: Control hazard: branch direction unknown; pipeline must guess or stall
- ALU: Structural hazard: two instructions need same hardware resource simultaneously
- ALU: Out-of-order execution: reorder independent instructions to maximize execution unit utilization
- ALU: Speculative execution: execute predicted branch path before branch resolves
- ALU: Spectre (2018): speculative execution side-channel leaks memory via cache timing

**Subtopic: Multi-Core and NUMA**
- ALU: Physical core: independent ALU, FPU, L1/L2, execution units
- ALU: Logical core (Hyper-Thread): two threads share one physical core's execution units
- ALU: Hyperthreading benefit: ~20-30% more throughput by filling execution unit idle cycles
- ALU: NUMA: Non-Uniform Memory Access; CPU socket has directly attached DRAM
- ALU: Local memory: same socket → ~100ns; Remote memory: cross-socket → ~200-400ns
- ALU: NUMA-unaware Spark: random memory allocation across NUMA nodes reduces performance
- ALU: numactl --membind=0 --cpunodebind=0: pin process to NUMA node 0

**ANIMATION SPEC 1.2.1 — CPU Pipeline:**
```
5 columns: FETCH | DECODE | EXECUTE | MEMORY | WRITEBACK
Instruction blocks flow left to right
Clock button: advance one cycle; auto-play button
4 instructions shown simultaneously in different stages
Stall: gray bubble inserted when data hazard detected
Branch: two speculative rows shown; misprediction flushes highlighted in red
Instructions per cycle counter at top
```

---

#### TOPIC 1.2.2 — Memory Hierarchy

**Subtopic: DRAM**
- ALU: DRAM cell: 1 capacitor + 1 transistor; capacitor leaks → refresh every ~64ms
- ALU: DDR4-3200: 25.6 GB/s per channel; dual-channel → 51.2 GB/s
- ALU: DDR5: higher bandwidth, on-die ECC, lower per-bit power
- ALU: ECC RAM: detects and corrects single-bit errors; required for production servers
- ALU: Memory channels: each channel is independent bus; more channels = more bandwidth
- ALU: LPDDR: low-power DDR for mobile; lower bandwidth, less power

**Subtopic: Virtual Memory**
- ALU: Each process sees private 64-bit virtual address space (~128TB usable on x86-64)
- ALU: MMU: Memory Management Unit translates virtual → physical via page tables
- ALU: 4-level page table walk: PML4 → PDPT → PD → PT → physical frame
- ALU: Each walk = 4 DRAM accesses; TLB caches recent translations
- ALU: TLB miss → hardware page table walk → ~100ns overhead
- ALU: Huge Pages (2MB): 512× fewer TLB entries; critical for large-heap workloads
- ALU: Spark: recommend hugepages on worker nodes for executor heap
- ALU: Swap: RAM exhausted → OS pages LRU pages to disk → catastrophic performance
- ALU: Set swappiness=1 or 0 on Spark/Databricks nodes to prevent swapping
- ALU: OOM killer: Linux kills processes by score when swap also exhausted

**Subtopic: Storage Tiers with Latencies**
- ALU: Register: sub-0.1ns
- ALU: L1 cache: ~0.4ns
- ALU: L2 cache: ~1.5ns
- ALU: L3 cache: ~10ns
- ALU: DRAM: ~100ns; 50-100 GB/s bandwidth
- ALU: NVMe PCIe4 SSD: ~50μs latency; ~7 GB/s sequential; ~1M IOPS
- ALU: SATA SSD: ~80μs latency; ~550 MB/s; ~100K IOPS
- ALU: HDD: 5-10ms latency; ~150 MB/s sequential; ~200 IOPS random
- ALU: Azure Premium SSD P30: ~1ms; ~200 MB/s; 5000 IOPS
- ALU: Azure Ultra Disk: <1ms; up to 4 GB/s; 160K IOPS
- ALU: ADLS Gen2: ~10ms first-byte; ~5-60 GB/s aggregate throughput
- ALU: AWS S3: similar to ADLS; ~5-10ms first-byte
- ALU: Implication: minimize ADLS API calls per query; use Parquet column pruning + row group skipping

**ANIMATION SPEC 1.2.2 — Memory Pyramid:**
```
7-tier inverted triangle (fast at top, slow at bottom)
Each tier: color gradient from deep blue (fast) to light gray (slow)
Each tier label: name, size range, typical latency, bandwidth
Click tier: tooltip with detailed specs
Data request simulation: starts from bottom tier
Checks each tier going up: miss = red X, hit = green check
Timer: shows cumulative latency building up
Warm cache repeat: same request hits L1 instantly
Side-by-side: cold (2000ms equivalent) vs warm (0.4ns)
```

---

### MODULE 1.3 — Operating Systems

#### TOPIC 1.3.1 — Processes and Threads

**Subtopic: Process Address Space**
- ALU: Text segment: read-only executable code; shared across instances of same program
- ALU: BSS: uninitialized global variables; OS zero-fills at process start
- ALU: Data segment: initialized global and static variables
- ALU: Heap: grows upward; malloc/new/Python object allocations
- ALU: Stack: grows downward; function call frames, local variables, return addresses
- ALU: Stack frame: return address, saved frame pointer, local variables, function arguments
- ALU: Stack overflow: deep recursion exhausts stack limit (default 8MB on Linux)
- ALU: mmap region: shared libraries, file-backed mappings, anonymous large allocations

**Subtopic: Process States**
- ALU: New → Ready → Running → Waiting/Blocked → Terminated
- ALU: Zombie: process exited but parent hasn't called wait() → PCB not freed
- ALU: Orphan: parent exited before child; adopted by init (PID 1)
- ALU: Context switch: save register state + page table pointer to PCB; load next process PCB
- ALU: Context switch cost: ~1-10μs; reason to prefer event-driven async over thread-per-request

**Subtopic: Threads**
- ALU: Thread shares: code segment, heap, global variables, file descriptors, signal handlers
- ALU: Thread owns: stack, registers, thread-local storage (TLS), errno
- ALU: Thread creation ~10× faster than process creation (no address space copy)
- ALU: Python GIL: only one thread executes Python bytecode at a time; CPU-bound threads don't parallelize
- ALU: Python multiprocessing: separate processes bypass GIL for CPU-bound work
- ALU: Java: no GIL; true parallel threads (Spark executors are JVM threads)
- ALU: Spark task: each task runs in one JVM thread; executor has N threads = N slots

**Subtopic: Synchronization**
- ALU: Mutex: one thread holds at a time; others block
- ALU: Spinlock: busy-poll for lock; low overhead for <100ns hold time; wastes CPU otherwise
- ALU: Reader-writer lock: N concurrent readers OR 1 exclusive writer
- ALU: Condition variable: wait(mutex, predicate); signal/broadcast to wake waiters
- ALU: Semaphore: counting; allows N concurrent holders; used for connection pools
- ALU: Memory barrier: prevents CPU/compiler reordering across the barrier point
- ALU: Compare-And-Swap (CAS): atomic: if *addr == expected { *addr = new; return true }
- ALU: Lock-free algorithms: built on CAS; no mutex; ABA problem awareness needed
- ALU: Deadlock: T1 holds A waits B; T2 holds B waits A; circular wait
- ALU: Deadlock prevention: always acquire locks in consistent global order (e.g., by resource ID)
- ALU: Livelock: threads keep yielding to each other; no progress; rare

**Subtopic: CPU Scheduling**
- ALU: Preemptive: OS timer interrupt forcibly removes CPU; quantum = 4-100ms
- ALU: Linux CFS: tracks vruntime per thread; always runs thread with minimum vruntime
- ALU: nice value: -20 (high priority) to +19 (low priority); default 0
- ALU: cgroups: limit CPU shares, CPU bandwidth quota, memory per group
- ALU: Docker: uses cgroups for --cpus and --memory limits
- ALU: Kubernetes: resource requests/limits map to cgroup constraints on pods
- ALU: Databricks: cluster nodes have cgroup limits enforced per executor

**ANIMATION SPEC 1.3.1 — Process State Machine:**
```
Circular state diagram: 6 nodes
Animated dot represents a process
Transitions labeled: create, schedule, interrupt, I/O-req, I/O-done, exit
Multiple dots showing concurrent processes
CPU depicted as single lane (one dot runs at a time)
Context switch: registers saved to PCB card, new PCB card loaded
Timeline bar: shows which process used CPU over time
```

---

#### TOPIC 1.3.2 — File Systems

**Subtopic: POSIX File Concepts**
- ALU: Inode: metadata structure (size, permissions, timestamps, block pointer list or extent tree)
- ALU: Inode does NOT store filename; directory stores (filename → inode number) mapping
- ALU: Hard link: additional directory entry pointing to existing inode; inode deleted only when count=0
- ALU: Symbolic link: file whose content is target path string; can cross filesystems
- ALU: File descriptor: per-process integer index; 0=stdin, 1=stdout, 2=stderr, 3+=user files
- ALU: open() returns fd; read(fd,...), write(fd,...), close(fd)
- ALU: File offset: position in file for next read/write; pread/pwrite use explicit offset

**Subtopic: POSIX Permissions**
- ALU: 9 permission bits: rwx (owner) rwx (group) rwx (others)
- ALU: r=4, w=2, x=1; chmod 755 = 4+2+1=7 owner, 4+1=5 group, 4+1=5 others
- ALU: Directory x bit: allows traversal (cd into); r bit: allows listing (ls)
- ALU: setuid (4000): on executable, runs as file owner's user ID
- ALU: setgid (2000): new files in directory inherit directory's group
- ALU: sticky bit (1000): on directory, only file owner can delete their files
- ALU: umask: mask applied to new file permissions (022 → files get 644, dirs get 755)
- ALU: POSIX ACLs: per-user/per-group entries beyond the owner/group/others model
- ALU: ADLS Gen2: POSIX ACLs control who can read/write/execute directory and file objects

**Subtopic: Journaling and Durability**
- ALU: Journal (WAL): write changes to log first; on crash, replay from journal
- ALU: ext4 data=ordered: data blocks written to disk before journal commit (default)
- ALU: ext4 data=journal: both data and metadata journaled (safest, slowest)
- ALU: fsync(): flush OS page cache to storage; ensures durability
- ALU: fdatasync(): flush only data (not metadata) for slightly better performance
- ALU: O_DIRECT: bypass kernel page cache for large sequential I/O
- ALU: CoW filesystems (ZFS/Btrfs): never overwrite in place; write new version then update pointer atomically

**Subtopic: Distributed File Systems**
- ALU: HDFS: 128MB blocks, 3× replication, rack-aware placement policy
- ALU: HDFS NameNode: single metadata server (bottleneck); HA mode: active + standby with ZooKeeper
- ALU: HDFS DataNode: stores blocks; sends heartbeat + block report to NameNode every 10s
- ALU: HDFS write pipeline: client → DataNode1 → DataNode2 → DataNode3 (chain)
- ALU: HDFS rack awareness: replicas on different racks for fault tolerance
- ALU: ADLS Gen2: hierarchical namespace = atomic directory rename (unlike flat blob storage)
- ALU: Azure Blob Storage: flat namespace; rename = copy + delete (not atomic; breaks Delta Lake without HNS)
- ALU: S3 strong consistency (since Dec 2020): read-after-write and list-after-write consistent
- ALU: Object storage limitation: no locking primitives; Delta Lake uses transaction log for coordination

---

### MODULE 1.4 — Networking

#### TOPIC 1.4.1 — TCP/IP Exhaustive

**Subtopic: OSI 7-Layer Model**
- ALU: Layer 7 Application: HTTP, HTTPS, gRPC, Kafka protocol, JDBC, LDAP, DNS (uses Layer 4)
- ALU: Layer 6 Presentation: TLS/SSL encryption, data serialization (JSON, Avro, Protobuf)
- ALU: Layer 5 Session: session management; rarely distinct in modern TCP/IP
- ALU: Layer 4 Transport: TCP (reliable, ordered) and UDP (fast, unreliable); port numbers
- ALU: Layer 3 Network: IP addressing, routing; Azure VNet routing tables
- ALU: Layer 2 Data Link: Ethernet MAC addressing, VLANs, ARP (IP → MAC resolution)
- ALU: Layer 1 Physical: cables, fiber optics, radio (WiFi); irrelevant for cloud data engineering

**Subtopic: TCP Connection**
- ALU: 3-way handshake: SYN → SYN-ACK → ACK; establishes sequence numbers
- ALU: 4-way teardown: FIN → ACK → FIN → ACK (each side closes independently)
- ALU: TIME_WAIT: 2×MSL ≈ 4 min; prevents old packets corrupting new connections on same port
- ALU: TCP state machine: CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, CLOSE_WAIT, LAST_ACK, TIME_WAIT
- ALU: SYN flood: attacker sends many SYN packets; server exhausts half-open connection table
- ALU: SYN cookies: encode state in sequence number; stateless defense against SYN flood

**Subtopic: TCP Reliability and Performance**
- ALU: Sequence numbers: 32-bit counter tracking bytes sent (not packets)
- ALU: ACK: cumulative acknowledgement; ACK=N means all bytes up to N received
- ALU: Retransmission Timeout (RTO): exponential backoff on timeout
- ALU: Fast retransmit: 3 duplicate ACKs triggers immediate retransmit before RTO
- ALU: SACK (Selective ACK): ACK non-contiguous received blocks; more efficient recovery
- ALU: Congestion window (cwnd): limits in-flight bytes to avoid overwhelming network
- ALU: Slow start: cwnd doubles each RTT until ssthresh; then linear increase
- ALU: CUBIC: Linux default CC; cubic growth function after congestion event
- ALU: BBR: Google CC; model-based; good for high-bandwidth-delay-product links
- ALU: Bandwidth-Delay Product (BDP) = bandwidth × RTT = max in-flight bytes
- ALU: 10Gbps × 50ms RTT = 62.5MB BDP; need TCP window ≥ 62.5MB for full utilization
- ALU: Jumbo frames: 9000-byte MTU in data centers (vs 1500 standard); reduces per-packet overhead
- ALU: TCP_NODELAY: disables Nagle algorithm; sends small packets immediately (Kafka uses this)
- ALU: Spark cross-AZ shuffle: 2-5ms RTT; limits shuffle throughput without large TCP buffers

**Subtopic: UDP**
- ALU: No connection, no handshake, no ACK, no retransmit, no ordering guarantee
- ALU: Lower overhead: no per-connection state, no ACK packets
- ALU: Uses: DNS queries, DHCP, SNMP, streaming media, online gaming, QUIC
- ALU: QUIC (HTTP/3): UDP + congestion control + multiplexing + TLS in userspace

**ANIMATION SPEC 1.4.1 — HTTP Lifecycle:**
```
Browser and Server icons on left and right
Step 1: DNS lookup animated (browser → recursive resolver → root → TLD → auth → IP returned)
Step 2: TCP 3-way handshake (SYN/SYN-ACK/ACK arrows with labels)
Step 3: TLS handshake (certificate icon, key exchange)
Step 4: HTTP GET request with header display
Step 5: Server processes (spinner), sends HTTP 200 OK response
Step 6: JSON payload shown expanding below response
Milliseconds timer updates at each step
Total shown at end: DNS 20ms + TCP 30ms + TLS 60ms + Request/Response 50ms = 160ms total
```

---

#### TOPIC 1.4.2 — DNS, HTTP, APIs

**Subtopic: DNS Record Types**
- ALU: A record: hostname → IPv4 address; TTL controls cache duration
- ALU: AAAA record: hostname → IPv6 address
- ALU: CNAME: alias pointing to another hostname (cannot be at zone apex)
- ALU: MX: mail exchange server with priority
- ALU: TXT: arbitrary text; used for SPF, DKIM, DMARC, domain verification
- ALU: NS: authoritative nameservers for zone
- ALU: SOA: Start of Authority; zone metadata; serial number for replication
- ALU: PTR: reverse DNS lookup (IP → hostname)
- ALU: SRV: service discovery (_http._tcp.example.com → host + port)
- ALU: Azure Private DNS: custom zones for private VNet name resolution
- ALU: Azure DNS: public DNS hosting for domain names

**Subtopic: HTTP Status Codes Complete**
- ALU: 200 OK, 201 Created, 202 Accepted, 204 No Content (success)
- ALU: 206 Partial Content: range request response (used for streaming/resumable downloads)
- ALU: 301 Moved Permanently, 302 Found (temp redirect), 304 Not Modified, 307 Temp, 308 Perm
- ALU: 400 Bad Request (malformed), 401 Unauthorized (not authenticated), 403 Forbidden (authenticated but not authorized)
- ALU: 404 Not Found, 405 Method Not Allowed, 409 Conflict, 410 Gone, 422 Unprocessable Entity
- ALU: 429 Too Many Requests (rate limited; check Retry-After header)
- ALU: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout
- ALU: Databricks API returns 429 during cluster scaling; retry logic required

**Subtopic: REST API Design**
- ALU: Resource-oriented: nouns not verbs; /pipelines/123 not /getPipeline?id=123
- ALU: HTTP methods map to CRUD: GET=read, POST=create, PUT=replace, PATCH=update, DELETE=remove
- ALU: Idempotency: GET/PUT/DELETE safe to retry; POST/PATCH not guaranteed
- ALU: Idempotency key: POST with X-Idempotency-Key header for safe retry
- ALU: Pagination: cursor-based (next_token) preferred over offset for large result sets
- ALU: Cursor advantages: stable during concurrent inserts; consistent O(1) per page
- ALU: Filtering: query params ?status=running&cluster_type=Standard_DS3_v2
- ALU: Sorting: ?sort_by=created_at&sort_order=DESC
- ALU: Rate limiting: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After
- ALU: Long-running operations: 202 Accepted + Location: /operations/{run_id} → poll for completion
- ALU: Databricks Jobs API 2.1: POST /jobs/runs/submit → get run_id → GET /jobs/runs/get?run_id=N
- ALU: Azure Data Factory REST API: pipelines, runs, triggers all follow REST conventions
- ALU: Authentication: Bearer token (OAuth2 access token); Azure uses AAD tokens

---

## LEVEL 2 — DATA FUNDAMENTALS: EXHAUSTIVE

---

### MODULE 2.1 — Data Types Complete Reference

#### TOPIC 2.1.1 — Numeric Types

**Subtopic: Integer Types All Databases**
- ALU: TINYINT: 1 byte; MySQL: 0–255 unsigned or -128–127 signed
- ALU: SMALLINT: 2 bytes; -32,768 to 32,767
- ALU: INT/INTEGER: 4 bytes; -2,147,483,648 to 2,147,483,647
- ALU: BIGINT: 8 bytes; ±9,223,372,036,854,775,807
- ALU: When BIGINT required: tables with >2B rows; Unix ms timestamps; Snowflake IDs
- ALU: Auto-increment overflow: INT identity wraps at 2.1B; switch to BIGINT proactively
- ALU: Python int: arbitrary precision (unlimited size, no overflow)
- ALU: Spark types: ByteType (8-bit), ShortType (16-bit), IntegerType (32-bit), LongType (64-bit)

**Subtopic: Floating-Point**
- ALU: IEEE 754 single (FLOAT, 32-bit): 1 sign + 8 exponent + 23 mantissa; ~7 significant decimal digits
- ALU: IEEE 754 double (DOUBLE, 64-bit): 1 sign + 11 exponent + 52 mantissa; ~15 significant decimal digits
- ALU: Classic pitfall: 0.1 + 0.2 ≠ 0.3 in IEEE 754 (= 0.30000000000000004)
- ALU: NaN: Not a Number; result of 0/0, sqrt(-1), Infinity - Infinity
- ALU: NaN property: NaN ≠ NaN (unique); use isnan() to check
- ALU: Infinity: 1.0/0.0 = +Inf; −1.0/0.0 = -Inf; legal IEEE 754 values
- ALU: Denormal numbers: very small values near zero; slower to compute on most CPUs
- ALU: Catastrophic cancellation: (1000001 - 1000000.999) loses almost all precision
- ALU: Financial data: NEVER use FLOAT; use DECIMAL(18,2) or BIGINT (store cents)
- ALU: Spark FloatType = Java float = 32-bit; DoubleType = Java double = 64-bit

**Subtopic: DECIMAL/NUMERIC**
- ALU: DECIMAL(precision, scale): precision=total digits; scale=digits after decimal point
- ALU: DECIMAL(10,2): max 99,999,999.99; storage: 4-9 bytes
- ALU: Exact arithmetic: no IEEE 754 rounding errors; stores as scaled integer
- ALU: NUMERIC is synonym for DECIMAL in most databases
- ALU: Spark DecimalType(precision, scale): precision max 38; uses 128-bit internal representation
- ALU: Spark decimal overflow: returns null with ANSI mode off; exception with ANSI mode on
- ALU: Safe aggregation: CAST(SUM(price) AS DECIMAL(20,4)) to avoid intermediate overflow

---

#### TOPIC 2.1.2 — String Types

**Subtopic: Character Encoding**
- ALU: ASCII: 7-bit encoding; 128 code points; only English + control characters
- ALU: Latin-1 (ISO-8859-1): 256 code points; extends ASCII with Western European characters
- ALU: Windows-1252: Microsoft superset of Latin-1; common in legacy Windows exports
- ALU: Unicode: U+0000 to U+10FFFF; 1.1M+ code points; covers all human writing systems
- ALU: UTF-8: variable length 1–4 bytes; backward-compatible with ASCII; world standard for storage
- ALU: UTF-8 byte sequences: 0xxxxxxx (1B), 110xxxxx 10xxxxxx (2B), 1110xxxx 10xxxxxx 10xxxxxx (3B)
- ALU: UTF-16: Java/C# internal representation; 2 bytes for BMP, 4 bytes (surrogate pairs) for supplementary
- ALU: UTF-32: fixed 4 bytes; simple indexing but 4× storage of UTF-8 for ASCII
- ALU: BOM (EF BB BF in UTF-8): byte order mark; causes parsing errors; use utf-8-sig codec to strip
- ALU: Mojibake: garbled text from reading bytes with wrong encoding (e.g., CP1252 read as Latin-1)
- ALU: Python 3 str: internal Unicode (Latin-1/UCS-2/UCS-4 depending on max code point)
- ALU: Python bytes: raw octets; encode('utf-8')/decode('utf-8') converts
- ALU: Spark StringType: UTF-8 encoded bytes internally

**Subtopic: SQL String Types**
- ALU: CHAR(n): fixed width, space-padded; reads same length always; no advantage in modern storage
- ALU: VARCHAR(n): variable width; stores actual length + data; max n characters
- ALU: NVARCHAR(n): UTF-16 Unicode; 2× storage vs VARCHAR; SQL Server for i18n
- ALU: TEXT/CLOB: unbounded; stored off-row in some engines; can't index directly
- ALU: VARCHAR(MAX): SQL Server unbounded; stored inline up to 8KB, off-row beyond
- ALU: Collation: rules for string comparison, sort order, case/accent sensitivity
- ALU: Binary collation (utf8mb4_bin): byte-by-byte comparison; case and accent sensitive
- ALU: SQL Server CI_AS: Case-Insensitive, Accent-Sensitive (default)
- ALU: Case-insensitive collation can prevent index range scan usage

---

#### TOPIC 2.1.3 — Date and Time

**Subtopic: Temporal Types by Database**
- ALU: DATE: stores year, month, day; Spark/PostgreSQL: integer days since epoch
- ALU: TIME: stores hour, minute, second, optional fraction; stored as nanoseconds from midnight
- ALU: DATETIME (MySQL): no timezone; 1-second precision; range 1000–9999
- ALU: DATETIME2(7) (SQL Server): 100ns precision; range 0001–9999; no timezone; preferred over DATETIME
- ALU: DATETIMEOFFSET(7) (SQL Server): DATETIME2 + UTC offset stored; timezone-aware
- ALU: TIMESTAMP (MySQL): auto-converts to UTC on store; range 1970–2038 (Y2038 problem)
- ALU: TIMESTAMP WITH TIME ZONE (PostgreSQL): stored as UTC; displayed with session TZ
- ALU: TIMESTAMP WITHOUT TIME ZONE (PostgreSQL): no TZ info; takes session TZ for interpretation
- ALU: Spark TimestampType: microseconds since 1970-01-01 00:00:00 UTC (internally UTC)
- ALU: Spark DateType: days since 1970-01-01 (integer)
- ALU: Spark session timezone: spark.sql.session.timeZone affects display and string→timestamp parsing

**Subtopic: Time Zone Pitfalls**
- ALU: UTC: Coordinated Universal Time; no DST; always safe for storage
- ALU: DST spring forward: 2:00 AM → 3:00 AM; that hour doesn't exist
- ALU: DST fall back: 2:00 AM occurs twice; ambiguous which occurrence
- ALU: IANA tzdata: authoritative DST rules (Olson database); updated for government changes
- ALU: Best practice: always store UTC; convert to user timezone only at display layer
- ALU: Spark default timezone: JVM system timezone; override with spark.sql.session.timeZone="UTC"
- ALU: Common Spark bug: CSV timestamps parsed in local timezone, stored as wrong UTC value

**Subtopic: Date Arithmetic Functions**
- ALU: CURRENT_TIMESTAMP / NOW() / GETUTCDATE(): current datetime
- ALU: DATEADD(day, 7, date) / DATE_ADD(date, 7) / date + INTERVAL 7 DAY
- ALU: DATEDIFF(day, start, end) / DATEDIFF(end, start) (MySQL reversed args)
- ALU: DATE_TRUNC('month', ts): first instant of containing month
- ALU: TRUNC(date, 'MM'): Oracle; TRUNC(ts, 'HH'): truncate to hour
- ALU: EXTRACT(YEAR FROM ts) / DATE_PART('year', ts) / YEAR(ts)
- ALU: TO_DATE('2024-01-15', 'YYYY-MM-DD') / STR_TO_DATE (MySQL) / PARSE_DATE (BigQuery)
- ALU: Spark: date_add, date_sub, datediff, months_between, add_months, last_day, next_day, date_trunc
- ALU: Spark: from_unixtime(ts_seconds), unix_timestamp(string, format), to_timestamp, to_date
- ALU: Window function date lookback: LAG(value,7) OVER (PARTITION BY user ORDER BY date) for 7-day prior

---

#### TOPIC 2.1.4 — NULL: Complete Reference

**Subtopic: NULL Logic**
- ALU: NULL = unknown; not zero, not empty string, not false; distinct semantic
- ALU: Three-valued logic: TRUE / FALSE / UNKNOWN
- ALU: NULL = 5 → UNKNOWN (not TRUE, not FALSE)
- ALU: NULL = NULL → UNKNOWN (NULL not equal to itself; this is intentional)
- ALU: WHERE clause retains rows only where predicate is TRUE; UNKNOWN → row excluded
- ALU: NULL AND TRUE = UNKNOWN; NULL AND FALSE = FALSE (FALSE dominates AND)
- ALU: NULL OR TRUE = TRUE (TRUE dominates OR); NULL OR FALSE = UNKNOWN
- ALU: NOT NULL = UNKNOWN
- ALU: COUNT(*) counts all rows; COUNT(col) skips NULLs
- ALU: SUM, AVG, MIN, MAX, STDDEV all ignore NULLs in their computation
- ALU: AVG denominator = count of non-null values (not total rows)
- ALU: NULL IN (1, 2, NULL) → UNKNOWN (not TRUE); row excluded from WHERE
- ALU: NULL NOT IN (1,2): UNKNOWN if subquery contains any NULL → classic no-rows-returned bug
- ALU: Workaround: WHERE id NOT IN (SELECT id FROM t WHERE id IS NOT NULL)
- ALU: GROUP BY: NULL values grouped together as one group
- ALU: ORDER BY: NULLS LAST (default most DBs) or NULLS FIRST
- ALU: ROLLUP/CUBE: uses NULL to represent subtotals — ambiguous with data NULLs

**Subtopic: NULL Handling Functions**
- ALU: COALESCE(a, b, c, ...): returns first non-NULL; short-circuit evaluation
- ALU: NULLIF(a, b): returns NULL if a=b, else a; common use: NULLIF(count, 0) for safe division
- ALU: IS NULL: only correct null check (not = NULL)
- ALU: IS NOT NULL: opposite
- ALU: IS DISTINCT FROM: NULL-safe !=; NULL IS DISTINCT FROM NULL → FALSE
- ALU: IS NOT DISTINCT FROM: NULL-safe =; NULL IS NOT DISTINCT FROM NULL → TRUE
- ALU: NVL(a, b): Oracle/Spark; two-arg COALESCE
- ALU: IFNULL(a, b): MySQL/Spark SQL; same as NVL
- ALU: Spark: col.isNull(), col.isNotNull(), col.isnan()
- ALU: Spark fillna(0): fill all numeric nulls with 0
- ALU: Spark fillna({"col1": 0, "col2": "unknown"}): per-column fill
- ALU: Spark dropna(how='any'): drop rows with any null
- ALU: Spark dropna(how='all'): drop rows where ALL columns are null
- ALU: Spark dropna(thresh=3): drop rows with fewer than 3 non-null values

---

### MODULE 2.2 — File Formats: Every Detail

#### TOPIC 2.2.1 — CSV

**Subtopic: CSV Structure**
- ALU: RFC 4180 (2005): comma delimiter, CRLF line endings, double-quote quoting
- ALU: Delimiter variants: tab (TSV), pipe (|), semicolon (;); configurable
- ALU: Header row: optional but conventional; defines column names
- ALU: Quoting: fields containing delimiter, newlines, or double-quotes must be quoted
- ALU: Escaped double-quote: doubled inside quoted field ("He said \\"\\\"hello\\"\\"")
- ALU: Backslash escape: non-standard; MySQL CSV uses backslash
- ALU: Line endings: CRLF on Windows, LF on Unix; cross-platform issues common
- ALU: Trailing newline: RFC 4180 recommends it; many tools produce it; some don't

**Subtopic: CSV Pitfalls**
- ALU: Encoding: UTF-8 without BOM is safest; Windows tools add BOM → parse errors
- ALU: Type inference: everything is string; each consumer infers types independently
- ALU: Null representation: empty field, \\N, NULL, none, NA — no standard
- ALU: Multi-line values: embedded newlines allowed in quoted fields; breaks naive line readers
- ALU: Schema drift: column added/removed/reordered in source → consumer breaks
- ALU: Large files: no random access; must scan from start; no statistics
- ALU: Non-splittable gzip: single-threaded read; kills Spark parallelism
- ALU: Splittable CSV: uncompressed or bzip2; enables parallel read by multiple Spark tasks

**Subtopic: Spark CSV Options**
- ALU: header=true: use first row as column names
- ALU: inferSchema=true: scan file to detect types (extra pass)
- ALU: sep=",": delimiter character
- ALU: quote='"': quoting character
- ALU: escape="\\": escape character
- ALU: nullValue="": string treated as NULL
- ALU: dateFormat="yyyy-MM-dd": pattern for date parsing
- ALU: timestampFormat="yyyy-MM-dd HH:mm:ss": timestamp pattern
- ALU: multiLine=true: allow quoted fields with embedded newlines
- ALU: encoding="UTF-8": character encoding of file

---

#### TOPIC 2.2.2 — Parquet: Exhaustive

**Subtopic: Physical Layout**
- ALU: Magic bytes: PAR1 at bytes 0–3 and last 4 bytes of file
- ALU: Row group: horizontal slice of all columns; default 128MB
- ALU: Optimal row group size: match HDFS block size or Spark partition target size
- ALU: Column chunk: data for one column within one row group
- ALU: Pages: unit within column chunk; Data Page v1/v2, Dictionary Page, Index Page
- ALU: Data page size: default 1MB (parquet.page.size); smaller = more compression metadata overhead
- ALU: Footer: schema definition + row group offsets/sizes + column chunk statistics
- ALU: File ends: 4-byte footer length + PAR1 magic; reader starts from end to find footer

**Subtopic: Encodings**
- ALU: PLAIN: raw bytes; always available as fallback
- ALU: DICTIONARY: dictionary page first in column chunk; data stores variable-length indices
- ALU: Dictionary threshold: if dictionary exceeds 1MB, fall back to PLAIN for remaining values
- ALU: RLE_DICTIONARY: dictionary encoding + run-length encoding of indices
- ALU: BIT_PACKING: pack integers into minimal bits (values 0–7 need 3 bits each)
- ALU: DELTA_BINARY_PACKED: delta-encode integers then bit-pack deltas (great for timestamps)
- ALU: DELTA_LENGTH_BYTE_ARRAY: delta-encode string lengths; concatenate string bytes
- ALU: DELTA_BYTE_ARRAY: prefix-suffix encoding for strings with common prefix (sorted strings)
- ALU: BYTE_STREAM_SPLIT: interleave float bytes across streams; improves LZ compression on floats

**Subtopic: Compression Codecs**
- ALU: UNCOMPRESSED: no compression; useful for debugging, already-compressed data
- ALU: SNAPPY: 1.5–3× ratio; very fast; not standardized (Google); Spark legacy default
- ALU: GZIP (zlib): 2–5× ratio; slow; standard; good archival
- ALU: ZSTD: 2–5× ratio; fast; Parquet 2.0+; recommended for new workloads
- ALU: LZ4: 1.5–2× ratio; extremely fast; good for shuffle spill files
- ALU: BROTLI: 3–7× ratio; very slow; best archival compression
- ALU: Per-column compression: each column chunk can use a different codec
- ALU: Compression is applied after encoding: encoding first, then compress encoded bytes

**Subtopic: Statistics and Predicate Pushdown**
- ALU: Column chunk stats: min_value, max_value, null_count, distinct_count (optional)
- ALU: Row group pruning: if WHERE col > 100 and column.max = 50 → entire row group skipped
- ALU: Column pruning: SELECT a, b FROM parquet reads only column chunks for a and b
- ALU: Statistics on BYTE_ARRAY disabled by default; enable with parquet.statistics.truncate.length
- ALU: Parquet 2.0 bloom filter: one per column per row group; answers "could value X be in this chunk?"
- ALU: Bloom filter false positive rate: ~1% default; tune with parquet.bloom.filter.expected.ndv
- ALU: Delta Lake uses Parquet stats for data skipping; tracks first 32 columns by default

**Subtopic: Schema and Nested Types**
- ALU: Dremel encoding: definition levels + repetition levels encode nullability and list nesting
- ALU: Definition level: how many optional fields in the path to this value are actually defined
- ALU: Repetition level: whether this value is a new record, new list item, or continuation
- ALU: Required (1): always present; Optional (0 or 1): may be null; Repeated (0+): list
- ALU: LIST logical type: 3-level nesting: optional list field → repeated element group → element
- ALU: MAP logical type: repeated key_value group containing key and value
- ALU: Nested struct: flat fields with dot-notation names (address.city, address.zip)

**Subtopic: Spark Parquet Options**
- ALU: spark.sql.parquet.compression.codec: snappy/gzip/zstd/lz4/none
- ALU: spark.sql.parquet.filterPushdown=true: enables predicate pushdown to Parquet reader
- ALU: spark.sql.parquet.mergeSchema=false: skip schema merging for faster reads
- ALU: parquet.block.size: row group size in bytes
- ALU: parquet.page.size: page size in bytes
- ALU: spark.sql.files.maxPartitionBytes: max Parquet file bytes per Spark partition

---

#### TOPIC 2.2.3 — Avro: Exhaustive

**Subtopic: Avro Schema**
- ALU: Schema defined in JSON; stored in file header (object container file format)
- ALU: Primitive types: null, boolean, int (32-bit), long (64-bit), float (32-bit), double (64-bit), bytes, string
- ALU: Record: {"type":"record","name":"User","namespace":"com.example","fields":[...]}
- ALU: Field: {"name":"age","type":"int","default":0,"doc":"user age in years"}
- ALU: Nullable field (union): {"name":"phone","type":["null","string"],"default":null}
- ALU: Enum: {"type":"enum","name":"Status","symbols":["ACTIVE","INACTIVE"]}
- ALU: Array: {"type":"array","items":"string"}
- ALU: Map: {"type":"map","values":"int"}
- ALU: Fixed: {"type":"fixed","name":"MD5","size":16}
- ALU: Logical types: date (int, days since epoch), time-millis (int, ms), timestamp-millis (long, ms), decimal (bytes/fixed), uuid (string)
- ALU: Schema naming: dot-separated namespace + name = full name; used for references

**Subtopic: Schema Evolution**
- ALU: Backward compatible (new reads old): add field with default; remove field that had default
- ALU: Forward compatible (old reads new): remove field with default; add field with default
- ALU: Full compatible: both directions; add/remove only fields with defaults
- ALU: Renaming: add "aliases" array to field; old name still resolves
- ALU: Type promotions allowed: int→long, int→float, int→double, long→float, long→double, float→double, string→bytes, bytes→string
- ALU: Type changes NOT allowed: no demotion, no changing complex type kind
- ALU: Schema registry: Confluent Schema Registry REST API; ID embedded in Kafka message payload
- ALU: Magic byte + schema ID: 5-byte prefix on Kafka messages (0x00 + 4-byte schema ID)
- ALU: Subject strategies: TopicNameStrategy (topic-key/topic-value), RecordNameStrategy, TopicRecordNameStrategy

**Subtopic: Avro vs. Parquet Decision Matrix**
- ALU: Use Avro when: Kafka serialization, schema evolution required, row-by-row streaming writes
- ALU: Use Parquet when: analytical queries, columnar scans, ADLS landing, Delta Lake files
- ALU: Avro row-oriented: faster for writing all fields of a record
- ALU: Parquet column-oriented: faster for reading subset of columns across many records
- ALU: Databricks: from_avro(col, schema_string) and to_avro(col) for Kafka integration
- ALU: Azure Event Hub Avro capture: messages captured as Avro container files in blob storage

---

### MODULE 2.3 — Data Architecture

#### TOPIC 2.3.1 — Pipeline Design Patterns

**Subtopic: Load Strategies**
- ALU: Full load: DELETE all + INSERT all; simple, idempotent; impractical for large tables
- ALU: Append-only: INSERT new records; no update/delete handling; fast; immutable log tables
- ALU: Incremental by watermark: load WHERE updated_at > last_high_watermark; requires reliable updated_at
- ALU: Watermark pitfalls: late-arriving data missed; clock skew; updated_at not always updated
- ALU: CDC via DB logs: Debezium reads binlog/WAL/redo log; captures INSERT/UPDATE/DELETE events
- ALU: CDC event format: before/after values, operation type, timestamp, transaction ID
- ALU: Full+increment hybrid: daily full snapshot + hourly incremental delta
- ALU: Upsert (MERGE INTO): INSERT if key absent, UPDATE if key present; Delta Lake native
- ALU: Hard delete: source records actually deleted; CDC required to propagate
- ALU: Soft delete: deleted_at timestamp set; simple to propagate with incremental load

**Subtopic: SCD Patterns**
- ALU: SCD Type 1 (overwrite): no history kept; simple; use for correcting data quality errors
- ALU: SCD Type 2 (history): new row per change; is_current BOOLEAN + effective_from + effective_to
- ALU: SCD Type 2 surrogate key: row_sk = BIGINT auto-increment; business key separate
- ALU: SCD Type 2 effective_to for current: 9999-12-31 or NULL convention
- ALU: SCD Type 3 (add column): prev_value column; tracks only one change; rarely useful
- ALU: SCD Type 4 (history table): current in main table; history in separate audit table
- ALU: SCD Type 6 (hybrid): current value + is_current + effective dates + prev_value column
- ALU: Delta Lake MERGE for SCD2:
  ```sql
  MERGE INTO dim_customer AS target
  USING source ON target.customer_id = source.customer_id AND target.is_current = true
  WHEN MATCHED AND source.hash != target.hash THEN
    UPDATE SET is_current = false, effective_to = current_timestamp()
  WHEN NOT MATCHED THEN
    INSERT (customer_id, name, email, is_current, effective_from, effective_to)
    VALUES (source.customer_id, source.name, source.email, true, current_timestamp(), '9999-12-31')
  ```
- ALU: Hash-based change detection: MD5/SHA256 of all non-key columns; compare to detect changes

**Subtopic: Medallion Architecture**
- ALU: Bronze layer: raw data exactly as received; append-only; never delete; preserve all history
- ALU: Bronze schema: raw_payload (STRING/VARIANT), source_system, source_filename, ingestion_timestamp
- ALU: Silver layer: cleansed, validated, standardized, deduplicated; business logic begins
- ALU: Silver schema: standardized column names (snake_case), correct data types, NULLs replaced, duplicates removed
- ALU: Gold layer: aggregated, enriched, business-domain-specific; optimized for consumption
- ALU: Gold schema: wide denormalized tables; pre-aggregated metrics; joined from multiple silver tables
- ALU: Reprocessing: Bronze never modified; Silver+Gold recomputed from Bronze when logic changes
- ALU: Quality gates: Bronze → Silver enforces schema validation and null checks
- ALU: Azure Databricks architecture: ADF ingests to Bronze ADLS; Databricks transforms Bronze→Silver→Gold
- ALU: Delta Live Tables: declarative Bronze→Silver→Gold pipeline with auto data quality

""")

# ─── PART 3: SQL COMPLETE ─────────────────────────────────────────────────────

append("""

---

# PART 3 — LEVEL 4: SQL FUNDAMENTALS TO MASTERY

**Domain Color:** `#f59e0b` (Amber) | **Prerequisites:** Level 3 | **Est. Hours:** 50+

---

## MODULE 4.1 — SQL Foundations

### TOPIC 4.1.1 — SELECT Statement

**Subtopic: Basic SELECT**
- ALU: SELECT returns a result set (virtual table); does not modify data
- ALU: SELECT * : returns all columns; avoid in production (schema changes break consumers)
- ALU: SELECT col1, col2: explicit column list; preferred
- ALU: Column aliases: SELECT col AS alias, col alias (AS optional but recommended)
- ALU: Expression in SELECT: SELECT price * quantity AS total_value
- ALU: String concatenation: SELECT first_name || ' ' || last_name AS full_name (ANSI/PostgreSQL)
- ALU: String concat SQL Server: SELECT first_name + ' ' + last_name
- ALU: CONCAT() function: SELECT CONCAT(first_name, ' ', last_name)
- ALU: Literal values: SELECT 'hello' AS greeting, 42 AS answer
- ALU: Column ordering in SELECT: does not affect FROM execution; just presentation order
- ALU: DISTINCT: SELECT DISTINCT col removes duplicate rows from result
- ALU: DISTINCT is expensive: requires sort or hash; use only when needed
- ALU: TOP/LIMIT/FETCH FIRST: limit rows returned
  - ALU: SQL Server: SELECT TOP 10 *
  - ALU: MySQL/PostgreSQL: SELECT * LIMIT 10
  - ALU: ANSI SQL: SELECT * FETCH FIRST 10 ROWS ONLY

**ANIMATION SPEC 4.1.1 — SELECT Visualizer:**
```
Table shown with all columns
SELECT statement typed incrementally
As columns listed: corresponding columns highlight in table
WHERE clause: non-matching rows fade out
ORDER BY: rows animate reordering
LIMIT: top N rows highlighted, rest faded
Result set shown below as new table
Step-through: parse → filter → project → sort → limit
```

**Subtopic: FROM Clause**
- ALU: FROM specifies source tables/views/subqueries
- ALU: FROM table_name AS alias (alias optional but required for subqueries)
- ALU: FROM database.schema.table (3-part qualified name)
- ALU: FROM catalog.schema.table (Databricks/Spark 3-part naming with Unity Catalog)
- ALU: Multiple tables in FROM without JOIN: implicit cross join (cartesian product)
- ALU: Table aliases: short names for readability; required for self-joins
- ALU: FROM subquery: SELECT * FROM (SELECT ...) AS subq
- ALU: FROM VALUES: SELECT * FROM (VALUES (1,'a'),(2,'b')) AS t(id,name)
- ALU: FROM CTE: with cte AS (...) SELECT * FROM cte

**Subtopic: WHERE Clause**
- ALU: Filters rows after FROM (before GROUP BY/HAVING)
- ALU: Comparison operators: =, <>, !=, <, <=, >, >=
- ALU: BETWEEN a AND b: inclusive on both ends; equivalent to >= a AND <= b
- ALU: IN (v1, v2, v3): matches any value in list; short for multiple OR conditions
- ALU: IN (subquery): correlated or uncorrelated subquery
- ALU: NOT IN: excludes matching rows; dangerous if subquery can return NULL
- ALU: LIKE 'pattern': % matches any sequence; _ matches exactly one character
- ALU: ILIKE: case-insensitive LIKE (PostgreSQL); LIKE with CI collation (SQL Server)
- ALU: IS NULL / IS NOT NULL: only correct way to test for NULL
- ALU: EXISTS (subquery): true if subquery returns any row; often faster than IN for large subqueries
- ALU: NOT EXISTS: true if subquery returns no rows
- ALU: SOME / ANY / ALL with subquery: quantified comparisons
- ALU: Logical operators: AND, OR, NOT; precedence: NOT > AND > OR; use parentheses explicitly
- ALU: CASE in WHERE: WHERE CASE WHEN ... END = value

**Subtopic: ORDER BY**
- ALU: ORDER BY col ASC: ascending (default); ORDER BY col DESC: descending
- ALU: ORDER BY col1, col2: multi-column sort; second column breaks ties from first
- ALU: ORDER BY column_position: ORDER BY 2 (second column); works but brittle
- ALU: ORDER BY alias: ORDER BY total_value (alias defined in SELECT)
- ALU: NULLS FIRST / NULLS LAST: explicit null placement in sort
- ALU: ORDER BY without LIMIT: expensive sort for display only; avoid on large tables
- ALU: ORDER BY in subquery: ignored unless LIMIT present (most databases)

---

### TOPIC 4.1.2 — Filtering and Operators

**Subtopic: Comparison Operators**
- ALU: = (equality); <> or != (inequality); both ANSI standard
- ALU: <, <=, >, >= for ordered types (numbers, strings, dates)
- ALU: String comparison: lexicographic by collation
- ALU: Date comparison: WHERE order_date >= '2024-01-01' (date literal format)
- ALU: BETWEEN: inclusive; WHERE age BETWEEN 18 AND 65 = WHERE age >= 18 AND age <= 65
- ALU: BETWEEN with dates: WHERE ts BETWEEN '2024-01-01' AND '2024-01-31 23:59:59'

**Subtopic: Pattern Matching**
- ALU: LIKE '%text%': contains; expensive (no index use); full scan required
- ALU: LIKE 'text%': starts with; CAN use index if on first char
- ALU: LIKE '%text': ends with; cannot use index
- ALU: _ (underscore): matches exactly one character; LIKE 'J_n' matches Jan, Jun, Jon
- ALU: ESCAPE character: LIKE '50\\%' ESCAPE '\\\\' matches literal '50%'
- ALU: SIMILAR TO (PostgreSQL): SQL-standard regex-lite
- ALU: ~ (PostgreSQL): POSIX regex match; ~* case-insensitive
- ALU: REGEXP / RLIKE (MySQL/Spark): PCRE regular expressions
- ALU: REGEXP_LIKE (Oracle/Spark): function form
- ALU: Spark: rlike('pattern'), col.rlike(pattern)

**Subtopic: Set Operators**
- ALU: UNION: combine result sets, remove duplicates (uses sort/hash)
- ALU: UNION ALL: combine without dedup; faster; use when duplicates don't matter
- ALU: INTERSECT: rows in both result sets; remove duplicates
- ALU: INTERSECT ALL: rows in both with duplicates preserved
- ALU: EXCEPT / MINUS: rows in first set not in second; remove duplicates
- ALU: EXCEPT ALL: rows in first not in second with duplicates
- ALU: Requirements: same column count and compatible types in each SELECT
- ALU: Column names from first SELECT in UNION; second SELECT names ignored
- ALU: ORDER BY after UNION: applies to combined result

**ANIMATION SPEC 4.1.2 — UNION/INTERSECT/EXCEPT:**
```
Two circles (Venn diagram)
Left circle: rows from query 1 (labeled with sample data)
Right circle: rows from query 2
UNION: both circles fill highlight; overlap deduplicated
UNION ALL: both circles fill; overlap shown twice
INTERSECT: only overlap highlighted
EXCEPT: only left-unique highlighted
Transition animation between each operation type
```

---

### TOPIC 4.1.3 — Aggregation Functions

**Subtopic: Aggregate Functions**
- ALU: COUNT(*): count all rows including NULLs
- ALU: COUNT(col): count non-NULL values in col
- ALU: COUNT(DISTINCT col): count distinct non-NULL values
- ALU: SUM(col): sum of non-NULL values; NULL if all values NULL
- ALU: AVG(col): average of non-NULL values; same NULL behavior
- ALU: MIN(col): minimum value; ignores NULLs; works on strings and dates
- ALU: MAX(col): maximum value; ignores NULLs; works on strings and dates
- ALU: STDDEV(col) / STDDEV_POP / STDDEV_SAMP: standard deviation
- ALU: VARIANCE / VAR_POP / VAR_SAMP: variance
- ALU: BOOL_AND / BOOL_OR (PostgreSQL): logical aggregation
- ALU: STRING_AGG(col, delimiter) / GROUP_CONCAT / LISTAGG: concatenate strings
- ALU: ARRAY_AGG(col): aggregate values into array (PostgreSQL/Spark)
- ALU: COLLECT_LIST / COLLECT_SET: Spark aggregate to list/set

**Subtopic: GROUP BY**
- ALU: Groups rows with identical values in specified columns
- ALU: Non-aggregated SELECT columns must appear in GROUP BY (ANSI standard)
- ALU: MySQL exception: allows non-grouped columns (hidden dependency; non-deterministic)
- ALU: GROUP BY col1, col2: each unique combination of col1+col2 is one group
- ALU: GROUP BY with ROLLUP: GROUP BY ROLLUP(a, b) = GROUP BY a,b + GROUP BY a + GROUP BY ()
- ALU: GROUP BY with CUBE: all combinations of grouping columns
- ALU: GROUPING SETS: explicit list of grouping combinations
- ALU: GROUPING() function: returns 1 if column is aggregated over in current row
- ALU: Execution order: WHERE filters rows → GROUP BY groups → HAVING filters groups → SELECT projects → ORDER BY sorts

**Subtopic: HAVING**
- ALU: Filters groups after GROUP BY; analogous to WHERE but operates on aggregated values
- ALU: HAVING COUNT(*) > 10: only groups with more than 10 rows
- ALU: HAVING SUM(amount) > 1000: only groups where total > 1000
- ALU: HAVING vs WHERE: WHERE filters rows (before grouping); HAVING filters groups (after aggregating)
- ALU: HAVING can reference aliases if database resolves aliases before HAVING (non-standard; varies)
- ALU: Performance: push predicates into WHERE when possible; HAVING requires group computation first

**ANIMATION SPEC 4.1.3 — GROUP BY Visualizer:**
```
Table of rows with department and salary columns
GROUP BY department: rows animate grouping into colored clusters
Aggregate box appears over each cluster: SUM, COUNT, AVG computed
Result set animates: one row per cluster with aggregated values
HAVING filter: clusters not meeting condition fade out
ROLLUP: subtotal rows animate appearing after each group + grand total at bottom
```

---

### TOPIC 4.1.4 — JOINs: Complete Reference

**Subtopic: INNER JOIN**
- ALU: Returns rows where join condition is true in BOTH tables
- ALU: Syntax: FROM a INNER JOIN b ON a.id = b.a_id (INNER is optional)
- ALU: Non-matching rows from either side are excluded
- ALU: Multiple conditions: ON a.id = b.a_id AND a.year = b.year
- ALU: NATURAL JOIN: auto-join on identically named columns; avoid (fragile)
- ALU: USING clause: JOIN b USING (id) when column name identical in both tables
- ALU: Self join: table joined to itself; requires aliases
  ```sql
  SELECT e.name, m.name AS manager
  FROM employees e JOIN employees m ON e.manager_id = m.id
  ```

**Subtopic: LEFT/RIGHT/FULL OUTER JOIN**
- ALU: LEFT JOIN: all rows from left + matching from right; unmatched right = NULL
- ALU: RIGHT JOIN: all rows from right + matching from left; unmatched left = NULL
- ALU: FULL OUTER JOIN: all rows from both; unmatched side = NULL
- ALU: LEFT JOIN to find non-matches: WHERE right.id IS NULL (anti-join pattern)
- ALU: LEFT JOIN order matters in multi-join queries
- ALU: Spark: LEFT ANTI JOIN: returns left rows with no match (equivalent to LEFT JOIN WHERE NULL)

**Subtopic: CROSS JOIN**
- ALU: Cartesian product: every row of left × every row of right
- ALU: M rows × N rows = M×N result rows
- ALU: Use cases: generate date ranges with numbers table, expand values
- ALU: Accidental cross join: comma in FROM without join condition

**Subtopic: Multi-Table Joins**
- ALU: Chain joins: FROM a JOIN b ON ... JOIN c ON ... JOIN d ON ...
- ALU: Join order: optimizer chooses; hints available in most databases
- ALU: Associativity: (A JOIN B) JOIN C ≠ A JOIN (B JOIN C) for outer joins
- ALU: Star schema queries: fact JOIN dim1 JOIN dim2 JOIN dim3
- ALU: Snowflake schema: dim tables also join to sub-dimension tables (more joins)
- ALU: Join elimination: optimizer removes joins to tables whose columns aren't used (FK known)

**Subtopic: JOIN Performance**
- ALU: Hash join: build smaller table into hash map; probe with larger; O(n+m)
- ALU: Nested loop: for each outer row, scan inner; good for small inner or indexed inner
- ALU: Sort-merge join: sort both on join key; merge scan; O(n log n + m log m)
- ALU: Broadcast join (Spark): small table broadcast to all executors; no shuffle
- ALU: Broadcast threshold: spark.sql.autoBroadcastJoinThreshold = 10MB default
- ALU: Skewed join: one join key has disproportionately many rows; Spark AQE handles automatically
- ALU: Index join (row databases): nested loop with index scan on inner table
- ALU: Join spill: hash join hash table too large for memory → spill to disk → slow

**ANIMATION SPEC 4.1.4 — JOIN Visualizer:**
```
Two tables side by side: Customers (left) and Orders (right)
JOIN type selector: INNER / LEFT / RIGHT / FULL OUTER / CROSS
INNER JOIN: matching rows draw connecting lines; unmatched faded
LEFT JOIN: left rows all kept; right side shows NULL for unmatched
RIGHT JOIN: mirror of left
FULL OUTER: both sides kept; unmatched show NULL on other side
Row matching animation: arrows from left row to matching right row(s)
Result table animates building below
Anti-join pattern demo: LEFT JOIN WHERE right.id IS NULL highlighted
```

**INTERACTION SPEC 4.1.4 — Join Simulator:**
```
Two configurable tables (editable rows/columns)
SELECT join type from dropdown
ON condition builder: column1 = column2
Execute: animated join process
Show result with source row highlighting
Explain: shows which rows matched, which didn't
```

---

### TOPIC 4.1.5 — Subqueries

**Subtopic: Subquery Types**
- ALU: Scalar subquery: returns exactly one row one column; used in SELECT or WHERE
- ALU: Row subquery: returns one row multiple columns; used with row constructors
- ALU: Table subquery: returns multiple rows/columns; used in FROM or IN
- ALU: Correlated subquery: references outer query columns; re-evaluated per outer row
- ALU: Non-correlated subquery: independent of outer query; evaluated once

**Subtopic: Scalar Subqueries**
- ALU: SELECT col, (SELECT MAX(salary) FROM emp) AS max_salary FROM emp
- ALU: Must return exactly 0 or 1 row; error if > 1 row returned
- ALU: If returns 0 rows: evaluates to NULL
- ALU: Performance: often better rewritten as JOIN + aggregation

**Subtopic: IN / EXISTS Subqueries**
- ALU: WHERE id IN (SELECT id FROM t2): tests membership in result set
- ALU: IN evaluates subquery once; compares each outer row against result set
- ALU: EXISTS: WHERE EXISTS (SELECT 1 FROM t2 WHERE t2.id = t1.id)
- ALU: EXISTS stops at first match; IN materializes full subquery result
- ALU: EXISTS often faster than IN for large subqueries
- ALU: NOT IN with NULL in subquery: returns no rows (NULL comparison = UNKNOWN)
- ALU: NOT EXISTS: correct alternative to NOT IN; handles NULLs correctly
- ALU: ANY/SOME: WHERE price > ANY (SELECT price FROM products WHERE category='A')
- ALU: ALL: WHERE price > ALL (SELECT price FROM products WHERE category='A')

**Subtopic: Correlated Subqueries**
- ALU: Reference outer query in inner WHERE
- ALU: Re-executed for each outer row: O(n×m) if naive; optimizer may convert to join
- ALU: Example: SELECT * FROM emp WHERE salary > (SELECT AVG(salary) FROM emp WHERE dept = emp.dept)
- ALU: LATERAL JOIN (PostgreSQL/Spark): correlated subquery in FROM that can reference earlier FROM items
- ALU: CROSS APPLY / OUTER APPLY (SQL Server): equivalent to LATERAL JOIN

**Subtopic: Derived Tables and CTEs**
- ALU: Derived table: subquery in FROM clause; evaluated once; must be aliased
- ALU: CTE (Common Table Expression): WITH clause; named, reusable within query
- ALU: CTE syntax: WITH cte_name AS (SELECT ...) SELECT * FROM cte_name
- ALU: Multiple CTEs: WITH a AS (...), b AS (...) SELECT * FROM a JOIN b ON ...
- ALU: CTE vs derived table: same semantics; CTE more readable; CTE can be referenced multiple times
- ALU: Recursive CTE: traverses hierarchies; WITH RECURSIVE (PostgreSQL/ANSI) or WITH without keyword (SQL Server)
- ALU: Recursive CTE structure: anchor member UNION ALL recursive member with termination condition
- ALU: Example: employee hierarchy traversal (CEO → managers → employees)
- ALU: CTE materialization: some databases materialize CTE (evaluate once); others inline it
- ALU: Spark: CTE inlined; no materialization guarantee; use temp views or cache() for reuse

**ANIMATION SPEC 4.1.5 — Correlated Subquery:**
```
Outer query shown: SELECT * FROM employees
For each outer row: inner subquery highlights and evaluates
Result from inner query shown in popup
Outer row kept/filtered based on comparison
Next outer row: inner query re-evaluates with new correlated value
Counter: shows how many times inner query executes
Alternative: rewritten as JOIN+GROUP BY shown side-by-side
Performance comparison: correlated vs. JOIN timing
```

---

## MODULE 4.2 — Advanced SQL

### TOPIC 4.2.1 — Window Functions

**Subtopic: Window Function Fundamentals**
- ALU: Operates on a set of rows related to current row (the "window")
- ALU: Does NOT collapse rows (unlike GROUP BY aggregation)
- ALU: Returns one value per row; the window is defined per row
- ALU: Syntax: function() OVER (PARTITION BY ... ORDER BY ... ROWS/RANGE BETWEEN ...)
- ALU: Evaluated after WHERE, GROUP BY, HAVING; before SELECT, DISTINCT, LIMIT
- ALU: Cannot use window functions in WHERE or HAVING
- ALU: Must use subquery/CTE to filter on window function result

**Subtopic: PARTITION BY and ORDER BY in Window**
- ALU: PARTITION BY: divides rows into groups (partitions); function resets per partition
- ALU: PARTITION BY is optional; if omitted, entire result set is one partition
- ALU: ORDER BY in OVER: defines row order within partition; required for ranking + running aggregates
- ALU: ORDER BY in OVER vs. query ORDER BY: independent; both can coexist
- ALU: Default frame with ORDER BY: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
- ALU: Default frame without ORDER BY: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

**Subtopic: Frame Clause**
- ALU: ROWS: physical row offset
- ALU: RANGE: logical value offset (requires ORDER BY on numeric or date)
- ALU: GROUPS (PostgreSQL 11+): group offset
- ALU: UNBOUNDED PRECEDING: from start of partition
- ALU: CURRENT ROW: current row or last row with same ORDER BY value (RANGE)
- ALU: UNBOUNDED FOLLOWING: to end of partition
- ALU: N PRECEDING / N FOLLOWING: fixed offset
- ALU: ROWS BETWEEN 6 PRECEDING AND CURRENT ROW: 7-row rolling window
- ALU: RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW: 7-day date range window
- ALU: EXCLUDE CURRENT ROW / EXCLUDE GROUP / EXCLUDE TIES (PostgreSQL 11+)

**Subtopic: Ranking Functions**
- ALU: ROW_NUMBER(): unique integer per row; no ties; 1,2,3,4,5
- ALU: RANK(): same value gets same rank; gaps after ties; 1,2,2,4,5
- ALU: DENSE_RANK(): same value same rank; no gaps; 1,2,2,3,4
- ALU: NTILE(n): divides partition into n buckets; assigns bucket number
- ALU: CUME_DIST(): cumulative distribution; fraction of partition rows <= current row value
- ALU: PERCENT_RANK(): relative rank 0–1; (rank-1)/(rows-1)
- ALU: ROW_NUMBER() use case: deduplication — WHERE rn = 1 per partition

**Subtopic: Offset Functions**
- ALU: LAG(col, offset, default): value of col from offset rows before current row
- ALU: LEAD(col, offset, default): value of col from offset rows after current row
- ALU: LAG(price, 1) OVER (ORDER BY date): previous day's price
- ALU: LEAD(price, 1) OVER (ORDER BY date): next day's price
- ALU: default parameter: returned when offset goes beyond partition boundary
- ALU: Day-over-day change: price - LAG(price,1) OVER (PARTITION BY ticker ORDER BY date)
- ALU: Period-over-period: amount / LAG(amount, 12) OVER (PARTITION BY product ORDER BY month) - 1

**Subtopic: FIRST_VALUE and LAST_VALUE**
- ALU: FIRST_VALUE(col) OVER (PARTITION BY ... ORDER BY ...): value of col from first row of window frame
- ALU: LAST_VALUE(col) OVER (...): value of col from last row of current window frame
- ALU: LAST_VALUE pitfall: default frame is RANGE UNBOUNDED PRECEDING TO CURRENT ROW; last value = current row!
- ALU: Fix: LAST_VALUE(col) OVER (...ORDER BY... ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
- ALU: NTH_VALUE(col, n): value of col from nth row of window frame

**Subtopic: Aggregate Window Functions**
- ALU: SUM(amount) OVER (PARTITION BY customer ORDER BY date): running total per customer
- ALU: AVG(price) OVER (PARTITION BY product ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW): 7-day moving avg
- ALU: COUNT(*) OVER (PARTITION BY dept): total count of dept rows (no ORDER BY = static per partition)
- ALU: MAX(price) OVER (PARTITION BY month): max price in month (shown on every row)
- ALU: Ratio to total: SUM(amount) / SUM(SUM(amount)) OVER (PARTITION BY dept) AS pct_of_dept

**ANIMATION SPEC 4.2.1 — Window Functions:**
```
Table of sales rows (date, customer, amount)
PARTITION BY customer: rows animate grouping by colored border; customer boundaries visible
ORDER BY date within partition: rows reorder within each group
ROW_NUMBER(): numbers appear in each row, resetting per partition
SUM() OVER with running total: cumulative sum column animates building row by row
LAG(): previous row value animates connecting to current row
Rolling average: frame window (blue highlight band) slides down rows
Frame controls: user can drag window size; aggregate updates live
```

**INTERACTION SPEC 4.2.1 — Window Builder:**
```
Table with configurable data
Function selector: ROW_NUMBER/RANK/DENSE_RANK/SUM/AVG/LAG/LEAD
PARTITION BY: select columns
ORDER BY: select column + ASC/DESC
Frame: ROWS/RANGE sliders for preceding/following
Execute: shows result column added to table
Explain: shows which rows are in window for highlighted row
```

---

### TOPIC 4.2.2 — CTEs and Recursive Queries

**Subtopic: CTE Deep Dive**
- ALU: WITH clause: defines named result sets for use in subsequent query
- ALU: Multiple CTEs: WITH a AS (...), b AS (...), c AS (...) SELECT ...
- ALU: CTE can reference earlier CTE: WITH a AS (...), b AS (SELECT * FROM a WHERE ...)
- ALU: CTE naming: use descriptive names (cleaned_orders, filtered_customers)
- ALU: CTE vs subquery: identical semantics (in most DBs); CTE preferred for readability
- ALU: CTE materialization: PostgreSQL materializes by default (MATERIALIZED/NOT MATERIALIZED hint available)
- ALU: SQL Server: CTE not materialized; inlined into query
- ALU: Spark: CTE inlined; use cache() or temp view for actual reuse across queries

**Subtopic: Recursive CTEs**
- ALU: Syntax: WITH RECURSIVE cte AS (anchor UNION ALL recursive)
- ALU: Anchor: base case (non-recursive SELECT); defines starting rows
- ALU: Recursive: selects from cte itself + joins to additional tables
- ALU: Termination: when recursive SELECT returns no rows
- ALU: Cycle detection: CYCLE clause (PostgreSQL 14+) or manual depth limit
- ALU: Employee hierarchy example:
  ```sql
  WITH RECURSIVE hierarchy AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e JOIN hierarchy h ON e.manager_id = h.id
  )
  SELECT * FROM hierarchy ORDER BY level, name
  ```
- ALU: Part explosion (BOM): recursive BOM traversal for manufacturing
- ALU: Graph traversal: shortest path, reachability
- ALU: Maximum recursion: SQL Server default 100; use MAXRECURSION option
- ALU: Spark recursive: not natively supported; use iterative approach or GraphX

---

### TOPIC 4.2.3 — CASE Expressions

**Subtopic: CASE Syntax**
- ALU: Simple CASE: CASE col WHEN val1 THEN res1 WHEN val2 THEN res2 ELSE default END
- ALU: Searched CASE: CASE WHEN condition1 THEN res1 WHEN condition2 THEN res2 ELSE default END
- ALU: CASE is an expression, not a statement; use anywhere expression expected
- ALU: CASE in SELECT: computed column
- ALU: CASE in WHERE: conditional filtering
- ALU: CASE in ORDER BY: conditional sorting
- ALU: CASE in GROUP BY: group by derived category
- ALU: CASE in aggregate: SUM(CASE WHEN status='complete' THEN amount ELSE 0 END) — conditional sum
- ALU: Nested CASE: CASE WHEN ... THEN CASE WHEN ... END END (avoid if possible)
- ALU: IIF() (SQL Server): IIF(condition, true_val, false_val) — syntactic shorthand
- ALU: IF() (MySQL/Spark): IF(condition, true_val, false_val)
- ALU: DECODE() (Oracle): similar to simple CASE
- ALU: CASE WHEN NULL: WHEN NULL THEN x never matches; use WHEN col IS NULL THEN x

**ANIMATION SPEC 4.2.3 — CASE Visualizer:**
```
Row-by-row evaluation shown
CASE expression highlighted in query
For each row: conditions tested in order top-to-bottom
First matching WHEN: result highlighted green
Non-matching WHENs: grayed out
ELSE: shown if no WHEN matched
Result value animates into result column
```

---

### TOPIC 4.2.4 — Transactions and DML

**Subtopic: INSERT**
- ALU: INSERT INTO table (col1,col2) VALUES (v1,v2)
- ALU: INSERT INTO table VALUES (v1,v2,v3) — must match all columns in order
- ALU: INSERT INTO table SELECT ... FROM ... — insert from query
- ALU: INSERT INTO ... ON CONFLICT DO NOTHING / UPDATE (PostgreSQL upsert)
- ALU: INSERT IGNORE (MySQL): ignore duplicate key errors
- ALU: MERGE INTO target USING source ON condition WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT ...
- ALU: INSERT OVERWRITE (Spark/Hive): replaces partition data
- ALU: Multi-row INSERT: INSERT INTO t VALUES (1,'a'),(2,'b'),(3,'c') — more efficient than single-row

**Subtopic: UPDATE**
- ALU: UPDATE table SET col = value WHERE condition
- ALU: Update multiple columns: SET col1 = v1, col2 = v2
- ALU: UPDATE with expression: SET price = price * 1.1
- ALU: UPDATE FROM (SQL Server/PostgreSQL): UPDATE t SET col = s.col FROM source s WHERE t.id = s.id
- ALU: UPDATE with CTE: WITH u AS (SELECT ...) UPDATE table SET ... FROM u WHERE ...
- ALU: UPDATE without WHERE: updates ALL rows — extremely dangerous
- ALU: Safe update mode (MySQL): require WHERE includes key column

**Subtopic: DELETE**
- ALU: DELETE FROM table WHERE condition
- ALU: DELETE without WHERE: deletes ALL rows (table structure remains)
- ALU: TRUNCATE TABLE: delete all rows faster; not logged row-by-row; cannot be rolled back in some DBs
- ALU: DELETE with JOIN (SQL Server): DELETE t FROM t JOIN s ON t.id = s.id WHERE s.flag=1
- ALU: DELETE using CTE (PostgreSQL): WITH d AS (SELECT id FROM t WHERE ...) DELETE FROM t WHERE id IN (SELECT id FROM d)
- ALU: Delta Lake: DELETE FROM table WHERE condition — uses MERGE under the hood
- ALU: Delta Lake VACUUM: physically removes old Parquet files after DELETE/UPDATE

**Subtopic: MERGE (UPSERT)**
- ALU: Standard SQL MERGE: MERGE INTO target USING source ON (join condition) WHEN MATCHED ... WHEN NOT MATCHED ...
- ALU: WHEN MATCHED AND extra_condition: additional filter on matched rows
- ALU: WHEN NOT MATCHED BY SOURCE (SQL Server): handle rows in target not in source
- ALU: Delta Lake MERGE: full ANSI MERGE with schema evolution support
- ALU: Delta Lake MERGE example:
  ```sql
  MERGE INTO target t
  USING source s ON t.id = s.id
  WHEN MATCHED AND s.updated_at > t.updated_at THEN
    UPDATE SET t.name = s.name, t.updated_at = s.updated_at
  WHEN NOT MATCHED THEN
    INSERT (id, name, created_at, updated_at) VALUES (s.id, s.name, s.created_at, s.updated_at)
  WHEN NOT MATCHED BY SOURCE THEN
    DELETE
  ```

---

### TOPIC 4.2.5 — DDL: Tables, Constraints, Indexes

**Subtopic: CREATE TABLE**
- ALU: CREATE TABLE schema.table_name (col1 type1 [constraints], col2 type2 ...)
- ALU: Column constraints: NOT NULL, DEFAULT value, CHECK (expression), UNIQUE, PRIMARY KEY, REFERENCES
- ALU: Table constraints: named constraints, composite keys
- ALU: CREATE TABLE IF NOT EXISTS: no error if exists
- ALU: CREATE TABLE AS SELECT ... (CTAS): create table from query result
- ALU: Spark: CREATE TABLE USING DELTA AS SELECT ...; LOCATION 'path' for external table
- ALU: External vs managed table: external = data persists beyond DROP TABLE

**Subtopic: ALTER TABLE**
- ALU: ALTER TABLE ADD COLUMN col type: add new column (typically fast, metadata-only)
- ALU: ALTER TABLE DROP COLUMN col: remove column
- ALU: ALTER TABLE ALTER COLUMN col TYPE new_type: change data type (may rewrite table)
- ALU: ALTER TABLE RENAME COLUMN old_name TO new_name
- ALU: ALTER TABLE RENAME TO new_table_name
- ALU: ALTER TABLE ADD CONSTRAINT name type: add constraint after table creation
- ALU: ALTER TABLE DROP CONSTRAINT name: remove constraint
- ALU: Delta Lake: ALTER TABLE SET TBLPROPERTIES; ALTER TABLE ADD COLUMNS; ALTER TABLE CHANGE COLUMN

**Subtopic: Views**
- ALU: CREATE VIEW name AS SELECT ...: virtual table; query stored; data not materialized
- ALU: SELECT FROM view: view expanded inline; no storage
- ALU: View benefits: abstraction, security (restrict columns), reusability
- ALU: Updateable views: limited conditions; avoid in practice
- ALU: Materialized view: query result stored physically; must be refreshed
- ALU: CREATE MATERIALIZED VIEW: PostgreSQL/Oracle; refresh on schedule or on demand
- ALU: Spark: CREATE OR REPLACE VIEW; equivalent to stored SQL definition
- ALU: Databricks: LIVE tables in DLT = materialized views with incremental refresh

**Subtopic: CREATE INDEX**
- ALU: CREATE INDEX idx_name ON table (col1 [ASC/DESC])
- ALU: CREATE UNIQUE INDEX idx_name ON table (col)
- ALU: CREATE INDEX ... WHERE condition: partial index (PostgreSQL)
- ALU: CREATE INDEX ON table (LOWER(col)): expression index (PostgreSQL)
- ALU: INCLUDE clause (SQL Server/PostgreSQL): non-key columns in leaf pages for covering index
- ALU: DROP INDEX idx_name: remove index
- ALU: REINDEX TABLE / REBUILD INDEX: rebuild fragmented index
- ALU: Delta Lake: CREATE BLOOMFILTER INDEX ON TABLE t FOR COLUMNS (col1)
- ALU: Delta Lake: OPTIMIZE TABLE t ZORDER BY (col1, col2): Z-order clustering

---

### TOPIC 4.2.6 — Advanced Aggregation

**Subtopic: ROLLUP**
- ALU: GROUP BY ROLLUP(a, b, c): generates: (a,b,c), (a,b), (a), ()
- ALU: Produces subtotals and grand total automatically
- ALU: NULL in ROLLUP result represents the "all values" aggregation level
- ALU: GROUPING(col): returns 1 if col is rolled up in this row (NULL from ROLLUP)
- ALU: Use GROUPING() to distinguish real NULLs from ROLLUP NULLs

**Subtopic: CUBE**
- ALU: GROUP BY CUBE(a, b, c): all 2^3 = 8 combinations of grouping
- ALU: More comprehensive than ROLLUP; crosses all dimension combinations
- ALU: Result has 2^n rows times the base data (can be large)
- ALU: Use case: OLAP-style cross-tabulation queries

**Subtopic: GROUPING SETS**
- ALU: GROUP BY GROUPING SETS((a,b),(a),(b),()): explicit list of groupings
- ALU: More control than ROLLUP or CUBE; choose exactly which aggregations needed
- ALU: Equivalent to UNION ALL of multiple GROUP BY queries (but more efficient)
- ALU: Spark: ROLLUP, CUBE, GROUPING SETS all supported in SparkSQL

**Subtopic: Conditional Aggregation**
- ALU: SUM(CASE WHEN status='paid' THEN amount ELSE 0 END) AS paid_total
- ALU: COUNT(CASE WHEN flag=1 THEN 1 END) AS flag_count (COUNT ignores NULLs)
- ALU: AVG(CASE WHEN country='US' THEN amount END) AS us_avg
- ALU: FILTER clause (ANSI SQL/PostgreSQL): SUM(amount) FILTER (WHERE status='paid')
- ALU: FILTER is cleaner than CASE; same semantics; better readability

---

### TOPIC 4.2.7 — String Functions Complete Reference

**Subtopic: String Manipulation**
- ALU: LENGTH/LEN(str): character count; OCTET_LENGTH: byte count
- ALU: UPPER(str) / LOWER(str): case conversion
- ALU: TRIM(str) / LTRIM / RTRIM: remove spaces; TRIM(chars FROM str): remove specified chars
- ALU: SUBSTRING(str, start, length) / SUBSTR / MID: extract substring
- ALU: LEFT(str, n) / RIGHT(str, n): extract from left/right
- ALU: CONCAT(s1, s2, ...) / s1 || s2: concatenation; CONCAT_WS(sep, s1, s2): with separator
- ALU: REPLACE(str, find, replace): replace all occurrences
- ALU: TRANSLATE(str, from_chars, to_chars): character-by-character replacement (PostgreSQL)
- ALU: LPAD(str, len, pad_char) / RPAD: pad string to length
- ALU: REPEAT(str, n): repeat string n times
- ALU: REVERSE(str): reverse string
- ALU: POSITION(sub IN str) / CHARINDEX / LOCATE: find substring position
- ALU: SPLIT_PART(str, delimiter, n) (PostgreSQL): extract nth field after splitting

**Subtopic: Pattern and Regex Functions**
- ALU: REGEXP_REPLACE(str, pattern, replacement): replace regex matches
- ALU: REGEXP_EXTRACT(str, pattern, group) (Spark/Hive): extract capture group
- ALU: REGEXP_LIKE(str, pattern): boolean match test
- ALU: REGEXP_SPLIT_TO_TABLE(str, pattern) (PostgreSQL): split string into rows

**Subtopic: Type Conversion**
- ALU: CAST(value AS type): standard SQL type conversion
- ALU: TRY_CAST(value AS type): returns NULL on failure instead of error
- ALU: CONVERT(type, value) (SQL Server): with optional style code
- ALU: TO_CHAR(number, format) / TO_CHAR(date, format): Oracle/PostgreSQL formatting
- ALU: TO_NUMBER(str, format): parse string to number
- ALU: FORMAT(value, format_string): SQL Server/MySQL formatting

---

### TOPIC 4.2.8 — Date Functions Complete Reference

**Subtopic: Date Arithmetic**
- ALU: DATEADD(day, 7, date) (SQL Server); DATE_ADD(date, INTERVAL 7 DAY) (MySQL); date + 7 (PostgreSQL)
- ALU: DATEDIFF(day, start, end) (SQL Server); DATEDIFF(end, start) (MySQL — reversed!)
- ALU: DATE_TRUNC('week', ts): truncate to start of week (Monday)
- ALU: DATE_TRUNC('month', ts): first day of month
- ALU: DATE_TRUNC('year', ts): Jan 1st of year
- ALU: LAST_DAY(date) (MySQL/Oracle): last day of month containing date
- ALU: EOMONTH(date) (SQL Server): end of month
- ALU: NEXT_DAY(date, 'MONDAY') (Oracle/Hive/Spark): next occurrence of weekday

**Subtopic: Date Parts**
- ALU: EXTRACT(YEAR FROM ts) / YEAR(ts) / DATE_PART('year', ts)
- ALU: EXTRACT(QUARTER FROM ts): returns 1-4
- ALU: EXTRACT(WEEK FROM ts): ISO week number
- ALU: EXTRACT(DOW FROM ts): day of week (PostgreSQL: 0=Sunday to 6=Saturday)
- ALU: EXTRACT(EPOCH FROM ts): Unix timestamp (seconds since 1970-01-01)
- ALU: EXTRACT(HOUR FROM ts), MINUTE, SECOND, MILLISECOND, MICROSECOND

**Subtopic: Date Formatting**
- ALU: FORMAT(ts, 'yyyy-MM-dd') (Spark/Hive): format timestamp to string
- ALU: TO_CHAR(ts, 'YYYY-MM-DD HH24:MI:SS') (PostgreSQL/Oracle)
- ALU: DATE_FORMAT(ts, '%Y-%m-%d') (MySQL)
- ALU: CONVERT(VARCHAR, ts, 121) (SQL Server): ISO format
- ALU: ISO 8601: YYYY-MM-DDTHH:MM:SS.sssZ (universal standard for data interchange)

---

### TOPIC 4.2.9 — Performance Tuning SQL

**Subtopic: Query Optimization Principles**
- ALU: Rule 1: Filter early — push WHERE predicates as close to data source as possible
- ALU: Rule 2: Reduce rows before joins — filter each table before joining
- ALU: Rule 3: Avoid SELECT * — read only needed columns (especially in Parquet/columnar)
- ALU: Rule 4: Use covering indexes — all columns in query available in index
- ALU: Rule 5: Avoid functions on indexed columns in WHERE — index won't be used
- ALU: Rule 6: Use EXPLAIN ANALYZE — verify actual vs estimated rows; find spills
- ALU: Rule 7: Update statistics — ANALYZE table / UPDATE STATISTICS
- ALU: Rule 8: Avoid implicit type casts — explicit CAST; prevent index scan inhibition
- ALU: Rule 9: Use set-based operations — avoid row-by-row cursors/loops
- ALU: Rule 10: Partition large tables — partition pruning eliminates irrelevant partitions

**Subtopic: Common Anti-Patterns**
- ALU: N+1 query: loop in application executing 1 query per item → replace with single JOIN
- ALU: Implicit cross join: FROM a, b without WHERE condition → cartesian product
- ALU: Correlated subquery in SELECT: re-executes per row → rewrite as JOIN
- ALU: OR with different indexed columns: index on each; bitmap union needed
- ALU: DISTINCT overuse: masks duplicate problem; fix the root cause
- ALU: Aggregate in subquery then join: materialize aggregate first in CTE
- ALU: Selecting unused columns: wider rows → more I/O
- ALU: Non-sargable predicate: WHERE YEAR(date_col) = 2024 → use >= '2024-01-01' AND < '2025-01-01'
- ALU: Sargable: Search ARGument ABLE — predicate that can use index

**Subtopic: Execution Plan Analysis**
- ALU: PostgreSQL EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT): actual rows, time, buffer hits
- ALU: Large actual vs estimated rows discrepancy: stale statistics → ANALYZE
- ALU: SQL Server SET STATISTICS IO ON: shows logical reads per table
- ALU: SQL Server SET STATISTICS TIME ON: CPU and elapsed time per statement
- ALU: Databricks Spark UI SQL tab: shows logical and physical plan
- ALU: Key metrics: HashAggregate/SortMergeJoin with spill → add executor memory
- ALU: Exchange (shuffle) bytes in Spark: measure inter-node data movement
- ALU: AQE (Adaptive Query Execution): Spark re-optimizes plan at runtime based on actual stats

**ANIMATION SPEC 4.2.9 — Query Optimizer:**
```
SQL query shown at top
Parse tree generated: animated AST construction
Optimizer tries 3 plan alternatives shown side by side
Cost model assigns cost to each: CPU + I/O
Optimal plan selected (highlighted)
Execution animation: operators run bottom-up
Statistics panel: estimated vs actual row counts per operator
Red indicator when estimates > 10x off: "Stale statistics detected"
```

""")

print("Parts 2 and 3 written successfully!")
