# Chapter 5: Molality (m)
## Part II: Enter the Mole

---

## 🎯 Stage 1: The Core Idea

### What is Molality?

Molality measures how many moles of solute are dissolved per kilogram of **solvent** (not solution!).

> **Analogy:** Imagine you're making lemonade. Molality asks: "How many lemons did you squeeze per kilogram of water?" It doesn't care about the total weight of the lemonade (water + lemon juice + sugar) — only the water.

### Why Molality, Not Just Molarity?

| Feature | Molality (m) | Molarity (M) |
|---------|-------------|-------------|
| Denominator | Mass of solvent (kg) | Volume of solution (L) |
| Temperature effect | **Independent** ✅ | Dependent ❌ |
| Measured with | Balance (mass) | Volumetric flask (volume) |
| Used for | Colligative properties | Lab work, stoichiometry |

> **Why temperature matters:** When you heat a solution, it expands — volume increases but mass stays the same. Molarity changes; molality doesn't. For colligative properties (boiling point elevation, freezing point depression, osmotic pressure), you need a concentration that doesn't drift with temperature. That's molality.

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
       Moles of solute           n_solute
m = ────────────────────── = ─────────────────
     Mass of solvent (kg)    W_solvent (in kg)
```

### Unpacking the Formula

```
         mass of solute / molar mass of solute
m = ──────────────────────────────────────────────
              mass of solvent / 1000

         W_solute × 1000
m = ──────────────────────────
     M_solute × W_solvent(g)

where:
    W_solute = mass of solute in grams
    M_solute = molar mass of solute in g/mol
    W_solvent = mass of SOLVENT in grams (NOT solution!)
```

### Critical Distinction

```
⚠️ SOLVENT ≠ SOLUTION

Mass of solution = Mass of solute + Mass of solvent
W_solution = W_solute + W_solvent
W_solvent = W_solution - W_solute

MOLALITY uses mass of SOLVENT (denominator)
Students CONSTANTLY confuse this with mass of SOLUTION
```

### Units

```
m = mol / kg = mol·kg⁻¹

Read as: "moles per kilogram of solvent"
Symbol: lowercase 'm' or 'mol/kg' or 'mol kg⁻¹'
```

### Temperature Dependence

Molality is **temperature-independent** ✅

Why? Mass of solvent doesn't change with temperature. Unlike volume (which expands/contracts), mass is invariant under temperature changes.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given mass of solute, molar mass, mass of solvent → find m

**The Pattern:** All three quantities are directly provided → plug into formula.

#### Solved Example 5.1
**Q:** 6 g of urea (NH₂CONH₂, M = 60 g/mol) is dissolved in 500 g of water. Find the molality of the solution. 🟢

**Solution:**
```
Step 1: Calculate moles of solute
    n_urea = mass / molar mass = 6/60 = 0.1 mol

Step 2: Convert mass of solvent to kg
    W_solvent = 500 g = 0.5 kg

Step 3: Calculate molality
    m = n/W = 0.1/0.5 = 0.2 mol/kg

Answer: m = 0.2 mol/kg (or 0.2 m)
```

> **Why this works:** Straightforward substitution. The only trap is forgetting to convert grams to kilograms in the denominator.

> **⚠️ Common Mistake:** Using mass of SOLUTION instead of mass of SOLVENT. In dilute solutions these are nearly equal, but in concentrated solutions, the difference is significant.

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.1a"></span>5.1a | 18 g of glucose (M = 180) in 100 g of water. Find m. | 🟢 |
| <span id="q-5.1b"></span>5.1b | 11.7 g of NaCl (M = 58.5) in 250 g of water. Find m. | 🟢 |
| <span id="q-5.1c"></span>5.1c | 4.9 g of H₂SO₄ (M = 98) in 500 g of water. Find m. | 🟢 |
| <span id="q-5.1d"></span>5.1d | 36 g of glucose (M = 180) in 1 kg of water. Find m. ⭐ | 🟢 |

<details>
<summary>View Answers</summary>

**5.1a**: m = 1
**5.1b**: m = 0.8
**5.1c**: m = 0.1
**5.1d**: m = 0.2

</details>


---

### Type 2: Reverse — Given m → find mass of solute needed

**The Pattern:** Molality is given → calculate how much solute to add to a known mass of solvent.

#### Solved Example 5.2
**Q:** How many grams of NaOH (M = 40) must be dissolved in 200 g of water to prepare a 2.5 m solution? 🟡

**Solution:**
```
Step 1: Find moles of solute needed
    m = n / W_solvent(kg)
    2.5 = n / 0.2
    n = 2.5 × 0.2 = 0.5 mol

