Created At: 2026-06-23T11:43:42Z
Completed At: 2026-06-23T11:43:42Z
File Path: `file:///i:/Lyra-Cofounder/Study/subjects/maths/trigonometry/09_compound_angles.md`

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
<details>
<summary>Solution</summary>

We can express \( 15^\circ \) as a difference of two standard angles: \( 15^\circ = 45^\circ - 30^\circ \).
Using the cosine compound angle formula:
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]
Setting \( A = 45^\circ \) and \( B = 30^\circ \):
\[ \cos 15^\circ = \cos(45^\circ - 30^\circ) = \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ \]
Substitute the standard trigonometric values:
\[ \cos 45^\circ = \frac{1}{\sqrt{2}}, \quad \cos 30^\circ = \frac{\sqrt{3}}{2} \]
\[ \sin 45^\circ = \frac{1}{\sqrt{2}}, \quad \sin 30^\circ = \frac{1}{2} \]
Therefore:
\[ \cos 15^\circ = \left(\frac{1}{\sqrt{2}}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{2}\right) = \frac{\sqrt{3} + 1}{2\sqrt{2}} \]

</details>

2. 🟡 Find tan 75°.
<details>
<summary>Solution</summary>

We can express \( 75^\circ \) as a sum of two standard angles: \( 75^\circ = 45^\circ + 30^\circ \).
Using the tangent compound angle formula:
\[ \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} \]
Setting \( A = 45^\circ \) and \( B = 30^\circ \):
\[ \tan 75^\circ = \tan(45^\circ + 30^\circ) = \frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ \tan 30^\circ} \]
Substitute the known values \( \tan 45^\circ = 1 \) and \( \tan 30^\circ = \frac{1}{\sqrt{3}} \):
\[ \tan 75^\circ = \frac{1 + \frac{1}{\sqrt{3}}}{1 - 1 \cdot \frac{1}{\sqrt{3}}} = \frac{\frac{\sqrt{3} + 1}{\sqrt{3}}}{\frac{\sqrt{3} - 1}{\sqrt{3}}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1} \]
Rationalizing the denominator by multiplying the numerator and denominator by \( \sqrt{3} + 1 \):
\[ \tan 75^\circ = \frac{(\sqrt{3} + 1)^2}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{3 + 1 + 2\sqrt{3}}{3 - 1} = \frac{4 + 2\sqrt{3}}{2} = 2 + \sqrt{3} \]

</details>

3. 🟡 Find sin 105°.
<details>
<summary>Solution</summary>

We can express \( 105^\circ \) as a sum of two standard angles: \( 105^\circ = 60^\circ + 45^\circ \).
Using the sine compound angle formula:
\[ \sin(A + B) = \sin A \cos B + \cos A \sin B \]
Setting \( A = 60^\circ \) and \( B = 45^\circ \):
\[ \sin 105^\circ = \sin(60^\circ + 45^\circ) = \sin 60^\circ \cos 45^\circ + \cos 60^\circ \sin 45^\circ \]
Substitute the standard trigonometric values:
\[ \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 45^\circ = \frac{1}{\sqrt{2}} \]
\[ \cos 60^\circ = \frac{1}{2}, \quad \sin 45^\circ = \frac{1}{\sqrt{2}} \]
Therefore:
\[ \sin 105^\circ = \left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{\sqrt{2}}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right) = \frac{\sqrt{3} + 1}{2\sqrt{2}} \]

</details>

4. 🟡 Find cos 105°.
<details>
<summary>Solution</summary>

 We can express \( 105^\circ \) as a sum of two standard angles: \( 105^\circ = 60^\circ + 45^\circ \).
Using the cosine compound angle formula:
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
Setting \( A = 60^\circ \) and \( B = 45^\circ \):
\[ \cos 105^\circ = \cos(60^\circ + 45^\circ) = \cos 60^\circ \cos 45^\circ - \sin 60^\circ \sin 45^\circ \]
Substitute the standard trigonometric values:
\[ \cos 60^\circ = \frac{1}{2}, \quad \cos 45^\circ = \frac{1}{\sqrt{2}} \]
\[ \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \sin 45^\circ = \frac{1}{\sqrt{2}} \]
Therefore:
\[ \cos 105^\circ = \left(\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right) - \left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{\sqrt{2}}\right) = \frac{1 - \sqrt{3}}{2\sqrt{2}} \]

</details>

5. 🔴 Find tan 165°.
<details>
<summary>Solution</summary>

We can write \( 165^\circ = 180^\circ - 15^\circ \).
Using the quadrant reduction formula \( \tan(180^\circ - \theta) = -\tan \theta \):
\[ \tan 165^\circ = -\tan 15^\circ \]
Now we find \( \tan 15^\circ \) using \( 15^\circ = 45^\circ - 30^\circ \):
\[ \tan 15^\circ = \tan(45^\circ - 30^\circ) = \frac{\tan 45^\circ - \tan 30^\circ}{1 + \tan 45^\circ \tan 30^\circ} \]
Substitute \( \tan 45^\circ = 1 \) and \( \tan 30^\circ = \frac{1}{\sqrt{3}} \):
\[ \tan 15^\circ = \frac{1 - \frac{1}{\sqrt{3}}}{1 + \frac{1}{\sqrt{3}}} = \frac{\sqrt{3} - 1}{\sqrt{3} + 1} \]
Rationalizing the denominator:
\[ \tan 15^\circ = \frac{(\sqrt{3} - 1)^2}{(\sqrt{3} + 1)(\sqrt{3} - 1)} = \frac{3 + 1 - 2\sqrt{3}}{3 - 1} = \frac{4 - 2\sqrt{3}}{2} = 2 - \sqrt{3} \]
Thus:
\[ \tan 165^\circ = -(2 - \sqrt{3}) = \sqrt{3} - 2 \]

</details>

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
<details>
<summary>Solution</summary>

Using the compound angle expansion formula for cosine:
\[ \cos(X + Y) = \cos X \cos Y - \sin X \sin Y \]
Letting \( X = 60^\circ \) and \( Y = A \), we get:
\[ \cos(60^\circ + A) = \cos 60^\circ \cos A - \sin 60^\circ \sin A \]
LHS = RHS. Hence proved.

</details>

7. 🟡 Prove sin(A + B) sin(A − B) = sin²A − sin²B.
<details>
<summary>Solution</summary>

Expand the LHS using compound angle formulas for sine:
\[ \sin(A + B) = \sin A \cos B + \cos A \sin B \]
\[ \sin(A - B) = \sin A \cos B - \cos A \sin B \]
Multiplying these two expressions:
\[ \sin(A + B) \sin(A - B) = (\sin A \cos B + \cos A \sin B)(\sin A \cos B - \cos A \sin B) \]
This is in the form \( (x + y)(x - y) = x^2 - y^2 \):
\[ \sin(A + B) \sin(A - B) = (\sin A \cos B)^2 - (\cos A \sin B)^2 \]
\[ = \sin^2 A \cos^2 B - \cos^2 A \sin^2 B \]
Substitute \( \cos^2 B = 1 - \sin^2 B \) and \( \cos^2 A = 1 - \sin^2 A \):
\[ = \sin^2 A (1 - \sin^2 B) - (1 - \sin^2 A) \sin^2 B \]
\[ = \sin^2 A - \sin^2 A \sin^2 B - \sin^2 B + \sin^2 A \sin^2 B \]
\[ = \sin^2 A - \sin^2 B \]
LHS = RHS. Hence proved.

