# Chapter 8: Activation Energy & Energy Profiles<br>
## Part IV — Temperature & Catalysis

---

## 🎯 Stage 1: The Core Idea

### The Scene

Imagine you are trying to push a heavy boulder over a hill to get it to roll down into a valley on the other side. The boulder is already some distance up the mountain, but you still have to push it up to the very peak before gravity takes over. 

In a chemical reaction, the reactants are the boulder. They already possess some internal energy, but to transform into products, they must cross a high-energy mountain peak. 

This peak is the **Transition State** (or Activated Complex). The total energy required to reach this peak from the ground is the **Threshold Energy**. The *extra* energy you need to push the reactants from their current energy level to the peak is the **Activation Energy ($E_a$)**.

> **Activation Energy ($E_a$)** is the extra minimum energy required by the reactant molecules to form the activated complex and convert into products.

### Who's Who: The Energy Terms

| Term | Symbol | Meaning | Memory Hook |
|------|--------|---------|-------------|
| **Threshold Energy** | $E_T$ | Total minimum energy needed for effective collision | "Total Height" of the mountain from sea level |
| **Activation Energy** | $E_a$ | Extra energy supplied to reactants | "Added Energy" from the starting point |
| **Enthalpy Change** | $\Delta H$ | Energy difference between Products and Reactants | "Height Difference" between start and finish |

**Rule 1:** $E_T = E_R + E_a$ (Threshold = Reactant Energy + Activation Energy)
**Rule 2:** The lower the activation energy, the faster the reaction (kinetically favorable).
**Rule 3:** The lower the product energy, the more stable the product (thermodynamically favorable).

> ⚠️ **Classic Trap:** A reaction can be highly exothermic (very stable products) but extremely slow if its activation energy peak is huge. Diamond turning into graphite is thermodynamically favorable but kinetically dead because the $E_a$ mountain is impossibly high at room temperature!

### The Two Mountain Profiles: Exothermic vs Endothermic

| Feature | Exothermic Reaction ($\Delta H < 0$) | Endothermic Reaction ($\Delta H > 0$) |
|:---:|:---:|:---:|
| **Energy Levels** | Reactants > Products | Products > Reactants |
| **Activation Energies** | $(E_a)_f < (E_a)_b$ | $(E_a)_f > (E_a)_b$ |
| **Net Result** | Heat is released | Heat is absorbed |

---

## 🔬 Stage 2: The Formula Lab

### Formula 1: The Threshold Equation

```
Threshold Energy = Energy of Reactants + Activation Energy (forward)
E_T = E_R + (E_a)_f
```
Also, for the reverse reaction:
```
E_T = E_P + (E_a)_b
```
*(where $E_P$ is Energy of Products, and $(E_a)_b$ is Activation Energy for backward reaction)*

### Formula 2: Enthalpy of Reaction ($\Delta H$)

The heat of reaction is simply the difference between the forward and backward activation energies.

```
ΔH = (E_a)_f - (E_a)_b
```
> **⚠️ Trap Alert:** Always do Forward minus Backward!
> - If $(E_a)_f < (E_a)_b$, $\Delta H$ is negative (Exothermic).
> - If $(E_a)_f > (E_a)_b$, $\Delta H$ is positive (Endothermic).

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Calculating $\Delta H$ from Activation Energies

**The Pattern:** You are given the activation energy for the forward and backward reactions. Find $\Delta H$ and determine if it's exothermic or endothermic.

#### Solved Example 8.1
**Q:** The activation energy for a forward reaction is $60 \text{ kJ mol}^{-1}$ and for the backward reaction is $80 \text{ kJ mol}^{-1}$. Calculate the enthalpy of the reaction and state its nature. 🟢

**Solution:**
```
Given:
(E_a)_f = 60 kJ/mol
(E_a)_b = 80 kJ/mol

Formula: ΔH = (E_a)_f - (E_a)_b
ΔH = 60 - 80 = -20 kJ/mol

Since ΔH is negative, the reaction is EXOTHERMIC.

Answer: -20 kJ/mol, Exothermic.
```

**Why this works:** The backward mountain is taller than the forward mountain, meaning the products sit in a deeper valley than the reactants. Heat was lost to reach that valley.

#### Solved Example 8.2
**Q:** An endothermic reaction $A \rightarrow B$ has an activation energy of $50 \text{ kJ mol}^{-1}$. If the heat of reaction is $20 \text{ kJ mol}^{-1}$, what is the activation energy of the backward reaction? 🟡

