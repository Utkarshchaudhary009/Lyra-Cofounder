# Chapter 3: Electrode Potential — The Microscopic Tug-of-War

> *NCERT Sections 3.3*

---

## 🎯 Stage 1: The Core Idea

### The Microscopic Tug-of-War
Imagine dipping a solid copper rod into a beaker of copper sulphate solution. At the exact microscopic boundary where the metal touches the liquid, a fierce tug-of-war begins. 

There are two competing desires:
1. **Solution Pressure (The "Push"):** Metal atoms on the rod want to lose electrons, become ions, and dissolve into the water ($M \rightarrow M^{n+} + ne^-$).
2. **Osmotic Pressure of Ions (The "Pull"):** Metal ions already in the water want to steal electrons from the rod and deposit themselves as solid metal ($M^{n+} + ne^- \rightarrow M$).

Depending on which force is stronger for a specific metal, the metal rod will either become slightly negatively charged (if atoms dissolve, leaving electrons behind) or slightly positively charged (if ions deposit, stealing electrons). 
This separation of charges at the boundary creates an electrical double layer. The potential difference developed across this layer is called the **Electrode Potential ($E$)**.

### Standard Electrode Potential ($E^\circ$)
Because temperature and concentration change the intensity of this tug-of-war, scientists agreed on a "fair battlefield" to measure all metals. If you measure the potential at exactly **298 K**, with exactly **1 Molar (1 M)** concentration of ions, and gases at **1 bar (or 1 atm)** pressure, you get the **Standard Electrode Potential ($E^\circ$)**.

---

## 🔬 Stage 2: The Formula Lab

### 1. The IUPAC Rule (Reduction is King)
A metal has an Oxidation Potential ($E_{ox}$) and a Reduction Potential ($E_{red}$). 
**Rule:** They are mathematically identical but opposite in sign.
$$ E_{ox} = -E_{red} $$
**IUPAC Convention:** When scientists just say "Standard Electrode Potential" ($E^\circ$), they *always* mean the **Standard Reduction Potential ($E^\circ_{red}$)**.

### 2. Intensive Property
Electrode potential is an **intensive property**. It depends on the *nature* of the material, not the *amount*. 
If $Ag^+ + e^- \rightarrow Ag$ has an $E^\circ = 0.80\ V$, then $2Ag^+ + 2e^- \rightarrow 2Ag$ also has $E^\circ = 0.80\ V$. You **never multiply** $E^\circ$ by stoichiometric coefficients.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Converting Oxidation and Reduction Potentials ⭐

**Pattern:** "Given an oxidation potential, find the reduction potential (or vice versa), and interpret IUPAC terminology."

**Solved Example** 🟢
> For zinc, the standard oxidation potential $E^\circ_{Zn/Zn^{2+}}$ is $+0.76\ V$. What is its standard reduction potential, and what is its IUPAC "Standard Electrode Potential"?

<details><summary><b>Solution</b></summary>
- Reduction is the exact reverse of oxidation. Therefore, $E^\circ_{red} = -E^\circ_{ox}$.
- $E^\circ_{Zn^{2+}/Zn} = -0.76\ V$.
- By IUPAC convention, "Standard Electrode Potential" always refers to the Reduction Potential. So, the Standard Electrode Potential of Zinc is **$-0.76\ V$**.
</details>

**Practice:**

1. 🟢 Given $E^\circ_{Cu^{2+}/Cu} = +0.34\ V$. What is the standard oxidation potential of Copper?
<details><summary><b>Answer</b></summary>
$E^\circ_{Cu/Cu^{2+}} = -0.34\ V$.
</details>

2. 🟢 The standard electrode potential of Silver is $+0.80\ V$. Write the half-reaction this value corresponds to.
<details><summary><b>Answer</b></summary>
Standard electrode potential implies *reduction*. Therefore, the reaction is: $Ag^+ + e^- \rightarrow Ag$.
</details>

