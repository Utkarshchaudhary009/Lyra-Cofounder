# Chapter 6: Solubility & Henry's Law
## Part III — Solubility

---

## 🎯 Stage 1: The Core Idea

### Two Types of Solubility, Two Different Stories

**Solid in Liquid:** Sugar in water. Heat it up — more dissolves. Cooling causes crystallization.

**Gas in Liquid:** CO₂ in soda. Heat it up — it escapes. Open the bottle (reduce pressure) — it fizzes out.

These two behave *opposite* to each other with temperature. This is the first thing to lock in.

### Henry's Law — The Gas Solubility Master

> **Henry's Law:** The solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the liquid.

Mathematically:
```
P_gas = K_H × χ_gas
```

**K_H is Henry's Constant** — it's unique to each gas, at each temperature.

### The K_H Intuition

- **Low K_H** = gas dissolves easily = high solubility (e.g., SO₂, CO₂)
- **High K_H** = gas barely dissolves = low solubility (e.g., O₂, N₂, He)

Why?<br> Gases with stronger intermolecular attraction to water molecules (polar gases, gases that form hydrogen bonds) dissolve more and have lower K_H.

### Real-World Applications of Henry's Law

| Situation | Henry's Law in Action |
|-----------|----------------------|
| Soft drinks / soda water | CO₂ dissolved under high pressure (high P → high χ_CO₂) |
| Deep sea diving | N₂ dissolves in blood at high pressure |
| Decompression sickness | Rapid pressure drop → N₂ bubbles in blood |
| Altitude sickness | Low P_O₂ → less O₂ dissolved in blood |
| Aquatic life in hot water | High T → K_H increases → O₂ solubility decreases |

---

## 🔬 Stage 2: The Formula Lab

### Henry's Law — Two Forms

**Primary form:**
```
P_gas = K_H × χ_gas

where:
    P_gas = partial pressure of gas above liquid (bar or atm)
    K_H   = Henry's constant (same units as pressure)
    χ_gas = mole fraction of gas dissolved in liquid
```

**In terms of solvent mole fraction** (since χ_gas + χ_solvent = 1):
```
P_gas = -K_H × χ_solvent + K_H

Slope on P vs. χ_solvent graph = -K_H (negative slope)
Y-intercept = K_H
```

### Graphical Summary

| Graph | Slope | Intercept |
|-------|-------|-----------|
| P_gas vs χ_gas | K_H (positive) | 0 |
| P_gas vs χ_solvent | -K_H (negative) | K_H |

### Temperature Effect on K_H

```
As Temperature ↑ → K_H ↑ → Solubility of gas ↓
```

This is because gas dissolution is exothermic (like condensation). Heating shifts equilibrium backward → gas escapes.

### Solid Solubility and Temperature

For most solids:
```
As Temperature ↑ → Solubility ↑
(dissolution of solids is usually endothermic)
```

Exception: Some salts like Na₂SO₄ and Li₂SO₄ show *decreasing* solubility above a certain temperature.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Theoretical — Factors Affecting Gas Solubility

**Pattern:** Conceptual questions about K_H, temperature, pressure, and polarity.

#### Solved Example 6.1
**Q:** Compare K_H values of SO₂ and H₂ in water. Which is larger?<br> 🟡

```
SO₂ is polar; H₂ is non-polar.
Polar gas ↔ polar solvent (water) → stronger interaction → higher solubility.
Higher solubility → Lower K_H.

∴ (K_H)_H₂ > (K_H)_SO₂

Answer: K_H of H₂ is greater than K_H of SO₂.
```

#### Solved Example 6.2
**Q:** Which statement about Henry's Law is INCORRECT?<br>
<br>
(A) Different gases have different K_H at same temperature
<br>
(B) K_H increases with temperature
<br>
(C)
 Partial pressure of gas ∝ mole fraction of gas
<br>
(D) Higher K_H at given pressure = higher solubility 🟡

```
<br>
(A) True ✓ — each gas has unique K_H
<br>
(B) True ✓ — K_H increases as T rises (solubility falls)
<br>
(C)
 True ✓ — that IS Henry's Law (P = K_H × χ)
<br>
(D) FALSE ✗ — Higher K_H means LOWER solubility
              (P = K_H × χ; at fixed P, higher K_H → smaller χ)

Answer: <br>
(D) is incorrect.
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 6.1a | Why does the solubility of CO₂ in a carbonated drink decrease when the cap is removed?<br> | 🟢 |
| 6.1b | Why do scuba divers ascend slowly?<br> | 🟡 |
| 6.1c | Explain why aquatic life struggles in hot water. | 🟡 |
| 6.1d | Among O₂, CO₂, and He, arrange in increasing order of K_H (at same temperature in water). | 🟡 |
| 6.1e | K_H for N₂ is 8.42 × 10⁴ bar and for CO₂ is 1.67 × 10³ bar. Which gas is more soluble?<br> | 🟢 |
| 6.1f | **Assertion(A):** The solubility of CO₂ in water is greater than that of O₂ at the same temperature and pressure.<br>**Reason (R):** CO₂ has a lower Henry's constant (K_H) than O₂ because CO₂ is more polar and reacts with water. | 🟢 |
| 6.1g | **Statement I:** When a bottle of soda water is opened at room temperature, CO₂ bubbles out vigorously.<br>**Statement II:** The partial pressure of CO₂ above the liquid drops from several atmospheres to approximately 0.0004 atm upon opening. | 🟢 |
| 6.1h | A deep-sea diver breathes compressed air at 10 atm pressure. If the mole fraction of N₂ in air is 0.78 and K_H for N₂ in blood is 8.42×10⁴ bar, estimate the mole fraction of N₂ dissolved in the diver's blood at this depth. (1 atm ≈ 1 bar) | 🟡 |
| 6.1i | **Assertion(A):** At high altitudes, people may suffer from anoxia (weakness and inability to think clearly).<br>**Reason (R):** At higher altitudes, the partial pressure of oxygen in the air is lower, reducing the amount of O₂ dissolved in blood according to Henry's Law. | 🟢 |
| 6.1j | **Statement I:** The solubility of most solids in water increases with temperature.<br>**Statement II:** The dissolution of most solids in water is an exothermic process. | 🟡 |
| 6.1k | In a fermentation tank, CO₂ builds up to a partial pressure of 2.5 bar above the aqueous broth at 298 K. K_H for CO₂ = 1.67×10³ bar. Calculate the mass of CO₂ dissolved per litre of broth. (MM of CO₂ = 44 g/mol) | 🔴 |
| 6.1l | **Assertion(A):** Aquatic life is more abundant in cold polar waters than in warm tropical waters.<br>**Reason (R):** K_H for O₂ decreases with decreasing temperature, increasing the concentration of dissolved oxygen in cold water. | 🟡 |
| 6.1m | **Statement I:** When a gas dissolves in a liquid, the process is accompanied by a release of heat (exothermic).<br>**Statement II:** According to Le Chatelier's principle, increasing temperature shifts the equilibrium of gas dissolution in the forward direction. | 🟡 |
| 6.1n | A fish pond has dissolved O₂ at equilibrium with air (P_O₂ = 0.21 bar) at 303 K. An aerator increases the partial pressure of O₂ in the water to 0.42 bar. By what factor does the dissolved O₂ concentration increase?<br> (K_H of O₂ = 46.82 kbar) | 🟡 |
| 6.1o | **Assertion(A):** Helium is preferred over nitrogen in deep-sea diving gas mixtures.<br>**Reason (R):** Helium has a much higher K_H than nitrogen, meaning it dissolves significantly less in blood at high pressure. | 🔴 |

<details>
<summary>💡 Solutions for Type 1</summary>

**6.1a:** By Henry's Law, solubility ∝ P_gas. Inside the bottle, CO₂ is under high pressure → high solubility. When cap is removed, P_CO₂ drops drastically → solubility drops → CO₂ escapes as bubbles.

**6.1b:** At depth, high water pressure causes N₂ to dissolve in blood (high P → high χ_N₂). If ascent is rapid, pressure drops suddenly → N₂ solubility plummets → N₂ forms dangerous bubbles in bloodstream (decompression sickness / "the bends").

**6.1c:** Gas dissolution is exothermic. Hot water → equilibrium shifts backward → O₂ escapes → less dissolved O₂ available for fish and aquatic organisms.

**6.1d:** He is inert/non-polar (highest K_H); O₂ is non-polar (medium K_H); CO₂ is polar and reacts with water (lowest K_H).
Order of increasing K_H: **CO₂ < O₂ < He**
(equivalently: CO₂ most soluble, He least soluble)

**6.1e:** Lower K_H = higher solubility. K_H(CO₂) = 1.67×10³ < K_H(N₂) = 8.42×10⁴. **CO₂ is more soluble.**

**6.1f → Answer:(A) Both A and R are true, and R is the correct explanation.**
- CO₂ is polar and reacts with water (forming H₂CO₃), giving it a much lower K_H than O₂ (non-polar). Lower K_H → higher solubility.

**6.1g → Both statements are true.**
- Soda is bottled under high CO₂ pressure. Opening drops the partial pressure from ~4 atm to ~0.0004 atm, so solubility plummets and CO₂ fizzes out.

**6.1h:**
- P_N₂ = 0.78 × 10 = 7.8 bar
- χ_N₂ = P_N₂/K_H = 7.8/(8.42×10⁴) = **9.26×10⁻⁵**

**6.1i → Answer:(A) Both A and R are true, and R is the correct explanation.**
- At high altitudes, P_total is lower → P_O₂ is lower → less O₂ dissolves in blood (Henry's Law) → anoxia.

**6.1j → Statement I is True, Statement II is False.**
- Statement I is true: For most solids, solubility increases with temperature.
- Statement II is false: Dissolution of most solids is ENDOTHERMIC (ΔH > 0), not exothermic.

**6.1k:**
- χ_CO₂ = 2.5/(1.67×10³) = 1.497×10⁻³
- n_water per litre = 1000/18 = 55.56 mol
- n_CO₂ ≈ 1.497×10⁻³ × 55.56 = 0.08317 mol
- Mass = 0.08317 × 44 = **3.66 g**

**6.1l → Answer:(A) Both A and R are true, and R is the correct explanation.**
- Cold water → lower T → lower K_H → higher O₂ solubility → more aquatic life.

**6.1m → Statement I is True, Statement II is False.**
- Statement I is true: Gas dissolution is exothermic.
- Statement II is false: Increasing temperature shifts the EXOTHERMIC equilibrium in the REVERSE direction (gas escapes), not forward.

**6.1n:**
- χ_O₂(initial) = 0.21/(46.82×10³) = 4.486×10⁻⁶
- χ_O₂(final) = 0.42/(46.82×10³) = 8.971×10⁻⁶
- Factor = 8.971/4.486 = **2.0** (doubling P doubles solubility)

**6.1o → Answer:(A) Both A and R are true, and R is the correct explanation.**
- K_H(He) ≈ 1.46×10⁵ bar > K_H(N₂) ≈ 8.42×10⁴ bar. He has higher K_H → lower solubility in blood → less risk of decompression sickness.
</details>

---

### Type 2: Graph Interpretation

**Pattern:** Interpret P vs. χ graphs for Henry's Law.

#### Solved Example 6.3
**Q:** Two gases A and B are plotted on a P_gas vs. χ_gas graph. Gas B has a steeper slope. Which gas has greater solubility?<br> 🟡

```
Slope of P vs. χ_gas = K_H