**Solution:**
```
Given:
(E_a)_f = 50 kJ/mol
ΔH = +20 kJ/mol (Endothermic means positive ΔH!)

Formula: ΔH = (E_a)_f - (E_a)_b
20 = 50 - (E_a)_b
(E_a)_b = 50 - 20 = 30 kJ/mol

Answer: 30 kJ/mol
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 8.1a | For a reaction, $(E_a)_f = 45 \text{ kJ/mol}$ and $(E_a)_b = 25 \text{ kJ/mol}$. Find $\Delta H$. | 🟢 |
| 8.1b | An exothermic reaction has $\Delta H = -40 \text{ kJ/mol}$. If $(E_a)_f$ is $30 \text{ kJ/mol}$, find $(E_a)_b$. | 🟡 |
| 8.1c | For an elementary reaction, the threshold energy is $100 \text{ kJ}$. The reactant energy is $40 \text{ kJ}$ and product energy is $20 \text{ kJ}$. Find $(E_a)_f$, $(E_a)_b$, and $\Delta H$. | 🟡 |
| 8.1d | If $(E_a)_f = (E_a)_b$, what is the value of $\Delta H$? | 🟢 |
| 8.1e | For a reaction, $(E_a)_f = 80 \text{ kJ/mol}$ and $(E_a)_b = 50 \text{ kJ/mol}$. Find $\Delta H$ and state the reaction type. | 🟢 |
| 8.1f | An endothermic reaction has $\Delta H = +25 \text{ kJ/mol}$. If $(E_a)_b = 35 \text{ kJ/mol}$, find $(E_a)_f$. | 🟡 |
| 8.1g | The threshold energy of a reaction is $180 \text{ kJ/mol}$. Reactant energy is $60 \text{ kJ/mol}$ and product energy is $40 \text{ kJ/mol}$. Find $(E_a)_f$ and $(E_a)_b$. | 🟡 |
| 8.1h | The backward activation energy is three times the forward activation energy. If $\Delta H = -40 \text{ kJ/mol}$, find $(E_a)_f$ and $(E_a)_b$. | 🔴 |
| 8.1i | For $A \rightarrow B$, $(E_a)_f = 75 \text{ kJ/mol}$ and $(E_a)_b = 95 \text{ kJ/mol}$. If $E_R = 50 \text{ kJ/mol}$, find (i) threshold energy (ii) $\Delta H$ (iii) $E_P$. | 🔴 |
| 8.1j | In an endothermic reaction, $(E_a)_b = 40 \text{ kJ/mol}$ and $\Delta H = 30 \text{ kJ/mol}$. If $E_R = 25 \text{ kJ/mol}$, find (i) $(E_a)_f$ (ii) threshold energy (iii) $E_P$. | 🔴 |
| 8.1k | If $(E_a)_f = 2(E_a)_b$ and $\Delta H = 30 \text{ kJ/mol}$, find $(E_a)_f$ and $(E_a)_b$. What will $(E_a)_b$ become if a catalyst lowers $(E_a)_f$ by $10 \text{ kJ/mol}$? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**8.1a:**
- $\Delta H = (E_a)_f - (E_a)_b = 45 - 25 = +20 \text{ kJ/mol}$ (Endothermic)

**8.1b:**
- $\Delta H = (E_a)_f - (E_a)_b$
- $-40 = 30 - (E_a)_b \implies (E_a)_b = 70 \text{ kJ/mol}$

**8.1c:**
- $(E_a)_f = E_T - E_R = 100 - 40 = 60 \text{ kJ}$
- $(E_a)_b = E_T - E_P = 100 - 20 = 80 \text{ kJ}$
- $\Delta H = (E_a)_f - (E_a)_b = 60 - 80 = -20 \text{ kJ}$ (or $E_P - E_R = 20 - 40 = -20 \text{ kJ}$)

**8.1d:**
- $\Delta H = 0 \text{ kJ/mol}$ (Isothermic reaction, neither exo nor endo)

**8.1e:**
- $\Delta H = 80 - 50 = +30 \text{ kJ/mol}$ (Endothermic)

**8.1f:**
- $\Delta H = (E_a)_f - (E_a)_b \implies 25 = (E_a)_f - 35 \implies (E_a)_f = 60 \text{ kJ/mol}$

**8.1g:**
- $(E_a)_f = E_T - E_R = 180 - 60 = 120 \text{ kJ/mol}$
- $(E_a)_b = E_T - E_P = 180 - 40 = 140 \text{ kJ/mol}$
- $\Delta H = 120 - 140 = -20 \text{ kJ/mol}$ (Exothermic)

**8.1h:**
- Let $(E_a)_f = x$, then $(E_a)_b = 3x$. $\Delta H = x - 3x = -2x = -40$.
- $x = 20$. So $(E_a)_f = 20 \text{ kJ/mol}$, $(E_a)_b = 60 \text{ kJ/mol}$.

**8.1i:**
- (i) $E_T = E_R + (E_a)_f = 50 + 75 = 125 \text{ kJ/mol}$
- (ii) $\Delta H = 75 - 95 = -20 \text{ kJ/mol}$
- (iii) $E_P = E_T - (E_a)_b = 125 - 95 = 30 \text{ kJ/mol}$ (or $E_P = E_R + \Delta H = 50 - 20 = 30 \text{ kJ/mol}$)

**8.1j:**
- (i) $\Delta H = (E_a)_f - (E_a)_b \implies 30 = (E_a)_f - 40 \implies (E_a)_f = 70 \text{ kJ/mol}$
- (ii) $E_T = E_R + (E_a)_f = 25 + 70 = 95 \text{ kJ/mol}$
- (iii) $E_P = E_T - (E_a)_b = 95 - 40 = 55 \text{ kJ/mol}$

**8.1k:**
- Let $(E_a)_b = x$, then $(E_a)_f = 2x$. $\Delta H = 2x - x = x = 30$.
- So $(E_a)_b = 30 \text{ kJ/mol}$, $(E_a)_f = 60 \text{ kJ/mol}$.
- Catalyst lowers both equally by $10 \text{ kJ/mol}$. New $(E_a)_b = 30 - 10 = 20 \text{ kJ/mol}$.
</details>

---

### Type 2: Interpreting Energy Profile Diagrams

**The Pattern:** You are given a graph or asked to describe features of the energy coordinate graph.

#### Solved Example 8.3
**Q:** Reactant A converts to Product B. The potential energy of A is $30 \text{ kJ/mol}$ and B is $70 \text{ kJ/mol}$. The activation energy of the forward reaction is $60 \text{ kJ/mol}$. What is the threshold energy of the reaction? 🟢

**Solution:**
```
Formula: E_T = E_R + (E_a)_f
Given: E_R (Energy of Reactant A) = 30 kJ/mol
(E_a)_f = 60 kJ/mol

E_T = 30 + 60 = 90 kJ/mol

