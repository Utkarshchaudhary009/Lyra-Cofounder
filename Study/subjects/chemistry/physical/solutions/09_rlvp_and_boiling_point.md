# Chapter 9: RLVP & Elevation of Boiling Point
## Part V — Colligative Properties

---

## 🎯 Stage 1: The Core Idea

### What Makes a Colligative Property?<br>

A **colligative property** depends *only on the number of solute particles*, not their identity. It doesn't matter if the solute is glucose or NaCl — what matters is how many particles are in solution.

The four colligative properties are:
1. **Relative Lowering of Vapour Pressure (RLVP)** ← This chapter
2. **Elevation of Boiling Point (ΔT_b)** ← This chapter
3. Depression of Freezing Point (ΔT_f) ← Chapter 10
4. Osmotic Pressure (π) ← Chapter 11

### RLVP — Why VP Drops

When you add a non-volatile solute, solute particles occupy space at the surface. Fewer solvent molecules can escape → evaporation rate drops → equilibrium VP is lower.

The fractional decrease = mole fraction of solute. That's it.

### Elevation of BP — Why BP Rises

Liquid boils when VP = atmospheric pressure. A solution has lower VP than pure solvent. So you need to heat the solution *more* to push VP up to atmospheric pressure.

More solute → lower VP → need more heat → higher boiling point.

**Visual intuition (VP vs T graph):** Plot VP on y-axis vs Temperature on x-axis. Both pure solvent and solution have exponentially rising VP curves, but the solution curve lies below the pure solvent curve. Draw a horizontal line at atmospheric pressure (P_atm) — where each curve crosses it is the boiling point. The solution's crossing is to the right (higher T). The horizontal distance between the two crossings = ΔT_b.

---

## 🔬 Stage 2: The Formula Lab

### RLVP Formulas

```
Standard RLVP:
    (P° − P_s)/P° = χ_solute = n_solute/(n_solute + n_solvent)

Modified RLVP (easier for unknown MM):
    (P° − P_s)/P_s = n_solute/n_solvent = (W_s × M_solvent)/(MM_s × W_solvent)

With van't Hoff factor:
    RLVP = (i × n_solute)/(i × n_solute + n_solvent)
```

### Elevation of Boiling Point Formulas

```
ΔT_b = K_b × m

Expanded:
    ΔT_b = K_b × (W_solute × 1000)/(MM_solute × W_solvent_g)

K_b (ebullioscopic constant):
    K_b = (M_solvent × R × T_b²)/(ΔH_vap × 1000)

With van't Hoff factor (electrolytes):
    ΔT_b = i × K_b × m
```

> **📌 Physical meaning of K_b:** The ebullioscopic constant K_b is the elevation in boiling point when 1 mole of a non-volatile solute is dissolved in 1 kg of the solvent. For water, K_b = 0.52 means a 1 molal aqueous solution boils at 100.52°C (ΔT_b = 0.52°C).

### Key K_b Values for Common Solvents

| Solvent | Normal BP (°C) | K_b (K·kg/mol) |
|---------|---------------|-----------------|
| Water | 100 | 0.52 |
| Benzene | 80.1 | 2.53 |
| Chloroform | 61.2 | 3.63 |
| CCl₄ | 76.7 | 5.03 |
| Ethanol | 78.4 | 1.20 |

> **⚠️ Trap:** ΔT_b = T_b(solution) − T_b(solvent). It's always positive (boiling point increases). If asked for "new boiling point," add ΔT_b to the solvent's boiling point.

### Abnormal Molecular Masses & van't Hoff Factor

When a solute dissociates (electrolytes like NaCl → Na⁺ + Cl⁻) or associates (like benzoic acid dimerization in benzene), the **observed** number of particles differs from the expected number.

$$i = \frac{\text{observed colligative effect}}{\text{expected colligative effect}} = \frac{\text{normal molar mass}}{\text{observed molar mass}}$$

For dissociation:
$$i = 1 + \alpha(\nu - 1)$$

where $\alpha$ = degree of dissociation, $\nu$ = number of ions per formula unit ($\nu = 2$ for NaCl, $\nu = 3$ for CaCl₂).

For association:
$$i = 1 + \alpha\left(\frac{1}{n} - 1\right)$$

where $n$ = number of molecules that associate (e.g., $n = 2$ for dimerization).

When using van't Hoff factor:
- RLVP formula: $\text{RLVP} = \dfrac{i \, n_{solute}}{i \, n_{solute} + n_{solvent}}$
- Boiling point elevation: $\Delta T_b = i \cdot K_b \cdot m$

### Ostwald-Walker Experiment (RLVP Measurement)

Dry air passes through: solution → pure solvent → CaCl₂ tube

```
RLVP = W_2/(W_1 + W_2)

where:
    W_1 = loss in mass of solution container
    W_2 = loss in mass of pure solvent container
    W_1 + W_2 = gain in mass of CaCl₂ tube
```

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct RLVP Calculation

**Pattern:** Find χ_solute or P_s from given data.

#### Solved Example 9.1
**Q:** 0.60 g urea (MM = 60) in 360 g water. P° = 35 mm. Find ΔP. 🟡 ⭐

```
n_urea = 0.60/60 = 0.01 mol
n_water = 360/18 = 20 mol
χ_urea = 0.01/20.01 = 4.998×10⁻⁴

ΔP = P° × χ_urea = 35 × 4.998×10⁻⁴ = 0.0175 mm Hg
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 9.1a | The relative lowering of vapour pressure of a dilute aqueous solution is 0.2. What is the mole fraction of the solute?<br> | 🟢 |
| 9.1b | At a given temperature, the vapour pressure of a pure solvent is 20 torr. When a non-volatile solute is dissolved, the vapour pressure of the solution becomes 17 torr at the same temperature. Determine the mole fraction of the solute. | 🟢 |
| 9.1c | 18 g of glucose (molar mass 180 g/mol) is dissolved in 180 g of water. The vapour pressure of pure water at the experimental temperature is 23.8 torr. Calculate the vapour pressure of the glucose solution. | 🟡 |
| 9.1d | The relative lowering of vapour pressure of an aqueous solution containing a non-volatile solute is 0.0125. Calculate the molality of the solution. ⭐ | 🟡 |
| 9.1e | 34.2 g of sucrose (molar mass 342 g/mol) is dissolved in 500 g of water. The vapour pressure of pure water at the given temperature is 30 torr. Calculate the lowering of vapour pressure and the vapour pressure of the solution. | 🟢 |
| 9.1f | The vapour pressure of a pure liquid at a certain temperature is 40 mm Hg. When a non-volatile non-electrolyte is dissolved in it, the vapour pressure drops to 39.2 mm Hg at the same temperature. Calculate the relative lowering of vapour pressure and the mole fraction of the solute. | 🟢 |
| 9.1g | A solution is prepared by dissolving 0.5 mole of a non-volatile solute in 500 g of water. The vapour pressure of pure water at the experimental temperature is 25 torr. Calculate the vapour pressure of the resulting solution. | 🟡 |
| 9.1h | At a given temperature, the vapour pressure of pure water is 23.8 torr. A solution of a non-volatile solute shows a vapour pressure of 23.5 torr at the same temperature. If the molality of the solution is 0.5 m, calculate the mole fraction of the solute. | 🟡 |
| 9.1i | The relative lowering of vapour pressure of an aqueous solution is 0.02. Calculate the mole fraction of water in the solution. | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**9.1a:** RLVP = χ_solute → **χ_solute = 0.2**

**9.1b:** RLVP = (20−17)/20 = 3/20 = **0.15 = χ_solute**

**9.1c:** n_glucose = 0.1; n_H₂O = 10; χ_water = 10/10.1 = 0.9901
**P_s = 23.8 × 0.9901 = 23.56 torr**

**9.1d:** χ_solute = 0.0125; χ_water = 0.9875
m = (0.0125×1000)/(0.9875×18) = 12.5/17.775 = **0.703 m**

**9.1e:** n_sucrose = 34.2/342 = 0.1 mol; n_H₂O = 500/18 = 27.78 mol
χ_sucrose = 0.1/27.88 = 0.003587
**ΔP = 30 × 0.003587 = 0.108 torr; P_s = 30 − 0.108 = 29.892 torr**

**9.1f:** RLVP = (40−39.2)/40 = 0.8/40 = **χ_solute = 0.02**

**9.1g:** n_solute = 0.5 mol; n_H₂O = 500/18 = 27.78 mol
χ_solute = 0.5/28.28 = 0.01768
**P_s = P° × (1 − χ_solute) = 25 × 0.9823 = 24.56 torr**

**9.1h → Statement I is False, Statement II is True.**
- Statement I is false: RLVP = χ_solute, which depends only on mole fraction, not the identity of the solute.
- Statement II is true: This is the definition of a colligative property.

**9.1i:** χ_solute = 0.02 → **χ_solvent = 1 − 0.02 = 0.98**
</details>

---

### Type 2: Finding Molar Mass Using RLVP

**Pattern:** VP lowering gives χ_solute → find moles → find MM.

#### Solved Example 9.2
**Q:** Pure benzene VP = 640 mm. 2.175 g non-volatile solid in 39 g benzene → VP = 600 mm. Find MM. 🟡 ⭐

```
Method: Modified formula
(P° − P_s)/P_s = n_solute/n_solvent
(640 − 600)/600 = (2.175/MM)/(39/78)
40/600 = (2.175/MM)/0.5
0.0667 = 4.35/MM
MM = 4.35/0.0667 = 65.25 g/mol
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 9.2a | VP of water at 20°C = 17.54 mm. 20 g of solute in 100 g water → VP = 17.24 mm. Find MM. ⭐ | 🟡 |
| 9.2b | VP benzene at 80°C = 750 mm. 2 g substance in 78 g benzene → VP drops by 10 mm. Find MM. | 🟡 |
| 9.2c | VP lowering = 0.30 mm from P° = 17.54 mm for 20 g solute in 100 g water. Find MM. | 🟡 |
| 9.2d | **Statement I:** The modified RLVP formula $\frac{P^\circ - P_s}{P_s} = \frac{n_2}{n_1}$ gives a more accurate molar mass than the standard formula.<br>**Statement II:** The standard formula requires the approximation $n_1 + n_2 \approx n_1$, while the modified formula does not. | 🟡 |
| 9.2e | **Assertion <br>
(A):** If the VP lowering ($\Delta P$) is known along with $P^\circ$, the molar mass of a non-volatile solute can always be uniquely determined.<br>**Reason (R):** $\Delta P / P^\circ = \chi_{solute}$, and $\chi_{solute}$ uniquely determines the molar mass when solvent mass and solute mass are known. | 🔴 |
| 9.2f | **Statement I:** For very dilute solutions, both the standard and modified RLVP formulas give nearly identical molar masses.<br>**Statement II:** At high dilution, $n_{solute} \ll n_{solvent}$, so the approximation in the standard formula becomes negligible. | 🟡 |
| 9.2g | **Assertion <br>
(A):** The RLVP method can determine molar masses of volatile solutes as accurately as non-volatile ones.<br>**Reason (R):** RLVP depends only on the mole fraction of the solute particles. | 🔴 |
| 9.2h | The vapour pressure of pure benzene at a certain temperature is 640 mm Hg. When 1.5 g of a non-volatile non-electrolyte solute is dissolved in 30 g of benzene (molar mass 78 g/mol), the vapour pressure of the solution is found to be 610 mm Hg. Calculate the molar mass of the solute. 🟡 ⭐ | 🟡 |
| 9.2i | At 25°C, the vapour pressure of pure water is 23.8 mm Hg. A solution is prepared by dissolving 5.0 g of an unknown non-volatile non-electrolyte in 100 g of water. The vapour pressure of this solution at the same temperature is found to be 23.5 mm Hg. Determine the molar mass of the unknown solute. 🔴 | 🔴 |
| 9.2j | The vapour pressure of pure chloroform (CHCl₃, molar mass 119.5 g/mol) at a given temperature is 200 mm Hg. When 2.0 g of a non-volatile substance is dissolved in 40.0 g of chloroform, the vapour pressure of the solution is 195 mm Hg at the same temperature. Calculate the molar mass of the dissolved substance. | 🟡 |

