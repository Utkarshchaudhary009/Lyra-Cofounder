# Chapter 13: Energy Stored in a Capacitor

> *NCERT Section 2.14*

---

### The Paradox of the Invisible Fuel

A fully charged capacitor has no moving parts, no chemical reaction, no heat source — and yet, it can deliver a sudden burst of energy powerful enough to restart a human heart (defibrillator), weld metals (spot welding), or fire a camera flash. Where is this energy hiding?

It is stored not *in the charges*, not *in the plates*, but in the **electric field itself** between the plates. The field is not just a mathematical abstraction — it is a physical entity that stores energy in every cubic meter of space it occupies.

This is one of the deepest ideas in all of physics: **fields carry energy.** The electric field between the plates of a charged capacitor is a reservoir of energy, precisely the energy you invested while charging it.

---

### Building the Concept: Deriving the Energy Formula

Imagine charging a capacitor from scratch. At some intermediate stage, the capacitor already has charge $q$ on its plates and potential difference $v = q/C$.

To add an additional infinitesimal charge $dq$, the work done (against the existing electric field) is:

$$dW = v \, dq = \frac{q}{C} \, dq$$

The total work to charge the capacitor from $0$ to $Q$:

$$W = \int_0^Q \frac{q}{C} \, dq = \frac{1}{C} \cdot \frac{Q^2}{2} = \frac{Q^2}{2C}$$

This work is stored as potential energy $U$:

$$\boxed{U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV}$$

All three forms are equivalent (use whichever is convenient based on the given quantities).

| Formula | When to use |
|---------|------------|
| $U = \frac{Q^2}{2C}$ | When $Q$ is constant (battery disconnected scenarios) |
| $U = \frac{1}{2}CV^2$ | When $V$ is constant (battery connected scenarios) |
| $U = \frac{1}{2}QV$ | When both $Q$ and $V$ are given directly |

---

### Energy Density of the Electric Field

For a parallel plate capacitor with $C = \epsilon_0 A/d$, $V = Ed$:

$$U = \frac{1}{2}CV^2 = \frac{1}{2} \cdot \frac{\epsilon_0 A}{d} \cdot (Ed)^2 = \frac{1}{2}\epsilon_0 E^2 \cdot Ad$$

But $Ad$ is the volume of the space between the plates. So the **energy per unit volume** (energy density) is:

$$\boxed{u = \frac{U}{\text{Volume}} = \frac{1}{2}\epsilon_0 E^2}$$

In a medium with dielectric constant $K$:

$$u = \frac{1}{2}\epsilon E^2 = \frac{1}{2}K\epsilon_0 E^2$$

> **Profound Insight:** This formula is not limited to capacitors. It applies to *any* electric field, anywhere in space. Every region of space where an electric field exists contains energy at a density of $\frac{1}{2}\epsilon_0 E^2$ joules per cubic meter. This includes the field around a point charge, the field of a lightning bolt, or the field inside an atom.

---

### Checkpoint 1: Direct Energy Calculations

**The Defibrillator Scenario:** *A hospital defibrillator stores energy in a large capacitor, which is then discharged through the patient's chest to restore normal heart rhythm.*

**Problem 1:** The defibrillator has a $32\mu F$ capacitor charged to $5000$ V. How much energy is stored?

<details><summary><b>Solution</b></summary>

$U = \frac{1}{2}CV^2 = \frac{1}{2} \times 32 \times 10^{-6} \times (5000)^2$

$U = \frac{1}{2} \times 32 \times 10^{-6} \times 25 \times 10^6 = \frac{1}{2} \times 800 = \textbf{400 J}$

That's enough energy to lift a 40 kg object by 1 meter — delivered in a few milliseconds!
</details>

**Problem 2:** If only $200$ J needs to be delivered, what voltage should the capacitor be charged to?

<details><summary><b>Solution</b></summary>

$V = \sqrt{\frac{2U}{C}} = \sqrt{\frac{2 \times 200}{32 \times 10^{-6}}} = \sqrt{\frac{400}{32 \times 10^{-6}}}$

$V = \sqrt{12.5 \times 10^6} = \textbf{3536 V ≈ 3.54 kV}$

Halving the energy requires reducing the voltage by a factor of $\sqrt{2}$, not 2. Energy depends on $V^2$.
</details>

**Problem 3:** A $100$ pF capacitor stores $1\mu J$ of energy. What is the charge on the capacitor?

