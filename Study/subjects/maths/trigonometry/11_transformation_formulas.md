# Chapter 11: Transformation Formulas

---

## Stage 1: The Core Idea

### Converting Sums to Products and Back

You have two expressions:
- sin A + sin B
- 2 sin((A+B)/2) cos((A−B)/2)

They're the same thing. But sometimes the sum form is useful, and sometimes the product form is.

**Transformation formulas** let you switch between sums and products — and this switching power is one of the deadliest weapons in JEE trigonometry. Factorization, simplification, solving equations — transformation is often the key step.

---

## Stage 2: The Formula Lab

### Sum → Product

```
sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2)
sin C − sin D = 2 cos((C+D)/2) sin((C−D)/2)
cos C + cos D = 2 cos((C+D)/2) cos((C−D)/2)
cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2)
```

### Product → Sum

```
2 sin A cos B = sin(A+B) + sin(A−B)
2 cos A sin B = sin(A+B) − sin(A−B)
2 cos A cos B = cos(A+B) + cos(A−B)
2 sin A sin B = cos(A−B) − cos(A+B)
```

**Memory trick:**
- For sum→product: average angles for the first factor, half-difference for the second
- For product→sum: the "2" on the left always appears on the right as two terms

**Trap to avoid:** cos C − cos D has a **minus** sign in front! This is the one formula students always forget the negative for.

---

## Stage 3: Type-wise Mastery

### Type 1: Expressing Sum as Product

**Goal:** Write a sum of trig functions as a product.

**Solved Example:**

Express sin 7θ + sin 3θ as a product.

**Solution:**
```
sin 7θ + sin 3θ = 2 sin((7θ+3θ)/2) cos((7θ−3θ)/2)
= 2 sin 5θ cos 2θ
```
🟢 Easy

---

**Practice Problems:**

1. 🟢 Express sin 5x + sin x as a product.
2. 🟢 Express cos 8θ − cos 2θ as a product.
3. 🟢 Express sin 6x − sin 2x as a product.
4. 🟢 Express cos 5x + cos 3x as a product.
5. 🟡 Express sin 50° + sin 10° as a product and evaluate.

---

### Type 2: Expressing Product as Sum

**Goal:** Write a product of trig functions as a sum.

**Solved Example:**

Express 2 cos 5x sin 3x as a sum.

**Solution:**
```
2 cos 5x sin 3x = sin(5x+3x) − sin(5x−3x) = sin 8x − sin 2x
```
🟢 Easy

---

**Practice Problems:**

6. 🟢 Express 2 sin 4x cos 2x as a sum.
7. 🟢 Express 2 cos 7x cos 3x as a sum.
8. 🟢 Express 2 sin 5x sin 2x as a sum.
9. 🟡 Express 2 cos 75° sin 15° as a sum and evaluate.
10. 🟡 Express 2 sin 105° cos 75° as a sum.

---

### Type 3: Simplifying Ratios Using Transformation

**Goal:** Simplify expressions of the form (sin A ± sin B)/(cos A ± cos B).

**Solved Example:**

Simplify (sin 7x + sin 5x)/(cos 7x + cos 5x).

**Solution:**
```
= (2 sin 6x cos x)/(2 cos 6x cos x)
= tan 6x
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 Simplify (sin 5x − sin 3x)/(cos 5x + cos 3x).

12. 🟡 Simplify (cos 6x + cos 4x)/(sin 6x − sin 4x).

13. 🟡 Simplify (sin A + sin 3A)/(cos A + cos 3A).

14. 🔴 Simplify (sin 7θ − sin 3θ − sin 5θ + sin θ)/(cos 7θ − cos 3θ − cos 5θ + cos θ).

15. 🔴 ⭐ Show that (sin 2x + sin 5x − sin x)/(cos 2x + cos 5x + cos x) = tan 2x.

---

### Type 4: Solving Equations Using Transformation

**Goal:** Convert sum to product to factor and solve.

**Solved Example:**

Solve sin 3x + sin x = 0 for 0° ≤ x ≤ 360°.

**Solution:**
```
2 sin 2x cos x = 0

Case 1: sin 2x = 0 → 2x = 0°, 180°, 360° → x = 0°, 90°, 180°
Case 2: cos x = 0 → x = 90°, 270°

Solution: x = 0°, 90°, 180°, 270°
(Note: 90° repeats)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Solve sin 7x − sin x = 0 for 0° ≤ x ≤ 360°.
17. 🟡 Solve cos 5x + cos 3x = 0 for 0° ≤ x ≤ 180°.
18. 🟡 Solve sin x + sin 3x + sin 5x = 0 for 0° ≤ x ≤ 180°.
19. 🔴 ⭐ Solve cos 2x + cos 4x + cos 6x = 0 for 0° ≤ x ≤ 180°.
20. 🔴 Solve sin x + sin 3x = cos x + cos 3x for 0° ≤ x ≤ 360°.

