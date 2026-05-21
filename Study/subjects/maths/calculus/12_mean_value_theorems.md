# Chapter 12: Mean Value Theorems

---

## Stage 1: The Core Idea

### Rolle's Theorem — The U-Turn Guarantee

If you throw a ball straight up, it goes up, reaches a peak, then comes down. At the peak, its velocity (the derivative of height) is exactly zero.

**Rolle's Theorem** captures this: if a differentiable function starts and ends at the same height, it must have a "flat spot" (zero derivative) somewhere in between.

### Lagrange's MVT — The Average Speed Guarantee

If you drive from Delhi to Agra (200 km) in exactly 4 hours, your average speed is 50 km/h. Does that mean you were going exactly 50 km/h at some moment? **Yes!** The Mean Value Theorem guarantees it — no matter how you sped up, slowed down, or even reversed, there must be at least one instant where your instantaneous speed was exactly 50 km/h.

This is the geometric meaning: **there exists a point where the tangent line is parallel to the secant line** joining the two endpoints.

---

## Stage 2: The Formula Lab

### Rolle's Theorem

**Conditions:** $f$ satisfies all THREE:
1. $f$ is **continuous** on $[a, b]$
2. $f$ is **differentiable** on $(a, b)$
3. $f(a) = f(b)$

**Conclusion:** There exists at least one $c \in (a, b)$ such that $f'(c) = 0$.

> ⚠️ **Trap:** ALL three conditions must be checked. If any one fails, Rolle's theorem **may not** apply. Finding that the conditions fail does NOT mean $f'(c) = 0$ has no solution — it just means the theorem doesn't guarantee it.

### Lagrange's Mean Value Theorem (LMVT)

**Conditions:** $f$ satisfies:
1. $f$ is **continuous** on $[a, b]$
2. $f$ is **differentiable** on $(a, b)$

