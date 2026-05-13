# Chapter 3: Potential Due to an Electric Dipole

> *NCERT Section 2.4*

---

### The Paradox of the Vanishing Charge

Here is a strange thought experiment. Place a $+q$ charge and a $-q$ charge infinitely far apart. The potential at any point in between is the sum of their individual potentials. As you bring them closer together — maintaining their charges — something remarkable happens: from very far away, the two charges begin to *cancel each other out*. A distant observer sees a system with zero total charge.

And yet, this system is not nothing. It creates a distinct, measurable electric field. It has a characteristic potential that falls off differently from a single charge. It rotates in an external field. It is, in every meaningful way, a new kind of electrical object.

This object is the **electric dipole** — and its potential is one of the most elegant results in all of electrostatics.

---

### Building the Concept: The Dipole Potential

An electric dipole consists of two equal and opposite charges, $+q$ and $-q$, separated by a small distance $2a$. The **dipole moment** is defined as:

$$\vec{p} = q \times 2a \quad (\text{directed from } -q \text{ to } +q)$$

We want the potential $V$ at an arbitrary point P, located at distance $r$ from the center of the dipole, at an angle $\theta$ from the dipole axis.

#### The Geometry

Let the distances from P to the charges be $r_1$ (to $+q$) and $r_2$ (to $-q$). By the superposition principle:

$$V = \frac{1}{4\pi\epsilon_0}\left(\frac{q}{r_1} + \frac{-q}{r_2}\right) = \frac{q}{4\pi\epsilon_0}\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = \frac{q}{4\pi\epsilon_0}\left(\frac{r_2 - r_1}{r_1 r_2}\right)$$

Now, if P is far away ($r \gg a$), we can use geometry to approximate:
- $r_2 - r_1 \approx 2a\cos\theta$
- $r_1 r_2 \approx r^2$

Substituting:

$$V \approx \frac{q \times 2a\cos\theta}{4\pi\epsilon_0 \, r^2} = \frac{p\cos\theta}{4\pi\epsilon_0 \, r^2}$$

$$\boxed{V_{\text{dipole}} = \frac{1}{4\pi\epsilon_0} \frac{p\cos\theta}{r^2}}$$

This is the potential due to an electric dipole at a far point.

#### The Three Special Cases

| Position | Angle $\theta$ | Potential $V$ | Physical Meaning |
|----------|:---------:|:--------:|------------------|
| **Axial** (along dipole axis) | $0°$ or $180°$ | $\pm\frac{p}{4\pi\epsilon_0 r^2}$ | Maximum potential (positive near $+q$, negative near $-q$) |
| **Equatorial** (perpendicular bisector) | $90°$ | $0$ | The $+q$ and $-q$ contributions exactly cancel |
| **General** | $\theta$ | $\frac{p\cos\theta}{4\pi\epsilon_0 r^2}$ | Depends on the projection of $\vec{p}$ onto $\hat{r}$ |

> **Critical Insight:** The dipole potential falls as $1/r^2$, unlike the monopole potential which falls as $1/r$. This means the dipole's influence weakens *much* faster with distance. At twice the distance, a monopole's potential halves, but a dipole's potential drops to one-quarter. From afar, a dipole is practically invisible compared to a single charge.

> **Why the equatorial potential is zero:** On the perpendicular bisector, any point is equidistant from both charges. The positive potential from $+q$ and the negative potential from $-q$ are equal in magnitude and opposite in sign. They annihilate perfectly.

---

### Checkpoint 1: Axial and Equatorial Potentials

**The Molecular Antenna:** A water molecule ($H_2O$) has a permanent dipole moment of $6.2 \times 10^{-30}$ C·m. A physicist is probing the electric potential created by this molecule.

**Problem 1:** Calculate the potential at a point on the axial line, $1 \times 10^{-9}$ m (1 nm) from the center of the molecule.

<details><summary><b>Solution</b></summary>

On the axis, $\theta = 0°$, so $\cos\theta = 1$.

