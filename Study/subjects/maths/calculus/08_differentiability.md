# Chapter 8: Differentiability

---

## Stage 1: The Core Idea

### The Sharp Corner Problem

Look at the graph of $y = |x|$. It's perfectly continuous — you can draw the whole thing without lifting your pencil. But at $x = 0$, it has a **sharp corner**.

Try to define the slope at that corner. From the left, the slope is $-1$. From the right, the slope is $+1$. The slope is different depending on which direction you approach from. There's no single, agreed-upon slope.

That's the essence of non-differentiability.

> A function is **differentiable** at $x=a$ if it has a unique, well-defined tangent line slope there.

### The Key Relationship

$$\text{Differentiable at } a \implies \text{Continuous at } a$$

But the converse is NOT true:
$$\text{Continuous at } a \not\implies \text{Differentiable at } a$$

**Memory aid:** Differentiability is the stricter, more demanding condition. Continuity is necessary but not sufficient.

---

## Stage 2: The Formula Lab

### Left-Hand Derivative (LHD) and Right-Hand Derivative (RHD)

$$\text{LHD} = \lim_{h \to 0^-} \frac{f(a+h) - f(a)}{h} = \lim_{x \to a^-} \frac{f(x)-f(a)}{x-a}$$

$$\text{RHD} = \lim_{h \to 0^+} \frac{f(a+h) - f(a)}{h} = \lim_{x \to a^+} \frac{f(x)-f(a)}{x-a}$$

