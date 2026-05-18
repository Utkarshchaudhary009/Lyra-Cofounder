# Chapter 8: Ideal vs Non-Ideal Solutions & Azeotropes
## Part IV — Vapour Pressure

---

## 🎯 Stage 1: The Core Idea

### Ideal Solutions — The Perfect World

An ideal solution is one where the A-B interactions are *exactly equal* to A-A and B-B interactions. The solute and solvent "feel" the same surrounded by either molecule.

Result: no energy change on mixing, no volume change on mixing, and perfect obedience to Raoult's Law.

**Ideal solution examples:** Benzene-Toluene, Hexane-Heptane, Ethyl bromide-Ethyl iodide, Chlorobenzene-Bromobenzene (similar structure, similar interactions).

### Non-Ideal Solutions — Reality

When A-B interactions differ from A-A and B-B, the solution deviates from Raoult's Law.

**Two types of deviation:**

| | Positive Deviation | Negative Deviation |
|--|------------------|--------------------|
| A-B interaction | **Weaker** than A-A, B-B | **Stronger** than A-A, B-B |
| Vapour Pressure | **Higher** than Raoult predicts | **Lower** than Raoult predicts |
| ΔH_mix | **> 0** (endothermic) | **< 0** (exothermic) |
| ΔV_mix | **> 0** (expansion) | **< 0** (contraction) |
| Boiling point | **Lower** | **Higher** |
| Azeotrope formed | **Minimum boiling** | **Maximum boiling** |

### Azeotropes — The "Stuck" Mixtures

An azeotrope is a liquid mixture that boils at a constant temperature — both liquid and vapour have the same composition. You **cannot** separate them by distillation.

- **Minimum boiling azeotrope:** Ethanol + Water (95% EtOH + 5% water); boils below either pure component
- **Maximum boiling azeotrope:** HNO₃ + Water (68% HNO₃ + 32% water, bp = 120.5°C); boils above either pure component

### Gibbs Free Energy of Mixing — Why Mixing Always Happens

Mixing two different liquids is always spontaneous. The driving force is captured by:

```
ΔG_mix = ΔH_mix − TΔS_mix
```

For **all** solutions (ideal or non-ideal):
- **ΔS_mix > 0** — always! Mixing two distinct species creates more microstates (disorder), regardless of interaction strengths. This is the engine that makes mixing happen.
- **ΔG_mix < 0** — always! Mixing is spontaneous.

The difference between ideal and non-ideal is only in ΔH_mix:
- **Ideal:** ΔH_mix = 0 → ΔG_mix = −TΔS_mix < 0 (entropy-driven)
- **Positive deviation:** ΔH_mix > 0 (endothermic) → ΔG_mix is less negative, but still < 0 because |TΔS| > |ΔH|
- **Negative deviation:** ΔH_mix < 0 (exothermic) → ΔG_mix is more negative than ideal

> **Key insight:** All real solutions have ΔS_mix > 0 and ΔG_mix < 0. The sign of ΔH_mix only changes the magnitude, not the direction, of spontaneity.

---

## 🔬 Stage 2: The Formula Lab

### Ideal Solution Conditions

```
P_T = P°_A χ_A + P°_B χ_B  (Raoult's Law holds)
ΔH_mix = 0
ΔV_mix = 0
ΔS_mix > 0  (always positive — entropy increases on mixing)
```

### Non-Ideal Deviations

```
Positive deviation: P_T > P°_A χ_A + P°_B χ_B
Negative deviation: P_T < P°_A χ_A + P°_B χ_B
```

### Azeotrope Condition

```
X_A = Y_A  (mole fraction in liquid = mole fraction in vapour)
X_B = Y_B

∴ Distillation cannot change composition at azeotropic point.
```

### P-x-y Diagrams — Deviation from the Ideal Line

For an ideal binary mixture, $P_{total}$ vs $\chi_A$ is a straight line. Non-ideal solutions deviate:

```
P_total
  |
  |   · ← pure A
P°_A | \   Positive deviation curve (above the line)
  |   \       Minimum boiling azeotrope forms at MAXIMUM of this curve
  |    \
  |    /       Negative deviation curve (below the line)
  |   /        Maximum boiling azeotrope forms at MINIMUM of this curve
P°_B | /· ← pure B
  |
  +------------------>
    0         1
          χ_A

Key: Dashed line = ideal (Raoult). Solid curve = actual.
     At azeotropic point: χ_A = Y_A, and the P-x and P-y curves TANGENTIALLY meet.
```

**Deviation patterns:**

| | Ideal | Positive Deviation | Negative Deviation |
|--|-------|-------------------|--------------------|
| P-x curve | Straight line | Above Raoult line (may have max) | Below Raoult line (may have min) |
| Azeotrope?<br> | No | Yes, if max is pronounced | Yes, if min is pronounced |
| Azeotrope type | — | Minimum boiling | Maximum boiling |

### T-x-y (Boiling Point) Diagrams — The Inverse Picture

Since boiling point is inversely related to vapour pressure (lower VP → higher BP), the T-x-y diagram is the **mirror image** of the P-x-y diagram:

```
Boiling point T
  |
  |   ·   Positive deviation → T-x-y shows a MINIMUM
  |    \   (minimum boiling azeotrope)
  |     \
  |      '·  Negative deviation → T-x-y shows a MAXIMUM
  |     /    (maximum boiling azeotrope)
  |    /
  |   ·/  
  |
  +------------------>
    0         1
          χ_A

Key: The azeotropic point is where liquid and vapour curves TOUCH.
     On the T-x-y diagram, the region between the liquid and vapour
     curves is the two-phase region where both phases coexist.
```

**Practical distillation insight:** When distilling a mixture:
- If the vapour reaches the azeotropic composition, it cannot progress further — the condensate has the same composition as the vapour, creating a "dead end"
- On the T-x-y diagram, at the azeotropic point, the liquid boiling curve and vapour condensation curve meet — no further enrichment

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Identifying Ideal vs Non-Ideal Solutions

**Pattern:** Given a mixture, identify if it's ideal or not — and what type of deviation.

#### Solved Example 8.1
**Q:** Classify: Ethanol + Cyclohexane. 🟡

```
Ethanol: polar, H-bonding (strong A-A)
Cyclohexane: non-polar (weak B-B)
A-B interaction: weak (unlike molecules)

→ A-B < A-A → Positive deviation from Raoult's Law
```

#### Solved Example 8.2
**Q:** Classify: Chloroform + Acetone. 🟡

```
Chloroform: δ+ H; Acetone: δ- O
→ These form H-bonds with each other:
   A-B interaction is STRONGER than A-A or B-B

→ Negative deviation from Raoult's Law
```

#### Quick Reference Table

| Mixture | Deviation |
|---------|-----------|
| Ethanol + Water | Positive |
| Acetone + CS₂ | Positive |
| CCl₄ + Benzene | Positive |
| Ethanol + Cyclohexane | Positive |
| CHCl₃ + Acetone | **Negative** |
| HCl + Water | **Negative** |
| HNO₃ + Water | **Negative** |
| Benzene + Toluene | Ideal |
| Hexane + Heptane | Ideal |

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 8.1a | Identify deviation: Acetone + CS₂ | 🟢 |
| 8.1b | Identify deviation: HCl + Water | 🟢 |
| 8.1c | What is the condition for an ideal solution?<br> | 🟢 |
| 8.1d | A solution shows positive deviation. Is A-B attraction stronger or weaker than A-A and B-B?<br> | 🟢 |
| 8.1e | Which pair forms ideal solution: <br>
(A) CHCl₃+Acetone, <br>
(B) C₆H₅Cl+C₆H₅Br, <br>
(C)
 Ethanol+Water | 🟡 |
| DPP 8.1 | If liquids A and B form an ideal solution, the: <br>
(A) Enthalpy of mixing is zero <br>
(B) Entropy of mixing is zero <br>
(C)
 Free energy of mixing is zero <br>
(D) Free energy as well as the entropy of mixing are each zero | 🟢 |
| DPP 8.3 | Which one of the following is not correct for an ideal solution?<br> <br>
(A) It must obey Raoult's law <br>
(B) ΔHmix = 0 <br>
(C)
 ΔVmix = 0 <br>
(D) ΔHmix = ΔVmix ≠0 | 🟢 |
| DPP 8.4 | Which pair from the following will not form an ideal solution?<br> <br>
(A) CCl₄ + SiCl₄ <br>
(B) H₂O + C₄H₉OH <br>
(C)
 C₂H₅Br + C₂H₅I <br>
(D) C₆H₁₄ + C₇H₁₆ | 🟢 |
| DPP 8.5 | Which of the following form an ideal solution?<br> <br>
(A) Ethyl Bromide + Ethyl iodide <br>
(B) Ethyl alcohol + Water <br>
(C)
 Chloroform + Benzene <br>
