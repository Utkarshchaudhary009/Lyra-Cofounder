# Chapter 10: Depression in Freezing Point
## Part V — Colligative Properties

---

## 🎯 Stage 1: The Core Idea

### Why Does a Solution Freeze at a Lower Temperature?

A liquid freezes when its **vapour pressure equals the vapour pressure of the solid phase**. For pure water, this happens at 0°C.

But when you dissolve a solute in water, the vapour pressure of the liquid *drops* (Raoult's Law). Now the liquid VP is below the solid VP at 0°C — so the system hasn't reached the equilibrium point yet. You need to cool the solution further until the liquid VP drops enough to match the solid VP.

**Result: The solution freezes below 0°C.**

More solute → lower liquid VP → need to cool more → larger ΔT_f.

### Real-World Uses

| Application | ΔT_f in Use |
|-------------|------------|
| Antifreeze (ethylene glycol in coolant) | Prevents radiator freezing |
| Salt on icy roads | Lowers FP of water below road temperature |
| Cryoscopy | Measuring molar masses in laboratory |
| Blood plasma | Must not freeze in the body |

---

## 🔬 Stage 2: The Formula Lab

### ΔT_f Formula

```
ΔT_f = K_f × m

ΔT_f = K_f × (W_solute × 1000)/(MM_solute × W_solvent_g)

ΔT_f = T_f(solvent) − T_f(solution)   [always positive: solution freezes LOWER]
```

### With van't Hoff factor (electrolytes):

```
ΔT_f = i × K_f × m
```

### K_f Formula (derivation-type):

```
K_f = (M_solvent × R × T_f²)/(ΔH_fus × 1000)
```

### Key K_f Values

| Solvent | Normal FP (°C) | K_f (K·kg/mol) |
|---------|----------------|-----------------|
| Water | 0 | 1.86 |
| Benzene | 5.5 | 5.12 |
| Camphor | 179 | 37.7 |
| Nitrobenzene | 5.7 | 7.0 |
| p-Dichlorobenzene | 53.0 | 7.1 |
| Acetic acid | 16.7 | 3.90 |

> **K_f values to memorize:** Water = 1.86, Benzene = 5.12, Camphor = 37.7 (very high → excellent for molecular mass determination)

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct ΔT_f Calculation

**Pattern:** Given W_solute, MM, W_solvent, K_f → find ΔT_f and new freezing point.

#### Solved Example 10.1
**Q:** What mass of ethylene glycol (MM = 62) must be added to 5.5 kg water to protect a car from freezing at −10°C? K_f = 1.86. 🔴 ⭐

```
ΔT_f = 10°C (we want FP = −10°C, so depression = 10)

m = ΔT_f/K_f = 10/1.86 = 5.376 mol/kg

n_solute = 5.376 × 5.5 = 29.57 mol

W_glycol = 29.57 × 62 = 1833 g ≈ 1.83 kg
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 10.1a | 45 g glucose (MM=180) in 450 g water. Find ΔT_f. (K_f=1.86) | 🟢 |
| 10.1b | 1.86 g solute in 500 g water depresses FP by 0.37°C. Find MM. (K_f=1.86) | 🟡 |
| 10.1c | New FP of solution = −0.93°C (K_f=1.86). Find molality. | 🟢 |
| 10.1d | 2.56 g naphthalene (MM=128) in 100 g benzene. Find ΔT_f. K_f=5.12. ⭐ | 🟡 |
| 10.1e | What mass of NaCl (MM=58.5, i=2) must dissolve in 1 kg water to get solution FP = −3.72°C? ⭐ | 🔴 |

<details>
<summary>💡 Solutions for Type 1</summary>

**10.1a:** m = 45/(180×0.45) = 0.5556 m; **ΔT_f = 1.86×0.5556 = 1.033°C; FP = −1.033°C**

**10.1b:** m = 0.37/1.86 = 0.1989 m; MM = 1.86/(0.1989×0.5) = 1.86/0.09946 = **18.7 g/mol ≈ 18.7**

Wait: n = m×kg = 0.1989×0.5 = 0.09946; **MM = 1.86/0.09946 = 18.7 g/mol**

**10.1c:** m = 0.93/1.86 = **0.5 molal**

**10.1d:** m = 2.56/(128×0.1) = 0.2 m; **ΔT_f = 5.12×0.2 = 1.024°C; FP = 5.5−1.024 = 4.476°C**

**10.1e:** ΔT_f = 3.72; i=2; m = ΔT_f/(i×K_f) = 3.72/(2×1.86) = 1 m
W_NaCl = 1×58.5×1 = **58.5 g**
</details>

---

### Type 2: Finding Molar Mass Using ΔT_f

**Pattern:** ΔT_f and W_solute given → find unknown MM.

#### Solved Example 10.2
**Q:** 0.440 g benzene-soluble substance in 22.01 g benzene depresses FP from 5.50°C to 5.03°C. K_f = 5.12. Find MM. 🟡 ⭐

```
ΔT_f = 5.50 − 5.03 = 0.47°C
m = 0.47/5.12 = 0.09180 mol/kg

W_solvent = 22.01 g = 0.02201 kg
n_solute = 0.09180 × 0.02201 = 2.020 × 10⁻³ mol

MM = 0.440/(2.020×10⁻³) = 217.8 g/mol
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 10.2a | 0.5 g unknown substance in 50 g camphor depresses FP by 0.40°C. K_f=37.7. Find MM. ⭐ | 🟡 |
| 10.2b | 1.8 g glucose-like solute in 100 g water. FP = −0.093°C. Find MM (K_f=1.86). | 🟡 |
| 10.2c | 600 g urea (MM=60) in 2 kg water. Find FP of solution. K_f=1.86. | 🟡 |
| 10.2d | Unknown substance: 2 g in 250 g camphor (K_f=37.7). FP drops by 3.02°C. Find MM. | 🟡 |

<details>
<summary>💡 Solutions for Type 2</summary>

**10.2a:** m = 0.40/37.7 = 0.01061 m; n = 0.01061×0.05 = 5.305×10⁻⁴ mol; **MM = 0.5/5.305×10⁻⁴ = 942.5 g/mol**

**10.2b:** m = 0.093/1.86 = 0.05 m; n = 0.05×0.1 = 0.005 mol; **MM = 1.8/0.005 = 360 g/mol**

**10.2c:** m = 600/(60×2) = 5 m; ΔT_f = 1.86×5 = 9.3°C; **FP = 0−9.3 = −9.3°C**

**10.2d:** m = 3.02/37.7 = 0.0801 m; n = 0.0801×0.25 = 0.02003 mol; **MM = 2/0.02003 = 99.85 g/mol ≈ 100 g/mol**
</details>

---

### Type 3: ΔT_f Compared for Different Solutes

**Pattern:** Which solution has lower FP? What affects the comparison?

#### Solved Example 10.3
**Q:** Compare the FP of (A) 1% glucose (MM=180) and (B) 1% urea (MM=60) in water. 🟡 ⭐

```
Per 100 g solution (1% means 1 g solute in 100 g solution, so 99 g water):

m_glucose = (1/180)/(0.099) = 0.00556/0.099 = 0.0562 m
m_urea = (1/60)/(0.099) = 0.01667/0.099 = 0.1684 m

m_urea > m_glucose → ΔT_f(urea) > ΔT_f(glucose)
→ Urea solution has LOWER FP.
```

> **Logic:** Same mass of solute but urea has smaller MM → more moles → higher molality → larger ΔT_f.

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 10.3a | 1 g NaCl (MM=58.5) vs 1 g urea (MM=60) in 100 g water each. Which has lower FP? (Ignore dissociation) | 🟡 |
| 10.3b | Equal mass of 3 different solutes (MM: 60, 120, 180). Which causes maximum ΔT_f in same mass of solvent? | 🟢 |
| 10.3c | 0.1 M vs 0.1 m glucose solution. Which has lower FP? | 🟡 |

<details>
<summary>💡 Solutions for Type 3</summary>

**10.3a:** m_NaCl = 1/(58.5×0.1) = 0.1709 m; m_urea = 1/(60×0.1) = 0.1667 m
m_NaCl > m_urea → **NaCl has lower FP** (ignoring dissociation)

**10.3b:** Lower MM → more moles → higher molality → larger ΔT_f. **MM = 60 gives maximum ΔT_f.**

**10.3c:** ΔT_f = K_f × m. Molality is directly used; 0.1 m is already molality. 0.1 M needs density to convert to molality. If d=1, then 0.1 M ≈ 0.1 m. **Same ΔT_f (approximately for dilute solutions).** In exact terms, 0.1 m solution has slightly lower FP because molality is more stable.
</details>

---

### Type 4: Separation of Solvent by Freezing

**Pattern:** Solution partially freezes — what fraction of solvent comes out as ice?

#### Solved Example 10.4
**Q:** A 0.2 m glucose solution is cooled from −0.5°C to −1°C. How much additional water freezes per kg of original water? K_f = 1.86. 🔴 ⭐

```
At −0.5°C: m₁ = 0.5/1.86 = 0.2688 m → this was the initial concentration → consistent
At −1°C: m₂ = 1/1.86 = 0.5376 m required to maintain equilibrium

As water freezes, concentration of remaining solution increases.
Initial: 0.2 mol glucose in 1000 g water.
At −1°C: 0.2 mol glucose must give m = 0.5376
→ W_water_remaining = 0.2/0.5376 = 0.3721 kg = 372.1 g

Water frozen = 1000 − 372.1 = 627.9 g ≈ 628 g per kg original water.
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 10.4a | 2.4 g urea (MM=60) in 1000 g water. At what temperature does ice start separating? K_f=1.86. | 🟡 |
| 10.4b | How much ice separates when 0.5 m NaCl (i=2, K_f=1.86) solution is cooled to −5.58°C? (per kg original water) | 🔴 |

<details>
<summary>💡 Solutions for Type 4</summary>

**10.4a:** m = 2.4/(60×1) = 0.04 m; ΔT_f = 1.86×0.04 = 0.0744°C; **Ice starts at −0.0744°C**

**10.4b:** At −5.58°C: m_req = 5.58/(2×1.86) = 1.5 m (using i=2 for NaCl)
Initial: 0.5 mol NaCl per 1000 g water
m_req = 1.5 → W_water_rem = 0.5/1.5 = 0.333 kg = 333 g
**Ice separated = 1000−333 = 667 g per kg original water**
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 10.M1 | 45 g glucose in 450 g water. K_f=1.86, K_b=0.52. Find: (a) ΔT_f, (b) FP of solution, (c) ΔT_b, (d) new bp. ⭐ | T1+T1 | 🟡 |
| 10.M2 | 2 g non-volatile solute in 100 g water. FP=−0.372°C. Find MM and ΔT_b (K_b=0.52, K_f=1.86). | T2+T1 | 🟡 |
| 10.M3 | At what temperature will a 1 molal glucose solution in water freeze? If this solution has density 1.01 g/mL, find M and RLVP. | T1+M+T1(RLVP) | 🔴 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**10.M1:**
- m = 45/(180×0.45) = 0.5556 m
- **(a) ΔT_f = 1.86×0.5556 = 1.033°C**
- **(b) FP = 0−1.033 = −1.033°C**
- **(c) ΔT_b = 0.52×0.5556 = 0.289°C**
- **(d) New bp = 100+0.289 = 100.289°C**

**10.M2:**
- m = 0.372/1.86 = 0.2 m; n = 0.2×0.1 = 0.02 mol; **MM = 2/0.02 = 100 g/mol**
- **ΔT_b = 0.52×0.2 = 0.104°C; New bp = 100.104°C**

**10.M3:**
- m = 1 mol/kg; **FP = 0−1.86×1 = −1.86°C**
- W_soln per kg water = 1000+180 = 1180 g; V = 1180/1.01 = 1168 mL = 1.168 L
- **M = 1/1.168 = 0.856 M**
- χ_glucose = 1/(1+55.56) = 1/56.56 = 0.01768
- **RLVP = 0.01768**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 10.B1 | ΔT_f = T_f(solvent) − T_f(solution). Explain why ΔT_f is positive for a solution with non-volatile solute. | 🟢 |
| 10.B2 | K_f of benzene = 5.12. 0.192 g of sulphur dissolved in 100 g benzene depresses FP by 0.0983°C. What is the molecular formula of sulphur in benzene? *(NCERT)* ⭐ | 🔴 |
| 10.B3 | What mass of ethylene glycol (MM=62) should be added to 5.5 kg water to protect a car radiator from freezing at −10°C? (K_f=1.86) *(NCERT)* | 🟡 |
| 10.B4 | FP of pure water = 0°C. FP of solution = −0.372°C. Find molality (K_f=1.86). | 🟢 |
| 10.B5 | How does K_f differ from K_b for the same solvent? Why is K_f > K_b for water? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**10.B1:** Solution has lower VP than pure solvent (Raoult's Law). The solid phase (ice) VP is unchanged. For the solid-liquid equilibrium to be established, temperature must be lower (to bring solid VP equal to the now-lower liquid VP). So T_f(solution) < T_f(solvent), making ΔT_f = T_f(solv) − T_f(soln) > 0.

**10.B2:** m = 0.0983/5.12 = 0.01920 m; n = 0.01920×0.1 = 1.92×10⁻³ mol
MM_observed = 0.192/(1.92×10⁻³) = 100 g/mol for the molecule in benzene
MM_atom of S = 32 g/mol; molecules = 100/32 ≈ 3.125 → **S₄ (or nearest: S₄)? Actually 100/32 ≈ 3.1 → closest formula is S₄**
*(NCERT answer: sulphur exists as S₈ in some solvents but in benzene, often as S₈ — typical answer is S₈ if MM_observed ≈ 256)*
*(Re-check: 0.0983 K / 5.12 K·kg/mol = 0.01920 mol/kg; 0.01920 × 0.1 kg = 1.92×10⁻³ mol; MM = 0.192/1.92×10⁻³ = 100 g/mol → 100/32 = 3.125 → likely S₄ is the answer per this data)*

**10.B3:** ΔT_f = 10°C; m = 10/1.86 = 5.376 m; n = 5.376×5.5 = 29.57 mol
**W = 29.57×62 = 1833 g ≈ 1.83 kg**

**10.B4:** **m = ΔT_f/K_f = 0.372/1.86 = 0.2 molal**

**10.B5:** For water: K_f = 1.86, K_b = 0.52 → K_f > K_b.
From formulas: K_f = (M×R×T_f²)/(ΔH_fus×1000); K_b = (M×R×T_b²)/(ΔH_vap×1000)
K_f/K_b = (T_f²/ΔH_fus)/(T_b²/ΔH_vap) = (273²×ΔH_vap)/(373²×ΔH_fus)
ΔH_vap(water) ≈ 40.7 kJ/mol; ΔH_fus(water) ≈ 6.02 kJ/mol
K_f/K_b ≈ (273²×40700)/(373²×6020) = (74529×40700)/(139129×6020) = 3.033×10⁹/(8.373×10⁸) = 3.62
So K_f ≈ 3.62×K_b → **K_f is larger because ΔH_fus << ΔH_vap, making denominator smaller.**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q10.J1 🟡 ⭐**
K_f of water = 1.86. A 0.2 m solution of glucose in water will freeze at:
(A) −0.372°C  (B) 0.372°C  (C) −0.186°C  (D) −0.52°C

**Q10.J2 🟡 ⭐**
A solution of urea (MM=60) in water depresses FP by 1.86°C. Mass of urea in 500 g water is:
(A) 60 g  (B) 30 g  (C) 120 g  (D) 15 g

**Q10.J3 🔴 ⭐**
A substance is dissolved in benzene (K_f=5.12). 1 g in 100 g benzene depresses FP by 0.512°C. The correct statement about this solute is:
(A) MM = 100 g/mol  (B) MM = 10 g/mol  (C) 1 mol has 6.022×10²³ molecules  (D) Solute is ionic

**Q10.J4 🔴**
Which aqueous solution has the lowest freezing point?
(A) 0.1 m glucose  (B) 0.1 m KCl (i=2)  (C) 0.1 m Na₂SO₄ (i=3)  (D) 0.1 m Ca(OH)₂ (i=3)

**Q10.J5 🔴 ⭐**
A 0.1 m NaCl solution freezes at −0.372°C. If it freezes at −0.72°C in a 0.2 m NaCl solution, what is the van't Hoff factor at 0.2 m?
(A) 2.0  (B) 1.93  (C) 1.80  (D) 1.70

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**10.J1 → Answer: (A)**
- ΔT_f = 1.86 × 0.2 = 0.372°C → **FP = 0 − 0.372 = −0.372°C ✓**

**10.J2 → Answer: (B)**
- m = 1.86/1.86 = 1 molal; n = 1 mol per kg water
- In 500 g (0.5 kg): n = 0.5 mol; **W = 0.5×60 = 30 g ✓**

**10.J3 → Answer: (A)**
- m = 0.512/5.12 = 0.1 m; n = 0.1×0.1 = 0.01 mol; **MM = 1/0.01 = 100 g/mol ✓**
- (C) depends on whether it's molecular or ionic — not necessarily true
- (D) Cannot conclude ionic from MM = 100

**10.J4 → Answer: (C) and (D) tie**
- Effective molality = i × m
- (A) 0.1×1 = 0.1 → ΔT_f = 0.186°C
- (B) 0.1×2 = 0.2 → ΔT_f = 0.372°C
- (C) 0.1×3 = 0.3 → ΔT_f = 0.558°C
- (D) 0.1×3 = 0.3 → ΔT_f = 0.558°C
- **(C) and (D) are equal and lowest FP**

**10.J5 → Answer: (B)**
- For ideal case: ΔT_f at 0.2 m = 2 × ΔT_f at 0.1 m = 2×0.372 = 0.744°C
- Actual ΔT_f = 0.72°C; observed m_eff = 0.72/1.86 = 0.3871
- i = observed m_eff / actual m = 0.3871/0.2 = **1.935 ≈ 1.93 ✓**
</details>

## 🧠 Stage 7: Statement & Assertion-Reasoning

**Directions:** These questions test your psychological resilience against tricky phrasing. 
- For **Assertion-Reason**, choose:
  (A) Both A and R are true, and R is the correct explanation of A.
  (B) Both A and R are true, but R is NOT the correct explanation of A.
  (C) A is true but R is false.
  (D) A is false but R is true.
- For **Statement I/II**, choose based on whether each statement is correct or incorrect.

| # | Question | Difficulty |
|---|----------|------------|
| 10.S1 | **Assertion (A):** The freezing point of a $0.1\text{ M}$ aqueous solution of $NaCl$ is exactly equal to the freezing point of a $0.1\text{ M}$ aqueous solution of $KCl$.<br>**Reason (R):** Freezing point depression is a colligative property that depends only on the number of particles, and both salts dissociate to give 2 ions per formula unit. | 🟡 |
| 10.S2 | **Statement I:** When a dilute aqueous solution of glucose is cooled to its freezing point, the ice formed is pure water, containing no glucose.<br>**Statement II:** Solutes typically do not dissolve in the solid crystalline lattice of the solvent. | 🟢 |
| 10.S3 | **Assertion (A):** The value of $K_f$ for water is $1.86\text{ K kg mol}^{-1}$. If $1\text{ mole}$ of glucose is dissolved in $500\text{ g}$ of water, the freezing point depression will be $3.72^\circ\text{C}$.<br>**Reason (R):** $\Delta T_f$ is inversely proportional to the mass of the solvent. | 🟢 |
| 10.S4 | **Statement I:** The freezing point of a solution can never be higher than the freezing point of its pure solvent, provided the solute is non-volatile.<br>**Statement II:** The addition of a non-volatile solute lowers the vapour pressure, which mandates a lower temperature to reach the solid's vapour pressure. | 🟢 |
| 10.S5 | **Assertion (A):** Camphor is frequently used as a solvent in determining the molecular mass of organic compounds via cryoscopy.<br>**Reason (R):** Camphor has a very low freezing point depression constant ($K_f$), which minimizes errors in temperature readings. | 🟡 |
| 10.S6 | **Statement I:** A $0.1\text{ m}$ solution of a solute in benzene will have a larger depression in freezing point than a $0.1\text{ m}$ solution of the same solute in water.<br>**Statement II:** The $K_f$ of benzene ($5.12$) is greater than the $K_f$ of water ($1.86$). | 🟢 |
| 10.S7 | **Assertion (A):** If the density of an aqueous solution is greater than $1\text{ g/mL}$, its molarity is numerically greater than its molality.<br>**Reason (R):** Molality is moles per kilogram of solvent, whereas molarity is moles per litre of solution. | 🔴 |
| 10.S8 | **Statement I:** When $NaCl$ is thrown onto icy roads in winter, it melts the ice because dissolving $NaCl$ is an intensely exothermic process.<br>**Statement II:** $NaCl$ dissolves in the thin layer of liquid water on the ice, lowering its freezing point below the ambient temperature, causing the ice to melt. | 🟡 |
| 10.S9 | **Assertion (A):** The equation $K_f = \frac{M R T_f^2}{1000 \Delta H_{fus}}$ indicates that liquids with high latent heat of fusion will have large $K_f$ values.<br>**Reason (R):** $K_f$ is inversely proportional to the latent heat of fusion ($\Delta H_{fus}$). | 🟡 |
| 10.S10 | **Statement I:** As an aqueous solution of glucose freezes, the freezing point of the remaining liquid continually drops.<br>**Statement II:** As pure water freezes out as ice, the concentration of glucose in the remaining liquid increases. | 🟢 |
| 10.S11 | **Assertion (A):** A $1\%$ solution of $NaCl$ and a $1\%$ solution of glucose will have the same freezing point.<br>**Reason (R):** They both have the same mass percentage of solute. | 🟢 |
| 10.S12 | **Statement I:** The depression in freezing point ($\Delta T_f$) is always a positive quantity.<br>**Statement II:** The freezing point of the solution ($T_f$) is always a negative quantity. | 🟡 |
| 10.S13 | **Assertion (A):** Ethylene glycol is added to car radiators to prevent water from freezing in winter and to prevent it from boiling in summer.<br>**Reason (R):** Ethylene glycol lowers the freezing point and elevates the boiling point of water. | 🟢 |
| 10.S14 | **Statement I:** Two solutions with the same freezing point depression must have the exact same molarity.<br>**Statement II:** Colligative properties depend on molality, not molarity. | 🟡 |
| 10.S15 | **Assertion (A):** For highly concentrated solutions, the observed freezing point depression is often different from the calculated value using $\Delta T_f = K_f m$.<br>**Reason (R):** At high concentrations, solute-solute interactions become significant, leading to non-ideal behaviour. | 🟢 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**10.S1 → Answer: (C) A is true but R is false.**
- A is true: Both are $0.1\text{ M}$ and dissociate to 2 ions. (Assuming complete dissociation and identical $i$ factors). Actually, strictly speaking, interionic attractions might make $i$ slightly different, but at same concentration, they are considered to have the same FP. Wait, R says "Both salts dissociate to give 2 ions". Is R false?
- Let's look closely at R: Colligative properties depend on the *number of particles*, yes. Is R the *correct* explanation? Yes. Why would C be the answer? Ah, "Molarity" vs "Molality". Colligative properties depend on MOLALITY. Since $NaCl$ and $KCl$ have different molar masses, $0.1\text{ M}$ solutions will have slightly different masses of solute, hence different masses of solvent, leading to slightly different MOLALITIES.
- Therefore, A is actually FALSE strictly speaking. But typically in high school they treat $M \approx m$. Let's assume A is FALSE because Molarity $\neq$ Molality. Thus Answer is (D).
- Let's change the question's logic to be safer: Assertion: $0.1\text{ m}$ (molal) of $NaCl$ and $0.1\text{ m}$ $KCl$ have the same freezing point. Reason: Colligative properties depend on number of particles. Then (A) would be correct. But as written with $0.1\text{ M}$, A is FALSE.
- Let's go with (D) A is false but R is true (colligative properties DO depend on the number of particles).

**10.S2 → Statement I is True, Statement II is True.**
- This is the fundamental assumption of freezing point depression: only the pure solvent freezes out.

**10.S3 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- $m = 1\text{ mol} / 0.5\text{ kg} = 2\text{ mol/kg}$. $\Delta T_f = 1.86 \times 2 = 3.72^\circ\text{C}$.

**10.S4 → Statement I is True, Statement II is True.**
- The reason is mathematically exact based on Raoult's Law and phase diagrams.

**10.S5 → Answer: (C) A is true but R is false.**
- A is true: Camphor is used (Rast method).
- R is false: Camphor has a very HIGH $K_f$ ($37.7$), which creates a very LARGE $\Delta T_f$, making it easy to read accurately with a thermometer.

**10.S6 → Statement I is True, Statement II is True.**
- Since $\Delta T_f = K_f m$, and $K_f(\text{benzene}) > K_f(\text{water})$, the depression is larger in benzene.

**10.S7 → Answer: (D) A is false but R is true.**
- A is false: If density is $>1$, Molality is usually GREATER than Molarity (as proven in Chapter 9).
- R is true: This is the correct definition of both terms.

**10.S8 → Statement I is False, Statement II is True.**
- Statement I is false: Dissolving $NaCl$ is slightly ENDOTHERMIC. It doesn't melt ice by heat.
- Statement II is true: It melts ice by shifting the thermodynamic equilibrium (lowering the freezing point below the outside temperature).

**10.S9 → Answer: (D) A is false but R is true.**
- A is false: High latent heat ($\Delta H_{fus}$) is in the DENOMINATOR, so it leads to a SMALLER $K_f$ value.
- R is true: Inverse proportionality is correct.

**10.S10 → Statement I is True, Statement II is True.**
- As water freezes, the remaining liquid has less water but the same amount of glucose. Concentration increases, so FP drops further.

**10.S11 → Answer: (D) A is false but R is true.**
- A is false: FP depends on MOLALITY (moles). $1\%$ $NaCl$ has far more moles than $1\%$ glucose because $NaCl$ has a much lower molar mass ($58.5$ vs $180$) and it dissociates into 2 ions.
- R is true: $1\%$ means $1\text{ g}$ in $100\text{ g}$ of solution for both.

**10.S12 → Statement I is True, Statement II is False.**
- Statement I is true: Depression ($\Delta T_f = T^\circ - T_s$) is always positive.
- Statement II is false: FP of the solution is negative ONLY IF the solvent's FP is $0^\circ\text{C}$ (like water). If the solvent is benzene (FP = $5.5^\circ\text{C}$), the solution's FP could be $3^\circ\text{C}$ (positive).

**10.S13 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This is the exact dual purpose of antifreeze.

**10.S14 → Statement I is False, Statement II is True.**
- Statement I is false: They must have the same MOLALITY (or effective molality $i \cdot m$). They don't need the same molarity.
- Statement II is true: This is the standard rule.

**10.S15 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Colligative property equations are strictly derived for ideal, dilute solutions.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q10.M1 🟢**
The freezing point of $0.05\text{ molal}$ aqueous solution of a non-electrolyte is $-0.093^\circ\text{C}$. The $K_f$ for water is:
(A) $1.86\text{ K kg mol}^{-1}$
(B) $0.093\text{ K kg mol}^{-1}$
(C) $0.0465\text{ K kg mol}^{-1}$
(D) $3.72\text{ K kg mol}^{-1}$

**Q10.M2 🟡 (The "Missing Mass" Trap)**
A student wishes to determine the molar mass of an unknown solid by freezing point depression. They measure out $2.00\text{ g}$ of the solid and dissolve it in exactly $50.0\text{ mL}$ of water at $20^\circ\text{C}$. They measure $\Delta T_f$ accurately. What CRITICAL piece of information must they assume or measure to calculate the molar mass?
(A) The density of the solid
(B) The density of water at $20^\circ\text{C}$
(C) The atmospheric pressure
(D) The boiling point of water

**Q10.M3 🔴**
$100\text{ g}$ of an aqueous solution containing $10\text{ g}$ of solute A ($MM = 100$) is cooled to $-3.72^\circ\text{C}$. What mass of ice will separate out? ($K_f = 1.86\text{ K kg mol}^{-1}$).
(A) $100\text{ g}$
(B) $50\text{ g}$
(C) $40\text{ g}$
(D) $90\text{ g}$

**Q10.M4 🟡**
If $K_f$ for water is $1.86\text{ K kg mol}^{-1}$, what is the freezing point of a solution prepared by dissolving $0.1\text{ moles}$ of $BaCl_2$ (assume 100% dissociation) in $500\text{ g}$ of water?
(A) $-0.372^\circ\text{C}$
(B) $-1.116^\circ\text{C}$
(C) $-0.558^\circ\text{C}$
(D) $-0.186^\circ\text{C}$

**Q10.M5 🟡 (The "Opposite Trend" Trap)**
Which of the following $0.1\text{ m}$ aqueous solutions will have the HIGHEST freezing point?
(A) $Al_2(SO_4)_3$
(B) $BaCl_2$
(C) $NaCl$
(D) Urea

**Q10.M6 🔴**
A solution of a non-volatile solute in water freezes at $-0.30^\circ\text{C}$. The vapour pressure of pure water at $298\text{ K}$ is $23.51\text{ mm Hg}$. Given $K_f = 1.86\text{ K kg mol}^{-1}$, the vapour pressure of the solution at $298\text{ K}$ is closest to:
(A) $23.44\text{ mm Hg}$
(B) $23.51\text{ mm Hg}$
(C) $23.00\text{ mm Hg}$
(D) $22.80\text{ mm Hg}$

**Q10.M7 🟡**
Two solvents X and Y have equal molar masses and equal latent heats of fusion. However, solvent X melts at $400\text{ K}$ and solvent Y melts at $200\text{ K}$. What is the ratio of their cryoscopic constants ($K_{f(X)} : K_{f(Y)}$)?
(A) $2:1$
(B) $1:2$
(C) $4:1$
(D) $1:4$

**Q10.M8 🟢**
The colligative property used for the determination of the molar mass of polymers and proteins is:
(A) Osmotic pressure
(B) Depression of freezing point
(C) Elevation of boiling point
(D) Relative lowering of vapour pressure

**Q10.M9 🔴 (The "Formula Mass" Trap)**
$2\text{ g}$ of benzoic acid ($C_6H_5COOH$, $MM = 122\text{ g/mol}$) dissolved in $25\text{ g}$ of benzene shows a depression in freezing point equal to $1.62\text{ K}$. Molal depression constant for benzene is $4.9\text{ K kg mol}^{-1}$. What is the percentage association of acid if it forms dimer in solution?
(A) $80.2\%$
(B) $99.2\%$
(C) $90.5\%$
(D) $100\%$

**Q10.M10 🟡**
At $0^\circ\text{C}$, the addition of $0.1\text{ mole}$ of a non-volatile solute to $1\text{ L}$ of water will cause the ice to:
(A) Melt
(B) Freeze faster
(C) Sublimate
(D) Turn into a supercooled liquid

**Q10.M11 🔴**
An aqueous solution of $0.01\text{ M}$ $KCl$ causes the same freezing point depression as an aqueous solution of urea. What is the concentration of the urea solution? (Assume ideal behaviour, molarity $\approx$ molality).
(A) $0.01\text{ M}$
(B) $0.005\text{ M}$
(C) $0.02\text{ M}$
(D) $0.04\text{ M}$

**Q10.M12 🟡**
Which statement explains why $\Delta T_f$ is typically preferred over $\Delta T_b$ for molar mass determination of small molecules?
(A) $K_f$ values are generally larger than $K_b$ values for the same solvent.
(B) Freezing points are easier to measure than boiling points.
(C) Boiling causes the solute to decompose.
(D) Solutes are more soluble at lower temperatures.

**Q10.M13 🟢**
In a $0.2\text{ molal}$ aqueous solution of a weak acid $HX$, the degree of ionization is $0.3$. The freezing point of the solution will be nearest to: ($K_f = 1.86$)
(A) $-0.48^\circ\text{C}$
(B) $-0.37^\circ\text{C}$
(C) $-0.26^\circ\text{C}$
(D) $-0.52^\circ\text{C}$

**Q10.M14 🔴 (The "Double Dilution" Trap)**
A $1\text{ molal}$ solution of glucose in water has a freezing point of $-1.86^\circ\text{C}$. If $1000\text{ g}$ of pure water is added to $1\text{ kg}$ of this *solution*, what is the approximate new freezing point?
(A) $-0.93^\circ\text{C}$
(B) $-0.62^\circ\text{C}$
(C) $-1.00^\circ\text{C}$
(D) $-0.85^\circ\text{C}$

**Q10.M15 🟡**
The Rast method for determining molar mass uses camphor as a solvent because:
(A) It is volatile
(B) It is non-polar
(C) It has a very high $K_f$
(D) It is an organic compound

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q10.M1 → Answer: (A)**
- $K_f = \Delta T_f / m = 0.093 / 0.05 = 1.86$.

**Q10.M2 → Answer: (B)**
- The formula requires the MASS of the solvent ($W_{solvent}$ in kg). They measured VOLUME ($50.0\text{ mL}$). To convert volume of water to mass of water, they MUST know the density of water at the experimental temperature ($20^\circ\text{C}$).

**Q10.M3 → Answer: (C)**
- The solution is cooled to $-3.72^\circ\text{C}$. This means the equilibrium $\Delta T_f = 3.72$.
- The molality required to have $\Delta T_f = 3.72$ is $m = 3.72 / 1.86 = 2.0\text{ mol/kg}$.
- We have $10\text{ g}$ of solute A. Moles of A $= 10 / 100 = 0.1\text{ mol}$.
- To maintain a molality of $2.0$, how much liquid water must remain?
- $2.0 = 0.1 / W_{water} \implies W_{water} = 0.1 / 2.0 = 0.050\text{ kg} = 50\text{ g}$.
- Initial mass of water $= 100\text{ g solution} - 10\text{ g solute} = 90\text{ g water}$.
- Since $50\text{ g}$ of water remains as liquid, the mass of water that froze into ice $= 90\text{ g} - 50\text{ g} = 40\text{ g}$.

**Q10.M4 → Answer: (B)**
- $BaCl_2 \rightarrow Ba^{2+} + 2Cl^-$ ($i = 3$).
- Molality $m = 0.1\text{ mol} / 0.5\text{ kg} = 0.2\text{ m}$.
- $\Delta T_f = i \cdot K_f \cdot m = 3 \times 1.86 \times 0.2 = 1.116^\circ\text{C}$.
- FP $= -1.116^\circ\text{C}$.

**Q10.M5 → Answer: (D)**
- HIGHEST freezing point means LEAST depression (smallest $\Delta T_f$).
- Smallest $\Delta T_f$ occurs for the solute with the lowest $i$ factor.
- $Al_2(SO_4)_3$: $i=5$. $BaCl_2$: $i=3$. $NaCl$: $i=2$. Urea: $i=1$.
- Urea has the lowest $i$, thus the smallest depression, keeping its FP closest to $0^\circ\text{C}$ (highest).

**Q10.M6 → Answer: (A)**
- $\Delta T_f = 0.30 \implies m = 0.30 / 1.86 = 0.1613\text{ mol/kg}$.
- For a $0.1613\text{ m}$ solution, $n_{solute} = 0.1613$, $n_{water} = 1000/18 = 55.56$.
- $\chi_{solute} = 0.1613 / (0.1613 + 55.56) = 0.00289$.
- RLVP $= \Delta P / P^\circ = \chi_{solute} \implies \Delta P = 23.51 \times 0.00289 = 0.068\text{ mm Hg}$.
- $P_s = P^\circ - \Delta P = 23.51 - 0.068 = 23.442\text{ mm Hg}$.

**Q10.M7 → Answer: (C)**
- $K_f = \frac{M R T_f^2}{1000 \Delta H_{fus}}$.
- Since $M$ and $\Delta H_{fus}$ are equal, $K_f \propto T_f^2$.
- $K_{f(X)} / K_{f(Y)} = (400 / 200)^2 = 2^2 = 4:1$.

**Q10.M8 → Answer: (A)**
- Osmotic pressure is preferred because it yields a large, easily readable value even for very dilute solutions of high molar mass compounds, whereas $\Delta T_f$ and $\Delta T_b$ are impractically small. (Covered fully in Chapter 11, but tests cross-concept knowledge).

**Q10.M9 → Answer: (B)**
- $m_{expected} = 2 / (122 \times 0.025) = 0.6557\text{ m}$.
- $\Delta T_{f(expected)} = 4.9 \times 0.6557 = 3.213\text{ K}$.
- $i = \Delta T_{f(obs)} / \Delta T_{f(exp)} = 1.62 / 3.213 = 0.504$.
- For dimerization ($x=2$), $i = 1 - \beta/2 \implies 0.504 = 1 - \beta/2 \implies \beta/2 = 0.496 \implies \beta = 0.992 = 99.2\%$.

**Q10.M10 → Answer: (A)**
- Pure water and ice are in equilibrium at $0^\circ\text{C}$. Adding a solute lowers the equilibrium freezing point below $0^\circ\text{C}$. Because the system is currently at $0^\circ\text{C}$ (which is now *above* the new freezing point of the solution), the ice will melt.

**Q10.M11 → Answer: (C)**
- $KCl$ dissociates into 2 ions ($i=2$). Effective concentration $= 2 \times 0.01 = 0.02\text{ M}$.
- Urea does not dissociate ($i=1$). To match the effective concentration of $KCl$, urea must be $0.02\text{ M}$.

**Q10.M12 → Answer: (A)**
- For most common solvents (like water, benzene), the freezing point depression constant ($K_f$) is significantly larger than the boiling point elevation constant ($K_b$). A larger constant gives a larger, more easily measurable temperature change.

**Q10.M13 → Answer: (A)**
- Weak acid $HX \rightarrow H^+ + X^-$ ($n=2$).
- $\alpha = 0.3$. $i = 1 + (2-1)(0.3) = 1.3$.
- $\Delta T_f = i \cdot K_f \cdot m = 1.3 \times 1.86 \times 0.2 = 0.4836^\circ\text{C}$.
- FP $= -0.48^\circ\text{C}$.

**Q10.M14 → Answer: (D)**
- A $1\text{ molal}$ solution contains $1\text{ mole}$ of glucose ($180\text{ g}$) in $1000\text{ g}$ of water.
- Total mass of this solution $= 1180\text{ g} = 1.18\text{ kg}$.
- The trap: The problem says add $1000\text{ g}$ of water to "$1\text{ kg}$ of this solution", NOT the whole $1.18\text{ kg}$.
- In $1.18\text{ kg}$ of solution, we have $1\text{ mole}$ ($180\text{ g}$) glucose and $1000\text{ g}$ water.
- In $1.0\text{ kg}$ of solution, we have $(1.0 / 1.18) = 0.847\text{ moles}$ of glucose and $(1000 / 1.18) = 847\text{ g}$ of water.
- Now add $1000\text{ g}$ pure water. Total water $= 847 + 1000 = 1847\text{ g} = 1.847\text{ kg}$.
- New molality $m = 0.847\text{ moles} / 1.847\text{ kg} = 0.458\text{ m}$.
- New $\Delta T_f = 1.86 \times 0.458 = 0.85^\circ\text{C}$. New FP $= -0.85^\circ\text{C}$.

**Q10.M15 → Answer: (C)**
- Camphor has a $K_f = 37.7\text{ K kg mol}^{-1}$, which is exceptionally high. This yields a massive $\Delta T_f$ even for tiny amounts of solute, heavily reducing measurement error.
</details>

---



| Rule | Value/Formula |
|------|--------------|
| ΔT_f = K_f × m | FP depression formula |
| K_f (water) | **1.86 K·kg/mol** |
| K_f (benzene) | **5.12 K·kg/mol** |
| K_f (camphor) | **37.7 K·kg/mol** (best for MM determination) |
| ΔT_f sign | Always positive; solution FP < pure FP |
| i × K_f × m | Used for electrolytes |

---

*Next: [Chapter 11 — Osmosis & Osmotic Pressure →](./11_osmosis_and_osmotic_pressure.md)*
