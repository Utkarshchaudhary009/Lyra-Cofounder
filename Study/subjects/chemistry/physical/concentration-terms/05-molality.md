# Chapter 5: Molality (m)
## Part II: Enter the Mole

---

## 🎯 Stage 1: The Core Idea

### What is Molality?

Molality measures how many moles of solute are dissolved per kilogram of **solvent** (not solution!).

> **Analogy:** Imagine you're making lemonade. Molality asks: "How many lemons did you squeeze per kilogram of water?" It doesn't care about the total weight of the lemonade (water + lemon juice + sugar) — only the water.

### Why Molality, Not Just Molarity?

| Feature | Molality (m) | Molarity (M) |
|---------|-------------|-------------|
| Denominator | Mass of solvent (kg) | Volume of solution (L) |
| Temperature effect | **Independent** ✅ | Dependent ❌ |
| Measured with | Balance (mass) | Volumetric flask (volume) |
| Used for | Colligative properties | Lab work, stoichiometry |

> **Why temperature matters:** When you heat a solution, it expands — volume increases but mass stays the same. Molarity changes; molality doesn't. For colligative properties (boiling point elevation, freezing point depression, osmotic pressure), you need a concentration that doesn't drift with temperature. That's molality.

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
       Moles of solute           n_solute
m = ────────────────────── = ─────────────────
     Mass of solvent (kg)    W_solvent (in kg)
```

### Unpacking the Formula

```
         mass of solute / molar mass of solute
m = ──────────────────────────────────────────────
              mass of solvent / 1000

         W_solute × 1000
m = ──────────────────────────
     M_solute × W_solvent(g)

where:
    W_solute = mass of solute in grams
    M_solute = molar mass of solute in g/mol
    W_solvent = mass of SOLVENT in grams (NOT solution!)
```

### Critical Distinction

```
⚠️ SOLVENT ≠ SOLUTION

Mass of solution = Mass of solute + Mass of solvent
W_solution = W_solute + W_solvent
W_solvent = W_solution - W_solute

MOLALITY uses mass of SOLVENT (denominator)
Students CONSTANTLY confuse this with mass of SOLUTION
```

### Units

```
m = mol / kg = mol·kg⁻¹

Read as: "moles per kilogram of solvent"
Symbol: lowercase 'm' or 'mol/kg' or 'mol kg⁻¹'
```

### Temperature Dependence

Molality is **temperature-independent** ✅

Why? Mass of solvent doesn't change with temperature. Unlike volume (which expands/contracts), mass is invariant under temperature changes.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given mass of solute, molar mass, mass of solvent → find m

**The Pattern:** All three quantities are directly provided → plug into formula.

#### Solved Example 5.1
**Q:** 6 g of urea (NH₂CONH₂, M = 60 g/mol) is dissolved in 500 g of water. Find the molality of the solution. 🟢

**Solution:**
```
Step 1: Calculate moles of solute
    n_urea = mass / molar mass = 6/60 = 0.1 mol

Step 2: Convert mass of solvent to kg
    W_solvent = 500 g = 0.5 kg

Step 3: Calculate molality
    m = n/W = 0.1/0.5 = 0.2 mol/kg

Answer: m = 0.2 mol/kg (or 0.2 m)
```

> **Why this works:** Straightforward substitution. The only trap is forgetting to convert grams to kilograms in the denominator.

> **⚠️ Common Mistake:** Using mass of SOLUTION instead of mass of SOLVENT. In dilute solutions these are nearly equal, but in concentrated solutions, the difference is significant.

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 5.1a | 18 g of glucose (M = 180) in 100 g of water. Find m. | 🟢 |
| 5.1b | 11.7 g of NaCl (M = 58.5) in 250 g of water. Find m. | 🟢 |
| 5.1c | 4.9 g of H₂SO₄ (M = 98) in 500 g of water. Find m. | 🟢 |
| 5.1d | 36 g of glucose (M = 180) in 1 kg of water. Find m. ⭐ | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**5.1a**
*   **Given:** Mass of glucose ($W_{solute}$) = 18 g, $M_{solute}$ = 180 g/mol, Mass of water ($W_{solvent}$) = 100 g.
*   **Step 1:** Calculate moles of glucose ($n$).
    *   $n = \frac{18 \text{ g}}{180 \text{ g/mol}} = 0.1 \text{ mol}$
*   **Step 2:** Convert mass of solvent to kg.
    *   $W_{solvent} = \frac{100 \text{ g}}{1000} = 0.1 \text{ kg}$
*   **Step 3:** Calculate molality ($m$).
    *   $m = \frac{n}{W_{solvent \text{ (in kg)}}} = \frac{0.1 \text{ mol}}{0.1 \text{ kg}} = 1 \text{ m}$
*   **Final Answer:** $m = 1 \text{ mol/kg}$

**5.1b**
*   **Given:** Mass of NaCl = 11.7 g, $M_{NaCl}$ = 58.5 g/mol, $W_{solvent}$ = 250 g = 0.25 kg.
*   **Step 1:** Calculate moles of NaCl.
    *   $n = \frac{11.7}{58.5} = 0.2 \text{ mol}$
*   **Step 2:** Calculate molality.
    *   $m = \frac{0.2 \text{ mol}}{0.25 \text{ kg}} = 0.8 \text{ m}$
*   **Final Answer:** $m = 0.8 \text{ mol/kg}$

**5.1c**
*   **Given:** Mass of H₂SO₄ = 4.9 g, $M_{H2SO4}$ = 98 g/mol, $W_{solvent}$ = 500 g = 0.5 kg.
*   **Step 1:** Calculate moles of H₂SO₄.
    *   $n = \frac{4.9}{98} = 0.05 \text{ mol}$
*   **Step 2:** Calculate molality.
    *   $m = \frac{0.05 \text{ mol}}{0.5 \text{ kg}} = 0.1 \text{ m}$
*   **Final Answer:** $m = 0.1 \text{ mol/kg}$

**5.1d**
*   **Given:** Mass of glucose = 36 g, $M_{glucose}$ = 180 g/mol, $W_{solvent}$ = 1 kg.
*   **Step 1:** Calculate moles of glucose.
    *   $n = \frac{36}{180} = 0.2 \text{ mol}$
*   **Step 2:** Calculate molality. *Note: Solvent is already in kg*.
    *   $m = \frac{0.2 \text{ mol}}{1 \text{ kg}} = 0.2 \text{ m}$
*   **Final Answer:** $m = 0.2 \text{ mol/kg}$

</details>

---

### Type 2: Reverse — Given m → find mass of solute needed

**The Pattern:** Molality is given → calculate how much solute to add to a known mass of solvent.

#### Solved Example 5.2
**Q:** How many grams of NaOH (M = 40) must be dissolved in 200 g of water to prepare a 2.5 m solution? 🟡

**Solution:**
```
Step 1: Find moles of solute needed
    m = n / W_solvent(kg)
    2.5 = n / 0.2
    n = 2.5 × 0.2 = 0.5 mol

