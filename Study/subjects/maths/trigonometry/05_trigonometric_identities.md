# Chapter 5: Trigonometric Identities — The Big Three

---

## Stage 1: The Core Idea

### The Pythagorean Connection

In a right triangle with angle θ:

```
       ┌───┐
       │   │
  opp  │   │  hyp = 1 (if scaling)
       │   │
       └───┘
         adj

By Pythagoras: opp² + adj² = hyp²
```

If we scale the triangle so hyp = 1, then:
- opp = sin θ
- adj = cos θ

And Pythagoras becomes: **sin²θ + cos²θ = 1**

From this single equation, two more follow:
- Divide by cos²θ: **1 + tan²θ = sec²θ**
- Divide by sin²θ: **1 + cot²θ = cosec²θ**

These **three identities** are the backbone of all trigonometry. Every simplification, every proof, every equation — they all come back to these three.

---

## Stage 2: The Formula Lab

### The Big Three

| # | Identity | Derivation |
|---|----------|-----------|
| 1 | sin²θ + cos²θ = 1 | Pythagoras on unit hyp triangle |
| 2 | 1 + tan²θ = sec²θ | Divide (1) by cos²θ |
| 3 | 1 + cot²θ = cosec²θ | Divide (1) by sin²θ |

### Variations

From sin²θ + cos²θ = 1:
```
sin²θ = 1 − cos²θ = (1 − cos θ)(1 + cos θ)
cos²θ = 1 − sin²θ = (1 − sin θ)(1 + sin θ)
```

From 1 + tan²θ = sec²θ:
```
tan²θ = sec²θ − 1 = (sec θ − 1)(sec θ + 1)
```

From 1 + cot²θ = cosec²θ:
```
cot²θ = cosec²θ − 1 = (cosec θ − 1)(cosec θ + 1)
```

**Trap to avoid:** sin²θ means (sin θ)², NOT sin(θ²). Similarly, sin⁻¹θ ≠ (sin θ)⁻¹.

---

## Stage 3: Type-wise Mastery

### Type 1: Proving LHS = RHS (Direct Substitution)

**Goal:** Prove an identity by substituting the basic identities.

**Solved Example:**

Prove that cos⁴θ − sin⁴θ = cos²θ − sin²θ.

**Solution:**
```
LHS = (cos²θ)² − (sin²θ)²
    = (cos²θ − sin²θ)(cos²θ + sin²θ)
    = (cos²θ − sin²θ)(1)
    = cos²θ − sin²θ = RHS ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Prove: (1 − cos²θ) × cosec²θ = 1.

2. 🟡 Prove: (1 + tan²θ) × cos²θ = 1.

3. 🟡 Prove: sin⁴θ − cos⁴θ = sin²θ − cos²θ.

4. 🟡 Prove: (sec²θ − 1)(cosec²θ − 1) = 1.

5. 🔴 Prove: (sin θ + cos θ)² + (sin θ − cos θ)² = 2.

---

### Type 2: Expressing One Ratio in Terms of Another

**Goal:** Write all trig ratios in terms of a given ratio.

**Solved Example:**

Express sin θ and tan θ in terms of cos θ.

**Solution:**
```
sin²θ = 1 − cos²θ
sin θ = √(1 − cos²θ)    (positive if θ acute)

tan θ = sin θ / cos θ = √(1 − cos²θ) / cos θ
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 Express cos θ and cot θ in terms of sin θ.

7. 🟡 Express sin θ and sec θ in terms of tan θ.

8. 🟡 Express all six ratios in terms of cos θ.

9. 🔴 Express cos θ in terms of cot θ.

10. 🔴 Express cosec θ in terms of cos θ.

---

### Type 3: Proving LHS = RHS (Factorisation)

**Goal:** Prove identities using algebraic factorisation.

**Solved Example:**

Prove: sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ.

