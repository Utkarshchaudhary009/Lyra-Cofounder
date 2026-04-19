# Chapter 11: Inter-conversion of Concentration Terms
## Part IV: The Master Level

---

## 🎯 Stage 1: The Core Idea

### Why Inter-conversion?

Every competitive exam question on solutions ultimately reduces to this: **"Convert from one concentration term to another."** You'll be given mass%, molality, mole fraction, or molarity — and asked to find a different one. Sometimes you'll chain 2-3 conversions in a single problem.

> **The master skill isn't memorizing formulas — it's knowing which formula to use, and what information you need (density? molar mass?) to bridge the gap.**

### The Conversion Landscape

```
                    ┌──────────────┐
                    │   w/w%       │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Molality │ │ Molarity │ │   Mole   │
        │   (m)    │◄┤   (M)    ├►│ Fraction │
        └─────┬────┘ └────┬─────┘ └────┬─────┘
              │           │            │
              └───────────┴────────────┘
                          │
                    [density needed for
                     anything with M]
```

### The Golden Rule

```
Any conversion TO or FROM molarity requires DENSITY.
Conversions between w/w%, molality, and mole fraction do NOT need density.
```

---

## 🔬 Stage 2: The Formula Lab

### All Master Formulas in One Place

| From → To | Formula | Requires Density? |
|-----------|---------|-------------------|
| w/w% → M | `M = (w/w% × d × 10) / M_solute` | ✅ Yes |
| w/w% → m | `m = (w/w% × 1000) / ((100 - w/w%) × M_solute)` | ❌ No |
| w/w% → χ | `χ = (w/w% / M_solute) / (w/w%/M_solute + (100-w/w%)/M_solvent)` | ❌ No |
| M → m | `m = (M × 1000) / (d × 1000 - M × M_solute)` | ✅ Yes |
| m → M | `M = (m × d × 1000) / (1000 + m × M_solute)` | ✅ Yes |
| χ → m | `m = (1000 × χ) / ((1 - χ) × M_solvent)` | ❌ No |
| m → χ | `χ = (m × M_solvent) / (1000 + m × M_solvent)` | ❌ No |
| χ → M | `M = (χ × d × 1000) / (χ × M_solute + (1-χ) × M_solvent)` | ✅ Yes |
| M → w/w% | `w/w% = (M × M_solute) / (d × 10)` | ✅ Yes |
| M → χ | Convert M → m first, then m → χ | ✅ Yes |

### The "Consider 100 g" / "Consider 1 L" Strategy

Instead of memorizing formulas, you can derive any conversion from first principles:

```
For w/w%, m, χ problems: "Consider 100 g of solution"
    → Mass of solute = w/w%
    → Mass of solvent = 100 - w/w%
    → Convert masses to moles
    → Apply the target formula

For M problems: "Consider 1 L of solution"  
    → Moles of solute = M
    → Mass of solution = d × 1000 g
    → Mass of solute = M × M_solute
    → Mass of solvent = d × 1000 - M × M_solute
```

> **This strategy is UNIVERSAL.** If you forget a formula during the exam, just start from "100 g" or "1 L" and derive what you need. It takes 30 seconds and never fails.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: w/w% ↔ Molarity (density given) ⭐⭐

**The Pattern:** The most frequently tested conversion.

#### Solved Example 11.1A (w/w% → M)
**Q:** A 20% (w/w) NaOH solution has density 1.22 g/mL. Find its molarity. (M_NaOH = 40) 🟡 ⭐

**Solution:**
```
Formula: M = (w/w% × d × 10) / M_solute

    M = (20 × 1.22 × 10) / 40
    M = 244 / 40
    M = 6.1 M

First principles check (consider 100 g of solution):
    Mass of NaOH = 20 g → n = 20/40 = 0.5 mol
    Volume = 100/1.22 = 81.97 mL = 0.08197 L
    M = 0.5/0.08197 = 6.1 M ✅

Answer: 6.1 M
```

