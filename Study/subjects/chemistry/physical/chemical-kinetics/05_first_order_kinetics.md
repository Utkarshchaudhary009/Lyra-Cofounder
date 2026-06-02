# Chapter 5: First Order Kinetics — Mastery<br>
## Part III — First Order Kinetics Deep Dive

---

## 🎯 Stage 1: The Core Idea

### The Scene

First-order kinetics rules the universe. Literally. From the radioactive decay of uranium in the earth's crust to the metabolism of medicine in your bloodstream, nature loves first-order processes.

Imagine a room with 100 bouncing ping-pong balls. Every minute, exactly 10% of the *remaining* balls fall through a trapdoor. 
- Minute 1: 10 fall (90 left).
- Minute 2: 9 fall (81 left).
- Minute 3: 8.1 fall... 

The number falling (the rate) is directly tied to the number remaining (the concentration). This is the hallmark of a **First Order Reaction**.

### Key Milestones in First Order Time

In first-order reactions, because the half-life ($t_{1/2}$) is constant and independent of concentration, we can use it as a powerful ruler to measure time.

| Milestone | Fraction Remaining | Percent Completed | Time in Half-lives | Memory Hook |
|-----------|--------------------|-------------------|--------------------|-------------|
| $1 \times t_{1/2}$ | 1/2 | 50% | $t_{50\%} = 1 \times t_{1/2}$ | "Halfway there" |
| $2 \times t_{1/2}$ | 1/4 | 75% | $t_{75\%} = 2 \times t_{1/2}$ | "Three-quarters done" |
| $3 \times t_{1/2}$ | 1/8 | 87.5% | $t_{87.5\%} = 3 \times t_{1/2}$ | "Seven-eighths gone" |
| $10 \times t_{1/2}$ | ~1/1000 | 99.9% | $t_{99.9\%} \approx 10 \times t_{1/2}$ | "Basically finished" |

> ⚠️ **Classic Trap:** Thinking that two half-lives equal 100% completion. In first order, $50\% + 50\%$ doesn't equal $100\%$. It's $50\%$ of the whole, then $50\%$ of what's left. It never truly hits 0!

---

## 🔬 Stage 2: The Formula Lab

### Formula 1: The Master Rate Equation

From Chapter 4, we know:
$$k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$$

Often, it's written in terms of initial amount $a$ and reacted amount $x$:
- Initial amount ($[A]_0$) = $a$
- Amount reacted at time $t$ = $x$
- Amount remaining ($[A]_t$) = $a - x$

$$k = \frac{2.303}{t} \log\left(\frac{a}{a-x}\right)$$

### Formula 2: Remaining Amount after $n$ Half-Lives

Since the amount halves every $t_{1/2}$:
After 1 half-life: $C_t = C_0 / 2$
After 2 half-lives: $C_t = C_0 / 4 = C_0 / 2^2$

**General Formula:**
$$C_t = \frac{C_0}{2^n}$$
Where $n = \frac{\text{Total Time}}{\text{Half-life}} = \frac{t}{t_{1/2}}$

### Formula 3: Radioactive Decay

Radioactivity is *always* first order. The formulas are identical, just with different symbols:
- $k \rightarrow \lambda$ (Decay constant)
- $[A]_0 \rightarrow N_0$ (Initial number of nuclei)
- $[A]_t \rightarrow N_t$ (Number of nuclei at time $t$)

$$\lambda = \frac{2.303}{t} \log\left(\frac{N_0}{N_t}\right)$$
$$t_{1/2} = \frac{0.693}{\lambda}$$

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: The Fractional Completion Shortcuts

**The Pattern:** Proving or using the relationship between different completion percentages.

#### Solved Example 5.1
**Q:** Prove that the time required for 99.9% completion of a first order reaction is 10 times its half-life.<br> 🟡

