# Chapter 7: Vapour Pressure & Raoult's Law
## Part IV — Vapour Pressure

---

## 🎯 Stage 1: The Core Idea

### What is Vapour Pressure?

Seal a liquid in a container. Some molecules have enough energy to escape the liquid surface and become vapour. Eventually, the rate of evaporation equals the rate of condensation — **equilibrium**. The pressure of this vapour at equilibrium is the **vapour pressure**.

Key facts:
- VP is temperature-dependent (higher T → higher VP)
- VP is independent of container size or liquid amount
- VP depends on intermolecular forces (stronger forces → lower VP)

**Intermolecular force strength:** Ionic > H-bond > Dipole-Dipole > van der Waals
→ Water (H-bonds) has lower VP than chloroform (dipole-dipole) at same T.

### Raoult's Law — For Volatile Solute (Liquid-Liquid Mixtures)

When two volatile liquids A and B mix, both contribute to total vapour pressure:

```
P_A = P°_A × χ_A
P_B = P°_B × χ_B
P_total = P_A + P_B = P°_A χ_A + P°_B χ_B
```

### Raoult's Law — For Non-Volatile Solute

When a non-volatile solute is added to a solvent, only the solvent evaporates:

```
P_solution = P°_solvent × χ_solvent

Since χ_solvent < 1:  P_solution < P°_solvent
```

This is the basis of **Relative Lowering of Vapour Pressure (RLVP)** — a colligative property.

### Composition of Vapour Phase

The vapour above a liquid-liquid mixture is richer in the more volatile component:

```
Y_A = P_A/P_total = (P°_A × χ_A) / P_total

Y_A/Y_B = (P°_A × χ_A) / (P°_B × χ_B)
```

---

## 🔬 Stage 2: The Formula Lab

### Complete Formula Set

**Vapour Pressure:**
```
P°_liquid: vapour pressure of pure liquid at temperature T

Clausius-Clapeyron:
log(VP_T2 / VP_T1) = (ΔH_vap / 2.303R) × (1/T1 − 1/T2)
```

**Raoult's Law (Volatile Solute — Two Liquid Components A and B):**
```
P_A = P°_A × χ_A (liquid phase)
P_B = P°_B × χ_B (liquid phase)
P_T = P°_A χ_A + P°_B χ_B = P°_B + χ_A(P°_A − P°_B)

Vapour phase composition:
Y_A = P_A/P_T = (P°_A χ_A) / P_T
Y_B = P_B/P_T = (P°_B χ_B) / P_T
```

**Raoult's Law (Non-Volatile Solute):**
```
P_s = P° × χ_solvent = P°(1 − χ_solute)

RLVP = (P° − P_s)/P° = χ_solute = n_solute/(n_solute + n_solvent)

Modified: (P° − P_s)/P_s = n_solute/n_solvent = (W_solute × M_solvent)/(MM_solute × W_solvent)
```

> **⚠️ Critical Distinction:** The standard RLVP formula has P° in the denominator. The modified form has P_s in the denominator. These give different numerical values — use the correct one!

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Pure Liquid VP — Temperature & Intermolecular Forces

#### Solved Example 7.1
**Q:** At 350 K, VP of a pure liquid = 1.5 atm. At 500 K, will VP be greater or less? 🟢

```
Vaporization is endothermic. Higher T → more energy → more evaporation.
VP increases exponentially with T.

Answer: VP > 1.5 atm at 500 K.
```

#### Solved Example 7.2
**Q:** Compare VP of CHCl₃ and H₂O at same temperature. 🟡

```
H₂O: hydrogen bonding (strong IMF) → low VP
CHCl₃: dipole-dipole only (weaker IMF) → higher VP

Answer: VP(H₂O) < VP(CHCl₃)
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 7.1a | If same liquid is placed in flasks of different shapes and sizes at same T, compare their VPs. | 🟢 |
| 7.1b | Arrange in increasing VP: diethyl ether, ethanol, water at 25°C. | 🟡 |
| 7.1c | VP of liquid A = 200 torr at 300 K. Liquid B has stronger IMF. Compare VP of B at 300 K. | 🟢 |
| 7.1d | Explain why VP increases exponentially (not linearly) with temperature. | 🟡 |

<details>
<summary>💡 Solutions for Type 1</summary>

**7.1a:** VP is the same in all flasks at the same temperature. VP is independent of container shape and liquid amount.

**7.1b:** Water has hydrogen bonding (strongest); ethanol has hydrogen bonding (weaker than water due to larger nonpolar part); diethyl ether has dipole-dipole only.
**Increasing VP: water < ethanol < diethyl ether**

**7.1c:** Stronger IMF → molecules harder to escape → **VP(B) < 200 torr**

**7.1d:** VP is related to equilibrium constant K_p for vaporization. K_p = e^(−ΔH/RT). Since ΔH_vap > 0, as T increases, K_p increases exponentially (Arrhenius-type). Hence VP is exponential, not linear.
</details>

---

### Type 2: Raoult's Law — Total Vapour Pressure of Volatile Mixture

**Pattern:** Two liquids A and B, given χ_A, χ_B, P°_A, P°_B → find P_total.

#### Solved Example 7.3
**Q:** P°_A = 400 mm Hg, P°_B = 600 mm Hg. χ_B = 0.5. Find P_total. 🟢

```
χ_A = 1 − 0.5 = 0.5
P_total = P°_A χ_A + P°_B χ_B = 400×0.5 + 600×0.5 = 200 + 300 = 500 mm Hg
```

#### Solved Example 7.4
**Q:** P_total = 180X_A + 90. Find P°_A and P°_B. 🟡

```
Compare with P_T = P°_B + χ_A(P°_A − P°_B):
    P°_B = 90 mm Hg
    P°_A − P°_B = 180 → P°_A = 270 mm Hg
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 7.2a | P°_A = 300 torr, P°_B = 800 torr, χ_A = 0.6. Find P_total. ⭐ | 🟢 |
| 7.2b | Equal moles of A (P° = 200) and B (P° = 500). Find P_total. | 🟢 |
| 7.2c | At 300 K, 1 mol hexane + 3 mol heptane → P_T = 550 mm. Adding 1 more mol heptane → P_T = 560 mm. Find P°_heptane. ⭐ | 🔴 |
| 7.2d | If P_T = 250X_B + 150, find P°_A and P°_B. | 🟡 |
| DPP 6.7 | The vapour pressure of pure CHCl₃ and CH₂Cl₂ are 200 and 41.5 atm respectively. The weight of CHCl₃ and CH₂Cl₂ are 11.9 g and 17 g respectively in a solution. The vapour pressure of solution (in atm) will be: (A) 80.5 (B) 79.5 (C) 94.3 (D) 105.5 | 🟡 |
| DPP 8.8 | Two liquids A and B form ideal solutions. At 300 K, the vapour pressure of a solution containing 1 mole of A and 3 moles of B is 550 mmHg. At the same temperature, if one more mole of B is added to this solution, the vapour pressure of the solution increases by 10 mmHg. The vapour pressure of A and B in their pure states (in mmHg) are respectively: (A) 400, 600 (B) 500, 500 (C) 600, 400 (D) None of these | 🔴 |

