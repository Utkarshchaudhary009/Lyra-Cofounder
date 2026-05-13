# Chapter 8: Potential Energy in an External Field

> *NCERT Section 2.8*

---

### The Story of the Puppet and the Stage

In the previous chapter, we calculated the energy of a *self-contained* system — the "cost" of assembling charges from scratch. But what happens when charges are placed into a field that *already exists*?

Think of a puppet placed on an already-tilted stage. The stage wasn't built for the puppet — it existed before the puppet arrived. The puppet's potential energy on this stage depends on where it's placed, but it doesn't change the stage itself.

In physics, this is the distinction between a **self-energy** problem (building the stage) and an **external field** problem (placing the puppet). This chapter deals with puppets on pre-existing stages — charges and dipoles placed in external electric fields.

---

### Building the Concept: Single Charge in an External Field

If an external electric field creates a potential $V(\vec{r})$ at every point in space, then the potential energy of a single charge $q$ placed at position $\vec{r}$ is:

$$\boxed{U = qV(\vec{r})}$$

This is simply the definition of potential: $V = U/q$, rearranged.

> **Subtlety:** This $U$ is the energy of the charge *in the external field only*. It does not include the self-energy of the charge or the energy stored in the external field itself.

---

### Checkpoint 1: Single Charge in an External Field

**Problem 1:** An external electric field creates the following potential: $V(x) = 300 - 50x$ (where $x$ is in meters and $V$ in volts). A charge of $+4 \mu C$ is placed at $x = 2$ m. What is its potential energy?

<details><summary><b>Solution</b></summary>

$V(2) = 300 - 50(2) = 200$ V

$U = qV = 4 \times 10^{-6} \times 200 = \textbf{8 × 10⁻⁴ J = 0.8 mJ}$
</details>

**Problem 2:** The charge is moved to $x = 4$ m. What is the change in potential energy? Does an external agent need to do positive or negative work?

<details><summary><b>Solution</b></summary>

$V(4) = 300 - 50(4) = 100$ V

$\Delta U = q(V_{final} - V_{initial}) = 4 \times 10^{-6}(100 - 200) = -4 \times 10^{-4}$ J

$\Delta U = \textbf{-0.4 mJ}$

The potential energy decreased — the charge moved "downhill." The electric field did the work; an external agent would need to do **negative** work (or equivalently, the external agent restrains the charge, and the field does $+0.4$ mJ of work).
</details>

---

### Building the Concept: Two Charges in an External Field

If two charges $q_1$ and $q_2$ are placed at positions $\vec{r}_1$ and $\vec{r}_2$ in an external potential $V(\vec{r})$, the total potential energy is:

$$U = q_1 V(\vec{r}_1) + q_2 V(\vec{r}_2) + \frac{kq_1 q_2}{r_{12}}$$

The first two terms are the energies of each charge in the external field. The third term is their mutual interaction energy (the "cost" of assembling the pair, independent of the external field).

---

### Building the Concept: Dipole in an External Field

This is the most important result in this chapter — and a Board/JEE examination favourite.

A dipole (charges $+q$ and $-q$ separated by distance $2a$, dipole moment $\vec{p} = q \times 2a$) is placed in a uniform external electric field $\vec{E}$.

#### Potential Energy

Place $-q$ at position A and $+q$ at position B, where the field points from A to B. If $\theta$ is the angle between $\vec{p}$ and $\vec{E}$:

$$U_{-q} = (-q)V(A) \quad \text{and} \quad U_{+q} = (+q)V(B)$$

The total energy in the external field:

$$U = q[V(B) - V(A)]$$

For a uniform field, $V(B) - V(A) = -E \times 2a\cos\theta = -E \times (2a)\cos\theta$:

$$U = q \times (-E \times 2a\cos\theta) + \frac{k(+q)(-q)}{2a}$$

