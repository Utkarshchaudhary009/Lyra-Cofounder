# Chapter 9: Mixing Two Solutions
## Part III: Operations on Solutions

---

## 🎯 Stage 1: The Core Idea

### What Happens When You Mix Solutions?

When you mix two solutions, the moles of solute from **both** solutions combine into a new, larger volume.

> **Analogy:** Two lemonade pitchers — one strong, one weak — are poured into a big bowl. The total lemon content is the sum from both pitchers. The final concentration is somewhere between the two originals.

### The Fundamental Principle

```
Total moles after mixing = Sum of moles from each solution

n_total = n₁ + n₂
M_f × V_f = M₁V₁ + M₂V₂

where V_f = V₁ + V₂ (assuming volumes are additive)
```

### Mixing vs. Dilution

| Dilution (Ch 8) | Mixing (Ch 9) |
|-----------------|---------------|
| Add pure solvent | Add another solution |
| One source of solute | Two (or more) sources |
| M₁V₁ = M₂V₂ | M_f = (M₁V₁ + M₂V₂)/(V₁ + V₂) |
| Final M < initial M (always) | Final M is between M₁ and M₂ |

---

## 🔬 Stage 2: The Formula Lab

### The Formula (Same Solute)

```
           M₁V₁ + M₂V₂
M_final = ────────────────
             V₁ + V₂
```

> This is a **weighted average** of the two concentrations, weighted by volume.

### For Normality

```
           N₁V₁ + N₂V₂
N_final = ────────────────
             V₁ + V₂
```

### The Answer is Always Between

```
If M₁ > M₂, then:    M₂ < M_final < M₁    (ALWAYS)

Think about it: mixing strong with weak gives medium. 
It can never be stronger than the strongest or weaker than the weakest.
```

### Volume Additivity Assumption

```
We assume: V_final = V₁ + V₂

This is excellent for dilute aqueous solutions.
It fails for:
    • Concentrated solutions
    • Mixing dissimilar liquids (ethanol + water)
    • 50 mL ethanol + 50 mL water ≈ 96 mL (not 100 mL!)
```

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Same Solute, Same Concentration

**The Pattern:** Mixing identical solutions. The concentration stays the same.

#### Solved Example 9.1
**Q:** 100 mL of 2 M NaCl is mixed with 200 mL of 2 M NaCl. Find the final molarity. 🟢

**Solution:**
```
    M_f = (M₁V₁ + M₂V₂) / (V₁ + V₂)
        = (2 × 100 + 2 × 200) / (100 + 200)
        = (200 + 400) / 300
        = 600/300
        = 2 M

Answer: 2 M (unchanged — obviously!)
```

> **Insight:** Mixing same-concentration solutions is essentially combining bottles. No change in concentration, only in total volume and total moles.

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 9.1b | 1 L + 2 L of 1 M NaOH. Final M? Total moles? | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**9.1a:**
*   **Calculation:** Mixing same concentration yields the same concentration. $M_{\text{final}} = 0.5\text{ M}$.
    Total volume = $50 + 150 = 200\text{ mL} = 0.2\text{ L}$.
    Total moles = $M \times V = 0.5 \times 0.2 = 0.1\text{ mol}$.
*   **Answer:** $0.5\text{ M}$, $0.1\text{ mol}$

**9.1b:**
*   **Calculation:** Same concentration $\Rightarrow M_{\text{final}} = 1\text{ M}$.
    Total volume = $1 + 2 = 3\text{ L}$.
    Total moles = $1 \times 3 = 3\text{ mol}$.
*   **Answer:** $1\text{ M}$, $3\text{ mol}$

</details>

---

### Type 2: Same Solute, Different Concentrations ⭐

**The Pattern:** The bread-and-butter mixing problem. Weighted average of concentrations.

#### Solved Example 9.2
**Q:** 200 mL of 3 M HCl is mixed with 300 mL of 1 M HCl. Find M_final. 🟡 ⭐

**Solution:**
```
    M_f = (M₁V₁ + M₂V₂) / (V₁ + V₂)
        = (3 × 200 + 1 × 300) / (200 + 300)
        = (600 + 300) / 500
        = 900/500
        = 1.8 M

Check: Is 1 < 1.8 < 3? ✅ (between the two original molarities)

Answer: 1.8 M
```

> **Why this works:** Total moles = 0.6 + 0.3 = 0.9 mol in total volume 500 mL = 0.5 L. M = 0.9/0.5 = 1.8 M.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 9.2d | 250 mL of 1 M KCl + 750 mL of 3 M KCl. Find M_f and total moles. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**9.2a:**
*   **Calculation:** Equal volumes, so the final molarity is the average.
    $M_f = \frac{4 + 2}{2} = 3\text{ M}$.
