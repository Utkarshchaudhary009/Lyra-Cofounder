# Chapter 9: Cells, EMF & Internal Resistance

> *NCERT Section 3.10*

---

## 🎯 Stage 1: The Core Idea

### The Water Pump Analogy

Think of a water circuit. The pipes are wires, the water is charge, and the flow is current.
What keeps the water moving?<br> **A pump.**
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

| Scenario | What's happening?<br> | Equation for $V$ | Relationship |
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

2. 🟢 What is the terminal voltage of the cell in Q1 while the current is flowing?<br>

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

4. 🟡 A battery of EMF $6\text{V}$ and internal resistance $1\text{ } \Omega$ is short-circuited. What is the current?<br> What is the terminal voltage?<br>

<details>
<summary><b>Answer</b></summary>

Short-circuit means $R = 0$.
$I_{short} = \varepsilon / r = 6 / 1 = \mathbf{6\text{ A}}$.
Terminal voltage $V = I \times R = 6 \times 0 = \mathbf{0\text{ V}}$.
</details>

5. 🟢 A cell of EMF $1.5\text{ V}$ and internal resistance $0.2\text{ }\Omega$ is connected to a resistor of $2.8\text{ }\Omega$. Find the current in the circuit.

<details>
<summary><b>Answer</b></summary>

$I = \frac{\varepsilon}{R+r} = \frac{1.5}{2.8 + 0.2} = \frac{1.5}{3.0} = \mathbf{0.5\text{ A}}$.
</details>

6. 🟡 A high-resistance voltmeter reads $2.2\text{ V}$ when connected across a cell on open circuit. When the cell is connected to a $5\text{ }\Omega$ resistor, the voltmeter reading drops to $1.8\text{ V}$. Find the internal resistance of the cell.

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon - I r \implies I = \frac{V}{R} = \frac{1.8}{5} = 0.36\text{ A}$.
Then $r = \frac{\varepsilon - V}{I} = \frac{2.2 - 1.8}{0.36} = \frac{0.4}{0.36} = \mathbf{1.11\text{ }\Omega}$.
</details>

7. 🟡 ⭐ A battery of EMF $\varepsilon$ and internal resistance $r$ is connected to an external resistor $R$. If the terminal voltage is $80\%$ of the EMF, find the ratio $R/r$.

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon \frac{R}{R+r} \implies 0.8\varepsilon = \varepsilon \frac{R}{R+r} \implies 0.8(R+r) = R \implies 0.8r = 0.2R \implies \frac{R}{r} = \mathbf{4}$.
</details>

8. 🟢 A battery has an EMF of $15.0\text{ V}$ and a terminal voltage of $11.6\text{ V}$ when supplying $20.0\text{ A}$ to start a car. What is its internal resistance?

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon - Ir \implies 11.6 = 15.0 - 20.0 r \implies 20.0r = 3.4 \implies r = \frac{3.4}{20.0} = \mathbf{0.17\text{ }\Omega}$.
</details>

9. 🟡 A cell of EMF $1.8\text{ V}$ and internal resistance $r$ is connected to a resistor of $10\text{ }\Omega$. If the current in the circuit is $0.15\text{ A}$, find the internal resistance of the cell and its terminal voltage.

<details>
<summary><b>Answer</b></summary>

$I = \frac{\varepsilon}{R+r} \implies 0.15 = \frac{1.8}{10+r} \implies 10+r = 12 \implies r = \mathbf{2\text{ }\Omega}$.
Terminal voltage $V = I R = 0.15 \times 10 = \mathbf{1.5\text{ V}}$.
</details>

10. 🔴 A cell of EMF $E$ and internal resistance $r$ is connected to a variable external resistance $R$. Under what conditions does the terminal voltage of the cell become zero, and what is the corresponding current?

<details>
<summary><b>Answer</b></summary>

