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
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2} \]
\[ \cos 60^\circ = \frac{1}{2}, \quad \sin 30^\circ = \frac{1}{2} \]

Substitute these into the expression:
\[ \sin 60^\circ \cos 30^\circ + \cos 60^\circ \sin 30^\circ = \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) \]
\[ = \frac{3}{4} + \frac{1}{4} = 1 \]

</details>

2. 🟢 Evaluate tan 45° + cot 45°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 45^\circ = 1, \quad \cot 45^\circ = 1 \]

Evaluate the sum:
\[ \tan 45^\circ + \cot 45^\circ = 1 + 1 = 2 \]

</details>

3. 🟢 Evaluate sin² 45° + cos² 45°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 45^\circ = \frac{1}{\sqrt{2}}, \quad \cos 45^\circ = \frac{1}{\sqrt{2}} \]

Calculate the sum of their squares:
\[ \sin^2 45^\circ + \cos^2 45^\circ = \left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 \]
\[ = \frac{1}{2} + \frac{1}{2} = 1 \]

</details>

4. 🟡 Evaluate (sin 30° + cos 60°)/(tan 45°).
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \cos 60^\circ = \frac{1}{2}, \quad \tan 45^\circ = 1 \]

Evaluate the expression:
\[ \frac{\sin 30^\circ + \cos 60^\circ}{\tan 45^\circ} = \frac{\frac{1}{2} + \frac{1}{2}}{1} = \frac{1}{1} = 1 \]

</details>

5. 🟡 Evaluate sec² 60° − tan² 60°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sec 60^\circ = 2, \quad \tan 60^\circ = \sqrt{3} \]

Evaluate the expression:
\[ \sec^2 60^\circ - \tan^2 60^\circ = (2)^2 - (\sqrt{3})^2 = 4 - 3 = 1 \]

</details>

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
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 45^\circ = 1, \quad \sec 45^\circ = \sqrt{2} \]

Evaluate both sides:
- **Left Hand Side (LHS):**
  \[ LHS = 1 + \tan^2 45^\circ = 1 + (1)^2 = 1 + 1 = 2 \]
- **Right Hand Side (RHS):**
  \[ RHS = \sec^2 45^\circ = (\sqrt{2})^2 = 2 \]

Since \( LHS = RHS = 2 \), the identity is verified.

</details>

7. 🟡 Verify sin 60° = 2 sin 30° cos 30°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \sin 30^\circ = \frac{1}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2} \]

Evaluate both sides:
- **Left Hand Side (LHS):**
  \[ LHS = \sin 60^\circ = \frac{\sqrt{3}}{2} \]
- **Right Hand Side (RHS):**
  \[ RHS = 2 \sin 30^\circ \cos 30^\circ = 2 \left(\frac{1}{2}\right) \left(\frac{\sqrt{3}}{2}\right) = \frac{\sqrt{3}}{2} \]

Since \( LHS = RHS \), the identity is verified.

</details>

8. 🟡 Verify cos 60° = cos² 30° − sin² 30°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \cos 60^\circ = \frac{1}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \sin 30^\circ = \frac{1}{2} \]

Evaluate both sides:
- **Left Hand Side (LHS):**
  \[ LHS = \cos 60^\circ = \frac{1}{2} \]
- **Right Hand Side (RHS):**
  \[ RHS = \cos^2 30^\circ - \sin^2 30^\circ = \left(\frac{\sqrt{3}}{2}\right)^2 - \left(\frac{1}{2}\right)^2 = \frac{3}{4} - \frac{1}{4} = \frac{2}{4} = \frac{1}{2} \]

Since \( LHS = RHS \), the identity is verified.

</details>

9. 🟡 Verify tan 60° = (2 tan 30°)/(1 − tan² 30°).
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 60^\circ = \sqrt{3}, \quad \tan 30^\circ = \frac{1}{\sqrt{3}} \]

Evaluate both sides:
- **Left Hand Side (LHS):**
  \[ LHS = \tan 60^\circ = \sqrt{3} \]
