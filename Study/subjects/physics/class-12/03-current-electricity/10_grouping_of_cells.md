# Chapter 10: Cells in Series and Parallel (Grouping of Cells)

> *NCERT Section 3.11*

---

## 🎯 Stage 1: The Core Idea

### Why Group Cells?

A single $1.5\text{V}$ AA battery can't power a flashlight that requires $6\text{V}$. And a single small battery can't provide the massive current needed to start a car engine. 

To get the voltage and current we need, we combine cells.

**1. Series Grouping (Stacking them up):**
When you place batteries end-to-end (positive to negative), you are stacking their "pumps" on top of each other. The water (charge) gets pushed by the first, then pushed *again* by the second.
- **Goal:** To increase the total **Voltage (EMF)**.

**2. Parallel Grouping (Side-by-side):**
When you connect all the positive terminals together and all the negative terminals together, you aren't increasing the pressure. Instead, you are providing multiple pumps working side-by-side to handle a massive volume of water.
- **Goal:** To increase the total **Current capacity** (and reduce internal resistance).

---

## 🔬 Stage 2: The Formula Lab

### 1. Cells in Series

Suppose we have $n$ identical cells, each of EMF $\varepsilon$ and internal resistance $r$, connected in series.
- **Equivalent EMF:** $\varepsilon_{eq} = \varepsilon + \varepsilon + \dots = \mathbf{n\varepsilon}$
- **Equivalent Internal Resistance:** $r_{eq} = r + r + \dots = \mathbf{nr}$

Current through an external resistor $R$:
$$I = \frac{n\varepsilon}{R + nr}$$

> **What if one cell is reversed?** ⭐
> If 1 cell out of $n$ is connected backwards, it cancels out itself AND one normal cell.
> Equivalent EMF = $(n-2)\varepsilon$. (Internal resistance remains $nr$).

### 2. Cells in Parallel

Suppose we have $m$ identical cells, each of EMF $\varepsilon$ and internal resistance $r$, connected in parallel.
- **Equivalent EMF:** $\varepsilon_{eq} = \mathbf{\varepsilon}$ *(Voltage doesn't add up in parallel!)*
- **Equivalent Internal Resistance:** $\frac{1}{r_{eq}} = \frac{1}{r} + \dots \implies r_{eq} = \mathbf{\frac{r}{m}}$

Current through an external resistor $R$:
$$I = \frac{\varepsilon}{R + \frac{r}{m}} = \frac{m\varepsilon}{mR + r}$$

### 3. Mixed Grouping (Series + Parallel)

Suppose we have $n$ cells in series in a row, and we have $m$ such identical rows connected in parallel.
Total number of cells = $N = mn$.
- EMF of one row = $n\varepsilon$. (Since all rows are in parallel, the total EMF is just the EMF of one row).
  **$\varepsilon_{eq} = n\varepsilon$**
- Resistance of one row = $nr$. Since there are $m$ rows in parallel, the total internal resistance is:
  **$r_{eq} = \frac{nr}{m}$**

Current through external resistor $R$:
$$I = \frac{n\varepsilon}{R + \frac{nr}{m}} = \frac{mn\varepsilon}{mR + nr}$$

**Condition for Maximum Current in Mixed Grouping:** ⭐
Current is maximum when external resistance = total internal resistance.
$$R = \frac{nr}{m}$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic Series & Parallel Grouping ⭐

**Pattern:** "Find total current for purely series or parallel identical cells."

**Solved Example** 🟢

> Four identical cells, each of EMF $2\text{V}$ and internal resistance $0.5\text{ } \Omega$, are connected in series to an external resistor of $8\text{ } \Omega$. Find the current in the circuit.

<details>
<summary><b>Solution</b></summary>

For series combination:
$\varepsilon_{eq} = n\varepsilon = 4 \times 2 = 8\text{ V}$.
$r_{eq} = nr = 4 \times 0.5 = 2\text{ } \Omega$.

Current $I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{8}{8 + 2} = \frac{8}{10} = \mathbf{0.8\text{ A}}$.
</details>

**Practice:**

1. 🟢 Three cells, each of EMF $1.5\text{V}$ and internal resistance $1\text{ } \Omega$, are connected in parallel across a $2.5\text{ } \Omega$ resistor. Find the total current.

<details>
<summary><b>Answer</b></summary>

In parallel:
$\varepsilon_{eq} = 1.5\text{V}$ (Same as one cell).
$r_{eq} = r/m = 1/3\text{ } \Omega$.
$I = \frac{1.5}{2.5 + 1/3} = \frac{1.5}{(7.5 + 1)/3} = \frac{4.5}{8.5} \approx \mathbf{0.53\text{ A}}$.
</details>

2. 🟡 10 cells, each of EMF $E$ and internal resistance $r$, are connected in series. If 2 cells are connected with reverse polarity, what is the equivalent EMF and equivalent internal resistance?

<details>
<summary><b>Answer</b></summary>

Equivalent EMF: 2 reversed cells cancel out 2 forward cells. Net forward cells = $10 - 2(2) = 6$. So $\varepsilon_{eq} = \mathbf{6E}$.
Equivalent internal resistance: Polarity doesn't affect resistance. $r_{eq} = \mathbf{10r}$.
</details>

3. 🟡 A battery consists of a variable number $n$ of identical cells (each having EMF $E$ and internal resistance $r$) connected in series. The terminals are short-circuited. How does the short-circuit current vary with $n$?

<details>
<summary><b>Answer</b></summary>

Short circuit means $R = 0$.
$I = \frac{nE}{R + nr} = \frac{nE}{0 + nr} = \frac{nE}{nr} = \frac{E}{r}$.
The current is **independent of $n$**. Adding more cells in series doesn't increase short-circuit current!
</details>

---

### Type 2: Non-Identical Cells in Parallel ⭐⭐⭐

**Pattern:** "Two different cells ($\varepsilon_1, r_1$ and $\varepsilon_2, r_2$) are in parallel. Find equivalent EMF."

> 🔑 **THE MASTER FORMULA:**
> When two non-identical cells are in parallel:
> Equivalent EMF: **$\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}$**
> Equivalent Resistance: **$r_{eq} = \frac{r_1 r_2}{r_1 + r_2}$**
> *(Note: If they are connected with opposing polarities, use a minus sign for one of the EMFs).*

