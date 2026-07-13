# Chapter 6: Eddy Currents — The Hidden Whirlpools Inside Metal

> *NCERT Section 6.7*

*← [Chapter 5 — Energy Consideration](./05_energy_consideration.md)*

---

## 🎯 Stage 1: The Core Idea

### The Stone in the Pond Analogy

Imagine tossing a stone into a still pond. The moment it hits the water, concentric rings of ripples spread outward — but if you look closely at one spot, you'll see tiny *whirlpools* of water swirling in circles. They are not going anywhere useful; they are just circular, churning motion inside the water itself.

Now replace the pond with a metal conductor, and the stone with a suddenly changing magnetic field. The moment the magnetic flux through the metal changes, the electrons inside it — all throughout its bulk — start swirling in closed loops. These **whirlpool currents** are called **eddy currents** (also known as **Foucault currents**, after the French physicist Léon Foucault who first observed them in 1851 — yes, the same Foucault of the famous pendulum!).

> 🔑 **Key Takeaway:** Eddy currents are **induced currents** that flow in **closed loops** within the **bulk of a conductor** whenever the **magnetic flux through it changes**. They do NOT flow in an external circuit — they circulate *inside* the metal itself.

### Two Faces of Eddy Currents

Here is what makes eddy currents fascinating: they are **not always the villain**. They have a split personality — harmful in some situations, deliberately engineered as heroes in others.

Think of them like **friction**: mostly unwanted in machines (wastes energy as heat), but essential when you want to stop a bicycle (brake pads rely on it). Eddy currents are exactly the same:

| **Role** | **Device/Situation** | **What They Do** |
|---|---|---|
| ✅ Useful | Induction furnace | Melt metal through intense Joule heating |
| ✅ Useful | Electromagnetic brakes (trains, roller coasters) | Provide smooth, contactless braking |
| ✅ Useful | Dead-beat galvanometer | Damp oscillations quickly → readings settle fast |
| ✅ Useful | Speedometer (vehicle) | Pointer deflects proportionally to speed |
| ✅ Useful | Induction cooker | Heat generated directly in vessel base |
| ✅ Useful | Metal detectors (airports, security) | Detect metallic objects by eddy current signatures |
| ✅ Useful | Energy meters (kWh meter) | Aluminium disc rotates — counts units consumed |
| ❌ Harmful | Transformer cores | Energy lost as heat; reduces efficiency |
| ❌ Harmful | Electric motors, generators | Core losses — devices run hotter |
| ❌ Harmful | Sensitive balances | Unwanted damping of the balance beam |

> ⚠️ **Critical Insight:** A common exam trap — "Eddy currents are always undesirable." This is **FALSE**. They are **deliberately induced** in furnaces, cookers, and brakes. Only in transformers and motors are they a problem.

### How Lamination Tames Eddy Currents — The Intuitive Picture

Imagine a wide, smooth road: cars (electrons) can zoom at high speed. Now imagine that same road chopped into many narrow lanes separated by walls. The cars can no longer race freely — they get bottlenecked.

That is exactly what **lamination** does to eddy currents:
- A **solid iron core** allows large eddy current loops to circulate freely through the entire cross-section — like a wide open road. Result: large $I$, large $I^2R$ heat loss.
- A **laminated core** (thin sheets, each insulated from the next) confines each eddy current loop to within one thin lamina. The loop is tiny → current is tiny → heat loss is tiny.

> 💡 **Tip:** Lamination reduces but does **NOT eliminate** eddy currents. Each lamina still has its own (smaller) eddy currents. The total loss is significantly reduced, not zero.

> ⚠️ **Critical Insight:** Cutting **slots** in the metal also reduces eddy currents by breaking the circular path. Both lamination and slotting are valid methods.

### Direction of Eddy Currents

Eddy currents always obey **Lenz's Law**: they flow in a direction such that the magnetic field they create **opposes the change in flux** that produced them. This is why:
- A metal plate entering a magnetic field slows down (the eddy currents create a magnetic field that repels the approaching flux).
- A magnet falling through a copper pipe slows down dramatically — eddy currents in the pipe walls push back against the falling magnet.

> 🔑 **Key Takeaway — The 3 Must-Knows:**
> 1. Eddy currents form in **bulk conductors** (not just wires).
> 2. Their direction → **Lenz's law** (oppose the change).
> 3. Their effect → **Joule heating** ($H = I^2Rt$).

---

## 🔬 Stage 2: The Formula Lab

### Key Relationships

**Faraday's Law — the root cause:**
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

When the flux $\Phi_B$ through a bulk conductor changes, this EMF drives eddy currents through the conductor's own resistance.

**Joule Heating by Eddy Currents:**
$$P = \frac{\mathcal{E}^2}{R} = I^2 R \quad \text{(heat generated per unit time)}$$

**Qualitative Power Loss Relationship:**

$$P_{\text{eddy}} \propto \frac{B^2 \, f^2 \, t^2}{\rho}$$

where the variables are defined below:

| Symbol | Meaning | Unit |
|---|---|---|
| $P_{\text{eddy}}$ | Eddy current power loss | W |
| $B$ | Peak magnetic field (flux density) | T |
| $f$ | Frequency of alternating field | Hz |
| $t$ | Thickness of lamina (or conductor) | m |
| $\rho$ | Electrical resistivity of material | $\Omega\cdot\text{m}$ |
| $\mathcal{E}$ | Induced EMF | V |
| $I$ | Eddy current magnitude | A |
| $R$ | Resistance of eddy current path | $\Omega$ |
| $\Phi_B$ | Magnetic flux | Wb |

### What This Formula Tells Us

$$P_{\text{eddy}} \propto \frac{B^2 f^2 t^2}{\rho}$$

- **$P \propto t^2$:** Thinner laminations ($t$ small) → dramatically less eddy current loss. Halving lamination thickness reduces loss by a factor of 4!
- **$P \propto f^2$:** High-frequency devices (like induction cookers operating at 20–100 kHz) generate *enormous* eddy currents — which is exactly what they want.
- **$P \propto 1/\rho$:** High-resistivity materials (silicon steel vs pure iron) reduce eddy currents — that's why transformer cores use silicon steel (higher $\rho$ than pure iron).
- **$P \propto B^2$:** Stronger field → more eddy currents → more heating.

### Derivation Context

Eddy currents arise from Faraday's law applied to closed paths within the conductor's cross-section. For a circular path of radius $r$ in a changing field $B(t) = B_0 \sin(2\pi ft)$:

$$\mathcal{E} = -\frac{d}{dt}(B \cdot \pi r^2) = -\pi r^2 \frac{dB}{dt} = -\pi r^2 B_0 \cdot 2\pi f \cos(2\pi ft)$$

$$|\mathcal{E}|_{\max} = 2\pi^2 r^2 f B_0$$

This shows why $\mathcal{E} \propto f$ and $\mathcal{E} \propto B_0$, giving $P \propto \mathcal{E}^2 \propto f^2 B_0^2$.

### Key Numbers to Memorize

| Fact | Value |
|---|---|
| Eddy currents discovered by | Léon Foucault, 1851 |
| Also called | Foucault currents |
| Typical transformer lamination thickness | 0.35 mm to 0.5 mm |
| Silicon steel resistivity (vs pure iron) | ~6× higher |
| Induction cooker frequency | 20 kHz – 100 kHz |

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Define Eddy Currents + Formation ⭐

**Pattern:** "What are eddy currents? How are they formed? State their direction."

---

**Solved Example** 🟢

> **Q:** Define eddy currents. Explain how they are formed in a metallic conductor placed in a changing magnetic field.

<details><summary><b>Solution</b></summary>

**Eddy Currents (Foucault Currents):**

Eddy currents are **induced electric currents** that flow in **closed loops within the bulk of a conductor** when the magnetic flux linked with it changes.

**Formation:**

