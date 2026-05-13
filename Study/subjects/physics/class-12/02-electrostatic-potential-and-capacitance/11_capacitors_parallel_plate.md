# Chapter 11: Capacitors and the Parallel Plate Capacitor

> *NCERT Sections 2.11–2.12*

---

### The Story of the Leyden Jar

In 1745, a Dutch scientist named Pieter van Musschenbroek was trying to store electricity in a bottle of water. He connected a wire from an electrostatic generator to the water inside a glass jar, and then held the jar in his hand. When he accidentally touched the wire, he received a violent shock — so powerful that he reportedly said he "would not take a second shock for the kingdom of France."

He had invented the **Leyden jar** — the first capacitor. Without knowing it, he had created a device with a conductor (the water), an insulator (the glass), and another conductor (his hand). The glass separated two charged surfaces, and the device stored far more charge than a conductor alone ever could.

This is the fundamental principle of a capacitor: **two conductors separated by an insulator, designed to store charge and energy.** Every electronic device you own — your phone, laptop, TV — contains thousands of capacitors.

---

### Building the Concept: Capacitance

#### What is a Capacitor?

A capacitor is a system of two conductors (called **plates**) separated by an insulating medium (air, vacuum, or a dielectric). When connected to a battery:
- One plate acquires charge $+Q$ 
- The other acquires charge $-Q$
- A potential difference $V$ develops between them

The ratio of charge to potential difference is a constant for any given capacitor:

$$\boxed{C = \frac{Q}{V}}$$

This constant $C$ is the **capacitance** — a measure of how much charge the capacitor can store per volt of potential difference.

| Quantity | Symbol | SI Unit |
|----------|:------:|:-------:|
| Capacitance | $C$ | Farad (F) = C/V |

> **The Farad is enormous.** A 1 F capacitor storing 1 V would hold 1 Coulomb of charge — roughly the charge in a lightning bolt. Practical capacitors are measured in $\mu F$ ($10^{-6}$), $nF$ ($10^{-9}$), or $pF$ ($10^{-12}$).

#### Capacitance of an Isolated Sphere

A conducting sphere of radius $R$ carrying charge $Q$ has potential $V = kQ/R$:

$$C = \frac{Q}{V} = \frac{Q}{kQ/R} = \frac{R}{k} = 4\pi\epsilon_0 R$$

For the Earth ($R = 6400$ km): $C = 4\pi \times 8.85 \times 10^{-12} \times 6.4 \times 10^6 \approx 711\mu F$. Even the entire Earth has less than 1 millifarad of capacitance.

---

### Building the Concept: The Parallel Plate Capacitor

The most important capacitor geometry. Two large, flat conducting plates of area $A$, separated by distance $d$, with $d \ll \sqrt{A}$ (so edge effects are negligible).

#### Derivation of Capacitance

1. **Surface charge density:** $\sigma = Q/A$ on each plate.

2. **Electric field between the plates:** Using Gauss's Law (or superposition of two infinite planes):

$$E = \frac{\sigma}{\epsilon_0} = \frac{Q}{\epsilon_0 A}$$

3. **Potential difference:** $V = Ed = \frac{Qd}{\epsilon_0 A}$

4. **Capacitance:**

$$\boxed{C_0 = \frac{\epsilon_0 A}{d}}$$

This formula reveals three ways to increase capacitance:
- **Increase plate area $A$** — more surface to store charge
- **Decrease plate separation $d$** — stronger field, higher $\sigma$ for the same $V$
- **Insert a dielectric** (see below)

#### With a Dielectric Slab (Thickness = $d$, Constant $K$)

The dielectric reduces the field by factor $K$, so $V_{new} = V_0/K$, while $Q$ remains unchanged:

$$\boxed{C = KC_0 = \frac{K\epsilon_0 A}{d} = \frac{\epsilon A}{d}}$$

where $\epsilon = K\epsilon_0$ is the permittivity of the dielectric material.

