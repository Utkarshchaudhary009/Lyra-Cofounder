# Chapter 14: The Van de Graaff Generator

> *NCERT Section 2.15*

---

### The Story of the Million-Volt Machine

In 1929, a young physicist named Robert J. Van de Graaff had a simple but audacious idea: build a machine that could generate voltages so enormous — millions of volts — that it could accelerate subatomic particles to speeds sufficient for studying the atomic nucleus. No battery could produce such voltages. No power plant could supply them directly.

But Van de Graaff realised he didn't need a powerful source. He needed a **clever accumulator**. His insight rested on two elegant principles from electrostatics that we have already mastered in this book:

1. **Charge resides on the outer surface of a conductor** (Chapter 9).
2. **The potential of a conducting sphere increases linearly with charge** ($V = kQ/R$).

By repeatedly transferring small amounts of charge to the *inside* of a hollow metallic sphere, and letting it migrate to the outside, he could accumulate enormous charges — and therefore enormous potentials — on the sphere. The transfer mechanism was beautifully simple: a moving belt.

He built the first prototype in 1931 using a tin can, a silk ribbon, and a small motor. It generated 80,000 volts. His later machines reached **5 million volts** and became cornerstone instruments in nuclear physics laboratories worldwide.

---

### Building the Concept: How It Works

#### The Core Principle

Consider a large hollow conducting sphere of radius $R$. If we place a small charged sphere (charge $q$) inside the hollow sphere and touch it to the inner surface, all of the charge $q$ transfers to the outer surface of the hollow sphere (Property 2 from Chapter 9: charge always migrates to the outer surface).

After transfer, the small sphere is uncharged. It can be withdrawn, recharged, and brought back inside to deposit more charge. Each cycle adds $q$ to the outer surface.

After $n$ cycles, the charge on the hollow sphere is $nq$, and its potential is:

$$V = \frac{knq}{R}$$

In principle, there is **no limit** to how much charge can be accumulated — except the dielectric breakdown of the surrounding air (about $3 \times 10^6$ V/m), at which point sparks discharge the sphere.

#### The Mechanism (Belt-Based)

The practical Van de Graaff generator uses a continuously moving **insulating belt** instead of manually inserting charged spheres:

1. **Charging the belt (bottom):** A sharp metal comb (spray comb) connected to a high-voltage DC source ionises air near the belt. Positive ions are sprayed onto the belt.

2. **Transporting charge (belt motion):** The insulating belt carries the charges upward into the interior of the large hollow metallic dome.

3. **Collecting charge (top):** Inside the dome, a second sharp comb (collecting comb) draws the charges off the belt onto the inner surface of the dome. The charges immediately migrate to the outer surface.

4. **Accumulation:** As the belt runs continuously, charge accumulates on the dome, building the potential higher and higher.

#### Maximum Voltage

The dome's potential is limited by the electric field at its surface:

$$E_{surface} = \frac{kQ}{R^2} = \frac{V}{R}$$

When $E_{surface}$ exceeds the **dielectric strength** of the surrounding gas ($E_{breakdown} \approx 3 \times 10^6$ V/m for air at atmospheric pressure):

$$V_{max} = E_{breakdown} \times R$$

For a dome of radius $R = 1$ m: $V_{max} = 3 \times 10^6 \times 1 = 3 \times 10^6$ V $= 3$ MV.

To achieve higher voltages, generators are placed inside tanks of high-pressure insulating gas (like sulfur hexafluoride, $SF_6$, with $E_{breakdown} \approx 9 \times 10^6$ V/m), which triples the achievable voltage.

---

### Checkpoint 1: Direct Application

**Problem 1:** A Van de Graaff generator has a dome of radius $0.5$ m. What is the maximum voltage it can achieve in air ($E_{breakdown} = 3 \times 10^6$ V/m)?<br>

<details><summary><b>Solution</b></summary>

$V_{max} = E_{breakdown} \times R = 3 \times 10^6 \times 0.5 = \textbf{1.5 × 10⁶ V = 1.5 MV}$
</details>

**Problem 2:** What charge does the dome hold at this maximum voltage?<br>

<details><summary><b>Solution</b></summary>

$Q = \frac{VR}{k} = \frac{1.5 \times 10^6 \times 0.5}{9 \times 10^9} = \frac{7.5 \times 10^5}{9 \times 10^9}$

