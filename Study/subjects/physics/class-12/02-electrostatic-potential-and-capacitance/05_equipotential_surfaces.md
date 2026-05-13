# Chapter 5: Equipotential Surfaces

> *NCERT Section 2.6*

---

### The Story of the Contour Map

Every hiker knows how to read a topographic map. The map is covered with thin, curved lines — **contour lines** — each representing a constant altitude. Where the lines are close together, the terrain is steep. Where they are far apart, the slope is gentle. A hiker walking *along* a contour line neither climbs nor descends — they traverse the hillside at constant height. But the moment they step *across* a contour line, they gain or lose altitude.

The electric potential creates an identical landscape, except in three dimensions. And the "contour surfaces" of this landscape are called **equipotential surfaces**.

An equipotential surface is a surface on which the electric potential has the same value at every point. Just as a hiker does no work against gravity when walking along a contour line, **no work is done in moving a charge along an equipotential surface.**

This is not a minor convenience — it is a *defining property* of conservative forces, and it gives us a powerful geometric tool for understanding electric fields.

---

### Building the Concept

#### Property 1: No Work Along an Equipotential Surface

If a charge $q$ moves from point A to point B on the same equipotential surface, then $V_A = V_B$, and:

$$W = q(V_B - V_A) = q \times 0 = 0$$

No work is done. This is true regardless of the path taken — as long as you stay on the surface.

#### Property 2: Electric Field Lines Are Perpendicular to Equipotential Surfaces

This follows from Property 1. If the field had any component *along* the surface, it would do work on a charge moving in that direction. But we just established that no work is done along the surface. Therefore, the field must be entirely *perpendicular* to the surface.

> This is the most exam-relevant property. Memorize it as a geometric fact: **$\vec{E}$ is always $\perp$ to equipotential surfaces.**

#### Property 3: Equipotential Surfaces Never Intersect

If two equipotential surfaces (say, $V = 100$ V and $V = 200$ V) intersected at a point P, then P would simultaneously have two different potentials. This is physically impossible — potential is single-valued. Therefore, equipotential surfaces *cannot* cross.

#### Property 4: Closer Surfaces Mean Stronger Fields

The spacing between equipotential surfaces tells you the magnitude of the field. Just like closely spaced contour lines mean a steep slope, closely spaced equipotential surfaces mean a strong electric field:

$$E \approx \frac{\Delta V}{\Delta r}$$

where $\Delta r$ is the perpendicular distance between neighboring surfaces.

---

### The Shapes of Equipotential Surfaces

| Source | Equipotential Surface Shape | Electric Field Lines |
|--------|:---------------------------:|:-------------------:|
| **Point charge** | Concentric spheres centered on the charge | Radial lines pointing outward (+) or inward (−) |
| **Uniform field** | Parallel planes perpendicular to the field | Straight parallel lines |
| **Electric dipole** | Complex, elongated shapes | Curved lines from + to − |
| **Two equal positive charges** | Complex, with a saddle point between them | Curved lines diverging from each charge |

> **For a point charge:** Each sphere has $V = kQ/r$. Larger spheres (larger $r$) have smaller $V$. The spheres are close together near the charge (strong field) and far apart at large distances (weak field).

> **For a uniform field:** All equipotential surfaces are flat planes. The potential drops linearly with distance: $V = V_0 - Ed$. This is exactly the setup between parallel plate capacitors.

---

### Checkpoint 1: Conceptual Understanding

**Problem 1:** A charge of $+5 \mu C$ is moved from a point where $V = 200$ V to another point where $V = 200$ V, along a curved path of length $50$ cm. How much work is done?

<details><summary><b>Solution</b></summary>

Both points are on the same equipotential surface ($V = 200$ V).

$W = q \Delta V = q(200 - 200) = \textbf{0}$

Zero work, regardless of the path length, curvature, or complexity of the route. The path length (50 cm) is a distractor — it is completely irrelevant.
</details>

**Problem 2:** An electron moves from a region where $V = -100$ V to a region where $V = -100$ V along a straight line. The distance covered is $2$ m. What can you say about the electric field along this line?

<details><summary><b>Solution</b></summary>

