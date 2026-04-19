# Chapter 4: Mole Fraction (χ)
## Part II: Enter the Mole

---

## 🎯 Stage 1: The Core Idea

### What is Mole Fraction?

Until now, we measured concentration using **mass** or **volume**. But chemistry doesn't run on grams — it runs on **moles**. One mole of any substance has the same number of particles (6.022 × 10²³). So if we want to know what fraction of all the particles in a solution belong to the solute, we need **mole fraction**.

> **Analogy:** Imagine a classroom with 30 students and 2 teachers. The "teacher fraction" is 2/32 = 0.0625. It tells you what proportion of all people in the room are teachers. Mole fraction does the exact same thing — but for molecules.

### Why Mole Fraction Matters

| Reason | Details |
|--------|---------|
| **Raoult's Law** | Vapour pressure of a solution: P = χ_solvent × P° |
| **Dalton's Law** | Partial pressure of a gas: P_A = χ_A × P_total |
| **No units** | Mole fraction is a pure ratio — no units, no confusion |
| **Temperature independent** | Based on moles (= number of particles), which don't change with T |
| **Symmetric** | Treats solute and solvent equally — no arbitrary "who is what" |

---

## 🔬 Stage 2: The Formula Lab

### The Formula (Binary Solution)

```
         Moles of component A           n_A
χ_A = ──────────────────────────── = ─────────
       Total moles in solution        n_A + n_B
```

### The Golden Rule

```
χ_A + χ_B = 1     (for binary solutions — ALWAYS)

In general: χ_1 + χ_2 + χ_3 + ... + χ_n = 1  (for any mixture)
```

> **Why does this work?** Because:
> χ_A + χ_B = n_A/(n_A + n_B) + n_B/(n_A + n_B) = (n_A + n_B)/(n_A + n_B) = 1

### From Mass to Mole Fraction — The Bridge

```
Step 1: Convert mass to moles          n = mass / molar mass
Step 2: Find total moles               n_total = n_A + n_B
Step 3: Divide                          χ_A = n_A / n_total
```

### Units Check

- Moles / Moles = **dimensionless** (no units)
- χ is always between 0 and 1
- χ = 0 means the component is absent
- χ = 1 means the component is pure

### Temperature Dependence

Mole fraction is **temperature-independent** ✅

Why? Because moles = number of particles. Heating something doesn't create or destroy particles. Both numerator (n_A) and denominator (n_A + n_B) stay constant.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given moles of solute & solvent, find χ

**The Pattern:** The simplest case. Moles are directly given → plug into formula.

#### Solved Example 4.1
**Q:** A solution contains 3 moles of ethanol and 7 moles of water. Find the mole fraction of ethanol and water. 🟢

**Solution:**
```
Given:
    n_ethanol = 3 mol
    n_water = 7 mol

Step 1: Total moles
    n_total = 3 + 7 = 10 mol

Step 2: Mole fractions
    χ_ethanol = 3/10 = 0.3
    χ_water = 7/10 = 0.7

Verification: 0.3 + 0.7 = 1.0 ✅

Answer: χ_ethanol = 0.3, χ_water = 0.7
```

> **Why this works:** When moles are directly given, it's a straight division. No conversion needed. Always verify that the mole fractions add to 1 — it's a free error-check.

> **⚠️ Common Mistake:** Students sometimes write χ = n_solute/n_solvent instead of n_solute/n_total. The denominator is ALWAYS the total moles, not just the solvent.

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 4.1a | A solution has 2 mol of sugar and 8 mol of water. Find χ_sugar and χ_water. | 🟢 |
| 4.1b | 0.5 mol acetone is mixed with 4.5 mol chloroform. Find χ of each. | 🟢 |
| 4.1c | 1.5 mol NaCl is dissolved in 53.5 mol of water. Find χ_NaCl. | 🟢 |
| 4.1d | A solution has χ_A = 0.35. If n_A = 7 mol, find n_B and χ_B. | 🟡 |
| 4.1e | A homogeneous mixture contains 4 mol of helium and 6 mol of argon. Calculate the mole fraction of each gas. | 🟢 |
| 4.1f | An alloy consists of 1.2 mol of copper and 0.8 mol of zinc. Determine the mole fraction of copper in the alloy. | 🟢 |
| 4.1g | A laboratory stock solution holds 2.5 mol of sulfuric acid and 17.5 mol of water. What is the mole fraction of sulfuric acid? | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**4.1a:**
- **Given:** $n_{sugar} = 2$ mol, $n_{water} = 8$ mol
- **Calculation:** $n_{total} = 2 + 8 = 10$ mol. $\chi_{sugar} = \frac{2}{10} = 0.2$. $\chi_{water} = \frac{8}{10} = 0.8$.
- **Final Answer:** $\chi_{sugar} = 0.2, \chi_{water} = 0.8$

**4.1b:**
- **Given:** $n_{acetone} = 0.5$ mol, $n_{chloroform} = 4.5$ mol
- **Calculation:** $n_{total} = 0.5 + 4.5 = 5.0$ mol. $\chi_{acetone} = \frac{0.5}{5.0} = 0.1$. $\chi_{chloroform} = \frac{4.5}{5.0} = 0.9$.
- **Final Answer:** $\chi_{acetone} = 0.1, \chi_{chloroform} = 0.9$

**4.1c:**
- **Given:** $n_{NaCl} = 1.5$ mol, $n_{water} = 53.5$ mol
- **Calculation:** $n_{total} = 1.5 + 53.5 = 55.0$ mol. $\chi_{NaCl} = \frac{1.5}{55.0} = 0.027$.
- **Final Answer:** $\chi_{NaCl} \approx 0.0273$

**4.1d:**
- **Given:** $\chi_A = 0.35$, $n_A = 7$ mol
- **Calculation:** $\chi_B = 1 - 0.35 = 0.65$. $\frac{n_A}{n_{total}} = 0.35 \Rightarrow n_{total} = \frac{7}{0.35} = 20$ mol. $n_B = n_{total} - n_A = 20 - 7 = 13$ mol.
- **Final Answer:** $n_B = 13$ mol, $\chi_B = 0.65$

**4.1e:**
- **Given:** $n_{He} = 4$ mol, $n_{Ar} = 6$ mol
- **Calculation:** $n_{total} = 10$ mol. $\chi_{He} = \frac{4}{10} = 0.4$, $\chi_{Ar} = \frac{6}{10} = 0.6$.
- **Final Answer:** $\chi_{He} = 0.4, \chi_{Ar} = 0.6$

**4.1f:**
- **Given:** $n_{Cu} = 1.2$ mol, $n_{Zn} = 0.8$ mol
- **Calculation:** $n_{total} = 1.2 + 0.8 = 2.0$ mol. $\chi_{Cu} = \frac{1.2}{2.0} = 0.6$.
- **Final Answer:** $\chi_{Cu} = 0.6$

**4.1g:**
- **Given:** $n_{H_2SO_4} = 2.5$ mol, $n_{water} = 17.5$ mol
- **Calculation:** $n_{total} = 2.5 + 17.5 = 20.0$ mol. $\chi_{H_2SO_4} = \frac{2.5}{20.0} = 0.125$.
- **Final Answer:** $\chi_{H_2SO_4} = 0.125$

</details>

---

### Type 2: Given masses → convert to moles → find χ

**The Pattern:** Masses given, not moles. Convert first, then apply χ formula.

#### Solved Example 4.2
**Q:** 46 g of ethanol (C₂H₅OH) is dissolved in 180 g of water. Find the mole fraction of ethanol. 🟢

**Solution:**
```
Step 1: Calculate moles
    Molar mass of ethanol = 2(12) + 6(1) + 16 = 46 g/mol
    Molar mass of water = 18 g/mol

    n_ethanol = 46/46 = 1 mol
    n_water = 180/18 = 10 mol

Step 2: Total moles
    n_total = 1 + 10 = 11 mol

Step 3: Mole fractions
    χ_ethanol = 1/11 = 0.0909
    χ_water = 10/11 = 0.9091

Verification: 0.0909 + 0.9091 = 1.0 ✅

Answer: χ_ethanol ≈ 0.091, χ_water ≈ 0.909
```

> **Why this works:** The key step is converting mass to moles using n = mass/M. Once you have moles, the formula is the same as Type 1.

> **⚠️ Common Mistake:** Using the wrong molar mass. Always write out the molar mass calculation explicitly. For ethanol: C₂H₅OH = 2(12) + 5(1) + 16 + 1 = 46, NOT 2(12) + 6(1) + 16 = 46. Both give 46 here, but the molecular formula must be read correctly.

