# Chapter 11: Derivatives of Special Functions (Inverse Trig, Absolute Value, Piecewise)

---

## Stage 1: The Core Idea

### The Inverses That Changed Everything

The function $\sin x$ takes an angle and gives a ratio. $\sin^{-1}x$ (or $\arcsin x$) takes a ratio and gives back the angle. These inverse functions have derivatives that look nothing like the trigonometric derivatives — they involve square roots and rational expressions.

Why do we care? Because functions like $\sin^{-1}x$, $\tan^{-1}x$ appear constantly in integration (which is the reverse of differentiation), in physics, in engineering, and in 3–4 questions per JEE Mains paper.

### The Absolute Value Trap

$|f(x)|$ is a function that flips negative values positive. But this flip creates a **corner** whenever $f(x) = 0$. Differentiating $|f(x)|$ requires careful casework — and it is a classic JEE trap.

---

## Stage 2: The Formula Lab

### Inverse Trigonometric Derivatives

| $f(x)$ | $f'(x)$ | Domain | Trap |
|--------|---------|--------|------|
| $\sin^{-1}x$ | $\frac{1}{\sqrt{1-x^2}}$ | $(-1,1)$ | Positive sign only |
| $\cos^{-1}x$ | $\frac{-1}{\sqrt{1-x^2}}$ | $(-1,1)$ | Negative sign — common error |
| $\tan^{-1}x$ | $\frac{1}{1+x^2}$ | $\mathbb{R}$ | No square root |
| $\cot^{-1}x$ | $\frac{-1}{1+x^2}$ | $\mathbb{R}$ | Negative sign |
| $\sec^{-1}x$ | $\frac{1}{|x|\sqrt{x^2-1}}$ | $|x|>1$ | Absolute value in denominator |
| $\csc^{-1}x$ | $\frac{-1}{|x|\sqrt{x^2-1}}$ | $|x|>1$ | Negative sign + $|x|$ |

### Key Observation

$\frac{d}{dx}(\sin^{-1}x) + \frac{d}{dx}(\cos^{-1}x) = 0$

This makes sense because $\sin^{-1}x + \cos^{-1}x = \pi/2$ (constant), so their derivatives sum to zero!

Similarly: $\tan^{-1}x + \cot^{-1}x = \pi/2$.

### Derivative of $|f(x)|$

$$\frac{d}{dx}|f(x)| = \frac{f(x)}{|f(x)|} \cdot f'(x) = \text{sgn}(f(x)) \cdot f'(x), \quad f(x) \neq 0$$

Where $\text{sgn}(f(x)) = +1$ if $f(x) > 0$ and $-1$ if $f(x) < 0$.

**Shortcut:** Write $|f(x)|$ as $f(x)$ when $f(x) > 0$ and $-f(x)$ when $f(x) < 0$, then differentiate each piece.

---

## Stage 3: Type-wise Mastery

### Type 1: Basic Inverse Trig Derivatives (with Chain Rule)

**Goal:** Apply the standard formula + chain rule for any inner function.

**Solved Example:** ⭐

Differentiate $y = \sin^{-1}(2x)$.

**Solution:**
```
Outer: sin⁻¹(·) → 1/√(1-(·)²)
Inner: 2x → 2

y' = 1/√(1-(2x)²) · 2 = 2/√(1-4x²)
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

1. 🟢 $y = \cos^{-1}(3x)$
<details>
<summary>Solution</summary>

`y' = \frac{-1}{\sqrt{1 - (3x)^2}} \cdot \frac{d}{dx}(3x) =` **\frac{-3}{\sqrt{1 - 9x^2}}**.
</details>

2. 🟡 $y = \tan^{-1}(x^2)$
<details>
<summary>Solution</summary>

`y' = \frac{1}{1 + (x^2)^2} \cdot \frac{d}{dx}(x^2) =` **\frac{2x}{1 + x^4}**.
</details>

3. 🟡 $y = \sin^{-1}(1 - 2x^2)$ — *You may simplify: this is related to $\cos^{-1}$.*
<details>
<summary>Solution</summary>

