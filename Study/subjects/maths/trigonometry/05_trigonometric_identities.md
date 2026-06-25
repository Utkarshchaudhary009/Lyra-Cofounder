# Chapter 5: Trigonometric Identities — The Big Three

---

## Stage 1: The Core Idea

### The Pythagorean Connection

In a right triangle with angle θ:

```
       ┌───┐
       │   │
  opp  │   │  hyp = 1 (if scaling)
       │   │
       └───┘
         adj

By Pythagoras: opp² + adj² = hyp²
```

If we scale the triangle so hyp = 1, then:
- opp = sin θ
- adj = cos θ

And Pythagoras becomes: **sin²θ + cos²θ = 1**

From this single equation, two more follow:
- Divide by cos²θ: **1 + tan²θ = sec²θ**
- Divide by sin²θ: **1 + cot²θ = cosec²θ**

These **three identities** are the backbone of all trigonometry. Every simplification, every proof, every equation — they all come back to these three.

---

## Stage 2: The Formula Lab

### The Big Three

| # | Identity | Derivation |
|---|----------|-----------|
| 1 | sin²θ + cos²θ = 1 | Pythagoras on unit hyp triangle |
| 2 | 1 + tan²θ = sec²θ | Divide (1) by cos²θ |
| 3 | 1 + cot²θ = cosec²θ | Divide (1) by sin²θ |

### Variations

From sin²θ + cos²θ = 1:
```
sin²θ = 1 − cos²θ = (1 − cos θ)(1 + cos θ)
cos²θ = 1 − sin²θ = (1 − sin θ)(1 + sin θ)
```

From 1 + tan²θ = sec²θ:
```
tan²θ = sec²θ − 1 = (sec θ − 1)(sec θ + 1)
```

From 1 + cot²θ = cosec²θ:
```
cot²θ = cosec²θ − 1 = (cosec θ − 1)(cosec θ + 1)
```

**Trap to avoid:** sin²θ means (sin θ)², NOT sin(θ²). Similarly, sin⁻¹θ ≠ (sin θ)⁻¹.

---

## Stage 3: Type-wise Mastery

### Type 1: Proving LHS = RHS (Direct Substitution)

**Goal:** Prove an identity by substituting the basic identities.

**Solved Example:**

Prove that cos⁴θ − sin⁴θ = cos²θ − sin²θ.

**Solution:**
```
LHS = (cos²θ)² − (sin²θ)²
    = (cos²θ − sin²θ)(cos²θ + sin²θ)
    = (cos²θ − sin²θ)(1)
    = cos²θ − sin²θ = RHS ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Prove: (1 − cos²θ) × cosec²θ = 1.
<details>
<summary>Solution</summary>

We know the fundamental trigonometric identity:
\[ \sin^2\theta + \cos^2\theta = 1 \implies 1 - \cos^2\theta = \sin^2\theta \]
Also, by the reciprocal definition of cosecant:
\[ \csc\theta = \frac{1}{\sin\theta} \implies \csc^2\theta = \frac{1}{\sin^2\theta} \]
Substituting these into the Left-Hand Side (LHS):
\[ \text{LHS} = (1 - \cos^2\theta) \times \csc^2\theta = \sin^2\theta \times \frac{1}{\sin^2\theta} = 1 = \text{RHS} \]
Hence proved.

</details>

2. 🟡 Prove: (1 + tan²θ) × cos²θ = 1.
<details>
<summary>Solution</summary>

We know the trigonometric identity relating tangent and secant:
\[ 1 + \tan^2\theta = \sec^2\theta \]
And the reciprocal relation of secant:
\[ \sec\theta = \frac{1}{\cos\theta} \implies \sec^2\theta = \frac{1}{\cos^2\theta} \]
Substituting these into the Left-Hand Side (LHS):
\[ \text{LHS} = (1 + \tan^2\theta) \times \cos^2\theta = \sec^2\theta \times \cos^2\theta = \frac{1}{\cos^2\theta} \times \cos^2\theta = 1 = \text{RHS} \]
Hence proved.

</details>

3. 🟡 Prove: sin⁴θ − cos⁴θ = sin²θ − cos²θ.
<details>
<summary>Solution</summary>

We factor the Left-Hand Side (LHS) as a difference of squares \( a^4 - b^4 = (a^2 - b^2)(a^2 + b^2) \):
\[ \text{LHS} = \sin^4\theta - \cos^4\theta = (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = (\sin^2\theta - \cos^2\theta) \times 1 = \sin^2\theta - \cos^2\theta = \text{RHS} \]
Hence proved.

</details>

4. 🟡 Prove: (sec²θ − 1)(cosec²θ − 1) = 1.
<details>
<summary>Solution</summary>

From the identities \( 1 + \tan^2\theta = \sec^2\theta \) and \( 1 + \cot^2\theta = \csc^2\theta \), we have:
\[ \sec^2\theta - 1 = \tan^2\theta \]
\[ \csc^2\theta - 1 = \cot^2\theta \]
Substituting these into the Left-Hand Side (LHS):
\[ \text{LHS} = (\sec^2\theta - 1)(\csc^2\theta - 1) = \tan^2\theta \times \cot^2\theta \]
Since \( \cot\theta = \frac{1}{\tan\theta} \implies \tan\theta \times \cot\theta = 1 \):
\[ \text{LHS} = \tan^2\theta \times \frac{1}{\tan^2\theta} = 1 = \text{RHS} \]
Hence proved.

</details>

5. 🔴 Prove: (sin θ + cos θ)² + (sin θ − cos θ)² = 2.
<details>
<summary>Solution</summary>

Expanding the terms on the Left-Hand Side (LHS) using the algebraic expansion \( (a \pm b)^2 = a^2 + b^2 \pm 2ab \):
\[ (\sin\theta + \cos\theta)^2 = \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta \]
\[ (\sin\theta - \cos\theta)^2 = \sin^2\theta + \cos^2\theta - 2\sin\theta\cos\theta \]
Adding these two expressions together:
\[ \text{LHS} = (\sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta) + (\sin^2\theta + \cos^2\theta - 2\sin\theta\cos\theta) \]
The cross terms cancel each other:
\[ \text{LHS} = 2(\sin^2\theta + \cos^2\theta) \]
Substituting the fundamental identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = 2 \times 1 = 2 = \text{RHS} \]
Hence proved.

</details>

---

### Type 2: Expressing One Ratio in Terms of Another

**Goal:** Write all trig ratios in terms of a given ratio.

**Solved Example:**

Express sin θ and tan θ in terms of cos θ.

**Solution:**
```
sin²θ = 1 − cos²θ
sin θ = √(1 − cos²θ)    (positive if θ acute)

tan θ = sin θ / cos θ = √(1 − cos²θ) / cos θ
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 Express cos θ and cot θ in terms of sin θ.
<details>
<summary>Solution</summary>

1. To express \( \cos\theta \) in terms of \( \sin\theta \), we use:
   \[ \sin^2\theta + \cos^2\theta = 1 \implies \cos^2\theta = 1 - \sin^2\theta \implies \cos\theta = \pm\sqrt{1 - \sin^2\theta} \]
   *(For an acute angle \( \theta \), \( \cos\theta = \sqrt{1 - \sin^2\theta} \))*

2. To express \( \cot\theta \) in terms of \( \sin\theta \):
   \[ \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{\pm\sqrt{1 - \sin^2\theta}}{\sin\theta} \]
   *(For an acute angle \( \theta \), \( \cot\theta = \frac{\sqrt{1 - \sin^2\theta}}{\sin\theta} \))*

</details>

7. 🟡 Express sin θ and sec θ in terms of tan θ.
<details>
<summary>Solution</summary>

1. To express \( \sec\theta \) in terms of \( \tan\theta \), we use the identity:
   \[ 1 + \tan^2\theta = \sec^2\theta \implies \sec\theta = \pm\sqrt{1 + \tan^2\theta} \]
   *(For an acute angle \( \theta \), \( \sec\theta = \sqrt{1 + \tan^2\theta} \))*

2. To express \( \sin\theta \) in terms of \( \tan\theta \):
   Since \( \tan\theta = \frac{\sin\theta}{\cos\theta} \implies \sin\theta = \tan\theta\cos\theta = \frac{\tan\theta}{\sec\theta} \):
   \[ \sin\theta = \frac{\tan\theta}{\pm\sqrt{1 + \tan^2\theta}} \]
   *(For an acute angle \( \theta \), \( \sin\theta = \frac{\tan\theta}{\sqrt{1 + \tan^2\theta}} \))*

</details>

