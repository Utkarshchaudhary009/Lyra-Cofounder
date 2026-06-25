# Chapter 16: Maximum & Minimum of Trig Expressions

---

## Stage 1: The Core Idea

### Finding the Boundaries

Every trig function has a limited range:
- sin θ ∈ [−1, 1]
- cos θ ∈ [−1, 1]
- a sin θ + b cos θ ∈ [−√(a²+b²), √(a²+b²)]

JEE loves asking: "Find the maximum/minimum value of ..." These problems test whether you understand the bounds.

---

## Stage 2: The Formula Lab

### Key Ranges

```
−1 ≤ sin θ ≤ 1
−1 ≤ cos θ ≤ 1
−√(a²+b²) ≤ a sin θ + b cos θ ≤ √(a²+b²)
```

### Expressing a sin θ + b cos θ as a Single Sine

```
a sin θ + b cos θ = R sin(θ + φ)
where R = √(a²+b²), tan φ = b/a
```

Or: `= R cos(θ − φ)` where tan φ = a/b.

### Quadratic Forms

For a sin²θ + b sin θ + c, treat as a quadratic in t = sin θ, then evaluate at endpoints.

---

## Stage 3: Type-wise Mastery

### Type 1: Max/Min of a ± b sin θ

**Goal:** Find range of expressions like 3 + 4 sin θ.

**Solved Example:**

Find the maximum and minimum of f(θ) = 5 − 3 sin θ.

**Solution:**
```
−1 ≤ sin θ ≤ 1
3 ≥ −3 sin θ ≥ −3
5+3 ≥ 5−3 sin θ ≥ 5−3
8 ≥ f(θ) ≥ 2
Max = 8, Min = 2
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Find max/min of f = 2 + 3 cos θ.
<details>
<summary>Solution</summary>

We know that for any real \(\theta\):
\[ -1 \le \cos\theta \le 1 \]

Multiplying by \(3\):
\[ -3 \le 3\cos\theta \le 3 \]

Adding \(2\):
\[ 2 - 3 \le 2 + 3\cos\theta \le 2 + 3 \]
\[ -1 \le f \le 5 \]

Hence:
- \(\text{Maximum value} = 5\)
- \(\text{Minimum value} = -1\)
</details>

2. 🟢 Find max/min of f = 4 − 5 sin θ.
<details>
<summary>Solution</summary>

We know that for any real \(\theta\):
\[ -1 \le \sin\theta \le 1 \]

Multiplying by \(-5\) (which reverses the inequality signs):
\[ -5 \le -5\sin\theta \le 5 \]

Adding \(4\):
\[ 4 - 5 \le 4 - 5\sin\theta \le 4 + 5 \]
\[ -1 \le f \le 9 \]

Hence:
- \(\text{Maximum value} = 9\)
- \(\text{Minimum value} = -1\)
</details>

3. 🟡 Find max/min of f = 2/(3 + sin θ).
<details>
<summary>Solution</summary>

We start with the range of \(\sin\theta\):
\[ -1 \le \sin\theta \le 1 \]

Adding \(3\):
\[ 2 \le 3 + \sin\theta \le 4 \]

Since all terms are positive, taking the reciprocal reverses the inequality:
\[ \frac{1}{4} \le \frac{1}{3 + \sin\theta} \le \frac{1}{2} \]

Multiplying by \(2\):
\[ \frac{2}{4} \le \frac{2}{3 + \sin\theta} \le \frac{2}{2} \]
\[ \frac{1}{2} \le f \le 1 \]

Hence:
- \(\text{Maximum value} = 1\)
- \(\text{Minimum value} = \frac{1}{2}\)
</details>

4. 🟡 Find max/min of f = 1/(2 − cos θ).
<details>
<summary>Solution</summary>

We start with the range of \(\cos\theta\):
\[ -1 \le \cos\theta \le 1 \]

Multiplying by \(-1\):
\[ -1 \le -\cos\theta \le 1 \]

Adding \(2\):
\[ 1 \le 2 - \cos\theta \le 3 \]

Taking the reciprocal (which reverses the inequality since all terms are positive):
\[ \frac{1}{3} \le \frac{1}{2 - \cos\theta} \le 1 \]

Hence:
- \(\text{Maximum value} = 1\)
- \(\text{Minimum value} = \frac{1}{3}\)
</details>

5. 🟡 Find max/min of f = 3 − 2 cos²θ.
<details>
<summary>Solution</summary>

We know that for any real \(\theta\):
\[ 0 \le \cos^2\theta \le 1 \]

Multiplying by \(-2\) (reversing the inequality):
\[ -2 \le -2\cos^2\theta \le 0 \]

Adding \(3\):
\[ 3 - 2 \le 3 - 2\cos^2\theta \le 3 + 0 \]
\[ 1 \le f \le 3 \]

Hence:
- \(\text{Maximum value} = 3\)
- \(\text{Minimum value} = 1\)
</details>

---

### Type 2: a sin θ + b cos θ

**Goal:** Use R-formula to find range.

**Solved Example:**

Find max/min of f(θ) = 3 sin θ + 4 cos θ.

**Solution:**
```
R = √(3² + 4²) = 5
∴ f(θ) = 5 sin(θ + φ)
Max = 5, Min = −5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Find max/min of 5 sin θ + 12 cos θ.
<details>
<summary>Solution</summary>

Using the standard range formula for \( a\sin\theta + b\cos\theta \):
\[ -\sqrt{a^2+b^2} \le a\sin\theta + b\cos\theta \le \sqrt{a^2+b^2} \]

Here, \( a = 5 \) and \( b = 12 \).
Compute the value of \( \sqrt{a^2+b^2} \):
\[ \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13 \]

Therefore:
- \(\text{Maximum value} = 13\)
- \(\text{Minimum value} = -13\)
</details>

7. 🟡 Find max/min of 8 sin θ − 6 cos θ.
<details>
<summary>Solution</summary>

Using the standard range formula for \( a\sin\theta + b\cos\theta \):
\[ -\sqrt{a^2+b^2} \le a\sin\theta + b\cos\theta \le \sqrt{a^2+b^2} \]

Here, \( a = 8 \) and \( b = -6 \).
Compute the value of \( \sqrt{a^2+b^2} \):
\[ \sqrt{8^2 + (-6)^2} = \sqrt{64 + 36} = \sqrt{100} = 10 \]

Therefore:
- \(\text{Maximum value} = 10\)
- \(\text{Minimum value} = -10\)
</details>

8. 🟡 Find max/min of sin θ + cos θ.
<details>
<summary>Solution</summary>

Using the standard range formula for \( a\sin\theta + b\cos\theta \):
\[ -\sqrt{a^2+b^2} \le a\sin\theta + b\cos\theta \le \sqrt{a^2+b^2} \]

Here, \( a = 1 \) and \( b = 1 \).
Compute the value of \( \sqrt{a^2+b^2} \):
\[ \sqrt{1^2 + 1^2} = \sqrt{2} \]

Therefore:
- \(\text{Maximum value} = \sqrt{2}\)
- \(\text{Minimum value} = -\sqrt{2}\)
</details>

9. 🟡 Find max/min of √3 sin θ + cos θ.
<details>
<summary>Solution</summary>