The terminal voltage $V = I R$. It becomes zero when $R = 0$ (short circuit condition). The corresponding current is $I_{short} = \frac{E}{r}$. Thus, $V = \mathbf{0\text{ V}}$ and $I = \mathbf{\frac{E}{r}}$.
</details>

---

### Type 2: Charging a Cell ⭐⭐

**Pattern:** "A battery is being charged by a DC supply."

**Solved Example** 🟡

> A storage battery of EMF $8.0\text{V}$ and internal resistance $0.5\text{ } \Omega$ is being charged by a $120\text{V}$ DC supply using a series resistor of $15.5\text{ } \Omega$. What is the terminal voltage of the battery during charging?<br>

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

1. 🟡 A $12\text{V}$ car battery with internal resistance $0.4\text{ } \Omega$ is being charged with a current of $5\text{ A}$. What is the potential difference across its terminals?<br>

<details>
<summary><b>Answer</b></summary>

Since it's charging, $V = \varepsilon + Ir$.
$V = 12 + (5 \times 0.4) = 12 + 2 = \mathbf{14\text{ V}}$.
</details>

2. 🟡 What is the purpose of having a series resistor when charging a battery from a high voltage DC supply?<br>

<details>
<summary><b>Answer</b></summary>

To limit the charging current. Without the series resistor, the current $I = (120 - 8)/0.5 = 224\text{ A}$, which would instantly overheat and destroy the battery.
</details>

3. 🟡 A backup power supply with an EMF of $24\text{ V}$ and internal resistance $0.8\text{ }\Omega$ is being charged by a DC generator. The charging current is $10\text{ A}$. What is the potential difference across its terminals during this time?

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon + Ir = 24 + (10 \times 0.8) = 24 + 8 = \mathbf{32\text{ V}}$.
</details>

4. 🟡 ⭐ A battery of EMF $6\text{ V}$ and internal resistance $0.5\text{ }\Omega$ is charged using a $24\text{ V}$ supply. If the charging current must be limited to $3\text{ A}$, find the value of the series resistor required.

<details>
<summary><b>Answer</b></summary>

Net EMF in the circuit = $V_{supply} - \varepsilon = 24 - 6 = 18\text{ V}$.
Total resistance in the circuit = $R_{series} + r = R_{series} + 0.5$.
Current $I = \frac{V_{net}}{R_{series} + r} \implies 3 = \frac{18}{R_{series} + 0.5} \implies R_{series} + 0.5 = 6 \implies R_{series} = \mathbf{5.5\text{ }\Omega}$.
</details>

5. 🟢 A storage cell of EMF $2.0\text{ V}$ and internal resistance $0.1\text{ }\Omega$ is being charged by a $12\text{ V}$ DC source. If a series resistor of $4.9\text{ }\Omega$ is used, find the charging current.

<details>
<summary><b>Answer</b></summary>

Net EMF = $12 - 2 = 10\text{ V}$.
Total resistance = $R_{series} + r = 4.9 + 0.1 = 5.0\text{ }\Omega$.
Current $I = \frac{10}{5.0} = \mathbf{2\text{ A}}$.
</details>

6. 🔴 A battery of EMF $\varepsilon$ and internal resistance $r$ is charged by a DC supply of voltage $V_{supply}$ through a series resistance $R$. Write the expression for the rate of chemical energy stored in the battery, the rate of energy dissipation as heat inside the battery, and the total power supplied to the battery.

<details>
<summary><b>Answer</b></summary>

During charging, the current enters the positive terminal.
The total power supplied to the battery is $P_{in} = V I$, where $V = \varepsilon + I r$ is the terminal voltage.
Rate of chemical energy stored = $\mathbf{\varepsilon I}$.
Rate of energy dissipation as heat inside the battery = $\mathbf{I^2 r}$.
Total power supplied to the battery = $V I = \mathbf{\varepsilon I + I^2 r}$.
</details>