<details><summary><b>Solution</b></summary>

$U = \frac{Q^2}{2C} \implies Q = \sqrt{2CU}$

$Q = \sqrt{2 \times 100 \times 10^{-12} \times 10^{-6}} = \sqrt{2 \times 10^{-16}}$

$Q = \sqrt{2} \times 10^{-8} = \textbf{1.414 × 10⁻⁸ C ≈ 14.14 nC}$
</details>

---

### Checkpoint 2: The Gauntlet — "The Battery's Dilemma"

*A $10\mu F$ capacitor is connected to a $100$ V battery and fully charged.*

**Problem 1:** What energy is stored in the capacitor?

<details><summary><b>Solution</b></summary>

$U_C = \frac{1}{2}CV^2 = \frac{1}{2} \times 10 \times 10^{-6} \times (100)^2 = \textbf{0.05 J = 50 mJ}$
</details>

**Problem 2:** How much charge did the battery deliver?

<details><summary><b>Solution</b></summary>

$Q = CV = 10 \times 10^{-6} \times 100 = \textbf{1 mC}$
</details>

**Problem 3:** How much energy did the battery deliver?

<details><summary><b>Solution</b></summary>

The battery delivers energy $W_{battery} = QV = 1 \times 10^{-3} \times 100 = \textbf{0.1 J = 100 mJ}$
</details>

**Problem 4:** The capacitor stores 50 mJ but the battery delivered 100 mJ. Where did the other 50 mJ go?

<details><summary><b>Solution</b></summary>

The "missing" 50 mJ was dissipated as **heat** in the resistance of the connecting wires (and internal resistance of the battery) during the charging process.

This is a universal result: **exactly half** the energy delivered by a battery during capacitor charging is lost as heat, regardless of the resistance of the circuit. The resistance only affects *how fast* the charging occurs, not the energy balance.

$U_{stored} = \frac{1}{2}QV$, $W_{battery} = QV$. Lost energy = $QV - \frac{1}{2}QV = \frac{1}{2}QV$.

The 50% loss is fundamental, not a design flaw.
</details>

---

### Checkpoint 3: Energy Changes with Dielectrics

**Problem 1:** A $5\mu F$ capacitor is charged to $200$ V by a battery. The battery is then disconnected, and a dielectric slab of $K = 4$ is inserted. Find the energy before and after, and explain the change.

<details><summary><b>Solution</b></summary>

**Before:**
$U_i = \frac{1}{2}CV^2 = \frac{1}{2} \times 5 \times 10^{-6} \times (200)^2 = \textbf{0.1 J = 100 mJ}$

$Q = CV = 5 \times 10^{-6} \times 200 = 1 \times 10^{-3}$ C (this charge stays constant)

**After (battery disconnected):**
$C' = KC = 4 \times 5 = 20\mu F$