$V = \frac{1}{4\pi\epsilon_0} \frac{p}{r^2} = \frac{9 \times 10^9 \times 6.2 \times 10^{-30}}{(10^{-9})^2}$

$V = \frac{9 \times 6.2 \times 10^{-21}}{10^{-18}} = \frac{55.8 \times 10^{-21}}{10^{-18}}$

$V = \textbf{0.0558 V ≈ 55.8 mV}$

At 1 nm from a single water molecule, the potential is about 56 millivolts — small but very much measurable.
</details>

**Problem 2:** What is the potential at the same distance, but on the equatorial line?

<details><summary><b>Solution</b></summary>

On the equatorial line, $\theta = 90°$, so $\cos 90° = 0$.

$V = \frac{1}{4\pi\epsilon_0} \frac{p \cos 90°}{r^2} = \textbf{0}$

The potential is exactly zero on the equatorial plane. This doesn't mean there's no electric field there — the equatorial field is very much nonzero. It just means the potential contributions from $+q$ and $-q$ cancel at every equatorial point.
</details>

**Problem 3:** At what angle $\theta$ does the potential drop to half its axial value (at the same $r$)?

<details><summary><b>Solution</b></summary>

$V(\theta) = V_{axial} \times \cos\theta$

$\frac{1}{2} V_{axial} = V_{axial} \cos\theta$

$\cos\theta = \frac{1}{2} \implies \theta = \textbf{60°}$
</details>

---

### Checkpoint 2: The Gauntlet — "The Dipole in the Lab"

*A researcher creates an artificial dipole using two charges: $+5$ nC and $-5$ nC, separated by $2$ mm. She measures the potential at various points.*

**Problem 1:** Calculate the dipole moment $p$.

<details><summary><b>Solution</b></summary>

$p = q \times 2a = 5 \times 10^{-9} \times 2 \times 10^{-3} = \textbf{1 × 10⁻¹¹ C·m}$
</details>

*She places a detector on the axial line, 10 cm from the center.*

**Problem 2:** What potential does the detector read? Verify that $r \gg a$ holds.

<details><summary><b>Solution</b></summary>

Check: $r = 0.1$ m, $a = 0.001$ m. $r/a = 100 \gg 1$. ✓ The far-field approximation is excellent.

$V = \frac{kp}{r^2} = \frac{9 \times 10^9 \times 10^{-11}}{(0.1)^2} = \frac{9 \times 10^{-2}}{10^{-2}} = \textbf{9 V}$
</details>

*She moves the detector to 20 cm on the axis.*

**Problem 3:** What is the new potential reading? By what factor did the potential change?

<details><summary><b>Solution</b></summary>

$V = \frac{kp}{r^2} = \frac{9 \times 10^9 \times 10^{-11}}{(0.2)^2} = \frac{9 \times 10^{-2}}{4 \times 10^{-2}} = \textbf{2.25 V}$

Factor of change: $9/2.25 = \textbf{4}$. Doubling the distance reduced the potential by a factor of 4. This confirms the $V \propto 1/r^2$ dependence.
</details>

*The detector is now placed at 10 cm from the center, but at $\theta = 45°$ from the axis.*

**Problem 4:** What does the detector read now?

<details><summary><b>Solution</b></summary>

$V = \frac{kp\cos\theta}{r^2} = 9 \times \cos 45° = 9 \times \frac{1}{\sqrt{2}} = 9 \times 0.707$

$V = \textbf{6.36 V}$
</details>

---

### Dipole vs. Monopole: A Comparison

| Property | Point Charge (Monopole) | Dipole |
|----------|:-----------------------:|:------:|
| Total charge | $Q$ | $0$ |
| Potential formula | $V = \frac{kQ}{r}$ | $V = \frac{kp\cos\theta}{r^2}$ |
| Distance dependence | $1/r$ | $1/r^2$ |
| Angular dependence | None (spherically symmetric) | $\cos\theta$ (axial symmetry) |
| Equipotential surfaces | Spheres | Complex shapes |
| Zero-potential surface | At infinity only | Equatorial plane |

