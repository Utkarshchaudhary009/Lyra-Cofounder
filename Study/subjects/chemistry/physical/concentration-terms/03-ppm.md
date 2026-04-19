# Chapter 3: Parts Per Million (ppm)
## Part I: The Foundations

---

## 🎯 Stage 1: The Core Idea

### What is PPM?

Your city's water supply has 0.0005% fluoride in it. That number is ugly, hard to read, and easy to misplace a zero. Scientists needed a better way to talk about **extremely small concentrations**.

Enter **parts per million (ppm)**.

Instead of saying "0.0005%", you say **"5 ppm"** — meaning there are 5 parts of fluoride in every 1,000,000 parts of water.

> **Think of it this way:** Mass percent says "parts per hundred." PPM says "parts per million." It's the same idea, just scaled up by 10,000.

### The Simple Relationship
```
1% = 10,000 ppm
0.1% = 1,000 ppm
0.01% = 100 ppm
0.001% = 10 ppm
0.0001% = 1 ppm
```

### Where Is PPM Used?

| Field | Example |
|-------|---------|
| Water quality | Fluoride in drinking water: 1–1.5 ppm |
| Air pollution | CO₂ in atmosphere: ~420 ppm |
| Food safety | Pesticide residues: < 0.1 ppm |
| Metallurgy | Impurities in gold: "99.99% pure" = 100 ppm impurities |
| Medical | Blood glucose: ~900 ppm (for normal levels) |

---

## 🔬 Stage 2: The Formula Lab

### The Formula

```
         Mass of solute
ppm = ─────────────────── × 10⁶
        Mass of solution
```

### Equivalent Forms

**Mass-based (most common in chemistry):**
```
ppm = (mg of solute / kg of solution)
ppm = (mg of solute / L of solution)     ← ONLY when d_solution ≈ 1 g/mL (dilute aqueous)
ppm = (µg of solute / g of solution)
```

### Why mg/L ≈ ppm for Dilute Aqueous Solutions

For very dilute aqueous solutions:
- Density of solution ≈ density of water ≈ 1 g/mL = 1 kg/L
- So 1 L of solution ≈ 1 kg of solution
- Therefore: mg/kg = mg/L = ppm

This approximation is used in almost all Board and JEE problems.

> **⚠️ Common Mistake:** This approximation ONLY works for dilute aqueous solutions. For concentrated solutions or non-aqueous solutions, you MUST use the exact formula with mass ratios.

### Relationship with Mass Percent

```
ppm = mass % × 10⁴

OR equivalently:

mass % = ppm / 10⁴ = ppm × 10⁻⁴
```

### Temperature Dependence

PPM (mass-based) is **temperature-independent** — same logic as w/w%. We're using mass ratios, and mass doesn't change with temperature.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Direct — Given masses, find ppm

**The Pattern:** Given mass of solute and mass of solution → calculate ppm.

#### Solved Example 3.1
**Q:** A water sample contains 0.003 g of dissolved chlorine in 1000 g (1 kg) of water. Express the concentration in ppm. 🟢

**Solution:**
```
Step 1: Identify
    Mass of solute (Cl₂) = 0.003 g
    Mass of solution ≈ 1000 g (dilute, so solution ≈ solvent)

Step 2: Apply formula
    ppm = (mass of solute / mass of solution) × 10⁶
    ppm = (0.003 / 1000) × 10⁶
    ppm = 3 × 10⁻⁶ × 10⁶
    ppm = 3 ppm

Answer: 3 ppm
```

**Alternative using mg/kg shortcut:**
```
0.003 g = 3 mg
Mass of solution = 1 kg
ppm = 3 mg / 1 kg = 3 ppm ✅ (same answer, faster)
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 3.1a | 0.006 g of fluoride is present in 2 kg of water. Find concentration in ppm. | 🟢 |
| 3.1b | A 500 g water sample contains 0.0015 g of lead. Express in ppm. | 🟢 |
| 3.1c | 10 mg of arsenic is found in 5 kg of soil sample. Find ppm. | 🟢 |
| 3.1d | A 250 g juice sample contains 0.00025 g of pesticide residue. Find ppm. | 🟡 |
| 3.1e | An industrial air filter captures 0.045 g of particulate matter from exactly 3000 kg of sampled air. Calculate the particulate concentration in ppm. | 🟢 |
| 3.1f | A 1.5 kg sample of underground well water contains 0.009 g of dissolved strontium. Express this concentration in ppm. | 🟢 |
| 3.1g | A metallurgical lab extracts 0.0007 g of silver impurities from a 10 g solid gold bar. What is the silver impurity concentration in ppm? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**3.1a:**
- **Given:** Solute mass = $0.006\text{ g}$. Solution mass = $2\text{ kg} = 2000\text{ g}$.
- **ppm:** $(0.006 / 2000) \times 10^6 = \mathbf{3\text{ ppm}}$.
- *(Shortcut: $0.006\text{ g} = 6\text{ mg}$. $6\text{ mg} / 2\text{ kg} = \mathbf{3\text{ ppm}}$)*.

**3.1b:**
- **Given:** Solute = $0.0015\text{ g} = 1.5\text{ mg}$. Solution = $500\text{ g} = 0.5\text{ kg}$.
- **ppm:** $1.5\text{ mg} / 0.5\text{ kg} = \mathbf{3\text{ ppm}}$.

**3.1c:**
- **Given:** Solute = $10\text{ mg}$. Solution = $5\text{ kg}$.
- **ppm:** $10\text{ mg} / 5\text{ kg} = \mathbf{2\text{ ppm}}$.

**3.1d:**
- **Given:** Solute = $0.00025\text{ g} = 0.25\text{ mg}$. Solution = $250\text{ g} = 0.25\text{ kg}$.
- **ppm:** $0.25\text{ mg} / 0.25\text{ kg} = \mathbf{1\text{ ppm}}$.

**3.1e:**
- **Given:** Solute = $0.045\text{ g} = 45\text{ mg}$. Solution = $3000\text{ kg}$.
- **ppm:** $45\text{ mg} / 3000\text{ kg} = \mathbf{0.015\text{ ppm}}$.

**3.1f:**
- **Given:** Solute = $0.009\text{ g} = 9\text{ mg}$. Solution = $1.5\text{ kg}$.
- **ppm:** $9\text{ mg} / 1.5\text{ kg} = \mathbf{6\text{ ppm}}$.

**3.1g:**
- **Given:** Solute = $0.0007\text{ g}$. Solution = $10\text{ g}$.
- **ppm:** $(0.0007 / 10) \times 10^6 = \mathbf{70\text{ ppm}}$.
</details>

---

### Type 2: Reverse — Given ppm, find mass of solute

**The Pattern:** Concentration in ppm known → how much solute in a given amount of solution?

#### Solved Example 3.2
**Q:** Drinking water has 1.2 ppm of fluoride. How much fluoride is present in 5 L (5 kg) of this water? 🟢

**Solution:**
```
Step 1: Understand what 1.2 ppm means
    1.2 ppm = 1.2 mg per kg of solution