<details>
<summary>💡 Solutions for Type 2</summary>

**9.2a:** RLVP = 0.30/17.54 = 0.01710
n_H₂O = 100/18 = 5.556; χ_s = n_s/(n_s+5.556) = 0.01710
n_s(1-0.01710) = 0.01710×5.556 = 0.09506; n_s = 0.09506/0.9829 = 0.09672 mol
**MM = 20/0.09672 = 206.8 g/mol**

**9.2b:** (P°−P_s)/P_s = n_s/n_solv → 10/740 = (2/MM)/(78/78) = 2/MM
**MM = 2×740/10 = 148 g/mol**

**9.2c:** Same as 9.2a → **MM ≈ 206.8 g/mol**

**9.2d → Statement I is True, Statement II is True.**
- Both statements are correct. The modified formula avoids the $n_1 + n_2 \approx n_1$ approximation, making it more accurate, especially for concentrated solutions.

**9.2e → Assertion is False, Reason is True.**
- A is false: Knowing $\Delta P$ and $P^\circ$ alone is not enough. You also need the masses of solute and solvent to compute the molar mass.
- R is true: $\Delta P/P^\circ = \chi_{solute}$, and with the masses, molar mass follows.

**9.2f → Statement I is True, Statement II is True.**
- In very dilute solutions, $n_2 \ll n_1$, so $n_1 + n_2 \approx n_1$ is an excellent approximation.

**9.2g → Assertion is False, Reason is False.**
- A is false: If the solute is volatile, it contributes to VP, so RLVP formulas (derived for non-volatile solutes) do not apply directly.
- R is false: RLVP depends on the mole fraction only when the solute is non-volatile. For volatile solutes, Raoult's law applies to both components.

**9.2h:** P° = 640 mm, P_s = 610 mm, ΔP = 30 mm
Using modified formula: (P°−P_s)/P_s = n_s/n_benzene
30/610 = (1.5/MM) / (30/78) → 0.04918 = (1.5/MM) / 0.3846
1.5/MM = 0.04918 × 0.3846 = 0.01892
**MM = 1.5/0.01892 = 79.3 g/mol**

**9.2i:** P° = 23.8 mm, P_s = 23.5 mm, ΔP = 0.3 mm
n_H₂O = 100/18 = 5.556 mol
RLVP = 0.3/23.8 = 0.01261 = n_s/(n_s + 5.556)
n_s = 0.01261 × 5.556 / (1 − 0.01261) = 0.07006/0.9874 = 0.07096 mol
**MM = 5.0/0.07096 = 70.5 g/mol**

**9.2j:** P° = 200 mm, P_s = 195 mm, ΔP = 5 mm
n_chloroform = 40.0/119.5 = 0.3347 mol
Using modified: (200−195)/195 = n_s/0.3347
5/195 = 0.02564 = n_s/0.3347
n_s = 0.02564 × 0.3347 = 0.008581 mol
**MM = 2.0/0.008581 = 233.1 g/mol**
</details>

---

### Type 3: Ostwald-Walker Experiment

**Pattern:** Use masses from Ostwald-Walker apparatus to find RLVP and then MM.

#### Solved Example 9.3
**Q:** Dry air passed through: 5 g solute in 80 g water → loss = 2.50 g; then pure water → loss = 0.04 g. Find MM of solute. 🔴 ⭐

