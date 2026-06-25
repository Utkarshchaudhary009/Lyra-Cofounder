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
<details>
<summary>Solution</summary>

**Step 1: Find the principal solutions.**
The principal solutions lie in the interval \([0, 2\pi)\) (or \([0^\circ, 360^\circ)\)).
Since \(\sin \theta = \frac{1}{2} > 0\), \(\theta\) must lie in the first or second quadrant.
- In Quadrant I: \(\theta = \frac{\pi}{6}\) (or \(30^\circ\))
- In Quadrant II: \(\theta = \pi - \frac{\pi}{6} = \frac{5\pi}{6}\) (or \(150^\circ\))

So, the principal solutions are \(\theta = \frac{\pi}{6}, \frac{5\pi}{6}\) (or \(30^\circ, 150^\circ\)).

**Step 2: Find the general solution.**
The general solution of \(\sin \theta = \sin \alpha\) is given by:
\[ \theta = n\pi + (-1)^n \alpha, \quad n \in \mathbb{Z} \]
Using \(\alpha = \frac{\pi}{6}\):
\[ \theta = n\pi + (-1)^n \frac{\pi}{6}, \quad n \in \mathbb{Z} \]
</details>

2. 🟡 Solve sin θ = 0. Give general solution.
<details>
<summary>Solution</summary>

The sine function is zero at all integer multiples of \(\pi\).
Therefore, the general solution of \(\sin \theta = 0\) is:
\[ \theta = n\pi, \quad n \in \mathbb{Z} \]
</details>

3. 🟡 Solve sin θ = −1/√2. Give principal solutions.
<details>
<summary>Solution</summary>

The principal solutions must lie in the interval \([0, 2\pi)\).
Since \(\sin \theta = -\frac{1}{\sqrt{2}} < 0\), \(\theta\) lies in Quadrant III or IV.
The reference angle is \(\frac{\pi}{4}\) (since \(\sin \frac{\pi}{4} = \frac{1}{\sqrt{2}}\)).
- In Quadrant III: \(\theta = \pi + \frac{\pi}{4} = \frac{5\pi}{4}\) (or \(225^\circ\))
- In Quadrant IV: \(\theta = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}\) (or \(315^\circ\))

Thus, the principal solutions are \(\theta = \frac{5\pi}{4}, \frac{7\pi}{4}\) (or \(225^\circ, 315^\circ\)).
</details>

4. 🟡 Solve sin θ = 1. Give general solution.
<details>
<summary>Solution</summary>

We have \(\sin \theta = 1\).
The smallest positive angle satisfying this is \(\theta = \frac{\pi}{2}\).
The general solution for \(\sin \theta = \sin \alpha\) is:
\[ \theta = n\pi + (-1)^n \alpha, \quad n \in \mathbb{Z} \]
For \(\alpha = \frac{\pi}{2}\):
- If \(n\) is even (\(n = 2m\)): \(\theta = 2m\pi + \frac{\pi}{2}\)
- If \(n\) is odd (\(n = 2m+1\)): \(\theta = (2m+1)\pi - \frac{\pi}{2} = 2m\pi + \pi - \frac{\pi}{2} = 2m\pi + \frac{\pi}{2}\)

In either case, the solution simplifies to:
\[ \theta = 2n\pi + \frac{\pi}{2} = (4n+1)\frac{\pi}{2}, \quad n \in \mathbb{Z} \]
</details>

5. 🔴 Solve sin θ = √(3)/2 for θ ∈ [−π, π].
<details>
<summary>Solution</summary>

We need to solve \(\sin \theta = \frac{\sqrt{3}}{2}\) in the interval \([-\pi, \pi]\).
Since \(\frac{\sqrt{3}}{2}\) is positive, \(\theta\) must lie in Quadrant I or II.
- In Quadrant I: \(\theta = \frac{\pi}{3}\)
- In Quadrant II: \(\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}\)

Both \(\frac{\pi}{3}\) and \(\frac{2\pi}{3}\) lie within the interval \([-\pi, \pi]\).
Therefore, the solutions are:
\[ \theta = \frac{\pi}{3}, \frac{2\pi}{3} \]
</details>

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
<details>
<summary>Solution</summary>