Since the potential is the same at both endpoints and along a straight line, the *component* of the electric field along this line is zero: $E_{\parallel} = -\frac{dV}{dx} = 0$.

However, the total electric field could be nonzero — it might have components perpendicular to this line. We can only conclude that **the field has no component along the direction of motion**.
</details>

**Problem 3:** Is it possible for the electric field to be zero at a point where the potential is not zero? Is it possible for the potential to be zero at a point where the field is not zero?

<details><summary><b>Solution</b></summary>

**Yes to both.**

- $E = 0, V \neq 0$: Inside a charged conducting sphere, $E = 0$ everywhere but $V = kQ/R$ (a constant, nonzero value).

- $V = 0, E \neq 0$: On the equatorial line of a dipole, $V = 0$ but the electric field is nonzero (and points antiparallel to $\vec{p}$).

$E = 0$ and $V = 0$ are independent conditions. Neither implies the other.
</details>

---

### Checkpoint 2: The Gauntlet — "The Topographic Map"

*An engineer is given the following equipotential map of a region. The potential values on successive surfaces are: 100 V, 80 V, 60 V, 40 V, 20 V. The surfaces are planar and parallel.*

**Problem 1:** What is the direction of the electric field?

<details><summary><b>Solution</b></summary>

The electric field points from **higher** potential to **lower** potential, perpendicular to the equipotential surfaces.

$\vec{E}$ points from the $100$ V surface towards the $20$ V surface.
</details>

*The distance between the 100 V surface and the 20 V surface is 0.4 m.*

**Problem 2:** What is the magnitude of the electric field in this region?

<details><summary><b>Solution</b></summary>

For a uniform field (implied by equally spaced, parallel, planar surfaces):

$E = \frac{\Delta V}{\Delta d} = \frac{100 - 20}{0.4} = \frac{80}{0.4} = \textbf{200 V/m}$
</details>

*A proton is placed on the 60 V surface.*

**Problem 3:** If the proton is released, in which direction does it move?

<details><summary><b>Solution</b></summary>

A positive charge moves from higher to lower potential. But wait — the proton is at 60 V. It will move towards **lower** potential surfaces (40 V, 20 V).

This is in the same direction as $\vec{E}$.
</details>

**Problem 4:** What is the kinetic energy of the proton when it reaches the 20 V surface?

<details><summary><b>Solution</b></summary>

$KE = q \Delta V = 1.6 \times 10^{-19} \times (60 - 20) = 1.6 \times 10^{-19} \times 40$

$KE = \textbf{6.4 × 10⁻¹⁸ J = 40 eV}$
</details>

**Problem 5:** If the proton is instead moved *along* the 60 V surface from one side to the other (a distance of 1 m), what is the work done?

<details><summary><b>Solution</b></summary>

Motion along an equipotential surface: $\Delta V = 0$.

$W = q \Delta V = \textbf{0}$

Distance is irrelevant. Zero work on an equipotential.
</details>

---

### Checkpoint 3: Drawing Equipotentials

**Problem 1:** The electric field in a region is $\vec{E} = 500 \hat{x}$ V/m (uniform, pointing in the positive x-direction). Describe the equipotential surfaces and find the potential difference between $x = 0$ and $x = 0.2$ m.

<details><summary><b>Solution</b></summary>

For a uniform field in the x-direction, the equipotential surfaces are **planes perpendicular to the x-axis** (i.e., $yz$-planes).

The potential decreases in the direction of $\vec{E}$:

$\Delta V = -E \Delta x = -500 \times 0.2 = -100$ V

If we set $V(x=0) = 0$, then $V(x=0.2) = -100$ V.

$\textbf{Potential difference = 100 V}$ (the point at $x = 0$ is at higher potential).
</details>

**Problem 2:** For a positive point charge, explain why equipotential surfaces are closer together near the charge and farther apart at large distances.

<details><summary><b>Solution</b></summary>

The electric field of a point charge is $E = kQ/r^2$, which is strong near the charge and weak far away.

Since $E = \Delta V / \Delta r$, a strong field means that the same potential difference $\Delta V$ occurs over a smaller distance $\Delta r$. So the equipotential surfaces are **closely packed** near the charge.