```
RLVP = W₂/(W₁+W₂) = 0.04/(2.50+0.04) = 0.04/2.54 = 0.01575

χ_solute = 0.01575
n_H₂O = 80/18 = 4.444 mol

n_s/(n_s + 4.444) = 0.01575
n_s(1-0.01575) = 0.01575×4.444 = 0.07
n_s = 0.07/0.9843 = 0.07112 mol

MM = 5/0.07112 = 70.3 g/mol ≈ 70 g/mol
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 9.3a | In Ostwald-Walker: solution mass loss = 2.50, solvent mass loss = 0.04, CaCl₂ gain = 2.54. Find RLVP. | 🟢 |
| 9.3b | 20 g solute in 250 mL water. Mass lost: solution = 26 g, CaCl₂ gain = 26.48 g. Find MM. ⭐ | 🔴 |
| 9.3c | **Statement I:** In Ostwald-Walker, the loss in mass of the solution container is proportional to the vapour pressure of the pure solvent.<br>**Statement II:** The CaCl₂ tube absorbs water vapour, and its gain equals the total vapour carried by the dry air.<br>Which is correct?<br> | 🔴 |
| 9.3d | **Statement I:** The Ostwald-Walker method can determine the molar mass of a non-volatile solute using only the gain in mass of the CaCl₂ tube and the loss in mass of the solution container.<br>**Statement II:** RLVP = (loss in solvent) / (gain in CaCl₂) = (CaCl₂ gain − solution loss) / (CaCl₂ gain). | 🟡 |
| 9.3e | **Assertion <br>
(A):** In the Ostwald-Walker experiment, the mass loss of the pure solvent container is always less than the mass loss of the solution container.<br>**Reason (R):** Pure solvent has a higher vapour pressure than the solution. | 🔴 |
| 9.3f | **Statement I:** If the CaCl₂ tube shows zero gain in the Ostwald-Walker experiment, the solution must be saturated.<br>**Statement II:** CaCl₂ absorbs all water vapour; zero gain means no vapour was carried by the air. | 🟡 |
| 9.3g | **Assertion <br>
(A):** Increasing the flow rate of dry air in the Ostwald-Walker experiment increases the measured RLVP value.<br>**Reason (R):** Faster air flow carries away more vapour, increasing the mass losses proportionally. | 🔴 |
| 9.3h | In an Ostwald-Walker experiment, dry air was bubbled successively through a solution containing 12 g of a non-volatile solute in 180 g water, then through pure water, and finally through a CaCl₂ drying tube. The loss in mass of the solution container was 3.60 g and the gain in mass of the CaCl₂ tube was 3.72 g. Calculate the molar mass of the solute. 🔴 ⭐ | 🔴 |
| 9.3i | An Ostwald-Walker experiment is set up with a solution containing 8.0 g of a non-volatile solute in 120 g of water. The loss in mass of the pure solvent container is 0.12 g, while the CaCl₂ tube gains 3.90 g. Determine the molar mass of the dissolved solute. 🔴 | 🔴 |
| 9.3j | In an Ostwald-Walker apparatus, 200 mL of water is used as the pure solvent. A solution bulb contains 25 g of a non-volatile solute dissolved in water. The mass loss of the solution bulb is 5.20 g and the mass loss of the pure solvent bulb is 0.08 g. Calculate the molar mass of the solute. (Density of water = 1 g/mL) 🔴 ⭐ | 🔴 |

<details>
<summary>💡 Solutions for Type 3</summary>

**9.3a:** RLVP = W₂/(W₁+W₂) = 0.04/2.54 = **0.01575**

**9.3b:** W₂ = 26.48 − 26 = 0.48 g (solvent loss); W₁+W₂ = 26.48 g
RLVP = 0.48/26.48 = 0.01813
n_H₂O = 250/18 = 13.89 mol
n_s/(n_s+13.89) = 0.01813 → n_s = 0.01813×13.89/0.98187 = 0.2564 mol
**MM = 20/0.2564 = 78.0 g/mol**

**9.3c → Statement I is False, Statement II is True.**
- Statement I is false: The loss in mass of the solution container is proportional to the VP of the **solution** (P_s), not the pure solvent.
- Statement II is true: The CaCl₂ tube is a desiccant — it absorbs all water vapour carried by the air stream.

**9.3d → Statement I is False, Statement II is True.**
- Statement I is false: You also need the loss in mass of the **solvent container** (or the CaCl₂ gain) to compute RLVP. Solution loss alone is insufficient.
- Statement II is true: RLVP = W₂/(W₁+W₂) where W₂ = CaCl₂ gain − solution loss.

**9.3e → Assertion is False, Reason is True.**
- A is false: The solution has **lower** VP, so less solvent evaporates from the solution container → solution loss is **less** than pure solvent loss (W₁ < W₂).
- R is true: Pure solvent has higher VP, so more evaporates.

**9.3f → Statement I is False, Statement II is True.**
- Statement I is false: Zero CaCl₂ gain means no air flowed through the apparatus or the CaCl₂ was exhausted, not that the solution is saturated.
- Statement II is true: CaCl₂ is a desiccant and absorbs water vapour completely.

**9.3g → Assertion is False, Reason is True.**
- A is false: RLVP = W₂/(W₁+W₂). Faster flow increases both W₁ and W₂ proportionally — the ratio RLVP remains unchanged.
- R is true: But both losses scale together, so the ratio is invariant to flow rate.

**9.3h:** CaCl₂ gain = W₁ + W₂ = 3.72 g; solution loss W₁ = 3.60 g
W₂ = 3.72 − 3.60 = 0.12 g
RLVP = W₂/(W₁+W₂) = 0.12/3.72 = 0.03226
n_H₂O = 180/18 = 10 mol
n_s/(n_s + 10) = 0.03226 → n_s = 0.03226 × 10 / (1 − 0.03226) = 0.3226/0.9677 = 0.3333 mol
**MM = 12/0.3333 = 36.0 g/mol**

**9.3i:** CaCl₂ gain = W₁ + W₂ = 3.90 g; W₂ = 0.12 g (solvent loss)
W₁ = 3.90 − 0.12 = 3.78 g
RLVP = W₂/(W₁+W₂) = 0.12/3.90 = 0.03077
n_H₂O = 120/18 = 6.667 mol
n_s/(n_s + 6.667) = 0.03077 → n_s = 0.03077 × 6.667 / 0.96923 = 0.2051/0.9692 = 0.2116 mol
**MM = 8.0/0.2116 = 37.8 g/mol**

**9.3j:** W₁ = 5.20 g, W₂ = 0.08 g (solvent loss directly given)
RLVP = W₂/(W₁+W₂) = 0.08/(5.20+0.08) = 0.08/5.28 = 0.01515
n_H₂O = 200/18 = 11.11 mol
n_s/(n_s + 11.11) = 0.01515 → n_s = 0.01515 × 11.11 / 0.98485 = 0.1683/0.9849 = 0.1709 mol
**MM = 25/0.1709 = 146.3 g/mol**
</details>

---

### Type 4: Direct ΔT_b Calculation

**Pattern:** Given m or W_solute and W_solvent → find ΔT_b and new boiling point.

#### Solved Example 9.4
**Q:** 6 g compound X in 100 g water. ΔT_b = 0.52°C. K_b = 0.52. Find MM of X. 🟢 ⭐

```
ΔT_b = K_b × m
0.52 = 0.52 × m
m = 1 mol/kg

m = W_solute/(MM × W_solvent_kg)
1 = 6/(MM × 0.1)
MM = 6/0.1 = 60 g/mol
```

#### Solved Example 9.5
**Q:** 1.8 g non-volatile solute in 90 g benzene. T_b rises from 353.23 K to 354.11 K. K_b = 2.53. Find MM. 🟡

```
ΔT_b = 354.11 − 353.23 = 0.88 K
m = ΔT_b/K_b = 0.88/2.53 = 0.3478 mol/kg

MM = W_solute/(m × W_solvent_kg) = 1.8/(0.3478 × 0.09) = 1.8/0.03130 = 57.5 g/mol
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 9.4a | 2.5×10⁻³ kg solute in 75×10⁻³ kg water. Solution boils at 373.535 K. K_b=0.52, T_b(water)=373.15 K. Find MM. ⭐ | 🟡 |
| 9.4b | 2 g non-volatile solute in 20 g water boils at 373.52 K (normal bp 373 K, K_b=0.52). Find MM. | 🟡 |
| 9.4c | What mass of sucrose (MM=342) must be added to 500 g water to raise bp by 0.37°C?<br> K_b=0.52. ⭐ | 🟡 |
| 9.4d | 3 g of X in 100 g CCl₄ raises bp by 0.60 K. K_b=5.0. Find MM. | 🟡 |
| 9.4e | **Assertion <br>
(A):** The boiling point of a 1 m aqueous glucose solution is 100.52°C.<br>**Reason (R):** $\Delta T_b = K_b \times m$, and $K_b$ for water is 0.52°C/m. | 🟢 |
| 9.4f | **Statement I:** If equal masses of two non-volatile solutes with different molar masses are dissolved in equal masses of the same solvent, the one with lower molar mass gives a higher $\Delta T_b$.<br>**Statement II:** $\Delta T_b$ is inversely proportional to the molar mass of the solute for a fixed mass of solute and solvent. | 🟡 |
| 9.4g | **Assertion <br>
(A):** $\Delta T_b$ for a solution depends on atmospheric pressure.<br>**Reason (R):** Boiling occurs when VP = external pressure; changing external pressure changes the boiling point of both pure solvent and solution. | 🔴 |
| 9.4h | **Statement I:** A 0.5 m solution in water and a 0.5 m solution in benzene have the same $\Delta T_b$.<br>**Statement II:** $\Delta T_b = K_b \times m$, and $K_b$ depends on the solvent. | 🟡 |
| 9.4i | A solution is prepared by dissolving 6.0 g of a non-volatile non-electrolyte solute in 100 g of water. The boiling point of this solution is measured as 100.52°C at 1 atm pressure. Given that the ebullioscopic constant of water is 0.52 K kg mol⁻¹ and the normal boiling point of water is 100°C, calculate the molar mass of the solute. 🟡 ⭐ | 🟡 |
| 9.4j | When 4.5 g of a non-volatile solute is dissolved in 75 g of benzene, the boiling point of the solution rises to 354.45 K. The normal boiling point of benzene is 353.23 K and its ebullioscopic constant is 2.53 K kg mol⁻¹. Determine the molar mass of the dissolved solute. 🔴 | 🔴 |
| 9.4k | How many grams of urea (molar mass 60 g/mol) must be added to 250 g of water so that the resulting solution boils at 100.78°C?<br> The ebullioscopic constant of water is 0.52 K kg mol⁻¹ and normal boiling point of water is 100°C. 🔴 ⭐ | 🔴 |

<details>
<summary>💡 Solutions for Type 4</summary>

**9.4a:** ΔT_b = 373.535−373.15 = 0.385 K; m = 0.385/0.52 = 0.7404 m
W_solute = 2.5×10⁻³ kg = 2.5 g; W_solvent = 75×10⁻³ kg = 0.075 kg
MM = W_s/(m×W_solv_kg) = 2.5/(0.7404×0.075) = 2.5/0.05553 = **45.0 g/mol**

**9.4b:** ΔT_b = 373.52−373 = 0.52 K; m = 0.52/0.52 = 1 m
MM = 2/(1×0.02) = **100 g/mol**

