# Chapter 13: Inverse Trigonometric Functions

---

## Stage 1: The Core Idea

### The Problem Inverses Solve

We know sin 30° = 1/2. But what if I ask: "What angle has sin = 1/2?<br>"

We need a function that does the opposite — an **inverse** function.

But here's the problem: sin θ is NOT one-to-one. sin 30° = 1/2, sin 150° = 1/2, sin 390° = 1/2... infinitely many angles give the same sine.

To make an inverse, we **restrict the domain** — choose a specific interval where the function is one-to-one. This restricted range gives us the **principal value**.

```
sin x: domain restricted to [−π/2, π/2]  →  arcsin x has range [−π/2, π/2]
cos x: domain restricted to [0, π]        →  arccos x has range [0, π]
tan x: domain restricted to (−π/2, π/2)   →  arctan x has range (−π/2, π/2)
```

---

## Stage 2: The Formula Lab

### Notation

```
arcsin x or sin⁻¹x   (NOT (sin x)⁻¹ which is cosec x!)
arccos x or cos⁻¹x
arctan x or tan⁻¹x
arccot x or cot⁻¹x
arcsec x or sec⁻¹x
arccosec x or cosec⁻¹x
```

**Trap to avoid:** sin⁻¹x ≠ (sin x)⁻¹. This is the #1 mistake in inverse trig.

### Domain and Range (Principal Values)

| Function | Domain | Range |
|----------|--------|-------|
| arcsin x | [−1, 1] | [−π/2, π/2] |
| arccos x | [−1, 1] | [0, π] |
| arctan x | ℝ | (−π/2, π/2) |
| arccot x | ℝ | (0, π) |
| arcsec x | (−∞, −1] ∪ [1, ∞) | [0, π] − {π/2} |
| arccosec x | (−∞, −1] ∪ [1, ∞) | [−π/2, π/2] − {0} |

---

## Stage 3: Type-wise Mastery

### Type 1: Finding Principal Values

**Goal:** Find the principal value of a given inverse trig function.

**Solved Example:**

Find the principal value of sin⁻¹(1/2).

**Solution:**
```
sin⁻¹(1/2) = π/6   (Since sin π/6 = 1/2 and π/6 ∈ [−π/2, π/2])
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Find cos⁻¹(√3/2).
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(\frac{\sqrt{3}}{2}\right) \).
By definition, \( \cos\theta = \frac{\sqrt{3}}{2} \).
Since the range of the principal value branch of \( \cos^{-1}x \) is \( [0, \pi] \), we look for \( \theta \in [0, \pi] \) such that \( \cos\theta = \frac{\sqrt{3}}{2} \).
Since \( \cos\left(\frac{\pi}{6}\right) = \frac{\sqrt{3}}{2} \), we have:
\[ \cos^{-1}\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{6} \]

</details>

2. 🟢 Find tan⁻¹(1).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}(1) \).
By definition, \( \tan\theta = 1 \).
Since the range of the principal value branch of \( \tan^{-1}x \) is \( \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), we look for \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \) such that \( \tan\theta = 1 \).
Since \( \tan\left(\frac{\pi}{4}\right) = 1 \), we have:
\[ \tan^{-1}(1) = \frac{\pi}{4} \]

</details>

3. 🟢 Find sin⁻¹(−1/2).
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(-\frac{1}{2}\right) \).
By definition, \( \sin\theta = -\frac{1}{2} \).
Since the range of the principal value branch of \( \sin^{-1}x \) is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we look for \( \theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \) such that \( \sin\theta = -\frac{1}{2} \).
Since \( \sin\left(-\frac{\pi}{6}\right) = -\frac{1}{2} \), we have:
\[ \sin^{-1}\left(-\frac{1}{2}\right) = -\frac{\pi}{6} \]

</details>

4. 🟡 Find sec⁻¹(2).
<details>
<summary>Solution</summary>

Let \( \theta = \sec^{-1}(2) \).
By definition, \( \sec\theta = 2 \), which is equivalent to \( \cos\theta = \frac{1}{2} \).
Since the range of the principal value branch of \( \sec^{-1}x \) is \( [0, \pi] \setminus \left\{\frac{\pi}{2}\right\} \), we look for \( \theta \in [0, \pi] \setminus \left\{\frac{\pi}{2}\right\} \) such that \( \cos\theta = \frac{1}{2} \).
Since \( \cos\left(\frac{\pi}{3}\right) = \frac{1}{2} \), we have:
\[ \sec^{-1}(2) = \frac{\pi}{3} \]

</details>

5. 🟡 Find arccot(1/√3).
<details>
<summary>Solution</summary>

Let \( \theta = \cot^{-1}\left(\frac{1}{\sqrt{3}}\right) \).
By definition, \( \cot\theta = \frac{1}{\sqrt{3}} \).
Since the range of the principal value branch of \( \cot^{-1}x \) is \( (0, \pi) \), we look for \( \theta \in (0, \pi) \) such that \( \cot\theta = \frac{1}{\sqrt{3}} \).
Since \( \cot\left(\frac{\pi}{3}\right) = \frac{1}{\sqrt{3}} \), we have:
\[ \cot^{-1}\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{3} \]

</details>

---

### Type 2: Simplifying sin(arcsin x) and arcsin(sin x)

**Goal:** Understand composition of inverse and regular trig functions.

**Key rules:**
```
sin(arcsin x) = x for x ∈ [−1, 1]
arcsin(sin x) = x only when x ∈ [−π/2, π/2]
```
For x outside this range, arcsin(sin x) = the angle in [−π/2, π/2] with the same sine.

**Solved Example:**

Find arcsin(sin(5π/6)).

**Solution:**
```
5π/6 is not in [−π/2, π/2].
sin(5π/6) = 1/2
arcsin(1/2) = π/6 (in [−π/2, π/2])
∴ arcsin(sin(5π/6)) = π/6
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Find arcsin(sin(π/4)).
<details>
<summary>Solution</summary>