$Q = \textbf{8.33 × 10⁻⁵ C = 83.3 μC}$
</details>

**Problem 3:** The dome is placed inside a tank of $SF_6$ gas ($E_{breakdown} = 9 \times 10^6$ V/m). What is the new maximum voltage?<br>

<details><summary><b>Solution</b></summary>

$V_{max} = 9 \times 10^6 \times 0.5 = \textbf{4.5 × 10⁶ V = 4.5 MV}$

Three times higher — the high-pressure gas tripled the voltage limit.
</details>

---

### Checkpoint 2: The Gauntlet — "The Nuclear Accelerator"

*A nuclear physics laboratory uses a Van de Graaff generator (dome radius $R = 2$ m, operated in air) to accelerate protons for collision experiments.*

**Problem 1:** What is the maximum kinetic energy (in MeV) a proton can acquire from this generator?<br>

<details><summary><b>Solution</b></summary>

$V_{max} = E_{breakdown} \times R = 3 \times 10^6 \times 2 = 6 \times 10^6$ V $= 6$ MV

A proton with charge $e$ through $6$ MV gains:

$KE = eV = 6 \times 10^6$ eV $= \textbf{6 MeV}$

(Recall: $1$ eV = energy gained by charge $e$ through $1$ V.)
</details>

*The lab upgrades to $SF_6$ gas insulation ($E_{breakdown} = 9 \times 10^6$ V/m).*

**Problem 2:** What is the new maximum kinetic energy for a proton?<br>

<details><summary><b>Solution</b></summary>

$V_{max} = 9 \times 10^6 \times 2 = 18 \times 10^6$ V $= 18$ MV

$KE = \textbf{18 MeV}$

This is enough to probe nuclear structure — which is exactly what Van de Graaff generators were designed for.
</details>

**Problem 3:** If an alpha particle ($q = 2e$) is accelerated instead, what kinetic energy does it gain?<br>

<details><summary><b>Solution</b></summary>

$KE = qV = 2e \times 18 \times 10^6 = \textbf{36 MeV}$

Double the charge means double the energy for the same voltage.
</details>

**Problem 4:** What is the speed of the $6$ MeV proton?<br> ($m_p = 1.67 \times 10^{-27}$ kg)

<details><summary><b>Solution</b></summary>

$KE = 6$ MeV $= 6 \times 10^6 \times 1.6 \times 10^{-19} = 9.6 \times 10^{-13}$ J

$\frac{1}{2}mv^2 = 9.6 \times 10^{-13}$

$v = \sqrt{\frac{2 \times 9.6 \times 10^{-13}}{1.67 \times 10^{-27}}} = \sqrt{1.15 \times 10^{15}}$

$v = 3.39 \times 10^7$ m/s $\approx \textbf{3.4 × 10⁷ m/s}$

This is about 11% of the speed of light! At this speed, relativistic effects begin to matter.
</details>

---

### Applications and Limitations

#### Applications

| Application | How the VdG is used |
|-------------|:-------------------:|
| **Nuclear physics** | Accelerating protons, deuterons, alpha particles for nuclear reactions |
| **Particle physics** | As injectors for larger accelerators (synchrotrons) |
| **Radiation therapy** | Generating X-rays and electron beams for cancer treatment |
| **Science education** | Dramatic demonstrations of electrostatic principles |

#### Limitations

| Limitation | Reason |
|------------|--------|
| Maximum voltage limited | Dielectric breakdown of surrounding medium |
| Continuous current is small | Belt can only transport a limited charge per second |
| Not suitable for very high energies | Linear accelerators and synchrotrons are more efficient above ~20 MeV |
| Large physical size | High voltage requires large dome radius |

---

### Checkpoint 3: Conceptual Questions (Board Favorites)

**Problem 1:** Explain the principle of a Van de Graaff generator. *(3 marks)*

<details><summary><b>Model Answer</b></summary>

The Van de Graaff generator works on two electrostatic principles:

**Principle 1:** Electric charge always resides on the outer surface of a hollow conductor. When a charged conductor is placed inside a hollow conductor and touches it, all charge transfers to the outer surface of the hollow conductor.

**Principle 2:** The electric potential of a sphere is proportional to its charge ($V = kQ/R$). By continuously adding charge, the potential can be built up to very high values.