$U_f = \frac{Q^2}{2C'} = \frac{(10^{-3})^2}{2 \times 20 \times 10^{-6}} = \frac{10^{-6}}{4 \times 10^{-5}} = \textbf{0.025 J = 25 mJ}$

Energy decreased by a factor of $K = 4$. The "lost" 75 mJ went into the mechanical work done by the fringing electric field pulling the dielectric slab into the capacitor.
</details>

**Problem 2:** Repeat the above, but this time the battery remains connected while the dielectric is inserted. Compare.

<details><summary><b>Solution</b></summary>

**Before:**
$U_i = \frac{1}{2}CV^2 = 100$ mJ (same as above)

**After (battery connected, $V = 200$ V constant):**
$C' = KC = 20\mu F$

$U_f = \frac{1}{2}C'V^2 = \frac{1}{2} \times 20 \times 10^{-6} \times (200)^2 = \textbf{0.4 J = 400 mJ}$

Energy increased by a factor of $K = 4$!

Where did this extra energy come from? The battery supplied it. When the dielectric is inserted with the battery connected, the battery pumps additional charge to maintain the voltage, doing work in the process.

Energy supplied by battery: $W = Q_{new}V - Q_{old}V = (C'V - CV)V = (KC - C)V^2 = (K-1)CV^2$

$W = (4-1) \times 5 \times 10^{-6} \times 40000 = 600$ mJ

Of this 600 mJ:
- 300 mJ → stored in capacitor ($U_f - U_i = 400 - 100$)
- 300 mJ → spent pulling the dielectric in (mechanical work + heat)

Wait, let's recheck: $U_f - U_i = 400 - 100 = 300$ mJ. Battery supplied $(K-1)CV^2 = 3 \times 5 \times 10^{-6} \times 40000 = 600$ mJ.

Energy balance: $600 = 300$(stored) + $300$(dielectric pulling work).

Not quite — the work done pulling the slab in actually equals $\frac{1}{2}(K-1)CV^2 = 150$ mJ, and there's also heat in the wires. The complete energy accounting is subtle, but the key exam-relevant facts are:
- Battery connected + dielectric → energy increases
- Battery disconnected + dielectric → energy decreases
</details>

---

### Checkpoint 4: Energy Density

**Problem 1:** The electric field between the plates of a capacitor is $2 \times 10^4$ V/m. Calculate the energy density.

<details><summary><b>Solution</b></summary>

$u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2} \times 8.85 \times 10^{-12} \times (2 \times 10^4)^2$

$u = \frac{1}{2} \times 8.85 \times 10^{-12} \times 4 \times 10^8 = \textbf{1.77 × 10⁻³ J/m³}$
</details>

**Problem 2:** A parallel plate capacitor has plates of area $0.1$ m² separated by $5$ mm, charged to $500$ V. Calculate the total energy (a) using $U = \frac{1}{2}CV^2$, and (b) using energy density.

<details><summary><b>Solution</b></summary>

**(a)** $C = \epsilon_0 A/d = 8.85 \times 10^{-12} \times 0.1/(5 \times 10^{-3}) = 1.77 \times 10^{-10}$ F

$U = \frac{1}{2}CV^2 = \frac{1}{2} \times 1.77 \times 10^{-10} \times 250000 = \textbf{2.21 × 10⁻⁵ J = 22.1 μJ}$

**(b)** $E = V/d = 500/(5 \times 10^{-3}) = 10^5$ V/m

$u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2} \times 8.85 \times 10^{-12} \times 10^{10} = 4.425 \times 10^{-2}$ J/m³

Volume $= Ad = 0.1 \times 5 \times 10^{-3} = 5 \times 10^{-4}$ m³

$U = u \times \text{Volume} = 4.425 \times 10^{-2} \times 5 \times 10^{-4} = \textbf{2.21 × 10⁻⁵ J = 22.1 μJ}$ ✓

Both methods agree perfectly.
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** A $20\mu F$ capacitor and a $30\mu F$ capacitor are connected in series across a $600$ V battery.

(a) Find the charge on each and the voltage across each.  
(b) Find the total energy stored.  
(c) The battery is disconnected. The capacitors are now reconnected in parallel (positive to positive). Find the common voltage, the new energy, and the energy lost.  
(d) If the energy lost in (c) equals the energy needed to heat $m$ grams of water by $1°C$ (specific heat = $4.2$ J/g·°C), find $m$.

<details><summary><b>Solution</b></summary>

**(a)** $C_{eq} = \frac{20 \times 30}{20 + 30} = 12\mu F$

$Q = C_{eq}V = 12 \times 10^{-6} \times 600 = 7200\mu C = 7.2$ mC

$V_1 = Q/C_1 = 7200/20 = \textbf{360 V}$

$V_2 = Q/C_2 = 7200/30 = \textbf{240 V}$

Check: $360 + 240 = 600$ V ✓

**(b)** $U_{total} = \frac{1}{2}C_{eq}V^2 = \frac{1}{2} \times 12 \times 10^{-6} \times (600)^2 = \frac{1}{2} \times 12 \times 10^{-6} \times 360000$

$U_{total} = \textbf{2.16 J}$

**(c)** Each capacitor has charge $7200\mu C$. In parallel (positive to positive), total charge = $2 \times 7200 = 14400\mu C$.

$V_{common} = \frac{Q_{total}}{C_1 + C_2} = \frac{14400}{50} = \textbf{288 V}$

$U_{new} = \frac{1}{2}(C_1 + C_2)V_{common}^2 = \frac{1}{2} \times 50 \times 10^{-6} \times (288)^2 = \frac{1}{2} \times 50 \times 10^{-6} \times 82944$

$U_{new} = \textbf{2.074 J}$

Energy lost: $\Delta U = 2.16 - 2.074 = \textbf{0.086 J = 86 mJ}$

**(d)** $86 \times 10^{-3} = m \times 4.2 \times 1$