#### Solved Example 4.2B
**Q:** 23 g of sodium (Na) is dissolved in 100 g of mercury (Hg) to form an amalgam. Find the mole fraction of sodium. 🟡

**Solution:**
```
Step 1: Calculate moles
    n_Na = 23/23 = 1 mol
    n_Hg = 100/200 = 0.5 mol

Step 2: Total moles
    n_total = 1 + 0.5 = 1.5 mol

Step 3: Mole fraction
    χ_Na = 1/1.5 = 2/3 ≈ 0.667

Answer: χ_Na = 0.667
```

> **Notice:** Even though sodium has less mass than mercury, it has MORE moles (because Na is lighter). Mole fraction captures the particle ratio, not the mass ratio.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 4.2a | 60 g of urea (NH₂CONH₂, M = 60) in 360 g water. Find χ_urea. ⭐ | 🟢 |
| 4.2b | 11.7 g of NaCl (M = 58.5) in 90 g of water. Find χ_NaCl. | 🟡 |
| 4.2c | 92 g of ethanol (M = 46) in 144 g of water. Find χ of each. | 🟢 |
| 4.2d | 34.2 g of sucrose (C₁₂H₂₂O₁₁, M = 342) in 100 g of water. Find χ_sucrose. | 🟡 |
| 4.2e | A solution has 10 g of methanol (CH₃OH, M = 32) and 40 g of ethanol (C₂H₅OH, M = 46). Find χ of each. | 🟡 |
| 4.2f | 64 g of methanol (CH₃OH, M = 32) is mixed with 144 g of water. Find the mole fraction of methanol. | 🟢 |
| 4.2g | 31.5 g of nitric acid (HNO₃, M = 63) is dissolved in 90 g of water. Calculate the mole fraction of both components. | 🟡 |
| 4.2h | 180 g of glucose (C₆H₁₂O₆, M = 180) is dissolved in 360 g of water. Find χ_glucose. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**4.2a:**
- **Given:** $m_{urea} = 60$ g ($M = 60$), $m_{water} = 360$ g ($M = 18$)
- **Calculation:** $n_{urea} = \frac{60}{60} = 1$ mol. $n_{water} = \frac{360}{18} = 20$ mol. $n_{total} = 1 + 20 = 21$ mol. $\chi_{urea} = \frac{1}{21}$.
- **Final Answer:** $\chi_{urea} \approx 0.0476$

**4.2b:**
- **Given:** $m_{NaCl} = 11.7$ g ($M = 58.5$), $m_{water} = 90$ g ($M = 18$)
- **Calculation:** $n_{NaCl} = \frac{11.7}{58.5} = 0.2$ mol. $n_{water} = \frac{90}{18} = 5$ mol. $n_{total} = 0.2 + 5 = 5.2$ mol. $\chi_{NaCl} = \frac{0.2}{5.2} = \frac{1}{26}$.
- **Final Answer:** $\chi_{NaCl} \approx 0.0385$

**4.2c:**
- **Given:** $m_{ethanol} = 92$ g ($M = 46$), $m_{water} = 144$ g ($M = 18$)
- **Calculation:** $n_{ethanol} = \frac{92}{46} = 2$ mol. $n_{water} = \frac{144}{18} = 8$ mol. $n_{total} = 10$ mol. $\chi_{ethanol} = \frac{2}{10} = 0.2, \chi_{water} = \frac{8}{10} = 0.8$.
- **Final Answer:** $\chi_{ethanol} = 0.2, \chi_{water} = 0.8$

**4.2d:**
- **Given:** $m_{sucrose} = 34.2$ g ($M = 342$), $m_{water} = 100$ g ($M = 18$)
- **Calculation:** $n_{sucrose} = \frac{34.2}{342} = 0.1$ mol. $n_{water} = \frac{100}{18} = 5.55$ mol. $n_{total} = 5.655$ mol. $\chi_{sucrose} = \frac{0.1}{5.655}$.
- **Final Answer:** $\chi_{sucrose} \approx 0.0177$

**4.2e:**
- **Given:** $m_{methanol} = 10$ g ($M = 32$), $m_{ethanol} = 40$ g ($M = 46$)
- **Calculation:** $n_{methanol} = \frac{10}{32} = 0.3125$ mol. $n_{ethanol} = \frac{40}{46} = 0.8696$ mol. $n_{total} = 0.3125 + 0.8696 = 1.1821$ mol. $\chi_{methanol} = \frac{0.3125}{1.1821}$. $\chi_{ethanol} = \frac{0.8696}{1.1821}$.
- **Final Answer:** $\chi_{methanol} \approx 0.264, \chi_{ethanol} \approx 0.736$

**4.2f:**
- **Given:** $m_{methanol} = 64$ g ($M = 32$), $m_{water} = 144$ g ($M = 18$)
- **Calculation:** $n_{methanol} = \frac{64}{32} = 2$ mol. $n_{water} = \frac{144}{18} = 8$ mol. $n_{total} = 10$ mol. $\chi_{methanol} = \frac{2}{10} = 0.2$.
- **Final Answer:** $\chi_{methanol} = 0.2$

**4.2g:**
- **Given:** $m_{HNO_3} = 31.5$ g ($M = 63$), $m_{water} = 90$ g ($M = 18$)
- **Calculation:** $n_{HNO_3} = \frac{31.5}{63} = 0.5$ mol. $n_{water} = \frac{90}{18} = 5$ mol. $n_{total} = 5.5$ mol. $\chi_{HNO_3} = \frac{0.5}{5.5} = \frac{1}{11}$. $\chi_{water} = \frac{5}{5.5} = \frac{10}{11}$.
- **Final Answer:** $\chi_{HNO_3} \approx 0.091, \chi_{water} \approx 0.909$

**4.2h:**
- **Given:** $m_{glucose} = 180$ g ($M = 180$), $m_{water} = 360$ g ($M = 18$)
- **Calculation:** $n_{glucose} = \frac{180}{180} = 1$ mol. $n_{water} = \frac{360}{18} = 20$ mol. $n_{total} = 21$ mol. $\chi_{glucose} = \frac{1}{21}$.
- **Final Answer:** $\chi_{glucose} \approx 0.0476$

</details>

---

### Type 3: Reverse — Given χ, find mole ratio

**The Pattern:** Mole fraction is given → find how many moles of each component are present (as a ratio).

#### Solved Example 4.3
**Q:** The mole fraction of glucose in an aqueous solution is 0.02. Find the ratio of moles of glucose to moles of water. 🟢

**Solution:**
```
Given: χ_glucose = 0.02

Step 1: Find χ_water
    χ_water = 1 - 0.02 = 0.98

Step 2: Find the ratio
    n_glucose / n_water = χ_glucose / χ_water = 0.02 / 0.98

    n_glucose : n_water = 2 : 98 = 1 : 49

Answer: For every 1 mole of glucose, there are 49 moles of water.
```

> **Why this works:** Since χ_A = n_A/n_total and χ_B = n_B/n_total, the ratio χ_A/χ_B = n_A/n_B. The total moles cancel out!

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 4.3a | χ_solute = 0.1. Find the mole ratio of solute to solvent. | 🟢 |
| 4.3b | χ_ethanol = 0.2 in an ethanol-water solution. If 10 moles of water are present, how many moles of ethanol? | 🟡 |
| 4.3c | χ_NaCl = 0.05 in a saline solution. If the total moles in solution = 200, find the moles of NaCl and water. | 🟡 |
| 4.3d | An aqueous solution of acetic acid has χ_acid = 0.04. Determine the ratio of acetic acid moles to completely pure solvent moles. | 🟢 |
| 4.3e | In a gas cylinder, χ_nitrogen = 0.8. If the total moles inside equal 50, exactly how many moles of nitrogen are contained? | 🟡 |
| 4.3f | A biochemist observes χ_enzyme = 0.01 in a buffer matrix. Calculate the exact ratio of buffer moles to enzyme moles. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**4.3a:**
- **Given:** $\chi_{solute} = 0.1$
- **Calculation:** $\chi_{solvent} = 1 - 0.1 = 0.9$. Ratio $n_{solute} : n_{solvent} = \chi_{solute} : \chi_{solvent} = 0.1 : 0.9 = 1 : 9$.
- **Final Answer:** $1:9$

**4.3b:**
- **Given:** $\chi_{ethanol} = 0.2$, $n_{water} = 10$ mol
- **Calculation:** $\chi_{water} = 0.8$. $\frac{n_{ethanol}}{n_{water}} = \frac{0.2}{0.8} = \frac{1}{4}$. $n_{ethanol} = 10 \cdot \frac{1}{4} = 2.5$ mol.
- **Final Answer:** $2.5$ mol