**Solution:**
```
Step 1: Express t_99.9%
Let initial amount [A]_0 = 100
Amount reacted x = 99.9
Amount remaining [A]_t = 100 - 99.9 = 0.1
t_99.9% = (2.303 / k) * log(100 / 0.1)
t_99.9% = (2.303 / k) * log(1000) = (2.303 / k) * 3
t_99.9% = 6.909 / k

Step 2: Express t_1/2
t_1/2 = 0.693 / k

Step 3: Compare
t_99.9% / t_1/2 = (6.909 / k) / (0.693 / k) = 6.909 / 0.693 ≈ 9.96 ≈ 10
Therefore, t_99.9% ≈ 10 * t_1/2
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 5.1a | Show that for a first order reaction, $t_{75\%} = 2 \times t_{50\%}$. | 🟢 |
| 5.1b | Show that for a first order reaction, $t_{87.5\%} = 3 \times t_{50\%}$. | 🟡 |
| 5.1c | The time for 75% completion of a 1st order reaction is 20 minutes. What is the time for 50% completion? | 🟢 |
| 5.1d | What fraction of the initial concentration remains after 5 half-lives of a first-order reaction? | 🟢 |
| 5.1e | A first-order reaction is 87.5% complete in 90 minutes. Find its half-life. | 🟢 |
| 5.1f | For a first-order reaction, $t_{90\%} = 69$ minutes. Calculate $t_{50\%}$ (Given $\log 10 = 1$, $\log 2 = 0.3010$). | 🟡 |
| 5.1g | The time required for a first-order reaction to go from 25% to 75% completion is 40 minutes. Find the half-life. (Given $\log 3 = 0.4771$) | 🟡 |
| 5.1h | Show that for a first-order reaction, $t_{99.99\%} \approx 13.29 \times t_{50\%}$. | 🔴 |
| 5.1i | The half-life of a first-order reaction is 10 minutes. Verify that $t_{99.9\%} = 10 \times t_{1/2}$ by direct calculation. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**5.1a:**
$t_{75\%} = \frac{2.303}{k} \log\left(\frac{100}{25}\right) = \frac{2.303}{k} \log(4) = \frac{2.303}{k} \times 2\log(2) = 2 \times \frac{0.693}{k} = 2 \times t_{50\%}$.

**5.1b:**
$t_{87.5\%} = \frac{2.303}{k} \log\left(\frac{100}{100-87.5}\right) = \frac{2.303}{k} \log\left(\frac{100}{12.5}\right) = \frac{2.303}{k} \log(8) = \frac{2.303}{k} \times 3\log(2) = 3 \times t_{50\%}$.

**5.1c:**
Since $t_{75\%} = 2 \times t_{50\%}$, we have $20 = 2 \times t_{50\%} \implies t_{50\%} = 10\text{ minutes}$.

**5.1d:**
Fraction remaining $= 1/2^5 = 1/32$.

**5.1e:**
87.5% complete $\implies$ 12.5% left $= 1/8 = 1/2^3 \implies n = 3$.
$t_{1/2} = 90/3 = 30\text{ minutes}$.

**5.1f:**
$\frac{t_{90\%}}{t_{50\%}} = \frac{\log(100/10)}{\log(2)} = \frac{\log(10)}{\log(2)} = \frac{1}{0.3010} = 3.322$.
$t_{50\%} = 69 / 3.322 = 20.77\text{ minutes}$.

**5.1g:**
At 25% completion, 75% remains. At 75% completion, 25% remains.
$k = \frac{2.303}{40}\log\left(\frac{75}{25}\right) = \frac{2.303}{40}\log(3) = \frac{2.303 \times 0.4771}{40} = 0.02746\text{ min}^{-1}$.
$t_{1/2} = 0.693 / 0.02746 = 25.24\text{ minutes}$.

**5.1h:**
$t_{99.99\%} = \frac{2.303}{k}\log\left(\frac{100}{0.01}\right) = \frac{2.303}{k}\log(10^4) = \frac{2.303}{k} \times 4 = \frac{9.212}{k}$.
$t_{50\%} = 0.693/k$.
Ratio $= \frac{9.212/k}{0.693/k} = 13.29$.

**5.1i:**
$t_{99.9\%} = \frac{2.303}{k}\log\left(\frac{100}{0.1}\right) = \frac{2.303}{k} \times 3 = \frac{6.909}{k}$.
$t_{1/2} = 0.693/k = 10 \implies k = 0.0693\text{ min}^{-1}$.
$t_{99.9\%} = 6.909/0.0693 = 99.7 \approx 100\text{ min} = 10 \times 10 = 10 \times t_{1/2}$. Verified.
</details>

---

### Type 2: The "n Half-lives" Rule

**The Pattern:** You are given an initial amount and asked for the amount remaining after a specific time that is a multiple of the half-life.

#### Solved Example 5.2
**Q:** A radioactive isotope has a half-life of 5 years. If the initial mass is 64 grams, how much will be left after 20 years?<br> 🟢

**Solution:**
```
Total time t = 20 years
Half-life t_1/2 = 5 years
Number of half-lives (n) = t / t_1/2 = 20 / 5 = 4