Answer: 90 kJ/mol
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 8.2a | An energy profile shows Reactants at $50 \text{ kJ}$ and the peak at $120 \text{ kJ}$. What is $(E_a)_f$? | 🟢 |
| 8.2b | In the same profile, if Products are at $20 \text{ kJ}$, what is $(E_a)_b$? | 🟢 |
| 8.2c | A reaction profile has an activation energy of $80 \text{ kJ}$ and a backward activation energy of $120 \text{ kJ}$. Is the product more thermodynamically stable than the reactant? | 🟡 |
| 8.2d | In an energy profile diagram, if $(E_a)_f = 35 \text{ kJ/mol}$ and $(E_a)_b = 55 \text{ kJ/mol}$, what type of reaction is it? | 🟢 |
| 8.2e | The peak of an energy diagram is at $150 \text{ kJ}$, reactants at $60 \text{ kJ}$, and products at $30 \text{ kJ}$. Calculate $(E_a)_f$, $(E_a)_b$, $\Delta H$, and identify the reaction type. | 🟡 |
| 8.2f | For a reaction, the transition state energy is $200 \text{ kJ/mol}$. Reactants have $80 \text{ kJ/mol}$ and products have $120 \text{ kJ/mol}$. Which reaction (forward or backward) has a lower $(E_a)$? | 🟡 |
| 8.2g | A catalyst reduces the peak of an energy profile from $180 \text{ kJ}$ to $140 \text{ kJ}$. If $E_R = 60 \text{ kJ}$ and $E_P = 90 \text{ kJ}$, find the new $(E_a)_f$ and $(E_a)_b$. | 🟡 |
| 8.2h | Is it possible for a reaction to have $(E_a)_f < (E_a)_b$ but products at a higher energy than reactants? Explain. | 🔴 |
| 8.2i | Two reactions share the same reactants ($E_R = 40 \text{ kJ}$) and same peak ($120 \text{ kJ}$). Reaction A has $E_P = 20 \text{ kJ}$, Reaction B has $E_P = 80 \text{ kJ}$. Which is more exothermic? Which has a higher $(E_a)_b$? | 🔴 |
| 8.2j | The threshold energy is $100 \text{ kJ}$ above the reactants. A catalyst lowers the transition state by $25\%$. Original $(E_a)_f = 80 \text{ kJ}$ and $E_R = 20 \text{ kJ}$. Find the new $(E_a)_f$. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**8.2a:**
- $(E_a)_f = \text{Peak} - \text{Reactants} = 120 - 50 = 70 \text{ kJ}$

**8.2b:**
- $(E_a)_b = \text{Peak} - \text{Products} = 120 - 20 = 100 \text{ kJ}$

**8.2c:**
- $\Delta H = 80 - 120 = -40 \text{ kJ}$. The reaction is exothermic.
- Since products have lower energy than reactants, **Yes, the product is more thermodynamically stable.** Lower energy = greater stability.

**8.2d:**
- $\Delta H = 35 - 55 = -20 \text{ kJ/mol}$ (Exothermic)

**8.2e:**
- $(E_a)_f = 150 - 60 = 90 \text{ kJ}$
- $(E_a)_b = 150 - 30 = 120 \text{ kJ}$
- $\Delta H = 90 - 120 = -30 \text{ kJ}$ (Exothermic)

**8.2f:**
- $(E_a)_f = 200 - 80 = 120 \text{ kJ/mol}$
- $(E_a)_b = 200 - 120 = 80 \text{ kJ/mol}$
- The **backward** reaction has lower $E_a$ ($80 < 120$).

**8.2g:**
- New $(E_a)_f = 140 - 60 = 80 \text{ kJ}$
- New $(E_a)_b = 140 - 90 = 50 \text{ kJ}$

**8.2h:**
- **No, it is impossible.** $(E_a)_f < (E_a)_b \implies \Delta H = (E_a)_f - (E_a)_b < 0$, which means the reaction is exothermic. For an exothermic reaction, products MUST be at lower energy than reactants, not higher.

**8.2i:**
- Reaction A: $(E_a)_b = 120 - 20 = 100 \text{ kJ}$, $\Delta H_A = 80 - 100 = -20 \text{ kJ}$
- Reaction B: $(E_a)_b = 120 - 80 = 40 \text{ kJ}$, $\Delta H_B = 80 - 40 = +40 \text{ kJ}$
- **Reaction A** is more exothermic ($-20 < +40$). **Reaction A** has a higher $(E_a)_b$ ($100 > 40$).

**8.2j:**
- Original $E_T = E_R + (E_a)_f = 20 + 80 = 100 \text{ kJ}$
- Catalyst lowers transition state by $25\%$: New $E_T = 100 \times 0.75 = 75 \text{ kJ}$
- New $(E_a)_f = 75 - 20 = 55 \text{ kJ}$
</details>

---

## 🔀 Stage 4: Type Mixer

