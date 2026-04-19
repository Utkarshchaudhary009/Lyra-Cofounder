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
| 11.1a | 10% KOH (M=56), d = 1.09 g/mL. Find M. ⭐ | 🟡 |
| 11.1b | 37% HCl (M=36.5), d = 1.19 g/mL. Find M. ⭐⭐ | 🟡 |
| 11.1c | 3 M glucose (M=180), d = 1.12 g/mL. Find w/w%. | 🟡 |
| 11.1d | 68% HNO₃ (M=63), d = 1.41 g/mL. Find M. ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**11.1a:**
*   **Calculation:** $M = \frac{w/w\% \times d \times 10}{M_{\text{solute}}} = \frac{10 \times 1.09 \times 10}{56} = \frac{109}{56} = 1.946\text{ M}$.
*   **Answer:** $1.95\text{ M}$

**11.1b:**
*   **Calculation:** $M = \frac{37 \times 1.19 \times 10}{36.5} = \frac{440.3}{36.5} = 12.06\text{ M}$.
*   **Answer:** $12.06\text{ M}$

**11.1c:**
*   **Calculation:** Rearrange: $w/w\% = \frac{M \times M_{\text{solute}}}{d \times 10} = \frac{3 \times 180}{1.12 \times 10} = \frac{540}{11.2} = 48.21\%$.
*   **Answer:** $48.21\%$

**11.1d:**
*   **Calculation:** $M = \frac{68 \times 1.41 \times 10}{63} = \frac{958.8}{63} = 15.22\text{ M}$.
*   **Answer:** $15.22\text{ M}$

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
| 11.2a | 5% urea (M=60). Find m. | 🟡 |
| 11.2b | 98% H₂SO₄ (M=98). Find m. ⭐ | 🟡 |
| 11.2c | m = 2.5, M_solute = 40 (NaOH). Find w/w%. (Reverse) | 🟡 |
| 11.2d | 25% NaCl (M=58.5). Find m. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**11.2a:**
*   **Calculation:** $m = \frac{w/w\% \times 1000}{M_{\text{solute}} \times (100 - w/w\%)} = \frac{5 \times 1000}{60 \times 95} = \frac{5000}{5700} = 0.877\text{ m}$.
*   **Answer:** $0.88\text{ mol/kg}$

**11.2b:**
*   **Calculation:** $m = \frac{98 \times 1000}{98 \times 2} = \frac{1000}{2} = 500\text{ m}$! (Concentrated acid has very little solvent).
*   **Answer:** $500\text{ mol/kg}$

**11.2c:**
*   **Calculation:** $w/w\% = \frac{m \times M_{\text{solute}} \times 100}{1000 + m \times M_{\text{solute}}} = \frac{2.5 \times 40 \times 100}{1000 + 2.5 \times 40} = \frac{10000}{1100} = 9.09\%$.
*   **Answer:** $9.09\%$

**11.2d:**
*   **Calculation:** $m = \frac{25 \times 1000}{58.5 \times 75} = \frac{25000}{4387.5} = 5.698\text{ m}$.
*   **Answer:** $5.70\text{ mol/kg}$

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
| 11.3a | 2 M glucose (M=180), d = 1.09 g/mL. Find m. ⭐ | 🟡 |
| 11.3b | 5 m NaOH (M=40), d = 1.18 g/mL. Find M. ⭐ | 🟡 |
| 11.3c | 18 M H₂SO₄, d = 1.84 g/mL, M=98. Find m. ⭐⭐ | 🔴 |
| 11.3d | If M = m for a solution, what is the density? (M_solute = 100) Derive the general condition. ⭐⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**11.3a:**
*   **Calculation:** $m = \frac{M \times 1000}{d \times 1000 - M \times M_{\text{solute}}} = \frac{2 \times 1000}{1.09 \times 1000 - 2 \times 180} = \frac{2000}{1090 - 360} = \frac{2000}{730} = 2.74\text{ m}$.
*   **Answer:** $2.74\text{ mol/kg}$