7. 🟡 A car battery ($\varepsilon = 12\text{ V}$, $r = 0.1\text{ }\Omega$) is connected to a battery charger. The terminal voltage of the battery is measured to be $14.5\text{ V}$. Determine the charging current and the power dissipated inside the battery.

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon + I r \implies 14.5 = 12 + 0.1 I \implies 0.1 I = 2.5 \implies I = \mathbf{25\text{ A}}$.
Power dissipated as heat inside the battery = $I^2 r = (25)^2 \times 0.1 = \mathbf{62.5\text{ W}}$.
</details>

8. 🟡 A battery of EMF $12\text{ V}$ and internal resistance $0.5\text{ }\Omega$ is being charged by a $120\text{ V}$ source. If the terminal voltage of the battery during charging is $15\text{ V}$, find the charging current and the external series resistance.

<details>
<summary><b>Answer</b></summary>

$V = \varepsilon + Ir \implies 15 = 12 + 0.5 I \implies 0.5 I = 3 \implies I = \mathbf{6\text{ A}}$.
Net voltage of the charging circuit = $120 - 12 = 108\text{ V}$.
Total resistance = $\frac{108}{6} = 18\text{ }\Omega$.
External series resistance $R_{series} = R_{total} - r = 18 - 0.5 = \mathbf{17.5\text{ }\Omega}$.
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

3. 🟢 In a $V-I$ graph for a discharging cell, the y-intercept is $6\text{ V}$ and the slope is $-0.5\text{ V/A}$. Find the EMF and internal resistance of the cell.

<details>
<summary><b>Answer</b></summary>

The equation is $V = \varepsilon - I r$.
Comparing with $y = mx + c$, the y-intercept is EMF, so $\varepsilon = \mathbf{6\text{ V}}$.
The magnitude of the slope is $r$, so $r = \mathbf{0.5\text{ }\Omega}$.
</details>

4. 🟡 For a cell, the terminal potential difference $V$ vs current $I$ is plotted. The graph is a straight line starting at $(0, 1.5\text{ V})$ and ending at $(3\text{ A}, 0)$. What is the maximum current that can be drawn from the cell, and what is its internal resistance?

<details>
<summary><b>Answer</b></summary>

The maximum current is drawn when the terminals are short-circuited ($V=0$), which is the x-intercept: $I_{max} = \mathbf{3\text{ A}}$.
The y-intercept is EMF: $\varepsilon = 1.5\text{ V}$.
Internal resistance $r = \frac{\varepsilon}{I_{max}} = \frac{1.5}{3} = \mathbf{0.5\text{ }\Omega}$.
</details>

5. 🟡 ⭐ Draw a graph showing the variation of terminal potential difference $V$ of a cell as a function of the current $I$ drawn from it. Mark the points representing: (i) open circuit state, (ii) short circuit state.

<details>
<summary><b>Answer</b></summary>

The graph of $V$ vs $I$ is a straight line with a negative slope, described by $V = \varepsilon - Ir$.
(i) **Open circuit state:** Represented by the y-intercept where $I = 0$ and $V = \mathbf{\varepsilon}$.
(ii) **Short circuit state:** Represented by the x-intercept where $V = 0$ and $I = \mathbf{\frac{\varepsilon}{r}}$.
</details>

6. 🟡 A cell of EMF $E$ and internal resistance $r$ is connected to a variable resistor $R$. Plot a graph showing the variation of current $I$ as a function of $R$.

<details>
<summary><b>Answer</b></summary>

The current is given by $I = \frac{E}{R+r}$.
When $R = 0$, $I = \frac{E}{r}$ (maximum current).
As $R \rightarrow \infty$, $I \rightarrow 0$.
The graph is a rectangular hyperbola shifted along the R-axis, starting at $(0, \frac{E}{r})$ and asymptotically approaching $I = 0$ as $R \rightarrow \infty$.
</details>

7. 🔴 A student plots terminal voltage $V$ against current $I$ for two different cells A and B. Cell A has y-intercept $2\text{ V}$ and x-intercept $1\text{ A}$. Cell B has y-intercept $1.5\text{ V}$ and x-intercept $2\text{ A}$. Which cell has larger internal resistance, and by what factor?

