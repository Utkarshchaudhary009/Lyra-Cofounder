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

3. 🟢 A copper wire has a resistance of $4.0 \text{ } \Omega$ at $0^\circ\text{C}$. If the temperature coefficient of resistance of copper is $4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$, find its resistance at $80^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_0 = 4.0 \text{ } \Omega$
- $T_0 = 0^\circ\text{C}$, $T = 80^\circ\text{C} \implies \Delta T = 80^\circ\text{C}$
- $\alpha = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

Formula:
$$R_T = R_0 (1 + \alpha \Delta T)$$

Substitution:
$$R_{80} = 4.0 \times [1 + (4.0 \times 10^{-3}) \times 80]$$
$$R_{80} = 4.0 \times [1 + 0.32] = 4.0 \times 1.32 = \mathbf{5.28 \text{ } \Omega}$$
</details>

4. 🟢 A coil of wire has a resistance of $8.2 \text{ } \Omega$ at $20^\circ\text{C}$. If its temperature coefficient of resistance is $3.8 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$, calculate its resistance at $100^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{20} = 8.2 \text{ } \Omega$
- $\alpha = 3.8 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$
- $\Delta T = 100 - 20 = 80^\circ\text{C}$

Assuming reference temperature is $20^\circ\text{C}$:
$$R_{100} = R_{20} (1 + \alpha \Delta T)$$
$$R_{100} = 8.2 \times [1 + (3.8 \times 10^{-3}) \times 80]$$
$$R_{100} = 8.2 \times [1 + 0.304] = 8.2 \times 1.304 = \mathbf{10.69 \text{ } \Omega}$$
</details>

5. 🟡 ⭐ At what temperature will the resistance of a copper wire become double its resistance at $0^\circ\text{C}$? (Given $\alpha_{\text{Cu}} = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Answer</b></summary>

Given:
- $R_T = 2 R_0$
- $\alpha = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$
- $T_0 = 0^\circ\text{C} \implies \Delta T = T$

Formula:
$$R_T = R_0 (1 + \alpha \Delta T)$$
$$2 R_0 = R_0 (1 + \alpha T)$$
$$2 = 1 + \alpha T \implies \alpha T = 1$$
$$T = \frac{1}{\alpha} = \frac{1}{4.0 \times 10^{-3}} = \mathbf{250^\circ\text{C}}$$
</details>

6. 🟢 A wire has a resistance of $5.0 \text{ } \Omega$ at $50^\circ\text{C}$. If $\alpha = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$ at $0^\circ\text{C}$, find its resistance at $0^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{50} = 5.0 \text{ } \Omega$
- $\alpha = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$ at $0^\circ\text{C}$
- $T_0 = 0^\circ\text{C}$, $T = 50^\circ\text{C} \implies \Delta T = 50^\circ\text{C}$

Formula:
$$R_{50} = R_0 (1 + \alpha \Delta T)$$
$$5.0 = R_0 [1 + (4.0 \times 10^{-3}) \times 50]$$
$$5.0 = R_0 [1 + 0.20] = 1.20 R_0$$
$$R_0 = \frac{5.0}{1.20} = \mathbf{4.17 \text{ } \Omega}$$
</details>

7. 🟡 The resistivity of a metal increases by $25\%$ when heated from $20^\circ\text{C}$ to $120^\circ\text{C}$. Find its temperature coefficient of resistivity $\alpha$ with $20^\circ\text{C}$ as the reference temperature.

<details>
<summary><b>Answer</b></summary>

Given:
- Reference resistivity at $T_0 = 20^\circ\text{C}$ is $\rho_{20}$.
- $\rho_{120} = 1.25 \rho_{20}$
- $\Delta T = 120 - 20 = 100^\circ\text{C}$

Formula:
$$\rho_{120} = \rho_{20} (1 + \alpha \Delta T)$$
$$1.25 \rho_{20} = \rho_{20} (1 + \alpha \times 100)$$
$$1.25 = 1 + 100 \alpha$$
$$0.25 = 100 \alpha \implies \alpha = \frac{0.25}{100} = \mathbf{2.5 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}}$$
</details>

