# Chapter 5: Superposition Principle — Forces Between Multiple Charges

> *NCERT Section 1.7*

---

## 🎯 Stage 1: The Core Idea

### When There Are More Than Two Charges

Coulomb's law tells you the force between **two** charges. But what if you have 3, 4, or 100 charges? Do they all interfere with each other in some complicated way?

The answer is beautifully simple:

> **The Principle of Superposition:** The force on any one charge due to a group of other charges is the **vector sum** of the individual Coulomb forces from each of the other charges, calculated independently.

### The Analogy

You're standing in a room with three fans blowing at you from different directions. Each fan creates its own breeze independently. The wind you feel is simply the **sum of all three breezes** (as vectors). Fan A doesn't change its breeze because Fan B exists.

Charges behave the same way. The force between q₁ and q₂ doesn't change just because q₃ is nearby.

### Why This Is Powerful

It means you never have to solve a "many-body problem" in electrostatics. You just:
1. Compute the force from **each** other charge separately (using Coulomb's law).
2. Add all forces as **vectors**.
3. Done.

---

## 🔬 Stage 2: The Formula Lab

### The Superposition Formula

For N charges q₁, q₂, ..., qₙ, the net force on charge q₁ is:

$$\vec{F}_1 = \vec{F}_{12} + \vec{F}_{13} + \vec{F}_{14} + \cdots + \vec{F}_{1N}$$

Where each term is:

$$\vec{F}_{1i} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q_1 q_i}{r_{1i}^2} \hat{r}_{1i}$$

### The Systematic Approach (Follow This Every Time)

| Step | Action |
|------|--------|
| 1 | **Draw** the charge configuration with coordinates |
| 2 | **Identify** all forces on the target charge |
| 3 | **Calculate** magnitude of each force using Coulomb's law |
| 4 | **Resolve** each force into x and y components |
| 5 | **Sum** all x-components → F_x; Sum all y-components → F_y |
| 6 | **Result:** F_net = √(Fx² + Fy²), direction = tan⁻¹(Fy/Fx) |

> ⚠️ **Common mistake:** Adding magnitudes directly instead of doing vector addition. Force is a VECTOR. You MUST resolve into components.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Three charges in a line ⭐

**Solved Example** 🟡

> Three charges q₁ = +2 μC, q₂ = −3 μC, and q₃ = +4 μC are placed along the x-axis at x = 0, x = 5 cm, and x = 10 cm. Find the net force on q₂.

**Solution:**

Force on q₂ (at x = 5 cm):

**F₂₁** (due to q₁): F = k × 2 × 10⁻⁶ × 3 × 10⁻⁶ / (0.05)²
= 9 × 10⁹ × 6 × 10⁻¹² / 2.5 × 10⁻³ = **21.6 N**
Direction: q₁ is positive, q₂ is negative → attractive → toward q₁ → **−x direction**

**F₂₃** (due to q₃): F = k × 3 × 10⁻⁶ × 4 × 10⁻⁶ / (0.05)²
= 9 × 10⁹ × 12 × 10⁻¹² / 2.5 × 10⁻³ = **43.2 N**
Direction: q₂ is negative, q₃ is positive → attractive → toward q₃ → **+x direction**

**Net force = 43.2 − 21.6 = 21.6 N in the +x direction**

**Practice:**

1. 🟡 Three charges +Q, +Q, +Q are at x = 0, a, 2a. Find net force on the middle charge. *(Ans: 0 — by symmetry!)*
2. 🟡 Charges +2Q, −Q, +2Q are at x = 0, a, 2a. Find force on −Q. *(Ans: 0 — by symmetry!)*
3. 🔴 Charges +Q, +4Q, +Q are at x = 0, a, 2a. Find force on +4Q. *(Ans: 0)*

---

### Type 2: Three charges at triangle vertices ⭐⭐

**Solved Example** 🔴

> Three charges q₁ = +1 μC, q₂ = +2 μC, q₃ = −3 μC are at the vertices of an equilateral triangle of side 10 cm. Find the net force on q₁.

**Solution:**