Method 1 (Chain Rule): `y' = \frac{1}{\sqrt{1 - (1-2x^2)^2}} \cdot (-4x) = \frac{-4x}{\sqrt{1 - (1 - 4x^2 + 4x^4)}} = \frac{-4x}{\sqrt{4x^2 - 4x^4}} = \frac{-4x}{2|x|\sqrt{1-x^2}}`.
Method 2 (Substitution): Let `x = \sin\theta`. `1 - 2\sin^2\theta = \cos 2\theta = \sin(\pi/2 - 2\theta)`.
So `y = \pi/2 - 2\theta = \pi/2 - 2\sin^{-1}x` (assuming principal values).
Then `y' =` **\frac{-2}{\sqrt{1-x^2}}** (for `x \in (0, 1)`).
</details>

4. 🟡 $y = \sec^{-1}(e^x)$
<details>
<summary>Solution</summary>

Since `e^x > 0`, `|e^x| = e^x`.
`y' = \frac{1}{e^x \sqrt{(e^x)^2 - 1}} \cdot \frac{d}{dx}(e^x) = \frac{e^x}{e^x \sqrt{e^{2x} - 1}} =` **\frac{1}{\sqrt{e^{2x} - 1}}**.
</details>

5. 🔴 $y = \tan^{-1}\left(\sqrt{\frac{1-x}{1+x}}\right)$ — *Hint: Substitute $x = \cos\theta$.*
<details>
<summary>Solution</summary>

Let `x = \cos\theta \implies \theta = \cos^{-1}x`.
`\frac{1-x}{1+x} = \frac{1-\cos\theta}{1+\cos\theta} = \frac{2\sin^2(\theta/2)}{2\cos^2(\theta/2)} = \tan^2(\theta/2)`.
So `y = \tan^{-1}(\sqrt{\tan^2(\theta/2)}) = \tan^{-1}(\tan(\theta/2)) = \frac{\theta}{2} = \frac{1}{2}\cos^{-1}x`.
`y' = \frac{1}{2} \left( \frac{-1}{\sqrt{1-x^2}} \right) =` **-\frac{1}{2\sqrt{1-x^2}}**.
</details>

---

### Type 2: Substitution Simplification

**Goal:** Use trig substitutions to convert inverse trig expressions into simpler ones before differentiating.

**Key Substitutions:**

| Expression | Substitution | Simplification |
|-----------|-------------|----------------|
| $\sin^{-1}\left(\frac{2x}{1+x^2}\right)$ | $x = \tan\theta$ | $= 2\tan^{-1}x$ |
| $\cos^{-1}\left(\frac{1-x^2}{1+x^2}\right)$ | $x = \tan\theta$ | $= 2\tan^{-1}x$ |
| $\tan^{-1}\left(\frac{2x}{1-x^2}\right)$ | $x = \tan\theta$ | $= 2\tan^{-1}x$ |
| $\sin^{-1}(2x\sqrt{1-x^2})$ | $x = \sin\theta$ | $= 2\sin^{-1}x$ |
| $\tan^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$ | $x = \tan\theta$ | $= \frac{1}{2}\tan^{-1}x$ |

**Solved Example:** ⭐

Differentiate $y = \tan^{-1}\left(\frac{2x}{1-x^2}\right)$.

**Solution:**
```
Recognize: tan(2θ) = 2tanθ/(1-tan²θ)
If x = tan θ, then y = tan⁻¹(tan 2θ) = 2θ = 2tan⁻¹x.

dy/dx = 2 · 1/(1+x²) = 2/(1+x²)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟡 $y = \sin^{-1}\left(\frac{2x}{1+x^2}\right)$
<details>
<summary>Solution</summary>

Let `x = \tan\theta`. The expression becomes `\frac{2\tan\theta}{1+\tan^2\theta} = \sin 2\theta`.
So `y = \sin^{-1}(\sin 2\theta) = 2\theta = 2\tan^{-1}x` (for `|x| \leq 1`).
`y' =` **\frac{2}{1+x^2}**.
</details>

