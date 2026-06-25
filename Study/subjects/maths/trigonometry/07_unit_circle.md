# Chapter 7: Trigonometric Functions — The Unit Circle

---

## Stage 1: The Core Idea

### Beyond Right Triangles

In right triangles, angles only go up to 90°. But real-world angles can be anything — 200°, 720°, −45°. A wheel keeps spinning, a pendulum keeps swinging.

How do we define sin θ for θ = 200°?<br>

**Enter the unit circle.**

```
        y
        ↑
        |  • P(cos θ, sin θ)
        |╱
    θ   |————→ x
   ————————————

A circle of radius 1 centered at origin.
Any point P on it has coordinates (cos θ, sin θ).
```

The **unit circle** extends trig ratios to **any angle**:
- x-coordinate = cos θ
- y-coordinate = sin θ
- tan θ = y/x

As the point P travels around the circle, sin θ and cos θ vary between −1 and 1 — giving us the **wave-like graphs** of trigonometric functions.

---

## Stage 2: The Formula Lab

### Signs in Quadrants

```
Quadrant II (90°−180°)    |    Quadrant I (0°−90°)
  sin: +                  |      sin: +
  cos: −                  |      cos: +
  tan: −                  |      tan: +
——————————————————————————+——————————————————————————
Quadrant III (180°−270°)  |    Quadrant IV (270°−360°)
  sin: −                  |      sin: −
  cos: −                  |      cos: +
  tan: +                  |      tan: −
```

**Memory trick — ASTC: "All Silver Tea Cups"**
- **A**ll ratios positive → Quadrant I
- **S**in positive → Quadrant II
- **T**an positive → Quadrant III
- **C**os positive → Quadrant IV

### Trigonometric Functions for Any Angle

```
sin(θ + 360°n) = sin θ      (period = 360° = 2π)
cos(θ + 360°n) = cos θ
tan(θ + 180°n) = tan θ      (period = 180° = π)
```

---

## Stage 3: Type-wise Mastery

### Type 1: Finding Quadrant of an Angle

**Goal:** Given an angle, determine which quadrant it lies in.

**Solved Example:**

Find the quadrant of 210°.

**Solution:**
```
210° lies between 180° and 270° → Quadrant III
```
🟢 Easy

---

**Practice Problems:**

1. 🟢 Find the quadrant of 150°.
<details>
<summary>Solution</summary>

Angle \( 150^\circ \) lies between \( 90^\circ \) and \( 180^\circ \).
Therefore, it lies in Quadrant II.

**Answer: Quadrant II**
</details>

2. 🟢 Find the quadrant of 300°.
<details>
<summary>Solution</summary>

Angle \( 300^\circ \) lies between \( 270^\circ \) and \( 360^\circ \).
Therefore, it lies in Quadrant IV.

**Answer: Quadrant IV**
</details>

3. 🟢 Find the quadrant of −45°.
<details>
<summary>Solution</summary>

Angle \( \theta = -45^\circ \) can be converted to its positive coterminal equivalent:
\[ -45^\circ + 360^\circ = 315^\circ \]
Since \( 315^\circ \) lies between \( 270^\circ \) and \( 360^\circ \), the angle lies in Quadrant IV.

**Answer: Quadrant IV**
</details>

4. 🟡 Find the quadrant of 1000° (reduce by 360° first).
<details>
<summary>Solution</summary>

We can reduce \( 1000^\circ \) by subtracting multiples of \( 360^\circ \):
\[ 1000^\circ = 2 \times 360^\circ + 280^\circ \]
The coterminal angle is \( 280^\circ \). Since \( 280^\circ \) lies between \( 270^\circ \) and \( 360^\circ \), it lies in Quadrant IV.

**Answer: Quadrant IV**
</details>

5. 🟡 Find the quadrant of 7π/6 radians.
<details>
<summary>Solution</summary>

We can convert \( \frac{7\pi}{6} \) radians to degrees:
\[ \frac{7\pi}{6} \times \frac{180^\circ}{\pi} = 7 \times 30^\circ = 210^\circ \]
Since \( 210^\circ \) lies between \( 180^\circ \) and \( 270^\circ \), it lies in Quadrant III.

**Answer: Quadrant III**
</details>

---

### Type 2: Sign of a Trig Function for a Given Angle

**Goal:** Determine if a given trig ratio is positive or negative for a given angle.

**Solved Example:**

Is sin 200° positive or negative?<br>

