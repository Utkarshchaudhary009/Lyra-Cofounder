# Chapter 7: Continuity

---

## Stage 1: The Core Idea

### The Broken Bridge

Imagine driving over a bridge. You're going smoothly — then suddenly there's a gap. You can't cross.

Or imagine a road that abruptly drops 10 feet, then continues at the lower level.

Mathematically, a function is **continuous** at a point if it has no such "gap", "jump", or "hole" at that point. The graph can be drawn without lifting your pencil.

### Three Conditions for Continuity

A function $f(x)$ is continuous at $x = a$ if and only if **ALL THREE** of the following hold:

1. **$f(a)$ is defined** (there's no hole at $x=a$)
2. **$\lim_{x \to a} f(x)$ exists** (the function approaches the same value from both sides)
3. **$\lim_{x \to a} f(x) = f(a)$** (the limit equals the actual value)

If ANY one of these fails, the function is **discontinuous** at $x = a$.

---

## Stage 2: The Formula Lab

### Types of Discontinuity

| Type | What Happens | Example |
|------|-------------|---------|
| **Removable** (Hole) | Limit exists, but $f(a)$ is either undefined or $\neq$ limit | $f(x) = \frac{x^2-1}{x-1}$ at $x=1$ |
| **Jump** | LHL $\neq$ RHL | $f(x) = \begin{cases} 1 & x < 0 \\ -1 & x \geq 0 \end{cases}$ |
| **Infinite** | $f(x) \to \pm\infty$ | $f(x) = \frac{1}{x}$ at $x=0$ |
| **Oscillatory** | Function oscillates with no limit | $f(x) = \sin(1/x)$ at $x=0$ |

### Continuity of Standard Functions

| Function | Continuous On |
|----------|--------------|
| Polynomials | $(-\infty, \infty)$ — always |
| Rational $f(x)/g(x)$ | Everywhere except where $g(x) = 0$ |
| $\sqrt{x}$ | $[0, \infty)$ |
| $\sin x$, $\cos x$ | $(-\infty, \infty)$ |
| $\tan x$ | Everywhere except $x = \pi/2 + n\pi$ |
| $e^x$, $a^x$ | $(-\infty, \infty)$ |
| $\ln x$ | $(0, \infty)$ |
| $|x|$ | $(-\infty, \infty)$ |
| $[x]$ (floor) | All non-integers (jump at every integer) |

### Intermediate Value Theorem (IVT)

> If $f$ is continuous on $[a, b]$ and $k$ is any number between $f(a)$ and $f(b)$, then there exists at least one $c \in (a, b)$ such that $f(c) = k$.

**Practical use:** If $f$ is continuous on $[a,b]$ and $f(a) < 0 < f(b)$, then $f$ has at least one root in $(a,b)$.

---

## Stage 3: Type-wise Mastery

### Type 1: Testing Continuity at a Point (3-Step Test)

**Goal:** Check all three conditions for a given function at a given point.

**Solved Example:** ⭐

Test continuity of $f(x) = \begin{cases} \frac{x^2-4}{x-2} & x \neq 2 \\ 5 & x = 2 \end{cases}$ at $x = 2$.

**Solution:**
```
Step 1: f(2) = 5. Defined ✓

Step 2: lim(x→2) (x²-4)/(x-2) = lim(x→2) (x+2) = 4. Limit exists ✓

Step 3: lim = 4 ≠ 5 = f(2). Condition FAILS ✗

Conclusion: f is DISCONTINUOUS at x = 2.
The discontinuity is REMOVABLE (change f(2) to 4 to fix it).
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

1. 🟢 Test continuity of $f(x) = x^2 + 3x - 1$ at $x = 2$.
<details>
<summary>Solution</summary>

`f(2) = 2^2 + 3(2) - 1 = 4 + 6 - 1 = 9`.
`\lim_{x\to2} (x^2 + 3x - 1) = 4 + 6 - 1 = 9`.
Since limit equals value, the function is **continuous** at `x = 2`.
*(Also, polynomials are continuous everywhere).*
</details>

2. 🟡 $f(x) = \begin{cases} \frac{x^2-9}{x-3} & x \neq 3 \\ 6 & x = 3 \end{cases}$ at $x=3$.
<details>
<summary>Solution</summary>

Limit: `\lim_{x\to3} \frac{x^2-9}{x-3} = \lim_{x\to3} \frac{(x-3)(x+3)}{x-3} = \lim_{x\to3} (x+3) = 6`.
Value: `f(3) = 6`.
Since `6 = 6`, it is **continuous**.
</details>

3. 🟡 ⭐ $f(x) = \begin{cases} \frac{\sin x}{x} & x \neq 0 \\ 0 & x = 0 \end{cases}$ at $x=0$.
<details>
<summary>Solution</summary>

Limit: `\lim_{x\to0} \frac{\sin x}{x} = 1`.
Value: `f(0) = 0`.
Since `1 \neq 0`, it is **discontinuous** (removable type).
</details>

4. 🟡 $f(x) = \begin{cases} x+1 & x \leq 2 \\ 2x-1 & x > 2 \end{cases}$ at $x = 2$.
<details>
<summary>Solution</summary>

LHL: `\lim_{x\to2^-} (x+1) = 2+1 = 3`.
RHL: `\lim_{x\to2^+} (2x-1) = 2(2)-1 = 3`.
Value: `f(2) = 2+1 = 3`.
All match, so it is **continuous**.
</details>

5. 🔴 $f(x) = \begin{cases} e^{1/x} & x \neq 0 \\ 0 & x = 0 \end{cases}$ at $x=0$.
<details>
<summary>Solution</summary>

RHL: As `x \to 0^+`, `1/x \to \infty`, so `e^{1/x} \to \infty`. Limit does not exist.
LHL: As `x \to 0^-`, `1/x \to -\infty`, so `e^{1/x} \to 0`.
Since RHL $\neq$ LHL and RHL goes to infinity, it is **discontinuous** (infinite discontinuity).
</details>

---

### Type 2: Finding the Value of a Constant for Continuity

**Goal:** Given that $f$ is continuous at $x=a$, find the unknown constant $k$.

**Solved Example:** ⭐

Find $k$ if $f(x) = \begin{cases} kx^2 + 1 & x \leq 2 \\ 3x - k & x > 2 \end{cases}$ is continuous at $x = 2$.

**Solution:**
```
For continuity: LHL = RHL = f(2)

LHL = lim(x→2⁻) (kx² + 1) = 4k + 1
RHL = lim(x→2⁺) (3x - k) = 6 - k
f(2) = 4k + 1

For continuity: 4k + 1 = 6 - k
5k = 5
k = 1
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟢 $f(x) = \begin{cases} ax + 5 & x \leq 1 \\ 3x + 2 & x > 1 \end{cases}$ is continuous. Find $a$.
<details>
<summary>Solution</summary>

For continuity at `x = 1`, LHL = RHL.
LHL = `a(1) + 5 = a + 5`.
RHL = `3(1) + 2 = 5`.
`a + 5 = 5 \implies a =` **0**.
</details>

7. 🟡 ⭐ $f(x) = \begin{cases} \frac{1-\cos kx}{x\sin x} & x \neq 0 \\ 1/2 & x=0 \end{cases}$ is continuous at $x=0$. Find $k$.
<details>
<summary>Solution</summary>

Limit: `\lim_{x\to0} \frac{2\sin^2(kx/2)}{x(\sin x)}`.
Multiply and divide by `x` to use standard limits:
`\lim_{x\to0} \frac{2\sin^2(kx/2)}{(kx/2)^2} \cdot \frac{(kx/2)^2}{x^2 (\sin x / x)} = 2(1)^2 \cdot \frac{k^2}{4} = \frac{k^2}{2}`.
Since `f(0) = 1/2`, we set `k^2/2 = 1/2 \implies k^2 = 1`.
So `k =` **\pm 1**.
</details>

8. 🟡 $f(x) = \begin{cases} \frac{x^2-ax+b}{x-2} & x \neq 2 \\ 3 & x=2 \end{cases}$ is continuous at $x=2$. Find $a$ and $b$.
<details>
<summary>Solution</summary>

For the limit to exist at `x=2`, the numerator must be `0` when `x=2` (to cancel the `x-2` factor).
`2^2 - a(2) + b = 0 \implies 4 - 2a + b = 0 \implies b = 2a - 4`.
Substitute `b` back: `\lim_{x\to2} \frac{x^2 - ax + 2a - 4}{x-2} = \lim_{x\to2} \frac{(x-2)(x+2) - a(x-2)}{x-2}`.
Cancel `(x-2)`: `\lim_{x\to2} (x + 2 - a) = 4 - a`.
For continuity, `4 - a = 3 \implies a =` **1**.
Then `b = 2(1) - 4 =` **-2**.
</details>

9. 🔴 $f(x) = \begin{cases} (1+2x)^{1/x} & x \neq 0 \\ k & x=0 \end{cases}$ is continuous. Find $k$.
<details>
<summary>Solution</summary>

This is a `1^\infty` form limit. Use `e^{\lim f(x)g(x)}`.
`\lim_{x\to0} \frac{1}{x} \cdot (1+2x - 1) = \lim_{x\to0} \frac{2x}{x} = 2`.
Limit is `e^2`.
For continuity, `k =` **e^2**.
</details>

10. 🔴 $f(x) = \begin{cases} \frac{\sin(a+1)x + \sin x}{x} & x < 0 \\ c & x = 0 \\ \frac{\sqrt{x+bx^2} - \sqrt{x}}{bx^{3/2}} & x > 0 \end{cases}$ is continuous. Find $a$, $b$, $c$.
<details>
<summary>Solution</summary>

LHL (at x=0): `\lim_{x\to0^-} \left( \frac{\sin((a+1)x)}{x} + \frac{\sin x}{x} \right) = (a+1) + 1 = a+2`.
RHL (at x=0): `\lim_{x\to0^+} \frac{\sqrt{x}(\sqrt{1+bx} - 1)}{bx\sqrt{x}} = \lim_{x\to0^+} \frac{\sqrt{1+bx} - 1}{bx}`.
Rationalize: `\frac{1+bx - 1}{bx(\sqrt{1+bx}+1)} = \frac{1}{\sqrt{1+bx}+1} = \frac{1}{2}`.
For continuity, `LHL = RHL = f(0)`.
`a + 2 = 1/2 = c`.
So **c = 1/2**, **a = -3/2**. The value of **b** can be any non-zero real number.
</details>

---

### Type 3: Continuity of Piecewise Functions with GIF and Modulus

**Goal:** Handle $|x|$, $[x]$, and $\{x\}$ which have natural discontinuities.

**Solved Example:** ⭐

Discuss continuity of $f(x) = x - [x]$ (fractional part function) at $x = 1$.

**Solution:**
```
LHL: As x → 1⁻ (like 0.9, 0.99), [x] = 0. So f(x) = x - 0 = x → 1.
RHL: As x → 1⁺ (like 1.01, 1.1), [x] = 1. So f(x) = x - 1 → 0.

LHL = 1 ≠ RHL = 0.
∴ f is discontinuous at x = 1 (jump discontinuity).
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

11. 🟡 Discuss continuity of $f(x) = [x] + [-x]$ at $x = 2$ and $x = 2.5$.
<details>
<summary>Solution</summary>

At `x=2` (Integer): `f(2) = 2 - 2 = 0`.
LHL (`x \to 2^-`): `[1.99] + [-1.99] = 1 + (-2) = -1`.
RHL (`x \to 2^+`): `[2.01] + [-2.01] = 2 + (-3) = -1`.
Limit is -1, but `f(2) = 0`. **Discontinuous** at `x=2`.

At `x=2.5` (Non-integer): `f(2.5) = 2 + (-3) = -1`.
LHL and RHL nearby are also `[2.4] + [-2.4] = 2 + (-3) = -1`.
**Continuous** at `x=2.5`.
</details>

12. 🟡 Discuss continuity of $f(x) = |x-2|$ at $x = 2$.
<details>
<summary>Solution</summary>

`f(2) = 0`.
LHL (`x \to 2^-`): `|1.99 - 2| = |-0.01| = 0`.
RHL (`x \to 2^+`): `|2.01 - 2| = 0`.
Limit = Value = 0. So it is **continuous**. *(The modulus function is continuous everywhere).*
</details>

13. 🟡 ⭐ $f(x) = \begin{cases} |x| + 1 & x < 0 \\ 0 & x = 0 \\ |x|-1 & x > 0 \end{cases}$ at $x=0$.
<details>
<summary>Solution</summary>

LHL: `\lim_{x\to0^-} (|x| + 1) = 0 + 1 = 1`.
RHL: `\lim_{x\to0^+} (|x| - 1) = 0 - 1 = -1`.
Since LHL $\neq$ RHL, the limit does not exist. **Discontinuous** (Jump discontinuity).
</details>

14. 🔴 Discuss continuity of $f(x) = \frac{x}{1 + e^{1/x}}$ at $x = 0$.
<details>
<summary>Solution</summary>

RHL (`x \to 0^+`): `1/x \to \infty`, `e^{1/x} \to \infty`. So `f(x) \to \frac{0}{\infty} = 0`.
LHL (`x \to 0^-`): `1/x \to -\infty`, `e^{1/x} \to 0`. So `f(x) \to \frac{0}{1+0} = 0`.
Both limits are 0. If `f(0)` is defined as `0`, it is **continuous**. Otherwise, it has a removable discontinuity. *(Usually assumed discontinuous if not explicitly defined).*
</details>

15. 🔴 Discuss continuity of $f(x) = [x^2]$ at $x = \sqrt{2}$.
<details>
<summary>Solution</summary>

`f(\sqrt{2}) = [2] = 2`.
LHL (`x \to \sqrt{2}^-`): `x^2` is slightly less than 2 (e.g., 1.99). So `[x^2] = 1`.
RHL (`x \to \sqrt{2}^+`): `x^2` is slightly greater than 2 (e.g., 2.01). So `[x^2] = 2`.
LHL $\neq$ RHL. **Discontinuous** (Jump discontinuity).
</details>

---

### Type 4: Intermediate Value Theorem Applications

**Goal:** Use IVT to prove existence of roots.

**Solved Example:**

Prove that $x^3 - 4x + 2 = 0$ has a root in $(1, 2)$.

**Solution:**
```
Let f(x) = x³ - 4x + 2.
f is a polynomial, so it is continuous everywhere.

f(1) = 1 - 4 + 2 = -1 < 0
f(2) = 8 - 8 + 2 = 2 > 0

Since f is continuous on [1,2] and f(1) < 0 < f(2),
by IVT, there exists c ∈ (1,2) such that f(c) = 0. ✓
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

16. 🟡 Prove $x^3 + x - 1 = 0$ has a root in $(0, 1)$.
<details>
<summary>Solution</summary>

Let `f(x) = x^3 + x - 1`. `f` is continuous on `[0, 1]`.
`f(0) = 0 + 0 - 1 = -1 < 0`.
`f(1) = 1 + 1 - 1 = 1 > 0`.
Since `f(0) < 0 < f(1)`, by the Intermediate Value Theorem (IVT), there is at least one root `c \in (0, 1)` where `f(c) = 0`.
</details>

17. 🟡 Show $2^x = 3x$ has a root in $(1, 2)$.
<details>
<summary>Solution</summary>

Let `f(x) = 2^x - 3x`. `f` is continuous.
`f(1) = 2 - 3 = -1 < 0`.
`f(2) = 4 - 6 = -2 < 0`.
Wait, the signs didn't change! IVT doesn't guarantee a root in `(1, 2)`.
*(Correction: Let's check `(0, 1)` and `(3, 4)`: `f(0) = 1 > 0`, so there is a root in `(0, 1)`. Also `f(3) = 8-9 = -1 < 0` and `f(4) = 16-12 = 4 > 0`, so there is a root in `(3, 4)`. The interval `(1, 2)` was a trap or typo in the problem!)*
</details>

18. 🔴 Prove that $f(x) = x\sin x + \cos x$ has a root in $(0, \pi)$.
<details>
<summary>Solution</summary>

`f` is continuous.
`f(0) = 0 + 1 = 1 > 0`.
`f(\pi) = \pi\sin\pi + \cos\pi = 0 - 1 = -1 < 0`.
Since `f(\pi) < 0 < f(0)`, by IVT, there is a root in `(0, \pi)`.
</details>

19. 🟡 A continuous function $f$ on $[0,1]$ satisfies $f(0) > 0 > f(1)$. Explain why $f$ must cross the x-axis.
<details>
<summary>Solution</summary>

The x-axis represents the line `y = 0`.
Since `f(1) < 0 < f(0)`, the value `0` is between `f(1)` and `f(0)`.
By IVT, since `f` is continuous, it must attain every value between `f(1)` and `f(0)`, including `0`. Thus, it must cross the x-axis.
</details>

20. 🔴 If $f:[a,b]\to[a,b]$ is continuous, prove there exists a fixed point $c \in [a,b]$ with $f(c) = c$. *[Hint: Apply IVT to $g(x) = f(x) - x$]*
<details>
<summary>Solution</summary>

Let `g(x) = f(x) - x`. `g` is continuous.
At `x = a`: `g(a) = f(a) - a`. Since `f(x)` is in `[a, b]`, `f(a) \geq a`, so `g(a) \geq 0`.
At `x = b`: `g(b) = f(b) - b`. Since `f(x)` is in `[a, b]`, `f(b) \leq b`, so `g(b) \leq 0`.
If `g(a) = 0` or `g(b) = 0`, we found the fixed point.
If `g(b) < 0 < g(a)`, by IVT, there exists `c \in (a, b)` where `g(c) = 0`.
Thus, `f(c) - c = 0 \implies f(c) = c`.
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ $f(x) = \begin{cases} \frac{1-\cos 4x}{8x^2} & x < 0 \\ k & x = 0 \\ \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}}-4} & x > 0 \end{cases}$. Find $k$ for continuity.
<details>
<summary>Solution</summary>