Far away, the field is weak, so the same $\Delta V$ requires a larger distance. The surfaces are **widely spaced**.

This is exactly like the steep slope near a mountain peak (closely spaced contour lines) versus the gentle plain at the base (widely spaced contour lines).
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** In a certain region, the equipotential surfaces are concentric spheres centered at the origin. The potential on a sphere of radius $0.5$ m is $+360$ V, and on a sphere of radius $1.5$ m is $+120$ V.

(a) Determine the charge at the origin.  
(b) Find the electric field at $r = 1.0$ m.  
(c) A charge of $+2 \mu C$ is moved from the surface of the $0.5$ m sphere to the $1.5$ m sphere. How much work is done by the electric field?  
(d) The same charge is then moved from one point on the $1.5$ m sphere to another point diametrically opposite on the same sphere. How much additional work is done?

<details><summary><b>Solution</b></summary>

**(a)** Using $V = kQ/r$:

From the 0.5 m sphere: $360 = \frac{9 \times 10^9 \times Q}{0.5} \implies Q = \frac{360 \times 0.5}{9 \times 10^9} = 2 \times 10^{-8}$ C

From the 1.5 m sphere: $120 = \frac{9 \times 10^9 \times Q}{1.5} \implies Q = \frac{120 \times 1.5}{9 \times 10^9} = 2 \times 10^{-8}$ C ✓

$Q = \textbf{20 nC}$. Both equations give the same charge — consistent, as expected.

**(b)** $E = \frac{kQ}{r^2} = \frac{9 \times 10^9 \times 2 \times 10^{-8}}{1.0^2} = \textbf{180 V/m}$

Alternatively: $E = -\frac{dV}{dr}$. For a point charge, $V = kQ/r$, so $E = kQ/r^2$, which gives the same result.

**(c)** Work done *by the electric field*:

$W_{field} = q(V_{initial} - V_{final}) = 2 \times 10^{-6} \times (360 - 120) = 2 \times 10^{-6} \times 240$

$W_{field} = \textbf{4.8 × 10⁻⁴ J = 0.48 mJ}$

Positive work — the field pushes the positive charge from high to low potential (downhill).

**(d)** Both the starting and ending points are on the same equipotential surface ($V = 120$ V). Therefore:

$W = q(V_{final} - V_{initial}) = q(120 - 120) = \textbf{0}$

Zero work, even though the charge travels a distance of $2 \times 1.5 = 3$ m. The path is along an equipotential surface.
</details>

---

## Question Bank — Chapter 5

### Section A: MCQs (15 Questions)

**Q1.** Work done in moving a charge between two points on an equipotential surface is:

(a) Positive &emsp; (b) Negative &emsp; (c) Zero &emsp; (d) Depends on the path

<details><summary><b>Answer</b></summary>**(c)** $\Delta V = 0$ on an equipotential, so $W = q\Delta V = 0$.</details>

---

**Q2.** Equipotential surfaces of a uniform electric field are:

(a) Concentric spheres &emsp; (b) Concentric cylinders &emsp; (c) Planes parallel to each other and perpendicular to $\vec{E}$ &emsp; (d) Ellipsoidal surfaces

<details><summary><b>Answer</b></summary>**(c)** For a uniform field, all equipotential surfaces are flat planes perpendicular to $\vec{E}$.</details>

---

**Q3.** The electric field line and equipotential surface at any point make an angle of:

(a) $45°$ &emsp; (b) $0°$ &emsp; (c) $90°$ &emsp; (d) $180°$

<details><summary><b>Answer</b></summary>**(c)** $\vec{E}$ is always perpendicular to equipotential surfaces.</details>

---

**Q4.** Can two equipotential surfaces intersect?

(a) Yes, always &emsp; (b) Yes, if they have the same value &emsp; (c) No &emsp; (d) Yes, at right angles only

<details><summary><b>Answer</b></summary>**(c)** If they intersected, a point would have two different potential values — impossible since potential is single-valued.</details>

---

**Q5.** For a point charge $+q$, the equipotential surfaces are:

(a) Parallel planes &emsp; (b) Concentric spheres &emsp; (c) Concentric cylinders &emsp; (d) Ellipsoidal surfaces

