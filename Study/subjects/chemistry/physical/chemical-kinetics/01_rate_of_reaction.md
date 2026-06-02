# Chapter 1: Rate of Chemical Reaction

## Part I — Foundations

***

## 🎯 Stage 1: The Core Idea

### The Scene

Imagine you are driving a car from your home to school. If the school is $10 \text{ km}$ away and it takes you $30 \text{ minutes}$, your average speed is distance divided by time. At any exact moment—say, when you cross a traffic light—your speedometer might show $45 \text{ km/hr}$. That's your instantaneous speed.

Chemical reactions are just like cars driving towards their destination (products). Instead of covering "distance", they consume "concentration".

> The **Rate of Reaction (ROR)** is the change in concentration of a reactant or a product per unit time.

### Average vs. Instantaneous Rate

| Type                                 | Analogy                                  | Chemistry Definition                                                            |
| ------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------- |
| **Average Rate** ($r\_{avg}$)        | Total distance / Total time              | $\frac{\Delta\[\text{Concentration}]}{\Delta t}$ over a specific time interval. |
| **Instantaneous Rate** ($r\_{inst}$) | Speedometer reading at a specific second | $\frac{d\[\text{Concentration}]}{dt}$ at a specific instant (slope of tangent). |

*Note: For a very small time interval ($\Delta t \rightarrow 0$), the average rate becomes the instantaneous rate.*

### The Golden Rule of Rates: Stoichiometry Matters

Suppose you are making a sandwich:
$$2 \text{ Bread} + 1 \text{ Cheese} \rightarrow 1 \text{ Sandwich}$$

If you make $1 \text{ Sandwich}$ per minute, you are *consuming* Bread at $2 \text{ slices}$ per minute, and Cheese at $1 \text{ slice}$ per minute.
The rates of disappearance of individual reactants are **not** always equal! They depend on the recipe (stoichiometry).

To define a single, universal "Rate of Reaction" that everyone can agree on, we must divide the rate of change of each substance by its **stoichiometric coefficient**.

***

## 🔬 Stage 2: The Formula Lab

### Formula 1: Rate of Disappearance and Appearance

For a general reaction: $aA + bB \rightarrow cC + dD$

- **Rate of Disappearance of A** = $-\frac{d\[A]}{dt}$ (Reactants decrease, so we add a minus sign to make the rate positive)
- **Rate of Appearance of C** = $+\frac{d\[C]}{dt}$ (Products increase)

> ⚠️ **Trap Alert:** The rate of appearance/disappearance of a specific substance *never* includes the stoichiometric coefficient in its definition.

### Formula 2: The Overall Rate of Reaction (ROR)

To find the unique rate of the entire reaction, divide the rate of each species by its coefficient:

$$\text{ROR} = -\frac{1}{a}\frac{d\[A]}{dt} = -\frac{1}{b}\frac{d\[B]}{dt} = +\frac{1}{c}\frac{d\[C]}{dt} = +\frac{1}{d}\frac{d\[D]}{dt}$$

### Formula 3: Units of Rate

$$\text{Rate} = \frac{\text{Concentration}}{\text{Time}} = \frac{\text{mol L}^{-1}}{\text{s}} = \text{mol L}^{-1} \text{s}^{-1} \text{ (or M s}^{-1})$$
*(If reactants are gases, rate can be in $\text{atm s}^{-1}$)*

***

## 🧱 Stage 3: Type-wise Mastery

***

### Type 1: Writing the Rate Expression

**The Pattern:** You are given a balanced chemical equation. You must write the equality relating the rates of all species.

#### Solved Example 1.1

**Q:** Write the rate expression for the reaction: $\text{N}\_2(g) + 3\text{H}\_2(g) \rightarrow 2\text{NH}\_3(g)$. 🟢

**Solution:**

```
1. Identify coefficients: N2 = 1, H2 = 3, NH3 = 2.
2. Reactants get a (-) sign, Products get a (+) sign.
3. Divide by coefficients.

Answer:
ROR = - d[N2]/dt = - (1/3) d[H2]/dt = + (1/2) d[NH3]/dt
```

#### Practice Questions — Type 1

| #    | Question                                                                                                                                                                 | Difficulty |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| 1.1a | Write the rate expression for: $2\text{HI}(g) \rightarrow \text{H}\_2(g) + \text{I}\_2(g)$                                                                               | 🟢         |
| 1.1b | Write the rate expression for: $5\text{Br}^- + \text{BrO}\_3^- + 6\text{H}^+ \rightarrow 3\text{Br}\_2 + 3\text{H}\_2\text{O}$                                           | 🟡         |
| 1.1c | For a reaction, the rate expression is: ROR = $-\frac{1}{2}\frac{d\[A]}{dt} = -\frac{d\[B]}{dt} = +\frac{1}{3}\frac{d\[C]}{dt}$. What is the balanced chemical equation? | 🟡         |
| 1.1d | Write the rate expression for: $4\text{NH}\_3(g) + 5\text{O}\_2(g) \rightarrow 4\text{NO}(g) + 6\text{H}\_2\text{O}(g)$                                                                                           | 🟢         |
| 1.1e | For a reaction, the rate expression is: $-\frac{d\[A]}{dt} = -\frac{1}{3}\frac{d\[B]}{dt} = +\frac{1}{2}\frac{d\[C]}{dt}$. Find the balanced chemical equation.                                                       | 🟡         |
| 1.1f | Write the rate expression for: $2\text{Fe}^{3+}(aq) + \text{Sn}^{2+}(aq) \rightarrow 2\text{Fe}^{2+}(aq) + \text{Sn}^{4+}(aq)$                                                                                     | 🟡         |
| 1.1g | Write the rate expression for: $2\text{KClO}\_3(s) \rightarrow 2\text{KCl}(s) + 3\text{O}\_2(g)$                                                                                                                    | 🔴         |
| 1.1h | For a reaction: $-\frac{1}{4}\frac{d\[X]}{dt} = -\frac{1}{5}\frac{d\[Y]}{dt} = +\frac{1}{6}\frac{d\[Z]}{dt}$. Find the balanced equation and the species with the fastest rate of change.                          | 🔴         |
| 1.1i | Write the rate expression for: $2\text{MnO}\_4^- + 5\text{C}\_2\text{O}\_4^{2-} + 16\text{H}^+ \rightarrow 2\text{Mn}^{2+} + 10\text{CO}\_2 + 8\text{H}\_2\text{O}$                                                   | 🔴         |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**1.1a:**

- Reactant: HI (coeff 2)
- Products: H2 (coeff 1), I2 (coeff 1)
- **Answer: ROR = $-\frac{1}{2}\frac{d\[\text{HI}]}{dt} = +\frac{d\[\text{H}\_2]}{dt} = +\frac{d\[\text{I}\_2]}{dt}$**

**1.1b:**

- **Answer: ROR = $-\frac{1}{5}\frac{d\[\text{Br}^-]}{dt} = -\frac{d\[\text{BrO}\_3^-]}{dt} = -\frac{1}{6}\frac{d\[\text{H}^+]}{dt} = +\frac{1}{3}\frac{d\[\text{Br}\_2]}{dt} = +\frac{1}{3}\frac{d\[\text{H}\_2\text{O}]}{dt}$**

**1.1c:**

- Reactants have negative signs: A (coeff 2), B (coeff 1).
- Products have positive signs: C (coeff 3).
- **Answer: $2A + B \rightarrow 3C$**

**1.1d:**