The formula \( \sin^{-1}(\sin x) = x \) holds if \( x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \).
Since \( \frac{\pi}{4} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we have:
\[ \sin^{-1}\left(\sin\left(\frac{\pi}{4}\right)\right) = \frac{\pi}{4} \]

</details>

7. 🟡 Find arccos(cos(5π/4)).
<details>
<summary>Solution</summary>

The formula \( \cos^{-1}(\cos x) = x \) holds if \( x \in [0, \pi] \).
Since \( \frac{5\pi}{4} \notin [0, \pi] \), we rewrite \( \cos\left(\frac{5\pi}{4}\right) \) using \( \cos(2\pi - \theta) = \cos\theta \):
\[ \cos\left(\frac{5\pi}{4}\right) = \cos\left(2\pi - \frac{5\pi}{4}\right) = \cos\left(\frac{3\pi}{4}\right) \]
Since \( \frac{3\pi}{4} \in [0, \pi] \), we have:
\[ \cos^{-1}\left(\cos\left(\frac{5\pi}{4}\right)\right) = \cos^{-1}\left(\cos\left(\frac{3\pi}{4}\right)\right) = \frac{3\pi}{4} \]

</details>

8. 🟡 Find arctan(tan(5π/6)).
<details>
<summary>Solution</summary>

The formula \( \tan^{-1}(\tan x) = x \) holds if \( x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \).
Since \( \frac{5\pi}{6} \notin \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), we rewrite \( \tan\left(\frac{5\pi}{6}\right) \) using \( \tan(\theta) = \tan(\theta - \pi) \):
\[ \tan\left(\frac{5\pi}{6}\right) = \tan\left(\frac{5\pi}{6} - \pi\right) = \tan\left(-\frac{\pi}{6}\right) \]
Since \( -\frac{\pi}{6} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), we have:
\[ \tan^{-1}\left(\tan\left(\frac{5\pi}{6}\right)\right) = \tan^{-1}\left(\tan\left(-\frac{\pi}{6}\right)\right) = -\frac{\pi}{6} \]

</details>

9. 🟡 Find sin⁻¹(sin(3π/4)).
<details>
<summary>Solution</summary>

The formula \( \sin^{-1}(\sin x) = x \) holds if \( x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \).
Since \( \frac{3\pi}{4} \notin \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we rewrite \( \sin\left(\frac{3\pi}{4}\right) \) using \( \sin\theta = \sin(\pi - \theta) \):
\[ \sin\left(\frac{3\pi}{4}\right) = \sin\left(\pi - \frac{3\pi}{4}\right) = \sin\left(\frac{\pi}{4}\right) \]
Since \( \frac{\pi}{4} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we have:
\[ \sin^{-1}\left(\sin\left(\frac{3\pi}{4}\right)\right) = \sin^{-1}\left(\sin\left(\frac{\pi}{4}\right)\right) = \frac{\pi}{4} \]

</details>

10. 🔴 Find cos⁻¹(cos(7π/6)).
<details>
<summary>Solution</summary>

The formula \( \cos^{-1}(\cos x) = x \) holds if \( x \in [0, \pi] \).
Since \( \frac{7\pi}{6} \notin [0, \pi] \), we rewrite \( \cos\left(\frac{7\pi}{6}\right) \) using \( \cos\theta = \cos(2\pi - \theta) \):
\[ \cos\left(\frac{7\pi}{6}\right) = \cos\left(2\pi - \frac{7\pi}{6}\right) = \cos\left(\frac{5\pi}{6}\right) \]
Since \( \frac{5\pi}{6} \in [0, \pi] \), we have:
\[ \cos^{-1}\left(\cos\left(\frac{7\pi}{6}\right)\right) = \cos^{-1}\left(\cos\left(\frac{5\pi}{6}\right)\right) = \frac{5\pi}{6} \]

</details>

---

### Type 3: Evaluating sin⁻¹(cos θ) Type Expressions

**Goal:** Simplify expressions where one trig function's output goes to another's inverse.

**Solved Example:**

Find sin⁻¹(cos 40°).

**Solution:**
```
cos 40° = sin 50° (using cos θ = sin(90° − θ))
sin⁻¹(sin 50°) = 50° (since 50° ∈ [−90°, 90°])
∴ sin⁻¹(cos 40°) = 50°
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Find cos⁻¹(sin 30°).
<details>
<summary>Solution</summary>

We know that \( \sin 30^\circ = \cos(90^\circ - 30^\circ) = \cos 60^\circ \).
Therefore:
\[ \cos^{-1}(\sin 30^\circ) = \cos^{-1}(\cos 60^\circ) \]
Since \( 60^\circ \in [0^\circ, 180^\circ] \) (the principal range of \( \cos^{-1}x \)):
\[ \cos^{-1}(\cos 60^\circ) = 60^\circ \text{ (or } \frac{\pi}{3}\text{)} \]

</details>

12. 🟡 Find tan⁻¹(cot 20°).
<details>
<summary>Solution</summary>

We know that \( \cot 20^\circ = \tan(90^\circ - 20^\circ) = \tan 70^\circ \).
Therefore:
\[ \tan^{-1}(\cot 20^\circ) = \tan^{-1}(\tan 70^\circ) \]
Since \( 70^\circ \in (-90^\circ, 90^\circ) \) (the principal range of \( \tan^{-1} \)):
\[ \tan^{-1}(\tan 70^\circ) = 70^\circ \text{ (or } \frac{7\pi}{18}\text{)} \]

</details>

13. 🟡 Find sin⁻¹(cos 100°).
<details>
<summary>Solution</summary>

We know that \( \cos 100^\circ = \sin(90^\circ - 100^\circ) = \sin(-10^\circ) \).
Therefore:
\[ \sin^{-1}(\cos 100^\circ) = \sin^{-1}(\sin(-10^\circ)) \]
Since \( -10^\circ \in [-90^\circ, 90^\circ] \) (the principal range of \( \sin^{-1}x \)):
\[ \sin^{-1}(\sin(-10^\circ)) = -10^\circ \text{ (or } -\frac{\pi}{18}\text{)} \]

</details>

14. 🟡 Find arcsin(cos(−60°)).
<details>
<summary>Solution</summary>

Since \( \cos(-\theta) = \cos\theta \), we have \( \cos(-60^\circ) = \cos 60^\circ \).
We know that \( \cos 60^\circ = \sin(90^\circ - 60^\circ) = \sin 30^\circ \).
Therefore:
\[ \sin^{-1}(\cos(-60^\circ)) = \sin^{-1}(\sin 30^\circ) \]
Since \( 30^\circ \in [-90^\circ, 90^\circ] \):
\[ \sin^{-1}(\sin 30^\circ) = 30^\circ \text{ (or } \frac{\pi}{6}\text{)} \]

</details>

15. 🔴 ⭐ Find arctan(cot 130°).
<details>
<summary>Solution</summary>

We know that \( \cot 130^\circ = \tan(90^\circ - 130^\circ) = \tan(-40^\circ) \).
Therefore:
\[ \tan^{-1}(\cot 130^\circ) = \tan^{-1}(\tan(-40^\circ)) \]
Since \( -40^\circ \in (-90^\circ, 90^\circ) \):
\[ \tan^{-1}(\tan(-40^\circ)) = -40^\circ \text{ (or } -\frac{2\pi}{9}\text{)} \]

</details>

---

### Type 4: Proving Identities with Inverse Trig

**Goal:** Prove relationships between inverse trig functions.

**Solved Example:**

Prove that sin⁻¹x + cos⁻¹x = π/2 for all x ∈ [−1, 1].

**Solution:**
```
Let sin⁻¹x = θ → x = sin θ, θ ∈ [−π/2, π/2]
Then cos θ = √(1 − x²) (positive since θ ∈ [−π/2, π/2])
θ = cos⁻¹(√(1 − x²))... 

Better: Let sin⁻¹x = A, cos⁻¹x = B
sin A = x, cos B = x
sin A = cos B
sin A = sin(π/2 − B)
A = π/2 − B (since A, π/2−B are in [−π/2, π/2])
A + B = π/2 ✓
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Prove that tan⁻¹x + cot⁻¹x = π/2.
<details>
<summary>Solution</summary>

Let \( \tan^{-1}x = \theta \).
Then \( x = \tan\theta \), where \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \).
We know that \( \tan\theta = \cot\left(\frac{\pi}{2} - \theta\right) \), so:
\[ x = \cot\left(\frac{\pi}{2} - \theta\right) \]
Since \( -\frac{\pi}{2} < \theta < \frac{\pi}{2} \), we have:
\[ -\frac{\pi}{2} < -\theta < \frac{\pi}{2} \implies 0 < \frac{\pi}{2} - \theta < \pi \]
Since \( \frac{\pi}{2} - \theta \in (0, \pi) \), which is the range of the principal branch of \( \cot^{-1} \), taking \( \cot^{-1} \) on both sides gives:
\[ \cot^{-1}x = \frac{\pi}{2} - \theta \]
Substitute \( \theta = \tan^{-1}x \):
\[ \cot^{-1}x = \frac{\pi}{2} - \tan^{-1}x \implies \tan^{-1}x + \cot^{-1}x = \frac{\pi}{2} \]
Hence proved.

</details>

17. 🟡 Prove that sec⁻¹x + cosec⁻¹x = π/2.
<details>
<summary>Solution</summary>

Let \( \sec^{-1}x = \theta \).
Then \( x = \sec\theta \), where \( \theta \in [0, \pi] \setminus \left\{\frac{\pi}{2}\right\} \).
We know that \( \sec\theta = \csc\left(\frac{\pi}{2} - \theta\right) \), so:
\[ x = \csc\left(\frac{\pi}{2} - \theta\right) \]
Since \( \theta \in [0, \pi] \setminus \left\{\frac{\pi}{2}\right\} \):
\[ 0 \le \theta \le \pi \text{ and } \theta \neq \frac{\pi}{2} \implies -\frac{\pi}{2} \le \frac{\pi}{2} - \theta \le \frac{\pi}{2} \text{ and } \frac{\pi}{2} - \theta \neq 0 \]
Thus, \( \frac{\pi}{2} - \theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \setminus \{0\} \), which is the range of the principal branch of \( \csc^{-1} \).
Taking \( \csc^{-1} \) on both sides gives:
\[ \csc^{-1}x = \frac{\pi}{2} - \theta \]
Substitute \( \theta = \sec^{-1}x \):
\[ \csc^{-1}x = \frac{\pi}{2} - \sec^{-1}x \implies \sec^{-1}x + \csc^{-1}x = \frac{\pi}{2} \]
Hence proved.

</details>

18. 🟡 Prove that arctan(1) + arctan(2) + arctan(3) = π.
<details>
<summary>Solution</summary>

We know that \( \tan^{-1}(1) = \frac{\pi}{4} \).
To evaluate \( \tan^{-1}(2) + \tan^{-1}(3) \), we use the identity for \( xy > 1 \) and \( x, y > 0 \):
\[ \tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\frac{x+y}{1-xy}\right) \]
Since \( 2 \times 3 = 6 > 1 \):
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\frac{2+3}{1 - 6}\right) = \pi + \tan^{-1}(-1) \]
Since \( \tan^{-1}(-1) = -\frac{\pi}{4} \):
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \]
Therefore:
\[ \tan^{-1}(1) + \tan^{-1}(2) + \tan^{-1}(3) = \frac{\pi}{4} + \frac{3\pi}{4} = \pi \]
Hence proved.

