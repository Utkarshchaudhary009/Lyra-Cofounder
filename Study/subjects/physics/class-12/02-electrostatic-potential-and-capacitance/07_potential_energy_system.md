# Chapter 7: Potential Energy of a System of Charges

> *NCERT Section 2.7*

---

### The Story of the Cost of Assembly

Imagine you are building a house of magnets. The first magnet costs you nothing to place — there's nothing around to push or pull against. But the second magnet requires effort: as you bring it close to the first, you must either push against repulsion or restrain against attraction. The third magnet interacts with *both* the first and second — more work. By the time you place the tenth magnet, you are fighting against nine others simultaneously.

The total "cost of construction" — the sum of all the work you did placing every magnet — is the **potential energy** of the system. This energy is real: if you release the magnets, they will fly apart (or together), and the kinetic energy they gain will exactly equal the potential energy you invested.

Electric charges behave identically. The potential energy of a system of charges is the total work required to assemble the configuration, bringing each charge from infinity to its position, one at a time.

---

### Building the Concept

#### Two Charges

Bringing the first charge $Q_1$ to its position costs nothing (no other charges exist yet):

$$W_1 = 0$$

Bringing the second charge $Q_2$ to a distance $r_{12}$ from $Q_1$ requires work against $Q_1$'s field:

$$W_2 = Q_2 \times V_1(r_{12}) = Q_2 \times \frac{kQ_1}{r_{12}} = \frac{kQ_1 Q_2}{r_{12}}$$

The total potential energy of the two-charge system:

$$\boxed{U = \frac{1}{4\pi\epsilon_0} \frac{Q_1 Q_2}{r_{12}}}$$

| Sign of $Q_1 Q_2$ | $U$ | Physical Meaning |
|:------------------:|:---:|:-----------------|
| $+$ (like charges) | $U > 0$ | Energy was *invested* to push them together; they repel |
| $-$ (unlike charges) | $U < 0$ | Energy was *released* as they attracted; they attract |

> **Critical Insight:** When $U > 0$, the system "wants" to fly apart. When $U < 0$, the system "wants" to stay together. The sign of $U$ tells you the stability of the configuration.

#### Three Charges

For three charges $Q_1, Q_2, Q_3$ at mutual distances $r_{12}, r_{13}, r_{23}$:

$$U = \frac{k Q_1 Q_2}{r_{12}} + \frac{k Q_1 Q_3}{r_{13}} + \frac{k Q_2 Q_3}{r_{23}}$$

This is the sum of potential energies of **all unique pairs**. For $n$ charges, there are $\frac{n(n-1)}{2}$ pairs.

#### General Formula for $n$ Charges

$$\boxed{U = \frac{1}{2} \sum_{i=1}^{n} \sum_{\substack{j=1 \\ j \neq i}}^{n} \frac{k Q_i Q_j}{r_{ij}}}$$

The factor of $1/2$ compensates for the double-counting (pair $ij$ and pair $ji$ are the same).

| Number of charges | Number of pairs |
|:-:|:-:|
| 2 | 1 |
| 3 | 3 |
| 4 | 6 |
| 5 | 10 |
| $n$ | $n(n-1)/2$ |

---

### Checkpoint 1: Two-Charge Systems

**The Nuclear Physicist's Problem:** *A nuclear physicist needs to calculate the energy required to bring two protons close together, overcoming their electrostatic repulsion.*

**Problem 1:** Two protons are $10^{-15}$ m apart (roughly the size of a nucleus). What is the electrostatic potential energy of this system?

<details><summary><b>Solution</b></summary>

$U = \frac{kQ_1 Q_2}{r} = \frac{9 \times 10^9 \times (1.6 \times 10^{-19})^2}{10^{-15}}$

$U = \frac{9 \times 10^9 \times 2.56 \times 10^{-38}}{10^{-15}} = 9 \times 2.56 \times 10^{-14}$

$U = 23.04 \times 10^{-14} = \textbf{2.3 × 10⁻¹³ J}$

In eV: $U = \frac{2.3 \times 10^{-13}}{1.6 \times 10^{-19}} = \textbf{1.44 × 10⁶ eV ≈ 1.44 MeV}$

