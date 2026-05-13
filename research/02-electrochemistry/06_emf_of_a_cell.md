# Chapter 6: EMF of a Cell — The Voltage Engine

> *NCERT Sections 3.2 & 3.3*

---

## 🎯 Stage 1: The Core Idea

### EMF vs. Potential Difference
Imagine a car engine. When the car is in neutral and you press the gas, the engine revs up to its **absolute maximum theoretical power**. But the moment you put it in gear and start driving, friction from the road and the weight of the car drag it down. The *actual* speed you get is less than the theoretical maximum.

An electrochemical cell works the exact same way:
- **Electromotive Force (EMF):** This is the engine in neutral. It is the maximum potential difference between the two electrodes when **no current is being drawn** from the cell (an open circuit). It is the true, intrinsic driving force of the reaction.
- **Potential Difference ($V$):** This is the car driving on the road. The moment you connect a wire and draw current (a closed circuit), the cell's own internal resistance causes a slight voltage drop. The voltage you actually measure across the working cell is the Potential Difference, and it is always *less* than the EMF ($V = E - Ir$).

### The Simple Math of EMF
The EMF of a cell is simply the difference in the reduction potentials of its two electrodes. The Cathode (which has a higher pull for electrons) minus the Anode (which has a lower pull).
**$EMF = \text{Pull of Cathode} - \text{Pull of Anode}$**

---

## 🔬 Stage 2: The Formula Lab

### The Master Formula
To calculate the Standard EMF ($E^\circ_{cell}$) of a cell, you only need one formula. 
**Crucial Rule:** Ensure BOTH values you plug in are Standard **Reduction** Potentials.

$$ E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} $$

Alternatively, using the L-O-A-N rule (Left is Anode, Right is Cathode):
$$ E^\circ_{cell} = E^\circ_{Right} - E^\circ_{Left} $$

### The Spontaneity Check
For a Galvanic cell to actually work (for the reaction to be spontaneous and generate electricity), the EMF **must be positive**.
- If $E^\circ_{cell} > 0 \implies$ Spontaneous (Galvanic cell works).
- If $E^\circ_{cell} < 0 \implies$ Non-spontaneous (You must supply electricity to force it to happen, like an Electrolytic cell).

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic $E^\circ_{cell}$ Calculation ⭐

**Pattern:** "Given two half-cell $E^\circ$ values, calculate the maximum possible standard EMF."

**Solved Example** 🟢
> Calculate the standard EMF of a cell made of Zinc and Silver. 
> Given: $E^\circ_{Zn^{2+}/Zn} = -0.76\ V$ and $E^\circ_{Ag^+/Ag} = +0.80\ V$.

<details><summary><b>Solution</b></summary>
- To get a working Galvanic cell, the EMF must be positive. 
- Therefore, the metal with the higher reduction potential must be the Cathode.
- $Ag$ ($+0.80\ V$) > $Zn$ ($-0.76\ V$). So, Ag is Cathode, Zn is Anode.
- $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$
- $E^\circ_{cell} = 0.80 - (-0.76) = 0.80 + 0.76 = \textbf{+1.56\ V}$.
</details>

**Practice:**

1. 🟢 Calculate standard EMF for a cell made of Cu ($+0.34\ V$) and Ag ($+0.80\ V$).
<details><summary><b>Answer</b></summary>
Ag is Cathode, Cu is Anode.
$E^\circ_{cell} = 0.80 - 0.34 = \textbf{+0.46\ V}$.
</details>

2. 🟢 Calculate standard EMF for a cell made of Mg ($-2.37\ V$) and Zn ($-0.76\ V$).
<details><summary><b>Answer</b></summary>
Zn has a higher reduction potential ($-0.76 > -2.37$). So Zn is Cathode, Mg is Anode.
$E^\circ_{cell} = -0.76 - (-2.37) = -0.76 + 2.37 = \textbf{+1.61\ V}$.
</details>

