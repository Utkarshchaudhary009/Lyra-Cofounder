# Chapter 2: Standard Limits & Trigonometric Limits

---

## Stage 1: The Core Idea

### The Wall of 0/0

In Chapter 1, you learned how to evaluate limits that resulted in the $0/0$ indeterminate form by factoring or rationalizing.

But what happens when you face $\lim_{x\to0} \frac{\sin x}{x}$?
- Direct substitution gives $\frac{\sin 0}{0} = \frac{0}{0}$.
- You can't factor $\sin x$.
- You can't rationalize it.

Or what about $\lim_{x\to0} \frac{e^x - 1}{x}$?
- Direct substitution gives $\frac{e^0 - 1}{0} = \frac{1 - 1}{0} = \frac{0}{0}$.
- Again, algebraic tricks fail.

To break through this wall, mathematicians established **Standard Limits**. Think of these as pre-solved puzzle pieces. Your job is no longer to solve the limit from scratch, but to manipulate the expression algebraically until it matches one of these pre-solved pieces.

### The Most Important Limit in Calculus

The cornerstone of all trigonometric limits is:
$$\lim_{x\to0} \frac{\sin x}{x} = 1$$

*Why is it 1?*
Imagine a circle of radius 1. For a very small angle $x$ (in radians), the length of the arc ($x$) and the length of the vertical sine line ($\sin x$) become nearly identical. As $x$ shrinks to 0, their ratio becomes exactly 1.

**(Note: This only works if $x$ is in radians!)**

---

## Stage 2: The Formula Lab

Here are the standard limits you must memorize. They are the grammar rules for the language of limits.