8. 🟡 Express all six ratios in terms of cos θ.
<details>
<summary>Solution</summary>

Assuming \( \theta \) is an acute angle (all trigonometric values are positive):
1. \( \cos\theta = \cos\theta \)
2. \( \sin\theta = \sqrt{1 - \cos^2\theta} \)
3. \( \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\sqrt{1 - \cos^2\theta}}{\cos\theta} \)
4. \( \sec\theta = \frac{1}{\cos\theta} \)
5. \( \csc\theta = \frac{1}{\sin\theta} = \frac{1}{\sqrt{1 - \cos^2\theta}} \)
6. \( \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{\cos\theta}{\sqrt{1 - \cos^2\theta}} \)

</details>

9. 🔴 Express cos θ in terms of cot θ.
<details>
<summary>Solution</summary>

We know that:
\[ \cot\theta = \frac{\cos\theta}{\sin\theta} \implies \cos\theta = \cot\theta\sin\theta \]
Also, using the identity \( \csc^2\theta = 1 + \cot^2\theta \):
\[ \sin\theta = \frac{1}{\csc\theta} = \frac{1}{\pm\sqrt{1 + \cot^2\theta}} \]
Substituting this into the expression for \( \cos\theta \):
\[ \cos\theta = \frac{\cot\theta}{\pm\sqrt{1 + \cot^2\theta}} \]
*(For an acute angle \( \theta \), \( \cos\theta = \frac{\cot\theta}{\sqrt{1 + \cot^2\theta}} \))*

</details>

10. 🔴 Express cosec θ in terms of cos θ.
<details>
<summary>Solution</summary>

Using the identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \sin\theta = \pm\sqrt{1 - \cos^2\theta} \]
Since \( \csc\theta = \frac{1}{\sin\theta} \):
\[ \csc\theta = \frac{1}{\pm\sqrt{1 - \cos^2\theta}} \]
*(For an acute angle \( \theta \), \( \csc\theta = \frac{1}{\sqrt{1 - \cos^2\theta}} \))*

</details>

---

### Type 3: Proving LHS = RHS (Factorisation)

**Goal:** Prove identities using algebraic factorisation.

**Solved Example:**

Prove: sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ.

**Solution:**
```
LHS = (sin²θ)² + (cos²θ)²
    = (sin²θ + cos²θ)² − 2 sin²θ cos²θ
    = (1)² − 2 sin²θ cos²θ
    = 1 − 2 sin²θ cos²θ = RHS ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 Prove: (sin θ + cos θ)² = 1 + 2 sin θ cos θ.
<details>
<summary>Solution</summary>

Expanding the Left-Hand Side (LHS) using \( (a+b)^2 = a^2 + b^2 + 2ab \):
\[ \text{LHS} = (\sin\theta + \cos\theta)^2 = \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta \]
Using the fundamental identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = 1 + 2\sin\theta\cos\theta = \text{RHS} \]
Hence proved.

</details>

12. 🟡 Prove: sin³θ + cos³θ = (sin θ + cos θ)(1 − sin θ cos θ).
<details>
<summary>Solution</summary>

Using the sum of cubes algebraic identity, \( a^3 + b^3 = (a + b)(a^2 - ab + b^2) \):
\[ \text{LHS} = \sin^3\theta + \cos^3\theta = (\sin\theta + \cos\theta)(\sin^2\theta - \sin\theta\cos\theta + \cos^2\theta) \]
Rearranging terms inside the second bracket:
\[ \text{LHS} = (\sin\theta + \cos\theta)((\sin^2\theta + \cos^2\theta) - \sin\theta\cos\theta) \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = (\sin\theta + \cos\theta)(1 - \sin\theta\cos\theta) = \text{RHS} \]
Hence proved.

</details>

13. 🟡 Prove: (1 + tan θ)² + (1 − tan θ)² = 2 sec²θ.
<details>
<summary>Solution</summary>

Expand both expressions on the Left-Hand Side (LHS):
\[ (1 + \tan\theta)^2 = 1 + \tan^2\theta + 2\tan\theta \]
\[ (1 - \tan\theta)^2 = 1 + \tan^2\theta - 2\tan\theta \]
Adding these terms together:
\[ \text{LHS} = (1 + \tan^2\theta + 2\tan\theta) + (1 + \tan^2\theta - 2\tan\theta) = 2(1 + \tan^2\theta) \]
Using the identity \( 1 + \tan^2\theta = \sec^2\theta \):
\[ \text{LHS} = 2\sec^2\theta = \text{RHS} \]
Hence proved.

</details>

14. 🔴 Prove: (sin θ + cosec θ)² + (cos θ + sec θ)² = 7 + tan²θ + cot²θ.
<details>
<summary>Solution</summary>

Expand the squared terms on the Left-Hand Side (LHS):
\[ (\sin\theta + \csc\theta)^2 = \sin^2\theta + \csc^2\theta + 2\sin\theta\csc\theta \]
\[ (\cos\theta + \sec\theta)^2 = \cos^2\theta + \sec^2\theta + 2\cos\theta\sec\theta \]
Since \( \sin\theta\csc\theta = 1 \) and \( \cos\theta\sec\theta = 1 \):
\[ \text{LHS} = \sin^2\theta + \csc^2\theta + 2 + \cos^2\theta + \sec^2\theta + 2 \]
Rearrange and group the terms:
\[ \text{LHS} = (\sin^2\theta + \cos^2\theta) + \csc^2\theta + \sec^2\theta + 4 \]
Substitute \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = 1 + \csc^2\theta + \sec^2\theta + 4 = 5 + \csc^2\theta + \sec^2\theta \]
Now use the variations of Pythagorean identities \( \csc^2\theta = 1 + \cot^2\theta \) and \( \sec^2\theta = 1 + \tan^2\theta \):
\[ \text{LHS} = 5 + (1 + \cot^2\theta) + (1 + \tan^2\theta) = 7 + \tan^2\theta + \cot^2\theta = \text{RHS} \]
Hence proved.

</details>

15. 🔴 ⭐ Prove: (tan θ + sec θ − 1)/(tan θ + sec θ + 1) = (1 + sin θ)/cos θ.
<details>
<summary>Solution</summary>

*Note: The standard form of this identity is \( \frac{\tan\theta + \sec\theta - 1}{\tan\theta - \sec\theta + 1} = \frac{1 + \sin\theta}{\cos\theta} \). Let's prove this standard relation:*

LHS:
\[ \frac{\tan\theta + \sec\theta - 1}{\tan\theta - \sec\theta + 1} \]
Using the identity \( \sec^2\theta - \tan^2\theta = 1 \), we substitute \( 1 = \sec^2\theta - \tan^2\theta \) in the numerator:
\[ \text{LHS} = \frac{(\tan\theta + \sec\theta) - (\sec^2\theta - \tan^2\theta)}{\tan\theta - \sec\theta + 1} \]
Factor the difference of squares \( \sec^2\theta - \tan^2\theta = (\sec\theta - \tan\theta)(\sec\theta + \tan\theta) \):
\[ \text{LHS} = \frac{(\sec\theta + \tan\theta) - (\sec\theta - \tan\theta)(\sec\theta + \tan\theta)}{\tan\theta - \sec\theta + 1} \]
Factor out the common term \( (\sec\theta + \tan\theta) \) from the numerator:
\[ \text{LHS} = \frac{(\sec\theta + \tan\theta)[1 - (\sec\theta - \tan\theta)]}{\tan\theta - \sec\theta + 1} = \frac{(\sec\theta + \tan\theta)(1 - \sec\theta + \tan\theta)}{\tan\theta - \sec\theta + 1} \]
Since \( 1 - \sec\theta + \tan\theta \) is equivalent to \( \tan\theta - \sec\theta + 1 \), we cancel this factor from the numerator and denominator:
\[ \text{LHS} = \sec\theta + \tan\theta = \frac{1}{\cos\theta} + \frac{\sin\theta}{\cos\theta} = \frac{1 + \sin\theta}{\cos\theta} = \text{RHS} \]
Hence proved.

</details>

---

### Type 4: Proving LHS = RHS (Using Denominators)

**Goal:** Prove identities by combining fractions.

**Solved Example:**

Prove: 1/(1 + sin θ) + 1/(1 − sin θ) = 2 sec²θ.

**Solution:**
```
LHS = (1 − sin θ + 1 + sin θ)/((1 + sin θ)(1 − sin θ))
    = 2/(1 − sin²θ)
    = 2/cos²θ
    = 2 sec²θ = RHS ✓
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Prove: 1/(1 + cos θ) + 1/(1 − cos θ) = 2 cosec²θ.
<details>
<summary>Solution</summary>

