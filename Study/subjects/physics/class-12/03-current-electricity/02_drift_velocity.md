# Chapter 2: Drift Velocity, Mobility & Current Density

> *NCERT Sections 3.3, 3.5*

---

## 🎯 Stage 1: The Core Idea

### The Chaotic Life of an Electron

Inside a metallic conductor at room temperature, free electrons are not sitting still. They behave like molecules in a gas, zooming around randomly in all directions at terrifying speeds (about $10^5 \text{ to } 10^6 \text{ m/s}$). This is called their **thermal velocity**.

Because their motion is completely random, for every electron moving right, there is one moving left. 
**Result:** The *average* thermal velocity of all electrons is **zero**. There is no net flow of charge, and hence, no electric current.

### Enter the Electric Field (The Battery)

When you connect a battery across the conductor, an electric field ($\vec{E}$) is established. This field exerts a force ($\vec{F} = -e\vec{E}$) on every free electron.

Now, on top of their chaotic random motion, all the electrons start to slowly "drift" in a direction opposite to the electric field. This slow, collective shift is called **drift velocity ($v_d$)**. 

> **Analogy:** Think of a swarm of bees buzzing around chaotically. If a gentle breeze starts blowing, the entire swarm slowly drifts with the wind, even though individual bees are still flying rapidly in all directions. The buzzing is thermal velocity; the slow movement of the swarm is drift velocity.

Drift velocity is shockingly slow — typically around $10^{-4} \text{ m/s}$ (a fraction of a millimeter per second). Yet, when you flip a switch, the bulb lights up instantly because the electric field travels through the wire at nearly the speed of light, setting all electrons drifting simultaneously.

### Collisions and Relaxation Time

As electrons drift, they constantly collide with the heavy, vibrating positive ions of the metal lattice. After each collision, they lose their acquired velocity and have to start accelerating again.

The average time interval between two successive collisions is called the **relaxation time ($\tau$)**.

---

## 🔬 Stage 2: The Formula Lab

### 1. Drift Velocity Formula

The force on an electron is $\vec{F} = -e\vec{E}$. Its acceleration is $\vec{a} = \frac{-e\vec{E}}{m}$.
The average velocity acquired between collisions is $\vec{v}_d = \vec{a}\tau$.

$$\vec{v}_d = -\frac{e\vec{E}}{m}\tau$$
$$v_d = \frac{eE}{m}\tau \quad \text{(Magnitude)}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $v_d$ | Drift velocity | m/s |
| $e$ | Charge of an electron | $1.6 \times 10^{-19}$ C |
| $E$ | Electric field intensity | V/m or N/C |
| $m$ | Mass of an electron | $9.1 \times 10^{-31}$ kg |
| $\tau$ | Relaxation time | s |

### 2. Current and Drift Velocity Relation ⭐

$$I = nAev_d$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $I$ | Electric current | A |
| $n$ | Number density of free electrons (electrons per unit volume) | $\text{m}^{-3}$ |
| $A$ | Cross-sectional area of the conductor | $\text{m}^2$ |

*Note: Since $E = V/L$ (where $V$ is potential difference and $L$ is length), we can also write $v_d = \frac{eV\tau}{mL}$.*

### 3. Current Density ($J$)

Current ($I$) is a scalar, but sometimes we need to talk about the flow of charge *at a specific point* and in a specific direction. For this, we use **Current Density ($\vec{J}$)**, which is a vector.

$$J = \frac{I}{A} = nev_d$$

Unit: $\text{A/m}^2$. Its direction is the same as the direction of conventional current (direction of $\vec{E}$).

### 4. Mobility ($\mu$)

How easily can an electron drift when an electric field is applied? This is measured by mobility. It is defined as the magnitude of drift velocity per unit electric field.

$$\mu = \frac{v_d}{E} = \frac{e\tau}{m}$$

Unit: $\text{m}^2/\text{V}\cdot\text{s}$. Mobility is always positive.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic $v_d$ and $I$ calculation ⭐