Step 2: Convert to mass
    mass = n × M = 0.5 × 40 = 20 g

Answer: 20 g of NaOH
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 5.2a | Find the mass of glucose (M = 180) required to prepare a 0.5 m solution using 1 kg of water. | 🟢 |
| 5.2b | How many grams of urea (M = 60) are needed to make a 1.5 m solution in 400 g of water? | 🟡 |
| 5.2c | A 0.1 m solution of KCl (M = 74.5) is prepared using 2 kg of water. Find the mass of KCl required. | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**5.2a**
*   **Given:** Molality ($m$) = 0.5 m, Mass of solvent ($W_{solvent}$) = 1 kg, $M_{glucose}$ = 180 g/mol.
*   **Step 1:** Calculate moles of solute required.
    *   $m = \frac{n}{W_{solvent \text{ (in kg)}}}$
    *   $0.5 = \frac{n}{1} \implies n = 0.5 \text{ mol}$
*   **Step 2:** Calculate mass of glucose.
    *   $\text{Mass} = n \times M = 0.5 \text{ mol} \times 180 \text{ g/mol} = 90 \text{ g}$
*   **Final Answer:** 90 g of glucose

**5.2b**
*   **Given:** Molality ($m$) = 1.5 m, Mass of solvent = 400 g = 0.4 kg, $M_{urea}$ = 60 g/mol.
*   **Step 1:** Calculate moles of urea needed.
    *   $1.5 = \frac{n}{0.4} \implies n = 1.5 \times 0.4 = 0.6 \text{ mol}$
*   **Step 2:** Calculate mass of urea.
    *   $\text{Mass} = 0.6 \text{ mol} \times 60 \text{ g/mol} = 36 \text{ g}$
*   **Final Answer:** 36 g of urea

**5.2c**
*   **Given:** Molality ($m$) = 0.1 m, Mass of solvent = 2 kg, $M_{KCl}$ = 74.5 g/mol.
*   **Step 1:** Calculate moles of KCl needed.
    *   $0.1 = \frac{n}{2} \implies n = 0.2 \text{ mol}$
*   **Step 2:** Calculate mass of KCl.
    *   $\text{Mass} = 0.2 \text{ mol} \times 74.5 \text{ g/mol} = 14.9 \text{ g}$
*   **Final Answer:** 14.9 g of KCl

</details>

---

### Type 3: Given m → find mass of solvent if moles of solute known

**The Pattern:** Reverse of the reverse — find how much solvent is needed.

#### Solved Example 5.3
**Q:** You have 0.3 mol of sucrose. How much water (in grams) do you need to make a 0.6 m solution? 🟡

**Solution:**
```
    m = n / W_solvent(kg)
    0.6 = 0.3 / W
    W = 0.3 / 0.6 = 0.5 kg = 500 g

Answer: 500 g of water
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 5.3a | 0.5 mol of NaCl needs to become a 2 m solution. How much water? | 🟢 |
| 5.3b | 0.1 mol of glucose must give m = 0.25. Find mass of water needed. | 🟡 |
| 5.3c | A pharmacist has 0.05 mol of a drug and needs m = 0.1. How much solvent? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**5.3a**
*   **Given:** Moles of NaCl ($n$) = 0.5 mol, Molality ($m$) = 2 m.
*   **Step 1:** Use molality formula to find mass of solvent in kg.
    *   $m = \frac{n}{W_{solvent \text{ (in kg)}}}$
    *   $2 = \frac{0.5}{W} \implies W = \frac{0.5}{2} = 0.25 \text{ kg}$
*   **Step 2:** Convert kg to grams (if necessary).
    *   $0.25 \text{ kg} = 250 \text{ g}$
*   **Final Answer:** 250 g of water

**5.3b**
*   **Given:** Moles of glucose ($n$) = 0.1 mol, Molality ($m$) = 0.25 m.
*   **Step 1:** Calculate mass of solvent.
    *   $0.25 = \frac{0.1}{W} \implies W = \frac{0.1}{0.25} = 0.4 \text{ kg}$
*   **Step 2:** Convert to grams.
    *   $0.4 \text{ kg} = 400 \text{ g}$
*   **Final Answer:** 400 g of water

**5.3c**
*   **Given:** Moles of drug = 0.05 mol, Target molality = 0.1 m.
*   **Step 1:** Calculate mass of solvent.
    *   $0.1 = \frac{0.05}{W} \implies W = \frac{0.05}{0.1} = 0.5 \text{ kg}$
*   **Step 2:** Convert to grams.
    *   $0.5 \text{ kg} = 500 \text{ g}$
*   **Final Answer:** 500 g of solvent

</details>

---

### Type 4: Dissolving solid in water — given masses → find m

**The Pattern:** Same as Type 1, but the problem says "dissolve X grams in Y grams of water." The water IS the solvent.

#### Solved Example 5.4
**Q:** 5 g of NaCl (M = 58.5) is dissolved in 95 g of water. Find the molality. 🟢

**Solution:**
```
Step 1: n_NaCl = 5/58.5 = 0.0855 mol

Step 2: W_solvent = 95 g = 0.095 kg

Step 3: m = 0.0855/0.095 = 0.9 mol/kg

Answer: m ≈ 0.9 m
```

> **⚠️ Common Mistake:** Some students add solute + solvent to get "100 g" and use 100 as the denominator. NO! The denominator is only the solvent (95 g), not the solution (100 g). For molality, ALWAYS subtract solute from solution to get solvent weight.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 5.4a | 30 g of urea (M = 60) dissolved in 970 g of water. Find m. | 🟢 |
| 5.4b | 98 g of H₂SO₄ (M = 98) dissolved in 902 g of water. Find m. Note the mass of solution = 1000 g. | 🟡 |
| 5.4c | 4.5 g of glucose (M = 180) in 50 g of water. Find m. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**5.4a**
*   **Given:** Mass of urea = 30 g, $M_{urea}$ = 60 g/mol, Mass of water ($W_{solvent}$) = 970 g = 0.97 kg.
*   **Step 1:** Calculate moles of urea.
    *   $n = \frac{30}{60} = 0.5 \text{ mol}$
*   **Step 2:** Calculate molality.
    *   $m = \frac{0.5 \text{ mol}}{0.97 \text{ kg}} = 0.515 \text{ m}$
*   **Final Answer:** $m \approx 0.515 \text{ mol/kg}$

**5.4b**
*   **Given:** Mass of H₂SO₄ = 98 g, $M_{H2SO4}$ = 98 g/mol, Mass of water ($W_{solvent}$) = 902 g = 0.902 kg.
*   **Step 1:** Calculate moles of H₂SO₄.
    *   $n = \frac{98}{98} = 1 \text{ mol}$
*   **Step 2:** Calculate molality. Notice we use $W_{solvent}$ (902 g), NOT the mass of solution (1000 g).
    *   $m = \frac{1 \text{ mol}}{0.902 \text{ kg}} = 1.108 \text{ m}$
*   **Final Answer:** $m \approx 1.11 \text{ mol/kg}$

**5.4c**
*   **Given:** Mass of glucose = 4.5 g, $M_{glucose}$ = 180 g/mol, Mass of water = 50 g = 0.05 kg.
*   **Step 1:** Calculate moles of glucose.
    *   $n = \frac{4.5}{180} = 0.025 \text{ mol}$
*   **Step 2:** Calculate molality.
    *   $m = \frac{0.025 \text{ mol}}{0.05 \text{ kg}} = 0.5 \text{ m}$
*   **Final Answer:** $m = 0.5 \text{ mol/kg}$

</details>

---

### Type 5: Given w/w% → convert to molality ⭐

**The Pattern:** Mass percent is given → derive molality.

#### Derivation
```
Let w/w% = x%. Consider 100 g of solution.
    Mass of solute = x g
    Mass of solvent = (100 - x) g

    n_solute = x / M_solute

    m = n_solute / (mass of solvent in kg)
    m = (x / M_solute) / ((100 - x) / 1000)
    m = (x × 1000) / (M_solute × (100 - x))