Step 2: Calculate for 5 kg
    Mass of fluoride = 1.2 mg/kg × 5 kg = 6 mg = 0.006 g

Answer: 6 mg (or 0.006 g) of fluoride
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 3.2a | Water contains 0.5 ppm of dissolved oxygen. How much O₂ is in 10 L of water? | 🟢 |
| 3.2b | A lake has mercury at 0.02 ppm. How much mercury is in 1000 kg (1 tonne) of lake water? | 🟡 |
| 3.2c | Air contains 400 ppm CO₂ by mass. How much CO₂ (in grams) is in 100 kg of air? | 🟢 |
| 3.2d | The safe limit of lead in drinking water is 15 ppm. A family uses 200 L of water per day. What is the maximum mass of lead they ingest daily? | 🟡 |
| 3.2e | A city's smog report indicates a sulfur dioxide (SO₂) concentration of 2.5 ppm by mass. How many grams of SO₂ are present in 4000 kg of the city's air? | 🟢 |
| 3.2f | The permissible level for barium in drinking water is 2.0 ppm. If an adult drinks 730 L of water exactly at this limit in a year, how many grams of barium are ingested? | 🟡 |
| 3.2g | A swimming pool containing 50,000 kg of water must be treated to maintain a chlorine concentration of 3 ppm. Calculate the mass of chlorine required in grams. | 🟢 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**3.2a:**
- **Given:** $0.5\text{ ppm}$. Interpreted as $0.5\text{ mg/L}$ (dilute aqueous).
- **In 10 L:** $0.5 \times 10 = 5\text{ mg} = \mathbf{0.005\text{ g}}$.

**3.2b:**
- **Given:** $0.02\text{ ppm}$. Interpreted as $0.02\text{ mg/kg}$.
- **In 1000 kg:** $0.02 \times 1000 = 20\text{ mg} = \mathbf{0.02\text{ g}}$.

**3.2c:**
- **Given:** $400\text{ ppm}$. Interpreted as $400\text{ mg/kg}$.
- **In 100 kg:** $400 \times 100 = 40,000\text{ mg} = \mathbf{40\text{ g}}$.

**3.2d:**
- **Given:** $15\text{ ppm} = 15\text{ mg/L}$.
- **In 200 L:** $15 \times 200 = 3000\text{ mg} = \mathbf{3\text{ g}}$.

**3.2e:**
- **Given:** $2.5\text{ ppm} = 2.5\text{ mg/kg}$.
- **In 4000 kg:** $2.5 \times 4000 = 10,000\text{ mg} = \mathbf{10\text{ g}}$.

**3.2f:**
- **Given:** $2.0\text{ ppm} = 2.0\text{ mg/L}$.
- **In 730 L:** $2.0 \times 730 = 1460\text{ mg} = \mathbf{1.46\text{ g}}$.

**3.2g:**
- **Given:** $3\text{ ppm} = 3\text{ mg/kg}$.
- **In 50,000 kg:** $3 \times 50,000 = 150,000\text{ mg} = \mathbf{150\text{ g}}$.
</details>

---

### Type 3: Water Hardness Problems (Board Favourite ⭐)

**The Pattern:** Hardness of water is expressed in ppm of CaCO₃. This is the most commonly asked ppm problem in Board exams.

#### Key Background
Water hardness = concentration of Ca²⁺ and Mg²⁺ ions, expressed as **equivalent mass of CaCO₃** in ppm.
- Soft water: < 60 ppm CaCO₃
- Moderately hard: 60–120 ppm
- Hard water: 120–180 ppm
- Very hard: > 180 ppm

#### Solved Example 3.3
**Q:** A water sample has hardness of 150 ppm (as CaCO₃). 
(a) How much CaCO₃ equivalent is present in 1 L of water?
(b) How much CaCO₃ is in 500 L of water used by a household daily? 🟢 ⭐

**Solution:**
```
(a) 150 ppm means 150 mg of CaCO₃ per L (for dilute aqueous)
    = 150 mg per litre
    = 0.15 g per litre

(b) In 500 L:
    Mass of CaCO₃ = 150 mg/L × 500 L = 75,000 mg = 75 g

Answer: (a) 150 mg/L  (b) 75 g
```

