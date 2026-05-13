# Chapter 9: Electrostatics of Conductors

> *NCERT Section 2.9*

---

### The Paradox of the Hollow Fortress

Here is a fact that should astonish you: during a lightning storm, the safest place to be is **inside a metal car**. Not because of the rubber tires (a common myth), but because the metal body acts as a **Faraday cage** — the electric field inside the car is exactly zero, regardless of how intense the lightning is outside.

But wait. Metal is a *conductor*. It is full of free electrons. If a massive electric field hits the outside of the car, why doesn't it penetrate through the metal and electrocute the passengers inside?

The answer reveals something profound about conductors: they don't just *passively sit* in an electric field. They *actively rearrange themselves* to nullify the field inside. The free electrons redistribute almost instantaneously, creating a counter-field that perfectly cancels the external field within the bulk of the conductor.

This is not a design feature. It is a thermodynamic inevitability.

---

### Building the Concept: The Six Properties

#### Property 1: The Electric Field Inside a Conductor is Zero

If there were a field inside the conductor, the free electrons would experience a force and would move. They would continue moving until their redistribution creates an internal field that exactly cancels the external field. This process takes a fraction of a nanosecond.

In equilibrium: $\vec{E}_{inside} = 0$.

> This is not approximate — it is exactly zero. Even one microscopic nonzero field inside the conductor would drive electron motion, contradicting the assumption of equilibrium.

#### Property 2: Charge Resides Only on the Surface

Apply Gauss's Law to any closed surface drawn entirely within the conductor. Since $\vec{E} = 0$ everywhere inside, the flux through this Gaussian surface is zero. By Gauss's Law, the enclosed charge must be zero.

Therefore, **all excess charge resides on the outer surface** of the conductor. The interior is charge-free.

#### Property 3: The Electric Field at the Surface is Perpendicular

If the field had a tangential component at the surface, free electrons on the surface would move along the surface, redistributing until the tangential component vanishes.

In equilibrium: $\vec{E}$ at the surface is **perpendicular** (normal) to the surface at every point.

The magnitude of this surface field is:

$$E = \frac{\sigma}{\epsilon_0}$$

where $\sigma$ is the local surface charge density.

#### Property 4: The Entire Conductor is an Equipotential

Since $\vec{E} = 0$ inside and has no tangential component on the surface, the potential difference between *any* two points on or inside the conductor is:

$$\Delta V = -\int \vec{E} \cdot d\vec{l} = 0$$

Therefore, $V = \text{constant}$ throughout the conductor — surface and interior alike.

#### Property 5: Electrostatic Shielding

A cavity inside a conductor is completely shielded from external electric fields. No matter what happens outside, the field inside the cavity remains zero (assuming no charge is placed inside the cavity).

This is the principle of the **Faraday cage** — and why sensitive electronic instruments are enclosed in metal housings.

#### Property 6: Surface Charge Density Varies with Curvature

On an irregularly shaped conductor, charge concentrates where the surface curves sharply (high curvature = small radius of curvature). At pointed tips, $\sigma$ can become extremely large, creating intense electric fields.

$$\sigma \propto \frac{1}{R} \quad \text{(for a charged conductor)}$$

This is why **corona discharge** occurs at sharp points and why lightning rods are pointed.

---

### Checkpoint 1: Conceptual Mastery

**Problem 1:** A solid conducting sphere of radius $R$ carries a total charge $Q$. Find the electric field and potential (a) at $r > R$, (b) at $r = R$, (c) at $r < R$.

<details><summary><b>Solution</b></summary>

**(a) Outside ($r > R$):**

The sphere behaves exactly like a point charge $Q$ at the center.

$E = \frac{kQ}{r^2}$, $V = \frac{kQ}{r}$

**(b) At the surface ($r = R$):**

$E = \frac{kQ}{R^2} = \frac{\sigma}{\epsilon_0}$, $V = \frac{kQ}{R}$

**(c) Inside ($r < R$):**