Using the standard range formula for \( a\sin\theta + b\cos\theta \):
\[ -\sqrt{a^2+b^2} \le a\sin\theta + b\cos\theta \le \sqrt{a^2+b^2} \]

Here, \( a = \sqrt{3} \) and \( b = 1 \).
Compute the value of \( \sqrt{a^2+b^2} \):
\[ \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = 2 \]

Therefore:
- \(\text{Maximum value} = 2\)
- \(\text{Minimum value} = -2\)
</details>

10. 🔴 ⭐ Find max/min of 3 sin θ − 4 cos θ + 2.
<details>
<summary>Solution</summary>

First, let us find the range of \( 3\sin\theta - 4\cos\theta \).
Using the formula for \( a\sin\theta + b\cos\theta \):
\[ -\sqrt{3^2 + (-4)^2} \le 3\sin\theta - 4\cos\theta \le \sqrt{3^2 + (-4)^2} \]
\[ -5 \le 3\sin\theta - 4\cos\theta \le 5 \]

Now, add \( 2 \) to the entire inequality:
\[ -5 + 2 \le 3\sin\theta - 4\cos\theta + 2 \le 5 + 2 \]
\[ -3 \le f(\theta) \le 7 \]

Therefore:
- \(\text{Maximum value} = 7\)
- \(\text{Minimum value} = -3\)
</details>

---

### Type 3: Quadratic Forms

**Goal:** Find max/min of expressions like a sin²θ + b sin θ + c.

**Solved Example:**

Find max/min of f = 2 sin²θ − 3 sin θ + 1.

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f(t) = 2t² − 3t + 1
Vertex: t = 3/4 = 0.75
f(0.75) = 2(9/16) − 3(3/4) + 1 = 9/8 − 9/4 + 1 = (9 − 18 + 8)/8 = −1/8

Check endpoints:
f(−1) = 2 + 3 + 1 = 6
f(1) = 2 − 3 + 1 = 0

Max = 6, Min = −1/8
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Find max/min of 3 sin²θ + 2 sin θ − 1.
<details>
<summary>Solution</summary>

Let \( t = \sin\theta \). Since \( \theta \) is a real number, \( t \in [-1, 1] \).
The expression is a quadratic function of \( t \):
\[ f(t) = 3t^2 + 2t - 1 \]

First, find the vertex of this parabola:
\[ t = -\frac{b}{2a} = -\frac{2}{2(3)} = -\frac{1}{3} \]

Since \( -\frac{1}{3} \in [-1, 1] \), we evaluate the function at the vertex and the boundaries \( t = -1 \) and \( t = 1 \):
1. **At the vertex** \( t = -\frac{1}{3} \):
   \[ f\left(-\frac{1}{3}\right) = 3\left(-\frac{1}{3}\right)^2 + 2\left(-\frac{1}{3}\right) - 1 = 3\left(\frac{1}{9}\right) - \frac{2}{3} - 1 = \frac{1}{3} - \frac{2}{3} - 1 = -\frac{4}{3} \]

2. **At endpoint** \( t = -1 \):
   \[ f(-1) = 3(-1)^2 + 2(-1) - 1 = 3 - 2 - 1 = 0 \]

3. **At endpoint** \( t = 1 \):
   \[ f(1) = 3(1)^2 + 2(1) - 1 = 3 + 2 - 1 = 4 \]

Comparing these values:
- The minimum value is \( -\frac{4}{3} \) (at \( \sin\theta = -\frac{1}{3} \)).
- The maximum value is \( 4 \) (at \( \sin\theta = 1 \)).
</details>

12. 🟡 Find max/min of cos²θ − 2 cos θ + 3.
<details>
<summary>Solution</summary>

Let \( t = \cos\theta \). Since \( \theta \) is a real number, \( t \in [-1, 1] \).
The expression is:
\[ f(t) = t^2 - 2t + 3 \]

We can rewrite this by completing the square:
\[ f(t) = (t - 1)^2 + 2 \]

Since \( t \in [-1, 1] \):
1. The minimum value of \( (t-1)^2 \) occurs when \( t = 1 \), where \( (1-1)^2 = 0 \).
   \[ \text{Minimum value} = f(1) = 0 + 2 = 2 \]

2. The maximum value of \( (t-1)^2 \) occurs when \( t \) is furthest from \( 1 \), which is at \( t = -1 \).
   \[ \text{Maximum value} = f(-1) = (-1 - 1)^2 + 2 = 4 + 2 = 6 \]

Therefore:
- \(\text{Maximum value} = 6\)
- \(\text{Minimum value} = 2\)
</details>

13. 🟡 Find max/min of 2 sin²θ + 5 sin θ − 3.
<details>
<summary>Solution</summary>

Let \( t = \sin\theta \). Since \( \theta \in \mathbb{R} \), we have \( t \in [-1, 1] \).
The expression is:
\[ f(t) = 2t^2 + 5t - 3 \]

First, locate the vertex:
\[ t = -\frac{b}{2a} = -\frac{5}{2(2)} = -1.25 \]

Since \( -1.25 \notin [-1, 1] \), the function is monotonic on the interval \( [-1, 1] \). Thus, the extreme values must occur at the endpoints \( t = -1 \) and \( t = 1 \):
1. **At endpoint** \( t = -1 \):
   \[ f(-1) = 2(-1)^2 + 5(-1) - 3 = 2 - 5 - 3 = -6 \]

2. **At endpoint** \( t = 1 \):
   \[ f(1) = 2(1)^2 + 5(1) - 3 = 2 + 5 - 3 = 4 \]

Therefore:
- \(\text{Maximum value} = 4\)
- \(\text{Minimum value} = -6\)
</details>

14. 🔴 Find max/min of sin⁴θ + cos⁴θ.
<details>
<summary>Solution</summary>

We simplify the expression:
\[ \sin^4\theta + \cos^4\theta = (\sin^2\theta + \cos^2\theta)^2 - 2\sin^2\theta\cos^2\theta \]
\[ = 1 - 2\left(\sin\theta\cos\theta\right)^2 \]
\[ = 1 - \frac{1}{2}(2\sin\theta\cos\theta)^2 = 1 - \frac{1}{2}\sin^2 2\theta \]

We know the range of \( \sin^2 2\theta \) is:
\[ 0 \le \sin^2 2\theta \le 1 \]

Multiplying by \( -\frac{1}{2} \) (reversing inequality):
\[ -\frac{1}{2} \le -\frac{1}{2}\sin^2 2\theta \le 0 \]

Adding \( 1 \):
\[ 1 - \frac{1}{2} \le 1 - \frac{1}{2}\sin^2 2\theta \le 1 \]
\[ \frac{1}{2} \le \sin^4\theta + \cos^4\theta \le 1 \]

Therefore:
- \(\text{Maximum value} = 1\) (when \( \sin^2 2\theta = 0 \), i.e., \( \theta = \frac{k\pi}{2} \))
- \(\text{Minimum value} = \frac{1}{2} \) (when \( \sin^2 2\theta = 1 \), i.e., \( \theta = \frac{\pi}{4} + \frac{k\pi}{2} \))
</details>

15. 🔴 ⭐ Find max/min of sin⁶θ + cos⁶θ.
<details>
<summary>Solution</summary>

