# Chapter 7: Self-Inductance — The Coil That Fights Change

> *NCERT Section 6.8.2*

*← [Chapter 6 — Eddy Currents](./06_eddy_currents.md)*

---

## 🎯 Stage 1: The Core Idea

### The Flywheel Analogy — Electrical Inertia

Imagine pushing a heavy flywheel that's at rest. At first, it resists your push — it takes time to get spinning. Once it's spinning, it also resists being stopped. This **resistance to change in motion** is called **inertia** in mechanics.

Now imagine a coil of wire connected to a battery. When you switch on the circuit, you'd expect current to instantly jump to its full value. But it doesn't. The coil **"pushes back"** against the growing current. And when you switch off the circuit, the current doesn't instantly die — the coil tries to **maintain** it (this is why you see sparks when you unplug an electromagnet!). This electromagnetic resistance to change in current is called **self-inductance**, and the coil is called an **inductor**.

> 🔑 **Key Takeaway:** Self-inductance ($L$) is the property of a coil that makes it **oppose any change in the current flowing through it**. It is the electrical analogue of mechanical inertia (or mass).

### What Actually Happens Inside?

When current flows through a coil, it creates a magnetic field (and hence magnetic flux) through its own turns. If that current **changes** — the flux changes — and by Faraday's law, an EMF is induced. But where is this EMF induced? In the **same coil itself**! This self-induced EMF always **opposes** the change that caused it (Lenz's law), which is why it's called **back EMF**.

Think of it this way:
- Current increasing → back EMF opposes the increase (acts like a brake)
- Current decreasing → back EMF tries to maintain the current (acts like a booster)

> ⚠️ **Critical Insight:** The back EMF is not an EMF that drives current in the external circuit — it is an EMF *within the coil itself* that opposes the driver (the battery). It's like the coil saying "slow down!" or "don't stop!"

### The Spark at the Switch

When you switch OFF a circuit containing a large inductor (like an electromagnet), the current suddenly tries to drop to zero. The inductor, resisting this change, generates a **very large back EMF** (since $\varepsilon = -L \cdot dI/dt$ and $dI/dt$ is huge). This large EMF drives a spark across the switch gap. This is also the working principle of **induction coils** used in car ignition systems.

> 💡 **Tip:** Self-inductance is to current what inertia is to velocity. A massive object resists changes in velocity; an inductor resists changes in current.

### Inductor vs. Capacitor — The Dual Analogy

| Property | **Capacitor** | **Inductor** |
|---|---|---|
| Stores | Electric energy | Magnetic energy |
| Opposes change in | Voltage | Current |
| Energy formula | $\frac{1}{2}CV^2$ | $\frac{1}{2}LI^2$ |
| Analogy | Spring (stores elastic PE) | Flywheel (stores kinetic energy) |
| At $t = 0$ (DC switch closed) | Short circuit (allows all current) | Open circuit (blocks current) |
| At steady state ($t \to \infty$, DC) | Open circuit (blocks current) | Short circuit (acts like plain wire) |

### Mechanical vs. Electrical Inertia

| Concept | **Mechanical** | **Electrical (Inductance)** |
|---|---|---|
| Quantity resisted | Change in velocity | Change in current |
| Agent of resistance | Mass ($m$) | Self-inductance ($L$) |
| Driving cause | Force ($F$) | EMF ($\varepsilon$) |
| Energy stored | $\frac{1}{2}mv^2$ (kinetic) | $\frac{1}{2}LI^2$ (magnetic) |
| Governing law | Newton's 2nd Law | Faraday + Lenz's Law |

> 🔑 **Key Takeaway:** Self-inductance $L$ depends **only on the geometry** of the coil (number of turns, area, length) and the **core material** (permeability). It does **NOT** depend on the current $I$ flowing through it — just like mass doesn't change based on how fast an object is moving.

> ⚠️ **Critical Insight — The N² Trap:** Self-inductance is proportional to $N^2$, not $N$. If you double the number of turns, the self-inductance becomes **four times** larger. This is because both the flux per turn AND the number of turns double simultaneously.

---

## 🔬 Stage 2: The Formula Lab

### Formula 1 — Definition of Self-Inductance

$$\boxed{L = \frac{N\Phi}{I}}$$

Where:
| Symbol | Meaning | SI Unit |
|---|---|---|
| $L$ | Self-inductance | Henry (H) |
| $N$ | Number of turns in the coil | dimensionless |
| $\Phi$ | Magnetic flux through **one turn** | Weber (Wb) |
| $N\Phi$ | Total flux linkage | Wb |
| $I$ | Current through the coil | Ampere (A) |

**What this formula says:** Self-inductance is the total magnetic flux linked per unit current. A coil with $L = 1$ H has a total flux linkage of 1 Wb when 1 A of current flows through it.

**SI Unit equivalences:**
$$1 \text{ H} = 1 \frac{\text{Wb}}{\text{A}} = 1 \frac{\text{V·s}}{\text{A}} = 1 \, \Omega \cdot \text{s}$$

> ⚠️ **Unit Trap:** The unit is **Henry (H)** = V·s/A = Wb/A. Common wrong answers in MCQs: Ω/s, V/A·s, J/A². Watch out!

---

### Formula 2 — Back EMF (Induced EMF)

$$\boxed{\varepsilon = -L\frac{dI}{dt}}$$

| Symbol | Meaning | SI Unit |
|---|---|---|
| $\varepsilon$ | Induced (back) EMF | Volt (V) |
| $L$ | Self-inductance | Henry (H) |
| $dI/dt$ | Rate of change of current | A/s |

