# Chapter 8: Electric Dipole

> *NCERT Sections 1.10–1.11 · **THE MOST IMPORTANT TOPIC FOR EXAMS***

---

## 🎯 Stage 1: The Core Idea

### What Is an Electric Dipole?<br>

An electric dipole is the **simplest arrangement of charges that has no net charge but still produces an electric field.** It consists of:

- Two equal and opposite charges: **+q** and **−q**
- Separated by a small distance **2a**

> **Analogy:** Think of a bar magnet — it has a North and South pole that are inseparable. Similarly, a dipole has a + and − end. You can't have one without the other. Many molecules (like water, HCl) are natural dipoles.

### Dipole Moment ⭐

The **electric dipole moment** p⃗ is:

$$\vec{p} = q \times 2a \times \hat{n}$$

Where n̂ is the unit vector from −q to +q.

**Direction:** Always from **negative to positive** charge.

| Property | Value |
|----------|-------|
| Magnitude | p = q × 2a |
| SI Unit | C·m (coulomb-metre) |
| Debye (non-SI) | 1 D = 3.33 × 10⁻³⁰ C·m |
| Direction | −q → +q |

> Dipole moment is a **vector**. Its direction matters enormously.

### Why Dipoles Matter

1. **Water molecule** is a dipole (p = 6.17 × 10⁻³⁰ C·m) — this is why water dissolves salts.
2. **Antennas** are oscillating dipoles.
3. Dipole fields fall as **1/r³** (faster than point charge fields at 1/r²) — they're short-range.
4. In board/JEE exams, dipole questions account for **~25% of all marks** from this chapter.

---

## 🔬 Stage 2: The Formula Lab

### Formula 1: Electric Field on the Axial Line (End-on) ⭐⭐

Point P is at distance r from the center of the dipole, along the dipole axis.

$$E_{axial} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{2pr}{(r^2 - a^2)^2}$$

**For r >> a (short dipole / far-field):**

$$\boxed{E_{axial} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{2p}{r^3}}$$

**Direction:** Along the dipole moment (from −q to +q) → **same direction as p⃗**

### Formula 2: Electric Field on the Equatorial Line (Broadside-on) ⭐⭐

Point P is at distance r from the center, perpendicular to the dipole axis.

$$E_{eq} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{p}{(r^2 + a^2)^{3/2}}$$

**For r >> a:**

$$\boxed{E_{eq} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{p}{r^3}}$$

**Direction:** Opposite to the dipole moment → **anti-parallel to p⃗**

### Critical Comparison ⭐

| Property | Axial | Equatorial |
|----------|:-----:|:----------:|
| Formula (r >> a) | 2kp/r³ | kp/r³ |
| Ratio | **E_axial = 2 × E_equatorial** | Baseline |
| Direction w.r.t. p⃗ | Same (parallel) | Opposite (anti-parallel) |
| Distance dependence | 1/r³ | 1/r³ |

### Formula 3: Torque on a Dipole in Uniform Field ⭐⭐

$$\boxed{\vec{\tau} = \vec{p} \times \vec{E}}$$
$$|\tau| = pE\sin\theta$$

Where θ = angle between p⃗ and E⃗.

| θ | τ | Condition |
|:-:|:-:|:----------|
| 0° | 0 | Stable equilibrium (p ∥ E) |
| 90° | pE (maximum) | Maximum torque |
| 180° | 0 | Unstable equilibrium (p anti-∥ E) |

### Formula 4: Potential Energy of Dipole ⭐

$$\boxed{U = -\vec{p} \cdot \vec{E} = -pE\cos\theta}$$

| θ | U | Stability |
|:-:|:-:|:----------|
| 0° | −pE | **Minimum energy → stable** |
| 90° | 0 | Reference |
| 180° | +pE | **Maximum energy → unstable** |

### Formula 5: Work done in rotating a dipole

$$W = U_f - U_i = pE(\cos\theta_1 - \cos\theta_2)$$

Where θ₁ is the initial angle and θ₂ is the final angle with E⃗.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Calculate dipole moment ⭐

**Solved Example** 🟢

> Two charges +5 nC and −5 nC are separated by 2 mm. Find the dipole moment.

**Solution:**
p = q × 2a = 5 × 10⁻⁹ × 2 × 10⁻³ = **10⁻¹¹ C·m = 10 pC·m**

Direction: from −5 nC to +5 nC.

**Practice:**

1. 🟢 Charges ±2 μC separated by 1 cm. Find p. *(Ans: 2 × 10⁻⁸ C·m)*
2. 🟡 The dipole moment of a water molecule is 6.17 × 10⁻³⁰ C·m. The separation between the charges is 0.96 Å. Find the charge. *(Ans: q = p/2a = 6.43 × 10⁻²⁰ C ≈ 0.4e — showing partial charge separation)*