#### With a Partial Dielectric (Thickness $t < d$)

If a dielectric slab of thickness $t$ and constant $K$ is inserted (the rest is air):

$$\boxed{C = \frac{\epsilon_0 A}{d - t + t/K}}$$

> **Derivation sketch:** The total potential difference is the sum of the voltage across the air gap and the voltage across the dielectric: $V = E_{air}(d-t) + E_{dielectric} \times t = \frac{\sigma}{\epsilon_0}(d-t) + \frac{\sigma}{K\epsilon_0}t = \frac{\sigma}{\epsilon_0}\left(d - t + \frac{t}{K}\right)$. Then $C = Q/V = \sigma A/V$.

#### With a Conducting Slab (Thickness $t < d$)

A conductor has $K \to \infty$, so $t/K \to 0$:

$$C = \frac{\epsilon_0 A}{d - t}$$

The conducting slab effectively reduces the gap. This makes sense — the field inside a conductor is zero, so the conducting region contributes zero to the voltage drop.

---

### Checkpoint 1: Direct Application

**Problem 1:** A parallel plate capacitor has plates of area $0.05$ m² separated by $1$ mm. Calculate its capacitance.

<details><summary><b>Solution</b></summary>

$C = \frac{\epsilon_0 A}{d} = \frac{8.85 \times 10^{-12} \times 0.05}{10^{-3}} = \frac{4.425 \times 10^{-13}}{10^{-3}}$

$C = \textbf{4.425 × 10⁻¹⁰ F = 0.4425 nF ≈ 442.5 pF}$
</details>

**Problem 2:** The same capacitor is connected to a $50$ V battery. How much charge is stored?

<details><summary><b>Solution</b></summary>

$Q = CV = 4.425 \times 10^{-10} \times 50 = \textbf{2.21 × 10⁻⁸ C = 22.1 nC}$
</details>

**Problem 3:** A mica slab ($K = 6$) of thickness $1$ mm (full gap) is inserted while the battery remains connected. Find the new capacitance and charge.

<details><summary><b>Solution</b></summary>

$C' = KC_0 = 6 \times 4.425 \times 10^{-10} = \textbf{2.655 × 10⁻⁹ F = 2.655 nF}$

Battery connected → $V = 50$ V (constant):

$Q' = C'V = 2.655 \times 10^{-9} \times 50 = \textbf{1.33 × 10⁻⁷ C = 133 nC}$

The charge increased by a factor of 6 (the battery pumped additional charge to maintain the voltage).
</details>

---

### Checkpoint 2: The Gauntlet — "The Capacitor Workshop"

*A student is building capacitors in the laboratory for different specifications.*

**Problem 1:** Design a parallel plate capacitor with $C = 1 \mu F$ using air as dielectric. If the plate separation is $1$ mm, what plate area is needed?

<details><summary><b>Solution</b></summary>

$A = \frac{Cd}{\epsilon_0} = \frac{10^{-6} \times 10^{-3}}{8.85 \times 10^{-12}} = \frac{10^{-9}}{8.85 \times 10^{-12}}$

$A = \textbf{113 m²}$

That's larger than a tennis court! This illustrates why practical capacitors use dielectrics (to multiply $C$ by $K$) and thin separations.
</details>

*The student decides to use a dielectric with $K = 100$ (like barium titanate ceramic).*

**Problem 2:** What plate area is needed now for $1 \mu F$?

<details><summary><b>Solution</b></summary>

$A = \frac{Cd}{K\epsilon_0} = \frac{113}{100} = \textbf{1.13 m²}$

Much more reasonable, though still large. Modern capacitors use even thinner dielectrics ($d \sim \mu m$) to achieve microfarad capacitances in tiny packages.
</details>

*She has a capacitor ($A = 200$ cm², $d = 4$ mm, air gap) and inserts a metal slab of thickness $2$ mm between the plates.*

**Problem 3:** What is the capacitance with the metal slab?

