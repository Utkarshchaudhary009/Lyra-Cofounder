# Chapter 4: Potential Due to a System of Charges

> *NCERT Section 2.5*

---

### The Story of the Architect's Shortcut

Imagine an architect designing a building. She needs to know the total weight pressing down on the foundation. She has hundreds of individual components — walls, columns, furniture, water tanks — each with its own weight. Does she need to worry about the *direction* each weight pushes? No. Weight always points straight down. She simply **adds up the numbers**.

This is the fundamental advantage of working with potential instead of electric field. The electric field is a vector — to find the total field from multiple charges, you must break each field into components, sum the components separately, and then combine them. It's laborious.

Potential is a scalar. You just... add.

---

### Building the Concept: Superposition of Potentials

Consider $n$ charges $Q_1, Q_2, \ldots, Q_n$ located at positions $\vec{r}_1, \vec{r}_2, \ldots, \vec{r}_n$. The potential at point P (position $\vec{r}$) due to this system is simply the algebraic sum of the individual potentials:

$$\boxed{V(\vec{r}) = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^{n} \frac{Q_i}{|\vec{r} - \vec{r}_i|}}$$

No vectors. No components. No $\sin\theta$ or $\cos\theta$ decomposition. Just plain arithmetic with signed numbers.

This is the **Principle of Superposition for Potentials**, and it is why potential calculations are almost always easier than field calculations.

> **When to use potential vs. field:** If a problem asks "find the field," you usually must work with vectors. But if it asks "find the work done" or "find the energy," always go through potential — it's faster. And if you need the field afterward, you can always get it from $\vec{E} = -\nabla V$ (covered in Chapter 6).

---

### Checkpoint 1: Direct Superposition

**The Charged Square:** *Four charges are placed at the corners of a square of side $a = 0.2$ m.*

**Problem 1:** All four charges are $+1 \mu C$. Find the potential at the center of the square.

<details><summary><b>Solution</b></summary>

The distance from each corner to the center of a square of side $a$ is $r = \frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$.

$r = \frac{0.2}{\sqrt{2}} = 0.1414$ m

$V = 4 \times \frac{kQ}{r} = 4 \times \frac{9 \times 10^9 \times 10^{-6}}{0.1414}$

$V = 4 \times 63640 = \textbf{254,558 V ≈ 255 kV}$
</details>

**Problem 2:** The charges are now $+1\mu C$, $-1\mu C$, $+1\mu C$, $-1\mu C$ (alternating). Find the potential at the center.

<details><summary><b>Solution</b></summary>

All charges are at the same distance from the center. The algebraic sum of charges is:

$Q_{total} = +1 - 1 + 1 - 1 = 0$

$V = \frac{k}{r}(Q_1 + Q_2 + Q_3 + Q_4) = \frac{k}{r} \times 0 = \textbf{0}$

The potential at the center of a charge-balanced arrangement is always zero, regardless of the specific geometry, as long as all charges are equidistant from the center.
</details>

**Problem 3:** The charges are $+2\mu C$, $-1\mu C$, $+3\mu C$, $-1\mu C$ at corners A, B, C, D respectively. Find the potential at the center.

<details><summary><b>Solution</b></summary>

$Q_{total} = 2 - 1 + 3 - 1 = +3 \mu C = 3 \times 10^{-6}$ C

$V = \frac{k \times Q_{total}}{r} = \frac{9 \times 10^9 \times 3 \times 10^{-6}}{0.1414} = \frac{27000}{0.1414}$

$V = \textbf{190,919 V ≈ 191 kV}$

The beauty of scalar addition — we can sum all charges first, then compute one potential instead of four.
</details>

---

### Checkpoint 2: The Gauntlet — "The Necklace Problem"

*A jeweler is designing a circular pendant with tiny charged beads arranged evenly on a ring of radius $R = 5$ cm. She wants to know the potential at the center to ensure no sparking occurs.*

**Problem 1:** Six identical beads, each with charge $+2$ nC, are equally spaced on the ring. Find the potential at the center.

<details><summary><b>Solution</b></summary>

Every bead is at distance $R = 0.05$ m from the center.

