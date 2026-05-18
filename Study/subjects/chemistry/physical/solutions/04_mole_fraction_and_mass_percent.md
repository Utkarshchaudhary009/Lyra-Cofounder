# Chapter 4: Mole Fraction, Mass Percent & ppm
## Part II — Concentration Mastery

---

## 🎯 Stage 1: The Core Idea

### Three Ways to Count Without Volume

Molarity needs a volumetric flask. But mole fraction, mass percent, and ppm need only a balance — and the truth is, they often tell you more.

**Mole Fraction (χ):** Of all the molecules in this solution, what fraction are molecule A?<br>

**Mass Percent (w/w%):** Of every 100 grams of this solution, how many grams are solute?<br>

**ppm:** Same idea as mass percent, but for incredibly dilute amounts — used when concentration is in the range of micrograms per gram.

All three are **temperature-independent** (mass-based, not volume-based) and all three appear in Raoult's Law, Henry's Law, and colligative property problems.

---

## 🔬 Stage 2: The Formula Lab

### Mole Fraction

For a **binary** solution (A = solute, B = solvent):

```
         n_A                        n_B
χ_A = ─────────       χ_B = ─────────────
       n_A + n_B               n_A + n_B

Golden Rule: χ_A + χ_B = 1 (always, for binary)
```

For a **ternary** solution (A, B, C):

```
χ_A = n_A / (n_A + n_B + n_C)
χ_A + χ_B + χ_C = 1
```

### Mass Percent (w/w%)

```
           W_solute
w/w% = ─────────────── × 100
           W_solution

W_solution = W_solute + W_solvent
```

### ppm (Parts Per Million)

```
           W_solute (g)
ppm = ─────────────────── × 10⁶
          W_solution (g)

Quick conversion:
ppm = w/w% × 10,000
w/w% = ppm / 10,000
```

### Connecting Mole Fraction to Molality

```
         χ_solute × 1000
m = ──────────────────────────
      χ_solvent × M_solvent
```

where M_solvent = molar mass of solvent in g/mol.

For **aqueous solutions** (M_water = 18):

```
         χ_solute × 1000
m = ─────────────────────────
            18 × χ_water
```

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Calculating Mole Fraction — Basic

**Pattern:** Given masses of solute and solvent → find χ of each component.

#### Solved Example 4.1
**Q:** 18 g of glucose (MM = 180) dissolved in 90 g of water. Find χ_glucose and χ_water. 🟢

```
n_glucose = 18/180 = 0.1 mol
n_water   = 90/18  = 5.0 mol
Total      = 5.1 mol

χ_glucose = 0.1/5.1 = 0.0196
χ_water   = 5.0/5.1 = 0.9804

Check: 0.0196 + 0.9804 = 1.000 ✓
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 4.1a | 46 g ethanol (MM = 46) + 54 g water. Find χ_ethanol. | 🟢 |
| 4.1b | 8 g NaOH (MM = 40) + 18 g water. Find χ_NaOH. | 🟢 |
| 4.1c | 180 g glucose + 180 g water. Find both mole fractions. | 🟡 |
| 4.1d | 2 mol A and 3 mol B. Find χ_A and χ_B. | 🟢 |
| 4.1e | If χ_solute = 0.025 in aqueous solution, find χ_water. | 🟢 |
| DPP 2.4 | 5.85 g of NaCl are dissolved in 90 g of water. The mole fraction of NaCl is: <br>
(A) 0.1 <br>
(B) 0.01 <br>
(C)
 0.2 <br>
(D) 0.0196 | 🟢 |
| DPP 3.4 | The density of a 56.0% by mass aqueous solution of 1-propanol (CH₃CH₂CH₂OH) is 0.8975 g/cm³. What is the mole fraction of the 1-propanol?<br> <br>
(A) 0.292 <br>
(B) 0.227 <br>
(C)
 0.241 <br>
(D) 0.276 | 🟡 |
| DPP 4.1 | Calculate the mole percentage of CH₃OH and H₂O respectively in 60% (by mass) aqueous solution of CH₃OH. <br>
(A) 45.8, 54.2 <br>
(B) 54.2, 45.8 <br>
(C)
 50,50 <br>
(D) 60,40 | 🟢 |
| DPP 5.4 | If ratio of mole fraction of solute to solvent is unity, what would be by wt. concentration of solute (M solute = molecular mass of solute, M solvent = molecular mass of solvent): <br>
(A) M solute × 100 / (M solute + M solvent) <br>
(B) 50% <br>
(C)
 66.67% <br>
(D) M solute × 100 / M solvent | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**4.1a:** n_eth = 46/46 = 1 mol; n_H₂O = 54/18 = 3 mol; **χ_eth = 1/4 = 0.25**

**4.1b:** n_NaOH = 8/40 = 0.2 mol; n_H₂O = 18/18 = 1 mol; **χ_NaOH = 0.2/1.2 = 0.167**

**4.1c:** n_glucose = 180/180 = 1 mol; n_H₂O = 180/18 = 10 mol
- **χ_glucose = 1/11 = 0.0909; χ_water = 10/11 = 0.9091**

**4.1d:** Total = 5 mol; **χ_A = 2/5 = 0.4; χ_B = 3/5 = 0.6**

**4.1e:** χ_water = 1 − 0.025 = **0.975**

**DPP 2.4:** n_NaCl = 5.85/58.5 = 0.1 mol; n_H₂O = 90/18 = 5 mol; Total = 5.1 mol. χ_NaCl = 0.1 / 5.1 = **0.0196 → Answer: <br>
(D)**

**DPP 3.4:** 1-propanol MM = 60. Per 100 g solution: 56 g propanol, 44 g water. n_prop = 56/60 = 0.9333 mol; n_H₂O = 44/18 = 2.444 mol. Total = 3.3777 mol. χ_prop = 0.9333 / 3.3777 = **0.2763 ≈ 0.276 → Answer: <br>
(D)**

**DPP 4.1:** Per 100 g solution: 60 g CH₃OH, 40 g water. n_CH₃OH = 60/32 = 1.875 mol; n_H₂O = 40/18 = 2.222 mol. Total = 4.097 mol. χ_CH₃OH = 1.875 / 4.097 = 0.4576 = **45.8%**; mole% water = **54.2% → Answer: <br>
(A)**

**DPP 5.4:** χ_solute / χ_solvent = 1 → n_solute = n_solvent. Let n_solute = n_solvent = 1 mol. Mass of solute = M solute; mass of solvent = M solvent. w/w% = M solute × 100 / (M solute + M solvent) → **Answer: <br>
(A)**
</details>

---

### Type 2: Calculating Mass Percent

**Pattern:** Given masses → find w/w%. Remember: denominator is solution, not solvent.

#### Solved Example 4.2
**Q:** 15 g of KNO₃ dissolved in 85 g of water. Find w/w%. 🟢

```
W_solution = 15 + 85 = 100 g
w/w% = (15/100) × 100 = 15%
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 4.2a | 20 g NaCl + 180 g water. Find w/w% NaCl. | 🟢 |
| 4.2b | A solution is 25% glucose. If solution mass = 400 g, find mass of glucose. | 🟢 |
| 4.2c | 5 g solute in 95 g solvent. Find w/w%. | 🟢 |
| 4.2d | A solution contains 36% HCl. Find mass of solvent in 200 g of solution. | 🟡 |
| 4.2e | 8 g urea (MM = 60) in 200 g water. Find w/w%. | 🟢 |
| DPP 4.3 | What is the meaning of 10% solution of NaCl?<br> <br>
(A) 10 g NaCl in 100 gram of solution <br>
(B) 58.5 grams of NaCl in 100 grams of solution <br>
(C)
 94 grams of NaCl in 100 grams of solution <br>