The self-energy term $k(+q)(-q)/2a$ is a constant — it doesn't depend on $\theta$ and doesn't change when we rotate the dipole. We can absorb it into the reference. The physically meaningful part is:

$$\boxed{U = -pE\cos\theta = -\vec{p} \cdot \vec{E}}$$

#### Torque (Review from Chapter 1)

The dipole also experiences a torque that tends to align it with the field:

$$\boxed{\vec{\tau} = \vec{p} \times \vec{E} \implies |\tau| = pE\sin\theta}$$

#### Key Orientations

| Orientation | $\theta$ | Torque | Energy $U$ | Stability |
|:-----------:|:--------:|:------:|:----------:|:---------:|
| $\vec{p} \parallel \vec{E}$ | $0°$ | $0$ | $-pE$ (minimum) | **Stable equilibrium** |
| $\vec{p} \perp \vec{E}$ | $90°$ | $pE$ (maximum) | $0$ | — |
| $\vec{p}$ antiparallel to $\vec{E}$ | $180°$ | $0$ | $+pE$ (maximum) | **Unstable equilibrium** |

> **Physical Intuition:** A dipole in a uniform field is like a compass needle in a magnetic field. It naturally swings to align with the field ($\theta = 0°$). At $\theta = 0°$, the energy is minimum and the torque is zero — stable rest. At $\theta = 180°$, the energy is maximum and the torque is also zero — but any tiny disturbance will cause it to flip. This is unstable equilibrium, like a pencil balanced on its tip.

---

### Checkpoint 2: Dipole in an External Field

**The Microwave Oven Scenario:** *In a microwave oven, water molecules (electric dipoles) are subjected to a rapidly oscillating electric field. The field flips direction billions of times per second, and each flip forces the water molecules to rotate, generating heat through molecular friction.*

**Problem 1:** A water molecule has a dipole moment $p = 6.2 \times 10^{-30}$ C·m. It is placed in a uniform electric field of $E = 5 \times 10^5$ V/m. What is the maximum torque experienced by the molecule?

<details><summary><b>Solution</b></summary>

Maximum torque occurs at $\theta = 90°$:

$\tau_{max} = pE = 6.2 \times 10^{-30} \times 5 \times 10^5$

$\tau_{max} = \textbf{3.1 × 10⁻²⁴ N·m}$

Tiny — but there are $\sim 10^{25}$ molecules in a glass of water, so the collective effect is enormous.
</details>

**Problem 2:** What is the potential energy of the molecule when it is (a) aligned with the field, (b) perpendicular to the field, (c) antiparallel to the field?

<details><summary><b>Solution</b></summary>

(a) $\theta = 0°$: $U = -pE\cos 0° = -pE = -3.1 \times 10^{-24}$ J

(b) $\theta = 90°$: $U = -pE\cos 90° = 0$

(c) $\theta = 180°$: $U = -pE\cos 180° = +pE = +3.1 \times 10^{-24}$ J

$\textbf{(a) -3.1 × 10⁻²⁴ J \quad (b) 0 \quad (c) +3.1 × 10⁻²⁴ J}$
</details>

**Problem 3:** How much work must be done by an external agent to rotate the molecule from $\theta = 0°$ to $\theta = 180°$?

<details><summary><b>Solution</b></summary>

$W = U_{final} - U_{initial} = (+pE) - (-pE) = 2pE$

$W = 2 \times 3.1 \times 10^{-24} = \textbf{6.2 × 10⁻²⁴ J}$

This work is stored as increased potential energy.
</details>

**Problem 4:** The molecule is released from $\theta = 60°$. Through what angle must it rotate to reach its minimum energy position? What is the work done by the electric field during this rotation?

<details><summary><b>Solution</b></summary>

Minimum energy is at $\theta = 0°$, so it rotates through $60°$.

$W_{field} = U_{initial} - U_{final} = (-pE\cos 60°) - (-pE\cos 0°)$

$W_{field} = -pE(1/2) + pE(1) = pE/2$