```

#### The Master Formula: w/w% → Molality

```
            w/w% × 1000                    x × 1000
m = ──────────────────────── = ────────────────────────────
     M_solute × (100 - w/w%)    M_solute × (100 - x)
```

#### Solved Example 5.5
**Q:** Find the molality of a 10% (w/w) NaOH solution. (M_NaOH = 40) 🟡 ⭐

**Solution:**
```
Method 1: Using the formula
    m = (10 × 1000) / (40 × (100 - 10))
    m = 10000 / (40 × 90)
    m = 10000 / 3600
    m = 2.78 mol/kg

Method 2: From first principles (recommended for understanding)
    In 100 g of solution:
        Solute = 10 g    → n = 10/40 = 0.25 mol
        Solvent = 90 g   = 0.09 kg
    
    m = 0.25/0.09 = 2.78 mol/kg ✅

Answer: m = 2.78 mol/kg
```

> **Why this works:** w/w% gives us masses. From masses we can find moles and mass of solvent — exactly what molality needs.

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 5.5a | Find the molality of a 20% glucose (M=180) solution. | 🟡 |
| 5.5b | A solution is 5% urea (M=60) by mass. Find m. ⭐ | 🟡 |
| 5.5c | Commercial H₂SO₄ is 98% by mass (M=98). Find its molality. ⭐ | 🟡 |
| 5.5d | If w/w% = 50% for a solute of M = 100, find m. What's special about this result? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**5.5a**
*   **Given:** 20% (w/w) glucose, $M_{glucose}$ = 180 g/mol.
*   **Step 1:** Deconstruct the percentage.
    *   Assume 100 g of solution.
    *   Mass of solute ($W_{solute}$) = 20 g
    *   Mass of solvent ($W_{solvent}$) = 100 g - 20 g = 80 g = 0.08 kg
*   **Step 2:** Calculate moles of glucose.
    *   $n = \frac{20}{180} = 0.111 \text{ mol}$
*   **Step 3:** Calculate molality.
    *   $m = \frac{0.111 \text{ mol}}{0.08 \text{ kg}} = 1.388 \text{ m}$
    *   *Alternative Formula method:* $m = \frac{20 \times 1000}{180 \times (100 - 20)} = \frac{20000}{180 \times 80} = \frac{20000}{14400} = 1.388 \text{ m}$
*   **Final Answer:** $m = 1.39 \text{ mol/kg}$

**5.5b**
*   **Given:** 5% (w/w) urea, $M_{urea}$ = 60 g/mol.
*   **Step 1:** Assume 100 g solution.
    *   $W_{solute}$ = 5 g, $W_{solvent}$ = 95 g = 0.095 kg
*   **Step 2:** Calculate molality.
    *   Using formula: $m = \frac{x \times 1000}{M \times (100 - x)} = \frac{5 \times 1000}{60 \times (100 - 5)}$
    *   $m = \frac{5000}{60 \times 95} = \frac{5000}{5700} = 0.877 \text{ m}$
*   **Final Answer:** $m \approx 0.88 \text{ mol/kg}$

**5.5c**
*   **Given:** 98% (w/w) H₂SO₄, $M_{H2SO4}$ = 98 g/mol.
*   **Step 1:** Assume 100 g solution.
    *   $W_{solute}$ = 98 g, $W_{solvent}$ = 2 g = 0.002 kg
*   **Step 2:** Calculate moles of H₂SO₄.
    *   $n = \frac{98}{98} = 1 \text{ mol}$
*   **Step 3:** Calculate molality.
    *   $m = \frac{1 \text{ mol}}{0.002 \text{ kg}} = 500 \text{ m}$
*   **Final Answer:** $m = 500 \text{ mol/kg}$

**5.5d**
*   **Given:** 50% (w/w) solute, $M_{solute}$ = 100 g/mol.
*   **Step 1:** Assume 100 g solution.
    *   $W_{solute}$ = 50 g, $W_{solvent}$ = 50 g = 0.05 kg
*   **Step 2:** Calculate molality.
    *   $n = \frac{50}{100} = 0.5 \text{ mol}$
    *   $m = \frac{0.5 \text{ mol}}{0.05 \text{ kg}} = 10 \text{ m}$
*   **What's special?** At 50% (w/w), the mass of solute exactly equals the mass of solvent.
*   **Final Answer:** $m = 10 \text{ mol/kg}$

</details>

---

### Type 6: Given mole fraction → convert to molality ⭐

**The Pattern:** Uses the formula derived in Chapter 4, Type 7.

#### The Formula (from Chapter 4)

```
            1000 × χ_solute
m = ──────────────────────────────
     (1 - χ_solute) × M_solvent
```

#### Solved Example 5.6
**Q:** The mole fraction of urea in an aqueous solution is 0.018. Find the molality. (M_water = 18) 🟡

**Solution:**
```
    m = (1000 × 0.018) / ((1 - 0.018) × 18)
    m = 18 / (0.982 × 18)
    m = 18 / 17.676
    m = 1.018 mol/kg

Answer: m ≈ 1.02 mol/kg
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 5.6a | χ_glucose = 0.1 in water. Find molality. (M_water = 18) | 🟡 |
| 5.6b | χ_solute = 0.2 in ethanol (M = 46). Find molality. | 🟡 |
| 5.6c | Molality of a solution is 5 m (solvent = water). Find χ_solute. (Reverse) ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**5.6a**
*   **Given:** $\chi_{glucose} = 0.1$, Solvent = water ($M_{water} = 18$ g/mol).
*   **Step 1:** Use the $\chi$ to $m$ conversion formula.
    *   $m = \frac{1000 \times \chi_{solute}}{(1 - \chi_{solute}) \times M_{solvent}}$
    *   $m = \frac{1000 \times 0.1}{(1 - 0.1) \times 18} = \frac{100}{0.9 \times 18}$
    *   $m = \frac{100}{16.2} = 6.17 \text{ m}$
*   **Final Answer:** $m \approx 6.17 \text{ mol/kg}$