(D) 5.85 grams of H₂O in 100 grams of solution | 🟢 |

<details>
<summary>💡 Solutions for Type 2</summary>

**4.2a:** W_soln = 20+180 = 200 g; **w/w% = (20/200)×100 = 10%**

**4.2b:** W_glucose = 25%×400 = **(25/100)×400 = 100 g**

**4.2c:** W_soln = 5+95 = 100 g; **w/w% = 5%**

**4.2d:** HCl = 36% → Water = 64%; W_water = 0.64×200 = **128 g**

**4.2e:** W_soln = 8+200 = 208 g; **w/w% = (8/208)×100 = 3.85%**

**DPP 4.3:** A 10% w/w solution means 10 parts by mass of solute are present in 100 parts by mass of the final solution. Thus, 10 g NaCl in 100 g of solution → **Answer: <br>
(A)**
</details>

---

### Type 3: Calculating ppm

**Pattern:** Trace-level concentration → use ppm. Often environmental questions.

#### Solved Example 4.3
**Q:** 0.002 g of fluoride ion is present per kg of drinking water. Express in ppm. 🟢

```
ppm = (W_solute / W_solution) × 10⁶
    = (0.002 / 1000) × 10⁶    [W_soln ≈ W_solvent for dilute solution]
    = 2 × 10⁻⁶ × 10⁶
    = 2 ppm
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 4.3a | 5 mg of Pb²⁺ in 1 kg water. Find concentration in ppm. | 🟢 |
| 4.3b | A solution is 0.005% w/w arsenic. Convert to ppm. | 🟢 |
| 4.3c | 2.5 ppm chlorine in water. Express as w/w%. | 🟢 |
| 4.3d | 0.05 g of CO₂ dissolved in 1 L water (d = 1 g/mL). Find ppm CO₂. | 🟡 |
| 4.3e | WHO limit for lead in water is 10 ppb. Express this in ppm and in w/w%. | 🟡 |
| DPP 5.1 | How much Ca(NO₃)₂, in mg, must be present in 50ml(d = 1 g/mL) of a solution with 2.35ppm of Ca?<br> <br>
(A) 0.1175 <br>
(B) 770.8 <br>
(C)
 4.7 <br>
(D) 0.48 | 🔴 |

<details>
<summary>💡 Solutions for Type 3</summary>

**4.3a:** 5 mg = 0.005 g; ppm = (0.005/1000)×10⁶ = **5 ppm**

**4.3b:** w/w% = 0.005%; ppm = 0.005 × 10,000 = **50 ppm**

**4.3c:** w/w% = 2.5/10,000 = **0.00025%**

**4.3d:** W_soln = 1000 mL × 1 g/mL = 1000 g; ppm = (0.05/1000)×10⁶ = **50 ppm**

**4.3e:** 10 ppb = 10 parts per billion = 10/1000 ppm = **0.01 ppm**; w/w% = 0.01/10,000 = **1×10⁻⁶%**

**DPP 5.1:** Mass of 50 mL solution = 50 g. ppm of Ca = 2.35 → W_Ca = (2.35 × 50) / 10⁶ g = 117.5 × 10⁻⁶ g = 0.1175 mg Ca.
Molar mass of Ca(NO₃)₂ = 40 + 2×14 + 6×16 = 164 g/mol. Since 40 mg Ca is present in 164 mg Ca(NO₃)₂, 0.1175 mg Ca is present in (164/40) × 0.1175 mg = **0.48175 mg ≈ 0.48 mg → Answer: <br>
(D)**
</details>

---

### Type 4: Converting Between Mole Fraction and Molality

**Pattern:** χ ↔ m interconversion — appears in JEE and Board.

#### Solved Example 4.4
**Q:** The mole fraction of glucose in an aqueous solution is 0.01. Find molality. 🟡

```
χ_glucose = 0.01 → χ_water = 0.99

