# Chapter 9: Equilibrium Constant from Nernst Equation — The Dead Battery

> *NCERT Sections 3.2.2*

---

## 🎯 Stage 1: The Core Idea

### The Anatomy of a Dead Battery
When you connect a voltmeter to a dead battery, it reads exactly **$0.00\ V$**. 
What does this mean chemically?<br> It means the "tug-of-war" for electrons has reached a perfect stalemate. The forward reaction (products forming) and the backward reaction (reactants reforming) are happening at the exact same speed. The driving force is gone. 

In chemistry, we call this state **Equilibrium**. 
At this exact moment:
1. The actual cell voltage drops to zero: **$E_{cell} = 0$**.
2. The reaction quotient ($Q$) stops changing and locks into a final, constant ratio known as the **Equilibrium Constant ($K_c$)**.

By substituting these two facts into the Nernst equation, we discover something amazing: we can calculate the exact ratio of products to reactants ($K_c$) just by knowing the battery's theoretical maximum voltage ($E^\circ_{cell}$)!

---

## 🔬 Stage 2: The Formula Lab

### The Derivation
Start with the complete cell Nernst equation:
$$ E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log Q $$

Apply the "Dead Battery" conditions:
1. Set $E_{cell} = 0$
2. Replace $Q$ with $K_c$

$$ 0 = E^\circ_{cell} - \frac{0.0591}{n} \log K_c $$

### The Master Formula
Rearrange the equation to solve for $\log K_c$:
$$ \log K_c = \frac{n \times E^\circ_{cell}}{0.0591} \quad (\text{at } 298\ K) $$

To find the actual value of $K_c$, you must take the Antilog:
$$ K_c = \text{Antilog}\left( \frac{n \times E^\circ_{cell}}{0.0591} \right) $$

*(Note: $E^\circ_{cell}$ is a constant based on the metals used. It **never** equals zero unless you build a concentration cell. It is the operating $E_{cell}$ that drops to zero).*

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Identifying the Dead Battery Condition ⭐

**Pattern:** "Conceptual understanding of what variables equal zero at equilibrium."

**Solved Example** 🟢
> A student claims that when a Daniell cell reaches equilibrium, its standard EMF ($E^\circ_{cell}$) becomes zero. Is this correct?<br>

<details><summary><b>Solution</b></summary>
**No, this is completely incorrect.** 
The standard EMF ($E^\circ_{cell}$) is a theoretical constant derived from standard tables ($1.10\ V$ for a Daniell cell). It never changes. 
What drops to zero is the **actual operating cell potential ($E_{cell}$)** due to the changing concentrations of ions.
</details>

**Practice:**

1. 🟢 At equilibrium, which of the following is true?<br>
(a) $E^\circ_{cell} = 0$
(b) $E_{cell} = 0$
(c) Both are zero
(d) Neither are zero
<details><summary><b>Answer</b></summary>
**Answer: (b) $E_{cell} = 0$.**
</details>

2. 🟢 At equilibrium, the reaction quotient $Q$ becomes equal to what?<br>
<details><summary><b>Answer</b></summary>
It becomes equal to the **Equilibrium Constant ($K_c$)**.
</details>

3. 🟡 If a cell reaction is perfectly balanced at equilibrium, what is the net flow of electrons through the external wire?<br>
<details><summary><b>Answer</b></summary>
The net flow is **zero**. Because there is no potential difference ($E_{cell} = 0$) driving them.
</details>

4. 🟡 For a concentration cell ($Cu | Cu^{2+} || Cu^{2+} | Cu$), both $E_{cell}$ and $E^\circ_{cell}$ can be zero. When does this happen?<br>
<details><summary><b>Answer</b></summary>
$E^\circ_{cell}$ is always zero for a concentration cell. $E_{cell}$ becomes zero when the cell reaches equilibrium, which occurs when the **concentrations in both half-cells become exactly equal**.
</details>

5. 🔴 Can an electrochemical cell with a negative $E^\circ_{cell}$ reach equilibrium?<br>
<details><summary><b>Answer</b></summary>
If $E^\circ_{cell}$ is negative, the reaction is non-spontaneous in the forward direction. It is actually already past equilibrium in the forward direction. The reverse reaction is spontaneous. It will reach equilibrium when the reverse reaction proceeds enough to make $E_{cell} = 0$.
</details>

---

