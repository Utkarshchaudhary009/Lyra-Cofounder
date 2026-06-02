# Chapter 4: Integrated Rate Equations<br>
## Part II — Rate Law & Order

---

## 🎯 Stage 1: The Core Idea

### The Scene

Imagine you're trying to empty a water tank. 
Scenario A: You use a pump that removes exactly 5 liters every minute, regardless of how much water is left. It never slows down. 
Scenario B: You open a valve at the bottom. When the tank is full, the pressure is high, and water gushes out quickly. As the tank empties, the pressure drops, and the water trickles out slower and slower.

This is the exact difference between **Zero Order** and **First Order** reactions.

> An **integrated rate equation** relates the concentration of reactants to time, allowing us to determine the exact amount of reactant left at any given moment, or the time required for a specific fraction of the reaction to complete.

### The Big Two: Zero vs. First Order

| Feature | Zero Order (The Pump) | First Order (The Valve) |
|---------|------------------------|--------------------------|
| **Dependence on Concentration** | None. Rate is constant. | Direct. As concentration drops, rate drops. |
| **Pace** | Steady and relentless. | Fast at first, then slows down exponentially. |
| **Completion** | It goes to 100% completion in a finite time. | Theoretically takes infinite time to reach 100%. |
| **Real-life analogy** | A person typing at a constant speed of 50 WPM. | Radioactive decay; cooling of a hot cup of coffee. |

### The "Order" Refresher

Remember from the previous chapter: 
Rate = $k[A]^n$
If $n = 0$, Rate = $k$ (Zero Order)
If $n = 1$, Rate = $k[A]$ (First Order)

> ⚠️ **Classic Trap:** Don't assume a reaction is zero order just because it has a constant rate initially. The rate must remain constant *throughout* the entire reaction. Also, zero order reactions are *never* elementary (single-step) reactions; they are always complex, often involving a saturated catalyst surface or photochemical processes.

---

## 🔬 Stage 2: The Formula Lab

Let's derive the tools we need to solve the mysteries of time and concentration.

### Derivation 1: Zero Order Integrated Rate Law

Consider a general reaction: $A \rightarrow \text{Products}$
For a zero-order reaction:
$$-\frac{d[A]}{dt} = k[A]^0 = k$$
$$d[A] = -k \, dt$$

Integrating both sides:
$$\int_{[A]_0}^{[A]_t} d[A] = -k \int_{0}^{t} dt$$
$$[A]_t - [A]_0 = -kt$$

**The Final Formula:**
$$[A]_0 - [A]_t = kt$$
Or, $[A]_t = [A]_0 - kt$

*Where:*
- $[A]_0 =$ Initial concentration (at $t=0$)
- $[A]_t =$ Concentration at time $t$
- $k =$ Rate constant (Units: $\text{mol L}^{-1}\text{s}^{-1}$)

### Derivation 2: First Order Integrated Rate Law

For a first-order reaction:
$$-\frac{d[A]}{dt} = k[A]^1$$
$$\frac{d[A]}{[A]} = -k \, dt$$

Integrating both sides from $t=0$ to $t=t$:
$$\int_{[A]_0}^{[A]_t} \frac{d[A]}{[A]} = -k \int_{0}^{t} dt$$
$$\ln[A]_t - \ln[A]_0 = -kt$$
$$\ln\left(\frac{[A]_t}{[A]_0}\right) = -kt$$

Converting natural log ($\ln$) to base-10 log ($\log$):
$$2.303 \log\left(\frac{[A]_t}{[A]_0}\right) = -kt$$

**The Final Formula:**
$$k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$$
Or, in exponential form: $[A]_t = [A]_0 e^{-kt}$

> ⚠️ **Classic Trap:** The ratio in the log is $\frac{\text{Initial}}{\text{Final}}$. If you flip it to $\frac{\text{Final}}{\text{Initial}}$, your $k$ will come out negative, which is impossible.

### Formula 3: The Half-Life ($t_{1/2}$)

The half-life is the time required for the reactant concentration to drop to half of its initial value ($[A]_t = [A]_0 / 2$).

**For Zero Order:**
Substitute $[A]_t = [A]_0 / 2$ into $[A]_0 - [A]_t = kt$:
$$[A]_0 - \frac{[A]_0}{2} = kt_{1/2}$$
$$t_{1/2} = \frac{[A]_0}{2k}$$
*(Note: Half-life is directly proportional to initial concentration!)*

**For First Order:**
Substitute $[A]_t = [A]_0 / 2$ into $k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$:
$$k = \frac{2.303}{t_{1/2}} \log\left(\frac{[A]_0}{[A]_0/2}\right)$$
$$k = \frac{2.303}{t_{1/2}} \log(2)$$
Since $\log(2) \approx 0.301$:
$$t_{1/2} = \frac{2.303 \times 0.301}{k} = \frac{0.693}{k}$$
*(Note: Half-life is completely independent of initial concentration!)*

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Zero Order Calculations

**The Pattern:** You are given initial concentration, rate constant, and asked for time to reach a final concentration, or vice versa. Use $[A]_0 - [A]_t = kt$.

#### Solved Example 4.1
**Q:** A zero-order reaction has an initial concentration of $0.6\text{ M}$. The rate constant $k$ is $0.2\text{ M/s}$. How much time will it take for the concentration to decrease to $0.2\text{ M}$?<br> 🟢

**Solution:**
```
Identify values: [A]_0 = 0.6 M, [A]_t = 0.2 M, k = 0.2 M/s
Formula: [A]_0 - [A]_t = kt
Substitute: 0.6 - 0.2 = 0.2 * t
0.4 = 0.2 * t
t = 0.4 / 0.2 = 2 seconds
```

#### Solved Example 4.2
**Q:** Calculate the time required for a zero-order reaction to go to 100% completion if the initial concentration is $2.0\text{ M}$ and $k = 0.5\text{ M min}^{-1}$.<br> 🟡