<details>
<summary><b>Answer</b></summary>

For Cell A: $\varepsilon_A = 2\text{ V}$, $I_{short, A} = 1\text{ A} \implies r_A = \frac{2}{1} = 2\text{ }\Omega$.
For Cell B: $\varepsilon_B = 1.5\text{ V}$, $I_{short, B} = 2\text{ A} \implies r_B = \frac{1.5}{2} = 0.75\text{ }\Omega$.
Thus, Cell A has larger internal resistance, and the ratio $\frac{r_A}{r_B} = \frac{2}{0.75} = \mathbf{2.67}$ times larger.
</details>

8. 🟡 For a cell of EMF $E$ and internal resistance $r$, the potential difference across its terminals is $V$. If a graph is plotted between $V$ and external resistance $R$, find the value of $R$ at which $V = 0.5 E$.

<details>
<summary><b>Answer</b></summary>

We know that $V = E \frac{R}{R+r}$.
If $V = 0.5 E$, then $0.5 E = E \frac{R}{R+r} \implies 0.5 = \frac{R}{R+r} \implies 0.5R + 0.5r = R \implies 0.5r = 0.5R \implies R = \mathbf{r}$.
So, the terminal voltage is half of the EMF when the external resistance equals the internal resistance.
</details>

---

### Type 4: Maximum Power Theorem

**Pattern:** "Find the condition or value for maximum power dissipated in the external resistor."

**Solved Example** 🔴

> A cell of EMF $10\text{V}$ and internal resistance $3\text{ } \Omega$ is connected to a variable resistor $R$. For what value of $R$ will the power dissipated in it be maximum?<br> What is this maximum power?<br>

<details>
<summary><b>Solution</b></summary>

Maximum Power Theorem: Power transferred to the external load is maximum when **external resistance = internal resistance**.
So, $R = r = \mathbf{3\text{ } \Omega}$.

Maximum power $P_{max} = \frac{\varepsilon^2}{4r} = \frac{10^2}{4 \times 3} = \frac{100}{12} = \mathbf{8.33\text{ W}}$.
</details>

**Practice:**

1. 🟡 A cell ($\varepsilon=6\text{V}$, $r=2\text{ }\Omega$) is connected to $R$. Plot a graph of Power $P$ vs $R$. At what $R$ does the peak occur?<br>

<details>
<summary><b>Answer</b></summary>

The graph starts at 0, rises to a peak, and then slowly falls towards 0 as $R \rightarrow \infty$.
The peak occurs precisely at $R = r = \mathbf{2\text{ }\Omega}$.
</details>

2. 🟢 A battery has an EMF of $12\text{ V}$ and an internal resistance of $1.5\text{ }\Omega$. What is the maximum power it can deliver to an external resistor?

<details>
<summary><b>Answer</b></summary>

Maximum power is delivered when $R = r = 1.5\text{ }\Omega$.
$P_{max} = \frac{\varepsilon^2}{4r} = \frac{12^2}{4 \times 1.5} = \frac{144}{6} = \mathbf{24\text{ W}}$.
</details>

3. 🟡 ⭐ A cell of EMF $E$ and internal resistance $r$ is connected to a variable external resistor $R$. Show that the efficiency of the cell at maximum power delivery is $50\%$.

<details>
<summary><b>Answer</b></summary>

The total power generated by the cell is $P_{total} = E I$.
The power delivered to the external resistor is $P_{out} = I^2 R$.
At maximum power transfer, $R = r$, which means $I = \frac{E}{R+r} = \frac{E}{2R}$.
So, $P_{total} = E \left(\frac{E}{2R}\right) = \frac{E^2}{2R}$.
And $P_{out} = \left(\frac{E}{2R}\right)^2 R = \frac{E^2}{4R}$.
Efficiency $\eta = \frac{P_{out}}{P_{total}} = \frac{E^2 / 4R}{E^2 / 2R} = 0.5 = \mathbf{50\%}$.
</details>