3. 🟡 Calculate standard EMF for a cell made of $Fe^{3+}/Fe^{2+}$ ($+0.77\ V$) and $I_2/I^-$ ($+0.54\ V$).
<details><summary><b>Answer</b></summary>
$Fe^{3+}/Fe^{2+}$ is Cathode, $I_2/I^-$ is Anode.
$E^\circ_{cell} = 0.77 - 0.54 = \textbf{+0.23\ V}$.
</details>

4. 🟡 You are given Sn ($-0.14\ V$) and Pb ($-0.13\ V$). What is the maximum voltage a standard cell made of these two can produce?
<details><summary><b>Answer</b></summary>
Pb is Cathode ($-0.13 > -0.14$). Sn is Anode.
$E^\circ_{cell} = -0.13 - (-0.14) = -0.13 + 0.14 = \textbf{+0.01\ V}$.
</details>

5. 🔴 Given $E^\circ_{Cu^{2+}/Cu} = +0.34\ V$ and the standard oxidation potential of Al is $+1.66\ V$. Calculate $E^\circ_{cell}$ for an Aluminum-Copper cell.
<details><summary><b>Answer</b></summary>
First, convert Al oxidation potential to reduction potential: $E^\circ_{Al^{3+}/Al} = -1.66\ V$.
Cu is Cathode, Al is Anode.
$E^\circ_{cell} = 0.34 - (-1.66) = \textbf{+2.00\ V}$.
</details>

---

### Type 2: Calculating $E^\circ_{cell}$ from Cell Notation ⭐

**Pattern:** "Given a specific cell notation like $A|A^+ || B^+|B$, calculate $E^\circ_{cell}$ without assuming it's spontaneous."

**Solved Example** 🟡
> Calculate the standard EMF of the cell: $Ag(s)\ |\ Ag^+(aq)\ ||\ Cu^{2+}(aq)\ |\ Cu(s)$
> Given $E^\circ_{Ag} = +0.80\ V, E^\circ_{Cu} = +0.34\ V$.

<details><summary><b>Solution</b></summary>
- The notation rigidly dictates roles. Left is Anode, Right is Cathode.
- Anode (Left) = Ag. Cathode (Right) = Cu.
- $E^\circ_{cell} = E^\circ_{Right} - E^\circ_{Left}$
- $E^\circ_{cell} = 0.34 - 0.80 = \textbf{-0.46\ V}$.
*(Note: A negative value means this specific setup will not work spontaneously in the direction written).*
</details>

**Practice:**

1. 🟢 Calculate $E^\circ_{cell}$ for $Zn\ |\ Zn^{2+}\ ||\ Ag^+\ |\ Ag$. ($Zn = -0.76\ V, Ag = +0.80\ V$).
<details><summary><b>Answer</b></summary>
Right - Left = $0.80 - (-0.76) = \textbf{+1.56\ V}$.
</details>

2. 🟢 Calculate $E^\circ_{cell}$ for $Fe\ |\ Fe^{2+}\ ||\ Zn^{2+}\ |\ Zn$. ($Fe = -0.44\ V, Zn = -0.76\ V$).
<details><summary><b>Answer</b></summary>
Right - Left = $-0.76 - (-0.44) = \textbf{-0.32\ V}$.
</details>

3. 🟡 Calculate $E^\circ_{cell}$ for $Pt\ |\ Br^-\ |\ Br_2\ ||\ Cl_2\ |\ Cl^-\ |\ Pt$. ($Br_2/Br^- = 1.09\ V, Cl_2/Cl^- = 1.36\ V$).
<details><summary><b>Answer</b></summary>
Right (Cathode) = Cl. Left (Anode) = Br.
$E^\circ_{cell} = 1.36 - 1.09 = \textbf{+0.27\ V}$.
</details>

4. 🟡 Calculate the standard potential of $Cu\ |\ Cu^{2+}\ ||\ H^+\ |\ H_2\ |\ Pt$. ($Cu = +0.34\ V$).
<details><summary><b>Answer</b></summary>
Right = SHE ($0.00\ V$). Left = Cu ($0.34\ V$).
$E^\circ_{cell} = 0.00 - 0.34 = \textbf{-0.34\ V}$.
</details>

