# Chapter 10: Cells in Series and Parallel (Grouping of Cells)

> *NCERT Section 3.11*

---

## 🎯 Stage 1: The Core Idea

### Why Group Cells?<br>

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

> **What if one cell is reversed?<br>** ⭐
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

2. 🟡 10 cells, each of EMF $E$ and internal resistance $r$, are connected in series. If 2 cells are connected with reverse polarity, what is the equivalent EMF and equivalent internal resistance?<br>

<details>
<summary><b>Answer</b></summary>

Equivalent EMF: 2 reversed cells cancel out 2 forward cells. Net forward cells = $10 - 2(2) = 6$. So $\varepsilon_{eq} = \mathbf{6E}$.
Equivalent internal resistance: Polarity doesn't affect resistance. $r_{eq} = \mathbf{10r}$.
</details>

3. 🟡 A battery consists of a variable number $n$ of identical cells (each having EMF $E$ and internal resistance $r$) connected in series. The terminals are short-circuited. How does the short-circuit current vary with $n$?<br>

<details>
<summary><b>Answer</b></summary>

Short circuit means $R = 0$.
$I = \frac{nE}{R + nr} = \frac{nE}{0 + nr} = \frac{nE}{nr} = \frac{E}{r}$.
The current is **independent of $n$**. Adding more cells in series doesn't increase short-circuit current!
</details>

4. 🟢 Five identical cells, each of EMF $1.5\text{ V}$ and internal resistance $0.2\text{ }\Omega$, are connected in series. Find the equivalent EMF and the short-circuit current of this combination.

<details>
<summary><b>Answer</b></summary>

$\varepsilon_{eq} = n \varepsilon = 5 \times 1.5 = \mathbf{7.5\text{ V}}$.
Short-circuit current $I_{short} = \frac{\varepsilon_{eq}}{n r} = \frac{7.5}{5 \times 0.2} = \frac{7.5}{1.0} = \mathbf{7.5\text{ A}}$.
</details>

5. 🟡 In a series combination of 8 identical cells (each of EMF $2.0\text{ V}$ and internal resistance $0.5\text{ }\Omega$), some cells are connected incorrectly with reversed polarity. The equivalent EMF of the combination is found to be $8.0\text{ V}$. Find the number of incorrectly connected cells.

<details>
<summary><b>Answer</b></summary>

Let $x$ be the number of incorrectly connected cells.
The equivalent EMF is given by $\varepsilon_{eq} = (n - 2x)\varepsilon$.
Substitute the given values: $8.0 = (8 - 2x) \times 2.0 \implies 4 = 8 - 2x \implies 2x = 4 \implies x = \mathbf{2}$.
So, 2 cells are connected with reversed polarity.
</details>

6. 🟢 Three identical cells, each of EMF $2\text{ V}$ and internal resistance $0.3\text{ }\Omega$, are connected in parallel. What is the equivalent EMF and the equivalent internal resistance of the combination?

<details>
<summary><b>Answer</b></summary>

In parallel, the equivalent EMF is equal to the EMF of a single cell: $\varepsilon_{eq} = \mathbf{2\text{ V}}$.
The equivalent internal resistance is $r_{eq} = \frac{r}{m} = \frac{0.3}{3} = \mathbf{0.1\text{ }\Omega}$.
</details>

7. 🟡 ⭐ A series combination of $n$ identical cells, each of EMF $E$ and internal resistance $r$, is connected across a variable external resistor $R$. Write the expression for the current $I$ and find the value of $R$ for which the terminal voltage across the battery combination is maximum.

<details>
<summary><b>Answer</b></summary>

The current is $I = \frac{nE}{R + nr}$.
The terminal voltage across the combination is $V = I R = \frac{nE R}{R + nr} = nE \left(\frac{1}{1 + \frac{nr}{R}}\right)$.
To maximize $V$, the term $\frac{nr}{R}$ should be as small as possible, which occurs when $R \rightarrow \infty$ (open circuit). The maximum terminal voltage is $V_{max} = \mathbf{nE}$, and it occurs at $R \rightarrow \infty$ (specifically, $\mathbf{R \gg nr}$).
</details>