</details>

8. 🟡 Prove cos(A + B) cos(A − B) = cos²A − sin²B.
<details>
<summary>Solution</summary>

Expand the LHS using compound angle formulas for cosine:
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]
Multiplying these two expressions:
\[ \cos(A + B) \cos(A - B) = (\cos A \cos B - \sin A \sin B)(\cos A \cos B + \sin A \sin B) \]
This is in the form \( (x - y)(x + y) = x^2 - y^2 \):
\[ \cos(A + B) \cos(A - B) = (\cos A \cos B)^2 - (\sin A \sin B)^2 \]
\[ = \cos^2 A \cos^2 B - \sin^2 A \sin^2 B \]
Substitute \( \cos^2 B = 1 - \sin^2 B \) and \( \sin^2 A = 1 - \cos^2 A \):
\[ = \cos^2 A (1 - \sin^2 B) - (1 - \cos^2 A) \sin^2 B \]
\[ = \cos^2 A - \cos^2 A \sin^2 B - \sin^2 B + \cos^2 A \sin^2 B \]
\[ = \cos^2 A - \sin^2 B \]
LHS = RHS. Hence proved.

</details>

9. 🔴 Prove tan A + tan B = sin(A + B)/(cos A cos B).
<details>
<summary>Solution</summary>

Express tangent in terms of sine and cosine:
\[ \text{LHS} = \tan A + \tan B = \frac{\sin A}{\cos A} + \frac{\sin B}{\cos B} \]
Combine the fractions by finding a common denominator:
\[ = \frac{\sin A \cos B + \cos A \sin B}{\cos A \cos B} \]
Apply the sine compound angle formula \( \sin(A + B) = \sin A \cos B + \cos A \sin B \) in the numerator:
\[ = \frac{\sin(A + B)}{\cos A \cos B} = \text{RHS} \]
Hence proved.

</details>

10. 🔴 ⭐ Prove that tan(45° + A) = (1 + tan A)/(1 − tan A).
<details>
<summary>Solution</summary>

Using the tangent compound angle formula:
\[ \tan(X + Y) = \frac{\tan X + \tan Y}{1 - \tan X \tan Y} \]
Substitute \( X = 45^\circ \) and \( Y = A \):
\[ \tan(45^\circ + A) = \frac{\tan 45^\circ + \tan A}{1 - \tan 45^\circ \tan A} \]
Substitute the known value \( \tan 45^\circ = 1 \):
\[ \tan(45^\circ + A) = \frac{1 + \tan A}{1 - 1 \cdot \tan A} = \frac{1 + \tan A}{1 - \tan A} = \text{RHS} \]
Hence proved.

</details>

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
<details>
<summary>Solution</summary>

Since A and B are acute (first quadrant), all trigonometric functions are positive.
Using the Pythagorean identity:
\[ \cos A = \sqrt{1 - \sin^2 A} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \sqrt{1 - \frac{16}{25}} = \frac{3}{5} \]
\[ \sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \sqrt{1 - \frac{144}{169}} = \frac{5}{13} \]
Now, expand \( \cos(A + B) \) using the compound angle formula:
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
Substitute the values:
\[ \cos(A + B) = \left(\frac{3}{5}\right)\left(\frac{12}{13}\right) - \left(\frac{4}{5}\right)\left(\frac{5}{13}\right) \]
\[ = \frac{36}{65} - \frac{20}{65} = \frac{16}{65} \]

</details>

12. 🟡 If tan A = 1/2, tan B = 1/3 (both acute), find tan(A + B).
<details>
<summary>Solution</summary>

Using the tangent compound angle formula:
\[ \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} \]
Substitute the values:
\[ \tan(A + B) = \frac{\frac{1}{2} + \frac{1}{3}}{1 - \left(\frac{1}{2}\right)\left(\frac{1}{3}\right)} = \frac{\frac{5}{6}}{1 - \frac{1}{6}} = \frac{\frac{5}{6}}{\frac{5}{6}} = 1 \]

</details>

13. 🟡 If sin A = 5/13 (QII) and cos B = −4/5 (QII), find sin(A − B).
<details>
<summary>Solution</summary>

In the second quadrant (QII), sine is positive and cosine is negative.
Given:
\[ \sin A = \frac{5}{13} \implies \cos A = -\sqrt{1 - \sin^2 A} = -\sqrt{1 - \frac{25}{169}} = -\frac{12}{13} \]
\[ \cos B = -\frac{4}{5} \implies \sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \frac{16}{25}} = \frac{3}{5} \]
Now, apply the compound angle formula for \( \sin(A - B) \):
\[ \sin(A - B) = \sin A \cos B - \cos A \sin B \]
Substitute the calculated ratios:
\[ \sin(A - B) = \left(\frac{5}{13}\right)\left(-\frac{4}{5}\right) - \left(-\frac{12}{13}\right)\left(\frac{3}{5}\right) \]
\[ = -\frac{20}{65} + \frac{36}{65} = \frac{16}{65} \]

</details>

14. 🔴 If sin A = 3/5, cos B = 15/17 (both acute), find tan(A + B).
<details>
<summary>Solution</summary>

Since A and B are acute:
\[ \sin A = \frac{3}{5} \implies \cos A = \sqrt{1 - \frac{9}{25}} = \frac{4}{5} \implies \tan A = \frac{\sin A}{\cos A} = \frac{3}{4} \]
\[ \cos B = \frac{15}{17} \implies \sin B = \sqrt{1 - \frac{225}{289}} = \frac{8}{17} \implies \tan B = \frac{\sin B}{\cos B} = \frac{8}{15} \]
Using the tangent compound angle formula:
\[ \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} \]
Substitute \( \tan A = \frac{3}{4} \) and \( \tan B = \frac{8}{15} \):
\[ \tan(A + B) = \frac{\frac{3}{4} + \frac{8}{15}}{1 - \left(\frac{3}{4}\right)\left(\frac{8}{15}\right)} \]
Calculate the numerator:
\[ \frac{3}{4} + \frac{8}{15} = \frac{45 + 32}{60} = \frac{77}{60} \]
Calculate the denominator:
\[ 1 - \frac{24}{60} = \frac{36}{60} \]
Therefore:
\[ \tan(A + B) = \frac{77/60}{36/60} = \frac{77}{36} \]

</details>

15. 🔴 ⭐ If cos A = −3/5 (QIII) and sin B = 5/13 (QII), find cos(A − B).
<details>
<summary>Solution</summary>

- Angle A is in QIII (third quadrant): both cosine and sine are negative.
- Angle B is in QII (second quadrant): sine is positive and cosine is negative.
Given:
\[ \cos A = -\frac{3}{5} \implies \sin A = -\sqrt{1 - \cos^2 A} = -\sqrt{1 - \frac{9}{25}} = -\frac{4}{5} \]
\[ \sin B = \frac{5}{13} \implies \cos B = -\sqrt{1 - \sin^2 B} = -\sqrt{1 - \frac{25}{169}} = -\frac{12}{13} \]
Using the compound angle formula for cosine:
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]
Substitute the values:
\[ \cos(A - B) = \left(-\frac{3}{5}\right)\left(-\frac{12}{13}\right) + \left(-\frac{4}{5}\right)\left(\frac{5}{13}\right) \]
\[ = \frac{36}{65} - \frac{20}{65} = \frac{16}{65} \]