**Solution:**
```
100% completion means final concentration [A]_t = 0.
Formula: [A]_0 - [A]_t = kt
2.0 - 0 = 0.5 * t
t = 2.0 / 0.5 = 4 minutes
```
*(Notice that for zero order, $t_{100\%} = [A]_0 / k$. It completes in finite time.)*

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 4.1a | For a zero order reaction, $[A]_0 = 1.5\text{ M}$, $k = 0.1\text{ M/s}$. Find $[A]$ after $5\text{ s}$. | 🟢 |
| 4.1b | A zero order reaction completes 50% in $20\text{ min}$. How much time will it take for 100% completion? | 🟡 |
| 4.1c | Calculate the rate constant of a zero-order reaction if its concentration drops from $0.8\text{ M}$ to $0.5\text{ M}$ in $15\text{ minutes}$. | 🟢 |
| 4.1d | What happens to the half-life of a zero-order reaction if the initial concentration is doubled? | 🟢 |
| 4.1e | A zero-order reaction has $[A]_0 = 2.0\text{ M}$ and $k = 0.25\text{ M s}^{-1}$. Find $[A]_t$ after $4$ seconds. | 🟢 |
| 4.1f | For a zero-order reaction, $[A]_0 = 4.0\text{ M}$ and after $10$ seconds $[A]_t = 3.0\text{ M}$. Find the rate constant $k$. | 🟢 |
| 4.1g | A zero-order reaction requires $12$ minutes for $60\%$ completion. Find the time required for $90\%$ completion. | 🟡 |
| 4.1h | The concentration of a reactant decreases from $0.5\text{ M}$ to $0.3\text{ M}$ in $20$ minutes in a zero-order reaction. Calculate $k$ and $t_{1/2}$. | 🟡 |
| 4.1i | A zero-order reaction has $t_{1/2} = 5$ hours when $[A]_0 = 0.8\text{ M}$. What is $t_{1/2}$ when $[A]_0 = 0.4\text{ M}$? | 🟡 |
| 4.1j | For a zero-order reaction, $75\%$ completion takes $30$ minutes. Find $[A]_0$ if $k = 0.05\text{ M min}^{-1}$. | 🔴 |
| 4.1k | In a zero-order reaction, $40\%$ decomposes in $10$ minutes. How long for $80\%$ decomposition? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**4.1a:**
$[A]_t = [A]_0 - kt = 1.5 - (0.1 \times 5) = 1.5 - 0.5 = 1.0\text{ M}$

**4.1b:**
For zero order, $t_{50\%} = \frac{[A]_0}{2k}$ and $t_{100\%} = \frac{[A]_0}{k}$.
Thus, $t_{100\%} = 2 \times t_{50\%} = 2 \times 20 = 40\text{ min}$.

**4.1c:**
$[A]_0 - [A]_t = kt$
$0.8 - 0.5 = k \times 15$
$0.3 = 15k \implies k = 0.02\text{ M min}^{-1}$

**4.1d:**
Since $t_{1/2} = \frac{[A]_0}{2k}$, if $[A]_0$ is doubled, the half-life is also doubled.

**4.1e:**
$[A]_t = [A]_0 - kt = 2.0 - (0.25 \times 4) = 2.0 - 1.0 = 1.0\text{ M}$

**4.1f:**
$[A]_0 - [A]_t = kt \implies 4.0 - 3.0 = k \times 10 \implies 1.0 = 10k \implies k = 0.10\text{ M s}^{-1}$

**4.1g:**
60% completion means $[A]_t = 0.4[A]_0$.
$[A]_0 - 0.4[A]_0 = k(12) \implies 0.6[A]_0 = 12k \implies k = 0.05[A]_0$.
For 90%: $[A]_0 - 0.1[A]_0 = kt \implies 0.9[A]_0 = 0.05[A]_0 t \implies t = 18\text{ min}$.

**4.1h:**
$k = \frac{0.5 - 0.3}{20} = \frac{0.2}{20} = 0.01\text{ M min}^{-1}$.
$t_{1/2} = \frac{[A]_0}{2k} = \frac{0.5}{2 \times 0.01} = 25\text{ min}$.

**4.1i:**
$t_{1/2} \propto [A]_0$ for zero order. Halving $[A]_0$ halves $t_{1/2}$.
New $t_{1/2} = 5/2 = 2.5$ hours.
(Or: $k = \frac{0.8}{2 \times 5} = 0.08\text{ M hr}^{-1}$; $t_{1/2} = \frac{0.4}{2 \times 0.08} = 2.5\text{ hr}$.)

**4.1j:**
75% done means $[A]_t = 0.25[A]_0$.
$[A]_0 - 0.25[A]_0 = 0.05 \times 30 \implies 0.75[A]_0 = 1.5 \implies [A]_0 = 2.0\text{ M}$.

**4.1k:**
40% decomposed: $[A]_t = 0.6[A]_0$.
$[A]_0 - 0.6[A]_0 = k(10) \implies 0.4[A]_0 = 10k \implies k = 0.04[A]_0$.
For 80%: $[A]_0 - 0.2[A]_0 = (0.04[A]_0)t \implies 0.8 = 0.04t \implies t = 20\text{ min}$.
</details>

---

### Type 2: First Order Rate Law Applications

**The Pattern:** Apply $k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$. Watch out for units of time and concentration.

#### Solved Example 4.3
**Q:** The initial concentration of $N_2O_5$ in a first-order liquid phase decomposition is $1.24 \times 10^{-2}\text{ mol L}^{-1}$. After $60\text{ minutes}$, the concentration becomes $0.20 \times 10^{-2}\text{ mol L}^{-1}$. Calculate the rate constant.<br> 🟡

**Solution:**
```
[A]_0 = 1.24 * 10^{-2} M
[A]_t = 0.20 * 10^{-2} M
t = 60 min
k = (2.303 / t) * log([A]_0 / [A]_t)
k = (2.303 / 60) * log(1.24 / 0.20)
k = (2.303 / 60) * log(6.2)
log(6.2) is approx 0.792 (from log tables)
k = (2.303 * 0.792) / 60 = 0.0304 min^{-1}
```

#### Solved Example 4.4
**Q:** A first order reaction has a rate constant $1.15 \times 10^{-3}\text{ s}^{-1}$. How long will $5\text{ g}$ of this reactant take to reduce to $3\text{ g}$?<br> 🟡

