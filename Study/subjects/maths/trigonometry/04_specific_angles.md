# Chapter 4: Trigonometric Ratios of Specific Angles

---

## Stage 1: The Core Idea

### Where Do the Standard Values Come From?<br>

You've memorised: sin 30° = 1/2, sin 45° = 1/√2, sin 60° = √3/2. But where do these come from?<br>

They come from **geometry** — two special triangles:

```
45-45-90 Triangle:
        ┌───┐
        │   │  hypotenuse = √2
    1   │   │
        │   │
        └───┘
           1

Both legs = 1, hypotenuse = √2

30-60-90 Triangle:
        ┌───┐
        │   │  hypotenuse = 2
    √3  │   │
        │   │
        └───┘
           1

Short leg = 1, long leg = √3, hyp = 2
(It's half an equilateral triangle of side 2)
```

From these two triangles, you can derive all six ratios for 30°, 45°, 60°.

The values for 0° and 90° come from thinking about what happens when an angle shrinks to 0 or grows to 90 — the triangle collapses into a line.

---

## Stage 2: The Formula Lab

### The Master Table

| θ | 0° | 30° | 45° | 60° | 90° |
|---|:--:|:---:|:---:|:---:|:---:|
| sin θ | 0 | 1/2 | 1/√2 | √3/2 | 1 |
| cos θ | 1 | √3/2 | 1/√2 | 1/2 | 0 |
| tan θ | 0 | 1/√3 | 1 | √3 | ∞ (undef) |
| cosec θ | ∞ | 2 | √2 | 2/√3 | 1 |
| sec θ | 1 | 2/√3 | √2 | 2 | ∞ |
| cot θ | ∞ | √3 | 1 | 1/√3 | 0 |

### Pattern Memory Trick

Write sin values for 0°, 30°, 45°, 60°, 90°:
```
√0/2, √1/2, √2/2, √3/2, √4/2
= 0, 1/2, 1/√2, √3/2, 1
```

Cos values are sin reversed:
```
√4/2, √3/2, √2/2, √1/2, √0/2
= 1, √3/2, 1/√2, 1/2, 0
```

Tan = sin/cos:
```
0, 1/√3, 1, √3, ∞
```

**Trap to avoid:** tan 90° is NOT defined (division by zero). Sec 90° and cosec 0° are also undefined.

---

## Stage 3: Type-wise Mastery

### Type 1: Direct Value Evaluation

**Goal:** Evaluate expressions using standard angle values.

**Solved Example:**

Find sin 30° cos 60° + cos 30° sin 60°.

**Solution:**
```
= (1/2)(1/2) + (√3/2)(√3/2)
= 1/4 + 3/4
= 1
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Evaluate sin 60° cos 30° + cos 60° sin 30°.

2. 🟢 Evaluate tan 45° + cot 45°.

3. 🟢 Evaluate sin² 45° + cos² 45°.

4. 🟡 Evaluate (sin 30° + cos 60°)/(tan 45°).

5. 🟡 Evaluate sec² 60° − tan² 60°.

---

### Type 2: Verifying Identities with Specific Angles

**Goal:** Substitute standard values to verify trig identities.

**Solved Example:**

Verify that sin² 30° + cos² 30° = 1.

**Solution:**
```
sin²30° + cos²30° = (1/2)² + (√3/2)² = 1/4 + 3/4 = 1 ✓
```
🟢 Easy

---

**Practice Problems:**

6. 🟢 Verify 1 + tan² 45° = sec² 45°.

7. 🟡 Verify sin 60° = 2 sin 30° cos 30°.

8. 🟡 Verify cos 60° = cos² 30° − sin² 30°.

9. 🟡 Verify tan 60° = (2 tan 30°)/(1 − tan² 30°).

10. 🔴 Show that sin(60° + 30°) ≠ sin 60° + sin 30°.

---

### Type 3: Finding Unknown Angles

**Goal:** Given an equation involving standard values, find the unknown angle.

**Solved Example:**

If 2 sin θ = 1, find θ (0° ≤ θ ≤ 90°).

**Solution:**
```
2 sin θ = 1
sin θ = 1/2
From the table, sin 30° = 1/2
∴ θ = 30°
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