### Type 2: Basic Calculation of $\log K_c$ ⭐

**Pattern:** "Given $E^\circ_{cell}$ and $n$, calculate the value of $\log K_c$ (without doing the final antilog step)."

**Solved Example** 🟢
> For the cell reaction $Ni(s) + 2Ag^+(aq) \rightarrow Ni^{2+}(aq) + 2Ag(s)$, the standard cell potential is $1.05\ V$. Calculate the value of $\log K_c$ at $298\ K$.

<details><summary><b>Solution</b></summary>
- Reaction: $Ni \rightarrow Ni^{2+} + 2e^-$. $n = 2$.
- $E^\circ_{cell} = 1.05\ V$.
- Formula: $\log K_c = \frac{n \times E^\circ_{cell}}{0.0591}$
- $\log K_c = \frac{2 \times 1.05}{0.0591} = \frac{2.10}{0.0591}$
- $\log K_c \approx \textbf{35.53}$.
</details>

**Practice:**

1. 🟢 Calculate $\log K_c$ for $Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$. ($E^\circ_{cell} = 1.10\ V$).
<details><summary><b>Answer</b></summary>
$n = 2$.
$\log K_c = \frac{2 \times 1.10}{0.0591} = \frac{2.20}{0.0591} \approx \textbf{37.22}$.
</details>

2. 🟢 Calculate $\log K_c$ for $Cu + 2Ag^+ \rightarrow Cu^{2+} + 2Ag$. ($E^\circ_{cell} = 0.46\ V$).
<details><summary><b>Answer</b></summary>
$n = 2$.
$\log K_c = \frac{2 \times 0.46}{0.0591} = \frac{0.92}{0.0591} \approx \textbf{15.56}$.
</details>

3. 🟡 For a reaction with $n = 1$, the standard EMF is $0.591\ V$. What is the value of $\log K_c$?<br>
<details><summary><b>Answer</b></summary>
$\log K_c = \frac{1 \times 0.591}{0.0591} = \textbf{10}$.
</details>

4. 🟡 A cell has $E^\circ_{cell} = 0.0591\ V$ and the balanced equation involves the transfer of 3 moles of electrons. Calculate $\log K_c$.
<details><summary><b>Answer</b></summary>
$n = 3$. 
$\log K_c = \frac{3 \times 0.0591}{0.0591} = \textbf{3}$.
</details>

5. 🔴 Two students calculate $\log K_c$ for the same physical cell. Student A uses the equation $Ag^+ + \frac{1}{2}Cu \rightarrow Ag + \frac{1}{2}Cu^{2+}$. Student B uses $2Ag^+ + Cu \rightarrow 2Ag + Cu^{2+}$. Will their $\log K_c$ values be the same?<br>
<details><summary><b>Answer</b></summary>
**No.** Student A uses $n = 1$. Student B uses $n = 2$. 
Because $K_c$ is derived from the specific stoichiometric equation written, Student B's $\log K_c$ will be exactly twice as large as Student A's. (This matches equilibrium rules: if you multiply an equation by 2, its $K_c$ is squared, meaning $\log(K_c^2) = 2\log K_c$).
</details>

---

### Type 3: Full Calculation of $K_c$ (Using Antilog) ⭐

**Pattern:** "Taking the calculation one step further by finding the actual equilibrium constant."

**Solved Example** 🟡
> If $\log K_c = 37.22$, calculate the value of $K_c$.

<details><summary><b>Solution</b></summary>
- $K_c = \text{Antilog}(37.22)$
- Break the number into the integer part (characteristic) and the decimal part (mantissa): $37 + 0.22$.
- The integer part becomes the power of 10: $10^{37}$.
- Use an antilog table (or given values) for the decimal part: $\text{Antilog}(0.22) \approx 1.66$.
- $K_c = \textbf{1.66} \times \textbf{10}^{\textbf{37}}$.
</details>

**Practice:**

1. 🟢 If $\log K_c = 2.0$, what is $K_c$?<br>
<details><summary><b>Answer</b></summary>
$K_c = 10^{2.0} = \textbf{100}$.
</details>

2. 🟢 If $\log K_c = 15.56$, and you are given that $10^{0.56} \approx 3.63$, what is $K_c$?<br>
<details><summary><b>Answer</b></summary>
$K_c = 10^{15} \times 10^{0.56} = \textbf{3.63} \times \textbf{10}^{\textbf{15}}$.
</details>