Amount remaining = Initial / 2^n
C_t = 64 / 2^4 = 64 / 16 = 4 grams
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 5.2a | A 1st order reaction has a half life of $10\text{ s}$. How much of $10\text{ M}$ reactant remains after $30\text{ s}$? | 🟢 |
| 5.2b | What fraction of a radioactive substance remains after 5 half-lives? | 🟢 |
| 5.2c | A substance decomposes by first order. After $24\text{ hours}$, 1/16th of the initial amount is left. Find the half-life. | 🟡 |
| 5.2d | The half-life of a radioactive isotope is 6 hours. What mass remains from a 48 g sample after 24 hours? | 🟢 |
| 5.2e | A first-order reaction is 75% complete in 40 minutes. What is its half-life? | 🟢 |
| 5.2f | A reactant decomposes by first-order kinetics. If the initial concentration is 1.6 M and after 32 minutes the concentration is 0.1 M, find the half-life. | 🟡 |
| 5.2g | After 6 half-lives, what fraction of the original sample of a first-order reaction remains? | 🟡 |
| 5.2h | A radioactive sample has a half-life of 2 hours. Starting with 128 g, what amount remains undecayed after 10 hours? | 🔴 |
| 5.2i | The concentration of a first-order reactant falls from 0.64 M to 0.01 M in 54 minutes. Determine the half-life. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**5.2a:**
$n = 30 / 10 = 3$. Remaining $= 10 / 2^3 = 10 / 8 = 1.25\text{ M}$.

**5.2b:**
Fraction remaining $= 1 / 2^5 = 1/32$.

**5.2c:**
Remaining $= 1/16 = 1/2^4 \implies n = 4$ half-lives.
Total time $= 4 \times t_{1/2} = 24 \implies t_{1/2} = 6\text{ hours}$.

**5.2d:**
$n = 24 / 6 = 4$. Remaining $= 48 / 2^4 = 48 / 16 = 3\text{ g}$.

**5.2e:**
75% complete $\implies$ 25% left $= 1/4 = 1/2^2 \implies n = 2$.
$t_{1/2} = 40 / 2 = 20\text{ minutes}$.

**5.2f:**
$0.1 / 1.6 = 0.0625 = 1/16 = 1/2^4 \implies n = 4$.
$t_{1/2} = 32 / 4 = 8\text{ minutes}$.

**5.2g:**
Fraction remaining $= 1/2^6 = 1/64$.

**5.2h:**
$n = 10 / 2 = 5$. Remaining $= 128 / 2^5 = 128 / 32 = 4\text{ g}$.

**5.2i:**
$0.01 / 0.64 = 0.015625 = 1/64 = 1/2^6 \implies n = 6$.
$t_{1/2} = 54 / 6 = 9\text{ minutes}$.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 5.M1 | The half-life of a radioactive element is 100 days. How long will it take for 99.9% of the sample to decay? | T1 | 🟡 |
| 5.M2 | A first order reaction takes 10 minutes for 20% decomposition. What fraction of the reactant will remain after 30 minutes? | T1 + T2 | 🔴 |
| 5.M3 | The half-life of $^{238}\text{U}$ is $4.5 \times 10^9$ years. What fraction of the original sample remains after $1.35 \times 10^{10}$ years? | T2 | 🟡 |
| 5.M4 | A first-order reaction has a rate constant of $0.0231\text{ min}^{-1}$. Calculate the time for 75% completion. | T1 | 🟡 |
| 5.M5 | The half-life of a first-order reaction is 20 minutes. What time is required for 90% completion? (Given $\log 10 = 1$, $\log 2 = 0.3010$) | T1 + T2 | 🟡 |
| 5.M6 | A first-order reaction is 40% complete in 30 minutes. Find the time for 80% completion. | T1 | 🔴 |
| 5.M7 | A substance decays by first-order kinetics with $k = 5 \times 10^{-4}\text{ s}^{-1}$. Find the time after which 90% of the sample has decayed. | T1 | 🔴 |
| 5.M8 | For a first-order reaction, the concentration decreases from 0.8 M to 0.2 M in 40 minutes. Find the rate constant and the time for 99% completion. | T1 + T2 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**5.M1:**
We know $t_{99.9\%} = 10 \times t_{1/2}$.
Therefore, $t = 10 \times 100 = 1000\text{ days}$.

