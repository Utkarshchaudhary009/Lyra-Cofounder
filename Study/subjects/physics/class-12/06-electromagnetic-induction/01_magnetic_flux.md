# Chapter 1: The Magnetic Flux — Counting Field Lines Through a Window

> *NCERT Section 6.2 | Class 12 Physics — Electromagnetic Induction*

---

## Stage 1: The Core Idea

### Rain on a Windowpane — The Perfect Analogy

Imagine standing outside in the rain. You hold a square window frame horizontally — rain pours straight down, and you catch **maximum** drops. Now tilt the frame to a 45° angle — fewer drops pass through. Tilt it vertically (frame edge-on to the falling rain) — **zero** drops pass through, even though the rain has not stopped!

This is **magnetic flux** in a nutshell. The magnetic field (B) is the "rain", and the surface area of your loop is the "window frame." **Magnetic flux** (Phi) measures how much of the magnetic field actually "passes through" the surface — and it depends critically on the **orientation** of that surface relative to the field.

### What is Magnetic Flux — Conceptually?

Think of a magnetic field as a set of invisible field lines flowing through space. Magnetic flux is simply **how many of those field lines pierce through a given surface**. If the surface faces the field head-on, maximum lines pass through. If the surface is parallel to the field (edge-on), zero lines pass through.

This concept is foundational: **electromagnetic induction happens only when flux CHANGES**, not when flux simply exists. A frozen flux, no matter how large, induces nothing. It is the *change* that matters — but that is Chapter 2. For now, let us master flux itself.

> Warning: Magnetic flux is a property of **both** the field AND the surface orientation together. You cannot talk about flux without specifying the surface.

> Tip: The "area vector" A points **perpendicular (normal) to the surface**. Its magnitude equals the area. The direction follows the right-hand rule for a closed loop.

> Key Takeaway: Flux is a **scalar** (a single number, can be positive, negative, or zero). It is NOT a vector quantity, even though it is calculated using a dot product of two vectors.

### Orientation vs. Flux — Comparison Table

| Orientation of Surface | Angle theta (B and normal) | cos theta | Flux |
|---|---|---|---|
| Normal parallel to B (field faces surface head-on) | 0 deg | 1 | **Maximum** = BA |
| Normal at 30 deg to field | 30 deg | sqrt(3)/2 approx 0.866 | 0.866 BA |
| Normal at 45 deg to field | 45 deg | 1/sqrt(2) approx 0.707 | 0.707 BA |
| Normal at 60 deg to field | 60 deg | 1/2 = 0.5 | **Half-max** = 0.5 BA |
| Normal perpendicular to B (surface edge-on) | 90 deg | 0 | **Zero** |
| Normal anti-parallel to B | 180 deg | -1 | **Minimum (negative)** = -BA |

> Classic Exam Trap: Beware! Problems sometimes give the angle between B and the **plane** of the coil (not the normal). If the plane makes angle alpha with B, then theta (angle with normal) = 90 - alpha, and flux = BA sin(alpha). This trap appears in **every board exam cycle!**


---

## Stage 2: The Formula Lab

### Core Formula

$$\boxed{\Phi_B = \vec{B} \cdot \vec{A} = BA\cos\theta}$$

where theta is the angle between the magnetic field vector B and the area normal vector n-hat.

### General (Non-Uniform Field) Formula

For a non-uniform magnetic field, flux must be integrated over the surface:

$$\Phi_B = \int_S \vec{B} \cdot d\vec{A} = \int_S B \cos\theta \; dA$$

### For a Coil with N Turns (Flux Linkage)

$$\Phi_{total} = N\Phi = NBA\cos\theta$$

### Gauss's Law for Magnetism (Closed Surface)

$$\oint_S \vec{B} \cdot d\vec{A} = 0$$

The total magnetic flux through **any** closed surface is always **zero**.

### Variable Reference Table

| Symbol | Meaning | SI Unit |
|---|---|---|
| $\Phi_B$ | Magnetic flux | Weber (Wb) |
| $\vec{B}$ | Magnetic field (flux density) | Tesla (T) |
| $B$ | Magnitude of magnetic field | T |
| $\vec{A}$ | Area vector (normal to surface) | m^2 |
| $A$ | Magnitude of area | m^2 |
| $\hat{n}$ | Unit normal vector to surface | dimensionless |
| $\theta$ | Angle between B and normal | degree or radian |
| $N$ | Number of turns in coil | dimensionless |

### What the Formula Tells Us

The formula Phi = BA cos(theta) encodes **three ways flux can change**:
1. **Change B** — vary the magnetic field strength
2. **Change A** — expand or shrink the area of the loop
3. **Change theta** — rotate the loop relative to the field

Any one of these three changes will change the flux — and changing flux drives electromagnetic induction!

### Key Numbers to Memorize

| Fact | Value |
|---|---|
| SI unit of flux | 1 Weber (Wb) |
| Equivalent units | 1 Wb = 1 T.m^2 = 1 V.s = 1 kg.m^2.A^-1.s^-2 |
| Flux through closed surface | Always **0** |
| Max flux through area A in field B | BA (when theta = 0 deg) |
| Flux is a ... | **Scalar** quantity |

### Special Cases Table

| theta (Normal vs. B) | Scenario | Phi |
|---|---|---|
| 0 deg | Field perpendicular to plane (parallel to normal) | BA (maximum) |
| 30 deg | | (sqrt(3)/2) BA |
| 60 deg | | (1/2) BA |
| 90 deg | Field parallel to plane of coil | 0 |
| 180 deg | Field anti-parallel to normal | -BA (minimum) |

---

## Stage 3: Type-wise Mastery

---

### Type 1: Direct Flux Calculation (B, A, theta given) *

**Pattern:** "A [shape] of area A is placed in magnetic field B making angle theta with [normal/field]. Find flux."

**Solved Example** (Easy)

> A rectangular loop of area 0.2 m^2 is placed in a uniform magnetic field of 0.5 T. The normal to the loop makes an angle of 60 deg with the magnetic field. Calculate the magnetic flux through the loop. (CBSE 2017, 2 marks)

<details><summary><b>Solution</b></summary>

**Given:**
- Area, A = 0.2 m^2
- Magnetic field, B = 0.5 T
- Angle between B and normal, theta = 60 deg

**Using the formula:**

$$\Phi = BA\cos\theta = 0.5 \times 0.2 \times \cos 60°$$

$$\Phi = 0.5 \times 0.2 \times 0.5$$

$$\boxed{\Phi = 0.05 \text{ Wb}}$$

Since theta is measured from the **normal**, we directly use cos 60 deg.

</details>

---

**Practice Questions**

1. (Easy) A circular coil of radius 0.1 m is placed in a uniform magnetic field of 2 T with its plane perpendicular to the field. Calculate the magnetic flux through the coil.

<details><summary><b>Answer</b></summary>

Plane perpendicular to field means normal is parallel to field: theta = 0 deg.

$$A = \pi r^2 = \pi \times (0.1)^2 = 0.01\pi \text{ m}^2$$

$$\Phi = BA\cos 0° = 2 \times 0.01\pi \times 1 = 0.02\pi \approx \boxed{6.28 \times 10^{-2} \text{ Wb}}$$

</details>

---

2. (Easy) A square loop of side 10 cm is placed in a uniform magnetic field of 0.4 T. The plane of the loop is parallel to the magnetic field. What is the flux through the loop?

<details><summary><b>Answer</b></summary>

Plane parallel to B means normal is perpendicular to B — theta = 90 deg.

$$A = (0.10)^2 = 0.01 \text{ m}^2$$

$$\Phi = BA\cos 90° = 0.4 \times 0.01 \times 0 = \boxed{0 \text{ Wb}}$$

</details>

---