**11.3b:**
*   **Calculation:** $M = \frac{m \times d \times 1000}{1000 + m \times M_{\text{solute}}} = \frac{5 \times 1.18 \times 1000}{1000 + 5 \times 40} = \frac{5900}{1200} = 4.917\text{ M}$.
*   **Answer:** $4.92\text{ M}$

**11.3c:**
*   **Calculation:** $m = \frac{18 \times 1000}{1.84 \times 1000 - 18 \times 98} = \frac{18000}{1840 - 1764} = \frac{18000}{76} = 236.8\text{ m}$.
*   **Answer:** $236.8\text{ mol/kg}$

**11.3d:**
*   **Calculation:** Start with $m = \frac{M \times 1000}{d \times 1000 - M \times M_{\text{solute}}}$. Let $M = m = x$.
    $x = \frac{x \times 1000}{d \times 1000 - x \times M_{\text{solute}}}$. Divide by $x$: $1 = \frac{1000}{d \times 1000 - x \times M_{\text{solute}}}$.
    $d \times 1000 - M \times M_{\text{solute}} = 1000 \Rightarrow d = \frac{1000 + M \times M_{\text{solute}}}{1000} = 1 + \frac{M \times M_{\text{solute}}}{1000}$.
    If $M_{\text{solute}} = 100$, then $d = 1 + \frac{100 M}{1000} = 1 + 0.1 M$.
*   **Answer:** $d = 1 + \frac{M \times M_{\text{solute}}}{1000}$; for $M_{\text{solute}} = 100$, $d = 1 + 0.1 M$

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
| 11.4a | χ_urea = 0.05 in water. Find m. (M_water = 18) ⭐ | 🟡 |
| 11.4b | m = 5 (solvent = water). Find χ_solute. | 🟡 |
| 11.4c | χ_solute = 0.1, solvent = benzene (M=78). Find m. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**11.4a:**
*   **Calculation:** $m = \frac{1000 \times \chi_{\text{solute}}}{(1 - \chi_{\text{solute}}) \times M_{\text{solvent}}} = \frac{1000 \times 0.05}{0.95 \times 18} = \frac{50}{17.1} = 2.92\text{ m}$.
*   **Answer:** $2.92\text{ mol/kg}$

**11.4b:**
*   **Calculation:** $\chi = \frac{m \times M_{\text{solvent}}}{1000 + m \times M_{\text{solvent}}} = \frac{5 \times 18}{1000 + 5 \times 18} = \frac{90}{1090} = 0.0826$.
*   **Answer:** $0.0826$

**11.4c:**
*   **Calculation:** $m = \frac{1000 \times 0.1}{0.9 \times 78} = \frac{100}{70.2} = 1.42\text{ m}$.
*   **Answer:** $1.42\text{ mol/kg}$

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
| 11.5a | χ_glucose = 0.05, d = 1.05 g/mL. Find M. (M_glucose = 180, M_water = 18) | 🔴 |
| 11.5b | 4 M NaCl (M=58.5), d = 1.13 g/mL. Find χ_NaCl. (Reverse) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**11.5a:**
*   **Calculation:** $M = \frac{\chi \times d \times 1000}{\chi \times M_{\text{solute}} + (1 - \chi) \times M_{\text{solvent}}} = \frac{0.05 \times 1.05 \times 1000}{0.05 \times 180 + 0.95 \times 18} = \frac{52.5}{9 + 17.1} = \frac{52.5}{26.1} = 2.01\text{ M}$.
*   **Answer:** $2.01\text{ M}$

**11.5b:**
*   **Calculation:** First, find m: $m = \frac{M \times 1000}{d \times 1000 - M \times M_{\text{solute}}} = \frac{4 \times 1000}{1130 - 4 \times 58.5} = \frac{4000}{1130 - 234} = \frac{4000}{896} = 4.464\text{ m}$.
    Then, find $\chi$: $\chi = \frac{m \times 18}{1000 + m \times 18} = \frac{4.464 \times 18}{1000 + 4.464 \times 18} = \frac{80.35}{1080.35} = 0.0744$.