4. 🟡 Two resistors of $2\text{ }\Omega$ and $8\text{ }\Omega$ are connected one by one across a cell. If the power dissipated in both cases is the same, find the internal resistance of the cell.

<details>
<summary><b>Answer</b></summary>

The power dissipated in external resistor $R$ is $P = I^2 R = \left(\frac{E}{R+r}\right)^2 R$.
Given $P(R_1) = P(R_2)$, where $R_1 = 2\text{ }\Omega$ and $R_2 = 8\text{ }\Omega$:
$\frac{E^2 R_1}{(R_1+r)^2} = \frac{E^2 R_2}{(R_2+r)^2} \implies \frac{R_1}{(R_1+r)^2} = \frac{R_2}{(R_2+r)^2}$.
Taking the square root on both sides: $\frac{\sqrt{R_1}}{R_1+r} = \frac{\sqrt{R_2}}{R_2+r} \implies \sqrt{R_1}(R_2+r) = \sqrt{R_2}(R_1+r)$.
$r(\sqrt{R_2} - \sqrt{R_1}) = \sqrt{R_1}R_2 - \sqrt{R_2}R_1 = \sqrt{R_1}\sqrt{R_2}(\sqrt{R_2} - \sqrt{R_1})$.
Since $R_1 \neq R_2$, we divide by $(\sqrt{R_2} - \sqrt{R_1})$:
$r = \sqrt{R_1 R_2} = \sqrt{2 \times 8} = \sqrt{16} = \mathbf{4\text{ }\Omega}$.
</details>

5. 🟡 A cell of EMF $6\text{ V}$ and internal resistance $1\text{ }\Omega$ delivers power to an external resistance $R$. If the power delivered is $8\text{ W}$, find the two possible values of $R$.

<details>
<summary><b>Answer</b></summary>

Power $P = \frac{E^2 R}{(R+r)^2} \implies 8 = \frac{6^2 R}{(R+1)^2} \implies 8(R+1)^2 = 36R \implies 2(R^2 + 2R + 1) = 9R \implies 2R^2 + 4R + 2 = 9R \implies 2R^2 - 5R + 2 = 0$.
Solving the quadratic equation: $(2R - 1)(R - 2) = 0$.
Thus, the two possible values of $R$ are $\mathbf{0.5\text{ }\Omega}$ and $\mathbf{2\text{ }\Omega}$.
</details>

6. 🔴 A source of EMF $E$ and internal resistance $r$ is connected to a load $R$. If the power transfer efficiency is to be $80\%$, find the ratio of load resistance $R$ to internal resistance $r$.

<details>
<summary><b>Answer</b></summary>

Efficiency $\eta = \frac{P_{out}}{P_{total}} = \frac{I^2 R}{I^2(R+r)} = \frac{R}{R+r}$.
Given $\eta = 0.8$:
$\frac{R}{R+r} = 0.8 \implies R = 0.8R + 0.8r \implies 0.2R = 0.8r \implies \frac{R}{r} = \mathbf{4}$.
</details>

7. 🟡 A battery of EMF $10\text{ V}$ and internal resistance $2\text{ }\Omega$ is connected to a variable load resistor. If the maximum power is transferred to the load, calculate the terminal potential difference and the rate of energy loss inside the battery.

<details>
<summary><b>Answer</b></summary>

For maximum power transfer, $R = r = 2\text{ }\Omega$.
The current is $I = \frac{E}{R+r} = \frac{10}{2+2} = 2.5\text{ A}$.
The terminal voltage is $V = E - Ir = 10 - 2.5 \times 2 = \mathbf{5\text{ V}}$ (which is $E/2$).
The rate of energy loss as heat inside the battery is $P_{loss} = I^2 r = (2.5)^2 \times 2 = 6.25 \times 2 = \mathbf{12.5\text{ W}}$.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1.** The EMF of a cell is defined as the potential difference between its terminals when:
(a) the cell is short-circuited
(b) the cell is discharging through an external resistance
(c) the cell is charging from an external source
(d) no current is drawn from the cell

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

