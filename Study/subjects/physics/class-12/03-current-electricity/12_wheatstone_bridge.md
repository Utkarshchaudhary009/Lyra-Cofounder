# Chapter 12: Wheatstone Bridge

> *NCERT Section 3.14*

---

## 🎯 Stage 1: The Core Idea

### The Diamond of Resistors

Imagine four resistors arranged in a diamond (or a square) shape. A battery connects to two opposite corners. A Galvanometer (a sensitive current detector) connects to the other two opposite corners.

This specific arrangement of four resistors ($P, Q, R, S$) is called a **Wheatstone Bridge**.

**The Magic Trick: "Balancing" the Bridge**
When current enters the diamond, it splits into two paths: the upper path and the lower path. 
Normally, some current will flow through the middle wire containing the galvanometer because the two paths have different voltage drops.

But, if you perfectly adjust the four resistors such that the voltage drops are proportional, the two middle corners will reach the **exact same electrical potential**.
Since water only flows downhill, and these two points are at the exact same "height," **no current flows through the middle wire.**

This state is called a **Balanced Wheatstone Bridge**. It is the most accurate way to measure an unknown resistance because it relies on a "null deflection" (reading exactly zero), which means the internal resistance of the battery or galvanometer won't affect the final result.

---

## 🔬 Stage 2: The Formula Lab

### The Balancing Condition

For a Wheatstone bridge with arms $P, Q, R, S$, and a galvanometer in the middle:

If the bridge is balanced ($I_g = 0$):
$$\frac{P}{Q} = \frac{R}{S}$$
*(or equivalently, $\frac{P}{R} = \frac{Q}{S}$)*

**What this means:** The ratio of the resistances in the upper arms equals the ratio of the resistances in the lower arms.

### The Beauty of a Balanced Bridge
If $\frac{P}{Q} = \frac{R}{S}$, then:
1. Current through the galvanometer is zero ($I_g = 0$).
2. The central resistor/galvanometer can be **completely removed** from the circuit for calculations.
3. The circuit simplifies drastically into $(P \text{ series } Q)$ parallel with $(R \text{ series } S)$.
   $R_{eq} = \frac{(P+Q)(R+S)}{(P+Q) + (R+S)}$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Checking for Balance and Finding Equivalent Resistance ⭐

**Pattern:** "Given a 5-resistor network, check if it's balanced and find $R_{eq}$."

**Solved Example** 🟢

> Five resistors are connected as a Wheatstone bridge. $P = 10\text{ } \Omega, Q = 20\text{ } \Omega, R = 30\text{ } \Omega, S = 60\text{ } \Omega$. A $50\text{ } \Omega$ galvanometer is in the middle. Find the equivalent resistance.

<details>
<summary><b>Solution</b></summary>

**Step 1: Check balance condition.**
Left ratio: $P/R = 10/30 = 1/3$.
Right ratio: $Q/S = 20/60 = 1/3$.
Since $1/3 = 1/3$, the **bridge is balanced**.

**Step 2: Remove the middle.**
The $50\text{ } \Omega$ resistor in the middle carries no current. Delete it.

**Step 3: Calculate $R_{eq}$.**
Top branch: $P + Q = 10 + 20 = 30\text{ } \Omega$.
Bottom branch: $R + S = 30 + 60 = 90\text{ } \Omega$.
These two branches are in parallel.
$R_{eq} = \frac{30 \times 90}{30 + 90} = \frac{2700}{120} = \mathbf{22.5\text{ } \Omega}$.
</details>

**Practice:**

1. 🟢 $P=2\text{ } \Omega, Q=4\text{ } \Omega, R=3\text{ } \Omega, S=6\text{ } \Omega$. The central resistor is $10\text{ } \Omega$. Is the bridge balanced? Find $R_{eq}$.

<details>
<summary><b>Answer</b></summary>