8. 🟢 A tungsten filament of a lamp has resistance $2.4 \text{ } \Omega$ at $20^\circ\text{C}$. Calculate its resistance when it hot-glows at a temperature of $2000^\circ\text{C}$. (Take $\alpha_{\text{W}} = 4.5 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{20} = 2.4 \text{ } \Omega$
- $\alpha = 4.5 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$
- $\Delta T = 2000 - 20 = 1980^\circ\text{C}$

Formula:
$$R_{2000} = R_{20} (1 + \alpha \Delta T)$$
$$R_{2000} = 2.4 \times [1 + (4.5 \times 10^{-3}) \times 1980]$$
$$R_{2000} = 2.4 \times [1 + 8.91] = 2.4 \times 9.91 = \mathbf{23.78 \text{ } \Omega}$$
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

2. 🟡 A platinum resistance thermometer has a resistance of $5.25 \text{ } \Omega$ at $0^\circ\text{C}$ and $6.75 \text{ } \Omega$ at $100^\circ\text{C}$. When it is inserted in a hot bath, its resistance becomes $9.00 \text{ } \Omega$. Find the temperature of the bath.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_0 = 5.25 \text{ } \Omega$ at $0^\circ\text{C}$
- $R_{100} = 6.75 \text{ } \Omega$ at $100^\circ\text{C}$
- $R_T = 9.00 \text{ } \Omega$ at $T$

We first find $\alpha$ or use the ratio formula:
$$R_T = R_0 (1 + \alpha T) \implies \alpha T = \frac{R_T - R_0}{R_0}$$
$$R_{100} = R_0 (1 + 100\alpha) \implies \alpha \times 100 = \frac{R_{100} - R_0}{R_0}$$

Dividing the two equations:
$$\frac{T}{100} = \frac{R_T - R_0}{R_{100} - R_0}$$
$$\frac{T}{100} = \frac{9.00 - 5.25}{6.75 - 5.25} = \frac{3.75}{1.50} = 2.5$$
$T = 2.5 \times 100 = \mathbf{250^\circ\text{C}}$
</details>

3. 🟡 ⭐ The resistance of the filament of a light bulb is $15 \text{ } \Omega$ at $20^\circ\text{C}$ and increases to $165 \text{ } \Omega$ when connected to a source. If the temperature coefficient of resistance is $4.5 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$ at $20^\circ\text{C}$, find the operating temperature of the filament.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{20} = 15 \text{ } \Omega$ at $T_0 = 20^\circ\text{C}$
- $R_T = 165 \text{ } \Omega$
- $\alpha = 4.5 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

Formula:
$$R_T = R_{20} [1 + \alpha (T - 20)]$$
$$165 = 15 [1 + (4.5 \times 10^{-3}) (T - 20)]$$
$$11 = 1 + (4.5 \times 10^{-3}) (T - 20)$$
$$10 = (4.5 \times 10^{-3}) (T - 20)$$
$$T - 20 = \frac{10}{4.5 \times 10^{-3}} = \frac{10000}{4.5} \approx 2222.2^\circ\text{C}$$
$$T \approx 2222.2 + 20 = \mathbf{2242.2^\circ\text{C}}$$
</details>

4. 🟡 A heating element has a resistance of $80 \text{ } \Omega$ at $27^\circ\text{C}$. What is the temperature when its resistance is $92 \text{ } \Omega$? (Given $\alpha = 1.5 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$)

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{27} = 80 \text{ } \Omega$ at $T_0 = 27^\circ\text{C}$
- $R_T = 92 \text{ } \Omega$
- $\alpha = 1.5 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}$

Formula:
$$R_T = R_{27} [1 + \alpha (T - 27)]$$
$$92 = 80 [1 + (1.5 \times 10^{-4}) (T - 27)]$$
$$1.15 = 1 + (1.5 \times 10^{-4}) (T - 27)$$
$$0.15 = (1.5 \times 10^{-4}) (T - 27)$$
$$T - 27 = \frac{0.15}{1.5 \times 10^{-4}} = 1000^\circ\text{C}$$
$$T = 1000 + 27 = \mathbf{1027^\circ\text{C}}$$
</details>

5. 🟡 A resistance of $50 \text{ } \Omega$ is measured at $0^\circ\text{C}$ for a copper wire. If its resistance at $T^\circ\text{C}$ is $65 \text{ } \Omega$, find $T$ if $\alpha$ of copper is $4.3 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$ at $0^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_0 = 50 \text{ } \Omega$
- $R_T = 65 \text{ } \Omega$
- $\alpha = 4.3 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

Formula:
$$R_T = R_0 (1 + \alpha T)$$
$$65 = 50 [1 + (4.3 \times 10^{-3}) T]$$
$$1.30 = 1 + (4.3 \times 10^{-3}) T$$
$$0.30 = (4.3 \times 10^{-3}) T$$
$$T = \frac{0.30}{4.3 \times 10^{-3}} \approx \mathbf{69.8^\circ\text{C}}$$
</details>

6. 🟡 The resistance of a silver wire is $2.0 \text{ } \Omega$ at $20^\circ\text{C}$ and increases to $2.8 \text{ } \Omega$ at a certain temperature $T$. Find $T$ if $\alpha_{\text{silver}} = 3.8 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$ at $20^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{20} = 2.0 \text{ } \Omega$ at $T_0 = 20^\circ\text{C}$
- $R_T = 2.8 \text{ } \Omega$
- $\alpha = 3.8 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

Formula:
$$R_T = R_{20} [1 + \alpha (T - 20)]$$
$$2.8 = 2.0 [1 + (3.8 \times 10^{-3}) (T - 20)]$$
$$1.4 = 1 + (3.8 \times 10^{-3}) (T - 20)$$
$$0.4 = (3.8 \times 10^{-3}) (T - 20)$$
$$T - 20 = \frac{0.4}{3.8 \times 10^{-3}} = \frac{400}{3.8} \approx 105.3^\circ\text{C}$$
$$T = 105.3 + 20 = \mathbf{125.3^\circ\text{C}}$$
</details>