Step 2: Convert to mass
    mass = n × M = 0.5 × 40 = 20 g

Answer: 20 g of NaOH
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.2a"></span>5.2a | Find the mass of glucose (M = 180) required to prepare a 0.5 m solution using 1 kg of water. | 🟢 |
| <span id="q-5.2b"></span>5.2b | How many grams of urea (M = 60) are needed to make a 1.5 m solution in 400 g of water? | 🟡 |
| <span id="q-5.2c"></span>5.2c | A 0.1 m solution of KCl (M = 74.5) is prepared using 2 kg of water. Find the mass of KCl required. | 🟡 |

<details>
<summary>View Answers</summary>

**5.2a**: 90 g
**5.2b**: 36 g
**5.2c**: Answer not found.

</details>


---

### Type 3: Given m → find mass of solvent if moles of solute known

**The Pattern:** Reverse of the reverse — find how much solvent is needed.

#### Solved Example 5.3
**Q:** You have 0.3 mol of sucrose. How much water (in grams) do you need to make a 0.6 m solution? 🟡

**Solution:**
```
    m = n / W_solvent(kg)
    0.6 = 0.3 / W
    W = 0.3 / 0.6 = 0.5 kg = 500 g

Answer: 500 g of water
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.3a"></span>5.3a | 0.5 mol of NaCl needs to become a 2 m solution. How much water? | 🟢 |
| <span id="q-5.3b"></span>5.3b | 0.1 mol of glucose must give m = 0.25. Find mass of water needed. | 🟡 |
| <span id="q-5.3c"></span>5.3c | A pharmacist has 0.05 mol of a drug and needs m = 0.1. How much solvent? | 🟡 |

<details>
<summary>View Answers</summary>

**5.3a**: Answer not found.
**5.3b**: Answer not found.
**5.3c**: Answer not found.

</details>


---

### Type 4: Dissolving solid in water — given masses → find m

**The Pattern:** Same as Type 1, but the problem says "dissolve X grams in Y grams of water." The water IS the solvent.

#### Solved Example 5.4
**Q:** 5 g of NaCl (M = 58.5) is dissolved in 95 g of water. Find the molality. 🟢

**Solution:**
```
Step 1: n_NaCl = 5/58.5 = 0.0855 mol

Step 2: W_solvent = 95 g = 0.095 kg

Step 3: m = 0.0855/0.095 = 0.9 mol/kg

Answer: m ≈ 0.9 m
```

> **⚠️ Common Mistake:** Some students add solute + solvent to get "100 g" and use 100 as the denominator. NO! The denominator is only the solvent (95 g), not the solution (100 g). For molality, ALWAYS subtract solute from solution to get solvent weight.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.4a"></span>5.4a | 30 g of urea (M = 60) dissolved in 970 g of water. Find m. | 🟢 |
| <span id="q-5.4b"></span>5.4b | 98 g of H₂SO₄ (M = 98) dissolved in 902 g of water. Find m. Note the mass of solution = 1000 g. | 🟡 |
| <span id="q-5.4c"></span>5.4c | 4.5 g of glucose (M = 180) in 50 g of water. Find m. | 🟢 |

<details>
<summary>View Answers</summary>

**5.4a**: Answer not found.
**5.4b**: Answer not found.
**5.4c**: Answer not found.

</details>


---

### Type 5: Given w/w% → convert to molality ⭐

**The Pattern:** Mass percent is given → derive molality.

#### Derivation
```
Let w/w% = x%. Consider 100 g of solution.
    Mass of solute = x g
    Mass of solvent = (100 - x) g

    n_solute = x / M_solute

    m = n_solute / (mass of solvent in kg)
    m = (x / M_solute) / ((100 - x) / 1000)
    m = (x × 1000) / (M_solute × (100 - x))
