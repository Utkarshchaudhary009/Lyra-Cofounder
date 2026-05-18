# Chapter 3: Ohm's Law — The Linear Relationship

> *NCERT Section 3.4*

---

## 🎯 Stage 1: The Core Idea

### The Water Pipe Analogy

Imagine water flowing through a horizontal pipe. 
- The **current ($I$)** is the amount of water flowing per second.
- The **potential difference ($V$)** is the pressure difference between the two ends of the pipe (maybe created by a pump).
- The **resistance ($R$)** is the pipe's opposition to flow (is the pipe narrow?<br> Is it clogged?<br>).

If you increase the pressure ($V$), more water flows ($I$). If you double the pressure, the flow doubles. They are directly proportional.

This is exactly what Georg Simon Ohm discovered in 1828 for electrical circuits.

### Ohm's Law Statement

> **If physical conditions (like temperature, mechanical strain, etc.) remain constant, the current flowing through a conductor is directly proportional to the potential difference applied across its ends.**

$$V \propto I \implies V = IR$$

Where $R$ is a constant of proportionality called the **Resistance** of the conductor. 
It represents the opposition offered by the conductor to the flow of electric current (due to collisions of electrons with positive ions).

### The Microscopic View (Vector Form)

While $V = IR$ is the macroscopic form we use in circuits, what happens inside the metal?<br> 
The electric field ($\vec{E}$) drives the current density ($\vec{J}$). 

> **$\vec{J} = \sigma \vec{E}$**

Where $\sigma$ is the **Conductivity** of the material (how easily it allows current to flow). This is the fundamental, microscopic form of Ohm's Law.

---

## 🔬 Stage 2: The Formula Lab

### 1. Macroscopic Ohm's Law

$$V = IR$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $V$ | Potential Difference | Volt (V) |
| $I$ | Electric Current | Ampere <br>
(A) |
| $R$ | Resistance | Ohm ($\Omega$) |

**Definition of 1 Ohm:** The resistance of a conductor is 1 ohm if a current of 1 ampere flows through it when a potential difference of 1 volt is applied across it. ($1 \text{ } \Omega = 1 \text{ V/A}$)

### 2. Conductance ($G$)

Conductance is the reciprocal of resistance. It tells you how easily a wire allows current to pass.

$$G = \frac{1}{R}$$

Unit: $\text{Ohm}^{-1}$ ($\Omega^{-1}$) or **Siemens (S)** or **mho ($\mho$)**.

### 3. Microscopic Ohm's Law

$$J = \sigma E$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $J$ | Current density ($I/A$) | $\text{A/m}^2$ |
| $\sigma$ | Conductivity ($1/\rho$) | $\text{S/m}$ or $\Omega^{-1}\text{m}^{-1}$ |
| $E$ | Electric field ($V/L$) | $\text{V/m}$ |

*Derivation connection:* We know $v_d = \frac{eE\tau}{m}$ and $J = nev_d$. 
Substituting $v_d$: $J = ne \left(\frac{eE\tau}{m}\right) = \left(\frac{ne^2\tau}{m}\right)E$.
So, $\sigma = \frac{ne^2\tau}{m}$.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Direct $V=IR$ Calculations ⭐

**Pattern:** "Given two of $V, I, R$, find the third."

**Solved Example** 🟢

> A heating element has a resistance of $150 \text{ } \Omega$ and draws a current of $1.5 \text{ A}$. What is the voltage of the supply?<br>

<details>
<summary><b>Solution</b></summary>

$V = IR = 1.5 \times 150 = \mathbf{225 \text{ V}}$
</details>

**Practice:**

1. 🟢 A car headlight operates on a $12 \text{ V}$ battery and draws $2.5 \text{ A}$. Find its resistance.

<details>
<summary><b>Answer</b></summary>

$R = V/I = 12 / 2.5 = \mathbf{4.8 \text{ } \Omega}$
</details>

2. 🟢 How much current will a $20 \text{ } \Omega$ resistor draw when connected to a $5 \text{ V}$ source?<br>

<details>
<summary><b>Answer</b></summary>

$I = V/R = 5 / 20 = \mathbf{0.25 \text{ A}}$
</details>

3. 🟡 An electrical appliance has a resistance of $25 \text{ } \Omega$. When connected to a $230 \text{ V}$ supply, calculate the current drawn and the conductance.

<details>
<summary><b>Answer</b></summary>

$I = V/R = 230 / 25 = \mathbf{9.2 \text{ A}}$
Conductance $G = 1/R = 1/25 = \mathbf{0.04 \text{ S}}$ (Siemens)
</details>

---

### Type 2: $V-I$ Graph Interpretation ⭐⭐

