# Chapter 3: Properties of Electric Charge

> *NCERT Section 1.5*

---

## 🎯 Stage 1: The Core Idea

Electric charge has three fundamental properties. Think of them as the *rules of the game* — every problem in electrostatics obeys these, no exceptions.

### Property 1: Additivity of Charges

Charges add up **algebraically** (not like scalars that are always positive).

If a system has charges q₁, q₂, q₃, ..., qₙ, then:

$$Q_{total} = q_1 + q_2 + q_3 + \cdots + q_n$$

The signs matter. +5 μC and −3 μC together give +2 μC, not 8 μC.

> **Analogy:** Think of charge like money in a bank account. Deposits are positive, withdrawals are negative. Your balance is the algebraic sum.

### Property 2: Conservation of Charge

The total charge of an **isolated system** never changes. Charge cannot be created or destroyed — only transferred.

This is one of the most fundamental conservation laws in physics, right alongside conservation of energy and momentum.

**Examples in nature:**
- Rubbing: Glass (+Q) + Silk (−Q) = 0 ✓
- Pair production: γ → e⁻ + e⁺ (0 → −e + e = 0) ✓
- β-decay: n → p + e⁻ + ν̄ₑ (0 → +1 − 1 + 0 = 0) ✓

### Property 3: Quantization of Charge ⭐

Charge comes in discrete packets. The smallest unit is:

$$e = 1.6 \times 10^{-19} \text{ C}$$

Any charge Q must be:

$$Q = ne \quad \text{where } n = 0, \pm1, \pm2, \pm3, \ldots$$

> **Analogy:** You can buy 1 egg, 2 eggs, 10 eggs — but never 1.5 eggs. Similarly, charge is "quantized" into indivisible units of *e*.

**Why don't we notice quantization in daily life?<br>**

Because *e* is incredibly small. A charge of 1 μC = 10⁻⁶ C contains about 6.25 × 10¹² elementary charges. At this scale, the "graininess" is invisible — like how sand looks smooth from an airplane.

> **At the macroscopic level, charge appears continuous. At the microscopic level, it's discrete.** This is why we can use continuous charge distributions (Chapter 9) without guilt.

---

## 🔬 Stage 2: The Formula Lab

### Formula 1: Additivity

$$Q_{total} = \sum_{i=1}^{n} q_i$$

- Charges are **algebraic** — include signs.
- Works for any system: point charges, distributed charges, etc.

### Formula 2: Conservation

$$Q_{before} = Q_{after} \quad \text{(for an isolated system)}$$

- "Isolated" means no charge enters or leaves the system boundary.
- This holds in ALL physical processes: chemical, nuclear, electromagnetic.

### Formula 3: Quantization

$$Q = ne$$

| Variable | Meaning | Unit |
|----------|---------|------|
| Q | Total charge | Coulomb <br>
(C)
 |
| n | Integer (positive, negative, or zero) | dimensionless |
| e | Elementary charge = 1.6 × 10⁻¹⁹ C | Coulomb <br>
(C)
 |

**Note on quarks:** Quarks carry charges of ±e/3 or ±2e/3, but they are **never observed in isolation** (confinement). So for all practical and exam purposes, e is the minimum free charge.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Find total charge of a system (Additivity) ⭐

**Solved Example** 🟢

> A system contains charges +3 μC, −5 μC, +7 μC, and −1 μC. Find the total charge.

**Solution:**
Q = (+3) + (−5) + (+7) + (−1) = **+4 μC**

**Practice:**

1. 🟢 Find total charge: +12 nC, −8 nC, +3 nC, −7 nC. *(Ans: 0)*
2. 🟢 A system has charges 2e, −3e, 5e, −e. What is the total charge in coulombs?<br> *(Ans: 3e = 4.8 × 10⁻¹⁹ C)*
3. 🟡 Three identical spheres carry charges +Q, +2Q, −4Q. They are all brought into contact simultaneously and then separated. What charge does each carry?<br> *(Ans: −Q/3 each)*

---

### Type 2: Conservation in contact problems ⭐

**Pattern:** "Two charged bodies touch and separate."

**Solved Example** 🟡

> Sphere A (+8 μC) and sphere B (−2 μC) are identical conducting spheres. They touch and separate. Find the charge on each.

**Solution:**
- Total charge = +8 + (−2) = +6 μC (conserved)
- Identical spheres share equally: Each = +6/2 = **+3 μC**

**Practice:**

