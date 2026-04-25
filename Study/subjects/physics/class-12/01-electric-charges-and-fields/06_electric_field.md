# Chapter 6: Electric Field

> *NCERT Section 1.8*

---

## 🎯 Stage 1: The Core Idea

### The Problem with "Action at a Distance"

Coulomb's law says two charges exert forces on each other across empty space. But *how*? Does charge q₁ somehow "know" that q₂ exists 10 cm away?

This bothered Michael Faraday. His answer changed physics forever:

> **A charge doesn't exert force directly on another charge. Instead, every charge creates an "electric field" in the space around it. Any other charge placed in this field *experiences* a force.**

### The Analogy

Think of a campfire. The fire doesn't reach out and burn you. Instead, it creates a **heat field** — a zone of warmth that exists in space whether or not you're standing in it. If you walk into the warm zone, *you* feel the heat. The field exists independently of your presence.

Similarly:
- Every charge creates an **electric field** in all of space around it.
- This field exists whether or not another charge is there to feel it.
- If a second charge is placed in this field, it experiences a force = qE.

### Formal Definition

The electric field **E⃗** at a point in space is defined as the force experienced by a small positive test charge q₀ placed at that point, divided by q₀:

$$\vec{E} = \frac{\vec{F}}{q_0}$$

> ⚠️ **Why "small" test charge?** If q₀ is too large, it would disturb the original charge distribution, changing the very field we're trying to measure. In the limit q₀ → 0, this disturbance vanishes.

### Physical Significance of Electric Field ⭐

Why introduce E instead of just using Coulomb's law?

1. **Time delay:** When a charge moves, the information doesn't reach another charge instantly — it travels at the speed of light. The electric field is the *mediator* that propagates this information.

2. **Accelerating charges produce electromagnetic waves** — this can only be understood through the field concept, not through direct action-at-a-distance.

3. Fields make superposition calculations **cleaner** — you compute E at a point once, then multiply by any charge placed there.

---

## 🔬 Stage 2: The Formula Lab

### Electric Field due to a Point Charge ⭐

$$\vec{E} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{Q}{r^2} \hat{r}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| E | Electric field intensity | N/C or V/m |
| Q | Source charge | C |
| r | Distance from source charge to the field point | m |
| r̂ | Unit vector from Q toward field point | — |

**Direction:**
- If Q > 0 → E points **away** from Q (outward)
- If Q < 0 → E points **toward** Q (inward)

**Magnitude:** E = kQ/r² = 9 × 10⁹ × Q/r²

### Key Relationships

| Relation | Formula |
|----------|---------|
| Force on charge q in field E | **F = qE** |
| Acceleration of charge (mass m) | **a = qE/m** |
| E due to multiple charges | **E⃗ = E⃗₁ + E⃗₂ + E⃗₃ + ...** (vector sum) |

### Units

- **E** is measured in N/C (newtons per coulomb) or equivalently V/m (volts per metre).
- 1 N/C = 1 V/m

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Find E due to a single point charge ⭐

**Solved Example** 🟢

> Find the electric field at a distance of 20 cm from a point charge of +5 μC.

**Solution:**
E = kQ/r² = 9 × 10⁹ × 5 × 10⁻⁶ / (0.2)²
= 45 × 10³ / 0.04 = **1.125 × 10⁶ N/C**

Direction: radially outward from the positive charge.

**Practice:**

1. 🟢 E at 10 cm from −3 μC. *(Ans: 2.7 × 10⁶ N/C, directed toward the charge)*
2. 🟢 At what distance from a +2 μC charge is E = 9 × 10⁴ N/C? *(Ans: ~0.447 m)*
3. 🟡 Two points A and B are at distances 10 cm and 20 cm from a point charge. Find E_A/E_B. *(Ans: 4 — inverse square law)*

---

### Type 2: Find force on a charge placed in a given field ⭐

**Solved Example** 🟢

> A charge of −2 μC is placed in a uniform electric field of 10⁴ N/C directed eastward. Find the force on the charge.

**Solution:**
F = qE = 2 × 10⁻⁶ × 10⁴ = **0.02 N = 20 mN**

Direction: The charge is negative, so force is **opposite** to E → **westward**.

**Practice:**

1. 🟢 Force on +5 nC in E = 2 × 10³ N/C. *(Ans: 10⁻⁵ N, along E)*
2. 🟡 An electron (mass 9.1 × 10⁻³¹ kg) is placed in E = 10⁵ N/C. Find its acceleration. *(Ans: a = eE/m = 1.76 × 10¹⁶ m/s², opposite to E)*
3. 🟡 A proton is released from rest in E = 500 N/C. Find its speed after 1 μs. *(Ans: v = at = eE/m × t = 4.8 × 10⁴ m/s)*

---

### Type 3: E due to a system of charges (superposition) ⭐⭐

**Solved Example** 🔴

> Two charges q₁ = +4 μC and q₂ = −4 μC are placed at (−3, 0) cm and (+3, 0) cm. Find E at the origin.

**Solution:**

At the origin:
- Distance to each charge = 3 cm = 0.03 m.

