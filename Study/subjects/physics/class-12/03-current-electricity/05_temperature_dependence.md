# Chapter 5: Temperature Dependence of Resistance

> *NCERT Section 3.8*

---

## 🎯 Stage 1: The Core Idea

### Why Does Temperature Change Resistance?<br>

Let's go back to the highway analogy from Chapter 4. 
- The **electrons** are the cars trying to drive down the highway.
- The **metal ions** forming the lattice are obstacles (like construction cones) on the road.

At absolute zero ($0 \text{ K}$), the ions are perfectly still. The electrons can weave through them easily.
But as the temperature rises, the metal ions gain thermal energy and start vibrating violently. They act like construction cones bouncing around the highway!

Because the ions are vibrating over a larger amplitude, the electrons collide with them much more frequently. 
- More collisions $\implies$ shorter relaxation time ($\tau$).
- Since resistivity $\rho \propto 1/\tau$, shorter relaxation time means **higher resistivity**.

> **For Metals (Conductors):** Temperature goes UP $\implies$ Resistance goes UP.

### The Semiconductor Twist

What about semiconductors (like Silicon or Germanium) and insulators?<br>
Here, an increase in temperature does increase lattice vibrations, but it does something much more important: **it breaks chemical bonds**, freeing up billions of new electrons to act as charge carriers.

In semiconductors, the number density of carriers ($n$) increases exponentially with temperature. This effect completely overpowers the decrease in relaxation time ($\tau$).
- Since $\rho \propto \frac{1}{n\tau}$, the massive increase in $n$ causes $\rho$ to drop.

> **For Semiconductors & Insulators:** Temperature goes UP $\implies$ Resistance goes DOWN.

### The Special Case of Alloys

Alloys like **Manganin, Constantan, and Nichrome** behave a bit weirdly. They already have high resistivity because their atomic structure is inherently messy (a mix of different metals).
When you heat them, their resistance increases, but only by a *tiny, almost negligible* amount.

This makes them perfect for creating standard resistance coils (like in a resistance box or a meter bridge wire), because their resistance won't change even if they heat up while being used!

---

## 🔬 Stage 2: The Formula Lab

### The Linear Approximation Formula

For small temperature ranges, the change in resistance of a metal is directly proportional to the original resistance and the change in temperature.

$$R_T = R_0 [1 + \alpha (T - T_0)]$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $R_T$ | Resistance at temperature $T$ | $\Omega$ |
| $R_0$ | Resistance at reference temperature $T_0$ (often $0^\circ\text{C}$ or $20^\circ\text{C}$) | $\Omega$ |
| $\alpha$ | Temperature coefficient of resistance | $^\circ\text{C}^{-1}$ or $\text{K}^{-1}$ |
| $T - T_0$ | Change in temperature ($\Delta T$) | $^\circ\text{C}$ or $\text{K}$ |

*(Note: The exact same formula applies to resistivity: $\rho_T = \rho_0 [1 + \alpha (T - T_0)]$)*

### Temperature Coefficient ($\alpha$)

$$\alpha = \frac{R_T - R_0}{R_0 \Delta T} = \frac{\Delta R}{R_0 \Delta T}$$

$\alpha$ defines how much a $1 \text{ }\Omega$ resistor changes its resistance when the temperature changes by $1^\circ\text{C}$.

| Material Type | Sign of $\alpha$ | Meaning |
|---------------|------------------|---------|
| Metals | Positive ($+$) | $R$ increases as $T$ increases |
| Semiconductors / Insulators | Negative ($-$) | $R$ decreases as $T$ increases |
| Alloys (Manganin, etc.) | Positive, but $\approx 0$ | $R$ is almost independent of $T$ |

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic $R_T = R_0(1+\alpha\Delta T)$ calculation ⭐

**Pattern:** "Given $R_0, \alpha$, and $\Delta T$, find $R_T$."

**Solved Example** 🟢