8. 🟡 Five identical cells are connected in series. If the current through an external resistance of $10\text{ }\Omega$ is $0.5\text{ A}$ and the current through an external resistance of $22\text{ }\Omega$ is $0.25\text{ A}$, find the EMF and internal resistance of each cell.

<details>
<summary><b>Answer</b></summary>

For series combination of 5 cells:
$I = \frac{5E}{R + 5r}$.
Case 1: $0.5 = \frac{5E}{10 + 5r} \implies 5 + 2.5r = 5E \implies 2 + r = 2E$.
Case 2: $0.25 = \frac{5E}{22 + 5r} \implies 5.5 + 1.25r = 5E \implies 2.2 + 0.5r = 2E$.
Equating the two: $2 + r = 2.2 + 0.5r \implies 0.5r = 0.2 \implies \mathbf{r = 0.4\text{ }\Omega}$.
Substitute $r$ into Case 1: $2E = 2 + 0.4 = 2.4 \implies \mathbf{E = 1.2\text{ V}}$.
</details>

9. 🔴 Ten cells, each of EMF $1.5\text{ V}$ and internal resistance $0.5\text{ }\Omega$, are connected in parallel. If this combination is connected to an external resistor of $2.45\text{ }\Omega$, find the current through the external resistor and the rate of chemical energy consumption in each cell.

<details>
<summary><b>Answer</b></summary>

In parallel:
$\varepsilon_{eq} = 1.5\text{ V}$.
$r_{eq} = \frac{0.5}{10} = 0.05\text{ }\Omega$.
Current in the external circuit $I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{1.5}{2.45 + 0.05} = \frac{1.5}{2.50} = \mathbf{0.6\text{ A}}$.
Since the cells are identical and connected in parallel, they share the current equally.
Current through each cell $I_i = \frac{I}{10} = \frac{0.6}{10} = 0.06\text{ A}$.
Rate of chemical energy consumption in each cell = $E \times I_i = 1.5\text{ V} \times 0.06\text{ A} = \mathbf{0.09\text{ W}}$.
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

2. 🔴 What if the same two cells (from Q1) are connected in parallel with opposing polarities (positive of one to negative of the other)?<br>

<details>
<summary><b>Answer</b></summary>

Let $\varepsilon_1 = 4\text{V}$ and $\varepsilon_2 = -8\text{V}$ (opposing).
$\varepsilon_{eq} = \frac{4(2) + (-8)(1)}{1 + 2} = \frac{8 - 8}{3} = \mathbf{0\text{ V}}$.
*(The net EMF is zero! The batteries will just drain each other in a loop).*
</details>

3. 🔴 Three identical cells of EMF $E$ and internal resistance $r$ are connected in parallel. However, one cell is connected with reverse polarity. What is the equivalent EMF?<br>

<details>
<summary><b>Answer</b></summary>

The general formula for $m$ parallel cells is $\frac{\varepsilon_{eq}}{r_{eq}} = \sum \frac{\varepsilon_i}{r_i}$.
Here $r_{eq} = r/3$.
$\frac{\varepsilon_{eq}}{r/3} = \frac{E}{r} + \frac{E}{r} - \frac{E}{r} = \frac{E}{r}$.
$\varepsilon_{eq} = (r/3) \times (E/r) = \mathbf{E/3}$.
</details>

4. 🟡 Two cells of EMF $2.0\text{ V}$ and $1.5\text{ V}$ and internal resistances $0.5\text{ }\Omega$ and $0.25\text{ }\Omega$ respectively are connected in parallel (positive terminals together). Find the equivalent EMF and equivalent internal resistance.

<details>
<summary><b>Answer</b></summary>

Using the parallel cell formula:
$\varepsilon_{eq} = \frac{E_1 r_2 + E_2 r_1}{r_1 + r_2} = \frac{2.0 \times 0.25 + 1.5 \times 0.5}{0.5 + 0.25} = \frac{0.5 + 0.75}{0.75} = \frac{1.25}{0.75} = \mathbf{1.67\text{ V}}$.
$r_{eq} = \frac{r_1 r_2}{r_1 + r_2} = \frac{0.5 \times 0.25}{0.5 + 0.25} = \frac{0.125}{0.75} = \mathbf{0.17\text{ }\Omega}$.
</details>