$E = \textbf{0}$, $V = \frac{kQ}{R}$ (constant, equal to the surface potential)

The potential inside is **not zero** — it is a constant equal to the surface value. A common mistake is to confuse "zero field" with "zero potential."
</details>

**Problem 2:** A conducting sphere of radius $10$ cm has a surface charge density of $\sigma = 1.77 \times 10^{-6}$ C/m². Find (a) the total charge, (b) the electric field just outside the surface, (c) the potential at the center.

<details><summary><b>Solution</b></summary>

(a) $Q = \sigma \times 4\pi R^2 = 1.77 \times 10^{-6} \times 4\pi(0.1)^2 = 1.77 \times 10^{-6} \times 0.1257$

$Q = \textbf{2.22 × 10⁻⁷ C ≈ 0.222 μC}$

(b) $E = \frac{\sigma}{\epsilon_0} = \frac{1.77 \times 10^{-6}}{8.85 \times 10^{-12}} = \textbf{2 × 10⁵ V/m = 200 kV/m}$

(c) The potential at the center equals the potential at the surface (constant throughout the conductor):

$V = \frac{kQ}{R} = \frac{9 \times 10^9 \times 2.22 \times 10^{-7}}{0.1} = \textbf{20,000 V = 20 kV}$
</details>

---

### Checkpoint 2: The Gauntlet — "The Concentric Shell Problem"

*A physicist has a solid conducting sphere of radius $a = 5$ cm carrying charge $+Q_1 = +6\mu C$. She then encloses it inside a hollow conducting spherical shell (inner radius $b = 10$ cm, outer radius $c = 15$ cm) carrying a net charge of $+Q_2 = +4\mu C$.*

**Problem 1:** What are the charges on the inner and outer surfaces of the shell?

<details><summary><b>Solution</b></summary>

The field inside the conducting material of the shell must be zero. Draw a Gaussian surface within the shell material (between $r = b$ and $r = c$). The flux must be zero, so the total enclosed charge must be zero.

Enclosed charge = $Q_1 + Q_{inner\ surface} = 0$

$Q_{inner} = -Q_1 = \textbf{-6 μC}$

The total charge on the shell is $+4 \mu C$:

$Q_{inner} + Q_{outer} = +4 \mu C$

$Q_{outer} = +4 - (-6) = \textbf{+10 μC}$
</details>

**Problem 2:** Find the electric field at (a) $r = 3$ cm, (b) $r = 7$ cm, (c) $r = 12$ cm, (d) $r = 20$ cm.

<details><summary><b>Solution</b></summary>

(a) $r = 3$ cm (inside the solid sphere): $E = \textbf{0}$ (conductor)

(b) $r = 7$ cm (between sphere and shell):

$E = \frac{kQ_1}{r^2} = \frac{9 \times 10^9 \times 6 \times 10^{-6}}{(0.07)^2} = \frac{54000}{0.0049}$

$E = \textbf{1.1 × 10⁷ V/m}$

(c) $r = 12$ cm (inside shell material): $E = \textbf{0}$ (conductor)

(d) $r = 20$ cm (outside everything):

Total enclosed charge = $Q_1 + Q_2 = 6 + 4 = 10\mu C$

$E = \frac{k \times 10 \times 10^{-6}}{(0.2)^2} = \frac{90000}{0.04} = \textbf{2.25 × 10⁶ V/m}$
</details>

**Problem 3:** Find the potential at the center of the system.

<details><summary><b>Solution</b></summary>

To find the potential at the center, we must add contributions from all charge distributions:

$V_{center} = \frac{kQ_1}{a} + \frac{k(-6 \times 10^{-6})}{b} + \frac{k(10 \times 10^{-6})}{c}$

Wait — the potential due to a uniformly charged shell at any point inside it equals $kQ/R$ where $R$ is the shell's radius.

$V_{center} = \frac{k \times 6 \times 10^{-6}}{0.05} + \frac{k \times (-6 \times 10^{-6})}{0.10} + \frac{k \times 10 \times 10^{-6}}{0.15}$