5. 🔴 Given the cell $Pt\ |\ H_2(1\ atm)\ |\ H^+(1\ M)\ ||\ X^{2+}(1\ M)\ |\ X$. If the voltmeter reads $-0.25\ V$, what is the standard reduction potential of X?
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = -0.25\ V$. 
$E^\circ_{cell} = E^\circ_X - E^\circ_{SHE}$
$-0.25\ V = E^\circ_X - 0.00\ V$
$E^\circ_X = \textbf{-0.25\ V}$.
</details>

---

### Type 3: Predicting Spontaneity from Cell Potential ⭐

**Pattern:** "Is the given chemical reaction or cell notation spontaneous?"

**Solved Example** 🟡
> Is the following reaction spontaneous? 
> $2Ag(s) + Zn^{2+}(aq) \rightarrow 2Ag^+(aq) + Zn(s)$
> ($Zn = -0.76\ V, Ag = +0.80\ V$)

<details><summary><b>Solution</b></summary>
- Determine roles from the reaction: Ag is oxidizing (0 to +1), so it acts as the Anode. $Zn^{2+}$ is reducing (+2 to 0), so it acts as the Cathode.
- Calculate $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$.
- $E^\circ_{cell} = -0.76 - (+0.80) = -1.56\ V$.
- Since $E^\circ_{cell}$ is negative, the reaction is **non-spontaneous**.
</details>

**Practice:**

1. 🟢 Is the cell $Cu\ |\ Cu^{2+}\ ||\ Ag^+\ |\ Ag$ spontaneous? ($Cu = 0.34\ V, Ag = 0.80\ V$).
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = 0.80 - 0.34 = +0.46\ V$. Positive, so **Yes, spontaneous**.
</details>

2. 🟢 Is the reaction $Ni^{2+} + Cu \rightarrow Ni + Cu^{2+}$ spontaneous? ($Ni = -0.25\ V, Cu = +0.34\ V$).
<details><summary><b>Answer</b></summary>
Cu is oxidizing (Anode). Ni is reducing (Cathode).
$E^\circ_{cell} = -0.25 - 0.34 = -0.59\ V$. Negative, so **No, non-spontaneous**.
</details>

3. 🟡 Can you keep $1\ M\ AgNO_3$ solution in a copper vessel?
<details><summary><b>Answer</b></summary>
Reaction to check: $Cu + 2Ag^+ \rightarrow Cu^{2+} + 2Ag$. 
Cu is Anode. Ag is Cathode.
$E^\circ_{cell} = 0.80 - 0.34 = +0.46\ V$. 
Since it is positive, the reaction IS spontaneous. The copper vessel will dissolve. Therefore, **No, you cannot keep it.**
</details>

4. 🟡 A student writes the notation $Sn\ |\ Sn^{2+}\ ||\ Pb^{2+}\ |\ Pb$. Is this cell capable of doing useful work? ($Sn = -0.14\ V, Pb = -0.13\ V$).
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = -0.13 - (-0.14) = +0.01\ V$.
Since $E^\circ_{cell}$ is positive, the cell generates electricity and can do useful work. **Yes.**
</details>

5. 🔴 Consider $2Fe^{3+} + 2I^- \rightarrow 2Fe^{2+} + I_2$. Given $E^\circ_{Fe^{3+}/Fe^{2+}} = 0.77\ V$ and $E^\circ_{I_2/I^-} = 0.54\ V$. Calculate $E^\circ_{cell}$. Does the stoichiometry (the "2" in front of Fe and I) affect the calculation?
<details><summary><b>Answer</b></summary>
$Fe^{3+}$ is reducing (Cathode). $I^-$ is oxidizing (Anode).
$E^\circ_{cell} = 0.77 - 0.54 = \textbf{+0.23\ V}$.
**No**, stoichiometry does not affect the calculation because standard electrode potentials are intensive properties.
</details>

---

### Type 4: EMF vs Potential Difference (Conceptual) ⭐