> This table is not just trivia — it is a JEE favorite. Questions that ask you to compare the fall-off of monopole vs. dipole potentials are extremely common.

---

### The Culmination: Synthesis

**Synthesis Problem:** An electric dipole of moment $p = 4 \times 10^{-9}$ C·m is oriented along the x-axis.

(a) Find the potential at the point $(0.3, 0)$ m (on the axis).  
(b) Find the potential at the point $(0, 0.3)$ m (on the equatorial line).  
(c) Find the potential at the point $(0.3, 0.3)$ m.  
(d) A $+2 \mu C$ charge is brought from infinity to the equatorial point in (b). How much work is done?

<details><summary><b>Solution</b></summary>

**(a)** On the axis ($\theta = 0°$):

$V = \frac{kp}{r^2} = \frac{9 \times 10^9 \times 4 \times 10^{-9}}{(0.3)^2} = \frac{36}{0.09} = \textbf{400 V}$

**(b)** On the equatorial line ($\theta = 90°$):

$V = \frac{kp\cos 90°}{r^2} = \textbf{0}$

**(c)** At $(0.3, 0.3)$:

$r = \sqrt{0.3^2 + 0.3^2} = 0.3\sqrt{2}$ m

$\cos\theta = \frac{x}{r} = \frac{0.3}{0.3\sqrt{2}} = \frac{1}{\sqrt{2}}$

$V = \frac{kp\cos\theta}{r^2} = \frac{9 \times 10^9 \times 4 \times 10^{-9} \times (1/\sqrt{2})}{(0.3\sqrt{2})^2}$

$V = \frac{36 \times 0.707}{0.18} = \frac{25.45}{0.18} = \textbf{141.4 V}$

**(d)** Work done to bring $q = +2\mu C$ from infinity (where $V = 0$) to the equatorial point (where $V = 0$):

$W = q(V_{final} - V_{initial}) = 2 \times 10^{-6} \times (0 - 0) = \textbf{0}$

No work is needed! Despite the electric field being nonzero along the equatorial line, the net work done in bringing a charge from infinity to any equatorial point is always zero, because the potential is zero everywhere on that plane.
</details>

---

## Question Bank — Chapter 3

### Section A: Multiple Choice Questions (MCQ)

**Q1.** The electric potential due to a dipole at a point on its axial line at distance $r$ is proportional to:

(a) $1/r$ &emsp; (b) $1/r^2$ &emsp; (c) $1/r^3$ &emsp; (d) $r^2$

<details><summary><b>Answer</b></summary>

**(b)** $V_{axial} = kp/r^2 \propto 1/r^2$
</details>

---

**Q2.** The electric potential at a point on the equatorial line of a dipole is:

(a) Maximum &emsp; (b) Minimum &emsp; (c) Zero &emsp; (d) $kp/r^2$

<details><summary><b>Answer</b></summary>

**(c)** On the equatorial line, $\theta = 90°$, so $V = kp\cos90°/r^2 = 0$
</details>

---

**Q3.** An electric dipole has dipole moment $\vec{p}$. The potential $V$ at a point making angle $\theta$ with the dipole axis at distance $r$ is:

(a) $\frac{kp\sin\theta}{r^2}$ &emsp; (b) $\frac{kp\cos\theta}{r^2}$ &emsp; (c) $\frac{kp\cos\theta}{r}$ &emsp; (d) $\frac{kp\sin\theta}{r}$

<details><summary><b>Answer</b></summary>

**(b)** $V = \frac{kp\cos\theta}{r^2}$
</details>

---

**Q4.** The unit of electric dipole moment is:

(a) C &emsp; (b) C·m &emsp; (c) C/m &emsp; (d) C·m²

<details><summary><b>Answer</b></summary>

**(b)** Dipole moment $p = q \times 2a$ has units of C·m (Coulomb-metre)
</details>

---

**Q5.** The potential at a distance $r$ from the center of a dipole, at an angle $\theta$, is doubled. If $r$ is kept constant, the new angle must be such that:

(a) $\cos\theta$ doubles &emsp; (b) $\sin\theta$ doubles &emsp; (c) $\theta$ doubles &emsp; (d) $\cos\theta$ remains the same

<details><summary><b>Answer</b></summary>

**(a)** Since $V = kp\cos\theta/r^2$, doubling $V$ with constant $r$ requires $\cos\theta$ to double.
</details>

---

**Q6.** For which of the following does a dipole NOT create any potential?

(a) Axial points &emsp; (b) Points on the perpendicular bisector &emsp; (c) Points at $\theta = 45°$ &emsp; (d) Points at $\theta = 30°$

<details><summary><b>Answer</b></summary>

**(b)** On the perpendicular bisector (equatorial line), $\theta = 90°$ and $V = 0$.
</details>

---

**Q7.** A dipole of moment $p$ is placed at the origin. The potential at $(0, r, 0)$ (if the dipole points along the x-axis) is:

(a) $kp/r^2$ &emsp; (b) Zero &emsp; (c) $kp/r$ &emsp; (d) $kp\sqrt{2}/r^2$

<details><summary><b>Answer</b></summary>

**(b)** The point $(0, r, 0)$ is on the equatorial line (perpendicular to dipole axis x). So $\theta = 90°$, $V = 0$.
</details>

---

**Q8.** Dipole potential falls with distance as:

(a) $1/r$ &emsp; (b) $1/r^2$ &emsp; (c) $1/r^3$ &emsp; (d) $1/r^4$

<details><summary><b>Answer</b></summary>

**(b)** $V_{dipole} \propto 1/r^2$ (compared to $1/r$ for a monopole and $1/r^3$ for a quadrupole)
</details>

---

**Q9.** Two charges $+3$ nC and $-3$ nC are $4$ cm apart. The dipole moment is:

(a) $12\times10^{-11}$ C·m &emsp; (b) $1.2\times10^{-10}$ C·m &emsp; (c) $6\times10^{-11}$ C·m &emsp; (d) Both (a) and (b)

<details><summary><b>Answer</b></summary>

**(d)** $p = q\times 2a = 3\times10^{-9}\times0.04 = 1.2\times10^{-10}$ C·m $= 12\times10^{-11}$ C·m. Both (a) and (b) are the same.
</details>

---

**Q10.** The potential at a point midway between the two charges of a dipole is:

(a) $kp/r^2$ &emsp; (b) $kq/a$ &emsp; (c) $0$ &emsp; (d) $-kq/a$

<details><summary><b>Answer</b></summary>

**(c)** At the midpoint, both charges are equidistant. $V = k(+q)/a + k(-q)/a = 0$
</details>

---

**Q11.** The angle between $\vec{p}$ and $\vec{E}$ at a point on the axial line of a dipole is:

(a) $0°$ or $180°$ &emsp; (b) $90°$ &emsp; (c) $45°$ &emsp; (d) $60°$

<details><summary><b>Answer</b></summary>

**(a)** On the axial line, the field is parallel (or antiparallel) to $\vec{p}$, so the angle is $0°$ or $180°$.
</details>

---

**Q12.** At what angle does the dipole potential equal half of its maximum value (for same $r$)?

(a) $30°$ &emsp; (b) $45°$ &emsp; (c) $60°$ &emsp; (d) $90°$

<details><summary><b>Answer</b></summary>

**(c)** Maximum $V = kp/r^2$ (at $\theta = 0°$). Half this: $\cos\theta = 1/2 \Rightarrow \theta = 60°$
</details>

---

**Q13.** The potential due to a dipole at the end-on position (at distance $r$ from center, $r \gg a$) is:

(a) $\frac{kp}{r}$ &emsp; (b) $\frac{kp}{2r^2}$ &emsp; (c) $\frac{kp}{r^2}$ &emsp; (d) $0$

<details><summary><b>Answer</b></summary>

**(c)** End-on position is the axial line ($\theta = 0°$): $V = kp\cos0°/r^2 = kp/r^2$
</details>

---

**Q14.** The electric field on the equatorial line of a dipole points:

(a) Parallel to $\vec{p}$ &emsp; (b) Antiparallel to $\vec{p}$ &emsp; (c) Perpendicular to $\vec{p}$ &emsp; (d) At $45°$ to $\vec{p}$

<details><summary><b>Answer</b></summary>

**(b)** On the equatorial line, the electric field points **antiparallel** to the dipole moment $\vec{p}$.
</details>

---

**Q15.** If the distance from a dipole is tripled, the potential changes by a factor of:

(a) $1/9$ &emsp; (b) $1/3$ &emsp; (c) $9$ &emsp; (d) $3$

<details><summary><b>Answer</b></summary>

**(a)** $V \propto 1/r^2$. Tripling $r$ gives $V' = V/9$.
</details>

---

### Section B: Short Answer Questions

**Q16.** Derive the expression for electric potential at an axial point of an electric dipole, without using the far-field approximation.

<details><summary><b>Answer</b></summary>

Dipole: $+q$ at $+a$ and $-q$ at $-a$ from center. Point P at distance $r$ on axis.

$V = \frac{kq}{r-a} + \frac{k(-q)}{r+a} = kq\left[\frac{1}{r-a} - \frac{1}{r+a}\right] = kq\cdot\frac{2a}{r^2-a^2}$

$$V_{axial} = \frac{1}{4\pi\epsilon_0}\frac{2pr}{r^2-a^2}$$

For $r \gg a$: $V \approx \frac{kp\cdot2r}{r^2} = \frac{2kp}{r} \times \frac{1}{...}$ — wait, let me redo:

$V = kq\cdot\frac{2a}{r^2-a^2}$, and $p = q\cdot2a$, so $V = \frac{kp}{r^2-a^2}$

For $r \gg a$: $V \approx kp/r^2$ ✓
</details>

---

**Q17.** A dipole of moment $p = 2\times10^{-9}$ C·m. Find the potential at:
(a) An axial point $10$ cm from the center
(b) An equatorial point at the same distance

<details><summary><b>Answer</b></summary>

**(a)** $V_{axial} = kp/r^2 = 9\times10^9\times2\times10^{-9}/(0.1)^2 = 18/0.01 = \mathbf{1800\,V}$

**(b)** $V_{equatorial} = kp\cos90°/r^2 = \mathbf{0}$
</details>

---

**Q18.** Two dipoles of moments $p_1 = 3\times10^{-10}$ C·m and $p_2 = 5\times10^{-10}$ C·m are placed at the origin along the x-axis and y-axis respectively. Find the potential at point $(0.2, 0, 0)$.

<details><summary><b>Answer</b></summary>

At $(0.2, 0, 0)$:
- Dipole $p_1$ (along x-axis): the point is on the axial line, $\theta_1 = 0°$
  $V_1 = kp_1\cos0°/r^2 = 9\times10^9\times3\times10^{-10}/(0.04) = 2.7/0.04 = 67.5$ V

- Dipole $p_2$ (along y-axis): the point is on the equatorial line of $p_2$, $\theta_2 = 90°$
  $V_2 = kp_2\cos90°/r^2 = 0$

$V_{total} = 67.5 + 0 = \mathbf{67.5\,V}$
</details>

---

**Q19.** Explain why the dipole potential falls as $1/r^2$ while the monopole potential falls as $1/r$. Connect this to the concept of "cancellation."

<details><summary><b>Answer</b></summary>

A dipole has zero net charge. Its positive and negative contributions to the potential partially cancel each other. The degree of cancellation increases with distance — at large $r$, the two charges appear nearly coincident, and their potentials nearly cancel.

Mathematically: $V = kq(\frac{1}{r_1} - \frac{1}{r_2})$. The difference $\frac{1}{r_1} - \frac{1}{r_2} \approx \frac{r_2 - r_1}{r^2} \approx \frac{2a\cos\theta}{r^2}$, introducing an extra power of $1/r$ compared to a single charge. Hence $V_{dipole} \propto 1/r^2$ instead of $1/r$.

A quadrupole (two dipoles) would cancel even more severely, giving $V \propto 1/r^3$.
</details>