**Solution:**
```
LHS = (sin²θ)² + (cos²θ)²
    = (sin²θ + cos²θ)² − 2 sin²θ cos²θ
    = (1)² − 2 sin²θ cos²θ
    = 1 − 2 sin²θ cos²θ = RHS ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 Prove: (sin θ + cos θ)² = 1 + 2 sin θ cos θ.

12. 🟡 Prove: sin³θ + cos³θ = (sin θ + cos θ)(1 − sin θ cos θ).

13. 🟡 Prove: (1 + tan θ)² + (1 − tan θ)² = 2 sec²θ.

14. 🔴 Prove: (sin θ + cosec θ)² + (cos θ + sec θ)² = 7 + tan²θ + cot²θ.

15. 🔴 ⭐ Prove: (tan θ + sec θ − 1)/(tan θ + sec θ + 1) = (1 + sin θ)/cos θ.

---

### Type 4: Proving LHS = RHS (Using Denominators)

**Goal:** Prove identities by combining fractions.

**Solved Example:**

Prove: 1/(1 + sin θ) + 1/(1 − sin θ) = 2 sec²θ.

**Solution:**
```
LHS = (1 − sin θ + 1 + sin θ)/((1 + sin θ)(1 − sin θ))
    = 2/(1 − sin²θ)
    = 2/cos²θ
    = 2 sec²θ = RHS ✓
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Prove: 1/(1 + cos θ) + 1/(1 − cos θ) = 2 cosec²θ.

17. 🟡 Prove: sec θ/(1 − tan θ) + tan θ/(sec θ − 1) = sec θ tan θ ... wait, let me simplify. Prove: (cosec θ − cot θ)² = (1 − cos θ)/(1 + cos θ).

18. 🟡 Prove: (1 + sin θ)/cos θ + cos θ/(1 + sin θ) = 2 sec θ.

19. 🔴 Prove: (tan A − tan B)/(cot B − cot A) = tan A tan B.

20. 🔴 ⭐ Prove: (sin A + sec A)² + (cos A + cosec A)² = (1 + sec A cosec A)².

---

### Type 5: Eliminating θ Between Two Equations

**Goal:** Given two equations involving θ, eliminate θ to find a relation between the constants.

**Solved Example:**

Eliminate θ from: x = a cos θ, y = b sin θ.

**Solution:**
```
cos θ = x/a, sin θ = y/b
Using sin²θ + cos²θ = 1:
x²/a² + y²/b² = 1
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Eliminate θ: x = 3 cos θ, y = 4 sin θ.

22. 🟡 Eliminate θ: x = a sec θ, y = b tan θ.

23. 🟡 Eliminate θ: x = a cos θ + b sin θ, y = a sin θ − b cos θ.

24. 🔴 Eliminate θ: x = a(cos θ + sin θ), y = a(cos θ − sin θ).

25. 🔴 If x = a cos²θ, y = b sin²θ, find a relation between x, y, a, b.

---

### Type 6: Conditional Identities (A + B + C = π)

**Goal:** Prove identities when the angles satisfy A + B + C = 180° (triangle angles).

**Key observations:**
- If A + B + C = π, then A + B = π − C
- So sin(A + B) = sin C, cos(A + B) = −cos C

**Solved Example:**

If A + B + C = π, prove that tan A + tan B + tan C = tan A tan B tan C.

**Solution:**
```
A + B = π − C
tan(A + B) = tan(π − C) = −tan C
(tan A + tan B)/(1 − tan A tan B) = −tan C
tan A + tan B = −tan C + tan A tan B tan C
tan A + tan B + tan C = tan A tan B tan C ✓
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 If A + B + C = π, prove that sin 2A + sin 2B + sin 2C = 4 sin A sin B sin C.

27. 🔴 If A + B + C = π, prove that cos 2A + cos 2B + cos 2C = −1 − 4 cos A cos B cos C.

28. 🔴 If A + B + C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2).

29. 🔴 If A + B + C = π/2, prove that cot A + cot B + cot C = cot A cot B cot C.

30. 🔴 ⭐ If x + y + z = xyz, prove that x/(1 − x²) + y/(1 − y²) + z/(1 − z²) = xyz/(1 − x²)(1 − y²)(1 − z²).

