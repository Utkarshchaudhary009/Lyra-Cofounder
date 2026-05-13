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

Why? Gases with stronger intermolecular attraction to water molecules (polar gases, gases that form hydrogen bonds) dissolve more and have lower K_H.

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
**Q:** Compare K_H values of SO₂ and H₂ in water. Which is larger? 🟡

```
SO₂ is polar; H₂ is non-polar.
Polar gas ↔ polar solvent (water) → stronger interaction → higher solubility.
Higher solubility → Lower K_H.

∴ (K_H)_H₂ > (K_H)_SO₂

Answer: K_H of H₂ is greater than K_H of SO₂.
```

#### Solved Example 6.2
**Q:** Which statement about Henry's Law is INCORRECT?
(A) Different gases have different K_H at same temperature
(B) K_H increases with temperature
(C) Partial pressure of gas ∝ mole fraction of gas
(D) Higher K_H at given pressure = higher solubility 🟡

```
(A) True ✓ — each gas has unique K_H
(B) True ✓ — K_H increases as T rises (solubility falls)
(C) True ✓ — that IS Henry's Law (P = K_H × χ)
(D) FALSE ✗ — Higher K_H means LOWER solubility
              (P = K_H × χ; at fixed P, higher K_H → smaller χ)

Answer: (D) is incorrect.
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 6.1a | Why does the solubility of CO₂ in a carbonated drink decrease when the cap is removed? | 🟢 |
| 6.1b | Why do scuba divers ascend slowly? | 🟡 |
| 6.1c | Explain why aquatic life struggles in hot water. | 🟡 |
| 6.1d | Among O₂, CO₂, and He, arrange in increasing order of K_H (at same temperature in water). | 🟡 |
| 6.1e | K_H for N₂ is 8.42 × 10⁴ bar and for CO₂ is 1.67 × 10³ bar. Which gas is more soluble? | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**6.1a:** By Henry's Law, solubility ∝ P_gas. Inside the bottle, CO₂ is under high pressure → high solubility. When cap is removed, P_CO₂ drops drastically → solubility drops → CO₂ escapes as bubbles.

**6.1b:** At depth, high water pressure causes N₂ to dissolve in blood (high P → high χ_N₂). If ascent is rapid, pressure drops suddenly → N₂ solubility plummets → N₂ forms dangerous bubbles in bloodstream (decompression sickness / "the bends").

**6.1c:** Gas dissolution is exothermic. Hot water → equilibrium shifts backward → O₂ escapes → less dissolved O₂ available for fish and aquatic organisms.

**6.1d:** He is inert/non-polar (highest K_H); O₂ is non-polar (medium K_H); CO₂ is polar and reacts with water (lowest K_H).
Order of increasing K_H: **CO₂ < O₂ < He**
(equivalently: CO₂ most soluble, He least soluble)

**6.1e:** Lower K_H = higher solubility. K_H(CO₂) = 1.67×10³ < K_H(N₂) = 8.42×10⁴. **CO₂ is more soluble.**
</details>

---

### Type 2: Graph Interpretation

**Pattern:** Interpret P vs. χ graphs for Henry's Law.

#### Solved Example 6.3
**Q:** Two gases A and B are plotted on a P_gas vs. χ_gas graph. Gas B has a steeper slope. Which gas has greater solubility? 🟡

```
Slope of P vs. χ_gas = K_H

Gas B has higher slope → higher K_H → lower solubility.
Gas A has lower slope → lower K_H → higher solubility.

Answer: Gas A has greater solubility.
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 6.2a | What does the slope represent in a P_gas vs. χ_gas plot? | 🟢 |
| 6.2b | In a plot of P_gas vs. χ_solvent, what is the slope and y-intercept? | 🟡 |
| 6.2c | Two gases A and B are plotted on P vs. χ. If slope_A > slope_B, which has higher solubility? | 🟢 |
| 6.2d | A gas shows a steeper P vs. χ curve at 40°C than at 25°C. What does this tell you about the effect of temperature on K_H? | 🟡 |

<details>
<summary>💡 Solutions for Type 2</summary>