**5.M2:**
This is tricky. Don't use half-lives if it's not a clean multiple.
Use the exponential form or basic rate law.
$k = \frac{2.303}{10} \log\left(\frac{100}{80}\right) = \frac{2.303}{10} \log(1.25) \approx \frac{2.303 \times 0.0969}{10} \approx 0.0223\text{ min}^{-1}$.
After 30 mins:
$k = \frac{2.303}{30} \log\left(\frac{1}{f}\right)$ where $f$ is fraction remaining.
$0.0223 = \frac{2.303}{30} \log(1/f) \implies \log(1/f) = 0.290 \implies 1/f = \text{antilog}(0.290) \approx 1.95 \approx 2$.
Actually, since it's exactly 3 intervals of 10 mins, the fraction remaining after each 10 min is $0.8$.
After 30 min (3 intervals): Remaining $= (0.8)^3 \times \text{Initial} = 0.512 \times \text{Initial}$.
So fraction remaining is $0.512$.

**5.M3:**
$n = 1.35 \times 10^{10} / 4.5 \times 10^9 = 3$.
Fraction remaining $= 1/2^3 = 1/8$.

**5.M4:**
$t_{1/2} = 0.693 / 0.0231 = 30\text{ minutes}$.
$t_{75\%} = 2 \times t_{1/2} = 2 \times 30 = 60\text{ minutes}$.

**5.M5:**
$\frac{t_{90\%}}{t_{50\%}} = \frac{\log(10)}{\log(2)} = \frac{1}{0.3010} = 3.322$.
$t_{90\%} = 3.322 \times 20 = 66.44\text{ minutes}$.

**5.M6:**
$k = \frac{2.303}{30}\log\left(\frac{100}{60}\right) = \frac{2.303}{30}\log\left(\frac{5}{3}\right) = \frac{2.303}{30} \times 0.2218 = 0.01703\text{ min}^{-1}$.
$t_{80\%} = \frac{2.303}{0.01703}\log\left(\frac{100}{20}\right) = 135.2 \times \log(5) = 135.2 \times 0.699 = 94.5\text{ minutes}$.

**5.M7:**
$t = \frac{2.303}{5 \times 10^{-4}}\log\left(\frac{100}{10}\right) = \frac{2.303}{5 \times 10^{-4}} \times 1 = 4606\text{ s}$.

**5.M8:**
$k = \frac{2.303}{40}\log\left(\frac{0.8}{0.2}\right) = \frac{2.303}{40}\log(4) = \frac{2.303 \times 0.602}{40} = 0.03466\text{ min}^{-1}$.
$t_{99\%} = \frac{2.303}{0.03466}\log(100) = \frac{2.303}{0.03466} \times 2 = 132.9\text{ minutes}$.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 5.B1 | A first-order reaction has a rate constant of $1.15 \times 10^{-3}\text{ s}^{-1}$. How long will $5\text{g}$ of this reactant take to reduce to $3\text{g}$? | 🟡 |
| 5.B2 | The rate constant for a first order reaction is $60\text{ s}^{-1}$. How much time will it take to reduce the initial concentration of the reactant to its 1/16th value? | 🟢 |
| 5.B3 | Show that in a first order reaction, time required for completion of 99.9% is 10 times of half-life of the reaction. ⭐ | 🟡 |
| 5.B4 | A first-order reaction has a rate constant of $0.001\text{ s}^{-1}$. Calculate its half-life. | 🟢 |
| 5.B5 | Show that in a first order reaction, the time required for 99% completion is double the time for 90% completion. ⭐ | 🟡 |
| 5.B6 | A first-order reaction is 90% complete in 50 minutes. Calculate the rate constant. | 🟡 |
| 5.B7 | The initial concentration of a reactant in a first-order reaction is 0.4 M. After 2 hours, the concentration is 0.05 M. Find its half-life. | 🟡 |
| 5.B8 | A first-order reaction has a rate constant of $2.5 \times 10^{-3}\text{ s}^{-1}$. What percentage of the reactant remains after 300 seconds? | 🔴 |
| 5.B9 | The half-life of a radioactive element is 1600 years. After how many years will 93.75% of the sample disintegrate? | 🔴 |
| 5.B10 | For a first-order reaction, derive $t_{1/2} = 0.693/k$ and hence find the time required for 99.9% completion in terms of $k$. ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**5.B1:**
$t = \frac{2.303}{k} \log\frac{[A]_0}{[A]_t} = \frac{2.303}{1.15 \times 10^{-3}} \log\frac{5}{3} = 2000 \times (0.699 - 0.477) = 2000 \times 0.222 = 444\text{ s}$.