This is the *Coulomb barrier* — the energy required to push two protons close enough for the nuclear force to take over. This is why nuclear fusion requires temperatures of millions of degrees.
</details>

**Problem 2:** What is the potential energy of a proton-electron pair in a hydrogen atom, where the average separation is $5.3 \times 10^{-11}$ m (the Bohr radius)?

<details><summary><b>Solution</b></summary>

$U = \frac{k \times (+e) \times (-e)}{r} = \frac{-k e^2}{r}$

$U = \frac{-9 \times 10^9 \times (1.6 \times 10^{-19})^2}{5.3 \times 10^{-11}}$

$U = \frac{-2.304 \times 10^{-28}}{5.3 \times 10^{-11}} = \textbf{-4.35 × 10⁻¹⁸ J ≈ -27.2 eV}$

Negative energy — the system is bound. You would need to supply 27.2 eV to separate the electron and proton completely. This is closely related to the ionization energy of hydrogen (13.6 eV), with the difference accounted for by the kinetic energy of the orbiting electron.
</details>

---

### Checkpoint 2: Three-Charge Systems

**Problem 1:** Three charges of $+1 \mu C$ each are placed at the corners of an equilateral triangle of side $1$ m. Find the total potential energy of the system.

<details><summary><b>Solution</b></summary>

There are 3 pairs, all with the same charge product and same distance.

$U = 3 \times \frac{k Q^2}{a} = 3 \times \frac{9 \times 10^9 \times (10^{-6})^2}{1}$

$U = 3 \times 9 \times 10^{-3} = \textbf{27 × 10⁻³ J = 27 mJ}$

Positive — the configuration is unstable. The charges repel each other and would fly apart if released.
</details>

**Problem 2:** The charges are now $+1\mu C$, $+1\mu C$, $-1\mu C$ at corners A, B, C of the same triangle. Find $U$.

<details><summary><b>Solution</b></summary>

Pairs:
- $Q_A Q_B$: $(+1)(+1) = +1 \mu C^2$, $r = 1$ m → $U_{AB} = +9 \times 10^{-3}$ J
- $Q_A Q_C$: $(+1)(-1) = -1 \mu C^2$, $r = 1$ m → $U_{AC} = -9 \times 10^{-3}$ J
- $Q_B Q_C$: $(+1)(-1) = -1 \mu C^2$, $r = 1$ m → $U_{BC} = -9 \times 10^{-3}$ J

$U = 9 - 9 - 9 = \textbf{-9 × 10⁻³ J = -9 mJ}$

Negative — this configuration is bound (more stable than the all-positive case).
</details>

**Problem 3:** Four charges $+q, +q, +q, +q$ are placed at the corners of a square of side $a$. Find the total potential energy.

<details><summary><b>Solution</b></summary>

There are $\binom{4}{2} = 6$ pairs.

4 pairs along the sides (distance $a$): $U_{side} = 4 \times \frac{kq^2}{a}$

2 pairs along the diagonals (distance $a\sqrt{2}$): $U_{diag} = 2 \times \frac{kq^2}{a\sqrt{2}}$

$U = \frac{kq^2}{a}\left(4 + \frac{2}{\sqrt{2}}\right) = \frac{kq^2}{a}(4 + \sqrt{2})$

$U = \textbf{\frac{kq²}{a}(4 + √2) ≈ 5.414 × kq²/a}$
</details>

---

### Checkpoint 3: The Gauntlet — "The Energy of Assembly"

*A student is assembling a charge configuration in a lab, bringing charges one at a time from infinity.*

**Problem 1:** She places $Q_1 = +2\mu C$ at the origin. How much work does this take?

<details><summary><b>Solution</b></summary>

$W_1 = \textbf{0}$ (no other charges to interact with).
</details>

*She now brings $Q_2 = +3\mu C$ to a point $0.5$ m from $Q_1$.*

**Problem 2:** How much work does this require?

<details><summary><b>Solution</b></summary>