- Coefficients: NH3 = 4, O2 = 5, NO = 4, H2O = 6.
- Reactants: NH3, O2. Products: NO, H2O.
- **Answer: ROR = $-\frac{1}{4}\frac{d\[\text{NH}\_3]}{dt} = -\frac{1}{5}\frac{d\[\text{O}\_2]}{dt} = +\frac{1}{4}\frac{d\[\text{NO}]}{dt} = +\frac{1}{6}\frac{d\[\text{H}\_2\text{O}]}{dt}$**

**1.1e:**

- Reactants: A (coeff 1 from $-\frac{d\[A]}{dt}$), B (coeff 3 from $-\frac{1}{3}\frac{d\[B]}{dt}$).
- Product: C (coeff 2 from $+\frac{1}{2}\frac{d\[C]}{dt}$).
- **Answer: $A + 3B \rightarrow 2C$**

**1.1f:**

- Coefficients: Fe³⁺ = 2, Sn²⁺ = 1, Fe²⁺ = 2, Sn⁴⁺ = 1.
- Reactants: Fe³⁺, Sn²⁺. Products: Fe²⁺, Sn⁴⁺.
- **Answer: ROR = $-\frac{1}{2}\frac{d\[\text{Fe}^{3+}]}{dt} = -\frac{d\[\text{Sn}^{2+}]}{dt} = +\frac{1}{2}\frac{d\[\text{Fe}^{2+}]}{dt} = +\frac{d\[\text{Sn}^{4+}]}{dt}$**

**1.1g:**

- Pure solids have constant concentration — their terms are omitted.
- Only O₂ (g) appears in the rate expression.
- **Answer: ROR = $+\frac{1}{3}\frac{d\[\text{O}\_2]}{dt}$**

**1.1h:**

- Reactants: X (coeff 4), Y (coeff 5). Product: Z (coeff 6).
- **Answer: $4X + 5Y \rightarrow 6Z$**
- Rate of change is fastest for the species with the smallest coefficient in the denominator of the rate expression: Z has $+\frac{1}{6}\frac{d\[Z]}{dt}$, so $\frac{d\[Z]}{dt} = 6 \times \text{ROR}$, making Z the fastest.

**1.1i:**

- Coefficients: MnO₄⁻ = 2, C₂O₄²⁻ = 5, H⁺ = 16, Mn²⁺ = 2, CO₂ = 10, H₂O = 8.
- **Answer: ROR = $-\frac{1}{2}\frac{d\[\text{MnO}\_4^-]}{dt} = -\frac{1}{5}\frac{d\[\text{C}\_2\text{O}\_4^{2-}]}{dt} = -\frac{1}{16}\frac{d\[\text{H}^+]}{dt} = +\frac{1}{2}\frac{d\[\text{Mn}^{2+}]}{dt} = +\frac{1}{10}\frac{d\[\text{CO}\_2]}{dt} = +\frac{1}{8}\frac{d\[\text{H}\_2\text{O}]}{dt}$**

</details>

***

### Type 2: Average Rate Calculations

**The Pattern:** You are given initial and final concentrations and a time interval. Use $\frac{-\Delta\[R]}{\Delta t}$ or $\frac{+\Delta\[P]}{\Delta t}$.

#### Solved Example 1.2

**Q:** For $R \rightarrow P$, the concentration of a reactant changes from $0.03\text{ M}$ to $0.02\text{ M}$ in $25\text{ minutes}$. Calculate the average rate of reaction in $\text{M min}^{-1}$ and $\text{M s}^{-1}$. 🟡

**Solution:**

```Java
1. Calculate in M/min:
   Rate = - ( [R]_final - [R]_initial ) / Δt
   Rate = - (0.02 - 0.03) / 25
   Rate = - (-0.01) / 25 = 1/2500 = 4 × 10^-4 M min^-1

2. Calculate in M/s:
   Δt = 25 min = 25 × 60 s = 1500 s
   Rate = - (-0.01) / 1500 = 6.67 × 10^-6 M s^-1

Answer: 4 × 10^-4 M min^-1 and 6.67 × 10^-6 M s^-1.
```

#### Practice Questions — Type 2

| #    | Question                                                                                                                                                      | Difficulty |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1.2a | Concentration of a reactant falls from $0.5\text{ M}$ to $0.1\text{ M}$ in $10\text{ seconds}$. Calculate the rate of disappearance.                          | 🟢         |
| 1.2b | For $A \rightarrow B$, $\[A]$ changes from $1.2\text{ M}$ to $0.6\text{ M}$ in $2\text{ minutes}$. Find the rate in $\text{M s}^{-1}$.                        | 🟡         |
| 1.2c | The concentration of a product increases from $0\text{ M}$ to $0.08\text{ M}$ in $4\text{ seconds}$. Calculate the average rate of appearance of the product. | 🟢         |
| 1.2d | A reactant's concentration falls from $0.9\text{ M}$ to $0.3\text{ M}$ in $30\text{ seconds}$. Find the average rate of disappearance.                                                                               | 🟢         |
| 1.2e | For $A \rightarrow B$, the concentration of $A$ changes from $2.0\text{ M}$ to $0.5\text{ M}$ in $3\text{ minutes}$. Find the average rate in $\text{M s}^{-1}$.                                                      | 🟡         |
| 1.2f | The concentration of a product rises from $0.02\text{ M}$ to $0.14\text{ M}$ in $6\text{ seconds}$. Calculate the rate of appearance in $\text{M min}^{-1}$.                                                         | 🟡         |
| 1.2g | A reactant decomposes from $0.10\text{ M}$ to $0.025\text{ M}$ in $50\text{ seconds}$. What is the average rate of decomposition?                                                                                   | 🟡         |
| 1.2h | For $2A \rightarrow B$, the concentration of $B$ increases from $0$ to $0.06\text{ M}$ in $20\text{ s}$. Find the average rate of disappearance of $A$ in $\text{M s}^{-1}$.                                         | 🔴         |
| 1.2i | At $t = 0$, $[R] = 0.8\text{ M}$. At $t = 20\text{ s}$, $[R] = 0.4\text{ M}$. At $t = 50\text{ s}$, $[R] = 0.1\text{ M}$. Calculate the average rate in each interval. Which interval has the highest rate?       | 🔴         |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**1.2a:**

- Rate = $-(0.1 - 0.5) / 10 = -(-0.4) / 10 = 0.04\text{ M s}^{-1}$

**1.2b:**

- $\Delta\[A] = 0.6 - 1.2 = -0.6\text{ M}$. Time $= 2\text{ min} = 120\text{ s}$.
- Rate $= -(-0.6) / 120 = 0.6 / 120 = 5 \times 10^{-3}\text{ M s}^{-1}$

**1.2c:**

- Rate = $+(0.08 - 0) / 4 = 0.02\text{ M s}^{-1}$

**1.2d:**

- Rate = $-(0.3 - 0.9) / 30 = -(-0.6) / 30 = 0.02\text{ M s}^{-1}$

**1.2e:**

- $\Delta\[A] = 0.5 - 2.0 = -1.5\text{ M}$. Time $= 3\text{ min} = 180\text{ s}$.
- Rate $= -(-1.5) / 180 = 1.5 / 180 = 8.33 \times 10^{-3}\text{ M s}^{-1}$

**1.2f:**

- Rate of appearance $= +(0.14 - 0.02) / 6 = 0.12 / 6 = 0.02\text{ M s}^{-1}$.
- In $\text{M min}^{-1}$: $0.02 \times 60 = 1.2\text{ M min}^{-1}$

**1.2g:**

- Rate $= -(0.025 - 0.10) / 50 = -(-0.075) / 50 = 1.5 \times 10^{-3}\text{ M s}^{-1}$

**1.2h:**

