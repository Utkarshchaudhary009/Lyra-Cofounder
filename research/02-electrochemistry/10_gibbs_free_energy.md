# Chapter 10: Gibbs Free Energy and Cell Potential

> *NCERT Section 3.2.3*

### The Paradox of Addition

Imagine you have two buckets of water. One is at $20^\circ C$, and the other is at $40^\circ C$. If you pour them together, does the combined water boil at $60^\circ C$?<br> Of course not. Temperature is an *intensive* property—it depends on the nature of the material, not the amount. You cannot simply add temperatures together.

Now imagine you are given the standard reduction potentials for two consecutive reactions of Iron:
1. $Fe^{3+} + e^- \rightarrow Fe^{2+} \quad (E^\circ_1 = +0.77\ V)$
2. $Fe^{2+} + 2e^- \rightarrow Fe \quad (E^\circ_2 = -0.44\ V)$

A student naturally assumes that to find the potential for the full reduction from $Fe^{3+}$ all the way down to solid $Fe$, they can just add the two voltages together: $0.77 + (-0.44) = +0.33\ V$. 

But if you run this experiment in a laboratory, the voltmeter reads **$-0.04\ V$**. The student's prediction is completely wrong. Why?<br> Because just like temperature, **Voltage (Potential) is an intensive property.** You cannot add or subtract voltages when you are merging half-reactions. 

To solve this paradox, we have to look past the "push" of the voltage and measure the actual, physical *work* being done. We have to look at energy.

---

### Building the Concept: The Invisible Hand of Work

Voltage is merely electrical pressure. By itself, pressure does no work unless it actually moves something. In electrochemistry, the "something" being moved is electrical charge. 

The total electrical work done by a Galvanic cell is equal to the total charge moved, multiplied by the electrical pressure pushing it.
$$ \text{Electrical Work} = \text{Total Charge} \times \text{Cell Potential} $$

