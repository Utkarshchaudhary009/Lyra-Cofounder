# Chapter 10: Dielectrics and Polarisation

> *NCERT Section 2.10*

---

### The Story of the Stubborn Insulator

Conductors are like crowds of free citizens — when an electric field arrives, the charges move freely across the entire body of the conductor, redistributing to cancel the field inside. But what about insulators — materials like glass, rubber, plastic, or pure water?<br> In these materials, there are **no free charges**. Every electron is bound tightly to its parent atom. They cannot migrate.

So when you place a piece of glass in an electric field, does nothing happen?<br>

Far from it. Something far more subtle occurs. The electrons cannot leave their atoms, but they can *shift* — slightly. Every atom in the material becomes a tiny electric dipole. The positive nucleus stays roughly in place, but the electron cloud is tugged slightly in the opposite direction to the field. Billions of atoms, all doing this simultaneously, create a macroscopic effect: the material **polarises**.

This polarisation partially *cancels* the external field inside the material — not completely (unlike a conductor), but partially. The degree of cancellation is characterised by a single number: the **dielectric constant** $K$.

---

### Building the Concept

#### Polar vs. Non-Polar Dielectrics

| Type | Example | Molecular Structure | In External Field |
|------|---------|:-------------------:|:-----------------:|
| **Non-polar** | $N_2$, $O_2$, $CH_4$, diamond | Symmetric; no permanent dipole | Atoms stretch → induced dipoles |
| **Polar** | $H_2O$, $HCl$, $NH_3$ | Asymmetric; permanent dipole | Dipoles partially align with field |

In *both* cases, the net effect is the same: the material develops a net dipole moment per unit volume, called the **Polarisation** $\vec{P}$.

#### The Mechanism of Polarisation

When a dielectric slab is placed in a uniform external field $\vec{E}_0$:

1. Internal dipoles align (partially) with the field.
2. The net effect is the appearance of **bound surface charges** on the two faces of the slab — positive charges on the face where $\vec{E}_0$ exits, negative charges on the face where it enters.
3. These bound surface charges create their own electric field inside the dielectric, directed **opposite** to $\vec{E}_0$.
4. The total field inside the dielectric is reduced:

$$\vec{E}_{inside} = \vec{E}_0 - \vec{E}_{polarisation}$$

#### The Dielectric Constant $K$

The ratio of the external field to the reduced field inside the dielectric is called the **dielectric constant** (or relative permittivity):

$$\boxed{K = \frac{E_0}{E_{inside}} = \frac{V_0}{V_{inside}}}$$

Since $E_{inside} < E_0$ always, $K > 1$ always.

| Material | Dielectric Constant $K$ |
|----------|:----:|
| Vacuum | $1$ (by definition) |
| Air | $1.00054$ (≈ 1) |
| Paper | $3.7$ |
| Glass | $5–10$ |
| Mica | $6$ |
| Water | $80$ |
| Titanium dioxide | $100$ |
| Conductor (perfect) | $\infty$ |

> **Water's extreme $K$:** Water molecules are strongly polar. In an external field, they align vigorously, creating a massive counter-field. This is why water is such an effective solvent for ionic compounds — it weakens the electrostatic attraction between ions by a factor of 80.

#### The Permittivity

We can rewrite all electrostatic formulas for media by replacing $\epsilon_0$ with $\epsilon = K\epsilon_0$:

$$\epsilon = K\epsilon_0$$

Coulomb's law in a medium: $F = \frac{1}{4\pi\epsilon} \frac{q_1 q_2}{r^2} = \frac{1}{4\pi K\epsilon_0} \frac{q_1 q_2}{r^2}$

The force is **reduced** by a factor of $K$ inside a dielectric.

---

### Checkpoint 1: Conceptual Understanding

**Problem 1:** A parallel plate capacitor has air between its plates and an electric field of $3 \times 10^4$ V/m. If a glass slab ($K = 5$) is inserted between the plates, what is the new electric field inside the glass?<br>

<details><summary><b>Solution</b></summary>

$E_{glass} = \frac{E_0}{K} = \frac{3 \times 10^4}{5} = \textbf{6000 V/m}$

The field is reduced by a factor of 5 inside the glass.
</details>

**Problem 2:** Two point charges of $+2\mu C$ each are held $10$ cm apart in vacuum. What is the force between them?<br> If the same charges are placed $10$ cm apart inside water ($K = 80$), what is the new force?<br>