We simplify using the identity \( a^3 + b^3 = (a+b)(a^2 - ab + b^2) \) with \( a = \sin^2\theta \) and \( b = \cos^2\theta \):
\[ \sin^6\theta + \cos^6\theta = (\sin^2\theta + \cos^2\theta)(\sin^4\theta - \sin^2\theta\cos^2\theta + \cos^4\theta) \]
\[ = 1 \cdot [(\sin^2\theta + \cos^2\theta)^2 - 3\sin^2\theta\cos^2\theta] \]
\[ = 1 - 3\sin^2\theta\cos^2\theta \]
\[ = 1 - \frac{3}{4}(2\sin\theta\cos\theta)^2 = 1 - \frac{3}{4}\sin^2 2\theta \]

We know:
\[ 0 \le \sin^2 2\theta \le 1 \]

Multiplying by \( -\frac{3}{4} \):
\[ -\frac{3}{4} \le -\frac{3}{4}\sin^2 2\theta \le 0 \]

Adding \( 1 \):
\[ 1 - \frac{3}{4} \le 1 - \frac{3}{4}\sin^2 2\theta \le 1 \]
\[ \frac{1}{4} \le \sin^6\theta + \cos^6\theta \le 1 \]

Therefore:
- \(\text{Maximum value} = 1\) (when \( \sin^2 2\theta = 0 \))
- \(\text{Minimum value} = \frac{1}{4}\) (when \( \sin^2 2\theta = 1 \))
</details>

---

### Type 4: Using AM-GM

**Goal:** Use AM ≥ GM for expressions like tan θ + cot θ.

**Solved Example:**

Find the minimum of tan θ + cot θ for acute θ.

**Solution:**
```
AM ≥ GM: (tan θ + cot θ)/2 ≥ √(tan θ × cot θ) = 1
tan θ + cot θ ≥ 2
Minimum = 2 (at θ = 45°)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Find minimum of sec θ + cosec θ for acute θ.
<details>
<summary>Solution</summary>

Let \( f(\theta) = \sec\theta + \csc\theta \) for \( \theta \in (0, \pi/2) \).
To find the minimum, we differentiate \( f(\theta) \) with respect to \( \theta \):
\[ f'(\theta) = \sec\theta\tan\theta - \csc\theta\cot\theta = \frac{\sin\theta}{\cos^2\theta} - \frac{\cos\theta}{\sin^2\theta} \]
\[ = \frac{\sin^3\theta - \cos^3\theta}{\sin^2\theta\cos^2\theta} \]

Set \( f'(\theta) = 0 \):
\[ \sin^3\theta - \cos^3\theta = 0 \implies \tan^3\theta = 1 \implies \tan\theta = 1 \]

For acute \( \theta \), this gives \( \theta = \frac{\pi}{4} \).
Since \( f(\theta) \to \infty \) as \( \theta \to 0^+ \) or \( \theta \to (\pi/2)^- \), this critical point must correspond to a minimum.

Evaluate the function at \( \theta = \frac{\pi}{4} \):
\[ f\left(\frac{\pi}{4}\right) = \sec\left(\frac{\pi}{4}\right) + \csc\left(\frac{\pi}{4}\right) = \sqrt{2} + \sqrt{2} = 2\sqrt{2} \]

Thus, the minimum value is \( 2\sqrt{2} \).
</details>

17. 🟡 Find minimum of sin θ + cosec θ for acute θ.
<details>
<summary>Solution</summary>

For acute \( \theta \in (0, \pi/2) \), both \( \sin\theta \) and \( \csc\theta \) are positive.
Applying the AM-GM inequality:
\[ \frac{\sin\theta + \csc\theta}{2} \ge \sqrt{\sin\theta \cdot \csc\theta} = \sqrt{\sin\theta \cdot \frac{1}{\sin\theta}} = 1 \]
\[ \sin\theta + \csc\theta \ge 2 \]

Equality holds when \( \sin\theta = \csc\theta \implies \sin^2\theta = 1 \implies \sin\theta = 1 \), which occurs at the boundary \( \theta = \frac{\pi}{2} \).
For strictly acute \( \theta \in (0, \pi/2) \), \( \sin\theta < 1 \), so the expression strictly exceeds \( 2 \), but has an infimum of \( 2 \). Allowing the limit or boundary at \( \theta = \frac{\pi}{2} \), the minimum value is \( 2 \).
</details>

18. 🟡 Find minimum of cos θ + sec θ for acute θ.
<details>
<summary>Solution</summary>

For acute \( \theta \in (0, \pi/2) \), \( \cos\theta \) and \( \sec\theta \) are positive.
Applying the AM-GM inequality:
\[ \frac{\cos\theta + \sec\theta}{2} \ge \sqrt{\cos\theta \cdot \sec\theta} = \sqrt{\cos\theta \cdot \frac{1}{\cos\theta}} = 1 \]
\[ \cos\theta + \sec\theta \ge 2 \]

Equality holds when \( \cos\theta = \sec\theta \implies \cos^2\theta = 1 \implies \cos\theta = 1 \), which occurs at the boundary \( \theta = 0 \). 
If the range is considered to approach \( 0 \), the infimum of the expression is \( 2 \). Allowing the boundary, the minimum value is \( 2 \).
</details>

19. 🔴 ⭐ Find the maximum of sin²θ cos²θ.
<details>
<summary>Solution</summary>

We rewrite the expression:
\[ \sin^2\theta \cos^2\theta = (\sin\theta\cos\theta)^2 = \left(\frac{1}{2}\sin 2\theta\right)^2 = \frac{1}{4}\sin^2 2\theta \]

Since \( \sin^2 2\theta \le 1 \) for all real \( \theta \):
\[ \frac{1}{4}\sin^2 2\theta \le \frac{1}{4} \]

The maximum value is \( \frac{1}{4} \) (which occurs when \( \sin^2 2\theta = 1 \), i.e., \( \theta = \frac{\pi}{4} + \frac{k\pi}{2} \)).
</details>

20. 🔴 Find the maximum of sin θ cos θ.
<details>
<summary>Solution</summary>

We rewrite the expression:
\[ \sin\theta\cos\theta = \frac{1}{2}\sin 2\theta \]

We know that for all real \( \theta \):
\[ \sin 2\theta \le 1 \]

Multiplying by \( \frac{1}{2} \):
\[ \frac{1}{2}\sin 2\theta \le \frac{1}{2} \]

Thus, the maximum value is \( \frac{1}{2} \) (which occurs when \( \theta = \frac{\pi}{4} + k\pi \)).
</details>

---

### Type 5: Substitution Methods

**Goal:** Substitute t = sin θ ± cos θ to simplify.

**Key:**
```
If sin θ + cos θ = t, then sin θ cos θ = (t² − 1)/2
Range of t = [−√2, √2]
```

**Solved Example:**

Find max/min of sin θ cos θ.

**Solution:**
```
sin θ cos θ = (1/2) sin 2θ
Since sin 2θ ∈ [−1, 1]:
Max = 1/2, Min = −1/2
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 Find max/min of sin θ + cos θ.
<details>
<summary>Solution</summary>

This is a direct application of the \( a\sin\theta + b\cos\theta \) formula where \( a = 1 \) and \( b = 1 \):
\[ -\sqrt{1^2 + 1^2} \le \sin\theta + \cos\theta \le \sqrt{1^2 + 1^2} \]
\[ -\sqrt{2} \le \sin\theta + \cos\theta \le \sqrt{2} \]