**9.4c:** m = ΔT_b/K_b = 0.37/0.52 = 0.7115 m
n = m×kg_solvent = 0.7115×0.5 = 0.3558 mol
**W_sucrose = 0.3558 × 342 = 121.7 g**

**9.4d:** m = 0.60/5.0 = 0.12 m
MM = 3/(0.12×0.1) = 3/0.012 = **250 g/mol**

**9.4e → Assertion is True, Reason is True, and R is the correct explanation.**
- 1 m glucose → ΔT_b = 0.52 × 1 = 0.52°C → boiling point = 100 + 0.52 = 100.52°C.

**9.4f → Statement I is True, Statement II is True.**
- n = W/MM, so lower MM → more moles → higher m → higher ΔT_b. Statement II correctly explains Statement I.

**9.4g → Assertion is False, Reason is True.**
- A is false: ΔT_b depends on K_b and m, not directly on atmospheric pressure.
- R is true: External pressure shifts both boiling points, but the *difference* ΔT_b remains unchanged (to a first approximation).

**9.4h → Statement I is False, Statement II is True.**
- Statement I is false: K_b(water) = 0.52, K_b(benzene) = 2.53, so ΔT_b differs even at the same molality.
- Statement II is true: K_b is a solvent-specific constant.

**9.4i:** ΔT_b = 100.52 − 100 = 0.52°C
m = ΔT_b / K_b = 0.52 / 0.52 = 1.0 mol/kg
MM = W_solute / (m × W_solvent_kg) = 6.0 / (1.0 × 0.1) = **60 g/mol**

**9.4j:** ΔT_b = 354.45 − 353.23 = 1.22 K
m = ΔT_b / K_b = 1.22 / 2.53 = 0.4822 mol/kg
MM = W_solute / (m × W_solvent_kg) = 4.5 / (0.4822 × 0.075) = 4.5 / 0.03617 = **124.4 g/mol**

**9.4k:** ΔT_b = 100.78 − 100 = 0.78°C
m = ΔT_b / K_b = 0.78 / 0.52 = 1.5 mol/kg
n_urea = m × kg_solvent = 1.5 × 0.250 = 0.375 mol
**W_urea = 0.375 × 60 = 22.5 g**
</details>

---

### Type 5: Ratio of ΔT_b for Different Solvents

**Pattern:** Same solute, same mass, different solvents or different K_b values.

#### Solved Example 9.6
**Q:** 1 g solute in 100 g each of solvents A and B (K_b ratio = 1:5). Find ratio of ΔT_b. 🟡

```
ΔT_b = K_b × m; same solute and same concentration
→ ΔT_b ∝ K_b

ΔT_b<br>
(A)/ΔT_b<br>
(B) = K_b<br>
(A)/K_b<br>
(B) = 1:5
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 9.5a | 2 g solute in 200 g solvent A and 200 g solvent B. K_b ratio = 1:8. Find ratio of ΔT_b. ⭐ | 🟡 |
| 9.5b | Two solvents X and Y have same MM. T_b ratio = 2:1, ΔH_vap ratio = 1:2. K_b(X) = m × K_b(Y). Find m. | 🔴 |
| 9.5c | **Assertion <br>
(A):** If the same mass of the same solute is dissolved in equal masses of two different solvents, the ratio of ΔT_b equals the ratio of their K_b values.<br>**Reason (R):** ΔT_b = K_b × m, and m is the same when solute mass and solvent mass are equal. | 🟢 |
| 9.5d | **Statement I:** K_b for a solvent increases with its boiling point.<br>**Statement II:** $K_b = \frac{M R T_b^2}{1000 \Delta H_{vap}}$, so $K_b \propto T_b^2$. | 🟡 |
| 9.5e | **Assertion <br>
(A):** Water has a lower K_b (0.52) than benzene (2.53), so the same solution in water shows a smaller ΔT_b than in benzene.<br>**Reason (R):** K_b is inversely related to ΔH_vap; water has a much higher ΔH_vap than benzene. | 🟡 |
| 9.5f | **Statement I:** If two solvents have the same boiling point and same molar mass, the one with higher ΔH_vap has a lower K_b.<br>**Statement II:** $K_b \propto 1/\Delta H_{vap}$ when all other factors are equal. | 🟡 |
| 9.5g | **Assertion <br>
(A):** The ebullioscopic constant of a solvent can be determined without knowing the solute's identity.<br>**Reason (R):** K_b depends only on solvent properties (M, T_b, ΔH_vap), not on the solute. | 🟢 |
| 9.5h | The same non-volatile solute (2.0 g) is dissolved separately in 100 g of water (K_b = 0.52) and 100 g of benzene (K_b = 2.53). The molar mass of the solute is 100 g/mol. Calculate the ratio of the boiling point elevations observed in the two solvents. | 🟡 |
| 9.5i | An organic compound is dissolved in two different solvents: (i) 3.0 g in 50 g of water (K_b = 0.52, bp 100°C), and (ii) 3.0 g in 50 g of chloroform (K_b = 3.63, bp 61.2°C). If the observed ΔT_b in water is 0.312°C, calculate the ΔT_b in chloroform for the same solute mass and solvent mass. 🔴 | 🔴 |
| 9.5j | Solvent P has a boiling point 400 K and ΔH_vap of 30 kJ/mol. Solvent Q has a boiling point 500 K and ΔH_vap of 40 kJ/mol. Both solvents have the same molar mass. Which solvent has the larger K_b value and by what factor?<br> 🔴 ⭐ | 🔴 |

<details>
<summary>💡 Solutions for Type 5</summary>

**9.5a:** Same mass and concentration → ΔT_b ∝ K_b → **ΔT_b<br>
(A):ΔT_b<br>
(B) = 1:8** → value of y = 8

**9.5b:** K_b = (M_solvent × R × T_b²)/(ΔH_vap × 1000)
K_b(X)/K_b(Y) = (T_b_X/T_b_Y)² × (ΔH_Y/ΔH_X) = (2)² × (2/1) = 4×2 = 8
(Since T_b_X = 2T_b_Y and ΔH_X = ΔH_Y/2)
**m = 8**

**9.5c → Assertion is True, Reason is True, and R is the correct explanation.**
- Same solute, same mass, same solvent mass → same molality m → ΔT_b ∝ K_b.

**9.5d → Statement I is True, Statement II is True.**
- Higher T_b gives a larger K_b since K_b ∝ T_b². But note that ΔH_vap also typically increases with T_b, which partially offsets the increase.

**9.5e → Assertion is True, Reason is True, and R is the correct explanation.**
- Water has ΔH_vap ≈ 40.7 kJ/mol, benzene ≈ 30.7 kJ/mol. Higher ΔH_vap → lower K_b.

**9.5f → Statement I is True, Statement II is True.**
- With T_b and M equal, K_b ∝ 1/ΔH_vap. Higher ΔH_vap → lower K_b.

**9.5g → Assertion is True, Reason is True, and R is the correct explanation.**
- K_b is a solvent property. It can be calculated from M, T_b, and ΔH_vap of the pure solvent.

**9.5h:** For water: m = 2.0/(100 × 0.1) = 0.2 m; ΔT_b(H₂O) = 0.52 × 0.2 = 0.104°C
For benzene: m = 2.0/(100 × 0.1) = 0.2 m; ΔT_b(benzene) = 2.53 × 0.2 = 0.506°C
**Ratio ΔT_b(H₂O) : ΔT_b(benzene) = 0.104 : 0.506 = 1 : 4.865 ≈ 1 : 4.87**

**9.5i:** For water: m = 3.0/(MM × 0.05); ΔT_b = 0.52 × m = 0.312
m = 0.312/0.52 = 0.6 m → MM = 3.0/(0.6 × 0.05) = 100 g/mol
For chloroform: m = 3.0/(100 × 0.05) = 0.6 m
**ΔT_b(chloroform) = 3.63 × 0.6 = 2.178°C**

**9.5j:** K_b ∝ T_b²/ΔH_vap
K_b(P) ∝ (400)²/30 = 160000/30 = 5333.3
K_b(Q) ∝ (500)²/40 = 250000/40 = 6250
**K_b(Q)/K_b(P) = 6250/5333.3 = 1.172**
Solvent Q has a larger K_b by a factor of **1.17**.
</details>

---

### Type 6: Electrolytes & van't Hoff Factor

**Pattern:** Compute boiling point elevation for electrolytes using $i$, or find degree of dissociation ($\alpha$) from $\Delta T_b$ data.

#### Solved Example 9.7
**Q:** 0.1 M NaCl dissociates 90% in water. Find its boiling point elevation. K_b = 0.52, assume 1 M ≈ 1 m. 🟡 ⭐

```
NaCl → Na⁺ + Cl⁻  (ν = 2)
α = 0.9
i = 1 + α(ν − 1) = 1 + 0.9(2−1) = 1.9
ΔT_b = i × K_b × m = 1.9 × 0.52 × 0.1 = 0.0988°C
```

#### Solved Example 9.8
**Q:** A 0.5 m aqueous solution of CaCl₂ boils at 100.78°C. Find the degree of dissociation of CaCl₂. K_b = 0.52. 🔴 ⭐

```
ΔT_b = 100.78 − 100 = 0.78°C
Observed m_eff = ΔT_b / K_b = 0.78 / 0.52 = 1.5 m
Expected m (no dissociation) = 0.5 m
i = observed m / expected m = 1.5 / 0.5 = 3