(D) HCl + Water | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**8.1a:** Acetone is polar (C=O), CS₂ is non-polar. A-B weaker than A-A. **Positive deviation.**

**8.1b:** HCl (gas) dissolves in water forming H₃O⁺ and Cl⁻ — strong ion-dipole interaction. A-B stronger than A-A or B-B. **Negative deviation.**

**8.1c:** A-B interaction = A-A = B-B (interaction strength same); ΔH_mix = 0; ΔV_mix = 0.

**8.1d:** **Weaker than A-A and B-B.** Molecules "prefer" their own kind → escape more easily → higher VP.

**8.1e:** **<br>
(B) Chlorobenzene + Bromobenzene.** Both have similar structure (benzene ring with halogen), nearly identical intermolecular forces → ideal solution.

**DPP 8.1:** For an ideal solution, the interactions are identical, so there is no change in enthalpy upon mixing (ΔH_mix = 0). Entropy of mixing is always positive (ΔS_mix > 0), and free energy of mixing is always negative (ΔG_mix < 0). → **Answer: <br>
(A)**

**DPP 8.3:** By definition, an ideal solution obeys Raoult's law, and has ΔH_mix = 0 and ΔV_mix = 0. Therefore, statement <br>
(D) is incorrect. → **Answer: <br>
(D)**

**DPP 8.4:** <br>
(A), <br>
(C)
, and <br>
(D) are classic examples of ideal solutions composed of non-polar or similarly substituted components. Water and butanol <br>
(B) form strong hydrogen bonds but have very different structures and polarities, thus forming a non-ideal solution. → **Answer: <br>
(B)**

**DPP 8.5:** Ethyl bromide and ethyl iodide have very similar structures and sizes, yielding nearly identical intermolecular forces, hence forming an ideal solution. → **Answer: <br>
(A)**
</details>

---

### Type 2: Thermodynamic Properties of Non-Ideal Solutions

**Pattern:** Given type of deviation → predict ΔH_mix, ΔV_mix, VP comparison.

#### Solved Example 8.3
**Q:** A solution shows positive deviation. Predict: (a) ΔH_mix, (b) ΔV_mix, (c) Compare VP to Raoult prediction. 🟡

```
Positive deviation → A-B weaker → less energy released on forming A-B bonds
→ Net energy absorbed (endothermic)
(a) ΔH_mix > 0

Weaker A-B → molecules spread out more
(b) ΔV_mix > 0 (volume expansion)

Molecules escape more easily (weaker attraction)
(c) VP > Raoult prediction (P_T > P°_A χ_A + P°_B χ_B)
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 8.2a | At 35°C, P°_CS₂ = 512 mm, P°_acetone = 344 mm. P_total = 600 mm (CS₂ + acetone). What type of deviation?<br> What is false: <br>
(A) 100 mL A + 100 mL B → V < 200 mL, <br>
(B) Heat absorbed, <br>
(C)
 Raoult's Law not obeyed, <br>
(D) A-B weaker than A-A, B-B?<br> ⭐ | 🔴 |
| 8.2b | Negative deviation: will the boiling point of the mixture be higher or lower than both pure components?<br> | 🟢 |
| 8.2c | A solution of CHCl₃ + acetone releases heat on mixing. What type of deviation?<br> | 🟢 |
| DPP 8.2 | A non-ideal solution was prepared by mixing 30 mL chloroform and 50 mL acetone. The volume of mixture will be: <br>
(A) > 80 mL <br>
(B) < 80 mL <br>
(C)
 = 80 mL <br>
(D) ≥80 mL | 🟡 |
| DPP 8.6 | Positive deviation from Raoult's law is shown by which of the following mixtures?<br> <br>
(A) Benzene and toluene <br>
(B) CHCl₃ and Acetone <br>
(C)
 Ethanol and Water <br>
(D) HCl and Water | 🟢 |

<details>
<summary>💡 Solutions for Type 2</summary>

**8.2a:**
- P_T = 600 mm > (512χ_CS₂ + 344χ_acetone) for typical composition → **Positive deviation**
- <br>
(A) "V < 200 mL" — FALSE. Positive deviation → ΔV_mix > 0 → **V > 200 mL** (A is false statement)
- <br>
(B) Heat absorbed → ΔH > 0 ✓ for positive deviation
- <br>
(C)
 Raoult's Law not obeyed ✓
- <br>
(D) A-B weaker ✓
- **Answer: <br>
(A) is the false statement**

**8.2b:** Negative deviation → stronger A-B attraction → molecules harder to escape → **VP below Raoult prediction → higher boiling point than either pure component.**

**8.2c:** Heat released → exothermic mixing → ΔH < 0 → **Negative deviation.**

**DPP 8.2:** Chloroform and acetone form strong hydrogen bonds between each other, resulting in a negative deviation from Raoult's law. Consequently, there is a volume contraction upon mixing (ΔV_mix < 0). Total volume < 30 + 50 = 80 mL. → **Answer: <br>
(B)**

**DPP 8.6:** Benzene-toluene is ideal. Chloroform-acetone and HCl-water show negative deviations. Ethanol and water form weaker interactions when mixed compared to the strong hydrogen bonding in pure water/ethanol, thus exhibiting positive deviation. → **Answer: <br>
(C)
**
</details>

---

### Type 3: Azeotropes — Identification and Properties

**Pattern:** Identify type of azeotrope, relate to deviation type.

#### Solved Example 8.4
**Q:** Minimum boiling azeotrope kis case me banta hai?<br> 🟢

```
Minimum boiling azeotrope:
→ Formed by positive deviation solutions
→ BP of azeotrope < BP of either pure component
→ Example: 95% Ethanol + 5% Water (bp = 78.1°C)
         Ethanol bp = 78.37°C, Water bp = 100°C
         Azeotrope bp < both!
```

#### Solved Example 8.5
**Q:** HNO₃ + Water boils at 120.5°C. HNO₃ bp = 86°C, Water bp = 100°C. Type of azeotrope?<br> 🟡

```
Azeotrope bp (120.5°C) > both pure components (86°C and 100°C)
→ Maximum boiling azeotrope
→ Formed by negative deviation (HNO₃ + Water: strong H-bonding)
```

#### Solved Example 8.6
**Q:** Can fractional distillation separate the ethanol-water azeotrope into pure components?<br> 🟡

```
At azeotropic composition, liquid and vapour have identical composition.
→ Distillation produces vapour with same composition as liquid.
→ Condensate = same composition → no separation possible.

Answer: NO — azeotropic mixture cannot be separated by fractional distillation.
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 8.3a | Which shows minimum boiling azeotrope: <br>
(A) CHCl₃+Acetone, <br>
(B) C₆H₅OH+C₆H₅NH₂, <br>
(C)
 CS₂+Acetone, <br>
(D) H₂O+HNO₃ | 🟡 |
| 8.3b | Ethanol-water azeotrope (95% EtOH). Can you obtain pure ethanol by distillation?<br> | 🟢 |
| 8.3c | Match: <br>
(A) Chloroform+Acetone, <br>
(B) Ethanol+Water → (I) Min boiling, (II) Max boiling azeotrope | 🟡 |
| 8.3d | Why is azeotrope also called "constant boiling mixture"?<br> | 🟢 |

<details>
<summary>💡 Solutions for Type 3</summary>

**8.3a:** <br>
(C)
 CS₂ + Acetone. CS₂ is non-polar, acetone is polar → positive deviation → **minimum boiling azeotrope**. 
- CHCl₃+Acetone → negative deviation → max boiling
- C₆H₅OH+C₆H₅NH₂ → negative deviation (amine-phenol H-bond) → max boiling
- H₂O+HNO₃ → negative deviation → max boiling

**8.3b:** No. The azeotropic mixture (95% EtOH) distills at constant composition — you can obtain the azeotrope but not pure ethanol by simple distillation.

**8.3c:** Chloroform + Acetone → negative deviation → **(II) Maximum boiling azeotrope**
Ethanol + Water → positive deviation → **(I) Minimum boiling azeotrope**

**8.3d:** An azeotrope boils at one constant temperature throughout (like a pure liquid), because its vapour and liquid have the same composition — so composition (and hence boiling point) never changes during distillation.

#### Enrichment: Azeotrope Breaking Methods

Since azeotropes cannot be separated by simple fractional distillation, special techniques are used:

| Method | How It Works | Example |
|--------|-------------|---------|
| **Azeotropic distillation** | Add a third component (entrainer) that alters relative volatility | Benzene added to ethanol-water azeotrope breaks the EtOH-H₂O H-bond network |
| **Pressure swing distillation** | Change external pressure → shifts azeotrope composition | Ethanol-water azeotrope changes from 95% at 1 atm to ~99% at 0.1 atm |
| **Molecular sieves** | Porous material selectively adsorbs the smaller molecule | 3A zeolite adsorbs water but not ethanol → obtain 99.9%+ ethanol |
| **Extractive distillation** | Add a high-boiling solvent that selectively interacts with one component | Ethylene glycol added to break EtOH-water azeotrope |

