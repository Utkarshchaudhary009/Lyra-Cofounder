# Chapter 2: Potential Due to a Point Charge

> *NCERT Section 2.3*

---

### The Story of the Gravitational Analogy

On Earth, every object creates a gravitational "well" around itself — a landscape where other masses are pulled inward. The deeper you are in the well (closer to the Earth's center), the more energy you'd need to escape. The surface of the Earth is deep in its gravitational well; the International Space Station, orbiting 400 km up, is slightly higher on the wall.

A point charge creates an identical landscape, except the "well" can also be a "hill."

A **positive** charge creates a potential *hill* — other positive charges are pushed away from it (they roll downhill). Approach it, and you climb higher and higher in potential. A **negative** charge creates a potential *well* — positive charges are drawn inward, falling deeper into the valley.

The question is: can we write down the exact mathematical shape of this landscape?

---

### Building the Concept: Deriving the Formula

Consider a point charge $Q$ sitting at the origin. We want to find the potential $V$ at a point P located at distance $r$ from the charge.

By definition, $V(r)$ equals the work done by an external force in bringing a unit positive test charge ($q_0 = +1$ C) from infinity to the point P, without acceleration.

#### The Calculation

The electric field due to $Q$ at a distance $r'$ from it is:

$$E = \frac{1}{4\pi\epsilon_0} \frac{Q}{r'^2}$$

The external force must exactly balance this field at every point along the path (quasi-static process): $F_{ext} = q_0 E = E$ (since $q_0 = 1$).

The work done by this external force in moving the unit charge from infinity to distance $r$:

$$V(r) = -\int_\infty^r E \, dr' = -\int_\infty^r \frac{1}{4\pi\epsilon_0} \frac{Q}{r'^2} \, dr'$$

The negative sign appears because we integrate *inward* (from $\infty$ to $r$), opposite to the direction of increasing $r'$.

$$V(r) = -\frac{Q}{4\pi\epsilon_0} \left[-\frac{1}{r'}\right]_\infty^r = -\frac{Q}{4\pi\epsilon_0} \left(-\frac{1}{r} + \frac{1}{\infty}\right)$$

$$\boxed{V(r) = \frac{1}{4\pi\epsilon_0} \frac{Q}{r}}$$

This is the electrostatic potential at distance $r$ from a point charge $Q$.

#### Key Observations

| Feature | Detail |
|---------|--------|
| **Scalar** | No direction — just a number at every point |
| **Sign** | $V > 0$ for positive $Q$; $V < 0$ for negative $Q$ |
| **Distance dependence** | $V \propto 1/r$ (falls slower than $E \propto 1/r^2$) |
| **At infinity** | $V \to 0$ (our reference point) |
| **At $r = 0$** | $V \to \pm\infty$ (undefined — a singularity) |

> **Critical Comparison:** The electric field $E$ falls as $1/r^2$. The potential $V$ falls as $1/r$. At large distances, the potential is significant even when the field is negligible. This is why high-voltage power lines (high $V$) can still be dangerous even at moderate distances where the field strength seems small.

---

### Checkpoint 1: Direct Application

**The Lightning Rod Scenario:** A metal sphere atop a building accumulates a charge of $+20 \mu C$ during a thunderstorm. A safety inspector needs to map the potential around it to determine safe distances.

**Problem 1:** Calculate the potential at distances of (a) $1$ m, (b) $2$ m, and (c) $10$ m from the center of the sphere. (Treat the sphere as a point charge.)

<details><summary><b>Solution</b></summary>

$V = \frac{1}{4\pi\epsilon_0} \frac{Q}{r} = \frac{9 \times 10^9 \times 20 \times 10^{-6}}{r} = \frac{1.8 \times 10^5}{r}$

(a) At $r = 1$ m: $V = \textbf{1.8 × 10⁵ V = 180 kV}$

(b) At $r = 2$ m: $V = \textbf{9 × 10⁴ V = 90 kV}$

(c) At $r = 10$ m: $V = \textbf{1.8 × 10⁴ V = 18 kV}$

Notice: doubling the distance halves the potential (since $V \propto 1/r$).
</details>

**Problem 2:** At what distance from the sphere is the potential equal to $100$ V?

<details><summary><b>Solution</b></summary>

$100 = \frac{1.8 \times 10^5}{r}$

$r = \frac{1.8 \times 10^5}{100} = \textbf{1800 m = 1.8 km}$

Even 1.8 km away, the potential is still 100 V. This illustrates the slow $1/r$ decay of potential.
</details>

*The inspector now discovers a second charge — a $-10 \mu C$ charge on a nearby metal pole, $5$ m away from the sphere.*

**Problem 3:** What is the potential at the exact midpoint between the two charges?

<details><summary><b>Solution</b></summary>

At the midpoint, the distance from each charge is $r = 2.5$ m.

$V_{total} = V_1 + V_2 = \frac{kQ_1}{r_1} + \frac{kQ_2}{r_2}$

$V_{total} = \frac{9 \times 10^9 \times 20 \times 10^{-6}}{2.5} + \frac{9 \times 10^9 \times (-10 \times 10^{-6})}{2.5}$

$V_{total} = 72000 + (-36000) = \textbf{36,000 V = 36 kV}$

Potential is a scalar — we simply add algebraically. No vector components needed!
</details>

---

### Checkpoint 2: The Inverse Problem

**Problem 1:** The potential at a point $0.5$ m from an unknown charge is $-3.6 \times 10^4$ V. Find the charge.

<details><summary><b>Solution</b></summary>

$V = \frac{kQ}{r} \implies Q = \frac{Vr}{k} = \frac{-3.6 \times 10^4 \times 0.5}{9 \times 10^9}$

$Q = \textbf{-2 × 10⁻⁶ C = -2 μC}$

The negative potential confirms the charge is negative.
</details>

**Problem 2:** Two points A and B are at distances $r$ and $2r$ from a point charge $Q$. If $V_A = 600$ V, what is $V_B$?

<details><summary><b>Solution</b></summary>

Since $V \propto 1/r$:

$\frac{V_B}{V_A} = \frac{r_A}{r_B} = \frac{r}{2r} = \frac{1}{2}$

$V_B = \frac{600}{2} = \textbf{300 V}$
</details>

**Problem 3:** The potential at the surface of a charged metallic sphere of radius $R = 0.1$ m is $V_0 = 900$ V. Find (a) the charge on the sphere, and (b) the potential at a distance $r = 0.3$ m from the center.

<details><summary><b>Solution</b></summary>

(a) At the surface, $r = R$:

$V_0 = \frac{kQ}{R} \implies Q = \frac{V_0 R}{k} = \frac{900 \times 0.1}{9 \times 10^9} = \textbf{1 × 10⁻⁸ C = 10 nC}$

(b) At $r = 0.3$ m:

$V = \frac{kQ}{r} = \frac{9 \times 10^9 \times 10^{-8}}{0.3} = \frac{90}{0.3} = \textbf{300 V}$

Or, using ratios: $V = V_0 \times \frac{R}{r} = 900 \times \frac{0.1}{0.3} = 300$ V.
</details>

---

### Checkpoint 3: Superposition of Potentials — "The Charged Triangle"

*Three charges are arranged at the corners of an equilateral triangle of side $a = 1$ m.*

**Problem 1:** Charges $+2\mu C$, $+2\mu C$, and $+2\mu C$ are placed at corners A, B, C. Find the potential at the centroid of the triangle.

<details><summary><b>Solution</b></summary>

The distance from each corner to the centroid of an equilateral triangle is $r = \frac{a}{\sqrt{3}} = \frac{1}{\sqrt{3}}$ m.

$V = V_A + V_B + V_C = 3 \times \frac{kQ}{r} = 3 \times \frac{9 \times 10^9 \times 2 \times 10^{-6}}{1/\sqrt{3}}$

$V = 3 \times 9 \times 10^9 \times 2 \times 10^{-6} \times \sqrt{3}$

$V = 3 \times 18000 \times 1.732 = 3 \times 31176 = \textbf{93,530 V ≈ 93.5 kV}$
</details>

**Problem 2:** Now change one charge: $+2\mu C$, $+2\mu C$, $-2\mu C$. Find the potential at the centroid.

<details><summary><b>Solution</b></summary>

Since all three charges are at the same distance from the centroid:

$V = \frac{k}{r}(Q_1 + Q_2 + Q_3) = \frac{k}{r}(2 + 2 - 2) \times 10^{-6} = \frac{k}{r} \times 2 \times 10^{-6}$

$V = \frac{9 \times 10^9 \times 2 \times 10^{-6}}{1/\sqrt{3}} = 18000\sqrt{3} \approx \textbf{31,177 V ≈ 31.2 kV}$

One negative charge reduced the potential by two-thirds. This is the power of scalar superposition.
</details>

**Problem 3:** What combination of charges at the three vertices would give $V = 0$ at the centroid?

<details><summary><b>Solution</b></summary>

For $V = 0$ at the centroid, since all distances are equal:

$V = \frac{k}{r}(Q_1 + Q_2 + Q_3) = 0$

$\implies Q_1 + Q_2 + Q_3 = 0$

Any combination where the charges sum to zero works. For example:
- $+q, +q, -2q$
- $+q, -q, 0$
- $+3q, +2q, -5q$

The algebraic sum of charges must vanish.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** A charge $Q_1 = +5 \mu C$ is placed at the origin. A second charge $Q_2 = -3 \mu C$ is placed at $x = 0.4$ m.

(a) Find the point on the x-axis where the electric potential is zero.  
(b) Is the electric field zero at this point? Justify.  
(c) How much work is needed to bring a $+1 \mu C$ charge from infinity to this zero-potential point?

<details><summary><b>Solution</b></summary>

**(a)** Let the zero-potential point be at distance $x$ from $Q_1$ (and therefore at $(0.4 - x)$ from $Q_2$). The potential at this point:

$V = \frac{kQ_1}{x} + \frac{kQ_2}{0.4 - x} = 0$

$\frac{5}{x} + \frac{-3}{0.4 - x} = 0$

$\frac{5}{x} = \frac{3}{0.4 - x}$

$5(0.4 - x) = 3x$

$2 - 5x = 3x \implies 8x = 2 \implies x = 0.25$ m

There is also a zero-potential point *outside* the charges (beyond $Q_2$). Let this point be at distance $d$ from $Q_1$ where $d > 0.4$:

$\frac{5}{d} + \frac{-3}{d - 0.4} = 0 \implies 5(d - 0.4) = 3d \implies 2d = 2 \implies d = 1$ m

$\textbf{Zero-potential points: x = 0.25 m and x = 1.0 m}$

**(b)** The electric field is **NOT** zero at these points. $V = 0$ means the potential *energy* of a test charge is zero there — it doesn't mean there's no force. At $x = 0.25$ m, both $E_1$ and $E_2$ point in the same direction (both towards the negative charge or away from the positive), so the net field is nonzero.

In general, $V = 0$ does **not** imply $E = 0$, and $E = 0$ does **not** imply $V = 0$.

**(c)** Work done = $q \times V_{final} - q \times V_{initial} = q \times 0 - q \times 0 = \textbf{0}$

Since the initial potential (at infinity) is 0, and the final potential (at the zero-potential point) is also 0, no net work is required! The charge arrives with zero potential energy — though it may have been "climbing" and "descending" hills along the way, the net energy change is zero.
</details>

---

## Question Bank — Chapter 2

### Section A: Multiple Choice Questions (MCQ)

**Q1.** The electric potential at a distance $r$ from a point charge $Q$ is proportional to:

(a) $r$ &emsp; (b) $r^2$ &emsp; (c) $1/r$ &emsp; (d) $1/r^2$

<details><summary><b>Answer</b></summary>

**(c)** $V = kQ/r \propto 1/r$
</details>

---

**Q2.** The potential at the surface of a conducting sphere of radius $R$ carrying charge $Q$ is:

(a) $kQ/R^2$ &emsp; (b) $kQ/R$ &emsp; (c) $kQ\cdot R$ &emsp; (d) Zero

<details><summary><b>Answer</b></summary>

**(b)** $V_{surface} = kQ/R$ (the sphere behaves like a point charge at its surface)
</details>

---

**Q3.** Two charges $+Q$ and $+4Q$ are separated by $3$ m. Where is the potential zero on the line joining them?

(a) $1$ m from $+Q$ &emsp; (b) Between them, $2$ m from $+Q$ &emsp; (c) Nowhere &emsp; (d) $1$ m from $+4Q$

<details><summary><b>Answer</b></summary>

**(c)** For two charges of the same sign, potential is always positive everywhere. Zero potential is impossible.
</details>

---

**Q4.** The electric potential inside a conducting sphere (at any internal point) is:

(a) Zero &emsp; (b) Equal to its surface potential &emsp; (c) Less than surface potential &emsp; (d) Infinite

<details><summary><b>Answer</b></summary>

**(b)** The potential is constant throughout the conductor (inside and on the surface), equal to the surface value $V = kQ/R$.
</details>

---

**Q5.** A charge $+Q$ is at the origin. The ratio $V(r)/V(2r)$ is:

(a) $1$ &emsp; (b) $2$ &emsp; (c) $4$ &emsp; (d) $1/2$

<details><summary><b>Answer</b></summary>

**(b)** $V \propto 1/r$, so $V(r)/V(2r) = 2r/r = 2$
</details>

---

**Q6.** The potential at the midpoint between a charge $+Q$ and $-Q$ separated by distance $2d$ is:

(a) $kQ/d$ &emsp; (b) $-kQ/d$ &emsp; (c) $2kQ/d$ &emsp; (d) $0$

<details><summary><b>Answer</b></summary>

**(d)** At the midpoint, distance from each charge is $d$. $V = kQ/d + k(-Q)/d = 0$
</details>

---

**Q7.** If the potential at a point due to a charge $Q$ is $V$, the potential at a distance doubled from the same charge is:

(a) $V/4$ &emsp; (b) $V/2$ &emsp; (c) $2V$ &emsp; (d) $4V$

<details><summary><b>Answer</b></summary>

**(b)** $V \propto 1/r$. Doubling $r$ halves $V$. New potential $= V/2$.
</details>

---

**Q8.** The unit of $\frac{1}{4\pi\epsilon_0}$ is:

(a) N·m²/C² &emsp; (b) C²/N·m² &emsp; (c) N/C &emsp; (d) V/m

<details><summary><b>Answer</b></summary>

**(a)** $k = 1/(4\pi\epsilon_0) = 9\times10^9$ N·m²/C²
</details>

---

**Q9.** Two point charges $+3\,\mu C$ and $-3\,\mu C$ are placed $4$ m apart. The potential at the midpoint is:

(a) $27\,\text{kV}$ &emsp; (b) $-27\,\text{kV}$ &emsp; (c) $0$ &emsp; (d) $13.5\,\text{kV}$

<details><summary><b>Answer</b></summary>

**(c)** At the midpoint ($r = 2$ m from each): $V = k(3\times10^{-6})/2 + k(-3\times10^{-6})/2 = 0$
</details>

---

**Q10.** The potential difference between two points in an electric field is independent of:

(a) The magnitude of the test charge &emsp; (b) The source charge &emsp; (c) The positions of the two points &emsp; (d) The sign of the test charge

<details><summary><b>Answer</b></summary>

**(a)** Potential difference is a property of the field (source), not the test charge. It is the same regardless of the test charge's magnitude or sign.
</details>

---

**Q11.** A metallic sphere has charge $+Q$ and radius $R$. The potential at a point $r = 2R$ from the center is:

(a) $kQ/(2R)$ &emsp; (b) $kQ/R$ &emsp; (c) $kQ/(4R)$ &emsp; (d) $2kQ/R$

<details><summary><b>Answer</b></summary>

**(a)** Outside the sphere, $V = kQ/r = kQ/(2R)$
</details>

---

**Q12.** If the potential at a point $1$ m from charge $Q$ is $9000$ V, the value of $Q$ is:

(a) $1\,\mu C$ &emsp; (b) $10\,\mu C$ &emsp; (c) $1\,\text{nC}$ &emsp; (d) $100\,\text{nC}$

<details><summary><b>Answer</b></summary>

**(a)** $Q = Vr/k = 9000\times1/(9\times10^9) = 10^{-6}$ C $= 1\,\mu C$
</details>

---

**Q13.** As a positive charge moves from infinity towards another positive charge, its electric potential energy:

(a) Increases &emsp; (b) Decreases &emsp; (c) Remains constant &emsp; (d) First increases then decreases

<details><summary><b>Answer</b></summary>

**(a)** $U = kQ_1Q_2/r$. As $r$ decreases (moving closer), $U$ increases for charges of same sign (both positive).
</details>

---

**Q14.** At what distance from a $+2\,\mu C$ charge is the potential equal to $18000$ V?

(a) $0.5$ m &emsp; (b) $1$ m &emsp; (c) $2$ m &emsp; (d) $0.1$ m

<details><summary><b>Answer</b></summary>

**(b)** $r = kQ/V = 9\times10^9\times2\times10^{-6}/18000 = 18000/18000 = 1$ m
</details>

---

**Q15.** Three equal charges $+q$ are at the three corners of an equilateral triangle of side $a$. The potential at the fourth corner of a square of the same side (if they formed a square) would be — this question is a trap. Instead: The potential at the centre of the equilateral triangle is:

(a) $kq/a$ &emsp; (b) $3kq/a$ &emsp; (c) $3\sqrt{3}\,kq/a$ &emsp; (d) $\sqrt{3}\,kq/a$

<details><summary><b>Answer</b></summary>

**(c)** Distance from vertex to centroid of equilateral triangle $= a/\sqrt{3}$. $V = 3\times kq/(a/\sqrt{3}) = 3\sqrt{3}\,kq/a$
</details>

---

### Section B: Short Answer Questions

**Q16.** Derive the expression for electric potential due to a point charge from first principles.

<details><summary><b>Answer</b></summary>

The electric field at distance $r'$ from charge $Q$: $E = kQ/r'^2$.

Work done by external force to bring unit positive charge from $\infty$ to $r$:

$$V(r) = -\int_\infty^r E\,dr' = -\int_\infty^r \frac{kQ}{r'^2}\,dr' = kQ\left[\frac{1}{r'}\right]_\infty^r = \frac{kQ}{r}$$