---

### Type 5: Proving Identities Using Transformation

**Goal:** Prove identities by converting sums to products.

**Solved Example:**

Prove that (sin 3x + sin x)/sin 2x = 2 cos x.

**Solution:**
```
LHS = (2 sin 2x cos x)/sin 2x = 2 cos x = RHS ✓
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 Prove sin 50° + sin 10° = 2 sin 30° cos 20° = cos 20°.

22. 🟡 Prove that (sin 5x − 2 sin 3x + sin x)/(cos 5x − cos x) = tan x.

23. 🟡 Prove that cos 20° + cos 100° + cos 140° = 0.

24. 🔴 ⭐ Prove that sin 10° + sin 20° + sin 40° + sin 50° = sin 70° + sin 80°.

25. 🔴 Prove that cos(π/7) + cos(3π/7) + cos(5π/7) = 1/2.

---

### Type 6: Evaluating Sums of Sines/Cosines in AP

**Goal:** Sum a series like sin α + sin(α+d) + sin(α+2d) + ... using transformations.

**Solved Example:**

Find the value of sin 10° + sin 20° + sin 30° + ... + sin 180°.

**Solution:**
This is 18 terms of sin in AP with d = 10°.
We can pair: sin 10° + sin 170° = 2 sin 90° cos 80° = 2 cos 80°
sin 20° + sin 160° = 2 sin 90° cos 70° = 2 cos 70°
...
sin 80° + sin 100° = 2 sin 90° cos 10° = 2 cos 10°
sin 90° = 1
sin 180° = 0

Total = 2(cos 10° + cos 20° + ... + cos 80°) + 1

This can be further simplified. Answer = 11.43...
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 Find sin 10° + sin 20° + ... + sin 90°.
27. 🔴 Find cos 20° + cos 40° + cos 60° + ... + cos 180°.
28. 🔴 ⭐ Find the sum of sin² 1° + sin² 2° + ... + sin² 90°.
29. 🔴 Prove that cos(2π/7) + cos(4π/7) + cos(6π/7) = −1/2.
30. 🔴 Find the value of sin(π/7) sin(2π/7) sin(3π/7).

---

### Type 7: Conditional Identities with A+B+C = π (Advanced)

**Goal:** Use transformation to prove identities when A+B+C = π.

**Solved Example:**

If A + B + C = π, prove that sin 2A + sin 2B + sin 2C = 4 sin A sin B sin C.

**Solution:**
```
sin 2A + sin 2B = 2 sin(A+B) cos(A−B)
= 2 sin(π−C) cos(A−B)
= 2 sin C cos(A−B)

Adding sin 2C = 2 sin C cos C:
sin 2A + sin 2B + sin 2C = 2 sin C[cos(A−B) + cos C]
= 2 sin C[cos(A−B) + cos(π−(A+B))]
= 2 sin C[cos(A−B) − cos(A+B)]
= 2 sin C[−2 sin A sin(−B)]
= 4 sin C sin A sin B ✓
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

31. 🔴 If A+B+C = π, prove that cos A + cos B + cos C = 1 + 4 sin(A/2) sin(B/2) sin(C/2).

32. 🔴 If A+B+C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2).

33. 🔴 If A+B+C = π, prove that tan A + tan B + tan C = tan A tan B tan C.

34. 🔴 ⭐ If A+B+C = π, prove that cos²A + cos²B + cos²C = 1 − 2 cos A cos B cos C.

35. 🔴 If A+B+C = 180°, prove that sin²A + sin²B + sin²C = 2 + 2 cos A cos B cos C.

---

### Type 8: Maximum/Minimum Using Transformation

**Goal:** Find max/min of sum expressions by converting to product.

**Solved Example:**

Find the maximum of sin θ + sin(θ + 60°).