#### Solved Example 11.1B (M → w/w%)
**Q:** A 5 M H₂SO₄ solution has d = 1.29 g/mL. Find the mass percent. (M = 98) 🟡 ⭐

**Solution:**
```
Rearranging: w/w% = (M × M_solute) / (d × 10)

    w/w% = (5 × 98) / (1.29 × 10)
    w/w% = 490 / 12.9
    w/w% = 37.98%

First principles (consider 1 L):
    Mass of H₂SO₄ = 5 × 98 = 490 g
    Mass of solution = 1.29 × 1000 = 1290 g
    w/w% = (490/1290) × 100 = 37.98% ✅

Answer: ≈ 38%
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.1a"></span>11.1a | 10% KOH (M=56), d = 1.09 g/mL. Find M. ⭐ | 🟡 |
| <span id="q-11.1b"></span>11.1b | 37% HCl (M=36.5), d = 1.19 g/mL. Find M. ⭐⭐ | 🟡 |
| <span id="q-11.1c"></span>11.1c | 3 M glucose (M=180), d = 1.12 g/mL. Find w/w%. | 🟡 |
| <span id="q-11.1d"></span>11.1d | 68% HNO₃ (M=63), d = 1.41 g/mL. Find M. ⭐ | 🟡 |

<details>
<summary>View Answers</summary>

**11.1a**: Answer not found.
**11.1b**: Answer not found.
**11.1c**: Answer not found.
**11.1d**: Answer not found.

</details>


---

### Type 2: w/w% ↔ Molality ⭐

**The Pattern:** No density needed!

#### Solved Example 11.2
**Q:** A 15% glucose (M = 180) solution. Find molality. 🟡 ⭐

**Solution:**
```
Formula: m = (w/w% × 1000) / (M_solute × (100 - w/w%))

    m = (15 × 1000) / (180 × 85)
    m = 15000 / 15300
    m = 0.98 mol/kg

First principles (100 g of solution):
    Solute = 15 g → n = 15/180 = 0.0833 mol
    Solvent = 85 g = 0.085 kg
    m = 0.0833/0.085 = 0.98 ✅

Answer: m ≈ 0.98 mol/kg
```

#### Reverse: m → w/w%
```
Rearranging:
    w/w% = (m × M_solute × 100) / (1000 + m × M_solute)
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.2a"></span>11.2a | 5% urea (M=60). Find m. | 🟡 |
| <span id="q-11.2b"></span>11.2b | 98% H₂SO₄ (M=98). Find m. ⭐ | 🟡 |
| <span id="q-11.2c"></span>11.2c | m = 2.5, M_solute = 40 (NaOH). Find w/w%. (Reverse) | 🟡 |
| <span id="q-11.2d"></span>11.2d | 25% NaCl (M=58.5). Find m. | 🟡 |

<details>
<summary>View Answers</summary>

**11.2a**: Answer not found.
**11.2b**: Answer not found.
**11.2c**: Answer not found.
**11.2d**: Answer not found.

</details>


---

### Type 3: Molarity ↔ Molality (density given) ⭐⭐⭐

**The Pattern:** THE most important conversion for JEE. Always needs density.

#### Solved Example 11.3A (M → m)
**Q:** 3 M NaCl solution, d = 1.11 g/mL. Find molality. (M_NaCl = 58.5) 🟡 ⭐⭐

**Solution:**
```
Formula: m = (M × 1000) / (d × 1000 - M × M_solute)

    m = (3 × 1000) / (1.11 × 1000 - 3 × 58.5)
    m = 3000 / (1110 - 175.5)
    m = 3000 / 934.5
    m = 3.21 mol/kg

First principles (1 L of solution):
    Moles of NaCl = 3 mol
    Mass of solution = 1110 g
    Mass of NaCl = 175.5 g
    Mass of solvent = 1110 - 175.5 = 934.5 g = 0.9345 kg
    m = 3/0.9345 = 3.21 ✅

Answer: m ≈ 3.21 mol/kg
```

#### Solved Example 11.3B (m → M)
**Q:** 2 m urea (M = 60) solution, d = 1.05 g/mL. Find molarity. 🟡 ⭐