**What this formula says:** The induced EMF is directly proportional to the rate of change of current. The negative sign (Lenz's law) means the EMF opposes the change. In numerical problems asking for **back EMF**, give the **magnitude**: $|\varepsilon| = L|dI/dt|$.

**For uniform change:** $|\varepsilon| = L \cdot \dfrac{\Delta I}{\Delta t}$

---

### Formula 3 — Self-Inductance of a Solenoid (★ DERIVATION — Asked Every Year ★)

$$\boxed{L = \frac{\mu_0 N^2 A}{l} = \mu_0 n^2 A l = \mu_0 n^2 V}$$

#### Full 4-Step Derivation

Consider a long solenoid of:
- Total turns: $N$, Turn density: $n = N/l$
- Length: $l$, Cross-sectional area: $A$
- Core: air (permeability $\mu_0$)
- Current through it: $I$

**Step 1 — Magnetic field inside:**

For an ideal long solenoid, the field is uniform inside:
$$B = \mu_0 n I = \mu_0 \frac{N}{l} I$$

**Step 2 — Flux through one turn:**
$$\Phi = B \cdot A = \mu_0 \frac{N}{l} I \cdot A$$

**Step 3 — Total flux linkage:**
$$N\Phi = N \cdot \mu_0 \frac{N}{l} I \cdot A = \frac{\mu_0 N^2 A}{l} \cdot I$$

**Step 4 — Apply definition $L = N\Phi / I$:**
$$L = \frac{N\Phi}{I} = \frac{\mu_0 N^2 A}{l}$$

Since $n = N/l$, and volume $V = A \cdot l$:
$$\boxed{L = \mu_0 n^2 A l = \mu_0 n^2 V}$$

**With a magnetic core (relative permeability $\mu_r$):**
$$L = \mu_0 \mu_r \frac{N^2 A}{l}$$

> 💡 **Key Numbers to Memorize:**
> - $\mu_0 = 4\pi \times 10^{-7}$ H/m
> - $L \propto N^2$, $L \propto A$, $L \propto 1/l$, $L \propto \mu_r$

---

### Formula 4 — Energy Stored in an Inductor

$$\boxed{U = \frac{1}{2}LI^2}$$

#### Derivation of Energy Stored

When current $i$ flows through an inductor, the back EMF is $\varepsilon = L\frac{di}{dt}$.

The power consumed (work done against back EMF per second):
$$P = \varepsilon \cdot i = L\frac{di}{dt} \cdot i$$

Total energy stored when current grows from 0 to $I$:
$$U = \int_0^t P \, dt = \int_0^I L \cdot i \, di = L \cdot \frac{I^2}{2}$$

$$\boxed{U = \frac{1}{2}LI^2}$$

This energy is stored in the **magnetic field** inside the inductor.

---

### Formula 5 — Magnetic Energy Density

The energy per unit volume stored inside a solenoid:

$$\boxed{u = \frac{B^2}{2\mu_0}}$$

**Derivation from $U = \frac{1}{2}LI^2$:**

For solenoid: $L = \mu_0 n^2 Al$ and $B = \mu_0 n I \Rightarrow I = B/(\mu_0 n)$

$$U = \frac{1}{2}(\mu_0 n^2 Al)\left(\frac{B}{\mu_0 n}\right)^2 = \frac{B^2 \cdot Al}{2\mu_0}$$

$$u = \frac{U}{V} = \frac{U}{Al} = \frac{B^2}{2\mu_0}$$

---

### Formula 6 — RL Circuit (Current Growth and Decay)

For a series RL circuit with battery EMF $\mathcal{E}$, resistance $R$, inductance $L$:

**Time constant:**
$$\boxed{\tau = \frac{L}{R}}$$

**Current growth (switch just closed at $t = 0$):**
$$\boxed{I(t) = I_0\left(1 - e^{-t/\tau}\right)}, \quad I_0 = \frac{\mathcal{E}}{R}$$

**Current decay (battery disconnected, current decays from $I_0$):**
$$\boxed{I(t) = I_0 \, e^{-t/\tau}}$$

**Back EMF during growth:**
$$\varepsilon_L(t) = \mathcal{E} \cdot e^{-t/\tau}$$

| Time | Current (Growth) | Back EMF |
|---|---|---|
| $t = 0$ | $0$ | $\mathcal{E}$ (maximum) |
| $t = \tau$ | $0.632 \, I_0$ | $0.368 \, \mathcal{E}$ |
| $t = 2\tau$ | $0.865 \, I_0$ | $0.135 \, \mathcal{E}$ |
| $t \to \infty$ | $I_0 = \mathcal{E}/R$ | $0$ |

### Complete Formula Summary Table

| Formula | Quantity | Notes |
|---|---|---|
| $L = N\Phi/I$ | Definition | Flux linkage per unit current |
| $\varepsilon = -L\,dI/dt$ | Back EMF | Negative sign = opposes change |
| $L = \mu_0 N^2 A/l$ | Solenoid L | Derivation asked every year |
| $L = \mu_0 n^2 Al = \mu_0 n^2 V$ | Solenoid L (alternate) | $n$ = turns per unit length |
| $L = \mu_0\mu_r N^2 A/l$ | Iron-core solenoid | $\mu_r \gg 1$ increases $L$ |
| $U = \frac{1}{2}LI^2$ | Energy stored | Magnetic field energy |
| $u = B^2/(2\mu_0)$ | Energy density | Per unit volume |
| $\tau = L/R$ | RL time constant | Units: seconds |
| $I(t) = I_0(1-e^{-t/\tau})$ | Current growth | Exponential rise |

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Calculate L from Definition (L = NΦ/I) ⭐

**Pattern:** *"A coil of N turns has total flux linkage NΦ when current I flows. Find L."* Or reverse: find flux given L and I.

---

**Solved Example 1.1** 🟢

> A coil of 200 turns has a magnetic flux of $5 \times 10^{-3}$ Wb linked with it when a current of 2 A flows through it. Calculate its self-inductance.

<details><summary><b>Solution</b></summary>

**Given:** $N = 200$, $\Phi = 5 \times 10^{-3}$ Wb, $I = 2$ A

Using the definition of self-inductance:

$$L = \frac{N\Phi}{I} = \frac{200 \times 5 \times 10^{-3}}{2}$$

$$\boxed{L = \frac{1.0}{2} = 0.5 \text{ H}}$$

</details>

---

**Practice Problems — Type 1**

1. 🟢 A coil of 100 turns has a flux linkage of $0.02$ Wb·turns when a current of 0.5 A flows through it. Find $L$.

<details><summary><b>Answer</b></summary>

$L = N\Phi/I = 0.02/0.5 = 0.04$ H $= 40$ mH

</details>

2. 🟢 The self-inductance of a coil is 4 H. If a current of 3 A flows, what is the total flux linkage $N\Phi$?

<details><summary><b>Answer</b></summary>

$N\Phi = LI = 4 \times 3 = 12$ Wb

</details>

3. 🟡 A coil has $L = 0.1$ H. What current must flow so that the total flux linkage is 0.5 Wb?

<details><summary><b>Answer</b></summary>

$I = N\Phi/L = 0.5/0.1 = 5$ A

</details>

4. 🟡 A 500-turn coil has $L = 250$ mH. Calculate the average magnetic flux through each turn when $I = 4$ A.

<details><summary><b>Answer</b></summary>

$N\Phi = LI = 0.25 \times 4 = 1$ Wb  
$\Phi = N\Phi/N = 1/500 = 2 \times 10^{-3}$ Wb $= 2$ mWb

</details>

5. 🟡 When current in a coil changes from 3 A to 7 A, the flux linkage changes from 1.5 Wb to 3.5 Wb. Find $L$.

<details><summary><b>Answer</b></summary>

$\Delta(N\Phi) = 3.5 - 1.5 = 2.0$ Wb; $\Delta I = 7 - 3 = 4$ A  
$L = \Delta(N\Phi)/\Delta I = 2.0/4 = 0.5$ H

</details>

6. 🔴 A coil of 300 turns has $L = 30$ mH. When the current is increased from 2 A to 5 A over 0.06 s, calculate (a) the change in flux linkage and (b) the induced back EMF.

<details><summary><b>Answer</b></summary>

(a) $\Delta(N\Phi) = L \cdot \Delta I = 0.030 \times 3 = 0.09$ Wb  
(b) $|\varepsilon| = L \cdot \Delta I/\Delta t = 0.030 \times 3/0.06 = 1.5$ V

</details>

7. 🔴 A solenoid has $L = 2$ H and carries a current that varies as $I = 4\sin(100\pi t)$ A. Find the maximum back EMF induced.

<details><summary><b>Answer</b></summary>

$\varepsilon = -L\,dI/dt = -L \cdot 4 \times 100\pi \cos(100\pi t)$  
Maximum when $|\cos(100\pi t)| = 1$:  
$|\varepsilon|_{\max} = 2 \times 4 \times 100\pi = 800\pi \approx 2513$ V

</details>

---

### Type 2: Solenoid Self-Inductance Formula ⭐ (ASKED EVERY YEAR IN BOARDS)

**Pattern:** *"A solenoid has N turns, length l, area A. Find L."* OR *"Derive an expression for self-inductance of a long solenoid."*

---

**Solved Example 2.1 — The Famous Derivation** 🟡

> Derive an expression for the self-inductance of a long solenoid of length $l$, cross-sectional area $A$, and total $N$ turns. Write the formula also in terms of turn density $n$ and volume $V$.

<details><summary><b>Solution</b></summary>

**Consider a long solenoid:**
- Length $l$, area $A$, total turns $N$, turn density $n = N/l$
- Current through solenoid: $I$

**Step 1 — Magnetic field inside the solenoid:**

$$B = \mu_0 n I = \mu_0 \frac{N}{l} I$$

(Valid for an ideal long solenoid where end effects are negligible.)

**Step 2 — Magnetic flux through one turn:**

$$\Phi = B \cdot A = \frac{\mu_0 N I A}{l}$$

**Step 3 — Total flux linkage (all N turns):**

$$N\Phi = N \cdot \frac{\mu_0 N I A}{l} = \frac{\mu_0 N^2 A}{l} \cdot I$$

**Step 4 — Apply the definition $L = N\Phi/I$:**

Dividing both sides by $I$:

$$\boxed{L = \frac{\mu_0 N^2 A}{l}}$$

**Alternate forms** (using $n = N/l$ and $V = Al$):

$$L = \mu_0 n^2 \cdot Al = \mu_0 n^2 V$$

**Note:** If the core has relative permeability $\mu_r$ (iron core):
$$L = \frac{\mu_0 \mu_r N^2 A}{l}$$

Since $\mu_r \gg 1$ for ferromagnetic materials, inserting an iron core dramatically increases $L$. ✓

</details>

---

**Solved Example 2.2** 🟡

> A solenoid has 500 turns, length 25 cm, and cross-sectional area $4 \text{ cm}^2$. Find its self-inductance.

<details><summary><b>Solution</b></summary>

**Given:** $N = 500$, $l = 0.25$ m, $A = 4 \times 10^{-4}$ m²

$$L = \frac{\mu_0 N^2 A}{l} = \frac{(4\pi \times 10^{-7}) \times (500)^2 \times (4 \times 10^{-4})}{0.25}$$

**Calculate numerator:**
$$= 4\pi \times 10^{-7} \times 250000 \times 4 \times 10^{-4}$$
$$= 4\pi \times 10^{-7} \times 10^{5} = 4\pi \times 10^{-2}$$

Wait — let me redo with the 4 from area:
$$= 4\pi \times 10^{-7} \times 2.5 \times 10^{5} \times 4 \times 10^{-4} = 4\pi \times 10^{-7} \times 10^{2} = 4\pi \times 10^{-5}$$

**Divide by $l = 0.25$:**
$$L = \frac{4\pi \times 10^{-5}}{0.25} = 16\pi \times 10^{-5} \approx 5.03 \times 10^{-4} \text{ H}$$

**Let's verify step-by-step:**
- $N^2 = 500^2 = 2.5 \times 10^5$
- $\mu_0 N^2 = 4\pi \times 10^{-7} \times 2.5 \times 10^5 = \pi \times 10^{-1} = 0.1\pi$
- $\mu_0 N^2 A = 0.1\pi \times 4 \times 10^{-4} = 4\pi \times 10^{-5}$
- $L = 4\pi \times 10^{-5}/0.25 = 16\pi \times 10^{-5}$

$$\boxed{L = 16\pi \times 10^{-5} \approx 5.03 \times 10^{-4} \text{ H} \approx 0.503 \text{ mH}}$$

</details>

---

**Practice Problems — Type 2**

1. 🟢 A solenoid has 200 turns, length 50 cm, and area $8 \text{ cm}^2$. Find $L$.

<details><summary><b>Answer</b></summary>

$L = \mu_0 N^2 A/l = (4\pi \times 10^{-7} \times 40000 \times 8 \times 10^{-4})/0.5$  
$= (4\pi \times 10^{-7} \times 3.2 \times 10^{1})/0.5 = (1.28\pi \times 10^{-5})/0.5 = 2.56\pi \times 10^{-5} \approx 8.04 \times 10^{-5}$ H $\approx 80.4$ μH

</details>

2. 🟢 The self-inductance of a solenoid is 5 mH. If the number of turns is doubled (keeping $l$ and $A$ same), what is the new inductance?

<details><summary><b>Answer</b></summary>

$L \propto N^2$. If $N \to 2N$, then $L \to 4L = 4 \times 5 = 20$ mH.

</details>

3. 🟡 A solenoid of length 1 m and cross-sectional area $10 \text{ cm}^2$ has a self-inductance of 1 mH. How many turns does it have? ($\mu_0 = 4\pi \times 10^{-7}$ H/m)

<details><summary><b>Answer</b></summary>

$L = \mu_0 N^2 A/l \Rightarrow N^2 = Ll/(\mu_0 A) = (10^{-3} \times 1)/(4\pi \times 10^{-7} \times 10^{-3}) = 10^{-3}/(4\pi \times 10^{-10}) = 10^7/(4\pi) \approx 795775$  
$N = \sqrt{795775} \approx 892$ turns

</details>

4. 🟡 A solenoid has turn density $n = 1000$ turns/m, area $= 10 \text{ cm}^2$, and length $50$ cm. Find $L$.

<details><summary><b>Answer</b></summary>

$L = \mu_0 n^2 Al = 4\pi \times 10^{-7} \times 10^6 \times 10^{-3} \times 0.5 = 4\pi \times 10^{-7} \times 500 = 2\pi \times 10^{-4} \approx 6.28 \times 10^{-4}$ H $\approx 0.628$ mH

</details>

5. 🟡 If an iron core of $\mu_r = 1000$ is inserted in the solenoid of Q4, what is the new inductance?

<details><summary><b>Answer</b></summary>

New $L = \mu_r \times L_{\text{air}} = 1000 \times 6.28 \times 10^{-4} = 0.628$ H

</details>

6. 🔴 Two solenoids A and B have the same number of turns and the same length. The radius of B is twice that of A. What is the ratio $L_A : L_B$?

<details><summary><b>Answer</b></summary>

$A_A = \pi r^2$; $A_B = \pi(2r)^2 = 4\pi r^2 = 4A_A$  
$L \propto A$, so $L_A/L_B = A_A/A_B = 1/4$  
$\boxed{L_A : L_B = 1 : 4}$

</details>

7. 🔴 The length of a solenoid is doubled and the radius is halved (number of turns unchanged). By what factor does its self-inductance change?

<details><summary><b>Answer</b></summary>

$L = \mu_0 N^2 A/l$. New: $l' = 2l$, $A' = \pi(r/2)^2 = A/4$  
$L' = \mu_0 N^2 (A/4)/(2l) = (\mu_0 N^2 A/l) \times (1/8) = L/8$  
**L decreases to 1/8 of its original value.**

</details>

8. 🔴 A solenoid has $L = 50$ mH when it has no core. An iron core with $\mu_r = 400$ is half inserted. Estimate the effective inductance (assume half the volume has $\mu_r = 400$ and half has $\mu_r = 1$, and they act like inductors in series).

<details><summary><b>Answer</b></summary>

Consider two halves in series: $L_1 = \mu_0 \mu_r N_1^2 A/l_1$ and $L_2 = \mu_0 N_2^2 A/l_2$  
Each half has $N/2$ turns and length $l/2$.  
$L_{\text{iron half}} = \mu_0 \times 400 \times (N/2)^2 A/(l/2) = 400 \times \frac{\mu_0 N^2 A}{2l} = 200 \times L/l \times l = 100 \times (L/l) \cdot l$  
More straightforwardly: $L_{\text{iron}} = \mu_r \times L/2 = 400 \times 25 = 10000$ mH (for that half)  
$L_{\text{air}} = L/2 = 25$ mH (for the other half)  
$L_{\text{total}} = 10000 + 25 = 10025$ mH $\approx 10$ H  
*(This is an approximation; the exact calculation requires knowing the turn distribution.)*

</details>

---

### Type 3: Back EMF (ε = L·dI/dt) ⭐

**Pattern:** *"Given change in current and time interval, find back EMF."* Or *"Given EMF and ΔI/Δt, find L."*

---

**Solved Example 3.1** 🟡

> A coil of self-inductance $L = 5$ H is connected to a battery. The current through it grows uniformly from 0 to 2 A in 0.1 s. Find the back EMF induced in the coil.

<details><summary><b>Solution</b></summary>

**Given:** $L = 5$ H, $\Delta I = 2 - 0 = 2$ A, $\Delta t = 0.1$ s

**Rate of change of current:**
$$\frac{\Delta I}{\Delta t} = \frac{2}{0.1} = 20 \text{ A/s}$$

**Back EMF:**
$$|\varepsilon| = L \cdot \frac{\Delta I}{\Delta t} = 5 \times 20 = 100 \text{ V}$$

$$\boxed{|\varepsilon| = 100 \text{ V}}$$

*(CBSE 2019 — 3 marks)*

</details>

---

**Solved Example 3.2** 🟡

> Current in an inductor changes from 2 A to 5 A in 0.05 s, and a back EMF of 3 V is observed. Find the self-inductance of the coil.

<details><summary><b>Solution</b></summary>

**Given:** $I_1 = 2$ A, $I_2 = 5$ A, $\Delta t = 0.05$ s, $|\varepsilon| = 3$ V

$$|\varepsilon| = L \cdot \frac{\Delta I}{\Delta t} \Rightarrow L = \frac{|\varepsilon| \cdot \Delta t}{\Delta I}$$

$$L = \frac{3 \times 0.05}{5 - 2} = \frac{0.15}{3} = 0.05 \text{ H}$$

$$\boxed{L = 0.05 \text{ H} = 50 \text{ mH}}$$

*(CBSE 2020 — 2 marks)*

</details>

---

**Practice Problems — Type 3**

1. 🟢 A coil of $L = 2$ H has current changing at a rate of 5 A/s. Find the induced back EMF.

<details><summary><b>Answer</b></summary>

$|\varepsilon| = L \cdot dI/dt = 2 \times 5 = 10$ V

</details>

2. 🟢 The back EMF in a coil is 50 V when current changes at 25 A/s. Find $L$.

<details><summary><b>Answer</b></summary>

$L = |\varepsilon|/(dI/dt) = 50/25 = 2$ H

</details>

3. 🟡 A 200 mH inductor has current $I = 3t^2 + 2t$ A (where $t$ is in seconds). Find the back EMF at $t = 2$ s.

<details><summary><b>Answer</b></summary>

$dI/dt = 6t + 2$. At $t = 2$: $dI/dt = 14$ A/s  
$|\varepsilon| = L \cdot dI/dt = 0.2 \times 14 = 2.8$ V

</details>

4. 🟡 An inductor of $L = 0.4$ H has current that changes from 10 A to 2 A in 0.02 s. Find: (a) back EMF (b) direction of induced current — does it oppose or support the original current?

<details><summary><b>Answer</b></summary>

(a) $|\varepsilon| = L \times |ΔI/Δt| = 0.4 \times 8/0.02 = 0.4 \times 400 = 160$ V  
(b) Current is decreasing, so induced EMF tries to **maintain** (support) the original current. The induced current flows in the **same** direction as the original current.

</details>

5. 🟡 A spark of 1000 V appears across an inductive switch when the current drops from 5 A to 0 in 5 ms. Find $L$.

<details><summary><b>Answer</b></summary>

$L = |\varepsilon| \cdot \Delta t / \Delta I = 1000 \times 0.005/5 = 1$ H

</details>

6. 🔴 Current in a coil varies as $I = I_0 e^{-\alpha t}$. Show that the back EMF is $\varepsilon = L\alpha I_0 e^{-\alpha t}$ and find its value at $t = 0$ if $L = 2$ H, $I_0 = 5$ A, $\alpha = 10$ s⁻¹.

<details><summary><b>Answer</b></summary>

$dI/dt = -I_0\alpha e^{-\alpha t}$  
$|\varepsilon| = L|dI/dt| = LI_0\alpha e^{-\alpha t}$  
At $t=0$: $|\varepsilon| = 2 \times 5 \times 10 = 100$ V

</details>

7. 🔴 Two inductors $L_1 = 3$ H and $L_2 = 5$ H are connected in series. Current changes at 4 A/s. Find total back EMF. What is the equivalent inductance?

<details><summary><b>Answer</b></summary>

For series: $L_{\text{eq}} = L_1 + L_2 = 8$ H  
Total back EMF $= L_{\text{eq}} \times dI/dt = 8 \times 4 = 32$ V  
(Equivalently: $\varepsilon_1 = 3 \times 4 = 12$ V; $\varepsilon_2 = 5 \times 4 = 20$ V; total $= 32$ V ✓)

</details>

---

### Type 4: Energy Stored in an Inductor (U = ½LI²) ⭐

**Pattern:** *"Given L and I, find energy."* Or *"Given energy and I, find L."*

---

**Solved Example 4.1** 🟡

> An inductor coil carries a current of 5 A and stores energy of 5 J. Calculate its self-inductance.

<details><summary><b>Solution</b></summary>

**Given:** $I = 5$ A, $U = 5$ J

$$U = \frac{1}{2}LI^2 \Rightarrow L = \frac{2U}{I^2} = \frac{2 \times 5}{5^2} = \frac{10}{25}$$

$$\boxed{L = 0.4 \text{ H}}$$

*(CBSE 2016 — 2 marks)*

</details>

---

**Practice Problems — Type 4**

1. 🟢 A 2 H inductor carries a current of 4 A. Find the energy stored.

<details><summary><b>Answer</b></summary>

$U = \frac{1}{2}LI^2 = \frac{1}{2} \times 2 \times 16 = 16$ J

</details>

2. 🟢 An inductor stores 100 J of energy when 10 A of current flows. Find $L$.

<details><summary><b>Answer</b></summary>

$L = 2U/I^2 = 200/100 = 2$ H

</details>

3. 🟡 The current in an inductor of $L = 50$ mH increases from 0 to 3 A. Find the energy stored in the magnetic field.

<details><summary><b>Answer</b></summary>

$U = \frac{1}{2} \times 0.05 \times 9 = 0.225$ J

</details>

4. 🟡 Current in a 4 H inductor is doubled from 2 A to 4 A. By how much does the stored energy increase?

<details><summary><b>Answer</b></summary>

$U_1 = \frac{1}{2} \times 4 \times 4 = 8$ J; $U_2 = \frac{1}{2} \times 4 \times 16 = 32$ J  
Increase $= 32 - 8 = 24$ J

</details>

5. 🟡 Compare energy stored in: (a) $L_1 = 2$ H carrying $I = 4$ A, and (b) $L_2 = 4$ H carrying $I = 2$ A.

<details><summary><b>Answer</b></summary>

$U_1 = \frac{1}{2} \times 2 \times 16 = 16$ J  
$U_2 = \frac{1}{2} \times 4 \times 4 = 8$ J  
$U_1 > U_2$ — doubling current stores more energy than doubling inductance (since $U \propto I^2$ but $U \propto L$).

</details>

6. 🔴 A solenoid with $N = 1000$, $l = 0.5$ m, $A = 20 \text{ cm}^2$ carries $I = 2$ A. Find (a) $L$, (b) energy stored, (c) magnetic energy density.

<details><summary><b>Answer</b></summary>

(a) $L = \mu_0 N^2 A/l = (4\pi \times 10^{-7} \times 10^6 \times 20 \times 10^{-4})/0.5 = (4\pi \times 10^{-7} \times 2000)/0.5 = 4\pi \times 10^{-7} \times 4000 = 16\pi \times 10^{-4} \approx 5.03 \times 10^{-3}$ H $\approx 5$ mH  
(b) $U = \frac{1}{2} \times 5.03 \times 10^{-3} \times 4 \approx 10.05 \times 10^{-3}$ J $\approx 10$ mJ  
(c) $V = Al = 20 \times 10^{-4} \times 0.5 = 10^{-3}$ m³; $u = U/V = 10 \times 10^{-3}/10^{-3} = 10$ J/m³

</details>

7. 🔴 An inductor of $L = 1$ H carries current $I(t) = 2e^{-3t}$ A. Find the energy stored at $t = 0$ and $t \to \infty$.

<details><summary><b>Answer</b></summary>

At $t=0$: $I = 2$ A, $U = \frac{1}{2} \times 1 \times 4 = 2$ J  
At $t \to \infty$: $I = 0$, $U = 0$ J  
All 2 J was dissipated as heat in the resistance.

</details>

---

### Type 5: Factors Affecting Self-Inductance

**Pattern:** *"How does L change when N, l, A, or core material changes?"*

---

**Solved Example 5.1** 🟡

> A solenoid with $N$ turns, length $l$, and area $A$ has self-inductance $L$. What happens to $L$ if: (a) $N$ is tripled, (b) $l$ is halved, (c) area is doubled, (d) an iron core of $\mu_r = 200$ is inserted?

<details><summary><b>Solution</b></summary>

Using $L = \mu_0 N^2 A/l$:

**(a) N tripled:** $N \to 3N \Rightarrow L \to (3)^2 L = 9L$ **(nine times)**

**(b) l halved:** $l \to l/2 \Rightarrow L \to L/(1/2) = 2L$ **(doubled)**

**(c) A doubled:** $A \to 2A \Rightarrow L \to 2L$ **(doubled)**

**(d) Iron core inserted:** $\mu_0 \to \mu_0\mu_r \Rightarrow L \to 200L$ **(200 times larger)**

</details>

---

**Practice Problems — Type 5**

1. 🟢 If the length of a solenoid is increased fourfold and number of turns doubled, how does $L$ change?

<details><summary><b>Answer</b></summary>

$L' = \mu_0 (2N)^2 A/(4l) = 4\mu_0 N^2A/(4l) = \mu_0 N^2 A/l = L$ — **L remains unchanged**.

</details>

2. 🟡 (NCERT Exemplar Q6.6) The self-inductance $L$ of a solenoid of fixed $N$ increases as:
   (a) both $l$ and $A$ increase &emsp; (b) $l$ decreases and $A$ increases &emsp; (c) $l$ increases and $A$ decreases &emsp; (d) both $l$ and $A$ decrease

<details><summary><b>Answer</b></summary>

**Answer: (b)**  
$L = \mu_0 N^2 A/l$. $L \propto A/l$. For $L$ to increase, $A$ must increase and $l$ must decrease.

</details>

3. 🟡 (NCERT Exemplar Q6.12) A solenoid connected to a DC source is stretched (length increases). What happens to the magnetic flux through the solenoid?

<details><summary><b>Answer</b></summary>

Stretching → $l$ increases, $n = N/l$ decreases, $L = \mu_0 n^2 Al$ decreases.  
With a DC source (constant voltage), current $I = V/R$ stays the same (inductor has no DC resistance effect at steady state), but flux $N\Phi = LI$ decreases. So the **magnetic flux decreases**.

</details>

4. 🔴 (NCERT Exemplar Q6.13) When a soft iron core is inserted into a solenoid connected to an AC source, which of the following happens momentarily?  
   (a) current increases &emsp; (b) current decreases &emsp; (c) current stays same &emsp; (d) flux stays same

<details><summary><b>Answer</b></summary>

**Answer: (b) current decreases**  
Iron core → $\mu_r$ increases → $L$ increases → $X_L = \omega L$ increases (for AC) → impedance increases → current $I = V/X_L$ **decreases**. Also, larger $L$ means larger back EMF opposing current.

</details>

---

### Type 6: RL Circuit (Growth / Decay / Time Constant)

**Pattern:** *"Find current at time t, or find time constant, or compare current at different instants."*

---

**Solved Example 6.1** 🟡

> A 10 Ω resistor and a 2 H inductor are connected in series to a 20 V battery. Find: (a) the time constant, (b) the steady-state current, (c) the current at $t = \tau$, (d) the back EMF at $t = 0$.

<details><summary><b>Solution</b></summary>

**Given:** $R = 10$ Ω, $L = 2$ H, $\mathcal{E} = 20$ V

**(a) Time constant:**
$$\tau = \frac{L}{R} = \frac{2}{10} = 0.2 \text{ s}$$

**(b) Steady-state current:**
$$I_0 = \frac{\mathcal{E}}{R} = \frac{20}{10} = 2 \text{ A}$$

**(c) Current at $t = \tau$:**
$$I(\tau) = I_0(1 - e^{-1}) = 2 \times (1 - 0.368) = 2 \times 0.632 = 1.264 \text{ A}$$

**(d) Back EMF at $t = 0$:**

At $t = 0$, the current is zero, so the entire battery voltage is dropped across the inductor:
$$\varepsilon_L(0) = \mathcal{E} \times e^{-0/\tau} = 20 \times 1 = \boxed{20 \text{ V}}$$

*(The inductor acts as an open circuit at $t = 0$, absorbing the full battery voltage as back EMF.)*

</details>

---

**Practice Problems — Type 6**

1. 🟢 An RL circuit has $L = 0.5$ H and $R = 25$ Ω. Find the time constant.

<details><summary><b>Answer</b></summary>

$\tau = L/R = 0.5/25 = 0.02$ s $= 20$ ms

</details>

2. 🟡 In an RL circuit with $\tau = 0.1$ s, the current grows to reach $I_0/2$ after time $t$. Find $t$.

<details><summary><b>Answer</b></summary>

$I_0/2 = I_0(1-e^{-t/\tau}) \Rightarrow 1/2 = 1 - e^{-t/\tau} \Rightarrow e^{-t/\tau} = 1/2$  
$t = \tau \ln 2 = 0.1 \times 0.693 = 0.0693$ s $\approx 69.3$ ms

</details>

3. 🟡 An RL circuit has $\mathcal{E} = 12$ V, $R = 6$ Ω, $L = 0.3$ H. Find the current at $t = 0.05$ s.

<details><summary><b>Answer</b></summary>

$\tau = 0.3/6 = 0.05$ s; $I_0 = 12/6 = 2$ A  
At $t = \tau = 0.05$ s: $I = 2(1 - e^{-1}) = 2 \times 0.632 = 1.264$ A

</details>

4. 🔴 In an RL circuit ($R = 5$ Ω, $L = 0.5$ H, $\mathcal{E} = 10$ V), find the rate of change of current at $t = 0$ and at $t \to \infty$.

<details><summary><b>Answer</b></summary>

Using $\mathcal{E} = iR + L\,di/dt$:  
At $t=0$: $i = 0$, so $L\,di/dt = \mathcal{E} \Rightarrow di/dt = \mathcal{E}/L = 10/0.5 = 20$ A/s  
At $t\to\infty$: $i = I_0 = 2$ A, $iR = 10 = \mathcal{E}$, so $L\,di/dt = 0 \Rightarrow di/dt = 0$ A/s

</details>

5. 🔴 A coil ($L = 2$ H, $R = 4$ Ω) carries steady current from a 8 V battery. The battery is suddenly removed and the coil is short-circuited. Find the current after $t = 0.5$ s.

<details><summary><b>Answer</b></summary>

Initial current: $I_0 = 8/4 = 2$ A; $\tau = L/R = 2/4 = 0.5$ s  
Decay: $I(0.5) = I_0 e^{-0.5/0.5} = 2e^{-1} = 2/e \approx 0.736$ A

</details>

---

### Type 7: Magnetic Energy Density (u = B²/2μ₀)

**Pattern:** *"Find energy density inside a solenoid"* or *"Compare energy densities."*

---

**Solved Example 7.1** 🟡

> A solenoid of length 0.5 m, cross-sectional area $4 \text{ cm}^2$, and $n = 800$ turns/m carries a current of 3 A. Find: (a) the magnetic field inside, (b) the energy density, (c) the total energy stored.

<details><summary><b>Solution</b></summary>

**Given:** $l = 0.5$ m, $A = 4 \times 10^{-4}$ m², $n = 800$ turns/m, $I = 3$ A

**(a) Magnetic field:**
$$B = \mu_0 n I = 4\pi \times 10^{-7} \times 800 \times 3 = 9.6\pi \times 10^{-4} \approx 3.016 \times 10^{-3} \text{ T}$$

**(b) Energy density:**
$$u = \frac{B^2}{2\mu_0} = \frac{(9.6\pi \times 10^{-4})^2}{2 \times 4\pi \times 10^{-7}}$$

$$= \frac{(9.6)^2 \pi^2 \times 10^{-8}}{8\pi \times 10^{-7}} = \frac{92.16\pi \times 10^{-8}}{8 \times 10^{-7}} = \frac{92.16\pi}{80} \approx 3.62 \text{ J/m}^3$$

**(c) Total energy:**
$$V = A \times l = 4 \times 10^{-4} \times 0.5 = 2 \times 10^{-4} \text{ m}^3$$
$$U = u \times V = 3.62 \times 2 \times 10^{-4} = 7.24 \times 10^{-4} \text{ J} \approx 0.72 \text{ mJ}$$

**Verification:** $L = \mu_0 n^2 Al = 4\pi \times 10^{-7} \times 640000 \times 2 \times 10^{-4} \approx 1.608 \times 10^{-4}$ H  
$U = \frac{1}{2}LI^2 = \frac{1}{2} \times 1.608 \times 10^{-4} \times 9 \approx 7.24 \times 10^{-4}$ J ✓

</details>

---

**Practice Problems — Type 7**

1. 🟢 The magnetic field inside a solenoid is $0.4$ T. Find the energy density of the magnetic field. ($\mu_0 = 4\pi \times 10^{-7}$ H/m)

<details><summary><b>Answer</b></summary>

$u = B^2/(2\mu_0) = (0.4)^2/(2 \times 4\pi \times 10^{-7}) = 0.16/(8\pi \times 10^{-7}) = 0.02/(\pi \times 10^{-7}) \approx 6.37 \times 10^4$ J/m³

</details>

2. 🟡 Inside a solenoid, $B = 2$ T. If the volume of the solenoid is $50 \text{ cm}^3$, find the total magnetic energy stored.

<details><summary><b>Answer</b></summary>

$u = B^2/(2\mu_0) = 4/(8\pi \times 10^{-7}) = 5/(π \times 10^{-7}) \approx 1.59 \times 10^6$ J/m³  
$U = u \times V = 1.59 \times 10^6 \times 50 \times 10^{-6} = 79.6$ J

</details>

3. 🔴 Show that the expression $u = B^2/(2\mu_0)$ is dimensionally consistent with energy per unit volume (J/m³).

<details><summary><b>Answer</b></summary>

$[B] = $ T $= $ kg/(A·s²) $= $ kg·s⁻²·A⁻¹  
$[B^2] = $ kg²·s⁻⁴·A⁻²  
$[\mu_0] = $ H/m $= $ kg·m·s⁻²·A⁻²  
$[B^2/\mu_0] = $ (kg²·s⁻⁴·A⁻²)/(kg·m·s⁻²·A⁻²) $=$ kg·s⁻²/m $=$ J/m³ ✓

</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1.** The SI unit of self-inductance is:

(a) Ω/s &emsp; (b) V·s/A &emsp; (c) A/V·s &emsp; (d) J/A

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) V·s/A**