3. 🟡 For the cell reaction $A + B^{2+} \rightarrow A^{2+} + B$, $E^\circ_{cell} = 0.2955\ V$. Calculate $K_c$.
<details><summary><b>Answer</b></summary>
$n = 2$. 
$\log K_c = \frac{2 \times 0.2955}{0.0591} = \frac{0.591}{0.0591} = 10$.
$K_c = \text{Antilog}(10) = \textbf{10}^{\textbf{10}}$.
</details>

4. 🟡 For a reaction where $n=1$, $E^\circ_{cell} = 0.000\ V$. What is $K_c$?<br>
<details><summary><b>Answer</b></summary>
$\log K_c = 0$.
$K_c = 10^0 = \textbf{1}$. (The reaction is at equilibrium under standard conditions!).
</details>

5. 🔴 Given $\log K_c = -2.5$. Calculate $K_c$. (Hint: Negative antilogs are tricky).
<details><summary><b>Answer</b></summary>
For negative logs, you must add and subtract 1 to get a positive mantissa.
$-2.5 = -3 + 0.5$.
The $-3$ becomes $10^{-3}$. The $0.5$ becomes $10^{0.5} \approx 3.16$.
$K_c = \textbf{3.16} \times \textbf{10}^{\textbf{-3}}$.
</details>

---

### Type 4: Calculating $K_c$ from Half-Cell Potentials ⭐

**Pattern:** "Not given $E^\circ_{cell}$ directly. You must calculate it first from $E^\circ_C - E^\circ_A$."

**Solved Example** 🟡
> Calculate the equilibrium constant for the reaction: 
> $Fe(s) + Cd^{2+}(aq) \rightleftharpoons Fe^{2+}(aq) + Cd(s)$
> Given $E^\circ_{Fe^{2+}/Fe} = -0.44\ V$ and $E^\circ_{Cd^{2+}/Cd} = -0.40\ V$.

<details><summary><b>Solution</b></summary>
- Step 1: Identify Cathode and Anode from the reaction. Fe oxidizes (Anode). Cd reduces (Cathode).
- Step 2: Calculate $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} = -0.40 - (-0.44) = \textbf{+0.04\ V}$.
- Step 3: Find $n$. Reaction transfers 2 electrons. $n = 2$.
- Step 4: $\log K_c = \frac{n \times E^\circ}{0.0591} = \frac{2 \times 0.04}{0.0591} = \frac{0.08}{0.0591} \approx 1.35$.
- Step 5: $K_c = \text{Antilog}(1.35) = 10^{1} \times 10^{0.35} \approx \textbf{2.24} \times \textbf{10}^{\textbf{1}}$.
</details>

**Practice:**

1. 🟢 Calculate $K_c$ for $Zn + Pb^{2+} \rightleftharpoons Zn^{2+} + Pb$. ($E^\circ_{Zn} = -0.76\ V, E^\circ_{Pb} = -0.13\ V$).
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = -0.13 - (-0.76) = +0.63\ V$. $n = 2$.
$\log K_c = \frac{2 \times 0.63}{0.0591} = \frac{1.26}{0.0591} \approx 21.32$.
$K_c = \text{Antilog}(21.32) = \textbf{2.08} \times \textbf{10}^{\textbf{21}}$.
</details>

2. 🟡 Calculate $K_c$ for $Cu + 2Ag^+ \rightleftharpoons Cu^{2+} + 2Ag$. ($E^\circ_{Cu} = +0.34\ V, E^\circ_{Ag} = +0.80\ V$).
<details><summary><b>Answer</b></summary>
$E^\circ_{cell} = 0.80 - 0.34 = 0.46\ V$. $n = 2$.
$\log K_c = \frac{2 \times 0.46}{0.0591} = \frac{0.92}{0.0591} \approx 15.56$.
$K_c = \textbf{3.6} \times \textbf{10}^{\textbf{15}}$.
</details>