<details><summary><b>Solution</b></summary>

In vacuum: $F_0 = \frac{kq^2}{r^2} = \frac{9 \times 10^9 \times (2 \times 10^{-6})^2}{(0.1)^2} = \frac{9 \times 10^9 \times 4 \times 10^{-12}}{0.01} = \textbf{3.6 N}$

In water: $F = \frac{F_0}{K} = \frac{3.6}{80} = \textbf{0.045 N}$

The electrostatic force is 80 times weaker in water. This is why NaCl dissolves in water but not in oil ($K \approx 2$) — water weakens the ionic bond enough for thermal energy to pull the ions apart.
</details>

**Problem 3:** Is it correct to say that a dielectric "blocks" the electric field?<br> Why or why not?<br>

<details><summary><b>Solution</b></summary>

**No.** A dielectric does not block the field — it *reduces* it. The field still penetrates the dielectric, just with reduced strength ($E/K$). Only a conductor ($K \to \infty$) reduces the internal field to exactly zero.

A more accurate statement: "A dielectric partially screens the electric field by developing a counter-field through polarisation."
</details>

---

### Checkpoint 2: The Gauntlet — "The Dielectric Slab"

*An engineer is testing the effect of different dielectric materials in a parallel plate capacitor. The plates are separated by $5$ mm, and a potential difference of $100$ V is applied across them.*

**Problem 1:** What is the electric field between the plates (without any dielectric)?<br>

<details><summary><b>Solution</b></summary>

$E_0 = \frac{V}{d} = \frac{100}{5 \times 10^{-3}} = \textbf{20,000 V/m = 20 kV/m}$
</details>

*She inserts a mica slab ($K = 6$) that completely fills the gap between the plates. The battery remains connected.*

**Problem 2:** What is the electric field inside the mica?<br>

<details><summary><b>Solution</b></summary>

Since the battery remains connected, the **voltage across the plates remains $100$ V** (the battery maintains it).

$E = \frac{V}{d} = \frac{100}{5 \times 10^{-3}} = \textbf{20,000 V/m}$

Wait — the field does NOT change when the battery stays connected! The battery pumps additional charge onto the plates to maintain the same voltage (and hence the same field).

This is a critical distinction:
- **Battery connected:** $V$ stays constant; $E$ stays constant; $Q$ increases.
- **Battery disconnected:** $Q$ stays constant; $E$ decreases (by factor $K$); $V$ decreases.
</details>

*She now disconnects the battery and then inserts a fresh mica slab ($K = 6$).*

**Problem 3:** What is the electric field inside the mica now?<br>

<details><summary><b>Solution</b></summary>

Battery disconnected → charge $Q$ on the plates is constant.

$E = \frac{E_0}{K} = \frac{20000}{6} = \textbf{3333 V/m}$

The field is reduced by a factor of 6.
</details>

**Problem 4:** What is the new voltage across the plates?<br>

<details><summary><b>Solution</b></summary>

$V = Ed = 3333 \times 5 \times 10^{-3} = \textbf{16.67 V}$

The voltage dropped from 100 V to 16.67 V. The "missing" voltage is being used to maintain the polarisation of the dielectric.
</details>

---

### Summary: Battery Connected vs. Battery Disconnected

| Quantity | Dielectric Inserted (Battery ON) | Dielectric Inserted (Battery OFF) |
|----------|:--:|:--:|
| Voltage $V$ | Constant ($V_0$) | Decreases ($V_0/K$) |
| Charge $Q$ | Increases ($KQ_0$) | Constant ($Q_0$) |
| Electric Field $E$ | Constant ($E_0$) | Decreases ($E_0/K$) |
| Capacitance $C$ | Increases ($KC_0$) | Increases ($KC_0$) |
| Energy $U$ | Increases ($KU_0$) | Decreases ($U_0/K$) |

> **This table is gold for JEE.** At least one question per paper involves inserting/removing a dielectric with the battery on or off. Master this distinction.

---

### The Culmination: Synthesis

**Synthesis Problem:** A parallel plate capacitor with plate area $A = 100$ cm² and separation $d = 2$ mm is charged by a $200$ V battery and then disconnected.

(a) Find the initial charge, field, and energy.  
(b) A dielectric slab of $K = 4$ and thickness $2$ mm (full gap) is inserted. Find the new charge, field, voltage, and energy.  
(c) Where did the "missing" energy go?<br>

