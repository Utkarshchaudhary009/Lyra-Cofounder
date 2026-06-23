# Chapter 8: The Nernst Equation (Complete Cell) — The Dying Battery

> *NCERT Sections 3.2.1*

---

## 🎯 Stage 1: The Core Idea

### Why Batteries Die
When you buy a brand new standard Daniell cell, its EMF is $1.10\ V$. But as you use it to power a bulb, the voltage slowly drops. Why?<br>
As the battery runs, the chemical reaction ($Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$) moves forward. 
- The reactant ($Cu^{2+}$) gets used up $\rightarrow$ Its concentration decreases.
- The product ($Zn^{2+}$) is created $\rightarrow$ Its concentration increases.

From Chapter 7, we know that diluting reactants lowers potential, and packing in products increases opposition. The combination of these two factors steadily strangles the cell's driving force. The **Nernst Equation for a Complete Cell** calculates exactly what the voltage ($E_{cell}$) is at any given moment based on the changing concentrations. 
Eventually, the voltage hits exactly **$0.00\ V$**. At this point, the forward and backward pulls are perfectly balanced. The battery is dead. We call this state **Equilibrium**.

---

## 🔬 Stage 2: The Formula Lab

### The Full Cell Equation
For a general balanced overall cell reaction:
$$ aA + bB \rightarrow cC + dD $$

The Nernst Equation at $298\ K$ is:
$$ E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log Q $$

Where:
- **$E^\circ_{cell}$** = Standard EMF ($E^\circ_{cathode} - E^\circ_{anode}$).
- **$n$** = **Total** number of moles of electrons transferred in the *balanced* equation.
- **$Q$** = Reaction Quotient = $\frac{[\text{Products}]^{\text{coefficients}}}{[\text{Reactants}]^{\text{coefficients}}}$. (Remember: Solid metals are omitted / taken as 1).

### The "Anode over Cathode" Shortcut
For standard metal-metal ion cells, the metal that oxidizes (Anode) becomes an aqueous product, and the metal that reduces (Cathode) is an aqueous reactant. 
So the formula often simplifies to:
$$ E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log \frac{[\text{Anode Ion}]^x}{[\text{Cathode Ion}]^y} $$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Finding 'n' and writing 'Q' for Full Cells ⭐

**Pattern:** "The hardest part of full-cell Nernst is setting it up. You must balance the electrons to find $n$ and write the correct powers for $Q$."

**Solved Example** 🟢
> Write the Nernst equation expression for the cell: $Al\ |\ Al^{3+}(aq)\ ||\ Cu^{2+}(aq)\ |\ Cu$.

<details><summary><b>Solution</b></summary>
- Anode (Oxidation): $Al \rightarrow Al^{3+} + 3e^-$
- Cathode (Reduction): $Cu^{2+} + 2e^- \rightarrow Cu$
- To balance electrons, multiply Anode by 2 and Cathode by 3.
  $2Al \rightarrow 2Al^{3+} + 6e^-$
  $3Cu^{2+} + 6e^- \rightarrow 3Cu$
- **$n = 6$**.
- Overall Reaction: $2Al + 3Cu^{2+} \rightarrow 2Al^{3+} + 3Cu$
- Products are $Al^{3+}$, Reactants are $Cu^{2+}$. 
- Expression: **$E_{cell} = E^\circ_{cell} - \frac{0.0591}{6} \log \frac{[Al^{3+}]^2}{[Cu^{2+}]^3}$**
</details>

**Practice:**

1. 🟢 Write the Nernst expression for $Zn\ |\ Zn^{2+}\ ||\ Ag^+\ |\ Ag$. What is $n$?<br>
<details><summary><b>Answer</b></summary>
$Zn \rightarrow Zn^{2+} + 2e^-$. $2Ag^+ + 2e^- \rightarrow 2Ag$. **$n = 2$**.
Expression: **$E = E^\circ - \frac{0.0591}{2} \log \frac{[Zn^{2+}]}{[Ag^+]^2}$**.
</details>

