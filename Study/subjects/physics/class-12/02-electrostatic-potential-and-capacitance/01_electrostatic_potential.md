# Chapter 1: Electrostatic Potential — The Landscape of Force

> *NCERT Sections 2.1–2.2*

---

### The Story of the Invisible Slope

Imagine you are standing on a perfectly flat, endless plain. You place a bowling ball on the ground. It doesn't move. Now imagine someone, invisibly, reshapes the ground beneath your feet into a smooth hill. You don't see it happen — but the moment you release the ball, it rolls downhill, accelerating as it goes. It moves from where the ground is *high* to where the ground is *low*. You never pushed the ball. The *landscape itself* did the work.

This is exactly what happens in the world of electric charges.

In the previous chapter, we learned about the **electric field** — the force that a charge experiences at every point in space. But there is a deeper, more elegant way to describe the same reality. Instead of asking "what force does a charge feel *here*?", we can ask: **"how much work would it take to bring a charge *to* here?"**

The answer to that question is called **Electrostatic Potential**. It is the invisible landscape — the hills and valleys — that charges roll across. Positive charges roll "downhill" from high potential to low potential, just like the bowling ball. Negative charges, being contrarian, roll "uphill."

Understanding potential is like having a topographic map of the electric universe. You don't need to calculate forces at every single point. You just look at the *height* of the landscape, and you know exactly where every charge will want to go.

---

### Building the Concept: From Work to Potential

#### Step 1: Electrostatic Force is Conservative

In Chapter 1, we established that the electrostatic force between charges follows Coulomb's Law. This force has a remarkable property: **the work done by the electrostatic force in moving a charge from point A to point B depends only on the positions of A and B, not on the path taken.** 

This is identical to gravity. Whether you carry a rock straight up a cliff or along a winding mountain trail, the work done *against* gravity depends only on the height difference. Forces with this property are called **conservative forces**.

> Any force that is conservative automatically has a **potential energy** associated with it. This is a theorem from mechanics, not an assumption.

#### Step 2: Defining Potential Energy

When an external force (your hand, say) moves a test charge $q$ from point A to point B against the electrostatic force, the work done by the external force is stored as **electrostatic potential energy**:

$$U_B - U_A = W_{A \to B}^{\text{external}}$$

Here, $W^{\text{external}}$ is the work done by the external agent (not the electrostatic force). The key constraint: the external force must move the charge **infinitely slowly** (quasi-statically), so that no kinetic energy is generated. All the work goes into potential energy.

> If we move the charge *with* the electric field (downhill), potential energy *decreases*. If we move it *against* the field (uphill), potential energy *increases*. Just like gravity.

#### Step 3: From Energy to Potential

Potential energy $U$ depends on the value of the test charge $q$. A $2\mu C$ charge has twice the potential energy of a $1\mu C$ charge at the same location. To create a quantity that describes the *landscape itself* — independent of who is standing on it — we divide by the test charge:

$$V = \frac{U}{q}$$

This is the **electrostatic potential** at a point. It tells you the potential energy *per unit positive charge*.

More precisely, the **potential difference** between two points A and B is:

$$V_B - V_A = \frac{W_{A \to B}^{\text{external}}}{q}$$

And the **absolute potential** at a point P (choosing infinity as the reference, where $V_\infty = 0$):

$$\boxed{V_P = \frac{W_{\infty \to P}^{\text{external}}}{q}}$$

In words: **The electrostatic potential at a point is the work done by an external force in bringing a unit positive test charge from infinity to that point, without acceleration.**

| Quantity | Symbol | SI Unit | Type |
|----------|--------|---------|------|
| Potential Energy | $U$ | Joule (J) | Scalar, extensive |
| Potential | $V$ | Volt (V) = J/C | Scalar, intensive |
| Potential Difference | $\Delta V$ | Volt (V) | Scalar |

> **Critical Insight:** Potential is a scalar. Unlike the electric field (a vector), you never need to worry about components, directions, or vector addition when working with potentials. This is the primary reason we use potentials — they make calculations dramatically simpler.

#### The Electron-Volt: A Unit Born from Potential

Since 1 Volt means 1 Joule per Coulomb, when a charge of $1e = 1.6 \times 10^{-19}$ C moves through a potential difference of 1 V, the energy gained is:

$$1 \text{ eV} = 1.6 \times 10^{-19} \text{ J}$$

This is the **electron-volt** — a unit of energy used throughout atomic and nuclear physics.

---

### Checkpoint 1: Understanding Potential and Potential Difference

**The Radio Tower Scenario:** A radio engineer needs to understand the "electrical landscape" around a charged antenna to ensure safety protocols.

**Problem 1:** The potential at point A near the antenna is $+500$ V and at point B (further away) is $+200$ V. How much work must be done to move a charge of $+4 \mu C$ from B to A?

<details><summary><b>Solution</b></summary>

$W = q(V_A - V_B) = 4 \times 10^{-6} \times (500 - 200) = 4 \times 10^{-6} \times 300$

$W = \textbf{1.2 × 10⁻³ J = 1.2 mJ}$

Since the charge is positive and we are moving it from lower to higher potential (uphill), the external agent must do positive work. This work is stored as potential energy.
</details>

**Problem 2:** Now suppose we release a $-2 \mu C$ charge at point A. Will it move towards B or away from B? Calculate the work done by the electric field as it moves from A to B.

<details><summary><b>Solution</b></summary>

A negative charge moves from lower potential to higher potential (opposite to positive charges). So it moves from A ($500$ V) to... wait. Let's think carefully.

A negative charge is attracted *towards* higher potential? No — a negative charge moves such that its potential energy *decreases*. 

$U = qV$. For $q < 0$: $U_A = (-2 \times 10^{-6})(500) = -1 \times 10^{-3}$ J and $U_B = (-2 \times 10^{-6})(200) = -0.4 \times 10^{-3}$ J.

$U_A < U_B$. So the charge moves from B to A (towards higher potential), since that decreases its potential energy.

Wait — the charge is *released at A*. At A, $U_A = -1 \times 10^{-3}$ J. At B, $U_B = -0.4 \times 10^{-3}$ J. Since $U_A < U_B$, point A is already the lower potential energy location. The charge at A has nowhere lower to go along the A-B line.