**5.B2:**
$1/16$ means 4 half-lives.
$t_{1/2} = 0.693 / 60 = 0.01155\text{ s}$.
Total time $= 4 \times 0.01155 = 0.0462\text{ s}$.

**5.B3:**
See Type 1, Solved Example 5.1.

**5.B4:**
$t_{1/2} = 0.693 / k = 0.693 / 0.001 = 693\text{ s}$.

**5.B5:**
$t_{99\%} = \frac{2.303}{k}\log\left(\frac{100}{1}\right) = \frac{2.303}{k} \times 2$.
$t_{90\%} = \frac{2.303}{k}\log\left(\frac{100}{10}\right) = \frac{2.303}{k} \times 1$.
$\therefore t_{99\%} = 2 \times t_{90\%}$.

**5.B6:**
$k = \frac{2.303}{50}\log\left(\frac{100}{10}\right) = \frac{2.303}{50} \times 1 = 0.04606\text{ min}^{-1}$.

**5.B7:**
$0.05 / 0.4 = 0.125 = 1/8 = 1/2^3 \implies n = 3$.
2 hours $= 120$ minutes.
$t_{1/2} = 120 / 3 = 40\text{ minutes}$.

**5.B8:**
$k = \frac{2.303}{300}\log\left(\frac{100}{x}\right)$, where $x$ is the percentage remaining.
$2.5 \times 10^{-3} = \frac{2.303}{300}\log(100/x)$.
$\log(100/x) = \frac{2.5 \times 10^{-3} \times 300}{2.303} = 0.3256$.
$100/x = \text{antilog}(0.3256) \approx 2.116$.
$x = 100 / 2.116 = 47.26\%$.

**5.B9:**
93.75% disintegrated $\implies$ 6.25% left $= 1/16 = 1/2^4 \implies n = 4$.
$t = 4 \times 1600 = 6400\text{ years}$.

**5.B10:**
$t_{1/2}$ is time when $[A]_t = [A]_0/2$.
$k = \frac{2.303}{t_{1/2}}\log\left(\frac{[A]_0}{[A]_0/2}\right) = \frac{2.303}{t_{1/2}}\log(2) = \frac{2.303 \times 0.3010}{t_{1/2}} = \frac{0.693}{t_{1/2}}$.
$\therefore t_{1/2} = 0.693/k$.
$t_{99.9\%} = \frac{2.303}{k}\log\left(\frac{100}{0.1}\right) = \frac{2.303}{k} \times 3 = 6.909/k = 10 \times 0.693/k = 10 \times t_{1/2}$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q5.J1 🟡**
The half-life of a radioactive isotope is 3 hours. If the initial mass is 256 g, the mass remaining after 18 hours is:
(A) 4 g
(B) 8 g
(C) 16 g
(D) 32 g

**Q5.J2 🔴 ⭐**
A first order reaction takes 40 min for 30% decomposition. Calculate $t_{1/2}$. (Given $\log 7 = 0.845$)
(A) 77.7 min
(B) 27.2 min
(C) 55.3 min
(D) 60 min