$W_{field} = \frac{3.1 \times 10^{-24}}{2} = \textbf{1.55 × 10⁻²⁴ J}$

This energy is converted into the rotational kinetic energy of the molecule.
</details>

---

### Checkpoint 3: The Work Integral

**Problem 1:** Calculate the work done by an external agent in rotating a dipole from angle $\theta_1$ to $\theta_2$ in a uniform field $E$.

<details><summary><b>Solution</b></summary>

$W_{ext} = U(\theta_2) - U(\theta_1) = -pE\cos\theta_2 - (-pE\cos\theta_1)$

$W_{ext} = pE(\cos\theta_1 - \cos\theta_2)$

This is the general formula. All specific cases can be derived from it:
- $\theta_1 = 0° \to \theta_2 = 90°$: $W = pE(1 - 0) = pE$
- $\theta_1 = 0° \to \theta_2 = 180°$: $W = pE(1 - (-1)) = 2pE$
- $\theta_1 = 90° \to \theta_2 = 180°$: $W = pE(0 - (-1)) = pE$
</details>

**Problem 2:** An electric dipole of moment $p = 2 \times 10^{-6}$ C·m is placed at $30°$ to a uniform field of $10^5$ V/m. Find: (a) the torque, (b) the potential energy, (c) the work required to rotate it to $90°$.

<details><summary><b>Solution</b></summary>

(a) $\tau = pE\sin 30° = 2 \times 10^{-6} \times 10^5 \times 0.5 = \textbf{0.1 N·m}$

(b) $U = -pE\cos 30° = -2 \times 10^{-6} \times 10^5 \times \frac{\sqrt{3}}{2} = -0.1\sqrt{3} = \textbf{-0.173 J}$

(c) $W = pE(\cos 30° - \cos 90°) = 0.2(\frac{\sqrt{3}}{2} - 0) = 0.1\sqrt{3} = \textbf{0.173 J}$
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** An electric dipole consists of charges $+20$ nC and $-20$ nC separated by $1$ mm. It is placed in an external uniform electric field of $5 \times 10^4$ V/m.

(a) Calculate the dipole moment.  
(b) If the dipole is initially perpendicular to the field, what is its initial potential energy and torque?  
(c) The dipole is released and swings to align with the field. What is the angular velocity at the aligned position, assuming the moment of inertia of the dipole about its center is $I = 5 \times 10^{-18}$ kg·m²?  
(d) Does the dipole overshoot and oscillate, or does it stop at $\theta = 0°$?

<details><summary><b>Solution</b></summary>

**(a)** $p = q \times 2a = 20 \times 10^{-9} \times 10^{-3} = \textbf{2 × 10⁻¹¹ C·m}$

**(b)** At $\theta = 90°$:

$U = -pE\cos 90° = \textbf{0}$

$\tau = pE\sin 90° = 2 \times 10^{-11} \times 5 \times 10^4 = \textbf{1 × 10⁻⁶ N·m = 1 μN·m}$

**(c)** Using energy conservation from $\theta = 90°$ to $\theta = 0°$:

$\Delta KE = -\Delta U$

$\frac{1}{2}I\omega^2 = U_{initial} - U_{final} = 0 - (-pE) = pE$

$\omega = \sqrt{\frac{2pE}{I}} = \sqrt{\frac{2 \times 2 \times 10^{-11} \times 5 \times 10^4}{5 \times 10^{-18}}}$

$\omega = \sqrt{\frac{2 \times 10^{-6}}{5 \times 10^{-18}}} = \sqrt{4 \times 10^{11}} = 2 \times 10^{5.5}$

$\omega = \textbf{6.32 × 10⁵ rad/s}$

**(d)** In the absence of friction, the dipole will **overshoot** $\theta = 0°$ and oscillate back and forth. At $\theta = 0°$, it has maximum kinetic energy and zero torque — it cannot stop instantaneously. The motion is analogous to a pendulum swinging through its lowest point.