Therefore:
- \(\text{Maximum value} = \sqrt{2}\)
- \(\text{Minimum value} = -\sqrt{2}\)
</details>

22. 🟡 Find max/min of sin²θ + cos⁴θ. (Hint: use substitution or range analysis.)
<details>
<summary>Solution</summary>

Using the identity \( \sin^2\theta = 1 - \cos^2\theta \), we rewrite the expression:
\[ f(\theta) = (1 - \cos^2\theta) + \cos^4\theta = \cos^4\theta - \cos^2\theta + 1 \]

Let \( t = \cos^2\theta \). Since \( \theta \) is a real number, \( t \in [0, 1] \).
The expression becomes a quadratic in \( t \):
\[ g(t) = t^2 - t + 1 \]

To find the minimum and maximum of \( g(t) \) on \( [0, 1] \):
1. **Vertex**: \( t = -\frac{b}{2a} = -\frac{-1}{2(1)} = \frac{1}{2} \).
   Since \( \frac{1}{2} \in [0, 1] \), we evaluate:
   \[ g\left(\frac{1}{2}\right) = \left(\frac{1}{2}\right)^2 - \frac{1}{2} + 1 = \frac{1}{4} - \frac{1}{2} + 1 = \frac{3}{4} \]

2. **Endpoints**:
   - At \( t = 0 \): \( g(0) = 1 \)
   - At \( t = 1 \): \( g(1) = 1^2 - 1 + 1 = 1 \)

Comparing these values:
- \(\text{Maximum value} = 1\) (achieved when \( \cos^2\theta = 0 \) or \( 1 \))
- \(\text{Minimum value} = \frac{3}{4}\) (achieved when \( \cos^2\theta = \frac{1}{2} \))
</details>

23. 🟡 Find max/min of sin 2θ − cos 2θ.
<details>
<summary>Solution</summary>

This expression is of the form \( a\sin x + b\cos x \) where \( x = 2\theta \), \( a = 1 \), and \( b = -1 \).
The range is given by:
\[ -\sqrt{a^2 + b^2} \le a\sin x + b\cos x \le \sqrt{a^2 + b^2} \]
\[ -\sqrt{1^2 + (-1)^2} \le \sin 2\theta - \cos 2\theta \le \sqrt{1^2 + (-1)^2} \]
\[ -\sqrt{2} \le \sin 2\theta - \cos 2\theta \le \sqrt{2} \]

Therefore:
- \(\text{Maximum value} = \sqrt{2}\)
- \(\text{Minimum value} = -\sqrt{2}\)
</details>

24. 🔴 ⭐ Find max/min of sin θ + cos θ + sin θ cos θ.
<details>
<summary>Solution</summary>

Let \( t = \sin\theta + \cos\theta \).
Squaring both sides:
\[ t^2 = (\sin\theta + \cos\theta)^2 = \sin^2\theta + \cos^2\theta + 2\sin\theta\cos\theta = 1 + 2\sin\theta\cos\theta \]
\[ \implies \sin\theta\cos\theta = \frac{t^2 - 1}{2} \]

The range of \( t \) is:
\[ -\sqrt{2} \le t \le \sqrt{2} \]

Substitute these into the original expression:
\[ f(t) = t + \frac{t^2 - 1}{2} = \frac{1}{2}t^2 + t - \frac{1}{2} \]

This is a quadratic in \( t \) defined on the interval \( [-\sqrt{2}, \sqrt{2}] \).
First, find the vertex:
\[ t = -\frac{b}{2a} = -\frac{1}{2(1/2)} = -1 \]

Since \( -1 \in [-\sqrt{2}, \sqrt{2}] \), we evaluate:
1. **At vertex** \( t = -1 \):
   \[ f(-1) = \frac{1}{2}(-1)^2 + (-1) - \frac{1}{2} = \frac{1}{2} - 1 - \frac{1}{2} = -1 \]

2. **At endpoint** \( t = \sqrt{2} \):
   \[ f(\sqrt{2}) = \frac{1}{2}(\sqrt{2})^2 + \sqrt{2} - \frac{1}{2} = 1 + \sqrt{2} - \frac{1}{2} = \sqrt{2} + \frac{1}{2} \approx 1.414 + 0.5 = 1.914 \]

3. **At endpoint** \( t = -\sqrt{2} \):
   \[ f(-\sqrt{2}) = \frac{1}{2}(-\sqrt{2})^2 - \sqrt{2} - \frac{1}{2} = 1 - \sqrt{2} - \frac{1}{2} = \frac{1}{2} - \sqrt{2} \approx 0.5 - 1.414 = -0.914 \]

Comparing these values:
- \(\text{Maximum value} = \sqrt{2} + \frac{1}{2} = \frac{2\sqrt{2} + 1}{2}\)
- \(\text{Minimum value} = -1\)
</details>

25. 🔴 Find max/min of (sin θ + cos θ)(sin θ − cos θ).
<details>
<summary>Solution</summary>

Expanding the product using the difference of squares:
\[ f(\theta) = \sin^2\theta - \cos^2\theta \]

We use the double-angle formula for cosine:
\[ \cos 2\theta = \cos^2\theta - \sin^2\theta \implies \sin^2\theta - \cos^2\theta = -\cos 2\theta \]

Since the range of \( \cos 2\theta \) is \( [-1, 1] \), the range of \( -\cos 2\theta \) is also \( [-1, 1] \):
\[ -1 \le f(\theta) \le 1 \]

Therefore:
- \(\text{Maximum value} = 1\)
- \(\text{Minimum value} = -1\)
</details>

---

### Type 6: Range of Rational Trig Functions

**Goal:** Find range of f = (a sin θ + b)/(c sin θ + d).

**Method:** Write as sin θ = ... then use −1 ≤ sin θ ≤ 1.

**Solved Example:**

Find range of f(θ) = (2 sin θ + 3)/(sin θ + 2).

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f = (2t + 3)/(t + 2)

Method: Cross multiply:
f(t+2) = 2t+3
ft + 2f = 2t + 3
ft − 2t = 3 − 2f
t(f − 2) = 3 − 2f
t = (3 − 2f)/(f − 2)

Since −1 ≤ t ≤ 1:
−1 ≤ (3 − 2f)/(f − 2) ≤ 1