$V = k \times 10^{-6}\left(\frac{6}{0.05} - \frac{6}{0.10} + \frac{10}{0.15}\right)$

$V = 9 \times 10^3 \left(120 - 60 + 66.67\right) = 9 \times 10^3 \times 126.67$

$V = \textbf{1.14 × 10⁶ V ≈ 1.14 MV}$
</details>

---

### Checkpoint 3: Electrostatic Shielding

**Problem 1:** A sensitive galvanometer is placed inside a thick hollow metal box. A strong external electric field of $10^6$ V/m is applied. What electric field does the galvanometer experience?

<details><summary><b>Solution</b></summary>

$E_{inside} = \textbf{0}$

The metal box acts as a Faraday cage. Free electrons in the box rearrange to completely cancel the external field within the cavity. The galvanometer is perfectly shielded.
</details>

**Problem 2:** Can we shield a region from a *gravitational* field using a similar approach?

<details><summary><b>Solution</b></summary>

**No.** Gravitational "charge" (mass) is always positive — there are no negative masses to redistribute. Therefore, there is no mechanism for self-cancellation inside a conductor. Electrostatic shielding works specifically because electric charges come in two signs.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** A large flat conducting plate has a surface charge density of $\sigma = 2 \times 10^{-6}$ C/m² on its upper surface. A small metal sphere of radius $1$ cm, initially uncharged, is placed $0.5$ m above the plate.

(a) What is the electric field between the plate and the sphere (ignoring edge effects)?  
(b) Does the sphere become charged? If so, what kind of charge appears on its lower surface?  
(c) The sphere is now grounded (connected to Earth) briefly and then disconnected. What charge does it acquire?  
(d) After grounding, is the sphere attracted to or repelled from the plate?

<details><summary><b>Solution</b></summary>

**(a)** The field due to an infinite charged plate: $E = \frac{\sigma}{2\epsilon_0}$. But for a conductor, the charge sits on one surface, so the field above it is:

$E = \frac{\sigma}{\epsilon_0} = \frac{2 \times 10^{-6}}{8.85 \times 10^{-12}} = \textbf{2.26 × 10⁵ V/m}$

(directed away from the plate, upward)

**(b)** Yes — by **electrostatic induction**. The external field from the plate pushes electrons in the sphere to the side facing *away* from the plate. The lower surface of the sphere (facing the plate) becomes positively charged, and the upper surface becomes negatively charged.

The sphere as a whole remains neutral, but it becomes *polarized*.

**(c)** When grounded, the excess electrons (on the upper surface) flow to Earth through the ground wire. The sphere is left with a net **positive** charge.

To estimate: The sphere is essentially at the potential of the surrounding field. $V = E \times d = 2.26 \times 10^5 \times 0.5 = 1.13 \times 10^5$ V (roughly).

For a sphere of radius $R$ at potential $V$: $Q = \frac{VR}{k} = \frac{1.13 \times 10^5 \times 0.01}{9 \times 10^9} \approx \textbf{1.26 × 10⁻⁷ C ≈ 0.126 μC}$

(This is approximate — the exact calculation requires image charges.)

**(d)** The sphere has positive charge, and the plate has positive charge. But the sphere is *closer* to the plate's field, and there's also an induced negative charge on the plate beneath the sphere. The dominant interaction is the **attraction** between the positive sphere and the induced negative charge on the plate. The sphere is **attracted**.
</details>

---

## Question Bank — Chapter 9

### Section A: MCQs (15 Questions)

**Q1.** Inside a charged conductor in electrostatic equilibrium, the electric field is:

(a) Maximum &emsp; (b) Minimum &emsp; (c) Zero &emsp; (d) Equal to the surface field

<details><summary><b>Answer</b></summary>**(c)** $\vec{E}_{inside} = 0$ always in electrostatic equilibrium.</details>

---

**Q2.** All excess charge on a conductor resides:

(a) In the interior &emsp; (b) On the outer surface &emsp; (c) Uniformly distributed &emsp; (d) Near the geometric center

<details><summary><b>Answer</b></summary>**(b)** By Gauss's Law applied inside the conductor: all excess charge is on the outer surface.</details>

---

**Q3.** The electric field just outside the surface of a conductor is:

(a) $\sigma/2\epsilon_0$ &emsp; (b) $\sigma/\epsilon_0$ &emsp; (c) $2\sigma/\epsilon_0$ &emsp; (d) $\sigma\epsilon_0$

<details><summary><b>Answer</b></summary>**(b)** $E = \sigma/\epsilon_0$ (normal to the surface).</details>

---

**Q4.** A Faraday cage protects its interior because:

(a) It absorbs electric fields &emsp; (b) Free electrons rearrange to cancel external field inside &emsp; (c) The walls are too thick &emsp; (d) Charge cannot enter metal

<details><summary><b>Answer</b></summary>**(b)** Free electrons redistribute to create an internal field that exactly cancels the external field inside.</details>

---

**Q5.** Two conducting spheres of radii $R$ and $2R$ are connected. The ratio of surface charge densities $\sigma_1/\sigma_2$ is:

(a) $1:2$ &emsp; (b) $2:1$ &emsp; (c) $1:4$ &emsp; (d) $4:1$

<details><summary><b>Answer</b></summary>**(b)** When connected: same potential. $Q \propto R$. $\sigma = Q/(4\pi R^2) \propto R/R^2 = 1/R$. $\sigma_1/\sigma_2 = R_2/R_1 = 2R/R = 2:1$.</details>

---

**Q6.** The electric field is tangential to the surface of a conductor in equilibrium.

(a) True &emsp; (b) False &emsp; (c) True only for spherical conductors &emsp; (d) True only for flat surfaces

<details><summary><b>Answer</b></summary>**(b)** False. The field is always **perpendicular** (normal) to the surface in equilibrium. Any tangential component would drive current.</details>

---

**Q7.** A conducting sphere carries charge $+Q$. The potential at its center is:

(a) Zero &emsp; (b) $kQ/R$ (same as surface) &emsp; (c) Greater than $kQ/R$ &emsp; (d) Less than $kQ/R$

<details><summary><b>Answer</b></summary>**(b)** The potential is constant throughout the conductor, equal to the surface potential $kQ/R$.</details>

---

**Q8.** Corona discharge occurs preferentially at sharp points because:

(a) Charge density is lower there &emsp; (b) Field is weaker there &emsp; (c) Charge density and field are higher there &emsp; (d) Insulation is thinner there

<details><summary><b>Answer</b></summary>**(c)** $\sigma \propto 1/R$ (curvature). Sharp points (small $R$) have high $\sigma$, hence high $E = \sigma/\epsilon_0$, causing ionization of air.</details>

---

**Q9.** A charge is placed inside a hollow conducting sphere. The charge on the inner surface is:

(a) Zero &emsp; (b) Equal and opposite to the enclosed charge &emsp; (c) Equal to the enclosed charge &emsp; (d) Double the enclosed charge

<details><summary><b>Answer</b></summary>**(b)** By Gauss's Law (Gaussian surface in conductor material): $Q_{inner} = -Q_{enclosed}$.</details>

---

**Q10.** The potential inside a conducting cavity (with no charge inside the cavity) is:

(a) Always zero &emsp; (b) Equal to the outer surface potential &emsp; (c) Depends on external field &emsp; (d) Varies with position

<details><summary><b>Answer</b></summary>**(b)** The cavity is shielded. The potential inside equals the conductor's (surface) potential — a constant.</details>

---

**Q11.** Two conducting spheres (radii $R_1 < R_2$, same potential) have surface charge densities $\sigma_1$ and $\sigma_2$. Then:

(a) $\sigma_1 < \sigma_2$ &emsp; (b) $\sigma_1 = \sigma_2$ &emsp; (c) $\sigma_1 > \sigma_2$ &emsp; (d) Cannot be determined

<details><summary><b>Answer</b></summary>**(c)** Same potential means $Q \propto R$. $\sigma = Q/(4\pi R^2) \propto 1/R$. Smaller $R_1$ → larger $\sigma_1$.</details>

---

**Q12.** A neutral conducting shell surrounds a $+Q$ charge at its center. What charge appears on the outer surface?

(a) $0$ &emsp; (b) $-Q$ &emsp; (c) $+Q$ &emsp; (d) $+2Q$

<details><summary><b>Answer</b></summary>**(c)** Inner surface gets $-Q$ (induced). Shell is neutral: $-Q + Q_{outer} = 0 \Rightarrow Q_{outer} = +Q$.</details>

---

**Q13.** The electric field inside a conductor is zero. This is because:

(a) The conductor is uncharged &emsp; (b) Induced charges exactly cancel external fields &emsp; (c) Electrons can't move in conductors &emsp; (d) The conductor is a perfect diamagnetic material

<details><summary><b>Answer</b></summary>**(b)** Free electrons rearrange until induced charges produce a field that exactly cancels any applied external field.</details>

---

**Q14.** If a $+5\,\mu C$ charge is placed inside a hollow conductor with $+3\,\mu C$ on it, the charge on the outer surface is:

(a) $+3\,\mu C$ &emsp; (b) $-5\,\mu C$ &emsp; (c) $+8\,\mu C$ &emsp; (d) $-2\,\mu C$

<details><summary><b>Answer</b></summary>**(c)** Inner surface: $-5\,\mu C$. Outer surface = total charge on shell + $5\,\mu C = 3 + 5 = +8\,\mu C$.</details>

---

**Q15.** The surface of a conductor in equilibrium is always an equipotential because:

(a) The field inside is zero, so no potential gradient along surface &emsp; (b) Conductors have infinite resistance &emsp; (c) Charge density is uniform &emsp; (d) All of the above

<details><summary><b>Answer</b></summary>**(a)** Since $E_{inside} = 0$, there's no potential gradient inside or along the surface ($E_{tangential} = 0$ → $\partial V/\partial l = 0$ → $V = $ constant on surface).</details>

---

### Section B: Short Answer Questions

**Q16.** State and explain the six properties of conductors in electrostatic equilibrium.

<details><summary><b>Answer</b></summary>

1. **$E_{inside} = 0$:** Free electrons rearrange until internal field is cancelled.
2. **Charge on outer surface:** Gauss's Law within conductor gives zero enclosed charge inside.
3. **Field perpendicular at surface:** Any tangential $E$ would drive surface current — equilibrium requires $E_{tangential} = 0$.
4. **Conductor is an equipotential:** No potential gradient since $E = 0$ inside.
5. **Electrostatic shielding:** External fields cannot penetrate a hollow conductor's cavity.
6. **$\sigma \propto 1/R$:** Charge concentrates at high-curvature (sharp) regions.
</details>

---

**Q17.** A conducting sphere of radius $5$ cm carries $+10\,\mu C$. Find (a) surface charge density, (b) field at $r = 5$ cm, (c) field at $r = 3$ cm, (d) potential at $r = 5$ cm, (e) potential at $r = 3$ cm.

<details><summary><b>Answer</b></summary>

**(a)** $\sigma = Q/(4\pi R^2) = 10^{-5}/(4\pi\times0.0025) = \mathbf{3.18\times10^{-4}\,C/m^2}$

**(b)** $E = \sigma/\epsilon_0 = 3.18\times10^{-4}/8.85\times10^{-12} = \mathbf{3.6\times10^7\,V/m}$

Or: $E = kQ/R^2 = 9\times10^9\times10^{-5}/0.0025 = 3.6\times10^7$ V/m ✓

**(c)** $E_{inside} = \mathbf{0}$ (inside conductor)