Place q₁ at origin, q₂ at (10, 0) cm, q₃ at (5, 5√3) cm.

**F₁₂** (due to q₂): F = 9 × 10⁹ × 1 × 10⁻⁶ × 2 × 10⁻⁶ / (0.1)²
= 1.8 N, **repulsive**, along −x direction (away from q₂)
F₁₂ = (−1.8, 0) N

**F₁₃** (due to q₃): F = 9 × 10⁹ × 1 × 10⁻⁶ × 3 × 10⁻⁶ / (0.1)²
= 2.7 N, **attractive**, toward q₃
Direction from q₁ to q₃: angle = 60° from x-axis
F₁₃ = (2.7 cos 60°, 2.7 sin 60°) = (1.35, 2.338) N

**Net force:**
Fx = −1.8 + 1.35 = −0.45 N
Fy = 0 + 2.338 = 2.338 N
F = √(0.45² + 2.338²) = √(0.2025 + 5.466) = √5.669 ≈ **2.38 N**

Direction: θ = tan⁻¹(2.338/0.45) ≈ 79° from −x axis (i.e., nearly pointing toward q₃).

**Practice:**

1. 🟡 ⭐ Three identical charges +Q at vertices of equilateral triangle side a. Force on each. *(Ans: √3 kQ²/a², directed away from opposite side)*
2. 🔴 Charges +Q, +Q, −Q at vertices of equilateral triangle side a. Force on −Q. *(Ans: √3 kQ²/a², directed toward midpoint of the two +Q charges)*
3. 🔴 Charges +Q at three vertices and −Q at the fourth vertex of a square of side a. Find net force on −Q.

---

### Type 3: Four charges at square vertices ⭐⭐

**Solved Example** 🔴

> Four charges +Q, +Q, +Q, +Q are placed at the corners of a square of side *a*. Find the net force on any one charge.

**Solution:**

Take the charge at corner A. Forces on it from the other three:

- **F_B** (adjacent): kQ²/a², along AB (away from B)
- **F_D** (adjacent): kQ²/a², along AD (away from D)  
- **F_C** (diagonal): kQ²/(a√2)² = kQ²/(2a²), along AC (away from C)

F_B and F_D are perpendicular → Resultant = √2 · kQ²/a², along diagonal AC.

F_C is also along diagonal AC = kQ²/(2a²).

**F_net = kQ²/a² (√2 + 1/2) = kQ²(2√2 + 1)/(2a²)**

Direction: along the diagonal away from the opposite corner.

**Practice:**

1. 🔴 Four charges: +Q, −Q, +Q, −Q at corners of a square (alternating). Find force on any +Q.
2. 🔴 ⭐ Four charges at square corners: +q, +2q, +3q, +4q (going around). Find force on the charge +q.

---

### Type 4: Null point for two fixed charges ⭐⭐

**Covered extensively in Chapter 4, Type 5.** Key results:

| Charges | Null point location |
|---------|-------------------|
| Both positive (+Q₁, +Q₂) | Between them, closer to the smaller charge |
| Both negative (−Q₁, −Q₂) | Between them, closer to the smaller charge |
| Opposite signs (+Q₁, −Q₂) | Outside, beyond the smaller charge |

**Practice:**

1. 🟡 ⭐ +16Q and +Q at distance d. Where is the null point? *(Ans: 4d/5 from +16Q)*
2. 🔴 +25 μC at origin, −4 μC at x = 9 cm. Find null point. *(Ans: x = 15 cm — beyond the −4 μC charge)*

---

### Type 5: Force on a charge due to a symmetric distribution

**Solved Example** 🟡

> Six identical charges +Q are placed at the vertices of a regular hexagon of side a. What is the net force on a charge +q placed at the center?

**Solution:**

By symmetry, for each charge, there is an **equal and opposite** charge on the other side of the center. All forces cancel in pairs.

**F_net = 0**

> 🔑 **Symmetry shortcut:** For any charge at the center of a regular polygon with identical charges at all vertices, the net force is **zero** (by symmetry).

**Practice:**