*   **Answer:** $0.074$

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
| 11.6a | 10% NaOH (M=40), d = 1.11 g/mL. Find M, m, χ. ⭐⭐ | 🔴 |
| 11.6b | 30% glucose (M=180), d = 1.13 g/mL. Find M, m, χ. | 🔴 |
| 11.6c | 40% urea (M=60), d = 1.09 g/mL. Find all four: M, m, χ, and N (n=1). | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**11.6a:**
*   **Calculation:** 
    $M = \frac{10 \times 1.11 \times 10}{40} = 2.775\text{ M}$.
    $m = \frac{10 \times 1000}{40 \times 90} = \frac{10000}{3600} = 2.778\text{ mol/kg}$.
    $\chi$: $n_{\text{NaOH}} = \frac{10}{40} = 0.25$, $n_{\text{water}} = \frac{90}{18} = 5$. $\chi = \frac{0.25}{5.25} = 0.0476$.
*   **Answer:** $M = 2.775\text{ M}$, $m = 2.778\text{ m}$, $\chi = 0.0476$

**11.6b:**
*   **Calculation:**
    $M = \frac{30 \times 1.13 \times 10}{180} = \frac{339}{180} = 1.883\text{ M}$.
    $m = \frac{30 \times 1000}{180 \times 70} = \frac{30000}{12600} = 2.38\text{ mol/kg}$.
    $\chi$: $n_{\text{glucose}} = \frac{30}{180} = 0.1667$, $n_{\text{water}} = \frac{70}{18} = 3.889$. $\chi = \frac{0.1667}{0.1667 + 3.889} = \frac{0.1667}{4.055} = 0.0411$.
*   **Answer:** $M = 1.88\text{ M}$, $m = 2.38\text{ m}$, $\chi = 0.041$

**11.6c:**
*   **Calculation:**
    $M = \frac{40 \times 1.09 \times 10}{60} = \frac{436}{60} = 7.267\text{ M}$.
    $m = \frac{40 \times 1000}{60 \times 60} = \frac{40000}{3600} = 11.11\text{ mol/kg}$.
    $\chi$: $n_{\text{urea}} = \frac{40}{60} = 0.667$, $n_{\text{water}} = \frac{60}{18} = 3.333$. $\chi = \frac{0.667}{0.667 + 3.333} = \frac{0.667}{4} = 0.167$.
    $N = M \times n_{\text{factor}} = 7.267 \times 1 = 7.267\text{ N}$.
*   **Answer:** $M = 7.27\text{ M}$, $m = 11.11\text{ m}$, $\chi = 0.167$, $N = 7.27\text{ N}$

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
| 11.7a | M = 2, m = 2.5, M_solute = 40. Find d. ⭐ | 🔴 |
| 11.7b | M = 10, m = 12, M_solute = 98 (H₂SO₄). Find d. | 🔴 |
| 11.7c | If M = m, show that d = 1 + M × M_solute/1000. For water as solvent and M_solute = 100, d = ? | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**11.7a:**
*   **Calculation:** $d = \frac{M}{m} + \frac{M \times M_{\text{solute}}}{1000} = \frac{2}{2.5} + \frac{2 \times 40}{1000} = 0.8 + 0.08 = 0.88\text{ g/mL}$.
*   **Answer:** $0.88\text{ g/mL}$

**11.7b:**
*   **Calculation:** $d = \frac{M}{m} + \frac{M \times M_{\text{solute}}}{1000} = \frac{10}{12} + \frac{10 \times 98}{1000} = 0.833 + 0.98 = 1.813\text{ g/mL}$.
*   **Answer:** $1.813\text{ g/mL}$

**11.7c:**
*   **Calculation:** Since $M = m$, $d = \frac{M}{M} + \frac{M \times M_{\text{solute}}}{1000} = 1 + \frac{M \times M_{\text{solute}}}{1000}$.
    For $M_{\text{solute}} = 100$, $d = 1 + \frac{100 M}{1000} = 1 + 0.1 M$.