<details><summary><b>Solution</b></summary>

For a conducting slab of thickness $t$:

$C = \frac{\epsilon_0 A}{d - t} = \frac{8.85 \times 10^{-12} \times 200 \times 10^{-4}}{4 \times 10^{-3} - 2 \times 10^{-3}} = \frac{1.77 \times 10^{-13}}{2 \times 10^{-3}}$

$C = \textbf{8.85 × 10⁻¹¹ F = 88.5 pF}$

Without the slab: $C_0 = \frac{1.77 \times 10^{-13}}{4 \times 10^{-3}} = 44.25$ pF. The metal slab doubled the capacitance.
</details>

**Problem 4:** She replaces the metal slab with a glass slab ($K = 5$) of the same thickness ($2$ mm). What is the capacitance now?

<details><summary><b>Solution</b></summary>

Partial dielectric formula:

$C = \frac{\epsilon_0 A}{d - t + t/K} = \frac{1.77 \times 10^{-13}}{(4 - 2 + 2/5) \times 10^{-3}} = \frac{1.77 \times 10^{-13}}{2.4 \times 10^{-3}}$

$C = \textbf{7.375 × 10⁻¹¹ F = 73.75 pF}$

Between the air-only value (44.25 pF) and the metal-slab value (88.5 pF), as expected.
</details>

---

### Checkpoint 3: Multiple Dielectric Layers

**Problem 1:** A parallel plate capacitor ($A$, separation $d$) has two dielectric slabs placed between the plates: one of thickness $d/3$ with $K_1 = 2$ and another of thickness $2d/3$ with $K_2 = 5$. Find the effective capacitance.

<details><summary><b>Solution</b></summary>

This is equivalent to two capacitors in **series** (each slab is a separate capacitor sharing the same $Q$):

$C_1 = \frac{K_1 \epsilon_0 A}{d/3} = \frac{6\epsilon_0 A}{d}$

$C_2 = \frac{K_2 \epsilon_0 A}{2d/3} = \frac{15\epsilon_0 A}{2d}$

$\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} = \frac{d}{6\epsilon_0 A} + \frac{2d}{15\epsilon_0 A} = \frac{d}{\epsilon_0 A}\left(\frac{1}{6} + \frac{2}{15}\right) = \frac{d}{\epsilon_0 A} \times \frac{5 + 4}{30} = \frac{3d}{10\epsilon_0 A}$

$C = \textbf{\frac{10\epsilon_0 A}{3d}}$

Alternatively, using the partial dielectric formula: $C = \frac{\epsilon_0 A}{(d/3)/K_1 + (2d/3)/K_2} = \frac{\epsilon_0 A}{d/6 + 2d/15} = \frac{\epsilon_0 A}{3d/10} = \frac{10\epsilon_0 A}{3d}$ ✓
</details>

**Problem 2:** A capacitor has two dielectrics placed **side by side** (each covering half the plate area): $K_1 = 3$ (area $A/2$) and $K_2 = 6$ (area $A/2$), both spanning the full gap $d$. Find the effective capacitance.

<details><summary><b>Solution</b></summary>

Side by side → same $V$ across both → **parallel** combination:

$C_1 = \frac{K_1 \epsilon_0 (A/2)}{d} = \frac{3\epsilon_0 A}{2d}$

$C_2 = \frac{K_2 \epsilon_0 (A/2)}{d} = \frac{6\epsilon_0 A}{2d} = \frac{3\epsilon_0 A}{d}$

$C = C_1 + C_2 = \frac{3\epsilon_0 A}{2d} + \frac{3\epsilon_0 A}{d} = \frac{3\epsilon_0 A + 6\epsilon_0 A}{2d} = \textbf{\frac{9\epsilon_0 A}{2d}}$

Equivalent dielectric constant: $K_{eff} = \frac{C}{C_0} = \frac{9\epsilon_0 A/(2d)}{\epsilon_0 A/d} = 9/2 = 4.5$
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** A parallel plate capacitor has plate area $A = 0.02$ m² and plate separation $d = 4$ mm. It is connected to a $100$ V battery.

