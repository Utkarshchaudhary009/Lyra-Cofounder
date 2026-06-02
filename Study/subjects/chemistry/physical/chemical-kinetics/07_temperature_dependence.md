# Chapter 7: Temperature Dependence of Rate<br>
## Part IV — Temperature & Catalysis

---

## 🎯 Stage 1: The Core Idea

### The Scene

Have you ever noticed that food spoils faster in the summer than in the winter? Or that milk stays fresh longer in the fridge?
Chemical reactions are deeply sensitive to temperature. As a general rule of thumb, **for every $10^\circ\text{C}$ rise in temperature, the rate of a chemical reaction roughly doubles**.

But *why*?

### Collision Theory

For a reaction to occur, reactant molecules must collide. But not just any collision works. An **effective collision** requires two things:
1. **Energy Barrier:** The molecules must crash into each other with enough force. This minimum required energy is called the **Threshold Energy**. The extra energy reactants need to reach this threshold is the **Activation Energy ($E_a$)**.
2. **Orientation Barrier:** They must hit each other in exactly the right spot (steric factor).

When you increase the temperature, the molecules don't just move a little faster. You vastly increase the *fraction* of molecules that possess enough kinetic energy to overcome the activation energy barrier.

### The Arrhenius Equation

Svante Arrhenius put this into a brilliant mathematical model:
$$k = A e^{-E_a/RT}$$

| Symbol | Name | Meaning |
|--------|------|---------|
| $k$ | Rate constant | How fast the reaction goes. |
| $A$ | Frequency Factor (Arrhenius factor) | How often molecules collide with the correct orientation. |
| $E_a$ | Activation Energy | The energy wall they have to climb ($\text{J mol}^{-1}$). |
| $R$ | Gas Constant | $8.314\text{ J K}^{-1}\text{mol}^{-1}$ |
| $T$ | Temperature | Must be in Kelvin! |
| $e^{-E_a/RT}$ | Boltzmann Factor | The fraction of molecules with energy $\ge E_a$. |

> ⚠️ **Classic Trap:** The unit of $A$ is exactly the same as the unit of $k$. Don't assume $A$ is unitless! Also, always convert $E_a$ from kJ to J before plugging it in with $R = 8.314$.

---

## 🔬 Stage 2: The Formula Lab

### Derivation 1: Logarithmic Forms of Arrhenius Equation

Start with: $k = A e^{-E_a/RT}$
Take natural log ($\ln$) on both sides:
$$\ln k = \ln A - \frac{E_a}{RT}$$
This is the equation of a straight line ($y = c + mx$). A plot of $\ln k$ versus $1/T$ yields a straight line with:
- Slope = $-E_a / R$
- y-intercept = $\ln A$

Convert to base-10 log:
$$2.303 \log k = 2.303 \log A - \frac{E_a}{RT}$$
$$\log k = \log A - \frac{E_a}{2.303 RT}$$
A plot of $\log k$ versus $1/T$ yields a straight line with:
- Slope = $-E_a / 2.303 R$

### Derivation 2: Two-Temperature Formula

If we measure the rate constant at two different temperatures ($T_1$ and $T_2$):
At $T_1$: $\ln k_1 = \ln A - \frac{E_a}{RT_1}$
At $T_2$: $\ln k_2 = \ln A - \frac{E_a}{RT_2}$

Subtracting the first from the second:
$$\ln k_2 - \ln k_1 = \frac{E_a}{R} \left( \frac{1}{T_1} - \frac{1}{T_2} \right)$$
$$\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303 R} \left[ \frac{1}{T_1} - \frac{1}{T_2} \right]$$
Or:
$$\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303 R} \left[ \frac{T_2 - T_1}{T_1 T_2} \right]$$

### Formula 3: Temperature Coefficient (T.C.)

$$\text{T.C.} = \frac{k_{T+10}}{k_T} \approx 2 \text{ or } 3$$
If temperature increases by $\Delta T$, the new rate constant is:
$$k_{new} = k_{old} \times (\text{T.C.})^{\frac{\Delta T}{10}}$$

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Temperature Coefficient Scaling

**The Pattern:** You are given the T.C. and asked how much the rate increases over a larger temperature gap.

#### Solved Example 7.1
**Q:** If the rate constant of a reaction at $30^\circ\text{C}$ is $x\text{ s}^{-1}$, find the rate constant at $60^\circ\text{C}$. (Given: Temperature Coefficient = 2)<br> 🟢