**Solution:**
```
Since ratio of masses is equal to ratio of concentrations (assuming constant volume), we can use masses directly.
a = 5 g, (a-x) = 3 g
k = 1.15 * 10^{-3} s^{-1}
t = (2.303 / k) * log(a / (a-x))
t = (2.303 / 1.15 * 10^{-3}) * log(5/3)
log(5/3) = log 5 - log 3 = 0.699 - 0.477 = 0.222
t = (2.303 * 0.222) / (1.15 * 10^{-3}) = 444 seconds
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 4.2a | A first-order reaction has $k = 10^{-2}\text{ s}^{-1}$. Calculate the time required to reduce the initial concentration to 1/10th of its initial value. | 🟢 |
| 4.2b | The rate constant of a reaction is $0.0693\text{ min}^{-1}$. If it's a first order reaction, find the time taken to drop the concentration from $1.0\text{ M}$ to $0.25\text{ M}$. | 🟡 |
| 4.2c | Prove that for a first order reaction, $t_{90\%} = \frac{2.303}{k}$. | 🟡 |
| 4.2d | $A \rightarrow B$ is a first order reaction. If $[A]_0 = 100$, and after $2\text{ hours}$ $[A]_t = 25$, find $k$. | 🟢 |
| 4.2e | A first-order reaction has $k = 0.0231\text{ min}^{-1}$. Find $t_{1/2}$. | 🟢 |
| 4.2f | For a first-order reaction, $75\%$ completes in $40$ minutes. Determine $k$. | 🟢 |
| 4.2g | A first-order reaction is $25\%$ complete in $30$ minutes. How long for $75\%$ completion? | 🟡 |
| 4.2h | The concentration drops from $0.6\text{ M}$ to $0.15\text{ M}$ in $50$ minutes for a first-order reaction. Find $k$. | 🟡 |
| 4.2i | A first-order reaction has $t_{1/2} = 20\text{ min}$. What time for $93.75\%$ completion? | 🟡 |
| 4.2j | A first-order reaction is $30\%$ complete in $25$ minutes. Find $t_{1/2}$. (Given: $\log 7 = 0.845$) | 🔴 |
| 4.2k | For a first-order reaction, $k = 3.465 \times 10^{-3}\text{ s}^{-1}$ and $[A]_0 = 2.0\text{ M}$. Find $[A]_t$ after $500\text{ s}$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**4.2a:**
$[A]_t = [A]_0 / 10 \implies [A]_0/[A]_t = 10$.
$t = \frac{2.303}{10^{-2}} \log(10) = 230.3\text{ seconds}$.

**4.2b:**
$1.0\text{ M} \rightarrow 0.5\text{ M} \rightarrow 0.25\text{ M}$. This is two half-lives.
$t_{1/2} = \frac{0.693}{0.0693} = 10\text{ min}$.
Total time = $2 \times 10 = 20\text{ minutes}$.
(Or use the formula: $t = \frac{2.303}{0.0693} \log(1.0/0.25) = \frac{2.303}{0.0693} \log(4) \approx 20\text{ min}$).

**4.2c:**
For 90% completion, $10\%$ is left. So $[A]_t = 0.1 [A]_0$.
$t_{90\%} = \frac{2.303}{k} \log\left(\frac{100}{10}\right) = \frac{2.303}{k} \log(10) = \frac{2.303}{k} \times 1 = \frac{2.303}{k}$.

**4.2d:**
$[A]_0 = 100$, $[A]_t = 25$.
$k = \frac{2.303}{2} \log\left(\frac{100}{25}\right) = 1.1515 \log(4) = 1.1515 \times 0.602 = 0.693\text{ hr}^{-1}$.
(Or simply recognize it's 2 half-lives, $2 t_{1/2} = 2\text{ hr} \implies t_{1/2} = 1\text{ hr} \implies k = 0.693/1 = 0.693\text{ hr}^{-1}$).

**4.2e:**
$t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0231} = 30\text{ min}$.

**4.2f:**
75% done means $[A]_t = 0.25[A]_0$.
$k = \frac{2.303}{40} \log\left(\frac{1}{0.25}\right) = \frac{2.303}{40} \log(4) = \frac{2.303}{40} \times 0.602 = 0.03466\text{ min}^{-1}$.

**4.2g:**
25% done means $[A]_t = 0.75[A]_0$.
$k = \frac{2.303}{30} \log\left(\frac{1}{0.75}\right) = \frac{2.303}{30} \log\left(\frac{4}{3}\right) = \frac{2.303}{30}(0.602 - 0.477) = \frac{2.303 \times 0.125}{30} = 0.009596\text{ min}^{-1}$.
For 75%: $t = \frac{2.303}{0.009596} \log(4) = \frac{2.303 \times 0.602}{0.009596} \approx 144.4\text{ min}$.

**4.2h:**
$0.6 \rightarrow 0.3 \rightarrow 0.15$ is two half-lives.
$2 \times t_{1/2} = 50 \implies t_{1/2} = 25\text{ min}$.
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{25} = 0.02772\text{ min}^{-1}$.

**4.2i:**
93.75% done means $6.25\%$ remains $= \frac{1}{16} = \left(\frac{1}{2}\right)^4$.
So 4 half-lives have passed.
$t = 4 \times 20 = 80\text{ min}$.

**4.2j:**
30% done means $70\%$ remains: $[A]_t = 0.7[A]_0$.
$k = \frac{2.303}{25} \log\left(\frac{10}{7}\right) = \frac{2.303}{25}(1 - 0.845) = \frac{2.303 \times 0.155}{25} = 0.01428\text{ min}^{-1}$.
$t_{1/2} = \frac{0.693}{0.01428} \approx 48.5\text{ min}$.

**4.2k:**
$k = \frac{2.303}{t} \log\frac{[A]_0}{[A]_t} \implies \log\frac{2.0}{[A]_t} = \frac{3.465 \times 10^{-3} \times 500}{2.303} = \frac{1.7325}{2.303} = 0.7523$.
$\frac{2.0}{[A]_t} = \text{antilog}(0.7523) \approx 5.657 \implies [A]_t = \frac{2.0}{5.657} = 0.354\text{ M}$.
</details>

---

### Type 3: Half-Life Relationships

**The Pattern:** Finding half-life from $k$, or $k$ from half-life, or using the $n$-th order formula $t_{1/2} \propto 1/[A]_0^{n-1}$.

#### Solved Example 4.5
**Q:** The half-life of a reaction $A \rightarrow \text{Product}$ is represented by $t_{1/2} \propto 1/[A]_0^2$. What is the order of the reaction?<br> 🟢

**Solution:**
```
The general formula is t_1/2 ∝ 1 / [A]_0^{n-1}
Comparing exponents:
n - 1 = 2
n = 3
The reaction is Third Order.
```

#### Solved Example 4.6
**Q:** A first order reaction takes $40\text{ minutes}$ for 30% decomposition. Calculate its half-life. (Given $\log 7 = 0.845$) <br> 🔴

**Solution:**
```
30% decomposition means 70% is remaining!
[A]_0 = 100
[A]_t = 100 - 30 = 70
t = 40 min

k = (2.303 / 40) * log(100 / 70)
k = (2.303 / 40) * log(10 / 7)
k = (2.303 / 40) * (log 10 - log 7)
k = (2.303 / 40) * (1 - 0.845)
k = (2.303 / 40) * 0.155 = 0.00892 min^{-1}