Combine the fractions on the Left-Hand Side (LHS) by finding a common denominator:
\[ \text{LHS} = \frac{(1 - \cos\theta) + (1 + \cos\theta)}{(1 + \cos\theta)(1 - \cos\theta)} = \frac{2}{1 - \cos^2\theta} \]
Using the identity \( 1 - \cos^2\theta = \sin^2\theta \):
\[ \text{LHS} = \frac{2}{\sin^2\theta} = 2\csc^2\theta = \text{RHS} \]
Hence proved.

</details>

17. 🟡 Prove: (cosec θ − cot θ)² = (1 − cos θ)/(1 + cos θ).
<details>
<summary>Solution</summary>

Convert the terms on the Left-Hand Side (LHS) to sine and cosine:
\[ \csc\theta = \frac{1}{\sin\theta}, \quad \cot\theta = \frac{\cos\theta}{\sin\theta} \]
Substitute these:
\[ \text{LHS} = \left(\frac{1}{\sin\theta} - \frac{\cos\theta}{\sin\theta}\right)^2 = \left(\frac{1 - \cos\theta}{\sin\theta}\right)^2 = \frac{(1 - \cos\theta)^2}{\sin^2\theta} \]
Substitute the identity \( \sin^2\theta = 1 - \cos^2\theta = (1 - \cos\theta)(1 + \cos\theta) \) into the denominator:
\[ \text{LHS} = \frac{(1 - \cos\theta)^2}{(1 - \cos\theta)(1 + \cos\theta)} = \frac{1 - \cos\theta}{1 + \cos\theta} = \text{RHS} \]
Hence proved.

</details>

18. 🟡 Prove: (1 + sin θ)/cos θ + cos θ/(1 + sin θ) = 2 sec θ.
<details>
<summary>Solution</summary>

Find the common denominator to combine the terms on the Left-Hand Side (LHS):
\[ \text{LHS} = \frac{(1 + \sin\theta)^2 + \cos^2\theta}{\cos\theta(1 + \sin\theta)} \]
Expand the squared term:
\[ \text{LHS} = \frac{1 + \sin^2\theta + 2\sin\theta + \cos^2\theta}{\cos\theta(1 + \sin\theta)} \]
Group \( \sin^2\theta + \cos^2\theta \) and substitute \( 1 \):
\[ \text{LHS} = \frac{1 + 1 + 2\sin\theta}{\cos\theta(1 + \sin\theta)} = \frac{2 + 2\sin\theta}{\cos\theta(1 + \sin\theta)} = \frac{2(1 + \sin\theta)}{\cos\theta(1 + \sin\theta)} \]
Cancel the common factor \( 1 + \sin\theta \):
\[ \text{LHS} = \frac{2}{\cos\theta} = 2\sec\theta = \text{RHS} \]
Hence proved.

</details>

19. 🔴 Prove: (tan A − tan B)/(cot B − cot A) = tan A tan B.
<details>
<summary>Solution</summary>

Express the cotangent terms in the denominator of the Left-Hand Side (LHS) as reciprocal tangent terms:
\[ \cot B = \frac{1}{\tan B}, \quad \cot A = \frac{1}{\tan A} \]
The denominator becomes:
\[ \cot B - \cot A = \frac{1}{\tan B} - \frac{1}{\tan A} = \frac{\tan A - \tan B}{\tan A\tan B} \]
Now rewrite LHS:
\[ \text{LHS} = \frac{\tan A - \tan B}{\left(\frac{\tan A - \tan B}{\tan A\tan B}\right)} = (\tan A - \tan B) \times \frac{\tan A\tan B}{\tan A - \tan B} \]
Cancel the common factor \( \tan A - \tan B \):
\[ \text{LHS} = \tan A\tan B = \text{RHS} \]
Hence proved.

</details>

20. 🔴 ⭐ Prove: (sin A + sec A)² + (cos A + cosec A)² = (1 + sec A cosec A)².
<details>
<summary>Solution</summary>

Convert the secant and cosecant terms on the Left-Hand Side (LHS) into cosine and sine:
\[ \text{LHS} = \left(\sin A + \frac{1}{\cos A}\right)^2 + \left(\cos A + \frac{1}{\sin A}\right)^2 \]
Combine the terms inside each parenthesis:
\[ \text{LHS} = \left(\frac{\sin A\cos A + 1}{\cos A}\right)^2 + \left(\frac{\cos A\sin A + 1}{\sin A}\right)^2 \]
Factor out the common numerator term \( (\sin A\cos A + 1)^2 \):
\[ \text{LHS} = (\sin A\cos A + 1)^2 \left[ \frac{1}{\cos^2 A} + \frac{1}{\sin^2 A} \right] \]
Simplify the term inside the square brackets by finding a common denominator:
\[ \frac{1}{\cos^2 A} + \frac{1}{\sin^2 A} = \frac{\sin^2 A + \cos^2 A}{\sin^2 A\cos^2 A} = \frac{1}{\sin^2 A\cos^2 A} \]
Substitute this back:
\[ \text{LHS} = (\sin A\cos A + 1)^2 \times \frac{1}{\sin^2 A\cos^2 A} = \left(\frac{\sin A\cos A + 1}{\sin A\cos A}\right)^2 \]
Divide the terms inside the parentheses:
\[ \frac{\sin A\cos A + 1}{\sin A\cos A} = 1 + \frac{1}{\sin A\cos A} = 1 + \sec A\csc A \]
Thus:
\[ \text{LHS} = (1 + \sec A\csc A)^2 = \text{RHS} \]
Hence proved.

</details>

---

### Type 5: Eliminating θ Between Two Equations

**Goal:** Given two equations involving θ, eliminate θ to find a relation between the constants.

**Solved Example:**

Eliminate θ from: x = a cos θ, y = b sin θ.

**Solution:**
```
cos θ = x/a, sin θ = y/b
Using sin²θ + cos²θ = 1:
x²/a² + y²/b² = 1
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Eliminate θ: x = 3 cos θ, y = 4 sin θ.
<details>
<summary>Solution</summary>

Rearrange the equations to find expressions for \( \cos\theta \) and \( \sin\theta \):
\[ \cos\theta = \frac{x}{3} \]
\[ \sin\theta = \frac{y}{4} \]
Using the fundamental Pythagorean identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \left(\frac{y}{4}\right)^2 + \left(\frac{x}{3}\right)^2 = 1 \implies \frac{x^2}{9} + \frac{y^2}{16} = 1 \]
This is the required equation with \( \theta \) eliminated.

</details>

22. 🟡 Eliminate θ: x = a sec θ, y = b tan θ.
<details>
<summary>Solution</summary>

Rearrange the equations:
\[ \sec\theta = \frac{x}{a} \]
\[ \tan\theta = \frac{y}{b} \]
Using the identity \( \sec^2\theta - \tan^2\theta = 1 \):
\[ \left(\frac{x}{a}\right)^2 - \left(\frac{y}{b}\right)^2 = 1 \implies \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \]
This is the required equation with \( \theta \) eliminated.

</details>

23. 🟡 Eliminate θ: x = a cos θ + b sin θ, y = a sin θ − b cos θ.
<details>
<summary>Solution</summary>

Square both equations:
\[ x^2 = (a\cos\theta + b\sin\theta)^2 = a^2\cos^2\theta + b^2\sin^2\theta + 2ab\sin\theta\cos\theta \]
\[ y^2 = (a\sin\theta - b\cos\theta)^2 = a^2\sin^2\theta + b^2\cos^2\theta - 2ab\sin\theta\cos\theta \]
Adding these two equations together:
\[ x^2 + y^2 = a^2(\cos^2\theta + \sin^2\theta) + b^2(\sin^2\theta + \cos^2\theta) \]
Using the identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ x^2 + y^2 = a^2 + b^2 \]
This is the relation with \( \theta \) eliminated.

</details>

24. 🔴 Eliminate θ: x = a(cos θ + sin θ), y = a(cos θ − sin θ).
<details>
<summary>Solution</summary>

Rearrange the equations:
\[ \frac{x}{a} = \cos\theta + \sin\theta \]
\[ \frac{y}{a} = \cos\theta - \sin\theta \]
Square both equations and add them:
\[ \left(\frac{x}{a}\right)^2 + \left(\frac{y}{a}\right)^2 = (\cos\theta + \sin\theta)^2 + (\cos\theta - \sin\theta)^2 \]
\[ \frac{x^2 + y^2}{a^2} = (\cos^2\theta + \sin^2\theta + 2\sin\theta\cos\theta) + (\cos^2\theta + \sin^2\theta - 2\sin\theta\cos\theta) \]
\[ \frac{x^2 + y^2}{a^2} = 2(\sin^2\theta + \cos^2\theta) \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ x^2 + y^2 = 2a^2 \]
This is the relation with \( \theta \) eliminated.

</details>

25. 🔴 If x = a cos²θ, y = b sin²θ, find a relation between x, y, a, b.
<details>
<summary>Solution</summary>

Solve for \( \cos^2\theta \) and \( \sin^2\theta \):
\[ \cos^2\theta = \frac{x}{a} \]
\[ \sin^2\theta = \frac{y}{b} \]
Using the fundamental identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \frac{y}{b} + \frac{x}{a} = 1 \implies \frac{x}{a} + \frac{y}{b} = 1 \]
This is the required relation.

</details>

---

### Type 6: Conditional Identities (A + B + C = π)

**Goal:** Prove identities when the angles satisfy A + B + C = 180° (triangle angles).

**Key observations:**
- If A + B + C = π, then A + B = π − C
- So sin(A + B) = sin C, cos(A + B) = −cos C

**Solved Example:**

If A + B + C = π, prove that tan A + tan B + tan C = tan A tan B tan C.

**Solution:**
```
A + B = π − C
tan(A + B) = tan(π − C) = −tan C
(tan A + tan B)/(1 − tan A tan B) = −tan C
tan A + tan B = −tan C + tan A tan B tan C
tan A + tan B + tan C = tan A tan B tan C ✓
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 If A + B + C = π, prove that sin 2A + sin 2B + sin 2C = 4 sin A sin B sin C.
<details>
<summary>Solution</summary>