**Solution:**
```
Delta T = 60 - 30 = 30°C
Number of 10° jumps = 30 / 10 = 3
k_new = k_old * (T.C.)^(Delta T / 10)
k_60 = x * (2)^3 = 8x s^{-1}
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 7.1a | A reaction's rate doubles for every $10^\circ$ rise. By what factor does it increase if temp goes from $20^\circ\text{C}$ to $70^\circ\text{C}$? | 🟢 |
| 7.1b | T.C. = 2.5 for a reaction. If temperature rises from $10^\circ\text{C}$ to $50^\circ\text{C}$, by what factor does the rate increase? | 🟢 |
| 7.1c | At $15^\circ\text{C}$, the rate constant $= 0.0015\text{ s}^{-1}$. T.C. = 2. Find $k$ at $55^\circ\text{C}$. | 🟢 |
| 7.1d | The temperature coefficient for a reaction is 3. If $k$ at $20^\circ\text{C}$ is $0.02\text{ s}^{-1}$, find $k$ at $60^\circ\text{C}$. | 🟡 |
| 7.1e | For a reaction, $k$ at $20^\circ\text{C}$ is $4.0 \times 10^{-4}\text{ s}^{-1}$ and T.C. = 2.5. Calculate $k$ at $50^\circ\text{C}$. | 🟡 |
| 7.1f | The rate of a reaction increases by 64 times when the temperature is raised from $20^\circ\text{C}$ to $80^\circ\text{C}$. Find the temperature coefficient. | 🟡 |
| 7.1g | $k$ at $25^\circ\text{C}$ is $3 \times 10^{-3}\text{ s}^{-1}$ and T.C. = 2. Determine $k$ at $95^\circ\text{C}$ and the factor increase. | 🔴 |
| 7.1h | T.C. = 1.5 and $k$ at $30^\circ\text{C}$ is $0.001\text{ s}^{-1}$. After what temperature rise does $k$ become $0.003375\text{ s}^{-1}$? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**7.1a:**
$\Delta T = 50$. Factor $= 2^{50/10} = 2^5 = 32$ times.

**7.1b:**
$\Delta T = 40^\circ\text{C}$. Factor $= (2.5)^{40/10} = (2.5)^4 = 39.0625$ times.

**7.1c:**
$\Delta T = 40^\circ\text{C}$. $k_{55} = 0.0015 \times (2)^4 = 0.0015 \times 16 = 0.024\text{ s}^{-1}$.

**7.1d:**
$\Delta T = 40^\circ\text{C}$. $k_{60} = 0.02 \times (3)^4 = 0.02 \times 81 = 1.62\text{ s}^{-1}$.

**7.1e:**
$\Delta T = 30^\circ\text{C}$. $k_{50} = 4.0 \times 10^{-4} \times (2.5)^3 = 4.0 \times 10^{-4} \times 15.625 = 6.25 \times 10^{-3}\text{ s}^{-1}$.

**7.1f:**
$64 = (\text{T.C.})^{(80-20)/10} = (\text{T.C.})^6 \implies \text{T.C.} = 64^{1/6} = 2$.

**7.1g:**
$\Delta T = 70^\circ\text{C}$. $k_{95} = 3 \times 10^{-3} \times (2)^7 = 3 \times 10^{-3} \times 128 = 0.384\text{ s}^{-1}$. Factor increase $= 128$ times.

**7.1h:**
$0.003375/0.001 = 3.375 = (1.5)^{\Delta T/10}$. $\log(3.375) = (\Delta T/10)\log(1.5)$. $\Delta T/10 = 0.5283/0.1761 = 3 \implies \Delta T = 30^\circ\text{C}$.
</details>

---

### Type 2: Arrhenius Graph Slopes

**The Pattern:** Extracting $E_a$ or $A$ from the slope of $\log k$ vs $1/T$.

#### Solved Example 7.2
**Q:** The plot of $\log k$ vs $1/T$ is a straight line with a slope of $-10000\text{ K}$. Calculate Activation Energy ($E_a$). (Given $R = 8.314\text{ J/K·mol}$) <br> 🟡

**Solution:**
```
For log k vs 1/T, Slope = -E_a / 2.303R
-10000 = -E_a / (2.303 * 8.314)
E_a = 10000 * 2.303 * 8.314
E_a = 191471 J/mol = 191.47 kJ/mol
```
> ⚠️ **Trap Alert:** Notice whether the graph is $\log$ or $\ln$. If it's $\ln$, don't use $2.303$!

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 7.2a | A plot of $\ln k$ vs $1/T$ has a slope of $-5000\text{ K}$. Find $E_a$. | 🟢 |
| 7.2b | A plot of $\log k$ vs $1/T$ has a slope of $-6000\text{ K}$. Find $E_a$. | 🟢 |
| 7.2c | The slope of $\ln k$ vs $1/T$ graph is $-8000\text{ K}$. Determine the activation energy. | 🟢 |
| 7.2d | For a reaction, $\log k$ vs $1/T$ gives a slope of $-12000\text{ K}$ and an intercept of $5$. Find $E_a$ and $A$. | 🟡 |
| 7.2e | A $\ln k$ vs $1/T$ plot passes through $(0.003, -2)$ and $(0.004, -5)$. Find $E_a$. | 🟡 |
| 7.2f | The activation energy of a reaction is $100\text{ kJ/mol}$. Find the slope of the $\ln k$ vs $1/T$ graph. | 🟡 |
| 7.2g | From a $\log k$ vs $1/T$ plot, slope $= -8000\text{ K}$ and intercept $= 8$. Find the ratio $k_{313}/k_{298}$. | 🔴 |
| 7.2h | For a reaction, $\log k$ vs $1/T$ slope $= -10900\text{ K}$. At what temperature does the rate constant double relative to its value at $300\text{ K}$? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**7.2a:**
Slope of $\ln k$ vs $1/T$ is $-E_a / R$.
$-5000 = -E_a / 8.314 \implies E_a = 5000 \times 8.314 = 41570\text{ J/mol} = 41.57\text{ kJ/mol}$.

**7.2b:**
Slope $= -E_a / 2.303R$. $-6000 = -E_a / (2.303 \times 8.314)$. $E_a = 6000 \times 2.303 \times 8.314 = 114883\text{ J/mol} = 114.88\text{ kJ/mol}$.

**7.2c:**
Slope $= -E_a / R$. $-8000 = -E_a / 8.314$. $E_a = 8000 \times 8.314 = 66512\text{ J/mol} = 66.51\text{ kJ/mol}$.

**7.2d:**
$E_a = 12000 \times 2.303 \times 8.314 = 229766\text{ J/mol} \approx 229.77\text{ kJ/mol}$. $\log A = \text{intercept} = 5 \implies A = 10^5$.

**7.2e:**
Slope $= (\Delta \ln k) / (\Delta (1/T)) = (-5 - (-2)) / (0.004 - 0.003) = -3 / 0.001 = -3000$. $-3000 = -E_a / 8.314 \implies E_a = 3000 \times 8.314 = 24942\text{ J/mol} \approx 24.94\text{ kJ/mol}$.

**7.2f:**
Slope $= -E_a / R = -100000 / 8.314 \approx -12028\text{ K}$.

**7.2g:**
$E_a = 8000 \times 2.303 \times 8.314 = 153177\text{ J/mol}$. $\log(k_{313}/k_{298}) = (E_a/2.303R)(1/298 - 1/313) = 8000 \times 0.000161 = 1.288$. $k_{313}/k_{298} = 10^{1.288} \approx 19.4$.

**7.2h:**
$E_a = 10900 \times 2.303 \times 8.314 = 208655\text{ J/mol}$. $\log(k_2/k_1) = \log 2 = (E_a/2.303R)(1/300 - 1/T_2)$. $0.3010 = (208655/19.147)(0.003333 - 1/T_2)$. $1/T_2 = 0.003306 \implies T_2 \approx 302.5\text{ K}$.
</details>

---

### Type 3: The Two-Temperature Calculation

**The Pattern:** Apply the full Arrhenius formula to find $E_a$, $k_1$, $k_2$, $T_1$, or $T_2$.

#### Solved Example 7.3
**Q:** The rate constant of a reaction increases by five times on an increase in temperature from $27^\circ\text{C}$ to $52^\circ\text{C}$. Find $E_a$ in $\text{kJ/mol}$.<br> 🔴

**Solution:**
```
T_1 = 27 + 273 = 300 K
T_2 = 52 + 273 = 325 K
k_2 / k_1 = 5