<details><summary><b>Solution</b></summary>

**(a)** 
$C_0 = \frac{\epsilon_0 A}{d} = \frac{8.85 \times 10^{-12} \times 100 \times 10^{-4}}{2 \times 10^{-3}} = \frac{8.85 \times 10^{-14}}{2 \times 10^{-3}} = 4.425 \times 10^{-11}$ F

$Q_0 = C_0 V_0 = 4.425 \times 10^{-11} \times 200 = 8.85 \times 10^{-9}$ C $= \textbf{8.85 nC}$

$E_0 = V_0/d = 200/(2 \times 10^{-3}) = \textbf{10⁵ V/m}$

$U_0 = \frac{1}{2}C_0 V_0^2 = \frac{1}{2} \times 4.425 \times 10^{-11} \times (200)^2 = \textbf{8.85 × 10⁻⁷ J = 0.885 μJ}$

**(b)** Battery disconnected → $Q$ is constant.

$Q = Q_0 = \textbf{8.85 nC}$ (unchanged)

$C = KC_0 = 4 \times 4.425 \times 10^{-11} = 17.7 \times 10^{-11}$ F

$V = Q/C = 8.85 \times 10^{-9}/(17.7 \times 10^{-11}) = \textbf{50 V}$ (reduced by factor $K = 4$)

$E = V/d = 50/(2 \times 10^{-3}) = \textbf{2.5 × 10⁴ V/m}$ (reduced by factor $K$)

$U = \frac{Q^2}{2C} = \frac{(8.85 \times 10^{-9})^2}{2 \times 17.7 \times 10^{-11}} = \frac{78.3 \times 10^{-18}}{35.4 \times 10^{-11}} = \textbf{2.21 × 10⁻⁷ J = 0.221 μJ}$

Energy reduced by factor $K$: $U = U_0/K = 0.885/4 = 0.221$ μJ ✓

**(c)** The "missing" energy ($0.885 - 0.221 = 0.664$ μJ) was spent as **work done by the electric field in pulling the dielectric slab into the gap**. As the dielectric is inserted, the fringing field at the edges exerts a force that *pulls* the slab in. This kinetic energy is ultimately dissipated as heat within the dielectric.
</details>

---

## Question Bank — Chapter 10

### Section A: MCQs (15 Questions)

**Q1.** When a dielectric is inserted between capacitor plates (battery disconnected), the electric field:

(a) Increases &emsp; (b) Decreases by factor $K$ &emsp; (c) Remains same &emsp; (d) Doubles

<details><summary><b>Answer</b></summary>**(b)** Battery disconnected → $Q$ constant. $E = \sigma/\epsilon_0$ stays if $Q$ is constant?<br> No — $E_{inside} = E_0/K$ in the dielectric. So $E$ decreases by $K$.</details>

---

**Q2.** The dielectric constant $K$ of a conductor is:

(a) $0$ &emsp; (b) $1$ &emsp; (c) $\infty$ &emsp; (d) $-1$

<details><summary><b>Answer</b></summary>**(c)** A conductor reduces the internal field to zero: $E = E_0/K = 0 \Rightarrow K \to \infty$.</details>

---

**Q3.** The permittivity of a medium with dielectric constant $K$ is:

(a) $K/\epsilon_0$ &emsp; (b) $K+\epsilon_0$ &emsp; (c) $K\epsilon_0$ &emsp; (d) $\epsilon_0/K$

<details><summary><b>Answer</b></summary>**(c)** $\epsilon = K\epsilon_0$.</details>

---

**Q4.** A dielectric slab is inserted between capacitor plates (battery connected). The capacitance:

(a) Decreases &emsp; (b) Increases by $K$ &emsp; (c) Remains same &emsp; (d) Doubles only

<details><summary><b>Answer</b></summary>**(b)** $C = KC_0$ regardless of battery connection.</details>

---

**Q5.** Coulomb's force between two charges in a dielectric medium (constant $K$) compared to vacuum is:

(a) $K$ times larger &emsp; (b) $K$ times smaller &emsp; (c) $K^2$ times smaller &emsp; (d) Same

<details><summary><b>Answer</b></summary>**(b)** $F = F_0/K$ in a medium with dielectric constant $K$.</details>

---

**Q6.** Polar dielectrics, unlike non-polar, have:

(a) No permanent dipole moment &emsp; (b) Permanent dipole moments that align in a field &emsp; (c) No polarisation &emsp; (d) Fixed charges only