**Solved Example** 🔴

> Two cells of EMFs $1.5\text{V}$ and $2.0\text{V}$ having internal resistances $0.2\text{ } \Omega$ and $0.3\text{ } \Omega$ respectively are connected in parallel. Find the equivalent EMF and equivalent internal resistance of the combination.

<details>
<summary><b>Solution</b></summary>

Using the master formula for equivalent EMF:
$\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2} = \frac{(1.5 \times 0.3) + (2.0 \times 0.2)}{0.2 + 0.3}$
$\varepsilon_{eq} = \frac{0.45 + 0.40}{0.5} = \frac{0.85}{0.5} = \mathbf{1.7\text{ V}}$.

Equivalent internal resistance:
$r_{eq} = \frac{r_1 r_2}{r_1 + r_2} = \frac{0.2 \times 0.3}{0.2 + 0.3} = \frac{0.06}{0.5} = \mathbf{0.12\text{ } \Omega}$.
</details>

**Practice:**

1. 🟡 Two cells of EMFs $4\text{V}$ and $8\text{V}$ and internal resistances $1\text{ } \Omega$ and $2\text{ } \Omega$ are connected in parallel (positive to positive). Find the equivalent EMF.

<details>
<summary><b>Answer</b></summary>

$\varepsilon_{eq} = \frac{4(2) + 8(1)}{1 + 2} = \frac{8 + 8}{3} = \mathbf{\frac{16}{3}\text{ V}} \approx 5.33\text{ V}$.
</details>

2. 🔴 What if the same two cells (from Q1) are connected in parallel with opposing polarities (positive of one to negative of the other)?

<details>
<summary><b>Answer</b></summary>

Let $\varepsilon_1 = 4\text{V}$ and $\varepsilon_2 = -8\text{V}$ (opposing).
$\varepsilon_{eq} = \frac{4(2) + (-8)(1)}{1 + 2} = \frac{8 - 8}{3} = \mathbf{0\text{ V}}$.
*(The net EMF is zero! The batteries will just drain each other in a loop).*
</details>

3. 🔴 Three identical cells of EMF $E$ and internal resistance $r$ are connected in parallel. However, one cell is connected with reverse polarity. What is the equivalent EMF?

<details>
<summary><b>Answer</b></summary>

The general formula for $m$ parallel cells is $\frac{\varepsilon_{eq}}{r_{eq}} = \sum \frac{\varepsilon_i}{r_i}$.
Here $r_{eq} = r/3$.
$\frac{\varepsilon_{eq}}{r/3} = \frac{E}{r} + \frac{E}{r} - \frac{E}{r} = \frac{E}{r}$.
$\varepsilon_{eq} = (r/3) \times (E/r) = \mathbf{E/3}$.
</details>