LHL (at x=0): `\lim_{x\to0^-} \frac{2\sin^2(2x)}{8x^2} = \lim_{x\to0^-} \frac{2(2x)^2}{8x^2} = \frac{8x^2}{8x^2} = 1`.
RHL (at x=0): `\lim_{x\to0^+} \frac{\sqrt{x}}{\sqrt{16+\sqrt{x}} - 4}`. Rationalize: `\frac{\sqrt{x}(\sqrt{16+\sqrt{x}} + 4)}{16+\sqrt{x} - 16} = \frac{\sqrt{x}(\sqrt{16+\sqrt{x}} + 4)}{\sqrt{x}} = \sqrt{16+0} + 4 = 8`.
Since LHL = 1 and RHL = 8, the limit does not exist.
**Conclusion:** It is impossible to make `f(x)` continuous for any value of `k`.
</details>

2. 🔴 A function $f$ is continuous on $[0,2]$ with $f(0) = 1$, $f(2) = 3$. Can we conclude $f(c) = 2$ for some $c \in (0,2)$? Justify.
<details>
<summary>Solution</summary>

**Yes.** Since `f` is continuous on `[0, 2]`, and `2` is a number strictly between `f(0) = 1` and `f(2) = 3`, the Intermediate Value Theorem guarantees that there is at least one `c \in (0, 2)` such that `f(c) = 2`.
</details>

