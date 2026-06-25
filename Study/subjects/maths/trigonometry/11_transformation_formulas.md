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
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = 5x \) and \( D = x \).
- \( \frac{C+D}{2} = \frac{5x+x}{2} = 3x \)
- \( \frac{C-D}{2} = \frac{5x-x}{2} = 2x \)

Substituting these values:
\[ \sin 5x + \sin x = 2 \sin 3x \cos 2x \]
</details>

2. 🟢 Express cos 8θ − cos 2θ as a product.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C - \cos D = -2 \sin\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \]

Here, \( C = 8\theta \) and \( D = 2\theta \).
- \( \frac{C+D}{2} = \frac{8\theta+2\theta}{2} = 5\theta \)
- \( \frac{C-D}{2} = \frac{8\theta-2\theta}{2} = 3\theta \)

Substituting these values:
\[ \cos 8\theta - \cos 2\theta = -2 \sin 5\theta \sin 3\theta \]
</details>

3. 🟢 Express sin 6x − sin 2x as a product.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C - \sin D = 2 \cos\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \]

Here, \( C = 6x \) and \( D = 2x \).
- \( \frac{C+D}{2} = \frac{6x+2x}{2} = 4x \)
- \( \frac{C-D}{2} = \frac{6x-2x}{2} = 2x \)

Substituting these values:
\[ \sin 6x - \sin 2x = 2 \cos 4x \sin 2x \]
</details>

4. 🟢 Express cos 5x + cos 3x as a product.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = 5x \) and \( D = 3x \).
- \( \frac{C+D}{2} = \frac{5x+3x}{2} = 4x \)
- \( \frac{C-D}{2} = \frac{5x-3x}{2} = x \)

Substituting these values:
\[ \cos 5x + \cos 3x = 2 \cos 4x \cos x \]
</details>

5. 🟡 Express sin 50° + sin 10° as a product and evaluate.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = 50^\circ \) and \( D = 10^\circ \).
- \( \frac{C+D}{2} = \frac{50^\circ+10^\circ}{2} = 30^\circ \)
- \( \frac{C-D}{2} = \frac{50^\circ-10^\circ}{2} = 20^\circ \)

Substituting these values:
\[ \sin 50^\circ + \sin 10^\circ = 2 \sin 30^\circ \cos 20^\circ \]

Since \( \sin 30^\circ = \frac{1}{2} \), we evaluate it as:
\[ 2 \cdot \frac{1}{2} \cdot \cos 20^\circ = \cos 20^\circ \]
</details>

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
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \]

Here, \( A = 4x \) and \( B = 2x \).
- \( A+B = 4x+2x = 6x \)
- \( A-B = 4x-2x = 2x \)

Substituting these:
\[ 2 \sin 4x \cos 2x = \sin 6x + \sin 2x \]
</details>

7. 🟢 Express 2 cos 7x cos 3x as a sum.
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \cos A \cos B = \cos(A+B) + \cos(A-B) \]

Here, \( A = 7x \) and \( B = 3x \).
- \( A+B = 7x+3x = 10x \)
- \( A-B = 7x-3x = 4x \)

Substituting these:
\[ 2 \cos 7x \cos 3x = \cos 10x + \cos 4x \]
</details>

8. 🟢 Express 2 sin 5x sin 2x as a sum.
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \sin A \sin B = \cos(A-B) - \cos(A+B) \]

Here, \( A = 5x \) and \( B = 2x \).
- \( A-B = 5x-2x = 3x \)
- \( A+B = 5x+2x = 7x \)

Substituting these:
\[ 2 \sin 5x \sin 2x = \cos 3x - \cos 7x \]
</details>

9. 🟡 Express 2 cos 75° sin 15° as a sum and evaluate.
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \cos A \sin B = \sin(A+B) - \sin(A-B) \]

Here, \( A = 75^\circ \) and \( B = 15^\circ \).
- \( A+B = 75^\circ + 15^\circ = 90^\circ \)
- \( A-B = 75^\circ - 15^\circ = 60^\circ \)

Substituting these:
\[ 2 \cos 75^\circ \sin 15^\circ = \sin 90^\circ - \sin 60^\circ \]

Evaluating the standard values:
- \( \sin 90^\circ = 1 \)
- \( \sin 60^\circ = \frac{\sqrt{3}}{2} \)

Therefore:
\[ 2 \cos 75^\circ \sin 15^\circ = 1 - \frac{\sqrt{3}}{2} = \frac{2-\sqrt{3}}{2} \]
</details>

10. 🟡 Express 2 sin 105° cos 75° as a sum.
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \]

Here, \( A = 105^\circ \) and \( B = 75^\circ \).
- \( A+B = 105^\circ + 75^\circ = 180^\circ \)
- \( A-B = 105^\circ - 75^\circ = 30^\circ \)

Substituting these:
\[ 2 \sin 105^\circ \cos 75^\circ = \sin 180^\circ + \sin 30^\circ \]
</details>

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
<details>
<summary>Solution</summary>

Apply the sum-to-product formulas to the numerator and denominator:
- Numerator: \( \sin 5x - \sin 3x = 2 \cos\left(\frac{5x+3x}{2}\right) \sin\left(\frac{5x-3x}{2}\right) = 2 \cos 4x \sin x \)
- Denominator: \( \cos 5x + \cos 3x = 2 \cos\left(\frac{5x+3x}{2}\right) \cos\left(\frac{5x-3x}{2}\right) = 2 \cos 4x \cos x \)

Taking the ratio:
\[ \frac{\sin 5x - \sin 3x}{\cos 5x + \cos 3x} = \frac{2 \cos 4x \sin x}{2 \cos 4x \cos x} = \frac{\sin x}{\cos x} = \tan x \]
</details>

12. 🟡 Simplify (cos 6x + cos 4x)/(sin 6x − sin 4x).
<details>
<summary>Solution</summary>

Apply the sum-to-product formulas to the numerator and denominator:
- Numerator: \( \cos 6x + \cos 4x = 2 \cos\left(\frac{6x+4x}{2}\right) \cos\left(\frac{6x-4x}{2}\right) = 2 \cos 5x \cos x \)
- Denominator: \( \sin 6x - \sin 4x = 2 \cos\left(\frac{6x+4x}{2}\right) \sin\left(\frac{6x-4x}{2}\right) = 2 \cos 5x \sin x \)

Taking the ratio:
\[ \frac{\cos 6x + \cos 4x}{\sin 6x - \sin 4x} = \frac{2 \cos 5x \cos x}{2 \cos 5x \sin x} = \frac{\cos x}{\sin x} = \cot x \]
</details>

13. 🟡 Simplify (sin A + sin 3A)/(cos A + cos 3A).
<details>
<summary>Solution</summary>

Rearrange the terms and apply the sum-to-product formulas:
- Numerator: \( \sin 3A + \sin A = 2 \sin\left(\frac{3A+A}{2}\right) \cos\left(\frac{3A-A}{2}\right) = 2 \sin 2A \cos A \)
- Denominator: \( \cos 3A + \cos A = 2 \cos\left(\frac{3A+A}{2}\right) \cos\left(\frac{3A-A}{2}\right) = 2 \cos 2A \cos A \)

Taking the ratio:
\[ \frac{\sin A + \sin 3A}{\cos A + \cos 3A} = \frac{2 \sin 2A \cos A}{2 \cos 2A \cos A} = \frac{\sin 2A}{\cos 2A} = \tan 2A \]
</details>

14. 🔴 Simplify (sin 7θ − sin 3θ − sin 5θ + sin θ)/(cos 7θ − cos 3θ − cos 5θ + cos θ).
<details>
<summary>Solution</summary>