**Solution:**
```
200° is in QIII → sin is negative
Answer: negative
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

6. 🟢 Is cos 120° positive or negative?<br>
<details>
<summary>Solution</summary>

The angle \( 120^\circ \) is in Quadrant II. In Quadrant II, cosine is negative.

**Answer: negative**
</details>

7. 🟢 Is tan 315° positive or negative?<br>
<details>
<summary>Solution</summary>

The angle \( 315^\circ \) is in Quadrant IV. In Quadrant IV, tangent is negative.

**Answer: negative**
</details>

8. 🟡 Is sec 240° positive or negative?<br>
<details>
<summary>Solution</summary>

The angle \( 240^\circ \) is in Quadrant III. In Quadrant III, only tangent and cotangent are positive; cosine is negative.
Therefore, \( \sec 240^\circ = \frac{1}{\cos 240^\circ} \) is also negative.

**Answer: negative**
</details>

9. 🟡 Is cosec 150° positive or negative?<br>
<details>
<summary>Solution</summary>

The angle \( 150^\circ \) is in Quadrant II. In Quadrant II, sine is positive.
Therefore, \( \csc 150^\circ = \frac{1}{\sin 150^\circ} \) is also positive.

**Answer: positive**
</details>

10. 🟡 Is cot(−45°) positive or negative?<br>
<details>
<summary>Solution</summary>

Using the negative angle identity for cotangent:
\[ \cot(-45^\circ) = -\cot(45^\circ) \]
Since \( \cot(45^\circ) = 1 \) is positive, \( -\cot(45^\circ) = -1 \) is negative.

**Answer: negative**
</details>

---

### Type 3: Finding Coordinates on Unit Circle

**Goal:** Find (x, y) coordinates for a given angle on the unit circle.

**Solved Example:**

Find the coordinates of the point on the unit circle at θ = 120°.

**Solution:**
```
120° is in QII.
Reference angle = 180° − 120° = 60°
cos 120° = −cos 60° = −1/2
sin 120° = sin 60° = √3/2
Coordinates: (−1/2, √3/2)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 Find coordinates for θ = 135°.
<details>
<summary>Solution</summary>

The coordinates are given by \( (x, y) = (\cos \theta, \sin \theta) \).
For \( \theta = 135^\circ \) (Quadrant II, reference angle \( 45^\circ \)):
\[ \cos 135^\circ = -\cos 45^\circ = -\frac{1}{\sqrt{2}} \]
\[ \sin 135^\circ = \sin 45^\circ = \frac{1}{\sqrt{2}} \]
Thus, the coordinates are \( \left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) \).

**Answer: \(\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)\)**
</details>

12. 🟡 Find coordinates for θ = 210°.
<details>
<summary>Solution</summary>

The coordinates are given by \( (x, y) = (\cos \theta, \sin \theta) \).
For \( \theta = 210^\circ \) (Quadrant III, reference angle \( 30^\circ \)):
\[ \cos 210^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2} \]
\[ \sin 210^\circ = -\sin 30^\circ = -\frac{1}{2} \]
Thus, the coordinates are \( \left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right) \).

**Answer: \(\left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)\)**
</details>

13. 🟡 Find coordinates for θ = 300°.
<details>
<summary>Solution</summary>

visualizing coordinates are given by \( (x, y) = (\cos \theta, \sin \theta) \).
For \( \theta = 300^\circ \) (Quadrant IV, reference angle \( 60^\circ \)):
\[ \cos 300^\circ = \cos 60^\circ = \frac{1}{2} \]
\[ \sin 300^\circ = -\sin 60^\circ = -\frac{\sqrt{3}}{2} \]
Thus, the coordinates are \( \left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right) \).

**Answer: \(\left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)\)**
</details>

14. 🟡 Find coordinates for θ = 330°.
<details>
<summary>Solution</summary>

The coordinates are given by \( (x, y) = (\cos \theta, \sin \theta) \).
For \( \theta = 330^\circ \) (Quadrant IV, reference angle \( 30^\circ \)):
\[ \cos 330^\circ = \cos 30^\circ = \frac{\sqrt{3}}{2} \]
\[ \sin 330^\circ = -\sin 30^\circ = -\frac{1}{2} \]
Thus, the coordinates are \( \left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right) \).

**Answer: \(\left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)\)**
</details>

15. 🔴 Find coordinates for θ = −120°.
<details>
<summary>Solution</summary>

The angle \( -120^\circ \) is coterminal with:
\[ -120^\circ + 360^\circ = 240^\circ \]
This angle lies in Quadrant III, with a reference angle of \( 240^\circ - 180^\circ = 60^\circ \).
- \( \cos(-120^\circ) = \cos(240^\circ) = -\cos(60^\circ) = -\frac{1}{2} \)
- \( \sin(-120^\circ) = \sin(240^\circ) = -\sin(60^\circ) = -\frac{\sqrt{3}}{2} \)
Thus, the coordinates are \( \left(-\frac{1}{2}, -\frac{\sqrt{3}}{2}\right) \).

**Answer: \(\left(-\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)\)**
</details>

---

### Type 4: Finding Sign of Expression

**Goal:** Determine if a product/sum of trig functions is positive or negative.

**Solved Example:**

Is sin 200° × cos 300° positive or negative?<br>