- **Right Hand Side (RHS):**
  \[ RHS = \frac{2 \tan 30^\circ}{1 - \tan^2 30^\circ} = \frac{2 \left(\frac{1}{\sqrt{3}}\right)}{1 - \left(\frac{1}{\sqrt{3}}\right)^2} \]
  \[ = \frac{\frac{2}{\sqrt{3}}}{1 - \frac{1}{3}} = \frac{\frac{2}{\sqrt{3}}}{\frac{2}{3}} = \frac{2}{\sqrt{3}} \times \frac{3}{2} = \frac{3}{\sqrt{3}} = \sqrt{3} \]

Since \( LHS = RHS \), the identity is verified.

</details>

10. 🔴 Show that sin(60° + 30°) ≠ sin 60° + sin 30°.
<details>
<summary>Solution</summary>

Evaluate both sides using standard values:
- **Left Hand Side (LHS):**
  \[ LHS = \sin(60^\circ + 30^\circ) = \sin 90^\circ = 1 \]
- **Right Hand Side (RHS):**
  \[ RHS = \sin 60^\circ + \sin 30^\circ = \frac{\sqrt{3}}{2} + \frac{1}{2} = \frac{\sqrt{3} + 1}{2} \]

Since \( \sqrt{3} \approx 1.732 \):
\[ RHS = \frac{1.732 + 1}{2} = 1.366 \neq 1 \]

Thus, \( LHS \neq RHS \).

</details>

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
<details>
<summary>Solution</summary>

We are given:
\[ \tan \theta = 1 \]

From the standard table, we know that for acute angles:
\[ \tan 45^\circ = 1 \]

Comparing both equations, we find:
\[ \theta = 45^\circ \]

</details>

12. 🟢 If √3 sec θ = 2, find θ.
<details>
<summary>Solution</summary>

We are given:
\[ \sqrt{3} \sec \theta = 2 \]

Divide both sides by \(\sqrt{3}\):
\[ \sec \theta = \frac{2}{\sqrt{3}} \]

From the standard values, we know:
\[ \sec 30^\circ = \frac{2}{\sqrt{3}} \]

Comparing both sides, we find:
\[ \theta = 30^\circ \]

</details>

13. 🟡 If 2 cos 3θ = 1, find θ.
<details>
<summary>Solution</summary>

We are given:
\[ 2 \cos 3\theta = 1 \]

Divide both sides by 2:
\[ \cos 3\theta = \frac{1}{2} \]

From the standard values, we know:
\[ \cos 60^\circ = \frac{1}{2} \]

Comparing the angles:
\[ 3\theta = 60^\circ \implies \theta = 20^\circ \]

</details>

14. 🟡 If sin(θ + 30°) = √3/2, find θ.
<details>
<summary>Solution</summary>

We are given:
\[ \sin(\theta + 30^\circ) = \frac{\sqrt{3}}{2} \]

From the standard values, we know:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2} \]

Comparing the angles:
\[ \theta + 30^\circ = 60^\circ \implies \theta = 60^\circ - 30^\circ = 30^\circ \]

</details>

15. 🔴 If tan²θ = 1/3, find θ (0° < θ < 90°).
<details>
<summary>Solution</summary>

We are given:
\[ \tan^2\theta = \frac{1}{3} \]

Taking the positive square root on both sides (since \( 0^\circ < \theta < 90^\circ \) lies in the first quadrant where tangent is positive):
\[ \tan \theta = \frac{1}{\sqrt{3}} \]

From the standard values, we know:
\[ \tan 30^\circ = \frac{1}{\sqrt{3}} \]

Therefore:
\[ \theta = 30^\circ \]

</details>

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
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \sin 45^\circ = \frac{1}{\sqrt{2}}, \quad \sin 60^\circ = \frac{\sqrt{3}}{2} \]

Calculate the sum of their squares:
\[ \sin^2 30^\circ + \sin^2 45^\circ + \sin^2 60^\circ = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 \]
\[ = \frac{1}{4} + \frac{1}{2} + \frac{3}{4} \]
\[ = \frac{1}{4} + \frac{2}{4} + \frac{3}{4} = \frac{6}{4} = \frac{3}{2} \]

</details>

17. 🟡 Evaluate: tan² 30° + tan² 45° + tan² 60°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 30^\circ = \frac{1}{\sqrt{3}}, \quad \tan 45^\circ = 1, \quad \tan 60^\circ = \sqrt{3} \]