*   **Answer:** $3\text{ M}$

**9.2b:**
*   **Calculation:** $M_f = \frac{M_1 V_1 + M_2 V_2}{V_1 + V_2} = \frac{0.1 \times 50 + 0.3 \times 150}{50 + 150} = \frac{5 + 45}{200} = \frac{50}{200} = 0.25\text{ M}$.
*   **Answer:** $0.25\text{ M}$

**9.2c:**
*   **Calculation:** $M_f = \frac{5 \times 400 + 2 \times 600}{400 + 600} = \frac{2000 + 1200}{1000} = \frac{3200}{1000} = 3.2\text{ M}$.
*   **Answer:** $3.2\text{ M}$

**9.2d:**
*   **Calculation:** Total moles = $M_1 V_1 + M_2 V_2$ (with $V$ in L)
    $= 1 \times 0.25 + 3 \times 0.75 = 0.25 + 2.25 = 2.5\text{ mol}$.
    Total volume = $250 + 750 = 1000\text{ mL} = 1\text{ L}$.
    $M_f = \frac{2.5}{1} = 2.5\text{ M}$.
*   **Answer:** $2.5\text{ M}$, $2.5\text{ mol}$

</details>

---

### Type 3: Predicting if Final M is Between M₁ and M₂

**The Pattern:** Conceptual — proving the result is always between the two concentrations.

#### Solved Example 9.3
**Q:** Without calculating, predict whether the final molarity of mixing 100 mL of 5 M NaCl with 400 mL of 1 M NaCl will be: (a) closer to 5 or to 1? (b) exactly 3? 🟡

**Solution:**
```
(a) Since V₂ = 400 mL >> V₁ = 100 mL, the weaker solution 
    dominates. Final M will be closer to 1 M than to 5 M.

    Actual calculation: M_f = (500 + 400)/500 = 1.8 M ✅
    Indeed, 1.8 is much closer to 1 than to 5.

(b) M_f = 3 only if they were mixed in equal volumes:
    M_f = (5 × V + 1 × V)/(2V) = 6V/(2V) = 3 M

    Since volumes are unequal (100 vs 400), M_f ≠ 3.

Key rule: The final M is a weighted average.
    The solution with MORE volume has MORE weight.
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 9.3b | Equal volumes of 2 M and 8 M. What will the final M be? | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**9.3a:**
*   **Calculation:** The $0.1\text{ M}$ solution has $99\times$ more volume ($990\text{ mL}$ vs $10\text{ mL}$). Therefore, the final concentration will be heavily weighted towards $0.1\text{ M}$.
    (Exact calculation: $M_f = \frac{10\times 10 + 0.1\times 990}{1000} = \frac{100 + 99}{1000} = 0.199\text{ M}$).
*   **Answer:** Much closer to $0.1\text{ M}$.

**9.3b:**
*   **Calculation:** If mixed in equal volumes, the relative weights are equal. So the final concentration is the exact arithmetic mean.
    $M_f = \frac{2 + 8}{2} = 5\text{ M}$.
*   **Answer:** $5\text{ M}$

</details>

---

### Type 4: Given Final M → Find Ratio V₁:V₂ (Alligation Method) ⭐⭐

**The Pattern:** You want a specific final concentration. In what volume ratio should you mix the two solutions?

#### Derivation
```
    M_f = (M₁V₁ + M₂V₂) / (V₁ + V₂)

    M_f(V₁ + V₂) = M₁V₁ + M₂V₂
    M_f·V₁ + M_f·V₂ = M₁V₁ + M₂V₂
    V₁(M₁ - M_f) = V₂(M_f - M₂)

    V₁/V₂ = (M_f - M₂) / (M₁ - M_f)
```

#### The Alligation Formula

```
    V₁     M_f - M₂
   ──── = ───────────
    V₂     M₁ - M_f

(Volume ratio = difference of the "other" concentration from the target)
```

#### The Alligation Diagram (Visual Method)
```
    M₁ ─────────┐
                 ├───── M_f
    M₂ ─────────┘

    V₁ corresponds to |M_f - M₂| (the "cross" difference)
    V₂ corresponds to |M₁ - M_f| (the "cross" difference)
```

#### Solved Example 9.4
**Q:** You need 2 M HCl. You have 6 M and 1 M HCl. In what volume ratio should you mix them? 🟡 ⭐⭐

**Solution:**
```
Using alligation:
    V₁/V₂ = (M_f - M₂)/(M₁ - M_f)
           = (2 - 1)/(6 - 2)
           = 1/4

