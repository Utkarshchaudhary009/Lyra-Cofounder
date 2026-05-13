# Chapter 1: Electric Current — The Flow of Charge

> *NCERT Sections 3.1–3.2*

---

## 🎯 Stage 1: The Core Idea

### What Is Electric Current?

Imagine a crowded corridor during lunch break. Students are walking randomly in every direction — no net movement anywhere. Now imagine the fire alarm goes off: suddenly, everyone rushes toward the exit. There's now a *net flow* of students in one direction.

**Electric current is exactly like this.**

Inside a metal conductor, free electrons are always jiggling around randomly at enormous speeds (~10⁶ m/s). But there's no net flow — just chaos. Now connect a battery: it creates an electric field inside the wire, and all those electrons start drifting slowly (very slowly — ~10⁻⁴ m/s) in one direction.

> **Electric current is the rate of flow of electric charge through a cross-section of a conductor.**

$$I = \frac{Q}{t} \quad \text{(steady current)}$$
$$I = \frac{dQ}{dt} \quad \text{(instantaneous current)}$$

### Key Insights

1. **Current is a scalar**, not a vector. It doesn't obey vector addition laws. When we say "current flows from A to B," we mean the direction of flow, not a vector direction.

2. **Conventional current** flows from positive (+) to negative (−) terminal *outside* the cell. This is opposite to the actual electron flow! Benjamin Franklin's mistake strikes again.

3. **Current requires a closed circuit.** No complete loop → no sustained current.

### Types of Current

| Type | Description | Example |
|------|-------------|---------|
| Steady (DC) | Constant magnitude and direction | Battery-powered torch |
| Varying | Magnitude changes with time | Charging capacitor |
| Alternating (AC) | Periodically reverses direction | Household supply |

---

## 🔬 Stage 2: The Formula Lab

### The Core Formula

$$I = \frac{Q}{t} = \frac{ne}{t}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| I | Electric current | Ampere (A) |
| Q | Total charge flowing | Coulomb (C) |
| t | Time | Second (s) |
| n | Number of electrons | Dimensionless |
| e | Elementary charge | 1.6 × 10⁻¹⁹ C |

### Definition of 1 Ampere

> **1 Ampere** is the current flowing through a conductor when **1 Coulomb** of charge passes through any cross-section in **1 second**.

$$1 \text{ A} = \frac{1 \text{ C}}{1 \text{ s}}$$

### Smaller Units

| Unit | Symbol | Value |
|------|--------|-------|
| Milliampere | mA | 10⁻³ A |
| Microampere | μA | 10⁻⁶ A |
| Nanoampere | nA | 10⁻⁹ A |

### Charge as Integral of Current

For non-steady current:

$$Q = \int_0^t I \, dt$$

> 💡 **Graphical interpretation:** The charge flowing in time t equals the **area under the I-t curve**.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Calculate current from charge and time ⭐

**Pattern:** "Q coulombs of charge flow in t seconds. Find I."

**Solved Example** 🟢

> A charge of 600 C flows through a conductor in 5 minutes. Find the current.

<details>
<summary><b>Solution</b></summary>

- Q = 600 C, t = 5 min = 300 s
- I = Q/t = 600/300 = **2 A**
</details>

**Practice:**

1. 🟢 A charge of 180 C flows through a wire in 1 minute. Find the current.

<details>
<summary><b>Answer</b></summary>

I = 180/60 = **3 A**
</details>

2. 🟢 A current of 0.5 A flows for 10 minutes. How much charge passes through the conductor?

<details>
<summary><b>Answer</b></summary>

Q = It = 0.5 × 600 = **300 C**
</details>

3. 🟡 A charge of 4.8 × 10⁴ C is transferred in 2 hours. Calculate the current in milliamperes.

<details>
<summary><b>Answer</b></summary>

t = 2 × 3600 = 7200 s
I = 4.8 × 10⁴ / 7200 = 6.67 A = **6670 mA**
</details>

4. 🟡 How long will it take for 10⁴ C of charge to flow if the current is 500 mA?

<details>
<summary><b>Answer</b></summary>

t = Q/I = 10⁴ / 0.5 = **20000 s ≈ 5.56 hours**
</details>

---

### Type 2: Current from electron flow rate ⭐