**Pattern:** "Understanding internal resistance and voltmeter vs potentiometer measurements."

**Solved Example** 🟡
> A student measures a newly built Daniell cell ($E^\circ = 1.10\ V$) using a standard laboratory voltmeter and gets a reading of $1.08\ V$. Why is there a discrepancy?

<details><summary><b>Solution</b></summary>
A standard voltmeter draws a tiny amount of current from the cell to deflect its needle. The moment current ($I$) flows, the cell's internal resistance ($r$) causes a voltage drop ($I \times r$).
The voltmeter measures **Potential Difference ($V$)**, where $V = E - Ir$. 
To measure true EMF ($E$), no current must be drawn, which requires a **potentiometer**, not a standard voltmeter.
</details>

**Practice:**

1. 🟢 Which is always greater for a discharging Galvanic cell: EMF or Potential Difference?
<details><summary><b>Answer</b></summary>
**EMF** is always greater (it is the maximum theoretical voltage).
</details>

2. 🟢 Under what specific condition does Potential Difference exactly equal EMF?
<details><summary><b>Answer</b></summary>
When the cell is in an **open circuit** (absolutely zero current is being drawn, $I = 0$).
</details>

3. 🟡 As a battery is used over time, its internal resistance increases. If the intrinsic EMF of the chemicals remains $1.5\ V$, what happens to the potential difference you can measure across a connected lightbulb?
<details><summary><b>Answer</b></summary>
Since $V = E - Ir$, as internal resistance ($r$) increases, the $Ir$ voltage drop increases. The potential difference ($V$) across the bulb **decreases**, causing the bulb to dim.
</details>

4. 🟡 Name the instrument that is preferred for accurately measuring the EMF of a cell.
<details><summary><b>Answer</b></summary>
A **Potentiometer** (because it balances the voltage without drawing any current from the cell).
</details>

---

### Type 5: Finding Unknown Half-Cell Potential ⭐

**Pattern:** "Using $E^\circ_{cell}$ and one known half-cell potential to find the other."

**Solved Example** 🟢
> A cell $A\ |\ A^{2+}\ ||\ B^{2+}\ |\ B$ has an $E^\circ_{cell}$ of $1.20\ V$. If the standard reduction potential of B is $+0.50\ V$, find the standard reduction potential of A.

<details><summary><b>Solution</b></summary>
- A is Anode (Left). B is Cathode (Right).
- $E^\circ_{cell} = E^\circ_{B} - E^\circ_{A}$
- $1.20 = 0.50 - E^\circ_{A}$
- $E^\circ_{A} = 0.50 - 1.20 = \textbf{-0.70\ V}$.
</details>

**Practice:**

1. 🟢 For $X\ |\ X^+\ ||\ Y^+\ |\ Y$, $E^\circ_{cell} = 0.90\ V$. If $E^\circ_X = -0.40\ V$, what is $E^\circ_Y$?
<details><summary><b>Answer</b></summary>
$0.90 = E^\circ_Y - (-0.40) \implies 0.90 = E^\circ_Y + 0.40$
$E^\circ_Y = 0.90 - 0.40 = \textbf{+0.50\ V}$.
</details>

2. 🟢 The standard EMF of $Zn\ |\ Zn^{2+}\ ||\ Ni^{2+}\ |\ Ni$ is $0.51\ V$. Given $E^\circ_{Zn} = -0.76\ V$, find $E^\circ_{Ni}$.
<details><summary><b>Answer</b></summary>
$0.51 = E^\circ_{Ni} - (-0.76) \implies E^\circ_{Ni} = 0.51 - 0.76 = \textbf{-0.25\ V}$.
</details>

3. 🟡 A cell consists of $SHE$ and a metal $M$ electrode. The cell potential is $2.37\ V$, and $M$ acts as the anode. What is the standard reduction potential of $M$?
<details><summary><b>Answer</b></summary>
M is Anode. SHE is Cathode ($0.00\ V$).
$2.37 = 0.00 - E^\circ_M$
$E^\circ_M = \textbf{-2.37\ V}$.
</details>

