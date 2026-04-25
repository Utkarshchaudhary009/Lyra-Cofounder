# NCERT Exemplar — Short & Long Answer Questions (Q 1.14 to 1.25)

> *Electric Charges and Fields · Board + JEE Must-Do*

---

## Short Answer Questions

### Q 1.14 ⭐

An arbitrary surface encloses a dipole. What is the electric flux through this surface?

<details>
<summary><b>Solution</b></summary>

A dipole consists of charges +q and −q.

Total charge enclosed = +q + (−q) = **0**

By Gauss's law: Φ = q_enclosed/ε₀ = **0**

The net electric flux through any closed surface enclosing a complete dipole is **zero**, regardless of the shape of the surface.

> 🔑 This is because every field line that leaves +q and exits the surface must eventually enter the surface and terminate on −q (or vice versa). Lines in = Lines out.
</details>

---

### Q 1.15 ⭐⭐

A metallic spherical shell has an inner radius R₁ and outer radius R₂. A charge Q is placed at the centre of the spherical cavity. What will be the surface charge density on (i) the inner surface, and (ii) the outer surface?

<details>
<summary><b>Solution</b></summary>

**(i) Inner surface:**

Draw a Gaussian sphere of radius r (R₁ < r < R₂) — inside the metal of the shell.

Inside a conductor in electrostatic equilibrium, E = 0.

∮ E⃗ · dA⃗ = 0 = (Q + q_inner)/ε₀

Therefore: q_inner = −Q

Surface charge density on inner surface:

$$\boxed{\sigma_{inner} = \frac{-Q}{4\pi R_1^2}}$$

**(ii) Outer surface:**

The shell is electrically neutral (initially uncharged). If −Q appears on the inner surface, then +Q must appear on the outer surface (conservation of charge).

$$\boxed{\sigma_{outer} = \frac{+Q}{4\pi R_2^2}}$$

> 🔑 The charge Q at the centre induces −Q on the inner surface and +Q on the outer surface. From outside, the shell looks exactly like a point charge +Q at the centre.
</details>

---

### Q 1.16 ⭐

The dimensions of an atom are of the order of an Angstrom. Thus there must be large electric fields between the protons and electrons. Why, then, is the electrostatic field inside a conductor zero?

<details>
<summary><b>Solution</b></summary>

The statement "E = 0 inside a conductor" refers to the **macroscopic** electric field — the field averaged over a volume containing many atoms (thousands or millions).

At the **microscopic** (atomic) level, there are indeed enormous electric fields (~10¹¹ V/m) between individual protons and electrons within each atom.

However, these atomic fields:
1. **Fluctuate wildly** in direction over atomic distances (~10⁻¹⁰ m)
2. **Average to zero** when summed over any macroscopic volume

The macroscopic field E (the one relevant to electrostatics) is this spatial average. In a conductor in electrostatic equilibrium, the free electrons have rearranged themselves so that this macroscopic average field is exactly zero.

> 🔑 "E = 0 inside a conductor" is a macroscopic statement. Microscopically, fields are enormous but cancel on average.
</details>

---

### Q 1.17 ⭐

If the total charge enclosed by a surface is zero, does it imply that the electric field everywhere on the surface is zero? Conversely, if the electric field everywhere on a surface is zero, does it imply that net charge inside is zero?

<details>
<summary><b>Solution</b></summary>

**Part 1: q_enclosed = 0 → E = 0 everywhere on surface?**

**No.** The total flux ∮ E⃗ · dA⃗ = 0, but this does NOT mean E = 0 at every point. The field can be non-zero at individual points as long as the net flux (integral) is zero.

**Example:** Place a dipole inside a closed surface. Net charge = 0, flux = 0, but E ≠ 0 at most points on the surface.

**Part 2: E = 0 everywhere on surface → q_enclosed = 0?**

**Yes.** If E = 0 at every point on the surface, then ∮ E⃗ · dA⃗ = 0, which by Gauss's law means q_enclosed = 0.

> 🔑 Zero flux does NOT imply zero field. But zero field everywhere DOES imply zero enclosed charge.
</details>

---

### Q 1.18

Sketch the electric field lines for a uniformly charged hollow cylinder shown in the figure.

<details>
<summary><b>Solution</b></summary>

For a uniformly charged hollow cylinder:

**Near the middle (far from ends):** The cylinder approximates an infinite charged wire → field lines point **radially outward** (perpendicular to the curved surface).