7. 🟡 $y = \cos^{-1}\left(\frac{1-x^2}{1+x^2}\right)$
<details>
<summary>Solution</summary>

Let `x = \tan\theta`. The expression becomes `\frac{1-\tan^2\theta}{1+\tan^2\theta} = \cos 2\theta`.
So `y = \cos^{-1}(\cos 2\theta) = 2\theta = 2\tan^{-1}x` (for `x \geq 0`).
`y' =` **\frac{2}{1+x^2}**.
</details>

8. 🟡 $y = \sin^{-1}(2x\sqrt{1-x^2})$
<details>
<summary>Solution</summary>

Let `x = \sin\theta`. The expression becomes `2\sin\theta\sqrt{1-\sin^2\theta} = 2\sin\theta\cos\theta = \sin 2\theta`.
So `y = \sin^{-1}(\sin 2\theta) = 2\theta = 2\sin^{-1}x` (for `|x| \leq 1/\sqrt{2}`).
`y' =` **\frac{2}{\sqrt{1-x^2}}**.
</details>

9. 🔴 $y = \tan^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$
<details>
<summary>Solution</summary>

Let `x = \tan\theta`. Then `\sqrt{1+\tan^2\theta} = \sec\theta`.
Inside: `\frac{\sec\theta - 1}{\tan\theta} = \frac{1/\cos\theta - 1}{\sin\theta/\cos\theta} = \frac{1-\cos\theta}{\sin\theta} = \frac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)} = \tan(\theta/2)`.
So `y = \tan^{-1}(\tan(\theta/2)) = \theta/2 = \frac{1}{2}\tan^{-1}x`.
`y' =` **\frac{1}{2(1+x^2)}**.
</details>

10. 🔴 $y = \tan^{-1}\left(\frac{\cos x}{1+\sin x}\right)$
<details>
<summary>Solution</summary>

Use half-angle formulas: `\cos x = \cos^2(x/2) - \sin^2(x/2)` and `1 + \sin x = (\cos(x/2) + \sin(x/2))^2`.
Ratio: `\frac{(\cos(x/2)-\sin(x/2))(\cos(x/2)+\sin(x/2))}{(\cos(x/2)+\sin(x/2))^2} = \frac{\cos(x/2)-\sin(x/2)}{\cos(x/2)+\sin(x/2)}`.
Divide numerator and denominator by `\cos(x/2)`:
`= \frac{1-\tan(x/2)}{1+\tan(x/2)} = \tan(\pi/4 - x/2)`.
So `y = \tan^{-1}(\tan(\pi/4 - x/2)) = \pi/4 - x/2`.
`y' =` **-1/2**.
</details>

---

### Type 3: Sum of Inverse Trig Functions

**Goal:** Exploit $\sin^{-1}x + \cos^{-1}x = \pi/2$ and similar identities.

**Solved Example:** ⭐

Differentiate $y = \sin^{-1}x + \cos^{-1}x$.

**Solution:**
```
y = π/2 (constant!)
dy/dx = 0
```
🟢 Easy ⭐ Must-Do (Classic trap question)

**Practice Problems:**

11. 🟢 $y = \tan^{-1}x + \cot^{-1}x$
<details>
<summary>Solution</summary>

Identity: `\tan^{-1}x + \cot^{-1}x = \pi/2` for all `x`.
Since `y = \pi/2` (a constant), `y' =` **0**.
</details>

12. 🟡 ⭐ $y = \tan^{-1}\left(\frac{1+x}{1-x}\right) - \tan^{-1}x$ — *Simplify using $\tan^{-1}a - \tan^{-1}b$ formula.*
<details>
<summary>Solution</summary>

Rewrite the first term: `\tan^{-1}\left(\frac{1+x}{1-1\cdot x}\right) = \tan^{-1}1 + \tan^{-1}x = \pi/4 + \tan^{-1}x`.
So `y = (\pi/4 + \tan^{-1}x) - \tan^{-1}x = \pi/4`.
Since `y` is a constant, `y' =` **0**.
</details>