$V = 6 \times \frac{kQ}{R} = 6 \times \frac{9 \times 10^9 \times 2 \times 10^{-9}}{0.05}$

$V = 6 \times \frac{18}{0.05} = 6 \times 360 = \textbf{2160 V}$
</details>

*She removes one bead (leaving 5 beads of $+2$ nC).*

**Problem 2:** What is the new potential at the center?

<details><summary><b>Solution</b></summary>

$V = 5 \times 360 = \textbf{1800 V}$

Simple subtraction — we lost one bead's contribution of 360 V.
</details>

*She replaces the removed bead with a bead of charge $-2$ nC.*

**Problem 3:** What is the potential at the center now?

<details><summary><b>Solution</b></summary>

$V = 5 \times \frac{k(+2 \times 10^{-9})}{R} + 1 \times \frac{k(-2 \times 10^{-9})}{R}$

$V = 5 \times 360 + 1 \times (-360) = 1800 - 360 = \textbf{1440 V}$

Or equivalently: the sum of all charges is $5(+2) + 1(-2) = 8$ nC.

$V = \frac{k \times 8 \times 10^{-9}}{0.05} = \frac{72}{0.05} = 1440$ V. ✓
</details>

*She wonders: what if she adds beads to make the sum of charges exactly zero?*

**Problem 4:** She has 3 beads of $+4$ nC and 3 beads of $-4$ nC, alternating around the ring. What is the potential at the center?

<details><summary><b>Solution</b></summary>

$Q_{total} = 3(+4) + 3(-4) = 0$

$V = \frac{k \times 0}{R} = \textbf{0}$

The potential is zero at the center. But the electric field at the center is *not* zero — the asymmetric arrangement of positive and negative charges creates a complicated field pattern. This distinction is crucial for exams.
</details>

---

### Checkpoint 3: Finding the Null Point

**Problem 1:** Two charges $Q_1 = +4\mu C$ and $Q_2 = +1\mu C$ are placed $3$ m apart. Find the point on the line joining them where the potential is zero.

<details><summary><b>Solution</b></summary>

For two positive charges, the potential is always positive everywhere on the line between them (and everywhere in space). 

$V = \frac{kQ_1}{r_1} + \frac{kQ_2}{r_2}$

Both terms are positive, so $V > 0$ always.

**There is no point where $V = 0$ on the line (or anywhere in space) for two charges of the same sign.**

This is a common conceptual trap in exams. Zero potential requires charges of opposite signs.
</details>

**Problem 2:** Now let $Q_1 = +4\mu C$ and $Q_2 = -1\mu C$, placed $3$ m apart. Find the point(s) on the line joining them where $V = 0$.

<details><summary><b>Solution</b></summary>

Let the zero-potential point be at distance $x$ from $Q_1$.

**Case 1: Between the charges** ($0 < x < 3$)

$\frac{kQ_1}{x} + \frac{kQ_2}{3 - x} = 0$

$\frac{4}{x} = \frac{1}{3 - x}$

$4(3 - x) = x \implies 12 - 4x = x \implies x = 2.4$ m

**Case 2: Beyond $Q_2$** (at distance $d$ from $Q_1$, where $d > 3$)

$\frac{4}{d} + \frac{-1}{d - 3} = 0$

$\frac{4}{d} = \frac{1}{d - 3}$

$4(d - 3) = d \implies 3d = 12 \implies d = 4$ m

$\textbf{Two points: x = 2.4 m (between) and x = 4.0 m (beyond Q₂)}$

> Note: There is no zero-potential point beyond $Q_1$ (on the opposite side), because the larger charge dominates everywhere in that region.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** Three charges are arranged as follows:  
- $Q_1 = +10 \mu C$ at the origin $(0, 0)$
- $Q_2 = -5 \mu C$ at $(3, 0)$ m
- $Q_3 = +5 \mu C$ at $(0, 4)$ m

(a) Find the potential at the point $(3, 4)$ m.  
(b) How much work is done in bringing a $-2 \mu C$ charge from infinity to $(3, 4)$?  
(c) If the charge of $-2 \mu C$ is now moved from $(3, 4)$ to the origin, what additional work is done?