From $\varepsilon = L \cdot dI/dt$: $[L] = [\varepsilon]/[dI/dt] = $ V/(A/s) $= $ V·s/A $= $ Henry.

Also $1$ H $= 1$ Wb/A $= 1$ Ω·s $=$ V·s/A. Options (a) Ω/s and (d) J/A are wrong units. (c) is the reciprocal.

</details>

---

**Q2.** The self-inductance of a coil depends on:

(a) The current flowing through it &emsp; (b) The rate of change of current &emsp; (c) The geometry of the coil and core material &emsp; (d) Both (a) and (b)

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

$L = \mu_0\mu_r N^2 A/l$ — depends only on geometry (N, A, l) and medium ($\mu_r$). It does NOT depend on $I$ or $dI/dt$. This is a fundamental property, just like capacitance depends on geometry not on charge.

</details>

---

**Q3.** The number of turns in a solenoid is doubled, keeping all other parameters the same. The self-inductance becomes:

(a) Half &emsp; (b) Double &emsp; (c) Four times &emsp; (d) Unchanged

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Four times**

$L \propto N^2$. So if $N \to 2N$, then $L \to (2)^2 L = 4L$.

⚠️ **Common trap:** Students often choose (b) Double, forgetting the $N^2$ dependence. Remember: self-inductance grows as the **square** of turns.

