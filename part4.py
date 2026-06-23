TARGET = r"D:\Personal\learn-with-me\MASTER_DATA_ENGINEERING_LEARNING_PLATFORM_SPECIFICATION.md"

content = r"""

---

# PART 4 — LEVEL 5: PYTHON FOR DATA ENGINEERING

**Domain Color:** `#3b82f6` | **Prerequisites:** Level 4 SQL | **Est. Hours:** 60+

---

## MODULE 5.1 — Python Foundations

### TOPIC 5.1.1 — Python Execution Model

- ALU: CPython: reference implementation; compiles .py → bytecode (.pyc); executes in VM
- ALU: bytecode: platform-independent; cached in __pycache__/; invalidated on source change
- ALU: dis module: inspect bytecode; dis.dis(func) shows opcodes
- ALU: GIL (Global Interpreter Lock): mutex protecting CPython object model; one thread executes bytecode at a time
- ALU: GIL impact: CPU-bound threads cannot run truly parallel; I/O-bound threads fine (GIL released during I/O)
- ALU: Workarounds: multiprocessing (separate processes, no GIL), Cython with nogil, C extensions releasing GIL
- ALU: Python 3.13+: experimental free-threaded mode (--disable-gil build)
- ALU: Memory management: reference counting + cyclic garbage collector
- ALU: Reference count: incremented on assignment, function call, container insert; decremented on del/scope exit
- ALU: Cyclic GC: handles reference cycles (a→b→a); generational: gen0 (new), gen1, gen2
- ALU: id(): memory address of object; is operator: identity (same object); == operator: equality
- ALU: Interning: small integers (-5 to 256) and short strings interned (shared objects)
- ALU: LEGB scope: Local → Enclosing → Global → Built-in lookup order
- ALU: global keyword: declares variable as global from inside function
- ALU: nonlocal keyword: declares variable as enclosing scope from inside closure

**ANIMATION SPEC 5.1.1 — Python Memory Model:**
```
Heap diagram: objects as boxes with reference count numbers
Variable names on left: arrows pointing to objects on heap
Assignment: new arrow drawn; ref count increments
del/reassign: arrow removed; ref count decrements to 0; object disappears
Cyclic GC: two objects with circular arrows; GC cycle sweeps them
```

---

### TOPIC 5.1.2 — Data Structures Deep Dive

**Subtopic: list**
- ALU: Dynamic array; amortized O(1) append; O(n) insert at arbitrary position
- ALU: Over-allocation: capacity grows by ~1.125x when full; avoids O(n^2) repeated resize
- ALU: list comprehension: [expr for x in iterable if condition]; faster than for+append
- ALU: Slicing: a[start:stop:step]; copy semantics; O(k) time and space
- ALU: sort(): in-place TimSort; stable; O(n log n); key= parameter
- ALU: sorted(): returns new list; same algorithm
- ALU: bisect module: binary search on sorted list; bisect_left, bisect_right, insort

**Subtopic: dict**
- ALU: Hash table; open addressing with pseudo-random probing (CPython 3.6+: insertion-ordered)
- ALU: Hash collision: handled by probing; load factor ~2/3 before resize
- ALU: O(1) average get/set/delete; O(n) worst case (all collisions)
- ALU: dict comprehension: {k: v for k, v in items}
- ALU: setdefault(key, default): insert if key absent; return value
- ALU: defaultdict(factory): auto-insert with factory() when key missing
- ALU: Counter(iterable): dict subclass counting element frequencies
- ALU: OrderedDict: preserves order pre-3.7; now mostly redundant; has move_to_end()
- ALU: ChainMap: logical overlay of multiple dicts; lookup traverses chain

**Subtopic: set / frozenset**
- ALU: Hash table of keys only; O(1) contains; O(n) iteration
- ALU: Set operations: | (union), & (intersection), - (difference), ^ (symmetric difference)
- ALU: set.add(), discard() (no error), remove() (KeyError if absent), pop() (arbitrary)
- ALU: frozenset: immutable; hashable; can be dict key or set member

**Subtopic: tuple**
- ALU: Immutable sequence; fixed-size array; faster than list for iteration
- ALU: Hashable if all elements hashable; use as dict key or set member
- ALU: Named tuple: collections.namedtuple; or typing.NamedTuple with type hints
- ALU: Unpacking: a, b, c = tup; starred: a, *rest = tup

**Subtopic: collections module**
- ALU: deque: doubly-linked list; O(1) appendleft/popleft; use for queues/sliding windows
- ALU: heapq: binary min-heap on list; heappush/heappop O(log n); nlargest/nsmallest
- ALU: array: typed array (like C array); more memory-efficient than list for homogeneous data

---

### TOPIC 5.1.3 — Functions

**Subtopic: Arguments**
- ALU: Positional args: def f(a, b)
- ALU: Default args: def f(a, b=10); evaluated ONCE at definition; mutable default bug
- ALU: *args: variadic positional; tuple inside function
- ALU: **kwargs: variadic keyword; dict inside function
- ALU: Keyword-only: def f(a, *, b): b must be passed as keyword
- ALU: Positional-only (3.8+): def f(a, b, /): a, b cannot be passed as keyword
- ALU: Argument order: positional → *args → keyword-only → **kwargs

**Subtopic: Closures**
- ALU: Inner function that references variables from enclosing scope
- ALU: Cell object: shared storage for closed-over variable
- ALU: Late binding: closure captures variable, not value; loop variable pitfall
- ALU: Fix loop closure: default arg capture or functools.partial

**Subtopic: Decorators**
- ALU: Decorator: function that takes function and returns function
- ALU: @functools.wraps(f): preserve __name__, __doc__ on wrapper
- ALU: @lru_cache(maxsize=None): memoization; thread-safe; key = args tuple
- ALU: @cache: Python 3.9+ alias for unbounded lru_cache
- ALU: @classmethod: cls as first arg; factory methods
- ALU: @staticmethod: no implicit first arg; utility function in class namespace
- ALU: @property: getter/setter/deleter for attribute-style access

**Subtopic: Generators**
- ALU: yield: suspends function; returns generator object; lazy evaluation
- ALU: Generator expression: (expr for x in iterable) — memory-efficient pipeline
- ALU: yield from: delegate to sub-generator; propagates values and exceptions
- ALU: send(value): resume generator passing value as result of yield
- ALU: StopIteration: raised when generator exhausted; drives for loops
- ALU: Data pipeline pattern: gen1 | gen2 | gen3 using generator composition

**ANIMATION SPEC 5.1.3 — Generator Pipeline:**
```
Three generator functions shown as pipes
Data flows right: source yields item → transform yields item → sink consumes
Memory: shows only one item in flight at a time
Counter: items processed vs items in memory (1 vs N)
Comparison: list-based (all N in memory) vs generator (1 at a time)
```

---

### TOPIC 5.1.4 — OOP in Python

**Subtopic: Classes**
- ALU: __init__: initializer (not constructor; object already created by __new__)
- ALU: __new__: actual object creation; rarely overridden; used for singletons/immutables
- ALU: Instance vs class vs static methods: self / cls / no implicit arg
- ALU: __slots__: declares fixed attribute set; reduces memory ~40%; prevents __dict__
- ALU: MRO (Method Resolution Order): C3 linearization; used for super() dispatch
- ALU: super(): delegates to next class in MRO; correct for multiple inheritance
- ALU: Abstract classes: abc.ABC; @abstractmethod; cannot instantiate directly
- ALU: dataclass (@dataclass): auto-generates __init__, __repr__, __eq__ from field annotations
- ALU: dataclass frozen=True: immutable; auto-generates __hash__

**Subtopic: Dunder Methods**
- ALU: __str__: human-readable string (str(obj), print(obj))
- ALU: __repr__: developer string; ideally eval-able; fallback for str
- ALU: __eq__, __ne__, __lt__, __le__, __gt__, __ge__: comparison
- ALU: __hash__: required if __eq__ defined; must be consistent with equality
- ALU: __len__, __getitem__, __setitem__, __delitem__, __contains__: sequence/mapping protocol
- ALU: __iter__, __next__: iterator protocol
- ALU: __enter__, __exit__: context manager protocol (with statement)
- ALU: __call__: make instance callable
- ALU: __getattr__, __setattr__, __delattr__: attribute access hooks
- ALU: __class_getitem__: support for generic aliases (list[int])

---

### TOPIC 5.1.5 — Error Handling

- ALU: try/except/else/finally: else runs if no exception; finally always runs
- ALU: Exception hierarchy: BaseException → Exception → most user exceptions
- ALU: Bare except: catches BaseException including KeyboardInterrupt/SystemExit; avoid
- ALU: except (TypeError, ValueError) as e: catch multiple types
- ALU: raise from: except SomeError as e: raise NewError("msg") from e — chains exceptions
- ALU: raise from None: suppress exception context
- ALU: Custom exceptions: subclass Exception; add attributes for structured error info
- ALU: contextlib.suppress(ExceptionType): silently ignore specific exceptions
- ALU: logging.exception("msg"): logs message + full traceback at ERROR level
- ALU: traceback module: format_exc(), extract_tb() for programmatic traceback handling

---

### TOPIC 5.1.6 — File I/O and Context Managers

- ALU: open(path, mode, encoding): modes r/w/a/rb/wb/r+; always specify encoding='utf-8'
- ALU: with open() as f: auto-closes on exit; use always
- ALU: f.read(): entire file as string; f.readline(): one line; f.readlines(): list of lines
- ALU: for line in f: memory-efficient line-by-line iteration
- ALU: f.write(s): write string; f.writelines(lines): write iterable of strings
- ALU: pathlib.Path: OOP path manipulation; p / 'subdir' / 'file.txt' concatenation
- ALU: Path.read_text() / write_text(): single-call file read/write
- ALU: Path.glob('**/*.csv'): recursive file listing
- ALU: tempfile.NamedTemporaryFile: secure temp file; auto-deleted on close
- ALU: io.StringIO / BytesIO: in-memory file-like objects; useful in tests

---

## MODULE 5.2 — Python for Data

### TOPIC 5.2.1 — pandas Complete Reference

**Subtopic: Core Concepts**
- ALU: DataFrame: 2D labeled data structure; column-oriented in memory
- ALU: Series: 1D labeled array; each DataFrame column is a Series
- ALU: Index: labels for rows; default RangeIndex; can be DatetimeIndex, MultiIndex
- ALU: Copy vs view: chained indexing creates views or copies unpredictably
- ALU: SettingWithCopyWarning: use .loc/.iloc directly to avoid ambiguity
- ALU: Memory layout: each column is contiguous C array; good for column operations

**Subtopic: I/O**
- ALU: pd.read_csv(path, sep, header, names, dtype, parse_dates, chunksize, encoding)
- ALU: pd.read_parquet(path, engine='pyarrow', columns=None): columnar read
- ALU: pd.read_excel(path, sheet_name, header, skiprows): openpyxl/xlrd engine
- ALU: pd.read_sql(query, con): SQLAlchemy connection or DBAPI2
- ALU: pd.read_json(path_or_string, orient, lines): lines=True for JSONL
- ALU: df.to_parquet(path, engine='pyarrow', compression='snappy', index=False)
- ALU: df.to_csv(path, index=False, encoding='utf-8')
- ALU: chunksize: read_csv/read_json in chunks; returns iterator; process large files

**Subtopic: Indexing**
- ALU: df[col]: select column; df[[col1,col2]]: select multiple columns
- ALU: df.loc[row_label, col_label]: label-based; inclusive on both ends
- ALU: df.iloc[row_int, col_int]: integer-based; exclusive end (like Python slice)
- ALU: df.loc[condition]: boolean mask filtering
- ALU: df.query("col > 5 and name == 'Alice'"): string expression; uses numexpr
- ALU: df.at[row, col]: fast scalar label access
- ALU: df.iat[row_int, col_int]: fast scalar integer access
- ALU: MultiIndex: df.loc[(level0, level1)] or df.loc[pd.IndexSlice[...]]

**Subtopic: Transformations**
- ALU: df.assign(new_col=lambda df: df.a + df.b): returns new df with added column
- ALU: df.apply(func, axis=0/1): apply function to columns (0) or rows (1)
- ALU: df[col].map(dict_or_func): element-wise transform on Series
- ALU: df[col].str.method(): vectorized string methods (str.lower, str.contains, str.split)
- ALU: df[col].dt.method(): datetime accessor (dt.year, dt.month, dt.floor)
- ALU: pd.get_dummies(df, columns): one-hot encode categorical columns
- ALU: df.melt(id_vars, value_vars): wide-to-long transformation
- ALU: df.pivot_table(values, index, columns, aggfunc): long-to-wide aggregation
- ALU: df.stack(): pivot innermost column level to row index
- ALU: df.unstack(): pivot innermost row level to columns

**Subtopic: GroupBy**
- ALU: df.groupby(by, sort=False): split-apply-combine
- ALU: .agg({'col1': 'sum', 'col2': ['mean', 'std']}): multiple agg functions
- ALU: .agg(new_name=pd.NamedAgg(column='col', aggfunc='sum')): named aggregation
- ALU: .transform(func): return same-index result for broadcasting back to original df
- ALU: .filter(func): keep groups where function returns True
- ALU: .apply(func): arbitrary function per group; flexible but slower
- ALU: as_index=False: return flat DataFrame instead of grouped index

**Subtopic: Merging**
- ALU: pd.merge(left, right, on, how, suffixes): SQL-style join
- ALU: how: inner/left/right/outer/cross
- ALU: left.merge(right, left_on='a', right_on='b'): different key names
- ALU: pd.merge_asof: merge on nearest key (time series join)
- ALU: pd.concat([df1, df2], axis=0, ignore_index=True): stack vertically
- ALU: pd.concat([df1, df2], axis=1): join horizontally by index alignment

**Subtopic: Performance**
- ALU: Vectorized operations: always prefer df[col] + df[col2] over apply with addition
- ALU: apply(axis=1): slow; Python loop over rows; avoid for large DataFrames
- ALU: numba: @jit-compiled UDFs for numeric apply operations
- ALU: eval()/query(): uses numexpr; avoids intermediate arrays; faster for large frames
- ALU: Categorical dtype: encode string columns with low cardinality; saves memory 50-90%
- ALU: Sparse arrays: pd.arrays.SparseArray for mostly-null data
- ALU: Chunked processing: pd.read_csv(chunksize=100000) for files too large for memory

**ANIMATION SPEC 5.2.1 — GroupBy Split-Apply-Combine:**
```
DataFrame shown with department column
groupby('department'): rows animate splitting into 3 groups
apply(sum): sum computed per group; shown animating
combine: result DataFrame animates reassembling
transform: result animates broadcasting back to original shape
Side-by-side: agg vs transform output shapes
```

---

### TOPIC 5.2.2 — PySpark Foundation (Preview)

- ALU: SparkContext/SparkSession: entry point; one per JVM; builder pattern
- ALU: DataFrame vs RDD: DataFrame has schema + Catalyst optimizer; RDD is raw objects
- ALU: Lazy evaluation: transformations build DAG; action triggers execution
- ALU: Transformations: select, filter, groupBy, join, withColumn, drop, distinct
- ALU: Actions: show, count, collect, take, write, foreach
- ALU: Catalyst: logical plan → analyzed → optimized logical → physical plan → code gen
- ALU: Tungsten: off-heap binary format; SIMD vectorization; whole-stage code generation
- ALU: Partition: unit of parallelism; one task per partition; default 200 post-shuffle
- ALU: spark.sql.shuffle.partitions: tune for cluster size; too many = overhead; too few = spill

---

## MODULE 5.3 — Linux for Data Engineers

### TOPIC 5.3.1 — Shell and File System

**Subtopic: Essential Commands**
- ALU: ls -la: list all files with permissions, size, date; -h for human-readable sizes
- ALU: find path -name "*.parquet" -mtime -7: find parquet files modified in last 7 days
- ALU: find . -type f -size +1G: files larger than 1GB
- ALU: du -sh */: disk usage of each subdirectory; du -sh * | sort -rh | head: top consumers
- ALU: df -h: filesystem disk usage; df -i: inode usage
- ALU: stat file: inode metadata; atime/mtime/ctime; size; permissions
- ALU: lsof -p PID: files open by process; lsof +D /path: processes using directory
- ALU: fuser -v /mnt/data: processes using mount point
- ALU: ln -s target link: create symbolic link; ln target link: hard link
- ALU: rsync -avz --progress src/ dest/: sync directories; only transfers changes

**Subtopic: Text Processing**
- ALU: grep -rn "pattern" path: recursive grep with line numbers
- ALU: grep -c: count matches; -l: only filenames; -v: invert; -i: case-insensitive
- ALU: grep -P "PCRE_pattern": Perl regex; -E: extended regex (egrep)
- ALU: awk '{print $1, $3}': print fields 1 and 3 (whitespace-delimited)
- ALU: awk -F',' '$3 > 100 {print $0}': comma-delimited filter on field 3
- ALU: awk '{sum+=$2} END {print sum}': accumulate sum
- ALU: sed 's/find/replace/g': global substitute in stream
- ALU: sed -n '10,20p': print lines 10-20; sed '/pattern/d': delete matching lines
- ALU: cut -d',' -f1,3: extract CSV fields 1 and 3
- ALU: sort -t',' -k2 -n: sort CSV by field 2 numerically
- ALU: sort -k2 -rn | head -10: top 10 by field 2 descending
- ALU: uniq -c: count consecutive duplicates; sort first for global dedup
- ALU: wc -l file: line count; wc -c: byte count; wc -w: word count
- ALU: tr -d '\r': remove carriage returns (Windows→Unix line endings)
- ALU: paste -d',' file1 file2: merge files column-wise

**Subtopic: Process Management**
- ALU: ps aux: all processes; ps aux | grep spark: filter for Spark
- ALU: top / htop: interactive process monitor; M sort by memory; P sort by CPU
- ALU: kill -9 PID: SIGKILL (cannot be caught); kill -15: SIGTERM (graceful)
- ALU: pkill -f "pattern": kill by command pattern
- ALU: nohup command &: run in background; immune to SIGHUP; output to nohup.out
- ALU: screen / tmux: terminal multiplexer; sessions survive SSH disconnect
- ALU: jobs: list background jobs; fg %1: bring job 1 to foreground
- ALU: strace -p PID: trace system calls; strace -e trace=network: filter to network calls
- ALU: lsof -i :8080: which process listening on port 8080
- ALU: netstat -tlnp / ss -tlnp: listening TCP ports with PID

**Subtopic: Permissions and Users**
- ALU: chmod 755 file / chmod u+x file: change permissions
- ALU: chown user:group file: change owner and group
- ALU: chown -R user:group dir: recursive ownership change
- ALU: sudo -u databricks command: run as another user
- ALU: sudo visudo: safely edit sudoers file
- ALU: id username: show UID, GID, supplementary groups
- ALU: groups username: list groups
- ALU: usermod -aG groupname username: add user to group (requires logout/login)
- ALU: su - username: switch user with login shell

**ANIMATION SPEC 5.3.1 — Linux Pipe Chain:**
```
Command: cat access.log | grep "ERROR" | awk '{print $5}' | sort | uniq -c | sort -rn | head -10
Each | shows as actual pipe
Data flows left to right as stream
Each stage shows: process name, count of lines in vs out
Final result: top 10 error codes with counts
Pause at each stage to explain what it does
```

---

### TOPIC 5.3.2 — Shell Scripting

**Subtopic: Bash Scripting Essentials**
- ALU: Shebang: #!/usr/bin/env bash (portable) or #!/bin/bash
- ALU: set -euo pipefail: exit on error (-e); unbound var error (-u); pipe failure (-o pipefail)
- ALU: Variables: var=value (no spaces); ${var}: reference; ${var:-default}: default if unset
- ALU: Command substitution: result=$(command) or result=`command` (backtick legacy)
- ALU: Arithmetic: $((a + b)); $(( var++ )); let var=5
- ALU: Arrays: arr=(a b c); ${arr[0]}; ${arr[@]} all elements; ${#arr[@]} length
- ALU: Conditionals: if [[ condition ]]; then ...; elif ...; else ...; fi
- ALU: [[ ]] vs [ ]: double bracket is bash-specific; no word splitting; supports && || regex
- ALU: String tests: [[ -z "$var" ]]: empty; [[ -n "$var" ]]: non-empty; [[ "$a" == "$b" ]]: equal
- ALU: File tests: [[ -f file ]]: regular file; [[ -d dir ]]: directory; [[ -r file ]]: readable
- ALU: Loops: for f in *.csv; do ...; done; while read line; do ...; done < file
- ALU: Functions: myfunc() { local var=val; echo "$var"; }; local scopes variables
- ALU: Exit codes: $? last exit code; explicit exit N; convention: 0=success, 1=general error
- ALU: Trap: trap 'cleanup_func' EXIT INT TERM: run on exit/interrupt
- ALU: Here-doc: psql <<EOF \n SQL here \n EOF; heredoc with variable interpolation
- ALU: Here-string: command <<< "string": single string as stdin

**Subtopic: Cron and Scheduling**
- ALU: crontab format: minute hour day month weekday command
- ALU: 0 2 * * * /scripts/daily_load.sh: run at 02:00 every day
- ALU: */15 * * * *: every 15 minutes
- ALU: 0 8-17 * * 1-5: hourly from 8-17 Mon-Fri
- ALU: crontab -e: edit; crontab -l: list; crontab -r: remove
- ALU: MAILTO=alerts@company.com: send stdout/stderr to email
- ALU: Run-parts: /etc/cron.daily/; /etc/cron.hourly/
- ALU: systemd timer: more reliable than cron; supports calendar spec; logs to journald

---

## MODULE 5.4 — Git for Data Engineers

### TOPIC 5.4.1 — Git Internals

**Subtopic: Object Model**
- ALU: Git is a content-addressable filesystem: objects stored by SHA-1 of content
- ALU: Object types: blob (file content), tree (directory), commit, tag
- ALU: Blob: pure content; no filename; identical content = one blob regardless of location
- ALU: Tree: list of (mode, name, SHA) entries; references blobs and other trees
- ALU: Commit: tree SHA + parent SHA(s) + author + committer + message
- ALU: Tag: annotated tag = object with tagger + message + target SHA
- ALU: .git/objects/: pack files and loose objects; git gc compresses loose objects
- ALU: git cat-file -p SHA: show object content; -t: show type
- ALU: git hash-object file: compute SHA without storing

**Subtopic: References**
- ALU: Branch: pointer to commit SHA; stored in .git/refs/heads/branchname
- ALU: HEAD: pointer to current branch (or commit in detached HEAD state)
- ALU: Detached HEAD: HEAD points directly to commit; commit not on any branch
- ALU: Remote tracking: refs/remotes/origin/main mirrors remote state
- ALU: FETCH_HEAD: SHA of last fetched commit
- ALU: MERGE_HEAD: SHA of commit being merged
- ALU: ORIG_HEAD: original HEAD before risky operation (merge/rebase/reset)

**Subtopic: Three Trees**
- ALU: Working directory: actual files on disk
- ALU: Index (staging area): snapshot of next commit; .git/index
- ALU: HEAD: last commit snapshot
- ALU: git add: working dir → index
- ALU: git commit: index → new commit + update HEAD
- ALU: git checkout: HEAD → index → working dir
- ALU: git reset HEAD~1 --soft: move HEAD back; keep index and working dir
- ALU: git reset HEAD~1 --mixed: move HEAD back; reset index; keep working dir
- ALU: git reset HEAD~1 --hard: move HEAD back; reset index; reset working dir (destructive)
- ALU: git restore --staged file: unstage (index → HEAD)
- ALU: git restore file: discard working changes (working dir → index)

**ANIMATION SPEC 5.4.1 — Git Three Trees:**
```
Three columns: Working Dir | Staging (Index) | HEAD
Files shown in each column with state indicator
git add file: file animates moving from Working Dir to Staging
git commit: Staging animates into new commit bubble with SHA label
git status: shows difference between columns
git diff: working vs index; git diff --cached: index vs HEAD
git reset --soft: commit disappears; content stays in staging
git reset --hard: all three columns revert (animated wipe)
```

---

### TOPIC 5.4.2 — Branching and Merging

**Subtopic: Branch Operations**
- ALU: git branch feature/xyz: create branch at HEAD
- ALU: git checkout -b feature/xyz: create + switch
- ALU: git switch -c feature/xyz: modern syntax (2.23+)
- ALU: git branch -d feature: delete merged branch; -D force-delete
- ALU: git branch -v: show last commit on each branch
- ALU: git branch --merged / --no-merged: filter by merge status
- ALU: Trunk-based development: short-lived branches, frequent merge to main
- ALU: GitFlow: main + develop + feature/release/hotfix branches (complex; less common now)

**Subtopic: Merging Strategies**
- ALU: Fast-forward merge: no divergence; just moves branch pointer forward; no merge commit
- ALU: 3-way merge: finds common ancestor; merges two tips; creates merge commit
- ALU: git merge --no-ff: always create merge commit even if fast-forward possible
- ALU: git merge --squash: combine all branch commits into one staged change; no merge commit
- ALU: Merge conflict: same lines changed in both branches; must manually resolve
- ALU: Conflict markers: <<<<<<< HEAD ... ======= ... >>>>>>> branch
- ALU: git mergetool: launch visual merge tool (vimdiff, meld, VS Code)
- ALU: git merge --abort: cancel ongoing merge; restore pre-merge state

**Subtopic: Rebasing**
- ALU: git rebase main: replay commits from current branch onto main tip
- ALU: Rebase vs merge: cleaner linear history vs preserved merge topology
- ALU: Interactive rebase: git rebase -i HEAD~5: reorder/squash/edit last 5 commits
- ALU: Squash: combine commits; pick → squash; write single message
- ALU: fixup: like squash but discard commit message
- ALU: reword: edit commit message only
- ALU: exec: run shell command between commits
- ALU: Golden rule: never rebase published commits (rewrites SHA; breaks collaborators)
- ALU: git pull --rebase: rebase local commits on top of fetched; avoids merge commit

**Subtopic: Cherry-pick and Stash**
- ALU: git cherry-pick SHA: apply single commit from another branch
- ALU: git cherry-pick A..B: apply range (exclusive A, inclusive B)
- ALU: git stash push -m "WIP: feature xyz": save dirty working tree
- ALU: git stash list: show all stashes
- ALU: git stash pop: apply most recent stash and remove from list
- ALU: git stash apply stash@{2}: apply specific stash without removing
- ALU: git stash drop stash@{0}: delete stash entry
- ALU: git stash branch new-branch: create branch from stash (avoids conflicts)

---

### TOPIC 5.4.3 — Git Workflows for Data Engineering

- ALU: Data pipeline repo: separate repos for ingestion/transformation/orchestration or monorepo
- ALU: Branch naming: feat/DE-123-add-bronze-layer; fix/DE-456-null-handling; chore/update-deps
- ALU: .gitignore: ignore .env, credentials.json, __pycache__, *.pyc, .databricks/, spark-warehouse/
- ALU: git-secrets: prevent committing secrets (API keys, passwords)
- ALU: pre-commit hooks: run linting/formatting before commit; pre-commit framework
- ALU: Commit message conventions: Conventional Commits: feat:, fix:, chore:, docs:, test:
- ALU: git log --oneline --graph --all: visual branch history
- ALU: git bisect: binary search commits to find regression introduction
- ALU: git blame file: show last commit modifying each line
- ALU: git shortlog -sn: commit counts by author
- ALU: Large files: git-lfs for model files, datasets; store pointer in git; blob in LFS server
- ALU: DVC: data version control; like git-lfs but for data pipelines; integrates with S3/ADLS
- ALU: Databricks Repos: git integration for notebooks; CI/CD push to cluster

""".lstrip()

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 4 written!")