**(d)** $V = kQ/R = 9\times10^9\times10^{-5}/0.05 = \mathbf{1.8\times10^6\,V}$

**(e)** $V_{inside} = V_{surface} = \mathbf{1.8\times10^6\,V}$ (constant throughout conductor)
</details>

---

**Q18.** Explain electrostatic shielding and one practical application.

<details><summary><b>Answer</b></summary>

**Electrostatic shielding:** When a conductor encloses a cavity, free electrons rearrange on the conductor's surface to completely cancel any external electric field within the cavity. The interior of the cavity experiences zero electric field regardless of external fields.

**Mechanism:** External field induces surface charges on the outer surface of the conductor. These induced charges create an equal and opposite field inside, resulting in $E_{net} = 0$ inside.

**Applications:**
1. **Faraday cage:** Sensitive instruments (galvanometers, oscilloscopes) are enclosed in metal boxes to shield from external EMI.
2. **Microwave ovens:** Metal walls contain the microwaves inside.
3. **Car during lightning:** Metal body shields passengers.
4. **Coaxial cables:** Outer conductor shields the inner signal wire.
</details>

---

**Q19.** A hollow conducting shell of inner radius $a$ and outer radius $b$ has charge $Q$ on it. A point charge $+q$ is placed at the center. Find the field and potential at $r = a/2$, $r = (a+b)/2$, and $r = 2b$.

<details><summary><b>Answer</b></summary>

Charge distribution: Inner surface $= -q$, Outer surface $= Q + q$.

**At $r = a/2$ (inside cavity):**
$E = kq/r^2 = kq/(a/2)^2 = 4kq/a^2$; $V = kq/r + k(-q)/a + k(Q+q)/b$

**At $r = (a+b)/2$ (inside conductor):**
$E = 0$; $V = $ constant (same as outer surface potential) $= k(Q+q)/b$

**At $r = 2b$ (outside):**
$E = k(Q+q)/(2b)^2 = k(Q+q)/(4b^2)$; $V = k(Q+q)/(2b)$
</details>

---

**Q20.** Why is it unsafe to stand under a tall isolated tree during a lightning storm, but relatively safe inside a car?

<details><summary><b>Answer</b></summary>

**Tree:** A tall tree acts as a conductor pointing upward toward the charged cloud. Its tip creates extremely high electric field (sharp-point effect: $\sigma \propto 1/R$, high $E$ at tip), causing corona discharge and providing an ionized path for lightning to strike. Standing under a tree exposes you to branch-spread lightning and step potential.

**Car:** A car's metal body acts as a Faraday cage. When lightning strikes the car, current flows through the metal body (outer surface) and into the ground, without passing through the interior. Passengers inside experience zero electric field. The misconception that rubber tires protect you is wrong — lightning easily jumps hundreds of meters through air; rubber is irrelevant.
</details>

---

**Q21.** Two concentric spherical conductors, inner (radius $R_1$, charge $Q_1$) and outer (radius $R_2$, charge $Q_2$). Find the potential at (a) $r < R_1$, (b) $R_1 < r < R_2$, (c) $r > R_2$.

<details><summary><b>Answer</b></summary>

**(a)** $r < R_1$ (inside inner conductor):
$V = kQ_1/R_1 + kQ_2/R_2$ (constant — inside both conductors)

**(b)** $R_1 < r < R_2$ (between conductors):
$V = kQ_1/r + kQ_2/R_2$ (outside inner sphere, inside outer)

**(c)** $r > R_2$ (outside both):
$V = k(Q_1+Q_2)/r$
</details>

---

**Q22.** A conducting sphere of radius $R$ is placed in an external uniform field $E_0$. Explain qualitatively what happens to the field and potential, and why the sphere acts as an equipotential.

<details><summary><b>Answer</b></summary>

When placed in field $E_0$: electrons migrate to the side facing the field direction, leaving positive charge on the opposite side. This creates a dipole distribution on the sphere's surface.