</details>

19. 🔴 ⭐ Prove that 2 arctan(1/3) + arctan(1/7) = π/4.
<details>
<summary>Solution</summary>

First, simplify \( 2\tan^{-1}\left(\frac{1}{3}\right) \) using the identity \( 2\tan^{-1}x = \tan^{-1}\left(\frac{2x}{1-x^2}\right) \) for \( |x| < 1 \):
\[ 2\tan^{-1}\left(\frac{1}{3}\right) = \tan^{-1}\left(\frac{2/3}{1 - 1/9}\right) = \tan^{-1}\left(\frac{2/3}{8/9}\right) = \tan^{-1}\left(\frac{3}{4}\right) \]
Now, add \( \tan^{-1}\left(\frac{1}{7}\right) \) using the identity \( \tan^{-1}x + \tan^{-1}y = \tan^{-1}\left(\frac{x+y}{1-xy}\right) \) for \( xy < 1 \):
Since \( \frac{3}{4} \times \frac{1}{7} = \frac{3}{28} < 1 \):
\[ \tan^{-1}\left(\frac{3}{4}\right) + \tan^{-1}\left(\frac{1}{7}\right) = \tan^{-1}\left(\frac{3/4 + 1/7}{1 - 3/28}\right) = \tan^{-1}\left(\frac{25/28}{25/28}\right) = \tan^{-1}(1) = \frac{\pi}{4} \]
Therefore:
\[ 2\tan^{-1}\left(\frac{1}{3}\right) + \tan^{-1}\left(\frac{1}{7}\right) = \frac{\pi}{4} \]
Hence proved.

</details>

20. 🔴 Prove that arctan(1/3) + arctan(1/5) + arctan(1/7) + arctan(1/8) = π/4.
<details>
<summary>Solution</summary>

We can group the terms as follows:
\[ \text{LHS} = \left[\tan^{-1}\left(\frac{1}{3}\right) + \tan^{-1}\left(\frac{1}{5}\right)\right] + \left[\tan^{-1}\left(\frac{1}{7}\right) + \tan^{-1}\left(\frac{1}{8}\right)\right] \]
1. Evaluate the first group: since \( \frac{1}{3} \times \frac{1}{5} = \frac{1}{15} < 1 \):
   \[ \tan^{-1}\left(\frac{1}{3}\right) + \tan^{-1}\left(\frac{1}{5}\right) = \tan^{-1}\left(\frac{1/3 + 1/5}{1 - 1/15}\right) = \tan^{-1}\left(\frac{8/15}{14/15}\right) = \tan^{-1}\left(\frac{4}{7}\right) \]
2. Evaluate the second group: since \( \frac{1}{7} \times \frac{1}{8} = \frac{1}{56} < 1 \):
   \[ \tan^{-1}\left(\frac{1}{7}\right) + \tan^{-1}\left(\frac{1}{8}\right) = \tan^{-1}\left(\frac{1/7 + 1/8}{1 - 1/56}\right) = \tan^{-1}\left(\frac{15/56}{55/56}\right) = \tan^{-1}\left(\frac{3}{11}\right) \]
3. Add the two groups: since \( \frac{4}{7} \times \frac{3}{11} = \frac{12}{77} < 1 \):
   \[ \tan^{-1}\left(\frac{4}{7}\right) + \tan^{-1}\left(\frac{3}{11}\right) = \tan^{-1}\left(\frac{4/7 + 3/11}{1 - 12/77}\right) = \tan^{-1}\left(\frac{65/77}{65/77}\right) = \tan^{-1}(1) = \frac{\pi}{4} \]
Therefore, LHS = \( \frac{\pi}{4} \).
Hence proved.

</details>

---

### Type 5: Writing as Sum/Difference of Inverse Functions

**Goal:** Simplify expressions like tan⁻¹(a) ± tan⁻¹(b).

**Formula:**
```
tan⁻¹x + tan⁻¹y = tan⁻¹((x + y)/(1 − xy))  if xy < 1
tan⁻¹x − tan⁻¹y = tan⁻¹((x − y)/(1 + xy))
```

**Solved Example:**

Prove that tan⁻¹(1/2) + tan⁻¹(1/3) = π/4.

**Solution:**
```
tan⁻¹(1/2) + tan⁻¹(1/3) = tan⁻¹((1/2 + 1/3)/(1 − 1/6))
= tan⁻¹((5/6)/(5/6))
= tan⁻¹(1)
= π/4 ✓
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Evaluate tan⁻¹(1/5) + tan⁻¹(3/5).
<details>
<summary>Solution</summary>

Since the product of the arguments is \( \frac{1}{5} \times \frac{3}{5} = \frac{3}{25} < 1 \), we apply the direct formula:
\[ \tan^{-1}\left(\frac{1}{5}\right) + \tan^{-1}\left(\frac{3}{5}\right) = \tan^{-1}\left(\frac{1/5 + 3/5}{1 - 3/25}\right) = \tan^{-1}\left(\frac{4/5}{22/25}\right) \]
Simplify the fraction inside the argument:
\[ \frac{4}{5} \times \frac{25}{22} = \frac{20}{22} = \frac{10}{11} \]
Therefore:
\[ \tan^{-1}\left(\frac{1}{5}\right) + \tan^{-1}\left(\frac{3}{5}\right) = \tan^{-1}\left(\frac{10}{11}\right) \]

</details>

22. 🟡 Evaluate tan⁻¹(2) + tan⁻¹(3).
<details>
<summary>Solution</summary>

Since \( x = 2 > 0 \), \( y = 3 > 0 \), and \( xy = 6 > 1 \), we use the formula:
\[ \tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\frac{x+y}{1-xy}\right) \]
Substitute the values:
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\frac{2+3}{1-6}\right) = \pi + \tan^{-1}(-1) \]
Since \( \tan^{-1}(-1) = -\frac{\pi}{4} \):
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \]

</details>

23. 🟡 Evaluate sin⁻¹(3/5) + cos⁻¹(4/5).
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(\frac{4}{5}\right) \implies \cos\theta = \frac{4}{5} \).
Since \( \theta \in [0, \pi] \), \( \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \frac{16}{25}} = \frac{3}{5} \).
Since \( \sin\theta > 0 \), \( \theta \in \left[0, \frac{\pi}{2}\right] \), which means \( \theta = \sin^{-1}\left(\frac{3}{5}\right) \).
Thus, we have:
\[ \cos^{-1}\left(\frac{4}{5}\right) = \sin^{-1}\left(\frac{3}{5}\right) \]
Therefore, the expression becomes:
\[ \sin^{-1}\left(\frac{3}{5}\right) + \cos^{-1}\left(\frac{4}{5}\right) = 2\sin^{-1}\left(\frac{3}{5}\right) \]
To write this as a single inverse function, let \( A = \sin^{-1}\left(\frac{3}{5}\right) \implies \sin A = 3/5, \cos A = 4/5 \).
Using the double angle identity:
\[ \sin(2A) = 2\sin A\cos A = 2\left(\frac{3}{5}\right)\left(\frac{4}{5}\right) = \frac{24}{25} \]
Since \( A < \frac{\pi}{4} \) (as \( \sin A = 0.6 < \frac{1}{\sqrt{2}} \approx 0.707 \)), \( 2A < \frac{\pi}{2} \).
Therefore:
\[ 2\sin^{-1}\left(\frac{3}{5}\right) = \sin^{-1}\left(\frac{24}{25}\right) \]

</details>

24. 🔴 ⭐ Prove that tan⁻¹(1/7) + tan⁻¹(1/13) = tan⁻¹(2/9).
<details>
<summary>Solution</summary>

Since the product of the arguments is \( \frac{1}{7} \times \frac{1}{13} = \frac{1}{91} < 1 \), we use the sum formula:
\[ \tan^{-1}\left(\frac{1}{7}\right) + \tan^{-1}\left(\frac{1}{13}\right) = \tan^{-1}\left(\frac{1/7 + 1/13}{1 - 1/91}\right) = \tan^{-1}\left(\frac{20/91}{90/91}\right) = \tan^{-1}\left(\frac{2}{9}\right) \]
Hence proved.

</details>

25. 🔴 Find the value of sin⁻¹(5/13) + sin⁻¹(12/13).
<details>
<summary>Solution</summary>

Let \( A = \sin^{-1}\left(\frac{5}{13}\right) \implies \sin A = \frac{5}{13} \) with \( A \in \left[0, \frac{\pi}{2}\right] \).
Let \( B = \sin^{-1}\left(\frac{12}{13}\right) \implies \sin B = \frac{12}{13} \) with \( B \in \left[0, \frac{\pi}{2}\right] \).
Since \( A \) is acute, we have:
\[ \cos A = \sqrt{1 - \sin^2 A} = \sqrt{1 - \frac{25}{169}} = \frac{12}{13} \]
Notice that \( \cos A = \sin B \).
Using the complementary relation \( \cos A = \sin\left(\frac{\pi}{2} - A\right) \):
\[ \sin B = \sin\left(\frac{\pi}{2} - A\right) \]
Since both \( B \) and \( \frac{\pi}{2} - A \) are in \( \left[0, \frac{\pi}{2}\right] \):
\[ B = \frac{\pi}{2} - A \implies A + B = \frac{\pi}{2} \]
Thus:
\[ \sin^{-1}\left(\frac{5}{13}\right) + \sin^{-1}\left(\frac{12}{13}\right) = \frac{\pi}{2} \]

</details>

---

### Type 6: Solving Equations with Inverse Trig

**Goal:** Solve equations involving inverse trig functions.

**Solved Example:**

Solve tan⁻¹x + tan⁻¹(2x) = π/4.

**Solution:**
```
tan⁻¹x + tan⁻¹(2x) = π/4
tan⁻¹((x + 2x)/(1 − 2x²)) = π/4
3x/(1 − 2x²) = 1
3x = 1 − 2x²
2x² + 3x − 1 = 0
x = (−3 ± √17)/4

