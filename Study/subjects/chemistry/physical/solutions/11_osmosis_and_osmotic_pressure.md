# Chapter 11: Osmosis & Osmotic Pressure
## Part V — Colligative Properties

---

## 🎯 Stage 1: The Core Idea

### The Semipermeable Membrane Analogy

Imagine a net bag full of sugar water, submerged in pure water. The bag's mesh is small enough for water molecules to pass through, but the sugar molecules can't fit. What happens?

Water rushes in. The bag swells. This spontaneous flow is **osmosis**.

**Osmosis:** The spontaneous flow of solvent from a region of lower solute concentration to higher solute concentration through a semipermeable membrane (SPM).

> Key phrase: **"Low concentration to high concentration"** (or equivalently: high VP side to low VP side, or dilute to concentrated).

### What Stops Osmosis?

Apply extra pressure on the concentrated side. At a certain pressure, the flow stops. This pressure is the **osmotic pressure (π)**.

Alternatively: Reverse osmosis — apply pressure *greater* than π on the concentrated side to push water backward through the membrane (used in water purification).

### Three Key Concentration Terms

| If... | Outcome |
|-------|---------|
| π_solution > π_blood | **Hypertonic** — cell shrinks (crenation) |
| π_solution = π_blood | **Isotonic** — no net flow |
| π_solution < π_blood | **Hypotonic** — cell swells (hemolysis) |

---

## 🔬 Stage 2: The Formula Lab

### Van't Hoff Equation for Osmotic Pressure

```
π = CRT = nRT/V = (n/V)RT

where:
    π = osmotic pressure (atm or Pa)
    C = molarity (mol/L)
    R = 0.0821 L·atm/(mol·K)  [or 8.314 J/(mol·K)]
    T = temperature in Kelvin (always!)
    n = moles of solute
    V = volume of solution (L)
```

### For Electrolytes (with van't Hoff factor)

```
π = iCRT
```

### Alternative Form — Molar Mass

```
π = (W_solute × R × T)/(MM_solute × V)

→ MM = (W × R × T)/(π × V)
```

### Isotonic Solutions

```
Two solutions are isotonic if:
    π₁ = π₂ → C₁ = C₂ (same Molarity)
```

### Reverse Osmosis

```
Applied pressure > π → solvent flows from concentrated to dilute
(opposite to natural osmosis direction)

Used in: water purification, desalination
```

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: Calculating Osmotic Pressure

**Pattern:** Given C and T → find π.

#### Solved Example 11.1
**Q:** 1.8 g glucose (MM=180) in 300 mL water at 27°C. Find π. 🟢 ⭐

```
C = n/V = (1.8/180) / 0.300 = 0.01/0.300 = 0.0333 mol/L
T = 27 + 273 = 300 K
π = CRT = 0.0333 × 0.0821 × 300 = 0.820 atm

Answer: π ≈ 0.82 atm
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 11.1a | 6 g urea (MM=60) in 500 mL at 27°C. Find π. | 🟢 |
| 11.1b | 0.1 M NaCl (i=2) at 300 K. Find π. | 🟢 |
| 11.1c | π = 2.46 atm at 298 K. Find C. | 🟢 |
| 11.1d | At 37°C, blood has π = 7.65 atm. What must be the molarity of saline to be isotonic with blood? ⭐ | 🟡 |
| 11.1e | 5 L of 0.1 M glucose at 300 K. Find π. | 🟢 |
| DPP 11.4 | Osmotic pressure is 0.0821 atm at temperature of 300 K. Find concentration in mole/litre: (A) 0.033 (B) 0.066 (C) 0.33 × 10⁻² (D) 3 | 🟢 |

<details>
<summary>💡 Solutions for Type 1</summary>

**11.1a:** n = 6/60 = 0.1 mol; C = 0.1/0.5 = 0.2 M; **π = 0.2×0.0821×300 = 4.93 atm**

**11.1b:** π = iCRT = 2×0.1×0.0821×300 = **4.93 atm**

**11.1c:** C = π/(RT) = 2.46/(0.0821×298) = 2.46/24.47 = **0.1005 M ≈ 0.1 M**

**11.1d:** C = π/(RT) = 7.65/(0.0821×310) = 7.65/25.451 = **0.3006 M ≈ 0.3 M**

**11.1e:** π = CRT = 0.1×0.0821×300 = **2.463 atm**

**DPP 11.4:** Formula: π = CRT → 0.0821 = C × 0.0821 × 300 → C × 300 = 1 → C = 1 / 300 = 0.00333 mol/L = **0.33 × 10⁻² mol/litre → Answer: (C)**
</details>

---

### Type 2: Finding Molar Mass from Osmotic Pressure

**Pattern:** Osmotic pressure and mass given → find MM. This is the **most sensitive** colligative method — preferred for large molecules.

#### Solved Example 11.2
**Q:** 200 cm³ solution containing 1.26 g haemoglobin at 300 K has π = 3.65 mm Hg. Find MM. 🔴 ⭐

```
Convert units:
    π = 3.65 mm Hg × (1 atm/760 mm Hg) = 0.004803 atm
    V = 200 cm³ = 0.200 L