$$\boxed{V = \frac{1}{4\pi\epsilon_0}\frac{Q}{r}}$$
</details>

---

**Q17.** A charge of $+1.6\times10^{-19}$ C is at the origin. Find the potential at $r = 0.53\times10^{-10}$ m (Bohr radius). What does this represent physically?

<details><summary><b>Answer</b></summary>

$V = \frac{kQ}{r} = \frac{9\times10^9\times1.6\times10^{-19}}{0.53\times10^{-10}} = \frac{1.44\times10^{-9}}{0.53\times10^{-10}} = \mathbf{27.17\,V}$

This is the electric potential felt by the electron in a hydrogen atom at the Bohr radius — exactly the potential that balances the electron's centripetal acceleration in the Bohr model.
</details>

---

**Q18.** Two charges $+9\,\mu C$ and $-1\,\mu C$ are placed $4$ m apart. Find all points on the line joining them where potential is zero.

<details><summary><b>Answer</b></summary>

**Between the charges** (at distance $x$ from $+9\mu C$):

$\frac{9}{x} = \frac{1}{4-x} \Rightarrow 9(4-x) = x \Rightarrow 36 = 10x \Rightarrow x = 3.6$ m

**Beyond the $-1\mu C$ charge** (at distance $d$ from $+9\mu C$, $d > 4$):