Check domain: x > 0 (since sum is positive)
x = (−3 + √17)/4 ≈ 0.28
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 Solve tan⁻¹(2x) + tan⁻¹(3x) = π/4.
<details>
<summary>Solution</summary>

Assuming \( 2x \times 3x < 1 \implies 6x^2 < 1 \), we apply the sum formula:
\[ \tan^{-1}\left(\frac{2x + 3x}{1 - 6x^2}\right) = \frac{\pi}{4} \]
Taking tangent of both sides:
\[ \frac{5x}{1 - 6x^2} = \tan\left(\frac{\pi}{4}\right) = 1 \]
\[ 5x = 1 - 6x^2 \implies 6x^2 + 5x - 1 = 0 \]
Factoring the quadratic:
\[ (6x - 1)(x + 1) = 0 \implies x = \frac{1}{6} \text{ or } x = -1 \]
Check the solutions:
- If \( x = -1 \): the LHS is \( \tan^{-1}(-2) + \tan^{-1}(-3) < 0 \), which cannot equal \( \frac{\pi}{4} \). So \( x = -1 \) is extraneous.
- If \( x = \frac{1}{6} \): \( 6(1/6)^2 = 1/6 < 1 \), and \( \tan^{-1}(1/3) + \tan^{-1}(1/2) > 0 \), which is valid.
Thus, the only solution is \( x = \frac{1}{6} \).

</details>

27. 🔴 Solve cos⁻¹x + sin⁻¹(1/2) = π.
<details>
<summary>Solution</summary>

We know that \( \sin^{-1}\left(\frac{1}{2}\right) = \frac{\pi}{6} \).
Substitute this value into the equation:
\[ \cos^{-1}x + \frac{\pi}{6} = \pi \implies \cos^{-1}x = \pi - \frac{\pi}{6} = \frac{5\pi}{6} \]
Taking cosine of both sides:
\[ x = \cos\left(\frac{5\pi}{6}\right) = -\frac{\sqrt{3}}{2} \]
Since \( -\frac{\sqrt{3}}{2} \in [-1, 1] \), this is a valid solution.
Thus, \( x = -\frac{\sqrt{3}}{2} \).

</details>

28. 🔴 Solve sin⁻¹x + sin⁻¹(1−x) = cos⁻¹x.
<details>
<summary>Solution</summary>

Using the identity \( \cos^{-1}x = \frac{\pi}{2} - \sin^{-1}x \), we can rewrite the equation as:
\[ \sin^{-1}x + \sin^{-1}(1-x) = \frac{\pi}{2} - \sin^{-1}x \]
\[ \sin^{-1}(1-x) = \frac{\pi}{2} - 2\sin^{-1}x \]
Taking sine of both sides:
\[ 1 - x = \sin\left(\frac{\pi}{2} - 2\sin^{-1}x\right) \]
Using the identity \( \sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta \):
\[ 1 - x = \cos(2\sin^{-1}x) \]
Using the double angle identity \( \cos(2\theta) = 1 - 2\sin^2\theta \):
\[ 1 - x = 1 - 2x^2 \implies 2x^2 - x = 0 \implies x(2x - 1) = 0 \]
This gives \( x = 0 \) or \( x = \frac{1}{2} \).
Checking the solutions in the original equation:
- If \( x = 0 \):
  LHS: \( \sin^{-1}(0) + \sin^{-1}(1) = 0 + \frac{\pi}{2} = \frac{\pi}{2} \).
  RHS: \( \cos^{-1}(0) = \frac{\pi}{2} \).
  LHS = RHS (Valid).
- If \( x = \frac{1}{2} \):
  LHS: \( \sin^{-1}(1/2) + \sin^{-1}(1/2) = \frac{\pi}{6} + \frac{\pi}{6} = \frac{\pi}{3} \).
  RHS: \( \cos^{-1}(1/2) = \frac{\pi}{3} \).
  LHS = RHS (Valid).
Thus, the solutions are \( x = 0, \frac{1}{2} \).

</details>

29. 🔴 ⭐ Solve tan⁻¹(x − 1) + tan⁻¹x + tan⁻¹(x + 1) = tan⁻¹(3x).
<details>
<summary>Solution</summary>

Rearrange the terms:
\[ \tan^{-1}(x - 1) + \tan^{-1}(x + 1) = \tan^{-1}(3x) - \tan^{-1}x \]
Apply the tangent addition and subtraction formulas:
- LHS:
  \[ \tan^{-1}(x - 1) + \tan^{-1}(x + 1) = \tan^{-1}\left(\frac{(x-1) + (x+1)}{1 - (x-1)(x+1)}\right) = \tan^{-1}\left(\frac{2x}{1 - (x^2 - 1)}\right) = \tan^{-1}\left(\frac{2x}{2 - x^2}\right) \]
- RHS:
  \[ \tan^{-1}(3x) - \tan^{-1}x = \tan^{-1}\left(\frac{3x - x}{1 + 3x^2}\right) = \tan^{-1}\left(\frac{2x}{1 + 3x^2}\right) \]
Equating the arguments:
\[ \frac{2x}{2 - x^2} = \frac{2x}{1 + 3x^2} \]
This yields two cases:
1. \( 2x = 0 \implies x = 0 \).
   Checking \( x = 0 \) in the original equation:
   \[ \tan^{-1}(-1) + \tan^{-1}(0) + \tan^{-1}(1) = -\frac{\pi}{4} + 0 + \frac{\pi}{4} = 0 = \tan^{-1}(0) \quad (\text{Valid}) \]
2. \( 2x \neq 0 \): dividing both sides by \( 2x \):
   \[ 2 - x^2 = 1 + 3x^2 \implies 4x^2 = 1 \implies x = \pm\frac{1}{2} \]
   Checking \( x = \pm\frac{1}{2} \) in the original equation:
   - For \( x = \frac{1}{2} \):
     LHS: \( \tan^{-1}(-1/2) + \tan^{-1}(1/2) + \tan^{-1}(3/2) = \tan^{-1}(3/2) \) (since \( \tan^{-1}(-u) = -\tan^{-1}u \)).
     RHS: \( \tan^{-1}(3/2) \).
     LHS = RHS (Valid).
   - For \( x = -\frac{1}{2} \):
     LHS: \( \tan^{-1}(-3/2) + \tan^{-1}(-1/2) + \tan^{-1}(1/2) = \tan^{-1}(-3/2) \).
     RHS: \( \tan^{-1}(-3/2) \).
     LHS = RHS (Valid).
Thus, the solutions are \( x = 0, \frac{1}{2}, -\frac{1}{2} \).

</details>

30. 🔴 Solve sin⁻¹(1 − x) − 2 sin⁻¹x = π/2.
<details>
<summary>Solution</summary>