Answer: Mix 6 M and 1 M in the ratio 1:4 by volume.

Verification:
    Let V₁ = 100 mL, V₂ = 400 mL
    M_f = (6×100 + 1×400)/(100+400) = 1000/500 = 2 M ✅
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 9.4d | Is it possible to get 12 M by mixing 5 M and 8 M solutions? Why or why not? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**9.4a:**
*   **Calculation:** Use alligation or ratio formula: $\frac{V_1}{V_2} = \frac{|M_f - M_2|}{|M_1 - M_f|}$.
    Let $V_1$ be $10\text{ M}$ and $V_2$ be $2\text{ M}$. Target $M_f = 4\text{ M}$.
    $\frac{V_1}{V_2} = \frac{|4 - 2|}{|10 - 4|} = \frac{2}{6} = \frac{1}{3}$.
*   **Answer:** Ratio of $10\text{ M}$ to $2\text{ M}$ is $1:3$.

**9.4b:**
*   **Calculation:** Let $V_1$ be $0.1\text{ M}$ and $V_2$ be $1\text{ M}$. Target $M_f = 0.4\text{ M}$.
    $\frac{V_1}{V_2} = \frac{|0.4 - 1|}{|0.1 - 0.4|} = \frac{0.6}{0.3} = 2$.
*   **Answer:** Ratio of $0.1\text{ M}$ to $1\text{ M}$ is $2:1$.

**9.4c:**
*   **Calculation:** Let $V_1$ be $18\text{ M}$ and $V_2$ be water ($0\text{ M}$). Target $M_f = 3\text{ M}$.
    $\frac{V_1}{V_2} = \frac{|3 - 0|}{|18 - 3|} = \frac{3}{15} = \frac{1}{5}$.
*   **Answer:** Ratio of acid to water is $1:5$.

**9.4d:**
*   **Calculation:** Mixing two solutions results in a weighted average. The final concentration must always lie *between* the two starting concentrations ($5\text{ M} < M_f < 8\text{ M}$).
*   **Answer:** No, because the maximum possible concentration you can achieve is $8\text{ M}$ (without evaporating solvent).

</details>

---

### Type 5: Mixing Acid + Base (Neutralization) ⭐⭐

**The Pattern:** When an acid meets a base, they react. Leftover concentration depends on which is in excess.

#### Key Approach
```
Step 1: Find mmol of acid and mmol of base
Step 2: Find the limiting reagent using stoichiometry
Step 3: Leftover mmol = excess - used
Step 4: Final concentration = leftover mmol / total volume (mL)
```

#### Solved Example 9.5
**Q:** 100 mL of 0.5 M HCl is mixed with 100 mL of 0.3 M NaOH. Find the concentration of the excess reagent. 🟡 ⭐