**Pattern:** "Given dimensions, carrier density, and current, find drift velocity."

**Solved Example** 🟢

> A copper wire of cross-sectional area $1.0 \times 10^{-6} \text{ m}^2$ carries a current of $1.6 \text{ A}$. If the free electron density is $10^{29} \text{ m}^{-3}$, calculate the drift velocity of electrons.

<details>
<summary><b>Solution</b></summary>

Using $I = nAev_d$:
$$v_d = \frac{I}{nAe}$$
$$v_d = \frac{1.6}{10^{29} \times 1.0 \times 10^{-6} \times 1.6 \times 10^{-19}}$$
$$v_d = \frac{1.6}{1.6 \times 10^4} = 10^{-4} \text{ m/s}$$
</details>

**Practice:**

1. 🟢 Find the drift velocity in a silver wire of area $2 \times 10^{-6} \text{ m}^2$ carrying $3.2 \text{ A}$. Given $n = 5 \times 10^{28} \text{ m}^{-3}$.

<details>
<summary><b>Answer</b></summary>

$v_d = I / (nAe) = 3.2 / (5 \times 10^{28} \times 2 \times 10^{-6} \times 1.6 \times 10^{-19}) = 3.2 / (16 \times 10^3) = 2 \times 10^{-4} \text{ m/s}$
</details>

2. 🟡 A wire has $v_d = 0.5 \text{ mm/s}$ when carrying $2 \text{ A}$. What will be the drift velocity if the current is increased to $6 \text{ A}$ (assuming same temperature)?

<details>
<summary><b>Answer</b></summary>

$v_d \propto I$. If current is tripled ($2 \text{ A} \rightarrow 6 \text{ A}$), $v_d$ also triples.
$v_d' = 3 \times 0.5 = 1.5 \text{ mm/s}$.
</details>

3. 🟡 Calculate the current in a wire of radius $1 \text{ mm}$ if electron density is $8 \times 10^{28} \text{ m}^{-3}$ and drift velocity is $0.1 \text{ mm/s}$.

<details>
<summary><b>Answer</b></summary>

$A = \pi r^2 = 3.14 \times (10^{-3})^2 = 3.14 \times 10^{-6} \text{ m}^2$.
$v_d = 10^{-4} \text{ m/s}$.
$I = nAev_d = 8 \times 10^{28} \times 3.14 \times 10^{-6} \times 1.6 \times 10^{-19} \times 10^{-4} \approx 4.02 \text{ A}$.
</details>

---

### Type 2: Effect of changing dimensions on $v_d$ ⭐⭐

**Pattern:** "A wire's radius/length is doubled. How does drift velocity change?"
*Crucial: Check if Current ($I$) is constant or Voltage ($V$) is constant!*

**Solved Example** 🔴

> A steady current flows in a uniform wire. If the wire is replaced by another of the same material and same length but double the radius, how does the drift velocity change, assuming the same current flows?

<details>
<summary><b>Solution</b></summary>

Case 1: **Current ($I$) is constant.**
We know $v_d = \frac{I}{nAe} \implies v_d \propto \frac{1}{A} \propto \frac{1}{r^2}$.
If radius is doubled ($r' = 2r$), Area becomes 4 times ($A' = 4A$).
Therefore, $v_d' = v_d / 4$.
The new drift velocity is **one-fourth** the original.
</details>

**Practice:**

1. 🟡 A battery of constant voltage $V$ is connected across a wire of length $L$. If the length is doubled ($2L$), how does $v_d$ change?

<details>
<summary><b>Answer</b></summary>

Here **Voltage ($V$) is constant**.
Use $v_d = \frac{eE}{m}\tau = \frac{eV}{mL}\tau$.
Since $v_d \propto \frac{1}{L}$, doubling the length makes drift velocity **half** ($v_d/2$).
</details>

2. 🔴 Two wires of same material have lengths in ratio 1:2 and radii in ratio 1:2. They are connected in series. Find ratio of their drift velocities.