$\frac{9}{d} = \frac{1}{d-4} \Rightarrow 9d - 36 = d \Rightarrow d = 4.5$ m

**Two zero-potential points: 3.6 m and 4.5 m from the $+9\mu C$ charge.**
</details>

---

**Q19.** Explain why the electric potential due to a point charge varies as $1/r$ while the field varies as $1/r^2$. Which one is "stronger" at very large distances?

<details><summary><b>Answer</b></summary>

The field is the *gradient* (rate of change) of potential: $E = -dV/dr$. When $V = kQ/r$, differentiating gives $E = kQ/r^2$. Each differentiation with respect to $r$ adds one power of $1/r$.

At large distances, $1/r$ decreases more slowly than $1/r^2$. So potential is "stronger" (more significant) at large distances — the potential at 1 km from a charge might be measurable even when the force is negligibly small.

This is why high-voltage transmission lines are dangerous at distances where the electric force is undetectable: the potential is still substantial.
</details>

---

**Q20.** A conducting sphere of radius $5$ cm has a surface potential of $450$ V. Find (a) the charge on the sphere, (b) the surface charge density $\sigma$.

<details><summary><b>Answer</b></summary>

**(a)** $Q = VR/k = 450\times0.05/(9\times10^9) = 22.5/(9\times10^9) = \mathbf{2.5\times10^{-9}\,C = 2.5\,nC}$

