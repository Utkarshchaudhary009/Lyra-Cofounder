# Chapter 6: Relation Between Field and Potential

> *NCERT Section 2.6 (continued)*

---

### The Paradox of the Flat Map

You have a topographic map that shows you the *height* at every point (the potential). Your friend has a compass that tells them the *slope* at every point (the field). Here is the paradox: if you give someone your map, they can *construct* the compass. But if someone gives you only the compass, you cannot fully reconstruct the map — you'll be missing a constant (the absolute altitude).

This asymmetry reveals a deep truth: **the electric field is the derivative of the potential.** The field is the *rate of change* of the potential with respect to position. You can always go from potential to field by differentiation, and from field to potential by integration — but integration introduces an unknown constant (the reference potential).

---

### Building the Concept

#### The General Relation

Consider two points A and B, infinitesimally close, separated by a displacement $d\vec{l}$. The work done by the electric field in moving a unit positive charge from A to B is:

$$dW = \vec{E} \cdot d\vec{l}$$

But this work also equals the decrease in potential:

$$dW = -dV$$

Therefore:

$$-dV = \vec{E} \cdot d\vec{l}$$

If we move specifically in the $x$-direction ($d\vec{l} = dx\,\hat{x}$):

$$E_x = -\frac{\partial V}{\partial x}$$

And similarly for the other directions. The full relation in three dimensions:

$$\boxed{\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{x} + \frac{\partial V}{\partial y}\hat{y} + \frac{\partial V}{\partial z}\hat{z}\right)}$$

#### The One-Dimensional Case (Most Common in Exams)

For problems involving motion along a single direction:

$$\boxed{E = -\frac{dV}{dr}}$$

The negative sign means that the field points in the direction of *decreasing* potential. Charges don't roll uphill — they roll downhill.

#### The Uniform Field Case

For a uniform electric field $E$ between two parallel surfaces at potentials $V_1$ and $V_2$, separated by distance $d$:

$$E = \frac{V_1 - V_2}{d} = \frac{\Delta V}{d}$$

This is just the slope of the "hill" — potential difference divided by distance.

> **Critical Insight for JEE:** Many JEE problems give you $V$ as a function of $x, y, z$ and ask you to find $\vec{E}$. The recipe is mechanical: take the negative partial derivative with respect to each coordinate. Master this, and you have a free 4-mark question.

---

### Checkpoint 1: From Potential to Field

**Problem 1:** The electric potential in a region is given by $V = 6x - 8xy - 8y + 6yz$ volts (where $x, y, z$ are in meters). Find the electric field at the origin.

<details><summary><b>Solution</b></summary>

$E_x = -\frac{\partial V}{\partial x} = -(6 - 8y) = -6 + 8y$

$E_y = -\frac{\partial V}{\partial y} = -(-8x - 8 + 6z) = 8x + 8 - 6z$

$E_z = -\frac{\partial V}{\partial z} = -(6y) = -6y$

At the origin $(0, 0, 0)$:

$E_x = -6 + 0 = -6$ V/m

$E_y = 0 + 8 - 0 = 8$ V/m

$E_z = 0$ V/m

$\vec{E} = -6\hat{x} + 8\hat{y}$ V/m

$|\vec{E}| = \sqrt{36 + 64} = \sqrt{100} = \textbf{10 V/m}$
</details>

**Problem 2:** The potential at a point is given by $V = 20/(x^2 + y^2 + z^2)^{1/2}$. What is this potential due to? Find $\vec{E}$ at $(1, 0, 0)$.

<details><summary><b>Solution</b></summary>

$V = \frac{20}{r}$ where $r = \sqrt{x^2 + y^2 + z^2}$. This is the potential due to a **point charge** at the origin with $kQ = 20$, i.e., $Q = 20/(9 \times 10^9) \approx 2.22 \times 10^{-9}$ C.

At $(1, 0, 0)$: $r = 1$ m, $V = 20$ V.

$E_x = -\frac{\partial V}{\partial x} = -\frac{\partial}{\partial x}\left[20(x^2 + y^2 + z^2)^{-1/2}\right]$

$E_x = -20 \times (-\frac{1}{2})(x^2 + y^2 + z^2)^{-3/2} \times 2x = \frac{20x}{r^3}$