Calculate the sum of their squares:
\[ \tan^2 30^\circ + \tan^2 45^\circ + \tan^2 60^\circ = \left(\frac{1}{\sqrt{3}}\right)^2 + (1)^2 + (\sqrt{3})^2 \]
\[ = \frac{1}{3} + 1 + 3 = 4 + \frac{1}{3} = \frac{13}{3} \]

</details>

18. 🟡 Evaluate: cosec² 30° − sec² 45° + cot² 60°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \csc 30^\circ = 2, \quad \sec 45^\circ = \sqrt{2}, \quad \cot 60^\circ = \frac{1}{\sqrt{3}} \]

Evaluate the expression:
\[ \csc^2 30^\circ - \sec^2 45^\circ + \cot^2 60^\circ = (2)^2 - (\sqrt{2})^2 + \left(\frac{1}{\sqrt{3}}\right)^2 \]
\[ = 4 - 2 + \frac{1}{3} = 2 + \frac{1}{3} = \frac{7}{3} \]

</details>

19. 🔴 Evaluate: 4 sin⁴ 30° + 3 cos² 60° − 2 tan⁴ 45°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \cos 60^\circ = \frac{1}{2}, \quad \tan 45^\circ = 1 \]

Evaluate the expression:
\[ 4 \sin^4 30^\circ + 3 \cos^2 60^\circ - 2 \tan^4 45^\circ = 4 \left(\frac{1}{2}\right)^4 + 3 \left(\frac{1}{2}\right)^2 - 2 (1)^4 \]
\[ = 4 \left(\frac{1}{16}\right) + 3 \left(\frac{1}{4}\right) - 2 \]
\[ = \frac{1}{4} + \frac{3}{4} - 2 = 1 - 2 = -1 \]

</details>

20. 🔴 ⭐ Find the value of (sin² 60° + cosec² 30°)/(cos² 45° + sec² 30°).
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2} \implies \sin^2 60^\circ = \frac{3}{4} \]
\[ \csc 30^\circ = 2 \implies \csc^2 30^\circ = 4 \]
\[ \cos 45^\circ = \frac{1}{\sqrt{2}} \implies \cos^2 45^\circ = \frac{1}{2} \]
\[ \sec 30^\circ = \frac{2}{\sqrt{3}} \implies \sec^2 30^\circ = \frac{4}{3} \]

Evaluate the numerator:
\[ \text{Numerator} = \sin^2 60^\circ + \csc^2 30^\circ = \frac{3}{4} + 4 = \frac{19}{4} \]

Evaluate the denominator:
\[ \text{Denominator} = \cos^2 45^\circ + \sec^2 30^\circ = \frac{1}{2} + \frac{4}{3} = \frac{3 + 8}{6} = \frac{11}{6} \]

Find the ratio:
\[ \frac{\text{Numerator}}{\text{Denominator}} = \frac{\frac{19}{4}}{\frac{11}{6}} = \frac{19}{4} \times \frac{6}{11} = \frac{19 \times 3}{2 \times 11} = \frac{57}{22} \]

</details>

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
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \cos 60^\circ = \frac{1}{2} \]
\[ \cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \sin 60^\circ = \frac{\sqrt{3}}{2} \]

Evaluate the Left Hand Side (LHS):
\[ LHS = \sin 30^\circ \cos 60^\circ + \cos 30^\circ \sin 60^\circ \]
\[ = \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) + \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) \]
\[ = \frac{1}{4} + \frac{3}{4} = 1 \]

Since \( LHS = RHS = 1 \), the equation is proved.

</details>

22. 🟡 Prove tan 45° + cot 45° = 2.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 45^\circ = 1, \quad \cot 45^\circ = 1 \]

Evaluate the Left Hand Side (LHS):
\[ LHS = \tan 45^\circ + \cot 45^\circ = 1 + 1 = 2 \]

Since \( LHS = RHS = 2 \), the equation is proved.

</details>

23. 🟡 Prove sin 60° = 2 tan 30°/(1 + tan² 30°).
<details>
<summary>Solution</summary>