**Solution:**
```
Step 1: Find millimoles
    mmol HCl = 0.5 × 100 = 50 mmol
    mmol NaOH = 0.3 × 100 = 30 mmol

Step 2: Reaction: HCl + NaOH → NaCl + H₂O  (1:1)
    HCl needed for 30 mmol NaOH = 30 mmol
    HCl available = 50 mmol
    → HCl is in EXCESS

Step 3: Leftover HCl
    mmol_excess = 50 - 30 = 20 mmol

Step 4: Final concentration
    Total volume = 100 + 100 = 200 mL
    [HCl]_excess = 20/200 = 0.1 M

Answer: The resulting solution contains 0.1 M HCl (acidic)
        Also contains 0.3 M NaCl (formed by the reaction).
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 9.5d | 25 mL of 0.5 M Ba(OH)₂ + 25 mL of 0.5 M HCl. Ba(OH)₂ + 2HCl → BaCl₂ + 2H₂O. Which is excess? ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**9.5a:**
*   **Calculation:** mmol HCl = $50 \times 1 = 50\text{ mmol}$. mmol NaOH = $50 \times 1 = 50\text{ mmol}$.
    Since they react $1:1$ and mmols are equal, neither is in excess. The solution is neutral ($0\text{ M}$ acid/base).
*   **Answer:** Completely neutralised (only salt NaCl remains).

**9.5b:**
*   **Calculation:** mmol H₂SO₄ = $100 \times 0.2 = 20\text{ mmol}$.
    mmol NaOH = $100 \times 0.3 = 30\text{ mmol}$.
    Reaction: $1\text{ H}_2\text{SO}_4 + 2\text{ NaOH} \rightarrow \dots$
    $30\text{ mmol}$ NaOH requires $15\text{ mmol}$ H₂SO₄.
    We have $20\text{ mmol}$ H₂SO₄, so H₂SO₄ is in excess by $20 - 15 = 5\text{ mmol}$.
    Total volume = $200\text{ mL}$. $[\text{H}_2\text{SO}_4]_{\text{excess}} = \frac{5}{200} = 0.025\text{ M}$.
*   **Answer:** H₂SO₄ is in excess. Concentration = $0.025\text{ M}$.

**9.5c:**
*   **Calculation:** mmol NaOH = $200 \times 0.1 = 20\text{ mmol}$.
    mmol HCl = $300 \times 0.05 = 15\text{ mmol}$.
    Reaction is $1:1$. NaOH is in excess by $20 - 15 = 5\text{ mmol}$.
    Total volume = $500\text{ mL}$. $[\text{NaOH}]_{\text{excess}} = \frac{5}{500} = 0.01\text{ M}$.
*   **Answer:** NaOH is in excess. Concentration = $0.01\text{ M}$.

**9.5d:**
*   **Calculation:** mmol Ba(OH)₂ = $25 \times 0.5 = 12.5\text{ mmol}$.
    mmol HCl = $25 \times 0.5 = 12.5\text{ mmol}$.
    Reaction: $1\text{ Ba(OH)}_2 + 2\text{ HCl} \rightarrow \dots$
    $12.5\text{ mmol}$ HCl consumes $6.25\text{ mmol}$ Ba(OH)₂.
    Excess Ba(OH)₂ = $12.5 - 6.25 = 6.25\text{ mmol}$.
*   **Answer:** Ba(OH)₂ is in excess.

</details>

---

### Type 6: Mixing Solution + Pure Solvent (M₂ = 0)

**The Pattern:** Special case where one "solution" is just pure water (M₂ = 0). This is actually dilution!

#### Solved Example 9.6
**Q:** 200 mL of 3 M NaCl is mixed with 300 mL of pure water. Find M_f. 🟢

**Solution:**
```
    M_f = (M₁V₁ + M₂V₂) / (V₁ + V₂)
        = (3 × 200 + 0 × 300) / (200 + 300)
        = 600/500
        = 1.2 M

This is identical to the dilution formula:
    M₁V₁ = M_f × V_f
    3 × 200 = 1.2 × 500 ✅

Answer: 1.2 M
```

> **Insight:** Dilution (Chapter 8) is just a special case of mixing where one component has M = 0!

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 9.6b | 50 mL of solution + 950 mL of water gives M_f = 0.05 M. Find M₁. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**9.6a:**
*   **Calculation:** $M_f = \frac{5 \times 100 + 0}{100 + 400} = \frac{500}{500} = 1\text{ M}$.
*   **Answer:** $1\text{ M}$

**9.6b:**
*   **Calculation:** Using $M_1 V_1 = M_f V_f$. Total volume $V_f = 50 + 950 = 1000\text{ mL}$.
    $M_1 \times 50 = 0.05 \times 1000 \Rightarrow 50 M_1 = 50 \Rightarrow M_1 = 1\text{ M}$.
*   **Answer:** $1\text{ M}$

</details>

---

### Type 7: Mixing More Than 2 Solutions

**The Pattern:** Extension to 3 or more solutions.

#### The Formula

```
           M₁V₁ + M₂V₂ + M₃V₃ + ...
M_final = ───────────────────────────────
              V₁ + V₂ + V₃ + ...
```

#### Solved Example 9.7
**Q:** 100 mL of 1 M, 200 mL of 2 M, and 200 mL of 4 M NaCl are mixed. Find M_f. 🟡

**Solution:**
```
    M_f = (1×100 + 2×200 + 4×200) / (100 + 200 + 200)
        = (100 + 400 + 800) / 500
        = 1300/500
        = 2.6 M

Answer: 2.6 M
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| 9.7c | Equal volumes of 1 M, 2 M, 3 M, and 4 M solutions. Find M_f. (No calculation needed!) | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**9.7a:**
*   **Calculation:** $M_f = \frac{1 \times 50 + 3 \times 50 + 2 \times 100}{50 + 50 + 100} = \frac{50 + 150 + 200}{200} = \frac{400}{200} = 2\text{ M}$.
*   **Answer:** $2\text{ M}$

**9.7b:**
*   **Calculation:** $M_f = \frac{0.5 \times 100 + 0.2 \times 200 + 0 \times 200}{100 + 200 + 200} = \frac{50 + 40 + 0}{500} = \frac{90}{500} = 0.18\text{ M}$.
*   **Answer:** $0.18\text{ M}$

