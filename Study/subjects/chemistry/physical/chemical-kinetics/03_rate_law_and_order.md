# Chapter 3: Rate Law, Rate Constant & Order
## Part II — Rate Law & Order

---

## 🎯 Stage 1: The Core Idea

### The "Black Box" of Kinetics

Look at the balanced equation: $2\text{NO} + \text{O}_2 \rightarrow 2\text{NO}_2$.
If you double the concentration of $\text{O}_2$, what happens to the rate of the reaction? Does it double? Quadruple? Stay the same?

**You cannot know just by looking at the equation.** 
The balanced equation is just a summary of what you start with and what you end with. It tells you nothing about the *actual steps* the molecules take (the mechanism). 

To find out how concentration actually affects the rate, scientists must run experiments. The mathematical result of these experiments is called the **Rate Law**.

### Order vs. Molecularity

| Feature | Order of Reaction | Molecularity |
|---------|-------------------|--------------|
| **Definition** | The sum of powers of concentration terms in the experimental rate law. | The number of reacting species colliding simultaneously in a single step (elementary reaction). |
| **Origin** | Strictly **experimental**. | **Theoretical** concept derived from mechanism. |
| **Values** | Can be 0, fraction, negative, or integer (usually 1, 2, 3). | Must be a whole number (1, 2, 3). Cannot be 0 or fractional. |
| **Applicability**| Applies to the overall reaction. | Applies only to a single, elementary step. |

> ⚠️ **Trap Alert:** For an *elementary* (single-step) reaction, Order = Molecularity. For a *complex* (multi-step) reaction, overall Molecularity has no meaning!

---

## 🔬 Stage 2: The Formula Lab

### Formula 1: The Rate Law

For a general reaction: $aA + bB \rightarrow \text{Products}$

The experimentally determined rate law is:
$$\text{Rate} = k[A]^x[B]^y$$

*   $k$ = Rate constant (specific reaction rate)
*   $x$ = Order with respect to A
*   $y$ = Order with respect to B
*   **Overall Order ($n$)** = $x + y$

*(Note: $x$ and $y$ may or may not be equal to the stoichiometric coefficients $a$ and $b$!)*

### Formula 2: Units of Rate Constant ($k$)

The unit of $k$ completely depends on the overall order ($n$) of the reaction.

$$\text{Rate} = k[\text{Concentration}]^n \implies \frac{\text{mol L}^{-1}}{\text{s}} = k (\text{mol L}^{-1})^n$$

Solving for $k$:
$$\text{Unit of } k = (\text{mol L}^{-1})^{1-n} \text{s}^{-1}$$

**Memorize these:**
*   **Zero Order ($n=0$):** $\text{mol L}^{-1} \text{s}^{-1}$ (Same as rate)
*   **First Order ($n=1$):** $\text{s}^{-1}$ (Time$^{-1}$ only)
*   **Second Order ($n=2$):** $\text{L mol}^{-1} \text{s}^{-1}$

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Deducing Order from the Units of $k$

**The Pattern:** You are given the value and unit of a rate constant. You must state the order. The value is a distraction; only look at the units.

#### Solved Example 3.1
**Q:** Identify the reaction order if $k = 2.3 \times 10^{-5} \text{ L mol}^{-1} \text{ s}^{-1}$. 🟢

**Solution:**
```
1. Write the general unit formula: (mol L^-1)^(1-n) s^-1
2. Look at the given unit: L mol^-1 s^-1. This can be rewritten as (mol L^-1)^-1 s^-1.
3. Compare the powers of (mol L^-1):
   1 - n = -1
   n = 2

Answer: Second order reaction.
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 3.1a | Identify the order if $k = 3 \times 10^{-4} \text{ s}^{-1}$. | 🟢 |
| 3.1b | Identify the order if $k = 1.5 \times 10^{-2} \text{ mol L}^{-1} \text{ s}^{-1}$. | 🟢 |
| 3.1c | What is the unit of $k$ for a $\frac{3}{2}$ order reaction? | 🟡 |
| 3.1d | If $k = 4.2 \times 10^{-3} \text{ L}^2 \text{ mol}^{-2} \text{ s}^{-1}$, determine the overall order. | 🟢 |
| 3.1e | A reaction has $k = 2.5 \times 10^{-4} \text{ mol}^{-1/2} \text{ L}^{1/2} \text{ s}^{-1}$. Find the order. | 🟡 |
| 3.1f | What is the unit of $k$ for a reaction of overall order $2.5$? | 🟡 |
| 3.1g | The rate constant is $3.6 \times 10^{-2} \text{ L mol}^{-1} \text{ min}^{-1}$. Identify the order. | 🟡 |
| 3.1h | If $k = 8.0 \times 10^{-3} \text{ mol}^2 \text{ L}^{-2} \text{ s}^{-1}$, determine the order. | 🔴 |
| 3.1i | For a gas-phase reaction, $k$ has the unit $\text{atm}^{-2} \text{ s}^{-1}$. What is the order? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**3.1a:**
- Unit is $\text{s}^{-1}$.
- $1 - n = 0 \implies n = 1$. **First order.**

**3.1b:**
- Unit is $\text{mol L}^{-1} \text{s}^{-1}$.
- $1 - n = 1 \implies n = 0$. **Zero order.**

**3.1c:**
- $n = 3/2$.
- Power $= 1 - 3/2 = -1/2$.
- Unit $= (\text{mol L}^{-1})^{-1/2} \text{ s}^{-1} = \text{mol}^{-1/2} \text{ L}^{1/2} \text{ s}^{-1}$.

**3.1d:**
- Unit is $\text{L}^2 \text{mol}^{-2} \text{s}^{-1} = (\text{mol L}^{-1})^{-2} \text{s}^{-1}$.
- $1 - n = -2 \implies n = 3$. **Third order.**

**3.1e:**
- Unit is $\text{mol}^{-1/2} \text{L}^{1/2} \text{s}^{-1} = (\text{mol L}^{-1})^{-1/2} \text{s}^{-1}$.
- $1 - n = -1/2 \implies n = 3/2$. **1.5 order.**

**3.1f:**
- $n = 2.5$.
- Power $= 1 - 2.5 = -1.5$.
- Unit $= (\text{mol L}^{-1})^{-1.5} \text{ s}^{-1} = \text{mol}^{-3/2} \text{ L}^{3/2} \text{ s}^{-1}$.

**3.1g:**
- Unit is $\text{L mol}^{-1} \text{min}^{-1} = (\text{mol L}^{-1})^{-1} \text{min}^{-1}$.
- $1 - n = -1 \implies n = 2$. **Second order.** (Time units don't affect order.)

**3.1h:**
- Unit is $\text{mol}^2 \text{L}^{-2} \text{s}^{-1} = (\text{mol L}^{-1})^{2} \text{s}^{-1}$.
- $1 - n = 2 \implies n = -1$. **Negative first order** (rare, but mathematically valid from units).

**3.1i:**
- When pressure (atm) is used instead of concentration: $k = (\text{atm})^{1-n} \text{s}^{-1}$.
- Given unit $\text{atm}^{-2} \text{s}^{-1} \implies 1 - n = -2 \implies n = 3$. **Third order.**
</details>

---

### Type 2: Deriving Rate Law from a Mechanism

**The Pattern:** You are given a multi-step mechanism. Identify the slow step to write the rate law. If the slow step contains an intermediate, use the fast equilibrium step to substitute it out.

#### Solved Example 3.2
**Q:** The mechanism for $2\text{NO}_2 + \text{F}_2 \rightarrow 2\text{NO}_2\text{F}$ is:
Step 1: $\text{NO}_2 + \text{F}_2 \rightarrow \text{NO}_2\text{F} + \text{F}^\bullet$ (Slow)
Step 2: $\text{NO}_2 + \text{F}^\bullet \rightarrow \text{NO}_2\text{F}$ (Fast)
Write the rate law. 🟡

**Solution:**
```
1. The slowest step is the rate-determining step (RDS).
2. Write the rate law using ONLY the reactants of the slow step.
   Rate = k [NO2]^1 [F2]^1