MM = WRT/(πV) = (1.26 × 0.0821 × 300)/(0.004803 × 0.200)
   = 31.033/(9.606 × 10⁻⁴)
   = 31.033/0.0009606
   = 32,305 g/mol ≈ 3.23 × 10⁴ g/mol
```

> **Why osmometry for large MM?** For large MM, molality is tiny. ΔT_b and ΔT_f are too small to measure accurately. But osmotic pressure can be large even for dilute solutions — making it ideal.

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 11.2a | 3.4 g sucrose in 250 mL at 27°C gives π = 2.46 atm. Verify MM (expected 342 g/mol). ⭐ | 🟡 |
| 11.2b | 0.1 L solution with 0.5 g protein at 27°C. π = 4.93×10⁻³ atm. Find MM. | 🔴 |
| 11.2c | MM of a polymer = 1.2×10⁴. 0.5 g in 100 mL at 300 K. Find π. | 🔴 |
| 11.2d | Why is osmotic pressure preferred for determining molar mass of biopolymers? | 🟡 |

<details>
<summary>💡 Solutions for Type 2</summary>

**11.2a:** MM = WRT/(πV) = (3.4×0.0821×300)/(2.46×0.250) = 83.742/0.615 = **136.2 ≈ 342?**
*(Re-check: n = π×V/(RT) = (2.46×0.250)/(0.0821×300) = 0.615/24.63 = 0.02497 mol; MM = 3.4/0.02497 = 136.2 — this gives 136, not 342. Possible discrepancy in problem data)*
*(If π = 0.82 atm: n = 0.82×0.25/24.63 = 0.00832 mol; MM = 3.4/0.00832 = 408 ≈ close to 342)*
*(Adjust π: π for sucrose 0.1M = 0.1×24.63 = 2.463 atm for 0.1M; C = 3.4/342/0.250 = 0.03977 M; π = 0.03977×24.63 = 0.98 atm)*

**11.2b:** n = πV/RT = (4.93×10⁻³×0.1)/(0.0821×300) = 4.93×10⁻⁴/24.63 = 2.002×10⁻⁵ mol
**MM = 0.5/2.002×10⁻⁵ = 24,975 g/mol ≈ 2.5×10⁴ g/mol**

**11.2c:** n = 0.5/(1.2×10⁴) = 4.167×10⁻⁵ mol; C = 4.167×10⁻⁵/0.1 = 4.167×10⁻⁴ M
**π = CRT = 4.167×10⁻⁴×0.0821×300 = 1.027×10⁻² atm = 7.80 mm Hg**

**11.2d:** For biopolymers (MM ~ 10⁴–10⁶), even 0.001 M gives π = 0.001×24.63 = 0.025 atm = 19 mm Hg — easily measurable. In contrast, ΔT_f = K_f×m ≈ 1.86×0.001 = 0.00186°C — too small to measure accurately. Osmometry is 1000× more sensitive.
</details>

---

### Type 3: Isotonic Solutions

**Pattern:** Two solutions are isotonic if same π → same C. Find what mass or concentration makes them isotonic.

#### Solved Example 11.3
**Q:** 0.9% NaCl (saline) is isotonic with blood at 37°C. Find π of blood. (MM of NaCl = 58.5, i = 2) 🟡 ⭐

```
0.9% NaCl = 0.9 g NaCl per 100 mL
C = (0.9/58.5) / 0.1 = 0.01538/0.1 = 0.1538 M

π = iCRT = 2 × 0.1538 × 0.0821 × 310 = **7.82 atm**
```

#### Solved Example 11.4
**Q:** What concentration of sucrose (MM = 342) solution would be isotonic with 0.154 M NaCl (i = 2) at same temperature? 🟡

```
Isotonic → same π
π_saline = 2 × 0.154 = 0.308 mol equivalent/L (in terms of effective C)
π_sucrose = C_sucrose (i=1)

C_sucrose = 2 × 0.154 = 0.308 M
Mass per litre = 0.308 × 342 = 105.3 g/L
```

#### Practice Questions — Type 3

| # | Question | Difficulty |
|---|----------|------------|
| 11.3a | Blood π = 7.65 atm at 310 K. What % NaCl (i=2) solution is isotonic? (MM=58.5) ⭐ | 🔴 |
| 11.3b | Which solution is hypertonic to 0.1 M glucose? (A) 0.1 M urea, (B) 0.2 M glucose, (C) 0.05 M NaCl, (D) 0.1 M NaCl | 🟡 |
| 11.3c | A solution of glucose (5%) and a solution of urea (x%) are isotonic. Find x. (MM_glucose=180, MM_urea=60) | 🟡 |

<details>
<summary>💡 Solutions for Type 3</summary>

**11.3a:** C_isotonic = π/(iRT) = 7.65/(2×0.0821×310) = 7.65/50.90 = 0.1503 M
Mass per 100 mL = 0.1503×0.1×58.5 = 0.879 g → **0.88% NaCl**

**11.3b:** π_glucose(0.1M) = 0.1×RT. Need π > 0.1×RT.
- (A) 0.1 M urea: π = 0.1×RT → isotonic
- **(B) 0.2 M glucose: π = 0.2×RT > 0.1×RT → hypertonic ✓**
- (C) 0.05 M NaCl: effective = 2×0.05=0.1 → isotonic
- (D) 0.1 M NaCl: effective = 0.2 → **also hypertonic**
- *(Both B and D are correct; if single answer needed: D has higher effective C)*

**11.3c:** C_glucose = 5%×1000/180 per L (need density or approximate)
Simple approach: per 100 g soln: glucose 5g = 5/180 mol; urea x g = x/60 mol
For same volume (isotonic → same C, same V): 5/180 = x/60 → **x = 5×60/180 = 1.67%**
</details>

---

### Type 4: Reverse Osmosis and Osmotic Pressure Direction

**Pattern:** Determine direction of flow or whether applied pressure causes RO.

#### Solved Example 11.5
**Q:** Sea water has π = 25 atm. What minimum pressure must be applied to cause reverse osmosis? 🟢

```
Applied pressure must exceed osmotic pressure.
Minimum pressure = π = 25 atm (just to stop normal osmosis)
To cause RO: pressure > 25 atm.