**Conclusion:** There exists at least one $c \in (a, b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

> **Geometric meaning:** The slope of the tangent at $c$ equals the slope of the secant through $(a, f(a))$ and $(b, f(b))$.

> **Note:** Rolle's theorem is just LMVT with the special case $f(a) = f(b)$ (so the secant slope is 0, and we need a tangent with slope 0).

### Key Consequences of LMVT

1. **If $f'(x) = 0$ on $(a,b)$**, then $f$ is constant on $[a,b]$.
2. **If $f'(x) > 0$ on $(a,b)$**, then $f$ is increasing on $[a,b]$.
3. **If $f'(x) < 0$ on $(a,b)$**, then $f$ is decreasing on $[a,b]$.
4. **If $|f'(x)| \leq M$ on $(a,b)$**, then $|f(b) - f(a)| \leq M(b-a)$.

---

## Stage 3: Type-wise Mastery

### Type 1: Verifying Rolle's Theorem

**Goal:** Check all three conditions, then find the point $c$.

**Solved Example:** ⭐

Verify Rolle's theorem for $f(x) = x^2 - 4x + 3$ on $[1, 3]$.

**Solution:**
```
Step 1: Continuity. f is a polynomial → continuous on [1,3]. ✓

Step 2: Differentiability. Polynomial → differentiable on (1,3). ✓

Step 3: f(1) = 1 - 4 + 3 = 0. f(3) = 9 - 12 + 3 = 0. f(1) = f(3). ✓

By Rolle's theorem, ∃ c ∈ (1,3) with f'(c) = 0.
f'(x) = 2x - 4 = 0 ⟹ x = 2.
c = 2 ∈ (1,3). ✓
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

1. 🟢 Verify Rolle's for $f(x) = x^2 - 5x + 4$ on $[1, 4]$.
<details>
<summary>Solution</summary>

1. Polynomial → continuous on `[1, 4]`.
2. Polynomial → differentiable on `(1, 4)`.
3. `f(1) = 1 - 5 + 4 = 0`; `f(4) = 16 - 20 + 4 = 0`. `f(1) = f(4)`.
All conditions met. `\exists c \in (1, 4)` such that `f'(c) = 0`.
`f'(x) = 2x - 5 = 0 \implies x = 2.5`. `c = 2.5 \in (1, 4)`. ✓
</details>

2. 🟡 Verify Rolle's for $f(x) = \sin x$ on $[0, \pi]$.
<details>
<summary>Solution</summary>

1. `\sin x` is continuous on `[0, \pi]`.
2. `\sin x` is differentiable on `(0, \pi)`.
3. `f(0) = \sin 0 = 0`; `f(\pi) = \sin \pi = 0`. `f(0) = f(\pi)`.
All conditions met. `\exists c \in (0, \pi)` such that `f'(c) = 0`.
`f'(x) = \cos x = 0 \implies x = \pi/2`. `c = \pi/2 \in (0, \pi)`. ✓
</details>

3. 🟡 $f(x) = x(x-1)(x-2)$ on $[0, 2]$.
<details>
<summary>Solution</summary>

1 & 2. Polynomial → continuous on `[0, 2]` and differentiable on `(0, 2)`.
3. `f(0) = 0`; `f(2) = 2(1)(0) = 0`. `f(0) = f(2)`.
All conditions met.
`f(x) = x^3 - 3x^2 + 2x`.
`f'(x) = 3x^2 - 6x + 2 = 0`.
`x = \frac{6 \pm \sqrt{36 - 24}}{6} = \frac{6 \pm \sqrt{12}}{6} = 1 \pm \frac{1}{\sqrt{3}}`.
Both `1 + 1/\sqrt{3} \approx 1.577` and `1 - 1/\sqrt{3} \approx 0.423` are in `(0, 2)`. ✓
</details>

4. 🔴 $f(x) = |x|$ on $[-1, 1]$. Does Rolle's theorem apply? Why not?
<details>
<summary>Solution</summary>

1. `f(x)` is continuous on `[-1, 1]`. ✓
2. `f(x)` is **not differentiable** at `x = 0`, which is in `(-1, 1)`. ✗
3. `f(-1) = 1 = f(1)`. ✓
Because condition 2 fails, **Rolle's Theorem does not apply**.
(Indeed, there is no point where the tangent is horizontal; the derivative is either -1 or 1).
</details>

5. 🔴 $f(x) = \begin{cases} x^2-x-2 & x \neq -1 \\ 2 & x = -1 \end{cases}$ on $[-2, 2]$. Identify which condition fails.
<details>
<summary>Solution</summary>

Check continuity at `x = -1`:
`\lim_{x\to-1} (x^2 - x - 2) = (-1)^2 - (-1) - 2 = 1 + 1 - 2 = 0`.
But `f(-1) = 2`.
Since `\lim_{x\to-1} f(x) \neq f(-1)`, the function is **not continuous** at `x = -1`.
Therefore, **Condition 1 (continuity on `[-2, 2]`) fails**.
</details>

---

### Type 2: Verifying LMVT and Finding c

**Goal:** Apply LMVT and compute the exact value of $c$.

**Solved Example:** ⭐

Verify LMVT for $f(x) = x^3 - x^2 - x + 1$ on $[0, 2]$.

**Solution:**
```
Step 1: f is a polynomial → continuous on [0,2] ✓ and differentiable on (0,2) ✓.

Step 2: Compute the secant slope:
f(0) = 1, f(2) = 8 - 4 - 2 + 1 = 3.
[f(2)-f(0)]/(2-0) = (3-1)/2 = 1.

Step 3: Set f'(c) = 1:
f'(x) = 3x² - 2x - 1 = 1
3x² - 2x - 2 = 0
x = [2 ± √(4+24)]/6 = [2 ± √28]/6 = [1 ± √7]/3.

c = (1 + √7)/3 ≈ 1.22 ∈ (0,2). ✓ [The other root is negative.]
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟢 Find $c$ for LMVT: $f(x) = 2x^2 - x$ on $[1, 3]$.
<details>
<summary>Solution</summary>

`f(1) = 2(1)^2 - 1 = 1`. `f(3) = 2(3)^2 - 3 = 18 - 3 = 15`.
Secant slope `= \frac{15 - 1}{3 - 1} = \frac{14}{2} = 7`.
`f'(x) = 4x - 1`. Set `f'(c) = 7 \implies 4c - 1 = 7 \implies 4c = 8 \implies c = 2`.
`2 \in (1, 3)`. ✓
</details>

7. 🟡 $f(x) = \sqrt{x}$ on $[4, 9]$.
<details>
<summary>Solution</summary>

`f(4) = 2`, `f(9) = 3`.
Secant slope `= \frac{3 - 2}{9 - 4} = \frac{1}{5}`.
`f'(x) = \frac{1}{2\sqrt{x}}`. Set `f'(c) = \frac{1}{5} \implies \frac{1}{2\sqrt{c}} = \frac{1}{5} \implies \sqrt{c} = 2.5 \implies c = 6.25`.
`6.25 \in (4, 9)`. ✓
</details>

8. 🟡 $f(x) = \ln x$ on $[1, e^2]$.
<details>
<summary>Solution</summary>

`f(1) = 0`, `f(e^2) = 2`.
Secant slope `= \frac{2 - 0}{e^2 - 1} = \frac{2}{e^2 - 1}`.
`f'(x) = \frac{1}{x}`. Set `f'(c) = \frac{2}{e^2 - 1} \implies c = \frac{e^2 - 1}{2}`.
Since `e \approx 2.718 \implies e^2 \approx 7.39`, we have `c \approx 6.39/2 = 3.195`.
This is in `(1, 7.39)`. So `c = \frac{e^2 - 1}{2}`. ✓
</details>

9. 🔴 $f(x) = x^{2/3}$ on $[-8, 8]$. Does LMVT apply? Find $c$ if it does, identify the issue if not.
<details>
<summary>Solution</summary>

`f'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3x^{1/3}}`.
The derivative is undefined at `x = 0`, which is in the interval `(-8, 8)`.
So, the function is **not differentiable** on `(-8, 8)`. **LMVT does not apply**.
(Secant slope `= 0`, but there is no point where the tangent is horizontal).
</details>

10. 🟡 ⭐ $f(x) = e^x$ on $[0, 1]$. Find $c$ and show $1 < e - 1 < e$.
<details>
<summary>Solution</summary>

`f(0) = 1`, `f(1) = e`. Secant slope `= \frac{e - 1}{1 - 0} = e - 1`.
`f'(x) = e^x`. Set `f'(c) = e - 1 \implies e^c = e - 1 \implies c = \ln(e - 1)`.
LMVT guarantees `c \in (0, 1)`. So `0 < \ln(e - 1) < 1`.
Since the exponential function is strictly increasing, exponentiate all parts:
`e^0 < e^{\ln(e - 1)} < e^1 \implies 1 < e - 1 < e`. (Proved).
</details>

---

### Type 3: Proving Inequalities using MVT

**Goal:** Use MVT to establish inequalities of the form $f(b) - f(a) \lessgtr k(b-a)$.

**Solved Example:** ⭐

Prove: $\frac{1}{9} < \ln(e+1) - 1 < \frac{1}{e}$.

**Solution:**
```
Apply LMVT to f(x) = ln x on [e, e+1].
f is continuous on [e, e+1] and differentiable on (e, e+1). ✓

By MVT: ∃ c ∈ (e, e+1) with f'(c) = [ln(e+1) - ln(e)] / [(e+1) - e]
= ln(e+1) - 1  [since ln e = 1]

f'(c) = 1/c.
Since c ∈ (e, e+1): e < c < e+1.
So: 1/(e+1) < 1/c < 1/e.

Therefore: 1/(e+1) < ln(e+1) - 1 < 1/e.
And since e+1 < e² < 9: 1/9 < 1/(e+1). So 1/9 < ln(e+1)-1 < 1/e. ✓
```
🔴 Hard ⭐ Must-Do

**Practice Problems:**

11. 🟡 Prove: $b - a < \sin^{-1}b - \sin^{-1}a$ for $0 < a < b < 1$.
<details>
<summary>Solution</summary>

Let `f(x) = \sin^{-1}x`. Apply LMVT on `[a, b]`:
`\frac{\sin^{-1}b - \sin^{-1}a}{b - a} = f'(c) = \frac{1}{\sqrt{1 - c^2}}` for some `c \in (a, b)`.
Since `0 < a < c < b < 1`, we have `0 < c^2 < 1`.
Thus `1 - c^2 < 1 \implies \sqrt{1 - c^2} < 1 \implies \frac{1}{\sqrt{1 - c^2}} > 1`.
So `\frac{\sin^{-1}b - \sin^{-1}a}{b - a} > 1`.
Since `b > a`, `b - a > 0`, multiply by `b - a` to get:
**\sin^{-1}b - \sin^{-1}a > b - a**. (Proved).
</details>

12. 🟡 Prove: $\frac{b-a}{b} < \ln\frac{b}{a} < \frac{b-a}{a}$ for $0 < a < b$.
<details>
<summary>Solution</summary>

Let `f(x) = \ln x`. Apply LMVT on `[a, b]`:
`\frac{\ln b - \ln a}{b - a} = f'(c) = \frac{1}{c}` for some `c \in (a, b)`.
Since `a < c < b`, we can invert to get: `\frac{1}{b} < \frac{1}{c} < \frac{1}{a}`.
Substitute `1/c`: `\frac{1}{b} < \frac{\ln b - \ln a}{b - a} < \frac{1}{a}`.
Multiply by `b - a` (which is positive):
`\frac{b-a}{b} < \ln\left(\frac{b}{a}\right) < \frac{b-a}{a}`. (Proved).
</details>

13. 🔴 Prove: $e^a(b-a) < e^b - e^a < e^b(b-a)$ for $a < b$.
<details>
<summary>Solution</summary>

Let `f(x) = e^x`. Apply LMVT on `[a, b]`:
`\frac{e^b - e^a}{b - a} = f'(c) = e^c` for some `c \in (a, b)`.
Since `e^x` is a strictly increasing function and `a < c < b`:
`e^a < e^c < e^b`.
Substitute `e^c`: `e^a < \frac{e^b - e^a}{b - a} < e^b`.
Multiply by `b - a` to get the result. (Proved).
</details>

14. 🔴 ⭐ Prove: $|\sin b - \sin a| \leq |b - a|$ for all $a, b$.
<details>
<summary>Solution</summary>

If `a = b`, `0 \leq 0` (true).
If `a \neq b`, apply LMVT to `f(x) = \sin x` on the interval between `a` and `b`:
`\frac{\sin b - \sin a}{b - a} = \cos c` for some `c` between `a` and `b`.
Take absolute value: `\left| \frac{\sin b - \sin a}{b - a} \right| = |\cos c|`.
Since `|\cos c| \leq 1` for all `c`, we have:
`\frac{|\sin b - \sin a|}{|b - a|} \leq 1 \implies |\sin b - \sin a| \leq |b - a|`. (Proved).
</details>

15. 🔴 If $|f'(x)| \leq 1$ for all $x$ and $f(0) = 0$, prove $|f(x)| \leq |x|$.
<details>
<summary>Solution</summary>

If `x = 0`, `f(0) = 0` and `0 \leq 0` (true).
If `x \neq 0`, apply LMVT to `f` on the interval between `0` and `x`:
`\frac{f(x) - f(0)}{x - 0} = f'(c)` for some `c` between `0` and `x`.
So `\frac{f(x)}{x} = f'(c)`.
Take absolute value: `\left| \frac{f(x)}{x} \right| = |f'(c)|`.
We are given `|f'(c)| \leq 1`, so `\frac{|f(x)|}{|x|} \leq 1 \implies |f(x)| \leq |x|`. (Proved).
</details>

---

### Type 4: Applications of MVT Consequences

**Goal:** Use the corollaries about increasing/decreasing functions.

**Solved Example:**

Show that $f(x) = x + \sin x$ is strictly increasing on $\mathbb{R}$.

**Solution:**
```
f'(x) = 1 + cos x.
Since -1 ≤ cos x ≤ 1: f'(x) = 1 + cos x ≥ 0 for all x.
f'(x) = 0 only at x = (2n+1)π — isolated points, not an interval.
By MVT consequence: f is strictly increasing on ℝ.
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

16. 🟡 Show $f(x) = \tan^{-1}x - x < 0$ for $x > 0$.
<details>
<summary>Solution</summary>

`f(0) = 0`.
`f'(x) = \frac{1}{1+x^2} - 1 = \frac{1 - (1+x^2)}{1+x^2} = \frac{-x^2}{1+x^2}`.
For `x > 0`, `f'(x) < 0`. This means `f(x)` is strictly decreasing for `x \geq 0`.
Since `f` is decreasing, for `x > 0`, `f(x) < f(0) \implies f(x) < 0`. (Proved).
</details>

17. 🟡 Show $x > \sin x$ for all $x > 0$.
<details>
<summary>Solution</summary>

Let `f(x) = x - \sin x`. `f(0) = 0`.
`f'(x) = 1 - \cos x`.
Since `-1 \leq \cos x \leq 1`, `f'(x) \geq 0` for all `x`. `f'(x) = 0` only at isolated points `x = 2n\pi`.
So `f(x)` is strictly increasing on `[0, \infty)`.
For `x > 0`, `f(x) > f(0) \implies x - \sin x > 0 \implies x > \sin x`. (Proved).
</details>

18. 🔴 Prove $e^x \geq 1 + x$ for all $x \in \mathbb{R}$.
<details>
<summary>Solution</summary>

Let `f(x) = e^x - x - 1`. `f(0) = e^0 - 0 - 1 = 0`.
`f'(x) = e^x - 1`.
For `x > 0`, `e^x > 1 \implies f'(x) > 0`, so `f` is increasing. Thus `f(x) > f(0) = 0`.
For `x < 0`, `e^x < 1 \implies f'(x) < 0`, so `f` is decreasing. Moving to the left of 0, `f` increases, so `f(x) > f(0) = 0`.
Thus `f(x) \geq 0` for all `x \in \mathbb{R}`, meaning `e^x \geq 1 + x`. (Proved).
</details>

19. 🔴 Show $\ln(1+x) < x$ for all $x > 0$.
<details>
<summary>Solution</summary>

Let `f(x) = x - \ln(1+x)`. `f(0) = 0`.
`f'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x}`.
For `x > 0`, both `x` and `1+x` are positive, so `f'(x) > 0`.
`f(x)` is strictly increasing for `x > 0`.
Thus `f(x) > f(0) \implies x - \ln(1+x) > 0 \implies x > \ln(1+x)`. (Proved).
</details>

20. 🔴 ⭐ If $f''(x) > 0$ on $(a,b)$ and $a < c < b$, show the graph lies above the tangent at $c$.
<details>
<summary>Solution</summary>

The tangent line at `c` is `L(x) = f(c) + f'(c)(x-c)`.
Let `F(x) = f(x) - L(x) = f(x) - f(c) - f'(c)(x-c)`. We must show `F(x) > 0` for `x \neq c`.
`F(c) = 0`. `F'(x) = f'(x) - f'(c)`.
Since `f''(x) > 0`, `f'` is strictly increasing on `(a,b)`.
For `x > c`: `f'(x) > f'(c) \implies F'(x) > 0`. `F` is increasing for `x>c`. Since `F(c)=0`, `F(x) > 0` here.
For `x < c`: `f'(x) < f'(c) \implies F'(x) < 0`. `F` is decreasing for `x<c`. Since `F(c)=0`, `F(x) > 0` here too.
Thus, `F(x) > 0` for all `x \neq c`. (Graph is above the tangent, definition of concave up).
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ Using Rolle's theorem, prove that between any two roots of $f(x) = 0$ there is a root of $f'(x) = 0$.
<details>
<summary>Solution</summary>

Let `x_1` and `x_2` be two distinct roots of `f(x) = 0`, so `f(x_1) = 0` and `f(x_2) = 0`.
Assume `f` is continuous on `[x_1, x_2]` and differentiable on `(x_1, x_2)`.
Since `f(x_1) = f(x_2) = 0`, all conditions for Rolle's Theorem are satisfied.
Therefore, there exists at least one `c \in (x_1, x_2)` such that `f'(c) = 0`.
This `c` is a root of `f'(x) = 0` lying exactly between the two roots of `f(x) = 0`. (Proved).
</details>

2. 🔴 Use LMVT to prove $|\cos b - \cos a| \leq |b - a|$.
<details>
<summary>Solution</summary>

Let `f(x) = \cos x`. Apply LMVT on the interval between `a` and `b`.
`\frac{\cos b - \cos a}{b - a} = f'(c) = -\sin c` for some `c`.
Take the absolute value of both sides: `\left| \frac{\cos b - \cos a}{b - a} \right| = |-\sin c| = |\sin c|`.
Since `|\sin c| \leq 1` for all `c`, we have `\frac{|\cos b - \cos a|}{|b - a|} \leq 1`.
Multiply by `|b - a|`: `|\cos b - \cos a| \leq |b - a|`. (Proved).
</details>

3. 🟡 Apply Rolle's to $f(x) = (x-1)(x-2)(x-3)$ on $[1,3]$ — find BOTH values of $c$.
<details>
<summary>Solution</summary>

`f(x) = x^3 - 6x^2 + 11x - 6`.
`f(1) = 0` and `f(3) = 0`. Continuous and differentiable. Rolle's applies.
`f'(x) = 3x^2 - 12x + 11`. Set `f'(c) = 0`:
`3c^2 - 12c + 11 = 0 \implies c = \frac{12 \pm \sqrt{144 - 132}}{6} = \frac{12 \pm \sqrt{12}}{6} = 2 \pm \frac{2\sqrt{3}}{6} = 2 \pm \frac{1}{\sqrt{3}}`.
Since `1/\sqrt{3} \approx 0.577`, the roots are `\approx 1.423` and `\approx 2.577`.
Both values lie within the interval `(1, 3)`.
**c = 2 - \frac{1}{\sqrt{3}}, 2 + \frac{1}{\sqrt{3}}**.
</details>

4. 🔴 Prove $2\sin^{-1}x < \pi x$ for $x \in (0,1)$ using MVT.
<details>
<summary>Solution</summary>

Let `g(x) = \frac{\sin^{-1}x}{x}`. We want to show `g(x)` is strictly increasing.
`g'(x) = \frac{\frac{x}{\sqrt{1-x^2}} - \sin^{-1}x}{x^2}`.
Let `h(x) = x - \sqrt{1-x^2}\sin^{-1}x`. `h(0) = 0`.
`h'(x) = 1 - \left( -\frac{x}{\sqrt{1-x^2}}\sin^{-1}x + 1 \right) = \frac{x\sin^{-1}x}{\sqrt{1-x^2}}`.
For `x \in (0,1)`, `h'(x) > 0`, so `h(x)` is strictly increasing, meaning `h(x) > h(0) = 0`.
Thus, `\frac{x}{\sqrt{1-x^2}} > \sin^{-1}x`, which means the numerator of `g'(x)` is positive.
Since `g'(x) > 0`, `g(x)` is strictly increasing on `(0, 1)`.
Therefore, `g(x) < \lim_{x\to1^-} g(x) = \frac{\pi/2}{1} = \frac{\pi}{2}`.
`\frac{\sin^{-1}x}{x} < \frac{\pi}{2} \implies` **2\sin^{-1}x < \pi x**. (Proved).
</details>

5. 🔴 Use MVT to show: if $f$ is differentiable and $f(a) = f'(a) = 0$, then $f(x) = 0$ for all $x$ in some neighbourhood if $f''(x) = 0$.
<details>
<summary>Solution</summary>

Since `f''(x) = 0` for all `x`, apply LMVT to `f'` on `[a, x]`:
`\frac{f'(x) - f'(a)}{x - a} = f''(c) = 0`.
Since `f'(a) = 0`, this means `f'(x) = 0` for all `x`.
Now apply LMVT to `f` on `[a, x]`:
`\frac{f(x) - f(a)}{x - a} = f'(d) = 0` (since `f'` is 0 everywhere).
Since `f(a) = 0`, this means `f(x) = 0` for all `x`. (Proved).
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Verify Rolle's theorem for $f(x) = \sin x + \cos x - 1$ on $[0, \pi/2]$. **(4 marks)**

**Solution:**
Polynomials and trig → continuous on $[0,\pi/2]$ ✓; differentiable on $(0,\pi/2)$ ✓.
$f(0) = 0 + 1 - 1 = 0$; $f(\pi/2) = 1 + 0 - 1 = 0$. ✓
By Rolle's: $\exists c$ with $f'(c) = \cos c - \sin c = 0 \Rightarrow \tan c = 1 \Rightarrow c = \pi/4 \in (0,\pi/2)$. ✓

---

**Q2.** 🟡 Verify LMVT for $f(x) = 2x - x^2$ on $[0, 1]$ and find $c$. **(3 marks)**

**Solution:**
Polynomial → conditions satisfied.
$[f(1)-f(0)]/(1-0) = [(2-1) - 0]/1 = 1$.
$f'(x) = 2 - 2x = 1 \Rightarrow x = 1/2 = c \in (0,1)$. ✓

---

**Q3.** 🔴 Prove that $\frac{\pi}{4} < \tan^{-1}\left(\frac{4}{3}\right) < \frac{\pi}{3}$. **(4 marks)**

**Solution:**
Apply MVT to $f(x) = \tan^{-1}x$ on $[1, 4/3]$.
$f(4/3) - f(1) = f'(c)(4/3 - 1) = f'(c)/3$ for some $c \in (1, 4/3)$.
$f'(x) = 1/(1+x^2)$.
For $c \in (1, 4/3)$: $\frac{1}{1+(4/3)^2} < f'(c) < \frac{1}{1+1} = 1/2$.
$\frac{9}{25} < f'(c) < \frac{1}{2}$
$\frac{9}{75} < f(4/3) - \pi/4 < \frac{1}{6}$
$\frac{3}{25} + \pi/4 < \tan^{-1}(4/3) < \frac{1}{6} + \pi/4$

Since $3/25 > 0$: $\tan^{-1}(4/3) > \pi/4$. And $1/6 + \pi/4 < \pi/3$ (check: $\pi/3 - \pi/4 = \pi/12 > 1/6$). ✓

---

## Stage 6: JEE Mains Arena

**Q1.** Which function violates Rolle's theorem on $[-1, 1]$?
<br>(a) $f(x) = x^2$   <br>(b) $f(x) = |x|$   <br>(c) $f(x) = \sin(\pi x)$   <br>(d) $f(x) = x^3 - x$

<details>
<summary>Solution</summary>
(b) |x|: f(-1)=1=f(1), continuous, but NOT differentiable at x=0 (corner). Condition 2 fails.
(a): f(-1)=1=f(1), differentiable. Rolle applies, c=0. ✓
(c): f(-1)=f(1)=0, smooth. ✓
(d): f(-1)=0=f(1), polynomial. ✓
Answer: (b) 🟡 ⭐
</details>

---

**Q2.** If $f(x) = \ln x$ and LMVT is applied on $[1,e]$, then $c =$:
<br>(a) $e-1$   <br>(b) $\frac{e-1}{\ln(e-1)}$   <br>(c) $e-1$   <br>(d) $\frac{e-1}{1} = e-1$

<details>
<summary>Solution</summary>
[f(e) - f(1)]/(e-1) = (1-0)/(e-1) = 1/(e-1).
f'(c) = 1/c = 1/(e-1). So c = e-1. ∈(1,e) ✓ (since 1 < e-1 ≈ 1.718 < e).
Answer: (a)/(c)/(d) — all same, c = e-1. 🟡
</details>

---

**Q3.** By LMVT, for any $a < b$, $\frac{\sin b - \sin a}{b - a}$ equals $\cos c$ for some $c \in (a,b)$. This means:
<br>(a) $|\sin b - \sin a| = |b-a|$   <br>(b) $|\sin b - \sin a| \leq |b-a|$   <br>(c) $|\sin b - \sin a| \geq |b-a|$   <br>(d) $\sin b - \sin a = b - a$

<details>
<summary>Solution</summary>
cos c ∈ [-1, 1], so |cos c| ≤ 1.
|sin b - sin a| = |cos c| · |b-a| ≤ |b-a|.
Answer: (b) 🟡 ⭐
</details>

---

**Q4.** Let $f(x) = (x-1)^2(x+1)^3$. Rolle's theorem guarantees a root of $f'$ in:
<br>(a) $(-1, 0)$   <br>(b) $(0, 1)$   <br>(c) $(-1, 1)$   <br>(d) Both (a) and (b)

<details>
<summary>Solution</summary>
f(-1) = 0 = f(1). So Rolle's applies on [-1,1]. ∃ c ∈ (-1,1) with f'(c)=0.
But f has roots at x=-1 and x=1, and between any two roots of f lies a root of f'.
f' also has roots between consecutive roots of f.
By inspection, c could be in both (-1,0) and (0,1).
Answer: (d) 🔴
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** Rolle's theorem is a special case of LMVT.
<br>**Reason (R):** When $f(a) = f(b)$, the secant slope is 0, and LMVT gives $f'(c) = 0$.

<details>
<summary>Solution</summary>
A is true: Rolle's is indeed a special case with the added condition f(a)=f(b).
R is true and gives the exact derivation.
Answer: (a) 🟢 ⭐
</details>

---

**Q2.**
<br>**Assertion (A):** If $f'(c) = 0$ at some $c \in (a,b)$, then Rolle's theorem applies on $[a,b]$.
<br>**Reason (R):** Rolle's theorem only states existence of $c$; it doesn't require $f(a)=f(b)$.

<details>
<summary>Solution</summary>
A is false: Rolle's theorem is a sufficient condition — it guarantees c exists IF the conditions hold. The converse (existence of c → conditions hold) is not necessarily true.
R is false: Rolle's theorem DOES require f(a)=f(b).
Answer: (d) 🔴
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 For Rolle's theorem, we need $f(a) = f(b)$ PLUS:
   <br>(a) $f$ is differentiable on $(a,b)$ only   <br>(b) $f$ is continuous on $[a,b]$ only   <br>(c) Both continuity on $[a,b]$ and differentiability on $(a,b)$   <br>(d) $f(a) = f(b) = 0$

2. 🟡 LMVT guarantees a $c$ where the tangent slope equals:
   <br>(a) $f'(a)$   <br>(b) $f'(b)$   <br>(c) $[f(b)-f(a)]/(b-a)$   <br>(d) $[f(a)+f(b)]/2$

3. 🟡 ⭐ Rolle's theorem applied to $f(x) = e^x\sin x$ on $[0, \pi]$ gives $c =$:
   <br>(a) $\pi/4$   <br>(b) $3\pi/4$   <br>(c) $\pi/2$   <br>(d) Not applicable

4. 🟡 $f(x) = |x-1|$ on $[-1,3]$. Rolle's theorem:
   <br>(a) Applies, $c=1$   <br>(b) Applies, $c=2$   <br>(c) Does not apply; f is not differentiable at $x=1$   <br>(d) Applies, $c=-1$

5. 🔴 ⭐ By LMVT on $[2,4]$ for $f(x) = \sqrt{x}$, $c =$:
   <br>(a) $3$   <br>(b) $(\sqrt{2}+2)^2$   <br>(c) $3.something$   <br>(d) $3.0$

6. 🟡 If $f$ is continuous on $[0,1]$, differentiable on $(0,1)$, and $f(0) = f(1) = 0$, then by Rolle's:
   <br>(a) $f$ has no roots in $(0,1)$   <br>(b) $f'$ has at least one root in $(0,1)$   <br>(c) $f' > 0$ always   <br>(d) $f$ is constant

7. 🔴 For $f(x) = x^3 - 3x$ on $[-\sqrt{3}, \sqrt{3}]$, value(s) of $c$ from Rolle's:
   <br>(a) $0$ only   <br>(b) $\pm 1$   <br>(c) $1$ only   <br>(d) $-1$ only

8. 🔴 ⭐ If $|f'(x)| \leq 2$ for all $x \in [1,4]$ and $f(1) = 3$, then $f(4)$ lies in:
   <br>(a) $[-3, 9]$   <br>(b) $[0, 6]$   <br>(c) $[-3, 9]$   <br>(d) $[-3, 6]$ — No, by MVT $|f(4)-f(1)| \leq 2 \times 3 = 6$, so $f(4) \in [-3, 9]$.

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | c | 5 | b |
| 2 | c | 6 | b |
| 3 | b | 7 | b |
| 4 | c | 8 | a |

</details>

---

## What's Next?

Mean Value Theorems are powerful but limited: they guarantee $c$ exists without telling you the exact value. What if you actually need to compute a limit of the form $0/0$ or $\infty/\infty$? In **Chapter 13**, we learn **L'Hôpital's Rule** — the direct application of derivatives to resolve these otherwise impossible limits.