---

### Type 2: Axial field of a dipole ⭐⭐

**Solved Example** 🟡

> A dipole with moment p = 4 × 10⁻⁹ C·m is placed along the x-axis. Find the electric field at a point 20 cm away on the axis.

**Solution:**
E = 2kp/r³ = 2 × 9 × 10⁹ × 4 × 10⁻⁹ / (0.2)³
= 72 / 0.008 = **9000 N/C = 9 kN/C**

Direction: along the dipole moment (from −q to +q).

**Practice:**

1. 🟢 Find E on the axis at 10 cm from a dipole of p = 10⁻¹¹ C·m. *(Ans: 0.18 N/C)*
2. 🟡 The axial field at distance r is 500 N/C. What is the field at 2r?<br> *(Ans: 500/8 = 62.5 N/C — since E ∝ 1/r³)*
3. 🟡 ⭐ At what distance on the axis is the field due to a dipole (p = 10⁻⁸ C·m) equal to 10⁵ N/C?<br> *(Ans: r³ = 2kp/E → r ≈ 0.012 m = 1.2 cm)*

---

### Type 3: Equatorial field of a dipole ⭐⭐

**Solved Example** 🟡

> Using the same dipole from Type 2 (p = 4 × 10⁻⁹ C·m), find E at 20 cm on the equatorial line.

**Solution:**
E = kp/r³ = 9 × 10⁹ × 4 × 10⁻⁹ / (0.2)³
= 36 / 0.008 = **4500 N/C**

This is exactly **half** the axial field. ✓

Direction: anti-parallel to p⃗.

**Practice:**

1. 🟡 At a point on the equatorial line, E = 200 N/C. What would E be at the same distance on the axial line?<br> *(Ans: 400 N/C)*
2. 🟡 ⭐ At distance r on the axis, E = E₀. At what distance on the equatorial line is E = E₀?<br> *(Ans: r/2^{1/3} = r × 0.794)*

---

### Type 4: Torque on a dipole ⭐⭐⭐

**Solved Example** 🟡

> A dipole (p = 3 × 10⁻⁸ C·m) is placed in a uniform electric field of 10⁵ N/C, making an angle of 30° with the field. Find the torque.

**Solution:**
τ = pE sin θ = 3 × 10⁻⁸ × 10⁵ × sin 30°
= 3 × 10⁻³ × 0.5 = **1.5 × 10⁻³ N·m**

**Practice:**

1. 🟢 p = 2 × 10⁻⁹ C·m, E = 10⁴ N/C, θ = 90°. Find τ. *(Ans: 2 × 10⁻⁵ N·m)*
2. 🟡 At what angle is the torque maximum?<br> *(Ans: 90°)*
3. 🟡 ⭐ At what angle is the torque half of the maximum?<br> *(Ans: sin θ = 0.5 → θ = 30° or 150°)*
4. 🔴 A dipole (±10 μC, separation 2 cm) is placed in E = 10⁵ N/C at 60°. Find (a) torque, (b) force on each charge, (c) net force.

<details>
<summary><b>Answer</b></summary>

p = 10 × 10⁻⁶ × 0.02 = 2 × 10⁻⁷ C·m

(a) τ = pE sin 60° = 2 × 10⁻⁷ × 10⁵ × (√3/2) = **√3 × 10⁻² N·m ≈ 0.0173 N·m**

(b) Force on each charge = qE = 10 × 10⁻⁶ × 10⁵ = **1 N**

(c) In a uniform field, the net force on a dipole = **0** (the forces on +q and −q are equal and opposite). Only torque exists.
</details>

---

### Type 5: Potential energy and work done ⭐⭐

**Solved Example** 🟡

> A dipole (p = 2 × 10⁻⁶ C·m) initially aligned with a field E = 10⁴ N/C is rotated to 90°. Find the work done.

**Solution:**
W = pE(cos θ₁ − cos θ₂) = 2 × 10⁻⁶ × 10⁴ × (cos 0° − cos 90°)
= 0.02 × (1 − 0) = **0.02 J**

**Practice:**

1. 🟢 Work to rotate from 0° to 180°. *(Ans: 2pE)*
2. 🟡 ⭐ Work to rotate from 60° to 90°. *(Ans: pE(cos 60° − cos 90°) = pE/2)*
3. 🟡 Work to rotate from 90° to 180°. *(Ans: pE(cos 90° − cos 180°) = pE)*
4. 🔴 ⭐ A dipole is released from θ = 60° in a uniform field. What is its angular speed when it passes through θ = 0°?<br> (Moment of inertia = I)

<details>
<summary><b>Answer</b></summary>

By conservation of energy: Loss in PE = Gain in KE

pE(cos 0° − cos 60°) = ½Iω²

pE(1 − 0.5) = ½Iω²

**ω = √(pE/I)**
</details>

