# Chapter 3: Parts Per Million (ppm)
## Part I: The Foundations

---

## 🎯 Stage 1: The Core Idea

### What is PPM?

Your city's water supply has 0.0005% fluoride in it. That number is ugly, hard to read, and easy to misplace a zero. Scientists needed a better way to talk about **extremely small concentrations**.

Enter **parts per million (ppm)**.

Instead of saying "0.0005%", you say **"5 ppm"** — meaning there are 5 parts of fluoride in every 1,000,000 parts of water.

> **Think of it this way:** Mass percent says "parts per hundred." PPM says "parts per million." It's the same idea, just scaled up by 10,000.

### The Simple Relationship
```
1% = 10,000 ppm
0.1% = 1,000 ppm
0.01% = 100 ppm
0.001% = 10 ppm
0.0001% = 1 ppm
```

### Where Is PPM Used?

| Field | Example |
|-------|---------|
| Water quality | Fluoride in drinking water: 1–1.5 ppm |
| Air pollution | CO₂ in atmosphere: ~420 ppm |
| Food safety | Pesticide residues: < 0.1 ppm |
| Metallurgy | Impurities in gold: "99.99% pure" = 100 ppm impurities |
| Medical | Blood glucose: ~900 ppm (for normal levels) |

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
         Mass of solute
ppm = ─────────────────── × 10⁶
        Mass of solution
```

### Equivalent Forms

**Mass-based (most common in chemistry):**
```
ppm = (mg of solute / kg of solution)
ppm = (mg of solute / L of solution)     ← ONLY when d_solution ≈ 1 g/mL (dilute aqueous)
ppm = (µg of solute / g of solution)
```

### Why mg/L ≈ ppm for Dilute Aqueous Solutions

For very dilute aqueous solutions:
- Density of solution ≈ density of water ≈ 1 g/mL = 1 kg/L
- So 1 L of solution ≈ 1 kg of solution
- Therefore: mg/kg = mg/L = ppm

This approximation is used in almost all Board and JEE problems.

> **⚠️ Common Mistake:** This approximation ONLY works for dilute aqueous solutions. For concentrated solutions or non-aqueous solutions, you MUST use the exact formula with mass ratios.

### Relationship with Mass Percent

```
ppm = mass % × 10⁴

OR equivalently:

mass % = ppm / 10⁴ = ppm × 10⁻⁴
```

### Temperature Dependence

PPM (mass-based) is **temperature-independent** — same logic as w/w%. We're using mass ratios, and mass doesn't change with temperature.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given masses, find ppm

**The Pattern:** Given mass of solute and mass of solution → calculate ppm.

#### Solved Example 3.1
**Q:** A water sample contains 0.003 g of dissolved chlorine in 1000 g (1 kg) of water. Express the concentration in ppm. 🟢

**Solution:**
```
Step 1: Identify
    Mass of solute (Cl₂) = 0.003 g
    Mass of solution ≈ 1000 g (dilute, so solution ≈ solvent)

Step 2: Apply formula
    ppm = (mass of solute / mass of solution) × 10⁶
    ppm = (0.003 / 1000) × 10⁶
    ppm = 3 × 10⁻⁶ × 10⁶
    ppm = 3 ppm

Answer: 3 ppm
```

**Alternative using mg/kg shortcut:**
```
0.003 g = 3 mg
Mass of solution = 1 kg
ppm = 3 mg / 1 kg = 3 ppm ✅ (same answer, faster)
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.1a"></span>3.1a | 0.006 g of fluoride is present in 2 kg of water. Find concentration in ppm. | 🟢 |
| <span id="q-3.1b"></span>3.1b | A 500 g water sample contains 0.0015 g of lead. Express in ppm. | 🟢 |
| <span id="q-3.1c"></span>3.1c | 10 mg of arsenic is found in 5 kg of soil sample. Find ppm. | 🟢 |
| <span id="q-3.1d"></span>3.1d | A 250 g juice sample contains 0.00025 g of pesticide residue. Find ppm. | 🟡 |

<details>
<summary>View Answers</summary>