log(k_2/k_1) = (E_a / 2.303R) * [ (T_2 - T_1) / (T_1 T_2) ]
log(5) = (E_a / (2.303 * 8.314)) * [ (325 - 300) / (300 * 325) ]
0.699 = (E_a / 19.147) * [ 25 / 97500 ]
0.699 = (E_a / 19.147) * [ 1 / 3900 ]
E_a = 0.699 * 19.147 * 3900 = 52196 J/mol
E_a ≈ 52.2 kJ/mol
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 7.3a | The rate constant of a reaction doubles when temperature is raised from $300\text{ K}$ to $310\text{ K}$. Find $E_a$. | 🟢 |
| 7.3b | A reaction has $k = 0.03\text{ s}^{-1}$ at $10^\circ\text{C}$ and $k = 0.24\text{ s}^{-1}$ at $40^\circ\text{C}$. Determine $E_a$. | 🟢 |
| 7.3c | The rate constant increases 4 times when temperature is raised from $27^\circ\text{C}$ to $47^\circ\text{C}$. Calculate $E_a$. | 🟡 |
| 7.3d | $E_a = 75\text{ kJ/mol}$ and $k = 0.02\text{ s}^{-1}$ at $298\text{ K}$. Find $k$ at $313\text{ K}$. | 🟡 |
| 7.3e | $E_a = 180\text{ kJ/mol}$ and $k = 10^{-4}\text{ s}^{-1}$ at $500\text{ K}$. Find the frequency factor $A$. | 🟡 |
| 7.3f | $k = 4 \times 10^{-3}\text{ s}^{-1}$ at $300\text{ K}$ and $k = 1.2 \times 10^{-2}\text{ s}^{-1}$ at $400\text{ K}$. Determine $E_a$. | 🔴 |
| 7.3g | For a reaction, $k_1 = 2 \times 10^{-4}\text{ s}^{-1}$ at $T_1$ and $k_2 = 8 \times 10^{-4}\text{ s}^{-1}$ at $T_2 = T_1 + 20\text{ K}$. If $E_a = 55\text{ kJ/mol}$, find $T_1$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**7.3a:**
$k_2/k_1 = 2$, $T_1 = 300\text{ K}$, $T_2 = 310\text{ K}$. $\log 2 = (E_a/2.303R)[(310-300)/(300 \times 310)]$. $0.3010 = (E_a/19.147)(10/93000) = (E_a/19.147)(1/9300)$. $E_a = 0.3010 \times 19.147 \times 9300 \approx 53593\text{ J/mol} \approx 53.59\text{ kJ/mol}$.

**7.3b:**
$T_1 = 283\text{ K}$, $T_2 = 313\text{ K}$, $k_2/k_1 = 8$. $\log 8 = (E_a/2.303R)[(313-283)/(283 \times 313)]$. $0.9031 = (E_a/19.147)(30/88579)$. $E_a \approx 0.9031 \times 19.147 \times 2952.6 \approx 51040\text{ J/mol} \approx 51.04\text{ kJ/mol}$.

