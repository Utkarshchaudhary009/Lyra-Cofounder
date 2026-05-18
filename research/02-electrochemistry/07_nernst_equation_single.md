# Chapter 7: The Nernst Equation (Single Electrode) — Escaping Standard Conditions

> *NCERT Sections 3.2.1*

---

## 🎯 Stage 1: The Core Idea

### The Tug-of-War: Adding Players to the Team
Recall that Electrode Potential is a "tug-of-war" for electrons between solid metal atoms (who want to dissolve) and aqueous metal ions (who want to deposit). 

The Standard Potential ($E^\circ$) is the baseline strength of this tug-of-war when the concentration of ions in the water is exactly $1\ M$. But what happens if you don't have exactly $1\ M$?<br>
- **If you add more ions (Concentration > $1\ M$):** The aqueous team has more "players" pulling for electrons. Their ability to reduce (gain electrons) becomes stronger. Therefore, the actual reduction potential ($E$) goes **up**.
- **If you dilute the solution (Concentration < $1\ M$):** The aqueous team loses players. Their pulling power drops. The reduction potential ($E$) goes **down**.

The **Nernst Equation** is simply the mathematical formula that calculates exactly how much the potential changes when you change the concentration or the temperature.

---

## 🔬 Stage 2: The Formula Lab

### The Nernst Equation for a Half-Cell
For a general reduction half-reaction: $M^{n+}(aq) + ne^- \rightarrow M(s)$

The exact Nernst Equation is:
$$ E = E^\circ - \frac{RT}{nF} \ln \frac{[Product]}{[Reactant]} $$

Since solid metals have a constant concentration, we take $[M(s)] = 1$. The reactant is the ion $[M^{n+}]$. Converting natural log ($\ln$) to base-10 log ($\log$) by multiplying by 2.303:

$$ E = E^\circ - \frac{2.303 RT}{nF} \log \frac{1}{[M^{n+}]} $$

### The "298 K" Shortcut (The Magic Number)
At standard room temperature ($298\ K$), the constants $R$ (8.314), $T$ (298), and $F$ (96487) combine with 2.303 to create a magic number: **$0.0591$**.
So, at $298\ K$, the formula you will use 99% of the time is:

$$ E = E^\circ - \frac{0.0591}{n} \log \frac{1}{[M^{n+}]} $$

Alternatively, you can flip the log fraction and change the negative sign to positive (which makes intuitive sense: as concentration goes up, potential goes up):
$$ E = E^\circ + \frac{0.0591}{n} \log [M^{n+}] $$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Identifying 'n' (Moles of Electrons) ⭐

**Pattern:** "The Nernst equation requires $n$. Find the number of electrons transferred in the balanced half-reaction."

**Solved Example** 🟢
> What is the value of $n$ for the reduction of the dichromate ion in acidic medium?<br> 
> $Cr_2O_7^{2-} \rightarrow 2Cr^{3+}$

<details><summary><b>Solution</b></summary>
- Find the oxidation state of Cr in reactant: $2x + 7(-2) = -2 \implies 2x = 12 \implies x = +6$.
- Oxidation state of Cr in product: $+3$.
- Change per Cr atom = $6 \rightarrow 3 = 3$ electrons.
- There are 2 Cr atoms reacting. Total electrons = $3 \times 2 = 6$.
- Therefore, **$n = 6$**.
</details>

**Practice:**

1. 🟢 What is the value of $n$ for $Al^{3+} \rightarrow Al$?<br>
<details><summary><b>Answer</b></summary>
$Al^{3+} + 3e^- \rightarrow Al$. **$n = 3$**.
</details>

2. 🟢 What is the value of $n$ for $Cl_2 \rightarrow 2Cl^-$?<br>
<details><summary><b>Answer</b></summary>
Each Cl atom goes from 0 to -1 (gains 1 electron). There are 2 atoms. $Cl_2 + 2e^- \rightarrow 2Cl^-$. **$n = 2$**.
</details>