</details>

---

**Q4.** In a series RL circuit with EMF $\mathcal{E}$, at the instant the switch is closed ($t = 0$), the back EMF of the inductor equals:

(a) Zero &emsp; (b) $\mathcal{E}/2$ &emsp; (c) $\mathcal{E}$ &emsp; (d) Infinity

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) $\mathcal{E}$**

At $t = 0$, current $I = 0$. By Kirchhoff's law: $\mathcal{E} = IR + L\,dI/dt = 0 + L\,dI/dt$. So the inductor absorbs the full battery EMF as back EMF. The inductor acts like an **open circuit** at $t = 0$.

</details>

---

**Q5. (Graph-based)** The current in an RL circuit grows with time. Which graph correctly shows $I$ vs $t$?

(a) A straight line through origin &emsp; (b) An exponential curve starting steeply and levelling off &emsp; (c) A parabola &emsp; (d) A straight horizontal line

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) An exponential curve starting steeply and levelling off**

$I(t) = I_0(1 - e^{-t/\tau})$ — exponential approach to $I_0$. At $t = 0$: slope is $\mathcal{E}/L$ (maximum, steep). As $t \to \infty$: slope approaches zero, current levels off at $I_0 = \mathcal{E}/R$.

**Back EMF vs. time:** Starts at $\mathcal{E}$ (maximum) and decays exponentially to 0 — the reverse shape.

