# Chapter 9: Compound Angles

---

## Stage 1: The Core Idea

### Breaking Angles Apart

What is sin(60° + 30°)?<br> Is it sin 60° + sin 30°?<br> Let's test:

```
sin(60° + 30°) = sin 90° = 1
sin 60° + sin 30° = √3/2 + 1/2 ≈ 0.866 + 0.5 = 1.366 ≠ 1
```

So sin(A + B) ≠ sin A + sin B. The relationship is more subtle.

**Compound angle formulas** tell you how to expand sin(A±B), cos(A±B), and tan(A±B). They are the most powerful tools in JEE trigonometry — almost every advanced problem uses them somewhere.

---

## Stage 2: The Formula Lab

### The Core Formulas

```
sin(A + B) = sin A cos B + cos A sin B
sin(A − B) = sin A cos B − cos A sin B

cos(A + B) = cos A cos B − sin A sin B
cos(A − B) = cos A cos B + sin A sin B

tan(A + B) = (tan A + tan B)/(1 − tan A tan B)
tan(A − B) = (tan A − tan B)/(1 + tan A tan B)
```

**Memory trick:** "Some People Can't Have Correct Trig Knowledge"
- **S**in(A+B) = **S**in A **C**os B + **C**os A **S**in B (same sign)
- **C**os(A+B) = **C**os A **C**os B − **S**in A **S**in B (opposite sign)

**Trap to avoid:** The sign in cos(A+B) is MINUS, not plus. This is the most common mistake.

### Derived Formulas

```
cot(A + B) = (cot A cot B − 1)/(cot B + cot A)
cot(A − B) = (cot A cot B + 1)/(cot B − cot A)
```

---

## Stage 3: Type-wise Mastery

### Type 1: Direct Evaluation Using Compound Angles

**Goal:** Find exact values of trig functions of angles like 15°, 75° using known values.

**Solved Example:**

Find sin 75°.

**Solution:**
```
sin 75° = sin(45° + 30°)
= sin 45° cos 30° + cos 45° sin 30°
= (1/√2)(√3/2) + (1/√2)(1/2)
= (√3 + 1)/(2√2)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Find cos 15° using compound angles.
2. 🟡 Find tan 75°.
3. 🟡 Find sin 105°.
4. 🟡 Find cos 105°.
5. 🔴 Find tan 165°.

---

### Type 2: Proving Identities with Compound Angles

**Goal:** Prove trigonometric identities using compound angle expansions.

**Solved Example:**

Prove that sin(45° + A) sin(45° − A) = 1/2 cos 2A.

**Solution:**
```
LHS = (sin 45° cos A + cos 45° sin A)(sin 45° cos A − cos 45° sin A)
    = (cos A/√2 + sin A/√2)(cos A/√2 − sin A/√2)
    = (1/2)(cos²A − sin²A)
    = (1/2) cos 2A = RHS ✓
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 Prove cos(60° + A) = cos 60° cos A − sin 60° sin A.

7. 🟡 Prove sin(A + B) sin(A − B) = sin²A − sin²B.

8. 🟡 Prove cos(A + B) cos(A − B) = cos²A − sin²B.

9. 🔴 Prove tan A + tan B = sin(A + B)/(cos A cos B).

10. 🔴 ⭐ Prove that tan(45° + A) = (1 + tan A)/(1 − tan A).

---

### Type 3: Finding Values Given Other Ratios

**Goal:** Given sin A and cos B (with quadrants), find sin(A+B), cos(A−B), etc.

**Solved Example:**

If sin A = 3/5 (A acute) and cos B = 5/13 (B acute), find sin(A + B).

**Solution:**
```
sin A = 3/5 → cos A = 4/5
cos B = 5/13 → sin B = 12/13

sin(A + B) = sin A cos B + cos A sin B
= (3/5)(5/13) + (4/5)(12/13)
= 15/65 + 48/65
= 63/65
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 If sin A = 4/5, cos B = 12/13 (both acute), find cos(A + B).

12. 🟡 If tan A = 1/2, tan B = 1/3 (both acute), find tan(A + B).

13. 🟡 If sin A = 5/13 (QII) and cos B = −4/5 (QII), find sin(A − B).

14. 🔴 If sin A = 3/5, cos B = 15/17 (both acute), find tan(A + B).

15. 🔴 ⭐ If cos A = −3/5 (QIII) and sin B = 5/13 (QII), find cos(A − B).

---

### Type 4: Solving Equations with Compound Angles

**Goal:** Solve trig equations by applying compound angle formulas.

**Solved Example:**

Solve sin 3x cos 2x + cos 3x sin 2x = 1/2.

**Solution:**
```
LHS = sin(3x + 2x) = sin 5x
sin 5x = 1/2
5x = π/6 or 5π/6 (plus general solutions)
x = π/30 or π/6 (plus n×2π/5)
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Solve cos 3x cos x − sin 3x sin x = 1/2.