Let \( \sin^{-1}x = \theta \implies x = \sin\theta \).
The equation becomes:
\[ \sin^{-1}(1 - \sin\theta) - 2\theta = \frac{\pi}{2} \implies \sin^{-1}(1 - \sin\theta) = \frac{\pi}{2} + 2\theta \]
Taking sine of both sides:
\[ 1 - \sin\theta = \sin\left(\frac{\pi}{2} + 2\theta\right) \]
Using \( \sin\left(\frac{\pi}{2} + \alpha\right) = \cos\alpha \):
\[ 1 - \sin\theta = \cos(2\theta) \]
Express \( \cos(2\theta) \) as \( 1 - 2\sin^2\theta \):
\[ 1 - \sin\theta = 1 - 2\sin^2\theta \implies 2\sin^2\theta - \sin\theta = 0 \implies \sin\theta(2\sin\theta - 1) = 0 \]
Since \( x = \sin\theta \):
\[ x(2x - 1) = 0 \implies x = 0 \text{ or } x = \frac{1}{2} \]
Let's check the solutions in the original equation:
- If \( x = 0 \):
  LHS: \( \sin^{-1}(1) - 2\sin^{-1}(0) = \frac{\pi}{2} - 0 = \frac{\pi}{2} = \text{RHS} \) (Valid).
- If \( x = \frac{1}{2} \):
  LHS: \( \sin^{-1}(1/2) - 2\sin^{-1}(1/2) = -\sin^{-1}(1/2) = -\frac{\pi}{6} \neq \frac{\pi}{2} \) (Extraneous).
Thus, the only solution is \( x = 0 \).

</details>

---

### Type 7: Simplifying sin(cos⁻¹x) etc.

**Goal:** Evaluate expressions like sin(cos⁻¹x), cos(tan⁻¹x), etc.

**Key idea:** Draw a right triangle.

**Solved Example:**

Find sin(cos⁻¹(3/5)).

**Solution:**
```
Let θ = cos⁻¹(3/5) → cos θ = 3/5, θ ∈ [0, π]
So adj = 3, hyp = 5 → opp = 4
sin θ = 4/5
∴ sin(cos⁻¹(3/5)) = 4/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

31. 🟡 Find cos(tan⁻¹(4/3)).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}\left(\frac{4}{3}\right) \implies \tan\theta = \frac{4}{3} \).
Since \( \tan\theta > 0 \) and \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), we have \( \theta \in \left(0, \frac{\pi}{2}\right) \).
Consider a right triangle with opposite side \( 4 \) and adjacent side \( 3 \).
The hypotenuse is \( \sqrt{3^2 + 4^2} = 5 \).
Therefore:
\[ \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{3}{5} \]
So, \( \cos(\tan^{-1}(4/3)) = \frac{3}{5} \).

</details>

32. 🟡 Find tan(sin⁻¹(12/13)).
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(\frac{12}{13}\right) \implies \sin\theta = \frac{12}{13} \).
Since \( \sin\theta > 0 \), we have \( \theta \in \left(0, \frac{\pi}{2}\right) \).
Consider a right triangle with opposite side \( 12 \) and hypotenuse \( 13 \).
The adjacent side is \( \sqrt{13^2 - 12^2} = 5 \).
Therefore:
\[ \tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{12}{5} \]
So, \( \tan(\sin^{-1}(12/13)) = \frac{12}{5} \).

</details>

33. 🟡 Find sec(tan⁻¹(2)).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}(2) \implies \tan\theta = 2 \).
Since \( \tan\theta > 0 \), we have \( \theta \in \left(0, \frac{\pi}{2}\right) \).
We use the trigonometric identity \( \sec^2\theta = 1 + \tan^2\theta \):
\[ \sec^2\theta = 1 + 2^2 = 5 \]
Since \( \theta \in \left(0, \frac{\pi}{2}\right) \), \( \sec\theta \) must be positive:
\[ \sec\theta = \sqrt{5} \]
So, \( \sec(\tan^{-1}(2)) = \sqrt{5} \).

</details>

34. 🟡 Find sin(cos⁻¹(5/13)).
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(\frac{5}{13}\right) \implies \cos\theta = \frac{5}{13} \).
Since \( \cos\theta > 0 \), we have \( \theta \in \left(0, \frac{\pi}{2}\right) \).
Consider a right triangle with adjacent side \( 5 \) and hypotenuse \( 13 \).
The opposite side is \( \sqrt{13^2 - 5^2} = 12 \).
Therefore:
\[ \sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{12}{13} \]
So, \( \sin(\cos^{-1}(5/13)) = \frac{12}{13} \).

</details>

35. 🔴 ⭐ Simplify sin(arctan x) in terms of x.
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}x \implies \tan\theta = x \), where \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \).
We can express \( \sin\theta \) in terms of \( \tan\theta \):
\[ \sin\theta = \frac{\tan\theta}{\sec\theta} = \frac{\tan\theta}{\sqrt{1 + \tan^2\theta}} \]
Since \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), the cosine (and thus secant) of \( \theta \) is positive. Therefore, we choose the positive sign for the square root:
\[ \sin\theta = \frac{\tan\theta}{\sqrt{1 + \tan^2\theta}} = \frac{x}{\sqrt{1 + x^2}} \]
So, \( \sin(\tan^{-1}x) = \frac{x}{\sqrt{1 + x^2}} \).

</details>

---

### Type 8: Simplifying Nested Inverse Expressions

**Goal:** Simplify expressions like sin(2 tan⁻¹x), cos(2 sin⁻¹x), etc.

**Solved Example:**

Simplify sin(2 tan⁻¹x).

**Solution:**
```
Let θ = tan⁻¹x → tan θ = x
sin 2θ = 2 tan θ/(1 + tan²θ) = 2x/(1 + x²)
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Simplify cos(2 tan⁻¹x).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}x \implies \tan\theta = x \).
We need to simplify \( \cos(2\theta) \). Using the identity for cosine of a double angle in terms of tangent:
\[ \cos(2\theta) = \frac{1 - \tan^2\theta}{1 + \tan^2\theta} \]
Substitute \( \tan\theta = x \):
\[ \cos(2\tan^{-1}x) = \frac{1 - x^2}{1 + x^2} \]

</details>

37. 🟡 Simplify tan(2 sin⁻¹x).
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}x \implies \sin\theta = x \), where \( \theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \).
We need to simplify \( \tan(2\theta) \). Using the identity:
\[ \tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta} \]
Since \( \sin\theta = x \), we have \( \cos\theta = \sqrt{1 - x^2} \) (positive since \( \theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \)).
Thus, \( \tan\theta = \frac{x}{\sqrt{1 - x^2}} \).
Substitute this into the identity:
\[ \tan(2\theta) = \frac{2\left(\frac{x}{\sqrt{1 - x^2}}\right)}{1 - \frac{x^2}{1 - x^2}} = \frac{\frac{2x}{\sqrt{1 - x^2}}}{\frac{1 - 2x^2}{1 - x^2}} = \frac{2x\sqrt{1 - x^2}}{1 - 2x^2} \]
So, \( \tan(2\sin^{-1}x) = \frac{2x\sqrt{1 - x^2}}{1 - 2x^2} \).

</details>

38. 🟡 Simplify sin(2 cos⁻¹x).
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}x \implies \cos\theta = x \), where \( \theta \in [0, \pi] \).
We need to simplify \( \sin(2\theta) \). Using the double angle formula:
\[ \sin(2\theta) = 2\sin\theta\cos\theta \]
Since \( \theta \in [0, \pi] \), \( \sin\theta \) is non-negative:
\[ \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - x^2} \]
Therefore:
\[ \sin(2\cos^{-1}x) = 2x\sqrt{1 - x^2} \]

</details>

39. 🔴 ⭐ Simplify tan(2 tan⁻¹(1/3)).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}\left(\frac{1}{3}\right) \implies \tan\theta = \frac{1}{3} \).
We need to evaluate \( \tan(2\theta) \). Using the double angle formula:
\[ \tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta} \]
Substitute \( \tan\theta = \frac{1}{3} \):
\[ \tan\left(2\tan^{-1}(1/3)\right) = \frac{2(1/3)}{1 - (1/3)^2} = \frac{2/3}{8/9} = \frac{2}{3} \times \frac{9}{8} = \frac{3}{4} \]

</details>

40. 🔴 Find the value of sin(2 tan⁻¹(2/3)) + cos(2 tan⁻¹(2/3)).
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}\left(\frac{2}{3}\right) \implies \tan\theta = \frac{2}{3} \).
We need to evaluate \( \sin(2\theta) + \cos(2\theta) \).
Using the tangent double angle formulas:
1. \( \sin(2\theta) = \frac{2\tan\theta}{1 + \tan^2\theta} = \frac{2(2/3)}{1 + 4/9} = \frac{4/3}{13/9} = \frac{12}{13} \)
2. \( \cos(2\theta) = \frac{1 - \tan^2\theta}{1 + \tan^2\theta} = \frac{1 - 4/9}{1 + 4/9} = \frac{5/9}{13/9} = \frac{5}{13} \)
Adding the two results:
\[ \sin(2\theta) + \cos(2\theta) = \frac{12}{13} + \frac{5}{13} = \frac{17}{13} \]

