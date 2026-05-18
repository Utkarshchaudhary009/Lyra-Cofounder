# Chapter 17: Trigonometric Inequalities

---

## Stage 1: The Core Idea

### Solving "Sin θ > 1/2"

An equation like sin θ = 1/2 gives specific points. An inequality like sin θ > 1/2 gives a **range** of θ values.

Solving trig inequalities uses:
1. The **unit circle** — visualise where on the circle the condition holds
2. **Graphs** — see which intervals satisfy the inequality
3. **Algebra** — combine with domain restrictions

---

## Stage 2: The Formula Lab

### Key Graphs for Inequalities

```
sin θ > k:   θ ∈ (arcsin k, π − arcsin k) in [0, 2π]
sin θ < k:   θ ∈ [0, arcsin k) ∪ (π − arcsin k, 2π)

cos θ > k:   θ ∈ (−arccos k, arccos k) in [0, 2π] → that is θ ∈ [0, arccos k) ∪ (2π − arccos k, 2π)
cos θ < k:   θ ∈ (arccos k, 2π − arccos k)

tan θ > k:   θ ∈ (arctan k, π/2) ∪ (π/2 + arctan k, 3π/2)...
```

---

## Stage 3: Type-wise Mastery

### Type 1: sin θ > k

**Goal:** Solve sin θ > 1/2 for θ ∈ [0, 2π].

**Solved Example:**

Solve sin θ > 1/2 for θ ∈ [0, 2π].

**Solution:**
```
sin θ = 1/2 at θ = π/6, 5π/6
sin θ > 1/2 when the y-coordinate on unit circle > 1/2
This happens when θ ∈ (π/6, 5π/6)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Solve sin θ ≤ 1/2 for θ ∈ [0, 2π].
2. 🟡 Solve sin θ > 0 for θ ∈ [0, 2π].
3. 🟡 Solve sin θ < −1/2 for θ ∈ [0, 2π].
4. 🟡 Solve sin θ ≥ −√3/2 for θ ∈ [0, 2π].
5. 🔴 Solve sin θ ≥ 0 for θ ∈ [0, 4π].

---

### Type 2: cos θ > k

**Goal:** Solve cos θ > 1/2 for θ ∈ [0, 2π].

**Solved Example:**

Solve cos θ ≥ 1/2 for θ ∈ [0, 2π].

**Solution:**
```
cos θ = 1/2 at θ = π/3, 5π/3
cos θ ≥ 1/2 when x-coordinate on unit circle ≥ 1/2
This happens when θ ∈ [0, π/3] ∪ [5π/3, 2π]
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 Solve cos θ > 0 for θ ∈ [0, 2π].
7. 🟡 Solve cos θ ≤ −1/2 for θ ∈ [0, 2π].
8. 🟡 Solve cos θ < √3/2 for θ ∈ [0, 2π].
9. 🟡 Solve cos θ > −1/√2 for θ ∈ [0, 2π].
10. 🔴 Solve |cos θ| ≤ 1/2 for θ ∈ [0, 2π].

---

### Type 3: tan θ > k

**Goal:** Solve tan θ > 1 for θ ∈ [0, 2π].

**Solved Example:**

Solve tan θ > 1 for θ ∈ [0, 2π].

**Solution:**
```
tan θ = 1 at θ = π/4, 5π/4
tan θ > 1 when:
θ ∈ (π/4, π/2) ∪ (5π/4, 3π/2)
(Near the asymptote, tan goes to +∞)
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Solve tan θ ≤ √3 for θ ∈ [0, 2π].
12. 🟡 Solve tan θ > 0 for θ ∈ [0, 2π].
13. 🟡 Solve tan θ < −1 for θ ∈ [0, 2π].
14. 🟡 Solve tan θ ≥ 0 for θ ∈ [0, π].
15. 🔴 ⭐ Solve tan θ ≤ 1 for θ ∈ [0, 2π].

---

### Type 4: Quadratic Inequalities

**Goal:** Solve 2 sin²θ − sin θ − 1 > 0.

**Solved Example:**

Solve 2 sin²θ − sin θ − 1 > 0 for θ ∈ [0, 2π].

**Solution:**
```
Let t = sin θ: 2t² − t − 1 > 0
(2t + 1)(t − 1) > 0
t < −1/2 or t > 1

t > 1: impossible (max sin = 1)
t < −1/2: sin θ < −1/2

sin θ = −1/2 at θ = 7π/6, 11π/6
sin θ < −1/2 when θ ∈ (7π/6, 11π/6)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Solve 2 cos²θ − cos θ − 1 ≤ 0 for θ ∈ [0, 2π].
17. 🟡 Solve 4 sin²θ − 1 > 0 for θ ∈ [0, 2π].
18. 🟡 Solve tan²θ − √3 tan θ ≤ 0 for θ ∈ [0, 2π].
19. 🔴 Solve 2 sin²θ + 3 sin θ − 2 > 0 for θ ∈ [0, 2π].
20. 🔴 ⭐ Solve 2 cos²θ + 5 cos θ + 2 < 0 for θ ∈ [0, 2π].