11. 🟢 If tan θ = 1, find θ.

12. 🟢 If √3 sec θ = 2, find θ.

13. 🟡 If 2 cos 3θ = 1, find θ.

14. 🟡 If sin(θ + 30°) = √3/2, find θ.

15. 🔴 If tan²θ = 1/3, find θ (0° < θ < 90°).

---

### Type 4: Value of Expressions with Mixed Angles

**Goal:** Evaluate compound expressions involving multiple standard angles.

**Solved Example:**

Find 4 sin² 60° + 3 tan² 30° − 8 sin² 45° cos 45°.

**Solution:**
```
= 4(√3/2)² + 3(1/√3)² − 8(1/√2)²(1/√2)
= 4(3/4) + 3(1/3) − 8(1/2)(1/√2)
= 3 + 1 − 4/√2
= 4 − 2√2
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Evaluate: sin² 30° + sin² 45° + sin² 60°.

17. 🟡 Evaluate: tan² 30° + tan² 45° + tan² 60°.

18. 🟡 Evaluate: cosec² 30° − sec² 45° + cot² 60°.

19. 🔴 Evaluate: 4 sin⁴ 30° + 3 cos² 60° − 2 tan⁴ 45°.

20. 🔴 ⭐ Find the value of (sin² 60° + cosec² 30°)/(cos² 45° + sec² 30°).

---

### Type 5: Proving Equations Using Standard Values

**Goal:** Show that an equation holds by substituting standard angle values.

**Solved Example:**

Show that cos 60° = 2 cos² 30° − 1.

**Solution:**
```
RHS = 2(√3/2)² − 1
    = 2(3/4) − 1
    = 3/2 − 1
    = 1/2 = cos 60° = LHS ✓
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 Prove sin 30° cos 60° + cos 30° sin 60° = 1.

22. 🟡 Prove tan 45° + cot 45° = 2.

23. 🟡 Prove sin 60° = 2 tan 30°/(1 + tan² 30°).

24. 🔴 Prove that sin² 60° + sin² 30° = sin² 45° + sin² 45°.

25. 🔴 ⭐ If A = 30°, verify that sin 2A = 2 sin A cos A.

---

### Type 6: Comparing Values

**Goal:** Determine which trig value is larger/smaller among standard angles.

**Solved Example:**

Which is greater: sin 30° or sin 60°?<br>

**Solution:**
```
sin 30° = 1/2 = 0.5
sin 60° = √3/2 ≈ 0.866
∴ sin 60° > sin 30°
```
🟢 Easy

---

**Practice Problems:**

26. 🟢 Which is greater: cos 30° or cos 60°?<br>

27. 🟢 Which is greater: tan 30° or tan 45°?<br>

28. 🟡 Arrange in increasing order: sin 0°, sin 30°, sin 45°, sin 60°, sin 90°.

29. 🟡 Arrange in decreasing order: cos 90°, cos 60°, cos 45°, cos 30°, cos 0°.

30. 🟡 Which is larger: sec 45° or cosec 45°?<br>

---

### Type 7: Finding Values of cosec, sec, cot

**Goal:** Use the standard table for reciprocal ratios.

**Solved Example:**

Find sec 30° + cosec 60°.

**Solution:**
```
sec 30° = 2/√3, cosec 60° = 2/√3
Sum = 2/√3 + 2/√3 = 4/√3
```
🟢 Easy

---

**Practice Problems:**

31. 🟢 Find cot 30° × tan 60°.

32. 🟢 Find cosec 45° × sec 45°.

33. 🟡 Find (cosec 30° + sec 60°)/(cot 45°).

34. 🟡 Find sec² 30° + cosec² 45° − cot² 60°.

35. 🔴 If cot θ = √3, find θ and then find sin θ cos θ + cos² θ.