> **JEE Insight:** The fact that azeotrope composition changes with pressure is a key differentiator between azeotropes and true chemical compounds.

#### Practice Questions — Type 3 (Expanded)

| # | Question | Difficulty |
|---|----------|------------|
| 8.3e | Can a minimum boiling azeotrope be separated by pressure swing distillation?<br> Explain. | 🔴 |
| 8.3f | Why does adding benzene help break the ethanol-water azeotrope?<br> | 🔴 |
| 8.3g | How does a molecular sieve separate ethanol from water at the azeotropic composition?<br> | 🟡 |
| 8.3h | What distinguishes an azeotrope from a chemical compound?<br> Give two reasons. | 🟡 |

<details>
<summary>💡 Solutions for Type 3 (Expanded)</summary>

**8.3e:** Yes. Changing the external pressure shifts the azeotropic composition (unlike a pure compound whose composition is fixed). At a different pressure, the azeotropic point moves — allowing further enrichment by distillation at that new pressure.

**8.3f:** Benzene preferentially interacts with ethanol, disrupting the ethanol-water hydrogen bonds that create the azeotrope. This alters the relative volatility of ethanol vs water, allowing ethanol to distill over more effectively.

**8.3g:** Zeolite 3A has pore size of ~3Å. Water molecules (~2.8Å) enter the pores and are trapped. Ethanol molecules (~4.4Å) are too large to enter and pass through. This physically separates water from ethanol.

**8.3h:** (i) Azeotrope composition varies with pressure; chemical compound composition is fixed. (ii) Azeotropes are physical mixtures, not chemically bonded compounds. (iii) Azeotropes can be broken by adding other substances; compounds cannot be separated by physical means.
</details>

---

### Type 4: VP-Composition (P-x-y) & T-x-y Diagrams

**Pattern:** Read or sketch a P-x-y or T-x-y diagram → identify deviation type, azeotrope, and distillation behavior.

#### Key Diagram Facts

```
P-x-y Diagram:
- Liquid line (P vs χ): Straight for ideal, curved for non-ideal
- Vapour line (P vs Y): Always below the liquid line
- Positive deviation: Liquid line ABOVE Raoult ideal straight line
- Negative deviation: Liquid line BELOW Raoult ideal straight line
- Two-phase region: Area enclosed between liquid and vapour curves
- Azeotrope: Where liquid and vapour curves meet (χ = Y)

T-x-y (Boiling Point) Diagram:
- Inverse of P-x-y (lower VP → higher BP at fixed P)
- Liquid boiling curve is BELOW the vapour condensation curve
- Minimum in T-x-y ↔ Maximum in P-x-y ↔ Minimum boiling azeotrope
- Maximum in T-x-y ↔ Minimum in P-x-y ↔ Maximum boiling azeotrope
```

#### Solved Example 8.7
**Q:** The P-x-y diagram of a binary mixture A+B at 300 K shows:
- P°_A = 400 torr, P°_B = 100 torr
- At χ_A = 0.6, the actual P_total = 250 torr
- At χ_A = 0.4, P_total = 220 torr (which is the minimum P)
- At this minimum, Y_A = χ_A = 0.4

Determine: (a) Type of deviation, (b) Ideal P at χ_A = 0.6, (c) Does it form an azeotrope?<br> 🟡 ⭐

```
(a) P_ideal at χ_A = 0.6: P = 400×0.6 + 100×0.4 = 280 torr
    Actual (250) < Ideal (280) → Negative deviation ✓

(b) P_ideal at χ_A = 0.6 = 280 torr ✓

(c) Minimum at χ_A = 0.4 where Y_A = χ_A = 0.4 → Azeotrope
    P is at a MINIMUM on P-x-y → Maximum boiling azeotrope ✓
```

#### Solved Example 8.8
**Q:** The T-x-y diagram of ethanol-water shows a minimum at χ_ethanol ≈ 0.9. Answer: (a) What type of azeotrope?<br> (b) If you distill a mixture with χ_ethanol = 0.50, what happens to the compositions of liquid and vapour?<br> 🟡

```
(a) Minimum in T-x-y → Minimum boiling azeotrope ✓
    Forms in positive deviation systems.

(b) At χ_ethanol = 0.50 (below azeotropic composition):
    - Vapour is richer in ethanol than the liquid
    - As vapour is removed, the liquid becomes poorer in ethanol
    - Liquid composition moves toward χ = 0 (pure water)
    - Distillate approaches the azeotropic composition (~0.9)
    - Can never exceed the azeotropic composition by simple distillation ✓
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 8.4a | The P-x-y diagram of a mixture has the liquid line above the Raoult straight line. What type of deviation?<br> Sketch the T-x-y diagram for this mixture. | 🟡 |
| 8.4b | P°_A = 500 torr, P°_B = 200 torr. At χ_A = 0.3, actual P = 320 torr. Find ideal P and determine deviation type. | 🟡 |
| 8.4c | A T-x-y diagram shows a minimum at χ_A = 0.6. (a) Does it form an azeotrope?<br> If yes, at what χ?<br> (b) What type of deviation?<br> (c) Starting with χ_A = 0.2, can you obtain pure A by distillation?<br> ⭐ | 🔴 |
| 8.4d | Match: (i) Positive deviation → <br>
(A) P-x has max, <br>
(B) T-x has min. (ii) Negative deviation → <br>
(C)
 P-x has min, <br>
(D) T-x has max. | 🟡 |
| 8.4e | P°_A = 300 torr, P°_B = 100 torr. Actual P = 250 torr at χ_A = 0.5. (a) Find ideal P and deviation type. (b) Which component is enriched in the vapour?<br> | 🔴 |
| DPP 8.7 | A solution of A and B exhibits a minimum boiling azeotrope. The correct statement is: <br>
(A) VP is higher than ideal at all compositions <br>
(B) VP curve has a maximum <br>
(C)
 Azeotrope composition is fixed and independent of pressure <br>
(D) Both <br>
(A) and <br>
(B) | 🟡 |
| DPP 8.8 | In a T-x-y diagram for a negative deviation mixture, the: <br>
(A) Liquid curve lies above vapour curve <br>
(B) Vapour curve lies above liquid curve <br>
(C)
 Both curves coincide everywhere <br>
(D) The curves never intersect | 🟡 |

<details>
<summary>💡 Solutions for Type 4</summary>

**8.4a:** Liquid line above Raoult line → **Positive deviation**. T-x-y diagram will have a **minimum** (inverse of P-x-y maximum).

**8.4b:**
P_ideal = 500×0.3 + 200×0.7 = 150 + 140 = **290 torr**
Actual (320) > Ideal (290) → **Positive deviation**

**8.4c:**
(a) Yes, azeotrope at χ_A = **0.6** (T minimum → liquid and vapour curves meet)
(b) Min boiling azeotrope → **Positive deviation**
(c) Starting at χ_A = 0.2, vapour is richer in A. Liquid moves toward χ_A = 0. Distillate approaches χ_A = 0.6 (azeotrope). **Pure A cannot be obtained** by simple distillation.

**8.4d:**
(i) Positive → P-x has max <br>
(A), T-x has min <br>
(B)
(ii) Negative → P-x has min <br>
(C)
, T-x has max <br>
(D)

**8.4e:**
(a) P_ideal = 300×0.5 + 100×0.5 = **200 torr**; Actual (250) > Ideal → **Positive deviation**
(b) A has higher P° (300 > 100) → A is more volatile → vapour is richer in **A**

**DPP 8.7:** Min boiling azeotrope → positive deviation → P curve has a **maximum**. VP is NOT higher at ALL compositions — just sufficiently higher near the azeotropic composition. The azeotrope composition **shifts with pressure**. → **Answer: <br>
(B)**

**DPP 8.8:** In T-x-y diagrams, the vapour condensation curve lies at higher T than the liquid boiling curve (you must superheat vapour to condense it). At the azeotrope, the two curves meet. → **Answer: <br>
(B)**
</details>

---

### Type 5: Numerical Deviation Problems

**Pattern:** Given P°_A, P°_B, composition, and experimental P_total → find ideal P, deviation type, % deviation, or solve for missing data.

#### Solved Example 8.9
**Q:** P°_A = 200 torr, P°_B = 400 torr. At χ_A = 0.4, the actual P_total = 340 torr. Find: (a) Ideal P, (b) Deviation type, (c) % deviation. 🟡

```
(a) P_ideal = 200×0.4 + 400×0.6 = 80 + 240 = 320 torr

(b) Actual (340) > Ideal (320) → Positive deviation ✓