(a) Calculate $C_0$, $Q_0$, and $E_0$.  
(b) While the battery stays connected, a dielectric slab ($K = 4$, thickness $t = 3$ mm) is inserted between the plates. Find the new $C$, $Q$, $E$ in the dielectric, and $E$ in the remaining air gap.  
(c) What additional charge did the battery supply when the dielectric was inserted?

<details><summary><b>Solution</b></summary>

**(a)** 
$C_0 = \frac{\epsilon_0 A}{d} = \frac{8.85 \times 10^{-12} \times 0.02}{4 \times 10^{-3}} = \textbf{4.425 × 10⁻¹¹ F = 44.25 pF}$

$Q_0 = C_0 V = 44.25 \times 10^{-12} \times 100 = \textbf{4.425 × 10⁻⁹ C = 4.425 nC}$

$E_0 = V/d = 100/(4 \times 10^{-3}) = \textbf{25,000 V/m}$

**(b)** Battery connected → $V = 100$ V (constant).

$C = \frac{\epsilon_0 A}{d - t + t/K} = \frac{8.85 \times 10^{-12} \times 0.02}{(4 - 3 + 3/4) \times 10^{-3}} = \frac{1.77 \times 10^{-13}}{1.75 \times 10^{-3}}$

$C = \textbf{1.011 × 10⁻¹⁰ F = 101.1 pF}$

$Q = CV = 101.1 \times 10^{-12} \times 100 = \textbf{1.011 × 10⁻⁸ C = 10.11 nC}$

The surface charge density: $\sigma = Q/A = 10.11 \times 10^{-9}/(0.02) = 5.057 \times 10^{-7}$ C/m²

$E_{air} = \sigma/\epsilon_0 = 5.057 \times 10^{-7}/(8.85 \times 10^{-12}) = \textbf{57,143 V/m}$

$E_{dielectric} = E_{air}/K = 57143/4 = \textbf{14,286 V/m}$

Check: $V = E_{air}(d-t) + E_{dielectric} \times t = 57143 \times 10^{-3} + 14286 \times 3 \times 10^{-3} = 57.14 + 42.86 = 100$ V ✓

**(c)** Additional charge = $Q - Q_0 = 10.11 - 4.425 = \textbf{5.685 nC}$

The battery supplied this additional charge to maintain the constant voltage across the increased capacitance.
</details>

---

## Question Bank — Chapter 11

### Section A: MCQs (15 Questions)

**Q1.** The capacitance of a parallel plate capacitor is:

(a) $\epsilon_0 d/A$ &emsp; (b) $\epsilon_0 A/d$ &emsp; (c) $\epsilon_0 A d$ &emsp; (d) $A/(d\epsilon_0)$

<details><summary><b>Answer</b></summary>**(b)** $C = \epsilon_0 A/d$.</details>

---

**Q2.** Doubling the plate area of a parallel plate capacitor (all else constant) makes the capacitance:

(a) Halved &emsp; (b) Doubled &emsp; (c) Quadrupled &emsp; (d) Unchanged

<details><summary><b>Answer</b></summary>**(b)** $C \propto A$. Doubling $A$ doubles $C$.</details>

---

**Q3.** A parallel plate capacitor is charged to $V$. If the separation $d$ is doubled (battery disconnected), the new potential difference is:

(a) $V$ &emsp; (b) $V/2$ &emsp; (c) $2V$ &emsp; (d) $4V$

<details><summary><b>Answer</b></summary>**(c)** Battery off: $Q$ constant. $C' = \epsilon_0 A/(2d) = C/2$. $V' = Q/C' = 2Q/C = 2V$.</details>

---

**Q4.** The capacitance of an isolated conducting sphere of radius $R$ is:

(a) $kR$ &emsp; (b) $R/k$ &emsp; (c) $4\pi\epsilon_0 R$ &emsp; (d) $kR^2$