**5.6b**
*   **Given:** $\chi_{solute} = 0.2$, Solvent = ethanol ($M = 46$ g/mol).
*   **Step 1:** Use the $\chi$ to $m$ conversion formula.
    *   $m = \frac{1000 \times 0.2}{(1 - 0.2) \times 46} = \frac{200}{0.8 \times 46}$
    *   $m = \frac{200}{36.8} = 5.43 \text{ m}$
*   **Final Answer:** $m \approx 5.43 \text{ mol/kg}$

**5.6c**
*   **Given:** Molality ($m$) = 5 m, Solvent = water ($M = 18$ g/mol). Let $\chi_{solute} = x$.
*   **Step 1:** Re-arrange the formula or substitute directly.
    *   $5 = \frac{1000x}{(1 - x) \times 18}$
    *   $5 \times 18 \times (1 - x) = 1000x$
    *   $90 \times (1 - x) = 1000x$
    *   $90 - 90x = 1000x \implies 1090x = 90$
    *   $x = \frac{90}{1090} = 0.0825$
*   **Alternative logic:** 5 m means 5 mol solute in 1 kg (1000 g) water.
    *   Moles of water = $\frac{1000}{18} = 55.55$ mol
    *   $\chi_{solute} = \frac{5}{5 + 55.55} = \frac{5}{60.55} = 0.0825$
*   **Final Answer:** $\chi_{solute} \approx 0.0825$

</details>

---

### Type 7: Given Molarity + Density → Convert to Molality ⭐⭐⭐

**The Pattern:** This is the **most important conversion** in all of concentration terms. JEE loves this.

#### Derivation
```
Consider 1 L of solution.
    Moles of solute = M (by definition of molarity)
    Mass of solute = M × M_solute (grams)
    
    Mass of 1 L solution = d × 1000 (grams)  [d in g/mL, 1L = 1000 mL]
    
    Mass of solvent = mass of solution - mass of solute
                    = d × 1000 - M × M_solute (grams)
                    = (d × 1000 - M × M_solute) / 1000 (kg)
    
    Molality = M / mass of solvent(kg)
             = (M × 1000) / (d × 1000 - M × M_solute)
```

#### The Master Formula: Molarity → Molality

```
              M × 1000
m = ──────────────────────────────
     d × 1000 - M × M_solute

where:
    M = molarity (mol/L)
    d = density (g/mL)
    M_solute = molar mass of solute (g/mol)
```

#### Solved Example 5.7
**Q:** A 2 M NaCl solution has a density of 1.08 g/mL. Find its molality. (M_NaCl = 58.5) 🟡 ⭐⭐

**Solution:**
```
Step 1: Consider 1 L of solution
    Moles of NaCl = 2 mol
    Mass of NaCl = 2 × 58.5 = 117 g

Step 2: Find mass of solution (1 L)
    mass = d × V = 1.08 × 1000 = 1080 g

Step 3: Find mass of solvent
    W_solvent = 1080 - 117 = 963 g = 0.963 kg

Step 4: Calculate molality
    m = 2/0.963 = 2.077 mol/kg

Answer: m ≈ 2.08 mol/kg

Using the formula directly:
    m = (2 × 1000)/(1.08 × 1000 - 2 × 58.5) = 2000/963 = 2.077 ✅
```

> **Why this works:** The trick is thinking about "1 L of solution." That gives you moles of solute directly (from M). Density gives you the mass of that 1 L. Subtract solute mass → solvent mass. Done.

> **⚠️ Common Mistake:** Using "1 kg of solution" instead of "1 L of solution." While both approaches work, starting with 1 L is cleaner because molarity directly gives you moles for 1 L.

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| 5.7a | A 1 M H₂SO₄ solution has d = 1.065 g/mL. Find molality. (M = 98) ⭐ | 🟡 |
| 5.7b | 3 M glucose (M = 180), d = 1.12 g/mL. Find m. | 🟡 |
| 5.7c | 0.5 M urea (M = 60), d = 1.01 g/mL. Find m. | 🟡 |
| 5.7d | 18 M H₂SO₄, d = 1.84 g/mL. Find m. (M = 98) ⭐⭐ | 🔴 |
| 5.7e | A solution has m = 4 and d = 1.2 g/mL. Solute M = 80. Find molarity. (Reverse) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**5.7a**
*   **Given:** Molarity ($M$) = 1 M, $d = 1.065$ g/mL, $M_{H2SO4} = 98$ g/mol.
*   **Step 1:** Consider 1 L (1000 mL) of solution.
    *   Moles of H₂SO₄ = 1 mol. Mass of H₂SO₄ = 98 g.
    *   Mass of solution = $d \times V = 1.065 \times 1000 = 1065$ g.
*   **Step 2:** Find mass of solvent.
    *   $W_{solvent} = 1065 - 98 = 967$ g = 0.967 kg.
*   **Step 3:** Calculate molality.
    *   $m = \frac{1 \text{ mol}}{0.967 \text{ kg}} = 1.034 \text{ m}$
*   **Alternative formula method:**
    *   $m = \frac{1 \times 1000}{1.065 \times 1000 - 1 \times 98} = \frac{1000}{1065 - 98} = \frac{1000}{967} = 1.034 \text{ m}$
*   **Final Answer:** $m \approx 1.03 \text{ mol/kg}$

**5.7b**
*   **Given:** $M = 3$ M, $d = 1.12$ g/mL, $M_{glucose} = 180$ g/mol.
*   **Step 1:** Calculate using formula.
    *   $m = \frac{M \times 1000}{d \times 1000 - M \times M_{solute}}$
    *   $m = \frac{3 \times 1000}{1.12 \times 1000 - 3 \times 180}$
    *   $m = \frac{3000}{1120 - 540} = \frac{3000}{580} = 5.17 \text{ m}$
*   **Final Answer:** $m = 5.17 \text{ mol/kg}$

**5.7c**
*   **Given:** $M = 0.5$ M, $d = 1.01$ g/mL, $M_{urea} = 60$ g/mol.
*   **Step 1:** Calculate using formula.
    *   $m = \frac{0.5 \times 1000}{1.01 \times 1000 - 0.5 \times 60}$
    *   $m = \frac{500}{1010 - 30} = \frac{500}{980} = 0.51 \text{ m}$
*   **Final Answer:** $m = 0.51 \text{ mol/kg}$

**5.7d**
*   **Given:** $M = 18$ M, $d = 1.84$ g/mL, $M_{H2SO4} = 98$ g/mol.
*   **Step 1:** Calculate using formula.
    *   $m = \frac{18 \times 1000}{1.84 \times 1000 - 18 \times 98}$
    *   $m = \frac{18000}{1840 - 1764} = \frac{18000}{76} = 236.8 \text{ m}$
*   **Final Answer:** $m \approx 236.8 \text{ mol/kg}$

