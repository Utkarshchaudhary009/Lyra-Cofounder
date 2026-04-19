# Chapter 8: Dilution
## Part III: Operations on Solutions

---

## 🎯 Stage 1: The Core Idea

### What is Dilution?

Dilution is adding **more solvent** to an existing solution. The solute doesn't change — you're just spreading it through more liquid.

> **Analogy:** You have a glass of very strong black coffee. You add hot water. The coffee gets weaker, but the total amount of coffee powder hasn't changed — it's just dissolved in more water now. That's dilution.

### The Fundamental Principle

```
BEFORE dilution: n moles of solute in V₁ litres
AFTER dilution:  n moles of solute in V₂ litres (V₂ > V₁)

Moles of solute NEVER change during dilution.
Only the volume changes → concentration decreases.
```

### What Dilution is NOT

| Dilution IS | Dilution is NOT |
|-------------|-----------------|
| Adding solvent to a solution | Adding more solute |
| Decreasing concentration | Changing the solute identity |
| Increasing volume | A chemical reaction |
| Reversible (by evaporation) | Mixing two different solutions (that's Ch 9) |

---

## 🔬 Stage 2: The Formula Lab

### The Master Formula

```
M₁V₁ = M₂V₂

where:
    M₁ = initial molarity (before dilution)
    V₁ = initial volume
    M₂ = final molarity (after dilution)
    V₂ = final volume
```

### Why This Works — Derivation

```
Before: moles = M₁ × V₁
After:  moles = M₂ × V₂

Since moles don't change:
    M₁ × V₁ = M₂ × V₂  ✅
```

### Works for Normality Too

```
N₁V₁ = N₂V₂    (since N = n-factor × M, and n-factor doesn't change)
```

### Volume Units

```
V₁ and V₂ MUST be in the same units.
Both in mL? Fine. Both in L? Fine. One in mL and one in L? ERROR!
```

### What About Molality?

```
⚠️ M₁V₁ = M₂V₂ does NOT work for molality!

Why? Because molality uses mass of solvent, not volume of solution.
When you add water:
    - Volume of solution changes (used in molarity)
    - Mass of solvent ALSO changes (used in molality)
    - But the relationship isn't simply m₁ × W₁ = m₂ × W₂ 
      because W refers to solvent mass, not solution volume.

For molality dilution: moles = m₁ × W₁(kg) = m₂ × W₂(kg)
where W₁, W₂ are masses of SOLVENT in kg.
```

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given M₁, V₁, V₂ → find M₂

**The Pattern:** The simplest dilution problem. Three values given, find the fourth.

#### Solved Example 8.1
**Q:** 100 mL of 2 M HCl is diluted to 500 mL. Find the new molarity. 🟢

**Solution:**
```
    M₁V₁ = M₂V₂
    2 × 100 = M₂ × 500
    M₂ = 200/500 = 0.4 M

Answer: 0.4 M
```

> **Why this works:** The 0.2 mol of HCl (2 × 0.1) is now spread across 0.5 L instead of 0.1 L. Concentration drops by a factor of 5.

> **⚠️ Common Mistake:** "Diluted TO 500 mL" means V₂ = 500 mL. "Diluted BY 500 mL" means V₂ = 100 + 500 = 600 mL. The preposition matters!

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 8.1a | 50 mL of 4 M NaOH diluted to 200 mL. Find M₂. | 🟢 |
| 8.1b | 250 mL of 0.5 M glucose diluted to 1 L. Find M₂. | 🟢 |
| 8.1c | 10 mL of 12 M HCl diluted to 500 mL. Find M₂. | 🟢 |
| 8.1d | 25 mL of 0.1 M KMnO₄ diluted to 250 mL. Find M₂. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**8.1a:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 4 \times 50 = M_2 \times 200 \Rightarrow M_2 = \frac{200}{200} = 1.0\text{ M}$.
*   **Answer:** $1.0\text{ M}$

**8.1b:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 0.5 \times 250 = M_2 \times 1000 \Rightarrow M_2 = \frac{125}{1000} = 0.125\text{ M}$.
*   **Answer:** $0.125\text{ M}$

**8.1c:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 12 \times 10 = M_2 \times 500 \Rightarrow M_2 = \frac{120}{500} = 0.24\text{ M}$.
*   **Answer:** $0.24\text{ M}$

**8.1d:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 0.1 \times 25 = M_2 \times 250 \Rightarrow M_2 = \frac{2.5}{250} = 0.01\text{ M}$.
*   **Answer:** $0.01\text{ M}$

</details>

---

### Type 2: Reverse — "What volume of stock to take?"

**The Pattern:** You have a concentrated solution (stock) and need a diluted solution. How much stock do you take?

#### Solved Example 8.2
**Q:** What volume of 6 M HCl is needed to prepare 500 mL of 0.5 M HCl? 🟡 ⭐

**Solution:**
```
    M₁V₁ = M₂V₂
    6 × V₁ = 0.5 × 500
    V₁ = 250/6 = 41.67 mL

Procedure: Take 41.67 mL of 6 M HCl and add water to make 
           the total volume 500 mL.

Answer: 41.67 mL
```

> **Lab practice:** Always add acid/stock to water, not the other way around. Transfer the measured stock to a volumetric flask that already has some water, then fill to the mark.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 8.2a | Volume of 18 M H₂SO₄ needed to make 1 L of 0.5 M H₂SO₄? ⭐ | 🟡 |
| 8.2b | Volume of 15 M HNO₃ to make 250 mL of 3 M HNO₃? | 🟡 |
| 8.2c | Volume of 12 M HCl to make 2 L of 0.1 M HCl? ⭐ | 🟡 |
| 8.2d | You need 100 mL of 0.01 M KMnO₄. You have 0.1 M KMnO₄. How much? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**8.2a:**
*   **Calculation:** $18 \times V_1 = 0.5 \times 1000 \Rightarrow V_1 = \frac{500}{18} = 27.78\text{ mL}$.
*   **Answer:** $27.78\text{ mL}$

**8.2b:**
*   **Calculation:** $15 \times V_1 = 3 \times 250 \Rightarrow 15 V_1 = 750 \Rightarrow V_1 = 50\text{ mL}$.
*   **Answer:** $50\text{ mL}$

**8.2c:**
*   **Calculation:** $12 \times V_1 = 0.1 \times 2000 \Rightarrow 12 V_1 = 200 \Rightarrow V_1 = 16.67\text{ mL}$.
*   **Answer:** $16.67\text{ mL}$

**8.2d:**
*   **Calculation:** $0.1 \times V_1 = 0.01 \times 100 \Rightarrow 0.1 V_1 = 1 \Rightarrow V_1 = 10\text{ mL}$.
*   **Answer:** $10\text{ mL}$

</details>

---

### Type 3: Adding Water — Volume of Water Added

**The Pattern:** "How much water was added?" = V₂ − V₁

#### Solved Example 8.3
**Q:** 200 mL of 3 M NaCl is diluted to 1 M by adding water. How much water was added? 🟢

**Solution:**
```
Step 1: Find final volume
    M₁V₁ = M₂V₂
    3 × 200 = 1 × V₂
    V₂ = 600 mL

Step 2: Water added
    V_water = V₂ - V₁ = 600 - 200 = 400 mL

Answer: 400 mL of water was added.
```

> **⚠️ Approximation alert:** We assume the final volume = initial volume + water volume. Strictly, volumes aren't perfectly additive (50 mL water + 50 mL ethanol ≠ 100 mL). But for dilute aqueous solutions, this approximation is very good.

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 8.3a | 100 mL of 5 M HCl diluted to 2 M. How much water added? | 🟢 |
| 8.3b | 500 mL of 0.2 M NaOH diluted to 0.05 M. Volume of water added? | 🟡 |
| 8.3c | 50 mL of 10 M H₂SO₄ needs to become 1 M. Water needed? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**8.3a:**
*   **Calculation:** $5 \times 100 = 2 \times V_2 \Rightarrow V_2 = 250\text{ mL}$.
    Volume of water added = $250 - 100 = 150\text{ mL}$.
*   **Answer:** $150\text{ mL}$

**8.3b:**
*   **Calculation:** $0.2 \times 500 = 0.05 \times V_2 \Rightarrow 100 = 0.05 V_2 \Rightarrow V_2 = 2000\text{ mL}$.
    Volume of water added = $2000 - 500 = 1500\text{ mL}$.
*   **Answer:** $1500\text{ mL}$

**8.3c:**
*   **Calculation:** $10 \times 50 = 1 \times V_2 \Rightarrow V_2 = 500\text{ mL}$.
    Volume of water needed = $500 - 50 = 450\text{ mL}$.
*   **Answer:** $450\text{ mL}$

</details>

---

### Type 4: Serial Dilution

**The Pattern:** Dilution in stages — dilute A to get B, then B to get C.

#### Solved Example 8.4
**Q:** 10 mL of 10 M HCl is diluted to 100 mL (Solution A). Then 10 mL of Solution A is diluted to 100 mL (Solution B). Find the molarity of Solution B. 🟡

**Solution:**
```
Step 1: Solution A
    M₁V₁ = M₂V₂
    10 × 10 = M_A × 100
    M_A = 1 M

Step 2: Solution B
    M_A × V_A = M_B × V_B
    1 × 10 = M_B × 100
    M_B = 0.1 M

Answer: Solution B is 0.1 M

Each 10× dilution reduces concentration by factor of 10.
Two 10× dilutions = 100× total dilution: 10 M → 0.1 M ✅
```

> **Shortcut for serial dilution:** Total dilution factor = product of individual factors.
> Factor₁ × Factor₂ = (V₂/V₁)₁ × (V₂/V₁)₂ = 10 × 10 = 100
> Final M = Initial M / Total factor = 10/100 = 0.1 M

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 8.4a | 5 mL of 6 M HCl → diluted to 50 mL (A). 5 mL of A → diluted to 50 mL (B). Find M_B. | 🟡 |
| 8.4b | Three successive 2× dilutions on a 8 M solution. Final molarity? | 🟡 |
| 8.4c | You need a 10⁻⁵ M solution from 0.1 M stock. Design a serial dilution protocol (suggest number of steps and volumes). | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**8.4a:**
*   **Calculation:** Step A: $6 \times 5 = M_A \times 50 \Rightarrow M_A = 0.6\text{ M}$.
    Step B: $0.6 \times 5 = M_B \times 50 \Rightarrow M_B = 0.06\text{ M}$.
    (Total factor: $10 \times 10 = 100$. $M_B = 6 / 100 = 0.06\text{ M}$).
*   **Answer:** $0.06\text{ M}$

**8.4b:**
*   **Calculation:** Three $2\times$ dilutions $\Rightarrow 2 \times 2 \times 2 = 8\times$ total dilution factor.
    Final $M = \frac{\text{Initial } M}{\text{factor}} = \frac{8}{8} = 1\text{ M}$.
*   **Answer:** $1\text{ M}$

**8.4c:**
*   **Calculation:** Required dilution factor = $\frac{0.1}{10^{-5}} = 10,000$.
    Instead of adding $1\text{ mL}$ to $9,999 \text{ mL}$ (hard and inaccurate), you map out a serial process.
    Protocol: Perform four separate $10\times$ dilutions.
    1. Take $10\text{ mL}$ stock, dilute to $100\text{ mL}$ ($10^{-2}\text{ M}$).
    2. Take $10\text{ mL}$ of new, dilute to $100\text{ mL}$ ($10^{-3}\text{ M}$).
    3. Take $10\text{ mL}$ of new, dilute to $100\text{ mL}$ ($10^{-4}\text{ M}$).
    4. Take $10\text{ mL}$ of new, dilute to $100\text{ mL}$ ($10^{-5}\text{ M}$).
    Alternatively: Two $100\times$ dilutions ($1\text{ mL}$ to $100\text{ mL}$ twice).
*   **Answer:** E.g., Four successive steps of diluting $10\text{ mL}$ to $100\text{ mL}$.

</details>

---

### Type 5: Dilution of Commercial Acids ⭐

**The Pattern:** Using the concentrated acid data from Chapter 6 (Type 9) to prepare laboratory solutions.

#### Solved Example 8.5
**Q:** Prepare 1 L of 1 M H₂SO₄ from concentrated H₂SO₄ (98% w/w, d = 1.84 g/mL, M_molar = 98). 🟡 ⭐

**Solution:**
```
Step 1: Find molarity of conc. H₂SO₄
    M₁ = (98 × 1.84 × 10)/98 = 18.4 M

Step 2: Apply dilution formula
    M₁V₁ = M₂V₂
    18.4 × V₁ = 1 × 1000
    V₁ = 1000/18.4 = 54.35 mL

Procedure:
    1. Take about 500 mL of water in a 1 L volumetric flask
    2. Slowly add 54.35 mL of conc. H₂SO₄ (ACID TO WATER!)
    3. Allow to cool (mixing acid and water is exothermic)
    4. Fill to the 1 L mark with water
    5. Mix well

Answer: Take 54.35 mL of conc. H₂SO₄ and dilute to 1 L.
```

> **Safety Rule:** "Do as you oughta — add acid to water!" Adding water to conc. H₂SO₄ can cause violent boiling and splattering.

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 8.5c | A lab needs 250 mL of 2 M H₂SO₄. How much conc. H₂SO₄ (98%, d=1.84)? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**8.5a:**
*   **Calculation:** Molarity of stock $M_1 = \frac{37 \times 1.19 \times 10}{36.5} = 12.06\text{ M}$.
    $M_1 V_1 = M_2 V_2 \Rightarrow 12.06 \times V_1 = 0.1 \times 500 \Rightarrow V_1 = \frac{50}{12.06} = 4.15\text{ mL}$.
*   **Answer:** $4.15\text{ mL}$

**8.5b:**
*   **Calculation:** Molarity of stock $M_1 = \frac{68 \times 1.41 \times 10}{63} = 15.22\text{ M}$.
    $M_1 V_1 = M_2 V_2 \Rightarrow 15.22 \times V_1 = 0.5 \times 2000 \Rightarrow V_1 = \frac{1000}{15.22} = 65.7\text{ mL}$.
*   **Answer:** $65.7\text{ mL}$

**8.5c:**
*   **Calculation:** Molarity of stock $M_1 = \frac{98 \times 1.84 \times 10}{98} = 18.4\text{ M}$.
    $M_1 V_1 = M_2 V_2 \Rightarrow 18.4 \times V_1 = 2 \times 250 \Rightarrow V_1 = \frac{500}{18.4} = 27.17\text{ mL}$.
*   **Answer:** $27.17\text{ mL}$

</details>

---

### Type 6: Evaporation — Reverse of Dilution

**The Pattern:** Removing solvent → volume decreases → concentration increases. It's dilution in reverse.

#### Solved Example 8.6
**Q:** 500 mL of 0.2 M NaCl is heated until 300 mL of water evaporates. Assuming the volume decreases by exactly 300 mL, find the new molarity. 🟡

**Solution:**
```
    V₂ = 500 - 300 = 200 mL

    M₁V₁ = M₂V₂   (moles of NaCl unchanged — NaCl doesn't evaporate)
    0.2 × 500 = M₂ × 200
    M₂ = 100/200 = 0.5 M

Answer: 0.5 M
```

> **Key insight:** Evaporation increases concentration. The formula is the same as dilution — just V₂ < V₁ instead of V₂ > V₁.

> **⚠️ Limitation:** This only works if the solute is non-volatile. If the solute can evaporate (like ethanol in water), some solute is also lost, and M₁V₁ ≠ M₂V₂.

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 8.6d | Why can't you use this method to concentrate an ethanol-water solution? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**8.6a:**
*   **Calculation:** $V_1 = 1000\text{ mL}, M_1 = 0.1\text{ M}, V_2 = 250\text{ mL}$.
    $0.1 \times 1000 = M_2 \times 250 \Rightarrow M_2 = \frac{100}{250} = 0.4\text{ M}$.
*   **Answer:** $0.4\text{ M}$

**8.6b:**
*   **Calculation:** $V_1 = 200\text{ mL}, M_1 = 2\text{ M}, V_2 = 50\text{ mL}$.
    $2 \times 200 = M_2 \times 50 \Rightarrow M_2 = \frac{400}{50} = 8\text{ M}$.
*   **Answer:** $8\text{ M}$

**8.6c:**
*   **Calculation:** $0.4 \times 500 = 1.0 \times V_2 \Rightarrow V_2 = 200\text{ mL}$.
    Water lost = $V_1 - V_2 = 500 - 200 = 300\text{ mL}$.
*   **Answer:** $300\text{ mL}$

**8.6d:**
*   **Calculation:** Moles of solute must remain constant for $M_1 V_1 = M_2 V_2$ to work. Ethanol is volatile (it evaporates). So, when you heat it, both water and ethanol evaporate, meaning moles of solute are not conserved.
*   **Answer:** Because ethanol is volatile; solute moles are lost during evaporation.

</details>

---

### Type 7: Dilution and Molality — Why M₁V₁ = M₂V₂ Fails

**The Pattern:** Understanding why the dilution formula doesn't apply to molality.

#### Solved Example 8.7
**Q:** Explain why M₁V₁ = M₂V₂ cannot be used for molality. What is the correct approach? 🟡

**Solution:**
```
Why it fails:
    M₁V₁ = M₂V₂ uses VOLUME of solution.
    Molality uses MASS OF SOLVENT, not volume of solution.
    When you add water:
        • Volume of solution changes
        • Mass of solvent ALSO changes
    But the relationship between volume and solvent mass isn't 
    the same as in molarity because molality's denominator is 
    different.

Correct approach for molality:
    Moles of solute = constant
    m₁ × W₁(kg of solvent) = m₂ × W₂(kg of solvent)

    If you add Δw kg of water:
        W₂ = W₁ + Δw
        m₂ = (m₁ × W₁) / (W₁ + Δw)

Example:
    2 m solution, 500 g solvent. Add 500 g water.
    moles = 2 × 0.5 = 1 mol
    New W = 500 + 500 = 1000 g = 1 kg
    m₂ = 1/1 = 1 m

    Using M₁V₁ = M₂V₂ would give a WRONG answer because
    volumes aren't directly proportional to solvent masses.
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| 8.7b | A 1 m aqueous glucose solution (M=180). 18 g of glucose is in 1 kg of water. If 500 g of water is added, find (a) new molality (b) new mole fraction. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**8.7a:**
*   **Calculation:** $m_1 \times W_1 (\text{in kg}) = \text{moles} = \text{constant}$.
    Moles = $3 \times 0.2\text{ kg} = 0.6 \text{ mol}$.
    New solvent mass $W_2 = 0.2 + 0.3 = 0.5\text{ kg}$.
    $m_2 = \frac{0.6}{0.5} = 1.2\text{ m}$.
*   **Answer:** $1.2\text{ m}$

**8.7b:**
*   **Calculation:** Original moles = $18/180 = 0.1\text{ mol}$.
    (a) New $W = 1\text{ kg} + 0.5\text{ kg} = 1.5\text{ kg}$.
    $m_2 = \frac{0.1}{1.5} = 0.0667\text{ m}$.
    (b) New mass of water = $1500\text{ g}$. Moles of water = $1500 / 18 = 83.33\text{ mol}$.
    $X_{\text{glucose}} = \frac{0.1}{0.1 + 83.33} = \frac{0.1}{83.43} \approx 0.0012$.
*   **Answer:** (a) $0.0667\text{ m}$, (b) $0.0012$

</details>

---

### Type 8: Percentage Change in Concentration on Dilution

**The Pattern:** By what percentage did the concentration decrease?

#### Solved Example 8.8
**Q:** 100 mL of 2 M HCl is diluted to 400 mL. By what percentage did the molarity decrease? 🟡

**Solution:**
```
    M₂ = M₁V₁/V₂ = 2 × 100/400 = 0.5 M

    Decrease = M₁ - M₂ = 2 - 0.5 = 1.5 M

    % decrease = (decrease/original) × 100
              = (1.5/2) × 100
              = 75%

Answer: 75% decrease in molarity

Alternatively: Dilution factor = V₂/V₁ = 400/100 = 4×
    Concentration becomes 1/4 of original → 75% decrease ✅
```

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| 8.8c | After a 5× dilution, the concentration is 0.3 M. What was the original M? | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**8.8a:**
*   **Calculation:** $M_2 = \frac{M_1 V_1}{V_2} = \frac{6 \times 50}{300} = 1\text{ M}$.
    Decrease = $6 - 1 = 5\text{ M}$.
    $\text{Percentage decrease} = \left(\frac{5}{6}\right) \times 100 = 83.33\%$.
*   **Answer:** $83.33\%$

**8.8b:**
*   **Calculation:** Drops by $90\% \Rightarrow$ final is $10\%$ of original.
    $M_2 = 0.1 M_1$.
    Since $M_1 V_1 = M_2 V_2 \Rightarrow M_1 V_1 = 0.1 M_1 V_2 \Rightarrow V_2 = 10 V_1$.
    Dilution factor = $\frac{V_2}{V_1} = 10$.
*   **Answer:** $10\times$

**8.8c:**
*   **Calculation:** $M_2 = \frac{M_1}{\text{factor}}$.
    $0.3 = \frac{M_1}{5} \Rightarrow M_1 = 0.3 \times 5 = 1.5\text{ M}$.
*   **Answer:** $1.5\text{ M}$

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 8.M4 | 100 mL of 0.5 N H₂SO₄ is diluted to 500 mL. (a) Find new N. (b) Convert to M. (c) What volume of this diluted solution neutralises 25 mL of 0.1 N NaOH? | T1 + Ch7-T2 + Ch7-T5 | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**8.M1:**
*   **Calculation:**
    (a) $18.4 \times V_1 = 2 \times 500 \Rightarrow V_1 = 54.35\text{ mL}$.
    (b) If diluted to $600\text{ mL}$ total: $18.4 \times 54.35 = M \times 600 \Rightarrow 1000 = M \times 600 \Rightarrow M = 1.67\text{ M}$.
    (c) Water to evaporate = $600\text{ mL} - 500\text{ mL} = 100\text{ mL}$.
*   **Answer:** (a) $54.35\text{ mL}$, (b) $1.67\text{ M}$, (c) $100\text{ mL}$

**8.M2:**
*   **Calculation:** Total Dilution Factor = $(100/10) \times (200/20) \times (500/50)$ = $10 \times 10 \times 10 = 1000$.
    Final $M = \frac{12}{1000} = 0.012\text{ M}$.
*   **Answer:** $0.012\text{ M}$

**8.M3:**
*   **Calculation:**
    (a) $m = \frac{n}{W(\text{kg})} \Rightarrow 2 = \frac{n}{1} \Rightarrow n = 2\text{ mol}$.
    (b) Add $500\text{ g}$ water. Total water = $1.5\text{ kg}$. $m_{\text{new}} = \frac{2}{1.5} = 1.33\text{ m}$.
    (c) Mass of solution = $(2 \times 180\text{ g glucose}) + 1500\text{ g water} = 1860\text{ g}$.
    Volume = $\frac{\text{Mass}}{d} = \frac{1860}{1.03} = 1805.8\text{ mL} = 1.806\text{ L}$.
    $M = \frac{\text{moles}}{V} = \frac{2}{1.806} = 1.107\text{ M}$.
*   **Answer:** (a) $2\text{ mol}$, (b) $1.33\text{ m}$, (c) $1.11\text{ M}$

**8.M4:**
*   **Calculation:**
    (a) $N_1 V_1 = N_2 V_2 \Rightarrow 0.5 \times 100 = N_2 \times 500 \Rightarrow N_2 = 0.1\text{ N}$.
    (b) H₂SO₄ $n\text{-factor} = 2$. $M = \frac{N}{n_f} = \frac{0.1}{2} = 0.05\text{ M}$.
    (c) Eq of acid = Eq of base. $N_a V_a = N_b V_b \Rightarrow 0.1 \times V_a = 0.1 \times 25 \Rightarrow V_a = 25\text{ mL}$.
*   **Answer:** (a) $0.1\text{ N}$, (b) $0.05\text{ M}$, (c) $25\text{ mL}$

</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 8.B3 | What volume of 12.1 M HCl must be diluted to get 1 L of 1 M HCl for a lab experiment? ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**8.B1:**
*   **Calculation:** 
    $N(\text{H}_2\text{SO}_4) = 0.05 \times 2 = 0.1\text{ N}$.
    $N(\text{NaOH}) = 0.1 \times 1 = 0.1\text{ N}$.
    $N_a V_a = N_b V_b \Rightarrow 0.1 \times 50 = 0.1 \times V_b \Rightarrow V_b = 50\text{ mL}$ of NaOH.
*   **Answer:** $50\text{ mL}$

**8.B2:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 18 \times 10 = M_2 \times 1000 \Rightarrow M_2 = \frac{180}{1000} = 0.18\text{ M}$.
*   **Answer:** $0.18\text{ M}$

**8.B3:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 12.1 \times V_1 = 1 \times 1000 \Rightarrow V_1 = \frac{1000}{12.1} = 82.64\text{ mL}$.
*   **Answer:** $82.64\text{ mL}$

</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 8.J4 | A student has a 5 m glucose solution in water. They add 200 mL of water (d = 1 g/mL). If the original solution had 500 g of water, find (a) new molality (b) why M₁V₁ = M₂V₂ gives a different (wrong) answer. | 🔴 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**8.J1:**
*   **Calculation:** $M_1 V_1 = M_2 V_2 \Rightarrow 0.5 \times 100 = 0.1 \times V_2 \Rightarrow V_2 = 500\text{ mL}$.
    Water added = $500 - 100 = 400\text{ mL}$.
    Moles of H₂SO₄ in diluted solution = $0.1\text{ M} \times 0.5\text{ L} = 0.05\text{ mol}$.
    Neutralisation: $\text{H}_2\text{SO}_4 + 2\text{NaOH} \rightarrow \text{Na}_2\text{SO}_4 + 2\text{H}_2\text{O}$
    $1\text{ mol}$ H₂SO₄ requires $2\text{ mol}$ NaOH.
    $0.05\text{ mol}$ H₂SO₄ requires $0.05 \times 2 = 0.1\text{ mol}$ NaOH.
*   **Answer:** Water added = $400\text{ mL}$, NaOH needed = $0.1\text{ mol}$

**8.J2:**
*   **Calculation:**
    (a) $M_1 = \frac{\% \times d \times 10}{M_w} = \frac{37 \times 1.19 \times 10}{36.5} = 12.06\text{ M}$.
    (b) Three $10\times$ dilutions $\Rightarrow 10 \times 10 \times 10 = 1000\times$ dilution factor.
        $M_{\text{final}} = \frac{12.06}{1000} = 0.01206\text{ M}$.
    (c) $1\text{ mL} \xrightarrow{10\times} 10\text{ mL} \xrightarrow{10\times} 100\text{ mL} \xrightarrow{10\times} 1000\text{ mL} = 1\text{ L}$.
*   **Answer:** (a) $12.06\text{ M}$, (b) $0.01206\text{ M}$, (c) $1\text{ L}$

**8.J3:**
*   **Calculation:**
    (a) Moles NaCl = $2\text{ M} \times 0.05\text{ L} = 0.1\text{ mol}$. Final Volume $V_2 = 0.02\text{ L}$.
        $M_2 = \frac{0.1}{0.02} = 5\text{ M}$.
    (b) Original mass of solution = $50\text{ mL} \times 1.08\text{ g/mL} = 54\text{ g}$.
        Volume lost = $50 - 20 = 30\text{ mL}$. Assuming only water evaporates with $d=1\text{ g/mL}$, mass lost = $30\text{ g}$.
        Final mass of solution = $54 - 30 = 24\text{ g}$.
        Mass of NaCl = $0.1\text{ mol} \times 58.5\text{ g/mol} = 5.85\text{ g}$.
        Mass $\%$ = $\frac{5.85}{24} \times 100 = 24.375\%$.
*   **Answer:** (a) $5\text{ M}$, (b) $24.38\%$

**8.J4:**
*   **Calculation:**
    (a) Initial moles glucose = $5\text{ m} \times 0.5\text{ kg} = 2.5\text{ mol}$.
        Added water = $200\text{ mL} = 200\text{ g} = 0.2\text{ kg}$.
        Total water $W_{\text{final}} = 0.5 + 0.2 = 0.7\text{ kg}$.
        $m_2 = \frac{2.5}{0.7} = 3.57\text{ m}$.
    (b) $M_1 V_1 = M_2 V_2$ explicitly uses *solution volume*, assuming volume strictly reflects dilution factor, but molality relates to *solvent mass*. Adding water changes the solution volume non-linearly due to the solute's presence and density variations, whereas it adds linearly to the solvent mass.
*   **Answer:** (a) $3.57\text{ m}$, (b) Molality depends on solvent mass, not solution volume.

</details>

---

## Key Takeaways from Chapter 8

```
┌──────────────────────────────────────────────────────────────┐
│                   DILUTION SUMMARY                            │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Golden Rule: Moles of solute DON'T change                   │
│                                                               │
│  Formula: M₁V₁ = M₂V₂  (also N₁V₁ = N₂V₂)                │
│                                                               │
│  "Diluted TO" → V₂ is the given value                       │
│  "Diluted BY" → V₂ = V₁ + added volume                     │
│                                                               │
│  Evaporation = reverse dilution (V₂ < V₁ → M₂ > M₁)       │
│                                                               │
│  Serial dilution:                                             │
│    Total factor = product of individual factors               │
│    Final M = Initial M / Total factor                        │
│                                                               │
│  ⚠️ Does NOT work for molality!                              │
│    For molality: m₁W₁ = m₂W₂ (W = mass of solvent in kg)   │
│                                                               │
│  Lab safety: Add acid TO water, not water to acid            │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 7 — Normality](./07-normality.md) | [Chapter 9 — Mixing Solutions →](./09-mixing-solutions.md)*