3. (Medium) A rectangular coil of dimensions 4 cm x 5 cm is placed in a uniform magnetic field of 0.6 T. The normal to the coil makes 30 deg with the field. Find the flux linkage if the coil has 50 turns.

<details><summary><b>Answer</b></summary>

$$A = 0.04 \times 0.05 = 2 \times 10^{-3} \text{ m}^2$$

Single-turn flux: $$\Phi_1 = 0.6 \times 2\times10^{-3} \times \cos 30° = 0.6 \times 2\times10^{-3} \times \frac{\sqrt{3}}{2} = 1.039 \times 10^{-3} \text{ Wb}$$

Total flux linkage:

$$\Phi_{total} = N\Phi_1 = 50 \times 1.039 \times 10^{-3} \approx \boxed{5.2 \times 10^{-2} \text{ Wb}}$$

</details>

---

4. (Medium) A magnetic field of 3 T exists in a region. A circular loop of area 50 cm^2 is placed such that the flux through it is 75 mWb. Find the angle the normal to the loop makes with the field.

<details><summary><b>Answer</b></summary>

$$\cos\theta = \frac{\Phi}{BA} = \frac{75 \times 10^{-3}}{3 \times 50 \times 10^{-4}} = \frac{0.075}{0.015} = 0.5$$

$$\theta = \cos^{-1}(0.5) = \boxed{60°}$$

</details>

---

4b. 🌱 **Noob-Mode Bridge** 🟢 — *(Meet the "strip" method with a CONSTANT field first)*

A uniform field B = 0.3 T points along the normal of a rectangle of length L = 0.5 m and width 0.1 m (running from x = 0 to x = 0.1 m). Slice the rectangle into thin vertical strips of width dx and length L. (i) Write the flux dΦ through one strip. (ii) Add up all the strips to find the total flux.

<details><summary><b>Answer</b></summary>

Each strip has area dA = L·dx and the field is perpendicular to it, so:

$$d\Phi = B \cdot L \, dx$$

Since B is constant, add (integrate) all strips from x = 0 to x = 0.1:

$$\Phi = \int_0^{0.1} B L \, dx = BL\,[x]_0^{0.1} = 0.3 \times 0.5 \times 0.1 = \boxed{0.015 \text{ Wb}}$$

Check: this equals BA = 0.3 × (0.5 × 0.1) = 0.015 Wb. The strip method gives the same answer as BA when B is constant — now we are ready to let B vary.

</details>

---

4c. 🌱 **Noob-Mode Bridge** 🟡 — *(Now let B VARY — one new idea: keep B inside the integral)*

A field along z varies as B(x) = 6x (T, x in metres). A rectangular region has length L = 2 m (along y) and runs from x = 0 to x = 1 m. Find the total flux.

<details><summary><b>Answer</b></summary>

Strip at position x, width dx, length L = 2 m:

$$d\Phi = B(x)\cdot L\,dx = 6x \times 2 \, dx = 12x\,dx$$

$$\Phi = \int_0^1 12x\,dx = 12\left[\frac{x^2}{2}\right]_0^1 = 12 \times \frac{1}{2} = \boxed{6 \text{ Wb}}$$

Because B changes with x, it must stay INSIDE the integral. This is exactly the skill Q5 needs.

</details>

---

5. (Hard) In a region, the magnetic field varies as B(x) = B0(1 + kx), where B0 = 0.2 T, k = 2 m^-1. A rectangular loop of width w = 0.1 m and length L = 0.5 m has one side at x = 0 and the other at x = 0.1 m. The loop lies in the x-y plane. Find the total flux through the loop.

<details><summary><b>Answer</b></summary>

The field is along z-direction and varies with x. Take a strip at position x of width dx and length L:

$$d\Phi = B(x) \cdot L \cdot dx = B_0(1 + kx) \cdot L \cdot dx$$

$$\Phi = B_0 L\left[x + \frac{kx^2}{2}\right]_0^{0.1} = 0.2 \times 0.5 \times \left[0.1 + \frac{2 \times 0.01}{2}\right] = 0.1 \times 0.11 = \boxed{0.011 \text{ Wb}}$$

</details>

---

6. (Hard) A long solenoid of cross-sectional area 4 cm^2 carries a current. The magnetic field inside is 0.8 T. A circular coil of radius 2 cm is placed coaxially inside the solenoid. Find the flux through the coil.

<details><summary><b>Answer</b></summary>

The coil is coaxially inside; field is uniform at B = 0.8 T; normal is parallel to B (theta = 0 deg).

$$A_{coil} = \pi (0.02)^2 = 4\pi \times 10^{-4} \text{ m}^2$$

$$\Phi = 0.8 \times 4\pi \times 10^{-4} = 3.2\pi \times 10^{-4} \approx \boxed{1.005 \times 10^{-3} \text{ Wb}}$$

Use the **coil's** area, NOT the solenoid area.

</details>

---

6b. 🌱 **Noob-Mode Bridge** 🟡 — *(A 1/r field and the ln integral — the exact tool for the wire problem)*

A field varies as B(r) = 12/r (T, r in metres) and points along the normal of a strip. The strip has length a = 1 m and runs from r = 1 m to r = 2 m (width dr). Find the flux.

<details><summary><b>Answer</b></summary>

Strip at distance r, width dr, length a = 1 m:

$$d\Phi = B(r)\cdot a\,dr = \frac{12}{r}\times 1 \, dr$$

$$\Phi = 12\int_1^2 \frac{dr}{r} = 12\,[\ln r]_1^2 = 12(\ln 2 - \ln 1) = 12\ln 2 \approx 12 \times 0.693 = \boxed{8.32 \text{ Wb}}$$

Key new tool: $\int \frac{dr}{r} = \ln r$. A wire's field ($B = \mu_0 I/2\pi r$) has exactly this 1/r shape, so its flux always contains a natural log — ready for Q7.

</details>

---

7. (Hard) A square frame of side a is placed at distance d from an infinitely long wire carrying current I. The frame is in the same plane as the wire. Find the flux through the frame. (mu0 = 4 pi x 10^-7 T.m/A)

<details><summary><b>Answer</b></summary>

B(r) = mu0 I / (2 pi r). Take strip at distance r, width dr, length a:

$$d\Phi = \frac{\mu_0 I a}{2\pi r} dr$$

$$\Phi = \frac{\mu_0 I a}{2\pi} \int_d^{d+a} \frac{dr}{r} = \boxed{\frac{\mu_0 I a}{2\pi} \ln\!\left(1 + \frac{a}{d}\right)}$$

</details>


---

### Type 2: Angle with Plane vs. Angle with Normal *

**Pattern:** "The coil makes angle alpha with [the field / horizontal]. Find flux."

> THE MOST COMMON TRAP! Angle given w.r.t. the **plane** use: Phi = BA sin(alpha). Angle given w.r.t. the **normal** use: Phi = BA cos(theta).

**Solved Example** (Medium)

> A rectangular coil of area 0.15 m^2 is placed in a uniform magnetic field of 0.8 T. The plane of the coil makes an angle of 30 deg with the magnetic field. Find the magnetic flux through the coil.

<details><summary><b>Solution</b></summary>

**Key:** The angle (30 deg) is between the **plane** of the coil and B.

Therefore, angle between the **normal** to the coil and B:

$$\theta_{normal} = 90° - 30° = 60°$$

$$\Phi = BA\cos\theta_{normal} = 0.8 \times 0.15 \times \cos 60° = 0.8 \times 0.15 \times 0.5$$

$$\boxed{\Phi = 0.06 \text{ Wb}}$$

**Alternative:** Phi = BA sin(alpha_plane) = 0.8 x 0.15 x sin(30 deg) = 0.8 x 0.15 x 0.5 = 0.06 Wb. Verified!