**5.7e**
*   **Given:** $m = 4$ m, $d = 1.2$ g/mL, $M_{solute} = 80$ g/mol.
*   **Step 1:** Substitute into formula and solve for $M$.
    *   $m = \frac{M \times 1000}{d \times 1000 - M \times M_{solute}}$
    *   $4 = \frac{1000M}{1200 - 80M}$
    *   $4800 - 320M = 1000M$
    *   $1320M = 4800 \implies M = \frac{4800}{1320} = 3.636 \text{ M}$
*   **Alternative Logic:** 4 m means 4 mol solute in 1 kg (1000 g) solvent.
    *   Mass of solute = $4 \times 80 = 320$ g.
    *   Total mass of solution = $1000 + 320 = 1320$ g.
    *   Volume of solution = $\frac{\text{Mass}}{d} = \frac{1320 \text{ g}}{1.2 \text{ g/mL}} = 1100$ mL = 1.1 L.
    *   Molarity = $\frac{\text{moles}}{\text{Volume (L)}} = \frac{4}{1.1} = 3.636 \text{ M}$.
*   **Final Answer:** Molarity = 3.64 M

</details>

---

### Type 8: Molality of Pure Liquid

**The Pattern:** A conceptual trick question. What is the "molality" of a pure substance?

#### Solved Example 5.8
**Q:** Calculate the molality of pure water. 🟡

**Solution:**
```
Wait — pure water has no solute. So what does molality even mean here?

Interpretation: Consider water as the "solute" in itself.
    Take 1 mol of water = 18 g (this is the "solute")
    The remaining water is the "solvent"

But this creates a circular problem. In reality:

For pure water:
    Consider 1000 g of water as solvent.
    Moles of water = 1000/18 = 55.55 mol

    "Molality" = 55.55 mol / 1 kg = 55.55 m

Answer: The "molality" of pure water is 55.55 m
(This is a theoretical construct — pure substances don't truly have "molality")
```

> **Why this matters:** This is a conceptual question that tests whether you understand molality at a deep level. It also connects to the idea that the "molarity of pure water = 55.5 M" (from Chapter 6).

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| 5.8a | Calculate the "molality" of pure ethanol (M = 46, d = 0.789 g/mL). | 🟡 |
| 5.8b | Why is the concept of molality undefined for pure substances in a rigorous sense? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**5.8a**
*   **Given:** Pure ethanol, $M$ = 46 g/mol. (Density is not actually needed if we assume 1 kg of mass).
*   **Step 1:** Consider 1000 g (1 kg) of pure ethanol as the "solvent".
*   **Step 2:** Calculate moles in this 1000 g.
    *   $n = \frac{1000}{46} = 21.74 \text{ mol}$
*   **Step 3:** Calculate pseudo-molality.
    *   $m = \frac{21.74 \text{ mol}}{1 \text{ kg}} = 21.74 \text{ m}$
*   **Final Answer:** "Molality" of pure ethanol is 21.74 m

**5.8b**
*   **Rigorous explanation:** Molality is inherently a property of a *mixture* (a solution). By definition, it requires two distinct components: a solute and a solvent. In a pure substance, there is no solute dissolved in a solvent; there is only one substance. We can mathematize it by treating the substance as both solute and solvent simultaneously (as done in 5.8a), but this is a theoretical exercise, not a physical reality. Thus, rigorously, it is undefined.

</details>

---

### Type 9: Why Molality is Preferred for Colligative Properties

**The Pattern:** Conceptual reasoning — no calculation.

#### Solved Example 5.9
**Q:** Why do we use molality (not molarity) in colligative property formulas? 🟡

**Solution:**
```
Colligative property formulas:
    ΔTb = Kb × m
    ΔTf = Kf × m
    π = mRT (for some formulations)

Why molality?

1. TEMPERATURE INDEPENDENCE
   Colligative properties (boiling point elevation, freezing point 
   depression) inherently involve TEMPERATURE CHANGES. If we used 
   molarity, the concentration itself would change as we heat/cool 
   the solution — making the formula self-contradictory.

2. ADDITIVITY
   Molality of solvent is directly proportional to the mole fraction 
   of solute (for dilute solutions), which is the fundamental quantity 
   that determines colligative properties.

3. MEASUREMENT SIMPLICITY
   Mass is easier to measure accurately than volume, especially 
   across different temperatures. No volumetric flask needed.

Summary: Colligative properties depend on the NUMBER OF SOLUTE 
         PARTICLES relative to solvent. Molality counts exactly that,
         without volume interference.
```

#### Practice Questions — Type 9

| # | Question | Difficulty |
|---|----------|------------|
| 5.9a | A student uses molarity instead of molality in ΔTb = Kb × m. At what temperature is the error zero? At what temperature is it maximum? | 🔴 |
| 5.9b | List all concentration terms that are temperature-independent. Why are they all based on mass (or moles)? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 9</summary>

**5.9a**
*   **Reasoning:** Molality ($m$) and Molarity ($M$) are essentially equal when the density of the solution is exactly $1 \text{ kg/L}$ (or $1 \text{ g/mL}$) and the solution is very highly dilute (mass of solute is negligible compared to mass of solvent).
*   For an aqueous solution, the density of water is exactly $1 \text{ g/mL}$ at $4^\circ\text{C}$. At this temperature, 1 L of water = 1 kg of water, making the numerical values of $m$ and $M$ nearly identical. Thus, the error is minimum/zero at $4^\circ\text{C}$ (assuming high dilution).
*   The error is maximum at temperatures furthest from $4^\circ\text{C}$ (e.g., near boiling point or past it, where volume expansion is highly pronounced and density drops significantly), because volume changes rapidly with high temperature but mass stays constant.

**5.9b**
*   **Temperature-independent terms:** Molality ($m$), Mole Fraction ($\chi$), Mass Percent (% w/w), Parts Per Million (ppm by mass).
*   **Why based on mass/moles?** Temperature changes affect the *volume* of a substance due to thermal expansion or contraction. However, temperature has absolutely no effect on the *mass* of the substance or the atomic/molecular count (*moles*). Because these concentration terms exclusively place mass or moles in both the numerator and denominator, they remain perfectly invariant regardless of temperature shifts.

</details>

---

### Type 10: Multi-solute — Two Solutes in Same Solvent

**The Pattern:** More than one solute → treat each separately, but use the SAME solvent mass.

#### Solved Example 5.10
**Q:** 6 g of urea (M = 60) and 5.85 g of NaCl (M = 58.5) are dissolved in 500 g of water. Find the molality of each solute and the total molality. 🟡

**Solution:**
```
Step 1: Calculate moles of each solute
    n_urea = 6/60 = 0.1 mol
    n_NaCl = 5.85/58.5 = 0.1 mol

Step 2: Mass of solvent = 500 g = 0.5 kg

Step 3: Individual molalities
    m_urea = 0.1/0.5 = 0.2 m
    m_NaCl = 0.1/0.5 = 0.2 m

Step 4: Total molality
    m_total = m_urea + m_NaCl = 0.2 + 0.2 = 0.4 m

Answer: m_urea = 0.2 m, m_NaCl = 0.2 m, m_total = 0.4 m
```

> **Why total molality matters:** For colligative properties of non-electrolytes, what matters is the TOTAL molality of all solute particles.