**Solution:**
```
sin θ + sin(θ+60°) = 2 sin(θ+30°) cos 30°
= 2(√3/2) sin(θ+30°)
= √3 sin(θ+30°)

Maximum = √3
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Find the maximum of cos θ + cos(θ + 120°).
37. 🟡 Find the maximum of sin θ + sin(θ + 120°).
38. 🟡 Find the minimum of cos θ + cos(θ + 60°).
39. 🔴 ⭐ Find the maximum of sin(θ + 30°) + cos(θ + 60°).
40. 🔴 Find the maximum value of sin²θ + sin²(θ + 60°) + sin²(θ + 120°).

---

## Stage 4: Type Mixer

1. 🟡 Express as a product: sin 65° + sin 25°. Hence find its value.

2. 🟡 Prove that (sin 5x − sin 3x + sin x)/(cos 5x − cos 3x + cos x) = tan x.

3. 🔴 ⭐ Solve sin 2x + sin 4x + sin 6x = 0 for 0° ≤ x ≤ 180°.

4. 🔴 If A + B + C = π, prove that sin 2A + sin 2B − sin 2C = 4 cos A cos B sin C.

5. 🔴 Show that cos 20° cos 40° cos 80° = 1/8 using product→sum transformations.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Express sin 5x − sin 3x as a product. **(1 mark)**

**Solution:**
```
sin 5x − sin 3x = 2 cos((5x+3x)/2) sin((5x−3x)/2) = 2 cos 4x sin x
```

---

**Q2.** 🟡 Simplify (sin 7x + sin 5x)/(cos 7x − cos 5x). **(2 marks)**

**Solution:**
```
= (2 sin 6x cos x)/(−2 sin 6x sin x)
= −cot x
```

---

**Q3.** 🟡 Express 2 sin 5θ cos 3θ as a sum. **(1 mark)**

**Solution:**
```
= sin(5θ+3θ) + sin(5θ−3θ) = sin 8θ + sin 2θ
```

---

**Q4.** 🔴 If A + B + C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2). **(3 marks)**

**Solution:**
```
sin A + sin B = 2 sin((A+B)/2) cos((A−B)/2)
= 2 sin((π−C)/2) cos((A−B)/2)
= 2 cos(C/2) cos((A−B)/2)