These problems combine energy profile reading, enthalpy calculations, and conceptual traps.

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 8.M1 | The threshold energy of a reaction is $250 \text{ kJ/mol}$. The average kinetic energy of the reactants is $100 \text{ kJ/mol}$ and that of products is $150 \text{ kJ/mol}$. Calculate (a) $(E_a)_f$, (b) $(E_a)_b$, and (c) state if it's endothermic or exothermic. | T1 + T2 | 🟡 |
| 8.M2 | For $X \rightarrow Y$, $(E_a)_f = 40 \text{ kJ/mol}$ and $\Delta H = -30 \text{ kJ/mol}$. If a catalyst lowers the threshold energy by $15 \text{ kJ/mol}$, what will be the new $(E_a)_b$? | T1 + T2 | 🔴 |
| 8.M3 | A reaction has $(E_a)_f = 85 \text{ kJ/mol}$ and $(E_a)_b = 55 \text{ kJ/mol}$. $E_R = 40 \text{ kJ/mol}$. Find (a) $\Delta H$, (b) $E_T$, (c) $E_P$, (d) reaction type. | T1 + T2 | 🟡 |
| 8.M4 | For $X \rightarrow Y$, $E_T = 140 \text{ kJ/mol}$. A catalyst lowers $E_T$ by $25 \text{ kJ/mol}$. $E_R = 50 \text{ kJ/mol}$. Original $(E_a)_b = 70 \text{ kJ/mol}$. Find (a) original $\Delta H$, (b) new $(E_a)_f$, (c) new $\Delta H$. | T1 + T2 | 🟡 |
| 8.M5 | For an endothermic reaction, $\Delta H = 40 \text{ kJ}$. $(E_a)_f$ is three times $(E_a)_b$. Find $(E_a)_f$ and $(E_a)_b$. | T1 | 🔴 |
| 8.M6 | Reaction 1: $A \rightarrow B$, $(E_a)_f = 50 \text{ kJ}$, $(E_a)_b = 70 \text{ kJ}$. Reaction 2: $C \rightarrow D$, $(E_a)_f = 80 \text{ kJ}$, $(E_a)_b = 50 \text{ kJ}$. $E_R = 30 \text{ kJ}$ for both. (a) Which is exothermic? (b) Which has higher $E_T$? (c) Which product is more stable? | T1 + T2 | 🔴 |
| 8.M7 | A student says: "In an exothermic reaction, the backward reaction needs less energy than the forward reaction." Is the student correct? Support your answer with a numerical example. | T1 + T2 | 🟡 |
| 8.M8 | For a reaction, $(E_a)_f = (E_a)_b = 60 \text{ kJ/mol}$ and $E_R = 40 \text{ kJ/mol}$. (a) Can $\Delta H$ be non-zero? Explain. (b) Find $E_T$. (c) Find $E_P$ and verify $\Delta H = 0$ using two methods. | T1 + T2 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**8.M1:**
- **(a)** $(E_a)_f = E_T - E_R = 250 - 100 = 150 \text{ kJ/mol}$
- **(b)** $(E_a)_b = E_T - E_P = 250 - 150 = 100 \text{ kJ/mol}$
- **(c)** $\Delta H = 150 - 100 = +50 \text{ kJ/mol} \rightarrow$ **Endothermic**

**8.M2:**
- Originally: $-30 = 40 - (E_a)_b \implies (E_a)_b = 70 \text{ kJ/mol}$.
- A catalyst lowers the peak (threshold energy) by $15$. This drops BOTH $(E_a)_f$ and $(E_a)_b$ by $15$.
- New $(E_a)_b = 70 - 15 = 55 \text{ kJ/mol}$.
- *(Note: $\Delta H$ remains $-30$ because $25 - 55 = -30$!)*

**8.M3:**
- (a) $\Delta H = 85 - 55 = +30 \text{ kJ/mol}$
- (b) $E_T = E_R + (E_a)_f = 40 + 85 = 125 \text{ kJ/mol}$
- (c) $E_P = E_T - (E_a)_b = 125 - 55 = 70 \text{ kJ/mol}$ (or $E_P = E_R + \Delta H = 40 + 30 = 70 \text{ kJ/mol}$)
- (d) $\Delta H > 0$, so **Endothermic**

**8.M4:**
- (a) Original $(E_a)_f = E_T - E_R = 140 - 50 = 90 \text{ kJ/mol}$. $\Delta H = 90 - 70 = +20 \text{ kJ/mol}$
- (b) New $E_T = 140 - 25 = 115 \text{ kJ/mol}$. New $(E_a)_f = 115 - 50 = 65 \text{ kJ/mol}$
- (c) New $\Delta H$ = unchanged = $+20 \text{ kJ/mol}$ (catalyst does not change $\Delta H$)

**8.M5:**
- Let $(E_a)_b = x$, then $(E_a)_f = 3x$. $\Delta H = 3x - x = 2x = 40$.
- $x = 20$. So $(E_a)_f = 60 \text{ kJ/mol}$, $(E_a)_b = 20 \text{ kJ/mol}$.

**8.M6:**
- (a) Reaction 1: $\Delta H = 50 - 70 = -20 \text{ kJ}$ (Exothermic). Reaction 2: $\Delta H = 80 - 50 = +30 \text{ kJ}$ (Endothermic). **Reaction 1 is exothermic.**
- (b) $E_T$ for R1 = $30 + 50 = 80 \text{ kJ}$. $E_T$ for R2 = $30 + 80 = 110 \text{ kJ}$. **Reaction 2** has higher $E_T$.
- (c) $E_P$ for R1 = $80 - 70 = 10 \text{ kJ}$. $E_P$ for R2 = $110 - 50 = 60 \text{ kJ}$. **Reaction 1** product is more stable (lower energy).

**8.M7:**
- The student is **INCORRECT**. In an exothermic reaction, the products sit in a lower energy valley. To climb back to the peak, the backward reaction needs MORE energy.
- Example: Take $(E_a)_f = 40 \text{ kJ/mol}$, $\Delta H = -30 \text{ kJ/mol}$. $(E_a)_b = (E_a)_f - \Delta H = 40 - (-30) = 70 \text{ kJ/mol}$, which is greater than $40$.

**8.M8:**
- (a) **No.** Since $\Delta H = (E_a)_f - (E_a)_b = 60 - 60 = 0$, $\Delta H$ must be zero.
- (b) $E_T = E_R + (E_a)_f = 40 + 60 = 100 \text{ kJ/mol}$
- (c) Method 1: $E_P = E_T - (E_a)_b = 100 - 60 = 40 \text{ kJ/mol}$. Method 2: $E_P = E_R + \Delta H = 40 + 0 = 40 \text{ kJ/mol}$. Both give $\Delta H = E_P - E_R = 0$. Verified.
</details>

---