**7.3c:**
$T_1 = 300\text{ K}$, $T_2 = 320\text{ K}$, $k_2/k_1 = 4$. $\log 4 = (E_a/2.303R)[(320-300)/(300 \times 320)]$. $0.6021 = (E_a/19.147)(20/96000) = (E_a/19.147)(1/4800)$. $E_a = 0.6021 \times 19.147 \times 4800 \approx 55325\text{ J/mol} \approx 55.33\text{ kJ/mol}$.

**7.3d:**
$\log(k_2/0.02) = (75000/19.147)(1/298 - 1/313) = 3917.1(0.003356 - 0.003195) = 3917.1 \times 0.000161 = 0.6307$. $k_2/0.02 = 10^{0.6307} \approx 4.27$. $k_2 = 0.02 \times 4.27 = 0.0854\text{ s}^{-1}$.

**7.3e:**
$k = A e^{-E_a/RT}$. $10^{-4} = A e^{-180000/(8.314 \times 500)} = A e^{-43.30}$. $A = 10^{-4} \times e^{43.30} \approx 10^{-4} \times 6.44 \times 10^{18} = 6.44 \times 10^{14}\text{ s}^{-1}$.

**7.3f:**
$\log(0.012/0.004) = \log 3 = (E_a/2.303R)[(400-300)/(300 \times 400)]$. $0.4771 = (E_a/19.147)(100/120000) = (E_a/19.147)(1/1200)$. $E_a = 0.4771 \times 19.147 \times 1200 \approx 10962\text{ J/mol} \approx 10.96\text{ kJ/mol}$.

**7.3g:**
$k_2/k_1 = 4 = 2^{\Delta T/10} = 2^{20/10} = 4$. Using Arrhenius: $\log 4 = (55000/19.147)[20/(T_1(T_1+20))]$. $0.6021 = 2872.7 \times 20/(T_1(T_1+20))$. $T_1(T_1+20) = 57454/0.6021 \approx 95440$. $T_1^2 + 20T_1 - 95440 = 0$. Solving: $T_1 \approx 299.5\text{ K}$.
</details>

---

---

## 🔀 Stage 4: Type Mixer & Catalysis

**Catalysis Insight:** A catalyst speeds up a reaction by lowering the activation energy ($E_a$). If a catalyzed reaction at $T_1$ runs at the same rate as the uncatalyzed reaction at $T_2$, then their exponents are equal:
$\frac{E_{a(uncat)}}{T_{uncat}} = \frac{E_{a(cat)}}{T_{cat}}$

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 7.M1 | For a reaction, $E_a$ is decreased by $30\text{ kJ/mol}$ with a catalyst. If the uncatalyzed reaction at $700\text{ K}$ has the same rate as the catalyzed one at $500\text{ K}$, what is $E_{a(uncat)}$? | Catalysis | 🔴 |
| 7.M2 | T.C. = 2 for a reaction. Calculate the percentage increase in rate when temperature changes from $25^\circ\text{C}$ to $45^\circ\text{C}$. | Type 1 | 🟢 |
| 7.M3 | A $\log k$ vs $1/T$ plot has slope $= -7500\text{ K}$. If T.C. = 2, find the factor by which rate increases from $30^\circ\text{C}$ to $60^\circ\text{C}$. | Types 1, 2 | 🟡 |
| 7.M4 | $E_{a(uncat)} = 120\text{ kJ/mol}$ and a catalyst lowers it by $40\text{ kJ/mol}$. At what temperature must the uncatalyzed reaction run to match the catalyzed rate at $400\text{ K}$? | Catalysis | 🟡 |
| 7.M5 | For a reaction, $\ln k$ vs $1/T$ gives slope $= -6500\text{ K}$. A catalyst lowers $E_a$ by $20\text{ kJ/mol}$. Find the new slope of the $\ln k$ vs $1/T$ plot. | Types 2, Catalysis | 🟡 |
| 7.M6 | $k = 0.001\text{ s}^{-1}$ at $298\text{ K}$ and $k = 0.004\text{ s}^{-1}$ at $308\text{ K}$. Find the temperature coefficient and predict $k$ at $318\text{ K}$. | Types 1, 3 | 🟡 |
| 7.M7 | Two reactions have $E_{a1} = 80\text{ kJ/mol}$, $E_{a2} = 100\text{ kJ/mol}$, and $A_1 = A_2$. At what temperature is $k_1 = 5k_2$? | Type 3 | 🔴 |
| 7.M8 | The rate of a reaction doubles for every $10^\circ\text{C}$ rise. What is the approximate slope of the $\ln k$ vs $1/T$ graph at $300\text{ K}$? | Types 1, 2 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**7.M1:**
$k_{uncat} = k_{cat}$
$A e^{-E_a/R(700)} = A e^{-(E_a-30)/R(500)}$
$\frac{E_a}{700} = \frac{E_a-30}{500}$
$5 E_a = 7 (E_a - 30) \implies 5 E_a = 7 E_a - 210 \implies 2 E_a = 210 \implies E_a = 105\text{ kJ/mol}$.

**7.M2:**
$\Delta T = 20^\circ\text{C}$. Factor $= 2^{20/10} = 2^2 = 4$. Percentage increase $= (4-1) \times 100\% = 300\%$.