When a conducting material (a solid metal block, plate, or core) is subjected to a **time-varying magnetic field** (or when the conductor moves relative to a magnetic field), the changing flux induces an EMF throughout the bulk of the conductor (by Faraday's law):
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

Since the conductor offers a **continuous path** through its body, this EMF drives currents that circulate in **closed loops** within the bulk metal — much like whirlpools or eddies in water.

**Direction:**

By **Lenz's law**, the eddy currents flow in such a direction that the magnetic field produced by them **opposes the change in magnetic flux** responsible for their induction.

**Effect:**

Eddy currents cause **Joule heating** ($H = I^2Rt$) within the conductor, which is generally wasteful but can be put to use (e.g., induction furnace).

</details>

---

**Practice Questions:**

1. 🟢 What is another name for eddy currents and who discovered them?
<details><summary><b>Answer</b></summary>
Eddy currents are also called **Foucault currents**, named after **Léon Foucault** who first observed them in 1851. (Fun fact: he is the same scientist famous for the Foucault pendulum demonstrating Earth's rotation.)
</details>

2. 🟢 State the law that governs the direction of eddy currents.
<details><summary><b>Answer</b></summary>
**Lenz's Law** governs the direction of eddy currents. They always flow in a direction such that the magnetic field they create opposes the change in magnetic flux that produced them. This is a consequence of the law of conservation of energy.
</details>

3. 🟢 A conducting ring is placed in a region where the magnetic field is increasing. In which direction do eddy currents flow — to oppose or support the increasing field?
<details><summary><b>Answer</b></summary>
The eddy currents flow so as to **oppose the increasing field**. By Lenz's law, they create a magnetic field directed opposite to the increasing external field (i.e., into the page if the external field is increasing out of the page). This means the eddy current flows **clockwise** when viewed from the direction of the increasing field.
</details>

4. 🟡 Why are eddy currents called "eddy" currents? What physical phenomenon does the name refer to?
<details><summary><b>Answer</b></summary>
They are named "eddy" currents because they resemble **eddies** — the swirling whirlpool patterns seen in a fluid (like water in a river near an obstacle). Just as water eddies form closed circular loops within the fluid itself rather than flowing along a definite direction, these induced currents form **closed loops within the bulk of the conductor** rather than flowing along a well-defined external circuit.
</details>

5. 🟡 Can eddy currents be induced in non-ferromagnetic metals like copper and aluminium? Justify.
<details><summary><b>Answer</b></summary>
**Yes.** Eddy currents can be induced in **any conducting material** — ferromagnetic or not. The requirement is only that the material is a **conductor** and is exposed to a changing magnetic flux. Copper and aluminium are excellent conductors and exhibit very strong eddy currents (copper's high conductivity means large current for a given EMF). This is why a magnet falls slowly through a copper pipe — large eddy currents are induced in the copper walls.

⚠️ **Common trap:** Students wrongly think eddy currents only occur in iron/steel.
</details>

6. 🟡 A thick metal disc is rotated in a strong magnetic field. Where exactly do the eddy currents flow, and what is their immediate observable effect?
<details><summary><b>Answer</b></summary>
The eddy currents flow in **closed loops within the bulk of the disc** — swirling like water eddies in horizontal planes perpendicular to the magnetic field. Their immediate observable effect is that the disc **heats up** (Joule heating: $H = I^2Rt$) and the disc experiences a **retarding torque** that opposes its rotation (by Lenz's law). Sustained rotation requires continuous input of energy to overcome this drag.
</details>

7a. 🌱 Noob-Mode Bridge 🟡 A flat metal plate is slid sideways from a region where the magnetic field is zero into a region of stronger, uniform magnetic field. Does the magnetic flux through the plate change, and what will the induced eddy currents try to do according to Lenz's law?

<details><summary><b>Answer</b></summary>

Yes — as the plate enters the stronger-field region, the magnetic flux through it **increases with time**. By Faraday's law this induces eddy currents, and by **Lenz's law** those currents flow so as to **oppose the increase in flux**.

Consequence: the eddy currents create a magnetic field directed opposite to the external field, which produces a force that **opposes the plate's motion** (a retarding/repulsive effect). This is the single new idea needed below — a conductor moving through a **non-uniform** field has its flux change, so eddy currents appear and fight the motion.

</details>

7. 🔴 A solid conducting sphere is moved rapidly through a non-uniform magnetic field. Describe qualitatively how eddy currents are set up and what happens to the sphere's kinetic energy.
<details><summary><b>Answer</b></summary>
As the sphere moves through the non-uniform field, different parts of the sphere experience different flux values, and the flux through any cross-section of the sphere changes continuously. By Faraday's law, EMFs are induced throughout the sphere, driving eddy currents in complex 3D closed loops within the conducting material.

By Lenz's law, these currents create forces opposing the sphere's motion (electromagnetic drag). The sphere **slows down**. The kinetic energy of the sphere is converted into **heat** within the sphere through Joule heating ($H = I^2Rt$), effectively acting as a non-contact braking mechanism.
</details>

8a. 🌱 Noob-Mode Bridge 🟢 The eddy current power loss follows $P_{\text{eddy}} \propto \dfrac{B^2 f^2 t^2}{\rho}$. Suppose only the resistivity $\rho$ is doubled while $B, f,$ and $t$ are kept the same. By what factor does the loss change?

<details><summary><b>Answer</b></summary>

Since $P \propto 1/\rho$:

$$\frac{P_{\text{new}}}{P_{\text{old}}} = \frac{\rho_{\text{old}}}{\rho_{\text{new}}} = \frac{\rho}{2\rho} = \frac{1}{2}$$

The loss is **halved**. Lower resistivity means larger eddy currents and more heating — the exact idea used in Q8.

</details>

8. 🔴 Explain why eddy currents are larger in conductors with lower resistivity. Use the formula $P \propto B^2 f^2 t^2/\rho$ to justify.
<details><summary><b>Answer</b></summary>
From the relationship $P_{\text{eddy}} \propto \dfrac{B^2 f^2 t^2}{\rho}$:

- Lower resistivity ($\rho$ small) → more current flows for the same induced EMF (since $I = \mathcal{E}/R$ and $R \propto \rho$).
- More current → larger magnetic force, larger heating ($P = I^2R$).
- Despite lower $R$, the $I^2$ term dominates: $P = I^2R = (\mathcal{E}/R)^2 \cdot R = \mathcal{E}^2/R \propto 1/R \propto 1/\rho$.

Therefore, **lower resistivity = larger eddy currents = greater power loss**. This is why silicon steel (higher $\rho$ than pure iron) is preferred for transformer cores — it naturally reduces eddy current losses.
</details>

---

### Type 2: Applications — Explain Each ⭐ (Most Tested)

**Pattern:** "Explain the working of [device] based on eddy currents." OR "State two applications of eddy currents." (2 marks — appears **every year**)

---

**Solved Example** 🟢

> **Q:** Explain the working of an **induction furnace** using the principle of eddy currents. *(CBSE-style, 2 marks)*

<details><summary><b>Solution</b></summary>

**Induction Furnace — Working:**

1. **Setup:** A high-frequency alternating current (AC) is passed through a **induction coil** (solenoid) surrounding the metal to be melted (placed inside as the "core").

2. **Mechanism:** The rapidly alternating current creates a continuously and rapidly **changing magnetic field** inside the coil. This changing flux links with the metal sample.

3. **Eddy Currents:** By Faraday's law, the changing flux induces **very large eddy currents** in the bulk of the metal.

4. **Heating:** These large eddy currents flow through the metal's resistance, generating enormous **Joule heat** ($H = I^2Rt$). Since the frequency is very high ($f$ is large), the induced EMF and hence the currents are very large ($\mathcal{E} \propto f$), leading to intense heating.

5. **Result:** The metal **melts** due to the generated heat.

**Advantage:** No direct contact between the heating source and metal → very pure melting, controllable, efficient.

</details>

---

**Practice Questions:**

1. 🟢 Name any **four** applications of eddy currents.
<details><summary><b>Answer</b></summary>

Four applications of eddy currents:

1. **Induction furnace** — melting metals using Joule heating by eddy currents.
2. **Electromagnetic braking** — smooth, frictionless braking in trains and roller coasters.
3. **Dead-beat galvanometer** — eddy currents in the metal frame damp coil oscillations quickly.
4. **Speedometer (vehicle)** — rotating magnet induces eddy currents in an aluminium disc; the resulting drag torque deflects the pointer proportional to speed.

*(Other valid answers: induction cooker, metal detector, energy meter, electromagnetic damping in balances.)*
</details>

2. 🟢 How does a **speedometer** use eddy currents to measure vehicle speed?
<details><summary><b>Answer</b></summary>

**Speedometer Working:**

- A **permanent magnet** is mechanically linked to the vehicle's wheels/transmission shaft and rotates with it.
- The rotating magnet is placed close to an **aluminium disc** (which can freely rotate on a spindle), held by a **hair spring**.
- As the magnet rotates, its field (which varies relative to the disc) induces **eddy currents** in the aluminium disc.
- By Lenz's law, the eddy currents experience a **drag torque** that tries to drag the disc in the direction of magnet's rotation.
- The disc deflects against the restoring force of the hair spring until the drag torque equals the spring torque.
- The **deflection of the disc (and its pointer) is proportional to the rotational speed**, which is proportional to the vehicle's speed.

</details>

3. 🟡 How do eddy currents help in **electromagnetic braking** used in trains?
<details><summary><b>Answer</b></summary>

**Electromagnetic Braking:**

- Strong electromagnets are mounted on the train near the rails or disc brakes.
- When the electromagnet is energised, it creates a strong magnetic field in the conducting material (rail/disc).
- As the train (and disc/rail) moves, the relative motion causes a **change in flux** through the conductor → **eddy currents** are induced.
- By Lenz's law, these eddy currents create a force that **opposes the relative motion** of the conductor — i.e., they retard the motion of the train.
- **Advantage:** No mechanical contact → no wear and tear, smooth and quiet braking, can be modulated by controlling electromagnet current.

</details>

4. 🟡 Explain **electromagnetic damping** in a dead-beat galvanometer.
<details><summary><b>Answer</b></summary>

**Dead-Beat Galvanometer:**

- In an ordinary galvanometer, when current flows through the coil, it deflects and **oscillates** (back and forth) before settling at the equilibrium position, wasting time.
- In a dead-beat galvanometer, the coil is wound on a **metallic (aluminium) frame**.
- When the coil swings, the frame moves through the magnetic field of the galvanometer's permanent magnet → **eddy currents** are induced in the metal frame.
- By Lenz's law, these eddy currents create a force opposing the coil's motion, **damping the oscillations**.
- The coil comes to rest quickly (in approximately one swing — "dead beat") at the correct deflection.
- **Benefit:** Faster, more accurate readings.

</details>

5. 🟡 Explain why only certain types of cooking vessels work on an **induction cooker**.
<details><summary><b>Answer</b></summary>

**Induction Cooker — Vessel Requirement:**

- An induction cooker uses a high-frequency alternating current coil beneath the ceramic/glass surface. This creates a rapidly **changing magnetic field** above the surface.
- For the cooker to work, the cooking vessel must be made of a **ferromagnetic conductor** (iron, stainless steel with iron content, cast iron) that:
  - Is a **good conductor** so eddy currents can flow in its base.
  - Has **ferromagnetic properties** so it efficiently links with the magnetic flux from the coil.
- Aluminium pans (non-ferromagnetic) do not work because the weak flux linkage induces insufficient eddy currents. Similarly, glass/ceramic vessels are insulators and have no eddy currents.
- **Efficient heat generation** occurs only when the vessel base has good electrical conductivity AND adequate ferromagnetic coupling.

</details>

6. 🟡 Explain the working of a **metal detector** at airport security using eddy currents.
<details><summary><b>Answer</b></summary>

**Metal Detector:**

- The detector consists of a coil carrying an **alternating current**, creating a time-varying magnetic field in the region being scanned.
- When a **metallic object** (e.g., a weapon, coin) passes through this region, the changing magnetic field induces **eddy currents** in the metal object.
- These eddy currents in the metal object in turn produce their own magnetic field (by Ampere's law), which modifies the overall field sensed by a **receiver coil** in the detector.
- This **change in signal** in the receiver coil is detected electronically and triggers an **alarm**.
- Non-metallic objects (plastic, cloth) do not produce eddy currents and therefore do not trigger the alarm.

</details>

7a. 🌱 Noob-Mode Bridge 🟡 An induction-type energy meter contains a **voltage coil** (carrying current ∝ voltage) and a **current coil** (carrying current ∝ load current). Both produce alternating magnetic fields in the aluminium disc between them. What do these fields induce in the disc, and what is the result?

<details><summary><b>Answer</b></summary>

The alternating fields from the two coils induce **eddy currents** in the aluminium disc (Faraday's law). The interaction between these eddy currents and the coil magnetic fields produces a **torque** that makes the disc rotate. That single idea — two coils → eddy currents in a disc → rotation — is exactly what Q7 extends to "rotation ∝ power consumed."

</details>

7. 🔴 An **energy meter** (kWh meter) at home uses eddy currents. Explain the role of eddy currents in making the aluminium disc rotate at a speed proportional to power consumed.
<details><summary><b>Answer</b></summary>

**Energy Meter (Induction-type):**

- The meter has two electromagnets: one connected to the **voltage coil** (current proportional to voltage), the other to the **current coil** (current proportional to load current).
- These coils produce **alternating magnetic fields** that are phase-shifted relative to each other.
- The overlapping, phase-shifted fields induce **eddy currents** in the aluminium disc between them.
- The interaction between the eddy currents in the disc and the stator magnetic fields produces a **rotating torque** (similar to a single-phase induction motor) on the aluminium disc.
- This torque is proportional to the **product of voltage and current** → i.e., proportional to **power consumed**.
- A **permanent magnet** provides braking torque so the disc speed is proportional to power (not just torque).
- The disc **rotates continuously** as long as power is consumed, and the total rotations (counted by a gear mechanism) measure the **energy consumed (kWh)**.

</details>

8a. 🌱 Noob-Mode Bridge 🟢 A plastic bead and a metal bead of identical size are each dropped through a vertical solenoid that carries alternating current (AC). In which bead are eddy currents induced, and which one falls more slowly?

<details><summary><b>Answer</b></summary>

Eddy currents are induced only in the **metal bead** (a conductor). By Lenz's law they create a magnetic force opposing its downward motion, so the metal bead falls **more slowly** than in free fall. The **plastic bead** is an insulator — no eddy currents, no electromagnetic drag — so it falls freely and reaches the bottom first. This is the exact comparison Q8 asks about, with a solenoid instead of a plain magnet.

</details>

8. 🔴 A thin copper coin and a thin plastic disc of identical shape, size, and mass are simultaneously dropped through the core of a vertical solenoid carrying AC. Which reaches the bottom first? Explain with reference to eddy currents.
<details><summary><b>Answer</b></summary>

**The plastic disc reaches the bottom first.**

**Explanation:**

- As the **copper coin** falls through the solenoid, the changing magnetic flux through it (as it enters and exits different cross-sections of the solenoid) induces **eddy currents** in the copper.
- By Lenz's law, these eddy currents create magnetic forces that **oppose the downward motion** of the coin — an upward retarding force acts on it (electromagnetic drag).
- The copper coin therefore falls **more slowly** than it would under gravity alone.
- The **plastic disc** is a non-conductor — no eddy currents can form in it. It falls freely under gravity with no electromagnetic retardation.
- **Result:** Plastic disc reaches the bottom first; copper coin is delayed.

</details>

---

### Type 3: Disadvantages + How to Minimize ⭐

**Pattern:** "Eddy currents are undesirable in [device]. How are they minimized?"

---

**Solved Example** 🟡

> **Q:** Why are eddy currents undesirable in the core of a transformer? How is this loss minimized? *(CBSE 2016–2021, 1–2 marks)*

<details><summary><b>Solution</b></summary>

**Why Undesirable:**

The core of a transformer is made of iron/ferromagnetic material — a conductor. The alternating flux in the core induces **eddy currents** in the core material. These currents flow in closed loops within the core, and due to the core's resistance, cause **Joule heating** ($H = I^2Rt$). This energy is dissipated as waste heat and is called **iron loss (core loss)**, reducing the transformer's efficiency.

**How to Minimize — Laminated Core:**

The core is constructed from **thin sheets (laminations) of silicon steel**, each sheet coated with an insulating layer (varnish or oxide), stacked together.

**Why it works:**
- Each lamina is electrically isolated from its neighbours.
- Eddy current loops are confined within each thin lamina (cannot cross the insulating boundary).
- The loop path is much shorter and thinner → the **resistance** of the eddy current path is much higher.
- Smaller loop area → smaller induced EMF per loop ($\mathcal{E} = -d\Phi/dt$, and $\Phi \propto$ area).
- Result: Much **smaller eddy current** ($I = \mathcal{E}/R$, where both $\mathcal{E}$ decreases and $R$ increases).
- Net power loss $P = I^2R$ drops dramatically (typically by factors of hundreds).

**Additionally:** Silicon steel (instead of pure iron) is used because its **higher electrical resistivity** naturally reduces eddy currents.

**Note:** Lamination **reduces** but does not completely **eliminate** eddy currents.

</details>

---

**Practice Questions:**

1. 🟢 Name two methods to reduce eddy current losses in the core of an electrical machine.
<details><summary><b>Answer</b></summary>

Two methods to reduce eddy current losses:

1. **Laminated core:** Using thin, insulated metal sheets (laminations) instead of a solid core. Each lamina restricts eddy currents to a thin layer, drastically reducing their magnitude.
2. **High-resistivity material:** Using **silicon steel** (or other high-resistivity alloys) for the core instead of pure iron. Higher resistivity → smaller current for the same induced EMF.

*Additional method: Cutting **slots** in the core to break eddy current loops.*
</details>

2. 🟢 Why does laminating a core reduce eddy currents even though the total metal cross-section area is the same?
<details><summary><b>Answer</b></summary>

Even though the total metal area is unchanged, lamination works because:

- The **induced EMF per eddy current loop** is proportional to the **area enclosed by the loop** ($\mathcal{E} = -d\Phi/dt = -A \cdot dB/dt$). Confining loops to thin lamina means each loop encloses a tiny area → tiny EMF.
- The **resistance** of each thin loop is much larger (longer path relative to cross-section, and the insulating boundary forces current through a longer route).
- Small EMF + large R → very small I per lamina.
- Even added up, the total eddy current power loss is far less than in a solid core.

</details>

3. 🟡 A solid iron cylinder and a laminated iron cylinder of the same dimensions are placed in a sinusoidal varying magnetic field of the same frequency. Which heats up more and why?
<details><summary><b>Answer</b></summary>

The **solid iron cylinder** heats up much more. In the solid cylinder, large eddy current loops can circulate throughout the entire cross-section, leading to large current magnitude and large Joule heating ($P = I^2R$). In the laminated cylinder, eddy currents are confined to thin laminations; each loop has a tiny area (small EMF) and high resistance → much smaller currents → much less heating. So $P_{\text{solid}} \gg P_{\text{laminated}}$.
</details>

4. 🟡 Why is silicon steel preferred over pure iron for transformer cores, despite iron being more easily available?
<details><summary><b>Answer</b></summary>

Silicon steel is preferred because:

1. **Higher electrical resistivity:** Silicon alloying increases iron's resistivity by about 6×. Since eddy current loss $P \propto 1/\rho$, higher resistivity means less eddy current loss.
2. **Lower hysteresis loss:** Silicon steel has a narrower magnetic hysteresis loop, meaning less energy lost per magnetisation cycle (important in AC transformers that cycle millions of times daily).
3. Combined effect: transformer efficiency is significantly improved.

</details>

5. 🟡 Is it possible to make a metal core completely free from eddy currents? Explain.
<details><summary><b>Answer</b></summary>

**No, it is not possible to completely eliminate eddy currents** in a conducting core. Even with very thin laminations, each lamina still has a small but finite cross-section, so small eddy current loops still exist within each lamina. We can only **reduce** eddy currents to a negligible level using:
- Thinner laminations
- Higher-resistivity material
- Slotted structures

A completely eddy-current-free core would require a non-conducting material, but then no useful magnetic flux would be carried efficiently (ferromagnetic metals are needed for their high permeability).
</details>

6a. 🌱 Noob-Mode Bridge 🟢 The eddy current power loss obeys $P \propto t^2$ (thickness squared). If the lamination thickness is made **one-third** of the original value, by what factor does the loss change?

<details><summary><b>Answer</b></summary>

$$\frac{P_{\text{new}}}{P_{\text{old}}} = \left(\frac{t_{\text{new}}}{t_{\text{old}}}\right)^2 = \left(\frac{1}{3}\right)^2 = \frac{1}{9}$$

The loss drops to **one-ninth** of its original value. Same squaring rule, just with friendlier numbers — now try the halving case in Q6.

</details>

6. 🔴 The eddy current power loss in a transformer core is given by $P \propto B^2 f^2 t^2 / \rho$. A transformer currently uses laminations of thickness $t = 0.5$ mm. If the lamination thickness is halved to 0.25 mm, by what factor does the eddy current loss change?
<details><summary><b>Answer</b></summary>

Using the relation $P \propto t^2$:

$$\frac{P_{\text{new}}}{P_{\text{old}}} = \left(\frac{t_{\text{new}}}{t_{\text{old}}}\right)^2 = \left(\frac{0.25}{0.50}\right)^2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$$

The eddy current loss is **reduced to one-quarter** (25%) of its original value. This demonstrates why thinner laminations are always preferred — a halving of thickness gives a 4× reduction in losses.
</details>

7. 🔴 In what two ways does using a slotted (rather than smooth) disc reduce eddy current effects, compared to cutting many radial slots vs. one slot?
<details><summary><b>Answer</b></summary>

**Slotted disc vs. smooth disc:**

1. **Break in current paths:** Each radial slot cuts through potential eddy current loop paths, forcing the current to take longer, more resistive detours. More slots = more path interruptions = weaker eddy currents.
2. **Reduction of effective loop areas:** Slots divide the disc into smaller segments. Eddy currents in each segment enclose a smaller area → smaller induced EMF per loop → smaller current.

**Many radial slots vs. one slot:**
- **One slot:** Barely interrupts the circular eddy current paths — currents simply route around the single gap. Effect: minimal reduction.
- **Many radial slots (like spokes):** Multiple interruptions force eddy currents into very small, isolated segments with tiny loop areas. Effect: dramatic reduction in eddy currents. (You can demonstrate this: a slotted pendulum swings many more times in a magnetic field than a solid one.)

</details>

---

### Type 4: Electromagnetic Braking (Disc Slowing) ⭐

**Pattern:** "A metallic disc rotates between the poles of a magnet and slows down. Explain." *(CBSE 2018 — 2 marks)*

---

**Solved Example** 🟡

> **Q:** A metallic disc is rotated about its axis between the poles of a permanent magnet. The disc gradually slows down and stops. Explain this behaviour using Lenz's law. *(CBSE 2018-style)*

<details><summary><b>Solution</b></summary>

**Explanation:**

1. As the metallic disc rotates, the portion of the disc passing through the magnetic field (between the poles) **cuts through the magnetic flux lines**.

2. The flux through any cross-section within the disc changes continuously as different parts enter and exit the field → by **Faraday's law**, an EMF is induced in the disc, driving **eddy currents** in closed loops within the conducting disc.

3. By **Lenz's law**, these eddy currents flow in directions such that the forces on them (due to the magnetic field) **oppose the rotation of the disc** — this is a retarding (braking) torque.

4. The kinetic energy of the rotating disc is progressively converted to **heat** (Joule heating by eddy currents).

5. As the disc slows, the rate of flux change decreases, reducing the eddy currents; but the disc keeps losing energy until it comes to a **complete stop**.

6. This mechanism is the principle of **electromagnetic braking** — used in trains, roller coasters, and fairground rides for smooth, contact-free deceleration.

</details>

---

**Practice Questions:**

1. 🟢 A bar magnet is quickly moved towards an aluminium ring. What happens in the ring and why?
<details><summary><b>Answer</b></summary>
As the magnet approaches, the **magnetic flux through the aluminium ring increases**. By Faraday's law, an EMF is induced which drives **eddy currents** in the ring. By Lenz's law, these currents flow so as to create a magnetic field opposing the increasing flux (i.e., opposing the approaching magnet). Therefore, the ring **experiences a repulsive force** from the magnet. If the ring is free to move, it will be pushed away (this is the basis of maglev repulsion). If held fixed, the approaching magnet simply slows down (feels a resistive force).
</details>

2. 🟢 Why does a magnet dropped into a copper tube fall more slowly than one dropped through a plastic tube of the same dimensions?
<details><summary><b>Answer</b></summary>
As the magnet falls through the **copper tube**, the changing flux through each section of the tube induces large **eddy currents** in the conducting copper walls. By Lenz's law, these currents produce a magnetic field that **opposes the motion of the magnet** — an upward force acts on it. The effective gravitational pull is reduced, so the magnet falls slowly (apparently experiencing increased "friction" though there is no physical contact).

In a **plastic tube** (non-conductor), no eddy currents are induced, so the magnet falls freely under gravity — much faster.
</details>

3. 🟡 A pendulum with a metallic bob swings between the poles of an electromagnet. What happens to its oscillations when (a) the electromagnet is switched ON, (b) slots are cut in the metallic bob?
<details><summary><b>Answer</b></summary>

**(a) Electromagnet switched ON:**
- The metallic bob, moving through the magnetic field, experiences changing flux.
- Eddy currents are induced in the bob → electromagnetic drag by Lenz's law.
- Oscillations are **damped rapidly**; the bob slows much faster than in a field-free region.
- With strong enough field, the bob may stop within a few oscillations (dead-beat effect).

**(b) Slots cut in bob:**
- Slots interrupt the circular eddy current paths within the bob.
- The effective magnitude of eddy currents is greatly reduced.
- Electromagnetic damping is therefore much weaker.
- The pendulum oscillates for **much longer** before stopping.
- This is a classic demonstration of eddy current reduction by slotting.
</details>

4. 🟡 Explain why an aluminium plate placed in a changing magnetic field quickly comes to rest (if it was oscillating), but an identical plate made of wood would not.
<details><summary><b>Answer</b></summary>
**Aluminium plate:** Aluminium is a good electrical conductor. When it moves through the magnetic field (as it oscillates), changing flux induces strong eddy currents within the metal. By Lenz's law, these create retarding forces opposing the motion, converting kinetic energy rapidly to heat. The plate quickly reaches equilibrium — electromagnetic damping.

**Wood plate:** Wood is an electrical insulator. No eddy currents are induced regardless of the changing flux. No electromagnetic damping occurs. The plate continues to oscillate (energy dissipated only by air resistance and internal friction, much slower).
</details>

5a. 🌱 Noob-Mode Bridge 🟡 A magnet is moved toward a stationary conducting plate. By Lenz's law, what is the direction of the force on the plate, and how could a sustained version of this same repulsive effect be used to lift (levitate) the magnet?

<details><summary><b>Answer</b></summary>

As the magnet approaches, the changing flux induces eddy currents in the plate. By Lenz's law those currents create a magnetic field that **repels** the approaching magnet — so the force on the plate (and on the magnet) is **pushing them apart**. If the conductor and magnet keep moving relative to each other so the repulsion is continuously sustained, that upward repulsive force can balance the magnet's weight and **levitate** it. That is the levitation half of Q5; the braking half you already practised in Q3–Q4.

</details>

5. 🔴 Magnetic levitation (Maglev) trains use eddy currents for both **braking** and **levitation**. Explain both using Lenz's law.
<details><summary><b>Answer</b></summary>

**Electromagnetic Braking:**
- The train carries superconducting electromagnets that create strong magnetic fields.
- As the train moves over the conducting aluminium guide rails, the changing flux in the rails induces eddy currents.
- Lenz's law: these eddy currents create forces opposing the train's forward motion → braking force.
- Braking is modulated by controlling the magnet current.

**Electromagnetic Levitation:**
- When the train moves over conducting loops/rails embedded in the track, the changing flux induces eddy currents in the loops.
- These eddy currents create a magnetic field that **repels** the train's magnets (Lenz's law — opposing the approach).
- The repulsive force **lifts the train** above the track (levitation).
- The faster the train moves, the stronger the eddy currents and the larger the levitating force — hence there is typically a **minimum speed** below which the train cannot levitate (it rests on wheels at slow speeds).
</details>

---

### Type 5: Dead-Beat Galvanometer / Electromagnetic Damping ⭐

**Pattern:** "Explain electromagnetic damping in a galvanometer." *(CBSE 2017 — 2 marks)*

---

**Solved Example** 🟡

> **Q:** What is a dead-beat galvanometer? How does it achieve quick settlement using eddy currents? *(CBSE 2017)*

<details><summary><b>Solution</b></summary>

**Dead-Beat Galvanometer:**

A dead-beat galvanometer is a **moving-coil galvanometer** designed to bring the deflection pointer to its equilibrium (correct reading) position **quickly without oscillating** (i.e., without overshooting back and forth).

**Mechanism — Eddy Current Damping:**

1. The coil of the galvanometer is wound on a **rectangular aluminium frame** (metallic former).
2. When a current passes through the coil, it deflects in the magnetic field of the permanent magnet.
3. If the current suddenly stops or changes, the coil tends to overshoot due to inertia.
4. As the aluminium frame swings in the galvanometer's magnetic field, the flux through the frame changes → **eddy currents are induced** in the aluminium frame.
5. By **Lenz's law**, these eddy currents create a retarding torque that opposes the swing.
6. The coil quickly settles at the correct position with **minimal oscillation** — it is "dead-beat."

**Benefit:** Enables rapid, accurate reading of the galvanometer without waiting for oscillations to die down.

</details>

---

**Practice Questions:**

1. 🟢 What is electromagnetic damping? Name one instrument that uses it.
<details><summary><b>Answer</b></summary>
**Electromagnetic damping** is the phenomenon where the oscillations of a conducting object in a magnetic field are quickly suppressed by eddy currents induced in the object. By Lenz's law, the eddy currents create forces opposing the oscillatory motion, converting kinetic energy to heat and bringing the object to rest rapidly.

**Example:** Dead-beat galvanometer — the metallic coil frame experiences eddy current damping in the galvanometer's permanent magnet field.
</details>

2. 🟡 Why does an ordinary galvanometer oscillate before settling, while a dead-beat galvanometer does not?
<details><summary><b>Answer</b></summary>
An **ordinary galvanometer** has a coil wound on a non-conducting frame (or has no frame). When it deflects, there is no conducting material to generate eddy currents. The only restoring force is from the hair spring, which causes the system to overshoot and oscillate like a harmonic oscillator, settling only slowly due to air and bearing friction.

A **dead-beat galvanometer** has the coil wound on an aluminium frame. As the coil swings, eddy currents in the aluminium frame generate electromagnetic damping forces that quickly oppose and eliminate the oscillations, allowing the pointer to settle at the equilibrium reading almost immediately.
</details>

3. 🟡 In sensitive analytical balances, eddy current damping is deliberately employed. Explain how and why.
<details><summary><b>Answer</b></summary>
In high-precision analytical balances, the balance beam has a tendency to oscillate for a long time after a mass is placed on the pan (very low friction, high sensitivity). This wastes time and can be annoying. To speed up settling:

- A small **conducting plate (aluminium vane)** is attached to the balance beam.
- The vane moves between the poles of a **permanent magnet** as the beam oscillates.
- Eddy currents induced in the vane by the changing flux create Lenz-law forces opposing the oscillation.
- The beam is **critically damped** — it settles quickly without overshooting.
- The balance remains sensitive for small mass differences but settles rapidly after disturbance.
</details>

4a. 🌱 Noob-Mode Bridge 🟢 The eddy-current damping coefficient is proportional to the frame's electrical conductivity: $b \propto \sigma$. The coil frame is changed from aluminium (a good conductor) to paper (an insulator, $\sigma \approx 0$). What happens to $b$?

<details><summary><b>Answer</b></summary>

Since $b \propto \sigma$ and paper has $\sigma \approx 0$,

$$b_{\text{paper}} \approx 0$$

The electromagnetic damping essentially **vanishes**. (The full version in Q4 adds the factors $t^2$ and $B^2$ to give $b \propto \sigma t^2 B^2$, but the key point — no conductor, no damping — is already clear here.)

</details>

4. 🔴 A galvanometer coil wound on a metallic frame is replaced by one wound on a paper frame. How does the damping change? Would the galvanometer now be dead-beat? Justify quantitatively in terms of eddy currents.
<details><summary><b>Answer</b></summary>
**Change in damping:** The damping would decrease dramatically.

**Reason:** Paper is a non-conductor (insulator). The paper frame cannot support eddy currents (there are no free charge carriers to form current loops). The dominant electromagnetic damping mechanism is completely absent.

The galvanometer would **no longer be dead-beat**. Instead, it would oscillate many times before settling due to only air resistance and bearing friction — much like an underdamped harmonic oscillator.

**Quantitatively:** The damping coefficient due to eddy currents is $b \propto \sigma t^2 B^2$ (where $\sigma$ is conductivity of the frame). For paper, $\sigma \approx 0$, so $b \approx 0$. The system becomes effectively underdamped with quality factor $Q = m\omega_0/b \to \infty$, meaning extremely prolonged oscillations.
</details>

---

### Type 6: Assertion-Reason Conceptual Traps ⭐

**Pattern:** Standard CBSE Assertion-Reason format with options (A)/(B)/(C)/(D).

---

**Solved Example** 🟡

> **Q — Assertion-Reason:**
> **Assertion (A):** The core of a transformer is made of laminated sheets instead of a solid metallic core.
> **Reason (R):** Laminated sheets increase the resistance of the eddy current path, reducing the magnitude of eddy currents and hence the heat loss.
>
> Choose the correct option:
> (a) Both A and R are true; R is the correct explanation of A.
> (b) Both A and R are true; R is NOT the correct explanation of A.
> (c) A is true; R is false.
> (d) A is false; R is true.

<details><summary><b>Solution</b></summary>

**Answer: (a)**

**Explanation:**
- **Assertion** is TRUE: Transformer cores are indeed made of laminated sheets.
- **Reason** is TRUE: Lamination confines eddy current loops to each thin lamina → the path resistance for eddy currents increases (shorter, thinner path) → smaller current $I$ → smaller power loss $P = I^2R$.
- **R correctly explains A:** The reason why laminated cores are used is exactly because of the mechanism stated in R.

</details>

---

**Practice Questions:**

1. 🟡 **Assertion (A):** Eddy currents are always undesirable in electrical devices.  
   **Reason (R):** Eddy currents always produce heating and hence waste energy.

   (a) Both A and R are true; R is the correct explanation of A.  
   (b) Both A and R are true; R is NOT the correct explanation of A.  
   (c) A is true; R is false.  
   (d) A is false; R may be true or false.

<details><summary><b>Answer</b></summary>

**Answer: (d) — Assertion is false.**

**Explanation:**
- **Assertion is FALSE:** Eddy currents are NOT always undesirable. They are intentionally used in induction furnaces (to melt metal), electromagnetic brakes, dead-beat galvanometers, speedometers, induction cookers, and energy meters.
- **Reason analysis:** The statement "eddy currents produce heating" is TRUE (they always cause Joule heating). However, since the Assertion itself is false, the answer is (d).

⚠️ **Exam trap:** Students often think "eddy currents = bad." This Assertion specifically says "always undesirable" — the word "always" makes it false.

</details>

2. 🟡 **Assertion (A):** A metallic disc spinning between the poles of a permanent magnet gradually decelerates and stops.  
   **Reason (R):** Eddy currents induced in the disc by the magnetic field create a retarding torque opposing the rotation, by Lenz's law.

   (a) Both A and R are true; R is the correct explanation of A.  
   (b) Both A and R are true; R is NOT the correct explanation of A.  
   (c) A is true; R is false.  
   (d) A is false; R is true.

<details><summary><b>Answer</b></summary>

**Answer: (a)**

**Explanation:**
- **Assertion is TRUE:** The disc does decelerate and stop due to electromagnetic braking.
- **Reason is TRUE:** Eddy currents induced by the changing relative flux between the disc and field create a Lenz's law retarding torque.
- **R correctly explains A:** The stopping mechanism is precisely the eddy current drag described in R.

</details>

3. 🟡 **Assertion (A):** Eddy currents can be induced in non-ferromagnetic conductors like copper and aluminium.  
   **Reason (R):** Eddy current induction depends only on the presence of free charge carriers in the conductor and a changing magnetic flux — not on the magnetic properties of the material.

   (a) Both A and R are true; R is the correct explanation of A.  
   (b) Both A and R are true; R is NOT the correct explanation of A.  
   (c) A is true; R is false.  
   (d) A is false; R is true.

<details><summary><b>Answer</b></summary>

**Answer: (a)**

**Explanation:**
- **Assertion is TRUE:** Copper and aluminium both experience eddy currents — in fact, copper (very low resistivity) has among the largest eddy currents of any common metal.
- **Reason is TRUE:** Eddy current induction depends on: (1) the material being an electrical conductor (has free electrons), and (2) the presence of a changing magnetic flux. Whether the material is ferromagnetic or not is irrelevant to Faraday's law.
- **R correctly explains A:** The reason accurately explains why non-ferromagnetic metals also experience eddy currents.

</details>

---

### Type 7: Induction Cooker / Modern Applications (Competency-Based) ⭐

**Pattern:** Case study / scenario-based question about a modern device using eddy currents.

---

**Solved Example** 🟡

> **Q (Competency-Based):** Reena is designing an induction cooker for home use. She notes that:
> - Her old aluminium frying pan doesn't heat up on the induction cooker.
> - Her cast iron pan heats up almost instantly.
> 
> (i) Explain the principle behind induction cooking. (ii) Why doesn't the aluminium pan work? (iii) What modifications could make the aluminium pan compatible?

<details><summary><b>Solution</b></summary>

**(i) Principle of Induction Cooking:**

The induction cooker contains a **coil** carrying a high-frequency alternating current (20–100 kHz). This coil creates a rapidly **changing magnetic field** above the cooker surface. When a suitable conducting vessel is placed on the cooker, this changing flux induces **eddy currents** in the base of the vessel. These eddy currents flow through the vessel's resistance and generate **Joule heat** ($H = I^2Rt$) directly within the vessel material — cooking the food from the vessel outward.

**(ii) Why aluminium pan doesn't work:**

- Aluminium is non-ferromagnetic (magnetic permeability ≈ $\mu_0$, essentially the same as air).
- The magnetic coupling between the induction coil and an aluminium pan is very poor — the coil field passes through aluminium almost as easily as through air.
- Even though aluminium is a good electrical conductor, the **flux linkage is insufficient** to generate the high eddy currents needed for cooking.
- Additionally, aluminium's very low resistivity means that even if eddy currents do flow, the power $P = \mathcal{E}^2/R$ — but low $R$ and very low $\mathcal{E}$ (due to poor coupling) means negligible heating.

**(iii) Modification:**

Attach a **ferromagnetic steel disc** (iron or stainless steel base plate) to the bottom of the aluminium pan. This disc:
- Efficiently couples with the induction coil's magnetic field (high relative permeability).
- Has adequate resistivity for strong eddy current heating.
- Transfers heat to the aluminium pan body.
(Modern "induction-compatible" aluminium pans use exactly this trick — a bonded steel base.)

</details>

---

**Practice Questions:**

1. 🟢 An induction cooker works at 50 kHz instead of 50 Hz. Give one reason why high frequency is preferred.
<details><summary><b>Answer</b></summary>
At higher frequency, the rate of change of magnetic flux is much higher: $\mathcal{E} = -d\Phi/dt \propto f$. Higher EMF induces much larger eddy currents in the vessel base, generating far more Joule heat per unit time. This makes cooking fast and efficient. At 50 Hz, the eddy currents would be $50,000/50 = 1000$ times weaker in terms of induced EMF, making cooking impractically slow.
</details>

2. 🟡 A metal sculptor melts silver by placing it inside a coil connected to a high-frequency generator. After the silver melts, the coil itself is barely warm, even though it carries large currents. Explain why the silver melts but the coil doesn't.
<details><summary><b>Answer</b></summary>
- The **silver** is placed in the rapidly changing magnetic field created by the coil. Eddy currents are induced in the bulk silver, and Joule heating rapidly melts it. The silver absorbs energy from the field.
- The **coil** itself carries the current that creates the field, but it is typically made of **hollow copper tubing with water cooling**. The coil's resistive heating ($I^2R$ of the coil wire) is managed by the water coolant. Moreover, the coil is specifically designed with low resistance per unit length.
- The energy input to the system goes overwhelmingly into eddy-current heating of the silver (the primary load), not into the coil.
</details>

3a. 🌱 Noob-Mode Bridge 🟢 For eddy-current heating, $P_{\text{eddy}} \propto f^2$. If the operating frequency is doubled (say from 25 kHz to 50 kHz) with the same vessel and field amplitude, by what factor does the heating power increase?

<details><summary><b>Answer</b></summary>

$$\frac{P_B}{P_A} = \left(\frac{f_B}{f_A}\right)^2 = \left(\frac{50}{25}\right)^2 = 2^2 = 4$$

The heating power becomes **4× larger**. Q3 asks the same comparison as a case study — just watch the "same input power" caveat there.

</details>

3. 🔴 **Case Study:** A company manufactures two models of induction cookers:
    - Model A: operates at 25 kHz
    - Model B: operates at 50 kHz, same power input
    
    Both use the same type of iron-base cooking vessel. A student claims Model B will heat the vessel faster. Is the student correct? Use $P_{\text{eddy}} \propto f^2$ to justify.
<details><summary><b>Answer</b></summary>

The student is **partially correct** for eddy current heating, but the full picture requires care.

**For eddy current power loss (= vessel heating):**

$$\frac{P_B}{P_A} = \frac{f_B^2}{f_A^2} = \frac{(50\,000)^2}{(25\,000)^2} = \frac{4}{1} = 4$$

If both models operate at the same power **input**, the power drawn from the source is the same. However, the **distribution** of that power between the coil and the vessel depends on their relative impedances. At higher frequency, the coil's inductive reactance increases, which can reduce the actual current and modify power transfer.

**Net conclusion:** With the same total input power, Model B does not necessarily deliver 4× more heating to the vessel — the power is split between resistive losses and inductive reactance differently. In practice, induction cooker designers optimise frequency to maximise power delivery to the vessel for a given coil design. The student is correct that higher frequency tends to produce more intense eddy currents for a given field strength, but at the same input power, the total heating may be similar if the coil is properly impedance-matched.

**For a board-level answer:** Yes, Model B heats faster for the same magnetic field amplitude, since $P \propto f^2$ and 50 kHz gives 4× more eddy-current power. This is the board-expected answer.

</details>

---

## 🧱 Stage 4: MCQ Mastery

**Instructions for Assertion-Reason MCQs:**
> (a) Both A and R are true; R is the correct explanation of A.
> (b) Both A and R are true; R is NOT the correct explanation of A.
> (c) A is true; R is false.
> (d) A is false; R is true (or both false).

---

**Q1.** Which of the following devices does **NOT** use eddy currents?

&emsp;(a) Induction furnace &emsp;(b) Dead-beat galvanometer &emsp;(c) Crystal oscillator &emsp;(d) Electromagnetic brake

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Crystal oscillator**

A crystal oscillator relies on the piezoelectric effect of a quartz crystal — mechanical vibration generating electrical oscillations. It has no relation to electromagnetic induction or eddy currents.

All other options directly use eddy currents:
- Induction furnace → eddy current heating
- Dead-beat galvanometer → eddy current damping
- Electromagnetic brake → eddy current retardation

</details>

---

**Q2.** The core of a transformer is laminated to:

&emsp;(a) Reduce flux leakage &emsp;(b) Reduce copper losses &emsp;(c) Reduce hysteresis losses &emsp;(d) Reduce eddy current losses

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d) Reduce eddy current losses**

Lamination confines eddy currents to thin sheets, dramatically reducing their magnitude and the consequent Joule heating (iron loss). 

- Flux leakage is reduced by core design, not lamination.
- Copper loss ($I^2R$ in windings) is not affected by lamination.
- Hysteresis loss is reduced by choice of core material (silicon steel), not by lamination.

</details>

---

**Q3.** **(NCERT Exemplar Q6.7 style)** A metal plate gets heated when:

&emsp;(a) It is placed in a steady (DC) magnetic field only  
&emsp;(b) It carries a direct current through it  
&emsp;(c) It is placed in a time-varying magnetic field  
&emsp;(d) It moves through a spatially non-uniform magnetic field

Which of the above cause eddy current heating? *(Select ALL that apply)*

&emsp;(a) Only (c) &emsp;(b) (b) and (c) only &emsp;(c) (b), (c) and (d) &emsp;(d) (a), (b), (c) and (d)

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) — (b), (c), and (d)**

**Analysis of each option:**

- **(a) Steady DC magnetic field, plate stationary:** No change in flux → no induced EMF → no eddy currents. **No heating from eddy currents.** (The plate may heat slightly from hysteresis if ferromagnetic, but no eddy current heating.) ❌

- **(b) Direct current through plate:** The plate itself carries current → $I^2R$ Joule heating within the plate. This is **not** eddy current heating, but the plate does get hot. ✓

- **(c) Time-varying magnetic field:** $d\Phi/dt \neq 0$ → EMF induced → eddy currents → Joule heating. ✓ This is the **classic eddy current** mechanism.

- **(d) Moving through non-uniform field:** As the plate moves, different parts experience different B → flux through the plate changes with time → eddy currents induced → heating. ✓

**Conclusion:** Options (b), (c), and (d) all cause the plate to get heated. Answer: **(c)**.

</details>

---

**Q4.** A copper ring is held stationary in a region where the magnetic field is changing rapidly. Which of the following is true?

&emsp;(a) No current is induced since the ring is stationary  
&emsp;(b) Eddy currents are induced only if copper is ferromagnetic  
&emsp;(c) Current is induced in the ring; its direction opposes the change in flux  
&emsp;(d) Current is induced in the ring; its direction supports the change in flux

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Faraday's law requires only that the **flux through the conductor change** — the conductor itself does NOT need to move. A stationary ring in a changing magnetic field has changing flux → EMF → induced current. Copper is an excellent conductor, ferromagnetism is irrelevant. By Lenz's law, the current opposes the change in flux.

</details>

---

**Q5.** Which of the following statements about eddy currents is/are **CORRECT**?

**Statement I:** Eddy currents flow only in ferromagnetic materials like iron and steel.  
**Statement II:** Eddy currents are always a source of energy loss in electrical machines.

&emsp;(a) Only Statement I is correct  
&emsp;(b) Only Statement II is correct  
&emsp;(c) Both Statements I and II are correct  
&emsp;(d) Neither Statement I nor II is correct

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d) Neither Statement I nor II is correct**

- **Statement I is FALSE:** Eddy currents form in **any conductor** — copper, aluminium, brass, etc. (non-ferromagnetic). Ferromagnetism has nothing to do with eddy current induction.
- **Statement II is FALSE:** While eddy currents do cause losses in transformers, motors, and generators, they are **intentionally used** in induction furnaces, electromagnetic brakes, speedometers, and energy meters — they are not always a loss.

</details>

---

**Q6.** **(Assertion-Reason)** 

**Assertion (A):** A bar magnet dropped through a metallic (copper) cylindrical pipe falls much more slowly than when dropped through a plastic pipe of identical dimensions.  
**Reason (R):** Eddy currents induced in the copper pipe by the falling magnet create a magnetic field opposing the magnet's motion, providing an upward retarding force.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) — Both A and R are true; R is the correct explanation of A.**

- **A is TRUE:** Experimentally well-verified — a magnet through copper pipe falls extremely slowly (takes ~10× longer than through plastic).
- **R is TRUE:** By Faraday's law, the changing flux induces eddy currents in the copper. By Lenz's law, these eddy currents oppose the magnet's motion with an upward force.
- **R correctly explains A:** The slower fall is exactly due to the opposing magnetic force described in R.

</details>

---

**Q7.** **(Assertion-Reason)**

**Assertion (A):** In a dead-beat galvanometer, the pointer immediately settles at the correct reading without oscillating.  
**Reason (R):** The coil is wound on a soft iron core, which enhances the magnetic field and prevents oscillations.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) — A is true; R is false.**

- **A is TRUE:** A dead-beat galvanometer does quickly settle without oscillation.
- **R is FALSE:** The settling is achieved by **eddy current damping** in the **metallic (aluminium) former/frame** on which the coil is wound — not by a soft iron core. The coil is wound on an aluminium former, not a soft iron core. (Soft iron core is used to concentrate magnetic flux, but it is not the cause of dead-beat behaviour.)

</details>

---

**Q8.** **(Assertion-Reason)**

**Assertion (A):** Lamination of transformer cores reduces eddy current loss but does not completely eliminate it.  
**Reason (R):** Each lamina still has finite conductivity and finite cross-sectional area, so eddy currents still exist within each lamina, just at reduced levels.

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) — Both A and R are true; R is the correct explanation of A.**

