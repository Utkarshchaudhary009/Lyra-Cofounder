# Chapter 8: Combination of Resistors — Series & Parallel

> *NCERT Chapter 3 (Foundational Concept)*

---

## 🎯 Stage 1: The Core Idea

### The Highway Tollbooth Analogy

Imagine resistors as tollbooths on a highway that slow down traffic (current).

**1. Series Combination (End-to-End):**
If you place three tollbooths back-to-back on a single lane, every single car *must* pass through all three. 
- **Current ($I$) is exactly the same** through all resistors.
- The total "delay" (Voltage drop, $V$) is the sum of the individual delays: $V = V_1 + V_2 + V_3$.
- The total resistance increases. It's harder to get through three tollbooths than one.

**2. Parallel Combination (Side-by-Side):**
If you place three tollbooths side-by-side across three parallel lanes, the cars split up.
- **Voltage drop ($V$) is exactly the same** across all resistors (all lanes start and end at the same points).
- The total traffic (Current, $I$) splits: $I = I_1 + I_2 + I_3$.
- The total resistance decreases. It's much easier for traffic to flow when there are multiple alternative paths, even if some of those alternative paths are quite restrictive!

---

## 🔬 Stage 2: The Formula Lab

### 1. Resistors in Series

$$R_{eq} = R_1 + R_2 + R_3 + \dots + R_n$$

- **Key Rule:** $I$ is constant. $V$ splits.
- **Result:** $R_{eq}$ is always **greater** than the largest individual resistance in the combination.
- **Shortcut for $n$ identical resistors:** $R_{eq} = nR$.

#### Voltage Divider Rule (For Series)
Since $V \propto R$ (because $I$ is constant), the voltage splits in the *direct ratio* of the resistances.
For two resistors $R_1$ and $R_2$ in series across voltage $V$:
$$V_1 = V \left( \frac{R_1}{R_1 + R_2} \right)$$
$$V_2 = V \left( \frac{R_2}{R_1 + R_2} \right)$$

### 2. Resistors in Parallel

$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots + \frac{1}{R_n}$$

- **Key Rule:** $V$ is constant. $I$ splits.
- **Result:** $R_{eq}$ is always **smaller** than the smallest individual resistance in the combination.
- **Shortcut for 2 resistors:** $R_{eq} = \frac{R_1 R_2}{R_1 + R_2}$ (Product over Sum).
- **Shortcut for $n$ identical resistors:** $R_{eq} = \frac{R}{n}$.