17. 🟡 Solve (tan x + tan 2x)/(1 − tan x tan 2x) = 1.

18. 🟡 Solve sin(x + 30°) = cos x.

19. 🔴 Solve sin 2x cos x + cos 2x sin x = 0.

20. 🔴 ⭐ Solve cos(x + π/4) − cos(x − π/4) = √2 sin x. (This is an identity — prove it first.)

---

### Type 5: Sum and Difference in Reverse

**Goal:** Write expressions like cos 3x cos 2x + sin 3x sin 2x as a single trig function.

**Solved Example:**

Simplify cos 3x cos 2x + sin 3x sin 2x.

**Solution:**
```
= cos(3x − 2x) = cos x
```
🟢 Easy

---

**Practice Problems:**

21. 🟢 Simplify sin 5x cos x − cos 5x sin x.

22. 🟢 Simplify cos 4x cos x + sin 4x sin x.

23. 🟡 Write sin 75° cos 15° + cos 75° sin 15° as a single trig function.

24. 🟡 Simplify (tan 3x − tan x)/(1 + tan 3x tan x).

25. 🔴 Simplify cos(A + B) cos B + sin(A + B) sin B.

---

### Type 6: Conditional Identities

**Goal:** Prove identities involving conditions like A + B + C = π.

**Solved Example:**

If A + B = 45°, prove that (1 + tan A)(1 + tan B) = 2.

**Solution:**
```
tan(A + B) = tan 45° = 1
(tan A + tan B)/(1 − tan A tan B) = 1
tan A + tan B = 1 − tan A tan B
tan A + tan B + tan A tan B = 1
1 + tan A + tan B + tan A tan B = 2
(1 + tan A)(1 + tan B) = 2 ✓
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

26. 🔴 If A + B = 45°, prove that (1 − tan A)(1 − tan B) = 2.

27. 🔴 If A + B + C = π, prove that tan A + tan B + tan C = tan A tan B tan C.

28. 🔴 If A + B = π/4, prove that (cot A − 1)(cot B − 1) = 2.

29. 🔴 ⭐ If sin(A + B) = 1 and sin(A − B) = 1/2, find A and B.

30. 🔴 If x + y = 3 − cos 4θ and x − y = 4 sin 2θ, show that √x + √y = 2.

---

### Type 7: Eliminating θ with Compound Angles

**Goal:** Eliminate θ from given equations.

**Solved Example:**

Eliminate θ: x = a sin(θ + α), y = a sin(θ + β).

**Solution:**
```
x/a = sin θ cos α + cos θ sin α
y/a = sin θ cos β + cos θ sin β

Solve for sin θ and cos θ:
sin θ = (x sin β − y sin α)/(a sin(β − α))
cos θ = (x cos β − y cos α)/(a sin(β − α))

Then sin²θ + cos²θ = 1 gives:
(x² + y² − 2xy cos(β − α)) = a² sin²(β − α)
```
🔴 Hard

---

**Practice Problems:**

31. 🔴 Eliminate θ: x = a cos(θ + α), y = b cos(θ + β).

32. 🔴 Eliminate θ: u = tan(θ + α), v = tan(θ + β).

33. 🔴 ⭐ If sin θ + cos θ = √2 cos α, prove that cos θ − sin θ = √2 sin α.

34. 🔴 If tan(θ + α) = n tan(θ − α), prove that (n + 1) sin 2α = (n − 1) sin 2θ.

35. 🔴 If sin(θ + α) = a and sin(θ + β) = b, prove that cos(α − β) = ab ± √((1 − a²)(1 − b²)).

---

### Type 8: Expressing Sum as Product (Preview)

**Goal:** Use compound angles to derive sum-to-product formulas.

**Solved Example:**

Express sin(A + B) + sin(A − B) as a product.

**Solution:**
```
sin(A + B) + sin(A − B) = 2 sin A cos B
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Express sin(A + B) − sin(A − B) as a product.

37. 🟡 Express cos(A + B) + cos(A − B) as a product.

38. 🟡 Express cos(A − B) − cos(A + B) as a product.