3. 🟡 If $f(x) = |x-2| + |x-3|$, discuss continuity at $x=2$ and $x=3$.
<details>
<summary>Solution</summary>

The modulus function `|x-a|` is continuous everywhere. The sum of two continuous functions is also continuous.
Therefore, `f(x)` is **continuous at both x=2 and x=3** (and everywhere else).
</details>

4. 🔴 $f(x) = \begin{cases} \frac{e^{1/x}-1}{e^{1/x}+1} & x \neq 0 \\ 0 & x = 0 \end{cases}$. Discuss continuity at $x=0$.
<details>
<summary>Solution</summary>

RHL (`x \to 0^+`): `1/x \to \infty`, `e^{1/x} \to \infty`. `\lim_{x\to0^+} \frac{1 - e^{-1/x}}{1 + e^{-1/x}} = \frac{1-0}{1+0} = 1`.
LHL (`x \to 0^-`): `1/x \to -\infty`, `e^{1/x} \to 0`. `\lim_{x\to0^-} \frac{0 - 1}{0 + 1} = -1`.
Since LHL $\neq$ RHL, the limit does not exist. **Discontinuous** (Jump discontinuity).
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Define continuity of a function $f(x)$ at a point $x=a$. **(2 marks)**

**Solution:**
A function $f(x)$ is continuous at $x=a$ if:
1. $f(a)$ is defined.
2. $\lim_{x\to a} f(x)$ exists.
3. $\lim_{x\to a} f(x) = f(a)$.