Substitute the standard values:
- **Left Hand Side (LHS):**
  \[ LHS = \sin 60^\circ = \frac{\sqrt{3}}{2} \]
- **Right Hand Side (RHS):**
  \[ RHS = \frac{2 \tan 30^\circ}{1 + \tan^2 30^\circ} = \frac{2 \left(\frac{1}{\sqrt{3}}\right)}{1 + \left(\frac{1}{\sqrt{3}}\right)^2} \]
  \[ = \frac{\frac{2}{\sqrt{3}}}{1 + \frac{1}{3}} = \frac{\frac{2}{\sqrt{3}}}{\frac{4}{3}} = \frac{2}{\sqrt{3}} \times \frac{3}{4} = \frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2} \]

Since \( LHS = RHS = \frac{\sqrt{3}}{2} \), the equation is proved.

</details>

24. 🔴 Prove that sin² 60° + sin² 30° = sin² 45° + sin² 45°.
<details>
<summary>Solution</summary>

Evaluate both sides using standard values:
- **Left Hand Side (LHS):**
  \[ LHS = \sin^2 60^\circ + \sin^2 30^\circ = \left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{3}{4} + \frac{1}{4} = 1 \]
- **Right Hand Side (RHS):**
  \[ RHS = \sin^2 45^\circ + \sin^2 45^\circ = \left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{2} + \frac{1}{2} = 1 \]

Since \( LHS = RHS = 1 \), the equation is proved.

</details>

25. 🔴 ⭐ If A = 30°, verify that sin 2A = 2 sin A cos A.
<details>
<summary>Solution</summary>

Given \( A = 30^\circ \), then \( 2A = 60^\circ \).
Evaluate both sides:
- **Left Hand Side (LHS):**
  \[ LHS = \sin 2A = \sin 60^\circ = \frac{\sqrt{3}}{2} \]
- **Right Hand Side (RHS):**
  \[ RHS = 2 \sin A \cos A = 2 \sin 30^\circ \cos 30^\circ = 2 \left(\frac{1}{2}\right) \left(\frac{\sqrt{3}}{2}\right) = \frac{\sqrt{3}}{2} \]

Since \( LHS = RHS = \frac{\sqrt{3}}{2} \), the identity is verified.

</details>

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
<details>
<summary>Solution</summary>

Evaluate both values using the standard table:
\[ \cos 30^\circ = \frac{\sqrt{3}}{2} \approx 0.866 \]
\[ \cos 60^\circ = \frac{1}{2} = 0.5 \]

Since \( 0.866 > 0.5 \), we have:
\[ \cos 30^\circ > \cos 60^\circ \]

Thus, **cos 30°** is greater.

</details>

27. 🟢 Which is greater: tan 30° or tan 45°?<br>
<details>
<summary>Solution</summary>

Evaluate both values using the standard table:
\[ \tan 30^\circ = \frac{1}{\sqrt{3}} \approx 0.577 \]
\[ \tan 45^\circ = 1 \]

Since \( 1 > 0.577 \), we have:
\[ \tan 45^\circ > \tan 30^\circ \]

Thus, **tan 45°** is greater.

</details>

28. 🟡 Arrange in increasing order: sin 0°, sin 30°, sin 45°, sin 60°, sin 90°.
<details>
<summary>Solution</summary>

Find the value of each:
- \( \sin 0^\circ = 0 \)
- \( \sin 30^\circ = 0.5 \)
- \( \sin 45^\circ = \frac{1}{\sqrt{2}} \approx 0.707 \)
- \( \sin 60^\circ = \frac{\sqrt{3}}{2} \approx 0.866 \)
- \( \sin 90^\circ = 1 \)

Comparing these values:
\[ 0 < 0.5 < 0.707 < 0.866 < 1 \]

Therefore, the increasing order is:
\[ \sin 0^\circ, \sin 30^\circ, \sin 45^\circ, \sin 60^\circ, \sin 90^\circ \]

</details>

29. 🟡 Arrange in decreasing order: cos 90°, cos 60°, cos 45°, cos 30°, cos 0°.
<details>
<summary>Solution</summary>