**4.3c:**
- **Given:** $\chi_{NaCl} = 0.05$, $n_{total} = 200$
- **Calculation:** $n_{NaCl} = \chi_{NaCl} \cdot n_{total} = 0.05 \cdot 200 = 10$ mol. $n_{water} = 200 - 10 = 190$ mol.
- **Final Answer:** $n_{NaCl} = 10$ mol, $n_{water} = 190$ mol

**4.3d:**
- **Given:** $\chi_{acid} = 0.04$
- **Calculation:** $\chi_{solvent} = 1 - 0.04 = 0.96$. $\frac{n_{acid}}{n_{solvent}} = \frac{0.04}{0.96} = \frac{1}{24}$.
- **Final Answer:** $1:24$

**4.3e:**
- **Given:** $\chi_{nitrogen} = 0.8$, $n_{total} = 50$
- **Calculation:** $n_{nitrogen} = \chi_{nitrogen} \cdot n_{total} = 0.8 \cdot 50 = 40$ mol.
- **Final Answer:** $40$ mol

**4.3f:**
- **Given:** $\chi_{enzyme} = 0.01$
- **Calculation:** $\chi_{buffer} = 1 - 0.01 = 0.99$. Ratio $n_{buffer} : n_{enzyme} = 0.99 : 0.01 = 99 : 1$.
- **Final Answer:** $99:1$

</details>

---

### Type 4: Given χ of one component → find χ of the other

**The Pattern:** The simplest possible problem. Uses χ_A + χ_B = 1.

#### Solved Example 4.4
**Q:** In a binary solution, χ_solute = 0.15. Find χ_solvent. 🟢

**Solution:**
```
χ_solvent = 1 - χ_solute = 1 - 0.15 = 0.85

Answer: χ_solvent = 0.85
```

This seems trivially easy — and it is. But this rule becomes critical when combined with other types, especially in multi-step interconversion problems.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 4.4a | χ_A = 0.3 in a binary mixture. Find χ_B. | 🟢 |
| 4.4b | χ_water = 0.95. What is χ_solute? If the solute is NaCl, how many moles of NaCl per 100 moles of water? | 🟡 |
| 4.4c | Is it possible for both χ_A > 0.5 and χ_B > 0.5 in a binary mixture? Justify your answer. | 🟡 |
| 4.4d | In a binary liquid mixture of toluene and benzene, χ_benzene = 0.42. What is χ_toluene? | 🟢 |
| 4.4e | If the mole fraction of solvent in a binary solution is exactly 0.992, how many actual moles of solute exist per exactly 1 mole of solvent? | 🟡 |
| 4.4f | Explain purely mathematically why χ_solute can never equal precisely 1.0 in a true binary solution. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**4.4a:**
- **Given:** $\chi_A = 0.3$
- **Calculation:** $\chi_B = 1 - \chi_A = 1 - 0.3 = 0.7$.
- **Final Answer:** $\chi_B = 0.7$

**4.4b:**
- **Given:** $\chi_{water} = 0.95$
- **Calculation:** $\chi_{solute} = 1 - 0.95 = 0.05$. Ratio $n_{solute} : n_{water} = 0.05 : 0.95 = 1 : 19$. For 100 moles of water, $n_{solute} = \frac{100}{19} \approx 5.26$ moles.
- **Final Answer:** $\chi_{solute} = 0.05$, $5.26$ moles of NaCl per $100$ moles of water.

**4.4c:**
- **Given:** binary mixture
- **Calculation:** $\chi_A + \chi_B = 1$. If both $> 0.5$, then sum $> 1.0$, which is mathematically impossible.
- **Final Answer:** No, it is impossible since they must sum exactly to 1.

**4.4d:**
- **Given:** $\chi_{benzene} = 0.42$
- **Calculation:** $\chi_{toluene} = 1 - 0.42 = 0.58$.
- **Final Answer:** $\chi_{toluene} = 0.58$

**4.4e:**
- **Given:** $\chi_{solvent} = 0.992$, $n_{solvent} = 1$ mol
- **Calculation:** $\chi_{solute} = 1 - 0.992 = 0.008$. $n_{solute} = n_{solvent} \cdot \frac{0.008}{0.992} = 1 \cdot \frac{1}{124} \approx 0.00806$ mol.
- **Final Answer:** $0.00806$ moles of solute

**4.4f:**
- **Given:** Concept question
- **Calculation:** If $\chi_{solute} = 1.0$, then $\chi_{solvent} = 0$. This means there is no solvent at all, making it a pure substance, not a binary solution.
- **Final Answer:** $\chi=1$ implies a pure substance, not a mixture/solution.

</details>

---

### Type 5: Multi-component Mixtures (3 or more substances)

**The Pattern:** More than two substances. The same formula applies, but with more terms in the denominator.

#### Solved Example 4.5
**Q:** A gas mixture contains 2 mol N₂, 0.5 mol O₂, and 0.1 mol CO₂. Find the mole fraction of each gas. 🟡