## 📋 Stage 5: Board Arsenal

**NCERT & Board-style questions. Score these every exam.**

| # | Question | Difficulty |
|---|----------|------------|
| 8.B1 | Define activation energy of a reaction. | 🟢 |
| 8.B2 | Draw a labeled potential energy profile for an exothermic reaction showing $E_a$ and $\Delta H$. | 🟢 |
| 8.B3 | What is the relationship between the activation energy of the forward reaction, the backward reaction, and the enthalpy of reaction? | 🟢 |
| 8.B4 | Why do some thermodynamically highly spontaneous reactions not occur at room temperature? | 🟡 |
| 8.B5 | The activation energy for the reaction $2HI(g) \rightarrow H_2(g) + I_2(g)$ is $209.5 \text{ kJ mol}^{-1}$ at $581 \text{ K}$. Explain what this signifies. ⭐ | 🟡 |
| 8.B6 | What is the relationship between threshold energy, activation energy, and the energy of reactants? | 🟢 |
| 8.B7 | An exothermic reaction has $(E_a)_f = 50 \text{ kJ/mol}$ and $\Delta H = -30 \text{ kJ/mol}$. Draw and label the energy profile diagram marking $(E_a)_f$, $(E_a)_b$, and $\Delta H$. | 🟡 |
| 8.B8 | Explain why a catalyst increases the rate of both forward and backward reactions equally. How does this affect the equilibrium constant? | 🟡 |
| 8.B9 | For a reversible reaction, $(E_a)_f = 70 \text{ kJ/mol}$ and $(E_a)_b = 90 \text{ kJ/mol}$. Calculate $\Delta H$. Will an increase in temperature favor the forward or backward reaction? | 🟡 |
| 8.B10 | A two-step reaction $A \rightarrow B \rightarrow C$ has step 1 with $E_a = 85 \text{ kJ/mol}$ and step 2 with $E_a = 45 \text{ kJ/mol}$. Overall $\Delta H = -30 \text{ kJ/mol}$. (a) Identify the RDS. (b) If step 1 has $\Delta H_1 = +25 \text{ kJ/mol}$, find $(E_a)_b$ for step 1. (c) Which is more stable: B or C? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**8.B1:**
- Activation energy is the minimum extra amount of energy absorbed by the reactant molecules so that their energy becomes equal to the threshold energy, enabling them to form the activated complex.

**8.B2:**
- Draw a curve starting at a higher energy level (Reactants), going over a peak (Transition State), and dropping to a lower energy level (Products).
- Label the peak minus Reactant level as $(E_a)_f$.
- Label the Reactant level minus Product level as $\Delta H$.

**8.B3:**
- $\Delta H = (E_a)_f - (E_a)_b$
- The enthalpy of the reaction is the difference between the activation energies of the forward and backward reactions.

**8.B4:**
- Some highly spontaneous reactions (like the burning of coal or graphite turning to diamond) have extremely high activation energies. At room temperature, practically no molecules have enough kinetic energy to cross this massive barrier, making the reaction kinetically frozen.

**8.B5:**
- It signifies that for one mole of $2HI$ to decompose into $H_2$ and $I_2$, the reactant molecules must collectively absorb $209.5 \text{ kJ}$ of energy to overcome the energy barrier and form the transition state. Below this energy, effective collisions will not result in a reaction.

**8.B6:**
- $E_T = E_R + (E_a)_f$. Threshold energy is the sum of reactant energy and the forward activation energy.

**8.B7:**
- $\Delta H = (E_a)_f - (E_a)_b \implies -30 = 50 - (E_a)_b \implies (E_a)_b = 80 \text{ kJ/mol}$.
- Diagram: Start at Reactants (level = $E_R$), peak at $E_R + 50$, drop to Products at $E_R - 30$.
- Label $(E_a)_f = 50$ (Reactants to peak), $(E_a)_b = 80$ (Products to peak), $\Delta H = -30$ (Products - Reactants).

**8.B8:**
- A catalyst provides an alternative pathway with a lower activation energy for both forward and backward reactions, reducing $(E_a)_f$ and $(E_a)_b$ by the same amount.
- Since $\Delta H = (E_a)_f - (E_a)_b$ remains unchanged, the equilibrium constant $K$ is also unchanged (thermodynamics unaffected). Only the rate of attainment of equilibrium increases.

**8.B9:**
- $\Delta H = 70 - 90 = -20 \text{ kJ/mol}$ (Exothermic).
- Increasing temperature favors the **backward** (endothermic) reaction according to Le Chatelier's principle, since the forward reaction is exothermic.

**8.B10:**
- (a) Step 1 ($E_a = 85 \text{ kJ/mol}$) is the RDS because it has the higher activation energy.
- (b) $\Delta H_1 = (E_a)_{f1} - (E_a)_{b1} \implies 25 = 85 - (E_a)_{b1} \implies (E_a)_{b1} = 60 \text{ kJ/mol}$.
- (c) Step 1 is endothermic ($\Delta H_1 = +25$), so B is higher in energy than A. Step 2: $\Delta H_2 = -30 - 25 = -55 \text{ kJ/mol}$ (highly exothermic), so C is much lower in energy than B. **C is more stable than B.**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**MCQs with traps. Explanation required.**

**Q8.J1 🟡**
For a given reaction, the activation energy of the forward reaction is $E_a$. The activation energy of the backward reaction is:
(A) Equal to $E_a$
(B) Less than $E_a$
(C) Greater than $E_a$
(D) Can be less than, greater than, or equal to $E_a$

**Q8.J2 🟡**
An endothermic reaction $X \rightarrow Y$ has an activation energy $E_1$. If the activation energy of the reverse reaction is $E_2$, then:
(A) $E_1 < E_2$
(B) $E_1 > E_2$
(C) $E_1 = E_2$
(D) $\Delta H = E_1 + E_2$