3. 🟡 For a metal $M$, $E^\circ_{M/M^{3+}} = +1.66\ V$. What is the value of $E^\circ_{M^{3+}/M}$?
<details><summary><b>Answer</b></summary>
The given notation $M/M^{3+}$ represents oxidation. The required notation $M^{3+}/M$ represents reduction. 
$E^\circ_{M^{3+}/M} = -1.66\ V$.
</details>

4. 🟡 A textbook states: "The standard oxidation potential of $Fe^{2+}$ to $Fe^{3+}$ is $-0.77\ V$." What is the standard electrode potential for the $Fe^{3+}/Fe^{2+}$ couple?
<details><summary><b>Answer</b></summary>
Given: $E^\circ_{Fe^{2+}/Fe^{3+}} = -0.77\ V$ (Oxidation).
Required: Standard electrode potential = Reduction potential = $E^\circ_{Fe^{3+}/Fe^{2+}}$.
$E^\circ_{Fe^{3+}/Fe^{2+}} = -(-0.77\ V) = \textbf{+0.77\ V}$.
</details>

5. 🔴 If the reduction potential of $I_2/I^-$ is $+0.54\ V$, what is the potential for the reaction $2I^- \rightarrow I_2 + 2e^-$?
<details><summary><b>Answer</b></summary>
The given reaction is an oxidation reaction.
$E_{ox} = -E_{red} = \textbf{-0.54\ V}$.
</details>

---

### Type 2: Identifying the Stronger "Pull" or "Push" ⭐

**Pattern:** "Compare $E^\circ$ values to determine which substance has a higher tendency to get reduced or oxidized."

**Solved Example** 🟡
> Given $E^\circ_{A^{2+}/A} = -0.25\ V$ and $E^\circ_{B^{2+}/B} = +0.15\ V$. Which metal has a greater tendency to undergo oxidation?

<details><summary><b>Solution</b></summary>
- These are reduction potentials. 
- Higher (more positive) reduction potential $\rightarrow$ greater tendency to get **reduced** (gain electrons). B wants to reduce more than A.
- Lower (more negative) reduction potential $\rightarrow$ greater tendency to get **oxidized** (lose electrons). 
- Therefore, **metal A** has a greater tendency to undergo oxidation.
</details>

**Practice:**

1. 🟢 Given $E^\circ_{X^+/X} = +0.80\ V$ and $E^\circ_{Y^{2+}/Y} = -0.76\ V$. Which ion has a greater tendency to gain electrons?
<details><summary><b>Answer</b></summary>
The ion with the more positive reduction potential wants to gain electrons (reduce). Therefore, **$X^+$** has a greater tendency to gain electrons.
</details>

2. 🟢 $E^\circ_{Zn^{2+}/Zn} = -0.76\ V$ and $E^\circ_{Cu^{2+}/Cu} = +0.34\ V$. Which metal prefers to lose electrons?
<details><summary><b>Answer</b></summary>
The metal with the more negative reduction potential prefers to oxidize (lose electrons). Therefore, **Zinc (Zn)** prefers to lose electrons.
</details>

3. 🟡 You have three metals: P ($E^\circ = -1.2\ V$), Q ($E^\circ = +0.4\ V$), and R ($E^\circ = -2.3\ V$). Arrange them in increasing order of their tendency to get oxidized.
<details><summary><b>Answer</b></summary>
Tendency to oxidize increases as reduction potential becomes more negative. 
Most positive to most negative: Q (+0.4) < P (-1.2) < R (-2.3).
Increasing order of oxidation tendency: **Q < P < R**.
</details>

4. 🟡 Given $E^\circ_{Mg^{2+}/Mg} = -2.37\ V$ and $E^\circ_{Ag^+/Ag} = +0.80\ V$. If you place Mg in a solution of $Ag^+$, will a spontaneous reaction occur?
<details><summary><b>Answer</b></summary>
Mg has a highly negative reduction potential, meaning it strongly wants to oxidize ($Mg \rightarrow Mg^{2+}$). $Ag^+$ has a positive reduction potential, meaning it strongly wants to reduce ($Ag^+ \rightarrow Ag$). Since both get what they "want", a **spontaneous reaction will occur**. (Mg will displace Ag).
</details>