**Solution:**
```
Step 1: Total moles
    n_total = 2 + 0.5 + 0.1 = 2.6 mol

Step 2: Individual mole fractions
    χ_N₂ = 2/2.6 = 0.769
    χ_O₂ = 0.5/2.6 = 0.192
    χ_CO₂ = 0.1/2.6 = 0.038

Verification: 0.769 + 0.192 + 0.038 ≈ 0.999 ≈ 1.0 ✅
    (rounding error is normal)

Answer: χ_N₂ = 0.769, χ_O₂ = 0.192, χ_CO₂ = 0.038
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 4.5a | A solution has 1 mol glucose, 0.5 mol sucrose, and 50 mol water. Find χ of each. | 🟡 |
| 4.5b | Air is approximately 78% N₂, 21% O₂, and 1% Ar by moles. Find χ of each gas. | 🟢 |
| 4.5c | A mixture of 5 g methanol (M=32), 10 g ethanol (M=46), and 85 g water. Find χ of each. | 🟡 |
| 4.5d | A diving gas tank contains 0.5 mol O₂, 2.0 mol He, and 0.5 mol N₂. Find the mole fraction of helium. | 🟢 |
| 4.5e | A petroleum fraction contains 20 g of pentane (M = 72), 43 g of hexane (M = 86), and 100 g of heptane (M = 100). Calculate the mole fraction of hexane. | 🟡 |
| 4.5f | An atmospheric sample has perfectly equal mass fractions of N₂ (M = 28) and O₂ (M = 32). Find the exact mole fraction of precisely O₂. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**4.5a:**
- **Given:** $n_{glucose} = 1$, $n_{sucrose} = 0.5$, $n_{water} = 50$
- **Calculation:** $n_{total} = 1 + 0.5 + 50 = 51.5$ mol. $\chi_{glucose} = \frac{1}{51.5} \approx 0.0194$. $\chi_{sucrose} = \frac{0.5}{51.5} \approx 0.0097$. $\chi_{water} = \frac{50}{51.5} \approx 0.9709$.
- **Final Answer:** $\chi_{glucose} \approx 0.019, \chi_{sucrose} \approx 0.010, \chi_{water} \approx 0.971$

**4.5b:**
- **Given:** $n_{N_2} = 78$, $n_{O_2} = 21$, $n_{Ar} = 1$ (assume 100 moles total)
- **Calculation:** $n_{total} = 100$ mol. $\chi_{N_2} = \frac{78}{100} = 0.78$. $\chi_{O_2} = \frac{21}{100} = 0.21$. $\chi_{Ar} = \frac{1}{100} = 0.01$.
- **Final Answer:** $\chi_{N_2} = 0.78, \chi_{O_2} = 0.21, \chi_{Ar} = 0.01$

**4.5c:**
- **Given:** $m_{methanol} = 5$ g ($M=32$), $m_{ethanol} = 10$ g ($M=46$), $m_{water} = 85$ g ($M=18$)
- **Calculation:** $n_{methanol} = \frac{5}{32} \approx 0.156$. $n_{ethanol} = \frac{10}{46} \approx 0.217$. $n_{water} = \frac{85}{18} \approx 4.722$. $n_{total} = 0.156 + 0.217 + 4.722 = 5.095$ mol. $\chi_{methanol} = \frac{0.156}{5.095}$. $\chi_{ethanol} = \frac{0.217}{5.095}$. $\chi_{water} = \frac{4.722}{5.095}$.
- **Final Answer:** $\chi_{methanol} \approx 0.031, \chi_{ethanol} \approx 0.043, \chi_{water} \approx 0.927$

**4.5d:**
- **Given:** $n_{O_2} = 0.5$, $n_{He} = 2.0$, $n_{N_2} = 0.5$
- **Calculation:** $n_{total} = 0.5 + 2.0 + 0.5 = 3.0$ mol. $\chi_{He} = \frac{2.0}{3.0} \approx 0.667$.
- **Final Answer:** $\chi_{He} = 0.667$

**4.5e:**
- **Given:** $m_{pentane} = 20$ g ($M=72$), $m_{hexane} = 43$ g ($M=86$), $m_{heptane} = 100$ g ($M=100$)
- **Calculation:** $n_{pentane} = \frac{20}{72} \approx 0.278$. $n_{hexane} = \frac{43}{86} = 0.5$. $n_{heptane} = \frac{100}{100} = 1.0$. $n_{total} = 0.278 + 0.5 + 1.0 = 1.778$ mol. $\chi_{hexane} = \frac{0.5}{1.778}$.
- **Final Answer:** $\chi_{hexane} \approx 0.281$

**4.5f:**
- **Given:** Equal mass fractions, let $m_{N_2} = x$ and $m_{O_2} = x$
- **Calculation:** $n_{N_2} = \frac{x}{28}$. $n_{O_2} = \frac{x}{32}$. $n_{total} = \frac{x}{28} + \frac{x}{32} = x \cdot \frac{32 + 28}{28 \cdot 32} = x \cdot \frac{60}{896}$. $\chi_{O_2} = \frac{\frac{x}{32}}{x \cdot \frac{60}{896}} = \frac{1}{32} \cdot \frac{896}{60} = \frac{28}{60} = \frac{7}{15}$.
- **Final Answer:** $\chi_{O_2} = \frac{7}{15} \approx 0.467$

</details>

---

### Type 6: Mole Fraction of Gas Mixtures — Dalton's Law Connection

**The Pattern:** For ideal gases, mole fraction = partial pressure / total pressure.

#### Key Relationship
```
χ_A = P_A / P_total        (Dalton's Law)

where P_A = partial pressure of gas A
      P_total = total pressure = P_A + P_B + ...
```

> **Why this works:** For ideal gases, PV = nRT. At the same T and V, pressure is directly proportional to moles. So the pressure fraction equals the mole fraction.

#### Solved Example 4.6
**Q:** A gas mixture at 1 atm total pressure contains N₂ (partial pressure 0.78 atm) and O₂ (partial pressure 0.22 atm). Find the mole fraction of each gas. 🟢

**Solution:**
```
Using Dalton's Law: χ = P_partial / P_total

    χ_N₂ = 0.78 / 1.0 = 0.78
    χ_O₂ = 0.22 / 1.0 = 0.22

Verification: 0.78 + 0.22 = 1.0 ✅

Answer: χ_N₂ = 0.78, χ_O₂ = 0.22
```

#### Solved Example 4.6B
**Q:** A container has 3 mol H₂ and 1 mol N₂ at a total pressure of 2 atm. Find the partial pressure of each gas. 🟡

**Solution:**
```
Step 1: Find mole fractions
    n_total = 3 + 1 = 4 mol
    χ_H₂ = 3/4 = 0.75
    χ_N₂ = 1/4 = 0.25

Step 2: Apply Dalton's Law
    P_H₂ = χ_H₂ × P_total = 0.75 × 2 = 1.5 atm
    P_N₂ = χ_N₂ × P_total = 0.25 × 2 = 0.5 atm

Verification: 1.5 + 0.5 = 2.0 atm = P_total ✅

Answer: P_H₂ = 1.5 atm, P_N₂ = 0.5 atm
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 4.6a | A gas cylinder contains 8 g of O₂ (M=32) and 7 g of N₂ (M=28). Total pressure is 3 atm. Find the partial pressure of each gas. ⭐ | 🟡 |
| 4.6b | The partial pressure of water vapour in air at 25°C is 23.8 mmHg. Atmospheric pressure is 760 mmHg. Find χ of water vapour. | 🟢 |
| 4.6c | A 10 L container at 300 K holds a mixture of gases with P_total = 5 atm. If χ_He = 0.40, find the partial pressure and moles of He. (R = 0.082 L·atm/mol·K) | 🔴 |
| 4.6d | A synthetic lung mixture has a total pressure of 1000 mmHg. If P_O₂ = 210 mmHg, find χ_O₂ in the mixture. | 🟢 |
| 4.6e | A reaction vessel at exactly 2.5 atm total pressure contains 4 mol of H₂ and 1 mol of CH₄. Calculate the partial pressure of CH₄. | 🟡 |
| 4.6f | The mole fraction of CO₂ in a sealed flask is 0.05. If its partial pressure is 0.1 atm, what is the total pressure in the flask? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**4.6a:**
- **Given:** $m_{O_2} = 8$ g, $m_{N_2} = 7$ g, $P_{total} = 3$ atm
- **Calculation:** $n_{O_2} = \frac{8}{32} = 0.25$ mol. $n_{N_2} = \frac{7}{28} = 0.25$ mol. $n_{total} = 0.5$ mol. $\chi_{O_2} = \frac{0.25}{0.5} = 0.5$. $\chi_{N_2} = \frac{0.25}{0.5} = 0.5$. Partial pressure $P_i = \chi_i P_{total}$. $P_{O_2} = 0.5 \cdot 3 = 1.5$ atm. $P_{N_2} = 0.5 \cdot 3 = 1.5$ atm.
- **Final Answer:** $P_{O_2} = 1.5$ atm, $P_{N_2} = 1.5$ atm

**4.6b:**
- **Given:** $P_{vap} = 23.8$ mmHg, $P_{total} = 760$ mmHg
- **Calculation:** $\chi_{water} = \frac{P_{vap}}{P_{total}} = \frac{23.8}{760}$.
- **Final Answer:** $\chi_{water} \approx 0.0313$

**4.6c:**
- **Given:** $V = 10$ L, $T = 300$ K, $P_{total} = 5$ atm, $\chi_{He} = 0.40$
- **Calculation:** $P_{He} = \chi_{He} \cdot P_{total} = 0.40 \cdot 5 = 2.0$ atm. $n_{He} = \frac{P_{He} V}{R T} = \frac{2.0 \cdot 10}{0.082 \cdot 300} = \frac{20}{24.6}$.
- **Final Answer:** $P_{He} = 2.0$ atm, $n_{He} \approx 0.813$ mol

**4.6d:**
- **Given:** $P_{total} = 1000$ mmHg, $P_{O_2} = 210$ mmHg
- **Calculation:** $\chi_{O_2} = \frac{P_{O_2}}{P_{total}} = \frac{210}{1000} = 0.21$.
- **Final Answer:** $\chi_{O_2} = 0.21$

**4.6e:**
- **Given:** $P_{total} = 2.5$ atm, $n_{H_2} = 4$ mol, $n_{CH_4} = 1$ mol
- **Calculation:** $n_{total} = 4 + 1 = 5$ mol. $\chi_{CH_4} = \frac{1}{5} = 0.2$. $P_{CH_4} = \chi_{CH_4} \cdot P_{total} = 0.2 \cdot 2.5 = 0.5$ atm.
- **Final Answer:** $P_{CH_4} = 0.5$ atm

**4.6f:**
- **Given:** $\chi_{CO_2} = 0.05$, $P_{CO_2} = 0.1$ atm
- **Calculation:** $P_{CO_2} = \chi_{CO_2} \cdot P_{total} \Rightarrow 0.1 = 0.05 \cdot P_{total} \Rightarrow P_{total} = \frac{0.1}{0.05} = 2.0$ atm.
- **Final Answer:** $P_{total} = 2.0$ atm

</details>

---

### Type 7: χ → Molality Conversion ⭐

**The Pattern:** Convert mole fraction to molality. This is a high-frequency Board + JEE formula.

#### Derivation
```
Given: Binary solution of solute A in solvent B.
    χ_A = n_A / (n_A + n_B)

Molality: m = n_A / (mass of solvent in kg)
         m = n_A / (n_B × M_B / 1000)    ← since n_B × M_B = mass of solvent in g
         m = (1000 × n_A) / (n_B × M_B)

Now, from χ_A:
    n_A/n_B = χ_A / χ_B = χ_A / (1 - χ_A)

Therefore:
    m = (1000 × χ_A) / ((1 - χ_A) × M_B)

where M_B = molar mass of SOLVENT (not solute!)
```

#### The Master Formula: χ → Molality

```
            1000 × χ_solute
m = ──────────────────────────────
     (1 - χ_solute) × M_solvent

where M_solvent is in g/mol
```

#### Solved Example 4.7
**Q:** The mole fraction of glucose in an aqueous solution is 0.02. Find the molality of the solution. 🟡 ⭐

**Solution:**
```
Given: χ_glucose = 0.02, M_water = 18 g/mol

    m = (1000 × χ_solute) / ((1 - χ_solute) × M_solvent)
    m = (1000 × 0.02) / ((1 - 0.02) × 18)
    m = 20 / (0.98 × 18)
    m = 20 / 17.64
    m = 1.134 mol/kg

Answer: m ≈ 1.13 mol/kg (or 1.13 m)
```

> **Why this works:** We've combined the mole fraction definition with the molality definition, eliminating n_A and n_B individually. The result only needs χ and molar mass of solvent.

#### Reverse: Molality → χ

```
Rearranging:
    χ_solute = (m × M_solvent) / (1000 + m × M_solvent)
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| 4.7a | χ_urea = 0.05 in an aqueous solution. Find molality. (M_water = 18) ⭐ | 🟡 |
| 4.7b | The molality of a sucrose solution is 0.5 m. Find χ_sucrose. (M_water = 18) | 🟡 |
| 4.7c | χ_NaCl = 0.1 in water. Find (a) molality (b) mass of NaCl in 500 g of water. (M_NaCl = 58.5, M_water = 18) ⭐ | 🔴 |
| 4.7d | A solution has molality 2 m with solvent methanol (M = 32). Find χ_solute. | 🟡 |
| 4.7e | An aqueous solution precisely has χ_solute = 0.04. Calculate exactly its molality. (M_water = 18) ⭐ | 🟡 |
| 4.7f | The molality of an aqueous glucose solution is exactly 1.5 m. Find χ_glucose. (M_water = 18) | 🟡 |
| 4.7g | In purely ethanol solvent (M = 46), determine the expected molality if χ_solute = 0.08. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**4.7a:**
- **Given:** $\chi_{urea} = 0.05$, aqueous ($M_{water} = 18$)
- **Calculation:** $m = \frac{1000 \cdot \chi_{solute}}{(1-\chi_{solute}) \cdot M_{solvent}} = \frac{1000 \cdot 0.05}{0.95 \cdot 18} = \frac{50}{17.1}$.
- **Final Answer:** $m \approx 2.92$ mol/kg

**4.7b:**
- **Given:** $m = 0.5$ mol/kg, $M_{water} = 18$
- **Calculation:** $\chi_{sucrose} = \frac{m \cdot M_{solvent}}{1000 + m \cdot M_{solvent}} = \frac{0.5 \cdot 18}{1000 + 0.5 \cdot 18} = \frac{9}{1009}$.
- **Final Answer:** $\chi_{sucrose} \approx 0.0089$

**4.7c:**
- **Given:** $\chi_{NaCl} = 0.1$, $M_{water} = 18$, $M_{NaCl} = 58.5$
- **Calculation:** (a) $m = \frac{1000 \cdot 0.1}{0.9 \cdot 18} = \frac{100}{16.2} \approx 6.17$ mol/kg. (b) For $500$ g water, moles of $NaCl = m \cdot 0.5$ kg $= 6.173 \cdot 0.5 = 3.086$ mol. Mass $= 3.086 \cdot 58.5 \approx 180.5$ g.
- **Final Answer:** (a) $6.17$ m, (b) $180.5$ g

**4.7d:**
- **Given:** $m = 2$ mol/kg, $M_{methanol} = 32$
- **Calculation:** $\chi_{solute} = \frac{m \cdot M_{solvent}}{1000 + m \cdot M_{solvent}} = \frac{2 \cdot 32}{1000 + 2 \cdot 32} = \frac{64}{1064}$.
- **Final Answer:** $\chi_{solute} \approx 0.0602$

**4.7e:**
- **Given:** $\chi_{solute} = 0.04$, aqueous ($M_{water} = 18$)
- **Calculation:** $m = \frac{1000 \cdot 0.04}{0.96 \cdot 18} = \frac{40}{17.28}$.
- **Final Answer:** $m \approx 2.315$ mol/kg

**4.7f:**
- **Given:** $m = 1.5$ mol/kg, $M_{water} = 18$
- **Calculation:** $\chi_{glucose} = \frac{1.5 \cdot 18}{1000 + 1.5 \cdot 18} = \frac{27}{1027}$.
- **Final Answer:** $\chi_{glucose} \approx 0.0263$

**4.7g:**
- **Given:** $\chi_{solute} = 0.08$, ethanol solvent ($M = 46$)
- **Calculation:** $m = \frac{1000 \cdot 0.08}{0.92 \cdot 46} = \frac{80}{42.32}$.
- **Final Answer:** $m \approx 1.89$ mol/kg

</details>

---

### Type 8: χ → Molarity Conversion (requires density) ⭐⭐

**The Pattern:** Converting mole fraction to molarity requires density because molarity uses **volume**, and you need density to connect mass to volume.

#### Derivation
```
Consider 1 mole of solution total (n_A + n_B = 1).
    n_A = χ_A,  n_B = χ_B = 1 - χ_A

Mass of this 1 mole of solution:
    mass = n_A × M_A + n_B × M_B = χ_A × M_A + (1 - χ_A) × M_B

Volume of this solution:
    V = mass / (density × 1000)    ← to get volume in litres

Molarity:
    M = n_A / V = χ_A / V
```

#### The Master Formula: χ → Molarity

```
              χ_A × d × 1000
M = ──────────────────────────────────
     χ_A × M_A + (1 - χ_A) × M_B

where d = density in g/mL, M_A = molar mass of solute, M_B = molar mass of solvent
```

#### Solved Example 4.8
**Q:** The mole fraction of ethanol in an ethanol-water solution is 0.2. The density of the solution is 0.96 g/mL. Find the molarity. (M_ethanol = 46, M_water = 18) 🔴 ⭐

**Solution:**
```
Given: χ_ethanol = 0.2, d = 0.96 g/mL, M_A = 46, M_B = 18

Step 1: Find average molar mass of solution
    M_avg = χ_A × M_A + χ_B × M_B
    M_avg = 0.2 × 46 + 0.8 × 18
    M_avg = 9.2 + 14.4 = 23.6 g/mol

Step 2: Apply formula
    M = (χ_A × d × 1000) / M_avg
    M = (0.2 × 0.96 × 1000) / 23.6
    M = 192 / 23.6
    M = 8.14 mol/L

Answer: Molarity ≈ 8.14 M
```

> **Why this needs density:** Molarity = moles/volume. Mole fraction gives us moles. But to find volume, we need mass ÷ density. That's why density is always required for any conversion involving molarity.

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| 4.8a | χ_glucose = 0.05 in aqueous solution, d = 1.04 g/mL. Find molarity. (M_glucose = 180, M_water = 18) ⭐ | 🔴 |
| 4.8b | An ethanol-water solution has χ_ethanol = 0.15, d = 0.97 g/mL. Find M. (M_ethanol = 46, M_water = 18) | 🔴 |
| 4.8c | Given: Molarity of a solution = 5 M, d = 1.2 g/mL, M_solute = 60, M_solvent = 18. Find χ_solute. (Reverse problem) ⭐ | 🔴 |
| 4.8d | An aqueous solution of urea (M=60) has χ_urea = 0.1. If its density is 1.15 g/mL, find its precise molarity. (M_water = 18) ⭐ | 🔴 |
| 4.8e | A methanol-water solution demonstrates χ_methanol = 0.25 and a density = 0.92 g/mL. Determine the molarity of methanol. (M_methanol = 32, M_water = 18) | 🔴 |
| 4.8f | Given an aqueous 2.5 M sugar solution (M=342) with a density of 1.25 g/mL, carefully find χ_sugar. ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**4.8a:**
- **Given:** $\chi_{glucose} = 0.05$, $d = 1.04$ g/mL, $M_A = 180$, $M_B = 18$
- **Calculation:** $M_{avg} = \chi_A M_A + \chi_B M_B = 0.05(180) + 0.95(18) = 9 + 17.1 = 26.1$ g/mol. $Molarity = \frac{\chi_A \cdot d \cdot 1000}{M_{avg}} = \frac{0.05 \cdot 1.04 \cdot 1000}{26.1} = \frac{52}{26.1}$.
- **Final Answer:** $Molarity \approx 1.99$ M

**4.8b:**
- **Given:** $\chi_{ethanol} = 0.15$, $d = 0.97$ g/mL, $M_A = 46$, $M_B = 18$
- **Calculation:** $M_{avg} = 0.15(46) + 0.85(18) = 6.9 + 15.3 = 22.2$. $Molarity = \frac{0.15 \cdot 0.97 \cdot 1000}{22.2} = \frac{145.5}{22.2}$.
- **Final Answer:** $Molarity \approx 6.55$ M

**4.8c:**
- **Given:** $M = 5$ M, $d = 1.2$ g/mL, $M_{solute} = 60$, $M_{solvent} = 18$
- **Calculation:** Assume $1$ L ($1000$ mL) solution. Mass of solution $= 1000 \cdot 1.2 = 1200$ g. Moles of solute $= 5$ mol. Mass of solute $= 5 \cdot 60 = 300$ g. Mass of solvent $= 1200 - 300 = 900$ g. Moles of solvent $= \frac{900}{18} = 50$ mol. $n_{total} = 5 + 50 = 55$ mol. $\chi_{solute} = \frac{5}{55} = \frac{1}{11}$.
- **Final Answer:** $\chi_{solute} \approx 0.0909$

**4.8d:**
- **Given:** $\chi_{urea} = 0.1$, $d = 1.15$ g/mL, $M_A = 60$, $M_B = 18$
- **Calculation:** $M_{avg} = 0.1(60) + 0.9(18) = 6 + 16.2 = 22.2$. $Molarity = \frac{0.1 \cdot 1.15 \cdot 1000}{22.2} = \frac{115}{22.2}$.
- **Final Answer:** $Molarity \approx 5.18$ M

**4.8e:**
- **Given:** $\chi_{methanol} = 0.25$, $d = 0.92$ g/mL, $M_A = 32$, $M_B = 18$
- **Calculation:** $M_{avg} = 0.25(32) + 0.75(18) = 8 + 13.5 = 21.5$. $Molarity = \frac{0.25 \cdot 0.92 \cdot 1000}{21.5} = \frac{230}{21.5}$.
- **Final Answer:** $Molarity \approx 10.7$ M

**4.8f:**
- **Given:** $M = 2.5$ M, sugar ($M = 342$), $d = 1.25$ g/mL
- **Calculation:** Assume $1$ L solution. Mass of solution $= 1250$ g. Moles of sugar $= 2.5$ mol. Mass of sugar $= 2.5 \cdot 342 = 855$ g. Mass of water $= 1250 - 855 = 395$ g. Moles of water $= \frac{395}{18} \approx 21.94$ mol. $n_{total} = 2.5 + 21.94 = 24.44$. $\chi_{sugar} = \frac{2.5}{24.44}$.
- **Final Answer:** $\chi_{sugar} \approx 0.102$

</details>

---

### Type 9: Temperature Independence — Proof and Reasoning

**The Pattern:** Conceptual — why is mole fraction unaffected by temperature?

#### Solved Example 4.9
**Q:** Explain why mole fraction is independent of temperature, while molarity is not. 🟡

**Solution:**
```
Temperature affects VOLUME, not MASS or NUMBER OF PARTICLES.

Mole fraction:
    χ = n_A / (n_A + n_B)
    
    n_A = number of moles = number of particles / Avogadro's number
    
    Heating a solution doesn't create or destroy particles.
    So n_A and n_B remain constant → χ remains constant. ✅

Molarity:
    M = n / V(in L)
    
    Heating a solution → volume increases (thermal expansion)
    → V increases → M decreases.
    
    So molarity IS temperature-dependent. ❌

Similarly:
    Molality: m = n / (mass of solvent in kg)
    Mass doesn't change with temperature → molality is T-independent ✅
    
    Mass percent: w/w% = mass ratio → T-independent ✅
    
    Volume percent: v/v% = volume ratio → T-dependent ❌
```

**Summary Table:**
| Concentration Term | T-Independent? | Why |
|-------------------|----------------|-----|
| Mole fraction (χ) | ✅ Yes | Based on moles (particles) |
| Molality (m) | ✅ Yes | Based on mass of solvent |
| Mass percent (w/w%) | ✅ Yes | Based on mass ratio |
| PPM (mass-based) | ✅ Yes | Based on mass ratio |
| Molarity (M) | ❌ No | Based on volume of solution |
| Volume percent (v/v%) | ❌ No | Based on volume ratio |

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| 4.9a | A solution has χ_solute = 0.1 at 25°C. What will be its mole fraction at 50°C? Justify. | 🟢 |
| 4.9b | Arrange the following in order of increasing sensitivity to temperature change: molality, molarity, mole fraction, mass percent. | 🟡 |
| 4.9c | Two identical aqueous solutions are sealed in rigid glass. One is cooled to 4°C, the other heated to 85°C. Compare their mole fractions. | 🟢 |
| 4.9d | Explain fundamentally why changing the pressure on a liquid solution does not theoretically alter the mole fraction of the dissolved solid solute. | 🟡 |
| 4.9e | A chemist argues that since molarity changes with temperature, the total moles in a solution must be changing. Use the definition of mole fraction to disprove this claim. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 9</summary>

**4.9a:**
- **Reasoning:** Mole fraction depends exclusively on the number of moles (particles), which do not change with temperature.
- **Final Answer:** $\chi_{solute} = 0.1$. It remains unchanged.

**4.9b:**
- **Reasoning:** Molality, mole fraction, and mass percent are all based on mass/moles and are entirely independent of temperature (sensitivity = 0). Molarity is based on volume and is temperature-sensitive.
- **Final Answer:** (Molality = Mole fraction = Mass percent) < Molarity

**4.9c:**
- **Reasoning:** Since mole fraction is independent of temperature, changing the temperature of identical sealed solutions does not change their particle ratios.
- **Final Answer:** Their mole fractions are identical.

**4.9d:**
- **Reasoning:** Mole fraction is determined by the number of moles ($n = \text{mass}/\text{molar mass}$). Changing external pressure does not create or destroy atoms/molecules. Although it may slightly compress the liquid (changing volume/molarity), the actual particle count ratio remains constant.
- **Final Answer:** Pressure does not change the number of particles (moles) of solute or solvent.

**4.9e:**
- **Reasoning:** Molarity ($M = \frac{n}{V}$) changes with temperature because the *volume* ($V$) expands or contracts. The number of moles ($n$) stays perfectly constant. Since mole fraction ($\chi = \frac{n_A}{n_A + n_B}$) relies only on moles, it proves that the particle counts are conserved even as the volume changing shifts the molarity.
- **Final Answer:** Molarity changes due to volume expansion/contraction, while moles remain constant, as evidenced by temperature-independent mole fraction.

</details>

---

### Type 10: Vapour Pressure Using Raoult's Law (Preview) ⭐⭐

**The Pattern:** Raoult's Law connects mole fraction to vapour pressure. This is a preview of the Solutions chapter's colligative properties.

#### Raoult's Law
```
P_solution = χ_solvent × P°_solvent

where:
    P_solution = vapour pressure of the solution
    P°_solvent = vapour pressure of PURE solvent
    χ_solvent = mole fraction of solvent in solution
```

#### Relative Lowering of Vapour Pressure
```
(P° - P) / P° = χ_solute

Relative lowering of VP = mole fraction of (non-volatile) solute
```

#### Solved Example 4.10
**Q:** The vapour pressure of pure water at 25°C is 23.8 mmHg. A solution is prepared by dissolving 18 g of glucose (M = 180) in 178.2 g of water (M = 18). Find: (a) mole fraction of glucose (b) vapour pressure of the solution (c) lowering of vapour pressure. 🟡 ⭐

**Solution:**
```
Step 1: Calculate moles
    n_glucose = 18/180 = 0.1 mol
    n_water = 178.2/18 = 9.9 mol

Step 2: Mole fractions
    χ_glucose = 0.1/(0.1 + 9.9) = 0.1/10 = 0.01
    χ_water = 9.9/10 = 0.99

Step 3: Apply Raoult's Law
    P_solution = χ_water × P°_water
    P_solution = 0.99 × 23.8 = 23.562 mmHg

Step 4: Lowering of VP
    ΔP = P° - P = 23.8 - 23.562 = 0.238 mmHg

    Verify: ΔP/P° = 0.238/23.8 = 0.01 = χ_glucose ✅

Answer: (a) χ_glucose = 0.01  (b) P = 23.562 mmHg  (c) ΔP = 0.238 mmHg
```

> **Why this works:** Adding a non-volatile solute essentially reduces the fraction of surface occupied by solvent molecules. Fewer solvent molecules at the surface → lower vapour pressure. The reduction is directly proportional to how many of the "slots" are taken by solute → i.e., χ_solute.

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| 4.10a | P° of water = 23.8 mmHg at 25°C. χ_solute = 0.05. Find P_solution and ΔP. | 🟡 |
| 4.10b | A solution has VP = 22.5 mmHg and P° = 23.8 mmHg. Find χ_solute. ⭐ | 🟡 |
| 4.10c | 30 g of urea (M=60) is dissolved in 270 g of water (M=18). P° of water = 31.82 mmHg. Find VP of solution. ⭐ | 🟡 |
| 4.10d | The VP of a solution is 95% of pure solvent's VP. Find χ_solute and χ_solvent. | 🟢 |
| 4.10e | 6 g of a non-volatile solute is dissolved in 180 g of water. VP of solution = 23.4 mmHg, P° = 23.8 mmHg. Find the molar mass of the solute. ⭐⭐ | 🔴 |
| 4.10f | Pure ethanol has a vapour pressure of 45.0 mmHg. Adding a non-volatile solute drops the pressure to 38.0 mmHg. Find the mole fraction of the solute. | 🟡 |
| 4.10g | An aqueous solution contains 0.2 moles of non-volatile solid and 9.8 moles of water. If P° of water is 24.0 mmHg, find the vapour pressure of the solution. | 🟡 |
| 4.10h | The relative lowering of vapour pressure for an aqueous solution is 0.04. Calculate the precise molality of the solution. (M_water = 18) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 10</summary>

**4.10a:**
- **Given:** $P^\circ = 23.8$ mmHg, $\chi_{solute} = 0.05$
- **Calculation:** $\Delta P / P^\circ = \chi_{solute} \Rightarrow \Delta P = 0.05 \cdot 23.8 = 1.19$ mmHg. $P_{solution} = P^\circ - \Delta P = 23.8 - 1.19 = 22.61$ mmHg.
- **Final Answer:** $P_{solution} = 22.61$ mmHg, $\Delta P = 1.19$ mmHg

**4.10b:**
- **Given:** $P_{solution} = 22.5$ mmHg, $P^\circ = 23.8$ mmHg
- **Calculation:** $\Delta P = 23.8 - 22.5 = 1.3$ mmHg. $\chi_{solute} = \frac{\Delta P}{P^\circ} = \frac{1.3}{23.8}$.
- **Final Answer:** $\chi_{solute} \approx 0.0546$

**4.10c:**
- **Given:** $m_{urea} = 30$ g ($M=60$), $m_{water} = 270$ g ($M=18$), $P^\circ = 31.82$ mmHg
- **Calculation:** $n_{urea} = \frac{30}{60} = 0.5$ mol. $n_{water} = \frac{270}{18} = 15$ mol. $\chi_{water} = \frac{15}{15.5} = \frac{30}{31}$. $P_{solution} = \chi_{water} \cdot P^\circ = \frac{30}{31} \cdot 31.82 = 30.79$ mmHg.
- **Final Answer:** $P_{solution} \approx 30.79$ mmHg

**4.10d:**
- **Given:** $P_{solution} = 0.95 P^\circ$
- **Calculation:** $\frac{P_{solution}}{P^\circ} = \chi_{solvent} \Rightarrow \chi_{solvent} = 0.95$. $\chi_{solute} = 1 - 0.95 = 0.05$.
- **Final Answer:** $\chi_{solute} = 0.05, \chi_{solvent} = 0.95$

**4.10e:**
- **Given:** $m_{solute} = 6$ g, $m_{water} = 180$ g, $P = 23.4$ mmHg, $P^\circ = 23.8$ mmHg
- **Calculation:** $\frac{\Delta P}{P^\circ} = \frac{0.4}{23.8} \approx 0.0168$. Also $\chi_{solute} = \frac{n_A}{n_A + n_B}$. $n_B = \frac{180}{18} = 10$ mol. For dilute solutions, $\chi_A \approx \frac{n_A}{n_B}$ or exact: $\frac{0.4}{23.8} = \frac{n_A}{n_A + 10} \Rightarrow 0.4(n_A + 10) = 23.8 n_A \Rightarrow 4 = 23.4 n_A \Rightarrow n_A = \frac{4}{23.4} \approx 0.1709$ mol. $M = \frac{mass}{moles} = \frac{6}{0.1709}$.
- **Final Answer:** $M \approx 35.1$ g/mol

**4.10f:**
- **Given:** $P^\circ = 45.0$ mmHg, $P = 38.0$ mmHg
- **Calculation:** $\Delta P = 45.0 - 38.0 = 7.0$ mmHg. $\chi_{solute} = \frac{\Delta P}{P^\circ} = \frac{7.0}{45.0}$.
- **Final Answer:** $\chi_{solute} \approx 0.156$

**4.10g:**
- **Given:** $n_{solute} = 0.2$, $n_{water} = 9.8$, $P^\circ = 24.0$ mmHg
- **Calculation:** $\chi_{water} = \frac{9.8}{0.2 + 9.8} = \frac{9.8}{10} = 0.98$. $P = \chi_{water} \cdot P^\circ = 0.98 \cdot 24.0 = 23.52$ mmHg.
- **Final Answer:** $P = 23.52$ mmHg

**4.10h:**
- **Given:** Relative lowering $\frac{\Delta P}{P^\circ} = 0.04$, $M_{water} = 18$
- **Calculation:** $\chi_{solute} = \frac{\Delta P}{P^\circ} = 0.04$. $m = \frac{1000 \cdot \chi_{solute}}{(1-\chi_{solute}) \cdot M_{solvent}} = \frac{1000 \cdot 0.04}{0.96 \cdot 18} = \frac{40}{17.28}$.
- **Final Answer:** $m \approx 2.31$ mol/kg

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 4.M5 | 5 g of a non-volatile, non-electrolyte solute is dissolved in 100 g of water. The VP of the solution is 17.7 mmHg at 20°C (P° = 17.8 mmHg). Find the molar mass of the solute. | T10 + T2 (reverse) | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**4.M1:**
- **Given:** $m_{ethanol} = 9.2$ g ($M=46$), $m_{water} = 36$ g ($M=18$), $P^\circ = 23.8$ mmHg
- **Calculation:** $n_{ethanol} = \frac{9.2}{46} = 0.2$ mol. $n_{water} = \frac{36}{18} = 2.0$ mol. $n_{total} = 2.2$. 
  (a) $\chi_{ethanol} = \frac{0.2}{2.2} = \frac{1}{11} \approx 0.0909$.
  (b) $m = \frac{n_{solute}}{m_{solvent\_kg}} = \frac{0.2}{0.036} = 5.55$ mol/kg.
  (c) $\chi_{water} = \frac{2.0}{2.2} = \frac{10}{11} \approx 0.909$. $P = \chi_{water} P^\circ = \frac{10}{11} \cdot 23.8 \approx 21.64$ mmHg.
- **Final Answer:** (a) $\approx 0.091$, (b) $5.55$ m, (c) $\approx 21.64$ mmHg

**4.M2:**
- **Given:** $\chi_{O_2} = 0.21$, $P_{total} = 5$ atm, binary with $N_2$, $n_{total} = 10$
- **Calculation:**
  (a) $P_{O_2} = \chi_{O_2} P_{total} = 0.21 \cdot 5 = 1.05$ atm.
  (b) $\chi_{N_2} = 1 - 0.21 = 0.79$. $P_{N_2} = 0.79 \cdot 5 = 3.95$ atm.
  (c) $n_{O_2} = 0.21 \cdot 10 = 2.1$ mol. $n_{N_2} = 0.79 \cdot 10 = 7.9$ mol.
- **Final Answer:** (a) $1.05$ atm, (b) $\chi_{N_2} = 0.79, P = 3.95$ atm, (c) $n_{O_2} = 2.1, n_{N_2} = 7.9$ mol

**4.M3:**
- **Given:** $m = 2.78$, $NaCl$ ($M=58.5$), water ($M=18$), $d = 1.08$ g/mL
- **Calculation:**
  (a) $\chi_{solute} = \frac{2.78 \cdot 18}{1000 + 2.78 \cdot 18} = \frac{50.04}{1050.04} \approx 0.0476$.
  (b) Take $1000$ g water. Mass of solution $= 1000 + 2.78 \cdot 58.5 = 1000 + 162.63 = 1162.63$ g. Volume $= \frac{1162.63}{1.08} \approx 1076.5$ mL $= 1.0765$ L. $M = \frac{2.78}{1.0765} \approx 2.58$ M.
- **Final Answer:** (a) $\chi \approx 0.0476$, (b) $M \approx 2.58$ M

**4.M4:**
- **Given:** $\chi_A = 0.1$, $M_A = 100$, $M_{water} = 18$, $d = 1.05$
- **Calculation:**
  (a) $m = \frac{1000 \cdot 0.1}{0.9 \cdot 18} = \frac{100}{16.2} \approx 6.17$ m.
  (b) $M_{avg} = 0.1(100) + 0.9(18) = 10 + 16.2 = 26.2$. $M = \frac{0.1 \cdot 1.05 \cdot 1000}{26.2} = \frac{105}{26.2} \approx 4.01$ M.
  (c) From 1 mole solution: mass of A $= 0.1 \cdot 100 = 10$ g. Total mass $= 26.2$ g. Mass $\% = \frac{10}{26.2} \cdot 100 \approx 38.17\%$.
- **Final Answer:** (a) $6.17$ m, (b) $4.01$ M, (c) $38.17\%$

**4.M5:**
- **Given:** $m_{solute} = 5$ g, $m_{water} = 100$ g, $P = 17.7$ mmHg, $P^\circ = 17.8$ mmHg
- **Calculation:** $\frac{\Delta P}{P^\circ} = \frac{17.8 - 17.7}{17.8} = \frac{0.1}{17.8} \approx 0.005618 = \chi_{solute}$. $n_{water} = \frac{100}{18} = 5.556$ mol. Using dilute approx: $\chi_{solute} = \frac{n_{solute}}{n_{water}} \Rightarrow n_{solute} = 0.005618 \cdot 5.556 = 0.0312$ mol. $M = \frac{mass}{moles} = \frac{5}{0.0312} \approx 160$ g/mol.
- **Final Answer:** $M \approx 160$ g/mol

</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 4.B4 | A solution of glucose in water has concentration 10% by mass. Find (a) mole fraction of glucose (b) molality. (M_glucose = 180) | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**4.B1:**
- **Given:** $30\%$ mass benzene ($M=78$) in $CCl_4$ ($M=154$)
- **Calculation:** Assume $100$ g solution. Mass of benzene $= 30$ g. Mass of $CCl_4 = 70$ g. $n_{benzene} = \frac{30}{78} \approx 0.385$ mol. $n_{CCl_4} = \frac{70}{154} \approx 0.455$ mol. $n_{total} = 0.385 + 0.455 = 0.840$. $\chi_{benzene} = \frac{0.385}{0.840}$.
- **Final Answer:** $\chi_{benzene} \approx 0.458$

**4.B2:**
- **Given:** $\chi_{solute} = 0.1$, aqueous ($M=18$)
- **Calculation:** $m = \frac{1000 \cdot \chi_{solute}}{(1-\chi_{solute}) \cdot M_{solvent}} = \frac{1000 \cdot 0.1}{0.9 \cdot 18} = \frac{100}{16.2}$.
- **Final Answer:** $m \approx 6.17$ mol/kg

**4.B3:**
- **Given:** $98\%$ $H_2SO_4$ ($M=98$) by mass in water ($M=18$)
- **Calculation:** Assume $100$ g solution. Mass $H_2SO_4 = 98$ g. Mass water $= 2$ g. $n_{H_2SO_4} = \frac{98}{98} = 1$ mol. $n_{water} = \frac{2}{18} = \frac{1}{9} \approx 0.111$ mol. $n_{total} = 1 + 0.111 = 1.111$ mol. $\chi_{H_2SO_4} = \frac{1}{1.111} = 0.9$.
- **Final Answer:** $\chi_{H_2SO_4} = 0.9$

**4.B4:**
- **Given:** $10\%$ mass glucose ($M=180$) in water
- **Calculation:** Assume $100$ g solution. Mass glucose $= 10$ g. Mass water $= 90$ g. $n_{glucose} = \frac{10}{180} = \frac{1}{18} \approx 0.0556$ mol. $n_{water} = \frac{90}{18} = 5$ mol. $n_{total} = 5.0556$ mol. 
  (a) $\chi_{glucose} = \frac{0.0556}{5.0556} \approx 0.011$.
  (b) $m = \frac{n_{solute}}{m_{solvent\_kg}} = \frac{\frac{1}{18}}{0.090} = \frac{1}{1.62} \approx 0.617$ mol/kg.
- **Final Answer:** (a) $\chi \approx 0.011$, (b) $m \approx 0.617$ m

</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 4.J5 | Given: 10% (w/w) NaOH solution, d = 1.2 g/mL, M = 40. Find (a) mole fraction of NaOH (b) molality (c) molarity. (Multi-step interconversion preview.) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**4.J1:**
- **Given:** $3\%$ urea ($M=60$), $7.45\%$ KCl ($M=74.5$) in water
- **Calculation:** Assume $100$ g solution. Mass urea $= 3$ g. Mass KCl $= 7.45$ g. Mass water $= 100 - 3 - 7.45 = 89.55$ g. $n_{urea} = \frac{3}{60} = 0.05$ mol. $n_{KCl} = \frac{7.45}{74.5} = 0.1$ mol. $n_{water} = \frac{89.55}{18} \approx 4.975$ mol. $n_{total} = 0.05 + 0.1 + 4.975 = 5.125$ mol. $\chi_{urea} = \frac{0.05}{5.125}$.
- **Final Answer:** $\chi_{urea} \approx 0.00976$

**4.J2:**
- **Given:** $\chi_{solute} = 0.1$, $d = 1.2$ g/mL, $M_{solute} = 100$, $M_{water} = 18$
- **Calculation:** $M_{avg} = 0.1(100) + 0.9(18) = 10 + 16.2 = 26.2$. $M = \frac{0.1 \cdot 1.2 \cdot 1000}{26.2} = \frac{120}{26.2}$.
- **Final Answer:** $Molarity \approx 4.58$ M

**4.J3:**
- **Given:** $M_{avg} = 10$, $M_{He} = 4$, $M_{Ne} = 20$
- **Calculation:** $M_{avg} = \chi_{He} M_{He} + \chi_{Ne} M_{Ne}$. $\chi_{He} \cdot 4 + (1 - \chi_{He}) \cdot 20 = 10 \Rightarrow 4 \chi_{He} + 20 - 20\chi_{He} = 10 \Rightarrow 16\chi_{He} = 10 \Rightarrow \chi_{He} = \frac{10}{16} = 0.625$. $\chi_{Ne} = 1 - 0.625 = 0.375$.
- **Final Answer:** $\chi_{He} = 0.625, \chi_{Ne} = 0.375$

**4.J4:**
- **Given:** $100$ g A ($M=40$), $1000$ g B ($M=80$). $P^\circ_A = 400$, $P^\circ_B = 200$
- **Calculation:** $n_A = \frac{100}{40} = 2.5$ mol. $n_B = \frac{1000}{80} = 12.5$ mol. $n_{total} = 15$ mol. $\chi_A = \frac{2.5}{15} = \frac{1}{6}$. $\chi_B = \frac{12.5}{15} = \frac{5}{6}$. $P_{total} = \chi_A P^\circ_A + \chi_B P^\circ_B = \frac{1}{6}(400) + \frac{5}{6}(200) = \frac{400 + 1000}{6} = \frac{1400}{6}$.
- **Final Answer:** $P_{total} \approx 233.3$ mmHg

**4.J5:**
- **Given:** $10\%$ NaOH ($M=40$), $d = 1.2$ g/mL
- **Calculation:** Assume $100$ g solution $\Rightarrow 10$ g NaOH, $90$ g water. 
  (a) $n_{NaOH} = \frac{10}{40} = 0.25$ mol. $n_{water} = \frac{90}{18} = 5$ mol. $\chi_{NaOH} = \frac{0.25}{5.25} = \frac{1}{21} \approx 0.0476$.
  (b) $m = \frac{0.25}{0.090} \approx 2.78$ m.
  (c) $V$ of solution $= \frac{100}{1.2} = 83.33$ mL $= 0.08333$ L. $M = \frac{0.25}{0.08333} = 3.0$ M.
- **Final Answer:** (a) $\approx 0.0476$, (b) $2.78$ m, (c) $3.0$ M

</details>

---

## Key Takeaways from Chapter 4

```
┌─────────────────────────────────────────────────────────────┐
│                 MOLE FRACTION SUMMARY                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Formula: χ_A = n_A / (n_A + n_B)                           │
│                                                              │
│  Golden Rule: χ_A + χ_B = 1  (always, for binary)          │
│                                                              │
│  Properties:                                                 │
│    • Dimensionless (no units)                               │
│    • Always between 0 and 1                                 │
│    • Temperature INDEPENDENT ✅                              │
│                                                              │
│  Key Conversions:                                            │
│    χ → m:  m = (1000 × χ_solute) / ((1 - χ) × M_solvent)  │
│    χ → M:  Requires density (density always needed for M)   │
│                                                              │
│  Gas Mixtures:                                               │
│    χ_A = P_A / P_total  (Dalton's Law)                      │
│                                                              │
│  Raoult's Law (Preview):                                     │
│    P_solution = χ_solvent × P°                              │
│    ΔP/P° = χ_solute                                         │
│                                                              │
│  Denominator trap:                                           │
│    χ = n_solute / n_TOTAL (NOT n_solvent!)                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 3 — PPM](./03-ppm.md) | [Chapter 5 — Molality →](./05-molality.md)*