**The charge moves from B towards A** — which means if released at A, it stays (it's already at the lower potential energy side). If released at B, it would move towards A.

*Let's reframe:* If the $-2 \mu C$ charge is released at **B**, it moves towards **A** (towards higher electric potential, but lower potential energy for a negative charge).

Work done by the electric field: $W_{field} = U_B - U_A = (-0.4 \times 10^{-3}) - (-1 \times 10^{-3}) = \textbf{+0.6 × 10⁻³ J = +0.6 mJ}$

Positive work by the field confirms the field drives the charge in this direction.
</details>

**Problem 3:** An electron ($e = 1.6 \times 10^{-19}$ C) is accelerated through a potential difference of $100$ V. What kinetic energy does it gain, in both joules and electron-volts?

<details><summary><b>Solution</b></summary>

By the work-energy theorem, the kinetic energy gained equals the work done by the electric field:

$KE = |q| \times |\Delta V| = 1.6 \times 10^{-19} \times 100 = \textbf{1.6 × 10⁻¹⁷ J}$

In electron-volts: $KE = 100 \text{ eV}$ (by definition — one electron through one volt gives one eV).

$\textbf{KE = 100 eV = 1.6 × 10⁻¹⁷ J}$
</details>

---

### Checkpoint 2: The Socratic Gauntlet — "The Charged Droplet Experiment"

*A researcher in a Millikan-style lab is studying charged oil droplets suspended between parallel plates. The top plate is at $+1000$ V and the bottom plate is at $0$ V. The plates are separated by $2$ cm.*

**Problem 1:** What is the potential difference between the plates?

<details><summary><b>Solution</b></summary>

$\Delta V = V_{top} - V_{bottom} = 1000 - 0 = \textbf{1000 V}$
</details>

*The researcher introduces a tiny oil droplet carrying a charge of $+3.2 \times 10^{-19}$ C (i.e., 2 elementary charges). The droplet is placed near the bottom plate.*

**Problem 2:** How much work must the electric field do to move this droplet from the bottom plate to the top plate?

<details><summary><b>Solution</b></summary>

A positive charge moves from low potential (0 V) to high potential (1000 V). This is "uphill" — the electric field does *negative* work (it opposes this motion).

$W_{field} = q(V_{initial} - V_{final}) = 3.2 \times 10^{-19} \times (0 - 1000)$

$W_{field} = \textbf{-3.2 × 10⁻¹⁶ J}$

The field opposes the motion, so the researcher must do $+3.2 \times 10^{-16}$ J of work to push it there.
</details>

*The droplet is now released from the top plate. It falls freely under the combined influence of gravity and the electric force.*

**Problem 3:** As the droplet falls from the top plate to the bottom plate, what is the change in its electrostatic potential energy? Does this energy increase or decrease?

<details><summary><b>Solution</b></summary>

$\Delta U = q \Delta V = q(V_{final} - V_{initial}) = 3.2 \times 10^{-19} \times (0 - 1000)$

$\Delta U = \textbf{-3.2 × 10⁻¹⁶ J}$

The potential energy **decreases** by $3.2 \times 10^{-16}$ J. This lost potential energy is converted into kinetic energy (and eventually heat, when the droplet hits the plate). This is exactly analogous to a ball falling downhill — potential energy converts to kinetic energy.
</details>

**Problem 4:** Express the kinetic energy gained by the droplet in electron-volts.

<details><summary><b>Solution</b></summary>

$KE = |\Delta U| = 3.2 \times 10^{-16}$ J

$KE = \frac{3.2 \times 10^{-16}}{1.6 \times 10^{-19}} = \textbf{2000 eV = 2 keV}$

Alternatively: The droplet has charge $2e$ and falls through $1000$ V, so $KE = 2 \times 1000 = 2000$ eV. Much faster!
</details>

---

### The Culmination: Synthesis

We have built the concept of electrostatic potential from scratch. Let's bring everything together with a problem that tests the full chain of reasoning.

**Synthesis Problem:** Two parallel metal plates are separated by $5$ mm. The electric field between them is uniform at $4 \times 10^4$ V/m, directed from plate A to plate B.

(a) What is the potential difference between the plates?  
(b) A proton ($q = +1.6 \times 10^{-19}$ C, $m = 1.67 \times 10^{-27}$ kg) is released from rest at plate A. What is its speed when it reaches plate B?  
(c) If the proton is replaced by an alpha particle ($q = +3.2 \times 10^{-19}$ C, $m = 6.64 \times 10^{-27}$ kg), what speed does it reach?  
(d) Comment on why the alpha particle is slower despite having double the charge.

<details><summary><b>Solution</b></summary>

**(a)** For a uniform field: $\Delta V = Ed = 4 \times 10^4 \times 5 \times 10^{-3} = \textbf{200 V}$

The field points from A to B, so A is at higher potential. $V_A - V_B = 200$ V.

**(b)** The proton (positive) moves from high to low potential — it accelerates.

$KE = q \Delta V = 1.6 \times 10^{-19} \times 200 = 3.2 \times 10^{-17}$ J

$\frac{1}{2}mv^2 = 3.2 \times 10^{-17}$

$v = \sqrt{\frac{2 \times 3.2 \times 10^{-17}}{1.67 \times 10^{-27}}} = \sqrt{3.83 \times 10^{10}} \approx \textbf{1.96 × 10⁵ m/s}$

**(c)** For the alpha particle:

$KE = 3.2 \times 10^{-19} \times 200 = 6.4 \times 10^{-17}$ J

$v = \sqrt{\frac{2 \times 6.4 \times 10^{-17}}{6.64 \times 10^{-27}}} = \sqrt{1.93 \times 10^{10}} \approx \textbf{1.39 × 10⁵ m/s}$

**(d)** The alpha particle has double the charge, so it gains double the kinetic energy ($6.4 \times 10^{-17}$ J vs. $3.2 \times 10^{-17}$ J). But it is four times heavier. Since $v \propto \sqrt{KE/m}$, doubling the energy and quadrupling the mass gives $v_\alpha = v_p \times \sqrt{2/4} = v_p / \sqrt{2}$. The mass penalty outweighs the charge advantage.

This is why proton beams, not alpha beams, are preferred for high-speed particle acceleration.
</details>

---

## Question Bank — Chapter 1

### Section A: Multiple Choice Questions (MCQ)

**Q1.** The work done in moving a charge of $3\,\mu C$ between two points having a potential difference of $30\,V$ is:

(a) $9\times10^{-5}$ J &emsp; (b) $10\,J$ &emsp; (c) $9\times10^{5}$ J &emsp; (d) $0.9\,J$

<details><summary><b>Answer</b></summary>

**(a)** $W = q\Delta V = 3\times10^{-6}\times30 = 9\times10^{-5}$ J
</details>

---

**Q2.** Which of the following is the SI unit of electric potential?

(a) J &emsp; (b) C &emsp; (c) V = J/C &emsp; (d) N/C

<details><summary><b>Answer</b></summary>

**(c)** Volt = Joule/Coulomb
</details>

---

**Q3.** The potential at a point is $+20\,V$. The work done by the electric field in bringing a $+1\,C$ charge from infinity to this point is:

(a) $+20\,J$ &emsp; (b) $-20\,J$ &emsp; (c) $0$ &emsp; (d) $+10\,J$

<details><summary><b>Answer</b></summary>

**(b)** $W_{field} = q(V_\infty - V_P) = 1\times(0-20) = -20\,J$. The field does negative work (the charge is moving uphill).
</details>

---

**Q4.** An electron is accelerated through $1000\,V$. Its kinetic energy is:

(a) $1.6\times10^{-16}$ J &emsp; (b) $1.6\times10^{-19}$ J &emsp; (c) $1000$ eV &emsp; (d) Both (a) and (c)

<details><summary><b>Answer</b></summary>

**(d)** $KE = 1000\,\text{eV} = 1000\times1.6\times10^{-19} = 1.6\times10^{-16}$ J. Both statements are correct.
</details>

---

**Q5.** If a positive charge is moved from a lower potential region to a higher potential region, the potential energy of the system:

(a) Decreases &emsp; (b) Increases &emsp; (c) Remains unchanged &emsp; (d) Becomes zero

<details><summary><b>Answer</b></summary>

**(b)** $\Delta U = q\Delta V$. For $q>0$ and $\Delta V>0$, $\Delta U>0$ — potential energy increases.
</details>

---

**Q6.** The potential difference between two points A and B is $V_A - V_B = 25\,V$. If a charge $q = -2\,\mu C$ is moved from B to A, the work done by the electric field is:

(a) $+50\,\mu J$ &emsp; (b) $-50\,\mu J$ &emsp; (c) $+25\,\mu J$ &emsp; (d) $-25\,\mu J$

<details><summary><b>Answer</b></summary>

**(b)** $W_{field} = q(V_B - V_A) = (-2\times10^{-6})(−25) = ?$. Wait: $W_{field} = q(V_{initial}-V_{final}) = (-2\times10^{-6})(V_B-V_A) = (-2\times10^{-6})(-25) = +50\,\mu J$. Hmm let me be careful. Moving from B to A: $W_{field} = q(V_B - V_A) = (-2\times10^{-6})(-25) = +50\,\mu J$. Answer: **(a)**
</details>

---

**Q7.** 1 kV is equal to:

(a) $10^3$ J/C &emsp; (b) $10^{-3}$ V &emsp; (c) $10^3$ C &emsp; (d) $10^{-3}$ J/C

<details><summary><b>Answer</b></summary>

**(a)** $1\,\text{kV} = 10^3\,\text{V} = 10^3\,\text{J/C}$
</details>

---

**Q8.** The potential difference required to accelerate a proton from rest to a speed of $10^6\,\text{m/s}$ is approximately ($m_p = 1.67\times10^{-27}$ kg, $e = 1.6\times10^{-19}$ C):

(a) $5000\,V$ &emsp; (b) $5220\,V$ &emsp; (c) $2610\,V$ &emsp; (d) $522\,V$

<details><summary><b>Answer</b></summary>

**(b)** $KE = \frac{1}{2}m_pv^2 = \frac{1}{2}\times1.67\times10^{-27}\times10^{12} = 8.35\times10^{-16}$ J. $\Delta V = KE/e = 8.35\times10^{-16}/1.6\times10^{-19} \approx 5220\,V$
</details>

---

**Q9.** A negative charge released from rest in a uniform electric field will:

(a) Move from high to low potential &emsp; (b) Move from low to high potential &emsp; (c) Stay at rest &emsp; (d) Oscillate

<details><summary><b>Answer</b></summary>

**(b)** A negative charge experiences force opposite to $\vec{E}$, i.e., from low to high potential (uphill in electric potential terms), which decreases its potential energy $U = qV$.
</details>

---

**Q10.** Electric potential is a:

(a) Scalar quantity &emsp; (b) Vector quantity &emsp; (c) Tensor quantity &emsp; (d) Dimensionless quantity

<details><summary><b>Answer</b></summary>

**(a)** Electric potential is a scalar quantity — it has magnitude but no direction.
</details>

---

**Q11.** If $10\,J$ of work is done in moving a $2\,C$ charge between two points, the potential difference between those points is:

(a) $5\,V$ &emsp; (b) $20\,V$ &emsp; (c) $0.2\,V$ &emsp; (d) $50\,V$

<details><summary><b>Answer</b></summary>

**(a)** $\Delta V = W/q = 10/2 = 5\,V$
</details>

---

**Q12.** The dimensions of electric potential are:

(a) $[ML^2T^{-3}A^{-1}]$ &emsp; (b) $[MLT^{-2}A^{-1}]$ &emsp; (c) $[ML^2T^{-2}A^{-1}]$ &emsp; (d) $[ML^2T^{-3}A^{-2}]$

<details><summary><b>Answer</b></summary>

**(a)** $[V] = \text{J/C} = \frac{[ML^2T^{-2}]}{[AT]} = [ML^2T^{-3}A^{-1}]$
</details>

---

**Q13.** A proton and an alpha particle are accelerated through the same potential difference. The ratio of their final kinetic energies $KE_p : KE_\alpha$ is:

(a) $1:2$ &emsp; (b) $1:1$ &emsp; (c) $2:1$ &emsp; (d) $4:1$

<details><summary><b>Answer</b></summary>

**(a)** $KE = q\Delta V$. For proton: $KE_p = e\Delta V$. For alpha: $KE_\alpha = 2e\Delta V$. Ratio $= 1:2$.
</details>

---

**Q14.** The work done against the electric field in moving a charge from one point to another on an equipotential surface is:

(a) Positive &emsp; (b) Negative &emsp; (c) Zero &emsp; (d) Depends on the path

<details><summary><b>Answer</b></summary>

**(c)** On an equipotential surface, $\Delta V = 0$, so $W = q\Delta V = 0$.
</details>

---

**Q15.** $1\,\text{eV}$ is approximately equal to:

(a) $1.6\times10^{-19}$ J &emsp; (b) $1.6\times10^{-19}$ C &emsp; (c) $9.1\times10^{-31}$ J &emsp; (d) $6.25\times10^{18}$ J

<details><summary><b>Answer</b></summary>

**(a)** By definition, $1\,\text{eV} = 1.6\times10^{-19}$ J.
</details>

---

### Section B: Short Answer Questions (2–3 marks)

**Q16.** Define electric potential at a point. State its SI unit. Is it a scalar or vector?

<details><summary><b>Answer</b></summary>

**Electric potential** at a point is the work done by an external force in bringing a unit positive test charge from infinity to that point without acceleration.

$$V = \frac{W_{\infty\to P}}{q_0}$$

**SI unit:** Volt (V) = Joule/Coulomb (J/C).

It is a **scalar** quantity.
</details>

---

**Q17.** What is the work done in moving a charge of $5\,\mu C$ through a potential difference of $-200\,V$?

<details><summary><b>Answer</b></summary>

$W = q\Delta V = 5\times10^{-6}\times(-200) = -10^{-3}$ J $= -1\,\text{mJ}$

The negative sign means the electric field does this work (the charge moved downhill — from higher to lower potential).
</details>

---

**Q18.** The potential at point A is $600\,V$ and at B is $-200\,V$. How much work is done by an external agent to move $+3\,\mu C$ from A to B?

<details><summary><b>Answer</b></summary>

$W_{ext} = q(V_B - V_A) = 3\times10^{-6}\times(-200 - 600) = 3\times10^{-6}\times(-800)$

$W_{ext} = -2.4\times10^{-3}\,\text{J} = \mathbf{-2.4\,\text{mJ}}$

Negative work — the external agent actually restrains the charge (the field assists the motion from A to B).
</details>

---

**Q19.** A charge of $+4\,\mu C$ is moved in a path from point P to Q to R. If $V_P = 100\,V$, $V_Q = 50\,V$, $V_R = 100\,V$, find the total work done by the external agent.

<details><summary><b>Answer</b></summary>

$W_{ext} = q(V_{final} - V_{initial}) = 4\times10^{-6}\times(V_R - V_P) = 4\times10^{-6}\times(100 - 100)$

$W_{ext} = \mathbf{0}$

Because the electrostatic force is conservative, the work depends only on initial and final positions — not on the path (through Q is irrelevant). Since $V_P = V_R$, the net work is zero.
</details>

---

**Q20.** Why does an electron accelerated from rest through $1\,V$ gain exactly $1\,\text{eV}$ of kinetic energy? Derive from first principles.

<details><summary><b>Answer</b></summary>

The electron has charge $q = e = 1.6\times10^{-19}$ C. When accelerated through potential difference $\Delta V = 1$ V, the work done by the field equals the gain in kinetic energy:

$KE = q\Delta V = e \times 1 = e$ joules $= 1\,\text{eV}$

The electron-volt is defined as the kinetic energy gained by an electron (charge $e$) through exactly $1\,V$. This is why the unit and the calculation agree by definition.
</details>

---

**Q21.** Two points A and B are at potentials $-100\,V$ and $+300\,V$ respectively. (a) Which point is at higher potential? (b) In which direction will an electron naturally move?

<details><summary><b>Answer</b></summary>

(a) Point **B** is at higher potential ($+300\,V > -100\,V$).

(b) An electron (negative charge) moves from lower to higher potential — so from A to B. This is because the electron's potential energy $U = qV = (-e)V$ is **lower** at higher $V$. The electron moves to minimize its potential energy.
</details>

---

**Q22.** The potential at a point changes from $100\,V$ to $-50\,V$ as we move $5\,\text{cm}$ in the x-direction. Estimate the electric field in this direction.

<details><summary><b>Answer</b></summary>

$E = -\frac{\Delta V}{\Delta x} = -\frac{-50-100}{5\times10^{-2}} = -\frac{-150}{0.05} = +3000\,\text{V/m}$

The field is **3000 V/m in the positive x-direction** (from high to low potential, but since potential decreased in the positive x-direction, the field points in the positive x-direction).
</details>

---

**Q23.** Is it possible for the potential to be zero at a point where the electric field is nonzero? Give an example.

<details><summary><b>Answer</b></summary>

**Yes.** The simplest example: at the midpoint between two equal and opposite charges ($+q$ at $-d$ and $-q$ at $+d$). The potential at the midpoint is zero ($V = kq/d + k(-q)/d = 0$), but the electric field at the midpoint is nonzero (both fields add, both pointing in the same direction).

Another example: on the equatorial plane of an electric dipole — potential is zero everywhere on this plane, but the field points antiparallel to $\vec{p}$.
</details>

---

**Q24.** An $\alpha$-particle and a proton are accelerated through the same potential difference $V$. Show that the de Broglie wavelength ratio $\lambda_\alpha/\lambda_p = 1/(2\sqrt{2})$.

<details><summary><b>Answer</b></summary>

After acceleration: $KE = q\Delta V$

Momentum: $p = \sqrt{2mKE} = \sqrt{2m\cdot q\Delta V}$

De Broglie wavelength: $\lambda = h/p = h/\sqrt{2mqV}$

$$\frac{\lambda_\alpha}{\lambda_p} = \frac{\sqrt{2m_p e V}}{\sqrt{2m_\alpha\cdot 2e\cdot V}} = \sqrt{\frac{m_p}{2m_\alpha}} = \sqrt{\frac{m_p}{2\times4m_p}} = \sqrt{\frac{1}{8}} = \frac{1}{2\sqrt{2}}$$
</details>

---

### Section C: Long Answer / Numerical Questions (3–5 marks)

**Q25.** A uniform electric field of $3\times10^4\,\text{V/m}$ exists between two parallel plates separated by $10\,\text{cm}$.

(a) Calculate the potential difference between the plates.  
(b) If an electron starts from rest at the negative plate, what is its kinetic energy when it reaches the positive plate (in eV)?  
(c) What is its speed at that point?

<details><summary><b>Answer</b></summary>

**(a)** $\Delta V = Ed = 3\times10^4\times0.10 = \mathbf{3000\,V}$

**(b)** $KE = e\Delta V = 1\times3000 = \mathbf{3000\,eV}$ (since the electron has charge $e$ and moves through $3000\,V$)

In joules: $3000\times1.6\times10^{-19} = 4.8\times10^{-16}\,J$

**(c)** $\frac{1}{2}m_e v^2 = 4.8\times10^{-16}$

$v = \sqrt{\frac{2\times4.8\times10^{-16}}{9.1\times10^{-31}}} = \sqrt{1.055\times10^{15}} = \mathbf{3.25\times10^7\,\text{m/s}}$

(~11% of speed of light — relativistic effects just beginning to matter)
</details>

---

**Q26.** Three charges $q_1 = +2\,\mu C$, $q_2 = -4\,\mu C$, $q_3 = +6\,\mu C$ lie on the x-axis at $x = 0$, $x = 0.3\,\text{m}$, $x = 0.6\,\text{m}$ respectively.

(a) Find the potential at the origin due to $q_2$ and $q_3$.  
(b) Find the total potential at $x = 0.3\,\text{m}$.  
(c) How much work is needed to bring a $+1\,\mu C$ charge from infinity to $x = 0.3\,\text{m}$?

<details><summary><b>Answer</b></summary>

**(a)** At origin ($x=0$), distance to $q_2 = 0.3\,\text{m}$, to $q_3 = 0.6\,\text{m}$:

$V_{q_2} = \frac{9\times10^9\times(-4\times10^{-6})}{0.3} = -120{,}000\,V$

$V_{q_3} = \frac{9\times10^9\times6\times10^{-6}}{0.6} = +90{,}000\,V$

$V_{total} = -120000 + 90000 = \mathbf{-30{,}000\,V}$

**(b)** At $x = 0.3\,\text{m}$ (due to $q_1$, $q_2$, $q_3$). Distances: to $q_1 = 0.3\,\text{m}$, to $q_2 = 0$, to $q_3 = 0.3\,\text{m}$.

$q_2$ is at that point — potential diverges (undefined/infinite). The potential due to a point charge at its own location is undefined. The question should ask for the potential due to $q_1$ and $q_3$ at the location of $q_2$:

$V = \frac{9\times10^9\times2\times10^{-6}}{0.3} + \frac{9\times10^9\times6\times10^{-6}}{0.3} = 60000 + 180000 = \mathbf{+240{,}000\,V}$

**(c)** Work $= q\times V = 1\times10^{-6}\times240000 = \mathbf{0.24\,J}$
</details>

---

**Q27.** An oil droplet of mass $m = 1.8\times10^{-15}\,\text{kg}$ carries $10$ electrons of excess charge. It is suspended motionless between vertical plates separated by $2\,\text{cm}$. Find the potential difference required. (g = $10\,\text{m/s}^2$)

<details><summary><b>Answer</b></summary>

For equilibrium: Electric force = Gravitational force

$qE = mg$

$q\frac{\Delta V}{d} = mg$

$\Delta V = \frac{mgd}{q} = \frac{1.8\times10^{-15}\times10\times0.02}{10\times1.6\times10^{-19}}$

$\Delta V = \frac{3.6\times10^{-16}}{1.6\times10^{-18}} = \mathbf{225\,V}$
</details>

---

**Q28.** Two parallel plates are at potentials $+3000\,V$ and $-1000\,V$. A proton is released from rest at the positive plate.

(a) What is the potential difference?  
(b) What kinetic energy does the proton gain?  
(c) What is the speed of the proton when it hits the negative plate?

<details><summary><b>Answer</b></summary>

**(a)** $\Delta V = 3000 - (-1000) = \mathbf{4000\,V}$

**(b)** $KE = e\Delta V = 1.6\times10^{-19}\times4000 = \mathbf{6.4\times10^{-16}\,J = 4000\,eV}$

**(c)** $v = \sqrt{\frac{2KE}{m_p}} = \sqrt{\frac{2\times6.4\times10^{-16}}{1.67\times10^{-27}}} = \sqrt{7.66\times10^{11}} = \mathbf{8.75\times10^5\,\text{m/s}}$
</details>

---

**Q29.** Explain why electric potential is more useful than electric field in many situations. Give two practical examples where potential-based analysis is preferred.

<details><summary><b>Answer</b></summary>

**Why potential is more useful:**

1. **Scalar vs. vector:** Potential is a scalar — it adds algebraically. Electric field is a vector — it requires component-wise addition. For multiple charges, calculating potential is far simpler.

2. **Direct energy connection:** Potential directly gives the energy per unit charge: $U = qV$. Energy calculations are immediate.

3. **Path independence:** Work depends only on the potential at start and end points — the path is irrelevant.

**Practical examples:**

1. **Battery voltage:** A battery is rated by its potential difference (e.g., 9 V), which tells you exactly how much work per unit charge it can do — without needing to know the field configuration inside.

2. **Particle accelerators:** Engineers design accelerating stages based on the potential difference. The final kinetic energy of a particle is simply $q\Delta V$ — no knowledge of field geometry is needed.
</details>

---

**Q30.** A charge $q$ is moved from point A to B along three different paths:
- Path 1: Direct straight line, length $L$
- Path 2: Semicircular arc, radius $r$
- Path 3: Zigzag path of total length $5L$

The potential difference $V_A - V_B = 50\,V$ and $q = +2\,\mu C$. Find the work done by the external agent for each path. What fundamental property of the electrostatic force does this illustrate?

<details><summary><b>Answer</b></summary>

For all three paths:

$W_{ext} = q(V_B - V_A) = 2\times10^{-6}\times(V_B - V_A) = 2\times10^{-6}\times(-50)$

$W_{ext} = \mathbf{-10^{-4}\,J = -0.1\,mJ}$ for all three paths.

The external agent does the same work $(-0.1\,\text{mJ})$ regardless of the path taken. The negative sign means the electric field does positive work (it assists the charge — the charge is moving downhill from A to B).

**Fundamental property illustrated:** The electrostatic force is **conservative**. The work done by or against it depends only on the initial and final positions, not on the path. This is why we can define a scalar potential function $V(\vec{r})$.
</details>

---

**Q31.** The potential at a point P due to a charge configuration is $V_P = 600\,V$. Another configuration is added, lowering the potential at P to $400\,V$. How much work must be done against the electric field to bring a $-5\,\mu C$ charge from infinity to P, (a) before and (b) after the second configuration is added?

<details><summary><b>Answer</b></summary>

$W_{against field} = -W_{by field} = -q(V_\infty - V_P) = q(V_P - 0) = qV_P$

Wait — $W_{against\ field} = W_{external} = q(V_P - V_\infty) = q\cdot V_P$

**(a)** $W = (-5\times10^{-6})\times600 = \mathbf{-3\times10^{-3}\,J = -3\,mJ}$

(Negative work against the field — the field actually assists bringing a negative charge towards positive potential. The external agent must restrain it.)

**(b)** $W = (-5\times10^{-6})\times400 = \mathbf{-2\times10^{-3}\,J = -2\,mJ}$
</details>

---

**Q32.** Derive the expression $V = W/q$ from the definition of potential energy, explaining why the test charge must be infinitesimally small and brought quasi-statically.

<details><summary><b>Answer</b></summary>

**Why infinitesimally small:** A test charge $q_0$ must not disturb the source charge distribution. If $q_0$ is large, it would exert forces on the source charges, rearranging them and changing the field we are trying to measure. By making $q_0\to0$, we probe the field without altering it.

**Why quasi-static:** If the charge is moved with acceleration, it gains kinetic energy. The work done by the external force would then split between potential energy and kinetic energy: $W_{ext} = \Delta U + \Delta KE$. By moving quasi-statically ($\Delta KE = 0$), all the external work goes into potential energy, and we can cleanly define $U = W_{ext}$.

**Derivation:**
- External work quasi-statically: $W_{ext} = \Delta U = U_P - U_\infty$
- Setting $U_\infty = 0$ (reference at infinity): $W_{ext} = U_P$
- Potential energy is proportional to $q_0$: $U_P = q_0 V_P$
- Therefore: $V_P = U_P/q_0 = W_{ext}/q_0$

$$\boxed{V_P = \frac{W_{\infty\to P}^{ext}}{q_0}}$$
</details>

---

*Next: [Chapter 2 — Potential Due to a Point Charge →](./02_potential_point_charge.md)*