- **A is TRUE:** Lamination dramatically reduces eddy current loss but cannot reduce it to zero.
- **R is TRUE:** Each lamina is a finite conductor with area and conductivity → some residual eddy current loops exist within each lamina.
- **R correctly explains A:** The reason eddy currents persist (though weakly) is because each lamina still provides a conducting cross-section for current flow.

</details>

---

**Q9.** An aluminium disc is rotated at angular velocity $\omega$ between the poles of a magnet. If the magnetic field strength is doubled while $\omega$ remains the same, the power dissipated as eddy currents:

&emsp;(a) Remains unchanged  
&emsp;(b) Doubles  
&emsp;(c) Quadruples  
&emsp;(d) Halves

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Quadruples**

From $P \propto B^2 f^2 t^2/\rho$, at constant frequency and geometry:

$$P \propto B^2$$

Doubling B: $P_{\text{new}} = P_{\text{old}} \times (2B)^2/B^2 = 4 P_{\text{old}}$

Power quadruples. This is why powerful magnets in electromagnetic brakes are very effective even at moderate speeds.

</details>

---

**Q10.** A graph is plotted of eddy current power loss $P$ vs frequency $f$ (for constant magnetic field amplitude). The graph is:

&emsp;(a) A straight line through the origin  
&emsp;(b) A parabola ($P \propto f^2$)  
&emsp;(c) An exponential curve  
&emsp;(d) A hyperbola

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) A parabola ($P \propto f^2$)**