> $f$ is differentiable at $a$ if and only if **LHD = RHD** (and the common value is $f'(a)$).

### Non-Differentiable Points

| Type | Graph Behaviour | Example |
|------|----------------|---------|
| **Corner** | Two distinct tangent slopes | $|x|$ at $x=0$ |
| **Cusp** | Slopes tend to $+\infty$ from one side, $-\infty$ from the other | $x^{2/3}$ at $x=0$ |
| **Vertical Tangent** | Both slopes tend to $\pm\infty$ | $\sqrt[3]{x}$ at $x=0$ |
| **Discontinuity** | No tangent can be defined | $[x]$ at integers |

### Differentiability on an Interval

$f$ is differentiable on $(a, b)$ if it is differentiable at every point inside $(a, b)$. For a closed interval $[a,b]$, the endpoints are checked using only one-sided derivatives (RHD at $a$, LHD at $b$).

---

## Stage 3: Type-wise Mastery

### Type 1: LHD / RHD at a Given Point

**Goal:** Compute both one-sided derivatives and check if they match.

**Solved Example:** ⭐

Check differentiability of $f(x) = |x-2|$ at $x = 2$.

**Solution:**
```
Note: f(x) = -(x-2) for x < 2 and f(x) = (x-2) for x ≥ 2.

LHD = lim(h→0⁻) [f(2+h) - f(2)] / h
= lim(h→0⁻) [|2+h-2| - 0] / h
= lim(h→0⁻) |h| / h
= lim(h→0⁻) (-h) / h    [since h < 0, |h| = -h]
= -1

RHD = lim(h→0⁺) [f(2+h) - f(2)] / h
= lim(h→0⁺) |h| / h
= lim(h→0⁺) h / h = 1

LHD = -1 ≠ RHD = 1
∴ f is NOT differentiable at x = 2.
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

1. 🟢 Check differentiability of $f(x) = |x+3|$ at $x=-3$.
<details>
<summary>Solution</summary>

The graph of `|x+3|` has a sharp V-shaped corner at `x=-3`.
LHD: `\lim_{h\to0^-} \frac{|(-3+h)+3| - 0}{h} = \lim_{h\to0^-} \frac{|h|}{h} = \frac{-h}{h} = -1`.
RHD: `\lim_{h\to0^+} \frac{|h|}{h} = \frac{h}{h} = 1`.
LHD $\neq$ RHD. **Not differentiable** at `x=-3`.
</details>

2. 🟡 $f(x) = \begin{cases} x^2 & x \leq 1 \\ 2x-1 & x > 1 \end{cases}$ at $x=1$.
<details>
<summary>Solution</summary>

Check continuity: `f(1^-) = 1^2 = 1`. `f(1^+) = 2(1)-1 = 1`. Continuous. ✓
LHD: derivative of `x^2` at `x=1` is `2x \big|_{x=1} = 2`.
RHD: derivative of `2x-1` at `x=1` is `2`.
LHD = RHD = 2. **Differentiable** at `x=1`.
</details>

3. 🟡 ⭐ $f(x) = \begin{cases} x^2 + 1 & x \leq 0 \\ \cos x & x > 0 \end{cases}$ at $x=0$.
<details>
<summary>Solution</summary>

Continuity: `f(0) = 0^2 + 1 = 1`. `\lim_{x\to0^+} \cos x = \cos 0 = 1`. Continuous. ✓
LHD: `d/dx(x^2 + 1) = 2x \implies 2(0) = 0`.
RHD: `d/dx(\cos x) = -\sin x \implies -\sin 0 = 0`.
LHD = RHD = 0. **Differentiable** at `x=0`.
</details>

4. 🔴 $f(x) = x|x|$ at $x=0$. Is it differentiable?
<details>
<summary>Solution</summary>

Rewrite: `f(x) = \begin{cases} -x^2 & x < 0 \\ x^2 & x \geq 0 \end{cases}`.
LHD: `d/dx(-x^2) = -2x \implies -2(0) = 0`.
RHD: `d/dx(x^2) = 2x \implies 2(0) = 0`.
LHD = RHD = 0. **Yes, differentiable** at `x=0` (and `f'(0) = 0`).
</details>

5. 🔴 $f(x) = \begin{cases} \sin x & x < \pi/2 \\ \cos x & x \geq \pi/2 \end{cases}$ at $x = \pi/2$.
<details>
<summary>Solution</summary>

Check continuity first!
`\lim_{x\to\pi/2^-} \sin x = \sin(\pi/2) = 1`.
`f(\pi/2) = \cos(\pi/2) = 0`.
Since LHL $\neq$ Value, `f(x)` is discontinuous at `x = \pi/2`.
Therefore, it is **not differentiable** (don't even bother checking LHD/RHD).
</details>

---

### Type 2: Piecewise Functions — Finding Constants for Differentiability

**Goal:** Since differentiability implies continuity, use BOTH conditions: continuity equation + equal derivatives.

**Solved Example:** ⭐

Find $a$ and $b$ so that $f(x) = \begin{cases} ax^2 + b & x \leq 1 \\ 2x + 1 & x > 1 \end{cases}$ is differentiable at $x = 1$.

**Solution:**
```
Continuity at x=1: f(1⁻) = f(1⁺)
a(1)² + b = 2(1) + 1
a + b = 3  ... (1)

Equal derivatives at x=1:
LHD: d/dx(ax² + b) at x=1 = 2ax|_{x=1} = 2a
RHD: d/dx(2x + 1) at x=1 = 2

For differentiability: 2a = 2 ⟹ a = 1
From (1): 1 + b = 3 ⟹ b = 2
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟡 Find $a, b$ so that $f(x) = \begin{cases} ax + b & x \leq 2 \\ x^2 & x > 2 \end{cases}$ is differentiable at $x=2$.
<details>
<summary>Solution</summary>

Continuity at `x=2`: `2a + b = 2^2 \implies 2a + b = 4`.
Equal derivatives at `x=2`: LHD = `a`, RHD = `2x|_{x=2} = 4`.
So **a = 4**.
Substitute `a` into continuity eq: `2(4) + b = 4 \implies 8 + b = 4 \implies` **b = -4**.
</details>

7. 🟡 ⭐ $f(x) = \begin{cases} x^2 + ax + b & x < 1 \\ 3x + 2 & x \geq 1 \end{cases}$ is differentiable at $x=1$. Find $a, b$.
<details>
<summary>Solution</summary>

Continuity at `x=1`: `1^2 + a(1) + b = 3(1) + 2 \implies 1 + a + b = 5 \implies a + b = 4`.
Equal derivatives at `x=1`: LHD = `2x + a \big|_{x=1} = 2 + a`. RHD = `3`.
`2 + a = 3 \implies` **a = 1**.
Substitute `a`: `1 + b = 4 \implies` **b = 3**.
</details>

8. 🔴 $f(x) = \begin{cases} p\sin x + q\cos x & x \leq 0 \\ e^x & x > 0 \end{cases}$ is differentiable at $x=0$. Find $p, q$.
<details>
<summary>Solution</summary>

Continuity at `x=0`: LHL = `p(0) + q(1) = q`. RHL = `e^0 = 1`.
`q = 1`.
Derivatives:
LHD at `x=0`: `p\cos x - q\sin x \big|_{x=0} = p(1) - q(0) = p`.
RHD at `x=0`: `e^x \big|_{x=0} = 1`.
For differentiability, LHD = RHD, so **p = 1**. **q = 1**.
</details>

9. 🔴 $f(x) = \begin{cases} ax^2 + bx & x \geq 1 \\ \frac{1}{x} & x < 1 \end{cases}$ is differentiable at $x=1$. Find $a, b$.
<details>
<summary>Solution</summary>

Continuity at `x=1`: RHL = `a(1)^2 + b(1) = a + b`. LHL = `1/1 = 1`.
`a + b = 1`.
Derivatives at `x=1`:
RHD = `2ax + b \big|_{x=1} = 2a + b`.
LHD = `d/dx(1/x) = -1/x^2 \big|_{x=1} = -1`.
So `2a + b = -1`.
Subtract the equations: `(2a + b) - (a + b) = -1 - 1 \implies` **a = -2**.
Since `-2 + b = 1 \implies` **b = 3**.
</details>

10. 🔴 $f(x) = \begin{cases} |x-1|\sin\frac{1}{x-1} & x \neq 1 \\ 0 & x = 1 \end{cases}$. Is $f$ differentiable at $x=1$?
<details>
<summary>Solution</summary>

Use the definition.
LHD: `\lim_{h\to0^-} \frac{|h|\sin(1/h) - 0}{h}`. Since `h < 0`, `|h| = -h`.
`= \lim_{h\to0^-} \frac{-h \sin(1/h)}{h} = \lim_{h\to0^-} -\sin(1/h)`.
This limit oscillates between -1 and 1, so it **does not exist**.
Since the LHD does not exist, `f` is **not differentiable** at `x=1`.
*(However, if it were `(x-1)^2 \sin \dots`, it would be differentiable).*
</details>

---

### Type 3: Non-Differentiability of Special Functions

**Goal:** Identify all points where $|f(x)|$, $[x]$, $\{x\}$, or $x^{n/m}$ fail to be differentiable.

**Solved Example:** ⭐

Find all points of non-differentiability of $f(x) = ||x| - 1|$.

**Solution:**
```
Step 1: |x| has a corner at x = 0.
Step 2: |x| - 1 is 0 when |x| = 1, i.e., x = ±1.
Step 3: ||x| - 1| has corners wherever the inner expression is 0.

Non-differentiable at: x = -1, 0, 1

Check: At these three points, LHD ≠ RHD.
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

11. 🟡 Find all points where $f(x) = |x^2 - 4|$ is not differentiable.
<details>
<summary>Solution</summary>

The function inside the absolute value is `x^2 - 4 = (x-2)(x+2)`.
The roots are `x = 2` and `x = -2`.
At these single roots, the graph of `x^2 - 4` crosses the x-axis, creating sharp corners when the absolute value flips the negative parts up.
**Non-differentiable points:** `x = 2` and `x = -2`.
</details>

12. 🟡 ⭐ Find all points where $f(x) = |x|^{3/2}$ is not differentiable. *[Hint: cusp?]*
<details>
<summary>Solution</summary>

Let's check `x=0`.
LHD = `\lim_{h\to0^-} \frac{|h|^{3/2} - 0}{h} = \lim_{h\to0^-} \frac{(-h)^{3/2}}{-(-h)} = \lim_{h\to0^-} -(-h)^{1/2} = 0`.
RHD = `\lim_{h\to0^+} \frac{h^{3/2}}{h} = \lim_{h\to0^+} h^{1/2} = 0`.
Since LHD = RHD = 0, it IS differentiable at `x=0`.
**Conclusion:** There are **no points** of non-differentiability. (It's differentiable everywhere).
</details>

13. 🔴 Find all non-differentiable points of $f(x) = \max(x, x^2)$.
<details>
<summary>Solution</summary>

Plot `y = x` and `y = x^2`. They intersect at `x=0` and `x=1`.
For `x < 0`, `x^2 > x` (e.g., at -1, 1 > -1). So `f(x) = x^2`.
For `0 \leq x \leq 1`, `x \geq x^2` (e.g., at 0.5, 0.5 > 0.25). So `f(x) = x`.
For `x > 1`, `x^2 > x`. So `f(x) = x^2`.
The function changes definition at `x=0` and `x=1`.
At `x=0`: LHD (from `x^2`) = 0, RHD (from `x`) = 1. Not diff.
At `x=1`: LHD (from `x`) = 1, RHD (from `x^2`) = 2. Not diff.
**Non-differentiable at:** `x = 0, 1`.
</details>

14. 🔴 Is $f(x) = x^{2/3}$ differentiable at $x=0$? *[Hint: LHD and RHD both go to $\pm\infty$]*
<details>
<summary>Solution</summary>

LHD = `\lim_{h\to0^-} \frac{h^{2/3} - 0}{h} = \lim_{h\to0^-} \frac{1}{h^{1/3}}`. As `h` is a tiny negative, `h^{1/3}` is a tiny negative, so LHD $\to -\infty$.
RHD = `\lim_{h\to0^+} \frac{1}{h^{1/3}} \to +\infty`.
The limit does not exist (it's infinite). This forms a **cusp** on the graph.
**Not differentiable** at `x=0`.
</details>

15. 🔴 ⭐ For $f(x) = \min(|x|, |x-1|, |x+1|)$, find all non-differentiable points.
<details>
<summary>Solution</summary>

This graph looks like a series of tiny tents (sawtooth wave).
We find the intersections of the absolute value graphs:
`|x| = |x-1| \implies x^2 = (x-1)^2 \implies x = 1/2`.
`|x| = |x+1| \implies x = -1/2`.
Also, the "tips" of the tents are at the roots: `x = -1, 0, 1`.
The function will have sharp corners at all of these intersection points and roots.
**Non-differentiable at:** `x = -1, -1/2, 0, 1/2, 1`. (5 points).
</details>

---

### Type 4: Differentiability from Functional Equations

**Goal:** Use given functional properties to find LHD, RHD, or $f'(0)$.

**Solved Example:** ⭐

$f(x+y) = f(x) + f(y)$ for all $x, y$. If $f'(0)$ exists and equals 1, find $f'(x)$.

**Solution:**
```
f'(x) = lim(h→0) [f(x+h) - f(x)] / h
     = lim(h→0) [f(x) + f(h) - f(x)] / h  [using the functional equation]
     = lim(h→0) f(h) / h

From f(x+y) = f(x)+f(y), put x=y=0: f(0) = 2f(0) ⟹ f(0) = 0.
So f'(x) = lim(h→0) f(h)/h = lim(h→0) [f(h) - f(0)]/h = f'(0) = 1.

∴ f'(x) = 1 for all x.
```
🔴 Hard ⭐ Must-Do

**Practice Problems:**

16. 🟡 If $f(x+y) = f(x)f(y)$ for all $x,y$ and $f'(0) = 2$, find $f'(x)$.
<details>
<summary>Solution</summary>

`f'(x) = \lim_{h\to0} \frac{f(x+h) - f(x)}{h} = \lim_{h\to0} \frac{f(x)f(h) - f(x)}{h} = f(x) \lim_{h\to0} \frac{f(h) - 1}{h}`.
Since `f(0+0) = f(0)f(0) \implies f(0) = 1` (assuming `f \neq 0`).
So `\lim_{h\to0} \frac{f(h) - f(0)}{h} = f'(0) = 2`.
Therefore, `f'(x) =` **2f(x)**.
</details>

17. 🟡 If $f(xy) = f(x) + f(y)$ and $f'(1) = 1$, find $f'(x)$.
<details>
<summary>Solution</summary>

`f'(x) = \lim_{h\to0} \frac{f(x+h) - f(x)}{h} = \lim_{h\to0} \frac{f(x(1 + h/x)) - f(x)}{h}`.
`= \lim_{h\to0} \frac{f(x) + f(1 + h/x) - f(x)}{h} = \lim_{h\to0} \frac{f(1 + h/x)}{h}`.
Let `t = h/x`. As `h \to 0`, `t \to 0`, and `h = xt`.
`= \lim_{t\to0} \frac{f(1+t)}{xt} = \frac{1}{x} \lim_{t\to0} \frac{f(1+t) - 0}{t}`.
Since `f(1) = 0`, this is `\frac{1}{x} f'(1) = \frac{1}{x}(1) =` **\frac{1}{x}**.
</details>

18. 🔴 If $f(x+y) = f(x) + f(y) + xy$ and $f'(0) = 0$, find $f'(2)$.
<details>
<summary>Solution</summary>

`f'(x) = \lim_{h\to0} \frac{f(x+h) - f(x)}{h} = \lim_{h\to0} \frac{f(x) + f(h) + xh - f(x)}{h}`.
`= \lim_{h\to0} \left( \frac{f(h)}{h} + x \right)`.
Since `f(0) = 0`, the limit `f(h)/h` is `f'(0) = 0`.
So `f'(x) = x`.
Then `f'(2) =` **2**.
</details>

19. 🔴 If $|f(x) - f(y)| \leq |x-y|^2$ for all $x,y$, prove $f$ is constant.
<details>
<summary>Solution</summary>

Divide by `|x-y|` (for `x \neq y`):
`\left|\frac{f(x) - f(y)}{x-y}\right| \leq |x-y|`.
Take the limit as `x \to y`:
`|f'(y)| \leq 0`.
Since absolute value cannot be negative, `|f'(y)| = 0 \implies f'(y) = 0` for all `y`.
Since the derivative is zero everywhere, `f(x)` is a **constant**.
</details>

20. 🔴 ⭐ $f(x+y) = \frac{f(x)+f(y)}{1-f(x)f(y)}$. If $f'(0)$ exists, find $f'(x)$ in terms of $f(x)$.
<details>
<summary>Solution</summary>

This is the tangent addition formula! Let `f'(0) = k`. Note `f(0) = 0`.
`f'(x) = \lim_{h\to0} \frac{1}{h} \left( \frac{f(x)+f(h)}{1-f(x)f(h)} - f(x) \right)`.
`= \lim_{h\to0} \frac{1}{h} \left( \frac{f(x) + f(h) - f(x) + f^2(x)f(h)}{1-f(x)f(h)} \right)`.
`= \lim_{h\to0} \frac{f(h)(1+f^2(x))}{h(1-f(x)f(h))}`.
Since `\lim_{h\to0} \frac{f(h)}{h} = f'(0)` and `f(h) \to 0`, the limit evaluates to:
`f'(x) =` **f'(0) (1 + [f(x)]^2)**.
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ $f(x) = \begin{cases} x^2 \sin(1/x) & x \neq 0 \\ 0 & x = 0 \end{cases}$. Show $f$ is differentiable at $x=0$ but $f'$ is not continuous at $x=0$.
<details>
<summary>Solution</summary>

Differentiability at `x=0`: `f'(0) = \lim_{h\to0} \frac{h^2 \sin(1/h) - 0}{h} = \lim_{h\to0} h \sin(1/h) = 0`. So it IS differentiable.
Derivative for `x \neq 0`: `f'(x) = 2x\sin(1/x) - \cos(1/x)`.
Check continuity of `f'` at 0: `\lim_{x\to0} f'(x) = \lim_{x\to0} (2x\sin(1/x) - \cos(1/x))`.
The first term goes to 0, but `\cos(1/x)` oscillates between -1 and 1. Limit does not exist.
Therefore, `f'` is NOT continuous at `x=0`.
</details>

2. 🔴 $f(x) = \max(2-x, 2, x+1)$. Find all points of non-differentiability.
<details>
<summary>Solution</summary>

Find the intersection points of the functions:
`2-x = 2 \implies x = 0`.
`2 = x+1 \implies x = 1`.
Plotting them reveals:
For `x < 0`, `2-x` is highest.
For `0 \leq x \leq 1`, `2` is highest.
For `x > 1`, `x+1` is highest.
So `f(x)` changes definition at `x=0` and `x=1`, creating sharp corners.
**Non-differentiable at:** `x = 0, 1`.
</details>

3. 🟡 If $f(x) = |x-3| + |4-x| + |x-4|$ on $[3,5]$, find number of non-differentiable points.
<details>
<summary>Solution</summary>

Simplify: `|4-x| = |x-4|`, so `f(x) = |x-3| + 2|x-4|`.
The roots of the absolute value terms are `x=3` and `x=4`.
Inside the interval `(3,5)`, the only sharp corner is at `x=4`. (At the boundary `x=3`, one-sided derivative exists, but strictly speaking, it's a "corner" of the full graph).
In the interior, there is **1** non-differentiable point: `x = 4`.
</details>

4. 🔴 $g(x) = \int_0^x f(t) \, dt$ where $f(t) = |t-1|$. Is $g$ differentiable at $x=1$?
<details>
<summary>Solution</summary>

By the Fundamental Theorem of Calculus, `g'(x) = f(x)` IF `f(x)` is continuous.
Since `f(t) = |t-1|` is continuous everywhere (including at `t=1`), `g'(1)` exists and equals `f(1) = 0`.
So **YES**, `g(x)` is differentiable at `x=1` (even though `f` is not differentiable there).
</details>

5. 🔴 If $f(x) = [x]\sin(\pi x)$, find all points in $(0,3)$ where $f$ is not differentiable.
<details>
<summary>Solution</summary>

The potential points are integers `x=1` and `x=2`.
At `x=1`: LHD `\to \lim_{h\to0^+} \frac{[1-h]\sin(\pi(1-h))}{(-h)} = 0`. RHD `\to \lim_{h\to0^+} \frac{1(-\sin(\pi h))}{h} = -\pi`. LHD $\neq$ RHD.
At `x=2`: LHD `\to \lim_{h\to0^+} \frac{1(-\sin(\pi h))}{-h} = \pi`. RHD `\to \lim_{h\to0^+} \frac{2\sin(\pi h)}{h} = 2\pi`. LHD $\neq$ RHD.
**Non-differentiable points:** `x = 1, 2`.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Show that $f(x) = |x|$ is continuous but not differentiable at $x=0$. **(3 marks)**

**Solution:**
Continuity: $f(0) = 0$. $\lim_{x\to0} |x| = 0 = f(0)$. ✓ Continuous.

Differentiability:
LHD = $\lim_{h\to0^-} |h|/h = -1$.
RHD = $\lim_{h\to0^+} |h|/h = 1$.
LHD $\neq$ RHD. ∴ Not differentiable at $x=0$.

---

**Q2.** 🟡 Find $a$ and $b$ so that $f(x) = \begin{cases} ax+b & x \leq 2 \\ x^2 - 5 & x > 2 \end{cases}$ is differentiable at $x=2$. **(4 marks)**

**Solution:**
Continuity: $2a + b = 4 - 5 = -1$ ... (1)
Equal derivatives: LHD = $a$; RHD = $2x|_{x=2} = 4$.
$\Rightarrow a = 4$
From (1): $8 + b = -1 \Rightarrow b = -9$.

---

## Stage 6: JEE Mains Arena

**Q1.** Let $f(x) = \begin{cases} x^n \sin(1/x) & x \neq 0 \\ 0 & x=0 \end{cases}$. $f$ is differentiable at $x=0$ when:
<br>(a) $n \geq 1$   <br>(b) $n \geq 2$   <br>(c) $n \leq 1$   <br>(d) Any $n$

<details>
<summary>Solution</summary>
f'(0) = lim(h→0) h^n sin(1/h) / h = lim(h→0) h^{n-1} sin(1/h).
For this limit to exist (= 0), we need h^{n-1} → 0 faster than sin(1/h) oscillates.
|h^{n-1} sin(1/h)| ≤ |h^{n-1}| → 0 requires n-1 > 0, i.e., n > 1, meaning n ≥ 2.
Answer: (b) 🔴 ⭐
</details>

---

**Q2.** $f(x) = \begin{cases} 1 + |x| & x < -1 \\ [x] & -1 \leq x \leq 1 \\ -1 + |x| & x > 1 \end{cases}$. Number of points of discontinuity:
<br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $3$

<details>
<summary>Solution</summary>
At x=-1: LHL = 1+|-1| = 2; RHL = [-1] = -1. Jump discontinuity. ✗
At x=0: Piece is [x], which is 0 on [-1,0) and 0 at 0. Continuous.
At x=1: LHL = [1⁻] = 0; RHL = -1+|1| = 0. Equal! Continuous.
Discontinuous only at x=-1.
Answer: (b) 🔴
</details>

---

**Q3.** The total number of points where $f(x) = |x+1| + |x-1|$ is NOT differentiable:
<br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $3$

<details>
<summary>Solution</summary>
Corner points at x = -1 and x = 1.
Check: LHD and RHD differ at both x=-1 and x=1.
Total: 2 points.
Answer: (c) 🟡
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** If $f$ is differentiable at $x=a$, then $f$ is continuous at $x=a$.
<br>**Reason (R):** $f(x)-f(a) = \frac{f(x)-f(a)}{x-a} \cdot (x-a) \to f'(a) \cdot 0 = 0$ as $x \to a$.

<details>
<summary>Solution</summary>
A is true: standard theorem.
R is true and gives the correct proof.
Answer: (a) 🟡 ⭐
</details>

---

**Q2.**
<br>**Assertion (A):** $f(x) = x^{1/3}$ is not differentiable at $x=0$.
<br>**Reason (R):** LHD = $-\infty$ and RHD = $+\infty$ at $x=0$.

<details>
<summary>Solution</summary>
A is true: vertical tangent at x=0.
R is false: Both LHD and RHD → +∞ (the cube root function's slope goes to +∞ from both sides). It's a vertical tangent, not a corner.
Answer: (c) 🔴
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 Differentiability at a point $\Rightarrow$:
   <br>(a) Only continuity   <br>(b) Differentiability everywhere   <br>(c) $f(a) = 0$   <br>(d) The derivative is constant

2. 🟡 $f(x) = |x|^3$ is differentiable at $x=0$:
   <br>(a) Yes, $f'(0) = 0$   <br>(b) No   <br>(c) Yes, $f'(0) = 1$   <br>(d) $f'(0)$ does not exist

3. 🟡 ⭐ Number of points where $f(x) = |x-1| + |x-2| + |x-3|$ is NOT differentiable:
   <br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $3$

4. 🟡 If $f(x) = [x]$ (floor function), $f$ is NOT differentiable at:
   <br>(a) No point   <br>(b) All integers   <br>(c) All non-integers   <br>(d) Only $x=0$

5. 🔴 ⭐ $f(x) = \begin{cases} ax^2 + bx & x < 1 \\ 2x + 1 & x \geq 1 \end{cases}$ is differentiable at $x=1$. Then $a-b=$:
   <br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $-1$

6. 🔴 $f(x) = x|x|$ is differentiable at $x=0$. $f'(0) =$:
   <br>(a) $0$   <br>(b) $1$   <br>(c) $-1$   <br>(d) Does not exist

7. 🟡 ⭐ $f(x) = \max(x, x^3)$ is NOT differentiable at:
   <br>(a) $x = 0$ only   <br>(b) $x = 1$ only   <br>(c) $x = -1$ and $x=1$   <br>(d) $x=-1$, $x=0$, $x=1$

8. 🔴 If $f$ is differentiable at $x=0$ and $f(x+y) = f(x)+f(y)+2xy$, with $f'(0)=3$, then $f'(x) =$:
   <br>(a) $3$   <br>(b) $3+2x$   <br>(c) $2x$   <br>(d) $3+x$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | a | 5 | b |
| 2 | a | 6 | a |
| 3 | d | 7 | d |
| 4 | b | 8 | b |

</details>

---

## What's Next?

Now you can precisely classify every function as continuous and/or differentiable. But what about $y = \sqrt{x^2 + \sin(e^x)}$? Even with all our rules, differentiating deeply nested functions is awkward. In **Chapter 9**, we study **Implicit and Parametric Differentiation** — powerful techniques for curves and equations where $y$ is not isolated.