**Near the ends:** Field lines **curve** and spread outward. Some lines emerge from the flat circular edges.

**Inside the cylinder:** For a thin hollow cylinder, E ≈ 0 inside (similar to a spherical shell, though not exactly zero due to finite length).

**Far away:** The entire cylinder looks like a point charge → field lines become radial.

Key features of the sketch:
- Lines are densest near the curved surface (strongest field)
- Lines are perpendicular to the surface everywhere (conductor property if conducting)
- Lines curve at the edges/ends
- No lines inside (approximately, for thin shell)
</details>

---

### Q 1.19

If the total charge contained in a volume is known, can the electric field on the surface enclosing the volume be determined using Gauss's Law? If not, what additional information is needed?

<details>
<summary><b>Solution</b></summary>

**No**, knowing q_enclosed alone is generally NOT sufficient to determine E at every point on the surface.

Gauss's law gives: ∮ E⃗ · dA⃗ = q/ε₀

This is a single equation relating an integral of E over the surface to the enclosed charge. To extract E from the integral, we need **additional information**:

**We need sufficient symmetry** so that:
1. E has a **constant magnitude** over the Gaussian surface (or parts of it)
2. E is either **parallel** or **perpendicular** to dA⃗ at every point

This is possible only for three types of symmetry:
- **Spherical symmetry** (concentric sphere as Gaussian surface)
- **Cylindrical symmetry** (coaxial cylinder)
- **Planar symmetry** (pill-box)

Without such symmetry, Gauss's law is true but not computationally useful for finding E.
</details>

---

## Long Answer Questions

### Q 1.20 ⭐

A paisa coin is made of Al-Mg alloy and weighs 0.75 g. It has a square shape and its diagonal measures 17 mm. It is electrically neutral and contains equal amounts of positive and negative charges. Treating the paisa coin as made of only Al (atomic mass = 26.98 g/mol, Z = 13), find the magnitude of the equal number of positive and negative charges. What conclusion do you draw from this magnitude?

<details>
<summary><b>Solution</b></summary>

**Step 1: Find number of atoms**

Number of moles = mass/molar mass = 0.75/26.98 = 0.0278 mol

Number of atoms = 0.0278 × 6.022 × 10²³ = **1.674 × 10²²**

**Step 2: Find total positive charge**

Each Al atom has Z = 13 protons.

Total positive charge = N × Z × e
= 1.674 × 10²² × 13 × 1.6 × 10⁻¹⁹
= **3.48 × 10⁴ C = 34.8 kC**

**Step 3: Total negative charge = −34.8 kC** (equal electrons)

**Conclusion:** Even a tiny coin contains an enormous amount of positive and negative charge (~34,800 C each!). The fact that matter is normally electrically neutral despite containing such huge charges shows the remarkable **balance** between protons and electrons. Even a tiny fractional imbalance would produce enormous electrostatic forces.

> 🔑 This magnitude (~35 kC) is astonishingly large. If even 1% of the electrons were removed, the coin would have a charge of ~350 C — enough to create forces of millions of tonnes!
</details>

---

### Q 1.21 ⭐

Consider the coin of Q 1.20. It is electrically neutral and contains equal amounts of positive and negative charge of magnitude 34.8 kC. Suppose that these charges were concentrated in two point charges separated by:

(i) 1 cm (= ½ diagonal) — Find the force.
(ii) 100 m — Find the force. What do you conclude?

<details>
<summary><b>Solution</b></summary>

**(i) Separation = 1 cm = 0.01 m**

F = kq₁q₂/r² = 9 × 10⁹ × 34800 × 34800 / (0.01)²

F = 9 × 10⁹ × 1.211 × 10⁹ / 10⁻⁴ = **1.09 × 10²³ N**

> That's about 10²³ N — a force equivalent to the weight of ~10¹⁹ tonnes. This is an incomprehensibly large force.

**(ii) Separation = 100 m**

F = 9 × 10⁹ × (34800)² / (100)²

F = 9 × 10⁹ × 1.211 × 10⁹ / 10⁴ = **1.09 × 10¹⁵ N**

> Still ~10¹⁵ N — a trillion newtons, even at 100 m!

**Conclusion:** The electrostatic force between the separated charges of even a small coin would be stupendously large at any reasonable distance. This demonstrates:
1. How enormously strong the electrostatic force is
2. Why exact neutrality of matter is crucial — even a tiny imbalance creates catastrophic forces
3. Why 1 coulomb is an extremely large unit of charge
</details>

---