- Rate of appearance of B $= +(0.06 - 0) / 20 = 0.003\text{ M s}^{-1}$.
- Stoichiometry: $-\frac{1}{2}\frac{d\[A]}{dt} = +\frac{d\[B]}{dt} \implies -\frac{d\[A]}{dt} = 2 \times 0.003 = 6 \times 10^{-3}\text{ M s}^{-1}$

**1.2i:**

- Interval 1 ($0$ to $20\text{ s}$): $-(0.4 - 0.8) / 20 = 0.4 / 20 = 0.02\text{ M s}^{-1}$
- Interval 2 ($20$ to $50\text{ s}$): $-(0.1 - 0.4) / 30 = 0.3 / 30 = 0.01\text{ M s}^{-1}$
- Interval 1 has the highest rate ($0.02\text{ M s}^{-1}$).

</details>

***

### Type 3: Interrelating Rates using Stoichiometry

**The Pattern:** You are given the rate of change of ONE species, and asked for the rate of change of ANOTHER species, or the overall ROR.

#### Solved Example 1.3

**Q:** For the reaction $2\text{N}\_2\text{O}\_5 \rightarrow 4\text{NO}\_2 + \text{O}\_2$, the rate of formation of $\text{NO}\_2$ is $2.8 \times 10^{-3}\text{ M s}^{-1}$. Calculate the rate of disappearance of $\text{N}\_2\text{O}\_5$. ⭐ 🟡

**Solution:**

```
1. Write the equality:
   - (1/2) d[N2O5]/dt = + (1/4) d[NO2]/dt

2. We need the "rate of disappearance of N2O5", which is just ( - d[N2O5]/dt ). Do NOT include the 1/2 in the final variable we are solving for!
   - d[N2O5]/dt = (2/4) × (+ d[NO2]/dt)
   
3. Substitute the given value (+ d[NO2]/dt = 2.8 × 10^-3):
   - d[N2O5]/dt = (1/2) × 2.8 × 10^-3 = 1.4 × 10^-3 M s^-1

Answer: 1.4 × 10^-3 M s^-1
```

> ⚠️ **Classic Trap:** Students often calculate $\text{ROR}$ (which is $0.7 \times 10^{-3}$) and present it as the rate of disappearance. Remember: **Rate of disappearance of A = $-\frac{d\[A]}{dt}$**.

#### Practice Questions — Type 3

| #    | Question                                                                                                                                                                                     | Difficulty |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1.3a | For $\text{N}\_2 + 3\text{H}\_2 \rightarrow 2\text{NH}\_3$, if $\frac{d\[\text{NH}\_3]}{dt} = 2 \times 10^{-4}\text{ M s}^{-1}$, find $-\frac{d\[\text{H}\_2]}{dt}$.                         | 🟡         |
| 1.3b | In $2\text{SO}\_2 + \text{O}\_2 \rightarrow 2\text{SO}\_3$, the rate of disappearance of $\text{O}\_2$ is $2 \times 10^{-4}\text{ M s}^{-1}$. Find the rate of appearance of $\text{SO}\_3$. | 🟢         |
| 1.3c | For $3A \rightarrow 2B$, rate of reaction is $1.5 \times 10^{-3}\text{ M s}^{-1}$. Find the rate of disappearance of $A$.                                                                    | 🟡         |
| 1.3d | For $2A \rightarrow B$, if $-\frac{d\[A]}{dt} = 4 \times 10^{-3}\text{ M s}^{-1}$, find $+\frac{d\[B]}{dt}$.                                                                              | 🟢         |
| 1.3e | In $\text{N}\_2 + 3\text{H}\_2 \rightarrow 2\text{NH}\_3$, the rate of formation of $\text{NH}\_3$ is $5 \times 10^{-4}\text{ M s}^{-1}$. Find the rate of disappearance of $\text{N}\_2$. | 🟢         |
| 1.3f | For $2\text{NO} + \text{O}\_2 \rightarrow 2\text{NO}\_2$, the rate of disappearance of $\text{O}\_2$ is $3 \times 10^{-3}\text{ M s}^{-1}$. Find the rate of appearance of $\text{NO}\_2$. | 🟡         |
| 1.3g | For $4A + 3B \rightarrow 2C$, the ROR is $2 \times 10^{-3}\text{ M s}^{-1}$. Find $-\frac{d\[A]}{dt}$ and $+\frac{d\[C]}{dt}$.                                                            | 🟡         |
| 1.3h | For $2\text{N}\_2\text{O}\_5 \rightarrow 4\text{NO}\_2 + \text{O}\_2$, the rate of appearance of $\text{O}\_2$ is $5 \times 10^{-4}\text{ M s}^{-1}$. Find (i) rate of appearance of $\text{NO}\_2$, (ii) rate of disappearance of $\text{N}\_2\text{O}\_5$. | 🔴         |
| 1.3i | For $A + 2B \rightarrow 3C$, $-\frac{d\[B]}{dt} = 6 \times 10^{-3}\text{ M s}^{-1}$ and $+\frac{d\[C]}{dt} = 9 \times 10^{-3}\text{ M s}^{-1}$. Are these rates consistent with stoichiometry? Find the ROR. | 🔴         |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**1.3a:**

- $-\frac{1}{3}\frac{d\[\text{H}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{NH}\_3]}{dt}$
- $-\frac{d\[\text{H}\_2]}{dt} = \frac{3}{2} (2 \times 10^{-4}) = 3 \times 10^{-4}\text{ M s}^{-1}$

**1.3b:**

- $-\frac{d\[\text{O}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{SO}\_3]}{dt}$
- $2 \times 10^{-4} = \frac{1}{2}\frac{d\[\text{SO}\_3]}{dt} \implies \frac{d\[\text{SO}\_3]}{dt} = 4 \times 10^{-4}\text{ M s}^{-1}$

**1.3c:**

- $\text{ROR} = -\frac{1}{3}\frac{d\[A]}{dt}$
- $-\frac{d\[A]}{dt} = 3 \times \text{ROR} = 3 \times 1.5 \times 10^{-3} = 4.5 \times 10^{-3}\text{ M s}^{-1}$

**1.3d:**

- $-\frac{1}{2}\frac{d\[A]}{dt} = +\frac{d\[B]}{dt}$
- $\frac{d\[B]}{dt} = \frac{1}{2} \times (4 \times 10^{-3}) = 2 \times 10^{-3}\text{ M s}^{-1}$

**1.3e:**

- $-\frac{d\[\text{N}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{NH}\_3]}{dt}$
- $-\frac{d\[\text{N}\_2]}{dt} = \frac{1}{2} \times (5 \times 10^{-4}) = 2.5 \times 10^{-4}\text{ M s}^{-1}$

**1.3f:**

- $-\frac{d\[\text{O}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{NO}\_2]}{dt}$
- $3 \times 10^{-3} = \frac{1}{2}\frac{d\[\text{NO}\_2]}{dt} \implies \frac{d\[\text{NO}\_2]}{dt} = 6 \times 10^{-3}\text{ M s}^{-1}$

**1.3g:**

- $-\frac{1}{4}\frac{d\[A]}{dt} = \text{ROR} \implies -\frac{d\[A]}{dt} = 4 \times (2 \times 10^{-3}) = 8 \times 10^{-3}\text{ M s}^{-1}$
- $+\frac{1}{2}\frac{d\[C]}{dt} = \text{ROR} \implies \frac{d\[C]}{dt} = 2 \times (2 \times 10^{-3}) = 4 \times 10^{-3}\text{ M s}^{-1}$

**1.3h:**