```

#### The Master Formula: w/w% → Molality

```
            w/w% × 1000                    x × 1000
m = ──────────────────────── = ────────────────────────────
     M_solute × (100 - w/w%)    M_solute × (100 - x)
```

#### Solved Example 5.5
**Q:** Find the molality of a 10% (w/w) NaOH solution. (M_NaOH = 40) 🟡 ⭐

**Solution:**
```
Method 1: Using the formula
    m = (10 × 1000) / (40 × (100 - 10))
    m = 10000 / (40 × 90)
    m = 10000 / 3600
    m = 2.78 mol/kg

Method 2: From first principles (recommended for understanding)
    In 100 g of solution:
        Solute = 10 g    → n = 10/40 = 0.25 mol
        Solvent = 90 g   = 0.09 kg
    
    m = 0.25/0.09 = 2.78 mol/kg ✅

Answer: m = 2.78 mol/kg
```

> **Why this works:** w/w% gives us masses. From masses we can find moles and mass of solvent — exactly what molality needs.

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.5a"></span>5.5a | Find the molality of a 20% glucose (M=180) solution. | 🟡 |
| <span id="q-5.5b"></span>5.5b | A solution is 5% urea (M=60) by mass. Find m. ⭐ | 🟡 |
| <span id="q-5.5c"></span>5.5c | Commercial H₂SO₄ is 98% by mass (M=98). Find its molality. ⭐ | 🟡 |
| <span id="q-5.5d"></span>5.5d | If w/w% = 50% for a solute of M = 100, find m. What's special about this result? | 🟡 |

<details>
<summary>View Answers</summary>

**5.5a**: m ≈ 1.39
**5.5b**: m ≈ 0.877
**5.5c**: m = 500 (!)
**5.5d**: Answer not found.

</details>


---

### Type 6: Given mole fraction → convert to molality ⭐

**The Pattern:** Uses the formula derived in Chapter 4, Type 7.

#### The Formula (from Chapter 4)

```
            1000 × χ_solute
m = ──────────────────────────────
     (1 - χ_solute) × M_solvent
```

#### Solved Example 5.6
**Q:** The mole fraction of urea in an aqueous solution is 0.018. Find the molality. (M_water = 18) 🟡

**Solution:**
```
    m = (1000 × 0.018) / ((1 - 0.018) × 18)
    m = 18 / (0.982 × 18)
    m = 18 / 17.676
    m = 1.018 mol/kg

Answer: m ≈ 1.02 mol/kg
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.6a"></span>5.6a | χ_glucose = 0.1 in water. Find molality. (M_water = 18) | 🟡 |
| <span id="q-5.6b"></span>5.6b | χ_solute = 0.2 in ethanol (M = 46). Find molality. | 🟡 |
| <span id="q-5.6c"></span>5.6c | Molality of a solution is 5 m (solvent = water). Find χ_solute. (Reverse) ⭐ | 🟡 |

<details>
<summary>View Answers</summary>

**5.6a**: Answer not found.
**5.6b**: Answer not found.
**5.6c**: Answer not found.

</details>


---

### Type 7: Given Molarity + Density → Convert to Molality ⭐⭐⭐

**The Pattern:** This is the **most important conversion** in all of concentration terms. JEE loves this.

#### Derivation
```
Consider 1 L of solution.
    Moles of solute = M (by definition of molarity)
    Mass of solute = M × M_solute (grams)
    
    Mass of 1 L solution = d × 1000 (grams)  [d in g/mL, 1L = 1000 mL]
    
    Mass of solvent = mass of solution - mass of solute
                    = d × 1000 - M × M_solute (grams)
                    = (d × 1000 - M × M_solute) / 1000 (kg)
    
    Molality = M / mass of solvent(kg)
             = (M × 1000) / (d × 1000 - M × M_solute)
```

#### The Master Formula: Molarity → Molality