**Principal Solutions:**
Since \(\cos \theta = \frac{\sqrt{3}}{2} > 0\), \(\theta\) lies in Quadrant I or IV:
- Quadrant I: \(\theta = \frac{\pi}{6}\) (or \(30^\circ\))
- Quadrant IV: \(\theta = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6}\) (or \(330^\circ\))

**General Solution:**
The general solution of \(\cos \theta = \cos \alpha\) is:
\[ \theta = 2n\pi \pm \alpha, \quad n \in \mathbb{Z} \]
Substituting \(\alpha = \frac{\pi}{6}\):
\[ \theta = 2n\pi \pm \frac{\pi}{6}, \quad n \in \mathbb{Z} \]
</details>

7. 🟡 Solve cos θ = 0.
<details>
<summary>Solution</summary>

**Principal Solutions:**
In the interval \([0, 2\pi)\), the cosine function is zero at:
\[ \theta = \frac{\pi}{2}, \frac{3\pi}{2} \quad (\text{or } 90^\circ, 270^\circ) \]

**General Solution:**
The cosine function is zero at all odd multiples of \(\frac{\pi}{2}\):
\[ \theta = (2n+1)\frac{\pi}{2}, \quad n \in \mathbb{Z} \]
</details>

8. 🟡 Solve cos θ = −1/2.
<details>
<summary>Solution</summary>

**Principal Solutions:**
Since \(\cos \theta = -\frac{1}{2} < 0\), \(\theta\) lies in Quadrant II or III.
The reference angle is \(\frac{\pi}{3}\) (since \(\cos \frac{\pi}{3} = \frac{1}{2}\)).
- Quadrant II: \(\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}\) (or \(120^\circ\))
- Quadrant III: \(\theta = \pi + \frac{\pi}{3} = \frac{4\pi}{3}\) (or \(240^\circ\))

**General Solution:**
Using \(\alpha = \frac{2\pi}{3}\):
\[ \theta = 2n\pi \pm \frac{2\pi}{3}, \quad n \in \mathbb{Z} \]
</details>

9. 🟡 Solve cos θ = −1.
<details>
<summary>Solution</summary>

**Principal Solution:**
In the interval \([0, 2\pi)\), the only angle that satisfies \(\cos \theta = -1\) is:
\[ \theta = \pi \quad (\text{or } 180^\circ) \]

**General Solution:**
The general solution is given by:
\[ \theta = (2n+1)\pi, \quad n \in \mathbb{Z} \]
</details>

10. 🔴 Solve cos θ = 0.5 for θ ∈ [−π, π].
<details>
<summary>Solution</summary>

We need to solve \(\cos \theta = 0.5 = \frac{1}{2}\) in the interval \([-\pi, \pi]\).
Since \(\cos \theta > 0\), the solution lies in Quadrant I (positive angle) and Quadrant IV (negative angle):
- Quadrant I: \(\theta = \frac{\pi}{3}\)
- Quadrant IV: \(\theta = -\frac{\pi}{3}\)

Both angles lie within the interval \([-\pi, \pi]\).
Therefore, the solutions are:
\[ \theta = -\frac{\pi}{3}, \frac{\pi}{3} \]
</details>

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
<details>
<summary>Solution</summary>

**Principal Solutions:**
Since \(\tan \theta = 1 > 0\), \(\theta\) lies in Quadrant I or III:
- Quadrant I: \(\theta = \frac{\pi}{4}\) (or \(45^\circ\))
- Quadrant III: \(\theta = \pi + \frac{\pi}{4} = \frac{5\pi}{4}\) (or \(225^\circ\))

**General Solution:**
The general solution of \(\tan \theta = \tan \alpha\) is:
\[ \theta = n\pi + \alpha, \quad n \in \mathbb{Z} \]
Using \(\alpha = \frac{\pi}{4}\):
\[ \theta = n\pi + \frac{\pi}{4}, \quad n \in \mathbb{Z} \]
</details>

12. 🟡 Solve tan θ = 0.
<details>
<summary>Solution</summary>

**Principal Solutions:**
In \([0, 2\pi)\), \(\tan \theta = 0\) at:
\[ \theta = 0, \pi \]

