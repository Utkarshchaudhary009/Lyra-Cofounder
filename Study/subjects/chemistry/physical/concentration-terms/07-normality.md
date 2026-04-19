# Chapter 7: Normality (N) — The Equivalent Approach
## Part II: Enter the Mole

---

## 🎯 Stage 1: The Core Idea

### What is Normality?

Normality counts **gram equivalents** of solute per litre of solution, instead of moles.

> **Analogy:** Imagine you're at a potluck. Molarity counts "how many dishes each person brought." Normality counts "how many servings each person contributed." One person might bring a huge dish (= many servings from one dish), while another brings a small plate. Normality cares about the actual reactive capacity.

### What is an "Equivalent"?

An equivalent is the amount of a substance that reacts with or supplies **one mole of H⁺ or OH⁻** (for acid-base), or **one mole of electrons** (for redox).

| Context | 1 Equivalent = |
|---------|----------------|
| Acid | Amount that provides 1 mol H⁺ |
| Base | Amount that provides 1 mol OH⁻ |
| Redox | Amount that gains or loses 1 mol electrons |

### The Key Relationship

```
N = n-factor × M

where n-factor (also called valence factor or equivalence factor)
depends on the reaction.
```

> **Why normality exists:** In titrations, the equivalence point is when equivalents of acid = equivalents of base. Using normality makes this: N₁V₁ = N₂V₂. Clean. Simple. No stoichiometric coefficients needed.

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
       Gram equivalents of solute        mass of solute
N = ──────────────────────────────── = ─────────────────────────
       Volume of solution (L)          Eq. wt × V(L)
```

### Equivalent Weight

```
                    Molar mass
Equivalent weight = ──────────────
                     n-factor
```

### n-factor Rules

#### For Acids: n-factor = number of replaceable H⁺ ions

| Acid | Formula | n-factor | Equivalent weight |
|------|---------|----------|-------------------|
| HCl | HCl | 1 | 36.5/1 = 36.5 |
| H₂SO₄ | H₂SO₄ | 2 | 98/2 = 49 |
| H₃PO₄ | H₃PO₄ | 3* | 98/3 = 32.67 |
| CH₃COOH | CH₃COOH | 1 | 60/1 = 60 |

*H₃PO₄ can have n = 1, 2, or 3 depending on the specific reaction.*

#### For Bases: n-factor = number of replaceable OH⁻ ions

| Base | Formula | n-factor | Equivalent weight |
|------|---------|----------|-------------------|
| NaOH | NaOH | 1 | 40/1 = 40 |
| Ca(OH)₂ | Ca(OH)₂ | 2 | 74/2 = 37 |
| Al(OH)₃ | Al(OH)₃ | 3 | 78/3 = 26 |

#### For Redox Agents: n-factor = change in oxidation state per formula unit

| Substance | Reaction Context | n-factor |
|-----------|-----------------|----------|
| KMnO₄ | Acidic medium (Mn⁷⁺ → Mn²⁺) | 5 |
| KMnO₄ | Neutral medium (Mn⁷⁺ → Mn⁴⁺) | 3 |
| KMnO₄ | Basic medium (Mn⁷⁺ → Mn⁶⁺) | 1 |
| K₂Cr₂O₇ | Acidic medium (each Cr⁶⁺ → Cr³⁺, 2 Cr per formula) | 6 |
| FeSO₄ | Fe²⁺ → Fe³⁺ | 1 |
| Na₂C₂O₄ | C₂O₄²⁻ → 2CO₂ (each C goes from +3 to +4) | 2 |
| H₂O₂ | As oxidant: O⁻¹ → O²⁻ | 2 |
| H₂O₂ | As reductant: O⁻¹ → O⁰ | 2 |

> **⚠️ Critical Warning:** The n-factor of KMnO₄ changes with the medium! Always check whether the reaction is in acidic, neutral, or basic conditions.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given mass, equivalent weight, volume → find N

**The Pattern:** Straightforward substitution into N = mass / (Eq. wt × V).

#### Solved Example 7.1
**Q:** 4.9 g of H₂SO₄ is dissolved to make 500 mL of solution. Find the normality. (M = 98, n = 2) 🟢

**Solution:**
```
Step 1: Find equivalent weight
    Eq. wt = M/n = 98/2 = 49 g/eq