**Q8.J3 🔴**
A reaction $A + B \rightarrow C + D$ has $\Delta H = -25 \text{ kcal}$. The activation energy for the forward reaction is $15 \text{ kcal}$. What is the activation energy for the backward reaction $C + D \rightarrow A + B$?
(A) $10 \text{ kcal}$
(B) $40 \text{ kcal}$
(C) $-10 \text{ kcal}$
(D) $15 \text{ kcal}$

**Q8.J4 🟡**
The threshold energy of a chemical reaction depends upon:
(A) Temperature
(B) Nature of reacting species
(C) Concentration of reactants
(D) Pressure

**Q8.J5 🔴 (The Catalyst Trap)**
A catalyst lowers the activation energy of a reaction from $100 \text{ kJ/mol}$ to $70 \text{ kJ/mol}$. If the enthalpy of the uncatalyzed reaction is $-20 \text{ kJ/mol}$, what is the enthalpy of the catalyzed reaction?
(A) $-50 \text{ kJ/mol}$
(B) $+10 \text{ kJ/mol}$
(C) $-20 \text{ kJ/mol}$
(D) $-80 \text{ kJ/mol}$

**Q8.J6 🟡**
For a reaction, $(E_a)_f = 50 \text{ kJ/mol}$ and $(E_a)_b = 70 \text{ kJ/mol}$. Which statement is correct?
(A) The reaction is endothermic with $\Delta H = +20 \text{ kJ/mol}$
(B) The reaction is exothermic with $\Delta H = -20 \text{ kJ/mol}$
(C) The reaction is endothermic with $\Delta H = -20 \text{ kJ/mol}$
(D) The reaction is exothermic with $\Delta H = +20 \text{ kJ/mol}$

**Q8.J7 🟡**
If $(E_a)_b = 2(E_a)_f$ and $\Delta H = -30 \text{ kJ/mol}$, then $(E_a)_f$ is:
(A) $15 \text{ kJ/mol}$
(B) $30 \text{ kJ/mol}$
(C) $60 \text{ kJ/mol}$
(D) $90 \text{ kJ/mol}$

**Q8.J8 🔴**
In an exothermic reaction, $E_P = 40 \text{ kJ/mol}$, $E_T = 120 \text{ kJ/mol}$, and $(E_a)_f = 70 \text{ kJ/mol}$. The activation energy of the backward reaction is:
(A) $50 \text{ kJ/mol}$
(B) $60 \text{ kJ/mol}$
(C) $80 \text{ kJ/mol}$
(D) $90 \text{ kJ/mol}$

**Q8.J9 🟡**
For a certain reaction, $(E_a)_b = 40 \text{ kJ/mol}$ and $\Delta H = +25 \text{ kJ/mol}$. $(E_a)_f$ is:
(A) $15 \text{ kJ/mol}$
(B) $65 \text{ kJ/mol}$
(C) $40 \text{ kJ/mol}$
(D) $25 \text{ kJ/mol}$

**Q8.J10 🔴 (The Catalyst Paradox)**
Statement I: When a catalyst is added, both forward and backward rate constants increase by the same factor.
Statement II: A catalyst lowers $(E_a)_f$ and $(E_a)_b$ by the same amount.
(A) Both statements are true and Statement II explains Statement I.
(B) Both statements are true but Statement II does not explain Statement I.
(C) Statement I is true, Statement II is false.
(D) Statement I is false, Statement II is true.

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**8.J1 → Answer: (D)**
- Depending on whether the reaction is exothermic, endothermic, or isothermic, the backward activation energy can be larger, smaller, or equal to the forward activation energy.

**8.J2 → Answer: (B)**
- For an endothermic reaction, products have higher energy than reactants.
- The forward reaction has a larger peak to climb than the backward reaction sliding down from the product shelf.
- Therefore, $(E_a)_f > (E_a)_b$, which means $E_1 > E_2$.

**8.J3 → Answer: (B)**
- $\Delta H = (E_a)_f - (E_a)_b$
- $-25 = 15 - (E_a)_b \implies (E_a)_b = 15 + 25 = 40 \text{ kcal}$.

**8.J4 → Answer: (B)**
- The threshold energy is determined by the specific chemical bonds breaking and forming, which depends entirely on the nature of the reactants. It is independent of temperature or concentration.

**8.J5 → Answer: (C)**
- A catalyst lowers both the forward and backward activation energies by the exact same amount ($30 \text{ kJ/mol}$ in this case).
- The difference between them ($\Delta H$) remains absolutely unchanged. Thermodynamics does not care about the kinetic pathway!

**8.J6 → Answer: (B)**
- $\Delta H = 50 - 70 = -20 \text{ kJ/mol}$. The reaction is exothermic.

**8.J7 → Answer: (B)**
- Let $(E_a)_f = x$, then $(E_a)_b = 2x$. $\Delta H = x - 2x = -x = -30$. So $x = 30 \text{ kJ/mol}$.

**8.J8 → Answer: (C)**
- $E_R = E_T - (E_a)_f = 120 - 70 = 50 \text{ kJ/mol}$.
- $(E_a)_b = E_T - E_P = 120 - 40 = 80 \text{ kJ/mol}$.
- Or: $\Delta H = 70 - 80 = -10 \text{ kJ/mol}$, and $E_P = E_R + \Delta H = 50 - 10 = 40 \text{ kJ/mol}$.

**8.J9 → Answer: (B)**
- $\Delta H = (E_a)_f - (E_a)_b \implies 25 = (E_a)_f - 40 \implies (E_a)_f = 65 \text{ kJ/mol}$.