#### Solved Example 3.3B
**Q:** A water sample contains 120 mg of MgSO₄ per litre. Express the hardness in ppm of CaCO₃ equivalent. 🟡 ⭐

**Solution:**
```
Step 1: Find moles of MgSO₄ per litre
    Molar mass of MgSO₄ = 24 + 32 + 64 = 120 g/mol
    Moles of MgSO₄ = 120 mg / 120 g/mol = 1 × 10⁻³ mol/L = 1 mmol/L

Step 2: Each MgSO₄ produces 1 Mg²⁺, which is equivalent to 1 CaCO₃
    Moles of CaCO₃ equivalent = 1 × 10⁻³ mol/L

Step 3: Convert to mass of CaCO₃
    Molar mass of CaCO₃ = 100 g/mol
    Mass of CaCO₃ = 1 × 10⁻³ × 100 = 0.1 g/L = 100 mg/L

Step 4: For dilute aqueous solution, mg/L ≈ ppm
    Hardness = 100 ppm (as CaCO₃)

Answer: 100 ppm
```

**Why we convert to CaCO₃ equivalent:** Different hardness-causing ions (Ca²⁺, Mg²⁺) have different molar masses. Converting everything to "CaCO₃ equivalent" gives a single, comparable standard.

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 3.3a | A water sample has hardness of 200 ppm. How much CaCO₃ is deposited when 1000 L of this water is boiled (assuming all temporary hardness)? | 🟡 |
| 3.3b | Water contains 162 mg/L of Ca(HCO₃)₂. Find hardness in ppm of CaCO₃. (M.M. of Ca(HCO₃)₂ = 162) ⭐ | 🟡 |
| 3.3c | A sample has 73 mg/L of Mg(HCO₃)₂. Express hardness in ppm as CaCO₃. (M.M. of Mg(HCO₃)₂ = 146) | 🟡 |
| 3.3d | Water has 111 mg/L CaCl₂ and 95 mg/L MgCl₂. Find total hardness in ppm as CaCO₃. (M.M.: CaCl₂=111, MgCl₂=95) ⭐ | 🔴 |
| 3.3e | A local river's water sample analysis shows a hardness of 85 ppm (as CaCO₃). Calculate the mass of CaCO₃ equivalent in a 250 L community water tank. | 🟢 |
| 3.3f | Groundwater is found to contain 136 mg/L of CaSO₄. Determine the hardness of this water expressed in ppm of CaCO₃. (M.M. of CaSO₄ = 136) ⭐ | 🟡 |
| 3.3g | A boiler feed water contains 84 mg/L of MgCO₃. If the boiler consumes 10,000 L of this water, calculate the scale formed expressed as mass of CaCO₃ equivalent. (M.M. of MgCO₃ = 84) | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 3</summary>

**3.3a:**
- **Given:** $200\text{ ppm}$ hardness $= 200\text{ mg/L}$ as CaCO₃.
- **In 1000 L:** $200\text{ mg/L} \times 1000\text{ L} = 200,000\text{ mg} = \mathbf{200\text{ g}}$ of deposit.

**3.3b:**
- **Given:** $162\text{ mg/L}$ of Ca(HCO₃)₂.
- **Moles:** $162\text{ mg} / 162\text{ g/mol} = 1\text{ mmol/L}$.
- **CaCO₃ equivalent:** $1\text{ mmol/L} \times 100\text{ g/mol} = 100\text{ mg/L}$.
- **Hardness:** $\mathbf{100\text{ ppm}}$.

**3.3c:**
- **Given:** $73\text{ mg/L}$ of Mg(HCO₃)₂.
- **Moles:** $73\text{ mg} / 146\text{ g/mol} = 0.5\text{ mmol/L}$.
- **CaCO₃ equivalent:** $0.5\text{ mmol/L} \times 100 = 50\text{ mg/L}$.
- **Hardness:** $\mathbf{50\text{ ppm}}$.

**3.3d:**
- **CaCl₂ Moles:** $111\text{ mg} / 111 = 1\text{ mmol/L} \rightarrow 100\text{ mg/L CaCO₃ eq}$.
- **MgCl₂ Moles:** $95\text{ mg} / 95 = 1\text{ mmol/L} \rightarrow 100\text{ mg/L CaCO₃ eq}$.
- **Total Hardness:** $100 + 100 = \mathbf{200\text{ ppm}}$.

**3.3e:**
- **Given:** $85\text{ ppm} = 85\text{ mg/L CaCO₃ eq}$.
- **In 250 L:** $85 \times 250 = 21,250\text{ mg} = \mathbf{21.25\text{ g}}$.

**3.3f:**
- **Given:** $136\text{ mg/L}$ of CaSO₄.
- **Moles:** $136 / 136 = 1\text{ mmol/L}$.
- **CaCO₃ eq:** $1 \times 100 = 100\text{ mg/L} = \mathbf{100\text{ ppm}}$.

**3.3g:**
- **Moles MgCO₃:** $84\text{ mg/L} / 84 = 1\text{ mmol/L}$.
- **CaCO₃ eq:** $1 \times 100 = 100\text{ mg/L}$.
- **In 10,000 L:** $100\text{ mg/L} \times 10,000\text{ L} = 1,000,000\text{ mg} = \mathbf{1000\text{ g}} = \mathbf{1\text{ kg}}$.
</details>

---

### Type 4: Air Pollution — ppm of Pollutant in Air