Let's group the terms to make simplification easier:
- **Numerator:**
  \[ (\sin 7\theta + \sin \theta) - (\sin 5\theta + \sin 3\theta) \]
  Applying \( \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  - \( \sin 7\theta + \sin \theta = 2 \sin 4\theta \cos 3\theta \)
  - \( \sin 5\theta + \sin 3\theta = 2 \sin 4\theta \cos \theta \)
  Thus, Numerator = \( 2 \sin 4\theta \cos 3\theta - 2 \sin 4\theta \cos \theta = 2 \sin 4\theta (\cos 3\theta - \cos \theta) \).

- **Denominator:**
  \[ (\cos 7\theta + \cos \theta) - (\cos 5\theta + \cos 3\theta) \]
  Applying \( \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  - \( \cos 7\theta + \cos \theta = 2 \cos 4\theta \cos 3\theta \)
  - \( \cos 5\theta + \cos 3\theta = 2 \cos 4\theta \cos \theta \)
  Thus, Denominator = \( 2 \cos 4\theta \cos 3\theta - 2 \cos 4\theta \cos \theta = 2 \cos 4\theta (\cos 3\theta - \cos \theta) \).

- **Ratio:**
  \[ \frac{2 \sin 4\theta (\cos 3\theta - \cos \theta)}{2 \cos 4\theta (\cos 3\theta - \cos \theta)} = \frac{\sin 4\theta}{\cos 4\theta} = \tan 4\theta \]
</details>

15. 🔴 ⭐ Show that (sin 2x + sin 5x − sin x)/(cos 2x + cos 5x + cos x) = tan 2x.
<details>
<summary>Solution</summary>

Let's group the first and third terms of both numerator and denominator:

- **Numerator:**
  \[ \sin 5x - \sin x + \sin 2x \]
  Using the formula \( \sin C - \sin D = 2 \cos\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \):
  - \( \sin 5x - \sin x = 2 \cos 3x \sin 2x \)
  Thus, Numerator = \( 2 \cos 3x \sin 2x + \sin 2x = \sin 2x (2 \cos 3x + 1) \).

- **Denominator:**
  \[ \cos 5x + \cos x + \cos 2x \]
  Using the formula \( \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  - \( \cos 5x + \cos x = 2 \cos 3x \cos 2x \)
  Thus, Denominator = \( 2 \cos 3x \cos 2x + \cos 2x = \cos 2x (2 \cos 3x + 1) \).

- **Ratio:**
  \[ \text{LHS} = \frac{\sin 2x (2 \cos 3x + 1)}{\cos 2x (2 \cos 3x + 1)} = \frac{\sin 2x}{\cos 2x} = \tan 2x = \text{RHS} \]
</details>

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
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin 7x - \sin x = 2 \cos 4x \sin 3x = 0 \]

This implies either \( \cos 4x = 0 \) or \( \sin 3x = 0 \).

- **Case 1: \( \sin 3x = 0 \)**
  For \( 0^\circ \le x \le 360^\circ \), the range of \( 3x \) is \( 0^\circ \le 3x \le 1080^\circ \).
  \[ 3x = 0^\circ, 180^\circ, 360^\circ, 540^\circ, 720^\circ, 900^\circ, 1080^\circ \]
  \[ x = 0^\circ, 60^\circ, 120^\circ, 180^\circ, 240^\circ, 300^\circ, 360^\circ \]

- **Case 2: \( \cos 4x = 0 \)**
  For \( 0^\circ \le x \le 360^\circ \), the range of \( 4x \) is \( 0^\circ \le 4x \le 1440^\circ \).
  \[ 4x = 90^\circ, 270^\circ, 450^\circ, 630^\circ, 810^\circ, 990^\circ, 1170^\circ, 1350^\circ \]
  \[ x = 22.5^\circ, 67.5^\circ, 112.5^\circ, 157.5^\circ, 202.5^\circ, 247.5^\circ, 292.5^\circ, 337.5^\circ \]

**Combined Solutions:**
\[ x = 0^\circ, 22.5^\circ, 60^\circ, 67.5^\circ, 112.5^\circ, 120^\circ, 157.5^\circ, 180^\circ, 202.5^\circ, 240^\circ, 247.5^\circ, 292.5^\circ, 300^\circ, 337.5^\circ, 360^\circ \]
</details>

17. 🟡 Solve cos 5x + cos 3x = 0 for 0° ≤ x ≤ 180°.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos 5x + \cos 3x = 2 \cos 4x \cos x = 0 \]

This implies either \( \cos 4x = 0 \) or \( \cos x = 0 \).

- **Case 1: \( \cos x = 0 \)**
  For \( 0^\circ \le x \le 180^\circ \):
  \[ x = 90^\circ \]

- **Case 2: \( \cos 4x = 0 \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 4x \) is \( 0^\circ \le 4x \le 720^\circ \).
  \[ 4x = 90^\circ, 270^\circ, 450^\circ, 630^\circ \]
  \[ x = 22.5^\circ, 67.5^\circ, 112.5^\circ, 157.5^\circ \]

**Combined Solutions:**
\[ x = 22.5^\circ, 67.5^\circ, 90^\circ, 112.5^\circ, 157.5^\circ \]
</details>

18. 🟡 Solve sin x + sin 3x + sin 5x = 0 for 0° ≤ x ≤ 180°.
<details>
<summary>Solution</summary>

Group the first and third terms:
\[ (\sin 5x + \sin x) + \sin 3x = 0 \]

Apply the sum-to-product formula:
\[ 2 \sin 3x \cos 2x + \sin 3x = 0 \]
\[ \sin 3x (2 \cos 2x + 1) = 0 \]

This gives two cases:

- **Case 1: \( \sin 3x = 0 \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 3x \) is \( 0^\circ \le 3x \le 540^\circ \).
  \[ 3x = 0^\circ, 180^\circ, 360^\circ, 540^\circ \]
  \[ x = 0^\circ, 60^\circ, 120^\circ, 180^\circ \]

- **Case 2: \( 2 \cos 2x + 1 = 0 \Rightarrow \cos 2x = -\frac{1}{2} \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 2x \) is \( 0^\circ \le 2x \le 360^\circ \).
  \[ 2x = 120^\circ, 240^\circ \]
  \[ x = 60^\circ, 120^\circ \] (which are already in the first list)

**Combined Solutions:**
\[ x = 0^\circ, 60^\circ, 120^\circ, 180^\circ \]
</details>

19. 🔴 ⭐ Solve cos 2x + cos 4x + cos 6x = 0 for 0° ≤ x ≤ 180°.
<details>
<summary>Solution</summary>

Group the first and third terms:
\[ (\cos 6x + \cos 2x) + \cos 4x = 0 \]

Apply the sum-to-product formula:
\[ 2 \cos 4x \cos 2x + \cos 4x = 0 \]
\[ \cos 4x (2 \cos 2x + 1) = 0 \]

This gives two cases:

- **Case 1: \( \cos 4x = 0 \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 4x \) is \( 0^\circ \le 4x \le 720^\circ \).
  \[ 4x = 90^\circ, 270^\circ, 450^\circ, 630^\circ \]
  \[ x = 22.5^\circ, 67.5^\circ, 112.5^\circ, 157.5^\circ \]

- **Case 2: \( 2 \cos 2x + 1 = 0 \Rightarrow \cos 2x = -\frac{1}{2} \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 2x \) is \( 0^\circ \le 2x \le 360^\circ \).
  \[ 2x = 120^\circ, 240^\circ \]
  \[ x = 60^\circ, 120^\circ \]

**Combined Solutions:**
\[ x = 22.5^\circ, 60^\circ, 67.5^\circ, 112.5^\circ, 120^\circ, 157.5^\circ \]
</details>

20. 🔴 Solve sin x + sin 3x = cos x + cos 3x for 0° ≤ x ≤ 360°.
<details>
<summary>Solution</summary>

Apply the sum-to-product formulas to both sides of the equation:
- LHS: \( \sin 3x + \sin x = 2 \sin 2x \cos x \)
- RHS: \( \cos 3x + \cos x = 2 \cos 2x \cos x \)

The equation becomes:
\[ 2 \sin 2x \cos x = 2 \cos 2x \cos x \]
\[ 2 \cos x (\sin 2x - \cos 2x) = 0 \]

This leads to two cases:

- **Case 1: \( \cos x = 0 \)**
  For \( 0^\circ \le x \le 360^\circ \):
  \[ x = 90^\circ, 270^\circ \]

- **Case 2: \( \sin 2x - \cos 2x = 0 \Rightarrow \tan 2x = 1 \)**
  For \( 0^\circ \le x \le 360^\circ \), the range of \( 2x \) is \( 0^\circ \le 2x \le 720^\circ \).
  \[ 2x = 45^\circ, 225^\circ, 405^\circ, 585^\circ \]
  \[ x = 22.5^\circ, 112.5^\circ, 202.5^\circ, 292.5^\circ \]

**Combined Solutions:**
\[ x = 22.5^\circ, 90^\circ, 112.5^\circ, 202.5^\circ, 270^\circ, 292.5^\circ \]
</details>

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
<details>
<summary>Solution</summary>

Let's simplify the LHS using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Setting \( C = 50^\circ \) and \( D = 10^\circ \):
\[ \sin 50^\circ + \sin 10^\circ = 2 \sin 30^\circ \cos 20^\circ \]

Since \( \sin 30^\circ = \frac{1}{2} \), substituting this gives:
\[ 2 \cdot \frac{1}{2} \cdot \cos 20^\circ = \cos 20^\circ \]

Thus:
\[ \text{LHS} = 2 \sin 30^\circ \cos 20^\circ = \cos 20^\circ = \text{RHS} \]
Hence, proved.
</details>

22. 🟡 Prove that (sin 5x − 2 sin 3x + sin x)/(cos 5x − cos x) = tan x.
<details>
<summary>Solution</summary>

Let's group the terms in the numerator:
- **Numerator:**
  \[ (\sin 5x + \sin x) - 2 \sin 3x \]
  Using the formula \( \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  \[ 2 \sin 3x \cos 2x - 2 \sin 3x = 2 \sin 3x (\cos 2x - 1) \]

- **Denominator:**
  \[ \cos 5x - \cos x \]
  Using the formula \( \cos C - \cos D = -2 \sin\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \):
  \[ -2 \sin 3x \sin 2x \]

- **Ratio:**
  \[ \text{LHS} = \frac{2 \sin 3x (\cos 2x - 1)}{-2 \sin 3x \sin 2x} = \frac{1 - \cos 2x}{\sin 2x} \]
  Using half-angle and double-angle formulas:
  - \( 1 - \cos 2x = 2 \sin^2 x \)
  - \( \sin 2x = 2 \sin x \cos x \)
  Substituting these:
  \[ \text{LHS} = \frac{2 \sin^2 x}{2 \sin x \cos x} = \frac{\sin x}{\cos x} = \tan x = \text{RHS} \]
Hence, proved.
</details>

23. 🟡 Prove that cos 20° + cos 100° + cos 140° = 0.
<details>
<summary>Solution</summary>

Rearrange the terms:
\[ (\cos 100^\circ + \cos 20^\circ) + \cos 140^\circ \]

Apply the sum-to-product formula on the first two terms:
\[ 2 \cos\left(\frac{100^\circ + 20^\circ}{2}\right) \cos\left(\frac{100^\circ - 20^\circ}{2}\right) + \cos 140^\circ \]
\[ = 2 \cos 60^\circ \cos 40^\circ + \cos 140^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ = 2 \cdot \frac{1}{2} \cdot \cos 40^\circ + \cos 140^\circ = \cos 40^\circ + \cos 140^\circ \]

Using the identity \( \cos(180^\circ - \theta) = -\cos\theta \):
\[ \cos 140^\circ = \cos(180^\circ - 40^\circ) = -\cos 40^\circ \]

Thus:
\[ \text{LHS} = \cos 40^\circ - \cos 40^\circ = 0 = \text{RHS} \]
Hence, proved.
</details>

24. 🔴 ⭐ Prove that sin 10° + sin 20° + sin 40° + sin 50° = sin 70° + sin 80°.
<details>
<summary>Solution</summary>

Let's group the terms on the LHS:
\[ (\sin 50^\circ + \sin 10^\circ) + (\sin 40^\circ + \sin 20^\circ) \]

Apply the sum-to-product formula to each group:
- \( \sin 50^\circ + \sin 10^\circ = 2 \sin 30^\circ \cos 20^\circ = 2 \cdot \frac{1}{2} \cdot \cos 20^\circ = \cos 20^\circ \)
- \( \sin 40^\circ + \sin 20^\circ = 2 \sin 30^\circ \cos 10^\circ = 2 \cdot \frac{1}{2} \cdot \cos 10^\circ = \cos 10^\circ \)

Thus, the LHS becomes:
\[ \text{LHS} = \cos 20^\circ + \cos 10^\circ \]

Now let's rewrite the RHS using co-function identities \( \sin(90^\circ - \theta) = \cos\theta \):
- \( \sin 70^\circ = \sin(90^\circ - 20^\circ) = \cos 20^\circ \)
- \( \sin 80^\circ = \sin(90^\circ - 10^\circ) = \cos 10^\circ \)

Thus:
\[ \text{RHS} = \cos 20^\circ + \cos 10^\circ \]

Since LHS = RHS, the identity is proved.
</details>

25. 🔴 Prove that cos(π/7) + cos(3π/7) + cos(5π/7) = 1/2.
<details>
<summary>Solution</summary>

Let \( S = \cos\left(\frac{\pi}{7}\right) + \cos\left(\frac{3\pi}{7}\right) + \cos\left(\frac{5\pi}{7}\right) \).

Multiply both sides by \( 2 \sin\left(\frac{\pi}{7}\right) \):
\[ 2 \sin\left(\frac{\pi}{7}\right) S = 2 \sin\left(\frac{\pi}{7}\right)\cos\left(\frac{\pi}{7}\right) + 2 \sin\left(\frac{\pi}{7}\right)\cos\left(\frac{3\pi}{7}\right) + 2 \sin\left(\frac{\pi}{7}\right)\cos\left(\frac{5\pi}{7}\right) \]

Apply product-to-sum formula \( 2 \cos A \sin B = \sin(A+B) - \sin(A-B) \):
- \( 2 \sin\left(\frac{\pi}{7}\right)\cos\left(\frac{\pi}{7}\right) = \sin\left(\frac{2\pi}{7}\right) \)
- \( 2 \cos\left(\frac{3\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) = \sin\left(\frac{4\pi}{7}\right) - \sin\left(\frac{2\pi}{7}\right) \)
- \( 2 \cos\left(\frac{5\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) = \sin\left(\frac{6\pi}{7}\right) - \sin\left(\frac{4\pi}{7}\right) \)

Summing these terms on the RHS:
\[ 2 \sin\left(\frac{\pi}{7}\right) S = \sin\left(\frac{2\pi}{7}\right) + \left(\sin\left(\frac{4\pi}{7}\right) - \sin\left(\frac{2\pi}{7}\right)\right) + \left(\sin\left(\frac{6\pi}{7}\right) - \sin\left(\frac{4\pi}{7}\right)\right) \]
All intermediate terms cancel out:
\[ 2 \sin\left(\frac{\pi}{7}\right) S = \sin\left(\frac{6\pi}{7}\right) \]

Since \( \sin\left(\frac{6\pi}{7}\right) = \sin\left(\pi - \frac{\pi}{7}\right) = \sin\left(\frac{\pi}{7}\right) \), we get:
\[ 2 \sin\left(\frac{\pi}{7}\right) S = \sin\left(\frac{\pi}{7}\right) \]

Since \( \sin\left(\frac{\pi}{7}\right) \neq 0 \), dividing both sides by \( 2 \sin\left(\frac{\pi}{7}\right) \) yields:
\[ S = \frac{1}{2} \]
Hence, proved.
</details>

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
<details>
<summary>Solution</summary>

This is a series of sines of angles in Arithmetic Progression (AP):
\[ \sum_{k=1}^n \sin(\alpha + (k-1)d) = \frac{\sin\left(\frac{nd}{2}\right)}{\sin\left(\frac{d}{2}\right)} \sin\left(\alpha + \frac{(n-1)d}{2}\right) \]

Here, the first term \( \alpha = 10^\circ \), common difference \( d = 10^\circ \), and number of terms \( n = 9 \).
- \( \frac{nd}{2} = \frac{9 \times 10^\circ}{2} = 45^\circ \)
- \( \frac{d}{2} = 5^\circ \)
- \( \alpha + \frac{(n-1)d}{2} = 10^\circ + \frac{8 \times 10^\circ}{2} = 50^\circ \)

Substituting these into the formula:
\[ \text{Sum} = \frac{\sin 45^\circ}{\sin 5^\circ} \sin 50^\circ = \frac{1}{\sqrt{2}} \frac{\sin 50^\circ}{\sin 5^\circ} = \frac{\cos 40^\circ}{\sqrt{2}\sin 5^\circ} \]
</details>

27. 🔴 Find cos 20° + cos 40° + cos 60° + ... + cos 180°.
<details>
<summary>Solution</summary>

This is a series of cosines of angles in Arithmetic Progression (AP):
\[ \sum_{k=1}^n \cos(\alpha + (k-1)d) = \frac{\sin\left(\frac{nd}{2}\right)}{\sin\left(\frac{d}{2}\right)} \cos\left(\alpha + \frac{(n-1)d}{2}\right) \]

Here, the first term \( \alpha = 20^\circ \), common difference \( d = 20^\circ \), and number of terms \( n = 9 \).
- \( \frac{nd}{2} = \frac{9 \times 20^\circ}{2} = 90^\circ \)
- \( \frac{d}{2} = 10^\circ \)
- \( \alpha + \frac{(n-1)d}{2} = 20^\circ + \frac{8 \times 20^\circ}{2} = 100^\circ \)

Substituting these into the formula:
\[ \text{Sum} = \frac{\sin 90^\circ}{\sin 10^\circ} \cos 100^\circ = \frac{1}{\sin 10^\circ} \cos(90^\circ + 10^\circ) \]
Since \( \cos(90^\circ + 10^\circ) = -\sin 10^\circ \):
\[ \text{Sum} = \frac{-\sin 10^\circ}{\sin 10^\circ} = -1 \]
</details>

28. 🔴 ⭐ Find the sum of sin² 1° + sin² 2° + ... + sin² 90°.
<details>
<summary>Solution</summary>

We can use the complementary relation \( \sin^2 \theta + \sin^2(90^\circ - \theta) = \sin^2 \theta + \cos^2 \theta = 1 \).

The series consists of 90 terms:
\[ S = \sin^2 1^\circ + \sin^2 2^\circ + \dots + \sin^2 44^\circ + \sin^2 45^\circ + \sin^2 46^\circ + \dots + \sin^2 89^\circ + \sin^2 90^\circ \]

Let's group complementary angles:
- \( \sin^2 1^\circ + \sin^2 89^\circ = \sin^2 1^\circ + \cos^2 1^\circ = 1 \)
- \( \sin^2 2^\circ + \sin^2 88^\circ = \sin^2 2^\circ + \cos^2 2^\circ = 1 \)
- ...
- \( \sin^2 44^\circ + \sin^2 46^\circ = \sin^2 44^\circ + \cos^2 44^\circ = 1 \)

This gives exactly 44 pairs, each summing to 1.
The remaining terms that are not part of any pair are:
- \( \sin^2 45^\circ = \left(\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{2} \)
- \( \sin^2 90^\circ = 1^2 = 1 \)

Therefore, the total sum is:
\[ S = 44 \times 1 + \frac{1}{2} + 1 = 45.5 \]
</details>

29. 🔴 Prove that cos(2π/7) + cos(4π/7) + cos(6π/7) = −1/2.
<details>
<summary>Solution</summary>

Let \( S = \cos\left(\frac{2\pi}{7}\right) + \cos\left(\frac{4\pi}{7}\right) + \cos\left(\frac{6\pi}{7}\right) \).

Multiply both sides by \( 2 \sin\left(\frac{\pi}{7}\right) \):
\[ 2 \sin\left(\frac{\pi}{7}\right) S = 2 \cos\left(\frac{2\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) + 2 \cos\left(\frac{4\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) + 2 \cos\left(\frac{6\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) \]

Apply the product-to-sum formula \( 2 \cos A \sin B = \sin(A+B) - \sin(A-B) \):
- \( 2 \cos\left(\frac{2\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) = \sin\left(\frac{3\pi}{7}\right) - \sin\left(\frac{\pi}{7}\right) \)
- \( 2 \cos\left(\frac{4\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) = \sin\left(\frac{5\pi}{7}\right) - \sin\left(\frac{3\pi}{7}\right) \)
- \( 2 \cos\left(\frac{6\pi}{7}\right)\sin\left(\frac{\pi}{7}\right) = \sin\left(\frac{7\pi}{7}\right) - \sin\left(\frac{5\pi}{7}\right) = \sin(\pi) - \sin\left(\frac{5\pi}{7}\right) \)

Summing these terms on the RHS:
\[ 2 \sin\left(\frac{\pi}{7}\right) S = \left(\sin\left(\frac{3\pi}{7}\right) - \sin\left(\frac{\pi}{7}\right)\right) + \left(\sin\left(\frac{5\pi}{7}\right) - \sin\left(\frac{3\pi}{7}\right)\right) + \left(\sin(\pi) - \sin\left(\frac{5\pi}{7}\right)\right) \]
Cancelling matching positive and negative terms:
\[ 2 \sin\left(\frac{\pi}{7}\right) S = \sin(\pi) - \sin\left(\frac{\pi}{7}\right) \]

Since \( \sin(\pi) = 0 \):
\[ 2 \sin\left(\frac{\pi}{7}\right) S = -\sin\left(\frac{\pi}{7}\right) \]

Dividing both sides by \( 2 \sin\left(\frac{\pi}{7}\right) \) (since \( \sin\left(\frac{\pi}{7}\right) \neq 0 \)):
\[ S = -\frac{1}{2} \]
Hence, proved.
</details>

30. 🔴 Find the value of sin(π/7) sin(2π/7) sin(3π/7).
<details>
<summary>Solution</summary>

Let the roots of \( \sin(7x) = 0 \) be examined.
We know that the roots are \( x = \frac{k\pi}{7} \) for \( k = 0, \pm 1, \pm 2, \pm 3 \).
The equation \( \sin(7x) = 0 \) can be expanded as a polynomial in \( \sin x \):
\[ \sin(7x) = \sin x (64 \sin^6 x - 112 \sin^4 x + 56 \sin^2 x - 7) = 0 \]

For \( x \neq k\pi \), the values \( \sin^2\left(\frac{\pi}{7}\right) \), \( \sin^2\left(\frac{2\pi}{7}\right) \), and \( \sin^2\left(\frac{3\pi}{7}\right) \) are the three roots of the cubic equation:
\[ 64 y^3 - 112 y^2 + 56 y - 7 = 0 \]
where \( y = \sin^2 x \).

By Vieta's relations, the product of the roots is:
\[ y_1 y_2 y_3 = \sin^2\left(\frac{\pi}{7}\right) \sin^2\left(\frac{2\pi}{7}\right) \sin^2\left(\frac{3\pi}{7}\right) = \frac{7}{64} \]

Since \( \frac{\pi}{7}, \frac{2\pi}{7}, \frac{3\pi}{7} \) all lie in the first quadrant, their sines are positive.
Taking the positive square root:
\[ \sin\left(\frac{\pi}{7}\right) \sin\left(\frac{2\pi}{7}\right) \sin\left(\frac{3\pi}{7}\right) = \frac{\sqrt{7}}{8} \]
</details>

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
<details>
<summary>Solution</summary>

Let's group the first two terms:
\[ \text{LHS} = (\cos A + \cos B) + \cos C \]

Apply the sum-to-product formula on the first group:
\[ \cos A + \cos B = 2 \cos\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Since \( A+B+C = \pi \), we have \( \frac{A+B}{2} = \frac{\pi}{2} - \frac{C}{2} \). Therefore, \( \cos\left(\frac{A+B}{2}\right) = \sin\left(\frac{C}{2}\right) \).
\[ \cos A + \cos B = 2 \sin\left(\frac{C}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Rewrite \( \cos C \) in terms of half-angles:
\[ \cos C = 1 - 2 \sin^2\left(\frac{C}{2}\right) \]

Substitute these back into the expression:
\[ \text{LHS} = 2 \sin\left(\frac{C}{2}\right) \cos\left(\frac{A-B}{2}\right) + 1 - 2 \sin^2\left(\frac{C}{2}\right) \]
\[ = 1 + 2 \sin\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) - \sin\left(\frac{C}{2}\right) \right] \]

Since \( \sin\left(\frac{C}{2}\right) = \cos\left(\frac{A+B}{2}\right) \):
\[ = 1 + 2 \sin\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) - \cos\left(\frac{A+B}{2}\right) \right] \]

Using the formula \( \cos X - \cos Y = 2 \sin\left(\frac{X+Y}{2}\right) \sin\left(\frac{Y-X}{2}\right) \):
\[ \cos\left(\frac{A-B}{2}\right) - \cos\left(\frac{A+B}{2}\right) = 2 \sin\left(\frac{A}{2}\right) \sin\left(\frac{B}{2}\right) \]

Substituting this gives:
\[ \text{LHS} = 1 + 2 \sin\left(\frac{C}{2}\right) \left[ 2 \sin\left(\frac{A}{2}\right) \sin\left(\frac{B}{2}\right) \right] = 1 + 4 \sin\left(\frac{A}{2}\right) \sin\left(\frac{B}{2}\right) \sin\left(\frac{C}{2}\right) = \text{RHS} \]
Hence, proved.
</details>

32. 🔴 If A+B+C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2).
<details>
<summary>Solution</summary>

Let's group the first two terms:
\[ \text{LHS} = (\sin A + \sin B) + \sin C \]

Apply the sum-to-product formula on the first group:
\[ \sin A + \sin B = 2 \sin\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Since \( A+B+C = \pi \), we have \( \frac{A+B}{2} = \frac{\pi}{2} - \frac{C}{2} \). Therefore, \( \sin\left(\frac{A+B}{2}\right) = \cos\left(\frac{C}{2}\right) \).
\[ \sin A + \sin B = 2 \cos\left(\frac{C}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Rewrite \( \sin C \) using the double-angle formula:
\[ \sin C = 2 \sin\left(\frac{C}{2}\right) \cos\left(\frac{C}{2}\right) \]

Substitute these back into the expression:
\[ \text{LHS} = 2 \cos\left(\frac{C}{2}\right) \cos\left(\frac{A-B}{2}\right) + 2 \sin\left(\frac{C}{2}\right) \cos\left(\frac{C}{2}\right) \]
\[ = 2 \cos\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) + \sin\left(\frac{C}{2}\right) \right] \]

Since \( \sin\left(\frac{C}{2}\right) = \cos\left(\frac{A+B}{2}\right) \):
\[ = 2 \cos\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) + \cos\left(\frac{A+B}{2}\right) \right] \]

Using the formula \( \cos X + \cos Y = 2 \cos\left(\frac{X+Y}{2}\right) \cos\left(\frac{X-Y}{2}\right) \):
\[ \cos\left(\frac{A-B}{2}\right) + \cos\left(\frac{A+B}{2}\right) = 2 \cos\left(\frac{A}{2}\right) \cos\left(\frac{B}{2}\right) \]

Substituting this gives:
\[ \text{LHS} = 2 \cos\left(\frac{C}{2}\right) \left[ 2 \cos\left(\frac{A}{2}\right) \cos\left(\frac{B}{2}\right) \right] = 4 \cos\left(\frac{A}{2}\right) \cos\left(\frac{B}{2}\right) \cos\left(\frac{C}{2}\right) = \text{RHS} \]
Hence, proved.
</details>

33. 🔴 If A+B+C = π, prove that tan A + tan B + tan C = tan A tan B tan C.
<details>
<summary>Solution</summary>

Given \( A+B+C = \pi \), we can write:
\[ A+B = \pi - C \]

Take the tangent of both sides:
\[ \tan(A+B) = \tan(\pi - C) \]

Apply the tangent addition formula:
\[ \frac{\tan A + \tan B}{1 - \tan A \tan B} = -\tan C \]

Cross-multiply:
\[ \tan A + \tan B = -\tan C (1 - \tan A \tan B) \]
\[ \tan A + \tan B = -\tan C + \tan A \tan B \tan C \]

Rearranging the terms:
\[ \tan A + \tan B + \tan C = \tan A \tan B \tan C \]
Hence, proved.
</details>

34. 🔴 ⭐ If A+B+C = π, prove that cos²A + cos²B + cos²C = 1 − 2 cos A cos B cos C.
<details>
<summary>Solution</summary>

Using the identity \( \cos^2 \theta = \frac{1 + \cos 2\theta}{2} \):
\[ \text{LHS} = \frac{1 + \cos 2A}{2} + \frac{1 + \cos 2B}{2} + \cos^2 C \]
\[ = 1 + \frac{\cos 2A + \cos 2B}{2} + \cos^2 C \]

Apply the sum-to-product formula on \( \cos 2A + \cos 2B \):
\[ \cos 2A + \cos 2B = 2 \cos(A+B) \cos(A-B) \]
Since \( A+B = \pi - C \), we have \( \cos(A+B) = \cos(\pi-C) = -\cos C \).
\[ \cos 2A + \cos 2B = -2 \cos C \cos(A-B) \]

Substitute this back:
\[ \text{LHS} = 1 - \cos C \cos(A-B) + \cos^2 C \]
\[ = 1 - \cos C [ \cos(A-B) - \cos C ] \]

Since \( -\cos C = \cos(A+B) \):
\[ = 1 - \cos C [ \cos(A-B) + \cos(A+B) ] \]

Using the identity \( \cos(A-B) + \cos(A+B) = 2 \cos A \cos B \):
\[ \text{LHS} = 1 - \cos C [ 2 \cos A \cos B ] = 1 - 2 \cos A \cos B \cos C = \text{RHS} \]
Hence, proved.
</details>

35. 🔴 If A+B+C = 180°, prove that sin²A + sin²B + sin²C = 2 + 2 cos A cos B cos C.
<details>
<summary>Solution</summary>

Using the relation \( \sin^2 \theta = 1 - \cos^2 \theta \):
\[ \text{LHS} = (1 - \cos^2 A) + (1 - \cos^2 B) + (1 - \cos^2 C) \]
\[ = 3 - (\cos^2 A + \cos^2 B + \cos^2 C) \]

Using the identity proved in the previous problem (Problem 34) for \( A+B+C = 180^\circ \):
\[ \cos^2 A + \cos^2 B + \cos^2 C = 1 - 2 \cos A \cos B \cos C \]

Substituting this in:
\[ \text{LHS} = 3 - (1 - 2 \cos A \cos B \cos C) = 2 + 2 \cos A \cos B \cos C = \text{RHS} \]
Hence, proved.
</details>

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
<details>
<summary>Solution</summary>

Apply the sum-to-product formula:
\[ \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = \theta + 120^\circ \) and \( D = \theta \).
- \( \frac{C+D}{2} = \frac{2\theta + 120^\circ}{2} = \theta + 60^\circ \)
- \( \frac{C-D}{2} = \frac{120^\circ}{2} = 60^\circ \)

Substituting these gives:
\[ \cos \theta + \cos(\theta + 120^\circ) = 2 \cos(\theta + 60^\circ) \cos 60^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ = 2 \cos(\theta + 60^\circ) \left(\frac{1}{2}\right) = \cos(\theta + 60^\circ) \]

Since the maximum value of \( \cos x \) is 1:
\[ \text{Maximum} = 1 \]
</details>

37. 🟡 Find the maximum of sin θ + sin(θ + 120°).
<details>
<summary>Solution</summary>

Apply the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = \theta + 120^\circ \) and \( D = \theta \).
- \( \frac{C+D}{2} = \theta + 60^\circ \)
- \( \frac{C-D}{2} = 60^\circ \)

Substituting these gives:
\[ \sin \theta + \sin(\theta + 120^\circ) = 2 \sin(\theta + 60^\circ) \cos 60^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ = 2 \sin(\theta + 60^\circ) \left(\frac{1}{2}\right) = \sin(\theta + 60^\circ) \]

Since the maximum value of \( \sin x \) is 1:
\[ \text{Maximum} = 1 \]
</details>

38. 🟡 Find the minimum of cos θ + cos(θ + 60°).
<details>
<summary>Solution</summary>

Apply the sum-to-product formula:
\[ \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = \theta + 60^\circ \) and \( D = \theta \).
- \( \frac{C+D}{2} = \theta + 30^\circ \)
- \( \frac{C-D}{2} = 30^\circ \)

Substituting these gives:
\[ \cos \theta + \cos(\theta + 60^\circ) = 2 \cos(\theta + 30^\circ) \cos 30^\circ \]

Since \( \cos 30^\circ = \frac{\sqrt{3}}{2} \):
\[ = 2 \cos(\theta + 30^\circ) \left(\frac{\sqrt{3}}{2}\right) = \sqrt{3} \cos(\theta + 30^\circ) \]

Since the minimum value of \( \cos x \) is -1:
\[ \text{Minimum} = -\sqrt{3} \]
</details>

39. 🔴 ⭐ Find the maximum of sin(θ + 30°) + cos(θ + 60°).
<details>
<summary>Solution</summary>

Rewrite \( \cos(\theta + 60^\circ) \) as a sine function using the identity \( \cos x = \sin(90^\circ - x) \):
\[ \cos(\theta + 60^\circ) = \sin(90^\circ - (\theta + 60^\circ)) = \sin(30^\circ - \theta) \]

The expression becomes:
\[ \sin(\theta + 30^\circ) + \sin(30^\circ - \theta) \]

Apply the sum-to-product formula:
\[ 2 \sin\left(\frac{(\theta + 30^\circ) + (30^\circ - \theta)}{2}\right) \cos\left(\frac{(\theta + 30^\circ) - (30^\circ - \theta)}{2}\right) \]
\[ = 2 \sin(30^\circ) \cos(\theta) \]

Since \( \sin 30^\circ = \frac{1}{2} \):
\[ = 2 \cdot \frac{1}{2} \cdot \cos\theta = \cos\theta \]

Since the maximum value of \( \cos\theta \) is 1:
\[ \text{Maximum} = 1 \]
</details>

40. 🔴 Find the maximum value of sin²θ + sin²(θ + 60°) + sin²(θ + 120°).
<details>
<summary>Solution</summary>

Let \( E = \sin^2\theta + \sin^2(\theta + 60^\circ) + \sin^2(\theta + 120^\circ) \).

Use the identity \( \sin^2 x = \frac{1 - \cos 2x}{2} \):
\[ E = \frac{1 - \cos 2\theta}{2} + \frac{1 - \cos(2\theta + 120^\circ)}{2} + \frac{1 - \cos(2\theta + 240^\circ)}{2} \]
\[ = \frac{3}{2} - \frac{1}{2} \left[ \cos 2\theta + \cos(2\theta + 120^\circ) + \cos(2\theta + 240^\circ) \right] \]

Simplify the terms inside the brackets:
\[ \cos(2\theta + 120^\circ) + \cos(2\theta + 240^\circ) = 2 \cos\left(\frac{4\theta + 360^\circ}{2}\right) \cos\left(\frac{-120^\circ}{2}\right) \]
\[ = 2 \cos(2\theta + 180^\circ) \cos(-60^\circ) \]

Since \( \cos(2\theta + 180^\circ) = -\cos 2\theta \) and \( \cos(-60^\circ) = \frac{1}{2} \):
\[ = 2 (-\cos 2\theta) \left(\frac{1}{2}\right) = -\cos 2\theta \]

Substituting this back into the bracket:
\[ \cos 2\theta + \left[ \cos(2\theta + 120^\circ) + \cos(2\theta + 240^\circ) \right] = \cos 2\theta - \cos 2\theta = 0 \]

Thus, the entire bracket is zero:
\[ E = \frac{3}{2} - 0 = \frac{3}{2} \]

Since the expression is constant, the maximum (and minimum) value is \( \frac{3}{2} \).
</details>

---

## Stage 4: Type Mixer

1. 🟡 Express as a product: sin 65° + sin 25°. Hence find its value.
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = 65^\circ \) and \( D = 25^\circ \).
- \( \frac{C+D}{2} = 45^\circ \)
- \( \frac{C-D}{2} = 20^\circ \)

Thus, the product form is:
\[ \sin 65^\circ + \sin 25^\circ = 2 \sin 45^\circ \cos 20^\circ \]

Since \( \sin 45^\circ = \frac{1}{\sqrt{2}} \), the value is:
\[ 2 \cdot \frac{1}{\sqrt{2}} \cdot \cos 20^\circ = \sqrt{2} \cos 20^\circ \]
</details>

2. 🟡 Prove that (sin 5x − sin 3x + sin x)/(cos 5x − cos 3x + cos x) = tan x.
<details>
<summary>Solution</summary>

Let's group the terms in the numerator and denominator:

- **Numerator:**
  \[ (\sin 5x + \sin x) - \sin 3x \]
  Using the formula \( \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  \[ = 2 \sin 3x \cos 2x - \sin 3x = \sin 3x (2 \cos 2x - 1) \]

- **Denominator:**
  \[ (\cos 5x + \cos x) - \cos 3x \]
  Using the formula \( \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \):
  \[ = 2 \cos 3x \cos 2x - \cos 3x = \cos 3x (2 \cos 2x - 1) \]

- **Ratio:**
  \[ \text{LHS} = \frac{\sin 3x (2 \cos 2x - 1)}{\cos 3x (2 \cos 2x - 1)} = \frac{\sin 3x}{\cos 3x} = \tan 3x \]

*Note: There is a typo in the original question's RHS, which states \( \tan x \). The correct simplified value is \( \tan 3x \).*
</details>

3. 🔴 ⭐ Solve sin 2x + sin 4x + sin 6x = 0 for 0° ≤ x ≤ 180°.
<details>
<summary>Solution</summary>

Group the first and third terms:
\[ (\sin 6x + \sin 2x) + \sin 4x = 0 \]

Apply the sum-to-product formula:
\[ 2 \sin 4x \cos 2x + \sin 4x = 0 \]
\[ \sin 4x (2 \cos 2x + 1) = 0 \]

This gives two cases:

- **Case 1: \( \sin 4x = 0 \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 4x \) is \( 0^\circ \le 4x \le 720^\circ \).
  \[ 4x = 0^\circ, 180^\circ, 360^\circ, 540^\circ, 720^\circ \]
  \[ x = 0^\circ, 45^\circ, 90^\circ, 135^\circ, 180^\circ \]

- **Case 2: \( 2 \cos 2x + 1 = 0 \Rightarrow \cos 2x = -\frac{1}{2} \)**
  For \( 0^\circ \le x \le 180^\circ \), the range of \( 2x \) is \( 0^\circ \le 2x \le 360^\circ \).
  \[ 2x = 120^\circ, 240^\circ \]
  \[ x = 60^\circ, 120^\circ \]

**Combined Solutions:**
\[ x = 0^\circ, 45^\circ, 60^\circ, 90^\circ, 120^\circ, 135^\circ, 180^\circ \]
</details>

4. 🔴 If A + B + C = π, prove that sin 2A + sin 2B − sin 2C = 4 cos A cos B sin C.
<details>
<summary>Solution</summary>

Group the first two terms of the LHS:
\[ \text{LHS} = (\sin 2A + \sin 2B) - \sin 2C \]

Apply the sum-to-product formula:
\[ \sin 2A + \sin 2B = 2 \sin(A+B) \cos(A-B) \]
Since \( A+B = \pi - C \), we have \( \sin(A+B) = \sin(\pi - C) = \sin C \).
\[ \sin 2A + \sin 2B = 2 \sin C \cos(A-B) \]

Using the double-angle formula for \( \sin 2C \):
\[ \sin 2C = 2 \sin C \cos C \]

Substitute these back into the expression:
\[ \text{LHS} = 2 \sin C \cos(A-B) - 2 \sin C \cos C \]
\[ = 2 \sin C [ \cos(A-B) - \cos C ] \]

Since \( C = \pi - (A+B) \), we have \( \cos C = \cos(\pi - (A+B)) = -\cos(A+B) \).
Substitute this in:
\[ \text{LHS} = 2 \sin C [ \cos(A-B) - (-\cos(A+B)) ] \]
\[ = 2 \sin C [ \cos(A-B) + \cos(A+B) ] \]

Using the identity \( \cos(A-B) + \cos(A+B) = 2 \cos A \cos B \):
\[ \text{LHS} = 2 \sin C [ 2 \cos A \cos B ] = 4 \cos A \cos B \sin C = \text{RHS} \]
Hence, proved.
</details>

5. 🔴 Show that cos 20° cos 40° cos 80° = 1/8 using product→sum transformations.
<details>
<summary>Solution</summary>

Let's start with the LHS:
\[ \text{LHS} = \cos 20^\circ \cos 40^\circ \cos 80^\circ \]

Multiply and divide by 2:
\[ = \frac{1}{2} (2 \cos 40^\circ \cos 20^\circ) \cos 80^\circ \]

Apply the product-to-sum formula \( 2 \cos A \cos B = \cos(A+B) + \cos(A-B) \):
\[ = \frac{1}{2} [ \cos(40^\circ + 20^\circ) + \cos(40^\circ - 20^\circ) ] \cos 80^\circ \]
\[ = \frac{1}{2} [ \cos 60^\circ + \cos 20^\circ ] \cos 80^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ = \frac{1}{2} \left[ \frac{1}{2} + \cos 20^\circ \right] \cos 80^\circ \]
\[ = \frac{1}{4} \cos 80^\circ + \frac{1}{2} \cos 80^\circ \cos 20^\circ \]

Multiply the second term by \( \frac{2}{2} \):
\[ = \frac{1}{4} \cos 80^\circ + \frac{1}{4} (2 \cos 80^\circ \cos 20^\circ) \]

Apply product-to-sum formula again:
\[ = \frac{1}{4} \cos 80^\circ + \frac{1}{4} [ \cos(80^\circ + 20^\circ) + \cos(80^\circ - 20^\circ) ] \]
\[ = \frac{1}{4} \cos 80^\circ + \frac{1}{4} [ \cos 100^\circ + \cos 60^\circ ] \]
\[ = \frac{1}{4} \cos 80^\circ + \frac{1}{4} \cos 100^\circ + \frac{1}{4} \left(\frac{1}{2}\right) \]

Since \( \cos 100^\circ = \cos(180^\circ - 80^\circ) = -\cos 80^\circ \):
\[ = \frac{1}{4} \cos 80^\circ - \frac{1}{4} \cos 80^\circ + \frac{1}{8} = \frac{1}{8} = \text{RHS} \]
Hence, proved.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Express sin 5x − sin 3x as a product. **(1 mark)**

<details>
<summary>Solution</summary>

```
sin 5x − sin 3x = 2 cos((5x+3x)/2) sin((5x−3x)/2) = 2 cos 4x sin x
```
</details>

---

**Q2.** 🟡 Simplify (sin 7x + sin 5x)/(cos 7x − cos 5x). **(2 marks)**

<details>
<summary>Solution</summary>

```
= (2 sin 6x cos x)/(−2 sin 6x sin x)
= −cot x
```
</details>

---

**Q3.** 🟡 Express 2 sin 5θ cos 3θ as a sum. **(1 mark)**

<details>
<summary>Solution</summary>

```
= sin(5θ+3θ) + sin(5θ−3θ) = sin 8θ + sin 2θ
```
</details>

---

**Q4.** 🔴 If A + B + C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2). **(3 marks)**

<details>
<summary>Solution</summary>

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
</details>

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
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Let \( C = 7x \) and \( D = 3x \):
- \( \frac{C+D}{2} = \frac{7x+3x}{2} = 5x \)
- \( \frac{C-D}{2} = \frac{7x-3x}{2} = 2x \)

Substituting these values:
\[ \sin 7x + \sin 3x = 2 \sin 5x \cos 2x \]

**Answer: (a) 2 sin 5x cos 2x**
</details>

2. 🟢 cos 7x − cos 3x equals:
   (a) −2 sin 5x sin 2x   (b) 2 sin 5x sin 2x   (c) −2 cos 5x cos 2x   (d) 2 cos 5x cos 2x
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C - \cos D = -2 \sin\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \]

Let \( C = 7x \) and \( D = 3x \):
- \( \frac{C+D}{2} = \frac{7x+3x}{2} = 5x \)
- \( \frac{C-D}{2} = \frac{7x-3x}{2} = 2x \)

Substituting these values:
\[ \cos 7x - \cos 3x = -2 \sin 5x \sin 2x \]

**Answer: (a) −2 sin 5x sin 2x**
</details>

3. 🟢 2 sin 5x cos 3x equals:
   (a) sin 8x + sin 2x   (b) sin 8x − sin 2x   (c) cos 8x + cos 2x   (d) cos 8x − cos 2x
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \]

Let \( A = 5x \) and \( B = 3x \):
- \( A+B = 5x+3x = 8x \)
- \( A-B = 5x-3x = 2x \)

Substituting these values:
\[ 2 \sin 5x \cos 3x = \sin 8x + \sin 2x \]

**Answer: (a) sin 8x + sin 2x**
</details>

4. 🟡 (sin 5x + sin 3x)/(cos 5x − cos 3x) equals:
   (a) tan x   (b) −cot 4x   (c) cot 4x   (d) tan 4x
<details>
<summary>Solution</summary>

*Note: The question contains a typo. The numerator should be \( \sin 5x - \sin 3x \) to match option (b).*

Assuming the correct expression is \( \frac{\sin 5x - \sin 3x}{\cos 5x - \cos 3x} \):
- Numerator: \( \sin 5x - \sin 3x = 2 \cos 4x \sin x \)
- Denominator: \( \cos 5x - \cos 3x = -2 \sin 4x \sin x \)

Taking the ratio:
\[ \frac{2 \cos 4x \sin x}{-2 \sin 4x \sin x} = -\frac{\cos 4x}{\sin 4x} = -\cot 4x \]

**Answer: (b) −cot 4x**
</details>

5. 🟡 sin 75° − sin 15° equals:
   (a) 1/√2   (b) √3/2   (c) 1/2   (d) 1
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C - \sin D = 2 \cos\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \]

Here, \( C = 75^\circ \) and \( D = 15^\circ \):
- \( \frac{C+D}{2} = 45^\circ \)
- \( \frac{C-D}{2} = 30^\circ \)

Substituting these:
\[ \sin 75^\circ - \sin 15^\circ = 2 \cos 45^\circ \sin 30^\circ \]

Using the standard values \( \cos 45^\circ = \frac{1}{\sqrt{2}} \) and \( \sin 30^\circ = \frac{1}{2} \):
\[ 2 \cdot \frac{1}{\sqrt{2}} \cdot \frac{1}{2} = \frac{1}{\sqrt{2}} \]

**Answer: (a) 1/√2**
</details>

6. 🟡 cos 75° + cos 15° equals:
   (a) √6/2   (b) √3/2   (c) 1/2   (d) 0
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Here, \( C = 75^\circ \) and \( D = 15^\circ \):
- \( \frac{C+D}{2} = 45^\circ \)
- \( \frac{C-D}{2} = 30^\circ \)

Substituting these:
\[ \cos 75^\circ + \cos 15^\circ = 2 \cos 45^\circ \cos 30^\circ \]

Using the standard values \( \cos 45^\circ = \frac{1}{\sqrt{2}} \) and \( \cos 30^\circ = \frac{\sqrt{3}}{2} \):
\[ 2 \cdot \frac{1}{\sqrt{2}} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{\sqrt{2}} = \frac{\sqrt{6}}{2} \]

**Answer: (a) √6/2**
</details>

7. 🟡 2 sin 50° cos 10° equals:
   (a) sin 60° + sin 40°   (b) sin 60° − sin 40°   (c) cos 60° + cos 40°   (d) cos 60° − cos 40°
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \]

Here, \( A = 50^\circ \) and \( B = 10^\circ \):
- \( A+B = 60^\circ \)
- \( A-B = 40^\circ \)

Substituting these:
\[ 2 \sin 50^\circ \cos 10^\circ = \sin 60^\circ + \sin 40^\circ \]

**Answer: (a) sin 60° + sin 40°**
</details>

8. 🟡 sin 20° + sin 40° equals:
   (a) sin 60°   (b) cos 10°   (c) sin 10°   (d) cos 20°
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Rearranging \( \sin 40^\circ + \sin 20^\circ \) where \( C = 40^\circ \) and \( D = 20^\circ \):
- \( \frac{C+D}{2} = 30^\circ \)
- \( \frac{C-D}{2} = 10^\circ \)

Substituting these:
\[ \sin 40^\circ + \sin 20^\circ = 2 \sin 30^\circ \cos 10^\circ \]

Since \( \sin 30^\circ = \frac{1}{2} \):
\[ 2 \cdot \frac{1}{2} \cdot \cos 10^\circ = \cos 10^\circ \]

**Answer: (b) cos 10°**
</details>

9. 🟡 cos 40° + cos 80° equals:
   (a) cos 20°   (b) √3 cos 20°   (c) √3 cos 10°   (d) cos 60°
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C + \cos D = 2 \cos\left(\frac{C+D}{2}\right) \cos\left(\frac{C-D}{2}\right) \]