---

### Type 5: Combined sin and cos Inequalities

**Goal:** Solve sin θ ≤ cos θ.

**Solved Example:**

Solve sin θ ≤ cos θ for θ ∈ [0, 2π].

**Solution:**
```
sin θ ≤ cos θ → sin θ − cos θ ≤ 0 → √2 sin(θ − π/4) ≤ 0
sin(θ − π/4) ≤ 0
θ − π/4 ∈ [π, 2π] (in [0, 2π] range)
θ ∈ [5π/4, 9π/4] → θ ∈ [5π/4, 2π) ∪ [0, π/4]
```
🔴 Hard

---

**Practice Problems:**

21. 🔴 Solve sin θ ≥ cos θ for θ ∈ [0, 2π].
22. 🔴 Solve sin θ > cos θ for θ ∈ [0, π].
23. 🔴 Solve |sin θ| ≤ |cos θ| for θ ∈ [0, 2π].
24. 🔴 ⭐ Solve sin θ cos θ < 0 for θ ∈ [0, 2π].
25. 🔴 Solve sin θ + cos θ > 1 for θ ∈ [0, 2π].

---

### Type 6: Domain-Restricted Inequalities

**Goal:** Solve considering the domain of tan, sec, etc.

**Solved Example:**

Find the domain of f(θ) = 1/√(sin θ) for θ ∈ [0, 2π].

**Solution:**
```
sin θ > 0 (since denominator under root must be positive)
sin θ > 0 when θ ∈ (0, π)
But also, sin θ ≠ 0 (not in denominator anyway since > 0)
Domain: (0, π)
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 Find domain of f(θ) = 1/√(cos θ).
27. 🟡 Find domain of f(θ) = √(tan θ).
28. 🟡 Find domain of f(θ) = 1/(sin θ − 1/2).
29. 🔴 ⭐ Find domain of f(θ) = √(sin θ) + √(cos θ).
30. 🔴 Find domain of f(θ) = √(2 sin θ − 1).

---

### Type 7: Product Inequalities

**Goal:** Solve (sin θ)(cos θ) ≥ 0.

**Solved Example:**

Solve sin θ cos θ > 0 for θ ∈ [0, 2π].

**Solution:**
```
sin θ cos θ > 0 when sin θ and cos θ have the SAME sign.
sin θ > 0, cos θ > 0 → QI → θ ∈ (0, π/2)
sin θ < 0, cos θ < 0 → QIII → θ ∈ (π, 3π/2)
Answer: (0, π/2) ∪ (π, 3π/2)
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 Solve sin θ cos θ < 0 for θ ∈ [0, 2π].
32. 🟡 Solve (sin θ − 1/2)(cos θ + 1/2) ≥ 0 for θ ∈ [0, 2π].
33. 🔴 Solve (tan θ)(sin θ) > 0 for θ ∈ [0, 2π].
34. 🔴 ⭐ Solve (sin θ − cos θ)(sin θ + cos θ) ≤ 0 for θ ∈ [0, 2π].
35. 🔴 Solve (2 sin θ − 1)(cos θ + 1) ≥ 0 for θ ∈ [0, 2π].

---

### Type 8: Inequalities in a Given Interval

**Goal:** Solve with specific interval restrictions.

**Solved Example:**

Solve sin θ > 1/2 for θ ∈ [−π, π].

**Solution:**
```
sin θ = 1/2 at θ = π/6, 5π/6
But 5π/6 > π, so out of range.
In [−π, π], sin > 1/2 when θ ∈ (π/6, 5π/6) but only the part within [−π, π]
Actually sin θ is positive and > 1/2 in QII as well, so 5π/6 is in range (it's < π).

sin θ > 1/2 for θ ∈ (π/6, 5π/6)
Both endpoints are within [−π, π].
Answer: (π/6, 5π/6)
```
🔴 Hard

---

**Practice Problems:**

36. 🔴 Solve cos θ ≤ 1/2 for θ ∈ [0, π].
37. 🔴 Solve tan θ > 1 for θ ∈ [−π/2, π/2].
38. 🔴 Solve sin θ + cos θ > 0 for θ ∈ [0, π].
39. 🔴 ⭐ Solve 2 cos²θ − 3 cos θ + 1 > 0 for θ ∈ [0, π].
40. 🔴 Solve |sin θ| < 1/2 for θ ∈ [0, 2π].

---

## Stage 4: Type Mixer

1. 🟡 Solve sin θ > cos θ for θ ∈ [0, 2π].