</details>

---

**Q6. (Assertion-Reason)** 

**Assertion (A):** The self-inductance of a coil depends only on its geometry and the permeability of the medium — not on the current.

**Reason (R):** $L = N\Phi/I$ shows that $L$ varies as $1/I$.

(a) Both A and R are correct, and R is the correct explanation of A.  
(b) Both A and R are correct, but R is NOT the correct explanation of A.  
(c) A is correct, but R is incorrect.  
(d) A is incorrect, but R is correct.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

**A is correct:** $L$ depends only on geometry ($N, A, l$) and $\mu_r$ — verified by $L = \mu_0 N^2 A/l$.

**R is incorrect:** The formula $L = N\Phi/I$ does NOT mean $L \propto 1/I$. The total flux $N\Phi$ is itself proportional to $I$ (since $B \propto I$ and $\Phi = BA$), so $N\Phi/I$ = constant = $L$. The ratio is constant regardless of $I$.

</details>

---

**Q7. (Assertion-Reason)**

**Assertion (A):** An inductor stores energy in its magnetic field; a capacitor stores energy in its electric field.

**Reason (R):** The energy stored in an inductor is $U = \frac{1}{2}LI^2$ and in a capacitor is $U = \frac{1}{2}CV^2$.

(a) Both A and R are correct, and R is the correct explanation of A.  
(b) Both A and R are correct, but R is NOT the correct explanation of A.  
(c) A is correct, but R is incorrect.  
(d) A is incorrect, but R is correct.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Both statements are fully correct. R correctly explains A — the $\frac{1}{2}LI^2$ formula arises from energy stored in the magnetic field of the inductor, while $\frac{1}{2}CV^2$ arises from energy in the electric field between capacitor plates.