```
              M × 1000
m = ──────────────────────────────
     d × 1000 - M × M_solute

where:
    M = molarity (mol/L)
    d = density (g/mL)
    M_solute = molar mass of solute (g/mol)
```

#### Solved Example 5.7
**Q:** A 2 M NaCl solution has a density of 1.08 g/mL. Find its molality. (M_NaCl = 58.5) 🟡 ⭐⭐

**Solution:**
```
Step 1: Consider 1 L of solution
    Moles of NaCl = 2 mol
    Mass of NaCl = 2 × 58.5 = 117 g

Step 2: Find mass of solution (1 L)
    mass = d × V = 1.08 × 1000 = 1080 g

Step 3: Find mass of solvent
    W_solvent = 1080 - 117 = 963 g = 0.963 kg

Step 4: Calculate molality
    m = 2/0.963 = 2.077 mol/kg

Answer: m ≈ 2.08 mol/kg

Using the formula directly:
    m = (2 × 1000)/(1.08 × 1000 - 2 × 58.5) = 2000/963 = 2.077 ✅
```

> **Why this works:** The trick is thinking about "1 L of solution." That gives you moles of solute directly (from M). Density gives you the mass of that 1 L. Subtract solute mass → solvent mass. Done.

> **⚠️ Common Mistake:** Using "1 kg of solution" instead of "1 L of solution." While both approaches work, starting with 1 L is cleaner because molarity directly gives you moles for 1 L.

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.7a"></span>5.7a | A 1 M H₂SO₄ solution has d = 1.065 g/mL. Find molality. (M = 98) ⭐ | 🟡 |
| <span id="q-5.7b"></span>5.7b | 3 M glucose (M = 180), d = 1.12 g/mL. Find m. | 🟡 |
| <span id="q-5.7c"></span>5.7c | 0.5 M urea (M = 60), d = 1.01 g/mL. Find m. | 🟡 |
| <span id="q-5.7d"></span>5.7d | 18 M H₂SO₄, d = 1.84 g/mL. Find m. (M = 98) ⭐⭐ | 🔴 |
| <span id="q-5.7e"></span>5.7e | A solution has m = 4 and d = 1.2 g/mL. Solute M = 80. Find molarity. (Reverse) ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**5.7a**: m ≈ 1.034
**5.7b**: m ≈ 3.95
**5.7c**: Answer not found.
**5.7d**: m ≈ 55.55
**5.7e**: Answer not found.

</details>


---

### Type 8: Molality of Pure Liquid

**The Pattern:** A conceptual trick question. What is the "molality" of a pure substance?

#### Solved Example 5.8
**Q:** Calculate the molality of pure water. 🟡

**Solution:**
```
Wait — pure water has no solute. So what does molality even mean here?

Interpretation: Consider water as the "solute" in itself.
    Take 1 mol of water = 18 g (this is the "solute")
    The remaining water is the "solvent"

But this creates a circular problem. In reality:

For pure water:
    Consider 1000 g of water as solvent.
    Moles of water = 1000/18 = 55.55 mol

    "Molality" = 55.55 mol / 1 kg = 55.55 m

Answer: The "molality" of pure water is 55.55 m
(This is a theoretical construct — pure substances don't truly have "molality")
```

> **Why this matters:** This is a conceptual question that tests whether you understand molality at a deep level. It also connects to the idea that the "molarity of pure water = 55.5 M" (from Chapter 6).

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.8a"></span>5.8a | Calculate the "molality" of pure ethanol (M = 46, d = 0.789 g/mL). | 🟡 |
| <span id="q-5.8b"></span>5.8b | Why is the concept of molality undefined for pure substances in a rigorous sense? | 🟡 |

<details>
<summary>View Answers</summary>

**5.8a**: Answer not found.
**5.8b**: Answer not found.

</details>


---

### Type 9: Why Molality is Preferred for Colligative Properties

**The Pattern:** Conceptual reasoning — no calculation.

#### Solved Example 5.9
**Q:** Why do we use molality (not molarity) in colligative property formulas? 🟡