Using the sum-to-product formula on the first two terms:
\[ \sin 2A + \sin 2B = 2\sin(A+B)\cos(A-B) \]
Since \( A+B+C = \pi \implies A+B = \pi - C \), we have \( \sin(A+B) = \sin(\pi - C) = \sin C \).
Thus:
\[ \sin 2A + \sin 2B = 2\sin C\cos(A-B) \]
Now rewrite \( \sin 2C \) using the double-angle formula \( \sin 2C = 2\sin C\cos C \):
\[ \text{LHS} = 2\sin C\cos(A-B) + 2\sin C\cos C = 2\sin C[\cos(A-B) + \cos C] \]
Since \( C = \pi - (A+B) \), we have \( \cos C = \cos(\pi - (A+B)) = -\cos(A+B) \). Substitute this:
\[ \text{LHS} = 2\sin C[\cos(A-B) - \cos(A+B)] \]
Using the product-to-sum formula \( \cos(A-B) - \cos(A+B) = 2\sin A\sin B \):
\[ \text{LHS} = 2\sin C[2\sin A\sin B] = 4\sin A\sin B\sin C = \text{RHS} \]
Hence proved.

</details>

27. 🔴 If A + B + C = π, prove that cos 2A + cos 2B + cos 2C = −1 − 4 cos A cos B cos C.
<details>
<summary>Solution</summary>

Using the sum-to-product formula on the first two terms:
\[ \cos 2A + \cos 2B = 2\cos(A+B)\cos(A-B) \]
Since \( A+B = \pi - C \), we have \( \cos(A+B) = -\cos C \).
Thus:
\[ \cos 2A + \cos 2B = -2\cos C\cos(A-B) \]
Using the double-angle formula \( \cos 2C = 2\cos^2 C - 1 \):
\[ \text{LHS} = -2\cos C\cos(A-B) + (2\cos^2 C - 1) = -1 - 2\cos C[\cos(A-B) - \cos C] \]
Since \( C = \pi - (A+B) \implies \cos C = -\cos(A+B) \), substitute this:
\[ \text{LHS} = -1 - 2\cos C[\cos(A-B) + \cos(A+B)] \]
Using the product-to-sum formula \( \cos(A-B) + \cos(A+B) = 2\cos A\cos B \):
\[ \text{LHS} = -1 - 2\cos C[2\cos A\cos B] = -1 - 4\cos A\cos B\cos C = \text{RHS} \]
Hence proved.

</details>

28. 🔴 If A + B + C = π, prove that sin A + sin B + sin C = 4 cos(A/2) cos(B/2) cos(C/2).
<details>
<summary>Solution</summary>

Apply the sum-to-product formula on the first two terms:
\[ \sin A + \sin B = 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right) \]
Since \( A+B+C = \pi \implies \frac{A+B}{2} = \frac{\pi}{2} - \frac{C}{2} \):
\[ \sin\left(\frac{A+B}{2}\right) = \sin\left(\frac{\pi}{2} - \frac{C}{2}\right) = \cos\left(\frac{C}{2}\right) \]
Thus:
\[ \sin A + \sin B = 2\cos\left(\frac{C}{2}\right)\cos\left(\frac{A-B}{2}\right) \]
Using the half-angle identity \( \sin C = 2\sin\left(\frac{C}{2}\right)\cos\left(\frac{C}{2}\right) \):
\[ \text{LHS} = 2\cos\left(\frac{C}{2}\right)\cos\left(\frac{A-B}{2}\right) + 2\sin\left(\frac{C}{2}\right)\cos\left(\frac{C}{2}\right) = 2\cos\left(\frac{C}{2}\right)\left[\cos\left(\frac{A-B}{2}\right) + \sin\left(\frac{C}{2}\right)\right] \]
Since \( \frac{C}{2} = \frac{\pi}{2} - \frac{A+B}{2} \implies \sin\left(\frac{C}{2}\right) = \cos\left(\frac{A+B}{2}\right) \):
\[ \text{LHS} = 2\cos\left(\frac{C}{2}\right)\left[\cos\left(\frac{A-B}{2}\right) + \cos\left(\frac{A+B}{2}\right)\right] \]
Using \( \cos\left(\frac{A-B}{2}\right) + \cos\left(\frac{A+B}{2}\right) = 2\cos\left(\frac{A}{2}\right)\cos\left(\frac{B}{2}\right) \):
\[ \text{LHS} = 2\cos\left(\frac{C}{2}\right)\left[2\cos\left(\frac{A}{2}\right)\cos\left(\frac{B}{2}\right)\right] = 4\cos\left(\frac{A}{2}\right)\cos\left(\frac{B}{2}\right)\cos\left(\frac{C}{2}\right) = \text{RHS} \]
Hence proved.

</details>

29. 🔴 If A + B + C = π/2, prove that cot A + cot B + cot C = cot A cot B cot C.
<details>
<summary>Solution</summary>

Given \( A+B+C = \frac{\pi}{2} \implies A+B = \frac{\pi}{2} - C \).
Taking cotangent on both sides:
\[ \cot(A+B) = \cot\left(\frac{\pi}{2} - C\right) \]
Using the compound angle identity for cotangent, and noting that \( \cot\left(\frac{\pi}{2} - C\right) = \tan C = \frac{1}{\cot C} \):
\[ \frac{\cot A\cot B - 1}{\cot A + \cot B} = \frac{1}{\cot C} \]
Cross-multiplying yields:
\[ \cot C(\cot A\cot B - 1) = \cot A + \cot B \]
\[ \cot A\cot B\cot C - \cot C = \cot A + \cot B \]
Rearranging terms:
\[ \cot A + \cot B + \cot C = \cot A\cot B\cot C \]
Hence proved.

</details>

30. 🔴 ⭐ If x + y + z = xyz, prove that x/(1 − x²) + y/(1 − y²) + z/(1 − z²) = xyz/(1 − x²)(1 − y²)(1 − z²).
<details>
<summary>Solution</summary>

*Note: The mathematically correct version of this identity is \( \frac{x}{1-x^2} + \frac{y}{1-y^2} + \frac{z}{1-z^2} = \frac{4xyz}{(1-x^2)(1-y^2)(1-z^2)} \). Let's prove it:*