2. 🟢 Write the Nernst expression for $Fe\ |\ Fe^{2+}\ ||\ Pb^{2+}\ |\ Pb$. What is $n$?<br>
<details><summary><b>Answer</b></summary>
Both are divalent. $n = 2$.
Expression: **$E = E^\circ - \frac{0.0591}{2} \log \frac{[Fe^{2+}]}{[Pb^{2+}]}$**.
</details>

3. 🟡 Write the Nernst expression for $Cr\ |\ Cr^{3+}\ ||\ Fe^{2+}\ |\ Fe$. What is $n$?<br>
<details><summary><b>Answer</b></summary>
$Cr \rightarrow Cr^{3+} + 3e^-$ (multiply by 2). $Fe^{2+} + 2e^- \rightarrow Fe$ (multiply by 3). **$n = 6$**.
Expression: **$E = E^\circ - \frac{0.0591}{6} \log \frac{[Cr^{3+}]^2}{[Fe^{2+}]^3}$**.
</details>

4. 🟡 A cell reaction is $H_2(g, 1\ atm) + 2Ag^+(aq) \rightarrow 2H^+(aq) + 2Ag(s)$. What is the $Q$ expression?<br>
<details><summary><b>Answer</b></summary>
Products: $H^+$. Reactants: $Ag^+$, $H_2$.
$Q = \frac{[H^+]^2}{[Ag^+]^2 \cdot P_{H_2}}$. Since $P_{H_2} = 1\ atm$, it is **$\frac{[H^+]^2}{[Ag^+]^2}$**.
</details>

5. 🔴 Find $n$ and $Q$ for $Pt\ |\ Sn^{2+}, Sn^{4+}\ ||\ MnO_4^-, Mn^{2+}, H^+\ |\ Pt$.
<details><summary><b>Answer</b></summary>
Anode: $Sn^{2+} \rightarrow Sn^{4+} + 2e^-$ (multiply by 5).
Cathode: $MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O$ (multiply by 2).
**$n = 10$**.
Overall: $5Sn^{2+} + 2MnO_4^- + 16H^+ \rightarrow 5Sn^{4+} + 2Mn^{2+} + 8H_2O$.
**$Q = \frac{[Sn^{4+}]^5 [Mn^{2+}]^2}{[Sn^{2+}]^5 [MnO_4^-]^2 [H^+]^{16}}$**.
</details>

---

### Type 2: Simple $E_{cell}$ Calculation ($n_{anode} = n_{cathode}$) ⭐

**Pattern:** "Calculating voltage when both metals have the same valency."

**Solved Example** 🟡
> Calculate the EMF of the cell at $298\ K$: 
> $Mg(s)\ |\ Mg^{2+}(0.1\ M)\ ||\ Cu^{2+}(1 \times 10^{-3}\ M)\ |\ Cu(s)$
> Given $E^\circ_{Mg} = -2.37\ V, E^\circ_{Cu} = +0.34\ V$.

<details><summary><b>Solution</b></summary>
- Step 1: Calculate $E^\circ_{cell} = E^\circ_{R} - E^\circ_{L} = 0.34 - (-2.37) = +2.71\ V$.
- Step 2: Identify $n$. $Mg \rightarrow Mg^{2+} + 2e^-$, $Cu^{2+} + 2e^- \rightarrow Cu$. $n = 2$.
- Step 3: Nernst Eq.
  $E_{cell} = 2.71 - \frac{0.0591}{2} \log \frac{[Mg^{2+}]}{[Cu^{2+}]}$
  $E_{cell} = 2.71 - 0.0295 \log \frac{10^{-1}}{10^{-3}}$
  $E_{cell} = 2.71 - 0.0295 \log(10^2) = 2.71 - 0.0295(2) = 2.71 - 0.059$
- **$E_{cell} = +2.651\ V$**.
</details>

**Practice:**

