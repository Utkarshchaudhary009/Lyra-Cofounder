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
| 8.5a | Prepare 500 mL of 0.1 M HCl from conc. HCl (37%, d = 1.19, M = 36.5). ⭐ | 🟡 |
| 8.5b | Prepare 2 L of 0.5 M HNO₃ from conc. HNO₃ (68%, d = 1.41, M = 63). | 🟡 |
| 8.5c | A lab needs 250 mL of 2 M H₂SO₄. How much conc. H₂SO₄ (98%, d=1.84)? | 🟡 |

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
| 8.6a | 1 L of 0.1 M NaCl is boiled until volume = 250 mL. Find M₂. | 🟡 |
| 8.6b | 200 mL of 2 M sugar solution evaporates to 50 mL. Find M₂. | 🟡 |
| 8.6c | A 500 mL solution is 0.4 M. After evaporation, it's 1.0 M. How much water was lost? | 🟡 |
| 8.6d | Why can't you use this method to concentrate an ethanol-water solution? | 🟡 |

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
| 8.7a | A 3 m solution has 200 g of water. 300 g of water is added. Find new molality. | 🟡 |
| 8.7b | A 1 m aqueous glucose solution (M=180). 18 g of glucose is in 1 kg of water. If 500 g of water is added, find (a) new molality (b) new mole fraction. | 🟡 |

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
| 8.8a | 50 mL of 6 M HCl diluted to 300 mL. % decrease in molarity? | 🟡 |
| 8.8b | A solution's concentration drops by 90%. What was the dilution factor? | 🟡 |
| 8.8c | After a 5× dilution, the concentration is 0.3 M. What was the original M? | 🟢 |

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 8.M1 | You have conc. H₂SO₄ (18.4 M). (a) Find volume needed for 500 mL of 2 M. (b) If you accidentally dilute to 600 mL instead of 500 mL, what's the actual M? (c) To fix it, how much water must you evaporate? | T2 + T1 + T6 | 🟡 |
| 8.M2 | 10 mL of 12 M HCl is diluted to 100 mL (A), then 20 mL of A is diluted to 200 mL (B), then 50 mL of B is diluted to 500 mL (C). Find M of C. Verify using the total dilution factor. | T4 | 🟡 |
| 8.M3 | A 2 m glucose solution (M=180) has 1 kg of water. (a) Find moles of glucose. (b) If you add 500 g of water, find new molality. (c) If the new solution has d = 1.03 g/mL, find the new molarity. | T7 + Ch5 + Ch6 | 🔴 |
| 8.M4 | 100 mL of 0.5 N H₂SO₄ is diluted to 500 mL. (a) Find new N. (b) Convert to M. (c) What volume of this diluted solution neutralises 25 mL of 0.1 N NaOH? | T1 + Ch7-T2 + Ch7-T5 | 🟡 |

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 8.B1 | How many mL of 0.1 M NaOH solution are needed to neutralise 50 mL of 0.05 M H₂SO₄? (First approach using dilution concept + stoichiometry.) ⭐ | 🟡 |
| 8.B2 | 10 mL of concentrated H₂SO₄ (18 M) is diluted to 1 L. What is the molarity of the diluted solution? | 🟢 |
| 8.B3 | What volume of 12.1 M HCl must be diluted to get 1 L of 1 M HCl for a lab experiment? ⭐ | 🟡 |

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 8.J1 | 100 mL of 0.5 M H₂SO₄ is diluted with water to make it 0.1 M. Find the volume of water added. Then find how many moles of NaOH are needed to neutralise this diluted solution completely. ⭐ | 🟡 |
| 8.J2 | A concentrated solution of HCl (37%, d = 1.19 g/mL) needs three serial 10× dilutions to reach the desired lab concentration. (a) Find starting M. (b) Find final M. (c) Total volume if you start with 1 mL. | 🔴 |
| 8.J3 | 50 mL of 2 M NaCl is heated. Water evaporates until the volume is 20 mL. (a) New M. (b) New mass %. (Assume d = 1.08 g/mL for the concentrated solution.) ⭐ | 🔴 |
| 8.J4 | A student has a 5 m glucose solution in water. They add 200 mL of water (d = 1 g/mL). If the original solution had 500 g of water, find (a) new molality (b) why M₁V₁ = M₂V₂ gives a different (wrong) answer. | 🔴 |

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
