# Chapter 2: Volume Percent (v/v%)
## Part I: The Foundations

---

## 🎯 Stage 1: The Core Idea

### What is Volume Percent?

Walk into any liquor store. Pick up a bottle of whiskey. It says: **"42% v/v"**.

What does that mean? It means: **out of every 100 mL of that liquid, 42 mL is pure alcohol and the remaining 58 mL is water (and other stuff).**

That's volume percent — expressing concentration as the volume of solute in every 100 units of solution volume.

### When Do We Use It?

Volume percent is used when **both solute and solvent are liquids** — and we measure them by volume (because pouring liquids by volume is easier than weighing them).

Common examples:
- Alcoholic beverages: "Beer is 5% v/v ethanol"
- Medical solutions: "70% v/v rubbing alcohol"
- Laboratory solvents: "Mix 30% acetone in water by volume"

### The Key Limitation

Volume percent is **temperature-dependent**. Why? Because liquids expand when heated. The same mass of liquid occupies more volume at higher temperature. So the ratio of volumes changes with temperature.

Also, **volumes are NOT always additive** when mixing liquids. 50 mL ethanol + 50 mL water ≠ 100 mL solution (it's actually ~96 mL). This is a crucial real-world fact, though most exam problems ignore it.

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
                     Volume of solute
Volume % (v/v%) = ───────────────────── × 100
                    Volume of solution
```

### Understanding Every Piece

| Variable | What it means | Common trap |
|----------|---------------|-------------|
| Volume of solute | Volume of the liquid being dissolved (mL or L) | Must use same units as denominator |
| Volume of solution | Total volume of the final solution | In exam problems, this is often assumed = V_solute + V_solvent |
| × 100 | Converts fraction to percentage | Same as mass percent |

### Three Forms

**Form 1: Find v/v%**
```
v/v% = (V_solute / V_solution) × 100
```

**Form 2: Find volume of solute**
```
V_solute = (v/v% × V_solution) / 100
```

**Form 3: Find volume of solution**
```
V_solution = (V_solute × 100) / v/v%
```

### Important Note: Volume Additivity Assumption

In most problems, unless stated otherwise:
```
V_solution = V_solute + V_solvent
```

But in reality, this is an approximation. Some problems (especially JEE) will explicitly state "assume volumes are additive" or give you the final volume directly.

> **Mass Percent vs Volume Percent — Quick Comparison:**
> | Feature | Mass % (w/w%) | Volume % (v/v%) |
> |---------|---------------|-----------------|
> | Numerator | Mass of solute | Volume of solute |
> | Denominator | Mass of solution | Volume of solution |
> | Temperature | Independent | **Dependent** |
> | Best used when | Solid solute in liquid | Both solute & solvent are liquids |

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given volumes, find v/v%

**The Pattern:** Two liquid volumes given → find percentage.

#### Solved Example 2.1
**Q:** 30 mL of ethanol is mixed with 70 mL of water. Assuming volumes are additive, calculate the volume percent of ethanol. 🟢

**Solution:**
```
Step 1: Identify components
    V_solute (ethanol) = 30 mL
    V_solvent (water) = 70 mL

Step 2: Total volume (assuming additive)
    V_solution = 30 + 70 = 100 mL

Step 3: Apply formula
    v/v% = (30 / 100) × 100 = 30%

Answer: 30% v/v ethanol
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.1a"></span>2.1a | 25 mL of acetone is mixed with 75 mL of water. Find v/v% of acetone (assume additive volumes). | 🟢 |
| <span id="q-2.1b"></span>2.1b | 150 mL of methanol is mixed with 850 mL of water. Find v/v%. | 🟢 |
| <span id="q-2.1c"></span>2.1c | A solution contains 40 mL of glycerol in a total volume of 250 mL. Find v/v%. | 🟢 |
| <span id="q-2.1d"></span>2.1d | 200 mL of ethanol is present in 1.5 L of a perfume solution. Find v/v%. | 🟢 |

<details>
<summary>View Answers</summary>

**2.1a**: 25% *(Key Step: (50/200) × 100)*
**2.1b**: 10% *(Key Step: (20/200) × 100)*
**2.1c**: Answer not found.
**2.1d**: Answer not found.

</details>


---

### Type 2: Reverse — Given v/v% and total volume, find volume of solute

**The Pattern:** Concentration and total volume known → find how much solute.

#### Solved Example 2.2
**Q:** A 750 mL bottle of wine is 12% v/v ethanol. What volume of pure ethanol is present? 🟢

**Solution:**
```
Step 1: Identify
    v/v% = 12%
    V_solution = 750 mL

Step 2: Calculate
    V_solute = (v/v% × V_solution) / 100
    V_solute = (12 × 750) / 100
    V_solute = 90 mL

Answer: 90 mL of pure ethanol
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.2a"></span>2.2a | A 500 mL bottle of rubbing alcohol is 70% v/v isopropanol. Find volume of isopropanol. | 🟢 |
| <span id="q-2.2b"></span>2.2b | A 2 L antiseptic solution is 5% v/v povidone-iodine. What volume of iodine solution is present? | 🟢 |
| <span id="q-2.2c"></span>2.2c | A 330 mL can of beer is 4.5% v/v ethanol. How many mL of pure ethanol does it contain? | 🟢 |
| <span id="q-2.2d"></span>2.2d | A hand sanitizer (100 mL) is 62% v/v ethanol. Find volume of ethanol and volume of other components. | 🟡 |

<details>
<summary>View Answers</summary>

**2.2a**: 175 mL *(Key Step: (35/100) × 500)*
**2.2b**: 70 mL *(Key Step: (14/100) × 500)*
**2.2c**: Answer not found.
**2.2d**: Answer not found.

</details>


---

### Type 3: Alcohol Solutions — Interpreting Labels

**The Pattern:** Real-world alcohol labeling interpretation.

#### Solved Example 2.3
**Q:** A bottle of vodka says "40% v/v". A person drinks 60 mL of vodka. How much pure alcohol has they consumed? If the density of ethanol is 0.789 g/mL, what mass of alcohol is this? 🟡

**Solution:**
```
Step 1: Volume of pure alcohol in 60 mL vodka
    V_ethanol = (40/100) × 60 = 24 mL

Step 2: Convert to mass using density
    mass = density × volume
    mass = 0.789 × 24 = 18.94 g

Answer: 24 mL or 18.94 g of pure ethanol
```

**Why this works:** v/v% gives volume of solute. Density then converts that volume to mass. This is the bridge between v/v% and w/w%.

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.3a"></span>2.3a | A 750 mL bottle of rum (42% v/v) is consumed entirely. How much pure ethanol was consumed? (d_ethanol = 0.789 g/mL) | 🟡 |
| <span id="q-2.3b"></span>2.3b | "Proof" is defined as 2 × v/v%. A 100-proof whiskey — what is its v/v%? How much alcohol in 200 mL? | 🟡 |
| <span id="q-2.3c"></span>2.3c | Is 500 mL of 8% beer or 60 mL of 40% vodka more alcohol? Calculate both. | 🟡 |

<details>
<summary>View Answers</summary>

**2.3a**: 35 mL ethanol in 100 mL solution *(Key Step: Definition of v/v%)*
**2.3b**: Answer not found.
**2.3c**: Answer not found.

</details>


---

### Type 4: Making a Solution of Desired v/v%

**The Pattern:** "Prepare X mL of Y% v/v solution" → find volumes to mix.

#### Solved Example 2.4
**Q:** How would you prepare 500 mL of 20% v/v ethanol solution? 🟢

**Solution:**
```
Step 1: Find volume of ethanol needed
    V_ethanol = (20/100) × 500 = 100 mL

Step 2: Find volume of water needed (assuming additive volumes)
    V_water = 500 − 100 = 400 mL

Answer: Mix 100 mL ethanol with 400 mL water
```

> **⚠️ Real-World Note:** In reality, you would pour 100 mL ethanol into a 500 mL volumetric flask, then add water *until the total volume reaches 500 mL* — NOT add 400 mL water. Volumes aren't perfectly additive for ethanol-water mixtures.

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.4a"></span>2.4a | Prepare 1 L of 30% v/v methanol solution. How much methanol and water? | 🟢 |
| <span id="q-2.4b"></span>2.4b | Prepare 250 mL of 10% v/v glycerol solution. | 🟢 |
| <span id="q-2.4c"></span>2.4c | A lab needs 2 L of 5% v/v acetone in water. How much pure acetone is required? | 🟢 |

<details>
<summary>View Answers</summary>

**2.4a**: Need 120 mL ethanol, add water to make 400 mL *(Key Step: (30/100) × 400 = 120)*
**2.4b**: Answer not found.
**2.4c**: Answer not found.

</details>


---

### Type 5: Temperature Dependence — Conceptual

**The Pattern:** Understanding why v/v% changes with temperature.

#### Solved Example 2.5
**Q:** A solution is 25% v/v at 20°C. If the solution is heated to 50°C, will the volume percent remain the same? Explain. 🟡

**Solution:**
```
No, it will NOT remain exactly the same.

Reason: When temperature increases:
    - Volume of solute changes (liquids expand)
    - Volume of solution changes (total expands)
    
If solute and solution expand at DIFFERENT rates
(which they usually do), the ratio V_solute/V_solution changes.

Therefore v/v% is TEMPERATURE-DEPENDENT.

Exception: If both expand at exactly the same rate 
(same coefficient of expansion), v/v% would stay constant. 
This almost never happens in practice.
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.5a"></span>2.5a | Which concentration terms are temperature-dependent: w/w%, v/v%, molarity, molality? Explain each. | 🟡 |
| <span id="q-2.5b"></span>2.5b | "A solution is 40% v/v at 25°C and remains 40% v/v at 100°C." Under what condition could this be true? | 🔴 |

<details>
<summary>View Answers</summary>

**2.5a**: Volume changes with T → v/v% changes *(Key Step: conceptual)*
**2.5b**: Answer not found.

</details>


---

### Type 6: Converting v/v% to Mass Terms Using Density

**The Pattern:** Given v/v% + densities of solute and/or solution → find w/w% or mass of solute.

#### Solved Example 2.6
**Q:** An aqueous solution is 20% v/v ethanol. The density of ethanol is 0.789 g/mL and the density of the solution is 0.97 g/mL. Calculate the mass percent (w/w%) of ethanol. 🔴 ⭐

**Solution:**
```
Step 1: Assume 100 mL of solution (this is the standard trick)

Step 2: Volume of ethanol in 100 mL solution
    V_ethanol = 20 mL (from 20% v/v)

Step 3: Mass of ethanol
    m_ethanol = V_ethanol × d_ethanol = 20 × 0.789 = 15.78 g

Step 4: Mass of solution
    m_solution = V_solution × d_solution = 100 × 0.97 = 97 g

Step 5: Mass percent
    w/w% = (15.78 / 97) × 100 = 16.27%

Answer: 16.27% w/w
```

**Key Insight:** v/v% and w/w% are NOT the same number unless the densities of solute and solution are equal. For ethanol, 20% v/v ≠ 20% w/w.

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.6a"></span>2.6a | A solution is 35% v/v methanol (d_methanol = 0.792 g/mL, d_solution = 0.95 g/mL). Find w/w%. | 🟡 |
| <span id="q-2.6b"></span>2.6b | A 10% v/v glycerol solution (d_glycerol = 1.26 g/mL) has d_solution = 1.025 g/mL. Find w/w%. | 🟡 |
| <span id="q-2.6c"></span>2.6c | A solution is 25% v/v and 21.3% w/w. If d_solution = 1.05 g/mL, find the density of the pure solute. ⭐ | 🔴 |

<details>
<summary>View Answers</summary>

**2.6a**: Multiply v/v% by density of solute to get mass, then use mass/volume of solution *(Key Step: bridge calculation)*
**2.6b**: Answer not found.
**2.6c**: Answer not found.

</details>


---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| <span id="q-2.M1"></span>2.M1 | A hand sanitizer is 62% v/v ethanol (d = 0.789 g/mL) with total density 0.87 g/mL. For a 500 mL bottle: (a) find volume of ethanol (b) find mass of ethanol (c) find w/w% of ethanol. | T2 + T3 + T6 | 🟡 |
| <span id="q-2.M2"></span>2.M2 | How would you prepare 2 L of 15% v/v acetone solution? If d_acetone = 0.791 g/mL, what mass of acetone is needed? | T4 + T6 | 🟡 |
| <span id="q-2.M3"></span>2.M3 | A 40% v/v ethanol solution (d_solution = 0.95 g/mL) is heated so its density becomes 0.935 g/mL. If the volume expands by 2%, estimate the new v/v% approximately. | T5 + T1 | 🔴 |
| <span id="q-2.M4"></span>2.M4 | Compare two drinks: 500 mL of 5% v/v beer and 30 mL of 40% v/v whiskey. Which contains more alcohol by mass? (d_ethanol = 0.789 g/mL) | T3 + T2 | 🟡 |

<details>
<summary>View Answers</summary>

**2.M1**: Answer not found.
**2.M2**: Answer not found.
**2.M3**: Answer not found.
**2.M4**: Answer not found.

</details>


---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.B1"></span>2.B1 | Calculate the volume percent of ethanol in a solution prepared by dissolving 50 mL of ethanol in 200 mL of solution. | 🟢 |
| <span id="q-2.B2"></span>2.B2 | A solution of ethanol in water has 35% v/v concentration. What volume of ethanol is present in 2 L of this solution? | 🟢 |
| <span id="q-2.B3"></span>2.B3 | A cough syrup contains 10% v/v alcohol. How much alcohol is in a 200 mL bottle? | 🟢 |
| <span id="q-2.B4"></span>2.B4 | If 30 mL of methanol (d = 0.792 g/mL) is mixed with water to prepare 150 mL of solution, find (a) v/v% and (b) mass of methanol. | 🟡 |

<details>
<summary>View Answers</summary>

**2.B1**: Answer not found.
**2.B2**: Answer not found.
**2.B3**: Answer not found.
**2.B4**: Answer not found.

</details>


---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| <span id="q-2.J1"></span>2.J1 | A solution is labelled "25% v/v ethanol" (d_solution = 0.96 g/mL, d_ethanol = 0.789 g/mL). Find (a) w/w% of ethanol (b) mass of water in 1 L of solution. ⭐ | 🟡 |
| <span id="q-2.J2"></span>2.J2 | 50 mL of ethanol (d = 0.789 g/mL) and 50 mL of water (d = 1.0 g/mL) are mixed. The actual volume of the solution is 96 mL. Find (a) the v/v% assuming ideal mixing (b) the actual v/v% (c) the w/w%. | 🔴 |
| <span id="q-2.J3"></span>2.J3 | A pharmacist needs to prepare 500 mL of a 12% v/v ethanol solution from a stock solution that is 60% v/v. What volume of stock solution is needed? (This previews Chapter 8: Dilution) | 🟡 |
| <span id="q-2.J4"></span>2.J4 | At 25°C, a solution is 15% v/v (d_solution = 1.02 g/mL). At 60°C, the volume of the same solution increases by 3% while the mass remains constant. Calculate the new density and new v/v% at 60°C if the solute expansion is 4%. | 🔴 |

<details>
<summary>View Answers</summary>

**2.J1**: Answer not found.
**2.J2**: Answer not found.
**2.J3**: Answer not found.
**2.J4**: Answer not found.

</details>


---

## Key Takeaways from Chapter 2

```
┌─────────────────────────────────────────────────────┐
│              VOLUME PERCENT SUMMARY                  │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Formula: v/v% = (V_solute / V_solution) × 100      │
│                                                      │
│  Used when: BOTH solute and solvent are liquids      │
│                                                      │
│  Temperature: DEPENDENT ❌                           │
│  (Volume changes with temperature)                   │
│                                                      │
│  v/v% ≠ w/w% unless densities are equal             │
│                                                      │
│  To convert v/v% → w/w%:                            │
│      Use densities of solute AND solution            │
│      Assume 100 mL of solution as starting point    │
│                                                      │
│  Real-world: Volumes may NOT be additive            │
│  (50 mL + 50 mL might give 96 mL, not 100 mL)     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

*← [Chapter 1 — Mass Percent](./01-mass-percent.md) | [Chapter 3 — Parts Per Million →](./03-ppm.md)*