**Q5.J3 🟢**
The half-life of a first-order reaction is 10 minutes. The time required for 75% completion is:
(A) 10 min
(B) 20 min
(C) 30 min
(D) 40 min

**Q5.J4 🟡**
For a first-order reaction, the rate constant is $0.0693\text{ min}^{-1}$. The time required for the concentration to decrease to half its initial value is:
(A) 10 min
(B) 20 min
(C) 15 min
(D) 5 min

**Q5.J5 🟡**
A first-order reaction is 20% complete in 10 minutes. The half-life period is: (Given $\log 1.25 = 0.0969$)
(A) 31.1 min
(B) 62.2 min
(C) 15.5 min
(D) 45.3 min

**Q5.J6 🟡**
If the concentration of a first-order reactant falls from 0.8 M to 0.2 M in 60 minutes, the rate constant is:
(A) $0.0231\text{ min}^{-1}$
(B) $0.0462\text{ min}^{-1}$
(C) $0.01155\text{ min}^{-1}$
(D) $0.0693\text{ min}^{-1}$

**Q5.J7 🔴**
The time required for 90% completion of a first-order reaction is proportional to its:
(A) Half-life
(B) Square of half-life
(C) Reciprocal of half-life
(D) Square root of half-life

**Q5.J8 🔴**
A radioactive sample has an initial activity of 800 dps. After 30 days, the activity becomes 100 dps. The half-life of the sample is:
(A) 5 days
(B) 10 days
(C) 15 days
(D) 20 days

**Q5.J9 🔴**
For a first-order reaction, which of the following statements is INCORRECT?
(A) The half-life is independent of the initial concentration
(B) The rate constant has units of $\text{time}^{-1}$
(C) The time for 75% completion is twice the half-life
(D) The plot of $\log[A]$ vs $t$ is a straight line with slope $= k$

**Q5.J10 🔴**
The half-life of $^{60}\text{Co}$ is 5.27 years. The time taken for the activity to fall to 6.25% of its original value is:
(A) 10.54 years
(B) 15.81 years
(C) 21.08 years
(D) 5.27 years

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**5.J1 → Answer: (A)**
$n = 18 / 3 = 6$ half-lives.
Remaining $= 256 / 2^6 = 256 / 64 = 4\text{ g}$.

**5.J2 → Answer: (A)**
$k = \frac{2.303}{40} \log\left(\frac{100}{70}\right) = \frac{2.303}{40} \times (1 - 0.845) = \frac{2.303 \times 0.155}{40} = 0.00892\text{ min}^{-1}$.
$t_{1/2} = 0.693 / 0.00892 = 77.7\text{ min}$.

**5.J3 → Answer: (B)**
75% completion $\implies$ 25% left $= 1/4 = 1/2^2 \implies n = 2$.
$t = 2 \times 10 = 20\text{ min}$.

**5.J4 → Answer: (A)**
$t_{1/2} = 0.693 / k = 0.693 / 0.0693 = 10\text{ min}$.

**5.J5 → Answer: (A)**
$k = \frac{2.303}{10} \log\left(\frac{100}{80}\right) = \frac{2.303}{10} \times \log(1.25) = \frac{2.303 \times 0.0969}{10} = 0.02232\text{ min}^{-1}$.
$t_{1/2} = 0.693 / 0.02232 = 31.1\text{ min}$.

**5.J6 → Answer: (A)**
$k = \frac{2.303}{60} \log\left(\frac{0.8}{0.2}\right) = \frac{2.303}{60} \log(4) = \frac{2.303 \times 0.602}{60} = 0.0231\text{ min}^{-1}$.

**5.J7 → Answer: (A)**
$t_{90\%} = \frac{2.303}{k} \log(10) = \frac{2.303}{k}$.
Since $t_{1/2} = 0.693/k$, we have $k = 0.693/t_{1/2}$.
$\therefore t_{90\%} = \frac{2.303}{0.693/t_{1/2}} = 3.322 \times t_{1/2}$.
Thus $t_{90\%}$ is directly proportional to $t_{1/2}$.

**5.J8 → Answer: (B)**
$100 / 800 = 1/8 = 1/2^3 \implies n = 3$.
$t_{1/2} = 30 / 3 = 10\text{ days}$.

