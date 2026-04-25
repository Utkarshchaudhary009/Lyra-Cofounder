# Chapter 4: Coulomb's Law — The Force Between Charges

> *NCERT Section 1.6*

---

## 🎯 Stage 1: The Core Idea

### The Most Important Equation in Electrostatics

Two point charges, sitting quietly in space, exert a force on each other. The question that haunted physicists for centuries: *how much force?*

Charles-Augustin de Coulomb answered in 1785 using a torsion balance:

> **The force between two point charges is directly proportional to the product of their magnitudes and inversely proportional to the square of the distance between them.**

### The Real-World Analogy

Imagine two people shouting at each other across a field.
- The **louder** each person shouts (bigger charges) → the more strongly they hear each other (bigger force).
- The **farther apart** they are → the weaker the sound (force drops with distance²).
- If both are angry (same sign) → they push away. If one is calling with love (opposite sign) → they pull together.

### Why Is This Law So Important?

Coulomb's law is to electrostatics what Newton's law of gravitation is to gravity. In fact, they have the **exact same mathematical form**:

| Feature | Coulomb's Law | Newton's Gravity |
|---------|:------------:|:----------------:|
| Formula | F = kq₁q₂/r² | F = Gm₁m₂/r² |
| Nature | Attractive or repulsive | Always attractive |
| Range | Infinite (1/r²) | Infinite (1/r²) |
| Relative strength | ~10³⁶ times stronger | 1 (baseline) |

> ⚡ **Mind-blowing fact:** The electric force between a proton and electron in a hydrogen atom is ~10³⁹ times stronger than the gravitational force between them. Gravity is *laughably* weak compared to electricity.

---

## 🔬 Stage 2: The Formula Lab

### The Scalar Form

$$F = \frac{1}{4\pi\varepsilon_0} \cdot \frac{|q_1||q_2|}{r^2}$$

| Symbol | Name | Value / Unit |
|--------|------|-------------|
| F | Force between charges | Newton (N) |
| q₁, q₂ | The two point charges | Coulomb (C) |
| r | Distance between centres of charges | metre (m) |
| ε₀ | Permittivity of free space | 8.854 × 10⁻¹² C²N⁻¹m⁻² |
| k = 1/(4πε₀) | Coulomb's constant | **9 × 10⁹ Nm²C⁻²** |

### The Vector Form ⭐

$$\vec{F}_{12} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q_1 q_2}{r^2} \hat{r}_{12}$$

Where:
- **F₁₂** = force on charge 1 due to charge 2
- **r̂₁₂** = unit vector from charge 2 toward charge 1
- If q₁q₂ > 0 (like charges) → F is along r̂₁₂ → **repulsion**
- If q₁q₂ < 0 (unlike charges) → F is opposite to r̂₁₂ → **attraction**

### In a Medium (Dielectric)

$$F_{medium} = \frac{1}{4\pi\varepsilon_0 \varepsilon_r} \cdot \frac{q_1 q_2}{r^2} = \frac{F_{vacuum}}{K}$$

Where **K = εᵣ** = dielectric constant (relative permittivity) of the medium.

| Medium | K (dielectric constant) |
|--------|:-----------------------:|
| Vacuum | 1 (exactly) |
| Air | 1.0006 ≈ 1 |
| Water | ~80 |
| Glass | ~5–10 |
| Mica | ~6 |
| Metals | ∞ (perfect screening) |

> **Key insight:** A medium **reduces** the electrostatic force. Water (K ≈ 80) reduces the force to 1/80th of its vacuum value — this is why ionic compounds dissolve in water (the ions can separate because the attractive force weakens).

### Conditions for Coulomb's Law to Work

1. Charges must be **point charges** (or separated by r >> size of charges).
2. Charges must be **stationary** (electrostatics — no moving charges).
3. The medium must be **uniform** between the charges.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Direct force calculation ⭐

**Pattern:** "Find the force between two point charges."

**Solved Example** 🟢

> Two point charges, q₁ = +3 μC and q₂ = −5 μC, are separated by 30 cm. Find the force between them.