Minimum pressure for RO = just greater than 25 atm.
```

#### Solved Example 11.6
**Q:** Two solutions A (1% urea) and B (3.42% sucrose, MM=342) are separated by SPM. In which direction does water flow? 🟡 ⭐

```
Per 100 g solution (approximation: volume ≈ 100 mL):
    C_urea = (1/60)/0.1 = 0.1667 M
    C_sucrose = (3.42/342)/0.1 = 0.01/0.1 = 0.1 M

π_urea = 0.1667×RT
π_sucrose = 0.1×RT

π_urea > π_sucrose → A is more concentrated → B is dilute side

Osmosis: water flows from dilute (B) to concentrated (A)
→ Water flows from sucrose solution to urea solution.
```

#### Practice Questions — Type 4

| # | Question | Difficulty |
|---|----------|------------|
| 11.4a | Osmosis: water flows from A to B. Which has higher concentration — A or B? | 🟢 |
| 11.4b | Salt water and fresh water separated by SPM. In which direction does water flow in natural osmosis? | 🟢 |
| 11.4c | Pressure of 30 atm is applied to 25 atm seawater. Does RO occur? Which way does water flow? ⭐ | 🟡 |

<details>
<summary>💡 Solutions for Type 4</summary>

**11.4a:** Water flows from A to B → A is **less concentrated** (lower π, higher VP), B is more concentrated. Water flows from dilute to concentrated.

**11.4b:** Salt water (concentrated) → fresh water (dilute) by applying pressure would be RO. In natural osmosis: **water flows from fresh water into salt water.**

**11.4c:** Applied pressure (30 atm) > π (25 atm) → **RO occurs. Water flows from salt water to fresh water side** (against natural osmosis direction → purification of salt water).
</details>

---

### Type 5: Comparison of Colligative Properties

**Pattern:** Given data, identify which colligative property is most/least sensitive.

#### Solved Example 11.7
**Q:** For 0.001 m aqueous solution of haemoglobin (MM ~ 68,000), calculate expected ΔT_f and π at 300 K. Which is more measurable? 🔴 ⭐

```
ΔT_f = K_f × m = 1.86 × 0.001 = 0.00186°C (too small to measure)

C ≈ m = 0.001 M (dilute approximation)
π = CRT = 0.001 × 0.0821 × 300 = 0.02463 atm = 18.72 mm Hg (measurable!)