By definition, Electromotive Force (EMF) is the terminal potential difference when the cell is in an open circuit (no current is drawn, $I=0$).
</details>

**Q2.** A cell of EMF $E$ and internal resistance $r$ is connected to an external resistance $R$. The terminal voltage of the cell is $V$. If a wire of zero resistance is connected directly across the terminals of the cell:
(a) $V$ becomes $E$
(b) $V$ becomes $0$
(c) the current in the cell becomes zero
(d) the power dissipated in the external circuit becomes maximum

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Connecting a zero resistance wire directly across the terminals is a short-circuit ($R=0$). Thus, $V = I R = I(0) = \mathbf{0\text{ V}}$. The current is maximum ($I = E/r$), and all power is dissipated internally as heat.
</details>

**Q3.** When a battery of EMF $E$ and internal resistance $r$ is being charged by a charger with constant current $I$:
(a) the terminal voltage of the battery is $E - Ir$
(b) the terminal voltage of the battery is $E + Ir$
(c) the chemical energy of the battery decreases
(d) no energy is lost inside the battery

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

During charging, current is forced into the positive terminal of the battery. The terminal voltage is given by $V = E + Ir$, which is greater than the EMF $E$.
</details>

**Q4.** A cell of EMF $E$ and internal resistance $r$ is connected across a variable external resistance $R$. If $R$ is decreased to zero, the current in the circuit:
(a) becomes zero
(b) becomes infinite
(c) becomes $E/r$
(d) remains constant

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Current is given by $I = \frac{E}{R+r}$. As $R \rightarrow 0$ (short circuit), the current reaches its maximum possible value, $I_{max} = \mathbf{E/r}$.
</details>

**Q5.** Which of the following factors does NOT increase the internal resistance of a chemical cell?
(a) Increasing the distance between the electrodes
(b) Decreasing the area of electrodes immersed in the electrolyte
(c) Decreasing the concentration of the electrolyte at very low concentrations
(d) Increasing the temperature of the electrolyte

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

As temperature increases, the viscosity of the electrolyte decreases and ionic mobility increases. Therefore, the internal resistance of the cell *decreases* with an increase in temperature.
</details>

**Q6.** The terminal potential difference of a cell is greater than its EMF when:
(a) the cell is in an open circuit
(b) the cell is discharging
(c) the cell is being charged
(d) the cell is short-circuited

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

When charging, the terminal voltage is $V = E + Ir > E$. For all other active cases, $V \le E$.
</details>

**Q7.** **Statement I:** The EMF of a cell is always greater than its terminal potential difference.
**Statement II:** During discharging of a cell, the current flows inside the cell from its negative electrode to its positive electrode.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

Statement I is false because during charging, the terminal potential difference ($V = E + Ir$) is greater than the EMF ($E$). Statement II is true: inside the discharging cell, current flows from the negative terminal to the positive terminal (completing the loop as current flows from positive to negative in the external circuit).
</details>

**Q8.** **Statement I:** A student connects a real voltmeter across the terminals of a cell in an open circuit, and it reads exactly the EMF of the cell.
**Statement II:** A real voltmeter has a finite resistance and therefore draws a small current, making the measured terminal voltage slightly less than the EMF.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is false, but Statement II is true.
(d) Statement I is true, but Statement II is false.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Statement I is false. Since a real voltmeter has finite resistance $R_v$, it draws a current $I = E/(R_v + r)$ when connected. Thus, the reading is $V = E - Ir < E$. Statement II is true and explains why Statement I is false.
</details>