Step 2: Find gram equivalents
    eq = mass/Eq.wt = 4.9/49 = 0.1 eq

Step 3: Normality
    N = eq/V(L) = 0.1/0.5 = 0.2 N

Answer: 0.2 N
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.1a"></span>7.1a | 7.3 g of HCl in 250 mL of solution. Find N. (M=36.5, n=1) | 🟢 |
| <span id="q-7.1b"></span>7.1b | 5.3 g of Na₂CO₃ in 500 mL. n = 2 (reacts with 2H⁺). Find N. (M=106) | 🟡 |
| <span id="q-7.1c"></span>7.1c | 3.16 g of KMnO₄ in 1 L (acidic medium). Find N. (M=158, n=5) | 🟡 |

<details>
<summary>View Answers</summary>

**7.1a**: 0.8 N
**7.1b**: Answer not found.
**7.1c**: Answer not found.

</details>


---

### Type 2: M to N Conversion Using n-factor ⭐

**The Pattern:** The simplest and most important normality calculation. N = n × M.

#### Solved Example 7.2
**Q:** Find the normality of: (a) 1 M HCl (b) 1 M H₂SO₄ (c) 1 M H₃PO₄ (fully neutralized) 🟢

**Solution:**
```
(a) HCl: n-factor = 1 (one H⁺)
    N = 1 × 1 = 1 N

(b) H₂SO₄: n-factor = 2 (two H⁺)
    N = 2 × 1 = 2 N

(c) H₃PO₄: n-factor = 3 (three H⁺, full neutralization)
    N = 3 × 1 = 3 N

Answer: (a) 1N  (b) 2N  (c) 3N
```

> **Key insight:** 1M H₂SO₄ is 2N because each molecule provides TWO H⁺ ions. The normality is always ≥ molarity (since n-factor ≥ 1).

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.2a"></span>7.2a | Find N of: 0.5 M NaOH, 0.5 M Ca(OH)₂, 0.5 M Al(OH)₃ | 🟢 |
| <span id="q-7.2b"></span>7.2b | 2 M KMnO₄ in acidic medium. Find N. ⭐ | 🟡 |
| <span id="q-7.2c"></span>7.2c | 0.1 M K₂Cr₂O₇ in acidic medium. Find N. ⭐ | 🟡 |
| <span id="q-7.2d"></span>7.2d | Is it possible for N < M? Why or why not? | 🟡 |

<details>
<summary>View Answers</summary>

**7.2a**: 0.5N, 1N, 1.5N
**7.2b**: N = 10 × 0.02 = 0.2 N (wait: N=5×2=10N? No: 0.02M × 5 = 0.1N)
**7.2c**: Answer not found.
**7.2d**: Answer not found.

</details>


---

### Type 3: Equivalent Weight Calculation

**The Pattern:** Finding the equivalent weight for acids, bases, and salts.

#### Solved Example 7.3
**Q:** Find the equivalent weight of: (a) NaOH (b) Ca(OH)₂ (c) KMnO₄ in acidic medium (d) K₂Cr₂O₇ in acidic medium. 🟡

**Solution:**
```
(a) NaOH, M = 40, n = 1
    Eq.wt = 40/1 = 40

(b) Ca(OH)₂, M = 74, n = 2
    Eq.wt = 74/2 = 37

(c) KMnO₄ (acidic), M = 158, n = 5
    Eq.wt = 158/5 = 31.6

(d) K₂Cr₂O₇ (acidic), M = 294, n = 6
    Eq.wt = 294/6 = 49
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.3a"></span>7.3a | Eq.wt of H₃PO₄ when (a) all 3 H⁺ replaced (b) only 1 H⁺ replaced (c) only 2 H⁺ replaced. | 🟡 |
| <span id="q-7.3b"></span>7.3b | Eq.wt of FeSO₄ (Fe²⁺ → Fe³⁺) and Na₂C₂O₄ (C₂O₄²⁻ → 2CO₂). (M_FeSO₄ = 152, M_Na₂C₂O₄ = 134) ⭐ | 🟡 |
| <span id="q-7.3c"></span>7.3c | Why does KMnO₄ have different equivalent weights in acidic vs. basic media? | 🟡 |

<details>
<summary>View Answers</summary>

**7.3a**: Answer not found.
**7.3b**: Answer not found.
**7.3c**: Answer not found.

</details>


---

### Type 4: N₁V₁ = N₂V₂ for Dilution

**The Pattern:** Same as M₁V₁ = M₂V₂, but using normality.

#### Solved Example 7.4
**Q:** 50 mL of 2 N H₂SO₄ is diluted to 500 mL. Find the new normality. 🟢

**Solution:**
```
    N₁V₁ = N₂V₂
    2 × 50 = N₂ × 500
    N₂ = 100/500 = 0.2 N