**8.J10 → Answer: (A)**
- Since $k \propto e^{-E_a/RT}$, lowering both $(E_a)_f$ and $(E_a)_b$ by the same amount multiplies both rate constants by the same factor. Thus Statement II correctly explains Statement I.
</details>

---

## Key Takeaways from Chapter 8

| Concept | Rule |
|---------|------|
| $\Delta H$ Formula | $\Delta H = (E_a)_f - (E_a)_b$ |
| Exothermic | $(E_a)_f < (E_a)_b \rightarrow \Delta H$ is negative |
| Endothermic | $(E_a)_f > (E_a)_b \rightarrow \Delta H$ is positive |
| Catalyst | Lowers $(E_a)_f$ and $(E_a)_b$ equally; $\Delta H$ is UNCHANGED |

---

## 🧠 Stage 7: Statement & Assertion-Reasoning

**Directions:** 
- For **Assertion-Reason**, choose:
  (A) Both A and R are true, and R is the correct explanation of A.
  (B) Both A and R are true, but R is NOT the correct explanation of A.
  (C) A is true but R is false.
  (D) A is false but R is true.
- For **Statement I/II**, choose based on whether each statement is correct or incorrect.

| # | Question | Difficulty |
|---|----------|------------|
| 8.S1 | **Assertion (A):** The activation energy of an exothermic reaction is always zero.<br>**Reason (R):** In an exothermic reaction, the products are more stable than the reactants. | 🟡 |
| 8.S2 | **Assertion (A):** A catalyst does not change the enthalpy of a reaction.<br>**Reason (R):** A catalyst lowers the activation energy of both the forward and backward reactions by the same amount. | 🟢 |
| 8.S3 | **Statement I:** All thermodynamically favorable reactions proceed instantly at room temperature.<br>**Statement II:** Thermodynamic stability is governed by $\Delta H$, while kinetic speed is governed by $E_a$. | 🟡 |
| 8.S4 | **Assertion (A):** For an endothermic reaction, the activation energy of the forward reaction must be greater than the enthalpy of the reaction.<br>**Reason (R):** $(E_a)_f = \Delta H + (E_a)_b$, and since $(E_a)_b$ must be positive, $(E_a)_f > \Delta H$. | 🔴 |
| 8.S5 | **Statement I:** The peak of an energy profile diagram represents the energy of the intermediate.<br>**Statement II:** The peak represents the transition state or activated complex, which cannot be isolated. | 🟡 |
| 8.S6 | **Assertion (A):** In an exothermic reaction, products are always formed faster than in an endothermic reaction.<br>**Reason (R):** Exothermic reactions have lower activation energy than endothermic reactions. | 🟡 |
| 8.S7 | **Assertion (A):** The minimum energy required for effective collisions is threshold energy, not activation energy.<br>**Reason (R):** Activation energy is extra energy above the average energy of reactants, while threshold energy is the absolute minimum needed. | 🔴 |
| 8.S8 | **Assertion (A):** A catalyst does not change the enthalpy of a reaction.<br>**Reason (R):** A catalyst lowers the activation energy of forward and backward reactions by the same amount. | 🟡 |
| 8.S9 | **Statement I:** In an endothermic reaction, $(E_a)_f$ is always greater than $\Delta H$.<br>**Statement II:** $(E_a)_f = \Delta H + (E_a)_b$, and $(E_a)_b$ must be positive. | 🟡 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**8.S1 → Answer: (D) A is false but R is true.**
- A is false: Even exothermic reactions have an energy barrier (activation energy) to break initial bonds (e.g., striking a match).
- R is true: Exothermic means products are at lower energy, thus more stable.

**8.S2 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Because $\Delta H = (E_a)_f - (E_a)_b$, if a catalyst subtracts $X$ from both terms, the difference $\Delta H$ remains identical.

**8.S3 → Statement I is False, Statement II is True.**
- Statement I is false: Graphite $\rightarrow$ Diamond is thermodynamically favorable but kinetically frozen due to huge $E_a$.

**8.S4 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- For endothermic, $\Delta H$ is positive. $\Delta H = (E_a)_f - (E_a)_b$.
- Rearranging: $(E_a)_f = \Delta H + (E_a)_b$. Since activation energies are always positive values, $(E_a)_f$ must be strictly greater than $\Delta H$.

**8.S5 → Statement I is False, Statement II is True.**
- The peak is the transition state, a fleeting state of bond-breaking/forming. An intermediate sits in a "valley" between two peaks in a multi-step reaction.

**8.S6 → Answer: (C) A is true but R is false.**
- A is true: An exothermic reaction has a lower $(E_a)_f$ typically, making products form faster.
- But R is false: Exothermic reactions do not ALWAYS have lower $E_a$ than endothermic reactions. A mildly exothermic reaction could have a high $E_a$ (e.g., diamond → graphite).

**8.S7 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- A is true: Threshold energy is the absolute minimum required.
- R is true and correctly explains: $E_T = E_R + E_a$, so activation energy is the extra amount.

**8.S8 → Answer: (C) A is true but R is false.**
- A is true: A catalyst does not change $\Delta H$.
- R is false: A catalyst lowers $(E_a)_f$ and $(E_a)_b$ by the **same** amount (not different amounts), which is exactly why $\Delta H$ stays unchanged.

**8.S9 → Statement I is True, Statement II is True, and Statement II correctly explains Statement I.**
- Since $\Delta H$ is positive for endothermic reactions and $(E_a)_b > 0$, $(E_a)_f = \Delta H + (E_a)_b > \Delta H$ always.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word.

**Q8.M1 🟢**
Which of the following is always true for an elementary chemical reaction?
(A) $(E_a)_f > \Delta H$
(B) $(E_a)_f < \Delta H$
(C) Threshold energy > Energy of reactants
(D) $\Delta H > 0$