In practice, molecular dipoles lose energy through collisions and radiation, and eventually settle at $\theta = 0°$. But in a frictionless scenario, the dipole oscillates indefinitely, executing simple harmonic motion (for small angles) with period $T = 2\pi\sqrt{I/pE}$.
</details>

---

## Question Bank — Chapter 8

### Section A: MCQs (15 Questions)

**Q1.** The potential energy of a dipole in a uniform electric field is:

(a) $pE\sin\theta$ &emsp; (b) $-pE\cos\theta$ &emsp; (c) $pE\cos\theta$ &emsp; (d) $-pE\sin\theta$

<details><summary><b>Answer</b></summary>**(b)** $U = -\vec{p}\cdot\vec{E} = -pE\cos\theta$</details>

---

**Q2.** A dipole is aligned parallel to a uniform electric field. Its potential energy is:

(a) $+pE$ &emsp; (b) $-pE$ &emsp; (c) $0$ &emsp; (d) $pE/2$

<details><summary><b>Answer</b></summary>**(b)** At $\theta = 0°$: $U = -pE\cos0° = -pE$ (minimum energy — stable equilibrium).</details>

---

**Q3.** A dipole is antiparallel to a uniform electric field. It is in:

(a) Stable equilibrium &emsp; (b) Unstable equilibrium &emsp; (c) No equilibrium &emsp; (d) Neutral equilibrium

<details><summary><b>Answer</b></summary>**(b)** At $\theta = 180°$: $U = +pE$ (maximum energy). Any disturbance causes it to flip. Unstable equilibrium.</details>

---

**Q4.** The torque on a dipole in a uniform field is maximum when:

(a) $\theta = 0°$ &emsp; (b) $\theta = 45°$ &emsp; (c) $\theta = 90°$ &emsp; (d) $\theta = 180°$

<details><summary><b>Answer</b></summary>**(c)** $\tau = pE\sin\theta$ is maximum at $\theta = 90°$.</details>

---

**Q5.** The work done to rotate a dipole from $\theta_1 = 30°$ to $\theta_2 = 90°$ is:

(a) $pE(1-\sqrt{3}/2)$ &emsp; (b) $pE(\sqrt{3}/2)$ &emsp; (c) $0$ &emsp; (d) $pE(\sqrt{3}/2 - 1)$

<details><summary><b>Answer</b></summary>**(b)** $W = pE(\cos\theta_1-\cos\theta_2) = pE(\cos30°-\cos90°) = pE(\sqrt{3}/2-0) = pE\sqrt{3}/2$.</details>

---

**Q6.** The potential energy of a charge $+q$ at a point where the external potential is $V$ is:

(a) $V/q$ &emsp; (b) $qV$ &emsp; (c) $q/V$ &emsp; (d) $q^2V$

<details><summary><b>Answer</b></summary>**(b)** $U = qV$ by definition of potential.</details>

---

**Q7.** For a dipole in an external uniform field, the stable equilibrium is at:

(a) $\theta = 0°$ (parallel to field) &emsp; (b) $\theta = 90°$ &emsp; (c) $\theta = 180°$ &emsp; (d) Any angle

<details><summary><b>Answer</b></summary>**(a)** $U = -pE\cos\theta$ is minimum at $\theta = 0°$ — the dipole aligns with the field in stable equilibrium.</details>

---

**Q8.** A water molecule (dipole) in a microwave oven experiences maximum heating when:

(a) Aligned with field &emsp; (b) Antiparallel to field &emsp; (c) Perpendicular to field &emsp; (d) At any orientation

<details><summary><b>Answer</b></summary>**(c)** At $\theta = 90°$, the torque is maximum, so maximum work is done on the molecule as it rotates toward alignment, converting maximum energy to heat.</details>

---

**Q9.** Two charges $q_1$ and $q_2$ are placed at positions $\vec{r}_1$ and $\vec{r}_2$ in an external potential $V(\vec{r})$. The total potential energy is:

(a) $q_1V(\vec{r}_1) + q_2V(\vec{r}_2)$ &emsp; (b) $q_1V(\vec{r}_1) + q_2V(\vec{r}_2) + kq_1q_2/r_{12}$ &emsp; (c) $kq_1q_2/r_{12}$ &emsp; (d) $(q_1+q_2)V$

<details><summary><b>Answer</b></summary>**(b)** Total PE = PE in external field + mutual interaction energy.</details>

---

**Q10.** If a dipole is released from $\theta = 90°$ in a uniform field, it reaches $\theta = 0°$ with kinetic energy:

(a) $pE/2$ &emsp; (b) $pE$ &emsp; (c) $2pE$ &emsp; (d) $0$

<details><summary><b>Answer</b></summary>**(b)** $\Delta KE = U_{90°} - U_{0°} = 0 - (-pE) = pE$.</details>

---

**Q11.** The period of oscillation of a dipole of moment $p$ and moment of inertia $I$ in field $E$ (for small angles) is:

(a) $2\pi\sqrt{I/(pE)}$ &emsp; (b) $2\pi\sqrt{pE/I}$ &emsp; (c) $2\pi\sqrt{I/p}$ &emsp; (d) $2\pi\sqrt{p/(IE)}$

<details><summary><b>Answer</b></summary>**(a)** Analogous to SHM of a pendulum: $T = 2\pi\sqrt{I/(pE)}$.</details>

---

**Q12.** The potential energy of a negative charge placed at a point of high positive potential is:

(a) Positive &emsp; (b) Negative &emsp; (c) Zero &emsp; (d) Infinite

<details><summary><b>Answer</b></summary>**(b)** $U = qV = (-)(+) = $ negative.</details>

---

**Q13.** A dipole in an external field experiences zero net force when:

(a) The field is uniform &emsp; (b) The torque is maximum &emsp; (c) $\theta = 90°$ &emsp; (d) $\theta = 0°$

<details><summary><b>Answer</b></summary>**(a)** In a uniform field, forces on $+q$ and $-q$ are equal and opposite — net force is zero for any orientation. (Non-uniform fields do exert net forces on dipoles.)</details>

---

**Q14.** When a charge $+q$ is placed at a point where $V = -500$ V (due to external field), its potential energy is:

(a) $-500q$ J &emsp; (b) $+500q$ J &emsp; (c) $500/q$ J &emsp; (d) $0$

<details><summary><b>Answer</b></summary>**(a)** $U = qV = q\times(-500) = -500q$ J.</details>

---

**Q15.** The net torque on a dipole is zero in a uniform field when $\theta$ equals:

(a) $0°$ only &emsp; (b) $90°$ only &emsp; (c) $0°$ or $180°$ &emsp; (d) $45°$ or $135°$

<details><summary><b>Answer</b></summary>**(c)** $\tau = pE\sin\theta = 0$ when $\sin\theta = 0$, i.e., $\theta = 0°$ or $180°$.</details>

---

### Section B: Short Answer Questions

**Q16.** A charge $+5\,\mu C$ is placed in an external field. The potential due to the external field at this point is $300$ V. Find the potential energy of the charge.

<details><summary><b>Answer</b></summary>

$U = qV = 5\times10^{-6}\times300 = \mathbf{1.5\times10^{-3}\,J = 1.5\,mJ}$
</details>

---

**Q17.** A dipole of moment $p = 3\times10^{-8}$ C·m is placed at $\theta = 60°$ to a uniform field $E = 2\times10^5$ V/m. Find (a) the torque, (b) the potential energy, (c) work to rotate to $\theta = 0°$.

<details><summary><b>Answer</b></summary>

**(a)** $\tau = pE\sin60° = 3\times10^{-8}\times2\times10^5\times(\sqrt{3}/2) = 6\times10^{-3}\times0.866 = \mathbf{5.2\times10^{-3}\,N\cdot m}$