</details>

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
<details>
<summary>Solution</summary>

Simplify the LHS using the cosine compound angle formula:
\[ \cos A \cos B - \sin A \sin B = \cos(A + B) \]
Let \( A = 3x \) and \( B = x \):
\[ \cos(3x + x) = \frac{1}{2} \implies \cos 4x = \frac{1}{2} \]
Since \( \cos \frac{\pi}{3} = \frac{1}{2} \), the general solution is:
\[ 4x = 2n\pi \pm \frac{\pi}{3}, \quad n \in \mathbb{Z} \]
Dividing by 4:
\[ x = \frac{n\pi}{2} \pm \frac{\pi}{12}, \quad n \in \mathbb{Z} \]

</details>

17. 🟡 Solve (tan x + tan 2x)/(1 − tan x tan 2x) = 1.
<details>
<summary>Solution</summary>

The LHS is the tangent compound angle formula:
\[ \frac{\tan A + \tan B}{1 - \tan A \tan B} = \tan(A + B) \]
Let \( A = 2x \) and \( B = x \):
\[ \tan(2x + x) = 1 \implies \tan 3x = 1 \]
The general solution for \( \tan \theta = \tan \alpha \) is \( \theta = n\pi + \alpha \).
Since \( \tan \frac{\pi}{4} = 1 \):
\[ 3x = n\pi + \frac{\pi}{4}, \quad n \in \mathbb{Z} \]
\[ x = \frac{n\pi}{3} + \frac{\pi}{12}, \quad n \in \mathbb{Z} \]
To ensure \( \tan x \) and \( \tan 2x \) are defined, we must check that:
- \( x \neq (2k+1)\frac{\pi}{2} \)
- \( 2x \neq (2k+1)\frac{\pi}{2} \implies x \neq (2k+1)\frac{\pi}{4} \)
Let's see if \( x = \frac{4n+1}{12}\pi \) can equal \( (2m+1)\frac{\pi}{4} \):
\[ \frac{4n+1}{12} = \frac{2m+1}{4} \implies 4n+1 = 6m+3 \implies 2n - 3m = 1 \]
If \( m \) is odd, say \( m = 2k+1 \), then:
\[ 2n - 6k - 3 = 1 \implies 2n - 6k = 4 \implies n = 3k + 2 \]
Thus, for \( n = 3k+2 \), the value of \( \tan 2x \) is undefined.
Therefore, the general solution is:
\[ x = \frac{n\pi}{3} + \frac{\pi}{12}, \quad n \in \mathbb{Z} \quad \text{where } n \neq 3k+2 \text{ for any } k \in \mathbb{Z} \]

</details>

18. 🟡 Solve sin(x + 30°) = cos x.
<details>
<summary>Solution</summary>

Using the co-function identity \( \cos x = \sin(90^\circ - x) \), the equation becomes:
\[ \sin(x + 30^\circ) = \sin(90^\circ - x) \]
The general solution for \( \sin \theta = \sin \alpha \) is \( \theta = n \cdot 180^\circ + (-1)^n \alpha \).
- **Case 1: \( n \) is even (\( n = 2k \))**
\[ x + 30^\circ = 360^\circ k + (90^\circ - x) \]
\[ 2x = 360^\circ k + 60^\circ \implies x = 180^\circ k + 30^\circ \]
- **Case 2: \( n \) is odd (\( n = 2k + 1 \))**
\[ x + 30^\circ = (2k + 1)180^\circ - (90^\circ - x) \]
\[ x + 30^\circ = 360^\circ k + 180^\circ - 90^\circ + x \]
\[ 30^\circ = 90^\circ \quad (\text{Impossible}) \]
Therefore, the solution is:
\[ x = 180^\circ k + 30^\circ \quad (\text{or } x = k\pi + \frac{\pi}{6}, \, k \in \mathbb{Z}) \]

</details>

19. 🔴 Solve sin 2x cos x + cos 2x sin x = 0.
<details>
<summary>Solution</summary>

Simplify the LHS using the sine compound angle formula:
\[ \sin A \cos B + \cos A \sin B = \sin(A + B) \]
Let \( A = 2x \) and \( B = x \):
\[ \sin(2x + x) = 0 \implies \sin 3x = 0 \]
The general solution for \( \sin \theta = 0 \) is:
\[ 3x = n\pi \implies x = \frac{n\pi}{3}, \quad n \in \mathbb{Z} \]

</details>

20. 🔴 ⭐ Solve cos(x + π/4) − cos(x − π/4) = √2 sin x. (This is an identity — prove it first.)
<details>
<summary>Solution</summary>

First, let us simplify the expression on the LHS using cosine compound angle formulas:
\[ \cos\left(x + \frac{\pi}{4}\right) = \cos x \cos\frac{\pi}{4} - \sin x \sin\frac{\pi}{4} = \frac{\cos x - \sin x}{\sqrt{2}} \]
\[ \cos\left(x - \frac{\pi}{4}\right) = \cos x \cos\frac{\pi}{4} + \sin x \sin\frac{\pi}{4} = \frac{\cos x + \sin x}{\sqrt{2}} \]
Subtracting the two:
\[ \text{LHS} = \frac{\cos x - \sin x - (\cos x + \sin x)}{\sqrt{2}} = \frac{-2\sin x}{\sqrt{2}} = -\sqrt{2} \sin x \]
Now substitute LHS back into the equation:
\[ -\sqrt{2} \sin x = \sqrt{2} \sin x \]
\[ 2\sqrt{2} \sin x = 0 \implies \sin x = 0 \]
The general solution for \( \sin x = 0 \) is:
\[ x = n\pi, \quad n \in \mathbb{Z} \]

</details>

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
<details>
<summary>Solution</summary>

Using the sine difference formula:
\[ \sin A \cos B - \cos A \sin B = \sin(A - B) \]
Setting \( A = 5x \) and \( B = x \):
\[ \sin 5x \cos x - \cos 5x \sin x = \sin(5x - x) = \sin 4x \]

</details>

22. 🟢 Simplify cos 4x cos x + sin 4x sin x.
<details>
<summary>Solution</summary>

Using the cosine difference formula:
\[ \cos A \cos B + \sin A \sin B = \cos(A - B) \]
Setting \( A = 4x \) and \( B = x \):
\[ \cos 4x \cos x + \sin 4x \sin x = \cos(4x - x) = \cos 3x \]

</details>

23. 🟡 Write sin 75° cos 15° + cos 75° sin 15° as a single trig function.
<details>
<summary>Solution</summary>

Using the sine sum formula:
\[ \sin A \cos B + \cos A \sin B = \sin(A + B) \]
Setting \( A = 75^\circ \) and \( B = 15^\circ \):
\[ \sin 75^\circ \cos 15^\circ + \cos 75^\circ \sin 15^\circ = \sin(75^\circ + 15^\circ) = \sin 90^\circ \]
Evaluating it:
\[ \sin 90^\circ = 1 \]

</details>

24. 🟡 Simplify (tan 3x − tan x)/(1 + tan 3x tan x).
<details>
<summary>Solution</summary>