---

## Stage 4: Type Mixer

1. 🟡 Find the value of tan² 60° + 2 tan² 45° − 3 cot² 30°.

2. 🟡 If 3 tan²θ = 1 and θ is acute, find θ and then find sin²θ + cos²θ.

3. 🔴 ⭐ Evaluate: (sin 30° − sin 90° + 2 cos 0°)/(tan 30° × tan 60°).

4. 🔴 If sin(A + B) = 1 and cos(A − B) = √3/2, find A and B (both acute, A > B).

5. 🔴 Prove that sin 60° cos 30° − cos 60° sin 30° = sin 30°.

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Evaluate: sin 60° cos 30° + cos 60° sin 30°. **(2 marks)**

**Solution:**
```
= (√3/2)(√3/2) + (1/2)(1/2)
= 3/4 + 1/4 = 1
```

---

**Q2.** 🟡 Find the value of x if 2 sin x = √3. **(2 marks)**

**Solution:**
```
2 sin x = √3
sin x = √3/2
∴ x = 60°
```

---

**Q3.** 🟡 Evaluate: 5 cos² 60° + 4 sec² 30° − tan² 45°. **(3 marks)**

**Solution:**
```
= 5(1/2)² + 4(2/√3)² − (1)²
= 5(1/4) + 4(4/3) − 1
= 5/4 + 16/3 − 1
= (15 + 64 − 12)/12
= 67/12
```

---

**Q4.** 🟡 If θ = 30°, verify sin 2θ = 2 sin θ cos θ. **(3 marks)**

**Solution:**
```
LHS: sin 60° = √3/2
RHS: 2 sin 30° cos 30° = 2(1/2)(√3/2) = √3/2
LHS = RHS ✓
```

---

## Stage 6: JEE Mains Arena

**Q1.** The value of (sin 30° + cos 30°)² is:
(a) 1
(b) (2 + √3)/2
(c) (2 − √3)/2
(d) √3

<details>
<summary>Solution</summary>
(sin 30° + cos 30°)² = (1/2 + √3/2)² = ((1+√3)/2)² = (1 + 2√3 + 3)/4 = (4 + 2√3)/4 = (2 + √3)/2
Answer: (b) 🟡
</details>

---

**Q2.** If sin(A − B) = 1/2 and cos(A + B) = 1/2, then A and B are:
(a) 45°, 15°
(b) 30°, 15°
(c) 45°, 30°
(d) 60°, 15°

<details>
<summary>Solution</summary>
sin(A − B) = 1/2 → A − B = 30°
cos(A + B) = 1/2 → A + B = 60°
Solving: A = 45°, B = 15°
Answer: (a) 🟡 ⭐
</details>

---

**Q3.** The value of 4 sin² 60° + 3 tan² 30° − 8 sin 45° cos 45° is:
(a) 3
(b) 2
(c) 1
(d) 0

<details>
<summary>Solution</summary>
= 4(3/4) + 3(1/3) − 8(1/√2)(1/√2)
= 3 + 1 − 8(1/2)
= 4 − 4 = 0
Answer: (d) 🟡
</details>

---

**Q4.** If θ = 30°, then (1 + tan θ)/(1 − tan θ) equals:
(a) 2 + √3
(b) 2 − √3
(c) 1
(d) √3

<details>
<summary>Solution</summary>
tan 30° = 1/√3
(1 + 1/√3)/(1 − 1/√3) = ((√3 + 1)/√3)/((√3 − 1)/√3) = (√3 + 1)/(√3 − 1)
Rationalise: (√3 + 1)²/(3 − 1) = (3 + 2√3 + 1)/2 = (4 + 2√3)/2 = 2 + √3
Answer: (a) 🔴 ⭐
</details>

---

**Q5.** The value of sin² 5° + sin² 10° + … + sin² 85° + sin² 90° is:
(a) 8
(b) 9.5
(c) 8.5
(d) 9