---

### Type 6: Net force on a dipole in a non-uniform field

**Key insight:** In a **uniform** field, net force on a dipole = 0 (only torque). In a **non-uniform** field, there IS a net force.

**Solved Example** 🔴

> A dipole (p directed along +x) is placed in a non-uniform field E = E₀(x/a) x̂. The centre of the dipole is at x = x₀. Find the net force.

**Solution:**

Force on +q at x₀ + a: F₊ = q × E₀(x₀ + a)/a, in +x
Force on −q at x₀ − a: F₋ = −q × E₀(x₀ − a)/a, in +x

Net force = qE₀[(x₀ + a) − (x₀ − a)]/a = qE₀(2a)/a = **2qE₀ = pE₀/a**

More generally: **F = p(dE/dx)** for a dipole in a non-uniform field.

**Practice:**

1. 🔴 A dipole is near a positive point charge Q at distance r (r >> a). Is the dipole attracted or repelled?<br> *(Ans: attracted — because the nearer charge of the dipole is opposite to Q and experiences stronger force than the farther same-sign charge)*

---

### Type 7: Derivation — Field on the axial line ⭐⭐ (Board must-know)

**This derivation is asked almost every year. Memorize the logic.**

**Setup:** Dipole with −q at A and +q at B, separated by 2a. Point P is on the axis at distance r from center O.

**E at P due to +q:** E₊ = kq/(r − a)² (directed away from +q, i.e., +x)
**E at P due to −q:** E₋ = kq/(r + a)² (directed toward −q, i.e., −x)

**Net E = E₊ − E₋** (since E₊ > E₋, net is along +x = direction of p)

$$E = kq\left[\frac{1}{(r-a)^2} - \frac{1}{(r+a)^2}\right] = kq \cdot \frac{4ar}{(r^2-a^2)^2}$$

Since p = q(2a):

$$E_{axial} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{2pr}{(r^2-a^2)^2}$$

For r >> a: (r² − a²)² ≈ r⁴

$$\boxed{E_{axial} \approx \frac{2kp}{r^3}}$$

---

### Type 8: Derivation — Field on the equatorial line ⭐⭐ (Board must-know)

**Setup:** Point P is at distance r from center O, on the perpendicular bisector.

Distance from each charge to P: √(r² + a²)

E₊ and E₋ have equal magnitudes: E = kq/(r² + a²)

By symmetry, **vertical components cancel**. Only horizontal (−x direction) survives.

Each horizontal component: E cos θ = E × a/√(r² + a²)

$$E_{eq} = 2 \times \frac{kq}{r^2+a^2} \times \frac{a}{\sqrt{r^2+a^2}} = \frac{kq \times 2a}{(r^2+a^2)^{3/2}} = \frac{kp}{(r^2+a^2)^{3/2}}$$

For r >> a:

$$\boxed{E_{eq} \approx \frac{kp}{r^3}}$$

Direction: **opposite to p⃗** (−x direction = from +q to −q).

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ A dipole is placed in a uniform field E. The dipole is initially at θ = 90°. Find: (a) torque, (b) PE, (c) work to bring it to 0°, (d) work to bring it to 180°.

<details>
<summary><b>Solution</b></summary>

(a) τ = pE sin 90° = **pE**
(b) U = −pE cos 90° = **0**
(c) W(90° → 0°) = pE(cos 90° − cos 0°) = pE(0 − 1) = **−pE** (energy released)
(d) W(90° → 180°) = pE(cos 90° − cos 180°) = pE(0 − (−1)) = **+pE** (energy required)
</details>

**Q2.** 🔴 ⭐ At a point on the axial line of a short dipole, E = 800 N/C. At the same distance on the equatorial line, E = ?<br>

<details>
<summary><b>Solution</b></summary>

E_axial = 2kp/r³ = 800 N/C
E_equatorial = kp/r³ = 800/2 = **400 N/C**
</details>

**Q3.** 🔴 A dipole (p = 10⁻⁷ C·m) is placed in E = 3 × 10⁴ N/C at θ = 30°. Find (a) torque, (b) PE, (c) work to rotate to 60°.

<details>
<summary><b>Solution</b></summary>

(a) τ = pE sin 30° = 10⁻⁷ × 3 × 10⁴ × 0.5 = **1.5 × 10⁻³ N·m**

(b) U = −pE cos 30° = −10⁻⁷ × 3 × 10⁴ × (√3/2) = **−2.6 × 10⁻³ J**

(c) W = pE(cos 30° − cos 60°) = 3 × 10⁻³ (√3/2 − 1/2) = 3 × 10⁻³ × 0.366 = **1.1 × 10⁻³ J**
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟡 ⭐ Define electric dipole and electric dipole moment. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Electric dipole:** A system of two equal and opposite charges (+q and −q) separated by a small fixed distance (2a) is called an electric dipole.