3. Check for intermediates. NO2 and F2 are both reactants in the overall equation, so this is the final answer.

Answer: Rate = k [NO2][F2]
```

#### Solved Example 3.3
**Q:** The mechanism for $2\text{O}_3 \rightarrow 3\text{O}_2$ is:
Step 1: $\text{O}_3 \rightleftharpoons \text{O}_2 + \text{O}$ (Fast equilibrium, constant $K_{eq}$)
Step 2: $\text{O} + \text{O}_3 \rightarrow 2\text{O}_2$ (Slow, rate constant $k_2$)
Find the rate law and overall order. 🔴 ⭐

**Solution:**
```
1. Write rate based on slow step: Rate = k_2 [O][O3]
2. 'O' is an intermediate (not in the overall reaction). It must be eliminated.
3. Use the fast equilibrium step:
   K_eq = ([O2][O]) / [O3]
   Solve for [O]: [O] = K_eq [O3] / [O2]
4. Substitute [O] back into the rate law:
   Rate = k_2 (K_eq [O3] / [O2]) [O3]
   Rate = (k_2 * K_eq) [O3]^2 [O2]^-1
   Rate = k_net [O3]^2 [O2]^-1
   
Answer: Order = 2 + (-1) = 1.
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 3.2a | Mechanism: (1) $A + B \rightarrow C$ (slow); (2) $A + C \rightarrow D$ (fast). Find rate law. | 🟢 |
| 3.2b | Mechanism: (1) $NO + NO \rightleftharpoons N_2O_2$ (fast); (2) $N_2O_2 + O_2 \rightarrow 2NO_2$ (slow). Write the rate law. | 🔴 |
| 3.2c | $A + 2B \rightarrow$ Products. Step 1: $A + B \rightarrow X$ (slow). Step 2: $B + X \rightarrow$ Products (fast). Write the rate law. | 🟢 |
| 3.2d | $2NO + Cl_2 \rightarrow 2NOCl$. Step 1: $NO + Cl_2 \rightleftharpoons NOCl_2$ (fast eq). Step 2: $NOCl_2 + NO \rightarrow 2NOCl$ (slow). Derive the rate law. | 🟡 |
| 3.2e | $H_2 + Br_2 \rightarrow 2HBr$. Step 1: $Br_2 \rightleftharpoons 2Br$ (fast eq). Step 2: $Br + H_2 \rightarrow HBr + H$ (slow). Step 3: $H + Br_2 \rightarrow HBr + Br$ (fast). Find the rate law in terms of $[H_2]$ and $[Br_2]$. | 🟡 |
| 3.2f | $2NO + 2H_2 \rightarrow N_2 + 2H_2O$. Step 1: $2NO \rightleftharpoons N_2O_2$ (fast eq). Step 2: $N_2O_2 + H_2 \rightarrow N_2O + H_2O$ (slow). Step 3: $N_2O + H_2 \rightarrow N_2 + H_2O$ (fast). Write the rate law. | 🟡 |
| 3.2g | $2A + B_2 \rightarrow 2AB$. Step 1: $B_2 \rightleftharpoons 2B$ (fast eq, $K_1$). Step 2: $A + B \rightleftharpoons AB^*$ (fast eq, $K_2$). Step 3: $AB^* + A \rightarrow 2AB$ (slow, $k_3$). Find the rate law and overall order. | 🔴 |
| 3.2h | For $2A + B \rightarrow C$, the observed rate law is Rate = $k[A][B]$. Proposed mechanism: Step 1: $A + B \rightleftharpoons D$ (fast eq). Step 2: $D + A \rightarrow C$ (slow). Is this mechanism consistent? If not, what rate law does it predict? | 🔴 |
| 3.2i | $2O_3 \rightarrow 3O_2$. Step 1: $O_3 \rightleftharpoons O_2 + O$ (fast eq). Step 2: $O + O_3 \rightarrow 2O_2$ (slow). If $[O_3]$ is tripled while $[O_2]$ is constant, by what factor does the rate increase? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**3.2a:**
- Slow step gives: Rate = $k[A][B]$. C is an intermediate but it's not in the rate law. Done.

**3.2b:**
- Slow step rate = $k_2[N_2O_2][O_2]$.
- $N_2O_2$ is an intermediate. From equilibrium: $K_{eq} = \frac{[N_2O_2]}{[NO]^2} \implies [N_2O_2] = K_{eq}[NO]^2$.
- Substitute: Rate = $k_2 K_{eq} [NO]^2 [O_2] = k_{net} [NO]^2 [O_2]$.