**(b)** $U = -pE\cos60° = -6\times10^{-3}\times0.5 = \mathbf{-3\times10^{-3}\,J}$

**(c)** $W = pE(\cos60°-\cos0°) = 6\times10^{-3}(0.5-1) = \mathbf{-3\times10^{-3}\,J}$ (field does the work)
</details>

---

**Q18.** Why does a dipole oscillate when displaced from its equilibrium in a uniform electric field? Derive the period of oscillation.

<details><summary><b>Answer</b></summary>

When displaced by small angle $\theta$ from $\theta = 0°$ (stable equilibrium), restoring torque: $\tau = -pE\sin\theta \approx -pE\theta$ (for small $\theta$)

Equation of motion: $I\ddot{\theta} = -pE\theta$

This is SHM with $\omega^2 = pE/I$.

Period: $T = 2\pi/\omega = 2\pi\sqrt{I/(pE)}$

The dipole acts like a torsional pendulum, oscillating about the field direction.
</details>

---

**Q19.** A charge $q_1 = +2\,\mu C$ is at position $A$ and $q_2 = -3\,\mu C$ is at position $B$, $0.5$ m apart. The external potential at A is $100$ V and at B is $-200$ V. Find the total potential energy.

<details><summary><b>Answer</b></summary>

$U = q_1V(A) + q_2V(B) + \frac{kq_1q_2}{r_{AB}}$

$U = 2\times10^{-6}\times100 + (-3\times10^{-6})\times(-200) + \frac{9\times10^9\times2\times10^{-6}\times(-3\times10^{-6})}{0.5}$

$U = 2\times10^{-4} + 6\times10^{-4} + \frac{-54\times10^{-3}}{0.5}$

$U = 2\times10^{-4} + 6\times10^{-4} - 108\times10^{-3} = 8\times10^{-4} - 0.108 = \mathbf{-0.1072\,J}$
</details>

---

**Q20.** A dipole of moment $p$ is initially at $\theta = 180°$ (antiparallel) to a field $E$. It is released. Describe qualitatively what happens. Find the maximum angular velocity it achieves.

<details><summary><b>Answer</b></summary>

From $\theta = 180°$, the dipole experiences a restoring torque toward $\theta = 0°$. It begins to rotate, gaining kinetic energy. At $\theta = 0°$, its KE is maximum:

$\frac{1}{2}I\omega_{max}^2 = U_{180°} - U_{0°} = pE - (-pE) = 2pE$

$\omega_{max} = \sqrt{4pE/I} = 2\sqrt{pE/I}$

It overshoots $\theta = 0°$ and continues to $\theta = -180°$ (same as $180°$), then oscillates. In a friction-free environment, it rotates continuously (full circles) if started from exactly $\theta = 180°$ with any kinetic energy.
</details>

---

**Q21.** A $+2\,\mu C$ charge moves from $V = 100$ V to $V = 400$ V in an external field. Find (a) change in potential energy, (b) work done by field, (c) work done by external agent.

<details><summary><b>Answer</b></summary>

**(a)** $\Delta U = q\Delta V = 2\times10^{-6}\times(400-100) = +6\times10^{-4}$ J = $\mathbf{+0.6\,mJ}$

**(b)** $W_{field} = -\Delta U = \mathbf{-0.6\,mJ}$ (field does negative work — opposes motion uphill)

**(c)** $W_{ext} = +\Delta U = \mathbf{+0.6\,mJ}$ (external agent pushes against field)
</details>

---

**Q22.** Show that for a dipole in an external field, the condition for stable equilibrium is that $U$ is minimum, which requires $\theta = 0°$.

<details><summary><b>Answer</b></summary>

$U(\theta) = -pE\cos\theta$

$dU/d\theta = pE\sin\theta = 0 \Rightarrow \theta = 0°$ or $180°$

$d^2U/d\theta^2 = pE\cos\theta$