This induced surface charge creates an internal field $E_{induced}$ that exactly cancels $E_0$ inside the sphere. The sphere is now an equipotential at potential $V = 0$ (by symmetry, if originally at zero potential).

Outside the sphere, the total field is the superposition of $E_0$ and the field of the induced dipole charge distribution. The field lines are distorted — they bunch up at the equator and are excluded from the sphere's interior.

Mathematically, the sphere's surface is an equipotential because $V_{sphere}$ satisfies the boundary condition that $V$ is constant on a sphere (a basic result from Laplace's equation in spherical geometry).
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** Sphere A (radius $5$ cm, charge $+6\,\mu C$) is enclosed by hollow shell B (inner $r = 10$ cm, outer $r = 15$ cm, charge $+4\,\mu C$). Find: (a) charges on inner and outer surfaces of B, (b) $E$ at $r = 7$ cm, (c) $V$ at center.

<details><summary><b>Answer</b></summary>

**(a)** Inner surface of B: $-6\,\mu C$ (induced). Outer surface: $4 - (-6) = +10\,\mu C$

**(b)** At $r = 7$ cm (between A and B): $E = kQ_A/r^2 = 9\times10^9\times6\times10^{-6}/(0.07)^2 = 1.1\times10^7$ V/m

**(c)** $V_{center} = kQ_A/R_A + k(-Q_A)/R_{inner} + k(Q_A+Q_B)/R_{outer}$
$= k\times10^{-6}[6/0.05 - 6/0.10 + 10/0.15] = 9\times10^3[120-60+66.7] = 9\times10^3\times126.7 = 1.14\times10^6$ V
</details>

---

**Q24.** Prove that the electric field just outside a conductor is $E = \sigma/\epsilon_0$ using Gauss's Law.

<details><summary><b>Answer</b></summary>

Draw a Gaussian "pillbox" surface straddling the conductor surface — one face inside the conductor (area $A$), one face outside.

Flux through inside face: $\Phi_{in} = E_{in}\times A = 0$ (field inside is zero)

Flux through outside face: $\Phi_{out} = E_{out}\times A$ (field is normal to surface)

Flux through sides: $\Phi_{sides} = 0$ (field is parallel to sides)

Total flux: $\Phi = E_{out}\times A$

Enclosed charge: $Q_{enc} = \sigma A$

By Gauss's Law: $E_{out}\times A = \sigma A/\epsilon_0 \Rightarrow \boxed{E_{out} = \sigma/\epsilon_0}$ ✓
</details>

---

**Q25.** A conducting sphere of radius $R$ has a charge $Q$ on it. A point charge $q$ is brought from infinity to a distance $d > R$ from the center. Find the work done.

<details><summary><b>Answer</b></summary>

Outside the sphere, it behaves as a point charge $Q$ at center.

$W_{ext} = q(V_f - V_i) = q(kQ/d - 0) = \mathbf{kqQ/d}$

This work is stored as electrostatic potential energy in the system.
</details>

---

**Q26.** Explain why grounding a conductor discharges it, even when no visible charge flow is seen.

<details><summary><b>Answer</b></summary>

**Grounding** connects a conductor to Earth (effectively an infinite reservoir of charge at zero potential). 

If the conductor is at potential $V > 0$: electrons flow from Earth to the conductor (to lower the potential). Net charge on conductor decreases.

If $V < 0$: electrons flow from conductor to Earth. Net charge increases toward zero.

The process continues until $V_{conductor} = V_{Earth} = 0$. The conductor is discharged — it has zero net charge (or just enough to maintain $V = 0$).

"No visible flow" occurs because the charge transferred may be tiny for small conductors, and the process is nearly instantaneous.
</details>

---

**Q27.** A conductor has a pointed tip of radius of curvature $r = 0.1$ mm. The total charge on it creates a uniform average field of $100$ kV/m. Estimate the field at the tip.

<details><summary><b>Answer</b></summary>

For a conductor, $E \propto \sigma \propto 1/R_{curvature}$ at the surface. The tip has much smaller $R$ than the average.