> The resistance of a platinum wire is $5.0 \text{ } \Omega$ at $0^\circ\text{C}$. If its temperature coefficient of resistance is $3.9 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$, find its resistance at $100^\circ\text{C}$.

<details>
<summary><b>Solution</b></summary>

$R_0 = 5.0 \text{ } \Omega$
$T_0 = 0^\circ\text{C}, T = 100^\circ\text{C} \implies \Delta T = 100^\circ\text{C}$
$\alpha = 3.9 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

$R_T = R_0 (1 + \alpha \Delta T)$
$R_T = 5.0 \times [1 + (3.9 \times 10^{-3}) \times 100]$
$R_T = 5.0 \times [1 + 0.39] = 5.0 \times 1.39 = \mathbf{6.95 \text{ } \Omega}$
</details>

**Practice:**

1. 🟢 A silver wire has a resistance of $2.1 \text{ } \Omega$ at $27.5^\circ\text{C}$. Find its resistance at $100^\circ\text{C}$. ($\alpha = 0.0039 \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Answer</b></summary>

$\Delta T = 100 - 27.5 = 72.5^\circ\text{C}$
$R_{100} = 2.1 \times [1 + 0.0039 \times 72.5] = 2.1 \times [1 + 0.28275] \approx \mathbf{2.7 \text{ } \Omega}$
</details>

2. 🟢 The resistance of a conductor is $10 \text{ } \Omega$ at $50^\circ\text{C}$ and $15 \text{ } \Omega$ at $100^\circ\text{C}$. Find its temperature coefficient of resistance ($\alpha$) assuming $0^\circ\text{C}$ as reference.

<details>
<summary><b>Answer</b></summary>

$R_{50} = R_0 (1 + 50\alpha) = 10$  --- (1)
$R_{100} = R_0 (1 + 100\alpha) = 15$ --- (2)
Divide (2) by (1):
$\frac{15}{10} = \frac{1 + 100\alpha}{1 + 50\alpha} \implies 1.5 (1 + 50\alpha) = 1 + 100\alpha$
$1.5 + 75\alpha = 1 + 100\alpha \implies 0.5 = 25\alpha \implies \alpha = 0.5 / 25 = \mathbf{0.02 \text{ } ^\circ\text{C}^{-1}}$
</details>

---

### Type 2: Finding the Temperature ⭐⭐

**Pattern:** "Given resistance at two temperatures, find the temperature where resistance reaches a specific value."

**Solved Example** 🟡

> The resistance of a heating element at room temperature ($27^\circ\text{C}$) is $100 \text{ } \Omega$. At what temperature will its resistance become $117 \text{ } \Omega$?<br> Given $\alpha = 1.7 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$.

<details>
<summary><b>Solution</b></summary>

$R_1 = 100 \text{ } \Omega$ at $T_1 = 27^\circ\text{C}$. (We can use this as our reference $R_0$)
$R_2 = 117 \text{ } \Omega$ at $T_2 = ?<br>$
$\alpha = 1.7 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$

$R_2 = R_1 [1 + \alpha(T_2 - T_1)]$
$117 = 100 [1 + 1.7 \times 10^{-4} \times (T_2 - 27)]$
$117 / 100 = 1 + 1.7 \times 10^{-4} (T_2 - 27)$
$1.17 - 1 = 1.7 \times 10^{-4} (T_2 - 27)$
$0.17 = 1.7 \times 10^{-4} (T_2 - 27)$
$T_2 - 27 = \frac{0.17}{1.7 \times 10^{-4}} = \frac{0.17}{0.00017} = 1000$
$T_2 = 1000 + 27 = \mathbf{1027^\circ\text{C}}$
</details>

**Practice:**

1. 🟡 A metallic wire has a resistance of $120 \text{ } \Omega$ at $20^\circ\text{C}$. Find the temperature at which its resistance becomes $240 \text{ } \Omega$. ($\alpha = 5 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Answer</b></summary>

$240 = 120 [1 + 5 \times 10^{-4} (T - 20)]$
$2 = 1 + 5 \times 10^{-4} (T - 20)$
$1 = 5 \times 10^{-4} (T - 20) \implies T - 20 = 1 / (5 \times 10^{-4}) = 2000$
$T = \mathbf{2020^\circ\text{C}}$
</details>

---

### Type 3: Null-Temperature (Two Resistors Becoming Equal)

**Pattern:** "Resistor A has $R_1, \alpha_1$. Resistor B has $R_2, \alpha_2$. At what temperature are they equal?<br>"

**Solved Example** 🔴

> At $0^\circ\text{C}$, the resistance of conductor A is $2 \text{ } \Omega$ and that of B is $3 \text{ } \Omega$. Their temperature coefficients are $0.004 \text{ } ^\circ\text{C}^{-1}$ and $0.002 \text{ } ^\circ\text{C}^{-1}$ respectively. At what temperature will they have the same resistance?<br>

<details>
<summary><b>Solution</b></summary>

We need $R_A = R_B$ at temperature $T$.
$R_{A0} (1 + \alpha_A T) = R_{B0} (1 + \alpha_B T)$
$2 (1 + 0.004 T) = 3 (1 + 0.002 T)$
$2 + 0.008 T = 3 + 0.006 T$
$0.008 T - 0.006 T = 3 - 2$
$0.002 T = 1 \implies T = 1 / 0.002 = \mathbf{500^\circ\text{C}}$
</details>

**Practice:**

1. 🔴 A carbon resistor (negative $\alpha$) of $47 \text{ } \Omega$ at $20^\circ\text{C}$ ($\alpha = -0.0005 \text{ } ^\circ\text{C}^{-1}$) is in series with an iron resistor of $40 \text{ } \Omega$ at $20^\circ\text{C}$ ($\alpha = 0.005 \text{ } ^\circ\text{C}^{-1}$). At what temperature will they have equal resistance?<br>

<details>
<summary><b>Answer</b></summary>

$47 [1 - 0.0005(T - 20)] = 40 [1 + 0.005(T - 20)]$
Let $x = T - 20$.
$47 - 0.0235x = 40 + 0.2x$
$7 = 0.2235x \implies x = 7 / 0.2235 \approx 31.32^\circ\text{C}$
$T = 20 + 31.32 = \mathbf{51.32^\circ\text{C}}$
</details>

---

### Type 4: Graph Interpretation

**Pattern:** "Given an $R$ vs $T$ or $\rho$ vs $T$ graph, identify the material."

| Material | Graph Shape (Resistivity vs Temp) | Why?<br> |
|----------|-----------------------------------|------|
| **Metals** (Copper, etc.) | Non-linear curve at very low T, then straight line with positive slope. | $\rho_T \approx \rho_0(1+\alpha T)$. $\alpha$ is positive. |
| **Alloys** (Nichrome, etc.) | Straight line with very small positive slope, starting high. | High $\rho_0$, very small $\alpha$. |
| **Semiconductors** (Si, Ge) | Exponential decay curve. | Number density $n$ increases exponentially with $T$. $\alpha$ is negative. |

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A standard coil is marked $3 \text{ } \Omega$. If it is made of manganin ($\alpha = 10^{-5} \text{ } ^\circ\text{C}^{-1}$), what will be its resistance at $100^\circ\text{C}$?<br> Assume the $3 \text{ } \Omega$ marking is at $0^\circ\text{C}$.

<details>
<summary><b>Solution</b></summary>

$R_{100} = R_0 (1 + \alpha \Delta T)$
$R_{100} = 3 \times [1 + 10^{-5} \times 100]$
$R_{100} = 3 \times [1 + 0.001] = 3 \times 1.001 = \mathbf{3.003 \text{ } \Omega}$

Notice how little it changed! This is why manganin is used for standard resistors.
</details>

**Q2.** 🔴 ⭐ An electric toaster uses nichrome for its heating element. When a negligibly small current passes through it, its resistance at room temperature ($27^\circ\text{C}$) is found to be $75.3 \text{ } \Omega$. When the toaster is connected to a $230 \text{ V}$ supply, the current settles, after a few seconds, to a steady value of $2.68 \text{ A}$. What is the steady temperature of the nichrome element?<br> ($\alpha = 1.7 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Solution</b></summary>

1. Resistance at room temp ($T_1 = 27^\circ\text{C}$) is $R_1 = 75.3 \text{ } \Omega$.
2. When operating, it gets hot. The steady resistance $R_2$ is found using Ohm's Law:
   $R_2 = V / I = 230 / 2.68 = \mathbf{85.8 \text{ } \Omega}$.
3. Now use the temperature formula:
   $R_2 = R_1 [1 + \alpha (T_2 - T_1)]$
   $85.8 = 75.3 [1 + 1.7 \times 10^{-4} \times (T_2 - 27)]$
   $85.8 / 75.3 = 1 + 1.7 \times 10^{-4} (T_2 - 27)$
   $1.139 = 1 + 1.7 \times 10^{-4} (T_2 - 27)$
   $0.139 = 1.7 \times 10^{-4} (T_2 - 27)$
   $T_2 - 27 = 0.139 / 0.00017 \approx 818^\circ\text{C}$
   $T_2 = 818 + 27 = \mathbf{845^\circ\text{C}}$

*(This is a classic NCERT exercise problem!)*
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Why does the resistivity of a metallic conductor increase with an increase in temperature?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Resistivity of a metal is given by $\rho = \frac{m}{ne^2\tau}$. 
When temperature increases, the amplitude of vibration of the positive ions in the metal lattice increases. This causes free electrons to collide more frequently with the ions, decreasing the average relaxation time ($\tau$).
Since $\rho \propto \frac{1}{\tau}$, the resistivity of the metal increases. The number density ($n$) remains almost constant for metals.
</details>

**Q2.** 🟡 Plot a graph showing the variation of resistivity with temperature for (i) a typical metal like copper, and (ii) a semiconductor. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(Draw two graphs)*
**(i) For Copper (Metal):** A curve starting slightly above the origin, increasing non-linearly at first, then becoming a straight line with a positive slope at higher temperatures.
**(ii) For Semiconductor:** A curve starting high on the y-axis and decaying exponentially towards the x-axis as temperature increases.
</details>

**Q3.** 🟡 Define temperature coefficient of resistance. What is its unit?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Temperature coefficient of resistance ($\alpha$) is defined as the fractional change in resistance of a conductor per unit change in its temperature, relative to its resistance at a reference temperature (usually $0^\circ\text{C}$).
Mathematically, $\alpha = \frac{\Delta R}{R_0 \Delta T}$.
**Unit:** $^\circ\text{C}^{-1}$ or $\text{K}^{-1}$.
</details>

**Q4.** 🟡 State two reasons why alloys like constantan and manganin are used for making standard resistor coils. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. They have **high resistivity**, allowing compact coils to provide appreciable resistance.
2. They have a **very low temperature coefficient of resistance ($\alpha$)**, which means their resistance remains practically constant even if their temperature changes during an experiment.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The resistance of a metal wire is $10 \text{ } \Omega$ at $20^\circ\text{C}$ and $12 \text{ } \Omega$ at $60^\circ\text{C}$. The temperature coefficient of resistance of the metal is:

(a) $0.005 \text{ } ^\circ\text{C}^{-1}$ &emsp; (b) $0.004 \text{ } ^\circ\text{C}^{-1}$ &emsp; (c) $0.01 \text{ } ^\circ\text{C}^{-1}$ &emsp; (d) $0.02 \text{ } ^\circ\text{C}^{-1}$

<details>
<summary><b>Answer</b></summary>

Let's assume the linear approximation holds from $20^\circ\text{C}$ directly.
$R_{T2} = R_{T1} [1 + \alpha (T_2 - T_1)]$
$12 = 10 [1 + \alpha (60 - 20)]$
$1.2 = 1 + 40\alpha$
$0.2 = 40\alpha \implies \alpha = 0.2 / 40 = \mathbf{0.005 \text{ } ^\circ\text{C}^{-1}}$

**Answer: (a)**
</details>

**Q2.** 🔴 Two wires of resistance $R_1$ and $R_2$ have temperature coefficients of resistance $\alpha_1$ and $\alpha_2$ respectively. They are joined in series. The effective temperature coefficient of resistance of the combination is:

(a) $\frac{\alpha_1 + \alpha_2}{2}$ &emsp; (b) $\sqrt{\alpha_1 \alpha_2}$ &emsp; (c) $\frac{\alpha_1 R_1 + \alpha_2 R_2}{R_1 + R_2}$ &emsp; (d) $\frac{\alpha_1 R_2 + \alpha_2 R_1}{R_1 + R_2}$

<details>
<summary><b>Answer</b></summary>

In series, equivalent resistance at $0^\circ\text{C}$ is $R_{eq} = R_1 + R_2$.
At temperature $T$:
$R_{eq}(T) = R_1(T) + R_2(T)$
$R_{eq}(1 + \alpha_{eq} T) = R_1(1 + \alpha_1 T) + R_2(1 + \alpha_2 T)$
$(R_1 + R_2) + (R_1 + R_2)\alpha_{eq} T = (R_1 + R_2) + (R_1\alpha_1 + R_2\alpha_2)T$
Cancel $(R_1 + R_2)$ from both sides:
$(R_1 + R_2)\alpha_{eq} T = (R_1\alpha_1 + R_2\alpha_2)T$
$\alpha_{eq} = \mathbf{\frac{R_1\alpha_1 + R_2\alpha_2}{R_1 + R_2}}$

**Answer: (c)**
*(This looks exactly like a center-of-mass formula!)*
</details>

**Q3.** 🔴 ⭐ An aluminium wire and a copper wire of the same length and same resistance are given. Which of the two is lighter?<br>
(Given: Density of Al $= 2.7 \text{ g/cm}^3$, $\rho_{Al} = 2.6 \times 10^{-8} \text{ } \Omega\cdot\text{m}$; Density of Cu $= 8.9 \text{ g/cm}^3$, $\rho_{Cu} = 1.7 \times 10^{-8} \text{ } \Omega\cdot\text{m}$)

(a) Aluminium &emsp; (b) Copper &emsp; (c) Both have same mass &emsp; (d) Cannot be determined

<details>
<summary><b>Answer</b></summary>

This is a classic question comparing materials for power transmission lines.
$R = \rho \frac{L}{A} \implies A = \frac{\rho L}{R}$.
Mass $m = \text{Volume} \times \text{Density} = (A \times L) \times d = \left(\frac{\rho L}{R}\right) \times L \times d = \frac{L^2}{R} (\rho d)$.
Since $L$ and $R$ are same for both, Mass $\propto (\rho \times d)$.
For Copper: $\rho \times d = (1.7 \times 10^{-8}) \times 8.9 \approx 15 \times 10^{-8}$
For Aluminium: $\rho \times d = (2.6 \times 10^{-8}) \times 2.7 \approx 7 \times 10^{-8}$

The product $(\rho \times d)$ is much smaller for Aluminium. Therefore, the **Aluminium wire is lighter** (less than half the mass of the copper wire for the same resistance). This is why overhead power cables use Aluminium instead of Copper.

**Answer: (a)**
</details>

---

*Next: [Chapter 6 — Limitations of Ohm's Law (Non-Ohmic Devices) →](./06_limitations_of_ohms_law.md)*