**3.1a**: 3 ppm *(Key Step: (0.006/2000) × 10⁶ = 3)*
**3.1b**: 3 ppm *(Key Step: (0.0015/500) × 10⁶ = 3)*
**3.1c**: 2 ppm *(Key Step: 10 mg / 5 kg = 2 ppm)*
**3.1d**: 1 ppm *(Key Step: (0.00025/250) × 10⁶ = 1)*

</details>


---

### Type 2: Reverse — Given ppm, find mass of solute

**The Pattern:** Concentration in ppm known → how much solute in a given amount of solution?

#### Solved Example 3.2
**Q:** Drinking water has 1.2 ppm of fluoride. How much fluoride is present in 5 L (5 kg) of this water? 🟢

**Solution:**
```
Step 1: Understand what 1.2 ppm means
    1.2 ppm = 1.2 mg per kg of solution

Step 2: Calculate for 5 kg
    Mass of fluoride = 1.2 mg/kg × 5 kg = 6 mg = 0.006 g

Answer: 6 mg (or 0.006 g) of fluoride
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.2a"></span>3.2a | Water contains 0.5 ppm of dissolved oxygen. How much O₂ is in 10 L of water? | 🟢 |
| <span id="q-3.2b"></span>3.2b | A lake has mercury at 0.02 ppm. How much mercury is in 1000 kg (1 tonne) of lake water? | 🟡 |
| <span id="q-3.2c"></span>3.2c | Air contains 400 ppm CO₂ by mass. How much CO₂ (in grams) is in 100 kg of air? | 🟢 |
| <span id="q-3.2d"></span>3.2d | The safe limit of lead in drinking water is 15 ppm. A family uses 200 L of water per day. What is the maximum mass of lead they ingest daily? | 🟡 |

<details>
<summary>View Answers</summary>

**3.2a**: 5 mg *(Key Step: 0.5 mg/kg × 10 kg = 5 mg)*
**3.2b**: 20 mg = 0.02 g *(Key Step: 0.02 × 1000 = 20 mg)*
**3.2c**: 40 g *(Key Step: 400 mg/kg × 100 kg = 40,000 mg = 40 g)*
**3.2d**: 3000 mg = 3 g *(Key Step: 15 mg/L × 200 L = 3000 mg)*

</details>


---

### Type 3: Water Hardness Problems (Board Favourite ⭐)

**The Pattern:** Hardness of water is expressed in ppm of CaCO₃. This is the most commonly asked ppm problem in Board exams.

#### Key Background
Water hardness = concentration of Ca²⁺ and Mg²⁺ ions, expressed as **equivalent mass of CaCO₃** in ppm.
- Soft water: < 60 ppm CaCO₃
- Moderately hard: 60–120 ppm
- Hard water: 120–180 ppm
- Very hard: > 180 ppm

#### Solved Example 3.3
**Q:** A water sample has hardness of 150 ppm (as CaCO₃). 
(a) How much CaCO₃ equivalent is present in 1 L of water?
(b) How much CaCO₃ is in 500 L of water used by a household daily? 🟢 ⭐

**Solution:**
```
(a) 150 ppm means 150 mg of CaCO₃ per L (for dilute aqueous)
    = 150 mg per litre
    = 0.15 g per litre

(b) In 500 L:
    Mass of CaCO₃ = 150 mg/L × 500 L = 75,000 mg = 75 g

Answer: (a) 150 mg/L  (b) 75 g
```

#### Solved Example 3.3B
**Q:** A water sample contains 120 mg of MgSO₄ per litre. Express the hardness in ppm of CaCO₃ equivalent. 🟡 ⭐

**Solution:**
```
Step 1: Find moles of MgSO₄ per litre
    Molar mass of MgSO₄ = 24 + 32 + 64 = 120 g/mol
    Moles of MgSO₄ = 120 mg / 120 g/mol = 1 × 10⁻³ mol/L = 1 mmol/L

Step 2: Each MgSO₄ produces 1 Mg²⁺, which is equivalent to 1 CaCO₃
    Moles of CaCO₃ equivalent = 1 × 10⁻³ mol/L

Step 3: Convert to mass of CaCO₃
    Molar mass of CaCO₃ = 100 g/mol
    Mass of CaCO₃ = 1 × 10⁻³ × 100 = 0.1 g/L = 100 mg/L