<details><summary><b>Answer</b></summary>**(b)** Polar molecules (like $H_2O$) have permanent dipoles that partially align with an applied field, giving a larger $K$.</details>

---

**Q7.** When a dielectric fills a capacitor and the battery remains connected, the energy stored:

(a) Decreases by $K$ &emsp; (b) Remains same &emsp; (c) Increases by $K$ &emsp; (d) Decreases by $K^2$

<details><summary><b>Answer</b></summary>**(c)** Battery ON: $V$ constant, $C' = KC$. $U = \frac{1}{2}C'V^2 = K\times\frac{1}{2}CV^2 = KU_0$. Energy increases.</details>

---

**Q8.** The bound surface charge density on a dielectric slab due to polarisation is:

(a) $\sigma_b = P$ &emsp; (b) $\sigma_b = P\sin\theta$ &emsp; (c) $\sigma_b = P\cos\theta$ &emsp; (d) $\sigma_b = P/K$

<details><summary><b>Answer</b></summary>**(c)** $\sigma_b = \vec{P}\cdot\hat{n} = P\cos\theta$ where $\theta$ is between $\vec{P}$ and the outward normal.</details>

---

**Q9.** When a dielectric is inserted with battery disconnected, energy stored:

(a) Increases by $K$ &emsp; (b) Remains same &emsp; (c) Decreases by $K$ &emsp; (d) Doubles