3. 🟡 What is the value of $n$ for $MnO_4^- \rightarrow Mn^{2+}$?<br>
<details><summary><b>Answer</b></summary>
Mn goes from $+7$ to $+2$. It gains 5 electrons. **$n = 5$**.
</details>

4. 🟡 A student writes the Nernst equation for $2Ag^+ + 2e^- \rightarrow 2Ag$. What value of $n$ must they use?<br> What is the exponent on $[Ag^+]$ in the log term?<br>
<details><summary><b>Answer</b></summary>
They wrote it with 2 moles of electrons, so **$n = 2$**. Because of the stoichiometry, the concentration term must be squared: $\log \frac{1}{[Ag^+]^2}$. *(Note: It mathematically simplifies to the exact same result as using $n=1$ and no square!)*
</details>

5. 🔴 What is the value of $n$ for the conversion of Hydrogen Peroxide ($H_2O_2$) to Water ($H_2O$) in acidic medium?<br>
<details><summary><b>Answer</b></summary>
$H_2O_2 + 2H^+ + 2e^- \rightarrow 2H_2O$. Oxygen goes from -1 to -2. Two oxygen atoms are involved. **$n = 2$**.
</details>

---

### Type 2: Basic Nernst Calculation (Metal Electrode) ⭐

**Pattern:** "Calculate the non-standard reduction potential $E$ when given $E^\circ$ and a specific concentration."

**Solved Example** 🟡
> Calculate the electrode potential of a Copper wire dipped in a $0.01\ M$ $CuSO_4$ solution at $298\ K$. ($E^\circ_{Cu^{2+}/Cu} = 0.34\ V$).

<details><summary><b>Solution</b></summary>
- Reaction: $Cu^{2+} + 2e^- \rightarrow Cu$. ($n = 2$).
- $[Cu^{2+}] = 0.01\ M = 10^{-2}\ M$.
- Formula: $E = E^\circ - \frac{0.0591}{n} \log \frac{1}{[Cu^{2+}]}$
- $E = 0.34 - \frac{0.0591}{2} \log \frac{1}{10^{-2}}$
- $E = 0.34 - 0.0295 \times \log(10^2)$
- $E = 0.34 - 0.0295 \times 2 = 0.34 - 0.059 = \textbf{+0.281\ V}$.
</details>

**Practice:**

1. 🟢 Calculate the potential of a Zinc electrode in $0.1\ M$ $ZnSO_4$ at $298\ K$. ($E^\circ = -0.76\ V$).
<details><summary><b>Answer</b></summary>
$n = 2$. $[Zn^{2+}] = 10^{-1}$.
$E = -0.76 - \frac{0.0591}{2} \log \frac{1}{10^{-1}}$
$E = -0.76 - 0.0295 \times \log(10^1) = -0.76 - 0.0295 = \textbf{-0.7895\ V}$.
</details>

2. 🟢 Calculate the potential of a Silver electrode in $0.001\ M$ $AgNO_3$ at $298\ K$. ($E^\circ = 0.80\ V$).
<details><summary><b>Answer</b></summary>
$n = 1$. $[Ag^+] = 10^{-3}$.
$E = 0.80 - \frac{0.0591}{1} \log \frac{1}{10^{-3}} = 0.80 - 0.0591 \times 3 = 0.80 - 0.1773 = \textbf{+0.6227\ V}$.
</details>

3. 🟡 An unknown metal M ($n=2$) has an electrode potential of $-0.40\ V$ when its ion concentration is $0.01\ M$. What is its standard electrode potential $E^\circ$?<br>
<details><summary><b>Answer</b></summary>
$E = E^\circ - \frac{0.0591}{2} \log \frac{1}{10^{-2}}$
$-0.40 = E^\circ - 0.0295 \times 2$
$-0.40 = E^\circ - 0.059$
$E^\circ = -0.40 + 0.059 = \textbf{-0.341\ V}$.
</details>