Step 4: For dilute aqueous solution, mg/L ≈ ppm
    Hardness = 100 ppm (as CaCO₃)

Answer: 100 ppm
```

**Why we convert to CaCO₃ equivalent:** Different hardness-causing ions (Ca²⁺, Mg²⁺) have different molar masses. Converting everything to "CaCO₃ equivalent" gives a single, comparable standard.

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.3a"></span>3.3a | A water sample has hardness of 200 ppm. How much CaCO₃ is deposited when 1000 L of this water is boiled (assuming all temporary hardness)? | 🟡 |
| <span id="q-3.3b"></span>3.3b | Water contains 162 mg/L of Ca(HCO₃)₂. Find hardness in ppm of CaCO₃. (M.M. of Ca(HCO₃)₂ = 162) ⭐ | 🟡 |
| <span id="q-3.3c"></span>3.3c | A sample has 73 mg/L of Mg(HCO₃)₂. Express hardness in ppm as CaCO₃. (M.M. of Mg(HCO₃)₂ = 146) | 🟡 |
| <span id="q-3.3d"></span>3.3d | Water has 111 mg/L CaCl₂ and 95 mg/L MgCl₂. Find total hardness in ppm as CaCO₃. (M.M.: CaCl₂=111, MgCl₂=95) ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**3.3a**: 200 g *(Key Step: 200 mg/L × 1000L = 200,000 mg = 200 g)*
**3.3b**: 100 ppm *(Key Step: 162mg/L → n = 162/162 = 1 mmol/L → CaCO₃ = 100 mg/L = 100 ppm)*
**3.3c**: 50 ppm *(Key Step: 73/146 = 0.5 mmol/L → 0.5 × 100 = 50 mg/L CaCO₃)*
**3.3d**: 150 ppm *(Key Step: CaCl₂: 111/111 = 1 mmol → 100 ppm; MgCl₂: 95/95 = 1 mmol → 100 ppm; Total = 200 ppm. Wait — each contributes 100 ppm, total = 200 ppm.)*

</details>


---

### Type 4: Air Pollution — ppm of Pollutant in Air

**The Pattern:** Concentration of gaseous pollutants in atmosphere.

#### Solved Example 3.4
**Q:** The CO₂ concentration in the atmosphere is approximately 420 ppm by mass. How much CO₂ is present in 1 kg of air? 🟢

**Solution:**
```
420 ppm = 420 parts per million by mass
= 420 mg per kg of air

In 1 kg of air:
    Mass of CO₂ = 420 mg = 0.42 g

Answer: 0.42 g of CO₂ per kg of air
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.4a"></span>3.4a | Ozone (O₃) in the upper atmosphere is about 8 ppm by mass. How much O₃ is in 500 kg of air? | 🟢 |
| <span id="q-3.4b"></span>3.4b | The safe limit of CO in workplace air is 50 ppm. How many mg of CO per kg of air is this? | 🟢 |
| <span id="q-3.4c"></span>3.4c | SO₂ in polluted city air is 0.2 ppm by mass. A person breathes 15 kg of air per day. How much SO₂ does this person inhale? | 🟡 |

<details>
<summary>View Answers</summary>

**3.4a**: 4 g *(Key Step: 8 mg/kg × 500 kg = 4000 mg = 4 g)*
**3.4b**: 50 mg/kg *(Key Step: Direct: 50 ppm = 50 mg/kg)*
**3.4c**: 3 mg *(Key Step: 0.2 mg/kg × 15 kg = 3 mg)*

</details>


---

### Type 5: Trace Analysis — Very Small Quantities

**The Pattern:** Working with µg, ng, and extremely small masses.

#### Solved Example 3.5
**Q:** A blood sample (10 mL, d ≈ 1.06 g/mL) contains 2 µg of lead (Pb). Express the lead concentration in ppm. 🟡

