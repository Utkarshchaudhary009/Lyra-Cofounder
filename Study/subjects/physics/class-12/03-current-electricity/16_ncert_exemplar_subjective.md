# Chapter 16: NCERT Exemplar — Subjective Questions (SA/LA)

> *This chapter compiles the best Short Answer (SA) and Long Answer (LA) questions from the official NCERT Exemplar. These questions often form the exact basis for 3-mark and 5-mark board exam questions.*

---

## 🎯 Short Answer Type (SA) — 2 & 3 Marks

**Q1.** 🟡 Alloys of metals usually have (greater/less) resistivity than that of their constituent metals. Why?<br>

<details>
<summary><b>Model Answer</b></summary>

Alloys usually have **greater** resistivity than their constituent metals.
**Reason:** In a pure metal, the lattice arrangement of positive ions is highly regular and periodic, allowing electrons to flow with relatively few collisions. An alloy is a mixture of different metals with different atomic sizes. This creates structural irregularities and disorder in the lattice. These irregularities act as scattering centers, significantly increasing the frequency of collisions for free electrons, thereby decreasing the relaxation time ($\tau$) and increasing resistivity ($\rho = \frac{m}{ne^2\tau}$).
</details>

**Q2.** 🟡 A straight line plot showing the terminal potential difference ($V$) of a cell as a function of current ($I$) drawn from it is given. The y-intercept is $1.5\text{V}$ and x-intercept is $1.5\text{A}$.
(a) What is the EMF of the cell?<br>
(b) What is the internal resistance of the cell?<br>

<details>
<summary><b>Model Answer</b></summary>

The equation for terminal potential difference when discharging is $V = \varepsilon - Ir$.
(a) The y-intercept occurs when $I = 0$ (open circuit). 
At $I = 0$, $V = \varepsilon$. Therefore, the EMF is **$1.5\text{V}$**.
(b) The x-intercept occurs when $V = 0$ (short circuit).
At $V = 0$, $0 = \varepsilon - Ir \implies r = \varepsilon / I$.
Given $I = 1.5\text{A}$ at the intercept, $r = 1.5\text{V} / 1.5\text{A} = \mathbf{1.0\text{ } \Omega}$.
</details>

**Q3.** 🟡 Is the momentum conserved when charge crosses a junction in an electric circuit?<br> Why or why not?<br>

<details>
<summary><b>Model Answer</b></summary>

**No**, the momentum of an individual charged particle (electron) is not conserved when it crosses a junction.
**Reason:** At a macroscopic level, current (charge flow) is conserved due to KCL. However, as electrons move, they constantly collide with the stationary lattice ions of the conductor. In each collision, they transfer momentum to the lattice (causing Joule heating). Furthermore, at a junction, the direction of the electric field steering the electrons changes. The electrons experience a force from this changing electric field and from the collisions, meaning there is an external force acting on them. Since external force $\neq 0$, momentum is not conserved.
</details>

**Q4.** 🔴 The relaxation time $\tau$ is nearly independent of applied electric field $\mathbf{E}$ whereas it changes significantly with temperature $T$. First fact is responsible for Ohm's law whereas the second fact leads to variation of $\rho$ with temperature. Elaborate why.

<details>
<summary><b>Model Answer</b></summary>