$P/Q = 2/4 = 1/2$. $R/S = 3/6 = 1/2$. Balanced!
Delete middle. Top branch = $2+4=6\text{ } \Omega$. Bottom branch = $3+6=9\text{ } \Omega$.
$R_{eq} = (6 \times 9) / (6 + 9) = 54 / 15 = \mathbf{3.6\text{ } \Omega}$.
</details>

2. 🟡 Four identical resistors $R$ form the arms of a Wheatstone bridge. A fifth resistor $R$ is connected between the middle points. Find the equivalent resistance.

<details>
<summary><b>Answer</b></summary>

$R/R = R/R \implies 1 = 1$. It is balanced.
Delete the middle $R$.
Top branch = $R+R=2R$. Bottom branch = $R+R=2R$.
$R_{eq} = (2R \times 2R) / (2R + 2R) = 4R^2 / 4R = \mathbf{R}$.
</details>

---

### Type 2: Finding an Unknown Resistance ⭐⭐

**Pattern:** "The bridge is balanced. Find the value of one missing resistor."

**Solved Example** 🟡

> In a Wheatstone bridge, $P = 15\text{ } \Omega$, $Q = 10\text{ } \Omega$, $R = 3\text{ } \Omega$. What should be the value of $S$ so that the galvanometer shows zero deflection?

<details>
<summary><b>Solution</b></summary>

Zero deflection means the bridge is balanced.
$\frac{P}{Q} = \frac{R}{S}$
$\frac{15}{10} = \frac{3}{S}$
$1.5 = \frac{3}{S} \implies S = \frac{3}{1.5} = \mathbf{2\text{ } \Omega}$.
</details>

**Practice:**

1. 🟢 $P=100\text{ } \Omega, Q=10\text{ } \Omega, R=X, S=5\text{ } \Omega$. The bridge is balanced. Find $X$.

<details>
<summary><b>Answer</b></summary>

$100 / 10 = X / 5$
$10 = X / 5 \implies X = \mathbf{50\text{ } \Omega}$.
</details>

2. 🟡 To balance a Wheatstone bridge, a resistance of $12\text{ } \Omega$ is needed in the S arm. However, the student only has an $18\text{ } \Omega$ resistor. What resistance should he connect in parallel with the $18\text{ } \Omega$ resistor to achieve balance?

<details>
<summary><b>Answer</b></summary>

We need $S_{eq} = 12\text{ } \Omega$.
Let the required parallel resistor be $R_x$.
$\frac{1}{12} = \frac{1}{18} + \frac{1}{R_x}$
$\frac{1}{R_x} = \frac{1}{12} - \frac{1}{18} = \frac{3 - 2}{36} = \frac{1}{36}$
$R_x = \mathbf{36\text{ } \Omega}$.
</details>

---

### Type 3: Hidden Wheatstone Bridges ⭐⭐⭐

**Pattern:** "A circuit doesn't look like a diamond, but it actually is a Wheatstone bridge."

> 🔑 **THE MASTER TRICK:**
> Watch out for these common "Hidden" shapes:
> 1. **The 'A' Frame:** Looks like the letter A with a resistor crossing the middle.
> 2. **The Folded Square:** A square with diagonals. Pull the corners apart and it becomes a diamond!
> 3. **The Circle:** Five resistors forming a circle with a cross.
> 
> *Rule of thumb: If you see exactly 5 resistors and two input/output nodes, it is almost certainly a Wheatstone bridge.*

**Solved Example** 🔴

> A circuit has three resistors $R_1, R_2, R_3$ in series. A wire connects the start of $R_1$ to the end of $R_2$ with a resistor $R_4$. Another wire connects the end of $R_1$ to the end of $R_3$ with a resistor $R_5$. Is this a Wheatstone bridge?

<details>
<summary><b>Solution</b></summary>