Rearranging \( \cos 80^\circ + \cos 40^\circ \) where \( C = 80^\circ \) and \( D = 40^\circ \):
- \( \frac{C+D}{2} = 60^\circ \)
- \( \frac{C-D}{2} = 20^\circ \)

Substituting these:
\[ \cos 80^\circ + \cos 40^\circ = 2 \cos 60^\circ \cos 20^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ 2 \cdot \frac{1}{2} \cdot \cos 20^\circ = \cos 20^\circ \]

**Answer: (a) cos 20°**
</details>

10. 🟡 cos 40° − cos 80° equals:
    (a) √3 sin 20°   (b) √3 sin 60°   (c) sin 20°   (d) −√3 sin 20°
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \cos C - \cos D = -2 \sin\left(\frac{C+D}{2}\right) \sin\left(\frac{C-D}{2}\right) \]

Here, \( C = 40^\circ \) and \( D = 80^\circ \):
- \( \frac{C+D}{2} = 60^\circ \)
- \( \frac{C-D}{2} = -20^\circ \)

Substituting these:
\[ \cos 40^\circ - \cos 80^\circ = -2 \sin 60^\circ \sin(-20^\circ) \]

Since \( \sin(-\theta) = -\sin\theta \):
\[ = 2 \sin 60^\circ \sin 20^\circ \]