</details>

---

## Stage 4: Type Mixer

1. 🟡 Find the principal values: sin⁻¹(−1/√2), cos⁻¹(1/2), tan⁻¹(√3).
<details>
<summary>Solution</summary>

We find each principal value separately:
1. Let \( \theta_1 = \sin^{-1}\left(-\frac{1}{\sqrt{2}}\right) \). Since \( \theta_1 \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \) and \( \sin\left(-\frac{\pi}{4}\right) = -\frac{1}{\sqrt{2}} \):
   \[ \sin^{-1}\left(-\frac{1}{\sqrt{2}}\right) = -\frac{\pi}{4} \]
2. Let \( \theta_2 = \cos^{-1}\left(\frac{1}{2}\right) \). Since \( \theta_2 \in [0, \pi] \) and \( \cos\left(\frac{\pi}{3}\right) = \frac{1}{2} \):
   \[ \cos^{-1}\left(\frac{1}{2}\right) = \frac{\pi}{3} \]
3. Let \( \theta_3 = \tan^{-1}(\sqrt{3}) \). Since \( \theta_3 \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \) and \( \tan\left(\frac{\pi}{3}\right) = \sqrt{3} \):
   \[ \tan^{-1}(\sqrt{3}) = \frac{\pi}{3} \]

The values are \( -\frac{\pi}{4} \), \( \frac{\pi}{3} \), and \( \frac{\pi}{3} \) respectively.

</details>

2. 🟡 Prove that arctan(1/2) + arctan(1/3) = π/4.
<details>
<summary>Solution</summary>

Since the product of the arguments is \( x y = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6} < 1 \), we use the sum formula:
\[ \tan^{-1}\left(\frac{1}{2}\right) + \tan^{-1}\left(\frac{1}{3}\right) = \tan^{-1}\left(\frac{1/2 + 1/3}{1 - 1/6}\right) = \tan^{-1}\left(\frac{5/6}{5/6}\right) = \tan^{-1}(1) \]
Since \( \tan^{-1}(1) = \frac{\pi}{4} \):
\[ \tan^{-1}\left(\frac{1}{2}\right) + \tan^{-1}\left(\frac{1}{3}\right) = \frac{\pi}{4} \]
Hence proved.

</details>

3. 🔴 ⭐ Evaluate: sin(cos⁻¹(3/5) + sin⁻¹(5/13)).
<details>
<summary>Solution</summary>

Let \( \alpha = \cos^{-1}\left(\frac{3}{5}\right) \implies \cos\alpha = \frac{3}{5} \).
Since \( \alpha \in [0, \pi] \) and \( \cos\alpha > 0 \), we have \( \alpha \in \left[0, \frac{\pi}{2}\right] \).
Thus, \( \sin\alpha = \sqrt{1 - \cos^2\alpha} = \frac{4}{5} \).

Let \( \beta = \sin^{-1}\left(\frac{5}{13}\right) \implies \sin\beta = \frac{5}{13} \).
Since \( \beta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \) and \( \sin\beta > 0 \), we have \( \beta \in \left[0, \frac{\pi}{2}\right] \).
Thus, \( \cos\beta = \sqrt{1 - \sin^2\beta} = \frac{12}{13} \).

We want to evaluate \( \sin(\alpha + \beta) \). Using the sine addition formula:
\[ \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta \]
Substitute the values:
\[ \sin(\alpha + \beta) = \left(\frac{4}{5}\right)\left(\frac{12}{13}\right) + \left(\frac{3}{5}\right)\left(\frac{5}{13}\right) = \frac{48}{65} + \frac{15}{65} = \frac{63}{65} \]

</details>

4. 🔴 Solve: tan⁻¹(2x) + tan⁻¹(3x) = π/4.
<details>
<summary>Solution</summary>

Assuming \( 6x^2 < 1 \), we apply the tangent sum identity:
\[ \tan^{-1}\left(\frac{2x + 3x}{1 - 6x^2}\right) = \frac{\pi}{4} \]
Taking tangent of both sides:
\[ \frac{5x}{1 - 6x^2} = 1 \implies 6x^2 + 5x - 1 = 0 \]
Factoring the quadratic:
\[ (6x - 1)(x + 1) = 0 \implies x = \frac{1}{6} \text{ or } x = -1 \]
Check the solutions:
- For \( x = -1 \): the LHS is \( \tan^{-1}(-2) + \tan^{-1}(-3) < 0 \), so this solution is rejected.
- For \( x = \frac{1}{6} \): the LHS is \( \tan^{-1}(1/3) + \tan^{-1}(1/2) \), which is in the first quadrant and evaluates to \( \frac{\pi}{4} \) (Valid).
Thus, the solution is \( x = \frac{1}{6} \).

</details>

5. 🔴 Simplify: sin⁻¹(3/5) + sin⁻¹(8/17) = sin⁻¹(77/85).
<details>
<summary>Solution</summary>

Let \( \alpha = \sin^{-1}\left(\frac{3}{5}\right) \implies \sin\alpha = \frac{3}{5} \), \( \cos\alpha = \frac{4}{5} \).
Let \( \beta = \sin^{-1}\left(\frac{8}{17}\right) \implies \sin\beta = \frac{8}{17} \), \( \cos\beta = \frac{15}{17} \).
Both \( \alpha \) and \( \beta \) are in \( \left[0, \frac{\pi}{2}\right] \).
We find \( \sin(\alpha + \beta) \):
\[ \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta \]
\[ \sin(\alpha + \beta) = \left(\frac{3}{5}\right)\left(\frac{15}{17}\right) + \left(\frac{4}{5}\right)\left(\frac{8}{17}\right) = \frac{45}{85} + \frac{32}{85} = \frac{77}{85} \]
Since \( \alpha, \beta \) are positive acute angles, their sum is:
\[ \alpha + \beta < 90^\circ + 90^\circ = 180^\circ \]
Specifically:
\( \sin\alpha = 0.6 \implies \alpha \approx 36.87^\circ \)
\( \sin\beta \approx 0.47 \implies \beta \approx 28.07^\circ \)
Thus, \( \alpha + \beta \approx 64.94^\circ < 90^\circ \), so \( \alpha + \beta \in \left[0, \frac{\pi}{2}\right] \).
Taking the inverse sine:
\[ \alpha + \beta = \sin^{-1}\left(\frac{77}{85}\right) \]
Substitute back the definitions of \( \alpha \) and \( \beta \):
\[ \sin^{-1}\left(\frac{3}{5}\right) + \sin^{-1}\left(\frac{8}{17}\right) = \sin^{-1}\left(\frac{77}{85}\right) \]
Hence proved.

</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Find the principal value of sin⁻¹(−1/2). **(1 mark)**

<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(-\frac{1}{2}\right) \).
Since the range of the principal value branch of \( \sin^{-1}x \) is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), and we know \( \sin\left(-\frac{\pi}{6}\right) = -\frac{1}{2} \):
\[ \sin^{-1}\left(-\frac{1}{2}\right) = -\frac{\pi}{6} \]

</details>

---

**Q2.** 🟡 Find the value of cos⁻¹(cos 7π/6). **(2 marks)**

<details>
<summary>Solution</summary>

The principal value range of \( \cos^{-1}x \) is \( [0, \pi] \). Since \( \frac{7\pi}{6} \notin [0, \pi] \), we rewrite \( \cos\left(\frac{7\pi}{6}\right) \) using the identity \( \cos(2\pi - \theta) = \cos\theta \):
\[ \cos\left(\frac{7\pi}{6}\right) = \cos\left(2\pi - \frac{7\pi}{6}\right) = \cos\left(\frac{5\pi}{6}\right) \]
Since \( \frac{5\pi}{6} \in [0, \pi] \):
\[ \cos^{-1}\left(\cos\left(\frac{7\pi}{6}\right)\right) = \cos^{-1}\left(\cos\left(\frac{5\pi}{6}\right)\right) = \frac{5\pi}{6} \]

</details>

---

**Q3.** 🟡 Write the value of sin⁻¹(3/5) + cos⁻¹(3/5). **(1 mark)**

<details>
<summary>Solution</summary>

We know the identity:
\[ \sin^{-1}x + \cos^{-1}x = \frac{\pi}{2} \quad \text{for } x \in [-1, 1] \]
Since \( \frac{3}{5} \in [-1, 1] \):
\[ \sin^{-1}\left(\frac{3}{5}\right) + \cos^{-1}\left(\frac{3}{5}\right) = \frac{\pi}{2} \]