<details><summary><b>Answer</b></summary>**(c)** $C = Q/V = Q/(kQ/R) = R/k = 4\pi\epsilon_0 R$.</details>

---

**Q5.** A metal slab of thickness $t$ is inserted in a capacitor of gap $d$. The new capacitance is:

(a) $\epsilon_0 A/(d+t)$ &emsp; (b) $\epsilon_0 A/(d-t)$ &emsp; (c) $\epsilon_0 A/d$ &emsp; (d) $\epsilon_0 A/t$

<details><summary><b>Answer</b></summary>**(b)** $C = \epsilon_0 A/(d-t)$ since conducting slab contributes zero voltage drop.</details>

---

**Q6.** The SI unit of capacitance is:

(a) Volt &emsp; (b) Coulomb &emsp; (c) Farad &emsp; (d) Henry

<details><summary><b>Answer</b></summary>**(c)** Farad (F) = Coulomb/Volt.</details>

---

**Q7.** If a dielectric of $K = 3$ fills a capacitor ($C_0 = 4$ pF), the new capacitance is:

(a) $12$ pF &emsp; (b) $4/3$ pF &emsp; (c) $4$ pF &emsp; (d) $7$ pF

<details><summary><b>Answer</b></summary>**(a)** $C = KC_0 = 3\times4 = 12$ pF.</details>

---

**Q8.** Which of the following increases capacitance the most?

(a) Doubling $d$ &emsp; (b) Halving $A$ &emsp; (c) Filling with dielectric ($K = 10$) &emsp; (d) Removing the dielectric

<details><summary><b>Answer</b></summary>**(c)** Inserting dielectric $K = 10$ multiplies $C$ by 10. Others reduce or don't change $C$.</details>

---

**Q9.** For a parallel plate capacitor with a partial dielectric slab (thickness $t$, constant $K$), the effective gap is:

(a) $d - t + Kt$ &emsp; (b) $d - t + t/K$ &emsp; (c) $d + t/K$ &emsp; (d) $d - t(1-K)$

<details><summary><b>Answer</b></summary>**(b)** $C = \epsilon_0 A/(d - t + t/K)$, so effective gap $= d - t + t/K$.</details>

---

**Q10.** A $10$ pF capacitor is charged to $100$ V. The charge stored is:

(a) $1$ nC &emsp; (b) $10$ nC &emsp; (c) $100$ nC &emsp; (d) $1$ pC

<details><summary><b>Answer</b></summary>**(a)** $Q = CV = 10\times10^{-12}\times100 = 10^{-9}$ C $= 1$ nC.</details>

---

**Q11.** The energy per unit area stored in a parallel plate capacitor is:

(a) $\sigma^2/\epsilon_0$ &emsp; (b) $\sigma^2/(2\epsilon_0)$ &emsp; (c) $\sigma/\epsilon_0$ &emsp; (d) $\epsilon_0\sigma^2$

<details><summary><b>Answer</b></summary>**(b)** $U/A = \frac{1}{2}\epsilon_0 E^2 d = \frac{1}{2}\epsilon_0(\sigma/\epsilon_0)^2 d = \sigma^2 d/(2\epsilon_0)$. Per unit area: $\sigma^2/(2\epsilon_0)$... actually this gives energy per unit volume times $d$. The energy per unit area of plate is $\sigma^2 d/(2\epsilon_0) = Q^2d/(2\epsilon_0 A^2)$.</details>

---

**Q12.** A parallel plate capacitor with area $A$, gap $d$, charged to $V_0$. The surface charge density $\sigma$ is:

(a) $\sigma = \epsilon_0 V_0/d$ &emsp; (b) $\sigma = \epsilon_0 V_0 d$ &emsp; (c) $\sigma = V_0/(\epsilon_0 d)$ &emsp; (d) $\sigma = \epsilon_0 d/V_0$