CaCl₂ → Ca²⁺ + 2Cl⁻ (ν = 3)
i = 1 + α(ν − 1) → 3 = 1 + α(3−1) → 2α = 2 → α = 1.0 (100% dissociated)
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 9.6a | 0.2 m NaCl (100% dissociated) in water. Find ΔT_b. K_b = 0.52. | 🟢 |
| 9.6b | 0.1 m K₂SO₄ solution shows ΔT_b = 0.156°C. Find van't Hoff factor i. K_b = 0.52. ⭐ | 🟡 |
| 9.6c | **Statement I:** The boiling point of 0.1 m NaCl is higher than that of 0.1 m glucose.<br>**Statement II:** NaCl dissociates into two ions, doubling the number of particles. | 🟡 |
| 9.6d | **Statement I:** For a partially dissociated electrolyte, the van't Hoff factor i lies between 1 and ν.<br>**Statement II:** i = 1 + α(ν − 1), and 0 ≤ α ≤ 1. | 🟢 |
| 9.6e | 0.1 m acetic acid (ν = 2) in water boils at 100.054°C. Find its degree of dissociation. K_b = 0.52. ⭐ | 🔴 |
| 9.6f | 0.05 m AlCl₃ (ν = 4) in water. Observed ΔT_b = 0.104°C. Find α. K_b = 0.52. | 🔴 |
| 9.6g | **Assertion <br>
(A):** 0.1 m NaCl and 0.1 m CaCl₂ solutions have the same boiling point elevation.<br>**Reason (R):** Both are strong electrolytes that dissociate completely in water. | 🟡 |
| 9.6h | **Statement I:** For an associated solute (e.g., dimerization in benzene), the van't Hoff factor i is less than 1.<br>**Statement II:** Association reduces the effective number of particles in solution. | 🟡 |
| 9.6i | **Assertion <br>
(A):** The observed molar mass of NaCl in water is approximately half its formula mass.<br>**Reason (R):** NaCl dissociates into Na⁺ and Cl⁻, doubling the particle count, and i = 2 = MM_theoretical / MM_observed. | 🟡 |
| 9.6j | **Statement I:** For a 0.01 m NaCl solution, ΔT_b is approximately 0.0104°C.<br>**Statement II:** ΔT_b for electrolytes = i × K_b × m, and for NaCl i ≈ 2. | 🟡 |
| 9.6k | A 0.2 molal aqueous solution of potassium chloride (KCl) is prepared. Given that KCl is a strong electrolyte and dissociates completely, and the ebullioscopic constant of water is 0.52 K kg mol⁻¹, calculate the boiling point elevation of this solution. | 🟢 |
| 9.6l | 1.17 g of sodium chloride (NaCl, molar mass 58.5 g/mol) is dissolved in 200 g of water. The boiling point of the resulting solution is measured as 100.104°C. Assuming complete dissociation of NaCl, calculate the observed van't Hoff factor. (K_b for water = 0.52 K kg mol⁻¹, normal boiling point of water = 100°C). 🔴 ⭐ | 🔴 |
| 9.6m | A 0.05 molal aqueous solution of magnesium chloride (MgCl₂) boils at 100.039°C. The normal boiling point of water is 100°C and K_b for water is 0.52 K kg mol⁻¹. Calculate the degree of dissociation of MgCl₂ in this solution. 🔴 ⭐ | 🔴 |

<details>
<summary>💡 Solutions for Type 6</summary>

**9.6a:** NaCl → ν = 2, 100% dissociated → i = 2
ΔT_b = 2 × 0.52 × 0.2 = **0.208°C**

**9.6b:** ΔT_b = i × K_b × m → i = ΔT_b / (K_b × m) = 0.156 / (0.52 × 0.1) = 0.156 / 0.052 = **3.0**
(K₂SO₄ → 2K⁺ + SO₄²⁻, ν = 3. i = 3 means complete dissociation.)

**9.6c → Both statements are true, and Statement II correctly explains Statement I.**
- 0.1 m NaCl (i = 2) → effective molality = 0.2 m → ΔT_b = 0.104°C
- 0.1 m glucose (i = 1) → ΔT_b = 0.052°C
- NaCl dissociates → more particles → higher ΔT_b.

**9.6d → Both statements are true, and Statement II correctly explains Statement I.**
- When α = 0 (no dissociation), i = 1. When α = 1 (complete), i = ν. For partial, 1 < i < ν.

**9.6e:** ΔT_b = 100.054 − 100 = 0.054°C
i = ΔT_b / (K_b × m) = 0.054 / (0.52 × 0.1) = 0.054 / 0.052 = 1.038
CH₃COOH ⇌ CH₃COO⁻ + H⁺, ν = 2
i = 1 + α(ν − 1) → α = (i − 1)/(ν − 1) = 0.038/1 = **0.038 (3.8% dissociated)**

**9.6f:** ΔT_b = i × K_b × m → i = 0.104 / (0.52 × 0.05) = 0.104 / 0.026 = 4.0
AlCl₃ → Al³⁺ + 3Cl⁻, ν = 4. i = 4 → α = (i − 1)/(ν − 1) = 3/3 = **1.0 (100% dissociated)**

**9.6g → Assertion is False, Reason is True.**
- A is false: NaCl (ν=2, i=2) gives ΔT_b = 2×0.52×0.1 = 0.104°C. CaCl₂ (ν=3, i=3) gives ΔT_b = 3×0.52×0.1 = 0.156°C. Different ΔT_b.
- R is true: Both are strong electrolytes and dissociate completely.

**9.6h → Statement I is True, Statement II is True.**
- Association (e.g., 2HA ⇌ (HA)₂) reduces particle count. If all molecules dimerize, i ≈ 0.5. i < 1 is the hallmark of association.

**9.6i → Assertion is True, Reason is True, and R is the correct explanation.**
- MM_observed = MM_theoretical / i = 58.5 / 2 ≈ 29.25 g/mol. Since i = 2, observed MM is half.

**9.6j → Statement I is True, Statement II is True.**
- For 0.01 m NaCl: i ≈ 2, ΔT_b = 2 × 0.52 × 0.01 = 0.0104°C. Both statements are correct.

**9.6k:** KCl → K⁺ + Cl⁻, ν = 2, complete dissociation → i = 2
ΔT_b = i × K_b × m = 2 × 0.52 × 0.2 = **0.208°C**

**9.6l:** n_NaCl = 1.17/58.5 = 0.02 mol
m = 0.02/0.2 = 0.1 mol/kg
ΔT_b = 100.104 − 100 = 0.104°C
If no dissociation: ΔT_b(expected) = K_b × m = 0.52 × 0.1 = 0.052°C
**i = ΔT_b(observed) / ΔT_b(expected) = 0.104 / 0.052 = 2.0**
(Complete dissociation confirmed)

**9.6m:** ΔT_b = 100.039 − 100 = 0.039°C
ΔT_b = i × K_b × m → i = 0.039 / (0.52 × 0.05) = 0.039 / 0.026 = 1.5
MgCl₂ → Mg²⁺ + 2Cl⁻, ν = 3
i = 1 + α(ν − 1) → 1.5 = 1 + α(3 − 1) → 0.5 = 2α
**α = 0.25 (25% dissociated)**

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 9.M1 | 18 g glucose in 180 g water. Find: (a) RLVP if P°=23.8 torr, (b) ΔT_b (K_b=0.52), (c) new boiling point. ⭐ | T1+T4 | 🟡 |
| 9.M2 | A solution of urea (MM=60) boils at 100.52°C. Find: (a) molality, (b) mass of urea in 500 g water, (c) RLVP if P°=760 mm at 100°C. | T4+T1 | 🔴 |
| 9.M3 | From Ostwald-Walker: loss in solution = 2.5, loss in solvent = 0.04. Solution: 5g solute in 80g water. Find MM and ΔT_b (K_b=0.52). | T3+T4 | 🔴 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**9.M1:**
- n_glucose = 18/180 = 0.1; n_H₂O = 10; χ_glucose = 0.1/10.1 = 0.00990
- **(a) RLVP = 0.00990; ΔP = 23.8×0.00990 = 0.236 torr; P_s = 23.564 torr**
- m = 0.1/0.18 = 0.5556 m
- **(b) ΔT_b = 0.52×0.5556 = 0.289°C**
- **(c) New bp = 100 + 0.289 = 100.289°C**