**Solution:**
```
Step 1: Find mass of blood sample
    mass = volume × density = 10 × 1.06 = 10.6 g

Step 2: Convert lead mass to compatible units
    2 µg = 2 × 10⁻⁶ g = 0.002 mg

Step 3: Calculate ppm
    ppm = (mass of solute / mass of solution) × 10⁶
    ppm = (2 × 10⁻⁶ / 10.6) × 10⁶
    ppm = 2 / 10.6
    ppm ≈ 0.189 ppm

Answer: ≈ 0.19 ppm
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.5a"></span>3.5a | A 5 g soil sample contains 15 µg of cadmium. Express in ppm. | 🟡 |
| <span id="q-3.5b"></span>3.5b | A 100 mL water sample (d = 1 g/mL) has 50 µg of arsenic. Find ppm. Is it safe? (WHO limit: 10 ppm) | 🟡 |
| <span id="q-3.5c"></span>3.5c | A 50 g food sample contains 0.3 µg of mercury. Express in ppm and ppb (parts per billion). | 🟡 |

<details>
<summary>View Answers</summary>

**3.5a**: 3 ppm *(Key Step: (15×10⁻⁶/5) × 10⁶ = 3)*
**3.5b**: 0.5 ppm. Safe (WHO limit is 10 ppb = 0.01 ppm. Wait: 10 ppm was stated). If limit is 10 ppm, yes safe. *(Key Step: Check problem)*
**3.5c**: 0.006 ppm = 6 ppb *(Key Step: (0.3×10⁻⁶/50) × 10⁶ = 0.006 ppm)*

</details>


---

### Type 6: ppm to Mass Percent Conversion (and vice versa)

**The Pattern:** Direct mathematical conversion between ppm and %.

#### Solved Example 3.6
**Q:** A solution has 250 ppm of dissolved salt. Express this as mass percent. 🟢

**Solution:**
```
Using: mass % = ppm / 10⁴ = ppm × 10⁻⁴

mass % = 250 / 10,000 = 0.025%

Answer: 0.025% or 2.5 × 10⁻²%
```

#### Solved Example 3.6B
**Q:** A solution is 0.05% sugar by mass. Express in ppm. 🟢

**Solution:**
```
Using: ppm = mass % × 10⁴

ppm = 0.05 × 10,000 = 500 ppm

Answer: 500 ppm
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.6a"></span>3.6a | Convert 75 ppm to mass percent. | 🟢 |
| <span id="q-3.6b"></span>3.6b | Convert 0.002% (w/w) to ppm. | 🟢 |
| <span id="q-3.6c"></span>3.6c | A solution is 1500 ppm NaCl. Express as (a) mass % (b) g per litre (for aqueous, d ≈ 1 g/mL). | 🟡 |
| <span id="q-3.6d"></span>3.6d | The mass percentage of lead in a water sample is 3 × 10⁻⁴%. Express in ppm. Is this above the safe limit of 15 ppm? | 🟡 |

<details>
<summary>View Answers</summary>

**3.6a**: 0.0075% *(Key Step: 75/10⁴ = 0.0075%)*
**3.6b**: 20 ppm *(Key Step: 0.002 × 10⁴ = 20)*
**3.6c**: (a) 0.15% (b) 1.5 g/L *(Key Step: 1500/10⁴ = 0.15%; 1500 mg/L = 1.5 g/L)*
**3.6d**: 3 ppm. Yes, below 15 ppm — safe. *(Key Step: 3×10⁻⁴ × 10⁴ = 3)*

</details>


---

### Type 7: WHO / Safety Guideline Problems

**The Pattern:** Real-world comparison with safety standards.

#### Solved Example 3.7
**Q:** The WHO recommends that fluoride in drinking water should be between 0.5 ppm and 1.5 ppm. A village water supply contains 2.5 mg of fluoride per litre. Is the water safe for drinking? 🟢 ⭐