Since \( \sin 60^\circ = \frac{\sqrt{3}}{2} \):
\[ = 2 \cdot \frac{\sqrt{3}}{2} \cdot \sin 20^\circ = \sqrt{3} \sin 20^\circ \]

**Answer: (a) √3 sin 20°**
</details>

11. 🟡 The product 2 sin A cos B equals:
    (a) sin(A+B) + sin(A−B)   (b) sin(A+B) − sin(A−B)   (c) cos(A+B) + cos(A−B)   (d) cos(A+B) − cos(A−B)
<details>
<summary>Solution</summary>

By standard product-to-sum identity:
\[ 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \]

**Answer: (a) sin(A+B) + sin(A−B)**
</details>

12. 🟡 (sin 3x + sin x)/sin 2x equals:
    (a) 2 cos x   (b) 2 sin x   (c) cos x   (d) sin x
<details>
<summary>Solution</summary>

Apply the sum-to-product formula on the numerator:
\[ \sin 3x + \sin x = 2 \sin 2x \cos x \]

Divide by the denominator \( \sin 2x \):
\[ \frac{2 \sin 2x \cos x}{\sin 2x} = 2 \cos x \]

**Answer: (a) 2 cos x**
</details>

13. 🟡 sin 50° − sin 70° + sin 10° equals:
    (a) 1   (b) 0   (c) 1/2   (d) √3/2
