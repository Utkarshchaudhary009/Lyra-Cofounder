# Chapter 14: Potentiometer

> *NCERT Section 3.16 (Note: Potentiometer has been removed from the latest CBSE reduced syllabus, but remains highly relevant for JEE Mains and Advanced).*

---

## 🎯 Stage 1: The Core Idea

### The Ideal Voltmeter

A normal voltmeter has a high resistance, but it's not infinite. When you connect it across a battery to measure its voltage, it draws a tiny bit of current. 
Because it draws current, it measures the *terminal voltage* ($V = \varepsilon - Ir$), not the true *EMF* ($\varepsilon$).

A **Potentiometer** is an instrument that measures potential difference **without drawing any current** from the circuit being measured. It is the only true "ideal voltmeter".

### How does it work?<br> (The Balance of Power)

Imagine a very long wire (usually $4$ to $10$ meters) connected to a strong, primary "Driver Battery". This driver battery creates a steady, continuous drop in voltage along the entire length of the wire. Every centimeter of wire represents a tiny drop in voltage (this is called the **Potential Gradient**, $k$).

Now, you take the smaller battery you want to measure and connect it to this long wire through a galvanometer. 
You slide a jockey along the wire until you find a point where the voltage drop on the wire *exactly matches* the EMF of your smaller battery.

At this exact point, the two batteries are pushing against each other with identical force. It's a perfect tie. **No current flows.** The galvanometer reads zero.
Since no current flows from your small battery, there is no $Ir$ drop. You are measuring its pure, unadulterated EMF!

---

## 🔬 Stage 2: The Formula Lab

### 1. Potential Gradient ($k$)

The most important concept of a potentiometer. It is the voltage drop per unit length of the potentiometer wire.
$$k = \frac{V_{wire}}{L_{wire}}$$
Unit: $\text{V/m}$ or $\text{V/cm}$.

To find $V_{wire}$, you look at the primary circuit (the driver battery $E_p$, driver internal resistance $r_p$, rheostat $R_h$, and wire resistance $R_{wire}$):
Current in primary $I = \frac{E_p}{R_{wire} + R_h + r_p}$
$V_{wire} = I \times R_{wire}$

### 2. Application 1: Comparing EMFs of Two Cells

If cell $\varepsilon_1$ balances at length $l_1$, then $\varepsilon_1 = k l_1$.
If cell $\varepsilon_2$ balances at length $l_2$, then $\varepsilon_2 = k l_2$.

$$\frac{\varepsilon_1}{\varepsilon_2} = \frac{l_1}{l_2}$$

### 3. Application 2: Finding Internal Resistance of a Cell ⭐

1. Balance the cell's EMF (open circuit, key $K$ open). Let balance length be $l_1$.
   $\varepsilon = k l_1$
2. Connect a known resistance $R$ across the cell (close key $K$). The cell now gives current to $R$. Find the new balance point for the terminal voltage $V$. Let it be $l_2$.
   $V = k l_2$

Since $r = R \left( \frac{\varepsilon - V}{V} \right)$, substituting the lengths gives:
$$r = R \left( \frac{l_1 - l_2}{l_2} \right)$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Calculating Potential Gradient ($k$) ⭐

**Pattern:** "Given driver cell details and wire details, find $k$."

**Solved Example** 🟢

> A potentiometer wire of length $10\text{ m}$ and resistance $20\text{ } \Omega$ is connected in series with a $15\text{V}$ battery and an external resistance of $40\text{ } \Omega$. Find the potential gradient of the wire.

<details>
<summary><b>Solution</b></summary>

Total resistance of primary circuit $R_{total} = R_{wire} + R_{ext} = 20 + 40 = 60\text{ } \Omega$.
Current $I = V / R_{total} = 15 / 60 = 0.25\text{ A}$.
Voltage across the $10\text{m}$ wire $V_{wire} = I \times R_{wire} = 0.25 \times 20 = 5\text{ V}$.
Potential gradient $k = V_{wire} / L = 5\text{ V} / 10\text{ m} = \mathbf{0.5\text{ V/m}}$.
</details>