5. 🟡 ⭐ Two cells of EMFs $3\text{ V}$ and $4\text{ V}$ having internal resistances $1\text{ }\Omega$ and $2\text{ }\Omega$ respectively are connected in parallel across an external resistor of $5\text{ }\Omega$. Find the current through the external resistor.

<details>
<summary><b>Answer</b></summary>

First, find equivalent battery:
$\varepsilon_{eq} = \frac{3 \times 2 + 4 \times 1}{1 + 2} = \frac{6 + 4}{3} = \frac{10}{3}\text{ V}$.
$r_{eq} = \frac{1 \times 2}{1 + 2} = \frac{2}{3}\text{ }\Omega$.
Now, find the current through $R = 5\text{ }\Omega$:
$I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{10/3}{5 + 2/3} = \frac{10/3}{17/3} = \frac{10}{17} \approx \mathbf{0.59\text{ A}}$.
</details>

6. 🔴 Two batteries of EMF $6\text{ V}$ and $12\text{ V}$ with internal resistances $1\text{ }\Omega$ and $2\text{ }\Omega$ respectively are connected in parallel, but with opposite polarity (positive of one to negative of the other). If they are connected to a load of $5\text{ }\Omega$, find the terminal potential difference across the combination.

<details>
<summary><b>Answer</b></summary>

Let $\varepsilon_1 = 6\text{ V}$ and $\varepsilon_2 = -12\text{ V}$ (opposing polarity).
$\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2} = \frac{6 \times 2 + (-12) \times 1}{1 + 2} = \frac{12 - 12}{3} = \mathbf{0\text{ V}}$.
$r_{eq} = \frac{1 \times 2}{1 + 2} = \frac{2}{3}\text{ }\Omega$.
Since $\varepsilon_{eq} = 0\text{ V}$, the terminal potential difference across the load $R = 5\text{ }\Omega$ is $V = I R = \frac{\varepsilon_{eq}}{R + r_{eq}} R = \mathbf{0\text{ V}}$.
</details>

7. 🟡 A cell of EMF $1.5\text{ V}$ and internal resistance $0.2\text{ }\Omega$ is connected in parallel with another cell of EMF $2.0\text{ V}$ and internal resistance $0.5\text{ }\Omega$. What is the current flowing in the local loop formed by the two batteries if no external load is connected?

<details>
<summary><b>Answer</b></summary>

The loop consists of the two cells connected positive-to-positive and negative-to-negative.
The net EMF driving current around the loop is $E_{net} = E_2 - E_1 = 2.0 - 1.5 = 0.5\text{ V}$.
The total resistance of the loop is $r_1 + r_2 = 0.2 + 0.5 = 0.7\text{ }\Omega$.
The current flowing in the loop is $I_{loop} = \frac{E_{net}}{r_1 + r_2} = \frac{0.5}{0.7} = \mathbf{0.71\text{ A}}$.
</details>

8. 🔴 Show that when two non-identical cells of EMFs $E_1, E_2$ and internal resistances $r_1, r_2$ are connected in parallel, the current through an external resistance $R$ is given by $I = \frac{E_1 r_2 + E_2 r_1}{R(r_1+r_2) + r_1 r_2}$.

<details>
<summary><b>Answer</b></summary>