**The Pattern:** Concentration of gaseous pollutants in atmosphere.

#### Solved Example 3.4
**Q:** The CO₂ concentration in the atmosphere is approximately 420 ppm by mass. How much CO₂ is present in 1 kg of air? 🟢

**Solution:**
```
420 ppm = 420 parts per million by mass
= 420 mg per kg of air

In 1 kg of air:
    Mass of CO₂ = 420 mg = 0.42 g

Answer: 0.42 g of CO₂ per kg of air
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 3.4a | Ozone (O₃) in the upper atmosphere is about 8 ppm by mass. How much O₃ is in 500 kg of air? | 🟢 |
| 3.4b | The safe limit of CO in workplace air is 50 ppm. How many mg of CO per kg of air is this? | 🟢 |
| 3.4c | SO₂ in polluted city air is 0.2 ppm by mass. A person breathes 15 kg of air per day. How much SO₂ does this person inhale? | 🟡 |
| 3.4d | Measurements inside a high-traffic tunnel show a carbon monoxide (CO) level of 120 ppm by mass. How many milligrams of CO are found in a 5 kg sample of this air? | 🟢 |
| 3.4e | Formaldehyde outgassing from new furniture reaches 0.5 ppm by mass in a closed room containing 60 kg of air. What is the total mass of formaldehyde in the room? | 🟢 |
| 3.4f | Nitrous oxide (N₂O) in an agricultural area is measured at 0.35 ppm by mass. How much N₂O is in an air column weighing 200,000 kg? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 4</summary>

**3.4a:**
- **Given:** $8\text{ ppm} = 8\text{ mg/kg}$.
- **In 500 kg air:** $8 \times 500 = 4000\text{ mg} = \mathbf{4\text{ g}}$.

**3.4b:**
- $50\text{ ppm}$ literally means $\mathbf{50\text{ mg}}$ of CO per kg of air.

**3.4c:**
- **Given:** $0.2\text{ ppm} = 0.2\text{ mg/kg}$.
- **In 15 kg:** $0.2 \times 15 = \mathbf{3\text{ mg}}$.

**3.4d:**
- **Given:** $120\text{ ppm} = 120\text{ mg/kg}$.
- **In 5 kg:** $120 \times 5 = \mathbf{600\text{ mg}}$.

**3.4e:**
- **Given:** $0.5\text{ ppm} = 0.5\text{ mg/kg}$.
- **In 60 kg:** $0.5 \times 60 = 30\text{ mg} = \mathbf{0.03\text{ g}}$.

**3.4f:**
- **Given:** $0.35\text{ ppm} = 0.35\text{ mg/kg}$.
- **In 200,000 kg:** $0.35 \times 200,000 = 70,000\text{ mg} = \mathbf{70\text{ g}}$.
</details>

---

### Type 5: Trace Analysis — Very Small Quantities

**The Pattern:** Working with µg, ng, and extremely small masses.

#### Solved Example 3.5
**Q:** A blood sample (10 mL, d ≈ 1.06 g/mL) contains 2 µg of lead (Pb). Express the lead concentration in ppm. 🟡

**Solution:**
```
Step 1: Find mass of blood sample
    mass = volume × density = 10 × 1.06 = 10.6 g

Step 2: Convert lead mass to compatible units
    2 µg = 2 × 10⁻⁶ g = 0.002 mg

Step 3: Calculate ppm
    ppm = (mass of solute / mass of solution) × 10⁶
    ppm = (2 × 10⁻⁶ / 10.6) × 10⁶
    ppm = 2 / 10.6
    ppm ≈ 0.189 ppm

Answer: ≈ 0.19 ppm
```

#### Practice Questions — Type 5

| # | Question | Difficulty |
|---|----------|------------|
| 3.5a | A 5 g soil sample contains 15 µg of cadmium. Express in ppm. | 🟡 |
| 3.5b | A 100 mL water sample (d = 1 g/mL) has 50 µg of arsenic. Find ppm. Is it safe? (WHO limit: 10 ppb) | 🟡 |
| 3.5c | A 50 g food sample contains 0.3 µg of mercury. Express in ppm and ppb (parts per billion). | 🟡 |
| 3.5d | A 250 mL urine sample (d ≈ 1.02 g/mL) from a worker contains 15 µg of unmetabolized solvent. Express this solvent concentration in ppm. | 🟡 |
| 3.5e | An analytical lab tests a 20 g leaf sample and finds 80 ng (nanograms) of a banned pesticide. Express the concentration in ppm. (1 µg = 1000 ng) | 🔴 |
| 3.5f | A 5 mL tear drop (d ≈ 1.0 g/mL) contains 0.1 µg of a specific stress biomarker. Determine the biomarker concentration in parts per billion (ppb). | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 5</summary>

**3.5a:**
- **Given:** Solute $= 15\text{ \mu g} = 15 \times 10^{-6}\text{ g}$. Solution $= 5\text{ g}$.
- **ppm:** $(15 \times 10^{-6} / 5) \times 10^6 = 15 / 5 = \mathbf{3\text{ ppm}}$.

**3.5b:**
- **Mass of water:** $100\text{ mL} \times 1\text{ g/mL} = 100\text{ g}$.
- **Solute:** $50\text{ \mu g} = 50 \times 10^{-6}\text{ g}$.
- **ppm:** $(50 \times 10^{-6} / 100) \times 10^6 = \mathbf{0.5\text{ ppm}}$.
- **Is it safe?** $0.5\text{ ppm} = 500\text{ ppb}$. WHO limit is $10\text{ ppb}$. **NOT safe**.

**3.5c:**
- **Solute:** $0.3\text{ \mu g} = 0.3 \times 10^{-6}\text{ g}$. Solution $= 50\text{ g}$.
- **ppm:** $(0.3 \times 10^{-6} / 50) \times 10^6 = 0.3 / 50 = \mathbf{0.006\text{ ppm}}$.
- **ppb:** $0.006 \times 1000 = \mathbf{6\text{ ppb}}$.

**3.5d:**
- **Solution mass:** $250 \times 1.02 = 255\text{ g} = 0.255\text{ kg}$.
- **Solute:** $15\text{ \mu g} = 0.015\text{ mg}$.
- **ppm:** $0.015 / 0.255 = \mathbf{0.0588\text{ ppm}}$.

**3.5e:**
- **Solute:** $80\text{ ng} = 0.08\text{ \mu g} = 0.08 \times 10^{-6}\text{ g}$. Solution $= 20\text{ g}$.
- **ppm:** $(0.08 \times 10^{-6} / 20) \times 10^6 = \mathbf{0.004\text{ ppm}}$.

**3.5f:**
- **Solution mass:** $5\text{ mL} \times 1.0\text{ g/mL} = 5\text{ g}$.
- **Solute:** $0.1\text{ \mu g} = 0.1 \times 10^{-6}\text{ g}$.
- **ppm:** $(0.1 \times 10^{-6} / 5) \times 10^6 = \mathbf{0.02\text{ ppm}}$.
- **ppb:** $0.02 \times 1000 = \mathbf{20\text{ ppb}}$.
</details>

---

### Type 6: ppm to Mass Percent Conversion (and vice versa)

**The Pattern:** Direct mathematical conversion between ppm and %.

#### Solved Example 3.6
**Q:** A solution has 250 ppm of dissolved salt. Express this as mass percent. 🟢

**Solution:**
```
Using: mass % = ppm / 10⁴ = ppm × 10⁻⁴