At $(1, 0, 0)$: $E_x = \frac{20 \times 1}{1} = 20$ V/m

By symmetry at this point: $E_y = E_z = 0$.

$\vec{E} = 20\hat{x}$ V/m. This matches $E = kQ/r^2 = 20/1 = 20$ V/m.  ✓
</details>

---

### Checkpoint 2: The Gauntlet — "The Voltage Landscape"

*A physicist measures the potential at various points in a laboratory and finds the empirical formula: $V = 3x^2 + 4y$ (with $V$ in volts, $x$ and $y$ in meters).*

**Problem 1:** Find $\vec{E}$ at any general point $(x, y)$.

<details><summary><b>Solution</b></summary>

$E_x = -\frac{\partial V}{\partial x} = -6x$

$E_y = -\frac{\partial V}{\partial y} = -4$

$E_z = -\frac{\partial V}{\partial z} = 0$

$\vec{E} = \textbf{-6x}\hat{x} + \textbf{(-4)}\hat{y}$ V/m
</details>

**Problem 2:** Is this a uniform field? Justify.

<details><summary><b>Solution</b></summary>

**No.** The $x$-component of the field ($-6x$) depends on position. The field varies from point to point. Only the $y$-component ($-4$) is constant.

A uniform field would require all components to be constant everywhere.
</details>

**Problem 3:** At what point(s) is the electric field purely in the $y$-direction?

<details><summary><b>Solution</b></summary>

For $\vec{E}$ to be purely in the $y$-direction, $E_x = 0$:

$-6x = 0 \implies x = 0$

Along the entire $y$-axis ($x = 0$), the field is $\vec{E} = -4\hat{y}$ V/m (uniform and vertical).
</details>

**Problem 4:** What is the magnitude of $\vec{E}$ at the point $(2, 3)$?

<details><summary><b>Solution</b></summary>

$E_x = -6(2) = -12$ V/m

$E_y = -4$ V/m

$|\vec{E}| = \sqrt{(-12)^2 + (-4)^2} = \sqrt{144 + 16} = \sqrt{160} = \textbf{4√10 ≈ 12.65 V/m}$
</details>

---

### Checkpoint 3: From Field to Potential

**Problem 1:** The electric field in a region is $\vec{E} = -30\hat{x}$ V/m (uniform). Find the potential difference between the origin $(0,0)$ and the point $(2, 0)$.

<details><summary><b>Solution</b></summary>

$V(2) - V(0) = -\int_0^2 E_x \, dx = -\int_0^2 (-30) \, dx = +30 \times 2 = \textbf{+60 V}$

The point $(2, 0)$ is at higher potential. This makes sense: $\vec{E}$ points in the $-x$ direction, meaning potential *increases* in the $+x$ direction.
</details>

**Problem 2:** In a certain region, $\vec{E} = (5\hat{x} + 3\hat{y})$ V/m (uniform). Find the potential difference $V_A - V_B$, where $A = (1, 2)$ m and $B = (3, 4)$ m.

<details><summary><b>Solution</b></summary>

For a uniform field:

$V_A - V_B = -\vec{E} \cdot (\vec{r}_A - \vec{r}_B)$

$\vec{r}_A - \vec{r}_B = (1 - 3)\hat{x} + (2 - 4)\hat{y} = -2\hat{x} - 2\hat{y}$

$V_A - V_B = -(5\hat{x} + 3\hat{y}) \cdot (-2\hat{x} - 2\hat{y}) = -(-10 - 6) = \textbf{+16 V}$

Point A is at higher potential than B.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** The electric potential in a region varies as $V = 2x^2 - 4y^2$ volts, where $x$ and $y$ are in meters.

(a) Find $\vec{E}$ at the point $(1, 1)$.  
(b) What is the magnitude and direction of $\vec{E}$ at $(1, 1)$?  
(c) A proton is placed at $(1, 1)$. In which direction does it begin to accelerate?  
(d) Find the equipotential curve passing through $(1, 1)$. What shape is it?  
(e) Verify that $\vec{E}$ at $(1, 1)$ is perpendicular to the equipotential curve at that point.

<details><summary><b>Solution</b></summary>

**(a)** 
$E_x = -\frac{\partial V}{\partial x} = -4x \implies E_x(1,1) = -4$ V/m

$E_y = -\frac{\partial V}{\partial y} = +8y \implies E_y(1,1) = +8$ V/m