**7.M3:**
$E_a = 7500 \times 2.303 \times 8.314 \approx 143596\text{ J/mol} \approx 143.6\text{ kJ/mol}$. Factor from T.C.: $2^{30/10} = 2^3 = 8$ times.

**7.M4:**
$A e^{-120000/R T_{uncat}} = A e^{-80000/R(400)}$. $\frac{120000}{T_{uncat}} = \frac{80000}{400}$. $T_{uncat} = 120000 \times 400 / 80000 = 600\text{ K}$.

**7.M5:**
Original $E_a = 6500 \times 8.314 \approx 54041\text{ J/mol}$. New $E_a' = 54041 - 20000 = 34041\text{ J/mol}$. New slope $= -34041/8.314 \approx -4094\text{ K}$.

**7.M6:**
T.C. $= k_{308}/k_{298} = 0.004/0.001 = 4$. $k_{318} = 0.004 \times 4 = 0.016\text{ s}^{-1}$.

**7.M7:**
$A e^{-80000/RT} = 5 \times A e^{-100000/RT}$. $e^{20000/RT} = 5$. $\ln 5 = 20000/(8.314T)$. $T = 20000/(8.314 \times 1.6094) \approx 1495\text{ K}$.

**7.M8:**
$k_2/k_1 = 2$ for $\Delta T = 10$. $\ln 2 = (E_a/R)(1/T - 1/(T+10)) \approx (E_a/R)(10/T^2)$. At $300\text{ K}$: $E_a \approx 0.693 \times 8.314 \times 300^2 / 10 \approx 51900\text{ J/mol}$. Slope $= -E_a/R \approx -51900/8.314 \approx -6242\text{ K}$.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 7.B1 | Write the Arrhenius equation. What does $e^{-E_a/RT}$ represent? | 🟢 |
| 7.B2 | Explain the effect of a catalyst on activation energy and enthalpy of reaction. ⭐ | 🟡 |
| 7.B3 | Define temperature coefficient. What is its approximate value for most reactions? | 🟢 |
| 7.B4 | What is the frequency factor $A$ in the Arrhenius equation? What factors does it depend on? | 🟢 |
| 7.B5 | Derive the expression $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left[\frac{1}{T_1} - \frac{1}{T_2}\right]$. ⭐ | 🟡 |
| 7.B6 | Why does the temperature coefficient vary with temperature? Explain briefly. | 🟡 |
| 7.B7 | The activation energy of a reaction is $75\text{ kJ/mol}$ at $300\text{ K}$. What fraction of molecules have energy equal to or greater than $E_a$? | 🟡 |
| 7.B8 | A catalyst lowers the activation energy of a reaction from $80\text{ kJ/mol}$ to $50\text{ kJ/mol}$ at $300\text{ K}$. How many times faster is the catalyzed reaction? | 🟡 |
| 7.B9 | Compare and contrast the temperature coefficient approach with the Arrhenius equation for predicting rate changes with temperature. ⭐ | 🔴 |
| 7.B10 | At $300\text{ K}$, an uncatalyzed reaction has $k = 2 \times 10^{-4}\text{ s}^{-1}$. With a catalyst, $E_a$ drops by $30\text{ kJ/mol}$. Assuming $A$ is unchanged, find $k_{cat}$ at $300\text{ K}$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**7.B1:**
$k = A e^{-E_a/RT}$. The term $e^{-E_a/RT}$ represents the fraction of molecules having kinetic energy greater than or equal to the activation energy.

**7.B2:**
A catalyst provides an alternate pathway with a lower activation energy, thus speeding up the reaction. It lowers both forward and backward activation energies equally, so the overall enthalpy of reaction ($\Delta H$) remains unchanged.

**7.B3:**
Temperature coefficient is the ratio of rate constants at $(T+10)^\circ\text{C}$ and $T^\circ\text{C}$, i.e. $\text{T.C.} = k_{T+10}/k_T$. For most reactions, it is approximately 2 or 3.

**7.B4:**
The frequency factor $A$ represents the frequency of collisions with the proper orientation. It depends on: (i) collision frequency, (ii) steric/orientation factor. The unit of $A$ is the same as that of $k$.

**7.B5:**
From $\ln k = \ln A - E_a/RT$, write equations at $T_1$ and $T_2$: $\ln k_1 = \ln A - E_a/RT_1$ and $\ln k_2 = \ln A - E_a/RT_2$. Subtract: $\ln(k_2/k_1) = (E_a/R)(1/T_1 - 1/T_2)$. Convert to $\log_{10}$: $\log(k_2/k_1) = (E_a/2.303R)(1/T_1 - 1/T_2)$. Simplifying with common denominator gives the required expression.

**7.B6:**
T.C. is not truly constant because the Arrhenius equation $k = A e^{-E_a/RT}$ is exponential. The factor by which $k$ increases for a fixed $10^\circ\text{C}$ rise depends on the absolute temperature. At higher temperatures, the same $10^\circ\text{C}$ rise produces a smaller relative increase in $k$, so T.C. decreases slightly with increasing temperature.

**7.B7:**
Fraction $= e^{-E_a/RT} = e^{-75000/(8.314 \times 300)} = e^{-30.07} \approx 8.7 \times 10^{-14}$.