**Pattern:** "Given a $V-I$ or $I-V$ graph, find resistance or compare resistances."

**Important Rule:** 
- In a $V \text{ vs } I$ graph (V on y-axis, I on x-axis), the slope $\tan(\theta) = V/I = R$. Steeper line = higher resistance.
- In an $I \text{ vs } V$ graph (I on y-axis, V on x-axis), the slope $\tan(\theta) = I/V = 1/R$. Steeper line = lower resistance.

**Solved Example** 🟡

> The $V-I$ graph for two metallic wires $A$ and $B$ at constant temperature are straight lines. The line for wire $A$ is steeper (makes a larger angle with the $I$-axis). Which wire has higher resistance?<br>

<details>
<summary><b>Solution</b></summary>

Since it is a $V-I$ graph (V on y, I on x), the slope represents Resistance ($R = V/I$).
Wire $A$ has a steeper slope, meaning larger $V/I$ ratio.
Therefore, **Wire $A$ has higher resistance.**
</details>

**Practice:**

1. 🟡 In an $I-V$ graph (Current on y-axis, Voltage on x-axis), curve $P$ is steeper than curve $Q$. Which has higher resistance?<br>

<details>
<summary><b>Answer</b></summary>

Slope of $I-V$ graph is $1/R$. Steeper slope means higher conductance ($1/R$) and therefore **lower resistance**.
So, $P$ has lower resistance. **$Q$ has higher resistance.**
</details>

2. 🔴 A $V-I$ graph for a conductor at temperature $T_1$ makes an angle of $30^\circ$ with the $I$-axis. At temperature $T_2$, it makes an angle of $60^\circ$ with the $I$-axis. Find the ratio of resistances $R_1 : R_2$.

<details>
<summary><b>Answer</b></summary>

$R = \text{slope} = \tan(\theta)$.
$R_1 = \tan(30^\circ) = 1/\sqrt{3}$.
$R_2 = \tan(60^\circ) = \sqrt{3}$.
$R_1 : R_2 = (1/\sqrt{3}) / \sqrt{3} = \mathbf{1:3}$.
</details>

---

### Type 3: Microscopic Ohm's Law Calculations

**Pattern:** "Given $E$ and $J$, find $\sigma$ or $\rho$, or verify $J = \sigma E$."

**Solved Example** 🟡

> The electric field inside a copper wire is $0.05 \text{ V/m}$ and the current density is $2.5 \times 10^6 \text{ A/m}^2$. Calculate the conductivity and resistivity of copper.

<details>
<summary><b>Solution</b></summary>

From microscopic Ohm's law: $J = \sigma E$
Conductivity $\sigma = J / E = (2.5 \times 10^6) / 0.05 = \mathbf{5 \times 10^7 \text{ S/m}}$
Resistivity $\rho = 1 / \sigma = 1 / (5 \times 10^7) = \mathbf{2 \times 10^{-8} \text{ } \Omega\cdot\text{m}}$
</details>

**Practice:**

1. 🟡 A wire has conductivity $6 \times 10^7 \text{ S/m}$. If an electric field of $0.1 \text{ V/m}$ is applied, find the current density.

<details>
<summary><b>Answer</b></summary>

$J = \sigma E = (6 \times 10^7) \times 0.1 = \mathbf{6 \times 10^6 \text{ A/m}^2}$
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A potential difference of $10 \text{ V}$ is applied across a uniform wire of length $2 \text{ m}$ and cross-sectional area $10^{-6} \text{ m}^2$. If the current flowing is $2 \text{ A}$, find: (a) resistance, (b) electric field inside the wire, (c) current density, and (d) conductivity of the material. Verify $J = \sigma E$.

<details>
<summary><b>Solution</b></summary>

(a) Resistance $R = V/I = 10 / 2 = \mathbf{5 \text{ } \Omega}$.
(b) Electric field $E = V/L = 10 / 2 = \mathbf{5 \text{ V/m}}$.
(c) Current density $J = I/A = 2 / 10^{-6} = \mathbf{2 \times 10^6 \text{ A/m}^2}$.
(d) We know $R = \rho L/A \implies \rho = RA/L = (5 \times 10^{-6}) / 2 = 2.5 \times 10^{-6} \text{ } \Omega\cdot\text{m}$.
    Conductivity $\sigma = 1/\rho = 1 / (2.5 \times 10^{-6}) = \mathbf{4 \times 10^5 \text{ S/m}}$.