Using the tangent difference formula:
\[ \frac{\tan A - \tan B}{1 + \tan A \tan B} = \tan(A - B) \]
Setting \( A = 3x \) and \( B = x \):
\[ \frac{\tan 3x - \tan x}{1 + \tan 3x \tan x} = \tan(3x - x) = \tan 2x \]

</details>

25. 🔴 Simplify cos(A + B) cos B + sin(A + B) sin B.
<details>
<summary>Solution</summary>

Using the cosine difference formula:
\[ \cos X \cos Y + \sin X \sin Y = \cos(X - Y) \]
Setting \( X = A + B \) and \( Y = B \):
\[ \cos(A + B) \cos B + \sin(A + B) \sin B = \cos((A + B) - B) = \cos A \]

</details>

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
<details>
<summary>Solution</summary>

*Note: For the identity \( (1 - \tan A)(1 - \tan B) = 2 \) to hold, we require \( \tan(A + B) = -1 \), which corresponds to \( A + B = 135^\circ \) (or \( -45^\circ \)). If the condition is \( A + B = 135^\circ \):*

Taking the tangent of both sides:
\[ \tan(A + B) = \tan(135^\circ) = -1 \]
Using the tangent compound angle formula:
\[ \frac{\tan A + \tan B}{1 - \tan A tan B} = -1 \]
Cross-multiplying:
\[ \tan A + \tan B = -1 + \tan A \tan B \]
Rearranging terms:
\[ \tan A \tan B - \tan A - \tan B = 1 \]
Adding 1 to both sides:
\[ 1 - \tan A - \tan B + \tan A \tan B = 2 \]
Factoring the LHS:
\[ (1 - \tan A)(1 - \tan B) = 2 \]
Hence proved.

</details>

27. 🔴 If A + B + C = π, prove that tan A + tan B + tan C = tan A tan B tan C.
<details>
<summary>Solution</summary>

Given \( A + B + C = \pi \):
\[ A + B = \pi - C \]
Take the tangent of both sides:
\[ \tan(A + B) = \tan(\pi - C) \]
Use the compound angle formula on the LHS, and reduction formula on the RHS:
\[ \frac{\tan A + \tan B}{1 - \tan A \tan B} = -\tan C \]
Cross-multiplying:
\[ \tan A + \tan B = -\tan C (1 - \tan A \tan B) \]
\[ \tan A + \tan B = -\tan C + \tan A \tan B \tan C \]
Rearranging:
\[ \tan A + \tan B + \tan C = \tan A \tan B \tan C \]
Hence proved.

</details>

28. 🔴 If A + B = π/4, prove that (cot A − 1)(cot B − 1) = 2.
<details>
<summary>Solution</summary>

Given \( A + B = \frac{\pi}{4} \):
Take cotangent on both sides:
\[ \cot(A + B) = \cot\left(\frac{\pi}{4}\right) = 1 \]
Use the cotangent compound angle formula:
\[ \frac{\cot A \cot B - 1}{\cot B + \cot A} = 1 \]
Cross-multiplying:
\[ \cot A \cot B - 1 = \cot A + \cot B \]
Rearranging:
\[ \cot A \cot B - \cot A - \cot B = 1 \]
Add 1 to both sides:
\[ \cot A \cot B - \cot A - \cot B + 1 = 2 \]
Factor the expression:
\[ (\cot A - 1)(\cot B - 1) = 2 \]
Hence proved.

</details>

29. 🔴 ⭐ If sin(A + B) = 1 and sin(A − B) = 1/2, find A and B.
<details>
<summary>Solution</summary>

Assuming acute/principal values:
\[ \sin(A + B) = 1 \implies A + B = 90^\circ \quad \text{--- (Equation 1)} \]
\[ \sin(A - B) = \frac{1}{2} \implies A - B = 30^\circ \quad \text{--- (Equation 2)} \]
Add Equation 1 and Equation 2:
\[ 2A = 120^\circ \implies A = 60^\circ \]
Subtract Equation 2 from Equation 1:
\[ 2B = 60^\circ \implies B = 30^\circ \]
Thus, \( A = 60^\circ \) (or \( \frac{\pi}{3} \)) and \( B = 30^\circ \) (or \( \frac{\pi}{6} \)).

</details>

30. 🔴 If x + y = 3 − cos 4θ and x − y = 4 sin 2θ, show that √x + √y = 2.
<details>
<summary>Solution</summary>

Given:
\[ x + y = 3 - \cos 4\theta \quad \text{--- (Equation 1)} \]
\[ x - y = 4 \sin 2\theta \quad \text{--- (Equation 2)} \]
Using the double angle identity \( \cos 4\theta = 1 - 2\sin^2 2\theta \), rewrite Equation 1:
\[ x + y = 3 - (1 - 2\sin^2 2\theta) = 2 + 2\sin^2 2\theta \]
Let \( P = \sqrt{x} + \sqrt{y} \). Squaring both sides:
\[ P^2 = x + y + 2\sqrt{xy} \]
We can find \( 4xy \) using the identity \( (x + y)^2 - (x - y)^2 = 4xy \):
\[ 4xy = (2 + 2\sin^2 2\theta)^2 - (4\sin 2\theta)^2 \]
\[ = 4(1 + \sin^2 2\theta)^2 - 16\sin^2 2\theta \]
\[ = 4(1 + 2\sin^2 2\theta + \sin^4 2\theta) - 16\sin^2 2\theta \]
\[ = 4 + 8\sin^2 2\theta + 4\sin^4 2\theta - 16\sin^2 2\theta \]
\[ = 4 - 8\sin^2 2\theta + 4\sin^4 2\theta \]
\[ = 4(1 - \sin^2 2\theta)^2 = 4(\cos^2 2\theta)^2 = 4\cos^4 2\theta \]
Dividing by 4:
\[ xy = \cos^4 2\theta \implies \sqrt{xy} = \cos^2 2\theta \]
Substitute \( x + y \) and \( \sqrt{xy} \) into the expression for \( P^2 \):
\[ P^2 = (2 + 2\sin^2 2\theta) + 2\cos^2 2\theta = 2 + 2(\sin^2 2\theta + \cos^2 2\theta) = 2 + 2(1) = 4 \]
Thus:
\[ P = \sqrt{x} + \sqrt{y} = \sqrt{4} = 2 \]
Hence proved.

</details>

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
<details>
<summary>Solution</summary>