2. 🟡 Solve 2 sin²θ − sin θ − 1 < 0 for θ ∈ [0, 2π].

3. 🔴 ⭐ Find the domain of f(θ) = √((sin θ − 1/2)(cos θ + 1/2)).

4. 🔴 Solve sin θ + sin 2θ > 0 for θ ∈ [0, 2π].

5. 🔴 Solve sec²θ − 2 tan θ ≥ 0 for θ ∈ [0, 2π].

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Solve sin θ > 1/2 for θ ∈ [0, 2π]. **(2 marks)**

**Solution:**
```
sin θ = 1/2 at π/6, 5π/6
sin θ > 1/2 when θ ∈ (π/6, 5π/6)
```

---

**Q2.** 🟡 Solve cos θ < 0 for θ ∈ [0, 2π]. **(1 mark)**

**Solution:**
```
cos θ < 0 in QII and QIII
θ ∈ (π/2, 3π/2)
```

---

**Q3.** 🟡 Solve 2 sin²θ − 3 sin θ + 1 ≤ 0 for θ ∈ [0, 2π]. **(3 marks)**

**Solution:**
```
Let t = sin θ: 2t² − 3t + 1 ≤ 0
(2t − 1)(t − 1) ≤ 0
1/2 ≤ t ≤ 1

sin θ ≥ 1/2 and sin θ ≤ 1
sin θ ≥ 1/2: θ ∈ [π/6, 5π/6]
sin θ ≤ 1: always true (except sin θ can be > 1?<br> no)

Answer: θ ∈ [π/6, 5π/6]
```

---

**Q4.** 🟡 Find the domain of f(x) = 1/√(2 sin x − 1). **(2 marks)**

**Solution:**
```
2 sin x − 1 > 0
sin x > 1/2
x ∈ (π/6, 5π/6) + 2nπ for n ∈ ℤ
```

---

## Stage 6: JEE Mains Arena

**Q1.** The solution set of sin θ > 1/2 in [0, 2π] is:
(a) (π/6, 5π/6)
(b) (π/3, 2π/3)
(c) (π/6, π/3)
(d) (π/6, 5π/6)

<details>
<summary>Solution</summary>
sin θ = 1/2 at π/6, 5π/6. sin > 1/2 between them.
Answer: (a) 🟡
</details>

---

**Q2.** The solution set of cos θ ≤ −1/2 in [0, 2π] is:
(a) [π/3, 5π/3]
(b) [2π/3, 4π/3]
(c) [π/2, 3π/2]
(d) [π/3, 2π/3]

<details>
<summary>Solution</summary>
cos θ = −1/2 at 2π/3, 4π/3. cos ≤ −1/2 between them (inclusive).
Answer: (b) 🟡
</details>

---

**Q3.** The number of integers n for which sin⁻¹(sin n) > 0 is:
(a) 0
(b) 1
(c) 2
(d) Infinite

<details>
<summary>Solution</summary>
sin⁻¹(sin n) > 0 when n is not an integer multiple of π where sin = 0.
Actually sin⁻¹(sin n) > 0 when sin n > 0 and the principal value is positive.
This holds for infinitely many integers n.
Answer: (d) 🔴
</details>

---

**Q4.** The domain of f(x) = √(sin x) + √(cos x) is:
(a) [2nπ, (2n+1)π/2]
(b) [2nπ, (2n+1)π]
(c) [(2n+1)π/2, (2n+1)π]
(d) [2nπ, 2nπ + π/2]

<details>
<summary>Solution</summary>
sin x ≥ 0 and cos x ≥ 0 → x in QI
x ∈ [2nπ, 2nπ + π/2]
Answer: (d) 🟡 ⭐
</details>

---

**Q5.** The solution of sin θ + cos θ > 0 in [0, 2π] is:
(a) (0, 3π/4)
(b) (0, 3π/4) ∪ (7π/4, 2π)
(c) (0, π/2)
(d) (3π/4, 7π/4)

<details>
<summary>Solution</summary>
sin θ + cos θ = √2 sin(θ + π/4) > 0
sin(θ + π/4) > 0
0 < θ + π/4 < π → −π/4 < θ < 3π/4
But θ ∈ [0, 2π], so: 0 ≤ θ < 3π/4
Also 2π < θ + π/4 < 3π → 7π/4 < θ < 11π/4
So 7π/4 < θ ≤ 2π
Answer: (0, 3π/4) ∪ (7π/4, 2π)
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin θ > 0 for θ ∈ (0, π).
**Reason (R):** Sin is positive in QI and QII.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** The inequality cos θ < 0 has solution θ ∈ (π/2, 3π/2) in [0, 2π].
**Reason (R):** Cos negative in QII and QIII.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The expression √(sin θ) is defined for θ ∈ [0, π].
**Reason (R):** sin θ ≥ 0 for θ ∈ [0, π].

