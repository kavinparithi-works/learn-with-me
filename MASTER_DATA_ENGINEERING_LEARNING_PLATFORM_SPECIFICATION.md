# MASTER DATA ENGINEERING LEARNING PLATFORM SPECIFICATION
## World-Class Educational Platform — Zero to Senior Azure Data Engineer + Databricks Professional

---

# PART 1 — PLATFORM OVERVIEW & DESIGN SYSTEM

---

## 1.1 PLATFORM IDENTITY

```
Platform Name    : Learn With Me — Data Engineering
Tagline          : From Zero to Senior Data Engineer
Target Audience  : Absolute beginners → Senior Azure Data Engineer → Databricks Professional
Comparable To    : Coursera · Udemy · DataCamp · Codecademy · Brilliant · Databricks Academy
Backend          : Firebase (Firestore + Auth + Storage)
Source Control   : GitHub via PAT (stored in Key Vault / environment variable — never commit to repo)
Deployment       : GitHub Pages (kavinparithi-works.github.io/learn-with-me)
```

---

## 1.2 CURRICULUM ARCHITECTURE OVERVIEW

The platform delivers learning through an 8-level hierarchy:

```
Level (1–12)
  └── Domain
        └── Module
              └── Topic
                    └── Subtopic
                          └── Sub-Subtopic
                                └── Sub-Sub-Subtopic
                                      └── Atomic Learning Unit (ALU)
```

Each **Atomic Learning Unit** is one lesson page containing:
- Learning Objective
- Prerequisites
- Concept Explanation
- Animated Illustration
- Interactive Playground
- Diagram Area
- Practice Exercise
- Knowledge Check Quiz

---

## 1.3 DESIGN SYSTEM

### 1.3.1 Design Philosophy

```
Inspiration: DataCamp + Brilliant + Codecademy + Microsoft Learn + Stripe Docs + Linear + Notion
Principle  : Clean · Professional · Educational · Spacious · Pastel
Anti-pattern: No neon · No dark clutter · No excessive animation · No flashy effects
```

### 1.3.2 COLOR SYSTEM (COMPLETE TOKEN SET)

```css
/* ── PRIMARY BRAND COLORS ── */
--color-blue-50:   #eff6ff;   /* Lightest blue wash */
--color-blue-100:  #dbeafe;   /* Pastel blue bg */
--color-blue-200:  #bfdbfe;   /* Light blue border */
--color-blue-300:  #93c5fd;   /* Mid blue */
--color-blue-400:  #60a5fa;   /* Pastel blue accent */
--color-blue-500:  #4f8ef7;   /* PRIMARY BLUE — buttons, links */
--color-blue-600:  #2563eb;   /* Dark blue hover */
--color-blue-700:  #1d4ed8;   /* Deep blue pressed */

--color-purple-50:  #faf5ff;  /* Lightest purple wash */
--color-purple-100: #f3e8ff;  /* Pastel purple bg */
--color-purple-200: #e9d5ff;  /* Light purple border */
--color-purple-300: #d8b4fe;  /* Mid purple */
--color-purple-400: #c084fc;  /* Pastel purple accent */
--color-purple-500: #8b5cf6;  /* PRIMARY PURPLE — secondary CTA */
--color-purple-600: #7c3aed;  /* Dark purple hover */

--color-green-50:   #f0fdf4;  /* Lightest green wash */
--color-green-100:  #dcfce7;  /* Pastel green bg */
--color-green-200:  #bbf7d0;  /* Light green border */
--color-green-300:  #86efac;  /* Mid green */
--color-green-400:  #4ade80;  /* Pastel green accent */
--color-green-500:  #22c55e;  /* PRIMARY GREEN — success, progress */

/* ── SUPPORTING NEUTRALS ── */
--color-gray-50:    #f9fafb;
--color-gray-100:   #f3f4f6;
--color-gray-200:   #e5e7eb;
--color-gray-300:   #d1d5db;
--color-gray-400:   #9ca3af;
--color-gray-500:   #6b7280;
--color-gray-600:   #4b5563;
--color-gray-700:   #374151;
--color-gray-800:   #1f2937;
--color-gray-900:   #111827;

--color-slate-50:   #f8fafc;
--color-slate-100:  #f1f5f9;
--color-slate-200:  #e2e8f0;

--color-off-white:  #fafafa;
--color-white:      #ffffff;

/* ── SEMANTIC FEEDBACK COLORS ── */
--color-success:        #22c55e;
--color-success-light:  #f0fdf4;
--color-success-border: #bbf7d0;
--color-warning:        #f59e0b;
--color-warning-light:  #fffbeb;
--color-warning-border: #fde68a;
--color-error:          #ef4444;
--color-error-light:    #fef2f2;
--color-error-border:   #fecaca;
--color-info:           #4f8ef7;
--color-info-light:     #eff6ff;
--color-info-border:    #bfdbfe;

/* ── DOMAIN ACCENT COLORS ── */
--color-domain-computer:    #4f8ef7;  /* Computer Fundamentals — blue */
--color-domain-data:        #8b5cf6;  /* Data Fundamentals — purple */
--color-domain-sql:         #f59e0b;  /* SQL — amber */
--color-domain-python:      #3b82f6;  /* Python — bright blue */
--color-domain-linux:       #f97316;  /* Linux — orange */
--color-domain-git:         #6366f1;  /* Git — indigo */
--color-domain-cloud:       #0ea5e9;  /* Cloud — sky */
--color-domain-azure:       #0078d4;  /* Azure — microsoft blue */
--color-domain-spark:       #e25c1a;  /* Spark — spark orange */
--color-domain-pyspark:     #3b82f6;  /* PySpark — blue */
--color-domain-delta:       #00a3e0;  /* Delta Lake — delta blue */
--color-domain-databricks:  #ff3621;  /* Databricks — databricks red */
--color-domain-streaming:   #8b5cf6;  /* Streaming — purple */
--color-domain-adf:         #0078d4;  /* ADF — azure blue */
--color-domain-governance:  #22c55e;  /* Governance — green */
--color-domain-devops:      #6366f1;  /* DevOps — indigo */
--color-domain-arch:        #64748b;  /* Architecture — slate */
```