Formula: m = (χ_solute × 1000) / (χ_solvent × M_solvent)
         m = (0.01 × 1000) / (0.99 × 18)
         m = 10 / 17.82
         m = 0.561 m
```

#### Solved Example 4.5
**Q:** A 2 molal aqueous glucose solution. Find χ_glucose. 🟡

```
2 molal = 2 mol glucose in 1000 g water
n_glucose = 2 mol
n_water = 1000/18 = 55.56 mol

χ_glucose = 2/(2 + 55.56) = 2/57.56 = 0.03474
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 4.4a | χ_ethanol = 0.04 in aqueous solution. Find molality. | 🟡 |
| 4.4b | 1 molal NaCl solution (ignore dissociation). Find χ_NaCl. | 🟡 |
| 4.4c | χ_solute = 0.1 in aqueous solution. Find molality. ⭐ | 🟡 |
| DPP 1.6 | A 5.2 molal aqueous solution of methyl alcohol, CH₃OH, is supplied. What is the mole fraction of methyl alcohol in the solution?<br> <br>
(A) 1.100 <br>
(B) 0.190 <br>
(C)
 0.086 <br>
(D) 0.050 | 🟡 |
| DPP 2.6 | Mole fraction of solvent in aqueous solution of NaOH having molality of 3 is: <br>
(A) 0.3 <br>
(B) 0.05 <br>
(C)
 0.7 <br>
(D) 0.95 | 🟡 |
| DPP 2.7 | Mole fraction of A in H₂O is 0.2. The molality of A in H₂O is: <br>
(A) 13.9 <br>
(B) 15.5 <br>
(C)
 14.5 <br>
(D) 16.8 | 🟡 |

<details>
<summary>💡 Solutions for Type 4</summary>

**4.4a:** m = (0.04×1000)/(0.96×18) = 40/17.28 = **2.315 m**

**4.4b:** n_NaCl = 1 mol; n_H₂O = 1000/18 = 55.56 mol
χ_NaCl = 1/(1+55.56) = 1/56.56 = **0.01768**

**4.4c:** χ_solute = 0.1 → χ_water = 0.9
m = (0.1×1000)/(0.9×18) = 100/16.2 = **6.17 m**

**DPP 1.6:** n_solute = 5.2 mol per 1000 g water. n_H₂O = 55.56 mol. χ_CH₃OH = 5.2 / (5.2 + 55.56) = 5.2 / 60.76 = **0.08558 ≈ 0.086 → Answer: <br>
(C)
**

**DPP 2.6:** m = 3 molal → n_NaOH = 3 mol; n_H₂O = 55.56 mol. Total = 58.56 mol. χ_solvent = 55.56 / 58.56 = **0.9487 ≈ 0.95 → Answer: <br>
(D)**

**DPP 2.7:** χ_A = 0.2 → χ_water = 0.8. m = (χ_A × 1000) / (χ_water × 18) = (0.2 × 1000) / (0.8 × 18) = 200 / 14.4 = **13.88 m ≈ 13.9 m → Answer: <br>
(A)**
</details>

---

### Type 5: Mole Fraction in Raoult's/Henry's Law Context

**Pattern:** Vapour pressure or gas solubility problem — extract the mole fraction from context.

#### Solved Example 4.6
**Q:** The RLVP of a solution is 0.2. What is the mole fraction of the solute?<br> 🟢

