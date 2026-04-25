# Chapter 10: Applications of Gauss's Law

> *NCERT Section 1.14 · **THE 3 DERIVATIONS THAT APPEAR EVERY YEAR***

---

## 🎯 Stage 1: The Core Idea

This chapter is where Gauss's Law earns its reputation. You'll derive the electric field for three classic charge distributions using cleverly chosen Gaussian surfaces. These three derivations are asked in **nearly every board exam and most JEE papers**.

| # | Configuration | Symmetry | Gaussian Surface |
|:-:|-------------|:--------:|:----------------:|
| 1 | Infinitely long straight charged wire | Cylindrical | Coaxial cylinder |
| 2 | Infinite uniformly charged plane sheet | Planar | Pill-box (thin cylinder) |
| 3 | Uniformly charged thin spherical shell | Spherical | Concentric sphere |

**The Strategy (Same Every Time):**
1. Identify the symmetry
2. Choose a Gaussian surface that exploits the symmetry
3. Argue why E is constant over the surface (or zero/perpendicular on parts)
4. Compute ∮ E⃗ · dA⃗ = E × (area of relevant part)
5. Set equal to q_enc/ε₀
6. Solve for E

---

## 🔬 Stage 2: The Formula Lab — All Three Derivations

### Derivation 1: Infinite Line Charge ⭐⭐⭐

**Setup:** An infinitely long straight wire with uniform linear charge density λ (C/m).

**Gaussian Surface:** A coaxial cylinder of radius r and length l, centered on the wire.

**Symmetry Arguments:**
- E is **radially outward** (by symmetry — no preferred direction along the wire or around it)
- E has the **same magnitude** at every point on the curved surface (same r)
- E is **perpendicular** to the flat end caps → E⃗ · dA⃗ = 0 on the caps

**Applying Gauss's Law:**

∮ E⃗ · dA⃗ = E × (2πrl) + 0 + 0 = q_enc/ε₀ = λl/ε₀

$$E \times 2\pi rl = \frac{\lambda l}{\varepsilon_0}$$

$$\boxed{E = \frac{\lambda}{2\pi\varepsilon_0 r} = \frac{2k\lambda}{r}}$$

| Key Features | |
|-------------|---|
| E ∝ 1/r | (NOT 1/r²!) |
| Direction | Radially outward (if λ > 0) |
| Independent of | Length of cylinder (l cancels) |

---

### Derivation 2: Infinite Plane Sheet of Charge ⭐⭐⭐

**Setup:** An infinite plane sheet with uniform surface charge density σ (C/m²).

**Gaussian Surface:** A pill-box (small cylinder) with its flat faces parallel to the sheet, one on each side, each at distance r from the sheet.

**Symmetry Arguments:**
- E is **perpendicular** to the sheet (by symmetry — no preferred direction along the sheet)
- E has the **same magnitude** on both sides at equal distance
- E is **parallel** to the curved surface of the pill-box → E⃗ · dA⃗ = 0 on the curved surface

**Applying Gauss's Law:**

∮ E⃗ · dA⃗ = EA + EA + 0 = q_enc/ε₀ = σA/ε₀

$$2EA = \frac{\sigma A}{\varepsilon_0}$$

$$\boxed{E = \frac{\sigma}{2\varepsilon_0}}$$

| Key Features | |
|-------------|---|
| E is **constant** | Does NOT depend on distance from the sheet! |
| Direction | Away from sheet (if σ > 0); toward sheet (if σ < 0) |
| This is a uniform field | Same E everywhere (one side) |

> ⚡ **For two parallel sheets** (+σ and −σ): Between the sheets, E = σ/ε₀ (fields add). Outside, E = 0 (fields cancel). This is how a parallel plate capacitor works!

---

### Derivation 3: Uniformly Charged Thin Spherical Shell ⭐⭐⭐

**Setup:** A thin spherical shell of radius R with total charge Q uniformly distributed.

**Gaussian Surface:** A concentric sphere of radius r.

#### Case 1: r > R (Point outside the shell)

**Symmetry:** E is radially outward and uniform over the Gaussian sphere.

∮ E⃗ · dA⃗ = E × 4πr² = Q/ε₀