Answer: 0.2 N
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.4a"></span>7.4a | Dilute 25 mL of 4 N NaOH to 200 mL. Find N₂. | 🟢 |
| <span id="q-7.4b"></span>7.4b | You need 1 L of 0.1 N HCl. You have 6 N HCl. How much do you need? | 🟡 |

<details>
<summary>View Answers</summary>

**7.4a**: Answer not found.
**7.4b**: Answer not found.

</details>


---

### Type 5: Titration — N₁V₁ = N₂V₂ at Equivalence Point ⭐⭐

**The Pattern:** At the equivalence point of a titration, milliequivalents of acid = milliequivalents of base.

#### The Golden Rule of Titration

```
At equivalence point:
    N₁V₁ = N₂V₂
    (for acid)  (for base)

OR equivalently:
    meq of acid = meq of base
    (where meq = N × V_mL)
```

> **Why this is powerful:** You don't need to know the balanced equation! Just equate equivalents.

#### Solved Example 7.5
**Q:** 25 mL of H₂SO₄ of unknown concentration is neutralized by 50 mL of 0.1 N NaOH. Find the normality and molarity of H₂SO₄. 🟡 ⭐

**Solution:**
```
Step 1: At equivalence point
    N_acid × V_acid = N_base × V_base
    N × 25 = 0.1 × 50
    N = 5/25 = 0.2 N

Step 2: Convert N to M
    N = n × M → M = N/n = 0.2/2 = 0.1 M

Answer: N_H₂SO₄ = 0.2 N, M_H₂SO₄ = 0.1 M
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.5a"></span>7.5a | 20 mL of 0.5 N HCl neutralises X mL of 0.2 N NaOH. Find X. ⭐ | 🟡 |
| <span id="q-7.5b"></span>7.5b | 25 mL of 0.1 M H₂SO₄ requires how many mL of 0.1 M NaOH? (Careful — convert to N first!) ⭐⭐ | 🟡 |
| <span id="q-7.5c"></span>7.5c | 10 mL of H₃PO₄ (all 3H⁺ react) is titrated with 30 mL of 0.1 N NaOH. Find the molarity of H₃PO₄. | 🔴 |
| <span id="q-7.5d"></span>7.5d | 25 mL of a monobasic acid (n=1) requires 20 mL of 0.25 N KOH. Find N and M of the acid. | 🟡 |

<details>
<summary>View Answers</summary>

**7.5a**: V = 50 mL *(Key Step: N₁V₁=N₂V₂: 0.5×20=0.2×X → X=50)*
**7.5b**: 50 mL *(Key Step: H₂SO₄: N=0.2; NaOH: N=0.1; 0.2×25=0.1×V → V=50)*
**7.5c**: Answer not found.
**7.5d**: Answer not found.

</details>


---

### Type 6: Back Titration Problems ⭐⭐

**The Pattern:** Excess reagent is added → titrate the leftover → find the original unknown.

#### Solved Example 7.6
**Q:** 0.5 g of an impure CaCO₃ sample is dissolved in 50 mL of 0.5 N HCl (excess). The excess HCl requires 25 mL of 0.2 N NaOH for neutralisation. Find the % purity of CaCO₃. (Eq.wt of CaCO₃ = 100/2 = 50) 🔴 ⭐⭐

**Solution:**
```
Step 1: Total meq of HCl taken
    meq_HCl = 0.5 × 50 = 25 meq