7. 🔴 A metal resistor has a resistance of $10.0 \text{ } \Omega$ at $0^\circ\text{C}$ and $10.5 \text{ } \Omega$ at $20^\circ\text{C}$. At what temperature will its resistance be $12.5 \text{ } \Omega$?

<details>
<summary><b>Answer</b></summary>

Given:
- $R_0 = 10.0 \text{ } \Omega$ at $0^\circ\text{C}$
- $R_{20} = 10.5 \text{ } \Omega$ at $20^\circ\text{C}$
- $R_T = 12.5 \text{ } \Omega$

Using the linear formula with reference $0^\circ\text{C}$:
$$R_{20} = R_0 (1 + 20 \alpha) \implies 10.5 = 10.0 (1 + 20 \alpha)$$
$$1.05 = 1 + 20 \alpha \implies 20 \alpha = 0.05 \implies \alpha = 0.0025 \text{ } ^\circ\text{C}^{-1}$$

Now find $T$ for $R_T = 12.5 \text{ } \Omega$:
$$R_T = R_0 (1 + \alpha T)$$
$$12.5 = 10.0 (1 + 0.0025 T)$$
$$1.25 = 1 + 0.0025 T$$
$$0.25 = 0.0025 T \implies T = \frac{0.25}{0.0025} = \mathbf{100^\circ\text{C}}$$
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

2. 🔴 Resistor A has a resistance of $200 \text{ } \Omega$ at $0^\circ\text{C}$ and $\alpha_A = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$. Resistor B has $220 \text{ } \Omega$ at $0^\circ\text{C}$ and $\alpha_B = 2.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$. At what temperature will both resistors have the exact same resistance?

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{A0} = 200 \text{ } \Omega$, $\alpha_A = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$
- $R_{B0} = 220 \text{ } \Omega$, $\alpha_B = 2.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$

We set $R_A(T) = R_B(T)$:
$$R_{A0} (1 + \alpha_A T) = R_{B0} (1 + \alpha_B T)$$
$$200 (1 + 0.004 T) = 220 (1 + 0.002 T)$$
$$200 + 0.8 T = 220 + 0.44 T$$
$$0.8 T - 0.44 T = 220 - 200$$
$$0.36 T = 20 \implies T = \frac{20}{0.36} = \mathbf{55.56^\circ\text{C}}$$
</details>

3. 🔴 A copper resistor of resistance $100 \text{ } \Omega$ ($\alpha_{\text{Cu}} = 3.9 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$) and an iron resistor of resistance $80 \text{ } \Omega$ ($\alpha_{\text{Fe}} = 5.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$), both at $0^\circ\text{C}$, are heated. At what temperature does the difference between their resistances become $21 \text{ } \Omega$?

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{Cu}(T) = R_{Cu0}(1 + \alpha_{Cu} T) = 100(1 + 0.0039 T) = 100 + 0.39 T$
- $R_{Fe}(T) = R_{Fe0}(1 + \alpha_{Fe} T) = 80(1 + 0.005 T) = 80 + 0.40 T$

We want the difference $|R_{Cu}(T) - R_{Fe}(T)| = 21 \text{ } \Omega$.
Let's look at the difference:
$$R_{Cu}(T) - R_{Fe}(T) = (100 + 0.39 T) - (80 + 0.40 T) = 20 - 0.01 T$$
Case 1: $20 - 0.01 T = 21 \implies -0.01 T = 1 \implies T = -100^\circ\text{C}$
Case 2: $20 - 0.01 T = -21 \implies 0.01 T = 41 \implies T = \mathbf{4100^\circ\text{C}}$

For a physical temperature rise, the temperature is **$4100^\circ\text{C}$** (or **$-100^\circ\text{C}$** if cooling down).
</details>

4. 🔴 ⭐ An alloy wire (Manganin) of resistance $50 \text{ } \Omega$ at $0^\circ\text{C}$ ($\alpha_1 = 1.0 \times 10^{-5} \text{ } ^\circ\text{C}^{-1}$) and a copper wire of resistance $40 \text{ } \Omega$ at $0^\circ\text{C}$ ($\alpha_2 = 4.0 \times 10^{-3} \text{ } ^\circ\text{C}^{-1}$) are connected in series. Find the temperature at which their combined resistance is $92 \text{ } \Omega$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_1(T) = 50 [1 + (1.0 \times 10^{-5}) T]$
- $R_2(T) = 40 [1 + (4.0 \times 10^{-3}) T]$

For series connection, the combined resistance is:
$$R_{eq}(T) = R_1(T) + R_2(T) = 50 + 0.0005 T + 40 + 0.16 T = 90 + 0.1605 T$$
We want $R_{eq}(T) = 92 \text{ } \Omega$:
$$90 + 0.1605 T = 92$$
$$0.1605 T = 2 \implies T = \frac{2}{0.1605} \approx \mathbf{12.46^\circ\text{C}}$$
</details>