$$\boxed{E_{outside} = \frac{1}{4\pi\varepsilon_0} \cdot \frac{Q}{r^2} = \frac{kQ}{r^2}}$$

> **The shell behaves as if all charge is concentrated at the centre!** This is the same as a point charge.

#### Case 2: r < R (Point inside the shell)

The Gaussian sphere (radius r < R) is **inside** the shell. No charge is enclosed!

q_enc = 0 → E × 4πr² = 0

$$\boxed{E_{inside} = 0}$$

> **There is NO electric field inside a uniformly charged spherical shell.** This is called **electrostatic shielding**.

#### Case 3: r = R (Point on the surface)

$$E_{surface} = \frac{kQ}{R^2} = \frac{\sigma}{ε_0}$$

(where σ = Q/4πR²)

### Summary Graph: E vs r for Spherical Shell

```
E ↑
   |     *
   |    *
   |   * (kQ/r² — like point charge)
   |  *
   | *
   |* ← E = kQ/R² at r = R
   |
   |______|_________________________→ r
   0      R
   E = 0    (E drops as 1/r² outside)
```

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: E due to infinite line charge ⭐

**Solved Example** 🟡

> A long wire has linear charge density λ = 5 × 10⁻⁶ C/m. Find E at 10 cm from the wire.

**Solution:**
E = λ/(2πε₀r) = 2kλ/r = 2 × 9 × 10⁹ × 5 × 10⁻⁶ / 0.1
= 90000 / 0.1 = **9 × 10⁵ N/C**

Direction: radially outward from the wire.

**Practice:**

1. 🟢 λ = 2 μC/m. Find E at 20 cm. *(Ans: 1.8 × 10⁵ N/C)*
2. 🟡 At what distance from a wire (λ = 3 × 10⁻⁸ C/m) is E = 27 N/C? *(Ans: 20 m)*
3. 🟡 ⭐ Two parallel infinite wires, separated by distance d, carry charges +λ and −λ per unit length. Find E at the midpoint. *(Ans: 2 × 2kλ/d = 4kλ/d = 2λ/(πε₀d), directed from +λ to −λ)*

---

### Type 2: E due to infinite plane sheet ⭐

**Solved Example** 🟢

> An infinite plane sheet has surface charge density σ = 2 × 10⁻⁶ C/m². Find E near the sheet.

**Solution:**
E = σ/(2ε₀) = 2 × 10⁻⁶ / (2 × 8.854 × 10⁻¹²)
= 2 × 10⁻⁶ / 1.77 × 10⁻¹¹ = **1.13 × 10⁵ N/C**

**Practice:**

1. 🟢 σ = 10 μC/m². Find E. *(Ans: 5.65 × 10⁵ N/C)*
2. 🟡 ⭐ Two parallel infinite sheets have charge densities +σ and −σ. Find E (a) between the sheets, (b) outside the sheets.

<details>
<summary><b>Answer</b></summary>

(a) Between: Fields from both sheets point in the same direction (from + to −).
E = σ/(2ε₀) + σ/(2ε₀) = **σ/ε₀**

(b) Outside: Fields from the two sheets point in opposite directions → cancel.
**E = 0**
</details>

3. 🔴 Two parallel sheets have charge densities +2σ and −σ. Find E in all three regions.

<details>
<summary><b>Answer</b></summary>

Let sheet 1 (+2σ) be on the left, sheet 2 (−σ) on the right.

Left of both: E₁ (leftward) + E₂ (rightward, toward −σ which is on the right)
Wait, let me be systematic.

E due to sheet 1 (+2σ): Magnitude σ/ε₀, directed **away** from sheet 1 (rightward on right side, leftward on left side)

E due to sheet 2 (−σ): Magnitude σ/(2ε₀), directed **toward** sheet 2 (rightward from left side, leftward from right side... no). For negative sheet, E points toward the sheet on both sides.

Let's use a coordinate: +x is rightward.

**Region I (left of both):**
E₁ = −2σ/(2ε₀) = −σ/ε₀ (leftward, away from positive sheet)
E₂ = +σ/(2ε₀) (rightward, toward negative sheet)
E_net = **−σ/(2ε₀)** (leftward) → magnitude **σ/(2ε₀)**

**Region II (between):**
E₁ = +σ/ε₀ (rightward)
E₂ = +σ/(2ε₀) (rightward, toward the −σ sheet on right)

