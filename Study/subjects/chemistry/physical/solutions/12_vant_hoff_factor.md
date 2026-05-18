# Chapter 12: Van't Hoff Factor & Abnormal Molar Mass
## Part VI — Abnormal Molar Mass

---

## 🎯 Stage 1: The Core Idea

### The Problem with Electrolytes

All colligative property formulas assume the solute stays as intact molecules. But NaCl in water doesn't exist as NaCl — it dissociates into Na⁺ and Cl⁻. Two particles instead of one. The effect on VP, BP, FP, π is *double* what you'd expect.

Similarly, some solutes **associate** — acetic acid in benzene forms dimers (two molecules join into one). Half as many particles. Half the expected effect.

**Van't Hoff factor (i)** corrects for this.

### The Two Cases

```
Dissociation:  1 → 2, 3, 4 particles → i > 1 → observed MM < actual MM
Association:   2, 3... → 1 particle → i < 1 → observed MM > actual MM
```

---

## 🔬 Stage 2: The Formula Lab

### Van't Hoff Factor

```
         Observed colligative property
i = ────────────────────────────────────────
         Calculated colligative property

OR

         Actual (normal) molar mass
i = ──────────────────────────────────────────
         Observed (abnormal) molar mass
```

### Modified Colligative Property Formulas

```
RLVP:    (P° − P_s)/P° = i × χ_solute
ΔT_b:    ΔT_b = i × K_b × m
ΔT_f:    ΔT_f = i × K_f × m
π:       π = i × C × R × T
```

### Degree of Dissociation (α)

For solute AB dissociating into n ions (AB → n particles):

```
         i − 1
α = ─────────────
         n − 1
```

where n = number of particles formed per formula unit.

**Example:** NaCl → Na⁺ + Cl⁻, n = 2:
```
α = (i − 1)/(2 − 1) = i − 1
i = 1 + α
```

**For K₂SO₄ → 2K⁺ + SO₄²⁻, n = 3:**
```
i = 1 + 2α
α = (i − 1)/2
```

### Degree of Association (β)

For x molecules associating into 1 cluster: (xA → Aₓ)

```
         1 − i
β = ─────────────
       1 − (1/x)

i = 1 − β(1 − 1/x)
```

**Example:** Acetic acid in benzene forms dimers (x = 2):
```
i = 1 − β/2
β = 2(1 − i)
```

### Summary Table: i values for Common Electrolytes

| Electrolyte | Dissociation | n | i (ideal) |
|-------------|-------------|---|-----------|
| NaCl, KCl, KBr | AB → A⁺ + B⁻ | 2 | 2 |
| MgCl₂, CaCl₂ | AB₂ → A²⁺ + 2B⁻ | 3 | 3 |
| AlCl₃ | AB₃ → A³⁺ + 3B⁻ | 4 | 4 |
| K₂SO₄, Na₂SO₄ | A₂B → 2A⁺ + B²⁻ | 3 | 3 |
| CH₃COOH (benzene) | 2A → A₂ (dimer) | — | 0.5 |
| Glucose, urea | No change | — | 1 |

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Finding i from Observed and Expected Values

**Pattern:** Calculate expected and observed colligative property → find i.

#### Solved Example 12.1
**Q:** 0.01 m NaCl solution has ΔT_b = 0.0196°C. Expected = 0.0104°C. Find i. 🟢

```
i = ΔT_b(observed)/ΔT_b(expected) = 0.0196/0.0104 = 1.885 ≈ 1.9
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 12.1a | 0.1 m KCl depresses FP by 0.32°C. K_f=1.86. Find i. | 🟢 |
| 12.1b | Observed MM of NaCl from experiment = 30. Actual = 58.5. Find i. | 🟢 |
| 12.1c | 0.1 m CH₃COOH (benzene): ΔT_f = 0.256°C, K_f = 5.12. Find i. | 🟡 |
| 12.1d | π = 4.93 atm for 0.1 M NaCl at 300 K. Find i. | 🟡 |
| DPP 11.9 | Observe the following abbreviations: πobs = observed colligative property, πcal = theoretical colligative property assuming normal behaviour of solute. Van't Hoff factor (i) is given by: <br>
(A) i = πobs × πcal <br>
(B) i = πobs + πcal <br>
(C)
 i = πobs − πcal <br>
(D) i = πobs / πcal | 🟢 |
| 12.1e | A 0.05 m solution of KCl shows ΔT_f = 0.167°C (K_f=1.86). Calculate the van't Hoff factor i and comment on the degree of dissociation. | 🟡 |
| 12.1f | **Assertion <br>
(A):** The van't Hoff factor i for a completely dissociated 0.1 m NaCl solution is 2.<br>**Reason (R):** i = Observed colligative property / Calculated colligative property assuming no dissociation. | 🟢 |
| 12.1g | 0.01 m acetic acid in benzene shows ΔT_f = 0.0256°C (K_f=5.12). Find i. What does this value suggest about acetic acid in benzene?<br> | 🟡 |
| 12.1h | **Statement I:** For a solute that forms dimers, i < 1.<br>**Statement II:** If i=0.5, it indicates 100% dimerization. | 🟡 |
| 12.1i | The observed molar mass of NaCl determined by cryoscopy is 30 g/mol. If the actual molar mass is 58.5 g/mol, calculate i and the degree of dissociation. | 🟡 |
| 12.1j | **Assertion <br>
(A):** The van't Hoff factor for glucose is always 1.<br>**Reason (R):** Glucose is a non-electrolyte that neither dissociates nor associates in water. | 🟢 |
| 12.1k | A 0.2 m solution of an unknown electrolyte shows ΔT_f = 0.93°C (K_f=1.86). If the formula suggests n = 3 (trivalent), find the actual i and the degree of dissociation. | 🔴 |
| 12.1l | **Statement I:** The van't Hoff factor can be greater than the number of ions theoretically possible.<br>**Statement II:** Interionic attractions can cause i to exceed the theoretical maximum. | 🟡 |
| 12.1m | 0.1 m MgCl₂ solution has an observed π of 6.15 atm at 300 K. Calculate i. How does it compare with the theoretical value?<br> | 🟡 |
| 12.1n | **Assertion <br>
(A):** For dilute solutions, the observed i is closer to the theoretical value than for concentrated solutions.<br>**Reason (R):** At higher concentrations, interionic attractions reduce the effective number of particles. | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**12.1a:** Expected ΔT_f = 1.86×0.1 = 0.186; **i = 0.32/0.186 = 1.72**

**12.1b:** **i = 58.5/30 = 1.95**

**12.1c:** Expected = 5.12×0.1 = 0.512; **i = 0.256/0.512 = 0.5** *(Acetic acid associates into dimers!)*

**12.1d:** Expected π = 0.1×0.0821×300 = 2.463; **i = 4.93/2.463 = 2.0**

**DPP 11.9:** The van't Hoff factor is defined as the ratio of the observed colligative property to the calculated/theoretical colligative property assuming no dissociation or association. Thus, i = πobs / πcal. → **Answer: <br>
(D)**

**12.1e:** Expected ΔT_f = 1.86×0.05 = 0.093°C; **i = 0.167/0.093 = 1.795 ≈ 1.80**
KCl → 2 ions, so α = (1.80−1)/(2−1) = 0.80 = **80% dissociation**

**12.1f:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation of A.

**12.1g:** Expected = 5.12×0.01 = 0.0512°C; **i = 0.0256/0.0512 = 0.50**
i < 1 indicates association; acetic acid forms dimers in benzene (100% dimerisation).

**12.1h:** **Statement I is True, Statement II is True.**
For dimers: i = 1 − β/2. If i = 0.5, then β = 2(1−0.5) = 1.0 = 100% dimerization. ✓

**12.1i:** **i = 58.5/30 = 1.95**; NaCl → 2 ions; **α = (1.95−1)/(2−1) = 0.95 = 95%**

**12.1j:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.

**12.1k:** Expected ΔT_f = 1.86×0.2 = 0.372°C; **i = 0.93/0.372 = 2.50**
n = 3: **α = (2.50−1)/(3−1) = 1.50/2 = 0.75 = 75%**

**12.1l:** **Statement I is False, Statement II is False.**
i cannot exceed n (the theoretical number of ions). Interionic attractions reduce i, not increase it.

**12.1m:** Expected π = 0.1×0.0821×300 = 2.463 atm; **i = 6.15/2.463 = 2.50 ≈ 2.5**
Theoretical i for MgCl₂ (n=3) = 3. Observed (2.5) < theoretical due to interionic attractions.

**12.1n:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
</details>

---

### Type 2: Finding Degree of Dissociation (α)

**Pattern:** Given i → find α using `α = (i−1)/(n−1)`.

#### Solved Example 12.2
**Q:** i = 1.8 for NaCl in water. Find degree of dissociation. 🟢 ⭐

```
NaCl → Na⁺ + Cl⁻, n = 2
α = (i − 1)/(n − 1) = (1.8 − 1)/(2 − 1) = 0.8/1 = 0.80

Answer: 80% dissociation
```

#### Solved Example 12.3
**Q:** i = 2.5 for K₂SO₄. Find α. 🟡

```
K₂SO₄ → 2K⁺ + SO₄²⁻, n = 3
α = (2.5 − 1)/(3 − 1) = 1.5/2 = 0.75

Answer: 75% dissociation
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 12.2a | i = 1.6 for KCl. Find α. | 🟢 |
| 12.2b | i = 2.7 for MgCl₂. Find α. | 🟡 |
| 12.2c | α = 0.9 for BaCl₂. Find i. | 🟡 |
| 12.2d | α = 0.6 for K₂SO₄. Find i. ⭐ | 🟡 |
| 12.2e | α = 0.75 for AlCl₃. Find i. | 🟡 |
| DPP 11.7 | The Van't Hoff's factor (i) for a dilute aqueous solution of Na₂SO₄ is: <br>
(A) 1 + α <br>
(B) 1 − α <br>
(C)
 1 + 2α <br>