$\vec{E} = \textbf{-4}\hat{x} + \textbf{8}\hat{y}$ V/m

**(b)** 
$|\vec{E}| = \sqrt{16 + 64} = \sqrt{80} = \textbf{4√5 ≈ 8.94 V/m}$

Direction: $\tan\alpha = E_y/E_x = 8/(-4) = -2$. The angle from the positive x-axis is in the second quadrant: $\alpha = 180° - \arctan(2) \approx 180° - 63.4° = \textbf{116.6°}$.

**(c)** A proton (positive charge) accelerates in the direction of $\vec{E}$: at $\textbf{116.6°}$ from the positive x-axis — that is, towards the upper-left.

**(d)** The equipotential through $(1,1)$: $V(1,1) = 2(1) - 4(1) = -2$ V.

The curve $2x^2 - 4y^2 = -2$, or $x^2 - 2y^2 = -1$, or equivalently:

$\frac{y^2}{1/2} - \frac{x^2}{1} = 1$

This is a **hyperbola** with the transverse axis along the y-axis.

**(e)** The gradient of the equipotential curve $2x^2 - 4y^2 = -2$ is found by implicit differentiation:

$4x - 8y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = \frac{4x}{8y} = \frac{x}{2y}$

At $(1, 1)$: slope of equipotential $= 1/2$.

The direction of $\vec{E}$ has slope $= E_y/E_x = 8/(-4) = -2$.

Product of slopes: $(1/2) \times (-2) = -1$. ✓

Since the product of slopes is $-1$, the field is **perpendicular** to the equipotential curve, as required.
</details>

---

## Question Bank — Chapter 6

### Section A: MCQs (15 Questions)

**Q1.** The relation between electric field and potential is:

(a) $E = V/r$ &emsp; (b) $E = -dV/dr$ &emsp; (c) $E = dV/dr$ &emsp; (d) $E = V\cdot r$

<details><summary><b>Answer</b></summary>**(b)** $E = -dV/dr$ — the field is the negative gradient of potential.</details>

---

**Q2.** In a uniform electric field of $200$ V/m, the potential difference between two points $5$ cm apart (along field lines) is:

(a) $40$ V &emsp; (b) $10$ V &emsp; (c) $4000$ V &emsp; (d) $1$ V

<details><summary><b>Answer</b></summary>**(b)** $\Delta V = E\times d = 200\times0.05 = 10$ V.</details>

---

**Q3.** If $V = 3x^2 + 5y$, the x-component of the electric field at $(2, 3)$ is:

(a) $-6$ V/m &emsp; (b) $6$ V/m &emsp; (c) $-12$ V/m &emsp; (d) $12$ V/m

<details><summary><b>Answer</b></summary>**(c)** $E_x = -\partial V/\partial x = -6x = -6(2) = -12$ V/m.</details>

---

**Q4.** The electric field in a region is zero. Which of the following is necessarily true?

(a) $V = 0$ &emsp; (b) $V = $ constant &emsp; (c) $V$ increases &emsp; (d) $V$ varies linearly

<details><summary><b>Answer</b></summary>**(b)** If $E = 0$ everywhere in a region, then $dV/dr = 0$, so $V$ is constant (could be any constant, not necessarily zero).</details>

---

**Q5.** For the relation $\vec{E} = -\nabla V$, the negative sign indicates:

(a) $\vec{E}$ and $V$ are in opposite directions &emsp; (b) $\vec{E}$ points from high to low potential &emsp; (c) $V$ is always negative &emsp; (d) Energy is always lost

<details><summary><b>Answer</b></summary>**(b)** The field points in the direction of decreasing potential (from high to low).</details>

---

**Q6.** The potential due to a point charge $V = kQ/r$. The electric field at distance $r$ is:

(a) $kQ/r$ &emsp; (b) $-kQ/r^2$ &emsp; (c) $kQ/r^2$ &emsp; (d) $-kQ/r$

<details><summary><b>Answer</b></summary>**(c)** $E = -dV/dr = -(-kQ/r^2) = kQ/r^2$ (magnitude; direction is radially outward for $+Q$).</details>

---

**Q7.** The potential gradient ($dV/dr$) has SI units of:

(a) V &emsp; (b) V/m = N/C &emsp; (c) V·m &emsp; (d) J/C²

