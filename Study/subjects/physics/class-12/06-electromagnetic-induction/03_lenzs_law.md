# Chapter 3: Lenz's Law — Nature's Great Referee

> *NCERT Section 6.4*

*← [Chapter 2 — Faraday's Law](./02_faradays_law.md)*

---

## 🎯 Stage 1: The Core Idea

### The Stubborn Universe

Imagine you are pushing open a revolving door. The harder you push, the harder it seems to push back. It never just swings open and lets you sail through without effort. You always have to work against it. Now imagine the electromagnetic world has the same stubbornness built into it — every time you try to *change* a magnetic field through a coil, the coil *fights back* by generating a current that opposes you. This, in essence, is **Lenz's Law**.

Or think of it like a stubborn friend who *always* does the exact opposite of what you want. Push the flux up? The induced current pulls it back down. Pull the flux down? The induced current pushes it back up. The universe, according to Lenz's Law, is deeply, profoundly *contrary*.

---

### What is Lenz's Law?

> **Lenz's Law:** The direction of the induced current is always such that it **opposes** the change in magnetic flux that caused it.

Two critical words: **opposes** and **change**.

- The induced current does NOT oppose the flux itself — it opposes the *change* in flux.
- If flux is increasing, the induced current tries to *decrease* it.
- If flux is decreasing, the induced current tries to *increase* it.

This law was formulated by **Heinrich Friedrich Emil Lenz** in 1834, and it is one of the most conceptually elegant laws in all of physics.

> 🔑 **Key Takeaway:** Lenz's Law gives the **DIRECTION** of induced current only. The **magnitude** is given by Faraday's Law. Together, they give the complete picture.

---

### Lenz vs. Faraday — Two Sides of the Same Coin

| Feature | Faraday's Law | Lenz's Law |
|---------|--------------|------------|
| Tells us | **Magnitude** of induced EMF | **Direction** of induced current |
| Formula | $\varepsilon = -N\dfrac{d\Phi}{dt}$ | Encoded in the **negative sign** |
| Nature | Quantitative | Qualitative |
| Origin | Experimental observation | Consequence of energy conservation |
| Exam weight | Calculation-based questions | Conceptual, direction, assertion-reason |

> 💡 **Tip:** The negative sign in Faraday's formula is not just a mathematical symbol — it IS Lenz's Law expressed mathematically. Examiners love asking this!

---

### The 4-Step Direction-Finding Algorithm

This is the most powerful skill for Lenz's Law problems. Master this and every direction question becomes mechanical:

**Step 1:** Identify the direction of the existing external magnetic field (B).

**Step 2:** Determine whether the magnetic flux through the loop is **increasing** or **decreasing**.

**Step 3:** The induced B-field must **oppose** the change:
  - If external flux is **increasing** → induced B points **opposite** to external B
  - If external flux is **decreasing** → induced B points **same** direction as external B

**Step 4:** Use the **Right-Hand Curl Rule** to find the current direction from the induced B:
  - Point your right thumb in the direction of induced B inside the loop
  - Your fingers curl in the direction of induced current

> ⚠️ **Critical Insight:** Always find the direction of **induced B first**, THEN find current. Students who try to find current directly often get confused. Go B → current, not the other way around.

---

### Common Physical Scenarios at a Glance

| Scenario | Change in Flux | Induced B | Face of Coil (near magnet) | Effect |
|----------|---------------|-----------|--------------------------|--------|
| N-pole of magnet **approaching** coil | Increasing ↑ | Opposes (points away from magnet) | N-pole (repels magnet) | Resists approach |
| N-pole of magnet **receding** from coil | Decreasing ↓ | Same direction (points toward magnet) | S-pole (attracts magnet) | Resists recession |
| S-pole of magnet **approaching** coil | Increasing ↑ | Opposes (points toward magnet) | S-pole (repels magnet) | Resists approach |
| S-pole of magnet **receding** from coil | Decreasing ↓ | Same direction | N-pole (attracts magnet) | Resists recession |
| Loop being pulled **OUT** of B-field region | Decreasing ↓ | Same as external B | — | Force opposes pulling out |
| Loop being pushed **INTO** B-field region | Increasing ↑ | Opposes external B | — | Force opposes pushing in |

> ⚠️ **Critical Insight (S-pole confusion):** Remember — magnetic field lines go FROM North TO South *outside* the magnet. Near an approaching S-pole, the external field points TOWARD the S-pole (i.e., INTO the coil from the S-pole side). The induced current will oppose this increase by creating field pointing AWAY → coil's near face becomes S-pole → repels the approaching S-pole. This is consistent with the general rule: approaching magnet → repulsion regardless of which pole.

---

### Why Must Lenz's Law Be This Way? — The Energy Conservation Argument

This is perhaps the most important conceptual argument in electromagnetic induction. Here's the logical chain:

**Suppose Lenz's Law were REVERSED** — i.e., the induced current *aided* the flux change instead of opposing it:

1. Magnet approaches coil → flux increases
2. Induced current *adds* to flux (instead of opposing)
3. More flux → more induced current (by Faraday's law)
4. More current → even more flux → even more current → ...
5. **Runaway chain reaction** — current and flux grow to infinity
6. This generates **infinite electrical energy from nothing**
7. This **violates the Law of Conservation of Energy** ❌

Therefore, the induced current **MUST** oppose the change — not as an arbitrary rule, but as a logical necessity imposed by energy conservation.

> 🔑 **Key Takeaway:** Lenz's Law is not an independent law — it is a **consequence of the Law of Conservation of Energy**. This is the single most tested conceptual point in CBSE boards (appears almost every year since 2015).

> ⚠️ **Critical Insight:** The work done by an external agent to move the magnet against the repulsive (or attractive) electromagnetic force is exactly equal to the electrical energy generated in the circuit (which is dissipated as heat in the resistance). Energy is transformed, never created.

---

### Lenz's Law in Real Life — Where You See It Every Day

| Application | How Lenz's Law Acts |
|-------------|---------------------|
| **Electromagnetic braking** (maglev trains, roller coasters) | Moving conductor in B-field develops eddy currents → retarding force slows vehicle |
| **Metal detectors at airports** | Changing B-field from detector induces currents in metal objects → detector senses energy loss |
| **Induction cooktops** | Eddy currents in pot base generate heat; no flame needed |
| **AC transformer core losses** | Eddy currents in iron core dissipate energy (why laminated cores are used) |
| **Speedometers (older models)** | Rotating magnet near aluminum disc — eddy currents create drag proportional to speed |
| **Magnetic damping in galvanometers** | Coil oscillation is damped by induced currents opposing motion |

---

## 🔬 Stage 2: The Formula Lab

### The Master Formula

The negative sign in Faraday's Law is the mathematical statement of Lenz's Law:

$$\boxed{\varepsilon = -N\frac{d\Phi_B}{dt}}$$

For a single loop (N = 1):

$$\varepsilon = -\frac{d\Phi_B}{dt}$$

The flux itself:

$$\Phi_B = B \cdot A \cdot \cos\theta$$

where $\theta$ is the angle between **B** and the area vector $\hat{n}$.

---

### Variable Table

| Symbol | Meaning | SI Unit |
|--------|---------|---------|
| $\varepsilon$ | Induced EMF (electromotive force) | Volt (V) |
| $N$ | Number of turns in the coil | Dimensionless |
| $\Phi_B$ | Magnetic flux through one turn | Weber (Wb) = T·m² |
| $\dfrac{d\Phi_B}{dt}$ | Rate of change of magnetic flux | Weber/second = Volt |
| $B$ | Magnetic field strength | Tesla (T) |
| $A$ | Area of the loop/coil | m² |
| $\theta$ | Angle between **B** and area normal $\hat{n}$ | Radian or degree |

---

### What the Negative Sign Means

- If $\Phi_B$ is **increasing** with time → $\dfrac{d\Phi_B}{dt} > 0$ → $\varepsilon < 0$

  This means the EMF (and hence current) acts to **reduce** the flux — it creates a B-field opposing the increase. **This is Lenz's Law.**

- If $\Phi_B$ is **decreasing** with time → $\dfrac{d\Phi_B}{dt} < 0$ → $\varepsilon > 0$

  The EMF acts to **maintain** the flux — it creates a B-field in the same direction as the original. **This is Lenz's Law.**

> 💡 **Tip:** In numerical problems, use the magnitude $|\varepsilon| = N\left|\dfrac{d\Phi_B}{dt}\right|$ to find EMF magnitude, then use Lenz's Law separately to find direction. Never mix them up.

---

### Key Numbers to Memorize

| Quantity | Value |
|----------|-------|
| 1 Weber | 1 T·m² = 1 V·s |
| 1 Tesla | 1 Wb/m² |
| Earth's magnetic field | ~$3.5 \times 10^{-5}$ T (for context) |
| Typical EMF in CBSE numericals | mV to V range |

---

### Formalized 4-Step Algorithm (with Logic)

| Step | Action | Logic |
|------|--------|-------|
| **1** | Find direction of external $\vec{B}$ | Define reference direction |
| **2** | Find $\Delta\Phi$: Is flux increasing or decreasing? | Depends on relative motion |
| **3** | Determine induced $\vec{B}_{ind}$: must oppose $\Delta\Phi$ | Lenz's Law |
| **4** | Apply Right-Hand Curl Rule for current from $\vec{B}_{ind}$ | Ampere's right-hand rule |

---

### Retarding Force Formula (Preview of Section 6.6)

When a conductor of length $l$ moves with velocity $v$ in a field $B$ (perpendicular), and has resistance $R$:

$$\varepsilon = Blv \quad \text{(motional EMF)}$$

$$I = \frac{Blv}{R}$$

$$F_{retarding} = BIl = \frac{B^2l^2v}{R} \quad \text{(directed opposite to motion — Lenz!)}$$

This retarding force is the electromagnetic manifestation of Lenz's Law — it's always opposing the motion.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Magnet Approaching or Receding from a Coil ⭐

**Pattern:** "The [N/S]-pole of a bar magnet is [moved toward/pulled away from] the [left/right] face of a coil. Find the direction of induced current as seen from the [left/right]."

> 🔑 **Quick Rule:** Approaching magnet → near face becomes **same pole** (repulsion). Receding magnet → near face becomes **opposite pole** (attraction).

---

**Solved Example** 🟢

> The North pole of a bar magnet is moved toward the left face of a circular coil as shown. What is the direction of induced current in the coil as observed from the left side?

<details><summary><b>Solution</b></summary>

**Step 1:** External B-field points to the right (from N-pole toward S-pole), i.e., from left to right through the coil.

**Step 2:** As the N-pole approaches, the magnetic flux through the coil (pointing right) **increases**.

**Step 3:** By Lenz's Law, the induced B-field must oppose the increase → induced $\vec{B}_{ind}$ must point **to the left** (opposite to external B) inside the coil.

**Step 4:** Using Right-Hand Curl Rule — if induced B points to the left (toward the observer on the left), the current must flow **anticlockwise** as seen from the left.

**Answer:** Induced current flows **anticlockwise** when viewed from the left side.

**Physical Check:** The left face of the coil, with anticlockwise current as seen from outside-left, behaves as a **North pole** → it **repels** the approaching N-pole. ✅ (Consistent with Lenz's Law)

</details>

---

**Practice Questions:**

1. 🟢 The North pole of a bar magnet is **pulled away** from the right face of a coil. What is the direction of induced current as seen from the right?

<details><summary><b>Answer</b></summary>

As N-pole recedes (moves away to the right), flux through the coil (pointing right) **decreases**. Induced B must oppose the decrease → induced B points **to the right** inside the coil. By RHR, current flows **clockwise** as seen from the right.

**Check:** Right face becomes **S-pole** → attracts the receding N-pole → tries to prevent recession. ✅

</details>

2. 🟢 The South pole of a bar magnet is brought closer to the left face of a coil. Find the direction of induced current as seen from the left.

<details><summary><b>Answer</b></summary>

Near an approaching S-pole, external B-field (which enters S-pole) points **to the right** (away from observer on left, toward the S-pole on left). Wait — let's be careful. S-pole is on the left side approaching the left face. Field lines enter the S-pole from outside, so external B points **from right to left** (from inside the coil toward the S-pole on the left).

As S-pole approaches, flux pointing left **increases**.

Induced B must oppose → induced B points to the **right** inside the loop.

By RHR: current is **clockwise** as seen from the left.

**Check:** Left face with clockwise current (as seen from left) acts as **S-pole** → repels approaching S-pole. ✅

</details>

3. 🟡 A circular coil is placed with its plane perpendicular to a uniform magnetic field B = 0.5 T. The field starts decreasing at a rate of 0.1 T/s. The coil has N = 200 turns and area A = 50 cm². Find (a) the induced EMF and (b) describe the direction of induced current.

<details><summary><b>Answer</b></summary>

**(a)** $|\varepsilon| = N \cdot A \cdot \left|\dfrac{dB}{dt}\right| = 200 \times 50 \times 10^{-4} \times 0.1 = 200 \times 5 \times 10^{-4} = \mathbf{0.1 \text{ V}}$

**(b)** Since B is decreasing, flux is decreasing. By Lenz's Law, induced current must create B in the **same direction** as the original field — to try to maintain the flux. So induced current flows in a direction consistent with supporting the original B.

</details>

4. 🟡 A magnet is dropped through a horizontal coil connected to a galvanometer. Describe the deflections of the galvanometer as the magnet (N-pole first) falls: (a) before entering the coil, (b) when fully inside, (c) as it exits from the bottom.

<details><summary><b>Answer</b></summary>

**(a) Before entering (N-pole approaching from top):** Flux through coil increases downward. Induced current opposes → creates B upward inside → **anticlockwise** current when viewed from top → galvanometer deflects to one side (say, right).

**(b) When fully inside:** Flux is momentarily constant as the magnet passes the center → **no change in flux** → **no induced EMF → galvanometer reads zero**.

**(c) As it exits (N-pole leaving from bottom):** Downward flux through coil decreases. Induced current maintains flux → creates B downward → **clockwise** when viewed from top → galvanometer deflects to the **opposite side** (left).

**Key Note:** The galvanometer deflects in opposite directions during entry and exit — this is a classic experimental observation.

</details>

5. 🟡 Two identical coils A and B are placed coaxially. Coil A is connected to a battery and switch. When the switch is closed, what happens in coil B (if it's connected to a galvanometer)?

<details><summary><b>Answer</b></summary>

When the switch is closed, current in A grows from 0 to steady value → magnetic flux through B **increases** → by Lenz's Law, induced current in B opposes the increase → induced current in B flows in **opposite direction** to current in A → galvanometer deflects momentarily (only during transient, not at steady state).

When switch is opened: current in A decreases → flux through B decreases → induced current in B is in **same direction** as original current in A → galvanometer deflects momentarily in opposite direction.

</details>

6. 🔴 A bar magnet is placed along the axis of a solenoid (100 turns, area = 10 cm²). The magnet is rotated so that its axis becomes perpendicular to the solenoid axis. Given that the initial flux per turn was $2 \times 10^{-3}$ Wb and the rotation takes 0.2 s, find the average induced EMF.

<details><summary><b>Answer</b></summary>

Initial flux per turn: $\Phi_i = 2 \times 10^{-3}$ Wb

Final flux per turn: When magnet axis is perpendicular to solenoid axis, the field is perpendicular to the area vector → $\Phi_f = BA\cos 90° = 0$

Change in flux per turn: $\Delta\Phi = 0 - 2\times10^{-3} = -2\times10^{-3}$ Wb

$$|\varepsilon_{avg}| = N \cdot \frac{|\Delta\Phi|}{\Delta t} = 100 \times \frac{2\times10^{-3}}{0.2} = \mathbf{1 \text{ V}}$$

Direction: By Lenz's Law, as flux decreases, induced current tries to maintain it → flows to create B in same direction as original.

</details>

7. 🔴 **(NCERT Exemplar style)** A cylindrical bar magnet is placed with its axis along the axis of a solenoid and rotated about its own axis. Will there be an induced current in the solenoid?

<details><summary><b>Answer</b></summary>

**No induced current.**

The magnetic field of a cylindrical bar magnet has **rotational symmetry** about its own axis. When the magnet rotates about its own axis, the magnetic field pattern (and hence the magnetic flux through the solenoid) does **not change**.

Since $\dfrac{d\Phi}{dt} = 0$, by Faraday's law, $\varepsilon = 0$, and hence **no induced current**.

This is an important NCERT Exemplar result — don't confuse "rotation" with "changing flux."

</details>

8. 🔴 A coil is connected to a galvanometer. A student claims that if he moves both the magnet and the coil in the same direction at the same speed, no current will be induced. Is the student correct?

<details><summary><b>Answer</b></summary>

**Yes, the student is correct.**

Electromagnetic induction depends on the **relative motion** between the magnet and coil, not their absolute motion. If both move together at the same velocity, there is no relative motion → no change in flux through the coil → no induced EMF → no induced current.

This directly follows from Faraday's Law: $\varepsilon = -\dfrac{d\Phi}{dt}$, and since $\Phi$ doesn't change, $\varepsilon = 0$.

</details>

---

### Type 2: Conductor/Loop Moving In and Out of B-Field Region ⭐

**Pattern:** "A rectangular loop ABCD (or conducting rod) moves [into/out of] a magnetic field region (directed [into/out of] the page). Using Lenz's Law, determine the direction of induced current."

> 🔑 **Quick Rule:** Loop enters field → current opposes entry (flux increasing → induced B opposes external B). Loop exits field → current opposes exit (flux decreasing → induced B in same direction as external B).

---

**Solved Example** 🟡

> A rectangular loop ABCD (A top-left, B top-right, C bottom-right, D bottom-left) is being pulled to the **right**, partially overlapping a region where magnetic field B is directed **into the page**. The right portion of the loop is inside the field. Find the direction of induced current in the loop.

<details><summary><b>Solution</b></summary>

**Setting up:** As the loop moves right, more area enters the B-field region → flux through the loop (into the page) is **increasing**.

**Step 3 (Lenz):** Induced B must oppose the increase → induced $\vec{B}_{ind}$ points **out of the page** inside the loop.

**Step 4 (RHR):** For B coming out of the page inside the loop, curl right-hand fingers so thumb points out of page → fingers go **anticlockwise**: A→D→C→B→A (i.e., counterclockwise when viewed from front).

**Answer:** Current flows **A → D → C → B → A** (counterclockwise), i.e., **anticlockwise**.

**Physical Check:**
- The bottom conductor DC moves right through B-field (into page). By Fleming's right-hand rule (or $\vec{F} = q\vec{v}\times\vec{B}$): $\vec{v}$ is rightward, $\vec{B}$ is into page → force on positive charges is upward (D→C direction? Let's verify: $\hat{x} \times (-\hat{z}) = \hat{x} \times (-\hat{z}) = -(\hat{x}\times\hat{z}) = -(-\hat{y}) = +\hat{y}$ — upward, i.e., from D to C). This gives current D→C in the bottom arm, consistent with anticlockwise flow D→C→B→A→D. ✅

</details>

---

**Practice Questions:**

1. 🟢 A rectangular loop is being pulled completely **out** of a region of magnetic field directed **into the page** (moving rightward, with the field on the left side). Find the direction of induced current.

<details><summary><b>Answer</b></summary>

As loop exits, flux (into the page) **decreases**. Induced B must oppose decrease → induced B points **into the page** (same as external). By RHR: current flows **clockwise** (viewed from front).

If the loop is ABCD (A top-left, B top-right, C bottom-right, D bottom-left): current flows **A → B → C → D → A** (clockwise).

</details>

2. 🟢 A square loop moves from a region of zero field into a region of uniform field B (directed out of the page). What is the direction of induced current?

<details><summary><b>Answer</b></summary>

As loop enters, flux (out of page) **increases**. Induced B must oppose → induced B points **into the page** inside the loop. By RHR: current flows **clockwise** (viewed from front).

This clockwise current creates a magnetic moment opposing the external field — that's Lenz's Law. ✅

</details>

3. 🟡 A rectangular loop (resistance R = 2 Ω) of dimensions $l = 20$ cm, $w = 10$ cm moves with velocity $v = 5$ m/s perpendicular to a uniform field $B = 0.5$ T. Find (a) induced EMF, (b) induced current, and (c) direction of current if the loop moves into the field (B into page).

<details><summary><b>Answer</b></summary>

**(a)** As loop enters: the leading edge (length $l = 20$ cm = 0.2 m) cuts field lines.

$$\varepsilon = Blv = 0.5 \times 0.2 \times 5 = \mathbf{0.5 \text{ V}}$$

**(b)** $$I = \frac{\varepsilon}{R} = \frac{0.5}{2} = \mathbf{0.25 \text{ A}}$$

**(c)** B into page, flux increasing → induced B out of page → current **anticlockwise** (in the leading edge, current flows upward).

</details>

4. 🟡 A triangular loop PQR (right angle at Q) with PQ = 3 cm horizontal and QR = 4 cm vertical moves horizontally to the right into a region of uniform B (into the page). At a certain instant, only the vertical arm QR is inside the field. What is the EMF? Which arm carries the induced EMF?

<details><summary><b>Answer</b></summary>

Only arm QR (vertical, length = 4 cm = 0.04 m) is cutting field lines as the loop moves right with velocity $v$.

$$\varepsilon = Blv = B \times 0.04 \times v$$

(Numerical value depends on $v$ and $B$.)

The **QR arm** is the source of motional EMF. The hypotenuse PR, while also potentially cutting lines, is not perpendicular — only the vertical component of PR contributes, but since QR is fully inside, QR carries the full EMF.

Direction of current in QR: $\vec{v}$ (right), $\vec{B}$ (into page) → force on positive charges: $\vec{F} = q\vec{v}\times\vec{B}$ = upward (from Q to R). So current in QR flows from Q→R (upward).

</details>

5. 🟡 A conducting rod of length 1 m is moved with velocity 5 m/s in a direction making 30° with a uniform B = 2 T (perpendicular to the rod). Find the induced EMF.

<details><summary><b>Answer</b></summary>

The effective velocity component perpendicular to the rod in the plane of motion:

$$\varepsilon = Blv\sin\theta = 2 \times 1 \times 5 \times \sin 30° = 2 \times 1 \times 5 \times 0.5 = \mathbf{5 \text{ V}}$$

(Here, the component of velocity perpendicular to the rod is $v\sin\theta$.)

</details>

6. 🔴 A rectangular loop ABCD (AB = 10 cm, BC = 5 cm) is placed in a non-uniform B-field. The field at AB is 2 T (into page) and at CD is 1 T (into page). The loop is stationary. Is there an induced EMF? Explain using Lenz's Law.

<details><summary><b>Answer</b></summary>

**Yes, there is a net flux, but NO induced EMF if the field is static.**

Net flux: $\Phi = B_{AB} \times A - B_{CD} \times A$? No — we compute total flux:

Since $B$ varies across the loop, $\Phi = \int \vec{B}\cdot d\vec{A}$. For this static non-uniform field, the flux is some fixed value. Since the loop is **stationary** and $B$ is **not changing with time**, $\dfrac{d\Phi}{dt} = 0$ → **No induced EMF**.

Lenz's Law applies only when there is a **change in flux**. A non-uniform but static field gives a fixed flux → no induction.

</details>

7. 🔴 **(NCERT Exemplar concept)** A current-carrying circular loop is placed in a uniform magnetic field. It begins to contract (radius decreases). Using Lenz's Law, find the direction of induced current if B points out of the page.

<details><summary><b>Answer</b></summary>

As the loop contracts, its area decreases → flux (out of page) **decreases**.

By Lenz's Law: induced current must oppose the decrease → induced B must point **out of the page** inside the loop.

By RHR: current flows **anticlockwise** (as viewed from the front/B direction).

This anticlockwise current creates magnetic moment pointing out of page, opposing the decrease in flux. ✅

</details>

---

### Type 3: Conservation of Energy — Theoretical/Explanation Questions ⭐⭐ (MOST IMPORTANT FOR BOARDS)

**Pattern:** "State Lenz's Law. Explain how it is consistent with the law of conservation of energy." OR "Why does the induced current always oppose the change in flux?"

This question appeared in CBSE board exams in **2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023** — nearly every single year!

---

**Solved Example** 🟡 *(Model 2-mark Board Answer)*

> State Lenz's Law. Explain how it is consistent with the law of conservation of energy. (CBSE 2019, 2 marks)

<details><summary><b>Solution</b></summary>

**Statement of Lenz's Law:**
The direction of the induced current is such that it always **opposes the change in magnetic flux** that causes it.

**Consistency with Conservation of Energy:**

Consider a bar magnet being brought toward a coil:

- By Lenz's Law, the induced current in the coil creates a magnetic field that **repels** the approaching magnet.
- To overcome this repulsive force and bring the magnet closer, an **external agent must do work**.
- This mechanical work done against the opposing electromagnetic force is converted into **electrical energy** in the coil, which is further dissipated as **heat** in the resistance of the coil.

**If Lenz's Law were violated** (i.e., if the induced current *aided* the approach):
- The magnet would be attracted and accelerated toward the coil
- This would increase the current further, which would attract the magnet more strongly
- The system would generate an ever-increasing amount of electrical energy with no external input
- This would violate the **Law of Conservation of Energy** — energy cannot be created from nothing.

**Conclusion:** The opposing nature of the induced current ensures that energy is *transformed* (mechanical → electrical → heat), never created. Hence Lenz's Law is a direct consequence of conservation of energy.

</details>

---

**Practice Questions:**

1. 🟢 In one line, state: What is the physical significance of the negative sign in $\varepsilon = -N\dfrac{d\Phi}{dt}$?

<details><summary><b>Answer</b></summary>

The negative sign represents **Lenz's Law** — it indicates that the induced EMF (and hence the induced current) acts in a direction that **opposes the change** in magnetic flux responsible for its production.

</details>

2. 🟡 A student argues: "Lenz's Law is just a consequence of Newton's Third Law — action-reaction." Is this statement correct? Justify.

<details><summary><b>Answer</b></summary>

The statement is **partially correct but misleading**.

Lenz's Law is a consequence of the **Law of Conservation of Energy**, not Newton's Third Law directly.

However, there is a similarity in spirit: when a magnet approaches a coil, the coil's induced current creates a force that **opposes** the magnet's approach (just as action-reaction). But the reason is fundamentally energetic — the induced current must oppose the change to prevent a perpetual motion machine, which is a statement about energy, not forces.

Newton's Third Law is about equal and opposite forces between two bodies. Lenz's Law is about the direction of induced current being such that it opposes the *cause* — which is energy conservation.

</details>

3. 🟡 A magnet is released from rest and falls through a copper ring. It is observed that the magnet falls slower than in free fall. Where does the "lost" kinetic energy go?

<details><summary><b>Answer</b></summary>

The "lost" kinetic energy is converted to **electrical energy** in the copper ring through electromagnetic induction, which is then dissipated as **heat** (Joule heating, $Q = I^2Rt$) in the resistance of the ring.

By Lenz's Law, the induced current in the ring opposes the magnet's motion (both during approach and recession), creating a retarding force. The work done against this retarding force is transformed into heat.

**Energy conservation:** $\Delta KE_{lost} = Q_{heat} + \Delta PE_{remaining}$ — total energy is conserved.

</details>

4. 🟡 Why does a copper disc (or metallic disc) rotating between the poles of a magnet gradually come to rest? Explain using Lenz's Law. (CBSE 2018, 2 marks)

<details><summary><b>Answer</b></summary>

When a metallic disc rotates between the poles of a magnet, different parts of the disc pass through regions of varying magnetic flux (some parts entering, some leaving the field region).

By Faraday's Law, **eddy currents** are induced in the disc. By Lenz's Law, these eddy currents flow in directions that create forces **opposing the rotation** of the disc — this is Faraday's braking principle.

The kinetic energy of rotation is continuously converted into **heat** by these eddy currents (Joule heating). Since energy is continuously being dissipated and no energy is being supplied, the disc **gradually slows down and eventually stops**.

This is the principle of **electromagnetic damping**.

</details>

5. 🔴 A ring made of a superconductor (zero resistance) is placed in a changing magnetic field. Discuss: (a) Will there be an induced EMF? (b) Will current flow? (c) Will Lenz's Law be satisfied?

<details><summary><b>Answer</b></summary>

**(a)** Yes, an induced EMF will be produced (by Faraday's Law), as long as there is a changing flux.

**(b)** Yes, current will flow. In a superconductor ($R = 0$), even an infinitesimally small EMF can drive current. In fact, the induced current will be so large that it **perfectly maintains** the flux through the ring — the induced B exactly cancels any external change in B, keeping $\Phi = \text{constant}$.

**(c)** Yes, Lenz's Law is **perfectly satisfied** — the induced current completely opposes the change in flux (to the point of preventing any change at all). This is the **Meissner effect** concept — a superconductor expels magnetic fields entirely.

**Energy note:** Since $R = 0$, no heat is generated, but the current persists indefinitely to maintain the flux.

</details>

6. 🔴 **(Competency-based)** High-speed trains in Japan (Shinkansen) and France (TGV) use **electromagnetic braking** for emergency stops. Explain the physics principle involved and discuss why electromagnetic braking is preferred over mechanical friction brakes for high-speed applications.

<details><summary><b>Answer</b></summary>

**Physics Principle — Lenz's Law / Eddy Current Braking:**

When the train's braking system engages, strong electromagnets are activated near the conducting rails or metal brake discs. The relative motion between the magnet and conductor causes a change in magnetic flux.

By Faraday's Law: $\varepsilon = -\dfrac{d\Phi}{dt}$, this induces **eddy currents** in the conducting material.

By Lenz's Law: These eddy currents create magnetic fields that **oppose the relative motion** — i.e., they create a retarding force on the train, slowing it down.

The kinetic energy of the train is converted to **heat** in the conductor.

**Advantages over mechanical friction brakes:**

| Feature | Electromagnetic Braking | Mechanical Friction |
|---------|------------------------|---------------------|
| Contact | Non-contact (no wear) | Contact (wear occurs) |
| Maintenance | Very low | High (brake pads) |
| Heat distribution | Spread over conductor | Concentrated at pads |
| Reliability at high speed | Excellent | Risk of fade at high speeds |
| Response time | Very fast (milliseconds) | Slower mechanical response |

**Limitation:** Electromagnetic braking force decreases at very low speeds (force $\propto v$), so mechanical brakes are still needed for final stop.

</details>

---

### Type 4: Retarding Force Analysis ⭐

**Pattern:** "A conducting rod/loop moves through a magnetic field. Show that the force on it is retarding (opposing motion)."

---

**Solved Example** 🟡

> A conducting rod of length $l = 0.5$ m slides on two parallel rails separated by 0.5 m. The rails have negligible resistance. A resistor $R = 2\ \Omega$ connects the rails at one end. The rod moves with velocity $v = 4$ m/s in a uniform field $B = 1$ T perpendicular to the plane of the rails. Find: (a) induced EMF, (b) current, (c) retarding force on the rod, and (d) verify using power.

<details><summary><b>Solution</b></summary>

**Given:** $l = 0.5$ m, $R = 2\ \Omega$, $v = 4$ m/s, $B = 1$ T

**(a) Induced EMF:**
$$\varepsilon = Blv = 1 \times 0.5 \times 4 = \mathbf{2 \text{ V}}$$

**(b) Induced Current:**
$$I = \frac{\varepsilon}{R} = \frac{2}{2} = \mathbf{1 \text{ A}}$$

**(c) Retarding Force:**
$$F = BIl = 1 \times 1 \times 0.5 = \mathbf{0.5 \text{ N}}$$

Direction: By Lenz's Law, this force **opposes** the direction of motion of the rod.

**(d) Power verification:**
- Power delivered by external agent (pushing rod): $P_{in} = F \times v = 0.5 \times 4 = 2$ W
- Power dissipated in resistor: $P_{out} = I^2R = 1^2 \times 2 = 2$ W
- ✅ $P_{in} = P_{out}$ — Energy is conserved!

Also: $P = \varepsilon \times I = 2 \times 1 = 2$ W ✅

</details>

---

**Practice Questions:**

1. 🟢 A rod of length 50 cm moves at 2 m/s in a field $B = 0.4$ T. Resistance = 1 Ω. Find the retarding force.

<details><summary><b>Answer</b></summary>

$\varepsilon = Blv = 0.4 \times 0.5 \times 2 = 0.4$ V

$I = \varepsilon/R = 0.4/1 = 0.4$ A

$F = BIl = 0.4 \times 0.4 \times 0.5 = \mathbf{0.08 \text{ N}}$ (retarding)

</details>

2. 🟡 To keep the rod in Type 4 (Solved Example) moving at constant velocity, what external force must be applied and what is its direction?

<details><summary><b>Answer</b></summary>

For constant velocity, net force = 0 → external force must exactly balance the retarding force.

**External force = 0.5 N in the direction of motion.**

Without this external force, the rod would decelerate to rest (converting all kinetic energy to heat). The external agent does 2 W of work, all of which appears as heat in R.

</details>

3. 🟡 The velocity of the rod in the solved example is doubled to 8 m/s. By what factor does the retarding force increase?

<details><summary><b>Answer</b></summary>

$F = \dfrac{B^2l^2v}{R}$

Since $F \propto v$, doubling $v$ **doubles** the retarding force.

New F = $\dfrac{1^2 \times 0.5^2 \times 8}{2} = \dfrac{0.25 \times 8}{2} = 1$ N (was 0.5 N — doubled ✅)

New power = $F \times v = 1 \times 8 = 8$ W (was 2 W — quadrupled, since $P \propto v^2$).

</details>

4. 🔴 A square loop (side $a$, resistance $R$) falls under gravity through a uniform horizontal field $B$ (into the page). The field exists only in a horizontal strip of height $h$. Show that the terminal velocity (if reached inside the strip) is $v_T = \dfrac{mgR}{B^2a^2}$.

<details><summary><b>Answer</b></summary>

As the loop enters the strip and falls with velocity $v$:

Induced EMF: $\varepsilon = Bav$

Induced current: $I = \dfrac{Bav}{R}$

Upward retarding force (Lenz's Law): $F_{mag} = BIa = \dfrac{B^2a^2v}{R}$

Downward gravitational force: $F_g = mg$

At terminal velocity, net force = 0:

$$mg = \frac{B^2a^2v_T}{R}$$

$$\boxed{v_T = \frac{mgR}{B^2a^2}}$$

This terminal velocity is reached when the braking force exactly equals gravity — a beautiful application of Lenz's Law.

</details>

---

### Type 5: Unusual Scenarios — NCERT Exemplar Style ⭐

**Pattern:** "Will current be induced in [unusual configuration]?" — requires deeper conceptual thinking.

---

**Solved Example** 🟡

> A bar magnet falls through a long solenoid connected to a galvanometer. Describe the direction of induced current (a) when N-pole is entering the top, (b) when N-pole is exiting the bottom, and (c) predict the shape of the current vs. time graph.

<details><summary><b>Solution</b></summary>

**Convention:** "Clockwise" and "anticlockwise" as viewed from the top of the solenoid.

**(a) N-pole entering from top:**
- Flux through solenoid increases (downward through solenoid)
- Induced current opposes → creates B upward (inside solenoid)
- At top end: induced current is **anticlockwise** (as seen from top) → top becomes N-pole → repels magnet

**(b) N-pole exiting from bottom:**
- Flux through solenoid decreases (downward field leaving)
- Induced current maintains → creates B downward
- At bottom end: current at bottom end is **clockwise** as seen from top → or anticlockwise as seen from bottom → bottom becomes S-pole → tries to attract the N-pole and slow its exit

**Direction reverses** between entry and exit.

**(c) Current vs time graph:**

```
I
 |     ___
 |    /   \
 |   /     \
---+---+---+---+-- t
   |   (inside)   |
   |              |
   |  ___
   | /   \  (exits — opposite direction)
```

Current rises to a peak (entry), drops to zero (when magnet is fully inside, momentarily), reverses and peaks (exit), then drops to zero.

The peak during exit is **larger** than during entry (because magnet is faster due to acceleration under gravity, so $d\Phi/dt$ is larger).

</details>

---

**Practice Questions:**

1. 🟡 A cylindrical bar magnet rotates about its own geometrical axis (the cylinder axis). A circular coil is placed coaxially. Will current be induced?

<details><summary><b>Answer</b></summary>

**No.** A cylindrical bar magnet has axial symmetry — its field is symmetric about its own axis. Rotating about the cylinder axis does **not change** the magnetic flux through the coaxial coil. Since $\dfrac{d\Phi}{dt} = 0$, no EMF and no current are induced.

*(NCERT Exemplar Q6.3 concept)*

</details>

2. 🟡 Coil A has a fixed current flowing in it. Coil B is nearby. If coil A is moved toward coil B (while maintaining constant current in A), will current be induced in B?

<details><summary><b>Answer</b></summary>

**Yes.** As A moves closer to B, the magnetic flux through B due to A's magnetic field **increases**. By Faraday's Law, this changing flux induces an EMF in B, which drives a current.

By Lenz's Law, the induced current in B will create a field opposing the increase — i.e., opposing the approach of A. The current in B will flow in the **opposite direction** to the current in A.

Note: This is different from the case where A's current is changing — here, the current is constant but the *position* changes.

</details>

3. 🔴 A conducting loop is placed in a uniform magnetic field. The loop is now **squeezed** so that its area becomes zero (without moving from the field region). What happens? Describe both the initial and final states.

<details><summary><b>Answer</b></summary>

**During squeezing:**
- Area decreases → flux $\Phi = BA\cos\theta$ decreases → $\dfrac{d\Phi}{dt} \neq 0$
- By Faraday's Law: EMF is induced during the squeezing process
- By Lenz's Law: induced current flows to **maintain** the flux → current flows in a direction to create B in the same direction as external B

**Final state (area = 0):**
- Flux = 0 → no change in flux → no EMF → no current

**Conclusion:** Current flows only **during** the squeezing process, not before or after. The total charge that flows is:

$$q = \frac{\Delta\Phi}{R} = \frac{BA}{R}$$ (initial flux / resistance)

</details>

4. 🔴 A circular conducting ring falls through the gap between two bar magnets arranged as N|S (the gap between N-pole and S-pole of two separate magnets, with field going from N to S between them). Describe qualitatively the motion.

<details><summary><b>Answer</b></summary>

As the ring falls through the magnetic field in the gap:

- **Entering the field from above:** Flux through ring increases → Lenz's Law induces current opposing the increase → ring experiences an **upward retarding force** → falls slower than free fall.

- **At the center of the gap:** The ring is fully in the uniform field. If the field is perfectly uniform, flux may momentarily be at maximum with zero rate of change → momentarily no induced current → no braking.

- **Exiting the field from below:** Flux decreases → Lenz's Law induces current to maintain flux → ring again experiences an **upward retarding force**.

**Overall:** The ring is retarded both on entry and exit. If the ring has finite resistance, it loses kinetic energy (converted to heat) and falls slower than free fall throughout. It does NOT stop unless resistance is zero (superconducting ring).

</details>

---

### Type 6: Assertion-Reason and Conceptual Open-Circuit Problems ⭐

**Pattern:** Assertion-Reason format, or "A loop is in an open circuit. Flux changes. What is induced?"

---

**Solved Example** 🟡

> **Assertion (A):** Induced EMF is always produced whenever there is a change in magnetic flux.
> **Reason (R):** Induced current is always produced whenever there is a change in magnetic flux.
> 
> (a) Both A and R are true, and R is the correct explanation of A.
> (b) Both A and R are true, but R is not the correct explanation of A.
> (c) A is true but R is false.
> (d) A is false but R is true.

<details><summary><b>Solution</b></summary>

**Answer: (c) A is true but R is false.**

**Explanation:**

**Assertion A (True):** Faraday's Law states that changing magnetic flux always produces an induced EMF — this is true regardless of whether the circuit is open or closed.

$$\varepsilon = -\frac{d\Phi}{dt} \neq 0 \text{ when } \frac{d\Phi}{dt} \neq 0$$

**Reason R (False):** Induced *current* requires a **closed circuit**. In an open circuit, even though EMF is induced, no current flows because there is no complete path.

$$I = \frac{\varepsilon}{R} \to 0 \text{ if } R \to \infty \text{ (open circuit)}$$

**Conclusion:** EMF exists in an open circuit, but current does not. This is a very important distinction and a favourite CBSE trap!

</details>

---

**Practice Questions:**

1. 🟢 A coil is connected to a galvanometer. The coil is moved into a region of increasing magnetic field. What does the galvanometer read?

<details><summary><b>Answer</b></summary>

The galvanometer shows a **deflection** (reads a non-zero value), indicating current is flowing. Since it's a closed circuit, both EMF and current are induced, and the galvanometer detects the current.

</details>

2. 🟡 A coil is connected to a voltmeter (very high resistance, effectively open circuit). The coil experiences a changing flux. What does the voltmeter read?

<details><summary><b>Answer</b></summary>

The voltmeter reads the **induced EMF** ($\varepsilon = -d\Phi/dt$). Even though effectively no current flows, the EMF exists across the open terminals and the voltmeter (which measures voltage/EMF) will show a reading.

This demonstrates that EMF can exist without current.

</details>

3. 🟡 **(CBSE trap)** "Lenz's Law gives the direction of induced EMF." Is this statement correct?

<details><summary><b>Answer</b></summary>

**Partially correct, but more precisely stated as:** Lenz's Law gives the direction of the **induced current** (in a closed circuit).

Since the direction of current is determined by the direction of EMF (current flows from lower to higher potential inside the source), knowing the current direction implies knowing the EMF direction. So Lenz's Law does indirectly give the direction of EMF, but it is more fundamentally about the **current** direction.

In an **open circuit**, Lenz's Law about current direction does not apply, but the EMF direction (polarity of the open terminals) still follows the same principle.

</details>

4. 🔴 Two conducting rings are placed coaxially, one above the other. The upper ring carries an increasing current flowing anticlockwise (as seen from above). What is the direction of induced current in the lower ring? What is the nature of the force between them (attractive or repulsive)?

<details><summary><b>Answer</b></summary>

**Direction of induced current in lower ring:**

Upper ring has anticlockwise current (as seen from above) → creates B-field pointing **upward** along the axis (by RHR).

As current in upper ring increases, upward flux through lower ring **increases**.

By Lenz's Law, induced current in lower ring must oppose the increase → create B pointing **downward** inside lower ring → current in lower ring flows **clockwise** as seen from above.

**Nature of Force:**

- Upper ring: anticlockwise (from above) → North pole below
- Lower ring: clockwise (from above) → South pole above (same pole as upper ring's south? No — let's recheck)

Upper ring anticlockwise from above → by right-hand rule: field points up → upper face is N-pole (outward), lower face is S-pole.

Lower ring clockwise from above → field points down → upper face is S-pole (inward for lower ring face seen from above... actually: clockwise from above → thumb points downward → upper face of lower ring acts as S-pole.

Upper ring's lower face: S-pole. Lower ring's upper face: S-pole. **S-S → Repulsive!**

Wait, let me recheck more carefully:
- Upper ring, anti-CW from top → right-hand thumb upward → upper face N, lower face S.
- Lower ring, CW from top → right-hand thumb downward → upper face S, lower face N.

Upper ring's lower face = S. Lower ring's upper face = S. **Same poles facing each other → REPULSIVE force.**

The rings repel each other. (This makes physical sense — the lower ring's induced current opposes the cause, i.e., it tries to reduce the flux increase, and repulsion achieves this by pushing the rings apart, reducing flux.)

</details>

---

## 🧱 Stage 4: MCQ Mastery

**Instructions:** Options (a) through (d). Select the best answer. Solutions in details below.

---

**Q1.** The negative sign in Faraday's law $\varepsilon = -N\dfrac{d\Phi}{dt}$ signifies:

(a) The induced EMF is always in the negative direction  
(b) The magnitude of induced EMF is always negative  
(c) The induced EMF opposes the change in flux (Lenz's Law)  
(d) The energy is always lost in the process

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The negative sign is the mathematical representation of **Lenz's Law** — the induced EMF (and hence current) always opposes the change in magnetic flux. It does not mean EMF is always negative (the sign is relative to the chosen positive direction). Options (a), (b) are incorrect (EMF can be "positive" or "negative" depending on convention); option (d) is not what the sign represents.

</details>

---

**Q2.** A bar magnet is moved toward a coil with its North pole facing the coil. The induced current in the coil, as seen from the magnet's side:

(a) Flows clockwise — the coil acts as S-pole  
(b) Flows anticlockwise — the coil acts as N-pole  
(c) Flows clockwise — the coil acts as N-pole  
(d) Flows anticlockwise — the coil acts as S-pole

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

As N-pole approaches, flux increases. Induced current opposes → coil face near the magnet becomes **N-pole** (repulsion). A N-pole (as seen from outside, i.e., from magnet's side) corresponds to **anticlockwise** current by RHR. Option (b) is correct.

</details>

---

**Q3.** A rectangular loop moves with constant velocity into a region of uniform magnetic field. Which graph best represents the induced EMF vs. time?

(a) EMF increases linearly with time  
(b) EMF remains constant throughout entry  
(c) EMF increases then decreases  
(d) EMF is zero throughout

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

As long as only one side of the loop is cutting field lines (i.e., during entry, only the leading edge is in the field), the rate of change of flux is constant ($\Phi = B \cdot l \cdot vt$ → $d\Phi/dt = Blv$ = constant). So **EMF is constant** during entry. It becomes zero once the loop is fully inside. Option (b) is correct.

</details>

---

**Q4.** Which of the following is NOT a consequence of Lenz's Law?

(a) A magnet falls more slowly through a copper tube than through a plastic tube  
(b) An aluminum disc rotates between poles of a magnet and slows down  
(c) A transformer steps up voltage  
(d) A metal ring is repelled when a current-carrying coil is brought near it

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

(a) Copper tube eddy currents retard the magnet — Lenz's Law ✅  
(b) Aluminum disc eddy current braking — Lenz's Law ✅  
(c) Transformer voltage step-up is based on Faraday's Law (mutual induction with turns ratio) — not specifically a Lenz's Law consequence. ❌  
(d) Repulsion of the ring due to opposing induced current — Lenz's Law ✅

</details>

---

**Q5.** **(Assertion-Reason)** 

**Assertion (A):** Lenz's Law is a consequence of the law of conservation of energy.

**Reason (R):** The direction of the induced current is such that it opposes the change in magnetic flux that produced it.

(a) Both A and R are true, and R is the correct explanation of A  
(b) Both A and R are true, but R is NOT the correct explanation of A  
(c) A is true but R is false  
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

**A is True:** Lenz's Law is indeed a consequence of energy conservation (if current aided the change, perpetual motion would result).

**R is True:** This is the statement of Lenz's Law.

**R correctly explains A:** The fact that induced current opposes the change (R) is *precisely the mechanism* by which energy conservation (A) is upheld. Without this opposition, energy would be created from nothing.

**Answer: (a)** ✅

</details>

---

**Q6.** **(Assertion-Reason)**

**Assertion (A):** When a magnet is pushed into a coil, the induced current creates a repulsive force on the magnet.

**Reason (R):** This repulsive force is in accordance with Newton's Third Law of Motion.

(a) Both A and R are true, and R is the correct explanation of A  
(b) Both A and R are true, but R is NOT the correct explanation of A  
(c) A is true but R is false  
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

**A is True:** By Lenz's Law, the coil's induced current creates a N-pole on the near side (when N-pole approaches) → repels the magnet. ✅

**R is True:** Newton's Third Law does apply — the magnet exerts a force on the coil, and the coil exerts an equal and opposite force on the magnet. ✅

**But R does NOT correctly explain A:** The repulsive force is explained by **Lenz's Law (conservation of energy)**, not by Newton's Third Law. Newton's Third Law tells us forces come in equal-opposite pairs, but it doesn't explain *why* the force is repulsive rather than attractive. Lenz's Law (energy conservation) does.

**Answer: (b)** ✅

</details>

---

**Q7.** **(Assertion-Reason)**

**Assertion (A):** Lenz's Law violates the conservation of energy.

**Reason (R):** The induced EMF always opposes the change in magnetic flux responsible for its production.

(a) Both A and R are true, and R is the correct explanation of A  
(b) Both A and R are true, but R is NOT the correct explanation of A  
(c) A is true but R is false  
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

**A is False:** Lenz's Law UPHOLDS (not violates) the conservation of energy. This is a common trick question! ❌

**R is True:** This is the correct statement of Lenz's Law. ✅

**Answer: (d) A is false but R is true.**

> ⚠️ **Exam Trap:** Read Assertion carefully — it says "violates" instead of "follows." Don't auto-select (a) just because the topic is familiar!

</details>

---

**Q8.** A flux vs. time graph for a coil is shown below. At which time interval is the **magnitude** of induced EMF the greatest?

| Time interval | Flux behavior |
|--------------|---------------|
| 0–2 s | Flux increases from 0 to 4 Wb (linearly) |
| 2–4 s | Flux constant at 4 Wb |
| 4–6 s | Flux decreases from 4 Wb to 0 Wb (linearly) |
| 6–8 s | Flux = 0 |

(a) 0–2 s  
(b) 2–4 s  
(c) 4–6 s  
(d) Both (a) and (c) equally

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

The induced EMF is $|\varepsilon| = \left|\dfrac{d\Phi}{dt}\right|$.

- 0–2 s: $|d\Phi/dt| = 4/2 = 2$ V/s
- 2–4 s: $|d\Phi/dt| = 0$ (constant flux) → $\varepsilon = 0$
- 4–6 s: $|d\Phi/dt| = 4/2 = 2$ V/s
- 6–8 s: $|d\Phi/dt| = 0$ → $\varepsilon = 0$

The magnitude is **equal in 0–2 s and 4–6 s** (both = 2 V). During 2–4 s and 6–8 s, $\varepsilon = 0$.

**Answer: (d)** ✅

The direction of induced current **reverses** between 0–2 s (opposing increase) and 4–6 s (opposing decrease).

</details>

---

**Q9.** A conducting ring is held stationary in a non-uniform, time-varying magnetic field. Which of the following statements is correct?

(a) No EMF is induced since the ring is stationary  
(b) EMF is induced only if the ring is closed  
(c) EMF is induced regardless of whether the ring is open or closed  
(d) Current is induced even if the ring is open

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

EMF is induced whenever magnetic flux changes — regardless of whether the circuit is open or closed. This is Faraday's Law: $\varepsilon = -d\Phi/dt$. The ring being stationary doesn't matter — the field is time-varying.

Option (a): Wrong — stationary ring in time-varying B still has changing flux.  
Option (b): Wrong — EMF is induced in open rings too.  
Option (d): Wrong — open ring has no closed path for current, so $I = 0$.

**Answer: (c)** ✅

</details>

---

**Q10.** Two identical circular loops A and B are coaxial, with B below A. Current in A is suddenly decreased. The induced current in B and the force between them are:

(a) Same direction as A; attractive  
(b) Opposite to A; repulsive  
(c) Same direction as A; repulsive  
(d) Opposite to A; attractive

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

When current in A decreases, flux through B decreases. By Lenz's Law, induced current in B tries to maintain the flux → current in B flows in the **same direction** as in A.

Now both carry currents in the same direction → like parallel wires with same-direction current → **attractive force**.

**Answer: (a)** ✅

</details>

---

**Q11.** A long straight wire carries a steady current $I$. A rectangular loop is placed in the same plane. If the loop is moved away from the wire:

(a) Induced current in loop is in the same direction as $I$ in the near side  
(b) Induced current in loop is opposite to $I$ in the near side  
(c) No current is induced  
(d) Induced current is clockwise in the loop

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

As the loop moves away from the wire, the flux (from the wire's field) through the loop **decreases**. By Lenz's Law, induced current in the loop creates flux in the same direction as the wire's field → by RHR, the current in the near side of the loop (side closer to wire) flows in the **same direction** as $I$.

**Answer: (a)** ✅

</details>

---

**Q12.** **(Statement I / Statement II type)**

**Statement I:** In electromagnetic induction, the work done by the external agent equals the electrical energy generated plus any energy stored in the magnetic field.

**Statement II:** For a resistive circuit with no inductance, all work done by the external agent is dissipated as heat.

(a) Statement I is correct, Statement II is correct  
(b) Statement I is correct, Statement II is incorrect  
(c) Statement I is incorrect, Statement II is correct  
(d) Both statements are incorrect

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

**Statement I:** Correct — in general, work done = electrical energy generated + energy stored in magnetic field of the induced current (relevant for inductive circuits).

**Statement II:** Correct — in a purely resistive circuit (no inductance), there is no energy stored in magnetic fields, so all electrical energy is dissipated as Joule heat: $P = I^2R$.

**Answer: (a)** ✅

</details>

---

## 🔀 Stage 5: Type Mixer

### Mixed Problem 1: Direction + Energy (Types 1 + 3) 🟡

> A student holds the N-pole of a bar magnet and pushes it toward a circular coil (10 turns, area = 20 cm², resistance = 5 Ω). The flux changes at 0.05 Wb/s. 
> (a) Find the induced EMF and current.
> (b) Find the direction of induced current as seen from the magnet side.
> (c) What force does the coil exert on the magnet?
> (d) Where does the energy come from to generate the induced current?

<details><summary><b>Solution</b></summary>

**(a) Induced EMF and Current:**

$$|\varepsilon| = N \cdot \frac{d\Phi}{dt} = 10 \times 0.05 = \mathbf{0.5 \text{ V}}$$

$$I = \frac{\varepsilon}{R} = \frac{0.5}{5} = \mathbf{0.1 \text{ A}}$$

**(b) Direction of Induced Current:**

N-pole approaches → flux through coil increases → induced B must oppose (point away from N-pole) → coil face nearest to magnet becomes N-pole → current flows **anticlockwise** as seen from the magnet side.

**(c) Force on Magnet:**

The coil's near face becomes N-pole (same as the approaching magnet's N-pole) → the coil **repels** the magnet with a force directed away from the coil.

The magnet must overcome this repulsion (the student must push against it), doing work.

**(d) Source of Energy:**

The energy comes from the **mechanical work done by the student** pushing the magnet against the repulsive electromagnetic force. This work is converted to electrical energy in the coil ($P = \varepsilon I = 0.5 \times 0.1 = 0.05$ W) and dissipated as **heat** in the coil's resistance.

No energy is created — it is transformed: mechanical → electrical → thermal. ✅ (Energy conservation)

</details>

---

### Mixed Problem 2: Loop Movement + Retarding Force (Types 2 + 4) 🟡

> A rectangular loop (20 cm × 10 cm, resistance 2 Ω) moves with velocity 3 m/s to the right, entering a uniform magnetic field $B = 0.5$ T directed into the page.
> (a) Calculate the induced EMF.
> (b) Find the induced current and its direction (loop has sides AB top, BC right, CD bottom, DA left).
> (c) Find the retarding force on the loop.
> (d) What power is delivered by the external agent to maintain constant velocity?

<details><summary><b>Solution</b></summary>

**Given:** $l = 20$ cm = 0.2 m (length of side entering field), $v = 3$ m/s, $B = 0.5$ T, $R = 2\ \Omega$

**(a) Induced EMF:**

$$\varepsilon = Blv = 0.5 \times 0.2 \times 3 = \mathbf{0.3 \text{ V}}$$

**(b) Induced Current:**

$$I = \frac{\varepsilon}{R} = \frac{0.3}{2} = \mathbf{0.15 \text{ A}}$$

**Direction:** B is into the page, flux increases as loop enters → induced B must point out of page → current is **anticlockwise**: A → D → C → B → A.

In the leading edge AB (which is inside the field): current flows from **B → A** (i.e., rightward at top, or: anticlockwise means current in top goes from right to left: B→A).

**(c) Retarding Force:**

The retarding force acts on the current-carrying side AB inside the field:

$$F = BIl = 0.5 \times 0.15 \times 0.2 = \mathbf{0.015 \text{ N}}$$

Direction: **opposing the motion** (i.e., pointing to the left, by Lenz's Law). Only the leading edge experiences a net force (the trailing edge is outside the field).

**(d) Power by External Agent:**

$$P = F \times v = 0.015 \times 3 = 0.045 \text{ W}$$

Check: $P = I^2R = (0.15)^2 \times 2 = 0.0225 \times 2 = 0.045$ W ✅

</details>

---

### Mixed Problem 3: Competency-Based Case Study — Electromagnetic Braking in Railways 🔴

> **Case Study:** Modern Indian Railways has introduced Linke Hofmann Busch (LHB) coaches with **electromagnetic/regenerative braking** systems. When the train decelerates, its motors act as generators, converting kinetic energy back into electrical energy that is fed to the grid or stored in batteries.
>
> A simplified model: A conducting disc (radius $r = 0.3$ m) rotates in a uniform B-field at angular velocity $\omega$ when the braking system is activated. The field is perpendicular to the disc, $B = 2$ T. The effective resistance of the disc's eddy current paths is $R = 0.5\ \Omega$.

> **(a)** Explain how Lenz's Law causes the disc to decelerate.

> **(b)** If the induced EMF is approximately $\varepsilon = \dfrac{1}{2}B\omega r^2 = 90$ mV, find the induced current.

> **(c)** Calculate the braking power (rate of energy dissipation).

> **(d)** If the disc (moment of inertia $J = 0.1$ kg·m²) was rotating at $\omega_0 = 100$ rad/s and the braking torque is $\tau = 0.054$ N·m, estimate the time to stop.

> **(e)** Why is electromagnetic braking preferred over friction braking in high-speed trains?

<details><summary><b>Solution</b></summary>

**(a) Lenz's Law Explanation:**

As the disc rotates in the B-field, different regions of the disc have continuously changing flux linkage. By Faraday's Law, EMF is induced in closed loops within the disc. By Lenz's Law, the resulting **eddy currents** flow in directions that create magnetic forces **opposing the rotation** of the disc. This opposing torque decelerates the disc — converting rotational kinetic energy into heat (or, in regenerative braking, into electrical energy fed to the supply).

**(b) Induced Current:**

$$I = \frac{\varepsilon}{R} = \frac{90 \times 10^{-3}}{0.5} = \mathbf{0.18 \text{ A}}$$

**(c) Braking Power:**

$$P = \frac{\varepsilon^2}{R} = \frac{(90\times10^{-3})^2}{0.5} = \frac{8.1\times10^{-3}}{0.5} = \mathbf{16.2 \text{ mW}}$$

Or: $P = I^2R = (0.18)^2 \times 0.5 = 0.0324 \times 0.5 = 16.2$ mW ✅

**(d) Time to Stop:**

Using angular deceleration:

$$\alpha = -\frac{\tau}{J} = -\frac{0.054}{0.1} = -0.54 \text{ rad/s}^2$$

Time to stop from $\omega_0 = 100$ rad/s:

$$t = \frac{\omega_0}{|\alpha|} = \frac{100}{0.54} \approx \mathbf{185 \text{ s}}$$

*(Note: In real systems, the torque is not constant as it depends on $\omega$, making this an approximation.)*

**(e) Advantages of Electromagnetic Braking:**

- **No mechanical contact** → No wear of brake pads → Lower maintenance costs
- **Smooth deceleration** → Better passenger comfort
- **Energy recovery** (regenerative) → More efficient use of energy
- **Faster response** → Electromagnetic forces act almost instantaneously
- **No brake fade** → Friction brakes overheat at high speeds; electromagnetic braking doesn't suffer from this

**Limitation:** Braking force decreases as speed decreases ($F \propto v$), so a final mechanical brake is still needed for complete stop.

</details>

---

### Mixed Problem 4: Two-Ring Interaction (Types 5 + 6) 🔴

> Ring A (carrying current flowing anticlockwise as seen from above) is held fixed above ring B (which is a free conductor with resistance R). The current in A is suddenly switched off.
> (a) What happens in ring B?
> (b) What is the nature of force between the rings at the instant of switch-off?
> (c) How does this relate to Lenz's Law and energy conservation?

<details><summary><b>Solution</b></summary>

**(a) Effect in Ring B:**

When current in A is switched off, the magnetic flux through B (which was downward, since A had anticlockwise current creating upward B... wait — anticlockwise from above → right-hand rule → thumb points up → B-field points upward).

So flux through B (below A) was **upward** (same direction as A's field).

When A's current is switched off, this upward flux through B **decreases**.

By Lenz's Law: induced current in B must oppose the decrease → create B pointing **upward** inside B → current in B flows **anticlockwise** (as seen from above, same as A was).

**Answer:** Induced current in B flows in the **same direction** as A's current was.

**(b) Nature of Force:**

- A has zero current (switched off) but B now carries current (anticlockwise from above).
- At the instant of switch-off, A is in the process of losing current (still some current flowing) and B is developing current.
- A's current (decreasing, anticlockwise from above) and B's induced current (anticlockwise from above) are in the same direction.
- Two coaxial rings with same-direction currents attract each other.

**Force is ATTRACTIVE** at the moment of switch-off.

**(c) Lenz's Law + Energy Conservation:**

The induced current in B creates a field that tries to maintain the original flux — this is Lenz's Law. The attractive force tries to pull A and B together, which would maintain the flux (bringing them closer would increase coupling). The energy comes from the **magnetic energy stored in A's field** during the switch-off transient, which is transferred to heat in B's resistance.

This is consistent with energy conservation — the electrical energy stored in A's inductance is dissipated in B.

</details>

---

## 📋 Stage 6: Board Arsenal

### Q1. ⭐ State Lenz's Law and prove that it is consistent with the law of conservation of energy. (CBSE 2015, 2017, 2019 — 2 marks)

<details><summary><b>Model Answer</b></summary>

**Statement of Lenz's Law:** (1 mark)

The direction of the induced current is always such that it **opposes the change in magnetic flux** that caused it.

**Consistency with Conservation of Energy:** (1 mark)

Consider a magnet moving toward a coil:

By Lenz's Law, the induced current creates a magnetic field that **repels** the approaching magnet. The external agent (the person moving the magnet) must do **work against this repulsive force**.

This mechanical work is converted into **electrical energy** in the coil, which is then dissipated as **heat** in the resistance.

If the induced current *aided* the approach instead of opposing it, the magnet would accelerate toward the coil, inducing more current, which would attract the magnet more — generating infinite energy from nothing — **violating conservation of energy**.

Hence, Lenz's Law is a **direct consequence** of the law of conservation of energy. ✅

</details>

---

### Q2. ⭐ A rectangular loop ABCD is placed in a magnetic field directed into the page (A: top-left, B: top-right, C: bottom-right, D: bottom-left). The loop is pulled to the right, out of the field. Using Lenz's law, determine the direction of induced current. (CBSE 2017, 2019 — 2 marks)

<details><summary><b>Model Answer</b></summary>

**Step 1:** The external magnetic field is directed **into the page**. The loop is being pulled to the right, so the area of loop inside the field is **decreasing**.

**Step 2:** Since B is into the page and area inside field is decreasing, flux (into the page) is **decreasing**.

**Step 3 (Lenz's Law):** To oppose the decrease, the induced magnetic field must be directed **into the page** inside the loop.

**Step 4 (Right-Hand Rule):** For induced B into the page, curling right-hand fingers gives current flowing **clockwise**: A → B → C → D → A.

**Answer:** Induced current flows in the direction **A → B → C → D → A** (clockwise as seen from the front). ✅ (1 mark for method, 1 mark for correct direction)

</details>

---

### Q3. A bar magnet is moved toward a coil. The galvanometer connected to the coil shows a deflection. State the direction of induced current if the N-pole is on the left and the coil is on the right, as viewed from the left. (CBSE 2016 — 1 mark)

<details><summary><b>Model Answer</b></summary>

As the N-pole approaches from the left, flux through the coil (pointing rightward, from N to S outside the magnet) **increases**.

By Lenz's Law, induced current must oppose this → coil's left face becomes a N-pole (repelling the incoming N-pole).

A N-pole on the left face of the coil means (by RHR) current flows **anticlockwise** as seen from the left. ✅

*(1 mark: correct direction with brief justification)*

</details>

---

### Q4. A metallic disc is rotated between the poles of a magnet. It is observed that the disc gradually slows down and eventually stops. Explain this observation using Lenz's Law. (CBSE 2018 — 2 marks)

<details><summary><b>Model Answer</b></summary>

**Observation:** When the metallic disc rotates in the magnetic field, different parts of the disc move through regions of varying magnetic flux.

**Explanation using Lenz's Law:** (1 mark)

By Faraday's Law, the changing flux through various conducting paths in the disc induces **eddy currents** (circulating currents within the body of the disc).

By Lenz's Law, these eddy currents flow in directions such that they create forces that **oppose the rotation** of the disc — i.e., a retarding torque is set up.

**Energy consideration:** (1 mark)

The kinetic energy of the rotating disc is continuously converted into **heat** by the eddy currents (through Joule heating, $Q = I^2Rt$). Since energy is being dissipated and no energy is being supplied, the disc's rotation progressively slows and it eventually **stops**.

This is the principle of **electromagnetic damping**, a direct application of Lenz's Law.

</details>

---

### Q5. ⭐ (3-mark comprehensive) (a) State Lenz's Law. (b) A coil of 200 turns and cross-sectional area 0.04 m² is placed in a magnetic field that changes from 0.1 T to 0.5 T in 0.4 s. Find the induced EMF. (c) Using Lenz's Law, state in which direction the induced current will flow if the magnetic field is directed into the page and is increasing. (CBSE 2021 style — 3 marks)

<details><summary><b>Model Answer</b></summary>

**(a) Lenz's Law:** (1 mark)

The direction of induced current in a circuit is always such that it **opposes the change in magnetic flux** that caused its induction.

**(b) Induced EMF:** (1 mark)

$$|\varepsilon| = N \cdot A \cdot \frac{\Delta B}{\Delta t} = 200 \times 0.04 \times \frac{0.5 - 0.1}{0.4}$$

$$= 200 \times 0.04 \times 1 = \mathbf{8 \text{ V}}$$

**(c) Direction of Induced Current:** (1 mark)

B is into the page and **increasing** → flux into page increases.

By Lenz's Law: induced B must oppose the increase → induced B points **out of the page** inside the loop.

By Right-Hand Rule: for B out of page inside loop, current flows **anticlockwise** (counterclockwise as viewed from the front). ✅

</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Format:** Single correct MCQ (or integer type). Solutions in details.

---

**JEE Q1.** A conducting square loop of side $L$ and resistance $R$ is kept in a magnetic field $B$ acting perpendicular to the plane of the loop. If the side of the loop is decreasing at a constant rate $\dfrac{dL}{dt} = -k$ (i.e., the loop is shrinking), the induced current is:

(a) $\dfrac{2BLk}{R}$ &emsp; (b) $\dfrac{BLk}{R}$ &emsp; (c) $\dfrac{BL^2k}{R}$ &emsp; (d) $\dfrac{Bk}{R}$

<details><summary><b>Answer</b></summary>

**Answer: (a)**

Flux: $\Phi = BL^2$

$$\varepsilon = -\frac{d\Phi}{dt} = -B \cdot 2L \cdot \frac{dL}{dt} = -B \cdot 2L \cdot (-k) = 2BLk$$

$$I = \frac{|\varepsilon|}{R} = \frac{2BLk}{R}$$

**Answer: (a)** ✅

**Direction:** Since the loop is shrinking (area decreasing), flux decreases. By Lenz's Law, induced current flows to maintain flux — anticlockwise if B is out of the page.

</details>

---

**JEE Q2.** A metal ring is held horizontally and a bar magnet is dropped through it with its N-pole going first. The velocity of the magnet as a function of time (starting from above the ring) is best described by:

(a) Constantly increasing (free fall)  
(b) Increases, then decreases, then increases again &emsp;  
(c) Increases, then remains constant (terminal velocity) &emsp;  
(d) Increases with smaller acceleration than free fall, momentarily decreases near the ring, then increases again

<details><summary><b>Answer</b></summary>

**Answer: (d)**

**Analysis:**

- **Before reaching the ring:** As N-pole approaches, induced current in ring creates repulsive force (opposing approach). Magnet still accelerates due to gravity but with **less than free fall acceleration** (net downward force = $mg - F_{mag}$).

- **As magnet passes through the ring:** When the center of the magnet is at the ring, flux is momentarily at maximum → rate of change of flux is momentarily zero → no braking force → brief period of free fall.

- **Just after passing through:** Now N-pole is below the ring and moving away → ring's S-pole forms (attraction) → again retarding force, so magnet decelerates slightly.

- **Far below the ring:** Flux change negligible → effectively free fall again.

**Overall:** The magnet falls with **less than free fall acceleration** throughout (when near the ring), not at constant velocity (that would require zero resistance ring). Option (d) best describes this.

*Note: Option (b) is tempting but "decreases" means velocity actually goes down — that would require the retarding force to exceed gravity. For a ring with finite resistance and typical magnets, this doesn't happen; the magnet just accelerates slower.*

**Answer: (d)** ✅

</details>

---

**JEE Q3.** A rectangular coil (area $A$, resistance $R$, $N$ turns) rotates with angular velocity $\omega$ in a uniform field $B$. At $t = 0$, the coil is perpendicular to the field (maximum flux). The force required to maintain constant angular velocity is maximum at:

(a) $t = 0$ &emsp; (b) $t = \dfrac{\pi}{2\omega}$ &emsp; (c) $t = \dfrac{\pi}{\omega}$ &emsp; (d) $t = \dfrac{3\pi}{2\omega}$

<details><summary><b>Answer</b></summary>

**Answer: (b)**

**Analysis:**

Flux: $\Phi = NBA\cos(\omega t)$ (maximum at $t = 0$ when coil ⊥ B)

Induced EMF: $\varepsilon = NBA\omega\sin(\omega t)$

Induced current: $I = \dfrac{NBA\omega\sin(\omega t)}{R}$

The opposing torque on the coil:

$$\tau_{opposing} = NIAB\sin(\omega t) = \frac{N^2A^2B^2\omega}{R}\sin^2(\omega t)$$

This is maximum when $\sin^2(\omega t) = 1$, i.e., $\sin(\omega t) = 1$, i.e., $\omega t = \pi/2$, i.e., **$t = \dfrac{\pi}{2\omega}$**.

At this time, the coil plane is parallel to B (coil in the plane of B), flux is zero but rate of change of flux (hence EMF) is maximum.

**Answer: (b)** ✅

</details>

---

**JEE Q4.** Two coaxial circular loops A and B (same radius) are separated by a distance $d$. Loop A has $n$ turns and carries current $I$. Loop B has $m$ turns and resistance $R$. If the current in A decreases at rate $\left|\dfrac{dI}{dt}\right| = k$, the mutual inductance being $M$, then the power dissipated in B is:

(a) $\dfrac{M^2k^2}{R}$ &emsp; (b) $\dfrac{(Mk)^2}{R}$ &emsp; (c) $\dfrac{M^2k^2}{R^2}$ &emsp; (d) $\dfrac{Mk}{R}$

<details><summary><b>Answer</b></summary>

**Answer: (a) [same as (b)]**

**Analysis:**

The induced EMF in B due to changing current in A:

$$\varepsilon_B = M\left|\frac{dI}{dt}\right| = Mk$$

Induced current in B:

$$I_B = \frac{\varepsilon_B}{R} = \frac{Mk}{R}$$

Power dissipated in B:

$$P = I_B^2 R = \left(\frac{Mk}{R}\right)^2 \times R = \frac{M^2k^2}{R}$$

**Answer: (a)** ✅

Note: Options (a) and (b) are identical ($M^2k^2/R$ = $(Mk)^2/R$) — this is intentional in the problem to illustrate the form.

</details>

---

**JEE Q5.** A conducting rod of mass $m$ and length $L$ is free to slide (without friction) on two long parallel horizontal rails separated by $L$. A uniform vertical magnetic field $B$ exists in the region. The rod is given an initial velocity $v_0$ and allowed to move freely. The rails have negligible resistance and are connected by a resistor $R$ at one end. The velocity of the rod varies with time as:

(a) $v = v_0 e^{-t/\tau}$ where $\tau = \dfrac{mR}{B^2L^2}$ &emsp;  
(b) $v = v_0 \left(1 - e^{-t/\tau}\right)$ &emsp;  
(c) $v = v_0 - \dfrac{B^2L^2}{mR}t$ &emsp;  
(d) $v = \dfrac{v_0}{1 + t/\tau}$

<details><summary><b>Answer</b></summary>

**Answer: (a)**

**Derivation:**

At any instant, velocity = $v$:

Induced EMF: $\varepsilon = BLv$

Induced current: $I = BLv/R$

Retarding force: $F = BIL = B^2L^2v/R$

Newton's second law:

$$m\frac{dv}{dt} = -\frac{B^2L^2}{R}v$$

This gives: $\dfrac{dv}{v} = -\dfrac{B^2L^2}{mR}dt$

Integrating: $\ln\left(\dfrac{v}{v_0}\right) = -\dfrac{B^2L^2}{mR}t$

$$\boxed{v = v_0 e^{-B^2L^2t/mR} = v_0 e^{-t/\tau}}$$

where $\tau = \dfrac{mR}{B^2L^2}$ is the time constant.

**Answer: (a)** ✅

This exponential decay is a beautiful result — the rod never completely stops (it asymptotically approaches zero), but practically stops for $t \gg \tau$.

</details>

---

## 📝 Quick Revision Table — Lenz's Law Summary

| Situation | Flux Change | Induced B | Current Direction | Physical Effect |
|-----------|-------------|-----------|-------------------|-----------------|
| N-pole approaching | Increases | Opposes (away from N) | Anticlockwise from magnet side | Coil repels magnet |
| N-pole receding | Decreases | Supports (toward N) | Clockwise from magnet side | Coil attracts magnet |
| S-pole approaching | Increases | Opposes (away from S) | Clockwise from magnet side | Coil repels magnet |
| Loop enters field (B into page) | Increases | Out of page | Anticlockwise | Opposing force on loop |
| Loop exits field (B into page) | Decreases | Into page | Clockwise | Opposing force on loop |
| Current in nearby coil increases | Increases | Opposes external | Opposite to source current | Repulsive force |
| Current in nearby coil decreases | Decreases | Supports external | Same as source current | Attractive force |
| Loop area shrinking in B | Decreases | Same as B | To maintain flux | — |
| Loop area growing in B | Increases | Opposite to B | To reduce flux | — |

---

## 🎯 Key Formulas at a Glance

$$\varepsilon = -N\frac{d\Phi_B}{dt} \quad \text{(Faraday + Lenz)}$$

$$\varepsilon_{motional} = Blv \quad \text{(rod/edge moving in B)}$$

$$I = \frac{\varepsilon}{R} = \frac{Blv}{R}$$

$$F_{retarding} = BIl = \frac{B^2l^2v}{R} \quad \text{(opposing motion)}$$

$$P_{mechanical} = Fv = \frac{B^2l^2v^2}{R} = I^2R = P_{electrical} \quad \text{(energy conservation)}$$

$$v(t) = v_0 e^{-t/\tau}, \quad \tau = \frac{mR}{B^2l^2} \quad \text{(freely sliding rod)}$$

---

## ⚠️ Common Mistakes & Traps — Lenz's Law Edition

| Mistake | Correct Understanding |
|---------|----------------------|
| "Lenz's Law opposes flux" | It opposes **change** in flux, not flux itself |
| "Open circuit → no EMF" | Open circuit → EMF exists, NO current |
| "S-pole approaching → coil becomes N" | Wrong! Coil becomes S on the approaching-S side (repulsion always) |
| "Rotating magnet about own axis → current" | No current! Cylindrical magnet rotation doesn't change flux |
| "Lenz's Law is Newton's 3rd Law" | It's a consequence of ENERGY CONSERVATION, not Newton's 3rd |
| "Magnet falls through ring and stops" | Ring with finite R only retards the fall; never stops it completely |
| "Lenz's Law gives magnitude of EMF" | It gives DIRECTION only; magnitude comes from Faraday's Law |
| "Induced current same direction as source current always" | Only when source current decreases; opposite when source increases |

---

*← [Chapter 2 — Faraday's Law](./02_faradays_law.md)*

*→ [Chapter 4 — Motional EMF](./04_motional_emf.md)*