**5.J9 → Answer: (D)**
The integrated rate law is $\log[A] = \log[A]_0 - kt/2.303$. The slope of $\log[A]$ vs $t$ is $-k/2.303$, not $k$. All other statements are correct.

**5.J10 → Answer: (C)**
6.25% $= 1/16 = 1/2^4 \implies n = 4$.
$t = 4 \times 5.27 = 21.08\text{ years}$.
</details>

---

## 🧠 Stage 7: Assertion-Reasoning

| # | Question | Difficulty |
|---|----------|------------|
| 5.S1 | **Assertion (A):** The half-life of a radioactive substance is independent of its initial mass.<br>**Reason (R):** Radioactive decay follows first-order kinetics. | 🟢 |
| 5.S2 | **Assertion (A):** A first-order reaction can never reach 100% completion in a finite time.<br>**Reason (R):** The rate of reaction decreases exponentially with time. | 🟡 |
| 5.S3 | **Assertion (A):** The unit of rate constant for a first-order reaction is $\text{s}^{-1}$.<br>**Reason (R):** For a first-order reaction, $\text{rate} = k[A]^1$, so $k = \text{rate}/[A]$ which has units $\text{(concentration time}^{-1})/\text{concentration} = \text{time}^{-1}$. | 🟢 |
| 5.S4 | **Assertion (A):** A plot of $\log[A]$ vs time gives a straight line for a first-order reaction.<br>**Reason (R):** The integrated rate law is $\log[A] = \log[A]_0 - kt/2.303$, which is of the form $y = mx + c$. | 🟢 |
| 5.S5 | **Assertion (A):** The half-life of a first-order reaction increases with an increase in temperature.<br>**Reason (R):** The rate constant increases with temperature, and $t_{1/2} = 0.693/k$. | 🟡 |
| 5.S6 | **Assertion (A):** For a first-order reaction, $t_{99.9\%} = 10 \times t_{50\%}$.<br>**Reason (R):** The half-life of a first-order reaction is independent of the initial concentration. | 🟡 |
| 5.S7 | **Assertion (A):** Radioactive decay follows first-order kinetics.<br>**Reason (R):** The rate of radioactive decay is directly proportional to the number of undecayed nuclei present. | 🟡 |
| 5.S8 | **Assertion (A):** The concentration of a first-order reactant after 3 half-lives is $1/6$th of the initial concentration.<br>**Reason (R):** After $n$ half-lives, the concentration remaining is $[A]_0/2^n$. | 🔴 |
| 5.S9 | **Assertion (A):** The time required for 99% completion of a first-order reaction is twice the time required for 90% completion.<br>**Reason (R):** $t_{99\%}/t_{90\%} = \log(100)/\log(10) = 2/1 = 2$. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**5.S1 → Answer: (A)**
Both are true and R is the correct explanation. For all first-order reactions, $t_{1/2} = 0.693/k$, which has no concentration term.

**5.S2 → Answer: (A)**
Both are true and R is the correct explanation. Because rate $\propto$ concentration, as concentration approaches zero, rate approaches zero, making the curve an asymptote to the x-axis.

**5.S3 → Answer: (A)**
Both true and R correctly explains A. For a first-order reaction, $k$ always has units of $\text{time}^{-1}$ regardless of the concentration units used.

**5.S4 → Answer: (A)**
Both true and R correctly explains A. The equation $\log[A] = \log[A]_0 - kt/2.303$ is linear in $t$ with slope $-k/2.303$.

**5.S5 → Answer: (D)**
A is false. As temperature increases, $k$ increases, so $t_{1/2} = 0.693/k$ decreases. R is true but does not support A.

**5.S6 → Answer: (B)**
Both A and R are true, but R is not the correct explanation. The relationship $t_{99.9\%} = 10 \times t_{50\%}$ is derived mathematically from the integrated rate law, not from the independence of half-life from concentration.

**5.S7 → Answer: (A)**
Both true and R correctly explains A. The rate of decay $= -\frac{dN}{dt} = \lambda N$, which is directly proportional to $N$, confirming first-order kinetics.

**5.S8 → Answer: (D)**
A is false. After 3 half-lives, concentration $= [A]_0/2^3 = [A]_0/8$, not $[A]_0/6$. R is true.