<details><summary><b>Answer</b></summary>**(b)** $V = kq/r = $ constant implies $r = $ constant: concentric spheres.</details>

---

**Q6.** If the electric field in a region is zero, the potential in that region is:

(a) Zero &emsp; (b) Non-zero but constant &emsp; (c) Varies linearly &emsp; (d) Zero or constant

<details><summary><b>Answer</b></summary>**(d)** $E = -dV/dr = 0$ means $V = $ constant (which could be zero or nonzero).</details>

---

**Q7.** The spacing between two consecutive equipotential surfaces of equal potential difference is inversely proportional to:

(a) Potential &emsp; (b) Electric field strength &emsp; (c) Charge &emsp; (d) Distance from source

<details><summary><b>Answer</b></summary>**(b)** $E = \Delta V/\Delta r$, so $\Delta r = \Delta V/E$. For fixed $\Delta V$, spacing $\propto 1/E$.</details>

---

**Q8.** A proton is moved from a point at potential $100$ V to a point at potential $-100$ V. The change in potential energy is:

(a) $+3.2\times10^{-17}$ J &emsp; (b) $-3.2\times10^{-17}$ J &emsp; (c) $+1.6\times10^{-17}$ J &emsp; (d) $-1.6\times10^{-17}$ J

<details><summary><b>Answer</b></summary>**(b)** $\Delta U = q\Delta V = 1.6\times10^{-19}\times(-100-100) = 1.6\times10^{-19}\times(-200) = -3.2\times10^{-17}$ J.</details>

---

**Q9.** At which location is the electric field strongest if the following equipotential surfaces are present: $100V$, $80V$, $60V$, $40V$ at distances $1cm$, $2cm$, $4cm$, $8cm$ from the source?

(a) Between 100V and 80V &emsp; (b) Between 80V and 60V &emsp; (c) Between 60V and 40V &emsp; (d) All have equal field

<details><summary><b>Answer</b></summary>**(a)** Same $\Delta V = 20V$ but smallest gap (1 cm): $E = 20/0.01 = 2000$ V/m (largest).</details>

---

**Q10.** An equipotential surface is described by $x + 2y + 3z = 12$. The electric field is:

(a) Along the x-axis &emsp; (b) Perpendicular to the plane &emsp; (c) Along the y-axis &emsp; (d) In the x-y plane

<details><summary><b>Answer</b></summary>**(b)** The field is always perpendicular to equipotential surfaces, so it's perpendicular to the plane $x+2y+3z=12$, i.e., along the direction $(1,2,3)/\sqrt{14}$.</details>

---

**Q11.** A charge $+2\,\mu C$ moves from $V = 50$ V to $V = 200$ V. The work done by the electric field is:

(a) $+0.3$ mJ &emsp; (b) $-0.3$ mJ &emsp; (c) $+0.5$ mJ &emsp; (d) $-0.5$ mJ

<details><summary><b>Answer</b></summary>**(b)** $W_{field} = q(V_i - V_f) = 2\times10^{-6}\times(50-200) = -0.3\times10^{-3}$ J $= -0.3$ mJ.</details>

---

**Q12.** The work done by an external agent in moving a charge $-3\,\mu C$ from $V = -100$ V to $V = +200$ V is:

(a) $+0.9$ mJ &emsp; (b) $-0.9$ mJ &emsp; (c) $+0.3$ mJ &emsp; (d) $-0.3$ mJ

<details><summary><b>Answer</b></summary>**(b)** $W_{ext} = q\Delta V = (-3\times10^{-6})\times(200-(-100)) = -3\times10^{-6}\times300 = -0.9\times10^{-3}$ J $= -0.9$ mJ.</details>

---

**Q13.** The angle between the electric field and an equipotential surface for a conducting sphere is:

(a) $0°$ &emsp; (b) $45°$ &emsp; (c) $90°$ &emsp; (d) $180°$

<details><summary><b>Answer</b></summary>**(c)** The field at a conductor surface is always perpendicular (normal) to the surface, which is also an equipotential.</details>

---

**Q14.** The equipotential surfaces near an electric dipole are:

(a) Spherical &emsp; (b) Planar &emsp; (c) Complex curves (figure-eight like) &emsp; (d) Cylindrical