1. 🟢 Calculate $E_{cell}$ for $Zn\ |\ Zn^{2+}(0.01\ M)\ ||\ Cu^{2+}(0.1\ M)\ |\ Cu$. ($E^\circ_{cell} = 1.10\ V$).
<details><summary><b>Answer</b></summary>
$E_{cell} = 1.10 - \frac{0.0591}{2} \log \frac{0.01}{0.1} = 1.10 - 0.0295 \log(10^{-1})$
$E_{cell} = 1.10 - 0.0295(-1) = 1.10 + 0.0295 = \textbf{+1.1295\ V}$.
</details>

2. 🟢 Given $E^\circ_{cell} = 0.59\ V$ for $Fe\ |\ Fe^{2+}(0.1\ M)\ ||\ Ni^{2+}(0.1\ M)\ |\ Ni$. Without calculating, what is $E_{cell}$?<br>
<details><summary><b>Answer</b></summary>
Since both concentrations are equal ($0.1\ M$) and $n$ is the same, the ratio is $0.1 / 0.1 = 1$.
$\log(1) = 0$. The whole term drops out. $E_{cell} = E^\circ_{cell} = \textbf{0.59\ V}$.
</details>

3. 🟡 For $Zn\ |\ Zn^{2+}(0.001\ M)\ ||\ Cd^{2+}(0.1\ M)\ |\ Cd$, $E^\circ_{cell} = 0.36\ V$. Find $E_{cell}$.
<details><summary><b>Answer</b></summary>
$E_{cell} = 0.36 - \frac{0.0591}{2} \log \frac{10^{-3}}{10^{-1}} = 0.36 - 0.0295 \log(10^{-2})$
$E_{cell} = 0.36 - 0.0295(-2) = 0.36 + 0.059 = \textbf{+0.419\ V}$.
</details>

4. 🟡 A cell $A\ |\ A^{2+}(10^{-4}\ M)\ ||\ B^{2+}(10^{-2}\ M)\ |\ B$ has $E_{cell} = 1.00\ V$. What is $E^\circ_{cell}$?<br>
<details><summary><b>Answer</b></summary>
$1.00 = E^\circ_{cell} - \frac{0.0591}{2} \log \frac{10^{-4}}{10^{-2}}$
$1.00 = E^\circ_{cell} - 0.0295 \log(10^{-2}) = E^\circ_{cell} + 0.059$
$E^\circ_{cell} = 1.00 - 0.059 = \textbf{+0.941\ V}$.
</details>

5. 🔴 Consider $Pb\ |\ Pb^{2+}(C_1)\ ||\ Cu^{2+}(C_2)\ |\ Cu$. If you increase both $C_1$ and $C_2$ by a factor of 10, how much does $E_{cell}$ change?<br>
<details><summary><b>Answer</b></summary>
Ratio is $\frac{C_1}{C_2}$. If both are multiplied by 10, the new ratio is $\frac{10 \times C_1}{10 \times C_2} = \frac{C_1}{C_2}$. The ratio does not change.
Therefore, the $E_{cell}$ **does not change at all**.
</details>

---

### Type 3: Complex $E_{cell}$ Calculation ($n_{anode} \neq n_{cathode}$) ⭐

**Pattern:** "The classic mistake zone. You must remember to raise concentrations to their stoichiometric powers."

**Solved Example** 🔴
> Calculate the EMF of the cell at $298\ K$:
> $Mg\ |\ Mg^{2+}(0.130\ M)\ ||\ Ag^+(0.0001\ M)\ |\ Ag$
> Given $E^\circ_{Mg} = -2.37\ V, E^\circ_{Ag} = +0.80\ V$.

<details><summary><b>Solution</b></summary>
- Step 1: $E^\circ_{cell} = 0.80 - (-2.37) = +3.17\ V$.
- Step 2: Find $n$ and $Q$.
  Reaction: $Mg + 2Ag^+ \rightarrow Mg^{2+} + 2Ag$. 
  $n = 2$.
  $Q = \frac{[Mg^{2+}]}{[Ag^+]^2}$ $\leftarrow$ **CRITICAL STEP: Ag+ must be squared!**