1. 🟢 Spheres with +10 μC and −4 μC (identical) touch and separate. *(Ans: +3 μC each)*
2. 🟡 Sphere A (+6 μC, radius R) and Sphere B (−2 μC, radius 2R) touch and separate. Find charges. *(Hint: Charge distributes in ratio of radii for unequal spheres: q_A/q_B = R_A/R_B)*

<details>
<summary><b>Answer to Q2</b></summary>

Total = +4 μC. Ratio = R : 2R = 1 : 2.
q_A = 4 × (1/3) = **4/3 μC**
q_B = 4 × (2/3) = **8/3 μC**
</details>

3. 🔴 ⭐ Sphere A (+Q) touches B (neutral, identical). B then touches C (neutral, identical). Then C touches A. Find final charge on each.

<details>
<summary><b>Answer</b></summary>

Step 1: A touches B → each gets Q/2. A = Q/2, B = Q/2.
Step 2: B touches C → each gets Q/4. B = Q/4, C = Q/4.
Step 3: C touches A → Total = Q/2 + Q/4 = 3Q/4. Each gets 3Q/8.
A = 3Q/8, C = 3Q/8.

**Final: A = 3Q/8, B = Q/4, C = 3Q/8**
Total = 3Q/8 + Q/4 + 3Q/8 = 3Q/8 + 2Q/8 + 3Q/8 = 8Q/8 = Q ✓
</details>

---

### Type 3: Conservation in nuclear/particle reactions

**Solved Example** 🟡

> In β⁻ decay, a neutron transforms as: n → p + e⁻ + ν̄ₑ. Verify conservation of charge.

**Solution:**
- Before: charge of neutron = 0
- After: charge of proton (+e) + electron (−e) + antineutrino (0) = 0
- 0 = 0 ✓ **Charge is conserved.**

**Practice:**

1. 🟢 Verify charge conservation in pair production: γ → e⁻ + e⁺ *(Ans: 0 = −e + e = 0 ✓)*
2. 🟡 In pair annihilation: e⁻ + e⁺ → 2γ. Is charge conserved?<br> *(Ans: (−e + e) = 0, and 2γ = 0. Yes ✓)*
3. 🟡 In nuclear fission: ²³⁵U + n → ¹⁴⁴Ba + ⁸⁹Kr + 3n. Verify charge conservation. *(Ans: 92 + 0 = 56 + 36 + 0 = 92 ✓)*

---

### Type 4: Is this charge quantized?<br> ⭐

**Solved Example** 🟢

> Which of the following charges are possible?<br> (a) 4.0 × 10⁻¹⁹ C (b) 3.2 × 10⁻¹⁹ C (c) 6.4 × 10⁻¹⁹ C (d) 5.0 × 10⁻¹⁹ C

**Solution:**
- (a) n = 4.0/1.6 = 2.5 → **Not possible** ✗
- (b) n = 3.2/1.6 = 2 → **Possible** ✓
- (c) n = 6.4/1.6 = 4 → **Possible** ✓
- (d) n = 5.0/1.6 = 3.125 → **Not possible** ✗

**Practice:**