> **⚠️ For electrolytes:** NaCl dissociates: NaCl → Na⁺ + Cl⁻. So the effective molality of particles = 0.2 × 2 = 0.4 m just from NaCl alone. This uses the van't Hoff factor (i) — preview for colligative properties.

#### Practice Questions — Type 10

| # | Question | Difficulty |
|---|----------|------------|
| 5.10a | 9 g of glucose (M = 180) and 3 g of urea (M = 60) in 250 g of water. Find m_glucose, m_urea, and m_total. | 🟡 |
| 5.10b | 11.1 g CaCl₂ (M = 111) and 5.85 g NaCl (M = 58.5) in 1 kg of water. Find individual and total molalities. For colligative purposes, what is the effective total molality? (CaCl₂ → Ca²⁺ + 2Cl⁻, NaCl → Na⁺ + Cl⁻) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 10</summary>

**5.10a**
*   **Given:** Glucose ($W = 9$ g, $M = 180$), Urea ($W = 3$ g, $M = 60$), $W_{solvent} = 250$ g = 0.25 kg.
*   **Step 1:** Calculate individual moles.
    *   $n_{glucose} = \frac{9}{180} = 0.05 \text{ mol}$
    *   $n_{urea} = \frac{3}{60} = 0.05 \text{ mol}$
*   **Step 2:** Calculate individual molalities.
    *   $m_{glucose} = \frac{0.05 \text{ mol}}{0.25 \text{ kg}} = 0.2 \text{ m}$
    *   $m_{urea} = \frac{0.05 \text{ mol}}{0.25 \text{ kg}} = 0.2 \text{ m}$
*   **Step 3:** Calculate total molality.
    *   $m_{total} = m_{glucose} + m_{urea} = 0.2 + 0.2 = 0.4 \text{ m}$
*   **Final Answer:** $m_{glucose} = 0.2 \text{ m}$, $m_{urea} = 0.2 \text{ m}$, $m_{total} = 0.4 \text{ m}$

**5.10b**
*   **Given:** CaCl₂ ($W = 11.1$ g, $M = 111$), NaCl ($W = 5.85$ g, $M = 58.5$), $W_{solvent} = 1$ kg.
*   **Step 1:** Calculate individual moles.
    *   $n_{CaCl2} = \frac{11.1}{111} = 0.1 \text{ mol}$
    *   $n_{NaCl} = \frac{5.85}{58.5} = 0.1 \text{ mol}$
*   **Step 2:** Calculate individual formal molalities.
    *   $m_{CaCl2} = \frac{0.1 \text{ mol}}{1 \text{ kg}} = 0.1 \text{ m}$
    *   $m_{NaCl} = \frac{0.1 \text{ mol}}{1 \text{ kg}} = 0.1 \text{ m}$
*   **Step 3:** Calculate formal total molality.
    *   $m_{total} = 0.1 + 0.1 = 0.2 \text{ m}$
*   **Step 4:** Calculate effective molality for colligative properties (accounting for dissociation ions).
    *   CaCl₂ $\rightarrow$ Ca²⁺ + 2Cl⁻ (yields 3 particles per molecule. $i = 3$).
    *   NaCl $\rightarrow$ Na⁺ + Cl⁻ (yields 2 particles per molecule. $i = 2$).
    *   Effective $m_{CaCl2} = 0.1 \times 3 = 0.3 \text{ m}$ of ions.
    *   Effective $m_{NaCl} = 0.1 \times 2 = 0.2 \text{ m}$ of ions.
    *   Total effective molality = $0.3 + 0.2 = 0.5 \text{ m}$.
*   **Final Answer:** Individual $m = 0.1 \text{ m}$ each. Formal total $m = 0.2 \text{ m}$. Effective total $m = 0.5 \text{ m}$.

</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 5.M1 | A 15% (w/w) glucose (M=180) solution has density 1.06 g/mL. Find: (a) molality (b) molarity (c) mole fraction of glucose. | T5 + T7 + Ch4 | 🔴 |
| 5.M2 | 2 M NaCl (d = 1.08 g/mL, M = 58.5). Find (a) molality (b) mass percent (c) mole fraction. | T7 + reverse T5 + Ch4 | 🔴 |
| 5.M3 | χ_urea = 0.04 (M_urea = 60, M_water = 18). (a) Find molality. (b) If d = 1.02 g/mL, find molarity. (c) Find mass % of urea. | T6 + Ch4-T8 + reverse T5 | 🔴 |
| 5.M4 | A student prepares a solution by dissolving 20 g of a substance (M = 40) in 480 g of water. (a) Find mass %. (b) Find molality. (c) If d = 1.01 g/mL, find molarity. (d) Find mole fraction. | T4 + T5 + T7 + Ch4 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**5.M1**
*   **Given:** 15% (w/w) glucose, $d = 1.06$ g/mL, $M_{glucose} = 180$.
*   **Step 1:** Deconstruct w/w%. Assume 100 g solution.
    *   $W_{solute}$ (glucose) = 15 g
    *   $W_{solvent}$ (water) = 85 g = 0.085 kg
    *   $n_{solute} = \frac{15}{180} = 0.0833 \text{ mol}$. $n_{solvent} = \frac{85}{18} = 4.72 \text{ mol}$.
*   **(a) Molality $(m)$:**
    *   $m = \frac{n_{solute}}{W_{solvent (kg)}} = \frac{0.0833}{0.085} \approx 0.98 \text{ m}$
*   **(b) Molarity $(M)$:**
    *   Volume of 100 g solution = $\frac{100 \text{ g}}{1.06 \text{ g/mL}} = 94.34 \text{ mL} = 0.09434 \text{ L}$
    *   $M = \frac{n_{solute}}{V_{(L)}} = \frac{0.0833}{0.09434} \approx 0.88 \text{ M}$
*   **(c) Mole fraction $(\chi)$:**
    *   $\chi_{glucose} = \frac{n_{solute}}{n_{solute} + n_{solvent}} = \frac{0.0833}{0.0833 + 4.72} = \frac{0.0833}{4.803} \approx 0.0173$
*   **Final Answer:** (a) $0.98 \text{ m}$, (b) $0.88 \text{ M}$, (c) $\chi \approx 0.0173$

**5.M2**
*   **Given:** $2 \text{ M}$ NaCl, $d = 1.08 \text{ g/mL}$, $M_{NaCl} = 58.5$.
*   **Step 1:** Assume 1 L (1000 mL) solution.
    *   $n_{NaCl} = 2 \text{ mol}$
    *   $W_{solute}$ (NaCl) = $2 \times 58.5 = 117 \text{ g}$
    *   Mass of solution = $1.08 \times 1000 = 1080 \text{ g}$
    *   $W_{solvent}$ (water) = $1080 - 117 = 963 \text{ g} = 0.963 \text{ kg}$
    *   $n_{solvent} = \frac{963}{18} = 53.5 \text{ mol}$