---

**Q2.** 🟡 Find all points of discontinuity of $f(x) = \frac{x^2 - 1}{x - 1}$, $x \neq 1$; $f(1) = 2$. **(3 marks)**

**Solution:**
At $x = 1$: $\lim_{x\to 1} \frac{x^2-1}{x-1} = \lim_{x\to1}(x+1) = 2 = f(1)$.
So $f$ is continuous at $x=1$.
For $x \neq 1$: $f(x) = x+1$ is a polynomial, continuous everywhere.
∴ $f$ is continuous on all of $\mathbb{R}$. No discontinuities.

---

**Q3.** 🟡 ⭐ Find $k$ so that $f(x) = \begin{cases} kx+1 & x \leq 5 \\ 3x-5 & x>5 \end{cases}$ is continuous at $x=5$. **(3 marks)**

**Solution:**
For continuity: $\lim_{x\to5^-} f(x) = \lim_{x\to5^+} f(x) = f(5)$
$f(5) = 5k + 1$
$\lim_{x\to5^+} = 15 - 5 = 10$
$5k + 1 = 10 \Rightarrow k = 9/5$

---

## Stage 6: JEE Mains Arena

**Q1.** The function $f(x) = \begin{cases} \frac{(4^x-1)^3}{\sin(x/4)\ln(1+x^2/3)} & x\neq 0 \\ k & x=0 \end{cases}$ is continuous at $x=0$. Then $k$ equals:
<br>(a) $4(\ln 4)^3$   <br>(b) $3(\ln 4)^3$   <br>(c) $12(\ln 4)^3$   <br>(d) $9(\ln 4)^3$