At $\theta = 0°$: $d^2U/d\theta^2 = pE > 0$ → **minimum** of $U$ → **stable equilibrium** ✓

At $\theta = 180°$: $d^2U/d\theta^2 = -pE < 0$ → **maximum** of $U$ → **unstable equilibrium** ✓
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** An electric dipole of length $2\,\text{cm}$ with charges $\pm10\,\mu C$ is placed in a uniform field of $10^5$ V/m at $30°$.
(a) Find the torque. (b) Find the work to rotate to $\theta = 90°$.

<details><summary><b>Answer</b></summary>

$p = 10\times10^{-6}\times0.02 = 2\times10^{-7}$ C·m

**(a)** $\tau = pE\sin30° = 2\times10^{-7}\times10^5\times0.5 = \mathbf{0.01\,N\cdot m}$

**(b)** $W = pE(\cos30°-\cos90°) = 2\times10^{-7}\times10^5\times(\sqrt{3}/2) = 2\times10^{-2}\times0.866 = \mathbf{0.01732\,J}$
</details>

---

**Q24.** A system of two charges is placed in a uniform external field $E = 1000$ V/m pointing in $+x$ direction.
$q_1 = +2\,\mu C$ at $(0, 0)$, $q_2 = -1\,\mu C$ at $(0.3, 0)$ m.
Find the total energy of the system in the external field.

<details><summary><b>Answer</b></summary>

$V_{ext}(x) = -Ex + C$. Setting $V = 0$ at $x = 0$: $V_{ext}(0) = 0$, $V_{ext}(0.3) = -1000\times0.3 = -300$ V.

$U_{ext} = q_1V_{ext}(0) + q_2V_{ext}(0.3) = 0 + (-10^{-6})\times(-300) = 3\times10^{-4}$ J

$U_{mutual} = \frac{k\times2\times10^{-6}\times(-10^{-6})}{0.3} = \frac{-18\times10^{-3}}{0.3} = -0.06$ J

$U_{total} = 3\times10^{-4} - 0.06 = \mathbf{-0.0597\,J}$
</details>

---

**Q25–Q32.** Torque, energy, and oscillation problems for dipoles.

**Q25.** A dipole of $p = 4\times10^{-9}$ C·m, $I = 2\times10^{-17}$ kg·m² oscillates in a field $E = 5\times10^4$ V/m. Find the period of small oscillations.

<details><summary><b>Answer</b></summary>

$T = 2\pi\sqrt{I/(pE)} = 2\pi\sqrt{\frac{2\times10^{-17}}{4\times10^{-9}\times5\times10^4}} = 2\pi\sqrt{\frac{2\times10^{-17}}{2\times10^{-4}}} = 2\pi\sqrt{10^{-13}}$

$T = 2\pi\times10^{-6.5} = 2\pi\times3.16\times10^{-7} = \mathbf{1.99\times10^{-6}\,s \approx 2\,\mu s}$
</details>

---

**Q26.** At what angle does the potential energy of a dipole equal half of its maximum value?

<details><summary><b>Answer</b></summary>

Maximum $U = +pE$ (at $\theta = 180°$). Half: $-pE\cos\theta = pE/2 \Rightarrow \cos\theta = -1/2 \Rightarrow \theta = \mathbf{120°}$
</details>

---

**Q27.** A dipole of moment $p$ is released from $\theta = 60°$ in a field $E$. Find its kinetic energy at $\theta = 0°$.

<details><summary><b>Answer</b></summary>

$KE = U_{60°} - U_{0°} = -pE\cos60° - (-pE\cos0°) = -pE/2 + pE = \mathbf{pE/2}$
</details>

---

**Q28.** Explain the significance of $U = -\vec{p}\cdot\vec{E}$. Why does alignment with the field give minimum energy?

<details><summary><b>Answer</b></summary>