<details>
<summary><b>Answer</b></summary>

In series, **Current ($I$) is same**.
$v_d \propto \frac{1}{A} \propto \frac{1}{r^2}$. Length doesn't matter here!
$(v_{d1} / v_{d2}) = (r_2 / r_1)^2 = (2 / 1)^2 = 4:1$.
</details>

3. 🔴 The same two wires (lengths 1:2, radii 1:2) are connected in parallel across a battery. Find ratio of drift velocities.

<details>
<summary><b>Answer</b></summary>

In parallel, **Voltage ($V$) is same**.
$v_d = \frac{eV}{mL}\tau \implies v_d \propto \frac{1}{L}$. Radius doesn't matter here!
$(v_{d1} / v_{d2}) = (L_2 / L_1) = 2:1$.
</details>

---

### Type 3: Non-uniform cross-section

**Pattern:** "A wire tapers from radius $r_1$ to $r_2$. Which quantities change and how?"

**Solved Example** 🟡

> A steady current flows through a metallic wire whose area of cross-section increases continuously from one end to the other. Which of the following quantities remains constant: drift velocity, current, or current density?

<details>
<summary><b>Solution</b></summary>

- **Current ($I$):** Must be **constant** due to conservation of charge (what goes in must come out).
- **Current Density ($J$):** $J = I/A$. As Area increases, $J$ **decreases**.
- **Drift Velocity ($v_d$):** $v_d = I/(nAe) \implies v_d \propto 1/A$. As Area increases, $v_d$ **decreases**.

Only **current** remains constant.
</details>

**Practice:**

1. 🟡 In a tapered wire, electron drift velocity at the narrower end is $v$. What is it at a point where the diameter is twice as large?

<details>
<summary><b>Answer</b></summary>

Diameter is twice $\rightarrow$ Radius is twice $\rightarrow$ Area is 4 times.
Since $v_d \propto 1/A$, the drift velocity becomes **$v/4$**.
</details>

---

### Type 4: Current Density and Electric Field

**Pattern:** "Use $J = nev_d$ or relate $J$ to $E$."

**Solved Example** 🟡

> Calculate the current density in a wire of radius $2 \text{ mm}$ carrying a current of $5 \text{ A}$.

<details>
<summary><b>Solution</b></summary>

$A = \pi r^2 = \pi \times (2 \times 10^{-3})^2 = 4\pi \times 10^{-6} \text{ m}^2$
$J = I/A = 5 / (4\pi \times 10^{-6}) \approx 3.98 \times 10^5 \text{ A/m}^2$
</details>

**Practice:**

1. 🟢 If current density in a wire is $10^6 \text{ A/m}^2$, and free electron density is $10^{29} \text{ m}^{-3}$, find drift velocity.

<details>
<summary><b>Answer</b></summary>

$J = nev_d \implies v_d = J / (ne) = 10^6 / (10^{29} \times 1.6 \times 10^{-19}) = 10^6 / (1.6 \times 10^{10}) = 6.25 \times 10^{-5} \text{ m/s}$.
</details>

---

### Type 5: Mobility and Relaxation Time

**Pattern:** "Calculate $\mu$ or $\tau$, or find their ratio."

**Solved Example** 🟡

> The drift velocity of electrons in a metal is $1.5 \times 10^{-4} \text{ m/s}$ under an electric field of $3 \times 10^{-2} \text{ V/m}$. Calculate the mobility of electrons.

<details>
<summary><b>Solution</b></summary>

$\mu = v_d / E = (1.5 \times 10^{-4}) / (3 \times 10^{-2}) = 0.5 \times 10^{-2} = \mathbf{5 \times 10^{-3} \text{ m}^2/\text{V}\cdot\text{s}}$
</details>

**Practice:**

1. 🟡 If the relaxation time of electrons in a metal is $3 \times 10^{-14} \text{ s}$, calculate their mobility. ($m = 9.1 \times 10^{-31} \text{ kg}$)

<details>
<summary><b>Answer</b></summary>