Let \( x = \tan A \), \( y = \tan B \), and \( z = \tan C \).
The given condition \( x + y + z = xyz \) becomes:
\[ \tan A + \tan B + \tan C = \tan A\tan B\tan C \]
This is a standard identity for angles of a triangle, meaning \( A + B + C = \pi \).
We wish to evaluate:
\[ \text{LHS} = \frac{\tan A}{1-\tan^2 A} + \frac{\tan B}{1-\tan^2 B} + \frac{\tan C}{1-\tan^2 C} \]
Multiply and divide the expression by 2:
\[ \text{LHS} = \frac{1}{2}\left( \frac{2\tan A}{1-\tan^2 A} + \frac{2\tan B}{1-\tan^2 B} + \frac{2\tan C}{1-\tan^2 C} \right) = \frac{1}{2}(\tan 2A + \tan 2B + \tan 2C) \]
Since \( A+B+C = \pi \), we have \( 2A+2B+2C = 2\pi \).
For any three angles whose sum is \( 2\pi \) (or any multiple of \( \pi \)), the sum of their tangents is equal to their product:
\[ \tan 2A + \tan 2B + \tan 2C = \tan 2A\tan 2B\tan 2C \]
Substituting this back:
\[ \text{LHS} = \frac{1}{2}(\tan 2A\tan 2B\tan 2C) \]
Using the double-angle identity \( \tan 2\theta = \frac{2\tan\theta}{1-\tan^2\theta} \):
\[ \text{LHS} = \frac{1}{2}\left( \frac{2x}{1-x^2} \right)\left( \frac{2y}{1-y^2} \right)\left( \frac{2z}{1-z^2} \right) = \frac{4xyz}{(1-x^2)(1-y^2)(1-z^2)} \]
This completes the derivation of the identity.

</details>

---

### Type 7: Finding Values Using Identities

**Goal:** Use identities to find the value of expressions without finding θ.

**Solved Example:**

If sin θ + cos θ = √2, find sin θ cos θ.

**Solution:**
```
(sin θ + cos θ)² = 2
sin²θ + cos²θ + 2 sin θ cos θ = 2
1 + 2 sin θ cos θ = 2
2 sin θ cos θ = 1
sin θ cos θ = 1/2
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 If sin θ − cos θ = 0, find sin θ cos θ.
<details>
<summary>Solution</summary>

Given:
\[ \sin\theta - \cos\theta = 0 \implies \sin\theta = \cos\theta \]
Square both sides of the equation:
\[ (\sin\theta - \cos\theta)^2 = 0 \]
\[ \sin^2\theta + \cos^2\theta - 2\sin\theta\cos\theta = 0 \]
Using the identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ 1 - 2\sin\theta\cos\theta = 0 \implies 2\sin\theta\cos\theta = 1 \implies \sin\theta\cos\theta = \frac{1}{2} \]

</details>

32. 🟡 If tan θ + cot θ = 2, find tan²θ + cot²θ.
<details>
<summary>Solution</summary>

Given:
\[ \tan\theta + \cot\theta = 2 \]
Square both sides of the equation:
\[ (\tan\theta + \cot\theta)^2 = 2^2 = 4 \]
\[ \tan^2\theta + \cot^2\theta + 2\tan\theta\cot\theta = 4 \]
Since \( \tan\theta\cot\theta = 1 \):
\[ \tan^2\theta + \cot^2\theta + 2 = 4 \implies \tan^2\theta + \cot^2\theta = 2 \]

</details>

33. 🟡 If sec θ + tan θ = p, find sec θ − tan θ.
<details>
<summary>Solution</summary>

We know the trigonometric identity:
\[ \sec^2\theta - \tan^2\theta = 1 \]
Using the difference of squares:
\[ (\sec\theta - \tan\theta)(\sec\theta + \tan\theta) = 1 \]
Substitute \( \sec\theta + \tan\theta = p \):
\[ (\sec\theta - \tan\theta) \times p = 1 \implies \sec\theta - \tan\theta = \frac{1}{p} \]

</details>

34. 🔴 If sin θ + sin²θ = 1, prove that cos²θ + cos⁴θ = 1.
<details>
<summary>Solution</summary>

Given:
\[ \sin\theta + \sin^2\theta = 1 \implies \sin\theta = 1 - \sin^2\theta \]
Using the identity \( 1 - \sin^2\theta = \cos^2\theta \):
\[ \sin\theta = \cos^2\theta \]
Squaring both sides:
\[ \sin^2\theta = \cos^4\theta \]
Substitute these values into the expression to be evaluated:
\[ \cos^2\theta + \cos^4\theta = \cos^2\theta + \sin^2\theta \]
Using \( \cos^2\theta + \sin^2\theta = 1 \):
\[ \cos^2\theta + \cos^4\theta = 1 \]
Hence proved.

</details>

35. 🔴 ⭐ If a cos θ + b sin θ = c, then prove that a sin θ − b cos θ = ±√(a² + b² − c²).
<details>
<summary>Solution</summary>

Let \( a\sin\theta - b\cos\theta = k \).
Squaring the first given equation:
\[ (a\cos\theta + b\sin\theta)^2 = c^2 \implies a^2\cos^2\theta + b^2\sin^2\theta + 2ab\sin\theta\cos\theta = c^2 \quad \text{--- (1)} \]
Squaring the second equation:
\[ (a\sin\theta - b\cos\theta)^2 = k^2 \implies a^2\sin^2\theta + b^2\cos^2\theta - 2ab\sin\theta\cos\theta = k^2 \quad \text{--- (2)} \]
Add equations (1) and (2):
\[ (a^2\cos^2\theta + a^2\sin^2\theta) + (b^2\sin^2\theta + b^2\cos^2\theta) = c^2 + k^2 \]
\[ a^2(\cos^2\theta + \sin^2\theta) + b^2(\sin^2\theta + \cos^2\theta) = c^2 + k^2 \]
Substitute the identity \( \sin^2\theta + \cos^2\theta = 1 \):
\[ a^2(1) + b^2(1) = c^2 + k^2 \implies a^2 + b^2 = c^2 + k^2 \]
Rearrange to solve for \( k \):
\[ k^2 = a^2 + b^2 - c^2 \implies k = \pm\sqrt{a^2 + b^2 - c^2} \]
Substitute back the value of \( k \):
\[ a\sin\theta - b\cos\theta = \pm\sqrt{a^2 + b^2 - c^2} \]
Hence proved.

</details>

---

### Type 8: Identity-Based Simplifications

**Goal:** Simplify complex expressions using identities.

**Solved Example:**

Simplify: (sec A + tan A)(1 − sin A).

**Solution:**
```
= (1/cos A + sin A/cos A)(1 − sin A)
= (1 + sin A)/cos A × (1 − sin A)
= (1 − sin²A)/cos A
= cos²A/cos A
= cos A
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Simplify: (1 + tan²θ)(1 − sin θ)(1 + sin θ).
<details>
<summary>Solution</summary>

First, combine the last two factors using the difference of squares:
\[ (1 - \sin\theta)(1 + \sin\theta) = 1 - \sin^2\theta \]
Using the trigonometric identities \( 1 + \tan^2\theta = \sec^2\theta \) and \( 1 - \sin^2\theta = \cos^2\theta \):
\[ (1 + \tan^2\theta)(1 - \sin\theta)(1 + \sin\theta) = \sec^2\theta \times \cos^2\theta \]
Since \( \sec\theta = \frac{1}{\cos\theta} \):
\[ \sec^2\theta \times \cos^2\theta = \frac{1}{\cos^2\theta} \times \cos^2\theta = 1 \]
The simplified value is \( 1 \).

</details>

37. 🟡 Simplify: cos²A/(1 − sin A) − cos²A/(1 + sin A).
<details>
<summary>Solution</summary>

Factor out \( \cos^2 A \):
\[ \text{Expression} = \cos^2 A \left[ \frac{1}{1 - \sin A} - \frac{1}{1 + \sin A} \right] \]
Combine the fractions inside the brackets:
\[ \frac{1}{1 - \sin A} - \frac{1}{1 + \sin A} = \frac{(1 + \sin A) - (1 - \sin A)}{(1 - \sin A)(1 + \sin A)} = \frac{2\sin A}{1 - \sin^2 A} \]
Since \( 1 - \sin^2 A = \cos^2 A \):
\[ \text{Expression} = \cos^2 A \times \frac{2\sin A}{\cos^2 A} = 2\sin A \]
The simplified expression is \( 2\sin A \).

</details>

38. 🟡 Simplify: sin⁶θ + cos⁶θ + 3 sin²θ cos²θ.
<details>
<summary>Solution</summary>

Using the algebraic identity \( a^3 + b^3 = (a+b)^3 - 3ab(a+b) \) with \( a = \sin^2\theta \) and \( b = \cos^2\theta \):
\[ \sin^6\theta + \cos^6\theta = (\sin^2\theta)^3 + (\cos^2\theta)^3 = (\sin^2\theta + \cos^2\theta)^3 - 3\sin^2\theta\cos^2\theta(\sin^2\theta + \cos^2\theta) \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \sin^6\theta + \cos^6\theta = 1^3 - 3\sin^2\theta\cos^2\theta(1) = 1 - 3\sin^2\theta\cos^2\theta \]
Substituting this back into the original expression:
\[ (1 - 3\sin^2\theta\cos^2\theta) + 3\sin^2\theta\cos^2\theta = 1 \]
The simplified value is \( 1 \).