- $+\frac{1}{4}\frac{d\[\text{NO}\_2]}{dt} = +\frac{d\[\text{O}\_2]}{dt} \implies \frac{d\[\text{NO}\_2]}{dt} = 4 \times (5 \times 10^{-4}) = 2 \times 10^{-3}\text{ M s}^{-1}$
- $-\frac{1}{2}\frac{d\[\text{N}\_2\text{O}\_5]}{dt} = +\frac{d\[\text{O}\_2]}{dt} \implies -\frac{d\[\text{N}\_2\text{O}\_5]}{dt} = 2 \times (5 \times 10^{-4}) = 1 \times 10^{-3}\text{ M s}^{-1}$

**1.3i:**

- Check: $-\frac{1}{2}\frac{d\[B]}{dt} = \frac{1}{2}(6 \times 10^{-3}) = 3 \times 10^{-3}$ and $+\frac{1}{3}\frac{d\[C]}{dt} = \frac{1}{3}(9 \times 10^{-3}) = 3 \times 10^{-3}$. They are equal, so consistent.
- $\text{ROR} = 3 \times 10^{-3}\text{ M s}^{-1}$

</details>

***

## 🔀 Stage 4: Type Mixer

| #    | Question                                                                                                                                                                                                                                                     | Types Used | Difficulty |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---------- |
| 1.M1 | For the reaction $2A + B \rightarrow 3C$, the concentration of $C$ increases from $0.1\text{ M}$ to $0.4\text{ M}$ in $15\text{ seconds}$. Calculate the rate of reaction and the rate of disappearance of $A$.                                              | T2 + T3    | 🟡         |
| 1.M2 | During the formation of ammonia ($\text{N}\_2 + 3\text{H}\_2 \rightarrow 2\text{NH}\_3$), $2\text{ moles}$ of $\text{N}\_2$ disappear in $1\text{ minute}$ in a $2\text{ Litre}$ vessel. Find the rate of appearance of $\text{NH}\_3$ in $\text{M s}^{-1}$. | T2 + T3    | 🔴         |
| 1.M3 | For $2A + 3B \rightarrow C$, the concentration of $A$ changes from $0.5\text{ M}$ to $0.2\text{ M}$ in $20\text{ s}$. Find the rate of reaction and the rate of disappearance of $B$.                                      | T2 + T3    | 🟡         |
| 1.M4 | In $A + 2B \rightarrow 3C$, $[C]$ increases from $0$ to $0.6\text{ M}$ in $10\text{ s}$. Find the ROR and $-\frac{d\[B]}{dt}$.                                                                                           | T2 + T3    | 🟡         |
| 1.M5 | For $4\text{NH}\_3 + 5\text{O}\_2 \rightarrow 4\text{NO} + 6\text{H}\_2\text{O}$, $0.8\text{ moles}$ of $\text{NH}\_3$ disappear in $25\text{ s}$ in a $4\text{ L}$ vessel. Find the rate of disappearance of $\text{O}\_2$ in $\text{M s}^{-1}$. | T2 + T3    | 🔴         |
| 1.M6 | The rate of disappearance of $A$ in $2A + B \rightarrow 3C$ is $0.02\text{ M s}^{-1}$. Separately, $[C]$ increases from $0.1\text{ M}$ to $0.4\text{ M}$ in $15\text{ s}$. Is the given rate of $A$ consistent?          | T2 + T3    | 🔴         |
| 1.M7 | For $3A \rightarrow 2B$, the concentration of $A$ falls from $0.9\text{ M}$ to $0.3\text{ M}$ in $20\text{ s}$. Find the rate of appearance of $B$ and the ROR.                                                           | T2 + T3    | 🟡         |
| 1.M8 | In $A + 2B \rightarrow 3C$, $2.4\text{ moles}$ of $A$ react in $40\text{ s}$ in a $6\text{ L}$ vessel. Find the rate of appearance of $C$ in $\text{M min}^{-1}$.                                                          | T2 + T3    | 🔴         |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**1.M1:**

- Rate of appearance of C = $+\frac{d\[C]}{dt} = \frac{0.4 - 0.1}{15} = \frac{0.3}{15} = 0.02\text{ M s}^{-1}$.
- $\text{ROR} = \frac{1}{3}\frac{d\[C]}{dt} = \frac{0.02}{3} = 6.67 \times 10^{-3}\text{ M s}^{-1}$.
- $-\frac{1}{2}\frac{d\[A]}{dt} = \frac{1}{3}\frac{d\[C]}{dt} \implies -\frac{d\[A]}{dt} = \frac{2}{3}(0.02) = 0.0133\text{ M s}^{-1}$.

**1.M2:**

- $\Delta\[\text{N}\_2] = \frac{2\text{ moles}}{2\text{ L}} = 1\text{ M}$. Time $= 60\text{ s}$.
- Rate of disappearance of $\text{N}\_2 = -\frac{d\[\text{N}\_2]}{dt} = \frac{1}{60}\text{ M s}^{-1}$.
- $-\frac{d\[\text{N}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{NH}\_3]}{dt} \implies \frac{d\[\text{NH}\_3]}{dt} = 2 \times \frac{1}{60} = \frac{1}{30} = 0.033\text{ M s}^{-1}$.

**1.M3:**

- $-\frac{d\[A]}{dt} = \frac{0.5 - 0.2}{20} = \frac{0.3}{20} = 0.015\text{ M s}^{-1}$.
- $\text{ROR} = -\frac{1}{2}\frac{d\[A]}{dt} = \frac{0.015}{2} = 7.5 \times 10^{-3}\text{ M s}^{-1}$.
- $-\frac{1}{3}\frac{d\[B]}{dt} = \text{ROR} \implies -\frac{d\[B]}{dt} = 3 \times 7.5 \times 10^{-3} = 0.0225\text{ M s}^{-1}$.

**1.M4:**

- $+\frac{d\[C]}{dt} = \frac{0.6 - 0}{10} = 0.06\text{ M s}^{-1}$.
- $\text{ROR} = +\frac{1}{3}\frac{d\[C]}{dt} = \frac{0.06}{3} = 0.02\text{ M s}^{-1}$.
- $-\frac{1}{2}\frac{d\[B]}{dt} = \text{ROR} \implies -\frac{d\[B]}{dt} = 2 \times 0.02 = 0.04\text{ M s}^{-1}$.

**1.M5:**

- $\Delta\[\text{NH}\_3] = \frac{0.8}{4} = 0.2\text{ M}$. Time $= 25\text{ s}$.
- $-\frac{d\[\text{NH}\_3]}{dt} = \frac{0.2}{25} = 8 \times 10^{-3}\text{ M s}^{-1}$.
- $-\frac{1}{4}\frac{d\[\text{NH}\_3]}{dt} = -\frac{1}{5}\frac{d\[\text{O}\_2]}{dt} \implies -\frac{d\[\text{O}\_2]}{dt} = \frac{5}{4} \times (8 \times 10^{-3}) = 10^{-2}\text{ M s}^{-1}$.

**1.M6:**

- Measured $+\frac{d\[C]}{dt} = \frac{0.4 - 0.1}{15} = 0.02\text{ M s}^{-1}$.
- From stoichiometry: $-\frac{1}{2}\frac{d\[A]}{dt} = +\frac{1}{3}\frac{d\[C]}{dt} \implies -\frac{d\[A]}{dt} = \frac{2}{3} \times 0.02 = 0.0133\text{ M s}^{-1}$.
- But the given $-\frac{d\[A]}{dt} = 0.02\text{ M s}^{-1}$. These differ, so the given rate is NOT consistent.

**1.M7:**