<details>
<summary>Solution</summary>
A is true (domain includes 0 and π where sin=0).
R is true and explains A.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** sin θ + cos θ > 0 for all θ ∈ (0, π/2).
**Reason (R):** Both sin and cos are positive in QI.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin θ > 0 in:
   (a) QI, QII   (b) QI, QIV   (c) QII, QIII   (d) QIII, QIV

2. 🟢 cos θ < 0 in:
   (a) QI, QII   (b) QI, QIV   (c) QII, QIII   (d) QIII, QIV

3. 🟡 sin θ > 1/2 in [0, 2π] for θ ∈:
   (a) (π/6, 5π/6)   (b) (π/3, 2π/3)   (c) (0, π/6)   (d) (5π/6, 2π)

4. 🟡 cos θ > 1/2 in [0, 2π] for θ ∈:
   (a) (0, π/3) ∪ (5π/3, 2π)   (b) (π/3, 5π/3)   (c) (0, π/3)   (d) (5π/3, 2π)

5. 🟡 tan θ > 0 in:
   (a) QI, QIII   (b) QI, QII   (c) QI, QIV   (d) QII, QIV

6. 🟡 The domain of √(sin x) is:
   (a) [0, π]   (b) [2nπ, (2n+1)π]   (c) [−π/2, π/2]   (d) ℝ

7. 🟡 sin θ cos θ > 0 in:
   (a) QI, QIII   (b) QI, QII   (c) QI, QIV   (d) QII, QIV

8. 🟡 The solution of sin θ ≥ 1/2 in [0, π] is:
   (a) [π/6, 5π/6]   (b) [π/6, π/2]   (c) [0, π/6]   (d) [5π/6, π]

9. 🟡 The inequality 2 sin²θ − sin θ − 1 < 0 has solution (in [0, 2π]):
   (a) (π/6, 5π/6)   (b) (0, π/6) ∪ (5π/6, 2π)   (c) (−π/6, π/6)   (d) (π/2, 2π)

10. 🟡 The domain of f(x) = 1/√(cos x) is:
    (a) ℝ   (b) (−π/2, π/2)   (c) (2nπ − π/2, 2nπ + π/2)   (d) [0, π]

11. 🟡 tan θ > 1 in [0, 2π] for θ ∈:
    (a) (π/4, π/2) ∪ (5π/4, 3π/2)   (b) (π/4, π/2)   (c) (0, π/4)   (d) (π/2, 5π/4)

12. 🟡 sin θ + cos θ > 0 for:
    (a) All θ   (b) No θ   (c) θ ∈ (0, 3π/4) ∪ (7π/4, 2π)   (d) θ ∈ (π/4, 5π/4)

13. 🟡 |sin θ| > 1/2 in [0, 2π] means θ ∈:
    (a) (π/6, 5π/6) ∪ (7π/6, 11π/6)   (b) (0, π/6)   (c) (5π/6, 2π)   (d) ℝ

14. 🟡 The smallest positive θ satisfying sin θ > cos θ is:
    (a) π/4   (b) π/2   (c) 0   (d) π/6

15. 🟡 2 cos²θ − 3 cos θ + 1 ≤ 0 gives cos θ ∈:
    (a) [1/2, 1]   (b) [0, 1/2]   (c) [−1, 1/2]   (d) [−1, −1/2]

16. 🟡 Domain of √(2 sin x − 1) is:
    (a) [π/6, 5π/6]   (b) [π/3, 2π/3]   (c) (π/6, 5π/6)   (d) [0, π/6]

17. 🟡 Solution of cos θ ≤ −√3/2 in [0, 2π]:
    (a) [5π/6, 7π/6]   (b) [π/3, 2π/3]   (c) [2π/3, 4π/3]   (d) [π/6, 11π/6]

18. 🟡 The inequality sec θ > √2 in [0, 2π] has solution:
    (a) (0, π/4) ∪ (7π/4, 2π)   (b) (π/4, 7π/4)   (c) (0, π/4)   (d) (π/4, π/2)

19. 🟡 sin θ + sin 2θ > 0 in [0, 2π] has:
    (a) 1 interval   (b) 2 intervals   (c) 3 intervals   (d) No solution

20. 🟡 The set of θ satisfying sin θ ≥ 0 and cos θ ≥ 0 is:
    (a) [0, π/2]   (b) [π/2, π]   (c) [π, 3π/2]   (d) [3π/2, 2π]

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | a | 16 | a |
| 2 | c | 7 | a | 12 | c | 17 | a |
| 3 | a | 8 | a | 13 | a | 18 | a |
| 4 | a | 9 | b | 14 | a | 19 | c |
| 5 | a | 10 | c | 15 | a | 20 | a |

</details>