<details><summary><b>Answer</b></summary>**(c)** Dipole equipotentials are complex, elongated curves — neither spherical nor planar.</details>

---

**Q15.** If equipotential surfaces are drawn at equal potential intervals, a region where they are densely packed indicates:

(a) Zero electric field &emsp; (b) Weak electric field &emsp; (c) Strong electric field &emsp; (d) Changing sign of field

<details><summary><b>Answer</b></summary>**(c)** Closely packed equipotentials $\Rightarrow$ large $dV/dr \Rightarrow$ strong field.</details>

---

### Section B: Short Answer Questions

**Q16.** What is an equipotential surface? State four properties.

<details><summary><b>Answer</b></summary>

**Equipotential surface:** A surface on which the electric potential has the same value at every point.

**Four properties:**
1. No work is done in moving a charge along an equipotential surface.
2. Electric field lines are always perpendicular to equipotential surfaces.
3. Two equipotential surfaces cannot intersect.
4. Closer spacing between equipotential surfaces indicates a stronger electric field.
</details>

---

**Q17.** Explain why the surface of a conductor in electrostatic equilibrium is an equipotential surface.

<details><summary><b>Answer</b></summary>

In electrostatic equilibrium, the electric field inside the conductor is zero. If there were a potential difference along the surface, a component of the field would exist tangentially (since $E_\parallel = -\partial V/\partial l$). This would drive current along the surface — contradicting the assumption of equilibrium. Therefore, no tangential field exists, meaning no potential gradient along the surface. Hence, the entire surface is at the same potential — an equipotential surface.
</details>

---

**Q18.** In a uniform electric field of $1000$ V/m pointing in the $+x$ direction, how far apart are the equipotential surfaces that differ by $50$ V?

<details><summary><b>Answer</b></summary>

$E = \Delta V/\Delta x \Rightarrow \Delta x = \Delta V/E = 50/1000 = \mathbf{0.05\,m = 5\,cm}$

The surfaces are 5 cm apart, and they are planes perpendicular to the x-axis.
</details>

---

**Q19.** An electron moves from potential $V_A = -200$ V to $V_B = +400$ V. Find (a) the work done by the electric field, (b) the change in kinetic energy.

<details><summary><b>Answer</b></summary>

**(a)** $W_{field} = q(V_A - V_B) = (-e)\times(-200-400) = (-1.6\times10^{-19})\times(-600) = +9.6\times10^{-17}$ J

**(b)** By work-energy theorem: $\Delta KE = W_{field} = \mathbf{+9.6\times10^{-17}\,J = 600\,eV}$

The electron gains kinetic energy (field does positive work on the electron since it moves opposite to $\vec{E}$, i.e., from lower to higher potential).
</details>

---

**Q20.** The equipotential surfaces for a system are concentric ellipsoids. What does this tell you about the electric field direction and the charge distribution?

<details><summary><b>Answer</b></summary>

The field lines are perpendicular to concentric ellipsoidal equipotential surfaces, so they point radially outward (or inward) in directions normal to the ellipsoids — not in simple radial directions like a point charge.

This suggests an elongated charge distribution, such as a prolate spheroid (stretched sphere) of charge, or two nearby equal charges. The field is not spherically symmetric but has axial symmetry (the same symmetry as the ellipsoids).
</details>

---

**Q21.** Charged parallel plates are separated by $4$ mm with $V = 120$ V across them. Find: (a) the electric field, (b) the spacing between the $10$V-interval equipotential surfaces.

<details><summary><b>Answer</b></summary>

**(a)** $E = V/d = 120/(4\times10^{-3}) = \mathbf{30{,}000\,V/m = 30\,kV/m}$

**(b)** For $\Delta V = 10$ V: $\Delta d = \Delta V/E = 10/30000 = \mathbf{3.33\times10^{-4}\,m = 0.333\,mm}$

There are $120/10 = 12$ equipotential surfaces spaced equally at 0.333 mm apart.
</details>

---

**Q22.** Prove that no work is done in moving a charge along an equipotential surface.

<details><summary><b>Answer</b></summary>

Work done by electric field when moving charge $q$ from A to B:

$W = q(V_A - V_B)$

On an equipotential surface, $V_A = V_B$ (by definition).

Therefore: $W = q(V_A - V_A) = q\times 0 = 0$

This result is independent of the path, the charge magnitude, or the distance. **Zero work is always done on an equipotential surface.**
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** In a region, the electric potential is given by $V = 5x^2 + 3y$. A charge $q = 2\,\mu C$ moves from $(0,0)$ to $(2, 4)$. Find: (a) $\vec{E}$ at the initial and final points, (b) work done by the external agent.

<details><summary><b>Answer</b></summary>

**(a)** $E_x = -\partial V/\partial x = -10x$, $E_y = -\partial V/\partial y = -3$

At $(0,0)$: $\vec{E} = -3\hat{y}$ V/m

At $(2,4)$: $\vec{E} = -20\hat{x} - 3\hat{y}$ V/m; $|E| = \sqrt{400+9} = \sqrt{409} \approx 20.2$ V/m

**(b)** $V(0,0) = 0$; $V(2,4) = 5(4)+3(4) = 20+12 = 32$ V

$W_{ext} = q(V_f-V_i) = 2\times10^{-6}\times(32-0) = \mathbf{6.4\times10^{-5}\,J = 64\,\mu J}$
</details>

---

**Q24.** Draw and describe the equipotential surfaces for: (a) two equal positive charges, (b) one positive and one negative charge of equal magnitude.

<details><summary><b>Answer</b></summary>

**(a) Two equal positive charges:** Near each charge, equipotentials are nearly spherical centered on that charge. Between the charges, they bulge toward the midpoint but never touch (saddle point). At large distances, they become nearly spherical centered on the pair's center of mass. The midpoint between the charges is a saddle point where the potential is a local minimum (relative to the axis) and a maximum (perpendicular to the axis).

**(b) Equal and opposite charges (dipole):** The equipotential $V = 0$ is the perpendicular bisector plane. For $V > 0$, closed surfaces surround the positive charge. For $V < 0$, closed surfaces surround the negative charge. All equipotentials are symmetric about the dipole axis. The field lines go from $+q$ to $-q$, always crossing the equipotential surfaces at right angles.
</details>

---

**Q25.** A region has the potential $V = 100 - 25r^2$ V, where $r$ is in meters. Find: (a) the electric field, (b) the radius of the equipotential surface at $V = 75$ V, (c) is the field directed inward or outward?

<details><summary><b>Answer</b></summary>

**(a)** $E = -dV/dr = -(-50r) = 50r$ V/m (magnitude), pointing radially outward.

**(b)** $75 = 100 - 25r^2 \Rightarrow 25r^2 = 25 \Rightarrow r = 1$ m

**(c)** Since $E = 50r > 0$ and we chose the positive sign for outward, the field points **outward**. But let's verify: as $r$ increases, $V$ decreases ($V = 100-25r^2$ is a decreasing function). Field points from high to low potential = outward. ✓
</details>

---

**Q26.** An electric field $\vec{E} = (3\hat{x} + 4\hat{y})$ V/m exists in a region. A charge of $5\,\mu C$ is moved from $(0, 0)$ to $(1, 2)$ m. Find: (a) the potential difference, (b) the work done by the field.

<details><summary><b>Answer</b></summary>

**(a)** $V_A - V_B = \int_A^B \vec{E}\cdot d\vec{l} = \vec{E}\cdot(\vec{r}_A - \vec{r}_B)$ (for uniform field)

$\vec{r}_A - \vec{r}_B = (0-1)\hat{x} + (0-2)\hat{y} = -\hat{x} - 2\hat{y}$

$V_A - V_B = (3\hat{x}+4\hat{y})\cdot(-\hat{x}-2\hat{y}) = -3-8 = -11$ V

So $V_B - V_A = +11$ V (the final point is at higher potential).

**(b)** $W_{field} = q(V_A-V_B) = 5\times10^{-6}\times(-11) = \mathbf{-55\times10^{-6}\,J = -55\,\mu J}$

The field does negative work (the charge moved uphill against the field).
</details>

---

**Q27–Q32:** Equipotential analysis problems.