Write the equations as:
\[ \frac{x}{a} = \cos(\theta + \alpha) = \cos \theta \cos \alpha - \sin \theta \sin \alpha \quad \text{--- (1)} \]
\[ \frac{y}{b} = \cos(\theta + \beta) = \cos \theta \cos \beta - \sin \theta \sin \beta \quad \text{--- (2)} \]
We solve for \( \cos \theta \) and \( \sin \theta \).
Multiply (1) by \( \sin \beta \) and (2) by \( \sin \alpha \), then subtract:
\[ \frac{x}{a}\sin \beta - \frac{y}{b}\sin \alpha = \cos \theta(\sin \beta \cos \alpha - \cos \beta \sin \alpha) = \cos \theta \sin(\beta - \alpha) \]
\[ \cos \theta = \frac{\frac{x}{a}\sin \beta - \frac{y}{b}\sin \alpha}{\sin(\beta - \alpha)} \]
Similarly, multiply (2) by \( \cos \alpha \) and (1) by \( \cos \beta \), then subtract:
\[ \frac{y}{b}\cos \alpha - \frac{x}{a}\cos \beta = \sin \theta(\sin \beta \cos \alpha - \cos \beta \sin \alpha) = \sin \theta \sin(\beta - \alpha) \]
\[ \sin \theta = \frac{\frac{y}{b}\cos \alpha - \frac{x}{a}\cos \beta}{\sin(\beta - \alpha)} \]
Using the identity \( \sin^2 \theta + \cos^2 \theta = 1 \):
\[ \left( \frac{\frac{x}{a}\sin \beta - \frac{y}{b}\sin \alpha}{\sin(\beta - \alpha)} \right)^2 + \left( \frac{\frac{y}{b}\cos \alpha - \frac{x}{a}\cos \beta}{\sin(\beta - \alpha)} \right)^2 = 1 \]
Multiply through by \( \sin^2(\beta - \alpha) \) and expand:
\[ \frac{x^2}{a^2}\sin^2 \beta + \frac{y^2}{b^2}\sin^2 \alpha - \frac{2xy}{ab}\sin \alpha \sin \beta + \frac{y^2}{b^2}\cos^2 \alpha + \frac{x^2}{a^2}\cos^2 \beta - \frac{2xy}{ab}\cos \alpha \cos \beta = \sin^2(\beta - \alpha) \]
Group the coefficients of \( x^2/a^2 \) and \( y^2/b^2 \):
\[ \frac{x^2}{a^2}(\sin^2 \beta + \cos^2 \beta) + \frac{y^2}{b^2}(\sin^2 \alpha + \cos^2 \alpha) - \frac{2xy}{ab}(\cos \alpha \cos \beta + \sin \alpha \sin \beta) = \sin^2(\beta - \alpha) \]
Since \( \sin^2 \phi + \cos^2 \phi = 1 \) and \( \cos \alpha \cos \beta + \sin \alpha \sin \beta = \cos(\beta - \alpha) \):
\[ \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{2xy}{ab}\cos(\beta - \alpha) = \sin^2(\beta - \alpha) \]

</details>

32. 🔴 Eliminate θ: u = tan(θ + α), v = tan(θ + β).
<details>
<summary>Solution</summary>

Notice that:
\[ (\theta + \alpha) - (\theta + \beta) = \alpha - \beta \]
Taking tangent on both sides:
\[ \tan((\theta + \alpha) - (\theta + \beta)) = \tan(\alpha - \beta) \]
Apply the tangent difference formula:
\[ \frac{\tan(\theta + \alpha) - \tan(\theta + \beta)}{1 + \tan(\theta + \alpha)\tan(\theta + \beta)} = \tan(\alpha - \beta) \]
Substitute \( u = \tan(\theta + \alpha) \) and \( v = \tan(\theta + \beta) \):
\[ \frac{u - v}{1 + uv} = \tan(\alpha - \beta) \]
\[ u - v = (1 + uv)\tan(\alpha - \beta) \]

</details>

33. 🔴 ⭐ If sin θ + cos θ = √2 cos α, prove that cos θ − sin θ = √2 sin α.
<details>
<summary>Solution</summary>

Given:
\[ \sin \theta + \cos \theta = \sqrt{2} \cos \alpha \]
Squaring both sides:
\[ (\sin \theta + \cos \theta)^2 = 2 \cos^2 \alpha \]
\[ \sin^2 \theta + \cos^2 \theta + 2 \sin \theta \cos \theta = 2 \cos^2 \alpha \]
\[ 1 + 2 \sin \theta \cos \theta = 2 \cos^2 \alpha \implies 2 \sin \theta \cos \theta = 2 \cos^2 \alpha - 1 \]
Now, let \( k = \cos \theta - \sin \theta \). Squaring \( k \):
\[ k^2 = (\cos \theta - \sin \theta)^2 = \cos^2 \theta + \sin^2 \theta - 2 \sin \theta \cos \theta \]
\[ k^2 = 1 - 2 \sin \theta \cos \theta \]
Substitute the expression for \( 2 \sin \theta \cos \theta \) we obtained above:
\[ k^2 = 1 - (2 \cos^2 \alpha - 1) = 2 - 2 \cos^2 \alpha = 2(1 - \cos^2 \alpha) = 2 \sin^2 \alpha \]
Taking the positive square root:
\[ k = \cos \theta - \sin \theta = \sqrt{2} \sin \alpha \]
Hence proved.

</details>

34. 🔴 If tan(θ + α) = n tan(θ − α), prove that (n + 1) sin 2α = (n − 1) sin 2θ.
<details>
<summary>Solution</summary>

Given:
\[ \frac{\tan(\theta + \alpha)}{\tan(\theta - \alpha)} = \frac{n}{1} \]
Convert tangents to sines and cosines:
\[ \frac{\sin(\theta + \alpha)}{\cos(\theta + \alpha)} \cdot \frac{\cos(\theta - \alpha)}{\sin(\theta - \alpha)} = n \]
\[ \frac{\sin(\theta + \alpha)\cos(\theta - \alpha)}{\cos(\theta + \alpha)\sin(\theta - \alpha)} = \frac{n}{1} \]
Applying Componendo and Dividendo:
\[ \frac{\sin(\theta + \alpha)\cos(\theta - \alpha) + \cos(\theta + \alpha)\sin(\theta - \alpha)}{\sin(\theta + \alpha)\cos(\theta - \alpha) - \cos(\theta + \alpha)\sin(\theta - \alpha)} = \frac{n + 1}{n - 1} \]
Apply compound angle formulas \( \sin(X \pm Y) \) in the numerator and denominator:
- Numerator: \( \sin((\theta + \alpha) + (\theta - \alpha)) = \sin 2\theta \)
- Denominator: \( \sin((\theta + \alpha) - (\theta - \alpha)) = \sin 2\alpha \)
Thus:
\[ \frac{\sin 2\theta}{\sin 2\alpha} = \frac{n + 1}{n - 1} \]
Cross-multiplying:
\[ (n - 1) \sin 2\theta = (n + 1) \sin 2\alpha \]
Hence proved.

</details>

35. 🔴 If sin(θ + α) = a and sin(θ + β) = b, prove that cos(α − β) = ab ± √((1 − a²)(1 − b²)).
<details>
<summary>Solution</summary>

Let \( X = \theta + \alpha \) and \( Y = \theta + \beta \).
Then \( X - Y = (\theta + \alpha) - (\theta + \beta) = \alpha - \beta \).
We are given:
\[ \sin X = a \implies \cos X = \pm \sqrt{1 - a^2} \]
\[ \sin Y = b \implies \cos Y = \pm \sqrt{1 - b^2} \]
Expand \( \cos(\alpha - \beta) \) as \( \cos(X - Y) \):
\[ \cos(X - Y) = \cos X \cos Y + \sin X \sin Y \]
Substitute the known values:
\[ \cos(\alpha - \beta) = \left(\pm \sqrt{1 - a^2}\right)\left(\pm \sqrt{1 - b^2}\right) + a \cdot b \]
\[ \cos(\alpha - \beta) = ab \pm \sqrt{(1 - a^2)(1 - b^2)} \]
Hence proved.

</details>

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
<details>
<summary>Solution</summary>