<details>
<summary>💡 Solutions for Type 2</summary>

**7.2a:** P_T = 300×0.6 + 800×0.4 = 180 + 320 = **500 torr**

**7.2b:** χ_A = χ_B = 0.5; P_T = 200×0.5 + 500×0.5 = **350 mm Hg**

**7.2c:**
- Case 1: 1 hex + 3 hep → χ_hex = 0.25; P = 0.25P°_hex + 0.75P°_hep = 550
- Case 2: 1 hex + 4 hep → χ_hex = 0.2; P = 0.2P°_hex + 0.8P°_hep = 560
- Subtract: 0.05P°_hex − 0.05P°_hep = −10 → P°_hex − P°_hep = −200
- From eq 1: 0.25P°_hex + 0.75P°_hep = 550
- Let P°_hex = P°_hep − 200; → 0.25(P°_hep−200) + 0.75P°_hep = 550 → P°_hep − 50 = 550 → **P°_heptane = 600 mm Hg** (P°_hexane = 400 mm Hg)

**7.2d:** Compare with P_T = P°_A + χ_B(P°_B − P°_A) = 150 + 250χ_B
**P°_A = 150 mm Hg; P°_B = 400 mm Hg**

**DPP 6.7:** Molar mass of CHCl₃ = 12 + 1 + 3×35.5 = 119. Molar mass of CH₂Cl₂ = 12 + 2 + 2×35.5 = 85.
n_CHCl₃ = 11.9 / 119 = 0.1 mol; n_CH₂Cl₂ = 17 / 85 = 0.2 mol. Total moles = 0.3 mol.
χ_CHCl₃ = 0.1/0.3 = 1/3; χ_CH₂Cl₂ = 0.2/0.3 = 2/3.
P_total = P°_CHCl₃ × χ_CHCl₃ + P°_CH₂Cl₂ × χ_CH₂Cl₂ = 200 × (1/3) + 41.5 × (2/3) = 66.67 + 27.67 = **94.34 atm ≈ 94.3 atm → Answer: (C)**

**DPP 8.8:** Let pure state VP be P°_A and P°_B.
Case 1: n_A = 1, n_B = 3 → χ_A = 0.25, χ_B = 0.75. P_T = 0.25P°_A + 0.75P°_B = 550.
Case 2: n_A = 1, n_B = 4 → χ_A = 0.20, χ_B = 0.80. P_T = 0.20P°_A + 0.80P°_B = 560.
Solving simultaneously yields P°_A = **400 mmHg** and P°_B = **600 mmHg → Answer: (A)**
</details>

---

### Type 3: Vapour Phase Composition

**Pattern:** Given liquid composition → find Y_A and Y_B in vapour phase.

#### Solved Example 7.5
**Q:** P°_A = 50 torr, P°_B = 100 torr, χ_A = 0.3. Find Y_B in vapour. 🟡 ⭐

```
P_A = 50 × 0.3 = 15 torr
P_B = 100 × 0.7 = 70 torr
P_total = 85 torr

Y_A = 15/85 = 0.176
Y_B = 70/85 = 0.824

Check: 0.176 + 0.824 = 1 ✓

Vapour is richer in B (more volatile: P°_B > P°_A).
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 7.3a | P°_benzene = 80 torr, P°_toluene = 24 torr, equimolar mixture. Find Y_benzene. | 🟡 |
| 7.3b | P°_A = 300 torr, P°_B = 800 torr, χ_A = 0.6. Find Y_A, Y_B. ⭐ | 🟡 |
| 7.3c | P°_A > P°_B. If X_A = Y_A, what can you conclude? | 🔴 |
| 7.3d | A liquid mixture has P°_A = 350, P°_B = 750 mm Hg. Find X_A if Y_A = Y_B. | 🔴 |
| DPP 6.3 | The vapour pressure of pure benzene and toluene are 160 and 60 torr respectively. The mole fraction of toluene in vapour phase in contact with equimolar solution of benzene and toluene is: (A) 0.50 (B) 0.6 (C) 0.27 (D) 0.73 | 🟡 |

<details>
<summary>💡 Solutions for Type 3</summary>

**7.3a:** P_benzene = 80×0.5 = 40; P_toluene = 24×0.5 = 12; P_T = 52
**Y_benzene = 40/52 = 0.769**

**7.3b:** P_A = 300×0.6 = 180; P_B = 800×0.4 = 320; P_T = 500
**Y_A = 180/500 = 0.36; Y_B = 320/500 = 0.64**

**7.3c:** If X_A = Y_A, then P_A/P_T = χ_A → P°_A×χ_A/(P°_A×χ_A + P°_B×χ_B) = χ_A → P°_A = P_T. This only happens at the **azeotropic point** (if it's an ideal mixture, it would mean P°_A = P°_B, i.e., both components have the same VP).

**7.3d:** Y_A = Y_B = 0.5 → P_A = P_B → P°_A×χ_A = P°_B×χ_B → 350χ_A = 750(1−χ_A)
350χ_A = 750 − 750χ_A → 1100χ_A = 750 → **χ_A = 750/1100 = 0.682**

**DPP 6.3:** Equimolar solution means χ_benz = 0.5, χ_tol = 0.5.
P_benz = 160 × 0.5 = 80 torr; P_tol = 60 × 0.5 = 30 torr. Total pressure = 80 + 30 = 110 torr.
Y_tol = P_tol / P_total = 30 / 110 = **0.2727 ≈ 0.27 → Answer: (C)**
</details>

---

### Type 4: RLVP — Non-Volatile Solute

**Pattern:** Find RLVP, P_solution, or molar mass of unknown solute.

#### Solved Example 7.6
**Q:** 0.60 g urea (MM = 60) in 360 g water. P° = 35 mm Hg. Find lowering of VP. 🟢 ⭐

```
n_urea = 0.60/60 = 0.01 mol
n_water = 360/18 = 20 mol