**7.B8:**
$k_{cat}/k_{uncat} = e^{-(E_{a(cat)}-E_{a(uncat)})/RT} = e^{-(50000-80000)/(8.314 \times 300)} = e^{30000/2494.2} = e^{12.03} \approx 1.67 \times 10^5$ times faster.

**7.B9:**
TC approach is empirical and approximate — it assumes a constant multiplicative factor per $10^\circ\text{C}$ rise. Arrhenius equation is theoretically derived and accurate, accounting for the exponential dependence of $k$ on $T$. TC is simpler for quick estimates but loses accuracy at extreme temperatures. Arrhenius gives precise results over any temperature range but requires knowledge of $E_a$.

**7.B10:**
$k_{uncat} = A e^{-E_a/RT} = 2 \times 10^{-4}$. $k_{cat} = A e^{-(E_a-30000)/RT} = A e^{-E_a/RT} \times e^{30000/RT} = 2 \times 10^{-4} \times e^{30000/(8.314 \times 300)}$. $k_{cat} = 2 \times 10^{-4} \times e^{12.03} = 2 \times 10^{-4} \times 1.67 \times 10^5 = 33.4\text{ s}^{-1}$.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q7.J1 🟡**
Consider plots of $\log k$ vs $1/T$ for three reactions. Line 1 is the steepest, Line 3 is the gentlest. The order of Activation Energies is:
(A) $E_{a1} > E_{a2} > E_{a3}$
(B) $E_{a3} > E_{a2} > E_{a1}$
(C) Cannot be determined

**Q7.J2 🔴 ⭐**
A catalyst lowers $E_a$ for both forward and backward reactions by $100\text{ kJ/mol}$. Which statement is correct?
(A) It alters the Gibbs energy change.
(B) It can make a non-spontaneous reaction spontaneous.
(C) Enthalpy change for the reaction remains unaltered.
(D) Equilibrium constant changes.

**Q7.J3 🟡**
For a reaction, the rate constant at $300\text{ K}$ is $0.02\text{ s}^{-1}$ and at $310\text{ K}$ is $0.04\text{ s}^{-1}$. The activation energy is approximately:
(A) $53.6\text{ kJ/mol}$
(B) $46.2\text{ kJ/mol}$
(C) $60.1\text{ kJ/mol}$
(D) $72.3\text{ kJ/mol}$

**Q7.J4 🟡**
Two Arrhenius plots ($\log k$ vs $1/T$) for reactions I and II have slopes in the ratio $3:2$. If $E_{a1} = 90\text{ kJ/mol}$, then $E_{a2}$ is:
(A) $60\text{ kJ/mol}$
(B) $45\text{ kJ/mol}$
(C) $135\text{ kJ/mol}$
(D) $30\text{ kJ/mol}$

**Q7.J5 🟢**
Which of the following does NOT affect the rate constant $k$?
(A) Temperature
(B) Activation energy
(C) Concentration of reactants
(D) Frequency factor

**Q7.J6 🔴**
A catalyst lowers the activation energy of a reaction from $150\text{ kJ/mol}$ to $100\text{ kJ/mol}$. At $400\text{ K}$, the catalyzed reaction is how many times faster?
(A) $e^{15.03}$
(B) $e^{7.52}$
(C) $e^{30.06}$
(D) $e^{3.76}$

**Q7.J7 🔴 ⭐**
The rate constant of a reaction is $1.5 \times 10^{-3}\text{ s}^{-1}$ at $298\text{ K}$ and $4.5 \times 10^{-3}\text{ s}^{-1}$ at $308\text{ K}$. The Arrhenius parameter $A$ is approximately:
(A) $1.2 \times 10^6\text{ s}^{-1}$
(B) $2.4 \times 10^8\text{ s}^{-1}$
(C) $3.6 \times 10^{10}\text{ s}^{-1}$
(D) $4.8 \times 10^{12}\text{ s}^{-1}$

**Q7.J8 🟡**
Which statement about the effect of a catalyst on the Arrhenius plot ($\ln k$ vs $1/T$) is correct?
(A) Slope increases, intercept unchanged
(B) Slope decreases, intercept unchanged
(C) Both slope and intercept decrease
(D) Both slope and intercept increase

**Q7.J9 🔴**
The temperature coefficient of a reaction is $2.5$. If the rate constant at $25^\circ\text{C}$ is $x$, what is the rate constant at $55^\circ\text{C}$?
(A) $15.625x$
(B) $7.5x$
(C) $2.5x$
(D) $12.5x$

**Q7.J10 🟡**
If a reaction has $E_a = 0$, what will be the value of $k$ at any temperature?
(A) $k = 0$
(B) $k = A$
(C) $k = A/RT$
(D) $k = e^{-A}$

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**7.J1 → Answer: (A)**
Slope $= -E_a / 2.303R$. The steeper the slope (larger negative value), the greater the magnitude of $E_a$.

**7.J2 → Answer: (C)**
A catalyst does NOT change thermodynamics. $\Delta H$, $\Delta G$, and $K_{eq}$ all remain completely unchanged.

**7.J3 → Answer: (A)**
$\log(0.04/0.02) = (E_a/2.303 \times 8.314)(10/(300 \times 310))$. $\log 2 = (E_a/19.147)(10/93000)$. $E_a = 0.3010 \times 19.147 \times 9300 \approx 53593\text{ J/mol} \approx 53.6\text{ kJ/mol}$.