**9.M2:**
- ΔT_b = 100.52−100 = 0.52°C; **(a) m = ΔT_b/K_b = 0.52/0.52 = 1 molal**
- **(b) n = 1×0.5 = 0.5 mol; W_urea = 0.5×60 = 30 g**
- n_urea = 0.5; n_H₂O = 500/18 = 27.78; χ_urea = 0.5/28.28 = 0.01769
- **(c) RLVP = 0.01769; ΔP = 760×0.01769 = 13.44 mm**

**9.M3:**
- From 9.3a: RLVP = 0.04/2.54 = 0.01575; MM = 70 g/mol (from solved example)
- m = W_s/(MM×W_solvent_kg) = 5/(70×0.08) = 5/5.6 = 0.893 m
- **ΔT_b = 0.52×0.893 = 0.464°C**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 9.B1 | Define relative lowering of vapour pressure. How is it related to mole fraction of solute?<br> *(NCERT)* | 🟢 |
| 9.B2 | The boiling point of benzene is 353.23 K. 1.8 g non-volatile solute dissolved in 90 g benzene raises bp to 354.1 K. Find MM. (K_b = 2.53) *(NCERT)* ⭐ | 🟡 |
| 9.B3 | Calculate the mass of urea needed to reduce VP of water by 25% at some temperature. MM_urea = 60. ⭐ | 🔴 |
| 9.B4 | At 25°C VP of water = 17.54 mm. When 20 g of glucose is dissolved in 180 g of water, VP drops to 17.44 mm. Verify Raoult's Law. | 🟡 |
| 9.B5 | Why is boiling point elevation called a colligative property?<br> | 🟢 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**9.B1:** RLVP = (P° − P_s)/P° = χ_solute. It equals the mole fraction of the non-volatile solute.

**9.B2:** ΔT_b = 354.1 − 353.23 = 0.87 K
m = 0.87/2.53 = 0.3439 m
MM = 1.8/(0.3439×0.09) = 1.8/0.03095 = **58.2 g/mol ≈ 58 g/mol**

**9.B3:** 25% VP drop → RLVP = 0.25 = χ_urea
χ_urea = n_u/(n_u + n_H₂O) = 0.25 → 0.75n_u = 0.25×n_H₂O
For 1000 g water: n_H₂O = 55.56; n_u = 0.25×55.56/0.75 = 18.52 mol
**W_urea = 18.52 × 60 = 1111 g per 1000 g water**

**9.B4:** n_glucose = 20/180 = 0.111; n_H₂O = 180/18 = 10
χ_glucose = 0.111/10.111 = 0.01098; χ_water = 0.98902
P_s (predicted) = 17.54 × 0.98902 = 17.35 mm ≈ 17.44 mm *(close but slight discrepancy due to rounding — the principle holds)*

**9.B5:** ΔT_b depends only on the number (molality) of solute particles, not their chemical nature. Adding 1 mol of glucose or 1 mol of urea to 1 kg water gives the same ΔT_b = 0.52°C. It is collective (depends on collection of particles) → colligative.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q9.J1 🟡 ⭐**
RLVP of a dilute aqueous solution = 0.0125. Molality of the solution is:
<br>
(A) 0.70 m  <br>
(B) 1.0 m  <br>
(C)
 0.50 m  <br>
(D) 0.35 m

**Q9.J2 🟡 ⭐**
Elevation in boiling point = 0.52°C when 6 g of compound X is dissolved in 100 g water (K_b = 0.52). Molecular weight of X is:
<br>
(A) 30 g/mol  <br>
(B) 60 g/mol  <br>
(C)
 120 g/mol  <br>
(D) 180 g/mol

**Q9.J3 🔴**
1 g non-volatile solute in 100 g each of solvents A and B. K_b<br>
(A):K_b<br>
(B) = 1:5. ΔT_b<br>
(A)/ΔT_b<br>
(B) = ?<br>
<br>
(A) 1:25  <br>
(B) 1:5  <br>
(C)
 5:1  <br>
(D) 25:1

**Q9.J4 🔴 ⭐**
At what external pressure would a 1 molal glucose solution boil at 100°C?<br> (K_b of water = 0.52, normal bp of water = 100°C at 1 atm)
<br>
(A) > 1 atm  <br>
(B) < 1 atm  <br>
(C)
 = 1 atm  <br>
(D) Cannot determine

**Q9.J5 🔴 ⭐**
The vapour pressure of an aqueous solution of glucose is 750 mm at the temperature where VP of pure water is 760 mm. The boiling point elevation (K_b = 0.52 for water) is approximately:
<br>
(A) 0.69°C  <br>
(B) 0.52°C  <br>
(C)
 1.0°C  <br>
(D) 0.35°C

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**9.J1 → Answer: <br>
(A)**
- χ_solute = 0.0125; χ_H₂O = 0.9875
- m = (0.0125×1000)/(0.9875×18) = 12.5/17.775 = **0.703 m ≈ 0.70 m ✓**

**9.J2 → Answer: <br>
(B)**
- ΔT_b = 0.52; m = ΔT_b/K_b = 1; MM = 6/(1×0.1) = **60 g/mol ✓**

**9.J3 → Answer: <br>
(B)**
- Same molality → ΔT_b ∝ K_b → **ratio = 1:5 ✓**

**9.J4 → Answer: <br>
(B)**
- 1 molal glucose → ΔT_b = 0.52°C → solution boils at 100.52°C at 1 atm.
- To make it boil at 100°C (lower temperature), we need to **reduce external pressure below 1 atm**
- This lowers the required VP → solution boils at lower temperature.
- **Answer: < 1 atm ✓**

**9.J5 → Answer: <br>
(D)**
- RLVP = (760−750)/760 = 10/760 = 0.01316 = χ_solute
- χ_H₂O = 0.98684; m = (0.01316×1000)/(0.98684×18) = 13.16/17.763 = 0.7408 m
- **ΔT_b = 0.52 × 0.7408 = 0.385°C**
- *(Closest to option <br>
(D) 0.35°C)*
</details>

---

## Key Takeaways from Chapter 9

| Formula | Use |
|---------|-----|
| RLVP = χ_solute | Standard RLVP |
| (P°−P_s)/P_s = n_s/n_solv | Finding unknown molar mass |
| ΔT_b = K_b × m | Boiling point elevation |
| MM = W_s/(m × W_solv_kg) | Finding MM from ΔT_b |
| K_b(water) = 0.52 K·kg/mol | Common exam value |
| K_b(benzene) = 2.53 K·kg/mol | Second most common |

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
| 9.S1 | **Assertion <br>
(A):** The boiling point of a solvent is always lower than the boiling point of its solution containing a non-volatile solute.<br>**Reason (R):** The addition of a non-volatile solute lowers the vapour pressure of the solvent. | 🟢 |
| 9.S2 | **Statement I:** The ebullioscopic constant ($K_b$) of a solvent depends on the nature of the solute dissolved in it.<br>**Statement II:** $K_b$ is the elevation in boiling point when one mole of solute is dissolved in $1000\text{ g}$ of solvent. | 🟡 |
| 9.S3 | **Assertion <br>
(A):** Relative lowering of vapour pressure ($\Delta P / P^\circ$) is a dimensionless quantity.<br>**Reason (R):** It is equal to the mole fraction of the solute, which is a ratio of moles. | 🟢 |
| 9.S4 | **Statement I:** If $1\text{ mole}$ of urea and $1\text{ mole}$ of glucose are separately dissolved in $1\text{ kg}$ of water, the boiling point elevation will be the same in both cases.<br>**Statement II:** Elevation of boiling point is a colligative property and depends only on the molar mass of the solute. | 🟡 |
| 9.S5 | **Assertion <br>
(A):** The formula $\Delta T_b = K_b \times m$ is strictly valid only for dilute solutions.<br>**Reason (R):** In concentrated solutions, intermolecular forces between solute particles cause deviations from ideal colligative behavior. | 🟡 |
| 9.S6 | **Statement I:** In the Ostwald-Walker experiment, the loss of mass in the solution container is proportional to the vapour pressure of the pure solvent ($P^\circ$).<br>**Statement II:** The dry air absorbs vapour until it reaches the equilibrium vapour pressure of the liquid it passes through. | 🔴 |
| 9.S7 | **Assertion <br>
(A):** A $1\text{ M}$ (molar) solution of glucose will have a higher boiling point than a $1\text{ m}$ (molal) solution of glucose in water ($d = 1.05\text{ g/mL}$).<br>**Reason (R):** For an aqueous solution with density $> 1\text{ g/mL}$, Molarity is numerically greater than Molality. | 🔴 |
| 9.S8 | **Statement I:** When a volatile solute is added to a volatile solvent, the boiling point of the solution is always elevated.<br>**Statement II:** Colligative properties apply exclusively to non-volatile solutes. | 🟡 |
| 9.S9 | **Assertion <br>
(A):** The value of $K_b$ for water is $0.52\text{ K kg mol}^{-1}$. This means boiling $1\text{ kg}$ of water requires $0.52\text{ Joules}$ of energy.<br>**Reason (R):** $K_b$ is defined as $\frac{R T_b^2}{1000 \Delta H_{vap}}$. | 🟢 |
| 9.S10 | **Statement I:** The modified relative lowering of vapour pressure formula $\frac{P^\circ - P_s}{P_s} = \frac{n_{solute}}{n_{solvent}}$ is more accurate for calculating molar mass than the standard formula.<br>**Statement II:** The standard formula requires approximating $n_{solute} + n_{solvent} \approx n_{solvent}$, whereas the modified formula requires no such approximation. | 🟡 |
| 9.S11 | **Assertion <br>
(A):** If the external pressure on a solution is increased, its boiling point elevation ($\Delta T_b$) also increases.<br>**Reason (R):** Higher external pressure increases the boiling point of both the pure solvent and the solution. | 🔴 |
| 9.S12 | **Statement I:** The unit of $K_b$ can be written as $\text{K kg mol}^{-1}$ or $^\circ\text{C kg mol}^{-1}$.<br>**Statement II:** A change of $1\text{ Kelvin}$ is exactly equal to a change of $1^\circ\text{C}$. | 🟢 |
| 9.S13 | **Assertion <br>
(A):** Adding $10\text{ g}$ of sucrose ($MM = 342$) to water will elevate the boiling point less than adding $10\text{ g}$ of urea ($MM = 60$) to the same amount of water.<br>**Reason (R):** Urea has a lower molar mass, so $10\text{ g}$ of urea contains more particles than $10\text{ g}$ of sucrose. | 🟢 |
| 9.S14 | **Statement I:** Lowering of vapour pressure ($\Delta P$) is a colligative property.<br>**Statement II:** Relative lowering of vapour pressure ($\Delta P / P^\circ$) is a colligative property. | 🟡 |
| 9.S15 | **Assertion <br>
(A):** In the formula $K_b = \frac{M_{solvent} R T_b^2}{1000 \Delta H_{vap}}$, the temperature $T_b$ must be in Kelvin.<br>**Reason (R):** The universal gas constant $R$ involves Kelvin in its units. | 🟢 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**9.S1 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is the fundamental premise of boiling point elevation. Lower VP means you must heat it more to reach atmospheric pressure.