**9.7c:**
*   **Calculation:** When volumes are equal, the final concentration is just the arithmetic mean of all concentrations.
    $M_f = \frac{1 + 2 + 3 + 4}{4} = \frac{10}{4} = 2.5\text{ M}$.
*   **Answer:** $2.5\text{ M}$

</details>

---

### Type 8: Volume NOT Additive — The Real-World Twist

**The Pattern:** When V₁ + V₂ ≠ V_final due to molecular interactions.

#### Solved Example 9.8
**Q:** 50 mL of ethanol and 50 mL of water are mixed. The actual final volume is 96 mL (not 100 mL). If the ethanol solution was 2 M in a certain solute, and the water had 0 M of that solute, find the actual concentration vs. the predicted concentration. 🔴

**Solution:**
```
Predicted (assuming V_f = 100 mL):
    M_f = (2 × 50 + 0 × 50) / 100 = 1 M

Actual (V_f = 96 mL):
    Total moles = 2 × 0.05 = 0.1 mol  (from 50 mL of 2 M)
    M_f = 0.1/0.096 = 1.042 M

Error = (1.042 - 1.0)/1.042 × 100 ≈ 4%

The actual concentration is HIGHER than predicted because 
the actual volume is LESS than expected.
```

> **Why volumes aren't additive:** When ethanol and water mix, ethanol molecules fit into the gaps between water molecules (like small balls filling spaces between large balls). The total volume is less than expected.

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| 9.8b | Why does this problem not arise significantly with dilute aqueous solutions? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**9.8a:**
*   **Calculation:** 
    Predicted $M_f = \frac{1 \times 50}{100} = 0.5\text{ M}$.
    Actual volume = $97\text{ mL}$. Total moles = $1 \times 0.050\text{ L} = 0.05\text{ mol}$.
    Actual $M_f = \frac{0.05\text{ mol}}{0.097\text{ L}} = 0.515\text{ M}$.
*   **Answer:** Actual = $0.515\text{ M}$, Predicted = $0.5\text{ M}$.

**9.8b:**
*   **Calculation:** Dilute aqueous solutions are overwhelmingly made of water. Mixing two dilute solutions is effectively mixing water with water, so the intermolecular forces and packing efficiencies remain largely unchanged, making the volumes almost perfectly additive.
*   **Answer:** Because both solutions are mostly water, so the molecular packing doesn't change significantly upon mixing.

</details>

---

### Type 9: Mixing in Molality Terms

**The Pattern:** Mixing using mass-based (not volume-based) calculations.

#### Solved Example 9.9
**Q:** 500 g of 2 m glucose solution is mixed with 500 g of 1 m glucose solution. Find the molality of the mixture. (The solvent is water in both.) 🔴

**Solution:**
```
Solution 1 (2 m):
    m₁ = 2, so 2 mol glucose per kg of solvent
    But we have 500 g of SOLUTION, not 500 g of solvent!
    
    We need to find solvent mass:
    In a 2 m solution, 1 kg solvent has 2 mol glucose = 2 × 180 = 360 g glucose
    Mass of solution = 1000 + 360 = 1360 g
    
    So in 500 g of solution:
        Mass of solvent = 500 × (1000/1360) = 367.6 g
        Moles of glucose = 500 × (360/1360) / 180 = 0.735 mol

    Alternatively, simply scale:
        If 1360 g solution → 2 mol glucose in 1000 g water
        500 g solution → (2 × 500/1360) mol = 0.735 mol in (1000 × 500/1360) = 367.6 g water

Solution 2 (1 m):
    1 kg solvent has 1 mol glucose = 180 g glucose
    Mass of solution per kg solvent = 1000 + 180 = 1180 g
    
    In 500 g of solution:
        Moles of glucose = 1 × 500/1180 = 0.424 mol
        Mass of solvent = 1000 × 500/1180 = 423.7 g

Mixture:
    Total moles = 0.735 + 0.424 = 1.159 mol
    Total solvent = 367.6 + 423.7 = 791.3 g = 0.7913 kg
    
    m_final = 1.159/0.7913 = 1.465 m

Answer: ~1.46 m
```

> **Key lesson:** Mixing in molality is more complicated because "mass of solution" ≠ "mass of solvent." You must carefully extract solvent mass from each solution before adding.

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| 9.9b | Why is mixing in molality harder than mixing in molarity? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 9</summary>

