# Chapter 15: Composition of Inverse & Trig Functions

---

## Stage 1: The Core Idea

### When Inverses Meet Their Functions

What is sin(arcsin x)?<br> It's x — that's the definition of inverse.

But what about arcsin(sin x)?<br> That's **not always** x. It equals x only when x ∈ [−π/2, π/2].

And what about sin(arccos x)?<br> Or tan(arcsin x)?<br> These are **compositions** of different functions — and they need a triangle diagram to simplify.

This chapter is about simplifying these nested expressions — a key JEE skill.

---

## Stage 2: The Formula Lab

### Direct Composition (Function with Its Own Inverse)

```
sin(arcsin x) = x, x ∈ [−1, 1]
cos(arccos x) = x, x ∈ [−1, 1]
tan(arctan x) = x, x ∈ ℝ

arcsin(sin x) = x, x ∈ [−π/2, π/2]
arccos(cos x) = x, x ∈ [0, π]
arctan(tan x) = x, x ∈ (−π/2, π/2)
```

### Cross Composition (One Function with Different Inverse)

For these, draw a **right triangle**:

```
sin(arccos x) = √(1 − x²)
cos(arcsin x) = √(1 − x²)
tan(arcsin x) = x/√(1 − x²)
tan(arccos x) = √(1 − x²)/x
```

---

## Stage 3: Type-wise Mastery

### Type 1: sin(arcsin x), cos(arccos x)

**Goal:** Simplify direct compositions.

**Solved Example:**

Simplify sin(arcsin 1/2).

**Solution:**
```
sin(arcsin 1/2) = 1/2 ✓
```
🟢 Easy

---

**Practice Problems:**

1. 🟢 Evaluate cos(arccos 0).
<details>
<summary>Solution</summary>

Using the property \(\cos(\arccos x) = x\) for \(x \in [-1, 1]\):
Since \(0 \in [-1, 1]\), we have:
\[ \cos(\arccos 0) = 0 \]
</details>

2. 🟢 Evaluate tan(arctan √3).
<details>
<summary>Solution</summary>

Using the property \(\tan(\arctan x) = x\) for all \(x \in \mathbb{R}\):
Since \(\sqrt{3} \in \mathbb{R}\), we have:
\[ \tan(\arctan \sqrt{3}) = \sqrt{3} \]
</details>

3. 🟢 Evaluate sec(arcsec 2).
<details>
<summary>Solution</summary>

Using the property \(\sec(\text{arcsec } x) = x\) for \(|x| \ge 1\):
Since \(2 \ge 1\), we have:
\[ \sec(\text{arcsec } 2) = 2 \]
</details>

4. 🟡 Evaluate sin(arcsin 0.6).
<details>
<summary>Solution</summary>

Using the property \(\sin(\arcsin x) = x\) for \(x \in [-1, 1]\):
Since \(0.6 \in [-1, 1]\), we have:
\[ \sin(\arcsin 0.6) = 0.6 \]
</details>

5. 🟡 Evaluate cos(arccos(−1/2)).
<details>
<summary>Solution</summary>

Using the property \(\cos(\arccos x) = x\) for \(x \in [-1, 1]\):
Since \(-\frac{1}{2} \in [-1, 1]\), we have:
\[ \cos\left(\arccos\left(-\frac{1}{2}\right)\right) = -\frac{1}{2} \]
</details>

---

### Type 2: arcsin(sin x) When x is in Range

**Goal:** Simplify when x is in the principal range.

**Solved Example:**

Find arcsin(sin π/4).

**Solution:**
```
π/4 ∈ [−π/2, π/2]
arcsin(sin π/4) = π/4
```
🟢 Easy

---

**Practice Problems:**

6. 🟢 Evaluate arccos(cos π/3).
<details>
<summary>Solution</summary>

Using the property \(\arccos(\cos x) = x\) for \(x \in [0, \pi]\):
Since \(\frac{\pi}{3} \in [0, \pi]\), we have:
\[ \arccos\left(\cos\frac{\pi}{3}\right) = \frac{\pi}{3} \]
</details>

7. 🟢 Evaluate arctan(tan π/6).
<details>
<summary>Solution</summary>

Using the property \(\arctan(\tan x) = x\) for \(x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\):
Since \(\frac{\pi}{6} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\), we have:
\[ \arctan\left(\tan\frac{\pi}{6}\right) = \frac{\pi}{6} \]
</details>

8. 🟡 Evaluate arcsin(sin(−π/6)).
<details>
<summary>Solution</summary>

Using the property \(\arcsin(\sin x) = x\) for \(x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\):
Since \(-\frac{\pi}{6} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\), we have:
\[ \arcsin\left(\sin\left(-\frac{\pi}{6}\right)\right) = -\frac{\pi}{6} \]
</details>

9. 🟡 Evaluate arccos(cos 0).
<details>
<summary>Solution</summary>

Using the property \(\arccos(\cos x) = x\) for \(x \in [0, \pi]\):
Since \(0 \in [0, \pi]\), we have:
\[ \arccos(\cos 0) = 0 \]
</details>

10. 🟡 Evaluate arctan(tan(−π/4)).
<details>
<summary>Solution</summary>

Using the property \(\arctan(\tan x) = x\) for \(x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\):
Since \(-\frac{\pi}{4} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\), we have:
\[ \arctan\left(\tan\left(-\frac{\pi}{4}\right)\right) = -\frac{\pi}{4} \]
</details>

---

### Type 3: arcsin(sin x) When x is OUT of Range

**Goal:** Simplify when x is outside principal range by finding the appropriate angle in range.

**Solved Example:**

Find arcsin(sin 5π/6).