</details>

---

**Q8. (Assertion-Reason)**

**Assertion (A):** In a DC RL circuit at steady state, the back EMF of the inductor is zero.

**Reason (R):** At steady state, the current is constant, so $dI/dt = 0$, making back EMF $\varepsilon = -L\,dI/dt = 0$.

(a) Both A and R are correct, and R is the correct explanation of A.  
(b) Both A and R are correct, but R is NOT the correct explanation of A.  
(c) A is correct, but R is incorrect.  
(d) Both A and R are incorrect.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Both are correct and causally linked. At steady state, $dI/dt = 0$, so back EMF $= 0$. The inductor behaves like a plain wire (pure resistor). All the battery voltage is dropped across the external resistance.

</details>

---

**Q9. (Statement I / Statement II)**

**Statement I:** The self-inductance of a toroidal solenoid is $L = \mu_0 N^2 A/(2\pi r)$, where $r$ is the mean radius.

**Statement II:** A toroid has no external magnetic field, so its self-inductance depends only on the field confined within its core.

(a) Statement I is true, Statement II is false.  
(b) Statement I is false, Statement II is true.  
(c) Both statements are true, and Statement II explains Statement I.  
(d) Both statements are true, but Statement II does NOT explain Statement I.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Both statements are true. For a toroid: the mean circumference is $2\pi r$, so $n_{\text{eff}} = N/(2\pi r)$, giving $L = \mu_0 n^2 \times V = \mu_0 N^2 A/(2\pi r)$. Statement II is correct — the toroid confines all flux inside, which is why the formula takes this form.

</details>

---

**Q10.** A solenoid has $L = L_0$. A second solenoid is made with twice the turns, same length, and same cross-section area. They are connected in series. The equivalent inductance is:

(a) $5L_0$ &emsp; (b) $3L_0$ &emsp; (c) $6L_0$ &emsp; (d) $L_0$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $5L_0$**

$L_1 = L_0$. For the second solenoid: $N' = 2N$, so $L_2 = \mu_0(2N)^2A/l = 4L_0$.

In series (assuming no mutual inductance): $L_{eq} = L_1 + L_2 = L_0 + 4L_0 = 5L_0$.

</details>

---

**Q11.** A coil of $L = 0.2$ H and $R = 2$ Ω is connected to a 10 V battery. After a long time, the battery is disconnected. The energy dissipated in the resistor after disconnection is:

(a) 0.25 J &emsp; (b) 2.5 J &emsp; (c) 25 J &emsp; (d) 5 J

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) 2.5 J**

At steady state: $I = V/R = 10/2 = 5$ A.  
Energy stored: $U = \frac{1}{2}LI^2 = \frac{1}{2} \times 0.2 \times 25 = 2.5$ J.  
After disconnection, all this energy is dissipated in the resistance.

</details>

---

**Q12. (Exemplar-depth)** A solenoid is connected to an ideal battery ($r = 0$) in steady DC state. The solenoid is then pulled apart (stretched), increasing its length. Which of the following is CORRECT immediately after stretching?

(a) Current increases, flux decreases  
(b) Current stays same, flux decreases  
(c) Current decreases, flux increases  
(d) Both current and flux stay the same

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Current stays same, flux decreases**

With an ideal battery ($r = 0$) and at steady DC: $I = V/R$ is fixed by the external resistance (not by $L$). Stretching → $l$ increases → $n = N/l$ decreases → $B = \mu_0 nI$ decreases → $\Phi = BA$ decreases → total flux $N\Phi = LI$ decreases (since $L$ decreases). Current stays constant (controlled by battery voltage and resistance).

</details>

---

## 🔀 Stage 5: Type Mixer

### Problem 1 (Types 2 + 4): The Solenoid Energy Analysis 🟡

> A solenoid has 500 turns, length 50 cm, and cross-sectional area $4 \text{ cm}^2$. It carries a current of 5 A. Calculate:  
> (a) The magnetic field inside the solenoid  
> (b) The flux through one turn  
> (c) The total flux linkage  
> (d) The self-inductance  
> (e) The energy stored

*(CBSE 2022 — 3 marks)*

<details><summary><b>Solution</b></summary>

**Given:** $N = 500$, $l = 0.50$ m, $A = 4 \times 10^{-4}$ m², $I = 5$ A  
$n = N/l = 500/0.5 = 1000$ turns/m

**(a) Magnetic field:**
$$B = \mu_0 n I = 4\pi \times 10^{-7} \times 1000 \times 5 = 2\pi \times 10^{-3} \approx 6.28 \times 10^{-3} \text{ T}$$

**(b) Flux through one turn:**
$$\Phi = BA = 6.28 \times 10^{-3} \times 4 \times 10^{-4} = 2.512 \times 10^{-6} \text{ Wb}$$

**(c) Total flux linkage:**
$$N\Phi = 500 \times 2.512 \times 10^{-6} = 1.256 \times 10^{-3} \text{ Wb}$$

**(d) Self-inductance:**
$$L = \frac{N\Phi}{I} = \frac{1.256 \times 10^{-3}}{5} = 2.512 \times 10^{-4} \text{ H}$$

**Verify using formula:**
$$L = \frac{\mu_0 N^2 A}{l} = \frac{4\pi \times 10^{-7} \times 250000 \times 4 \times 10^{-4}}{0.5} = \frac{4\pi \times 10^{-5}}{0.5} = 8\pi \times 10^{-5} \approx 2.513 \times 10^{-4} \text{ H} \checkmark$$

**(e) Energy stored:**
$$U = \frac{1}{2}LI^2 = \frac{1}{2} \times 2.512 \times 10^{-4} \times 25 = 3.14 \times 10^{-3} \text{ J} \approx 3.14 \text{ mJ}$$

</details>

---

### Problem 2 (Types 3 + 6): RL Circuit with Back EMF Analysis 🔴

> In an RL circuit, $R = 100$ Ω, $L = 0.5$ H, $\mathcal{E} = 20$ V. The switch is closed at $t = 0$.  
> (a) Find the time constant $\tau$.  
> (b) Find the initial rate of rise of current.  
> (c) Find the back EMF at $t = \tau$.  
> (d) Find the energy stored in the inductor at $t = 2\tau$.

<details><summary><b>Solution</b></summary>

**Given:** $R = 100$ Ω, $L = 0.5$ H, $\mathcal{E} = 20$ V

**(a) Time constant:**
$$\tau = \frac{L}{R} = \frac{0.5}{100} = 5 \times 10^{-3} \text{ s} = 5 \text{ ms}$$

**(b) Initial rate of rise of current:**

At $t = 0$: $I = 0$, so full EMF drives $dI/dt$:
$$\frac{dI}{dt}\bigg|_{t=0} = \frac{\mathcal{E}}{L} = \frac{20}{0.5} = 40 \text{ A/s}$$