5. 🔴 Two conductors A and B have resistances $150 \text{ } \Omega$ and $100 \text{ } \Omega$ at $0^\circ\text{C}$, and their temperature coefficients of resistance are $\alpha_A = 0.003 \text{ } ^\circ\text{C}^{-1}$ and $\alpha_B = 0.005 \text{ } ^\circ\text{C}^{-1}$ respectively. At what temperature will their resistances be in the ratio $4:3$?

<details>
<summary><b>Answer</b></summary>

Given:
- $R_A(T) = 150 (1 + 0.003 T)$
- $R_B(T) = 100 (1 + 0.005 T)$

We want $\frac{R_A(T)}{R_B(T)} = \frac{4}{3}$:
$$\frac{150 (1 + 0.003 T)}{100 (1 + 0.005 T)} = \frac{4}{3}$$
$$1.5 \frac{1 + 0.003 T}{1 + 0.005 T} = \frac{4}{3} \implies \frac{1 + 0.003 T}{1 + 0.005 T} = \frac{4}{4.5} = \frac{8}{9}$$
$$9 (1 + 0.003 T) = 8 (1 + 0.005 T)$$
$$9 + 0.027 T = 8 + 0.04 T$$
$$1 = 0.04 T - 0.027 T \implies 0.013 T = 1$$
$$T = \frac{1}{0.013} \approx \mathbf{76.92^\circ\text{C}}$$
</details>

6. 🔴 A carbon resistor has resistance $R_C$ and a copper resistor has resistance $R_{Cu}$ at $0^\circ\text{C}$. Their temperature coefficients are $\alpha_C = -0.0005 \text{ } ^\circ\text{C}^{-1}$ and $\alpha_{Cu} = 0.004 \text{ } ^\circ\text{C}^{-1}$. If their series combination has a resistance independent of temperature, find the ratio of their resistances $R_C / R_{Cu}$ at $0^\circ\text{C}$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_C(T) = R_C (1 + \alpha_C T)$
- $R_{Cu}(T) = R_{Cu} (1 + \alpha_{Cu} T)$

For the series combination to be independent of temperature, the sum $R_C(T) + R_{Cu}(T)$ must not vary with $T$:
$$R_{eq}(T) = R_C + R_{Cu} + (R_C \alpha_C + R_{Cu} \alpha_{Cu}) T$$
For this to be independent of $T$, the coefficient of $T$ must be zero:
$$R_C \alpha_C + R_{Cu} \alpha_{Cu} = 0 \implies \frac{R_C}{R_{Cu}} = -\frac{\alpha_{Cu}}{\alpha_C}$$
Substituting the given values:
$$\frac{R_C}{R_{Cu}} = -\frac{0.004}{-0.0005} = \mathbf{8}$$

The ratio must be **8**.
</details>

7. 🔴 Two coils of different metals A and B have resistances of $10 \text{ } \Omega$ and $15 \text{ } \Omega$ at $0^\circ\text{C}$. If they have equal resistances at $150^\circ\text{C}$, and $\alpha_A = 0.004 \text{ } ^\circ\text{C}^{-1}$, find $\alpha_B$.

<details>
<summary><b>Answer</b></summary>

Given:
- $R_{A0} = 10 \text{ } \Omega$, $\alpha_A = 0.004 \text{ } ^\circ\text{C}^{-1}$
- $R_{B0} = 15 \text{ } \Omega$, $\alpha_B = ?$
- $R_A(150) = R_B(150)$

First calculate $R_A$ at $150^\circ\text{C}$:
$$R_A(150) = 10 \times [1 + 0.004 \times 150] = 10 \times [1 + 0.6] = 16 \text{ } \Omega$$

For coil B:
$$R_B(150) = 15 \times [1 + \alpha_B \times 150] = 16$$
$$1 + 150 \alpha_B = \frac{16}{15}$$
$$150 \alpha_B = \frac{16}{15} - 1 = \frac{1}{15}$$
$$\alpha_B = \frac{1}{150 \times 15} = \frac{1}{2250} \approx \mathbf{4.44 \times 10^{-4} \text{ } ^\circ\text{C}^{-1}}$$
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

## 🧱 Stage 4: MCQ Mastery

**Q1.** The temperature coefficient of resistance of a wire is $0.00125 \text{ } ^\circ\text{C}^{-1}$. At $300 \text{ K}$, its resistance is $1 \text{ } \Omega$. At what temperature will its resistance become $2 \text{ } \Omega$?
(a) $1100 \text{ K}$  (b) $1127 \text{ K}$  (c) $1127^\circ\text{C}$  (d) $827^\circ\text{C}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Using the temperature dependence formula:
$$R_T = R_{0}[1 + \alpha(T - T_0)]$$
Here, the reference temperature is $T_0 = 300 \text{ K} = 27^\circ\text{C}$.
We want the resistance to become $2 \text{ } \Omega$ from $1 \text{ } \Omega$:
$$2 = 1 [1 + 0.00125 (T_C - 27)]$$
$$1 = 0.00125 (T_C - 27) \implies T_C - 27 = \frac{1}{0.00125} = 800^\circ\text{C}$$
$$T_C = 800 + 27 = 827^\circ\text{C}$$