4. 🟡 For the half-cell $Fe^{3+} + e^- \rightarrow Fe^{2+}$, write the Nernst equation expression.
<details><summary><b>Answer</b></summary>
Both species are aqueous. Neither is solid. So both must appear in the log term.
$E = E^\circ_{Fe^{3+}/Fe^{2+}} - \frac{0.0591}{1} \log \frac{[Fe^{2+}]}{[Fe^{3+}]}$
</details>

5. 🔴 Calculate the oxidation potential of a Zinc electrode in $0.1\ M$ solution. ($E^\circ_{red} = -0.76\ V$).
<details><summary><b>Answer</b></summary>
First find reduction potential $E$:
$E_{red} = -0.76 - \frac{0.0591}{2} \log(10) = -0.76 - 0.0295 = -0.7895\ V$.
Oxidation potential is the negative of reduction potential:
$E_{ox} = -E_{red} = \textbf{+0.7895\ V}$.
*(Notice: Diluting the solution decreases reduction potential, but INCREASES oxidation potential!)*
</details>

---

### Type 3: The Effect of Dilution (Intuition) ⭐

**Pattern:** "Qualitative and quantitative changes when water is added."

**Solved Example** 🟡
> If you dilute a $1\ M$ solution of $CuSO_4$ to $0.01\ M$, by how much does the reduction potential of the copper electrode change?<br>

<details><summary><b>Solution</b></summary>
- Intuition: Dilution $\rightarrow$ fewer players pulling for electrons $\rightarrow$ reduction potential must **decrease**.
- Quantitative: $E = E^\circ - \frac{0.0591}{2} \log \frac{1}{10^{-2}}$
- $E = E^\circ - 0.0295 \times 2 = E^\circ - 0.059\ V$.
- The potential **decreases by $0.059\ V$**.
</details>

**Practice:**

1. 🟢 If you dilute a silver half-cell ($Ag^+/Ag$, $n=1$) by a factor of 10, by how much does the potential decrease?<br>
<details><summary><b>Answer</b></summary>
$E = E^\circ - \frac{0.0591}{1} \log(10) = E^\circ - 0.0591$. 
It decreases by **$0.0591\ V$**.
</details>

2. 🟢 If you dilute an aluminum half-cell ($Al^{3+}/Al$, $n=3$) by a factor of 10, by how much does the potential decrease?<br>
<details><summary><b>Answer</b></summary>
$E = E^\circ - \frac{0.0591}{3} \log(10) = E^\circ - 0.0197$.
It decreases by **$0.0197\ V$**. (Higher valency = smaller change upon dilution).
</details>

3. 🟡 You have a Zinc electrode in $1\ M$ solution. You add a large amount of water to the beaker. Does the *oxidation* potential of Zinc increase or decrease?<br>
<details><summary><b>Answer</b></summary>
Adding water dilutes the $Zn^{2+}$ ions. It becomes *easier* for solid Zinc to dissolve (oxidize) into a less crowded solution. Therefore, the **oxidation potential increases**.
</details>

4. 🟡 How many times must you dilute a $Cu^{2+}$ ($n=2$) solution to drop its potential by exactly $0.0591\ V$?<br>
<details><summary><b>Answer</b></summary>
Change in $E = \frac{0.0591}{2} \log(\text{dilution factor}) = 0.0591$.
$\frac{1}{2} \log(x) = 1 \implies \log(x) = 2 \implies x = 10^2 = 100$.
You must dilute it by **100 times**.
</details>

5. 🔴 For an electrode $M^{n+}/M$, the potential drops by $0.0197\ V$ when the solution is diluted 10 times. What is the valency ($n$) of the metal?<br>
<details><summary><b>Answer</b></summary>
Drop = $\frac{0.0591}{n} \log(10) = 0.0197$
$\frac{0.0591}{n} \times 1 = 0.0197$
$n = \frac{0.0591}{0.0197} = \textbf{3}$.
</details>

---

### Type 4: Nernst for Hydrogen Electrode (pH Impact) ⭐