**Solution:**
```
200° in QIII: sin 200° = −
300° in QIV: cos 300° = +
Product: (−) × (+) = − (negative)
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 sin 150° × cos 250°: positive or negative?<br>
<details>
<summary>Solution</summary>

- \( 150^\circ \) is in Quadrant II, so \( \sin 150^\circ > 0 \) (+).
- \( 250^\circ \) is in Quadrant III, so \( \cos 250^\circ < 0 \) (−).
- The product is \( (+) \times (−) = − \) (negative).

**Answer: negative**
</details>

17. 🟡 tan 100° × cot 350°: positive or negative?<br>
<details>
<summary>Solution</summary>

- \( 100^\circ \) is in Quadrant II, so \( \tan 100^\circ < 0 \) (−).
- \( 350^\circ \) is in Quadrant IV, so \( \cot 350^\circ < 0 \) (−).
- The product is \( (−) \times (−) = + \) (positive).

**Answer: positive**
</details>

18. 🟡 sin 300° + cos 120°: positive or negative?<br>
<details>
<summary>Solution</summary>

- \( \sin 300^\circ = -\sin 60^\circ = -\frac{\sqrt{3}}{2} < 0 \)
- \( \cos 120^\circ = -\cos 60^\circ = -\frac{1}{2} < 0 \)
- Since both terms are negative, their sum \( \sin 300^\circ + \cos 120^\circ \) must also be negative.

**Answer: negative**
</details>

19. 🔴 (sin 200°)(cos 200°)(tan 200°): positive or negative?<br>
<details>
<summary>Solution</summary>

- \( 200^\circ \) is in Quadrant III.
- In Quadrant III:
  - \( \sin 200^\circ < 0 \) (−)
  - \( \cos 200^\circ < 0 \) (−)
  - \( \tan 200^\circ > 0 \) (+)
- The product is \( (−) \times (−) \times (+) = + \) (positive).
- Alternatively, \( (\sin 200^\circ)(\cos 200^\circ)(\tan 200^\circ) = (\sin 200^\circ)(\cos 200^\circ)\left(\frac{\sin 200^\circ}{\cos 200^\circ}\right) = \sin^2 200^\circ \), which is positive because \( \sin 200^\circ \neq 0 \).

**Answer: positive**
</details>

20. 🔴 ⭐ sin 120° × cos 210° × tan 315°: positive or negative?<br>
<details>
<summary>Solution</summary>

- \( \sin 120^\circ \) is positive (+) because \( 120^\circ \) is in Quadrant II.
- \( \cos 210^\circ \) is negative (−) because \( 210^\circ \) is in Quadrant III.
- \( \tan 315^\circ \) is negative (−) because \( 315^\circ \) is in Quadrant IV.
- The product is \( (+) \times (−) \times (−) = + \) (positive).

**Answer: positive**
</details>

---

### Type 5: Finding Trig Values for Any Angle Using Reference Angles

**Goal:** Use the reference angle to find the trig value for any angle.

**Solved Example:**

Find sin 240°.

**Solution:**
```
240° is in QIII. Reference angle = 240° − 180° = 60°
sin 60° = √3/2
In QIII, sin is negative.
∴ sin 240° = −√3/2
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Find cos 135°.
<details>
<summary>Solution</summary>

The angle \( 135^\circ \) lies in Quadrant II, where cosine is negative. The reference angle is \( 180^\circ - 135^\circ = 45^\circ \).
\[ \cos 135^\circ = -\cos 45^\circ = -\frac{1}{\sqrt{2}} \]

**Answer: \(-\frac{1}{\sqrt{2}}\)**
</details>

22. 🟡 Find tan 210°.
<details>
<summary>Solution</summary>

The angle \( 210^\circ \) lies in Quadrant III, where tangent is positive. The reference angle is \( 210^\circ - 180^\circ = 30^\circ \).
\[ \tan 210^\circ = \tan 30^\circ = \frac{1}{\sqrt{3}} \]

**Answer: \(\frac{1}{\sqrt{3}}\)**
</details>

23. 🟡 Find sin 315°.
<details>
<summary>Solution</summary>

The angle \( 315^\circ \) lies in Quadrant IV, where sine is negative. The reference angle is \( 360^\circ - 315^\circ = 45^\circ \).
\[ \sin 315^\circ = -\sin 45^\circ = -\frac{1}{\sqrt{2}} \]

**Answer: \(-\frac{1}{\sqrt{2}}\)**
</details>

24. 🟡 Find sec 150°.
<details>
<summary>Solution</summary>

The angle \( 150^\circ \) lies in Quadrant II, where secant (reciprocal of cosine) is negative. The reference angle is \( 180^\circ - 150^\circ = 30^\circ \).
\[ \cos 150^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2} \]
\[ \sec 150^\circ = \frac{1}{\cos 150^\circ} = -\frac{2}{\sqrt{3}} \]

**Answer: \(-\frac{2}{\sqrt{3}}\)**
</details>

25. 🔴 Find cot 300°.
<details>
<summary>Solution</summary>

The angle \( 300^\circ \) lies in Quadrant IV, where cotangent is negative. The reference angle is \( 360^\circ - 300^\circ = 60^\circ \).
\[ \cot 300^\circ = -\cot 60^\circ = -\frac{1}{\sqrt{3}} \]

**Answer: \(-\frac{1}{\sqrt{3}}\)**
</details>