1. 🟢 Check: 0.8 × 10⁻¹⁹ C. *(Ans: n = 0.5, not possible)*
2. 🟢 Check: 1.6 × 10⁻²⁰ C. *(Ans: n = 0.1, not possible)*
3. 🟡 The minimum charge that can exist freely in nature is ___. *(Ans: 1.6 × 10⁻¹⁹ C = e. Quarks have smaller charges but don't exist freely.)*

---

### Type 5: Number of electrons for macroscopic charges

**Solved Example** 🟡

> How many electrons must be removed from a neutral body to give it a charge of +1 C?<br>

**Solution:**
n = Q/e = 1 / (1.6 × 10⁻¹⁹) = **6.25 × 10¹⁸ electrons**

> That's 6.25 billion billion electrons — an astronomically large number, showing how tiny the elementary charge is.

**Practice:**

1. 🟢 How many electrons are in 1 mC of charge?<br> *(Ans: 6.25 × 10¹⁵)*
2. 🟡 A copper coin (mass 3 g, atomic mass 63.5 u, Z = 29) has how many electrons?<br> *(Ans: ≈ 8.4 × 10²³)*
3. 🔴 What fraction of electrons in the coin from Q2 would need to be removed to give it a charge of +1 C?<br> *(Ans: ~7.4 × 10⁻⁶ → less than 1 in a million!)*

---

### Type 6: Additivity with vector-like sign considerations

**Solved Example** 🟡

> A hydrogen atom has 1 proton and 1 electron. What is the total charge?<br> A helium atom has 2 protons, 2 neutrons, and 2 electrons. Total charge?<br>

**Solution:**
- H: +e + (−e) = **0**
- He: 2(+e) + 2(0) + 2(−e) = **0**

All neutral atoms have zero net charge.

**Practice:**

1. 🟢 A Na⁺ ion has 11 protons and 10 electrons. What is its charge?<br> *(Ans: +e = 1.6 × 10⁻¹⁹ C)*
2. 🟢 An O²⁻ ion has 8 protons and 10 electrons. Charge?<br> *(Ans: −2e = −3.2 × 10⁻¹⁹ C)*
3. 🟡 In 1 mole of NaCl, what is the total charge?<br> *(Ans: 0 — equal Na⁺ and Cl⁻ ions)*

---

### Type 7: Charge conservation in chemical reactions

**Solved Example** 🟡

> In the reaction: Fe → Fe²⁺ + 2e⁻, verify charge conservation.

**Solution:**
- Before: Fe is neutral → charge = 0
- After: Fe²⁺ has charge +2e, and 2e⁻ has charge −2e → total = 0
- 0 = 0 ✓

**Practice:**

1. 🟢 Cu → Cu²⁺ + 2e⁻. Is charge conserved?<br> *(Ans: Yes)*
2. 🟡 2H₂ + O₂ → 2H₂O. Is charge conserved?<br> *(Ans: Yes — all neutral species, total charge = 0 throughout)*

---

### Type 8: Conceptual questions on properties

**Solved Example** 🟡

> "Charge is conserved" and "charge is quantized" — are these independent properties?<br> Can a system violate one while obeying the other?<br>

**Solution:**

These are **independent** properties:
- **Conservation** is about the total quantity remaining constant.
- **Quantization** is about the charge coming in discrete units.

In principle, you could have a universe where charge is conserved but not quantized (continuous charge, always conserved). Or quantized but not conserved (discrete chunks that appear/disappear). In *our* universe, both hold simultaneously.

**Practice:**

1. 🟡 "At the macroscopic level, quantization of charge can be ignored." Justify. *(Ans: Because e is so small, macroscopic charges contain ~10¹²⁺ quanta, making charge appear continuous)*
2. 🟡 Does conservation of charge hold for non-isolated systems?<br> *(Ans: No — charge can flow in/out. It holds only for the total isolated system.)*
3. 🟡 A proton and an antiproton annihilate to produce two gamma ray photons. Is charge conserved?<br> *(Ans: Yes. +e + (−e) = 0, and γ photons have zero charge.)*

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🟡 ⭐ Three identical spheres A, B, C have charges +6 μC, −2 μC, and +4 μC. A and B touch first and separate. Then B and C touch and separate. Find final charges on A, B, C. Verify conservation.

<details>
<summary><b>Solution</b></summary>

**Step 1:** A (+6) touches B (−2) → Total = 4 μC → Each gets +2 μC.
A = +2 μC, B = +2 μC, C = +4 μC.

**Step 2:** B (+2) touches C (+4) → Total = 6 μC → Each gets +3 μC.
A = +2 μC, B = +3 μC, C = +3 μC.

**Check:** 2 + 3 + 3 = 8 μC. Original: 6 + (−2) + 4 = 8 μC ✓ **Conserved.**
</details>

**Q2.** 🔴 A body has 10²⁰ protons and 10²⁰ + 3 × 10¹² electrons. Find (a) the net charge on the body, (b) is this charge quantized?<br> (c) what fraction of total electrons constitutes the excess?<br>

<details>
<summary><b>Solution</b></summary>

(a) Excess electrons = 3 × 10¹²
Q = −ne = −3 × 10¹² × 1.6 × 10⁻¹⁹ = **−4.8 × 10⁻⁷ C = −0.48 μC**

(b) n = 3 × 10¹², an integer → **Yes, quantized** ✓

(c) Fraction = 3 × 10¹² / 10²⁰ = **3 × 10⁻⁸ = 0.000003%**

> This tiny imbalance produces a measurable charge — showing how sensitive electrostatics is.
</details>

**Q3.** 🟡 When 10¹⁴ electrons are transferred from body A to body B:
(a) What is the charge acquired by B?<br>
(b) What is the charge on A?<br>
(c) Is the total charge conserved?<br>

<details>
<summary><b>Solution</b></summary>

(a) B gains 10¹⁴ electrons → Q_B = −10¹⁴ × 1.6 × 10⁻¹⁹ = **−16 μC**
(b) A loses 10¹⁴ electrons → Q_A = **+16 μC**
(c) Total = +16 + (−16) = 0 = initial charge (both were neutral) → **Yes** ✓
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 ⭐ State the three basic properties of electric charge. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. **Additivity:** The total charge of a system is the algebraic sum of all individual charges: Q = q₁ + q₂ + ... + qₙ.

2. **Conservation:** The total charge of an isolated system remains constant. Charge is neither created nor destroyed, only transferred.

3. **Quantization:** Charge exists in discrete packets. The charge on any body is always an integral multiple of the elementary charge e = 1.6 × 10⁻¹⁹ C. That is, Q = ne, where n is an integer.
</details>

**Q2.** 🟡 ⭐ What is quantization of charge?<br> Why is it not observed at the macroscopic level?<br> *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Quantization of charge** means that the charge on any body can only take values that are integral multiples of the elementary charge *e* = 1.6 × 10⁻¹⁹ C. Mathematically, Q = ne, where n is an integer.

At the **macroscopic level**, the charges we deal with (microcoulombs, millicoulombs) involve an enormous number of elementary charges (~10¹² or more). At this scale, the discrete nature of charge is imperceptible, and charge appears to be a continuous quantity — just as individual grains of sand are invisible when looking at a beach from a distance.
</details>

**Q3.** 🟡 An ebonite rod is rubbed with fur. The rod acquires a charge of −4.8 × 10⁻⁸ C. (a) How many electrons were transferred and in which direction?<br> (b) What charge does the fur acquire?<br> *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

(a) n = Q/e = 4.8 × 10⁻⁸ / 1.6 × 10⁻¹⁹ = **3 × 10¹¹ electrons**
Direction: From fur to ebonite rod (rod gained electrons, so fur lost them).

(b) By conservation of charge: Charge on fur = **+4.8 × 10⁻⁸ C**
</details>

**Q4.** 🟢 Is a charge of 2 × 10⁻¹⁹ C possible?<br> Justify. *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

n = 2 × 10⁻¹⁹ / 1.6 × 10⁻¹⁹ = 1.25

Since n is not an integer, this charge is **not possible** according to the quantization of charge.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ Which of the following is NOT a property of electric charge?<br>

(a) Charge is conserved  
(b) Charge is quantized  
(c) Charge is additive  
(d) Charge of a body depends on its speed  

<details>
<summary><b>Answer</b></summary>

**(d)** — Electric charge is **invariant** — it does not change with speed (unlike mass in relativistic mechanics). This is a fundamental property: charge is Lorentz invariant.
</details>

**Q2.** 🟡 The minimum charge on any body (observed in isolation) is:

(a) 1 C  
(b) 1.6 × 10⁻¹⁹ C  
(c) 1.6 × 10⁻²⁰ C  
(d) 5.3 × 10⁻²⁰ C  

<details>
<summary><b>Answer</b></summary>

**(b)** — The elementary charge e = 1.6 × 10⁻¹⁹ C. Quarks have fractional charges but are never isolated.
</details>

**Q3.** 🔴 ⭐ Two identical conducting spheres with charges +6Q and −2Q are brought into contact and separated. The electrostatic force between them at distance *d* after separation, compared to the force before contact, changes by a factor of:

(a) 4/3 &emsp; (b) 1/3 &emsp; (c) 3/4 &emsp; (d) 1/2

<details>
<summary><b>Answer</b></summary>

**Before contact:** F₁ = k(6Q)(2Q)/d² = 12kQ²/d²

**After contact:** Each gets (6Q − 2Q)/2 = 2Q.
F₂ = k(2Q)(2Q)/d² = 4kQ²/d²

Ratio = F₂/F₁ = 4/12 = **1/3**

**Answer: (b)**
</details>

**Q4.** 🔴 A certain charge Q is divided into two parts: q and (Q − q). For the two parts to have maximum Coulomb repulsion at a fixed separation, q should be:

(a) Q/4 &emsp; (b) Q/2 &emsp; (c) Q &emsp; (d) 2Q

<details>
<summary><b>Answer</b></summary>

F = kq(Q − q)/r²

For maximum F: dF/dq = k(Q − 2q)/r² = 0 → **q = Q/2**

**Answer: (b)**
</details>

**Q5.** 🟡 Charge is quantized because:

(a) Charge cannot be destroyed  
(b) There is a minimum possible charge  
(c) Charge adds up algebraically  
(d) Charge is always positive  

<details>
<summary><b>Answer</b></summary>

**(b)** — Quantization specifically means there exists a minimum indivisible unit of charge (e = 1.6 × 10⁻¹⁹ C), and all observed charges are integer multiples of it.
</details>

---

*Next: [Chapter 4 — Coulomb's Law →](./04_coulombs_law.md)*