$m = \frac{86 \times 10^{-3}}{4.2} = \textbf{0.0205 g ≈ 20.5 mg}$

The "lost" energy can heat about 20 milligrams (a single drop) of water by 1°C. Even small capacitor energy losses are physically real and measurable.
</details>

---

## Question Bank — Chapter 13

### Section A: MCQs (15 Questions)

**Q1.** The energy stored in a capacitor of capacitance $C$ charged to voltage $V$ is:

(a) $CV$ &emsp; (b) $\frac{1}{2}CV$ &emsp; (c) $\frac{1}{2}CV^2$ &emsp; (d) $CV^2$

<details><summary><b>Answer</b></summary>**(c)** $U = \frac{1}{2}CV^2$.</details>

---

**Q2.** When a capacitor is charged from $0$ to $Q$, the total work done equals:

(a) $Q^2/C$ &emsp; (b) $Q^2/(2C)$ &emsp; (c) $QV$ &emsp; (d) $CV^2$

<details><summary><b>Answer</b></summary>**(b)** $W = \int_0^Q \frac{q}{C}dq = Q^2/(2C)$.</details>

---

**Q3.** The energy density in a uniform electric field $E$ is:

(a) $\epsilon_0 E$ &emsp; (b) $\frac{1}{2}\epsilon_0 E^2$ &emsp; (c) $\epsilon_0 E^2$ &emsp; (d) $E^2/(2\epsilon_0)$

<details><summary><b>Answer</b></summary>**(b)** $u = \frac{1}{2}\epsilon_0 E^2$.</details>

---

**Q4.** A battery delivers $Q$ charge at voltage $V$ to charge a capacitor. What fraction of the energy is stored in the capacitor?

(a) $1/4$ &emsp; (b) $1/2$ &emsp; (c) $3/4$ &emsp; (d) All

<details><summary><b>Answer</b></summary>**(b)** Battery delivers $QV$. Capacitor stores $\frac{1}{2}QV$. Always exactly half — the other half dissipates as heat.</details>

---

**Q5.** If the voltage across a capacitor is doubled, the energy stored:

(a) Doubles &emsp; (b) Quadruples &emsp; (c) Halves &emsp; (d) Remains same

<details><summary><b>Answer</b></summary>**(b)** $U \propto V^2$. Doubling $V$ quadruples $U$.</details>

---

**Q6.** Doubling the capacitance at constant charge, the energy:

(a) Doubles &emsp; (b) Quadruples &emsp; (c) Halves &emsp; (d) Quadruples

<details><summary><b>Answer</b></summary>**(c)** $U = Q^2/(2C)$. At constant $Q$, doubling $C$ halves $U$.</details>

---

**Q7.** The energy stored in a $100\,\mu F$ capacitor charged to $50$ V is:

(a) $125\,mJ$ &emsp; (b) $5\,mJ$ &emsp; (c) $250\,mJ$ &emsp; (d) $0.125\,J$

<details><summary><b>Answer</b></summary>**(a)** $U = \frac{1}{2}\times100\times10^{-6}\times2500 = 0.125$ J $= 125$ mJ.</details>

---

**Q8.** The energy stored in an electric field is:

(a) In the charges &emsp; (b) In the plates &emsp; (c) In the space between plates (the field itself) &emsp; (d) In the battery

<details><summary><b>Answer</b></summary>**(c)** Field carries energy. It's stored in the electric field permeating the space between the plates.</details>

---

**Q9.** Which formula should be used to find energy when charge is known but not voltage?

(a) $\frac{1}{2}CV^2$ &emsp; (b) $\frac{1}{2}QV$ &emsp; (c) $Q^2/(2C)$ &emsp; (d) $Q/C$

<details><summary><b>Answer</b></summary>**(c)** $U = Q^2/(2C)$ uses only $Q$ and $C$.</details>

---

**Q10.** When a dielectric is inserted (battery disconnected), energy:

(a) Increases &emsp; (b) Stays same &emsp; (c) Decreases by $K$ &emsp; (d) Increases by $K$