<details><summary><b>Solution</b></summary>

**(a)** First, find the distances from $(3, 4)$ to each charge:

- From $Q_1$ at $(0,0)$: $r_1 = \sqrt{3^2 + 4^2} = 5$ m
- From $Q_2$ at $(3,0)$: $r_2 = \sqrt{0^2 + 4^2} = 4$ m
- From $Q_3$ at $(0,4)$: $r_3 = \sqrt{3^2 + 0^2} = 3$ m

$V = k\left(\frac{Q_1}{r_1} + \frac{Q_2}{r_2} + \frac{Q_3}{r_3}\right)$

$V = 9 \times 10^9 \left(\frac{10 \times 10^{-6}}{5} + \frac{-5 \times 10^{-6}}{4} + \frac{5 \times 10^{-6}}{3}\right)$

$V = 9 \times 10^9 \left(2 \times 10^{-6} - 1.25 \times 10^{-6} + 1.667 \times 10^{-6}\right)$

$V = 9 \times 10^9 \times 2.417 \times 10^{-6} = \textbf{21,750 V ≈ 21.75 kV}$

**(b)** Work done by external force:

$W = q(V_{final} - V_{initial}) = (-2 \times 10^{-6})(21750 - 0)$

$W = \textbf{-0.0435 J = -43.5 mJ}$