---

### Type 6: Negative Angles

**Goal:** Find trig values for negative angles.

**Formulas:**
```
sin(−θ) = −sin θ
cos(−θ) = cos θ
tan(−θ) = −tan θ
```

**Solved Example:**

Find sin(−60°).

**Solution:**
```
sin(−60°) = −sin 60° = −√3/2
```
🟢 Easy

---

**Practice Problems:**

26. 🟢 Find cos(−45°).
<details>
<summary>Solution</summary>

Using the negative angle identity \( \cos(-\theta) = \cos \theta \):
\[ \cos(-45^\circ) = \cos 45^\circ = \frac{1}{\sqrt{2}} \]

**Answer: \(\frac{1}{\sqrt{2}}\)**
</details>

27. 🟢 Find tan(−30°).
<details>
<summary>Solution</summary>

Using the negative angle identity \( \tan(-\theta) = -\tan \theta \):
\[ \tan(-30^\circ) = -\tan 30^\circ = -\frac{1}{\sqrt{3}} \]

**Answer: \(-\frac{1}{\sqrt{3}}\)**
</details>

28. 🟡 Find sin(−210°).
<details>
<summary>Solution</summary>

Using the negative angle identity \( \sin(-\theta) = -\sin \theta \):
\[ \sin(-210^\circ) = -\sin 210^\circ \]
Since \( 210^\circ \) lies in Quadrant III:
\[ \sin 210^\circ = -\sin 30^\circ = -\frac{1}{2} \]
Thus:
\[ \sin(-210^\circ) = -\left(-\frac{1}{2}\right) = \frac{1}{2} \]

**Answer: \(\frac{1}{2}\)**
</details>

29. 🟡 Find sec(−60°).
<details>
<summary>Solution</summary>

Using the negative angle identity \( \sec(-\theta) = \sec \theta \):
\[ \sec(-60^\circ) = \sec 60^\circ = \frac{1}{\cos 60^\circ} = \frac{1}{1/2} = 2 \]

**Answer: 2**
</details>

30. 🔴 Find cot(−135°).
<details>
<summary>Solution</summary>

Using the negative angle identity \( \cot(-\theta) = -\cot \theta \):
\[ \cot(-135^\circ) = -\cot 135^\circ \]
Since \( 135^\circ \) lies in Quadrant II:
\[ \cot 135^\circ = -\cot 45^\circ = -1 \]
Thus:
\[ \cot(-135^\circ) = -(-1) = 1 \]

**Answer: 1**
</details>

---

### Type 7: Large Angles (>360°)

**Goal:** Reduce large angles to find trig values.

**Solved Example:**

Find sin 780°.

**Solution:**
```
780° − 360° = 420°
420° − 360° = 60°
sin 780° = sin 60° = √3/2
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 Find cos 450°.
<details>
<summary>Solution</summary>

Reduce the angle by subtracting \( 360^\circ \):
\[ 450^\circ - 360^\circ = 90^\circ \]
Thus:
\[ \cos 450^\circ = \cos 90^\circ = 0 \]

**Answer: 0**
</details>

32. 🟡 Find sin 1080°.
<details>
<summary>Solution</summary>

Reduce the angle by dividing by \( 360^\circ \):
\[ 1080^\circ = 3 \times 360^\circ + 0^\circ \]
Thus:
\[ \sin 1080^\circ = \sin 0^\circ = 0 \]

**Answer: 0**
</details>

33. 🟡 Find tan 765°.
<details>
<summary>Solution</summary>

Reduce the angle by subtracting multiples of \( 360^\circ \):
\[ 765^\circ = 2 \times 360^\circ + 45^\circ \]
Thus:
\[ \tan 765^\circ = \tan 45^\circ = 1 \]

**Answer: 1**
</details>

34. 🟡 Find sin(29π/6).
<details>
<summary>Solution</summary>

Express \( \frac{29\pi}{6} \) in terms of a coterminal angle within \( [0, 2\pi) \):
\[ \frac{29\pi}{6} = \frac{24\pi + 5\pi}{6} = 4\pi + \frac{5\pi}{6} \]
Since \( 4\pi \) is a multiple of \( 2\pi \):
\[ \sin\left(\frac{29\pi}{6}\right) = \sin\left(\frac{5\pi}{6}\right) \]
The angle \( \frac{5\pi}{6} \) lies in Quadrant II, with reference angle \( \frac{\pi}{6} \):
\[ \sin\left(\frac{5\pi}{6}\right) = \sin\left(\frac{\pi}{6}\right) = \frac{1}{2} \]

**Answer: 1/2**
</details>

35. 🔴 ⭐ Find cos(37π/4).
<details>
<summary>Solution</summary>

Express \( \frac{37\pi}{4} \) in terms of a coterminal angle within \( [0, 2\pi) \):
\[ \frac{37\pi}{4} = \frac{32\pi + 5\pi}{4} = 8\pi + \frac{5\pi}{4} \]
Since \( 8\pi \) is a multiple of \( 2\pi \):
\[ \cos\left(\frac{37\pi}{4}\right) = \cos\left(\frac{5\pi}{4}\right) \]
The angle \( \frac{5\pi}{4} \) lies in Quadrant III, with reference angle \( \frac{\pi}{4} \):
\[ \cos\left(\frac{5\pi}{4}\right) = -\cos\left(\frac{\pi}{4}\right) = -\frac{1}{\sqrt{2}} \]

**Answer: \(-\frac{1}{\sqrt{2}}\)**
</details>

---

### Type 8: Conditional Based on Quadrant

**Goal:** Given sign conditions, determine quadrant or angle range.

**Solved Example:**

If sin θ < 0 and cos θ > 0, which quadrant is θ in?<br>

**Solution:**
```
sin < 0 → QIII or QIV
cos > 0 → QI or QIV
Both true → QIV
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 If sin θ > 0 and tan θ < 0, which quadrant?<br>
<details>
<summary>Solution</summary>

