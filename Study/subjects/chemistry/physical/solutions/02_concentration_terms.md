# Chapter 2: The Language of Concentration
## Overview of All Concentration Terms

---

## 🎯 Stage 1: The Core Idea

### Why Do We Need Concentration?<br>

"My tea has sugar" — useless information.
"My tea has 5 grams of sugar" — better, but still depends on how much tea.
"My tea is 2% sugar by mass" — *now* you know exactly how sweet it is.

**Concentration** tells you how much solute is packed into a given amount of solution. Without it, chemistry becomes vague.

The problem?<br> There are **six major ways** to express concentration, each designed for a different purpose. Knowing which one to use — and how they relate — is the core skill of this entire chapter.

### The Six Concentration Terms at a Glance

| Term | Symbol | Formula | Units | Temperature Dependent?<br> |
|------|--------|---------|-------|------------------------|
| **Molarity** | M | mol solute / L solution | mol/L | **Yes** (volume changes with T) |
| **Molality** | m | mol solute / kg solvent | mol/kg | **No** (mass doesn't change with T) |
| **Mole Fraction** | χ (chi) | mol component / total mol | Dimensionless | **No** |
| **Mass Percent** | w/w% | (mass solute / mass solution) × 100 | % | **No** |
| **ppm** | ppm | (mass solute / mass solution) × 10⁶ | ppm | **No** |
| **Normality** | N | equivalents / L solution | eq/L | **Yes** |

### The Big Divide: Mass-Based vs. Volume-Based

```
    ┌──────────────────────────────┬─────────────────────────────┐
    │   MASS-BASED (T-independent) │   VOLUME-BASED (T-dependent)│
    │                              │                             │
    │   • Mass percent (w/w%)      │   • Molarity (M)            │
    │   • Molality (m)             │   • Normality (N)           │
    │   • Mole Fraction (χ)        │                             │
    │   • ppm                      │                             │
    └──────────────────────────────┴─────────────────────────────┘

KEY INSIGHT: To convert between these two groups, you ALWAYS need DENSITY.
```

### When to Use Which?<br>

| Situation | Use |
|-----------|-----|
| Lab measurements, reactions | Molarity (M) |
| Temperature-varying experiments | Molality (m) |
| Colligative properties (VP, BP, FP, osmosis) | Mole fraction or Molality |
| Commercial chemicals, food labels | Mass percent (w/w%) |
| Environmental chemistry, trace amounts | ppm |
| Acid-base / redox titrations | Normality (N) |

---

## 🔬 Stage 2: The Formula Lab

### All Six Formulas — Clean Reference

**1. Molarity (M)**
```
         Moles of solute (n)           W_solute × 1000
M = ──────────────────────────── = ────────────────────────
      Volume of solution (L)          MM_solute × V_mL
```
- W_solute = mass of solute in grams
- MM_solute = molar mass of solute
- V_mL = volume of solution in mL

---

**2. Molality (m)**
```
         Moles of solute              W_solute × 1000
m = ──────────────────────── = ────────────────────────────
      Mass of solvent (kg)          MM_solute × W_solvent_g
```

---

**3. Mole Fraction (χ)**
```
             n_A                          n_B
χ_A = ────────────────     χ_B = ────────────────
         n_A + n_B                   n_A + n_B

→ Always: χ_A + χ_B = 1 (for binary solution)
```

---

**4. Mass Percent (w/w%)**
```
              W_solute
w/w% = ────────────────── × 100
           W_solution
```
where W_solution = W_solute + W_solvent

---

**5. ppm (Parts Per Million)**
```
             W_solute (g)
ppm = ─────────────────────── × 10⁶
          W_solution (g)

(Or equivalently: ppm = w/w% × 10,000)
```

---

**6. Normality (N)**
```
         Equivalents of solute            M × n-factor
N = ─────────────────────────────── = ────────────────────
         Volume of solution (L)               1
```
where n-factor = number of H⁺ (acid), OH⁻ (base), or electrons transferred (redox)

---

### Summary Table: What Goes Where

| Term | Numerator | Denominator |
|------|-----------|-------------|
| Molarity M | mol solute | L of **solution** |
| Molality m | mol solute | kg of **solvent** |
| Mole Fraction χ | mol component | Total mol (solute + solvent) |
| Mass % | g solute | g of **solution** |
| ppm | g solute | g of **solution** × 10⁶ |

> **⚠️ #1 Exam Trap:** Molality uses kg of **solvent**. Molarity uses L of **solution**. These are NOT interchangeable. Mixing them up is the single most common mistake in this chapter.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Identifying the Concentration Term from Context

**The Pattern:** You're given a situation. Which term applies?<br>

#### Solved Example 2.1
**Q:** A chemist needs a concentration that won't change when the laboratory temperature shifts from 20°C to 30°C. Which term should they use?<br> 🟢

**Solution:**
```
Temperature-independent terms:
    - Molality ✓
    - Mole Fraction ✓
    - Mass percent ✓
    - ppm ✓

Temperature-dependent terms (avoid):
    - Molarity ✗ (volume changes with T)

Answer: Use Molality (m) or Mole Fraction or Mass percent.
```

#### Solved Example 2.2
**Q:** Which concentration term is most appropriate to describe the concentration of fluoride ions (0.0003%) in drinking water?<br> 🟢

**Solution:**
```
0.0003% is an extremely small concentration.
ppm = mass percent × 10,000
0.0003% × 10,000 = 3 ppm

→ ppm is the appropriate term for trace/environmental amounts.
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 2.1a | Why is molality preferred over molarity for colligative property calculations?<br> | 🟢 |
| 2.1b | A solution is used in titrations. Which term gives the most direct equivalence relationship?<br> | 🟢 |
| 2.1c | In the formula for Raoult's Law and Henry's Law, which concentration term appears?<br> | 🟡 |
| 2.1d | A 37% HCl solution: this concentration is expressed as which term?<br> | 🟢 |
| 2.1e | Which concentration term(s) are dimensionless?<br> | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**2.1a:**
- Colligative properties involve solutions at varying temperatures (boiling point elevation, freezing point depression).
- Molality uses kg of solvent (mass) → **temperature-independent** → doesn't change as solution expands/contracts.
- Molarity uses volume of solution → changes with temperature → unreliable.

**2.1b:**
- **Normality (N)** — because 1 equivalent of acid reacts with exactly 1 equivalent of base regardless of formula. N_acid × V_acid = N_base × V_base.

**2.1c:**
- **Mole Fraction (χ)** — Raoult's Law: P_A = χ_A × P°_A. Henry's Law: P_gas = K_H × χ_gas.

**2.1d:**
- **Mass percent (w/w%)** — "37% HCl" means 37 g HCl per 100 g solution.

**2.1e:**
- **Mole fraction (χ)** — mol/mol ratio, no units.
- (Mass percent has units of %, but is sometimes considered dimensionless ratio × 100)
</details>

---

### Type 2: Calculating Each Concentration Term from Given Data

**The Pattern:** You're given mass of solute, mass of solvent or volume of solution. Calculate a specific term.

#### Solved Example 2.3 — Calculating Molarity
**Q:** 5.85 g of NaCl (MM = 58.5 g/mol) is dissolved in water to make 500 mL of solution. Find Molarity. 🟢

**Solution:**
```
Step 1: Moles of NaCl = 5.85 / 58.5 = 0.1 mol

Step 2: Volume of solution = 500 mL = 0.5 L

Step 3: M = n / V = 0.1 / 0.5 = 0.2 mol/L

Answer: M = 0.2 M
```

#### Solved Example 2.4 — Calculating Molality
**Q:** 5.85 g of NaCl is dissolved in 500 g of water. Find Molality. 🟢

**Solution:**
```
Step 1: Moles of NaCl = 5.85 / 58.5 = 0.1 mol

Step 2: Mass of solvent = 500 g = 0.5 kg

Step 3: m = n / kg_solvent = 0.1 / 0.5 = 0.2 mol/kg

Answer: m = 0.2 m (molal)
```

> **Notice:** Same mass of solute, same numerical answer — but these are DIFFERENT denominator types! In a real problem, molarity ≠ molality.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 2.2a | 4.9 g of H₂SO₄ (MM = 98) is dissolved in 250 mL of solution. Find M. | 🟢 |
| 2.2b | 4.9 g of H₂SO₄ is dissolved in 250 g of water. Find molality. | 🟢 |
| 2.2c | 18 g of glucose (MM = 180) and 18 g of water. Find mole fraction of glucose. | 🟡 |
| 2.2d | 10 g of NaOH is dissolved in 90 g of water. Find mass percent of NaOH. | 🟢 |
| 2.2e | 0.002 g of arsenic is found in 1 kg of water. Express in ppm. | 🟢 |
| 2.2f | 9.8 g of H₂SO₄ in 500 mL solution. Find Normality (n-factor = 2). | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**2.2a:**
- n = 4.9/98 = 0.05 mol; V = 0.250 L
- **M = 0.05/0.250 = 0.2 M**

**2.2b:**
- n = 0.05 mol; solvent = 0.250 kg
- **m = 0.05/0.250 = 0.2 m**

**2.2c:**
- n_glucose = 18/180 = 0.1 mol; n_water = 18/18 = 1.0 mol
- χ_glucose = 0.1/(0.1+1.0) = 0.1/1.1 = **0.0909**
- χ_water = 1 - 0.0909 = **0.9091**

**2.2d:**
- Solution mass = 10 + 90 = 100 g
- **w/w% = (10/100) × 100 = 10%**

**2.2e:**
- ppm = (0.002 / 1000) × 10⁶ = **2 ppm**
- *(Note: 1 kg = 1000 g; solution ≈ solvent for very dilute solutions)*

**2.2f:**
- n_H₂SO₄ = 9.8/98 = 0.1 mol; equivalents = 0.1 × 2 = 0.2 eq
- V = 0.5 L
- **N = 0.2/0.5 = 0.4 N**
</details>

---

### Type 3: Temperature Dependence — Conceptual

**The Pattern:** Identify which terms change when temperature changes and explain why.

#### Solved Example 2.5
**Q:** A 1 M glucose solution is prepared at 25°C. When heated to 80°C, does the molarity change?<br> Does molality change?<br> 🟡

**Solution:**
```
At 25°C → 1 M = 1 mol glucose per litre.

When heated to 80°C:
    - Water expands → volume of solution INCREASES
    - Same moles of glucose in MORE volume
    → Molarity DECREASES (M < 1 M at 80°C)

Molality:
    - Moles of glucose: unchanged ✓
    - Mass of water: unchanged (mass doesn't expand) ✓
    → Molality is UNCHANGED ✓

Answer: Molarity changes (decreases). Molality stays constant.
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 2.3a | List all concentration terms that are temperature-independent and explain why. | 🟡 |
| 2.3b | A 2 M NaCl solution is cooled from 25°C to 5°C. Does concentration increase or decrease?<br> Which term is it expressed in matters — explain. | 🟡 |
| 2.3c | For a colligative property calculation, why should molality be used instead of molarity?<br> Give a concrete example. | 🔴 |
| DPP 3.8 | Which of the following concentration terms is temperature dependent?<br> <br>
(A) % by mass <br>
(B) Mole fraction <br>
(C)
 Mass/volume ratio <br>
(D) Molality | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**2.3a:**
- **Temperature-independent:** Molality (uses kg of solvent — mass is constant), Mole fraction (uses moles of components — moles don't change), Mass percent (uses mass of solute and solution — both constant), ppm (mass-based).
- **Temperature-dependent:** Molarity (L of solution — volume changes with T), Normality (L of solution — same as Molarity).
- **Why:** Volume expands/contracts with temperature; mass does not.

**2.3b:**
- Cooling = volume decreases (liquid contracts slightly) → same moles in less volume.
- **If in Molarity:** M increases (more mol per L) as volume decreases.
- **If in Molality/Mass%:** No change — mass doesn't change with temperature.
- The "2 M NaCl" label is only accurate at the temperature at which it was prepared.

**2.3c:**
- Colligative properties like ΔT_b = K_b × m use molality.
- Example: ΔT_b of a 1 molal NaCl solution = 0.52 × 1 = 0.52°C.
- If we said "1 M NaCl" and the experiment is run at 50°C, the actual volume has expanded, the true molarity has dropped below 1 M — but the molality is still exactly 1 molal.
- Using molarity would give a wrong ΔT_b. Molality gives the correct answer regardless of temperature.

**DPP 3.8:**
- Terms based on mass (% by mass, mole fraction, molality) are independent of temperature because mass does not change with temperature.
- Mass/volume ratio (w/v%) depends on the volume of solution, which expands or contracts with temperature changes.
- **Answer: <br>
(C)
 Mass/volume ratio**
</details>

---

### Type 4: Comparison of Terms for the Same Solution

**The Pattern:** Given data, calculate multiple concentration terms for the same solution. Compare them.

#### Solved Example 2.6
**Q:** 36 g of glucose (MM = 180 g/mol) is dissolved in 200 mL of water (density of water = 1 g/mL, density of solution = 1.08 g/mL). Calculate: M, m, χ_glucose, w/w%. 🔴 ⭐

**Solution:**
```
Given:
    W_glucose = 36 g
    V_water = 200 mL → W_water = 200 g (density = 1)
    V_solution = ?<br> → W_solution = 36 + 200 = 236 g
    V_solution = 236 / 1.08 = 218.5 mL = 0.2185 L

Step 1 — Moles:
    n_glucose = 36 / 180 = 0.2 mol
    n_water = 200 / 18 = 11.11 mol

Step 2 — Molarity:
    M = n / V_soln = 0.2 / 0.2185 = 0.915 M

Step 3 — Molality:
    m = n / kg_solvent = 0.2 / 0.200 = 1.0 m

Step 4 — Mole Fraction of Glucose:
    χ_glucose = 0.2 / (0.2 + 11.11) = 0.2 / 11.31 = 0.0177

Step 5 — Mass Percent:
    w/w% = (36 / 236) × 100 = 15.25%
```

> **Key observation:** M ≠ m even for the same solution. Here M = 0.915 but m = 1.0. They're close because density is close to 1, but they are NOT equal.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 2.4a | 4.5 g of glucose (MM = 180) in 250 mL of solution (d = 1.02 g/mL). Find M and w/w%. | 🟡 |
| 2.4b | 5.85 g NaCl in 500 g water. Find m and χ_NaCl. | 🟡 |
| 2.4c | Why would molarity and molality for the same solution be equal only if density = 1 g/mL and solute molar mass is negligibly small?<br> | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**2.4a:**
- n_glucose = 4.5/180 = 0.025 mol; V_soln = 0.250 L
- **M = 0.025/0.250 = 0.1 M**
- W_soln = 0.250 L × 1.02 g/mL × 1000 mL/L = 255 g
- **w/w% = (4.5/255) × 100 = 1.76%**

**2.4b:**
- n_NaCl = 5.85/58.5 = 0.1 mol; W_solvent = 500 g = 0.5 kg
- **m = 0.1/0.5 = 0.2 m**
- n_water = 500/18 = 27.78 mol
- **χ_NaCl = 0.1/(0.1 + 27.78) = 0.1/27.88 = 0.00359**

**2.4c:**
- Molarity = n_solute / V_soln (L). Molality = n_solute / W_solvent (kg).
- If density = 1 g/mL: 1 L solution = 1000 g solution.
- If solute mass is negligible: 1000 g solution ≈ 1000 g solvent = 1 kg solvent.
- Then V_soln (L) ≈ W_solvent (kg) → M ≈ m.
- But in real solutions, solute has mass, and density ≠ 1 exactly → M ≠ m.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 2.M1 | A solution of H₂SO₄ is 49% by mass and has density 1.39 g/mL. Find M and N (n-factor = 2). ⭐ | T2 + T2(N) | 🟡 |
| 2.M2 | 100 mL of 0.1 M HCl is heated. Does the molarity change?<br> What if you use molality?<br> | T3 + conceptual | 🟡 |
| 2.M3 | 2 g of a solute is dissolved in 100 g of water. The solution has density 1.012 g/mL. Calculate: (a) ppm, (b) w/w%, (c) molarity if MM = 40 g/mol, (d) molality. | T2 all terms | 🔴 |
| 2.M4 | Why is mole fraction used in Raoult's law?<br> Why not molarity?<br> | T1 + T3 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**2.M1:**
- W_soln per 100 g: W_H₂SO₄ = 49 g, W_water = 51 g
- n_H₂SO₄ = 49/98 = 0.5 mol
- V_solution = 100 g / 1.39 g/mL = 71.94 mL = 0.07194 L
- **M = 0.5 / 0.07194 = 6.95 M ≈ 6.95 M**
- **N = M × n-factor = 6.95 × 2 = 13.9 N**

**2.M2:**
- Heating → liquid expands → volume increases.
- Same moles of HCl in greater volume → **Molarity decreases**.
- Mass of solvent unchanged → **Molality unchanged**.

**2.M3:**
- W_solute = 2 g, W_solvent = 100 g, W_solution = 102 g
- V_solution = 102 / 1.012 = 100.8 mL = 0.1008 L
- **(a) ppm = (2/102) × 10⁶ = 19,608 ppm ≈ 19,600 ppm**
- **(b) w/w% = (2/102) × 100 = 1.96%**
- **(c) n = 2/40 = 0.05 mol; M = 0.05/0.1008 = 0.496 M ≈ 0.5 M**
- **(d) m = 0.05/0.100 = 0.5 m**

**2.M4:**
- Raoult's Law involves the ratio of molecules of one component to total molecules at the solution surface — this is exactly what mole fraction measures.
- Mole fraction is temperature-independent and captures the ratio of particles — the physical quantity that determines vapour pressure.
- Molarity depends on volume (temperature-dependent) and includes the entire solution volume, not just the surface composition.
- Using molarity in Raoult's Law would give inconsistent results at different temperatures.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 2.B1 | What is the SI unit of molality?<br> Why is molality preferred for colligative property calculations?<br> *(NCERT)* | 🟢 |
| 2.B2 | Which of the following are temperature-dependent: (a) mass percent, (b) molarity, (c) molality, (d) mole fraction?<br> | 🟢 |
| 2.B3 | Express the concentration of 0.5 ppm fluoride ion in terms of molarity (MM of F = 19). | 🟡 |
| 2.B4 | Calculate the mole fraction of ethanol in a solution containing 46 g ethanol (MM = 46) and 54 g water. *(NCERT pattern)* ⭐ | 🟢 |
| 2.B5 | What is the difference between the denominator in Molarity and in Molality?<br> Why does this matter for temperature dependence?<br> | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**2.B1:**
- SI unit: **mol kg⁻¹** (moles per kilogram of solvent)
- Preferred for colligative properties because it uses mass (kg) of solvent — mass doesn't change with temperature. Molarity uses volume which expands/contracts, making it unreliable.

**2.B2:**
- (a) Mass percent → **Temperature-independent** (mass/mass)
- (b) Molarity → **Temperature-dependent** (mol/volume — volume changes with T)
- (c) Molality → **Temperature-independent** (mol/kg — mass is constant)
- (d) Mole fraction → **Temperature-independent** (mol/mol)

**2.B3:**
- 0.5 ppm = 0.5 g F⁻ per 10⁶ g solution ≈ 0.5 g per 10⁶ g water = 0.5 g per 1000 L
- n_F = 0.5/19 = 0.02632 mol per 1000 L = **2.63 × 10⁻⁵ mol/L = 2.63 × 10⁻⁵ M**

**2.B4:**
- n_ethanol = 46/46 = 1 mol; n_water = 54/18 = 3 mol
- Total moles = 1 + 3 = 4 mol
- **χ_ethanol = 1/4 = 0.25**
- **χ_water = 3/4 = 0.75**

**2.B5:**
- Molarity: denominator = **L of solution** (solution volume changes when T changes)
- Molality: denominator = **kg of solvent** (mass is invariant; doesn't change with T)
- This is why molarity is T-dependent and molality is T-independent. When temperature changes, the solution expands (more volume), but the mass of solvent remains constant.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q2.J1 🟡 ⭐**
Which of the following concentration terms does NOT change when the solution is heated?<br>
<br>
(A) Molarity  <br>
(B) Normality  <br>
(C)
 Molality  <br>
(D) All change

**Q2.J2 🟡**
Mole fraction of water in a 1 molal aqueous NaCl solution is approximately:
<br>
(A) 0.018  <br>
(B) 0.982  <br>
(C)
 1.0  <br>
(D) 0.5

**Q2.J3 🔴 ⭐**
A solution of H₂SO₄ is 18% by mass and has density 1.20 g/mL. The molarity of the solution is closest to:
<br>
(A) 1.8 M  <br>
(B) 2.2 M  <br>
(C)
 2.4 M  <br>
(D) 3.6 M

**Q2.J4 🔴**
Which pair has the same units?<br>
<br>
(A) Molarity and Normality  <br>
(B) Molality and Mole Fraction  <br>
(C)
 ppm and Mass percent  <br>
(D) All are dimensionless

**Q2.J5 🔴 ⭐**
The concentration of a solution is expressed as 500 ppm. What is the equivalent mass percent?<br>
<br>
(A) 0.05%  <br>
(B) 0.5%  <br>
(C)
 5%  <br>
(D) 50%

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**2.J1 → Answer: <br>
(C)
**
- Molarity <br>
(A) and Normality <br>
(B) both use volume in denominator → T-dependent.
- **Molality uses kg of solvent (mass) → T-independent ✓**

**2.J2 → Answer: <br>
(B)**
- 1 molal NaCl = 1 mol NaCl per 1 kg water
- n_NaCl = 1 mol; n_water = 1000/18 = 55.56 mol
- χ_water = 55.56/(55.56+1) = 55.56/56.56 = **0.982 ✓**
- *(Trap: students often pick 0.018, which is χ_NaCl, not χ_water)*

**2.J3 → Answer: <br>
(B)**
- Per 100 g solution: 18 g H₂SO₄, 82 g water
- n_H₂SO₄ = 18/98 = 0.1837 mol
- V_solution = 100 g / 1.20 g/mL = 83.33 mL = 0.08333 L
- **M = 0.1837/0.08333 = 2.20 M ✓**

**2.J4 → Answer: <br>
(A)**
- Molarity: mol/L → Normality: eq/L → same SI dimension [amount/volume]
- Molality: mol/kg → Mole Fraction: dimensionless → different
- ppm: mass/mass × 10⁶ → mass percent: mass/mass × 100 → same ratio, different scale
- **Answer: <br>
(A)** Molarity and Normality have the same units (mol/L or eq/L)

**2.J5 → Answer: <br>
(A)**
- ppm = (g solute / g solution) × 10⁶
- Mass % = (g solute / g solution) × 100
- Relation: **Mass % = ppm / 10,000**
- 500 ppm / 10,000 = **0.05% ✓**
</details>

---

## Key Takeaways from Chapter 2

| Must Remember | Detail |
|--------------|--------|
| **Molarity denominator** | Litres of **solution** (volume changes with T) |
| **Molality denominator** | kg of **solvent** (mass, T-independent) |
| **Mole fraction** | Dimensionless; used in Raoult's & Henry's Law |
| **ppm = mass% × 10,000** | Conversion shortcut |
| **For colligative properties** | Always use molality or mole fraction |
| **To convert M ↔ m** | You need density |

---

## 🧠 Stage 7: Statement & Assertion-Reasoning

**Directions:** These questions test your psychological resilience against tricky phrasing. 
- For **Assertion-Reason**, choose:
  <br>
(A) Both A and R are true, and R is the correct explanation of A.
  <br>
(B) Both A and R are true, but R is NOT the correct explanation of A.
  <br>
(C)
 A is true but R is false.
  <br>
(D) A is false but R is true.
- For **Statement I/II**, choose based on whether each statement is correct or incorrect.

| # | Question | Difficulty |
|---|----------|------------|
| 2.S1 | **Assertion <br>
(A):** The molarity of a $0.1\text{ M}$ aqueous solution of NaCl increases when it is heated from $25^\circ\text{C}$ to $50^\circ\text{C}$.<br>**Reason (R):** Heating causes the volume of the solution to expand. | 🟡 |
| 2.S2 | **Statement I:** Molality is always preferred over molarity in experiments involving significant temperature changes.<br>**Statement II:** The mass of a solvent is independent of temperature variations. | 🟢 |
| 2.S3 | **Assertion <br>
(A):** For a very dilute aqueous solution, molarity and molality are almost numerically equal.<br>**Reason (R):** In highly dilute aqueous solutions, the density of the solution is approximately $1\text{ g/mL}$ and the mass of solute is negligible compared to the solvent. | 🟡 |
| 2.S4 | **Statement I:** Normality of a solution changes with temperature.<br>**Statement II:** Normality is defined as the number of equivalents of solute per kilogram of solvent. | 🟡 |
| 2.S5 | **Assertion <br>
(A):** A $10\% (\text{w/w})$ solution of $H_2SO_4$ in water is prepared. Its mole fraction of $H_2SO_4$ is independent of temperature.<br>**Reason (R):** Mole fraction is a ratio of moles, and the number of moles does not change upon heating. | 🟢 |
| 2.S6 | **Statement I:** $1\text{ ppm}$ of a solute is equivalent to $1\text{ mg}$ of solute dissolved in $1\text{ L}$ of an aqueous solution having a density of $1\text{ g/mL}$.<br>**Statement II:** Parts per million is purely a volume-based concentration unit. | 🟡 |
| 2.S7 | **Assertion <br>
(A):** The sum of mole fractions of all components in any solution is always equal to 1.<br>**Reason (R):** Mole fraction is a dimensionless quantity representing the part of a whole. | 🟢 |
| 2.S8 | **Statement I:** Molarity of a solution is determined by dividing the moles of solute by the volume of the solvent in liters.<br>**Statement II:** The volume of a solution is always exactly equal to the sum of the volumes of the solute and the solvent. | 🔴 |
| 2.S9 | **Assertion <br>
(A):** Molality is defined as the number of moles of solute dissolved per liter of solvent.<br>**Reason (R):** The density of water is exactly $1\text{ g/mL}$ at all temperatures, so $1\text{ L}$ of water is always $1\text{ kg}$. | 🔴 |
| 2.S10 | **Statement I:** Mass percentage ($\%\text{ w/w}$) of a solution decreases as the temperature increases.<br>**Statement II:** The mass of a liquid solution remains constant regardless of temperature changes (assuming no evaporation). | 🟡 |
| 2.S11 | **Assertion <br>
(A):** If equal masses of two solutions (A and B) of the same solute are mixed, the final mass percent is simply the average of their individual mass percents.<br>**Reason (R):** Mass percent is an additive property when equal masses of solutions are combined. | 🟡 |
| 2.S12 | **Statement I:** $500\text{ ppm}$ of fluoride in toothpaste means there is $500\text{ g}$ of fluoride per $10^6\text{ g}$ of toothpaste.<br>**Statement II:** $500\text{ ppm}$ is equivalent to $5\% (\text{w/w})$. | 🟢 |
| 2.S13 | **Assertion <br>
(A):** Normality of a given acid solution can never be less than its molarity.<br>**Reason (R):** Normality is the product of molarity and the n-factor, and the n-factor for any substance is an integer $\ge 1$. | 🟡 |
| 2.S14 | **Statement I:** To convert molarity to molality, one must know the molar mass of the solvent.<br>**Statement II:** Density of the solution is absolutely required to convert between molarity and molality. | 🔴 |
| 2.S15 | **Assertion <br>
(A):** A $1\text{ m}$ solution of $NaCl$ is more concentrated than a $1\text{ M}$ solution of $NaCl$ at room temperature.<br>**Reason (R):** $1\text{ M}$ solution contains $1\text{ mole}$ in $1000\text{ mL}$ of solution, meaning the solvent volume is less than $1000\text{ mL}$, whereas $1\text{ m}$ contains $1\text{ mole}$ in $1000\text{ g}$ of solvent. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**2.S1 → Answer: <br>
(D) A is false but R is true.**
- A is false: When heated, volume expands. Molarity = moles / volume. Since the denominator (volume) increases, the overall fraction (molarity) **decreases**, not increases.
- R is true: Liquids generally expand on heating.

**2.S2 → Statement I is True, Statement II is True.**
- Both statements are correct, and Statement II is exactly why Statement I is true. Molality depends on mass, which is T-independent.

**2.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- For a highly dilute aqueous solution, mass of solute is tiny, so mass of solution $\approx$ mass of solvent. Since density is $1\text{ g/mL}$, $1\text{ L}$ of solution weighs $1\text{ kg}$, making the denominators for M and m practically identical.

**2.S4 → Statement I is True, Statement II is False.**
- Statement I is true: Normality = equivalents / volume of solution. Volume changes with T, so Normality changes.
- Statement II is false: Normality is per *liter of solution*, not *kilogram of solvent*.

**2.S5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Mole fraction is based purely on the number of moles. Moles are calculated from mass, and mass does not change with temperature.

**2.S6 → Statement I is True, Statement II is False.**
- Statement I is true: $1\text{ mg}$ in $1\text{ L}$ water ($1000\text{ g}$) is $1\text{ mg}$ per $1,000,000\text{ mg}$, which is $1\text{ ppm}$.
- Statement II is false: ppm is fundamentally a **mass/mass** ratio (parts per million by mass), not volume-based.

**2.S7 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- The fractions of all components must add up to the whole (1).

**2.S8 → Both Statements are False.**
- Statement I is false: Molarity is moles divided by volume of **solution**, not solvent.
- Statement II is false: Volumes are NOT additive. $50\text{ mL}$ of water + $50\text{ mL}$ of ethanol $\neq 100\text{ mL}$ due to intermolecular packing.

**2.S9 → Answer: <br>
(D) A is false and R is false.** (Wait, actually both are false. Let me check the options. If both are false, standard A/R options sometimes don't cover it. I'll re-evaluate. The question says "Choose based on whether...". Ah, standard A/R usually has <br>
(D) as A is false but R is true. Wait, is R true?<br> No, density of water is only exactly $1\text{ g/mL}$ at $4^\circ\text{C}$. It changes with T. So both are false. If standard options don't have "Both false", I will formulate it as: A is false but R is false. Let's just say both are false in explanation.)
- A is false: Molality is per **kg** of solvent, not liter.
- R is false: Density of water changes with temperature (e.g., at $90^\circ\text{C}$ it's about $0.96\text{ g/mL}$).

**2.S10 → Statement I is False, Statement II is True.**
- Statement I is false: Mass percent is mass/mass. Since mass doesn't change with T, mass percent is constant.
- Statement II is true: Mass is conserved regardless of temperature.

**2.S11 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Let $m$ be the mass of each solution. Mass of solute 1 = $m \times w_1$, Mass of solute 2 = $m \times w_2$. Total solute = $m(w_1 + w_2)$. Total mass = $2m$. Final mass % = $[m(w_1 + w_2) / 2m] \times 100 = (w_1 + w_2) / 2$, which is the average.

**2.S12 → Statement I is True, Statement II is False.**
- Statement I is true: $500\text{ g}$ per million grams is the definition of $500\text{ ppm}$.
- Statement II is false: $\%\text{ w/w} = \text{ppm} / 10,000$. So $500\text{ ppm} = 0.05\%$, not $5\%$.

**2.S13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $N = M \times n_{factor}$. Since $n_{factor}$ (number of exchanged electrons, $H^+$, etc.) is at minimum 1, $N$ is always $\ge M$. It can never be less.

**2.S14 → Statement I is False, Statement II is True.**
- Statement I is false: You don't need the molar mass of the *solvent*, you need the molar mass of the *solute* to convert between M and m.
- Statement II is true: Density of the solution is the critical bridge connecting volume (Molarity) to mass (Molality).

**2.S15 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- In $1\text{ M}$ solution, 1 mole of NaCl is in $1000\text{ mL}$ of **solution**. Since NaCl takes up space and adds mass, the actual water present is less than $1000\text{ g}$.
- In $1\text{ m}$ solution, 1 mole of NaCl is in exactly $1000\text{ g}$ of water. 
- Wait! Let's re-read carefully. Concentration is ratio of solute to solvent. 
- $1\text{ M}$: 1 mole solute / (< 1000 g water). Ratio is > 1 mol / 1000 g water.
- $1\text{ m}$: 1 mole solute / 1000 g water.
- Therefore, $1\text{ M}$ has a HIGHER ratio of solute to solvent. So $1\text{ M}$ is MORE concentrated than $1\text{ m}$.
- Let me re-evaluate A: "A 1 m solution is more concentrated than a 1 M solution". This is FALSE. $1\text{ M}$ is more concentrated!
- R is true: $1\text{ M}$ does have less than $1000\text{ mL}$ (or $1000\text{ g}$) of solvent.
- Therefore, Answer is <br>
(D) A is false but R is true. (Psychological trap: I almost fell for it myself!).
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q2.M1 🟢**
You have $100\text{ g}$ of a $10\% (\text{w/w})$ $NaOH$ solution. How much water must you evaporate to make it a $20\% (\text{w/w})$ solution?<br>
<br>
(A) $10\text{ g}$
<br>
(B) $20\text{ g}$
<br>
(C)
 $50\text{ g}$
<br>
(D) $80\text{ g}$

**Q2.M2 🟡 (The "Flip" Trap)**
The mole fraction of a solute in an aqueous solution is $0.2$. What is the ratio of moles of solute to moles of solvent?<br>
<br>
(A) 1 : 5
<br>
(B) 1 : 4
<br>
(C)
 4 : 1
<br>
(D) 1 : 0.8

**Q2.M3 🔴**
A student measures out exactly $1\text{ L}$ of a $1\text{ M}$ aqueous $NaCl$ solution at $25^\circ\text{C}$. The solution is then cooled to $4^\circ\text{C}$, causing the water to contract. Which of the following is TRUE about the solution at $4^\circ\text{C}$?<br>
<br>
(A) Its molarity is exactly $1\text{ M}$.
<br>
(B) Its molarity is less than $1\text{ M}$.
<br>
(C)
 Its molarity is greater than $1\text{ M}$.
<br>
(D) Its molality has increased.

**Q2.M4 🟡**
To prepare a $0.5\text{ m}$ (molal) solution of glucose (Molar mass = 180), you should dissolve:
<br>
(A) $90\text{ g}$ of glucose in $1\text{ L}$ of solution.
<br>
(B) $90\text{ g}$ of glucose in $1\text{ kg}$ of solution.
<br>
(C)
 $90\text{ g}$ of glucose in $1\text{ kg}$ of water.
<br>
(D) $180\text{ g}$ of glucose in $500\text{ g}$ of water.

**Q2.M5 🟡 (The "Density Missing" Trap)**
A solution is prepared by mixing $20\text{ mL}$ of ethanol with $80\text{ mL}$ of water. Assuming the final volume is $100\text{ mL}$, what is the mass percent of ethanol?<br> (Density of ethanol = $0.789\text{ g/mL}$, Density of water = $1.0\text{ g/mL}$).
<br>
(A) $20\%$
<br>
(B) $16.5\%$
<br>
(C)
 $25\%$
<br>
(D) $19.7\%$

**Q2.M6 🔴**
An aqueous solution of urea has a mole fraction of urea equal to $0.1$. What is its molality?<br> (Molar mass of water = $18\text{ g/mol}$).
<br>
(A) $5.55\text{ m}$
<br>
(B) $6.17\text{ m}$
<br>
(C)
 $10\text{ m}$
<br>
(D) $11.1\text{ m}$

**Q2.M7 🟡**
Which of the following will change if you take a solution from Earth to the Moon?<br> (Assume closed container, constant temperature).
<br>
(A) Molarity
<br>
(B) Molality
<br>
(C)
 Mass percent
<br>
(D) None of the above

**Q2.M8 🟢**
A factory releases wastewater containing $0.05\text{ g}$ of lead per $1000\text{ kg}$ of water. What is the concentration of lead in ppm?<br>
<br>
(A) $50\text{ ppm}$
<br>
(B) $5\text{ ppm}$
<br>
(C)
 $0.05\text{ ppm}$
<br>
(D) $0.5\text{ ppm}$

**Q2.M9 🔴 (The "Math Blindness" Trap)**
You have $1\text{ L}$ of a $2\text{ M}$ solution of $HCl$. You add $1\text{ L}$ of water. You then take $500\text{ mL}$ of this new mixture. What is the molarity of the $500\text{ mL}$ sample?<br>
<br>
(A) $1\text{ M}$
<br>
(B) $0.5\text{ M}$
<br>
(C)
 $2\text{ M}$
<br>
(D) $0.25\text{ M}$

**Q2.M10 🟡**
A commercially available concentrated hydrochloric acid contains $38\% \text{HCl}$ by mass. What does this mean?<br>
<br>
(A) $38\text{ g}$ of HCl in $100\text{ mL}$ of water.
<br>
(B) $38\text{ g}$ of HCl in $100\text{ mL}$ of solution.
<br>
(C)
 $38\text{ g}$ of HCl in $100\text{ g}$ of solution.
<br>
(D) $38\text{ g}$ of HCl in $100\text{ g}$ of water.

**Q2.M11 🔴**
If $V_1\text{ mL}$ of a liquid A (density $d_1$) is mixed with $V_2\text{ mL}$ of liquid B (density $d_2$) to form a solution (assuming volumes are additive), the mass percent of liquid A is:
<br>
(A) $[V_1 / (V_1 + V_2)] \times 100$
<br>
(B) $[(V_1 d_1) / (V_1 d_1 + V_2 d_2)] \times 100$
<br>
(C)
 $[(V_1 d_2) / (V_2 d_1)] \times 100$
<br>
(D) $[d_1 / (d_1 + d_2)] \times 100$

**Q2.M12 🟡**
The concentration of $Ag^+$ ions in a saturated solution is $1.08 \times 10^{-5} \text{ g/L}$. Express this in ppm. (Density of solution $\approx 1\text{ g/mL}$)
<br>
(A) $1.08\text{ ppm}$
<br>
(B) $0.108\text{ ppm}$
<br>
(C)
 $0.0108\text{ ppm}$
<br>
(D) $10.8\text{ ppm}$

**Q2.M13 🟢**
Which term uses the exact same denominator as mole fraction?<br>
<br>
(A) Molality
<br>
(B) Molarity
<br>
(C)
 Mass percent
<br>
(D) None of the above

**Q2.M14 🔴 (The "Equal Mix" Trap)**
$100\text{ mL}$ of $0.2\text{ M}$ $H_2SO_4$ is mixed with $100\text{ mL}$ of $0.2\text{ M}$ $NaOH$. What is the molarity of the resulting $Na_2SO_4$ salt in the final solution?<br>
<br>
(A) $0.2\text{ M}$
<br>
(B) $0.1\text{ M}$
<br>
(C)
 $0.05\text{ M}$
<br>
(D) $0.4\text{ M}$

**Q2.M15 🟡**
For an extremely dilute aqueous solution, the numerical value of which two concentration terms will be almost perfectly identical?<br>
<br>
(A) Mole fraction and Mass percent
<br>
(B) Molarity and Molality
<br>
(C)
 ppm and Molality
<br>
(D) Mass percent and ppm

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q2.M1 → Answer: <br>
(C)
**
- Initial: $100\text{ g}$ solution, $10\% \text{w/w}$ $\rightarrow$ $10\text{ g}$ $NaOH$, $90\text{ g}$ water.
- We want a $20\% \text{w/w}$ solution. The mass of $NaOH$ ($10\text{ g}$) does NOT change.
- So, $10\text{ g}$ must be $20\%$ of the new total mass ($m_{new}$).
- $10 = 0.20 \times m_{new} \rightarrow m_{new} = 50\text{ g}$.
- We started with $100\text{ g}$ and ended with $50\text{ g}$. So we evaporated $100 - 50 = 50\text{ g}$ of water.
- Trap: Assuming you evaporate half the mass ($10\text{ g}$) to double the concentration.

**Q2.M2 → Answer: <br>
(B)**
- Mole fraction = $X_A = 0.2$. Therefore, mole fraction of solvent $X_B = 0.8$.
- Ratio = $n_A / n_B = X_A / X_B = 0.2 / 0.8 = 1/4 = 1 : 4$.
- Trap: <br>
(A) 1:5, assuming 0.2 means 1 out of 5 parts is solute and the solvent is the remaining 5 parts (it's remaining 4 parts).

**Q2.M3 → Answer: <br>
(C)
**
- Molarity = moles / Volume.
- Cooling from $25^\circ\text{C}$ to $4^\circ\text{C}$ causes water (and the solution) to contract (water has max density at $4^\circ\text{C}$). 
- Since volume decreases and moles remain constant, the fraction (moles/volume) INCREASES.
- So M > $1\text{ M}$. Molality does not change with temperature.
- Trap: Thinking Molarity decreases when volume decreases. It's inversely proportional!

**Q2.M4 → Answer: <br>
(C)
**
- Molality (m) = moles of solute / kg of **solvent**.
- $0.5\text{ m}$ means $0.5\text{ moles}$ of glucose per $1\text{ kg}$ of water.
- $0.5\text{ moles} = 0.5 \times 180 = 90\text{ g}$.
- So, $90\text{ g}$ in $1\text{ kg}$ of **water** (solvent).
- Trap: <br>
(A) and <br>
(B) use "solution". <br>
(D) calculates $1\text{ mol}$ per $0.5\text{ kg}$, which is $2\text{ m}$.

**Q2.M5 → Answer: <br>
(B)**
- Mass of ethanol = $20\text{ mL} \times 0.789\text{ g/mL} = 15.78\text{ g}$.
- Mass of water = $80\text{ mL} \times 1.0\text{ g/mL} = 80\text{ g}$.
- Total mass = $15.78 + 80 = 95.78\text{ g}$.
- Mass % = $(15.78 / 95.78) \times 100 = 16.47\% \approx 16.5\%$.
- Trap: <br>
(A) $20\%$ is volume percent (v/v%), not mass percent (w/w%).

**Q2.M6 → Answer: <br>
(B)**
- Let total moles = $1$. Then $n_{urea} = 0.1\text{ mol}$ and $n_{water} = 0.9\text{ mol}$.
- Mass of water (solvent) = $0.9\text{ mol} \times 18\text{ g/mol} = 16.2\text{ g} = 0.0162\text{ kg}$.
- Molality = $n_{urea} / \text{kg}_{water} = 0.1 / 0.0162 = 6.17\text{ m}$.
- Trap: Not knowing how to leverage mole fraction ratios to find mass of solvent.

**Q2.M7 → Answer: <br>
(D)**
- Molarity = mol / L. Mass, volume, and moles do not change with gravity.
- Molality = mol / kg. Mass doesn't change with gravity.
- Mass percent = mass / mass. No change.
- Gravity only affects weight, not mass, moles, or volume. So concentration terms are unaffected.

**Q2.M8 → Answer: <br>
(C)
**
- ppm = (mass of solute / mass of solution) $\times 10^6$.
- Mass of solute = $0.05\text{ g}$. Mass of solution $\approx 1000\text{ kg} = 1,000,000\text{ g} = 10^6\text{ g}$.
- ppm = $(0.05 / 10^6) \times 10^6 = 0.05\text{ ppm}$.
- Trap: Not matching units (g vs kg).

**Q2.M9 → Answer: <br>
(A)**
- Initial: $1\text{ L}$ of $2\text{ M} \rightarrow$ $2\text{ moles}$ of HCl.
- Add $1\text{ L}$ water $\rightarrow$ Total volume = $2\text{ L}$.
- New Molarity = $2\text{ moles} / 2\text{ L} = 1\text{ M}$.
- Taking a $500\text{ mL}$ sample does NOT change the concentration of that sample. It remains $1\text{ M}$.
- Trap: <br>
(B) Halving it again because they took half a litre. Concentration is an intensive property!

**Q2.M10 → Answer: <br>
(C)
**
- Definition of mass percent (w/w%): grams of solute per $100\text{ g}$ of **solution**.
- Therefore, $38\text{ g}$ of HCl in $100\text{ g}$ of solution.
- Trap: <br>
(D) $100\text{ g}$ of water. If it were $100\text{ g}$ of water, total mass would be $138\text{ g}$, so it wouldn't be $38\%$.

**Q2.M11 → Answer: <br>
(B)**
- Mass of A = $V_1 \times d_1$. Mass of B = $V_2 \times d_2$.
- Total mass = $V_1 d_1 + V_2 d_2$.
- Mass % A = (Mass of A / Total Mass) $\times 100 = [(V_1 d_1) / (V_1 d_1 + V_2 d_2)] \times 100$.

**Q2.M12 → Answer: <br>
(C)
**
- $1.08 \times 10^{-5}\text{ g/L}$ means $1.08 \times 10^{-5}\text{ g}$ in $1\text{ L}$ of solution.
- Since density $\approx 1\text{ g/mL}$, $1\text{ L} = 1000\text{ g}$.
- ppm = (g solute / g solution) $\times 10^6 = (1.08 \times 10^{-5} / 1000) \times 10^6 = 1.08 \times 10^{-5} \times 10^3 = 0.0108\text{ ppm}$.

**Q2.M13 → Answer: <br>
(D)**
- Mole fraction denominator is **Total Moles**.
- Molality denominator is kg solvent.
- Molarity denominator is L solution.
- Mass percent denominator is Total Mass.
- None match.

**Q2.M14 → Answer: <br>
(C)
**
- $H_2SO_4 + 2NaOH \rightarrow Na_2SO_4 + 2H_2O$.
- Moles $H_2SO_4 = 0.1\text{ L} \times 0.2\text{ M} = 0.02\text{ mol}$.
- Moles $NaOH = 0.1\text{ L} \times 0.2\text{ M} = 0.02\text{ mol}$.
- To fully react $0.02\text{ mol}$ $H_2SO_4$, we need $0.04\text{ mol}$ $NaOH$. But we only have $0.02\text{ mol}$ $NaOH$.
- So $NaOH$ is the limiting reagent!
- $2\text{ mol}$ $NaOH$ produce $1\text{ mol}$ $Na_2SO_4$.
- So $0.02\text{ mol}$ $NaOH$ produce $0.01\text{ mol}$ $Na_2SO_4$.
- Final volume = $100 + 100 = 200\text{ mL} = 0.2\text{ L}$.
- Molarity of $Na_2SO_4$ = $0.01\text{ mol} / 0.2\text{ L} = 0.05\text{ M}$.
- Trap: Assuming 1:1 reaction or just taking the average molarity.

**Q2.M15 → Answer: <br>
(B)**
- For extremely dilute aqueous solutions, the mass of solute is negligible compared to the water.
- $1\text{ L}$ of solution weighs approx $1\text{ kg}$.
- Molarity = moles / $1\text{ L}$ solution.
- Molality = moles / $1\text{ kg}$ solvent.
- Since $1\text{ L}$ solution $\approx 1\text{ kg}$ solvent, Molarity $\approx$ Molality.

</details>

---

*Next: [Chapter 3 — Molarity & Molality: The Power Duo →](./03_molarity_and_molality.md)*