mass % = 250 / 10,000 = 0.025%

Answer: 0.025% or 2.5 × 10⁻²%
```

#### Solved Example 3.6B
**Q:** A solution is 0.05% sugar by mass. Express in ppm. 🟢

**Solution:**
```
Using: ppm = mass % × 10⁴

ppm = 0.05 × 10,000 = 500 ppm

Answer: 500 ppm
```

#### Practice Questions — Type 6

| # | Question | Difficulty |
|---|----------|------------|
| 3.6a | Convert 75 ppm to mass percent. | 🟢 |
| 3.6b | Convert 0.002% (w/w) to ppm. | 🟢 |
| 3.6c | A solution is 1500 ppm NaCl. Express as (a) mass % (b) g per litre (for aqueous, d ≈ 1 g/mL). | 🟡 |
| 3.6d | The mass percentage of lead in a water sample is 3 × 10⁻⁴%. Express in ppm. Is this above the safe limit of 15 ppm? | 🟡 |
| 3.6e | The concentration of a rare earth element in an ore is 850 ppm. Express this as a mass percent. | 🟢 |
| 3.6f | A pharmaceutical ointment contains 0.015% w/w of an active steroid. What is the steroid concentration in ppm? | 🟢 |
| 3.6g | An electronic grade silicon wafer is allowed a maximum of 0.00005% boron impurity by mass. What is this limit in completely equivalent ppm? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 6</summary>

**3.6a:**
- $\text{mass } \% = \text{ppm} / 10^4 = 75 / 10,000 = \mathbf{0.0075\%}$.

**3.6b:**
- $\text{ppm} = \text{mass } \% \times 10^4 = 0.002 \times 10,000 = \mathbf{20\text{ ppm}}$.

**3.6c:**
- **(a) mass %:** $1500 / 10^4 = \mathbf{0.15\%}$.
- **(b) g/L:** $1500\text{ ppm} = 1500\text{ mg/L} = \mathbf{1.5\text{ g/L}}$.

**3.6d:**
- $\text{ppm} = 3 \times 10^{-4} \times 10^4 = \mathbf{3\text{ ppm}}$.
- **Is it above 15 ppm?** No, it is $\mathbf{safe}$.

**3.6e:**
- $\text{mass } \% = 850 / 10^4 = \mathbf{0.085\%}$.

**3.6f:**
- $\text{ppm} = 0.015 \times 10^4 = \mathbf{150\text{ ppm}}$.

**3.6g:**
- $\text{ppm} = 0.00005 \times 10^4 = \mathbf{0.5\text{ ppm}}$.
</details>

---

### Type 7: WHO / Safety Guideline Problems

**The Pattern:** Real-world comparison with safety standards.

#### Solved Example 3.7
**Q:** The WHO recommends that fluoride in drinking water should be between 0.5 ppm and 1.5 ppm. A village water supply contains 2.5 mg of fluoride per litre. Is the water safe for drinking? 🟢 ⭐

**Solution:**
```
Step 1: Convert mg/L to ppm
    For dilute aqueous solutions: mg/L ≈ ppm
    Concentration = 2.5 ppm

Step 2: Compare with WHO guidelines
    Safe range: 0.5 to 1.5 ppm
    Sample: 2.5 ppm > 1.5 ppm (upper limit)

Answer: The water is NOT safe. Fluoride level (2.5 ppm) exceeds 
        the WHO upper limit (1.5 ppm). Excess fluoride causes 
        fluorosis (damage to teeth and bones).