- $-\frac{d\[A]}{dt} = \frac{0.9 - 0.3}{20} = \frac{0.6}{20} = 0.03\text{ M s}^{-1}$.
- $\text{ROR} = -\frac{1}{3}\frac{d\[A]}{dt} = \frac{0.03}{3} = 0.01\text{ M s}^{-1}$.
- $+\frac{1}{2}\frac{d\[B]}{dt} = \text{ROR} \implies \frac{d\[B]}{dt} = 2 \times 0.01 = 0.02\text{ M s}^{-1}$.

**1.M8:**

- $\Delta\[A] = \frac{2.4}{6} = 0.4\text{ M}$. Time $= 40\text{ s}$.
- $-\frac{d\[A]}{dt} = \frac{0.4}{40} = 0.01\text{ M s}^{-1}$.
- $-\frac{d\[A]}{dt} = +\frac{1}{3}\frac{d\[C]}{dt} \implies \frac{d\[C]}{dt} = 3 \times 0.01 = 0.03\text{ M s}^{-1}$.
- In $\text{M min}^{-1}$: $0.03 \times 60 = 1.8\text{ M min}^{-1}$.

</details>

***

## 📋 Stage 5: Board Arsenal

**NCERT & Board-style questions. Score these every exam.**

| #    | Question                                                                                                                                                                                 | Difficulty |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1.B1 | Define the rate of a reaction. What is its unit?                                                                                                                                         | 🟢         |
| 1.B2 | Differentiate between average rate and instantaneous rate of a reaction.                                                                                                                 | 🟢         |
| 1.B3 | For the reaction $R \rightarrow P$, the concentration of a reactant changes from $0.05\text{ M}$ to $0.04\text{ M}$ in $30\text{ minutes}$. Calculate average rate in seconds. *(NCERT)* | 🟡         |
| 1.B4 | Express the rate of the following reaction in terms of different reactants and products: $4\text{NH}\_3(g) + 5\text{O}\_2(g) \rightarrow 4\text{NO}(g) + 6\text{H}\_2\text{O}(g)$.       | 🟢         |
| 1.B5 | For the reaction $2\text{H}\_2\text{O}\_2 \rightarrow 2\text{H}\_2\text{O} + \text{O}\_2$, write the rate expression.                                                                   | 🟢         |
| 1.B6 | What is the difference between the rate of disappearance of a reactant and the overall rate of reaction? Explain with an example.                                                       | 🟢         |
| 1.B7 | The rate of formation of $\text{NO}\_2$ in $2\text{N}\_2\text{O}\_5 \rightarrow 4\text{NO}\_2 + \text{O}\_2$ is $2.8 \times 10^{-3}\text{ M s}^{-1}$. Calculate the rate of disappearance of $\text{N}\_2\text{O}\_5$ and the rate of reaction. | 🟡         |
| 1.B8 | If the rate of reaction is $3 \times 10^{-4}\text{ M s}^{-1}$ for $2A + B \rightarrow 3C$, find $-\frac{d\[A]}{dt}$ and $+\frac{d\[C]}{dt}$.                                            | 🟡         |
| 1.B9 | For $A + 3B \rightarrow 2C$, $[B]$ decreases from $0.8\text{ M}$ to $0.2\text{ M}$ in $40\text{ s}$. Calculate: (i) average ROR, (ii) rate of disappearance of $A$, (iii) rate of appearance of $C$. | 🔴         |
| 1.B10 | The rate of a reaction quadruples when the concentration of a reactant is doubled. If the rate law is $r = k\[A]^n$, determine the value of $n$.                                         | 🔴         |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**1.B1:**

- Rate of a reaction is defined as the change in concentration of any of the reactants or products per unit time. Unit: $\text{mol L}^{-1}\text{s}^{-1}$.

**1.B2:**

- **Average Rate:** Change in concentration over a finite, macroscopic time interval ($\Delta t$). It is calculated as $\frac{\Delta C}{\Delta t}$.
- **Instantaneous Rate:** Rate of change of concentration at a specific, exact instant of time ($dt$). It is calculated as the slope of the tangent to the concentration-time curve at that instant, $\frac{dc}{dt}$.

**1.B3:**

- $\Delta t = 30\text{ min} \times 60 = 1800\text{ s}$.
- Rate = $-\frac{0.04 - 0.05}{1800} = \frac{0.01}{1800} = 5.56 \times 10^{-6}\text{ M s}^{-1}$.

**1.B4:**

- $\text{Rate} = -\frac{1}{4}\frac{d\[\text{NH}\_3]}{dt} = -\frac{1}{5}\frac{d\[\text{O}\_2]}{dt} = +\frac{1}{4}\frac{d\[\text{NO}]}{dt} = +\frac{1}{6}\frac{d\[\text{H}\_2\text{O}]}{dt}$

**1.B5:**

- $\text{ROR} = -\frac{1}{2}\frac{d\[\text{H}\_2\text{O}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{H}\_2\text{O}]}{dt} = +\frac{d\[\text{O}\_2]}{dt}$

**1.B6:**

- Rate of disappearance of a reactant ($-\frac{d\[R]}{dt}$) is the change in its concentration per unit time. The overall rate of reaction divides this by the stoichiometric coefficient. Example: For $2A \rightarrow B$, $-\frac{d\[A]}{dt}$ is the rate of disappearance, while $\text{ROR} = -\frac{1}{2}\frac{d\[A]}{dt}$.

**1.B7:**

- $-\frac{1}{2}\frac{d\[\text{N}\_2\text{O}\_5]}{dt} = +\frac{1}{4}\frac{d\[\text{NO}\_2]}{dt}$
- $-\frac{d\[\text{N}\_2\text{O}\_5]}{dt} = \frac{2}{4}(2.8 \times 10^{-3}) = 1.4 \times 10^{-3}\text{ M s}^{-1}$
- $\text{ROR} = +\frac{1}{4}\frac{d\[\text{NO}\_2]}{dt} = \frac{2.8 \times 10^{-3}}{4} = 7 \times 10^{-4}\text{ M s}^{-1}$

**1.B8:**

- $-\frac{1}{2}\frac{d\[A]}{dt} = \text{ROR} \implies -\frac{d\[A]}{dt} = 2 \times (3 \times 10^{-4}) = 6 \times 10^{-4}\text{ M s}^{-1}$
- $+\frac{1}{3}\frac{d\[C]}{dt} = \text{ROR} \implies \frac{d\[C]}{dt} = 3 \times (3 \times 10^{-4}) = 9 \times 10^{-4}\text{ M s}^{-1}$

**1.B9:**

- $-\frac{d\[B]}{dt} = \frac{0.8 - 0.2}{40} = \frac{0.6}{40} = 0.015\text{ M s}^{-1}$
- (i) $\text{ROR} = -\frac{1}{3}\frac{d\[B]}{dt} = \frac{0.015}{3} = 5 \times 10^{-3}\text{ M s}^{-1}$
- (ii) $-\frac{d\[A]}{dt} = \text{ROR} = 5 \times 10^{-3}\text{ M s}^{-1}$
- (iii) $+\frac{1}{2}\frac{d\[C]}{dt} = \text{ROR} \implies \frac{d\[C]}{dt} = 2 \times (5 \times 10^{-3}) = 0.01\text{ M s}^{-1}$

**1.B10:**

- Doubling $[A]$ quadruples $r$: $\frac{r_2}{r_1} = \frac{k(2\[A])^n}{k\[A]^n} = 2^n = 4 \implies n = 2$.

</details>

***

## 🚀 Stage 6: JEE Mains Arena

**MCQs with traps. Explanation required.**