- Step 3: Nernst Eq.
  $E = 3.17 - \frac{0.0591}{2} \log \frac{0.130}{(10^{-4})^2}$
  $E = 3.17 - 0.0295 \log \frac{0.130}{10^{-8}} = 3.17 - 0.0295 \log(1.3 \times 10^7)$
  $\log(1.3 \times 10^7) = \log(1.3) + 7 \approx 0.11 + 7 = 7.11$.
  $E = 3.17 - 0.0295(7.11) = 3.17 - 0.21 = \textbf{+2.96\ V}$.
</details>

**Practice:**

1. 🟡 Write the Nernst equation with substituted values for $Ni\ |\ Ni^{2+}(0.1\ M)\ ||\ Ag^+(0.1\ M)\ |\ Ag$. ($E^\circ_{cell} = 1.05\ V$).
<details><summary><b>Answer</b></summary>
$E = 1.05 - \frac{0.0591}{2} \log \frac{0.1}{(0.1)^2}$
</details>

2. 🟡 Evaluate the previous expression to find $E_{cell}$.
<details><summary><b>Answer</b></summary>
$E = 1.05 - 0.0295 \log \frac{0.1}{0.01} = 1.05 - 0.0295 \log(10) = 1.05 - 0.0295 = \textbf{+1.0205\ V}$.
</details>

3. 🔴 For the cell $Al\ |\ Al^{3+}(0.01\ M)\ ||\ Cu^{2+}(0.1\ M)\ |\ Cu$, $E^\circ_{cell} = 2.00\ V$. Find $E_{cell}$.
<details><summary><b>Answer</b></summary>
Reaction: $2Al + 3Cu^{2+} \rightarrow 2Al^{3+} + 3Cu$. $n = 6$.
$E = 2.00 - \frac{0.0591}{6} \log \frac{[Al^{3+}]^2}{[Cu^{2+}]^3}$
$E = 2.00 - 0.00985 \log \frac{(10^{-2})^2}{(10^{-1})^3} = 2.00 - 0.00985 \log \frac{10^{-4}}{10^{-3}}$
$E = 2.00 - 0.00985 \log(10^{-1}) = 2.00 - 0.00985(-1) = \textbf{+2.00985\ V}$.
</details>

4. 🔴 A cell is $Pt\ |\ H_2(1\ atm)\ |\ H^+(pH = 3)\ ||\ Ag^+(0.01\ M)\ |\ Ag$. $E^\circ_{Ag} = 0.80\ V$. Find $E_{cell}$.
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = 0.80 - 0.00 = 0.80\ V$.
Reaction: $H_2 + 2Ag^+ \rightarrow 2H^+ + 2Ag$. $n = 2$.
$[H^+] = 10^{-3}\ M$. $[Ag^+] = 10^{-2}\ M$.
$E = 0.80 - \frac{0.0591}{2} \log \frac{(10^{-3})^2}{(10^{-2})^2} = 0.80 - 0.0295 \log \frac{10^{-6}}{10^{-4}}$
$E = 0.80 - 0.0295 \log(10^{-2}) = 0.80 - 0.0295(-2) = 0.80 + 0.059 = \textbf{+0.859\ V}$.
</details>

5. 🔴 In the $Mg/Ag^+$ cell from the solved example, what happens to the potential if we multiply the stoichiometric equation by 2?<br>
<details><summary><b>Answer</b></summary>
$n$ doubles (from 2 to 4). The powers in the log term double (squaring the fraction). 
$E_{cell} = E^\circ_{cell} - \frac{0.0591}{4} \log \left(\frac{[Mg^{2+}]}{[Ag^+]^2}\right)^2$
By log rules, the squared power comes down: $\frac{2 \times 0.0591}{4} \log(Q) = \frac{0.0591}{2} \log(Q)$.
It returns to the exact same formula. The potential **remains completely unchanged**.
</details>

---

### Type 4: Concentration Cells ⭐