**General Solution:**
Since \(\tan \theta = \frac{\sin \theta}{\cos \theta}\), it is zero when \(\sin \theta = 0\):
\[ \theta = n\pi, \quad n \in \mathbb{Z} \]
</details>

13. 🟡 Solve tan θ = 1/√3.
<details>
<summary>Solution</summary>

**Principal Solutions:**
Since \(\tan \theta = \frac{1}{\sqrt{3}} > 0\), \(\theta\) lies in Quadrant I or III:
- Quadrant I: \(\theta = \frac{\pi}{6}\) (or \(30^\circ\))
- Quadrant III: \(\theta = \pi + \frac{\pi}{6} = \frac{7\pi}{6}\) (or \(210^\circ\))

**General Solution:**
Using \(\alpha = \frac{\pi}{6}\):
\[ \theta = n\pi + \frac{\pi}{6}, \quad n \in \mathbb{Z} \]
</details>

14. 🟡 Solve tan θ = −1.
<details>
<summary>Solution</summary>

**Principal Solutions:**
Since \(\tan \theta = -1 < 0\), \(\theta\) lies in Quadrant II or IV:
- Quadrant II: \(\theta = \pi - \frac{\pi}{4} = \frac{3\pi}{4}\) (or \(135^\circ\))
- Quadrant IV: \(\theta = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4}\) (or \(315^\circ\))

**General Solution:**
Using the Quadrant II principal solution \(\alpha = \frac{3\pi}{4}\):
\[ \theta = n\pi + \frac{3\pi}{4}, \quad n \in \mathbb{Z} \]
*(Note: This is equivalent to \(\theta = n\pi - \frac{\pi}{4}\).)*
</details>

15. 🔴 Solve tan θ = −√3 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

We need to solve \(\tan \theta = -\sqrt{3}\) in the interval \([0, 2\pi]\).
Since \(\tan \theta < 0\), \(\theta\) lies in Quadrant II or IV.
The reference angle is \(\frac{\pi}{3}\) because \(\tan \frac{\pi}{3} = \sqrt{3}\).
- Quadrant II: \(\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}\)
- Quadrant IV: \(\theta = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}\)

Both angles lie within \([0, 2\pi]\).
Therefore, the solutions are:
\[ \theta = \frac{2\pi}{3}, \frac{5\pi}{3} \]
</details>

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
<details>
<summary>Solution</summary>

**Step 1: Factor the quadratic equation.**
Let \(t = \cos \theta\). The equation becomes:
\[ 2t^2 - 3t + 1 = 0 \]
Factoring by splitting the middle term:
\[ 2t^2 - 2t - t + 1 = 0 \]
\[ 2t(t - 1) - 1(t - 1) = 0 \]
\[ (2t - 1)(t - 1) = 0 \]
This gives:
\[ t = \frac{1}{2} \quad \text{or} \quad t = 1 \]

**Step 2: Solve for \(\theta\) in the range \([0^\circ, 360^\circ]\).**
- Case 1: \(\cos \theta = 1\)
  \[ \theta = 0^\circ, 360^\circ \]
- Case 2: \(\cos \theta = \frac{1}{2}\\)
  Since \(\cos \theta\) is positive, \(\theta\) is in Quadrant I or IV:
  - Quadrant I: \(\theta = 60^\circ\)
  - Quadrant IV: \(\theta = 360^\circ - 60^\circ = 300^\circ\)

**Conclusion:**
Combining all solutions, we get:
\[ \theta = 0^\circ, 60^\circ, 300^\circ, 360^\circ \]
</details>

17. 🟡 Solve 4 sin²θ = 1 for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Simplify the equation.**
\[ 4\sin^2\theta = 1 \implies \sin^2\theta = \frac{1}{4} \]
Taking the square root on both sides:
\[ \sin \theta = \pm \frac{1}{2} \]

**Step 2: Solve for \(\theta\) in the range \([0^\circ, 360^\circ]\).**
- Case 1: \(\sin \theta = \frac{1}{2}\) (positive in Quadrant I & II)
  - Quadrant I: \(\theta = 30^\circ\)
  - Quadrant II: \(\theta = 180^\circ - 30^\circ = 150^\circ\)