<details><summary><b>Answer</b></summary>**(b)** $dV/dr$ has units V/m, which equals N/C (the unit of electric field).</details>

---

**Q8.** If $V = 5$ (constant everywhere), the electric field is:

(a) $5$ V/m &emsp; (b) $-5$ V/m &emsp; (c) $0$ &emsp; (d) Undefined

<details><summary><b>Answer</b></summary>**(c)** $E = -dV/dr = 0$ when $V$ is constant.</details>

---

**Q9.** The potential in a region varies as $V = 10 - 3x$. The electric field is:

(a) $-3\hat{x}$ V/m &emsp; (b) $3\hat{x}$ V/m &emsp; (c) $10\hat{x}$ V/m &emsp; (d) $-10\hat{x}$ V/m

<details><summary><b>Answer</b></summary>**(b)** $E_x = -dV/dx = -(-3) = +3$ V/m. $\vec{E} = 3\hat{x}$ V/m.</details>

---

**Q10.** The work done by the electric field in moving charge $q$ from potential $V_1$ to $V_2$ is:

(a) $q(V_2 - V_1)$ &emsp; (b) $q(V_1 - V_2)$ &emsp; (c) $(V_1 - V_2)/q$ &emsp; (d) $(V_2 - V_1)/q$

<details><summary><b>Answer</b></summary>**(b)** $W_{field} = q(V_1 - V_2)$. Positive when moving from high to low potential.</details>

---

**Q11.** In a uniform field $\vec{E} = E_0\hat{x}$, the potential difference $V(0) - V(d)$ is:

(a) $-E_0 d$ &emsp; (b) $E_0 d$ &emsp; (c) $0$ &emsp; (d) $E_0/d$

<details><summary><b>Answer</b></summary>**(b)** $V(0) - V(d) = E_0\times d$ (field points from high to low, so $V(0) > V(d)$ if field is in $+x$ direction).</details>

---

**Q12.** A potential function $V = ax^2 + by^2$ gives a zero electric field at:

(a) $(a/b, 0)$ &emsp; (b) $(0, 0)$ &emsp; (c) $(a, b)$ &emsp; (d) Everywhere

<details><summary><b>Answer</b></summary>**(b)** $E_x = -2ax$, $E_y = -2by$. Both are zero only at the origin $(0,0)$.</details>

---

**Q13.** The electric potential decreases in the direction of:

(a) Electric field &emsp; (b) Electric force on a negative charge &emsp; (c) Increasing charge density &emsp; (d) Increasing radius

<details><summary><b>Answer</b></summary>**(a)** $V$ decreases in the direction of $\vec{E}$ (since $E = -dV/dr$, field points toward decreasing $V$).</details>

---

**Q14.** If $V = 3x + 4y + 5z$, the magnitude of the electric field is:

(a) $\sqrt{3^2+4^2+5^2}$ V/m &emsp; (b) $(3+4+5)$ V/m &emsp; (c) $\sqrt{9+16}$ V/m &emsp; (d) $5$ V/m

<details><summary><b>Answer</b></summary>**(a)** $\vec{E} = -(3\hat{x}+4\hat{y}+5\hat{z})$, $|E| = \sqrt{9+16+25} = \sqrt{50} = 5\sqrt{2}$ V/m.</details>

---

**Q15.** A potential function $V = 5/r^2$ gives an electric field that varies as:

(a) $1/r^2$ &emsp; (b) $1/r^3$ &emsp; (c) $1/r$ &emsp; (d) $r$

<details><summary><b>Answer</b></summary>**(b)** $E = -dV/dr = -(-10/r^3) = 10/r^3 \propto 1/r^3$.</details>

---

### Section B: Short Answer Questions

**Q16.** Derive the relation $E = -dV/dr$ starting from the definition of work done by the electric force.

<details><summary><b>Answer</b></summary>

Work done by electric field on unit positive charge displaced by $dr$: $dW = E\,dr$

By definition of potential: $dW = -dV$ (decrease in potential energy per unit charge)

Therefore: $E\,dr = -dV \Rightarrow E = -dV/dr$

For 3D: $\vec{E} = -\nabla V = -(\partial V/\partial x\,\hat{x} + \partial V/\partial y\,\hat{y} + \partial V/\partial z\,\hat{z})$
</details>