**Pattern:** "Using the Nernst equation on the $H^+/H_2$ couple to relate Potential directly to pH."

**Solved Example** 🟡
> Calculate the reduction potential of a hydrogen electrode placed in a solution of $pH = 10$ at $298\ K$ and $1\ atm$ pressure.

<details><summary><b>Solution</b></summary>
- Reaction: $2H^+ + 2e^- \rightarrow H_2(g)$. ($n = 2$).
- $[H^+] = 10^{-pH} = 10^{-10}\ M$.
- $E = E^\circ - \frac{0.0591}{2} \log \frac{P_{H_2}}{[H^+]^2}$
- $E = 0 - \frac{0.0591}{2} \log \frac{1}{(10^{-10})^2} = - \frac{0.0591}{2} \log (10^{20})$
- $E = - \frac{0.0591}{2} \times 20 = -0.0591 \times 10 = \textbf{-0.591\ V}$.
*(Shortcut Formula: $E_{red} = -0.0591 \times pH$)*
</details>

**Practice:**

1. 🟢 Calculate the reduction potential of a hydrogen electrode at $pH = 3$.
<details><summary><b>Answer</b></summary>
Using shortcut: $E = -0.0591 \times 3 = \textbf{-0.1773\ V}$.
</details>

2. 🟢 A hydrogen electrode has a reduction potential of $-0.2364\ V$. What is the pH of the solution?<br>
<details><summary><b>Answer</b></summary>
$-0.2364 = -0.0591 \times pH \implies pH = \frac{0.2364}{0.0591} = \textbf{4}$.
</details>

3. 🟡 Calculate the *oxidation* potential of a hydrogen electrode in pure water ($pH = 7$).
<details><summary><b>Answer</b></summary>
Reduction potential $E_{red} = -0.0591 \times 7 = -0.4137\ V$.
Oxidation potential $E_{ox} = -E_{red} = \textbf{+0.4137\ V}$.
</details>

4. 🟡 A hydrogen electrode is dipped in $0.05\ M\ H_2SO_4$ (assume complete dissociation). What is its reduction potential?<br>
<details><summary><b>Answer</b></summary>
$[H^+] = 2 \times 0.05 = 0.1\ M = 10^{-1}\ M$.
$pH = 1$.
$E = -0.0591 \times 1 = \textbf{-0.0591\ V}$.
</details>

5. 🔴 If the pressure of $H_2$ gas in a standard hydrogen electrode is increased to $100\ atm$ (while keeping $[H^+] = 1\ M$), what is the new reduction potential?<br>
<details><summary><b>Answer</b></summary>
$E = E^\circ - \frac{0.0591}{2} \log \frac{P_{H_2}}{[H^+]^2}$
$E = 0 - \frac{0.0591}{2} \log \frac{100}{1^2} = -0.0295 \times \log(10^2)$
$E = -0.0295 \times 2 = \textbf{-0.059\ V}$.
</details>

---

### Type 5: Non-Metal Electrodes (Halogens) ⭐

**Pattern:** "Applying Nernst to halogens where the non-metal is reduced to an anion."

**Solved Example** 🟡
> Write the Nernst equation for a Chlorine gas electrode: $Cl_2(g) \rightarrow 2Cl^-(aq)$ and calculate its potential if $P_{Cl_2} = 1\ atm$ and $[Cl^-] = 0.1\ M$. ($E^\circ = 1.36\ V$).

<details><summary><b>Solution</b></summary>
- Reaction: $Cl_2(g) + 2e^- \rightarrow 2Cl^-(aq)$. ($n = 2$).
- Nernst Expression: $E = E^\circ - \frac{0.0591}{2} \log \frac{[Cl^-]^2}{P_{Cl_2}}$
- Note: The aqueous ion is now the *product*.
- $E = 1.36 - \frac{0.0591}{2} \log \frac{(0.1)^2}{1}$
- $E = 1.36 - 0.0295 \times \log(10^{-2}) = 1.36 - 0.0295 \times (-2)$
- $E = 1.36 + 0.059 = \textbf{+1.419\ V}$.
</details>