- Case 2: \(\sin \theta = -\frac{1}{2}\) (negative in Quadrant III & IV)
  - Quadrant III: \(\theta = 180^\circ + 30^\circ = 210^\circ\)
  - Quadrant IV: \(\theta = 360^\circ - 30^\circ = 330^\circ\)

**Conclusion:**
The solutions are:
\[ \theta = 30^\circ, 150^\circ, 210^\circ, 330^\circ \]
</details>

18. 🟡 Solve tan²θ − √3 tan θ = 0 for 0° ≤ θ ≤ 180°.
<details>
<summary>Solution</summary>

**Step 1: Factor the equation.**
\[ \tan^2\theta - \sqrt{3}\tan\theta = 0 \]
Factor out \(\tan\theta\):
\[ \tan\theta(\tan\theta - \sqrt{3}) = 0 \]
This gives two cases:
\[ \tan\theta = 0 \quad \text{or} \quad \tan\theta = \sqrt{3} \]

**Step 2: Solve for \(\theta\) in the range \([0^\circ, 180^\circ]\).**
- Case 1: \(\tan\theta = 0\)
  \[ \theta = 0^\circ, 180^\circ \]
- Case 2: \(\tan\theta = \sqrt{3}\)
  Since \(\sqrt{3}\) is positive, \(\theta\) lies in Quadrant I (the range is only up to \(180^\circ\)):
  \[ \theta = 60^\circ \]

**Conclusion:**
The solutions are:
\[ \theta = 0^\circ, 60^\circ, 180^\circ \]
</details>

19. 🔴 Solve 2 sin²θ + 3 cos θ = 0 for 0° ≤ θ ≤ 360°. (Hint: Convert sin² to cos².)
<details>
<summary>Solution</summary>

**Step 1: Convert the equation to be in terms of \(\cos\theta\).**
Using \(\sin^2\theta = 1 - \cos^2\theta\):
\[ 2(1 - \cos^2\theta) + 3\cos\theta = 0 \]
\[ 2 - 2\cos^2\theta + 3\cos\theta = 0 \]
Multiply by \(-1\) to write it in standard quadratic form:
\[ 2\cos^2\theta - 3\cos\theta - 2 = 0 \]

**Step 2: Factor the quadratic equation.**
Let \(t = \cos\theta\):
\[ 2t^2 - 3t - 2 = 0 \]
\[ 2t^2 - 4t + t - 2 = 0 \]
\[ 2t(t - 2) + 1(t - 2) = 0 \]
\[ (2t + 1)(t - 2) = 0 \]
This gives:
\[ \cos\theta = -\frac{1}{2} \quad \text{or} \quad \cos\theta = 2 \]

Since \(\cos\theta\) cannot exceed \(1\), \(\cos\theta = 2\) has no real solution.

**Step 3: Solve \(\cos\theta = -\frac{1}{2}\) for \(\theta \in [0^\circ, 360^\circ]\).**
Since \(\cos\theta < 0\), \(\theta\) lies in Quadrant II or III. The reference angle is \(60^\circ\):
- Quadrant II: \(\theta = 180^\circ - 60^\circ = 120^\circ\)
- Quadrant III: \(\theta = 180^\circ + 60^\circ = 240^\circ\)

**Conclusion:**
The solutions are:
\[ \theta = 120^\circ, 240^\circ \]
</details>

20. 🔴 ⭐ Solve 3 cos²θ + 2 sin θ − 2 = 0 for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Convert the equation to be in terms of \(\sin\theta\).**
Using \(\cos^2\theta = 1 - \sin^2\theta\):
\[ 3(1 - \sin^2\theta) + 2\sin\theta - 2 = 0 \]
\[ 3 - 3\sin^2\theta + 2\sin\theta - 2 = 0 \]
\[ -3\sin^2\theta + 2\sin\theta + 1 = 0 \]
Multiply by \(-1\):
\[ 3\sin^2\theta - 2\sin\theta - 1 = 0 \]