### Q 1.22 ⭐⭐

Figure represents a crystal unit of caesium chloride (CsCl). The caesium atoms, each carrying a charge +e, are situated at the eight corners of a cube and a chlorine atom carrying a charge −e is at the centre of the cube. The edge length of the cube is 0.40 nm.

(a) What is the net electric field on the Cl⁻ ion due to the eight Cs⁺ ions?
(b) Suppose that the Cs⁺ ion at one corner A is missing. What is the net force now on the Cl⁻ ion due to the seven remaining Cs⁺ ions?

<details>
<summary><b>Solution</b></summary>

**(a) Net field at the centre due to all 8 Cs⁺:**

By **symmetry**, each corner Cs⁺ has a partner at the diagonally opposite corner. The electric field contributions from opposite corners point in opposite directions and have equal magnitudes (equal distance from centre).

Therefore, all contributions cancel in pairs.

**E_net = 0**

**(b) One Cs⁺ (at corner A) is missing:**

If all 8 were present → E = 0 (from part a).
If we remove one Cs⁺ at A, the net field = −(field due to the removed Cs⁺)

The removed Cs⁺ would have produced a field directed from A toward the centre. So the remaining 7 produce a field directed **from the centre toward A** (away from the missing corner).

**Distance from corner to centre of cube:**

Half-diagonal of cube with edge a = 0.40 nm:
d = (a√3)/2 = (0.40 × 10⁻⁹ × √3)/2 = 3.464 × 10⁻¹⁰ m

**Force on Cl⁻ (charge −e) due to the "missing" Cs⁺:**

F = ke²/d² = 9 × 10⁹ × (1.6 × 10⁻¹⁹)² / (3.464 × 10⁻¹⁰)²

= 9 × 10⁹ × 2.56 × 10⁻³⁸ / 1.2 × 10⁻¹⁹

= **1.92 × 10⁻⁹ N**