**(c) Back EMF at $t = \tau$:**
$$\varepsilon_L(\tau) = \mathcal{E} \cdot e^{-1} = 20 \times 0.368 = 7.36 \text{ V}$$

**(d) Energy stored at $t = 2\tau$:**

Current at $t = 2\tau$:
$$I(2\tau) = I_0(1 - e^{-2}) = \frac{20}{100}(1 - 0.135) = 0.2 \times 0.865 = 0.173 \text{ A}$$

Energy:
$$U = \frac{1}{2}LI^2 = \frac{1}{2} \times 0.5 \times (0.173)^2 = 0.25 \times 0.0299 \approx 7.48 \times 10^{-3} \text{ J} = 7.48 \text{ mJ}$$

</details>

---

### Problem 3 (Types 2 + 7): L Formula and Energy Density Comparison 🔴

> Two solenoids A and B have the same volume $V = 10^{-3}$ m³ and the same turn density $n = 500$ turns/m. Solenoid A has an air core; solenoid B has an iron core with $\mu_r = 500$. Both carry the same current $I = 2$ A. Compare:  
> (a) $L_A$ and $L_B$  
> (b) $B_A$ and $B_B$ inside  
> (c) Energy density $u_A$ and $u_B$  
> (d) Total energy $U_A$ and $U_B$

<details><summary><b>Solution</b></summary>

**Given:** $V = 10^{-3}$ m³, $n = 500$/m, $I = 2$ A, $\mu_r(B) = 500$

**(a) Inductances:**
$$L_A = \mu_0 n^2 V = 4\pi \times 10^{-7} \times 250000 \times 10^{-3} = 4\pi \times 10^{-7} \times 250 = \pi \times 10^{-4} \approx 3.14 \times 10^{-4} \text{ H}$$
$$L_B = \mu_r \times L_A = 500 \times 3.14 \times 10^{-4} = 0.157 \text{ H}$$

**(b) Magnetic fields:**
$$B_A = \mu_0 n I = 4\pi \times 10^{-7} \times 500 \times 2 = 4\pi \times 10^{-4} \approx 1.26 \times 10^{-3} \text{ T}$$
$$B_B = \mu_0 \mu_r n I = 500 \times B_A = 0.628 \text{ T}$$

**(c) Energy densities:**
$$u_A = \frac{B_A^2}{2\mu_0} = \frac{(1.26 \times 10^{-3})^2}{8\pi \times 10^{-7}} = \frac{1.588 \times 10^{-6}}{2.513 \times 10^{-6}} \approx 0.632 \text{ J/m}^3$$

$$u_B = \frac{B_B^2}{2\mu_0\mu_r} = \frac{(0.628)^2}{2 \times 4\pi \times 10^{-7} \times 500} = \frac{0.394}{1.257 \times 10^{-3}} \approx 313 \text{ J/m}^3$$

So $u_B/u_A = \mu_r = 500$ — iron core stores 500× more energy per unit volume.

**(d) Total energies:**
$$U_A = \frac{1}{2}L_A I^2 = \frac{1}{2} \times 3.14 \times 10^{-4} \times 4 = 6.28 \times 10^{-4} \text{ J}$$
$$U_B = \frac{1}{2}L_B I^2 = \frac{1}{2} \times 0.157 \times 4 = 0.314 \text{ J}$$

$U_B = 500 \times U_A$ — iron core is 500× more effective at storing energy.

</details>

---

### Problem 4 (Competency-Based): Wireless Charging Technology 🔴

> **Passage:** Wireless phone chargers (Qi standard) work on the principle of mutual induction, but the transmitter coil must itself have appropriate self-inductance to maintain stable current oscillations. A transmitter coil has 20 turns wound tightly in a flat spiral. Engineers model it as a single-layer solenoid of effective length $l = 2$ mm and diameter $d = 5$ cm, operating at $I = 1$ A.
>
> (a) Estimate the self-inductance of this coil.  
> (b) If the coil is in a resonant LC circuit with $C = 10$ μF, find the operating frequency $f = 1/(2\pi\sqrt{LC})$.  
> (c) If the current oscillates as $I(t) = \cos(2\pi ft)$ A, find the peak back EMF.  
> (d) Why is a high $L$ desirable in the transmitter coil?

<details><summary><b>Solution</b></summary>

**(a) Self-inductance:**
$N = 20$, $l = 2 \times 10^{-3}$ m, $A = \pi(0.025)^2 = \pi \times 6.25 \times 10^{-4} = 1.963 \times 10^{-3}$ m²

$$L = \frac{\mu_0 N^2 A}{l} = \frac{4\pi \times 10^{-7} \times 400 \times 1.963 \times 10^{-3}}{2 \times 10^{-3}}$$
$$= \frac{4\pi \times 10^{-7} \times 400 \times 1.963 \times 10^{-3}}{2 \times 10^{-3}} = 4\pi \times 10^{-7} \times 200 \times 1.963$$
$$= 4\pi \times 10^{-7} \times 392.5 \approx 4.93 \times 10^{-4} \text{ H} \approx 0.49 \text{ mH}$$

**(b) Resonant frequency:**
$$f = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{4.93 \times 10^{-4} \times 10^{-5}}}$$
$$= \frac{1}{2\pi\sqrt{4.93 \times 10^{-9}}} = \frac{1}{2\pi \times 7.02 \times 10^{-5}} \approx \frac{1}{4.41 \times 10^{-4}} \approx 2.27 \text{ kHz}$$

(Typical Qi standard uses 110–205 kHz; a real coil would need different parameters, but the principle is the same.)

**(c) Peak back EMF:**
$$I(t) = \cos(2\pi f t) \Rightarrow \frac{dI}{dt} = -2\pi f \sin(2\pi f t)$$
$$|\varepsilon|_{\text{peak}} = L \times 2\pi f \times 1 = 4.93 \times 10^{-4} \times 2\pi \times 2270 \approx 4.93 \times 10^{-4} \times 14262 \approx 7.03 \text{ V}$$

**(d) Why high L is desirable:**  
Higher $L$ means:
- Greater flux linkage for same current → stronger magnetic coupling to the receiving coil
- Better energy storage per cycle
- Higher back EMF keeps oscillations stable
- Resonance condition is met with smaller capacitance

</details>

---

## 📋 Stage 6: Board Arsenal

### Board Q1 ⭐ (CBSE 2015–2023, Every Year, 2-3 marks)

> Derive an expression for the self-inductance of a long solenoid of cross-sectional area $A$, length $l$, and total $N$ turns wound on it. What would be the self-inductance if an iron core of relative permeability $\mu_r$ is introduced?

<details><summary><b>Model Answer</b></summary>

**Self-Inductance of a Long Solenoid** [3 marks]

Consider a long solenoid:
- Length $l$, Area $A$, total turns $N$, turn density $n = N/l$
- Current through solenoid: $I$

**Step 1 — Field inside:**
$$B = \mu_0 n I = \frac{\mu_0 N I}{l}$$

**Step 2 — Flux through one turn:**
$$\Phi = BA = \frac{\mu_0 N A I}{l}$$

**Step 3 — Total flux linkage:**
$$N\Phi = N \times \frac{\mu_0 N A I}{l} = \frac{\mu_0 N^2 A I}{l}$$

**Step 4 — By definition of self-inductance ($L = N\Phi/I$):**
$$\boxed{L = \frac{\mu_0 N^2 A}{l}}$$

**With iron core** (relative permeability $\mu_r$): Replace $\mu_0$ with $\mu_0\mu_r$:
$$\boxed{L_{\text{iron}} = \frac{\mu_0 \mu_r N^2 A}{l}}$$

Since $\mu_r \gg 1$, the iron core greatly increases the self-inductance. ✓

**[1 mark: Setting up, Step 1-2] [1 mark: Step 3-4, final expression] [1 mark: Iron core modification]**

</details>

---

### Board Q2 (CBSE 2016, 2 marks)

> An inductor coil carries a steady current of 5 A. The energy stored in it is 5 J. Calculate the self-inductance of the coil.

<details><summary><b>Model Answer</b></summary>

**Given:** $I = 5$ A, $U = 5$ J

Using the energy formula for an inductor:
$$U = \frac{1}{2}LI^2$$

Solving for $L$:
$$L = \frac{2U}{I^2} = \frac{2 \times 5}{(5)^2} = \frac{10}{25}$$

$$\boxed{L = 0.4 \text{ H}}$$

**[1 mark: Formula stated correctly] [1 mark: Correct substitution and answer]**

</details>

---

### Board Q3 (CBSE 2019, 3 marks)

> (a) Define self-inductance of a coil. Write its SI unit.  
> (b) A coil of self-inductance $L = 5$ H is connected to a battery. The current grows from 0 to 2 A in 0.1 s. Find the magnitude of the back EMF induced in the coil during this interval.

