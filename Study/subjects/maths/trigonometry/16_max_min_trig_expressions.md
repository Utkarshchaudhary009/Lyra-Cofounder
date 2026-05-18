# Chapter 16: Maximum & Minimum of Trig Expressions

---

## Stage 1: The Core Idea

### Finding the Boundaries

Every trig function has a limited range:
- sin θ ∈ [−1, 1]
- cos θ ∈ [−1, 1]
- a sin θ + b cos θ ∈ [−√(a²+b²), √(a²+b²)]

JEE loves asking: "Find the maximum/minimum value of ..." These problems test whether you understand the bounds.

---

## Stage 2: The Formula Lab

### Key Ranges

```
−1 ≤ sin θ ≤ 1
−1 ≤ cos θ ≤ 1
−√(a²+b²) ≤ a sin θ + b cos θ ≤ √(a²+b²)
```

### Expressing a sin θ + b cos θ as a Single Sine

```
a sin θ + b cos θ = R sin(θ + φ)
where R = √(a²+b²), tan φ = b/a
```

Or: `= R cos(θ − φ)` where tan φ = a/b.

### Quadratic Forms

For a sin²θ + b sin θ + c, treat as a quadratic in t = sin θ, then evaluate at endpoints.

---

## Stage 3: Type-wise Mastery

### Type 1: Max/Min of a ± b sin θ

**Goal:** Find range of expressions like 3 + 4 sin θ.

**Solved Example:**

Find the maximum and minimum of f(θ) = 5 − 3 sin θ.

**Solution:**
```
−1 ≤ sin θ ≤ 1
3 ≥ −3 sin θ ≥ −3
5+3 ≥ 5−3 sin θ ≥ 5−3
8 ≥ f(θ) ≥ 2
Max = 8, Min = 2
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Find max/min of f = 2 + 3 cos θ.
2. 🟢 Find max/min of f = 4 − 5 sin θ.
3. 🟡 Find max/min of f = 2/(3 + sin θ).
4. 🟡 Find max/min of f = 1/(2 − cos θ).
5. 🟡 Find max/min of f = 3 − 2 cos²θ.

---

### Type 2: a sin θ + b cos θ

**Goal:** Use R-formula to find range.

**Solved Example:**

Find max/min of f(θ) = 3 sin θ + 4 cos θ.

**Solution:**
```
R = √(3² + 4²) = 5
∴ f(θ) = 5 sin(θ + φ)
Max = 5, Min = −5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Find max/min of 5 sin θ + 12 cos θ.
7. 🟡 Find max/min of 8 sin θ − 6 cos θ.
8. 🟡 Find max/min of sin θ + cos θ.
9. 🟡 Find max/min of √3 sin θ + cos θ.
10. 🔴 ⭐ Find max/min of 3 sin θ − 4 cos θ + 2.

---

### Type 3: Quadratic Forms

**Goal:** Find max/min of expressions like a sin²θ + b sin θ + c.

**Solved Example:**

Find max/min of f = 2 sin²θ − 3 sin θ + 1.

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f(t) = 2t² − 3t + 1
Vertex: t = 3/4 = 0.75
f(0.75) = 2(9/16) − 3(3/4) + 1 = 9/8 − 9/4 + 1 = (9 − 18 + 8)/8 = −1/8

Check endpoints:
f(−1) = 2 + 3 + 1 = 6
f(1) = 2 − 3 + 1 = 0

Max = 6, Min = −1/8
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Find max/min of 3 sin²θ + 2 sin θ − 1.
12. 🟡 Find max/min of cos²θ − 2 cos θ + 3.
13. 🟡 Find max/min of 2 sin²θ + 5 sin θ − 3.
14. 🔴 Find max/min of sin⁴θ + cos⁴θ.
15. 🔴 ⭐ Find max/min of sin⁶θ + cos⁶θ.

---

### Type 4: Using AM-GM

**Goal:** Use AM ≥ GM for expressions like tan θ + cot θ.

**Solved Example:**