*   **Answer:** $d = 1 + \frac{M \times M_{\text{solute}}}{1000}$; $d = 1 + 0.1 M$

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
| 11.8a | Conc. HCl: 37%, d = 1.19, M = 36.5. Find M, m, χ, N. ⭐⭐ | 🔴 |
| 11.8b | Conc. HNO₃: 68%, d = 1.41, M = 63. Find M, m, χ. ⭐ | 🔴 |
| 11.8c | Glacial acetic acid: 99.7%, d = 1.049, M = 60. Find M, m, χ. ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**11.8a:**
*   **Calculation:**
    $M = \frac{37 \times 1.19 \times 10}{36.5} = \frac{440.3}{36.5} = 12.06\text{ M}$.
    $m = \frac{37 \times 1000}{36.5 \times 63} = \frac{37000}{2299.5} = 16.09\text{ m}$.
    $\chi$: $n_{\text{HCl}} = \frac{37}{36.5} = 1.0137$, $n_{\text{water}} = \frac{63}{18} = 3.5$. $\chi_{\text{HCl}} = \frac{1.0137}{1.0137 + 3.5} = 0.224$.
    $N = M \times 1 = 12.06\text{ N}$.
*   **Answer:** $M = 12.06\text{ M}$, $m = 16.09\text{ m}$, $\chi = 0.224$, $N = 12.06\text{ N}$

**11.8b:**
*   **Calculation:**
    $M = \frac{68 \times 1.41 \times 10}{63} = \frac{958.8}{63} = 15.22\text{ M}$.
    $m = \frac{68 \times 1000}{63 \times 32} = \frac{68000}{2016} = 33.73\text{ m}$.
    $\chi$: $n_{\text{HNO}_3} = \frac{68}{63} = 1.079$, $n_{\text{water}} = \frac{32}{18} = 1.778$. $\chi_{\text{HNO}_3} = \frac{1.079}{1.079 + 1.778} = 0.378$.
*   **Answer:** $M = 15.22\text{ M}$, $m = 33.73\text{ m}$, $\chi = 0.378$

**11.8c:**
*   **Calculation:**
    $M = \frac{99.7 \times 1.049 \times 10}{60} = \frac{1045.85}{60} = 17.43\text{ M}$.
    $m = \frac{99.7 \times 1000}{60 \times 0.3} = \frac{99700}{18} = 5538.9\text{ m}$. (almost pure acid)
    $\chi$: $n_{\text{acid}} = \frac{99.7}{60} = 1.6617$, $n_{\text{water}} = \frac{0.3}{18} = 0.0167$. $\chi_{\text{acid}} = \frac{1.6617}{1.6617 + 0.0167} = 0.99$.
*   **Answer:** $M = 17.43\text{ M}$, $m = 5539\text{ m}$, $\chi = 0.99$

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 11.M1 | A solution has m = 3, d = 1.08 g/mL, M_solute = 60. Find (a) M (b) w/w% (c) χ (d) N (if n=1). | T3 + T2 + T4 | 🔴 |
| 11.M2 | Given: χ_solute = 0.2, M_solute = 100, M_solvent = 18, d = 1.2 g/mL. Complete the chain: χ → m → M → w/w% → N (n=2). | T4 + T3 + T1 + Ch7 | 🔴 |
| 11.M3 | 5 M NaOH (M=40), d = 1.19. Find m. Then verify by converting m back to M. Round-trip check! | T3 (both ways) | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**11.M1:**
*   **Calculation:** 
    (a) $M = \frac{m \times d \times 1000}{1000 + m \times M_{\text{solute}}} = \frac{3 \times 1.08 \times 1000}{1000 + 3 \times 60} = \frac{3240}{1180} = 2.746\text{ M}$.
    (b) $w/w\% = \frac{m \times M_{\text{solute}} \times 100}{1000 + m \times M_{\text{solute}}} = \frac{3 \times 60 \times 100}{1180} = \frac{18000}{1180} = 15.25\%$.
    (c) $\chi = \frac{m \times M_{\text{solvent}}}{1000 + m \times M_{\text{solvent}}} = \frac{3 \times 18}{1000 + 3 \times 18} = \frac{54}{1054} = 0.0512$.
    (d) $N = M \times 1 = 2.75\text{ N}$.
*   **Answer:** (a) $2.75\text{ M}$, (b) $15.25\%$, (c) $0.051$, (d) $2.75\text{ N}$