*   **(a) Molality $(m)$:**
    *   $m = \frac{n_{solute}}{W_{solvent (kg)}} = \frac{2}{0.963} \approx 2.08 \text{ m}$
*   **(b) Mass percent (w/w%):**
    *   $\%\text{w/w} = \left(\frac{W_{solute}}{W_{solution}}\right) \times 100 = \left(\frac{117}{1080}\right) \times 100 = 10.83\%$
*   **(c) Mole fraction $(\chi)$:**
    *   $\chi_{NaCl} = \frac{2}{2 + 53.5} = \frac{2}{55.5} \approx 0.036$
*   **Final Answer:** (a) $2.08 \text{ m}$, (b) $10.83\%$, (c) $\chi \approx 0.036$

**5.M3**
*   **Given:** $\chi_{urea} = 0.04$, $M_{urea} = 60$, $M_{water} = 18$, $d = 1.02 \text{ g/mL}$.
*   **Step 1:** Assume total moles = 1 mol.
    *   $n_{urea} = 0.04 \text{ mol} \implies W_{urea} = 0.04 \times 60 = 2.4 \text{ g}$
    *   $n_{water} = 0.96 \text{ mol} \implies W_{water} = 0.96 \times 18 = 17.28 \text{ g} = 0.01728 \text{ kg}$
    *   Total mass of solution = $2.4 + 17.28 = 19.68 \text{ g}$
*   **(a) Molality $(m)$:**
    *   $m = \frac{0.04 \text{ mol}}{0.01728 \text{ kg}} \approx 2.31 \text{ m}$
*   **(b) Molarity $(M)$:**
    *   Volume of 19.68 g solution = $\frac{19.68}{1.02} = 19.29 \text{ mL} = 0.01929 \text{ L}$
    *   $M = \frac{0.04 \text{ mol}}{0.01929 \text{ L}} \approx 2.07 \text{ M}$
*   **(c) Mass percent:**
    *   $\%\text{w/w} = \left(\frac{2.4}{19.68}\right) \times 100 \approx 12.2\%$
*   **Final Answer:** (a) $2.31 \text{ m}$, (b) $2.07 \text{ M}$, (c) $12.2\%$

**5.M4**
*   **Given:** $W_{solute} = 20 \text{ g}$ ($M=40$), $W_{solvent} = 480 \text{ g}$, $d = 1.01 \text{ g/mL}$.
*   **Step 1:** Calculate core values.
    *   $n_{solute} = \frac{20}{40} = 0.5 \text{ mol}$
    *   $W_{solution} = 20 + 480 = 500 \text{ g}$
    *   $n_{solvent} = \frac{480}{18} = 26.67 \text{ mol}$
*   **(a) Mass percent:**
    *   $\%\text{w/w} = \left(\frac{20}{500}\right) \times 100 = 4\%$
*   **(b) Molality $(m)$:**
    *   $m = \frac{0.5 \text{ mol}}{480/1000 \text{ kg}} = \frac{0.5}{0.48} \approx 1.04 \text{ m}$
*   **(c) Molarity $(M)$:**
    *   Volume context = $\frac{500 \text{ g}}{1.01 \text{ g/mL}} = 495.05 \text{ mL} = 0.495 \text{ L}$
    *   $M = \frac{0.5 \text{ mol}}{0.495 \text{ L}} \approx 1.01 \text{ M}$
*   **(d) Mole fraction:**
    *   $\chi = \frac{0.5}{0.5 + 26.67} = \frac{0.5}{27.17} \approx 0.0184$
*   **Final Answer:** (a) $4\%$, (b) $1.04 \text{ m}$, (c) $1.01 \text{ M}$, (d) $\chi \approx 0.0184$

</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 5.B1 | Calculate the molality of 2.5 g of ethanoic acid (CH₃COOH, M = 60) dissolved in 75 g of benzene. ⭐ | 🟢 |
| 5.B2 | A solution is prepared by dissolving 0.5 mol of NaOH in 500 g of water. Calculate the molality. | 🟢 |
| 5.B3 | The mass percentage of aspirin (C₉H₈O₄, M = 180) in acetonitrile (CH₃CN, M = 41) is 6.5%. Calculate the molality of the solution. ⭐ | 🟡 |
| 5.B4 | A 5% solution of cane sugar (C₁₂H₂₂O₁₁, M = 342) in water. Calculate (a) molality (b) mole fraction. ⭐ | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**5.B1**
*   **Step 1:** Moles of ethanoic acid = $\frac{2.5 \text{ g}}{60 \text{ g/mol}} = 0.0417 \text{ mol}$.
*   **Step 2:** Mass of solvent (benzene) = 75 g = 0.075 kg.
*   **Step 3:** Molality = $\frac{0.0417 \text{ mol}}{0.075 \text{ kg}} = 0.556 \text{ m}$.
*   **Final Answer:** $0.556 \text{ mol/kg}$

**5.B2**
*   **Step 1:** Moles of NaOH = 0.5 mol.
*   **Step 2:** Mass of solvent (water) = 500 g = 0.5 kg.
*   **Step 3:** Molality = $\frac{0.5 \text{ mol}}{0.5 \text{ kg}} = 1 \text{ m}$.
*   **Final Answer:** $1 \text{ mol/kg}$

**5.B3**
*   **Step 1:** Assume 100 g solution. Aspirin = 6.5 g. Acetonitrile (solvent) = $100 - 6.5 = 93.5 \text{ g} = 0.0935 \text{ kg}$.
*   **Step 2:** Moles of aspirin = $\frac{6.5 \text{ g}}{180 \text{ g/mol}} = 0.0361 \text{ mol}$.
*   **Step 3:** Molality = $\frac{0.0361 \text{ mol}}{0.0935 \text{ kg}} \approx 0.386 \text{ m}$.
*   **Final Answer:** $0.386 \text{ mol/kg}$

**5.B4**
*   **Step 1:** Assume 100 g solution. Sugar = 5 g. Water (solvent) = 95 g = 0.095 kg.
*   **Step 2:** Calculate molality.
    *   Moles of sugar = $\frac{5}{342} = 0.0146 \text{ mol}$.
    *   Molality = $\frac{0.0146 \text{ mol}}{0.095 \text{ kg}} = 0.154 \text{ m}$.
*   **Step 3:** Calculate mole fraction.
    *   Moles of water = $\frac{95}{18} = 5.278 \text{ mol}$.
    *   $\chi_{sugar} = \frac{0.0146}{0.0146 + 5.278} = \frac{0.0146}{5.2926} \approx 0.00276$.
*   **Final Answer:** (a) $m = 0.154 \text{ mol/kg}$, (b) $\chi = 0.00276$