---

### Type 7: Finding Values Using Identities

**Goal:** Use identities to find the value of expressions without finding θ.

**Solved Example:**

If sin θ + cos θ = √2, find sin θ cos θ.

**Solution:**
```
(sin θ + cos θ)² = 2
sin²θ + cos²θ + 2 sin θ cos θ = 2
1 + 2 sin θ cos θ = 2
2 sin θ cos θ = 1
sin θ cos θ = 1/2
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 If sin θ − cos θ = 0, find sin θ cos θ.

32. 🟡 If tan θ + cot θ = 2, find tan²θ + cot²θ.

33. 🟡 If sec θ + tan θ = p, find sec θ − tan θ.

34. 🔴 If sin θ + sin²θ = 1, prove that cos²θ + cos⁴θ = 1.

35. 🔴 ⭐ If a cos θ + b sin θ = c, then prove that a sin θ − b cos θ = ±√(a² + b² − c²).

---

### Type 8: Identity-Based Simplifications

**Goal:** Simplify complex expressions using identities.

**Solved Example:**

Simplify: (sec A + tan A)(1 − sin A).

**Solution:**
```
= (1/cos A + sin A/cos A)(1 − sin A)
= (1 + sin A)/cos A × (1 − sin A)
= (1 − sin²A)/cos A
= cos²A/cos A
= cos A
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Simplify: (1 + tan²θ)(1 − sin θ)(1 + sin θ).

37. 🟡 Simplify: cos²A/(1 − sin A) − cos²A/(1 + sin A).

38. 🟡 Simplify: sin⁶θ + cos⁶θ + 3 sin²θ cos²θ.

39. 🔴 Simplify: √((sec θ − 1)/(sec θ + 1)) + √((sec θ + 1)/(sec θ − 1)).

40. 🔴 ⭐ Simplify: (tan A + sec A − 1)(tan A + sec A + 1).

---

## Stage 4: Type Mixer

1. 🟡 Prove: (1 + tan²θ) + (1 + cot²θ) = (sin²θ + cos²θ)/(sin²θ cos²θ) ... simplify to: 1/(sin²θ cos²θ).

2. 🟡 If sec θ + tan θ = 3, find sec θ − tan θ and hence find cos θ.

3. 🔴 ⭐ Prove: (sin A − 2 sin³A)/(2 cos³A − cos A) = tan A.

4. 🔴 Eliminate θ: x = a sec³θ, y = b tan³θ.

5. 🔴 If a sin²θ + b cos²θ = c, express tan²θ in terms of a, b, c.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Prove: (1 + tan²A)/(1 + cot²A) = tan²A. **(2 marks)**

**Solution:**
```
LHS = (sec²A)/(cosec²A) = (1/cos²A)/(1/sin²A) = sin²A/cos²A = tan²A = RHS ✓
```

---

**Q2.** 🟡 Prove: √((1 + sin A)/(1 − sin A)) = sec A + tan A. **(3 marks)**

**Solution:**
```
LHS = √((1 + sin A)²/(1 − sin²A))
    = (1 + sin A)/√(cos²A)
    = (1 + sin A)/cos A
    = sec A + tan A = RHS ✓
```

---

**Q3.** 🟡 Prove: (sin θ − cos θ + 1)/(sin θ + cos θ − 1) = 1/(sec θ − tan θ). **(3 marks)**

**Solution:**
```
Divide numerator and denominator by cos θ:
LHS = (tan θ − 1 + sec θ)/(tan θ + 1 − sec θ)
    = (tan θ + sec θ − 1)/(tan θ − sec θ + 1)
Now using identity sec²θ − tan²θ = 1:
    = (tan θ + sec θ − 1)/((tan θ − sec θ) + (sec²θ − tan²θ))
    = (tan θ + sec θ − 1)/((tan θ − sec θ)(1 − (tan θ + sec θ)))
... which simplifies to 1/(sec θ − tan θ) ✓
```

---