Let the currents in the two cells be $I_1$ and $I_2$.
$I = I_1 + I_2$.
The terminal voltage across $R$ is $V = I R$.
We also have:
$V = E_1 - I_1 r_1 \implies I_1 = \frac{E_1 - V}{r_1}$.
$V = E_2 - I_2 r_2 \implies I_2 = \frac{E_2 - V}{r_2}$.
So, $I = \frac{E_1 - V}{r_1} + \frac{E_2 - V}{r_2} = \left(\frac{E_1}{r_1} + \frac{E_2}{r_2}\right) - V\left(\frac{1}{r_1} + \frac{1}{r_2}\right)$.
Substitute $V = I R$:
$I = \left(\frac{E_1}{r_1} + \frac{E_2}{r_2}\right) - I R \left(\frac{r_1 + r_2}{r_1 r_2}\right) \implies I \left[1 + R\left(\frac{r_1+r_2}{r_1 r_2}\right)\right] = \frac{E_1 r_2 + E_2 r_1}{r_1 r_2}$.
Multiply by $r_1 r_2$:
$I [r_1 r_2 + R(r_1 + r_2)] = E_1 r_2 + E_2 r_1$.
Therefore, $I = \mathbf{\frac{E_1 r_2 + E_2 r_1}{R(r_1+r_2) + r_1 r_2}}$.
</details>

9. 🟡 Two cells of EMFs $E_1$ and $E_2$ with internal resistances $r_1$ and $r_2$ are in parallel. If the equivalent EMF is equal to $E_1$, what must be the relation between $E_1$, $E_2$, $r_1$, and $r_2$?

<details>
<summary><b>Answer</b></summary>

We are given $\varepsilon_{eq} = E_1$.
$\frac{E_1 r_2 + E_2 r_1}{r_1 + r_2} = E_1 \implies E_1 r_2 + E_2 r_1 = E_1 r_1 + E_1 r_2 \implies E_2 r_1 = E_1 r_1$.
Since $r_1 \neq 0$, we divide by $r_1$ to get $\mathbf{E_1 = E_2}$.
Thus, the EMFs of the two cells must be equal.
</details>

---

### Type 3: Mixed Grouping Optimization ⭐⭐

**Pattern:** "Given $N$ cells, arrange them in $m$ rows of $n$ cells to get maximum current through $R$."

**Solved Example** 🟡

> You have 24 identical cells, each of internal resistance $1\text{ } \Omega$. You need to maximize the current through an external resistor of $1.5\text{ } \Omega$. How should you arrange the cells (how many in series per row, how many rows)?<br>

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

2. 🔴 If the external resistance is extremely high (much larger than the internal resistance of any combination of the 36 cells), how should you connect them for maximum current?<br>

<details>
<summary><b>Answer</b></summary>

If $R$ is very large, the denominator in $I = nE / (R + nr/m)$ is dominated by $R$.
To maximize $I$, we must maximize the numerator ($nE$).
To maximize $nE$, we must make $n$ as large as possible.
Therefore, connect **all cells in series** ($n=36, m=1$).
</details>

3. 🟢 You have 12 identical cells, each of internal resistance $0.5\text{ }\Omega$. You want to connect them to get maximum current through a $1.5\text{ }\Omega$ resistor. Find the configuration.

<details>
<summary><b>Answer</b></summary>

Total cells $N = mn = 12 \implies m = 12/n$.
For max current: $R = \frac{nr}{m} \implies 1.5 = \frac{n \times 0.5}{12/n} = \frac{0.5 n^2}{12}$.
$n^2 = \frac{1.5 \times 12}{0.5} = 3 \times 12 = 36 \implies n = \mathbf{6}$ cells in series.
Number of rows $m = 12/6 = \mathbf{2}$ rows in parallel.
</details>

4. 🟡 ⭐ In a mixed grouping of cells, we have $m$ parallel rows, each containing $n$ cells in series. If each cell has EMF $E$ and internal resistance $r$, and the load resistance is $R$, show that the current in the load is maximum when the internal resistance of the combination equals the load resistance.

<details>
<summary><b>Answer</b></summary>

The current is $I = \frac{mnE}{mR + nr} = \frac{NE}{mR + nr}$.
To maximize $I$, we need to minimize the denominator $D = mR + nr$ subject to $mn = N$ (constant).
We can rewrite $D = (\sqrt{mR} - \sqrt{nr})^2 + 2\sqrt{mnRr}$.
Since $N = mn$ is constant, the second term $2\sqrt{NRr}$ is constant.
The term $(\sqrt{mR} - \sqrt{nr})^2$ is always non-negative and achieves its minimum value of 0 when $\sqrt{mR} = \sqrt{nr} \implies mR = nr \implies R = \mathbf{\frac{nr}{m}}$.
This shows that current is maximum when the load resistance equals the equivalent internal resistance of the cell combination.
</details>