13. 🟡 $y = \sin^{-1}x + \sin^{-1}\sqrt{1-x^2}$
<details>
<summary>Solution</summary>

Let `x = \sin\theta` (assume `x \in (0,1)` so `\theta \in (0, \pi/2)`). Then `\sqrt{1-x^2} = \cos\theta`.
`y = \sin^{-1}(\sin\theta) + \sin^{-1}(\cos\theta) = \theta + \sin^{-1}(\sin(\pi/2-\theta)) = \theta + \pi/2 - \theta = \pi/2`.
Since `y = \pi/2`, `y' =` **0**.
*(Note: for `x \in (-1, 0)`, `y = 2\sin^{-1}x + \pi/2 \implies y' = \frac{2}{\sqrt{1-x^2}}`)*.
</details>

14. 🔴 $y = \tan^{-1}\left(\frac{a-x}{1+ax}\right)$ where $a$ is constant.
<details>
<summary>Solution</summary>

Use the inverse tangent difference formula: `\tan^{-1}\left(\frac{a-x}{1+ax}\right) = \tan^{-1}a - \tan^{-1}x`.
Differentiate: `y' = 0 - \frac{1}{1+x^2} =` **-\frac{1}{1+x^2}**.
</details>

15. 🔴 ⭐ $y = \tan^{-1}\left(\frac{1}{1+x+x^2}\right)$ — *Write as $\tan^{-1}(x+1) - \tan^{-1}(x)$.*
<details>
<summary>Solution</summary>

Rewrite the denominator to match `1 + ab` format: `1 + x(x+1)`.
Rewrite the numerator to match `b - a`: `(x+1) - x`.
So `y = \tan^{-1}\left(\frac{(x+1) - x}{1 + (x+1)x}\right) = \tan^{-1}(x+1) - \tan^{-1}x`.
Differentiate: `y' =` **\frac{1}{1+(x+1)^2} - \frac{1}{1+x^2}**.
</details>

---

### Type 4: Differentiating $|f(x)|$

**Goal:** Write $|f(x)|$ as a piecewise function, differentiate each branch.

**Solved Example:** ⭐

Differentiate $y = |x^2 - 4|$.

**Solution:**
```
x² - 4 = 0 when x = ±2.

For |x| > 2: y = x² - 4, so y' = 2x.
For |x| < 2: y = -(x² - 4) = 4 - x², so y' = -2x.

At x = ±2: y is not differentiable (corner).

dy/dx = { 2x,  if |x| > 2
         { -2x, if |x| < 2
         { DNE, if x = ±2
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

16. 🟡 $y = |x^2 - 3x + 2|$
<details>
<summary>Solution</summary>

Factor: `x^2 - 3x + 2 = (x-1)(x-2)`. Roots at `x=1` and `x=2`.
For `x \in (1, 2)`: The quadratic is negative, so `y = -(x^2-3x+2) = -x^2+3x-2 \implies y' = -2x+3`.
For `x < 1` or `x > 2`: The quadratic is positive, so `y = x^2-3x+2 \implies y' = 2x-3`.
At `x=1` and `x=2`: `y'` does not exist.
Answer: **y' = 2x-3 for x \in (-\infty, 1) \cup (2, \infty); y' = 3-2x for x \in (1, 2)**.
</details>

17. 🟡 ⭐ $y = |x-1| + |x-2|$, differentiate for all $x$.
<details>
<summary>Solution</summary>

Break into intervals around roots `x=1` and `x=2`:
For `x < 1`: `y = -(x-1) - (x-2) = -2x+3 \implies y' = -2`.
For `1 < x < 2`: `y = (x-1) - (x-2) = 1 \implies y' = 0`.
For `x > 2`: `y = (x-1) + (x-2) = 2x-3 \implies y' = 2`.
At `x=1, 2`, the derivative does not exist.
Answer: **y' = -2 (x<1), 0 (1<x<2), 2 (x>2)**.
</details>

18. 🔴 $y = |\sin x|$, find $y'$ and state where it fails.
<details>
<summary>Solution</summary>

