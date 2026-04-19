# Chapter 4: Mole Fraction (χ)
## Part II: Enter the Mole

---

## 🎯 Stage 1: The Core Idea

### What is Mole Fraction?

Until now, we measured concentration using **mass** or **volume**. But chemistry doesn't run on grams — it runs on **moles**. One mole of any substance has the same number of particles (6.022 × 10²³). So if we want to know what fraction of all the particles in a solution belong to the solute, we need **mole fraction**.

> **Analogy:** Imagine a classroom with 30 students and 2 teachers. The "teacher fraction" is 2/32 = 0.0625. It tells you what proportion of all people in the room are teachers. Mole fraction does the exact same thing — but for molecules.

### Why Mole Fraction Matters

| Reason | Details |
|--------|---------|
| **Raoult's Law** | Vapour pressure of a solution: P = χ_solvent × P° |
| **Dalton's Law** | Partial pressure of a gas: P_A = χ_A × P_total |
| **No units** | Mole fraction is a pure ratio — no units, no confusion |
| **Temperature independent** | Based on moles (= number of particles), which don't change with T |
| **Symmetric** | Treats solute and solvent equally — no arbitrary "who is what" |

---

## 🔬 Stage 2: The Formula Lab

### The Formula (Binary Solution)

```
         Moles of component A           n_A
χ_A = ──────────────────────────── = ─────────
       Total moles in solution        n_A + n_B
```

### The Golden Rule

```
χ_A + χ_B = 1     (for binary solutions — ALWAYS)

In general: χ_1 + χ_2 + χ_3 + ... + χ_n = 1  (for any mixture)
```

> **Why does this work?** Because:
> χ_A + χ_B = n_A/(n_A + n_B) + n_B/(n_A + n_B) = (n_A + n_B)/(n_A + n_B) = 1

### From Mass to Mole Fraction — The Bridge

```
Step 1: Convert mass to moles          n = mass / molar mass
Step 2: Find total moles               n_total = n_A + n_B
Step 3: Divide                          χ_A = n_A / n_total
```

### Units Check

- Moles / Moles = **dimensionless** (no units)
- χ is always between 0 and 1
- χ = 0 means the component is absent
- χ = 1 means the component is pure

### Temperature Dependence

Mole fraction is **temperature-independent** ✅

Why? Because moles = number of particles. Heating something doesn't create or destroy particles. Both numerator (n_A) and denominator (n_A + n_B) stay constant.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given moles of solute & solvent, find χ

**The Pattern:** The simplest case. Moles are directly given → plug into formula.

#### Solved Example 4.1
**Q:** A solution contains 3 moles of ethanol and 7 moles of water. Find the mole fraction of ethanol and water. 🟢

**Solution:**
```
Given:
    n_ethanol = 3 mol
    n_water = 7 mol

Step 1: Total moles
    n_total = 3 + 7 = 10 mol

Step 2: Mole fractions
    χ_ethanol = 3/10 = 0.3
    χ_water = 7/10 = 0.7

Verification: 0.3 + 0.7 = 1.0 ✅

Answer: χ_ethanol = 0.3, χ_water = 0.7
```

> **Why this works:** When moles are directly given, it's a straight division. No conversion needed. Always verify that the mole fractions add to 1 — it's a free error-check.