5. 🔴 If $E^\circ_{F_2/F^-} = +2.87\ V$ and $E^\circ_{Li^+/Li} = -3.05\ V$, which species is the strongest electron puller (oxidizing agent) and which is the strongest electron pusher (reducing agent)?
<details><summary><b>Answer</b></summary>
- Highest reduction potential (+2.87 V) means it pulls electrons the hardest. So, **$F_2$** is the strongest electron puller (strongest oxidizing agent).
- Lowest reduction potential (-3.05 V) means it pushes away electrons the hardest. So, **$Li(s)$** is the strongest electron pusher (strongest reducing agent).
</details>

---

### Type 3: The Intensive Nature of Electrode Potential ⭐

**Pattern:** "Given the $E^\circ$ for a half-reaction, find the $E^\circ$ when the reaction is multiplied by a stoichiometric coefficient."

**Solved Example** 🟢
> The standard reduction potential for $Cu^{2+} + 2e^- \rightarrow Cu$ is $+0.34\ V$. What is the standard potential for the half-reaction $\frac{1}{2} Cu^{2+} + e^- \rightarrow \frac{1}{2} Cu$?

<details><summary><b>Solution</b></summary>
Electrode potential ($E^\circ$) is an **intensive property**. It depends on the concentration and nature of the material, not the quantity. 
Changing the stoichiometric coefficients does NOT change the $E^\circ$ value.
Therefore, the potential is still **$+0.34\ V$**.
</details>

**Practice:**

1. 🟢 $E^\circ$ for $Ag^+ + e^- \rightarrow Ag$ is $0.80\ V$. What is $E^\circ$ for $2Ag^+ + 2e^- \rightarrow 2Ag$?
<details><summary><b>Answer</b></summary>
It remains unchanged. **$0.80\ V$**.
</details>

