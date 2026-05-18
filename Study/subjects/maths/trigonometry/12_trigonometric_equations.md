# Chapter 12: Trigonometric Equations

---

## Stage 1: The Core Idea

### Finding All Angles That Satisfy an Equation

If I ask "solve sin θ = 1/2", most students say "θ = 30°". But the correct answer is:

θ = 30°, 150°, 390°, 510°, −210°, −330°, ...

Because trig functions are **periodic**, a simple equation has **infinitely many solutions**.

We express this using **general solutions**:
```
sin θ = 1/2 → θ = nπ + (−1)ⁿ(π/6)
```

This chapter is about finding **all** solutions — not just the first one.

---

## Stage 2: The Formula Lab

### General Solutions

| Equation | General Solution |
|----------|-----------------|
| sin θ = sin α | θ = nπ + (−1)ⁿα |
| cos θ = cos α | θ = 2nπ ± α |
| tan θ = tan α | θ = nπ + α |
| sin θ = 0 | θ = nπ |
| cos θ = 0 | θ = (2n+1)π/2 |
| tan θ = 0 | θ = nπ |

Where n ∈ ℤ.

### Principal Solutions

Solutions in the interval [0, 2π) or [0°, 360°).

### Types of Equations

1. **Direct**: sin θ = k, cos θ = k, tan θ = k (where |k| ≤ 1)
2. **Quadratic**: a sin²θ + b sin θ + c = 0
3. **Factorisable**: Using identities to factor
4. **Using transformations**: Sum→product → zero factor property
5. **Conditional**: Involving domain restrictions

---

## Stage 3: Type-wise Mastery

### Type 1: Solving sin θ = k

**Goal:** Find principal and general solutions for sin θ = k.

**Solved Example:**

Solve sin θ = √3/2.

**Solution:**
```
Principal: θ = 60°, 120° (in [0°, 360°])
General: θ = nπ + (−1)ⁿ(π/3)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Solve sin θ = 1/2. Give principal and general solutions.
2. 🟡 Solve sin θ = 0. Give general solution.
3. 🟡 Solve sin θ = −1/√2. Give principal solutions.
4. 🟡 Solve sin θ = 1. Give general solution.
5. 🔴 Solve sin θ = √(3)/2 for θ ∈ [−π, π].

---

### Type 2: Solving cos θ = k

**Goal:** Find principal and general solutions for cos θ = k.

**Solved Example:**

Solve cos θ = 1/2.

**Solution:**
```
Principal: θ = 60°, 300°
General: θ = 2nπ ± π/3
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Solve cos θ = √3/2.
7. 🟡 Solve cos θ = 0.
8. 🟡 Solve cos θ = −1/2.
9. 🟡 Solve cos θ = −1.
10. 🔴 Solve cos θ = 0.5 for θ ∈ [−π, π].

---

### Type 3: Solving tan θ = k

**Goal:** Find principal and general solutions for tan θ = k.

**Solved Example:**

Solve tan θ = √3.

**Solution:**
```
Principal: θ = 60°, 240°
General: θ = nπ + π/3
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Solve tan θ = 1.
12. 🟡 Solve tan θ = 0.
13. 🟡 Solve tan θ = 1/√3.
14. 🟡 Solve tan θ = −1.
15. 🔴 Solve tan θ = −√3 for θ ∈ [0, 2π].

---

### Type 4: Quadratic in sin θ or cos θ

**Goal:** Solve equations like a sin²θ + b sin θ + c = 0.

**Solved Example:**

Solve 2 sin²θ − sin θ − 1 = 0 for 0° ≤ θ ≤ 360°.

**Solution:**
```
Let t = sin θ → 2t² − t − 1 = 0
(2t + 1)(t − 1) = 0
t = −1/2 or t = 1

sin θ = 1 → θ = 90°
sin θ = −1/2 → θ = 210°, 330°

Answer: θ = 90°, 210°, 330°
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Solve 2 cos²θ − 3 cos θ + 1 = 0 for 0° ≤ θ ≤ 360°.
17. 🟡 Solve 4 sin²θ = 1 for 0° ≤ θ ≤ 360°.
18. 🟡 Solve tan²θ − √3 tan θ = 0 for 0° ≤ θ ≤ 180°.
19. 🔴 Solve 2 sin²θ + 3 cos θ = 0 for 0° ≤ θ ≤ 360°. (Hint: Convert sin² to cos².)
20. 🔴 ⭐ Solve 3 cos²θ + 2 sin θ − 2 = 0 for 0° ≤ θ ≤ 360°.

---

### Type 5: Using sin²θ + cos²θ = 1 to Convert