</details>

---

**Practice Questions**

1. (Easy) A square coil of side 0.2 m is in a field of 1.5 T. The plane of the coil is parallel to B (0 deg with B). Find flux.

<details><summary><b>Answer</b></summary>

Plane parallel to B means normal perpendicular to B — theta = 90 deg.

$$\Phi = BA\cos 90° = \boxed{0 \text{ Wb}}$$

</details>

---

2. (Easy) A circular loop of radius 5 cm is in a field of 0.3 T. The plane of the loop makes 90 deg with B. Find flux.

<details><summary><b>Answer</b></summary>

Plane 90 deg to B means normal parallel to B — theta = 0 deg.

$$A = \pi(0.05)^2 = 7.854 \times 10^{-3} \text{ m}^2$$

$$\Phi = BA\cos 0° = 0.3 \times 7.854 \times 10^{-3} \approx \boxed{2.36 \times 10^{-3} \text{ Wb}}$$

</details>

---

3. (Medium) A coil of area 0.1 m^2 is in a field of 2 T. The plane makes 45 deg with B. Find flux and state what angle you use in the formula.

<details><summary><b>Answer</b></summary>

Angle with plane = 45 deg, angle with normal = 90 - 45 = 45 deg.

$$\Phi = BA\cos 45° = 2 \times 0.1 \times \frac{1}{\sqrt{2}} = \frac{0.2}{\sqrt{2}} \approx \boxed{0.141 \text{ Wb}}$$

The angle used in the formula is **45 deg** (between B and the normal).

</details>

---

4. (Medium) A 40 cm x 25 cm rectangular loop is in a field of 1.2 T. The broad face makes 60 deg with B. Find flux.

<details><summary><b>Answer</b></summary>

A = 0.40 x 0.25 = 0.10 m^2. Angle with plane = 60 deg, angle with normal = 30 deg.

$$\Phi = 1.2 \times 0.10 \times \cos 30° = 0.12 \times \frac{\sqrt{3}}{2} \approx \boxed{0.104 \text{ Wb}}$$

</details>

---

5. (Hard) A coil is placed so that Phi = (1/2)BA. Someone says "the plane makes 60 deg with the field." Is this correct? Justify and find what angle the normal actually makes.

<details><summary><b>Answer</b></summary>

$$\Phi = BA\cos\theta = \frac{1}{2}BA \implies \cos\theta = \frac{1}{2} \implies \theta = 60°$$

So the **normal makes 60 deg with the field**.

Angle of plane with B = 90 - 60 = 30 deg.

If the plane made 60 deg with B, then Phi = BA sin(60 deg) = (sqrt(3)/2)BA, which is NOT (1/2)BA.

So the statement is **incorrect** — the plane makes **30 deg** with the field.

</details>

---

6. (Hard) A coil is rotated from a position where its plane is perpendicular to B, to a position where the plane is parallel to B. If B = 0.5 T and A = 0.2 m^2, find the change in flux.

<details><summary><b>Answer</b></summary>

Initial: plane perpendicular to B, normal parallel to B, theta_i = 0 deg.

$$\Phi_i = BA\cos 0° = 0.5 \times 0.2 \times 1 = 0.1 \text{ Wb}$$

Final: plane parallel to B, normal perpendicular to B, theta_f = 90 deg.

$$\Phi_f = BA\cos 90° = 0$$

$$\Delta\Phi = 0 - 0.1 = \boxed{-0.1 \text{ Wb}}$$

Magnitude of change = 0.1 Wb (decrease).

</details>


---

### Type 3: Vector Flux (B dot A with components) *

**Pattern:** "B = Bx i-hat + By j-hat + Bz k-hat. A loop lies in [x-y / y-z / x-z] plane. Find flux."

> Key Rule: If the loop lies in the x-y plane, its area vector is along k-hat. If in y-z plane: along i-hat. If in x-z plane: along j-hat.

**Solved Example (Medium) — NCERT Exemplar Q 6.1**

> A square of side L lies in the x-y plane in a region where B = B0(2 i-hat + 3 j-hat + 4 k-hat) T, where B0 is a constant. Find the magnitude of magnetic flux through the square.

<details><summary><b>Solution</b></summary>

The square lies in the **x-y plane**. Area vector: A = L^2 k-hat.

**Using dot product:**

$$\Phi = \vec{B} \cdot \vec{A} = B_0(2\hat{i} + 3\hat{j} + 4\hat{k}) \cdot (L^2\hat{k})$$

$$= B_0 L^2 (2 \cdot 0 + 3 \cdot 0 + 4 \cdot 1)$$

$$\boxed{\Phi = 4B_0L^2 \text{ Wb}}$$

Only the k-hat component of B contributes to flux through a surface in the x-y plane!

</details>

---

**Solved Example (Hard) — NCERT Exemplar Q 6.2 (Adapted)**

> A loop ABCDEFA (3D path) covers two perpendicular faces of a cube of side L. B = B0 k-hat. Find the flux through the loop.

<details><summary><b>Solution</b></summary>

For the 3D loop, choose an open surface bounded by the loop. The loop ABCDEFA bounds a surface that can be divided into:

- A square of side L in the x-y plane (area vector = L^2 k-hat): Phi_1 = B0 x L^2 x 1 = B0 L^2
- A square of side L in the x-z plane (area vector = L^2 j-hat): Phi_2 = B0 k-hat . L^2 j-hat = 0

However, for the specific path ABCDEFA (the standard NCERT Exemplar problem), the effective projected area on the x-y plane is 2L^2:

$$\boxed{\Phi = 2B_0L^2 \text{ Wb}}$$

Key principle: flux through an open surface depends on the specific surface bounded by the path.

</details>

---

**Practice Questions**

1. (Easy) B = (3 i-hat + 4 j-hat) T. A square of side 2 m lies in the x-y plane. Find Phi.

<details><summary><b>Answer</b></summary>

A = (2)^2 k-hat = 4 k-hat m^2.

$$\Phi = (3\hat{i} + 4\hat{j}) \cdot 4\hat{k} = 4(3 \cdot 0 + 4 \cdot 0) = \boxed{0 \text{ Wb}}$$

Neither i-hat nor j-hat contributes to flux through x-y plane.

</details>

---

2. (Easy) B = (2 i-hat + 3 j-hat + 5 k-hat) T. A rectangle of area 0.5 m^2 lies in the y-z plane. Find Phi.

<details><summary><b>Answer</b></summary>

Loop in y-z plane: A = 0.5 i-hat m^2.

$$\Phi = (2\hat{i} + 3\hat{j} + 5\hat{k})\cdot(0.5\hat{i}) = 2 \times 0.5 = \boxed{1.0 \text{ Wb}}$$

</details>

---

3. (Medium) B = B0(i-hat + j-hat + k-hat) T. A square of side a lies in the x-z plane. Find flux.

<details><summary><b>Answer</b></summary>

Loop in x-z plane: area vector along j-hat: A = a^2 j-hat.

$$\Phi = B_0(\hat{i}+\hat{j}+\hat{k})\cdot a^2\hat{j} = B_0 a^2(0 + 1 + 0) = \boxed{B_0 a^2 \text{ Wb}}$$

</details>

---

4. (Medium) B = (4 i-hat - 3 j-hat + 5 k-hat) T. A loop has area vector A = (2 i-hat + 3 j-hat - k-hat) m^2. Find flux (with sign).

<details><summary><b>Answer</b></summary>

$$\Phi = \vec{B}\cdot\vec{A} = (4)(2) + (-3)(3) + (5)(-1) = 8 - 9 - 5 = \boxed{-6 \text{ Wb}}$$

Negative means the field passes through the surface opposite to the area normal direction.

</details>