<details>
<summary>Solution</summary>

Rearrange terms:
\[ (\sin 50^\circ + \sin 10^\circ) - \sin 70^\circ \]

Apply the sum-to-product formula to the first two terms:
\[ 2 \sin 30^\circ \cos 20^\circ - \sin 70^\circ \]

Since \( \sin 30^\circ = \frac{1}{2} \):
\[ = 2 \cdot \frac{1}{2} \cdot \cos 20^\circ - \sin 70^\circ = \cos 20^\circ - \sin 70^\circ \]

Using the identity \( \sin(90^\circ - \theta) = \cos\theta \):
\[ \sin 70^\circ = \sin(90^\circ - 20^\circ) = \cos 20^\circ \]

Substitute this back:
\[ \cos 20^\circ - \cos 20^\circ = 0 \]

**Answer: (b) 0**
</details>

14. 🟡 cos 20° + cos 100° + cos 140° equals:
    (a) 1   (b) 0   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

Rearrange terms:
\[ (\cos 100^\circ + \cos 20^\circ) + \cos 140^\circ \]

Apply the sum-to-product formula to the first two terms:
\[ 2 \cos 60^\circ \cos 40^\circ + \cos 140^\circ \]

Since \( \cos 60^\circ = \frac{1}{2} \):
\[ = \cos 40^\circ + \cos 140^\circ \]