**11.M2:**
*   **Calculation:**
    $\chi \rightarrow m$: $m = \frac{1000 \times 0.2}{0.8 \times 18} = \frac{200}{14.4} = 13.89\text{ m}$.
    $m \rightarrow M$: $M = \frac{13.89 \times 1.2 \times 1000}{1000 + 13.89 \times 100} = \frac{16668}{2389} = 6.977\text{ M}$.
    $M \rightarrow w/w\%$: $w/w\% = \frac{M \times M_{\text{solute}}}{d \times 10} = \frac{6.977 \times 100}{1.2 \times 10} = \frac{697.7}{12} = 58.14\%$.
    $M \rightarrow N$: $N = M \times 2 = 6.977 \times 2 = 13.95\text{ N}$.
*   **Answer:** $m = 13.89\text{ m}$, $M = 6.98\text{ M}$, $w/w\% = 58.1\%$, $N = 13.95\text{ N}$

**11.M3:**
*   **Calculation:**
    $m = \frac{5 \times 1000}{1.19 \times 1000 - 5 \times 40} = \frac{5000}{1190 - 200} = \frac{5000}{990} = 5.05\text{ m}$.
    Verify: $M = \frac{5.05 \times 1.19 \times 1000}{1000 + 5.05 \times 40} = \frac{6009.5}{1000 + 202} = \frac{6009.5}{1202} = 5.00\text{ M}$ ✅.
*   **Answer:** $m = 5.05\text{ m}$, Round-trip verified.

</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 11.B1 | A 10% (w/w) solution of NaOH (M=40) has density 1.11 g/mL. Find (a) molarity (b) molality. ⭐⭐ | 🟡 |
| 11.B2 | Calculate the mole fraction and molality of a 20% (w/w) aqueous solution of glucose (M=180). ⭐ | 🟡 |
| 11.B3 | Concentrated HCl is 37% (w/w), d = 1.19 g/mL. Find molarity. If 10 mL is diluted to 500 mL, find new M. ⭐ | 🟡 |
| 11.B4 | A 4 M NaCl solution (M=58.5) has d = 1.13 g/mL. Find (a) w/w% (b) molality. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**11.B1:**
*   **Calculation:**
    (a) $M = \frac{10 \times 1.11 \times 10}{40} = 2.775\text{ M}$.
    (b) $m = \frac{10 \times 1000}{40 \times 90} = \frac{10000}{3600} = 2.778\text{ m}$.
*   **Answer:** (a) $2.78\text{ M}$, (b) $2.78\text{ m}$

**11.B2:**
*   **Calculation:**
    $w/w\% \rightarrow m$: $m = \frac{20 \times 1000}{180 \times 80} = \frac{20000}{14400} = 1.389\text{ m}$.
    $m \rightarrow \chi$: $\chi = \frac{1.389 \times 18}{1000 + 1.389 \times 18} = \frac{25}{1025} = 0.0244$.
*   **Answer:** $m = 1.39\text{ m}$, $\chi = 0.0244$

**11.B3:**
*   **Calculation:**
    Initial $M: M = \frac{37 \times 1.19 \times 10}{36.5} = 12.06\text{ M}$.
    Dilution: $12.06 \times 10 = M_2 \times 500 \Rightarrow M_2 = \frac{120.6}{500} = 0.241\text{ M}$.
*   **Answer:** Initial $M = 12.06\text{ M}$, New $M = 0.241\text{ M}$

**11.B4:**
*   **Calculation:**
    (a) $w/w\% = \frac{4 \times 58.5}{1.13 \times 10} = \frac{234}{11.3} = 20.71\%$.
    (b) $m = \frac{4 \times 1000}{1130 - 4 \times 58.5} = \frac{4000}{1130 - 234} = \frac{4000}{896} = 4.464\text{ m}$.
*   **Answer:** (a) $20.7\%$, (b) $4.46\text{ mol/kg}$