5. 🟡 Find the maximum current that can be sent through a $2\text{ }\Omega$ resistor using 36 cells, each of EMF $1.5\text{ V}$ and internal resistance $0.5\text{ }\Omega$.

<details>
<summary><b>Answer</b></summary>

First, find the optimal grouping for maximum current:
$mn = 36 \implies m = 36/n$.
$R = \frac{nr}{m} \implies 2 = \frac{n \times 0.5}{36/n} = \frac{0.5 n^2}{36} \implies n^2 = \frac{72}{0.5} = 144 \implies n = \mathbf{12}$.
$m = 36/12 = \mathbf{3}$.
Now, calculate the maximum current:
$I_{max} = \frac{mnE}{mR + nr} = \frac{36 \times 1.5}{3 \times 2 + 12 \times 0.5} = \frac{54}{6 + 6} = \frac{54}{12} = \mathbf{4.5\text{ A}}$.
</details>

6. 🔴 A mixed grouping of 48 cells is used to send maximum current through a load of $3\text{ }\Omega$. If the internal resistance of each cell is $1\text{ }\Omega$ and its EMF is $2.0\text{ V}$, find the power dissipated in the load.

<details>
<summary><b>Answer</b></summary>

Find optimal grouping:
$mn = 48 \implies m = 48/n$.
$R = \frac{nr}{m} \implies 3 = \frac{n \times 1}{48/n} = \frac{n^2}{48} \implies n^2 = 144 \implies n = \mathbf{12}$.
$m = 48/12 = \mathbf{4}$.
The maximum current is:
$I_{max} = \frac{mnE}{mR + nr} = \frac{48 \times 2.0}{4 \times 3 + 12 \times 1} = \frac{96}{12 + 12} = \frac{96}{24} = \mathbf{4\text{ A}}$.
The power dissipated in the load is $P = I_{max}^2 R = 4^2 \times 3 = 16 \times 3 = \mathbf{48\text{ W}}$.
</details>

7. 🟡 If you have 50 cells, each with internal resistance $r = 1\text{ }\Omega$, and want to deliver maximum power to a load $R = 2\text{ }\Omega$, can you find an exact mixed grouping arrangement? If not, what is the closest practical arrangement?

<details>
<summary><b>Answer</b></summary>

For exact maximum power:
$mn = 50 \implies m = 50/n$.
$R = \frac{nr}{m} \implies 2 = \frac{n \times 1}{50/n} = \frac{n^2}{50} \implies n^2 = 100 \implies n = \mathbf{10}$.
$m = 50/10 = \mathbf{5}$.
Since both $n = 10$ and $m = 5$ are integers and their product is exactly 50, an exact mixed grouping arrangement **does exist** with $\mathbf{n = 10}$ cells in series per row and $\mathbf{m = 5}$ rows in parallel.
</details>

8. 🟡 A group of cells is connected in a mixed grouping with $m$ rows in parallel, each row having $n$ cells in series. If the EMF of each cell is $1.5\text{ V}$ and its internal resistance is $0.5\text{ }\Omega$, and $n=20$, $m=5$, what is the terminal voltage of the combination when connected to a load resistor of $2\text{ }\Omega$?

<details>
<summary><b>Answer</b></summary>

Equivalent EMF $\varepsilon_{eq} = nE = 20 \times 1.5 = 30\text{ V}$.
Equivalent internal resistance $r_{eq} = \frac{nr}{m} = \frac{20 \times 0.5}{5} = \frac{10}{5} = 2\text{ }\Omega$.
Current through external load $R = 2\text{ }\Omega$:
$I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{30}{2 + 2} = 7.5\text{ A}$.
Terminal voltage $V = I R = 7.5 \times 2 = \mathbf{15\text{ V}}$ (or $V = \varepsilon_{eq} - I r_{eq} = 30 - 7.5 \times 2 = \mathbf{15\text{ V}}$).
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1.** Two identical cells of EMF $E$ and internal resistance $r$ are connected in parallel. The equivalent EMF and internal resistance are:
(a) $2E$, $2r$ &emsp; (b) $E$, $r/2$ &emsp; (c) $2E$, $r/2$ &emsp; (d) $E$, $2r$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