Yes! Draw the nodes.
Let Input be A (start of $R_1$). Let Output be B (end of $R_3$).
Let node C be between $R_1$ and $R_2$. Let node D be between $R_2$ and $R_3$.
$R_1$ is between A and C.
$R_2$ is between C and D. (This is the galvanometer arm!)
$R_3$ is between D and B.
$R_4$ is between A and D.
$R_5$ is between C and B.
If you redraw it, $R_2$ sits perfectly in the middle of the bridge formed by $R_1, R_4, R_5, R_3$.
If $R_1/R_4 = R_5/R_3$, then $R_2$ carries no current!
</details>

**Practice:**

1. 🟡 Five resistors of $10\text{ } \Omega$ each are arranged to form a pentagon. A battery is connected across two adjacent corners. Is it a Wheatstone bridge?

<details>
<summary><b>Answer</b></summary>

**No.** A Wheatstone bridge requires two nodes for input/output and two nodes for the middle bridge. A pentagon across adjacent corners doesn't fit the topological structure of a bridge. It's just a series-parallel circuit.
</details>

2. 🔴 Six resistors form the edges of a tetrahedron. You measure resistance across any one edge. Can you use Wheatstone bridge symmetry here?

<details>
<summary><b>Answer</b></summary>

**Yes!** If you measure across edge AB, the other two nodes C and D form the "middle" arm of the bridge. The edge CD will act as the galvanometer arm. Due to symmetry, the bridge is balanced, and no current flows through CD. You can remove edge CD and solve it easily.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 In a Wheatstone bridge, $P = 10\text{ } \Omega, Q = 20\text{ } \Omega, R = 15\text{ } \Omega, S = 30\text{ } \Omega$. A $10\text{V}$ battery is connected. What is the current drawn from the battery? What is the current through the $P$ resistor?

<details>
<summary><b>Solution</b></summary>

$P/R = 10/15 = 2/3$. $Q/S = 20/30 = 2/3$. Bridge is balanced.
Top branch = $P+Q = 30\text{ } \Omega$. Bottom branch = $R+S = 45\text{ } \Omega$.
$R_{eq} = (30 \times 45) / (30 + 45) = 1350 / 75 = \mathbf{18\text{ } \Omega}$.
Total current $I = V / R_{eq} = 10 / 18 = \mathbf{0.55\text{ A}}$.

The voltage across the top branch is $10\text{V}$.
Current through $P$ = Current through top branch = $V / (P+Q) = 10 / 30 = \mathbf{0.33\text{ A}}$.
</details>

**Q2.** 🔴 ⭐ An unbalanced Wheatstone bridge has $P = 10\text{ } \Omega, Q = 5\text{ } \Omega, R = 5\text{ } \Omega, S = 10\text{ } \Omega$, and $G = 10\text{ } \Omega$. Find $R_{eq}$.

<details>
<summary><b>Solution</b></summary>

$P/Q = 2$, but $R/S = 0.5$. **Unbalanced.** You cannot delete $G$.
You must use Kirchhoff's rules (or delta-star transform if you know it).
Using Nodal Analysis: Let bottom corner be $0\text{V}$, top corner be $V$. Let left node be $x$ and right node be $y$.
KCL at $x$: $\frac{x-V}{10} + \frac{x-0}{5} + \frac{x-y}{10} = 0 \implies (x-V) + 2x + (x-y) = 0 \implies 4x - y = V$.
KCL at $y$: $\frac{y-V}{5} + \frac{y-0}{10} + \frac{y-x}{10} = 0 \implies 2(y-V) + y + (y-x) = 0 \implies -x + 4y = 2V$.
Solve for $x$ and $y$: Multiply first eq by 4: $16x - 4y = 4V$. Add to second: $15x = 6V \implies x = 0.4V$.
$y = 4x - V = 1.6V - V = 0.6V$.
Total current leaving top node $I = \frac{V-x}{10} + \frac{V-y}{5} = \frac{V-0.4V}{10} + \frac{V-0.6V}{5} = \frac{0.6V}{10} + \frac{0.4V}{5} = 0.06V + 0.08V = 0.14V$.
$R_{eq} = V / I = 1 / 0.14 = 100 / 14 = \mathbf{50/7 \text{ } \Omega \approx 7.14\text{ } \Omega}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 What is the principle of a Wheatstone bridge? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