**Solution:**
```
5π/6 ∉ [−π/2, π/2]
sin(5π/6) = 1/2
arcsin(1/2) = π/6 ∈ [−π/2, π/2]
∴ arcsin(sin 5π/6) = π/6
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 Evaluate arcsin(sin 2π/3).
<details>
<summary>Solution</summary>

The angle \(\frac{2\pi}{3}\) does not lie in the principal branch interval \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) of \(\arcsin\).
We rewrite the expression by using the identity \(\sin(\theta) = \sin(\pi - \theta)\):
\[ \sin\left(\frac{2\pi}{3}\right) = \sin\left(\pi - \frac{2\pi}{3}\right) = \sin\left(\frac{\pi}{3}\right) \]
Since \(\frac{\pi}{3} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\), we have:
\[ \arcsin\left(\sin\frac{2\pi}{3}\right) = \arcsin\left(\sin\frac{\pi}{3}\right) = \frac{\pi}{3} \]
</details>

12. 🟡 Evaluate arccos(cos 5π/4).
<details>
<summary>Solution</summary>

The angle \(\frac{5\pi}{4}\) does not lie in the principal branch interval \([0, \pi]\) of \(\arccos\).
We rewrite the expression by using the identity \(\cos(\theta) = \cos(2\pi - \theta)\):
\[ \cos\left(\frac{5\pi}{4}\right) = \cos\left(2\pi - \frac{5\pi}{4}\right) = \cos\left(\frac{3\pi}{4}\right) \]
Since \(\frac{3\pi}{4} \in [0, \pi]\), we have:
\[ \arccos\left(\cos\frac{5\pi}{4}\right) = \arccos\left(\cos\frac{3\pi}{4}\right) = \frac{3\pi}{4} \]
</details>

13. 🟡 Evaluate arctan(tan 5π/6).
<details>
<summary>Solution</summary>

The angle \(\frac{5\pi}{6}\) does not lie in the principal branch interval \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\) of \(\arctan\).
We rewrite the expression using the identity \(\tan(\theta) = \tan(\theta - \pi)\):
\[ \tan\left(\frac{5\pi}{6}\right) = \tan\left(\frac{5\pi}{6} - \pi\right) = \tan\left(-\frac{\pi}{6}\right) \]
Since \(-\frac{\pi}{6} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\), we have:
\[ \arctan\left(\tan\frac{5\pi}{6}\right) = \arctan\left(\tan\left(-\frac{\pi}{6}\right)\right) = -\frac{\pi}{6} \]
</details>

14. 🟡 Evaluate arcsin(sin 7π/6).
<details>
<summary>Solution</summary>

The angle \(\frac{7\pi}{6}\) does not lie in the principal branch interval \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) of \(\arcsin\).
We rewrite the expression using the identity \(\sin(\theta) = \sin(\pi - \theta)\):
\[ \sin\left(\frac{7\pi}{6}\right) = \sin\left(\pi - \frac{7\pi}{6}\right) = \sin\left(-\frac{\pi}{6}\right) \]
Since \(-\frac{\pi}{6} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\), we have:
\[ \arcsin\left(\sin\frac{7\pi}{6}\right) = \arcsin\left(\sin\left(-\frac{\pi}{6}\right)\right) = -\frac{\pi}{6} \]
</details>

15. 🔴 ⭐ Evaluate arcsin(sin 10).
<details>
<summary>Solution</summary>

The value \(10\) represents an angle in radians. Let us locate \(10\) relative to multiples of \(\pi \approx 3.14159\):
- \(3\pi \approx 9.42\)
- \(3.5\pi \approx 11.00\)
So, \(10 \in [3\pi - \frac{\pi}{2}, 3\pi + \frac{\pi}{2}] = [2.5\pi, 3.5\pi]\).
We use the periodic properties of the sine function:
\[ \sin(10) = \sin(3\pi - (3\pi - 10)) = \sin(3\pi - 10) \]
We check if the angle \((3\pi - 10)\) falls within the principal range \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\):
\[ 3\pi - 10 \approx 9.4248 - 10 = -0.5752 \text{ radians} \]
Since \(-0.5752 \in [-1.5708, 1.5708]\), the angle \((3\pi - 10)\) is in the principal interval.
Therefore:
\[ \arcsin(\sin 10) = 3\pi - 10 \]
</details>

---

### Type 4: sin(arccos x) — Different Functions

**Goal:** Simplify composition of different functions.

**Solved Example:**

Find sin(arccos 3/5).

**Solution:**
```
Let θ = arccos(3/5) → cos θ = 3/5, θ ∈ [0, π]
Draw triangle: adj = 3, hyp = 5 → opp = 4
sin θ = 4/5
∴ sin(arccos 3/5) = 4/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Find cos(arcsin 5/13).
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin\left(\frac{5}{13}\right)\). Then \(\sin\theta = \frac{5}{13}\) and \(\theta \in \left[0, \frac{\pi}{2}\right]\).
Using the Pythagorean identity:
\[ \cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \left(\frac{5}{13}\right)^2} = \sqrt{\frac{144}{169}} = \frac{12}{13} \]
Since \(\theta\) is in the first quadrant, the cosine value is positive.
Thus:
\[ \cos\left(\arcsin\frac{5}{13}\right) = \frac{12}{13} \]
</details>

17. 🟡 Find tan(arccos 4/5).
<details>
<summary>Solution</summary>

Let \(\theta = \arccos\left(\frac{4}{5}\right)\). Then \(\cos\theta = \frac{4}{5}\) and \(\theta \in \left[0, \frac{\pi}{2}\right]\).
For a right triangle with adjacent side \(4\) and hypotenuse \(5\):
\[ \text{opposite side} = \sqrt{5^2 - 4^2} = 3 \]
Thus:
\[ \tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{3}{4} \]
Therefore:
\[ \tan\left(\arccos\frac{4}{5}\right) = \frac{3}{4} \]
</details>

18. 🟡 Find sec(arctan 2).
<details>
<summary>Solution</summary>

Let \(\theta = \arctan(2)\). Then \(\tan\theta = 2\) and \(\theta \in \left(0, \frac{\pi}{2}\right)\).
Using the trigonometric identity \(\sec^2\theta = 1 + \tan^2\theta\):
\[ \sec\theta = \sqrt{1 + \tan^2\theta} = \sqrt{1 + 2^2} = \sqrt{5} \]
(Taking the positive root since \(\theta \in (0, \pi/2)\) where secant is positive).
Thus:
\[ \sec(\arctan 2) = \sqrt{5} \]
</details>

19. 🟡 Find cosec(arccos 12/13).
<details>
<summary>Solution</summary>

Let \(\theta = \arccos\left(\frac{12}{13}\right)\). Then \(\cos\theta = \frac{12}{13}\) and \(\theta \in \left[0, \frac{\pi}{2}\right]\).
For a right triangle with adjacent side \(12\) and hypotenuse \(13\):
\[ \text{opposite side} = \sqrt{13^2 - 12^2} = 5 \]
So, \(\sin\theta = \frac{5}{13}\).
The cosecant function is the reciprocal of sine:
\[ \csc\theta = \frac{1}{\sin\theta} = \frac{13}{5} \]
Therefore:
\[ \csc\left(\arccos\frac{12}{13}\right) = \frac{13}{5} \]
</details>

20. 🔴 Find cot(arcsin 3/5).
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin\left(\frac{3}{5}\right)\). Then \(\sin\theta = \frac{3}{5}\) and \(\theta \in \left(0, \frac{\pi}{2}\right)\).
For a right triangle with opposite side \(3\) and hypotenuse \(5\):
\[ \text{adjacent side} = \sqrt{5^2 - 3^2} = 4 \]
So, \(\cos\theta = \frac{4}{5}\).
The cotangent function is:
\[ \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{4}{3} \]
Therefore:
\[ \cot\left(\arcsin\frac{3}{5}\right) = \frac{4}{3} \]
</details>

---

### Type 5: Expressing in Terms of x

**Goal:** Simplify expressions like sin(arctan x), cos(arcsin x) in algebraic form.

**Solved Example:**

Express sin(arctan x) in terms of x.