$\mu = e\tau / m = (1.6 \times 10^{-19} \times 3 \times 10^{-14}) / (9.1 \times 10^{-31}) \approx 5.27 \times 10^{-3} \text{ m}^2/\text{V}\cdot\text{s}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A copper wire of length $L$ and radius $r$ is connected to a battery of voltage $V$. If the wire is stretched to double its length (volume remains constant), how do the following change? (a) Drift velocity, (b) Current density.

<details>
<summary><b>Solution</b></summary>

Volume constant $\implies A_{initial} L = A_{final} (2L) \implies A_{final} = A/2$.
We also know Electric field $E = V/L$. Since length doubles, $E_{new} = V/(2L) = E/2$.

(a) Drift velocity $v_d = \frac{eE}{m}\tau$. Since $E$ becomes half, $v_d$ becomes **half**.
(b) Current density $J = nev_d$. Since $v_d$ becomes half, $J$ becomes **half**.

*(Note: We could also use $I = V/R$. $R_{new} = \rho(2L)/(A/2) = 4R$. $I_{new} = V/4R = I/4$. Then $J = I_{new}/A_{new} = (I/4)/(A/2) = I/2A = J/2$.)*
</details>

**Q2.** 🔴 ⭐ An electron beam has an aperture of $1 \text{ mm}^2$. A total of $6 \times 10^{16}$ electrons go through any perpendicular cross-section per second. Find (a) the current, (b) the current density.

<details>
<summary><b>Solution</b></summary>

(a) $I = q/t = (n_{total})e/t = 6 \times 10^{16} \times 1.6 \times 10^{-19} = \mathbf{9.6 \times 10^{-3} \text{ A} = 9.6 \text{ mA}}$.
(b) $J = I/A = 9.6 \times 10^{-3} / 10^{-6} = \mathbf{9600 \text{ A/m}^2}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Define drift velocity and relaxation time. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Drift Velocity:** The average velocity with which free electrons in a conductor get drifted towards the positive end of the conductor under the influence of an applied external electric field.

**Relaxation Time:** The average time interval between two successive collisions of a free electron with the positive ions in a conductor.
</details>

**Q2.** 🟡 ⭐ Derive the relation $\vec{v}_d = -\frac{e\vec{E}}{m}\tau$. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

When an electric field $\vec{E}$ is applied, force on an electron is $\vec{F} = -e\vec{E}$.
Acceleration of electron $\vec{a} = \frac{\vec{F}}{m} = -\frac{e\vec{E}}{m}$.
Let $\vec{u}_1, \vec{u}_2 \dots \vec{u}_n$ be the initial random thermal velocities of $n$ electrons. Their average is zero: $\frac{1}{n}\sum \vec{u}_i = 0$.
Velocity of $i^{th}$ electron after time $t_i$ (time since last collision) is $\vec{v}_i = \vec{u}_i + \vec{a}t_i$.
Drift velocity is the average of all these velocities:
$\vec{v}_d = \frac{1}{n} \sum (\vec{u}_i + \vec{a}t_i) = \frac{1}{n}\sum \vec{u}_i + \vec{a} \left(\frac{1}{n}\sum t_i\right)$
Since average thermal velocity is zero and $\frac{1}{n}\sum t_i = \tau$ (relaxation time):
$\vec{v}_d = 0 + \vec{a}\tau = -\frac{e\vec{E}}{m}\tau$.
</details>

**Q3.** 🟡 ⭐ Establish the relation between electric current and drift velocity. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

Consider a conductor of length $L$ and uniform cross-sectional area $A$.
Volume of the conductor = $AL$.
Let $n$ be the number of free electrons per unit volume.
Total number of free electrons = $nAL$.
Total charge of these electrons $Q = (nAL)e$.
Time taken by electrons to cross the length $L$ with drift velocity $v_d$ is $t = \frac{L}{v_d}$.
Current $I = \frac{Q}{t} = \frac{nALe}{L/v_d} = nAev_d$.
</details>