---

**Q17.** The potential in a region is $V = 4x^2 - 3y + 7z$. Find (a) $\vec{E}$, (b) the magnitude of $\vec{E}$ at $(1, 2, -1)$.

<details><summary><b>Answer</b></summary>

**(a)** $E_x = -8x$, $E_y = +3$, $E_z = -7$. $\vec{E} = -8x\hat{x}+3\hat{y}-7\hat{z}$ V/m

**(b)** At $(1,2,-1)$: $\vec{E} = -8\hat{x}+3\hat{y}-7\hat{z}$

$|E| = \sqrt{64+9+49} = \sqrt{122} \approx \mathbf{11.05\,\text{V/m}}$
</details>

---

**Q18.** The potential along the x-axis is $V = 5x^3 - 2x$. Find: (a) $E_x$ as a function of $x$, (b) the points where $E_x = 0$.

<details><summary><b>Answer</b></summary>

**(a)** $E_x = -dV/dx = -(15x^2-2) = 2-15x^2$

**(b)** $E_x = 0$: $2-15x^2 = 0 \Rightarrow x^2 = 2/15 \Rightarrow x = \pm\sqrt{2/15} = \pm0.365$ m
</details>

---

**Q19.** An electric field $\vec{E} = E_0(x\hat{x} + y\hat{y})$ exists in a region. Find the potential function $V(x, y)$ (choose $V = 0$ at the origin).

<details><summary><b>Answer</b></summary>

$E_x = -\partial V/\partial x = E_0 x \Rightarrow \partial V/\partial x = -E_0 x$

Integrating: $V = -E_0 x^2/2 + f(y)$

$E_y = -\partial V/\partial y = -f'(y) = E_0 y \Rightarrow f'(y) = -E_0 y \Rightarrow f(y) = -E_0 y^2/2 + C$

With $V(0,0) = 0$: $C = 0$.

$V(x,y) = -\frac{E_0}{2}(x^2+y^2) = -\frac{E_0 r^2}{2}$
</details>

---

**Q20.** In the relation $\vec{E} = -\nabla V$: (a) can $V$ be positive where $\vec{E}$ is nonzero? (b) can $V$ be zero where $\vec{E}$ is nonzero? Give examples.

<details><summary><b>Answer</b></summary>

**(a) Yes.** Inside a positively charged conductor: $V = kQ/R > 0$, but $E = 0$.

Actually the question asks if $V > 0$ where $E \neq 0$: Yes. Around a positive charge, $V = kQ/r > 0$ and $E = kQ/r^2 \neq 0$ everywhere outside.

**(b) Yes.** On the equatorial plane of a dipole, $V = 0$ but $E = kp/r^3 \neq 0$. Also at the midpoint between a $+q$ and $-q$ charge: $V = 0$, $E \neq 0$.
</details>

---

**Q21.** The potential at a distance $r$ from the center of a non-conducting sphere of radius $R$ and uniform charge density $\rho$ is $V = \frac{\rho}{6\epsilon_0}(3R^2-r^2)$ for $r \leq R$. Find the field inside.

<details><summary><b>Answer</b></summary>

$E = -dV/dr = -\frac{\rho}{6\epsilon_0}(0-2r) = \frac{\rho r}{3\epsilon_0}$

This is directed radially outward. It equals $E = \rho r/(3\epsilon_0) = Qr/(4\pi\epsilon_0 R^3)$, which matches the result from Gauss's law for a uniformly charged sphere. ✓
</details>

---

**Q22.** A potential $V = -3x^2 + 4y^2 - 2z$ V is given. Find: (a) $\vec{E}$ at $(1,1,1)$, (b) the surface on which $V = 0$ passing through the origin.

<details><summary><b>Answer</b></summary>

**(a)** $E_x = 6x = 6$, $E_y = -8y = -8$, $E_z = 2$

$\vec{E} = 6\hat{x}-8\hat{y}+2\hat{z}$ V/m; $|E| = \sqrt{36+64+4} = \sqrt{104} \approx 10.2$ V/m