<details><summary><b>Answer</b></summary>**(c)** Battery OFF: $Q$ constant. $U = Q^2/(2C') = Q^2/(2KC) = U_0/K$. Energy decreases.</details>

---

**Q10.** The electric susceptibility $\chi_e$ of a dielectric is related to $K$ by:

(a) $K = \chi_e$ &emsp; (b) $K = 1 + \chi_e$ &emsp; (c) $K = 1 - \chi_e$ &emsp; (d) $K = \chi_e - 1$

<details><summary><b>Answer</b></summary>**(b)** $K = 1 + \chi_e$ where $\chi_e$ is the electric susceptibility.</details>

---

**Q11.** The dielectric constant of vacuum is:

(a) $0$ &emsp; (b) $\infty$ &emsp; (c) $1$ &emsp; (d) $8.85\times10^{-12}$

<details><summary><b>Answer</b></summary>**(c)** By definition, $K_{vacuum} = 1$.</details>

---

**Q12.** Two charges are $10$ cm apart in water ($K = 80$). Compared to the same charges in air, the force is:

(a) $80\times$ larger &emsp; (b) $80\times$ smaller &emsp; (c) Same &emsp; (d) $\sqrt{80}$ times smaller

<details><summary><b>Answer</b></summary>**(b)** $F_{water} = F_{air}/K = F_{air}/80$.</details>

---

**Q13.** The polarisation $\vec{P}$ of a dielectric medium represents:

(a) Total charge in the medium &emsp; (b) Dipole moment per unit volume &emsp; (c) Surface charge density &emsp; (d) Electric permittivity

<details><summary><b>Answer</b></summary>**(b)** $\vec{P}$ is the net electric dipole moment per unit volume of the dielectric.</details>

---

**Q14.** When battery is ON and dielectric ($K = 5$) is fully inserted, the charge on the capacitor:

(a) Decreases 5 times &emsp; (b) Increases 5 times &emsp; (c) Remains same &emsp; (d) Doubles

<details><summary><b>Answer</b></summary>**(b)** $Q = C'V = KCV = 5Q_0$. Charge increases 5-fold with battery connected.</details>

---

**Q15.** Dielectric breakdown occurs when:

(a) Temperature rises &emsp; (b) Applied field exceeds dielectric strength &emsp; (c) Capacitor is fully charged &emsp; (d) Frequency is too high

<details><summary><b>Answer</b></summary>**(b)** When the applied field $E > E_{breakdown}$ (dielectric strength), the insulating bonds break and the material becomes conducting.</details>

---

### Section B: Short Answer Questions

**Q16.** Distinguish between polar and non-polar dielectrics with examples. Which has a larger dielectric constant?<br>

<details><summary><b>Answer</b></summary>

**Non-polar:** Molecules have symmetric charge distribution; no permanent dipole. In a field, induced dipoles form. Examples: $N_2$, $O_2$, $CH_4$, diamond. Typical $K \approx 1-4$.

**Polar:** Molecules have asymmetric charge distribution; permanent dipoles exist. In a field, dipoles partially align. Examples: $H_2O$, $HCl$, $NH_3$. Typical $K \approx 10-80$.

**Larger $K$:** Polar dielectrics generally have larger $K$ because both induced AND permanent dipoles contribute to polarisation.
</details>

---

**Q17.** A parallel plate capacitor has $C = 10$ pF with air. A mica slab ($K = 6$) fills the gap. Find the new $C$, and find what happens to $Q$, $E$, $V$ when (a) battery stays connected, (b) battery is disconnected before insertion.

<details><summary><b>Answer</b></summary>

$C' = KC = 6\times10 = 60$ pF (same in both cases)

**(a) Battery connected** ($V = $ const):
- $Q' = C'V = 6Q_0$ ↑ (increases)
- $E' = V/d = E_0$ (unchanged)
- $V' = V_0$ (unchanged)

**(b) Battery disconnected** ($Q = $ const):
- $Q' = Q_0$ (unchanged)
- $E' = E_0/K = E_0/6$ ↓ (decreases)
- $V' = V_0/K = V_0/6$ ↓ (decreases)
</details>

---

**Q18.** The dielectric strength of air is $3\times10^6$ V/m. Calculate the maximum charge that can be stored on a conducting sphere of radius $10$ cm in air.

<details><summary><b>Answer</b></summary>

$E_{max} = kQ_{max}/R^2 \Rightarrow Q_{max} = E_{max}R^2/k = 3\times10^6\times(0.1)^2/(9\times10^9)$

$Q_{max} = 3\times10^4/(9\times10^9) = \mathbf{3.33\times10^{-6}\,C = 3.33\,\mu C}$
</details>

---

**Q19.** Explain why water ($K = 80$) is such a good solvent for ionic compounds.

<details><summary><b>Answer</b></summary>

Ionic compounds like NaCl are held together by strong electrostatic forces: $F = ke^2/r^2$.

In water, this force becomes $F_{water} = ke^2/(Kr^2) = F_{vacuum}/80$.

The Coulomb attraction between $Na^+$ and $Cl^-$ is reduced by a factor of 80. This weakening allows the thermal energy of water molecules ($kT \approx 0.025$ eV) to pull the ions apart, dissolving the crystal.

In oil ($K \approx 2$), the ionic bond is only halved — still far too strong for thermal energy to break. So NaCl doesn't dissolve in oil.
</details>

---

**Q20.** A capacitor has plate area $200$ cm², separation $4$ mm. A dielectric slab ($K = 5$, thickness $2$ mm) is inserted. Find $C$.

<details><summary><b>Answer</b></summary>

$C = \frac{\epsilon_0 A}{d-t+t/K} = \frac{8.85\times10^{-12}\times0.02}{(4-2+2/5)\times10^{-3}} = \frac{1.77\times10^{-13}}{2.4\times10^{-3}} = \mathbf{7.375\times10^{-11}\,F = 73.75\,pF}$
</details>

---

**Q21.** Define dielectric constant. Show that $K = C/C_0$ where $C_0$ is capacitance without dielectric.

<details><summary><b>Answer</b></summary>

**Dielectric constant $K$:** Ratio of Coulomb force in vacuum to Coulomb force in medium: $K = F_{vacuum}/F_{medium}$. Equivalently, $K = E_0/E_{medium}$.

**Proof $K = C/C_0$:**

Without dielectric: $C_0 = \epsilon_0 A/d$, $V_0 = Q/C_0$

With dielectric: Field reduced to $E = E_0/K$. New voltage $V = Ed = E_0d/K = V_0/K$.

$C = Q/V = Q/(V_0/K) = KQ/V_0 = KC_0$

$\therefore K = C/C_0$ ✓
</details>

---

**Q22.** A capacitor of $5\,\mu F$ is charged to $100$ V. Battery disconnected, then a dielectric of $K = 4$ is inserted. Find the energy before and after and account for the difference.

<details><summary><b>Answer</b></summary>

$U_i = \frac{1}{2}CV^2 = \frac{1}{2}\times5\times10^{-6}\times10^4 = 0.025$ J $= 25$ mJ

After: $Q$ unchanged, $C' = 4C = 20\,\mu F$

$U_f = Q^2/(2C') = (C_0V_0)^2/(2KC_0) = C_0V_0^2/(2K) = U_i/K = 25/4 = \mathbf{6.25\,mJ}$

Energy lost = $25 - 6.25 = 18.75$ mJ. This energy went as work done by the electric field pulling the dielectric slab into the gap.
</details>

---

### Section C: Long Answer / JEE-Level

**Q23.** A capacitor (plate area $A$, gap $d$, air) is charged to $V_0$ by battery, then disconnected. A conductor slab of thickness $d/2$ is inserted. Find new $C$, $V$, $E$, $U$.

<details><summary><b>Answer</b></summary>

Conducting slab: $K \to \infty$. $C = \epsilon_0 A/(d-t) = \epsilon_0 A/(d-d/2) = 2\epsilon_0 A/d = 2C_0$

$Q$ unchanged (battery disconnected). $V = Q/C' = Q/(2C_0) = V_0/2$

$E = V/(d-t) = (V_0/2)/(d/2) = V_0/d = E_0$ (field in the remaining air gap is unchanged!)

$U = Q^2/(2C') = Q^2/(4C_0) = U_0/2$ (energy halved)
</details>

---

**Q24.** Compare the effect of inserting a dielectric in a charged capacitor with and without the battery, summarizing all changes in $C$, $Q$, $E$, $V$, $U$.

<details><summary><b>Answer</b></summary>

| Quantity | Battery ON | Battery OFF |
|----------|:----------:|:-----------:|
| $C$ | $KC_0$ | $KC_0$ |
| $Q$ | $KQ_0$ | $Q_0$ |
| $V$ | $V_0$ | $V_0/K$ |
| $E$ | $E_0$ | $E_0/K$ |
| $U$ | $KU_0$ | $U_0/K$ |
</details>

---

**Q25.** Two dielectric slabs of thicknesses $d_1$ and $d_2$ ($d_1+d_2 = d$) with constants $K_1$ and $K_2$ fill a capacitor. Derive the equivalent capacitance.

<details><summary><b>Answer</b></summary>

Each slab is a capacitor in series (same charge $Q$, voltages add):

$C_1 = K_1\epsilon_0 A/d_1$, $C_2 = K_2\epsilon_0 A/d_2$

$\frac{1}{C} = \frac{1}{C_1}+\frac{1}{C_2} = \frac{d_1}{K_1\epsilon_0 A}+\frac{d_2}{K_2\epsilon_0 A} = \frac{1}{\epsilon_0 A}\left(\frac{d_1}{K_1}+\frac{d_2}{K_2}\right)$

$C = \frac{\epsilon_0 A}{\frac{d_1}{K_1}+\frac{d_2}{K_2}} = \frac{K_1K_2\epsilon_0 A}{K_2d_1+K_1d_2}$
</details>

---

**Q26.** A parallel plate capacitor ($C_0 = 10$ pF, $d = 2$ mm) has a $K=4$ dielectric inserted (battery connected at $V = 100$ V). Find the polarisation $P$ in the dielectric.

<details><summary><b>Answer</b></summary>

$E = V/d = 100/(2\times10^{-3}) = 5\times10^4$ V/m (unchanged with battery connected)

$P = \epsilon_0(K-1)E = 8.85\times10^{-12}\times3\times5\times10^4 = 8.85\times10^{-12}\times1.5\times10^5 = \mathbf{1.33\times10^{-6}\,C/m^2}$
</details>

---

**Q27.** Explain with diagrams: (a) non-polar molecule in external field, (b) polar molecule alignment in field.

<details><summary><b>Answer</b></summary>

**(a) Non-polar molecule (e.g., $O_2$):**
Without field: charge centers coincide → $\vec{p} = 0$.
With field $\vec{E}_0$: electron cloud shifts opposite to $\vec{E}$, nucleus shifts along $\vec{E}$ → small induced dipole $\vec{p}_{ind}$ parallel to $\vec{E}$. Polarisation: $P = n\alpha E$ where $n$ = number density, $\alpha$ = polarisability.

**(b) Polar molecule (e.g., $H_2O$):**
Without field: permanent dipoles randomly oriented → net $P = 0$.
With field: dipoles experience torque $\tau = pE\sin\theta$, tending to align with field. Thermal agitation prevents complete alignment. Net polarisation $P$ is proportional to $E/T$ (Curie's law for polar dielectrics).

Both effects produce bound surface charges that partially screen the external field, giving $E_{internal} = E_0/K$.
</details>

---

**Q28.** Derive the relation $E = E_0/K$ for a dielectric slab fully filling a capacitor.

<details><summary><b>Answer</b></summary>

External field: $E_0 = \sigma_f/\epsilon_0$ (due to free charges $\sigma_f$ on plates).

Dielectric polarises: bound charges $\sigma_b$ appear on surfaces. Inside dielectric:

$E = (E_0 - E_{polarisation}) = \frac{\sigma_f}{\epsilon_0} - \frac{\sigma_b}{\epsilon_0} = \frac{\sigma_f - \sigma_b}{\epsilon_0}$

But by definition of $K$: $\sigma_f - \sigma_b = \sigma_f/K$ (since the free charge is screened by bound charges by factor $K$).

$E = \frac{\sigma_f/K}{\epsilon_0} = \frac{\sigma_f}{K\epsilon_0} = \frac{E_0}{K}$ ✓
</details>

---

**Q29–Q32:** Applied dielectric problems.

**Q29.** A radio capacitor uses mica ($K = 6$, dielectric strength $10^8$ V/m). It needs $C = 100$ pF. Find the minimum plate area if the rated voltage is $500$ V.

<details><summary><b>Answer</b></summary>

$C = K\epsilon_0 A/d$. Minimum $d$ for breakdown protection: $d_{min} = V/E_{breakdown} = 500/10^8 = 5\times10^{-6}$ m.

$A = Cd/(K\epsilon_0) = 100\times10^{-12}\times5\times10^{-6}/(6\times8.85\times10^{-12}) = 5\times10^{-16}/(53.1\times10^{-12})$

$A = \mathbf{9.4\times10^{-6}\,m^2 = 9.4\,mm^2}$ — compact, practical.
</details>

---

**Q30.** Two capacitors ($C_1 = 5\,\mu F$, $C_2 = 10\,\mu F$) are in series, charged by $120$ V. A dielectric of $K = 2$ fills $C_1$. Find new charge on each (battery stays connected).

<details><summary><b>Answer</b></summary>

After dielectric: $C_1' = 2C_1 = 10\,\mu F$.

New series combination: $C_{eq}' = 10\times10/(10+10) = 5\,\mu F$

$Q' = C_{eq}'\times V = 5\times10^{-6}\times120 = 600\,\mu C$

Both capacitors have the same charge (series): $Q_1 = Q_2 = \mathbf{600\,\mu C}$
</details>

---

**Q31.** A capacitor of $4\,\mu F$ is charged to $50$ V with air. A dielectric of $K = 5$ is now inserted with the battery disconnected. What is the new potential difference?<br>

<details><summary><b>Answer</b></summary>

Battery disconnected → $Q$ constant = $CV = 4\times10^{-6}\times50 = 200\,\mu C$

$C' = KC = 5\times4 = 20\,\mu F$

$V' = Q/C' = 200\times10^{-6}/(20\times10^{-6}) = \mathbf{10\,V}$

(Reduced by $K = 5$, from 50 V to 10 V)
</details>

---

**Q32.** The energy density in a dielectric medium is $u = K\epsilon_0 E^2/2$. A capacitor with $K = 4$, $A = 0.01\,m^2$, $d = 1\,mm$, $V = 200$ V. Find total energy by (a) $U = \frac{1}{2}CV^2$, (b) $U = u\times$ Volume.

<details><summary><b>Answer</b></summary>

$C = K\epsilon_0 A/d = 4\times8.85\times10^{-12}\times0.01/10^{-3} = 3.54\times10^{-10}$ F

**(a)** $U = \frac{1}{2}\times3.54\times10^{-10}\times(200)^2 = \frac{1}{2}\times3.54\times10^{-10}\times4\times10^4 = \mathbf{7.08\times10^{-6}\,J}$

**(b)** $E = V/d = 200/10^{-3} = 2\times10^5$ V/m

$u = K\epsilon_0 E^2/2 = 4\times8.85\times10^{-12}\times(2\times10^5)^2/2 = 4\times8.85\times10^{-12}\times2\times10^{10} = 7.08\times10^{-1}$ J/m³

Volume $= 0.01\times10^{-3} = 10^{-5}$ m³

$U = u\times V_{vol} = 7.08\times10^{-1}\times10^{-5} = 7.08\times10^{-6}$ J ✓
</details>

---

*Next: [Chapter 11 — Capacitors and the Parallel Plate Capacitor →](./11_capacitors_parallel_plate.md)*