<details><summary><b>Answer</b></summary>**(c)** $U = Q^2/(2C') = Q^2/(2KC) = U_0/K$. Decreases by factor $K$.</details>

---

**Q11.** When a dielectric is inserted (battery connected), energy:

(a) Increases by $K$ &emsp; (b) Decreases by $K$ &emsp; (c) Stays same &emsp; (d) Doubles

<details><summary><b>Answer</b></summary>**(a)** $U = \frac{1}{2}C'V^2 = \frac{1}{2}KCV^2 = KU_0$. Increases by $K$.</details>

---

**Q12.** A camera flash uses a $1000\,\mu F$ capacitor charged to $300$ V. Energy stored is:

(a) $45\,J$ &emsp; (b) $4.5\,J$ &emsp; (c) $90\,J$ &emsp; (d) $150\,J$

<details><summary><b>Answer</b></summary>**(a)** $U = \frac{1}{2}\times10^{-3}\times9\times10^4 = 45$ J.</details>

---

**Q13.** The energy per unit volume in a dielectric with constant $K$ is:

(a) $\frac{1}{2}\epsilon_0 E^2$ &emsp; (b) $\frac{1}{2}K\epsilon_0 E^2$ &emsp; (c) $K\epsilon_0 E^2$ &emsp; (d) $\epsilon_0 E^2/K$

<details><summary><b>Answer</b></summary>**(b)** $u = \frac{1}{2}\epsilon E^2 = \frac{1}{2}K\epsilon_0 E^2$.</details>

---

**Q14.** A defibrillator uses a capacitor to deliver energy to the heart. This application uses the ability of a capacitor to:

(a) Store charge indefinitely &emsp; (b) Deliver large current in a short burst &emsp; (c) Reduce voltage &emsp; (d) Convert AC to DC

<details><summary><b>Answer</b></summary>**(b)** A charged capacitor can discharge rapidly through the body, delivering a large current pulse in milliseconds.</details>

---

**Q15.** The energy of the electric field around a uniformly charged sphere (outside, $r > R$) is:

(a) Infinite &emsp; (b) $kQ^2/(2R)$ &emsp; (c) $Q^2/(8\pi\epsilon_0 R)$ &emsp; (d) Zero

<details><summary><b>Answer</b></summary>**(c)** $U = \int_R^\infty \frac{1}{2}\epsilon_0 E^2\,4\pi r^2\,dr = \int_R^\infty \frac{1}{2}\epsilon_0 (kQ/r^2)^2\,4\pi r^2\,dr = \frac{Q^2}{8\pi\epsilon_0 R}$.</details>

---

### Section B: Short Answer Questions

**Q16.** Derive $U = \frac{1}{2}CV^2$ from the definition of work done in charging a capacitor.

<details><summary><b>Answer</b></summary>

At charge $q$, potential $v = q/C$. Work to add $dq$: $dW = v\,dq = (q/C)\,dq$.

Total work: $U = \int_0^Q (q/C)\,dq = \frac{Q^2}{2C} = \frac{(CV)^2}{2C} = \frac{1}{2}CV^2$ ✓

Also $U = \frac{1}{2}QV = \frac{1}{2}CV\times V = \frac{1}{2}CV^2$ ✓
</details>

---

**Q17.** A $40\,\mu F$ capacitor is charged to $1000$ V. Find the energy stored and the charge on the plates.

<details><summary><b>Answer</b></summary>

$U = \frac{1}{2}CV^2 = \frac{1}{2}\times40\times10^{-6}\times10^6 = \mathbf{20\,J}$

$Q = CV = 40\times10^{-6}\times1000 = \mathbf{0.04\,C = 40\,mC}$
</details>

---

**Q18.** Explain why exactly half the energy supplied by a battery is lost as heat when charging a capacitor, regardless of circuit resistance.

<details><summary><b>Answer</b></summary>

**Energy supplied by battery:** $W_{battery} = QV$ (charge $Q$ moved through voltage $V$).

**Energy stored in capacitor:** $U_C = \frac{1}{2}QV$ (integral of $qV/C\,dq$).

**Energy lost:** $W_{battery} - U_C = QV - \frac{1}{2}QV = \frac{1}{2}QV$.

**Why independent of $R$?** The energy dissipated is $\int I^2R\,dt$. Higher $R$ reduces current $I$ but increases time $t$ proportionally. The product $\int I^2R\,dt$ remains $\frac{1}{2}QV$ regardless. Even with a superconductor ($R = 0$), the energy is radiated as electromagnetic waves instead of heat.
</details>

---

**Q19.** Find the energy density in a capacitor ($V = 200$ V, $d = 2$ mm, $K = 3$).

<details><summary><b>Answer</b></summary>

$E = V/d = 200/(2\times10^{-3}) = 10^5$ V/m

$u = \frac{1}{2}K\epsilon_0 E^2 = \frac{1}{2}\times3\times8.85\times10^{-12}\times10^{10} = \mathbf{1.328\times10^{-1}\,J/m^3 = 132.8\,mJ/m^3}$
</details>

---

**Q20.** The parallel plate capacitor ($A = 0.01$ m², $d = 0.5$ mm) is charged to $100$ V. Find energy by both $U = \frac{1}{2}CV^2$ and energy density methods.

<details><summary><b>Answer</b></summary>

$C = \epsilon_0 A/d = 8.85\times10^{-12}\times0.01/(5\times10^{-4}) = 1.77\times10^{-10}$ F

**(Method 1):** $U = \frac{1}{2}\times1.77\times10^{-10}\times10^4 = \mathbf{8.85\times10^{-7}\,J = 0.885\,\mu J}$

**(Method 2):** $E = V/d = 10^5/0.5\times10^{-3}=2\times10^5$ V/m

$u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2}\times8.85\times10^{-12}\times4\times10^{10} = 0.177$ J/m³