---

**Q20.** The water molecule has a dipole moment of $6.2\times10^{-30}$ C·m. If the two partial charges of the molecule are separated by $1.04\times10^{-10}$ m, find the effective partial charge.

<details><summary><b>Answer</b></summary>

$p = q_{eff} \times d$

$q_{eff} = p/d = \frac{6.2\times10^{-30}}{1.04\times10^{-10}} = 5.96\times10^{-20}$ C

$q_{eff} \approx \mathbf{6\times10^{-20}\,C \approx 0.375\,e}$

This partial charge (about 37.5% of an elementary charge) explains the polar nature of water molecules and their ability to dissolve ionic compounds.
</details>

---

**Q21.** At a point on the axial line, $V = 40$ V and $E = 1000$ V/m. Find the dipole moment and the distance of the point from the dipole.

<details><summary><b>Answer</b></summary>

On the axial line: $V = kp/r^2$ and $E = 2kp/r^3$

Dividing: $\frac{E}{V} = \frac{2kp/r^3}{kp/r^2} = \frac{2}{r}$

$r = 2V/E = 2\times40/1000 = \mathbf{0.08\,m = 8\,cm}$

$p = Vr^2/k = 40\times(0.08)^2/(9\times10^9) = 40\times0.0064/(9\times10^9) = 2.84\times10^{-11}\,\text{C·m}$
</details>

---

**Q22.** Show that the locus of points having equal potential due to a dipole lies on the curve $r^2 = C\cos\theta$ (where $C$ is a constant).

<details><summary><b>Answer</b></summary>

$V = kp\cos\theta/r^2 = $ constant $= V_0$

$\cos\theta/r^2 = V_0/kp = $ constant

$\Rightarrow r^2 = \frac{kp}{V_0}\cos\theta = C\cos\theta$

where $C = kp/V_0$. This is indeed the equation of a "dimpled" closed curve in polar coordinates — it represents the equipotential surfaces of a dipole.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** A short dipole of moment $p = 5\times10^{-8}$ C·m is at the origin, pointing along the x-axis. Find the potential at:
(a) $(0.3, 0, 0)$
(b) $(0, 0.3, 0)$
(c) $(0.3, 0.4, 0)$
(d) Work done to bring $+1\,\mu C$ from infinity to the point in (c)

<details><summary><b>Answer</b></summary>

**(a)** Axial point ($\theta = 0°$): $V = kp/r^2 = 9\times10^9\times5\times10^{-8}/(0.09) = 5000\,V$

**(b)** Equatorial point ($\theta = 90°$): $V = 0$

**(c)** $r = \sqrt{0.09+0.16} = \sqrt{0.25} = 0.5$ m. $\cos\theta = 0.3/0.5 = 0.6$

$V = kp\cos\theta/r^2 = 9\times10^9\times5\times10^{-8}\times0.6/(0.25) = 9\times10^9\times3\times10^{-8}/0.25 = 1080\,V$

**(d)** $W = qV = 1\times10^{-6}\times1080 = \mathbf{1.08\times10^{-3}\,J = 1.08\,mJ}$
</details>

---

**Q24.** Two short dipoles, each of moment $p$, are placed at the origin. One points along $+x$ and the other along $+y$. Find the magnitude and direction of the resultant dipole moment, and find the potential at the point $(r, 0, 0)$.

<details><summary><b>Answer</b></summary>

**Resultant dipole moment:** $\vec{p}_{net} = p\hat{x} + p\hat{y}$

$|\vec{p}_{net}| = p\sqrt{2}$, at $45°$ to the x-axis.

**Potential at $(r, 0, 0)$:**

Due to $p\hat{x}$ (axial point): $V_1 = kp/r^2$

Due to $p\hat{y}$ (equatorial point of the y-dipole): $V_2 = 0$

$V_{total} = kp/r^2$

Alternatively, using the resultant dipole: $\theta = 45°$ between $\vec{p}_{net}$ and the direction to $(r, 0, 0)$.