Since \( \cos 140^\circ = \cos(180^\circ - 40^\circ) = -\cos 40^\circ \):
\[ = \cos 40^\circ - \cos 40^\circ = 0 \]

**Answer: (b) 0**
</details>

15. 🟡 The sum sin 5° + sin 10° + ... + sin 85° can be simplified using:
    (a) Compound angles   (b) Transformation formulas   (c) Half-angle   (d) Double angle
<details>
<summary>Solution</summary>

This is a series of sines of angles in Arithmetic Progression (AP) which can be simplified using product-to-sum / sum-to-product (transformation) formulas.

**Answer: (b) Transformation formulas**
</details>

16. 🟡 The value of sin 20° sin 40° sin 80° is:
    (a) √3/8   (b) 1/8   (c) 1/4   (d) 3/8
<details>
<summary>Solution</summary>

Group the first two terms:
\[ \sin 20^\circ \sin 40^\circ \sin 80^\circ = \frac{1}{2} (2 \sin 40^\circ \sin 20^\circ) \sin 80^\circ \]

Apply the product-to-sum formula \( 2 \sin A \sin B = \cos(A-B) - \cos(A+B) \):
\[ = \frac{1}{2} [ \cos 20^\circ - \cos 60^\circ ] \sin 80^\circ \]
\[ = \frac{1}{2} \left[ \cos 20^\circ - \frac{1}{2} \right] \sin 80^\circ \]
\[ = \frac{1}{2} \cos 20^\circ \sin 80^\circ - \frac{1}{4} \sin 80^\circ \]