Step 2: meq of excess HCl (neutralised by NaOH)
    meq_excess = 0.2 × 25 = 5 meq

Step 3: meq of HCl used to react with CaCO₃
    meq_used = 25 - 5 = 20 meq

Step 4: meq of CaCO₃ = meq of HCl used = 20 meq
    mass of CaCO₃ = meq × Eq.wt / 1000 = 20 × 50 / 1000 = 1 g

Wait — that gives 1 g of CaCO₃, but the sample was only 0.5 g!
Let me recheck... The meq should give mass in grams:
    
    Actually: mass = gram equivalents × Eq.wt
    gram equivalents = 20/1000 = 0.02 eq
    mass = 0.02 × 50 = 1 g

This can't be right — sample is only 0.5 g. Let me recheck the problem.

Corrected problem: 50 mL of 0.1 N HCl instead.

Step 1: meq_HCl = 0.1 × 50 = 5 meq
Step 2: meq_excess = 0.2 × 25 = 5 meq

Still doesn't work — all HCl is excess. Let me use:

Corrected: 0.5 g sample + 50 mL of 0.5 N HCl. Excess HCl needs 10 mL of 0.2 N NaOH.

Step 1: meq_HCl(total) = 0.5 × 50 = 25 meq
Step 2: meq_excess = 0.2 × 10 = 2 meq
Step 3: meq_used = 25 - 2 = 23 meq
Step 4: mass CaCO₃ = 23 × 50/1000 = 1.15 g — still too large!

Let me use more realistic numbers:
```

**Corrected Solved Example 7.6:**
**Q:** 1 g of impure CaCO₃ is dissolved in 50 mL of 0.5 N HCl (excess). The excess HCl requires 20 mL of 0.25 N NaOH. Find the % purity. (Eq.wt of CaCO₃ = 50) 🔴 ⭐⭐

**Solution:**
```
Step 1: Total meq of HCl
    meq_HCl = 0.5 × 50 = 25 meq

Step 2: meq of excess HCl (titrated by NaOH)
    meq_excess = 0.25 × 20 = 5 meq

Step 3: meq of HCl that reacted with CaCO₃
    meq_CaCO₃ = 25 - 5 = 20 meq

Step 4: Mass of pure CaCO₃
    mass = (meq × Eq.wt) / 1000 = (20 × 50) / 1000 = 1.0 g

Hmm — exactly 1 g. But sample was 1 g. So purity = 100%.

Let me set up a clean example with clear numbers:
```

**Clean Solved Example 7.6:**
**Q:** 0.5 g of impure CaCO₃ is dissolved in 100 mL of 0.1 N HCl. The excess HCl requires 20 mL of 0.1 N NaOH. Find the % purity. (Eq. wt of CaCO₃ = 50) 🔴 ⭐⭐

**Solution:**
```
Step 1: Total meq of HCl added
    meq_HCl = N × V(mL) = 0.1 × 100 = 10 meq

Step 2: meq of excess HCl (titrated with NaOH)
    meq_excess = 0.1 × 20 = 2 meq

Step 3: meq of HCl consumed by CaCO₃
    meq_consumed = 10 - 2 = 8 meq

Step 4: Mass of pure CaCO₃
    gram eq = 8/1000 = 0.008 eq
    mass = 0.008 × 50 = 0.4 g

Step 5: % purity
    purity = (0.4/0.5) × 100 = 80%