**6.2a:** **Slope = K_H (Henry's constant)**

**6.2b:** Slope = **−K_H** (negative); Y-intercept = **K_H**

**6.2c:** slope_A > slope_B → K_H(A) > K_H(B) → **Gas B has higher solubility**

**6.2d:** Steeper slope at 40°C → higher K_H → **K_H increases with temperature**, meaning solubility of gas decreases as temperature rises.
</details>

---

### Type 3: Numerical — Direct Henry's Law Calculation

**Pattern:** Given K_H and P_gas → find χ_gas → convert to moles dissolved.

#### Solved Example 6.4
**Q:** O₂ is bubbled through water at 303 K. K_H = 46.82 kbar, P_O₂ = 0.920 bar. How many millimoles of O₂ dissolve in 1 L of water? 🔴 ⭐

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
</details>

---

### Type 4: Solid Solubility — Temperature Effect

**Pattern:** Conceptual + graph reading for solid solubility.

#### Solved Example 6.6
**Q:** How does the solubility of a solid change with temperature compared to a gas? Explain. 🟢

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
| 6.4b | Why does warm soda go flat faster than cold soda? | 🟢 |
| 6.4c | A solubility curve shows decreasing solubility with increasing temperature for a salt. What does this indicate about the dissolution enthalpy? | 🟡 |

<details>
<summary>💡 Solutions for Type 4</summary>

**6.4a:** Endothermic dissolution + heating → forward reaction favoured → **Solubility increases.**

**6.4b:** Warm temperature → K_H of CO₂ increases → χ_CO₂ decreases at same atmospheric pressure → CO₂ escapes → soda loses fizz faster.

**6.4c:** Decreasing solubility with temperature → dissolution is **exothermic** (ΔH_dissolution < 0). Heating shifts equilibrium backward, reducing solubility.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 6.M1 | K_H for O₂ = 46.82 kbar at 303 K. Air = 21% O₂ by mole at 1 bar total pressure. Find mass of O₂ dissolved in 1 L of water at sea level. ⭐ | T3 | 🔴 |
| 6.M2 | A soft drink contains CO₂ at 4 bar pressure (K_H = 1600 bar). After opening, pressure drops to 0.0004 bar (partial pressure of CO₂ in air). Compare χ_CO₂ before and after opening. | T1+T3 | 🔴 |
| 6.M3 | Two gases A and B at same temperature. K_H(A) = 2×10⁴ bar, K_H(B) = 5×10³ bar. Both are at P = 1 bar. Find the ratio χ_A:χ_B. | T2+T3 | 🟡 |

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
- χ_A = P/K_H(A) = 1/(2×10⁴) = 5×10⁻⁵
- χ_B = P/K_H(B) = 1/(5×10³) = 2×10⁻⁴
- **χ_A:χ_B = 5×10⁻⁵ : 2×10⁻⁴ = 1:4** (B is 4× more soluble)
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 6.B1 | State Henry's Law. Give its mathematical expression. *(NCERT)* | 🟢 |
| 6.B2 | State any two applications of Henry's Law. | 🟢 |
| 6.B3 | K_H of CO₂ at 298 K = 1.67×10³ bar. If CO₂ exerts partial pressure of 0.835 bar, find χ_CO₂ in the solution. | 🟡 |
| 6.B4 | Why is the solubility of a gas in a liquid inversely proportional to temperature? | 🟡 |
| 6.B5 | The Henry's law constant for O₂ dissolved in water is 46.82 kbar at 303 K. If the partial pressure of O₂ is 0.920 bar, what is the mole fraction of O₂ in water? *(NCERT)* ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**6.B1:** Henry's Law: At constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of the gas above the liquid. Formula: **P_gas = K_H × χ_gas**

**6.B2:** (Any two): (1) Carbonated beverages — CO₂ dissolved under high pressure. (2) Scuba diving — divers breathe pressurized air; rapid ascent causes "bends." (3) Blood oxygen transport — O₂ solubility depends on P_O₂ in lungs.

**6.B3:** χ_CO₂ = P_CO₂/K_H = 0.835/(1.67×10³) = **5.0×10⁻⁴**

**6.B4:** Gas dissolution is exothermic (ΔH < 0). By Le Chatelier's principle, increasing temperature favours the reverse reaction (gas escaping from solution). Thus solubility decreases as temperature increases.

**6.B5:** χ_O₂ = P_O₂/K_H = 0.920/(46.82×10³) = 0.920/46820 = **1.965×10⁻⁵**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q6.J1 🟡 ⭐**
Which of the following about Henry's Law is INCORRECT?
(A) Higher K_H = lower solubility
(B) K_H increases with temperature
(C) K_H is the same for all gases at same temperature
(D) Partial pressure of gas ∝ its mole fraction in solution

**Q6.J2 🟡**
On a graph of P_gas (y-axis) vs. χ_solvent (x-axis), the slope of the Henry's Law line is:
(A) +K_H  (B) −K_H  (C) 1/K_H  (D) Zero

**Q6.J3 🔴 ⭐**
CO₂ is dissolved in water at 298 K (K_H = 1.67×10³ bar). x mmol of CO₂ dissolves in 0.9 L water at P_CO₂ = 0.835 bar. Find x.
(A) 10  (B) 25  (C) 50  (D) 5

**Q6.J4 🔴**
If K_H of a gas at 300 K is 2×10⁴ bar and at 400 K is 4×10⁴ bar, what can you conclude?
(A) Solubility increases with temperature
(B) Solubility decreases with temperature
(C) Dissolution is endothermic
(D) Dissolution is exothermic, and (B) is correct

**Q6.J5 🔴 ⭐**
Mole fraction of O₂ in water = 1.5×10⁻⁵ when partial pressure of O₂ = 1.0 bar. What is K_H?
(A) 1.5×10⁻⁵ bar  (B) 6.67×10⁴ bar  (C) 1.5×10⁵ bar  (D) 15 bar

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**6.J1 → Answer: (C)**
- Different gases have DIFFERENT K_H values at the same temperature (their interaction with solvent differs). **(C) is incorrect ✓**

**6.J2 → Answer: (B)**
- P_gas = K_H × χ_gas = K_H(1 − χ_solvent) = −K_H × χ_solvent + K_H
- Slope = **−K_H ✓**

**6.J3 → Answer: (B)**
- χ_CO₂ = 0.835/1670 = 5×10⁻⁴
- n_water in 0.9L = 900/18 = 50 mol
- n_CO₂ = 5×10⁻⁴ × 50 = 0.025 mol = **25 mmol ✓**

**6.J4 → Answer: (D)**
- K_H increases with T → solubility decreases with T → dissolution is **exothermic**
- Both the conclusion about solubility (B) and enthalpy sign are correct → **(D) ✓**

**6.J5 → Answer: (B)**
- K_H = P_gas/χ_gas = 1.0/(1.5×10⁻⁵) = **6.67×10⁴ bar ✓**
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
  (A) Both A and R are true, and R is the correct explanation of A.
  (B) Both A and R are true, but R is NOT the correct explanation of A.
  (C) A is true but R is false.
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

**6.S1 → Answer: (D) A is false but R is true.**
- A is false: Higher $K_H$ means LOWER solubility. Since Helium is less soluble, it has a HIGHER $K_H$ than oxygen.
- R is true: Helium is indeed less soluble because it's a non-polar noble gas with extremely weak intermolecular forces.

**6.S2 → Statement I is True, Statement II is False.**
- Statement I is true: Heating drives gases out of solution.
- Statement II is false: Gas dissolution is generally an EXOTHERMIC process ($\Delta H < 0$).

**6.S3 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Cold water $\rightarrow$ lower temperature $\rightarrow$ lower $K_H$ $\rightarrow$ higher solubility of $O_2$.

**6.S4 → Statement I is False, Statement II is True.**
- Statement I is false: $K_H$ can be in $torr$, $mmHg$, $Pa$, $kPa$, $bar$, $atm$, etc.
- Statement II is true: Since $\chi$ is unitless, $P = K_H \times \chi$ implies the units of $K_H$ must exactly match the units of $P$.

**6.S5 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This is the standard algebraic derivation of the negative slope when plotting against the *solvent's* mole fraction.

**6.S6 → Statement I is False, Statement II is True.**
- Statement I is false: If $P$ is doubled, the mole fraction $\chi$ (solubility) doubles. $K_H$ remains constant.
- Statement II is true: $K_H$ is a constant for a given gas-solvent pair at a fixed temperature.

**6.S7 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Chemical reaction with the solvent (forming $H_2CO_3$) greatly enhances solubility.

**6.S8 → Statement I is True, Statement II is False.**
- Statement I is true: E.g., sugar or salt in hot water.
- Statement II is false: Most solid dissolution is ENDOTHERMIC. (Heating shifts equilibrium forward).

**6.S9 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- High $P$ inside = high solubility. Open cap $\rightarrow$ $P$ drops to atmospheric $\rightarrow$ solubility drops $\rightarrow$ gas escapes as bubbles.

**6.S10 → Statement I is True, Statement II is False.**
- Statement I is true: It prevents the bends and nitrogen narcosis.
- Statement II is false: Helium has a very HIGH $K_H$ (low solubility), which is exactly *why* they use it—it doesn't dissolve much in the blood even at high pressure.

**6.S11 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- $\chi = P / K_H$. If $K_H$ is $10$ times smaller, $\chi$ is $10$ times larger.

**6.S12 → Statement I is True, Statement II is False.**
- Statement I is true: $K_H$ increases with $T$.
- Statement II is false: Higher temperature shifts the EXOTHERMIC dissolution equilibrium in the REVERSE direction (gas escapes).

**6.S13 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This is a direct application of Henry's Law in biology.

**6.S14 → Statement I is True, Statement II is False.**
- Statement I is true: Gas (high entropy) $\rightarrow$ dissolved state (lower entropy). $\Delta S < 0$.
- Statement II is false: $\Delta G = \Delta H - T\Delta S$. For $\Delta G < 0$ when $\Delta S$ is negative, the $-T\Delta S$ term is positive. Thus, $\Delta H$ MUST be highly NEGATIVE (exothermic) to overpower it and make $\Delta G$ negative.

**6.S15 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Henry: $P = K_H \chi_{solute}$. Raoult: $P_A = P_A^\circ \chi_A$. They have identical mathematical forms.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q6.M1 🟢**
Which of the following gases will have the lowest value of Henry's law constant ($K_H$) in water at $298\text{ K}$?
(A) $He$
(B) $N_2$
(C) $O_2$
(D) $CO_2$

**Q6.M2 🟡 (The "Slope Reversal" Trap)**
For a given gas in a liquid, the plot of partial pressure of the gas ($P$) versus the mole fraction of the GAS ($\chi_{gas}$) gives a straight line. What is the y-intercept of this line?
(A) $K_H$
(B) $-K_H$
(C) Zero
(D) $P^\circ$

**Q6.M3 🔴**
The Henry's law constant for dissolution of $CH_4$ in benzene at $298\text{ K}$ is $4.27 \times 10^5\text{ mmHg}$. The solubility of $CH_4$ in benzene at $298\text{ K}$ under $760\text{ mmHg}$ is:
(A) $1.78 \times 10^{-3}$
(B) $1.78 \times 10^{-5}$
(C) $5.6 \times 10^2$
(D) $4.27 \times 10^5$

**Q6.M4 🟡**
If the solubility of a gas is $0.05\text{ mol/L}$ at a pressure of $2\text{ atm}$, what will be its solubility at $6\text{ atm}$ at the same temperature?
(A) $0.05\text{ mol/L}$
(B) $0.15\text{ mol/L}$
(C) $0.30\text{ mol/L}$
(D) $0.016\text{ mol/L}$

**Q6.M5 🟡 (The "Temperature Paradox" Trap)**
You have a glass of cold water ($10^\circ\text{C}$) and a glass of warm water ($40^\circ\text{C}$). You dissolve $O_2$ gas in both until saturation at $1\text{ atm}$ pressure. Which glass contains a greater mole fraction of $O_2$, and in which glass is the $K_H$ of $O_2$ higher?
(A) Greater $\chi_{O_2}$ in cold; Higher $K_H$ in warm
(B) Greater $\chi_{O_2}$ in warm; Higher $K_H$ in cold
(C) Greater $\chi_{O_2}$ in cold; Higher $K_H$ in cold
(D) Greater $\chi_{O_2}$ in warm; Higher $K_H$ in warm

**Q6.M6 🔴**
$K_H$ for $Ar_{(g)}$, $CO_{2(g)}$, $HCHO_{(g)}$, and $CH_{4(g)}$ are $40.39$, $1.67$, $1.83 \times 10^{-5}$, and $0.413$, respectively. Arrange these gases in the order of their increasing solubility.
(A) $HCHO < CH_4 < CO_2 < Ar$
(B) $HCHO < CO_2 < CH_4 < Ar$
(C) $Ar < CO_2 < CH_4 < HCHO$
(D) $Ar < CH_4 < CO_2 < HCHO$

**Q6.M7 🟡**
According to Henry's law, a graph of the mass of a gas dissolved per unit volume of solvent ($m$) versus the pressure of the gas ($P$) is a straight line passing through the origin. The slope of this line is related to:
(A) The boiling point of the solvent
(B) The volume of the container
(C) The specific Henry's law constant for the mass-pressure relationship
(D) Universal gas constant $R$

**Q6.M8 🟢**
The dissolution of a solid in a liquid is an endothermic process. According to Le Chatelier's principle, its solubility should:
(A) Increase with an increase in pressure
(B) Decrease with an increase in temperature
(C) Increase with an increase in temperature
(D) Be independent of temperature

**Q6.M9 🔴 (The "Unit Mismatch" Trap)**
Henry's law constant for $O_2$ in water is $4.6 \times 10^4\text{ bar}$. What is the mole fraction of $O_2$ dissolved in water if the partial pressure of $O_2$ is $0.2\text{ atm}$? ($1\text{ atm} = 1.013\text{ bar}$).
(A) $4.34 \times 10^{-6}$
(B) $4.40 \times 10^{-6}$
(C) $2.3 \times 10^5$
(D) $0.2 \times 10^{-4}$

**Q6.M10 🟡**
Which condition is NOT required for Henry's Law to be strictly valid?
(A) The pressure should not be too high.
(B) The temperature should not be too low.
(C) The gas should not undergo chemical reaction with the solvent.
(D) The gas must be highly soluble in the solvent.

**Q6.M11 🔴**
A mixture of two gases $X$ and $Y$ exerts a total pressure of $10\text{ atm}$ over a solvent. The mole fraction of $X$ in the gas phase is $0.6$. If the $K_H$ values for $X$ and $Y$ are $2 \times 10^4\text{ atm}$ and $1 \times 10^4\text{ atm}$ respectively, what is the ratio of mole fractions of $X$ and $Y$ dissolved in the liquid? ($\chi_{X(liquid)} : \chi_{Y(liquid)}$)
(A) $3:4$
(B) $3:2$
(C) $4:3$
(D) $1:1$

**Q6.M12 🟡**
At a given temperature, oxygen gas is bubbled through water. The concentration of dissolved oxygen is found to be $0.04\text{ g/L}$ at a pressure of $1\text{ atm}$. If the pressure is increased to $2.5\text{ atm}$, what will be the concentration of dissolved oxygen?
(A) $0.04\text{ g/L}$
(B) $0.016\text{ g/L}$
(C) $0.10\text{ g/L}$
(D) $0.25\text{ g/L}$

**Q6.M13 🟢**
The "bends" experienced by deep-sea divers is primarily due to:
(A) High solubility of $O_2$ at high pressure
(B) Low solubility of $N_2$ at high pressure
(C) Sudden decrease in the solubility of $N_2$ in blood upon rapid ascent
(D) Chemical reaction of He with blood cells

**Q6.M14 🔴 (The "Reverse Formula" Trap)**
An experiment shows that $0.1\text{ moles}$ of a gas dissolves in $9.9\text{ moles}$ of water at $2\text{ atm}$. If Henry's law is written as $\chi_{gas} = K' \times P$, what is the value of $K'$?
(A) $20\text{ atm}^{-1}$
(B) $0.005\text{ atm}^{-1}$
(C) $200\text{ atm}$
(D) $0.01\text{ atm}^{-1}$

**Q6.M15 🟡**
If a gas undergoes dissociation (e.g., $HCl \rightarrow H^+ + Cl^-$) when dissolved in water, Henry's Law:
(A) Applies perfectly to the total dissolved concentration
(B) Fails because the gas chemically changes state in the solvent
(C) Applies only at extremely high pressures
(D) Applies only at extremely high temperatures

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q6.M1 → Answer: (D)**
- $K_H$ is inversely proportional to solubility.
- $CO_2$ is polar/reactive with water, making it the most soluble among the choices.
- Most soluble = lowest $K_H$.

**Q6.M2 → Answer: (C)**
- Equation: $P_{gas} = K_H \times \chi_{gas}$.
- This is in the form $y = mx + c$.
- Slope $m = K_H$. Y-intercept $c = 0$.
- Trap: (B) applies to the plot against $\chi_{solvent}$.

**Q6.M3 → Answer: (A)**
- $\chi = \frac{P}{K_H} = \frac{760}{4.27 \times 10^5}$.
- $760 / 427000 = 1.779 \times 10^{-3} \approx 1.78 \times 10^{-3}$.

**Q6.M4 → Answer: (B)**
- Solubility $\propto$ Pressure.
- $S_1 / P_1 = S_2 / P_2 \rightarrow 0.05 / 2 = S_2 / 6$.
- $S_2 = 0.05 \times 3 = 0.15\text{ mol/L}$.

**Q6.M5 → Answer: (A)**
- Cold water: Lower temperature means lower $K_H$, which means HIGHER solubility ($\chi_{O_2}$).
- Warm water: Higher temperature means HIGHER $K_H$, which means LOWER solubility.

**Q6.M6 → Answer: (C)**
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

**Q6.M7 → Answer: (C)**
- Henry's law can also be written in terms of mass: $m = K_H' \times P$. The slope is the modified Henry's constant for those specific units.

**Q6.M8 → Answer: (C)**
- Endothermic process ($\Delta H > 0$): By Le Chatelier's Principle, increasing temperature adds heat, shifting the equilibrium forward to dissolve more solid.

**Q6.M9 → Answer: (B)**
- Convert Pressure to bar to match $K_H$: $P = 0.2\text{ atm} \times 1.013\text{ bar/atm} = 0.2026\text{ bar}$.
- $\chi = \frac{P}{K_H} = \frac{0.2026}{4.6 \times 10^4} = 0.0440 \times 10^{-4} = 4.40 \times 10^{-6}$.
- Trap: (A) Using $0.2$ directly without unit conversion gives $4.34 \times 10^{-6}$.

**Q6.M10 → Answer: (D)**
- Henry's law is actually an IDEAL gas law equivalent for solutions. It works best for gases that are slightly or moderately soluble. If a gas is highly soluble, it often means it's reacting with the solvent (like $NH_3$ in water), causing massive deviations from the simple linear Henry's Law. So, requiring it to be "highly soluble" is false.
- Conditions for validity: Low pressure, high temperature, no association/dissociation.

**Q6.M11 → Answer: (A)**
- Partial pressure of $X$ in gas: $P_X = 0.6 \times 10\text{ atm} = 6\text{ atm}$.
- Partial pressure of $Y$ in gas: $P_Y = 0.4 \times 10\text{ atm} = 4\text{ atm}$.
- In liquid: $\chi_X = \frac{P_X}{K_{H,X}} = \frac{6}{2 \times 10^4} = 3 \times 10^{-4}$.
- In liquid: $\chi_Y = \frac{P_Y}{K_{H,Y}} = \frac{4}{1 \times 10^4} = 4 \times 10^{-4}$.
- Ratio $\chi_X : \chi_Y = 3 : 4$.

**Q6.M12 → Answer: (C)**
- $S \propto P$.
- $S_2 = S_1 \times (P_2 / P_1) = 0.04 \times (2.5 / 1.0) = 0.10\text{ g/L}$.

**Q6.M13 → Answer: (C)**
- At high pressure underwater, $N_2$ dissolves in blood. Upon rapid ascent, pressure drops, solubility plummets, and $N_2$ bubbles out into the veins.

**Q6.M14 → Answer: (B)**
- The question uses the reverse format: $\chi = K' \times P$. Here $K' = 1/K_H$.
- Mole fraction of gas $\chi_{gas} = \frac{0.1}{0.1 + 9.9} = \frac{0.1}{10.0} = 0.01$.
- $\chi = K' \times P \rightarrow 0.01 = K' \times 2 \rightarrow K' = 0.005\text{ atm}^{-1}$.
- Trap: Using the standard $P = K_H \chi \rightarrow 2 = K_H \times 0.01 \rightarrow K_H = 200$.

**Q6.M15 → Answer: (B)**
- Henry's Law applies to the undissociated molecular species in equilibrium with the gas. If the gas dissociates or associates, the simple linear relationship $P \propto$ total dissolved concentration fails. It only applies strictly if there is no chemical interaction/change.
</details>

---

*Next: [Chapter 7 — Vapour Pressure & Raoult's Law →](./07_vapour_pressure_and_raoults_law.md)*