**Q27.** Two large parallel plates have potentials $+500$ V and $-500$ V separated by $10$ cm. Sketch the equipotential surfaces at $400V$, $200V$, $0V$, $-200V$, $-400V$ and find the spacing between consecutive ones.

<details><summary><b>Answer</b></summary>

The field is uniform: $E = 1000/0.10 = 10000$ V/m.

Spacing between consecutive surfaces (200 V apart): $\Delta d = 200/10000 = 0.02$ m $= 2$ cm.

The surfaces are equally spaced planes: at $0.8$ cm, $2.8$ cm, $5$ cm (center), $7.2$ cm, $9.2$ cm from the $+500$ V plate.
</details>

---

**Q28.** Can the electric field be zero at a point where the potential is changing? Explain with an example.

<details><summary><b>Answer</b></summary>

**No.** If the potential is changing at a point, its gradient is nonzero: $\nabla V \neq 0$. Since $\vec{E} = -\nabla V$, this means $\vec{E} \neq 0$.

If the potential is constant (not changing) in some direction, then the field component in that direction is zero. But if the potential is changing in any direction, there must be a nonzero field component in that direction.

**Contrast with:** Can the potential be zero where the field is nonzero? YES (dipole equatorial plane). But the reverse is not true.
</details>

---

**Q29.** The potential at points A, B, C on an equipotential surface are all 300 V. A charge $+q$ is moved from A to B (path length 5 cm) and then from B to C (path length 12 cm). Find the total work done.

<details><summary><b>Answer</b></summary>

All points A, B, C are on the same equipotential ($V = 300$ V). Path length is irrelevant.

$W_{A\to B} = q(V_B - V_A) = 0$

$W_{B\to C} = q(V_C - V_B) = 0$

$W_{total} = \mathbf{0}$

Zero work regardless of path lengths (5 cm + 12 cm = 17 cm total is irrelevant).
</details>

---

**Q30.** The potential in a region is $V = kx + my + nz$ (a linear function). Show that the electric field is uniform and find its magnitude.

<details><summary><b>Answer</b></summary>

$E_x = -\partial V/\partial x = -k$ (constant)

$E_y = -\partial V/\partial y = -m$ (constant)

$E_z = -\partial V/\partial z = -n$ (constant)

Since all components are constants (independent of position), the field is **uniform**.

$|\vec{E}| = \sqrt{k^2+m^2+n^2}$

The equipotential surfaces are planes $kx+my+nz = $ constant, all perpendicular to $\vec{E}$.
</details>

---

**Q31.** Between two concentric spheres of radii $R_1 = 5$ cm and $R_2 = 10$ cm, the potential varies as $V = A/r$. If $V(R_1) = 1000$ V, find: (a) A, (b) $V(R_2)$, (c) the equipotential surface where $V = 600$ V.

<details><summary><b>Answer</b></summary>

**(a)** $1000 = A/R_1 = A/0.05 \Rightarrow A = 50$ V·m

**(b)** $V(R_2) = A/R_2 = 50/0.10 = \mathbf{500\,V}$

**(c)** $600 = 50/r \Rightarrow r = 50/600 = 0.0833$ m $= \mathbf{8.33\,cm}$

The 600 V equipotential is a sphere of radius 8.33 cm.
</details>

---

**Q32.** Prove that the surface of a conductor in electrostatic equilibrium is always an equipotential, and that the field inside is zero.

<details><summary><b>Answer</b></summary>

**Field inside is zero:** In a conductor, free electrons move in response to any electric field. If an internal field $\vec{E} \neq 0$ existed, electrons would accelerate, creating a current. This current redistributes charges until the internal field is exactly cancelled. In static equilibrium (no current), $\vec{E}_{inside} = 0$.

**Surface is equipotential:** Since $\vec{E}_{inside} = 0$, there is no potential gradient inside: $V = $ constant throughout. On the surface, the field is purely normal (perpendicular) — any tangential component would drive surface current. So $E_{tangential} = -\partial V/\partial l = 0$, meaning $V$ is constant along the surface. The surface (and interior) form a single equipotential.
</details>

---

*Next: [Chapter 6 — Relation Between Field and Potential →](./06_field_and_potential.md)*
