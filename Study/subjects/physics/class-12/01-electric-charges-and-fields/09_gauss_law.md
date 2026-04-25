# Chapter 9: Electric Flux & Gauss's Law

> *NCERT Sections 1.10, 1.12–1.13*

---

## 🎯 Stage 1: The Core Idea

### Electric Flux — Counting Field Lines Through a Surface

Imagine holding a fishing net in a river. The amount of water flowing through the net depends on:
1. **How fast** the water flows (field strength E)
2. **How big** the net is (area A)
3. **What angle** the net makes with the current (angle θ)

If you hold the net perpendicular to the flow → maximum water passes through.
If you hold it parallel → zero water passes through.

**Electric flux** (Φ) is exactly this — it measures "how much electric field passes through a surface."

$$\Phi = \vec{E} \cdot \vec{A} = EA\cos\theta$$

Where θ is the angle between E⃗ and the **area vector** (outward normal to the surface).

| θ | cos θ | Flux | Interpretation |
|:-:|:-----:|:----:|:------------|
| 0° | 1 | EA (max) | Field ⊥ to surface (passes straight through) |
| 90° | 0 | 0 | Field ∥ to surface (no field lines pierce it) |
| 180° | −1 | −EA | Field enters the surface (inward) |

**SI unit of flux:** N·m²/C or V·m

### Continuous Charge Distribution

So far, we've dealt with **point charges**. But real objects have charge spread over them continuously. Three types:

| Distribution | Symbol | Charge element | Unit | Formula |
|-------------|:------:|:--------------:|:----:|:-------:|
| **Linear** (wire) | λ (lambda) | dq = λ dl | C/m | λ = Q/L |
| **Surface** (sheet) | σ (sigma) | dq = σ dA | C/m² | σ = Q/A |
| **Volume** (sphere) | ρ (rho) | dq = ρ dV | C/m³ | ρ = Q/V |

### Gauss's Law — The Most Powerful Tool in Electrostatics ⭐⭐⭐

> **Gauss's Law:** The total electric flux through any closed surface equals 1/ε₀ times the total charge enclosed by that surface.

$$\boxed{\oint \vec{E} \cdot d\vec{A} = \frac{q_{enclosed}}{\varepsilon_0}}$$

### Why Gauss's Law Is Revolutionary

- Coulomb's law requires you to calculate E by summing contributions from every tiny charge element → messy integrals.
- Gauss's law lets you find E in **one line** if the problem has symmetry (spherical, cylindrical, or planar).
- It works for ANY closed surface — but clever choice of surface (called **Gaussian surface**) makes the math trivial.

### The Three Sacred Symmetries

| Symmetry | Gaussian Surface | Examples |
|----------|:----------------:|---------|
| **Spherical** | Concentric sphere | Point charge, charged sphere/shell |
| **Cylindrical** | Coaxial cylinder | Infinite line charge, charged wire |
| **Planar** | Pill-box (flat cylinder) | Infinite plane sheet |

### What Gauss's Law Does NOT Tell You

- It doesn't tell you E at every point — only the flux through the whole surface.
- It's only useful when symmetry allows you to pull E out of the integral.
- It doesn't tell you the direction of E — you need to infer that from symmetry.

---

## 🔬 Stage 2: The Formula Lab

### Flux Through a Flat Surface

$$\Phi = EA\cos\theta$$

### Flux Through a Closed Surface (Gauss's Law)

$$\Phi = \oint \vec{E} \cdot d\vec{A} = \frac{q_{enc}}{\varepsilon_0}$$

### Key Results from Gauss's Law (Derived in Chapter 10)

| Configuration | Electric Field |
|---------------|:-------------:|
| Point charge Q at distance r | E = kQ/r² |
| Infinite line charge (λ) | E = λ/(2πε₀r) |
| Infinite plane sheet (σ) | E = σ/(2ε₀) |
| Spherical shell (outside) | E = kQ/r² |
| Spherical shell (inside) | E = 0 |