<details><summary><b>Answer</b></summary>**(a)** $E = V_0/d = \sigma/\epsilon_0 \Rightarrow \sigma = \epsilon_0 V_0/d$.</details>

---

**Q13.** The capacitance of Earth (radius $6400$ km) is approximately:

(a) $711$ F &emsp; (b) $711$ mF &emsp; (c) $711\,\mu F$ &emsp; (d) $711$ pF

<details><summary><b>Answer</b></summary>**(c)** $C = 4\pi\epsilon_0 R = R/k = 6.4\times10^6/(9\times10^9) \approx 711\times10^{-6}$ F $= 711\,\mu F$.</details>

---

**Q14.** The charge distribution in a parallel plate capacitor (assuming infinite plates) is:

(a) Uniform on inner faces only &emsp; (b) Uniform on both inner and outer faces &emsp; (c) Non-uniform &emsp; (d) Zero

<details><summary><b>Answer</b></summary>**(a)** For ideal (infinite) parallel plates, charge concentrates only on the inner facing surfaces. (Edge effects cause some distribution on outer surfaces for real capacitors.)</details>

---

**Q15.** Two dielectric slabs of the same area fill the capacitor gap side-by-side (half area each). The effective constant $K_{eff}$ is:

(a) $(K_1 + K_2)/2$ &emsp; (b) $2K_1K_2/(K_1+K_2)$ &emsp; (c) $\sqrt{K_1K_2}$ &emsp; (d) $K_1K_2$

<details><summary><b>Answer</b></summary>**(a)** Side-by-side = parallel combination. $C = (K_1 + K_2)\epsilon_0 A/(2d) = K_{eff}\epsilon_0 A/d \Rightarrow K_{eff} = (K_1+K_2)/2$.</details>

---

### Section B: Short Answer Questions (Q16–Q22)

**Q16.** Derive the formula $C = \epsilon_0 A/d$ for a parallel plate capacitor from first principles.

<details><summary><b>Answer</b></summary>