<details>
<summary>Solution</summary>
k = lim(x→0) (4^x-1)³ / [sin(x/4) · ln(1+x²/3)]

Multiply and divide:
= lim [(4^x-1)/x]³ · x³ / [sin(x/4)/(x/4) · (x/4) · ln(1+x²/3)/(x²/3) · (x²/3)]

As x→0:
[(4^x-1)/x] → ln 4 → (ln 4)³ for the cube
sin(x/4)/(x/4) → 1
ln(1+x²/3)/(x²/3) → 1

So = (ln 4)³ · x³ / [(x/4) · (x²/3)]
= (ln 4)³ · x³ / [x³/12]
= 12(ln 4)³

Answer: (c) 🔴 ⭐
</details>

---

**Q2.** $f(x) = \begin{cases} \frac{e^{1/x} - 1}{e^{1/x} + 1} & x \neq 0 \\ 0 & x = 0 \end{cases}$. At $x=0$, $f$ is:
<br>(a) Continuous   <br>(b) Has removable discontinuity   <br>(c) Has jump discontinuity   <br>(d) Has infinite discontinuity

<details>
<summary>Solution</summary>
As x → 0⁺: 1/x → +∞, e^{1/x} → ∞, so (e^{1/x}-1)/(e^{1/x}+1) → (∞-1)/(∞+1) = 1. RHL = 1.
As x → 0⁻: 1/x → -∞, e^{1/x} → 0, so (0-1)/(0+1) = -1. LHL = -1.
LHL ≠ RHL ⟹ Jump discontinuity.
Answer: (c) 🔴 ⭐
</details>