**Step 2: Factor the quadratic equation.**
Let \(t = \sin\theta\):
\[ 3t^2 - 2t - 1 = 0 \]
\[ (3t + 1)(t - 1) = 0 \]
This gives:
\[ \sin\theta = 1 \quad \text{or} \quad \sin\theta = -\frac{1}{3} \]

**Step 3: Solve for \(\theta\) in \([0^\circ, 360^\circ]\).**
- Case 1: \(\sin\theta = 1\)
  \[ \theta = 90^\circ \]
- Case 2: \(\sin\theta = -\frac{1}{3}\)
  Since \(\sin\theta\) is negative, the solutions lie in Quadrant III and IV.
  Let \(\alpha = \sin^{-1}\left(\frac{1}{3}\right)\) be the reference angle (approx. \(19.47^\circ\)):
  - Quadrant III: \(\theta = 180^\circ + \sin^{-1}\left(\frac{1}{3}\right)\)
  - Quadrant IV: \(\theta = 360^\circ - \sin^{-1}\left(\frac{1}{3}\right)\)

**Conclusion:**
The solutions are:
\[ \theta = 90^\circ, \ 180^\circ + \sin^{-1}\left(\frac{1}{3}\right), \ 360^\circ - \sin^{-1}\left(\frac{1}{3}\right) \]
</details>

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
<details>
<summary>Solution</summary>

**Step 1: Convert the equation to be in terms of \(\cos\theta\).**
Using \(\sin^2\theta = 1 - \cos^2\theta\):
\[ 5(1 - \cos^2\theta) - 4\cos\theta = 4 \]
\[ 5 - 5\cos^2\theta - 4\cos\theta = 4 \]
\[ 5\cos^2\theta + 4\cos\theta - 1 = 0 \]

**Step 2: Factor the quadratic equation.**
Let \(t = \cos\theta\):
\[ 5t^2 + 4t - 1 = 0 \]
\[ (5t - 1)(t + 1) = 0 \]
This gives:
\[ \cos\theta = \frac{1}{5} \quad \text{or} \quad \cos\theta = -1 \]

**Step 3: Solve for \(\theta\) in \([0^\circ, 360^\circ]\).**
- Case 1: \(\cos\theta = -1\)
  \[ \theta = 180^\circ \]
- Case 2: \(\cos\theta = \frac{1}{5}\)
  Since \(\cos\theta > 0\), \(\theta\) lies in Quadrant I and IV:
  - Quadrant I: \(\theta = \cos^{-1}\left(\frac{1}{5}\right)\)
  - Quadrant IV: \(\theta = 360^\circ - \cos^{-1}\left(\frac{1}{5}\right)\)

**Conclusion:**
The solutions are:
\[ \theta = 180^\circ, \ \cos^{-1}\left(\frac{1}{5}\right), \ 360^\circ - \cos^{-1}\left(\frac{1}{5}\right) \]
</details>

22. 🟡 Solve 2 sin²θ + 5 cos θ + 1 = 0 for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Convert the equation to be in terms of \(\cos\theta\).**
Using \(\sin^2\theta = 1 - \cos^2\theta\):
\[ 2(1 - \cos^2\theta) + 5\cos\theta + 1 = 0 \]
\[ 2 - 2\cos^2\theta + 5\cos\theta + 1 = 0 \]
\[ 2\cos^2\theta - 5\cos\theta - 3 = 0 \]

**Step 2: Factor the quadratic equation.**
Let \(t = \cos\theta\):
\[ 2t^2 - 5t - 3 = 0 \]
\[ (2t + 1)(t - 3) = 0 \]
This gives:
\[ \cos\theta = -\frac{1}{2} \quad \text{or} \quad \cos\theta = 3 \ \text{(no real solution)} \]

**Step 3: Solve \(\cos\theta = -\frac{1}{2}\) for \(\theta \in [0^\circ, 360^\circ]\).**
- Quadrant II: \(\theta = 180^\circ - 60^\circ = 120^\circ\)
- Quadrant III: \(\theta = 180^\circ + 60^\circ = 240^\circ\)

**Conclusion:**
The solutions are:
\[ \theta = 120^\circ, 240^\circ \]
</details>