**Goal:** Solve equations mixing sin and cos by converting using the identity.

**Solved Example:**

Solve 2 cos²θ + 3 sin θ = 0 for 0° ≤ θ ≤ 360°.

**Solution:**
```
2(1 − sin²θ) + 3 sin θ = 0
2 − 2 sin²θ + 3 sin θ = 0
2 sin²θ − 3 sin θ − 2 = 0
(2 sin θ + 1)(sin θ − 2) = 0
sin θ = −1/2 or sin θ = 2 (impossible)
θ = 210°, 330°
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 Solve 5 sin²θ − 4 cos θ = 4 for 0° ≤ θ ≤ 360°.
22. 🟡 Solve 2 sin²θ + 5 cos θ + 1 = 0 for 0° ≤ θ ≤ 360°.
23. 🟡 Solve 3 sin²θ + 4 cos²θ = 5 for 0° ≤ θ ≤ 360°.
24. 🔴 Solve sec²θ = 1 + tan θ for 0° ≤ θ ≤ 360°.
25. 🔴 ⭐ Solve 2 sin²θ + sin²2θ = 2 for 0° ≤ θ ≤ 360°.

---

### Type 6: Equations Using Transformation Formulas

**Goal:** Convert sum to product to solve.

**Solved Example:**

Solve sin 5x + sin 3x = 0 for 0° ≤ x ≤ 360°.

**Solution:**
```
2 sin 4x cos x = 0
sin 4x = 0 → 4x = 0°, 180°, 360°, 540°, 720°
           x = 0°, 45°, 90°, 135°, 180°
cos x = 0 → x = 90°, 270°
Answer: x = 0°, 45°, 90°, 135°, 180°, 270°
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

26. 🟡 Solve cos 5x + cos x = 0 for 0° ≤ x ≤ 360°.
27. 🟡 Solve sin 7x − sin x = 0 for 0° ≤ x ≤ 360°.
28. 🟡 Solve cos 4x + cos 2x = 0 for 0° ≤ x ≤ 180°.
29. 🔴 Solve sin x + sin 3x + sin 5x = 0 for 0° ≤ x ≤ 180°.
30. 🔴 ⭐ Solve cos 2x + cos 4x + cos 6x = 0 for 0° ≤ x ≤ 180°.

---

### Type 7: Equations with Multiple Angles

**Goal:** Solve equations like sin 2θ = cos 3θ.

**Solved Example:**

Solve sin 2x = cos 3x for 0° ≤ x ≤ 360°.

**Solution:**
```
sin 2x = cos 3x
sin 2x = sin(90° − 3x)

Either: 2x = 90° − 3x + 360°n
        5x = 90° + 360°n
        x = 18° + 72°n
        x = 18°, 90°, 162°, 234°, 306°

Or: 2x = 180° − (90° − 3x) + 360°n
    2x = 90° + 3x + 360°n
    −x = 90° + 360°n
    x = −90° − 360°n
    x = 270° (for n = −1)

Answer: x = 18°, 90°, 162°, 234°, 270°, 306°
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

31. 🔴 Solve sin 2x = sin x for 0° ≤ x ≤ 360°.
32. 🔴 Solve cos 3x = cos 2x for 0° ≤ x ≤ 360°.
33. 🔴 Solve tan 3x = tan x for 0° ≤ x ≤ 180°.
34. 🔴 ⭐ Solve sin 2x + cos x = 0 for 0° ≤ x ≤ 360°.
35. 🔴 Solve cos 2x + sin x = 0 for 0° ≤ x ≤ 360°.

---

### Type 8: Equations Involving sec, cosec, cot

**Goal:** Solve equations with reciprocal trig functions.

**Solved Example:**

Solve sec θ = 2 for 0° ≤ θ ≤ 360°.

**Solution:**
```
sec θ = 2 → cos θ = 1/2
θ = 60°, 300°
```
🟢 Easy

---

**Practice Problems:**

36. 🟡 Solve cosec θ = 2 for 0° ≤ θ ≤ 360°.
37. 🟡 Solve cot θ = √3 for 0° ≤ θ ≤ 360°.
38. 🟡 Solve sec θ + tan θ = 2 for 0° ≤ θ ≤ 360°.
39. 🔴 ⭐ Solve sec²θ + tan²θ = 5 for 0° ≤ θ ≤ 360°.
40. 🔴 Solve cosec²θ + cot²θ = 2 for 0° ≤ θ ≤ 360°.

---

## Stage 4: Type Mixer

1. 🟡 Solve 4 sin²θ = 3 for θ ∈ [0, 2π].

2. 🟡 Solve cos x + cos 3x = 0 for x ∈ [0, π].

3. 🔴 ⭐ Solve 2 sin²x − 3 sin x + 1 = 0 for x ∈ [0, 2π].

4. 🔴 Solve sin 2x = cos x for x ∈ [0, 2π].

5. 🔴 Solve tan θ + sec θ = √3 for θ ∈ [0, 2π].

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Solve sin θ = −1/2 for 0° ≤ θ ≤ 360°. **(2 marks)**

**Solution:**
```
sin θ = −1/2
θ = 210°, 330°
```

---

**Q2.** 🟡 Solve 2 cos²θ − 1 = 0 for 0° ≤ θ ≤ 360°. **(2 marks)**

**Solution:**
```
2 cos²θ = 1
cos²θ = 1/2
cos θ = ±1/√2
θ = 45°, 135°, 225°, 315°
```

---

**Q3.** 🟡 Solve 2 sin²x + sin x − 1 = 0 for 0° ≤ x ≤ 360°. **(3 marks)**

**Solution:**
```
Let t = sin x → 2t² + t − 1 = 0
(2t − 1)(t + 1) = 0
t = 1/2 or t = −1