$U = u\times Ad = 0.177\times0.01\times5\times10^{-4} = 8.85\times10^{-7}$ J ✓
</details>

---

**Q21.** A $100\,\mu F$ capacitor is charged by a $12$ V battery. Find: (a) charge, (b) energy stored, (c) energy supplied by battery, (d) energy lost as heat.

<details><summary><b>Answer</b></summary>

**(a)** $Q = CV = 10^{-4}\times12 = \mathbf{1.2\,mC}$

**(b)** $U_C = \frac{1}{2}CV^2 = \frac{1}{2}\times10^{-4}\times144 = \mathbf{7.2\,mJ}$

**(c)** $W_{battery} = QV = 1.2\times10^{-3}\times12 = \mathbf{14.4\,mJ}$

**(d)** $Q_{heat} = W_{battery} - U_C = 14.4-7.2 = \mathbf{7.2\,mJ}$ (exactly half)
</details>

---

**Q22.** The electric field breakdown of air is $3\times10^6$ V/m. Find the maximum energy density possible in an air capacitor.

<details><summary><b>Answer</b></summary>

$u_{max} = \frac{1}{2}\epsilon_0 E_{max}^2 = \frac{1}{2}\times8.85\times10^{-12}\times(3\times10^6)^2$

$= \frac{1}{2}\times8.85\times10^{-12}\times9\times10^{12} = \frac{1}{2}\times79.65 = \mathbf{39.8\,J/m^3}$
</details>

---

### Section C: Long Answer / JEE-Level

**Q23–Q30:** Energy problems.

**Q23.** Two capacitors $C_1 = 2\,\mu F$ (charged to $200$ V) and $C_2 = 8\,\mu F$ (uncharged) are connected in parallel. Find (a) common voltage, (b) energy before, (c) energy after, (d) percentage energy lost.

<details><summary><b>Answer</b></summary>

**(a)** $V = Q/C_{total} = (2\times200)/(2+8) = 400/10 = \mathbf{40\,V}$

**(b)** $U_i = \frac{1}{2}\times2\times10^{-6}\times40000 = \mathbf{40\,mJ}$

**(c)** $U_f = \frac{1}{2}\times10\times10^{-6}\times1600 = \mathbf{8\,mJ}$

**(d)** Loss $= 32\,mJ$. % lost $= 32/40\times100 = \mathbf{80\%}$
</details>

---

**Q24.** Derive $u = \frac{1}{2}\epsilon_0 E^2$ from the energy stored in a parallel plate capacitor.

<details><summary><b>Answer</b></summary>

$U = \frac{1}{2}CV^2$. For parallel plate: $C = \epsilon_0 A/d$, $V = Ed$.

$U = \frac{1}{2}\times\frac{\epsilon_0 A}{d}\times(Ed)^2 = \frac{1}{2}\epsilon_0 AEd\times E = \frac{1}{2}\epsilon_0 E^2\times(Ad)$

Volume $= Ad$. Energy density: $u = U/(Ad) = \frac{1}{2}\epsilon_0 E^2$ ✓
</details>

---

**Q25.** A $10\,\mu F$ capacitor is charged to $100$ V. A second $10\,\mu F$ is then connected in parallel (battery disconnected). Find the final voltage, energy before and after, and the energy lost.

<details><summary><b>Answer</b></summary>