**3.2c:**
- Slow step: Rate = $k[A][B]$. Intermediate $X$ does not appear in this rate law.
- **Rate = $k[A][B]$.**

**3.2d:**
- Slow step: Rate = $k_2[NOCl_2][NO]$.
- Intermediate $NOCl_2$ from equilibrium: $K_{eq} = \frac{[NOCl_2]}{[NO][Cl_2]} \implies [NOCl_2] = K_{eq}[NO][Cl_2]$.
- Substitute: Rate = $k_2 K_{eq} [NO]^2 [Cl_2] = k_{net}[NO]^2[Cl_2]$.

**3.2e:**
- Rate determined by slow step 2: Rate = $k_2[Br][H_2]$.
- $Br$ is an intermediate. From step 1 equilibrium: $K_1 = \frac{[Br]^2}{[Br_2]} \implies [Br] = \sqrt{K_1[Br_2]}$.
- Substitute: Rate = $k_2 \sqrt{K_1[Br_2]} [H_2] = k_{net}[H_2][Br_2]^{1/2}$.
- **Rate = $k[H_2][Br_2]^{1/2}$** (fractional order from mechanism).

**3.2f:**
- Slow step: Rate = $k_2[N_2O_2][H_2]$.
- $N_2O_2$ intermediate from equilibrium: $K_{eq} = \frac{[N_2O_2]}{[NO]^2} \implies [N_2O_2] = K_{eq}[NO]^2$.
- Substitute: Rate = $k_2 K_{eq} [NO]^2 [H_2] = k_{net}[NO]^2[H_2]$.
- **Rate = $k[NO]^2[H_2]$.**

**3.2g:**
- Slow step: Rate = $k_3[AB^*][A]$.
- $AB^*$ from step 2: $K_2 = \frac{[AB^*]}{[A][B]} \implies [AB^*] = K_2[A][B]$.
- $B$ from step 1: $K_1 = \frac{[B]^2}{[B_2]} \implies [B] = \sqrt{K_1[B_2]}$.
- $[AB^*] = K_2[A]\sqrt{K_1[B_2]}$.
- Rate = $k_3 K_2 \sqrt{K_1} [A]^2 [B_2]^{1/2} = k_{net}[A]^2[B_2]^{1/2}$.
- **Overall order = $2 + 0.5 = 2.5$.**

**3.2h:**
- Mechanism predicts: Rate = $k_2[D][A]$. From eq: $K_{eq} = \frac{[D]}{[A][B]} \implies [D] = K_{eq}[A][B]$.
- Predicted Rate = $k_2 K_{eq} [A]^2[B]$.
- Experimental Rate = $k[A][B]$.
- **Not consistent.** The mechanism gives order 2 in $A$; experiment shows order 1 in $A$.

**3.2i:**
- Rate = $k_2[O][O_3]$. From eq: $K_{eq} = \frac{[O_2][O]}{[O_3]} \implies [O] = K_{eq}\frac{[O_3]}{[O_2]}$.
- Rate = $k_2 K_{eq} \frac{[O_3]^2}{[O_2]} = k[O_3]^2[O_2]^{-1}$.
- Tripling $[O_3]$ at constant $[O_2]$: Rate factor = $3^2 = 9$.
- **Rate increases 9 times.**
</details>
</details>

---

### Type 3: The Initial Rate Method (Table Method)

**The Pattern:** You are given a data table. Find experiments where one reactant changes while the other is kept constant. Observe how the rate responds.

#### Solved Example 3.4
**Q:** For $A + B \rightarrow C$, the data is:
| Exp | [A] | [B] | Initial Rate |
|---|---|---|---|
| 1 | 0.1 | 0.1 | $2 \times 10^{-3}$ |
| 2 | 0.1 | 0.2 | $4 \times 10^{-3}$ |
| 3 | 0.2 | 0.1 | $8 \times 10^{-3}$ |
Find the rate law. 🟡 ⭐