1. **Independence from $\mathbf{E}$:** The drift velocity $v_d$ gained by electrons due to the applied electric field is of the order of $10^{-4}\text{ m/s}$. The random thermal velocity of electrons is massive, around $10^5\text{ m/s}$. Since $10^{-4} \ll 10^5$, the addition of the electric field barely changes the overall speed of the electrons. Thus, the time between collisions ($\tau = \text{distance} / \text{thermal speed}$) is entirely dominated by the thermal speed and remains practically unchanged by $\mathbf{E}$. Since $\tau$ is constant with respect to $\mathbf{E}$, resistivity ($\rho$) remains constant, leading to $V \propto I$ (Ohm's Law).
2. **Dependence on $T$:** When temperature $T$ increases, the thermal energy of both the electrons and the lattice ions increases. The ions vibrate with a much larger amplitude. Because the obstacles are moving more wildly, the electrons collide with them much more frequently. This drastically decreases the relaxation time $\tau$. Since $\rho \propto 1/\tau$, the resistivity increases significantly with temperature.
</details>

---

## 🎯 Long Answer Type (LA) — 5 Marks

**Q5.** 🔴 Two cells of same emf $E$ but internal resistance $r_1$ and $r_2$ are connected in series to an external resistor $R$ (Fig). What should be the value of $R$ so that the potential difference across the terminals of the first cell becomes zero?<br>

<details>
<summary><b>Model Answer</b></summary>

**Step 1: Find the total current in the circuit.**
The two cells are in series. Total EMF = $E + E = 2E$.
Total resistance = $R + r_1 + r_2$.
Current $I = \frac{2E}{R + r_1 + r_2}$.

**Step 2: Find the terminal potential difference of the first cell.**
The terminal potential difference of a discharging cell is $V_1 = E - I r_1$.
We are given that $V_1 = 0$.
So, $E - I r_1 = 0 \implies E = I r_1$.

**Step 3: Substitute $I$ and solve for $R$.**
Substitute the expression for $I$ from Step 1:
$E = \left( \frac{2E}{R + r_1 + r_2} \right) r_1$
Divide both sides by $E$:
$1 = \frac{2r_1}{R + r_1 + r_2}$
Cross-multiply:
$R + r_1 + r_2 = 2r_1$
$R = 2r_1 - r_1 - r_2$
**$R = r_1 - r_2$**

*(Note: For this to be physically possible, $R$ must be positive, which means the internal resistance of the first cell $r_1$ must be strictly greater than the internal resistance of the second cell $r_2$).*
</details>

**Q6.** 🔴 ⭐ (a) State the two Kirchhoff's rules.
(b) A network of resistors is connected to a $16\text{V}$ battery with internal resistance of $1\text{ } \Omega$. The network consists of:
- A parallel pair of $4\text{ } \Omega$ and $4\text{ } \Omega$ between nodes A and B.
- A series resistor of $1\text{ } \Omega$ between nodes B and C.
- A parallel pair of $12\text{ } \Omega$ and $6\text{ } \Omega$ between nodes C and D.
Calculate the equivalent resistance of the network, the total current, and the voltage drops $V_{AB}$, $V_{BC}$, and $V_{CD}$.

<details>
<summary><b>Model Answer</b></summary>

**(a) Kirchhoff's Rules:**
1. **Junction Rule (KCL):** $\sum I = 0$ at any node. (Conservation of charge).
2. **Loop Rule (KVL):** $\sum \Delta V = 0$ around any closed loop. (Conservation of energy).

**(b) Circuit Analysis:**
**Step 1: Equivalent Resistance ($R_{eq}$)**
- Part AB (Parallel): $R_{AB} = \frac{4 \times 4}{4 + 4} = \frac{16}{8} = 2\text{ } \Omega$.
- Part BC (Series): $R_{BC} = 1\text{ } \Omega$.
- Part CD (Parallel): $R_{CD} = \frac{12 \times 6}{12 + 6} = \frac{72}{18} = 4\text{ } \Omega$.
Total external resistance $R_{ext} = R_{AB} + R_{BC} + R_{CD} = 2 + 1 + 4 = \mathbf{7\text{ } \Omega}$.

**Step 2: Total Current ($I$)**
Total circuit resistance = $R_{ext} + r = 7 + 1 = 8\text{ } \Omega$.
Total current $I = \varepsilon / R_{total} = 16 / 8 = \mathbf{2\text{ A}}$.

**Step 3: Voltage Drops**
Since all these sections are in series with the main battery, the total current of $2\text{A}$ flows through each section.
- $V_{AB} = I \times R_{AB} = 2 \times 2 = \mathbf{4\text{ V}}$.
- $V_{BC} = I \times R_{BC} = 2 \times 1 = \mathbf{2\text{ V}}$.
- $V_{CD} = I \times R_{CD} = 2 \times 4 = \mathbf{8\text{ V}}$.

*(Verification: Total external voltage $V_{ext} = 4 + 2 + 8 = 14\text{V}$. Terminal voltage $V = \varepsilon - Ir = 16 - 2(1) = 14\text{V}$. The calculations are correct!)*
</details>

**Q7.** 🔴 Determine the current drawn from a $12\text{V}$ supply with internal resistance $0.5\text{ } \Omega$ by an infinite network shown in the standard configuration (repeating series $1\text{ } \Omega$ and parallel $2\text{ } \Omega$).

<details>
<summary><b>Model Answer</b></summary>

*(This is a classic problem we covered in Chapter 8, but formulated as a board question).*

**Step 1: Find Equivalent Resistance of the infinite ladder.**
Let the equivalent resistance of the infinite ladder be $X$.
The repeating unit is a $1\text{ } \Omega$ series and a $2\text{ } \Omega$ parallel resistor.
If we remove the first unit, the remaining infinite ladder still has resistance $X$.
Therefore, the circuit is equivalent to $1\text{ } \Omega$ in series with the parallel combination of $2\text{ } \Omega$ and $X$.
$X = 1 + \frac{2X}{2 + X}$
$X(2 + X) = 1(2 + X) + 2X$
$2X + X^2 = 2 + 3X$
$X^2 - X - 2 = 0$
$(X - 2)(X + 1) = 0$
Since resistance must be positive, $X = \mathbf{2\text{ } \Omega}$.

**Step 2: Calculate Current**
The external resistance is $R = 2\text{ } \Omega$.
The battery has $\varepsilon = 12\text{V}$ and internal resistance $r = 0.5\text{ } \Omega$.
Total resistance = $R + r = 2 + 0.5 = 2.5\text{ } \Omega$.
Current $I = \frac{\varepsilon}{R + r} = \frac{12}{2.5} = \frac{120}{25} = \mathbf{4.8\text{ A}}$.
</details>

---

**🏁 CONGRATULATIONS! You have completed the Current Electricity Mastery Book! 🏁**