Answer: Osmotic pressure is far more useful for such large MM solutes.
```

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types | Difficulty |
|---|----------|-------|------------|
| 11.M1 | 6 g urea (MM=60) in 500 mL at 300 K. Find π. If 0.5 L of 0.2 M glucose is added, find new π. | T1+T1 | 🟡 |
| 11.M2 | RBC has π = 7.65 atm at 37°C. If placed in 0.5% NaCl (MM=58.5, i=2) solution, what happens? ⭐ | T3 | 🔴 |
| 11.M3 | 1 g polymer in 500 mL water at 27°C has π = 0.0246 atm. Find MM. Then find ΔT_f if K_f=1.86. Which is more measurable? | T2+T1 | 🔴 |

<details>
<summary>💡 Solutions for Type Mixer</summary>

**11.M1:**
- n_urea = 0.1 mol; C_urea = 0.2 M; **π = 0.2×0.0821×300 = 4.93 atm**
- After adding glucose: total V = 1 L; n_urea = 0.1 mol; n_glucose = 0.1 mol; total n = 0.2
- C_total = 0.2 M; **π_new = 0.2×0.0821×300 = 4.93 atm** *(same because C_glucose = 0.1M and C_urea = 0.1M gives same total)*

**11.M2:**
- π_solution(NaCl) = iCRT = 2×(0.5/58.5/0.1)×0.0821×310 = 2×0.0855×25.45 = **4.35 atm**
- π_blood = 7.65 atm > π_solution = 4.35 atm
- Solution is **hypotonic** compared to blood
- RBC placed in hypotonic solution → water flows INTO cell → **cell swells and may burst (hemolysis)**

**11.M3:**
- MM = WRT/(πV) = (1×0.0821×300)/(0.0246×0.5) = 24.63/0.0123 = **2002.4 ≈ 2000 g/mol**
- m ≈ C = 1/(2000×0.5L/1000) = 0.001 mol/kg
- ΔT_f = 1.86×0.001 = **0.00186°C** (immeasurable)
- π = 0.0246 atm = 18.7 mm Hg (easily measured with osmometer)
- **Osmotic pressure is more measurable ✓**
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 11.B1 | Define osmosis and osmotic pressure. *(NCERT)* | 🟢 |
| 11.B2 | What is the difference between isotonic, hypertonic, and hypotonic solutions? Give examples. ⭐ | 🟡 |
| 11.B3 | Explain why reverse osmosis is used in water purification. | 🟢 |
| 11.B4 | 200 mL solution of haemoglobin at 300 K has π = 2.57 × 10⁻³ atm. If 1.26 g of Hb is present, find MM. *(NCERT pattern)* ⭐ | 🔴 |
| 11.B5 | 5% (w/w) glucose (MM=180) vs 5% (w/w) sucrose (MM=342) — which has higher osmotic pressure? | 🟡 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**11.B1:** Osmosis = spontaneous flow of solvent through a semipermeable membrane from a region of lower concentration (or lower solute, higher VP) to higher concentration. Osmotic pressure = the minimum pressure that must be applied on the concentrated side to just stop osmotic flow.

**11.B2:**
- **Isotonic:** Same π as reference (cell). No net water movement. Example: 0.9% NaCl (normal saline) with respect to blood.
- **Hypertonic:** Higher π. Causes water to flow OUT of cell → cell shrinks (crenation). Example: concentrated salt water.
- **Hypotonic:** Lower π. Causes water to flow INTO cell → cell swells (hemolysis). Example: distilled water.

**11.B3:** In RO, pressure greater than π is applied on the concentrated (salt water) side. This forces water to flow backward through the SPM (from salty to fresh side), effectively filtering out dissolved salts. Used in desalination of seawater and removal of dissolved contaminants.

**11.B4:** MM = WRT/(πV) = (1.26 × 0.0821 × 300)/(2.57×10⁻³ × 0.200)
= 31.03/(5.14×10⁻⁴) = **60,370 g/mol ≈ 6.0×10⁴ g/mol**

**11.B5:** Per 100 g solution: glucose = 5g, sucrose = 5g
C_glucose = (5/180) per 100 mL = 0.02778 mol/100 mL = 0.2778 M
C_sucrose = (5/342) per 100 mL = 0.01462 mol/100 mL = 0.1462 M
C_glucose > C_sucrose → **π_glucose > π_sucrose**
(Same mass but lower MM → more moles → higher concentration → higher π)
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q11.J1 🟡 ⭐**
1.8 g of glucose (MM=180) is dissolved in 1 L water at 27°C. The osmotic pressure is:
(A) 0.082 atm  (B) 0.246 atm  (C) 2.46 atm  (D) 0.820 atm

**Q11.J2 🟡 ⭐**
Saline used for IV injection must be isotonic with blood (π = 7.65 atm at 310 K, i=2 for NaCl, MM=58.5). The % (w/v) of NaCl in such saline is approximately:
(A) 0.9%  (B) 1.8%  (C) 0.45%  (D) 2%

**Q11.J3 🔴**
A semipermeable membrane separates 0.1 M urea from 0.2 M sucrose. In which direction does water flow, and what is the initial osmotic pressure difference?
(A) To urea side; Δπ = 0.1×RT  (B) To sucrose side; Δπ = 0.1×RT
(C) To sucrose side; Δπ = 0.2×RT  (D) No flow

**Q11.J4 🔴 ⭐**
500 mL solution at 27°C has π = 0.5 atm. What is the MM of solute if 10 g was dissolved?
(A) 500 g/mol  (B) 200 g/mol  (C) 1000 g/mol  (D) 250 g/mol

**Q11.J5 🔴 ⭐**
Which colligative property is most useful for determining molar mass of proteins and polymers?
(A) Elevation of boiling point  (B) Depression of freezing point
(C) Osmotic pressure  (D) Relative lowering of vapour pressure

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**11.J1 → Answer: (B)**
- C = (1.8/180)/1 = 0.01 M; T = 300 K
- **π = 0.01 × 0.0821 × 300 = 0.2463 ≈ 0.246 atm ✓**

**11.J2 → Answer: (A)**
- C = π/(iRT) = 7.65/(2×0.0821×310) = 7.65/50.90 = 0.1503 M
- % (w/v) = C×MM×100 per 1000 mL = 0.1503×58.5×100/1000 = **0.879% ≈ 0.9% ✓**

**11.J3 → Answer: (B)**
- π_urea = 0.1×RT; π_sucrose = 0.2×RT → sucrose side is more concentrated
- Water flows from dilute (urea) to concentrated (sucrose)
- **To sucrose side; Δπ = (0.2−0.1)×RT = 0.1×RT ✓**

**11.J4 → Answer: (A)**
- MM = WRT/(πV) = (10×0.0821×300)/(0.5×0.5) = 246.3/0.25 = **985.2 ≈ 1000 g/mol → (C)**
- *(Let me verify: 10g, V=0.5L, T=300K, π=0.5atm; n=πV/RT=0.5×0.5/(0.0821×300)=0.25/24.63=0.01015 mol; MM=10/0.01015=985 ≈ 1000 → (C))*

**11.J5 → Answer: (C)**
- For large MM: even small concentrations give measurable π (tens of mm Hg)
- ΔT_b and ΔT_f are typically < 0.01°C → immeasurable
- RLVP also immeasurably small for very dilute solutions
- **Osmotic pressure is most useful ✓**
</details>

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
| 11.S1 | **Assertion (A):** In osmosis, solvent molecules flow strictly in one direction: from the dilute solution to the concentrated solution.<br>**Reason (R):** The semipermeable membrane blocks all movement of solvent molecules from the concentrated side to the dilute side. | 🔴 |
| 11.S2 | **Statement I:** Osmotic pressure is the pressure exerted by the solute molecules striking the semipermeable membrane.<br>**Statement II:** Osmotic pressure is an externally applied mechanical pressure required to stop the net flow of solvent. | 🟡 |
| 11.S3 | **Assertion (A):** A $0.1\text{ M}$ solution of $NaCl$ is hypertonic to a $0.1\text{ M}$ solution of glucose.<br>**Reason (R):** $NaCl$ dissociates into two ions, creating a higher effective particle concentration ($0.2\text{ M}$) than glucose ($0.1\text{ M}$). | 🟢 |
| 11.S4 | **Statement I:** If a red blood cell is placed in pure distilled water, it will undergo plasmolysis (shrinking).<br>**Statement II:** Distilled water is hypertonic compared to the intracellular fluid of the red blood cell. | 🟢 |
| 11.S5 | **Assertion (A):** Osmotic pressure ($\pi$) can be calculated using the formula $\pi = C R T$, where $C$ is the molality of the solution.<br>**Reason (R):** Colligative properties must be independent of temperature, hence molality is always preferred over molarity in theoretical derivations. | 🟡 |
| 11.S6 | **Statement I:** During reverse osmosis, solvent molecules move from a region of higher solute concentration to a region of lower solute concentration.<br>**Statement II:** Reverse osmosis is a non-spontaneous process driven by an external pressure greater than the osmotic pressure. | 🟢 |
| 11.S7 | **Assertion (A):** A $5\%$ (w/v) solution of cane sugar (sucrose) is isotonic with a $5\%$ (w/v) solution of urea.<br>**Reason (R):** Both solutions contain the same mass of solute per unit volume. | 🟡 |
| 11.S8 | **Statement I:** For a given dilute solution at constant temperature, osmotic pressure is directly proportional to its concentration in molarity.<br>**Statement II:** The Van't Hoff equation $\pi = C R T$ mathematically mimics the ideal gas law $P = \frac{n}{V} R T$. | 🟢 |
| 11.S9 | **Assertion (A):** Osmotic pressure measurement is preferred over freezing point depression for finding the molar mass of proteins.<br>**Reason (R):** Proteins are sensitive to temperature changes and might denature, and their large molar masses produce highly measurable osmotic pressures but unreadably small freezing point depressions. | 🟢 |
| 11.S10 | **Statement I:** If two solutions are separated by a semipermeable membrane, solvent will always flow from the side with higher vapour pressure to the side with lower vapour pressure.<br>**Statement II:** A dilute solution has a higher vapour pressure than a concentrated solution of the same non-volatile solute. | 🟡 |
| 11.S11 | **Assertion (A):** Addition of a non-volatile solute to a solvent increases its osmotic pressure.<br>**Reason (R):** Pure solvent has an osmotic pressure of zero. | 🟢 |
| 11.S12 | **Statement I:** When a solution is separated from pure solvent by a semipermeable membrane, the osmotic pressure is generated spontaneously inside the solution.<br>**Statement II:** Osmotic pressure is an inherent thermodynamic property of a solution, exactly like vapour pressure, and exists whether a membrane is present or not. | 🔴 |
| 11.S13 | **Assertion (A):** A $0.1\text{ M}$ solution of $BaCl_2$ and a $0.15\text{ M}$ solution of $NaCl$ are isotonic (assuming complete dissociation).<br>**Reason (R):** Both solutions have an effective particle concentration of $0.3\text{ M}$. | 🟡 |
| 11.S14 | **Statement I:** In natural osmosis, water moves from a region of lower water concentration to a region of higher water concentration.<br>**Statement II:** "Lower solute concentration" is synonymous with "higher solvent (water) concentration". | 🟡 |
| 11.S15 | **Assertion (A):** The unit of the gas constant $R$ used in the equation $\pi = C R T$ is generally $0.0821\text{ L atm K}^{-1} \text{mol}^{-1}$ when $\pi$ is in atm.<br>**Reason (R):** Using $8.314\text{ J K}^{-1} \text{mol}^{-1}$ would yield osmotic pressure in units of Pascals ($N/m^2$), provided volume is in cubic meters ($m^3$). | 🟢 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**11.S1 → Answer: (C) A is true but R is false.**
- A is true: NET flow is from dilute to concentrated.
- R is false: Solvent molecules cross the membrane in BOTH directions continuously. However, the rate of flow from dilute to concentrated is faster, resulting in a NET flow in one direction.

**11.S2 → Statement I is False, Statement II is True.**
- Statement I is false: Osmotic pressure is NOT the kinetic collision pressure of solute molecules. It is a thermodynamic phenomenon driven by differences in chemical potential (or vapour pressure).
- Statement II is true: It is defined as the external mechanical pressure required to halt the net flow.

**11.S3 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- $NaCl$ ($i=2$) creates $0.2\text{ M}$ effective particles. Glucose ($i=1$) creates $0.1\text{ M}$. Higher effective concentration = hypertonic.

**11.S4 → Statement I is False, Statement II is False.**
- Statement I is false: Distilled water is hypotonic. Water flows INTO the cell, causing it to swell and burst (hemolysis), not shrink (plasmolysis/crenation).
- Statement II is false: Distilled water has zero solutes, making it strictly hypotonic to cell fluid.

**11.S5 → Answer: (D) A is false but R is true.**
- A is false: The formula is $\pi = C R T$, where $C$ is MOLARITY (mol/L), not molality.
- R is true: While molality is independent of temperature and preferred in $\Delta T_b / \Delta T_f$, the Van't Hoff equation specifically relies on Molarity ($n/V$).

**11.S6 → Statement I is True, Statement II is True.**
- This is the exact definition and mechanism of reverse osmosis.

**11.S7 → Answer: (D) A is false but R is true.**
- A is false: Isotonic means same $\pi$, which requires same MOLARITY. $5\%$ cane sugar ($MM=342$) and $5\%$ urea ($MM=60$) have vastly different molarities.
- R is true: $5\%$ (w/v) means $5\text{ g}$ per $100\text{ mL}$ for both, so they do have the same mass per unit volume.

**11.S8 → Statement I is True, Statement II is True.**
- Van't Hoff observed that dilute solutions behave thermodynamically similarly to ideal gases, hence the analogous equation.

**11.S9 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- Proteins denature if boiled or frozen, and their massive molar mass makes $\Delta T$ values practically zero. Osmotic pressure provides large, readable values at room temperature.

**11.S10 → Statement I is True, Statement II is True.**
- This is an excellent alternative definition of osmosis. Solvent moves from High VP (dilute side) to Low VP (concentrated side) to establish equilibrium.

**11.S11 → Answer: (B) Both A and R are true, but R is NOT the correct explanation.**
- A is true: Adding solute increases $\pi$.
- R is true: Pure solvent doesn't have an osmotic pressure by itself (it's the baseline). But the *explanation* for why $\pi$ increases is because solute lowers the solvent's chemical potential, requiring pressure to restore equilibrium, not simply because the baseline is zero.

**11.S12 → Statement I is False, Statement II is False.**
- Statement I is false: Osmotic pressure is NOT generated "inside" the solution. It is the external pressure YOU must apply to stop flow.
- Statement II is false: Unlike vapour pressure, osmotic pressure only manifests when the solution is separated from pure solvent (or a different concentration) by an SPM. It is not an inherent property of an isolated beaker of solution.

**11.S13 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- $BaCl_2 \rightarrow 3$ ions. Effective $C = 3 \times 0.1 = 0.3\text{ M}$.
- $NaCl \rightarrow 2$ ions. Effective $C = 2 \times 0.15 = 0.3\text{ M}$. Same effective $C$ = isotonic.

**11.S14 → Statement I is False, Statement II is True.**
- Statement I is false: Water moves from a region of HIGHER water concentration (dilute solution) to LOWER water concentration (concentrated solution).
- Statement II is true: The wording in Statement I was flipped.

**11.S15 → Answer: (A) Both A and R are true, and R is the correct explanation.**
- This highlights the importance of unit matching. If volume is in litres and pressure in atm, use $0.0821$. If SI units ($m^3$, Pascals) are used, use $8.314$.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Directions:** These questions feature meticulously designed traps. Read every word. Check your units. Don't trust your instincts blindly.

**Q11.M1 🟢**
If $3.0\text{ g}$ of an unknown non-electrolyte is dissolved in $250\text{ mL}$ of solution at $27^\circ\text{C}$, the osmotic pressure is found to be $1.23\text{ atm}$. The molar mass of the solute is closest to: ($R = 0.0821\text{ L atm / K mol}$)
(A) $120\text{ g/mol}$
(B) $240\text{ g/mol}$
(C) $60\text{ g/mol}$
(D) $300\text{ g/mol}$

**Q11.M2 🟡 (The "Percentage Isotonic" Trap)**
A $4\%$ (w/v) solution of a non-volatile solute A is isotonic with a $10\%$ (w/v) solution of solute B. If the molar mass of B is $200\text{ g/mol}$, what is the molar mass of A?
(A) $80\text{ g/mol}$
(B) $500\text{ g/mol}$
(C) $100\text{ g/mol}$
(D) $40\text{ g/mol}$

**Q11.M3 🔴**
Two solutions, A ($0.1\text{ M}$ Urea) and B ($0.1\text{ M}$ $NaCl$), are separated by a semipermeable membrane. Which of the following statements is correct?
(A) Solvent flows from B to A because $NaCl$ is heavier.
(B) Solvent flows from A to B because B is hypertonic.
(C) No flow occurs because they are equimolar.
(D) Solute $NaCl$ flows into A to equalize concentration.

**Q11.M4 🟡**
To prepare an aqueous solution isotonic with blood ($7.65\text{ atm}$ at $37^\circ\text{C}$), what mass of glucose ($MM = 180$) should be dissolved per litre of solution?
(A) $27.3\text{ g}$
(B) $54.1\text{ g}$
(C) $30.0\text{ g}$
(D) $9.0\text{ g}$

**Q11.M5 🟡 (The "Temperature Dependency" Trap)**
If the temperature of a dilute solution is doubled (in Kelvin) while keeping the volume constant, its osmotic pressure will:
(A) Halve
(B) Double
(C) Remain constant
(D) Quadruple

**Q11.M6 🔴**
An aqueous solution of $K_2SO_4$ has an osmotic pressure of $3.0\text{ atm}$ at $27^\circ\text{C}$. Assuming complete dissociation, what is the approximate MOLARITY of the solution?
(A) $0.12\text{ M}$
(B) $0.04\text{ M}$
(C) $0.36\text{ M}$
(D) $0.08\text{ M}$

**Q11.M7 🟡**
Which of the following pairs of solutions are isotonic at the same temperature?
(A) $0.1\text{ M}$ Urea and $0.1\text{ M}$ $NaCl$
(B) $0.1\text{ M}$ $CaCl_2$ and $0.15\text{ M}$ $NaCl$
(C) $0.1\text{ M}$ $Al_2(SO_4)_3$ and $0.1\text{ M}$ $BaCl_2$
(D) $0.2\text{ M}$ Glucose and $0.1\text{ M}$ $Na_2SO_4$

**Q11.M8 🟢**
Reverse osmosis is applied to seawater. The membrane allows the passage of:
(A) $Na^+$ and $Cl^-$ ions only
(B) Water molecules only
(C) Both water molecules and ions
(D) Gases dissolved in water only

**Q11.M9 🔴 (The "Reverse Pressure" Trap)**
A solution has an osmotic pressure of $5\text{ atm}$. A mechanical pressure of $3\text{ atm}$ is applied to the solution side. What will happen?
(A) Reverse osmosis occurs.
(B) Natural osmosis continues, but at a reduced rate.
(C) Net flow of solvent stops completely.
(D) Solute is pushed through the membrane.

**Q11.M10 🟡**
For a highly polymeric substance, the osmotic pressure at $298\text{ K}$ is $0.002\text{ atm}$ for a concentration of $10\text{ g/L}$. The molar mass of the polymer is:
(A) $\sim 1.2 \times 10^5\text{ g/mol}$
(B) $\sim 1.2 \times 10^4\text{ g/mol}$
(C) $\sim 6.0 \times 10^4\text{ g/mol}$
(D) $\sim 2.4 \times 10^5\text{ g/mol}$

**Q11.M11 🔴**
A $0.1\text{ M}$ solution of a weak monobasic acid ($HA$) has an osmotic pressure of $2.6\text{ atm}$ at $300\text{ K}$. What is the degree of dissociation ($\alpha$) of the acid? ($R = 0.0821$)
(A) $0.05$
(B) $0.10$
(C) $0.02$
(D) $0.15$

**Q11.M12 🟡**
Which condition guarantees that two solutions will NOT be isotonic?
(A) Different molar masses of solutes.
(B) Different mass percentages of solutes.
(C) Different effective molarities ($i \times C$).
(D) Different densities.

**Q11.M13 🟢**
If a plant cell shrinks when placed in a solution, the solution is:
(A) Hypotonic
(B) Hypertonic
(C) Isotonic
(D) A saturated solution

**Q11.M14 🔴 (The "Unit Disaster" Trap)**
A student calculates molar mass using $MM = \frac{W R T}{\pi V}$. They input $W = 5\text{ g}$, $T = 300\text{ K}$, $\pi = 760\text{ mm Hg}$, $V = 1\text{ L}$, and $R = 0.0821$. What glaring error did they make?
(A) $V$ should be in $mL$.
(B) $W$ should be in $kg$.
(C) $\pi$ must be converted to $atm$ when using $R = 0.0821$.
(D) $T$ should be in Celsius.

**Q11.M15 🟡**
At $27^\circ\text{C}$, the osmotic pressure of a solution containing $4.0\text{ g}$ of a solute in $100\text{ mL}$ is $10\text{ atm}$. What will be the osmotic pressure if the solution is diluted to $500\text{ mL}$ at the same temperature?
(A) $10\text{ atm}$
(B) $50\text{ atm}$
(C) $2.0\text{ atm}$
(D) $0.5\text{ atm}$

<details>
<summary>💡 Full Solutions — Stage 8 MCQ Mastery</summary>

**Q11.M1 → Answer: (B)**
- $MM = \frac{W R T}{\pi V} = \frac{3.0 \times 0.0821 \times 300}{1.23 \times 0.25} = \frac{73.89}{0.3075} = 240.2\text{ g/mol}$.

**Q11.M2 → Answer: (A)**
- Isotonic $\implies C_A = C_B$.
- $4\%$ means $4\text{ g}$ in $100\text{ mL}$. $10\%$ means $10\text{ g}$ in $100\text{ mL}$.
- $C_A = \frac{4/MM_A}{0.1} = \frac{40}{MM_A}$. $C_B = \frac{10/200}{0.1} = \frac{0.05}{0.1} = 0.5\text{ M}$.
- $\frac{40}{MM_A} = 0.5 \implies MM_A = 40 / 0.5 = 80\text{ g/mol}$.

**Q11.M3 → Answer: (B)**
- A = $0.1\text{ M}$ Urea ($i=1 \implies 0.1\text{ M}$ effective).
- B = $0.1\text{ M}$ $NaCl$ ($i=2 \implies 0.2\text{ M}$ effective).
- B is more concentrated (hypertonic). Water flows from dilute (A) to concentrated (B).
- Trap: (D) Solutes generally do NOT cross semipermeable membranes.

**Q11.M4 → Answer: (B)**
- $\pi = 7.65\text{ atm}$, $T = 310\text{ K}$.
- $C = \pi / (RT) = 7.65 / (0.0821 \times 310) = 0.3006\text{ M}$.
- Since volume is $1\text{ L}$, moles needed $= 0.3006\text{ mol}$.
- Mass $= 0.3006 \times 180 = 54.1\text{ g}$.

**Q11.M5 → Answer: (B)**
- $\pi = C R T$. Since $\pi$ is directly proportional to absolute temperature $T$, doubling $T$ doubles $\pi$.

**Q11.M6 → Answer: (B)**
- $K_2SO_4 \rightarrow 2K^+ + SO_4^{2-}$ ($i=3$).
- $\pi = i C R T \implies 3.0 = 3 \times C \times 0.0821 \times 300$.
- $3.0 = 3 \times C \times 24.63 \implies 3.0 = 73.89 \times C$.
- $C = 3.0 / 73.89 \approx 0.0406\text{ M}$.

**Q11.M7 → Answer: (B)**
- Isotonic pairs must have the same $i \times C$.
- (A) $0.1 \times 1 \neq 0.1 \times 2$.
- (B) $0.1 \times 3 (CaCl_2) = 0.3$. $0.15 \times 2 (NaCl) = 0.3$. These are equal!
- (C) $0.1 \times 5 \neq 0.1 \times 3$.
- (D) $0.2 \times 1 \neq 0.1 \times 3$.

**Q11.M8 → Answer: (B)**
- A semipermeable membrane (SPM) used in RO only allows the solvent (water) to pass. It blocks all dissolved ions and solutes.

**Q11.M9 → Answer: (B)**
- To stop osmosis, you must apply EXACTLY $5\text{ atm}$.
- To cause reverse osmosis, you must apply $> 5\text{ atm}$.
- Since only $3\text{ atm}$ is applied, it opposes but does not overcome the osmotic pressure. Natural osmosis continues, but the net driving pressure is reduced to $5 - 3 = 2\text{ atm}$, so the rate is reduced.

**Q11.M10 → Answer: (A)**
- $C = \frac{10/MM}{1} = \frac{10}{MM}\text{ M}$.
- $\pi = C R T \implies 0.002 = \frac{10}{MM} \times 0.0821 \times 298$.
- $MM = \frac{10 \times 24.46}{0.002} = \frac{244.6}{0.002} = 122,300 \approx 1.2 \times 10^5\text{ g/mol}$.

**Q11.M11 → Answer: (A)**
- $\pi_{exp} = 2.6\text{ atm}$.
- $\pi_{theo} = C R T = 0.1 \times 0.0821 \times 300 = 2.463\text{ atm}$.
- $i = \pi_{exp} / \pi_{theo} = 2.6 / 2.463 = 1.055$.
- For weak monobasic acid, $n=2$ ($HA \rightarrow H^+ + A^-$).
- $\alpha = \frac{i-1}{n-1} = \frac{1.055-1}{2-1} = 0.055 \approx 0.05$. (Wait, $2.6 / 2.46 \approx 1.056$. So $\alpha \approx 5.6\%$).
- Option A ($0.05$) is the closest intended answer. Let's re-verify: $1.05 \times 2.46 = 2.583 \approx 2.6$.

**Q11.M12 → Answer: (C)**
- Isotonicity is strictly defined by equal effective molarities (osmolarity), which is $i \times C$. If this is different, they cannot be isotonic.

**Q11.M13 → Answer: (B)**
- If a cell shrinks (plasmolysis), water is leaving the cell. This means the outside solution is more concentrated (has a higher osmotic pressure) than the inside. The solution is hypertonic.

**Q11.M14 → Answer: (C)**
- The value $R = 0.0821$ has units of $\text{L \textbf{atm} K}^{-1} \text{mol}^{-1}$. Therefore, pressure MUST be in atmospheres ($atm$). Using $760\text{ mm Hg}$ directly will give an answer off by a factor of 760.

**Q11.M15 → Answer: (C)**
- Osmotic pressure is directly proportional to concentration $C$ ($\pi \propto C$).
- $C = n / V$. If volume increases from $100\text{ mL}$ to $500\text{ mL}$ (a 5-fold increase), the concentration becomes $1/5$th of the original.
- Therefore, $\pi$ also becomes $1/5$th of the original. $10\text{ atm} / 5 = 2.0\text{ atm}$.
</details>

---



| Formula | Meaning |
|---------|---------|
| π = CRT | Core osmotic pressure formula |
| π = iCRT | For electrolytes |
| MM = WRT/(πV) | Finding MM from osmometry |
| Isotonic: π₁ = π₂ | Same concentration, no net flow |
| Hypertonic | Higher π → cell shrinks |
| Hypotonic | Lower π → cell swells |

---

*Next: [Chapter 12 — Van't Hoff Factor & Abnormal Molar Mass →](./12_vant_hoff_factor.md)*