**Q1.J1 🟡**
For the reaction $\text{N}\_2(g) + 3\text{H}\_2(g) \rightarrow 2\text{NH}\_3(g)$, under certain conditions of temperature and partial pressure of the reactants, the rate of formation of $\text{NH}\_3$ is $0.001\text{ kg hr}^{-1}$. The rate of conversion of $\text{H}\_2$ under the same conditions is:

(A) $1.5 \times 10^{-3}\text{ kg hr}^{-1}$&#x20;
(B) $1.76 \times 10^{-4}\text{ kg hr}^{-1}$&#x20;
(C) $2 \times 10^{-3}\text{ kg hr}^{-1}$&#x20;
(D) $3 \times 10^{-3}\text{ kg hr}^{-1}$

**Q1.J2 🔴 (The Unit Trap)**
For the reaction $2\text{SO}\_2 + \text{O}\_2 \rightarrow 2\text{SO}\_3$, the rate of disappearance of $\text{SO}\_2$ is $1.28 \times 10^{-3}\text{ g s}^{-1}$. What is the rate of appearance of $\text{SO}\_3$ in $\text{mol L}^{-1}\text{ s}^{-1}$ if the volume of the vessel is $2\text{ Litres}$? (Atomic mass: S=32, O=16)

(A) $1.28 \times 10^{-3}$&#x20;
(B) $10^{-5}$&#x20;
(C) $2 \times 10^{-5}$&#x20;
(D) $0.64 \times 10^{-3}$

**Q1.J3 🟡**
In the reaction $A + 2B \rightarrow 3C + 2D$, the rate of disappearance of B is $1 \times 10^{-2}\text{ mol L}^{-1}\text{s}^{-1}$. What will be the rate of the reaction and rate of change of concentration of A?

(A) $1 \times 10^{-2}, 1 \times 10^{-2}$&#x20;
(B) $0.5 \times 10^{-2}, 0.5 \times 10^{-2}$&#x20;
(C) $2 \times 10^{-2}, 1 \times 10^{-2}$&#x20;
(D) $1 \times 10^{-2}, 0.5 \times 10^{-2}$

**Q1.J4 🟡**
For $\text{CO}(g) + \text{Cl}\_2(g) \rightarrow \text{COCl}\_2(g)$, the rate of disappearance of $\text{Cl}\_2$ is $0.02\text{ M s}^{-1}$. The rate of appearance of $\text{COCl}\_2$ is:

(A) $0.01\text{ M s}^{-1}$&#x20;
(B) $0.02\text{ M s}^{-1}$&#x20;
(C) $0.04\text{ M s}^{-1}$&#x20;
(D) $0.03\text{ M s}^{-1}$

**Q1.J5 🟡**
For $2\text{NOBr}(g) \rightarrow 2\text{NO}(g) + \text{Br}\_2(g)$, the rate of disappearance of $\text{NOBr}$ is $6 \times 10^{-4}\text{ M s}^{-1}$. What is the rate of appearance of $\text{Br}\_2$?

(A) $3 \times 10^{-4}\text{ M s}^{-1}$&#x20;
(B) $6 \times 10^{-4}\text{ M s}^{-1}$&#x20;
(C) $1.2 \times 10^{-3}\text{ M s}^{-1}$&#x20;
(D) $1.5 \times 10^{-4}\text{ M s}^{-1}$

**Q1.J6 🟡**
In a reaction $R \rightarrow P$, the concentration of $R$ falls from $0.04\text{ M}$ to $0.03\text{ M}$ in $10\text{ min}$. The average rate during this interval is:

(A) $10^{-3}\text{ M min}^{-1}$&#x20;
(B) $10^{-4}\text{ M min}^{-1}$&#x20;
(C) $10^{-5}\text{ M min}^{-1}$&#x20;
(D) $10^{-2}\text{ M min}^{-1}$

**Q1.J7 🔴 (Unit Conversion)**
The concentration of a reactant changes from $0.6\text{ M}$ to $0.2\text{ M}$ in $5\text{ min}$. The average rate in $\text{M s}^{-1}$ is:

(A) $0.08$&#x20;
(B) $1.33 \times 10^{-3}$&#x20;
(C) $8 \times 10^{-3}$&#x20;
(D) $0.0133$

**Q1.J8 🔴**
For $2\text{NH}\_3 \rightarrow \text{N}\_2 + 3\text{H}\_2$, the rate of disappearance of $\text{NH}\_3$ is $1.2 \times 10^{-3}\text{ M s}^{-1}$. The rate of appearance of $\text{H}\_2$ is:

(A) $0.6 \times 10^{-3}\text{ M s}^{-1}$&#x20;
(B) $1.2 \times 10^{-3}\text{ M s}^{-1}$&#x20;
(C) $1.8 \times 10^{-3}\text{ M s}^{-1}$&#x20;
(D) $2.4 \times 10^{-3}\text{ M s}^{-1}$

**Q1.J9 🟡**
For $2A \rightarrow B$, the rate of reaction is $0.02\text{ M s}^{-1}$ at a certain instant. What is $-\frac{d\[A]}{dt}$ at that instant?

(A) $0.01\text{ M s}^{-1}$&#x20;
(B) $0.02\text{ M s}^{-1}$&#x20;
(C) $0.04\text{ M s}^{-1}$&#x20;
(D) $0.005\text{ M s}^{-1}$

**Q1.J10 🔴**
For the reaction $2\text{SO}\_2 + \text{O}\_2 \rightarrow 2\text{SO}\_3$, the rate of disappearance of $\text{SO}\_2$ is $2 \times 10^{-4}\text{ mol L}^{-1}\text{s}^{-1}$. If the volume of the vessel is $5\text{ L}$, what is the rate of consumption of $\text{SO}\_2$ in $\text{mol s}^{-1}$?

(A) $10^{-3}\text{ mol s}^{-1}$&#x20;
(B) $2 \times 10^{-4}\text{ mol s}^{-1}$&#x20;
(C) $4 \times 10^{-4}\text{ mol s}^{-1}$&#x20;
(D) $5 \times 10^{-4}\text{ mol s}^{-1}$

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**1.J1 → Answer: (B)**

- **Trap:** The rate is given in **kg/hr**, NOT mol/hr! Stoichiometric relations ($-\frac{1}{3}\frac{d\[\text{H}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{NH}\_3]}{dt}$) ONLY work for **moles or molarity**.
- First, convert mass rate to mole rate: Molar mass of $\text{NH}\_3 = 17\text{ g/mol} = 0.017\text{ kg/mol}$.
- $\frac{d n\_{\text{NH}\_3}}{dt} = \frac{0.001}{0.017} = \frac{1}{17}\text{ mol hr}^{-1}$.
- Now use stoichiometry: $-\frac{d n_{\text{H}_2}}{dt} = \frac{3}{2} \times \frac{d n_{\text{NH}\_3}}{dt} = \frac{3}{2} \times \frac{1}{17} = \frac{3}{34}\text{ mol hr}^{-1}$.
- Convert back to mass rate for $\text{H}\_2$ (Molar mass = $2\text{ g/mol} = 0.002\text{ kg/mol}$):
- Rate in kg/hr $= \frac{3}{34} \times 0.002 = 1.76 \times 10^{-4}\text{ kg hr}^{-1}$.

**1.J2 → Answer: (B)**