#### Current Divider Rule (For Parallel) ⭐
Since $I \propto 1/R$ (because $V$ is constant), the current splits in the *inverse ratio* of the resistances.
For two resistors $R_1$ and $R_2$ in parallel carrying total current $I$:
$$I_1 = I \left( \frac{R_2}{R_1 + R_2} \right) \quad \text{(Notice it's } R_2 \text{ on top!)}$$
$$I_2 = I \left( \frac{R_1}{R_1 + R_2} \right)$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic Series & Parallel Reduction ⭐

**Pattern:** "Given a simple network, find the equivalent resistance between two points."

**Solved Example** 🟢

> Three resistors of $2\text{ } \Omega$, $3\text{ } \Omega$, and $6\text{ } \Omega$ are connected in parallel. Find the equivalent resistance.

<details>
<summary><b>Solution</b></summary>

$\frac{1}{R_{eq}} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6}$
$\frac{1}{R_{eq}} = \frac{3 + 2 + 1}{6} = \frac{6}{6} = 1$
$R_{eq} = \mathbf{1\text{ } \Omega}$
*(Notice the answer is smaller than the smallest resistor, $2\text{ } \Omega$!)*
</details>

**Practice:**

1. 🟢 Two resistors of $10\text{ } \Omega$ and $15\text{ } \Omega$ are in parallel. Find $R_{eq}$.

<details>
<summary><b>Answer</b></summary>

Use product over sum: $R_{eq} = (10 \times 15) / (10 + 15) = 150 / 25 = \mathbf{6\text{ } \Omega}$.
</details>

2. 🟢 Four identical resistors, each of $8\text{ } \Omega$, are connected in parallel. Find $R_{eq}$.

<details>
<summary><b>Answer</b></summary>

Shortcut for identical resistors: $R_{eq} = R/n = 8/4 = \mathbf{2\text{ } \Omega}$.
</details>

3. 🟡 A $4\text{ } \Omega$ resistor is connected in series with a parallel combination of a $6\text{ } \Omega$ and a $3\text{ } \Omega$ resistor. Find total resistance.

<details>
<summary><b>Answer</b></summary>

First, solve parallel part: $R_p = (6 \times 3) / (6 + 3) = 18/9 = 2\text{ } \Omega$.
Now add the series part: $R_{total} = 4 + 2 = \mathbf{6\text{ } \Omega}$.
</details>

4. 🟡 How can you connect three resistors of $3\text{ } \Omega$ each to get an equivalent resistance of $2\text{ } \Omega$?<br>

<details>
<summary><b>Answer</b></summary>

We need $R_{eq} < 3\text{ } \Omega$, but not as low as $3/3 = 1\text{ } \Omega$. This implies a mixed grouping.
Try two in parallel, one in series: $(3 \parallel 3) + 3 = 1.5 + 3 = 4.5\text{ } \Omega$ (Incorrect).
Try two in series, one in parallel: $(3 + 3) \parallel 3 = 6 \parallel 3 = (6 \times 3)/(6 + 3) = 18/9 = \mathbf{2\text{ } \Omega}$.
So, **connect two in series, and connect that combination in parallel with the third**.
</details>

5. 🔴 Five identical resistors yield an equivalent resistance of $R_1$ when connected in series and $R_2$ when connected in parallel. Find $R_1/R_2$.

<details>
<summary><b>Answer</b></summary>

Let each resistor be $R$.
Series: $R_1 = 5R$.
Parallel: $R_2 = R/5$.
Ratio $R_1 / R_2 = (5R) / (R/5) = 5 \times 5 = \mathbf{25}$.
*(General rule: $R_{series} / R_{parallel} = n^2$)*
</details>

---

### Type 2: Voltage and Current Dividers ⭐⭐

**Pattern:** "Find the voltage across or current through a specific resistor in a network."

**Solved Example** 🟡

> A voltage of $24\text{V}$ is applied across a series combination of a $2\text{ } \Omega$ and a $6\text{ } \Omega$ resistor. Find the voltage across the $6\text{ } \Omega$ resistor.

<details>
<summary><b>Solution</b></summary>

Using Voltage Divider Rule:
$V_2 = V_{total} \left( \frac{R_2}{R_1 + R_2} \right)$
$V_6 = 24 \left( \frac{6}{2 + 6} \right) = 24 \left( \frac{6}{8} \right) = 24 \times \frac{3}{4} = \mathbf{18\text{ V}}$.

*(Alternative: Total $R = 8\text{ } \Omega$. Total $I = 24/8 = 3\text{ A}$. $V_6 = I \times R_6 = 3 \times 6 = 18\text{ V}$. Both methods work perfectly!)*
</details>

**Practice:**

1. 🟢 A $10\text{ } \Omega$ and a $40\text{ } \Omega$ resistor are in series across $100\text{V}$. Find voltage across the $10\text{ } \Omega$ resistor.

<details>
<summary><b>Answer</b></summary>

$V_{10} = 100 \times \left( \frac{10}{10 + 40} \right) = 100 \times \left( \frac{10}{50} \right) = 100 \times \frac{1}{5} = \mathbf{20\text{ V}}$.
</details>

2. 🟡 A current of $5\text{ A}$ enters a parallel combination of a $3\text{ } \Omega$ and a $2\text{ } \Omega$ resistor. Find the current through the $3\text{ } \Omega$ resistor.

<details>
<summary><b>Answer</b></summary>

Using Current Divider Rule:
$I_3 = I_{total} \times \left( \frac{R_{other}}{R_1 + R_2} \right) = 5 \times \left( \frac{2}{3 + 2} \right) = 5 \times \frac{2}{5} = \mathbf{2\text{ A}}$.
*(Notice: The bigger resistor gets the smaller current!)*
</details>

3. 🟡 In a parallel circuit with $10\text{ } \Omega$, $20\text{ } \Omega$, and $30\text{ } \Omega$ resistors, the total current is $11\text{ A}$. Find the current through the $20\text{ } \Omega$ resistor.

<details>
<summary><b>Answer</b></summary>

When there are more than 2 resistors, the shortcut is to find the total voltage first.
$1/R_{eq} = 1/10 + 1/20 + 1/30 = (6+3+2)/60 = 11/60 \implies R_{eq} = 60/11\text{ } \Omega$.
Total Voltage $V = I \times R_{eq} = 11 \times (60/11) = 60\text{ V}$.
Current through $20\text{ } \Omega$ resistor = $V / R_{20} = 60 / 20 = \mathbf{3\text{ A}}$.
</details>

4. 🔴 A current of $10\text{ A}$ splits between two parallel branches of $4\text{ } \Omega$ and $R\text{ } \Omega$. If $8\text{ A}$ flows through the $4\text{ } \Omega$ branch, find the value of $R$.

<details>
<summary><b>Answer</b></summary>

Current through $R$ branch = $10\text{ A} - 8\text{ A} = 2\text{ A}$.
Since they are in parallel, voltage across them is equal.
$V_4 = V_R$
$I_4 \times 4 = I_R \times R$
$8 \times 4 = 2 \times R \implies 32 = 2R \implies R = \mathbf{16\text{ } \Omega}$.
</details>

---

### Type 3: Identifying Equipotential Points (Symmetry & Wires) ⭐⭐⭐

**Pattern:** "A circuit looks impossibly complex, or has 'empty' wires connecting nodes."

> 🔑 **THE MASTER TRICK:**
> Any two points connected by a plain wire (0 resistance) are at the **exact same potential**. You can "merge" them into a single point. 
> If a resistor connects between two points of the *same* potential, **no current flows through it**, and you can delete it from the circuit!

**Solved Example** 🔴

> Three resistors $R_1, R_2, R_3$ are connected in series between points A and B. However, a plain wire connects the start of $R_1$ to the end of $R_2$. Another plain wire connects the end of $R_1$ to the end of $R_3$. What is the equivalent resistance?<br>

<details>
<summary><b>Solution</b></summary>

Let's label the nodes. 
Node A is the start of $R_1$. The wire connects Node A to the end of $R_2$. So both ends are Node A.
The end of $R_1$ is a new node, let's call it B. The wire connects Node B to the end of $R_3$ (which is the output terminal). 
Wait, let's draw this carefully in our minds:
$R_1$ connects A to B.
$R_2$ connects B to A (since the end of $R_2$ is connected to A).
$R_3$ connects A to B (since start of $R_3$ is the end of $R_2$ which is A, and end of $R_3$ is B).
So, $R_1, R_2,$ and $R_3$ are all connected directly between Node A and Node B!
They are in **pure parallel**.
$1/R_{eq} = 1/R_1 + 1/R_2 + 1/R_3$.
*(This is a classic "looks like series but is actually parallel" trap).*
</details>

**Practice:**

1. 🟡 A $10\text{ } \Omega$ resistor is connected between A and B. A plain copper wire is also connected directly between A and B. What is the equivalent resistance?<br>

<details>
<summary><b>Answer</b></summary>

The plain wire has $R=0$. The $10\text{ } \Omega$ resistor is in parallel with a $0\text{ } \Omega$ resistor.
$R_{eq} = (10 \times 0) / (10 + 0) = \mathbf{0\text{ } \Omega}$.
The current takes the path of least resistance. The resistor is "short-circuited".
</details>

2. 🔴 Consider a square ABCD with resistors of $R$ on each side. A diagonal resistor $R$ connects A and C. Another diagonal resistor $R$ connects B and D. Find resistance across A and C.

<details>
<summary><b>Answer</b></summary>

This is a balanced Wheatstone bridge! (We will cover this in detail in Chapter 12).
Path A-B-C has $R+R=2R$. Path A-D-C has $R+R=2R$.
Because of symmetry, points B and D are at the same potential.
The resistor between B and D carries **zero current** and can be removed.
Now we have three parallel paths between A and C:
Path 1 (via B) = $2R$
Path 2 (diagonal) = $R$
Path 3 (via D) = $2R$
$1/R_{eq} = 1/2R + 1/R + 1/2R = 2/2R + 1/R = 1/R + 1/R = 2/R$.
$R_{eq} = \mathbf{R/2}$.
</details>

---

### Type 4: Infinite Ladder Networks ⭐⭐⭐

**Pattern:** "A repeating pattern of resistors goes on to infinity."

> 🔑 **THE MASTER TRICK:**
> Since the ladder is infinite, removing one "repeating unit" from the front leaves you with exactly the same infinite ladder!
> 1. Let the total resistance be $X$.
> 2. Identify the repeating unit.
> 3. Replace the entire infinite part *after* the first unit with a single resistor $X$.
> 4. Solve the resulting quadratic equation for $X$.

**Solved Example** 🔴

> An infinite ladder is formed by a series resistor $1\text{ } \Omega$ and a parallel resistor $2\text{ } \Omega$, repeating forever. Find the equivalent resistance across the input terminals.

<details>
<summary><b>Solution</b></summary>

Let the total equivalent resistance be $X$.
The repeating unit is: Series $1\text{ } \Omega$, Parallel $2\text{ } \Omega$.
If we chop off the first unit, the rest of the infinite ladder still has a resistance of $X$.
So, the circuit is equivalent to: A $1\text{ } \Omega$ resistor in series with a parallel combination of $2\text{ } \Omega$ and $X$.
$X = 1 + \frac{2 \times X}{2 + X}$
Multiply by $(2+X)$:
$X(2+X) = 1(2+X) + 2X$
$2X + X^2 = 2 + X + 2X$
$X^2 - X - 2 = 0$
$(X - 2)(X + 1) = 0$
Since resistance cannot be negative, $X = \mathbf{2\text{ } \Omega}$.
</details>

**Practice:**

1. 🔴 An infinite ladder consists of repeating units of series $R$ and parallel $R$. Find equivalent resistance.

<details>
<summary><b>Answer</b></summary>

Let equivalent resistance be $X$.
$X = R + \frac{R \cdot X}{R + X}$
$X(R+X) = R(R+X) + RX$
$RX + X^2 = R^2 + RX + RX$
$X^2 - RX - R^2 = 0$
Solve using quadratic formula: $X = \frac{R \pm \sqrt{R^2 - 4(1)(-R^2)}}{2} = \frac{R \pm \sqrt{5R^2}}{2} = \mathbf{\frac{R(\sqrt{5} + 1)}{2}}$.
*(The Golden Ratio appears!)*
</details>

2. 🔴 An infinite sequence of parallel branches is connected to a source. Branch 1 has resistance $R$, Branch 2 has $2R$, Branch 3 has $4R$, and so on ($2^{n-1}R$). Find total equivalent resistance.

<details>
<summary><b>Answer</b></summary>

This is an infinite geometric progression in parallel.
$1/R_{eq} = 1/R + 1/2R + 1/4R + \dots$
$1/R_{eq} = (1/R) [1 + 1/2 + 1/4 + \dots]$
The term in brackets is an infinite geometric series with $a=1, r=1/2$. Sum $S = a / (1-r) = 1 / (1 - 1/2) = 2$.
$1/R_{eq} = (1/R) \times 2 = 2/R$.
$R_{eq} = \mathbf{R/2}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A wire of resistance $12\text{ } \Omega$ per meter is bent to form a complete circle of radius $10\text{ cm}$. The resistance between two diametrically opposite points A and B is:

<details>
<summary><b>Solution</b></summary>

Circumference of circle = $2\pi r = 2\pi(0.1) = 0.2\pi$ meters.
Total resistance of the wire = $12 \times 0.2\pi = 2.4\pi\text{ } \Omega$.
When calculating across a diameter, the circle splits into two equal semi-circles in parallel.
Resistance of each semi-circle = $2.4\pi / 2 = 1.2\pi\text{ } \Omega$.
Equivalent resistance in parallel $R_{eq} = R/2 = 1.2\pi / 2 = \mathbf{0.6\pi\text{ } \Omega}$.
</details>

**Q2.** 🔴 ⭐ Twelve equal resistors of resistance $R$ are connected to form the edges of a cube. Find the equivalent resistance across: (a) Body diagonal, (b) Face diagonal, (c) Adjacent edge.
*(Memorizing these results is highly recommended for JEE!)*

<details>
<summary><b>Solution</b></summary>

Using symmetry and current distribution:
(a) **Body diagonal:** Current $I$ splits into $I/3$, then $I/6$, then reunites to $I/3$.
    $V = (I/3)R + (I/6)R + (I/3)R = I(5/6)R \implies R_{eq} = \mathbf{\frac{5}{6}R}$.
(b) **Face diagonal:** $R_{eq} = \mathbf{\frac{3}{4}R}$.
(c) **Adjacent edge:** $R_{eq} = \mathbf{\frac{7}{12}R}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Two resistors of $10\text{ } \Omega$ and $20\text{ } \Omega$ are connected in series. A voltage of $60\text{V}$ is applied. Find the current and the voltage across the $10\text{ } \Omega$ resistor. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Total resistance $R_{eq} = 10 + 20 = 30\text{ } \Omega$.
Current $I = V / R_{eq} = 60 / 30 = \mathbf{2\text{ A}}$.
Voltage across $10\text{ } \Omega$ resistor $V_{10} = I \times R_{10} = 2 \times 10 = \mathbf{20\text{ V}}$.
</details>

**Q2.** 🟡 Show that when three resistors $R_1, R_2, R_3$ are connected in parallel, the equivalent resistance $R_p$ is given by $1/R_p = 1/R_1 + 1/R_2 + 1/R_3$. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

In a parallel combination, the potential difference $V$ across each resistor is the same, but the total current $I$ splits among the branches.
By Kirchhoff's current law at the junction:
$I = I_1 + I_2 + I_3$
Using Ohm's law ($I = V/R$) for each resistor:
$I_1 = V/R_1$, $I_2 = V/R_2$, $I_3 = V/R_3$
Therefore, $I = V/R_1 + V/R_2 + V/R_3 = V(1/R_1 + 1/R_2 + 1/R_3)$  --- (Eq 1)
If $R_p$ is the equivalent resistance of the parallel combination, it must draw the same total current $I$ for the same voltage $V$:
$I = V/R_p$ --- (Eq 2)
Comparing Eq 1 and Eq 2:
$V/R_p = V(1/R_1 + 1/R_2 + 1/R_3)$
Dividing by $V$ on both sides:
**$1/R_p = 1/R_1 + 1/R_2 + 1/R_3$**
</details>

**Q3.** 🟡 A wire of uniform cross-section and resistance $4\text{ } \Omega$ is bent into a circle. What is the resistance between two diametrically opposite points?<br> *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

The wire is split into two semi-circles, each of resistance $2\text{ } \Omega$.
These two semi-circles are in parallel.
$R_{eq} = \frac{2 \times 2}{2 + 2} = \mathbf{1\text{ } \Omega}$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ Six equal resistors are connected between points P, Q, and R as shown in a triangle (two resistors on each side). The equivalent resistance between P and Q is:

(a) $R$ &emsp; (b) $R/2$ &emsp; (c) $2R/3$ &emsp; (d) $4R/3$

<details>
<summary><b>Answer</b></summary>

Assume each side has two resistors in series. Resistance of one side = $2R$.
The triangle has three sides. We want resistance across one side (P-Q).
The side PQ has resistance $2R$.
The path P-R-Q has resistance $2R + 2R = 4R$.
These two paths are in parallel.
$R_{eq} = \frac{(2R)(4R)}{2R + 4R} = \frac{8R^2}{6R} = \mathbf{\frac{4}{3}R}$.

**Answer: (d)**
</details>

**Q2.** 🔴 An infinite ladder network consists of $1\text{ } \Omega$ resistors in series and $1\text{ } \Omega$ resistors in parallel. The effective resistance between A and B is:

(a) $(\sqrt{5}-1)/2 \text{ } \Omega$ &emsp; (b) $(\sqrt{5}+1)/2 \text{ } \Omega$ &emsp; (c) $1\text{ } \Omega$ &emsp; (d) $2\text{ } \Omega$

<details>
<summary><b>Answer</b></summary>

This is exactly the Practice problem from Type 4.
$X^2 - RX - R^2 = 0$. Here $R=1$.
$X^2 - X - 1 = 0 \implies X = \frac{1 + \sqrt{1 - 4(-1)}}{2} = \mathbf{\frac{1 + \sqrt{5}}{2} \text{ } \Omega}$.

**Answer: (b)**
</details>

**Q3.** 🔴 ⭐ In the circuit shown, all resistors are $R$. A wire of zero resistance connects the nodes forming a shape that looks like a bridge but the galvanometer arm is replaced by a plain wire. What is the equivalent resistance?<br>

<details>
<summary><b>Answer</b></summary>

A generic "bridge with a short circuit" problem.
If the middle arm is a plain wire ($0\text{ } \Omega$), then the two nodes it connects are at the *same potential*.
This places the two upper resistors in parallel with each other, and the two lower resistors in parallel with each other.
Upper parallel pair: $R \parallel R = R/2$.
Lower parallel pair: $R \parallel R = R/2$.
These two pairs are in series.
$R_{eq} = R/2 + R/2 = \mathbf{R}$.
*(This happens frequently in symmetry-based folding tricks).*
</details>

---

*Next: [Chapter 9 — Cells, EMF & Internal Resistance →](./09_cells_emf_internal_resistance.md)*