**(b)** $V = 0$: $-3x^2+4y^2-2z = 0$, i.e., $z = 2y^2 - \frac{3}{2}x^2$ — a saddle surface passing through the origin.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** The electric field in a region is $\vec{E} = (2x\hat{x} + 3y\hat{y})$ V/m. Find: (a) the potential $V(x,y)$ with $V(0,0) = 0$, (b) $V$ at $(3, 4)$, (c) work done to bring $+2\,\mu C$ from $(0,0)$ to $(3,4)$.

<details><summary><b>Answer</b></summary>

**(a)** From $E_x = -\partial V/\partial x = 2x$: $V = -x^2 + f(y)$

From $E_y = -\partial V/\partial y = 3y$: $f'(y) = -3y \Rightarrow f(y) = -3y^2/2$

$V(x,y) = -x^2 - \frac{3y^2}{2}$

Check: $V(0,0) = 0$ ✓

**(b)** $V(3,4) = -9 - 24 = -33$ V

**(c)** $W_{ext} = q\Delta V = 2\times10^{-6}\times(-33-0) = \mathbf{-6.6\times10^{-5}\,J = -66\,\mu J}$

(The field does positive work; external agent restrains the charge.)
</details>

---

**Q24.** Prove that for a point charge $Q$: (a) $V = kQ/r$, (b) $E = kQ/r^2$ can be derived from (a) using $E = -dV/dr$.

<details><summary><b>Answer</b></summary>

**(a)** $V = kQ/r$ derived in Chapter 2 by integration of force.

**(b)** $E = -\frac{dV}{dr} = -\frac{d}{dr}\left(\frac{kQ}{r}\right) = -kQ\times\left(-\frac{1}{r^2}\right) = \frac{kQ}{r^2}$ ✓

This confirms the consistency of the two definitions and shows that knowing $V$ is equivalent to knowing $E$.
</details>

---

**Q25.** The potential in a spherically symmetric field varies as $V = A/r + Br^2$. Find (a) $E(r)$, (b) what physical charge distributions could produce each term.

<details><summary><b>Answer</b></summary>

**(a)** $E = -dV/dr = A/r^2 - 2Br$

**(b)** - The $A/r$ term gives $E_1 = A/r^2$: this is the field of a **point charge** at the origin (with $A = kQ$).

- The $Br^2$ term gives $E_2 = -2Br$: this is linear in $r$, characteristic of a **uniform volume charge density** (like inside a uniformly charged sphere, where $E \propto r$).

So the total field is the superposition of a point charge and a surrounding uniform charge distribution.
</details>

---

**Q26.** Given $V = 10\sin(\pi x)\cos(\pi y)$, find: (a) $\vec{E}$ everywhere, (b) all points where $\vec{E} = 0$.

<details><summary><b>Answer</b></summary>

**(a)** $E_x = -\partial V/\partial x = -10\pi\cos(\pi x)\cos(\pi y)$

$E_y = -\partial V/\partial y = +10\pi\sin(\pi x)\sin(\pi y)$

**(b)** $E_x = 0$: $\cos(\pi x)\cos(\pi y) = 0$, i.e., $x = (2n+1)/2$ or $y = (2m+1)/2$

$E_y = 0$: $\sin(\pi x)\sin(\pi y) = 0$, i.e., $x = n$ or $y = m$ (integers)

Both simultaneously: $x = n$ (integer) AND $y = (2m+1)/2$ (half-integer), or $y = m$ (integer) AND $x = (2n+1)/2$ (half-integer).

These form a grid of saddle points in the xy-plane.
</details>

---

**Q27.** Two infinite parallel plates are at $x = 0$ ($V = 0$) and $x = d$ ($V = V_0$). Derive the field between them from the potential, and show it equals $V_0/d$.

<details><summary><b>Answer</b></summary>

Between the plates, the potential must satisfy Laplace's equation ($\nabla^2 V = 0$, no charges between plates):

$\frac{d^2V}{dx^2} = 0 \Rightarrow V = Ax + B$

Boundary conditions: $V(0) = 0 \Rightarrow B = 0$; $V(d) = V_0 \Rightarrow A = V_0/d$

$V(x) = V_0 x/d$

$E_x = -dV/dx = -V_0/d$

The field is uniform with magnitude $V_0/d$, pointing from high to low potential (from $x = d$ to $x = 0$ if $V_0 > 0$). ✓
</details>

---