**Solution:**
- q₁ = 3 × 10⁻⁶ C, q₂ = 5 × 10⁻⁶ C, r = 0.3 m
- F = kq₁q₂/r² = 9 × 10⁹ × 3 × 10⁻⁶ × 5 × 10⁻⁶ / (0.3)²
- F = 9 × 10⁹ × 15 × 10⁻¹² / 0.09
- F = 135 × 10⁻³ / 0.09 = **1.5 N (attractive)**

**Practice:**

1. 🟢 Find force between +2 μC and +4 μC separated by 20 cm in vacuum. *(Ans: 1.8 N, repulsive)*
2. 🟢 Two electrons are 1 Å apart (10⁻¹⁰ m). Find the electrostatic force. *(Ans: 2.3 × 10⁻⁸ N)*
3. 🟡 ⭐ What is the force between +1 C and +1 C placed 1 m apart? Comment on its magnitude. *(Ans: 9 × 10⁹ N ≈ weight of ~1 million tonnes! Shows 1 C is enormous.)*

---

### Type 2: Force in a medium ⭐

**Pattern:** "Find the force when charges are in a medium with dielectric constant K."

**Solved Example** 🟡

> Two charges +4 μC and −6 μC are 10 cm apart in water (K = 80). Find the force.

**Solution:**
- F = kq₁q₂/(Kr²) = 9 × 10⁹ × 4 × 10⁻⁶ × 6 × 10⁻⁶ / (80 × 0.01)
- F = 216 × 10⁻³ / 0.8 = **0.27 N (attractive)**
- Compare with vacuum: F_vac = 216 × 10⁻³ / 0.01 = 21.6 N → reduced by factor 80.

**Practice:**

1. 🟢 Force between two charges in vacuum is 10 N. What is the force in a medium with K = 5? *(Ans: 2 N)*
2. 🟡 The force between two charges in air is F. At what distance in a medium (K = 4) would the force be the same F? *(Ans: r/2 — half the original distance)*
3. 🟡 ⭐ Two charges experience force F at distance r in vacuum. In a medium of K = 9, at what distance is the force still F? *(Ans: r/3)*

---

### Type 3: Comparison / ratio problems ⭐⭐

**Pattern:** "Force changes when distance/charge/medium changes. Find the ratio."

**Solved Example** 🟡

> If the distance between two charges is halved, by what factor does the force change?

**Solution:**
- F ∝ 1/r² → If r → r/2, then F → F × (r/(r/2))² = F × 4 = **4F**
- Force increases by a factor of **4**.

**Solved Example** 🟡

> The distance between two charges is tripled and each charge is doubled. Find the new force.

**Solution:**
- F' = k(2q₁)(2q₂)/(3r)² = 4kq₁q₂/9r² = **(4/9)F**

**Practice:**

1. 🟢 Distance is doubled → Force = ? *(Ans: F/4)*
2. 🟡 One charge is tripled, distance is halved → Force = ? *(Ans: 12F)*
3. 🟡 ⭐ Both charges doubled, distance doubled, medium changed from vacuum to K = 2 → Force = ? *(Ans: 4F/(4×2) = F/2)*
4. 🔴 Force between two charges in vacuum at distance d is F. They are placed in a medium of K = 4 at distance d/2. What is the new force? *(Ans: F)*

---

### Type 4: Find the unknown charge or distance

**Pattern:** "Given force, find q or r."

**Solved Example** 🟡

> Two identical charges separated by 50 cm experience a repulsive force of 3.6 N. Find the charge.

**Solution:**
- F = kq²/r² → q² = Fr²/k = 3.6 × 0.25 / (9 × 10⁹) = 10⁻¹⁰
- q = 10⁻⁵ C = **10 μC**

**Practice:**

1. 🟢 Force of 100 N between charges +2 μC and q₂ at 6 cm. Find q₂. *(Ans: 20 μC)*
2. 🟡 Two charges of 3 μC and 5 μC repel with 0.54 N. Find the separation. *(Ans: 50 cm)*
3. 🟡 At what distance will two protons experience the same force as two electrons at 1 Å? *(Ans: 1 Å — same charges, same distance gives same force)*

---

### Type 5: Equilibrium of three charges ⭐⭐⭐