For parallel combination of identical cells, the EMF remains the same as that of a single cell ($E$), and the internal resistance is halved ($r/2$).
</details>

**Q2.** When $n$ identical cells are connected in series, the equivalent internal resistance is:
(a) $r/n$ &emsp; (b) $nr$ &emsp; (c) $r$ &emsp; (d) $n^2 r$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

In series, resistances simply add up: $r + r + \dots = \mathbf{nr}$.
</details>

**Q3.** In a series combination of $N$ cells, if $n$ cells are wrongly connected (reversed polarity), the net EMF of the combination becomes (each cell has EMF $E$):
(a) $(N-n)E$ &emsp; (b) $(N-2n)E$ &emsp; (c) $NE - nE$ &emsp; (d) $(N+2n)E$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

A wrongly connected cell opposes the EMF of the others, canceling its own EMF and also neutralizing one correctly connected cell. Thus, the effective EMF is $\mathbf{(N-2n)E}$.
</details>

**Q4.** To get maximum current through a very low external resistance, the cells should be connected in:
(a) series
(b) parallel
(c) mixed grouping with $m = n$
(d) series-parallel with $n > m$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

When external resistance $R \approx 0$, the series current is $I_{series} = E/r$ (independent of the number of cells). The parallel current is $I_{parallel} = mE/r$, which is $m$ times larger. Hence, parallel grouping is best.
</details>

**Q5.** To get maximum current through a very high external resistance, the cells should be connected in:
(a) series
(b) parallel
(c) mixed grouping with $m = n$
(d) none of these

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

When external resistance $R \gg r$, the current in series is $nE/R$, which is $n$ times that of a single cell, whereas in parallel the current is $E/R$. Hence, series grouping is best.
</details>

**Q6.** For a mixed grouping of $N$ identical cells (each of internal resistance $r$) connected to a load $R$, the current is maximum when:
(a) $R = r$
(b) $R = Nr$
(c) $R = nr/m$
(d) $R = mr/n$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Maximum current is obtained when the load resistance equals the equivalent internal resistance of the combination, which is $r_{eq} = \mathbf{nr/m}$.
</details>

**Q7.** **Statement I:** In mixed grouping of cells, the maximum current is obtained when the external resistance is equal to the total internal resistance of all the cells.
**Statement II:** The equivalent internal resistance of a mixed grouping of $mn$ cells (with $n$ in series per row and $m$ rows in parallel) is $nr/m$.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Statement I is the condition for maximum current in mixed grouping. Statement II gives the formula for the equivalent internal resistance. Since the maximum current condition is $R = r_{eq}$, and $r_{eq} = nr/m$, Statement II is the correct explanation.
</details>

**Q8.** **Statement I:** If two cells of different EMFs $E_1$ and $E_2$ ($E_1 > E_2$) are connected in parallel, the equivalent EMF $E_{eq}$ is always less than $E_1$ and greater than $E_2$.
**Statement II:** The equivalent EMF of two cells in parallel is a weighted average of their individual EMFs, which always lies between the two values.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

The formula is $E_{eq} = \frac{E_1 r_2 + E_2 r_1}{r_1 + r_2}$, which is a weighted average of $E_1$ and $E_2$. Therefore, $E_{eq}$ must lie strictly between $E_1$ and $E_2$.
</details>

**Q9.** **Statement I:** When cells are connected in series, the total internal resistance increases.
**Statement II:** When cells are connected in parallel, the total internal resistance decreases.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Both statements are true and describe the resistance behavior in series and parallel groupings, but Statement II does not explain Statement I.
</details>