3. 🟡 If $E^\circ_{A^{2+}/A} = 0.10\ V$ and $E^\circ_{B^{2+}/B} = -0.20\ V$. What is the equilibrium constant for $A + B^{2+} \rightleftharpoons A^{2+} + B$?<br>
<details><summary><b>Answer</b></summary>
A is Anode, B is Cathode. $E^\circ_{cell} = -0.20 - 0.10 = -0.30\ V$. $n=2$.
$\log K_c = \frac{2 \times (-0.30)}{0.0591} = -10.15$.
$K_c = \text{Antilog}(-10.15) = \text{Antilog}(-11 + 0.85) \approx \textbf{7.0} \times \textbf{10}^{\textbf{-11}}$.
*(A very small $K_c$, meaning the reaction barely proceeds forward).*
</details>

4. 🔴 Calculate $K_c$ for $2Fe^{3+} + 2I^- \rightleftharpoons 2Fe^{2+} + I_2$. ($E^\circ_{Fe} = 0.77\ V, E^\circ_I = 0.54\ V$).
<details><summary><b>Answer</b></summary>
Fe reduces (Cathode). I oxidizes (Anode). $E^\circ_{cell} = 0.77 - 0.54 = +0.23\ V$. $n = 2$.
$\log K_c = \frac{2 \times 0.23}{0.0591} = \frac{0.46}{0.0591} \approx 7.78$.
$K_c = \text{Antilog}(7.78) \approx \textbf{6.0} \times \textbf{10}^{\textbf{7}}$.
</details>

---

### Type 5: Understanding Magnitude (Very Large $K_c$) ⭐

**Pattern:** "Connecting the massive numbers to physical reality."

**Solved Example** 🟡
> The equilibrium constant for the Daniell cell is approximately $1.66 \times 10^{37}$. What does this astronomically large number tell you about the reaction $Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu$?<br>

<details><summary><b>Solution</b></summary>
- $K_c = \frac{[\text{Products}]}{[\text{Reactants}]}$.
- A value of $10^{37}$ means there are $10^{37}$ times more products than reactants at equilibrium.
- This tells us the reaction **goes almost to 100% completion**. Virtually all the $Cu^{2+}$ ions will be consumed before the battery officially "dies".
</details>

**Practice:**

1. 🟢 If $E^\circ_{cell}$ is highly positive, what can you say about the magnitude of $K_c$?<br>
<details><summary><b>Answer</b></summary>
Since $\log K_c$ is directly proportional to $E^\circ_{cell}$, a highly positive $E^\circ_{cell}$ results in a **very large, highly positive exponent** for $K_c$.
</details>

2. 🟢 If a reaction has $K_c = 10^{-15}$, will a battery based on this reaction be useful?<br>
<details><summary><b>Answer</b></summary>
**No.** A $K_c$ much less than 1 means $E^\circ_{cell}$ is negative. The reaction strongly favors reactants and will not generate electricity spontaneously.
</details>

3. 🟡 If the EMF of cell A is $0.5\ V$ and cell B is $1.0\ V$ (both with $n=2$), how does the $K_c$ of B compare to A?<br>
<details><summary><b>Answer</b></summary>
Because it's a logarithmic relationship, doubling the EMF does not double the $K_c$. It **squares** it.
If $\log K_A \propto 0.5$ and $\log K_B \propto 1.0$, then $K_B = (K_A)^2$.
</details>

---

### Type 6: Reverse Calculation (Finding $E^\circ$ from $K_c$) ⭐

**Pattern:** "Given an equilibrium constant, calculate the standard potential of the cell."

**Solved Example** 🟡
> The equilibrium constant for a cell reaction ($n=2$) is $100$ at $298\ K$. Calculate its standard cell potential.

<details><summary><b>Solution</b></summary>
- $K_c = 100 \implies \log K_c = \log(100) = 2$.
- Formula: $\log K_c = \frac{n \times E^\circ_{cell}}{0.0591}$
- $2 = \frac{2 \times E^\circ_{cell}}{0.0591}$
- $E^\circ_{cell} = \frac{2 \times 0.0591}{2} = \textbf{+0.0591\ V}$.
</details>

**Practice:**

1. 🟢 A reaction with $n=1$ has $K_c = 10^{10}$. What is $E^\circ_{cell}$?<br>
<details><summary><b>Answer</b></summary>
$\log(10^{10}) = 10$.
$10 = \frac{1 \times E^\circ_{cell}}{0.0591} \implies E^\circ_{cell} = 10 \times 0.0591 = \textbf{+0.591\ V}$.
</details>