**Q9.** **Statement I:** When an external resistance $R$ connected across a cell of internal resistance $r$ is equal to $r$, the power transferred to the external circuit is maximum.
**Statement II:** Under the maximum power transfer condition, the efficiency of the cell is only $50\%$.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Both statements are true. Statement I is the Maximum Power Transfer Theorem. Statement II is also true because when $R=r$, half of the total power is dissipated inside the cell as heat, and half is delivered to the load. However, Statement II is not the explanation of Statement I (Statement I is derived by maximizing the power function $P = I^2 R$ with respect to $R$).
</details>

**Q10.** A cell of EMF $E$ and internal resistance $r$ is connected to a variable external resistance $R$. The maximum power dissipated in the external circuit is:
(a) $E^2/r$
(b) $E^2/(2r)$
(c) $E^2/(4r)$
(d) $4E^2/r$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Maximum power occurs when $R=r$. The current is $I = E/(2r)$. The power dissipated is $P_{max} = I^2 R = (E/2r)^2 r = \mathbf{E^2/(4r)}$.
</details>

**Q11.** For a cell of EMF $E$ and internal resistance $r$, the terminal voltage is $V$ when a current $I$ is drawn. The graph of $V$ versus $I$ is a straight line. The slope of this line represents:
(a) the EMF $E$
(b) the negative of the internal resistance $-r$
(c) the external resistance $R$
(d) the conductance of the cell

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

The equation for the terminal voltage is $V = -r I + E$. This is of the form $y = mx + c$, where the slope $m = \mathbf{-r}$.
</details>

**Q12.** A battery consists of a cell of EMF $2.0\text{ V}$ and internal resistance $0.5\text{ }\Omega$. If this battery is short-circuited, the rate of heat generation inside the battery is:
(a) $2\text{ W}$
(b) $4\text{ W}$
(c) $8\text{ W}$
(d) $0\text{ W}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Short-circuit current is $I_{short} = E/r = 2.0 / 0.5 = 4\text{ A}$. The rate of heat generation inside the battery is $P = I^2 r = 4^2 \times 0.5 = 16 \times 0.5 = \mathbf{8\text{ W}}$.
</details>

**Q13.** Two identical cells, each of EMF $E$ and internal resistance $r$, are connected in parallel. If they are connected to an external resistance $R = r$, the current through the resistor $R$ is:
(a) $E/r$
(b) $2E/(3r)$
(c) $E/(2r)$
(d) $4E/(3r)$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

For parallel combination of two identical cells, the equivalent EMF is $E_{eq} = E$, and equivalent internal resistance is $r_{eq} = r/2$.
Current through external resistor $R$ is $I = \frac{E_{eq}}{R + r_{eq}} = \frac{E}{r + r/2} = \frac{E}{1.5r} = \mathbf{\frac{2E}{3r}}$.
</details>

**Q14.** A battery charger delivers a constant current of $2\text{ A}$ to a cell of EMF $1.2\text{ V}$ and internal resistance $0.15\text{ }\Omega$. The electrical power converted to chemical energy in the cell is:
(a) $2.4\text{ W}$
(b) $0.6\text{ W}$
(c) $3.0\text{ W}$
(d) $1.8\text{ W}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

During charging, the electrical power converted into chemical energy is given by $P_{chem} = E \times I = 1.2\text{ V} \times 2\text{ A} = \mathbf{2.4\text{ W}}$. The power dissipated as heat is $I^2 r = 2^2 \times 0.15 = 0.6\text{ W}$, and the total input power is $V I = (E + Ir)I = (1.2 + 0.3) \times 2 = 3.0\text{ W}$.
</details>

**Q15.** The terminal potential difference $V$ across a cell of EMF $E$ and internal resistance $r$ is plotted against the external resistance $R$. Which of the following is correct?
(a) The graph is a straight line starting from the origin with a positive slope.
(b) The graph starts from $E$ when $R=0$ and decreases to $0$ as $R \rightarrow \infty$.
(c) The graph starts from $0$ when $R=0$ and approaches $E$ asymptotically as $R \rightarrow \infty$.
(d) The graph is a horizontal straight line at $V = E$.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The relation is $V = E \frac{R}{R+r}$. At $R = 0$, $V = 0$. As $R \rightarrow \infty$, $V \rightarrow E$. Thus, the graph starts from the origin and asymptotically approaches $E$.
</details>