```
RLVP = (P° - P_s)/P° = χ_solute

∴ χ_solute = 0.2
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 4.5a | P° of solvent = 100 torr. Solution VP = 80 torr. Find χ_solute. | 🟢 |
| 4.5b | χ_O₂ in water = 1.97×10⁻⁵ at P_O₂ = 0.920 bar. Find K_H for O₂. | 🟡 |
| 4.5c | RLVP = 0.015. Find mole fraction of solvent. ⭐ | 🟢 |

<details>
<summary>💡 Solutions for Type 5</summary>

**4.5a:** RLVP = (100-80)/100 = 0.2 = χ_solute; **χ_solute = 0.2**

**4.5b:** K_H = P_O₂/χ_O₂ = 0.920/(1.97×10⁻⁵) = **46,700 bar ≈ 46.7 kbar**

**4.5c:** χ_solute = 0.015; **χ_solvent = 1 - 0.015 = 0.985**
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 4.M1 | 5 g urea (MM = 60) in 90 g water. Find: (a) χ_urea, (b) w/w%, (c) molality, (d) RLVP if P°_water = 20 torr. ⭐ | T1+T2+T5 | 🔴 |
| 4.M2 | A solution has w/w% = 10% (MM of solute = 100, solvent = water). Find molality and mole fraction. | T2+T4 | 🟡 |
| 4.M3 | If χ_solute = 0.0125 and RLVP = 0.0125, find molality of the aqueous solution. | T4+T5 | 🟡 |
| DPP 4.4 | 300gm of 25%w/w solution of solute A is mixed with 400gm of 40%w/w solution of another solute B. What is the w/w percentage of the new mixture?<br> <br>
(A) 33.57% <br>
(B) 35% <br>
(C)
 25% <br>
(D) 40% | Mixing | 🟡 |
| DPP 4.6 | 60 g of solution containing 40% by mass of NaCl are mixed with 100 g of a solution containing 15% by mass NaCl. Determine the mass percent of sodium chloride in the final solution. <br>
(A) 24.4% <br>
(B) 78% <br>
(C)
 48.8% <br>
(D) 19.68% | Mixing | 🟡 |
| DPP 5.3 | 30ml, 50%(v/v)HCl added into 70ml, 20%(v/v) HCl solution. Find % of resultant solution: <br>
(A) 14 <br>
(B) 29 <br>
(C)
 15 <br>
(D) 70 | Mixing | 🟡 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**4.M1:**
- n_urea = 5/60 = 0.0833 mol; n_H₂O = 90/18 = 5 mol
- **(a) χ_urea = 0.0833/5.0833 = 0.01639**
- **(b) w/w% = 5/95 × 100 = 5.26%** *(W_soln = 95 g)*
- **(c) m = 0.0833/0.09 = 0.926 m**
- **(d) RLVP = χ_urea = 0.01639; P_s = P°(1-χ) = 20×(1-0.01639) = 19.67 torr; lowering = 0.33 torr**

**4.M2:**
- Per 100 g solution: 10 g solute, 90 g water
- n_solute = 10/100 = 0.1 mol; n_H₂O = 90/18 = 5 mol
- **m = 0.1/0.090 = 1.11 m**
- **χ_solute = 0.1/(0.1+5) = 0.1/5.1 = 0.0196**

**4.M3:**
- χ_solute = 0.0125; χ_water = 0.9875
- m = (0.0125×1000)/(0.9875×18) = 12.5/17.775 = **0.703 m**

**DPP 4.4:**
- Total solute mass = (0.25 × 300) + (0.40 × 400) = 75 + 160 = 235 g. Total solution mass = 300 + 400 = 700 g.
- w/w% = (235 / 700) × 100 = **33.57% → Answer: <br>
(A)**

**DPP 4.6:**
- Total NaCl mass = (0.40 × 60) + (0.15 × 100) = 24 + 15 = 39 g. Total solution mass = 60 + 100 = 160 g.
- w/w% = (39 / 160) × 100 = **24.375% ≈ 24.4% → Answer: <br>
(A)**

**DPP 5.3:**
- Total pure HCl volume = (0.50 × 30) + (0.20 × 70) = 15 + 14 = 29 mL. Total solution volume = 30 + 70 = 100 mL.
- %(v/v) = (29 / 100) × 100 = **29% → Answer: <br>
(B)**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 4.B1 | Calculate mole fraction of benzene in a solution containing 30 g benzene (MM = 78) and 120 g toluene (MM = 92). | 🟢 |
| 4.B2 | The mole fraction of acetone in its mixture with chloroform is 0.30. Find mole fraction of chloroform. | 🟢 |
| 4.B3 | Concentration of O₂ dissolved in water is 8 mg/L at 25°C. Express in ppm (density of water = 1 g/mL). | 🟡 |
| 4.B4 | Calculate mass% of ethanol in a mixture of 46 g ethanol and 108 g water. *(NCERT pattern)* | 🟢 |
| 4.B5 | The mass % of H₂SO₄ is 98%. Find its mole fraction in concentrated H₂SO₄ (per 100 g: 98 g H₂SO₄, 2 g water). ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**4.B1:** n_benzene = 30/78 = 0.385 mol; n_toluene = 120/92 = 1.304 mol
χ_benzene = 0.385/1.689 = **0.228**

**4.B2:** χ_chloroform = 1 − 0.30 = **0.70**

**4.B3:** 8 mg/L = 8 mg/1000 g = 0.008 g/1000 g; ppm = (0.008/1000)×10⁶ = **8 ppm**

**4.B4:** W_soln = 46+108 = 154 g; **w/w% = (46/154)×100 = 29.87% ≈ 30%**

**4.B5:** n_H₂SO₄ = 98/98 = 1 mol; n_H₂O = 2/18 = 0.111 mol
**χ_H₂SO₄ = 1/1.111 = 0.900**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q4.J1 🟡 ⭐**
Relative lowering of vapour pressure of a dilute solution is 0.2. The mole fraction of non-volatile solute is:
<br>
(A) 0.8  <br>
(B) 0.2  <br>
(C)
 0.02  <br>
(D) Cannot determine

**Q4.J2 🟡**
1 molal aqueous NaCl solution (ignore dissociation). Mole fraction of NaCl is approximately:
<br>
(A) 0.018  <br>
(B) 0.0176  <br>
(C)
 0.05  <br>
(D) 0.0278

**Q4.J3 🔴 ⭐**
1 g of an unknown solute dissolved in 100 g water gives a solution with χ_solute = 9.0 × 10⁻³. Molar mass of the solute is:
<br>
(A) 100 g/mol  <br>
(B) 200 g/mol  <br>
(C)
 50 g/mol  <br>
(D) 62 g/mol

**Q4.J4 🔴**
20% (w/w) glucose solution (MM = 180). Its molality is:
<br>
(A) 1.39 m  <br>
(B) 2.5 m  <br>
(C)
 0.5 m  <br>
(D) 1.25 m

**Q4.J5 🔴 ⭐**
An aqueous solution has χ_solute = 0.1. Its molality (MW of solvent = 18) is:
<br>
(A) 5.56 m  <br>
(B) 6.17 m  <br>
(C)
 0.1 m  <br>
(D) 1 m

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**4.J1 → Answer: <br>
(B)**
- RLVP = (P°−P_s)/P° = χ_solute by Raoult's Law
- **χ_solute = 0.2 ✓**

**4.J2 → Answer: <br>
(B)**
- 1 molal = 1 mol NaCl per 1000 g water
- n_NaCl = 1; n_H₂O = 1000/18 = 55.56
- **χ_NaCl = 1/56.56 = 0.01768 ≈ 0.0176 ✓**

**4.J3 → Answer: <br>
(A)**
- n_H₂O = 100/18 = 5.556 mol
- χ_solute = n_s/(n_s + 5.556) = 9×10⁻³
- n_s(1 − 9×10⁻³) = 9×10⁻³ × 5.556
- n_s × 0.991 = 0.05; n_s = 0.05/0.991 = 0.01 mol
- **MM = 1/0.01 = 100 g/mol ✓**

**4.J4 → Answer: <br>
(A)**
- Per 100 g solution: 20 g glucose, 80 g water
- n_glucose = 20/180 = 0.1111 mol; W_water = 80 g = 0.08 kg
- **m = 0.1111/0.08 = 1.39 m ✓**

**4.J5 → Answer: <br>
(B)**
- χ_solute = 0.1; χ_solvent = 0.9
- m = (χ_solute × 1000)/(χ_solvent × 18) = (0.1×1000)/(0.9×18) = 100/16.2 = **6.17 m ✓**
</details>

---

## Key Takeaways from Chapter 4

| Rule | Detail |
|------|--------|
| χ_A + χ_B = 1 | Always (binary solution) |
| RLVP = χ_solute | Direct from Raoult's Law |
| ppm = w/w% × 10,000 | Quick conversion |
| m from χ | `m = (χ_s × 1000) / (χ_solvent × M_solvent)` |
| χ from m (water) | `χ_s = m/(m + 55.56)` |

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
| 4.S1 | **Assertion <br>
(A):** Mole fraction of a component in a solution is always less than 1.<br>**Reason (R):** A solution must contain at least two components, meaning the moles of one component are strictly less than the total moles. | 🟢 |
| 4.S2 | **Statement I:** Both mole fraction and mass percent of a solution change with a change in temperature.<br>**Statement II:** Volume of a solution changes with temperature, but mass and moles do not. | 🟢 |
| 4.S3 | **Assertion <br>
(A):** If the mole fraction of a solute is $0.1$ and the solvent is water, the mole ratio of solute to solvent is $1:9$.<br>**Reason (R):** The sum of mole fractions of all components in a binary mixture is exactly $1$. | 🟡 |
| 4.S4 | **Statement I:** $10\text{ ppm}$ of $F^-$ in water means there are $10\text{ mg}$ of $F^-$ in $1\text{ kg}$ of the solution.<br>**Statement II:** $\text{ppm}$ is the ratio of the mass of the solute to the mass of the solvent, multiplied by $10^6$. | 🟡 |
| 4.S5 | **Assertion <br>
(A):** The molality of an aqueous solution whose solute mole fraction is $0.5$ is $55.55\text{ m}$.<br>**Reason (R):** If $\chi_{solute} = 0.5$, then $\chi_{water} = 0.5$. This implies the solution contains $1\text{ mole}$ of solute for every $1\text{ mole}$ of water, which is $18\text{ g}$. Molality is moles of solute per $1000\text{ g}$ of water. | 🔴 |
| 4.S6 | **Statement I:** A $10\% (\text{w/w})$ aqueous solution of glucose contains $10\text{ g}$ of glucose dissolved in $100\text{ g}$ of water.<br>**Statement II:** Mass percent is calculated as the mass of the solute divided by the total mass of the solution. | 🟢 |
| 4.S7 | **Assertion <br>
(A):** The mole fraction of water in a mixture of $18\text{ g}$ water and $46\text{ g}$ ethanol is $0.5$.<br>**Reason (R):** The mixture contains equal masses of water and ethanol, but their molar masses are different. | 🟡 |
| 4.S8 | **Statement I:** To convert mole fraction of a solute to its mass percent, one must know the molar masses of both the solute and the solvent.<br>**Statement II:** Mole fraction does not depend on the molar masses of the components, but mass percent does. | 🔴 |
| 4.S9 | **Assertion <br>
(A):** If two different solutes, A and B, have the same mass percent in water, they must have the same mole fraction.<br>**Reason (R):** Mole fraction depends directly on the number of moles, which in turn depends on the molar mass of the solute. | 🟡 |
| 4.S10 | **Statement I:** A concentration of $1\text{ ppm}$ is equivalent to $1\text{ mg}$ of solute per litre of an aqueous solution, provided the density of the solution is exactly $1\text{ g/mL}$.<br>**Statement II:** In highly dilute aqueous solutions, the mass of the solution is approximately equal to the volume of the solution in mL. | 🟢 |
| 4.S11 | **Assertion <br>
(A):** Mixing $100\text{ g}$ of a $10\% (\text{w/w})$ solution with $100\text{ g}$ of a $20\% (\text{w/w})$ solution results in a $15\% (\text{w/w})$ solution.<br>**Reason (R):** When equal masses of solutions are mixed, the resulting mass percent is the arithmetic mean of their initial mass percents. | 🟡 |
| 4.S12 | **Statement I:** The sum of mass percentages of all components in a solution is always $100$.<br>**Statement II:** The sum of mole fractions of all components in a solution is always $100$. | 🟢 |
| 4.S13 | **Assertion <br>
(A):** If the mole fraction of a gas dissolved in water increases, its molality also increases.<br>**Reason (R):** Molality and mole fraction are directly proportional to each other for all concentration ranges. | 🔴 |
| 4.S14 | **Statement I:** For a very dilute aqueous solution, molality and molarity are nearly identical.<br>**Statement II:** In a very dilute aqueous solution, $1\text{ kg}$ of solvent has almost the same volume as $1\text{ L}$ of solution. | 🟡 |
| 4.S15 | **Assertion <br>
(A):** A $20\text{ ppm}$ solution of $CaCO_3$ contains $20\text{ g}$ of $CaCO_3$ in $10^6\text{ g}$ of solvent.<br>**Reason (R):** Parts per million is defined strictly with respect to the mass of the solvent, not the solution. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**4.S1 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- By definition, $\chi_A + \chi_B = 1$. Since $n_A, n_B > 0$, both $\chi_A$ and $\chi_B$ must be $< 1$.

**4.S2 → Statement I is False, Statement II is True.**
- Statement I is false: Neither mole fraction nor mass percent depends on volume. Both are temperature-INDEPENDENT.
- Statement II is true: Volume changes with temperature due to expansion/contraction.

**4.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $\chi_{solute} = 0.1 \rightarrow \chi_{water} = 0.9$. The ratio is $0.1 : 0.9 = 1 : 9$.

**4.S4 → Statement I is True, Statement II is False.**
- Statement I is true: $10\text{ mg}$ in $1\text{ kg} = (10 \times 10^{-3}\text{ g}) / 1000\text{ g} = 10 \times 10^{-6} = 10\text{ ppm}$.
- Statement II is false: ppm is mass of solute to mass of **solution**, not solvent (though for very dilute solutions they are nearly the same, the *definition* uses solution).

**4.S5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- If $\chi_s = 0.5$, then $n_s = n_w$. Let's say $1\text{ mole}$ of each.
- Mass of solvent (water) $= 18\text{ g} = 0.018\text{ kg}$.
- Molality $= \text{moles of solute} / \text{kg of solvent} = 1 / 0.018 = 55.55\text{ m}$.

**4.S6 → Statement I is False, Statement II is True.**
- Statement I is false: It contains $10\text{ g}$ glucose in $90\text{ g}$ of water (to make $100\text{ g}$ of *solution*).
- Statement II is true: This is the definition.

**4.S7 → Answer: <br>
(C)
 A is true but R is false.**
- A is true: $18\text{ g}$ water $= 1\text{ mol}$. $46\text{ g}$ ethanol $= 1\text{ mol}$. Total $= 2\text{ mol}$. $\chi_{water} = 1/2 = 0.5$.
- R is false: The masses are NOT equal ($18\text{ g}$ vs $46\text{ g}$).

**4.S8 → Statement I is True, Statement II is False.**
- Statement I is true: To go from moles to masses, you need the molar masses of both.
- Statement II is false: Mole fraction *does* depend on molar masses if you are starting from a mass ratio. The statement as written is tricky: "Mole fraction does not depend on the molar masses" implies the formula $\chi = n_A/(n_A+n_B)$ doesn't contain $M$, but to *calculate* it from physical quantities, you need $M$. Let's evaluate exactly. "Mole fraction does not depend on the molar masses of the components, but mass percent does." Actually, mass percent is purely mass-based ($w_1/w_{total}$), so it DOES NOT need molar masses! Mole fraction NEEDS molar masses to convert mass to moles. So Statement II is entirely backwards. False.

**4.S9 → Answer: <br>
(D) A is false but R is true.**
- A is false: If they have the same mass percent, they have the same mass. But if their molar masses differ, their moles will differ, so their mole fractions will differ.
- R is true: This is exactly why A is false.

**4.S10 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $1\text{ mg/L}$. If density $= 1\text{ g/mL}$, $1\text{ L} = 1000\text{ g}$. $1\text{ mg} = 10^{-3}\text{ g}$. Ratio $= 10^{-3} / 1000 = 10^{-6} = 1\text{ ppm}$.

**4.S11 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $10\text{ g}$ solute from first $+ 20\text{ g}$ solute from second $= 30\text{ g}$ total solute. Total mass $= 200\text{ g}$.
- $w/w\% = (30/200) \times 100 = 15\%$. When masses are equal, you can average them.

**4.S12 → Statement I is True, Statement II is False.**
- Statement II is false: Sum of mole fractions is $1$, not $100$ (unless it specifically said "mole percentage").

**4.S13 → Answer: <br>
(C)
 A is true but R is false.**
- A is true: Both measure concentration. If one goes up, the other goes up.
- R is false: They are NOT directly proportional. $m = (1000 \chi_s) / (\chi_w M_w)$. Because $\chi_w = 1 - \chi_s$, the denominator changes. The relationship is non-linear.

**4.S14 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- For very dilute aqueous solutions, $d \approx 1\text{ g/mL}$, and mass of solute is negligible. Thus $1\text{ L}$ solution $\approx 1\text{ kg}$ solution $\approx 1\text{ kg}$ solvent. So $M \approx m$.

**4.S15 → Answer: <br>
(C)
 A is false and R is false. (Both False)**
- A is false: $10^6\text{ g}$ of *solution*, not solvent.
- R is false: ppm uses the mass of the solution in the denominator.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q4.M1 🟢**
A solution is prepared by mixing $2\text{ moles}$ of $A$ and $3\text{ moles}$ of $B$. What is the mole fraction of $A$ in the solution?<br>
<br>
(A) $0.4$
<br>
(B) $0.6$
<br>
(C)
 $0.66$
<br>
(D) $1.5$

**Q4.M2 🟡 (The "Missing Molar Mass" Trap)**
An aqueous solution contains $20\%$ by mass of a solute. To find its mole fraction, what additional information is MUST be provided?<br>
<br>
(A) Density of the solution
<br>
(B) Molar mass of the solute
<br>
(C)
 Temperature of the solution
<br>
(D) Volume of the solution

**Q4.M3 🔴**
An aqueous solution contains $10\% (\text{w/w})$ of $NaOH$ and $10\% (\text{w/w})$ of $KOH$. What is the mole fraction of water in this solution?<br> (MM: $NaOH = 40$, $KOH = 56$, $H_2O = 18$).
<br>
(A) $0.800$
<br>
(B) $0.854$
<br>
(C)
 $0.914$
<br>
(D) $0.882$

**Q4.M4 🟡**
The mole fraction of ethanol ($C_2H_5OH$) in water is $0.20$. What is the molality of the solution?<br>
<br>
(A) $13.9\text{ m}$
<br>
(B) $11.1\text{ m}$
<br>
(C)
 $27.8\text{ m}$
<br>
(D) $55.5\text{ m}$

**Q4.M5 🟡 (The "ppm to ppb" Trap)**
A water sample contains $5\text{ ppm}$ of dissolved $O_2$. What is this concentration expressed in parts per billion ($\text{ppb}$)?<br>
<br>
(A) $0.005\text{ ppb}$
<br>
(B) $50\text{ ppb}$
<br>
(C)
 $500\text{ ppb}$
<br>
(D) $5000\text{ ppb}$

**Q4.M6 🔴**
If the ratio of the mole fraction of a solute to the mole fraction of the solvent is $1:4$ in an aqueous solution, and the solute's molar mass is $72\text{ g/mol}$, what is the mass percent of the solute?<br>
<br>
(A) $20\%$
<br>
(B) $50\%$
<br>
(C)
 $25\%$
<br>
(D) $40\%$

**Q4.M7 🟡**
You mix $100\text{ g}$ of a $10\% (\text{w/w})$ $NaCl$ solution with $400\text{ g}$ of a $20\% (\text{w/w})$ $NaCl$ solution. What is the mass percent of the resulting mixture?<br>
<br>
(A) $15\%$
<br>
(B) $18\%$
<br>
(C)
 $16\%$
<br>
(D) $12\%$

**Q4.M8 🟢**
Which of the following concentration terms does NOT change when the solution is heated from $25^\circ\text{C}$ to $50^\circ\text{C}$?<br>
<br>
(A) Molarity
<br>
(B) Normality
<br>
(C)
 Volume percent ($\text{v/v}\%$)
<br>
(D) Mole fraction

**Q4.M9 🔴 (The "Double Denominator" Trap)**
A solution contains $1\text{ mole}$ of water and $1\text{ mole}$ of ethanol. What is the mass percent of water in this mixture?<br>
<br>
(A) $50\%$
<br>
(B) $28.1\%$
<br>
(C)
 $71.9\%$
<br>
(D) $18\%$

**Q4.M10 🟡**
To prepare a $10\% (\text{w/w})$ solution of $BaCl_2$, how many grams of water must be added to $20\text{ g}$ of $BaCl_2$?<br>
<br>
(A) $200\text{ g}$
<br>
(B) $180\text{ g}$
<br>
(C)
 $100\text{ g}$
<br>
(D) $80\text{ g}$

**Q4.M11 🔴**
An aqueous solution of a nonelectrolyte has a molality of $m$. The mole fraction of the solute is given by:
<br>
(A) $\frac{m}{m + 1000}$
<br>
(B) $\frac{m}{m + 55.5}$
<br>
(C)
 $\frac{m}{1000}$
<br>
(D) $\frac{55.5}{m + 55.5}$

**Q4.M12 🟡**
The concentration of a toxic chemical in a lake is $1.5\text{ mg}$ per $1\text{ kg}$ of water. What is its concentration in $\text{ppm}$?<br>
<br>
(A) $1.5\text{ ppm}$
<br>
(B) $15\text{ ppm}$
<br>
(C)
 $0.15\text{ ppm}$
<br>
(D) $150\text{ ppm}$

**Q4.M13 🟢**
If $\chi_A = 0.25$, $\chi_B = 0.35$, and $\chi_C = x$ in a ternary solution, what is the value of $x$?<br>
<br>
(A) $0.60$
<br>
(B) $0.50$
<br>
(C)
 $0.40$
<br>
(D) Cannot be determined without masses.

**Q4.M14 🔴 (The "Reverse Mixing" Trap)**
You need $500\text{ g}$ of a $15\% (\text{w/w})$ solution. You have a $30\% (\text{w/w})$ stock solution and pure water. How much of the stock solution do you need?<br>
<br>
(A) $250\text{ g}$
<br>
(B) $150\text{ g}$
<br>
(C)
 $200\text{ g}$
<br>
(D) $300\text{ g}$

**Q4.M15 🟡**
An aqueous solution of urea has a mole fraction of urea $= 0.05$. What is the ratio of the mass of water to the mass of urea in this solution?<br> ($MM_{urea} = 60$).
<br>
(A) $19:1$
<br>
(B) $171:6$
<br>
(C)
 $5.7:1$
<br>
(D) $9.5:1$

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q4.M1 → Answer: <br>
(A)**
- Total moles $= 2 + 3 = 5$.
- $\chi_A = 2 / 5 = 0.4$.

**Q4.M2 → Answer: <br>
(B)**
- $20\text{ g}$ solute, $80\text{ g}$ water.
- We can find moles of water ($80/18$).
- To find moles of solute (and thus mole fraction), we MUST have the molar mass of the solute ($20/MM$). Density and temperature are irrelevant here.

**Q4.M3 → Answer: <br>
(C)
**
- Assume $100\text{ g}$ solution.
- $10\text{ g}\ NaOH \rightarrow n = 10 / 40 = 0.25\text{ mol}$.
- $10\text{ g}\ KOH \rightarrow n = 10 / 56 = 0.1786\text{ mol}$.
- Water $= 100 - 10 - 10 = 80\text{ g} \rightarrow n_{H_2O} = 80 / 18 = 4.444\text{ mol}$.
- Total moles $= 0.25 + 0.1786 + 4.444 = 4.8726\text{ mol}$.
- $\chi_{water} = 4.444 / 4.8726 = 0.912 \approx 0.914$. (Exact arithmetic: $0.25 + 10/56 + 80/18 = 1/4 + 5/28 + 40/9 = (63 + 45 + 1120)/252 = 1228/252 = 4.873$. $4.444 / 4.873 = 0.912$. Option C is the closest).

**Q4.M4 → Answer: <br>
(A)**
- $\chi_{EtOH} = 0.20 \rightarrow \chi_{water} = 0.80$.
- $m = (\chi_{solute} \times 1000) / (\chi_{water} \times 18) = (0.20 \times 1000) / (0.80 \times 18) = 200 / 14.4 = 13.88\text{ m}$.

**Q4.M5 → Answer: <br>
(D)**
- $\text{ppm} = 1$ part per $10^6$.
- $\text{ppb} = 1$ part per $10^9$.
- $5\text{ ppm} = 5$ parts per $1,000,000$. Multiply by $1000$ to get parts per $1,000,000,000$.
- $5 \times 1000 = 5000\text{ ppb}$.

**Q4.M6 → Answer: <br>
(B)**
- Ratio $1:4$ means for every $1\text{ mole}$ of solute, there are $4\text{ moles}$ of solvent.
- Mass of solute $= 1\text{ mol} \times 72\text{ g/mol} = 72\text{ g}$.
- Mass of solvent (water) $= 4\text{ mol} \times 18\text{ g/mol} = 72\text{ g}$.
- Total mass $= 72 + 72 = 144\text{ g}$.
- Mass percent $= (72 / 144) \times 100 = 50\%$.

**Q4.M7 → Answer: <br>
(B)**
- Mass of $NaCl$ from solution $1 = 10\%$ of $100 = 10\text{ g}$.
- Mass of $NaCl$ from solution $2 = 20\%$ of $400 = 80\text{ g}$.
- Total mass of $NaCl = 10 + 80 = 90\text{ g}$.
- Total mass of mixture $= 100 + 400 = 500\text{ g}$.
- Mass percent $= (90 / 500) \times 100 = 18\%$.

**Q4.M8 → Answer: <br>
(D)**
- Mole fraction is based purely on moles (mass), which does not change with temperature. Molarity, normality, and volume percent all depend on volume, which expands with heat.

**Q4.M9 → Answer: <br>
(B)**
- Mass of water $= 1 \times 18 = 18\text{ g}$.
- Mass of ethanol $= 1 \times 46 = 46\text{ g}$.
- Total mass $= 18 + 46 = 64\text{ g}$.
- Mass $\%$ water $= (18 / 64) \times 100 = 28.125\%$.
- Trap: <br>
(A) $50\%$, confusing mole percent with mass percent.

**Q4.M10 → Answer: <br>
(B)**
- $10\% = (\text{Mass of solute} / \text{Total Mass}) \times 100$.
- $10 = (20 / W_{total}) \times 100 \rightarrow W_{total} = 200\text{ g}$.
- Mass of water added $= W_{total} - W_{solute} = 200 - 20 = 180\text{ g}$.
- Trap: <br>
(A) Thinking total mass is the mass of water to be added.

**Q4.M11 → Answer: <br>
(B)**
- $m$ molal means $m$ moles of solute in $1000\text{ g}$ ($55.5\text{ moles}$) of water.
- Total moles $= m + 55.5$.
- $\chi_{solute} = m / (m + 55.5)$.

**Q4.M12 → Answer: <br>
(A)**
- $1.5\text{ mg}$ in $1\text{ kg} = 1.5 \times 10^{-3}\text{ g} / 1000\text{ g} = 1.5 \times 10^{-6} = 1.5\text{ ppm}$.
- "mg/kg" or "mg/L" (for water) is exactly ppm.

**Q4.M13 → Answer: <br>
(C)
**
- $\chi_A + \chi_B + \chi_C = 1$.
- $0.25 + 0.35 + x = 1 \rightarrow 0.60 + x = 1 \rightarrow x = 0.40$.

**Q4.M14 → Answer: <br>
(A)**
- Let mass of stock be $x$.
- Solute needed $= 15\%$ of $500\text{ g} = 75\text{ g}$.
- The stock is $30\%$, so $0.30 x = 75 \rightarrow x = 75 / 0.30 = 250\text{ g}$.
- Alternatively, dilution law for mass: $W_1 C_1 = W_2 C_2 \rightarrow x \times 30 = 500 \times 15 \rightarrow 30x = 7500 \rightarrow x = 250\text{ g}$.

**Q4.M15 → Answer: <br>
(C)
**
- $\chi_{urea} = 0.05 \rightarrow \chi_{water} = 0.95$.
- Mole ratio $n_{water} : n_{urea} = 0.95 : 0.05 = 19 : 1$.
- Mass of water for $19\text{ moles} = 19 \times 18 = 342\text{ g}$.
- Mass of urea for $1\text{ mole} = 1 \times 60 = 60\text{ g}$.
- Mass ratio $= 342 : 60 = 5.7 : 1$.
</details>

---

*Next: [Chapter 5 — Interconversion of Concentration Units →](./05_interconversion.md)*