Solve: f ∈ [1/3, 5/3]...(exercise complete)
```
🔴 Hard

---

**Practice Problems:**

26. 🔴 Find range of (sin θ + 2)/(sin θ + 3).
<details>
<summary>Solution</summary>

Let \( t = \sin\theta \). Since \( \theta \in \mathbb{R} \), we have \( t \in [-1, 1] \).
The expression is:
\[ f(t) = \frac{t + 2}{t + 3} \]

Simplify by rewriting the numerator:
\[ f(t) = \frac{(t + 3) - 1}{t + 3} = 1 - \frac{1}{t + 3} \]

Since \( -1 \le t \le 1 \):
\[ 2 \le t + 3 \le 4 \]

Taking reciprocals (which reverses the inequalities because all terms are positive):
\[ \frac{1}{4} \le \frac{1}{t + 3} \le \frac{1}{2} \]

Multiplying by \(-1\):
\[ -\frac{1}{2} \le -\frac{1}{t + 3} \le -\frac{1}{4} \]

Adding \(1\):
\[ 1 - \frac{1}{2} \le 1 - \frac{1}{t + 3} \le 1 - \frac{1}{4} \]
\[ \frac{1}{2} \le f(t) \le \frac{3}{4} \]

Thus, the range of the expression is \( \left[\frac{1}{2}, \frac{3}{4}\right] \).
</details>

27. 🔴 Find range of (2 cos θ + 1)/(cos θ − 2).
<details>
<summary>Solution</summary>

Let \( t = \cos\theta \). Since \( \theta \in \mathbb{R} \), we have \( t \in [-1, 1] \).
The expression is:
\[ f(t) = \frac{2t + 1}{t - 2} \]

Rewrite the numerator:
\[ f(t) = \frac{2(t - 2) + 5}{t - 2} = 2 + \frac{5}{t - 2} \]

Since \( -1 \le t \le 1 \):
\[ -3 \le t - 2 \le -1 \]

Taking reciprocals (which reverses the inequalities because all terms are negative):
\[ -1 \le \frac{1}{t - 2} \le -\frac{1}{3} \]

Multiplying by \( 5 \):
\[ -5 \le \frac{5}{t - 2} \le -\frac{5}{3} \]

Adding \( 2 \):
\[ 2 - 5 \le 2 + \frac{5}{t - 2} \le 2 - \frac{5}{3} \]
\[ -3 \le f(t) \le \frac{1}{3} \]

Thus, the range is \( \left[-3, \frac{1}{3}\right] \).
</details>

28. 🔴 Find range of (3 tan θ − 1)/(tan θ + 2).
<details>
<summary>Solution</summary>

Let \( t = \tan\theta \). For \( \theta \in \mathbb{R} \) (excluding values where \( \tan\theta \) is undefined), \( t \) can take any real value: \( t \in \mathbb{R} \).
The expression is:
\[ f(t) = \frac{3t - 1}{t + 2} \]

Rewrite the numerator:
\[ f(t) = \frac{3(t + 2) - 7}{t + 2} = 3 - \frac{7}{t + 2} \]

We analyze the function as a transformation of \( \frac{1}{t+2} \):
- As \( t \to \infty \) or \( t \to -\infty \), \( f(t) \to 3 \).
- The term \( \frac{7}{t+2} \) can take any non-zero real value because \( t+2 \) can be any real number except \( 0 \).
- Specifically:
  - If \( t > -2 \), then \( t+2 > 0 \), so \( \frac{7}{t+2} \in (0, \infty) \), meaning \( 3 - \frac{7}{t+2} \in (-\infty, 3) \).
  - If \( t < -2 \), then \( t+2 < 0 \), so \( \frac{7}{t+2} \in (-\infty, 0) \), meaning \( 3 - \frac{7}{t+2} \in (3, \infty) \).

Therefore, \( f(t) \) can take any real value except \( 3 \).
The range is \( \mathbb{R} \setminus \{3\} \) or \( (-\infty, 3) \cup (3, \infty) \).
</details>

29. 🔴 ⭐ Find range of (sin θ − 1)/(sin θ + 1).
<details>
<summary>Solution</summary>

Let \( t = \sin\theta \). For the expression to be defined, \( \sin\theta \ne -1 \), so \( t \in (-1, 1] \).
The expression is:
\[ f(t) = \frac{t - 1}{t + 1} \]

Rewrite the numerator:
\[ f(t) = \frac{(t + 1) - 2}{t + 1} = 1 - \frac{2}{t + 1} \]

Since \( -1 < t \le 1 \):
\[ 0 < t + 1 \le 2 \]

Taking reciprocals of these positive quantities:
\[ \frac{1}{t + 1} \ge \frac{1}{2} \]

Multiplying by \(-2\) (reversing the inequality):
\[ -\frac{2}{t + 1} \le -1 \]

Adding \(1\):
\[ 1 - \frac{2}{t + 1} \le 1 - 1 \implies f(t) \le 0 \]

Since \( t + 1 > 0 \), the term \( -\frac{2}{t+1} \) is negative and can become arbitrarily large in magnitude as \( t \to -1^+ \). Thus, \( f(t) \to -\infty \).

Therefore, the range is \( (-\infty, 0] \).
</details>

30. 🔴 Find range of (sec θ + tan θ)/(sec θ − tan θ).
<details>
<summary>Solution</summary>

Recall the fundamental identity:
\[ \sec^2\theta - \tan^2\theta = 1 \implies (\sec\theta + \tan\theta)(\sec\theta - \tan\theta) = 1 \]
\[ \implies \sec\theta - \tan\theta = \frac{1}{\sec\theta + \tan\theta} \]

Let \( x = \sec\theta + \tan\theta \).
Since \( x = \frac{1+\sin\theta}{\cos\theta} \), for \( \theta \ne \frac{\pi}{2} + k\pi \), \( x \) can take any non-zero real value: \( x \in \mathbb{R} \setminus \{0\} \).
Substitute this into the expression:
\[ f(\theta) = \frac{\sec\theta + \tan\theta}{\sec\theta - \tan\theta} = \frac{x}{1/x} = x^2 \]

Since \( x \) can be any non-zero real number, \( x^2 \) can take any positive real value:
\[ x^2 \in (0, \infty) \]

Thus, the range is \( (0, \infty) \).
</details>

---

### Type 7: Conditional Max/Min with A+B+C = π

**Goal:** Find max/min under triangle angle conditions.

**Solved Example:**

In a triangle ABC, find the maximum value of sin A + sin B + sin C.

**Solution:**
```
For a fixed sum A+B+C = π, sin A + sin B + sin C is maximum when A = B = C = π/3
Maximum = 3 sin(π/3) = 3√3/2
```
🔴 Hard

---

**Practice Problems:**

31. 🔴 In a triangle, find max of cos A + cos B + cos C.
<details>
<summary>Solution</summary>

Let \( f = \cos A + \cos B + \cos C \) where \( A, B, C > 0 \) and \( A + B + C = \pi \).
Using sum-to-product identities:
\[ \cos A + \cos B = 2\cos\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right) = 2\sin\left(\frac{C}{2}\right)\cos\left(\frac{A-B}{2}\right) \]
And:
\[ \cos C = 1 - 2\sin^2\left(\frac{C}{2}\right) \]

Substitute these back:
\[ f = 2\sin\left(\frac{C}{2}\right)\cos\left(\frac{A-B}{2}\right) + 1 - 2\sin^2\left(\frac{C}{2}\right) \]

Since \( \cos\left(\frac{A-B}{2}\right) \le 1 \) and \( \sin\left(\frac{C}{2}\right) > 0 \) (as \( 0 < C < \pi \)):
\[ f \le -2\sin^2\left(\frac{C}{2}\right) + 2\sin\left(\frac{C}{2}\right) + 1 \]

Let \( x = \sin\left(\frac{C}{2}\right) \). We want to maximize the quadratic \( g(x) = -2x^2 + 2x + 1 \):
\[ g(x) = -2\left(x^2 - x\right) + 1 = -2\left(x - \frac{1}{2}\right)^2 + \frac{1}{2} + 1 = -2\left(x - \frac{1}{2}\right)^2 + \frac{3}{2} \]

The maximum value of this quadratic is \( \frac{3}{2} \), which is achieved when:
- \( x = \sin\left(\frac{C}{2}\right) = \frac{1}{2} \implies \frac{C}{2} = \frac{\pi}{6} \implies C = \frac{\pi}{3} \)
- \( \cos\left(\frac{A-B}{2}\right) = 1 \implies A = B \)

Since \( A + B + C = \pi \), this gives \( A = B = C = \frac{\pi}{3} \) (an equilateral triangle).

Thus, the maximum value is \( \frac{3}{2} \).
</details>

32. 🔴 In a triangle, find max of sin A sin B sin C.
<details>
<summary>Solution</summary>

Let \( P = \sin A \sin B \sin C \) where \( A, B, C > 0 \) and \( A+B+C = \pi \).
Since \( A, B, C \in (0, \pi) \), the function \( f(x) = \ln(\sin x) \) is defined because \( \sin x > 0 \).
Let us find the second derivative of \( f(x) = \ln(\sin x) \):
\[ f'(x) = \cot x \]
\[ f''(x) = -\csc^2 x \]

Since \( f''(x) < 0 \) for all \( x \in (0, \pi) \), \( \ln(\sin x) \) is strictly concave on this interval.
Applying Jensen's Inequality:
\[ \frac{\ln(\sin A) + \ln(\sin B) + \ln(\sin C)}{3} \le \ln\left(\sin\left(\frac{A+B+C}{3}\right)\right) \]
\[ \frac{\ln(\sin A \sin B \sin C)}{3} \le \ln\left(\sin\left(\frac{\pi}{3}\right)\right) = \ln\left(\frac{\sqrt{3}}{2}\right) \]
\[ \ln(\sin A \sin B \sin C) \le 3\ln\left(\frac{\sqrt{3}}{2}\right) = \ln\left(\left(\frac{\sqrt{3}}{2}\right)^3\right) \]

Exponentiating both sides:
\[ \sin A \sin B \sin C \le \frac{3\sqrt{3}}{8} \]

Equality holds when \( A = B = C = \frac{\pi}{3} \).
Thus, the maximum value is \( \frac{3\sqrt{3}}{8} \).
</details>

33. 🔴 ⭐ In a triangle, find max of tan A + tan B + tan C.
<details>
<summary>Solution</summary>

In any triangle \( ABC \) (where no angle is \( 90^\circ \)), we have the identity:
\[ \tan A + \tan B + \tan C = \tan A \tan B \tan C \]

We must consider different types of triangles:
1. **Obtuse Triangles**:
   If one of the angles (say \( A \)) is obtuse, then \( \tan A < 0 \) and \( \tan B, \tan C > 0 \). The product \( \tan A \tan B \tan C \) (and hence the sum) is negative. The sum can approach \( -\infty \) as \( A \to \frac{\pi}{2}^+ \).
   
2. **Acute Triangles**:
   If the triangle is acute, \( \tan A, \tan B, \tan C > 0 \).
   Using the AM-GM inequality on their sum:
   \[ \frac{\tan A + \tan B + \tan C}{3} \ge \sqrt[3]{\tan A \tan B \tan C} \]
   Substitute \( \tan A \tan B \tan C = \tan A + \tan B + \tan C \):
   \[ \frac{\tan A + \tan B + \tan C}{3} \ge \sqrt[3]{\tan A + \tan B + \tan C} \]
   Let \( S = \tan A + \tan B + \tan C > 0 \). Then:
   \[ \frac{S}{3} \ge S^{1/3} \implies S^{2/3} \ge 3 \implies S^2 \ge 27 \implies S \ge 3\sqrt{3} \]
   Thus, for acute triangles, the minimum value is \( 3\sqrt{3} \) (occurring when \( A = B = C = \frac{\pi}{3} \)).
   However, we can make one of the angles arbitrarily close to \( \frac{\pi}{2} \) from below, which makes its tangent approach \( +\infty \).

Therefore:
- There is **no maximum value** (the sum is unbounded above, i.e., it can approach \( \infty \)).
- For an acute triangle, the **minimum** value is \( 3\sqrt{3} \).
</details>

34. 🔴 If A+B+C = π, find max of sin²A + sin²B + sin²C.
<details>
<summary>Solution</summary>

We rewrite the expression in terms of cosines using the identity \( \sin^2 x = \frac{1-\cos 2x}{2} \):
\[ S = \sin^2 A + \sin^2 B + \sin^2 C \]
\[ = \frac{1 - \cos 2A}{2} + \frac{1 - \cos 2B}{2} + 1 - \cos^2 C \]
\[ = 2 - \frac{1}{2}(\cos 2A + \cos 2B) - \cos^2 C \]

Using the sum-to-product identity:
\[ \cos 2A + \cos 2B = 2\cos(A+B)\cos(A-B) = 2\cos(\pi-C)\cos(A-B) = -2\cos C\cos(A-B) \]

Substitute this back:
\[ S = 2 - \frac{1}{2}(-2\cos C\cos(A-B)) - \cos^2 C \]
\[ = 2 + \cos C\cos(A-B) - \cos^2 C \]

To maximize this expression, we should maximize \( \cos(A-B) \). Since \( \cos(A-B) \le 1 \), and assuming \( \cos C > 0 \) to get the maximum value:
\[ S \le 2 + \cos C - \cos^2 C \]

Let \( x = \cos C \). We maximize the quadratic \( g(x) = -x^2 + x + 2 \):
\[ g(x) = -\left(x^2 - x\right) + 2 = -\left(x - \frac{1}{2}\right)^2 + \frac{1}{4} + 2 = -\left(x - \frac{1}{2}\right)^2 + \frac{9}{4} \]

The maximum value of the quadratic is \( \frac{9}{4} \), which occurs when:
- \( \cos C = \frac{1}{2} \implies C = \frac{\pi}{3} \)
- \( \cos(A-B) = 1 \implies A = B \)

Since \( A+B+C = \pi \), this gives \( A = B = C = \frac{\pi}{3} \).

Thus, the maximum value of \( \sin^2 A + \sin^2 B + \sin^2 C \) is \( \frac{9}{4} \).
</details>

35. 🔴 If A+B = 45°, find max of sin A sin B.
<details>
<summary>Solution</summary>

We use the product-to-sum formula:
\[ \sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)] \]

Since \( A+B = 45^\circ \):
\[ \sin A \sin B = \frac{1}{2}\left[\cos(A-B) - \cos 45^\circ\right] = \frac{1}{2}\left[\cos(A-B) - \frac{1}{\sqrt{2}}\right] \]

To maximize this expression, we must maximize \( \cos(A-B) \).
The maximum value of \( \cos(A-B) \) is \( 1 \), which occurs when \( A - B = 0 \implies A = B \).
Since \( A+B = 45^\circ \), this occurs when \( A = B = 22.5^\circ \).

Substitute \( \cos(A-B) = 1 \):
\[ \text{Maximum value} = \frac{1}{2}\left[1 - \frac{1}{\sqrt{2}}\right] = \frac{\sqrt{2}-1}{2\sqrt{2}} = \frac{2-\sqrt{2}}{4} \]
</details>

---

### Type 8: Using Graph-Based Insight

**Goal:** Visual max/min without heavy algebra.

**Solved Example:**

Find max of |sin x| + |cos x|.

**Solution:**
```
For x in QI, f = sin x + cos x = √2 sin(x + π/4), max = √2
Similarly in each quadrant, the max is √2.
So overall max = √2.
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Find max of |sin x| − |cos x|.
<details>
<summary>Solution</summary>