**Q16.** A cell of EMF $E$ and internal resistance $r$ is connected to a variable external resistance $R$. As $R$ is increased from zero to a very large value, the current $I$ and terminal voltage $V$ vary as:
(a) $I$ increases, $V$ increases
(b) $I$ decreases, $V$ decreases
(c) $I$ decreases, $V$ increases
(d) $I$ increases, $V$ decreases

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

$I = \frac{E}{R+r}$, so as $R$ increases, the denominator increases, and $I$ decreases.
$V = E - Ir$. Since $I$ decreases, $Ir$ decreases, which means $V$ increases.
</details>

**Q17.** A cell of EMF $E$ and internal resistance $r$ is connected across a resistor $R$. If the current in the circuit is $I$, the potential difference across the internal resistance of the cell is:
(a) $E$
(b) $V$
(c) $E+V$
(d) $E-V$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

The terminal potential difference is $V = E - Ir$. Therefore, the potential drop across the internal resistance is $Ir = \mathbf{E - V}$.
</details>

**Q18.** A cell of EMF $1.5\text{ V}$ and internal resistance $1\text{ }\Omega$ is connected to an external resistance of $2\text{ }\Omega$. The rate of heat dissipation inside the cell is:
(a) $0.25\text{ W}$
(b) $0.50\text{ W}$
(c) $0.75\text{ W}$
(d) $1.00\text{ W}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Current in the circuit is $I = \frac{E}{R+r} = \frac{1.5}{2+1} = \frac{1.5}{3} = 0.5\text{ A}$. The rate of heat dissipation inside the cell (in its internal resistance $r$) is $P = I^2 r = (0.5)^2 \times 1 = \mathbf{0.25\text{ W}}$.
</details>

**Q19.** An external resistance $R$ is connected to a cell of EMF $E$ and internal resistance $r$. The efficiency of power transfer is defined as $\eta = P_{out} / P_{total}$. The efficiency $\eta$:
(a) is independent of $R$
(b) increases as $R$ increases
(c) decreases as $R$ increases
(d) is maximum when $R = r$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Efficiency $\eta = \frac{I^2 R}{I^2 (R+r)} = \frac{R}{R+r} = \frac{1}{1 + r/R}$. As $R$ increases, $r/R$ decreases, so the denominator decreases, and efficiency $\eta$ increases (approaching $100\%$ as $R \rightarrow \infty$, though the actual power delivered drops to zero as current vanishes).
</details>

**Q20.** **Statement I:** Under short-circuit conditions, the current drawn from a cell is maximum, but the power delivered to the external circuit is zero.
**Statement II:** Under short-circuit conditions, the external resistance is zero, so the terminal voltage of the cell becomes zero.
(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Both statements are true. In a short circuit, $R = 0$, so $I = E/r$ (maximum current). The power delivered to the external circuit is $P = I^2 R = I^2 (0) = \mathbf{0\text{ W}}$. Since $R = 0$, the terminal voltage $V = I R = \mathbf{0\text{ V}}$, which explains why the power delivered is zero.
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🔴 A battery of EMF $10\text{V}$ and internal resistance $3\text{ } \Omega$ is connected to a resistor. If the current in the circuit is $0.5\text{ A}$, what is the resistance of the resistor?<br> What is the terminal voltage of the battery when the circuit is closed?<br>

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

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Define internal resistance of a cell. On what factors does it depend?<br> *(2 marks)*

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

## 🚀 Stage 7: JEE Mains Arena

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

**Q3.** 🔴 ⭐ In a circuit, a cell of EMF $\varepsilon$ and internal resistance $r$ is connected to an external resistance $R$. A voltmeter (which is non-ideal and has finite resistance $R_v$) is connected across the cell. Which of the following statements is true?<br>

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