Find the value of each:
- \( \cos 90^\circ = 0 \)
- \( \cos 60^\circ = 0.5 \)
- \( \cos 45^\circ = \frac{1}{\sqrt{2}} \approx 0.707 \)
- \( \cos 30^\circ = \frac{\sqrt{3}}{2} \approx 0.866 \)
- \( \cos 0^\circ = 1 \)

Comparing these values in descending order (largest to smallest):
\[ 1 > 0.866 > 0.707 > 0.5 > 0 \]

Therefore, the decreasing order is:
\[ \cos 0^\circ, \cos 30^\circ, \cos 45^\circ, \cos 60^\circ, \cos 90^\circ \]

</details>

30. 🟡 Which is larger: sec 45° or cosec 45°?<br>
<details>
<summary>Solution</summary>

Evaluate both values using the standard table:
\[ \sec 45^\circ = \sqrt{2} \]
\[ \csc 45^\circ = \sqrt{2} \]

Both values are exactly equal to \( \sqrt{2} \approx 1.414 \). Thus, neither is larger; they are equal.

</details>

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
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \cot 30^\circ = \sqrt{3}, \quad \tan 60^\circ = \sqrt{3} \]

Find their product:
\[ \cot 30^\circ \times \tan 60^\circ = \sqrt{3} \times \sqrt{3} = 3 \]

</details>

32. 🟢 Find cosec 45° × sec 45°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \csc 45^\circ = \sqrt{2}, \quad \sec 45^\circ = \sqrt{2} \]

Find their product:
\[ \csc 45^\circ \times \sec 45^\circ = \sqrt{2} \times \sqrt{2} = 2 \]

</details>

33. 🟡 Find (cosec 30° + sec 60°)/(cot 45°).
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \csc 30^\circ = 2, \quad \sec 60^\circ = 2, \quad \cot 45^\circ = 1 \]

Calculate the value of the expression:
\[ \frac{\csc 30^\circ + \sec 60^\circ}{\cot 45^\circ} = \frac{2 + 2}{1} = 4 \]

</details>

34. 🟡 Find sec² 30° + cosec² 45° − cot² 60°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sec 30^\circ = \frac{2}{\sqrt{3}}, \quad \csc 45^\circ = \sqrt{2}, \quad \cot 60^\circ = \frac{1}{\sqrt{3}} \]

Evaluate the expression:
\[ \sec^2 30^\circ + \csc^2 45^\circ - \cot^2 60^\circ = \left(\frac{2}{\sqrt{3}}\right)^2 + (\sqrt{2})^2 - \left(\frac{1}{\sqrt{3}}\right)^2 \]
\[ = \frac{4}{3} + 2 - \frac{1}{3} \]
\[ = \left(\frac{4}{3} - \frac{1}{3}\right) + 2 = 1 + 2 = 3 \]

</details>

35. 🔴 If cot θ = √3, find θ and then find sin θ cos θ + cos² θ.
<details>
<summary>Solution</summary>

Given:
\[ \cot \theta = \sqrt{3} \]

For an acute angle, we know:
\[ \cot 30^\circ = \sqrt{3} \implies \theta = 30^\circ \]

Now, substitute \( \theta = 30^\circ \) into the given expression:
\[ \sin 30^\circ = \frac{1}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2} \]

Evaluate the expression:
\[ \sin 30^\circ \cos 30^\circ + \cos^2 30^\circ = \left(\frac{1}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{3}}{2}\right)^2 \]
\[ = \frac{\sqrt{3}}{4} + \frac{3}{4} = \frac{3 + \sqrt{3}}{4} \]

</details>

---

## Stage 4: Type Mixer

1. 🟡 Find the value of tan² 60° + 2 tan² 45° − 3 cot² 30°.
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \tan 60^\circ = \sqrt{3}, \quad \tan 45^\circ = 1, \quad \cot 30^\circ = \sqrt{3} \]

Evaluate the expression:
\[ \tan^2 60^\circ + 2 \tan^2 45^\circ - 3 \cot^2 30^\circ = (\sqrt{3})^2 + 2(1)^2 - 3(\sqrt{3})^2 \]
\[ = 3 + 2(1) - 3(3) \]
\[ = 3 + 2 - 9 = -4 \]

</details>