**(b)** $\sigma = Q/(4\pi R^2) = 2.5\times10^{-9}/(4\pi\times0.0025) = 2.5\times10^{-9}/(0.03142) = \mathbf{7.96\times10^{-8}\,C/m^2}$
</details>

---

**Q21.** Two identical metal spheres, one with charge $+6\,\mu C$ and radius $R$ and the other uncharged, are brought into contact and separated. They are then placed $1$ m apart. Find the force between them.

<details><summary><b>Answer</b></summary>

After contact: each sphere has charge $+3\,\mu C$.

$F = \frac{kQ_1 Q_2}{r^2} = \frac{9\times10^9\times3\times10^{-6}\times3\times10^{-6}}{1^2} = 9\times10^9\times9\times10^{-12} = \mathbf{0.081\,N}$
</details>

---

**Q22.** A charge $+Q$ is at $x = 0$ and $+4Q$ is at $x = L$. At what point on the x-axis (between them) is the electric field zero? Is the potential also zero there?

<details><summary><b>Answer</b></summary>

Electric field zero: $\frac{kQ}{x^2} = \frac{k(4Q)}{(L-x)^2}$

$\frac{1}{x^2} = \frac{4}{(L-x)^2} \Rightarrow (L-x)^2 = 4x^2 \Rightarrow L-x = 2x \Rightarrow x = L/3$