(c) % deviation = (P_actual − P_ideal) / P_ideal × 100
               = (340 − 320) / 320 × 100 = 6.25% ✓
```

#### Solved Example 8.10
**Q:** An equimolar mixture of A and B has P°_A = 100 torr, P°_B = 300 torr. Raoult predicts P = 200 torr, but actual P = 160 torr. The vapour phase composition is Y_A = 0.25, Y_B = 0.75. Find the actual partial pressures and compare with Raoult predictions. 🟡 ⭐

```
Actual P_total = 160 torr
P_A(actual) = Y_A × P_total = 0.25 × 160 = 40 torr
P_B(actual) = Y_B × P_total = 0.75 × 160 = 120 torr
Check: 40 + 120 = 160 ✓

Raoult predictions: P_A(ideal) = 100×0.5 = 50 torr
                     P_B(ideal) = 300×0.5 = 150 torr

Both actual P_A (40 < 50) and P_B (120 < 150) are BELOW ideal → Negative deviation ✓
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 8.5a | P°_A = 250, P°_B = 500 torr. At χ_A = 0.6, actual P = 350 torr. Find ideal P, deviation type, and % deviation. ⭐ | 🟡 |
| 8.5b | At χ_A = 0.5, P_ideal = 300, P_actual = 330. At χ_A = 0.25, P_ideal = 200, P_actual = 180. Is the deviation type the same at both compositions?<br> | 🔴 |
| 8.5c | P°_A = 600, P°_B = 200. An equimolar mixture has actual P = 500 torr. Y_A in vapour = 0.6. Find the actual P_A, P_B and compare with Raoult predictions. | 🔴 |
| 8.5d | At χ_A = 0.4, P_ideal = 280 torr, P_actual = 300 torr. P°_A = 400, P°_B = 200, Y_A = 0.533. Find actual P_A and P_B. Does this confirm the deviation type?<br> ⭐ | 🔴 |
| 8.5e | A mixture with χ_A = 0.3 has P_actual = 195 torr. P°_B = 150 torr, P_ideal = 180 torr. Find P°_A and deviation type. | 🟡 |
| DPP 8.9 | The actual VP of an equimolar mixture of A and B is 420 torr. P°_A = 300, P°_B = 500 torr. The % deviation is: <br>
(A) Positive, 5% <br>
(B) Positive, 10% <br>
(C)
 Negative, 5% <br>
(D) Negative, 10% | 🟡 |
| DPP 8.10 | For a binary solution with χ_A = 0.3: P_ideal = 180 torr, P_actual = 195 torr. If P°_B = 150 torr, find P°_A. | 🟡 |

<details>
<summary>💡 Solutions for Type 5</summary>

**8.5a:**
P_ideal = 250×0.6 + 500×0.4 = 150 + 200 = **350 torr**
Actual (350) = Ideal (350) → **Ideal solution**, % deviation = **0%**

**8.5b:**
At χ_A = 0.5: Actual (330) > Ideal (300) → positive deviation
At χ_A = 0.25: Actual (180) < Ideal (200) → negative deviation
**No, the deviation type changes with composition.** Some real solutions show a crossover — the deviation flips sign. This is more complex than simple single-deviation classification.

**8.5c:**
P_ideal = 600×0.5 + 200×0.5 = 400 torr
Actual P_A = Y_A × P_total = 0.6×500 = **300 torr**
Actual P_B = 0.4×500 = **200 torr**
Raoult predictions: P_A = 600×0.5 = 300; P_B = 200×0.5 = 100
P_A (300) matches Raoult (300). P_B (200) > Raoult (100).
**Positive deviation** (from B), but A behaves ideally. Total: 500 > 400 → positive ✓

**8.5d:**
P_actual = 300. Y_A = 0.533.
Actual P_A = 0.533×300 = **160 torr**
Actual P_B = (1−0.533)×300 = 0.467×300 = **140 torr**
Raoult P_A = 400×0.4 = 160; Raoult P_B = 200×0.6 = 120
P_A (160) = Raoult (160) — no deviation for A
P_B (140) > Raoult (120) — positive deviation for B
Total: 300 > 280 → confirms **positive deviation** ✓

**8.5e:**
P_ideal = P°_A×0.3 + 150×0.7 = 180
0.3P°_A + 105 = 180 → 0.3P°_A = 75 → **P°_A = 250 torr**
Actual (195) > Ideal (180) → **Positive deviation**

**DPP 8.9:**
P_ideal = 300×0.5 + 500×0.5 = 400 torr
Actual (420) > Ideal (400) → Positive deviation
% = (420−400)/400 × 100 = 5%
→ **Answer: <br>
(A)**

**DPP 8.10:**
P_ideal = P°_A×0.3 + 150×0.7 = 180
0.3P°_A + 105 = 180 → P°_A = 75/0.3 = **250 torr**
</details>

---

### Type 6: Azeotrope Data Analysis

**Pattern:** Given azeotropic composition and pure VP data → compare with ideal, confirm deviation type, classify azeotrope.

#### Key Azeotrope Math

```
At azeotrope: χ_A = Y_A, χ_B = Y_B
This means P_A/P_total = χ_A and P_B/P_total = χ_B
P_total(actual) = P°_A χ_A + P°_B χ_B + Δ(deviation)

For positive deviation: P_actual > P_ideal → P-x-y has a MAXIMUM → min boiling azeotrope
For negative deviation: P_actual < P_ideal → P-x-y has a MINIMUM → max boiling azeotrope
```

#### Solved Example 8.11
**Q:** A minimum boiling azeotrope forms at χ_A = 0.6. P°_A = 200 torr, P°_B = 100 torr at the azeotropic temperature. (a) Find ideal P at the azeotropic composition. (b) Should actual P be greater or less than this?<br> (c) If the actual P at the azeotrope is 180 torr, find % deviation from Raoult. 🟡

```
(a) χ_A = 0.6, χ_B = 0.4
    P_ideal = 200×0.6 + 100×0.4 = 120 + 40 = 160 torr ✓

(b) Minimum boiling azeotrope → Positive deviation
    → Actual P > Ideal P ✓

(c) % deviation = (180 − 160)/160 × 100 = 12.5% ✓
```

#### Solved Example 8.12
**Q:** A maximum boiling azeotrope has χ_HNO₃ = 0.38. At the boiling temperature, P°_H₂O = 1485 torr and P°_HNO₃ = 380 torr. (a) Find the ideal P at this composition. (b) The actual VP of the mixture at this T is 760 torr (1 atm). Find the % deviation and classify. 🔴 ⭐