**Pattern:** "n electrons pass through a cross-section in t seconds. Find I."

**Solved Example** 🟢

> 6.25 × 10¹⁸ electrons pass through a cross-section of a wire in 1 second. Find the current.

<details>
<summary><b>Solution</b></summary>

- Q = ne = 6.25 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 1 C
- I = Q/t = 1/1 = **1 A**
</details>

**Practice:**

1. 🟢 10²⁰ electrons flow through a wire in 4 seconds. Find the current.

<details>
<summary><b>Answer</b></summary>

Q = 10²⁰ × 1.6 × 10⁻¹⁹ = 16 C
I = 16/4 = **4 A**
</details>

2. 🟡 A current of 2 A flows through a conductor. How many electrons pass a cross-section per second?

<details>
<summary><b>Answer</b></summary>

Q = It = 2 × 1 = 2 C
n = Q/e = 2 / (1.6 × 10⁻¹⁹) = **1.25 × 10¹⁹ electrons**
</details>

3. 🟡 ⭐ A current of 5 A flows through a metallic conductor for 2 minutes. Calculate (a) the total charge, (b) the number of electrons that flow.

<details>
<summary><b>Answer</b></summary>

(a) Q = It = 5 × 120 = **600 C**
(b) n = Q/e = 600 / (1.6 × 10⁻¹⁹) = **3.75 × 10²¹ electrons**
</details>

4. 🟡 If 10⁶ electrons are removed from a conductor every microsecond, what current does this constitute?

<details>
<summary><b>Answer</b></summary>

Q/t = ne/t = 10⁶ × 1.6 × 10⁻¹⁹ / 10⁻⁶ = 1.6 × 10⁻⁷ A = **0.16 μA**
</details>

5. 🔴 A current of 1.6 mA flows through a conductor. How many electrons pass through a cross-section in 1 nanosecond?

<details>
<summary><b>Answer</b></summary>

Q = It = 1.6 × 10⁻³ × 10⁻⁹ = 1.6 × 10⁻¹² C
n = Q/e = 1.6 × 10⁻¹² / 1.6 × 10⁻¹⁹ = **10⁷ electrons**
</details>

---

### Type 3: Non-uniform current — charge from I(t) ⭐

**Pattern:** "Current varies as I = f(t). Find charge in time interval."

**Solved Example** 🟡

> The current through a conductor is given by I = (3t² + 2t) A. Find the charge flowing in the interval t = 2s to t = 4s.

<details>
<summary><b>Solution</b></summary>

$$Q = \int_2^4 (3t^2 + 2t) \, dt = \left[t^3 + t^2\right]_2^4$$
$$= (64 + 16) - (8 + 4) = 80 - 12 = \textbf{68 C}$$
</details>

**Practice:**

1. 🟡 I = 5t A. Find Q from t = 0 to t = 4 s.

<details>
<summary><b>Answer</b></summary>

Q = ∫₀⁴ 5t dt = 5[t²/2]₀⁴ = 5 × 8 = **40 C**
</details>

2. 🟡 I = (2 + 3t²) A. Find Q from t = 1 to t = 3 s.

<details>
<summary><b>Answer</b></summary>

Q = ∫₁³ (2 + 3t²) dt = [2t + t³]₁³ = (6 + 27) − (2 + 1) = **30 C**
</details>

3. 🔴 ⭐ I = 4e⁻²ᵗ A. Find the total charge from t = 0 to t = ∞.

<details>
<summary><b>Answer</b></summary>

Q = ∫₀^∞ 4e⁻²ᵗ dt = 4 × [−1/2 × e⁻²ᵗ]₀^∞ = 4 × (0 − (−1/2)) = **2 C**
</details>

4. 🔴 I = I₀ sin(ωt). Find the charge flowing in one complete cycle (0 to 2π/ω).

<details>
<summary><b>Answer</b></summary>

Q = ∫₀^(2π/ω) I₀ sin(ωt) dt = I₀ × [−cos(ωt)/ω]₀^(2π/ω)
= I₀/ω × [−cos(2π) + cos(0)] = I₀/ω × [−1 + 1] = **0**

Net charge in one full cycle of AC is zero!
</details>

---

### Type 4: Charge from I-t graph ⭐

**Pattern:** "Given an I-t graph, find the charge."