**Practice:**

1. 🟢 For a Bromine liquid electrode ($Br_2(l) + 2e^- \rightarrow 2Br^-$), write the log term for the Nernst equation.
<details><summary><b>Answer</b></summary>
Since $Br_2$ is a pure liquid, its concentration is 1. 
Log term: **$\log ([Br^-]^2)$**.
</details>

2. 🟡 If you increase the concentration of $Cl^-$ ions around a Chlorine electrode, does its reduction potential increase or decrease?<br>
<details><summary><b>Answer</b></summary>
$Cl^-$ is a product in the reduction reaction ($Cl_2 + 2e^- \rightarrow 2Cl^-$). According to Le Chatelier, adding product shifts equilibrium backwards, opposing reduction. Therefore, the reduction potential **decreases**.
</details>

3. 🟡 Calculate the potential of $Pt\ |\ Cl_2(1\ atm)\ |\ Cl^-(0.01\ M)$. ($E^\circ = 1.36\ V$).
<details><summary><b>Answer</b></summary>
$E = 1.36 - \frac{0.0591}{2} \log(10^{-2})^2 = 1.36 - 0.0295 \times \log(10^{-4})$
$E = 1.36 - 0.0295 \times (-4) = 1.36 + 0.118 = \textbf{+1.478\ V}$.
</details>

4. 🔴 A cell is $Pt\ |\ I_2(s)\ |\ I^-(0.1\ M)$. Find $E$ if $E^\circ = 0.54\ V$.
<details><summary><b>Answer</b></summary>
$I_2(s) + 2e^- \rightarrow 2I^-$.
$E = 0.54 - \frac{0.0591}{2} \log(0.1)^2 = 0.54 - 0.0295 \times (-2) = 0.54 + 0.059 = \textbf{+0.599\ V}$.
</details>

---

### Type 6: Graphical Analysis (Preview) ⭐

**Pattern:** "Interpreting straight line graphs of $E$ vs $\log[M^{n+}]$. "

**Solved Example** 🟡
> If you plot the reduction potential $E$ (y-axis) against $\log[Cu^{2+}]$ (x-axis) for a Copper electrode, what kind of graph do you get?<br> What are its slope and y-intercept?<br>

<details><summary><b>Solution</b></summary>
- Start with Nernst: $E = E^\circ - \frac{0.0591}{n} \log \frac{1}{[Cu^{2+}]}$
- Rewrite using log properties: $E = E^\circ + \frac{0.0591}{n} \log[Cu^{2+}]$
- Compare to $y = mx + c$:
  - $y = E$
  - $x = \log[Cu^{2+}]$
- It is a **straight line**.
- **Slope ($m$):** $+\frac{0.0591}{2} = \textbf{+0.0295}$.
- **y-intercept ($c$):** **$E^\circ_{Cu}$** ($+0.34\ V$).
</details>

**Practice:**

1. 🟢 For a plot of $E$ vs $\log[Ag^+]$, will the slope be steeper or flatter than the plot for $Cu^{2+}$?<br>
<details><summary><b>Answer</b></summary>
Slope for Ag ($n=1$) is $0.0591/1 = 0.0591$. Slope for Cu ($n=2$) is $0.0295$. 
Therefore, the plot for Ag will be **steeper**.
</details>

2. 🟡 What does the y-intercept represent on a graph of $E$ vs $\log[M^{n+}]$?<br>
<details><summary><b>Answer</b></summary>
The **Standard Electrode Potential ($E^\circ$)**. It is the potential when $\log[M^{n+}] = 0$, which means $[M^{n+}] = 1\ M$ (standard conditions).
</details>