</details>

---

**Q4.** 🟡 Evaluate tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3). **(2 marks)**

<details>
<summary>Solution</summary>

We evaluate the expression term-by-step:
1. Since \( \tan\left(\frac{\pi}{4}\right) = 1 \) and \( \frac{\pi}{4} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \):
   \[ \tan^{-1}(1) = \frac{\pi}{4} \]
2. For \( \tan^{-1}(2) + \tan^{-1}(3) \), since both \( 2 > 0 \) and \( 3 > 0 \) and their product \( 2 \times 3 = 6 > 1 \), we use the identity:
   \[ \tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\frac{x+y}{1-xy}\right) \]
   Therefore:
   \[ \tan^{-1}(2) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\frac{2+3}{1-6}\right) = \pi + \tan^{-1}(-1) \]
   Since \( \tan^{-1}(-1) = -\frac{\pi}{4} \):
   \[ \tan^{-1}(2) + \tan^{-1}(3) = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \]
3. Adding all terms together:
   \[ \tan^{-1}(1) + \tan^{-1}(2) + \tan^{-1}(3) = \frac{\pi}{4} + \frac{3\pi}{4} = \pi \]

</details>

---

## Stage 6: JEE Mains Arena

**Q1.** The principal value of sin⁻¹(−√3/2) is:
(a) −π/3
(b) π/3
(c) 2π/3
(d) −2π/3

<details>
<summary>Solution</summary>
sin⁻¹(−√3/2) = −π/3 (in [−π/2, π/2])
Answer: (a) 🟢
</details>

---

**Q2.** tan⁻¹(1/2) + tan⁻¹(1/3) equals:
(a) π/6
(b) π/4
(c) π/3
(d) π/2

<details>
<summary>Solution</summary>
tan⁻¹(1/2) + tan⁻¹(1/3) = tan⁻¹((1/2+1/3)/(1−1/6)) = tan⁻¹(1) = π/4
Answer: (b) 🟡 ⭐
</details>

---

**Q3.** The value of sin⁻¹(sin 2π/3) is:
(a) π/3
(b) 2π/3
(c) −π/3
(d) π/6

<details>
<summary>Solution</summary>
sin(2π/3) = √3/2. sin⁻¹(√3/2) = π/3 (in [−π/2, π/2]).
Answer: (a) 🟡 ⭐
</details>

---

**Q4.** If tan⁻¹(2x) + tan⁻¹(3x) = π/4, then x equals:
(a) 1/6
(b) 1
(c) −1
(d) 0

<details>
<summary>Solution</summary>
tan⁻¹(5x/(1−6x²)) = π/4
5x/(1−6x²) = 1
5x = 1 − 6x²
6x² + 5x − 1 = 0
(6x − 1)(x + 1) = 0
x = 1/6 or x = −1
x = −1 gives LHS = tan⁻¹(−2) + tan⁻¹(−3) < 0, not π/4
x = 1/6 ✓
Answer: (a) 🔴 ⭐
</details>

---

**Q5.** The value of sin(cos⁻¹(3/5) + sin⁻¹(5/13)) is:
(a) 56/65
(b) 63/65
(c) 16/65
(d) 33/65

<details>
<summary>Solution</summary>
cos⁻¹(3/5) = α → cos α = 3/5, sin α = 4/5
sin⁻¹(5/13) = β → sin β = 5/13, cos β = 12/13
sin(α + β) = sin α cos β + cos α sin β = (4/5)(12/13) + (3/5)(5/13)
= 48/65 + 15/65 = 63/65
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin⁻¹x ∈ [−π/2, π/2].
**Reason (R):** The range of arcsin is the principal value branch.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** sin⁻¹(1/2) + cos⁻¹(1/2) = π/2.
**Reason (R):** sin⁻¹x + cos⁻¹x = π/2 for all x ∈ [−1, 1].

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sin⁻¹(sin 5π/4) = π/4.
**Reason (R):** sin⁻¹(sin x) = x for all x.

<details>
<summary>Solution</summary>
A is true: sin⁻¹(sin 5π/4) = sin⁻¹(−1/√2) = −π/4... wait, that's −π/4, not π/4.
Actually sin⁻¹(sin 5π/4) = sin⁻¹(−1/√2) = −π/4.
But 5π/4 = 225°, sin = −1/√2, principal value = −π/4.
So A is false (it's −π/4, not π/4).
R is false: sin⁻¹(sin x) = x only when x ∈ [−π/2, π/2].
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** tan⁻¹x + tan⁻¹(1/x) = π/2 for x > 0.
**Reason (R):** tan(π/2 − θ) = cot θ = 1/tan θ.

<details>
<summary>Solution</summary>
A is true: tan⁻¹x + tan⁻¹(1/x) = π/2 for x > 0.
R is true and explains A (since tan⁻¹x = θ, tan⁻¹(1/x) = π/2 − θ).
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The principal value of sin⁻¹(1/√2) is:
   (a) π/4   (b) π/3   (c) π/6   (d) π/2
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(\frac{1}{\sqrt{2}}\right) \).
Since the range of the principal value branch of \( \sin^{-1}x \) is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), and we know that \( \sin\left(\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}} \):
\[ \sin^{-1}\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4} \]

**Answer: (a) \(\pi/4\)**
</details>

2. 🟢 The principal value of cos⁻¹(1/2) is:
   (a) π/6   (b) π/3   (c) π/4   (d) π/2
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(\frac{1}{2}\right) \).
Since the range of the principal value branch of \( \cos^{-1}x \) is \( [0, \pi] \), and we know that \( \cos\left(\frac{\pi}{3}\right) = \frac{1}{2} \):
\[ \cos^{-1}\left(\frac{1}{2}\right) = \frac{\pi}{3} \]

**Answer: (b) \(\pi/3\)**
</details>

3. 🟢 tan⁻¹(√3) equals:
   (a) π/6   (b) π/4   (c) π/3   (d) π/2
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}(\sqrt{3}) \).
Since the range of the principal value branch of \( \tan^{-1}x \) is \( \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \), and we know that \( \tan\left(\frac{\pi}{3}\right) = \sqrt{3} \):
\[ \tan^{-1}(\sqrt{3}) = \frac{\pi}{3} \]

**Answer: (c) \(\pi/3\)**
</details>

4. 🟡 sin⁻¹(−1) equals:
   (a) π/2   (b) −π/2   (c) π   (d) −π
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}(-1) \).
Since the range of the principal value branch of \( \sin^{-1}x \) is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), and we know that \( \sin\left(-\frac{\pi}{2}\right) = -1 \):
\[ \sin^{-1}(-1) = -\frac{\pi}{2} \]

**Answer: (b) \(-\pi/2\)**
</details>

5. 🟡 cos⁻¹(−1/2) equals:
   (a) π/3   (b) 2π/3   (c) π/6   (d) 5π/6
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(-\frac{1}{2}\right) \).
We know that for \( x \in [-1, 1] \), \( \cos^{-1}(-x) = \pi - \cos^{-1}x \).
Therefore:
\[ \cos^{-1}\left(-\frac{1}{2}\right) = \pi - \cos^{-1}\left(\frac{1}{2}\right) = \pi - \frac{\pi}{3} = \frac{2\pi}{3} \]

**Answer: (b) \(2\pi/3\)**
</details>

6. 🟡 sin⁻¹x + cos⁻¹x = ?<br>
   (a) 0   (b) π/2   (c) π   (d) −π/2
<details>
<summary>Solution</summary>

This is a standard trigonometric identity. For any \( x \in [-1, 1] \):
\[ \sin^{-1}x + \cos^{-1}x = \frac{\pi}{2} \]

**Answer: (b) \(\pi/2\)**
</details>

7. 🟡 tan⁻¹x + cot⁻¹x = ?<br>
   (a) 0   (b) π/2   (c) π   (d) −π/2
<details>
<summary>Solution</summary>

This is a standard trigonometric identity. For any \( x \in \mathbb{R} \):
\[ \tan^{-1}x + \cot^{-1}x = \frac{\pi}{2} \]

**Answer: (b) \(\pi/2\)**
</details>

8. 🟡 sin⁻¹(sin π/4) = ?<br>
   (a) π/4   (b) 3π/4   (c) −π/4   (d) 5π/4
<details>
<summary>Solution</summary>

Since the angle \( \frac{\pi}{4} \) lies within the principal value branch of \( \sin^{-1}x \), which is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we have:
\[ \sin^{-1}\left(\sin\left(\frac{\pi}{4}\right)\right) = \frac{\pi}{4} \]

**Answer: (a) \(\pi/4\)**
</details>