**Pattern:** "Using the exact same metal on both sides. $E^\circ_{cell}$ is zero, but the cell still works because of a concentration difference."

**Solved Example** 🟡
> Calculate the EMF of the cell: $Cu\ |\ Cu^{2+}(0.01\ M)\ ||\ Cu^{2+}(0.1\ M)\ |\ Cu$.

<details><summary><b>Solution</b></summary>
- This is a concentration cell. Since both electrodes are Copper, $E^\circ_{cell} = E^\circ_{Cu} - E^\circ_{Cu} = \textbf{0.00\ V}$.
- $n = 2$.
- The Nernst equation becomes: $E_{cell} = 0 - \frac{0.0591}{2} \log \frac{[\text{Anode Ion}]}{[\text{Cathode Ion}]}$
- $E_{cell} = -0.0295 \log \frac{0.01}{0.1} = -0.0295 \log(10^{-1}) = -0.0295(-1) = \textbf{+0.0295\ V}$.
*(The cell works! Electrons flow from the dilute side to the concentrated side until concentrations are equal).*
</details>

**Practice:**

1. 🟢 For a concentration cell to be spontaneous ($E_{cell} > 0$), must the Anode concentration be higher or lower than the Cathode concentration?<br>
<details><summary><b>Answer</b></summary>
From $E_{cell} = - \frac{0.0591}{n} \log \frac{C_{anode}}{C_{cathode}}$, to make $E_{cell}$ positive, the log term must be negative. This happens when the fraction is $< 1$. Therefore, **Anode concentration must be lower** than Cathode concentration. ($C_1 < C_2$).
</details>

2. 🟢 Calculate EMF of $Zn\ |\ Zn^{2+}(0.1\ M)\ ||\ Zn^{2+}(0.1\ M)\ |\ Zn$.
<details><summary><b>Answer</b></summary>
Concentrations are equal. The system is already at equilibrium. $E_{cell} = \textbf{0.00\ V}$.
</details>

3. 🟡 Calculate EMF of $Ag\ |\ Ag^+(0.001\ M)\ ||\ Ag^+(0.1\ M)\ |\ Ag$.
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = 0$. $n = 1$.
$E_{cell} = -0.0591 \log \frac{0.001}{0.1} = -0.0591 \log(10^{-2}) = -0.0591(-2) = \textbf{+0.1182\ V}$.
</details>

4. 🟡 A concentration cell $H_2(1\ atm)\ |\ H^+(pH = x)\ ||\ H^+(pH = y)\ |\ H_2(1\ atm)$ generates voltage. In which compartment is the pH higher?<br>
<details><summary><b>Answer</b></summary>
For a spontaneous cell, Anode concentration must be lower than Cathode concentration.
$[H^+]_{anode} < [H^+]_{cathode}$.
Since pH is the negative log, a lower concentration means a higher pH. 
Therefore, the **Anode compartment has the higher pH** ($x > y$).
</details>

5. 🔴 Given $H_2(P_1\ atm)\ |\ H^+(1\ M)\ ||\ H^+(1\ M)\ |\ H_2(P_2\ atm)$. This is a gas concentration cell. For this cell to be spontaneous, what must be the relation between $P_1$ and $P_2$?<br>
<details><summary><b>Answer</b></summary>
Reaction: $H_2(P_1) + 2H^+(1M) \rightarrow 2H^+(1M) + H_2(P_2)$.
Net reaction: $H_2(P_1) \rightarrow H_2(P_2)$.
$Q = \frac{P_2}{P_1}$.
$E_{cell} = - \frac{0.0591}{2} \log \frac{P_2}{P_1}$.
To make $E$ positive, $\frac{P_2}{P_1} < 1$, which means **$P_1 > P_2$**. Gas flows from high pressure to low pressure.
</details>

---

### Type 5: Predicting Change in EMF (Le Chatelier) ⭐

**Pattern:** "Using qualitative logic to predict if $E_{cell}$ increases or decreases when you mess with the beakers."