1. 🟢 Five identical charges at the vertices of a regular pentagon. Force at the center? *(Ans: 0)*
2. 🟡 ⭐ Six charges +Q at five vertices and −Q at one vertex of a regular hexagon. Force on charge at center?

<details>
<summary><b>Answer</b></summary>

The missing "+Q" at the sixth vertex would have contributed force kQq/a² directed away from that vertex (toward center from that vertex's perspective — actually toward center, no, away from vertex toward center... Let me think clearly).

If all six were +Q → net force = 0. Replacing one +Q with −Q means we subtract that +Q's contribution and add a −Q's contribution.

Effectively: F = force due to −Q − force due to +Q at that vertex = (−kQq/a² − kQq/a²) r̂ = −2kQq/a² along the line from center toward that vertex.

Wait, let me redo. Force at center due to all 6 (+Q) = 0. Now one is changed to −Q (a difference of −2Q at that vertex).

Extra force = k(q)(2Q)/a² directed toward that vertex (the −Q vertex attracts, and the missing +Q no longer repels).

**F = 2kQq/a²** directed toward the vertex with −Q.
</details>

3. 🔴 ⭐ Seven charges: +Q at all 6 vertices of a regular hexagon, and one +Q is removed. What is the force on a charge +q at the center? *(Ans: kQq/a² toward the vacant vertex — same logic: 5 charges = 6 charges minus 1, and the "missing" charge contributes the unbalanced force.)*

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ Two charges +Q are fixed at (0, +a) and (0, −a). A charge −q is placed at the origin. If it is slightly displaced along the x-axis, will it return to origin? What if displaced along y-axis?

<details>
<summary><b>Solution</b></summary>

**Along x-axis (displaced to point (x, 0), x << a):**
Both +Q charges attract −q. By symmetry, the y-components cancel. The x-components both point toward origin.
Net restoring force ∝ x (for small x) → **Stable equilibrium → SHM → returns to origin.** ✓

**Along y-axis (displaced to point (0, y), y small from origin toward one +Q):**
The closer +Q pulls harder than the farther +Q. Net force is **away** from origin (toward the closer charge).
→ **Unstable equilibrium → does NOT return.** ✗

> This is Earnshaw's theorem in action: a charge cannot be in stable equilibrium under electrostatic forces alone in all directions simultaneously.
</details>

**Q2.** 🔴 Three charges +Q, +Q, −2Q are at vertices of an equilateral triangle of side a. Find the net force on −2Q.

<details>
<summary><b>Solution</b></summary>

Force on −2Q due to each +Q: F = 2kQ²/a² (attractive, toward each +Q).

Both forces have magnitude F = 2kQ²/a². Angle between them = 60°.

F_net = √(F² + F² + 2F² cos 60°) = F√(2 + 1) = F√3 = **2√3 kQ²/a²**

Direction: toward the midpoint of the line joining the two +Q charges.
</details>

**Q3.** 🟡 Two charges +4Q and +Q are at distance d. A third charge q is placed at the null point. Is the equilibrium stable or unstable?

<details>
<summary><b>Solution</b></summary>

Null point is at 2d/3 from +4Q. For displacement along the line: one force increases and the other decreases → **unstable** along the line.

For displacement perpendicular to the line: both forces have components pushing further away → **unstable** perpendicular too.

**Equilibrium is unstable in all directions** (Earnshaw's theorem).
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟡 ⭐ State the principle of superposition. Use it to find the force on charge q₁ due to charges q₂ and q₃. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Principle of Superposition:** The net electrostatic force on a given charge due to a number of other charges is the vector sum of the individual forces exerted on it by each of the other charges. The individual forces are unaffected by the presence of other charges.

For charge q₁ in the presence of q₂ and q₃:

F⃗₁ = F⃗₁₂ + F⃗₁₃

where F⃗₁₂ = (1/4πε₀)(q₁q₂/r₁₂²)r̂₁₂ and F⃗₁₃ = (1/4πε₀)(q₁q₃/r₁₃²)r̂₁₃

The resultant is obtained by vector addition (parallelogram/component method).
</details>

**Q2.** 🔴 ⭐ Three equal charges Q are placed at the three corners of an equilateral triangle of side a. Find the magnitude and direction of the resultant force on any one charge. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

Consider charge at vertex A. Forces from B and C:
- F_B = kQ²/a² (repulsive, along BA)
- F_C = kQ²/a² (repulsive, along CA)
- Angle between F_B and F_C = 60°

By parallelogram law:
F = √(F_B² + F_C² + 2F_BF_C cos 60°)
= (kQ²/a²)√(1 + 1 + 1) = **(√3)kQ²/a²**

Direction: Along the angle bisector at A, directed away from side BC (i.e., along the perpendicular from A to BC, outward).
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🔴 ⭐ Equal charges Q are placed at the four vertices of a square of side a. The force on a charge q placed at the center is:

(a) Zero &emsp; (b) kQq/a² &emsp; (c) 4kQq/a² &emsp; (d) 2√2 kQq/a²

<details>
<summary><b>Answer</b></summary>

**(a) Zero** — by symmetry, forces from opposite corners cancel in pairs.
</details>

**Q2.** 🔴 ⭐ Five charges, each +q, are placed at the five vertices of a regular hexagon of side a. A charge −Q is placed at the center. The force on −Q due to all five charges is:

(a) Zero  
(b) kqQ/a² away from vacant vertex  
(c) kqQ/a² toward vacant vertex  
(d) 5kqQ/a²  

<details>
<summary><b>Answer</b></summary>

**(b)** — If all six vertices had +q, the net force at center = 0. Missing one +q means the force from the remaining 5 is equal and opposite to what the 6th would exert. Since +q at the 6th vertex would push −Q **toward** the 6th vertex (attraction), the missing charge means the net force is **away** from the vacant vertex. Wait — −Q at center and +q at vertex → force on −Q is toward the vertex (attraction).

The "missing" +q would have attracted −Q toward the vacant vertex with force kqQ/a². Without it, the net force is kqQ/a² **away from** the vacant vertex? No...

Let me reconsider. Six identical +q at vertices → net force on −Q at center = 0. Now remove one +q. The remaining 5 charges exert a force = −(force from the removed charge). The removed charge would have pulled −Q toward the vacant vertex. So the force from 5 charges = −(attraction toward vacant) = **away from vacant vertex**.

Wait, no. If all 6 create zero net force, then F₅ + F₆ = 0 → F₅ = −F₆. F₆ (from the charge at the 6th vertex on −Q) = attraction toward vertex 6. So F₅ = repulsion from vertex 6 = **away from vacant vertex**.

Hmm, but actually F₆ is toward vertex 6 (attraction). So F₅ = −F₆ = away from vertex 6? That would mean the 5 charges push −Q away from the vacant vertex. But physically, there's more attraction on the side with 5 charges, so −Q should be pulled toward the 5 charges (away from the vacant vertex). Yes, that's consistent.

**Answer: (b) kqQ/a² away from vacant vertex**

Actually wait. Let me re-examine. The direction "away from vacant vertex" means toward the opposite side where 5 charges are clustered, which makes physical sense — the center charge −Q is attracted more strongly toward the side with more positive charges.

**Answer: (b)** ✓
</details>

**Q3.** 🔴 Two equal positive charges +Q are separated by distance 2d. A third charge +q is placed at the midpoint. If +q is displaced slightly along the perpendicular bisector, the motion is:

(a) SHM &emsp; (b) Non-periodic &emsp; (c) Along the line of charges &emsp; (d) Remains at rest

<details>
<summary><b>Answer</b></summary>

At the midpoint, force on +q is zero (by symmetry). When displaced along the perpendicular bisector by small distance y:

Both +Q charges exert forces on +q. The components along the bisector (vertical) both point **away** from the line → net force pushes +q **further away** from the midpoint.

This is **unstable equilibrium** → non-periodic, accelerating motion.

**Answer: (b)**

> Note: If the displaced charge were −q (opposite sign), the force would be restoring → SHM. This is a common JEE trap.
</details>

---

*Next: [Chapter 6 — Electric Field →](./06_electric_field.md)*