Answer: 80% purity
```

> **Back titration logic:** Total reagent − leftover reagent = reagent consumed by the analyte.

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.6a"></span>7.6a | 0.7 g of impure CaCO₃ + 100 mL of 0.2 N HCl. Excess needs 30 mL of 0.1 N NaOH. Find purity. (Eq.wt = 50) ⭐ | 🔴 |
| <span id="q-7.6b"></span>7.6b | 1 g of antacid (assume pure CaCO₃) + 50 mL of 0.5 N HCl. Excess titrated with 15 mL of 0.2 N NaOH. Find mass of CaCO₃ actually present and % active ingredient. ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**7.6a**: Answer not found.
**7.6b**: Answer not found.

</details>


---

### Type 7: Normality of Polyprotic Acids Depending on Reaction ⭐

**The Pattern:** The n-factor of H₃PO₄ depends on how many H⁺ ions actually react.

#### Solved Example 7.7
**Q:** 1 M H₃PO₄ reacts with NaOH. Find the normality when: (a) H₃PO₄ → NaH₂PO₄ (b) H₃PO₄ → Na₂HPO₄ (c) H₃PO₄ → Na₃PO₄ 🟡 ⭐

**Solution:**
```
(a) H₃PO₄ + NaOH → NaH₂PO₄ + H₂O
    Only 1 H⁺ replaced → n = 1
    N = 1 × 1 = 1 N

(b) H₃PO₄ + 2NaOH → Na₂HPO₄ + 2H₂O
    2 H⁺ replaced → n = 2
    N = 2 × 1 = 2 N

(c) H₃PO₄ + 3NaOH → Na₃PO₄ + 3H₂O
    3 H⁺ replaced → n = 3
    N = 3 × 1 = 3 N

Answer: (a) 1N  (b) 2N  (c) 3N — all from the SAME 1M solution!
```

> **Key lesson:** Normality is reaction-dependent! The same solution can have different normalities depending on the reaction it undergoes. This is why some modern textbooks avoid normality — it's ambiguous without specifying the reaction.

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.7a"></span>7.7a | 0.5 M H₂SO₄: Find N when (a) both H⁺ react (b) only one H⁺ reacts (as NaHSO₄). | 🟡 |
| <span id="q-7.7b"></span>7.7b | What is the normality of 0.1 M H₂CO₃ if it reacts to form (a) NaHCO₃ (b) Na₂CO₃? | 🟡 |

<details>
<summary>View Answers</summary>

**7.7a**: Answer not found.
**7.7b**: Answer not found.

</details>


---

### Type 8: Normality in Redox Reactions ⭐⭐

**The Pattern:** n-factor = total change in oxidation state per formula unit.

#### Solved Example 7.8
**Q:** Find the normality of 0.02 M KMnO₄ in: (a) acidic medium (b) neutral medium (c) basic medium. 🟡 ⭐

**Solution:**
```
(a) Acidic: MnO₄⁻ → Mn²⁺ (change from +7 to +2 = 5 electrons)
    n = 5
    N = 5 × 0.02 = 0.1 N

(b) Neutral: MnO₄⁻ → MnO₂ (change from +7 to +4 = 3 electrons)
    n = 3
    N = 3 × 0.02 = 0.06 N

(c) Basic: MnO₄⁻ → MnO₄²⁻ (change from +7 to +6 = 1 electron)
    n = 1
    N = 1 × 0.02 = 0.02 N

Answer: (a) 0.1N  (b) 0.06N  (c) 0.02N
```

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.8a"></span>7.8a | Find N of 0.05 M K₂Cr₂O₇ in acidic medium. (n = 6) ⭐ | 🟡 |
| <span id="q-7.8b"></span>7.8b | 0.1 M FeSO₄ (Fe²⁺ → Fe³⁺). Find N. | 🟢 |
| <span id="q-7.8c"></span>7.8c | 0.1 M Na₂C₂O₄ (oxalate: C₂O₄²⁻ → 2CO₂). Find N. (n = 2) | 🟡 |
| <span id="q-7.8d"></span>7.8d | 0.02 M KMnO₄ titrates 20 mL of 0.1 M FeSO₄ in acidic medium. Find volume of KMnO₄ needed. (Equate meq: N₁V₁ = N₂V₂) ⭐⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**7.8a**: Answer not found.
**7.8b**: Answer not found.
**7.8c**: Answer not found.
**7.8d**: Answer not found.

</details>


---

### Type 9: Milliequivalent Concept (meq = N × V_mL)

**The Pattern:** Working in milliequivalents for titration calculations.

#### Solved Example 7.9
**Q:** How many milliequivalents of H₂SO₄ are present in 50 mL of 0.2 N H₂SO₄? 🟢

**Solution:**
```
    meq = N × V(mL) = 0.2 × 50 = 10 meq