---

5. (Hard) B = B0(2 i-hat + 3 j-hat + 4 k-hat) T. Square of side L in x-y plane, and another square of same L in y-z plane. Find ratio of fluxes.

<details><summary><b>Answer</b></summary>

**x-y plane:** A1 = L^2 k-hat, Phi_1 = B0 x 4 x L^2 = 4B0L^2

**y-z plane:** A2 = L^2 i-hat, Phi_2 = B0 x 2 x L^2 = 2B0L^2

$$\frac{\Phi_1}{\Phi_2} = \frac{4B_0L^2}{2B_0L^2} = \boxed{2:1}$$

</details>

---

5b. 🌱 **Noob-Mode Bridge** 🟡 — *(Strip integration in vector form — B along k-hat, varying with x)*

B = 2x k-hat (T, x in metres) threads a square of side 2 m lying in the x-y plane, from x = 0 to x = 2 m. Find the flux.

<details><summary><b>Answer</b></summary>

The area vector is along k-hat, so only the k-hat component matters. Take a strip at x, width dx, length 2 m (along y): dA = 2 dx k-hat.

$$d\Phi = \vec{B}\cdot d\vec{A} = (2x\hat{k})\cdot(2\,dx\,\hat{k}) = 4x\,dx$$

$$\Phi = \int_0^2 4x\,dx = 4\left[\frac{x^2}{2}\right]_0^2 = 4 \times 2 = \boxed{8 \text{ Wb}}$$

Same strip method as Type 1, now written with the dot product. Q6 is the identical idea with symbols instead of numbers.

</details>

---

6. (Hard) B = B0 x k-hat (field varies with x). Find flux through a square of side a in the x-y plane (one side at x = 0, opposite at x = a).

<details><summary><b>Answer</b></summary>

Take a strip at position x, width dx, length a (along y):

$$d\Phi = B_0 x \cdot a \cdot dx$$

$$\Phi = \int_0^a B_0 x \cdot a \, dx = B_0 a \cdot \frac{a^2}{2} = \boxed{\frac{B_0 a^3}{2} \text{ Wb}}$$

</details>


---

### Type 4: Total Flux through a Closed Surface

**Pattern:** "Find total flux through a closed surface / cube / sphere in a magnetic field."

**Solved Example** (Medium)

> A cube is placed in a uniform magnetic field B = B0 k-hat. Find the net magnetic flux through the entire cube.

<details><summary><b>Solution</b></summary>

Using **Gauss's Law for Magnetism:**

$$\oint_S \vec{B} \cdot d\vec{A} = 0$$

For any closed surface, the **net magnetic flux is always zero**.

Magnetic monopoles do not exist — magnetic field lines always form **closed loops**. Every field line that enters the closed surface must exit it.

$$\boxed{\Phi_{net} = 0}$$

**Verification (cube side a):**
- Top face (normal +k-hat): Phi_top = B0 . a^2
- Bottom face (normal -k-hat): Phi_bottom = -B0 . a^2
- Four side faces: normal perpendicular to k-hat, Phi = 0 each

Total = B0.a^2 + (-B0.a^2) + 0 + 0 + 0 + 0 = 0. Confirmed!

</details>

---

**Practice Questions**

1. (Easy) A spherical surface surrounds a bar magnet. What is the total magnetic flux through the spherical surface?

<details><summary><b>Answer</b></summary>

By Gauss's Law for magnetism, total flux through **any** closed surface is zero.

$$\boxed{\Phi_{net} = 0}$$

This holds regardless of what is inside the surface.

</details>

---

2. (Easy) Five faces of a closed cube have fluxes: +5, -3, +4, -2, +6 Wb. What is flux through the sixth face?

<details><summary><b>Answer</b></summary>