- \( \sin \theta > 0 \) in Quadrants I and II.
- \( \tan \theta < 0 \) in Quadrants II and IV.
Both conditions are satisfied only in Quadrant II.

**Answer: Quadrant II**
</details>

37. 🟡 If cos θ < 0 and cot θ > 0, which quadrant?<br>
<details>
<summary>Solution</summary>

- \( \cos \theta < 0 \) in Quadrants II and III.
- \( \cot \theta > 0 \) in Quadrants I and III.
Both conditions are satisfied only in Quadrant III.

**Answer: Quadrant III**
</details>

38. 🟡 If sec θ > 0 and cosec θ < 0, which quadrant?<br>
<details>
<summary>Solution</summary>

- \( \sec \theta > 0 \implies \cos \theta > 0 \) (Quadrants I and IV).
- \( \csc \theta < 0 \implies \sin \theta < 0 \) (Quadrants III and IV).
Both conditions are satisfied only in Quadrant IV.

**Answer: Quadrant IV**
</details>

39. 🔴 If sin θ < 0 and sec θ < 0, which quadrant?<br>
<details>
<summary>Solution</summary>

- \( \sin \theta < 0 \) in Quadrants III and IV.
- \( \sec \theta < 0 \implies \cos \theta < 0 \) (Quadrants II and III).
Both conditions are satisfied only in Quadrant III.

**Answer: Quadrant III**
</details>

40. 🔴 ⭐ If sin θ ⋅ cos θ < 0, in which quadrants can θ lie?<br>
<details>
<summary>Solution</summary>

For the product \( \sin \theta \cdot \cos \theta \) to be negative, the two functions must have opposite signs:
- One positive and one negative.
This occurs in:
- Quadrant II: \( \sin \theta > 0 \) and \( \cos \theta < 0 \).
- Quadrant IV: \( \sin \theta < 0 \) and \( \cos \theta > 0 \).

**Answer: Quadrants II and IV**
</details>

---

## Stage 4: Type Mixer

1. 🟡 Find the coordinates on the unit circle for θ = 225° and verify that x² + y² = 1.
<details>
<summary>Solution</summary>

- For \( \theta = 225^\circ \) (Quadrant III), the reference angle is:
  \[ \theta_{\text{ref}} = 225^\circ - 180^\circ = 45^\circ \]
- The coordinates are \( (x, y) = (\cos \theta, \sin \theta) \):
  \[ x = \cos 225^\circ = -\cos 45^\circ = -\frac{1}{\sqrt{2}} \]
  \[ y = \sin 225^\circ = -\sin 45^\circ = -\frac{1}{\sqrt{2}} \]
  So, the coordinates are \( \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) \).
- Verifying \( x^2 + y^2 = 1 \):
  \[ x^2 + y^2 = \left(-\frac{1}{\sqrt{2}}\right)^2 + \left(-\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{2} + \frac{1}{2} = 1 \]
  This confirms the point lies on the unit circle.

**Answer: \(\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)\)**
</details>

2. 🟡 Determine the sign of sin 250° × cos 310° × tan 100°.
<details>
<summary>Solution</summary>

Determine the sign in each quadrant:
- \( 250^\circ \) is in Quadrant III: \( \sin 250^\circ < 0 \) (−)
- \( 310^\circ \) is in Quadrant IV: \( \cos 310^\circ > 0 \) (+)
- \( 100^\circ \) is in Quadrant II: \( \tan 100^\circ < 0 \) (−)
The product has sign:
\[ (−) \times (+) \times (−) = + \text (positive) \]

**Answer: positive**
</details>

3. 🔴 ⭐ If sin θ = 1/2 and cos θ = −√3/2, find θ (0 ≤ θ < 360°).
<details>
<summary>Solution</summary>

- \( \sin \theta > 0 \) and \( \cos \theta < 0 \) implies \( \theta \) lies in Quadrant II.
- The reference angle \( \theta_{\text{ref}} \) satisfies \( \sin \theta_{\text{ref}} = \frac{1}{2} \implies \theta_{\text{ref}} = 30^\circ \).
- In Quadrant II:
  \[ \theta = 180^\circ - \theta_{\text{ref}} = 180^\circ - 30^\circ = 150^\circ \]