2. 🟢 A reaction with $n=2$ has $K_c = 1$. What is $E^\circ_{cell}$?<br>
<details><summary><b>Answer</b></summary>
$\log(1) = 0$.
$0 = \frac{2 \times E^\circ_{cell}}{0.0591} \implies E^\circ_{cell} = \textbf{0.00\ V}$.
</details>

3. 🟡 If the equilibrium constant for a reaction is $10^{-5}$, what must be true about the sign of $E^\circ_{cell}$?<br>
<details><summary><b>Answer</b></summary>
$\log(10^{-5}) = -5$. Since $\log K_c$ is negative, **$E^\circ_{cell}$ must be negative**. (The reaction is non-spontaneous).
</details>

4. 🔴 A researcher finds $K_c = 2 \times 10^3$ for a reaction where $n=2$. Calculate $E^\circ_{cell}$. (Given $\log 2 = 0.301$).
<details><summary><b>Answer</b></summary>
$\log(2 \times 10^3) = \log(2) + \log(10^3) = 0.301 + 3 = 3.301$.
$3.301 = \frac{2 \times E^\circ_{cell}}{0.0591}$
$E^\circ_{cell} = \frac{3.301 \times 0.0591}{2} \approx \textbf{+0.0975\ V}$.
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1. (NCERT Type)** 🟢 The equilibrium constant of a cell reaction is related to standard EMF of the cell by the expression:
(a) $E^\circ_{cell} = \frac{0.0591}{n} \log K_c$
(b) $E^\circ_{cell} = \frac{n}{0.0591} \log K_c$
(c) $E^\circ_{cell} = \frac{0.0591}{n} K_c$
(d) $\log K_c = \frac{0.0591}{n} E^\circ_{cell}$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
Derived directly from $0 = E^\circ_{cell} - \frac{0.0591}{n} \log K_c$.
</details>

**Q2. (JEE Mains Type)** 🔴 For the cell reaction $2Ce^{4+} + Co \rightarrow 2Ce^{3+} + Co^{2+}$, $E^\circ_{cell} = 1.89\ V$. If $E^\circ_{Co^{2+}/Co} = -0.28\ V$, what is the value of $\log K_c$ for the reaction?<br>
(a) $\frac{2 \times 1.89}{0.0591}$
(b) $\frac{2 \times (1.89 - 0.28)}{0.0591}$
(c) $\frac{1 \times 1.89}{0.0591}$
(d) $\frac{3 \times 1.89}{0.0591}$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
The value of $E^\circ_{Co^{2+}/Co}$ is extra information designed to distract you. You already have the $E^\circ_{cell}$ ($1.89\ V$).
Cobalt goes from 0 to +2 ($n=2$).
Formula is simply $\log K_c = \frac{n E^\circ_{cell}}{0.0591} = \frac{2 \times 1.89}{0.0591}$.
</details>

**Q3. (Exemplar Type)** 🟡 When a cell reaction reaches equilibrium, which of the following happens?<br>
(a) EMF of the cell becomes maximum.
(b) The standard EMF of the cell becomes zero.
(c) The EMF of the cell becomes zero.
(d) The reaction quotient $Q$ becomes zero.

<details><summary><b>Answer</b></summary>
**Answer: (c)**
The actual operating voltage ($E_{cell}$) drops to zero. Standard EMF is a constant, and $Q$ becomes $K_c$.
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🟡 ⭐ Consider a cell $A\ |\ A^{2+}\ ||\ B^{2+}\ |\ B$. The equilibrium constant $K_c$ is $10^{20}$.
(a) What is the standard cell potential $E^\circ_{cell}$?<br>
(b) If you build this cell using $1\ M$ solutions of both, will the initial voltmeter reading be equal to, greater than, or less than $E^\circ_{cell}$?<br>
(c) What will the voltmeter read after a very long time?<br>