**9.9a:**
*   **Calculation:**
    Solution 1 ($1\text{ m}$): $1\text{ kg}$ solvent ($1000\text{ g}$) contains $1\text{ mol}$ urea ($60\text{ g}$). Total mass = $1060\text{ g}$.
    In $200\text{ g}$ solution: $W_1 = 200 \times \frac{1000}{1060} = 188.68\text{ g}$. Moles $n_1 = 200 \times \frac{1}{1060} = 0.1887\text{ mol}$.
    Solution 2 ($3\text{ m}$): $1\text{ kg}$ solvent contains $3\text{ mol}$ urea ($180\text{ g}$). Total mass = $1180\text{ g}$.
    In $300\text{ g}$ solution: $W_2 = 300 \times \frac{1000}{1180} = 254.24\text{ g}$. Moles $n_2 = 300 \times \frac{3}{1180} = 0.7627\text{ mol}$.
    Mixture: Total moles = $0.1887 + 0.7627 = 0.9514\text{ mol}$.
    Total solvent = $188.68 + 254.24 = 442.92\text{ g} = 0.4429\text{ kg}$.
    $m_f = \frac{0.9514}{0.4429} = 2.148\text{ m}$.
*   **Answer:** $2.148\text{ m}$

**9.9b:**
*   **Calculation:** Molarity requires solution volume, which is usually given directly, making $M = n/V$ straightforward to apply. Molality is based on solvent mass, but mixtures are usually given in terms of total solution mass (or volume). Therefore, one must first isolate and calculate the solvent mass fraction for each solution before adding.
*   **Answer:** Because you must extract the mass of the solvent from the mass of the solution before mixing.

</details>

---

### Type 10: Mixing and Then Diluting

**The Pattern:** Two-step process — mix first, then dilute.

#### Solved Example 9.10
**Q:** 100 mL of 3 M HCl and 100 mL of 1 M HCl are mixed, then the mixture is diluted to 500 mL. Find: (a) M after mixing (b) M after dilution. 🟡

**Solution:**
```
(a) After mixing:
    M_mix = (3×100 + 1×100)/(100+100) = 400/200 = 2 M
    Volume = 200 mL

(b) After dilution to 500 mL:
    M₁V₁ = M₂V₂
    2 × 200 = M₂ × 500
    M₂ = 400/500 = 0.8 M

Answer: (a) 2 M  (b) 0.8 M
```

> **Shortcut:** You can combine both steps:
> M_final = (M₁V₁ + M₂V₂) / V_final = (300 + 100)/500 = 0.8 M ✅

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| 9.10b | Mix 100 mL of 0.5 M HCl, 200 mL of 0.3 M HCl, and 200 mL of water. Then dilute to 1 L. Final M? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 10</summary>

**9.10a:**
*   **Calculation:** Moles = $4\text{ M} \times 0.05\text{ L} + 2\text{ M} \times 0.05\text{ L} = 0.2 + 0.1 = 0.3\text{ mol}$.
    Final volume = $500\text{ mL} = 0.5\text{ L}$.
    $M_f = \frac{0.3}{0.5} = 0.6\text{ M}$.
*   **Answer:** $0.6\text{ M}$

**9.10b:**
*   **Calculation:** Moles = $0.5 \times 0.1 + 0.3 \times 0.2 + 0 = 0.05 + 0.06 = 0.11\text{ mol}$.
    Final volume = $1\text{ L}$.
    $M_f = \frac{0.11}{1} = 0.11\text{ M}$.
*   **Answer:** $0.11\text{ M}$

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 9.M3 | 100 mL of 1 M HCl, 100 mL of 2 M NaOH, and 100 mL of 1 M HCl are all mixed. (a) Total mmol HCl and NaOH. (b) Which is excess? (c) Final concentration. | T7 + T5 | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**9.M1:**
*   **Calculation:** mmol H₂SO₄ = $200 \times 0.5 = 100\text{ mmol}$. mmol NaOH = $300 \times 0.2 = 60\text{ mmol}$.
    Reaction: $1\text{ H}_2\text{SO}_4 + 2\text{ NaOH} \rightarrow \dots$
    $60\text{ mmol}$ NaOH consumes $30\text{ mmol}$ H₂SO₄.
    (a) Excess H₂SO₄ = $100 - 30 = 70\text{ mmol}$.
    (b) Total volume = $500\text{ mL}$. $[\text{H}_2\text{SO}_4] = \frac{70}{500} = 0.14\text{ M}$.
    (c) To neutralise $70\text{ mmol}$ H₂SO₄ (which provides $140\text{ mmol}$ H⁺), we need $140\text{ mmol}$ NaOH.
    $V \times 0.1 = 140 \Rightarrow V = 1400\text{ mL}$.