Using the absolute value chain rule: `\frac{d}{dx}|f(x)| = \text{sgn}(f(x)) \cdot f'(x)`.
`y' = \text{sgn}(\sin x) \cdot \cos x = \frac{\sin x}{|\sin x|} \cos x =` **\cot x |\sin x|** (or `\text{sgn}(\sin x)\cos x`).
It fails (is not differentiable) where `\sin x = 0`, which is at **x = n\pi** (for any integer `n`).
</details>

19. 🔴 $y = \ln|x|$
<details>
<summary>Solution</summary>

For `x > 0`: `y = \ln x \implies y' = 1/x`.
For `x < 0`: `y = \ln(-x) \implies y' = \frac{1}{-x} \cdot (-1) = 1/x`.
The derivative is the same in both branches!
**y' = 1/x** (for all `x \neq 0`).
</details>

20. 🔴 ⭐ $y = x|x|$. Find $y'$ everywhere (including $x=0$).
<details>
<summary>Solution</summary>

Rewrite: `y = x^2` for `x \geq 0`, and `y = -x^2` for `x < 0`.
For `x > 0`: `y' = 2x`.
For `x < 0`: `y' = -2x`.
At `x = 0`: `\lim_{h\to0} \frac{h|h| - 0}{h} = \lim_{h\to0} |h| = 0`. So `y'(0) = 0`.
Notice that `2x` for positive and `-2x` for negative can be combined into a single expression.
**y' = 2|x|** (for all `x`).
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ Differentiate $y = \sin^{-1}\left(\frac{2\tan x}{1+\tan^2 x}\right)$.
<details>
<summary>Solution</summary>

Identity: `\frac{2\tan x}{1+\tan^2 x} = \sin 2x`.
So `y = \sin^{-1}(\sin 2x) = 2x` (assuming `2x \in [-\pi/2, \pi/2]`).
`y' =` **2**.
</details>

2. 🔴 Differentiate $y = \tan^{-1}\left(\frac{\sin x - \cos x}{\sin x + \cos x}\right)$. Simplify first.
<details>
<summary>Solution</summary>

Divide numerator and denominator by `\cos x`:
`y = \tan^{-1}\left(\frac{\tan x - 1}{\tan x + 1}\right) = \tan^{-1}\left(\frac{\tan x - \tan(\pi/4)}{1 + \tan x\tan(\pi/4)}\right)`.
`y = \tan^{-1}(\tan(x - \pi/4)) = x - \pi/4`.
`y' =` **1**.
</details>

3. 🔴 If $y = \cos^{-1}\left(\frac{x^2-1}{x^2+1}\right)$, find $y'$ and state domain.
<details>
<summary>Solution</summary>

Rewrite: `\frac{x^2-1}{x^2+1} = -\left(\frac{1-x^2}{1+x^2}\right)`.
Use `\cos^{-1}(-z) = \pi - \cos^{-1}(z)`:
`y = \pi - \cos^{-1}\left(\frac{1-x^2}{1+x^2}\right)`.
Let `x = \tan\theta`. The inner part becomes `\cos 2\theta`.
`y = \pi - 2\tan^{-1}|x|`.
For `x > 0`: `y = \pi - 2\tan^{-1}x \implies y' =` **\frac{-2}{1+x^2}**.
For `x < 0`: `y = \pi + 2\tan^{-1}x \implies y' =` **\frac{2}{1+x^2}**.
Domain is all `x \in \mathbb{R}`. Not differentiable at `x=0`.
</details>

4. 🟡 Differentiate $y = |\tan^{-1}x|$. Is it differentiable everywhere?
<details>
<summary>Solution</summary>

For `x > 0`: `\tan^{-1}x > 0`, so `y = \tan^{-1}x \implies y' = \frac{1}{1+x^2}`.
For `x < 0`: `\tan^{-1}x < 0`, so `y = -\tan^{-1}x \implies y' = \frac{-1}{1+x^2}`.
At `x = 0`: LHD = -1, RHD = 1.
**No, it is not differentiable at x=0**.
</details>