**Solution:**
```
Step 1: Convert mg/L to ppm
    For dilute aqueous solutions: mg/L ≈ ppm
    Concentration = 2.5 ppm

Step 2: Compare with WHO guidelines
    Safe range: 0.5 to 1.5 ppm
    Sample: 2.5 ppm > 1.5 ppm (upper limit)

Answer: The water is NOT safe. Fluoride level (2.5 ppm) exceeds 
        the WHO upper limit (1.5 ppm). Excess fluoride causes 
        fluorosis (damage to teeth and bones).
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.7a"></span>3.7a | WHO limit for arsenic in drinking water is 10 ppb (parts per billion). A sample has 0.015 ppm. Is it safe? (1 ppm = 1000 ppb) ⭐ | 🟡 |
| <span id="q-3.7b"></span>3.7b | The permissible limit of nitrate in drinking water is 45 ppm. A water sample has 0.005% nitrate by mass. Is it safe? | 🟡 |
| <span id="q-3.7c"></span>3.7c | Chlorine residual in treated drinking water should be 0.2–1.0 ppm. A treatment plant adds 3 g of Cl₂ to 10,000 L of water. Find the resulting concentration. Is it in the safe range? | 🟡 |

<details>
<summary>View Answers</summary>

**3.7a**: 15 ppb = 0.015 ppm > 10 ppb = 0.01 ppm → NOT safe *(Key Step: Unit conversion)*
**3.7b**: 0.005% = 50 ppm > 45 ppm → NOT safe *(Key Step: 0.005 × 10⁴ = 50)*
**3.7c**: 0.3 ppm. Within range (0.2-1.0 ppm). *(Key Step: 3g/10⁷g × 10⁶ = 0.3)*

</details>


---

### Type 8: ppm in Aqueous Solutions — The mg/L Shortcut

**The Pattern:** For dilute aqueous solutions, exploiting d ≈ 1 g/mL to simplify calculations.

#### Solved Example 3.8
**Q:** Explain why, for dilute aqueous solutions, ppm ≈ mg/L. Under what conditions does this approximation fail? 🟡

**Solution:**
```
Derivation:
    ppm = (mass of solute / mass of solution) × 10⁶

    For 1 L of dilute aqueous solution:
        mass of solution ≈ 1000 g = 1 kg  (since d ≈ 1 g/mL)
    
    ppm = (mass of solute in g / 1000 g) × 10⁶
        = mass of solute in g × 1000
        = mass of solute in mg

    So: ppm = mg of solute per litre = mg/L ✅

This approximation FAILS when:
    1. Solution is concentrated (density ≠ 1 g/mL)
    2. Solvent is not water (e.g., organic solvents)
    3. Solution has high dissolved solid content (brine, seawater)