From the eddy current power formula: $P \propto B^2 f^2 t^2/\rho$. At constant $B$, $t$, and $\rho$:

$$P \propto f^2$$

This is a **parabolic relationship** — a graph of $P$ vs $f$ is a parabola (passing through the origin). This is why high-frequency applications (like induction cookers at ~50 kHz) have enormous eddy current heating, while low-frequency transformers (50 Hz) have manageable eddy current loss.

</details>

---

**Q11.** Which of the following pairs of methods BOTH reduce eddy current losses?

&emsp;(a) Using thicker laminations; using pure iron instead of silicon steel  
&emsp;(b) Using thinner laminations; using high-resistivity silicon steel  
&emsp;(c) Using a solid core; reducing the frequency of operation  
&emsp;(d) Increasing the magnetic field; cutting slots in the core

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Thinner laminations + high-resistivity silicon steel**

- **Thinner laminations:** $P \propto t^2$ → thinner laminas → much less power loss. ✓
- **Silicon steel:** Higher resistivity ($\rho$ larger) → $P \propto 1/\rho$ → less loss. ✓

Analysis of wrong options:
- (a): **Thicker** laminations → **MORE** loss. Wrong direction.
- (c): Solid core → **MORE** eddy currents, not less.
- (d): Stronger field → $P \propto B^2$ → **MORE** loss.