Gas B has higher slope → higher K_H → lower solubility.
Gas A has lower slope → lower K_H → higher solubility.

Answer: Gas A has greater solubility.
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 6.2a | What does the slope represent in a P_gas vs. χ_gas plot?<br> | 🟢 |
| 6.2b | In a plot of P_gas vs. χ_solvent, what is the slope and y-intercept?<br> | 🟡 |
| 6.2c | Two gases A and B are plotted on P vs. χ. If slope_A > slope_B, which has higher solubility?<br> | 🟢 |
| 6.2d | A gas shows a steeper P vs. χ curve at 40°C than at 25°C. What does this tell you about the effect of temperature on K_H?<br> | 🟡 |
| 6.2e | **Assertion(A):** In a plot of P_gas vs. χ_gas, the slope is equal to K_H.<br>**Reason (R):** Henry's Law states P_gas = K_H × χ_gas, which is a linear equation with slope K_H and zero intercept. | 🟢 |
| 6.2f | **Statement I:** The plot of P_gas vs. χ_solvent for Henry's Law has a negative slope.<br>**Statement II:** χ_gas + χ_solvent = 1, making P_gas = K_H(1 - χ_solvent) = -K_H·χ_solvent + K_H. | 🟢 |
| 6.2g | A researcher plots P_gas vs. χ_gas for two gases X and Y at the same temperature. The slope for X is 2×10⁴ bar and for Y is 5×10⁴ bar. If the partial pressure of each is 1 bar, find the ratio of their mole fractions dissolved. | 🟡 |
| 6.2h | **Assertion(A):** If the P_gas vs. χ_gas plot for a gas at 40°C is steeper than at 20°C, the gas is less soluble at 40°C.<br>**Reason (R):** A steeper slope means a higher K_H, and solubility is inversely proportional to K_H. | 🟡 |
| 6.2i | **Statement I:** If the P_gas vs. χ_gas line passes through the origin, it confirms Henry's Law is obeyed.<br>**Statement II:** Henry's Law predicts zero dissolved gas at zero partial pressure. | 🟢 |
| 6.2j | From a P_gas vs. χ_solvent graph, the y-intercept is found to be 1.67×10³ bar and the slope is -1.67×10³ bar. Identify the gas and find its mole fraction in water when P_gas = 0.835 bar. | 🔴 |
| 6.2k | **Assertion(A):** The Henry's Law constant K_H can be determined from either the slope of P vs. χ_gas or the intercept of P vs. χ_solvent.<br>**Reason (R):** Both graphs contain information about K_H, just represented differently through the relation χ_gas + χ_solvent = 1. | 🟡 |
| 6.2l | **Statement I:** For a gas with very low solubility, the P_gas vs. χ_solvent plot will appear nearly horizontal.<br>**Statement II:** Very low solubility means K_H is very large, making the slope -K_H very steep (more negative). | 🔴 |
| 6.2m | A company measures the solubility of a new refrigerant gas in water. At P = 0.5 bar, χ_gas = 2.5×10⁻⁵. At P = 1.0 bar, χ_gas = 5.0×10⁻⁵. Find K_H and state whether the data follows Henry's Law. | 🟡 |
| 6.2n | **Assertion(A):** The Henry's Law plot for NH₃ in water deviates significantly from the straight line predicted by P = K_H·χ.<br>**Reason (R):** NH₃ chemically reacts with water (forming NH₄OH), so the simple physical dissolution described by Henry's Law does not apply. | 🔴 |

<details>
<summary>💡 Solutions for Type 2</summary>