- Mass rate of $\text{SO}\_2 = 1.28 \times 10^{-3}\text{ g s}^{-1}$. Molar mass of $\text{SO}\_2 = 64\text{ g/mol}$.
- Mole rate of $\text{SO}\_2 = \frac{1.28 \times 10^{-3}}{64} = 2 \times 10^{-5}\text{ mol s}^{-1}$.
- Molarity rate of $\text{SO}\_2$ (since V=2L) $= \frac{2 \times 10^{-5}}{2} = 10^{-5}\text{ mol L}^{-1}\text{s}^{-1}$.
- Stoichiometry: $-\frac{1}{2}\frac{d\[\text{SO}\_2]}{dt} = +\frac{1}{2}\frac{d\[\text{SO}\_3]}{dt}$.
- Therefore, rate of appearance of $\text{SO}\_3 = 10^{-5}\text{ mol L}^{-1}\text{s}^{-1}$.

**1.J3 → Answer: (B)**

- $\text{ROR} = -\frac{1}{2}\frac{d\[B]}{dt} = \frac{1}{2}(1 \times 10^{-2}) = 0.5 \times 10^{-2}\text{ M s}^{-1}$.
- $-\frac{d\[A]}{dt} = \text{ROR} = 0.5 \times 10^{-2}\text{ M s}^{-1}$.

**1.J4 → Answer: (B)**

- $\text{CO} + \text{Cl}\_2 \rightarrow \text{COCl}\_2$ has all coefficients 1.
- $-\frac{d\[\text{Cl}\_2]}{dt} = +\frac{d\[\text{COCl}\_2]}{dt} = 0.02\text{ M s}^{-1}$.

**1.J5 → Answer: (A)**

- $-\frac{1}{2}\frac{d\[\text{NOBr}]}{dt} = +\frac{d\[\text{Br}\_2]}{dt}$
- $\frac{d\[\text{Br}\_2]}{dt} = \frac{1}{2} \times (6 \times 10^{-4}) = 3 \times 10^{-4}\text{ M s}^{-1}$.

**1.J6 → Answer: (A)**

- Average rate $= -\frac{0.03 - 0.04}{10} = \frac{0.01}{10} = 10^{-3}\text{ M min}^{-1}$.

**1.J7 → Answer: (B)**

- $\Delta\[R] = 0.2 - 0.6 = -0.4\text{ M}$. $\Delta t = 5 \times 60 = 300\text{ s}$.
- Rate $= -(-0.4) / 300 = 0.4 / 300 = 1.33 \times 10^{-3}\text{ M s}^{-1}$.

**1.J8 → Answer: (C)**

- $-\frac{1}{2}\frac{d\[\text{NH}\_3]}{dt} = +\frac{1}{3}\frac{d\[\text{H}\_2]}{dt}$
- $\frac{d\[\text{H}\_2]}{dt} = \frac{3}{2} \times (1.2 \times 10^{-3}) = 1.8 \times 10^{-3}\text{ M s}^{-1}$.

**1.J9 → Answer: (C)**

- $\text{ROR} = -\frac{1}{2}\frac{d\[A]}{dt} \implies -\frac{d\[A]}{dt} = 2 \times \text{ROR} = 2 \times 0.02 = 0.04\text{ M s}^{-1}$.

**1.J10 → Answer: (A)**

- Rate of disappearance of $\text{SO}\_2$ in $\text{mol L}^{-1}\text{s}^{-1}$ is $2 \times 10^{-4}$.
- In a $5\text{ L}$ vessel, total moles consumed per second $= 2 \times 10^{-4} \times 5 = 10^{-3}\text{ mol s}^{-1}$.

</details>

***

## Key Takeaways from Chapter 1

| Concept                          | Rule                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| Writing Rate Expression          | Divide by stoichiometry. Reactants (-), Products (+).                                      |
| Defining "Rate of Disappearance" | It's just $-\frac{d\[Reactant]}{dt}$. Do not include the stoichiometry in the term itself. |
| Non-Molar Rates (Mass/Volume)    | Convert to moles/molarity *before* using the stoichiometric rate expression.               |

***

## 🧠 Stage 7: Statement & Assertion-Reasoning

**Directions:**

- **Assertion-Reason**: (A) Both A and R are true, and R is the correct explanation. (B) Both A and R are true, but R is NOT the correct explanation. (C) A is true but R is false. (D) A is false but R is true.
- **Statement I/II**: Choose based on whether each statement is correct or incorrect.

| #    | Question                                                                                                                                                                                                                       | Difficulty |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| 1.S1 | **Assertion (A):** The rate of a chemical reaction always decreases as the reaction proceeds.**Reason (R):** The concentration of reactants decreases with time, and rate is typically proportional to reactant concentration. | 🟡         |
| 1.S2 | **Assertion (A):** For $A \rightarrow 2B$, the rate of appearance of $B$ is twice the rate of disappearance of $A$.**Reason (R):** The stoichiometric coefficients dictates the relative rates of change of species.           | 🟢         |
| 1.S3 | **Statement I:** The average rate and instantaneous rate of a reaction are always equal.**Statement II:** Instantaneous rate is calculated by drawing a tangent to the concentration-time curve.                               | 🟢         |
| 1.S4 | **Assertion (A):** The unit of rate of reaction is $\text{mol L}^{-1}\text{ s}^{-1}$.**Reason (R):** Rate is defined as change in concentration per unit time.                                                                 | 🟢         |
| 1.S5 | **Assertion (A):** For $2A + B \rightarrow 3C$, the rate of disappearance of $A$ is twice the rate of disappearance of $B$.**Reason (R):** Stoichiometric coefficients dictate the relative rates of change of species.       | 🟡         |
| 1.S6 | **Assertion (A):** The rate of appearance of a product and the rate of disappearance of a reactant can be numerically different.**Reason (R):** They are related through the stoichiometric coefficients of the reaction.     | 🟡         |
| 1.S7 | **Assertion (A):** For $\text{N}\_2 + 3\text{H}\_2 \rightarrow 2\text{NH}\_3$, the rate of reaction is equal to $-\frac{d\[\text{H}\_2]}{dt}$.**Reason (R):** The rate of reaction is defined as $-\frac{1}{a}\frac{d\[R]}{dt}$ for a reactant with coefficient $a$. | 🔴         |
| 1.S8 | **Assertion (A):** The instantaneous rate of a reaction is always greater than the average rate over the same time interval.**Reason (R):** The instantaneous rate is the slope of the tangent at a point on the concentration-time curve. | 🔴         |
| 1.S9 | **Statement I:** For a zero-order reaction, the average rate equals the instantaneous rate at all times.**Statement II:** The concentration-time graph for a zero-order reaction is a straight line with constant slope.    | 🟡         |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**1.S1 → Answer: (A)**

- A is true: Except for zero-order reactions, rate decreases as time proceeds.
- R is true and is the exact reason: As reactants are consumed, there are fewer molecules to collide, lowering the rate.

**1.S2 → Answer: (A)**

- A is true: $-\frac{d\[A]}{dt} = +\frac{1}{2}\frac{d\[B]}{dt} \implies \frac{d\[B]}{dt} = 2 \times (-\frac{d\[A]}{dt})$.
- R is true: Stoichiometry is the reason for this relationship.

**1.S3 → Statement I is False, Statement II is True.**

- Statement I: False. Average rate spans an interval; instantaneous rate is at one specific point. They are only equal if the concentration-time graph is a straight line (zero-order reaction).

**1.S4 → Answer: (A)**

- A is true: Rate has units of $\text{concentration time}^{-1}$.
- R is true: Rate $= \frac{\Delta C}{\Delta t}$, hence units $\text{mol L}^{-1}\text{ s}^{-1}$. R correctly explains A.

**1.S5 → Answer: (A)**

- A is true: $-\frac{1}{2}\frac{d\[A]}{dt} = -\frac{d\[B]}{dt} \implies -\frac{d\[A]}{dt} = 2 \times (-\frac{d\[B]}{dt})$.
- R is true: The relative rates come from the stoichiometry. R correctly explains A.