4. 🟡 For $Cu\ |\ Cu^{2+}\ ||\ Ag^+\ |\ Ag$, $E^\circ_{cell} = 0.46\ V$. If the standard *oxidation* potential of Cu is $-0.34\ V$, find the standard *reduction* potential of Ag.
<details><summary><b>Answer</b></summary>
Oxidation potential of Cu = $-0.34\ V \implies$ Reduction potential $E^\circ_{Cu} = +0.34\ V$.
$0.46 = E^\circ_{Ag} - 0.34$
$E^\circ_{Ag} = 0.46 + 0.34 = \textbf{+0.80\ V}$.
</details>

---

### Type 6: Extensive Properties and Max Work (Preview) ⭐

**Pattern:** "Understanding the relationship between intensive EMF and extensive properties like energy/work."

**Solved Example** 🔴
> Two students calculate the $E^\circ_{cell}$ for $Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$. Student A uses the equation as written and gets $1.10\ V$. Student B multiplies the equation by 2: $2Zn + 2Cu^{2+} \rightarrow 2Zn^{2+} + 2Cu$. What $E^\circ_{cell}$ does Student B get, and will the maximum work extracted from both cells be the same?

<details><summary><b>Solution</b></summary>
- EMF is an intensive property. It does not depend on stoichiometry. Student B also gets **$1.10\ V$**.
- However, Work (Energy) is an *extensive* property. Student B's reaction transfers twice as many electrons (4 moles instead of 2 moles). Therefore, a battery running Student B's reaction contains twice as much fuel and will do **twice as much maximum work**.
</details>

**Practice:**

1. 🟡 If you connect two identical $1.5\ V$ batteries in parallel (side-by-side), what is the EMF of the combination? What if you connect them in series (end-to-end)?
<details><summary><b>Answer</b></summary>
- Parallel: EMF remains **$1.5\ V$** (intensive nature; you just have a larger "pool" of chemicals, so it lasts longer).
- Series: EMF adds up to **$3.0\ V$** (you are stacking the potential differences).
</details>

2. 🔴 $E^\circ$ for $Ag^+ + e^- \rightarrow Ag$ is $0.80\ V$. $E^\circ$ for $Cu^{2+} + 2e^- \rightarrow Cu$ is $0.34\ V$. Why can we directly subtract $0.80 - 0.34$ to get the cell potential for $Cu + 2Ag^+ \rightarrow Cu^{2+} + 2Ag$, even though 2 moles of Ag are involved?
<details><summary><b>Answer</b></summary>
Because $E^\circ$ values represent the potential difference per unit charge. Just like temperature doesn't double if you have two cups of boiling water, the potential difference of the Ag half-cell doesn't double just because 2 moles are reacting. The intensive $E^\circ$ values can be directly added/subtracted.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1. (NCERT Type)** 🟢 The standard EMF of a Galvanic cell involving cell reaction with $n = 2$ is found to be $0.295\ V$ at $25^\circ C$. The equilibrium constant of the reaction would be... Wait, no, just purely EMF concept: The standard EMF of a cell is determined by:
(a) $E^\circ_{anode} + E^\circ_{cathode}$
(b) $E^\circ_{cathode} - E^\circ_{anode}$
(c) $E^\circ_{anode} - E^\circ_{cathode}$
(d) $\frac{E^\circ_{cathode}}{E^\circ_{anode}}$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
Assuming both are reduction potentials, it is always Cathode minus Anode.
</details>

**Q2. (Board Type)** 🟡 Which of the following statements about EMF and Potential Difference is true?
(a) Potential difference is responsible for the steady flow of current; EMF is measured when current is flowing.
(b) EMF is the maximum voltage a cell can deliver; Potential difference is the voltage measured across a closed circuit.
(c) Both are exactly the same thing.
(d) EMF depends on internal resistance, but potential difference does not.

<details><summary><b>Answer</b></summary>
**Answer: (b)**
EMF is measured in an open circuit (max voltage). Potential difference is measured in a closed circuit and is always less than EMF due to internal resistance drop.
</details>