**Working:** A continuously moving insulating belt transports charges (sprayed onto it by a sharp comb at the base) into the interior of a large hollow metallic dome. Inside the dome, a collecting comb removes the charges, which migrate to the outer surface. This continuous process accumulates charge on the dome, raising its potential to millions of volts.

**Limitation:** The maximum voltage is limited by the dielectric breakdown of the surrounding medium (air or gas).
</details>

**Problem 2:** Why is the Van de Graaff generator enclosed in a steel chamber filled with high-pressure gas?<br>

<details><summary><b>Solution</b></summary>

The maximum voltage achievable is $V_{max} = E_{breakdown} \times R$. By using a gas with a higher dielectric strength (such as $SF_6$) at high pressure, $E_{breakdown}$ increases significantly (up to $9 \times 10^6$ V/m compared to air's $3 \times 10^6$ V/m). This allows the generator to achieve much higher voltages without sparking.

The steel chamber also contains the gas safely and shields the surroundings from the high voltage.
</details>

**Problem 3:** A Van de Graaff generator produces a potential of $5$ MV. Can it be used to drive current through a household appliance rated at $1$ kW, $220$ V?<br>

<details><summary><b>Solution</b></summary>

**No.** While the voltage is enormously high, the Van de Graaff generator delivers extremely small currents (of the order of microamperes). A $1$ kW appliance requires:

$I = P/V = 1000/220 \approx 4.5$ A

The generator cannot supply anywhere near this current. The Van de Graaff is a *high-voltage, low-current* device — useful for accelerating individual particles, not for powering appliances.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** A Van de Graaff generator has a dome of radius $R = 0.3$ m. The belt delivers charge at a rate of $5 \mu C/s$.

(a) What is the current flowing to the dome?<br>  
(b) How long will it take for the dome potential to reach $1$ MV?<br>  
(c) What is the charge on the dome at $1$ MV?<br>  
(d) What is the electric field at the surface at $1$ MV?<br> Is this below the breakdown threshold of air?<br>  
(e) What is the maximum achievable potential in air, and how long does it take to reach it?<br>

<details><summary><b>Solution</b></summary>

**(a)** Current = rate of charge flow = $5 \mu C/s = \textbf{5 × 10⁻⁶ A = 5 μA}$

**(b)** Charge needed for $V = 1$ MV:

$Q = \frac{VR}{k} = \frac{10^6 \times 0.3}{9 \times 10^9} = 3.33 \times 10^{-5}$ C $= 33.3\mu C$

Time: $t = Q/I = 33.3 \times 10^{-6}/(5 \times 10^{-6}) = \textbf{6.67 s}$

**(c)** $Q = \textbf{33.3 μC}$ (from above)

**(d)** $E = \frac{kQ}{R^2} = \frac{V}{R} = \frac{10^6}{0.3} = 3.33 \times 10^6$ V/m

This **exceeds** the breakdown threshold of air ($3 \times 10^6$ V/m). So $1$ MV is NOT achievable in air with this dome radius.

**(e)** $V_{max} = E_{breakdown} \times R = 3 \times 10^6 \times 0.3 = \textbf{9 × 10⁵ V = 900 kV}$

$Q_{max} = \frac{V_{max} R}{k} = \frac{9 \times 10^5 \times 0.3}{9 \times 10^9} = 3 \times 10^{-5}$ C $= 30\mu C$

$t = Q_{max}/I = 30/5 = \textbf{6 s}$

After 6 seconds, the dome reaches 900 kV and begins sparking. Any additional charge delivered by the belt is immediately lost through corona discharge at the surface.
</details>

---

## Question Bank — Chapter 14

### Section A: MCQs (15 Questions)

**Q1.** The working of a Van de Graaff generator is based on:

(a) Magnetic induction &emsp; (b) Charge always residing on outer surface of conductor &emsp; (c) Capacitance formula &emsp; (d) Ohm's law

<details><summary><b>Answer</b></summary>**(b)** Charge deposited inside a hollow conductor migrates to the outer surface, allowing unlimited accumulation.</details>

---

**Q2.** The maximum voltage a Van de Graaff generator can produce in air with a dome radius $R$ is:

(a) $V = kQ/R$ &emsp; (b) $V = E_{breakdown}/R$ &emsp; (c) $V = E_{breakdown}\times R$ &emsp; (d) $V = kR/Q$

<details><summary><b>Answer</b></summary>**(c)** $V_{max} = E_{breakdown}\times R$. Larger dome → higher max voltage.</details>

---

**Q3.** If the dome radius is doubled, the maximum achievable voltage:

(a) Halves &emsp; (b) Stays same &emsp; (c) Doubles &emsp; (d) Quadruples

<details><summary><b>Answer</b></summary>**(c)** $V_{max} = E_{breakdown}\times R$. Doubling $R$ doubles $V_{max}$.</details>

---

**Q4.** A Van de Graaff generator placed inside $SF_6$ gas achieves higher voltages because:

(a) Gas is colder &emsp; (b) $SF_6$ has higher dielectric strength than air &emsp; (c) Pressure is lower &emsp; (d) $SF_6$ is a better conductor

<details><summary><b>Answer</b></summary>**(b)** $SF_6$ has $E_{breakdown} \approx 9\times10^6$ V/m vs air's $3\times10^6$ V/m. Higher dielectric strength means higher $V_{max}$.</details>

---

**Q5.** The Van de Graaff generator is a:

(a) Low voltage, high current device &emsp; (b) High voltage, high current device &emsp; (c) High voltage, low current device &emsp; (d) Low voltage, low current device

<details><summary><b>Answer</b></summary>**(c)** The belt can only transport charge at a slow rate (microamperes), but to a very high voltage (megavolts).</details>

---

**Q6.** Which component of the Van de Graaff generator sprays charge onto the belt at the bottom?<br>

(a) Collecting comb &emsp; (b) Metal dome &emsp; (c) Spray comb (ionising comb) &emsp; (d) Motor

<details><summary><b>Answer</b></summary>**(c)** A sharp metal spray comb creates a corona discharge, spraying positive ions onto the belt.</details>

---

**Q7.** A proton accelerated through potential difference $V$ gains kinetic energy:

(a) $eV/2$ &emsp; (b) $eV$ &emsp; (c) $2eV$ &emsp; (d) $e^2V$

<details><summary><b>Answer</b></summary>**(b)** $KE = qV = eV$.</details>

---

**Q8.** What is the maximum kinetic energy a proton gains from a $3$ MV generator?<br>

(a) $1.5$ MeV &emsp; (b) $3$ MeV &emsp; (c) $6$ MeV &emsp; (d) $9$ MeV

<details><summary><b>Answer</b></summary>**(b)** $KE = eV = e\times3\times10^6 = 3$ MeV.</details>

---

**Q9.** An alpha particle ($q = 2e$) accelerated through $2$ MV gains KE of:

(a) $1$ MeV &emsp; (b) $2$ MeV &emsp; (c) $4$ MeV &emsp; (d) $8$ MeV

<details><summary><b>Answer</b></summary>**(c)** $KE = qV = 2e\times2\times10^6 = 4$ MeV.</details>

---

**Q10.** The charge on the dome increases until the potential reaches $V_{max}$. This is because:

(a) No more charge can fit on the dome &emsp; (b) The belt stops &emsp; (c) Dielectric breakdown causes charge to leak off &emsp; (d) The motor overheats

<details><summary><b>Answer</b></summary>**(c)** At $V_{max}$, the field at the dome surface equals $E_{breakdown}$. Air ionises, creating a conducting path that discharges the dome as fast as the belt charges it.</details>

---

**Q11.** The potential of the dome increases linearly with charge. This means:

(a) $V \propto Q^2$ &emsp; (b) $V \propto Q$ &emsp; (c) $V \propto 1/Q$ &emsp; (d) $V \propto Q/R^2$

<details><summary><b>Answer</b></summary>**(b)** $V = kQ/R$. Linear relationship between $V$ and $Q$ for a sphere.</details>

---

**Q12.** The primary purpose of Van de Graaff generators in nuclear physics labs is to:

(a) Generate electricity &emsp; (b) Create X-rays directly &emsp; (c) Accelerate charged particles for nuclear reactions &emsp; (d) Create magnetic fields

<details><summary><b>Answer</b></summary>**(c)** High voltage accelerates protons/alpha particles to energies (MeV) sufficient for nuclear reactions and structure studies.</details>

---

**Q13.** When you touch the dome of a Van de Graaff generator, your hair stands up because:

(a) Magnetic force acts on hair &emsp; (b) Like charges on hair strands repel each other &emsp; (c) Induced charges in hair attract &emsp; (d) Temperature rises

<details><summary><b>Answer</b></summary>**(b)** Charge distributes over your body including hair. Each hair strand carries the same sign charge and repels others, causing them to stand on end.</details>

---

**Q14.** The belt of a Van de Graaff generator must be:

(a) Metallic and conducting &emsp; (b) Insulating &emsp; (c) Magnetic &emsp; (d) Superconducting

<details><summary><b>Answer</b></summary>**(b)** The belt must be insulating to carry charges on its surface without conducting them away.</details>

---

**Q15.** The Van de Graaff generator becomes a Tandem Van de Graaff when:

(a) Two generators are used in series &emsp; (b) Negative ions are first accelerated to positive terminal, then electrons stripped, positive ions repelled again &emsp; (c) AC is used &emsp; (d) It operates underwater

<details><summary><b>Answer</b></summary>**(b)** Tandem design: negative ions accelerated toward +terminal, stripped of electrons at target, then positive ions repelled back — giving double the energy from the same voltage.</details>

---

### Section B: Short Answer Questions

**Q16.** Explain the principle and construction of a Van de Graaff generator with a labeled diagram description.

<details><summary><b>Answer</b></summary>

**Principle:** Two properties of conductors:
1. Charge resides on outer surface of a hollow conductor.
2. A sharp-tipped conductor at high potential ionises surrounding air (corona discharge).

**Construction:** A large hollow metallic dome (radius $R$) supported by insulating pillars. An insulating belt runs between two pulleys — one at the bottom (near a spray comb connected to DC source) and one at the top (inside the dome, near a collecting comb).

**Working:**
- Spray comb (bottom): $\approx10$ kV applied. Corona discharge sprays $+$ charges onto belt.
- Belt moves up, carrying charges into dome.
- Collecting comb (top): Draws charges off belt onto dome's inner surface.
- Charges migrate immediately to outer surface.
- Dome potential builds up to $V_{max} = E_{breakdown}\times R$.
</details>

---

**Q17.** A Van de Graaff dome of radius $0.4$ m operates in air. Find: (a) $V_{max}$, (b) max charge, (c) capacitance of dome.

<details><summary><b>Answer</b></summary>

**(a)** $V_{max} = E_{breakdown}\times R = 3\times10^6\times0.4 = \mathbf{1.2\,MV}$

**(b)** $Q_{max} = V_{max}R/k = 1.2\times10^6\times0.4/(9\times10^9) = 4.8\times10^5/(9\times10^9) = \mathbf{53.3\,\mu C}$

**(c)** $C = 4\pi\epsilon_0 R = R/k = 0.4/(9\times10^9) = \mathbf{4.44\times10^{-11}\,F = 44.4\,pF}$
</details>

---

**Q18.** A Van de Graaff belt transports $2\,\mu C/s$. The dome has radius $0.5$ m (in air). Find: (a) current, (b) time to reach max voltage.

<details><summary><b>Answer</b></summary>

**(a)** Current $= \mathbf{2\,\mu A}$

**(b)** $V_{max} = 3\times10^6\times0.5 = 1.5$ MV

$Q_{max} = V_{max}/k\times R = 1.5\times10^6\times0.5/(9\times10^9) = 83.3\,\mu C$

$t = Q_{max}/I = 83.3\times10^{-6}/(2\times10^{-6}) = \mathbf{41.7\,s}$
</details>

---

**Q19.** Why can't a Van de Graaff generator be used to power household appliances?<br>

<details><summary><b>Answer</b></summary>

Household appliances require **high current** (amperes). A Van de Graaff generator is a **high voltage, low current** device — the belt delivers charge at only a few microamperes.

Power = $VI$. Even at $10^6$ V, if $I = 10\,\mu A$: $P = 10^6\times10^{-5} = 10$ W.

A $1$ kW appliance needs $P/V = 1000/220 \approx 4.5$ A. The generator cannot supply this. Also, the voltage is DC and unregulated — not suitable for standard appliances.
</details>

---

**Q20.** Calculate the kinetic energy (in MeV and joules) of a doubly charged ion ($q = 2e$) accelerated through $5$ MV.

<details><summary><b>Answer</b></summary>

$KE = qV = 2e\times5\times10^6 = 10\,eV\times10^6 = \mathbf{10\,MeV}$

In joules: $KE = 10\times10^6\times1.6\times10^{-19} = \mathbf{1.6\times10^{-12}\,J}$
</details>

---

**Q21.** If a proton is accelerated from rest through a Van de Graaff generator ($V = 2$ MV), find its final speed. ($m_p = 1.67\times10^{-27}$ kg)

<details><summary><b>Answer</b></summary>

$KE = eV = 1.6\times10^{-19}\times2\times10^6 = 3.2\times10^{-13}$ J

$\frac{1}{2}m_pv^2 = 3.2\times10^{-13}$

$v = \sqrt{2\times3.2\times10^{-13}/1.67\times10^{-27}} = \sqrt{3.83\times10^{14}} = \mathbf{1.96\times10^7\,m/s}$

About 6.5% of the speed of light — relativistic effects are just starting to appear.
</details>

---

**Q22.** Describe three applications of the Van de Graaff generator beyond nuclear physics.

<details><summary><b>Answer</b></summary>

1. **Cancer Therapy:** Accelerated electrons or X-rays produced by the generator irradiate tumors. Precise high-energy beams kill cancer cells while sparing surrounding tissue.

2. **Ion Implantation (Semiconductor Manufacturing):** Ions accelerated by Van de Graaff machines are implanted into silicon wafers to create p-n junctions in computer chips. This is used in virtually every microprocessor.

3. **Electron Microscopy:** Accelerated electrons (by a scaled-down Van de Graaff) create the high-energy electron beams needed in electron microscopes, achieving resolutions of $<1$ nm — far better than optical microscopes.

4. **Science Education:** The benchtop Van de Graaff (miniature version) is used in schools to demonstrate electrostatics — making hair stand, creating sparks, and illustrating charge storage.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23–Q30:** Van de Graaff problems.

**Q23.** A VdG generator with dome of radius $1.5$ m is inside $SF_6$ ($E_{breakdown} = 9\times10^6$ V/m). Find: (a) $V_{max}$, (b) charge at $V_{max}$, (c) energy stored.

<details><summary><b>Answer</b></summary>

**(a)** $V_{max} = 9\times10^6\times1.5 = \mathbf{13.5\,MV}$

**(b)** $Q = V_{max}R/k = 13.5\times10^6\times1.5/(9\times10^9) = \mathbf{2.25\,mC}$

**(c)** $C = R/k = 1.5/(9\times10^9) = 1.67\times10^{-10}$ F

$U = \frac{1}{2}CV^2 = \frac{1}{2}\times1.67\times10^{-10}\times(13.5\times10^6)^2 = \frac{1}{2}\times1.67\times10^{-10}\times1.82\times10^{14} = \mathbf{15.2\,J}$
</details>

---

**Q24.** Compare the maximum achievable kinetic energy for (a) proton, (b) $\alpha$-particle, (c) electron accelerated through a $5$ MV Van de Graaff.

<details><summary><b>Answer</b></summary>

**(a) Proton** ($q = e$): $KE = eV = 5$ MeV

**(b) $\alpha$-particle** ($q = 2e$): $KE = 2e\times5 = 10$ MeV

**(c) Electron** ($q = -e$, decelerated by same field, or must reverse polarity): $KE = eV = 5$ MeV

Note: For equal charge magnitude, all gain 5 MeV per $e$ of charge. The alpha gains the most because $q = 2e$.
</details>

---

**Q25.** A nuclear physics experiment requires protons of $8$ MeV. Design a Van de Graaff in air. Find the minimum dome radius required.

<details><summary><b>Answer</b></summary>

$V_{required} = KE/e = 8\times10^6$ V $= 8$ MV

$R_{min} = V/E_{breakdown} = 8\times10^6/(3\times10^6) = \mathbf{2.67\,m}$

A dome of radius $\approx 2.67$ m would be needed. In practice, researchers use $SF_6$ to reduce the size:

$R_{min}(SF_6) = 8\times10^6/(9\times10^6) = \mathbf{0.89\,m}$ — much more practical.
</details>

---

**Q26.** The outer dome of a tandem Van de Graaff is at $+6$ MV. Explain how a tandem design doubles the particle energy compared to a conventional design.

<details><summary><b>Answer</b></summary>

**Conventional design:** Proton starts at ground (0 V) and accelerates to $+6$ MV dome: gains $KE = 6$ MeV.

**Tandem design:**
- Start: Negative hydrogen ion (H$^-$, charge $-e$) at ground.
- Phase 1: H$^-$ accelerated **toward** $+6$ MV terminal (opposite charge → attractive): gains $6$ MeV.
- At terminal: H$^-$ ion passes through a thin foil, both electrons stripped → bare proton ($+e$).
- Phase 2: Proton (now $+e$) **repelled** from $+6$ MV terminal back to ground: gains another $6$ MeV.

Total: $12$ MeV from a $6$ MV generator — double the conventional energy. No increase in dome voltage needed.
</details>

---

**Q27.** The dome of a Van de Graaff is grounded accidentally (connected to earth). What happens?<br>

<details><summary><b>Answer</b></summary>

When grounded: the dome's potential is forced to $V = 0$ (Earth potential). All stored charge flows to Earth instantly through the grounding wire. The dome completely discharges.

If the belt is still running: charge from the belt continues to flow to Earth. The dome potential remains at $0$ V — the belt simply acts as a pump delivering charge to Earth, not building up any voltage.

Removing the ground restores the normal operation.

(This is similar to a Faraday ice pail experiment, where grounding neutralizes the charge on an outer conductor.)
</details>

---

**Q28.** Why do Van de Graaff generators spark to nearby grounded conductors?<br> Explain using the concept of breakdown field.

<details><summary><b>Answer</b></summary>

As the dome charges up, the electric field outside the dome increases: $E = kQ/r^2$.

At the dome surface: $E_{surface} = V/R$. As $V$ approaches $V_{max} = E_{breakdown}\times R$, the field $E_{surface}$ approaches $E_{breakdown} = 3\times10^6$ V/m.

In the gap between the dome and a nearby grounded object: the field is $V/d$ where $d$ is the gap. If the dome is at $1$ MV and a grounded rod is $0.5$ m away:

$E_{gap} = 10^6/0.5 = 2\times10^6$ V/m < breakdown.

But if the rod is $0.3$ m away: $E_{gap} = 10^6/0.3 = 3.33\times10^6$ V/m > breakdown → spark!

The spark is a thin conducting channel of ionised air formed when $E > E_{breakdown}$. Current flows until the dome discharges.
</details>

---

**Q29.** A school Van de Graaff has a dome of radius $15$ cm. It operates in air. Find: (a) $V_{max}$, (b) maximum charge, (c) energy stored, (d) the length of spark you'd expect.

<details><summary><b>Answer</b></summary>

**(a)** $V_{max} = 3\times10^6\times0.15 = \mathbf{450\,kV}$

**(b)** $Q_{max} = V_{max}R/k = 4.5\times10^5\times0.15/(9\times10^9) = 7.5\,\mu C$

**(c)** $C = R/k = 1.67\times10^{-11}$ F; $U = \frac{1}{2}CV^2 = \frac{1}{2}\times1.67\times10^{-11}\times(4.5\times10^5)^2 = \mathbf{1.69\,J}$

**(d)** Spark length: $d_{max} = V_{max}/E_{breakdown} = 4.5\times10^5/(3\times10^6) = \mathbf{0.15\,m = 15\,cm}$

So the spark can jump up to 15 cm — the same as the dome radius!
</details>

---

**Q30.** A Van de Graaff generator has a dome of radius $R = 0.6$ m inside $SF_6$ ($E_{breakdown} = 9\times10^6$ V/m). The belt delivers $10\,\mu C/s$. How long does it take to reach max voltage?<br> What current does it deliver at steady state once breakdown begins?<br>

<details><summary><b>Answer</b></summary>

$V_{max} = E_{breakdown}\times R = 9\times10^6\times0.6 = 5.4$ MV

$Q_{max} = V_{max}R/k = 5.4\times10^6\times0.6/(9\times10^9) = 360\,\mu C$

$t = Q_{max}/I_{belt} = 360\times10^{-6}/(10\times10^{-6}) = \mathbf{36\,s}$

At steady state (breakdown): belt delivers $10\,\mu A$. This exactly equals the leakage current through corona discharge and sparks. The dome remains at $V_{max} = 5.4$ MV, and the steady-state output current to the experiment is **$10\,\mu A$ at $5.4$ MV**.
</details>

---

*This concludes the Electrostatic Potential and Capacitance mastery book.*

*Return to: [Table of Contents →](./00_preface.md)*