For seawater (d ≈ 1.025 g/mL), the error is about 2.5%.
```

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.8a"></span>3.8a | A solution has 50 ppm NaCl. If d_solution = 1.0 g/mL, how many mg are in 1 L? What if d = 1.2 g/mL? | 🟡 |
| <span id="q-3.8b"></span>3.8b | Seawater (d = 1.025 g/mL) has about 35,000 ppm dissolved salts. Find (a) mass of salt per litre using the exact formula (b) using the mg/L approximation (c) percentage error. | 🔴 |

<details>
<summary>View Answers</summary>

**3.8a**: If d=1: 50 mg. If d=1.2: 50×1.2=60mg actual in 1L, but ppm is still 50 (mass-based). mg/L would be 60. *(Key Step: Key distinction)*
**3.8b**: (a) 35,000 × 1.025/1000 × 1000 = 35.875 g/L (b) 35 g/L by approx (c) ~2.5% error *(Key Step: Density correction)*

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-3.M1"></span>3.M1 | A water sample has 200 ppm of dissolved salts. (a) Express as mass %. (b) How much salt is in 50 L of this water? (c) If the salt is entirely NaCl (M.M. = 58.5), how many moles of NaCl is this? | T6 + T2 + new | 🟡 |
| <span id="q-3.M2"></span>3.M2 | The fluoride level in a village well is 3.5 ppm. The WHO limit is 1.5 ppm. If the village mixes this water with fluoride-free water in equal volumes, what is the resulting fluoride concentration? Is it now safe? | T7 + T1 | 🟡 |
| <span id="q-3.M3"></span>3.M3 | A factory discharge has 500 ppm of mercury. If 1000 L of this discharge is released into a lake containing 10⁶ L of water (originally 0 ppm Hg), find the final Hg concentration in ppm. | T1 + T2 | 🔴 |
| <span id="q-3.M4"></span>3.M4 | 100 mg of Ca(HCO₃)₂ and 50 mg of MgCl₂ are dissolved in 1 L of water. Find (a) total dissolved solids in ppm (b) hardness in ppm as CaCO₃. Molar masses: Ca(HCO₃)₂ = 162, MgCl₂ = 95, CaCO₃ = 100. | T3 + T1 | 🔴 |

<details>
<summary>View Answers</summary>

**3.M1**: Answer not found.
**3.M2**: Answer not found.
**3.M3**: Answer not found.
**3.M4**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.B1"></span>3.B1 | Calculate the mass of urea (NH₂CONH₂) required to be dissolved in 1000 g of water in order to reduce the vapour pressure to 99.5% of the vapour pressure of pure water at that temperature. Express the concentration in ppm. *(Hint: involves Raoult's Law — preview)* | 🔴 |
| <span id="q-3.B2"></span>3.B2 | The recommended concentration of fluoride in drinking water is up to 1 ppm. The molar mass of fluoride (as NaF) is 42 g/mol. How many moles of NaF are present per litre of water at this concentration? ⭐ | 🟡 |
| <span id="q-3.B3"></span>3.B3 | Express 500 ppm of KCl in water as (a) mass percent and (b) molality. (M.M. of KCl = 74.5) ⭐ | 🟡 |
| <span id="q-3.B4"></span>3.B4 | A 1 kg water sample is found to contain 2 mg of lead. Express the concentration as (a) ppm (b) mass percent (c) mg/L (assume d = 1 g/mL). | 🟢 |

<details>
<summary>View Answers</summary>

**3.B1**: Answer not found.
**3.B2**: Answer not found.
**3.B3**: Answer not found.
**3.B4**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-3.J1"></span>3.J1 | Sea water contains 6 × 10⁻³ ppm of dissolved gold. The total mass of ocean water is approximately 1.4 × 10²¹ kg. Calculate the total mass of dissolved gold in the oceans (in tonnes). | 🟡 |
| <span id="q-3.J2"></span>3.J2 | A 10 ppm solution of NaCl (M.M. = 58.5) in water has density approximately 1 g/mL. Find (a) its molarity (b) its molality. ⭐ | 🔴 |
| <span id="q-3.J3"></span>3.J3 | Air contains 78% N₂, 21% O₂, and the rest is argon and trace gases. If CO₂ is 420 ppm by mass of the total atmosphere, and the mass of Earth's atmosphere is 5.15 × 10¹⁸ kg, find the total mass of CO₂ in the atmosphere. | 🟡 |
| <span id="q-3.J4"></span>3.J4 | Hard water contains 120 ppm of Ca²⁺ ions. Express the Ca²⁺ concentration in mol/L. (Atomic mass of Ca = 40). ⭐ | 🟡 |
| <span id="q-3.J5"></span>3.J5 | A water sample has 2 ppm of dissolved chlorine (Cl₂). If Cl₂ disinfection requires at least 0.5 ppm residual after 30 minutes, and 60% of the Cl₂ reacts with organic matter, is the initial dose sufficient? | 🔴 |

<details>
<summary>View Answers</summary>

**3.J1**: Answer not found.
**3.J2**: Answer not found.
**3.J3**: Answer not found.
**3.J4**: Answer not found.
**3.J5**: Answer not found.

</details>


---

## Key Takeaways from Chapter 3

```
┌─────────────────────────────────────────────────────┐
│                   PPM SUMMARY                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Formula: ppm = (W_solute / W_solution) × 10⁶       │
│                                                      │
│  Key relationship: 1% = 10,000 ppm                  │
│                                                      │
│  For dilute aqueous solutions:                       │
│      ppm ≈ mg/L ≈ mg/kg                            │
│      (because d_solution ≈ 1 g/mL)                  │
│                                                      │
│  Temperature: INDEPENDENT ✅ (mass-based)            │
│                                                      │
│  Most common exam topic:                             │
│      Water hardness in ppm of CaCO₃                 │
│                                                      │
│  ppb = parts per billion = ppm × 10⁻³               │
│      1 ppm = 1000 ppb                               │
│                                                      │
│  Conversions:                                        │
│      ppm → mass%: divide by 10⁴                     │
│      mass% → ppm: multiply by 10⁴                   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

*← [Chapter 2 — Volume Percent](./02-volume-percent.md) | [Chapter 4 — Mole Fraction →](./04-mole-fraction.md)*