39. 🔴 Find the value of sin 75° − sin 15°.

40. 🔴 ⭐ Show that (sin 7x + sin 5x)/(cos 7x + cos 5x) = tan 6x.

---

## Stage 4: Type Mixer

1. 🟡 If tan A = 2 and tan B = 3, find tan(A + B). What can you conclude about A + B?<br>

2. 🟡 Prove that cos(60° + A) + sin(30° + A) = cos A.

3. 🔴 ⭐ If sin A = 3/5 and cos B = 12/13, where A and B are acute, find sin(A − B) and cos(A + B).

4. 🔴 If A + B = 45°, prove that (cot A − 1)(cot B − 1) = 2.

5. 🔴 Show that sin(45° + A) cos(45° − B) + cos(45° + A) sin(45° − B) = cos(A − B).

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find sin 15° using compound angle formula. **(2 marks)**

**Solution:**
```
sin 15° = sin(45° − 30°)
= sin 45° cos 30° − cos 45° sin 30°
= (1/√2)(√3/2) − (1/√2)(1/2)
= (√3 − 1)/(2√2)
```

---

**Q2.** 🟡 If tan A = 1/2, tan B = 1/3, find tan(A + B) and deduce A + B. **(3 marks)**

**Solution:**
```
tan(A + B) = (1/2 + 1/3)/(1 − 1/6) = (5/6)/(5/6) = 1
A + B = 45°
```

---

**Q3.** 🟡 Prove that cos(A + B) cos B + sin(A + B) sin B = cos A. **(2 marks)**

**Solution:**
```
LHS = cos((A + B) − B) = cos A = RHS ✓
```

---

**Q4.** 🔴 If sin(A + B) = 1 and sin(A − B) = 1/2, find A and B (0 < A, B < 90°). **(3 marks)**

**Solution:**
```
A + B = 90°
A − B = 30°
Solving: A = 60°, B = 30°
```

---

## Stage 6: JEE Mains Arena

**Q1.** If sin A = 3/5, cos B = 5/13 (both acute), sin(A + B) equals:
(a) 56/65
(b) 63/65
(c) 16/65
(d) 33/65

<details>
<summary>Solution</summary>
cos A = 4/5, sin B = 12/13
sin(A+B) = (3/5)(5/13) + (4/5)(12/13) = 15/65 + 48/65 = 63/65
Answer: (b) 🟡 ⭐
</details>

---

**Q2.** The value of cos 15° − sin 15° is:
(a) 1/√2
(b) √2
(c) 1/2
(d) √3/2

<details>
<summary>Solution</summary>
cos 15° − sin 15° = √2 cos(15° + 45°) = √2 cos 60° = √2(1/2) = 1/√2
Answer: (a) 🔴 ⭐
</details>

---

**Q3.** If A + B = 45°, then (1 + tan A)(1 + tan B) equals:
(a) 0
(b) 1
(c) 2
(d) 3

<details>
<summary>Solution</summary>
tan(A+B) = 1 → (tan A + tan B)/(1 − tan A tan B) = 1
tan A + tan B = 1 − tan A tan B
(1 + tan A)(1 + tan B) = 1 + tan A + tan B + tan A tan B = 1 + 1 = 2
Answer: (c) 🔴 ⭐
</details>

---

**Q4.** If tan A = 2 and tan B = 3, then A + B equals:
(a) 45°
(b) 135°
(c) 225°
(d) 315°

<details>
<summary>Solution</summary>
tan(A+B) = (2+3)/(1-6) = 5/(-5) = -1
Since tan A > 0 and tan B > 0, both A,B ∈ (0,90°)
So A+B ∈ (0,180°) and tan(A+B) = -1 → A+B = 135°
Answer: (b) 🟡
</details>

---

**Q5.** The expression (sin 7x + sin 5x)/(cos 7x + cos 5x) simplifies to:
(a) tan x
(b) tan 6x
(c) tan 12x
(d) cot 6x

<details>
<summary>Solution</summary>
= (2 sin 6x cos x)/(2 cos 6x cos x) = tan 6x
Answer: (b) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin(A + B) = sin A cos B + cos A sin B.
**Reason (R):** sin(A + B) = sin A + sin B is incorrect.

<details>
<summary>Solution</summary>
A is true. R is true but doesn't explain the formula — it just says the wrong formula is false.
Answer: (b)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** cos(A + B) = cos A cos B − sin A sin B.
**Reason (R):** cos(A + B) = cos A cos B + sin A sin B.