We know that for any real \( x \):
- \( |\sin x| \le 1 \)
- \( |\cos x| \ge 0 \)

Therefore, the difference:
\[ |\sin x| - |\cos x| \le 1 - 0 = 1 \]

Equality is achieved when \( |\sin x| = 1 \) and \( |\cos x| = 0 \), which occurs at \( x = \frac{\pi}{2} + k\pi \).
Thus, the maximum value is \( 1 \).
</details>

37. 🟡 Find max of sin²x + cos⁴x.
<details>
<summary>Solution</summary>

Using the identity \( \sin^2 x = 1 - \cos^2 x \), we can write the expression as:
\[ f(x) = 1 - \cos^2 x + \cos^4 x = \cos^4 x - \cos^2 x + 1 \]

Let \( t = \cos^2 x \). Since \( x \) is real, \( t \in [0, 1] \).
We analyze the quadratic \( g(t) = t^2 - t + 1 \) on \( [0, 1] \):
- **Vertex**: \( t = -\frac{b}{2a} = \frac{1}{2} \). The value is \( g(1/2) = 1/4 - 1/2 + 1 = 3/4 \).
- **Endpoints**:
  - At \( t = 0 \): \( g(0) = 1 \)
  - At \( t = 1 \): \( g(1) = 1 \)