**5.S9 → Answer: (A)**
Both true and R correctly explains A. $t_{99\%} = \frac{2.303}{k}\log(100)$ and $t_{90\%} = \frac{2.303}{k}\log(10)$, so the ratio is $\log(100)/\log(10) = 2/1 = 2$.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Q5.M1 🟢**
For a first order reaction, the ratio of times for 99.9% completion to 50% completion is:
(A) 1
(B) 2
(C) 10
(D) 100

**Q5.M2 🟡**
If a first order reaction has a half-life of 15 minutes, how much time is required to complete 87.5%?
(A) 15 min
(B) 30 min
(C) 45 min
(D) 60 min

**Q5.M3 🟢**
The decay constant ($\lambda$) and half-life ($t_{1/2}$) of a radioactive element are related as:
(A) $\lambda = 0.693/t_{1/2}$
(B) $\lambda = t_{1/2}/0.693$
(C) $\lambda = 2.303/t_{1/2}$
(D) $\lambda = t_{1/2}/2.303$

**Q5.M4 🟢**
A first-order reaction has $k = 0.005\text{ s}^{-1}$. The time required to reduce the concentration to $1/e$ of its initial value is:
(A) 200 s
(B) 0.005 s
(C) 20 s
(D) 0.693 s

**Q5.M5 🟡**
For a first-order reaction, which of the following graphs is correct?
(A) $\log[A]$ vs $t$ — straight line with positive slope
(B) $\log[A]$ vs $t$ — straight line with negative slope
(C) $[A]$ vs $t$ — straight line with negative slope
(D) $\log[A]$ vs $1/t$ — straight line

**Q5.M6 🟡**
The slope of the straight line obtained by plotting $\log([A]_0/[A]_t)$ vs time for a first-order reaction is:
(A) $k$
(B) $k/2.303$
(C) $-k/2.303$
(D) $-k$

**Q5.M7 🔴**
A first-order reaction is 50% complete in 69.3 minutes. The time required for 90% completion is:
(A) 230.3 min
(B) 69.3 min
(C) 138.6 min
(D) 34.65 min

**Q5.M8 🔴**
A radioactive element has a half-life of 8 days. After 24 days, the fraction of the original sample left undecayed is:
(A) $1/2$
(B) $1/4$
(C) $1/8$
(D) $1/16$

**Q5.M9 🔴**
The time required for 99.9% completion of a first-order reaction with $t_{1/2} = 10$ min is:
(A) 20 min
(B) 100 min
(C) 50 min
(D) 10 min

<details>
<summary>💡 Full Solutions — MCQ Mastery (Samples)</summary>

**5.M1 → Answer: (C)**
$t_{99.9\%} \approx 10 \times t_{50\%}$. Ratio is 10.

**5.M2 → Answer: (C)**
87.5% completion means 12.5% (1/8th) is left.
$1/8 = 1/2^3$, so 3 half-lives have passed.
$3 \times 15 = 45\text{ minutes}$.

**5.M3 → Answer: (A)**
For a first-order reaction, $\lambda = 0.693/t_{1/2}$.

**5.M4 → Answer: (A)**
$\ln([A]_0/[A]_t) = kt$. For $[A]_t = [A]_0/e$, $\ln(e) = 1 = kt$.
$t = 1/k = 1/0.005 = 200\text{ s}$.

**5.M5 → Answer: (B)**
$\log[A] = \log[A]_0 - kt/2.303$, which is of the form $y = c + mx$ with negative slope $-k/2.303$.

**5.M6 → Answer: (B)**
$\log([A]_0/[A]_t) = kt/2.303$, which is a straight line through origin with slope $k/2.303$.

**5.M7 → Answer: (A)**
$k = 0.693/69.3 = 0.01\text{ min}^{-1}$.
$t_{90\%} = \frac{2.303}{0.01}\log(10) = 230.3 \times 1 = 230.3\text{ min}$.

**5.M8 → Answer: (C)**
$n = 24/8 = 3$. Fraction remaining $= 1/2^3 = 1/8$.

**5.M9 → Answer: (B)**
$t_{99.9\%} = 10 \times t_{1/2} = 10 \times 10 = 100\text{ min}$.
</details>