If $n$ moles of electrons are transferred in a reaction, the total charge is $nF$ (where $F$ is Faraday's constant, roughly $96487\ C\ mol^{-1}$). Therefore, the maximum electrical work the cell can do is $nFE_{cell}$.

But where does this work come from?<br> It comes from the intrinsic chemical energy of the atoms themselves. In thermodynamics, the maximum non-expansion work that can be extracted from a closed system is defined as the decrease in its **Gibbs Free Energy ($\Delta G$)**. 

Since the system is losing this energy to do work *on* the surroundings, $\Delta G$ must be negative.
$$ \Delta G = -nFE_{cell} $$

If the cell is operating under standard conditions (1 M concentrations, 1 atm pressure, 298 K), we simply add the standard degree symbols:
$$ \Delta G^\circ = -nFE^\circ_{cell} $$

This equation is the holy grail of electrochemistry. It is the bridge that connects the measurable voltage of a battery ($E^\circ_{cell}$) to the fundamental laws of thermodynamics ($\Delta G^\circ$). Unlike voltage, **energy is an extensive property**. You *can* add and subtract energies.

---

### Checkpoint 1: Extracting Maximum Work

Let's test our understanding of this fundamental connection. To find the maximum work a battery can do, we must calculate its standard Gibbs free energy change.

**Problem 1:** Calculate the standard Gibbs free energy change and the maximum electrical work for the Daniell cell ($Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$), given $E^\circ_{cell} = 1.10\ V$ and $1\ F = 96487\ C\ mol^{-1}$.

<details><summary><b>Solution</b></summary>
The reaction involves the transfer of 2 electrons ($Zn \rightarrow Zn^{2+} + 2e^-$). Thus, $n = 2$.
$\Delta G^\circ = -nFE^\circ_{cell}$
$\Delta G^\circ = - (2\ mol) \times (96487\ C\ mol^{-1}) \times (1.10\ V)$
$\Delta G^\circ = - 212,271\ J = \textbf{-212.27\ kJ}$.
The maximum electrical work the cell can do is the magnitude of this energy decrease: **$212.27\ kJ$**.
</details>

**Problem 2:** A cell reaction is written as $2Al(s) + 3Cu^{2+}(aq) \rightarrow 2Al^{3+}(aq) + 3Cu(s)$ with $E^\circ_{cell} = 2.00\ V$. What is the $\Delta G^\circ$ for this reaction?<br> 
If a student writes the reaction as $Al(s) + \frac{3}{2}Cu^{2+}(aq) \rightarrow Al^{3+}(aq) + \frac{3}{2}Cu(s)$, does the $\Delta G^\circ$ change?<br> Does the $E^\circ_{cell}$ change?<br>

<details><summary><b>Solution</b></summary>
For the first reaction, $Al \rightarrow Al^{3+} + 3e^-$. Since there are 2 Al atoms, $n = 6$.
$\Delta G^\circ_1 = - (6)(96487)(2.00) = -1,157,844\ J = \textbf{-1157.8\ kJ}$.

For the second reaction, only 1 Al atom reacts, so $n = 3$.
$\Delta G^\circ_2 = - (3)(96487)(2.00) = -578,922\ J = \textbf{-578.9\ kJ}$.

- The **$\Delta G^\circ$ is halved** because Free Energy is extensive; it depends on the exact stoichiometry written.
- The **$E^\circ_{cell}$ remains exactly $2.00\ V$** because Voltage is intensive; it is just the "pressure" of the reaction, regardless of how much material is reacting.
</details>

---

### The Spontaneity Triangle

In science, there are three primary ways to state whether a process will happen on its own (spontaneously). They form a perfect, interconnected triangle:
1. **Thermodynamics:** A process is spontaneous if it releases free energy ($\Delta G < 0$).
2. **Electrochemistry:** A cell is spontaneous if it generates a positive voltage ($E_{cell} > 0$).
3. **Equilibrium:** A reaction is spontaneous (product-favored) if its equilibrium constant is massive ($K > 1$).

We have already linked $\Delta G^\circ$ and $E^\circ_{cell}$. We also know from thermodynamics that $\Delta G^\circ = -RT \ln K_c$. Setting these two equations equal to each other proves everything we learned in the previous chapter:
$$ -nFE^\circ_{cell} = -RT \ln K_c $$
$$ E^\circ_{cell} = \frac{RT}{nF} \ln K_c $$

---

### Checkpoint 2: Navigating the Triangle

**Problem 1:** A hypothetical cell reaction has $\Delta G^\circ = +45\ kJ\ mol^{-1}$. What can you infer about the sign of its $E^\circ_{cell}$ and the magnitude of its $K_c$?<br> Will this cell power a lightbulb?<br>

<details><summary><b>Solution</b></summary>
- Since $\Delta G^\circ$ is positive, the reaction requires energy to proceed. It is non-spontaneous.
- From $\Delta G^\circ = -nFE^\circ_{cell}$, a positive $\Delta G^\circ$ requires a **negative $E^\circ_{cell}$**.
- From $\Delta G^\circ = -RT \ln K_c$, a positive $\Delta G^\circ$ means $\ln K_c$ must be negative, so **$K_c$ must be less than 1** (reactant-favored).
- Because it is non-spontaneous, it will **not** power a lightbulb. It is a dead (or electrolytic) cell.
</details>

**Problem 2:** Calculate $\Delta G^\circ$ and $K_c$ for the reaction $Ni(s) + 2Ag^+(aq) \rightarrow Ni^{2+}(aq) + 2Ag(s)$ given $E^\circ_{cell} = 1.05\ V$. (Use $1\ F = 96500\ C\ mol^{-1}$ and $T = 298\ K$).

<details><summary><b>Solution</b></summary>
- Find $n$: Ni oxidizes from 0 to +2. $n = 2$.
- Find $\Delta G^\circ$: 
  $\Delta G^\circ = -nFE^\circ_{cell} = - (2)(96500)(1.05) = -202,650\ J = \textbf{-202.65\ kJ\ mol^{-1}}$.
- Find $K_c$:
  Using the shortcut from the previous chapter: $\log K_c = \frac{nE^\circ}{0.0591}$.
  $\log K_c = \frac{2 \times 1.05}{0.0591} = \frac{2.10}{0.0591} = 35.53$.
  $K_c = \text{Antilog}(35.53) = \textbf{3.38} \times \textbf{10}^{\textbf{35}}$.
</details>

---

### Resolving the Paradox: Hess's Law for Electrochemistry

We return to our opening paradox. Why does $0.77\ V$ and $-0.44\ V$ not add up to $+0.33\ V$?<br>

When you combine two separate chemical equations to form a third, you are essentially combining the *energy* of those reactions. According to Hess's Law, energies ($\Delta G$) are strictly additive. Voltages ($E^\circ$) are not.

To correctly find the potential of a combined half-reaction, you must take a detour through energy:
1. Convert the voltage of Reaction 1 into energy ($\Delta G_1 = -n_1 F E_1$).
2. Convert the voltage of Reaction 2 into energy ($\Delta G_2 = -n_2 F E_2$).
3. Add the energies together ($\Delta G_3 = \Delta G_1 + \Delta G_2$).
4. Convert that final energy back into voltage ($\Delta G_3 = -n_3 F E_3$).

If we substitute the formulas into Step 3, the Faraday constants ($F$) cancel out, leaving us with a beautiful, unified rule for combining half-cells:
$$ n_3 E_3 = n_1 E_1 + n_2 E_2 $$

Let's test this on our iron paradox.
1. $Fe^{3+} + 1e^- \rightarrow Fe^{2+}$ ($n_1 = 1, E_1 = +0.77\ V$)
2. $Fe^{2+} + 2e^- \rightarrow Fe$ ($n_2 = 2, E_2 = -0.44\ V$)
3. Target: $Fe^{3+} + 3e^- \rightarrow Fe$ ($n_3 = 3, E_3 = ?<br>$)

$$ 3 \times E_3 = (1 \times 0.77) + (2 \times -0.44) $$
$$ 3E_3 = 0.77 - 0.88 = -0.11 $$
$$ E_3 = \frac{-0.11}{3} = \textbf{-0.036\ V} $$
The math perfectly predicts the laboratory measurement!

---

### Checkpoint 3: The Intensive Trap

**Problem 1:** Given the standard reduction potentials:
$Cu^{2+} + 2e^- \rightarrow Cu \quad (E^\circ_1 = +0.34\ V)$
$Cu^{2+} + 1e^- \rightarrow Cu^+ \quad (E^\circ_2 = +0.15\ V)$
Calculate the standard reduction potential for the $Cu^+ / Cu$ half-cell.

<details><summary><b>Solution</b></summary>
We need the reaction: $Cu^+ + e^- \rightarrow Cu$.
Let's align our given equations to build this target.
Eq 1: $Cu^{2+} + 2e^- \rightarrow Cu$ ($\Delta G_1 = -2F(0.34) = -0.68F$)
Eq 2: $Cu^{2+} + e^- \rightarrow Cu^+$ ($\Delta G_2 = -1F(0.15) = -0.15F$)

To get the target, we must subtract Eq 2 from Eq 1 (which means reversing Eq 2 and adding it):
$Cu^{2+} + 2e^- \rightarrow Cu$
$Cu^+ \rightarrow Cu^{2+} + e^-$
Sum: $Cu^+ + e^- \rightarrow Cu$ (Target achieved. $n_3 = 1$).

$\Delta G_3 = \Delta G_1 - \Delta G_2 = -0.68F - (-0.15F) = -0.53F$.
We also know $\Delta G_3 = -n_3 F E_3 = -1 F E_3$.
Therefore, $-1 F E_3 = -0.53F \implies E_3 = \textbf{+0.53\ V}$.
</details>

**Problem 2:** Let $E^\circ_1$ be the potential for $MnO_4^- \rightarrow Mn^{2+}$ ($n=5$). Let $E^\circ_2$ be the potential for $Mn^{2+} \rightarrow Mn$ ($n=2$). Write the expression for the standard potential $E^\circ_3$ of the full reduction $MnO_4^- \rightarrow Mn$.

<details><summary><b>Solution</b></summary>
The target reaction is the direct sum of the two sequential reductions.
Target $n_3 = 5 + 2 = 7$.
Using the energy addition rule: $n_3 E_3 = n_1 E_1 + n_2 E_2$.
$7 \times E^\circ_3 = 5 \times E^\circ_1 + 2 \times E^\circ_2$.
$E^\circ_3 = \textbf{\frac{5E^\circ_1 + 2E^\circ_2}{7}}$.
</details>

---

### The Culmination: Synthesis and Application

We have seen that voltages cannot be added when calculating a new half-reaction. However, what if we are calculating the EMF of a full cell ($E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$)?<br> Why are we allowed to just subtract the voltages there without using $\Delta G$?<br>

Because in a balanced *full cell* reaction, the number of electrons lost at the anode is exactly equal to the number of electrons gained at the cathode. The $n$ value is the same for the entire process. 

Let's prove it with $\Delta G$.
$\Delta G_{cell} = \Delta G_{cathode} + \Delta G_{anode (oxidation)}$
$-(n) F E_{cell} = -(n) F E_{cathode} + [-(n) F (-E_{anode})]$
Notice that $nF$ appears in every single term! We can divide the entire equation by $-nF$, and we get:
$E_{cell} = E_{cathode} - E_{anode}$

This is why the formula works. The EMF of a full cell is a special case where the stoichiometry cancels out perfectly, leaving the intensive voltages behind. But the moment you combine half-reactions that do *not* have matching electrons (creating a new, third half-reaction), you must return to the unbreakable laws of Gibbs Free Energy.

**Synthesis Problem:** 
Given:
$Fe^{3+} + e^- \rightarrow Fe^{2+} \quad E^\circ = +0.77\ V$
$I_2 + 2e^- \rightarrow 2I^- \quad E^\circ = +0.54\ V$
Calculate the $\Delta G^\circ$ and the equilibrium constant $K_c$ for the reaction $2Fe^{3+} + 2I^- \rightarrow 2Fe^{2+} + I_2$ at $298\ K$.

<details><summary><b>Solution</b></summary>
**Step 1: Find $E^\circ_{cell}$.**
$Fe^{3+}$ is reducing (Cathode). $I^-$ is oxidizing (Anode).
$E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} = 0.77 - 0.54 = \textbf{+0.23\ V}$.
*(Because this is a full cell reaction, we can subtract voltages directly!).*

**Step 2: Find $\Delta G^\circ$.**
The balanced reaction transfers 2 electrons. $n = 2$.
$\Delta G^\circ = -nFE^\circ_{cell} = - (2)(96487)(0.23) = \textbf{-44,384\ J\ mol^{-1}}$ (or $-44.38\ kJ\ mol^{-1}$).

**Step 3: Find $K_c$.**
$\log K_c = \frac{nE^\circ}{0.0591} = \frac{2 \times 0.23}{0.0591} = \frac{0.46}{0.0591} = 7.78$.
$K_c = \text{Antilog}(7.78) = 10^7 \times 10^{0.78}$.
Using tables or given values, $10^{0.78} \approx 6.0$.
$K_c = \textbf{6.0} \times \textbf{10}^{\textbf{7}}$.
The reaction is highly spontaneous, releasing over $44\ kJ$ of energy per mole, and strongly favors the formation of iodine and iron(II).
</details>

---

*Next: [Chapter 11 — Resistance, Conductance, and Cell Constant →](./11_resistance_conductance.md)*