**7.J4 → Answer: (A)**
Slope $\propto E_a$. $E_{a1}/E_{a2} = 3/2 \implies 90/E_{a2} = 3/2 \implies E_{a2} = 60\text{ kJ/mol}$.

**7.J5 → Answer: (C)**
$k$ depends on temperature, $E_a$, and $A$ (frequency factor). Concentration affects the rate, not the rate constant.

**7.J6 → Answer: (A)**
$k_{cat}/k_{uncat} = e^{-(E_{a(cat)}-E_{a(uncat)})/RT} = e^{-(100-150) \times 10^3/(8.314 \times 400)} = e^{50000/3325.6} = e^{15.03}$.

**7.J7 → Answer: (C)**
$\log(4.5/1.5) = \log 3 = (E_a/19.147)(10/(298 \times 308))$. $0.4771 = (E_a/19.147)(10/91784)$. $E_a \approx 83807\text{ J/mol}$. Then $\log A = \log k + E_a/(2.303RT) = \log(1.5\times10^{-3}) + 83807/(19.147 \times 298)$. $\log A = -2.824 + 14.68 = 11.856$. $A \approx 7.2 \times 10^{11}\text{ s}^{-1}$.

**7.J8 → Answer: (B)**
Catalyst lowers $E_a$, so slope $= -E_a/R$ becomes less negative (decreases in magnitude). The intercept $\ln A$ is unaffected.

**7.J9 → Answer: (A)**
$\Delta T = 30^\circ\text{C}$. $k_{55} = x \times (2.5)^{30/10} = x \times (2.5)^3 = 15.625x$.

**7.J10 → Answer: (B)**
$k = A e^{-0/RT} = A e^0 = A$. So $k = A$ at all temperatures.
</details>

---

## 🧠 Stage 7: Assertion-Reasoning

| # | Question | Difficulty |
|---|----------|------------|
| 7.S1 | **Assertion (A):** The rate of reaction increases with an increase in temperature.<br>**Reason (R):** The number of effective collisions increases. | 🟢 |
| 7.S2 | **Assertion (A):** A catalyst does not alter the equilibrium constant of a reaction.<br>**Reason (R):** It catalyzes both forward and backward reactions to the same extent. | 🟡 |
| 7.S3 | **Assertion (A):** A catalyst increases the rate of reaction.<br>**Reason (R):** A catalyst provides an alternative pathway with a lower activation energy. | 🟢 |
| 7.S4 | **Assertion (A):** The plot of $\ln k$ vs $1/T$ is a straight line.<br>**Reason (R):** Activation energy and frequency factor are constant for a given reaction. | 🟡 |
| 7.S5 | **Assertion (A):** Activation energy is independent of temperature.<br>**Reason (R):** The Arrhenius equation includes temperature in the exponential term. | 🟡 |
| 7.S6 | **Assertion (A):** The value of $\log k$ decreases as $1/T$ increases.<br>**Reason (R):** The slope of $\log k$ vs $1/T$ is negative. | 🟢 |
| 7.S7 | **Assertion (A):** A reaction with higher $E_a$ is more sensitive to temperature changes.<br>**Reason (R):** The slope of the $\ln k$ vs $1/T$ graph is steeper for larger $E_a$. | 🔴 |
| 7.S8 | **Assertion (A):** The temperature coefficient of a reaction is always 2.<br>**Reason (R):** For every $10^\circ\text{C}$ rise, the rate of every reaction doubles. | 🟡 |
| 7.S9 | **Assertion (A):** A catalyst speeds up only the forward reaction.<br>**Reason (R):** A catalyst lowers only the forward activation energy. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**7.S1 → Answer: (A)**
Both are true and R is the correct explanation. Higher temp = larger fraction of molecules with $E \ge E_a$ = more effective collisions.

**7.S2 → Answer: (A)**
Both are true and R is the correct explanation. By lowering the activation energy barrier for both directions by the exact same amount, the rates of both increase proportionally, leaving the ratio (equilibrium constant) unchanged.

**7.S3 → Answer: (A)**
Both A and R are true, and R is the correct explanation. A catalyst provides an alternative pathway with a lower $E_a$, thereby increasing the rate.

**7.S4 → Answer: (A)**
Both A and R are true, and R is the correct explanation. Constant $E_a$ and $A$ give the linear form $\ln k = \ln A - E_a/RT$, which is $y = c + mx$ with $x = 1/T$.

**7.S5 → Answer: (B)**
A is true (for a given reaction, $E_a$ is approximately constant), but R does not correctly explain A. The presence of $T$ in the Arrhenius equation does not make $E_a$ itself temperature-dependent.

**7.S6 → Answer: (A)**
Both A and R are true, and R is the correct explanation. $\log k = \log A - (E_a/2.303R)(1/T)$. As $1/T$ increases, the negative term grows, so $\log k$ decreases.

**7.S7 → Answer: (A)**
Both A and R are true, and R is the correct explanation. Slope $= -E_a/R$, so higher $E_a$ gives a steeper negative slope, meaning $k$ changes more rapidly with $T$.

**7.S8 → Answer: (D)**
A is false — T.C. varies between approximately 2 and 3 depending on the reaction. R is also false — not every reaction doubles its rate for a $10^\circ\text{C}$ rise.