**9.S2 → Statement I is False, Statement II is True.**
- Statement I is false: $K_b$ is a property of the SOLVENT ONLY. It does not depend on the solute.
- Statement II is true: This is the definition of $K_b$ (molal elevation constant).

**9.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Pressure / Pressure = dimensionless. Moles / Moles = dimensionless.

**9.S4 → Statement I is True, Statement II is False.**
- Statement I is true: Both are $1\text{ m}$ solutions of non-electrolytes. Same particles = same $\Delta T_b$.
- Statement II is false: Colligative properties depend on the NUMBER of particles, NOT the molar mass of the solute directly (though you use MM to find the number of particles).

**9.S5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- At high concentrations, solute-solute interactions and changes in solvent structure cause deviations from simple linear colligative behavior.

**9.S6 → Statement I is False, Statement II is True.**
- Statement I is false: The loss in mass of the solution container is proportional to the vapour pressure of the SOLUTION ($P_s$), not the pure solvent. The pure solvent container loses mass proportional to $(P^\circ - P_s)$.
- Statement II is true: The air gets saturated to the local VP.

**9.S7 → Answer: <br>
(C)
 A is true but R is false.**
- A $1\text{ M}$ glucose solution has $d > 1$, so $m > M$:
  $m = \frac{1000 M}{1000 d - M \cdot MM} = \frac{1000}{1050 - 180} = 1.15\text{ m}$.
- Since $1.15\text{ m} > 1\text{ m}$, the $1\text{ M}$ solution has a higher boiling point. **Assertion is true.**
- Reason claims "Molarity > Molality" — the calculation shows $m = 1.15 > M = 1$. **Reason is false.**

**9.S8 → Statement I is False, Statement II is True.**
- Statement I is false: If the solute is MORE volatile than the solvent (e.g., adding ethanol to water), the boiling point of the mixture is LOWERED, not elevated.
- Statement II is true: Standard colligative property derivations assume the solute does not contribute to the vapour pressure.

**9.S9 → Answer: <br>
(D) A is false but R is true.**
- A is false: $K_b = 0.52$ means a $1\text{ molal}$ solution boils at a temperature $0.52\text{ K}$ higher. It has nothing to do with Joules of energy required to boil.
- R is true: This is the thermodynamic derivation of $K_b$.

**9.S10 → Statement I is True, Statement II is True.**
- Both statements are true and correctly relate the advantage of the modified formula.

**9.S11 → Answer: <br>
(D) A is false but R is true.**
- A is false: $\Delta T_b$ depends only on molality and $K_b$. Changing external pressure shifts both the solvent BP and solution BP up, but the *difference* ($\Delta T_b$) remains roughly constant (at least to a first approximation, technically $K_b$ varies slightly with BP, but standard curriculum says $\Delta T_b$ is dependent only on m).
- R is true: Higher external pressure means you must reach a higher VP to boil, elevating both boiling points.

**9.S12 → Statement I is True, Statement II is True.**
- A temperature *difference* ($\Delta T$) of $1\text{ K}$ is exactly the same as a difference of $1^\circ\text{C}$. Since $K_b$ relates to $\Delta T_b$, either unit is perfectly valid.

**9.S13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Moles of sucrose = $10/342 = 0.029$. Moles of urea = $10/60 = 0.167$.
- More moles $\rightarrow$ higher molality $\rightarrow$ greater $\Delta T_b$.

**9.S14 → Statement I is False, Statement II is True.**
- Statement I is false: Lowering of VP ($\Delta P$) equals $P^\circ \chi_{solute}$. Since it depends on $P^\circ$ (nature of solvent), it is not strictly a colligative property on its own.
- Statement II is true: $\Delta P / P^\circ = \chi_{solute}$, which depends purely on the number fraction of particles.

**9.S15 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Thermodynamic derivations require absolute temperature (Kelvin).
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q9.M1 🟢**
Which of the following has the highest boiling point?<br> (Assume complete dissociation for electrolytes).
<br>
(A) $0.1\text{ M}$ Glucose
<br>
(B) $0.1\text{ M}$ Urea
<br>
(C)
 $0.1\text{ M}$ Sucrose
<br>
(D) All have the same boiling point

**Q9.M2 🟡 (The "Temperature Addition" Trap)**
A solution of a non-volatile solute in water exhibits an elevation in boiling point of $0.52^\circ\text{C}$. What is the new boiling point of the solution in Kelvin?<br>
<br>
(A) $100.52\text{ K}$
<br>
(B) $373.15\text{ K}$
<br>
(C)
 $373.67\text{ K}$
<br>
(D) $0.52\text{ K}$

**Q9.M3 🔴**
An aqueous solution of a non-volatile solute boils at $100.26^\circ\text{C}$. The $K_b$ for water is $0.52\text{ K kg mol}^{-1}$. What is the relative lowering of vapour pressure ($\Delta P / P^\circ$) for this solution?<br>
<br>
(A) $0.009$
<br>
(B) $0.50$
<br>
(C)
 $0.018$
<br>
(D) $0.005$

**Q9.M4 🟡**
If $K_b$ for water is $0.52\text{ K kg mol}^{-1}$, what is the boiling point elevation when $0.1\text{ mole}$ of solute is dissolved in $100\text{ mL}$ of water?<br> (Density of water = $1\text{ g/mL}$).
<br>
(A) $0.052^\circ\text{C}$
<br>
(B) $0.52^\circ\text{C}$
<br>
(C)
 $5.2^\circ\text{C}$
<br>
(D) $0.0052^\circ\text{C}$

**Q9.M5 🟡 (The "Missing Solvent Data" Trap)**
You are given the elevation in boiling point ($\Delta T_b$) and the mass of the solute and solvent. To find the molar mass of the solute, what else MUST you know?<br>
<br>
(A) The boiling point of the pure solvent
<br>
(B) The $K_b$ of the solvent
<br>
(C)
 The atmospheric pressure
<br>
(D) The density of the solution

**Q9.M6 🔴**
In an Ostwald-Walker experiment, the loss in mass of the solution bulbs is $1.2\text{ g}$, and the loss in mass of the solvent bulbs is $0.05\text{ g}$. What is the relative lowering of vapour pressure?<br>
<br>
(A) $0.05 / 1.2$
<br>
(B) $1.2 / 1.25$
<br>
(C)
 $0.05 / 1.25$
<br>
(D) $0.05 / 1.15$

**Q9.M7 🟡**
$10\text{ g}$ of solute A ($MM = 100$) and $20\text{ g}$ of solute B ($MM = 200$) are dissolved in the same mass of identical solvent in separate beakers. The ratio of their boiling point elevations ($\Delta T_{b<br>
(A)} : \Delta T_{b<br>
(B)}$) is:
<br>
(A) $1:2$
<br>
(B) $2:1$
<br>
(C)
 $1:1$
<br>
(D) $1:4$

**Q9.M8 🟢**
The unit of ebullioscopic constant ($K_b$) is:
<br>
(A) $\text{K kg mol}^{-1}$
<br>
(B) $\text{K mol kg}^{-1}$
<br>
(C)
 $\text{K kg}^{-1} \text{mol}$