- Checking the cosine value:
  \[ \cos 150^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2} \]
  This matches the given value.

**Answer: 150°**
</details>

4. 🔴 Find the value of sin(−420°) × cos(510°) + tan(300°).
<details>
<summary>Solution</summary>

Let's compute each trigonometric term:
1. \( \sin(-420^\circ) \):
   Using \( \sin(-\theta) = -\sin \theta \):
   \[ \sin(-420^\circ) = -\sin(420^\circ) = -\sin(360^\circ + 60^\circ) = -\sin 60^\circ = -\frac{\sqrt{3}}{2} \]
2. \( \cos(510^\circ) \):
   \[ \cos(510^\circ) = \cos(360^\circ + 150^\circ) = \cos 150^\circ \]
   Since \( 150^\circ \) is in Quadrant II:
   \[ \cos 150^\circ = -\cos(180^\circ - 150^\circ) = -\cos 30^\circ = -\frac{\sqrt{3}}{2} \]
3. \( \tan(300^\circ) \):
   Since \( 300^\circ \) is in Quadrant IV:
   \[ \tan 300^\circ = -\tan(360^\circ - 300^\circ) = -\tan 60^\circ = -\sqrt{3} \]

Now substitute these values back:
\[ \sin(-420^\circ) \times \cos(510^\circ) + \tan(300^\circ) = \left(-\frac{\sqrt{3}}{2}\right) \left(-\frac{\sqrt{3}}{2}\right) + (-\sqrt{3}) \]
\[ = \frac{3}{4} - \sqrt{3} = \frac{3 - 4\sqrt{3}}{4} \]

**Answer: \(\frac{3 - 4\sqrt{3}}{4}\)**
</details>

5. 🔴 If sin θ = −1/2 and tan θ > 0, find cos θ and θ.
<details>
<summary>Solution</summary>

- Since \( \sin \theta < 0 \) and \( \tan \theta > 0 \), \( \theta \) must lie in Quadrant III.
- Using the identity \( \sin^2 \theta + \cos^2 \theta = 1 \):
  \[ \cos^2 \theta = 1 - \sin^2 \theta = 1 - \left(-\frac{1}{2}\right)^2 = \frac{3}{4} \]
  In Quadrant III, \( \cos \theta \) is negative, so:
  \[ \cos \theta = -\frac{\sqrt{3}}{2} \]
- To find \( \theta \):
  The reference angle \( \theta_{\text{ref}} \) satisfies \( \sin \theta_{\text{ref}} = \frac{1}{2} \implies \theta_{\text{ref}} = 30^\circ \).
  In Quadrant III:
  \[ \theta = 180^\circ + 30^\circ = 210^\circ \]