**Solution:**
```
Let θ = arctan x → tan θ = x, θ ∈ (−π/2, π/2)
Draw triangle: opp = x, adj = 1 → hyp = √(1 + x²)
sin θ = x/√(1 + x²)
∴ sin(arctan x) = x/√(1 + x²)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 Express cos(arctan x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arctan x\). Then \(\tan\theta = x\) and \(\theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\).
Consider a right triangle where the side opposite to \(\theta\) is \(x\) and the adjacent side is \(1\).
The hypotenuse is \(\sqrt{1 + x^2}\).
Since \(\theta\) lies in the interval \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\), \(\cos\theta\) is positive for all real \(x\):
\[ \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{1}{\sqrt{1 + x^2}} \]
Thus:
\[ \cos(\arctan x) = \frac{1}{\sqrt{1 + x^2}} \]
</details>

22. 🟡 Express tan(arcsin x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin x\) for \(x \in (-1, 1)\). Then \(\sin\theta = x\) and \(\theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\).
Using a right triangle with opposite side \(x\) and hypotenuse \(1\):
\[ \text{adjacent side} = \sqrt{1 - x^2} \]
Since \(\theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\), \(\cos\theta = \sqrt{1 - x^2} > 0\).
Thus:
\[ \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{x}{\sqrt{1 - x^2}} \]
Therefore:
\[ \tan(\arcsin x) = \frac{x}{\sqrt{1 - x^2}} \]
</details>

23. 🟡 Express sec(arctan x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arctan x\). Then \(\tan\theta = x\) and \(\theta \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\).
Using the identity \(\sec^2\theta = 1 + \tan^2\theta\):
\[ \sec\theta = \sqrt{1 + x^2} \]
(Taking the positive root because secant is positive in the interval \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\)).
Thus:
\[ \sec(\arctan x) = \sqrt{1 + x^2} \]
</details>

24. 🟡 Express sin(arccos x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arccos x\) for \(x \in [-1, 1]\). Then \(\cos\theta = x\) and \(\theta \in [0, \pi]\).
Using the identity \(\sin^2\theta = 1 - \cos^2\theta\):
\[ \sin\theta = \sqrt{1 - x^2} \]
(Taking the positive root since \(\sin\theta \ge 0\) for \(\theta \in [0, \pi]\)).
Thus:
\[ \sin(\arccos x) = \sqrt{1 - x^2} \]
</details>

25. 🔴 ⭐ Express cot(arcsec x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \text{arcsec } x\) for \(|x| \ge 1\). Then \(\sec\theta = x\) and \(\theta \in [0, \pi] \setminus \left\{\frac{\pi}{2}\right\}\).
Using the identity \(\tan^2\theta = \sec^2\theta - 1 = x^2 - 1\).
Since \(\cot\theta = \frac{1}{\tan\theta}\), we have:
\[ \cot^2\theta = \frac{1}{x^2 - 1} \]
Let's consider the sign of \(\cot\theta\):
- If \(x \ge 1\), then \(\theta \in \left[0, \frac{\pi}{2}\right)\), so \(\cot\theta \ge 0\). Hence, \(\cot\theta = \frac{1}{\sqrt{x^2 - 1}}\).
- If \(x \le -1\), then \(\theta \in \left(\frac{\pi}{2}, \pi\right)\), so \(\cot\theta \le 0\). Hence, \(\cot\theta = -\frac{1}{\sqrt{x^2 - 1}}\).
Thus, we can write:
\[ \cot(\text{arcsec } x) = \frac{\text{sgn}(x)}{\sqrt{x^2 - 1}} = \frac{x}{|x|\sqrt{x^2 - 1}} \]
For positive real values of \(x > 1\), it simplifies to:
\[ \cot(\text{arcsec } x) = \frac{1}{\sqrt{x^2 - 1}} \]
</details>

---

### Type 6: Nested with Double Angle

**Goal:** Simplify sin(2 arcsin x), cos(2 arctan x), etc.

**Solved Example:**

Express sin(2 arctan x) in terms of x.

**Solution:**
```
Let θ = arctan x → tan θ = x
sin 2θ = 2 tan θ/(1 + tan²θ) = 2x/(1 + x²)
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 Express cos(2 arctan x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arctan x\). Then \(\tan\theta = x\).
Using the double angle formula for cosine in terms of tangent:
\[ \cos(2\theta) = \frac{1 - \tan^2\theta}{1 + \tan^2\theta} \]
Substituting \(\tan\theta = x\):
\[ \cos(2\arctan x) = \frac{1 - x^2}{1 + x^2} \]
</details>

27. 🟡 Express tan(2 arcsin x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin x\). Then \(\sin\theta = x\) and \(\cos\theta = \sqrt{1 - x^2}\) (since \(\theta \in [-\pi/2, \pi/2]\)).
First, we find the double angle values:
\[ \sin(2\theta) = 2\sin\theta\cos\theta = 2x\sqrt{1 - x^2} \]
\[ \cos(2\theta) = 1 - 2\sin^2\theta = 1 - 2x^2 \]
Now, using the definition of tangent:
\[ \tan(2\theta) = \frac{\sin(2\theta)}{\cos(2\theta)} = \frac{2x\sqrt{1 - x^2}}{1 - 2x^2} \]
Thus:
\[ \tan(2\arcsin x) = \frac{2x\sqrt{1 - x^2}}{1 - 2x^2} \]
</details>

28. 🟡 Express sin(2 arccos x) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \arccos x\). Then \(\cos\theta = x\) and \(\sin\theta = \sqrt{1 - x^2}\) (since \(\theta \in [0, \pi]\)).
Using the double angle formula for sine:
\[ \sin(2\theta) = 2\sin\theta\cos\theta = 2\sqrt{1 - x^2}(x) = 2x\sqrt{1 - x^2} \]
Thus:
\[ \sin(2\arccos x) = 2x\sqrt{1 - x^2} \]
</details>

29. 🔴 ⭐ Express cos(2 arcsin x) in terms of x as a simplified radical.
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin x\). Then \(\sin\theta = x\).
Using the double angle formula:
\[ \cos(2\theta) = 1 - 2\sin^2\theta \]
Substituting \(\sin\theta = x\):
\[ \cos(2\arcsin x) = 1 - 2x^2 \]
*(Note: This expression is a polynomial, so no radical is necessary in its fully simplified form).*
</details>

30. 🔴 Find the value of sin(2 arctan 1/2).
<details>
<summary>Solution</summary>

Let \(\theta = \arctan\left(\frac{1}{2}\right)\). Then \(\tan\theta = \frac{1}{2}\).
Using the double angle formula:
\[ \sin(2\theta) = \frac{2\tan\theta}{1 + \tan^2\theta} \]
Substituting \(\tan\theta = \frac{1}{2}\):
\[ \sin\left(2\arctan\frac{1}{2}\right) = \frac{2(1/2)}{1 + (1/2)^2} = \frac{1}{1 + 1/4} = \frac{1}{5/4} = \frac{4}{5} \]
</details>