<br>
(D) $\text{K}^{-1} \text{kg mol}$

**Q9.M9 🔴 (The "Formula Confusion" Trap)**
A student incorrectly uses the formula $\frac{\Delta P}{P^\circ} = \frac{n_2}{n_1}$ instead of $\frac{\Delta P}{P_s} = \frac{n_2}{n_1}$ to calculate the molar mass of a solute from experimental RLVP data. How will their calculated molar mass compare to the true molar mass?<br>
<br>
(A) Calculated MM will be exactly correct.
<br>
(B) Calculated MM will be too high.
<br>
(C)
 Calculated MM will be too low.
<br>
(D) Depends on the temperature.

**Q9.M10 🟡**
Two solvents X and Y have boiling points $T_X$ and $T_Y$ such that $T_X = 2 T_Y$ (in Kelvin). Their latent heats of vaporization ($\Delta H_{vap}$) are equal. If their molar masses are also equal, what is the ratio of their $K_b$ values ($K_{b(X)} : K_{b(Y)}$)?<br>
<br>
(A) $2:1$
<br>
(B) $4:1$
<br>
(C)
 $1:2$
<br>
(D) $1:4$

**Q9.M11 🔴**
An aqueous solution contains $5\%$ by mass of urea ($MM = 60$) and $10\%$ by mass of glucose ($MM = 180$). What is the boiling point of this solution?<br> ($K_b = 0.52^\circ\text{C/m}$).
<br>
(A) $100.72^\circ\text{C}$
<br>
(B) $100.52^\circ\text{C}$
<br>
(C)
 $100.85^\circ\text{C}$
<br>
(D) $101.2^\circ\text{C}$

**Q9.M12 🟡**
If the mole fraction of a non-volatile solute in an aqueous solution is $0.1$, what is the relative lowering of vapour pressure?<br>
<br>
(A) $0.9$
<br>
(B) $0.1$
<br>
(C)
 $100$
<br>
(D) Cannot be determined without $P^\circ$

**Q9.M13 🟢**
Boiling point elevation ($\Delta T_b$) is directly proportional to:
<br>
(A) Molarity
<br>
(B) Molality
<br>
(C)
 Mole fraction of solvent
<br>
(D) Normal boiling point

**Q9.M14 🔴 (The "Latent Heat Units" Trap)**
To calculate $K_b$ using $K_b = \frac{M \cdot R \cdot T_b^2}{1000 \cdot \Delta H_{vap}}$, if $R$ is used as $8.314\text{ J/(mol K)}$ and $\Delta H_{vap}$ is in $\text{J/mol}$, what must be the unit of $M$ (molar mass of solvent)?<br>
<br>
(A) $\text{kg/mol}$
<br>
(B) $\text{g/mol}$
<br>
(C)
 dimensionless
<br>
(D) $M$ is not used, $W_{solvent}$ is used.

**Q9.M15 🟡**
A solution of a polymer (unknown, very high MM) shows a boiling point elevation of $0.001^\circ\text{C}$. Which colligative property would be best to accurately determine its molar mass?<br>
<br>
(A) Elevation of boiling point
<br>
(B) Depression of freezing point
<br>
(C)
 Relative lowering of vapour pressure
<br>
(D) Osmotic pressure

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q9.M1 → Answer: <br>
(D)**
- All are $0.1\text{ M}$ non-electrolytes. Since they do not dissociate ($i=1$), they produce the same number of particles in solution.
- Same particle concentration = same $\Delta T_b$.

**Q9.M2 → Answer: <br>
(C)
**
- Normal BP of water = $100^\circ\text{C} = 373.15\text{ K}$.
- New BP = $373.15 + 0.52 = 373.67\text{ K}$.
- Trap: <br>
(A) Adding $^\circ\text{C}$ to Kelvin indiscriminately.

**Q9.M3 → Answer: <br>
(A)**
- $\Delta T_b = 100.26 - 100 = 0.26^\circ\text{C}$.
- $m = \Delta T_b / K_b = 0.26 / 0.52 = 0.5\text{ mol/kg}$.
- RLVP $= \chi_{solute}$.
- For a $0.5\text{ m}$ solution, $n_{solute} = 0.5$, $n_{H_2O} = 1000/18 = 55.56$.
- $\chi_{solute} = 0.5 / (0.5 + 55.56) = 0.5 / 56.06 = 0.0089 \approx 0.009$.

**Q9.M4 → Answer: <br>
(B)**
- $100\text{ mL}$ water = $100\text{ g}$ water = $0.1\text{ kg}$.
- Molality $m = 0.1\text{ mol} / 0.1\text{ kg} = 1.0\text{ m}$.
- $\Delta T_b = 0.52 \times 1.0 = 0.52^\circ\text{C}$.
- Trap: <br>
(A) Forgetting to convert $100\text{ g}$ to $0.1\text{ kg}$.

**Q9.M5 → Answer: <br>
(B)**
- The formula is $MM = \frac{K_b \cdot W_{solute}}{\Delta T_b \cdot W_{solvent(kg)}}$. You must know $K_b$.

**Q9.M6 → Answer: <br>
(C)
**
- Loss in solution ($W_1$) $\propto P_s = 1.2$.
- Loss in solvent ($W_2$) $\propto P^\circ - P_s = 0.05$.
- Gain in CaCl$_2$ tube ($W_1 + W_2$) $\propto P^\circ = 1.25$.
- RLVP $= \frac{P^\circ - P_s}{P^\circ} = \frac{W_2}{W_1 + W_2} = \frac{0.05}{1.25}$.

**Q9.M7 → Answer: <br>
(C)
**
- Moles of A $= 10 / 100 = 0.1\text{ mol}$.
- Moles of B $= 20 / 200 = 0.1\text{ mol}$.
- Since moles are equal and solvent mass is equal, molality is equal.
- Therefore, $\Delta T_b$ ratio is $1:1$.

**Q9.M8 → Answer: <br>
(A)**
- $\Delta T_b = K_b \cdot m \implies K_b = \Delta T_b / m = \text{K} / (\text{mol/kg}) = \text{K kg mol}^{-1}$.

**Q9.M9 → Answer: <br>
(B)**
- Correct formula: $\frac{\Delta P}{P_s} = \frac{n_2}{n_1} \implies MM_{true} = \frac{P_s}{\Delta P} \cdot \frac{W_2 M_1}{W_1}$.
- Student uses: $\frac{\Delta P}{P^\circ} = \frac{n_2}{n_1} \implies MM_{student} = \frac{P^\circ}{\Delta P} \cdot \frac{W_2 M_1}{W_1}$.
- Since $P^\circ > P_s$, the student's denominator in the fraction $\frac{\Delta P}{P^\circ}$ is larger → calculated $n_2$ is smaller → $MM = W/n_2$ is **too high**.

**Q9.M10 → Answer: <br>
(B)**
- $K_b \propto T_b^2 / \Delta H_{vap}$.
- Since $\Delta H_{vap}$ and $M$ are equal: $K_{b(X)} / K_{b(Y)} = (T_X / T_Y)^2 = (2/1)^2 = 4$.

**Q9.M11 → Answer: <br>
(C)
**
- $100\text{ g}$ solution has $5\text{ g}$ urea, $10\text{ g}$ glucose, and $85\text{ g}$ water.
- Moles urea $= 5/60 = 0.0833$.
- Moles glucose $= 10/180 = 0.0555$.
- Total moles solute $= 0.1388$.
- Mass of solvent $= 0.085\text{ kg}$.
- $m = 0.1388 / 0.085 = 1.633\text{ m}$.
- $\Delta T_b = 0.52 \times 1.633 = 0.849^\circ\text{C} \approx 0.85^\circ\text{C}$.
- BP $= 100.85^\circ\text{C}$.

**Q9.M12 → Answer: <br>
(B)**
- RLVP is literally equal to the mole fraction of the solute. It is $0.1$.

**Q9.M13 → Answer: <br>
(B)**
- By definition, $\Delta T_b = K_b \cdot m$ (where $m$ is molality).

**Q9.M14 → Answer: <br>
(B)**
- The formula $K_b = \frac{M \cdot R \cdot T_b^2}{1000 \cdot \Delta H_{vap}}$ has a $1000$ in the denominator specifically to convert the molar mass of the solvent $M$ from $\text{g/mol}$ to $\text{kg/mol}$ so it cancels properly with the definition of molality ($\text{mol/kg}$). Thus, $M$ must be substituted in $\text{g/mol}$.

**Q9.M15 → Answer: <br>
(D)**
- For macromolecules (polymers, proteins), $\Delta T_b$, $\Delta T_f$, and RLVP are too small to measure accurately (e.g., $0.001^\circ\text{C}$). Osmotic pressure gives a large, easily measurable physical pressure even for very dilute solutions, making it the best colligative property for high molar masses.
</details>

---

*Next: [Chapter 10 — Depression in Freezing Point →](./10_freezing_point_depression.md)*