Field is zero at $x = L/3$ from $+Q$.

Potential at $x = L/3$: $V = \frac{kQ}{L/3} + \frac{k(4Q)}{2L/3} = \frac{3kQ}{L} + \frac{6kQ}{L} = \frac{9kQ}{L} \neq 0$

**The potential is NOT zero** where the field is zero (both charges positive, so potential is always positive).
</details>

---

**Q23.** Calculate the potential energy of a system consisting of two charges $+2\,\mu C$ and $-3\,\mu C$ separated by $20$ cm.

<details><summary><b>Answer</b></summary>

$U = \frac{kQ_1Q_2}{r} = \frac{9\times10^9\times2\times10^{-6}\times(-3\times10^{-6})}{0.20}$

$U = \frac{9\times10^9\times(-6\times10^{-12})}{0.2} = \frac{-54\times10^{-3}}{0.2} = \mathbf{-0.27\,J}$

Negative energy — the system is bound (the charges attract).
</details>

---

### Section C: Long Answer / JEE-Level

**Q24.** A charge $+Q$ is placed at each corner of a cube of side $a$. Find the potential at the center of the cube.

<details><summary><b>Answer</b></summary>

The distance from any corner to the center of a cube of side $a$ is $r = \frac{a\sqrt{3}}{2}$.

