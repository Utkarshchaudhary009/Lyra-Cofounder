# Chapter 13: Inverse Trigonometric Functions

---

## Stage 1: The Core Idea

### The Problem Inverses Solve

We know sin 30° = 1/2. But what if I ask: "What angle has sin = 1/2?<br>"

We need a function that does the opposite — an **inverse** function.

But here's the problem: sin θ is NOT one-to-one. sin 30° = 1/2, sin 150° = 1/2, sin 390° = 1/2... infinitely many angles give the same sine.

To make an inverse, we **restrict the domain** — choose a specific interval where the function is one-to-one. This restricted range gives us the **principal value**.

```
sin x: domain restricted to [−π/2, π/2]  →  arcsin x has range [−π/2, π/2]
cos x: domain restricted to [0, π]        →  arccos x has range [0, π]
tan x: domain restricted to (−π/2, π/2)   →  arctan x has range (−π/2, π/2)
```

---

## Stage 2: The Formula Lab

### Notation

```
arcsin x or sin⁻¹x   (NOT (sin x)⁻¹ which is cosec x!)
arccos x or cos⁻¹x
arctan x or tan⁻¹x
arccot x or cot⁻¹x
arcsec x or sec⁻¹x
arccosec x or cosec⁻¹x
```

**Trap to avoid:** sin⁻¹x ≠ (sin x)⁻¹. This is the #1 mistake in inverse trig.

### Domain and Range (Principal Values)

| Function | Domain | Range |
|----------|--------|-------|
| arcsin x | [−1, 1] | [−π/2, π/2] |
| arccos x | [−1, 1] | [0, π] |
| arctan x | ℝ | (−π/2, π/2) |
| arccot x | ℝ | (0, π) |
| arcsec x | (−∞, −1] ∪ [1, ∞) | [0, π] − {π/2} |
| arccosec x | (−∞, −1] ∪ [1, ∞) | [−π/2, π/2] − {0} |

---

## Stage 3: Type-wise Mastery

### Type 1: Finding Principal Values

**Goal:** Find the principal value of a given inverse trig function.

**Solved Example:**

Find the principal value of sin⁻¹(1/2).

**Solution:**
```
sin⁻¹(1/2) = π/6   (Since sin π/6 = 1/2 and π/6 ∈ [−π/2, π/2])
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Find cos⁻¹(√3/2).
2. 🟢 Find tan⁻¹(1).
3. 🟢 Find sin⁻¹(−1/2).
4. 🟡 Find sec⁻¹(2).
5. 🟡 Find arccot(1/√3).

---

### Type 2: Simplifying sin(arcsin x) and arcsin(sin x)

**Goal:** Understand composition of inverse and regular trig functions.

**Key rules:**
```
sin(arcsin x) = x for x ∈ [−1, 1]
arcsin(sin x) = x only when x ∈ [−π/2, π/2]
```
For x outside this range, arcsin(sin x) = the angle in [−π/2, π/2] with the same sine.

**Solved Example:**

Find arcsin(sin(5π/6)).

**Solution:**
```
5π/6 is not in [−π/2, π/2].
sin(5π/6) = 1/2
arcsin(1/2) = π/6 (in [−π/2, π/2])
∴ arcsin(sin(5π/6)) = π/6
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Find arcsin(sin(π/4)).
7. 🟡 Find arccos(cos(5π/4)).
8. 🟡 Find arctan(tan(5π/6)).
9. 🟡 Find sin⁻¹(sin(3π/4)).
10. 🔴 Find cos⁻¹(cos(7π/6)).

---

### Type 3: Evaluating sin⁻¹(cos θ) Type Expressions

**Goal:** Simplify expressions where one trig function's output goes to another's inverse.

**Solved Example:**

Find sin⁻¹(cos 40°).

**Solution:**
```
cos 40° = sin 50° (using cos θ = sin(90° − θ))
sin⁻¹(sin 50°) = 50° (since 50° ∈ [−90°, 90°])
∴ sin⁻¹(cos 40°) = 50°
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Find cos⁻¹(sin 30°).
12. 🟡 Find tan⁻¹(cot 20°).
13. 🟡 Find sin⁻¹(cos 100°).
14. 🟡 Find arcsin(cos(−60°)).
15. 🔴 ⭐ Find arctan(cot 130°).

---

### Type 4: Proving Identities with Inverse Trig

**Goal:** Prove relationships between inverse trig functions.

**Solved Example:**

Prove that sin⁻¹x + cos⁻¹x = π/2 for all x ∈ [−1, 1].

**Solution:**
```
Let sin⁻¹x = θ → x = sin θ, θ ∈ [−π/2, π/2]
Then cos θ = √(1 − x²) (positive since θ ∈ [−π/2, π/2])
θ = cos⁻¹(√(1 − x²))... 