```
(a) χ_H₂O = 1 − 0.38 = 0.62
    P_ideal = 1485×0.62 + 380×0.38 = 920.7 + 144.4 = 1065.1 torr ✓

(b) Maximum boiling azeotrope → Negative deviation
    Actual (760) < Ideal (1065) ✓
    % deviation = (760 − 1065)/1065 × 100
               = −305/1065 × 100 = −28.6%
    (Negative sign confirms negative deviation) ✓
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 8.6a | A minimum boiling azeotrope exists at χ_A = 0.7. P°_A = 300, P°_B = 150 torr. Find ideal P and state whether actual P is higher or lower. | 🟡 |
| 8.6b | A maximum boiling azeotrope of A and B has χ_A = 0.4. P°_A = 700 torr, P°_B = 600 torr at the azeotropic T. Find ideal P and % deviation if actual P = 580 torr. ⭐ | 🔴 |
| 8.6c | The azeotrope of CHCl₃ + acetone (negative deviation) has χ_CHCl₃ = 0.4. P°_CHCl₃ = 295 torr, P°_acetone = 345 torr. Compute ideal VP. If actual VP = 280 torr, find % deviation. | 🔴 |
| 8.6d | A mixture forms an azeotrope at χ_A = 0.3. P°_A = 300, P°_B = 100 torr. The actual P at this composition is 250 torr. Classify the azeotrope and calculate % deviation. | 🟡 |
| DPP 8.11 | At the azeotropic composition of a minimum boiling azeotrope: <br>
(A) P_total is maximum, Y_A = χ_A <br>
(B) P_total is minimum, Y_A = χ_A <br>
(C)
 P_total is maximum, Y_A > χ_A <br>
(D) P_total is minimum, Y_A < χ_A | 🟡 |
| DPP 8.12 | A maximum boiling azeotrope has P_actual < P_ideal at the azeotropic composition. This implies: <br>
(A) ΔH_mix > 0 <br>
(B) ΔV_mix > 0 <br>
(C)
 A-B interactions weaker than A-A, B-B <br>
(D) The solution shows negative deviation | 🟡 |

<details>
<summary>💡 Solutions for Type 6</summary>

**8.6a:**
P_ideal = 300×0.7 + 150×0.3 = 210 + 45 = **255 torr**
Minimum boiling azeotrope → positive deviation → **actual P > 255 torr**

**8.6b:**
χ_A = 0.4, χ_B = 0.6
P_ideal = 700×0.4 + 600×0.6 = 280 + 360 = **640 torr**
Max boiling azeotrope → negative deviation → actual < ideal ✓
Actual = 580 → % deviation = (580−640)/640 × 100 = **−9.375%**

**8.6c:**
χ_CHCl₃ = 0.4, χ_acetone = 0.6
P_ideal = 295×0.4 + 345×0.6 = 118 + 207 = **325 torr**
Negative deviation → Actual < Ideal → 280 < 325 ✓
% deviation = (280−325)/325 × 100 = **−13.8%**

**8.6d:**
P_ideal = 300×0.3 + 100×0.7 = 90 + 70 = **160 torr**
Actual (250) > Ideal (160) → Positive deviation
% deviation = (250−160)/160 × 100 = **56.25%**
Positive deviation → **Minimum boiling azeotrope** ✓

**DPP 8.11:** Minimum boiling azeotrope → positive deviation → P_total curve has a **maximum** (higher VP means boils at lower T). At this max, Y_A = χ_A (azeotrope condition). → **Answer: <br>
(A)**

**DPP 8.12:** P_actual < P_ideal at the azeotrope → lower VP than predicted → stronger A-B bonds hold molecules in liquid → exothermic ΔH < 0 → volume contraction ΔV < 0. → **Answer: <br>
(D)**
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 8.M1 | CS₂ + Acetone: P_total = 600 mm at 35°C (P°_CS₂ = 512, P°_acetone = 344). Is this deviation positive or negative?<br> Calculate ideal P and compare. | T1+T2 | 🔴 |
| 8.M2 | A binary mixture shows negative deviation. (a) Draw a qualitative VP vs. χ curve. (b) What type of azeotrope forms?<br> (c) Which mixture does this?<br> | T1+T3 | 🟡 |
| 8.M3 | Ethanol-water mixture: pure water bp = 100°C, pure ethanol bp = 78.4°C. Azeotrope bp = 78.1°C. Identify azeotrope type and deviation. Explain why separation by distillation fails. | T1+T3 | 🟡 |
| 8.M4 | The P-x-y diagram of A+B shows the liquid line below the Raoult line at all compositions. A minimum is observed at P = 220 torr, χ_A = 0.4. P°_A = 400 torr, P°_B = 100 torr. (a) Deviation type?<br> (b) Does an azeotrope form?<br> (c) Find ideal P at χ_A = 0.4. | T4+T5 | 🔴 |
| 8.M5 | A maximum boiling azeotrope of A (P°_A = 500 torr) and B (P°_B = 300 torr) forms at χ_A = 0.5. The actual VP at the azeotropic T is 340 torr. (a) Find ideal P and % deviation. (b) If this mixture is distilled, which component enriches in the residue?<br> | T6+T3 | 🔴 ⭐ |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**8.M1:**
- Equimolar mixture: χ_CS₂ = χ_acetone = 0.5 (assuming)
- Ideal P = 512×0.5 + 344×0.5 = 428 mm
- Actual P = 600 mm > 428 mm → **Positive deviation**
- A-B interaction (CS₂-acetone) weaker than A-A or B-B

**8.M2:**
- (a) VP curve lies below the ideal (straight line) Raoult prediction; shows a minimum.
- (b) **Maximum boiling azeotrope** (boiling point at maximum, VP at minimum)
- (c) Examples: CHCl₃ + Acetone; HNO₃ + Water

**8.M3:**
- Azeotrope bp (78.1°C) < ethanol bp (78.4°C) < water bp (100°C)
- **Minimum boiling azeotrope** → **Positive deviation** (EtOH-Water: A-B weaker than strong H-bonded A-A or B-B)
- At azeotropic point: χ_liquid = χ_vapour → distillation produces vapour of same composition → condenses to same composition → no change possible

**8.M4:**
(a) Liquid line below Raoult line → **Negative deviation** ✓
(b) Minimum observed on P-x-y → **Azeotrope forms at χ_A = 0.4** ✓
   Minimum P → Maximum boiling azeotrope ✓
(c) P_ideal at χ_A = 0.4: P = 400×0.4 + 100×0.6 = 160 + 60 = **220 torr**
   Actual P = 220 torr = Ideal P at this exact composition (coincidence — the curves touch at the minimum; deviation is zero only at the minimum point where the slope changes sign)

**8.M5:**
(a) χ_A = 0.5, χ_B = 0.5
    P_ideal = 500×0.5 + 300×0.5 = 250 + 150 = **400 torr**
    Actual = 340 < ideal → **% deviation = (340−400)/400 × 100 = −15%** ✓
(b) Maximum boiling azeotrope → mixture has higher BP than pure components.
    During distillation, the higher-boiling azeotrope stays in the residue.
    The lower-boiling component distills off first.
    Since this is a max boiling azeotrope, the azeotrope composition itself has the highest BP.
    **B is less volatile** (P°_B = 300 < P°_A = 500 → B is less volatile)
    → A enriches in the vapour, B enriches in the residue.
    → **Residue becomes richer in B** (the less volatile component)
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 8.B1 | What are ideal solutions?<br> State two conditions. *(NCERT)* | 🟢 |
| 8.B2 | Distinguish between positive and negative deviations from Raoult's Law. | 🟡 |
| 8.B3 | What are azeotropes?<br> Explain minimum and maximum boiling azeotropes with examples. *(NCERT)* ⭐ | 🟡 |
| 8.B4 | A solution of ethanol in cyclohexane shows positive deviation. Explain: (a) ΔH_mix, (b) ΔV_mix, (c) Can they be separated by distillation?<br> | 🟡 |
| 8.B5 | Why can't azeotropic mixtures be separated by fractional distillation?<br> | 🟢 |
| 8.B6 | What is the sign of ΔG_mix for an ideal solution?<br> Explain why mixing is always spontaneous. | 🟢 |
| 8.B7 | Draw a labelled P-x-y diagram showing positive deviation from Raoult's Law. Mark: (i) the ideal Raoult line, (ii) the actual VP curve, (iii) the azeotropic point. | 🟡 |
| 8.B8 | Calculate the ideal VP of an equimolar mixture of A (P°_A = 400 torr) and B (P°_B = 200 torr). The actual VP is 350 torr. Classify the deviation and calculate % deviation. ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**8.B1:** Ideal solutions obey Raoult's Law over entire composition range. Conditions: (1) ΔH_mix = 0 (no heat absorbed or released), (2) ΔV_mix = 0 (no volume change on mixing).

**8.B2:**
| Property | Positive Deviation | Negative Deviation |
|----------|-------------------|--------------------|
| VP | Higher than Raoult | Lower than Raoult |
| ΔH_mix | > 0 (endothermic) | < 0 (exothermic) |
| ΔV_mix | > 0 (expansion) | < 0 (contraction) |
| A-B forces | Weaker | Stronger |

**8.B3:** Azeotropes = constant-boiling binary liquid mixtures where both phases have the same composition.
- *Minimum boiling:* Formed by positive deviation; BP < either pure component. Example: 95% EtOH + 5% water.
- *Maximum boiling:* Formed by negative deviation; BP > either pure component. Example: 68% HNO₃ + 32% water.

**8.B4:**
- (a) ΔH_mix > 0 (endothermic — weak A-B formed)
- (b) ΔV_mix > 0 (expansion)
- (c) Partially — can be enriched but at the azeotropic point (if positive deviation), distillation stops changing composition. Cannot obtain pure components.

**8.B5:** At the azeotropic composition, the vapour and liquid have identical mole fractions. The condensate from distilled vapour is the same composition as the original liquid — no enrichment occurs. The system is "stuck" at this boiling point.

**8.B6:** ΔG_mix = ΔH_mix − TΔS_mix. For an ideal solution: ΔH_mix = 0, ΔS_mix > 0 (always positive for mixing two distinct species). Therefore: **ΔG_mix = −TΔS_mix < 0** — mixing is always spontaneous (negative ΔG). The entropy increase from mixing drives the process.

**8.B7:**
```
P_total ↑    · ← pure A (P°_A)
  |   ·       ·
  |    \  ·····   ← actual VP curve (above Raoult)
  |     \       ·  (has a maximum where azeotrope forms)
  |      \     · 
  |       \   ·   ← - - - Raoult ideal line (straight)
  |        \ ·
  |         ·← pure B (P°_B)
  +-------------------→
  0         χ_A     1
           ↑
     Azeotropic point
     (χ_A = Y_A at this max)
