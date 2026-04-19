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
| <span id="q-9.1a"></span>9.1a | 50 mL + 150 mL of 0.5 M HCl. Final M? Final total moles? | 🟢 |
| <span id="q-9.1b"></span>9.1b | 1 L + 2 L of 1 M NaOH. Final M? Total moles? | 🟢 |

<details>
<summary>View Answers</summary>

**9.1a**: Answer not found.
**9.1b**: Answer not found.

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
| <span id="q-9.2a"></span>9.2a | 100 mL of 4 M NaOH + 100 mL of 2 M NaOH. Find M_f. | 🟢 |
| <span id="q-9.2b"></span>9.2b | 50 mL of 0.1 M HCl + 150 mL of 0.3 M HCl. Find M_f. ⭐ | 🟡 |
| <span id="q-9.2c"></span>9.2c | 400 mL of 5 M H₂SO₄ + 600 mL of 2 M H₂SO₄. Find M_f. | 🟡 |
| <span id="q-9.2d"></span>9.2d | 250 mL of 1 M KCl + 750 mL of 3 M KCl. Find M_f and total moles. | 🟡 |

<details>
<summary>View Answers</summary>

**9.2a**: 3 M
**9.2b**: 0.25 M
**9.2c**: Answer not found.
**9.2d**: Answer not found.

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
| <span id="q-9.3a"></span>9.3a | 10 mL of 10 M + 990 mL of 0.1 M. Is final M closer to 10 or to 0.1? Estimate before calculating. | 🟡 |
| <span id="q-9.3b"></span>9.3b | Equal volumes of 2 M and 8 M. What will the final M be? | 🟢 |

<details>
<summary>View Answers</summary>

**9.3a**: Answer not found.
**9.3b**: Answer not found.

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
| <span id="q-9.4a"></span>9.4a | Mix 10 M and 2 M NaOH to get 4 M. Find V₁:V₂. ⭐ | 🟡 |
| <span id="q-9.4b"></span>9.4b | You have 0.1 M and 1 M HCl. What ratio gives 0.4 M? | 🟡 |
| <span id="q-9.4c"></span>9.4c | Mix 18 M conc. H₂SO₄ with 0 M (water) to get 3 M. Ratio? (Note: M₂ = 0 for water!) ⭐ | 🟡 |
| <span id="q-9.4d"></span>9.4d | Is it possible to get 12 M by mixing 5 M and 8 M solutions? Why or why not? | 🟡 |

<details>
<summary>View Answers</summary>

**9.4a**: V₁:V₂ = 1:3
**9.4b**: Answer not found.
**9.4c**: Answer not found.
**9.4d**: Answer not found.

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
| <span id="q-9.5a"></span>9.5a | 50 mL of 1 M HCl + 50 mL of 1 M NaOH. What's left? | 🟢 |
| <span id="q-9.5b"></span>9.5b | 100 mL of 0.2 M H₂SO₄ + 100 mL of 0.3 M NaOH. Which is excess? Find its final concentration. (H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O) ⭐⭐ | 🔴 |
| <span id="q-9.5c"></span>9.5c | 200 mL of 0.1 M NaOH + 300 mL of 0.05 M HCl. Excess and final concentration? | 🟡 |
| <span id="q-9.5d"></span>9.5d | 25 mL of 0.5 M Ba(OH)₂ + 25 mL of 0.5 M HCl. Ba(OH)₂ + 2HCl → BaCl₂ + 2H₂O. Which is excess? ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**9.5a**: Neutral — nothing left (all NaCl + H₂O)
**9.5b**: mmol H⁺ = 0.2×100×2 = 40; mmol OH⁻ = 0.3×100 = 30; H⁺ excess = 10 mmol in 200 mL → 0.05 M H⁺
**9.5c**: Answer not found.
**9.5d**: Answer not found.

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
| <span id="q-9.6a"></span>9.6a | 100 mL of 5 M HCl + 400 mL of water. Find M_f. | 🟢 |
| <span id="q-9.6b"></span>9.6b | 50 mL of solution + 950 mL of water gives M_f = 0.05 M. Find M₁. | 🟡 |

<details>
<summary>View Answers</summary>

**9.6a**: Answer not found.
**9.6b**: Answer not found.

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
| <span id="q-9.7a"></span>9.7a | 50 mL of 1 M + 50 mL of 3 M + 100 mL of 2 M HCl. Find M_f. | 🟡 |
| <span id="q-9.7b"></span>9.7b | 100 mL of 0.5 M NaOH + 200 mL of 0.2 M NaOH + 200 mL of water. Find M_f. | 🟡 |
| <span id="q-9.7c"></span>9.7c | Equal volumes of 1 M, 2 M, 3 M, and 4 M solutions. Find M_f. (No calculation needed!) | 🟢 |

<details>
<summary>View Answers</summary>