Multiply the first term by \( \frac{2}{2} \):
\[ = \frac{1}{4} (2 \sin 80^\circ \cos 20^\circ) - \frac{1}{4} \sin 80^\circ \]

Apply product-to-sum formula \( 2 \sin A \cos B = \sin(A+B) + \sin(A-B) \):
\[ = \frac{1}{4} [ \sin 100^\circ + \sin 60^\circ ] - \frac{1}{4} \sin 80^\circ \]

Since \( \sin 100^\circ = \sin(180^\circ - 80^\circ) = \sin 80^\circ \):
\[ = \frac{1}{4} \sin 80^\circ + \frac{1}{4} \sin 60^\circ - \frac{1}{4} \sin 80^\circ \]
\[ = \frac{1}{4} \sin 60^\circ = \frac{1}{4} \left(\frac{\sqrt{3}}{2}\right) = \frac{\sqrt{3}}{8} \]

**Answer: (a) √3/8**
</details>

17. 🟡 cos 10° cos 30° cos 50° cos 70° equals:
    (a) 1/16   (b) 3/16   (c) 5/16   (d) 7/16
<details>
<summary>Solution</summary>

Substitute the value of \( \cos 30^\circ = \frac{\sqrt{3}}{2} \):
\[ S = \frac{\sqrt{3}}{2} \cos 10^\circ \cos 50^\circ \cos 70^\circ \]