$V = \frac{k p\sqrt{2}\cos45°}{r^2} = \frac{k p\sqrt{2}\cdot(1/\sqrt{2})}{r^2} = \frac{kp}{r^2}$ ✓
</details>

---

**Q25.** The potential due to a dipole is given by $V = kp\cos\theta/r^2$. Find the two components of the electric field $E_r$ and $E_\theta$ by taking appropriate gradients, and verify that at the axial point, the field equals $2kp/r^3$.

<details><summary><b>Answer</b></summary>

$E_r = -\frac{\partial V}{\partial r} = -kp\cos\theta\times(-2/r^3) = \frac{2kp\cos\theta}{r^3}$

$E_\theta = -\frac{1}{r}\frac{\partial V}{\partial\theta} = -\frac{1}{r}\times kp\times\frac{(-\sin\theta)}{r^2} = \frac{kp\sin\theta}{r^3}$

**At axial point** ($\theta = 0°$):
$E_r = 2kp/r^3$, $E_\theta = 0$

Net field $= 2kp/r^3$ (along $\hat{r}$, i.e., along the axis) ✓

**At equatorial point** ($\theta = 90°$):
$E_r = 0$, $E_\theta = kp/r^3$

Net field $= kp/r^3$ (perpendicular to $\hat{r}$, i.e., antiparallel to $\vec{p}$) ✓
</details>

---

**Q26.** A dipole of moment $p$ is placed at a point $r$ from the center of a large conducting sphere. Qualitatively describe what happens to the equipotential surfaces in the vicinity of the dipole, and how they are modified by the presence of the conductor.

<details><summary><b>Answer</b></summary>

Without conductor: the equipotential surfaces of the dipole are axially symmetric, with zero-potential surface coinciding with the equatorial plane.

With the conducting sphere:
1. The sphere's surface is an equipotential (say $V_0$).
2. The dipole induces surface charges on the sphere, redistributing them to maintain the sphere as an equipotential.
3. The equipotential surfaces near the dipole are distorted — they must smoothly connect to the sphere's constant-potential surface.
4. The effect of the conductor is equivalent to adding an "image dipole" inside the sphere (by the method of images), which modifies all nearby equipotential surfaces.
5. The field inside the conductor remains zero.

This is a classic problem in electrostatics solved by the method of images, showing how conductors reshape the entire potential landscape.
</details>

---

**Q27.** A dipole of $p = 4\times10^{-9}$ C·m is at the origin along the z-axis. Find:
(a) The potential at $(0, 0, 2)$ m
(b) The potential at $(1, 1, 0)$ m
(c) The ratio $V_a/V_b$

<details><summary><b>Answer</b></summary>

**(a)** $(0, 0, 2)$: axial point, $r = 2$ m, $\theta = 0°$

$V_a = kp/r^2 = 9\times10^9\times4\times10^{-9}/4 = 9\,V$

**(b)** $(1, 1, 0)$: $r = \sqrt{2}$ m, angle to z-axis: $\cos\theta = 0$ (the z-component of position is 0)

$V_b = kp\cos90°/r^2 = 0$

**(c)** $V_a/V_b$ is undefined (division by zero). Point (b) is on the equatorial plane of the z-dipole — the potential is exactly zero.
</details>

---

**Q28.** An electric dipole of length $2\,\text{cm}$ has charges $\pm4\,\mu C$ at its ends. It is placed making an angle of $30°$ with a uniform electric field of $3\times10^5$ V/m.

(a) Find the torque acting on it.
(b) Find the potential energy.
(c) What is the work done to rotate it by $60°$ further?

<details><summary><b>Answer</b></summary>

$p = q\times 2a = 4\times10^{-6}\times0.02 = 8\times10^{-8}$ C·m

**(a)** $\tau = pE\sin\theta = 8\times10^{-8}\times3\times10^5\times\sin30° = 24\times10^{-3}\times0.5 = \mathbf{0.012\,N\cdot m}$

**(b)** $U = -pE\cos\theta = -8\times10^{-8}\times3\times10^5\times\cos30° = -24\times10^{-3}\times0.866 = \mathbf{-0.02078\,J}$