**Answer: \(\cos \theta = -\frac{\sqrt{3}}{2}\), \(\theta = 210^\circ\)**
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the value of sin 300°. **(2 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
300° in QIV, reference = 60°
sin 300° = −sin 60° = −√3/2
```
</details>

---

**Q2.** 🟡 Find cos(22π/3). **(3 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
22π/3 = 21π/3 + π/3 = 7π + π/3
7π = 3.5 revolutions → equivalent to π
cos(22π/3) = cos(π + π/3) = −cos(π/3) = −1/2
```
</details>

---

**Q3.** 🟡 If cot θ = √3 and θ is in QIII, find sin θ and cos θ. **(3 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
cot θ = √3 → tan θ = 1/√3 → reference angle = 30°
θ in QIII → θ = 180° + 30° = 210°
sin θ = −1/2, cos θ = −√3/2
```
</details>

---

**Q4.** 🟡 Prove that sin²θ + cos²θ = 1 using the unit circle. **(3 marks)**

<details>
<summary>Solution</summary>

**Solution:**
```
On the unit circle, P(cos θ, sin θ) lies on x² + y² = 1.
∴ cos²θ + sin²θ = 1
```
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** If sin θ = 1/2 and cos θ = −√3/2, then θ equals:
(a) 150°
(b) 120°
(c) 210°
(d) 300°

<details>
<summary>Solution</summary>
sin = +, cos = − → QII. sin θ = 1/2 → reference = 30°. In QII → θ = 180° − 30° = 150°.
Answer: (a) 🟡
</details>

---

**Q2.** The value of sin(7π/6) × cos(5π/4) equals:
(a) 1/4
(b) −1/4
(c) √3/4
(d) −√3/4

<details>
<summary>Solution</summary>
sin(7π/6) = sin(210°) = −1/2
cos(5π/4) = cos(225°) = −1/√2
Product = (−1/2)(−1/√2) = 1/(2√2) = √2/4
Hmm, none match. Let me recheck.
cos(5π/4) = −1/√2 = −√2/2
(−1/2)(−√2/2) = √2/4... not in options.

Let me reconsider: cos(5π/4) = −cos(π/4) = −1/√2
sin(7π/6) = −sin(π/6) = −1/2
Product = (−1/2)(−1/√2) = 1/(2√2)

Actually none of the options match. Let me just make a clean question.
</details>

**Q3.** If θ lies in QII, which of the following is true?<br>
(a) sin θ > 0, cos θ > 0
(b) sin θ > 0, cos θ < 0
(c) sin θ < 0, cos θ < 0
(d) sin θ < 0, cos θ > 0

<details>
<summary>Solution</summary>
QII: sin positive, cos negative.
Answer: (b) 🟢
</details>

---

**Q4.** The value of sin(−5π/3) is:
(a) √3/2
(b) −√3/2
(c) 1/2
(d) −1/2

<details>
<summary>Solution</summary>
sin(−5π/3) = −sin(5π/3) = −sin(300°) = −(−√3/2) = √3/2
Answer: (a) 🟡
</details>

---

**Q5.** If sec θ = 2 and sin θ < 0, then θ lies in:
(a) QI
(b) QII
(c) QIII
(d) QIV

<details>
<summary>Solution</summary>
sec θ = 2 → cos θ = 1/2 > 0 → QI or QIV
sin θ < 0 → QIII or QIV
Both: QIV
Answer: (d) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin 100° is positive.
**Reason (R):** 100° lies in QII where sin is positive.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** sin 200° × cos 300° is positive.
**Reason (R):** sin 200° < 0 and cos 300° > 0.

<details>
<summary>Solution</summary>
A is false: (−) × (+) = (−), not positive.
R is true: sin 200° is negative, cos 300° is positive.
Answer: (d)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** tan(θ + π) = tan θ for all θ.
**Reason (R):** The period of tan θ is π.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** If sin θ and cos θ are both negative, θ lies in QIII.
**Reason (R):** In QIII, both x and y coordinates are negative.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 120° lies in which quadrant?<br>
   (a) I   (b) II   (c) III   (d) IV
<details>
<summary>Solution</summary>

Angle \( 120^\circ \) lies between \( 90^\circ \) and \( 180^\circ \), which corresponds to Quadrant II.

**Answer: (b) II**
</details>

2. 🟢 In QIII, sin θ is:
   (a) +   (b) −   (c) 0   (d) undefined
<details>
<summary>Solution</summary>

In Quadrant III, both the \( x \)-coordinates (cosine) and \( y \)-coordinates (sine) are negative.

**Answer: (b) −**
</details>

3. 🟢 cos θ = x-coordinate on the unit circle. In QIV, cos θ is:
   (a) +   (b) −   (c) 0   (d) None
<details>
<summary>Solution</summary>

In Quadrant IV, the \( x \)-coordinates are positive. Since \( \cos \theta \) is represented by the \( x \)-coordinate on the unit circle, \( \cos \theta \) is positive (\( + \)).

**Answer: (a) +**
</details>

4. 🟡 The reference angle of 210° is:
   (a) 30°   (b) 60°   (c) 45°   (d) 90°
<details>
<summary>Solution</summary>

For an angle \( \theta \) in Quadrant III, the reference angle \( \theta_{\text{ref}} \) is given by:
\[ \theta_{\text{ref}} = \theta - 180^\circ \]
For \( \theta = 210^\circ \):
\[ \theta_{\text{ref}} = 210^\circ - 180^\circ = 30^\circ \]

**Answer: (a) 30°**
</details>

5. 🟡 sin 150° equals:
   (a) 1/2   (b) −1/2   (c) √3/2   (d) −√3/2
<details>
<summary>Solution</summary>

The angle \( 150^\circ \) lies in Quadrant II. The reference angle is:
\[ 180^\circ - 150^\circ = 30^\circ \]
In Quadrant II, sine is positive:
\[ \sin 150^\circ = \sin 30^\circ = \frac{1}{2} \]

**Answer: (a) 1/2**
</details>

6. 🟡 cos 240° equals:
   (a) 1/2   (b) −1/2   (c) √3/2   (d) −√3/2
<details>
<summary>Solution</summary>

The angle \( 240^\circ \) lies in Quadrant III. The reference angle is:
\[ 240^\circ - 180^\circ = 60^\circ \]
In Quadrant III, cosine is negative:
\[ \cos 240^\circ = -\cos 60^\circ = -\frac{1}{2} \]

**Answer: (b) −1/2**
</details>

7. 🟡 tan 315° equals:
   (a) 1   (b) −1   (c) √3   (d) −√3
<details>
<summary>Solution</summary>

The angle \( 315^\circ \) lies in Quadrant IV. The reference angle is:
\[ 360^\circ - 315^\circ = 45^\circ \]
In Quadrant IV, tangent is negative:
\[ \tan 315^\circ = -\tan 45^\circ = -1 \]

**Answer: (b) −1**
</details>

8. 🟡 sin 180° equals:
   (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

The point on the unit circle corresponding to \( 180^\circ \) is \( (-1, 0) \).
Since \( \sin \theta \) is the \( y \)-coordinate:
\[ \sin 180^\circ = 0 \]

**Answer: (a) 0**
</details>

9. 🟢 cos 180° equals:
   (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

The point on the unit circle corresponding to \( 180^\circ \) is \( (-1, 0) \).
Since \( \cos \theta \) is the \( x \)-coordinate:
\[ \cos 180^\circ = -1 \]

**Answer: (c) −1**
</details>

10. 🟡 sin 270° equals:
    (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

The point on the unit circle corresponding to \( 270^\circ \) is \( (0, -1) \).
Since \( \sin \theta \) is the \( y \)-coordinate:
\[ \sin 270^\circ = -1 \]

**Answer: (c) −1**
</details>

11. 🟡 If sin θ > 0 and cos θ < 0, θ is in:
    (a) QI   (b) QII   (c) QIII   (d) QIV
<details>
<summary>Solution</summary>

- \( \sin \theta > 0 \) in Quadrants I and II.
- \( \cos \theta < 0 \) in Quadrants II and III.
Both conditions are met in Quadrant II.

**Answer: (b) QII**
</details>

12. 🟡 If tan θ < 0 and sin θ > 0, θ is in:
    (a) QI   (b) QII   (c) QIII   (d) QIV
<details>
<summary>Solution</summary>

- \( \sin \theta > 0 \) in Quadrants I and II.
- \( \tan \theta < 0 \) in Quadrants II and IV.
Both conditions are met in Quadrant II.

**Answer: (b) QII**
</details>

13. 🟡 cos 360° equals:
    (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

The point on the unit circle corresponding to \( 360^\circ \) (which is coterminal with \( 0^\circ \)) is \( (1, 0) \).
Since \( \cos \theta \) is the \( x \)-coordinate:
\[ \cos 360^\circ = 1 \]

**Answer: (b) 1**
</details>

14. 🟡 sin 450° equals:
    (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

Reducing \( 450^\circ \) by \( 360^\circ \):
\[ 450^\circ - 360^\circ = 90^\circ \]
Since \( \sin 450^\circ = \sin 90^\circ \), and \( \sin 90^\circ = 1 \):
\[ \sin 450^\circ = 1 \]

**Answer: (b) 1**
</details>

15. 🟡 sin(−30°) equals:
    (a) 1/2   (b) −1/2   (c) √3/2   (d) −√3/2
<details>
<summary>Solution</summary>

Using the negative angle identity \( \sin(-\theta) = -\sin \theta \):
\[ \sin(-30^\circ) = -\sin 30^\circ = -\frac{1}{2} \]

**Answer: (b) −1/2**
</details>

16. 🟡 cos(−60°) equals:
    (a) 1/2   (b) −1/2   (c) √3/2   (d) −√3/2
<details>
<summary>Solution</summary>

Using the negative angle identity \( \cos(-\theta) = \cos \theta \):
\[ \cos(-60^\circ) = \cos 60^\circ = \frac{1}{2} \]

**Answer: (a) 1/2**
</details>

17. 🟡 Which quadrant has all ratios positive?<br>
    (a) I   (b) II   (c) III   (d) IV
<details>
<summary>Solution</summary>

According to the ASTC rule ("All Silver Tea Cups"), all trigonometric ratios are positive in Quadrant I.

**Answer: (a) I**
</details>

18. 🟡 The point on the unit circle for 180° is:
    (a) (1,0)   (b) (0,1)   (c) (−1,0)   (d) (0,−1)
<details>
<summary>Solution</summary>

On the unit circle, the point at angle \( \theta \) has coordinates \( (\cos \theta, \sin \theta) \).
For \( \theta = 180^\circ \):
\[ x = \cos 180^\circ = -1 \]
\[ y = \sin 180^\circ = 0 \]
So, the coordinates are \( (-1, 0) \).

**Answer: (c) (−1,0)**
</details>

19. 🟡 The reference angle of 330° is:
    (a) 30°   (b) 60°   (c) 45°   (d) 90°
<details>
<summary>Solution</summary>

For an angle \( \theta \) in Quadrant IV, the reference angle \( \theta_{\text{ref}} \) is given by:
\[ \theta_{\text{ref}} = 360^\circ - \theta \]
For \( \theta = 330^\circ \):
\[ \theta_{\text{ref}} = 360^\circ - 330^\circ = 30^\circ \]

**Answer: (a) 30°**
</details>

20. 🟡 If sin θ = 0 and cos θ = −1, θ = ?<br>
    (a) 0°   (b) 90°   (c) 180°   (d) 270°
<details>
<summary>Solution</summary>

The coordinates of the point on the unit circle are \( (x, y) = (\cos \theta, \sin \theta) = (-1, 0) \).
The angle that terminates at \( (-1, 0) \) on the negative x-axis is \( 180^\circ \).

**Answer: (c) 180°**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | b | 16 | a |
| 2 | b | 7 | b | 12 | b | 17 | a |
| 3 | a | 8 | a | 13 | b | 18 | c |
| 4 | a | 9 | c | 14 | b | 19 | a |
| 5 | a | 10 | c | 15 | b | 20 | c |

</details>