sin x = 1/2 → x = 30°, 150°
sin x = −1 → x = 270°
Answer: 30°, 150°, 270°
```

---

**Q4.** 🔴 Solve sin 2x + sin 4x = 0 for 0° ≤ x ≤ 360°. **(3 marks)**

**Solution:**
```
2 sin 3x cos x = 0
sin 3x = 0 → 3x = 0°, 180°, 360°, 540°, 720°, 900°, 1080°
            x = 0°, 60°, 120°, 180°, 240°, 300°, 360°
cos x = 0 → x = 90°, 270°
Answer: 0°, 60°, 90°, 120°, 180°, 240°, 270°, 300°, 360°
```

---

## Stage 6: JEE Mains Arena

**Q1.** The general solution of sin θ = sin α is:
(a) θ = nπ + α
(b) θ = nπ + (−1)ⁿα
(c) θ = 2nπ ± α
(d) θ = nπ ± α

<details>
<summary>Solution</summary>
General solution of sin θ = sin α: θ = nπ + (−1)ⁿα
Answer: (b) 🟢
</details>

---

**Q2.** The number of solutions of sin x = x/10 in [0, 2π] is:
(a) 1
(b) 2
(c) 3
(d) 4

<details>
<summary>Solution</summary>
Graphically, sin x and x/10 intersect at x = 0 and at one positive solution before x = π, and one between π and 2π.
Answer: (c) 🔴 ⭐
</details>

---

**Q3.** The general solution of tan θ = 1 is:
(a) θ = nπ + π/6
(b) θ = nπ + π/4
(c) θ = 2nπ + π/4
(d) θ = nπ ± π/4

<details>
<summary>Solution</summary>
tan θ = 1 → θ = nπ + π/4
Answer: (b) 🟢
</details>

---

**Q4.** If sin θ + cos θ = 1, then θ (general solution) is:
(a) θ = 2nπ
(b) θ = 2nπ + π/2
(c) Both (a) and (b)
(d) θ = nπ + (−1)ⁿπ/4

<details>
<summary>Solution</summary>
sin θ + cos θ = 1 → √2 sin(θ + π/4) = 1 → sin(θ + π/4) = 1/√2
θ + π/4 = nπ + (−1)ⁿ(π/4)
When n is even: θ + π/4 = 2mπ + π/4 → θ = 2mπ
When n is odd: θ + π/4 = (2m+1)π − π/4 → θ = 2mπ + π/2
Answer: (c) 🔴 ⭐
</details>

---

**Q5.** The equation 2 sin²θ − 5 sin θ + 2 = 0 has:
(a) No real solution
(b) One solution in [0, π]
(c) Two solutions in [0, 2π]
(d) Four solutions in [0, 2π]

<details>
<summary>Solution</summary>
2 sin²θ − 5 sin θ + 2 = 0
(2 sin θ − 1)(sin θ − 2) = 0
sin θ = 1/2 or sin θ = 2 (impossible)
sin θ = 1/2 → θ = π/6, 5π/6
Answer: (c) 🟡
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin θ = 1 has general solution θ = (4n+1)π/2.
**Reason (R):** sin θ = 1 only when θ = π/2, 5π/2, ...

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** The equation sin θ = 2 has no real solution.
**Reason (R):** Range of sin θ is [−1, 1].

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The equation cos²θ = 1/4 has 4 solutions in [0, 2π].
**Reason (R):** cos θ = ±1/2 gives four solutions in [0, 2π].

<details>
<summary>Solution</summary>
A is true and R correctly counts them: 60°, 120°, 240°, 300°.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The equation sec θ = 1/2 has no real solution.
**Reason (R):** sec θ = 1/cos θ ≥ 1 or ≤ −1.

<details>
<summary>Solution</summary>
A is true: sec θ = 1/2 → cos θ = 2, impossible.
R is true: sec θ ∈ (−∞, −1] ∪ [1, ∞).
R explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The general solution of sin θ = 0 is:
   (a) θ = nπ   (b) θ = (2n+1)π/2   (c) θ = 2nπ   (d) θ = nπ ± π/2

2. 🟢 The general solution of cos θ = 0 is:
   (a) θ = nπ   (b) θ = (2n+1)π/2   (c) θ = 2nπ   (d) θ = nπ + (−1)ⁿπ/2

3. 🟢 The general solution of tan θ = 0 is:
   (a) θ = nπ   (b) θ = (2n+1)π/2   (c) θ = 2nπ   (d) θ = nπ + π/2

4. 🟡 The principal solutions of sin θ = 1/2 are:
   (a) 30°, 150°   (b) 30°, 210°   (c) 30°, 330°   (d) 150°, 210°

5. 🟡 The principal solutions of cos θ = −1/2 are:
   (a) 120°, 240°   (b) 60°, 300°   (c) 120°, 300°   (d) 60°, 120°

6. 🟡 Number of solutions of sin θ = 1/2 in [0, 2π]:
   (a) 1   (b) 2   (c) 3   (d) 4

7. 🟡 Number of solutions of tan θ = 2 in [0, 2π]:
   (a) 1   (b) 2   (c) 3   (d) 4

8. 🟡 2 sin²θ − 3 sin θ + 1 = 0 has in [0, 2π]:
   (a) 1 solution   (b) 2 solutions   (c) 3 solutions   (d) 4 solutions

9. 🟡 sin θ = cos θ → general solution:
   (a) θ = nπ + π/4   (b) θ = 2nπ + π/4   (c) θ = nπ ± π/4   (d) θ = nπ + π/2

10. 🟡 cos²θ = 1 has solutions in [0, 2π]:
    (a) θ = 0   (b) θ = 0, π   (c) θ = 0, 2π   (d) θ = 0, π, 2π

11. 🟡 sin 2x = sin x →general solution:
    (a) x = nπ   (b) x = 2nπ ± π/3   (c) x = nπ, x = 2nπ ± π/3   (d) x = nπ, x = 2nπ ± π/6

12. 🟡 cos 2x = cos x has in [0, 2π]:
    (a) 2 solutions   (b) 3 solutions   (c) 4 solutions   (d) 5 solutions

13. 🟡 tan 2x = tan x → in [0, π]:
    (a) x = 0   (b) x = 0, π   (c) x = π/2   (d) No solution

14. 🟡 sin x + sin 3x = 0 → number of solutions in [0, π]:
    (a) 2   (b) 3   (c) 4   (d) 5

15. 🟡 The equation 2 sin²θ + 5 cos θ = 4 → general solution:
    (a) θ = 2nπ ± π/3   (b) θ = 2nπ ± π/6   (c) θ = nπ + (−1)ⁿπ/6   (d) θ = nπ ± π/3

16. 🟡 Number of solutions of sin x = cos x in [0, 2π]:
    (a) 1   (b) 2   (c) 3   (d) 4

17. 🟡 General solution of sin θ = sin α is:
    (a) θ = 2nπ ± α   (b) θ = nπ + (−1)ⁿα   (c) θ = nπ + α   (d) θ = nπ ± α

18. 🟡 General solution of cos θ = cos α is:
    (a) θ = nπ + (−1)ⁿα   (b) θ = 2nπ ± α   (c) θ = nπ + α   (d) θ = nπ ± α

19. 🟡 The number of solutions of sin²θ = 1/4 in [0, 2π] is:
    (a) 2   (b) 3   (c) 4   (d) 5

20. 🟡 If sin θ + cos ec θ = 2, then θ =
    (a) 2nπ ± π/3   (b) nπ + (−1)ⁿπ/6   (c) 2nπ + π/2   (d) nπ + (−1)ⁿπ/2

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | c | 16 | b |
| 2 | b | 7 | b | 12 | c | 17 | b |
| 3 | a | 8 | c | 13 | b | 18 | b |
| 4 | a | 9 | a | 14 | b | 19 | c |
| 5 | a | 10 | d | 15 | a | 20 | c |

</details>