**Solution:**
```
Colligative property formulas:
    ΔTb = Kb × m
    ΔTf = Kf × m
    π = mRT (for some formulations)

Why molality?

1. TEMPERATURE INDEPENDENCE
   Colligative properties (boiling point elevation, freezing point 
   depression) inherently involve TEMPERATURE CHANGES. If we used 
   molarity, the concentration itself would change as we heat/cool 
   the solution — making the formula self-contradictory.

2. ADDITIVITY
   Molality of solvent is directly proportional to the mole fraction 
   of solute (for dilute solutions), which is the fundamental quantity 
   that determines colligative properties.

3. MEASUREMENT SIMPLICITY
   Mass is easier to measure accurately than volume, especially 
   across different temperatures. No volumetric flask needed.

Summary: Colligative properties depend on the NUMBER OF SOLUTE 
         PARTICLES relative to solvent. Molality counts exactly that,
         without volume interference.
```

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.9a"></span>5.9a | A student uses molarity instead of molality in ΔTb = Kb × m. At what temperature is the error zero? At what temperature is it maximum? | 🔴 |
| <span id="q-5.9b"></span>5.9b | List all concentration terms that are temperature-independent. Why are they all based on mass (or moles)? | 🟡 |

<details>
<summary>View Answers</summary>

**5.9a**: Answer not found.
**5.9b**: Answer not found.

</details>


---

### Type 10: Multi-solute — Two Solutes in Same Solvent

**The Pattern:** More than one solute → treat each separately, but use the SAME solvent mass.

#### Solved Example 5.10
**Q:** 6 g of urea (M = 60) and 5.85 g of NaCl (M = 58.5) are dissolved in 500 g of water. Find the molality of each solute and the total molality. 🟡

**Solution:**
```
Step 1: Calculate moles of each solute
    n_urea = 6/60 = 0.1 mol
    n_NaCl = 5.85/58.5 = 0.1 mol

Step 2: Mass of solvent = 500 g = 0.5 kg

Step 3: Individual molalities
    m_urea = 0.1/0.5 = 0.2 m
    m_NaCl = 0.1/0.5 = 0.2 m

Step 4: Total molality
    m_total = m_urea + m_NaCl = 0.2 + 0.2 = 0.4 m

Answer: m_urea = 0.2 m, m_NaCl = 0.2 m, m_total = 0.4 m
```

> **Why total molality matters:** For colligative properties of non-electrolytes, what matters is the TOTAL molality of all solute particles.

> **⚠️ For electrolytes:** NaCl dissociates: NaCl → Na⁺ + Cl⁻. So the effective molality of particles = 0.2 × 2 = 0.4 m just from NaCl alone. This uses the van't Hoff factor (i) — preview for colligative properties.

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.10a"></span>5.10a | 9 g of glucose (M = 180) and 3 g of urea (M = 60) in 250 g of water. Find m_glucose, m_urea, and m_total. | 🟡 |
| <span id="q-5.10b"></span>5.10b | 11.1 g CaCl₂ (M = 111) and 5.85 g NaCl (M = 58.5) in 1 kg of water. Find individual and total molalities. For colligative purposes, what is the effective total molality? (CaCl₂ → Ca²⁺ + 2Cl⁻, NaCl → Na⁺ + Cl⁻) ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**5.10a**: Answer not found.
**5.10b**: Answer not found.

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-5.M1"></span>5.M1 | A 15% (w/w) glucose (M=180) solution has density 1.06 g/mL. Find: (a) molality (b) molarity (c) mole fraction of glucose. | T5 + T7 + Ch4 | 🔴 |
| <span id="q-5.M2"></span>5.M2 | 2 M NaCl (d = 1.08 g/mL, M = 58.5). Find (a) molality (b) mass percent (c) mole fraction. | T7 + reverse T5 + Ch4 | 🔴 |
| <span id="q-5.M3"></span>5.M3 | χ_urea = 0.04 (M_urea = 60, M_water = 18). (a) Find molality. (b) If d = 1.02 g/mL, find molarity. (c) Find mass % of urea. | T6 + Ch4-T8 + reverse T5 | 🔴 |
| <span id="q-5.M4"></span>5.M4 | A student prepares a solution by dissolving 20 g of a substance (M = 40) in 480 g of water. (a) Find mass %. (b) Find molality. (c) If d = 1.01 g/mL, find molarity. (d) Find mole fraction. | T4 + T5 + T7 + Ch4 | 🔴 |