*   **Answer:** (a) H₂SO₄, (b) $0.14\text{ M}$, (c) $1400\text{ mL}$

**9.M2:**
*   **Calculation:**
    (a) Alligation: $\frac{V_1}{V_2} = \frac{|0.6 - 0.1|}{|2 - 0.6|} = \frac{0.5}{1.4} = \frac{5}{14}$.
    (b) $V_1 + V_2 = 500 \Rightarrow \frac{5}{19} \times 500$ and $V_2 = \frac{14}{19} \times 500$.
    $V_1 = 131.58\text{ mL}$ ($2\text{ M}$ stock), $V_2 = 368.42\text{ mL}$ ($0.1\text{ M}$ stock).
*   **Answer:** $131.58\text{ mL}$ of $2\text{ M}$ and $368.42\text{ mL}$ of $0.1\text{ M}$

**9.M3:**
*   **Calculation:**
    (a) Total mmol HCl = $100 \times 1 + 100 \times 1 = 200\text{ mmol}$. Total mmol NaOH = $100 \times 2 = 200\text{ mmol}$.
    (b) $200\text{ mmol}$ acid reacts perfectly with $200\text{ mmol}$ base ($1:1$). Neither is in excess.
    (c) Neutral solution, so excess reactant concentration is $0\text{ M}$. ([NaCl] = $200/300 = 0.67\text{ M}$).
*   **Answer:** (a) $200\text{ mmol}$ HCl, $200\text{ mmol}$ NaOH, (b) Neither, (c) $0\text{ M}$ (neutral)

</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 9.B3 | 50 mL of 0.2 M H₂SO₄ + 50 mL of 0.2 M NaOH. Is the final solution acidic, basic, or neutral? (H₂SO₄ is diprotic!) ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**9.B1:**
*   **Calculation:** $M_f = \frac{0.5 \times 100 + 0.3 \times 200}{100 + 200} = \frac{50 + 60}{300} = \frac{110}{300} = 0.367\text{ M}$.
*   **Answer:** $0.367\text{ M}$

**9.B2:**
*   **Calculation:** Equal volumes $\Rightarrow$ equal moles (since $M=1$ for both). They perfectly neutralise to form NaCl and water.
*   **Answer:** A $0.5\text{ M}$ neutral solution of NaCl.

**9.B3:**
*   **Calculation:** mmol H₂SO₄ = $50 \times 0.2 = 10\text{ mmol}$. mmol NaOH = $50 \times 0.2 = 10\text{ mmol}$.
    H₂SO₄ is diprotic, so $10\text{ mmol}$ provides $20\text{ mmol}$ of H⁺ ions.
    NaOH provides $10\text{ mmol}$ of OH⁻ ions.
    Excess H⁺ = $20 - 10 = 10\text{ mmol}$ H⁺ remaining. Thus, the solution is acidic.
*   **Answer:** Acidic

</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 9.J5 | Three solutions: 100 mL of 3 M, 200 mL of x M, and 100 mL of 1 M (all same solute). If M_f = 2 M, find x. ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**9.J1:**
*   **Calculation:** mmol H⁺ = $(200 \times 0.2\text{ HCl}) + (100 \times 0.3\text{ HCl}) = 40 + 30 = 70\text{ mmol}$.
    mmol OH⁻ = $300 \times 0.1\text{ NaOH} = 30\text{ mmol}$.
    Excess H⁺ = $70 - 30 = 40\text{ mmol}$. Total volume = $200 + 300 + 100 = 600\text{ mL}$.
    $[\text{H}^+]_{\text{excess}} = \frac{40}{600} = 0.0667\text{ M}$.
*   **Answer:** $[\text{H}^+] = 0.0667\text{ M}$

**9.J2:**
*   **Calculation:** $M_f = \frac{C_1 V_1 + C_2 V_2}{V_1 + V_2} = \frac{C_1 + C_2}{2}$.
    $2(C_1 V_1 + C_2 V_2) = (C_1 + C_2)(V_1 + V_2) = C_1 V_1 + C_1 V_2 + C_2 V_1 + C_2 V_2$.
    $C_1 V_1 + C_2 V_2 = C_1 V_2 + C_2 V_1 \Rightarrow C_1(V_1 - V_2) - C_2(V_1 - V_2) = 0$.
    $(C_1 - C_2)(V_1 - V_2) = 0$. Since concentrations are different ($C_1 \neq C_2$), we must have $V_1 - V_2 = 0 \Rightarrow V_1 = V_2$.