Expand using the compound angle formulas:
\[ \sin(A + B) = \sin A \cos B + \cos A \sin B \]
\[ \sin(A - B) = \sin A \cos B - \cos A \sin B \]
Subtract the second equation from the first:
\[ \sin(A + B) - \sin(A - B) = (\sin A \cos B + \cos A \sin B) - (\sin A \cos B - \cos A \sin B) \]
\[ = 2 \cos A \sin B \]

</details>

37. 🟡 Express cos(A + B) + cos(A − B) as a product.
<details>
<summary>Solution</summary>

Expand using the compound angle formulas:
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]
Add the two equations:
\[ \cos(A + B) + \cos(A - B) = 2 \cos A \cos B \]

</details>

38. 🟡 Express cos(A − B) − cos(A + B) as a product.
<details>
<summary>Solution</summary>

Expand using the compound angle formulas:
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
Subtract the second equation from the first:
\[ \cos(A - B) - \cos(A + B) = (\cos A \cos B + \sin A \sin B) - (\cos A \cos B - \sin A \sin B) \]
\[ = 2 \sin A \sin B \]

</details>

39. 🔴 Find the value of sin 75° − sin 15°.
<details>
<summary>Solution</summary>

Using the identity:
\[ \sin(x + y) - \sin(x - y) = 2 \cos x \sin y \]
Let \( x + y = 75^\circ \) and \( x - y = 15^\circ \).
Solving for \( x \) and \( y \):
\[ x = \frac{75^\circ + 15^\circ}{2} = 45^\circ \]
\[ y = \frac{75^\circ - 15^\circ}{2} = 30^\circ \]
Substitute these values:
\[ \sin 75^\circ - \sin 15^\circ = 2 \cos 45^\circ \sin 30^\circ \]
Substitute the standard ratios:
\[ = 2 \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{2}\right) = \frac{1}{\sqrt{2}} \]

</details>

40. 🔴 ⭐ Show that (sin 7x + sin 5x)/(cos 7x + cos 5x) = tan 6x.
<details>
<summary>Solution</summary>

Using the sum-to-product formulas:
\[ \sin C + \sin D = 2 \sin\left(\frac{C + D}{2}\right) \cos\left(\frac{C - D}{2}\right) \]
\[ \cos C + \cos D = 2 \cos\left(\frac{C + D}{2}\right) \cos\left(\frac{C - D}{2}\right) \]
Letting \( C = 7x \) and \( D = 5x \):
\[ \sin 7x + \sin 5x = 2 \sin 6x \cos x \]
\[ \cos 7x + \cos 5x = 2 \cos 6x \cos x \]
Dividing the two expressions:
\[ \frac{\sin 7x + \sin 5x}{\cos 7x + \cos 5x} = \frac{2 \sin 6x \cos x}{2 \cos 6x \cos x} = \frac{\sin 6x}{\cos 6x} = \tan 6x \]
Hence proved.

</details>

---

## Stage 4: Type Mixer

1. 🟡 If tan A = 2 and tan B = 3, find tan(A + B). What can you conclude about A + B?<br>
<details>
<summary>Solution</summary>

Using the tangent compound angle formula:
\[ \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} \]
Substitute \( \tan A = 2 \) and \( \tan B = 3 \):
\[ \tan(A + B) = \frac{2 + 3}{1 - (2)(3)} = \frac{5}{1 - 6} = \frac{5}{-5} = -1 \]
Since \( \tan A = 2 > 0 \) and \( \tan B = 3 > 0 \), both A and B are acute angles in the first quadrant, i.e., \( A, B \in \left(0, \frac{\pi}{2}\right) \).
This means:
\[ A + B \in (0, \pi) \]
Since \( \tan(A + B) = -1 \) and \( A + B \) lies in the range \( (0, \pi) \), \( A + B \) must be in the second quadrant:
\[ A + B = 135^\circ \quad \left(\text{or } \frac{3\pi}{4}\right) \]

</details>

2. 🟡 Prove that cos(60° + A) + sin(30° + A) = cos A.
<details>
<summary>Solution</summary>

Expand both terms using compound angle formulas:
\[ \cos(60^\circ + A) = \cos 60^\circ \cos A - \sin 60^\circ \sin A = \frac{1}{2}\cos A - \frac{\sqrt{3}}{2}\sin A \]
\[ \sin(30^\circ + A) = \sin 30^\circ \cos A + \cos 30^\circ \sin A = \frac{1}{2}\cos A + \frac{\sqrt{3}}{2}\sin A \]
Adding them together:
\[ \text{LHS} = \left(\frac{1}{2}\cos A - \frac{\sqrt{3}}{2}\sin A\right) + \left(\frac{1}{2}\cos A + \frac{\sqrt{3}}{2}\sin A\right) = \frac{1}{2}\cos A + \frac{1}{2}\cos A = \cos A = \text{RHS} \]
Hence proved.

</details>

3. 🔴 ⭐ If sin A = 3/5 and cos B = 12/13, where A and B are acute, find sin(A − B) and cos(A + B).
<details>
<summary>Solution</summary>

Since A and B are acute:
\[ \sin A = \frac{3}{5} \implies \cos A = \sqrt{1 - \left(\frac{3}{5}\right)^2} = \frac{4}{5} \]
\[ \cos B = \frac{12}{13} \implies \sin B = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13} \]
Now, calculate the required values:
1. **\( \sin(A - B) \):**
\[ \sin(A - B) = \sin A \cos B - \cos A \sin B \]
\[ = \left(\frac{3}{5}\right)\left(\frac{12}{13}\right) - \left(\frac{4}{5}\right)\left(\frac{5}{13}\right) = \frac{36}{65} - \frac{20}{65} = \frac{16}{65} \]
2. **\( \cos(A + B) \):**
\[ \cos(A + B) = \cos A \cos B - \sin A \sin B \]
\[ = \left(\frac{4}{5}\right)\left(\frac{12}{13}\right) - \left(\frac{3}{5}\right)\left(\frac{5}{13}\right) = \frac{48}{65} - \frac{15}{65} = \frac{33}{65} \]

</details>

4. 🔴 If A + B = 45°, prove that (cot A − 1)(cot B − 1) = 2.
<details>
<summary>Solution</summary>

Given \( A + B = 45^\circ \):
Take cotangent on both sides:
\[ \cot(A + B) = \cot 45^\circ = 1 \]
Using the cotangent compound angle formula:
\[ \frac{\cot A \cot B - 1}{\cot B + \cot A} = 1 \]
Cross-multiplying:
\[ \cot A \cot B - 1 = \cot A + \cot B \]
Rearranging:
\[ \cot A \cot B - \cot A - \cot B = 1 \]
Adding 1 to both sides:
\[ \cot A \cot B - \cot A - \cot B + 1 = 2 \]
Factoring the LHS:
\[ (\cot A - 1)(\cot B - 1) = 2 \]
Hence proved.

</details>

5. 🔴 Show that sin(45° + A) cos(45° − B) + cos(45° + A) sin(45° − B) = cos(A − B).
<details>
<summary>Solution</summary>

Apply the sine compound angle formula \( \sin(X + Y) = \sin X \cos Y + \cos X \sin Y \) with:
- \( X = 45^\circ + A \)
- \( Y = 45^\circ - B \)

This gives:
\[ \text{LHS} = \sin((45^\circ + A) + (45^\circ - B)) = \sin(90^\circ + A - B) \]
Using the identity \( \sin(90^\circ + \theta) = \cos \theta \):
\[ \sin(90^\circ + (A - B)) = \cos(A - B) = \text{RHS} \]
Hence proved.