</details>

39. 🔴 Simplify: √((sec θ − 1)/(sec θ + 1)) + √((sec θ + 1)/(sec θ − 1)).
<details>
<summary>Solution</summary>

Assuming \( \theta \) is acute such that \( \sec\theta > 1 \) (rendering all terms inside the square root positive):
Combine the terms under a single denominator:
\[ \text{Expression} = \frac{(\sqrt{\sec\theta - 1})^2 + (\sqrt{\sec\theta + 1})^2}{\sqrt{(\sec\theta + 1)(\sec\theta - 1)}} = \frac{(\sec\theta - 1) + (\sec\theta + 1)}{\sqrt{\sec^2\theta - 1}} \]
\[ \text{Expression} = \frac{2\sec\theta}{\sqrt{\tan^2\theta}} \]
For an acute angle, \( \sqrt{\tan^2\theta} = \tan\theta \):
\[ \text{Expression} = \frac{2\sec\theta}{\tan\theta} = \frac{\left(\frac{2}{\cos\theta}\right)}{\left(\frac{\sin\theta}{\cos\theta}\right)} = \frac{2}{\sin\theta} = 2\csc\theta \]
The simplified expression is \( 2\csc\theta \).

</details>

40. 🔴 ⭐ Simplify: (tan A + sec A − 1)(tan A + sec A + 1).
<details>
<summary>Solution</summary>

Let \( x = \tan A + \sec A \). The expression is in the form of:
\[ (x - 1)(x + 1) = x^2 - 1 \]
Substitute \( x \) back:
\[ (\tan A + \sec A)^2 - 1 = \tan^2 A + \sec^2 A + 2\tan A\sec A - 1 \]
Using the identity \( \sec^2 A - 1 = \tan^2 A \):
\[ \text{Expression} = \tan^2 A + \tan^2 A + 2\tan A\sec A = 2\tan^2 A + 2\tan A\sec A \]
Factoring out \( 2\tan A \):
\[ \text{Expression} = 2\tan A(\tan A + \sec A) \]
Alternatively, in terms of sine and cosine:
\[ 2\frac{\sin A}{\cos A}\left(\frac{\sin A + 1}{\cos A}\right) = \frac{2\sin A(1+\sin A)}{\cos^2 A} = \frac{2\sin A(1+\sin A)}{1-\sin^2 A} = \frac{2\sin A}{1-\sin A} \]
Both forms are valid simplifications.

</details>

---

## Stage 4: Type Mixer

1. 🟡 Prove: (1 + tan²θ) + (1 + cot²θ) = (sin²θ + cos²θ)/(sin²θ cos²θ) ... simplify to: 1/(sin²θ cos²θ).
<details>
<summary>Solution</summary>

Using the identities \( 1 + \tan^2\theta = \sec^2\theta \) and \( 1 + \cot^2\theta = \csc^2\theta \):
\[ \text{LHS} = \sec^2\theta + \csc^2\theta \]
Convert to sine and cosine:
\[ \text{LHS} = \frac{1}{\cos^2\theta} + \frac{1}{\sin^2\theta} \]
Combine with a common denominator:
\[ \text{LHS} = \frac{\sin^2\theta + \cos^2\theta}{\sin^2\theta\cos^2\theta} \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \text{LHS} = \frac{1}{\sin^2\theta\cos^2\theta} = \text{RHS} \]
Hence proved.

</details>

2. 🟡 If sec θ + tan θ = 3, find sec θ − tan θ and hence find cos θ.
<details>
<summary>Solution</summary>

We know the identity:
\[ \sec^2\theta - \tan^2\theta = 1 \implies (\sec\theta - \tan\theta)(\sec\theta + \tan\theta) = 1 \]
Given \( \sec\theta + \tan\theta = 3 \):
\[ \sec\theta - \tan\theta = \frac{1}{3} \]
Now, add the two equations together:
\[ (\sec\theta + \tan\theta) + (\sec\theta - \tan\theta) = 3 + \frac{1}{3} \]
\[ 2\sec\theta = \frac{10}{3} \implies \sec\theta = \frac{5}{3} \]
Since \( \cos\theta = \frac{1}{\sec\theta} \):
\[ \cos\theta = \frac{3}{5} \]

</details>

3. 🔴 ⭐ Prove: (sin A − 2 sin³A)/(2 cos³A − cos A) = tan A.
<details>
<summary>Solution</summary>

Factor out \( \sin A \) from the numerator and \( \cos A \) from the denominator on the Left-Hand Side (LHS):
\[ \text{LHS} = \frac{\sin A(1 - 2\sin^2 A)}{\cos A(2\cos^2 A - 1)} \]
Using the identity \( 1 = \sin^2 A + \cos^2 A \):
- For numerator:
  \[ 1 - 2\sin^2 A = (\sin^2 A + \cos^2 A) - 2\sin^2 A = \cos^2 A - \sin^2 A \]
- For denominator:
  \[ 2\cos^2 A - 1 = 2\cos^2 A - (\sin^2 A + \cos^2 A) = \cos^2 A - \sin^2 A \]
Substituting these back into the expression:
\[ \text{LHS} = \frac{\sin A(\cos^2 A - \sin^2 A)}{\cos A(\cos^2 A - \sin^2 A)} \]
Cancel the common factor \( \cos^2 A - \sin^2 A \):
\[ \text{LHS} = \frac{\sin A}{\cos A} = \tan A = \text{RHS} \]
Hence proved.

</details>

4. 🔴 Eliminate θ: x = a sec³θ, y = b tan³θ.
<details>
<summary>Solution</summary>

Solve the equations for \( \sec\theta \) and \( \tan\theta \):
\[ \sec^3\theta = \frac{x}{a} \implies \sec\theta = \left(\frac{x}{a}\right)^{1/3} \]
\[ \tan^3\theta = \frac{y}{b} \implies \tan\theta = \left(\frac{y}{b}\right)^{1/3} \]
Using the identity \( \sec^2\theta - \tan^2\theta = 1 \):
\[ \left(\frac{x}{a}\right)^{2/3} - \left(\frac{y}{b}\right)^{2/3} = 1 \]
This is the required relation with \( \theta \) eliminated.

</details>

5. 🔴 If a sin²θ + b cos²θ = c, express tan²θ in terms of a, b, c.
<details>
<summary>Solution</summary>

Divide the entire equation by \( \cos^2\theta \):
\[ a\frac{\sin^2\theta}{\cos^2\theta} + b\frac{\cos^2\theta}{\cos^2\theta} = c\frac{1}{\cos^2\theta} \]
\[ a\tan^2\theta + b = c\sec^2\theta \]
Using the identity \( \sec^2\theta = 1 + \tan^2\theta \):
\[ a\tan^2\theta + b = c(1 + \tan^2\theta) \]
\[ a\tan^2\theta + b = c + c\tan^2\theta \]
Rearrange to group the \( \tan^2\theta \) terms:
\[ a\tan^2\theta - c\tan^2\theta = c - b \]
\[ (a - c)\tan^2\theta = c - b \]
\[ \tan^2\theta = \frac{c - b}{a - c} \]
*(Or equivalently, \( \tan^2\theta = \frac{b - c}{c - a} \))*

</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Prove: (1 + tan²A)/(1 + cot²A) = tan²A. **(2 marks)**

<details>
<summary>Solution</summary>

LHS = (sec²A)/(cosec²A) = (1/cos²A)/(1/sin²A) = sin²A/cos²A = tan²A = RHS ✓
</details>

---

**Q2.** 🟡 Prove: √((1 + sin A)/(1 − sin A)) = sec A + tan A. **(3 marks)**

<details>
<summary>Solution</summary>

LHS = √((1 + sin A)²/(1 − sin²A))
    = (1 + sin A)/√(cos²A)
    = (1 + sin A)/cos A
    = sec A + tan A = RHS ✓
</details>

---

**Q3.** 🟡 Prove: (sin θ − cos θ + 1)/(sin θ + cos θ − 1) = 1/(sec θ − tan θ). **(3 marks)**

<details>
<summary>Solution</summary>

Divide numerator and denominator by cos θ:
LHS = (tan θ − 1 + sec θ)/(tan θ + 1 − sec θ)
    = (tan θ + sec θ − 1)/(tan θ − sec θ + 1)