Verify: $\sigma E = (4 \times 10^5) \times 5 = 20 \times 10^5 = 2 \times 10^6 \text{ A/m}^2 = J$. (Verified!)
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 State Ohm's law. Are there materials that do not obey Ohm's law?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Ohm's Law:** It states that if physical conditions (like temperature, pressure, etc.) remain unchanged, the current flowing through a conductor is directly proportional to the potential difference applied across its ends ($V \propto I$ or $V = IR$).

Yes, there are materials and devices that do not obey Ohm's law. They are called non-ohmic devices. Examples include semiconductor diodes, transistors, thermistors, and electrolytes.
</details>

**Q2.** 🟡 Derive the vector form of Ohm's law ($\vec{J} = \sigma\vec{E}$). *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

We know the relation between current and drift velocity: $I = nAev_d$
And drift velocity is given by: $v_d = \frac{eE\tau}{m}$
Substituting $v_d$ in the first equation:
$$I = nAe \left(\frac{eE\tau}{m}\right) = \left(\frac{ne^2\tau}{m}\right) AE$$
Current density $J = I/A$. Therefore:
$$J = \left(\frac{ne^2\tau}{m}\right) E$$
The term $\left(\frac{ne^2\tau}{m}\right)$ is constant for a given material at constant temperature and is called conductivity ($\sigma$).
Hence, $J = \sigma E$.
In vector form, since current density $\vec{J}$ is in the direction of the electric field $\vec{E}$, we write:
**$\vec{J} = \sigma\vec{E}$**
</details>

**Q3.** 🟡 Why is Ohm's law not a universal law?<br> *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

Ohm's law is not a fundamental or universal law of nature (like Newton's laws of gravitation) because it depends on the properties of specific materials. Many materials and devices (like semiconductors, discharge tubes) exhibit a non-linear relationship between $V$ and $I$, thereby violating Ohm's law.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ Two wires $A$ and $B$ of the same material have their lengths in the ratio $1:2$ and radii in the ratio $2:1$. The two wires are connected in parallel across a battery. The ratio of the currents in $A$ and $B$ ($I_A : I_B$) is:

(a) 1:8 &emsp; (b) 8:1 &emsp; (c) 1:4 &emsp; (d) 4:1

<details>
<summary><b>Answer</b></summary>

Resistance $R = \rho L/A = \rho L / (\pi r^2)$. So $R \propto L/r^2$.
$R_A \propto L_A / r_A^2 = 1 / 2^2 = 1/4$
$R_B \propto L_B / r_B^2 = 2 / 1^2 = 2$
Ratio of resistances: $R_A / R_B = (1/4) / 2 = 1/8$.

In parallel, Voltage ($V$) is same. So $I = V/R \implies I \propto 1/R$.
$I_A / I_B = R_B / R_A = 8/1$.

**Answer: (b)**
</details>

**Q2.** 🔴 A steady current flows in a metallic conductor of non-uniform cross-section. Which of the following quantities is constant along the conductor?<br>

(a) Current density &emsp; (b) Electric field &emsp; (c) Drift speed &emsp; (d) Current

<details>
<summary><b>Answer</b></summary>

In a series circuit (which a single wire is, even if tapered), the rate of flow of charge must be constant everywhere to prevent charge accumulation. Thus, **current ($I$) is constant**.
Since $A$ varies, $J = I/A$ varies.
Since $v_d = I/(nAe)$, $v_d$ varies.
Since $E = J/\sigma$, $E$ varies.

**Answer: (d)**
</details>

**Q3.** 🔴 ⭐ An electric field of $100 \text{ V/m}$ is applied to a sample of n-type semiconductor whose Hall coefficient is $-0.0125 \text{ m}^3/\text{C}$. Find the current density if the mobility of electrons is $0.36 \text{ m}^2/\text{V}\cdot\text{s}$. (Assume current is entirely due to electrons).

(a) $2880 \text{ A/m}^2$ &emsp; (b) $288 \text{ A/m}^2$ &emsp; (c) $1440 \text{ A/m}^2$ &emsp; (d) $5760 \text{ A/m}^2$

<details>
<summary><b>Answer</b></summary>

Hall coefficient $R_H = -1/(ne)$. Thus $1/(ne) = 0.0125 \implies ne = 1/0.0125 = 80 \text{ C/m}^3$.
We know $J = nev_d$.
Also mobility $\mu = v_d / E \implies v_d = \mu E$.
So, $J = ne(\mu E) = (80) \times 0.36 \times 100 = 80 \times 36 = \mathbf{2880 \text{ A/m}^2}$.

**Answer: (a)**
*Note: This touches upon a slightly advanced concept (Hall effect) that occasionally appears in JEE.*
</details>

---

*Next: [Chapter 4 — Resistance & Resistivity →](./04_resistance_resistivity.md)*