</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find sin 15° using compound angle formula. **(2 marks)**

<details>
<summary>Solution</summary>

```
sin 15° = sin(45° − 30°)
= sin 45° cos 30° − cos 45° sin 30°
= (1/√2)(√3/2) − (1/√2)(1/2)
= (√3 − 1)/(2√2)
```

</details>

---

**Q2.** 🟡 If tan A = 1/2, tan B = 1/3, find tan(A + B) and deduce A + B. **(3 marks)**

<details>
<summary>Solution</summary>

```
tan(A + B) = (1/2 + 1/3)/(1 − 1/6) = (5/6)/(5/6) = 1
A + B = 45°
```

</details>

---

**Q3.** 🟡 Prove that cos(A + B) cos B + sin(A + B) sin B = cos A. **(2 marks)**

<details>
<summary>Solution</summary>

```
LHS = cos((A + B) − B) = cos A = RHS ✓
```

</details>

---

**Q4.** 🔴 If sin(A + B) = 1 and sin(A − B) = 1/2, find A and B (0 < A, B < 90°). **(3 marks)**

<details>
<summary>Solution</summary>

```
A + B = 90°
A − B = 30°
Solving: A = 60°, B = 30°
```

</details>

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
<details>
<summary>Solution</summary>

By standard trigonometric compound angle expansion, we have:
\[ \sin(A + B) = \sin A \cos B + \cos A \sin B \]

**Answer: (b)**
</details>

2. 🟢 cos(A − B) equals:
   (a) cos A cos B + sin A sin B   (b) cos A cos B − sin A sin B   (c) sin A cos B + cos A sin B   (d) sin A cos B − cos A sin B
<details>
<summary>Solution</summary>

By standard trigonometric compound angle expansion, we have:
\[ \cos(A - B) = \cos A \cos B + \sin A \sin B \]

**Answer: (a)**
</details>

3. 🟡 sin 15° equals:
   (a) (√3 + 1)/(2√2)   (b) (√3 − 1)/(2√2)   (c) (√3 − 1)/2   (d) (√3 + 1)/2
<details>
<summary>Solution</summary>

We can express \( 15^\circ \) as:
\[ 15^\circ = 45^\circ - 30^\circ \]
Applying the sine difference compound angle formula:
\[ \sin 15^\circ = \sin(45^\circ - 30^\circ) = \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ \]
\[ = \left(\frac{1}{\sqrt{2}}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{2}\right) = \frac{\sqrt{3} - 1}{2\sqrt{2}} \]

**Answer: (b)**
</details>

4. 🟡 cos 75° equals:
   (a) (√3 − 1)/(2√2)   (b) (√3 + 1)/(2√2)   (c) (√3 − 1)/2   (d) (√3 + 1)/2
<details>
<summary>Solution</summary>

Since \( 75^\circ = 90^\circ - 15^\circ \):
\[ \cos 75^\circ = \sin 15^\circ \]
Using the value of \( \sin 15^\circ \) (derived as \( \frac{\sqrt{3} - 1}{2\sqrt{2}} \)):
\[ \cos 75^\circ = \frac{\sqrt{3} - 1}{2\sqrt{2}} \]

**Answer: (a)**
</details>

5. 🟡 tan(45° + A) equals:
   (a) (1 − tan A)/(1 + tan A)   (b) (1 + tan A)/(1 − tan A)   (c) (tan A − 1)/(tan A + 1)   (d) 1
<details>
<summary>Solution</summary>

Applying the tangent sum compound angle formula:
\[ \tan(45^\circ + A) = \frac{\tan 45^\circ + \tan A}{1 - \tan 45^\circ \tan A} \]
Since \( \tan 45^\circ = 1 \):
\[ \tan(45^\circ + A) = \frac{1 + \tan A}{1 - \tan A} \]

**Answer: (b)**
</details>

6. 🟡 If sin A = 4/5, cos A = 3/5, then sin 2A = ?<br>
   (a) 24/25   (b) 12/25   (c) 7/25   (d) 9/25
<details>
<summary>Solution</summary>

Using the double angle identity for sine:
\[ \sin 2A = 2 \sin A \cos A \]
Substitute the given values:
\[ \sin 2A = 2 \left(\frac{4}{5}\right)\left(\frac{3}{5}\right) = \frac{24}{25} \]

**Answer: (a)**
</details>

7. 🟡 cos(60° + A) + sin(30° + A) equals:
   (a) sin A   (b) cos A   (c) 0   (d) 1
<details>
<summary>Solution</summary>

Expanding each term using compound angle formulas:
\[ \cos(60^\circ + A) = \cos 60^\circ \cos A - \sin 60^\circ \sin A = \frac{1}{2}\cos A - \frac{\sqrt{3}}{2}\sin A \]
\[ \sin(30^\circ + A) = \sin 30^\circ \cos A + \cos 30^\circ \sin A = \frac{1}{2}\cos A + \frac{\sqrt{3}}{2}\sin A \]
Adding these two expressions:
\[ \cos(60^\circ + A) + \sin(30^\circ + A) = \frac{1}{2}\cos A + \frac{1}{2}\cos A = \cos A \]

**Answer: (b)**
</details>

8. 🟡 If A + B = 45° and tan A = 1/2, then tan B = ?<br>
   (a) 1/3   (b) 2/3   (c) 1/4   (d) 2/5
<details>
<summary>Solution</summary>

Since \( A + B = 45^\circ \):
\[ \tan(A + B) = \tan 45^\circ = 1 \]
Using the compound angle expansion for tangent:
\[ \frac{\tan A + \tan B}{1 - \tan A \tan B} = 1 \]
Substitute \( \tan A = 1/2 \):
\[ \frac{1/2 + \tan B}{1 - (1/2)\tan B} = 1 \]
\[ \frac{1}{2} + \tan B = 1 - \frac{1}{2}\tan B \]
\[ \frac{3}{2}\tan B = \frac{1}{2} \implies \tan B = \frac{1}{3} \]

**Answer: (a)**
</details>

9. 🟡 sin(π/4 + x) + sin(π/4 − x) equals:
   (a) √2 sin x   (b) √2 cos x   (c) 2 sin x   (d) 2 cos x
<details>
<summary>Solution</summary>

Using the sum-to-product formula \( \sin C + \sin D = 2 \sin\left(\frac{C+D}{2}\right)\cos\left(\frac{C-D}{2}\right) \):
Let \( C = \frac{\pi}{4} + x \) and \( D = \frac{\pi}{4} - x \):
\[ \sin\left(\frac{\pi}{4} + x\right) + \sin\left(\frac{\pi}{4} - x\right) = 2 \sin\left(\frac{\pi}{4}\right)\cos(x) \]
Substitute \( \sin\frac{\pi}{4} = \frac{1}{\sqrt{2}} \):
\[ = 2\left(\frac{1}{\sqrt{2}}\right)\cos x = \sqrt{2}\cos x \]

**Answer: (b)**
</details>

10. 🟡 If sin(A + B) = 1/2 and sin(A − B) = 0, then A = ?<br>
    (a) 15°   (b) 30°   (c) 45°   (d) 60°
<details>
<summary>Solution</summary>