### 1.3.3 TYPOGRAPHY SYSTEM

```css
/* ── FONT STACK ── */
--font-display:  'Space Grotesk', system-ui, sans-serif;  /* H1–H3, hero, titles */
--font-body:     'Inter', system-ui, sans-serif;           /* Body, labels, UI */
--font-mono:     'JetBrains Mono', 'Fira Code', monospace; /* Code, terminals */

/* ── TYPE SCALE ── */
--text-xs:    0.75rem;   /* 12px — labels, captions */
--text-sm:    0.875rem;  /* 14px — secondary text */
--text-base:  1rem;      /* 16px — body */
--text-lg:    1.125rem;  /* 18px — large body */
--text-xl:    1.25rem;   /* 20px — lead text */
--text-2xl:   1.5rem;    /* 24px — H4 */
--text-3xl:   1.875rem;  /* 30px — H3 */
--text-4xl:   2.25rem;   /* 36px — H2 */
--text-5xl:   3rem;      /* 48px — H1 */
--text-6xl:   3.75rem;   /* 60px — Hero */

/* ── LINE HEIGHTS ── */
--leading-tight:   1.2;
--leading-snug:    1.375;
--leading-normal:  1.6;
--leading-relaxed: 1.75;
--leading-loose:   2;

/* ── FONT WEIGHTS ── */
--weight-light:    300;
--weight-regular:  400;
--weight-medium:   500;
--weight-semibold: 600;
--weight-bold:     700;
--weight-black:    900;

/* ── LETTER SPACING ── */
--tracking-tight:  -0.025em;
--tracking-normal:  0em;
--tracking-wide:    0.025em;
--tracking-wider:   0.05em;
--tracking-widest:  0.1em;
```

### 1.3.4 SPACING SYSTEM

```css
--space-1:   4px;
--space-2:   8px;
--space-3:   12px;
--space-4:   16px;
--space-5:   20px;
--space-6:   24px;
--space-8:   32px;
--space-10:  40px;
--space-12:  48px;
--space-14:  56px;
--space-16:  64px;
--space-20:  80px;
--space-24:  96px;
--space-32:  128px;
```

### 1.3.5 BORDER RADIUS SYSTEM

```css
--radius-none:  0;
--radius-sm:    4px;
--radius-base:  8px;
--radius-md:    10px;
--radius-lg:    12px;
--radius-xl:    16px;
--radius-2xl:   20px;
--radius-3xl:   24px;
--radius-full:  9999px;
```

### 1.3.6 SHADOW SYSTEM