For a rough estimate: if the average dimension of the conductor is $\bar{R} \approx 1$ cm:

$E_{tip}/E_{avg} = R_{avg}/R_{tip} = 0.01/0.0001 = 100$

$E_{tip} \approx 100\times100\,\text{kV/m} = \mathbf{10\,MV/m}$

This exceeds the breakdown field of air ($\sim 3$ MV/m), causing corona discharge (lightning rod principle).
</details>

---

**Q28.** Two identical conducting spheres of radius $R$ carry charges $+3Q$ and $-Q$. They are brought into contact and separated. Find: (a) final charge on each, (b) force between them when separated by $d \gg R$.

<details><summary><b>Answer</b></summary>

**(a)** Total charge = $3Q + (-Q) = 2Q$. Equal sharing: each gets $Q$.

**(b)** $F = kQ^2/d^2$
</details>

---

**Q29.** A spherical conductor of radius $10$ cm has potential $V_0 = 500$ V. A second sphere of radius $20$ cm at far distance has $V_0 = 0$. If connected by a thin wire, find the final potential of the system.

<details><summary><b>Answer</b></summary>

$Q_1 = V_0 R_1/k = 500\times0.10/(9\times10^9) = 5.56\times10^{-9}$ C. $Q_2 = 0$.

Total charge $= Q_{total} = 5.56\times10^{-9}$ C.

After connection: same potential. $V_f = kQ_{total}/(R_1+R_2) = kQ_{total}/0.30 = 9\times10^9\times5.56\times10^{-9}/0.30 = 166.7$ V

Final charge: $Q_1' = V_f R_1/k = 166.7\times0.10/(9\times10^9) = 1.85\times10^{-9}$ C; $Q_2' = V_f R_2/k = 3.70\times10^{-9}$ C.

**Final potential $= 166.7$ V on both spheres.**
</details>

---

**Q30.** Can a conductor have a region of positive surface charge density and another region of negative surface charge density simultaneously? If yes, give an example.

<details><summary><b>Answer</b></summary>

**Yes.** This occurs when a conductor is placed in an external electric field or near a charge.

**Example:** A neutral conducting sphere placed near a positive charge $+Q$: electrons are attracted toward the near side, making it negatively charged ($\sigma < 0$). The far side has deficit of electrons, becoming positively charged ($\sigma > 0$). The conductor remains neutral overall but has both $+$ and $-$ regions.

This is electrostatic induction. The net charge is zero, but the charge distribution is non-uniform.
</details>

---

**Q31.** Find the potential at the center of a conducting spherical shell (inner radius $a$, outer radius $b$) that carries charge $Q$ on its outer surface only (no charge inside the cavity).

<details><summary><b>Answer</b></summary>

The shell has charge $Q$ on its outer surface. The inner surface has zero charge (since there's no enclosed charge).

$V_{center} = V_{inner\ surface} + V_{outer\ surface}$

$= k(0)/a + kQ/b = \mathbf{kQ/b}$

This equals the outer surface potential — the center potential equals the surface potential because the shell is an equipotential (no charge inside).
</details>

---

**Q32.** A flat conducting slab of large area is placed in a uniform field $E_0$. Find the induced surface charge density on each face.

<details><summary><b>Answer</b></summary>

The external field $E_0$ is perpendicular to the slab. Electrons migrate to the face opposing the field direction, leaving positive charge on the other face.

For the field inside the conductor to be zero, the induced surface charges must create a field that cancels $E_0$:

$E_{induced} = \sigma_{induced}/\epsilon_0 = E_0$

$\sigma_{induced} = \epsilon_0 E_0$

One face has $\sigma = +\epsilon_0 E_0$, the other has $\sigma = -\epsilon_0 E_0$. The net charge is zero (neutral slab).
</details>

---

*Next: [Chapter 10 — Dielectrics and Polarisation →](./10_dielectrics_and_polarisation.md)*