**1.S6 → Answer: (A)**

- A is true: For $aA \rightarrow bB$, $-\frac{1}{a}\frac{d\[A]}{dt} = +\frac{1}{b}\frac{d\[B]}{dt}$, so $\frac{d\[B]}{dt} = \frac{b}{a}(-\frac{d\[A]}{dt})$. They differ unless $a = b$.
- R is true and correctly explains why.

**1.S7 → Answer: (D)**

- A is false: $-\frac{d\[\text{H}\_2]}{dt} = 3 \times \text{ROR}$, because $\text{ROR} = -\frac{1}{3}\frac{d\[\text{H}\_2]}{dt}$.
- R is true: The correct definition of ROR divides by the stoichiometric coefficient.

**1.S8 → Answer: (D)**

- A is false: The instantaneous rate changes over time (typically decreases). It is not always greater than the average rate — it depends on which instant is chosen.
- R is true: This is the correct definition of instantaneous rate, but it does not imply A.

**1.S9 → Statement I is True, Statement II is True, II explains I.**

- Both statements are true. For zero-order reaction, rate $= k$ (constant). The concentration-time graph is a straight line, so its slope $\frac{\Delta C}{\Delta t} = \frac{dC}{dt}$ at all points.

</details>

***

## 🏆 Stage 8: MCQ Mastery

**Q1.M1 🟢**
Which of the following is correct for the reaction $aA \rightarrow bB$?

(A) Rate $= -\frac{a}{b} \frac{d\[A]}{dt}$&#x20;
(B) Rate $= -\frac{1}{a} \frac{d\[A]}{dt} = +\frac{1}{b} \frac{d\[B]}{dt}$&#x20;
(C) Rate $= -\frac{d\[A]}{dt} = +\frac{d\[B]}{dt}$&#x20;
(D) Rate $= +\frac{1}{a} \frac{d\[A]}{dt} = -\frac{1}{b} \frac{d\[B]}{dt}$

**Q1.M2 🟡**
For the reaction $2\text{NO} + \text{O}\_2 \rightarrow 2\text{NO}\_2$, the rate of disappearance of $\text{O}\_2$ is $x$. The rate of reaction is:

(A) $x$&#x20;
(B) $2x$&#x20;
(C) $x/2$&#x20;
(D) $4x$

**Q1.M3 🔴 (Graph Interpretation)**
The slope of a tangent drawn at a point on the concentration-time curve for a reactant yields:

(A) Average rate of reaction&#x20;
(B) Rate constant&#x20;
(C) Negative of instantaneous rate&#x20;
(D) Negative of average rate

**Q1.M4 🟢**
For $3A \rightarrow 2B$, if the rate of reaction is $r$, then $-\frac{d\[A]}{dt}$ equals:

(A) $r$&#x20;
(B) $2r$&#x20;
(C) $3r$&#x20;
(D) $\frac{r}{3}$

**Q1.M5 🟡**
In $4\text{NH}\_3 + 5\text{O}\_2 \rightarrow 4\text{NO} + 6\text{H}\_2\text{O}$, which of the following relations is correct?

(A) $-\frac{d\[\text{NH}\_3]}{dt} = \frac{5}{4}\frac{d\[\text{O}\_2]}{dt}$&#x20;
(B) $-\frac{d\[\text{O}\_2]}{dt} = \frac{5}{4}\frac{d\[\text{NH}\_3]}{dt}$&#x20;
(C) $\frac{d\[\text{NO}]}{dt} = \frac{d\[\text{NH}\_3]}{dt}$&#x20;
(D) $\frac{d\[\text{H}\_2\text{O}]}{dt} = \frac{3}{2}\frac{d\[\text{NO}]}{dt}$

**Q1.M6 🟡**
The average rate of disappearance of a reactant in the first $10\text{ s}$ is $0.02\text{ M s}^{-1}$ and in the next $20\text{ s}$ is $0.01\text{ M s}^{-1}$. The total change in concentration in $30\text{ s}$ is:

(A) $0.3\text{ M}$&#x20;
(B) $0.4\text{ M}$&#x20;
(C) $0.5\text{ M}$&#x20;
(D) $0.2\text{ M}$

**Q1.M7 🔴**
For $A + 2B \rightarrow 3C$, the rate of reaction is $0.5 \times 10^{-2}\text{ M s}^{-1}$. What is $-\frac{d\[B]}{dt}$?

(A) $0.5 \times 10^{-2}\text{ M s}^{-1}$&#x20;
(B) $1.0 \times 10^{-2}\text{ M s}^{-1}$&#x20;
(C) $1.5 \times 10^{-2}\text{ M s}^{-1}$&#x20;
(D) $0.25 \times 10^{-2}\text{ M s}^{-1}$

**Q1.M8 🔴**
Which of the following statements about the rate of a reaction is FALSE?

(A) It can be expressed in $\text{atm s}^{-1}$ for gaseous reactions&#x20;
(B) It is always positive&#x20;
(C) The rate of disappearance of a reactant is always equal to the rate of appearance of a product&#x20;
(D) It is defined as the change in concentration per unit time

**Q1.M9 🔴**
If the rate of disappearance of $B$ in $A + 3B \rightarrow 2C$ is $0.6\text{ M s}^{-1}$, the rate of appearance of $C$ is:

(A) $0.2\text{ M s}^{-1}$&#x20;
(B) $0.4\text{ M s}^{-1}$&#x20;
(C) $0.6\text{ M s}^{-1}$&#x20;
(D) $0.9\text{ M s}^{-1}$

<details>
<summary>💡 Full Solutions — MCQ Mastery</summary>

**1.M1 → Answer: (B)**

- Standard definition of ROR.

**1.M2 → Answer: (A)**

- $\text{ROR} = -\frac{d\[\text{O}\_2]}{dt} = x$.

**1.M3 → Answer: (C)**

- The curve is for a reactant, so it is sloping downwards. Slope $= \frac{d\[R]}{dt}$ (which is a negative value).
- Instantaneous rate $= -\frac{d\[R]}{dt} = -(\text{Slope})$.
- Therefore, Slope $= -(\text{Instantaneous rate})$.

**1.M4 → Answer: (C)**

- $\text{ROR} = -\frac{1}{3}\frac{d\[A]}{dt} = r \implies -\frac{d\[A]}{dt} = 3r$.

**1.M5 → Answer: (D)**

- $\frac{d\[\text{H}\_2\text{O}]}{dt} = \frac{6}{4}\frac{d\[\text{NO}]}{dt} = \frac{3}{2}\frac{d\[\text{NO}]}{dt}$.

**1.M6 → Answer: (B)**

- First interval: $0.02 \times 10 = 0.2\text{ M}$. Second interval: $0.01 \times 20 = 0.2\text{ M}$. Total $= 0.4\text{ M}$.

**1.M7 → Answer: (B)**

- $\text{ROR} = -\frac{1}{2}\frac{d\[B]}{dt} \implies -\frac{d\[B]}{dt} = 2 \times (0.5 \times 10^{-2}) = 1.0 \times 10^{-2}\text{ M s}^{-1}$.

**1.M8 → Answer: (C)**

- (C) is false. The rates are related by stoichiometry and are only equal when coefficients are equal.

**1.M9 → Answer: (B)**

- $-\frac{1}{3}\frac{d\[B]}{dt} = +\frac{1}{2}\frac{d\[C]}{dt} \implies \frac{d\[C]}{dt} = \frac{2}{3} \times 0.6 = 0.4\text{ M s}^{-1}$.

</details>