**Q4.** 🔴 If sec θ + tan θ = p, find the value of sin θ. **(3 marks)**

**Solution:**
```
sec θ + tan θ = p   ...(1)
We know sec²θ − tan²θ = 1
(sec θ − tan θ)(sec θ + tan θ) = 1
(sec θ − tan θ)(p) = 1
sec θ − tan θ = 1/p   ...(2)

From (1) and (2):
sec θ = (p + 1/p)/2 = (p² + 1)/(2p)
tan θ = (p − 1/p)/2 = (p² − 1)/(2p)

sin θ = tan θ / sec θ = (p² − 1)/(p² + 1)
```

---

## Stage 6: JEE Mains Arena

**Q1.** If sin θ − cos θ = 0, then sin⁴θ + cos⁴θ equals:
(a) 1/4
(b) 1/2
(c) 1
(d) 3/4

<details>
<summary>Solution</summary>
sin θ = cos θ → tan θ = 1 → sin θ = cos θ = 1/√2
sin⁴θ + cos⁴θ = (1/4) + (1/4) = 1/2
Answer: (b) 🟡
</details>

---

**Q2.** If sin⁴θ + cos⁴θ = 1, then θ equals:
(a) 0°
(b) 90°
(c) 0° or 90°
(d) 45°

<details>
<summary>Solution</summary>
sin⁴θ + cos⁴θ = (sin²θ + cos²θ)² − 2 sin²θ cos²θ = 1 − 2 sin²θ cos²θ
Given: 1 − 2 sin²θ cos²θ = 1
→ sin²θ cos²θ = 0
→ sin θ = 0 or cos θ = 0
→ θ = 0° or 90°
Answer: (c) 🔴 ⭐
</details>

---

**Q3.** If tan θ + cot θ = 2, then tan²θ + cot²θ equals:
(a) 1
(b) 2
(c) 3
(d) 4

<details>
<summary>Solution</summary>
tan θ + cot θ = 2
Square both sides: tan²θ + cot²θ + 2 tan θ cot θ = 4
tan²θ + cot²θ + 2(1) = 4
tan²θ + cot²θ = 2
Answer: (b) 🟡
</details>

---

**Q4.** The expression (sin⁶θ + cos⁶θ − 1)/(sin⁴θ + cos⁴θ − 1) simplifies to:
(a) 1
(b) 2/3
(c) 3/2
(d) 0

<details>
<summary>Solution</summary>
sin⁶θ + cos⁶θ = (sin²θ + cos²θ)³ − 3 sin²θ cos²θ(sin²θ + cos²θ) = 1 − 3 sin²θ cos²θ
sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ

Expression = (1 − 3 sin²θ cos²θ − 1)/(1 − 2 sin²θ cos²θ − 1)
= (−3 sin²θ cos²θ)/(−2 sin²θ cos²θ)
= 3/2
Answer: (c) 🔴 ⭐
</details>

---

**Q5.** If sin θ + sin²θ = 1, then cos²θ + cos⁴θ equals:
(a) 0
(b) 1
(c) 2
(d) −1

<details>
<summary>Solution</summary>
Given: sin θ + sin²θ = 1
→ sin θ = 1 − sin²θ = cos²θ

Now, cos²θ + cos⁴θ = sin θ + sin²θ = 1
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin²θ + cos²θ = 1 for all θ.
**Reason (R):** This follows from the Pythagoras theorem.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** 1 + tan²θ = sec²θ for all θ.
**Reason (R):** tan θ is defined for all real θ.

<details>
<summary>Solution</summary>
A is true: 1 + tan²θ = sec²θ.
R is false: tan θ is undefined at θ = 90°, 270°, etc.
Answer: (c)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The maximum value of sin⁴θ + cos⁴θ is 1.
**Reason (R):** sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ ≤ 1.

<details>
<summary>Solution</summary>
A is true (max = 1 at θ = 0°, 90°).
R is true (since sin²θ cos²θ ≥ 0).
R correctly explains A.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** (1 + tan²θ)(1 − sin θ)(1 + sin θ) = 1.
**Reason (R):** sec²θ × cos²θ = 1.