**Q8.M2 🟡**
For a reaction $A \rightarrow B$, the forward rate constant increases by a factor of 10 in the presence of a catalyst. The backward rate constant will:
(A) Increase by a factor of 10
(B) Decrease by a factor of 10
(C) Remain unchanged
(D) Cannot be determined without temperature

**Q8.M3 🔴 (The Multi-Step Trap)**
A reaction occurs in two steps:
Step 1: $X \rightarrow Y$ (Activation energy = $80 \text{ kJ/mol}$)
Step 2: $Y \rightarrow Z$ (Activation energy = $20 \text{ kJ/mol}$)
Which step is the rate-determining step?
(A) Step 1, because it has higher activation energy and is slower.
(B) Step 2, because it forms the final product.
(C) Both are equally important.
(D) Cannot be determined without knowing $\Delta H$.

**Q8.M4 🟡**
If a reaction is highly exothermic, the activation energy of the reverse reaction must be:
(A) Very small
(B) Equal to the forward activation energy
(C) Very large
(D) Zero

**Q8.M5 🔴**
An energy profile diagram for $P \rightarrow Q$ shows the reactant $P$ at $10 \text{ kJ}$, the product $Q$ at $40 \text{ kJ}$, and the transition state at $90 \text{ kJ}$. What are $(E_a)_f$ and $\Delta H$ respectively?
(A) $80 \text{ kJ}$, $30 \text{ kJ}$
(B) $90 \text{ kJ}$, $30 \text{ kJ}$
(C) $80 \text{ kJ}$, $-30 \text{ kJ}$
(D) $50 \text{ kJ}$, $40 \text{ kJ}$

**Q8.M6 🟢**
Which of the following statements about activation energy is correct?
(A) Activation energy is always zero for spontaneous reactions.
(B) Activation energy is the difference between threshold energy and reactant energy.
(C) Activation energy is the total energy of the transition state.
(D) Activation energy increases with the addition of a catalyst.

**Q8.M7 🟡**
For a reaction, $(E_a)_f = 60 \text{ kJ/mol}$, $\Delta H = -40 \text{ kJ/mol}$, and $E_R = 30 \text{ kJ/mol}$. The threshold energy is:
(A) $90 \text{ kJ/mol}$
(B) $50 \text{ kJ/mol}$
(C) $20 \text{ kJ/mol}$
(D) $70 \text{ kJ/mol}$

**Q8.M8 🔴**
For a reversible reaction, $(E_a)_f = 100 \text{ kJ/mol}$ and $(E_a)_b = 60 \text{ kJ/mol}$. A catalyst reduces the threshold energy by $20 \text{ kJ/mol}$. The new $\Delta H$ will be:
(A) $+40 \text{ kJ/mol}$
(B) $-40 \text{ kJ/mol}$
(C) $+20 \text{ kJ/mol}$
(D) $-20 \text{ kJ/mol}$

**Q8.M9 🟡**
An energy profile for $X \rightarrow Y$ shows $E_X = 25 \text{ kJ}$, $E_Y = 55 \text{ kJ}$, and $E_T = 105 \text{ kJ}$. A catalyst lowers $(E_a)_f$ by $15 \text{ kJ}$. The new $(E_a)_b$ is:
(A) $35 \text{ kJ}$
(B) $50 \text{ kJ}$
(C) $65 \text{ kJ}$
(D) $80 \text{ kJ}$

<details>
<summary>💡 Full Solutions — MCQ Mastery</summary>

**8.M1 → Answer: (C)**
- The peak (Threshold) is always physically higher than the starting point (Reactants). Therefore, Threshold > Reactant energy is a universal truth. (A) is false for exothermic reactions.

**8.M2 → Answer: (A)**
- A catalyst lowers $(E_a)_f$ and $(E_a)_b$ by the *same amount*. Since $k \propto e^{-E_a/RT}$, lowering the barrier equally multiplies both rate constants by the *same exponential factor*. Therefore, the backward rate constant also increases by exactly a factor of 10!

**8.M3 → Answer: (A)**
- The step with the highest activation energy peak is the hardest to cross, making it the slowest step. The slowest step is always the rate-determining step (RDS).

**8.M4 → Answer: (C)**
- $\Delta H = (E_a)_f - (E_a)_b$. If it's highly exothermic, $\Delta H$ is a very large negative number. This means $(E_a)_b$ must be a very large positive number (much larger than $(E_a)_f$). It has to climb a huge mountain from the deep valley.

**8.M5 → Answer: (A)**
- $(E_a)_f = \text{Peak} - \text{Reactants} = 90 - 10 = 80 \text{ kJ}$.
- $\Delta H = \text{Products} - \text{Reactants} = 40 - 10 = +30 \text{ kJ}$.

**8.M6 → Answer: (B)**
- $(E_a)_f = E_T - E_R$ is the definition of activation energy. (A) is false: spontaneous reactions still need $E_a$ to overcome the barrier. (C) is false: that's threshold energy. (D) is false: a catalyst lowers $E_a$.

**8.M7 → Answer: (A)**
- $E_T = E_R + (E_a)_f = 30 + 60 = 90 \text{ kJ/mol}$.

**8.M8 → Answer: (A)**
- Original $\Delta H = 100 - 60 = +40 \text{ kJ/mol}$. A catalyst lowers both $(E_a)_f$ and $(E_a)_b$ equally by $20 \text{ kJ/mol}$, so $\Delta H$ remains $+40 \text{ kJ/mol}$.

**8.M9 → Answer: (A)**
- Original $(E_a)_f = 105 - 25 = 80 \text{ kJ}$. Original $(E_a)_b = 105 - 55 = 50 \text{ kJ}$.
- Catalyst lowers both by $15 \text{ kJ}$ equally. New $(E_a)_b = 50 - 15 = 35 \text{ kJ}$.
</details>