**Practice:**

1. 🟢 A potentiometer wire is $5\text{ m}$ long and has a resistance of $10\text{ } \Omega$. It is connected to a $2\text{V}$ accumulator of negligible internal resistance. Find $k$.

<details>
<summary><b>Answer</b></summary>

Since there's no other resistance, the entire $2\text{V}$ drops across the wire.
$k = 2\text{V} / 5\text{m} = \mathbf{0.4\text{ V/m}}$.
</details>

2. 🟡 A $10\text{ m}$ long potentiometer wire has a resistance of $10\text{ } \Omega$. It is connected in series with a battery of EMF $3\text{V}$ and internal resistance $1\text{ } \Omega$, and a resistance box. What resistance should be plugged in the box to get a potential gradient of $0.1\text{ V/m}$?<br>

<details>
<summary><b>Answer</b></summary>

Required $k = 0.1\text{ V/m}$. So $V_{wire} = k \times L = 0.1 \times 10 = 1\text{ V}$.
Current in wire $I = V_{wire} / R_{wire} = 1 / 10 = 0.1\text{ A}$.
Total current in circuit is $0.1\text{ A}$.
$I = E / (R_{wire} + r + R_{box}) \implies 0.1 = 3 / (10 + 1 + R_{box})$.
$11 + R_{box} = 3 / 0.1 = 30 \implies R_{box} = \mathbf{19\text{ } \Omega}$.
</details>

---

### Type 2: Comparing EMFs ⭐⭐

**Pattern:** "Two cells are balanced individually, or in series combinations."

**Solved Example** 🟡

> Two cells of EMFs $\varepsilon_1$ and $\varepsilon_2$ are connected in series aiding each other (positive to negative) and balanced on a potentiometer at $60\text{ cm}$. When they are connected opposing each other, the balance point is at $20\text{ cm}$. Compare their EMFs ($\varepsilon_1 / \varepsilon_2$).

<details>
<summary><b>Solution</b></summary>

Aiding (Sum): $\varepsilon_1 + \varepsilon_2 = k(60)$  --- (1)
Opposing (Difference): $\varepsilon_1 - \varepsilon_2 = k(20)$ --- (2)

Divide (1) by (2):
$\frac{\varepsilon_1 + \varepsilon_2}{\varepsilon_1 - \varepsilon_2} = \frac{60}{20} = \frac{3}{1}$
Cross multiply:
$1(\varepsilon_1 + \varepsilon_2) = 3(\varepsilon_1 - \varepsilon_2)$
$\varepsilon_1 + \varepsilon_2 = 3\varepsilon_1 - 3\varepsilon_2$
$4\varepsilon_2 = 2\varepsilon_1 \implies \frac{\varepsilon_1}{\varepsilon_2} = \frac{4}{2} = \mathbf{\frac{2}{1}}$.
</details>

**Practice:**

1. 🟢 Cell A balances at $40\text{ cm}$. Cell B balances at $60\text{ cm}$. Find the ratio of their EMFs.

<details>
<summary><b>Answer</b></summary>

$\varepsilon_A / \varepsilon_B = l_A / l_B = 40 / 60 = \mathbf{2/3}$.
</details>

2. 🟡 In a potentiometer experiment, a standard cell of EMF $1.08\text{V}$ balances at $54\text{ cm}$. What is the EMF of a cell that balances at $75\text{ cm}$?<br>

<details>
<summary><b>Answer</b></summary>

$\varepsilon / 1.08 = 75 / 54$.
$\varepsilon = 1.08 \times (75 / 54) = 1.08 \times (25 / 18) = 0.06 \times 25 = \mathbf{1.5\text{ V}}$.
</details>

---

### Type 3: Internal Resistance Calculation ⭐⭐⭐

**Pattern:** "Open circuit vs Closed circuit balancing lengths."