**Q3. (JEE Mains Type)** 🔴 Given the standard electrode potentials: 
$K^+/K = -2.93\ V, Ag^+/Ag = 0.80\ V, Hg^{2+}/Hg = 0.79\ V, Mg^{2+}/Mg = -2.37\ V, Cr^{3+}/Cr = -0.74\ V$. 
Which of the following cells will yield the maximum standard EMF?
(a) $Mg\ |\ Mg^{2+}\ ||\ Ag^+\ |\ Ag$
(b) $K\ |\ K^+\ ||\ Ag^+\ |\ Ag$
(c) $Mg\ |\ Mg^{2+}\ ||\ Hg^{2+}\ |\ Hg$
(d) $K\ |\ K^+\ ||\ Cr^{3+}\ |\ Cr$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
To get maximum EMF, you want the largest possible difference between the Cathode and Anode.
You need the highest possible $E^\circ_{cathode}$ and the lowest possible (most negative) $E^\circ_{anode}$.
Highest is $Ag$ ($+0.80\ V$). Lowest is $K$ ($-2.93\ V$).
$E^\circ_{cell} = 0.80 - (-2.93) = \textbf{+3.73\ V}$.
</details>

**Q4. (Exemplar Type)** 🟡 A cell is represented by $Zn\ |\ Zn^{2+}(aq)\ ||\ Cu^{2+}(aq)\ |\ Cu$. Given $E^\circ_{Zn} = -0.76\ V$ and $E^\circ_{Cu} = 0.34\ V$. If the concentration of both $Zn^{2+}$ and $Cu^{2+}$ is changed from $1\ M$ to $0.1\ M$, what happens to the standard EMF ($E^\circ$)?
(a) It increases.
(b) It decreases.
(c) It remains the same.
(d) The cell stops functioning.

<details><summary><b>Answer</b></summary>
**Answer: (c)**
Trick question! The *Standard* EMF ($E^\circ$) is a fixed constant value defined strictly at $1\ M$ concentration. It does not change. What changes is the *actual operating EMF* ($E_{cell}$) as given by the Nernst equation (which we will see in the next chapter).
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🟡 ⭐ Consider three metals X, Y, and Z. 
- X displaces Y from its salt solution.
- Z displaces X from its salt solution.
(a) Arrange them in increasing order of their standard reduction potentials.
(b) If you want to construct a Galvanic cell with the maximum possible EMF using two of these metals, which will act as the anode and which as the cathode?

<details><summary><b>Solution</b></summary>
(a) X displaces Y $\implies$ X is a stronger reducing agent $\implies E^\circ_X < E^\circ_Y$.
Z displaces X $\implies$ Z is a stronger reducing agent $\implies E^\circ_Z < E^\circ_X$.
Therefore, $E^\circ_Z < E^\circ_X < E^\circ_Y$.
Increasing order: **Z < X < Y**.
(b) Max EMF requires the largest difference. You must pair the lowest potential (Z) with the highest potential (Y).
Anode (lowest $E^\circ$): **Z**.
Cathode (highest $E^\circ$): **Y**.
</details>

**Q2.** 🔴 Given $E^\circ_{Fe^{3+}/Fe^{2+}} = +0.77\ V$ and $E^\circ_{Fe^{2+}/Fe} = -0.44\ V$. 
A student attempts to calculate $E^\circ$ for $Fe^{3+} \rightarrow Fe$ by simply adding the two potentials: $0.77 + (-0.44) = +0.33\ V$. Is this correct? Why or why not?

<details><summary><b>Solution</b></summary>
**No, this is completely incorrect.**
You can only directly add or subtract $E^\circ$ values if the final reaction does *not* involve free electrons (i.e., combining two half-reactions to make a full cell reaction).
Here, the student is combining two half-reactions to make a *third half-reaction* ($Fe^{3+} + 3e^- \rightarrow Fe$). Because the number of electrons changes, you cannot simply add the intensive voltages. You must convert them to extensive free energies ($\Delta G^\circ = -nFE^\circ$), add the free energies, and then convert back. (We will master this in Chapter 10).
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Write the formula to calculate the standard EMF of a cell. *(1 mark)*
<details><summary><b>Model Answer</b></summary>
$E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$ (where both are standard reduction potentials).
</details>