Now, calculate half-life:
t_1/2 = 0.693 / k = 0.693 / 0.00892 = 77.7 minutes
```
> ⚠️ **Trap Alert:** Many students put 30 in the denominator. $[A]_t$ is the amount *remaining*, not the amount *reacted*!

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 4.3a | The half-life of a first order reaction is $60\text{ min}$. How long will it take to complete 50%? | 🟢 |
| 4.3b | The half-life period for a zero order reaction is $2\text{ hours}$. If initial concentration is $2\text{ M}$, calculate the rate constant. | 🟡 |
| 4.3c | A reaction obeys the expression $t_{1/2} = \frac{1}{ka}$. What is its order? | 🟡 |
| 4.3d | If $t_{1/2}$ is independent of initial concentration, what is the order? | 🟢 |
| 4.3e | A first-order reaction has $k = 0.0693\text{ s}^{-1}$. Calculate $t_{1/2}$. | 🟢 |
| 4.3f | The half-life of a reaction is inversely proportional to $[A]_0$. What is the order? | 🟢 |
| 4.3g | For a reaction, $t_{1/2} = 50\text{ min}$ at $[A]_0 = 0.2\text{ M}$ and $t_{1/2} = 25\text{ min}$ at $[A]_0 = 0.4\text{ M}$. Determine the order. | 🟡 |
| 4.3h | $t_{1/2}$ of a zero-order reaction is $30\text{ min}$ when $[A]_0 = 1.2\text{ M}$. Find $k$ and the time for $75\%$ completion. | 🟡 |
| 4.3i | A first-order reaction has $t_{1/2} = 15\text{ min}$. What fraction remains after $1$ hour? | 🟡 |
| 4.3j | For a reaction, $t_{1/2} = 20\text{ min}$ at $[A]_0 = 2.0\text{ M}$ and $t_{1/2} = 40\text{ min}$ at $[A]_0 = 1.0\text{ M}$. Find the order and $k$. | 🔴 |
| 4.3k | In a first-order reaction, concentration falls from $0.5\text{ M}$ to $0.125\text{ M}$ in $30$ minutes. Find $t_{1/2}$ and $k$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**4.3a:**
Half-life *is* the time for 50% completion. So, $60\text{ minutes}$.

**4.3b:**
$t_{1/2} = \frac{[A]_0}{2k} \implies 2 = \frac{2}{2k} \implies k = 0.5\text{ M hr}^{-1}$.

**4.3c:**
$t_{1/2} \propto 1/a^1$.
Comparing with $1/a^{n-1}$, we get $n - 1 = 1 \implies n = 2$. **Second Order**.

**4.3d:**
If it is independent, $t_{1/2} \propto a^0$.
$n - 1 = 0 \implies n = 1$. **First Order**.

**4.3e:**
$t_{1/2} = \frac{0.693}{k} = \frac{0.693}{0.0693} = 10\text{ s}$.

**4.3f:**
$t_{1/2} \propto \frac{1}{[A]_0^{n-1}}$. If $t_{1/2} \propto 1/[A]_0$, then $n-1 = 1 \implies n = 2$. **Second Order**.

**4.3g:**
When $[A]_0$ doubles, $t_{1/2}$ halves. So $t_{1/2} \propto 1/[A]_0$.
$n-1 = 1 \implies n = 2$. **Second Order**.

**4.3h:**
$t_{1/2} = \frac{[A]_0}{2k} \implies 30 = \frac{1.2}{2k} \implies k = 0.02\text{ M min}^{-1}$.
For 75%: $[A]_t = 0.25[A]_0$.
$1.2 - 0.3 = 0.02t \implies 0.9 = 0.02t \implies t = 45\text{ min}$.

**4.3i:**
$t = 1\text{ hr} = 60\text{ min}$. Number of half-lives $= 60/15 = 4$.
Fraction remaining $= \left(\frac{1}{2}\right)^4 = \frac{1}{16}$.

**4.3j:**
$[A]_0$ halves $\implies$ $t_{1/2}$ doubles. So $t_{1/2} \propto [A]_0$.
$t_{1/2} \propto [A]_0^1 \implies t_{1/2} \propto 1/[A]_0^{-1} \implies n-1 = -1 \implies n = 0$. **Zero Order**.
$k = \frac{[A]_0}{2t_{1/2}} = \frac{2.0}{2 \times 20} = 0.05\text{ M min}^{-1}$.

**4.3k:**
$0.5 \rightarrow 0.25 \rightarrow 0.125$ is two half-lives.
$2 \times t_{1/2} = 30 \implies t_{1/2} = 15\text{ min}$.
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{15} = 0.0462\text{ min}^{-1}$.
</details>

---

### Type 4: Graphical Methods

**The Pattern:** Identifying the order or parameters ($k$, initial concentration) from graphs.

#### Solved Example 4.7
**Q:** A graph plotted between $\ln[A]_t$ vs $t$ is a straight line with a negative slope. What is the order of the reaction and what does the slope equal?<br> 🟢

**Solution:**
```
The equation for a first-order reaction is:
ln[A]_t = ln[A]_0 - kt
This is in the form of y = c + mx (equation of a straight line).
Here, y = ln[A]_t, x = t.
Slope (m) = -k
Intercept (c) = ln[A]_0
Answer: First Order; Slope = -k.
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 4.4a | A plot of $[A]_t$ vs $t$ gives a straight line. What is the order? | 🟢 |
| 4.4b | For a zero order reaction, what is plotted against what to get a horizontal line parallel to the time axis? | 🟡 |
| 4.4c | In a first order reaction, a plot of $\log[A]_t$ vs time is drawn. What is the slope? | 🟡 |
| 4.4d | For a reaction, a plot of $\log[A]_t$ vs $t$ is a straight line. What is the order? | 🟢 |
| 4.4e | What is the intercept of the straight line obtained by plotting $\log[A]_t$ vs $t$ for a first-order reaction? | 🟢 |
| 4.4f | A plot of $[A]_t$ vs $t$ gives a straight line with slope $= -0.05$. If $[A]_0 = 2.0\text{ M}$, find $k$ and the order. | 🟡 |
| 4.4g | For a zero-order reaction, what quantity plotted vs $t$ gives a straight line with slope $= k$? | 🟡 |
| 4.4h | A plot of $t_{1/2}$ vs $[A]_0$ for a reaction is a horizontal line. What is the order? | 🟡 |
| 4.4i | For a first-order reaction, a plot of $\log([A]_0/[A]_t)$ vs $t$ is a straight line. What is its slope? | 🔴 |
| 4.4j | Two first-order reactions have slopes of $\log[A]_t$ vs $t$ in the ratio $2:3$. What is the ratio of their $k$ values? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**4.4a:**
$[A]_t = [A]_0 - kt$. This is a straight line for **Zero Order**.

**4.4b:**
**Rate vs Time**. For zero order, rate $= k$, which is constant and doesn't change with time.

**4.4c:**
$\log[A]_t = \log[A]_0 - \frac{k}{2.303} t$.
Slope $= -\frac{k}{2.303}$.

**4.4d:**
$\log[A]_t = \log[A]_0 - \frac{k}{2.303}t$. Straight line of $\log[A]_t$ vs $t$ indicates **First Order**.

**4.4e:**
From $\log[A]_t = \log[A]_0 - \frac{k}{2.303}t$, intercept $= \log[A]_0$.