**7.S9 → Answer: (D)**
A is false — a catalyst speeds up both forward and backward reactions equally. R is also false — a catalyst lowers $E_a$ for both directions by the same amount.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Q7.M1 🟢**
Which of the following statements about the Arrhenius equation is NOT correct?
(A) $k = A e^{-E_a/RT}$
(B) $A$ is temperature-dependent
(C) $E_a$ is the activation energy
(D) $R$ is the gas constant

**Q7.M2 🟢**
As temperature approaches infinity ($T \to \infty$), the rate constant $k$ approaches:
(A) $0$
(B) $A$
(C) $\infty$
(D) $E_a/R$

**Q7.M3 🟡**
For a plot of $\log k$ vs $1/T$, the slope is:
(A) $-E_a/R$
(B) $-E_a/2.303R$
(C) $-2.303E_a/R$
(D) $-R/E_a$

**Q7.M4 🟡**
The fraction of molecules with energy $\ge 50\text{ kJ/mol}$ at $300\text{ K}$ is approximately:
(A) $2.0 \times 10^{-9}$
(B) $4.0 \times 10^{-8}$
(C) $1.0 \times 10^{-5}$
(D) $3.0 \times 10^{-12}$

**Q7.M5 🟡**
The slope of $\log k$ vs $1/T$ plot for a reaction is $-10000\text{ K}$. The activation energy is:
(A) $83.14\text{ kJ/mol}$
(B) $191.47\text{ kJ/mol}$
(C) $100.00\text{ kJ/mol}$
(D) $41.57\text{ kJ/mol}$

**Q7.M6 🔴**
Which of the following statements about a catalyst is correct?
(A) It increases the enthalpy change of the reaction.
(B) It is consumed during the reaction.
(C) It lowers the activation energy equally for forward and backward reactions.
(D) It increases the equilibrium constant.

**Q7.M7 🔴**
For a reaction, $k = 2 \times 10^{-3}\text{ s}^{-1}$ at $300\text{ K}$ and $k = 8 \times 10^{-3}\text{ s}^{-1}$ at $320\text{ K}$. The activation energy is approximately:
(A) $38.4\text{ kJ/mol}$
(B) $55.3\text{ kJ/mol}$
(C) $72.6\text{ kJ/mol}$
(D) $41.2\text{ kJ/mol}$

**Q7.M8 🔴**
Two reactions have $E_{a1} = 60\text{ kJ/mol}$ and $E_{a2} = 80\text{ kJ/mol}$. At $400\text{ K}$, the ratio $k_1/k_2$ (assuming $A_1 = A_2$) is:
(A) $e^{6.01}$
(B) $e^{3.01}$
(C) $e^{12.02}$
(D) $e^{1.50}$

**Q7.M9 🟡**
For a first-order reaction with $A = 10^{12}\text{ s}^{-1}$ and $E_a = 180\text{ kJ/mol}$, the rate constant at $500\text{ K}$ is approximately:
(A) $1.2 \times 10^{-7}\text{ s}^{-1}$
(B) $2.5 \times 10^{-6}\text{ s}^{-1}$
(C) $3.8 \times 10^{-8}\text{ s}^{-1}$
(D) $4.0 \times 10^{-5}\text{ s}^{-1}$

<details>
<summary>💡 Full Solutions — MCQ Mastery</summary>

**Q7.M1 → Answer: (B)**
$A$ is assumed to be approximately constant (temperature-independent) over moderate temperature ranges. All other statements are true.

**Q7.M2 → Answer: (B)**
As $T \to \infty$, $e^{-E_a/RT} \to e^0 = 1$, so $k \to A$.

**Q7.M3 → Answer: (B)**
$\log k = \log A - E_a/(2.303RT)$, so slope $= -E_a/2.303R$.

**Q7.M4 → Answer: (A)**
Fraction $= e^{-E_a/RT} = e^{-50000/(8.314 \times 300)} = e^{-20.05} \approx 2.0 \times 10^{-9}$.

**Q7.M5 → Answer: (B)**
$E_a = 10000 \times 2.303 \times 8.314 = 191471\text{ J/mol} \approx 191.47\text{ kJ/mol}$.

**Q7.M6 → Answer: (C)**
A catalyst lowers $E_a$ equally for forward and backward reactions. It does not change $\Delta H$, $\Delta G$, or $K_{eq}$, and is not consumed.

**Q7.M7 → Answer: (B)**
$\log(8/2) = \log 4 = (E_a/2.303R)[(320-300)/(300 \times 320)]$. $0.6021 = (E_a/19.147)(20/96000)$. $E_a = 0.6021 \times 19.147 \times 4800 \approx 55325\text{ J/mol} \approx 55.3\text{ kJ/mol}$.

**Q7.M8 → Answer: (A)**
$k_1/k_2 = e^{-(E_{a1}-E_{a2})/RT} = e^{-(60000-80000)/(8.314 \times 400)} = e^{20000/3325.6} = e^{6.01}$.

**Q7.M9 → Answer: (A)**
$k = A e^{-E_a/RT} = 10^{12} \times e^{-180000/(8.314 \times 500)} = 10^{12} \times e^{-43.30} = 10^{12} \times 1.2 \times 10^{-19} \approx 1.2 \times 10^{-7}\text{ s}^{-1}$.
</details>