### Charge Density Conversions

| Type | Formula | Example |
|------|---------|---------|
| Linear: λ | Q/L or dq/dl | Wire of length L, total charge Q |
| Surface: σ | Q/A or dq/dA | Disc of area A, total charge Q |
| Volume: ρ | Q/V or dq/dV | Solid sphere of volume V, total charge Q |

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Flux through a flat surface ⭐

**Solved Example** 🟢

> A uniform electric field E = 500 N/C is directed along the x-axis. A square surface of side 10 cm lies in the y-z plane. Find the flux through the surface.

**Solution:**
- Area A = 0.1 × 0.1 = 0.01 m²
- Area vector is along x-axis (normal to y-z plane)
- θ = 0° (E ∥ A⃗)
- Φ = EA cos 0° = 500 × 0.01 × 1 = **5 N·m²/C**

**Practice:**

1. 🟢 E = 200 N/C along x-axis. A circle of radius 5 cm in the x-y plane. Find flux. *(Ans: 0 — E is parallel to the surface)*
2. 🟡 E = 1000 N/C at 60° to a square of side 20 cm. Find flux. *(Ans: 1000 × 0.04 × cos 60° = 20 N·m²/C)*
3. 🟡 ⭐ A hemisphere of radius R is placed in a uniform field E with its flat face perpendicular to E. Find the flux through the curved surface.

<details>
<summary><b>Answer</b></summary>

Flux through the entire closed surface (hemisphere + flat disc) = 0 (no charge enclosed, assuming E is uniform and external).

Flux through flat disc = E × πR² (into the hemisphere → negative if outward normal is used)

So flux through curved surface = −(flux through flat) = **EπR²** (outward).
</details>

---

### Type 2: Flux using Gauss's Law (charge enclosed) ⭐⭐

**Solved Example** 🟡

> A charge of +5 μC is placed inside a closed surface. Find the total flux through the surface.

**Solution:**
Φ = q/ε₀ = 5 × 10⁻⁶ / 8.854 × 10⁻¹² = **5.65 × 10⁵ N·m²/C**

> **The shape of the surface doesn't matter!** Whether it's a sphere, cube, or potato-shaped blob, the flux depends only on the enclosed charge.

**Practice:**