**Q4.** 🟡 Define mobility of a charge carrier. Write its SI unit. How does mobility of electrons in a metallic conductor vary with temperature? *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Mobility ($\mu$)** is defined as the magnitude of drift velocity per unit electric field applied. $\mu = v_d / E$.
**SI Unit:** $\text{m}^2/\text{V}\cdot\text{s}$ (or $\text{m}^2\text{C}/\text{J}\cdot\text{s}$).
**Effect of temperature:** $\mu = e\tau/m$. As temperature increases, the thermal speed of electrons increases, causing them to collide more frequently with lattice ions. This decreases the relaxation time ($\tau$). Therefore, mobility **decreases** with an increase in temperature.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ A current $I$ flows through a uniform wire of diameter $d$ when the mean electron drift velocity is $v$. The same current will flow through a wire of diameter $d/2$ made of the same material if the mean drift velocity of the electron is:

(a) $v/4$ &emsp; (b) $v/2$ &emsp; (c) $2v$ &emsp; (d) $4v$

<details>
<summary><b>Answer</b></summary>

$I = nAev_d \implies v_d = \frac{I}{nAe} \propto \frac{1}{A} \propto \frac{1}{d^2}$ (since $I$ and material are same).
If diameter becomes $d/2$, area becomes $A/4$.
So new drift velocity must be $4 \times$ the original to maintain the same current.
$v_d' = 4v$.

**Answer: (d)**
</details>

**Q2.** 🔴 The drift velocity of free electrons in a conductor is $v$ when a current $I$ is flowing in it. If both the radius and current are doubled, then drift velocity will be:

(a) $v/4$ &emsp; (b) $v/2$ &emsp; (c) $v$ &emsp; (d) $2v$

<details>
<summary><b>Answer</b></summary>

$v_d = \frac{I}{nAe} = \frac{I}{n\pi r^2 e}$
$v_d \propto \frac{I}{r^2}$
$v_d' \propto \frac{2I}{(2r)^2} = \frac{2I}{4r^2} = \frac{1}{2} \left(\frac{I}{r^2}\right)$
$v_d' = v/2$.

**Answer: (b)**
</details>

**Q3.** 🔴 ⭐ When a potential difference $V$ is applied across a conductor of length $l$, the drift velocity is $v_d$. If the potential difference is doubled and the length is halved, the drift velocity will become:

(a) $v_d$ &emsp; (b) $2v_d$ &emsp; (c) $4v_d$ &emsp; (d) $v_d/4$

<details>
<summary><b>Answer</b></summary>

$v_d = \frac{eV\tau}{ml}$
$v_d \propto \frac{V}{l}$
$v_d' \propto \frac{2V}{l/2} = 4 \left(\frac{V}{l}\right)$
$v_d' = 4v_d$.

**Answer: (c)**
</details>

**Q4.** 🔴 A wire of length $L$ and 3 identical cells of negligible internal resistance are connected in series. Due to the current, the drift velocity of free electrons is $v$. If the length of the wire is reduced to $L/2$ and only 2 cells are used, the new drift velocity will be:

(a) $v$ &emsp; (b) $\frac{4}{3}v$ &emsp; (c) $\frac{3}{4}v$ &emsp; (d) $\frac{2}{3}v$

<details>
<summary><b>Answer</b></summary>

$v_d \propto E \propto \frac{V}{L}$.
Initial state: $V_{initial} = 3E_{cell}$, $L_{initial} = L$. So $v \propto \frac{3E_{cell}}{L}$.
Final state: $V_{final} = 2E_{cell}$, $L_{final} = L/2$. So $v' \propto \frac{2E_{cell}}{L/2} = \frac{4E_{cell}}{L}$.
Ratio: $\frac{v'}{v} = \frac{4}{3} \implies v' = \frac{4}{3}v$.

**Answer: (b)**
</details>

---

*Next: [Chapter 3 — Ohm's Law — The Linear Relationship →](./03_ohms_law.md)*