A cube has 8 corners, each with charge $+Q$.

$V = 8\times\frac{kQ}{r} = 8\times\frac{kQ}{a\sqrt{3}/2} = \frac{16kQ}{a\sqrt{3}} = \mathbf{\frac{16Q}{4\pi\epsilon_0 a\sqrt{3}}}$
</details>

---

**Q25.** A charge $Q = -8\,\mu C$ is at $x = 0$ and $Q_2 = +2\,\mu C$ is at $x = 6$ m.

(a) Find all points on the x-axis where $V = 0$.
(b) Find the electric field at each of these points.
(c) Are these zero-field points? Justify.

<details><summary><b>Answer</b></summary>

Let zero-potential point be at distance $x$ from the $-8\,\mu C$ charge.

**Between charges** ($0 < x < 6$): $\frac{-8}{x} + \frac{2}{6-x} = 0 \Rightarrow -8(6-x) = -2x \Rightarrow -48+8x = -2x \Rightarrow 10x = 48$... 

Actually: $\frac{8}{x} = \frac{2}{6-x} \Rightarrow 8(6-x) = 2x \Rightarrow 48-8x = 2x \Rightarrow x = 4.8$ m

**Beyond $+2\,\mu C$** (at $d > 6$ from $-8\mu C$): $\frac{8}{d} = \frac{2}{d-6} \Rightarrow 8(d-6) = 2d \Rightarrow 6d = 48 \Rightarrow d = 8$ m

**Zero-potential at $x = 4.8$ m and $x = 8$ m** from $-8\mu C$ charge.

**(b)** Electric field at $x = 4.8$ m:

$E_1 = k\times8\times10^{-6}/(4.8)^2$ toward $-8\mu C$ (left) $= 9\times10^9\times8\times10^{-6}/23.04 = 3125$ V/m (left)

$E_2 = k\times2\times10^{-6}/(1.2)^2$ away from $+2\mu C$ (right to left) $= 9\times10^9\times2\times10^{-6}/1.44 = 12500$ V/m (left)

Net field is nonzero — both point to the left. $E_{net} \neq 0$.

**(c)** These are NOT zero-field points. $V = 0$ and $E = 0$ are independent conditions.
</details>

---

**Q26.** Three charges $+q$, $-q$, $+q$ are placed at $(-a, 0)$, $(0, 0)$, $(+a, 0)$ respectively. Find the potential at the point $(0, a)$.