1. 🟢 Charge −3 μC inside a closed surface. Flux = ? *(Ans: −3.39 × 10⁵ N·m²/C)*
2. 🟢 ⭐ A cube contains charges +2 μC and −2 μC. Total flux through the cube? *(Ans: 0 — net enclosed charge = 0)*
3. 🟡 Charges +4 μC, −1 μC, +3 μC are inside a surface. A charge +5 μC is outside. Find the flux. *(Ans: (4 − 1 + 3) × 10⁻⁶ / ε₀ = 6 × 10⁻⁶ / ε₀ ≈ 6.78 × 10⁵ N·m²/C. Outside charge doesn't matter!)*

---

### Type 3: Flux through one face of a cube ⭐⭐

**Solved Example** 🟡

> A charge Q is placed at the centre of a cube. Find the flux through one face.

**Solution:**
- Total flux through the cube = Q/ε₀
- By symmetry, flux is equally distributed through all 6 faces.
- Flux through one face = **Q/(6ε₀)**

**Practice:**

1. 🟡 Q = 12 μC at the centre of a cube. Flux through one face? *(Ans: 2 × 10⁻⁶ / ε₀ = 2.26 × 10⁵ N·m²/C)*
2. 🔴 ⭐ A charge Q is at one corner of a cube. What is the flux through the cube?

<details>
<summary><b>Answer</b></summary>

A corner is shared by **8 cubes** (imagine 8 cubes meeting at that corner). The total flux from Q passes equally through all 8 cubes.

Flux through one cube = **Q/(8ε₀)**
</details>

3. 🔴 ⭐ A charge Q is at one corner of a cube. Find the flux through each of the three faces adjacent to the charge, and each of the three faces opposite.

<details>
<summary><b>Answer</b></summary>

The three faces **adjacent** to the corner where Q sits: E is parallel to these faces (the charge is ON the surface) → **Φ = 0** through each adjacent face.

The three faces **opposite**: By symmetry, all three share the flux equally.
Total flux through cube = Q/(8ε₀). Flux through 3 opposite faces = Q/(8ε₀).
Each opposite face: **Q/(24ε₀)**
</details>

---

### Type 4: Charge enclosed from given flux

**Solved Example** 🟡

> The electric flux through a closed surface is 8.85 × 10³ N·m²/C. Find the enclosed charge.

**Solution:**
q = ε₀Φ = 8.854 × 10⁻¹² × 8.85 × 10³ = **7.84 × 10⁻⁸ C ≈ 78.4 nC**

**Practice:**

1. 🟢 Φ = 10⁶ N·m²/C through a closed surface. Find q_enc. *(Ans: 8.854 μC)*
2. 🟡 Flux entering a surface = 200 N·m²/C. Flux leaving = 500 N·m²/C. Charge inside? *(Ans: q = ε₀(500 − 200) = ε₀ × 300 ≈ 2.66 nC)*

---

### Type 5: Proving Coulomb's law from Gauss's law ⭐

**Solved Example** 🟡

> Use Gauss's law to derive Coulomb's law for a point charge.

**Solution:**

Consider a point charge Q. Draw a Gaussian sphere of radius r centered on Q.

By symmetry:
- E is radially outward and has the same magnitude everywhere on the sphere.
- dA⃗ is also radially outward on the sphere.
- E⃗ · dA⃗ = E dA (since E ∥ dA⃗)

Gauss's law: ∮ E dA = Q/ε₀
→ E × 4πr² = Q/ε₀
→ **E = Q/(4πε₀r²) = kQ/r²**

This IS Coulomb's law! Force on a test charge q₀: F = q₀E = kQq₀/r². ✓

---

### Type 6: Flux through a surface when charge is outside

**Key principle:** If no charge is enclosed, total flux through the closed surface = 0.

This doesn't mean E = 0 at every point! It means whatever flux enters the surface, an equal flux exits it.

**Solved Example** 🟡

> A charge Q is placed outside a closed surface S. What is the total flux through S?

**Solution:** Φ = q_enc/ε₀ = **0** (no charge inside)

**Practice:**

1. 🟢 A charge sits just outside a sphere. Flux through the sphere? *(Ans: 0)*
2. 🟡 An electric dipole is inside a closed surface. Flux through the surface? *(Ans: 0 — net charge of a dipole = +q + (−q) = 0)*

---

### Type 7: Linear, surface, and volume charge density calculations

**Solved Example** 🟡

> A wire of length 2 m has a total charge of 4 μC uniformly distributed. Find (a) linear charge density, (b) charge on a 10 cm segment.

**Solution:**
(a) λ = Q/L = 4 × 10⁻⁶ / 2 = **2 × 10⁻⁶ C/m = 2 μC/m**
(b) q = λ × l = 2 × 10⁻⁶ × 0.1 = **0.2 μC**

**Practice:**

1. 🟢 A sphere of radius 10 cm has surface charge 5 μC. Find σ. *(Ans: σ = Q/(4πR²) = 39.8 μC/m²)*
2. 🟡 A solid sphere of radius 5 cm has volume charge density ρ = 3 × 10⁻⁶ C/m³. Find total charge. *(Ans: Q = ρ × (4/3)πR³ = 1.57 nC)*

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 ⭐ A charge +Q is placed at the centre of a cube of side a. Find: (a) flux through the cube, (b) flux through one face, (c) if the charge is moved to one corner, flux through the cube.

<details>
<summary><b>Solution</b></summary>

(a) Φ = Q/ε₀
(b) By symmetry: Φ_face = Q/(6ε₀)
(c) Corner is shared by 8 cubes → Φ = **Q/(8ε₀)**
</details>

**Q2.** 🔴 A uniform electric field E passes through a closed cylindrical surface (axis parallel to E). Show that the net flux through the cylinder is zero.

<details>
<summary><b>Solution</b></summary>

- Flux through left flat face: −EA (field enters → negative)
- Flux through right flat face: +EA (field exits → positive)
- Flux through curved surface: 0 (E ⊥ to A⃗ of curved surface, since E is parallel to the axis)
- Total: −EA + EA + 0 = **0** ✓ (no charge enclosed)
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟡 ⭐ State Gauss's law. Write its mathematical expression. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Gauss's Law** states that the total electric flux through any closed surface is equal to 1/ε₀ times the total electric charge enclosed within that surface.

$$\oint \vec{E} \cdot d\vec{A} = \frac{q_{enclosed}}{\varepsilon_0}$$

Here, the integral is over the entire closed surface (Gaussian surface), and q_enclosed is the algebraic sum of all charges inside the surface.
</details>

**Q2.** 🟡 ⭐ Define electric flux. What is its SI unit? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Electric flux** through a surface is defined as the surface integral of the electric field over that surface. For a uniform field:

Φ = E⃗ · A⃗ = EA cos θ

where θ is the angle between the electric field and the outward normal to the surface.

**SI unit:** N·m²/C (newton-metre-squared per coulomb) or equivalently V·m (volt-metre).
</details>

**Q3.** 🟡 ⭐ Use Gauss's law to derive Coulomb's law. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(See Type 5 above for the complete derivation.)*
</details>

**Q4.** 🟡 What is a Gaussian surface? What properties should it have for Gauss's law to be useful? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

A **Gaussian surface** is any hypothetical closed surface used to apply Gauss's law. For Gauss's law to be computationally useful, the Gaussian surface should be chosen such that:

1. The electric field has constant magnitude over the surface (or parts of it).
2. The electric field is either parallel or perpendicular to the area vector at every point on the surface.

This is only possible when the charge distribution has spherical, cylindrical, or planar symmetry.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ A charge Q is placed at the centre of a cube. The flux through one face is:

(a) Q/ε₀ &emsp; (b) Q/(2ε₀) &emsp; (c) Q/(4ε₀) &emsp; (d) Q/(6ε₀)

<details>
<summary><b>Answer</b></summary>

**(d)** — Total flux = Q/ε₀, distributed equally through 6 faces.
</details>

**Q2.** 🟡 ⭐ A charge Q is at a corner of a cube. The electric flux through the cube is:

(a) Q/ε₀ &emsp; (b) Q/(2ε₀) &emsp; (c) Q/(4ε₀) &emsp; (d) Q/(8ε₀)

<details>
<summary><b>Answer</b></summary>

**(d)** — Corner is shared by 8 cubes. Flux through each = Q/(8ε₀).
</details>

**Q3.** 🔴 ⭐ A point charge +Q is at the centre of a spherical shell of inner radius R₁ and outer radius R₂. The electric flux through a Gaussian sphere of radius r (R₁ < r < R₂) is:

(a) Q/ε₀ &emsp; (b) 0 &emsp; (c) Q/(2ε₀) &emsp; (d) Depends on r

<details>
<summary><b>Answer</b></summary>

**(b) 0** — The metallic shell has induced charge −Q on its inner surface. For R₁ < r < R₂ (inside the metal), E = 0 everywhere → flux = 0.

Alternatively: charge enclosed by Gaussian surface at r = +Q (centre) + (−Q) (inner surface) = 0.
</details>

**Q4.** 🔴 An electric dipole is placed inside a spherical surface. The total flux through the sphere is:

(a) q/ε₀ &emsp; (b) 2q/ε₀ &emsp; (c) q/(2ε₀) &emsp; (d) 0

<details>
<summary><b>Answer</b></summary>

**(d) 0** — A dipole has charges +q and −q. Net charge enclosed = 0 → flux = 0.
</details>

---

*Next: [Chapter 10 — Applications of Gauss's Law →](./10_applications_of_gauss_law.md)*