**Solution:**
```
Formula: M = (m × d × 1000) / (1000 + m × M_solute)

    M = (2 × 1.05 × 1000) / (1000 + 2 × 60)
    M = 2100 / 1120
    M = 1.875 M

First principles (1 kg of solvent):
    Moles = 2 mol
    Mass of solute = 120 g
    Mass of solution = 1120 g
    Volume = 1120/1.05 = 1066.7 mL = 1.0667 L
    M = 2/1.0667 = 1.875 ✅

Answer: M ≈ 1.88 M
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.3a"></span>11.3a | 2 M glucose (M=180), d = 1.09 g/mL. Find m. ⭐ | 🟡 |
| <span id="q-11.3b"></span>11.3b | 5 m NaOH (M=40), d = 1.18 g/mL. Find M. ⭐ | 🟡 |
| <span id="q-11.3c"></span>11.3c | 18 M H₂SO₄, d = 1.84 g/mL, M=98. Find m. ⭐⭐ | 🔴 |
| <span id="q-11.3d"></span>11.3d | If M = m for a solution, what is the density? (M_solute = 100) Derive the general condition. ⭐⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**11.3a**: Answer not found.
**11.3b**: Answer not found.
**11.3c**: Answer not found.
**11.3d**: Answer not found.

</details>


---

### Type 4: Mole Fraction ↔ Molality ⭐

**The Pattern:** No density needed. Direct mathematical relationship.

#### Solved Example 11.4
**Q:** χ_ethanol = 0.2 in ethanol-water solution. Find molality. (M_water = 18) 🟡

**Solution:**
```
Formula: m = (1000 × χ_solute) / ((1 - χ_solute) × M_solvent)

    m = (1000 × 0.2) / ((1 - 0.2) × 18)
    m = 200 / (0.8 × 18)
    m = 200 / 14.4
    m = 13.89 mol/kg

Answer: m ≈ 13.89 mol/kg

Reverse check: χ = (m × M_solvent)/(1000 + m × M_solvent) 
             = (13.89 × 18)/(1000 + 13.89 × 18)
             = 250/1250 = 0.2 ✅
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.4a"></span>11.4a | χ_urea = 0.05 in water. Find m. (M_water = 18) ⭐ | 🟡 |
| <span id="q-11.4b"></span>11.4b | m = 5 (solvent = water). Find χ_solute. | 🟡 |
| <span id="q-11.4c"></span>11.4c | χ_solute = 0.1, solvent = benzene (M=78). Find m. | 🟡 |

<details>
<summary>View Answers</summary>

**11.4a**: Answer not found.
**11.4b**: Answer not found.
**11.4c**: Answer not found.

</details>


---

### Type 5: Mole Fraction ↔ Molarity (density given) ⭐

**The Pattern:** Requires density. Usually done as a two-step: χ → m → M, or directly using the formula.

#### Solved Example 11.5
**Q:** χ_NaOH = 0.1 in aqueous solution. d = 1.15 g/mL. Find molarity. (M_NaOH = 40, M_water = 18) 🔴 ⭐

**Solution:**
```
Direct formula:
    M = (χ × d × 1000) / (χ × M_solute + (1-χ) × M_solvent)
    M = (0.1 × 1.15 × 1000) / (0.1 × 40 + 0.9 × 18)
    M = 115 / (4 + 16.2)
    M = 115 / 20.2
    M = 5.69 M

Two-step verification:
    Step 1: χ → m
        m = (1000 × 0.1)/(0.9 × 18) = 100/16.2 = 6.17 m
    Step 2: m → M
        M = (6.17 × 1.15 × 1000)/(1000 + 6.17 × 40) = 7095.5/1246.8 = 5.69 ✅

Answer: M ≈ 5.69 M
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.5a"></span>11.5a | χ_glucose = 0.05, d = 1.05 g/mL. Find M. (M_glucose = 180, M_water = 18) | 🔴 |
| <span id="q-11.5b"></span>11.5b | 4 M NaCl (M=58.5), d = 1.13 g/mL. Find χ_NaCl. (Reverse) ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**11.5a**: Answer not found.
**11.5b**: Answer not found.

</details>


---

### Type 6: Chain Conversion — w/w% → M → m → χ ⭐⭐⭐

**The Pattern:** Multi-step conversion in a single problem. The ultimate test.

#### Solved Example 11.6
**Q:** A solution of H₂SO₄ is 49% by mass with density 1.39 g/mL. Find: (a) Molarity (b) Molality (c) Mole fraction of H₂SO₄. (M = 98, M_water = 18) 🔴 ⭐⭐

**Solution:**
```
(a) w/w% → Molarity
    M = (49 × 1.39 × 10) / 98
    M = 681.1 / 98
    M = 6.95 M