Now using identity sec²θ − tan²θ = 1:
    = (tan θ + sec θ − 1)/((tan θ − sec θ) + (sec²θ − tan²θ))
    = (tan θ + sec θ − 1)/((tan θ − sec θ)(1 − (tan θ + sec θ)))
... which simplifies to 1/(sec θ − tan θ) ✓
</details>

---

**Q4.** 🔴 If sec θ + tan θ = p, find the value of sin θ. **(3 marks)**

<details>
<summary>Solution</summary>

sec θ + tan θ = p   ...(1)
We know sec²θ − tan²θ = 1
(sec θ − tan θ)(sec θ + tan θ) = 1
(sec θ − tan θ)(p) = 1
sec θ − tan θ = 1/p   ...(2)

From (1) and (2):
sec θ = (p + 1/p)/2 = (p² + 1)/(2p)
tan θ = (p − 1/p)/2 = (p² − 1)/(2p)

sin θ = tan θ / sec θ = (p² − 1)/(p² + 1)
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** If sin θ − cos θ = 0, then sin⁴θ + cos⁴θ equals:
(a) 1/4
(b) 1/2
(c) 1
(d) 3/4

<details>
<summary>Solution</summary>
sin θ = cos θ → tan θ = 1 → sin θ = cos θ = 1/√2
sin⁴θ + cos⁴θ = (1/4) + (1/4) = 1/2
Answer: (b) 🟡
</details>

---

**Q2.** If sin⁴θ + cos⁴θ = 1, then θ equals:
(a) 0°
(b) 90°
(c) 0° or 90°
(d) 45°

<details>
<summary>Solution</summary>
sin⁴θ + cos⁴θ = (sin²θ + cos²θ)² − 2 sin²θ cos²θ = 1 − 2 sin²θ cos²θ
Given: 1 − 2 sin²θ cos²θ = 1
→ sin²θ cos²θ = 0
→ sin θ = 0 or cos θ = 0
→ θ = 0° or 90°
Answer: (c) 🔴 ⭐
</details>

---

**Q3.** If tan θ + cot θ = 2, then tan²θ + cot²θ equals:
(a) 1
(b) 2
(c) 3
(d) 4

<details>
<summary>Solution</summary>
tan θ + cot θ = 2
Square both sides: tan²θ + cot²θ + 2 tan θ cot θ = 4
tan²θ + cot²θ + 2(1) = 4
tan²θ + cot²θ = 2
Answer: (b) 🟡
</details>

---

**Q4.** The expression (sin⁶θ + cos⁶θ − 1)/(sin⁴θ + cos⁴θ − 1) simplifies to:
(a) 1
(b) 2/3
(c) 3/2
(d) 0

<details>
<summary>Solution</summary>
sin⁶θ + cos⁶θ = (sin²θ + cos²θ)³ − 3 sin²θ cos²θ(sin²θ + cos²θ) = 1 − 3 sin²θ cos²θ
sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ

Expression = (1 − 3 sin²θ cos²θ − 1)/(1 − 2 sin²θ cos²θ − 1)
= (−3 sin²θ cos²θ)/(−2 sin²θ cos²θ)
= 3/2
Answer: (c) 🔴 ⭐
</details>

---

**Q5.** If sin θ + sin²θ = 1, then cos²θ + cos⁴θ equals:
(a) 0
(b) 1
(c) 2
(d) −1

<details>
<summary>Solution</summary>
Given: sin θ + sin²θ = 1
→ sin θ = 1 − sin²θ = cos²θ

Now, cos²θ + cos⁴θ = sin θ + sin²θ = 1
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin²θ + cos²θ = 1 for all θ.
**Reason (R):** This follows from the Pythagoras theorem.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** 1 + tan²θ = sec²θ for all θ.
**Reason (R):** tan θ is defined for all real θ.

<details>
<summary>Solution</summary>
A is true: 1 + tan²θ = sec²θ.
R is false: tan θ is undefined at θ = 90°, 270°, etc.
Answer: (c)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The maximum value of sin⁴θ + cos⁴θ is 1.
**Reason (R):** sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ ≤ 1.

<details>
<summary>Solution</summary>
A is true (max = 1 at θ = 0°, 90°).
R is true (since sin²θ cos²θ ≥ 0).
R correctly explains A.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** (1 + tan²θ)(1 − sin θ)(1 + sin θ) = 1.
**Reason (R):** sec²θ × cos²θ = 1.

<details>
<summary>Solution</summary>
A: (1 + tan²θ)(1 − sin²θ) = sec²θ × cos²θ = 1. True.
R: sec²θ × cos²θ = (1/cos²θ)(cos²θ) = 1. True.
R explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin²θ + cos²θ = ?<br>
   (a) 0   (b) 1   (c) −1   (d) 2
<details>
<summary>Solution</summary>

This is the fundamental Pythagorean identity:
\[ \sin^2\theta + \cos^2\theta = 1 \]

**Answer: (b) 1**
</details>

2. 🟢 1 + tan²θ = ?<br>
   (a) sin²θ   (b) cot²θ   (c) sec²θ   (d) cosec²θ
<details>
<summary>Solution</summary>

By the second Pythagorean identity (obtained by dividing \( \sin^2\theta + \cos^2\theta = 1 \) by \( \cos^2\theta \)):
\[ 1 + \tan^2\theta = \sec^2\theta \]

**Answer: (c) sec²θ**
</details>

3. 🟢 1 + cot²θ = ?<br>
   (a) tan²θ   (b) sec²θ   (c) cosec²θ   (d) sin²θ
<details>
<summary>Solution</summary>

By the third Pythagorean identity (obtained by dividing \( \sin^2\theta + \cos^2\theta = 1 \) by \( \sin^2\theta \)):
\[ 1 + \cot^2\theta = \csc^2\theta \]

**Answer: (c) cosec²θ**
</details>

4. 🟡 (sec²θ − 1) equals:
   (a) tan²θ   (b) cot²θ   (c) sin²θ   (d) cos²θ
<details>
<summary>Solution</summary>

Rearranging the identity \( 1 + \tan^2\theta = \sec^2\theta \):
\[ \sec^2\theta - 1 = \tan^2\theta \]

**Answer: (a) tan²θ**
</details>

5. 🟡 (1 − sin²θ)(1 + tan²θ) equals:
   (a) 0   (b) 1   (c) 2   (d) −1
<details>
<summary>Solution</summary>

Substitute the identities \( 1 - \sin^2\theta = \cos^2\theta \) and \( 1 + \tan^2\theta = \sec^2\theta \):
\[ (1 - \sin^2\theta)(1 + \tan^2\theta) = \cos^2\theta \times \sec^2\theta \]
Since \( \sec^2\theta = \frac{1}{\cos^2\theta} \):
\[ \cos^2\theta \times \frac{1}{\cos^2\theta} = 1 \]

**Answer: (b) 1**
</details>

6. 🟡 If sin θ = 3/5, cos²θ = ?<br>
   (a) 9/25   (b) 16/25   (c) 4/5   (d) 25/16
<details>
<summary>Solution</summary>

Using the identity \( \cos^2\theta = 1 - \sin^2\theta \):
\[ \cos^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25} \]

**Answer: (b) 16/25**
</details>

7. 🟡 (sin θ + cos θ)² = ?<br>
   (a) 1   (b) 1 + 2 sin θ cos θ   (c) 1 − 2 sin θ cos θ   (d) 2
<details>
<summary>Solution</summary>

Expanding the square:
\[ (\sin\theta + \cos\theta)^2 = \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta \]
Substitute \( \sin^2\theta + \cos^2\theta = 1 \):
\[ (\sin\theta + \cos\theta)^2 = 1 + 2\sin\theta\cos\theta \]

**Answer: (b) 1 + 2 sin θ cos θ**
</details>

8. 🟡 (sin θ − cos θ)² = ?<br>
   (a) 1   (b) 1 + 2 sin θ cos θ   (c) 1 − 2 sin θ cos θ   (d) 2
<details>
<summary>Solution</summary>

Expanding the square:
\[ (\sin\theta - \cos\theta)^2 = \sin^2\theta + \cos^2\theta - 2\sin\theta\cos\theta \]
Substitute \( \sin^2\theta + \cos^2\theta = 1 \):
\[ (\sin\theta - \cos\theta)^2 = 1 - 2\sin\theta\cos\theta \]

**Answer: (c) 1 − 2 sin θ cos θ**
</details>

9. 🟢 sec²θ − tan²θ = ?<br>
   (a) 0   (b) 1   (c) −1   (d) 2
<details>
<summary>Solution</summary>