Answer: 10 milliequivalents
```

#### Key meq Relationships
```
1 equivalent = 1000 milliequivalents
meq = N × V(mL)
mass (mg) = meq × equivalent weight
```

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.9a"></span>7.9a | meq of NaOH in 25 mL of 0.1 N NaOH? | 🟢 |
| <span id="q-7.9b"></span>7.9b | How many mg of NaOH in 25 mL of 0.1 N NaOH? (Eq.wt = 40) | 🟡 |
| <span id="q-7.9c"></span>7.9c | 10 meq of HCl = how many mL of 0.5 N HCl? | 🟡 |

<details>
<summary>View Answers</summary>

**7.9a**: Answer not found.
**7.9b**: Answer not found.
**7.9c**: Answer not found.

</details>


---

### Type 10: Mixed Titration / Double Indicator Problems (Advanced)

**The Pattern:** A mixture of two bases (e.g., NaOH + Na₂CO₃) is titrated with HCl using two indicators.

#### Concept Brief
```
When NaOH + Na₂CO₃ is titrated with HCl:

Indicator 1 (Phenolphthalein — PP):
    - NaOH + HCl → NaCl + H₂O        (complete)
    - Na₂CO₃ + HCl → NaHCO₃ + NaCl   (half of Na₂CO₃ reacts)
    Volume of HCl = V₁ (at PP endpoint)

Indicator 2 (Methyl Orange — MO):
    Continue from PP endpoint:
    - NaHCO₃ + HCl → NaCl + H₂O + CO₂  (remaining half)
    Additional volume = V₂ (from PP to MO)

Results:
    meq of Na₂CO₃ = 2 × V₂ × N_HCl    (V₂ corresponds to half of Na₂CO₃)
    meq of NaOH = (V₁ - V₂) × N_HCl
```

#### Solved Example 7.10
**Q:** A mixture of NaOH and Na₂CO₃ is dissolved and titrated with 0.1 N HCl. With phenolphthalein, the endpoint comes at 25 mL. After adding methyl orange, an additional 5 mL is needed. Find the meq of NaOH and Na₂CO₃. 🔴 ⭐

**Solution:**
```
    V₁ = 25 mL (PP endpoint)
    V₂ = 5 mL (PP → MO)
    N_HCl = 0.1 N

    meq of Na₂CO₃ = 2 × V₂ × N = 2 × 5 × 0.1 = 1 meq
    meq of NaOH = (V₁ - V₂) × N = (25 - 5) × 0.1 = 2 meq