<details>
<summary>Solution</summary>
Pairs: sin² 5° + sin² 85° = sin² 5° + cos² 5° = 1
Similarly up to sin² 40° + sin² 50° = 1
That gives 8 pairs (5° to 40° with 85° to 50°)
+ sin² 45° = 1/2 + sin² 90° = 1
Total = 8 + 0.5 + 1 = 9.5
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin 45° = cos 45°.
**Reason (R):** sin(90° − θ) = cos θ, and 45° = 90° − 45°.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** tan 60° = √3.
**Reason (R):** tan 60° = sin 60°/cos 60° = (√3/2)/(1/2) = √3.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sec 90° is defined.
**Reason (R):** sec θ = 1/cos θ and cos 90° = 0.

<details>
<summary>Solution</summary>
A is false: sec 90° = 1/0 which is undefined.
R is true: cos 90° = 0.
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The value of sin θ increases as θ increases from 0° to 90°.
**Reason (R):** cos θ decreases as θ increases from 0° to 90°.

<details>
<summary>Solution</summary>
A is true: sin 0°=0, sin 30°=0.5, sin 60°=0.866, sin 90°=1.
R is also true: cos 0°=1, cos 30°=0.866, cos 60°=0.5, cos 90°=0.
But R does not explain A — they are independent properties.
Answer: (b)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin 30° equals:
   (a) 1/2   (b) √3/2   (c) 1/√2   (d) 1

2. 🟢 cos 45° equals:
   (a) 1/2   (b) √3/2   (c) 1/√2   (d) 0

3. 🟢 tan 60° equals:
   (a) 1/√3   (b) √3   (c) 1   (d) 0

4. 🟡 sin 60° cos 30° + cos 60° sin 30° equals:
   (a) 1/2   (b) 1   (c) √3/2   (d) 0

5. 🟢 The value of sin 0° is:
   (a) 0   (b) 1   (c) −1   (d) 1/2

6. 🟢 cos 90° equals:
   (a) 1   (b) 0   (c) −1   (d) 1/2

7. 🟡 If sin θ = 1/2, θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

8. 🟡 If √3 tan θ = 1, θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

9. 🟢 sec 45° equals:
   (a) 1   (b) √2   (c) 2/√3   (d) 2

10. 🟡 sin² 30° + sin² 60° equals:
    (a) 0   (b) 1/2   (c) 1   (d) 3/2

11. 🟡 tan 45° + cot 45° equals:
    (a) 1   (b) 2   (c) 0   (d) 3

12. 🟡 cosec 30° equals:
    (a) 2   (b) 2/√3   (c) √2   (d) 1

13. 🟢 Which is true?<br>
    (a) sin 30° < sin 45°   (b) sin 30° > sin 45°   (c) sin 30° = sin 45°   (d) None

14. 🟡 If sin 2θ = √3/2, θ = ?<br>
    (a) 15°   (b) 30°   (c) 45°   (d) 60°

15. 🟡 The value of 2 tan 45° + cos 60° − sin 30° is:
    (a) 1   (b) 2   (c) 0   (d) 3

16. 🟡 sin 0° + cos 0° + tan 0° equals:
    (a) 0   (b) 1   (c) 2   (d) 3

17. 🟡 sec 30° + cosec 60° equals:
    (a) 4/√3   (b) 2/√3   (c) √3   (d) 2

18. 🟡 cot 45° equals:
    (a) 0   (b) 1   (c) √3   (d) 1/√3

19. 🟡 cos 60° × sec 60° equals:
    (a) 0   (b) 1/2   (c) 1   (d) 2

20. 🟡 If sin(A + B) = 1 and sin(A − B) = 1/2, (A>B), then A = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 75°

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | b | 16 | b |
| 2 | c | 7 | a | 12 | a | 17 | a |
| 3 | b | 8 | a | 13 | a | 18 | b |
| 4 | b | 9 | b | 14 | b | 19 | c |
| 5 | a | 10 | c | 15 | b | 20 | c |

</details>
