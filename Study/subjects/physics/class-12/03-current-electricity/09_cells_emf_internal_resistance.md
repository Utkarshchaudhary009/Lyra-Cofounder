# Chapter 9: Cells, EMF & Internal Resistance

> *NCERT Section 3.10*

---

## 🎯 Stage 1: The Core Idea

### The Water Pump Analogy

Think of a water circuit. The pipes are wires, the water is charge, and the flow is current.
What keeps the water moving? **A pump.**
An electrochemical cell (a battery) is exactly like a water pump. It doesn't *create* water (charge); it just takes water from a low-pressure area and pumps it up to a high-pressure area so it can flow down through the pipes again.

- **Electromotive Force (EMF, $\varepsilon$):** This is the "pump rating" printed on the box. It's the maximum pressure difference the pump can create when *nothing* is flowing. (e.g., $1.5\text{V}$ AA battery).
- **Internal Resistance ($r$):** The pump itself has some internal friction. When it starts pumping water rapidly, some pressure is lost inside the pump itself fighting this friction.
- **Terminal Voltage ($V$):** This is the *actual* pressure difference you get at the outlet of the pump when it's running. Because of the internal friction, the actual output pressure ($V$) is always a little less than the rated pressure ($\varepsilon$) when water is flowing.

### The Big Misconception about EMF

"Electromotive Force" is a terrible, historically inaccurate name. **It is NOT a force.** It does not have units of Newtons.
EMF is **Work done per unit charge** (Joules/Coulomb = Volts). It is a potential difference.

> **EMF** is the potential difference across the cell terminals when the cell is in an **open circuit** (no current is drawn).

---

## 🔬 Stage 2: The Formula Lab

### 1. The Core Circuit Equation

When a cell of EMF $\varepsilon$ and internal resistance $r$ is connected to an external resistor $R$:

$$I = \frac{\varepsilon}{R + r}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $I$ | Current in circuit | $\text{A}$ |
| $\varepsilon$ | Electromotive Force (EMF) | $\text{V}$ |
| $R$ | External Resistance | $\Omega$ |
| $r$ | Internal Resistance of the cell | $\Omega$ |

### 2. Terminal Voltage ($V$) Equations ⭐