```css
--shadow-xs:   0 1px 2px rgba(0,0,0,0.04);
--shadow-sm:   0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
--shadow-md:   0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);
--shadow-lg:   0 10px 15px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.05);
--shadow-xl:   0 20px 25px rgba(0,0,0,0.09), 0 10px 10px rgba(0,0,0,0.04);
--shadow-2xl:  0 25px 50px rgba(0,0,0,0.12);
--shadow-blue: 0 4px 24px rgba(79,142,247,0.25);
--shadow-purple: 0 4px 24px rgba(139,92,246,0.25);
--shadow-green: 0 4px 24px rgba(34,197,94,0.20);
```

### 1.3.7 ANIMATION & TRANSITION SYSTEM

```css
/* ── DURATIONS ── */
--duration-instant:  50ms;
--duration-fast:     150ms;
--duration-normal:   220ms;
--duration-slow:     350ms;
--duration-slower:   500ms;
--duration-slowest:  800ms;

/* ── EASING ── */
--ease-linear:    linear;
--ease-in:        cubic-bezier(0.4, 0, 1, 1);
--ease-out:       cubic-bezier(0, 0, 0.2, 1);
--ease-in-out:    cubic-bezier(0.4, 0, 0.2, 1);
--ease-spring:    cubic-bezier(0.34, 1.56, 0.64, 1);
--ease-bounce:    cubic-bezier(0.68, -0.55, 0.265, 1.55);

/* ── STANDARD TRANSITIONS ── */
--transition-fast:   150ms cubic-bezier(0.4,0,0.2,1);
--transition-normal: 220ms cubic-bezier(0.4,0,0.2,1);
--transition-slow:   350ms cubic-bezier(0.4,0,0.2,1);

/* ANIMATION RULES:
   - All animations must TEACH, not decorate
   - Max 1 auto-playing animation per lesson section
   - User must be able to pause/replay every animation
   - Animations must not autoplay faster than 800ms per step
   - No infinite looping animations except subtle background pulses
   - Respect prefers-reduced-motion at all times
*/
```

### 1.3.8 LAYOUT SYSTEM

```
Page Structure:
┌─────────────────────────────────────────────────────┐
│  TOPBAR (fixed, 60px height)                        │
├────────────┬────────────────────────────────────────┤
│            │                                        │
│  SIDEBAR   │  MAIN CONTENT AREA                     │
│  (280px)   │  (max-width: 860px, centered)          │
│            │                                        │
│  fixed     │  scrollable                            │
│            │                                        │
└────────────┴────────────────────────────────────────┘

Content Max Widths:
--content-prose:    72ch;   /* Readable text column */
--content-wide:     860px;  /* Normal content */
--content-full:     1180px; /* Landing / hero sections */

Grid System: 12-column, 24px gutters, 60px margins
Breakpoints:
  --bp-sm:  640px
  --bp-md:  768px
  --bp-lg:  1024px
  --bp-xl:  1280px
  --bp-2xl: 1536px
```

---

## 1.4 COMPONENT LIBRARY SPECIFICATION

### 1.4.1 TOPBAR COMPONENT

```
Height: 60px
Background: rgba(255,255,255,0.96) with backdrop-filter: blur(12px)
Border-bottom: 1px solid var(--color-gray-100)
Position: fixed top-0 z-index:500

Left Section:
  - Logo mark (SVG, 28px) + "Learn With Me" wordmark
  - Active domain breadcrumb chip (e.g., "SQL › Joins")

Center Section:
  - Global search bar (280px wide)
  - Placeholder: "Search topics, lessons..."
  - Keyboard shortcut: Cmd/Ctrl+K

Right Section:
  - Progress ring (overall %) 
  - Streak badge (🔥 N days)
  - Notification bell
  - User avatar dropdown
    - Profile
    - My Progress
    - Certificates
    - Settings
    - Sign Out

Mobile: hamburger menu replaces sidebar toggle
```

### 1.4.2 SIDEBAR COMPONENT

```
Width: 280px
Background: #ffffff
Border-right: 1px solid var(--color-gray-100)
Position: fixed left-0, below topbar

Sections:
  1. Domain Navigator
     - Collapsible accordion per domain
     - Domain icon + name + completion %
     - Module list under each domain
     - Active item: left border 3px solid domain-color + bg tint

  2. Progress Summary
     - Mini progress bar
     - "N of M lessons complete"

  3. Quick Actions
     - Continue Learning (last visited)
     - Bookmarks
     - Practice Mode

Sidebar Item States:
  - locked: gray, lock icon
  - available: normal
  - in-progress: blue left border
  - completed: green checkmark
  - current: filled background tint
```

### 1.4.3 LESSON PAGE LAYOUT