$W_2 = \frac{kQ_1 Q_2}{r_{12}} = \frac{9 \times 10^9 \times 2 \times 10^{-6} \times 3 \times 10^{-6}}{0.5}$

$W_2 = \frac{54 \times 10^{-3}}{0.5} = \textbf{0.108 J = 108 mJ}$
</details>

*Finally, she brings $Q_3 = -1\mu C$ to a point that is $0.5$ m from $Q_1$ and $0.5$ m from $Q_2$.*

**Problem 3:** How much work does bringing $Q_3$ require?

<details><summary><b>Solution</b></summary>

$Q_3$ interacts with both $Q_1$ and $Q_2$:

$W_3 = \frac{kQ_1 Q_3}{r_{13}} + \frac{kQ_2 Q_3}{r_{23}}$

$W_3 = \frac{9 \times 10^9 \times 2 \times 10^{-6} \times (-1 \times 10^{-6})}{0.5} + \frac{9 \times 10^9 \times 3 \times 10^{-6} \times (-1 \times 10^{-6})}{0.5}$

$W_3 = -0.036 + (-0.054) = \textbf{-0.090 J = -90 mJ}$

Negative work — the field *assists* bringing the negative charge in (it's attracted to both positive charges).
</details>

**Problem 4:** What is the total potential energy of the assembled system?

<details><summary><b>Solution</b></summary>

$U = W_1 + W_2 + W_3 = 0 + 0.108 + (-0.090) = \textbf{0.018 J = 18 mJ}$

Alternatively, summing all three pairs:
$U = \frac{kQ_1 Q_2}{r_{12}} + \frac{kQ_1 Q_3}{r_{13}} + \frac{kQ_2 Q_3}{r_{23}} = 108 - 36 - 54 = 18$ mJ ✓
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** Four charges are placed at the corners of a square of side $a$:
- $Q$ at $(0, 0)$
- $-Q$ at $(a, 0)$
- $Q$ at $(a, a)$
- $-Q$ at $(0, a)$

(a) Find the total potential energy of the system.  
(b) What charge $q$ should be placed at the center of the square so that the entire system is in equilibrium (net force on each charge is zero)?  
(c) Is this equilibrium stable or unstable?

<details><summary><b>Solution</b></summary>

**(a)** There are 6 pairs:

**Side pairs** (4 of them, each with distance $a$):
- $(Q)(-Q)$: appears 4 times → $U_{sides} = 4 \times \frac{k(Q)(-Q)}{a} = \frac{-4kQ^2}{a}$

**Diagonal pairs** (2 of them, each with distance $a\sqrt{2}$):
- $(Q)(Q)$: one diagonal → $\frac{kQ^2}{a\sqrt{2}}$
- $(-Q)(-Q)$: other diagonal → $\frac{k(-Q)(-Q)}{a\sqrt{2}} = \frac{kQ^2}{a\sqrt{2}}$

$U_{diag} = 2 \times \frac{kQ^2}{a\sqrt{2}} = \frac{2kQ^2}{a\sqrt{2}} = \frac{\sqrt{2}kQ^2}{a}$

$U = -\frac{4kQ^2}{a} + \frac{\sqrt{2}kQ^2}{a} = \frac{kQ^2}{a}(\sqrt{2} - 4)$

$U = \textbf{\frac{kQ²}{a}(√2 - 4) ≈ -2.586 × kQ²/a}$

Negative — the system is bound overall.

**(b)** Place charge $q$ at the center. The center is at distance $a\sqrt{2}/2 = a/\sqrt{2}$ from each corner.

For equilibrium, the net force on each corner charge must be zero. Consider the charge $+Q$ at $(0,0)$. The forces on it are:
- From $-Q$ at $(a, 0)$: attractive, along $+x$
- From $Q$ at $(a, a)$: repulsive, along the diagonal (at $45°$) 
- From $-Q$ at $(0, a)$: attractive, along $+y$
- From $q$ at center: along the diagonal to the center

By symmetry, the net force from the 3 corner charges on the corner $+Q$ is along the diagonal towards the center. The central charge $q$ must provide a force equal and opposite (repulsive — away from center). So $q$ must be negative.

By detailed force balance (summing all components):

$q = \frac{-Q}{4}(1 + 2\sqrt{2})$

$q = \textbf{\frac{-Q(1 + 2√2)}{4}}$

**(c)** The equilibrium is **unstable**. If the central charge is displaced slightly along a diagonal, it will not return. This is a consequence of Earnshaw's theorem — stable equilibrium is impossible in electrostatics alone. The system has a saddle point, not a minimum.
</details>

---

## Question Bank — Chapter 7

### Section A: MCQs (15 Questions)

**Q1.** The potential energy of a system of two charges $Q_1$ and $Q_2$ separated by $r$ is:

(a) $kQ_1Q_2r$ &emsp; (b) $kQ_1Q_2/r$ &emsp; (c) $k(Q_1+Q_2)/r$ &emsp; (d) $kQ_1Q_2/r^2$

<details><summary><b>Answer</b></summary>**(b)** $U = kQ_1Q_2/r$</details>

---

**Q2.** The work done to assemble three equal charges $+q$ at the vertices of an equilateral triangle of side $a$ is:

(a) $kq^2/a$ &emsp; (b) $2kq^2/a$ &emsp; (c) $3kq^2/a$ &emsp; (d) $6kq^2/a$

<details><summary><b>Answer</b></summary>**(c)** 3 pairs, each contributing $kq^2/a$: Total $= 3kq^2/a$.</details>

---

**Q3.** The potential energy of a system is negative. This means:

(a) The system is unstable &emsp; (b) The charges repel &emsp; (c) The system is bound (attractive) &emsp; (d) Energy was released in assembling

<details><summary><b>Answer</b></summary>**(c) and (d)** Negative potential energy means the system is bound (charges attract) and energy was released during assembly.</details>

---

**Q4.** Two charges $+q$ and $-q$ are $r$ apart. Their potential energy is:

(a) $kq^2/r$ &emsp; (b) $-kq^2/r$ &emsp; (c) $0$ &emsp; (d) $2kq^2/r$

<details><summary><b>Answer</b></summary>**(b)** $U = k(+q)(-q)/r = -kq^2/r$</details>

---

**Q5.** When two positive charges are brought closer, the potential energy:

(a) Decreases &emsp; (b) Increases &emsp; (c) Remains the same &emsp; (d) Becomes negative

<details><summary><b>Answer</b></summary>**(b)** $U = kq_1q_2/r$ with $q_1q_2 > 0$. As $r$ decreases, $U$ increases.</details>

---

**Q6.** The number of pairs in a system of 5 charges is:

(a) 5 &emsp; (b) 10 &emsp; (c) 15 &emsp; (d) 20

<details><summary><b>Answer</b></summary>**(b)** $\binom{5}{2} = 10$ pairs.</details>

---

**Q7.** The SI unit of electric potential energy is:

(a) N·C &emsp; (b) V/C &emsp; (c) J &emsp; (d) C/V

<details><summary><b>Answer</b></summary>**(c)** Joule (J).</details>

---

**Q8.** A charge $+q$ is brought from infinity to a point where the potential (due to other charges) is $V$. The work done by the external agent is:

(a) $qV/2$ &emsp; (b) $qV$ &emsp; (c) $-qV$ &emsp; (d) $q^2V$

<details><summary><b>Answer</b></summary>**(b)** $W_{ext} = q(V_{final}-V_{initial}) = q(V-0) = qV$</details>

---

**Q9.** The potential energy of two protons $1$ fm ($10^{-15}$ m) apart is approximately:

(a) $1.44$ eV &emsp; (b) $1.44$ keV &emsp; (c) $1.44$ MeV &emsp; (d) $1.44$ GeV

<details><summary><b>Answer</b></summary>**(c)** $U = ke^2/r = 9\times10^9\times(1.6\times10^{-19})^2/10^{-15} \approx 2.3\times10^{-13}$ J $\approx 1.44$ MeV.</details>

---

**Q10.** When two identical conducting spheres, one charged and one uncharged, are touched and separated, the potential energy of the system:

(a) Doubles &emsp; (b) Halves &emsp; (c) Remains same &emsp; (d) Quadruples

<details><summary><b>Answer</b></summary>**(b)** After touching, each has $Q/2$. Original $U = kQ^2/r$. Final $U = k(Q/2)^2/r = kQ^2/(4r) = U/4$... Wait: original is one charged, one uncharged — no interaction energy. After: $U = k(Q/2)(Q/2)/r = kQ^2/(4r)$. If original $U = 0$ (uncharged sphere), PE increases to $kQ^2/(4r)$.</details>

---

**Q11.** Three charges in a straight line with equal separations $d$: $+q$, $+q$, $+q$. The total potential energy is:

(a) $3kq^2/d$ &emsp; (b) $2.5kq^2/d$ &emsp; (c) $kq^2/d$ &emsp; (d) $4kq^2/d$

<details><summary><b>Answer</b></summary>**(b)** Pairs: $(1,2)$ at $d$: $kq^2/d$; $(2,3)$ at $d$: $kq^2/d$; $(1,3)$ at $2d$: $kq^2/2d$. Total $= 2kq^2/d + kq^2/2d = 2.5kq^2/d$.</details>

---

**Q12.** The minimum energy of two charges of opposite sign (equal magnitude) is achieved when:

(a) They are infinitely far apart &emsp; (b) They are at the same point &emsp; (c) They form a dipole &emsp; (d) At a specific intermediate distance

<details><summary><b>Answer</b></summary>**(b)** $U = -kq^2/r \to -\infty$ as $r \to 0$. The minimum energy is at $r = 0$ (practically, this is where quantum effects take over).</details>

---

**Q13.** The work done in rotating a dipole from $\theta = 0°$ to $\theta = 90°$ in a uniform field is:

(a) $0$ &emsp; (b) $pE$ &emsp; (c) $2pE$ &emsp; (d) $-pE$

<details><summary><b>Answer</b></summary>**(b)** $W = pE(\cos\theta_1-\cos\theta_2) = pE(\cos0°-\cos90°) = pE(1-0) = pE$.</details>

---

**Q14.** The self-energy of a charge $q$ (energy required to assemble the charge from scratch) is:

(a) Zero (infinite, actually) &emsp; (b) $kq^2/R$ (for a sphere of radius $R$) &emsp; (c) $kq^2/(2R)$ &emsp; (d) Not defined in classical physics

<details><summary><b>Answer</b></summary>**(d)** The self-energy of a point charge diverges in classical electrostatics. It is only defined (as $kq^2/(2R)$) for a charge distributed on a sphere of radius $R$.</details>

---

**Q15.** A charge is slowly moved from a region of high potential to low potential by an external agent. The work done by the external agent is:

(a) Positive &emsp; (b) Negative &emsp; (c) Zero &emsp; (d) Cannot be determined

<details><summary><b>Answer</b></summary>**(b)** $W_{ext} = q\Delta V = q(V_f - V_i)$. For positive $q$ moving from high to low: $\Delta V < 0$, so $W_{ext} < 0$ (external agent opposes the motion).</details>

---

### Section B: Short Answer Questions

**Q16.** Find the potential energy of a system of three charges: $+3\,\mu C$ at origin, $-2\,\mu C$ at $(0.3, 0)$ m, and $+4\,\mu C$ at $(0, 0.4)$ m.

<details><summary><b>Answer</b></summary>

Distances: $r_{12} = 0.3$ m, $r_{13} = 0.4$ m, $r_{23} = \sqrt{0.09+0.16} = 0.5$ m.

$U = k\left[\frac{(3)(-2)\times10^{-12}}{0.3} + \frac{(3)(4)\times10^{-12}}{0.4} + \frac{(-2)(4)\times10^{-12}}{0.5}\right]$

$U = 9\times10^9\times10^{-12}[-6/0.3 + 12/0.4 - 8/0.5] = 9\times10^{-3}[-20+30-16] = 9\times10^{-3}\times(-6) = \mathbf{-54\,mJ}$
</details>

---

**Q17.** How much energy is released when a proton and electron (initially far apart) form a hydrogen atom with $r = 0.53$ Å?

<details><summary><b>Answer</b></summary>

$U = \frac{ke^2}{r} \times(-1) = -\frac{9\times10^9\times(1.6\times10^{-19})^2}{0.53\times10^{-10}} = -\frac{2.304\times10^{-28}}{0.53\times10^{-10}} = -4.35\times10^{-18}$ J

$= -27.2$ eV

Energy released $= 27.2$ eV (but actual ionization energy is 13.6 eV — the difference is the electron's kinetic energy, which must be subtracted from the total energy).
</details>

---

**Q18.** Four charges $+q$ at corners of a square of side $a$. Find the work done to bring a fifth charge $+Q$ from infinity to the center.

<details><summary><b>Answer</b></summary>

Center-to-corner distance $= a\sqrt{2}/2 = a/\sqrt{2}$.

$V_{center} = 4\times\frac{kq}{a/\sqrt{2}} = \frac{4\sqrt{2}kq}{a}$

$W = QV_{center} = \frac{4\sqrt{2}kqQ}{a}$
</details>

---

**Q19.** Explain why the potential energy of the universe is negative.

<details><summary><b>Answer</b></summary>

The universe contains both positive and negative charges. In their natural configuration (atoms with electrons bound to nuclei), opposite charges are close together — contributing large negative potential energies — while like charges are kept apart by those same attractive forces.

The net effect is that the universe's total electrostatic potential energy is enormously negative. This is actually a feature: it means the universe is a bound system, not a collection of free particles. The energy released in forming all atoms since the Big Bang represents the "descent" from a zero-energy (infinite separation) state to the current negative-energy configuration.
</details>

---

**Q20.** A system of two charges $+2\,\mu C$ and $+8\,\mu C$ are $4$ m apart. If the distance is halved, what is the new potential energy? What was the work done?

<details><summary><b>Answer</b></summary>

$U_i = k\times2\times10^{-6}\times8\times10^{-6}/4 = 9\times10^9\times16\times10^{-12}/4 = 36\times10^{-3}$ J $= 36$ mJ

$U_f = k\times2\times10^{-6}\times8\times10^{-6}/2 = 72$ mJ

$W_{ext} = \Delta U = 72-36 = \mathbf{36\,mJ}$

Work done = 36 mJ (positive — external agent pushes like charges together).
</details>

---

**Q21.** Show that for a system of $n$ charges, the total potential energy can be written as $U = \frac{1}{2}\sum_i q_i V_i$ where $V_i$ is the potential at the location of charge $q_i$ due to all other charges.

<details><summary><b>Answer</b></summary>

The total potential energy is the sum over all unique pairs:

$U = \sum_{i<j} \frac{kq_iq_j}{r_{ij}}$

Now consider $\frac{1}{2}\sum_i q_i V_i$ where $V_i = \sum_{j\neq i} kq_j/r_{ij}$:

$\frac{1}{2}\sum_i q_i V_i = \frac{1}{2}\sum_i q_i \sum_{j\neq i}\frac{kq_j}{r_{ij}} = \frac{1}{2}\sum_{i\neq j}\frac{kq_iq_j}{r_{ij}}$

The double sum over $i\neq j$ counts each pair $(i,j)$ twice (once as $(i,j)$ and once as $(j,i)$). The factor of $1/2$ corrects this:

$= \sum_{i<j}\frac{kq_iq_j}{r_{ij}} = U$ ✓
</details>

---

**Q22.** Two small spheres, each of mass $m$ and charge $+q$, are placed on a smooth insulating surface. They are pushed to a separation of $r$ and then released. Find their velocities when they are very far apart.

<details><summary><b>Answer</b></summary>

By conservation of energy: $U_i + KE_i = U_f + KE_f$

$\frac{kq^2}{r} + 0 = 0 + 2\times\frac{1}{2}mv^2$ (both move symmetrically)

$v = \sqrt{\frac{kq^2}{mr}}$

By conservation of momentum, both spheres move with equal and opposite velocities of magnitude $v = \sqrt{kq^2/(mr)}$.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23–Q32:** Comprehensive potential energy calculations.

**Q23.** A charge $+4\,\mu C$ is at the origin. How much work is done to bring a $-2\,\mu C$ charge from $r = 5$ m to $r = 2$ m?

<details><summary><b>Answer</b></summary>

$W_{ext} = U_f - U_i = \frac{k(4)(-2)\times10^{-12}}{2} - \frac{k(4)(-2)\times10^{-12}}{5}$

$= 9\times10^9\times(-8\times10^{-12})(1/2 - 1/5) = -72\times10^{-3}\times0.3 = \mathbf{-21.6\,mJ}$

Negative work — the field (attraction) assists the motion.
</details>

---

**Q24.** Two conducting spheres of radii $R_1$ and $R_2$ carry charges $Q_1$ and $Q_2$. They are connected by a wire. Show that the final charge distribution satisfies $Q_1'/Q_2' = R_1/R_2$.

<details><summary><b>Answer</b></summary>

After connection, both spheres reach the same potential:

$V_1 = V_2 \Rightarrow kQ_1'/R_1 = kQ_2'/R_2 \Rightarrow Q_1'/R_1 = Q_2'/R_2 \Rightarrow Q_1'/Q_2' = R_1/R_2$

Charge distributes proportionally to radius. The smaller sphere gets less charge but has higher surface charge density $\sigma \propto Q/R^2 = (R)/R^2 = 1/R$ — smaller sphere always has higher surface charge density and hence stronger surface field.
</details>

---

**Q25.** Calculate the work done to disperse a system of four charges $+1\,\mu C$ at the corners of a square of side $1$ m (i.e., to move all charges to infinity).

<details><summary><b>Answer</b></summary>

Work to disperse = $-U_{system}$

$U = 4\times\frac{kq^2}{a} + 2\times\frac{kq^2}{a\sqrt{2}} = kq^2\left(\frac{4}{a}+\frac{\sqrt{2}}{a}\right) = \frac{kq^2}{a}(4+\sqrt{2})$

$U = \frac{9\times10^9\times10^{-12}}{1}(4+1.414) = 9\times10^{-3}\times5.414 = 48.7$ mJ

$W_{disperse} = \mathbf{48.7\,mJ}$
</details>

---

**Q26.** Three charges $+q$, $-2q$, $+q$ are on the x-axis at $-a$, $0$, $+a$. Find the potential energy and determine if this is a bound system.

<details><summary><b>Answer</b></summary>

Pairs: $(+q)(-2q)$ at $a$: $-2kq^2/a$; $(-2q)(+q)$ at $a$: $-2kq^2/a$; $(+q)(+q)$ at $2a$: $kq^2/(2a)$

$U = -2kq^2/a - 2kq^2/a + kq^2/(2a) = kq^2(-4+0.5)/a = \mathbf{-3.5kq^2/a}$

Since $U < 0$, the system is bound.
</details>

---

**Q27.** Two identical charges $+q$ are at $(\pm d, 0)$. Show that the potential energy of a third charge $-Q$ at $(0, y)$ is $U = -2kqQ/\sqrt{d^2+y^2}$ and find the equilibrium position.

<details><summary><b>Answer</b></summary>

Distance from $(0,y)$ to $(\pm d, 0)$: $r = \sqrt{d^2+y^2}$

$U_{-Q} = \frac{k(q)(-Q)}{r} + \frac{k(q)(-Q)}{r} = -\frac{2kqQ}{\sqrt{d^2+y^2}}$ ✓

Also $U_{qq} = kq^2/(2d)$ (constant).

Force on $-Q$ in y-direction: $F_y = -dU_{-Q}/dy = -2kqQ\times\frac{y}{(d^2+y^2)^{3/2}}$

For equilibrium: $F_y = 0 \Rightarrow y = 0$. The equilibrium is at the origin (but unstable in x-direction).
</details>

---

**Q28.** Calculate the total potential energy of a NaCl ion pair, where Na$^+$ and Cl$^-$ are separated by $2.82$ Å. What does the negative sign mean?

<details><summary><b>Answer</b></summary>

$U = \frac{k(+e)(-e)}{r} = \frac{-ke^2}{r} = \frac{-9\times10^9\times(1.6\times10^{-19})^2}{2.82\times10^{-10}}$

$U = \frac{-2.304\times10^{-28}}{2.82\times10^{-10}} = -8.17\times10^{-19}$ J $= -5.1$ eV

Negative sign means: the Na$^+$-Cl$^-$ ion pair is bound. 5.1 eV of energy must be supplied to separate them. This is the ionic bond energy of NaCl.
</details>

---

**Q29.** A system of charges is in equilibrium. Prove using Earnshaw's theorem that this equilibrium must be unstable.

<details><summary><b>Answer</b></summary>

**Earnshaw's Theorem:** A charge cannot remain in stable electrostatic equilibrium under the influence of electrostatic forces alone.

**Proof:** For stable equilibrium, the potential energy must have a minimum at the equilibrium point. This requires $\nabla^2 U > 0$, i.e., $\nabla^2 V < 0$ (for positive charge).

But for a charge-free region, Laplace's equation requires $\nabla^2 V = 0$ everywhere. A function satisfying Laplace's equation cannot have a local minimum or maximum (by the maximum principle). Therefore, $V$ can only be a saddle point, never a true minimum — making all electrostatic equilibria unstable.

(In practice, stable configurations exist when other forces — like quantum mechanical forces or constraints — are also present.)
</details>

---

**Q30.** The electrostatic potential energy of a system is $U = \frac{kQ^2}{a}\left(\sqrt{2}-4\right)$ (from the synthesis problem). If the charges are released, what happens? Find the velocity of each charge when they are separated by $10a$ (assume all four charges are equal mass $m$).

<details><summary><b>Answer</b></summary>

By symmetry, the square arrangement would first expand maintaining its shape. However, exact dynamics are complex. For a rough estimate using energy conservation (ignoring intermediate geometry):

$KE_{final} \approx |U_i| - |U_f|$ where $|U_f| \approx 0$ at large separation.

$KE_{total} = |U_i| = \frac{kQ^2}{a}(4-\sqrt{2}) \approx 2.586\frac{kQ^2}{a}$

With 4 charges of mass $m$ each: $4\times\frac{1}{2}mv^2 = 2.586\frac{kQ^2}{a}$

$v = \sqrt{\frac{2.586kQ^2}{2ma}} = \sqrt{\frac{1.293kQ^2}{ma}}$

This is an approximation; exact dynamics require numerical simulation.
</details>

---

**Q31.** A charge $-q$ is at the center of a ring of radius $R$ carrying charge $+Q$. Find the potential energy of this configuration.

<details><summary><b>Answer</b></summary>

Potential at center of ring: $V_{ring} = kQ/R$

Potential energy of $-q$ at center: $U = (-q)\times V_{ring} = \frac{-kqQ}{R}$

Self-energy of the ring is not included (it's a fixed configuration). Total potential energy of the system (ring + central charge):

$U = -kqQ/R$

The system is bound if $q > 0$ and $Q > 0$ (opposite charges attracted).
</details>

---

**Q32.** Show that $1$ eV $= 1.6\times10^{-19}$ J, and find the potential energy (in eV) of a doubly ionized helium ion (He$^{2+}$, charge $+2e$) and an electron at $r = 1$ Å.

<details><summary><b>Answer</b></summary>

**Derivation:** When a charge $q = e = 1.6\times10^{-19}$ C is moved through a potential difference of $1$ V:

$W = qV = 1.6\times10^{-19}\times1 = 1.6\times10^{-19}$ J $\equiv 1$ eV ✓

**Potential energy:**

$U = \frac{k(+2e)(-e)}{r} = \frac{-2ke^2}{r} = \frac{-2\times9\times10^9\times(1.6\times10^{-19})^2}{10^{-10}}$

$U = \frac{-2\times2.304\times10^{-28}}{10^{-10}} = -4.608\times10^{-18}$ J

In eV: $U = -4.608\times10^{-18}/(1.6\times10^{-19}) = \mathbf{-28.8\,eV}$
</details>

---

*Next: [Chapter 8 — Potential Energy in an External Field →](./08_potential_energy_external_field.md)*