Given \( \sin(A - B) = 0 \implies A - B = 0 \implies A = B \) (taking the principal value).
Substitute \( B = A \) into the first equation:
\[ \sin(A + A) = \sin 2A = \frac{1}{2} \]
For acute angles:
\[ 2A = 30^\circ \implies A = 15^\circ \]

**Answer: (a)**
</details>

11. 🟡 sin 105° equals:
    (a) (√3 + 1)/(2√2)   (b) (√3 − 1)/(2√2)   (c) √3/2   (d) 1/2
<details>
<summary>Solution</summary>

Since \( 105^\circ = 180^\circ - 75^\circ \):
\[ \sin 105^\circ = \sin 75^\circ = \sin(45^\circ + 30^\circ) \]
Applying the sine sum formula:
\[ \sin(45^\circ + 30^\circ) = \sin 45^\circ \cos 30^\circ + \cos 45^\circ \sin 30^\circ \]
\[ = \left(\frac{1}{\sqrt{2}}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{2}\right) = \frac{\sqrt{3} + 1}{2\sqrt{2}} \]

**Answer: (a)**
</details>

12. 🟡 cos(90° + A) equals:
    (a) sin A   (b) −sin A   (c) cos A   (d) −cos A
<details>
<summary>Solution</summary>

Using the cosine compound angle formula:
\[ \cos(90^\circ + A) = \cos 90^\circ \cos A - \sin 90^\circ \sin A \]
Since \( \cos 90^\circ = 0 \) and \( \sin 90^\circ = 1 \):
\[ \cos(90^\circ + A) = 0 \cdot \cos A - 1 \cdot \sin A = -\sin A \]

**Answer: (b)**
</details>

13. 🟡 sin(π/3 + θ) − sin(π/3 − θ) equals:
    (a) sin θ   (b) cos θ   (c) √3 sin θ   (d) √3 cos θ
<details>
<summary>Solution</summary>

Using the sine difference compound angle formula, or identity \( \sin(X + Y) - \sin(X - Y) = 2\cos X\sin Y \):
\[ \sin\left(\frac{\pi}{3} + \theta\right) - \sin\left(\frac{\pi}{3} - \theta\right) = 2 \cos\left(\frac{\pi}{3}\right) \sin\theta \]
Since \( \cos\left(\frac{\pi}{3}\right) = \frac{1}{2} \):
\[ = 2\left(\frac{1}{2}\right)\sin\theta = \sin\theta \]

**Answer: (a)**
</details>

14. 🟡 If tan A = 1/3 and tan B = 1/2, A + B = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Using the tangent compound angle formula:
\[ \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} \]
Substitute \( \tan A = 1/3 \) and \( \tan B = 1/2 \):
\[ \tan(A + B) = \frac{1/3 + 1/2}{1 - (1/3)(1/2)} = \frac{5/6}{1 - 1/6} = \frac{5/6}{5/6} = 1 \]
Assuming positive acute angles:
\[ A + B = 45^\circ \]

**Answer: (b)**
</details>

15. 🟡 cos(α + β) cos(α − β) equals:
    (a) cos²α − sin²β   (b) cos²α + sin²β   (c) sin²α − cos²β   (d) cos²α − cos²β
<details>
<summary>Solution</summary>

Expanding:
\[ \cos(\alpha + \beta) \cos(\alpha - \beta) = (\cos \alpha \cos \beta - \sin \alpha \sin \beta)(\cos \alpha \cos \beta + \sin \alpha \sin \beta) \]
\[ = \cos^2 \alpha \cos^2 \beta - \sin^2 \alpha \sin^2 \beta \]
Substitute \( \cos^2 \beta = 1 - \sin^2 \beta \) and \( \sin^2 \alpha = 1 - \cos^2 \alpha \):
\[ = \cos^2 \alpha(1 - \sin^2 \beta) - (1 - \cos^2 \alpha)\sin^2 \beta \]
\[ = \cos^2 \alpha - \cos^2 \alpha \sin^2 \beta - \sin^2 \beta + \cos^2 \alpha \sin^2 \beta \]
\[ = \cos^2 \alpha - \sin^2 \beta \]

**Answer: (a)**
</details>

16. 🟡 tan 75° equals:
    (a) 2 + √3   (b) 2 − √3   (c) √3 + 1   (d) √3 − 1
<details>
<summary>Solution</summary>

Using \( 75^\circ = 45^\circ + 30^\circ \):
\[ \tan 75^\circ = \frac{\tan 45^\circ + \tan 30^\circ}{1 - \tan 45^\circ \tan 30^\circ} = \frac{1 + 1/\sqrt{3}}{1 - 1/\sqrt{3}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1} \]
Rationalizing:
\[ \frac{(\sqrt{3} + 1)^2}{3 - 1} = \frac{3 + 1 + 2\sqrt{3}}{2} = 2 + \sqrt{3} \]

**Answer: (a)**
</details>

17. 🟡 sin 75° − sin 15° equals:
    (a) 1/√2   (b) √3/2   (c) 1/2   (d) √2
<details>
<summary>Solution</summary>

Using the values of \( \sin 75^\circ \) and \( \sin 15^\circ \):
\[ \sin 75^\circ = \frac{\sqrt{3} + 1}{2\sqrt{2}} \]
\[ \sin 15^\circ = \frac{\sqrt{3} - 1}{2\sqrt{2}} \]
Subtracting them:
\[ \sin 75^\circ - \sin 15^\circ = \frac{(\sqrt{3} + 1) - (\sqrt{3} - 1)}{2\sqrt{2}} = \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}} \]

**Answer: (a)**
</details>

18. 🟡 cos 15° − sin 15° equals:
    (a) 1/√2   (b) √2   (c) 0   (d) −1/√2
<details>
<summary>Solution</summary>

Using the values of \( \cos 15^\circ = \frac{\sqrt{3}+1}{2\sqrt{2}} \) and \( \sin 15^\circ = \frac{\sqrt{3}-1}{2\sqrt{2}} \):
\[ \cos 15^\circ - \sin 15^\circ = \frac{(\sqrt{3} + 1) - (\sqrt{3} - 1)}{2\sqrt{2}} = \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}} \]

**Answer: (a)**
</details>

19. 🟡 If sin(A + B) = sin A cos B + cos A sin B, then sin 2A = ?<br>
    (a) sin²A   (b) 2 sin A cos A   (c) cos²A   (d) 1
<details>
<summary>Solution</summary>

Setting \( B = A \) in the compound angle formula:
\[ \sin(A + A) = \sin A \cos A + \cos A \sin A \implies \sin 2A = 2 \sin A \cos A \]

**Answer: (b)**
</details>

20. 🟡 The expression (tan 3x − tan x)/(1 + tan 3x tan x) equals:
    (a) tan 2x   (b) tan 4x   (c) tan x   (d) tan 3x
<details>
<summary>Solution</summary>

Using the tangent compound angle formula:
\[ \tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B} \]
Setting \( A = 3x \) and \( B = x \):
\[ \tan(3x - x) = \tan 2x \]

**Answer: (a)**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | a | 11 | a | 16 | a |
| 2 | a | 7 | b | 12 | b | 17 | a |
| 3 | b | 8 | a | 13 | a | 18 | a |
| 4 | a | 9 | b | 14 | b | 15 | a |
| 5 | b | 10 | a | 15 | a | 20 | a |

</details>