*   **Answer:** Proven above.

**9.J3:**
*   **Calculation:** mmol AgNO₃ = $100 \times 0.1 = 10\text{ mmol}$. mmol NaCl = $100 \times 0.2 = 20\text{ mmol}$.
    AgNO₃ is limiting ($10\text{ mmol}$). 
    (a) AgCl formed = $10\text{ mmol}$.
    (b) Excess NaCl = $20 - 10 = 10\text{ mmol}$. Total volume = $200\text{ mL}$. $[\text{NaCl}]_{\text{excess}} = 10/200 = 0.05\text{ M}$.
    (c) Na⁺ came from $20\text{ mmol}$ NaCl $\Rightarrow [\text{Na}^+] = 20/200 = 0.1\text{ M}$.
        NO₃⁻ came from $10\text{ mmol}$ $\Rightarrow [\text{NO}_3^-] = 10/200 = 0.05\text{ M}$.
        Cl⁻ is the excess $\Rightarrow [\text{Cl}^-] = 10/200 = 0.05\text{ M}$.
*   **Answer:** (a) $10\text{ mmol}$, (b) $0.05\text{ M}$, (c) $[\text{Na}^+] = 0.1\text{ M}, [\text{NO}_3^-] = 0.05\text{ M}, [\text{Cl}^-] = 0.05\text{ M}$

**9.J4:**
*   **Calculation:** mmol Ba(OH)₂ = $50 \times 0.5 = 25\text{ mmol}$. mmol HCl = $100 \times 0.3 = 30\text{ mmol}$.
    $1\text{ Ba(OH)}_2 + 2\text{ HCl} \rightarrow \dots$
    $30\text{ mmol}$ HCl consumes $15\text{ mmol}$ Ba(OH)₂.
    Excess Ba(OH)₂ = $25 - 15 = 10\text{ mmol}$. Total volume = $150\text{ mL}$.
    $[\text{Ba(OH)}_2]_{\text{excess}} = \frac{10}{150} = 0.0667\text{ M}$.
    Ions: $[\text{Ba}^{2+}]$ from all $25\text{ mmol}$ = $25/150 = 0.167\text{ M}$.
    $[\text{Cl}^-]$ from all $30\text{ mmol}$ = $30/150 = 0.20\text{ M}$.
    $[\text{OH}^-]$ from excess $10\text{ mmol}$ Ba(OH)₂ = $20\text{ mmol}$ OH⁻ / $150 = 0.133\text{ M}$.
*   **Answer:** $[\text{Ba(OH)}_2]_{\text{excess}} = 0.0667\text{ M}$. $[\text{Ba}^{2+}] = 0.167\text{ M}, [\text{Cl}^-] = 0.20\text{ M}, [\text{OH}^-] = 0.133\text{ M}$

**9.J5:**
*   **Calculation:** $M_f = \frac{M_1 V_1 + M_2 V_2 + M_3 V_3}{V_{\text{total}}} \Rightarrow 2 = \frac{3 \times 100 + x \times 200 + 1 \times 100}{100 + 200 + 100}$.
    $2 = \frac{300 + 200x + 100}{400} \Rightarrow 800 = 400 + 200x \Rightarrow 400 = 200x \Rightarrow x = 2\text{ M}$.
*   **Answer:** $x = 2$

</details>

---

## Key Takeaways from Chapter 9

```
┌──────────────────────────────────────────────────────────────┐
│                MIXING SOLUTIONS SUMMARY                       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Same solute mixing:                                          │
│      M_f = (M₁V₁ + M₂V₂) / (V₁ + V₂)                     │
│                                                               │
│  Result is always BETWEEN M₁ and M₂                         │
│                                                               │
│  Alligation (find ratio):                                     │
│      V₁/V₂ = (M_f - M₂) / (M₁ - M_f)                      │
│                                                               │
│  Acid + Base → neutralisation:                                │
│      Find mmol of each → identify excess → leftover conc     │
│      ⚠️ Watch stoichiometry (H₂SO₄ is diprotic!)            │
│                                                               │
│  Mixing + dilution shortcut:                                  │
│      M_f = (M₁V₁ + M₂V₂) / V_final                        │
│                                                               │
│  Molality mixing: More complex — need solvent mass,           │
│      can't use simple volume formula                          │
│                                                               │
│  Volume additivity: Assumed for dilute aqueous solutions      │
│      Fails for concentrated or non-aqueous mixtures           │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 8 — Dilution](./08-dilution.md) | [Chapter 10 — Ionic Concentration →](./10-ionic-concentration.md)*