```
Every lesson page MUST contain these sections in order:

┌─ LESSON HEADER ──────────────────────────────────────┐
│  Breadcrumb → Domain → Module → Topic → Lesson       │
│  Lesson Title (H1, Space Grotesk, 700)               │
│  Difficulty badge · Est. time · Prerequisites chips  │
│  Progress: [■■■■□□□□] 4 of 8 lessons                │
└──────────────────────────────────────────────────────┘

┌─ LEARNING OBJECTIVES ────────────────────────────────┐
│  "After this lesson you will be able to:"            │
│  ✓ Objective 1                                       │
│  ✓ Objective 2                                       │
│  ✓ Objective 3                                       │
└──────────────────────────────────────────────────────┘

┌─ CONCEPT EXPLANATION ────────────────────────────────┐
│  Clear prose, Inter 16px, line-height 1.75           │
│  Inline code snippets, highlighted keywords          │
│  Callout boxes (Info / Warning / Tip / Example)      │
└──────────────────────────────────────────────────────┘

┌─ ANIMATED ILLUSTRATION ──────────────────────────────┐
│  SVG-based teaching animation                        │
│  Play / Pause / Step-back / Step-forward controls    │
│  Speed control: 0.5x / 1x / 2x                      │
│  Caption below animation                             │
└──────────────────────────────────────────────────────┘

┌─ DIAGRAM AREA ───────────────────────────────────────┐
│  SVG diagram (responsive)                            │
│  Click to zoom / Download as PNG                     │
└──────────────────────────────────────────────────────┘

┌─ INTERACTIVE PLAYGROUND ─────────────────────────────┐
│  Domain-specific interactive component               │
│  (SQL Editor / Python REPL / Visual Builder / etc.)  │
│  Reset / Run / Solution buttons                      │
└──────────────────────────────────────────────────────┘

┌─ PRACTICE EXERCISES ─────────────────────────────────┐
│  2–4 graded exercises with hints                     │
│  Auto-graded with immediate feedback                 │
└──────────────────────────────────────────────────────┘

┌─ KNOWLEDGE CHECK ────────────────────────────────────┐
│  3–5 MCQ questions                                   │
│  Must pass 80% to unlock next lesson                 │
└──────────────────────────────────────────────────────┘

┌─ NAVIGATION ─────────────────────────────────────────┐
│  ← Previous Lesson          Next Lesson →            │
│  Related Topics (3 cards)                            │
└──────────────────────────────────────────────────────┘
```

### 1.4.4 CARD COMPONENTS

```
Lesson Card:
  - 280px min-width
  - White bg, 12px radius, shadow-sm
  - Top color bar (4px, domain color)
  - Domain icon + module label
  - Lesson title (H4, 700)
  - Description (2 lines, clamp)
  - Footer: difficulty pill + time estimate + completion status
  - Hover: translateY(-3px) + shadow-md transition 220ms

Domain Card (Homepage):
  - Full-width on mobile, 1/3 on desktop
  - Gradient background (domain color 5%→10%)
  - Large domain icon (48px SVG)
  - Domain name (H3)
  - Lesson count + completion %
  - Progress bar
  - CTA button

Progress Card:
  - Circular progress ring (SVG)
  - Stat: N% complete
  - Subtext: "N of M lessons"
  - Streak display
```

### 1.4.5 CALLOUT BOXES

```
Info Box:    bg #eff6ff, border-left 4px #4f8ef7, icon ℹ️
Warning Box: bg #fffbeb, border-left 4px #f59e0b, icon ⚠️
Tip Box:     bg #f0fdf4, border-left 4px #22c55e, icon 💡
Example Box: bg #faf5ff, border-left 4px #8b5cf6, icon 📌
Danger Box:  bg #fef2f2, border-left 4px #ef4444, icon 🚫
```

### 1.4.6 CODE BLOCK COMPONENT

```
Background: #0f172a (dark theme only for code blocks)
Font: JetBrains Mono, 14px
Line numbers: yes, color #475569
Syntax highlighting: Prism.js or highlight.js
Copy button: top-right, "Copy" → "Copied!" flash
Language badge: top-left chip
Line highlighting: specific lines highlighted in yellow
Max height: 400px with internal scroll
Run button (where applicable): triggers playground execution
```

### 1.4.7 PROGRESS & GAMIFICATION COMPONENTS