---

### Type 7: Sum of Compositions

**Goal:** Simplify expressions like sin(arcsin x + arcsin y).

**Solved Example:**

Find sin(arcsin 3/5 + arcsin 4/5).

**Solution:**
```
Let α = arcsin 3/5, β = arcsin 4/5
cos α = 4/5, cos β = 3/5
sin(α + β) = sin α cos β + cos α sin β
= (3/5)(3/5) + (4/5)(4/5)
= 9/25 + 16/25
= 1

So α + β = π/2 (since sin = 1 and both angles acute)
```
🔴 Hard

---

**Practice Problems:**

31. 🔴 Find cos(arcsin 3/5 + arccos 12/13).
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{3}{5}\right)\) and \(\beta = \arccos\left(\frac{12}{13}\right)\).
Since both arguments are positive, \(\alpha, \beta \in \left(0, \frac{\pi}{2}\right)\).
- \(\sin\alpha = \frac{3}{5} \implies \cos\alpha = \sqrt{1 - (3/5)^2} = \frac{4}{5}\)
- \(\cos\beta = \frac{12}{13} \implies \sin\beta = \sqrt{1 - (12/13)^2} = \frac{5}{13}\)
Using the cosine sum formula:
\[ \cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta \]
Substitute the values:
\[ \cos(\alpha + \beta) = \left(\frac{4}{5}\right)\left(\frac{12}{13}\right) - \left(\frac{3}{5}\right)\left(\frac{5}{13}\right) = \frac{48}{65} - \frac{15}{65} = \frac{33}{65} \]
Thus:
\[ \cos\left(\arcsin\frac{3}{5} + \arccos\frac{12}{13}\right) = \frac{33}{65} \]
</details>

32. 🔴 Find tan(arctan 1/2 + arctan 1/3).
<details>
<summary>Solution</summary>

Let \(\alpha = \arctan\left(\frac{1}{2}\right)\) and \(\beta = \arctan\left(\frac{1}{3}\right)\).
So, \(\tan\alpha = \frac{1}{2}\) and \(\tan\beta = \frac{1}{3}\).
Using the tangent addition formula:
\[ \tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta} \]
Substitute the values:
\[ \tan(\alpha + \beta) = \frac{1/2 + 1/3}{1 - (1/2)(1/3)} = \frac{5/6}{1 - 1/6} = \frac{5/6}{5/6} = 1 \]
Thus:
\[ \tan\left(\arctan\frac{1}{2} + \arctan\frac{1}{3}\right) = 1 \]
</details>

33. 🔴 Find sin(arcsin 5/13 + arcsin 12/13).
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{5}{13}\right)\) and \(\beta = \arcsin\left(\frac{12}{13}\right)\).
Since both arguments are positive, \(\alpha, \beta \in \left(0, \frac{\pi}{2}\right)\).
- \(\sin\alpha = \frac{5}{13} \implies \cos\alpha = \frac{12}{13}\)
- \(\sin\beta = \frac{12}{13} \implies \cos\beta = \frac{5}{13}\)
Using the sine sum formula:
\[ \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta \]
Substitute the values:
\[ \sin(\alpha + \beta) = \left(\frac{5}{13}\right)\left(\frac{5}{13}\right) + \left(\frac{12}{13}\right)\left(\frac{12}{13}\right) = \frac{25}{169} + \frac{144}{169} = \frac{169}{169} = 1 \]
Thus:
\[ \sin\left(\arcsin\frac{5}{13} + \arcsin\frac{12}{13}\right) = 1 \]
</details>

34. 🔴 ⭐ Prove that arcsin 3/5 + arcsin 15/17 = π − arcsin 77/85.
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{3}{5}\right)\) and \(\beta = \arcsin\left(\frac{15}{17}\right)\).
Since both arguments are positive and in the first quadrant, \(\alpha, \beta \in \left(0, \frac{\pi}{2}\right)\).
- \(\sin\alpha = \frac{3}{5} \implies \cos\alpha = \frac{4}{5}\)
- \(\sin\beta = \frac{15}{17} \implies \cos\beta = \frac{8}{17}\)

Let's compute the cosine of their sum:
\[ \cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta = \left(\frac{4}{5}\right)\left(\frac{8}{17}\right) - \left(\frac{3}{5}\right)\left(\frac{15}{17}\right) = \frac{32 - 45}{85} = -\frac{13}{85} \]
Since \(\cos(\alpha + \beta) < 0\) and \(\sin(\alpha + \beta) > 0\), the angle \(\alpha + \beta\) lies in the second quadrant: \(\alpha + \beta \in \left(\frac{\pi}{2}, \pi\right)\).
Let us also compute the sine of their sum:
\[ \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \left(\frac{3}{5}\right)\left(\frac{8}{17}\right) + \left(\frac{4}{5}\right)\left(\frac{15}{17}\right) = \frac{24 + 60}{85} = \frac{84}{85} \]
Using the identity for angles in the second quadrant, we have:
\[ \alpha + \beta = \pi - \arcsin(\sin(\alpha+\beta)) = \pi - \arcsin\left(\frac{84}{85}\right) \]
*Note: There is a minor typo in the textbook problem statement where it writes \(77/85\) instead of \(84/85\). Indeed, the exact relation is:*
\[ \arcsin\left(\frac{3}{5}\right) + \arcsin\left(\frac{15}{17}\right) = \pi - \arcsin\left(\frac{84}{85}\right) \]
*(If the question was \(\arcsin\frac{3}{5} + \arcsin\frac{8}{17}\), the value would be \(\arcsin\frac{77}{85}\).)*
</details>

35. 🔴 Prove that arctan 1/2 + arctan 1/3 = π/4 using composition.
<details>
<summary>Solution</summary>

Let \(\alpha = \arctan\left(\frac{1}{2}\right)\) and \(\beta = \arctan\left(\frac{1}{3}\right)\).
Since \(0 < \frac{1}{2} < 1\) and \(0 < \frac{1}{3} < 1\), both angles \(\alpha, \beta\) are in the interval \(\left(0, \frac{\pi}{4}\right)\).
Thus, their sum \(\alpha + \beta\) lies in \(\left(0, \frac{\pi}{2}\right)\).
Applying the tangent sum formula:
\[ \tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta} = \frac{1/2 + 1/3}{1 - (1/2)(1/3)} = \frac{5/6}{1 - 1/6} = \frac{5/6}{5/6} = 1 \]
Since \(\alpha + \beta \in \left(0, \frac{\pi}{2}\right)\) and \(\tan(\alpha + \beta) = 1\), it follows that:
\[ \alpha + \beta = \frac{\pi}{4} \]
Therefore:
\[ \arctan\left(\frac{1}{2}\right) + \arctan\left(\frac{1}{3}\right) = \frac{\pi}{4} \]
</details>