---

### Type 3: Mixed Grouping Optimization ⭐⭐

**Pattern:** "Given $N$ cells, arrange them in $m$ rows of $n$ cells to get maximum current through $R$."

**Solved Example** 🟡

> You have 24 identical cells, each of internal resistance $1\text{ } \Omega$. You need to maximize the current through an external resistor of $1.5\text{ } \Omega$. How should you arrange the cells (how many in series per row, how many rows)?

<details>
<summary><b>Solution</b></summary>

Total cells $N = mn = 24 \implies m = 24/n$.
For maximum current, external resistance must equal total internal resistance.
$R = \frac{nr}{m}$
Substitute given values:
$1.5 = \frac{n(1)}{24/n} \implies 1.5 = \frac{n^2}{24}$
$n^2 = 1.5 \times 24 = 36$
$n = \mathbf{6}$ (cells in series per row).
$m = 24/n = 24/6 = \mathbf{4}$ (rows in parallel).
</details>

**Practice:**

1. 🟡 36 cells, each of internal resistance $0.5\text{ } \Omega$, are to be grouped to send maximum current through a $2\text{ } \Omega$ resistor. Find $m$ and $n$.

<details>
<summary><b>Answer</b></summary>

$mn = 36$.
$R = nr/m \implies 2 = n(0.5)/m \implies 2 = n(0.5)/(36/n) \implies 2 = 0.5n^2/36$.
$72 = 0.5n^2 \implies n^2 = 144 \implies \mathbf{n = 12}$.
$m = 36/12 = \mathbf{3}$.
</details>

2. 🔴 If the external resistance is extremely high (much larger than the internal resistance of any combination of the 36 cells), how should you connect them for maximum current?

<details>
<summary><b>Answer</b></summary>

If $R$ is very large, the denominator in $I = nE / (R + nr/m)$ is dominated by $R$.
To maximize $I$, we must maximize the numerator ($nE$).
To maximize $nE$, we must make $n$ as large as possible.
Therefore, connect **all cells in series** ($n=36, m=1$).
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 Two batteries, one of EMF $18\text{V}$ and internal resistance $2\text{ } \Omega$, and the other of EMF $12\text{V}$ and internal resistance $1\text{ } \Omega$, are connected in parallel. The combination is connected to an external resistance of $10\text{ } \Omega$. Find the current through the external resistance.

<details>
<summary><b>Solution</b></summary>

First, find the equivalent battery for the parallel combination:
$\varepsilon_{eq} = \frac{18(1) + 12(2)}{1 + 2} = \frac{18 + 24}{3} = \frac{42}{3} = 14\text{ V}$.
$r_{eq} = \frac{2 \times 1}{2 + 1} = \frac{2}{3}\text{ } \Omega$.

Now apply this equivalent battery to the external resistor $R = 10\text{ } \Omega$.
$I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{14}{10 + 2/3} = \frac{14}{32/3} = \frac{42}{32} = \mathbf{1.3125\text{ A}}$.
</details>

**Q2.** 🔴 ⭐ $N$ identical cells are connected in a closed loop (in series, positive to negative to positive...). What is the potential difference across any one cell?

<details>
<summary><b>Solution</b></summary>

Since they are in a closed loop, the total EMF is $NE$, and total internal resistance is $Nr$.
Current flowing in the loop is $I = \frac{NE}{Nr} = \frac{E}{r}$.
Now, find the terminal voltage across any *single* cell.
It is discharging, so $V = E - Ir$.
Substitute the current we found: $V = E - (E/r)r = E - E = \mathbf{0\text{ V}}$.
The terminal voltage of every cell in this loop is exactly zero!
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Why is it recommended to connect cells in parallel when the external resistance is very low compared to the internal resistance? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

When cells are in parallel, the current is $I = \frac{E}{R + r/m}$.
If $R$ is very low ($R \ll r/m$), the current $I \approx \frac{E}{r/m} = m \frac{E}{r}$.
The current is $m$ times the current given by a single cell. Thus, connecting cells in parallel significantly increases the current when external resistance is negligible.
</details>

**Q2.** 🟡 Deduce the expression for the equivalent EMF and equivalent internal resistance for two cells connected in parallel. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