**6.2a:** **Slope = K_H (Henry's constant)**

**6.2b:** Slope = **−K_H** (negative); Y-intercept = **K_H**

**6.2c:** slope_A > slope_B → K_H<br>
(A) > K_H<br>
(B) → **Gas B has higher solubility**

**6.2d:** Steeper slope at 40°C → higher K_H → **K_H increases with temperature**, meaning solubility of gas decreases as temperature rises.

**6.2e → Answer:(A) Both A and R are true, and R is the correct explanation.**
- P_gas = K_H·χ_gas is y = mx + 0 with m = K_H.

**6.2f → Both statements are true.**
- Substituting χ_gas = 1 - χ_solvent gives P = K_H(1 - χ_solvent) = -K_H·χ_solvent + K_H. Slope = -K_H (negative).

**6.2g:**
- Slope = K_H. So K_H(X) = 2×10⁴ bar, K_H(Y) = 5×10⁴ bar.
- χ_X = P/K_H(X) = 1/(2×10⁴) = 5×10⁻⁵; χ_Y = 1/(5×10⁴) = 2×10⁻⁵
- **χ_X : χ_Y = 5:2** (X is 2.5× more soluble)

**6.2h → Answer:(A) Both A and R are true, and R is the correct explanation.**
- Steeper slope at 40°C → higher K_H at 40°C → lower solubility at higher temperature.

**6.2i → Both statements are true.**
- P = K_H·χ_gas passes through (0,0). At P = 0, χ_gas = 0, which is physically correct.

**6.2j:**
- Equation: P = -K_H·χ_solvent + K_H. Y-intercept = K_H = 1.67×10³ bar.
- K_H = 1.67×10³ bar matches **CO₂** at 298 K.
- At P = 0.835 bar: χ_CO₂ = 0.835/(1.67×10³) = **5.0×10⁻⁴**

**6.2k → Answer:(A) Both A and R are true, and R is the correct explanation.**
- P vs. χ_gas: slope = +K_H; P vs. χ_solvent: intercept = +K_H.

**6.2l → Statement I is False, Statement II is True.**
- Statement I is false: Very low solubility → very large K_H → slope (-K_H) is very steep (very negative), not horizontal.
- Statement II is true.

**6.2m:**
- From data: χ doubles when P doubles → linear relationship through origin → **obeys Henry's Law**.
- K_H = P/χ = 0.5/(2.5×10⁻⁵) = 1.0/(5.0×10⁻⁵) = **2.0×10⁴ bar**

**6.2n → Answer:(A) Both A and R are true, and R is the correct explanation.**
- NH₃ reacts chemically with water (NH₃ + H₂O ⇌ NH₄OH), so it does not follow Henry's Law which assumes only physical dissolution.
</details>

---

### Type 3: Numerical — Direct Henry's Law Calculation

**Pattern:** Given K_H and P_gas → find χ_gas → convert to moles dissolved.

#### Solved Example 6.4
**Q:** O₂ is bubbled through water at 303 K. K_H = 46.82 kbar, P_O₂ = 0.920 bar. How many millimoles of O₂ dissolve in 1 L of water?<br> 🔴 ⭐

```
Step 1: Find χ_O₂
    P_O₂ = K_H × χ_O₂
    0.920 = 46820 × χ_O₂    (convert kbar → bar: 46.82 kbar = 46820 bar)
    χ_O₂ = 0.920/46820 = 1.965 × 10⁻⁵

Step 2: Find moles of O₂ in 1L water
    n_water = 1000/18 = 55.56 mol
    χ_O₂ = n_O₂/(n_O₂ + n_water) ≈ n_O₂/n_water  (since χ_O₂ << 1)
    n_O₂ = χ_O₂ × n_water = 1.965 × 10⁻⁵ × 55.56 = 1.092 × 10⁻³ mol

Answer: ≈ 1 mmol of O₂ dissolves per litre.
```

#### Solved Example 6.5
**Q:** CO₂ is bubbled through 0.9 L water at 298 K. K_H = 1.67 × 10³ bar, P_CO₂ = 0.835 bar. Find mmol of CO₂ dissolved. 🔴 ⭐

```
χ_CO₂ = P_CO₂/K_H = 0.835/(1.67×10³) = 5.0 × 10⁻⁴

n_water = (0.9×1000)/18 = 50 mol

n_CO₂ = χ_CO₂ × n_water = 5.0×10⁻⁴ × 50 = 0.025 mol = 25 mmol

Answer: 25 mmol
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 6.3a | K_H for He = 1.46×10⁵ bar. P_He = 0.5 bar. Find χ_He in water. | 🟡 |
| 6.3b | χ_N₂ in water = 3×10⁻⁶ at P_N₂ = 0.8 bar. Find K_H for N₂. | 🟡 |
| 6.3c | K_H for O₂ = 4.6×10⁴ bar at 25°C. P_O₂ = 0.21 bar (air). Find moles of O₂ dissolved per litre of water. ⭐ | 🔴 |
| 6.3d | K_H for CO₂ at 298 K = 8.0×10⁴ kPa. P_CO₂ = 20 kPa. Find molar solubility of O₂ in mol/dm³. | 🔴 |
| 6.3e | K_H for Ar in water = 40.39 kbar at 298 K. If the partial pressure of Ar in air is 0.0093 bar, find the millimoles of Ar dissolved in 2 L of water. | 🟡 |
| 6.3f | **Assertion(A):** If K_H for a gas doubles when temperature increases from 25°C to 50°C, the solubility at 50°C is half of that at 25°C at the same pressure.<br>**Reason (R):** At constant pressure, χ ∝ 1/K_H, so doubling K_H halves the mole fraction. | 🟡 |
| 6.3g | A soft drink manufacturer dissolves CO₂ at 4 atm pressure into water at 298 K. K_H = 1.67×10³ bar. After opening, the CO₂ pressure drops to 0.0004 bar. Calculate the percentage of CO₂ that escapes. | 🔴 |
| 6.3h | **Statement I:** To find the moles of gas dissolved in a given volume of solvent, it is necessary to know the number of moles of solvent.<br>**Statement II:** The mole fraction of gas is defined as n_gas/(n_gas + n_solvent), and for dilute solutions, n_gas ≈ χ × n_solvent. | 🟢 |
| 6.3i | A scuba tank contains a mixture of O₂ (21%) and He (79%) at 200 bar total pressure. K_H for O₂ = 46.82 kbar and for He = 146 kbar at 303 K. Compare the mole fractions of O₂ and He that would dissolve in a diver's body fluids if the diver breathes at this pressure. | 🔴 |
| 6.3j | **Assertion(A):** When using P_gas = K_H × χ_gas, the units of K_H must be the same as the units of P_gas.<br>**Reason (R):** Mole fraction (χ) is a dimensionless quantity, so for dimensional consistency, K_H must have pressure units. | 🟢 |
| 6.3k | At 293 K, K_H for O₂ = 4.0×10⁴ bar and at 303 K, K_H for O₂ = 4.68×10⁴ bar. A lake at 293 K has P_O₂ = 0.21 bar. In summer, the lake warms to 303 K. Find the ratio of dissolved O₂ in winter to summer. | 🔴 |
| 6.3l | **Statement I:** A gas with K_H = 500 bar is more soluble than a gas with K_H = 5000 bar at the same pressure.<br>**Statement II:** Lower K_H corresponds to higher solubility because χ = P/K_H. | 🟢 |
| 6.3m | A sample of water from a deep well contains dissolved CH₄ gas at a mole fraction of 1.2×10⁻⁵. K_H for CH₄ = 0.413×10³ bar at well temperature. What is the partial pressure of CH₄ in contact with the water?<br> | 🟡 |
| 6.3n | **Assertion(A):** In the calculation n_gas = χ_gas × n_water, we approximate n_gas + n_water ≈ n_water.<br>**Reason (R):** For most gases dissolving in water, χ_gas is of the order of 10⁻⁵ or smaller, making n_gas negligible compared to n_water. | 🟢 |

<details>
<summary>💡 Solutions for Type 3</summary>

**6.3a:** χ_He = P/K_H = 0.5/(1.46×10⁵) = **3.42×10⁻⁶**

**6.3b:** K_H = P/χ = 0.8/(3×10⁻⁶) = **2.67×10⁵ bar**

**6.3c:** χ_O₂ = 0.21/(4.6×10⁴) = 4.565×10⁻⁶
n_water = 1000/18 = 55.56 mol
n_O₂ = 4.565×10⁻⁶ × 55.56 = **2.54×10⁻⁴ mol**

**6.3d:** χ_CO₂ = 20/(8×10⁴) = 2.5×10⁻⁴
n_water per dm³ = 1000/18 = 55.56 mol
n_CO₂ = 2.5×10⁻⁴ × 55.56 = 0.01389 mol/dm³ = **1.389×10⁻² mol/dm³**

**6.3e:**
- χ_Ar = 0.0093/(40.39×10³) = 2.303×10⁻⁷
- n_water in 2 L = 2000/18 = 111.11 mol
- n_Ar = 2.303×10⁻⁷ × 111.11 = 2.559×10⁻⁵ mol = **0.0256 mmol**

**6.3f → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- At constant P, χ = P/K_H. If K_H doubles, χ halves. So solubility at 50°C is half that at 25°C.

**6.3g:**
- Before: χ₁ = 4/1670 = 2.395×10⁻³ (1 atm ≈ 1 bar)
- After: χ₂ = 0.0004/1670 = 2.395×10⁻⁷
- % escaped = [(χ₁ - χ₂)/χ₁] × 100 ≈ **99.99%** (essentially all CO₂ escapes)

**6.3h → Both statements are true.**
- χ_gas = n_gas/(n_gas + n_water). For dilute solutions, n_gas ≪ n_water, so n_gas ≈ χ_gas × n_water.

**6.3i:**
- P_O₂ = 0.21 × 200 = 42 bar; P_He = 0.79 × 200 = 158 bar
- χ_O₂ = 42/(46.82×10³) = 8.97×10⁻⁴
- χ_He = 158/(146×10³) = 1.082×10⁻³
- **χ_He > χ_O₂** (higher partial pressure compensates for higher K_H)

**6.3j → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- χ is dimensionless, so K_H must have the same units as P (pressure) for the equation to be dimensionally consistent.

**6.3k:**
- Winter: χ_w = 0.21/(4.0×10⁴) = 5.25×10⁻⁶
- Summer: χ_s = 0.21/(4.68×10⁴) = 4.487×10⁻⁶
- **Ratio (winter/summer) = 5.25/4.487 = 1.17** (17% more O₂ in winter)

**6.3l → Both statements are true.**
- χ = P/K_H, so lower K_H → higher χ → more soluble.

**6.3m:**
- P_CH₄ = K_H × χ_CH₄ = (0.413×10³) × (1.2×10⁻⁵) = **4.956×10⁻³ bar** ≈ 0.005 bar

**6.3n → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- The approximation n_gas + n_water ≈ n_water is justified because χ_gas is tiny (∼10⁻⁵), making n_gas negligible.
</details>

---

### Type 4: Solid Solubility — Temperature Effect

**Pattern:** Conceptual + graph reading for solid solubility.

#### Solved Example 6.6
**Q:** How does the solubility of a solid change with temperature compared to a gas?<br> Explain. 🟢

```
Solid dissolving in liquid: usually endothermic (takes in heat)
→ By Le Chatelier: heating favours forward reaction → more dissolves
→ Solubility INCREASES with temperature (for most solids).

Gas dissolving in liquid: exothermic (releases heat)
→ By Le Chatelier: heating favours reverse reaction → gas escapes
→ Solubility DECREASES with temperature.

These are OPPOSITE trends.
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 6.4a | The dissolution of solid KNO₃ is endothermic. Predict the effect of increasing temperature on its solubility. | 🟢 |
| 6.4b | Why does warm soda go flat faster than cold soda?<br> | 🟢 |
| 6.4c | A solubility curve shows decreasing solubility with increasing temperature for a salt. What does this indicate about the dissolution enthalpy?<br> | 🟡 |
| 6.4d | The solubility of KNO₃ in water is 30 g/100 mL at 20°C and 85 g/100 mL at 50°C. Assuming the dissolution is endothermic, estimate the approximate solubility at 35°C. | 🟡 |
| 6.4e | **Assertion (A):** Na₂SO₄ solubility increases up to about 32°C and then decreases with further temperature increase.<br>**Reason (R):** The dissolution of Na₂SO₄ changes from endothermic to exothermic above 32°C due to a phase transition in the hydrated salt. | 🔴 |
| 6.4f | **Statement I:** The solubility of Ca(OH)₂ decreases with increasing temperature.<br>**Statement II:** The dissolution of Ca(OH)₂ is exothermic. | 🟡 |
| 6.4g | A student observes that 50 g of a salt dissolves in 100 mL water at 30°C but only 35 g dissolves at 60°C. Is the dissolution endothermic or exothermic?<br> What is the sign of ΔH?<br> | 🟢 |
| 6.4h | **Assertion (A):** Sugar dissolves faster in hot tea than in iced tea.<br>**Reason (R):** Higher temperature increases both the solubility and the rate of dissolution of sugar. | 🟢 |
| 6.4i | The enthalpy of dissolution of NH₄NO₃ is +25.7 kJ/mol. If 10 g of NH₄NO₃ is dissolved in 100 mL water at 25°C, estimate whether the solution temperature will increase or decrease, and by roughly how much. (Specific heat of water ≈ 4.18 J/g·°C) | 🔴 |
| 6.4j | **Statement I:** A saturated solution at a higher temperature generally contains more dissolved solid than at a lower temperature for most salts.<br>**Statement II:** The solubility of NaCl changes very little with temperature compared to KNO₃. | 🟡 |
| 6.4k | **Assertion (A):** Fish can survive in a frozen lake even when the surface is covered with ice.<br>**Reason (R):** Water has maximum density at 4°C, so the bottom of the lake remains at 4°C, and oxygen dissolved in this water is sufficient for fish. | 🟡 |
| 6.4l | A factory discharges hot water at 45°C into a river at 15°C. If dissolved O₂ at 15°C is 10 mg/L and at 45°C is 5 mg/L, and the river flows at 1000 L/s with the factory adding 100 L/s of hot water, estimate the downstream O₂ concentration (assuming complete mixing). | 🔴 |
| 6.4m | **Assertion (A):** Carbonated beverages are stored in pressurized containers.<br>**Reason (R):** High pressure increases the solubility of CO₂, keeping the drink carbonated until opened. | 🟢 |

<details>
<summary>💡 Solutions for Type 4</summary>

**6.4a:** Endothermic dissolution + heating → forward reaction favoured → **Solubility increases.**

**6.4b:** Warm temperature → K_H of CO₂ increases → χ_CO₂ decreases at same atmospheric pressure → CO₂ escapes → soda loses fizz faster.

**6.4c:** Decreasing solubility with temperature → dissolution is **exothermic** (ΔH_dissolution < 0). Heating shifts equilibrium backward, reducing solubility.

**6.4d:**
- Linear interpolation between 20°C (30 g) and 50°C (85 g): slope = (85-30)/(50-20) = 55/30 = 1.833 g/°C
- At 35°C: 30 + 1.833×(35-20) = 30 + 27.5 = **≈ 57.5 g/100 mL**

**6.4e → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Na₂SO₄·10H₂O undergoes a phase transition at ~32°C. Below 32°C, dissolution is endothermic (solubility ↑ with T); above 32°C, the anhydrous form dissolves exothermically.

**6.4f → Both statements are true.**
- Ca(OH)₂ is an exception: its dissolution is exothermic, so solubility decreases as temperature rises.

**6.4g:**
- Solubility decreases as temperature increases → dissolution is **exothermic** → **ΔH < 0** (negative sign).

**6.4h → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Higher temperature increases both kinetic rate (faster dissolution) and equilibrium solubility of sugar (endothermic dissolution).

**6.4i:**
- ΔH = +25.7 kJ/mol (endothermic — absorbs heat)
- Moles NH₄NO₃ = 10/80.04 = 0.125 mol
- Heat absorbed = 0.125 × 25.7 = 3.212 kJ = 3212 J
- Mass of solution ≈ 100 g water + 10 g salt = 110 g
- ΔT = -Q/(m·c) = -3212/(110 × 4.18) = -3212/459.8 = **-6.99°C** → temperature **decreases** by ~7°C

**6.4j → Both statements are true.**
- For most salts, solubility ↑ with T. But NaCl's solubility is nearly flat (~36 g/100 mL at 0°C to ~39 g at 100°C), while KNO₃'s solubility changes dramatically.

**6.4k → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Water at 4°C is densest, so it sinks to the bottom. The bottom stays at ~4°C, and O₂ solubility is higher at 4°C than near 0°C surface.

**6.4l:**
- O₂ concentration in river water = 10 mg/L at 1000 L/s = 10,000 mg/s
- O₂ concentration in factory water = 5 mg/L at 100 L/s = 500 mg/s
- Total O₂ = 10,500 mg/s; Total flow = 1100 L/s
- **Downstream O₂ ≈ 10,500/1100 = 9.55 mg/L**

**6.4m → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- High pressure keeps CO₂ dissolved (Henry's Law). Releasing pressure causes CO₂ to escape.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 6.M1 | K_H for O₂ = 46.82 kbar at 303 K. Air = 21% O₂ by mole at 1 bar total pressure. Find mass of O₂ dissolved in 1 L of water at sea level. ⭐ | T3 | 🔴 |
| 6.M2 | A soft drink contains CO₂ at 4 bar pressure (K_H = 1600 bar). After opening, pressure drops to 0.0004 bar (partial pressure of CO₂ in air). Compare χ_CO₂ before and after opening. | T1+T3 | 🔴 |
| 6.M3 | Two gases A and B at same temperature. K_H<br>
(A) = 2×10⁴ bar, K_H<br>
(B) = 5×10³ bar. Both are at P = 1 bar. Find the ratio χ_A:χ_B. | T2+T3 | 🟡 |
| 6.M4 | A gas mixture (O₂ 21%, N₂ 78%, Ar 1%) at 1 bar is in equilibrium with water at 298 K. K_H values: O₂ = 46.82 kbar, N₂ = 86.2 kbar, Ar = 40.39 kbar. Find the composition (mole fractions) of dissolved gases in water. Which gas has the highest mole fraction in solution?<br> ⭐ | T3+Mix | 🔴 |
| 6.M5 | **Assertion (A):** For a gas that associates with solvent molecules, Henry's Law may not hold even at low pressure.<br>**Reason (R):** Henry's Law assumes no chemical interaction between the gas and the solvent. | T1 | 🟡 |
| 6.M6 | The solubility of a gas at 1 atm pressure is 2.5×10⁻² mol/L at 25°C. (a) Find K_H in bar·L/mol. (b) What will be the solubility at 5 atm?<br> ⭐ | T3 | 🟡 |
| 6.M7 | **Statement I:** The solubility of a gas in a liquid always increases with increase in pressure.<br>**Statement II:** The solubility of a gas in a liquid always decreases with increase in temperature. | T1 | 🟡 |
| 6.M8 | Mount Everest climbers at 8848 m experience atmospheric pressure of about 0.33 bar. If the mole fraction of O₂ in air is constant at 0.21, calculate P_O₂ at the summit and the ratio of dissolved O₂ in blood compared to sea level (1 bar). ⭐ | T3 | 🔴 |
| 6.M9 | **Assertion (A):** Higher the temperature of the ocean, lower the concentration of dissolved oxygen available for marine life.<br>**Reason (R):** Global warming leads to thermal pollution of oceans, reducing dissolved oxygen levels. | T1 | 🟡 |
| 6.M10 | A diver uses a heliox mixture (He 80%, O₂ 20%) at 30 m depth where total pressure = 4 bar. K_H for He = 1.46×10⁵ bar, K_H for O₂ = 4.68×10⁴ bar at body temperature (37°C). Find: (a) Partial pressures of He and O₂, (b) Mole fractions of each dissolved, (c) Which gas poses a greater risk of decompression sickness?<br> ⭐ | T3+Mix | 🔴 |
| 6.M11 | **Assertion (A):** The oxygen content of blood decreases at high altitudes, causing hypoxia.<br>**Reason (R):** At high altitudes, the total atmospheric pressure is lower, and consequently the partial pressure of oxygen is lower. | T1 | 🟢 |
| 6.M12 | Henry's Law constant for O₂ in water at 298 K is 4.6×10⁴ bar. Calculate: (a) The mole fraction of O₂ in water exposed to air at 1 bar (21% O₂). (b) The molar concentration of O₂ in water (density = 1 g/mL). (c) The mass of O₂ per litre in mg. ⭐ | T3 | 🔴 |
| 6.M13 | **Assertion (A):** The y-intercept in a P_gas vs. χ_solvent plot is numerically equal to K_H.<br>**Reason (R):** When χ_solvent = 0, the equation P = −K_H·χ_solvent + K_H gives P = K_H, which represents the hypothetical case of pure gas with no solvent. | T2 | 🟡 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**6.M1:**
- P_O₂ = 0.21 × 1 = 0.21 bar (21% of 1 bar total)
- χ_O₂ = 0.21/46820 = 4.486×10⁻⁶
- n_water in 1L = 55.56 mol
- n_O₂ = 4.486×10⁻⁶ × 55.56 = 2.493×10⁻⁴ mol
- Mass = 2.493×10⁻⁴ × 32 = **7.977×10⁻³ g ≈ 8 mg**

**6.M2:**
- Before: χ_CO₂ = 4/1600 = **2.5×10⁻³**
- After: χ_CO₂ = 0.0004/1600 = **2.5×10⁻⁷**
- Ratio: 10,000:1 — CO₂ solubility drops 10,000-fold after opening!

**6.M3:**
- χ_A = P/K_H<br>
(A) = 1/(2×10⁴) = 5×10⁻⁵
- χ_B = P/K_H<br>
(B) = 1/(5×10³) = 2×10⁻⁴
- **χ_A:χ_B = 5×10⁻⁵ : 2×10⁻⁴ = 1:4** (B is 4× more soluble)

**6.M4:**
- P_O₂ = 0.21 bar, P_N₂ = 0.78 bar, P_Ar = 0.01 bar
- χ_O₂ = 0.21/(46.82×10³) = 4.486×10⁻⁶
- χ_N₂ = 0.78/(86.2×10³) = 9.049×10⁻⁶
- χ_Ar = 0.01/(40.39×10³) = 2.476×10⁻⁷
- **Highest χ: N₂** (despite having highest K_H among the three, its much higher partial pressure dominates)

**6.M5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Henry's Law assumes only physical dissolution. Chemical association/dissociation violates this assumption.

**6.M6:**
- (a) K_H = P/S = 1/(2.5×10⁻²) = **40 bar·L/mol**
- (b) S₂ = P₂/K_H = 5/40 = **0.125 mol/L** (or directly: S ∝ P → S₂ = 2.5×10⁻² × 5 = 0.125 mol/L)

**6.M7 → Statement I is True, Statement II is True.**
- Both statements are correct: solubility ↑ with P (Henry's Law), and solubility ↓ with T (exothermic dissolution).

**6.M8:**
- P_O₂(summit) = 0.33 × 0.21 = 0.0693 bar
- P_O₂(sea level) = 1 × 0.21 = 0.21 bar
- Ratio = 0.0693/0.21 = **0.33** (33% of sea-level O₂ dissolves at the summit)

**6.M9 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Higher ocean temperature → higher K_H → lower dissolved O₂. Global warming exacerbates this.

**6.M10:**
- (a) P_He = 0.80 × 4 = 3.2 bar; P_O₂ = 0.20 × 4 = 0.8 bar
- (b) χ_He = 3.2/(1.46×10⁵) = 2.192×10⁻⁵; χ_O₂ = 0.8/(4.68×10⁴) = 1.709×10⁻⁵
- (c) **O₂** has the higher dissolved mole fraction → greater risk (but in practice, decompression sickness is caused by the inert gas, here He, since O₂ is metabolized)

**6.M11 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Lower total pressure → lower P_O₂ → less O₂ dissolves in blood (Henry's Law) → hypoxia.

**6.M12:**
- (a) χ_O₂ = 0.21/(4.6×10⁴) = **4.565×10⁻⁶**
- (b) n_water/L = 55.56 mol; n_O₂ = 4.565×10⁻⁶ × 55.56 = 2.537×10⁻⁴ mol/L
- (c) Mass = 2.537×10⁻⁴ × 32 × 1000 = **8.12 mg/L**

**6.M13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- P = −K_H·χ_solvent + K_H. When χ_solvent = 0, P = K_H. This corresponds to the hypothetical intercept.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 6.B1 | State Henry's Law. Give its mathematical expression. *(NCERT)* | 🟢 |
| 6.B2 | State any two applications of Henry's Law. | 🟢 |
| 6.B3 | K_H of CO₂ at 298 K = 1.67×10³ bar. If CO₂ exerts partial pressure of 0.835 bar, find χ_CO₂ in the solution. | 🟡 |
| 6.B4 | Why is the solubility of a gas in a liquid inversely proportional to temperature?<br> | 🟡 |
| 6.B5 | The Henry's law constant for O₂ dissolved in water is 46.82 kbar at 303 K. If the partial pressure of O₂ is 0.920 bar, what is the mole fraction of O₂ in water?<br> *(NCERT)* ⭐ | 🟡 |
| 6.B6 | Explain why a person suffering from altitude sickness is advised to breathe oxygen-enriched air. Use Henry's Law in your answer. | 🟡 |
| 6.B7 | At 25°C, K_H for CO₂ is 1.67×10³ bar. Calculate the volume of CO₂ (at STP) that would dissolve in 500 mL of water if the partial pressure of CO₂ is 0.5 bar. (Molar volume at STP = 22.4 L/mol) | 🔴 |
| 6.B8 | **Assertion (A):** Henry's Law is a special case of Raoult's Law.<br>**Reason (R):** Both laws state that the vapour pressure of a component is proportional to its mole fraction. | 🟡 |
| 6.B9 | A diver using compressed air at 20 m depth breathes air at 3 bar. If the ascent is too rapid, nitrogen bubbles form in the blood. Explain this using Henry's Law and calculate the approximate ratio of dissolved N₂ at 20 m vs. at the surface (1 bar). | 🔴 |
| 6.B10 | K_H for O₂ in water = 4.68×10⁴ bar at 310 K (body temperature). Air contains 21% O₂. A person's lungs have P_O₂ = 0.13 bar. Find the mole fraction of O₂ in the blood. If P_O₂ drops to 0.07 bar (at high altitude), find the new mole fraction. | 🟡 |
| 6.B11 | Why does warm soda go flat faster than cold soda?<br> Explain with reference to Henry's Law and temperature dependence of K_H. | 🟢 |
| 6.B12 | The solubility of ethane (C₂H₆) in water at 25°C and 1 bar pressure is 6.1×10⁻⁵ molal. Calculate the Henry's Law constant for ethane in bar·kg/mol. | 🟡 |
| 6.B13 | **Assertion (A):** Carbonated drinks are bottled under high CO₂ pressure to prevent them from going flat.<br>**Reason (R):** According to Henry's Law, higher pressure above the liquid keeps more gas dissolved in the liquid. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**6.B1:** Henry's Law: At constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the liquid. Formula: **P_gas = K_H × χ_gas**

**6.B2:** (Any two): (1) Carbonated beverages — CO₂ dissolved under high pressure. (2) Scuba diving — divers breathe pressurized air; rapid ascent causes "bends." (3) Blood oxygen transport — O₂ solubility depends on P_O₂ in lungs.

**6.B3:** χ_CO₂ = P_CO₂/K_H = 0.835/(1.67×10³) = **5.0×10⁻⁴**

**6.B4:** Gas dissolution is exothermic (ΔH < 0). By Le Chatelier's principle, increasing temperature favours the reverse reaction (gas escaping from solution). Thus solubility decreases as temperature increases.

**6.B5:** χ_O₂ = P_O₂/K_H = 0.920/(46.82×10³) = 0.920/46820 = **1.965×10⁻⁵**

**6.B6:**
- At high altitude, P_total is lower → P_O₂ is lower (same mole fraction but lower total pressure).
- By Henry's Law (χ_O₂ = P_O₂/K_H), lower P_O₂ → less O₂ dissolves in blood → anoxia/hypoxia.
- Breathing O₂-enriched air increases P_O₂ in lungs → more O₂ dissolves in blood → symptoms relieved.

**6.B7:**
- χ_CO₂ = 0.5/(1.67×10³) = 2.994×10⁻⁴
- n_water in 500 mL = 500/18 = 27.78 mol
- n_CO₂ = 2.994×10⁻⁴ × 27.78 = 8.317×10⁻³ mol
- Volume at STP = 8.317×10⁻³ × 22.4 = **0.186 L = 186 mL**

**6.B8 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Henry's Law: P_solute = K_H·χ_solute. Raoult's Law: P_solvent = P°_solvent·χ_solvent. Both are proportional relationships. Henry's Law for the solute becomes Raoult's Law when K_H = P° (hypothetical).

**6.B9:**
- At 20 m: P_total = 3 bar, P_N₂ = 0.78 × 3 = 2.34 bar
- At surface: P_total = 1 bar, P_N₂ = 0.78 × 1 = 0.78 bar
- χ_N₂(20m) / χ_N₂(surface) = P_N₂(20m)/P_N₂(surface) = 2.34/0.78 = **3** (three times more dissolved N₂ at depth)
- Rapid ascent → pressure drops → solubility drops → N₂ comes out of solution forming bubbles (the bends).

**6.B10:**
- Normal: χ_O₂ = 0.13/(4.68×10⁴) = **2.78×10⁻⁶**
- High altitude: χ_O₂ = 0.07/(4.68×10⁴) = **1.50×10⁻⁶**
- Ratio = 1.50/2.78 = 0.54 (about half the dissolved O₂)

**6.B11:**
- Gas dissolution is exothermic. Higher temperature → K_H increases → χ_CO₂ decreases at same P_CO₂.
- Warm soda has lower CO₂ solubility → CO₂ escapes faster → soda goes flat more quickly.

**6.B12:**
- Molality = 6.1×10⁻⁵ mol/kg H₂O → in 1 kg water: n_ethane = 6.1×10⁻⁵ mol, n_water = 1000/18 = 55.56 mol
- χ_ethane = 6.1×10⁻⁵/(6.1×10⁻⁵ + 55.56) ≈ 6.1×10⁻⁵/55.56 = 1.098×10⁻⁶
- K_H = P/χ = 1/(1.098×10⁻⁶) = **9.11×10⁵ bar**
- In bar·kg/mol: K_H' = P/m = 1/(6.1×10⁻⁵) = **1.64×10⁴ bar·kg/mol**

**6.B13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- High pressure → high χ_CO₂ (Henry's Law). When sealed, CO₂ stays dissolved. Opening reduces pressure → CO₂ escapes.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q6.J1 🟡 ⭐**
Which of the following about Henry's Law is INCORRECT?<br>
<br>
(A) Higher K_H = lower solubility
<br>
(B) K_H increases with temperature
<br>
(C)
 K_H is the same for all gases at same temperature
<br>
(D) Partial pressure of gas ∝ its mole fraction in solution

**Q6.J2 🟡**
On a graph of P_gas (y-axis) vs. χ_solvent (x-axis), the slope of the Henry's Law line is:
<br>
(A) +K_H  <br>
(B) −K_H  <br>
(C)
 1/K_H  <br>
(D) Zero

**Q6.J3 🔴 ⭐**
CO₂ is dissolved in water at 298 K (K_H = 1.67×10³ bar). x mmol of CO₂ dissolves in 0.9 L water at P_CO₂ = 0.835 bar. Find x.
<br>
(A) 10  <br>
(B) 25  <br>
(C)
 50  <br>
(D) 5

**Q6.J4 🔴**
If K_H of a gas at 300 K is 2×10⁴ bar and at 400 K is 4×10⁴ bar, what can you conclude?<br>
<br>
(A) Solubility increases with temperature
<br>
(B) Solubility decreases with temperature
<br>
(C)
 Dissolution is endothermic
<br>
(D) Dissolution is exothermic, and <br>
(B) is correct

**Q6.J5 🔴 ⭐**
Mole fraction of O₂ in water = 1.5×10⁻⁵ when partial pressure of O₂ = 1.0 bar. What is K_H?<br>
<br>
(A) 1.5×10⁻⁵ bar  <br>
(B) 6.67×10⁴ bar  <br>
(C)
 1.5×10⁵ bar  <br>
(D) 15 bar

**Q6.J6 🟡**
**Assertion <br>
(A):** At a given temperature, hydrogen (H₂) has a higher K_H value in water than ammonia (NH₃).
**Reason (R):** H₂ is non-polar while NH₃ forms hydrogen bonds with water, making NH₃ more soluble.
<br>
(A) Both A and R are true, R is correct explanation
<br>
(B) Both A and R are true, R is NOT correct explanation
<br>
(C)
 A is true but R is false
<br>
(D) A is false but R is true

**Q6.J7 🔴**
A gas has a solubility of 0.04 g/L at 1 atm. At what pressure will its solubility be 0.1 g/L at the same temperature?<br>
<br>
(A) 2.0 atm  <br>
(B) 2.5 atm  <br>
(C)
 0.4 atm  <br>
(D) 1.5 atm

**Q6.J8 🔴**
At 40 m depth in seawater, total pressure is 5 atm. If air is 79% N₂ (K_H = 8.42×10⁴ bar) and the diver breathes compressed air, what is χ_N₂ in blood?<br> (1 atm ≈ 1 bar)
<br>
(A) 9.38×10⁻⁶  <br>
(B) 4.69×10⁻⁵  <br>
(C)
 2.34×10⁻⁵  <br>
(D) 7.03×10⁻⁵

**Q6.J9 🟡**
**Statement I:** K_H for a gas increases with increasing temperature.
**Statement II:** K_H for a gas is independent of the nature of the gas.
<br>
(A) Both statements are true
<br>
(B) Statement I true, II false
<br>
(C)
 I false, II true
<br>
(D) Both false

**Q6.J10 🟡**
**Assertion <br>
(A):** When a bottle of cold drink is opened, CO₂ fizzes out.
**Reason (R):** Opening reduces pressure, so solubility of CO₂ decreases.
<br>
(A) Both A and R are true, R is correct explanation
<br>
(B) Both A and R are true, R is NOT correct explanation
<br>
(C)
 A is true but R is false
<br>
(D) A is false but R is true

**Q6.J11 🟡**
K_H for CO₂ in water is 1.67×10³ bar at 298 K. The mole fraction of CO₂ in water when partial pressure of CO₂ is 0.835 bar:
<br>
(A) 5.0×10⁻⁴  <br>
(B) 2.0×10³  <br>
(C)
 1.67×10⁻³  <br>
(D) 8.35×10⁻²

**Q6.J12 🔴**
At sea level, P_O₂ = 0.21 bar. At the top of Mount Everest, P_total = 0.33 bar. What percentage of sea-level O₂ dissolves in blood at the summit?<br> (Assume temperature constant)
<br>
(A) 33%  <br>
(B) 21%  <br>
(C)
 7%  <br>
(D) 11%

**Q6.J13 🔴**
**Assertion <br>
(A):** Scuba divers use a mixture of oxygen and helium rather than oxygen and nitrogen for deep dives.
**Reason (R):** Helium has a lower solubility in blood than nitrogen at high pressures.
<br>
(A) Both A and R are true, R is correct explanation
<br>
(B) Both A and R are true, R is NOT correct explanation
<br>
(C)
 A is true but R is false
<br>
(D) A is false but R is true

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**6.J1 → Answer: <br>
(C)
**
- Different gases have DIFFERENT K_H values at the same temperature (their interaction with solvent differs). **<br>
(C)
 is incorrect ✓**

**6.J2 → Answer: <br>
(B)**
- P_gas = K_H × χ_gas = K_H(1 − χ_solvent) = −K_H × χ_solvent + K_H
- Slope = **−K_H ✓**

**6.J3 → Answer: <br>
(B)**
- χ_CO₂ = 0.835/1670 = 5×10⁻⁴
- n_water in 0.9L = 900/18 = 50 mol
- n_CO₂ = 5×10⁻⁴ × 50 = 0.025 mol = **25 mmol ✓**

**6.J4 → Answer: <br>
(D)**
- K_H increases with T → solubility decreases with T → dissolution is **exothermic**
- Both the conclusion about solubility <br>
(B) and enthalpy sign are correct → **<br>
(D) ✓**

**6.J5 → Answer: <br>
(B)**
- K_H = P_gas/χ_gas = 1.0/(1.5×10⁻⁵) = **6.67×10⁴ bar ✓**

**6.J6 → Answer: <br>
(A)**
- H₂ is non-polar → weak interaction with water → high K_H. NH₃ forms H-bonds with water → low K_H (high solubility). R correctly explains A.

**6.J7 → Answer: <br>
(B)**
- S ∝ P → P₂ = P₁ × (S₂/S₁) = 1 × (0.1/0.04) = **2.5 atm**

**6.J8 → Answer: <br>
(B)**
- P_N₂ = 0.79 × 5 = 3.95 bar ≈ 3.95 atm
- χ_N₂ = 3.95/(8.42×10⁴) = **4.69×10⁻⁵**

**6.J9 → Answer: <br>
(B)**
- Statement I is true: K_H increases with temperature.
- Statement II is false: K_H depends on the nature of the gas (different gases have different K_H).

**6.J10 → Answer: <br>
(A)**
- Opening the bottle reduces pressure → CO₂ solubility drops → CO₂ fizzes out. R correctly explains A.

**6.J11 → Answer: <br>
(A)**
- χ_CO₂ = 0.835/(1.67×10³) = **5.0×10⁻⁴**

**6.J12 → Answer: <br>
(A)**
- P_O₂(Everest) = 0.33 × 0.21 = 0.0693 bar
- Ratio = 0.0693/0.21 = 0.33 = **33%**

**6.J13 → Answer: <br>
(A)**
- He has higher K_H (146 kbar) than N₂ (86.2 kbar), meaning He has LOWER solubility in blood.
- R states "lower solubility" which is correct. Both A and R are true, R is correct explanation.
</details>

---

## Key Takeaways from Chapter 6

| Rule | Detail |
|------|--------|
| Henry's Law | P_gas = K_H × χ_gas |
| High K_H | Low solubility |
| K_H ↑ with T | Gas solubility ↓ with T |
| Gas dissolution | Exothermic |
| Solid dissolution | Usually endothermic (solubility ↑ with T) |
| Graph P vs. χ_gas | Slope = +K_H |
| Graph P vs. χ_solvent | Slope = −K_H, intercept = K_H |

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
| 6.S1 | **Assertion (A):** The value of Henry's constant ($K_H$) is greater for oxygen ($O_2$) than for helium ($He$) at the same temperature.<br>**Reason (R):** Helium is a noble gas and is less soluble in water than oxygen. | 🔴 |
| 6.S2 | **Statement I:** As the temperature of water increases, the solubility of dissolved oxygen gas decreases.<br>**Statement II:** The dissolution of a gas in a liquid is an endothermic process. | 🟢 |
| 6.S3 | **Assertion (A):** Aquatic species are more comfortable in cold water than in warm water.<br>**Reason (R):** The value of $K_H$ for oxygen decreases with a decrease in temperature, leading to higher dissolved oxygen. | 🟡 |
| 6.S4 | **Statement I:** According to Henry's Law, $P = K_H \times \chi$. The unit of $K_H$ must always be in $bar$ or $atm$.<br>**Statement II:** The unit of $K_H$ depends on the unit of partial pressure used, as mole fraction is dimensionless. | 🟢 |
| 6.S5 | **Assertion (A):** The slope of a plot of partial pressure of a gas ($P$) versus the mole fraction of the solvent ($\chi_{solvent}$) is $-K_H$.<br>**Reason (R):** $P = K_H(1 - \chi_{solvent}) = -K_H \chi_{solvent} + K_H$. | 🟡 |
| 6.S6 | **Statement I:** If the pressure of a gas over a liquid is doubled, the value of its Henry's constant $K_H$ also doubles.<br>**Statement II:** $K_H$ is a function of the nature of the gas and temperature, but is independent of pressure. | 🟡 |
| 6.S7 | **Assertion (A):** Carbon dioxide is more soluble in water than oxygen under identical conditions of temperature and pressure.<br>**Reason (R):** $CO_2$ is a polar molecule and reacts with water to form carbonic acid, while $O_2$ is non-polar. | 🟢 |
| 6.S8 | **Statement I:** The solubility of most solid solutes in liquid solvents increases with an increase in temperature.<br>**Statement II:** The dissolution of most solid solutes is an exothermic process. | 🟡 |
| 6.S9 | **Assertion (A):** A bottle of soda water fizzes when opened.<br>**Reason (R):** The partial pressure of $CO_2$ outside the bottle is much lower than inside, causing a sudden decrease in its solubility. | 🟢 |
| 6.S10 | **Statement I:** Scuba divers carry tanks filled with air diluted with helium.<br>**Statement II:** Helium has a very low Henry's constant, meaning it is highly soluble in blood at high pressures. | 🔴 |
| 6.S11 | **Assertion (A):** If gas A has $K_H = 10^5\text{ bar}$ and gas B has $K_H = 10^4\text{ bar}$, gas B is ten times more soluble than gas A at the same pressure.<br>**Reason (R):** Solubility (mole fraction) is inversely proportional to $K_H$ at constant pressure. | 🟡 |
| 6.S12 | **Statement I:** The value of $K_H$ increases as the temperature of the solution increases.<br>**Statement II:** Higher temperature shifts the equilibrium of gas dissolution in the forward direction. | 🟢 |
| 6.S13 | **Assertion (A):** People living at high altitudes often suffer from anoxia (weakness and inability to think clearly).<br>**Reason (R):** At high altitudes, the partial pressure of oxygen is less than at ground level, leading to low concentrations of dissolved oxygen in the blood. | 🟢 |
| 6.S14 | **Statement I:** The dissolution of a gas in a liquid involves a decrease in entropy ($\Delta S < 0$).<br>**Statement II:** Since the process is spontaneous ($\Delta G < 0$) and $\Delta S < 0$, it must be highly endothermic to compensate. | 🟡 |
| 6.S15 | **Assertion (A):** Raoult's law becomes a special case of Henry's law when $K_H$ becomes equal to the vapor pressure of the pure solvent ($P^\circ$).<br>**Reason (R):** Both laws express the partial pressure of a component as proportional to its mole fraction. | 🟡 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**6.S1 → Answer: <br>
(D) A is false but R is true.**
- A is false: Higher $K_H$ means LOWER solubility. Since Helium is less soluble, it has a HIGHER $K_H$ than oxygen.
- R is true: Helium is indeed less soluble because it's a non-polar noble gas with extremely weak intermolecular forces.

**6.S2 → Statement I is True, Statement II is False.**
- Statement I is true: Heating drives gases out of solution.
- Statement II is false: Gas dissolution is generally an EXOTHERMIC process ($\Delta H < 0$).

**6.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Cold water $\rightarrow$ lower temperature $\rightarrow$ lower $K_H$ $\rightarrow$ higher solubility of $O_2$.

**6.S4 → Statement I is False, Statement II is True.**
- Statement I is false: $K_H$ can be in $torr$, $mmHg$, $Pa$, $kPa$, $bar$, $atm$, etc.
- Statement II is true: Since $\chi$ is unitless, $P = K_H \times \chi$ implies the units of $K_H$ must exactly match the units of $P$.

**6.S5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is the standard algebraic derivation of the negative slope when plotting against the *solvent's* mole fraction.

**6.S6 → Statement I is False, Statement II is True.**
- Statement I is false: If $P$ is doubled, the mole fraction $\chi$ (solubility) doubles. $K_H$ remains constant.
- Statement II is true: $K_H$ is a constant for a given gas-solvent pair at a fixed temperature.

**6.S7 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Chemical reaction with the solvent (forming $H_2CO_3$) greatly enhances solubility.

**6.S8 → Statement I is True, Statement II is False.**
- Statement I is true: E.g., sugar or salt in hot water.
- Statement II is false: Most solid dissolution is ENDOTHERMIC. (Heating shifts equilibrium forward).

**6.S9 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- High $P$ inside = high solubility. Open cap $\rightarrow$ $P$ drops to atmospheric $\rightarrow$ solubility drops $\rightarrow$ gas escapes as bubbles.

**6.S10 → Statement I is True, Statement II is False.**
- Statement I is true: It prevents the bends and nitrogen narcosis.
- Statement II is false: Helium has a very HIGH $K_H$ (low solubility), which is exactly *why* they use it—it doesn't dissolve much in the blood even at high pressure.

**6.S11 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $\chi = P / K_H$. If $K_H$ is $10$ times smaller, $\chi$ is $10$ times larger.

**6.S12 → Statement I is True, Statement II is False.**
- Statement I is true: $K_H$ increases with $T$.
- Statement II is false: Higher temperature shifts the EXOTHERMIC dissolution equilibrium in the REVERSE direction (gas escapes).

**6.S13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is a direct application of Henry's Law in biology.

**6.S14 → Statement I is True, Statement II is False.**
- Statement I is true: Gas (high entropy) $\rightarrow$ dissolved state (lower entropy). $\Delta S < 0$.
- Statement II is false: $\Delta G = \Delta H - T\Delta S$. For $\Delta G < 0$ when $\Delta S$ is negative, the $-T\Delta S$ term is positive. Thus, $\Delta H$ MUST be highly NEGATIVE (exothermic) to overpower it and make $\Delta G$ negative.

**6.S15 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Henry: $P = K_H \chi_{solute}$. Raoult: $P_A = P_A^\circ \chi_A$. They have identical mathematical forms.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q6.M1 🟢**
Which of the following gases will have the lowest value of Henry's law constant ($K_H$) in water at $298\text{ K}$?<br>
<br>
(A) $He$
<br>
(B) $N_2$
<br>
(C)
 $O_2$
<br>
(D) $CO_2$

**Q6.M2 🟡 (The "Slope Reversal" Trap)**
For a given gas in a liquid, the plot of partial pressure of the gas ($P$) versus the mole fraction of the GAS ($\chi_{gas}$) gives a straight line. What is the y-intercept of this line?<br>
<br>
(A) $K_H$
<br>
(B) $-K_H$
<br>
(C)
 Zero
<br>
(D) $P^\circ$

**Q6.M3 🔴**
The Henry's law constant for dissolution of $CH_4$ in benzene at $298\text{ K}$ is $4.27 \times 10^5\text{ mmHg}$. The solubility of $CH_4$ in benzene at $298\text{ K}$ under $760\text{ mmHg}$ is:
<br>
(A) $1.78 \times 10^{-3}$
<br>
(B) $1.78 \times 10^{-5}$
<br>
(C)
 $5.6 \times 10^2$
<br>
(D) $4.27 \times 10^5$

**Q6.M4 🟡**
If the solubility of a gas is $0.05\text{ mol/L}$ at a pressure of $2\text{ atm}$, what will be its solubility at $6\text{ atm}$ at the same temperature?<br>
<br>
(A) $0.05\text{ mol/L}$
<br>
(B) $0.15\text{ mol/L}$
<br>
(C)
 $0.30\text{ mol/L}$
<br>
(D) $0.016\text{ mol/L}$

**Q6.M5 🟡 (The "Temperature Paradox" Trap)**
You have a glass of cold water ($10^\circ\text{C}$) and a glass of warm water ($40^\circ\text{C}$). You dissolve $O_2$ gas in both until saturation at $1\text{ atm}$ pressure. Which glass contains a greater mole fraction of $O_2$, and in which glass is the $K_H$ of $O_2$ higher?<br>
<br>
(A) Greater $\chi_{O_2}$ in cold; Higher $K_H$ in warm
<br>
(B) Greater $\chi_{O_2}$ in warm; Higher $K_H$ in cold
<br>
(C)
 Greater $\chi_{O_2}$ in cold; Higher $K_H$ in cold
<br>
(D) Greater $\chi_{O_2}$ in warm; Higher $K_H$ in warm

**Q6.M6 🔴**
$K_H$ for $Ar_{(g)}$, $CO_{2(g)}$, $HCHO_{(g)}$, and $CH_{4(g)}$ are $40.39$, $1.67$, $1.83 \times 10^{-5}$, and $0.413$, respectively. Arrange these gases in the order of their increasing solubility.
<br>
(A) $HCHO < CH_4 < CO_2 < Ar$
<br>
(B) $HCHO < CO_2 < CH_4 < Ar$
<br>
(C)
 $Ar < CO_2 < CH_4 < HCHO$
<br>
(D) $Ar < CH_4 < CO_2 < HCHO$

**Q6.M7 🟡**
According to Henry's law, a graph of the mass of a gas dissolved per unit volume of solvent ($m$) versus the pressure of the gas ($P$) is a straight line passing through the origin. The slope of this line is related to:
<br>
(A) The boiling point of the solvent
<br>
(B) The volume of the container
<br>
(C)
 The specific Henry's law constant for the mass-pressure relationship
<br>
(D) Universal gas constant $R$

**Q6.M8 🟢**
The dissolution of a solid in a liquid is an endothermic process. According to Le Chatelier's principle, its solubility should:
<br>
(A) Increase with an increase in pressure
<br>
(B) Decrease with an increase in temperature
<br>
(C)
 Increase with an increase in temperature
<br>
(D) Be independent of temperature

**Q6.M9 🔴 (The "Unit Mismatch" Trap)**
Henry's law constant for $O_2$ in water is $4.6 \times 10^4\text{ bar}$. What is the mole fraction of $O_2$ dissolved in water if the partial pressure of $O_2$ is $0.2\text{ atm}$?<br> ($1\text{ atm} = 1.013\text{ bar}$).
<br>
(A) $4.34 \times 10^{-6}$
<br>
(B) $4.40 \times 10^{-6}$
<br>
(C)
 $2.3 \times 10^5$
<br>
(D) $0.2 \times 10^{-4}$

**Q6.M10 🟡**
Which condition is NOT required for Henry's Law to be strictly valid?<br>
<br>
(A) The pressure should not be too high.
<br>
(B) The temperature should not be too low.
<br>
(C)
 The gas should not undergo chemical reaction with the solvent.
<br>
(D) The gas must be highly soluble in the solvent.

**Q6.M11 🔴**
A mixture of two gases $X$ and $Y$ exerts a total pressure of $10\text{ atm}$ over a solvent. The mole fraction of $X$ in the gas phase is $0.6$. If the $K_H$ values for $X$ and $Y$ are $2 \times 10^4\text{ atm}$ and $1 \times 10^4\text{ atm}$ respectively, what is the ratio of mole fractions of $X$ and $Y$ dissolved in the liquid?<br> ($\chi_{X(liquid)} : \chi_{Y(liquid)}$)
<br>
(A) $3:4$
<br>
(B) $3:2$
<br>
(C)
 $4:3$
<br>
(D) $1:1$

**Q6.M12 🟡**
At a given temperature, oxygen gas is bubbled through water. The concentration of dissolved oxygen is found to be $0.04\text{ g/L}$ at a pressure of $1\text{ atm}$. If the pressure is increased to $2.5\text{ atm}$, what will be the concentration of dissolved oxygen?<br>
<br>
(A) $0.04\text{ g/L}$
<br>
(B) $0.016\text{ g/L}$
<br>
(C)
 $0.10\text{ g/L}$
<br>
(D) $0.25\text{ g/L}$

**Q6.M13 🟢**
The "bends" experienced by deep-sea divers is primarily due to:
<br>
(A) High solubility of $O_2$ at high pressure
<br>
(B) Low solubility of $N_2$ at high pressure
<br>
(C)
 Sudden decrease in the solubility of $N_2$ in blood upon rapid ascent
<br>
(D) Chemical reaction of He with blood cells

**Q6.M14 🔴 (The "Reverse Formula" Trap)**
An experiment shows that $0.1\text{ moles}$ of a gas dissolves in $9.9\text{ moles}$ of water at $2\text{ atm}$. If Henry's law is written as $\chi_{gas} = K' \times P$, what is the value of $K'$?<br>
<br>
(A) $20\text{ atm}^{-1}$
<br>
(B) $0.005\text{ atm}^{-1}$
<br>
(C)
 $200\text{ atm}$
<br>
(D) $0.01\text{ atm}^{-1}$

**Q6.M15 🟡**
If a gas undergoes dissociation (e.g., $HCl \rightarrow H^+ + Cl^-$) when dissolved in water, Henry's Law:
<br>
(A) Applies perfectly to the total dissolved concentration
<br>
(B) Fails because the gas chemically changes state in the solvent
<br>
(C)
 Applies only at extremely high pressures
<br>
(D) Applies only at extremely high temperatures

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q6.M1 → Answer: <br>
(D)**
- $K_H$ is inversely proportional to solubility.
- $CO_2$ is polar/reactive with water, making it the most soluble among the choices.
- Most soluble = lowest $K_H$.

**Q6.M2 → Answer: <br>
(C)
**
- Equation: $P_{gas} = K_H \times \chi_{gas}$.
- This is in the form $y = mx + c$.
- Slope $m = K_H$. Y-intercept $c = 0$.
- Trap: <br>
(B) applies to the plot against $\chi_{solvent}$.

**Q6.M3 → Answer: <br>
(A)**
- $\chi = \frac{P}{K_H} = \frac{760}{4.27 \times 10^5}$.
- $760 / 427000 = 1.779 \times 10^{-3} \approx 1.78 \times 10^{-3}$.

**Q6.M4 → Answer: <br>
(B)**
- Solubility $\propto$ Pressure.
- $S_1 / P_1 = S_2 / P_2 \rightarrow 0.05 / 2 = S_2 / 6$.
- $S_2 = 0.05 \times 3 = 0.15\text{ mol/L}$.

**Q6.M5 → Answer: <br>
(A)**
- Cold water: Lower temperature means lower $K_H$, which means HIGHER solubility ($\chi_{O_2}$).
- Warm water: Higher temperature means HIGHER $K_H$, which means LOWER solubility.

**Q6.M6 → Answer: <br>
(C)
**
- Solubility is inversely proportional to $K_H$.
- Arrange $K_H$ from highest to lowest to get solubility from lowest to highest.
- $K_H$: $Ar (40.39) > CH_4 (0.413) > CO_2 (1.67) > HCHO (1.83 \times 10^{-5})$.
- *Wait, let me re-check the values in the question:*
  $Ar: 40.39$
  $CO_2: 1.67$
  $HCHO: 1.83 \times 10^{-5}$
  $CH_4: 0.413$
- Order of $K_H$ (decreasing): $Ar > CO_2 > CH_4 > HCHO$.
- Therefore, Order of solubility (increasing): $Ar < CO_2 < CH_4 < HCHO$.

**Q6.M7 → Answer: <br>
(C)
**
- Henry's law can also be written in terms of mass: $m = K_H' \times P$. The slope is the modified Henry's constant for those specific units.

**Q6.M8 → Answer: <br>
(C)
**
- Endothermic process ($\Delta H > 0$): By Le Chatelier's Principle, increasing temperature adds heat, shifting the equilibrium forward to dissolve more solid.

**Q6.M9 → Answer: <br>
(B)**
- Convert Pressure to bar to match $K_H$: $P = 0.2\text{ atm} \times 1.013\text{ bar/atm} = 0.2026\text{ bar}$.
- $\chi = \frac{P}{K_H} = \frac{0.2026}{4.6 \times 10^4} = 0.0440 \times 10^{-4} = 4.40 \times 10^{-6}$.
- Trap: <br>
(A) Using $0.2$ directly without unit conversion gives $4.34 \times 10^{-6}$.

**Q6.M10 → Answer: <br>
(D)**
- Henry's law is actually an IDEAL gas law equivalent for solutions. It works best for gases that are slightly or moderately soluble. If a gas is highly soluble, it often means it's reacting with the solvent (like $NH_3$ in water), causing massive deviations from the simple linear Henry's Law. So, requiring it to be "highly soluble" is false.
- Conditions for validity: Low pressure, high temperature, no association/dissociation.

**Q6.M11 → Answer: <br>
(A)**
- Partial pressure of $X$ in gas: $P_X = 0.6 \times 10\text{ atm} = 6\text{ atm}$.
- Partial pressure of $Y$ in gas: $P_Y = 0.4 \times 10\text{ atm} = 4\text{ atm}$.
- In liquid: $\chi_X = \frac{P_X}{K_{H,X}} = \frac{6}{2 \times 10^4} = 3 \times 10^{-4}$.
- In liquid: $\chi_Y = \frac{P_Y}{K_{H,Y}} = \frac{4}{1 \times 10^4} = 4 \times 10^{-4}$.
- Ratio $\chi_X : \chi_Y = 3 : 4$.

**Q6.M12 → Answer: <br>
(C)
**
- $S \propto P$.
- $S_2 = S_1 \times (P_2 / P_1) = 0.04 \times (2.5 / 1.0) = 0.10\text{ g/L}$.

**Q6.M13 → Answer: <br>
(C)
**
- At high pressure underwater, $N_2$ dissolves in blood. Upon rapid ascent, pressure drops, solubility plummets, and $N_2$ bubbles out into the veins.

**Q6.M14 → Answer: <br>
(B)**
- The question uses the reverse format: $\chi = K' \times P$. Here $K' = 1/K_H$.
- Mole fraction of gas $\chi_{gas} = \frac{0.1}{0.1 + 9.9} = \frac{0.1}{10.0} = 0.01$.
- $\chi = K' \times P \rightarrow 0.01 = K' \times 2 \rightarrow K' = 0.005\text{ atm}^{-1}$.
- Trap: Using the standard $P = K_H \chi \rightarrow 2 = K_H \times 0.01 \rightarrow K_H = 200$.

**Q6.M15 → Answer: <br>
(B)**
- Henry's Law applies to the undissociated molecular species in equilibrium with the gas. If the gas dissociates or associates, the simple linear relationship $P \propto$ total dissolved concentration fails. It only applies strictly if there is no chemical interaction/change.
</details>

---

*Next: [Chapter 7 — Vapour Pressure & Raoult's Law →](./07_vapour_pressure_and_raoults_law.md)*