```

#### Practice Questions — Type 7

| # | Question | Difficulty |
|---|----------|------------|
| 3.7a | WHO limit for arsenic in drinking water is 10 ppb (parts per billion). A sample has 0.015 ppm. Is it safe? (1 ppm = 1000 ppb) ⭐ | 🟡 |
| 3.7b | The permissible limit of nitrate in drinking water is 45 ppm. A water sample has 0.005% nitrate by mass. Is it safe? | 🟡 |
| 3.7c | Chlorine residual in treated drinking water should be 0.2–1.0 ppm. A treatment plant adds 3 g of Cl₂ to 10,000 L of water. Find the resulting concentration. Is it in the safe range? | 🟡 |
| 3.7d | The WHO guideline for cadmium in drinking water is 0.003 ppm. A lab reports a cadmium level of 4 µg/L. Does this exceed the recommended safety limit? ⭐ | 🟡 |
| 3.7e | The maximum safe limit for cyanide in wastewater is 0.2 ppm. A chemical plant releases 50,000 L of effluent containing a total of 8 g of cyanide. Is the plant in violation of safety limits? | 🟡 |
| 3.7f | Safe indoor air shouldn't exceed 0.1 ppm of prolonged ozone exposure. If a 100 kg room of air contains 25 mg of ozone, is it safe? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Type 7</summary>

**3.7a:**
- **Convert:** $10\text{ ppb} = 0.01\text{ ppm}$ limit.
- **Sample:** $0.015\text{ ppm}$. $> 0.01\text{ ppm}$. **NOT safe**.

**3.7b:**
- **Sample:** $0.005\% \times 10^4 = 50\text{ ppm}$.
- **Limit:** $45\text{ ppm}$. $> 45\text{ ppm}$. **NOT safe**.

**3.7c:**
- **Concentration:** $3\text{ g} / 10,000\text{ L} = 3000\text{ mg} / 10,000\text{ L} = 0.3\text{ mg/L} \approx \mathbf{0.3\text{ ppm}}$.
- **Safe range?** Yes, $0.3\text{ ppm}$ is within $0.2-1.0\text{ ppm}$.

**3.7d:**
- **Sample:** $4\text{ \mu g/L} = 0.004\text{ mg/L} \approx \mathbf{0.004\text{ ppm}}$.
- **Limit:** $0.003\text{ ppm}$. $> 0.003\text{ ppm}$. **Exceeds limit**.

**3.7e:**
- **Concentration:** $8\text{ g} / 50,000\text{ L} = 8000\text{ mg} / 50,000\text{ L} = \mathbf{0.16\text{ mg/L} \approx 0.16\text{ ppm}}$.
- **Limit:** $0.2\text{ ppm}$. **NOT in violation**.

**3.7f:**
- **Concentration:** $25\text{ mg} / 100\text{ kg} = \mathbf{0.25\text{ ppm}}$.
- **Limit:** $0.1\text{ ppm}$. **NOT safe**.
</details>

---

### Type 8: ppm in Aqueous Solutions — The mg/L Shortcut

**The Pattern:** For dilute aqueous solutions, exploiting d ≈ 1 g/mL to simplify calculations.

#### Solved Example 3.8
**Q:** Explain why, for dilute aqueous solutions, ppm ≈ mg/L. Under what conditions does this approximation fail? 🟡

**Solution:**
```
Derivation:
    ppm = (mass of solute / mass of solution) × 10⁶

    For 1 L of dilute aqueous solution:
        mass of solution ≈ 1000 g = 1 kg  (since d ≈ 1 g/mL)
    
    ppm = (mass of solute in g / 1000 g) × 10⁶
        = mass of solute in g × 1000
        = mass of solute in mg

    So: ppm = mg of solute per litre = mg/L ✅

This approximation FAILS when:
    1. Solution is concentrated (density ≠ 1 g/mL)
    2. Solvent is not water (e.g., organic solvents)
    3. Solution has high dissolved solid content (brine, seawater)