9. 🟡 cos⁻¹(cos 5π/4) = ?<br>
   (a) π/4   (b) 3π/4   (c) 5π/4   (d) −3π/4
<details>
<summary>Solution</summary>

The range of the principal value branch of \( \cos^{-1}x \) is \( [0, \pi] \).
Since \( \frac{5\pi}{4} \notin [0, \pi] \), we rewrite the cosine term using the identity \( \cos(2\pi - \theta) = \cos\theta \):
\[ \cos\left(\frac{5\pi}{4}\right) = \cos\left(2\pi - \frac{5\pi}{4}\right) = \cos\left(\frac{3\pi}{4}\right) \]
Since \( \frac{3\pi}{4} \in [0, \pi] \):
\[ \cos^{-1}\left(\cos\left(\frac{5\pi}{4}\right)\right) = \cos^{-1}\left(\cos\left(\frac{3\pi}{4}\right)\right) = \frac{3\pi}{4} \]

**Answer: (b) \(3\pi/4\)**
</details>

10. 🟡 sin(cos⁻¹(4/5)) = ?<br>
    (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Let \( \theta = \cos^{-1}\left(\frac{4}{5}\right) \implies \cos\theta = \frac{4}{5} \), where \( \theta \in [0, \pi] \).
Since \( \cos\theta > 0 \), \( \theta \in \left[0, \frac{\pi}{2}\right] \).
Using the Pythagorean identity:
\[ \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \sqrt{1 - \frac{16}{25}} = \sqrt{\frac{9}{25}} = \frac{3}{5} \]
Thus, \( \sin\left(\cos^{-1}\left(\frac{4}{5}\right)\right) = \frac{3}{5} \).

**Answer: (a) 3/5**
</details>

11. 🟡 cos(tan⁻¹(3/4)) = ?<br>
    (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Let \( \theta = \tan^{-1}\left(\frac{3}{4}\right) \implies \tan\theta = \frac{3}{4} \), where \( \theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \).
Since \( \tan\theta > 0 \), \( \theta \in \left(0, \frac{\pi}{2}\right) \).
Using a right triangle with opposite side \( 3 \) and adjacent side \( 4 \), the hypotenuse is:
\[ \sqrt{3^2 + 4^2} = 5 \]
Therefore:
\[ \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{4}{5} \]

**Answer: (b) 4/5**
</details>

12. 🟡 tan(sin⁻¹(5/13)) = ?<br>
    (a) 5/12   (b) 12/5   (c) 13/5   (d) 5/13
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(\frac{5}{13}\right) \implies \sin\theta = \frac{5}{13} \), where \( \theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \).
Since \( \sin\theta > 0 \), \( \theta \in \left(0, \frac{\pi}{2}\right) \).
Using a right triangle with opposite side \( 5 \) and hypotenuse \( 13 \), the adjacent side is:
\[ \sqrt{13^2 - 5^2} = 12 \]
Therefore:
\[ \tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{5}{12} \]

**Answer: (a) 5/12**
</details>

13. 🟡 Domain of sin⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) [−π/2, π/2]   (d) [0, π]
<details>
<summary>Solution</summary>

The sine function \( \sin\theta \) outputs values in the interval \( [-1, 1] \). Therefore, its inverse function \( \sin^{-1}x \) takes inputs from \( [-1, 1] \).
Thus, the domain of \( \sin^{-1}x \) is \( [-1, 1] \).

**Answer: (b) \([-1, 1]\)**
</details>

14. 🟡 Range of cos⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) [−π/2, π/2]   (d) [0, π]
<details>
<summary>Solution</summary>

To make the cosine function one-to-one so it has an inverse, its domain is restricted to the principal value branch \( [0, \pi] \).
Thus, the range (principal value branch) of \( \cos^{-1}x \) is \( [0, \pi] \).

**Answer: (d) \([0, \pi]\)**
</details>

15. 🟡 Domain of tan⁻¹x is:
    (a) ℝ   (b) [−1, 1]   (c) (−π/2, π/2)   (d) (0, π)
<details>
<summary>Solution</summary>

The tangent function \( \tan\theta \) outputs any real number (range is \( \mathbb{R} \)). Consequently, the inverse tangent function \( \tan^{-1}x \) accepts any real number as its input.
Thus, the domain of \( \tan^{-1}x \) is \( \mathbb{R} \).

**Answer: (a) \(\mathbb{R}\)**
</details>

16. 🟡 tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3) = ?<br>
    (a) π/2   (b) π   (c) 3π/2   (d) 2π
<details>
<summary>Solution</summary>

We evaluate the expression term-by-step:
1. \( \tan^{-1}(1) = \frac{\pi}{4} \).
2. For \( \tan^{-1}(2) + \tan^{-1}(3) \), since both \( 2 > 0 \) and \( 3 > 0 \) and their product \( 2 \times 3 = 6 > 1 \), we use the identity:
   \[ \tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\frac{x+y}{1-xy}\right) \]
   Therefore:
   \[ \tan^{-1}(2) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\frac{2+3}{1-6}\right) = \pi + \tan^{-1}(-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \]
3. Adding all terms together:
   \[ \tan^{-1}(1) + \tan^{-1}(2) + \tan^{-1}(3) = \frac{\pi}{4} + \frac{3\pi}{4} = \pi \]

**Answer: (b) \(\pi\)**
</details>

17. 🟡 sin⁻¹(12/13) + cos⁻¹(12/13) = ?<br>
    (a) 0   (b) π/2   (c) π   (d) −π/2
<details>
<summary>Solution</summary>

Using the identity \( \sin^{-1}x + \cos^{-1}x = \frac{\pi}{2} \) for all \( x \in [-1, 1] \):
Since \( \frac{12}{13} \in [-1, 1] \), we have:
\[ \sin^{-1}\left(\frac{12}{13}\right) + \cos^{-1}\left(\frac{12}{13}\right) = \frac{\pi}{2} \]

**Answer: (b) \(\pi/2\)**
</details>

18. 🟡 sin⁻¹(sin 3) equals:
    (a) 3   (b) π − 3   (c) 3 − π   (d) −3
<details>
<summary>Solution</summary>

The range of the principal value branch of \( \sin^{-1}x \) is \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \approx [-1.57, 1.57] \).
Since \( 3 \) radians lies outside this interval (specifically in the second quadrant, as \( \frac{\pi}{2} < 3 < \pi \)), we rewrite using \( \sin\theta = \sin(\pi - \theta) \):
\[ \sin(3) = \sin(\pi - 3) \]
Since \( \pi - 3 \approx 3.14 - 3 = 0.14 \), which lies within \( \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \), we get:
\[ \sin^{-1}(\sin 3) = \sin^{-1}(\sin(\pi - 3)) = \pi - 3 \]

**Answer: (b) \(\pi - 3\)**
</details>

19. 🟡 tan⁻¹(2) + tan⁻¹(3) = ?<br>
    (a) π/4   (b) 3π/4   (c) π/2   (d) π
<details>
<summary>Solution</summary>

Since \( x = 2 > 0 \), \( y = 3 > 0 \), and their product \( xy = 6 > 1 \), we use the identity:
\[ \tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\left(\frac{x+y}{1-xy}\right) \]
Substitute \( x=2 \) and \( y=3 \):
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi + \tan^{-1}\left(\frac{2+3}{1-6}\right) = \pi + \tan^{-1}(-1) \]
Since \( \tan^{-1}(-1) = -\frac{\pi}{4} \):
\[ \tan^{-1}(2) + \tan^{-1}(3) = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \]

**Answer: (b) \(3\pi/4\)**
</details>

20. 🟡 The value of sin(2 sin⁻¹(3/5)) is:
    (a) 24/25   (b) 12/25   (c) 6/25   (d) 4/5
<details>
<summary>Solution</summary>

Let \( \theta = \sin^{-1}\left(\frac{3}{5}\right) \implies \sin\theta = \frac{3}{5} \).
Since \( \theta \in \left[0, \frac{\pi}{2}\right] \), we have:
\[ \cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \frac{9}{25}} = \frac{4}{5} \]
We need to find \( \sin(2\theta) \). Using the double angle formula:
\[ \sin(2\theta) = 2\sin\theta\cos\theta = 2\left(\frac{3}{5}\right)\left(\frac{4}{5}\right) = \frac{24}{25} \]

**Answer: (a) 24/25**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | b | 16 | b |
| 2 | b | 7 | b | 12 | a | 17 | b |
| 3 | c | 8 | a | 13 | b | 18 | b |
| 4 | b | 9 | b | 14 | d | 19 | b |
| 5 | b | 10 | a | 15 | a | 20 | a |

</details>