**Solution:**
```
Assume Rate = k[A]^x[B]^y
1. Find 'y' (Keep [A] constant):
   Compare Exp 1 and 2. [A] is constant (0.1).
   [B] doubles (0.1 -> 0.2).
   Rate doubles (2x10^-3 -> 4x10^-3).
   2^y = 2  => y = 1.

2. Find 'x' (Keep [B] constant):
   Compare Exp 1 and 3. [B] is constant (0.1).
   [A] doubles (0.1 -> 0.2).
   Rate quadruples (2x10^-3 -> 8x10^-3).
   2^x = 4  => x = 2.

Answer: Rate = k[A]^2[B]^1
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 3.3a | Exp 1: [A]=0.1, Rate=0.05. Exp 2: [A]=0.2, Rate=0.05. What is the order? | 🟢 |
| 3.3b | [A] doubles, rate increases 8 times. What is the order w.r.t A? | 🟢 |
| 3.3c | | | |
| | Exp | [A] | [B] | Rate (M/s) | | |
| | 1 | 0.1 | 0.1 | $1.0\times10^{-3}$ | | |
| | 2 | 0.2 | 0.1 | $1.0\times10^{-3}$ | | |
| | 3 | 0.1 | 0.2 | $2.0\times10^{-3}$ | | |
| | Find the order with respect to A and B. | | 🟢 |
| 3.3d | | | |
| | Exp | [A] | [B] | Rate (M/s) | | |
| | 1 | 0.1 | 0.1 | $5.0\times10^{-3}$ | | |
| | 2 | 0.1 | 0.3 | $1.5\times10^{-2}$ | | |
| | 3 | 0.2 | 0.1 | $2.0\times10^{-2}$ | | |
| | Determine the rate law. | | 🟡 |
| 3.3e | | | |
| | Exp | [P] | [Q] | Rate (M/s) | | |
| | 1 | 0.1 | 0.1 | $3.0\times10^{-4}$ | | |
| | 2 | 0.2 | 0.1 | $1.2\times10^{-3}$ | | |
| | 3 | 0.2 | 0.2 | $4.8\times10^{-3}$ | | |
| | Find the order w.r.t P and Q and the overall order. | | 🟡 |
| 3.3f | | | |
| | Exp | [A] | [B] | Rate (M/s) | | |
| | 1 | 1.0 | 2.0 | 0.80 | | |
| | 2 | 2.0 | 2.0 | 0.80 | | |
| | 3 | 1.0 | 4.0 | 3.20 | | |
| | Find the rate law and calculate $k$ with units. | | 🟡 |
| 3.3g | | | |
| | Exp | [A] | [B] | [C] | Rate (M/s) | |
| | 1 | 0.1 | 0.1 | 0.1 | $4.0\times10^{-4}$ | |
| | 2 | 0.2 | 0.1 | 0.1 | $1.6\times10^{-3}$ | |
| | 3 | 0.1 | 0.3 | 0.1 | $4.0\times10^{-4}$ | |
| | 4 | 0.1 | 0.1 | 0.2 | $8.0\times10^{-4}$ | |
| | Find the rate law and overall order. | | 🔴 |
| 3.3h | | | |
| | Exp | [A] | [B] | Rate (M/min) | | |
| | 1 | 0.1 | 0.1 | $1.0\times10^{-2}$ | | |
| | 2 | 0.1 | 0.2 | $4.0\times10^{-2}$ | | |
| | 3 | 0.2 | 0.1 | $2.0\times10^{-2}$ | | |
| | 4 | 0.2 | 0.4 | ? | | |
| | Determine the rate law and predict the rate for experiment 4. | | 🔴 |
| 3.3i | | | |
| | Exp | [A] | [B] | Rate (M/s) | | |
| | 1 | 0.1 | 0.1 | $2.0\times10^{-3}$ | | |
| | 2 | 0.3 | 0.1 | $6.0\times10^{-3}$ | | |
| | 3 | 0.1 | 0.3 | $6.0\times10^{-3}$ | | |
| | 4 | 0.3 | 0.3 | ? | | |
| | Determine orders and predict the rate for experiment 4. | | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**3.3a:**
- [A] doubles, but rate remains unchanged (0.05).
- $2^x = 1 \implies x = 0$. Zero order.

**3.3b:**
- $2^x = 8 \implies 2^x = 2^3 \implies x = 3$. Third order.

**3.3c:**
- Compare Exp 1 & 2: [B] is constant (0.1). [A] doubles (0.1$\to$0.2), rate unchanged ($1.0\times10^{-3}$). $2^x = 1 \implies x = 0$.
- Compare Exp 1 & 3: [A] is constant (0.1). [B] doubles (0.1$\to$0.2), rate doubles ($1.0\to2.0\times10^{-3}$). $2^y = 2 \implies y = 1$.
- **Order w.r.t A = 0, w.r.t B = 1.** Rate = $k[B]$.

**3.3d:**
- Compare Exp 1 & 2: [A] constant (0.1). [B] ×3 (0.1$\to$0.3), rate ×3. $3^y = 3 \implies y = 1$.
- Compare Exp 1 & 3: [B] constant (0.1). [A] ×2 (0.1$\to$0.2), rate ×4. $2^x = 4 \implies x = 2$.
- **Rate = $k[A]^2[B]$.**

**3.3e:**
- Compare Exp 1 & 2: [Q] constant (0.1). [P] ×2, rate ×4. $2^x = 4 \implies x = 2$.
- Compare Exp 2 & 3: [P] constant (0.2). [Q] ×2, rate ×4. $2^y = 4 \implies y = 2$.
- **Order w.r.t P = 2, w.r.t Q = 2. Overall order = 4.**

**3.3f:**
- Compare Exp 1 & 2: [B] constant (2.0). [A] ×2, rate same. $2^x = 1 \implies x = 0$.
- Compare Exp 1 & 3: [A] constant (1.0). [B] ×2, rate ×4. $2^y = 4 \implies y = 2$.
- Rate = $k[B]^2$. $k = \frac{0.80}{(2.0)^2} = \frac{0.80}{4} = 0.20\ \text{M}^{-1}\text{s}^{-1}$.

**3.3g:**
- Compare 1 & 2: [B][C] constant. [A] ×2, rate ×4 $\implies$ order w.r.t A = 2.
- Compare 1 & 3: [A][C] constant. [B] ×3, rate same $\implies$ order w.r.t B = 0.
- Compare 1 & 4: [A][B] constant. [C] ×2, rate ×2 $\implies$ order w.r.t C = 1.
- **Rate = $k[A]^2[C]$. Overall order = 3.**

**3.3h:**
- Compare 1 & 2: [A] constant. [B] ×2, rate ×4 $\implies y = 2$.
- Compare 1 & 3: [B] constant. [A] ×2, rate ×2 $\implies x = 1$.
- Rate = $k[A][B]^2$. From exp 1: $k = \frac{1.0\times10^{-2}}{0.1 \times (0.1)^2} = 10\ \text{M}^{-2}\text{min}^{-1}$.
- Exp 4: Rate = $10 \times 0.2 \times (0.4)^2 = 10 \times 0.2 \times 0.16 = 0.32\ \text{M/min}$.

**3.3i:**
- Compare 1 & 2: [B] constant. [A] ×3, rate ×3 $\implies x = 1$.
- Compare 1 & 3: [A] constant. [B] ×3, rate ×3 $\implies y = 1$.
- Rate = $k[A][B]$. $k = \frac{2.0\times10^{-3}}{0.1 \times 0.1} = 0.2\ \text{M}^{-1}\text{s}^{-1}$.
- Exp 4: Rate = $0.2 \times 0.3 \times 0.3 = 1.8 \times 10^{-2}\ \text{M/s}$.
</details>
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 3.M1 | For a reaction $A + B \rightarrow P$, rate = $k[A]^2[B]$. If the volume of the reaction vessel is suddenly halved, how many times will the rate increase? | Rate law + Volume logic | 🔴 |
| 3.M2 | The unit of rate constant for a reaction is $\text{L mol}^{-1} \text{s}^{-1}$. If the rate law is Rate = $k[A]^x[B]^y$ and doubling $[B]$ does not change the rate, what is $x + y$? | Units + Order logic | 🟢 |
| 3.M3 | For $2A + 2B \rightarrow C + D$, the data is: Exp 1: [A]=0.1, [B]=0.1, Rate=$2.0\times10^{-3}$; Exp 2: [A]=0.2, [B]=0.1, Rate=$8.0\times10^{-3}$; Exp 3: [A]=0.1, [B]=0.2, Rate=$2.0\times10^{-3}$. The rate constant has unit $\text{L mol}^{-1} \text{s}^{-1}$. Is the data consistent with this unit? Find the rate law and verify. | Table + Unit check | 🟡 |
| 3.M4 | For a reaction, Rate = $k[A]^{1/2}[B]^2$. What is the unit of $k$? If the volume is reduced to $\frac14$ of its original, by what factor does the rate change? | Units + Volume logic | 🟡 |
| 3.M5 | For $A + B \rightarrow$ Products: Exp 1: [A]=0.1, [B]=0.2, Rate=$4.0\times10^{-3}$; Exp 2: [A]=0.2, [B]=0.2, Rate=$8.0\times10^{-3}$; Exp 3: [A]=0.2, [B]=0.4, Rate=$3.2\times10^{-2}$. A student claims order w.r.t A is 1 and w.r.t B is 2. Using unit analysis of $k$, verify this claim. | Table + Unit verification | 🟡 |
| 3.M6 | For the hypothetical reaction $A + B \rightarrow C$, the proposed mechanism is Step 1: $A + B \rightarrow X$ (slow). But experimentally, Rate = $k[A]^2[B]$. Does this mean the mechanism is wrong? Explain. | Mechanism vs Experiment | 🔴 |
| 3.M7 | A reaction has Rate = $k[A][B]^2$. Initial rates: Cond 1: [A]=0.2 M, [B]=0.2 M, Rate=$1.6\times10^{-2}$ M/s. Cond 2: [A]=0.1 M, [B]=0.4 M, Rate$_2 = ?$. Predict Rate$_2$. | Rate law + Prediction | 🔴 |
| 3.M8 | $2A + B \rightarrow 2C$. Step 1: $A + B \rightleftharpoons D$ (fast eq, $K_c = 10\ \text{L/mol}$). Step 2: $D + A \rightarrow 2C$ (slow, $k_2 = 5\ \text{s}^{-1}$). If $[A]=0.2$ M and $[B]=0.1$ M initially, find the initial rate. | Mechanism + Calculation | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**3.M1:**
- Halving the volume doubles the concentration of EVERY gas.
- New $[A] = 2[A]$, New $[B] = 2[B]$.
- New Rate = $k (2[A])^2 (2[B]) = k \cdot 4[A]^2 \cdot 2[B] = 8 \cdot k[A]^2[B]$.
- The rate increases 8 times.

**3.M2:**
- Unit $\text{L mol}^{-1} \text{s}^{-1} = (\text{mol L}^{-1})^{-1} \text{s}^{-1} \implies 1-n = -1 \implies n = 2$.
- Doubling $[B]$ doesn't change rate $\implies y = 0$.
- Since overall $n = x + y = 2$ and $y = 0 \implies x = 2$.
- **$x + y = 2$.**

**3.M3:**
- Compare 1 & 2: [B] constant, [A]×2, rate×4 $\implies$ order w.r.t A = 2.
- Compare 1 & 3: [A] constant, [B]×2, rate same $\implies$ order w.r.t B = 0.
- Rate = $k[A]^2$. Overall $n = 2$. Unit should be $\text{L mol}^{-1} \text{s}^{-1}$. ✓.
- $k = \frac{2.0\times10^{-3}}{(0.1)^2} = 0.2\ \text{L mol}^{-1} \text{s}^{-1}$. **Consistent.**

**3.M4:**
- Overall $n = 0.5 + 2 = 2.5$. Unit of $k = (\text{mol L}^{-1})^{1-2.5} \text{s}^{-1} = (\text{mol L}^{-1})^{-1.5} \text{s}^{-1}$.
- **Unit:** $\text{mol}^{-3/2} \text{L}^{3/2} \text{s}^{-1}$.
- Volume $\to \frac14$ means all concentrations $\times 4$.
- Rate factor = $(4)^{1/2} \times (4)^2 = 2 \times 16 = 32$.
- **Rate increases 32 times.**

**3.M5:**
- Compare 1 & 2: [B] constant, [A]×2, rate×2 $\implies x = 1$. ✓ Claim.
- Compare 2 & 3: [A] constant, [B]×2, rate×4 $\implies y = 2$. ✓ Claim.
- Overall $n = 3$. Rate = $k[A][B]^2$.
- $k = \frac{4.0\times10^{-3}}{0.1 \times (0.2)^2} = \frac{4.0\times10^{-3}}{0.004} = 1\ \text{L}^2 \text{mol}^{-2} \text{s}^{-1}$.
- Unit $\text{L}^2 \text{mol}^{-2} \text{s}^{-1}$ matches $n = 3$. **Claim verified.**

**3.M6:**
- If Step 1 is slow and elementary: Rate = $k[A][B]$.
- But experimental rate is $k[A]^2[B]$. The two do not match.
- **Yes, the mechanism is wrong.** The actual mechanism must be different (e.g., a pre-equilibrium involving A).

**3.M7:**
- Cond 2 relative to Cond 1: $[A]$ halved ($\times \frac12$), $[B]$ doubled ($\times 2$).
- Rate factor = $(\frac12)^1 \times (2)^2 = \frac12 \times 4 = 2$.
- **Rate$_2 = 2 \times 1.6\times10^{-2} = 3.2\times10^{-2}$ M/s.**

**3.M8:**
- Slow step: Rate = $k_2[D][A]$.
- From equilibrium: $K_c = \frac{[D]}{[A][B]} \implies [D] = K_c[A][B] = 10 \times 0.2 \times 0.1 = 0.2$ M.
- Initial Rate = $5 \times 0.2 \times 0.2 = 0.2$ M/s.
- **Initial rate = $0.2$ M/s.**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 3.B1 | Define order of a reaction. Can it be a fraction? | 🟢 |
| 3.B2 | Distinguish between order and molecularity (write 2 points). | 🟢 |
| 3.B3 | A reaction is second order with respect to a reactant. How is the rate affected if the concentration of the reactant is (i) doubled, (ii) reduced to half? | 🟡 |
| 3.B4 | Define rate law. How is it different from the law of mass action? | 🟢 |
| 3.B5 | What is the order of a reaction if the unit of rate constant is $\text{s}^{-1}$? What does this imply about the rate's dependence on concentration? | 🟢 |
| 3.B6 | For an elementary reaction $2A + B \rightarrow C$, write the rate law. What are the orders with respect to A, B, and overall? | 🟡 |
| 3.B7 | Can a reaction have the same order with respect to a reactant as its stoichiometric coefficient? Give an example where they differ. | 🟡 |
| 3.B8 | For $A + B \rightarrow P$, the data is: [A]=0.1, [B]=0.1, Rate=$2.5\times10^{-3}$; [A]=0.2, [B]=0.1, Rate=$5.0\times10^{-3}$; [A]=0.1, [B]=0.2, Rate=$1.0\times10^{-2}$. Write the rate law and overall order. | 🟡 |
| 3.B9 | Explain with an example how the molecularity of an elementary step differs from the overall order of a complex reaction. | 🔴 |
| 3.B10 | The unit of $k$ is $\text{L}^{3/2} \text{mol}^{-3/2} \text{min}^{-1}$. What is the overall order? If the rate quadruples when $[A]$ doubles, what is the order w.r.t A? What can you conclude about other reactants? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**3.B1:** Order is the sum of the powers to which concentration terms are raised in the experimentally determined rate law. Yes, it can be a fraction (e.g., $1.5$).
**3.B2:** Order is experimental and can be 0 or fractional. Molecularity is theoretical (number of colliding particles) and must be an integer (1, 2, 3).
**3.B3:** Rate = $k[A]^2$. (i) Doubled: Rate becomes $(2)^2 = 4$ times. (ii) Halved: Rate becomes $(1/2)^2 = 1/4$th.
**3.B4:** Rate law is the experimental expression relating rate to concentrations. Law of mass action applies only to elementary steps and uses stoichiometric coefficients as powers. Rate law powers are experimentally determined and may differ.
**3.B5:** Unit $\text{s}^{-1}$ means $1-n = 0 \implies n = 1$ (first order). The rate depends linearly on concentration: doubling $[A]$ doubles the rate.
**3.B6:** For an elementary reaction, Rate = $k[A]^2[B]^1$. Order w.r.t A = 2, w.r.t B = 1. **Overall order = 3.**
**3.B7:** Yes, for elementary reactions they are equal. They differ in complex reactions — e.g., $2N_2O_5 \rightarrow 4NO_2 + O_2$ has stoichiometric coefficient 2 for $N_2O_5$, but experimental order is 1.
**3.B8:** Compare 1 & 2: [B] constant, [A]×2, rate×2 $\implies x=1$. Compare 1 & 3: [A] constant, [B]×2, rate×4 $\implies y=2$. Rate = $k[A][B]^2$. **Overall order = 3.**
**3.B9:** Example: $2O_3 \rightarrow 3O_2$ mechanism has elementary steps with molecularities 2 and 2. But overall order derived from the rate law is 1 (Rate = $k[O_3]^2[O_2]^{-1}$). Molecularity applies to individual steps; order applies to the net reaction.
**3.B10:** Unit $\text{L}^{3/2} \text{mol}^{-3/2} \text{min}^{-1} = (\text{mol L}^{-1})^{-3/2} \text{min}^{-1}$. $1-n = -\frac32 \implies n = \frac52 = 2.5$. Rate quadruples when $[A]$ doubles $\implies 2^x = 4 \implies x = 2$ w.r.t A. Since overall $n = 2.5$, the sum of orders of other reactants = $0.5$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q3.J1 🟡**
For a chemical reaction $X \rightarrow Y$, it is found that the rate of reaction increases 2.25 times when the concentration of X is increased 1.5 times. What is the order of the reaction?
<br>
(A) 1 <br>
(B) 1.5 <br>
(C) 2 <br>
(D) 2.5

**Q3.J2 🔴**
The rate law for the reaction $RCl + NaOH \rightarrow ROH + NaCl$ is Rate = $k[RCl]$. The rate of reaction will be:
<br>
(A) Doubled on doubling the concentration of NaOH. <br>
(B) Halved on reducing the concentration of RCl to one half. <br>
(C) Decreased on increasing the temperature. <br>
(D) Unaffected by increasing temperature.

**Q3.J3 🟢**
The rate constant for a reaction is $2.0 \times 10^{-3}\ \text{L mol}^{-1} \text{s}^{-1}$. The order of the reaction is:
<br>
(A) 0 <br>
(B) 1 <br>
(C) 2 <br>
(D) 3

**Q3.J4 🟡**
For a reaction, Rate = $k[A]^{1/2}[B]^{3/2}$. The overall order is:
<br>
(A) 1 <br>
(B) 1.5 <br>
(C) 2 <br>
(D) 2.5

**Q3.J5 🟡**
For $2NO_2 + F_2 \rightarrow 2NO_2F$, the mechanism is: $NO_2 + F_2 \rightarrow NO_2F + F$ (slow), $NO_2 + F \rightarrow NO_2F$ (fast). The rate law is:
<br>
(A) $k[NO_2][F_2]$ <br>
(B) $k[NO_2]^2[F_2]$ <br>
(C) $k[NO_2][F]$ <br>
(D) $k[NO_2]^2$

**Q3.J6 🟡**
For $A \rightarrow$ Products, the rate quadruples when $[A]$ is doubled and becomes 9 times when $[A]$ is tripled. The order is:
<br>
(A) 1 <br>
(B) 1.5 <br>
(C) 2 <br>
(D) 3

**Q3.J7 🟡**
Rate = $k[A]^2[B]$. If $[A]$ is doubled and $[B]$ is halved, the rate will:
<br>
(A) Remain same <br>
(B) Double <br>
(C) Quadruple <br>
(D) Become 8 times

**Q3.J8 🔴**
For a reaction, Rate = $k[A]^0[B]^{3/2}$. The unit of $k$ is:
<br>
(A) $\text{L}^{1/2} \text{mol}^{-1/2} \text{s}^{-1}$ <br>
(B) $\text{L}^{-1/2} \text{mol}^{1/2} \text{s}^{-1}$ <br>
(C) $\text{L}^{3/2} \text{mol}^{-3/2} \text{s}^{-1}$ <br>
(D) $\text{L mol}^{-1} \text{s}^{-1}$

**Q3.J9 🔴**
A + B $\rightleftharpoons$ C (fast), C + A $\rightarrow$ D (slow). If $[A]$ is doubled and $[B]$ is tripled, the rate increases by:
<br>
(A) 8 <br>
(B) 12 <br>
(C) 6 <br>
(D) 9

**Q3.J10 🔴**
For $A + B \rightarrow C$: [A]=0.1, [B]=0.1, Rate=$1.0\times10^{-3}$; [A]=0.1, [B]=0.2, Rate=$4.0\times10^{-3}$; [A]=0.2, [B]=0.1, Rate=$2.0\times10^{-3}$. The rate constant $k$ is:
<br>
(A) $0.1\ \text{L mol}^{-1} \text{s}^{-1}$ <br>
(B) $0.5\ \text{L mol}^{-1} \text{s}^{-1}$ <br>
(C) $1.0\ \text{L}^2 \text{mol}^{-2} \text{s}^{-1}$ <br>
(D) $2.0\ \text{L}^2 \text{mol}^{-2} \text{s}^{-1}$

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**3.J1 → Answer: (C)**
- Let order be $n$.
- $(1.5)^n = 2.25$
- $(1.5)^n = (1.5)^2 \implies n=2$.

**3.J2 → Answer: (B)**
- The rate law shows it is zero order with respect to NaOH (it doesn't appear in the equation). So changing NaOH does nothing.
- It is first order w.r.t RCl. If RCl is halved, rate is halved.

**3.J3 → Answer: (C)**
- Unit $\text{L mol}^{-1} \text{s}^{-1} = (\text{mol L}^{-1})^{-1} \text{s}^{-1}$.
- $1-n = -1 \implies n = 2$. Second order.

**3.J4 → Answer: (C)**
- Overall order = $\frac12 + \frac32 = 2$.

**3.J5 → Answer: (A)**
- Slow step is RDS: Rate = $k[NO_2][F_2]$.
- Neither species is an intermediate. Direct match.

**3.J6 → Answer: (C)**
- $2^n = 4 \implies n = 2$. Also $3^n = 9 \implies n = 2$. Consistent.
- Second order.

**3.J7 → Answer: (B)**
- New Rate = $k(2[A])^2(\frac12[B]) = k \cdot 4[A]^2 \cdot \frac12[B] = 2 \cdot k[A]^2[B]$.
- Rate doubles.

**3.J8 → Answer: (A)**
- Overall $n = 0 + 1.5 = 1.5$.
- $1-n = -0.5$. Unit = $(\text{mol L}^{-1})^{-0.5} \text{s}^{-1} = \text{L}^{1/2} \text{mol}^{-1/2} \text{s}^{-1}$.

**3.J9 → Answer: (B)**
- Slow step: Rate = $k_2[C][A]$. From eq: $K = \frac{[C]}{[A][B]} \implies [C] = K[A][B]$.
- Rate = $k_2 K [A]^2[B]$. $[A]\times2$, $[B]\times3$: factor = $2^2 \times 3 = 12$.

**3.J10 → Answer: (C)**
- Compare 1 & 2: [A] constant, [B]×2, rate×4 $\implies y=2$.
- Compare 1 & 3: [B] constant, [A]×2, rate×2 $\implies x=1$.
- Rate = $k[A][B]^2$. $k = \frac{1.0\times10^{-3}}{0.1 \times (0.1)^2} = 1.0\ \text{L}^2 \text{mol}^{-2} \text{s}^{-1}$.
</details>

---

## Key Takeaways from Chapter 3

| Concept | Rule |
|---------|------|
| Unit of $k$ | $(\text{mol L}^{-1})^{1-n} \text{s}^{-1}$ |
| Mechanisms | Rate is defined by the slowest step. Eliminate intermediates using $K_{eq}$. |
| Volume Halved | Concentration doubles. Multiply out the powers in the rate law. |

---

## 🧠 Stage 7: Statement & Assertion-Reasoning

| # | Question | Difficulty |
|---|----------|------------|
| 3.S1 | **Assertion (A):** The order of a reaction can be zero or fractional.<br>**Reason (R):** Order of a reaction is an experimentally determined quantity. | 🟢 |
| 3.S2 | **Assertion (A):** For a complex reaction, overall molecularity has no significance.<br>**Reason (R):** The overall rate is controlled by the slowest step, and different steps have different molecularities. | 🟡 |
| 3.S3 | **Assertion (A):** The order of a reaction can be determined from its balanced chemical equation.<br>**Reason (R):** Order is an experimentally determined quantity from rate data. | 🟢 |
| 3.S4 | **Assertion (A):** For an elementary reaction $2NO + O_2 \rightarrow 2NO_2$, the rate law is $k[NO]^2[O_2]$.<br>**Reason (R):** For elementary reactions, the order equals the molecularity. | 🟡 |
| 3.S5 | **Assertion (A):** The unit of rate constant for a zero order reaction is $\text{mol L}^{-1} \text{s}^{-1}$.<br>**Reason (R):** For zero order, Rate = $k$, and rate has units of $\text{mol L}^{-1} \text{s}^{-1}$. | 🟡 |
| 3.S6 | **Assertion (A):** The molecularity of a complex reaction is defined as the sum of stoichiometric coefficients.<br>**Reason (R):** Molecularity is meaningful only for elementary steps, not for overall complex reactions. | 🟡 |
| 3.S7 | **Assertion (A):** The rate law of a complex reaction can be derived solely from the balanced chemical equation.<br>**Reason (R):** The rate-determining step controls the overall rate, and different mechanisms can give different rate laws. | 🔴 |
| 3.S8 | **Assertion (A):** If the rate doubles when a reactant's concentration is doubled, the order with respect to that reactant must be 1.<br>**Reason (R):** From $(2)^n = 2$, solving gives $n = 1$. | 🔴 |
| 3.S9 | **Assertion (A):** The overall order of a reaction can be negative in some cases.<br>**Reason (R):** If a product inhibits the reaction, its concentration appears in the denominator, contributing a negative power to the rate law. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**3.S1 → Answer: (A)**
- Both true, R explains A.

**3.S2 → Answer: (A)**
- Both true. You cannot just count all the molecules in the overall balanced equation, because they don't all collide at the exact same time.

**3.S3 → Answer: (D)**
- A is false (order is experimental, not from the balanced equation). R is true. So A false, R true.

**3.S4 → Answer: (A)**
- For elementary reactions, Rate = $k[NO]^2[O_2]$. Both true, R correctly explains A.

**3.S5 → Answer: (A)**
- Zero order: Rate = $k$, so $k$ has same unit as rate. Both true, R explains A.

**3.S6 → Answer: (D)**
- A is false (molecularity of a complex reaction is not defined / has no meaning). R is true. So A false, R true.

**3.S7 → Answer: (D)**
- A is false (rate law requires experimental data or mechanism, not just the balanced equation). R is true. So A false, R true.

**3.S8 → Answer: (A)**
- $2^n = 2 \implies n = 1$. Both true, R explains A.

**3.S9 → Answer: (A)**
- Both true. E.g., $O_3$ decomposition: Rate = $k[O_3]^2[O_2]^{-1}$, order w.r.t $O_2$ is $-1$. Overall order = $1$. R explains how negative orders arise.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Q3.M1 🟢**
The unit of rate constant for a zero order reaction is:
<br>
(A) $\text{s}^{-1}$ <br>
(B) $\text{mol L}^{-1}\text{s}^{-1}$ <br>
(C) $\text{L mol}^{-1}\text{s}^{-1}$ <br>
(D) $\text{L}^2\text{mol}^{-2}\text{s}^{-1}$

**Q3.M2 🔴 (The Negative Order Trap)**
Can the order of a reaction with respect to a specific reactant be negative?
<br>
(A) No, order must be positive. <br>
(B) Yes, if it is a product in a reversible step acting as an inhibitor (like $O_2$ in $O_3$ decomposition). <br>
(C) Yes, but only for zero order overall reactions. <br>
(D) No, because concentration cannot be negative.

**Q3.M3 🟢**
The unit of rate constant for a first order reaction is:
<br>
(A) $\text{mol L}^{-1} \text{s}^{-1}$ <br>
(B) $\text{s}^{-1}$ <br>
(C) $\text{L mol}^{-1} \text{s}^{-1}$ <br>
(D) $\text{L}^2 \text{mol}^{-2} \text{s}^{-1}$

**Q3.M4 🟡**
For $A + 2B \rightarrow C$, the rate law is Rate = $k[A][B]^0$. The overall order is:
<br>
(A) 0 <br>
(B) 1 <br>
(C) 2 <br>
(D) 3

**Q3.M5 🟡**
Initial rate method data: [A] = 0.1, 0.2, 0.4 M; Rate = 0.02, 0.08, 0.32 M/s. The order w.r.t A is:
<br>
(A) 1 <br>
(B) 1.5 <br>
(C) 2 <br>
(D) 2.5

**Q3.M6 🟡**
$2A + B \rightarrow A_2B$. Mechanism: $A + B \rightleftharpoons C$ (fast); $A + C \rightarrow A_2B$ (slow). The rate law is:
<br>
(A) $k[A]^2[B]$ <br>
(B) $k[A][B]$ <br>
(C) $k[A]^2$ <br>
(D) $k[A][B]^2$

**Q3.M7 🟡**
$k = 3.0 \times 10^{-3}\ \text{L}^{3/2} \text{mol}^{-3/2} \text{s}^{-1}$. The overall order is:
<br>
(A) 1.5 <br>
(B) 2.0 <br>
(C) 2.5 <br>
(D) 3.0

**Q3.M8 🔴**
For $NO_2 + CO \rightarrow NO + CO_2$, Rate = $k[NO_2]^2$. Which mechanism is consistent?
<br>
(A) $NO_2 + NO_2 \rightarrow NO + NO_3$ (slow); $NO_3 + CO \rightarrow NO_2 + CO_2$ (fast) <br>
(B) $NO_2 + CO \rightarrow NO + CO_2$ (slow) <br>
(C) $NO_2 \rightleftharpoons NO + O$ (fast); $O + CO \rightarrow CO_2$ (slow) <br>
(D) $CO + NO_2 \rightarrow CO_2 + NO$ (slow)

**Q3.M9 🔴**
For $A + B \rightarrow$ Products: [A]=0.2, [B]=0.1, Rate=$8.0\times10^{-3}$; [A]=0.2, [B]=0.2, Rate=$1.6\times10^{-2}$; [A]=0.4, [B]=0.1, Rate=$3.2\times10^{-2}$. If [A]=0.5 M, [B]=0.3 M, the predicted rate (M/s) is:
<br>
(A) 0.12 <br>
(B) 0.15 <br>
(C) 0.18 <br>
(D) 0.24

<details>
<summary>💡 Full Solutions — MCQ Mastery</summary>

**3.M1 → Answer: (B)**
- Same as the unit of rate itself.

**3.M2 → Answer: (B)**
- See Example 3.3. The order w.r.t $O_2$ was -1. This means adding $O_2$ *slows down* the reaction.

**3.M3 → Answer: (B)**
- First order: $1-n = 0 \implies$ unit = $\text{s}^{-1}$.

**3.M4 → Answer: (B)**
- Order w.r.t B is 0. Overall order = $1 + 0 = 1$.

**3.M5 → Answer: (C)**
- 0.1$\to$0.2: ×2, rate 0.02$\to$0.08: ×4. 0.2$\to$0.4: ×2, rate 0.08$\to$0.32: ×4.
- $2^n = 4 \implies n = 2$.

**3.M6 → Answer: (A)**
- Rate = $k_2[C][A]$. $K = [C]/([A][B]) \implies [C] = K[A][B]$.
- Rate = $k_2 K [A]^2[B] = k[A]^2[B]$.

**3.M7 → Answer: (C)**
- $\text{L}^{3/2} \text{mol}^{-3/2} \text{s}^{-1} = (\text{mol L}^{-1})^{-3/2} \text{s}^{-1}$.
- $1-n = -3/2 \implies n = 5/2 = 2.5$.

**3.M8 → Answer: (A)**
- (A): Slow step Rate = $k[NO_2]^2$. ✓ Matches.
- (B) & (D): Rate = $k[NO_2][CO]$. ✗
- (C): Rate = $k[O][CO]$. $[O] = K[NO_2]/[NO]$. Rate = $kK[CO][NO_2]/[NO]$. ✗

**3.M9 → Answer: (B)**
- 1 & 2: [A] const, [B]×2, rate×2 $\implies y=1$.
- 1 & 3: [B] const, [A]×2, rate×4 $\implies x=2$.
- Rate = $k[A]^2[B]$. $k = \frac{8.0\times10^{-3}}{(0.2)^2 \times 0.1} = 2\ \text{L}^2 \text{mol}^{-2} \text{s}^{-1}$.
- At [A]=0.5, [B]=0.3: Rate = $2 \times (0.5)^2 \times 0.3 = 2 \times 0.25 \times 0.3 = 0.15$ M/s.
</details>