Total = 0 (Gauss's Law for magnetism).

$$5 + (-3) + 4 + (-2) + 6 + \Phi_6 = 0 \implies 10 + \Phi_6 = 0$$

$$\boxed{\Phi_6 = -10 \text{ Wb}}$$

</details>

---

3. (Medium) For a cube in field B = B k-hat, which faces have zero flux and which have non-zero flux?

<details><summary><b>Answer</b></summary>

Four side faces (normals along +/- i-hat and +/- j-hat) have **zero** flux because B = Bk-hat is perpendicular to their normals.

Only top (normal +k-hat, flux = +Ba^2) and bottom (normal -k-hat, flux = -Ba^2) have non-zero flux. These cancel: net = 0.

</details>

---

4. (Medium) A closed cylinder in a non-uniform field has fluxes: curved surface = 3 Wb, top face = -1 Wb. Find flux through bottom face.

<details><summary><b>Answer</b></summary>

$$3 + (-1) + \Phi_{bottom} = 0 \implies \boxed{\Phi_{bottom} = -2 \text{ Wb}}$$

</details>

---

5. (Hard) Why does Gauss's Law for magnetism always give zero for any closed surface? Contrast with Gauss's Law for electricity.

<details><summary><b>Answer</b></summary>

**Gauss's Law for Electricity:** ∮ E . dA = q_enc / epsilon_0 — non-zero because **electric monopoles (charges)** exist; field lines begin/end at charges.

**Gauss's Law for Magnetism:** ∮ B . dA = 0 — always zero because **magnetic monopoles do not exist** in nature. Magnetic field lines always form closed loops — they cannot begin or terminate at any point. Every field line entering a closed surface must also exit it, so net flux = zero.

This is one of Maxwell's four fundamental equations.

</details>


---

### Type 5: Flux through a Coil (N Turns)

**Pattern:** "A coil of N turns, each of area A, is placed in field B at angle theta. Find the total flux linkage."

**Solved Example (Easy) — CBSE 2018**

> A circular coil of N turns and radius r is placed in a uniform magnetic field B such that the normal to the coil makes an angle theta with B. Find the magnetic flux through the coil.

<details><summary><b>Solution</b></summary>

**For a single turn:**

$$\Phi_{one} = B \cdot \pi r^2 \cdot \cos\theta$$

**For N turns (total flux linkage):**

$$\boxed{\Phi_{total} = NB\pi r^2\cos\theta}$$

Special cases:
- theta = 0 deg: Phi_max = NBpi r^2 (maximum)
- theta = 90 deg: Phi = 0 (zero)

</details>

---

**Practice Questions**

1. (Easy) A coil of 200 turns and area 100 cm^2 is in a field of 0.5 T perpendicular to the plane of the coil. Find the flux linkage.

<details><summary><b>Answer</b></summary>

N = 200, A = 10^-2 m^2, B = 0.5 T, theta = 0 deg.

$$\Phi = NBA\cos 0° = 200 \times 0.5 \times 10^{-2} \times 1 = \boxed{1 \text{ Wb}}$$

</details>

---

2. (Easy) A coil of 50 turns, area 20 cm^2 is in a 2 T field with the plane parallel to the field. Find flux linkage.

<details><summary><b>Answer</b></summary>

Plane parallel to B means theta = 90 deg.

$$\Phi = NBA\cos 90° = \boxed{0 \text{ Wb}}$$

</details>

---

3. (Medium) A coil of 100 turns, radius 5 cm is in a field of 0.4 T. The plane of the coil makes 60 deg with the field. Find flux linkage.

<details><summary><b>Answer</b></summary>

A = pi(0.05)^2 = 7.854 x 10^-3 m^2. Plane makes 60 deg with field means normal makes 30 deg with field.

$$\Phi = NBA\cos 30° = 100 \times 0.4 \times 7.854\times10^{-3} \times \frac{\sqrt{3}}{2}$$

$$= 100 \times 0.4 \times 7.854\times10^{-3} \times 0.866 \approx \boxed{0.272 \text{ Wb}}$$

</details>

---

4. (Medium) A search coil of 500 turns, area 2 cm^2 has flux linkage 0.03 Wb when normal is parallel to the field. Find B.

<details><summary><b>Answer</b></summary>

$$B = \frac{\Phi}{NA} = \frac{0.03}{500 \times 2\times10^{-4}} = \frac{0.03}{0.1} = \boxed{0.3 \text{ T}}$$

</details>

---

5. (Hard) A toroid has 400 turns, cross-sectional area 3 cm^2, and field inside B = 0.5 T everywhere in the core. Find the total flux linkage.

<details><summary><b>Answer</b></summary>

For each turn: Phi_one = BA = 0.5 x 3 x 10^-4 = 1.5 x 10^-4 Wb

Total: Phi_total = N x Phi_one = 400 x 1.5 x 10^-4 = 0.06 Wb

$$\boxed{\Phi_{total} = 0.06 \text{ Wb}}$$

</details>

---

### Type 6: Change in Flux (Delta Phi Problems)

**Pattern:** "A coil changes from [initial state] to [final state]. Find delta Phi."

**Solved Example** (Medium)

> A circular coil of 50 turns and radius 0.1 m is placed in a uniform magnetic field of 0.2 T with its plane perpendicular to the field. The coil is then rotated through 90 deg about a diameter. Find the change in magnetic flux.

<details><summary><b>Solution</b></summary>

**Initial:** Plane perpendicular to field, normal parallel to field, theta_i = 0 deg.

$$\Phi_i = NBA\cos 0° = 50 \times 0.2 \times \pi(0.1)^2 = 50 \times 0.2 \times 0.01\pi = 0.1\pi = 0.314 \text{ Wb}$$

**After rotating 90 deg:** theta_f = 90 deg.

$$\Phi_f = NBA\cos 90° = 0$$

$$\Delta\Phi = \Phi_f - \Phi_i = 0 - 0.314 = \boxed{-0.314 \text{ Wb}}$$

Magnitude of change = 0.314 Wb (decrease).

</details>

---

**Practice Questions**

1. (Easy) A coil (normal parallel to field) is in B = 0.5 T, A = 0.04 m^2. Field is switched off. Find delta Phi.

<details><summary><b>Answer</b></summary>

Phi_i = 0.5 x 0.04 = 0.02 Wb; Phi_f = 0.

$$\Delta\Phi = 0 - 0.02 = \boxed{-0.02 \text{ Wb}}$$

</details>

---

2. (Easy) Field through a coil (area 0.1 m^2, normal parallel to field) changes from 1 T to 4 T. Find delta Phi.

<details><summary><b>Answer</b></summary>

$$\Delta\Phi = (B_f - B_i) \times A = (4 - 1) \times 0.1 = \boxed{0.3 \text{ Wb}}$$

</details>

---

3. (Medium) A square loop of side 10 cm is in a field of 0.3 T with its plane parallel to B. It is rotated 90 deg so the plane becomes perpendicular to B. Find delta Phi.

<details><summary><b>Answer</b></summary>

Initial: plane parallel to B, theta = 90 deg, Phi_i = 0.3 x 0.01 x cos(90) = 0.

Final: plane perpendicular to B, theta = 0 deg, Phi_f = 0.3 x 0.01 x 1 = 3 x 10^-3 Wb.

$$\Delta\Phi = 3\times10^{-3} - 0 = \boxed{3 \times 10^{-3} \text{ Wb}}$$

</details>

---

4. (Medium) A coil of 100 turns and area 50 cm^2 is in a field that changes from 0.8 T to 0.2 T (normal parallel to field). Find delta Phi (total flux linkage change).

<details><summary><b>Answer</b></summary>

$$\Delta\Phi_{linkage} = N(B_f - B_i)A = 100 \times (0.2 - 0.8) \times 50\times10^{-4}$$

$$= 100 \times (-0.6) \times 5\times10^{-3} = \boxed{-0.3 \text{ Wb}}$$

</details>

---

4b. 🌱 **Noob-Mode Bridge** 🟢 — *(Angles bigger than 90°: flux can go NEGATIVE)*

A coil has NBA = 8 Wb. Find its flux linkage when the normal makes (i) θ = 60° with the field, and (ii) θ = 120° with the field. Then find the change ΔΦ from (i) to (ii).

<details><summary><b>Answer</b></summary>

(i) $\Phi_1 = NBA\cos 60° = 8 \times 0.5 = 4$ Wb

(ii) $\cos 120° = -0.5$, so $\Phi_2 = NBA\cos 120° = 8 \times (-0.5) = -4$ Wb

$$\Delta\Phi = \Phi_2 - \Phi_1 = -4 - 4 = \boxed{-8 \text{ Wb}}$$

Flipping past 90° makes cos negative, so the flux reverses sign. Flipping a coil by 180° turns θ into 180° − θ — exactly the move Q5 asks for.

</details>

---

5. (Hard) A 200-turn coil (area 0.02 m^2) has its plane making 30 deg with a 1.5 T field. It is then flipped 180 deg (normal reverses). Find delta Phi.

<details><summary><b>Answer</b></summary>

Plane makes 30 deg with B — normal makes 60 deg with B.

Initial: theta_i = 60 deg.

$$\Phi_i = NBA\cos 60° = 200 \times 1.5 \times 0.02 \times 0.5 = 3 \text{ Wb}$$

After flipping 180 deg, new theta = 180 - 60 = 120 deg.

$$\Phi_f = NBA\cos 120° = 200 \times 1.5 \times 0.02 \times (-0.5) = -3 \text{ Wb}$$

$$\Delta\Phi = -3 - 3 = \boxed{-6 \text{ Wb}}$$

</details>


---

## Stage 4: MCQ Mastery

**Q1.** The SI unit of magnetic flux is:

(a) Tesla &emsp; (b) Weber &emsp; (c) Henry &emsp; (d) Tesla/meter^2

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Weber**

1 Weber (Wb) = 1 T.m^2 = 1 V.s. Tesla is the unit of the magnetic field B itself. Henry is the unit of inductance.

</details>

---

**Q2.** A rectangular coil is placed in a uniform magnetic field. The flux through the coil is maximum when:

(a) The plane of the coil is parallel to B
(b) The plane of the coil is perpendicular to B
(c) The plane makes 45 deg with B
(d) The plane makes 60 deg with B

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) The plane of the coil is perpendicular to B**

When the plane is perpendicular to B, the normal is parallel to B (theta = 0 deg), giving Phi = BA cos(0) = BA = maximum. Option (a): normal perpendicular to B, theta = 90 deg, Phi = 0.

</details>

---

**Q3.** B = B0(2 i-hat + 3 j-hat + 4 k-hat) passes through a square of side L in the x-y plane. The magnetic flux is: (NCERT Exemplar)

(a) 2B0L^2 Wb &emsp; (b) 3B0L^2 Wb &emsp; (c) 4B0L^2 Wb &emsp; (d) sqrt(29) B0L^2 Wb

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) 4B0L^2 Wb**

A = L^2 k-hat. Phi = B0(2 i-hat + 3 j-hat + 4 k-hat) . L^2 k-hat = 4B0L^2. Only the k-hat component contributes. Option (d) is the error of using |B| times area instead of the dot product.

</details>

---

**Q4.** The net magnetic flux through a closed surface is:

(a) Always positive &emsp; (b) Always negative &emsp; (c) Always zero &emsp; (d) Depends on the enclosed source

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Always zero**

By Gauss's Law for Magnetism (∮ B . dA = 0), net flux through any closed surface is always zero — magnetic monopoles do not exist.

</details>

---

**Q5.** A circular loop is kept in a region where the magnetic field is uniform and constant. The induced emf in the loop is:

(a) Non-zero and constant &emsp; (b) Non-zero and varying &emsp; (c) Zero &emsp; (d) Cannot be determined

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Zero**

A constant field means Phi = BA cos(theta) does not change. emf = -dPhi/dt = 0. Flux alone does NOT induce emf — **CHANGE in flux** does.

</details>

---

**Q6.** (Assertion-Reason Type)

**Assertion (A):** The magnetic flux through a surface can be negative.

**Reason (R):** Magnetic flux is a scalar and the dot product B . A can be negative when the angle between B and A is greater than 90 deg.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) Both A and R are true, and R is the correct explanation of A**

Phi = BA cos(theta). When 90 deg < theta <= 180 deg, cos(theta) < 0, so Phi < 0. This means the field passes through the surface opposite to the chosen area normal. Both assertion and reason are correct, and R explains A.

</details>

---

**Q7.** (Assertion-Reason Type)

**Assertion (A):** The magnetic flux through a coil does not depend on the resistance of the coil.

**Reason (R):** Magnetic flux Phi = NBA cos(theta) depends only on N, B, A, and theta.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) Both A and R are true, and R is the correct explanation of A**

The formula Phi = NBA cos(theta) has no resistance term. Resistance only affects induced current (via I = emf/R), not the flux. R correctly explains A.

</details>

---

**Q8.** (Statement-based)

**Statement I:** If the magnetic flux through a loop is zero, no magnetic field exists in the region.

**Statement II:** Magnetic flux being zero can occur when B is perpendicular to the area vector.

Which of the following is correct?

(a) Statement I is true, Statement II is false
(b) Statement I is false, Statement II is true
(c) Both statements are true
(d) Both statements are false

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Statement I is false, Statement II is true**

Statement I is **false** — flux can be zero even when B is non-zero (when theta = 90 deg, i.e., B parallel to plane of coil). Zero flux does NOT mean zero field.

Statement II is **true** — when B perpendicular to A (theta = 90 deg), Phi = BA cos(90) = 0 regardless of the value of B.

</details>

---

**Q9.** (Graph Interpretation) A circular coil rotates uniformly in a uniform magnetic field. The graph of flux vs. time t is:

(a) A straight line
(b) A sinusoidal curve
(c) An exponential decay
(d) A parabola

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) A sinusoidal curve**

As the coil rotates with angular velocity omega, theta = omega t, so:

$$\Phi(t) = BA\cos(\omega t)$$

This is a cosine (sinusoidal) function of time. This sinusoidal variation of flux leads to a sinusoidal induced emf (emf = BA omega sin(omega t)) — the basis of AC generators.

</details>

---

**Q10.** A long solenoid of cross-section area A carries current creating field B inside. A small loop of area A' (A' < A) is placed coaxially inside. The flux through the small loop is:

(a) BA' &emsp; (b) BA &emsp; (c) B(A - A') &emsp; (d) Zero

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) BA'**

The field inside the solenoid is uniform at B throughout. Flux through the small loop = B x (area of **small loop**) = BA'. A common error is using A (solenoid area) instead of A' (loop area).

</details>

---

**Q11.** (Exemplar Depth) Two different surfaces S1 and S2 are bounded by the same closed loop C. The flux through S1 is Phi1 and through S2 is Phi2. Then:

(a) Phi1 > Phi2 always
(b) Phi1 < Phi2 always
(c) Phi1 = Phi2 always
(d) Phi1 + Phi2 = 0 always

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Phi1 = Phi2 always**

Since div(B) = 0 (divergence of B is zero), the flux through any surface bounded by the same closed loop is identical. S1 and S2 form a closed volume, and Gauss's Law demands zero net flux through it, proving Phi1 = Phi2.

</details>

---

**Q12.** (FAQ Trap) Which of the following is NOT equivalent to 1 Weber?

(a) 1 T.m^2 &emsp; (b) 1 V.s &emsp; (c) 1 J/A &emsp; (d) 1 A.Omega.s^2

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d) 1 A.Omega.s^2**

- (a) 1 T.m^2 = 1 Wb (by definition) -- Correct
- (b) 1 V.s = 1 Wb (since emf = dPhi/dt, so Phi = emf x t) -- Correct
- (c) 1 J/A = 1 Wb (since 1 H = 1 Wb/A and 1 J = 1 H.A^2) -- Correct
- (d) 1 A.Omega.s^2 = A.(V/A).s^2 = V.s^2 = NOT V.s = NOT Wb -- **Incorrect unit**

</details>


---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 2 + 5 combined

A coil of 80 turns, each of area 0.05 m^2, is placed in a uniform magnetic field of 1.2 T. The plane of the coil makes an angle of 30 deg with the direction of the field. Calculate:
(a) The total flux linkage
(b) The new flux linkage if the coil is rotated so the plane becomes perpendicular to the field
(c) The change in total flux linkage

<details><summary><b>Solution</b></summary>

**Given:** N = 80, A = 0.05 m^2, B = 1.2 T

**(a)** Plane makes 30 deg with B, so normal makes 60 deg with B.

$$\Phi_i = NBA\cos 60° = 80 \times 1.2 \times 0.05 \times 0.5 = \boxed{2.4 \text{ Wb}}$$

**(b)** Plane perpendicular to field, normal parallel to field, theta = 0 deg.

$$\Phi_f = NBA\cos 0° = 80 \times 1.2 \times 0.05 \times 1 = \boxed{4.8 \text{ Wb}}$$

**(c)**

$$\Delta\Phi = \Phi_f - \Phi_i = 4.8 - 2.4 = \boxed{2.4 \text{ Wb}}$$

</details>

---

**Problem 2** (Medium) — Types 3 + 4 combined

B = (3 i-hat + 4 j-hat + 5 k-hat) T exists uniformly throughout space. A closed cube of side 0.2 m is placed in this field.
(a) Find flux through the top face (normal +k-hat).
(b) Find flux through the right face (normal +i-hat).
(c) What is the net flux through the entire box?

<details><summary><b>Solution</b></summary>

A = (0.2)^2 = 0.04 m^2 for each face.

**(a)** Top face, area vector = 0.04 k-hat:

$$\Phi_{top} = (3\hat{i}+4\hat{j}+5\hat{k})\cdot 0.04\hat{k} = 5 \times 0.04 = \boxed{0.20 \text{ Wb}}$$

**(b)** Right face, area vector = 0.04 i-hat:

$$\Phi_{right} = (3\hat{i}+4\hat{j}+5\hat{k})\cdot 0.04\hat{i} = 3 \times 0.04 = \boxed{0.12 \text{ Wb}}$$

**(c)** By Gauss's Law for magnetism:

$$\Phi_{net} = \boxed{0 \text{ Wb}}$$

Verification: Bottom = -0.20, left = -0.12, front = +0.16, back = -0.16 Wb. Total = 0.20 - 0.20 + 0.12 - 0.12 + 0.16 - 0.16 = 0. Confirmed!

</details>

---

**Problem 3** (Hard) — Types 1 + 2 + 6 combined

A rectangular coil (20 cm x 15 cm, 100 turns) rotates from a position where its plane makes 40 deg with a 0.8 T uniform field to a position where its plane makes 20 deg with the same field. Calculate:
(a) Initial flux linkage
(b) Final flux linkage
(c) Change in flux linkage

<details><summary><b>Solution</b></summary>

A = 0.20 x 0.15 = 0.03 m^2, N = 100, B = 0.8 T

**(a)** Plane makes 40 deg with B — normal makes 50 deg with B.

$$\Phi_i = NBA\cos 50° = 100 \times 0.8 \times 0.03 \times 0.6428 = 2.4 \times 0.6428 \approx \boxed{1.543 \text{ Wb}}$$

**(b)** Plane makes 20 deg with B — normal makes 70 deg with B.