<details>
<summary>Solution</summary>
A: (1 + tan²θ)(1 − sin²θ) = sec²θ × cos²θ = 1. True.
R: sec²θ × cos²θ = (1/cos²θ)(cos²θ) = 1. True.
R explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin²θ + cos²θ = ?<br>
   (a) 0   (b) 1   (c) −1   (d) 2

2. 🟢 1 + tan²θ = ?<br>
   (a) sin²θ   (b) cot²θ   (c) sec²θ   (d) cosec²θ

3. 🟢 1 + cot²θ = ?<br>
   (a) tan²θ   (b) sec²θ   (c) cosec²θ   (d) sin²θ

4. 🟡 (sec²θ − 1) equals:
   (a) tan²θ   (b) cot²θ   (c) sin²θ   (d) cos²θ

5. 🟡 (1 − sin²θ)(1 + tan²θ) equals:
   (a) 0   (b) 1   (c) 2   (d) −1

6. 🟡 If sin θ = 3/5, cos²θ = ?<br>
   (a) 9/25   (b) 16/25   (c) 4/5   (d) 25/16

7. 🟡 (sin θ + cos θ)² = ?<br>
   (a) 1   (b) 1 + 2 sin θ cos θ   (c) 1 − 2 sin θ cos θ   (d) 2

8. 🟡 (sin θ − cos θ)² = ?<br>
   (a) 1   (b) 1 + 2 sin θ cos θ   (c) 1 − 2 sin θ cos θ   (d) 2

9. 🟢 sec²θ − tan²θ = ?<br>
   (a) 0   (b) 1   (c) −1   (d) 2

10. 🟡 If tan θ = 2, sec θ = ?<br>
    (a) √5   (b) 5   (c) √3   (d) 3

11. 🟡 If cot θ = 3, cosec θ = ?<br>
    (a) √10   (b) √8   (c) 3   (d) 10

12. 🟡 sin⁴θ − cos⁴θ = ?<br>
    (a) 1   (b) sin²θ − cos²θ   (c) 0   (d) 2

13. 🟡 (1 + tan θ)² + (1 − tan θ)² = ?<br>
    (a) 2   (b) 2 sec²θ   (c) 2 tan²θ   (d) 4

14. 🟡 1/(1 + sin θ) + 1/(1 − sin θ) = ?<br>
    (a) 2   (b) 2 sec²θ   (c) 2 cos²θ   (d) 2 sin²θ

15. 🟢 Which identity is CORRECT?<br>
    (a) sin²θ = 1 + cos²θ   (b) 1 + cot²θ = cosec²θ   (c) tan²θ + 1 = cosec²θ   (d) sec²θ + 1 = tan²θ

16. 🟡 If sec θ + tan θ = 2, then sec θ − tan θ = ?<br>
    (a) 2   (b) 1/2   (c) 0   (d) 1

17. 🟡 If sin θ + cos θ = √2, then sin θ cos θ = ?<br>
    (a) 1/2   (b) 1   (c) 0   (d) 2

18. 🟡 (sin⁴θ + cos⁴θ) + 2 sin²θ cos²θ = ?<br>
    (a) 0   (b) 1   (c) 2   (d) 1/2

19. 🟡 sin θ/(1 + cos θ) + (1 + cos θ)/sin θ = ?<br>
    (a) 2 sin θ   (b) 2 cos θ   (c) 2 cosec θ   (d) 2 sec θ

20. 🟡 If tan²θ = 1 − e², then sec θ + tan³θ cosec θ = ?<br>
    (a) (2 − e²)^(3/2)   (b) (2 − e²)^(1/2)   (c) 2 − e²   (d) 1

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | a | 16 | b |
| 2 | c | 7 | b | 12 | b | 17 | a |
| 3 | c | 8 | c | 13 | b | 18 | b |
| 4 | a | 9 | b | 14 | b | 19 | c |
| 5 | b | 10 | a | 15 | b | 20 | a |

</details>