Wait, I need to reconsider. For −σ on the right sheet, field points toward it from both sides. From the left side of −σ sheet → rightward. Actually no: field due to −σ points TOWARD the sheet, so from left of sheet → rightward, from right of sheet → leftward.

In region II (between): E₁ = +2σ/(2ε₀) = σ/ε₀ (rightward), E₂ = σ/(2ε₀) (rightward, toward −σ sheet)
E_net = **3σ/(2ε₀)** (rightward)

**Region III (right of both):**
E₁ = +σ/ε₀ (rightward), E₂ = −σ/(2ε₀) (leftward, toward −σ sheet)
E_net = **σ/(2ε₀)** (rightward)
</details>

---

### Type 3: E due to spherical shell ⭐⭐

**Solved Example** 🟡

> A thin spherical shell of radius 20 cm has charge 4 μC. Find E at (a) 30 cm from centre, (b) 10 cm from centre, (c) on the surface.

**Solution:**
(a) r = 30 cm > R: E = kQ/r² = 9 × 10⁹ × 4 × 10⁻⁶ / (0.3)² = **4 × 10⁵ N/C**
(b) r = 10 cm < R: **E = 0** (inside the shell)
(c) r = R = 20 cm: E = kQ/R² = 9 × 10⁹ × 4 × 10⁻⁶ / (0.2)² = **9 × 10⁵ N/C**

**Practice:**

1. 🟡 Shell of radius R, charge Q. At what distance outside is E = E_surface/4? *(Ans: 2R)*
2. 🟡 ⭐ A conducting sphere of radius 10 cm has charge 2 μC. Find E at r = 5 cm, 10 cm, 15 cm. *(Ans: 0, 1.8 × 10⁶ N/C, 8 × 10⁵ N/C)*
3. 🔴 Two concentric shells: inner (radius R₁, charge +Q) and outer (radius R₂, charge −Q). Find E for r < R₁, R₁ < r < R₂, and r > R₂.

<details>
<summary><b>Answer</b></summary>