3. 🔴 A graph of $E_{red}$ vs $\log[M^{n+}]$ gives a straight line with a slope of $+0.0197$. What is the charge on the metal ion?<br>
<details><summary><b>Answer</b></summary>
Slope = $0.0591 / n$.
$0.0197 = 0.0591 / n \implies n = 0.0591 / 0.0197 = \textbf{3}$. The ion is $M^{3+}$.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1. (NCERT Type)** 🟢 The Nernst equation for the electrode $M^{n+}/M$ at $298\ K$ is:
(a) $E = E^\circ + \frac{0.0591}{n} \log[M^{n+}]$
(b) $E = E^\circ - \frac{0.0591}{n} \log[M^{n+}]$
(c) $E = E^\circ + \frac{0.0591}{n} \log \frac{1}{[M^{n+}]}$
(d) $E = E^\circ - \frac{n}{0.0591} \log[M^{n+}]$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
The standard form is $E = E^\circ - \frac{0.0591}{n} \log \frac{1}{[M^{n+}]}$. Bringing the term up flips the sign to positive.
</details>

**Q2. (Board Type)** 🟡 An increase in the concentration of the reactant ions in a half-cell:
(a) Increases the reduction potential.
(b) Decreases the reduction potential.
(c) Does not affect the reduction potential.
(d) Decreases the standard reduction potential.

<details><summary><b>Answer</b></summary>
**Answer: (a)**
More reactant ions shift the equilibrium forward (more reduction), making the "pull" stronger. (Note: option d is wrong because *Standard* potential is a constant).
</details>

**Q3. (JEE Mains Type)** 🔴 The reduction potential of a hydrogen half-cell will be negative if:
(a) $P_{H_2} = 1\ atm$ and $[H^+] = 2\ M$
(b) $P_{H_2} = 1\ atm$ and $[H^+] = 1\ M$
(c) $P_{H_2} = 2\ atm$ and $[H^+] = 1\ M$
(d) $P_{H_2} = 2\ atm$ and $[H^+] = 2\ M$

<details><summary><b>Answer</b></summary>
**Answer: (c)**
$E = - \frac{0.0591}{2} \log \frac{P_{H_2}}{[H^+]^2}$. To make E negative, the log term must be positive, which means the fraction $\frac{P_{H_2}}{[H^+]^2}$ must be greater than 1.
(a) $1 / 2^2 = 0.25$ (Log is negative $\rightarrow E$ is positive).
(b) $1 / 1 = 1$ (Log is 0 $\rightarrow E$ is 0).
(c) $2 / 1^2 = 2$ (Log is positive $\rightarrow E$ is negative).
</details>

**Q4. (Exemplar Type)** 🟡 What is the ratio of the slopes of the graphs of $E$ vs $\log[M^{n+}]$ for $Ag^+$ and $Zn^{2+}$?<br>
(a) $1:2$
(b) $2:1$
(c) $1:1$
(d) $4:1$

<details><summary><b>Answer</b></summary>
**Answer: (b)**
Slope for Ag+ ($n=1$) is $0.0591 / 1$.
Slope for Zn2+ ($n=2$) is $0.0591 / 2$.
Ratio $= \frac{0.0591}{0.0591/2} = \textbf{2:1}$.
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🟡 ⭐ A hydrogen electrode is placed in a buffer solution of acetic acid and sodium acetate in a 1:10 ratio. If $pK_a$ of acetic acid is 4.74, calculate the reduction potential of the electrode at $298\ K$ and $1\ atm\ H_2$ pressure.

<details><summary><b>Solution</b></summary>
- Step 1: Find pH using Henderson-Hasselbalch equation.
$pH = pK_a + \log \frac{[\text{Salt}]}{[\text{Acid}]} = 4.74 + \log(10/1) = 4.74 + 1 = 5.74$.
- Step 2: Use the Nernst shortcut for Hydrogen.
$E_{red} = -0.0591 \times pH$
$E_{red} = -0.0591 \times 5.74 \approx \textbf{-0.339\ V}$.
</details>