**Q2.** 🟡 Differentiate between EMF and Potential Difference. *(2 marks)*
<details><summary><b>Model Answer</b></summary>
| EMF (Electromotive Force) | Potential Difference |
| :--- | :--- |
| It is the potential difference when no current is drawn (open circuit). | It is the potential difference when current is flowing (closed circuit). |
| It is the maximum voltage a cell can deliver. | It is always less than the EMF. |
| Measured accurately by a potentiometer. | Measured by a voltmeter. |
</details>

**Q3.** 🟡 A cell is formed by dipping a Zinc rod in $ZnSO_4$ and a Silver rod in $AgNO_3$. Which electrode will act as the cathode? Justify. ($E^\circ_{Zn} = -0.76\ V, E^\circ_{Ag} = +0.80\ V$). *(2 marks)*
<details><summary><b>Model Answer</b></summary>
The **Silver rod** will act as the cathode. This is because Silver has a higher standard reduction potential ($+0.80\ V$) than Zinc ($-0.76\ V$), meaning it has a greater tendency to get reduced (gain electrons).
</details>

**Q4.** 🟢 What is the condition for a cell reaction to be spontaneous in terms of standard EMF? *(1 mark)*
<details><summary><b>Model Answer</b></summary>
The standard EMF ($E^\circ_{cell}$) must be positive ($E^\circ_{cell} > 0$).
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🔴 ⭐ For the cell $Tl\ |\ Tl^+(0.001\ M)\ ||\ Cu^{2+}(0.1\ M)\ |\ Cu$, $E_{cell}$ at 298 K is $0.83\ V$. If the EMF of the cell can be increased by:
(a) Increasing $[Tl^+]$
(b) Decreasing $[Cu^{2+}]$
(c) Increasing $[Tl^+]$ and decreasing $[Cu^{2+}]$
(d) Decreasing $[Tl^+]$ and increasing $[Cu^{2+}]$

<details><summary><b>Answer</b></summary>
**Answer: (d)**
Cell Reaction: $2Tl + Cu^{2+} \rightarrow 2Tl^+ + Cu$.
According to Le Chatelier's principle (and Nernst equation), to drive the reaction forward (increase the driving force/EMF), you must increase the concentration of reactants ($Cu^{2+}$) and decrease the concentration of products ($Tl^+$).
</details>

**Q2.** 🔴 The standard potentials for two half-cells are given:
$Fe^{2+} + 2e^- \rightarrow Fe \quad E^\circ = -0.44\ V$
$Fe^{3+} + e^- \rightarrow Fe^{2+} \quad E^\circ = +0.77\ V$
Determine the standard EMF for the cell reaction: $2Fe^{3+} + Fe \rightarrow 3Fe^{2+}$
(a) $+0.33\ V$
(b) $+1.21\ V$
(c) $+1.98\ V$
(d) $+1.54\ V$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
The cell reaction is: $Fe + 2Fe^{3+} \rightarrow 3Fe^{2+}$.
Anode (Oxidation of Fe): $Fe \rightarrow Fe^{2+} + 2e^-$. $E^\circ_{anode} = -0.44\ V$.
Cathode (Reduction of Fe3+): $2Fe^{3+} + 2e^- \rightarrow 2Fe^{2+}$. $E^\circ_{cathode} = +0.77\ V$.
$E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$
$E^\circ_{cell} = 0.77 - (-0.44) = 0.77 + 0.44 = \textbf{+1.21\ V}$.
*(Notice we did NOT multiply the 0.77 by 2, because EMF is intensive. Also, this is a full cell reaction (no free electrons), so we CAN use $E_{cathode} - E_{anode}$ directly).*
</details>

---

*Next: [Chapter 7 — The Nernst Equation (Single Electrode) →](./07_nernst_equation_single.md)*