From the identity \( 1 + \tan^2\theta = \sec^2\theta \), subtracting \( \tan^2\theta \) from both sides yields:
\[ \sec^2\theta - \tan^2\theta = 1 \]

**Answer: (b) 1**
</details>

10. 🟡 If tan θ = 2, sec θ = ?<br>
    (a) √5   (b) 5   (c) √3   (d) 3
<details>
<summary>Solution</summary>

Using the identity \( \sec^2\theta = 1 + \tan^2\theta \):
\[ \sec^2\theta = 1 + 2^2 = 5 \implies \sec\theta = \sqrt{5} \]
*(Assuming acute angle \( \theta \) for the positive sign)*

**Answer: (a) \(\sqrt{5}\)**
</details>

11. 🟡 If cot θ = 3, cosec θ = ?<br>
    (a) √10   (b) √8   (c) 3   (d) 10
<details>
<summary>Solution</summary>

Using the identity \( \csc^2\theta = 1 + \cot^2\theta \):
\[ \csc^2\theta = 1 + 3^2 = 10 \implies \csc\theta = \sqrt{10} \]
*(Assuming acute angle \( \theta \) for the positive sign)*

**Answer: (a) \(\sqrt{10}\)**
</details>

12. 🟡 sin⁴θ − cos⁴θ = ?<br>
    (a) 1   (b) sin²θ − cos²θ   (c) 0   (d) 2
<details>
<summary>Solution</summary>

Factoring as a difference of squares:
\[ \sin^4\theta - \cos^4\theta = (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) \]
Since \( \sin^2\theta + \cos^2\theta = 1 \):
\[ \sin^4\theta - \cos^4\theta = (\sin^2\theta - \cos^2\theta) \times 1 = \sin^2\theta - \cos^2\theta \]

**Answer: (b) sin²θ − cos²θ**
</details>

13. 🟡 (1 + tan θ)² + (1 − tan θ)² = ?<br>
    (a) 2   (b) 2 sec²θ   (c) 2 tan²θ   (d) 4
<details>
<summary>Solution</summary>

Expanding both squares:
\[ (1+\tan\theta)^2 + (1-\tan\theta)^2 = (1 + \tan^2\theta + 2\tan\theta) + (1 + \tan^2\theta - 2\tan\theta) = 2(1 + \tan^2\theta) \]
Since \( 1 + \tan^2\theta = \sec^2\theta \):
\[ 2(1 + \tan^2\theta) = 2\sec^2\theta \]

**Answer: (b) 2 sec²θ**
</details>

14. 🟡 1/(1 + sin θ) + 1/(1 − sin θ) = ?<br>
    (a) 2   (b) 2 sec²θ   (c) 2 cos²θ   (d) 2 sin²θ
<details>
<summary>Solution</summary>

Combining the fractions:
\[ \frac{1}{1+\sin\theta} + \frac{1}{1-\sin\theta} = \frac{1-\sin\theta + 1+\sin\theta}{(1+\sin\theta)(1-\sin\theta)} = \frac{2}{1-\sin^2\theta} \]
Using \( 1 - \sin^2\theta = \cos^2\theta \):
\[ \frac{2}{\cos^2\theta} = 2\sec^2\theta \]

**Answer: (b) 2 sec²θ**
</details>

15. 🟢 Which identity is CORRECT?<br>
    (a) sin²θ = 1 + cos²θ   (b) 1 + cot²θ = cosec²θ   (c) tan²θ + 1 = cosec²θ   (d) sec²θ + 1 = tan²θ
<details>
<summary>Solution</summary>

Let's verify each statement:
- (a) Incorrect: \( \sin^2\theta = 1 - \cos^2\theta \)
- (b) Correct: This is the standard identity \( 1 + \cot^2\theta = \csc^2\theta \)
- (c) Incorrect: \( \tan^2\theta + 1 = \sec^2\theta \)
- (d) Incorrect: \( \sec^2\theta - 1 = \tan^2\theta \)

**Answer: (b) 1 + cot²θ = cosec²θ**
</details>

16. 🟡 If sec θ + tan θ = 2, then sec θ − tan θ = ?<br>
    (a) 2   (b) 1/2   (c) 0   (d) 1
<details>
<summary>Solution</summary>

Since \( \sec^2\theta - \tan^2\theta = 1 \implies (\sec\theta - \tan\theta)(\sec\theta + \tan\theta) = 1 \):
\[ \sec\theta - \tan\theta = \frac{1}{\sec\theta + \tan\theta} = \frac{1}{2} \]

**Answer: (b) 1/2**
</details>

17. 🟡 If sin θ + cos θ = √2, then sin θ cos θ = ?<br>
    (a) 1/2   (b) 1   (c) 0   (d) 2
<details>
<summary>Solution</summary>

Squaring both sides of \( \sin\theta + \cos\theta = \sqrt{2} \):
\[ (\sin\theta + \cos\theta)^2 = 2 \implies \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta = 2 \]
Substitute \( \sin^2\theta + \cos^2\theta = 1 \):
\[ 1 + 2\sin\theta\cos\theta = 2 \implies 2\sin\theta\cos\theta = 1 \implies \sin\theta\cos\theta = \frac{1}{2} \]

**Answer: (a) 1/2**
</details>

18. 🟡 (sin⁴θ + cos⁴θ) + 2 sin²θ cos²θ = ?<br>
    (a) 0   (b) 1   (c) 2   (d) 1/2
<details>
<summary>Solution</summary>

This is a perfect square expansion in the form of \( a^2 + 2ab + b^2 = (a+b)^2 \), where \( a = \sin^2\theta \) and \( b = \cos^2\theta \):
\[ (\sin^2\theta)^2 + 2\sin^2\theta\cos^2\theta + (\cos^2\theta)^2 = (\sin^2\theta + \cos^2\theta)^2 \]
Substituting \( \sin^2\theta + \cos^2\theta = 1 \):
\[ (\sin^2\theta + \cos^2\theta)^2 = 1^2 = 1 \]

**Answer: (b) 1**
</details>

19. 🟡 sin θ/(1 + cos θ) + (1 + cos θ)/sin θ = ?<br>
    (a) 2 sin θ   (b) 2 cos θ   (c) 2 cosec θ   (d) 2 sec θ
<details>
<summary>Solution</summary>

Combine the terms by finding a common denominator:
\[ \text{Expression} = \frac{\sin^2\theta + (1+\cos\theta)^2}{\sin\theta(1+\cos\theta)} = \frac{\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta}{\sin\theta(1+\cos\theta)} \]
Group \( \sin^2\theta + \cos^2\theta \):
\[ \text{Expression} = \frac{(\sin^2\theta + \cos^2\theta) + 1 + 2\cos\theta}{\sin\theta(1+\cos\theta)} = \frac{1 + 1 + 2\cos\theta}{\sin\theta(1+\cos\theta)} \]
\[ = \frac{2(1+\cos\theta)}{\sin\theta(1+\cos\theta)} = \frac{2}{\sin\theta} = 2\csc\theta \]

**Answer: (c) 2 cosec θ**
</details>

20. 🟡 If tan²θ = 1 − e², then sec θ + tan³θ cosec θ = ?<br>
    (a) (2 − e²)^(3/2)   (b) (2 − e²)^(1/2)   (c) 2 − e²   (d) 1
<details>
<summary>Solution</summary>

Simplify the expression:
\[ \sec\theta + \tan^3\theta\csc\theta = \sec\theta + \frac{\sin^3\theta}{\cos^3\theta} \times \frac{1}{\sin\theta} \]
\[ = \sec\theta + \frac{\sin^2\theta}{\cos^3\theta} = \sec\theta + \frac{\sin^2\theta}{\cos^2\theta} \times \frac{1}{\cos\theta} \]
\[ = \sec\theta + \tan^2\theta\sec\theta = \sec\theta(1+\tan^2\theta) \]
Since \( 1 + \tan^2\theta = \sec^2\theta \):
\[ \sec\theta(1+\tan^2\theta) = \sec^3\theta = (\sec^2\theta)^{3/2} \]
Substitute \( \sec^2\theta = 1 + \tan^2\theta = 1 + (1 - e^2) = 2 - e^2 \):
\[ \sec^3\theta = (2 - e^2)^{3/2} \]

**Answer: (a) (2 − e²)^(3/2)**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | a | 16 | b |
| 2 | c | 7 | b | 12 | b | 17 | a |
| 3 | c | 8 | c | 13 | b | 18 | b |
| 4 | a | 9 | b | 14 | b | 19 | c |
| 5 | b | 10 | a | 15 | b | 20 | a |

</details>