1. Surface charge density: $\sigma = Q/A$
2. Electric field (Gauss's Law, infinite plate): $E = \sigma/\epsilon_0 = Q/(\epsilon_0 A)$
3. Potential difference: $V = Ed = Qd/(\epsilon_0 A)$
4. Capacitance: $C = Q/V = Q\epsilon_0 A/(Qd) = \epsilon_0 A/d$ ✓
</details>

---

**Q17.** A parallel plate capacitor ($A = 0.04$ m², $d = 2$ mm) has a dielectric slab ($K = 5$, $t = 1.5$ mm). Find $C$.

<details><summary><b>Answer</b></summary>

$C = \frac{\epsilon_0 A}{d-t+t/K} = \frac{8.85\times10^{-12}\times0.04}{(2-1.5+1.5/5)\times10^{-3}} = \frac{3.54\times10^{-13}}{0.8\times10^{-3}} = \mathbf{4.425\times10^{-10}\,F = 442.5\,pF}$
</details>

---

**Q18.** Calculate $C_0$ (air gap) and $C'$ (with $K=4$ dielectric) for: $A = 100$ cm², $d = 1$ mm.

<details><summary><b>Answer</b></summary>

$C_0 = \epsilon_0 A/d = 8.85\times10^{-12}\times0.01/10^{-3} = 88.5\times10^{-12}$ F $= 88.5$ pF

$C' = KC_0 = 4\times88.5 = \mathbf{354\,pF}$
</details>

---

**Q19.** For two parallel plate capacitors of equal area: $C_1$ (gap $d$, air) and $C_2$ (gap $d$, dielectric $K$). Compare their surface charge densities when both are connected to the same battery.

<details><summary><b>Answer</b></summary>

Both at same voltage $V$: $\sigma_1 = \epsilon_0 V/d$ (air), $\sigma_2 = K\epsilon_0 V/d$ (dielectric)

$\sigma_2/\sigma_1 = K$. The capacitor with dielectric stores $K$ times more charge per unit area.
</details>

---

**Q20.** A student says "A 1 Farad capacitor is the world's largest capacitor." Is this correct?

<details><summary><b>Answer</b></summary>

Not anymore. 1 Farad was once impractically large. Modern **supercapacitors** (also called ultracapacitors or electric double-layer capacitors) routinely achieve **1 F, 10 F, 100 F, even 3000 F** in small packages.

They work by using nanoscale electrode separation (a few angstroms between ions and electrode surface) and enormous effective surface areas (activated carbon with $\sim 1000$ m² per gram). This makes $C = \epsilon A/d$ astronomically large even with small $A$ per gram.

A 1 Farad supercapacitor today fits in your hand.
</details>

---

**Q21.** Show that the electric field between the plates of a parallel plate capacitor can be written as $E = Q/(\epsilon_0 A)$, and derive the expression for voltage.

<details><summary><b>Answer</b></summary>

By Gauss's Law (Gaussian cylinder through one plate, area $A$):

$\Phi = EA = Q_{enc}/\epsilon_0 = \sigma A/\epsilon_0 = Q/\epsilon_0$

$E = Q/(\epsilon_0 A)$ ✓

Voltage: $V = Ed = Qd/(\epsilon_0 A)$

This confirms $C = Q/V = \epsilon_0 A/d$.
</details>

---

**Q22.** A capacitor is charged to $V_0$ with a battery and then disconnected. The plate separation is then tripled. What happens to $E$ and $V$?

<details><summary><b>Answer</b></summary>

Battery disconnected → $Q$ constant.

$E = \sigma/\epsilon_0 = Q/(\epsilon_0 A)$ — **unchanged** (doesn't depend on $d$!)

$V = Ed' = E\times3d = 3Ed = 3V_0$ — **tripled**

$C' = \epsilon_0 A/(3d) = C/3$ → $V' = Q/C' = 3Q/C = 3V_0$ ✓

The electric field stays the same but the potential difference triples because the plates are further apart.
</details>

---

### Section C: Long Answer / JEE-Level (Q23–Q30)

**Q23.** A parallel plate capacitor ($A = 0.02$ m², $d = 4$ mm) has a $1$ mm glass slab ($K = 5$) and a $1$ mm air gap remaining on each side. Battery provides $200$ V. Find $C$, $Q$, $E$ in glass, $E$ in air.

<details><summary><b>Answer</b></summary>

$C = \epsilon_0 A/(d-t+t/K) = 8.85\times10^{-12}\times0.02/(4-1+1/5)\times10^{-3}$
$= 1.77\times10^{-13}/(3.2\times10^{-3}) = 5.53\times10^{-11}$ F

$Q = CV = 5.53\times10^{-11}\times200 = 1.106\times10^{-8}$ C

$\sigma = Q/A = 1.106\times10^{-8}/0.02 = 5.53\times10^{-7}$ C/m²

$E_{air} = \sigma/\epsilon_0 = 5.53\times10^{-7}/(8.85\times10^{-12}) = 6.25\times10^4$ V/m

$E_{glass} = E_{air}/K = 6.25\times10^4/5 = \mathbf{1.25\times10^4\,V/m}$
</details>

---

**Q24.** Three conducting plates each of area $A$ are arranged: plate 1, gap $d_1$, plate 2, gap $d_2$, plate 3. Find the equivalent capacitance between outer plates, treating inner plate as common electrode.

<details><summary><b>Answer</b></summary>

The arrangement is equivalent to two capacitors in parallel (both with plate 2 as a common electrode):

$C_1 = \epsilon_0 A/d_1$, $C_2 = \epsilon_0 A/d_2$

$C_{eq} = C_1 + C_2 = \epsilon_0 A(1/d_1 + 1/d_2) = \epsilon_0 A(d_1+d_2)/(d_1 d_2)$
</details>

---

**Q25–Q30.** Numerical problems on capacitance.

**Q25.** A $50$ pF capacitor needs to store $1\,\mu J$ energy. Find the required voltage.

<details><summary><b>Answer</b></summary>

$V = \sqrt{2U/C} = \sqrt{2\times10^{-6}/(50\times10^{-12})} = \sqrt{4\times10^4} = \mathbf{200\,V}$
</details>

---

**Q26.** At what plate area would a parallel plate air capacitor (separation $1$ mm) have the same capacitance as Earth ($711\,\mu F$)?

<details><summary><b>Answer</b></summary>

$A = Cd/\epsilon_0 = 711\times10^{-6}\times10^{-3}/(8.85\times10^{-12}) = 711\times10^{-9}/(8.85\times10^{-12}) = 80{,}339$ m²

≈ **8 hectares** — the area of about 11 football fields!
</details>

---

**Q27.** A capacitor is charged and the battery disconnected. A metal slab of thickness $d/3$ is inserted. By what factor does the capacitance change? What happens to energy?

<details><summary><b>Answer</b></summary>

$C' = \epsilon_0 A/(d-d/3) = \epsilon_0 A/(2d/3) = 3C_0/2$

$C$ increases by factor $3/2$.

$U' = Q^2/(2C') = Q^2/(2\times3C_0/2) = Q^2/(3C_0) = 2U_0/3$

Energy decreases to $2/3$ of original.
</details>

---

**Q28.** The capacitance of a capacitor is $8$ pF when filled with a dielectric of $K = 4$. What is the capacitance with: (a) $K = 2$ dielectric, (b) air, (c) another dielectric of $K = 8$?

<details><summary><b>Answer</b></summary>

$C_0 = C/K = 8/4 = 2$ pF (air capacitance)

**(a)** $K = 2$: $C = 2\times2 = \mathbf{4\,pF}$

**(b)** Air: $C = C_0 = \mathbf{2\,pF}$

**(c)** $K = 8$: $C = 8\times2 = \mathbf{16\,pF}$
</details>

---

**Q29.** A $20$ pF capacitor is charged to $500$ V. Find: (a) charge, (b) energy, (c) energy density if plate area is $0.1$ m² and gap $1.5$ mm.

<details><summary><b>Answer</b></summary>

**(a)** $Q = CV = 20\times10^{-12}\times500 = 10^{-8}$ C $= \mathbf{10\,nC}$

**(b)** $U = \frac{1}{2}CV^2 = \frac{1}{2}\times20\times10^{-12}\times2.5\times10^5 = \mathbf{2.5\,\mu J}$

**(c)** $E = V/d = 500/1.5\times10^{-3} = 3.33\times10^5$ V/m

$u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2}\times8.85\times10^{-12}\times(3.33\times10^5)^2 = \mathbf{0.491\,J/m^3}$

Check: $U = u\times Ad = 0.491\times0.1\times1.5\times10^{-3} = 7.36\times10^{-5}\,J$... (discrepancy because $C_0 = \epsilon_0 A/d = 8.85\times10^{-12}\times0.1/1.5\times10^{-3} = 5.9\,pF \neq 20\,pF$; the 20 pF likely includes a dielectric)
</details>

---

**Q30.** A cylindrical capacitor has inner radius $a$, outer radius $b$, length $L$. Its capacitance is $C = 2\pi\epsilon_0 L/\ln(b/a)$. For $a = 1$ cm, $b = 2$ cm, $L = 0.5$ m, find $C$.

<details><summary><b>Answer</b></summary>

$C = 2\pi\epsilon_0 L/\ln(b/a) = 2\pi\times8.85\times10^{-12}\times0.5/\ln(2)$

$= 2\pi\times4.425\times10^{-12}/0.693 = 5.56\times10^{-11}/0.693$

$= \mathbf{8.02\times10^{-11}\,F = 80.2\,pF}$
</details>

---

*Next: [Chapter 12 — Combination of Capacitors →](./12_combination_of_capacitors.md)*