Answer: meq NaOH = 2, meq Na₂CO₃ = 1
```

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.10a"></span>7.10a | NaOH + Na₂CO₃ mixture titrated with 0.5 N HCl. V₁ (PP) = 20 mL, V₂ (PP→MO) = 8 mL. Find meq and mass of each. (Eq.wt NaOH = 40, Eq.wt Na₂CO₃ = 53) ⭐ | 🔴 |
| <span id="q-7.10b"></span>7.10b | If V₁ = V₂ in the above setup, what does it mean about the sample? | 🔴 |

<details>
<summary>View Answers</summary>

**7.10a**: Answer not found.
**7.10b**: Answer not found.

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-7.M1"></span>7.M1 | Concentrated H₂SO₄ is 98% w/w, d = 1.84 g/mL. Find: (a) molarity (b) normality (c) equivalent weight (d) volume needed to make 500 mL of 0.1 N H₂SO₄. | T2 + Ch6-T4 + T3 + T4 | 🔴 |
| <span id="q-7.M2"></span>7.M2 | 0.316 g of KMnO₄ (M=158) is dissolved to make 100 mL of solution. Find its normality in (a) acidic medium (b) neutral medium. Then use each normality to find how many mL of 0.1 N FeSO₄ it can titrate in acidic medium. | T1 + T8 + T5 | 🔴 |
| <span id="q-7.M3"></span>7.M3 | 25 mL of 0.1 M H₂SO₄ is titrated with 0.1 M NaOH. (a) Convert both to normality. (b) Find volume of NaOH needed. (c) Verify using mole method. | T2 + T5 | 🟡 |

<details>
<summary>View Answers</summary>

**7.M1**: Answer not found.
**7.M2**: Answer not found.
**7.M3**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.B1"></span>7.B1 | Find the normality of: (a) 0.5 M H₂SO₄ (b) 0.25 M Ca(OH)₂ (c) 2 M HCl. ⭐ | 🟢 |
| <span id="q-7.B2"></span>7.B2 | 3.65 g of HCl is dissolved in water to make 1 L. Find N and M. | 🟢 |
| <span id="q-7.B3"></span>7.B3 | 25 mL of an NaOH solution of unknown concentration requires 20 mL of 0.1 N HCl for neutralisation. Find the normality and molarity of NaOH. ⭐ | 🟡 |
| <span id="q-7.B4"></span>7.B4 | Find the equivalent weight of: (a) H₂SO₄ (b) NaOH (c) Ca(OH)₂ (d) Na₂CO₃ (reacts with 2H⁺). | 🟢 |

<details>
<summary>View Answers</summary>

**7.B1**: Answer not found.
**7.B2**: Answer not found.
**7.B3**: Answer not found.
**7.B4**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-7.J1"></span>7.J1 | 20 mL of 0.02 M KMnO₄ in acidic medium reacts with X mL of 0.1 M FeSO₄. Find X. (Use normality approach.) ⭐⭐ | 🔴 |
| <span id="q-7.J2"></span>7.J2 | 1 g of a mixture of Na₂CO₃ and NaHCO₃ requires 15 mL of 0.1 N HCl. The same weight, treated with excess HCl, requires 20 mL total. Find mass of each in the mixture. ⭐ | 🔴 |
| <span id="q-7.J3"></span>7.J3 | 25 mL of H₂O₂ is titrated with 20 mL of 0.02 M KMnO₄ in acidic medium. Find the volume strength of H₂O₂. (1 volume H₂O₂ = 0.1786 N) ⭐ | 🔴 |
| <span id="q-7.J4"></span>7.J4 | Is it meaningful to say "the normality of H₃PO₄ is 3N" without specifying the reaction? Discuss. | 🟡 |
| <span id="q-7.J5"></span>7.J5 | 0.1 g of an oxalic acid sample (H₂C₂O₄·2H₂O, M = 126) is dissolved in water and titrated with 0.05 M KMnO₄ in acidic medium. 20 mL of KMnO₄ is required. Find the purity of oxalic acid. (n-factor of oxalate = 2, n-factor of KMnO₄ = 5) ⭐⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**7.J1**: X = 20 mL *(Key Step: KMnO₄ N=0.1; FeSO₄ N=0.1; 0.1×20=0.1×X → X=20)*
**7.J2**: Answer not found.
**7.J3**: Answer not found.
**7.J4**: Answer not found.
**7.J5**: Answer not found.

</details>


---

## Key Takeaways from Chapter 7

```
┌──────────────────────────────────────────────────────────────┐
│                   NORMALITY SUMMARY                           │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Formula: N = gram equivalents / V(L)                        │
│                                                               │
│  Key Relation: N = n-factor × M  ← MEMORIZE                 │
│                                                               │
│  Equivalent Weight = Molar Mass / n-factor                   │
│                                                               │
│  n-factor rules:                                              │
│    Acids: # of H⁺ donated                                   │
│    Bases: # of OH⁻ donated                                  │
│    Redox: Change in oxidation state per formula unit         │
│                                                               │
│  Titration at equivalence:                                    │
│    N₁V₁ = N₂V₂  (meq acid = meq base)                      │
│                                                               │
│  ⚠️ n-factor is REACTION DEPENDENT                           │
│    KMnO₄: n=5 (acidic), n=3 (neutral), n=1 (basic)         │
│    H₃PO₄: n=1,2,3 depending on how many H⁺ react           │
│                                                               │
│  meq = N × V(mL)  (fast titration calculation)               │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 6 — Molarity](./06-molarity.md) | [Chapter 8 — Dilution →](./08-dilution.md)*