```
Streak Badge:
  - Fire icon + day count
  - Color: amber gradient
  - Tooltip: "N day streak! Keep it up."

XP Bar:
  - Horizontal progress bar
  - Level label: "Level 5 — Data Practitioner"
  - XP earned per lesson: +50 base, +bonus for quiz

Achievement Badges (16 total):
  1. First Lesson        9. Spark Master
  2. SQL Apprentice      10. Delta Explorer
  3. SQL Master          11. Azure Certified Path
  4. Python Coder        12. Databricks Pro
  5. Python Expert       13. Unity Catalog Expert
  6. Cloud Beginner      14. Streaming Specialist
  7. Azure Practitioner  15. Production Engineer
  8. Data Modeler        16. Complete Path

Certificate Component:
  - Issued per domain completion
  - Downloadable PDF
  - Shareable link + LinkedIn badge
```

---

## 1.5 FIREBASE BACKEND ARCHITECTURE

```
Firebase Project: learn-with-me-platform

Authentication:
  - Google OAuth (primary)
  - Email/Password (secondary)
  - Anonymous (preview mode)

Firestore Collections:
  /users/{uid}
    - displayName, email, photoURL
    - createdAt, lastActive
    - currentLevel, totalXP, streak
    - streakLastDate

  /users/{uid}/progress/{lessonId}
    - status: "not_started" | "in_progress" | "completed"
    - score: number (quiz score %)
    - completedAt: timestamp
    - timeSpentSeconds: number
    - attempts: number

  /users/{uid}/bookmarks/{lessonId}
    - addedAt: timestamp

  /users/{uid}/achievements/{achievementId}
    - earnedAt: timestamp

  /lessons/{lessonId}
    - title, domain, module, topic
    - order, prerequisites[]
    - estimatedMinutes
    - difficulty: 1-5
    - xpReward

  /domains/{domainId}
    - name, icon, color, order
    - totalLessons

Security Rules:
  - Users can only read/write their own /users/{uid}/** documents
  - /lessons/** is publicly readable
  - /domains/** is publicly readable
  - No user can write to /lessons or /domains (admin SDK only)

Firebase Storage:
  /avatars/{uid}/profile.jpg
  /certificates/{uid}/{domainId}.pdf

Realtime features via Firestore onSnapshot:
  - Live streak updates
  - Live progress sync across tabs
  - Live XP updates
```

---

## 1.6 GITHUB INTEGRATION

```
Repository: kavinparithi-works/learn-with-me
PAT: stored in environment variable GITHUB_PAT (never commit to repo)
Deployment: GitHub Pages from /main branch root

File Structure:
  /
  ├── index.html              ← Homepage / dashboard
  ├── lesson.html             ← Single lesson page template
  ├── css/
  │   ├── styles.css          ← Master stylesheet
  │   ├── animations.css      ← All CSS animations
  │   └── components.css      ← Reusable components
  ├── js/
  │   ├── firebase.js         ← Firebase init + auth
  │   ├── progress.js         ← Progress tracking
  │   ├── animations/         ← JS animation controllers
  │   │   ├── sql-animations.js
  │   │   ├── python-animations.js
  │   │   ├── spark-animations.js
  │   │   └── delta-animations.js
  │   └── interactive/        ← Interactive component controllers
  │       ├── sql-playground.js
  │       ├── join-simulator.js
  │       └── dag-builder.js
  ├── domains/
  │   ├── sql/
  │   │   ├── index.html
  │   │   └── lessons/
  │   │       ├── select-basics.html
  │   │       ├── where-clause.html
  │   │       └── ... (all lesson files)
  │   ├── python/
  │   ├── spark/
  │   ├── delta/
  │   ├── azure/
  │   ├── databricks/
  │   └── ...
  └── assets/
      ├── icons/              ← SVG domain icons
      ├── diagrams/           ← SVG diagrams per lesson
      └── fonts/              ← Self-hosted font fallbacks

CI/CD: GitHub Actions auto-deploy on push to main
```

---


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
- ALU: Escaped double-quote: doubled inside quoted field ("He said \"\"hello\"\"")
- ALU: Backslash escape: non-standard; MySQL CSV uses backslash
- ALU: Line endings: CRLF on Windows, LF on Unix; cross-platform issues common
- ALU: Trailing newline: RFC 4180 recommends it; many tools produce it; some don't

**Subtopic: CSV Pitfalls**
- ALU: Encoding: UTF-8 without BOM is safest; Windows tools add BOM → parse errors
- ALU: Type inference: everything is string; each consumer infers types independently
- ALU: Null representation: empty field, \N, NULL, none, NA — no standard
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
- ALU: escape="\": escape character
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
- ALU: ESCAPE character: LIKE '50\%' ESCAPE '\' matches literal '50%'
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