Converting this back to Kelvin:
$$T_K = 827 + 273 = \mathbf{1100 \text{ K}}$$
Alternatively, since $\Delta T$ is the same in Celsius and Kelvin, $\Delta T = 800 \text{ K}$. Hence, $T = 300 \text{ K} + 800 \text{ K} = \mathbf{1100 \text{ K}}$.
</details>

**Q2.** For a semiconductor, which of the following is true when the temperature is increased?
(a) Both number density ($n$) and relaxation time ($\tau$) increase.
(b) Both number density ($n$) and relaxation time ($\tau$) decrease.
(c) Number density ($n$) increases exponentially while relaxation time ($\tau$) decreases.
(d) Number density ($n$) decreases while relaxation time ($\tau$) increases.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

As the temperature of a semiconductor increases:
1. Thermal energy is supplied to the valence electrons, breaking covalent bonds and generating electron-hole pairs. Consequently, the carrier density $n$ increases exponentially: $n(T) \propto e^{-E_g / 2k_B T}$.
2. The thermal vibration of ions in the lattice increases, leading to more frequent collisions, which decreases the average relaxation time $\tau$.
The exponential increase in $n$ completely dominates over the minor decrease in $\tau$, causing the resistivity $\rho = \frac{m}{n e^2 \tau}$ to decrease exponentially.
</details>

**Q3.** Two resistors with temperature coefficients of resistance $\alpha_1$ and $\alpha_2$ are connected in parallel. If their resistances at $0^\circ\text{C}$ are $R_1$ and $R_2$ respectively, the effective temperature coefficient of resistance of the combination is:
(a) $\frac{\alpha_1 R_1 + \alpha_2 R_2}{R_1 + R_2}$
(b) $\frac{\alpha_1 R_2 + \alpha_2 R_1}{R_1 + R_2}$
(c) $\alpha_1 + \alpha_2$
(d) $\frac{\alpha_1 \alpha_2}{\alpha_1 + \alpha_2}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

The equivalent resistance $R_p$ in parallel is given by:
$$\frac{1}{R_p(T)} = \frac{1}{R_1(T)} + \frac{1}{R_2(T)}$$

Using the linear approximation $R(T) = R_0(1 + \alpha T)$, we write:
$$\frac{1}{R_p(0)(1 + \alpha_p T)} = \frac{1}{R_1(0)(1 + \alpha_1 T)} + \frac{1}{R_2(0)(1 + \alpha_2 T)}$$

Assuming $\alpha T \ll 1$, we can use the binomial expansion $(1 + x)^{-1} \approx 1 - x$:
$$\frac{1}{R_p(0)} (1 - \alpha_p T) \approx \frac{1}{R_1(0)} (1 - \alpha_1 T) + \frac{1}{R_2(0)} (1 - \alpha_2 T)$$

Since $\frac{1}{R_p(0)} = \frac{1}{R_1(0)} + \frac{1}{R_2(0)}$, the constant terms cancel out:
$$-\frac{\alpha_p T}{R_p(0)} = -\frac{\alpha_1 T}{R_1(0)} - \frac{\alpha_2 T}{R_2(0)} \implies \frac{\alpha_p}{R_p(0)} = \frac{\alpha_1}{R_1(0)} + \frac{\alpha_2}{R_2(0)}$$

Substituting $R_p(0) = \frac{R_1 R_2}{R_1 + R_2}$ (omitting the $(0)$ for brevity):
$$\alpha_p = R_p \left( \frac{\alpha_1 R_2 + \alpha_2 R_1}{R_1 R_2} \right) = \left( \frac{R_1 R_2}{R_1 + R_2} \right) \left( \frac{\alpha_1 R_2 + \alpha_2 R_1}{R_1 R_2} \right) = \mathbf{\frac{\alpha_1 R_2 + \alpha_2 R_1}{R_1 + R_2}}$$
</details>

**Q4.** (Statement-based Question)
**Statement I:** The temperature coefficient of resistance ($\alpha$) of a conductor is always positive, while for a semiconductor it is negative.
**Statement II:** In a conductor, the charge carrier density increases with temperature, while in a semiconductor it decreases.
(a) Both Statement I and Statement II are correct.
(b) Both Statement I and Statement II are incorrect.
(c) Statement I is correct but Statement II is incorrect.
(d) Statement I is incorrect but Statement II is correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

- **Statement I is correct**: Metals have a positive $\alpha$ because resistance increases with temperature. Semiconductors have a negative $\alpha$ because resistance decreases with temperature.
- **Statement II is incorrect**: In a metal conductor, the number density of free electrons $n$ is extremely high ($\approx 10^{29} \text{ m}^{-3}$) and remains essentially constant, independent of temperature. In a semiconductor, the charge carrier density $n$ increases exponentially with temperature as more covalent bonds are broken.
</details>

**Q5.** Which of the following graphs best represents the temperature dependence of resistivity $\rho(T)$ of a semiconductor like Silicon?
(a) A straight line with positive slope
(b) A straight line with negative slope
(c) An exponentially decreasing curve
(d) An exponentially increasing curve

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