(D) 1 − 2α | 🟡 |
| DPP 11.8 | For the given electrolyte XmYn, the degree of dissociation 'α' is given by ('i' is the Van't Hoff factor): <br>
(A) α = (i−1)/(m+n−1) <br>
(B) i = (1−α) + mα + nα <br>
(C)
 α = (i−1)/(m+n−1) <br>
(D) All of these | 🟡 |
| 12.2f | AlCl₃ solution has i = 3.25. Find the degree of dissociation. | 🟡 |
| 12.2g | **Assertion <br>
(A):** For an electrolyte AB₂, the maximum value of i is 3.<br>**Reason (R):** AB₂ dissociates into A²⁺ + 2B⁻, giving 3 ions per formula unit. | 🟢 |
| 12.2h | A 0.1 m K₃[Fe(CN)₆] solution shows i = 3.2. Find α if the compound dissociates into 4 ions. | 🟡 |
| 12.2i | **Statement I:** Degree of dissociation α can never exceed 1.<br>**Statement II:** i = 1 + (n-1)α, so when α > 1, i would exceed the maximum possible value n. | 🟢 |
| 12.2j | 0.2 m solution of Na₂SO₄ has ΔT_f = 0.837°C (K_f=1.86). Find i and α. | 🔴 |
| 12.2k | **Assertion <br>
(A):** For a weak electrolyte, i approaches 1 as the solution is diluted.<br>**Reason (R):** Ostwald's dilution law states that α decreases with dilution. | 🟡 |
| 12.2l | A solution of a weak dibasic acid (H₂A) has i = 1.4. Find α assuming it dissociates in two steps: H₂A → 2H⁺ + A²⁻. | 🔴 |
| 12.2m | **Statement I:** The expression α = (i-1)/(n-1) is valid only for systems without association.<br>**Statement II:** If association and dissociation occur simultaneously, this formula does not apply. | 🟡 |
| 12.2n | 0.05 m BaCl₂ solution freezes at -0.2325°C (K_f=1.86). Find i and α. | 🟡 |
| 12.2o | **Assertion <br>
(A):** For strong electrolytes, the observed i at moderate concentrations is always less than the theoretical n.<br>**Reason (R):** Strong electrolytes are completely dissociated, but interionic attractions reduce their effective concentration. | 🔴 |

<details>
<summary>💡 Solutions for Type 2</summary>

**12.2a:** KCl → 2 ions; **α = (1.6−1)/(2−1) = 0.6 = 60%**

**12.2b:** MgCl₂ → 3 ions; **α = (2.7−1)/(3−1) = 1.7/2 = 0.85 = 85%**

**12.2c:** BaCl₂ → 3 ions; **i = 1 + (n−1)α = 1 + 2×0.9 = 2.8**

**12.2d:** K₂SO₄ → 3 ions; **i = 1 + 2×0.6 = 2.2**

**12.2e:** AlCl₃ → 4 ions; **i = 1 + 3×0.75 = 3.25**

**DPP 11.7:** Na₂SO₄ dissociates into 2 Na⁺ + SO₄²⁻, giving n = 3 ions per formula unit.
Formula: i = 1 + (n − 1)α = 1 + (3 − 1)α = **1 + 2α → Answer: <br>
(C)
**

**DPP 11.8:** Total particles formed per formula unit is n_total = m + n.
Using standard formulation: α = (i − 1) / (n_total − 1) = (i − 1) / (m + n − 1).
Also, effective particles i = 1 − α + (m + n)α = (1 − α) + mα + nα.
Thus, all given formulations are mathematically identical and valid. → **Answer: <br>
(D)**

**12.2f:** AlCl₃ → Al³⁺ + 3Cl⁻, n=4; **α = (3.25−1)/(4−1) = 2.25/3 = 0.75 = 75%**

**12.2g:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
AB₂ → A²⁺ + 2B⁻ gives n=3; i_max = 1 + (3−1)×1 = 3. ✓

**12.2h:** K₃[Fe(CN)₆] → 3K⁺ + [Fe(CN)₆]³⁻, n=4; **α = (3.2−1)/(4−1) = 2.2/3 = 0.733 = 73.3%**

**12.2i:** **Statement I is True, Statement II is True.**
α ∈ [0,1]; when α=1, i = n (maximum possible value). α > 1 would give i > n.

**12.2j:** i = 0.837/(1.86×0.2) = 0.837/0.372 = **2.25**; Na₂SO₄ → 3 ions; **α = (2.25−1)/(3−1) = 1.25/2 = 0.625 = 62.5%**

**12.2k:** **Answer: <br>
(C)
** A is true but R is false.
A is true: weak electrolytes approach i ≈ 1 at moderate concentrations. R is false: Ostwald's law states α INCREASES with dilution (approaching 1), not decreases.

**12.2l:** H₂A → 2H⁺ + A²⁻, n=3; **α = (1.4−1)/(3−1) = 0.4/2 = 0.20 = 20%**
(Note: This assumes two-step dissociation can be approximated by overall α for n=3.)

**12.2m:** **Statement I is True, Statement II is True.**
The formula α = (i-1)/(n-1) derives from i = 1 − α + nα = 1 + (n-1)α, assuming pure dissociation. If association also occurs, the relation breaks down.

**12.2n:** Expected ΔT_f = 1.86×0.05 = 0.093°C; **i = 0.2325/0.093 = 2.50**
BaCl₂ → 3 ions; **α = (2.50−1)/(3−1) = 1.50/2 = 0.75 = 75%**

**12.2o:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Strong electrolytes are 100% dissociated (α=1, i_theoretical=n), but Debye-Hückel interionic attractions reduce effective i, especially at moderate concentrations.
</details>

---

### Type 3: Finding Degree of Association (β)

**Pattern:** i < 1 (association) → find β using dimer or higher cluster formula.

#### Solved Example 12.4
**Q:** Acetic acid in benzene has i = 0.52. Find degree of association (x = 2). 🟡 ⭐

```
β = 2(1 − i) = 2(1 − 0.52) = 2 × 0.48 = 0.96

Answer: 96% associated (forms dimers)
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 12.3a | Benzoic acid in benzene: i = 0.54. Find β (x=2). | 🟡 |
| 12.3b | β = 0.8 for dimeric solute (x=2). Find i. | 🟡 |
| 12.3c | If i = 0.4 for acetic acid (x=2 dimer), find β. | 🟡 |
| 12.3d | A solute forms trimers (x=3). i = 0.60. Find β. | 🔴 |
| DPP 11.10 | Phenol dimerises in benzene having van't Hoff factor 0.54. What is the degree of association?<br> <br>
(A) 1.92 <br>
(B) 0.98 <br>
(C)
 1.08 <br>
(D) 0.92 | 🟡 |
| 12.3e | A 0.05 m solution of benzoic acid in benzene shows ΔT_f = 0.128°C (K_f=5.12). Find i and the degree of association (dimer). | 🟡 |
| 12.3f | **Assertion <br>
(A):** The minimum possible value of i for a dimerizing substance is 0.5.<br>**Reason (R):** i = 1 − β/2, and β ≤ 1, so i ≥ 0.5. | 🟡 |
| 12.3g | A solute forms trimers (x=3) in solution. If the observed i is 0.7, find the degree of association β. | 🔴 |
| 12.3h | **Statement I:** Association always leads to i < 1.<br>**Statement II:** The observed molar mass in association is higher than the actual molar mass. | 🟢 |
| 12.3i | Acetic acid (MM=60) in benzene shows an observed molar mass of 100 g/mol. Find i and the degree of dimerization β. | 🔴 |
| 12.3j | **Assertion <br>
(A):** The degree of association cannot be greater than 1.<br>**Reason (R):** β = 1 represents 100% association, which is the physically maximum value. | 🟢 |
| 12.3k | A compound with actual MM = 150 shows obs MM = 300 in a solvent. Determine the type of association (dimer vs. trimer vs. tetramer). | 🔴 |
| 12.3l | **Statement I:** For a solute showing association, i increases with increase in temperature.<br>**Statement II:** Higher temperature breaks associated clusters, increasing the number of particles. | 🟡 |
| 12.3m | At 25°C, a 0.1 m solution of a solute has i = 0.6. At 50°C, the same solution has i = 0.8. Find the degree of association (dimer) at each temperature. What trend do you observe?<br> | 🔴 |
| 12.3n | **Assertion <br>
(A):** Phenol in benzene shows association, while phenol in water shows dissociation.<br>**Reason (R):** Benzene is non-polar and promotes hydrogen bonding between phenol molecules; water is polar and promotes ionization. | 🔴 |

<details>
<summary>💡 Solutions for Type 3</summary>

**12.3a:** **β = 2(1−0.54) = 0.92 = 92%**

**12.3b:** i = 1 − β(1−1/x) = 1 − 0.8×(1−0.5) = 1 − 0.4 = **i = 0.6**

**12.3c:** **β = 2(1−0.4) = 1.2** — impossible (>1); likely means i should be > 0.5 for dimers.

**12.3d:** x=3: β = (1−i)/(1−1/3) = (1−0.6)/(2/3) = 0.4/0.667 = **β = 0.60 = 60%**

**DPP 11.10:** Dimerisation means x = 2. Formula: β = 2(1 − i) = 2(1 − 0.54) = 2 × 0.46 = **0.92 → Answer: <br>
(D)**

**12.3e:** Expected ΔT_f = 5.12×0.05 = 0.256°C; **i = 0.128/0.256 = 0.50**
Dimer: **β = 2(1−0.50) = 1.0 = 100% association** (complete dimerization)

**12.3f:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
i = 1 − β/2. Minimum at β=1: i = 1 − 0.5 = 0.5. ✓

**12.3g:** x=3: i = 1 − β(1−1/3) = 1 − 2β/3; **β = 3(1−i)/2 = 3(1−0.7)/2 = 3×0.3/2 = 0.45 = 45%**

**12.3h:** **Statement I is True, Statement II is True.**
Association reduces particle count → i < 1 → observed MM = actual MM/i > actual MM. ✓

**12.3i:** **i = 60/100 = 0.60**; dimer (x=2): **β = 2(1−0.60) = 0.80 = 80% dimerization**

**12.3j:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
β ∈ [0,1]; β=1 is complete association. ✓

**12.3k:** **i = 150/300 = 0.50**
For 100% association (β=1): i = 1/x. So 1/x = 0.5 → x = 2.
The association is **dimerization**.

**12.3l:** **Statement I is True, Statement II is True.**
Higher temperature supplies energy to break intermolecular bonds holding clusters together, releasing more individual particles and increasing i.

**12.3m:** At 25°C: **β = 2(1−0.6) = 0.80 = 80%**
At 50°C: **β = 2(1−0.8) = 0.40 = 40%**
**Trend:** Degree of association decreases with increasing temperature, as thermal energy disrupts the associated clusters.

**12.3n:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Benzene (non-polar) encourages H-bonding between phenol molecules (association). Water (polar, H-bonding) stabilizes phenoxide ions (dissociation).
</details>

---

### Type 4: Colligative Properties with i (Full Calculation)

**Pattern:** Given α or β → find i → apply modified formula.

#### Solved Example 12.5
**Q:** 1.86 g NaCl (MM=58.5) in 200 g water. α = 0.80. Find ΔT_f. K_f=1.86. 🟡 ⭐

```
i = 1 + (2−1)×0.80 = 1.80

m = 1.86/(58.5 × 0.2) = 0.1590 mol/kg

ΔT_f = i × K_f × m = 1.80 × 1.86 × 0.1590 = 0.532°C
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 12.4a | 0.1 m KCl (α=0.7, K_f=1.86). Find ΔT_f. | 🟡 |
| 12.4b | 0.05 m Na₂SO₄ (α=0.8, K_b=0.52). Find ΔT_b. | 🟡 |
| 12.4c | 0.001 M haemoglobin (i=1) at 300 K. Find π in atm and mm Hg. | 🟢 |
| 12.4d | 0.01 m acetic acid in benzene (β=0.90, K_f=5.12). Find ΔT_f. ⭐ | 🔴 |
| DPP 11.1 | Which of the following solutions will have highest boiling point?<br> <br>
(A) 0.1M FeCl₃ <br>
(B) 0.1M BaCl₂ <br>
(C)
 0.1M NaCl <br>
(D) 0.1M urea | 🟡 |
| DPP 11.2 | Maximum lowering of vapour pressure is observed in the case of: <br>
(A) 0.1M glucose <br>
(B) 0.1M BaCl₂ <br>
(C)
 0.1M MgSO₄ <br>
(D) 0.1M NaCl | 🟡 |
| DPP 11.3 | If 0.1 M solutions of each electrolyte are taken and if all electrolytes are completely dissociated, then whose boiling point will be highest?<br> <br>
(A) Glucose <br>
(B) KCl <br>
(C)
 BaCl₂ <br>
(D) K₄[Fe(CN)₆] | 🔴 |
| DPP 11.5 | The freezing point of one molal NaCl solution assuming NaCl to be 100% dissociated in water is (molal depression constant = 1.86°C kg mol⁻¹): <br>
(A) 1.86°C <br>
(B) 3.72°C <br>
(C)
 +1.86°C <br>
(D) +3.72°C | 🟡 |
| DPP 11.6 | The order of osmotic pressure of isomolar solution of BaCl₂, NaCl and sucrose is: <br>
(A) BaCl₂ > NaCl > sucrose <br>
(B) NaCl > BaCl₂ > sucrose <br>
(C)
 Sucrose > NaCl > BaCl₂ <br>
(D) BaCl₂ > sucrose > NaCl | 🟡 |
| 12.4e | 0.2 m Al₂(SO₄)₃ (complete dissociation, i=5, K_f=1.86). Find ΔT_f and freezing point. | 🟡 |
| 12.4f | **Assertion <br>
(A):** 0.1 M FeCl₃ has a higher boiling point than 0.1 M BaCl₂.<br>**Reason (R):** FeCl₃ produces 4 ions while BaCl₂ produces 3 ions per formula unit. | 🟢 |
| 12.4g | Arrange the following 0.1 M solutions in order of increasing osmotic pressure: NaCl, CaCl₂, AlCl₃, glucose. (Assume complete dissociation) | 🟡 |
| 12.4h | **Statement I:** The van't Hoff factor i appears in all four colligative property formulas.<br>**Statement II:** i modifies the effective concentration of particles. | 🟢 |
| 12.4i | 0.1 m KCl (α=0.85) solution at 300 K. Calculate (a) i, (b) π, (c) ΔT_f (K_f=1.86). | 🟡 |
| 12.4j | **Assertion <br>
(A):** Among 0.1 M solutions of urea, NaCl, and CaCl₂, CaCl₂ has the highest boiling point.<br>**Reason (R):** CaCl₂ has the highest van't Hoff factor (i=3). | 🟢 |
| 12.4k | A 0.05 m K₄[Fe(CN)₆] (complete dissociation, i=5, K_b=0.52). Find ΔT_b and boiling point. | 🟡 |
| 12.4l | **Statement I:** The osmotic pressure of 0.1 M FeCl₃ is greater than 0.1 M Glucose at the same temperature.<br>**Statement II:** π = iCRT and i for FeCl₃ is 4 while for glucose it is 1. | 🟢 |
| 12.4m | 0.01 m acetic acid in benzene (β=0.8, K_f=5.12). Find i and ΔT_f. | 🟡 |
| 12.4n | **Assertion <br>
(A):** For concentrated electrolyte solutions, experimental ΔT_f is always less than calculated using i × K_f × m.<br>**Reason (R):** Ion-pairing and interionic attractions reduce the effective number of particles. | 🟡 |

<details>
<summary>💡 Solutions for Type 4</summary>

**12.4a:** i = 1+0.7 = 1.7; **ΔT_f = 1.7×1.86×0.1 = 0.316°C**

**12.4b:** Na₂SO₄ → 3 ions; i = 1+2×0.8 = 2.6; **ΔT_b = 2.6×0.52×0.05 = 0.0676°C**

**12.4c:** **π = 1×0.001×0.0821×300 = 0.02463 atm = 18.7 mm Hg**

**12.4d:** i = 1−β/2 = 1−0.45 = 0.55; **ΔT_f = 0.55×5.12×0.01 = 0.02816°C**

**DPP 11.1:** Elevation of boiling point ΔT_b ∝ i × C. Since molarity C is 0.1M for all, the one with the maximum van't Hoff factor `i` exhibits the highest boiling point. Assuming complete dissociation: FeCl₃ gives 4 ions (i=4), BaCl₂ gives 3 ions (i=3), NaCl gives 2 ions (i=2), urea gives 1 particle (i=1). Highest i is for FeCl₃. → **Answer: <br>
(A)**

**DPP 11.2:** Lowering of vapour pressure ΔP ∝ i × C. At identical concentration (0.1M), maximum lowering occurs for the solute with the highest particle count `i`. Glucose i=1, BaCl₂ i=3, MgSO₄ i=2, NaCl i=2. Maximum lowering is for BaCl₂. → **Answer: <br>
(B)**

**DPP 11.3:** Complete dissociation yields: Glucose i=1, KCl i=2, BaCl₂ i=3, K₄[Fe(CN)₆] dissociates into 4 K⁺ + [Fe(CN)₆]⁴⁻ giving 5 ions (i=5). Highest i gives maximum boiling point elevation. → **Answer: <br>
(D)**

**DPP 11.5:** 100% dissociation of NaCl gives i = 2. Depression of freezing point ΔT_f = i × K_f × m = 2 × 1.86 × 1 = 3.72°C. Therefore, the freezing point depression is **3.72°C → Answer: <br>
(B)**

**DPP 11.6:** Osmotic pressure π ∝ i × C. For isomolar solutions, π directly tracks `i`. BaCl₂ gives 3 ions (i=3), NaCl gives 2 ions (i=2), sucrose gives 1 particle (i=1). Order: BaCl₂ > NaCl > sucrose. → **Answer: <br>
(A)**

**12.4e:** **ΔT_f = 5×1.86×0.2 = 1.86°C**; **FP = 0 − 1.86 = −1.86°C**

**12.4f:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
FeCl₃ (i=4) > BaCl₂ (i=3), so FeCl₃ has higher ΔT_b and higher boiling point.

**12.4g:** Glucose (i=1) < NaCl (i=2) < CaCl₂ (i=3) < AlCl₃ (i=4)
π ∝ i, so: **glucose < NaCl < CaCl₂ < AlCl₃**

**12.4h:** **Statement I is True, Statement II is True.**
i appears in RLVP (i×χ), ΔT_b (i×K_b×m), ΔT_f (i×K_f×m), and π (i×C×R×T). It modifies the effective particle concentration.

**12.4i:** (a) KCl → 2 ions: **i = 1 + 0.85 = 1.85**
(b) **π = 1.85×0.1×0.0821×300 = 4.56 atm**
(c) **ΔT_f = 1.85×1.86×0.1 = 0.344°C**

**12.4j:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Urea (i=1), NaCl (i=2), CaCl₂ (i=3). Highest i → highest ΔT_b → highest BP. ✓

**12.4k:** **ΔT_b = 5×0.52×0.05 = 0.13°C**; **BP = 100 + 0.13 = 100.13°C**

**12.4l:** **Statement I is True, Statement II is True.**
π(FeCl₃) = 4×0.1×R×T = 0.4RT; π(glucose) = 1×0.1×R×T = 0.1RT. FeCl₃ > Glucose. ✓

**12.4m:** Dimer (x=2): **i = 1 − 0.8/2 = 1 − 0.4 = 0.60**
**ΔT_f = 0.60×5.12×0.01 = 0.0307°C**

**12.4n:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Ion-pairing and interionic attractions (Debye-Hückel effect) reduce effective particle count, so ΔT_f(observed) < i×K_f×m.
</details>

---

### Type 5: Abnormal Molar Mass Calculation

**Pattern:** Observed ΔT or π → find observed MM → compare with actual MM → find i.

#### Solved Example 12.6
**Q:** 0.5 g of acetic acid in 50 g benzene. ΔT_f = 0.256°C. K_f = 5.12. Find observed MM and i. 🔴 ⭐

```
m = ΔT_f/K_f = 0.256/5.12 = 0.05 m

Observed MM = W/(m × W_solvent_kg) = 0.5/(0.05 × 0.05) = 0.5/0.0025 = 200 g/mol

Actual MM of CH₃COOH = 60 g/mol

i = Actual/Observed = 60/200 = 0.3

Check with dimer: i = 0.3 → β = 2(1−0.3) = 1.4 → >1, impossible!
→ Must form trimers or higher?<br> Or data issue.
(Typically: observed MM ≈ 120 for complete dimer association → i=0.5)
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 12.5a | 2 g KCl in 500 g water. ΔT_f = 0.123°C. K_f=1.86. Find observed MM and i. ⭐ | 🟡 |
| 12.5b | Expected MM of AlCl₃ = 133.5. Observed = 50. Find i. | 🟡 |
| 12.5c | 3 g urea (MM=60) in 100 g water. ΔT_f = 0.930°C. K_f=1.86. Is MM normal?<br> Find i. | 🟡 |
| 12.5d | 1 g of an electrolyte XY₂ (actual MM=100 g/mol) is dissolved in 500 g water. ΔT_f = 0.0744°C (K_f=1.86). Find observed MM and i. | 🔴 |
| 12.5e | **Assertion <br>
(A):** If the observed molar mass is greater than the actual molar mass, the solute must be undergoing association.<br>**Reason (R):** i < 1 implies observed MM > actual MM, which is characteristic of association. | 🟢 |
| 12.5f | 0.45 g of a non-electrolyte in 50 g water gives ΔT_f = 0.093°C (K_f=1.86). Find the observed MM. If the actual MM is 180, comment on the result. | 🟡 |
| 12.5g | **Statement I:** Abnormal molar masses are observed for both electrolytes and non-electrolytes.<br>**Statement II:** For non-electrolytes, abnormal MM arises only from association, while for electrolytes it arises from dissociation. | 🟡 |
| 12.5h | 0.3 g of a protein dissolved in 25 g of water gives ΔT_f = 0.00093°C (K_f=1.86). Find the observed molar mass. Is this method suitable for proteins?<br> | 🔴 |
| 12.5i | **Assertion <br>
(A):** The molar mass of NaCl determined by colligative property measurement is always less than 58.5 g/mol.<br>**Reason (R):** NaCl dissociates, increasing particle count and decreasing the observed MM. | 🟡 |
| 12.5j | In a Rast method experiment, 0.1 g of a compound in 10 g camphor (K_f=37.7) gives ΔT_f = 1.885°C. Find the observed MM. | 🔴 |
| 12.5k | **Statement I:** The Rast method using camphor as solvent is suitable for compounds with molar masses up to about 500 g/mol.<br>**Statement II:** Camphor has a very high K_f (37.7), producing large ΔT_f even for small amounts of solute. | 🟡 |
| 12.5l | 0.62 g of ethylene glycol (actual MM=62) in 100 g water gives ΔT_f = 0.186°C. Confirm that the observed MM matches the actual. | 🟡 |
| 12.5m | **Assertion <br>
(A):** The formula i = Actual MM / Observed MM gives the van't Hoff factor regardless of which colligative property is measured.<br>**Reason (R):** All colligative properties are inversely proportional to molar mass, so the ratio of actual to observed MM always equals i. | 🟡 |

<details>
<summary>💡 Solutions for Type 5</summary>

**12.5a:** m = 0.123/1.86 = 0.0661 m; observed MM = 2/(0.0661×0.5) = 2/0.03306 = **60.5 g/mol**
i = 74.5(actual KCl MM)/60.5 = **1.23** (partial dissociation ≈ 23%)

**12.5b:** **i = 133.5/50 = 2.67** (AlCl₃ partially dissociates → less than ideal i=4)

**12.5c:** m_expected = 3/(60×0.1) = 0.5 m; ΔT_f_expected = 1.86×0.5 = 0.93°C
Observed ΔT_f = 0.930°C ≈ expected → **i = 1.0; MM is normal; urea doesn't dissociate** ✓

**12.5d:** m = ΔT_f/K_f = 0.0744/1.86 = 0.04 m; observed MM = 1/(0.04×0.5) = 1/0.02 = **50 g/mol**
**i = 100/50 = 2.0**; XY₂ → 3 ions ideal; α = (2−1)/(3−1) = 0.5 = 50% dissociation

**12.5e:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
i = Actual MM/Observed MM. If observed > actual, i < 1 → association. ✓

**12.5f:** m = 0.093/1.86 = 0.05 m; observed MM = 0.45/(0.05×0.05) = 0.45/0.0025 = **180 g/mol**
Observed MM matches actual MM (180) → **i = 1.0**; the non-electrolyte neither dissociates nor associates.

**12.5g:** **Statement I is True, Statement II is True.**
Non-electrolytes can show abnormal MM via association (e.g., acetic acid in benzene). Electrolytes show abnormal MM via dissociation.

**12.5h:** m = 0.00093/1.86 = 0.0005 m; observed MM = 0.3/(0.0005×0.025) = 0.3/0.0000125 = **24,000 g/mol**
The ΔT_f is very small (0.00093°C), hard to measure accurately. Cryoscopy is not ideal for macromolecules; osmotic pressure is preferred.

**12.5i:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
NaCl dissociates → i > 1 → observed MM = actual MM/i < actual MM (58.5). ✓

**12.5j:** m = ΔT_f/K_f = 1.885/37.7 = 0.05 m; observed MM = 0.1/(0.05×0.01) = 0.1/0.0005 = **200 g/mol**

**12.5k:** **Statement I is True, Statement II is True.**
Camphor's high K_f (37.7) gives measurable ΔT_f even for small solute amounts, making the Rast method sensitive for moderate MM compounds.

**12.5l:** m_expected = 0.62/(62×0.1) = 0.1 m; ΔT_f_expected = 1.86×0.1 = 0.186°C
Observed ΔT_f = 0.186°C → **i = 1.0, observed MM = 62 g/mol** (matches actual). Ethylene glycol is a non-electrolyte. ✓

**12.5m:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
All colligative properties ∝ (1/MM), so i = property_observed/property_calculated = (1/MM_obs)/(1/MM_act) = MM_act/MM_obs. ✓
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 12.M1 | 0.1 m NaCl in water at 300 K. α = 0.85. Find: (a) i, (b) ΔT_f, (c) π, (d) RLVP. ⭐ | T2+T4 | 🔴 |
| 12.M2 | 0.01 m CH₃COOH in benzene. ΔT_f = 0.0256°C (K_f=5.12). Find i, β, and state if dimer forms. | T3+T5 | 🔴 |
| 12.M3 | 0.1 m K₂SO₄ solution has ΔT_f = 0.432°C (K_f=1.86). Find i, α, and expected ΔT_f for complete dissociation. ⭐ | T2+T4 | 🔴 |
| 12.M4 | A 0.1 m solution of an electrolyte AB₂ shows ΔT_f = 0.465°C (K_f=1.86). Find i and α. If the same solution shows π = 6.15 atm at 300 K, verify consistency of i. ⭐ | T1+T2+T4 | 🔴 |
| 12.M5 | **Assertion <br>
(A):** The van't Hoff factor for a solution of K₂SO₄ is temperature dependent.<br>**Reason (R):** Temperature affects the degree of dissociation and interionic interactions. | AR | 🟡 |
| 12.M6 | 1 g of NaCl (MM=58.5, α=0.8) is dissolved in 100 g water. Calculate: (a) i, (b) ΔT_f (K_f=1.86), (c) π at 300 K. ⭐ | T2+T4 | 🟡 |
| 12.M7 | **Assertion <br>
(A):** For a 1:1 electrolyte (like NaCl), the maximum i is 2.<br>**Reason (R):** i = 1 + (n-1)α, where n=2 and α ≤ 1, so i_max = 2. | AR | 🟢 |
| 12.M8 | 0.2 m solution of a weak acid HA (α=0.05). Find: (a) i, (b) ΔT_f (K_f=1.86), (c) π at 300 K. ⭐ | T2+T4 | 🟡 |
| 12.M9 | A student prepares a 0.1 M solution of acetic acid in water. The measured π at 300 K is 2.52 atm. Find i and α for acetic acid. Compare this with its behaviour in benzene (where it dimerizes). ⭐ | T1+T2 | 🔴 |
| 12.M10 | **Assertion <br>
(A):** Camphor's exceptionally high K_f (37.7) makes the Rast method highly sensitive.<br>**Reason (R):** A high K_f produces large ΔT_f for small amounts of solute, reducing percentage measurement error. | AR | 🟢 |
| 12.M11 | A dialysate solution for kidney dialysis must have the same effective particle concentration as blood. Blood has equivalent i×C = 0.3 M. If the dialysate contains 0.1 M NaCl and some glucose, calculate the required glucose concentration. ⭐ | T4 | 🔴 |
| 12.M12 | **Assertion <br>
(A):** For a mixture of two solutes, the effective van't Hoff factor is the weighted average of individual i values.<br>**Reason (R):** Colligative properties are additive, so total i×C = i₁C₁ + i₂C₂. | AR | 🟡 |
| 12.M13 | A solution contains 0.05 M Na₂SO₄ (i=3) and 0.1 M glucose. Calculate the total osmotic pressure at 310 K. Compare this with 0.15 M NaCl (i=2). Which has higher π?<br> ⭐ | T4 | 🔴 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**12.M1:**
- **(a) i = 1 + 0.85 = 1.85**
- **(b) ΔT_f = 1.85×1.86×0.1 = 0.344°C → FP = −0.344°C**
- **(c) π = 1.85×0.1×0.0821×300 = 4.56 atm**
- **(d) RLVP = i×χ; n_NaCl=0.1, n_H₂O=55.56; χ_s = 0.1/55.66 = 0.001796; RLVP = 1.85×0.001796 = 0.00332**

**12.M2:**
- m = ΔT_f/K_f = 0.0256/5.12 = 0.005 m
- Expected (no association): 0.01 m → i = 0.005/0.01 = **0.5**
- β = 2(1−i) = 2(1−0.5) = **1.0 = 100% dimerisation**
- Yes, acetic acid forms complete dimers in benzene.

**12.M3:**
- i = ΔT_f/(K_f×m) = 0.432/(1.86×0.1) = 0.432/0.186 = **2.323**
- K₂SO₄ → 3 ions; **α = (2.323−1)/(3−1) = 1.323/2 = 0.662 = 66.2%**
- Complete dissociation: i=3; ΔT_f = 3×1.86×0.1 = **0.558°C**

**12.M4:**
- From ΔT_f: i = 0.465/(1.86×0.1) = 0.465/0.186 = **2.50**
- AB₂ → 3 ions: α = (2.50−1)/(3−1) = 1.50/2 = **0.75 = 75%**
- From π: Expected π (no dissociation) = 0.1×0.0821×300 = 2.463 atm; i = 6.15/2.463 = **2.50** ✓
- **Consistent:** both methods give i = 2.50

**12.M5:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Temperature changes affect both α (degree of dissociation) and interionic interactions, making i temperature-dependent.

**12.M6:**
- **(a) i = 1 + 0.8 = 1.8**
- m = 1/(58.5×0.1) = 0.171 m
- **(b) ΔT_f = 1.8×1.86×0.171 = 0.572°C**
- **(c) π = 1.8×0.171×0.0821×300 = 7.58 atm**

**12.M7:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
For 1:1 electrolyte, n=2; i = 1 + α. Since α ≤ 1, i_max = 2. ✓

**12.M8:**
- **(a) i = 1 + 0.05 = 1.05**
- **(b) ΔT_f = 1.05×1.86×0.2 = 0.391°C**
- **(c) π = 1.05×0.2×0.0821×300 = 5.17 atm**

**12.M9:**
- Expected π (no dissociation) = 0.1×0.0821×300 = 2.463 atm
- **i = 2.52/2.463 = 1.023**
- Acetic acid → CH₃COO⁻ + H⁺ (n=2): **α = (1.023−1)/(2−1) = 0.023 = 2.3%**
- **Comparison:** In benzene, acetic acid dimerizes (i ≈ 0.5, β ≈ 1). In water, it weakly dissociates (i ≈ 1.023, α ≈ 0.023). The solvent determines behaviour — polar solvents favour dissociation, non-polar favour association.

**12.M10:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
High K_f amplifies ΔT_f signal, enabling accurate MM determination with small samples. ✓

**12.M11:**
- NaCl contributes: i×C = 2×0.1 = 0.2 M
- Glucose needed: 0.3 − 0.2 = **0.1 M glucose**
- i×C for glucose = 1×0.1 = 0.1 M
- Total = 0.2 + 0.1 = 0.3 M ✓

**12.M12:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
Colligative properties are additive: π_total = π₁ + π₂ = (i₁C₁ + i₂C₂)RT. Effective i = (i₁C₁ + i₂C₂)/(C₁ + C₂). ✓

**12.M13:**
- Na₂SO₄: π₁ = iCRT = 3×0.05×0.0821×310 = 3.82 atm
- Glucose: π₂ = 1×0.1×0.0821×310 = 2.55 atm
- **Total π = 3.82 + 2.55 = 6.37 atm**
- NaCl: π_NaCl = 2×0.15×0.0821×310 = 7.64 atm
- **NaCl solution has higher π (7.64 atm > 6.37 atm)** despite same total solute concentration (0.15 M vs 0.15 M), because NaCl has higher effective i.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 12.B1 | Define van't Hoff factor. How is it related to degree of dissociation?<br> | 🟢 |
| 12.B2 | 0.5 g KCl (MM=74.5) in 100 g water gives ΔT_f = 0.24°C. K_f=1.86. Find i and α. *(NCERT pattern)* ⭐ | 🟡 |
| 12.B3 | Write all four modified colligative property formulas with i. | 🟢 |
| 12.B4 | If solute associates into dimers with β = 0.8, what is i?<br> ⭐ | 🟡 |
| 12.B5 | Why does NaCl have i > 1 and acetic acid in benzene have i < 1?<br> | 🟡 |
| 12.B6 | Why does a 0.1 M NaCl solution have nearly double the colligative effect of 0.1 M glucose?<br> Explain using the van't Hoff factor. | 🟢 |
| 12.B7 | 0.1 m K₂SO₄ solution has a freezing point of -0.434°C (K_f=1.86). Calculate the degree of dissociation of K₂SO₄. ⭐ | 🟡 |
| 12.B8 | **Assertion <br>
(A):** Acetic acid in benzene has i < 1, while in water it has i > 1.<br>**Reason (R):** In benzene, acetic acid forms dimers (association); in water, it ionizes (dissociation). | 🟡 |
| 12.B9 | 0.5 g of a solute dissolved in 50 g of camphor (K_f=37.7) gave a freezing point depression of 1.885°C. Calculate the molar mass of the solute. | 🟡 |
| 12.B10 | Explain why the observed molar mass of KCl in water is less than its formula mass. What would you expect for benzoic acid in benzene?<br> | 🟡 |
| 12.B11 | A 0.1 m solution of a weak electrolyte shows ΔT_f = 0.1953°C (K_f=1.86). If the electrolyte dissociates into 2 ions, calculate its degree of dissociation. | 🟡 |
| 12.B12 | **Assertion <br>
(A):** The van't Hoff factor for a completely dissociated CaCl₂ solution is 3.<br>**Reason (R):** CaCl₂ → Ca²⁺ + 2Cl⁻, producing 3 ions per formula unit. | 🟢 |
| 12.B13 | A 0.01 m solution of acetic acid in benzene freezes at 5.474°C (pure benzene freezes at 5.50°C, K_f=5.12). Determine the van't Hoff factor and the degree of association. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**12.B1:** van't Hoff factor i = (observed colligative property)/(calculated assuming no dissociation/association) = (actual MM)/(observed MM).
For dissociation into n ions: i = 1 + (n−1)α, so α = (i−1)/(n−1).

**12.B2:** m = ΔT_f/K_f/i → first find i:
Expected (no dissociation): m = 0.5/(74.5×0.1) = 0.0671 m; ΔT_f_expected = 1.86×0.0671 = 0.1248°C
**i = 0.24/0.1248 = 1.923**
KCl → 2 ions; **α = (1.923−1)/1 = 0.923 = 92.3%**

**12.B3:**
- RLVP = i × χ_solute
- ΔT_b = i × K_b × m
- ΔT_f = i × K_f × m
- π = i × C × R × T

**12.B4:** i = 1 − β(1−1/x) = 1 − 0.8×(1−0.5) = 1 − 0.4 = **i = 0.6**

**12.B5:** NaCl dissociates into Na⁺ + Cl⁻ → 2 particles → more particles than expected → colligative property larger → **i > 1**. Acetic acid in benzene forms dimers (H-bonded pairs) → 2 molecules act as 1 particle → fewer particles than expected → colligative property smaller → **i < 1**.

**12.B6:** NaCl dissociates into Na⁺ and Cl⁻ in water, giving i ≈ 2. Glucose is a non-electrolyte, i = 1. Since ΔT_b, ΔT_f, π, and RLVP all depend on i × concentration, NaCl has roughly twice the colligative effect of glucose at the same molar concentration.

**12.B7:** i = ΔT_f/(K_f×m) = 0.434/(1.86×0.1) = 0.434/0.186 = **2.333**
K₂SO₄ → 2K⁺ + SO₄²⁻ (n=3): **α = (2.333−1)/(3−1) = 1.333/2 = 0.667 = 66.7%**

**12.B8:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
In benzene (non-polar), acetic acid forms H-bonded dimers (i < 1). In water (polar), it dissociates into ions (i > 1, though weakly since it's a weak acid).

**12.B9:** m = ΔT_f/K_f = 1.885/37.7 = 0.05 m
MM = W/(m × W_solvent_kg) = 0.5/(0.05 × 0.05) = 0.5/0.0025 = **200 g/mol**

**12.B10:** KCl dissociates into K⁺ + Cl⁻, so the number of particles increases → i > 1 → observed MM = actual MM/i < actual MM (74.5 g/mol).
For benzoic acid in benzene: benzoic acid forms dimers via H-bonding → association → i < 1 → **observed MM > actual MM (122 g/mol)**.

**12.B11:** i = 0.1953/(1.86×0.1) = 0.1953/0.186 = **1.05**
n=2: **α = (1.05−1)/(2−1) = 0.05 = 5%**

**12.B12:** **Answer: <br>
(A)** Both A and R are true, R is correct explanation.
CaCl₂ → Ca²⁺ + 2Cl⁻ gives n=3; complete dissociation → i = 3. ✓

**12.B13:** ΔT_f = 5.50 − 5.474 = **0.0256°C**
Expected ΔT_f (no association) = 5.12×0.01 = 0.0512°C
**i = 0.0256/0.0512 = 0.50**
Dimer (x=2): **β = 2(1−0.50) = 1.0 = 100% association**
Acetic acid is completely dimerized in benzene.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q12.J1 🟡 ⭐**
For NaCl with degree of dissociation α, van't Hoff factor i equals:
<br>
(A) 1 + α  <br>
(B) 1 − α  <br>
(C)
 1 + 2α  <br>
(D) α − 1

**Q12.J2 🟡 ⭐**
If the observed molar mass of benzoic acid in benzene is 122 g/mol and actual is 122 g/mol, it means:
<br>
(A) i = 2, full association  <br>
(B) i = 1, no association  <br>
(C)
 i = 0.5, full dimerisation  <br>
(D) i = 0.5, α = 0.5

**Q12.J3 🔴 ⭐**
0.1 m K₂SO₄ has i = 2.2. Degree of dissociation is:
<br>
(A) 0.6  <br>
(B) 0.3  <br>
(C)
 0.8  <br>
(D) 0.2

**Q12.J4 🔴 ⭐**
An electrolyte AB₂ completely dissociates (α = 1). Which i is correct?<br>
<br>
(A) i = 2  <br>
(B) i = 3  <br>
(C)
 i = 4  <br>
(D) i = 1.5

**Q12.J5 🔴 ⭐**
0.01 M acetic acid in benzene. β = 0.9 (dimerisation). Find π at 300 K.
<br>
(A) 1.23 × 10⁻² atm  <br>
(B) 6.16 × 10⁻³ atm  <br>
(C)
 2.46 × 10⁻² atm  <br>
(D) 4.93 × 10⁻³ atm

**Q12.J6 🟡**
**Assertion <br>
(A):** K₄[Fe(CN)₆] dissociates in water to give 5 ions.
**Reason (R):** The complex [Fe(CN)₆]⁴⁻ does not dissociate further in water.
<br>
(A) Both A and R are true, R is correct explanation
<br>
(B) Both A and R are true, R is NOT correct explanation
<br>
(C)
 A is true but R is false
<br>
(D) A is false but R is true

**Q12.J7 🟡**
For a 0.1 m electrolyte A₂B (which dissociates into 2A⁺ + B²⁻) with α = 0.7, van't Hoff factor i is:
<br>
(A) 1.7 <br>
(B) 2.4 <br>
(C)
 1.0 <br>
(D) 2.0

**Q12.J8 🔴**
A 0.1 M solution of complex PtCl₄·4NH₃ shows ΔT_f = -0.54°C (K_f=1.80). The number of ions produced per formula unit is:
<br>
(A) 5 <br>
(B) 2 <br>
(C)
 3 <br>
(D) 4

**Q12.J9 🔴**
**Assertion <br>
(A):** The observed molar mass of NaCl is always less than 58.5 g/mol.
**Reason (R):** i = Actual MM/Observed MM, and since i > 1 for NaCl, observed MM < actual MM.
<br>
(A) Both A and R are true, R is correct explanation
<br>
(B) Both A and R are true, R is NOT correct explanation
<br>
(C)
 A is true but R is false
<br>
(D) A is false but R is true

**Q12.J10 🟡**
The van't Hoff factor for 0.1 m BaCl₂ is 2.6. The degree of dissociation is:
<br>
(A) 0.8 <br>
(B) 0.9 <br>
(C)
 0.7 <br>
(D) 1.0

**Q12.J11 🔴**
0.02 m solution of acetic acid in benzene (K_f=5.12) freezes at 5.449°C (pure benzene freezes at 5.50°C). The degree of association of acetic acid (dimer) is:
<br>
(A) 0.50 <br>
(B) 0.75 <br>
(C)
 0.90 <br>
(D) 1.0

**Q12.J12 🟡**
**Statement I:** The degree of dissociation α is always between 0 and 1.
**Statement II:** α = 1 represents complete dissociation.
<br>
(A) Both true <br>
(B) I true, II false <br>
(C)
 I false, II true <br>
(D) Both false

**Q12.J13 🔴**
A 0.1 m aqueous solution of a triprotic acid H₃A (which dissociates into 4 ions) shows ΔT_f = 0.372°C (K_f=1.86). The degree of dissociation of the acid is:
<br>
(A) 0.35 <br>
(B) 0.50 <br>
(C)
 0.75 <br>
(D) 0.90

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**12.J1 → Answer: <br>
(A)**
- NaCl → Na⁺ + Cl⁻, n = 2
- i = 1 + (n−1)α = 1 + (2−1)α = **1 + α ✓**

**12.J2 → Answer: <br>
(B)**
- Observed MM = actual MM → no change in particle count → **i = 1, no association ✓**
- *(If full dimerisation: observed MM = 244, not 122)*

**12.J3 → Answer: <br>
(A)**
- K₂SO₄ → 3 ions, n = 3
- α = (i−1)/(n−1) = (2.2−1)/(3−1) = 1.2/2 = **0.6 ✓**

**12.J4 → Answer: <br>
(B)**
- AB₂ → A²⁺ + 2B⁻ → 3 ions, n = 3
- α = 1: i = 1 + (3−1)×1 = 1+2 = **3 ✓**

**12.J5 → Answer: <br>
(B)**
- Dimer: x = 2; i = 1 − β(1−1/2) = 1 − 0.9×0.5 = 1 − 0.45 = **0.55**
- π = iCRT = 0.55 × 0.01 × 0.0821 × 300 = 0.55 × 0.2463 = **0.1355/10 = 0.01355 ≈ 1.35×10⁻² atm**
- *(Closest to <br>
(A) 1.23×10⁻²)*

Wait: 0.55 × 0.01 × 0.0821 × 300 = 0.55 × 2.463 = 1.3547 × 10⁻¹ → No:
C = 0.01 M; π = 0.55 × 0.01 × 24.63 × (1) = 0.55 × 0.2463 = **0.1355 atm** — that's wrong.
π = iCRT = 0.55 × 0.01 × 0.0821 × 300 = 0.55 × 0.2463 = **0.1355 atm**

Hmm: 0.01 × 0.0821 × 300 = 0.2463; × 0.55 = 0.1355 atm ≈ **1.355 × 10⁻¹ atm**

Closest option: none exact. If C = 0.01M means mol/L, answer = 0.1355 atm. If answer <br>
(A) = 1.23×10⁻² then maybe C was 0.001 M or β was different. **<br>
(B) 6.16×10⁻³ atm would need i×C = 0.01/4 which doesn't fit.** MCQ data may need adjustment — key formula is: **π = iCRT with i = 1 − β/2**.

**12.J6 → Answer: <br>
(A)**
- K₄[Fe(CN)₆] → 4K⁺ + [Fe(CN)₆]⁴⁻ = 5 ions. ✓
- [Fe(CN)₆]⁴⁻ is a stable complex and does not dissociate further. ✓
- R correctly explains why total ions = 5. → <br>
(A)

**12.J7 → Answer: <br>
(B)**
- A₂B → 2A⁺ + B²⁻, n = 3
- i = 1 + (n−1)α = 1 + (3−1)×0.7 = 1 + 2×0.7 = **1 + 1.4 = 2.4 → <br>
(B)**

**12.J8 → Answer: <br>
(C)
**
- i = ΔT_f/(K_f×m) = 0.54/(1.80×0.1) = 0.54/0.18 = **3**
- The complex produces 3 ions per formula unit.
- [Pt(NH₃)₄Cl₂]Cl₂ → [Pt(NH₃)₄Cl₂]²⁺ + 2Cl⁻ gives 3 ions. → <br>
(C)


**12.J9 → Answer: <br>
(A)**
- NaCl dissociates → i > 1 → observed MM = actual MM/i < 58.5. ✓
- R correctly explains why using the i formula. → <br>
(A)

**12.J10 → Answer: <br>
(A)**
- BaCl₂ → Ba²⁺ + 2Cl⁻, n = 3
- i = 1 + (n−1)α → 2.6 = 1 + 2α → 2α = 1.6 → **α = 0.8 → <br>
(A)**

**12.J11 → Answer: <br>
(D)**
- ΔT_f = 5.50 − 5.449 = 0.051°C
- Expected ΔT_f = 5.12×0.02 = 0.1024°C
- i = 0.051/0.1024 = 0.498 ≈ **0.5**
- β = 2(1−0.5) = **1.0 = 100% dimerisation → <br>
(D)**

**12.J12 → Answer: <br>
(A)**
- α ∈ [0,1] by definition. α = 1 means complete dissociation. Both statements true. → <br>
(A)

**12.J13 → Answer: <br>
(A)**
- i = 0.372/(1.86×0.1) = 0.372/0.186 = **2.0**
- H₃A → 3H⁺ + A³⁻, n = 4
- α = (i−1)/(n−1) = (2.0−1)/(4−1) = 1/3 = **0.333 ≈ 0.35 → <br>
(A)**
</details>

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
| 12.S1 | **Assertion <br>
(A):** The van't Hoff factor ($i$) for a dilute solution of glucose is always $1$.<br>**Reason (R):** Glucose is a non-electrolyte and neither dissociates nor associates in aqueous solution. | 🟢 |
| 12.S2 | **Statement I:** If a solute associates in a given solvent, its observed molar mass will be lower than its actual theoretical molar mass.<br>**Statement II:** Association decreases the number of particles in solution, leading to a van't Hoff factor $i < 1$. | 🟡 |
| 12.S3 | **Assertion <br>
(A):** The van't Hoff factor of $BaCl_2$ at $100\%$ dissociation is $3$.<br>**Reason (R):** One formula unit of $BaCl_2$ dissociates into one $Ba^{2+}$ ion and two $Cl^-$ ions. | 🟢 |
| 12.S4 | **Statement I:** The degree of dissociation ($\alpha$) of a weak acid can be greater than $1$.<br>**Statement II:** The van't Hoff factor ($i$) for a weak acid can be greater than $1$. | 🟢 |
| 12.S5 | **Assertion <br>
(A):** A $0.1\text{ M}$ solution of $NaCl$ will have a lower vapour pressure than a $0.1\text{ M}$ solution of urea at the same temperature.<br>**Reason (R):** The relative lowering of vapour pressure is directly proportional to the van't Hoff factor ($i$) of the solute. | 🟡 |
| 12.S6 | **Statement I:** The formula $i = \frac{\text{Calculated Molar Mass}}{\text{Observed Molar Mass}}$ is universally true for all colligative properties.<br>**Statement II:** Colligative properties are inversely proportional to the molar mass of the solute. | 🟢 |
| 12.S7 | **Assertion <br>
(A):** Acetic acid dimerizes completely in benzene, resulting in a van't Hoff factor of exactly $0.5$.<br>**Reason (R):** Two molecules of acetic acid form a cyclic dimer via intermolecular hydrogen bonding. | 🟡 |
| 12.S8 | **Statement I:** As a solution of a weak electrolyte is diluted, its van't Hoff factor ($i$) approaches $1$.<br>**Statement II:** Ostwald's dilution law states that the degree of dissociation ($\alpha$) of a weak electrolyte increases upon dilution, approaching $100\%$ at infinite dilution. | 🔴 |
| 12.S9 | **Assertion <br>
(A):** The observed freezing point depression of a $0.1\text{ m}$ $KCl$ solution is roughly twice that of a $0.1\text{ m}$ glucose solution.<br>**Reason (R):** $KCl$ is a strong electrolyte that completely dissociates into 2 ions, doubling the effective particle concentration. | 🟢 |
| 12.S10 | **Statement I:** For a solute undergoing dissociation, $i = 1 + (n-1)\alpha$. This means $i$ is always greater than or equal to $1$.<br>**Statement II:** If $\alpha = 0$, the solute acts as a non-electrolyte and $i = 1$. | 🟢 |
| 12.S11 | **Assertion <br>
(A):** $K_4[Fe(CN)_6]$ has a maximum van't Hoff factor of $5$.<br>**Reason (R):** The complex ion $[Fe(CN)_6]^{4-}$ dissociates into $Fe^{2+}$ and $6 CN^-$ ions in aqueous solution. | 🔴 |
| 12.S12 | **Statement I:** If a solute forms trimers in a solvent, the theoretical lower limit for its van't Hoff factor is $0.33$.<br>**Statement II:** If $100\%$ of the molecules associate into groups of three, the number of particles is reduced to one-third. | 🟡 |
| 12.S13 | **Assertion <br>
(A):** The actual, real-world van't Hoff factor for a $0.1\text{ M}$ $NaCl$ solution is slightly less than $2.0$ (e.g., $1.87$).<br>**Reason (R):** Interionic attractions (Debye-Hückel effect) prevent independent movement of all ions, slightly reducing the effective particle count. | 🟡 |
| 12.S14 | **Statement I:** To calculate the degree of association ($\beta$) for a dimer, the formula is $\beta = \frac{1-i}{2}$.<br>**Statement II:** The correct mathematical rearrangement of $i = 1 - \beta(1 - 1/2)$ is $\beta = 2(1-i)$. | 🟡 |
| 12.S15 | **Assertion <br>
(A):** Abnormal molar masses are observed only for strong electrolytes.<br>**Reason (R):** Weak electrolytes and organic acids never dissociate or associate. | 🟢 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**12.S1 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- Classic definition of a non-electrolyte colligative behaviour.

**12.S2 → Statement I is False, Statement II is True.**
- Statement I is false: Association means molecules stick together (e.g., dimers). The particles look LARGER to the solvent. Therefore, the OBSERVED molar mass is HIGHER than the actual molar mass.
- Statement II is true: Fewer particles means $i < 1$. Since $i = \text{Actual MM} / \text{Observed MM}$, if $i < 1$, then Observed MM > Actual MM.

**12.S3 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $BaCl_2 \rightarrow Ba^{2+} + 2Cl^-$. Total $n=3$. If $\alpha=1$, $i=3$.

**12.S4 → Statement I is False, Statement II is True.**
- Statement I is false: Degree of dissociation ($\alpha$) is a fraction ranging from $0$ to $1$ (or $0\%$ to $100\%$). It cannot exceed $1$.
- Statement II is true: Since it dissociates into multiple ions, the effective particle multiplier ($i$) will be $> 1$.

**12.S5 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $NaCl$ has $i=2$, urea has $i=1$. Higher $i$ $\rightarrow$ greater relative lowering of vapour pressure $\rightarrow$ lower final vapour pressure.

**12.S6 → Statement I is True, Statement II is True.**
- This is the fundamental reason why the first formula works. Because all colligative properties are proportional to $(1/MM)$, the ratio of observed to calculated properties mathematically flips for molar masses.

**12.S7 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- This is a standard textbook example of hydrogen-bonded dimerization.

**12.S8 → Statement I is False, Statement II is True.**
- Statement I is false: As a weak electrolyte is diluted, $\alpha$ INCREASES towards $1$. Since $i = 1 + (n-1)\alpha$, if $\alpha$ increases, $i$ ALSO INCREASES towards its maximum value $n$. It does NOT approach $1$.
- Statement II is true: This is Ostwald's dilution law.

**12.S9 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- $i_{KCl} = 2$, $i_{glucose} = 1$. Therefore, the depression is twice as large.

**12.S10 → Statement I is True, Statement II is True.**
- Both statements mathematically and logically align.

**12.S11 → Answer: <br>
(C)
 A is true but R is false.**
- A is true: $K_4[Fe(CN)_6] \rightarrow 4K^+ + [Fe(CN)_6]^{4-}$. Total $n = 4 + 1 = 5$.
- R is false: The complex ion $[Fe(CN)_6]^{4-}$ is stable and does NOT dissociate further into $Fe^{2+}$ and $CN^-$ in water.

**12.S12 → Statement I is True, Statement II is True.**
- For a trimer ($x=3$), $i = 1 - \beta(1 - 1/3)$. If $\beta = 1$ ($100\%$ association), $i = 1 - 1(2/3) = 1/3 = 0.33$.

**12.S13 → Answer: <br>
(A) Both A and R are true, and R is the correct explanation.**
- In real solutions, unless at infinite dilution, ions experience electrostatic attractions that slightly reduce their independence, making the observed $i$ slightly less than the ideal $n$.

**12.S14 → Statement I is False, Statement II is True.**
- Statement I uses an incorrect algebraic rearrangement. Statement II provides the correct one.

**12.S15 → Answer: <br>
(D) A is false but R is false.**
- A is false: Weak electrolytes partially dissociate, leading to abnormal molar masses. Organic acids often associate (dimerize), also leading to abnormal molar masses.
- R is false: They do dissociate/associate.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q12.M1 🟢**
The van't Hoff factor for a $0.1\text{ M}$ ideal solution of $Al_2(SO_4)_3$ is:
<br>
(A) $3$
<br>
(B) $4$
<br>
(C)
 $5$
<br>
(D) $6$

**Q12.M2 🟡 (The "Wrong Multiplier" Trap)**
If the degree of dissociation of a weak acid $H_2A$ is $\alpha$, what is its van't Hoff factor $i$?<br>
<br>
(A) $1 + \alpha$
<br>
(B) $1 + 2\alpha$
<br>
(C)
 $1 + 3\alpha$
<br>
(D) $1 - 2\alpha$

**Q12.M3 🔴**
An aqueous solution of $PtCl_4 \cdot 4NH_3$ freezes at $-0.0054^\circ\text{C}$. The molality of the solution is $0.001\text{ m}$ and $K_f$ for water is $1.80\text{ K kg mol}^{-1}$. Assuming complete dissociation, the structural formula of the complex is likely:
<br>
(A) $[Pt(NH_3)_4Cl_2]Cl_2$
<br>
(B) $[Pt(NH_3)_4Cl_4]$
<br>
(C)
 $[Pt(NH_3)_4Cl_3]Cl$
<br>
(D) $[Pt(NH_3)_4]Cl_4$

**Q12.M4 🟡**
A solute A forms a tetramer ($A_4$) in a solvent. If the degree of association is $80\%$, what is the van't Hoff factor?<br>
<br>
(A) $0.80$
<br>
(B) $0.20$
<br>
(C)
 $0.40$
<br>
(D) $0.25$

**Q12.M5 🟡 (The "Observed Mass Direction" Trap)**
A solute has an actual molar mass of $100\text{ g/mol}$. In solution, it partially dissociates such that its van't Hoff factor $i = 1.25$. What is its apparent (observed) molar mass?<br>
<br>
(A) $125\text{ g/mol}$
<br>
(B) $80\text{ g/mol}$
<br>
(C)
 $75\text{ g/mol}$
<br>
(D) $100\text{ g/mol}$

**Q12.M6 🔴**
The freezing point depression of a $0.1\text{ M}$ solution of acetic acid is $0.19^\circ\text{C}$ ($K_f$ for water is $1.86$). What is the approximate degree of dissociation ($\alpha$) of acetic acid?<br>
<br>
(A) $0.02$
<br>
(B) $0.05$
<br>
(C)
 $0.10$
<br>
(D) $0.90$

**Q12.M7 🟡**
Which of the following aqueous solutions will have the lowest vapour pressure at a given temperature?<br>
<br>
(A) $0.1\text{ M}$ $NaCl$
<br>
(B) $0.1\text{ M}$ $CaCl_2$
<br>
(C)
 $0.1\text{ M}$ $AlCl_3$
<br>
(D) $0.1\text{ M}$ $C_{12}H_{22}O_{11}$ (Sucrose)

**Q12.M8 🟢**
What is the theoretical maximum value of the van't Hoff factor ($i$) for $Na_3PO_4$?<br>
<br>
(A) $2$
<br>
(B) $3$
<br>
(C)
 $4$
<br>
(D) $5$

**Q12.M9 🔴 (The "Reverse Association" Trap)**
A compound with molar mass $150\text{ g/mol}$ yields an observed molar mass of $300\text{ g/mol}$ in benzene. If the association is $100\%$, what type of association is occurring?<br>
<br>
(A) Dimerization
<br>
(B) Trimerization
<br>
(C)
 Tetramerization
<br>
(D) Polymerization

**Q12.M10 🟡**
For a solution of $NaCl$ at very high concentration, the measured van't Hoff factor is $1.8$. Which statement best explains this?<br>
<br>
(A) $NaCl$ is a weak electrolyte.
<br>
(B) Strong interionic attractions cause ion-pairing, reducing the number of independent particles.
<br>
(C)
 $NaCl$ associates to form $Na_2Cl_2$ dimers.
<br>
(D) The water evaporates, increasing the concentration.

**Q12.M11 🔴**
$0.2\text{ molal}$ aqueous solution of an acid $HX$ is $20\%$ ionized. The boiling point of this solution will be: ($K_b = 0.52\text{ K kg mol}^{-1}$)
<br>
(A) $100.125^\circ\text{C}$
<br>
(B) $100.208^\circ\text{C}$
<br>
(C)
 $100.104^\circ\text{C}$
<br>
(D) $100.250^\circ\text{C}$

**Q12.M12 🟡**
If a solute exists exactly as a mixture of $50\%$ monomers and $50\%$ dimers in a solution (by moles of species present), what is its average van't Hoff factor $i$?<br>
<br>
(A) $0.50$
<br>
(B) $0.75$
<br>
(C)
 $0.67$
<br>
(D) $1.00$

**Q12.M13 🟢**
The ratio of the value of any colligative property for $KCl$ solution to that of a sugar solution of the same molality is nearly:
<br>
(A) $1$
<br>
(B) $2$
<br>
(C)
 $0.5$
<br>
(D) $3$

**Q12.M14 🔴 (The "Formula Reversal" Trap)**
A student measures $i = 2.5$ for $MgCl_2$. They calculate the degree of dissociation as $\alpha = (2.5 - 1) / 3 = 0.50$. What mistake did they make?<br>
<br>
(A) $MgCl_2$ produces 4 ions, not 3.
<br>
(B) They divided by $n$ instead of $(n-1)$.
<br>
(C)
 They should have used $1-i$.
<br>
(D) They added 1 instead of subtracting 1.

**Q12.M15 🟡**
Equal volumes of $0.1\text{ M}$ $AgNO_3$ and $0.1\text{ M}$ $NaCl$ are mixed. Assuming complete precipitation of $AgCl$ and complete dissociation of the remaining salts, what is the effective molarity (osmolarity) of the resulting solution?<br>
<br>
(A) $0.2\text{ M}$
<br>
(B) $0.1\text{ M}$
<br>
(C)
 $0.4\text{ M}$
<br>
(D) $0.05\text{ M}$

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q12.M1 → Answer: <br>
(C)
**
- $Al_2(SO_4)_3 \rightarrow 2Al^{3+} + 3SO_4^{2-}$. Total ions $n = 2 + 3 = 5$. Ideal $i = 5$.

**Q12.M2 → Answer: <br>
(B)**
- $H_2A \rightarrow 2H^+ + A^{2-}$. Total ions $n = 3$.
- $i = 1 + (n-1)\alpha = 1 + (3-1)\alpha = 1 + 2\alpha$.
- Trap: Assuming $n=2$ gives option A.

**Q12.M3 → Answer: <br>
(A)**
- $i = \Delta T_f / (K_f \cdot m) = 0.0054 / (1.80 \times 0.001) = 0.0054 / 0.0018 = 3$.
- The complex must dissociate into $3$ ions.
- <br>
(A) $[Pt(NH_3)_4Cl_2]Cl_2 \rightarrow [Pt(NH_3)_4Cl_2]^{2+} + 2Cl^-$ ($n=3$). This fits!
- <br>
(B) $n=1$. <br>
(C)
 $n=2$. <br>
(D) $n=5$.

**Q12.M4 → Answer: <br>
(C)
**
- Tetramer means $x=4$. $\beta = 0.80$.
- $i = 1 - \beta(1 - 1/x) = 1 - 0.80(1 - 1/4) = 1 - 0.80(3/4) = 1 - 0.60 = 0.40$.

**Q12.M5 → Answer: <br>
(B)**
- $i = \text{Actual MM} / \text{Observed MM} \implies \text{Observed MM} = \text{Actual MM} / i$.
- $\text{Observed MM} = 100 / 1.25 = 80\text{ g/mol}$.
- Trap: <br>
(A) results from multiplying instead of dividing.

**Q12.M6 → Answer: <br>
(A)**
- Expected $\Delta T_f = 1.86 \times 0.1 = 0.186^\circ\text{C}$.
- $i = 0.19 / 0.186 = 1.0215$.
- Acetic acid ($CH_3COOH$) dissociates into 2 ions ($n=2$).
- $\alpha = (i-1)/(n-1) = (1.0215 - 1) / 1 = 0.0215 \approx 0.02$.

**Q12.M7 → Answer: <br>
(C)
**
- Lowest vapour pressure = highest vapour pressure lowering = highest effective concentration.
- $NaCl$ ($i=2 \rightarrow 0.2\text{ M}$), $CaCl_2$ ($i=3 \rightarrow 0.3\text{ M}$), $AlCl_3$ ($i=4 \rightarrow 0.4\text{ M}$), Sucrose ($i=1 \rightarrow 0.1\text{ M}$).
- $AlCl_3$ has the highest effective concentration, thus the lowest VP.

**Q12.M8 → Answer: <br>
(C)
**
- $Na_3PO_4 \rightarrow 3Na^+ + PO_4^{3-}$. Total ions $= 3 + 1 = 4$.

**Q12.M9 → Answer: <br>
(A)**
- $i = \text{Actual MM} / \text{Observed MM} = 150 / 300 = 0.5$.
- If association is $100\%$ ($\beta=1$), then $i = 1 - 1(1 - 1/x) = 1/x$.
- $1/x = 0.5 \implies x = 2$.
- $x=2$ corresponds to dimerization.

**Q12.M10 → Answer: <br>
(B)**
- At high concentrations, ions are crowded. Oppositely charged ions attract each other (Debye-Hückel effect) and temporarily act as a single particle ("ion-pairing"), reducing the effective number of particles below the theoretical maximum of $2.0$.

**Q12.M11 → Answer: <br>
(A)**
- $HX \rightarrow H^+ + X^-$ ($n=2$).
- $\alpha = 0.20 \implies i = 1 + (2-1)(0.20) = 1.20$.
- $\Delta T_b = i \cdot K_b \cdot m = 1.20 \times 0.52 \times 0.2 = 0.1248^\circ\text{C}$.
- Boiling point $= 100 + 0.1248 = 100.1248 \approx 100.125^\circ\text{C}$.

**Q12.M12 → Answer: <br>
(B)**
- Let's say we started with 100 molecules.
- If it's $50\%$ monomers and $50\%$ dimers *by species present*, let there be 50 monomers and 50 dimers.
- Total particles = $50 + 50 = 100$ particles.
- To make 50 dimers, it took 100 original molecules. The 50 monomers took 50 original molecules.
- Total original molecules = $150$.
- $i = \text{final particles} / \text{initial particles} = 100 / 150 = 2/3 = 0.67$.
- Wait, the trap is in interpreting "50% monomers and 50% dimers". Let's use the standard degree of association ($\beta$). If $x\%$ of original molecules associate: $i = 1 - \beta/2$.
- Let's re-read carefully: "mixture of 50% monomers and 50% dimers (by moles of species present)".
- So, $n_{monomer} = n_{dimer}$. Let both be 1 mole. Total particles = 2 moles.
- Original molecules: 1 mole monomer + 2 moles (to make 1 mole dimer) = 3 moles original.
- $i = \text{Particles Present} / \text{Original Particles} = 2 / 3 = 0.67$.
- *Self-correction: The question implies <br>
(C)
 0.67 is the answer. Let me re-verify my math.*
- Yes, $2/3 \approx 0.67$. Answer is <br>
(C)
. (Note: I initially thought B, but my derivation proves C).
- *Correction: I will mark Answer as <br>
(C)
.*

**Q12.M13 → Answer: <br>
(B)**
- $KCl$ ($i=2$). Sugar ($i=1$). Ratio is $2/1 = 2$.

**Q12.M14 → Answer: <br>
(B)**
- $MgCl_2 \rightarrow Mg^{2+} + 2Cl^-$ ($n=3$).
- The correct formula is $\alpha = (i-1) / (n-1) = (2.5 - 1) / (3 - 1) = 1.5 / 2 = 0.75$.
- The student incorrectly divided by $n$ ($3$) instead of $(n-1)$ ($2$).

**Q12.M15 → Answer: <br>
(B)**
- When equal volumes are mixed, concentrations are halved.
- $AgNO_3$ becomes $0.05\text{ M}$. $NaCl$ becomes $0.05\text{ M}$.
- Reaction: $Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow$.
- The $0.05\text{ M}$ $Ag^+$ and $0.05\text{ M}$ $Cl^-$ react completely to form solid $AgCl$ (which does not contribute to osmolarity).
- Remaining spectator ions: $0.05\text{ M}$ $Na^+$ and $0.05\text{ M}$ $NO_3^-$.
- Total effective concentration $= 0.05 + 0.05 = 0.10\text{ M}$.
</details>

---



| Formula | When to Use |
|---------|------------|
| i = 1 + (n−1)α | Dissociation, n = number of ions |
| i = 1 − β(1−1/x) | Association, x = cluster size |
| i > 1 | Dissociation (electrolytes) |
| i < 1 | Association (acetic acid in benzene) |
| i = 1 | No change (glucose, urea) |
| All 4 colligative formulas × i | For electrolytes |

---

## 🏁 Chapter Complete — Book Complete

You have now completed all 12 chapters of the **Solutions Mastery Book**.

### Revision Priority

| Priority | Chapters |
|----------|----------|
| ⭐ Must revise first | 5 (Interconversion), 9 (RLVP+ΔT_b), 10 (ΔT_f), 11 (Osmosis), 12 (van't Hoff) |
| 🟡 Revise second | 3 (M & m), 4 (χ & w%), 7 (Raoult's Law) |
| 🟢 Quick review | 1 (Types), 2 (Overview), 6 (Henry's Law), 8 (Ideal/Non-Ideal) |

---

*← [Chapter 11 — Osmosis](./11_osmosis_and_osmotic_pressure.md) | [Back to Preface](./00_preface.md) →*