> **⚠️ Common Mistake:** Students sometimes write χ = n_solute/n_solvent instead of n_solute/n_total. The denominator is ALWAYS the total moles, not just the solvent.

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.1a"></span>[4.1a](./answer-key.md#ans-4.1a) | A solution has 2 mol of sugar and 8 mol of water. Find χ_sugar and χ_water. | 🟢 |
| <span id="q-4.1b"></span>[4.1b](./answer-key.md#ans-4.1b) | 0.5 mol acetone is mixed with 4.5 mol chloroform. Find χ of each. | 🟢 |
| <span id="q-4.1c"></span>[4.1c](./answer-key.md#ans-4.1c) | 1.5 mol NaCl is dissolved in 53.5 mol of water. Find χ_NaCl. | 🟢 |
| <span id="q-4.1d"></span>[4.1d](./answer-key.md#ans-4.1d) | A solution has χ_A = 0.35. If n_A = 7 mol, find n_B and χ_B. | 🟡 |

---

### Type 2: Given masses → convert to moles → find χ

**The Pattern:** Masses given, not moles. Convert first, then apply χ formula.

#### Solved Example 4.2
**Q:** 46 g of ethanol (C₂H₅OH) is dissolved in 180 g of water. Find the mole fraction of ethanol. 🟢

**Solution:**
```
Step 1: Calculate moles
    Molar mass of ethanol = 2(12) + 6(1) + 16 = 46 g/mol
    Molar mass of water = 18 g/mol

    n_ethanol = 46/46 = 1 mol
    n_water = 180/18 = 10 mol

Step 2: Total moles
    n_total = 1 + 10 = 11 mol

Step 3: Mole fractions
    χ_ethanol = 1/11 = 0.0909
    χ_water = 10/11 = 0.9091

Verification: 0.0909 + 0.9091 = 1.0 ✅

Answer: χ_ethanol ≈ 0.091, χ_water ≈ 0.909
```

> **Why this works:** The key step is converting mass to moles using n = mass/M. Once you have moles, the formula is the same as Type 1.

> **⚠️ Common Mistake:** Using the wrong molar mass. Always write out the molar mass calculation explicitly. For ethanol: C₂H₅OH = 2(12) + 5(1) + 16 + 1 = 46, NOT 2(12) + 6(1) + 16 = 46. Both give 46 here, but the molecular formula must be read correctly.

#### Solved Example 4.2B
**Q:** 23 g of sodium (Na) is dissolved in 100 g of mercury (Hg) to form an amalgam. Find the mole fraction of sodium. 🟡

**Solution:**
```
Step 1: Calculate moles
    n_Na = 23/23 = 1 mol
    n_Hg = 100/200 = 0.5 mol

Step 2: Total moles
    n_total = 1 + 0.5 = 1.5 mol

Step 3: Mole fraction
    χ_Na = 1/1.5 = 2/3 ≈ 0.667

Answer: χ_Na = 0.667
```

> **Notice:** Even though sodium has less mass than mercury, it has MORE moles (because Na is lighter). Mole fraction captures the particle ratio, not the mass ratio.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.2a"></span>[4.2a](./answer-key.md#ans-4.2a) | 60 g of urea (NH₂CONH₂, M = 60) in 360 g water. Find χ_urea. ⭐ | 🟢 |
| <span id="q-4.2b"></span>[4.2b](./answer-key.md#ans-4.2b) | 11.7 g of NaCl (M = 58.5) in 90 g of water. Find χ_NaCl. | 🟡 |
| <span id="q-4.2c"></span>[4.2c](./answer-key.md#ans-4.2c) | 92 g of ethanol (M = 46) in 144 g of water. Find χ of each. | 🟢 |
| <span id="q-4.2d"></span>[4.2d](./answer-key.md#ans-4.2d) | 34.2 g of sucrose (C₁₂H₂₂O₁₁, M = 342) in 100 g of water. Find χ_sucrose. | 🟡 |
| <span id="q-4.2e"></span>[4.2e](./answer-key.md#ans-4.2e) | A solution has 10 g of methanol (CH₃OH, M = 32) and 40 g of ethanol (C₂H₅OH, M = 46). Find χ of each. | 🟡 |

---

### Type 3: Reverse — Given χ, find mole ratio

**The Pattern:** Mole fraction is given → find how many moles of each component are present (as a ratio).

#### Solved Example 4.3
**Q:** The mole fraction of glucose in an aqueous solution is 0.02. Find the ratio of moles of glucose to moles of water. 🟢

**Solution:**
```
Given: χ_glucose = 0.02

Step 1: Find χ_water
    χ_water = 1 - 0.02 = 0.98

Step 2: Find the ratio
    n_glucose / n_water = χ_glucose / χ_water = 0.02 / 0.98

    n_glucose : n_water = 2 : 98 = 1 : 49

Answer: For every 1 mole of glucose, there are 49 moles of water.
```

> **Why this works:** Since χ_A = n_A/n_total and χ_B = n_B/n_total, the ratio χ_A/χ_B = n_A/n_B. The total moles cancel out!

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.3a"></span>[4.3a](./answer-key.md#ans-4.3a) | χ_solute = 0.1. Find the mole ratio of solute to solvent. | 🟢 |
| <span id="q-4.3b"></span>[4.3b](./answer-key.md#ans-4.3b) | χ_ethanol = 0.2 in an ethanol-water solution. If 10 moles of water are present, how many moles of ethanol? | 🟡 |
| <span id="q-4.3c"></span>[4.3c](./answer-key.md#ans-4.3c) | χ_NaCl = 0.05 in a saline solution. If the total moles in solution = 200, find the moles of NaCl and water. | 🟡 |

---

### Type 4: Given χ of one component → find χ of the other

**The Pattern:** The simplest possible problem. Uses χ_A + χ_B = 1.

#### Solved Example 4.4
**Q:** In a binary solution, χ_solute = 0.15. Find χ_solvent. 🟢

**Solution:**
```
χ_solvent = 1 - χ_solute = 1 - 0.15 = 0.85

Answer: χ_solvent = 0.85
```

This seems trivially easy — and it is. But this rule becomes critical when combined with other types, especially in multi-step interconversion problems.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.4a"></span>[4.4a](./answer-key.md#ans-4.4a) | χ_A = 0.3 in a binary mixture. Find χ_B. | 🟢 |
| <span id="q-4.4b"></span>[4.4b](./answer-key.md#ans-4.4b) | χ_water = 0.95. What is χ_solute? If the solute is NaCl, how many moles of NaCl per 100 moles of water? | 🟡 |
| <span id="q-4.4c"></span>[4.4c](./answer-key.md#ans-4.4c) | Is it possible for both χ_A > 0.5 and χ_B > 0.5 in a binary mixture? Justify your answer. | 🟡 |

---

### Type 5: Multi-component Mixtures (3 or more substances)

**The Pattern:** More than two substances. The same formula applies, but with more terms in the denominator.

#### Solved Example 4.5
**Q:** A gas mixture contains 2 mol N₂, 0.5 mol O₂, and 0.1 mol CO₂. Find the mole fraction of each gas. 🟡

**Solution:**
```
Step 1: Total moles
    n_total = 2 + 0.5 + 0.1 = 2.6 mol

Step 2: Individual mole fractions
    χ_N₂ = 2/2.6 = 0.769
    χ_O₂ = 0.5/2.6 = 0.192
    χ_CO₂ = 0.1/2.6 = 0.038

Verification: 0.769 + 0.192 + 0.038 ≈ 0.999 ≈ 1.0 ✅
    (rounding error is normal)

Answer: χ_N₂ = 0.769, χ_O₂ = 0.192, χ_CO₂ = 0.038
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.5a"></span>[4.5a](./answer-key.md#ans-4.5a) | A solution has 1 mol glucose, 0.5 mol sucrose, and 50 mol water. Find χ of each. | 🟡 |
| <span id="q-4.5b"></span>[4.5b](./answer-key.md#ans-4.5b) | Air is approximately 78% N₂, 21% O₂, and 1% Ar by moles. Find χ of each gas. | 🟢 |
| <span id="q-4.5c"></span>[4.5c](./answer-key.md#ans-4.5c) | A mixture of 5 g methanol (M=32), 10 g ethanol (M=46), and 85 g water. Find χ of each. | 🟡 |

---

### Type 6: Mole Fraction of Gas Mixtures — Dalton's Law Connection

**The Pattern:** For ideal gases, mole fraction = partial pressure / total pressure.

#### Key Relationship
```
χ_A = P_A / P_total        (Dalton's Law)

where P_A = partial pressure of gas A
      P_total = total pressure = P_A + P_B + ...
```

> **Why this works:** For ideal gases, PV = nRT. At the same T and V, pressure is directly proportional to moles. So the pressure fraction equals the mole fraction.

#### Solved Example 4.6
**Q:** A gas mixture at 1 atm total pressure contains N₂ (partial pressure 0.78 atm) and O₂ (partial pressure 0.22 atm). Find the mole fraction of each gas. 🟢

**Solution:**
```
Using Dalton's Law: χ = P_partial / P_total

    χ_N₂ = 0.78 / 1.0 = 0.78
    χ_O₂ = 0.22 / 1.0 = 0.22

Verification: 0.78 + 0.22 = 1.0 ✅

Answer: χ_N₂ = 0.78, χ_O₂ = 0.22
```

#### Solved Example 4.6B
**Q:** A container has 3 mol H₂ and 1 mol N₂ at a total pressure of 2 atm. Find the partial pressure of each gas. 🟡

**Solution:**
```
Step 1: Find mole fractions
    n_total = 3 + 1 = 4 mol
    χ_H₂ = 3/4 = 0.75
    χ_N₂ = 1/4 = 0.25

Step 2: Apply Dalton's Law
    P_H₂ = χ_H₂ × P_total = 0.75 × 2 = 1.5 atm
    P_N₂ = χ_N₂ × P_total = 0.25 × 2 = 0.5 atm

Verification: 1.5 + 0.5 = 2.0 atm = P_total ✅

Answer: P_H₂ = 1.5 atm, P_N₂ = 0.5 atm
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.6a"></span>[4.6a](./answer-key.md#ans-4.6a) | A gas cylinder contains 8 g of O₂ (M=32) and 7 g of N₂ (M=28). Total pressure is 3 atm. Find the partial pressure of each gas. ⭐ | 🟡 |
| <span id="q-4.6b"></span>[4.6b](./answer-key.md#ans-4.6b) | The partial pressure of water vapour in air at 25°C is 23.8 mmHg. Atmospheric pressure is 760 mmHg. Find χ of water vapour. | 🟢 |
| <span id="q-4.6c"></span>[4.6c](./answer-key.md#ans-4.6c) | A 10 L container at 300 K holds a mixture of gases with P_total = 5 atm. If χ_He = 0.40, find the partial pressure and moles of He. (R = 0.082 L·atm/mol·K) | 🔴 |

---

### Type 7: χ → Molality Conversion ⭐

**The Pattern:** Convert mole fraction to molality. This is a high-frequency Board + JEE formula.

#### Derivation
```
Given: Binary solution of solute A in solvent B.
    χ_A = n_A / (n_A + n_B)

Molality: m = n_A / (mass of solvent in kg)
         m = n_A / (n_B × M_B / 1000)    ← since n_B × M_B = mass of solvent in g
         m = (1000 × n_A) / (n_B × M_B)

Now, from χ_A:
    n_A/n_B = χ_A / χ_B = χ_A / (1 - χ_A)

Therefore:
    m = (1000 × χ_A) / ((1 - χ_A) × M_B)

where M_B = molar mass of SOLVENT (not solute!)
```

#### The Master Formula: χ → Molality

```
            1000 × χ_solute
m = ──────────────────────────────
     (1 - χ_solute) × M_solvent

where M_solvent is in g/mol
```

#### Solved Example 4.7
**Q:** The mole fraction of glucose in an aqueous solution is 0.02. Find the molality of the solution. 🟡 ⭐

**Solution:**
```
Given: χ_glucose = 0.02, M_water = 18 g/mol

    m = (1000 × χ_solute) / ((1 - χ_solute) × M_solvent)
    m = (1000 × 0.02) / ((1 - 0.02) × 18)
    m = 20 / (0.98 × 18)
    m = 20 / 17.64
    m = 1.134 mol/kg

Answer: m ≈ 1.13 mol/kg (or 1.13 m)
```

> **Why this works:** We've combined the mole fraction definition with the molality definition, eliminating n_A and n_B individually. The result only needs χ and molar mass of solvent.

#### Reverse: Molality → χ

```
Rearranging:
    χ_solute = (m × M_solvent) / (1000 + m × M_solvent)
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.7a"></span>[4.7a](./answer-key.md#ans-4.7a) | χ_urea = 0.05 in an aqueous solution. Find molality. (M_water = 18) ⭐ | 🟡 |
| <span id="q-4.7b"></span>[4.7b](./answer-key.md#ans-4.7b) | The molality of a sucrose solution is 0.5 m. Find χ_sucrose. (M_water = 18) | 🟡 |
| <span id="q-4.7c"></span>[4.7c](./answer-key.md#ans-4.7c) | χ_NaCl = 0.1 in water. Find (a) molality (b) mass of NaCl in 500 g of water. (M_NaCl = 58.5, M_water = 18) ⭐ | 🔴 |
| <span id="q-4.7d"></span>[4.7d](./answer-key.md#ans-4.7d) | A solution has molality 2 m with solvent methanol (M = 32). Find χ_solute. | 🟡 |

---

### Type 8: χ → Molarity Conversion (requires density) ⭐⭐

**The Pattern:** Converting mole fraction to molarity requires density because molarity uses **volume**, and you need density to connect mass to volume.

#### Derivation
```
Consider 1 mole of solution total (n_A + n_B = 1).
    n_A = χ_A,  n_B = χ_B = 1 - χ_A

Mass of this 1 mole of solution:
    mass = n_A × M_A + n_B × M_B = χ_A × M_A + (1 - χ_A) × M_B

Volume of this solution:
    V = mass / (density × 1000)    ← to get volume in litres

Molarity:
    M = n_A / V = χ_A / V
```

#### The Master Formula: χ → Molarity

```
              χ_A × d × 1000
M = ──────────────────────────────────
     χ_A × M_A + (1 - χ_A) × M_B

where d = density in g/mL, M_A = molar mass of solute, M_B = molar mass of solvent
```

#### Solved Example 4.8
**Q:** The mole fraction of ethanol in an ethanol-water solution is 0.2. The density of the solution is 0.96 g/mL. Find the molarity. (M_ethanol = 46, M_water = 18) 🔴 ⭐

**Solution:**
```
Given: χ_ethanol = 0.2, d = 0.96 g/mL, M_A = 46, M_B = 18

Step 1: Find average molar mass of solution
    M_avg = χ_A × M_A + χ_B × M_B
    M_avg = 0.2 × 46 + 0.8 × 18
    M_avg = 9.2 + 14.4 = 23.6 g/mol

Step 2: Apply formula
    M = (χ_A × d × 1000) / M_avg
    M = (0.2 × 0.96 × 1000) / 23.6
    M = 192 / 23.6
    M = 8.14 mol/L

Answer: Molarity ≈ 8.14 M
```

> **Why this needs density:** Molarity = moles/volume. Mole fraction gives us moles. But to find volume, we need mass ÷ density. That's why density is always required for any conversion involving molarity.

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.8a"></span>[4.8a](./answer-key.md#ans-4.8a) | χ_glucose = 0.05 in aqueous solution, d = 1.04 g/mL. Find molarity. (M_glucose = 180, M_water = 18) ⭐ | 🔴 |
| <span id="q-4.8b"></span>[4.8b](./answer-key.md#ans-4.8b) | An ethanol-water solution has χ_ethanol = 0.15, d = 0.97 g/mL. Find M. (M_ethanol = 46, M_water = 18) | 🔴 |
| <span id="q-4.8c"></span>[4.8c](./answer-key.md#ans-4.8c) | Given: Molarity of a solution = 5 M, d = 1.2 g/mL, M_solute = 60, M_solvent = 18. Find χ_solute. (Reverse problem) ⭐ | 🔴 |

---

### Type 9: Temperature Independence — Proof and Reasoning

**The Pattern:** Conceptual — why is mole fraction unaffected by temperature?

#### Solved Example 4.9
**Q:** Explain why mole fraction is independent of temperature, while molarity is not. 🟡

**Solution:**
```
Temperature affects VOLUME, not MASS or NUMBER OF PARTICLES.

Mole fraction:
    χ = n_A / (n_A + n_B)
    
    n_A = number of moles = number of particles / Avogadro's number
    
    Heating a solution doesn't create or destroy particles.
    So n_A and n_B remain constant → χ remains constant. ✅

Molarity:
    M = n / V(in L)
    
    Heating a solution → volume increases (thermal expansion)
    → V increases → M decreases.
    
    So molarity IS temperature-dependent. ❌

Similarly:
    Molality: m = n / (mass of solvent in kg)
    Mass doesn't change with temperature → molality is T-independent ✅
    
    Mass percent: w/w% = mass ratio → T-independent ✅
    
    Volume percent: v/v% = volume ratio → T-dependent ❌
```

**Summary Table:**
| Concentration Term | T-Independent? | Why |
|-------------------|----------------|-----|
| Mole fraction (χ) | ✅ Yes | Based on moles (particles) |
| Molality (m) | ✅ Yes | Based on mass of solvent |
| Mass percent (w/w%) | ✅ Yes | Based on mass ratio |
| PPM (mass-based) | ✅ Yes | Based on mass ratio |
| Molarity (M) | ❌ No | Based on volume of solution |
| Volume percent (v/v%) | ❌ No | Based on volume ratio |

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.9a"></span>[4.9a](./answer-key.md#ans-4.9a) | A solution has χ_solute = 0.1 at 25°C. What will be its mole fraction at 50°C? Justify. | 🟢 |
| <span id="q-4.9b"></span>[4.9b](./answer-key.md#ans-4.9b) | Arrange the following in order of increasing sensitivity to temperature change: molality, molarity, mole fraction, mass percent. | 🟡 |

---

### Type 10: Vapour Pressure Using Raoult's Law (Preview) ⭐⭐

**The Pattern:** Raoult's Law connects mole fraction to vapour pressure. This is a preview of the Solutions chapter's colligative properties.

#### Raoult's Law
```
P_solution = χ_solvent × P°_solvent

where:
    P_solution = vapour pressure of the solution
    P°_solvent = vapour pressure of PURE solvent
    χ_solvent = mole fraction of solvent in solution
```

#### Relative Lowering of Vapour Pressure
```
(P° - P) / P° = χ_solute

Relative lowering of VP = mole fraction of (non-volatile) solute
```

#### Solved Example 4.10
**Q:** The vapour pressure of pure water at 25°C is 23.8 mmHg. A solution is prepared by dissolving 18 g of glucose (M = 180) in 178.2 g of water (M = 18). Find: (a) mole fraction of glucose (b) vapour pressure of the solution (c) lowering of vapour pressure. 🟡 ⭐

**Solution:**
```
Step 1: Calculate moles
    n_glucose = 18/180 = 0.1 mol
    n_water = 178.2/18 = 9.9 mol

Step 2: Mole fractions
    χ_glucose = 0.1/(0.1 + 9.9) = 0.1/10 = 0.01
    χ_water = 9.9/10 = 0.99

Step 3: Apply Raoult's Law
    P_solution = χ_water × P°_water
    P_solution = 0.99 × 23.8 = 23.562 mmHg

Step 4: Lowering of VP
    ΔP = P° - P = 23.8 - 23.562 = 0.238 mmHg

    Verify: ΔP/P° = 0.238/23.8 = 0.01 = χ_glucose ✅

Answer: (a) χ_glucose = 0.01  (b) P = 23.562 mmHg  (c) ΔP = 0.238 mmHg
```

> **Why this works:** Adding a non-volatile solute essentially reduces the fraction of surface occupied by solvent molecules. Fewer solvent molecules at the surface → lower vapour pressure. The reduction is directly proportional to how many of the "slots" are taken by solute → i.e., χ_solute.

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.10a"></span>[4.10a](./answer-key.md#ans-4.10a) | P° of water = 23.8 mmHg at 25°C. χ_solute = 0.05. Find P_solution and ΔP. | 🟡 |
| <span id="q-4.10b"></span>[4.10b](./answer-key.md#ans-4.10b) | A solution has VP = 22.5 mmHg and P° = 23.8 mmHg. Find χ_solute. ⭐ | 🟡 |
| <span id="q-4.10c"></span>[4.10c](./answer-key.md#ans-4.10c) | 30 g of urea (M=60) is dissolved in 270 g of water (M=18). P° of water = 31.82 mmHg. Find VP of solution. ⭐ | 🟡 |
| <span id="q-4.10d"></span>[4.10d](./answer-key.md#ans-4.10d) | The VP of a solution is 95% of pure solvent's VP. Find χ_solute and χ_solvent. | 🟢 |
| <span id="q-4.10e"></span>[4.10e](./answer-key.md#ans-4.10e) | 6 g of a non-volatile solute is dissolved in 180 g of water. VP of solution = 23.4 mmHg, P° = 23.8 mmHg. Find the molar mass of the solute. ⭐⭐ | 🔴 |

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-4.M1"></span>[4.M1](./answer-key.md#ans-4.M1) | 9.2 g of ethanol (M=46) is mixed with 36 g of water. Find: (a) χ_ethanol (b) molality (c) VP of solution if P° of water = 23.8 mmHg. | T2 + T7 + T10 | 🟡 |
| <span id="q-4.M2"></span>[4.M2](./answer-key.md#ans-4.M2) | A gas mixture has χ_O₂ = 0.21 at 5 atm total pressure. (a) Find partial pressure of O₂. (b) If the remaining gas is N₂, find χ_N₂ and P_N₂. (c) If total moles = 10, find individual moles. | T6 + T4 + T1 | 🟡 |
| <span id="q-4.M3"></span>[4.M3](./answer-key.md#ans-4.M3) | An aqueous solution has molality = 2.78 m. Find: (a) χ_solute (b) If the solute is NaCl (M=58.5) and d = 1.08 g/mL, find molarity. | T7 + T8 | 🔴 |
| <span id="q-4.M4"></span>[4.M4](./answer-key.md#ans-4.M4) | χ_A = 0.1 in a solution where A has M = 100 and the solvent (water) has M = 18. (a) Find molality. (b) If d = 1.05 g/mL, find molarity. (c) Express as mass percent. | T7 + T8 + new | 🔴 |
| <span id="q-4.M5"></span>[4.M5](./answer-key.md#ans-4.M5) | 5 g of a non-volatile, non-electrolyte solute is dissolved in 100 g of water. The VP of the solution is 17.7 mmHg at 20°C (P° = 17.5 mmHg — wait, that can't be right: VP of solution should be LESS than P°). Corrected: P° = 17.8 mmHg, P_solution = 17.7 mmHg. Find the molar mass of the solute. | T10 + T2 (reverse) | 🔴 |

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.B1"></span>[4.B1](./answer-key.md#ans-4.B1) | Calculate the mole fraction of benzene in a solution containing 30% by mass of benzene in carbon tetrachloride. (M_benzene = 78, M_CCl₄ = 154) ⭐ | 🟡 |
| <span id="q-4.B2"></span>[4.B2](./answer-key.md#ans-4.B2) | The mole fraction of a solute in an aqueous solution is 0.1. Calculate the molality of the solution. (M_water = 18) ⭐ | 🟡 |
| <span id="q-4.B3"></span>[4.B3](./answer-key.md#ans-4.B3) | Calculate the mole fraction of H₂SO₄ in a solution containing 98% H₂SO₄ by mass. (M_H₂SO₄ = 98, M_H₂O = 18) ⭐ | 🟡 |
| <span id="q-4.B4"></span>[4.B4](./answer-key.md#ans-4.B4) | A solution of glucose in water has concentration 10% by mass. Find (a) mole fraction of glucose (b) molality. (M_glucose = 180) | 🟡 |

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-4.J1"></span>[4.J1](./answer-key.md#ans-4.J1) | An aqueous solution contains 3% urea (M=60) and 7.45% KCl (M=74.5) by mass. Calculate the mole fraction of urea in the solution. (Consider KCl as a molecular solute for this problem.) ⭐ | 🔴 |
| <span id="q-4.J2"></span>[4.J2](./answer-key.md#ans-4.J2) | The mole fraction of a solute in a solution is 0.1. The solution's density is 1.2 g/mL and the molar mass of solute = 100 g/mol (solvent = water, M = 18). Calculate the molarity. ⭐ | 🔴 |
| <span id="q-4.J3"></span>[4.J3](./answer-key.md#ans-4.J3) | A mixture of He and Ne has an average molar mass of 10 g/mol. Find the mole fraction of each gas. (M_He = 4, M_Ne = 20) ⭐ | 🟡 |
| <span id="q-4.J4"></span>[4.J4](./answer-key.md#ans-4.J4) | 100 g of liquid A (M = 40) is dissolved in 1000 g of liquid B (M = 80). The vapour pressure of pure A = 400 mmHg and of pure B = 200 mmHg. Assuming ideal behaviour, find the total vapour pressure of the solution. (Both are volatile.) ⭐⭐ | 🔴 |
| <span id="q-4.J5"></span>[4.J5](./answer-key.md#ans-4.J5) | Given: 10% (w/w) NaOH solution, d = 1.2 g/mL, M = 40. Find (a) mole fraction of NaOH (b) molality (c) molarity. (Multi-step interconversion preview.) ⭐ | 🔴 |

---

## Key Takeaways from Chapter 4

```
┌─────────────────────────────────────────────────────────────┐
│                 MOLE FRACTION SUMMARY                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Formula: χ_A = n_A / (n_A + n_B)                           │
│                                                              │
│  Golden Rule: χ_A + χ_B = 1  (always, for binary)          │
│                                                              │
│  Properties:                                                 │
│    • Dimensionless (no units)                               │
│    • Always between 0 and 1                                 │
│    • Temperature INDEPENDENT ✅                              │
│                                                              │
│  Key Conversions:                                            │
│    χ → m:  m = (1000 × χ_solute) / ((1 - χ) × M_solvent)  │
│    χ → M:  Requires density (density always needed for M)   │
│                                                              │
│  Gas Mixtures:                                               │
│    χ_A = P_A / P_total  (Dalton's Law)                      │
│                                                              │
│  Raoult's Law (Preview):                                     │
│    P_solution = χ_solvent × P°                              │
│    ΔP/P° = χ_solute                                         │
│                                                              │
│  Denominator trap:                                           │
│    χ = n_solute / n_TOTAL (NOT n_solvent!)                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 3 — PPM](./03-ppm.md) | [Chapter 5 — Molality →](./05-molality.md)*