For a semiconductor, the resistivity is given by $\rho = \frac{m}{n e^2 \tau}$. 
As temperature increases, the number density of charge carriers $n$ increases exponentially ($n \propto e^{-E_g / 2k_B T}$). Although the relaxation time $\tau$ decreases due to increased collision frequency, the exponential rise in $n$ dominates the behavior. Thus, resistivity $\rho$ decreases exponentially as temperature increases.
</details>

**Q6.** A wire of resistance $R$ is stretched to twice its original length. How does its temperature coefficient of resistance ($\alpha$) change?
(a) It becomes $4\alpha$.
(b) It becomes $2\alpha$.
(c) It becomes $\alpha/2$.
(d) It remains unchanged.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

The temperature coefficient of resistance ($\alpha$) is an intrinsic property of the material of the wire. Stretching the wire changes its length $L$ and cross-sectional area $A$, which changes its resistance $R = \rho \frac{L}{A}$. However, it does not change the material composition itself. Therefore, $\alpha$ remains completely unchanged.
</details>

**Q7.** (Assertion-Reason Question)
**Assertion (A):** The resistivity of alloys like Nichrome is relatively high and shows a very weak temperature dependence.
**Reason (R):** Alloys have highly disordered crystal lattices, which makes their resistivity high and relatively insensitive to thermal lattice vibrations.
(a) Both A and R are true and R is the correct explanation of A.
(b) Both A and R are true but R is not the correct explanation of A.
(c) A is true but R is false.
(d) A is false but R is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Alloys like Nichrome, Constantan, and Manganin are prepared by mixing different metals, resulting in a highly disordered crystal structure. This disorder scatters conduction electrons heavily even at absolute zero, giving rise to a high residual resistivity. When heated, the added scattering due to lattice vibrations is very small compared to this dominant background impurity/disorder scattering. Therefore, the temperature dependence of resistivity is extremely weak ($\alpha \approx 0$).
</details>

**Q8.** A copper wire and a silicon wire have the same resistance at $300\text{ K}$. They are cooled to $150\text{ K}$. What happens to their resistances?
(a) Resistance of both wires increases.
(b) Resistance of both wires decreases.
(c) Resistance of copper increases, while that of silicon decreases.
(d) Resistance of copper decreases, while that of silicon increases.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

- Copper is a metallic conductor. Its temperature coefficient of resistance $\alpha$ is positive. When cooled (temperature decreases), its resistance decreases.
- Silicon is a semiconductor. Its temperature coefficient of resistance $\alpha$ is negative. When cooled (temperature decreases), its carrier density $n$ drops exponentially, causing its resistance to increase.
</details>

**Q9.** For a metallic conductor, the relation between resistivity $\rho$ and relaxation time $\tau$ is $\rho \propto 1/\tau$. As the temperature of the conductor increases, the average speed of electrons ($v_{rms}$) and the mean free path ($\lambda$) change such that:
(a) $v_{rms}$ increases and $\lambda$ decreases.
(b) $v_{rms}$ decreases and $\lambda$ increases.
(c) Both $v_{rms}$ and $\lambda$ increase.
(d) Both $v_{rms}$ and $\lambda$ decrease.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

- The root-mean-square thermal speed of the electrons is $v_{rms} = \sqrt{\frac{3 k_B T}{m^*}}$, which increases with temperature $T$.
- With rising temperature, the amplitude of thermal vibrations of positive ions in the lattice increases, making them larger obstacles. This increases the probability of collision and decreases the mean free path $\lambda$ (the average distance traveled between consecutive collisions).
- Since relaxation time is $\tau = \frac{\lambda}{v_{rms}}$, an increase in $v_{rms}$ and a decrease in $\lambda$ both act to reduce $\tau$, causing resistivity $\rho$ to rise.
</details>

**Q10.** The resistance of a conductor at temperature $T$ is given by $R_T = R_0[1+\alpha(T-T_0)]$. If we choose a different reference temperature $T_1$ instead of $T_0$, the new temperature coefficient of resistance $\alpha_1$ is related to the old one $\alpha$ by:
(a) $\alpha_1 = \alpha$
(b) $\alpha_1 = \frac{\alpha}{1 + \alpha(T_1 - T_0)}$
(c) $\alpha_1 = \alpha [1 + \alpha(T_1 - T_0)]$
(d) $\alpha_1 = \frac{\alpha}{1 - \alpha(T_1 - T_0)}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

We have two equations describing the same resistance at temperature $T$:
1. $R(T) = R(T_0)[1 + \alpha(T - T_0)]$
2. $R(T) = R(T_1)[1 + \alpha_1(T - T_1)]$

Using the first equation for $T = T_1$:
$$R(T_1) = R(T_0)[1 + \alpha(T_1 - T_0)]$$

Substitute $R(T_1)$ into the second equation:
$$R(T) = R(T_0)[1 + \alpha(T_1 - T_0)][1 + \alpha_1(T - T_1)]$$

Equate this to the first expression:
$$1 + \alpha(T - T_0) = [1 + \alpha(T_1 - T_0)][1 + \alpha_1(T - T_1)]$$