**Solved Example** 🔴

> A cell gives a balance point at $l_1 = 80\text{ cm}$ on a potentiometer. When a resistance of $2\text{ } \Omega$ is connected across the cell, the balance point shifts to $l_2 = 60\text{ cm}$. Find the internal resistance of the cell.

<details>
<summary><b>Solution</b></summary>

Use the formula directly:
$r = R \left( \frac{l_1 - l_2}{l_2} \right)$
$r = 2 \left( \frac{80 - 60}{60} \right) = 2 \left( \frac{20}{60} \right) = 2 \times \frac{1}{3} = \mathbf{0.67\text{ } \Omega}$.
</details>

**Practice:**

1. 🟡 A cell is balanced at $250\text{ cm}$. When a $5\text{ } \Omega$ resistor is shunted across it, the balance point becomes $200\text{ cm}$. What is the internal resistance?<br>

<details>
<summary><b>Answer</b></summary>

$r = 5 \times ((250 - 200) / 200) = 5 \times (50 / 200) = 5 \times (1/4) = \mathbf{1.25\text{ } \Omega}$.
</details>

2. 🔴 A cell balances at $100\text{ cm}$. When a $10\text{ } \Omega$ resistance is connected across it, balance point is $80\text{ cm}$. If the $10\text{ } \Omega$ resistance is replaced by a $20\text{ } \Omega$ resistance, where will the new balance point be?<br>

<details>
<summary><b>Answer</b></summary>

First, find $r$:
$r = 10 \times ((100 - 80) / 80) = 10 \times (20/80) = 10 \times 1/4 = 2.5\text{ } \Omega$.
Now, use the same formula with new $R = 20\text{ } \Omega$ to find new $l_2$:
$2.5 = 20 \times ((100 - l_2) / l_2)$
$2.5 / 20 = (100 - l_2) / l_2 \implies 1/8 = (100 - l_2) / l_2$
$l_2 = 800 - 8l_2 \implies 9l_2 = 800 \implies l_2 = 800 / 9 \approx \mathbf{88.89\text{ cm}}$.
*(Notice higher $R$ pulls the balance point closer to the open-circuit $l_1$).*
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 Why can't you balance a $5\text{V}$ battery using a potentiometer whose primary driver battery is only $2\text{V}$?<br>

<details>
<summary><b>Solution</b></summary>

The maximum voltage drop across the entire potentiometer wire is determined by the driver battery (minus any internal drops). If the driver is $2\text{V}$, the wire's potential ranges from $0\text{V}$ to maybe $1.9\text{V}$.
You cannot find a point on this wire that equals $5\text{V}$. The galvanometer will always deflect in one direction, and the balance point is "off the wire" (impossible to reach).
**Rule:** The EMF of the primary driver cell MUST be greater than the EMF of the cell being measured.
</details>

**Q2.** 🔴 ⭐ In a potentiometer experiment to determine internal resistance, what happens to the balancing length ($l_1$) if:
(i) The resistance of the primary circuit rheostat is increased?<br>
(ii) The cell being measured is replaced by another cell of higher EMF?<br>

<details>
<summary><b>Solution</b></summary>

(i) If rheostat resistance increases, primary current $I$ decreases. $V_{wire}$ decreases. Potential gradient $k$ decreases.
Since $\varepsilon = k l_1$ remains constant, if $k$ goes down, **$l_1$ must increase** to compensate. The balance point shifts to the right.
(ii) If a cell of higher EMF $\varepsilon$ is used, and $k$ is constant, then $l_1$ must increase ($\varepsilon \propto l_1$). The balance point **shifts to the right**.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 State the principle of a potentiometer. *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

When a constant current flows through a wire of uniform cross-section and composition, the potential drop across any length of the wire is directly proportional to that length ($V \propto l$).
</details>

**Q2.** 🟡 Why is a potentiometer preferred over a voltmeter for measuring the EMF of a cell?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