Better: Let sin⁻¹x = A, cos⁻¹x = B
sin A = x, cos B = x
sin A = cos B
sin A = sin(π/2 − B)
A = π/2 − B (since A, π/2−B are in [−π/2, π/2])
A + B = π/2 ✓
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Prove that tan⁻¹x + cot⁻¹x = π/2.
17. 🟡 Prove that sec⁻¹x + cosec⁻¹x = π/2.
18. 🟡 Prove that arctan(1) + arctan(2) + arctan(3) = π.
19. 🔴 ⭐ Prove that 2 arctan(1/3) + arctan(1/7) = π/4.
20. 🔴 Prove that arctan(1/3) + arctan(1/5) + arctan(1/7) + arctan(1/8) = π/4.

---

### Type 5: Writing as Sum/Difference of Inverse Functions

**Goal:** Simplify expressions like tan⁻¹(a) ± tan⁻¹(b).

**Formula:**
```
tan⁻¹x + tan⁻¹y = tan⁻¹((x + y)/(1 − xy))  if xy < 1
tan⁻¹x − tan⁻¹y = tan⁻¹((x − y)/(1 + xy))
```

**Solved Example:**

Prove that tan⁻¹(1/2) + tan⁻¹(1/3) = π/4.

**Solution:**
```
tan⁻¹(1/2) + tan⁻¹(1/3) = tan⁻¹((1/2 + 1/3)/(1 − 1/6))
= tan⁻¹((5/6)/(5/6))
= tan⁻¹(1)
= π/4 ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Evaluate tan⁻¹(1/5) + tan⁻¹(3/5).
22. 🟡 Evaluate tan⁻¹(2) + tan⁻¹(3).
23. 🟡 Evaluate sin⁻¹(3/5) + cos⁻¹(4/5).
24. 🔴 ⭐ Prove that tan⁻¹(1/7) + tan⁻¹(1/13) = tan⁻¹(2/9).
25. 🔴 Find the value of sin⁻¹(5/13) + sin⁻¹(12/13).

---

### Type 6: Solving Equations with Inverse Trig

**Goal:** Solve equations involving inverse trig functions.

**Solved Example:**

Solve tan⁻¹x + tan⁻¹(2x) = π/4.

**Solution:**
```
tan⁻¹x + tan⁻¹(2x) = π/4
tan⁻¹((x + 2x)/(1 − 2x²)) = π/4
3x/(1 − 2x²) = 1
3x = 1 − 2x²
2x² + 3x − 1 = 0
x = (−3 ± √17)/4

Check domain: x > 0 (since sum is positive)
x = (−3 + √17)/4 ≈ 0.28
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 Solve tan⁻¹(2x) + tan⁻¹(3x) = π/4.
27. 🔴 Solve cos⁻¹x + sin⁻¹(1/2) = π.
28. 🔴 Solve sin⁻¹x + sin⁻¹(1−x) = cos⁻¹x.
29. 🔴 ⭐ Solve tan⁻¹(x − 1) + tan⁻¹x + tan⁻¹(x + 1) = tan⁻¹(3x).
30. 🔴 Solve sin⁻¹(1 − x) − 2 sin⁻¹x = π/2.

---

### Type 7: Simplifying sin(cos⁻¹x) etc.

**Goal:** Evaluate expressions like sin(cos⁻¹x), cos(tan⁻¹x), etc.

**Key idea:** Draw a right triangle.

**Solved Example:**

Find sin(cos⁻¹(3/5)).

**Solution:**
```
Let θ = cos⁻¹(3/5) → cos θ = 3/5, θ ∈ [0, π]
So adj = 3, hyp = 5 → opp = 4
sin θ = 4/5
∴ sin(cos⁻¹(3/5)) = 4/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

31. 🟡 Find cos(tan⁻¹(4/3)).
32. 🟡 Find tan(sin⁻¹(12/13)).
33. 🟡 Find sec(tan⁻¹(2)).
34. 🟡 Find sin(cos⁻¹(5/13)).
35. 🔴 ⭐ Simplify sin(arctan x) in terms of x.

---

### Type 8: Simplifying Nested Inverse Expressions

**Goal:** Simplify expressions like sin(2 tan⁻¹x), cos(2 sin⁻¹x), etc.

**Solved Example:**

Simplify sin(2 tan⁻¹x).

**Solution:**
```
Let θ = tan⁻¹x → tan θ = x
sin 2θ = 2 tan θ/(1 + tan²θ) = 2x/(1 + x²)
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Simplify cos(2 tan⁻¹x).
37. 🟡 Simplify tan(2 sin⁻¹x).
38. 🟡 Simplify sin(2 cos⁻¹x).
39. 🔴 ⭐ Simplify tan(2 tan⁻¹(1/3)).
40. 🔴 Find the value of sin(2 tan⁻¹(2/3)) + cos(2 tan⁻¹(2/3)).