**4.4f:**
$[A]_t$ vs $t$ linear $\implies$ **Zero Order**. Slope $= -k = -0.05 \implies k = 0.05\text{ M s}^{-1}$.

**4.4g:**
For zero order: $[A]_0 - [A]_t = kt$. Plot $([A]_0 - [A]_t)$ vs $t$ to get slope $= k$.

**4.4h:**
Horizontal line means $t_{1/2}$ is independent of $[A]_0$. This is characteristic of **First Order**.

**4.4i:**
$\log\left(\frac{[A]_0}{[A]_t}\right) = \frac{k}{2.303}t$. Comparing with $y = mx$, slope $= \frac{k}{2.303}$.

**4.4j:**
For first order, slope of $\log[A]_t$ vs $t$ is $-\frac{k}{2.303}$.
$|m| \propto k$. Ratio of $k$ values $= 2:3$.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 4.M1 | A first-order reaction is 20% complete in 10 minutes. Calculate the time required for 80% completion. | T2 + T3 | 🔴 |
| 4.M2 | For a certain reaction, a plot of $t_{1/2}$ versus $[A]_0$ is a straight line passing through the origin. Identify the order and calculate the rate constant if the slope is 0.25. | T3 + T4 | 🟡 |
| 4.M3 | $A \rightarrow B$ is zero order. Initial concentration is $0.2\text{ M}$ and half-life is $6\text{ hr}$. What is the concentration after $9\text{ hr}$? | T1 + T3 | 🔴 |
| 4.M4 | A first-order reaction is $50\%$ complete in $30$ minutes. Another first-order reaction is $50\%$ complete in $60$ minutes. Find the ratio $k_1:k_2$ with same $[A]_0$. | T2 + T3 | 🟡 |
| 4.M5 | Zero-order reaction: $[A]_0 = 0.8\text{ M}$, $k = 0.04\text{ M min}^{-1}$. Find $[A]$ after $10$ min and additional time for $100\%$ completion. | T1 + T3 | 🟡 |
| 4.M6 | $t_{1/2} \propto 1/[A]_0^2$. If $[A]_0 = 0.5\text{ M}$ and $t_{1/2} = 20\text{ min}$, find the order and $k$. | T3 + T2 | 🔴 |
| 4.M7 | A first-order reaction has $[A]_0 = 0.4\text{ M}$ and after $25$ min $[A]_t = 0.1\text{ M}$. Find $t_{90\%}$. | T2 + T3 | 🟡 |
| 4.M8 | Slope of $\log[A]_t$ vs $t$ is $-0.02\text{ s}^{-1}$. Find $k$ and the time for $[A]_t = 0.01[A]_0$. | T4 + T2 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**4.M1:**
Step 1: Find k from 20% completion.
$[A]_0 = 100$, $[A]_t = 100 - 20 = 80$.
$k = \frac{2.303}{10} \log\left(\frac{100}{80}\right) = 0.2303 \log(1.25) \approx 0.2303 \times 0.0969 = 0.0223\text{ min}^{-1}$.

Step 2: Find time for 80% completion.
$[A]_0 = 100$, $[A]_t = 100 - 80 = 20$.
$t = \frac{2.303}{0.0223} \log\left(\frac{100}{20}\right) = \frac{2.303}{0.0223} \log(5) \approx 103.2 \times 0.699 = 72.1\text{ minutes}$.

**4.M2:**
Since $t_{1/2} \propto [A]_0$, it is a **Zero Order** reaction.
For zero order, $t_{1/2} = \frac{1}{2k} [A]_0$.
Slope $= \frac{1}{2k} = 0.25 \implies 2k = 4 \implies k = 2\text{ M}^{-1}\text{s}^{-1}$ (or appropriate time unit).

**4.M3:**
Step 1: Find k.
$t_{1/2} = \frac{[A]_0}{2k} \implies 6 = \frac{0.2}{2k} \implies 12k = 0.2 \implies k = 0.01667\text{ M hr}^{-1}$.

Step 2: Find $[A]_t$ at 9 hrs.
$[A]_t = [A]_0 - kt = 0.2 - (0.01667 \times 9) = 0.2 - 0.15 = 0.05\text{ M}$.

**4.M4:**
$t_{1/2} = \frac{0.693}{k}$. $k \propto 1/t_{1/2}$.
$k_1/k_2 = t_{1/2,2}/t_{1/2,1} = 60/30 = 2$. So $k_1:k_2 = 2:1$.

**4.M5:**
$[A]_{10} = 0.8 - 0.04 \times 10 = 0.4\text{ M}$.
$t_{100\%} = [A]_0/k = 0.8/0.04 = 20\text{ min}$.
Additional time $= 20 - 10 = 10\text{ min}$.

**4.M6:**
$t_{1/2} \propto 1/[A]_0^2 \implies n-1 = 2 \implies n = 3$. **Third Order**.
$t_{1/2} = \frac{3}{2k[A]_0^2} \implies 20 = \frac{3}{2k(0.5)^2} = \frac{3}{0.5k} \implies k = \frac{3}{0.5 \times 20} = 0.3\text{ M}^{-2}\text{ min}^{-1}$.

**4.M7:**
$0.4 \rightarrow 0.2 \rightarrow 0.1$ is two half-lives.
$2 \times t_{1/2} = 25 \implies t_{1/2} = 12.5\text{ min}$, $k = 0.693/12.5 = 0.05544\text{ min}^{-1}$.
$t_{90\%} = \frac{2.303}{0.05544} \log(10) = 41.54\text{ min}$.

**4.M8:**
For first order: slope of $\log[A]_t$ vs $t = -\frac{k}{2.303}$.
$k = 0.02 \times 2.303 = 0.04606\text{ s}^{-1}$.
$t = \frac{2.303}{k} \log(100) = \frac{2.303 \times 2}{0.04606} = 100\text{ s}$.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 4.B1 | Derive the integrated rate equation for a zero-order reaction. | 🟢 |
| 4.B2 | Show that the time required for 99% completion is twice the time required for the completion of 90% of a first-order reaction. ⭐ | 🔴 |
| 4.B3 | Identify the order of a reaction from the following unit of its rate constant: $\text{L mol}^{-1}\text{s}^{-1}$. | 🟢 |
| 4.B4 | A first-order reaction has a rate constant of $0.0051\text{ min}^{-1}$. If we begin with $0.10\text{ M}$ concentration of the reactant, what concentration of reactant will be left after $3\text{ hours}$? | 🟡 |
| 4.B5 | What is the effect of doubling the initial concentration on the half-life of a (i) zero-order reaction, and (ii) first-order reaction? | 🟢 |
| 4.B6 | Write the half-life expression for a first-order reaction and state its dependence on $[A]_0$. | 🟢 |
| 4.B7 | The slope of $[A]_t$ vs $t$ for a zero-order reaction is $-0.15\text{ M s}^{-1}$ and $[A]_0 = 3.0\text{ M}$. Find $[A]_t$ after $10$ s and $t_{1/2}$. | 🟡 |
| 4.B8 | For a first-order reaction, show that $t_{99.9\%} = 3 \times t_{90\%}$. | 🟡 |
| 4.B9 | A zero-order reaction is $20\%$ complete in $5$ minutes. Find the time for $80\%$ completion and $t_{1/2}$ if $[A]_0 = 0.5\text{ M}$. | 🔴 |
| 4.B10 | At $[A]_0 = 0.1\text{ M}$, $t_{1/2} = 40\text{ min}$; at $[A]_0 = 0.2\text{ M}$, $t_{1/2} = 20\text{ min}$. Determine the order and $k$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**4.B1:**
Refer to Stage 2, Derivation 1 for the complete derivation step-by-step. Ensure you show the integration limits from $0$ to $t$.