A voltmeter draws some current from the cell to deflect its pointer, so it measures the terminal voltage ($V = \varepsilon - Ir$), which is less than the true EMF.
A potentiometer works on the null deflection method. At the balance point, it draws exactly zero current from the cell, thus measuring its true, accurate EMF.
</details>

**Q3.** 🟡 How can the sensitivity of a potentiometer be increased?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Sensitivity is increased by decreasing the potential gradient ($k$). This can be done by:
1. Increasing the length of the potentiometer wire.
2. Decreasing the current in the primary circuit by increasing the resistance of the series rheostat.
*(A smaller $k$ means a larger shift in balancing length for a tiny change in voltage).*
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ A potentiometer wire has length $4\text{ m}$ and resistance $8\text{ } \Omega$. The resistance that must be connected in series with the wire and an accumulator of EMF $2\text{V}$, so as to get a potential gradient $1\text{ mV per cm}$ on the wire is:

(a) $32\text{ } \Omega$ &emsp; (b) $40\text{ } \Omega$ &emsp; (c) $44\text{ } \Omega$ &emsp; (d) $48\text{ } \Omega$

<details>
<summary><b>Answer</b></summary>

Required $k = 1\text{ mV/cm} = 10^{-3}\text{ V} / 10^{-2}\text{ m} = 0.1\text{ V/m}$.
Voltage across the $4\text{m}$ wire: $V_w = k \times L = 0.1 \times 4 = 0.4\text{ V}$.
Current in the wire $I = V_w / R_w = 0.4 / 8 = 0.05\text{ A}$.
This current is driven by the $2\text{V}$ accumulator through the total resistance $(R_w + R_{series})$.
$I = E / (R_w + R_{series}) \implies 0.05 = 2 / (8 + R_{series})$.
$8 + R_{series} = 2 / 0.05 = 40$.
$R_{series} = 40 - 8 = \mathbf{32\text{ } \Omega}$.

**Answer: (a)**
</details>

**Q2.** 🔴 In a potentiometer experiment, the balancing length with a cell is at length $240\text{ cm}$. On shunting the cell with a resistance of $2\text{ } \Omega$, the balancing length becomes $120\text{ cm}$. The internal resistance of the cell is:

(a) $1\text{ } \Omega$ &emsp; (b) $0.5\text{ } \Omega$ &emsp; (c) $4\text{ } \Omega$ &emsp; (d) $2\text{ } \Omega$

<details>
<summary><b>Answer</b></summary>

Use the internal resistance formula:
$r = R \left( \frac{l_1 - l_2}{l_2} \right)$
$r = 2 \times \left( \frac{240 - 120}{120} \right) = 2 \times \left( \frac{120}{120} \right) = 2 \times 1 = \mathbf{2\text{ } \Omega}$.

**Answer: (d)**
</details>

**Q3.** 🔴 ⭐ An ideal voltmeter $V$ is connected to a $2.0\text{V}$ potentiometer wire of length $1\text{m}$ as shown. What will the voltmeter read when the jockey is at the $30\text{ cm}$ mark?<br> (Assume driver battery is exactly $2.0\text{V}$ and has no internal resistance).

(a) $0.6\text{ V}$ &emsp; (b) $1.4\text{ V}$ &emsp; (c) $2.0\text{ V}$ &emsp; (d) $0\text{ V}$

<details>
<summary><b>Answer</b></summary>

Potential gradient $k = 2.0\text{V} / 100\text{cm} = 0.02\text{ V/cm}$.
If the voltmeter connects the zero mark to the $30\text{ cm}$ mark, it measures the voltage drop across that $30\text{ cm}$ segment.
$V = k \times l = 0.02 \times 30 = \mathbf{0.6\text{ V}}$.
*(This question is just checking if you know what a potentiometer wire actually does physically!)*

**Answer: (a)**
</details>

---

*Next: [Chapter 15 — NCERT Exemplar: Objective Questions →](./15_ncert_exemplar_mcq.md)*