---

**Q3.** The number of points at which $f(x) = [x] + \sqrt{x - [x]}$ is discontinuous is:
<br>(a) $0$   <br>(b) Infinitely many   <br>(c) 1   <br>(d) 2

<details>
<summary>Solution</summary>
[x] is discontinuous at all integers. √(x-[x]) = √{x} (fractional part), which equals 0 at integers but the square root is continuous.
Combined function: at integers, [x] jumps but √{x} = 0 makes RHL easier.
At integer n: LHL of [x] = n-1, LHL of √{x-[x]} = √1 = 1. So LHL = n.
RHL: [x]=n, {x}=0, so RHL = n+0 = n. f(n)=n.
Actually LHL = (n-1) + 1 = n. RHL = n. So continuous at integers!
f is continuous everywhere. Answer: (a) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** Every differentiable function is continuous.
<br>**Reason (R):** If $\lim_{h\to0} \frac{f(a+h)-f(a)}{h}$ exists, then $\lim_{h\to0} f(a+h) = f(a)$.

<details>
<summary>Solution</summary>
A is true: Differentiability ⟹ Continuity (proven in Chapter 8).
R is true and gives the exact proof: if the derivative limit exists, then f(a+h) - f(a) = h · [f'(a) + ε] → 0, so f is continuous.
Answer: (a) 🟡 ⭐
</details>

---

**Q2.**
<br>**Assertion (A):** Every continuous function is differentiable.
<br>**Reason (R):** $f(x) = |x|$ is continuous everywhere but not differentiable at $x=0$.

<details>
<summary>Solution</summary>
A is false: Continuity does NOT imply differentiability.
R is true and provides a counterexample proving A is false.
Answer: (d) 🟢 ⭐
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 $f(x) = \frac{x^2-4}{x-2}$ for $x \neq 2$, $f(2) = 4$. At $x=2$, $f$ is:
   <br>(a) Continuous   <br>(b) Discontinuous (removable)   <br>(c) Discontinuous (jump)   <br>(d) Not defined

2. 🟡 $f(x) = [x]$ (greatest integer function) is discontinuous at:
   <br>(a) All real numbers   <br>(b) All integers   <br>(c) No points   <br>(d) Rational numbers only

3. 🟡 ⭐ For $f(x) = \begin{cases} x^2 & x \leq 1 \\ 2-x & x > 1 \end{cases}$, $f$ is:
   <br>(a) Continuous at $x=1$   <br>(b) Discontinuous (jump)   <br>(c) Discontinuous (removable)   <br>(d) Discontinuous (infinite)

4. 🟡 If $f(x)$ is continuous at $x=a$ then necessarily:
   <br>(a) $f'(a)$ exists   <br>(b) $f(a)$ is defined   <br>(c) $f$ is differentiable   <br>(d) $f(a) = 0$

5. 🟡 $f(x) = \sin(1/x)$ at $x=0$:
   <br>(a) Is continuous   <br>(b) Has a jump discontinuity   <br>(c) Has a removable discontinuity   <br>(d) Has oscillatory discontinuity

6. 🔴 ⭐ $f(x) = \begin{cases} \frac{\sin 2x}{x} & x < 0 \\ a & x = 0 \\ \frac{x+b}{x^2+b} & x > 0 \end{cases}$ is continuous at $x=0$. Then $2a+3b =$:
   <br>(a) $0$   <br>(b) $2$   <br>(c) $4$   <br>(d) $-4$

7. 🟢 A polynomial function is continuous on:
   <br>(a) $(0, \infty)$   <br>(b) $(-\infty, 0)$   <br>(c) All real numbers   <br>(d) Rational numbers only

8. 🟡 $f(x) = \frac{1}{1 + e^{1/x}}$, $x\neq 0$, $f(0)=0$ at $x=0$:
   <br>(a) Continuous   <br>(b) Jump discontinuity   <br>(c) Infinite discontinuity   <br>(d) Removable discontinuity

9. 🟡 By IVT, the equation $x^5 + x + 1 = 0$ has a real root in:
   <br>(a) $(0, 1)$   <br>(b) $(-1, 0)$   <br>(c) $(1, 2)$   <br>(d) $(-2, -1)$

10. 🔴 The function $f(x) = \begin{cases} \frac{|x|}{x} & x \neq 0 \\ 0 & x=0 \end{cases}$ is:
    <br>(a) Continuous everywhere   <br>(b) Continuous only at $x=0$   <br>(c) Discontinuous at $x=0$   <br>(d) Continuous for $x>0$ only

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | a | 6 | c |
| 2 | b | 7 | c |
| 3 | a | 8 | b |
| 4 | b | 9 | b |
| 5 | d | 10 | c |

</details>

---

## What's Next?

Continuity asks: does the function flow through a point? Differentiability asks a harder question: does the function have a well-defined *slope* at that point? A function can be continuous without having a slope (think of a corner). In **Chapter 8**, we'll explore the precise relationship between continuity and differentiability.