χ_urea = 0.01/(0.01+20) = 0.01/20.01 ≈ 0.0005

ΔP = P° × χ_urea = 35 × 0.0005 = 0.0175 mm Hg ≈ 0.017 mm Hg
```

#### Solved Example 7.7
**Q:** Pure benzene VP = 640 mm. 2.175 g of non-volatile solid in 39 g benzene → VP = 600 mm. Find MM of solid. 🟡 ⭐

```
Using modified formula: (P° − P_s)/P_s = n_solute/n_solvent

(640 − 600)/600 = (2.175/MM)/(39/78)

40/600 = (2.175/MM)/0.5

0.0667 = 2 × 2.175/MM

MM = 4.35/0.0667 = 65.25 g/mol
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 7.4a | RLVP of a dilute solution = 0.2. Find χ_solute. | 🟢 |
| 7.4b | VP of solvent = 20 torr. Solution VP = 17 torr. Find χ_solute. | 🟢 |
| 7.4c | 20 g non-ionic solute in 100 g water. VP drops from 17.54 to 17.24 mm. Find MM. | 🟡 |
| 7.4d | Benzene VP = 750 mm at 80°C. Adding 2 g non-volatile substance to 78 g benzene drops VP by 10 mm. Find MM. ⭐ | 🟡 |
| 7.4e | Mass of urea needed to reduce VP of water by 25% at some temperature. | 🔴 |
| DPP 6.1 | Which of the following is the expression of Raoult's law? (p = vapour pressure of pure solvent, ps = vapour pressure of the solution, n = moles of solute, N = moles of solvent) (A) (p − ps)/ps = n/N (B) (p − ps)/p = N/(N+n) (C) (p − ps)/ps = N/n (D) (ps − p)/p = (N − n)/N | 🟢 |
| DPP 6.2 | The vapour pressure of water at room temperature is lowered by 5% by dissolving a solute in it, then the approximately molality of solution is: (A) 2 (B) 1 (C) 4 (D) 3 | 🟡 |
| DPP 6.4 | Relative lowering of vapour pressure of a dilute solution is 0.2. What is the mole fraction of the non-volatile solute? (A) 0.8 (B) 0.5 (C) 0.3 (D) 0.2 | 🟢 |
| DPP 6.5 | The statement "the relative lowering of the vapour pressure is equal to the ratio of moles of the solute to the total number of the moles in the solution" refers to: (A) Hess's law (B) Dalton's law (C) Raoult's law (D) Charles' law | 🟢 |
| DPP 6.6 | The vapour pressure of water at 20°C is 17.54 mm. When 20 g of non-ionic substance is dissolved in 100 g of water, the vapour pressure is lowered by 0.30 mm. What is the molecular weight of the substance? (A) 210.48 (B) 206.88 (C) 215.2 (D) 200.8 | 🟡 |
| DPP 6.8 | The vapour pressure lowering caused by the addition of 100 g of sucrose (molecular mass = 342) to 1000 g of water if the vapour pressure of pure water at 25ºC is 23.8 mm Hg, is: (A) 1.25 mm Hg (B) 0.125 mm Hg (C) 1.15 mm Hg (D) 0.012 mm Hg | 🟢 |
| DPP 7.2 | For a dilute solution, Raoult's law states that: (A) The lowering of vapour pressure is equal to mole fraction of solute (B) The relative lowering of vapour pressure is equal to mole fraction of solute (C) The relative lowering of vapour pressure is proportional to the amount of solute in solution (D) The vapour pressure of the solution is equal to the mole fraction of solvent | 🟢 |
| DPP 7.6 | The relative lowering of vapour pressure of a dilute aqueous solution containing non-volatile solute is 0.0125. The molality of the solution is about: (A) 0.70 (B) 0.50 (C) 0.90 (D) 0.80 | 🟡 |
| DPP 7.8 | Which of the following is incorrect? (A) Relative lowering of vapour pressure is independent of the nature of the solute and the solvent. (B) The relative lowering of vapour pressure is a colligative property. (C) Vapour pressure of a solution is lower than the vapour pressure of the solvent. (D) The relative lowering of vapour pressure is directly proportional to the original pressure. | 🟢 |
| DPP 7.9 | The mass of a non-volatile solute of molar mass 40 g mol⁻¹ that should be dissolved in 114 g of Octane to lower its vapour pressure by 20% is: (A) 10 g (B) 11.4 g (C) 9.8 g (D) 12.8 g | 🔴 |

<details>
<summary>💡 Solutions for Type 4</summary>

**7.4a:** RLVP = χ_solute → **χ_solute = 0.2**

**7.4b:** RLVP = (20−17)/20 = 3/20 = **0.15 = χ_solute**

**7.4c:** RLVP = 0.30/17.54 = 0.01710
χ_solute = n/(n + n_H₂O): n_H₂O = 100/18 = 5.556
0.01710 = n/(n+5.556) → n(1−0.01710) = 0.01710×5.556 → n = 0.09503/0.9829 = 0.09669 mol
**MM = 20/0.09669 = 206.8 g/mol**

**7.4d:** (P°−P_s)/P_s = n_solute/n_solvent
10/740 = (2/MM)/(78/78) = 2/MM → **MM = 2×740/10 = 148 g/mol**

**7.4e:** Reduction of 25% → P_s = 0.75P°
RLVP = 0.25 = n_urea/(n_urea + n_H₂O)
0.25(n_urea + 55.56) = n_urea → 0.75n_urea = 13.89 → n_urea = 18.52 mol
**W_urea = 18.52 × 60 = 1111 g per 1000g water**

**DPP 6.1:** Modified form of Raoult's law states: (p − ps)/ps = n/N. This relates the lowering of vapour pressure directly to the moles of solute and solvent. → **Answer: (A)**

**DPP 6.2:** Lowered by 5% means RLVP = (p − ps)/p = 0.05 = χ_solute.
Formula: m = (χ_solute × 1000) / (χ_solvent × 18) = (0.05 × 1000) / (0.95 × 18) = 50 / 17.1 = **2.92 m ≈ 3 m → Answer: (D)**

**DPP 6.4:** RLVP directly equals the mole fraction of the non-volatile solute by Raoult's Law. Thus, χ_solute = **0.2 → Answer: (D)**

**DPP 6.5:** This is the exact textbook definition of Raoult's law for solutions containing non-volatile solutes. → **Answer: (C)**