**Solved Example** 🟡
> Consider a standard Daniell cell ($Zn/Cu$). What happens to the EMF of the cell if you dissolve some solid $ZnSO_4$ into the anode compartment?<br>

<details><summary><b>Solution</b></summary>
- Reaction: $Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$.
- Adding $ZnSO_4$ increases the concentration of $Zn^{2+}$ (a product).
- According to Le Chatelier's principle, adding a product shifts the equilibrium backward, opposing the spontaneous reaction.
- Therefore, the driving force of the cell drops. The **EMF will decrease**.
*(Mathematically: In $E = E^\circ - \text{const} \times \log[Zn^{2+}]/[Cu^{2+}]$, increasing the numerator increases the subtracted term, lowering E).*
</details>

**Practice:**

1. 🟢 In a $Zn/Cu$ cell, what happens to EMF if you add water to the Cathode ($Cu$) compartment?<br>
<details><summary><b>Answer</b></summary>
Adding water dilutes the $Cu^{2+}$ ions (reactant). Decreasing reactant shifts equilibrium backward. **EMF decreases**.
</details>

2. 🟢 In a $Zn/Cu$ cell, what happens to EMF if you add water to the Anode ($Zn$) compartment?<br>
<details><summary><b>Answer</b></summary>
Adding water dilutes the $Zn^{2+}$ ions (product). Decreasing product shifts equilibrium forward. **EMF increases**.
</details>

3. 🟡 If you add ammonia ($NH_3$) to the cathode compartment of a $Zn/Cu$ cell, $NH_3$ forms a complex with $Cu^{2+}$, effectively removing free $Cu^{2+}$ ions from the solution. What happens to the cell EMF?<br>
<details><summary><b>Answer</b></summary>
Removing free $Cu^{2+}$ (a reactant) decreases its concentration. This shifts the equilibrium backward. **EMF decreases drastically**.
</details>