**Electric dipole moment (p⃗):** It is defined as the product of the magnitude of either charge and the distance between the charges: p = q × 2a. It is a vector directed from the negative charge to the positive charge. SI unit: C·m.
</details>

**Q2.** 🔴 ⭐ Derive the expression for the electric field at a point on the axial line of an electric dipole. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(See Type 7 above for the complete derivation. Write it step-by-step with a diagram.)*

**Key result:** E_axial = (1/4πε₀) × 2pr/(r²−a²)² ≈ (1/4πε₀) × 2p/r³ for r >> a

Direction: along the dipole moment vector.
</details>

**Q3.** 🔴 ⭐ Derive the expression for torque on an electric dipole placed in a uniform electric field. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

Consider a dipole (charges +q and −q, separation 2a) making angle θ with uniform field E.

Force on +q: F₊ = qE (along E)
Force on −q: F₋ = qE (opposite to E)

Net force = 0 (uniform field).

These equal, opposite, non-collinear forces form a **couple**.

Torque = force × perpendicular distance between lines of action
= qE × 2a sin θ = pE sin θ

In vector form: **τ⃗ = p⃗ × E⃗**

The torque tends to align the dipole along the field (θ → 0).
</details>

**Q4.** 🟡 ⭐ An electric dipole is placed in a uniform electric field. When is (a) torque maximum, (b) torque minimum, (c) PE maximum, (d) PE minimum?<br> *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

(a) Torque maximum when θ = 90° (p ⊥ E): τ_max = pE
(b) Torque minimum (zero) when θ = 0° or 180° (p ∥ E or p anti-∥ E)
(c) PE maximum when θ = 180° (p anti-parallel to E): U = +pE (unstable equilibrium)
(d) PE minimum when θ = 0° (p parallel to E): U = −pE (stable equilibrium)
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The ratio of the electric field due to a short dipole on its axial line to that on its equatorial line at the same distance is:

(a) 1:1 &emsp; (b) 2:1 &emsp; (c) 1:2 &emsp; (d) 4:1

<details>
<summary><b>Answer</b></summary>

E_axial/E_eq = (2kp/r³)/(kp/r³) = **2:1**

**Answer: (b)**
</details>

**Q2.** 🔴 ⭐ An electric dipole is placed at an angle of 30° with a uniform electric field of 10⁴ N/C. It experiences a torque of 5 N·m. The charge on the dipole, if the dipole length is 2 cm, is:

(a) 5 mC &emsp; (b) 50 mC &emsp; (c) 500 mC &emsp; (d) 7 μC

<details>
<summary><b>Answer</b></summary>

τ = pE sin θ → p = τ/(E sin θ) = 5/(10⁴ × 0.5) = 10⁻³ C·m

p = q × 2a → q = p/(2a) = 10⁻³/0.02 = 0.05 C = **50 mC**

**Answer: (b)**
</details>

**Q3.** 🔴 ⭐ The work done in rotating a dipole from stable equilibrium (θ = 0°) to θ = 60° in a uniform field is W. The work to rotate from 60° to 90° is:

(a) W &emsp; (b) W/2 &emsp; (c) (√3 − 1)W &emsp; (d) W(2 − √3)/(2 − √3)

<details>
<summary><b>Answer</b></summary>

W₁ (0° → 60°) = pE(cos 0° − cos 60°) = pE(1 − 1/2) = pE/2 = W
→ pE = 2W

W₂ (60° → 90°) = pE(cos 60° − cos 90°) = 2W(1/2 − 0) = **W**

**Answer: (a)**

> 🔑 Trap alert: Many students think the second rotation requires more work because the angle is "bigger." But W depends on the change in cos θ, not the change in θ.
</details>

**Q4.** 🔴 A dipole of moment p is placed perpendicular to a uniform field E. The work done in rotating it to the direction of the field is:

(a) pE &emsp; (b) −pE &emsp; (c) 2pE &emsp; (d) −2pE

<details>
<summary><b>Answer</b></summary>

W = pE(cos 90° − cos 0°) = pE(0 − 1) = **−pE**

The negative sign means **energy is released** (the dipole naturally wants to align, so the field does positive work = pE, and work done against the field = −pE).

**Answer: (b)**
</details>

**Q5.** 🔴 An electric dipole is free to move in a non-uniform electric field. It will:

(a) Move toward stronger field  
(b) Move toward weaker field  
(c) Not move at all  
(d) Rotate only  

<details>
<summary><b>Answer</b></summary>

**(a)** — In a non-uniform field, the force on the closer charge is stronger. After the dipole aligns with the field, it moves toward the region of stronger field (the force on the nearer charge dominates).
</details>

---

*Next: [Chapter 9 — Electric Flux & Gauss's Law →](./09_gauss_law.md)*