A Wheatstone bridge is an arrangement of four resistances ($P, Q, R, S$) used to determine an unknown resistance. Its principle is based on the **null deflection method**. When the bridge is balanced ($P/Q = R/S$), the potential difference between the opposite junctions is zero, and no current flows through the galvanometer connected between them.
</details>

**Q2.** 🟡 Why is the Wheatstone bridge method considered more accurate than measuring voltage and current separately to find resistance? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. It is a **null method** (galvanometer reading is zero at balance). Therefore, the internal resistance of the galvanometer and the battery do not affect the result.
2. It relies only on the ratios of known resistances, eliminating errors caused by measuring instruments like voltmeters and ammeters which can draw some current and skew readings.
</details>

**Q3.** 🟡 In a Wheatstone bridge, what happens to the balance point if the positions of the battery and the galvanometer are interchanged? *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

The balance point **remains unchanged**. The bridge remains balanced ($P/R = Q/S$ is mathematically equivalent to $P/Q = R/S$).
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ In a Wheatstone bridge, all four arms have equal resistance $R$. If the resistance of the galvanometer arm is also $R$, the equivalent resistance of the combination as seen by the battery is:

(a) $R/2$ &emsp; (b) $R$ &emsp; (c) $2R$ &emsp; (d) $R/4$

<details>
<summary><b>Answer</b></summary>

Since all arms are $R$, $R/R = R/R$. The bridge is perfectly balanced.
The galvanometer resistance does not matter because no current flows through it.
Remove the galvanometer. Top branch = $R+R=2R$. Bottom branch = $R+R=2R$.
Parallel combination: $(2R)/2 = \mathbf{R}$.

**Answer: (b)**
</details>

**Q2.** 🔴 The four arms of a Wheatstone bridge have resistances $10\text{ } \Omega, 10\text{ } \Omega, 10\text{ } \Omega$ and $20\text{ } \Omega$. A galvanometer of $15\text{ } \Omega$ resistance is connected across the diagonal. Is the bridge balanced? If not, what will be the qualitative direction of current through the galvanometer?

<details>
<summary><b>Answer</b></summary>

Let $P=10, Q=10, R=10, S=20$.
$P/Q = 10/10 = 1$. $R/S = 10/20 = 0.5$.
$1 \neq 0.5$, so the bridge is **unbalanced**.
Let the battery be connected to left ($0\text{V}$) and right ($V$) nodes.
Top node $x$ is formed by $P$ and $Q$. $V_x = V(Q/(P+Q)) = V(10/20) = 0.5V$. (Assuming galvanometer draws negligible current initially to find potential difference).
Bottom node $y$ is formed by $R$ and $S$. $V_y = V(S/(R+S)) = V(20/30) = 0.67V$.
Since $V_y > V_x$, current flows from **y to x (bottom to top)** through the galvanometer.

**Answer: Unbalanced; Current flows from the junction of R,S to the junction of P,Q.**
</details>

**Q3.** 🔴 ⭐ Which of the following is true about the sensitivity of a Wheatstone bridge?

(a) It is highest when all four resistances are roughly equal.
(b) It is highest when the galvanometer resistance is zero.
(c) It is independent of the battery EMF.
(d) It increases if we use very high resistances for $P$ and $Q$.

<details>
<summary><b>Answer</b></summary>

A Wheatstone bridge is most sensitive (gives the largest galvanometer deflection for a small unbalance) when the resistances in all four arms are **of the same order of magnitude** ($P \approx Q \approx R \approx S$). If the ratio is extreme (e.g., $1000 : 1$), a small change in the unknown resistor will barely move the galvanometer needle, making precise measurement difficult.

**Answer: (a)**
</details>

---

*Next: [Chapter 13 — Meter Bridge →](./13_meter_bridge.md)*