**DPP 6.6:** Lowering ΔP = p − ps = 0.30 mm. p = 17.54 mm. Modified formula: (p − ps)/ps = n/N.
ps = 17.54 − 0.30 = 17.24 mm.
0.30 / 17.24 = (20/MM) / (100/18) = (20/MM) / 5.556 → MM = (20 × 17.24) / (0.30 × 5.556) = 344.8 / 1.6667 = **206.88 g/mol → Answer: (B)**

**DPP 6.8:** n_sucrose = 100 / 342 = 0.2924 mol; n_water = 1000 / 18 = 55.56 mol.
χ_sucrose = 0.2924 / (0.2924 + 55.56) = 0.2924 / 55.8524 = 0.005235.
ΔP = P° × χ_sucrose = 23.8 × 0.005235 = **0.1246 mm Hg ≈ 0.125 mm Hg → Answer: (B)**

**DPP 7.2:** For a dilute solution containing a non-volatile solute, Raoult's law states that the relative lowering of vapour pressure is equal to the mole fraction of the solute. → **Answer: (B)**

**DPP 7.6:** RLVP = χ_solute = 0.0125 → χ_water = 0.9875.
m = (0.0125 × 1000) / (0.9875 × 18) = 12.5 / 17.775 = **0.703 m ≈ 0.70 m → Answer: (A)**

**DPP 7.8:** RLVP is independent of the nature of the solute (colligative property). However, it depends on the solvent's properties in some formulations, but the statement (D) "directly proportional to the original pressure" is mathematically incorrect as RLVP is the *ratio* of lowering to the original pressure (ΔP/P°). → **Answer: (D)**

**DPP 7.9:** Octane (C₈H₁₈) MM = 8×12 + 18 = 114 g/mol. Mass of octane = 114 g → n_octane = 1 mol.
Lower VP by 20% means RLVP = 0.20 = n_solute / (n_solute + n_octane).
0.20(n_solute + 1) = n_solute → 0.20 = 0.80n_solute → n_solute = 0.25 mol.
Mass of solute = 0.25 mol × 40 g/mol = **10 g → Answer: (A)**
</details>

---

### Type 5: Successive Distillation

**Pattern:** Vapour from one step becomes liquid for next step.

#### Solved Example 7.8
**Q:** P°_A = 300 torr, P°_B = 100 torr, χ_A(1) = 0.6. Find Y_A after first distillation step. 🔴 ⭐