$$\Phi_f = NBA\cos 70° = 2.4 \times 0.3420 \approx \boxed{0.821 \text{ Wb}}$$

**(c)**

$$\Delta\Phi = 0.821 - 1.543 = \boxed{-0.722 \text{ Wb}}$$

The flux linkage decreases by 0.722 Wb.

</details>

---

**Problem 4** (Hard — Competency-Based) — Types 3 + 5 + 6 combined

A research team designs a coil sensor to detect magnetic fields. The sensor: 500 turns, each turn 4 cm x 3 cm. They place it in a region where B = B0(2 i-hat - 3 k-hat) T, and the area vector of the coil is A = (12 x 10^-4) k-hat m^2.

(a) Calculate the flux through one turn of the coil.
(b) Calculate total flux linkage.
(c) If repositioned so area vector becomes A' = (12 x 10^-4) i-hat m^2, find new total flux linkage.
(d) Which orientation detects higher flux magnitude?

<details><summary><b>Solution</b></summary>

**(a)** One turn, A = 12 x 10^-4 k-hat m^2:

$$\Phi_{one} = B_0(2\hat{i} - 3\hat{k})\cdot 12\times10^{-4}\hat{k} = B_0 \times 12\times10^{-4} \times (-3) = -3.6\times10^{-3}B_0 \text{ Wb}$$

**(b)** Total flux linkage:

$$\Phi_{total} = 500 \times (-3.6\times10^{-3}B_0) = -1.8B_0 \text{ Wb}$$

**(c)** A' = 12 x 10^-4 i-hat m^2:

$$\Phi'_{one} = B_0(2\hat{i}-3\hat{k})\cdot 12\times10^{-4}\hat{i} = 2B_0 \times 12\times10^{-4} = 2.4\times10^{-3}B_0 \text{ Wb}$$

$$\Phi'_{total} = 500 \times 2.4\times10^{-3}B_0 = 1.2B_0 \text{ Wb}$$

**(d)** Original: |Phi_total| = 1.8 B0 Wb; New: |Phi'_total| = 1.2 B0 Wb.

The **original orientation** (area vector along k-hat) detects higher flux magnitude.

</details>


---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE 2017 pattern]**

(a) Define the term 'magnetic flux'. Write its SI unit.
(b) A circular loop of area 0.1 m^2 is placed in a magnetic field of 0.8 T. The plane of the loop makes an angle of 60 deg with the direction of the field. Calculate the magnetic flux through the loop.

<details><summary><b>Model Answer</b></summary>

**(a) Definition:** Magnetic flux through a surface is defined as the scalar product of the magnetic field B and the area vector A of the surface:

$$\Phi_B = \vec{B}\cdot\vec{A} = BA\cos\theta$$

where theta is the angle between B and the normal to the surface.

**SI unit:** Weber (Wb) [also accepted: T.m^2 or V.s] **[1 mark]**

**(b) Calculation:**

Plane makes 60 deg with field — normal makes 90 - 60 = 30 deg with field.

$$\Phi = BA\cos 30° = 0.8 \times 0.1 \times \frac{\sqrt{3}}{2} = 0.08 \times 0.866 \approx \boxed{6.93 \times 10^{-2} \text{ Wb}}$$ **[1 mark]**

</details>

---

**Q2. [3 marks — CBSE Board pattern]**

A square loop of side 20 cm and resistance 4 Ohm is placed in a uniform magnetic field of 0.5 T perpendicular to the plane of the loop.

(a) Find the magnetic flux through the loop. [1 mark]
(b) If the side is reduced to 10 cm (same field and orientation), find new flux and change in flux. [1 mark]
(c) Does the resistance of the loop affect the magnetic flux? Justify. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** Field perpendicular to plane, theta = 0 deg.

$$A_1 = (0.20)^2 = 0.04 \text{ m}^2, \quad \Phi_1 = 0.5 \times 0.04 = \boxed{0.02 \text{ Wb}}$$ **[1 mark]**

**(b)** New A2 = (0.10)^2 = 0.01 m^2.

$$\Phi_2 = 0.5 \times 0.01 = 5\times10^{-3} \text{ Wb}, \quad \Delta\Phi = 5\times10^{-3} - 0.02 = \boxed{-0.015 \text{ Wb}}$$ **[1 mark]**

**(c) No.** Phi = BA cos(theta) depends only on B, A, and theta — NOT on resistance. Resistance only affects induced current (I = emf/R), not the flux itself. **[1 mark]**

</details>

---

**Q3. [3 marks — CBSE Exemplar-level]**

A square of side L lies in the x-y plane in a region where B = B0(2 i-hat + 3 j-hat + 4 k-hat) T.