</details>

---

**Q12.** A student performs an experiment: she swings a flat aluminium plate like a pendulum through the gap between two strong magnets. She observes the plate stops swinging very quickly. She then cuts several parallel slots in the plate and repeats the experiment. The plate now:

&emsp;(a) Stops even faster — the slots create more surface area for eddy currents  
&emsp;(b) Swings for longer — the slots reduce the eddy current paths, decreasing damping  
&emsp;(c) Swings identically — slots do not affect eddy currents  
&emsp;(d) Heats up more — slots concentrate current paths

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Swings for longer — the slots reduce the eddy current paths, decreasing damping**

The slots interrupt the circular eddy current loops that would otherwise flow in the bulk of the plate. With slots:
- The effective eddy current path is broken → eddy currents are much weaker.
- Electromagnetic damping force is reduced.
- The plate oscillates for longer (less energy is extracted per swing).

This classic demonstration is often performed in physics labs to visually show how slotting reduces eddy currents.

</details>

---

## 🔀 Stage 5: Type Mixer

*Problems combining multiple types — the kind you see in CBSE 5-mark questions and JEE.*

---

**Problem 1** 🟡 *(Types 1 + 2 + 3 combined)*

> A transformer has a solid iron core. An engineer proposes two separate upgrades to improve efficiency:
> **(a)** Replace the solid iron core with a laminated silicon-steel core.
> **(b)** Coat the individual laminations with shellac (an insulating varnish).
>
> Explain the role of eddy currents in the original loss, how each upgrade addresses the loss, and why both upgrades are needed together rather than individually.