5. 🔴 ⭐ Prove $\frac{d}{dx}\left[\tan^{-1}\left(\frac{a+x}{1-ax}\right)\right] = \frac{1}{1+x^2}$ (for $ax < 1$).
<details>
<summary>Solution</summary>

Using the inverse tangent addition formula (since `ax < 1`):
`\tan^{-1}\left(\frac{a+x}{1-ax}\right) = \tan^{-1}a + \tan^{-1}x`.
Since `\tan^{-1}a` is a constant, its derivative is 0.
Derivative = `0 + \frac{1}{1+x^2} =` **\frac{1}{1+x^2}**. (Proved).
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Differentiate $y = \tan^{-1}\left(\frac{1+x}{1-x}\right)$. **(3 marks)**

**Solution:**
$y = \tan^{-1}(1) + \tan^{-1}(x) = \pi/4 + \tan^{-1}x$ (using addition formula)
Wait: $\tan^{-1}\frac{a+b}{1-ab} = \tan^{-1}a + \tan^{-1}b$ if $ab < 1$.
Here $\frac{1+x}{1-x} = \frac{1+x}{1-1\cdot x}$, so $y = \tan^{-1}1 + \tan^{-1}x = \pi/4 + \tan^{-1}x$.
$y' = \frac{1}{1+x^2}$.

---

**Q2.** 🔴 If $y = \tan^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$, show $y' = \frac{1}{2(1+x^2)}$. **(4 marks)**

**Solution:**
Let $x = \tan\theta$. Then $\sqrt{1+\tan^2\theta} = \sec\theta$.
$y = \tan^{-1}\left(\frac{\sec\theta - 1}{\tan\theta}\right) = \tan^{-1}\left(\frac{1-\cos\theta}{\sin\theta}\right) = \tan^{-1}\left(\tan\frac{\theta}{2}\right) = \theta/2 = \frac{1}{2}\tan^{-1}x$
$y' = \frac{1}{2(1+x^2)}$ ✓

---

## Stage 6: JEE Mains Arena

**Q1.** If $y = \sin^{-1}\left(\frac{x}{\sqrt{1+x^2}}\right)$, then $\frac{dy}{dx} =$:
<br>(a) $\frac{1}{1+x^2}$   <br>(b) $\frac{1}{\sqrt{1+x^2}}$   <br>(c) $\frac{x}{(1+x^2)^{3/2}}$   <br>(d) $\frac{1}{\sqrt{1+x^2}(1+x^2)}$

<details>
<summary>Solution</summary>
Let x = tan θ. Then x/√(1+x²) = tan θ/sec θ = sin θ.
y = sin⁻¹(sin θ) = θ = tan⁻¹ x.
dy/dx = 1/(1+x²).
Answer: (a) 🟡 ⭐
</details>

---

**Q2.** The number of points where $f(x) = |\cos x|$ is not differentiable in $[0, 2\pi]$:
<br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $3$

<details>
<summary>Solution</summary>
|cos x| is not differentiable where cos x = 0, i.e., x = π/2 and x = 3π/2 in [0, 2π].
Count: 2 points.
Answer: (c) 🟡
</details>

---

**Q3.** $\frac{d}{dx}\left[\tan^{-1}\left(\frac{a\cos x - b\sin x}{b\cos x + a\sin x}\right)\right] =$:
<br>(a) $-1$   <br>(b) $1$   <br>(c) $a/b$   <br>(d) $-b/a$

<details>
<summary>Solution</summary>
Divide numerator and denominator by b cos x:
= tan⁻¹[(a/b - tan x)/(1 + (a/b)tan x)]
= tan⁻¹(a/b) - tan⁻¹(tan x)
= tan⁻¹(a/b) - x (constant - x)

Derivative = -1.
Answer: (a) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** $\frac{d}{dx}[\sin^{-1}x + \cos^{-1}x] = 0$ for all $x \in (-1,1)$.
<br>**Reason (R):** $\sin^{-1}x + \cos^{-1}x = \pi/2$, a constant.

<details>
<summary>Solution</summary>
A is true: derivative of a constant is 0.
R is true and is the correct explanation — the sum is always π/2, so the derivative is 0.
Answer: (a) 🟢 ⭐
</details>