<details><summary><b>Solution</b></summary>
(a) $\log(10^{20}) = 20$. 
$20 = \frac{2 \times E^\circ_{cell}}{0.0591} \implies E^\circ_{cell} = 10 \times 0.0591 = \textbf{+0.591\ V}$.
(b) If you use $1\ M$ solutions, $[Products] = [Reactants] = 1$. The $Q$ value is 1, and $\log(1) = 0$. The Nernst equation becomes $E_{cell} = E^\circ_{cell} - 0$. The initial reading will be **exactly equal** to $E^\circ_{cell}$ ($0.591\ V$).
(c) After a very long time, equilibrium is reached. The voltmeter will read **$0.00\ V$**.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 Deduce the relationship between Standard EMF ($E^\circ_{cell}$) and Equilibrium Constant ($K_c$). *(2 marks)*
<details><summary><b>Model Answer</b></summary>
From the Nernst equation:
$E_{cell} = E^\circ_{cell} - \frac{2.303 RT}{nF} \log Q$
At equilibrium, the cell potential drops to zero ($E_{cell} = 0$) and the reaction quotient becomes the equilibrium constant ($Q = K_c$).
Substituting these values:
$0 = E^\circ_{cell} - \frac{2.303 RT}{nF} \log K_c$
Therefore: $E^\circ_{cell} = \frac{2.303 RT}{nF} \log K_c$.
</details>

**Q2.** 🟡 Calculate the equilibrium constant of the reaction: $Cu(s) + 2Ag^+(aq) \rightarrow Cu^{2+}(aq) + 2Ag(s)$. $E^\circ_{cell} = 0.46\ V$. *(2 marks)*
<details><summary><b>Model Answer</b></summary>
$n = 2$.
$\log K_c = \frac{n \times E^\circ_{cell}}{0.0591} = \frac{2 \times 0.46}{0.0591} = 15.56$
$K_c = \text{Antilog}(15.56) = \text{Antilog}(15 + 0.56) = 10^{15} \times 3.63$
$K_c = \textbf{3.63} \times \textbf{10}^{\textbf{15}}$.
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🔴 ⭐ For the following half-cell reactions:
$A^{2+} + 2e^- \rightarrow A \quad E^\circ = -0.24\ V$
$B^{2+} + 2e^- \rightarrow B \quad E^\circ = +0.80\ V$
$C^{2+} + 2e^- \rightarrow C \quad E^\circ = -0.14\ V$
Which of the following reactions will have the largest equilibrium constant ($K_c$)?<br>
(a) $A + B^{2+} \rightarrow A^{2+} + B$
(b) $C + B^{2+} \rightarrow C^{2+} + B$
(c) $A + C^{2+} \rightarrow A^{2+} + C$
(d) $C + A^{2+} \rightarrow C^{2+} + A$

<details><summary><b>Answer</b></summary>
**Answer: (a)**
$K_c$ is exponentially proportional to $E^\circ_{cell}$. The largest $K_c$ comes from the reaction with the largest $E^\circ_{cell}$.
To maximize $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$, we need the highest cathode (most positive) and lowest anode (most negative).
Highest is B (+0.80 V) $\rightarrow$ Cathode.
Lowest is A (-0.24 V) $\rightarrow$ Anode.
Reaction: A oxidizes, B reduces $\implies A + B^{2+} \rightarrow A^{2+} + B$.
$E^\circ_{cell} = 0.80 - (-0.24) = 1.04\ V$. This will yield the largest $K_c$.
</details>

**Q2.** 🔴 Given the equilibrium constants:
Reaction 1: $X + Y^+ \rightleftharpoons X^+ + Y \quad K_1 = 10^5$
Reaction 2: $Y + Z^+ \rightleftharpoons Y^+ + Z \quad K_2 = 10^8$
Calculate the standard cell potential $E^\circ_{cell}$ for the reaction $X + Z^+ \rightleftharpoons X^+ + Z$ at $298\ K$. (Assume $n=1$ for all).

<details><summary><b>Answer</b></summary>
**Answer:**
This uses Hess's law for equilibrium constants. 
If you add Reaction 1 and Reaction 2:
$(X + Y^+) + (Y + Z^+) \rightleftharpoons (X^+ + Y) + (Y^+ + Z)$
The $Y$ and $Y^+$ terms cancel out, leaving:
$X + Z^+ \rightleftharpoons X^+ + Z$ (The target reaction).
When you add chemical equations, you **multiply** their equilibrium constants.
$K_{target} = K_1 \times K_2 = 10^5 \times 10^8 = 10^{13}$.
Now find $E^\circ_{cell}$ for the target reaction ($n=1$):
$\log K_{target} = 13$.
$13 = \frac{1 \times E^\circ_{cell}}{0.0591} \implies E^\circ_{cell} = 13 \times 0.0591 = \textbf{+0.7683\ V}$.
</details>

---

*Next: [Chapter 10 — Gibbs Free Energy and Cell Potential →](./10_gibbs_free_energy.md)*