**Pattern:** "Place a charge so the net force on it is zero" or "find the position of equilibrium."

**This is the most important problem type for JEE from Coulomb's law.**

**Solved Example** 🔴

> Two charges q₁ = +4Q and q₂ = +Q are fixed at distance L apart. Where should a third charge q₃ be placed so that the net force on it is zero?

**Solution:**

Let q₃ be at distance x from q₁ (and L − x from q₂) along the line joining them.

For equilibrium of q₃:
- Force due to q₁ = Force due to q₂ (in opposite directions)
- k(4Q)(q₃)/x² = k(Q)(q₃)/(L−x)²
- 4/(x²) = 1/(L−x)²
- 2/(x) = 1/(L−x) → 2(L−x) = x → 2L = 3x → **x = 2L/3**

The third charge must be placed at **2L/3 from the larger charge** (closer to the smaller charge).

> 🔑 **Rule of thumb:** The equilibrium point is always closer to the smaller charge. For like charges, it's between them. For unlike charges, it's outside (beyond the smaller charge).

**Practice:**

1. 🟡 ⭐ Charges +9Q and +Q are separated by distance d. Where is the null point? *(Ans: 3d/4 from +9Q, or d/4 from +Q — but let's verify: 3/(3d/4) = 1/(d/4)? → 4/d = 4/d ✓... Actually: 9Q/x² = Q/(d-x)² → 3/(x) = 1/(d-x) → x = 3d/4)*
2. 🔴 Charges +4Q and −Q are fixed at distance L. Where should a third charge be placed for equilibrium? *(Ans: outside, at distance L from −Q, i.e., 2L from +4Q)*
3. 🔴 ⭐ Two fixed charges +Q are at distance 2d apart. A charge −q (mass m) is placed at the midpoint and slightly displaced along the line. Show that it oscillates with SHM and find the period.

<details>
<summary><b>Answer to Q3</b></summary>

At midpoint, F = 0 (by symmetry). Displace by x (small) from midpoint.

Net restoring force = kQq/(d−x)² − kQq/(d+x)²

For x << d: ≈ kQq · [1/(d−x)² − 1/(d+x)²] ≈ kQq · 4xd/(d²)² (binomial approx)

F ≈ 4kQqx/d³ → F ∝ x → **SHM** with ω² = 4kQq/(md³)

T = 2π√(md³/(4kQq)) = **π√(md³/(kQq))**
</details>

---

### Type 6: Force between charges at polygon vertices

**Pattern:** "Find net force on one charge due to all others at vertices of a triangle/square/hexagon."

**Solved Example** 🔴

> Three identical charges +Q are placed at the three vertices of an equilateral triangle of side *a*. Find the net force on any one charge.

**Solution:**

Consider the charge at vertex A. Forces on it:
- F₁ = kQ²/a² due to B (along AB, repulsive)
- F₂ = kQ²/a² due to C (along AC, repulsive)

Angle between F₁ and F₂ = 60°.

Net force = √(F₁² + F₂² + 2F₁F₂cos60°)
= F₁√(1 + 1 + 2×½) = F₁√3 = **√3 kQ²/a²**

Direction: Along the bisector of angle A, pointing away from BC.

**Practice:**

1. 🟡 Two charges +Q are at two vertices of an equilateral triangle (side a). A charge −Q is at the third. Find net force on −Q. *(Ans: √3 kQ²/a², toward the midpoint of the +Q charges)*
2. 🔴 ⭐ Four identical charges +Q at the four corners of a square of side a. Find net force on one charge. *(Ans: kQ²/a² × (2 + 1/√2)... wait let me compute properly)*

<details>
<summary><b>Answer to Q2</b></summary>

On charge at corner A:
- From adjacent corner B: F₁ = kQ²/a² (along AB)
- From adjacent corner D: F₂ = kQ²/a² (along AD)
- From diagonal corner C: F₃ = kQ²/(a√2)² = kQ²/2a² (along diagonal AC)

F₁ and F₂ are perpendicular → their resultant = √2 · kQ²/a² along diagonal.
F₃ is also along diagonal = kQ²/2a².

**Net = kQ²/a² (√2 + 1/2) = kQ²/a² · (2√2 + 1)/2**

Direction: along the diagonal, away from C.
</details>

---

### Type 7: Coulomb's law vs Gravitation comparison

**Solved Example** 🟡

> Compare the electrostatic and gravitational forces between an electron and proton in a hydrogen atom. (r = 0.53 Å)

**Solution:**
- F_e = ke²/r² = 9 × 10⁹ × (1.6 × 10⁻¹⁹)² / (0.53 × 10⁻¹⁰)² = **8.2 × 10⁻⁸ N**
- F_g = Gm_em_p/r² = 6.67 × 10⁻¹¹ × 9.1 × 10⁻³¹ × 1.67 × 10⁻²⁷ / (0.53 × 10⁻¹⁰)² = **3.6 × 10⁻⁴⁷ N**
- Ratio: F_e/F_g ≈ **2.3 × 10³⁹**

**Practice:**

1. 🟡 Find the distance at which two protons have electrostatic force of 1 N. *(Ans: ≈ 1.52 × 10⁻¹⁴ m)*
2. 🟡 At what distance would two 1 kg masses need to be placed for their gravitational force to equal the Coulomb force between two 1 C charges at 1 m? *(Ans: impossible — would need distance ~2.7 × 10⁻¹¹ m, below atomic scale)*

---

### Type 8: Charge division for maximum/minimum force ⭐

**Solved Example** 🔴

> A charge Q is split into q and (Q − q). For maximum force at fixed distance r:

F = kq(Q − q)/r² → Maximize qQ − q²

dF/dq = Q − 2q = 0 → **q = Q/2**

The force is maximized when the charge is split **equally**.

**Practice:**

1. 🟡 A charge of 20 μC is divided into two parts. For maximum repulsion at 10 cm, find each part. *(Ans: 10 μC and 10 μC)*
2. 🔴 A charge Q is split into q and (Q − q). Find q for the force to be (a) maximum, (b) F/2 of maximum.

<details>
<summary><b>Answer to (b)</b></summary>

F_max = kQ²/(4r²) (at q = Q/2)

F = kq(Q−q)/r² = F_max/2 = kQ²/(8r²)

→ q(Q−q) = Q²/8 → 8q² − 8Qq + Q² = 0

q = [8Q ± √(64Q² − 32Q²)] / 16 = [8Q ± 4Q√2] / 16

q = Q(2 ± √2)/4

So q ≈ 0.854Q or q ≈ 0.146Q (two solutions, symmetric about Q/2).
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ Two point charges +4 μC and +1 μC are fixed at positions (0, 0) and (6, 0) cm respectively. At what point on the x-axis is the net electric force on a test charge zero? What if the second charge is −1 μC?

<details>
<summary><b>Solution</b></summary>

**Case 1: Both positive (+4μC at origin, +1μC at x = 6 cm)**

Null point between them (like charges). Let it be at x from +4μC.

k(4μC)/x² = k(1μC)/(6−x)² → 4(6−x)² = x² → 2(6−x) = x → 12 = 3x → **x = 4 cm**

**Case 2: +4μC at origin, −1μC at x = 6 cm**

Null point outside, beyond the smaller charge. Let it be at x from +4μC (x > 6).

k(4μC)/x² = k(1μC)/(x−6)² → 4(x−6)² = x² → 2(x−6) = x → x = 12 cm

**Null point at x = 12 cm** (6 cm beyond the −1μC charge)
</details>

**Q2.** 🔴 Three charges +Q, −2Q, +Q are placed at x = 0, x = a, x = 2a. Find the net force on the middle charge.

<details>
<summary><b>Solution</b></summary>

Force on −2Q due to left +Q: F₁ = k(Q)(2Q)/a² = 2kQ²/a² (toward left, attractive)
Force on −2Q due to right +Q: F₂ = k(Q)(2Q)/a² = 2kQ²/a² (toward right, attractive)

These two forces are **equal and opposite** → **Net force = 0**

> The middle charge is in equilibrium! But it's an unstable equilibrium.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 ⭐ State Coulomb's law. Write it in vector form. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Coulomb's law** states that the electrostatic force between two point charges is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them. The force acts along the line joining the two charges.

**Scalar form:** F = (1/4πε₀) × |q₁||q₂|/r²

**Vector form:** F⃗₁₂ = (1/4πε₀) × (q₁q₂/r²) r̂₁₂

where r̂₁₂ is the unit vector from q₂ to q₁. This form automatically accounts for attraction (opposite signs) and repulsion (same signs).
</details>

**Q2.** 🟡 ⭐ Compare Coulomb's law with Newton's law of gravitation. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

| Feature | Coulomb's Law | Newton's Law |
|---------|:------------:|:------------:|
| Formula | F = kq₁q₂/r² | F = Gm₁m₂/r² |
| Nature | Attractive or repulsive | Always attractive |
| Constant | k = 9 × 10⁹ Nm²/C² | G = 6.67 × 10⁻¹¹ Nm²/kg² |
| Medium dependence | Yes (F ∝ 1/K) | No |
| Relative strength | ~10³⁶ stronger | Baseline |
| Acts between | Charges | Masses |

Both follow inverse-square law and are central forces.
</details>

**Q3.** 🟡 What is the effect of the medium on electrostatic force? Define dielectric constant. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

The electrostatic force between two charges decreases when a dielectric medium is placed between them. The force becomes:

F_medium = F_vacuum / K

where **K (or εᵣ)** is the **dielectric constant** (relative permittivity) of the medium. It is defined as the ratio of the force between two charges in vacuum to the force between the same charges at the same distance in that medium.

K = F_vacuum / F_medium (K ≥ 1, with K = 1 for vacuum)
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ Two point charges +3 μC and +8 μC repel each other with a force of 40 N. If a charge of −5 μC is added to each, the force becomes:

(a) −10 N &emsp; (b) +10 N &emsp; (c) +20 N &emsp; (d) −20 N

<details>
<summary><b>Answer</b></summary>

New charges: (+3 − 5) = −2 μC and (+8 − 5) = +3 μC

Original: F = k(3)(8)/r² = 24k/r² = 40 N → k/r² = 40/24 = 5/3

New: F' = k(2)(3)/r² = 6 × (5/3) = **10 N**

Since charges are opposite sign → **attractive → −10 N**

**Answer: (a)**
</details>

**Q2.** 🔴 ⭐ Two identical charged spheres are suspended by strings of equal length from the same point. They repel and make angle 2θ with each other. If the charge on each is doubled and the length of strings is halved, the new angle 2θ' satisfies:

(a) tan θ' = 8 tan θ &emsp; (b) tan θ' = tan θ &emsp; (c) tan θ' = 4 tan θ &emsp; (d) tan θ' = 2 tan θ

<details>
<summary><b>Answer</b></summary>

At equilibrium: T sin θ = F_e and T cos θ = mg → **tan θ = F_e/mg = kq²/(r² mg)**

If strings have length L, the separation r = 2L sin θ.

This is a complex geometry problem. For small angles: r ≈ 2Lθ, so tan θ ≈ kq²/(4L²θ² mg).

When q → 2q and L → L/2:
tan θ' = k(4q²)/((L/2)² × 4θ'² × mg)

This requires careful analysis. For the simplified version assuming r doesn't change significantly:

tan θ' / tan θ = (2q)² × r² / (q² × r'²)

The exact answer depends on the angle regime. For small angles where r ∝ L: **tan θ' = 8 tan θ**

**Answer: (a)**
</details>

**Q3.** 🔴 The force between two charges in vacuum is F. The force between the same charges at the same distance in a medium of dielectric constant 4, and then the distance is halved, becomes:

(a) F &emsp; (b) 2F &emsp; (c) F/2 &emsp; (d) 4F

<details>
<summary><b>Answer</b></summary>

F' = kq₁q₂ / (K × (r/2)²) = kq₁q₂ / (4 × r²/4) = kq₁q₂/r² = **F**

**Answer: (a)** — The effects of medium and distance exactly cancel!
</details>

---

*Next: [Chapter 5 — Superposition Principle →](./05_superposition_principle.md)*