**Q28.** The potential in a region is $V = Ax^2y^3z$ where $A$ is a constant. Find: (a) all three field components, (b) the field at $(1,1,1)$, (c) is the Laplace equation satisfied ($\nabla^2 V = 0$)?

<details><summary><b>Answer</b></summary>

**(a)** $E_x = -2Axy^3z$; $E_y = -3Ax^2y^2z$; $E_z = -Ax^2y^3$

**(b)** At $(1,1,1)$: $\vec{E} = -2A\hat{x}-3A\hat{y}-A\hat{z}$

$|E| = A\sqrt{4+9+1} = A\sqrt{14}$

**(c)** $\partial^2V/\partial x^2 = 2Ay^3z$; $\partial^2V/\partial y^2 = 6Ax^2yz$; $\partial^2V/\partial z^2 = 0$

$\nabla^2 V = 2Ay^3z + 6Ax^2yz \neq 0$ (generally). Laplace's equation is NOT satisfied — there are charges in this region.
</details>

---

**Q29.** The electric field along the axis of a uniformly charged ring (radius $a$, charge $Q$) is $E = kQx/(x^2+a^2)^{3/2}$. Find the potential at axial distance $x$ by integration.

<details><summary><b>Answer</b></summary>

$V(x) = -\int_\infty^x E\,dx' = \int_x^\infty \frac{kQx'}{(x'^2+a^2)^{3/2}}\,dx'$

Let $u = x'^2+a^2$, $du = 2x'\,dx'$:

$V = \frac{kQ}{2}\int_{x^2+a^2}^\infty u^{-3/2}\,du = \frac{kQ}{2}\left[\frac{-2}{\sqrt{u}}\right]_{x^2+a^2}^\infty = \frac{kQ}{\sqrt{x^2+a^2}}$

This is the standard result for the axial potential of a charged ring. ✓
</details>

---

**Q30.** If $V(r)$ is spherically symmetric and $E(r) = c/r^n$ for some constants $c$ and $n$, find $V(r)$ in terms of $c$, $n$, and $r$.

<details><summary><b>Answer</b></summary>

$E = -dV/dr = c/r^n \Rightarrow dV/dr = -c/r^n$

$V(r) = -c\int r^{-n}\,dr = -c\times\frac{r^{-n+1}}{-n+1} + C = \frac{c}{(n-1)r^{n-1}} + C$ (for $n \neq 1$)

Setting $V(\infty) = 0$: $C = 0$.

$V(r) = \frac{c}{(n-1)r^{n-1}}$

For $n = 2$ (point charge): $V = c/r = kQ/r$ ✓

For $n = 3$ (dipole field): $V = c/(2r^2)$, which is consistent with $V_{axial} \propto 1/r^2$ ✓
</details>

---

**Q31.** A $+5\,\mu C$ charge is at the origin. Using the relation $E = -dV/dr$, calculate: (a) $V$ at $r = 0.3$ m, (b) $E$ at $r = 0.3$ m, (c) the rate of change of $V$ with $r$ at this point.

<details><summary><b>Answer</b></summary>

**(a)** $V = kQ/r = 9\times10^9\times5\times10^{-6}/0.3 = \mathbf{150{,}000\,V}$

**(b)** $E = kQ/r^2 = 9\times10^9\times5\times10^{-6}/0.09 = \mathbf{500{,}000\,V/m}$

**(c)** $dV/dr = -E = \mathbf{-500{,}000\,V/m}$ (potential decreases at 500,000 V per metre as $r$ increases)
</details>

---

**Q32.** The work done in moving charge $+q$ from point A $(V_A = 200$ V) to B $(V_B = 100$ V) is $W_1$. Then from B to C $(V_C = 300$ V) is $W_2$. Compare $W_1$ and $W_2$, and find the work done if the charge went directly from A to C.

<details><summary><b>Answer</b></summary>

$W_1 = q(V_A-V_B) = q(200-100) = 100q$

$W_2 = q(V_B-V_C) = q(100-300) = -200q$

$W_{A\to C} = q(V_A-V_C) = q(200-300) = -100q$

Also: $W_1 + W_2 = 100q + (-200q) = -100q = W_{A\to C}$ ✓

This confirms that the work by the electrostatic field depends only on the initial and final positions, not the path (conservative force property).
</details>

---

*Next: [Chapter 7 — Potential Energy of a System of Charges →](./07_potential_energy_system.md)*