**Solved Example** 🟡

> A current varies linearly from 0 to 10 A over 5 seconds, then stays constant at 10 A for 3 more seconds. Find the total charge.

<details>
<summary><b>Solution</b></summary>

- Phase 1 (triangle): Q₁ = ½ × base × height = ½ × 5 × 10 = 25 C
- Phase 2 (rectangle): Q₂ = 10 × 3 = 30 C
- **Total Q = 25 + 30 = 55 C**
</details>

**Practice:**

1. 🟢 Current is constant at 3 A for 10 seconds. Find Q from the I-t graph.

<details>
<summary><b>Answer</b></summary>

Q = area of rectangle = 3 × 10 = **30 C**
</details>

2. 🟡 Current increases linearly from 2 A to 8 A over 6 seconds. Find Q.

<details>
<summary><b>Answer</b></summary>

Q = area of trapezium = ½ × (2 + 8) × 6 = **30 C**
</details>

3. 🟡 An I-t graph shows a triangular pulse: I rises from 0 to 5 A in 4 s, then drops back to 0 in 4 s. Find Q.

<details>
<summary><b>Answer</b></summary>

Q = area of triangle = ½ × 8 × 5 = **20 C**
</details>

---

### Type 5: Direction of conventional vs electron current

**Pattern:** "In which direction does current flow? / Identify electron flow direction."

**Solved Example** 🟢

> In an external circuit, electrons flow from terminal A to terminal B of a battery. What is the direction of conventional current?

<details>
<summary><b>Solution</b></summary>

Conventional current is opposite to electron flow.
∴ Conventional current flows from **B to A** in the external circuit.
This means B is the positive terminal and A is the negative terminal.
</details>

**Practice:**

1. 🟢 Electrons drift from right to left through a wire. What is the direction of conventional current?

<details>
<summary><b>Answer</b></summary>

Conventional current flows **left to right** (opposite to electron flow).
</details>

2. 🟡 A battery drives a current of 2 A through an external circuit from its positive terminal P to a bulb and back to its negative terminal N. In which direction do the electrons actually move?

<details>
<summary><b>Answer</b></summary>

Electrons move from **N (negative terminal) → through external circuit → to P (positive terminal)** — opposite to conventional current.
</details>

3. 🟡 Current flows clockwise in a circular loop when viewed from above. What is the direction of electron flow?

<details>
<summary><b>Answer</b></summary>

Electrons flow **anticlockwise** when viewed from above.
</details>

---

### Type 6: Current through multiple carriers

**Pattern:** "Both positive and negative charges move. Find net current."

**Solved Example** 🔴

> In an electrolyte, 10²⁰ positive ions (each with charge +e) move to the right per second, and 5 × 10¹⁹ negative ions (each with charge −e) move to the left per second. Find the net current and its direction.

<details>
<summary><b>Solution</b></summary>

- Current due to positive ions moving right: I₁ = n₁e/t = 10²⁰ × 1.6 × 10⁻¹⁹ = 16 A (to the right)
- Current due to negative ions moving left: Negative charges moving left = conventional current to the right!
  I₂ = n₂e/t = 5 × 10¹⁹ × 1.6 × 10⁻¹⁹ = 8 A (to the right)
- **Net current = 16 + 8 = 24 A to the right**

> 🔑 Key insight: When positive charges move in one direction and negative charges move in the opposite direction, their contributions to conventional current ADD UP.
</details>

**Practice:**

1. 🟡 In a discharge tube, 10¹⁸ protons move left per second and 2 × 10¹⁸ electrons move right per second. Find the current and its direction.

<details>
<summary><b>Answer</b></summary>

I_protons = 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.16 A (to the left — same as proton motion)
I_electrons = 2 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.32 A (to the left — opposite to electron motion)
**Net current = 0.16 + 0.32 = 0.48 A to the left**
</details>

2. 🔴 In a semiconductor, 5 × 10¹⁸ electrons per second move from A to B, and 3 × 10¹⁸ holes per second move from A to B. Find the net current and its direction.

<details>
<summary><b>Answer</b></summary>

I_electrons = 5 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.8 A (from B to A — conventional, opposite to electron motion)
I_holes = 3 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.48 A (from A to B — same as hole motion)