2. 🟡 If 3 tan²θ = 1 and θ is acute, find θ and then find sin²θ + cos²θ.
<details>
<summary>Solution</summary>

Given:
\[ 3 \tan^2\theta = 1 \implies \tan^2\theta = \frac{1}{3} \]

Taking the positive square root (since \( \theta \) is acute, \( \tan\theta > 0 \ )):
\[ \tan \theta = \frac{1}{\sqrt{3}} \]

From the standard table, we get:
\[ \theta = 30^\circ \]

Now, find \( \sin^2\theta + \cos^2\theta \):
By the fundamental trigonometric identity:
\[ \sin^2\theta + \cos^2\theta = 1 \]

Alternatively, by direct substitution of \( \theta = 30^\circ \):
\[ \sin^2 30^\circ + \cos^2 30^\circ = \left(\frac{1}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1 \]

</details>

3. 🔴 ⭐ Evaluate: (sin 30° − sin 90° + 2 cos 0°)/(tan 30° × tan 60°).
<details>
<summary>Solution</summary>

Substitute the standard values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \sin 90^\circ = 1, \quad \cos 0^\circ = 1 \]
\[ \tan 30^\circ = \frac{1}{\sqrt{3}}, \quad \tan 60^\circ = \sqrt{3} \]

Calculate the numerator:
\[ \text{Numerator} = \sin 30^\circ - \sin 90^\circ + 2\cos 0^\circ = \frac{1}{2} - 1 + 2(1) = \frac{3}{2} \]

Calculate the denominator:
\[ \text{Denominator} = \tan 30^\circ \times \tan 60^\circ = \frac{1}{\sqrt{3}} \times \sqrt{3} = 1 \]

Evaluate the full expression:
\[ \frac{\text{Numerator}}{\text{Denominator}} = \frac{3/2}{1} = \frac{3}{2} \]

</details>

4. 🔴 If sin(A + B) = 1 and cos(A − B) = √3/2, find A and B (both acute, A > B).
<details>
<summary>Solution</summary>

Given:
1) \[ \sin(A + B) = 1 \]
Since \( A, B \) are acute, \( A + B \le 180^\circ \). Thus:
\[ A + B = 90^\circ \quad \text{--- (Equation 1)} \]

2) \[ \cos(A - B) = \frac{\sqrt{3}}{2} \]
Since \( A > B \) and both are acute, \( 0^\circ < A - B < 90^\circ \). Thus:
\[ A - B = 30^\circ \quad \text{--- (Equation 2)} \]

Solve the system of equations:
Add Equation 1 and Equation 2:
\[ (A + B) + (A - B) = 90^\circ + 30^\circ \]
\[ 2A = 120^\circ \implies A = 60^\circ \]

Subtract Equation 2 from Equation 1:
\[ (A + B) - (A - B) = 90^\circ - 30^\circ \]
\[ 2B = 60^\circ \implies B = 30^\circ \]

Thus, \( A = 60^\circ \) and \( B = 30^\circ \).

</details>

5. 🔴 Prove that sin 60° cos 30° − cos 60° sin 30° = sin 30°.
<details>
<summary>Solution</summary>

Evaluate both sides using standard values:
- **Left Hand Side (LHS):**
  \[ LHS = \sin 60^\circ \cos 30^\circ - \cos 60^\circ \sin 30^\circ \]
  \[ = \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) \]
  \[ = \frac{3}{4} - \frac{1}{4} = \frac{2}{4} = \frac{1}{2} \]
- **Right Hand Side (RHS):**
  \[ RHS = \sin 30^\circ = \frac{1}{2} \]

Since \( LHS = RHS = \frac{1}{2} \), the identity is proved.

