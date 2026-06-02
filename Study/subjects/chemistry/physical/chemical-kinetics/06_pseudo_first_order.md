# Chapter 6: Pseudo First Order & Special Cases<br>
## Part III — First Order Kinetics Deep Dive

---

## 🎯 Stage 1: The Core Idea

### The Scene

Imagine you're making hundreds of cups of tea for a massive wedding. You need tea bags and boiling water. The rate at which you make tea depends on both the number of tea bags and the amount of water. 
But wait... you are standing next to a literal *river* of boiling water. The water is practically infinite. Now, the rate at which you make tea depends *only* on how many tea bags you can grab. 
Because the water is in vast excess, its amount doesn't change enough to affect the rate.

This is exactly what happens in a **Pseudo First Order Reaction**.

> A **pseudo first order reaction** is a reaction that is not truly of the first order (its molecularity is $\geq 2$), but under certain conditions, it behaves as a first-order reaction. This typically happens when one of the reacting molecules is present in such large excess that its concentration remains essentially constant throughout the reaction.

### Molecularity vs. Order

For a reaction like hydrolysis of an ester:
$\text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O} \xrightarrow{H^+} \text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH}$

- **Molecularity:** 2 (Bimolecular — both ester and water must collide).
- **True Rate Law:** $\text{Rate} = k[\text{Ester}][\text{Water}]$
- **Condition:** Water is the solvent and is present in huge excess (e.g., $55.5\text{ M}$). During the reaction, the concentration of water barely changes.
- **Pseudo Rate Law:** $\text{Rate} = k'[\text{Ester}]$ 
*(where $k' = k[\text{Water}]$ is the pseudo first-order rate constant)*.
- **Apparent Order:** 1

> ⚠️ **Classic Trap:** The true rate constant ($k$) and pseudo rate constant ($k'$) have different units! $k'$ has the unit of a first order reaction ($\text{time}^{-1}$), while the true $k$ has the unit of a second order reaction ($\text{L mol}^{-1}\text{time}^{-1}$).

---

## 🔬 Stage 2: The Formula Lab

In this chapter, we don't just calculate theoretical concentrations; we measure real physical properties. 

### Case 1: Gas Phase First Order Reactions

For $A(g) \rightarrow B(g) + C(g)$:
Let initial pressure of $A$ be $P_i$.
At time $t$, pressure of $A$ drops by $x$. $P_A = P_i - x$.
Pressures of $B$ and $C$ are $x$ each.
Total pressure $P_t = (P_i - x) + x + x = P_i + x$.
Therefore, $x = P_t - P_i$.
The remaining pressure of reactant $A$ is $P_A = P_i - x = 2P_i - P_t$.

**The Formula:**
$$k = \frac{2.303}{t} \log\left(\frac{P_i}{2P_i - P_t}\right)$$

### Case 2: Hydrolysis of Esters (Acid-Catalyzed)

The reaction is monitored by titrating with a base (like NaOH) at different times.
- $V_0$ (volume of base at $t=0$) is proportional to the constant acid catalyst concentration $[H^+]$.
- $V_\infty$ (volume at $t=\infty$) is proportional to the acid catalyst + total acetic acid formed from ester.
- The initial amount of ester $\propto (V_\infty - V_0)$.
- The remaining amount of ester at time $t \propto (V_\infty - V_t)$.

**The Formula:**
$$k = \frac{2.303}{t} \log\left(\frac{V_\infty - V_0}{V_\infty - V_t}\right)$$

### Case 3: Inversion of Cane Sugar (Sucrose)

$\text{Sucrose} + \text{H}_2\text{O} \xrightarrow{H^+} \text{Glucose} + \text{Fructose}$
Tracked by optical rotation ($r$):
- $r_0$ = rotation at $t=0$
- $r_t$ = rotation at time $t$
- $r_\infty$ = rotation at $t=\infty$

**The Formula:**
$$k = \frac{2.303}{t} \log\left(\frac{r_0 - r_\infty}{r_t - r_\infty}\right)$$

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Gas Phase Pressure Monitoring

**The Pattern:** You are given initial pressure $P_i$ and total pressure $P_t$ at time $t$. Find the rate constant $k$.

#### Solved Example 6.1
**Q:** The following data were obtained during the first order thermal decomposition of $N_2O_5$ at constant volume:
$2N_2O_5(g) \rightarrow 2N_2O_4(g) + O_2(g)$
At $t=0$, Total Pressure = $0.5\text{ atm}$.
At $t=100\text{ s}$, Total Pressure = $0.512\text{ atm}$.
Calculate the rate constant. 🔴

**Solution:**
```
Reaction: 2 N_2O_5 -> 2 N_2O_4 + O_2
At t=0:     0.5         0        0
At t=100:   0.5 - 2x    2x       x

Total pressure P_t = (0.5 - 2x) + 2x + x = 0.5 + x
At t=100, P_t = 0.512 atm
0.5 + x = 0.512  =>  x = 0.012 atm

Pressure of N_2O_5 at t=100 is P_A = 0.5 - 2(0.012) = 0.5 - 0.024 = 0.476 atm

Now use the first order formula:
k = (2.303 / t) * log(P_i / P_A)
k = (2.303 / 100) * log(0.5 / 0.476)
k = (2.303 / 100) * log(1.05)
Given log(1.05) = 0.0212
k = (2.303 / 100) * 0.0212 = 4.88 * 10^{-4} s^{-1}
```
*(Notice how the stoichiometry changes the standard formula! Always map out the reaction.)*

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 6.1a | For $A \rightarrow B + C$, $P_i = 100\text{ mm}$, $P_t = 120\text{ mm}$ at $10\text{ min}$. Find $k$. | 🟡 |
| 6.1b | For $A \rightarrow 2B + C$, if $P_i = 50\text{ atm}$ and $P_t = 60\text{ atm}$ at $t$, find $P_A$. | 🟡 |
| 6.1c | For $2N_2O_5(g) \rightarrow 4NO_2(g) + O_2(g)$, $P_i = 100\text{ kPa}$, $P_t = 112\text{ kPa}$ at $50\text{ s}$. Find $k$. | 🟡 |
| 6.1d | For $A \rightarrow 3B(g)$, initial pressure $= P_i$. At time $t$, total pressure $= 2P_i$. Find the fraction of $A$ decomposed. | 🟡 |
| 6.1e | For $2A(g) \rightarrow B(g) + 3C(g)$, $P_i = 200\text{ mmHg}$, $P_t = 280\text{ mmHg}$ at $t = 20\text{ min}$. Find $k$. | 🔴 |
| 6.1f | The half-life of $A(g) \rightarrow B(g) + C(g)$ is $10\text{ min}$. If $P_i = 1\text{ atm}$, find $P_t$ after $20\text{ min}$. | 🔴 |
| 6.1g | For $A(g) \rightarrow 2B(g) + C(g)$, $P_i = 0.5\text{ atm}$. At $t = 15\text{ min}$, partial pressure of $B$ is $0.6\text{ atm}$. Find $k$. | 🔴 |
| 6.1h | For $A(g) \rightarrow B(g) + C(g)$, $P_i = 1.6\text{ atm}$. Find $P_t$ after $5$ half-lives. | 🟡 |
| 6.1i | $SO_2Cl_2(g) \rightarrow SO_2(g) + Cl_2(g)$; $P_i = 0.4\text{ atm}$; $P_t = 0.7\text{ atm}$ at $60\text{ min}$. Find $k$ and the fraction decomposed. | 🔴 ⭐ |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**6.1a:**
$P_t = 100 + x = 120 \implies x = 20$.
$P_A = P_i - x = 100 - 20 = 80\text{ mm}$.
$k = \frac{2.303}{10} \log\left(\frac{100}{80}\right) = 0.2303 \times \log(1.25) = 0.2303 \times 0.0969 = 0.0223\text{ min}^{-1}$.

**6.1b:**
$A \rightarrow 2B + C$.
$P_t = (50 - x) + 2x + x = 50 + 2x = 60 \implies 2x = 10 \implies x = 5\text{ atm}$.
$P_A = 50 - x = 45\text{ atm}$.

**6.1c:**
$2N_2O_5 \rightarrow 4NO_2 + O_2$.
$P_t = (100 - 2x) + 4x + x = 100 + 3x = 112 \implies 3x = 12 \implies x = 4\text{ kPa}$.
$P_{N_2O_5} = 100 - 2(4) = 92\text{ kPa}$.
$k = \frac{2.303}{50} \log\left(\frac{100}{92}\right) = \frac{2.303}{50} \log(1.087)$
$\log(1.087) \approx 0.0362$
$k = \frac{2.303}{50} \times 0.0362 = 1.67 \times 10^{-3}\text{ s}^{-1}$.

**6.1d:**
$A \rightarrow 3B$.
$P_t = (P_i - x) + 3x = P_i + 2x = 2P_i \implies 2x = P_i \implies x = P_i/2$.
Fraction decomposed $= x/P_i = 0.5$ or $50\%$.

**6.1e:**
$2A \rightarrow B + 3C$.
$P_t = (200 - 2x) + x + 3x = 200 + 2x = 280 \implies 2x = 80 \implies x = 40\text{ mmHg}$.
$P_A = 200 - 2(40) = 120\text{ mmHg}$.
$k = \frac{2.303}{20} \log\left(\frac{200}{120}\right) = \frac{2.303}{20} \log\left(\frac{5}{3}\right)$
$\log(5/3) = 0.699 - 0.477 = 0.222$
$k = \frac{2.303}{20} \times 0.222 = 0.0256\text{ min}^{-1}$.

**6.1f:**
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{10} = 0.0693\text{ min}^{-1}$.
After $20\text{ min}$, $t = 20$ min $= 2$ half-lives.
Fraction remaining $= (1/2)^2 = 1/4$, so $P_A = 1 \times \frac{1}{4} = 0.25\text{ atm}$.
$P_A = P_i - x \implies 0.25 = 1 - x \implies x = 0.75\text{ atm}$.
$P_t = P_i + x = 1 + 0.75 = 1.75\text{ atm}$.

**6.1g:**
$A \rightarrow 2B + C$.
At $t=15$, $P_B = 2x = 0.6 \implies x = 0.3\text{ atm}$.
$P_A = 0.5 - 0.3 = 0.2\text{ atm}$.
$k = \frac{2.303}{15} \log\left(\frac{0.5}{0.2}\right) = \frac{2.303}{15} \log(2.5)$
$\log(2.5) = \log(5/2) = 0.699 - 0.301 = 0.398$
$k = \frac{2.303}{15} \times 0.398 = 0.0611\text{ min}^{-1}$.

**6.1h:**
After $5$ half-lives, $P_A = P_i \left(\frac{1}{2}\right)^5 = 1.6 \times \frac{1}{32} = 0.05\text{ atm}$.
$P_A = P_i - x \implies 0.05 = 1.6 - x \implies x = 1.55\text{ atm}$.
$P_t = P_i + x = 1.6 + 1.55 = 3.15\text{ atm}$.

**6.1i:**
$SO_2Cl_2 \rightarrow SO_2 + Cl_2$.
$P_t = (0.4 - x) + x + x = 0.4 + x = 0.7 \implies x = 0.3\text{ atm}$.
$P_{A} = 0.4 - 0.3 = 0.1\text{ atm}$.
$k = \frac{2.303}{60} \log\left(\frac{0.4}{0.1}\right) = \frac{2.303}{60} \log(4) = \frac{2.303}{60} \times 0.602 = 0.0231\text{ min}^{-1}$.
Fraction decomposed $= x/P_i = 0.3/0.4 = 0.75$ or $75\%$.
</details>

---

### Type 2: Titration and Optical Rotation

**The Pattern:** Substitute $V$ or $r$ values directly into their respective modified first-order formulas.

#### Solved Example 6.2
**Q:** In a pseudo first order hydrolysis of an ester, the volume of NaOH used at $t=0$, $t=30\text{ min}$, and $t=\infty$ are $10\text{ ml}$, $20\text{ ml}$, and $40\text{ ml}$ respectively. Calculate the rate constant.<br> 🟡

**Solution:**
```
Formula: k = (2.303 / t) * log[ (V_inf - V_0) / (V_inf - V_t) ]
V_0 = 10, V_t = 20, V_inf = 40, t = 30
k = (2.303 / 30) * log[ (40 - 10) / (40 - 20) ]
k = (2.303 / 30) * log[ 30 / 20 ]
k = (2.303 / 30) * log(1.5)
log(1.5) = log(3/2) = 0.477 - 0.301 = 0.176
k = (2.303 / 30) * 0.176 = 0.0135 min^{-1}
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 6.2a | For inversion of sucrose, $r_0 = 35^\circ$, $r_{10\text{min}} = 10^\circ$, $r_\infty = -15^\circ$. Find $k$. | 🔴 |
| 6.2b | For acid-catalyzed hydrolysis of ester, $V_0 = 5\text{ ml}$, $V_t = 15\text{ ml}$ at $t = 20\text{ min}$, $V_\infty = 35\text{ ml}$. Find $k$. | 🟡 |
| 6.2c | For inversion of sucrose, $r_0 = 45^\circ$, $r_t = 20^\circ$ at $t = 15\text{ min}$, $r_\infty = -10^\circ$. Find $k$. | 🟡 |
| 6.2d | In ester hydrolysis, $V_0 = 8\text{ ml}$, $V_\infty = 44\text{ ml}$, $k = 0.0231\text{ min}^{-1}$. Find $V_t$ at $t = 25\text{ min}$. | 🟡 |
| 6.2e | For ester hydrolysis, $V_0 = 10\text{ ml}$, $V_\infty = 50\text{ ml}$, $V_t = 25\text{ ml}$ at $t = 15\text{ min}$. Find the time when $V_t = 40\text{ ml}$. | 🔴 |
| 6.2f | For sucrose inversion, $r_\infty = -10^\circ$, $k = 0.0693\text{ min}^{-1}$, at $t = 5\text{ min}$, $r_t = 20^\circ$. Find $r_0$. | 🔴 |
| 6.2g | In ester hydrolysis, $V_\infty - V_0 = 30\text{ ml}$. If hydrolysis is $75\%$ complete, find $V_t$ in terms of $V_0$. | 🟡 |
| 6.2h | For ester hydrolysis, $V_0 = 4\text{ ml}$, $V_\infty = 34\text{ ml}$. At $t = 10\text{ min}$, ester concentration is $40\%$ of initial. Find $V_t$ and $k$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**6.2a:**
$k = \frac{2.303}{t} \log\left(\frac{r_0 - r_\infty}{r_t - r_\infty}\right)$
$r_0 - r_\infty = 35 - (-15) = 50^\circ$
$r_t - r_\infty = 10 - (-15) = 25^\circ$
$k = \frac{2.303}{10} \log\left(\frac{50}{25}\right) = \frac{2.303}{10} \log(2) = \frac{0.693}{10} = 0.0693\text{ min}^{-1}$.

**6.2b:**
$k = \frac{2.303}{20} \log\left(\frac{35 - 5}{35 - 15}\right) = \frac{2.303}{20} \log\left(\frac{30}{20}\right)$
$= \frac{2.303}{20} \log(1.5) = \frac{2.303}{20} \times 0.176 = 0.0203\text{ min}^{-1}$.

**6.2c:**
$k = \frac{2.303}{15} \log\left(\frac{45 - (-10)}{20 - (-10)}\right) = \frac{2.303}{15} \log\left(\frac{55}{30}\right) = \frac{2.303}{15} \log(1.833)$
$\log(1.833) \approx 0.263$
$k = \frac{2.303}{15} \times 0.263 = 0.0404\text{ min}^{-1}$.

**6.2d:**
$k = \frac{2.303}{t} \log\left(\frac{V_\infty - V_0}{V_\infty - V_t}\right)$
$0.0231 = \frac{2.303}{25} \log\left(\frac{44 - 8}{44 - V_t}\right)$
$0.0231 \times \frac{25}{2.303} = \log\left(\frac{36}{44 - V_t}\right)$
$0.251 = \log\left(\frac{36}{44 - V_t}\right)$
$10^{0.251} = 1.78 = \frac{36}{44 - V_t}$
$44 - V_t = \frac{36}{1.78} = 20.2$
$V_t = 44 - 20.2 = 23.8\text{ ml}$.

**6.2e:**
Find $k$: $k = \frac{2.303}{15} \log\left(\frac{50 - 10}{50 - 25}\right) = \frac{2.303}{15} \log\left(\frac{40}{25}\right) = \frac{2.303}{15} \log(1.6)$
$\log(1.6) = 0.204$, $k = \frac{2.303}{15} \times 0.204 = 0.0313\text{ min}^{-1}$.
Find $t$ when $V_t = 40$:
$0.0313 = \frac{2.303}{t} \log\left(\frac{50 - 10}{50 - 40}\right) = \frac{2.303}{t} \log\left(\frac{40}{10}\right) = \frac{2.303}{t} \log(4)$
$t = \frac{2.303 \times 0.602}{0.0313} = \frac{1.386}{0.0313} = 44.3\text{ min}$.

**6.2f:**
$k = \frac{2.303}{t} \log\left(\frac{r_0 - r_\infty}{r_t - r_\infty}\right)$
$0.0693 = \frac{2.303}{5} \log\left(\frac{r_0 - (-10)}{20 - (-10)}\right)$
$0.0693 \times \frac{5}{2.303} = \log\left(\frac{r_0 + 10}{30}\right)$
$0.1505 = \log\left(\frac{r_0 + 10}{30}\right)$
$10^{0.1505} = 1.414 = \frac{r_0 + 10}{30}$
$r_0 + 10 = 42.4 \implies r_0 = 32.4^\circ$.

**6.2g:**
At $75\%$ completion, $25\%$ ester remains.
$\frac{[\text{Ester}]_t}{[\text{Ester}]_0} = \frac{V_\infty - V_t}{V_\infty - V_0} = \frac{1}{4}$
$\frac{V_\infty - V_t}{30} = \frac{1}{4} \implies V_\infty - V_t = 7.5$
$V_t = V_\infty - 7.5 = (V_0 + 30) - 7.5 = V_0 + 22.5\text{ ml}$.

**6.2h:**
$40\%$ remains $\implies \frac{V_\infty - V_t}{V_\infty - V_0} = 0.4$
$\frac{34 - V_t}{34 - 4} = \frac{34 - V_t}{30} = 0.4$
$34 - V_t = 12 \implies V_t = 22\text{ ml}$.
$k = \frac{2.303}{10} \log\left(\frac{1}{0.4}\right) = \frac{2.303}{10} \log(2.5)$
$= \frac{2.303}{10} \times 0.398 = 0.0917\text{ min}^{-1}$.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 6.M1 | The decomposition of $H_2O_2$ is monitored via $KMnO_4$ titration. At $t=0$, $V_0 = 25\text{ ml}$. At $t=10\text{ min}$, $V_t = 20\text{ ml}$. What is the average rate of reaction from 0 to 10 min? (Hint: rate refers to concentration drop, but $V$ is proportional to concentration. Assume $[H_2O_2]_0 = 0.5\text{ M}$ corresponds to $25\text{ ml}$) | T2 | 🔴 |
| 6.M2 | In a reaction $A + B \rightarrow$ products, $[B]_0 = 1.0\text{ M}$ while $[A]_0 = 0.01\text{ M}$. True $k_2 = 0.05\text{ L mol}^{-1}\text{min}^{-1}$. Find pseudo $k'$. | T2 | 🟡 |
| 6.M3 | $A(g) \rightarrow 2B(g)$; $P_i = 0.8\text{ atm}$, $P_t = 1.2\text{ atm}$ at $t = 20\text{ min}$. Also, $t_{50\%}$ is same at different $P_i$. Find $k$ and identify reaction order. | T1 | 🟡 |
| 6.M4 | An ester hydrolysis is pseudo first order. In $0.05\text{ M HCl}$, $k' = 0.025\text{ min}^{-1}$. If the same ester is hydrolyzed in $0.025\text{ M H}_2\text{SO}_4$, find $k'$. | T2 | 🔴 |
| 6.M5 | For $A(\text{limiting}) + B(\text{excess}) \rightarrow$ products, $[B]_0 = 25[A]_0$. During reaction, $[B]$ drops to $24.5[A]_0$. Is the pseudo first-order assumption valid? Justify. | T2 | 🔴 |
| 6.M6 | $A(g) \rightarrow B(g) + C(g)$: $P_i = 0.6\text{ atm}$, $P_t = 0.9\text{ atm}$ at $30\text{ min}$. Separate titration: $V_0 = 10\text{ ml}$, $V_\infty = 30\text{ ml}$, $V_t = 20\text{ ml}$ at same $t$. Compare $k$ values. | T1,T2 | 🔴 |
| 6.M7 | For pseudo first order $k' = k[B]_0$. If $[B]_0$ is doubled, by what factor does $t_{1/2}$ change? If $[B]_0$ is halved? | T2 | 🟡 |
| 6.M8 | Reaction $2A + B \rightarrow$ products with $[B]_0 \gg [A]_0$. Data: $[B]_0 = 0.1\text{ M} \Rightarrow k' = 0.02\text{ min}^{-1}$, $[B]_0 = 0.2\text{ M} \Rightarrow k' = 0.04\text{ min}^{-1}$, $[B]_0 = 0.4\text{ M} \Rightarrow k' = 0.08\text{ min}^{-1}$. Find true order w.r.t. $B$. | T2 | 🔴 ⭐ |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**6.M1:**
If $25\text{ ml}$ corresponds to $0.5\text{ M}$, then the proportionality constant is $0.5 / 25 = 0.02\text{ M/ml}$.
At $t=10$, $V_t = 20\text{ ml}$, so concentration is $20 \times 0.02 = 0.4\text{ M}$.
Average rate $= \frac{-\Delta[C]}{\Delta t} = \frac{-(0.4 - 0.5)}{10} = \frac{0.1}{10} = 0.01\text{ M min}^{-1}$.

**6.M2:**
$k' = k_2[B]_0 = 0.05 \times 1.0 = 0.05\text{ min}^{-1}$.

**6.M3:**
$A \rightarrow 2B$.
$P_t = (0.8 - x) + 2x = 0.8 + x = 1.2 \implies x = 0.4\text{ atm}$.
$P_A = 0.8 - 0.4 = 0.4\text{ atm}$.
$k = \frac{2.303}{20} \log\left(\frac{0.8}{0.4}\right) = \frac{2.303}{20} \log(2) = \frac{0.693}{20} = 0.0347\text{ min}^{-1}$.
Since $t_{50\%}$ is independent of $P_i$, the reaction is first order.

**6.M4:**
$k' \propto [H^+]$.
In $0.05\text{ M HCl}$, $[H^+] = 0.05\text{ M}$.
In $0.025\text{ M H}_2\text{SO}_4$, $[H^+] = 2 \times 0.025 = 0.05\text{ M}$.
$\therefore k'$ in $H_2SO_4$ is also $0.025\text{ min}^{-1}$.

**6.M5:**
$[B]_0 = 25[A]_0$. Final $[B] = 24.5[A]_0$.
Change in $[B] = 0.5[A]_0$.
Percent change $= \frac{0.5}{25} \times 100 = 2\%$.
Since $[B]$ changes by only $2\%$, the pseudo first-order assumption (constant $[B]$) is valid.

**6.M6:**
Gas: $P_t = 0.6 + x = 0.9 \implies x = 0.3$, $P_A = 0.3$.
$k = \frac{2.303}{30} \log\left(\frac{0.6}{0.3}\right) = \frac{2.303}{30} \times 0.301 = 0.0231\text{ min}^{-1}$.
Titration: $k = \frac{2.303}{30} \log\left(\frac{30 - 10}{30 - 20}\right) = \frac{2.303}{30} \log(2) = 0.0231\text{ min}^{-1}$.
$k$ values are equal, confirming first-order kinetics in both phases.

**6.M7:**
$t_{1/2} = \frac{0.693}{k'} = \frac{0.693}{k[B]_0}$.
If $[B]_0$ is doubled, $t_{1/2}$ is halved.
If $[B]_0$ is halved, $t_{1/2}$ is doubled.

**6.M8:**
$k'$ doubles when $[B]_0$ doubles: $\frac{k'_2}{k'_1} = \frac{0.04}{0.02} = 2 = \frac{0.2}{0.1}$.
$k' \propto [B]_0^1$, so order w.r.t. $B$ is $1$.
$k' = k[B]_0$, confirming pseudo first-order behavior.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 6.B1 | What is a pseudo first-order reaction? Give one example. | 🟢 |
| 6.B2 | Why does the hydrolysis of ethyl acetate behave as a first-order reaction even though its molecularity is 2? ⭐ | 🟡 |
| 6.B3 | Write the expression for the rate constant for the reaction $A(g) \rightarrow B(g) + C(g)$ in terms of initial pressure $p_i$ and total pressure $p_t$. | 🟢 |
| 6.B4 | Derive the expression for the rate constant for the first-order gas phase reaction $A(g) \rightarrow B(g) + C(g)$ in terms of initial and total pressure. | 🟡 |
| 6.B5 | Explain why the hydrolysis of methyl acetate in the presence of dilute HCl is considered a pseudo first-order reaction. | 🟢 |
| 6.B6 | Distinguish between the true rate constant and the pseudo rate constant for ester hydrolysis. How do their units differ? | 🟡 |
| 6.B7 | Show that for a pseudo first-order reaction, the half-life is independent of the initial concentration of the limiting reactant. | 🟡 |
| 6.B8 | How does increasing the concentration of the acid catalyst affect the pseudo first-order rate constant for ester hydrolysis? | 🟢 |
| 6.B9 | In the inversion of cane sugar, the optical rotation changes from positive to negative as the reaction proceeds. Explain why. | 🟡 |
| 6.B10 | Derive the relationship between the rate constant and the titration volumes ($V_0, V_t, V_\infty$) for the acid-catalyzed hydrolysis of an ester. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**6.B1:**
A pseudo first-order reaction is a reaction that is not truly first order (molecularity $>1$) but behaves as first order under specific conditions, usually when one reactant is in large excess. Example: Acid-catalyzed hydrolysis of ethyl acetate.

**6.B2:**
Because water is present in such large excess (as a solvent) that its concentration practically remains constant throughout the reaction. Thus, the rate becomes dependent only on the concentration of ethyl acetate, making the apparent order 1.

**6.B3:**
$k = \frac{2.303}{t} \log\left(\frac{p_i}{2p_i - p_t}\right)$.

**6.B4:**
For $A(g) \rightarrow B(g) + C(g)$:
$P_t = (P_i - x) + x + x = P_i + x \implies x = P_t - P_i$.
$P_A = P_i - x = 2P_i - P_t$.
$k = \frac{2.303}{t} \log\frac{P_i}{P_A} = \frac{2.303}{t} \log\left(\frac{P_i}{2P_i - P_t}\right)$.

**6.B5:**
Molecularity of ester hydrolysis is 2 (bimolecular). Water is the solvent in vast excess ($\sim 55.5\text{ M}$). Its concentration remains practically constant during the reaction. Hence, rate depends only on ester concentration, making it appear first order — a pseudo first-order reaction.

**6.B6:**
True $k$ has units of $\text{L mol}^{-1}\text{time}^{-1}$ (second order). Pseudo $k'$ has units of $\text{time}^{-1}$ (first order). $k' = k[\text{Water}]$, so $k'$ is numerically larger and has different dimensions.

**6.B7:**
For pseudo first order: $\text{Rate} = k'[A]$ where $k' = k[B]_0$ is constant.
$k' = \frac{2.303}{t} \log\frac{[A]_0}{[A]}$.
At $t_{1/2}$, $[A] = [A]_0/2$.
$t_{1/2} = \frac{2.303}{k'} \log(2) = \frac{0.693}{k'}$, independent of $[A]_0$.

**6.B8:**
$k' = k[H^+]$. Increasing $[H^+]$ increases $k'$ proportionally, speeding up the reaction.

**6.B9:**
Sucrose is dextrorotatory (positive rotation). Upon hydrolysis, it produces glucose (dextrorotatory) and fructose (strongly laevorotatory). The mixture becomes laevorotatory overall because fructose's negative rotation dominates. Hence $r_0 > 0$ and $r_\infty < 0$.

**6.B10:**
$V_0 \propto [H^+]$ (catalyst). $V_\infty \propto [H^+] + [\text{acid produced}]$.
$\therefore V_\infty - V_0 \propto$ initial ester, $V_\infty - V_t \propto$ ester remaining.
$\frac{[\text{Ester}]_t}{[\text{Ester}]_0} = \frac{V_\infty - V_t}{V_\infty - V_0}$.
$k' = \frac{2.303}{t} \log\left(\frac{V_\infty - V_0}{V_\infty - V_t}\right)$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q6.J1 🟡**
In a pseudo-first order hydrolysis of an ester in water, the following ester concentration data was obtained:
At $t=0\text{ min}$, $[\text{Ester}] = 0.55\text{ M}$
At $t=30\text{ min}$, $[\text{Ester}] = 0.31\text{ M}$
At $t=60\text{ min}$, $[\text{Ester}] = 0.17\text{ M}$
Calculate the average rate of reaction between 30 and 60 minutes.
(A) $4.67 \times 10^{-3}\text{ M/min}$
(B) $1.98 \times 10^{-2}\text{ M/min}$
(C) $2.44 \times 10^{-3}\text{ M/min}$
(D) $8.00 \times 10^{-3}\text{ M/min}$

**Q6.J2 🔴 ⭐**
The hydrolysis of an ester is carried out separately in $0.05\text{ M HCl}$ and $0.05\text{ M H}_2\text{SO}_4$. Which of the following is true for the pseudo first-order rate constant ($k'$) of the reaction?
(A) $k'_{HCl} > k'_{H_2SO_4}$
(B) $k'_{HCl} < k'_{H_2SO_4}$
(C) $k'_{HCl} = k'_{H_2SO_4}$
(D) Cannot be compared

**Q6.J3 🟡**
For the first-order gas phase reaction $A(g) \rightarrow B(g) + C(g)$, $P_i = 0.8\text{ atm}$ and $P_t = 1.2\text{ atm}$ at $t = 20\text{ min}$. The rate constant $k$ is:
(A) $0.0347\text{ min}^{-1}$
(B) $0.0693\text{ min}^{-1}$
(C) $0.0231\text{ min}^{-1}$
(D) $0.0173\text{ min}^{-1}$

**Q6.J4 🟡**
The inversion of sucrose follows pseudo first-order kinetics. If $r_0 = 32^\circ$, $r_\infty = -16^\circ$, and half-life is 10 min, find the rotation after 20 min.
(A) $8^\circ$
(B) $-4^\circ$
(C) $4^\circ$
(D) $-8^\circ$

**Q6.J5 🟡**
In the acid-catalyzed hydrolysis of an ester, $V_0 = 20\text{ ml}$, $V_\infty = 50\text{ ml}$. At what time will $V_t = 35\text{ ml}$ if $k = 0.0231\text{ min}^{-1}$?
(A) $15\text{ min}$
(B) $20\text{ min}$
(C) $30\text{ min}$
(D) $25\text{ min}$

**Q6.J6 🔴**
Two experiments for ester hydrolysis: (i) $0.04\text{ M HCl}$, (ii) $0.02\text{ M H}_2\text{SO}_4$. Ratio of pseudo rate constants $k'_I : k'_{II}$ is:
(A) $1:1$
(B) $2:1$
(C) $1:2$
(D) $4:1$

**Q6.J7 🔴**
For $2A(g) \rightarrow 3B(g) + C(g)$, $P_i = 200\text{ mmHg}$. At $t = 20\text{ min}$, $P_t = 280\text{ mmHg}$. The rate constant is:
(A) $0.0347\text{ min}^{-1}$
(B) $0.0173\text{ min}^{-1}$
(C) $0.0256\text{ min}^{-1}$
(D) $0.0139\text{ min}^{-1}$

**Q6.J8 🟢**
For a pseudo first-order reaction $A + B \rightarrow$ products ($B$ in excess), if $[B]_0$ is doubled, the half-life:
(A) remains the same
(B) is halved
(C) is doubled
(D) becomes four times

**Q6.J9 🟢**
After 3 half-lives, the percentage of ester remaining in a pseudo first-order hydrolysis is:
(A) $12.5\%$
(B) $25\%$
(C) $6.25\%$
(D) $50\%$

**Q6.J10 🔴 ⭐**
The rate constant for hydrolysis of an ester in $0.10\text{ M HCl}$ is $4.0 \times 10^{-3}\text{ min}^{-1}$. In $0.05\text{ M H}_2\text{SO}_4$, the rate constant will be approximately:
(A) $2.0 \times 10^{-3}\text{ min}^{-1}$
(B) $4.0 \times 10^{-3}\text{ min}^{-1}$
(C) $8.0 \times 10^{-3}\text{ min}^{-1}$
(D) $1.0 \times 10^{-3}\text{ min}^{-1}$

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**6.J1 → Answer: (A)**
Average rate $= \frac{-\Delta[\text{Ester}]}{\Delta t} = \frac{-(0.17 - 0.31)}{60 - 30} = \frac{0.14}{30} \approx 4.67 \times 10^{-3}\text{ M/min}$.

**6.J2 → Answer: (B)**
The pseudo rate constant $k'$ depends on the concentration of the catalyst $H^+$.
In $0.05\text{ M HCl}$, $[H^+] = 0.05\text{ M}$.
In $0.05\text{ M H}_2\text{SO}_4$, $[H^+] = 2 \times 0.05 = 0.10\text{ M}$.
Since $[H^+]$ is higher in sulfuric acid, the rate constant $k'$ will be greater.

**6.J3 → Answer: (A)**
$P_t = P_i + x \implies 1.2 = 0.8 + x \implies x = 0.4\text{ atm}$.
$P_A = 0.8 - 0.4 = 0.4\text{ atm}$.
$k = \frac{2.303}{20} \log\left(\frac{0.8}{0.4}\right) = \frac{2.303}{20} \log(2) = 0.0347\text{ min}^{-1}$.

**6.J4 → Answer: (B)**
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{10} = 0.0693\text{ min}^{-1}$.
After $20\text{ min}$ (2 half-lives), $\frac{r_t - r_\infty}{r_0 - r_\infty} = \frac{1}{4}$.
$\frac{r_t + 16}{32 + 16} = \frac{r_t + 16}{48} = \frac{1}{4} \implies r_t + 16 = 12 \implies r_t = -4^\circ$.

**6.J5 → Answer: (C)**
$k = \frac{2.303}{t} \log\left(\frac{V_\infty - V_0}{V_\infty - V_t}\right)$
$0.0231 = \frac{2.303}{t} \log\left(\frac{50 - 20}{50 - 35}\right) = \frac{2.303}{t} \log\left(\frac{30}{15}\right) = \frac{2.303}{t} \log(2)$
$t = \frac{2.303 \times 0.3010}{0.0231} = \frac{0.693}{0.0231} = 30\text{ min}$.

**6.J6 → Answer: (A)**
$k' \propto [H^+]$.
(i) $0.04\text{ M HCl}$: $[H^+] = 0.04\text{ M}$.
(ii) $0.02\text{ M H}_2\text{SO}_4$: $[H^+] = 2 \times 0.02 = 0.04\text{ M}$.
Ratio $k'_I : k'_{II} = 0.04 : 0.04 = 1:1$.

**6.J7 → Answer: (C)**
$2A \rightarrow 3B + C$.
$P_t = (200 - 2x) + 3x + x = 200 + 2x = 280 \implies x = 40\text{ mmHg}$.
$P_A = 200 - 2(40) = 120\text{ mmHg}$.
$k = \frac{2.303}{20} \log\left(\frac{200}{120}\right) = \frac{2.303}{20} \log\left(\frac{5}{3}\right)$
$\log(5/3) = 0.699 - 0.477 = 0.222$
$k = \frac{2.303}{20} \times 0.222 = 0.0256\text{ min}^{-1}$.

**6.J8 → Answer: (B)**
$k' = k[B]_0$, $t_{1/2} = 0.693/k' = 0.693/(k[B]_0)$.
Doubling $[B]_0$ doubles $k'$, halving $t_{1/2}$.

**6.J9 → Answer: (A)**
After $n$ half-lives, fraction remaining $= (1/2)^n$.
After 3 half-lives: $(1/2)^3 = 1/8 = 12.5\%$.

**6.J10 → Answer: (B)**
$k' \propto [H^+]$.
$0.10\text{ M HCl}$: $[H^+] = 0.10\text{ M}$, $k' = 4.0 \times 10^{-3}\text{ min}^{-1}$.
$0.05\text{ M H}_2\text{SO}_4$: $[H^+] = 2 \times 0.05 = 0.10\text{ M}$.
$\therefore k' = 4.0 \times 10^{-3}\text{ min}^{-1}$.
</details>

---

## 🧠 Stage 7: Assertion-Reasoning

| # | Question | Difficulty |
|---|----------|------------|
| 6.S1 | **Assertion (A):** Hydrolysis of cane sugar is a pseudo first-order reaction.<br>**Reason (R):** Water is present in large excess during hydrolysis. | 🟢 |
| 6.S2 | **Assertion (A):** For $A(g) \rightarrow B(g) + C(g)$, the concentration of $A$ at time $t$ is $(2P_i - P_t)/RT$.<br>**Reason (R):** $P_A = 2P_i - P_t$. | 🟡 |
| 6.S3 | **Assertion (A):** The rate constant of a pseudo first-order reaction depends on acid catalyst concentration.<br>**Reason (R):** $k' = k[H^+]$. | 🟢 |
| 6.S4 | **Assertion (A):** Half-life of a pseudo first-order reaction depends on the initial concentration of the excess reactant.<br>**Reason (R):** $t_{1/2} = 0.693/(k[B]_0)$. | 🟡 |
| 6.S5 | **Assertion (A):** In ester hydrolysis, the volume of NaOH consumed ($V_t$) increases with time.<br>**Reason (R):** Acetic acid is produced, requiring more base. | 🟢 |
| 6.S6 | **Assertion (A):** In sucrose inversion, $r_t$ decreases continuously from $r_0$ to $r_\infty$.<br>**Reason (R):** Dextrorotatory sucrose converts to a laevorotatory mixture. | 🟡 |
| 6.S7 | **Assertion (A):** The pseudo rate constant $k'$ has units of $\text{time}^{-1}$.<br>**Reason (R):** $k' = k[\text{Water}]$, where $k$ is the true second-order constant. | 🟡 |
| 6.S8 | **Assertion (A):** The pseudo rate constant for ester hydrolysis in $0.1\text{ M HCl}$ equals that in $0.05\text{ M H}_2\text{SO}_4$.<br>**Reason (R):** Both solutions have the same $[H^+]$. | 🔴 |
| 6.S9 | **Assertion (A):** In the excess method, doubling the concentration of the excess reactant does not change the observed rate.<br>**Reason (R):** The rate is independent of the excess reactant concentration. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**6.S1 → Answer: (A)**
Both A and R are true, and R is the correct explanation. The vast excess of water means its concentration doesn't change meaningfully, dropping it from the effective rate equation.

**6.S2 → Answer: (A)**
Both A and R are true; R is the correct explanation. $P_A = 2P_i - P_t$, and concentration $= P_A/RT$.

**6.S3 → Answer: (A)**
Both A and R are true; R is the correct explanation. $k' = k[H^+]$, so $k'$ is directly proportional to $[H^+]$.

**6.S4 → Answer: (A)**
Both A and R are true; R is the correct explanation. $t_{1/2} = 0.693/k' = 0.693/(k[B]_0)$. Since $[B]_0$ appears in the denominator, $t_{1/2}$ depends on it.

**6.S5 → Answer: (A)**
Both A and R are true; R is the correct explanation. As the ester hydrolyzes, acetic acid accumulates, requiring more NaOH for neutralization.

**6.S6 → Answer: (A)**
Both A and R are true; R is the correct explanation. Sucrose ($+66^\circ$) produces glucose ($+52^\circ$) and fructose ($-92^\circ$). The mixture is laevorotatory due to fructose dominance.

**6.S7 → Answer: (A)**
Both A and R are true; R is the correct explanation. $k' = k[H_2O]$, and since $[H_2O]$ is constant ($\sim 55.5\text{ M}$), $k'$ has units of $\text{time}^{-1}$.

**6.S8 → Answer: (A)**
Both A and R are true; R is the correct explanation.
$0.1\text{ M HCl} \Rightarrow [H^+] = 0.1\text{ M}$.
$0.05\text{ M H}_2\text{SO}_4 \Rightarrow [H^+] = 2 \times 0.05 = 0.1\text{ M}$.
Same $[H^+]$, same $k'$.

**6.S9 → Answer: (D)**
A is false; R is true. Doubling $[B]_0$ doubles $k' = k[B]_0$, which changes the rate. The rate DOES depend on the excess reactant concentration through $k'$.
</details>

---

## 🏆 Stage 8: MCQ Mastery

*(Additional practice problems focusing on gas pressures and titrations...)*

**Q6.MC1 🟢**
Which of the following is NOT an example of a pseudo first-order reaction?
(A) Acid-catalyzed hydrolysis of ethyl acetate
(B) Inversion of cane sugar
(C) Decomposition of $N_2O_5$ in $CCl_4$
(D) Hydrolysis of methyl acetate in excess water

**Q6.MC2 🟡**
For $A(g) \rightarrow B(g) + C(g)$, after 2 half-lives the total pressure is 1.75 atm. The initial pressure of A was:
(A) $0.5\text{ atm}$
(B) $1.0\text{ atm}$
(C) $1.5\text{ atm}$
(D) $2.0\text{ atm}$

**Q6.MC3 🟡**
In the acid-catalyzed hydrolysis of an ester, which of the following remains constant during the reaction?
(A) Volume of NaOH used at time $t$
(B) Concentration of the ester
(C) Concentration of $H^+$ ions
(D) Total volume of the reaction mixture

**Q6.MC4 🟡**
For the inversion of sucrose, $r_0 = 45^\circ$, $r_\infty = -15^\circ$. After 10 min, if the reaction is 50% complete, $r_t$ is:
(A) $30^\circ$
(B) $15^\circ$
(C) $7.5^\circ$
(D) $22.5^\circ$

**Q6.MC5 🔴**
For a pseudo first-order reaction $A + B \rightarrow$ products with $[B]_0 = 50[A]_0$, the true rate law is $r = k[A][B]$. The observed half-life is 20 min. The true second-order rate constant $k$ is:
(A) $\frac{0.693}{20 \times 50[A]_0}$
(B) $\frac{0.693}{20}$
(C) $\frac{0.693}{20 \times [A]_0}$
(D) $\frac{0.693 \times 50[A]_0}{20}$

**Q6.MC6 🟢**
In the titration method for monitoring ester hydrolysis, $V_\infty$ is the volume of NaOH required when:
(A) All the ester has been consumed
(B) Half the ester has been consumed
(C) The reaction has just started
(D) The catalyst is neutralized

**Q6.MC7 🟡**
For $A(g) \rightarrow 2B(g) + C(g)$, initially only A is present. If total pressure becomes 1.5 times the initial pressure, the fraction of A decomposed is:
(A) $0.25$
(B) $0.50$
(C) $0.75$
(D) $1.00$

**Q6.MC8 🔴**
The rate constant for pseudo first-order hydrolysis of an ester is $0.0231\text{ min}^{-1}$. If initial ester concentration is 0.2 M and water concentration is 55.5 M, the true second-order rate constant (in L mol$^{-1}$ min$^{-1}$) is:
(A) $0.0231$
(B) $4.16 \times 10^{-4}$
(C) $1.28 \times 10^{-5}$
(D) $0.693$

**Q6.MC9 🔴 ⭐**
Two pseudo first-order reactions have half-lives $t_1$ and $t_2$. The excess reactant concentration for the first is 3 times that of the second, and true rate constants $k$ are equal. Then $t_1/t_2$ is:
(A) $1/3$
(B) $3$
(C) $1$
(D) $1/9$

<details>
<summary>💡 Detailed Solutions for Stage 8</summary>

**6.MC1 → Answer: (C)**
Decomposition of $N_2O_5$ is a true first-order reaction, not pseudo. The others use excess water to create pseudo first-order conditions.

**6.MC2 → Answer: (B)**
After 2 half-lives, $P_A = P_i/4$.
$P_A = P_i - x \implies P_i/4 = P_i - x \implies x = 3P_i/4$.
$P_t = P_i + x = P_i + 3P_i/4 = 7P_i/4 = 1.75 \implies P_i = 1.0\text{ atm}$.

**6.MC3 → Answer: (C)**
The $H^+$ catalyst is regenerated during the reaction, so its concentration remains constant.

**6.MC4 → Answer: (B)**
50% complete $\implies \frac{r_t - r_\infty}{r_0 - r_\infty} = \frac{1}{2}$.
$\frac{r_t + 15}{45 + 15} = \frac{r_t + 15}{60} = \frac{1}{2} \implies r_t = 15^\circ$.

**6.MC5 → Answer: (A)**
$k' = \frac{0.693}{t_{1/2}} = \frac{0.693}{20}$.
$k' = k[B]_0 = k(50[A]_0) \implies k = \frac{0.693}{20 \times 50[A]_0}$.

**6.MC6 → Answer: (A)**
$V_\infty$ is the NaOH volume at $t = \infty$ when all ester has been fully hydrolyzed to acetic acid.

**6.MC7 → Answer: (A)**
$A \rightarrow 2B + C$.
$P_t = (P_i - x) + 2x + x = P_i + 2x = 1.5P_i$.
$2x = 0.5P_i \implies x = 0.25P_i$.
Fraction decomposed $= x/P_i = 0.25$.

**6.MC8 → Answer: (B)**
$k' = k[H_2O] = 0.0231$.
$k = \frac{0.0231}{55.5} = 4.16 \times 10^{-4}\text{ L mol}^{-1}\text{ min}^{-1}$.

**6.MC9 → Answer: (A)**
$t_{1/2} = \frac{0.693}{k'} = \frac{0.693}{k[B]_0}$.
$\frac{t_1}{t_2} = \frac{[B]_{0,2}}{[B]_{0,1}} = \frac{1}{3}$.
</details>