These are in opposite directions!
Net current = 0.8 − 0.48 = **0.32 A from B to A**

Wait — let me reconsider. Electrons move A→B, so conventional current due to electrons is B→A. Holes move A→B, so conventional current due to holes is A→B.
Net = 0.8 (B→A) − 0.48 (A→B) = **0.32 A from B to A**
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🟡 ⭐ A steady current of 8 A flows through a conductor for 3 minutes. (a) How much charge flows? (b) How many electrons pass through any cross-section? (c) If the current direction reverses, in which direction do the electrons actually move now?

<details>
<summary><b>Solution</b></summary>

(a) Q = It = 8 × 180 = **1440 C**

(b) n = Q/e = 1440 / (1.6 × 10⁻¹⁹) = **9 × 10²¹ electrons**

(c) If conventional current reverses direction, electrons now drift in the **original conventional current direction** (since electron flow is always opposite to conventional current).
</details>

**Q2.** 🟡 The current through a wire is given by I = (6t + 4) A. (a) Find the charge flowing between t = 0 and t = 3 s. (b) How many electrons flow in this time? (c) What is the average current?

<details>
<summary><b>Solution</b></summary>

(a) Q = ∫₀³ (6t + 4) dt = [3t² + 4t]₀³ = 27 + 12 = **39 C**

(b) n = 39 / (1.6 × 10⁻¹⁹) = **2.4375 × 10²⁰ electrons**

(c) I_avg = Q/t = 39/3 = **13 A**
</details>

**Q3.** 🔴 ⭐ In an electrolyte solution, Na⁺ ions move to the right at a rate of 4 × 10¹⁸ per second and Cl⁻ ions move to the left at a rate of 3.6 × 10¹⁸ per second. (a) Find the current due to each ion. (b) Find the total current. (c) How much charge passes through a cross-section in 10 seconds?

<details>
<summary><b>Solution</b></summary>

(a) I_Na⁺ = 4 × 10¹⁸ × 1.6 × 10⁻¹⁹ = **0.64 A** (to the right)
    I_Cl⁻ = 3.6 × 10¹⁸ × 1.6 × 10⁻¹⁹ = **0.576 A** (to the right — negative ions moving left contribute current to the right)

(b) Total I = 0.64 + 0.576 = **1.216 A** (to the right)

(c) Q = It = 1.216 × 10 = **12.16 C**
</details>

**Q4.** 🔴 The current in a circuit varies as shown: I = 2 A for 0 ≤ t ≤ 5 s, then I = (12 − 2t) A for 5 < t ≤ 6 s, then I = 0. Find: (a) total charge, (b) average current over the entire 6 s interval.

<details>
<summary><b>Solution</b></summary>

(a) Q₁ = 2 × 5 = 10 C (rectangle)
Q₂ = ∫₅⁶ (12 − 2t) dt = [12t − t²]₅⁶ = (72 − 36) − (60 − 25) = 36 − 35 = 1 C

Total Q = 10 + 1 = **11 C**

(b) I_avg = Q/t = 11/6 = **1.83 A**
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 ⭐ Define electric current. Is it a scalar or vector? Why? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Electric current** is defined as the rate of flow of electric charge through any cross-section of a conductor. Mathematically, I = Q/t (for steady current) or I = dQ/dt (for varying current).

Electric current is a **scalar quantity**. Although current has a direction (along the wire), it does not obey the laws of vector addition. For example, when two currents meet at a junction, the resultant is found by algebraic addition, not vector addition. Hence, current is treated as a scalar.
</details>

**Q2.** 🟢 ⭐ Define the SI unit of electric current. *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

The SI unit of electric current is the **ampere (A)**. One ampere is defined as the current flowing through a conductor when one coulomb of charge passes through any cross-section in one second.

1 A = 1 C / 1 s
</details>

**Q3.** 🟡 ⭐ Distinguish between conventional current and electron current. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

| Property | Conventional Current | Electron Current |
|----------|---------------------|-----------------|
| Direction | From positive to negative terminal (external circuit) | From negative to positive terminal (external circuit) |
| Carriers | Assumed to be positive charges | Actual electrons (negative charges) |
| Convention | Established by Benjamin Franklin | Discovered later |
| Relation | Opposite to electron flow | Opposite to conventional current |