Direction: From the centre **toward corner A** (the Cl⁻ is pulled toward the vacant corner because the balancing Cs⁺ is gone, leaving the opposite corner's force uncompensated).

> 🔑 The symmetry trick: 7 charges = 8 charges − 1 charge. If 8 gives zero, then 7 gives the negative of the missing one's contribution.
</details>

---

### Q 1.23 ⭐⭐

Two charges q and −3q are placed fixed on the x-axis separated by distance d. Where should a third charge 2q be placed such that it will not experience any force?

<details>
<summary><b>Solution</b></summary>

Let charge q be at origin (x = 0) and charge −3q be at x = d.

The third charge 2q must be placed where the net force on it is zero. Since the two fixed charges have opposite signs, the null point is **outside** the two charges, **beyond the smaller magnitude charge** (q).

Let the third charge be at x = −x₀ (to the left of q, at distance x₀ from q).

Force due to q on 2q: F₁ = k(q)(2q)/x₀² — repulsive, in −x direction (pushing left)

Force due to −3q on 2q: F₂ = k(3q)(2q)/(d + x₀)² — attractive, in +x direction (pulling right)

For equilibrium: F₁ = F₂

k(2q²)/x₀² = k(6q²)/(d + x₀)²

1/x₀² = 3/(d + x₀)²

(d + x₀)² = 3x₀²

d + x₀ = ±√3 · x₀

Taking positive root: d + x₀ = √3 · x₀

d = (√3 − 1)x₀

$$\boxed{x_0 = \frac{d}{\sqrt{3} - 1} = \frac{d(\sqrt{3} + 1)}{2} \approx 1.366d}$$

The charge 2q should be placed at distance **d(√3 + 1)/2 ≈ 1.37d** to the left of charge q.

> Note: The sign of the third charge (2q) doesn't matter for the equilibrium position — only the magnitudes and positions of the fixed charges determine the null point.
</details>

---

### Q 1.24 ⭐

Figure shows the electric field lines around three point charges A, B, and C.

(a) Which charges are positive?
(b) Which charge has the largest magnitude? Why?
(c) In which region or regions of the picture could the electric field be zero? Justify.

<details>
<summary><b>Solution</b></summary>

**(a) Which charges are positive?**

Field lines **originate** from positive charges and **terminate** on negative charges.

- **A**: Lines emerge from A → **A is positive** ✓
- **C**: Lines emerge from C → **C is positive** ✓
- **B**: Lines terminate on B → **B is negative**

**(b) Which charge has the largest magnitude?**

The number of field lines is proportional to the magnitude of charge.

**B has the largest magnitude** because the total number of field lines terminating on B (coming from both A and C) is greater than the number emerging from either A or C individually.

If A has N₁ lines and C has N₂ lines, then B has (N₁ + N₂) lines → |q_B| = |q_A| + |q_C| (all lines from A and C terminate on B).

**(c) Where could E = 0?**

For E = 0, we need a point where the fields from all three charges cancel.

Since A and C are both positive and B is negative, the null point(s) would be:
- **Between A and C** (on the far side from B) — the repulsive fields from A and C push outward, while B's attraction pulls back. At some point they balance.
- More precisely: in the region **away from B**, between or beyond the positive charges A and C, where the fields from A and C (pointing away from them) can cancel.

The null point cannot be between A and B or between B and C (fields from both the positive charge and B would point in the same direction there).
</details>

---

### Q 1.25 ⭐⭐⭐

Five charges, q each, are placed at the corners of a regular pentagon of side 'a'.

(a) What will be the electric field at O, the centre of the pentagon?
(b) What will be the electric field at O if the charge from one of the corners (say A) is removed?
(c) What will be the electric field at O if the charge q at A is replaced by −q?

<details>
<summary><b>Solution</b></summary>

**(a) E at centre with all 5 charges:**

By **symmetry**, a regular pentagon with equal charges at all vertices produces zero net field at the centre. Each charge's field is exactly balanced by the others.

$$\boxed{E = 0}$$

**(b) One charge removed (charge at A removed):**

If all 5 charges produce E = 0, we can write:

E⃗_A + E⃗_remaining4 = 0

Therefore: E⃗_remaining4 = −E⃗_A

The field due to the missing charge A at the centre would be:

E_A = kq/r² (directed from A toward O, since charge at A would push a positive test charge toward O... wait, the charge at A is positive → field at O points **away from A**, i.e., from A through O outward)

So: E⃗_remaining4 = −E⃗_A → magnitude kq/r², directed **from O toward A** (toward the vacant vertex).

Now we need r (distance from vertex to centre of a regular pentagon):

For a regular pentagon with side a:
r = a/(2 sin(π/5)) = a/(2 sin 36°) = a/(2 × 0.5878) = **a/1.176 ≈ 0.851a**

$$\boxed{E = \frac{kq}{r^2} = \frac{kq}{0.724a^2} \text{, directed from O toward the vacant vertex A}}$$

Or equivalently: E = kq/(a/(2sin36°))² = 4kq sin²36°/a²

**(c) Charge at A replaced by −q:**

Original: all +q → E = 0.
Now: replace +q at A with −q. This is equivalent to:
- Keeping all +q (E = 0)
- Adding −2q at vertex A (since we changed from +q to −q = removing +q and adding −q = adding −2q)

Field at O due to the extra −2q at A:

E = k(2q)/r², directed **from O toward A** (since −2q attracts a positive test charge toward A)

$$\boxed{E = \frac{2kq}{r^2} = \frac{8kq\sin^2 36°}{a^2} \text{, directed from O toward A}}$$

> 🔑 **The symmetry trick used here is extremely powerful:**
> - 5 equal charges at regular polygon → E = 0 at centre
> - Remove one → E = field of ONE charge, pointing toward vacant vertex
> - Replace one by −q → E = field of TWO charges (2q), pointing toward that vertex
>
> This trick works for ANY regular polygon (triangle, square, hexagon, etc.)!
</details>

---

## Summary: Exam Readiness Checklist

### From the Exemplar MCQs:
- [ ] Q 1.4 — Do I understand why E on the LHS of Gauss's law depends on ALL charges?
- [ ] Q 1.7/1.13 — Can I analyze stability of a charge at the centre of a ring (plane vs axis)?
- [ ] Q 1.8 — Zero flux ≠ zero field. Am I clear on this?
- [ ] Q 1.11 — Do I know the multipole expansion (1/r³ dominance when net charge = 0)?

### From the Exemplar SA/LA:
- [ ] Q 1.15 — Can I find surface charge densities on inner/outer surfaces of a shell?
- [ ] Q 1.22 — Can I use the symmetry trick (8 charges − 1 = 7 charges)?
- [ ] Q 1.23 — Can I find equilibrium positions for unlike charges (null point outside)?
- [ ] Q 1.25 — Can I apply the pentagon symmetry trick (remove/replace one charge)?

---

*← [Back to MCQ Questions](./11_ncert_exemplar_mcq.md) · [Back to Table of Contents](./00_preface.md)*