Notice that \( \cos 50^\circ = \cos(60^\circ - 10^\circ) \) and \( \cos 70^\circ = \cos(60^\circ + 10^\circ) \).
Using the product identity:
\[ \cos \theta \cos(60^\circ - \theta) \cos(60^\circ + 80^\circ) = \frac{1}{4} \cos 3\theta \]
Wait, it's \( 60^\circ + \theta \), which is \( 70^\circ \).
For \( \theta = 10^\circ \):
\[ \cos 10^\circ \cos 50^\circ \cos 70^\circ = \frac{1}{4} \cos 30^\circ = \frac{1}{4} \left(\frac{\sqrt{3}}{2}\right) = \frac{\sqrt{3}}{8} \]

Substitute this back into the expression:
\[ S = \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{3}}{8} = \frac{3}{16} \]

**Answer: (b) 3/16**
</details>

18. 🟡 2 cos 70° cos 10° equals:
    (a) cos 80° + cos 60°   (b) cos 80° − cos 60°   (c) sin 80° + sin 60°   (d) sin 80° − sin 60°
<details>
<summary>Solution</summary>

Using the product-to-sum formula:
\[ 2 \cos A \cos B = \cos(A+B) + \cos(A-B) \]

Here, \( A = 70^\circ \) and \( B = 10^\circ \):
- \( A+B = 80^\circ \)
- \( A-B = 60^\circ \)

Substituting these gives:
\[ 2 \cos 70^\circ \cos 10^\circ = \cos 80^\circ + \cos 60^\circ \]

**Answer: (a) cos 80° + cos 60°**
</details>

19. 🟡 The maximum value of sin θ + sin(θ + 60°) is:
    (a) 2   (b) √3   (c) 1   (d) √2
<details>
<summary>Solution</summary>

Using the sum-to-product formula:
\[ \sin \theta + \sin(\theta + 60^\circ) = 2 \sin\left(\frac{2\theta + 60^\circ}{2}\right) \cos\left(\frac{60^\circ}{2}\right) \]
\[ = 2 \sin(\theta + 30^\circ) \cos 30^\circ \]

Since \( \cos 30^\circ = \frac{\sqrt{3}}{2} \):
\[ = 2 \sin(\theta + 30^\circ) \left(\frac{\sqrt{3}}{2}\right) = \sqrt{3} \sin(\theta + 30^\circ) \]

Since the maximum value of \( \sin(\theta + 30^\circ) \) is 1:
\[ \text{Maximum value} = \sqrt{3} \]

**Answer: (b) √3**
</details>

20. 🟡 If A + B + C = π, then cos A + cos B + cos C equals:
    (a) 1 + 4 sin(A/2) sin(B/2) sin(C/2)   (b) 1 − 4 sin(A/2) sin(B/2) sin(C/2)
    (c) 4 sin(A/2) sin(B/2) sin(C/2)   (d) 2
<details>
<summary>Solution</summary>

Group the first two terms:
\[ \cos A + \cos B = 2 \cos\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Since \( A+B = \pi - C \), we have \( \frac{A+B}{2} = \frac{\pi}{2} - \frac{C}{2} \). Thus, \( \cos\left(\frac{A+B}{2}\right) = \sin\left(\frac{C}{2}\right) \):
\[ \cos A + \cos B = 2 \sin\left(\frac{C}{2}\right) \cos\left(\frac{A-B}{2}\right) \]

Rewrite \( \cos C \) in terms of half-angle \( C/2 \):
\[ \cos C = 1 - 2 \sin^2\left(\frac{C}{2}\right) \]

Substituting these in:
\[ \cos A + \cos B + \cos C = 1 + 2 \sin\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) - \sin\left(\frac{C}{2}\right) \right] \]

Since \( \sin\left(\frac{C}{2}\right) = \cos\left(\frac{A+B}{2}\right) \):
\[ = 1 + 2 \sin\left(\frac{C}{2}\right) \left[ \cos\left(\frac{A-B}{2}\right) - \cos\left(\frac{A+B}{2}\right) \right] \]

Using \( \cos X - \cos Y = 2 \sin\left(\frac{X+Y}{2}\right) \sin\left(\frac{Y-X}{2}\right) \):
\[ = 1 + 4 \sin\left(\frac{A}{2}\right) \sin\left(\frac{B}{2}\right) \sin\left(\frac{C}{2}\right) \]

**Answer: (a) 1 + 4 sin(A/2) sin(B/2) sin(C/2)**
</details>

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