4. 🟡 For the cell $Fe\ |\ Fe^{2+}\ ||\ Ag^+\ |\ Ag$, what is the effect on EMF if the size of the Silver electrode is doubled?<br>
<details><summary><b>Answer</b></summary>
Solid metals do not appear in the Nernst equation ($[Ag(s)] = 1$). Changing the size or mass of the electrodes **has no effect on the EMF**. (It only increases the cell's physical capacity/lifespan).
</details>

5. 🔴 A cell consists of $SHE\ ||\ Ag^+(1\ M)\ |\ Ag$. If you bubble $H_2S$ gas into the cathode compartment, it precipitates out $Ag_2S$. What happens to the cell voltage?<br>
<details><summary><b>Answer</b></summary>
Precipitating $Ag^+$ removes the reactant ions from the solution, massively dropping $[Ag^+]$. This shifts the equilibrium backward. The **cell voltage decreases**.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1. (NCERT Type)** 🟢 The cell reaction of a cell is $Mg(s) + Cu^{2+}(aq) \rightarrow Mg^{2+}(aq) + Cu(s)$. If the standard EMF of the cell is $2.71\ V$, the EMF of the cell when $[Mg^{2+}] = 0.1\ M$ and $[Cu^{2+}] = 0.01\ M$ is:
(a) $2.71 - \frac{0.0591}{2} \log(10)$
(b) $2.71 + \frac{0.0591}{2} \log(10)$
(c) $2.71 - \frac{0.0591}{2} \log(0.1)$
(d) $2.71 + \frac{0.0591}{2} \log(0.1)$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
$Q = \frac{[Mg^{2+}]}{[Cu^{2+}]} = \frac{0.1}{0.01} = 10$.
$E = E^\circ - \frac{0.0591}{2} \log(Q) = 2.71 - \frac{0.0591}{2} \log(10)$.
</details>

**Q2. (JEE Mains Type)** 🔴 For the cell $Zn\ |\ Zn^{2+}(aq)\ ||\ Cu^{2+}(aq)\ |\ Cu$, $E_{cell}$ is $1.10\ V$ when $[Zn^{2+}] = [Cu^{2+}] = 1\ M$. If $[Cu^{2+}]$ is increased to $10\ M$, the $E_{cell}$:
(a) Increases by $0.0591\ V$
(b) Decreases by $0.0591\ V$
(c) Increases by $0.0295\ V$
(d) Decreases by $0.0295\ V$

<details><summary><b>Answer</b></summary>
**Answer: (c)**
$E = 1.10 - \frac{0.0591}{2} \log \frac{1}{10} = 1.10 - 0.0295 \log(10^{-1}) = 1.10 + 0.0295$.
It increases by exactly $0.0295\ V$.
</details>

**Q3. (Exemplar Type)** 🟡 In a concentration cell involving the same metal and metal ions, the cell potential is zero when:
(a) The cell is at $298\ K$
(b) Concentration of metal ions is $1\ M$ in both half-cells
(c) Concentration of metal ions in both half-cells are exactly equal
(d) The metal is standard hydrogen electrode

<details><summary><b>Answer</b></summary>
**Answer: (c)**
When $C_{anode} = C_{cathode}$, the ratio is 1, and $\log(1) = 0$, making $E_{cell} = 0$. (It doesn't have to be exactly $1\ M$, any equal concentration results in 0 V).
</details>

**Q4. (Subtle Detail)** 🔴 As a Galvanic cell operates and discharges, its $E_{cell}$ value:
(a) Remains constant until the limiting reactant is completely zero.
(b) Decreases logarithmically until it reaches $E^\circ_{cell}$.
(c) Decreases logarithmically until it reaches zero.
(d) Increases due to product formation.

<details><summary><b>Answer</b></summary>
**Answer: (c)**
As products form and reactants deplete, $Q$ increases. As $Q$ increases, $\log Q$ increases, so a larger value is subtracted from $E^\circ_{cell}$. $E_{cell}$ drops until it hits 0 V (equilibrium/dead battery).
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🟡 ⭐ A cell is constructed: $Ag\ |\ Ag^+(0.1\ M)\ ||\ Ag^+(x\ M)\ |\ Ag$. If the measured cell potential is $0.0591\ V$ at $298\ K$, calculate the unknown concentration $x$. Is the right compartment the anode or the cathode?<br>

<details><summary><b>Solution</b></summary>
- Since it's written in standard notation, Right is Cathode. (To verify: $E_{cell}$ is positive, so the standard setup is spontaneous. Yes, Right is Cathode).
- $E^\circ = 0$, $n = 1$.
- $E = -0.0591 \log \frac{[\text{Anode}]}{[\text{Cathode}]} = -0.0591 \log \frac{0.1}{x}$
- $0.0591 = -0.0591 \log \frac{0.1}{x}$
- $-1 = \log \frac{0.1}{x} \implies 10^{-1} = \frac{0.1}{x} \implies 0.1 = \frac{0.1}{x}$
- $x = \textbf{1.0\ M}$.
</details>

**Q2.** 🔴 For $Sn\ |\ Sn^{2+}(0.1\ M)\ ||\ H^+(pH = 2)\ |\ H_2(1\ atm)\ |\ Pt$. Given $E^\circ_{Sn} = -0.14\ V$.
(a) Calculate $E^\circ_{cell}$.
(b) Calculate $E_{cell}$ at $298\ K$.
(c) Will the cell work as written?<br>

<details><summary><b>Solution</b></summary>
(a) $E^\circ_{cell} = E^\circ_{SHE} - E^\circ_{Sn} = 0.00 - (-0.14) = \textbf{+0.14\ V}$.
(b) Reaction: $Sn + 2H^+ \rightarrow Sn^{2+} + H_2$. $n=2$.
$[H^+] = 10^{-2}\ M$. $[Sn^{2+}] = 0.1 = 10^{-1}\ M$.
$E = 0.14 - \frac{0.0591}{2} \log \frac{[Sn^{2+}]}{[H^+]^2} = 0.14 - 0.0295 \log \frac{10^{-1}}{(10^{-2})^2}$
$E = 0.14 - 0.0295 \log \frac{10^{-1}}{10^{-4}} = 0.14 - 0.0295 \log(10^3)$
$E = 0.14 - 0.0295(3) = 0.14 - 0.0885 = \textbf{+0.0515\ V}$.
(c) Yes, $E_{cell}$ is positive, so it **will work** (is spontaneous) as written.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Write the Nernst equation for the cell reaction: $aA + bB \rightarrow cC + dD$. *(1 mark)*
<details><summary><b>Model Answer</b></summary>
$E_{cell} = E^\circ_{cell} - \frac{2.303 RT}{nF} \log \frac{[C]^c [D]^d}{[A]^a [B]^b}$
</details>

**Q2.** 🟡 What is a concentration cell?<br> Give an example. *(2 marks)*
<details><summary><b>Model Answer</b></summary>
A Galvanic cell in which both the electrodes are made of the same material, but the concentrations of the electrolyte solutions in the two half-cells are different. 
Example: $Cu(s)\ |\ Cu^{2+}(0.1\ M)\ ||\ Cu^{2+}(1.0\ M)\ |\ Cu(s)$.
</details>

**Q3.** 🟡 Why does the voltage of a Galvanic cell drop to zero after some time?<br> *(2 marks)*
<details><summary><b>Model Answer</b></summary>
As the cell operates, reactants are consumed (decreasing their concentration) and products are formed (increasing their concentration). According to the Nernst equation, this causes a steady decrease in $E_{cell}$. Eventually, the system reaches chemical equilibrium, at which point the driving force is zero, and $E_{cell} = 0$.
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🔴 ⭐ An electrochemical cell is set up: $Pt\ |\ H_2(1\ atm)\ |\ HA(0.1\ M)\ ||\ HCl(0.1\ M)\ |\ H_2(1\ atm)\ |\ Pt$. The measured cell potential is $0.1182\ V$. What is the acid dissociation constant ($K_a$) of the weak acid HA?<br>
(a) $10^{-3}$
(b) $10^{-5}$
(c) $10^{-4}$
(d) $10^{-6}$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
This is a gas concentration cell. $E^\circ_{cell} = 0$. $n=2$.
Right side (Cathode): Strong acid HCl, fully dissociated. $[H^+]_C = 0.1\ M = 10^{-1}$.
Left side (Anode): Weak acid HA, partially dissociated. Let $[H^+]_A = x$.
$E_{cell} = - \frac{0.0591}{2} \log \frac{[H^+]_A^2}{[H^+]_C^2} = -0.0591 \log \frac{x}{10^{-1}}$.
$0.1182 = -0.0591 \log(10x)$
$-2 = \log(10x) \implies 10x = 10^{-2} \implies x = 10^{-3}\ M$.
So $[H^+]$ in the weak acid is $10^{-3}\ M$.
For a weak acid, $[H^+] \approx \sqrt{K_a \cdot C}$.
$10^{-3} = \sqrt{K_a \times 0.1}$
$10^{-6} = K_a \times 10^{-1} \implies K_a = \frac{10^{-6}}{10^{-1}} = \textbf{10^{-5}}$.
</details>

**Q2.** 🔴 For a cell reaction involving a two-electron transfer, the standard EMF is $0.295\ V$ at $25^\circ C$. If the concentrations of products are suddenly increased by a factor of 100, and reactants are kept standard, the new cell potential will be:
(a) $0.295\ V$
(b) $0.236\ V$
(c) $0.354\ V$
(d) $0.000\ V$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
$E^\circ = 0.295\ V$. $n=2$.
New $Q = \frac{100}{1} = 10^2$.
$E_{cell} = 0.295 - \frac{0.0591}{2} \log(10^2) = 0.295 - 0.0295(2) = 0.295 - 0.059 = \textbf{0.236\ V}$.
</details>

---

*Next: [Chapter 9 — Equilibrium Constant from Nernst Equation →](./09_equilibrium_constant.md)*