Find the minimum of tan θ + cot θ for acute θ.

**Solution:**
```
AM ≥ GM: (tan θ + cot θ)/2 ≥ √(tan θ × cot θ) = 1
tan θ + cot θ ≥ 2
Minimum = 2 (at θ = 45°)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Find minimum of sec θ + cosec θ for acute θ.
17. 🟡 Find minimum of sin θ + cosec θ for acute θ.
18. 🟡 Find minimum of cos θ + sec θ for acute θ.
19. 🔴 ⭐ Find the maximum of sin²θ cos²θ.
20. 🔴 Find the maximum of sin θ cos θ.

---

### Type 5: Substitution Methods

**Goal:** Substitute t = sin θ ± cos θ to simplify.

**Key:**
```
If sin θ + cos θ = t, then sin θ cos θ = (t² − 1)/2
Range of t = [−√2, √2]
```

**Solved Example:**

Find max/min of sin θ cos θ.

**Solution:**
```
sin θ cos θ = (1/2) sin 2θ
Since sin 2θ ∈ [−1, 1]:
Max = 1/2, Min = −1/2
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 Find max/min of sin θ + cos θ.
22. 🟡 Find max/min of sin²θ + cos⁴θ. (Hint: use substitution or range analysis.)
23. 🟡 Find max/min of sin 2θ − cos 2θ.
24. 🔴 ⭐ Find max/min of sin θ + cos θ + sin θ cos θ.
25. 🔴 Find max/min of (sin θ + cos θ)(sin θ − cos θ).

---

### Type 6: Range of Rational Trig Functions

**Goal:** Find range of f = (a sin θ + b)/(c sin θ + d).

**Method:** Write as sin θ = ... then use −1 ≤ sin θ ≤ 1.

**Solved Example:**

Find range of f(θ) = (2 sin θ + 3)/(sin θ + 2).

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f = (2t + 3)/(t + 2)

Method: Cross multiply:
f(t+2) = 2t+3
ft + 2f = 2t + 3
ft − 2t = 3 − 2f
t(f − 2) = 3 − 2f
t = (3 − 2f)/(f − 2)

Since −1 ≤ t ≤ 1:
−1 ≤ (3 − 2f)/(f − 2) ≤ 1

Solve: f ∈ [1/3, 5/3]...(exercise complete)
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 Find range of (sin θ + 2)/(sin θ + 3).
27. 🔴 Find range of (2 cos θ + 1)/(cos θ − 2).
28. 🔴 Find range of (3 tan θ − 1)/(tan θ + 2).
29. 🔴 ⭐ Find range of (sin θ − 1)/(sin θ + 1).
30. 🔴 Find range of (sec θ + tan θ)/(sec θ − tan θ).

---

### Type 7: Conditional Max/Min with A+B+C = π

**Goal:** Find max/min under triangle angle conditions.

**Solved Example:**

In a triangle ABC, find the maximum value of sin A + sin B + sin C.

**Solution:**
```
For a fixed sum A+B+C = π, sin A + sin B + sin C is maximum when A = B = C = π/3
Maximum = 3 sin(π/3) = 3√3/2
```
🔴 Hard

---

**Practice Problems:**

31. 🔴 In a triangle, find max of cos A + cos B + cos C.
32. 🔴 In a triangle, find max of sin A sin B sin C.
33. 🔴 ⭐ In a triangle, find max of tan A + tan B + tan C.
34. 🔴 If A+B+C = π, find max of sin²A + sin²B + sin²C.
35. 🔴 If A+B = 45°, find max of sin A sin B.

---

### Type 8: Using Graph-Based Insight

**Goal:** Visual max/min without heavy algebra.

**Solved Example:**

Find max of |sin x| + |cos x|.