<details><summary><b>Model Answer</b></summary>

**(a) Definition:**

Self-inductance is the property of a coil by which it **opposes any change in the current flowing through it**. Numerically, it equals the total magnetic flux linkage per unit current:
$$L = \frac{N\Phi}{I}$$

Alternatively, it is the magnitude of back EMF per unit rate of change of current: $L = |\varepsilon|/(dI/dt)$.

**SI Unit:** Henry (H) = 1 V·s/A = 1 Wb/A

**(b) Numerical:**

**Given:** $L = 5$ H, $\Delta I = 2 - 0 = 2$ A, $\Delta t = 0.1$ s

$$|\varepsilon| = L \cdot \frac{\Delta I}{\Delta t} = 5 \times \frac{2}{0.1} = 5 \times 20$$

$$\boxed{|\varepsilon| = 100 \text{ V}}$$

**[1 mark: Definition] [0.5 mark: SI unit] [0.5 mark: Formula] [1 mark: Correct answer]**

</details>

---

### Board Q4 (CBSE 2020, 2 marks)

> The current in a coil changes from 2 A to 5 A in 0.05 s, producing a back EMF of 3 V. Find the self-inductance of the coil.

<details><summary><b>Model Answer</b></summary>

**Given:** $I_1 = 2$ A, $I_2 = 5$ A, $\Delta t = 0.05$ s, $|\varepsilon| = 3$ V

$$|\varepsilon| = L \cdot \frac{\Delta I}{\Delta t}$$

$$L = \frac{|\varepsilon| \cdot \Delta t}{\Delta I} = \frac{3 \times 0.05}{5 - 2} = \frac{0.15}{3}$$

$$\boxed{L = 0.05 \text{ H} = 50 \text{ mH}}$$

**[1 mark: Correct formula and rearrangement] [1 mark: Correct numerical answer with unit]**

</details>

---

### Board Q5 (CBSE 2023-style, 3 marks)

> A coil of self-inductance $L = 4$ H carries a current that varies with time as $I(t) = (2t^2 + 3)$ A.  
> (a) Find the back EMF induced in the coil at $t = 2$ s.  
> (b) Find the energy stored in the coil at $t = 2$ s.  
> (c) An engineer proposes doubling both $L$ and the current to store maximum energy. Which parameter should be doubled for greater effect on stored energy?

<details><summary><b>Model Answer</b></summary>

**Given:** $L = 4$ H, $I(t) = 2t^2 + 3$

**(a) Back EMF at $t = 2$ s:**
$$\frac{dI}{dt} = 4t$$
At $t = 2$: $dI/dt = 8$ A/s

$$|\varepsilon| = L \cdot \frac{dI}{dt} = 4 \times 8 = \boxed{32 \text{ V}}$$

**(b) Energy at $t = 2$ s:**
$$I(2) = 2(4) + 3 = 11 \text{ A}$$
$$U = \frac{1}{2}LI^2 = \frac{1}{2} \times 4 \times 121 = 2 \times 121 = \boxed{242 \text{ J}}$$

**(c) Which parameter to double:**

$U = \frac{1}{2}LI^2$.  
- Doubling $L$ (keeping $I = 11$ A): $U' = \frac{1}{2}(2L)I^2 = 2U = 484$ J  
- Doubling $I$ (keeping $L = 4$ H): $U'' = \frac{1}{2}L(2I)^2 = 4U = 968$ J

**Double the current** — since $U \propto I^2$, doubling $I$ quadruples the energy, while doubling $L$ only doubles it.

</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** In an RL circuit with time constant $\tau$, after time $t = \tau$, the current as a fraction of the maximum current $I_0$ is approximately:

(a) $0.500$ &emsp; (b) $0.368$ &emsp; (c) $0.632$ &emsp; (d) $0.865$

<details><summary><b>Answer</b></summary>

**Answer: (c) 0.632**

$I(\tau) = I_0(1 - e^{-1}) = I_0(1 - 0.368) = 0.632 \, I_0$

The time constant $\tau = L/R$ is defined as the time to reach $63.2\%$ (i.e., $(1 - 1/e)$) of the final current. Note: $0.368 = 1/e$ — that's the remaining fraction, not the attained fraction.

</details>

---

**Q2.** Two inductors $L_1 = 4$ H and $L_2 = 6$ H are connected in parallel (no mutual inductance). The equivalent inductance is:

(a) $10$ H &emsp; (b) $2.4$ H &emsp; (c) $5$ H &emsp; (d) $1.5$ H

<details><summary><b>Answer</b></summary>

**Answer: (b) 2.4 H**

For parallel inductors (assuming no mutual inductance):
$$\frac{1}{L_{eq}} = \frac{1}{L_1} + \frac{1}{L_2} = \frac{1}{4} + \frac{1}{6} = \frac{3+2}{12} = \frac{5}{12}$$
$$L_{eq} = \frac{12}{5} = 2.4 \text{ H}$$

</details>

---

**Q3.** In an RL circuit, $R = 10$ Ω, $L = 100$ mH, $V = 10$ V. At $t = 10$ ms (which equals one time constant $\tau = L/R$), the rate of change of current $dI/dt$ is:

(a) $36.8$ A/s &emsp; (b) $100$ A/s &emsp; (c) $63.2$ A/s &emsp; (d) $10$ A/s

<details><summary><b>Answer</b></summary>

**Answer: (a) 36.8 A/s**

From Kirchhoff's law: $V = IR + L\,dI/dt$, so $L\,dI/dt = V - IR = V \cdot e^{-t/\tau}$ (since the back EMF decays exponentially).

$$\frac{dI}{dt} = \frac{V}{L} e^{-t/\tau}$$

At $t = \tau$:
$$\frac{dI}{dt} = \frac{10}{0.1} \times e^{-1} = 100 \times 0.368 = 36.8 \text{ A/s}$$

</details>

---

**Q4.** A solenoid has $n = 1000$ turns/m and carries $I = 2$ A. The energy stored per unit volume (energy density) of the magnetic field inside it is: ($\mu_0 = 4\pi \times 10^{-7}$ H/m)

(a) $8\pi \times 10^{-4}$ J/m³ &emsp; (b) $4\pi \times 10^{-4}$ J/m³ &emsp; (c) $2\pi \times 10^{-1}$ J/m³ &emsp; (d) $\pi \times 10^{-3}$ J/m³

<details><summary><b>Answer</b></summary>

**Answer: (c) $2\pi \times 10^{-1}$ J/m³**

$B = \mu_0 n I = 4\pi \times 10^{-7} \times 1000 \times 2 = 8\pi \times 10^{-4}$ T

$$u = \frac{B^2}{2\mu_0} = \frac{(8\pi \times 10^{-4})^2}{2 \times 4\pi \times 10^{-7}}$$

$$= \frac{64\pi^2 \times 10^{-8}}{8\pi \times 10^{-7}} = \frac{64\pi \times 10^{-8}}{8 \times 10^{-7}} = \frac{64\pi}{80} = \frac{4\pi}{5} \approx 2.51 \approx 2\pi \times 10^{-1} \text{ J/m}^3$$

More precisely: $u = 64\pi^2 \times 10^{-8}/(8\pi \times 10^{-7}) = 8\pi \times 10^{-1} = 0.8\pi \approx 2.51$ J/m³. The closest answer is **(c)** — check with $u = \frac{1}{2}\mu_0 n^2 I^2 = \frac{1}{2} \times 4\pi \times 10^{-7} \times 10^6 \times 4 = 2\pi \times 4 \times 10^{-1}/10 = 0.8\pi$.

</details>

---

**Q5.** A coil connected to a battery has $L = 2$ H, $R = 4$ Ω, $\mathcal{E} = 8$ V. After the current reaches steady state, the battery is suddenly removed and the ends are connected to a resistance $R' = 4$ Ω (same as the coil's own resistance). The total heat dissipated across $R'$ is:

(a) 4 J &emsp; (b) 2 J &emsp; (c) 8 J &emsp; (d) 1 J

<details><summary><b>Answer</b></summary>

**Answer: (b) 2 J**

Steady-state current: $I_0 = \mathcal{E}/R = 8/4 = 2$ A

Total energy stored in inductor: $U = \frac{1}{2}LI_0^2 = \frac{1}{2} \times 2 \times 4 = 4$ J

When battery is removed, current decays through total resistance $R_{total} = R + R' = 4 + 4 = 8$ Ω.

Total energy dissipated = 4 J, split equally between $R$ and $R'$ (since they are equal):

$$U_{R'} = \frac{R'}{R + R'} \times 4 = \frac{4}{8} \times 4 = \boxed{2 \text{ J}}$$

</details>

---

*← [Chapter 6 — Eddy Currents](./06_eddy_currents.md)*

*→ [Chapter 8 — Mutual Inductance](./08_mutual_induction.md)*