Let $\Delta T_0 = T_1 - T_0$ and $\Delta T_1 = T - T_1$. Note that $T - T_0 = \Delta T_0 + \Delta T_1$:
$$1 + \alpha(\Delta T_0 + \Delta T_1) = (1 + \alpha \Delta T_0)(1 + \alpha_1 \Delta T_1)$$
$$1 + \alpha \Delta T_0 + \alpha \Delta T_1 = 1 + \alpha \Delta T_0 + \alpha_1 \Delta T_1 (1 + \alpha \Delta T_0)$$
$$\alpha \Delta T_1 = \alpha_1 \Delta T_1 (1 + \alpha \Delta T_0)$$
$$\alpha_1 = \frac{\alpha}{1 + \alpha(T_1 - T_0)}$$
</details>

**Q11.** The resistivity of a metal like Copper at temperatures below $50\text{ K}$ is best described as:
(a) Becoming zero at $0\text{ K}$ according to a linear function.
(b) Approaching a constant finite value (residual resistivity) non-linearly.
(c) Increasing exponentially.
(d) Dropping abruptly to zero at all temperatures below $50\text{ K}$.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

According to Matthiessen's rule, the total resistivity of a metal is the sum of resistivity due to thermal lattice vibrations (phonons) and resistivity due to static defects/impurities: $\rho = \rho_{\text{phonon}}(T) + \rho_{\text{defect}}$.
At extremely low temperatures ($T < 50\text{ K}$), the phonon scattering goes to zero ($\rho_{\text{phonon}} \propto T^5 \to 0$), leaving only the temperature-independent residual resistivity $\rho_{\text{defect}}$. Therefore, the resistivity levels off non-linearly to a constant non-zero value.
</details>

**Q12.** Thermistors are temperature-sensitive resistors that usually:
(a) Are made of metals with a positive temperature coefficient.
(b) Are made of oxides of transition metals with a very large negative temperature coefficient.
(c) Have a temperature coefficient that is exactly zero.
(d) Only work at absolute zero.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Thermistors (thermal resistors) are semiconductor devices typically fabricated from oxides of transition metals like manganese, nickel, cobalt, copper, and iron. They exhibit a very large negative temperature coefficient of resistance (up to $-6\% \text{ per } ^\circ\text{C}$ at room temperature), allowing them to detect minute temperature variations that would be imperceptible with ordinary metal resistors.
</details>

**Q13.** As the temperature of an electrolyte solution increases, its electrical conductivity:
(a) Decreases, because ions collide more frequently.
(b) Increases, because the viscosity of the solvent decreases and degree of ionization increases.
(c) Remains unchanged.
(d) Drops to zero because ions recombine.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

For an electrolyte solution, electrical conduction occurs due to the movement of solvated ions. As the temperature rises:
1. The viscosity of the solvent decreases, reducing the drag forces on the moving ions and increasing their mobility.
2. The thermal energy increases the dissociation of solute molecules into free ions.
Both effects lead to a significant increase in the electrical conductivity of the electrolyte, meaning its resistance decreases ($\alpha$ is negative).
</details>

**Q14.** A metallic conductor has a resistance of $R_0 = 100 \text{ } \Omega$ at $0^\circ\text{C}$. When heated to $T^\circ\text{C}$, the fractional change in resistance ($\Delta R/R_0$) is plotted against $T$. The slope of this graph represents:
(a) The resistance at $T$.
(b) The resistivity of the metal.
(c) The temperature coefficient of resistance $\alpha$.
(d) The reciprocal of $\alpha$.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The relationship for temperature dependence is:
$$R_T = R_0 (1 + \alpha T) \implies R_T - R_0 = R_0 \alpha T$$
$$\frac{\Delta R}{R_0} = \alpha T$$
If we plot $\frac{\Delta R}{R_0}$ on the y-axis and $T$ on the x-axis, we get a straight line passing through the origin. The slope of this line ($y/x$) is equal to the temperature coefficient of resistance, $\alpha$.
</details>

**Q15.** (Statement-based Question)
**Statement I:** A super-conductor exhibits zero resistivity when cooled below its critical temperature.
**Statement II:** During the transition to the superconducting state, the material expels all magnetic fields from its interior (Meissner Effect).
(a) Both Statement I and Statement II are correct.
(b) Both Statement I and Statement II are incorrect.
(c) Statement I is correct but Statement II is incorrect.
(d) Statement I is incorrect but Statement II is correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Both statements are standard definitions of superconductivity:
- **Statement I is correct**: When a superconductor is cooled below its material-specific critical temperature $T_c$, its electrical resistivity drops abruptly to exactly zero.
- **Statement II is correct**: The Meissner effect is the complete expulsion of magnetic flux lines from the interior of a superconductor as it transitions into the superconducting state. It confirms that superconductivity is a thermodynamic phase transition rather than just perfect conductivity.
</details>

**Q16.** The resistance of a conductor is $R_1$ at $t_1^\circ\text{C}$ and $R_2$ at $t_2^\circ\text{C}$. The temperature coefficient of resistance at $0^\circ\text{C}$ is:
(a) $\frac{R_2 - R_1}{R_1 t_2 - R_2 t_1}$
(b) $\frac{R_2 - R_1}{R_2 t_2 - R_1 t_1}$
(c) $\frac{R_2 - R_1}{R_1 t_1 - R_2 t_2}$
(d) $\frac{R_1 - R_2}{R_1 t_2 - R_2 t_1}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