23. 🟡 Solve 3 sin²θ + 4 cos²θ = 5 for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Simplify using trigonometric identities.**
We can rewrite the equation as:
\[ 3\sin^2\theta + 3\cos^2\theta + \cos^2\theta = 5 \]
Since \(\sin^2\theta + \cos^2\theta = 1\):
\[ 3(1) + \cos^2\theta = 5 \]
\[ 3 + \cos^2\theta = 5 \]
\[ \cos^2\theta = 2 \]

**Step 2: Analyze the result.**
Taking the square root:
\[ \cos\theta = \pm\sqrt{2} \]
Since \(\sqrt{2} \approx 1.414\), and the range of \(\cos\theta\) is \([-1, 1]\), \(\cos\theta\) cannot be greater than \(1\) or less than \(-1\).

Therefore, there is **no real solution** for this equation.
</details>

24. 🔴 Solve sec²θ = 1 + tan θ for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Use the identity \(\sec^2\theta = 1 + \tan^2\theta\).**
Substitute this into the equation:
\[ 1 + \tan^2\theta = 1 + \tan\theta \]
Subtract 1 from both sides:
\[ \tan^2\theta = \tan\theta \]
\[ \tan^2\theta - \tan\theta = 0 \]
Factor out \(\tan\theta\):
\[ \tan\theta(\tan\theta - 1) = 0 \]
This gives two cases:
\[ \tan\theta = 0 \quad \text{or} \quad \tan\theta = 1 \]

**Step 2: Solve for \(\theta\) in \([0^\circ, 360^\circ]\).**
- Case 1: \(\tan\theta = 0\)
  \[ \theta = 0^\circ, 180^\circ, 360^\circ \]
- Case 2: \(\tan\theta = 1\)
  Since \(\tan\theta > 0\), \(\theta\) lies in Quadrant I or III:
  - Quadrant I: \(\theta = 45^\circ\)
  - Quadrant III: \(\theta = 180^\circ + 45^\circ = 225^\circ\)

**Conclusion:**
The solutions are:
\[ \theta = 0^\circ, 45^\circ, 180^\circ, 225^\circ, 360^\circ \]
</details>

25. 🔴 ⭐ Solve 2 sin²θ + sin²2θ = 2 for 0° ≤ θ ≤ 360°.
<details>
<summary>Solution</summary>

**Step 1: Simplify the equation using double angle formula.**
Recall \(\sin 2\theta = 2\sin\theta\cos\theta\). Thus, \(\sin^2 2\theta = 4\sin^2\theta\cos^2\theta\).
Substitute this into the equation:
\[ 2\sin^2\theta + 4\sin^2\theta\cos^2\theta = 2 \]
Divide the entire equation by 2:
\[ \sin^2\theta + 2\sin^2\theta\cos^2\theta = 1 \]
Rearrange to group the \(\sin^2\theta\) terms or use \(1 - \sin^2\theta = \cos^2\theta\):
\[ 2\sin^2\theta\cos^2\theta = 1 - \sin^2\theta \]
\[ 2\sin^2\theta\cos^2\theta = \cos^2\theta \]
\[ 2\sin^2\theta\cos^2\theta - \cos^2\theta = 0 \]
Factor out \(\cos^2\theta\):
\[ \cos^2\theta (2\sin^2\theta - 1) = 0 \]

**Step 2: Solve the factored equations for \(\theta \in [0^\circ, 360^\circ]\).**
- **Case 1:** \(\cos^2\theta = 0 \implies \cos\theta = 0\)
  \[ \theta = 90^\circ, 270^\circ \]
- **Case 2:** \(2\sin^2\theta - 1 = 0 \implies \sin^2\theta = \frac{1}{2} \implies \sin\theta = \pm\frac{1}{\sqrt{2}}\)
  - For \(\sin\theta = \frac{1}{\sqrt{2}}\): \(\theta = 45^\circ, 135^\circ\)
  - For \(\sin\theta = -\frac{1}{\sqrt{2}}\): \(\theta = 225^\circ, 315^\circ\)

**Conclusion:**
Combining all solutions in order:
\[ \theta = 45^\circ, 90^\circ, 135^\circ, 225^\circ, 270^\circ, 315^\circ \]
</details>

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