**E due to q₁ (+4 μC at −3 cm):**
E₁ = k × 4 × 10⁻⁶ / (0.03)² = 9 × 10⁹ × 4 × 10⁻⁶ / 9 × 10⁻⁴ = 4 × 10⁷ N/C
Direction: away from q₁ (positive charge) → toward +x.

**E due to q₂ (−4 μC at +3 cm):**
E₂ = k × 4 × 10⁻⁶ / (0.03)² = 4 × 10⁷ N/C
Direction: toward q₂ (negative charge) → toward +x.

**Both fields point in the +x direction!**

E_net = E₁ + E₂ = **8 × 10⁷ N/C in the +x direction**

> 💡 This is a dipole! At the center, both fields add up (they don't cancel) because E from +q points away from it and E from −q points toward it — both rightward.

**Practice:**

1. 🟡 Two charges +Q and +Q at (−a, 0) and (+a, 0). Find E at the origin. *(Ans: 0, by symmetry — fields cancel)*
2. 🟡 Two charges +Q and +Q at (−a, 0) and (+a, 0). Find E at (0, b). *(Ans: 2kQb/(a² + b²)^{3/2} in the +y direction)*
3. 🔴 Three charges +Q, −2Q, +Q at vertices of an equilateral triangle of side a. Find E at the centroid.

---

### Type 4: Null point in electric field ⭐⭐

**Pattern:** "Find where the net electric field is zero."

**Solved Example** 🟡

> Two charges +4Q and +Q are at distance d apart. Where is E = 0?

**Solution:**

Between the charges (since both positive), at distance x from +4Q:

k(4Q)/x² = k(Q)/(d−x)²
4(d−x)² = x²
2(d−x) = x → x = **2d/3**

E = 0 at **2d/3 from the larger charge**.

> ⚠️ Note: The null point for E is the same as for F on a test charge. This makes sense because F = qE, so F = 0 ⟺ E = 0.

**Practice:**

1. 🟡 +9Q and +Q at distance d. Find null point. *(Ans: 3d/4 from +9Q)*
2. 🔴 +4Q and −Q at distance d. Where is E = 0? *(Ans: outside, at distance d from −Q, i.e., 2d from +4Q)*

---

### Type 5: Motion of a charge in a uniform electric field ⭐⭐

**Pattern:** "A charged particle enters/is released in a uniform E field."

**Solved Example** 🔴

> An electron enters a uniform electric field E = 2 × 10⁴ N/C (directed downward) with horizontal velocity v₀ = 3 × 10⁷ m/s. Find the vertical deflection after traveling 5 cm horizontally.

**Solution:**

This is exactly like projectile motion, but with electric force instead of gravity.

- Horizontal: x = v₀t → t = 0.05 / (3 × 10⁷) = 1.67 × 10⁻⁹ s
- Vertical acceleration: a = eE/m = 1.6 × 10⁻¹⁹ × 2 × 10⁴ / (9.1 × 10⁻³¹) = 3.52 × 10¹⁵ m/s²
- Vertical deflection: y = ½at² = ½ × 3.52 × 10¹⁵ × (1.67 × 10⁻⁹)²
= 0.5 × 3.52 × 10¹⁵ × 2.79 × 10⁻¹⁸ = **4.9 × 10⁻³ m ≈ 4.9 mm**

Direction: **upward** (electron accelerates opposite to E, since it's negative).

**Practice:**

1. 🟡 A proton is released from rest in E = 1000 N/C. How far does it travel in 2 μs? *(Ans: ~0.192 m)*
2. 🔴 ⭐ An electron is projected horizontally at 2 × 10⁶ m/s into a vertical E field of 5000 N/C. Find (a) time to travel 10 cm horizontally, (b) vertical deflection, (c) velocity at that point.

---

### Type 6: E at a point on the axis/perpendicular bisector of two equal charges

**Solved Example** 🟡

> Two charges +Q are at (−a, 0) and (+a, 0). Find E at point P = (0, y) on the y-axis.

**Solution:**

Distance from each charge to P: r = √(a² + y²)

E from each charge: E₁ = E₂ = kQ/(a² + y²)

By symmetry, x-components cancel. Only y-components survive.

Each y-component: E_y = E₁ × cos θ where cos θ = y/√(a² + y²)

E_net = 2 × kQ/(a² + y²) × y/√(a² + y²) = **2kQy/(a² + y²)^{3/2}** (directed along +y)

**Special cases:**
- y >> a: E ≈ 2kQ/y² (two charges look like one charge 2Q from far away)
- y = 0: E = 0 (by symmetry)

**Practice:**

1. 🟡 Two charges −Q at (±a, 0). Find E at (0, y). *(Ans: 2kQy/(a² + y²)^{3/2} toward the origin, i.e., −y direction)*
2. 🔴 ⭐ Charges +Q and −Q at (−a, 0) and (+a, 0). Find E at (0, y). *(This is a dipole — equatorial field! E = kp/(a² + y²)^{3/2} along −x. Covered in Chapter 8.)*

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ A charge +Q is at the origin. Another charge −Q is at (d, 0). Find: (a) E at (d/2, 0) — the midpoint; (b) E at (2d, 0); (c) E at (0, d).

<details>
<summary><b>Solution</b></summary>

**(a) Midpoint (d/2, 0):**
E due to +Q: kQ/(d/2)² = 4kQ/d², directed +x
E due to −Q: kQ/(d/2)² = 4kQ/d², directed −x (toward −Q, which is at +x)... wait, toward −Q means +x.

Both fields point in the **+x direction** → E = 8kQ/d²

**(b) Point (2d, 0):**
E due to +Q: kQ/(2d)² = kQ/4d², directed +x
E due to −Q: kQ/d² = kQ/d², directed −x (toward −Q at x = d)
E_net = kQ/d² − kQ/4d² = 3kQ/4d², directed **−x** (toward −Q)

**(c) Point (0, d):**
E from +Q: kQ/d², directed +y (away from +Q at origin)
E from −Q: at distance √(d² + d²) = d√2, directed toward −Q
E₂ = kQ/2d²

Direction of E₂: toward (d, 0) from (0, d) → at 45° below horizontal → components (kQ/2d² × cos45°, −kQ/2d² × sin45°)

E_x = kQ/(2√2 d²), E_y = kQ/d² − kQ/(2√2 d²)

(Full vector computation needed for exact answer.)
</details>

**Q2.** 🟡 A uniform electric field E = 500 N/C exists in the +x direction. A charge of +2 μC (mass 10 g) is released from rest. Find (a) force, (b) acceleration, (c) speed after 3 s, (d) KE after 3 s.

<details>
<summary><b>Solution</b></summary>

(a) F = qE = 2 × 10⁻⁶ × 500 = **10⁻³ N = 1 mN**

(b) a = F/m = 10⁻³ / 10⁻² = **0.1 m/s²**

(c) v = at = 0.1 × 3 = **0.3 m/s**

(d) KE = ½mv² = ½ × 0.01 × 0.09 = **4.5 × 10⁻⁴ J**
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 ⭐ Define electric field. What is its SI unit? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

The **electric field** at a point is defined as the force experienced by a unit positive test charge placed at that point:

E⃗ = F⃗/q₀ (in the limit q₀ → 0)

**SI unit:** Newton per coulomb (N/C) or equivalently Volt per metre (V/m).
</details>

**Q2.** 🟡 ⭐ What is the physical significance of the electric field? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

The electric field has real physical significance beyond being a mathematical convenience:

1. It is the **mediator of electrostatic force** — charges interact through their fields, not directly across space.
2. The concept becomes essential for time-varying fields: when a charge accelerates, the effect is not felt instantaneously by distant charges. Instead, the change in electric field propagates at the speed of light. This time delay can only be described using the field concept, and not by Coulomb's law alone.
</details>

**Q3.** 🟡 Derive the expression for the electric field due to a point charge Q at distance r. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

Place a positive test charge q₀ at distance r from charge Q.

By Coulomb's law, the force on q₀ is:
F = (1/4πε₀) × Qq₀/r²

By definition, E = F/q₀:
**E = (1/4πε₀) × Q/r²**

In vector form: **E⃗ = (1/4πε₀) × (Q/r²) r̂**

where r̂ is the unit vector from Q to the field point.
- If Q > 0, E⃗ points radially outward.
- If Q < 0, E⃗ points radially inward.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The electric field at a distance r from a charge Q is E. At what distance from a charge 4Q will the field be E/2?

(a) 2r &emsp; (b) 2√2 r &emsp; (c) 4r &emsp; (d) r/2

<details>
<summary><b>Answer</b></summary>

E = kQ/r². We need kQ'/r'² = E/2 where Q' = 4Q.

k(4Q)/r'² = kQ/(2r²) → r'² = 8r² → r' = **2√2 r**

**Answer: (b)**
</details>

**Q2.** 🔴 ⭐ Two point charges +8q and −2q are placed at x = 0 and x = L. The point on the x-axis where the electric field is zero is:

(a) x = L/3 &emsp; (b) x = 2L &emsp; (c) x = −L &emsp; (d) x = 4L

<details>
<summary><b>Answer</b></summary>

Charges are unlike, so null point is **outside**, beyond the smaller charge (−2q at x = L).

Let the null point be at x = L + d.

k(8q)/(L + d)² = k(2q)/d²
4d² = (L + d)²
2d = L + d → d = L

Null point at x = L + L = **2L**

**Answer: (b)**
</details>

**Q3.** 🔴 An electron and a proton are released from rest in a uniform electric field. After 1 second, the ratio of their displacements (electron to proton) is approximately:

(a) 1:1 &emsp; (b) 1:1836 &emsp; (c) 1836:1 &emsp; (d) 42.8:1

<details>
<summary><b>Answer</b></summary>

Both experience the same force magnitude F = eE.

s = ½at² = ½(F/m)t² → s ∝ 1/m

s_e/s_p = m_p/m_e = **1836**

**Answer: (c)**
</details>

---

*Next: [Chapter 7 — Electric Field Lines →](./07_electric_field_lines.md)*