(a) Write down the area vector for the square. [1 mark]
(b) Calculate the magnetic flux through the square. [1 mark]
(c) If the same square were placed in the y-z plane in the same field, what would the flux be? [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** The square lies in the x-y plane. Its area vector is perpendicular to the x-y plane:

$$\vec{A} = L^2\hat{k} \text{ m}^2$$ **[1 mark]**

**(b)** Using dot product:

$$\Phi = B_0(2\hat{i}+3\hat{j}+4\hat{k})\cdot(L^2\hat{k}) = B_0L^2(0 + 0 + 4) = \boxed{4B_0L^2 \text{ Wb}}$$ **[1 mark]**

**(c)** In y-z plane, A' = L^2 i-hat:

$$\Phi' = B_0(2\hat{i}+3\hat{j}+4\hat{k})\cdot(L^2\hat{i}) = \boxed{2B_0L^2 \text{ Wb}}$$ **[1 mark]**

</details>

---

**Q4. [5 marks — Long Answer]**

(a) State Gauss's Law for magnetism. What does it imply about the nature of magnetic sources? [2 marks]
(b) Five faces of a closed cube have fluxes (in Wb): +8, -5, +3, -4, +6. Find flux through the sixth face. [1 mark]
(c) A coil of 200 turns and radius 8 cm is placed in a uniform magnetic field of 0.6 T. The plane of the coil makes 53 deg with the magnetic field. Calculate the flux linkage. (cos 37 deg = 0.8) [2 marks]

<details><summary><b>Model Answer</b></summary>

**(a) Gauss's Law for Magnetism:**

$$\oint_S \vec{B}\cdot d\vec{A} = 0$$

The net magnetic flux through any closed surface is zero. **[1 mark]**

**Implication:** Magnetic monopoles do not exist. Magnetic poles always exist in pairs (dipoles). Magnetic field lines always form closed loops — they never originate or terminate at a single point. **[1 mark]**

**(b)**

$$8 + (-5) + 3 + (-4) + 6 + \Phi_6 = 0 \implies 8 + \Phi_6 = 0 \implies \boxed{\Phi_6 = -8 \text{ Wb}}$$ **[1 mark]**

**(c)** N = 200, r = 0.08 m, B = 0.6 T. Plane makes 53 deg with field means normal makes 37 deg with field.

$$A = \pi r^2 = \pi \times (0.08)^2 = 64\pi\times10^{-4} \approx 2.011\times10^{-2} \text{ m}^2$$

$$\Phi = NBA\cos 37° = 200 \times 0.6 \times 2.011\times10^{-2} \times 0.8 \approx \boxed{1.93 \text{ Wb}}$$ **[2 marks]**

</details>

---

**Q5. [5 marks — Competency-Based / Case Study]**

MRI machines use superconducting coils to produce extremely strong, uniform magnetic fields (1.5-3 T) in a cylindrical bore. A small detector coil of 100 turns and radius 2 cm is placed coaxially inside the 1.5 T bore field (field directed along the axis of the cylinder).

(a) Calculate the flux through the detector coil when placed with its normal parallel to the main field. [1 mark]
(b) The detector coil is rotated so its plane makes 30 deg with the main field. Find the new flux linkage. [2 marks]
(c) Why is it important to ensure the plane of the detector coil is perpendicular to the main field for maximum sensitivity? [1 mark]
(d) If the main field is gradually reduced to zero, what happens to the flux? What effect does this have? [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** N = 100, r = 0.02 m, B = 1.5 T, theta = 0 deg.

$$A = \pi(0.02)^2 = 4\pi\times10^{-4} \text{ m}^2$$

$$\Phi_{one} = BA\cos 0° = 1.5 \times 4\pi\times10^{-4} \approx \boxed{1.885\times10^{-3} \text{ Wb}}$$ **[1 mark]**

**(b)** Plane makes 30 deg with field — normal makes 60 deg with field.

$$\Phi_{linkage} = N \times BA\cos 60° = 100 \times 1.5 \times 4\pi\times10^{-4} \times 0.5$$

$$= 100 \times 9.42\times10^{-4} = \boxed{9.42\times10^{-2} \text{ Wb}}$$ **[2 marks]**

**(c)** When normal is parallel to field (theta = 0 deg), flux is maximum = BA. Maximum flux means any small change in field produces the largest possible change in flux, inducing the maximum detectable emf — giving maximum sensitivity. **[1 mark]**

**(d)** As B reduces to zero, Phi = BA also reduces to zero. This **changing flux induces an emf** (and current) in the detector coil (by Faraday's Law) — this is how the MRI machine detects signals. **[1 mark]**

</details>


---

## Stage 7: JEE Mains Arena

**Q1.** A square loop of side a is placed in the x-y plane. Magnetic field B = B0 y k-hat exists in the region. The loop extends from y = 0 to y = a. The magnetic flux through the loop is:

(a) $B_0 a^2$ &emsp; (b) $\dfrac{1}{2}B_0 a^3$ &emsp; (c) $\dfrac{1}{2}B_0 a^2$ &emsp; (d) $2B_0 a^3$

<details><summary><b>Answer</b></summary>

**Answer: (b)** $\dfrac{1}{2}B_0 a^3$

The field B = B0 y varies with y. Take a strip at height y, width dy, length a (along x):

$$d\Phi = B_0 y \cdot a\,dy$$

$$\Phi = \int_0^a B_0 ya\,dy = B_0 a\left[\frac{y^2}{2}\right]_0^a = \frac{B_0 a^3}{2}$$

</details>

---

**Q2.** A hemispherical surface of radius R is placed in a uniform magnetic field B = B k-hat with the flat face in the x-y plane. The magnetic flux through the **curved** hemispherical surface is:

(a) $2\pi R^2 B$ &emsp; (b) $\pi R^2 B$ &emsp; (c) $-\pi R^2 B$ &emsp; (d) Zero

<details><summary><b>Answer</b></summary>

**Answer: (b)** $\pi R^2 B$

**Smart approach using Gauss's Law:**

The closed surface = curved hemisphere + flat circular base.

$$\Phi_{curved} + \Phi_{flat} = 0$$

For the flat circular base (in x-y plane, outward normal = -k-hat, area = pi R^2):

$$\Phi_{flat} = B\hat{k}\cdot(-\pi R^2\hat{k}) = -\pi R^2 B$$

$$\Phi_{curved} = -\Phi_{flat} = +\pi R^2 B$$

No need to integrate over the curved surface — just use Gauss's Law for magnetism!

</details>

---

**Q3.** B = B0(i-hat - 2 j-hat + 3 k-hat) T. Surface S1 has area vector A1 = (2 i-hat + j-hat) m^2. Surface S2 has area vector A2 = (a i-hat + b j-hat + c k-hat) m^2. If S1 and S2 are bounded by the **same closed loop**, which condition must hold?

(a) a = 2, b = 1, c = 0 &emsp; (b) $2a - b + 3c = 0$ &emsp; (c) $a - 2b + 3c = 0$ &emsp; (d) $a - 2b + 3c = 4$

<details><summary><b>Answer</b></summary>

**Answer: (c)** $a - 2b + 3c = 0$

Since S1 and S2 share the same boundary loop, their fluxes must be equal (div(B) = 0):

$$\vec{B}\cdot\vec{A}_1 = B_0(\hat{i}-2\hat{j}+3\hat{k})\cdot(2\hat{i}+\hat{j}+0\hat{k}) = B_0(2 - 2 + 0) = 0$$

$$\vec{B}\cdot\vec{A}_2 = B_0(a - 2b + 3c) = 0 \implies a - 2b + 3c = 0$$

</details>

---

**Q4.** A coil rotates at frequency f in a magnetic field B. Area of coil = A. At t = 0, the plane of the coil is perpendicular to B (maximum flux position). The magnetic flux as a function of time is:

(a) $\Phi = BA\sin(2\pi ft)$ &emsp; (b) $\Phi = BA\cos(2\pi ft)$ &emsp; (c) $\Phi = BA\sin^2(\pi ft)$ &emsp; (d) $\Phi = BA(1 - \cos 2\pi ft)$

<details><summary><b>Answer</b></summary>

**Answer: (b)** $\Phi = BA\cos(2\pi ft)$

At t = 0, plane perpendicular to B means normal parallel to B, theta = 0, Phi = BA (maximum).

As the coil rotates with omega = 2 pi f:

$$\Phi(t) = BA\cos(\omega t) = BA\cos(2\pi f t)$$

Starts at maximum (BA) at t = 0 — cosine function is correct. If t = 0 were defined at zero flux position, answer would be sine.

</details>

---

**Q5.** An irregular shaped wire loop of area A is placed perpendicular to a uniform magnetic field B. The wire is deformed into a circle (same perimeter, different shape) while remaining in the same field and orientation. If the circular area A' > A, what happens to the magnetic flux?

(a) Increases from BA to BA' &emsp; (b) Remains BA (unchanged) &emsp; (c) Decreases &emsp; (d) Becomes zero

<details><summary><b>Answer</b></summary>

**Answer: (a) Increases from BA to BA'**

Magnetic flux depends on the actual **enclosed area** of the loop, NOT on the perimeter. Since the loop is deformed from area A to area A' > A (a circle encloses the maximum area for a given perimeter — isoperimetric inequality), the flux increases to BA'.

Classic JEE trap: students think deforming the wire doesn't change flux since perimeter is unchanged. But Phi = BA, and A changes.

$$\Phi_{initial} = BA \longrightarrow \Phi_{final} = BA' > BA$$

</details>

---

*Next: [Chapter 2 — Faraday's Law of Induction](./02_faradays_law.md)*

---

## Quick Revision Summary

| Concept | Formula | Key Point |
|---|---|---|
| Magnetic Flux | $\Phi = BA\cos\theta$ | theta = angle with **normal** |
| Plane-angle trap | $\Phi = BA\sin\alpha$ | alpha = angle with **plane** |
| Vector flux | $\Phi = \vec{B}\cdot\vec{A}$ | Only perpendicular B component counts |
| N-turn coil | $\Phi = NBA\cos\theta$ | Multiply single-turn flux by N |
| Closed surface | $\oint\vec{B}\cdot d\vec{A} = 0$ | Always zero — no monopoles |
| SI unit | 1 Wb = 1 T.m^2 = 1 V.s | Scalar quantity |
| Rotating coil | $\Phi(t) = BA\cos(\omega t)$ | Sinusoidal variation |
| Non-uniform B | $\Phi = \int B\,dA$ | Integration needed |

> The Golden Rule: Flux depends on B, A, and theta — **never** on resistance, current, or other circuit parameters.

> The Number One Exam Trap: Always check whether the given angle is with the **plane** or with the **normal** before substituting into Phi = BA cos(theta).