**4.B2:**
For 99% completion: $[A]_t = 1\%$ of $[A]_0 = 0.01 [A]_0$.
$t_{99\%} = \frac{2.303}{k} \log\left(\frac{[A]_0}{0.01 [A]_0}\right) = \frac{2.303}{k} \log(100) = \frac{2.303}{k} \times 2 = \frac{4.606}{k}$.

For 90% completion: $[A]_t = 10\%$ of $[A]_0 = 0.1 [A]_0$.
$t_{90\%} = \frac{2.303}{k} \log\left(\frac{[A]_0}{0.1 [A]_0}\right) = \frac{2.303}{k} \log(10) = \frac{2.303}{k} \times 1 = \frac{2.303}{k}$.

Comparing the two: $t_{99\%} = 2 \times t_{90\%}$. (Proved).

**4.B3:**
General unit of k is $(\text{mol L}^{-1})^{1-n}\text{s}^{-1}$.
Here it is $\text{L mol}^{-1}\text{s}^{-1} = (\text{mol L}^{-1})^{-1}\text{s}^{-1}$.
$1 - n = -1 \implies n = 2$.
It is a **Second Order** reaction.

**4.B4:**
$k = 0.0051\text{ min}^{-1}$, $t = 3\text{ hours} = 180\text{ minutes}$.
$k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$
$0.0051 = \frac{2.303}{180} \log\left(\frac{0.10}{[A]_t}\right)$
$\log\left(\frac{0.10}{[A]_t}\right) = \frac{0.0051 \times 180}{2.303} = 0.398$
$\frac{0.10}{[A]_t} = \text{antilog}(0.398) = 2.5$
$[A]_t = \frac{0.10}{2.5} = 0.04\text{ M}$.

**4.B5:**
(i) For zero order, $t_{1/2} = \frac{[A]_0}{2k}$. If initial concentration is doubled, half-life is **doubled**.
(ii) For first order, $t_{1/2} = \frac{0.693}{k}$. It is independent of initial concentration. Half-life remains **unchanged**.

**4.B6:**
$t_{1/2} = \frac{0.693}{k}$. For first order, $t_{1/2}$ is independent of $[A]_0$.

**4.B7:**
Slope $= -k = -0.15 \implies k = 0.15\text{ M s}^{-1}$ (Zero Order).
$[A]_{10} = 3.0 - 0.15 \times 10 = 1.5\text{ M}$.
$t_{1/2} = \frac{[A]_0}{2k} = \frac{3.0}{2 \times 0.15} = 10\text{ s}$.

**4.B8:**
99.9% done: $[A]_t = 0.001[A]_0$.
$t_{99.9\%} = \frac{2.303}{k} \log(1000) = \frac{2.303}{k} \times 3 = \frac{6.909}{k}$.
$t_{90\%} = \frac{2.303}{k}$.
Thus, $t_{99.9\%} = 3 \times t_{90\%}$.

**4.B9:**
20% done: $[A]_t = 0.8[A]_0$.
$[A]_0 - 0.8[A]_0 = k \times 5 \implies 0.2[A]_0 = 5k \implies k = 0.04[A]_0$.
For 80%: $0.8[A]_0 = (0.04[A]_0)t \implies t = 20\text{ min}$.
$t_{1/2} = \frac{[A]_0}{2k} = \frac{[A]_0}{2 \times 0.04[A]_0} = 12.5\text{ min}$.

**4.B10:**
$[A]_0$ doubles, $t_{1/2}$ halves $\implies t_{1/2} \propto 1/[A]_0$.
$n-1 = 1 \implies n = 2$. **Second Order**.
$t_{1/2} = \frac{1}{k[A]_0} \implies 40 = \frac{1}{k \times 0.1} \implies k = \frac{10}{40} = 0.25\text{ M}^{-1}\text{ min}^{-1}$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q4.J1 🟡**
For a zero order reaction, the plot of $[A]_t$ vs time is linear with:
(A) +ve slope and zero intercept
(B) -ve slope and zero intercept
(C) +ve slope and non-zero intercept
(D) -ve slope and non-zero intercept

**Q4.J2 🔴 ⭐**
The half-life of a first order reaction is $10\text{ min}$. If initial amount is $0.08\text{ mol L}^{-1}$ and concentration at some instant is $0.01\text{ mol L}^{-1}$, then time $t$ is:
(A) $10\text{ min}$
(B) $30\text{ min}$
(C) $20\text{ min}$
(D) $40\text{ min}$

**Q4.J3 🟡**
Time required to decompose half of the substance for an $n$-th order reaction is inversely proportional to:
(A) $a^{n+1}$
(B) $a^{n-1}$
(C) $a^{n-2}$
(D) $a^n$

**Q4.J4 🔴**
A graph plotted between $\log t_{50\%}$ vs $\log a$ is a straight horizontal line parallel to the x-axis. What conclusion can you draw?
(A) $n=1, t_{1/2} = \frac{k}{a}$
(B) $n=2, t_{1/2} = \frac{1}{a}$
(C) $n=1, t_{1/2} = \frac{0.693}{k}$
(D) $n=0, t_{1/2} = \frac{a}{2k}$

**Q4.J5 🔴 (The 100% Trap)**
Which of the following reactions will never go to 100% completion in a finite time?
(A) Zero order
(B) First order
(C) Fractional order
(D) Only radioactive decay

**Q4.J6 🟡**
For a zero-order reaction, if $[A]_0$ is tripled, the half-life becomes:
(A) Three times
(B) One-third
(C) Same
(D) Nine times

**Q4.J7 🟡**
A first-order reaction is $90\%$ complete in $50$ minutes. Its $t_{1/2}$ is approximately:
(A) $5\text{ min}$
(B) $15\text{ min}$
(C) $25\text{ min}$
(D) $35\text{ min}$