Let two cells ($\varepsilon_1, r_1$) and ($\varepsilon_2, r_2$) be in parallel.
Total current $I = I_1 + I_2$.
The terminal voltage $V$ across both cells is the same.
From cell 1: $V = \varepsilon_1 - I_1 r_1 \implies I_1 = (\varepsilon_1 - V)/r_1$.
From cell 2: $V = \varepsilon_2 - I_2 r_2 \implies I_2 = (\varepsilon_2 - V)/r_2$.
Substitute into total current:
$I = \left(\frac{\varepsilon_1}{r_1} + \frac{\varepsilon_2}{r_2}\right) - V\left(\frac{1}{r_1} + \frac{1}{r_2}\right)$.
Rearranging for $V$:
$V = \frac{\frac{\varepsilon_1}{r_1} + \frac{\varepsilon_2}{r_2}}{\frac{1}{r_1} + \frac{1}{r_2}} - I \frac{1}{\frac{1}{r_1} + \frac{1}{r_2}}$.
Comparing this with the standard equivalent cell equation $V = \varepsilon_{eq} - I r_{eq}$, we get:
$\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}$ and $r_{eq} = \frac{r_1 r_2}{r_1 + r_2}$.
</details>

**Q3.** 🟡 You have 10 identical cells. You connect them in series, but mistakenly connect 1 cell in reverse. How much does the total EMF decrease compared to the correct arrangement? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Correct arrangement EMF = $10E$.
When 1 is reversed, it cancels out 1 correct cell. The effective number of forward cells is $10 - 2(1) = 8$.
New EMF = $8E$.
The decrease in EMF is $10E - 8E = \mathbf{2E}$.
*(Common mistake: Students say it decreases by 1E. But one reversed cell subtracts its own EMF AND neutralizes another cell's EMF!).*
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ In a mixed grouping of identical cells, there are $n$ identical cells in series per row, and $m$ such rows in parallel. The maximum power delivered to the external resistance $R$ is:
(Given $E$ is EMF of one cell, $r$ is internal resistance of one cell, and total cells $N = mn$).

(a) $\frac{N E^2}{4r}$ &emsp; (b) $\frac{N^2 E^2}{4r}$ &emsp; (c) $\frac{N E^2}{2r}$ &emsp; (d) $\frac{E^2}{4r}$

<details>
<summary><b>Answer</b></summary>

Maximum power occurs when $R = nr/m$.
At this condition, equivalent EMF = $nE$. Equivalent internal resistance = $nr/m = R$.
$P_{max} = \frac{V_{eq}^2}{4 R_{eq}} = \frac{(nE)^2}{4(nr/m)} = \frac{n^2 E^2 m}{4nr} = \frac{mn E^2}{4r}$.
Since $mn = N$, $P_{max} = \mathbf{\frac{N E^2}{4r}}$.

**Answer: (a)**
</details>

**Q2.** 🔴 Two non-ideal batteries are connected in parallel. Consider the following statements:
(A) The equivalent EMF is smaller than either of the two EMFs.
(B) The equivalent internal resistance is smaller than either of the two internal resistances.

(a) Both A and B are correct
(b) A is correct but B is wrong
(c) B is correct but A is wrong
(d) Both A and B are wrong

<details>
<summary><b>Answer</b></summary>

Statement A: $\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}$. This is a weighted average of $\varepsilon_1$ and $\varepsilon_2$. A weighted average ALWAYS lies *between* the two values. Therefore, it is larger than the smaller EMF and smaller than the larger EMF. Statement A is **wrong**.
Statement B: Equivalent resistance of parallel resistors is ALWAYS smaller than the smallest individual resistor. Statement B is **correct**.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ 100 cells each of EMF $5\text{V}$ and internal resistance $1\text{ } \Omega$ are to be arranged to produce maximum current in a $25\text{ } \Omega$ resistance. Each row contains equal number of cells. The number of rows should be:

(a) 2 &emsp; (b) 4 &emsp; (c) 5 &emsp; (d) 10

<details>
<summary><b>Answer</b></summary>

$N = mn = 100 \implies n = 100/m$.
Condition for max current: $R = nr/m$.
Substitute values: $25 = n(1)/m$.
$25 = (100/m)/m \implies 25 = 100/m^2$.
$m^2 = 100/25 = 4 \implies \mathbf{m = 2}$.
*(Number of rows $m = 2$. Number of cells per row $n = 50$.)*

**Answer: (a)**
</details>

---

*Next: [Chapter 11 — Kirchhoff's Rules →](./11_kirchhoffs_rules.md)*