<details><summary><b>Solution</b></summary>

**Original Problem — Eddy Currents in Solid Core:**

The transformer core carries alternating magnetic flux. The flux induces EMFs throughout the solid iron core by Faraday's law:
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$
Large eddy current loops circulate through the entire cross-section of the solid core. Since iron has low resistivity, the current $I = \mathcal{E}/R$ is large. Joule heating $P = I^2R$ causes significant energy loss (iron loss), reducing transformer efficiency.

---

**Upgrade (a) — Silicon Steel instead of Iron:**

Pure iron: resistivity $\rho_{\text{Fe}} \approx 10 \times 10^{-8}$ Ω·m  
Silicon steel: resistivity $\rho_{\text{Si-Fe}} \approx 50 \times 10^{-8}$ Ω·m (≈5× higher)

Since $P_{\text{eddy}} \propto 1/\rho$, using silicon steel reduces eddy current power loss by about 5×, even without lamination. Additionally, silicon steel has lower hysteresis loss. **This helps but is not sufficient alone** — a thick silicon-steel block still allows large eddy current loops.

---

**Upgrade (b) — Shellac Coating (Insulation between Laminations):**

If we laminate pure iron without insulation (bare metal sheets in contact), adjacent laminas are electrically connected → eddy current loops can cross lamination boundaries → effectiveness of lamination is nullified! The insulating shellac coating:
- Electrically isolates each lamina.
- Forces eddy currents to remain within each thin lamina.
- Dramatically reduces loop size → EMF ∝ area (small) and R ∝ 1/cross-section (large) → very small $I$.