<details><summary><b>Answer</b></summary>

Distance from $(0, a)$ to each charge:
- To $(-a, 0)$: $r = \sqrt{a^2+a^2} = a\sqrt{2}$
- To $(0, 0)$: $r = a$
- To $(+a, 0)$: $r = \sqrt{a^2+a^2} = a\sqrt{2}$

$V = \frac{k(+q)}{a\sqrt{2}} + \frac{k(-q)}{a} + \frac{k(+q)}{a\sqrt{2}}$

$V = \frac{2kq}{a\sqrt{2}} - \frac{kq}{a} = \frac{kq\sqrt{2}}{a} - \frac{kq}{a} = \frac{kq(\sqrt{2}-1)}{a}$

$V = \mathbf{\frac{kq(\sqrt{2}-1)}{a}}$
</details>

---

**Q27.** A $+5\,\mu C$ charge is at the origin. Calculate:
(a) The potential at $r = 0.5$ m
(b) The potential energy when a $-2\,\mu C$ charge is placed at $r = 0.5$ m
(c) The work done to bring the $-2\,\mu C$ charge from infinity to $r = 0.5$ m
(d) What happens to this energy when the charges are released?

<details><summary><b>Answer</b></summary>

**(a)** $V = kQ/r = 9\times10^9\times5\times10^{-6}/0.5 = \mathbf{90{,}000\,V}$

**(b)** $U = qV = (-2\times10^{-6})\times90000 = \mathbf{-0.18\,J}$

**(c)** Work $= q(V_P - V_\infty) = (-2\times10^{-6})\times(90000-0) = -0.18$ J. Work done by external agent is $\mathbf{-0.18\,J}$ (field assists the motion — restraint needed).

**(d)** When released, the potential energy ($-0.18$ J) converts to kinetic energy. The charges accelerate toward each other, with total kinetic energy reaching $0.18$ J at contact.
</details>

---

**Q28.** Show that the electric potential outside a uniformly charged sphere of radius $R$ and charge $Q$ at distance $r > R$ is the same as if all the charge were concentrated at the center.

<details><summary><b>Answer</b></summary>