**9.7a**: Answer not found.
**9.7b**: Answer not found.
**9.7c**: Answer not found.

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
| <span id="q-9.8a"></span>9.8a | 50 mL of methanol + 50 mL of water → 97 mL total. If methanol was 1 M in solute X, actual vs predicted M of X? | 🔴 |
| <span id="q-9.8b"></span>9.8b | Why does this problem not arise significantly with dilute aqueous solutions? | 🟡 |

<details>
<summary>View Answers</summary>

**9.8a**: Answer not found.
**9.8b**: Answer not found.

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
| <span id="q-9.9a"></span>9.9a | 200 g of 1 m urea + 300 g of 3 m urea (both aqueous). Find final molality. (M_urea = 60) | 🔴 |
| <span id="q-9.9b"></span>9.9b | Why is mixing in molality harder than mixing in molarity? | 🟡 |

<details>
<summary>View Answers</summary>

**9.9a**: Answer not found.
**9.9b**: Answer not found.

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
| <span id="q-9.10a"></span>9.10a | Mix 50 mL of 4 M and 50 mL of 2 M NaOH. Dilute to 500 mL. Final M? | 🟡 |
| <span id="q-9.10b"></span>9.10b | Mix 100 mL of 0.5 M HCl, 200 mL of 0.3 M HCl, and 200 mL of water. Then dilute to 1 L. Final M? | 🟡 |

<details>
<summary>View Answers</summary>

**9.10a**: Answer not found.
**9.10b**: Answer not found.

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-9.M1"></span>9.M1 | 200 mL of 0.5 M H₂SO₄ + 300 mL of 0.2 M NaOH. (a) Which is excess? (Use stoichiometry!) (b) Find [excess] after mixing. (c) What volume of 0.1 M NaOH to fully neutralise the excess? | T5 + Ch8 | 🔴 |
| <span id="q-9.M2"></span>9.M2 | You need 500 mL of 0.6 M NaCl. You have 2 M and 0.1 M stock. (a) Find V₁ and V₂. (b) If total V must be exactly 500 mL, solve the system. | T4 + algebra | 🔴 |
| <span id="q-9.M3"></span>9.M3 | 100 mL of 1 M HCl, 100 mL of 2 M NaOH, and 100 mL of 1 M HCl are all mixed. (a) Total mmol HCl and NaOH. (b) Which is excess? (c) Final concentration. | T7 + T5 | 🟡 |

<details>
<summary>View Answers</summary>

**9.M1**: Answer not found.
**9.M2**: Answer not found.
**9.M3**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-9.B1"></span>9.B1 | 100 mL of 0.5 M NaCl is mixed with 200 mL of 0.3 M NaCl. Find the final molarity. ⭐ | 🟡 |
| <span id="q-9.B2"></span>9.B2 | Equal volumes of 1 M HCl and 1 M NaOH are mixed. What is in the resulting solution? | 🟢 |
| <span id="q-9.B3"></span>9.B3 | 50 mL of 0.2 M H₂SO₄ + 50 mL of 0.2 M NaOH. Is the final solution acidic, basic, or neutral? (H₂SO₄ is diprotic!) ⭐ | 🟡 |

<details>
<summary>View Answers</summary>

**9.B1**: Answer not found.
**9.B2**: Answer not found.
**9.B3**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-9.J1"></span>9.J1 | 200 mL of 0.2 M HCl + 300 mL of 0.1 M NaOH + 100 mL of 0.3 M HCl. Find final [H⁺] or [OH⁻], whichever is in excess. ⭐ | 🔴 |
| <span id="q-9.J2"></span>9.J2 | Mix V₁ mL of C₁ M and V₂ mL of C₂ M of the same solute. If M_f = (C₁ + C₂)/2, prove that V₁ = V₂. | 🟡 |
| <span id="q-9.J3"></span>9.J3 | 100 mL of 0.1 M AgNO₃ + 100 mL of 0.2 M NaCl. AgNO₃ + NaCl → AgCl↓ + NaNO₃. Find: (a) moles of AgCl formed (b) concentration of excess reagent (c) [Na⁺], [NO₃⁻], [Cl⁻] in final solution. ⭐⭐ | 🔴 |
| <span id="q-9.J4"></span>9.J4 | 50 mL of 0.5 M Ba(OH)₂ is mixed with 100 mL of 0.3 M HCl. Ba(OH)₂ + 2HCl → BaCl₂ + 2H₂O. Find the concentration of excess reagent and all ions present. ⭐ | 🔴 |
| <span id="q-9.J5"></span>9.J5 | Three solutions: 100 mL of 3 M, 200 mL of x M, and 100 mL of 1 M (all same solute). If M_f = 2 M, find x. ⭐ | 🟡 |

<details>
<summary>View Answers</summary>

**9.J1**: Answer not found.
**9.J2**: Answer not found.
**9.J3**: Answer not found.
**9.J4**: Answer not found.
**9.J5**: x = 2 M (solve: 300+200x+100=800 → 200x=400 → x=2)

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