**(c)** Rotating by $60°$ further: new angle $= 30° + 60° = 90°$

$W = pE(\cos\theta_1 - \cos\theta_2) = 8\times10^{-8}\times3\times10^5\times(\cos30° - \cos90°)$

$W = 24\times10^{-3}\times(0.866 - 0) = \mathbf{0.02078\,J}$
</details>

---

**Q29.** An HCl molecule has bond length $1.27\,Å$ and dipole moment $3.44\times10^{-30}$ C·m. Find the effective charge on each atom.

<details><summary><b>Answer</b></summary>

$q_{eff} = p/(2a) = \frac{3.44\times10^{-30}}{1.27\times10^{-10}} = 2.71\times10^{-20}$ C

$q_{eff}/e = 2.71\times10^{-20}/(1.6\times10^{-19}) = 0.169$

The effective partial charge is $\approx 0.17e$, meaning about 17% charge transfer between H and Cl. This is the ionic character of the H–Cl bond.
</details>

---

**Q30.** Prove that the potential due to a dipole at any point on its axis, at distance $r$ from center, equals $2V_{eq}$ if both points are at the same distance — but that's trivially zero. Instead: show that $V_{axial}(r) = -2V_{general}(r, 120°)$.

<details><summary><b>Answer</b></summary>

$V_{axial}(r) = kp\cos0°/r^2 = kp/r^2$

$V_{general}(r, 120°) = kp\cos120°/r^2 = kp\times(-1/2)/r^2 = -kp/(2r^2)$

$-2V_{general}(r, 120°) = -2\times(-kp/2r^2) = kp/r^2 = V_{axial}(r)$ ✓

This elegant relation shows that the axial potential can be extracted from the general formula by choosing $\theta = 120°$ and negating twice.
</details>

---

**Q31.** The potential at a distance $r$ from a short dipole varies as $V = A\cos\theta/r^2$. At $r = 0.3$ m and $\theta = 60°$, $V = 100$ V. Find the dipole moment.

<details><summary><b>Answer</b></summary>

$V = kp\cos\theta/r^2$

$100 = kp\cos60°/(0.3)^2 = kp\times0.5/0.09$

$kp = 100\times0.09/0.5 = 18$

$p = 18/(9\times10^9) = 2\times10^{-9}$ C·m $= \mathbf{2\,\text{nC·m}}$
</details>

---

**Q32.** Two charges $+q$ and $-q$ are placed at $(0, 0, a)$ and $(0, 0, -a)$ respectively. A third charge $+Q$ is placed at the origin.

(a) Is the system a dipole? What is its dipole moment?
(b) Find the potential at $(x, 0, 0)$ for large $x$.
(c) What does this tell you about the leading-order behavior of the potential?

<details><summary><b>Answer</b></summary>

**(a)** The system is NOT a pure dipole. The dipole moment: $\vec{p} = q\times\hat{z}\times a + (-q)\times\hat{z}\times(-a) = 2qa\hat{z}$... wait.

Actually: $\vec{p}_{total} = \sum q_i\vec{r}_i = (+q)(0,0,a) + (-q)(0,0,-a) + Q(0,0,0)$

$\vec{p} = qa\hat{z} - q(-a)\hat{z} + 0 = qa\hat{z} + qa\hat{z} = 2qa\hat{z}$

Yes — the $+Q$ charge at the origin doesn't contribute to the dipole moment (it's at $r = 0$). But the total charge is $+Q$, so the leading-order term in the potential is the monopole term $kQ/r$ (not zero).

**(b)** At large $x$ (equatorial to the dipole $\pm q$): $V_{dipole} = kp\cos90°/x^2 = 0$

Total potential: $V \approx kQ/x$ (monopole dominates)

**(c)** When the net charge is nonzero, the potential behaves as $1/r$ (monopole) at large distances, regardless of any multipole structure. The dipole and higher terms are subdominant.
</details>

---

*Next: [Chapter 4 — Potential Due to a System of Charges →](./04_potential_system_of_charges.md)*