**Q10.** Two non-identical cells of EMFs $2\text{ V}$ and $1\text{ V}$ and internal resistances $1\text{ }\Omega$ and $2\text{ }\Omega$ are connected in parallel with opposite polarity. The equivalent EMF of the combination is:
(a) $1.5\text{ V}$
(b) $1.0\text{ V}$
(c) $0.67\text{ V}$
(d) $3.0\text{ V}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Here, $\varepsilon_1 = 2\text{ V}$, $r_1 = 1\text{ }\Omega$, $\varepsilon_2 = -1\text{ V}$ (opposite polarity), $r_2 = 2\text{ }\Omega$.
Using the formula:
$\varepsilon_{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2} = \frac{2 \times 2 + (-1) \times 1}{1 + 2} = \frac{4 - 1}{3} = \frac{3}{3} = \mathbf{1.0\text{ V}}$.
</details>

**Q11.** If $N$ identical cells are connected in series to form a closed loop, the current in the loop is:
(a) zero
(b) $E/r$
(c) $NE/r$
(d) infinite

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

The total EMF in the loop is $NE$, and the total internal resistance is $Nr$. Thus, the current is $I = NE / Nr = \mathbf{E/r}$.
</details>

**Q12.** In the closed loop of $N$ identical cells (from Q11), the potential difference across the terminals of any one cell is:
(a) $E$
(b) $E/N$
(c) zero
(d) $E - E/N$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Each cell is discharging, so the terminal voltage is $V = E - Ir$. Since $I = E/r$, we get $V = E - (E/r)r = \mathbf{0\text{ V}}$.
</details>

**Q13.** Two identical cells of EMF $E$ and internal resistance $r$ are connected in parallel across an external resistance $R$. The power dissipated in the external resistor is maximum when:
(a) $R = r$
(b) $R = 2r$
(c) $R = r/2$
(d) $R = 0$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The equivalent internal resistance of the two cells in parallel is $r_{eq} = r/2$. The power dissipated in the load is maximum when $R = r_{eq} = \mathbf{r/2}$.
</details>

**Q14.** We have 4 cells, each of EMF $2\text{ V}$ and internal resistance $1\text{ }\Omega$. What is the maximum current they can deliver to an external resistor of $1\text{ }\Omega$?
(a) $2\text{ A}$
(b) $1.5\text{ A}$
(c) $4\text{ A}$
(d) $1\text{ A}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Let's test the configurations:
1. All series ($n=4, m=1$): $I = \frac{4 \times 2}{1 + 4 \times 1} = \frac{8}{5} = 1.6\text{ A}$.
2. All parallel ($n=1, m=4$): $I = \frac{1 \times 2}{1 + 1/4} = \frac{2}{1.25} = 1.6\text{ A}$.
3. Mixed ($n=2, m=2$): $I = \frac{2 \times 2}{1 + (2 \times 1)/2} = \frac{4}{1 + 1} = \mathbf{2\text{ A}}$.
Thus, the mixed grouping with $n=2, m=2$ yields the maximum current of $2\text{ A}$.
</details>

**Q15.** When two cells of EMFs $E_1, E_2$ and internal resistances $r_1, r_2$ are connected in parallel, the equivalent internal resistance $r_{eq}$ is:
(a) $r_1 + r_2$
(b) $\frac{r_1 r_2}{r_1 + r_2}$
(c) $\frac{E_1 r_2 + E_2 r_1}{E_1 + E_2}$
(d) $\frac{E_1 r_1 + E_2 r_2}{E_1 + E_2}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

The equivalent internal resistance of parallel cells is always the parallel combination of their individual internal resistances: $r_{eq} = \mathbf{\frac{r_1 r_2}{r_1 + r_2}}$.
</details>

**Q16.** **Statement I:** In parallel grouping of cells, if the cells are not identical, current may flow through the cells even when the external circuit is open.
**Statement II:** A net loop EMF exists in an open-circuit parallel combination of non-identical cells, causing a circulating current.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

If two cells of different EMFs ($E_1 \neq E_2$) are in parallel, they form a closed loop. The net EMF in this loop is $E_1 - E_2 \neq 0$, which drives a current $I = (E_1 - E_2)/(r_1 + r_2)$ around the loop even when the external switch is open.
</details>