(b) w/w% → Molality (no density needed!)
    m = (49 × 1000) / (98 × 51)
    m = 49000 / 4998
    m = 9.80 mol/kg

(c) Molality → Mole fraction (or directly from w/w%)
    χ = (m × M_solvent) / (1000 + m × M_solvent)
    χ = (9.80 × 18) / (1000 + 9.80 × 18)
    χ = 176.4 / (1000 + 176.4)
    χ = 176.4 / 1176.4
    χ = 0.15

    Direct from 100 g:
    n_H₂SO₄ = 49/98 = 0.5 mol
    n_water = 51/18 = 2.833 mol
    χ = 0.5/(0.5 + 2.833) = 0.5/3.333 = 0.15 ✅

Answer: (a) 6.95 M  (b) 9.80 m  (c) χ = 0.15
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.6a"></span>11.6a | 10% NaOH (M=40), d = 1.11 g/mL. Find M, m, χ. ⭐⭐ | 🔴 |
| <span id="q-11.6b"></span>11.6b | 30% glucose (M=180), d = 1.13 g/mL. Find M, m, χ. | 🔴 |
| <span id="q-11.6c"></span>11.6c | 40% urea (M=60), d = 1.09 g/mL. Find all four: M, m, χ, and N (n=1). | 🔴 |

<details>
<summary>View Answers</summary>

**11.6a**: Answer not found.
**11.6b**: Answer not found.
**11.6c**: Answer not found.

</details>


---

### Type 7: Reverse Derivation — Given M + m → Find Density ⭐⭐

**The Pattern:** If both molarity and molality are known, density can be calculated.

#### Derivation
```
From M → m formula:
    m = (M × 1000) / (d × 1000 - M × M_solute)

Rearranging for d:
    m × (d × 1000 - M × M_solute) = M × 1000
    d × 1000 × m - m × M × M_solute = M × 1000
    d = (M × 1000 + m × M × M_solute) / (m × 1000)
    d = M/m + (M × M_solute)/1000

Simplified:
    d = (M/m) × (1 + m × M_solute/1000)

Or equivalently:
    d = (M × (1000 + m × M_solute)) / (m × 1000)
```

#### Solved Example 11.7
**Q:** A solution has M = 4 (molarity) and m = 5 (molality). M_solute = 60. Find the density. 🔴 ⭐

**Solution:**
```
From relationship:
    m = (M × 1000) / (d × 1000 - M × M_solute)

    5 = (4 × 1000) / (d × 1000 - 4 × 60)
    5 = 4000 / (1000d - 240)
    5(1000d - 240) = 4000
    5000d - 1200 = 4000
    5000d = 5200
    d = 1.04 g/mL

Answer: d = 1.04 g/mL
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.7a"></span>11.7a | M = 2, m = 2.5, M_solute = 40. Find d. ⭐ | 🔴 |
| <span id="q-11.7b"></span>11.7b | M = 10, m = 12, M_solute = 98 (H₂SO₄). Find d. | 🔴 |
| <span id="q-11.7c"></span>11.7c | If M = m, show that d = 1 + M × M_solute/1000. For water as solvent and M_solute = 100, d = ? | 🔴 |

<details>
<summary>View Answers</summary>

**11.7a**: Answer not found.
**11.7b**: Answer not found.
**11.7c**: Answer not found.

</details>


---

### Type 8: Real Commercial Solution Analysis ⭐⭐⭐

**The Pattern:** Given a commercial acid's label data → find ALL concentration terms.

#### Solved Example 11.8
**Q:** A bottle of concentrated H₂SO₄ reads: "98% w/w, d = 1.84 g/mL". (M = 98, M_water = 18). Find: (a) Molarity (b) Molality (c) Mole fraction (d) Normality. 🔴 ⭐⭐⭐

**Solution:**
```
(a) Molarity
    M = (98 × 1.84 × 10) / 98 = 18.4 M