```

**8.B8:**
χ_A = χ_B = 0.5
P_ideal = 400×0.5 + 200×0.5 = 200 + 100 = **300 torr**
Actual (350) > Ideal (300) → **Positive deviation**
% deviation = (350−300)/300 × 100 = **16.67%**
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q8.J1 🟡 ⭐**
Which of the following is a minimum boiling azeotrope?<br>
<br>
(A) HNO₃ + Water  <br>
(B) HCl + Water  <br>
(C)
 Ethanol + Water  <br>
(D) CHCl₃ + Acetone

**Q8.J2 🟡**
A solution shows ΔH_mix < 0 and ΔV_mix < 0. Its deviation from Raoult's Law is:
<br>
(A) Positive  <br>
(B) Negative  <br>
(C)
 Zero (Ideal)  <br>
(D) Cannot determine

**Q8.J3 🔴 ⭐**
Identify the mixture that shows positive deviation:
<br>
(A) (CH₃)₂CO + C₆H₅NH₂  <br>
(B) CHCl₃ + C₆H₆  <br>
(C)
 CHCl₃ + (CH₃)₂CO  <br>
(D) (CH₃)₂CO + CS₂

**Q8.J4 🔴**
The azeotropic mixture of HCl and water boils at 108.5°C (pure HCl bp = −85°C, pure water = 100°C). Distilling this mixture can give:
<br>
(A) Pure HCl only  <br>
(B) Pure water only  <br>
(C)
 Neither pure HCl nor pure water  <br>
(D) Both pure HCl and water

**Q8.J5 🔴 ⭐**
For a solution showing negative deviation, which combination of properties is TRUE?<br>
<br>
(A) ΔH > 0, ΔV > 0, A-B weaker
<br>
(B) ΔH < 0, ΔV < 0, A-B stronger, VP lower than Raoult
<br>
(C)
 ΔH > 0, ΔV < 0, VP higher than Raoult
<br>
(D) ΔH < 0, ΔV > 0, VP lower than Raoult

**Q8.J6 🔴 (P-x-y Graph Analysis)**
The P-x-y diagram of a binary mixture at 300 K shows these data points:
- χ_A = 0: P = 200 torr; χ_A = 1: P = 400 torr
- The actual P curve has a maximum at P = 500 torr where χ_A = 0.3
- At this maximum, Y_A = χ_A = 0.3
Which of the following is correct?<br>
<br>
(A) The mixture shows negative deviation, azeotrope at χ_A = 0.3, max boiling
<br>
(B) The mixture shows positive deviation, azeotrope at χ_A = 0.3, min boiling
<br>
(C)
 The mixture shows negative deviation, azeotrope at χ_A = 0.7
<br>
(D) Ideal solution, no azeotrope

**Q8.J7 🔴 ⭐**
P°_A = 400 torr, P°_B = 100 torr. An equimolar mixture has actual P_total = 300 torr. Y_A in the vapour = 0.667. The actual P_A and P_B are:
<br>
(A) P_A = 150, P_B = 150  <br>
(B) P_A = 200, P_B = 100  <br>
(C)
 P_A = 250, P_B = 50  <br>
(D) P_A = 100, P_B = 200

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**8.J1 → Answer: <br>
(C)
**
- HNO₃+Water: negative deviation → **maximum** boiling azeotrope
- HCl+Water: negative deviation → max boiling
- **Ethanol+Water: positive deviation → minimum boiling azeotrope ✓**
- CHCl₃+Acetone: negative deviation → max boiling

**8.J2 → Answer: <br>
(B)**
- ΔH < 0 → exothermic → stronger A-B bond formed → A-B stronger → **negative deviation ✓**
- ΔV < 0 → confirms negative deviation (contraction on mixing)

**8.J3 → Answer: <br>
(D)**
- <br>
(A) Acetone + Aniline: polar-polar, similar size → likely negative deviation
- <br>
(B) CHCl₃ + Benzene: CHCl₃ has dipole; benzene provides π electrons → H-bond type → negative deviation
- <br>
(C)
 CHCl₃ + Acetone: strong A-B H-bond → negative deviation
- **<br>
(D) Acetone + CS₂: polar + non-polar → A-B weaker → positive deviation ✓**

**8.J4 → Answer: <br>
(C)
**
- Azeotrope composition is fixed. Distillation always produces this same composition.
- **Neither pure HCl nor pure water can be obtained ✓**

**8.J5 → Answer: <br>
(B)**
- Negative deviation: A-B stronger → exothermic (ΔH < 0) → contraction (ΔV < 0) → stronger attraction keeps molecules in liquid → VP lower than Raoult prediction
- **All conditions in <br>
(B) are correct ✓**

**8.J6 → Answer: <br>
(B)**
- P°_A = 400 (from χ_A = 1), P°_B = 200 (from χ_A = 0)
- The actual P (500) > both P° values → **Positive deviation** ✓
- Maximum in P-x-y → Minimum boiling azeotrope ✓
- At maximum, Y_A = χ_A = 0.3 → **Azeotrope at χ_A = 0.3** ✓

**8.J7 → Answer: <br>
(B)**
- P_total = 300 torr, Y_A = 0.667
- P_A(actual) = Y_A × P_total = 0.667 × 300 = 200 torr ✓
- P_B(actual) = (1−0.667) × 300 = 100 torr ✓
- Check: Raoult predicts P_A = 400×0.5 = 200, P_B = 100×0.5 = 50
- P_A (200) = Raoult (200), P_B (100) > Raoult (50) → Positive deviation (from B)
- → **Answer: <br>
(B) P_A = 200, P_B = 100** ✓
</details>

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
| 8.S1 | **Assertion <br>
(A):** A mixture of chloroform and acetone forms a solution with a volume strictly less than the sum of their individual volumes.<br>**Reason (R):** Chloroform and acetone form strong intermolecular hydrogen bonds, leading to a negative deviation from Raoult's Law and $\Delta V_{mix} < 0$. | 🟢 |
| 8.S2 | **Statement I:** In an ideal solution, the entropy of mixing ($\Delta S_{mix}$) is zero.<br>**Statement II:** Since the interactions (A-A, B-B, A-B) are identical in an ideal solution, no thermodynamic disorder is created upon mixing. | 🔴 |
| 8.S3 | **Assertion <br>
(A):** An azeotropic mixture of ethanol and water cannot be separated into pure components by fractional distillation.<br>**Reason (R):** At the azeotropic composition, the liquid and vapour phases have identical mole fractions. | 🟢 |
| 8.S4 | **Statement I:** A solution showing positive deviation from Raoult's law will always form a minimum boiling azeotrope at some specific composition.<br>**Statement II:** Positive deviation means the vapour pressure is higher than ideal, which corresponds to a lower boiling point. | 🟡 |
| 8.S5 | **Assertion <br>
(A):** When $10\text{ mL}$ of ethanol is mixed with $10\text{ mL}$ of water, the total volume becomes exactly $20\text{ mL}$.<br>**Reason (R):** Both ethanol and water are highly polar molecules that readily form hydrogen bonds. | 🟡 |
| 8.S6 | **Statement I:** If $\Delta H_{mix} > 0$ for a binary liquid mixture, the solution will feel cold to the touch upon mixing.<br>**Statement II:** $\Delta H_{mix} > 0$ implies the process is endothermic, meaning heat is absorbed from the surroundings. | 🟢 |
| 8.S7 | **Assertion <br>
(A):** A mixture of nitric acid ($HNO_3$) and water shows a massive negative deviation from Raoult's law.<br>**Reason (R):** Nitric acid completely dissociates in water, and the resulting ion-dipole interactions are much stronger than the original hydrogen bonds in pure water. | 🟡 |
| 8.S8 | **Statement I:** For a solution showing negative deviation, the partial vapour pressure of component A ($P_A$) is less than $P_A^\circ \chi_A$.<br>**Statement II:** The total vapour pressure is less than $P_A^\circ \chi_A + P_B^\circ \chi_B$, but individual partial pressures can still be higher than their Raoult prediction. | 🔴 |
| 8.S9 | **Assertion <br>
(A):** Hexane and heptane form a nearly ideal solution.<br>**Reason (R):** Both are non-polar aliphatic hydrocarbons of similar size, leading to roughly equal A-A, B-B, and A-B van der Waals forces. | 🟢 |
| 8.S10 | **Statement I:** In a maximum boiling azeotrope, the boiling point of the mixture is higher than the boiling points of both pure components.<br>**Statement II:** Maximum boiling azeotropes are formed by solutions exhibiting large positive deviations from Raoult's law. | 🟡 |
| 8.S11 | **Assertion <br>
(A):** To separate the components of an azeotrope, one must use non-distillation techniques like chemical separation or azeotropic distillation (adding a third component).<br>**Reason (R):** Fractional distillation relies on differences in volatility, but at the azeotropic point, both components behave as a single liquid with uniform volatility. | 🟢 |
| 8.S12 | **Statement I:** For an ideal solution, $\Delta G_{mix} = 0$.<br>**Statement II:** Since $\Delta H_{mix} = 0$ and $\Delta S_{mix} = 0$ for ideal solutions, the Gibbs free energy change must be zero. | 🔴 |
| 8.S13 | **Assertion <br>
(A):** Dissolving $HCl$ gas in water forms a solution that shows a positive deviation from Raoult's law.<br>**Reason (R):** Gases naturally want to escape, resulting in a higher vapour pressure. | 🟡 |
| 8.S14 | **Statement I:** An azeotrope is a chemical compound formed by the reaction of two liquids in a fixed stoichiometric ratio.<br>**Statement II:** The fixed boiling point and constant composition of an azeotrope mimic the properties of a pure compound. | 🟢 |
| 8.S15 | **Assertion <br>
(A):** Benzene and toluene form an ideal solution at all temperatures.<br>**Reason (R):** Ideal behaviour is independent of temperature as long as the molecular structures remain intact. | 🟡 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**8.S1 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- True. Stronger A-B bonds pull molecules closer together, causing volume contraction ($\Delta V_{mix} < 0$).

**8.S2 → Statement I is False, Statement II is False.**
- Statement I is false: Entropy of mixing ($\Delta S_{mix}$) is ALWAYS positive for any mixture (ideal or non-ideal), because mixing increases disorder.
- Statement II is false: Thermodynamic disorder (entropy) is related to the number of microstates, which always increases when two distinct species are mixed, regardless of their interactions.

**8.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is the fundamental definition of an azeotrope and why fractional distillation fails.

**8.S4 → Statement I is False, Statement II is True.**
- Statement I is false: A solution must show a LARGE positive deviation to form an azeotrope. Small positive deviations (like in many mildly non-ideal mixtures) do NOT create a maximum or minimum in the VP curve, thus no azeotrope forms.
- Statement II is true: Positive deviation = higher VP = lower boiling point.

**8.S5 → Answer: <br>
(D) A is false but R is true.**
- A is false: 10 mL ethanol + 10 mL water ≠ 20 mL. Ethanol-water is non-ideal (positive deviation from Raoult's Law). For ANY non-ideal solution, the volumes are not exactly additive, so total ≠ 20 mL.
- R is true: Both ethanol and water are polar molecules capable of hydrogen bonding.
- (A is false because the volume is never exactly additive for non-ideal solutions; R is true independently.)

**8.S6 → Statement I is True, Statement II is True.**
- Endothermic processes absorb heat from the surroundings (the solution itself, the beaker, your hand), making it feel cold.

**8.S7 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- The formation of $H_3O^+$ and $NO_3^-$ creates strong ion-dipole interactions, which are much stronger than the H-bonds in pure water or pure $HNO_3$, leading to negative deviation.

**8.S8 → Statement I is True, Statement II is False.**
- Statement I is true: Negative deviation applies to both the total pressure AND the individual partial pressures.
- Statement II is false: Individual partial pressures are ALSO less than their Raoult prediction ($P_A < P_A^\circ \chi_A$).

**8.S9 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Classic textbook example of an ideal solution.

**8.S10 → Statement I is True, Statement II is False.**
- Statement I is true: Max boiling azeotrope boils at a temperature higher than both pure components.
- Statement II is false: Maximum boiling azeotropes are formed by solutions exhibiting NEGATIVE deviations (lower VP $\rightarrow$ higher BP).

**8.S11 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is correct. Adding benzene to ethanol-water azeotrope breaks it, a process called azeotropic distillation.

**8.S12 → Statement I is False, Statement II is False.**
- Statement I is false: Mixing is spontaneous, so $\Delta G_{mix} < 0$.
- Statement II is false: $\Delta S_{mix}$ is positive, so $\Delta G_{mix} = \Delta H_{mix} - T\Delta S_{mix} = 0 - T(+ve) = \text{negative}$.

**8.S13 → Answer: <br>
(D) A is false but R is true.**
- A is false: $HCl$ + water shows NEGATIVE deviation because it ionizes and forms strong ion-dipole interactions.
- R is true: Gases do have high vapour pressure, but in this specific solution context, the interaction overcomes the natural volatility.

**8.S14 → Statement I is False, Statement II is True.**
- Statement I is false: An azeotrope is a MIXTURE, not a chemical compound. The ratio can change if external pressure changes (unlike a true chemical compound which has a fixed ratio by Dalton's atomic theory).
- Statement II is true: It *mimics* a pure compound by boiling at a constant temperature.

**8.S15 → Answer: <br>
(C)
 A is true but R is false.**
- A is true: It is considered the standard ideal solution.
- R is false: "Ideal behaviour" can deviate slightly at extreme temperatures where molecular kinetic energy vastly overpowers intermolecular forces or near freezing points. But more importantly, no solution is *perfectly* ideal at all temperatures.

</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q8.M1 🟢**
Which of the following thermodynamic properties is strictly ZERO for an ideal solution?<br>
<br>
(A) $\Delta S_{mix}$
<br>
(B) $\Delta G_{mix}$
<br>
(C)
 $\Delta H_{mix}$
<br>
(D) Both <br>
(A) and <br>
(C)


**Q8.M2 🟡 (The "Double Negative" Trap)**
A liquid mixture of A and B shows negative deviation from Raoult's law. Which of the following statements is INCORRECT?<br>
<br>
(A) The boiling point of the mixture is higher than expected.
<br>
(B) The A-B intermolecular forces are stronger than A-A and B-B forces.
<br>
(C)
 The process of mixing A and B is endothermic.
<br>
(D) The total volume of the mixture is less than the sum of individual volumes.

**Q8.M3 🔴**
An azeotropic mixture of $HNO_3$ and water boils at $120.5^\circ\text{C}$ ($1\text{ atm}$). The boiling point of pure $HNO_3$ is $86^\circ\text{C}$ and pure water is $100^\circ\text{C}$. This mixture exhibits:
<br>
(A) Large positive deviation from Raoult's law
<br>
(B) Large negative deviation from Raoult's law
<br>
(C)
 Ideal behaviour at $120.5^\circ\text{C}$
<br>
(D) No deviation from Raoult's law

**Q8.M4 🟡**
$100\text{ mL}$ of liquid A and $50\text{ mL}$ of liquid B are mixed. The total volume of the resulting solution was found to be $152\text{ mL}$. What type of deviation does this solution show, and what type of azeotrope might it form?<br>
<br>
(A) Positive deviation, Minimum boiling azeotrope
<br>
(B) Positive deviation, Maximum boiling azeotrope
<br>
(C)
 Negative deviation, Minimum boiling azeotrope
<br>
(D) Negative deviation, Maximum boiling azeotrope

**Q8.M5 🟡 (The "Temperature Dependent Azeotrope" Trap)**
Is the composition of an azeotrope completely fixed and independent of external conditions?<br>
<br>
(A) Yes, because it behaves like a pure chemical compound.
<br>
(B) Yes, because Raoult's law dictates a fixed composition for minimum/maximum VP.
<br>
(C)
 No, altering the external pressure will change the boiling point and the azeotropic composition.
<br>
(D) No, adding a catalyst will change its composition.

**Q8.M6 🔴**
Consider two solutions: 
Solution 1: Ethanol + Water
Solution 2: Chloroform + Acetone
Which of the following correctly pairs the solution with the sign of its enthalpy of mixing ($\Delta H_{mix}$)?<br>
<br>
(A) 1: Positive, 2: Positive
<br>
(B) 1: Negative, 2: Positive
<br>
(C)
 1: Positive, 2: Negative
<br>
(D) 1: Negative, 2: Negative

**Q8.M7 🟡**
If a binary mixture shows a large positive deviation from Raoult's law, the vapor pressure vs. mole fraction curve will have a:
<br>
(A) Maximum, corresponding to a minimum boiling point
<br>
(B) Minimum, corresponding to a minimum boiling point
<br>
(C)
 Maximum, corresponding to a maximum boiling point
<br>
(D) Minimum, corresponding to a maximum boiling point

**Q8.M8 🟢**
Which of the following mixtures forms an ideal solution?<br>
<br>
(A) Chloroform and Benzene
<br>
(B) Ethyl chloride and Ethyl bromide
<br>
(C)
 Phenol and Aniline
<br>
(D) Water and Nitric acid

**Q8.M9 🔴 (The "Reverse Logic" Trap)**
You are given an unknown binary liquid mixture. During fractional distillation, you notice that the residue in the distillation flask becomes progressively richer in component A, while the distillate collected is a constant-boiling mixture. What can you conclude?<br>
<br>
(A) The mixture forms a maximum boiling azeotrope.
<br>
(B) The mixture forms a minimum boiling azeotrope.
<br>
(C)
 Component A is more volatile than component B.
<br>
(D) The solution is perfectly ideal.

**Q8.M10 🟡**
For a non-ideal solution showing positive deviation, the relationship between observed partial pressure ($P_A$) and Raoult's law predicted partial pressure ($P_A^\circ \chi_A$) is:
<br>
(A) $P_A = P_A^\circ \chi_A$
<br>
(B) $P_A > P_A^\circ \chi_A$
<br>
(C)
 $P_A < P_A^\circ \chi_A$
<br>
(D) Depends on the specific liquids

**Q8.M11 🔴**
An ideal mixture contains equimolar amounts of A and B. If $P_A^\circ = 200\text{ mm}$ and $P_B^\circ = 100\text{ mm}$, the vapour will be:
<br>
(A) Equimolar
<br>
(B) Richer in B
<br>
(C)
 Richer in A
<br>
(D) Pure A

**Q8.M12 🟡**
In a mixture of A and B showing negative deviation, the escaping tendency of molecules A and B from the solution:
<br>
(A) Increases
<br>
(B) Decreases
<br>
(C)
 Remains the same
<br>
(D) Becomes zero

**Q8.M13 🟢**
The azeotropic mixture of water and ethanol contains approx 95% ethanol by volume. If you distill a 50% ethanol solution, what is the maximum concentration of ethanol you can achieve in the distillate?<br>
<br>
(A) 100%
<br>
(B) 50%
<br>
(C)
 95%
<br>
(D) 0%

**Q8.M14 🔴 (The "Entropy Illusion" Trap)**
For a highly non-ideal solution with a massive negative deviation (e.g., strong acid + water), the entropy of mixing ($\Delta S_{mix}$) is:
<br>
(A) Negative, because strong interactions create order.
<br>
(B) Zero, because the system reaches a stable equilibrium.
<br>
(C)
 Positive, because mixing two different liquids always increases thermodynamic disorder.
<br>
(D) Depends on the temperature.

**Q8.M15 🟡**
A student mixes $50\text{ mL}$ of liquid X and $50\text{ mL}$ of liquid Y. The beaker becomes noticeably warm. The total volume of the mixture is likely:
<br>
(A) Exactly $100\text{ mL}$
<br>
(B) Slightly more than $100\text{ mL}$
<br>
(C)
 Slightly less than $100\text{ mL}$
<br>
(D) Exactly $50\text{ mL}$

**Q8.M16 🔴 (P-x-y Reading)**
The P-x-y diagram of a binary mixture at 300 K has the following features: P°_A = 350 torr, P°_B = 150 torr. The actual P vs χ_A curve lies above the Raoult line and shows a maximum at χ_A = 0.5 where P = 450 torr. At this maximum, Y_A = 0.5. Which of the following is FALSE?<br>
<br>
(A) The mixture shows positive deviation from Raoult's Law
<br>
(B) The azeotropic composition is χ_A = 0.5
<br>
(C)
 The azeotrope is a maximum boiling azeotrope
<br>
(D) The Raoult-predicted P at χ_A = 0.5 is 250 torr

**Q8.M17 🟡 (Azeotrope Data)**
A maximum boiling azeotrope of A and B has χ_A = 0.6 at its boiling point. P°_A = 800 torr and P°_B = 400 torr at this temperature. The ideal VP at this composition is:
<br>
(A) 640 torr  <br>
(B) 720 torr  <br>
(C)
 480 torr  <br>
(D) 560 torr

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q8.M1 → Answer: <br>
(C)
**
- Ideal solutions have $\Delta H_{mix} = 0$ and $\Delta V_{mix} = 0$.
- Trap: <br>
(A) and <br>
(B) are false because $\Delta S_{mix} > 0$ and $\Delta G_{mix} < 0$ for ALL spontaneous mixing.

**Q8.M2 → Answer: <br>
(C)
**
- Negative deviation means strong A-B bonds are formed, releasing energy. Thus, the process is EXOTHERMIC ($\Delta H_{mix} < 0$).
- Option C says it is endothermic, which is incorrect.

**Q8.M3 → Answer: <br>
(B)**
- The boiling point is higher than both pure components $\rightarrow$ Maximum boiling azeotrope.
- Maximum boiling azeotropes are caused by large negative deviations (lower VP $\rightarrow$ need more heat to reach $1\text{ atm}$).

**Q8.M4 → Answer: <br>
(A)**
- $100 + 50 = 150\text{ mL}$. Actual volume is $152\text{ mL}$.
- Expansion ($\Delta V > 0$) indicates Positive Deviation.
- Positive deviations form Minimum boiling azeotropes.

**Q8.M5 → Answer: <br>
(C)
**
- Unlike pure compounds, the composition of an azeotrope shifts if the external pressure is changed. You can actually "break" an azeotrope by distilling it under vacuum.

**Q8.M6 → Answer: <br>
(C)
**
- Solution 1 (Ethanol + Water): Positive deviation $\rightarrow$ Endothermic $\rightarrow \Delta H_{mix} > 0$.
- Solution 2 (Chloroform + Acetone): Negative deviation $\rightarrow$ Exothermic $\rightarrow \Delta H_{mix} < 0$.

**Q8.M7 → Answer: <br>
(A)**
- Positive deviation means VP is higher than expected. If deviation is large enough, the VP curve creates a local MAXIMUM.
- High VP means it boils easily, so the boiling point curve will have a MINIMUM.

**Q8.M8 → Answer: <br>
(B)**
- Ethyl chloride and ethyl bromide have almost identical structures and polarities.

**Q8.M9 → Answer: <br>
(B)**
- The distillate is a constant-boiling mixture (azeotrope). Since it comes off as vapour, it must be boiling at a lower temperature than the residue.
- Lower boiling point $\rightarrow$ Minimum boiling azeotrope. (If it were a max boiling azeotrope, the azeotrope would stay in the flask as residue while the pure components boiled off first).

**Q8.M10 → Answer: <br>
(B)**
- Positive deviation applies to the total pressure AND individual partial pressures. Both are higher than Raoult's prediction.

**Q8.M11 → Answer: <br>
(C)
**
- $\chi_A = \chi_B = 0.5$.
- $P_A = 200 \times 0.5 = 100$. $P_B = 100 \times 0.5 = 50$.
- $Y_A = 100 / 150 = 0.67$.
- Vapour is richer in A (the more volatile component).

**Q8.M12 → Answer: <br>
(B)**
- Negative deviation means strong A-B intermolecular forces. These forces hold the molecules in the liquid tighter, DECREASING their escaping tendency.

**Q8.M13 → Answer: <br>
(C)
**
- Distilling a 50% mixture will enrich the vapour in ethanol until it hits the azeotropic composition of 95%. Once it hits 95%, the vapour and liquid compositions become identical, and further distillation yields no enrichment.

**Q8.M14 → Answer: <br>
(C)
**
- No matter how strong the interactions or how non-ideal the solution, the process of mixing two separate components ALWAYS increases the number of microstates (disorder). $\Delta S_{mix}$ is ALWAYS positive.

**Q8.M15 → Answer: <br>
(C)
**
- Beaker becomes warm $\rightarrow$ Exothermic $\rightarrow \Delta H < 0 \rightarrow$ Negative deviation.
- Negative deviation implies contraction ($\Delta V < 0$).
- Volume will be less than $100\text{ mL}$.

**Q8.M16 → Answer: <br>
(C)
**
- Actual P curve lies ABOVE Raoult line → Positive deviation ✓
- Maximum in P-x-y at χ_A = 0.5 with Y_A = χ_A → **Minimum boiling azeotrope** (NOT maximum boiling)
- Option C says "maximum boiling azeotrope" → **FALSE** ✓
- Raoult P at χ_A = 0.5: 350×0.5 + 150×0.5 = 175 + 75 = **250 torr** (D is true)

**Q8.M17 → Answer: <br>
(A)**
- χ_A = 0.6, χ_B = 0.4
- P_ideal = 800×0.6 + 400×0.4 = 480 + 160 = **640 torr ✓**
- Actual P < 640 (since it's a max boiling azeotrope → negative deviation → actual < ideal)
</details>

---

## Key Takeaways from Chapter 8

| Type | A-B forces | ΔH | ΔV | VP | P-x-y curve | T-x-y curve | Azeotrope |
|------|-----------|----|----|----|-------------|-------------|----|
| Ideal | = A-A, B-B | 0 | 0 | = Raoult | Straight line | Straight | None |
| Positive deviation | Weaker | > 0 | > 0 | > Raoult | Above ideal (may have max) | Has minimum | Min boiling |
| Negative deviation | Stronger | < 0 | < 0 | < Raoult | Below ideal (may have min) | Has maximum | Max boiling |

> **Key addition:** ΔG_mix < 0 for ALL solutions (ideal or non-ideal). ΔS_mix > 0 always. Only ΔH_mix changes sign.

---

*Next: [Chapter 9 — RLVP & Elevation of Boiling Point →](./09_rlvp_and_boiling_point.md)*