A uniformly charged sphere can be divided into concentric shells. The potential at an external point $r > R$ due to each thin shell (of charge $dQ$ and radius $R'< R$) is:

$dV = \frac{k\,dQ}{r}$ (potential due to a shell at an external point equals that of a point charge at the center)

Since all shells have the same external-point formula, the total potential is:

$V = \int \frac{k\,dQ}{r} = \frac{k}{r}\int dQ = \frac{kQ}{r}$

This is exactly the potential of a point charge $Q$ at $r = 0$. QED.
</details>

---

**Q29.** The electric potential along the x-axis is given by $V(x) = kQ/\sqrt{x^2+a^2}$ (potential on the axis of a charged ring of radius $a$ and charge $Q$). Find the point on the axis where the electric field is maximum.

<details><summary><b>Answer</b></summary>

$E_x = -\frac{dV}{dx} = -kQ\frac{d}{dx}(x^2+a^2)^{-1/2} = kQ\frac{x}{(x^2+a^2)^{3/2}}$

For maximum $E_x$: $\frac{dE_x}{dx} = 0$

$\frac{d}{dx}\left[\frac{x}{(x^2+a^2)^{3/2}}\right] = \frac{(x^2+a^2)^{3/2} - x\cdot\frac{3}{2}(x^2+a^2)^{1/2}\cdot2x}{(x^2+a^2)^3} = 0$

Numerator: $(x^2+a^2) - 3x^2 = a^2-2x^2 = 0$

$x = \frac{a}{\sqrt{2}}$

**The electric field on the axis of the ring is maximum at $x = a/\sqrt{2}$ from the center.**
</details>

---

**Q30.** Two conducting spheres of radii $R_1 = 5$ cm and $R_2 = 10$ cm are connected by a long wire. If the total charge is $Q = 150\,\mu C$, find:
(a) The charge on each sphere
(b) The potential on each sphere
(c) The surface charge density on each sphere

<details><summary><b>Answer</b></summary>

Connected by wire $\Rightarrow$ both at same potential $V$.

$V = kQ_1/R_1 = kQ_2/R_2 \Rightarrow Q_1/R_1 = Q_2/R_2$

$Q_1 = Q_2R_1/R_2 = Q_2\times0.05/0.10 = Q_2/2$

Also $Q_1+Q_2 = 150\mu C$: $Q_2/2 + Q_2 = 150 \Rightarrow Q_2 = 100\,\mu C$, $Q_1 = 50\,\mu C$

**(a)** $Q_1 = \mathbf{50\,\mu C}$, $Q_2 = \mathbf{100\,\mu C}$

**(b)** $V = kQ_1/R_1 = 9\times10^9\times50\times10^{-6}/0.05 = \mathbf{9\times10^6\,V}$ (same on both)

**(c)** $\sigma_1 = Q_1/(4\pi R_1^2) = 50\times10^{-6}/(4\pi\times0.0025) = \mathbf{1592\,\mu C/m^2}$

$\sigma_2 = 100\times10^{-6}/(4\pi\times0.01) = \mathbf{796\,\mu C/m^2}$

Note: $\sigma_1/\sigma_2 = R_2/R_1 = 2$ — smaller sphere has higher surface charge density.
</details>

---

**Q31.** A hollow conducting sphere of inner radius $R_1 = 5$ cm and outer radius $R_2 = 10$ cm carries charge $+Q = 20\,\mu C$. A point charge $+q = 5\,\mu C$ is placed at the center. Find the potential at:
(a) $r = 15$ cm (outside all)
(b) $r = 7.5$ cm (inside the shell material)
(c) $r = 3$ cm (inside the cavity)

<details><summary><b>Answer</b></summary>

Inner surface: $-q = -5\,\mu C$ (induced). Outer surface: $Q + q = +25\,\mu C$.

**(a)** At $r = 15$ cm, total charge = $q + Q = 25\,\mu C$:

$V = k\times25\times10^{-6}/0.15 = 9\times10^9\times25\times10^{-6}/0.15 = \mathbf{1.5\times10^6\,V}$

**(b)** Inside conducting shell material: Same as outer surface potential.

$V = kq_{total}/R_2 = $ (outer surface potential) $= k\times25\times10^{-6}/0.10 = \mathbf{2.25\times10^6\,V}$

**(c)** At $r = 3$ cm inside cavity:

$V = V_{central\ charge} + V_{inner\ surface} + V_{outer\ surface}$

$V = \frac{kq}{r} + \frac{k(-q)}{R_1} + \frac{k(Q+q)}{R_2}$

$V = \frac{9\times10^9\times5\times10^{-6}}{0.03} + \frac{9\times10^9\times(-5\times10^{-6})}{0.05} + \frac{9\times10^9\times25\times10^{-6}}{0.10}$

$V = 1500000 - 900000 + 2250000 = \mathbf{2.85\times10^6\,V}$
</details>

---

**Q32.** Two charges, each $+q = 10\,\mu C$, are fixed at $(-1, 0)$ m and $(+1, 0)$ m. A third charge $Q = -5\,\mu C$ is placed at the origin.

(a) What is the net force on $Q$?
(b) What is the total potential energy of the three-charge system?
(c) How much work must be done to remove $Q$ to infinity while keeping the two $+q$ charges fixed?

<details><summary><b>Answer</b></summary>

**(a)** The two $+q$ charges are symmetrically placed about $Q$. Their forces on $Q$ are equal in magnitude, opposite in direction → **Net force = 0**.

**(b)** Three pairs:
- $U_{12}$ ($+q$ at $-1$ and $+q$ at $+1$): $k(10^{-5})^2/2 = 9\times10^9\times10^{-10}/2 = 0.45$ J
- $U_{1Q}$ ($+q$ at $-1$ and $Q$ at $0$): $k(10^{-5})(-5\times10^{-6})/1 = 9\times10^9\times(-5\times10^{-11}) = -0.45$ J
- $U_{2Q}$ ($+q$ at $+1$ and $Q$ at $0$): same as $U_{1Q} = -0.45$ J

$U_{total} = 0.45 - 0.45 - 0.45 = \mathbf{-0.45\,J}$

**(c)** Work to remove $Q$ to infinity = $-(U_{1Q} + U_{2Q})$, since $U_{12}$ doesn't change.

$W = -(-0.45 - 0.45) = \mathbf{+0.90\,J}$

You must do $0.90$ J of work against the attractive forces pulling $Q$ back.
</details>

---

*Next: [Chapter 3 — Potential Due to an Electric Dipole →](./03_potential_dipole.md)*