Comparing these, the maximum value is \( 1 \).
</details>

38. 🔴 Find max of sin x cos 2x.
<details>
<summary>Solution</summary>

Let \( f(x) = \sin x \cos 2x \).
Using the identity \( \cos 2x = 1 - 2\sin^2 x \):
\[ f(x) = \sin x (1 - 2\sin^2 x) = \sin x - 2\sin^3 x \]

Let \( t = \sin x \). Since \( x \in \mathbb{R} \), \( t \in [-1, 1] \).
We want to maximize the function \( g(t) = t - 2t^3 \) on \( [-1, 1] \):
Differentiate \( g(t) \):
\[ g'(t) = 1 - 6t^2 \]
Set \( g'(t) = 0 \implies t^2 = \frac{1}{6} \implies t = \pm\frac{1}{\sqrt{6}} \).

Let's evaluate \( g(t) \) at the critical points and endpoints:
1. **At critical point** \( t = \frac{1}{\sqrt{6}} \):
   \[ g\left(\frac{1}{\sqrt{6}}\right) = \frac{1}{\sqrt{6}} - 2\left(\frac{1}{6\sqrt{6}}\right) = \frac{1}{\sqrt{6}} - \frac{1}{3\sqrt{6}} = \frac{2}{3\sqrt{6}} = \frac{\sqrt{6}}{9} \approx 0.272 \]
   
2. **At critical point** \( t = -\frac{1}{\sqrt{6}} \):
   \[ g\left(-\frac{1}{\sqrt{6}}\right) = -\frac{\sqrt{6}}{9} \approx -0.272 \]

3. **At endpoint** \( t = 1 \):
   \[ g(1) = 1 - 2(1)^3 = -1 \]

4. **At endpoint** \( t = -1 \):
   \[ g(-1) = -1 - 2(-1)^3 = -1 + 2 = 1 \]

Comparing these values, the maximum is \( 1 \) (which is achieved when \( \sin x = -1 \implies x = \frac{3\pi}{2} + 2k\pi \)).
</details>

39. 🔴 ⭐ Find max of sin³x + cos³x for x ∈ [0, π/2].
<details>
<summary>Solution</summary>

Let \( f(x) = \sin^3 x + \cos^3 x \) for \( x \in [0, \pi/2] \).
Let's find the derivative:
\[ f'(x) = 3\sin^2 x \cos x - 3\cos^2 x \sin x = 3\sin x \cos x (\sin x - \cos x) \]

For \( x \in [0, \pi/2] \):
- \( 3\sin x \cos x \ge 0 \)
- \( \sin x - \cos x \) is:
  - negative for \( x \in [0, \pi/4) \)
  - zero at \( x = \pi/4 \)
  - positive for \( x \in (\pi/4, \pi/2] \)

Thus, \( f(x) \) decreases on \( [0, \pi/4] \) and increases on \( [\pi/4, \pi/2] \).
- The minimum occurs at \( x = \frac{\pi}{4} \):
  \[ f\left(\frac{\pi}{4}\right) = \left(\frac{1}{\sqrt{2}}\right)^3 + \left(\frac{1}{\sqrt{2}}\right)^3 = \frac{1}{2\sqrt{2}} + \frac{1}{2\sqrt{2}} = \frac{1}{\sqrt{2}} \]
- The maximum must occur at the boundaries:
  - At \( x = 0 \): \( f(0) = 0 + 1 = 1 \)
  - At \( x = \frac{\pi}{2} \): \( f\left(\frac{\pi}{2}\right) = 1 + 0 = 1 \)

Thus, the maximum value is \( 1 \).
</details>

40. 🔴 Find min of (sin x + cosec x)² + (cos x + sec x)².
<details>
<summary>Solution</summary>

Expand the terms:
\[ f(x) = (\sin x + \csc x)^2 + (\cos x + \sec x)^2 \]
\[ = \sin^2 x + \csc^2 x + 2\sin x \csc x + \cos^2 x + \sec^2 x + 2\cos x \sec x \]

Since \( \sin x \csc x = 1 \) and \( \cos x \sec x = 1 \):
\[ f(x) = \sin^2 x + \csc^2 x + 2 + \cos^2 x + \sec^2 x + 2 \]
\[ = (\sin^2 x + \cos^2 x) + \csc^2 x + \sec^2 x + 4 \]
\[ = 5 + \csc^2 x + \sec^2 x \]

Rewrite \( \csc^2 x + \sec^2 x \) in terms of sines and cosines:
\[ \csc^2 x + \sec^2 x = \frac{1}{\sin^2 x} + \frac{1}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\sin^2 x \cos^2 x} = \frac{1}{\sin^2 x \cos^2 x} \]
\[ = \frac{4}{(2\sin x \cos x)^2} = \frac{4}{\sin^2 2x} \]

Substitute this back:
\[ f(x) = 5 + \frac{4}{\sin^2 2x} \]

To minimize \( f(x) \), we maximize \( \sin^2 2x \). The maximum value of \( \sin^2 2x \) is \( 1 \) (when \( 2x = \frac{\pi}{2} + k\pi \)).
Thus:
\[ \text{Minimum value} = 5 + \frac{4}{1} = 9 \]
</details>

---

## Stage 4: Type Mixer

1. 🟡 Find the maximum of f(θ) = 5 sin θ + 12 cos θ + 3.

2. 🔴 Find the minimum of tan²θ + cot²θ.

3. 🔴 ⭐ Find the maximum of sin θ cos θ sin 2θ.

4. 🔴 Find the range of f(θ) = (sin θ + 1)/(sin θ − 2).

5. 🔴 In a triangle ABC, find the maximum value of cos A + cos B + cos C.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the maximum and minimum of 3 cos θ + 4 sin θ. **(2 marks)**

**Solution:**
```
R = √(3²+4²) = 5
Max = 5, Min = −5
```

---

**Q2.** 🟡 Find the range of f(θ) = 2 + 3 sin θ. **(2 marks)**

**Solution:**
```
−1 ≤ sin θ ≤ 1
−3 ≤ 3 sin θ ≤ 3
−1 ≤ 2 + 3 sin θ ≤ 5
Range: [−1, 5]
```

---

**Q3.** 🟡 Find the minimum of sin θ + cosec θ for θ ∈ (0, π/2). **(2 marks)**

**Solution:**
```
AM ≥ GM: sin θ + cosec θ ≥ 2√(sin θ × cosec θ) = 2
Minimum = 2 (at sin θ = 1 → θ = π/2... wait, that's at the endpoint)

Actually, by AM-GM: (sin θ + 1/sin θ)/2 ≥ √(sin θ × 1/sin θ) = 1
sin θ + 1/sin θ ≥ 2
Minimum = 2 (at sin θ = 1, i.e., θ = π/2)
```

---

**Q4.** 🔴 ⭐ Find the range of (2 sin θ − 1)/(sin θ + 3). **(3 marks)**

**Solution:**
```
Let t = sin θ, t ∈ [−1, 1]
f(t) = (2t − 1)/(t + 3)

Cross multiply: f(t+3) = 2t−1
ft + 3f = 2t − 1
ft − 2t = −1 − 3f
t(f − 2) = −(1 + 3f)
t = −(1 + 3f)/(f − 2)

−1 ≤ −(1+3f)/(f−2) ≤ 1
Solving gives f ∈ [−3/4, 3/2]
```

---

## Stage 6: JEE Mains Arena

**Q1.** The maximum value of sin θ + cos θ is:
(a) 1
(b) √2
(c) 2
(d) √3

<details>
<summary>Solution</summary>
sin θ + cos θ = √2 sin(θ + π/4), max = √2
Answer: (b) 🟢 ⭐
</details>

---

**Q2.** The minimum value of 4 sin²θ + 5 cos²θ is:
(a) 0
(b) 4
(c) 5
(d) 1

<details>
<summary>Solution</summary>
= 4 sin²θ + 5 cos²θ = 4(sin²θ + cos²θ) + cos²θ = 4 + cos²θ
Since cos²θ ≥ 0, minimum = 4
Answer: (b) 🟡
</details>

---

**Q3.** The maximum value of 3 sin θ − 4 cos θ is:
(a) 3
(b) 4
(c) 5
(d) 7

<details>
<summary>Solution</summary>
R = √(3²+4²) = 5
Answer: (c) 🟢
</details>

---

**Q4.** The minimum value of tan θ + cot θ is:
(a) 0
(b) 1
(c) 2
(d) 4

<details>
<summary>Solution</summary>
tan θ + cot θ ≥ 2√(tan θ × cot θ) = 2
Minimum = 2
Answer: (c) 🟡 ⭐
</details>

---

**Q5.** The range of sin⁴θ + cos⁴θ is:
(a) [0, 1]
(b) [1/2, 1]
(c) [0, 1/2]
(d) [1/2, 1]

<details>
<summary>Solution</summary>
sin⁴θ + cos⁴θ = 1 − 2 sin²θ cos²θ = 1 − (1/2) sin²2θ
sin²2θ ∈ [0, 1], so expression ∈ [1/2, 1]
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** Maximum of sin θ is 1.
**Reason (R):** sin θ ≤ 1 for all real θ.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** Minimum of 3 − 2 sin θ is 1.
**Reason (R):** −2 ≤ −2 sin θ ≤ 2, so 1 ≤ 3 − 2 sin θ ≤ 5.

<details>
<summary>Solution</summary>
A is true (min = 1). R is true and correctly computes the range.
Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The maximum of a sin θ + b cos θ is |a| + |b|.
**Reason (R):** The maximum is √(a² + b²).

<details>
<summary>Solution</summary>
A is false: maximum is √(a²+b²), not |a|+|b|.
R is true.
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The minimum value of sin⁴θ + cos⁴θ is 1/2.
**Reason (R):** sin⁴θ + cos⁴θ = 1 − (1/2) sin²2θ ≥ 1/2.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 Range of sin θ is:
   (a) ℝ   (b) [−1, 1]   (c) [0, 1]   (d) (−1, 1)

2. 🟢 Max of 3 + 2 sin θ is:
   (a) 3   (b) 5   (c) 1   (d) 2

3. 🟡 Max of sin θ + √3 cos θ is:
   (a) 2   (b) √3   (c) √10   (d) 4

4. 🟡 Min of 5 − 3 cos θ is:
   (a) 2   (b) 5   (c) 8   (d) 3

5. 🟡 Max of 4 sin θ + 3 cos θ is:
   (a) 5   (b) 7   (c) 1   (d) 25

6. 🟡 Min of sin²θ + cos²θ is:
   (a) 0   (b) 1   (c) 1/2   (d) 2

7. 🟡 Min of 4 sin²θ + 4 cos²θ is:
   (a) 0   (b) 4   (c) 8   (d) 2

8. 🟡 Min of tan θ + cot θ is:
   (a) 1   (b) 2   (c) 0   (d) −2

9. 🟡 Max of 3 sin²θ + 4 cos²θ is:
   (a) 3   (b) 4   (c) 7   (d) 12

10. 🟡 Min of 3 sin²θ + 4 cos²θ is:
    (a) 3   (b) 4   (c) 7   (d) 0

11. 🟡 Max of sin θ cos θ is:
    (a) 1/2   (b) 1   (c) 1/4   (d) 2

12. 🟡 Range of sin⁴θ + cos⁴θ is:
    (a) [0, 1]   (b) [1/2, 1]   (c) [0, 1/2]   (d) [1/2, 1/2]

13. 🟡 Max of sin θ + cos θ + 3 is:
    (a) √2 + 3   (b) 5   (c) 4   (d) 2 + √3

14. 🟡 Min of sec²θ + cosec²θ is:
    (a) 4   (b) 2   (c) 0   (d) 1

15. 🟡 Max of 2 sin θ − 3 cos θ is:
    (a) √13   (b) 5   (c) 6   (d) √5

16. 🟡 Min of sin⁶θ + cos⁶θ is:
    (a) 0   (b) 1/4   (c) 1/2   (d) 1

17. 🟡 Max of (sin θ + cos θ)² is:
    (a) 1   (b) 2   (c) 4   (d) √2

18. 🟡 Min of 2 sin²θ − sin θ + 1 is:
    (a) 0   (b) 7/8   (c) 1   (d) 3/4

19. 🟡 Range of (sin θ + 1)/(sin θ + 2) is:
    (a) [0, 2/3]   (b) [0, 1]   (c) [2/3, 2]   (d) [1/2, 2]

20. 🟡 Max of sin 2θ − cos 2θ is:
    (a) 1   (b) √2   (c) 2   (d) 0

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | a | 16 | b |
| 2 | b | 7 | b | 12 | b | 17 | b |
| 3 | a | 8 | b | 13 | a | 18 | b |
| 4 | a | 9 | b | 14 | a | 19 | a |
| 5 | a | 10 | a | 15 | a | 20 | b |

</details>