Negative work means the external force actually *restrains* the charge — the charge naturally wants to move toward this point (since it's negative and the potential there is positive, the potential energy $U = qV$ is negative, which is lower than at infinity).

**(c)** At the origin, the potential due to $Q_2$ and $Q_3$ is:

$V_{origin} = k\left(\frac{Q_2}{3} + \frac{Q_3}{4}\right) = 9 \times 10^9 \left(\frac{-5 \times 10^{-6}}{3} + \frac{5 \times 10^{-6}}{4}\right)$

$V_{origin} = 9 \times 10^9 \left(-1.667 \times 10^{-6} + 1.25 \times 10^{-6}\right) = 9 \times 10^9 \times (-0.417 \times 10^{-6})$

$V_{origin} = -3750$ V

(We exclude $Q_1$ because we cannot compute the potential of a charge at its own location — it diverges. The work done is calculated using only the potential due to *other* charges.)

$W = q(V_{final} - V_{initial}) = (-2 \times 10^{-6})(-3750 - 21750)$

$W = (-2 \times 10^{-6})(-25500) = \textbf{+0.051 J = +51 mJ}$

Positive work — the external agent must push the charge from $(3,4)$ to the origin, fighting against the electric field of the system.
</details>

---

## Question Bank — Chapter 4

### Section A: MCQs (15 Questions)

**Q1.** The principle of superposition of electric potential states that the total potential is the:

(a) Vector sum of individual potentials &emsp; (b) Algebraic sum of individual potentials &emsp; (c) Product of individual potentials &emsp; (d) None of the above

<details><summary><b>Answer</b></summary>**(b)** Potential is a scalar — it adds algebraically (with sign).</details>

---

**Q2.** Four charges $+q$, $+q$, $-q$, $-q$ are placed at the corners of a square. The potential at the center is:

(a) $4kq/r$ &emsp; (b) $2kq/r$ &emsp; (c) $0$ &emsp; (d) $kq/r$

<details><summary><b>Answer</b></summary>**(c)** Net charge $= +q+q-q-q = 0$. All corners equidistant from center. $V = k(0)/r = 0$.</details>

---

**Q3.** Three charges $+q$, $+q$, $+q$ are at the corners of an equilateral triangle. The potential at the centroid is:

(a) $kq/a$ &emsp; (b) $3kq/a$ &emsp; (c) $3\sqrt{3}kq/a$ &emsp; (d) $\sqrt{3}kq/a$

<details><summary><b>Answer</b></summary>**(c)** Centroid distance $= a/\sqrt{3}$. $V = 3\times kq/(a/\sqrt{3}) = 3\sqrt{3}kq/a$.</details>

---

**Q4.** Two charges $+Q$ and $-Q$ are placed at points A and B. At the midpoint M of AB, the electric potential is:

(a) $2kQ/r$ &emsp; (b) $kQ/r$ &emsp; (c) $0$ &emsp; (d) $-kQ/r$

<details><summary><b>Answer</b></summary>**(c)** Equidistant from $+Q$ and $-Q$: $V = kQ/d + k(-Q)/d = 0$.</details>

---

**Q5.** Which of the following charge distributions can give zero potential everywhere in space?

(a) A single $+q$ charge &emsp; (b) Two equal $+q$ charges &emsp; (c) No finite distribution of charges &emsp; (d) An infinite line of $+q$ charges

<details><summary><b>Answer</b></summary>**(c)** Any finite charge distribution produces nonzero potential somewhere. Zero potential everywhere implies no charges.</details>

---

**Q6.** At a null point (zero potential), the electric field:

(a) Is always zero &emsp; (b) May or may not be zero &emsp; (c) Is always nonzero &emsp; (d) Is undefined

<details><summary><b>Answer</b></summary>**(b)** Zero potential does not imply zero field. $V = 0$ and $E = 0$ are independent conditions.</details>

---

**Q7.** Two charges $+4\,\mu C$ and $-1\,\mu C$ are $3$ m apart. The number of zero-potential points on the line joining them is:

(a) 0 &emsp; (b) 1 &emsp; (c) 2 &emsp; (d) Infinite

<details><summary><b>Answer</b></summary>**(c)** For opposite charges, there are exactly 2 zero-potential points on the joining line (one between, one outside near the smaller charge).</details>

---

**Q8.** $n$ identical charges $q$ are equally spaced on a circle of radius $R$. The potential at the center is:

(a) $knq/R$ &emsp; (b) $kq/R$ &emsp; (c) $kq/(nR)$ &emsp; (d) $0$

<details><summary><b>Answer</b></summary>**(a)** Each charge contributes $kq/R$. Total: $V = nkq/R$.</details>

---

**Q9.** If the potential at a point due to a system of charges is $V$, the work done to bring charge $q$ from infinity to that point is:

(a) $qV$ &emsp; (b) $V/q$ &emsp; (c) $q/V$ &emsp; (d) $q^2V$

<details><summary><b>Answer</b></summary>**(a)** $W = qV$ (by definition of potential).</details>

---

**Q10.** Potential due to a system of charges obeys:

(a) Inverse square law &emsp; (b) Inverse law &emsp; (c) Superposition principle &emsp; (d) Both (b) and (c)

<details><summary><b>Answer</b></summary>**(d)** Each charge contributes $kq/r$ (inverse law), and these are added by superposition.</details>

---

**Q11.** The potential at the center of a regular hexagon with charges $+q$ at all 6 vertices (side $a$) is:

(a) $kq/a$ &emsp; (b) $6kq/a$ &emsp; (c) $\sqrt{6}kq/a$ &emsp; (d) $0$

<details><summary><b>Answer</b></summary>**(b)** In a regular hexagon, the center-to-vertex distance equals the side $a$. Each charge contributes $kq/a$. Total: $6kq/a$.</details>

---

**Q12.** The advantage of using potential over electric field for a system of charges is:

(a) Potential is a vector &emsp; (b) Potential requires no angle calculations &emsp; (c) Potential is always positive &emsp; (d) Potential is quantized

<details><summary><b>Answer</b></summary>**(b)** Scalar addition needs no vector components or angle decomposition.</details>

---

**Q13.** A charge $q$ is placed at a point where the potential due to other charges is $V_0$. The potential energy of the system increases by:

(a) $qV_0/2$ &emsp; (b) $qV_0$ &emsp; (c) $2qV_0$ &emsp; (d) $q^2V_0$

<details><summary><b>Answer</b></summary>**(b)** The increase in potential energy equals the work done bringing $q$ to that point: $\Delta U = qV_0$.</details>

---

**Q14.** Two charges $Q_1 = +5\,\mu C$ and $Q_2 = -5\,\mu C$ are separated by $10$ cm. The potential at their midpoint is:

(a) $900$ kV &emsp; (b) $-900$ kV &emsp; (c) $0$ &emsp; (d) $450$ kV

<details><summary><b>Answer</b></summary>**(c)** Equal and opposite charges equidistant from midpoint: $V = 0$.</details>

---

**Q15.** In a system of $n$ charges, the number of distinct pairwise interactions is:

(a) $n$ &emsp; (b) $n^2$ &emsp; (c) $n(n-1)/2$ &emsp; (d) $n(n+1)/2$

<details><summary><b>Answer</b></summary>**(c)** Number of pairs = $\binom{n}{2} = n(n-1)/2$.</details>

---

### Section B: Short Answer Questions

**Q16.** Two charges $+3\,\mu C$ and $-7\,\mu C$ are placed $5$ m apart. Find the two points on the joining line where $V = 0$.

<details><summary><b>Answer</b></summary>

**Between charges** (at $x$ from $+3\mu C$): $3/x = 7/(5-x) \Rightarrow 15-3x = 7x \Rightarrow x = 1.5$ m

**Beyond** $-7\mu C$ (at $d$ from $+3\mu C$, $d>5$): $3/d = 7/(d-5) \Rightarrow 3d-15 = 7d \Rightarrow d = -3.75$ m (negative, so this case gives $d = 15/4 = 3.75$ m from $-7\mu C$ on the far side).

Redo: $3/d = 7/(d-5) \Rightarrow 3(d-5) = 7d \Rightarrow 3d-15 = 7d \Rightarrow -4d = 15 \Rightarrow d = -3.75$ m

This means the point is at $3.75$ m on the other side of $+3\mu C$, i.e., $3.75$ m from $+3\mu C$ in the direction away from $-7\mu C$.

Check: at $x = -3.75$ m from $+3\mu C$: $V = k(3\mu C)/3.75 + k(-7\mu C)/8.75 = k[0.8 - 0.8]\times 10^{-6} = 0$ ✓

**Points: $1.5$ m from $+3\mu C$ (between them) and $3.75$ m from $+3\mu C$ (beyond $+3\mu C$).**
</details>

---

**Q17.** Five charges of $+2\,\mu C$ each are placed at the vertices of a regular pentagon of side $0.1$ m. Find the potential at the center. (Distance from center to vertex of a regular pentagon of side $a$: $r = a/(2\sin36°) \approx 0.85a$)

<details><summary><b>Answer</b></summary>

$r \approx 0.85\times0.1 = 0.085$ m

$V = 5\times\frac{kq}{r} = 5\times\frac{9\times10^9\times2\times10^{-6}}{0.085} = 5\times\frac{18000}{0.085} = 5\times211765 \approx \mathbf{1.06\times10^6\,V}$
</details>

---

**Q18.** Explain the statement: "For calculating electric potential, the superposition principle makes life dramatically easier than for electric field."

<details><summary><b>Answer</b></summary>

**Electric field** from $n$ charges: must compute $n$ vector quantities $\vec{E}_i$, each with direction, then add components: $\vec{E} = \sum\vec{E}_i$. Requires trigonometry for angles and separate x, y, z summations.

**Electric potential** from $n$ charges: compute $n$ scalar quantities $V_i = kq_i/r_i$, then simply add: $V = \sum V_i$. No angles, no components, no direction tracking.

For $n = 10$ charges at random positions, computing the field requires $30$ numbers ($x,y,z$ for each field), while computing the potential requires only $10$ scalar additions.
</details>

---

**Q19.** Four charges $+q$, $+q$, $-q$, $-q$ are placed at the four corners of a square of diagonal $2r$. Compute the potential at the center.

<details><summary><b>Answer</b></summary>

All four charges are at distance $r$ from the center (half-diagonal).

$V = k(+q+q-q-q)/r = \mathbf{0}$

The charges cancel in pairs at the equidistant center.
</details>

---

**Q20.** A $+1\,\mu C$ charge is at the origin and a $-2\,\mu C$ charge is at $x = 4$ m. At what point on the x-axis (other than infinity) is the potential zero?

<details><summary><b>Answer</b></summary>

**Between charges** (at $x$, $0 < x < 4$): $1/x = 2/(4-x) \Rightarrow 4-x = 2x \Rightarrow x = 4/3 \approx 1.33$ m ✓

**Beyond** $+1\mu C$ (at $x < 0$, distance $|x|$ from origin, $4-x$ from $-2\mu C$):
$1/|x| = 2/(4+|x|) \Rightarrow 4+|x| = 2|x| \Rightarrow |x| = 4$ m, so $x = -4$ m.

**Two points: $x = 4/3$ m and $x = -4$ m.**
</details>

---

**Q21.** Three charges $+5\,\mu C$, $-3\,\mu C$, and $+8\,\mu C$ are placed at the vertices of a right triangle with legs $3$ m and $4$ m. Find the potential at the right-angle vertex (where the $+8\,\mu C$ charge is NOT).

<details><summary><b>Answer</b></summary>

Let $+5\mu C$ at A, $-3\mu C$ at B, $+8\mu C$ at C. Right angle at vertex P (not at C). Legs AP = 3 m, BP = 4 m; hypotenuse CP = 5 m.

$V = \frac{k\times5\times10^{-6}}{3} + \frac{k\times(-3\times10^{-6})}{4} + \frac{k\times8\times10^{-6}}{5}$

$V = 9\times10^9\times10^{-6}\left(\frac{5}{3} - \frac{3}{4} + \frac{8}{5}\right) = 9000\left(1.667 - 0.75 + 1.6\right)$

$V = 9000\times2.517 = \mathbf{22{,}650\,V \approx 22.7\,kV}$
</details>

---

**Q22.** Show that the potential at the center of a uniformly charged ring of radius $R$ and total charge $Q$ is $V = kQ/R$.

<details><summary><b>Answer</b></summary>

Divide the ring into infinitesimal elements $dq$. Each element is at distance $R$ from the center.

$V = \int \frac{k\,dq}{R} = \frac{k}{R}\int dq = \frac{kQ}{R}$

This is the same as the potential of a point charge $Q$ at distance $R$. The result is exact (no approximation needed) because all elements are equidistant from the center.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** Charges $+1\,\mu C$, $+2\,\mu C$, $+3\,\mu C$ are at the corners A, B, C of an equilateral triangle of side $1$ m. A fourth charge $Q$ is placed at the centroid such that the system is in equilibrium. Find $Q$.

<details><summary><b>Answer</b></summary>

For equilibrium, the force on each corner charge must be zero. By symmetry, the centroidal charge $Q$ must produce equal and opposite forces on each corner charge relative to the other two.

However, since the corner charges are not equal ($1, 2, 3\,\mu C$), true equilibrium for ALL charges simultaneously is impossible (Earnshaw's theorem prevents it anyway). The problem likely asks: what $Q$ makes the net force on the centroid charge zero?

At centroid, all three corner charges are at distance $r = a/\sqrt{3} = 1/\sqrt{3}$ m.

Force on $Q$ due to $+1\mu C$: $F_1 = kQ\times1\times10^{-6}/r^2$ (along centroid→A direction)

By superposition, net force = $\frac{kQ}{r^2}\times10^{-6}\times(\vec{1}+\vec{2}+\vec{3})$ where $\vec{1},\vec{2},\vec{3}$ are unit vectors from centroid to each vertex.

In an equilateral triangle, the unit vectors from centroid to vertices sum to zero: $\vec{1}+\vec{2}+\vec{3} = 0$.

Therefore, net force on $Q$ = 0 for **any** value of $Q$.

So $Q$ can be any value (it's always in force equilibrium at the centroid by symmetry of equilateral triangle geometry — but the charges must be equal for this. Since they're not equal here, the geometry does not produce perfect vector cancellation).

For equal charges $+q$ at all vertices, the centroid is an equilibrium point for any $Q$.
</details>

---

**Q24.** Two charges $+Q$ and $-Q$ are fixed on the x-axis at $x = +a$ and $x = -a$. A third charge $q$ can move freely. Show that any point on the y-axis is an equilibrium position for $q$, but the equilibrium is unstable.

<details><summary><b>Answer</b></summary>

**Force on $q$ at $(0, y)$:**

Distance to each charge: $r = \sqrt{a^2+y^2}$

Force from $+Q$: $F_+ = kqQ/r^2$ directed from $(a,0)$ to $(0,y)$

Force from $-Q$: $F_- = kqQ/r^2$ directed from $(0,y)$ to $(-a,0)$

By symmetry, the x-components cancel. The y-components:

$F_{y+} = F_+\sin\theta = \frac{kqQ}{r^2}\cdot\frac{y}{r}$

$F_{y-} = -F_-\sin\theta = -\frac{kqQ}{r^2}\cdot\frac{y}{r}$

Net y-force = 0. So YES, every point on the y-axis is an equilibrium.

**Why unstable:** If $q$ is displaced in the x-direction, both charges exert forces in the same x-direction — no restoring force. The equilibrium is unstable in the x-direction (and by Earnshaw's theorem, cannot be stable in all directions simultaneously).
</details>

---

**Q25–Q32:** (Varied numericals on finding potential at geometric points, work calculations, null points, and energy of assembly — all following patterns established in Q16–Q24 above.)

> *These problems mirror JEE Mains pattern: geometric setups with 3–4 charges, request for potential at a specific point, then work/energy calculation.*

**Q25.** Charges $+2, -3, +5\,\mu C$ are at $(0,0)$, $(3,0)$, $(0,4)$ m. Find $V$ at $(3,4)$ m and work to bring $+1\,\mu C$ from $\infty$ to $(3,4)$.

<details><summary><b>Answer</b></summary>

Distances from $(3,4)$: to $(0,0) = 5$ m, to $(3,0) = 4$ m, to $(0,4) = 3$ m.

$V = k\left(\frac{2\times10^{-6}}{5} + \frac{-3\times10^{-6}}{4} + \frac{5\times10^{-6}}{3}\right) = 9\times10^3\left(0.4 - 0.75 + 1.667\right) = 9000\times1.317 = \mathbf{11{,}850\,V}$

$W = qV = 1\times10^{-6}\times11850 = \mathbf{0.01185\,J \approx 11.85\,mJ}$
</details>

---

**Q26.** Charges $+q$ are at all four corners of a square of side $a$. Find the work done to bring a charge $+Q$ from infinity to the center.

<details><summary><b>Answer</b></summary>

Center-to-corner distance $= a\sqrt{2}/2 = a/\sqrt{2}$.

$V_{center} = 4\times\frac{kq}{a/\sqrt{2}} = \frac{4\sqrt{2}kq}{a}$

$W = QV = \frac{4\sqrt{2}kqQ}{a}$
</details>

---

**Q27.** In a hydrogen atom, the electron (charge $-e$) moves from the ground state orbit ($r_1 = 0.53$ Å) to the first excited state orbit ($r_2 = 2.12$ Å). Find the change in potential energy. (Proton charge $= +e$)

<details><summary><b>Answer</b></summary>

$U_1 = \frac{k(-e)(+e)}{r_1} = \frac{-ke^2}{r_1}$, $U_2 = \frac{-ke^2}{r_2}$

$\Delta U = U_2 - U_1 = -ke^2\left(\frac{1}{r_2} - \frac{1}{r_1}\right) = ke^2\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$

$\Delta U = 9\times10^9\times(1.6\times10^{-19})^2\left(\frac{1}{0.53\times10^{-10}} - \frac{1}{2.12\times10^{-10}}\right)$

$= 9\times10^9\times2.56\times10^{-38}\times(18.87-4.72)\times10^9 = 2.304\times10^{-28}\times14.15\times10^9$

$\Delta U \approx \mathbf{3.26\times10^{-18}\,J \approx 20.4\,eV}$

The PE increased by $20.4$ eV when the electron moved to the higher orbit.
</details>

---

**Q28.** A system of charges has potential $V(x,y) = 3x^2 - 2y^2 + 5$ (in volts, with $x,y$ in metres). Find the electric field components $E_x$ and $E_y$, and identify the charge-free region (where $\nabla^2 V = 0$).

<details><summary><b>Answer</b></summary>

$E_x = -\partial V/\partial x = -6x$

$E_y = -\partial V/\partial y = +4y$

$\nabla^2 V = \partial^2V/\partial x^2 + \partial^2V/\partial y^2 = 6 + (-4) = 2 \neq 0$

Since $\nabla^2 V \neq 0$ everywhere, there is a **nonzero charge density** everywhere (by Poisson's equation $\nabla^2 V = -\rho/\epsilon_0$). There is no charge-free region.
</details>

---

**Q29.** Three identical charges $+q$ are placed at the vertices of an equilateral triangle of side $a$. A fourth charge $-3q$ is placed at the centroid. Find the total potential energy of the system.

<details><summary><b>Answer</b></summary>

Centroid-to-vertex distance: $r = a/\sqrt{3}$

Pairs involving the three $+q$ charges with each other (3 pairs, each at distance $a$):
$U_{qq} = 3\times kq^2/a$

Pairs of each $+q$ with $-3q$ at centroid (3 pairs, each at distance $a/\sqrt{3}$):
$U_{q(-3q)} = 3\times\frac{k(q)(-3q)}{a/\sqrt{3}} = 3\times\frac{-3kq^2\sqrt{3}}{a} = \frac{-9\sqrt{3}kq^2}{a}$

Total: $U = \frac{3kq^2}{a} - \frac{9\sqrt{3}kq^2}{a} = \frac{kq^2}{a}(3-9\sqrt{3})$
</details>

---

**Q30.** Show that the potential at any point inside a uniformly charged spherical shell of radius $R$ and charge $Q$ equals $kQ/R$ (same as the surface potential).

<details><summary><b>Answer</b></summary>

The field inside a uniformly charged shell is zero (by Gauss's law). Since $E = -dV/dr = 0$ inside, $V$ must be constant inside.

At the surface ($r = R$): $V = kQ/R$.

Since $V$ is continuous and constant inside, $V_{inside} = kQ/R$ everywhere inside.

This means an entire region of space has the same potential as the surface — the interior is one giant equipotential volume.
</details>

---

**Q31.** Charges $Q_1 = +10\,\mu C$ and $Q_2 = -6\,\mu C$ are separated by $d = 0.5$ m. Find all points where the potential is zero. How many such points are there?

<details><summary><b>Answer</b></summary>

**Between** (at $x$ from $Q_1$): $10/x = 6/(0.5-x) \Rightarrow 5 - 10x = 6x \Rightarrow x = 5/16 = 0.3125$ m

**Beyond $Q_2$** (at $d$ from $Q_1$, $d>0.5$): $10/d = 6/(d-0.5) \Rightarrow 10d-5 = 6d \Rightarrow d = 1.25$ m

**Two zero-potential points:** at $0.3125$ m and $1.25$ m from $Q_1$ (both on the same side as $Q_2$).

Note: there is no zero-potential point on the far side of $Q_1$ (beyond the larger charge), as $Q_1$ dominates there.
</details>

---

**Q32.** Eight charges $+q$ are placed at the corners of a cube of side $a$. Find the potential at:
(a) The center of the cube
(b) The center of any face
(c) The midpoint of any edge

<details><summary><b>Answer</b></summary>

**(a)** Distance corner-to-center $= a\sqrt{3}/2$. $V_{center} = 8\times kq/(a\sqrt{3}/2) = 16kq/(a\sqrt{3})$

**(b)** Face center: 4 adjacent corners at distance $a/\sqrt{2}$, 4 diagonal corners at distance $a\sqrt{3/2} = a\sqrt{6}/2$.

$V_{face} = 4\times\frac{kq}{a/\sqrt{2}} + 4\times\frac{kq}{a\sqrt{6}/2} = \frac{4\sqrt{2}kq}{a} + \frac{8kq}{a\sqrt{6}}$

**(c)** Edge midpoint: 2 corners at $a/2$, 4 at $a\sqrt{5}/2$, 2 at $a\sqrt{3}/2$.

$V_{edge} = 2\times\frac{kq}{a/2} + 4\times\frac{2kq}{a\sqrt{5}} + 2\times\frac{2kq}{a\sqrt{3}} = \frac{kq}{a}\left(4 + \frac{8}{\sqrt{5}} + \frac{4}{\sqrt{3}}\right)$
</details>

---

*Next: [Chapter 5 — Equipotential Surfaces →](./05_equipotential_surfaces.md)*