Both have the same magnitude and produce the same effects in a circuit.
</details>

**Q4.** 🟡 A current of 0.4 A is drawn by a filament of an electric bulb for 25 minutes. Find the amount of electric charge that flows through the circuit. *(NCERT)* *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Given: I = 0.4 A, t = 25 min = 25 × 60 = 1500 s

Q = It = 0.4 × 1500 = **600 C**
</details>

**Q5.** 🟡 In a discharge tube, 2 × 10¹⁸ electrons and 1.5 × 10¹⁸ singly-charged positive ions pass through a cross-section per second in opposite directions. Find the total current. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

Current due to electrons = n_e × e = 2 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.32 A
Current due to positive ions = n_p × e = 1.5 × 10¹⁸ × 1.6 × 10⁻¹⁹ = 0.24 A

Since electrons and positive ions move in opposite directions, both contribute to conventional current in the **same** direction.

**Total current = 0.32 + 0.24 = 0.56 A**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The charge flowing through a resistance R varies with time as Q = at − bt², where a and b are positive constants. The total heat produced in the resistance is:

(a) a³/6b &emsp; (b) a³R/6b &emsp; (c) a³/3bR &emsp; (d) a³R/3b

<details>
<summary><b>Answer</b></summary>

I = dQ/dt = a − 2bt

Current becomes zero at t₀ = a/(2b)

Heat H = ∫₀^(a/2b) I²R dt = R ∫₀^(a/2b) (a − 2bt)² dt

Let u = a − 2bt, du = −2b dt

H = R/(2b) ∫ₐ⁰ u² du = R/(2b) × [u³/3]ₐ⁰ = R/(2b) × a³/3 = **a³R/6b**

**Answer: (b)**
</details>

**Q2.** 🟡 A wire carries a current of 2 A. The number of electrons per second passing through a cross-section of the wire is:

(a) 1.25 × 10¹⁹ &emsp; (b) 6.25 × 10¹⁸ &emsp; (c) 1.6 × 10¹⁹ &emsp; (d) 3.2 × 10¹⁸

<details>
<summary><b>Answer</b></summary>

n = I/e = 2 / (1.6 × 10⁻¹⁹) = **1.25 × 10¹⁹**

**Answer: (a)**
</details>

**Q3.** 🟡 ⭐ The current flowing through a conductor is given by I = (3 + 4t) A, where t is in seconds. The charge flowing through the conductor from t = 1 to t = 3 s is:

(a) 22 C &emsp; (b) 24 C &emsp; (c) 18 C &emsp; (d) 22 C

<details>
<summary><b>Answer</b></summary>

Q = ∫₁³ (3 + 4t) dt = [3t + 2t²]₁³ = (9 + 18) − (3 + 2) = 27 − 5 = **22 C**

**Answer: (a)**
</details>

**Q4.** 🔴 ⭐ A current of 5 A is passing through a metallic conductor of cross-sectional area 4 × 10⁻⁶ m². If the density of the charge carriers is 5 × 10²⁶ m⁻³, the drift velocity of the electrons is:

(a) 1.6 × 10⁻² m/s &emsp; (b) 1.56 × 10⁻² m/s &emsp; (c) 1.56 × 10⁻³ m/s &emsp; (d) 1.56 × 10⁻⁴ m/s

<details>
<summary><b>Answer</b></summary>

I = nAevd → vd = I/(nAe)
= 5 / (5 × 10²⁶ × 4 × 10⁻⁶ × 1.6 × 10⁻¹⁹)
= 5 / (5 × 4 × 1.6 × 10¹)
= 5 / 320
= **1.56 × 10⁻² m/s**

**Answer: (b)**
</details>

**Q5.** 🔴 A charge Q flows through a conductor in time t. If the same charge Q passes in time t/2, the new current is:

(a) I/2 &emsp; (b) I &emsp; (c) 2I &emsp; (d) 4I

<details>
<summary><b>Answer</b></summary>

I = Q/t → I' = Q/(t/2) = 2Q/t = **2I**

**Answer: (c)**

This looks trivially easy but is a common trap — students sometimes overthink it.
</details>

---

*Next: [Chapter 2 — Drift Velocity, Mobility & Current Density →](./02_drift_velocity.md)*