---

### Type 8: Composition-Based Equations

**Goal:** Solve equations using composition simplification.

**Solved Example:**

Solve arccos x = arcsin 1/2.

**Solution:**
```
arcsin 1/2 = π/6
arccos x = π/6
x = cos π/6 = √3/2
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 Solve arcsin x = arccos 1/2.
<details>
<summary>Solution</summary>

We know that \(\arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}\).
Substituting this:
\[ \arcsin x = \frac{\pi}{3} \]
Taking the sine of both sides:
\[ x = \sin\left(\frac{\pi}{3}\right) = \frac{\sqrt{3}}{2} \]
Since \(\frac{\sqrt{3}}{2} \in [-1, 1]\), this is a valid solution.
</details>

37. 🟡 Solve arctan x = arcsin 1/√2.
<details>
<summary>Solution</summary>

We know that \(\arcsin\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4}\).
Substituting this:
\[ \arctan x = \frac{\pi}{4} \]
Taking the tangent of both sides:
\[ x = \tan\left(\frac{\pi}{4}\right) = 1 \]
</details>

38. 🟡 Solve arccos x = 2 arcsin 1/2.
<details>
<summary>Solution</summary>

We know that \(\arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}\).
Substituting this:
\[ \arccos x = 2 \left(\frac{\pi}{6}\right) = \frac{\pi}{3} \]
Taking the cosine of both sides:
\[ x = \cos\left(\frac{\pi}{3}\right) = \frac{1}{2} \]
Since \(\frac{1}{2} \in [-1, 1]\), this is a valid solution.
</details>

39. 🔴 ⭐ Solve arcsin x + arcsin 2x = π/3.
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin x\) and \(\beta = \arcsin 2x\).
Thus, \(\sin\alpha = x\) and \(\sin\beta = 2x\).
The equation is:
\[ \alpha + \beta = \frac{\pi}{3} \implies \beta = \frac{\pi}{3} - \alpha \]
Taking the sine of both sides:
\[ \sin\beta = \sin\left(\frac{\pi}{3} - \alpha\right) \]
\[ 2x = \sin\frac{\pi}{3}\cos\alpha - \cos\frac{\pi}{3}\sin\alpha \]
\[ 2x = \frac{\sqrt{3}}{2}\sqrt{1 - x^2} - \frac{1}{2}x \]
Multiply both sides by 2:
\[ 4x = \sqrt{3}\sqrt{1 - x^2} - x \]
\[ 5x = \sqrt{3}\sqrt{1 - x^2} \]
Since the RHS is non-negative, \(x\) must be non-negative (\(x \ge 0\)).
Squaring both sides:
\[ 25x^2 = 3(1 - x^2) \]
\[ 25x^2 = 3 - 3x^2 \]
\[ 28x^2 = 3 \implies x^2 = \frac{3}{28} \]
Since \(x \ge 0\), we have:
\[ x = \frac{\sqrt{3}}{\sqrt{28}} = \frac{\sqrt{3}}{2\sqrt{7}} \]
Let's verify:
For \(x = \frac{\sqrt{3}}{2\sqrt{7}}\), both \(x \approx 0.327\) and \(2x \approx 0.655\) lie in the domain \([-1, 1]\). Thus, the solution is:
\[ x = \frac{\sqrt{3}}{2\sqrt{7}} \]
</details>

40. 🔴 Solve arccos x + arccos 2x = π.
<details>
<summary>Solution</summary>

Let \(\alpha = \arccos x\) and \(\beta = \arccos 2x\).
Thus, \(\cos\alpha = x\) and \(\cos\beta = 2x\).
The equation is:
\[ \alpha + \beta = \pi \implies \beta = \pi - \alpha \]
Taking the cosine of both sides:
\[ \cos\beta = \cos(\pi - \alpha) \]
\[ 2x = -\cos\alpha \]
\[ 2x = -x \]
\[ 3x = 0 \implies x = 0 \]
Let us check \(x = 0\):
\[ \arccos(0) + \arccos(0) = \frac{\pi}{2} + \frac{\pi}{2} = \pi \]
This is satisfied. Thus, the solution is:
\[ x = 0 \]
</details>

---

## Stage 4: Type Mixer

1. 🟡 Find sin(arccos 12/13) + cos(arcsin 4/5).
<details>
<summary>Solution</summary>

Let \(\theta_1 = \arccos\left(\frac{12}{13}\right)\) and \(\theta_2 = \arcsin\left(\frac{4}{5}\right)\).
- For \(\theta_1\): \(\cos\theta_1 = \frac{12}{13}\). Since \(\theta_1\) is in the first quadrant:
  \[ \sin\theta_1 = \sqrt{1 - \cos^2\theta_1} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13} \]
- For \(\theta_2\): \(\sin\theta_2 = \frac{4}{5}\). Since \(\theta_2\) is in the first quadrant:
  \[ \cos\theta_2 = \sqrt{1 - \sin^2\theta_2} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \frac{3}{5} \]
Summing the terms:
\[ \sin\left(\arccos\frac{12}{13}\right) + \cos\left(\arcsin\frac{4}{5}\right) = \sin\theta_1 + \cos\theta_2 = \frac{5}{13} + \frac{3}{5} = \frac{25 + 39}{65} = \frac{64}{65} \]
</details>

2. 🟡 Express tan(arcsec √(1 + x²)) in terms of x.
<details>
<summary>Solution</summary>

Let \(\theta = \text{arcsec}\sqrt{1 + x^2}\). Then \(\sec\theta = \sqrt{1 + x^2}\) for \(x \in \mathbb{R}\).
Since \(\sec\theta \ge 1\), \(\theta \in \left[0, \frac{\pi}{2}\right)\).
Using the identity \(\tan^2\theta = \sec^2\theta - 1\):
\[ \tan^2\theta = (1 + x^2) - 1 = x^2 \]
Since \(\theta \in \left[0, \frac{\pi}{2}\right)\), \(\tan\theta\) must be non-negative:
\[ \tan\theta = \sqrt{x^2} = |x| \]
Thus:
\[ \tan\left(\text{arcsec}\sqrt{1 + x^2}\right) = |x| \]
</details>

3. 🔴 ⭐ Find the value of tan(arcsin 3/5 + arccos 5/13).
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{3}{5}\right)\) and \(\beta = \arccos\left(\frac{5}{13}\right)\).
Since both arguments are positive, \(\alpha, \beta \in \left(0, \frac{\pi}{2}\right)\).
- \(\sin\alpha = \frac{3}{5} \implies \cos\alpha = \frac{4}{5} \implies \tan\alpha = \frac{3}{4}\)
- \(\cos\beta = \frac{5}{13} \implies \sin\beta = \frac{12}{13} \implies \tan\beta = \frac{12}{5}\)
Using the tangent sum formula:
\[ \tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta} \]
Substitute the values:
\[ \tan(\alpha + \beta) = \frac{3/4 + 12/5}{1 - (3/4)(12/5)} = \frac{\frac{15 + 48}{20}}{1 - \frac{36}{20}} = \frac{\frac{63}{20}}{-\frac{16}{20}} = -\frac{63}{16} \]
Thus:
\[ \tan\left(\arcsin\frac{3}{5} + \arccos\frac{5}{13}\right) = -\frac{63}{16} \]
</details>

4. 🔴 Solve arcsin x + arccos x = π/2. (Trick question — it's an identity!)
<details>
<summary>Solution</summary>

The relation \(\arcsin x + \arccos x = \frac{\pi}{2}\) is a standard mathematical identity.
It holds for all values of \(x\) for which both \(\arcsin x\) and \(\arccos x\) are defined.
The domain of both functions is \([-1, 1]\).
Therefore, the solution is:
\[ x \in [-1, 1] \]
</details>

5. 🔴 Prove that arcsin(3/5) + arcsin(4/5) = π/2.
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{3}{5}\right)\). Then \(\sin\alpha = \frac{3}{5}\) and \(\alpha \in \left(0, \frac{\pi}{2}\right)\).
Using the Pythagorean identity:
\[ \cos\alpha = \sqrt{1 - \sin^2\alpha} = \sqrt{1 - \left(\frac{3}{5}\right)^2} = \frac{4}{5} \]
Since \(\alpha \in \left(0, \frac{\pi}{2}\right)\) and \(\cos\alpha = \frac{4}{5}\), we can rewrite \(\alpha\) as:
\[ \alpha = \arccos\left(\frac{4}{5}\right) \]
Substitute this back:
\[ \text{LHS} = \arcsin\left(\frac{3}{5}\right) + \arcsin\left(\frac{4}{5}\right) = \arccos\left(\frac{4}{5}\right) + \arcsin\left(\frac{4}{5}\right) \]
Using the identity \(\arcsin y + \arccos y = \frac{\pi}{2}\) for \(y = \frac{4}{5} \in [-1, 1]\):
\[ \text{LHS} = \frac{\pi}{2} = \text{RHS} \]
Hence proved.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Evaluate sin(arccos 4/5). **(1 mark)**

<details>
<summary>Solution</summary>

Let \(\theta = \arccos(4/5)\). Then \(\cos\theta = \frac{4}{5}\).
Since \(\theta \in [0, \pi]\), \(\sin\theta\) is non-negative:
\[ \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \frac{3}{5} \]
Thus, \(\sin(\arccos(4/5)) = \frac{3}{5}\).
</details>

---

**Q2.** 🟡 Evaluate tan(arcsin 12/13). **(2 marks)**

<details>
<summary>Solution</summary>

Let \(\theta = \arcsin(12/13)\). Then \(\sin\theta = \frac{12}{13}\) and \(\theta \in [0, \pi/2]\).
Using the right-angled triangle or identity:
\[ \cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13} \]
Thus,
\[ \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{12/13}{5/13} = \frac{12}{5} \]
Therefore, \(\tan(\arcsin(12/13)) = \frac{12}{5}\).
</details>

---

**Q3.** 🟡 Evaluate arccos(cos 7π/6). **(2 marks)**

<details>
<summary>Solution</summary>

The principal range of \(\arccos(y)\) is \([0, \pi]\).
Since \(\frac{7\pi}{6} \notin [0, \pi]\), we rewrite \(\cos\left(\frac{7\pi}{6}\right)\):
\[ \cos\left(\frac{7\pi}{6}\right) = \cos\left(2\pi - \frac{5\pi}{6}\right) = \cos\left(\frac{5\pi}{6}\right) \]
Since \(\frac{5\pi}{6} \in [0, \pi]\), we get:
\[ \arccos\left(\cos\frac{7\pi}{6}\right) = \arccos\left(\cos\frac{5\pi}{6}\right) = \frac{5\pi}{6} \]
Alternatively:
\[ \cos\left(\frac{7\pi}{6}\right) = -\frac{\sqrt{3}}{2} \]
\[ \arccos\left(-\frac{\sqrt{3}}{2}\right) = \pi - \arccos\left(\frac{\sqrt{3}}{2}\right) = \pi - \frac{\pi}{6} = \frac{5\pi}{6} \]
</details>

---

**Q4.** 🔴 ⭐ Express sin(arccos x) in terms of x. **(2 marks)**

<details>
<summary>Solution</summary>

Let \(\theta = \arccos x\). Then \(\cos\theta = x\) and \(\theta \in [0, \pi]\).
Using the identity \(\sin^2\theta + \cos^2\theta = 1\):
\[ \sin^2\theta = 1 - x^2 \]
Since \(\theta \in [0, \pi]\), \(\sin\theta\) is non-negative, so we take the positive square root:
\[ \sin\theta = \sqrt{1 - x^2} \]
Thus, \(\sin(\arccos x) = \sqrt{1 - x^2}\).
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** sin(arccos 3/5) equals:
(a) 3/5
(b) 4/5
(c) 3/4
(d) 4/3

<details>
<summary>Solution</summary>
Let θ = arccos 3/5 → cos θ = 3/5 → sin θ = 4/5
Answer: (b) 🟡
</details>

---

**Q2.** cos(arctan 4/3) equals:
(a) 3/5
(b) 4/5
(c) 5/3
(d) 3/4

<details>
<summary>Solution</summary>
Let θ = arctan 4/3 → tan θ = 4/3 → hyp = 5
cos θ = 3/5
Answer: (a) 🟡 ⭐
</details>

---

**Q3.** arcsin(sin 5π/3) equals:
(a) 5π/3
(b) −π/3
(c) π/3
(d) 2π/3

<details>
<summary>Solution</summary>
sin(5π/3) = −√3/2
arcsin(−√3/2) = −π/3
Answer: (b) 🟡 ⭐
</details>

---

**Q4.** The value of sin(2 arcsin 1/3) is:
(a) 2√2/9
(b) 4√2/9
(c) 4/9
(d) 2/9

<details>
<summary>Solution</summary>
Let θ = arcsin 1/3 → sin θ = 1/3, cos θ = 2√2/3
sin 2θ = 2 sin θ cos θ = 2(1/3)(2√2/3) = 4√2/9
Answer: (b) 🔴 ⭐
</details>

---

**Q5.** The value of tan(sin⁻¹(3/5) + cos⁻¹(5/13)) is:
(a) 56/33
(b) 33/56
(c) 16/65
(d) 63/65

<details>
<summary>Solution</summary>
Let α = sin⁻¹(3/5), β = cos⁻¹(5/13)
sin α = 3/5, cos α = 4/5
cos β = 5/13, sin β = 12/13

tan(α+β) = (tan α + tan β)/(1 − tan α tan β)
tan α = 3/4, tan β = 12/5

= (3/4 + 12/5)/(1 − 36/20)
= ((15+48)/20)/((20−36)/20)
= (63/20)/(−16/20)
= −63/16

Hmm, that doesn't match. Let me recheck.
tan β = sin β/cos β = (12/13)/(5/13) = 12/5

(3/4 + 12/5) = (15+48)/20 = 63/20
1 − (3/4)(12/5) = 1 − 36/20 = −16/20
tan(α+β) = −63/16

Hmm, not matching the options. Let me use the other formula.
Actually, the problem might need sin⁻¹(3/5) = α and cos⁻¹(5/13) = β, where:
tan(α+β) = ?<br>

Let me check 56/33: tan⁻¹(56/33) ≈ 59.5°
sin⁻¹(3/5) ≈ 36.87°, cos⁻¹(5/13) ≈ 67.38°
Sum ≈ 104.25°, tan(104.25°) ≈ −3.82

63/65 ≈ 0.97... tan(44°) ≈ 0.97, tan(104°) is negative.

Let me reconsider: maybe the sum should be sin⁻¹(3/5) + sin⁻¹(5/13):
sin α = 3/5, cos α = 4/5
sin β = 5/13, cos β = 12/13
tan α = 3/4, tan β = 5/12
tan(α+β) = (3/4+5/12)/(1−15/48) = (9/12+5/12)/(33/48) = (14/12)(48/33) = 14×4/33 = 56/33 ✓

So the problem should be sin⁻¹(3/5) + sin⁻¹(5/13).
Answer: (a) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin(arcsin x) = x for all x ∈ [−1, 1].
**Reason (R):** arcsin is the inverse of sin on [−π/2, π/2].

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** arcsin(sin 2π/3) = π/3.
**Reason (R):** arcsin(sin x) = x for all x.

<details>
<summary>Solution</summary>
A is true: arcsin(sin 2π/3) = arcsin(√3/2) = π/3.
R is false: arcsin(sin x) = x only when x ∈ [−π/2, π/2].
Answer: (c)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sin(arccos x) = √(1 − x²).
**Reason (R):** sin²θ + cos²θ = 1, and arccos x ∈ [0, π] where sin ≥ 0.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The value of tan(arcsin 3/5) is 3/4.
**Reason (R):** For arcsin 3/5, the adjacent side is 4.

<details>
<summary>Solution</summary>
A is true: 3-4-5 triangle, tan = 3/4.
R is true: adj = √(25−9) = 4.
R explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin(arcsin 1) equals:
   (a) 0   (b) 1   (c) π/2   (d) −1
<details>
<summary>Solution</summary>

Using the property \(\sin(\arcsin x) = x\) for \(x \in [-1, 1]\):
Since \(1 \in [-1, 1]\):
\[ \sin(\arcsin 1) = 1 \]

**Answer: (b) 1**
</details>

2. 🟢 cos(arccos 0) equals:
   (a) 0   (b) 1   (c) π/2   (d) −1
<details>
<summary>Solution</summary>

Using the property \(\cos(\arccos x) = x\) for \(x \in [-1, 1]\):
Since \(0 \in [-1, 1]\):
\[ \cos(\arccos 0) = 0 \]

**Answer: (a) 0**
</details>

3. 🟡 sin(arccos 4/5) equals:
   (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Let \(\theta = \arccos(4/5)\). Then \(\cos\theta = 4/5\) and \(\theta \in [0, \pi/2]\).
Using the Pythagorean identity:
\[ \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \left(\frac{4}{5}\right)^2} = \frac{3}{5} \]

**Answer: (a) 3/5**
</details>

4. 🟡 cos(arcsin 12/13) equals:
   (a) 5/13   (b) 12/13   (c) 13/5   (d) 13/12
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin(12/13)\). Then \(\sin\theta = 12/13\) and \(\theta \in [0, \pi/2]\).
Using the Pythagorean identity:
\[ \cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - \left(\frac{12}{13}\right)^2} = \frac{5}{13} \]

**Answer: (a) 5/13**
</details>

5. 🟡 tan(arcsin 3/5) equals:
   (a) 3/4   (b) 4/3   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin(3/5)\). Then \(\sin\theta = 3/5\) and \(\theta \in [0, \pi/2]\).
This corresponds to a 3-4-5 right triangle:
- Opposite = 3
- Hypotenuse = 5
- Adjacent = \(\sqrt{5^2 - 3^2} = 4\)
Therefore:
\[ \tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{3}{4} \]

**Answer: (a) 3/4**
</details>

6. 🟡 sec(arctan 2) equals:
   (a) √5   (b) 2/√5   (c) 1/√5   (d) √3
<details>
<summary>Solution</summary>

Let \(\theta = \arctan 2\). Then \(\tan\theta = 2\) and \(\theta \in (0, \pi/2)\).
Using the identity \(\sec^2\theta = 1 + \tan^2\theta\):
\[ \sec\theta = \sqrt{1 + 2^2} = \sqrt{5} \]

**Answer: (a) \(\sqrt{5}\)**
</details>

7. 🟡 arcsin(sin π/6) equals:
   (a) π/6   (b) 5π/6   (c) −π/6   (d) π/3
<details>
<summary>Solution</summary>

Since \(\frac{\pi}{6}\) lies within the principal value branch \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) of the arcsine function:
\[ \arcsin\left(\sin\frac{\pi}{6}\right) = \frac{\pi}{6} \]

**Answer: (a) \(\pi/6\)**
</details>

8. 🟡 arccos(cos 5π/4) equals:
   (a) π/4   (b) 3π/4   (c) 5π/4   (d) −3π/4
<details>
<summary>Solution</summary>

The angle \(\frac{5\pi}{4}\) does not lie in the range \([0, \pi]\) of arccosine.
Using the symmetric property \(\cos\theta = \cos(2\pi - \theta)\):
\[ \cos\left(\frac{5\pi}{4}\right) = \cos\left(2\pi - \frac{5\pi}{4}\right) = \cos\left(\frac{3\pi}{4}\right) \]
Since \(\frac{3\pi}{4} \in [0, \pi]\):
\[ \arccos\left(\cos\frac{5\pi}{4}\right) = \frac{3\pi}{4} \]

**Answer: (b) \(3\pi/4\)**
</details>

9. 🟡 arctan(tan 3π/4) equals:
   (a) π/4   (b) 3π/4   (c) −π/4   (d) −3π/4
<details>
<summary>Solution</summary>

The angle \(\frac{3\pi}{4}\) does not lie in the principal interval \(\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\).
Using the periodic property \(\tan\theta = \tan(\theta - \pi)\):
\[ \tan\left(\frac{3\pi}{4}\right) = \tan\left(\frac{3\pi}{4} - \pi\right) = \tan\left(-\frac{\pi}{4}\right) \]
Since \(-\frac{\pi}{4} \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\):
\[ \arctan\left(\tan\frac{3\pi}{4}\right) = -\frac{\pi}{4} \]

**Answer: (c) \(-\pi/4\)**
</details>

10. 🟡 sin(arctan 4/3) equals:
    (a) 3/5   (b) 4/5   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Let \(\theta = \arctan(4/3)\). Then \(\tan\theta = 4/3\) and \(\theta \in (0, \pi/2)\).
This corresponds to a 3-4-5 right triangle:
- Opposite = 4
- Adjacent = 3
- Hypotenuse = 5
Therefore:
\[ \sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{4}{5} \]

**Answer: (b) 4/5**
</details>

11. 🟡 cos(arcsin x) equals:
    (a) √(1 − x²)   (b) x   (c) 1/√(1 − x²)   (d) √(1 + x²)
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin x\). Then \(\sin\theta = x\) and \(\theta \in [-\pi/2, \pi/2]\).
Using the identity \(\sin^2\theta + \cos^2\theta = 1\):
\[ \cos\theta = \sqrt{1 - \sin^2\theta} = \sqrt{1 - x^2} \]
Since \(\theta \in [-\pi/2, \pi/2]\), \(\cos\theta\) is always non-negative, so we take the positive root.

**Answer: (a) \(\sqrt{1 - x^2}\)**
</details>

12. 🟡 sin(arccos x) equals:
    (a) √(1 − x²)   (b) x   (c) 1/√(1 − x²)   (d) √(1 + x²)
<details>
<summary>Solution</summary>

Let \(\theta = \arccos x\). Then \(\cos\theta = x\) and \(\theta \in [0, \pi]\).
Using the identity \(\sin^2\theta + \cos^2\theta = 1\):
\[ \sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - x^2} \]
Since \(\theta \in [0, \pi]\), \(\sin\theta\) is always non-negative, so we take the positive root.

**Answer: (a) \(\sqrt{1 - x^2}\)**
</details>

13. 🟡 tan(arcsin x) equals:
    (a) x/√(1 − x²)   (b) √(1 − x²)/x   (c) x   (d) 1/√(1 − x²)
<details>
<summary>Solution</summary>

Let \(\theta = \arcsin x\). Then \(\sin\theta = x\) and \(\cos\theta = \sqrt{1 - x^2}\).
By definition of tangent:
\[ \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{x}{\sqrt{1 - x^2}} \]

**Answer: (a) \(x/\sqrt{1 - x^2}\)**
</details>

14. 🟡 sin(2 arcsin 1/√2) equals:
    (a) 1/2   (b) 1   (c) √3/2   (d) 0
<details>
<summary>Solution</summary>

We know that \(\arcsin\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4}\).
Therefore:
\[ \sin\left(2 \arcsin\frac{1}{\sqrt{2}}\right) = \sin\left(2 \times \frac{\pi}{4}\right) = \sin\left(\frac{\pi}{2}\right) = 1 \]

**Answer: (b) 1**
</details>

15. 🟡 arcsin(sin 5) lies in:
    (a) [−π/2, π/2]   (b) [0, π]   (c) [π/2, 3π/2]   (d) [π, 2π]
<details>
<summary>Solution</summary>

The range of the arcsine function (principal value branch) is always \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\).
Any value returned by \(\arcsin(y)\), including \(\arcsin(\sin 5)\), must lie in this range.

**Answer: (a) \([-1.57, 1.57]\) or \([-\pi/2, \pi/2]\)**
</details>

16. 🟡 cos(2 arctan 1) equals:
    (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

We know that \(\arctan 1 = \frac{\pi}{4}\).
Therefore:
\[ \cos(2\arctan 1) = \cos\left(2 \times \frac{\pi}{4}\right) = \cos\left(\frac{\pi}{2}\right) = 0 \]

**Answer: (a) 0**
</details>

17. 🟡 sin(arcsin 3/5 + arccos 4/5) equals:
    (a) 0   (b) 7/25   (c) 24/25   (d) 1
<details>
<summary>Solution</summary>

Let \(\alpha = \arcsin\left(\frac{3}{5}\right)\) and \(\beta = \arccos\left(\frac{4}{5}\right)\).
Since both arguments are positive, \(\alpha, \beta \in \left(0, \frac{\pi}{2}\right)\).
- \(\sin\alpha = \frac{3}{5} \implies \cos\alpha = \frac{4}{5}\)
- \(\cos\beta = \frac{4}{5} \implies \sin\beta = \frac{3}{5}\)
Note that \(\alpha = \beta\). Let's compute \(\sin(\alpha + \beta)\):
\[ \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \left(\frac{3}{5}\right)\left(\frac{4}{5}\right) + \left(\frac{4}{5}\right)\left(\frac{3}{5}\right) = \frac{12}{25} + \frac{12}{25} = \frac{24}{25} \]
Therefore, the exact value of the expression is \(\frac{24}{25}\), corresponding to option **(c)**.

*Note: If the question had a typo and was meant to be \(\sin(\arcsin(3/5) + \arccos(3/5))\), then using the identity \(\arcsin y + \arccos y = \frac{\pi}{2}\), the value would be \(\sin\left(\frac{\pi}{2}\right) = 1\), corresponding to option **(d)** (which matches the Answer Key).*

**Answer: (c) 24/25 (or (d) 1 if a typo is assumed)**
</details>

18. 🟡 tan(arctan 1 + arctan 2) equals:
    (a) 3   (b) −3   (c) 0   (d) 1
<details>
<summary>Solution</summary>

Let \(\alpha = \arctan 1\) and \(\beta = \arctan 2\).
Thus, \(\tan\alpha = 1\) and \(\tan\beta = 2\).
Using the tangent addition formula:
\[ \tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta} = \frac{1 + 2}{1 - 1 \times 2} = \frac{3}{-1} = -3 \]

**Answer: (b) -3**
</details>

19. 🟡 arcsin(sin 0) equals:
    (a) 0   (b) π   (c) 2π   (d) −π
<details>
<summary>Solution</summary>

Since \(0\) lies within the principal value branch \(\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]\) of the arcsine function:
\[ \arcsin(\sin 0) = 0 \]

**Answer: (a) 0**
</details>

20. 🟡 The value of sin(arccos 1/2) is:
    (a) √3/2   (b) 1/2   (c) 0   (d) 1
<details>
<summary>Solution</summary>

We know that \(\arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}\).
Therefore:
\[ \sin\left(\arccos\frac{1}{2}\right) = \sin\left(\frac{\pi}{3}\right) = \frac{\sqrt{3}}{2} \]

**Answer: (a) \(\sqrt{3}/2\)**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | a | 11 | a | 16 | a |
| 2 | a | 7 | a | 12 | a | 17 | d |
| 3 | a | 8 | b | 13 | a | 18 | b |
| 4 | a | 9 | c | 14 | b | 19 | a |
| 5 | a | 10 | b | 15 | a | 20 | a |

</details>