**Q4.J8 🔴**
The unit of rate constant for a reaction whose half-life is independent of initial concentration is:
(A) $\text{mol L}^{-1}\text{s}^{-1}$
(B) $\text{s}^{-1}$
(C) $\text{L mol}^{-1}\text{s}^{-1}$
(D) $\text{L}^2\text{ mol}^{-2}\text{s}^{-1}$

**Q4.J9 🔴**
Which graph correctly represents the change in half-life with initial concentration for a zero-order reaction?
(A) Rising straight line through origin
(B) Horizontal straight line
(C) Rising curve
(D) Falling curve

**Q4.J10 🔴**
In a first-order reaction, concentration decreases from $0.8\text{ M}$ to $0.2\text{ M}$ in $40$ minutes. The rate constant ($\text{min}^{-1}$) is:
(A) $\frac{0.693}{40}$
(B) $\frac{0.693}{20}$
(C) $\frac{0.693}{10}$
(D) $\frac{0.693}{80}$

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**4.J1 → Answer: (D)**
Equation: $[A]_t = -kt + [A]_0$. This is $y = mx + c$.
Slope (m) is $-k$ (negative). Intercept (c) is $[A]_0$ (non-zero).

**4.J2 → Answer: (B)**
Concentration halves every $10\text{ min}$.
$0.08 \xrightarrow{10\text{ min}} 0.04 \xrightarrow{10\text{ min}} 0.02 \xrightarrow{10\text{ min}} 0.01$.
Three half-lives have passed. Total time $= 3 \times 10 = 30\text{ minutes}$.

**4.J3 → Answer: (B)**
The general formula is $t_{1/2} \propto \frac{1}{a^{n-1}}$. Therefore, it is inversely proportional to $a^{n-1}$.

**4.J4 → Answer: (C)**
A horizontal line for $\log t_{50\%}$ vs $\log a$ means $t_{50\%}$ does not change when $a$ changes.
It is independent of initial concentration. This is the hallmark of a **First Order** reaction.
For first order, $t_{1/2} = \frac{0.693}{k}$.

**4.J5 → Answer: (B)**
First order reactions follow an exponential decay curve ($[A]_t = [A]_0 e^{-kt}$). The concentration approaches zero asymptotically, meaning it theoretically requires infinite time to reach 100% completion. Zero order reactions complete in finite time ($t = [A]_0 / k$).

**4.J6 → Answer: (A)**
$t_{1/2} = \frac{[A]_0}{2k}$. Tripling $[A]_0$ triples $t_{1/2}$.

**4.J7 → Answer: (B)**
$k = \frac{2.303}{50} \log(10) = 0.04606\text{ min}^{-1}$.
$t_{1/2} = \frac{0.693}{0.04606} \approx 15\text{ min}$.

**4.J8 → Answer: (B)**
$t_{1/2}$ independent of $[A]_0$ means first order. Unit of $k$ for first order is $\text{s}^{-1}$.

**4.J9 → Answer: (A)**
For zero order: $t_{1/2} = \frac{[A]_0}{2k}$. This is a straight line through origin with positive slope.

**4.J10 → Answer: (B)**
$0.8 \rightarrow 0.4 \rightarrow 0.2$ is two half-lives.
$2 \times t_{1/2} = 40 \implies t_{1/2} = 20\text{ min}$.
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{20}$.
</details>

---

## 🧠 Stage 7: Assertion-Reasoning

**Directions:**
(A) Both A and R are true, and R is the correct explanation of A.
(B) Both A and R are true, but R is NOT the correct explanation of A.
(C) A is true but R is false.
(D) A is false but R is true.

| # | Question | Difficulty |
|---|----------|------------|
| 4.S1 | **Assertion (A):** For a zero-order reaction, the half-life depends on the initial concentration.<br>**Reason (R):** For a zero order reaction, rate is independent of concentration. | 🟡 |
| 4.S2 | **Assertion (A):** The unit of rate constant for a first-order reaction is time$^{-1}$.<br>**Reason (R):** The rate of a first-order reaction is independent of reactant concentration. | 🟢 |
| 4.S3 | **Assertion (A):** A plot of $\log[A]$ vs $t$ for a first-order reaction gives a straight line with slope $-k/2.303$.<br>**Reason (R):** Integrated rate equation is $k = \frac{2.303}{t} \log\frac{[A]_0}{[A]_t}$. | 🟡 |
| 4.S4 | **Assertion (A):** It takes finite time for a zero-order reaction to reach 100% completion.<br>**Reason (R):** The reactant is consumed at a constant rate until it is completely gone. | 🟢 |
| 4.S5 | **Assertion (A):** The half-life of a first order reaction is $10\text{ min}$. It will complete 75% in $20\text{ min}$.<br>**Reason (R):** For first order, $t_{75\%} = 2 \times t_{50\%}$. | 🟡 |
| 4.S6 | **Assertion (A):** For a zero-order reaction, $t_{100\%} = 2 \times t_{50\%}$.<br>**Reason (R):** $t_{50\%} = \frac{[A]_0}{2k}$ and $t_{100\%} = \frac{[A]_0}{k}$ for zero order. | 🟡 |
| 4.S7 | **Assertion (A):** The half-life of a first-order reaction is independent of initial concentration.<br>**Reason (R):** The rate constant of a first-order reaction does not depend on reactant concentration. | 🟡 |
| 4.S8 | **Assertion (A):** A plot of $\log[A]_t$ vs $t$ for a first-order reaction has slope $= -\frac{k}{2.303}$.<br>**Reason (R):** Integrated rate law gives $\log[A]_t = \log[A]_0 - \frac{k}{2.303}t$. | 🔴 |
| 4.S9 | **Assertion (A):** For a zero-order reaction, $[A]_t$ vs $t$ graph has negative slope equal to $-k$.<br>**Reason (R):** For zero order, rate $= k$, which is independent of concentration. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**4.S1 → Answer: (B)**
A is true ($t_{1/2} = [A]_0 / 2k$, so it depends on $[A]_0$).
R is true (rate = $k[A]^0 = k$, independent of concentration).
However, R does not explain A. The correct explanation is the mathematical derivation of half-life.

**4.S2 → Answer: (C)**
A is true (unit is $\text{s}^{-1}$ or $\text{min}^{-1}$, etc.).
R is false (rate = $k[A]^1$, so rate *is* dependent on concentration).

**4.S3 → Answer: (A)**
Both are true and R is the correct explanation. Rearranging the equation in R gives $\log[A]_t = \log[A]_0 - \frac{k}{2.303}t$, which explains the slope.

**4.S4 → Answer: (A)**
Both are true and R is the correct explanation. Because the pump is constant (zero order), it will eventually empty the tank (100% completion) in finite time ($t = [A]_0 / k$).