**Why both are needed together:**

| Upgrade | Benefit | Limitation alone |
|---|---|---|
| Silicon steel only | Lower $\rho$ reduces $I$ | Still large loops in thick core |
| Insulated lamination only | Small loop areas | If low-$\rho$ material, $I$ still considerable |
| Both together | Small loops + high $\rho$ → minimal $I^2R$ | Maximum efficiency |

Together: small loop area (lamination) + high resistivity (silicon steel) + electrical isolation (shellac) = dramatic reduction in eddy current losses.

</details>

---

**Problem 2** 🟡 *(Types 4 + 5 combined)*

> A metallic bob pendulum swings between the poles of a strong electromagnet. The experimentalist observes:
> **(i)** When the electromagnet is ON, the bob stops within 3 swings.
> **(ii)** When a slotted bob of the same mass is used, it takes 15 swings to stop.
> **(iii)** When an identical plastic bob is used, it takes over 500 swings to stop.
>
> Explain all three observations using Lenz's law and eddy currents. Also explain how this phenomenon is useful in a galvanometer.

<details><summary><b>Solution</b></summary>

**Observation (i) — Solid metallic bob, electromagnet ON:**

- As the solid metal bob swings through the magnetic field, the flux through the bob changes continuously.
- Large eddy current loops form throughout the bulk of the solid bob — maximum eddy current magnitude since there are no path restrictions.
- By Lenz's law, these currents produce a force opposing the swing → large retarding force → rapid damping.
- Kinetic energy converts to heat quickly → **stops in ~3 swings.**

**Observation (ii) — Slotted metallic bob:**

- The slots cut through the potential eddy current loop paths, breaking the continuous metal path.
- Eddy currents are confined to small segments between slots → much smaller loop area → smaller induced EMF per loop → smaller current.
- Retarding force is significantly weaker.
- Damping is reduced → **takes ~15 swings** (≈5× more than solid bob).

**Observation (iii) — Plastic bob:**

- Plastic is an electrical insulator → **no eddy currents** can form.
- Zero electromagnetic damping.
- The bob loses energy only through air resistance and bearing friction, which are extremely small.
- Oscillation continues for a very long time → **~500+ swings.**

**Comparison Table:**

| Bob Type | Eddy Currents | Damping | Swings to Stop |
|---|---|---|---|
| Solid metal | Large | Strong | ~3 |
| Slotted metal | Reduced | Moderate | ~15 |
| Plastic | None | Minimal | ~500+ |

**Application in Galvanometer:**

In a dead-beat galvanometer, the coil is wound on an **aluminium frame** (equivalent to the solid metallic bob). When current causes the coil to deflect:
- The aluminium frame swings in the galvanometer's permanent magnet.
- Eddy currents in the frame provide electromagnetic damping (like observation (i)).
- The coil settles quickly at the correct reading position with minimal oscillation.
- This enables fast, accurate current measurements.

</details>

---

**Problem 3** 🔴 *(Types 2 + 7 combined — Competency-Based Case Study)*

> **Case Study: Smart Industrial Heating**
>
> A metallurgical plant is evaluating two methods to melt a 10 kg block of steel:
>
> **Method 1 (Traditional):** Place steel in a gas furnace at 1500°C — takes 45 minutes.  
> **Method 2 (Induction):** Place steel inside an induction coil driven at 50 kHz — takes 8 minutes.
>
> **(a)** Explain why the induction method is faster, using Faraday's law.  
> **(b)** The plant engineers add a **laminated iron yoke** around the induction coil to direct flux. Why must the yoke be laminated?  
> **(c)** An engineer suggests using a copper coil vs. a water-cooled copper coil. Which is correct and why?  
> **(d)** If the frequency is doubled to 100 kHz, what happens to the heating rate? (Use $P \propto f^2$)

<details><summary><b>Solution</b></summary>

**(a) Why induction is faster:**

In the gas furnace, heat is transferred by **convection and radiation** from the hot gases to the surface of the steel block, then slowly conducted inward. This is slow because steel is a poor thermal conductor relative to its mass.

In induction heating, the changing magnetic flux at 50 kHz induces eddy currents **throughout the entire bulk of the steel block simultaneously** (skin-depth effects at lower frequency mean the currents penetrate well). Every cubic centimeter of the steel generates its own Joule heat — the entire volume heats simultaneously, not from outside in.

By Faraday's law: $|\mathcal{E}| = |d\Phi/dt| \propto f$. At 50 kHz: EMF is 1000× that at 50 Hz → current is 1000× → power $\propto f^2$ is $10^6 ×$ that at 50 Hz. Concentrated, direct, volumetric heating makes induction dramatically faster.

**(b) Why the flux-directing yoke must be laminated:**

The yoke is made of iron to concentrate and direct the magnetic flux toward the steel sample (similar to a transformer core function). The iron yoke is itself in a time-varying magnetic field (at 50 kHz!). If it were solid, enormous eddy currents would circulate in it, causing:
- Massive Joule heating of the yoke itself (energy waste — not useful).
- Reduction of flux delivered to the steel sample.
- Possible overheating and damage to the yoke.

Lamination of the yoke confines eddy current loops to thin sheets → much weaker eddy currents → yoke stays cool → flux is efficiently delivered to the steel.

**(c) Copper coil vs. Water-cooled copper coil:**

**Water-cooled copper coil is the correct choice.**

The induction coil carries a very large high-frequency current to generate the intense magnetic field needed. Even copper's low resistance causes significant $I^2R$ heating in the coil at such large currents and frequency. Without cooling:
- The coil overheats → insulation melts → coil fails.
- Coil temperature rises, increasing resistance → more heating (runaway).

Water-cooled coils (hollow copper tubing with water flowing inside) remove this heat continuously, allowing sustained operation at high power levels. This is standard practice in all industrial induction heating systems.

**(d) Effect of doubling frequency to 100 kHz:**

From $P_{\text{eddy}} \propto f^2$:

$$\frac{P_{100\text{ kHz}}}{P_{50\text{ kHz}}} = \left(\frac{100}{50}\right)^2 = 4$$

The heating rate **quadruples**. If the original melting took 8 minutes, the new time would be approximately $8/4 = 2$ minutes.

**Important caveat:** At higher frequency, the **skin depth** decreases ($\delta \propto 1/\sqrt{f}$), meaning eddy currents concentrate near the surface rather than penetrating the full depth. For a 10 kg block, this may reduce the volumetric heating advantage at very high frequency. Optimal frequency depends on the size of the workpiece — smaller pieces/thinner cross-sections can use higher frequencies.

</details>

---

## 📋 Stage 6: Board Arsenal

*Exact-style CBSE board questions with model answers.*

---

**Q1. (CBSE 2015–2020 style, 2 marks)**

> **(a)** What are eddy currents? **(b)** State any two applications of eddy currents.

<details><summary><b>Model Answer</b></summary>

**(a) Eddy Currents [1 mark]:**