We write the equations using $0^\circ\text{C}$ as reference:
$$R_1 = R_0(1 + \alpha t_1)$$
$$R_2 = R_0(1 + \alpha t_2)$$

Dividing the second equation by the first:
$$\frac{R_2}{R_1} = \frac{1 + \alpha t_2}{1 + \alpha t_1}$$
$$R_2(1 + \alpha t_1) = R_1(1 + \alpha t_2)$$
$$R_2 + R_2 \alpha t_1 = R_1 + R_1 \alpha t_2$$
$$R_2 - R_1 = \alpha (R_1 t_2 - R_2 t_1)$$
$$\alpha = \frac{R_2 - R_1}{R_1 t_2 - R_2 t_1}$$
</details>

**Q17.** (Assertion-Reason Question)
**Assertion (A):** The temperature coefficient of resistance of alloys like Constantan is extremely small.
**Reason (R):** Alloys have no free electrons, so temperature does not affect their conduction mechanism.
(a) Both A and R are true and R is the correct explanation of A.
(b) Both A and R are true but R is not the correct explanation of A.
(c) A is true but R is false.
(d) A is false but R is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

- **Assertion is true**: Constantan and Manganin are chosen for standard resistors specifically because their temperature coefficient $\alpha$ is near zero.
- **Reason is false**: Alloys are metal mixtures and possess a high density of free electrons, making them good conductors. The temperature independence is due to the fact that their resistivity is dominated by scattering off static lattice defects (disorder), which is independent of temperature, rather than thermal vibrations.
</details>

**Q18.** If the temperature coefficient of resistance of a material is negative and very small in magnitude, the material is likely:
(a) A highly pure metal
(b) A semiconductor
(c) An alloy with negative coefficient
(d) A superconductor

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

- A negative temperature coefficient of resistance ($\alpha < 0$) is the signature of semiconductors and insulators.
- Pure metals have positive and relatively large coefficients ($\approx 10^{-3} \text{ K}^{-1}$).
- Alloys have positive, near-zero coefficients.
- Superconductors have zero resistivity below $T_c$.
Thus, a negative coefficient immediately points to a semiconductor.
</details>

**Q19.** At $0^\circ\text{C}$, a resistor A has resistance $R$ and temperature coefficient $\alpha$. Resistor B has resistance $2R$ and temperature coefficient $2\alpha$ at $0^\circ\text{C}$. If they are connected in series, the temperature coefficient of the combination is:
(a) $1.5\alpha$  (b) $\frac{5}{3}\alpha$  (c) $1.67\alpha$  (d) Both (b) and (c) are correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

For a series combination, the equivalent resistance at temperature $T$ is:
$$R_{eq}(T) = R_1(T) + R_2(T) = R_1(1 + \alpha_1 T) + R_2(1 + \alpha_2 T)$$
$$R_{eq}(T) = (R_1 + R_2) + (R_1 \alpha_1 + R_2 \alpha_2) T$$

We also define $R_{eq}(T) = (R_1 + R_2)(1 + \alpha_{eq} T) = (R_1 + R_2) + (R_1 + R_2)\alpha_{eq} T$.
Comparing coefficients of $T$:
$$\alpha_{eq} = \frac{R_1 \alpha_1 + R_2 \alpha_2}{R_1 + R_2}$$

Substitute $R_1 = R$, $\alpha_1 = \alpha$, $R_2 = 2R$, $\alpha_2 = 2\alpha$:
$$\alpha_{eq} = \frac{R \cdot \alpha + 2R \cdot 2\alpha}{R + 2R} = \frac{5 R \alpha}{3 R} = \frac{5}{3}\alpha \approx 1.67\alpha$$
Therefore, both (b) and (c) are correct expressions of the same answer.
</details>

**Q20.** A metallic wire has resistance $R$. It is cut into three equal pieces and they are connected in parallel. What is the temperature coefficient of resistance of this parallel combination?
(a) $\alpha/3$
(b) $3\alpha$
(c) $\alpha$
(d) $\alpha/9$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Each of the three pieces has resistance $R/3$ and temperature coefficient of resistance $\alpha$ (since they are made of the same material). 
When identical resistors are combined in parallel, the equivalent resistance at temperature $T$ is:
$$R_p(T) = \frac{R'(T)}{3} = \frac{R'(0)(1 + \alpha T)}{3} = R_p(0)(1 + \alpha T)$$
Comparing this to $R_p(T) = R_p(0)(1 + \alpha_{eq} T)$, we find that $\alpha_{eq} = \alpha$. In general, any parallel or series combination of resistors made of the same material will have an equivalent temperature coefficient of resistance equal to the individual coefficient $\alpha$.
</details>

---

## 🔀 Stage 5: Type Mixer

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

## 📋 Stage 6: Board Arsenal

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

## 🚀 Stage 7: JEE Mains Arena

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