<details>
<summary>View Answers</summary>

**5.M1**: Answer not found.
**5.M2**: Answer not found.
**5.M3**: Answer not found.
**5.M4**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.B1"></span>5.B1 | Calculate the molality of 2.5 g of ethanoic acid (CH₃COOH, M = 60) dissolved in 75 g of benzene. ⭐ | 🟢 |
| <span id="q-5.B2"></span>5.B2 | A solution is prepared by dissolving 0.5 mol of NaOH in 500 g of water. Calculate the molality. | 🟢 |
| <span id="q-5.B3"></span>5.B3 | The mass percentage of aspirin (C₉H₈O₄, M = 180) in acetonitrile (CH₃CN, M = 41) is 6.5%. Calculate the molality of the solution. ⭐ | 🟡 |
| <span id="q-5.B4"></span>5.B4 | A 5% solution of cane sugar (C₁₂H₂₂O₁₁, M = 342) in water. Calculate (a) molality (b) mole fraction. ⭐ | 🟡 |

<details>
<summary>View Answers</summary>

**5.B1**: Answer not found.
**5.B2**: Answer not found.
**5.B3**: Answer not found.
**5.B4**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-5.J1"></span>5.J1 | Concentrated H₂SO₄ has d = 1.84 g/mL and is 98% by mass (M = 98). Find (a) molarity (b) molality (c) mole fraction. ⭐⭐ | 🔴 |
| <span id="q-5.J2"></span>5.J2 | A 4 M NaOH solution has d = 1.15 g/mL (M = 40). Find (a) molality (b) mass %. Which is greater — M or m? Why? | 🔴 |
| <span id="q-5.J3"></span>5.J3 | The molality and molarity of an aqueous solution are equal in magnitude. Given that M_solute = 100 g/mol, find the density of the solution. ⭐ | 🔴 |
| <span id="q-5.J4"></span>5.J4 | A solution has m = 10 molal and M = 8 molar. If M_solute = 50 g/mol, find the density. | 🔴 |
| <span id="q-5.J5"></span>5.J5 | An aqueous solution has mole fraction of solute = 0.2 and density = 1.25 g/mL. M_solute = 60. Find (a) molality (b) molarity (c) mass %. (Full interconversion chain.) ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**5.J1**: M=18.4, m=500, χ=0.9
**5.J2**: Answer not found.
**5.J3**: d = 1 + M×M_s/1000 = 1.1 for M_s=100 at M=m=1
**5.J4**: Answer not found.
**5.J5**: Answer not found.

</details>


---

## Key Takeaways from Chapter 5

```
┌─────────────────────────────────────────────────────────────┐
│                  MOLALITY SUMMARY                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Formula: m = n_solute / W_solvent(kg)                      │
│                                                              │
│  Expanded: m = (W_solute × 1000) / (M_solute × W_solvent)  │
│                                                              │
│  Key Properties:                                             │
│    • Units: mol/kg (or simply 'm')                          │
│    • Temperature INDEPENDENT ✅                              │
│    • Denominator = mass of SOLVENT (not solution!)           │
│                                                              │
│  Critical Conversions:                                       │
│    w/w% → m:  m = (x × 1000) / (M × (100-x))             │
│    χ → m:     m = (1000 × χ) / ((1-χ) × M_solvent)        │
│    M → m:     m = (M × 1000) / (d×1000 - M×M_solute)      │
│                                                              │
│  THE #1 TRAP:                                                │
│    Using W_solution instead of W_solvent ❌                  │
│    Always: W_solvent = W_solution - W_solute                │
│                                                              │
│  Used for: Colligative properties (ΔTb, ΔTf, π)            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 4 — Mole Fraction](./04-mole-fraction.md) | [Chapter 6 — Molarity →](./06-molarity.md)*