</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Evaluate: sin 60° cos 30° + cos 60° sin 30°. **(2 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
= (√3/2)(√3/2) + (1/2)(1/2)
= 3/4 + 1/4 = 1
```

</details>

---

**Q2.** 🟡 Find the value of x if 2 sin x = √3. **(2 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
2 sin x = √3
sin x = √3/2
∴ x = 60°
```

</details>

---

**Q3.** 🟡 Evaluate: 5 cos² 60° + 4 sec² 30° − tan² 45°. **(3 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
= 5(1/2)² + 4(2/√3)² − (1)²
= 5(1/4) + 4(4/3) − 1
= 5/4 + 16/3 − 1
= (15 + 64 − 12)/12
= 67/12
```

</details>

---

**Q4.** 🟡 If θ = 30°, verify sin 2θ = 2 sin θ cos θ. **(3 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
LHS: sin 60° = √3/2
RHS: 2 sin 30° cos 30° = 2(1/2)(√3/2) = √3/2
LHS = RHS ✓
```

</details>

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
= 4(3/4) + 3(1/3) − 8(1/2)
= 3 + 1 − 4 = 0
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
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \sin 30^\circ = \frac{1}{2} \]

**Answer: (a)**

</details>

2. 🟢 cos 45° equals:
   (a) 1/2   (b) √3/2   (c) 1/√2   (d) 0
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \cos 45^\circ = \frac{1}{\sqrt{2}} \]

**Answer: (c)**

</details>

3. 🟢 tan 60° equals:
   (a) 1/√3   (b) √3   (c) 1   (d) 0
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \tan 60^\circ = \sqrt{3} \]

**Answer: (b)**

</details>

4. 🟡 sin 60° cos 30° + cos 60° sin 30° equals:
   (a) 1/2   (b) 1   (c) √3/2   (d) 0
<details>
<summary>Solution</summary>

Substitute the values:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2} \]
\[ \cos 60^\circ = \frac{1}{2}, \quad \sin 30^\circ = \frac{1}{2} \]

Evaluate the expression:
\[ \sin 60^\circ \cos 30^\circ + \cos 60^\circ \sin 30^\circ = \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) \]
\[ = \frac{3}{4} + \frac{1}{4} = 1 \]

**Answer: (b)**

</details>

5. 🟢 The value of sin 0° is:
   (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \sin 0^\circ = 0 \]

**Answer: (a)**

</details>

6. 🟢 cos 90° equals:
   (a) 1   (b) 0   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \cos 90^\circ = 0 \]

**Answer: (b)**

</details>

7. 🟡 If sin θ = 1/2, θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Given:
\[ \sin \theta = \frac{1}{2} \]

From the standard values for acute angles:
\[ \sin 30^\circ = \frac{1}{2} \implies \theta = 30^\circ \]

**Answer: (a)**

</details>

8. 🟡 If √3 tan θ = 1, θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Given:
\[ \sqrt{3} \tan \theta = 1 \implies \tan \theta = \frac{1}{\sqrt{3}} \]

From the standard values for acute angles:
\[ \tan 30^\circ = \frac{1}{\sqrt{3}} \implies \theta = 30^\circ \]

**Answer: (a)**

</details>

9. 🟢 sec 45° equals:
   (a) 1   (b) √2   (c) 2/√3   (d) 2
<details>
<summary>Solution</summary>

Recall that \( \sec\theta = \frac{1}{\cos\theta} \). Therefore:
\[ \sec 45^\circ = \frac{1}{\cos 45^\circ} = \frac{1}{1/\sqrt{2}} = \sqrt{2} \]

**Answer: (b)**

</details>

10. 🟡 sin² 30° + sin² 60° equals:
    (a) 0   (b) 1/2   (c) 1   (d) 3/2
<details>
<summary>Solution</summary>

Substitute the values:
\[ \sin 30^\circ = \frac{1}{2}, \quad \sin 60^\circ = \frac{\sqrt{3}}{2} \]