**Q17.** A cell of EMF $E$ and internal resistance $r$ is connected to $n-1$ identical cells in series (all in the same direction). If the polarity of the first cell is reversed, the net EMF of the combination decreases by:
(a) $E$
(b) $2E$
(c) $nE$
(d) $(n-2)E$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Originally, all $n$ cells are in the same direction, so net EMF is $nE$. When one cell is reversed, the net EMF becomes $(n-2)E$. The decrease in EMF is $nE - (n-2)E = \mathbf{2E}$.
</details>

**Q18.** A battery of 10 cells in series has an EMF of $15\text{ V}$. If one cell is connected backwards, the terminal potential difference across an external resistance of $10\text{ }\Omega$ (neglecting internal resistances) will be:
(a) $15\text{ V}$
(b) $13.5\text{ V}$
(c) $12\text{ V}$
(d) $10\text{ V}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Each cell has EMF $1.5\text{ V}$ (since 10 cells in series give $15\text{ V}$).
When one cell is connected backwards, the net EMF becomes $(10 - 2 \times 1) \times 1.5 = 8 \times 1.5 = \mathbf{12\text{ V}}$.
Since internal resistances are neglected, the terminal potential difference is equal to the net EMF, which is $12\text{ V}$.
</details>

**Q19.** Which grouping of cells is preferred to obtain a large voltage?
(a) Series grouping
(b) Parallel grouping
(c) Mixed grouping with $m \gg n$
(d) None of these

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Series grouping adds the EMFs of the cells ($\varepsilon_{eq} = n \varepsilon$), so it is used to obtain a larger voltage.
</details>

**Q20.** Two non-identical cells in parallel have equivalent EMF $E_{eq}$ and equivalent internal resistance $r_{eq}$. If the external resistance connected across them is very large, the terminal voltage is:
(a) $E_{eq}$
(b) $E_{eq} - I r_{eq}$
(c) both (a) and (b) are approximately correct as $I \rightarrow 0$
(d) zero

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

When the external resistance $R$ is very large, the current $I$ drawn from the combination is very small ($I \rightarrow 0$). In this case, the terminal voltage is $V = E_{eq} - Ir_{eq} \approx E_{eq}$. Hence, both expressions are correct in this context.
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🔴 Two batteries, one of EMF $18\text{V}$ and internal resistance $2\text{ } \Omega$, and the other of EMF $12\text{V}$ and internal resistance $1\text{ } \Omega$, are connected in parallel. The combination is connected to an external resistance of $10\text{ } \Omega$. Find the current through the external resistance.

<details>
<summary><b>Solution</b></summary>

First, find the equivalent battery for the parallel combination:
$\varepsilon_{eq} = \frac{18(1) + 12(2)}{1 + 2} = \frac{18 + 24}{3} = \frac{42}{3} = 14\text{ V}$.
$r_{eq} = \frac{2 \times 1}{2 + 1} = \frac{2}{3}\text{ } \Omega$.

Now apply this equivalent battery to the external resistor $R = 10\text{ } \Omega$.
$I = \frac{\varepsilon_{eq}}{R + r_{eq}} = \frac{14}{10 + 2/3} = \frac{14}{32/3} = \frac{14}{32} = \frac{42}{32} = \mathbf{1.3125\text{ A}}$.
</details>

**Q2.** 🔴 ⭐ $N$ identical cells are connected in a closed loop (in series, positive to negative to positive...). What is the potential difference across any one cell?<br>

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

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Why is it recommended to connect cells in parallel when the external resistance is very low compared to the internal resistance?<br> *(2 marks)*

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

**Q3.** 🟡 You have 10 identical cells. You connect them in series, but mistakenly connect 1 cell in reverse. How much does the total EMF decrease compared to the correct arrangement?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Correct arrangement EMF = $10E$.
When 1 is reversed, it cancels out 1 correct cell. The effective number of forward cells is $10 - 2(1) = 8$.
New EMF = $8E$.
The decrease in EMF is $10E - 8E = \mathbf{2E}$.
*(Common mistake: Students say it decreases by 1E. But one reversed cell subtracts its own EMF AND neutralizes another cell's EMF!).*
</details>

---

## 🚀 Stage 7: JEE Mains Arena

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
<br>
(A) The equivalent EMF is smaller than either of the two EMFs.
<br>
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