$U = -\vec{p}\cdot\vec{E} = -pE\cos\theta$. When $\theta = 0°$ (aligned), $\cos\theta = 1$, $U = -pE$ (most negative = minimum).

Physically: when $+q$ is on the high-potential side and $-q$ on the low-potential side (aligned with $E$), both charges are at their most favorable potential positions ($+q$ at low PE side, $-q$ at high PE side — wait, $U_{+q} = +qV_{high}$ and $U_{-q} = -qV_{low}$... Actually the combined system is at lowest energy when the net displacement of charge is in the field direction — the field "pulls" the dipole into alignment.

Nature minimizes energy, so the dipole always tends toward $\theta = 0°$.
</details>

---

**Q29.** Show that a dipole in a non-uniform field experiences a net translational force in addition to a torque.

<details><summary><b>Answer</b></summary>

Force on $+q$ at position $\vec{r}_+$: $\vec{F}_+ = +q\vec{E}(\vec{r}_+)$

Force on $-q$ at position $\vec{r}_-$: $\vec{F}_- = -q\vec{E}(\vec{r}_-)$

Net force: $\vec{F} = q[\vec{E}(\vec{r}_+) - \vec{E}(\vec{r}_-)] = q\Delta\vec{E}$

If $\vec{E}$ is uniform, $\Delta\vec{E} = 0$ → no net force.

If $\vec{E}$ is non-uniform, $\Delta\vec{E} \neq 0$ → net force exists.

For a dipole along x-axis: $F_x \approx p\frac{\partial E_x}{\partial x}$ (derivative of field = non-uniformity gives the force).
</details>

---

**Q30.** A dipole with $p = 5\times10^{-8}$ C·m is in a uniform field $E = 3\times10^4$ V/m. Find the difference in energy between the parallel and antiparallel orientations.

<details><summary><b>Answer</b></summary>

$\Delta U = U_{180°} - U_{0°} = +pE - (-pE) = 2pE = 2\times5\times10^{-8}\times3\times10^4 = \mathbf{3\times10^{-3}\,J = 3\,mJ}$
</details>

---

**Q31.** Three charges are in an external potential $V(r) = A/r$. Charges: $+q$ at $r_1 = 1$ m, $+q$ at $r_2 = 2$ m, $-q$ at $r_3 = 3$ m. Find the total potential energy given $A = 100$ V·m.

<details><summary><b>Answer</b></summary>

$V_{ext}(1) = 100$ V, $V_{ext}(2) = 50$ V, $V_{ext}(3) = 33.3$ V

$U_{ext} = q(100) + q(50) + (-q)(33.3) = q(100+50-33.3) = 116.7q$

$U_{mutual}$: Need distances between charges. Assuming on x-axis at $x = 1, 2, 3$ m:

$U_{12} = kq^2/1$, $U_{13} = kq^2/2$, $U_{23} = k(q)(-q)/1 = -kq^2$

$U_{mutual} = kq^2(1 + 0.5 - 1) = 0.5kq^2$

$U_{total} = 116.7q + 0.5kq^2$
</details>

---

**Q32.** Compare and contrast the behavior of a dipole in (a) a uniform electric field, (b) a non-uniform electric field.

<details><summary><b>Answer</b></summary>

| Property | Uniform Field | Non-uniform Field |
|----------|:------------:|:-----------------:|
| Net force | Zero | Non-zero (toward stronger field region) |
| Torque | $\tau = pE\sin\theta$ (exists) | $\tau$ exists + net force |
| Equilibrium | Rotational equilibrium possible | Translational motion too |
| Potential energy | $U = -pE\cos\theta$ | $U = -\vec{p}\cdot\vec{E}(\vec{r})$ (varies with position) |
| Stable position | $\theta = 0°$ (any position) | Aligns AND moves toward field maximum |
| Example | Between capacitor plates | Near a point charge |
</details>

---

*Next: [Chapter 9 — Electrostatics of Conductors →](./09_electrostatics_of_conductors.md)*