Eddy currents (also called Foucault currents) are **induced electric currents that flow in closed loops within the bulk of a conductor** whenever the magnetic flux linked with it changes. They are set up by the EMF induced by the changing flux (Faraday's law) and flow in directions governed by Lenz's law (opposing the change in flux).

**(b) Two Applications [1 mark]:**

1. **Induction Furnace:** A rapidly alternating magnetic field induces large eddy currents in the metal to be melted; Joule heating ($H = I^2Rt$) melts the metal.

2. **Electromagnetic Braking:** Eddy currents induced in moving conducting parts (wheels/discs) of trains create retarding forces (Lenz's law), providing smooth, contactless braking.

*(Other acceptable pairs: dead-beat galvanometer, speedometer, induction cooker, metal detector, energy meter.)*

</details>

---

**Q2. (CBSE 2016–2021 style, 1–2 marks)**

> Why is the core of a transformer made of laminated sheets instead of a solid piece of iron? Explain.

<details><summary><b>Model Answer</b></summary>

The alternating flux in the transformer core induces eddy currents in the iron core material, which cause energy loss as heat (Joule heating, $H = I^2Rt$). This reduces the transformer's efficiency.

**To reduce eddy current losses, the core is laminated:**

- The core is made of **thin sheets (laminations) of silicon steel**, each coated with an insulating varnish, stacked together.
- The insulating coating prevents current from flowing between laminations.
- Each lamination is thin → eddy current loops are confined to a small area within each sheet → **smaller induced EMF** and **higher resistance** per loop.
- The eddy currents are thus much weaker → much less Joule heating → higher transformer efficiency.

> **Note:** Silicon steel is used (instead of pure iron) for its higher resistivity, further reducing eddy currents, and lower hysteresis losses.

</details>

---

**Q3. (CBSE 2018 style, 2 marks)**

> A metallic disc is rotated about its axis in a region between the poles of a strong permanent magnet. The disc gradually slows down and eventually stops. Explain this phenomenon on the basis of electromagnetic induction.

<details><summary><b>Model Answer</b></summary>

As the metallic disc rotates, the portion of the disc passing between the poles of the magnet experiences a **continuously changing magnetic flux** (since different parts of the disc enter and exit the field, and the relative orientation changes).

By **Faraday's law**, this changing flux induces an EMF, which drives **eddy currents** in closed loops within the bulk of the conducting disc.

By **Lenz's law**, these eddy currents flow in a direction such that the magnetic force on them (force on current-carrying conductor in a magnetic field: $\vec{F} = I\vec{L} \times \vec{B}$) **opposes the rotation** of the disc — a retarding torque acts on the disc.

The rotational kinetic energy of the disc is progressively dissipated as **heat** in the disc (Joule heating by eddy currents). The disc slows down and eventually comes to rest.

This is the principle of **electromagnetic braking**, used in trains and other vehicles for smooth, contactless deceleration.

</details>

---

**Q4. (CBSE 2017 style, 2 marks)**

> A moving-coil galvanometer is said to be "dead-beat." What does this mean? Explain the role of eddy currents in achieving this behaviour.

<details><summary><b>Model Answer</b></summary>

**"Dead-beat" meaning:** A dead-beat galvanometer is one in which the coil deflects to its equilibrium position quickly and smoothly, **without oscillating** (no back-and-forth swinging) when the current changes. The pointer settles almost immediately.

**Role of Eddy Currents:**

1. The galvanometer coil is wound on a **metallic (aluminium) rectangular former/frame**.
2. When the coil deflects in the galvanometer's magnetic field (due to current), any overshoot causes the metallic frame to move through the field.
3. This motion induces **eddy currents** in the aluminium frame (Faraday's law).
4. By **Lenz's law**, these eddy currents create a magnetic field that opposes the motion of the frame — providing a **retarding (damping) force**.
5. The oscillations are **critically damped** — the coil comes to rest at the equilibrium position rapidly.

**Result:** Fast, accurate readings without waiting for oscillations to die down.

</details>

---

**Q5. (3-mark board question)**

> **(a)** Explain how eddy currents are set up in a metallic conductor placed in a time-varying magnetic field.  
> **(b)** Name THREE devices that use eddy currents, stating briefly how each device makes use of them.  
> **(c)** How can eddy current losses be minimized in the core of an electrical machine?

<details><summary><b>Model Answer</b></summary>

**(a) Formation of Eddy Currents [1 mark]:**

When a metallic conductor is placed in a region of time-varying magnetic field (or when a conductor moves in a magnetic field), the changing magnetic flux through the conductor induces an EMF throughout its bulk (Faraday's law: $\mathcal{E} = -d\Phi_B/dt$). Since the conductor is a continuous medium with many free electrons, this EMF drives currents in **closed loops within the bulk** of the conductor. These circulating induced currents are called **eddy currents** (Foucault currents). Their direction is given by Lenz's law — they oppose the change in flux.

**(b) Three Devices [1.5 marks]:**

| Device | Use of Eddy Currents |
|---|---|
| **Induction Furnace** | High-frequency alternating field induces massive eddy currents in metal; Joule heating melts the metal. |
| **Dead-Beat Galvanometer** | Eddy currents in the aluminium coil former damp oscillations via Lenz's law; pointer settles quickly. |
| **Speedometer** | Rotating magnet induces eddy currents in aluminium disc; drag torque deflects pointer ∝ speed. |

**(c) Minimizing Eddy Current Losses [0.5 marks]:**

1. **Lamination:** Use thin, insulated sheets (laminations) of silicon steel stacked together as the core. Eddy current loops are confined to thin laminas → smaller EMF per loop + higher resistance → much weaker currents.
2. **High-resistivity material:** Use silicon steel (resistivity ≈ 5× higher than pure iron) → $P \propto 1/\rho$ → less loss.

</details>

---

## 🚀 Stage 7: JEE Mains Arena

*Competitive-level MCQs requiring deeper analysis.*

---

**Q1.** *(JEE-style conceptual)* Which of the following does **NOT** reduce eddy current losses in a core?

&emsp;(a) Using laminated sheets insulated with varnish &emsp;&emsp;(b) Using high-resistivity material for the core  
&emsp;(c) Increasing the thickness of the individual laminations &emsp;&emsp;(d) Cutting slots in the conducting material

<details><summary><b>Answer</b></summary>

**Answer: (c) Increasing lamination thickness**

$P_{\text{eddy}} \propto t^2$ — increasing thickness **increases** eddy current loss. Halving thickness reduces it by a factor of 4.

- (a) Lamination with insulation → reduced eddy currents. ✓ (reduces loss)
- (b) High resistivity → $P \propto 1/\rho$ → reduced. ✓
- (d) Slots interrupt current paths → reduced. ✓
- (c) Thicker lamina → larger $t^2$ → **increased** loss. ✗

</details>

---

**Q2.** *(NCERT Exemplar Q6.7 adapted for JEE-MCQ II format)*

A metal plate is getting heated due to eddy currents. Which of the following situations can cause eddy current heating? *(One or more options may be correct)*

&emsp;(a) Plate carries a steady DC current  
&emsp;(b) Plate is placed in a time-varying magnetic field (AC field)  
&emsp;(c) Plate moves through a spatially uniform, steady magnetic field  
&emsp;(d) Plate moves through a spatially non-uniform, steady magnetic field

<details><summary><b>Answer</b></summary>

**Answer: (b) and (d)**

- **(a) Steady DC current:** Plate heats due to $I^2R$ (Joule heating from the external current), **not eddy currents**. No changing flux in the plate from this scenario.

- **(b) Time-varying (AC) magnetic field:** $d\Phi/dt \neq 0$ → Faraday's law → eddy currents → heating. ✓ **Classic eddy current scenario.**

- **(c) Uniform, steady field, plate moving:** If the field is **spatially uniform**, the flux through any cross-section of the plate does **not change** as it moves (same field everywhere). $d\Phi/dt = 0$ → no eddy currents. ✗

- **(d) Non-uniform, steady field, plate moving:** As the plate moves through a non-uniform field, different parts enter regions of different $B$ → flux through cross-sections changes with time → eddy currents → heating. ✓

**Note on (a):** Some NCERT Exemplar solutions include (a) because the DC current itself causes Joule heating — but this is **not eddy current heating**. The standard answer for "eddy current heating" is **(b) and (d)**.

</details>

---

**Q3.** *(JEE-analysis level)* A thin conducting circular disc of radius $R$, thickness $t$, and resistivity $\rho$ is placed perpendicular to a sinusoidal magnetic field $B = B_0 \sin(2\pi ft)$. The average power dissipated in the disc due to eddy currents is proportional to:

&emsp;(a) $B_0 f R^2 / \rho$ &emsp;&emsp;(b) $B_0^2 f^2 R^4 t / \rho$ &emsp;&emsp;(c) $B_0^2 f R^2 t^2 / \rho$ &emsp;&emsp;(d) $B_0^2 f^2 R^2 t / \rho$

<details><summary><b>Answer</b></summary>

**Answer: (b) $B_0^2 f^2 R^4 t / \rho$**

**Derivation:**

For an annular ring of radius $r$ and width $dr$ in the disc:
- EMF: $\mathcal{E} = \pi r^2 \cdot (dB/dt)_{\max} = \pi r^2 \cdot 2\pi f B_0$
- Resistance of ring: $dR = \rho \cdot (2\pi r)/(t \cdot dr)$
- Power: $dP = \mathcal{E}^2/(2dR) = \frac{(\pi r^2 \cdot 2\pi f B_0)^2}{2} \cdot \frac{t \, dr}{\rho \cdot 2\pi r}$
- $dP \propto r^3 dr$
- Total: $P \propto \int_0^R r^3 dr = R^4/4$

So: $P \propto B_0^2 f^2 R^4 t / \rho$

This confirms option **(b)**. Note $P \propto R^4$ — larger discs have dramatically more eddy current loss!

</details>

---

**Q4.** *(JEE reasoning)* Consider three scenarios:  
**P:** A solid copper block in a time-varying magnetic field.  
**Q:** A hollow copper shell (thin walls) in the same field.  
**R:** A solid copper block with 10 radial slots, in the same field.

Rank the eddy current power loss from highest to lowest:

&emsp;(a) P > Q > R &emsp;&emsp;(b) P > R > Q &emsp;&emsp;(c) Q > P > R &emsp;&emsp;(d) R > P > Q

<details><summary><b>Answer</b></summary>

**Answer: (b) P > R > Q**

**Analysis:**

**P (Solid block):** Maximum continuous cross-section → maximum eddy current loop size → maximum induced EMF and minimum resistance per loop → **largest eddy currents and power loss**.

**R (10 radial slots):** Slots interrupt circular eddy current paths, reducing effective loop area. However, currents still flow in the spaces between slots. Power loss is **intermediate** — significantly less than solid but more than hollow shell.

**Q (Hollow thin-walled shell):** The thin walls have very small cross-sectional area for eddy current loops (currents must flow through thin walls). The effective path resistance is high, loop area is limited to the thin wall cross-section. **Smallest eddy current losses** among the three.

**Ranking: P > R > Q** ✓

</details>

---

**Q5.** *(JEE trap question)* A metallic ring is placed with its plane parallel to a spatially uniform, time-varying magnetic field $B(t) = B_0 e^{-\alpha t}$. An identical ring made of a **superconductor** (zero resistance) is placed in the same field. Which statement is correct?

&emsp;(a) Both rings dissipate equal amounts of heat as eddy currents.  
&emsp;(b) The metallic ring dissipates more heat; the superconductor dissipates none.  
&emsp;(c) The superconductor dissipates more heat than the metallic ring.  
&emsp;(d) Neither ring dissipates heat, since both have $\mathcal{E} = 0$ in equilibrium.

<details><summary><b>Answer</b></summary>

**Answer: (b) The metallic ring dissipates more heat; the superconductor dissipates none.**

**Reasoning:**

**Metallic ring:** Changing $B$ → changing flux → EMF → eddy currents → Joule heating ($H = I^2Rt > 0$ since $R > 0$). Normal metal has finite resistance → energy is dissipated as heat.

**Superconductor:** Changing $B$ → changing flux → EMF → **perfect currents** induced (no resistance). However, the superconductor's induced currents are such that they completely expel the changing flux from its interior (Meissner effect / perfect diamagnetism). Since resistance $R = 0$:
$$H = I^2 R t = I^2 \cdot 0 \cdot t = 0$$

**No energy is dissipated** as heat in a superconductor. The induced currents persist indefinitely and the energy is stored in the magnetic field of the induced currents, not converted to heat.

**Additional nuance:** In a Type-II superconductor, flux penetrates in quantised vortices, and there can be small dissipation — but for the purposes of this JEE question, a superconductor is treated as zero-resistance → zero heat dissipation.

</details>

---

*→ [Chapter 7 — Self-Inductance](./07_self_induction.md)*

---

## 📝 Quick Reference Summary

| Concept | Key Point |
|---|---|
| Definition | Induced currents in closed loops within bulk conductor |
| Also called | Foucault currents (Léon Foucault, 1851) |
| Governing law | Lenz's law (oppose change in flux) |
| Effect | Joule heating ($H = I^2Rt$) |
| Power formula | $P \propto B^2 f^2 t^2/\rho$ |
| Reduction method 1 | Laminated core (thin insulated sheets) |
| Reduction method 2 | High-resistivity material (silicon steel) |
| Reduction method 3 | Slotted structure |
| Useful applications | Induction furnace, EM braking, dead-beat galvanometer, speedometer, induction cooker, metal detector, energy meter |
| Harmful | Transformer/motor core losses |
| Non-ferromagnetic? | Yes — copper, aluminium also have eddy currents |
| Lamination eliminates? | NO — reduces significantly, not eliminates |

> ⚠️ **Top 3 Exam Traps:**
> 1. "Eddy currents are always harmful" → **FALSE** (useful in many devices)
> 2. "Eddy currents only in ferromagnetic metals" → **FALSE** (any conductor)
> 3. "Lamination eliminates eddy currents" → **FALSE** (only reduces them)

---

*← [Chapter 5 — Energy Consideration](./05_energy_consideration.md)*&emsp;&emsp;*→ [Chapter 7 — Self-Inductance](./07_self_induction.md)*