<details>
<summary>Solution</summary>
A is true. R is false (it's the formula for cos(A−B)).
Answer: (c)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** tan(π/4 + A) = (1 + tan A)/(1 − tan A).
**Reason (R):** tan(π/4) = 1.

<details>
<summary>Solution</summary>
Both true, R explains A (it's the tan compound formula with tan π/4 = 1).
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** sin(α + β) = 1 and sin(α − β) = 2/√3 is impossible.
**Reason (R):** Range of sine function is [−1, 1].

<details>
<summary>Solution</summary>
A is true: sin(α − β) = 2/√3 ≈ 1.155 > 1, impossible.
R is true: range of sin is [−1, 1].
R explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin(A + B) equals:
   (a) sin A + sin B   (b) sin A cos B + cos A sin B   (c) sin A cos B − cos A sin B   (d) cos A cos B − sin A sin B

2. 🟢 cos(A − B) equals:
   (a) cos A cos B + sin A sin B   (b) cos A cos B − sin A sin B   (c) sin A cos B + cos A sin B   (d) sin A cos B − cos A sin B

3. 🟡 sin 15° equals:
   (a) (√3 + 1)/(2√2)   (b) (√3 − 1)/(2√2)   (c) (√3 − 1)/2   (d) (√3 + 1)/2

4. 🟡 cos 75° equals:
   (a) (√3 − 1)/(2√2)   (b) (√3 + 1)/(2√2)   (c) (√3 − 1)/2   (d) (√3 + 1)/2

5. 🟡 tan(45° + A) equals:
   (a) (1 − tan A)/(1 + tan A)   (b) (1 + tan A)/(1 − tan A)   (c) (tan A − 1)/(tan A + 1)   (d) 1

6. 🟡 If sin A = 4/5, cos A = 3/5, then sin 2A = ?<br>
   (a) 24/25   (b) 12/25   (c) 7/25   (d) 9/25

7. 🟡 cos(60° + A) + sin(30° + A) equals:
   (a) sin A   (b) cos A   (c) 0   (d) 1

8. 🟡 If A + B = 45° and tan A = 1/2, then tan B = ?<br>
   (a) 1/3   (b) 2/3   (c) 1/4   (d) 2/5

9. 🟡 sin(π/4 + x) + sin(π/4 − x) equals:
   (a) √2 sin x   (b) √2 cos x   (c) 2 sin x   (d) 2 cos x

10. 🟡 If sin(A + B) = 1/2 and sin(A − B) = 0, then A = ?<br>
    (a) 15°   (b) 30°   (c) 45°   (d) 60°

11. 🟡 sin 105° equals:
    (a) (√3 + 1)/(2√2)   (b) (√3 − 1)/(2√2)   (c) √3/2   (d) 1/2

12. 🟡 cos(90° + A) equals:
    (a) sin A   (b) −sin A   (c) cos A   (d) −cos A

13. 🟡 sin(π/3 + θ) − sin(π/3 − θ) equals:
    (a) sin θ   (b) cos θ   (c) √3 sin θ   (d) √3 cos θ

14. 🟡 If tan A = 1/3 and tan B = 1/2, A + B = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 90°

15. 🟡 cos(α + β) cos(α − β) equals:
    (a) cos²α − sin²β   (b) cos²α + sin²β   (c) sin²α − cos²β   (d) cos²α − cos²β

16. 🟡 tan 75° equals:
    (a) 2 + √3   (b) 2 − √3   (c) √3 + 1   (d) √3 − 1

17. 🟡 sin 75° − sin 15° equals:
    (a) 1/√2   (b) √3/2   (c) 1/2   (d) √2

18. 🟡 cos 15° − sin 15° equals:
    (a) 1/√2   (b) √2   (c) 0   (d) −1/√2

19. 🟡 If sin(A + B) = sin A cos B + cos A sin B, then sin 2A = ?<br>
    (a) sin²A   (b) 2 sin A cos A   (c) cos²A   (d) 1

20. 🟡 The expression (tan 3x − tan x)/(1 + tan 3x tan x) equals:
    (a) tan 2x   (b) tan 4x   (c) tan x   (d) tan 3x

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | a | 11 | a | 16 | a |
| 2 | a | 7 | b | 12 | b | 17 | a |
| 3 | b | 8 | a | 13 | a | 18 | a |
| 4 | a | 9 | b | 14 | b | 19 | b |
| 5 | b | 10 | a | 15 | a | 20 | a |

</details>