(b) Molality
    m = (98 × 1000) / (98 × (100 - 98))
    m = 98000 / (98 × 2)
    m = 98000 / 196
    m = 500 mol/kg  (!!!)

    This is correct — concentrated H₂SO₄ has almost no water.
    In 100 g: 98 g acid (1 mol) + 2 g water (0.111 mol)
    m = 1/0.002 = 500 ✅

(c) Mole fraction
    In 100 g of solution:
    n_H₂SO₄ = 98/98 = 1 mol
    n_H₂O = 2/18 = 0.111 mol
    χ_H₂SO₄ = 1/(1 + 0.111) = 1/1.111 = 0.9

    H₂SO₄ dominates — it's almost pure acid!

(d) Normality (for complete neutralization, n = 2)
    N = n-factor × M = 2 × 18.4 = 36.8 N

Answer: (a) 18.4 M  (b) 500 m  (c) 0.9  (d) 36.8 N
```

> **Key insight:** Concentrated H₂SO₄ is 98% acid and only 2% water. That's why molality is astronomically high (500 m!) — there's almost no solvent. This is a reality check that tests deep understanding.

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.8a"></span>11.8a | Conc. HCl: 37%, d = 1.19, M = 36.5. Find M, m, χ, N. ⭐⭐ | 🔴 |
| <span id="q-11.8b"></span>11.8b | Conc. HNO₃: 68%, d = 1.41, M = 63. Find M, m, χ. ⭐ | 🔴 |
| <span id="q-11.8c"></span>11.8c | Glacial acetic acid: 99.7%, d = 1.049, M = 60. Find M, m, χ. ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**11.8a**: Answer not found.
**11.8b**: Answer not found.
**11.8c**: Answer not found.

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-11.M1"></span>11.M1 | A solution has m = 3, d = 1.08 g/mL, M_solute = 60. Find (a) M (b) w/w% (c) χ (d) N (if n=1). | T3 + T2 + T4 | 🔴 |
| <span id="q-11.M2"></span>11.M2 | Given: χ_solute = 0.2, M_solute = 100, M_solvent = 18, d = 1.2 g/mL. Complete the chain: χ → m → M → w/w% → N (n=2). | T4 + T3 + T1 + Ch7 | 🔴 |
| <span id="q-11.M3"></span>11.M3 | 5 M NaOH (M=40), d = 1.19. Find m. Then verify by converting m back to M. Round-trip check! | T3 (both ways) | 🟡 |

<details>
<summary>View Answers</summary>

**11.M1**: Answer not found.
**11.M2**: Answer not found.
**11.M3**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.B1"></span>11.B1 | A 10% (w/w) solution of NaOH (M=40) has density 1.11 g/mL. Find (a) molarity (b) molality. ⭐⭐ | 🟡 |
| <span id="q-11.B2"></span>11.B2 | Calculate the mole fraction and molality of a 20% (w/w) aqueous solution of glucose (M=180). ⭐ | 🟡 |
| <span id="q-11.B3"></span>11.B3 | Concentrated HCl is 37% (w/w), d = 1.19 g/mL. Find molarity. If 10 mL is diluted to 500 mL, find new M. ⭐ | 🟡 |
| <span id="q-11.B4"></span>11.B4 | A 4 M NaCl solution (M=58.5) has d = 1.13 g/mL. Find (a) w/w% (b) molality. | 🟡 |

<details>
<summary>View Answers</summary>

**11.B1**: Answer not found.
**11.B2**: Answer not found.
**11.B3**: Answer not found.
**11.B4**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-11.J1"></span>11.J1 | Conc. H₂SO₄ (98%, d=1.84, M=98). Find ALL: M, m, χ, N. Then find volume needed for 500 mL of 0.1 M. ⭐⭐⭐ | 🔴 |
| <span id="q-11.J2"></span>11.J2 | A solution has M = 5 and m = 6. M_solute = 80. Find (a) density (b) w/w% (c) mole fraction. ⭐⭐ | 🔴 |
| <span id="q-11.J3"></span>11.J3 | Two solutions: Sol A (M_A = 4, d_A = 1.2, M_solute = 60) and Sol B (m_B = 5, M_solute = 60, M_solvent = 18). (a) Find m_A and M_B (if d_B = 1.15). (b) Are they the same solution? | 🔴 |
| <span id="q-11.J4"></span>11.J4 | An aqueous solution has the property that its molarity equals its molality (M = m). Derive a general formula for the density of such a solution in terms of M_solute. For M_solute = 180 (glucose), find d. ⭐⭐ | 🔴 |
| <span id="q-11.J5"></span>11.J5 | Given only that a 2.5 m aqueous glucose (M=180) solution has d = 1.07 g/mL, find ALL of: M, w/w%, χ, N (n=1), and ppm (for comparison). ⭐⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**11.J1**: Answer not found.
**11.J2**: Answer not found.
**11.J3**: Answer not found.
**11.J4**: Answer not found.
**11.J5**: Answer not found.

</details>


---

## Quick Reference: "Which Formula When?"

```
┌─────────────────────────────────────────────────────────────┐
│                 CONVERSION DECISION TREE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Q: Do you HAVE density?                                     │
│                                                              │
│  YES → You can convert TO/FROM Molarity                     │
│        • w/w% + d → M: use (% × d × 10)/M_s               │
│        • m + d → M: use (m × d × 1000)/(1000 + m × M_s)   │
│        • M + d → m: use (M × 1000)/(d×1000 - M × M_s)     │
│        • χ + d → M: use (χ × d × 1000)/M_avg              │
│                                                              │
│  NO → You can ONLY convert among w/w%, m, and χ             │
│       • w/w% → m: (% × 1000)/((100-%) × M_s)              │
│       • χ → m: (1000 × χ)/((1-χ) × M_solvent)             │
│       • These three are "mass-only" terms                    │
│                                                              │
│  HAVE both M and m?                                          │
│       → You can FIND density!                                │
│       d = M(1000 + m × M_s)/(m × 1000)                     │
│                                                              │
│  NEED Normality?                                             │
│       → Find M first, then N = n-factor × M                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways from Chapter 11

```
┌──────────────────────────────────────────────────────────────┐
│              INTERCONVERSION SUMMARY                          │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  RULE #1: Any conversion involving Molarity needs density    │
│                                                               │
│  RULE #2: w/w%, m, χ are interconvertible WITHOUT density   │
│                                                               │
│  RULE #3: If you forget a formula, use:                       │
│           "Consider 100 g of solution" (for %, m, χ)         │
│           "Consider 1 L of solution" (for M)                 │
│                                                               │
│  RULE #4: Given M and m → find density                       │
│           Given M and d → find m                             │
│           Given m and d → find M                             │
│           Given % and d → find everything                    │
│                                                               │
│  THE BIG FIVE conversions to master:                          │
│    1. w/w% → M (⭐⭐⭐)                                      │
│    2. M ↔ m (⭐⭐⭐)                                          │
│    3. w/w% → m (⭐⭐)                                        │
│    4. χ → m (⭐⭐)                                           │
│    5. Commercial acid analysis (⭐⭐⭐)                       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 10 — Ionic Concentration](./10-ionic-concentration.md) | [Chapter 12 — Comprehensive Problems →](./12-comprehensive-problems.md)*