Calculate the sum of their squares:
\[ \sin^2 30^\circ + \sin^2 60^\circ = \left(\frac{1}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1 \]

**Answer: (c)**

</details>

11. 🟡 tan 45° + cot 45° equals:
    (a) 1   (b) 2   (c) 0   (d) 3
<details>
<summary>Solution</summary>

Substitute the values:
\[ \tan 45^\circ = 1, \quad \cot 45^\circ = 1 \]

Evaluate the sum:
\[ \tan 45^\circ + \cot 45^\circ = 1 + 1 = 2 \]

**Answer: (b)**

</details>

12. 🟡 cosec 30° equals:
    (a) 2   (b) 2/√3   (c) √2   (d) 1
<details>
<summary>Solution</summary>

Recall that \( \csc\theta = \frac{1}{\sin\theta} \). Therefore:
\[ \csc 30^\circ = \frac{1}{\sin 30^\circ} = \frac{1}{1/2} = 2 \]

**Answer: (a)**

</details>

13. 🟢 Which is true?<br>
    (a) sin 30° < sin 45°   (b) sin 30° > sin 45°   (c) sin 30° = sin 45°   (d) None
<details>
<summary>Solution</summary>

Compare the values:
\[ \sin 30^\circ = 0.5 \]
\[ \sin 45^\circ = \frac{1}{\sqrt{2}} \approx 0.707 \]

Since \( 0.5 < 0.707 \), we have \( \sin 30^\circ < \sin 45^\circ \).

**Answer: (a)**

</details>

14. 🟡 If sin 2θ = √3/2, θ = ?<br>
    (a) 15°   (b) 30°   (c) 45°   (d) 60°
<details>
<summary>Solution</summary>

Given:
\[ \sin 2\theta = \frac{\sqrt{3}}{2} \]

Since \( \sin 60^\circ = \frac{\sqrt{3}}{2} \):
\[ 2\theta = 60^\circ \implies \theta = 30^\circ \]

**Answer: (b)**

</details>

15. 🟡 The value of 2 tan 45° + cos 60° − sin 30° is:
    (a) 1   (b) 2   (c) 0   (d) 3
<details>
<summary>Solution</summary>

Substitute the values:
\[ \tan 45^\circ = 1, \quad \cos 60^\circ = \frac{1}{2}, \quad \sin 30^\circ = \frac{1}{2} \]

Evaluate the expression:
\[ 2\tan 45^\circ + \cos 60^\circ - \sin 30^\circ = 2(1) + \frac{1}{2} - \frac{1}{2} = 2 \]

**Answer: (b)**

</details>

16. 🟡 sin 0° + cos 0° + tan 0° equals:
    (a) 0   (b) 1   (c) 2   (d) 3
<details>
<summary>Solution</summary>

Substitute the values:
\[ \sin 0^\circ = 0, \quad \cos 0^\circ = 1, \quad \tan 0^\circ = 0 \]

Evaluate the sum:
\[ \sin 0^\circ + \cos 0^\circ + \tan 0^\circ = 0 + 1 + 0 = 1 \]

**Answer: (b)**

</details>

17. 🟡 sec 30° + cosec 60° equals:
    (a) 4/√3   (b) 2/√3   (c) √3   (d) 2
<details>
<summary>Solution</summary>

Substitute the values:
\[ \sec 30^\circ = \frac{2}{\sqrt{3}} \]
\[ \csc 60^\circ = \frac{2}{\sqrt{3}} \]

Evaluate:
\[ \sec 30^\circ + \csc 60^\circ = \frac{2}{\sqrt{3}} + \frac{2}{\sqrt{3}} = \frac{4}{\sqrt{3}} \]

**Answer: (a)**

</details>

18. 🟡 cot 45° equals:
    (a) 0   (b) 1   (c) √3   (d) 1/√3
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \cot 45^\circ = 1 \]

**Answer: (b)**

</details>

19. 🟡 cos 60° × sec 60° equals:
    (a) 0   (b) 1/2   (c) 1   (d) 2
<details>
<summary>Solution</summary>

Using the reciprocal identity:
\[ \cos 60^\circ \times \sec 60^\circ = 1 \]

Alternatively, substituting the values:
\[ \cos 60^\circ = \frac{1}{2}, \quad \sec 60^\circ = 2 \implies \frac{1}{2} \times 2 = 1 \]

**Answer: (c)**

</details>

20. 🟡 If sin(A + B) = 1 and sin(A − B) = 1/2, (A>B), then A = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 75°
<details>
<summary>Solution</summary>

Given A and B are acute angles:
1) \[ \sin(A + B) = 1 \implies A + B = 90^\circ \]
2) \[ \sin(A - B) = \frac{1}{2} \implies A - B = 30^\circ \]

Add the two equations:
\[ (A + B) + (A - B) = 90^\circ + 30^\circ \]
\[ 2A = 120^\circ \implies A = 60^\circ \]

**Answer: (c)**

</details>

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