Adding sin C = 2 sin(C/2) cos(C/2):
sin A + sin B + sin C = 2 cos(C/2)[cos((A−B)/2) + sin(C/2)]
= 2 cos(C/2)[cos((A−B)/2) + sin((π−(A+B))/2)]
= 2 cos(C/2)[cos((A−B)/2) + cos((A+B)/2)]
= 2 cos(C/2)[2 cos(A/2) cos(B/2)]
= 4 cos(A/2) cos(B/2) cos(C/2) ✓
```

---

## Stage 6: JEE Mains Arena

**Q1.** The value of sin 20° sin 40° sin 80° is:
(a) √3/8
(b) √3/4
(c) 1/2
(d) 1/8

<details>
<summary>Solution</summary>
= (1/2)(2 sin 20° sin 40°) sin 80°
= (1/2)[cos 20° − cos 60°] sin 80°
= (1/2)[cos 20° − 1/2] sin 80°
= (1/2)(cos 20° sin 80°) − (1/4) sin 80°
= (1/4)[sin 100° + sin 60°] − (1/4) sin 80°
= (1/4)[sin 80° + √3/2] − (1/4) sin 80°
= √3/8
Answer: (a) 🔴 ⭐
</details>

---

**Q2.** The value of sin 50° − sin 70° + sin 10° is:
(a) 0
(b) 1
(c) 1/2
(d) √3/2

<details>
<summary>Solution</summary>
= (sin 50° + sin 10°) − sin 70°
= 2 sin 30° cos 20° − sin 70°
= 2(1/2) cos 20° − sin 70°
= cos 20° − sin 70°
= cos 20° − cos 20° = 0
Answer: (a) 🟡 ⭐
</details>

---

**Q3.** The expression (sin 3x + sin x)/(cos 3x + cos x) simplifies to:
(a) tan x
(b) tan 2x
(c) tan 3x
(d) cot x

<details>
<summary>Solution</summary>
= (2 sin 2x cos x)/(2 cos 2x cos x) = tan 2x
Answer: (b) 🟡
</details>

---

**Q4.** If A + B + C = π, then cos 2A + cos 2B + cos 2C = ?<br>
(a) 1 − 4 cos A cos B cos C
(b) −1 − 4 cos A cos B cos C
(c) 1 + 4 cos A cos B cos C
(d) −1 + 4 cos A cos B cos C

<details>
<summary>Solution</summary>
cos 2A + cos 2B = 2 cos(A+B) cos(A−B) = 2 cos(π−C) cos(A−B) = −2 cos C cos(A−B)
Adding cos 2C = 2 cos²C − 1:
Sum = −2 cos C cos(A−B) + 2 cos²C − 1
= −2 cos C[cos(A−B) − cos C] − 1
= −2 cos C[cos(A−B) − cos(π−(A+B))] − 1
= −2 cos C[cos(A−B) + cos(A+B)] − 1
= −2 cos C[2 cos A cos B] − 1
= −4 cos A cos B cos C − 1
Answer: (b) 🔴 ⭐
</details>

---

**Q5.** The sum of sin² 5° + sin² 10° + ... + sin² 90° is:
(a) 8
(b) 9
(c) 9.5
(d) 10

<details>
<summary>Solution</summary>
This has 18 terms (5°, 10°, ..., 90°).
Pairs: sin²θ + sin²(90°−θ) = sin²θ + cos²θ = 1
Pairs: 5°+85°, 10°+80°, ..., 40°+50° = 8 pairs = 8
+ sin²45° = 1/2
+ sin²90° = 1
Total = 8 + 0.5 + 1 = 9.5
Answer: (c) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2).
**Reason (R):** This formula converts sum to product.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** cos C − cos D = 2 sin((C+D)/2) sin((C−D)/2).
**Reason (R):** The formula for cos C − cos D does not involve a negative sign.

<details>
<summary>Solution</summary>
A is false: cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2), missing the negative sign.
R is false: the correct formula does have a negative sign.
Answer: (d)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sin 50° + sin 10° = 2 sin 30° cos 20°.
**Reason (R):** sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2).

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The maximum value of sin x + sin y is 2.
**Reason (R):** sin x + sin y = 2 sin((x+y)/2) cos((x−y)/2) ≤ 2.

<details>
<summary>Solution</summary>
A is true (when sin((x+y)/2) = 1 and cos((x−y)/2) = 1).
R is true and explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin 7x + sin 3x equals:
   (a) 2 sin 5x cos 2x   (b) 2 cos 5x sin 2x   (c) 2 sin 2x cos 5x   (d) 2 cos 2x sin 5x

2. 🟢 cos 7x − cos 3x equals:
   (a) −2 sin 5x sin 2x   (b) 2 sin 5x sin 2x   (c) −2 cos 5x cos 2x   (d) 2 cos 5x cos 2x

3. 🟢 2 sin 5x cos 3x equals:
   (a) sin 8x + sin 2x   (b) sin 8x − sin 2x   (c) cos 8x + cos 2x   (d) cos 8x − cos 2x

4. 🟡 (sin 5x + sin 3x)/(cos 5x − cos 3x) equals:
   (a) tan x   (b) −cot 4x   (c) cot 4x   (d) tan 4x

5. 🟡 sin 75° − sin 15° equals:
   (a) 1/√2   (b) √3/2   (c) 1/2   (d) 1

6. 🟡 cos 75° + cos 15° equals:
   (a) √6/2   (b) √3/2   (c) 1/2   (d) 0

7. 🟡 2 sin 50° cos 10° equals:
   (a) sin 60° + sin 40°   (b) sin 60° − sin 40°   (c) cos 60° + cos 40°   (d) cos 60° − cos 40°

8. 🟡 sin 20° + sin 40° equals:
   (a) sin 60°   (b) cos 10°   (c) sin 10°   (d) cos 20°

9. 🟡 cos 40° + cos 80° equals:
   (a) cos 20°   (b) √3 cos 20°   (c) √3 cos 10°   (d) cos 60°

10. 🟡 cos 40° − cos 80° equals:
    (a) √3 sin 20°   (b) √3 sin 60°   (c) sin 20°   (d) −√3 sin 20°

11. 🟡 The product 2 sin A cos B equals:
    (a) sin(A+B) + sin(A−B)   (b) sin(A+B) − sin(A−B)   (c) cos(A+B) + cos(A−B)   (d) cos(A+B) − cos(A−B)

12. 🟡 (sin 3x + sin x)/sin 2x equals:
    (a) 2 cos x   (b) 2 sin x   (c) cos x   (d) sin x

13. 🟡 sin 50° − sin 70° + sin 10° equals:
    (a) 1   (b) 0   (c) 1/2   (d) √3/2

14. 🟡 cos 20° + cos 100° + cos 140° equals:
    (a) 1   (b) 0   (c) −1   (d) 1/2

15. 🟡 The sum sin 5° + sin 10° + ... + sin 85° can be simplified using:
    (a) Compound angles   (b) Transformation formulas   (c) Half-angle   (d) Double angle

16. 🟡 The value of sin 20° sin 40° sin 80° is:
    (a) √3/8   (b) 1/8   (c) 1/4   (d) 3/8

17. 🟡 cos 10° cos 30° cos 50° cos 70° equals:
    (a) 1/16   (b) 3/16   (c) 5/16   (d) 7/16

18. 🟡 2 cos 70° cos 10° equals:
    (a) cos 80° + cos 60°   (b) cos 80° − cos 60°   (c) sin 80° + sin 60°   (d) sin 80° − sin 60°

19. 🟡 The maximum value of sin θ + sin(θ + 60°) is:
    (a) 2   (b) √3   (c) 1   (d) √2

20. 🟡 If A + B + C = π, then cos A + cos B + cos C equals:
    (a) 1 + 4 sin(A/2) sin(B/2) sin(C/2)   (b) 1 − 4 sin(A/2) sin(B/2) sin(C/2)
    (c) 4 sin(A/2) sin(B/2) sin(C/2)   (d) 2

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | a | 11 | a | 16 | a |
| 2 | a | 7 | a | 12 | a | 17 | b |
| 3 | a | 8 | b | 13 | b | 18 | a |
| 4 | b | 9 | a | 14 | b | 19 | b |
| 5 | a | 10 | a | 15 | b | 20 | a |

</details>