```
P_A = 300×0.6 = 180; P_B = 100×0.4 = 40; P_T = 220

Y_A(1) = 180/220 = 0.818

After condensation: χ_A(2) = Y_A(1) = 0.818 (vapour becomes liquid)
Second distillation:
P_A = 300×0.818 = 245.4; P_B = 100×0.182 = 18.2; P_T = 263.6
Y_A(2) = 245.4/263.6 = 0.931

Answer: Y_A after 1st step = 0.818
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 7.5a | P°_A = 300 torr, P°_B = 800 torr, χ_A = 0.6. At what pressure does the first bubble form? ⭐ | 🟡 |
| 7.5b | Using same data as 7.5a, what is the composition of the first bubble? | 🟡 |

<details>
<summary>💡 Solutions for Type 5</summary>

**7.5a:** First bubble = total VP at original liquid composition
P_T = 300×0.6 + 800×0.4 = 180+320 = **500 torr**

**7.5b:** Y_A = 180/500 = 0.36; **Y_B = 320/500 = 0.64**
(Vapour is richer in B — the more volatile component)
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 7.M1 | P°_A = 200, P°_B = 500 torr. 3 mol A + 2 mol B. Find: (a) P_total, (b) Y_A, (c) Y_B. ⭐ | T2+T3 | 🟡 |
| 7.M2 | A non-volatile solute reduces VP of water (P° = 32 mm) to 30.4 mm. Find χ_solute and molality if MM_solute = 60. | T4 | 🟡 |
| 7.M3 | 80 g benzene (MM=78) + 100 g toluene (MM=92). P°_B = 50.71 mm, P°_T = 32.06 mm. Find P_total and Y_benzene. | T2+T3 | 🔴 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**7.M1:**
- χ_A = 3/5 = 0.6; χ_B = 2/5 = 0.4
- **(a) P_T = 200×0.6 + 500×0.4 = 120+200 = 320 torr**
- P_A = 120, P_B = 200
- **(b) Y_A = 120/320 = 0.375**
- **(c) Y_B = 200/320 = 0.625**

**7.M2:**
- RLVP = (32−30.4)/32 = 1.6/32 = 0.05 = χ_solute
- χ_solute = n_solute/(n_solute + n_H₂O)
- n_H₂O = 1000/18 = 55.56 mol (per 1 kg)
- n_s/(n_s+55.56) = 0.05 → n_s = 0.05×55.56/0.95 = 2.924 mol
- **Molality = 2.924 m**

**7.M3:**
- n_benz = 80/78 = 1.026 mol; n_tol = 100/92 = 1.087 mol; Total = 2.113
- χ_benz = 1.026/2.113 = 0.4856; χ_tol = 0.5144
- P_benz = 50.71×0.4856 = 24.62 mm; P_tol = 32.06×0.5144 = 16.49 mm
- **P_total = 41.11 mm**
- **Y_benzene = 24.62/41.11 = 0.599**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 7.B1 | State Raoult's Law for a solution containing a non-volatile solute. *(NCERT)* | 🟢 |
| 7.B2 | Vapour pressure of water at 20°C = 17.54 mm. Calculate VP of solution with 20 g non-volatile solute (MM = 60) in 180 g water. | 🟡 |
| 7.B3 | What are ideal solutions? Give two examples. | 🟢 |
| 7.B4 | The vapour pressure of pure liquids A and B are 450 and 700 mm Hg. Calculate the vapour pressure of the mixture containing equal masses (90 g each) of A (MM=90) and B (MM=180). ⭐ | 🟡 |
| 7.B5 | Why is the vapour above a liquid-liquid mixture always richer in the more volatile component? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**7.B1:** The vapour pressure of a solution containing a non-volatile solute is directly proportional to the mole fraction of the solvent: P_s = P° × χ_solvent

**7.B2:** n_solute = 20/60 = 0.333 mol; n_water = 180/18 = 10 mol
χ_solvent = 10/10.333 = 0.9677
P_s = 17.54 × 0.9677 = **16.97 mm Hg**

**7.B3:** Ideal solutions obey Raoult's Law over entire composition range. ΔH_mix = 0, ΔV_mix = 0.
Examples: Benzene-toluene, hexane-heptane, ethyl bromide-ethyl iodide.

**7.B4:** n_A = 90/90 = 1 mol; n_B = 90/180 = 0.5 mol; Total = 1.5
χ_A = 1/1.5 = 0.667; χ_B = 0.5/1.5 = 0.333
P_T = 450×0.667 + 700×0.333 = 300 + 233.3 = **533.3 mm Hg**

**7.B5:** By Dalton's Law, Y_A = P_A/P_T = P°_A χ_A / P_T. Since the more volatile component has higher P°, its partial pressure contribution is larger relative to its liquid mole fraction — so Y_A > χ_A for the more volatile component. The vapour is enriched in the more volatile species.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q7.J1 🟡 ⭐**
Vapour pressure of pure A = 400 mm, pure B = 600 mm. Mole fraction of B in solution = 0.5. Mole fraction of B in vapour is:
(A) 0.5  (B) 0.6  (C) 0.55  (D) 0.45

**Q7.J2 🟡 ⭐**
RLVP of a solution = 0.0125. Molality of the solution (in water) is approximately:
(A) 0.70 m  (B) 0.35 m  (C) 1.0 m  (D) 0.125 m

**Q7.J3 🔴**
80 g benzene (MM=78) dissolved in 100 g toluene (MM=92). P°_benzene = 160 torr, P°_toluene = 60 torr. Y_benzene in vapour is:
(A) 0.72  (B) 0.65  (C) 0.80  (D) 0.55

**Q7.J4 🔴 ⭐**
The vapour pressure of benzene at 80°C is 750 mm. When 2 g of non-volatile substance is dissolved in 78 g benzene, VP drops to 740 mm. The molar mass of the solute is:
(A) 148 g/mol  (B) 74 g/mol  (C) 65 g/mol  (D) 156 g/mol

**Q7.J5 🔴**
When a non-volatile solute is dissolved in water, VP decreases by 10 mm and χ_solute = 0.2. If VP decreases by 20 mm, the mole fraction of solvent is:
(A) 0.4  (B) 0.6  (C) 0.8  (D) 0.2

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**7.J1 → Answer: (B)**
- χ_B = 0.5, χ_A = 0.5; P_A = 400×0.5=200; P_B = 600×0.5=300; P_T = 500
- **Y_B = 300/500 = 0.6 ✓**

**7.J2 → Answer: (A)**
- χ_solute = RLVP = 0.0125 → χ_water = 0.9875
- m = (0.0125×1000)/(0.9875×18) = 12.5/17.775 = **0.703 m ≈ 0.70 m ✓**

**7.J3 → Answer: (A)**
- n_benz = 80/78 = 1.026; n_tol = 100/92 = 1.087; Total = 2.113
- χ_benz = 0.4857; χ_tol = 0.5143
- P_benz = 160×0.4857 = 77.7; P_tol = 60×0.5143 = 30.86; P_T = 108.56
- **Y_benz = 77.7/108.56 = 0.716 ≈ 0.72 ✓**

**7.J4 → Answer: (A)**
- n_benz = 78/78 = 1 mol
- (P°−P_s)/P_s = n_solute/n_solvent → (750−740)/740 = (2/MM)/1
- 10/740 = 2/MM → **MM = 2×740/10 = 148 g/mol ✓**

**7.J5 → Answer: (B)**
- From case 1: ΔP_1 = P° × χ_solute_1 = 10; χ_solute_1 = 0.2 → P° = 10/0.2 = 50 mm
- Case 2: ΔP_2 = 20 mm; χ_solute_2 = 20/50 = 0.4
- **χ_solvent = 1 − 0.4 = 0.6 ✓**
</details>

---

## Key Takeaways from Chapter 7

| Formula | Use |
|---------|-----|
| P_A = P°_A × χ_A | Volatile solute (liquid-liquid) |
| P_s = P° × χ_solvent | Non-volatile solute |
| RLVP = (P°−P_s)/P° = χ_solute | Key colligative property |
| Modified RLVP: (P°−P_s)/P_s = n_s/n_solv | Used to find molar mass |
| Y_A = P_A/P_T | Vapour phase composition |

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
| 7.S1 | **Assertion (A):** The vapour pressure of a liquid increases exponentially with an increase in temperature.<br>**Reason (R):** The Clausius-Clapeyron equation dictates that $\ln(P)$ is directly proportional to $T$. | 🟡 |
| 7.S2 | **Statement I:** If the volume of the container enclosing a liquid-vapour equilibrium is suddenly doubled at constant temperature, the vapour pressure will eventually halve.<br>**Statement II:** Vapour pressure is an intensive property and is independent of the volume of the container or the amount of liquid present. | 🟢 |
| 7.S3 | **Assertion (A):** For an ideal liquid mixture of A and B, if $P_A^\circ > P_B^\circ$, the mole fraction of A in the vapour phase ($Y_A$) is always strictly greater than its mole fraction in the liquid phase ($\chi_A$).<br>**Reason (R):** The vapour phase is always richer in the more volatile component compared to the liquid phase. | 🟡 |
| 7.S4 | **Statement I:** The formula $\frac{P^\circ - P_s}{P_s} = \frac{n_{solute}}{n_{solvent}}$ is an exact mathematical relationship derived from Raoult's Law.<br>**Statement II:** The formula $\frac{P^\circ - P_s}{P^\circ} = \frac{n_{solute}}{n_{solvent}}$ is an approximation that only holds for very dilute solutions. | 🟢 |
| 7.S5 | **Assertion (A):** Addition of a non-volatile solute to a volatile solvent increases the rate of evaporation of the solvent.<br>**Reason (R):** Solute molecules occupy surface area, increasing the internal energy of the solvent molecules. | 🟢 |
| 7.S6 | **Statement I:** If two volatile liquids A and B are mixed, and $P_A^\circ = 500\text{ torr}$ while $P_B^\circ = 200\text{ torr}$, the total vapour pressure of any mixture of A and B must lie strictly between $200\text{ torr}$ and $500\text{ torr}$.<br>**Statement II:** Total pressure $P_T = P_B^\circ + \chi_A(P_A^\circ - P_B^\circ)$, which is a linear interpolation between the pure vapour pressures. | 🟡 |
| 7.S7 | **Assertion (A):** In a closed vessel, the vapour pressure of water is $23.8\text{ torr}$ at $25^\circ\text{C}$. If salt is dissolved in the water, the vapour pressure remains $23.8\text{ torr}$.<br>**Reason (R):** Vapour pressure is a constant at a given temperature. | 🟢 |
| 7.S8 | **Statement I:** When plotting $P_{total}$ versus the mole fraction of component A ($\chi_A$) for an ideal binary solution, the graph is a straight line.<br>**Statement II:** When plotting $P_{total}$ versus the mole fraction of component A in the vapour phase ($Y_A$), the graph is also a straight line. | 🔴 |
| 7.S9 | **Assertion (A):** Relative lowering of vapour pressure is equal to the mole fraction of the solute.<br>**Reason (R):** This statement is true only for dilute solutions of non-volatile solutes. | 🟡 |
| 7.S10 | **Statement I:** For a solution containing a non-volatile solute, $P_s = P^\circ \cdot \chi_{solvent}$. This implies that the vapour pressure of the solution is directly proportional to the mole fraction of the solute.<br>**Statement II:** As the mole fraction of the solute increases, the vapour pressure of the solution decreases. | 🟢 |
| 7.S11 | **Assertion (A):** Fractional distillation can separate any ideal liquid mixture completely into its pure components.<br>**Reason (R):** In an ideal mixture, there is no azeotrope formation, so the successive boiling and condensation constantly enriches the vapour in the more volatile component until purity is reached. | 🟡 |
| 7.S12 | **Statement I:** The mass of a solute can be determined exactly using the formula $\frac{\Delta P}{P^\circ} = \frac{W_{solute} \times M_{solvent}}{MM_{solute} \times W_{solvent}}$ for all concentrations.<br>**Statement II:** This formula incorrectly assumes $n_{solute} + n_{solvent} \approx n_{solvent}$, which is only valid for highly dilute solutions. | 🟡 |
| 7.S13 | **Assertion (A):** At $100^\circ\text{C}$, the vapour pressure of pure water is exactly $1\text{ atm}$.<br>**Reason (R):** The normal boiling point of a liquid is defined as the temperature at which its vapour pressure equals $1\text{ atm}$. | 🟢 |
| 7.S14 | **Statement I:** If liquid A is more volatile than liquid B, then the intermolecular forces in liquid A are stronger than those in liquid B.<br>**Statement II:** Weaker intermolecular forces allow molecules to escape more easily into the vapour phase. | 🟢 |
| 7.S15 | **Assertion (A):** In an ideal solution of A and B, if $Y_A = Y_B = 0.5$, then the liquid must be equimolar ($\chi_A = \chi_B = 0.5$).<br>**Reason (R):** The composition of the vapour phase mirrors the composition of the liquid phase for ideal solutions. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**7.S1 → Answer: (C) A is true but R is false.**
- A is true: VP increases exponentially with T.
- R is false: The equation is $\ln(P) = -\frac{\Delta H_{vap}}{RT} + C$. So $\ln(P)$ is proportional to $1/T$, NOT to $T$.

**7.S2 → Statement I is False, Statement II is True.**
- Statement I is false: If volume is doubled, pressure initially drops, but liquid evaporates to restore the equilibrium VP. As long as some liquid remains, VP will return to its original value.
- Statement II is true: VP depends only on temperature and the nature of the liquid.

**7.S3 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Mathematically, if $P_A^\circ > P_B^\circ$, then $Y_A = \frac{P_A^\circ \chi_A}{P_A^\circ \chi_A + P_B^\circ \chi_B}$. Dividing numerator and denominator by $P_A^\circ \chi_A$, we see $Y_A > \chi_A$ because the denominator is less than $1 + (\text{something})$.

**7.S4 → Statement I is True, Statement II is True.**
- Statement I is true: $\frac{P^\circ - P_s}{P_s} = \frac{P^\circ - P^\circ \chi_1}{P^\circ \chi_1} = \frac{1-\chi_1}{\chi_1} = \frac{\chi_2}{\chi_1} = \frac{n_2}{n_1}$. This is EXACT.
- Statement II is true: $\frac{P^\circ - P_s}{P^\circ} = \chi_2 = \frac{n_2}{n_1 + n_2}$. The approximation $\approx \frac{n_2}{n_1}$ only works if $n_2$ is negligible.

**7.S5 → Answer: (D) A is false but R is false.**
- A is false: It DECREASES the rate of evaporation (lowers VP).
- R is false: Solute molecules occupy surface area, physically blocking solvent escape. It does not increase internal energy.

**7.S6 → Statement I is True, Statement II is True.**
- This is the fundamental premise of Raoult's Law for ideal solutions. The total pressure is a weighted average of the pure component pressures.

**7.S7 → Answer: (D) A is false but R is true.**
- A is false: Dissolving salt (non-volatile solute) LOWERS the vapour pressure. It will be less than $23.8\text{ torr}$.
- R is true: VP of a *pure* liquid is constant at a given temperature, but the assertion describes a solution. (Wait, R says "Vapour pressure is a constant at a given temperature". Technically, this refers to pure VP, but since A is false, D is the best fit).

**7.S8 → Statement I is True, Statement II is False.**
- Statement I is true: $P_T = P_B^\circ + \chi_A(P_A^\circ - P_B^\circ)$ is a linear equation $y = mx + c$.
- Statement II is false: $Y_A = \frac{P_A^\circ \chi_A}{P_T}$. When plotted against $Y_A$, the total pressure curve is NOT a straight line; it's a curve (hyperbola).

**7.S9 → Answer: (C) A is true but R is false.**
- A is true: $\frac{\Delta P}{P^\circ} = \chi_2$.
- R is false: This equation is EXACT for all concentrations of ideal solutions, not just dilute ones. The approximation comes in when relating mole fraction to mass ratios.

**7.S10 → Statement I is False, Statement II is True.**
- Statement I is false: VP is directly proportional to the mole fraction of the SOLVENT ($\chi_1$), not the solute ($\chi_2$).
- Statement II is true: $P_s = P^\circ(1 - \chi_{solute})$.

**7.S11 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This is the theoretical basis of fractional distillation for ideal liquid mixtures.

**7.S12 → Statement I is False, Statement II is True.**
- Statement I is false: This formula is an approximation.
- Statement II is true: The exact formula uses $\frac{\Delta P}{P_s} = \frac{n_2}{n_1}$.

**7.S13 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This is the definition of the normal boiling point.

**7.S14 → Statement I is False, Statement II is True.**
- Statement I is false: More volatile means it evaporates EASIER, which means WEAKER intermolecular forces.
- Statement II is true: Self-explanatory.

**7.S15 → Answer: (D) A is false but R is false.**
- A is false: If $Y_A = Y_B$, then $P_A^\circ \chi_A = P_B^\circ \chi_B$. Since $P_A^\circ \neq P_B^\circ$ generally, $\chi_A \neq \chi_B$.
- R is false: Vapour composition NEVER mirrors liquid composition in an ideal mixture unless $P_A^\circ = P_B^\circ$ (which means they are essentially the same liquid in terms of volatility).

</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q7.M1 🟢**
At a given temperature, the vapour pressure of a pure liquid A is $P^\circ$. If the container's volume is halved, the vapour pressure will:
(A) Double
(B) Halve
(C) Remain $P^\circ$
(D) Become $P^\circ / 4$

**Q7.M2 🟡 (The "Wrong Denominator" Trap)**
For a solution of a non-volatile solute in a solvent, the exact relationship for calculating molar mass from relative lowering of vapour pressure is:
(A) $\frac{P^\circ - P_s}{P^\circ} = \frac{n_{solute}}{n_{solvent}}$
(B) $\frac{P^\circ - P_s}{P_s} = \frac{n_{solute}}{n_{solvent}}$
(C) $\frac{P_s - P^\circ}{P^\circ} = \frac{n_{solute}}{n_{solvent}}$
(D) $\frac{P^\circ - P_s}{P_s} = \frac{n_{solvent}}{n_{solute}}$

**Q7.M3 🔴**
An ideal mixture of A and B has $P_A^\circ = 300\text{ torr}$ and $P_B^\circ = 600\text{ torr}$. If the total pressure of the mixture is $400\text{ torr}$, what is the mole fraction of A in the VAPOUR phase ($Y_A$)?
(A) $0.66$
(B) $0.33$
(C) $0.50$
(D) $0.75$

**Q7.M4 🟡**
To exactly halve the vapour pressure of a solvent (from $P^\circ$ to $0.5 P^\circ$) by adding a non-volatile solute, the ratio of moles of solute to moles of solvent ($n_{solute}/n_{solvent}$) must be:
(A) $0.5$
(B) $1.0$
(C) $2.0$
(D) $0.25$

**Q7.M5 🟡 (The "Non-Volatile Definition" Trap)**
A solution is prepared by mixing $10\text{ g}$ of glucose (non-volatile) and $10\text{ g}$ of urea (non-volatile) in $100\text{ g}$ of water. Which of the following is responsible for the vapour pressure of the solution?
(A) Only glucose
(B) Only urea
(C) Both glucose and urea
(D) Only water

**Q7.M6 🔴**
For an ideal solution of two volatile liquids A and B, a plot of $\frac{1}{P_{total}}$ versus $Y_A$ (mole fraction of A in vapour phase) yields a straight line. What is the slope of this line?
(A) $P_A^\circ - P_B^\circ$
(B) $\frac{1}{P_A^\circ} - \frac{1}{P_B^\circ}$
(C) $\frac{1}{P_B^\circ} - \frac{1}{P_A^\circ}$
(D) $P_B^\circ - P_A^\circ$

**Q7.M7 🟡**
Two liquids A and B form an ideal solution. If $P_A^\circ$ is twice $P_B^\circ$, and the mixture is prepared using equal MASSES of A and B (where $MM_A$ is half of $MM_B$), what is the mole fraction of A in the vapour phase ($Y_A$)?
(A) $0.80$
(B) $0.66$
(C) $0.50$
(D) $0.88$

**Q7.M8 🟢**
The vapour pressure of pure water at $20^\circ\text{C}$ is $17.5\text{ mm Hg}$. A solution containing $1\text{ mole}$ of a non-volatile solute in $4\text{ moles}$ of water will have a vapour pressure of:
(A) $3.5\text{ mm Hg}$
(B) $14.0\text{ mm Hg}$
(C) $17.5\text{ mm Hg}$
(D) $8.75\text{ mm Hg}$

**Q7.M9 🔴 (The "Tricky Vapour Composition" Trap)**
Liquid A ($P_A^\circ = 100\text{ mm}$) and Liquid B ($P_B^\circ = 300\text{ mm}$) form an ideal solution. The liquid mixture is boiled, and the very first bubble of vapour is collected and condensed into a new container. If the original liquid had $\chi_A = 0.5$, what is the mole fraction of A in this *new* condensed liquid?
(A) $0.50$
(B) $0.75$
(C) $0.25$
(D) $0.33$

**Q7.M10 🟡**
If $P_A^\circ = P_B^\circ$ for an ideal binary mixture, which of the following is ALWAYS true regardless of liquid composition?
(A) $P_{total} = 2 P_A^\circ$
(B) $Y_A = \chi_A$
(C) $Y_A = 0.5$
(D) The mixture forms an azeotrope

**Q7.M11 🔴**
An ideal solution contains equal moles of A, B, and C. Their pure vapour pressures are $100\text{ torr}$, $200\text{ torr}$, and $300\text{ torr}$ respectively. What is the mole fraction of B in the vapour phase?
(A) $0.33$
(B) $0.50$
(C) $0.16$
(D) $0.25$

**Q7.M12 🟡**
The vapour pressure of a dilute aqueous solution of glucose is $740\text{ mm Hg}$ at $100^\circ\text{C}$. What is the mole fraction of the SOLVENT?
(A) $740/760$
(B) $20/760$
(C) $20/740$
(D) $760/740$

**Q7.M13 🟢**
Which of the following does NOT affect the vapour pressure of a pure liquid?
(A) Temperature
(B) Intermolecular forces
(C) Surface area of the liquid
(D) Nature of the liquid

**Q7.M14 🔴 (The "Reverse Math" Trap)**
A mixture of volatile liquids A and B has a total vapour pressure of $600\text{ torr}$. The vapour phase contains $40\%\text{ A}$ by moles. If $P_A^\circ = 400\text{ torr}$, what is $P_B^\circ$?
(A) $800\text{ torr}$
(B) $900\text{ torr}$
(C) $1000\text{ torr}$
(D) $600\text{ torr}$

**Q7.M15 🟡**
According to the Clausius-Clapeyron equation, a plot of $\ln(P)$ versus $\frac{1}{T}$ gives a straight line. The slope of this line is:
(A) $\Delta H_{vap} / R$
(B) $-\Delta H_{vap} / R$
(C) $\Delta H_{vap}$
(D) $-\Delta H_{vap} / 2.303 R$

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q7.M1 → Answer: (C)**
- Vapour pressure is independent of container volume. It only depends on temperature.

**Q7.M2 → Answer: (B)**
- The exact relationship derived from $\frac{P^\circ - P_s}{P^\circ} = \chi_{solute}$ without approximations is $\frac{P^\circ - P_s}{P_s} = \frac{n_{solute}}{n_{solvent}}$.
- Trap: (A) is the approximation.

**Q7.M3 → Answer: (C)**
- Step 1: Find liquid mole fractions. $P_T = P_A^\circ \chi_A + P_B^\circ(1 - \chi_A)$.
- $400 = 300 \chi_A + 600 - 600 \chi_A \rightarrow 300 \chi_A = 200 \rightarrow \chi_A = 2/3$.
- Step 2: Find partial pressure of A. $P_A = 300 \times (2/3) = 200\text{ torr}$.
- Step 3: Find $Y_A$. $Y_A = P_A / P_T = 200 / 400 = 0.50$.
- Trap: Assuming $Y_A = \chi_A$ or doing reverse math poorly.

**Q7.M4 → Answer: (B)**
- $P_s = P^\circ \chi_{solvent}$. If $P_s = 0.5 P^\circ$, then $\chi_{solvent} = 0.5$.
- This means $\chi_{solute}$ must also be $0.5$.
- Therefore, $n_{solute} = n_{solvent}$, and their ratio is $1.0$.

**Q7.M5 → Answer: (D)**
- Since both glucose and urea are non-volatile, they do not contribute to the vapour phase. ONLY water molecules evaporate, so the vapour pressure is due solely to water.

**Q7.M6 → Answer: (B)**
- From Dalton's and Raoult's law: $P_A = Y_A P_T = \chi_A P_A^\circ \implies \chi_A = \frac{Y_A P_T}{P_A^\circ}$.
- Similarly, $\chi_B = \frac{Y_B P_T}{P_B^\circ} = \frac{(1 - Y_A) P_T}{P_B^\circ}$.
- Since $\chi_A + \chi_B = 1$, we get $\frac{Y_A P_T}{P_A^\circ} + \frac{(1 - Y_A) P_T}{P_B^\circ} = 1$.
- Divide by $P_T$: $\frac{1}{P_T} = \frac{Y_A}{P_A^\circ} + \frac{1 - Y_A}{P_B^\circ} = Y_A \left( \frac{1}{P_A^\circ} - \frac{1}{P_B^\circ} \right) + \frac{1}{P_B^\circ}$.
- This is $y = mx + c$. Slope $m = \frac{1}{P_A^\circ} - \frac{1}{P_B^\circ}$.

**Q7.M7 → Answer: (A)**
- Let $M_A = x$. $M_B = x$.
- $n_A = x / MM_A$. $n_B = x / MM_B = x / (2 MM_A) = 0.5 n_A$.
- So $n_A = 2 n_B$. Therefore $\chi_A = 2/3$, $\chi_B = 1/3$.
- $P_A = P_A^\circ (2/3)$. $P_B = P_B^\circ (1/3) = (0.5 P_A^\circ) (1/3) = (1/6) P_A^\circ$.
- $P_T = (2/3) P_A^\circ + (1/6) P_A^\circ = (5/6) P_A^\circ$.
- $Y_A = P_A / P_T = (2/3 P_A^\circ) / (5/6 P_A^\circ) = 4/5 = 0.80$.

**Q7.M8 → Answer: (B)**
- $\chi_{solvent} = n_{solvent} / (n_{solute} + n_{solvent}) = 4 / (1 + 4) = 4/5 = 0.8$.
- $P_s = P^\circ \chi_{solvent} = 17.5 \times 0.8 = 14.0\text{ mm Hg}$.

**Q7.M9 → Answer: (C)**
- This is a distillation step. The first bubble's composition is $Y_A$.
- $P_A = 100 \times 0.5 = 50$. $P_B = 300 \times 0.5 = 150$. $P_T = 200$.
- $Y_A = 50 / 200 = 0.25$.
- When this condenses, the new liquid has $\chi_A = Y_A = 0.25$.
- Trap: (A) Thinking it doesn't change, or (B) using the wrong pressure ratio.

**Q7.M10 → Answer: (B)**
- If $P_A^\circ = P_B^\circ = P^\circ$, then $P_T = P^\circ \chi_A + P^\circ \chi_B = P^\circ (\chi_A + \chi_B) = P^\circ$.
- $Y_A = P_A / P_T = (P^\circ \chi_A) / P^\circ = \chi_A$.
- The vapour composition always matches the liquid composition, but it's an ideal solution, so it's NOT considered an azeotrope (an azeotrope specifically requires non-ideal behaviour).

**Q7.M11 → Answer: (A)**
- $\chi_A = \chi_B = \chi_C = 1/3$.
- $P_A = 100/3$, $P_B = 200/3$, $P_C = 300/3$.
- $P_T = (100+200+300)/3 = 600/3 = 200$.
- $Y_B = P_B / P_T = (200/3) / 200 = 1/3 = 0.33$.

**Q7.M12 → Answer: (A)**
- At $100^\circ\text{C}$, the VP of pure water ($P^\circ$) is exactly $1\text{ atm} = 760\text{ mm Hg}$ (normal boiling point).
- $P_s = P^\circ \chi_{solvent} \implies \chi_{solvent} = P_s / P^\circ = 740 / 760$.
- Trap: (B) gives the mole fraction of the solute (RLVP).

**Q7.M13 → Answer: (C)**
- Surface area affects the *rate* of evaporation, but NOT the final equilibrium vapour pressure. VP is purely an intensive property dependent on T and nature of liquid.

**Q7.M14 → Answer: (B)**
- $Y_A = 0.40 \implies P_A = 0.40 \times P_T = 0.40 \times 600 = 240\text{ torr}$.
- $P_B = 600 - 240 = 360\text{ torr}$.
- Also, $P_A = P_A^\circ \chi_A \implies 240 = 400 \chi_A \implies \chi_A = 240/400 = 0.6$.
- Since $\chi_A = 0.6$, $\chi_B = 0.4$.
- $P_B = P_B^\circ \chi_B \implies 360 = P_B^\circ \times 0.4 \implies P_B^\circ = 360 / 0.4 = 900\text{ torr}$.

**Q7.M15 → Answer: (B)**
- The equation is $\ln(P) = -\frac{\Delta H_{vap}}{R} \cdot \frac{1}{T} + C$.
- This is $y = mx + c$. Slope $m = -\frac{\Delta H_{vap}}{R}$.
- Trap: (D) applies if the plot is $\log_{10}(P)$ instead of $\ln(P)$.
</details>

---

*Next: [Chapter 8 — Ideal vs Non-Ideal Solutions & Azeotropes →](./08_ideal_and_nonideal_solutions.md)*