2. 🟢 Given $E^\circ_{Al^{3+}/Al} = -1.66\ V$. Find the potential for $3Al \rightarrow 3Al^{3+} + 9e^-$.
<details><summary><b>Answer</b></summary>
First, the reaction is reversed (it's oxidation). So sign changes: $+1.66\ V$.
Second, it is multiplied by 3. But $E^\circ$ is intensive, so the multiplier has no effect.
Answer: **$+1.66\ V$**.
</details>

3. 🟡 Why is $\Delta G^\circ$ multiplied when a reaction is multiplied, but $E^\circ$ is not?
<details><summary><b>Answer</b></summary>
$\Delta G^\circ$ is an extensive property (energy depends on the amount of substance). $E^\circ$ is an intensive property (voltage/potential difference does not depend on the size of the system, just like temperature). The formula relating them is $\Delta G^\circ = -nFE^\circ$. If you multiply the reaction by 2, $n$ (moles of electrons) doubles, so $\Delta G^\circ$ doubles, but $E^\circ$ remains constant.
</details>

4. 🟡 A student calculates the oxidation potential of $2Cl^- \rightarrow Cl_2 + 2e^-$ as $-1.36\ V$. What is the reduction potential of $\frac{1}{2} Cl_2 + e^- \rightarrow Cl^-$?
<details><summary><b>Answer</b></summary>
Reverse the reaction: Oxidation to Reduction means change sign $\rightarrow +1.36\ V$.
Ignore the stoichiometric coefficient differences (intensive property).
Answer: **$+1.36\ V$**.
</details>

5. 🔴 Given $E^\circ_{Fe^{3+}/Fe^{2+}} = 0.77\ V$. Is it correct to say the potential for the transfer of 2 electrons ($2Fe^{3+} + 2e^- \rightarrow 2Fe^{2+}$) is $1.54\ V$?
<details><summary><b>Answer</b></summary>
**No.** Potential is intensive. The potential difference driving the reaction is independent of the number of moles reacting. The value remains **$0.77\ V$**.
</details>

---

### Type 4: Standard Conditions Identification ⭐

**Pattern:** "Identify what constitutes 'Standard Conditions' and how deviations affect the definition."

**Solved Example** 🟢
> A scientist measures the potential of a Copper electrode dipped in a $0.1\ M$ $CuSO_4$ solution at 298 K. Can this value be called the Standard Electrode Potential ($E^\circ$)?

<details><summary><b>Solution</b></summary>
**No.** Standard Electrode Potential requires the concentration of all aqueous ions to be exactly **$1\ M$** (1 mol/L). Since the concentration here is $0.1\ M$, the measured value is simply an electrode potential ($E$), not the standard one ($E^\circ$).
</details>

**Practice:**

1. 🟢 What are the standard conditions of temperature and pressure for measuring $E^\circ$?
<details><summary><b>Answer</b></summary>
Temperature = **298 K** ($25^\circ C$). Pressure for gases = **1 bar** (or 1 atm).
</details>

2. 🟢 If you measure a Zinc half-cell at 300 K with a $1\ M$ solution, is it the standard potential?
<details><summary><b>Answer</b></summary>
**No.** The temperature must be exactly 298 K.
</details>

3. 🟡 A chlorine gas electrode $Pt | Cl_2 | Cl^-$ has $Cl_2$ gas bubbling at 2 atm and $[Cl^-] = 1\ M$ at 298 K. Is this a standard half-cell?
<details><summary><b>Answer</b></summary>
**No.** The gas pressure must be exactly 1 atm (or 1 bar). 
</details>

4. 🟡 For the half-cell $Pt | Fe^{2+}, Fe^{3+}$, what concentrations are required to make it a standard half-cell?
<details><summary><b>Answer</b></summary>
**Both** $[Fe^{2+}]$ and $[Fe^{3+}]$ must be exactly $1\ M$.
</details>

5. 🔴 Why do we even need "Standard Conditions"?
<details><summary><b>Answer</b></summary>
Electrode potential varies continuously with concentration and temperature (as dictated by the Nernst Equation). To compare the intrinsic "electron-pulling" strength of different elements fairly, we must measure them all under identical baseline conditions.
</details>

---

### Type 5: Nernst Theory of Solution Pressure vs Osmotic Pressure ⭐

**Pattern:** "Conceptual understanding of the electrical double layer formation."

**Solved Example** 🟡
> If the solution pressure of a metal $M$ is greater than the osmotic pressure of its ions $M^{n+}$ in the solution, what will be the charge on the metal rod?

<details><summary><b>Solution</b></summary>
- Solution pressure pushes metal atoms into the solution as ions: $M \rightarrow M^{n+} + ne^-$.
- Osmotic pressure pushes ions onto the rod: $M^{n+} + ne^- \rightarrow M$.
- If Solution Pressure > Osmotic Pressure, the metal dissolves faster than it deposits. The metal atoms leave their electrons behind on the rod.
- Therefore, the metal rod acquires a **Negative** charge.
</details>

**Practice:**

1. 🟢 If the osmotic pressure of ions is greater than the solution pressure of the metal, what happens to the metal rod?
<details><summary><b>Answer</b></summary>
Ions from the solution deposit onto the rod ($M^{n+} + ne^- \rightarrow M$), stealing electrons from it. The rod becomes deficient in electrons and acquires a **Positive** charge.
</details>

2. 🟡 A metal rod is dipped in its salt solution and develops no potential difference. What does this imply about the two pressures?
<details><summary><b>Answer</b></summary>
It implies that the system is at perfect equilibrium where **Solution Pressure = Osmotic Pressure**. The rate of dissolution equals the rate of deposition.
</details>

3. 🟡 Why does the dissolution of a metal into its own solution eventually stop if not connected to an external circuit?
<details><summary><b>Answer</b></summary>
As the metal dissolves, it leaves electrons on the rod (making it negative) and adds positive ions to the solution. The negative rod attracts the positive ions, creating an electrical double layer. This potential difference eventually opposes and halts further dissolution (equilibrium is reached).
</details>

4. 🔴 At the interface of a positively charged electrode and the solution, what does the Helmholtz electrical double layer consist of?
<details><summary><b>Answer</b></summary>
It consists of a layer of positive charge rigidly on the metal surface, and an adjacent layer of negative ions (anions) from the solution firmly attracted to the metal surface, acting like a microscopic capacitor.
</details>

---

### Type 6: Identifying Feasibility from a Single Half-Cell Sign ⭐

**Pattern:** "Using the sign of $E^\circ$ to predict if a metal will dissolve in acids or act as a good reducing/oxidizing agent."

**Solved Example** 🟡
> The standard reduction potential of $Ni^{2+}/Ni$ is $-0.25\ V$. Does Nickel have a natural tendency to be oxidized or reduced when compared to Hydrogen (which has $E^\circ = 0.00\ V$)?

<details><summary><b>Solution</b></summary>
- Since $E^\circ_{Ni^{2+}/Ni}$ is negative, it is lower than Hydrogen's potential.
- A lower reduction potential means it has a stronger tendency to undergo oxidation (lose electrons) compared to Hydrogen. 
- Therefore, Nickel has a **natural tendency to be oxidized** (it will dissolve in acids and release $H_2$ gas).
</details>

**Practice:**

1. 🟢 $E^\circ_{Cu^{2+}/Cu} = +0.34\ V$. Will Copper naturally oxidize or reduce compared to Hydrogen?
<details><summary><b>Answer</b></summary>
It has a positive reduction potential (higher than Hydrogen). It prefers to be **reduced**. (This is why Copper does not dissolve in dilute non-oxidizing acids like $HCl$).
</details>

2. 🟢 A metal has $E^\circ = -2.37\ V$. Is it a strong oxidizing agent or a strong reducing agent?
<details><summary><b>Answer</b></summary>
Highly negative reduction potential means it strongly wants to oxidize. A substance that oxidizes easily is a **strong reducing agent**.
</details>

3. 🟡 Arrange the following in order of increasing oxidizing power: $A$ ($E^\circ = +1.50\ V$), $B$ ($E^\circ = -0.74\ V$), $C$ ($E^\circ = 0.00\ V$).
<details><summary><b>Answer</b></summary>
Oxidizing power is the tendency to get reduced. Higher (more positive) $E^\circ$ means higher oxidizing power.
Increasing order: **$B < C < A$**.
</details>

4. 🟡 A non-metal $X_2$ has $E^\circ_{X_2/X^-} = +2.87\ V$. Is $X_2$ a good electron donor or electron acceptor?
<details><summary><b>Answer</b></summary>
Extremely high positive reduction potential means it strongly wants to reduce (gain electrons). Therefore, it is an excellent **electron acceptor**.
</details>

5. 🔴 Consider $E^\circ_{Sn^{4+}/Sn^{2+}} = +0.15\ V$ and $E^\circ_{Cr^{3+}/Cr} = -0.74\ V$. Which species is the most stable: $Sn^{4+}$, $Sn^{2+}$, $Cr^{3+}$, or $Cr$?
<details><summary><b>Answer</b></summary>
- $Cr$ has a highly negative reduction potential, meaning it strongly wants to oxidize to $Cr^{3+}$. Thus, $Cr^{3+}$ is very stable.
- $Sn^{4+}$ has a positive reduction potential to become $Sn^{2+}$, meaning it wants to reduce. Thus $Sn^{2+}$ is more stable than $Sn^{4+}$.
Therefore, the most stable oxidation state species among these is **$Cr^{3+}$**.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1. (NCERT Type)** 🟢 The standard electrode potential is measured by assigning a potential of zero to which electrode?
(a) Standard Zinc Electrode
(b) Standard Calomel Electrode
(c) Standard Hydrogen Electrode (SHE)
(d) Standard Copper Electrode

<details><summary><b>Answer</b></summary>
**Answer: (c)**
By international convention, the Standard Hydrogen Electrode (SHE) is arbitrarily assigned a potential of exactly 0.00 V at all temperatures. All other potentials are measured relative to it.
</details>

**Q2. (Exemplar Type)** 🟡 Which of the following is an intensive property?
(a) Gibbs Free Energy ($\Delta G$)
(b) Enthalpy ($\Delta H$)
(c) Standard Electrode Potential ($E^\circ$)
(d) Cell Resistance ($R$)

<details><summary><b>Answer</b></summary>
**Answer: (c)**
Standard Electrode Potential does not depend on the mass or number of moles of the substance participating in the half-reaction.
</details>

**Q3. (Subtle Detail)** 🟡 If a metal has a negative standard reduction potential, it means:
(a) The metal ions are easily reduced.
(b) The metal is a poorer reducing agent than Hydrogen.
(c) The metal is a better reducing agent than Hydrogen.
(d) The metal acts as an inert electrode.

<details><summary><b>Answer</b></summary>
**Answer: (c)**
Hydrogen's reduction potential is 0.00 V. A negative reduction potential means the metal *hates* being reduced and *loves* being oxidized compared to hydrogen. A substance that oxidizes easily is a good reducing agent.
</details>

**Q4. (Tricky)** 🔴 For the half-cell reaction $M^{n+} + ne^- \rightarrow M$, the Nernst equation shows how potential changes with concentration. If the concentration of $M^{n+}$ is zero, what happens to the electrode potential?
(a) It becomes zero.
(b) It becomes equal to $E^\circ$.
(c) It becomes infinitely negative.
(d) It becomes infinitely positive.

<details><summary><b>Answer</b></summary>
**Answer: (c)**
$E = E^\circ - \frac{RT}{nF} \ln \frac{1}{[M^{n+}]}$. If $[M^{n+}] \rightarrow 0$, the $\ln(\infty)$ term approaches $+\infty$, making the whole expression $E^\circ - \infty$, which means the potential becomes infinitely negative. (Physically, a metal in pure water with zero of its own ions has an undefined/highly unstable potential until some ions dissolve).
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🟡 ⭐ You are given the following half-reactions:
$A^{3+} + 3e^- \rightarrow A \quad (E^\circ = -1.50\ V)$
$B^{2+} + 2e^- \rightarrow B \quad (E^\circ = +0.50\ V)$
If you multiply the first reaction by 2 and the second by 3, what are the new standard oxidation potentials of A and B?

<details><summary><b>Solution</b></summary>
- Multiplying the reactions by any stoichiometric coefficient **does not change** the magnitude of the potential because $E^\circ$ is an intensive property.
- The given values are Reduction Potentials.
- The question asks for **Oxidation Potentials**. We must reverse the sign.
- $E^\circ_{ox}(A) = -(-1.50\ V) = \textbf{+1.50\ V}$
- $E^\circ_{ox}(B) = -(+0.50\ V) = \textbf{-0.50\ V}$
</details>

**Q2.** 🔴 Consider a beaker containing a $1\ M$ solution of $ZnSO_4$ at 298 K. A piece of zinc is dropped into it. 
(a) Is this a standard half-cell?
(b) Why doesn't a massive continuous current flow?
(c) Does an electrical double layer form?

<details><summary><b>Solution</b></summary>
(a) **Yes**, it is a standard half-cell because the temperature is 298 K and the ion concentration is $1\ M$.
(b) No continuous current flows because it is an **open circuit** (only one half-cell). Electrons have nowhere to go.
(c) **Yes**. A microscopic amount of Zn will dissolve (or deposit) until the solution pressure equals the osmotic pressure, creating the Helmholtz electrical double layer and establishing the equilibrium potential of $-0.76\ V$.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Define Electrode Potential. *(1 mark)*
<details><summary><b>Model Answer</b></summary>
Electrode potential is the potential difference that develops between a metal electrode and its ions in the surrounding solution when the metal is in equilibrium with its ions.
</details>

**Q2.** 🟢 What is meant by Standard Electrode Potential? *(1 mark)*
<details><summary><b>Model Answer</b></summary>
It is the electrode potential of a half-cell measured under standard conditions: temperature of 298 K, concentration of ions at 1 M, and pressure of gases (if any) at 1 atm. By IUPAC convention, it refers to the standard reduction potential.
</details>

**Q3.** 🟡 Why is it impossible to measure the absolute electrode potential of a single half-cell? *(2 marks)*
<details><summary><b>Model Answer</b></summary>
A potential difference can only be measured across a closed circuit between two points. A single half-cell represents only half of a reaction (either oxidation or reduction alone cannot happen). We can only measure the *difference* in potential between two half-cells connected together, which is why a reference electrode (like SHE) is required.
</details>

**Q4.** 🟡 State the IUPAC convention for representing electrode potentials. *(1 mark)*
<details><summary><b>Model Answer</b></summary>
According to IUPAC convention, all standard electrode potentials are represented and tabulated as **Standard Reduction Potentials**.
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🟡 ⭐ If the standard oxidation potential of $Zn/Zn^{2+}$ is $+0.76\ V$ and that of $Fe/Fe^{2+}$ is $+0.44\ V$, then which of the following is correct?
(a) $Zn^{2+}$ is a stronger oxidizing agent than $Fe^{2+}$.
(b) $Zn$ is a stronger reducing agent than $Fe$.
(c) $Fe$ is a stronger reducing agent than $Zn$.
(d) $Fe^{2+}$ is a stronger reducing agent than $Zn^{2+}$.

<details><summary><b>Answer</b></summary>
**Answer: (b)**
Oxidation potential represents the tendency to lose electrons (act as a reducing agent). Zinc has a higher oxidation potential (+0.76 V) than Iron (+0.44 V). Therefore, Zinc has a stronger tendency to oxidize, making it a **stronger reducing agent**.
</details>

**Q2.** 🔴 The standard reduction potentials for $Cu^{2+}/Cu$, $Zn^{2+}/Zn$, $Li^+/Li$, and $Ag^+/Ag$ are $+0.34\ V$, $-0.76\ V$, $-3.05\ V$, and $+0.80\ V$ respectively. Which of the following is the strongest oxidizing agent?
(a) $Ag^+$
(b) $Li^+$
(c) $Cu^{2+}$
(d) $Zn^{2+}$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
The strongest oxidizing agent is the species that has the highest tendency to get reduced (gain electrons). This corresponds to the highest (most positive) standard reduction potential. $Ag^+/Ag$ has the highest value (+0.80 V), making **$Ag^+$** the strongest oxidizing agent. (Note: $Li$ is the strongest *reducing* agent, but $Li^+$ is the weakest oxidizing agent).
</details>

**Q3.** 🔴 Let $E_1$ be the standard reduction potential for the reaction $X^{2+} + 2e^- \rightarrow X$. Let $E_2$ be the standard reduction potential for the reaction $\frac{1}{2} X^{2+} + e^- \rightarrow \frac{1}{2} X$. The relationship between $E_1$ and $E_2$ is:
(a) $E_1 = 2E_2$
(b) $E_1 = E_2 / 2$
(c) $E_1 = E_2$
(d) $E_1 = E_2^2$

<details><summary><b>Answer</b></summary>
**Answer: (c)**
Standard electrode potential is an intensive thermodynamic property. It represents the potential difference (voltage) driving the reaction, which is independent of the stoichiometry (the amount of substance reacting). Therefore, $E_1 = E_2$.
</details>

---

*Next: [Chapter 4 — Standard Hydrogen Electrode (SHE) →](./04_standard_hydrogen_electrode.md)*