</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 11.J1 | Conc. H₂SO₄ (98%, d=1.84, M=98). Find ALL: M, m, χ, N. Then find volume needed for 500 mL of 0.1 M. ⭐⭐⭐ | 🔴 |
| 11.J2 | A solution has M = 5 and m = 6. M_solute = 80. Find (a) density (b) w/w% (c) mole fraction. ⭐⭐ | 🔴 |
| 11.J3 | Two solutions: Sol A (M_A = 4, d_A = 1.2, M_solute = 60) and Sol B (m_B = 5, M_solute = 60, M_solvent = 18). (a) Find m_A and M_B (if d_B = 1.15). (b) Are they the same solution? | 🔴 |
| 11.J4 | An aqueous solution has the property that its molarity equals its molality (M = m). Derive a general formula for the density of such a solution in terms of M_solute. For M_solute = 180 (glucose), find d. ⭐⭐ | 🔴 |
| 11.J5 | Given only that a 2.5 m aqueous glucose (M=180) solution has d = 1.07 g/mL, find ALL of: M, w/w%, χ, N (n=1), and ppm (for comparison). ⭐⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**11.J1:**
*   **Calculation:**
    Found in Ex 11.8: $M = 18.4\text{ M}$, $m = 500\text{ m}$, $\chi = 0.9$, $N = 36.8\text{ N}$.
    Volume needed: $M_1 V_1 = M_2 V_2 \Rightarrow 18.4 \times V_1 = 0.1 \times 500 \Rightarrow V_1 = \frac{50}{18.4} = 2.717\text{ mL}$.
*   **Answer:** $M = 18.4, m = 500, \chi = 0.9, N = 36.8$; $V = 2.72\text{ mL}$

**11.J2:**
*   **Calculation:**
    (a) $d = \frac{M}{m} + \frac{M \times M_{\text{solute}}}{1000} = \frac{5}{6} + \frac{5 \times 80}{1000} = 0.833 + 0.4 = 1.233\text{ g/mL}$.
    (b) $w/w\% = \frac{M \times M_{\text{solute}}}{d \times 10} = \frac{5 \times 80}{12.33} = \frac{400}{12.33} = 32.44\%$.
    (c) $\chi = \frac{m \times 18}{1000 + m \times 18} = \frac{6 \times 18}{1000 + 108} = \frac{108}{1108} = 0.097$.
*   **Answer:** (a) $1.233\text{ g/mL}$, (b) $32.4\%$, (c) $0.097$

**11.J3:**
*   **Calculation:**
    Sol A: $m_A = \frac{4 \times 1000}{1200 - 4 \times 60} = \frac{4000}{960} = 4.167\text{ m}$.
    Sol B: $M_B = \frac{5 \times 1.15 \times 1000}{1000 + 5 \times 60} = \frac{5750}{1300} = 4.42\text{ M}$.
    (b) Sol A has $m = 4.167$; Sol B has $m = 5$. They are NOT the same solution (different concentrations).
*   **Answer:** (a) $m_A = 4.17\text{ m}$, $M_B = 4.42\text{ M}$, (b) No, they are different solutions.

**11.J4:**
*   **Calculation:** Let $m=M=x$.
    $x = \frac{x \times 1000}{d \times 1000 - x \times M_{\text{solute}}} \Rightarrow 1000 = d \times 1000 - M \times M_{\text{solute}} \Rightarrow d = 1 + \frac{M \times M_{\text{solute}}}{1000}$.
    For $M_{\text{solute}} = 180$, $d = 1 + \frac{M \times 180}{1000} = 1 + 0.18 M$.
*   **Answer:** $d = 1 + \frac{M \times M_{\text{solute}}}{1000}$; for glucose, $d = 1 + 0.18 M$

**11.J5:**
*   **Calculation:**
    $M = \frac{2.5 \times 1.07 \times 1000}{1000 + 2.5 \times 180} = \frac{2675}{1450} = 1.845\text{ M}$.
    $w/w\% = \frac{2.5 \times 180 \times 100}{1450} = \frac{45000}{1450} = 31.03\%$.
    $\chi = \frac{2.5 \times 18}{1000 + 2.5 \times 18} = \frac{45}{1045} = 0.043$.
    $N = M \times 1 = 1.845\text{ N}$.
    $ppm = 31.03 \times 10^4 = 310,345\text{ ppm}$.
*   **Answer:** $M = 1.85\text{ M}$, $w/w\% = 31.0\%$, $\chi = 0.043$, $N = 1.85\text{ N}$, $ppm = 310,345$

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