---

## Stage 4: Type Mixer

1. 🟡 Find the principal values: sin⁻¹(−1/√2), cos⁻¹(1/2), tan⁻¹(√3).

2. 🟡 Prove that arctan(1/2) + arctan(1/3) = π/4.

3. 🔴 ⭐ Evaluate: sin(cos⁻¹(3/5) + sin⁻¹(5/13)).

4. 🔴 Solve: tan⁻¹(2x) + tan⁻¹(3x) = π/4.

5. 🔴 Simplify: sin⁻¹(3/5) + sin⁻¹(8/17) = sin⁻¹(77/85).

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Find the principal value of sin⁻¹(−1/2). **(1 mark)**

**Solution:**
```
sin⁻¹(−1/2) = −π/6
```

---

**Q2.** 🟡 Find the value of cos⁻¹(cos 7π/6). **(2 marks)**

**Solution:**
```
cos(7π/6) = −√3/2
cos⁻¹(−√3/2) = 5π/6 (since 5π/6 ∈ [0, π])
```

---

**Q3.** 🟡 Write the value of sin⁻¹(3/5) + cos⁻¹(3/5). **(1 mark)**

**Solution:**
```
sin⁻¹(3/5) + cos⁻¹(3/5) = π/2
```

---

**Q4.** 🟡 Evaluate tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3). **(2 marks)**

**Solution:**
```
tan⁻¹(1) + tan⁻¹(2) = tan⁻¹((1+2)/(1−2)) = tan⁻¹(3/(−1)) = tan⁻¹(−3) = π − arctan(3) (not principal)

Better: tan⁻¹(1) = π/4
tan⁻¹(2) + tan⁻¹(3) = tan⁻¹((2+3)/(1−6)) = tan⁻¹(5/(−5)) = tan⁻¹(−1)
= −π/4 (but 2,3 > 0, so these are positive angles)
tan⁻¹(2) + tan⁻¹(3) = π + tan⁻¹(−1) = π − π/4 = 3π/4

Total = π/4 + 3π/4 = π
```

---

## Stage 6: JEE Mains Arena

**Q1.** The principal value of sin⁻¹(−√3/2) is:
(a) −π/3
(b) π/3
(c) 2π/3
(d) −2π/3

<details>
<summary>Solution</summary>
sin⁻¹(−√3/2) = −π/3 (in [−π/2, π/2])
Answer: (a) 🟢
</details>

---

**Q2.** tan⁻¹(1/2) + tan⁻¹(1/3) equals:
(a) π/6
(b) π/4
(c) π/3
(d) π/2

<details>
<summary>Solution</summary>
tan⁻¹(1/2) + tan⁻¹(1/3) = tan⁻¹((1/2+1/3)/(1−1/6)) = tan⁻¹(1) = π/4
Answer: (b) 🟡 ⭐
</details>

---

**Q3.** The value of sin⁻¹(sin 2π/3) is:
(a) π/3
(b) 2π/3
(c) −π/3
(d) π/6

<details>
<summary>Solution</summary>
sin(2π/3) = √3/2. sin⁻¹(√3/2) = π/3 (in [−π/2, π/2]).
Answer: (a) 🟡 ⭐
</details>

---

**Q4.** If tan⁻¹(2x) + tan⁻¹(3x) = π/4, then x equals:
(a) 1/6
(b) 1
(c) −1
(d) 0

<details>
<summary>Solution</summary>
tan⁻¹(5x/(1−6x²)) = π/4
5x/(1−6x²) = 1
5x = 1 − 6x²
6x² + 5x − 1 = 0
(6x − 1)(x + 1) = 0
x = 1/6 or x = −1
x = −1 gives LHS = tan⁻¹(−2) + tan⁻¹(−3) < 0, not π/4
x = 1/6 ✓
Answer: (a) 🔴 ⭐
</details>

---

**Q5.** The value of sin(cos⁻¹(3/5) + sin⁻¹(5/13)) is:
(a) 56/65
(b) 63/65
(c) 16/65
(d) 33/65