**Q2.** 🔴 An electrode $M^{n+}/M$ has a potential of $0.295\ V$ at $0.01\ M$ and $0.3245\ V$ at $0.1\ M$. Calculate the valency of the metal ($n$) and its standard electrode potential ($E^\circ$).

<details><summary><b>Solution</b></summary>
- Set up two equations:
1) $0.295 = E^\circ + \frac{0.0591}{n} \log(10^{-2}) \implies 0.295 = E^\circ - \frac{0.1182}{n}$
2) $0.3245 = E^\circ + \frac{0.0591}{n} \log(10^{-1}) \implies 0.3245 = E^\circ - \frac{0.0591}{n}$
- Subtract equation (1) from (2):
$0.3245 - 0.295 = \left(-\frac{0.0591}{n}\right) - \left(-\frac{0.1182}{n}\right)$
$0.0295 = \frac{0.0591}{n} \implies n = \frac{0.0591}{0.0295} = \textbf{2}$.
- Substitute $n=2$ into equation (2):
$0.3245 = E^\circ - \frac{0.0591}{2} \implies 0.3245 = E^\circ - 0.0295$
$E^\circ = 0.3245 + 0.0295 = \textbf{+0.354\ V}$.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Write the Nernst equation for a single electrode reduction reaction at $298\ K$. *(1 mark)*
<details><summary><b>Model Answer</b></summary>
$E = E^\circ - \frac{0.0591}{n} \log \frac{1}{[M^{n+}]}$
where $E$ is electrode potential, $E^\circ$ is standard electrode potential, $n$ is number of electrons gained, and $[M^{n+}]$ is the molar concentration of the metal ion.
</details>

**Q2.** 🟡 How does the reduction potential of a metal electrode change if the concentration of its ions in solution is decreased?<br> *(1 mark)*
<details><summary><b>Model Answer</b></summary>
The reduction potential **decreases** when the concentration of metal ions is decreased.
</details>

**Q3.** 🟡 State the significance of the Nernst equation. *(2 marks)*
<details><summary><b>Model Answer</b></summary>
1. It allows the calculation of electrode potential and cell EMF under non-standard conditions of concentration, pressure, and temperature.
2. It relates the potential of a cell to the concentration of reactant and product species, forming the basis for determining equilibrium constants and pH.
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🔴 ⭐ The oxidation potential of a hydrogen electrode at $pH = 10$ and $P_{H_2} = 1\ atm$ is:
(a) $0.59\ V$
(b) $0.00\ V$
(c) $-0.59\ V$
(d) $0.059\ V$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
Reduction potential $E_{red} = -0.0591 \times pH = -0.0591 \times 10 = -0.591\ V$.
The question asks for **oxidation potential**. $E_{ox} = -E_{red} = \textbf{+0.591\ V}$.
</details>

**Q2.** 🔴 For the half-cell $Fe^{3+} + e^- \rightarrow Fe^{2+}$, the standard potential is $+0.77\ V$. If a student prepares a solution where $[Fe^{3+}] = 0.1\ M$ and $[Fe^{2+}] = 0.01\ M$, what is the electrode potential?<br>
(a) $0.77\ V$
(b) $0.711\ V$
(c) $0.829\ V$
(d) $0.888\ V$

<details><summary><b>Answer</b></summary>
**Answer: (c)**
$E = E^\circ - \frac{0.0591}{n} \log \frac{[\text{Product}]}{[\text{Reactant}]}$
$E = 0.77 - \frac{0.0591}{1} \log \frac{[Fe^{2+}]}{[Fe^{3+}]}$
$E = 0.77 - 0.0591 \log \frac{0.01}{0.1} = 0.77 - 0.0591 \log(10^{-1})$
$E = 0.77 - 0.0591(-1) = 0.77 + 0.0591 = \textbf{0.8291\ V}$.
*(Intuition check: We have more reactant than product compared to standard state, so the reaction is driven forward harder. The potential must increase!)*
</details>

---

*Next: [Chapter 8 — The Nernst Equation (Complete Cell) →](./08_nernst_equation_cell.md)*