### 1. Trigonometric Standard Limits (Angle must be in radians and $\to 0$)
| Formula | Trap Warning |
|---------|--------------|
| $\lim_{x\to0} \frac{\sin x}{x} = 1$ | The angle inside sine MUST exactly match the denominator. |
| $\lim_{x\to0} \frac{\tan x}{x} = 1$ | Works for tan, but NOT for cos. $\lim_{x\to0} \cos x = 1$. |
| $\lim_{x\to0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$ | A very common pattern. Notice the $x^2$ in the denominator. |
| $\lim_{x\to0} \frac{\sin^{-1} x}{x} = 1$ | Works for inverse trig too. |
| $\lim_{x\to0} \frac{\tan^{-1} x}{x} = 1$ | |

### 2. Exponential and Logarithmic Standard Limits
| Formula | Trap Warning |
|---------|--------------|
| $\lim_{x\to0} \frac{e^x - 1}{x} = 1$ | The power of $e$ MUST exactly match the denominator. |
| $\lim_{x\to0} \frac{a^x - 1}{x} = \ln a$ | When the base is not $e$, the limit is $\ln(\text{base})$. ($a > 0$) |
| $\lim_{x\to0} \frac{\ln(1 + x)}{x} = 1$ | The term added to 1 inside the log MUST match the denominator. |

### The Golden Rule of Standard Limits

The variable doesn't matter. The structure matters.
If $\text{B(x)} \to 0$, then:
- $\lim_{\text{B(x)}\to0} \frac{\sin(\text{B(x)})}{\text{B(x)}} = 1$
- $\lim_{\text{B(x)}\to0} \frac{e^{\text{B(x)}} - 1}{\text{B(x)}} = 1$

Your goal in every problem is to build $\text{B(x)}$ in the denominator to match the numerator.

---

## Stage 3: Type-wise Mastery

### Type 1: Basic Trigonometric Limits (Matching Angles)

**Goal:** Multiply and divide to make the denominator match the angle inside the sine or tangent.

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{\sin 5x}{x}$

**Solution:**
```
The angle is 5x. We need 5x in the denominator.
Multiply numerator and denominator by 5:
= lim(x→0) [5 * sin(5x)] / (5x)
= 5 * lim(x→0) [sin(5x) / 5x]
Since x → 0, 5x → 0.
= 5 * (1) = 5
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 $\lim_{x\to0} \frac{\sin 3x}{x}$
<details>
<summary>Solution</summary>

Multiply numerator and denominator by 3:
`lim(x→0) (3 * sin(3x)) / (3x) = 3 * lim(x→0) sin(3x)/(3x)`
Since `x → 0`, `3x → 0`. The standard limit gives `1`.
Result: `3 * 1 =` **3**.
</details>

2. 🟢 $\lim_{x\to0} \frac{\tan 7x}{2x}$
<details>
<summary>Solution</summary>

Rewrite as `(1/2) * lim(x→0) tan(7x)/x`.
Multiply and divide by 7: `(1/2) * 7 * lim(x→0) tan(7x)/(7x)`.
Standard limit `tan(u)/u → 1`.
Result: `7/2 * 1 =` **7/2**.
</details>

3. 🟡 $\lim_{x\to0} \frac{\sin 4x}{\sin 9x}$ — *Hint: Divide numerator and denominator by x*
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x`:
`[sin(4x)/x] / [sin(9x)/x]`.
For numerator, multiply/divide by 4: `4 * [sin(4x)/(4x)] → 4 * 1 = 4`.
For denominator, multiply/divide by 9: `9 * [sin(9x)/(9x)] → 9 * 1 = 9`.
Result: **4/9**.
</details>

4. 🟡 $\lim_{x\to0} \frac{x \sin x}{1 - \cos x}$ — *Hint: Multiply conjugate (1+cos x)*
<details>
<summary>Solution</summary>

Multiply by `(1 + cos x) / (1 + cos x)`:
`(x sin x)(1 + cos x) / (1 - cos²x) = (x sin x)(1 + cos x) / (sin²x)`.
Cancel one `sin x`: `x(1 + cos x) / sin x`.
Rewrite as `(x / sin x) * (1 + cos x)`.
Since `lim(sin x / x) = 1`, `lim(x / sin x) = 1`.
As `x → 0`, `cos x → 1`, so `1 + cos x → 2`.
Result: `1 * 2 =` **2**.
*(Alternatively, use `1 - cos x = 2sin²(x/2)`)*
</details>

5. 🟡 $\lim_{x\to0} \frac{\sin(x^\circ)}{x}$ — *Hint: Convert degrees to radians first!*
<details>
<summary>Solution</summary>

Convert `x` degrees to radians: `x^\circ = (π/180) * x` radians.
The limit becomes `lim(x→0) sin(πx/180) / x`.
Multiply numerator and denominator by `π/180`:
`(π/180) * lim(x→0) sin(πx/180) / (πx/180) = (π/180) * 1 =` **π/180**.
</details>

---

### Type 2: Trigonometric Identities to Standard Limits

**Goal:** Use identities like $1 - \cos 2x = 2\sin^2 x$ to transform the limit into a standard form.

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{1 - \cos 4x}{x^2}$

**Solution:**
```
Use the identity: 1 - cos(θ) = 2sin²(θ/2). Here θ = 4x.
1 - cos 4x = 2sin²(2x)

= lim(x→0) [2sin²(2x)] / x²
= 2 * lim(x→0) [sin(2x) / x]²

We need 2x in the denominator inside the square. Multiply and divide by 2 inside:
= 2 * lim(x→0) [ 2 * sin(2x) / (2x) ]²
= 2 * [ 2 * 1 ]²
= 2 * 4 = 8
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟢 $\lim_{x\to0} \frac{1 - \cos 2x}{x^2}$
<details>
<summary>Solution</summary>

Use identity `1 - cos(2x) = 2sin²(x)`.
`lim(x→0) 2sin²(x) / x² = 2 * lim(x→0) (sin x / x)²`.
Since `lim (sin x / x) = 1`, the result is `2 * 1² =` **2**.
</details>

7. 🟡 $\lim_{x\to0} \frac{1 - \cos x}{x \sin x}$
<details>
<summary>Solution</summary>

Use `1 - cos x = 2sin²(x/2)`.
`lim(x→0) 2sin²(x/2) / (x sin x)`.
Divide numerator and denominator by `x²`:
Numerator: `2 * [sin(x/2) / x]² = 2 * [(1/2) * sin(x/2)/(x/2)]² → 2 * (1/4) = 1/2`.
Denominator: `(x sin x) / x² = sin x / x → 1`.
Result: `(1/2) / 1 =` **1/2**.
</details>

8. 🟡 $\lim_{x\to0} \frac{\tan x - \sin x}{x^3}$ — *Hint: factor out sin x*
<details>
<summary>Solution</summary>

Write `tan x` as `sin x / cos x`:
`(sin x / cos x - sin x) / x³ = sin x (1/cos x - 1) / x³ = sin x (1 - cos x) / (x³ cos x)`.
Split into standard limits: `(sin x / x) * [(1 - cos x)/x²] * (1 / cos x)`.
`lim(sin x / x) = 1`.
`lim((1 - cos x)/x²) = 1/2`.
`lim(1 / cos x) = 1`.
Result: `1 * 1/2 * 1 =` **1/2**.
</details>

9. 🔴 $\lim_{x\to0} \frac{\sqrt{1 - \cos 2x}}{x}$ — *Careful: $\sqrt{x^2} = |x|$*
<details>
<summary>Solution</summary>

`1 - cos 2x = 2sin²x`.
`√(2sin²x) = √2 * |sin x|`.
Limit: `lim(x→0) √2 |sin x| / x`.
RHL: as `x → 0⁺`, `|sin x| = sin x`. Limit is `√2 (sin x / x) = √2`.
LHL: as `x → 0⁻`, `|sin x| = -sin x`. Limit is `√2 (-sin x / x) = -√2`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

10. 🟡 $\lim_{x\to0} \frac{\cos 3x - \cos x}{x^2}$ — *Use cos C - cos D formula*
<details>
<summary>Solution</summary>

Formula: `cos C - cos D = -2sin((C+D)/2)sin((C-D)/2)`.
`cos 3x - cos x = -2sin(2x)sin(x)`.
Limit: `lim(x→0) -2sin(2x)sin(x) / x² = -2 * lim(x→0) [sin(2x)/x] * [sin(x)/x]`.
`sin(2x)/x = 2 * sin(2x)/(2x) → 2`.
`sin(x)/x → 1`.
Result: `-2 * 2 * 1 =` **-4**.
</details>

---

### Type 3: Exponential Limits

**Goal:** Match the exponent to the denominator using $\frac{e^x - 1}{x} = 1$ or $\frac{a^x - 1}{x} = \ln a$.

**Solved Example:**

Find $\lim_{x\to0} \frac{e^{3x} - 1}{x}$

**Solution:**
```
The exponent is 3x. We need 3x in the denominator.
Multiply numerator and denominator by 3:
= lim(x→0) 3 * [(e^{3x} - 1) / (3x)]
= 3 * 1 = 3
```
🟢 Easy

---

**Practice Problems:**

11. 🟢 $\lim_{x\to0} \frac{e^{5x} - 1}{2x}$
<details>
<summary>Solution</summary>

Rewrite as `(1/2) * lim (e^{5x} - 1)/x`.
Multiply by 5/5: `(5/2) * lim (e^{5x} - 1)/(5x)`.
Standard limit gives 1.
Result: `5/2 * 1 =` **5/2**.
</details>

12. 🟡 $\lim_{x\to0} \frac{e^x - e^{-x}}{x}$ — *Hint: Add and subtract 1*
<details>
<summary>Solution</summary>

Add and subtract 1: `(e^x - 1 - e^{-x} + 1)/x = (e^x - 1)/x - (e^{-x} - 1)/x`.
First limit: `lim (e^x - 1)/x = 1`.
Second limit: `lim (e^{-x} - 1)/x = -1 * lim (e^{-x} - 1)/(-x) = -1 * 1 = -1`.
Result: `1 - (-1) =` **2**.
</details>

13. 🟡 $\lim_{x\to0} \frac{2^x - 1}{x}$
<details>
<summary>Solution</summary>

Using standard limit `(a^x - 1)/x → \ln a`.
Here `a = 2`.
Result is **\ln 2**.
</details>

14. 🟡 $\lim_{x\to0} \frac{e^{\sin x} - 1}{x}$ — *Hint: Multiply and divide by sin x*
<details>
<summary>Solution</summary>

Multiply and divide by `sin x`:
`lim(x→0) [ (e^{\sin x} - 1) / \sin x ] * [ \sin x / x ]`.
As `x → 0`, `\sin x → 0`. The first factor is the standard limit `(e^u - 1)/u → 1`.
The second factor is `1`.
Result: `1 * 1 =` **1**.
</details>

15. 🔴 $\lim_{x\to0} \frac{3^x - 2^x}{x}$ — *Hint: Add and subtract 1*
<details>
<summary>Solution</summary>

Add and subtract 1: `(3^x - 1 - 2^x + 1)/x = (3^x - 1)/x - (2^x - 1)/x`.
Use standard limit `(a^x - 1)/x → \ln a`.
Limit is `\ln 3 - \ln 2 =` **\ln(3/2)**.
</details>

---

### Type 4: Logarithmic Limits

**Goal:** Use $\frac{\ln(1+x)}{x} = 1$ by manipulating the expression inside the log.

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{\ln(1 + 4x)}{x}$

**Solution:**
```
We need 4x in the denominator.
Multiply numerator and denominator by 4:
= lim(x→0) 4 * [\ln(1 + 4x) / (4x)]
= 4 * 1 = 4
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

16. 🟢 $\lim_{x\to0} \frac{\ln(1 - 2x)}{x}$
<details>
<summary>Solution</summary>

We need `-2x` in the denominator.
Multiply numerator and denominator by -2:
`-2 * lim [\ln(1 - 2x) / (-2x)]`.
Standard limit gives 1.
Result: `-2 * 1 =` **-2**.
</details>

17. 🟡 $\lim_{x\to0} \frac{\log_{10}(1 + x)}{x}$ — *Hint: Change base to e*
<details>
<summary>Solution</summary>

Change of base formula: `\log_{10}(1+x) = \ln(1+x) / \ln 10`.
The limit becomes `lim [ (1 / \ln 10) * \ln(1+x)/x ]`.
Since `\ln(1+x)/x → 1`, the result is **1 / \ln 10**.
</details>

18. 🟡 $\lim_{x\to0} \frac{\ln(1 + x^2)}{x \sin x}$
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x²`:
Num: `\ln(1 + x²) / x² → 1` (since `x² → 0`).
Denom: `(x \sin x) / x² = \sin x / x → 1`.
Result: `1 / 1 =` **1**.
</details>

19. 🔴 $\lim_{x\to1} \frac{\ln x}{x - 1}$ — *Hint: Let x = 1+h*
<details>
<summary>Solution</summary>

Let `h = x - 1`. As `x → 1`, `h → 0`. `x = 1 + h`.
Substitute: `\ln(1 + h) / h`.
This is exactly the standard limit formula.
Result: **1**.
</details>

20. 🔴 $\lim_{x\to0} \frac{\ln(2 + x) - \ln 2}{x}$ — *Hint: Use log properties to get ln(1 + something)*
<details>
<summary>Solution</summary>

Use log subtraction property: `\ln(2+x) - \ln 2 = \ln((2+x)/2) = \ln(1 + x/2)`.
Limit: `lim [\ln(1 + x/2)] / x`.
Multiply/divide by 2: `(1/2) * lim [\ln(1 + x/2) / (x/2)]`.
Standard limit gives 1.
Result: `1/2 * 1 =` **1/2**.
</details>

---

### Type 5: Limit Evaluation using Substitution ($x \to a, a \neq 0$)

**Goal:** Standard limits only work when the variable approaches 0. If $x \to a$, substitute $h = x - a$ so that $h \to 0$.

**Solved Example:** ⭐

Find $\lim_{x\to\pi} \frac{\sin x}{x - \pi}$

**Solution:**
```
Let h = x - π. As x → π, h → 0.
Then x = π + h.

Substitute:
= lim(h→0) sin(π + h) / h
Since sin(π + h) = -sin(h):
= lim(h→0) -sin(h) / h
= -1 * lim(h→0) sin(h)/h
= -1
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟢 $\lim_{x\to\pi/2} \frac{\cos x}{x - \pi/2}$
<details>
<summary>Solution</summary>

Let `h = x - π/2`, so `x = π/2 + h`. As `x → π/2`, `h → 0`.
Substitute: `cos(π/2 + h) / h`.
Using trig identity: `cos(π/2 + h) = -sin(h)`.
Limit: `lim(h→0) -sin(h)/h = -1 * 1 =` **-1**.
</details>

22. 🟡 $\lim_{x\to1} \frac{\sin(\pi x)}{x - 1}$
<details>
<summary>Solution</summary>

Let `h = x - 1`, so `x = 1 + h`. As `x → 1`, `h → 0`.
Substitute: `sin(π(1 + h)) / h = sin(π + πh) / h`.
Using trig identity: `sin(π + θ) = -sin(θ)`. So `sin(π + πh) = -sin(πh)`.
Limit: `lim(h→0) -sin(πh)/h`. Multiply and divide by `π`: `-π * lim(h→0) sin(πh)/(πh) = -π * 1 =` **-π**.
</details>

23. 🟡 $\lim_{x\to\pi/4} \frac{\sin x - \cos x}{x - \pi/4}$
<details>
<summary>Solution</summary>

Let `h = x - π/4`, so `x = π/4 + h`. As `x → π/4`, `h → 0`.
Num: `sin(π/4 + h) - cos(π/4 + h)`.
`sin(π/4 + h) = (1/√2)cos h + (1/√2)sin h`.
`cos(π/4 + h) = (1/√2)cos h - (1/√2)sin h`.
Subtracting them: `((1/√2)cos h + (1/√2)sin h) - ((1/√2)cos h - (1/√2)sin h) = (2/√2)sin h = √2 sin h`.
Limit: `lim(h→0) (√2 sin h) / h = √2 * 1 =` **√2**.
</details>

24. 🔴 $\lim_{x\to a} \frac{x \sin a - a \sin x}{x - a}$
<details>
<summary>Solution</summary>

Let `h = x - a`, so `x = a + h`.
Num: `(a+h)sin a - a sin(a+h) = a sin a + h sin a - a[sin a cos h + cos a sin h]`.
Group terms: `a sin a(1 - cos h) + h sin a - a cos a sin h`.
Divide by `h`: `a sin a * (1 - cos h)/h + sin a - a cos a * (sin h)/h`.
Limit as `h → 0`:
`(1 - cos h)/h → 0`.
`(sin h)/h → 1`.
Result: `a sin a * (0) + sin a - a cos a * (1) =` **sin a - a cos a**.
</details>

25. 🔴 $\lim_{x\to 2} \frac{e^x - e^2}{x - 2}$
<details>
<summary>Solution</summary>

Let `h = x - 2`, so `x = 2 + h`.
Num: `e^{2+h} - e² = e² * e^h - e² = e²(e^h - 1)`.
Limit: `lim(h→0) e²(e^h - 1)/h = e² * lim(h→0) (e^h - 1)/h`.
Since the standard limit is 1, the result is `e² * 1 =` **e²**.
</details>

---

### Type 6: Evaluating Limits of $1^\infty$ Form

**Goal:** Evaluate limits of the form $\lim (1 + f(x))^{g(x)}$ where $f(x) \to 0$ and $g(x) \to \infty$.

**Key Formula:**
If $\lim_{x\to a} f(x) = 0$ and $\lim_{x\to a} g(x) = \infty$, then:
$$\lim_{x\to a} (1 + f(x))^{g(x)} = e^{\lim_{x\to a} f(x)g(x)}$$

*(Or generally: $\lim_{x\to a} (h(x))^{g(x)} = e^{\lim_{x\to a} (h(x)-1)g(x)}$ if the form is $1^\infty$)*

**Solved Example:** ⭐

Find $\lim_{x\to0} (1 + 3x)^{2/x}$

**Solution:**
```
As x → 0, the base (1+3x) → 1, and exponent 2/x → ∞. This is 1^∞ form.
Using the shortcut formula: f(x) = 3x, g(x) = 2/x
Limit = e^[ lim(x→0) (3x) * (2/x) ]
= e^[ lim(x→0) 6 ]
= e^6
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

26. 🟢 $\lim_{x\to0} (1 + 5x)^{1/x}$
<details>
<summary>Solution</summary>

Form is `1^∞`. Here `f(x) = 5x`, `g(x) = 1/x`.
Limit = `e^[lim(x→0) f(x) * g(x)]`.
`lim(x→0) 5x * (1/x) = 5`.
Result: **e⁵**.
</details>

27. 🟡 $\lim_{x\to0} (1 - 2x)^{3/x}$
<details>
<summary>Solution</summary>

Form is `1^∞`. Here `f(x) = -2x`, `g(x) = 3/x`.
Limit = `e^[lim(x→0) (-2x) * (3/x)]`.
`lim(x→0) -6 = -6`.
Result: **e⁻⁶**.
</details>

28. 🟡 $\lim_{x\to0} (\cos x)^{1/x^2}$ — *Hint: Base is cos x. h(x)-1 = cos x - 1*
<details>
<summary>Solution</summary>

Form is `1^∞`. Using general formula `e^[lim (h(x)-1) * g(x)]`.
Base `h(x) = cos x`, so `h(x) - 1 = cos x - 1`. Exponent `g(x) = 1/x²`.
Power limit: `lim(x→0) (cos x - 1) * (1/x²) = lim(x→0) -(1 - cos x)/x² = -1/2`.
Result: **e^{-1/2}** or **1/√e**.
</details>

29. 🔴 $\lim_{x\to\infty} \left(\frac{x+2}{x-1}\right)^x$ — *Hint: Let y = 1/x, y→0*
<details>
<summary>Solution</summary>

Base limit as `x → ∞` is `1`. Exponent is `∞`. So it's `1^∞` form.
`h(x) - 1 = (x+2)/(x-1) - 1 = (x+2 - x + 1)/(x-1) = 3/(x-1)`.
Power limit: `lim(x→∞) [3/(x-1)] * x = lim(x→∞) 3x/(x-1) = 3`.
Result: **e³**.
</details>

30. 🔴 $\lim_{x\to0} (1 + \sin x)^{2\cot x}$
<details>
<summary>Solution</summary>

Form is `1^∞`. `f(x) = sin x`, `g(x) = 2cot x = 2cos x / sin x`.
Power limit: `lim(x→0) (sin x) * (2cos x / sin x) = lim(x→0) 2cos x = 2(1) = 2`.
Result: **e²**.
</details>

---

### Type 7: Inverse Trigonometric Limits

**Goal:** Use the standard limits $\lim_{x\to0} \frac{\sin^{-1}x}{x} = 1$ and $\lim_{x\to0} \frac{\tan^{-1}x}{x} = 1$.

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{\sin^{-1}(3x)}{\tan^{-1}(2x)}$

**Solution:**
```
Divide numerator and denominator by x:
= lim(x→0) [sin⁻¹(3x) / x] / [tan⁻¹(2x) / x]
Multiply numerator by 3/3 and denominator by 2/2:
= lim(x→0) [3 * sin⁻¹(3x) / (3x)] / [2 * tan⁻¹(2x) / (2x)]
= (3 * 1) / (2 * 1) = 3/2
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

31. 🟢 $\lim_{x\to0} \frac{\sin^{-1}(5x)}{x}$
<details>
<summary>Solution</summary>

Multiply numerator and denominator by 5:
`lim(x→0) 5 * [\sin^{-1}(5x) / (5x)]`.
Standard limit `sin⁻¹(u)/u → 1`.
Result: `5 * 1 =` **5**.
</details>

32. 🟡 $\lim_{x\to0} \frac{x \tan^{-1}(4x)}{1 - \cos x}$
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x²`:
Numerator: `(x \tan^{-1}(4x)) / x² = \tan^{-1}(4x) / x`.
Denominator: `(1 - \cos x) / x²`.
Num limit: `lim 4 * [\tan^{-1}(4x) / (4x)] = 4 * 1 = 4`.
Denom limit: `lim (1 - \cos x)/x² = 1/2`.
Result: `4 / (1/2) =` **8**.
</details>

33. 🟡 $\lim_{x\to0} \frac{\sin^{-1}(x^2)}{x^2}$
<details>
<summary>Solution</summary>

Let `u = x²`. As `x → 0`, `u → 0⁺`.
Limit becomes `lim(u→0) \sin^{-1}(u) / u`.
This is exactly the standard limit.
Result: **1**.
</details>

34. 🔴 $\lim_{x\to0} \frac{\sin^{-1}(\sin x)}{x}$
<details>
<summary>Solution</summary>

For `x` very close to 0 (specifically `|x| < π/2`), `\sin^{-1}(\sin x) = x`.
So the expression is `x / x = 1` for `x ≠ 0`.
Limit is `lim(x→0) 1 =` **1**.
</details>

35. 🔴 $\lim_{x\to0} \frac{\tan^{-1}(\sin x)}{x}$
<details>
<summary>Solution</summary>

Divide and multiply by `\sin x`:
`lim [\tan^{-1}(\sin x) / \sin x] * [\sin x / x]`.
As `x → 0`, `\sin x → 0`. The first factor is the standard limit `\tan^{-1}(u)/u → 1`.
The second factor `\sin x / x → 1`.
Result: `1 * 1 =` **1**.
</details>

---

### Type 8: The Expansion Method (JEE Super-Weapon)

**Goal:** When standard limits are too complex or give $0/0$ even after basic manipulation, use Taylor/Maclaurin series expansions. 

**Key Expansions to Memorize:**
- $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
- $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
- $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$
- $\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \dots$

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{x - \sin x}{x^3}$

**Solution:**
```
Expand sin x:
sin x = x - x³/6 + x⁵/120 - ...

Substitute into the limit:
= lim(x→0) [ x - (x - x³/6 + x⁵/120 - ...) ] / x³
= lim(x→0) [ x³/6 - x⁵/120 + ... ] / x³

Divide by x³:
= lim(x→0) [ 1/6 - x²/120 + ... ]

As x → 0, all higher power terms become 0.
= 1/6
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

36. 🟡 $\lim_{x\to0} \frac{e^x - 1 - x}{x^2}$
<details>
<summary>Solution</summary>

Expand `e^x = 1 + x + x²/2! + x³/3! + ...`
Numerator: `(1 + x + x²/2 + x³/6 + ...) - 1 - x = x²/2 + x³/6 + ...`
Divide by `x²`: `(x²/2 + x³/6 + ...) / x² = 1/2 + x/6 + ...`
As `x → 0`, limit is **1/2**.
</details>

37. 🟡 $\lim_{x\to0} \frac{x - \ln(1+x)}{x^2}$
<details>
<summary>Solution</summary>

Expand `\ln(1+x) = x - x²/2 + x³/3 - ...`
Numerator: `x - (x - x²/2 + x³/3 - ...) = x²/2 - x³/3 + ...`
Divide by `x²`: `(x²/2 - x³/3 + ...) / x² = 1/2 - x/3 + ...`
As `x → 0`, limit is **1/2**.
</details>

38. 🔴 $\lim_{x\to0} \frac{\tan x - x}{x^3}$
<details>
<summary>Solution</summary>

Expand `\tan x = x + x³/3 + 2x⁵/15 + ...`
Numerator: `(x + x³/3 + ...) - x = x³/3 + ...`
Divide by `x³`: `(x³/3 + ...) / x³ = 1/3 + ...`
As `x → 0`, limit is **1/3**.
</details>

39. 🔴 $\lim_{x\to0} \frac{\cos x - 1 + x^2/2}{x^4}$
<details>
<summary>Solution</summary>

Expand `\cos x = 1 - x²/2! + x⁴/4! - x⁶/6! + ...`
Numerator: `(1 - x²/2 + x⁴/24 - ...) - 1 + x²/2 = x⁴/24 - ...`
Divide by `x⁴`: `(x⁴/24 - ...) / x⁴ = 1/24 - ...`
As `x → 0`, limit is **1/24**.
</details>

40. 🔴 $\lim_{x\to0} \frac{e^x - e^{-x} - 2x}{x^3}$
<details>
<summary>Solution</summary>

Expand `e^x = 1 + x + x²/2 + x³/6 + ...`
Expand `e^{-x} = 1 - x + x²/2 - x³/6 + ...`
`e^x - e^{-x} = 2x + 2(x³/6) + 2(x⁵/120) + ... = 2x + x³/3 + ...`
Numerator: `(2x + x³/3 + ...) - 2x = x³/3 + ...`
Divide by `x³`: `(x³/3 + ...) / x³ = 1/3 + ...`
As `x → 0`, limit is **1/3**.
</details>

---

### Type 9: Adding & Subtracting 1 (Numerator Splitting)

**Goal:** Break complex numerators into separate standard limits by adding and subtracting terms (usually 1).

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{e^{3x} + e^{2x} - 2}{x}$

**Solution:**
```
Split the "-2" into "-1" and "-1":
= lim(x→0) (e^{3x} - 1 + e^{2x} - 1) / x

Separate the fraction:
= lim(x→0) [ (e^{3x} - 1)/x ] + [ (e^{2x} - 1)/x ]
= 3(1) + 2(1) = 5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

41. 🟢 $\lim_{x\to0} \frac{e^x + \sin x - 1}{x}$
<details>
<summary>Solution</summary>

Rearrange and split: `(e^x - 1 + \sin x) / x = (e^x - 1)/x + (\sin x)/x`.
Limits are `1 + 1 =` **2**.
</details>

42. 🟡 $\lim_{x\to0} \frac{a^x - b^x}{x}$ — *Hint: +1 and -1*
<details>
<summary>Solution</summary>

Add and subtract 1: `(a^x - 1 - b^x + 1)/x = (a^x - 1)/x - (b^x - 1)/x`.
Limits: `\ln a - \ln b =` **\ln(a/b)**.
</details>

43. 🟡 $\lim_{x\to0} \frac{e^{5x} + 2^x - 2}{x}$
<details>
<summary>Solution</summary>

Split -2 into -1 and -1: `(e^{5x} - 1 + 2^x - 1)/x = (e^{5x} - 1)/x + (2^x - 1)/x`.
First limit: multiply/divide by 5, gives `5`.
Second limit: gives `\ln 2`.
Result: **5 + \ln 2**.
</details>

44. 🔴 $\lim_{x\to0} \frac{\ln(1+x) + \cos x - 1}{x}$
<details>
<summary>Solution</summary>

Split: `(\ln(1+x))/x - (1 - \cos x)/x`.
First limit: `1`.
Second limit: `lim (1 - \cos x)/x * (x/x) = lim [(1 - \cos x)/x²] * x = (1/2)*0 = 0`.
Result: `1 - 0 =` **1**.
</details>

45. 🔴 $\lim_{x\to0} \frac{e^x \cos x - 1}{x}$ — *Hint: Add and subtract e^x or 1*
<details>
<summary>Solution</summary>

Add and subtract `e^x`: `(e^x \cos x - e^x + e^x - 1)/x = e^x(\cos x - 1)/x + (e^x - 1)/x`.
First part: `lim e^x * lim (\cos x - 1)/x = 1 * 0 = 0`.
Second part: `lim (e^x - 1)/x = 1`.
Result: `0 + 1 =` **1**.
</details>

---

## Stage 4: Type Mixer

1. 🟡 $\lim_{x\to0} \frac{1 - \cos 2x}{x(e^x - 1)}$ *[Trig + Exponential]*
<details>
<summary>Solution</summary>

Multiply and divide by `x`: `(1 - \cos 2x) / x² * [ x / (e^x - 1) ]`.
First factor: `(1 - \cos 2x)/x² = 2\sin²x/x² → 2`.
Second factor: `x/(e^x - 1) → 1`.
Limit: `2 * 1 =` **2**.
</details>

2. 🔴 $\lim_{x\to0} \frac{\ln(1 + x^3)}{\sin^3 x}$ *[Log + Trig]*
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x³`:
`[ \ln(1 + x³) / x³ ] / [ (\sin x)/x ]³`.
Both numerator and denominator limits are 1.
Result: `1 / 1³ =` **1**.
</details>

3. 🟡 $\lim_{x\to0} \frac{a^x - b^x}{x}$ *[Exponential + Algebraic Manipulation]*
<details>
<summary>Solution</summary>

Add and subtract 1: `(a^x - 1 - (b^x - 1)) / x`.
Standard limit: `\ln a - \ln b =` **\ln(a/b)**.
</details>

4. 🔴 $\lim_{x\to\pi/2} (\sin x)^{\tan^2 x}$ *[1^∞ form with substitution]*
<details>
<summary>Solution</summary>

Form `1^∞`. Formula `e^[lim (\sin x - 1) * \tan² x]`.
Let `h = x - π/2`, `x = π/2 + h`.
`\sin(π/2 + h) = \cos h`. `\tan(π/2 + h) = -\cot h`.
Power limit: `lim(h→0) (\cos h - 1) * (-\cot h)² = lim(h→0) (\cos h - 1) * (\cos²h / \sin²h)`.
`\cos h - 1 = -2\sin²(h/2)`. `\sin²h = 4\sin²(h/2)\cos²(h/2)`.
Expression: `[-2\sin²(h/2) * \cos²h] / [4\sin²(h/2)\cos²(h/2)] = -\cos²h / [2\cos²(h/2)]`.
As `h → 0`, `\cos(0) = 1`. Power limit = `-1 / 2 = -1/2`.
Result: **e^{-1/2}** or **1/√e**.
</details>

5. 🔴 $\lim_{x\to0} \frac{x(e^x - 1)}{1 - \cos x}$ *[Trig + Exponential]*
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x²`:
Numerator: `x(e^x - 1) / x² = (e^x - 1) / x → 1`.
Denominator: `(1 - \cos x) / x² → 1/2`.
Result: `1 / (1/2) =` **2**.
</details>

6. 🔴 $\lim_{x\to1} (1 - x)\tan\left(\frac{\pi x}{2}\right)$ *[Substitution + Trig]*
<details>
<summary>Solution</summary>

Let `x = 1 - h`. As `x → 1`, `h → 0`.
Expression: `h * \tan(π(1 - h) / 2) = h * \tan(π/2 - πh/2)`.
`\tan(π/2 - θ) = \cot(θ)`. So it's `h * \cot(πh/2) = h / \tan(πh/2)`.
Multiply/divide by `π/2`: `(2/π) * [(πh/2) / \tan(πh/2)]`.
Standard limit gives 1.
Result: `(2/π) * 1 =` **2/π**.
</details>

7. 🔴 $\lim_{x\to0} \frac{\sin^{-1}(2x) - 2x}{x^3}$ *[Inverse Trig + Expansion]*
<details>
<summary>Solution</summary>

Expansion of `\sin^{-1} u = u + u³/6 + ...`
Here `u = 2x`, so `\sin^{-1}(2x) = 2x + (2x)³/6 + ... = 2x + 8x³/6 + ... = 2x + 4x³/3 + ...`
Numerator: `(2x + 4x³/3 + ...) - 2x = 4x³/3 + ...`
Divide by `x³`: `4/3 + ...`
Limit: **4/3**.
</details>

8. 🔴 $\lim_{x\to0} \frac{e^x - \ln(1+x) - 1}{x^2}$ *[Expansion Method]*
<details>
<summary>Solution</summary>

`e^x = 1 + x + x²/2 + ...`
`\ln(1+x) = x - x²/2 + ...`
Numerator: `(1 + x + x²/2) - (x - x²/2) - 1 = x²`.
Divide by `x²`: `x² / x² = 1`.
Limit: **1**.
</details>

9. 🟡 $\lim_{x\to0} \frac{3^x + 4^x - 2}{x}$ *[Numerator Splitting]*
<details>
<summary>Solution</summary>

Split -2: `(3^x - 1)/x + (4^x - 1)/x`.
Limits: `\ln 3 + \ln 4 = \ln(3 * 4) =` **\ln 12**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Evaluate $\lim_{x\to0} \frac{\sin 4x}{\sin 2x}$ **(2 marks)**

**Solution:**
Divide numerator and denominator by x:
= lim(x→0) [ (sin 4x)/x ] / [ (sin 2x)/x ]
Multiply by 4 and 2 respectively:
= lim(x→0) [ 4*(sin 4x)/(4x) ] / [ 2*(sin 2x)/(2x) ]
= (4*1) / (2*1) = 2

---

**Q2.** 🟡 Evaluate $\lim_{x\to0} \frac{1 - \cos 2x}{x^2}$ **(2 marks)**

**Solution:**
Using 1 - cos 2x = 2sin²x
= lim(x→0) (2sin²x) / x²
= 2 * lim(x→0) (sin x / x)²
= 2 * (1)² = 2

---

**Q3.** 🟡 ⭐ Evaluate $\lim_{x\to0} \frac{e^{ax} - e^{bx}}{x}$ **(3 marks)**

**Solution:**
Add and subtract 1 in the numerator:
= lim(x→0) (e^{ax} - 1 - e^{bx} + 1) / x
= lim(x→0) [ (e^{ax} - 1)/x ] - [ (e^{bx} - 1)/x ]
Multiply by a and b:
= a * lim(x→0) (e^{ax} - 1)/(ax) - b * lim(x→0) (e^{bx} - 1)/(bx)
= a(1) - b(1) = a - b

---

**Q4.** 🔴 Evaluate $\lim_{x\to0} \frac{\sqrt{1 + x} - 1}{\ln(1 + x)}$ **(4 marks)**

**Solution:**
Divide numerator and denominator by x:
= lim(x→0) [ (√(1+x) - 1)/x ] / [ \ln(1+x)/x ]
The denominator limit is 1 (Standard Limit).
For numerator, rationalize:
lim(x→0) (√(1+x) - 1)/x * (√(1+x) + 1)/(√(1+x) + 1)
= lim(x→0) (1+x - 1) / (x(√(1+x) + 1))
= lim(x→0) 1 / (√(1+x) + 1) = 1/2
Overall limit = (1/2) / 1 = 1/2

---

## Stage 6: JEE Mains Arena

**Q1.** $\lim_{x\to0} \frac{\sin(\pi \cos^2 x)}{x^2}$ equals:
(a) $\pi$   <br> (b) $-\pi$   <br> (c) $1$   <br> (d) $0$

<details>
<summary>Solution</summary>
cos²x = 1 - sin²x
Numerator = sin(π(1 - sin²x)) = sin(π - πsin²x) = sin(πsin²x)
Limit = lim(x→0) sin(πsin²x) / x²
Multiply and divide by πsin²x:
= lim(x→0) [sin(πsin²x) / (πsin²x)] * [πsin²x / x²]
As x→0, πsin²x → 0.
= 1 * π * lim(x→0) (sin x / x)²
= 1 * π * 1 = π
Answer: (a) 🔴 ⭐
</details>

---

**Q2.** Let $f(x) = \frac{1 - \tan x}{4x - \pi}$, $x \neq \pi/4$. If $\lim_{x\to\pi/4} f(x)$ exists, it equals:
(a) $-1/2$   <br> (b) $1/2$   <br> (c) $1$   <br> (d) $-1$

<details>
<summary>Solution</summary>
Let x = π/4 + h. As x → π/4, h → 0.
f(π/4 + h) = (1 - tan(π/4 + h)) / (4(π/4 + h) - π)
= (1 - (1+tan h)/(1-tan h)) / (4h)
= ((1-tan h - 1 - tan h) / (1-tan h)) / 4h
= -2tan h / (4h(1-tan h))
= (-2/4) * (tan h / h) * (1 / (1-tan h))
Limit as h→0: (-1/2) * 1 * (1/1) = -1/2
Answer: (a) 🟡
</details>

---

**Q3.** $\lim_{x\to0} \frac{\ln(1 + 3x^2)}{x(e^{2x} - 1)}$ equals:
(a) $2/3$   <br> (b) $3/2$   <br> (c) $3$   <br> (d) $1/2$

<details>
<summary>Solution</summary>
Rewrite to match standard limits:
= lim(x→0) [\ln(1 + 3x^2) / (3x^2)] * 3x^2 / (x * [(e^{2x} - 1)/(2x)] * 2x)
= lim(x→0) (1) * 3x^2 / (x * 1 * 2x)
= lim(x→0) 3x^2 / 2x^2 = 3/2
Answer: <br> (b) 🟡 ⭐
</details>

---

**Q4.** $\lim_{x\to0} (\sec x + \tan x)^{\frac{1}{x}}$ equals:
(a) $e$   <br> (b) $1$   <br> (c) $1/e$   <br> (d) $e^2$

<details>
<summary>Solution</summary>
This is 1^∞ form since sec 0 + tan 0 = 1 + 0 = 1, and 1/0 → ∞.
Use formula: e^[ lim(x→0) (sec x + tan x - 1) * (1/x) ]
= e^[ lim(x→0) ((1-cos x)/cos x + sin x/cos x) / x ]
= e^[ lim(x→0) (1-cos x)/(x cos x) + (sin x)/(x cos x) ]
(1-cos x)/x = (1-cos x)/x² * x → (1/2)*0 = 0.
(sin x)/x * (1/cos x) → 1 * 1 = 1.
So the exponent limit is 0 + 1 = 1.
Result = e^1 = e.
Answer: (a) 🔴
</details>

---

## Stage 7: Assertion-Reasoning

**Directions:** Choose:
(a) Both A and R are true and R is the correct explanation of A
<br> (b) Both A and R are true but R is NOT the correct explanation of A
<br> (c) A is true but R is false
<br> (d) A is false but R is true

---

**Q1.**
<br> **Assertion (A):** $\lim_{x\to0} \frac{\sin x^\circ}{x} = \frac{\pi}{180}$<br>
<br> **Reason (R):** The formula $\lim_{x\to0} \frac{\sin x}{x} = 1$ is only valid when $x$ is measured in radians.

<details>
<summary>Solution</summary>
A is true: x° = πx/180 radians. Limit = lim(x→0) sin(πx/180)/x = π/180.
R is true and is the exact reason why we must convert to radians.
Answer: (a) 🟢 ⭐
</details>

---

**Q2.** <br> **Assertion (A):** $\lim_{x\to0} \frac{1 - \cos x}{x} = 0$
<br> **Reason (R):** $\lim_{x\to0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$

<details>
<summary>Solution</summary>
A is true: lim(x→0) (1-cos x)/x = lim(x→0) [(1-cos x)/x^2] * x = (1/2) * 0 = 0.
R is true and can be used to prove A.
Answer: (a) 🟡
</details>

---

**Q3.** <br> **Assertion (A):** $\lim_{x\to0} \frac{e^x - 1}{x} = 1$ implies $\lim_{x\to0} \frac{2^x - 1}{x} = 1$
<br> **Reason (R):** The limit of $\frac{a^x - 1}{x}$ as $x\to0$ is $\ln a$.

<details>
<summary>Solution</summary>
A is false: The limit for 2^x is ln 2, not 1.
R is true: The standard limit for base a is ln a.
Answer: <br> (d) 🟢
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 $\lim_{x\to0} \frac{\sin 6x}{3x} =$
   <br>(a) $2$   <br> (b) $1/2$   <br> (c) $6$   <br> (d) $3$

2. 🟢 $\lim_{x\to0} \frac{1 - \cos x}{x^2} =$
   <br>(a) $1$   <br> (b) $0$   <br> (c) $1/2$   <br> (d) $-1/2$

3. 🟡 ⭐ $\lim_{x\to0} \frac{\tan 2x}{\sin 3x} =$
   <br>(a) $2/3$   <br> (b) $3/2$   <br> (c) $1$   <br> (d) $0$

4. 🟡 $\lim_{x\to0} \frac{e^{2x} - 1}{x} =$
   <br>(a) $1$   <br> (b) $2$   <br> (c) $e^2$   <br> (d) $1/2$

5. 🟡 $\lim_{x\to0} \frac{\ln(1 + 5x)}{x} =$
   <br>(a) $1$   <br> (b) $5$   <br> (c) $1/5$   <br> (d) $\ln 5$

6. 🟡 $\lim_{x\to0} \frac{x}{\sqrt{1 - \cos x}} =$
   <br>(a) $\sqrt{2}$   <br> (b) $-\sqrt{2}$   <br> (c) Does not exist   <br> (d) $1/\sqrt{2}$
   *(Hint: $\sqrt{x^2} = |x|$)*

7. 🟡 ⭐ $\lim_{x\to0} \frac{3^x - 1}{x} =$
   <br>(a) $1$   <br> (b) $3$   <br> (c) $\ln 3$   <br> (d) $\log_{10} 3$

8. 🔴 $\lim_{x\to\pi/2} \frac{\cos x}{\pi - 2x} =$
   <br>(a) $1$   <br> (b) $1/2$   <br> (c) $-1/2$   <br> (d) $0$

9. 🟡 $\lim_{x\to0} (1 + 4x)^{1/x} =$
   <br>(a) $e^4$   <br> (b) $e^{1/4}$   <br> (c) $4$   <br> (d) $1$

10. 🟡 $\lim_{x\to0} \frac{\sin^2 3x}{x^2} =$
    <br>(a) $3$   <br> (b) $6$   <br> (c) $9$   <br> (d) $1$

11. 🔴 $\lim_{x\to0} \frac{e^{\sin x} - 1}{x} =$
    <br>(a) $0$   <br> (b) $1$   <br> (c) $e$   <br> (d) $1/e$

12. 🔴 ⭐ $\lim_{x\to0} \frac{a^x - b^x}{x} =$
    <br>(a) $\ln(a/b)$   <br> (b) $\ln(ab)$   <br> (c) $a/b$   <br> (d) $\ln(b/a)$

13. 🔴 $\lim_{x\to0} \frac{\ln(1 + x)}{e^x - 1} =$
    <br>(a) $0$   <br> (b) $e$   <br> (c) $1$   <br> (d) $\ln 2$

14. 🟡 $\lim_{x\to0} \frac{\sin x^\circ}{x} =$
    <br>(a) $1$   <br> (b) $\pi/180$   <br> (c) $180/\pi$   <br> (d) $0$

15. 🔴 $\lim_{x\to\infty} \left(1 + \frac{1}{x}\right)^x =$
    <br>(a) $0$   <br> (b) $1$   <br> (c) $\infty$   <br> (d) $e$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| 1 | a | 6 | c | 11 | b |
| 2 | c | 7 | c | 12 | a |
| 3 | a | 8 | b | 13 | c |
| 4 | b | 9 | a | 14 | b |
| 5 | b | 10 | c | 15 | d |

</details>

---

## What's Next?

You've now mastered the grammar of limits. You can handle $0/0$ forms using algebra (Chapter 1) and standard limits for trig, exponential, and logarithmic functions (Chapter 2). You also learned how to handle the tricky $1^\infty$ form.

But what happens when $x$ doesn't approach a number like $0$ or $2$, but instead goes off to infinity?

In **Chapter 3**, we'll tackle **Limits at Infinity** ($\lim_{x\to\infty}$), which is all about figuring out which parts of a function dominate when numbers get unimaginably large.

**Key takeaway from Chapter 2:** Don't memorize a hundred formulas. Memorize the **structure** of the standard limits, and algebraically manipulate your problem until it matches that structure.