For seawater (d ≈ 1.025 g/mL), the error is about 2.5%.
```

#### Practice Questions — Type 8

| # | Question | Difficulty |
|---|----------|------------|
| 3.8a | A solution has 50 ppm NaCl. If d_solution = 1.0 g/mL, how many mg are in 1 L? What if d = 1.2 g/mL? | 🟡 |
| 3.8b | Seawater (d = 1.025 g/mL) has about 35,000 ppm dissolved salts. Find (a) mass of salt per litre using the exact formula (b) using the mg/L approximation (c) percentage error. | 🔴 |
| 3.8c | A municipal water supply reports a sodium concentration of 120 ppm. Assuming exactly dilute aqueous behavior, what mass of sodium is in a 2 L bottle of this water? | 🟢 |
| 3.8d | A heavy syrup (d = 1.35 g/mL) has a preservative concentration of 200 ppm. Discuss mathematically why using the mg/L approximation here would lead to a significant formulation error. | 🔴 |
| 3.8e | An oceanographer analyzes estuarine water (d = 1.01 g/mL) containing 450 ppm sulfate. Calculate the absolute error in mg/L if the standard aqueous shortcut is used instead of the exact density. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 8</summary>

**3.8a:**
- **If $d = 1.0\text{ g/mL}$:** $50\text{ ppm} = \mathbf{50\text{ mg/L}}$.
- **If $d = 1.2\text{ g/mL}$:** $1\text{ L} = 1200\text{ g} = 1.2\text{ kg}$. $50\text{ ppm} = 50\text{ mg/kg}$. $50 \times 1.2 = \mathbf{60\text{ mg/L}}$.

**3.8b:**
- **(a) Exact:** $1\text{ L} = 1025\text{ g} = 1.025\text{ kg}$. Mass = $35,000\text{ mg/kg} \times 1.025\text{ kg} = 35,875\text{ mg} = \mathbf{35.875\text{ g}}$.
- **(b) Shortcut:** $35,000\text{ ppm} = 35,000\text{ mg/L} = \mathbf{35.0\text{ g}}$.
- **(c) Error:** $|35.875 - 35.0| / 35.875 \times 100 \approx \mathbf{2.44\%}$.

**3.8c:**
- **In 1 L:** $120\text{ mg}$.
- **In 2 L:** $120 \times 2 = \mathbf{240\text{ mg}}$.

**3.8d:**
- Shortcut assumes $1\text{ L} = 1\text{ kg}$. But here, $1\text{ L} = 1.35\text{ kg}$.
- Using shortcut giving $200\text{ mg/L}$ would mean actual ppm $= 200\text{ mg} / 1.35\text{ kg} = 148\text{ ppm}$, significantly underdosing the preservative.

**3.8e:**
- **Exact:** $1\text{ L} = 1010\text{ g} = 1.01\text{ kg}$. $450\text{ mg/kg} \times 1.01\text{ kg} = 454.5\text{ mg/L}$.
- **Shortcut:** $450\text{ ppm} = 450\text{ mg/L}$.
- **Absolute Error:** $|454.5 - 450| = \mathbf{4.5\text{ mg/L}}$.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 3.M1 | A water sample has 200 ppm of dissolved salts. (a) Express as mass %. (b) How much salt is in 50 L of this water? (c) If the salt is entirely NaCl (M.M. = 58.5), how many moles of NaCl is this? | T6 + T2 + new | 🟡 |
| 3.M2 | The fluoride level in a village well is 3.5 ppm. The WHO limit is 1.5 ppm. If the village mixes this water with fluoride-free water in equal volumes, what is the resulting fluoride concentration? Is it now safe? | T7 + T1 | 🟡 |
| 3.M3 | A factory discharge has 500 ppm of mercury. If 1000 L of this discharge is released into a lake containing 10⁶ L of water (originally 0 ppm Hg), find the final Hg concentration in ppm. | T1 + T2 | 🔴 |
| 3.M4 | 100 mg of Ca(HCO₃)₂ and 50 mg of MgCl₂ are dissolved in 1 L of water. Find (a) total dissolved solids in ppm (b) hardness in ppm as CaCO₃. Molar masses: Ca(HCO₃)₂ = 162, MgCl₂ = 95, CaCO₃ = 100. | T3 + T1 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**3.M1:**
- **(a) mass %:** $200 / 10^4 = \mathbf{0.02\%}$.
- **(b) Amount:** $200\text{ ppm} = 200\text{ mg/L}$. In $50\text{ L} \rightarrow 200 \times 50 = 10000\text{ mg} = \mathbf{10\text{ g}}$.
- **(c) Moles:** $10\text{ g} / 58.5\text{ g/mol} = \mathbf{0.171\text{ mol}}$.

**3.M2:**
- Equal volumes means average concentration.
- New concentration = $(3.5 + 0) / 2 = \mathbf{1.75\text{ ppm}}$.
- Still exceeds the $1.5\text{ ppm}$ limit. **NOT safe**.

**3.M3:**
- $1000\text{ L}$ of $500\text{ ppm}$ (so $500,000\text{ mg Hg}$) added to $10^6\text{ L}$.
- Total volume $\approx 1,001,000\text{ L}$.
- Final ppm $= 500,000\text{ mg} / 1,001,000\text{ L} \approx \mathbf{0.5\text{ ppm}}$.

**3.M4:**
- **(a) TDS:** Total mass = $100 + 50 = 150\text{ mg}$. Volume = $1\text{ L}$. $\mathbf{150\text{ ppm}}$.
- **(b) Hardness:**
  - Ca(HCO₃)₂ Moles $= 100\text{ mg} / 162 \approx 0.617\text{ mmol} \rightarrow 61.7\text{ mg CaCO}_3$.
  - MgCl₂ Moles $= 50\text{ mg} / 95 \approx 0.526\text{ mmol} \rightarrow 52.6\text{ mg CaCO}_3$.
  - Total Hardness $= 61.7 + 52.6 = \mathbf{114.3\text{ ppm}}$.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 3.B1 | Calculate the mass of urea (NH₂CONH₂) required to be dissolved in 1000 g of water in order to reduce the vapour pressure to 99.5% of the vapour pressure of pure water at that temperature. Express the concentration in ppm. *(Hint: involves Raoult's Law — preview)* | 🔴 |
| 3.B2 | The recommended concentration of fluoride in drinking water is up to 1 ppm. The molar mass of fluoride (as NaF) is 42 g/mol. How many moles of NaF are present per litre of water at this concentration? ⭐ | 🟡 |
| 3.B3 | Express 500 ppm of KCl in water as (a) mass percent and (b) molality. (M.M. of KCl = 74.5) ⭐ | 🟡 |
| 3.B4 | A 1 kg water sample is found to contain 2 mg of lead. Express the concentration as (a) ppm (b) mass percent (c) mg/L (assume d = 1 g/mL). | 🟢 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**3.B1:**
- This is a relative lowering of vapor pressure question previewing Raoult's Law. $\Delta P / P^\circ = X_{solute}$.
- $0.5\% \text{ lowering} \rightarrow X_{solute} = 0.005$.
- $Moles_{water} = 1000 / 18 = 55.55$.
- $Moles_{solute} / (Moles_{solute} + 55.55) = 0.005 \rightarrow Moles_{solute} \approx 0.279\text{ mol}$.
- $Mass_{urea} = 0.279 \times 60 = 16.74\text{ g}$.
- $ppm = (16.74 / 1000) \times 10^6 = \mathbf{16,740\text{ ppm}}$.

**3.B2:**
- $1\text{ ppm} = 1\text{ mg/L} = 0.001\text{ g/L}$.
- $Moles = 0.001\text{ g} / 42\text{ g/mol} = \mathbf{2.38 \times 10^{-5}\text{ mol/L}}$.

**3.B3:**
- **(a) mass %:** $500 / 10^4 = \mathbf{0.05\%}$.
- **(b) molality:** $500\text{ ppm} \rightarrow 500\text{ mg solute in } 10^6\text{ mg solution}$. So $0.5\text{ g}$ in $\approx 1000\text{ g}$ water. Moles $= 0.5 / 74.5 \approx \mathbf{0.0067\text{ m}}$.

**3.B4:**
- **(a) ppm:** $2\text{ mg} / 1\text{ kg} = \mathbf{2\text{ ppm}}$.
- **(b) mass %:** $2 / 10^4 = \mathbf{0.0002\%}$.
- **(c) mg/L:** $1\text{ kg} = 1\text{ L}$, so **$2\text{ mg/L}$**.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

| # | Question | Difficulty |
|---|----------|------------|
| 3.J1 | Sea water contains 6 × 10⁻³ ppm of dissolved gold. The total mass of ocean water is approximately 1.4 × 10²¹ kg. Calculate the total mass of dissolved gold in the oceans (in tonnes). | 🟡 |
| 3.J2 | A 10 ppm solution of NaCl (M.M. = 58.5) in water has density approximately 1 g/mL. Find (a) its molarity (b) its molality. ⭐ | 🔴 |
| 3.J3 | Air contains 78% N₂, 21% O₂, and the rest is argon and trace gases. If CO₂ is 420 ppm by mass of the total atmosphere, and the mass of Earth's atmosphere is 5.15 × 10¹⁸ kg, find the total mass of CO₂ in the atmosphere. | 🟡 |
| 3.J4 | Hard water contains 120 ppm of Ca²⁺ ions. Express the Ca²⁺ concentration in mol/L. (Atomic mass of Ca = 40). ⭐ | 🟡 |
| 3.J5 | A water sample has 2 ppm of dissolved chlorine (Cl₂). If Cl₂ disinfection requires at least 0.5 ppm residual after 30 minutes, and 60% of the Cl₂ reacts with organic matter, is the initial dose sufficient? | 🔴 |

<details>
<summary>💡 Detailed Solutions for JEE Mains Arena</summary>

**3.J1:**
- Mass of gold in $1\text{ kg} = 6 \times 10^{-3}\text{ mg} = 6 \times 10^{-9}\text{ kg}$.
- Total mass $= 1.4 \times 10^{21} \times 6 \times 10^{-9} = 8.4 \times 10^{12}\text{ kg} = \mathbf{8.4 \times 10^9\text{ tonnes}}$.

**3.J2:**
- $10\text{ ppm} = 10\text{ mg/L} = 0.01\text{ g/L}$.
- **(a) Molarity:** $Moles = 0.01 / 58.5 = 1.71 \times 10^{-4}\text{ mol}$. Vol $= 1\text{ L}$. $\mathbf{M = 1.71 \times 10^{-4}\text{ M}}$.
- **(b) Molality:** $1\text{ L} \approx 1\text{ kg}$ water. $\mathbf{m \approx 1.71 \times 10^{-4}\text{ m}}$.

**3.J3:**
- Total CO₂ mass $= 420\text{ ppm} \times 5.15 \times 10^{18}\text{ kg}$.
- $420 \times 10^{-6} \times 5.15 \times 10^{18} = 2.163 \times 10^{15}\text{ kg} = \mathbf{2163\text{ gigatonnes}}$.

**3.J4:**
- $120\text{ ppm Ca}^{2+} = 120\text{ mg/L} = 0.12\text{ g/L}$.
- Moles $= 0.12 / 40 = 0.003\text{ mol/L} = \mathbf{3 \times 10^{-3}\text{ M}}$.

**3.J5:**
- Initial $= 2\text{ ppm}$.
- Reacts $= 60\%$ of $2 = 1.2\text{ ppm}$.
- Residual $= 2 - 1.2 = \mathbf{0.8\text{ ppm}}$.
- $0.8\text{ ppm} > 0.5\text{ ppm}$ needed limit. **Yes, it is sufficient.**
</details>

---

## Key Takeaways from Chapter 3

```
┌─────────────────────────────────────────────────────┐
│                   PPM SUMMARY                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Formula: ppm = (W_solute / W_solution) × 10⁶       │
│                                                      │
│  Key relationship: 1% = 10,000 ppm                  │
│                                                      │
│  For dilute aqueous solutions:                       │
│      ppm ≈ mg/L ≈ mg/kg                            │
│      (because d_solution ≈ 1 g/mL)                  │
│                                                      │
│  Temperature: INDEPENDENT ✅ (mass-based)            │
│                                                      │
│  Most common exam topic:                             │
│      Water hardness in ppm of CaCO₃                 │
│                                                      │
│  ppb = parts per billion = ppm × 10⁻³               │
│      1 ppm = 1000 ppb                               │
│                                                      │
│  Conversions:                                        │
│      ppm → mass%: divide by 10⁴                     │
│      mass% → ppm: multiply by 10⁴                   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

*← [Chapter 2 — Volume Percent](./02-volume-percent.md) | [Chapter 4 — Mole Fraction →](./04-mole-fraction.md)*