$V_f = Q/C_{total} = 1000/20 = 50$ V

$U_i = \frac{1}{2}\times10^{-5}\times10^4 = 50\,mJ$

$U_f = \frac{1}{2}\times2\times10^{-5}\times2500 = 25\,mJ$

Energy lost $= 25\,mJ$.

Using formula: $\Delta U = \frac{C_1C_2(V_1-V_2)^2}{2(C_1+C_2)} = \frac{10^{-5}\times10^{-5}\times10^4}{2\times2\times10^{-5}} = \frac{10^{-6}}{4\times10^{-5}} = 25\,mJ$ ✓
</details>

---

**Q26.** How much energy must be supplied to move charge $Q$ from infinity to the surface of a sphere of radius $R$ already carrying charge $Q$?

<details><summary><b>Answer</b></summary>

The potential at the surface when charge is $q$: $V = kq/R$.

Energy to add final charge $Q$ (bringing from $\infty$ to surface where charge already $Q$):

$W = QV = Q\times kQ/R = kQ^2/R$

(This doubles the charge from $Q$ to $2Q$, not adds from $0$ to $Q$.)

For the *total* energy of the sphere with charge $Q$:

$U = \int_0^Q kq/R\,dq = kQ^2/(2R) = Q^2/(8\pi\epsilon_0 R)$
</details>

---

**Q27.** The energy stored in a $50\,\mu F$ capacitor is $10\,J$. What is the voltage? If the capacitor is discharged through a lamp in $0.1$ s, what is the average power?

<details><summary><b>Answer</b></summary>

$V = \sqrt{2U/C} = \sqrt{2\times10/(50\times10^{-6})} = \sqrt{4\times10^5} = \mathbf{632\,V}$

$P_{avg} = U/t = 10/0.1 = \mathbf{100\,W}$
</details>

---

**Q28.** Calculate the total electrostatic field energy stored around a proton modeled as a sphere of radius $r_p = 0.8\times10^{-15}$ m carrying charge $+e$.

<details><summary><b>Answer</b></summary>

Energy in field outside proton:

$U = \int_{r_p}^\infty \frac{1}{2}\epsilon_0 E^2\,4\pi r^2\,dr = \int_{r_p}^\infty \frac{ke^2}{2r^4}\times\frac{1}{k}\,4\pi r^2\,dr$

$= \frac{ke^2}{2}\int_{r_p}^\infty r^{-2}dr = \frac{ke^2}{2r_p}$

$= \frac{9\times10^9\times(1.6\times10^{-19})^2}{2\times0.8\times10^{-15}} = \frac{2.304\times10^{-28}}{1.6\times10^{-15}} = \mathbf{1.44\times10^{-13}\,J = 0.9\,MeV}$

This is the classical electrostatic self-energy of the proton.
</details>

---

**Q29.** Two parallel plate capacitors ($C_1 = 2\,\mu F$, $C_2 = 4\,\mu F$) are in series with a $12$ V battery. Find the energy stored in each and the total.

<details><summary><b>Answer</b></summary>

$C_{eq} = 4/3\,\mu F$; $Q = 12\times4/3\times10^{-6} = 16\,\mu C$

$U_1 = Q^2/(2C_1) = (16)^2/(2\times2)\,\mu J = 64\,\mu J$

$U_2 = Q^2/(2C_2) = (16)^2/(2\times4)\,\mu J = 32\,\mu J$

$U_{total} = 96\,\mu J$. Check: $U_{total} = \frac{1}{2}C_{eq}V^2 = \frac{1}{2}\times4/3\times10^{-6}\times144 = 96\,\mu J$ ✓
</details>

---

**Q30.** The electric field near a storm cloud reaches $2\times10^6$ V/m over a $5$ km² area, $500$ m deep. Estimate the total electrostatic energy in the field.

<details><summary><b>Answer</b></summary>

$u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2}\times8.85\times10^{-12}\times4\times10^{12} = 17.7$ J/m³

Volume $= 5\times10^6\times500 = 2.5\times10^9$ m³

$U = u\times V_{vol} = 17.7\times2.5\times10^9 = \mathbf{4.4\times10^{10}\,J = 44\,GJ}$

This is roughly the energy of a hydrogen bomb! It's also why lightning storms are so violent — they tap into this enormous stored energy.
</details>

---

*Next: [Chapter 14 — The Van de Graaff Generator →](./14_van_de_graaff_generator.md)*