<details>
<summary>Solution</summary>
cos⁻¹(3/5) = α → cos α = 3/5, sin α = 4/5
sin⁻¹(5/13) = β → sin β = 5/13, cos β = 12/13
sin(α + β) = sin α cos β + cos α sin β = (4/5)(12/13) + (3/5)(5/13)
= 48/65 + 15/65 = 63/65
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin⁻¹x ∈ [−π/2, π/2].
**Reason (R):** The range of arcsin is the principal value branch.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** sin⁻¹(1/2) + cos⁻¹(1/2) = π/2.
**Reason (R):** sin⁻¹x + cos⁻¹x = π/2 for all x ∈ [−1, 1].

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sin⁻¹(sin 5π/4) = π/4.
**Reason (R):** sin⁻¹(sin x) = x for all x.

<details>
<summary>Solution</summary>
A is true: sin⁻¹(sin 5π/4) = sin⁻¹(−1/√2) = −π/4... wait, that's −π/4, not π/4.
Actually sin⁻¹(sin 5π/4) = sin⁻¹(−1/√2) = −π/4.
But 5π/4 = 225°, sin = −1/√2, principal value = −π/4.
So A is false (it's −π/4, not π/4).
R is false: sin⁻¹(sin x) = x only when x ∈ [−π/2, π/2].
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** tan⁻¹x + tan⁻¹(1/x) = π/2 for x > 0.
**Reason (R):** tan(π/2 − θ) = cot θ = 1/tan θ.

<details>
<summary>Solution</summary>
A is true: tan⁻¹x + tan⁻¹(1/x) = π/2 for x > 0.
R is true and explains A (since tan⁻¹x = θ, tan⁻¹(1/x) = π/2 − θ).
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The principal value of sin⁻¹(1/√2) is:
   (a) π/4   (b) π/3   (c) π/6   (d) π/2

2. 🟢 The principal value of cos⁻¹(1/2) is:
   (a) π/6   (b) π/3   (c) π/4   (d) π/2

3. 🟢 tan⁻¹(√3) equals:
   (a) π/6   (b) π/4   (c) π/3   (d) π/2

4. 🟡 sin⁻¹(−1) equals:
   (a) π/2   (b) −π/2   (c) π   (d) −π

5. 🟡 cos⁻¹(−1/2) equals:
   (a) π/3   (b) 2π/3   (c) π/6   (d) 5π/6

6. 🟡 sin⁻¹x + cos⁻¹x = ?<br>
   (a) 0   (b) π/2   (c) π   (d) −π/2

7. 🟡 tan⁻¹x + cot⁻¹x = ?<br>
   (a) 0   (b) π/2   (c) π   (d) −π/2

8. 🟡 sin⁻¹(sin π/4) = ?<br>
   (a) π/4   (b) 3π/4   (c) −π/4   (d) 5π/4

9. 🟡 cos⁻¹(cos 5π/4) = ?<br>
   (a) π/4   (b) 3π/4   (c) 5π/4   (d) −3π/4

10. 🟡 sin(cos⁻¹(4/5)) = ?<br>
    (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4

11. 🟡 cos(tan⁻¹(3/4)) = ?<br>
    (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4

12. 🟡 tan(sin⁻¹(5/13)) = ?<br>
    (a) 5/12   (b) 12/5   (c) 13/5   (d) 5/13

13. 🟡 Domain of sin⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) [−π/2, π/2]   (d) [0, π]

14. 🟡 Range of cos⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) [−π/2, π/2]   (d) [0, π]

15. 🟡 Domain of tan⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) (−π/2, π/2)   (d) (0, π)

16. 🟡 tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3) = ?<br>
    (a) π/2   (b) π   (c) 3π/2   (d) 2π

17. 🟡 sin⁻¹(12/13) + cos⁻¹(12/13) = ?<br>
    (a) 0   (b) π/2   (c) π   (d) −π/2

18. 🟡 sin⁻¹(sin 3) equals:
    (a) 3   (b) π − 3   (c) 3 − π   (d) −3

19. 🟡 tan⁻¹(2) + tan⁻¹(3) = ?<br>
    (a) π/4   (b) 3π/4   (c) π/2   (d) π

20. 🟡 The value of sin(2 sin⁻¹(3/5)) is:
    (a) 24/25   (b) 12/25   (c) 6/25   (d) 4/5

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | b | 16 | b |
| 2 | b | 7 | b | 12 | a | 17 | b |
| 3 | c | 8 | a | 13 | b | 18 | b |
| 4 | b | 9 | b | 14 | d | 19 | b |
| 5 | b | 10 | a | 15 | a | 20 | a |

</details>