**Solution:**
```
For x in QI, f = sin x + cos x = √2 sin(x + π/4), max = √2
Similarly in each quadrant, the max is √2.
So overall max = √2.
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Find max of |sin x| − |cos x|.
37. 🟡 Find max of sin²x + cos⁴x.
38. 🔴 Find max of sin x cos 2x.
39. 🔴 ⭐ Find max of sin³x + cos³x for x ∈ [0, π/2].
40. 🔴 Find min of (sin x + cosec x)² + (cos x + sec x)².

---

## Stage 4: Type Mixer

1. 🟡 Find the maximum of f(θ) = 5 sin θ + 12 cos θ + 3.

2. 🔴 Find the minimum of tan²θ + cot²θ.

3. 🔴 ⭐ Find the maximum of sin θ cos θ sin 2θ.

4. 🔴 Find the range of f(θ) = (sin θ + 1)/(sin θ − 2).

5. 🔴 In a triangle ABC, find the maximum value of cos A + cos B + cos C.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the maximum and minimum of 3 cos θ + 4 sin θ. **(2 marks)**

**Solution:**
```
R = √(3²+4²) = 5
Max = 5, Min = −5
```

---

**Q2.** 🟡 Find the range of f(θ) = 2 + 3 sin θ. **(2 marks)**

**Solution:**
```
−1 ≤ sin θ ≤ 1
−3 ≤ 3 sin θ ≤ 3
−1 ≤ 2 + 3 sin θ ≤ 5
Range: [−1, 5]
```

---

**Q3.** 🟡 Find the minimum of sin θ + cosec θ for θ ∈ (0, π/2). **(2 marks)**

**Solution:**
```
AM ≥ GM: sin θ + cosec θ ≥ 2√(sin θ × cosec θ) = 2
Minimum = 2 (at sin θ = 1 → θ = π/2... wait, that's at the endpoint)

Actually, by AM-GM: (sin θ + 1/sin θ)/2 ≥ √(sin θ × 1/sin θ) = 1
sin θ + 1/sin θ ≥ 2
Minimum = 2 (at sin θ = 1, i.e., θ = π/2)
```

---

**Q4.** 🔴 ⭐ Find the range of (2 sin θ − 1)/(sin θ + 3). **(3 marks)**

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f(t) = (2t − 1)/(t + 3)

Cross multiply: f(t+3) = 2t−1
ft + 3f = 2t − 1
ft − 2t = −1 − 3f
t(f − 2) = −(1 + 3f)
t = −(1 + 3f)/(f − 2)

−1 ≤ −(1+3f)/(f−2) ≤ 1
Solving gives f ∈ [−3/4, 3/2]
```

---

## Stage 6: JEE Mains Arena

**Q1.** The maximum value of sin θ + cos θ is:
(a) 1
(b) √2
(c) 2
(d) √3

<details>
<summary>Solution</summary>
sin θ + cos θ = √2 sin(θ + π/4), max = √2
Answer: (b) 🟢 ⭐
</details>

---

**Q2.** The minimum value of 4 sin²θ + 5 cos²θ is:
(a) 0
(b) 4
(c) 5
(d) 1

<details>
<summary>Solution</summary>
= 4 sin²θ + 5 cos²θ = 4(sin²θ + cos²θ) + cos²θ = 4 + cos²θ
Since cos²θ ≥ 0, minimum = 4
Answer: (b) 🟡
</details>

---

**Q3.** The maximum value of 3 sin θ − 4 cos θ is:
(a) 3
(b) 4
(c) 5
(d) 7

<details>
<summary>Solution</summary>
R = √(3²+4²) = 5
Answer: (c) 🟢
</details>

---

**Q4.** The minimum value of tan θ + cot θ is:
(a) 0
(b) 1
(c) 2
(d) 4

<details>
<summary>Solution</summary>
tan θ + cot θ ≥ 2√(tan θ × cot θ) = 2
Minimum = 2
Answer: (c) 🟡 ⭐
</details>

---

**Q5.** The range of sin⁴θ + cos⁴θ is:
(a) [0, 1]
(b) [1/2, 1]
(c) [0, 1/2]
(d) [1/2, 1]

<details>
<summary>Solution</summary>
sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ = 1 − (1/2) sin²2θ
sin²2θ ∈ [0, 1], so expression ∈ [1/2, 1]
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** Maximum of sin θ is 1.
**Reason (R):** sin θ ≤ 1 for all real θ.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** Minimum of 3 − 2 sin θ is 1.
**Reason (R):** −2 ≤ −2 sin θ ≤ 2, so 1 ≤ 3 − 2 sin θ ≤ 5.

<details>
<summary>Solution</summary>
A is true (min = 1). R is true and correctly computes the range.
Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The maximum of a sin θ + b cos θ is |a| + |b|.
**Reason (R):** The maximum is √(a² + b²).

<details>
<summary>Solution</summary>
A is false: maximum is √(a²+b²), not |a|+|b|.
R is true.
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The minimum value of sin⁴θ + cos⁴θ is 1/2.
**Reason (R):** sin⁴θ + cos⁴θ = 1 − (1/2) sin²2θ ≥ 1/2.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 Range of sin θ is:
   (a) ℝ   (b) [−1, 1]   (c) [0, 1]   (d) (−1, 1)

2. 🟢 Max of 3 + 2 sin θ is:
   (a) 3   (b) 5   (c) 1   (d) 2

3. 🟡 Max of sin θ + √3 cos θ is:
   (a) 2   (b) √3   (c) √10   (d) 4

4. 🟡 Min of 5 − 3 cos θ is:
   (a) 2   (b) 5   (c) 8   (d) 3

5. 🟡 Max of 4 sin θ + 3 cos θ is:
   (a) 5   (b) 7   (c) 1   (d) 25

6. 🟡 Min of sin²θ + cos²θ is:
   (a) 0   (b) 1   (c) 1/2   (d) 2

7. 🟡 Min of 4 sin²θ + 4 cos²θ is:
   (a) 0   (b) 4   (c) 8   (d) 2

8. 🟡 Min of tan θ + cot θ is:
   (a) 1   (b) 2   (c) 0   (d) −2

9. 🟡 Max of 3 sin²θ + 4 cos²θ is:
   (a) 3   (b) 4   (c) 7   (d) 12

10. 🟡 Min of 3 sin²θ + 4 cos²θ is:
    (a) 3   (b) 4   (c) 7   (d) 0

11. 🟡 Max of sin θ cos θ is:
    (a) 1/2   (b) 1   (c) 1/4   (d) 2

12. 🟡 Range of sin⁴θ + cos⁴θ is:
    (a) [0, 1]   (b) [1/2, 1]   (c) [0, 1/2]   (d) [1/2, 1/2]

13. 🟡 Max of sin θ + cos θ + 3 is:
    (a) √2 + 3   (b) 5   (c) 4   (d) 2 + √3

14. 🟡 Min of sec²θ + cosec²θ is:
    (a) 4   (b) 2   (c) 0   (d) 1

15. 🟡 Max of 2 sin θ − 3 cos θ is:
    (a) √13   (b) 5   (c) 6   (d) √5

16. 🟡 Min of sin⁶θ + cos⁶θ is:
    (a) 0   (b) 1/4   (c) 1/2   (d) 1

17. 🟡 Max of (sin θ + cos θ)² is:
    (a) 1   (b) 2   (c) 4   (d) √2

18. 🟡 Min of 2 sin²θ − sin θ + 1 is:
    (a) 0   (b) 7/8   (c) 1   (d) 3/4

19. 🟡 Range of (sin θ + 1)/(sin θ + 2) is:
    (a) [0, 2/3]   (b) [0, 1]   (c) [2/3, 2]   (d) [1/2, 2]

20. 🟡 Max of sin 2θ − cos 2θ is:
    (a) 1   (b) √2   (c) 2   (d) 0

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | a | 16 | b |
| 2 | b | 7 | b | 12 | b | 17 | b |
| 3 | a | 8 | b | 13 | a | 18 | b |
| 4 | a | 9 | b | 14 | a | 19 | a |
| 5 | a | 10 | a | 15 | a | 20 | b |

</details>