---

**Q2.**
<br>**Assertion (A):** $\frac{d}{dx}(\cos^{-1}x) = \frac{1}{\sqrt{1-x^2}}$.
<br>**Reason (R):** $\cos^{-1}x = \pi/2 - \sin^{-1}x$, and $\frac{d}{dx}(\sin^{-1}x) = \frac{1}{\sqrt{1-x^2}}$.

<details>
<summary>Solution</summary>
A is false: The correct derivative is -1/√(1-x²), not +1/√(1-x²).
R is true: The relationship is correct, and differentiating: d/dx(π/2 - sin⁻¹x) = -1/√(1-x²).
Answer: (d) 🟡 ⭐
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 $\frac{d}{dx}[\sin^{-1}(1-2x^2)] =$
   <br>(a) $\frac{-4x}{\sqrt{1-x^2}}$ for $0<x<1$   <br>(b) $\frac{4x}{\sqrt{1-x^2}}$   <br>(c) $\frac{2}{\sqrt{1-x^2}}$   <br>(d) $\frac{-2}{\sqrt{1-x^2}}$

2. 🟡 $\frac{d}{dx}[\tan^{-1}(x^2)] =$
   <br>(a) $\frac{1}{1+x^4}$   <br>(b) $\frac{2x}{1+x^4}$   <br>(c) $\frac{1}{1+x^2}$   <br>(d) $\frac{x^2}{1+x^4}$

3. 🟡 ⭐ $\frac{d}{dx}\left[\tan^{-1}\left(\frac{2x}{1-x^2}\right)\right]$ for $|x|<1$:
   <br>(a) $\frac{1}{1+x^2}$   <br>(b) $\frac{2}{1+x^2}$   <br>(c) $\frac{1}{(1+x^2)^2}$   <br>(d) $\frac{4}{1+x^2}$

4. 🟡 $\frac{d}{dx}|\sin x|$ at $x = \pi$ is:
   <br>(a) $1$   <br>(b) $-1$   <br>(c) $0$   <br>(d) DNE

5. 🔴 ⭐ $\frac{d}{dx}\left[\cos^{-1}\left(\frac{x^2-1}{x^2+1}\right)\right] =$
   <br>(a) $\frac{-4x}{x^2+1}$   <br>(b) $\frac{4x}{x^4-1}$   <br>(c) $\frac{-2}{1+x^2}$   <br>(d) $\frac{-4}{x(1+x^2)}$

6. 🟡 $\frac{d}{dx}[\tan^{-1}(\cot x)] =$
   <br>(a) $0$   <br>(b) $-1$   <br>(c) $1$   <br>(d) $\sec^2 x$

7. 🟡 $\frac{d}{dx}\left[\sin^{-1}\left(\sqrt{\frac{1-x}{2}}\right)\right] =$
   <br>(a) $\frac{-1}{2\sqrt{1-x^2}}$   <br>(b) $\frac{1}{2\sqrt{1-x^2}}$   <br>(c) $\frac{-1}{\sqrt{1-x^2}}$   <br>(d) $\frac{1}{\sqrt{1-x^2}}$

8. 🔴 ⭐ If $y = \tan^{-1}\left(\frac{1}{1+x+x^2}\right)$, then $y' =$
   <br>(a) $\frac{1}{1+(1+x)^2} - \frac{1}{1+x^2}$   <br>(b) $\frac{-1}{1+(1+x)^2}$   <br>(c) $\frac{1}{1+x^2}$   <br>(d) $0$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | a | 5 | c |
| 2 | b | 6 | b |
| 3 | b | 7 | a |
| 4 | d | 8 | a |

</details>

---

## What's Next?

You've conquered every differentiation technique: rules, chain rule, implicit, parametric, logarithmic, higher order, and special functions. Now we step into the JEE-level application territory. In **Chapter 12**, we meet the **Mean Value Theorems** — Rolle's theorem and Lagrange's MVT — which connect derivatives to the geometry of curves.