- r < R₁: E = 0 (inside inner shell)
- R₁ < r < R₂: E = kQ/r² (only inner shell's charge is enclosed)
- r > R₂: q_enc = Q + (−Q) = 0 → **E = 0**
</details>

---

### Type 4: Force on a charge near these distributions

**Solved Example** 🟡

> A charge of +2 nC is placed 5 cm from an infinite line charge (λ = 4 × 10⁻⁶ C/m). Find the force on the charge.

**Solution:**
E = 2kλ/r = 2 × 9 × 10⁹ × 4 × 10⁻⁶ / 0.05 = 1.44 × 10⁶ N/C

F = qE = 2 × 10⁻⁹ × 1.44 × 10⁶ = **2.88 × 10⁻³ N ≈ 2.88 mN**

Direction: radially away from wire (both charge and wire are positive).

**Practice:**

1. 🟡 An electron is 1 mm from an infinite sheet (σ = 5 × 10⁻⁹ C/m²). Find its acceleration. *(Ans: E = σ/2ε₀ ≈ 282 N/C, a = eE/m ≈ 4.95 × 10¹³ m/s²)*
2. 🔴 A charge +q is at distance d from the centre of a spherical shell (radius R > d, charge +Q). What is the force on q? *(Ans: 0 — E inside shell = 0)*

---

### Type 5: Deriving results using Gauss's Law (Exam derivation practice)

**This is where board marks live.** Practice writing these derivations cleanly.

**Template for a perfect derivation answer:**

1. ✅ State the problem and draw a labeled diagram
2. ✅ Choose and label the Gaussian surface
3. ✅ State the symmetry arguments (why E is constant/zero on different parts)
4. ✅ Write Gauss's law: ∮ E⃗ · dA⃗ = q_enc/ε₀
5. ✅ Evaluate LHS and RHS separately
6. ✅ Solve for E
7. ✅ State the direction

**Practice:**

1. 🔴 ⭐ Derive E due to an infinitely long straight charged wire using Gauss's law. *(Full derivation — practice writing in under 10 minutes)*
2. 🔴 ⭐ Derive E due to an infinite uniformly charged plane sheet using Gauss's law.
3. 🔴 ⭐ Derive E due to a uniformly charged thin spherical shell at points (a) outside, (b) inside.

---

### Type 6: Graph-based questions ⭐

**Pattern:** "Plot E vs r for the given configuration."

| Configuration | Graph Shape |
|--------------|-------------|
| Point charge | E ∝ 1/r² — smooth decay from infinity |
| Infinite wire | E ∝ 1/r — slower decay |
| Infinite sheet | E = constant — flat horizontal line |
| Spherical shell | E = 0 (r < R), then kQ/r² (r > R) — discontinuity at r = R |
| Solid sphere (uniform ρ) | E ∝ r (r < R), then kQ/r² (r > R) — rises linearly then decays |

**Practice:**

1. 🟡 Sketch E vs r for a uniformly charged solid sphere.
2. 🟡 ⭐ Sketch E vs r for two concentric shells with charges +Q (inner) and +2Q (outer).
3. 🟡 At what point is E maximum for a solid uniformly charged sphere? *(Ans: at the surface, r = R)*

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ A spherical shell of radius R has charge Q. A point charge q is placed at the centre. Find E at (a) r < R, (b) r > R.

<details>
<summary><b>Solution</b></summary>

(a) r < R: Only q is enclosed → E = kq/r² (due to q alone; shell contributes nothing inside)

(b) r > R: Both q and Q are enclosed → E = k(Q + q)/r²
</details>

**Q2.** 🔴 Two infinite parallel sheets carry charge densities σ₁ = +6 μC/m² and σ₂ = −4 μC/m². Find E in the three regions.

<details>
<summary><b>Solution</b></summary>

E₁ = σ₁/(2ε₀) = 6/(2 × 8.854 × 10⁻⁶) = 3.39 × 10⁵ N/C
E₂ = σ₂/(2ε₀) = 4/(2 × 8.854 × 10⁻⁶) = 2.26 × 10⁵ N/C

**Left of both:** E₁ (leftward) + E₂ (rightward, toward −σ₂) = (3.39 − 2.26) × 10⁵ = **1.13 × 10⁵ N/C leftward**

**Between:** E₁ (rightward) + E₂ (rightward) = (3.39 + 2.26) × 10⁵ = **5.65 × 10⁵ N/C rightward**

**Right of both:** E₁ (rightward) + E₂ (leftward) = (3.39 − 2.26) × 10⁵ = **1.13 × 10⁵ N/C rightward**
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🔴 ⭐ Using Gauss's law, derive the expression for the electric field due to an infinitely long straight uniformly charged wire at a distance r from it. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(See Derivation 1 above. Write with diagram, label Gaussian cylinder, show all symmetry arguments, arrive at E = λ/2πε₀r.)*
</details>

**Q2.** 🔴 ⭐ Using Gauss's law, derive the expression for the electric field due to a uniformly charged infinite plane sheet. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(See Derivation 2 above. Draw pill-box, show E is perpendicular to sheet and same on both sides, arrive at E = σ/2ε₀.)*
</details>

**Q3.** 🔴 ⭐ Using Gauss's law, show that the electric field inside a uniformly charged thin spherical shell is zero, and outside it is the same as if all charge were concentrated at the centre. *(5 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(See Derivation 3 above. Two cases: r > R gives E = kQ/r², r < R gives E = 0.)*
</details>

**Q4.** 🟡 A large plane sheet has σ = 2.0 × 10⁻⁶ C/m². Find the flux through a rectangular surface of area 0.02 m² held parallel to the sheet and then perpendicular to the sheet. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

E = σ/(2ε₀) = 2 × 10⁻⁶ / (2 × 8.854 × 10⁻¹²) ≈ 1.13 × 10⁵ N/C

**Parallel to sheet:** Area vector ⊥ to sheet, same as E direction → Φ = EA = 1.13 × 10⁵ × 0.02 = **2260 N·m²/C**

**Perpendicular to sheet:** Area vector ∥ to sheet, ⊥ to E → Φ = EA cos 90° = **0**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The electric field due to an infinite plane sheet of charge is:

(a) Proportional to distance from the sheet  
(b) Inversely proportional to distance  
(c) Inversely proportional to square of distance  
(d) Independent of distance  

<details>
<summary><b>Answer</b></summary>

**(d)** — E = σ/(2ε₀) is **independent** of the distance from the sheet. This is a remarkably counter-intuitive result.
</details>

**Q2.** 🟡 ⭐ A thin spherical shell of radius R has charge Q. The electric field at distance r (r < R) from the centre is:

(a) kQ/R² &emsp; (b) kQ/r² &emsp; (c) Zero &emsp; (d) kQr/R³

<details>
<summary><b>Answer</b></summary>

**(c) Zero** — no charge is enclosed by a Gaussian sphere inside the shell.
</details>

**Q3.** 🔴 ⭐ Two infinite parallel plane sheets have equal and opposite charge densities +σ and −σ. The electric field between and outside the sheets are:

(a) σ/ε₀ and 0  
(b) σ/(2ε₀) and σ/(2ε₀)  
(c) 0 and σ/ε₀  
(d) σ/ε₀ and σ/(2ε₀)  

<details>
<summary><b>Answer</b></summary>

**(a)** — Between: fields from both sheets add → σ/ε₀. Outside: fields cancel → 0.
</details>

**Q4.** 🔴 ⭐ A charge Q is uniformly distributed over a long thin wire of length L. The electric field at a point at distance r from the wire (r << L) is:

(a) Q/(4πε₀r²) &emsp; (b) Q/(2πε₀rL) &emsp; (c) Q/(4πε₀rL) &emsp; (d) Qr/(4πε₀L²)

<details>
<summary><b>Answer</b></summary>

λ = Q/L. For r << L (wire appears infinite):

E = λ/(2πε₀r) = **Q/(2πε₀rL)**

**Answer: (b)**
</details>

**Q5.** 🔴 A uniformly charged solid sphere of radius R has total charge Q. The electric field at distance r (r < R) from the centre is:

(a) Zero &emsp; (b) kQ/r² &emsp; (c) kQr/R³ &emsp; (d) kQ/R²

<details>
<summary><b>Answer</b></summary>

For a solid sphere (NOT a shell!), charge enclosed inside radius r:
q_enc = Q × (r³/R³) (ratio of volumes)

E × 4πr² = q_enc/ε₀ = Qr³/(R³ε₀)

E = Qr/(4πε₀R³) = **kQr/R³**

**Answer: (c)**

> ⚠️ **JEE Trap:** Don't confuse shell (E = 0 inside) with solid sphere (E ∝ r inside). This distinction is tested constantly.
</details>

**Q6.** 🔴 The electric field at the surface of a charged conductor is 10⁴ N/C. The surface charge density is:

(a) ε₀ × 10⁴ &emsp; (b) 10⁴/ε₀ &emsp; (c) 2ε₀ × 10⁴ &emsp; (d) 10⁴/(2ε₀)

<details>
<summary><b>Answer</b></summary>

At the surface of a conductor: E = σ/ε₀

→ σ = ε₀E = **ε₀ × 10⁴**

**Answer: (a)**

> Note: For a conductor, it's σ/ε₀ (not σ/2ε₀) because the field only exists on ONE side (outside). This is different from an infinite sheet of charge (field on both sides → σ/2ε₀ each).
</details>

---

## 🏆 Congratulations — You've Finished the Book!

You've worked through **all 10 chapters** of Electric Charges and Fields. Here's your final checklist:

### Board Exam Readiness ✅

- [ ] Can I write the 3 Gauss's law derivations in under 10 minutes each?
- [ ] Can I derive E on axial and equatorial lines of a dipole?
- [ ] Can I derive the torque on a dipole in a uniform field?
- [ ] Do I know all properties of electric field lines?
- [ ] Can I solve charge quantization problems quickly?

### JEE Mains Readiness ✅

- [ ] Can I find null points for any two-charge system?
- [ ] Can I handle polygon geometry problems (triangle, square, hexagon)?
- [ ] Do I know the difference between shell and solid sphere?
- [ ] Can I compute flux through cubes (centre, corner, edge)?
- [ ] Can I analyze motion of charged particles in fields?

> **Go back to any chapter where you're not confident. The 6-stage method works only if you actually DO every problem, not just read the solutions.**

*Now go crush that exam.* ⚡

---

*← [Back to Table of Contents](./00_preface.md)*