**4.S5 → Answer: (A)**
A is true (2 half-lives for 75%).
R is true and correctly explains A. After one half-life, 50% remains. After the second, 25% remains, meaning 75% is completed.

**4.S6 → Answer: (A)**
A is true: $t_{100\%} = 2 \times t_{50\%}$ for zero order.
R is true and correctly explains A: $t_{50\%} = \frac{[A]_0}{2k}$ and $t_{100\%} = \frac{[A]_0}{k} = 2 \times \frac{[A]_0}{2k}$.

**4.S7 → Answer: (B)**
A is true ($t_{1/2} = 0.693/k$, independent of $[A]_0$).
R is true (rate constant is a constant at a given temperature).
But R does not explain A — the independence arises from the integrated rate law where $[A]_0$ cancels out.

**4.S8 → Answer: (A)**
Both are true and R directly explains A. Rearranging gives $\log[A]_t = \log[A]_0 - \frac{k}{2.303}t$, which is $y = c + mx$ with slope $= -k/2.303$.

**4.S9 → Answer: (A)**
A is true: $[A]_t = [A]_0 - kt$, slope $= -k$.
R is true: zero order rate is constant ($d[A]/dt = -k$).
R correctly explains A because the constant rate leads to linear decrease.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Q4.M1 🟢**
The integrated rate law for a zero order reaction is:
(A) $k = \frac{2.303}{t} \log\left(\frac{a}{a-x}\right)$
(B) $x = kt$
(C) $k = \frac{1}{t} \left(\frac{1}{a-x} - \frac{1}{a}\right)$
(D) $k = \frac{0.693}{t_{1/2}}$

**Q4.M2 🟡**
If $a$ is the initial concentration of a substance which reacts according to zero order kinetics, and $k$ is the rate constant, the time for the reaction to go to completion is:
(A) $a/k$
(B) $2/ka$
(C) $a/2k$
(D) $2k/a$

**Q4.M3 🔴**
The half-life period of a first order chemical reaction is $6.93\text{ minutes}$. The time required for the completion of 99% of the chemical reaction will be ($\log 2 = 0.301$):
(A) $23.03\text{ minutes}$
(B) $46.06\text{ minutes}$
(C) $460.6\text{ minutes}$
(D) $230.3\text{ minutes}$

**Q4.M4 🟡**
In a first order reaction, the concentration of reactant decreases from $0.8\text{ M}$ to $0.4\text{ M}$ in $15\text{ minutes}$. The time taken for the concentration to change from $0.1\text{ M}$ to $0.025\text{ M}$ is:
(A) $7.5\text{ min}$
(B) $15\text{ min}$
(C) $30\text{ min}$
(D) $60\text{ min}$

**Q4.M5 🟡**
For a chemical reaction $A \rightarrow B$, the rate of the reaction is $2 \times 10^{-3}\text{ mol dm}^{-3}\text{s}^{-1}$, when the initial concentration is $0.05\text{ mol dm}^{-3}$. The rate is the same when the concentration is $0.01\text{ mol dm}^{-3}$. The reaction is of:
(A) Zero order
(B) First order
(C) Second order
(D) Fractional order

**Q4.M6 🟡**
For a first-order reaction, the time for $75\%$ completion is:
(A) $\frac{0.693}{k}$
(B) $\frac{1.386}{k}$
(C) $\frac{2.303}{k}$
(D) $\frac{0.346}{k}$

**Q4.M7 🟡**
A zero-order reaction has $k = 0.02\text{ M min}^{-1}$ and $[A]_0 = 0.5\text{ M}$. The time for $100\%$ completion is:
(A) $12.5\text{ min}$
(B) $25\text{ min}$
(C) $50\text{ min}$
(D) $2.5\text{ min}$

**Q4.M8 🔴**
If $n$ is the order of a reaction, $t_{1/2}$ is proportional to:
(A) $[A]_0^{1-n}$
(B) $[A]_0^{n-1}$
(C) $[A]_0^{n}$
(D) $[A]_0^{1/n}$

**Q4.M9 🔴**
A plot of $\log(\text{rate})$ vs $\log[A]$ gives a straight line with slope $= 2$ and intercept $= \log k$. The half-life for $[A]_0 = 0.5\text{ M}$ is:
(A) Depends on $[A]_0$
(B) $\frac{0.693}{k}$
(C) $\frac{1}{k \times 0.5}$
(D) $\frac{2}{k}$

<details>
<summary>💡 Full Solutions — MCQ Mastery (Samples)</summary>

**4.M1 → Answer: (B)**
For zero order, $[A]_0 - [A]_t = kt$. If $[A]_0 = a$ and $[A]_t = a - x$, then $a - (a - x) = kt \implies x = kt$.

**4.M2 → Answer: (A)**
For 100% completion, $[A]_t = 0$.
$[A]_0 - 0 = kt \implies t = [A]_0 / k = a/k$.

**4.M3 → Answer: (B)**
$k = \frac{0.693}{t_{1/2}} = \frac{0.693}{6.93} = 0.1\text{ min}^{-1}$.
For 99% completion, $[A]_t = 0.01 [A]_0$.
$t = \frac{2.303}{k} \log\left(\frac{100}{1}\right) = \frac{2.303}{0.1} \times 2 = 23.03 \times 2 = 46.06\text{ minutes}$.

**4.M4 → Answer: (C)**
$0.8\text{ M} \rightarrow 0.4\text{ M}$ is one half-life. So $t_{1/2} = 15\text{ minutes}$.
$0.1\text{ M} \rightarrow 0.05\text{ M} \rightarrow 0.025\text{ M}$ is two half-lives.
Total time = $2 \times 15 = 30\text{ minutes}$.

**4.M5 → Answer: (A)**
The rate is $2 \times 10^{-3}$ at $0.05\text{ M}$ and remains the exact same at $0.01\text{ M}$. Since the rate is independent of concentration, it is a Zero Order reaction.

**4.M6 → Answer: (B)**
$75\%$ done means $[A]_t = 0.25[A]_0$.
$t = \frac{2.303}{k} \log(4) = \frac{2.303 \times 0.602}{k} = \frac{1.386}{k}$.

**4.M7 → Answer: (B)**
$t_{100\%} = \frac{[A]_0}{k} = \frac{0.5}{0.02} = 25\text{ min}$.

**4.M8 → Answer: (A)**
$t_{1/2} \propto \frac{1}{[A]_0^{n-1}} = [A]_0^{1-n}$.

**4.M9 → Answer: (C)**
Rate $= k[A]^n \implies \log(\text{rate}) = \log k + n\log[A]$.
Slope $= n = 2$. **Second Order**.
$t_{1/2} = \frac{1}{k[A]_0} = \frac{1}{k \times 0.5}$.
</details>