This is the voltage you actually measure across the cell terminals (or across the external resistor $R$).
$V = IR$ (Ohm's law for the external circuit).

Depending on what the cell is doing, $V$ behaves differently:

| Scenario | What's happening? | Equation for $V$ | Relationship |
|----------|-------------------|------------------|--------------|
| **Discharging** | Cell is giving current to the circuit | $V = \varepsilon - Ir$ | $V < \varepsilon$ |
| **Charging** | Another bigger battery is pushing current *into* this cell | $V = \varepsilon + Ir$ | $V > \varepsilon$ |
| **Open Circuit** | Switch is open, $I = 0$ | $V = \varepsilon - (0)r = \varepsilon$ | $V = \varepsilon$ |
| **Short Circuit** | Terminals connected directly with a plain wire ($R=0$) | $V = I(0) = 0$ | $V = 0$ ($I = \varepsilon/r$) |

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Calculating $V, I, R, r$ (Discharging Cell) ⭐

**Pattern:** "A cell of EMF $\varepsilon$ and internal resistance $r$ is connected to $R$. Find current or terminal voltage."

**Solved Example** 🟢

> A battery of EMF $12\text{V}$ and internal resistance $2\text{ } \Omega$ is connected to a $4\text{ } \Omega$ resistor. Find the current and the terminal voltage.

<details>
<summary><b>Solution</b></summary>

Current $I = \frac{\varepsilon}{R + r} = \frac{12}{4 + 2} = \frac{12}{6} = \mathbf{2\text{ A}}$.
Terminal Voltage $V = IR = 2 \times 4 = \mathbf{8\text{ V}}$.
*(Alternatively: $V = \varepsilon - Ir = 12 - (2 \times 2) = 12 - 4 = \mathbf{8\text{ V}}$. Both formulas work!)*
</details>

**Practice:**

1. 🟢 A cell of EMF $2\text{V}$ and internal resistance $0.5\text{ } \Omega$ is connected to a $3.5\text{ } \Omega$ resistor. Find the current.

<details>
<summary><b>Answer</b></summary>

$I = \frac{\varepsilon}{R+r} = \frac{2}{3.5 + 0.5} = \frac{2}{4} = \mathbf{0.5\text{ A}}$.
</details>

2. 🟢 What is the terminal voltage of the cell in Q1 while the current is flowing?

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon - Ir = 2 - (0.5 \times 0.5) = 2 - 0.25 = \mathbf{1.75\text{ V}}$.
</details>

3. 🟡 A cell provides a current of $0.5\text{ A}$ through a $3\text{ } \Omega$ resistor and a current of $0.25\text{ A}$ through a $7\text{ } \Omega$ resistor. Find the EMF and internal resistance of the cell.

<details>
<summary><b>Answer</b></summary>

Case 1: $0.5 = \varepsilon / (3 + r) \implies \varepsilon = 1.5 + 0.5r$
Case 2: $0.25 = \varepsilon / (7 + r) \implies \varepsilon = 1.75 + 0.25r$
Equate the two: $1.5 + 0.5r = 1.75 + 0.25r \implies 0.25r = 0.25 \implies \mathbf{r = 1\text{ } \Omega}$.
Substitute $r$ into Case 1: $\varepsilon = 1.5 + 0.5(1) = \mathbf{2\text{ V}}$.
</details>

4. 🟡 A battery of EMF $6\text{V}$ and internal resistance $1\text{ } \Omega$ is short-circuited. What is the current? What is the terminal voltage?

<details>
<summary><b>Answer</b></summary>

Short-circuit means $R = 0$.
$I_{short} = \varepsilon / r = 6 / 1 = \mathbf{6\text{ A}}$.
Terminal voltage $V = I \times R = 6 \times 0 = \mathbf{0\text{ V}}$.
</details>

---

### Type 2: Charging a Cell ⭐⭐

**Pattern:** "A battery is being charged by a DC supply."

**Solved Example** 🟡

> A storage battery of EMF $8.0\text{V}$ and internal resistance $0.5\text{ } \Omega$ is being charged by a $120\text{V}$ DC supply using a series resistor of $15.5\text{ } \Omega$. What is the terminal voltage of the battery during charging?

<details>
<summary><b>Solution</b></summary>

When charging, the charger ($120\text{V}$) fights against the battery ($8\text{V}$). The net driving EMF is $120 - 8 = 112\text{V}$.
Total resistance in circuit = $R_{series} + r = 15.5 + 0.5 = 16\text{ } \Omega$.
Charging Current $I = \frac{V_{net}}{R_{total}} = \frac{112}{16} = \mathbf{7\text{ A}}$.

Terminal voltage of the battery **during charging**:
$V = \varepsilon + Ir = 8.0 + (7 \times 0.5) = 8.0 + 3.5 = \mathbf{11.5\text{ V}}$.
*(Notice $V > \varepsilon$ here!)*
</details>

**Practice:**

1. 🟡 A $12\text{V}$ car battery with internal resistance $0.4\text{ } \Omega$ is being charged with a current of $5\text{ A}$. What is the potential difference across its terminals?

<details>
<summary><b>Answer</b></summary>

Since it's charging, $V = \varepsilon + Ir$.
$V = 12 + (5 \times 0.4) = 12 + 2 = \mathbf{14\text{ V}}$.
</details>

2. 🟡 What is the purpose of having a series resistor when charging a battery from a high voltage DC supply?

<details>
<summary><b>Answer</b></summary>

To limit the charging current. Without the series resistor, the current $I = (120 - 8)/0.5 = 224\text{ A}$, which would instantly overheat and destroy the battery.
</details>

---

### Type 3: Graph of $V$ vs $I$ for a Cell ⭐⭐⭐

**Pattern:** "A graph of terminal voltage vs current is given. Extract $\varepsilon$ and $r$."

**Solved Example** 🟡

> The $V-I$ graph for a cell is a straight line. The y-intercept is $1.5\text{V}$ and the x-intercept is $3.0\text{A}$. Find the EMF and internal resistance.

<details>
<summary><b>Solution</b></summary>

The equation for discharging is $V = -rI + \varepsilon$. This is a straight line ($y = mx + c$).
- **y-intercept ($c$)** is where $I=0$. This is the open-circuit voltage, which is the **EMF**.
  $\varepsilon = \mathbf{1.5\text{ V}}$.
- **x-intercept** is where $V=0$. This is the short-circuit current, $I = \varepsilon/r$.
  $3.0 = 1.5 / r \implies r = 1.5 / 3.0 = \mathbf{0.5\text{ } \Omega}$.
- *(Alternatively, the slope of the line is $-r$)*.
</details>

**Practice:**

1. 🟢 From a $V-I$ graph, the maximum voltage is $2.0\text{V}$. The maximum current is $10\text{A}$. Find $r$.

<details>
<summary><b>Answer</b></summary>

$\varepsilon = 2.0\text{V}$. $I_{max} = 10\text{A}$.
$r = \varepsilon / I_{max} = 2.0 / 10 = \mathbf{0.2\text{ } \Omega}$.
</details>

2. 🟡 Plot a graph showing variation of terminal voltage ($V$) with external resistance ($R$).

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon - Ir = \varepsilon - \left(\frac{\varepsilon}{R+r}\right)r = \varepsilon \left(1 - \frac{r}{R+r}\right) = \varepsilon \left(\frac{R}{R+r}\right)$.
When $R=0$, $V=0$.
As $R \rightarrow \infty$, $V \rightarrow \varepsilon$.
The graph is a curve starting from the origin and asymptotically approaching the horizontal line $V = \varepsilon$.
</details>

---

### Type 4: Maximum Power Theorem

**Pattern:** "Find the condition or value for maximum power dissipated in the external resistor."

**Solved Example** 🔴

> A cell of EMF $10\text{V}$ and internal resistance $3\text{ } \Omega$ is connected to a variable resistor $R$. For what value of $R$ will the power dissipated in it be maximum? What is this maximum power?

<details>
<summary><b>Solution</b></summary>

Maximum Power Theorem: Power transferred to the external load is maximum when **external resistance = internal resistance**.
So, $R = r = \mathbf{3\text{ } \Omega}$.

Maximum power $P_{max} = \frac{\varepsilon^2}{4r} = \frac{10^2}{4 \times 3} = \frac{100}{12} = \mathbf{8.33\text{ W}}$.
</details>

**Practice:**

1. 🟡 A cell ($\varepsilon=6\text{V}$, $r=2\text{ }\Omega$) is connected to $R$. Plot a graph of Power $P$ vs $R$. At what $R$ does the peak occur?

<details>
<summary><b>Answer</b></summary>

The graph starts at 0, rises to a peak, and then slowly falls towards 0 as $R \rightarrow \infty$.
The peak occurs precisely at $R = r = \mathbf{2\text{ }\Omega}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A battery of EMF $10\text{V}$ and internal resistance $3\text{ } \Omega$ is connected to a resistor. If the current in the circuit is $0.5\text{ A}$, what is the resistance of the resistor? What is the terminal voltage of the battery when the circuit is closed?

<details>
<summary><b>Solution</b></summary>

$I = \varepsilon / (R + r)$
$0.5 = 10 / (R + 3)$
$R + 3 = 10 / 0.5 = 20 \implies R = \mathbf{17\text{ } \Omega}$.

Terminal voltage $V = IR = 0.5 \times 17 = \mathbf{8.5\text{ V}}$.
*(Check: $V = \varepsilon - Ir = 10 - (0.5 \times 3) = 10 - 1.5 = 8.5\text{V}$. Matches!)*
</details>

**Q2.** 🔴 ⭐ An electric motor, which has an internal resistance of $1\text{ } \Omega$, is connected to a $24\text{V}$ battery with $1\text{ } \Omega$ internal resistance. When the motor is running, it draws a current of $2\text{ A}$. Find the "back EMF" generated by the running motor.

<details>
<summary><b>Solution</b></summary>

A running motor acts like a battery pushing back (back EMF, let's call it $E_{back}$).
The circuit is basically a $24\text{V}$ battery pushing against $E_{back}$.
Net EMF = $24 - E_{back}$.
Total resistance = $r_{battery} + r_{motor} = 1 + 1 = 2\text{ } \Omega$.
Current $I = V_{net} / R_{total}$
$2 = (24 - E_{back}) / 2 \implies 4 = 24 - E_{back} \implies E_{back} = \mathbf{20\text{ V}}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Define internal resistance of a cell. On what factors does it depend? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Internal resistance** is the resistance offered by the electrolyte and electrodes of a cell to the flow of current within it.
It depends on:
1. Distance between electrodes (larger distance $\implies$ higher $r$).
2. Area of electrodes immersed in electrolyte (larger area $\implies$ lower $r$).
3. Concentration of electrolyte (higher concentration $\implies$ higher $r$).
4. Temperature (higher temp $\implies$ lower $r$).
</details>

**Q2.** 🟡 State the condition under which the terminal potential difference of a cell is (i) greater than its EMF, (ii) equal to its EMF. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

(i) Terminal voltage is greater than EMF ($V > \varepsilon$) when the cell is **being charged** by an external source.
(ii) Terminal voltage is equal to EMF ($V = \varepsilon$) when the cell is in an **open circuit** (no current is drawn, $I=0$).
</details>

**Q3.** 🟡 A primary cell of EMF $1.5\text{V}$, when short-circuited, gives a current of $3\text{A}$. Calculate the internal resistance of the cell. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

When short-circuited, external resistance $R = 0$.
Current $I = \varepsilon / r$
$3 = 1.5 / r \implies r = 1.5 / 3 = \mathbf{0.5\text{ } \Omega}$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ A cell of internal resistance $r$ drives current through an external resistance $R$. The power delivered by the cell to the external resistance will be maximum when:

(a) $R = 0$ &emsp; (b) $R = r$ &emsp; (c) $R = 2r$ &emsp; (d) $R = 1000 r$

<details>
<summary><b>Answer</b></summary>

This is the direct statement of the Maximum Power Transfer Theorem. Power is maximum when external resistance equals internal resistance.

**Answer: (b)**
</details>

**Q2.** 🔴 A cell having an EMF $\varepsilon$ and internal resistance $r$ is connected across a variable external resistance $R$. As the resistance $R$ is increased, the plot of potential difference $V$ across $R$ is given by:

(a) A straight line passing through origin
(b) A straight line with negative slope
(c) A curve starting from origin and approaching $\varepsilon$ asymptotically
(d) A curve starting from $\varepsilon$ and decaying to zero

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon \left(\frac{R}{R+r}\right)$
When $R \rightarrow 0$, $V \rightarrow 0$.
When $R \rightarrow \infty$, the term $\frac{R}{R+r} \approx \frac{R}{R} = 1$, so $V \rightarrow \varepsilon$.
The graph starts at 0 and curves upwards, flattening out at $V = \varepsilon$.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ In a circuit, a cell of EMF $\varepsilon$ and internal resistance $r$ is connected to an external resistance $R$. A voltmeter (which is non-ideal and has finite resistance $R_v$) is connected across the cell. Which of the following statements is true?

(a) The voltmeter reads exactly $\varepsilon$.
(b) The voltmeter reads slightly less than $\varepsilon$ even if $R$ is disconnected.
(c) The voltmeter reads exactly the voltage across $R$.
(d) Both (b) and (c) are true.

<details>
<summary><b>Answer</b></summary>

A real voltmeter has resistance $R_v$. Even if the main external circuit $R$ is disconnected, the voltmeter itself completes a circuit and draws a tiny current $I = \varepsilon / (r + R_v)$.
Therefore, the voltage it measures is $V = \varepsilon - I r$, which is slightly less than $\varepsilon$. So (b) is true.
Since the voltmeter is connected in parallel with the cell and the resistor $R$, it measures the potential difference between those two nodes, which is exactly the terminal voltage $V$ (and the voltage across $R$). So (c) is also true.

**Answer: (d)**
</details>

---

*Next: [Chapter 10 — Cells in Series and Parallel (Grouping of Cells) →](./10_grouping_of_cells.md)*