</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 5.J1 | Concentrated H₂SO₄ has d = 1.84 g/mL and is 98% by mass (M = 98). Find (a) molarity (b) molality (c) mole fraction. ⭐⭐ | 🔴 |
| 5.J2 | A 4 M NaOH solution has d = 1.15 g/mL (M = 40). Find (a) molality (b) mass %. Which is greater — M or m? Why? | 🔴 |
| 5.J3 | The molality and molarity of an aqueous solution are equal in magnitude. Given that M_solute = 100 g/mol, find the density of the solution. ⭐ | 🔴 |
| 5.J4 | A solution has m = 10 molal and M = 8 molar. If M_solute = 50 g/mol, find the density. | 🔴 |
| 5.J5 | An aqueous solution has mole fraction of solute = 0.2 and density = 1.25 g/mL. M_solute = 60. Find (a) molality (b) molarity (c) mass %. (Full interconversion chain.) ⭐ | 🔴 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**5.J1**
*   **Step 1:** Assume 100 g solution. $W_{H2SO4} = 98 \text{ g}$, $W_{water} = 2 \text{ g} = 0.002 \text{ kg}$. $n_{H2SO4} = \frac{98}{98} = 1 \text{ mol}$.
*   **(a) Molarity $(M)$:**
    *   Volume = $\frac{100 \text{ g}}{1.84 \text{ g/mL}} = 54.35 \text{ mL} = 0.05435 \text{ L}$.
    *   $M = \frac{1 \text{ mol}}{0.05435 \text{ L}} = 18.4 \text{ M}$.
*   **(b) Molality $(m)$:**
    *   $m = \frac{1 \text{ mol}}{0.002 \text{ kg}} = 500 \text{ m}$.
*   **(c) Mole fraction:**
    *   $n_{water} = \frac{2}{18} = 0.111 \text{ mol}$.
    *   $\chi_{H2SO4} = \frac{1}{1 + 0.111} = 0.9$.
*   **Final Answer:** (a) $18.4 \text{ M}$, (b) $500 \text{ m}$, (c) $0.9$

**5.J2**
*   **Step 1:** 1 L solution. $n_{NaOH} = 4 \text{ mol}$, $W_{NaOH} = 4 \times 40 = 160 \text{ g}$.
*   **Step 2:** Mass of 1 L solution = $1.15 \times 1000 = 1150 \text{ g}$.
*   **Step 3:** Mass of solvent = $1150 - 160 = 990 \text{ g} = 0.99 \text{ kg}$.
*   **(a) Molality:** $m = \frac{4}{0.99} = 4.04 \text{ m}$.
*   **(b) Mass %:** $\%\text{w/w} = \left(\frac{160}{1150}\right) \times 100 = 13.9\%$.
*   **Greater:** $m$ is slightly greater than $M$ ($4.04 > 4$). This is because 1 L of solution contains *less* than 1 kg of solvent due to the space taken up by the dense solute. Molarity divides moles by 1 L; molality divides by 0.99 kg.
*   **Final Answer:** (a) $4.04 \text{ m}$, (b) $13.9\%$, $m > M$.

**5.J3**
*   **Given:** $|m| = |M| = x$. Formula connecting M and m: $m = \frac{M \times 1000}{d \times 1000 - M \times M_{solute}}$.
*   **Step 1:** Assume 1 L (1000 mL) solution.
*   Moles of solute = $M$. Mass of solute = $M \times 100$.
*   Mass of solution = $1000 \times d$.
*   Mass of solvent = $(1000d - 100M)$ g = $\frac{1000d - 100M}{1000}$ kg $= (d - 0.1M)$ kg.
*   Molality $m = \frac{\text{moles}}{\text{kg solvent}} = \frac{M}{d - 0.1M}$.
*   Since $|m| = |M|$ and $M > 0$, we have $M = \frac{M}{d - 0.1M}$.
*   Dividing both sides by M (M != 0): $1 = \frac{1}{d - 0.1M}$.
*   $d - 0.1M = 1 \implies d = 1 + 0.1M$.
*   **Final Answer:** density $= (1 + 0.1M) \text{ g/mL}$

**5.J4**
*   **Given:** $m = 10$, $M = 8$, $M_{solute} = 50$. Find density $d$.
*   **Step 1:** Use $m = \frac{1000M}{1000d - M \times M_{solute}}$.
    *   $10 = \frac{1000(8)}{1000d - 8 \times 50}$
    *   $10 = \frac{8000}{1000d - 400}$
    *   $10 \times (1000d - 400) = 8000 \implies 1000d - 400 = 800$
    *   $1000d = 1200 \implies d = 1.2 \text{ g/mL}$.
*   **Final Answer:** $d = 1.2 \text{ g/mL}$

**5.J5**
*   **Given:** $\chi_{solute} = 0.2$, $d = 1.25 \text{ g/mL}$, solute $M=60$. Aqueous implies solvent is water ($M=18$).
*   **(a) Molality $(m)$:**
    *   $m = \frac{1000 \times \chi_{solute}}{(1 - \chi_{solute}) \times M_{water}} = \frac{1000 \times 0.2}{0.8 \times 18} = \frac{200}{14.4} \approx 13.89 \text{ m}$.
*   **(c) Mass percent:**
    *   Assume 1 total mole. $n_{solute} = 0.2$, $n_{water} = 0.8$.
    *   $W_{solute} = 0.2 \times 60 = 12 \text{ g}$.
    *   $W_{water} = 0.8 \times 18 = 14.4 \text{ g}$.
    *   Total Mass = $12 + 14.4 = 26.4 \text{ g}$.
    *   $\%\text{w/w} = \left(\frac{12}{26.4}\right) \times 100 \approx 45.45\%$.
*   **(b) Molarity $(M)$:**
    *   Volume of 26.4 g solution = $\frac{26.4 \text{ g}}{1.25 \text{ g/mL}} = 21.12 \text{ mL} = 0.02112 \text{ L}$.
    *   $M = \frac{0.2 \text{ mol}}{0.02112 \text{ L}} \approx 9.47 \text{ M}$.
*   **Final Answer:** (a) $13.89 \text{ m}$, (b) $9.47 \text{ M}$, (c) $45.45\%$

</details>

---

## Key Takeaways from Chapter 5

```
┌─────────────────────────────────────────────────────────────┐
│                  MOLALITY SUMMARY                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Formula: m = n_solute / W_solvent(kg)                      │
│                                                              │
│  Expanded: m = (W_solute × 1000) / (M_solute × W_solvent)  │
│                                                              │
│  Key Properties:                                             │
│    • Units: mol/kg (or simply 'm')                          │
│    • Temperature INDEPENDENT ✅                              │
│    • Denominator = mass of SOLVENT (not solution!)           │
│                                                              │
│  Critical Conversions:                                       │
│    w/w% → m:  m = (x × 1000) / (M × (100-x))             │
│    χ → m:     m = (1000 × χ) / ((1-χ) × M_solvent)        │
│    M → m:     m = (M × 1000) / (d×1000 - M×M_solute)      │
│                                                              │
│  THE #1 TRAP:                                                │
│    Using W_solution instead of W_solvent ❌                  │
│    Always: W_solvent = W_solution - W_solute                │
│                                                              │
│  Used for: Colligative properties (ΔTb, ΔTf, π)            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*← [Chapter 4 — Mole Fraction](./04-mole-fraction.md) | [Chapter 6 — Molarity →](./06-molarity.md)*
