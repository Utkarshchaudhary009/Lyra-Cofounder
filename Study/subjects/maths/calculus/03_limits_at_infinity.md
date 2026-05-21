# Chapter 3: Limits at Infinity

---

## Stage 1: The Core Idea

### The Battle of Growth Rates

Imagine you and a friend are playing a game. You both start counting. You add 100 every second ($100x$). Your friend squares the number of seconds ($x^2$).

At first, you are winning:
- 1 second: You = 100, Friend = 1
- 10 seconds: You = 1000, Friend = 100

But eventually, the square catches up and crushes the linear term:
- 100 seconds: You = 10,000, Friend = 10,000
- 1000 seconds: You = 100,000, Friend = 1,000,000

When we take limits as $x \to \infty$, we don't care about what happens at $x = 10$ or $x = 100$. We care about what happens when $x$ becomes unimaginably large. In that arena, **only the fastest-growing term matters.**

If you have $f(x) = x^3 + 1,000,000x^2$, as $x \to \infty$, the $x^3$ term becomes so massive that the $1,000,000x^2$ term is mathematically irrelevant. $x^3$ is the **dominant term**.

### The Ultimate Truth of Infinity

The entire chapter is built on one simple truth:
> **If you divide 1 pizza among an infinitely large number of people, everyone gets 0 pizza.**
> $$\lim_{x \to \infty} \frac{1}{x} = 0$$

If $\frac{1}{x} \to 0$, then $\frac{5}{x^2} \to 0$, and $\frac{1,000,000}{\sqrt{x}} \to 0$. Any constant divided by a variable that grows to infinity will approach exactly zero.

---

## Stage 2: The Formula Lab

### 1. The Dominant Term Rule (Rational Functions)

When evaluating $\lim_{x \to \infty} \frac{P(x)}{Q(x)}$ where $P$ and $Q$ are polynomials:

| Condition | Result | Why? |
|-----------|--------|------|
| Degree of Num < Degree of Den | **0** | Denominator grows faster and crushes the numerator. |
| Degree of Num = Degree of Den | **Ratio of leading coefficients** | Both grow at the same rate; a steady tie. |
| Degree of Num > Degree of Den | **$\infty$ or $-\infty$** | Numerator outgrows denominator. |

### 2. The Hierarchy of Infinity (Who wins?)

When $x \to \infty$, functions grow at vastly different speeds. Memorize this hierarchy (from slowest to fastest):
$$ \ln(x) \ll x^n \ll a^x \ll x! \ll x^x $$
*(Logs grow slower than polynomials, polynomials slower than exponentials, etc.)*

### 3. Trap Warnings
- **Trap 1:** $\infty - \infty$ is NOT zero. It is an indeterminate form. You must algebraically manipulate it (usually by factoring or rationalizing).
- **Trap 2:** $\lim_{x\to-\infty} \sqrt{x^2} = |x| = -x$. When $x$ goes to negative infinity, taking it out of a square root introduces a negative sign!

---

## Stage 3: Type-wise Mastery

### Type 1: Rational Functions (Polynomial / Polynomial)

**Goal:** Divide every term in the numerator and denominator by the highest power of $x$ present in the denominator.

**Solved Example:** ⭐

Find $\lim_{x\to\infty} \frac{3x^2 - 5x + 1}{2x^2 + 4}$

**Solution:**
```
The highest power of x in the denominator is x².
Divide every single term by x²:

= lim(x→∞) [ (3x²/x²) - (5x/x²) + (1/x²) ] / [ (2x²/x²) + (4/x²) ]
= lim(x→∞) [ 3 - 5/x + 1/x² ] / [ 2 + 4/x² ]

As x → ∞, any term with x in the denominator becomes 0.
= [ 3 - 0 + 0 ] / [ 2 + 0 ]
= 3/2
```
🟢 Easy ⭐ Must-Do

*(Notice this matches the shortcut: degrees are equal, so the answer is the ratio of leading coefficients: 3/2)*

---

**Practice Problems:**

1. 🟢 $\lim_{x\to\infty} \frac{4x^3 - 2x + 1}{7x^3 + 5}$
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x³` (highest power in denominator).
`lim(x→∞) (4 - 2/x² + 1/x³) / (7 + 5/x³)`.
As `x → ∞`, `1/x²` and `1/x³` go to 0.
Result: `4/7`.
</details>

2. 🟢 $\lim_{x\to\infty} \frac{x^2 + 5x}{x^3 - 1}$
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x³`.
`lim(x→∞) (1/x + 5/x²) / (1 - 1/x³)`.
As `x → ∞`, all `1/x` terms go to 0.
Result: `(0 + 0) / (1 - 0) =` **0**.
</details>

3. 🟡 $\lim_{x\to\infty} \frac{(2x+1)(3x-2)}{(x+5)(4x-1)}$ — *Hint: Find the leading term of the expanded form first.*
<details>
<summary>Solution</summary>

Numerator leading term: `(2x)(3x) = 6x²`.
Denominator leading term: `(x)(4x) = 4x²`.
Degrees are equal (degree 2).
Result is the ratio of leading coefficients: `6 / 4 =` **3/2**.
</details>

4. 🟡 $\lim_{x\to\infty} \frac{5x^4 - x^2}{2x^3 + 10x}$
<details>
<summary>Solution</summary>

Divide numerator and denominator by `x³`.
`lim(x→∞) (5x - 1/x) / (2 + 10/x²)`.
As `x → ∞`, numerator goes to `∞`, denominator goes to `2`.
Result: **∞** (or Limit Does Not Exist).
</details>

5. 🟡 $\lim_{n\to\infty} \frac{\sum n^2}{n^3}$ — *Hint: Use the formula for sum of squares: $n(n+1)(2n+1)/6$*
<details>
<summary>Solution</summary>

Sum of squares: `\sum n² = n(n+1)(2n+1)/6 = (2n³ + 3n² + n)/6`.
Limit: `lim(n→∞) (2n³ + 3n² + n) / (6n³)`.
Degrees are equal. Leading coefficients ratio: `2/6 =` **1/3**.
</details>

---

### Type 2: Limits with Square Roots

**Goal:** Handle $x$ inside square roots carefully. Remember $\sqrt{x^2} = |x|$. 
- If $x \to \infty$, $\sqrt{x^2} = x$. 
- If $x \to -\infty$, $\sqrt{x^2} = -x$.

**Solved Example:** ⭐

Find $\lim_{x\to-\infty} \frac{\sqrt{4x^2 + 1}}{3x - 5}$

**Solution:**
```
Divide numerator and denominator by x.
Since x is approaching negative infinity, x is negative.
So, when we bring x INSIDE the square root, we must write x = -√x².

Denominator: (3x - 5) / x = 3 - 5/x
Numerator: √(4x² + 1) / x = √(4x² + 1) / (-√x²) = -√( (4x² + 1)/x² ) = -√(4 + 1/x²)

Limit = lim(x→-∞) [ -√(4 + 1/x²) ] / [ 3 - 5/x ]
As x → -∞, 1/x² → 0 and 5/x → 0.
= -√(4 + 0) / (3 - 0)
= -2/3
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 $\lim_{x\to\infty} \frac{\sqrt{9x^2 + 2}}{5x + 1}$
<details>
<summary>Solution</summary>

Divide by `x` (since `x → ∞`, `x = \sqrt{x^2}`).
Numerator: `\sqrt{9x^2 + 2} / \sqrt{x^2} = \sqrt{9 + 2/x^2} → \sqrt{9} = 3`.
Denominator: `(5x + 1) / x = 5 + 1/x → 5`.
Result: **3/5**.
</details>

7. 🔴 $\lim_{x\to-\infty} \frac{\sqrt{x^2 + 4x}}{2x - 3}$
<details>
<summary>Solution</summary>

Divide by `x`. Since `x → -∞`, `x` is negative, so `x = -\sqrt{x^2}` inside the root.
Numerator: `\sqrt{x^2 + 4x} / (-\sqrt{x^2}) = -\sqrt{1 + 4/x} → -\sqrt{1} = -1`.
Denominator: `(2x - 3) / x = 2 - 3/x → 2`.
Result: **-1/2**.
</details>

8. 🟡 $\lim_{x\to\infty} \frac{x + \sqrt{x^2 + 1}}{3x}$
<details>
<summary>Solution</summary>

Divide by `x` (positive).
Numerator: `x/x + \sqrt{x^2+1}/x = 1 + \sqrt{1 + 1/x^2} → 1 + \sqrt{1} = 2`.
Denominator: `3x/x = 3`.
Result: **2/3**.
</details>

9. 🔴 $\lim_{x\to-\infty} \frac{x^2 + 1}{\sqrt{x^4 + 3x^2}}$
<details>
<summary>Solution</summary>

Divide by `x²` (which is always positive, so `x² = \sqrt{x^4}`).
Numerator: `(x² + 1)/x² = 1 + 1/x² → 1`.
Denominator: `\sqrt{x^4 + 3x^2}/\sqrt{x^4} = \sqrt{1 + 3/x^2} → 1`.
Result: `1/1 =` **1**.
</details>

10. 🔴 $\lim_{x\to\infty} \frac{\sqrt[3]{8x^3 + 1}}{2x - 1}$ — *Hint: $\sqrt[3]{x^3} = x$ for both positive and negative x.*
<details>
<summary>Solution</summary>

Divide by `x`. Inside the cube root, it becomes division by `x³`.
Numerator: `\sqrt[3]{8x^3 + 1} / \sqrt[3]{x^3} = \sqrt[3]{8 + 1/x^3} → \sqrt[3]{8} = 2`.
Denominator: `(2x - 1) / x = 2 - 1/x → 2`.
Result: `2/2 =` **1**.
</details>

---

### Type 3: Infinity Minus Infinity ($\infty - \infty$)

**Goal:** Convert $\infty - \infty$ into a fraction ($\infty/\infty$) by rationalizing or taking a common denominator.

**Solved Example:** ⭐

Find $\lim_{x\to\infty} (\sqrt{x^2 + x} - x)$

**Solution:**
```
Direct evaluation gives ∞ - ∞. Indeterminate!
Multiply and divide by the conjugate: (√(x² + x) + x)

= lim(x→∞) [ (√(x² + x) - x) * (√(x² + x) + x) ] / [ √(x² + x) + x ]
= lim(x→∞) [ (x² + x) - x² ] / [ √(x² + x) + x ]
= lim(x→∞) x / [ √(x² + x) + x ]

Now it is ∞/∞ form. Divide top and bottom by x (which is √x² inside the root):
= lim(x→∞) 1 / [ √(1 + 1/x) + 1 ]
= 1 / [ √(1 + 0) + 1 ] = 1/2
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 $\lim_{x\to\infty} (\sqrt{x^2 + 4x} - x)$
<details>
<summary>Solution</summary>

Multiply by conjugate `(\sqrt{x^2+4x} + x)`.
Numerator: `(x² + 4x) - x² = 4x`.
Expression: `4x / (\sqrt{x^2+4x} + x)`.
Divide by `x`: `4 / (\sqrt{1 + 4/x} + 1)`.
Limit: `4 / (1 + 1) =` **2**.
</details>

12. 🟡 $\lim_{x\to\infty} (\sqrt{x^2 + 1} - \sqrt{x^2 - 1})$
<details>
<summary>Solution</summary>

Multiply by conjugate `(\sqrt{x^2+1} + \sqrt{x^2-1})`.
Numerator: `(x² + 1) - (x² - 1) = 2`.
Expression: `2 / (\sqrt{x^2+1} + \sqrt{x^2-1})`.
As `x → ∞`, denominator goes to `∞`.
Result: `2 / ∞ =` **0**.
</details>

13. 🔴 $\lim_{x\to\infty} x(\sqrt{x^2 + 1} - x)$
<details>
<summary>Solution</summary>

Rationalize the term inside parenthesis: `\sqrt{x^2+1} - x`.
Multiply by conjugate: `(x² + 1 - x²) / (\sqrt{x^2+1} + x) = 1 / (\sqrt{x^2+1} + x)`.
Expression becomes: `x / (\sqrt{x^2+1} + x)`.
Divide numerator and denominator by `x`:
`1 / (\sqrt{1 + 1/x^2} + 1)`.
Limit: `1 / (1 + 1) =` **1/2**.
</details>

14. 🔴 $\lim_{x\to-\infty} (\sqrt{x^2 + 3x} + x)$ — *Hint: Notice it's + x, but since x → -∞, it is still ∞ - ∞ form!*
<details>
<summary>Solution</summary>

Let `t = -x`. As `x → -∞`, `t → ∞`.
Substitute `x = -t`: `\lim(t→∞) (\sqrt{(-t)^2 + 3(-t)} + (-t)) = \lim(t→∞) (\sqrt{t^2 - 3t} - t)`.
Multiply by conjugate: `((t² - 3t) - t²) / (\sqrt{t^2 - 3t} + t) = -3t / (\sqrt{t^2 - 3t} + t)`.
Divide by `t` (which is positive): `-3 / (\sqrt{1 - 3/t} + 1)`.
Limit: `-3 / (1 + 1) =` **-3/2**.
</details>

15. 🟡 $\lim_{x\to\infty} \left( \frac{x^2}{x+1} - x \right)$ — *Hint: Take common denominator.*
<details>
<summary>Solution</summary>

Common denominator: `(x² - x(x+1)) / (x+1) = (x² - x² - x) / (x+1) = -x / (x+1)`.
Limit: `\lim(x→∞) -x / (x+1)`.
Divide by `x`: `-1 / (1 + 1/x)`.
Limit: `-1 / 1 =` **-1**.
</details>

---

### Type 4: Exponential Limits at Infinity

**Goal:** Divide by the dominant exponential term. Remember $\lim_{x\to\infty} e^{-x} = 0$.

**Solved Example:**

Find $\lim_{x\to\infty} \frac{3^{x+1} - 5^x}{3^x + 5^{x+1}}$

**Solution:**
```
The dominant term is 5^x (since 5 > 3).
Divide numerator and denominator by 5^x:

= lim(x→∞) [ 3*(3^x/5^x) - (5^x/5^x) ] / [ (3^x/5^x) + 5*(5^x/5^x) ]
= lim(x→∞) [ 3*(3/5)^x - 1 ] / [ (3/5)^x + 5 ]

Since 3/5 < 1, as x → ∞, (3/5)^x → 0.
= [ 3(0) - 1 ] / [ 0 + 5 ]
= -1/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟢 $\lim_{x\to\infty} \frac{e^x + e^{-x}}{e^x - e^{-x}}$
<details>
<summary>Solution</summary>

As `x → ∞`, `e^x` is the dominant term.
Divide numerator and denominator by `e^x`:
`\lim(x→∞) (1 + e^{-2x}) / (1 - e^{-2x})`.
Since `e^{-2x} → 0`, the limit is `(1 + 0) / (1 - 0) =` **1**.
</details>

17. 🟢 $\lim_{x\to-\infty} \frac{e^x + e^{-x}}{e^x - e^{-x}}$ — *Hint: Which term dominates as x → -∞?*
<details>
<summary>Solution</summary>

As `x → -∞`, `e^{-x}` goes to `∞` and `e^x` goes to `0`. So `e^{-x}` dominates.
Divide numerator and denominator by `e^{-x}`:
`\lim(x→-∞) (e^{2x} + 1) / (e^{2x} - 1)`.
Since `e^{2x} → 0`, the limit is `(0 + 1) / (0 - 1) =` **-1**.
</details>

18. 🟡 $\lim_{x\to\infty} \frac{2^{x+2} + 3^x}{2^x - 3^{x-1}}$
<details>
<summary>Solution</summary>

The dominant term is `3^x`.
Divide numerator and denominator by `3^x`:
Numerator: `2²(2/3)^x + 1 → 4(0) + 1 = 1`.
Denominator: `(2/3)^x - 3^{-1} → 0 - 1/3 = -1/3`.
Result: `1 / (-1/3) =` **-3**.
</details>

19. 🔴 $\lim_{x\to\infty} \frac{x^2 + 2^x}{x^3 + 2^{x+1}}$ — *Hint: Use the Hierarchy of Infinity.*
<details>
<summary>Solution</summary>

By the Hierarchy of Infinity, exponential `2^x` dominates polynomials `x²` and `x³`.
Divide everything by `2^x`:
`\lim(x→∞) (x²/2^x + 1) / (x³/2^x + 2)`.
Polynomials divided by exponentials go to 0 as `x → ∞`.
Result: `(0 + 1) / (0 + 2) =` **1/2**.
</details>

20. 🟡 $\lim_{x\to\infty} \tanh x$ — *Recall $\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$*
<details>
<summary>Solution</summary>

Write as `\lim(x→∞) (e^x - e^{-x}) / (e^x + e^{-x})`.
Dominant term is `e^x`.
Divide by `e^x`: `(1 - e^{-2x}) / (1 + e^{-2x})`.
Limit is `(1 - 0) / (1 + 0) =` **1**.
</details>

---

### Type 5: Squeeze Theorem at Infinity

**Goal:** Handle oscillating functions like $\sin x$ or $\cos x$ as $x \to \infty$.

**Key Fact:** $\sin x$ and $\cos x$ never settle down as $x \to \infty$, but they are always bounded between $-1$ and $1$.

**Solved Example:**

Find $\lim_{x\to\infty} \frac{\cos x}{x}$

**Solution:**
```
We know: -1 ≤ cos x ≤ 1
Divide by x (which is positive since x → ∞):
-1/x ≤ (cos x)/x ≤ 1/x

As x → ∞, both -1/x and 1/x approach 0.
By the Squeeze Theorem, lim(x→∞) (cos x)/x = 0.
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

21. 🟢 $\lim_{x\to\infty} \frac{\sin^2 x}{x^2 + 1}$
<details>
<summary>Solution</summary>

We know `0 ≤ \sin^2 x ≤ 1`.
Divide by `x^2 + 1`: `0 ≤ (\sin^2 x)/(x^2 + 1) ≤ 1/(x^2 + 1)`.
As `x → ∞`, `1/(x^2 + 1) → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

22. 🟡 $\lim_{x\to\infty} \frac{x + \sin x}{x - \cos x}$ — *Hint: Divide numerator and denominator by x.*
<details>
<summary>Solution</summary>

Divide by `x`: `\lim(x→∞) (1 + (\sin x)/x) / (1 - (\cos x)/x)`.
Since `(\sin x)/x → 0` and `(\cos x)/x → 0` as `x → ∞` (by Squeeze Theorem).
Result: `(1 + 0) / (1 - 0) =` **1**.
</details>

23. 🟡 $\lim_{x\to\infty} e^{-x} \cos x$
<details>
<summary>Solution</summary>

Write as `(\cos x) / e^x`.
Since `-1 ≤ \cos x ≤ 1`, we have `-1/e^x ≤ (\cos x)/e^x ≤ 1/e^x`.
As `x → ∞`, `1/e^x → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

24. 🔴 $\lim_{x\to\infty} \frac{\lfloor x \rfloor}{x}$ — *Hint: $x-1 < \lfloor x \rfloor \le x$. Squeeze it!*
<details>
<summary>Solution</summary>

We know `x - 1 < \lfloor x \rfloor ≤ x`.
Divide by `x` (since `x > 0` as `x → ∞`):
`(x-1)/x < \lfloor x \rfloor/x ≤ x/x`.
`1 - 1/x < \lfloor x \rfloor/x ≤ 1`.
As `x → ∞`, `1 - 1/x → 1`. Both sides approach 1.
By Squeeze Theorem, the limit is **1**.
</details>

25. 🔴 $\lim_{x\to\infty} \frac{x^2 \sin(1/x)}{2x-1}$ — *Hint: Rewrite as $\frac{x \sin(1/x)}{2-1/x}$ and recall $\lim_{\theta\to0} \frac{\sin \theta}{\theta}$*
<details>
<summary>Solution</summary>

Let `\theta = 1/x`. As `x → ∞`, `\theta → 0`.
Substitute `x = 1/\theta`:
`\lim(\theta→0) (1/\theta^2) \sin(\theta) / (2/\theta - 1)`.
Multiply numerator and denominator by `\theta`:
`\lim(\theta→0) (\sin \theta / \theta) / (2 - \theta)`.
Since `\sin \theta / \theta → 1` and `2 - \theta → 2`.
Result: `1 / 2 =` **1/2**.
</details>

---

## Stage 4: Type Mixer

1. 🟡 $\lim_{x\to\infty} \frac{\sqrt{x^2+1} - \sqrt{x^2-1}}{x}$ *[Type 2 + Type 3]*
<details>
<summary>Solution</summary>

Divide by `x` directly (bring into square root as `x²` since `x > 0`):
`\sqrt{1 + 1/x²} - \sqrt{1 - 1/x²}`.
As `x → ∞`, `1/x² → 0`.
Limit is `\sqrt{1} - \sqrt{1} = 1 - 1 =` **0**.
</details>

2. 🔴 $\lim_{x\to-\infty} x(\sqrt{x^2+1} + x)$ *[Type 2 + Type 3 with negative infinity]*
<details>
<summary>Solution</summary>

Multiply by conjugate `(\sqrt{x^2+1} - x)`:
`x(x² + 1 - x²) / (\sqrt{x^2+1} - x) = x / (\sqrt{x^2+1} - x)`.
Divide numerator and denominator by `x` (since `x → -∞`, `x = -\sqrt{x^2}` inside the root):
`1 / (-\sqrt{1+1/x^2} - 1)`.
Limit: `1 / (-1 - 1) =` **-1/2**.
</details>

3. 🟡 $\lim_{x\to\infty} \frac{3x + \sin x}{5x + 2}$ *[Type 1 + Type 5]*
<details>
<summary>Solution</summary>

Divide by `x`:
`(3 + (\sin x)/x) / (5 + 2/x)`.
Since `(\sin x)/x → 0` by Squeeze Theorem.
Result: `(3 + 0) / (5 + 0) =` **3/5**.
</details>

4. 🔴 $\lim_{x\to\infty} \left( \sqrt{x^2 - 2x - 1} - \sqrt{x^2 - 7x + 3} \right)$ *[Type 3]*
<details>
<summary>Solution</summary>

Multiply by conjugate:
`((x² - 2x - 1) - (x² - 7x + 3)) / (\sqrt{x^2-2x-1} + \sqrt{x^2-7x+3})`.
Numerator simplifies to `5x - 4`.
Divide by `x`: `(5 - 4/x) / (\sqrt{1 - 2/x - 1/x^2} + \sqrt{1 - 7/x + 3/x^2})`.
Limit: `5 / (\sqrt{1} + \sqrt{1}) =` **5/2**.
</details>

5. 🔴 $\lim_{x\to\infty} \frac{2x^3 + 3^x}{x^4 + 3^{x-1}}$ *[Type 1 + Type 4]*
<details>
<summary>Solution</summary>

Dominant term is `3^x`. Divide everything by `3^x`.
Numerator: `2(x³/3^x) + 1 → 0 + 1 = 1`.
Denominator: `x⁴/3^x + 3^{-1} → 0 + 1/3 = 1/3`.
Result: `1 / (1/3) =` **3**.
</details>

6. 🔴 $\lim_{x\to\infty} x \tan(1/x)$ *[Trig standard limit transformed]*
<details>
<summary>Solution</summary>

Let `\theta = 1/x`. As `x → ∞`, `\theta → 0`.
Limit becomes `\lim(\theta→0) (1/\theta) \tan \theta = \lim(\theta→0) (\tan \theta)/\theta`.
By standard limit, this is **1**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Evaluate $\lim_{x\to\infty} \frac{3x^2 - 4x + 5}{2x^2 + x - 1}$ **(2 marks)**

**Solution:**
Divide numerator and denominator by x²:
= lim(x→∞) [ 3 - 4/x + 5/x² ] / [ 2 + 1/x - 1/x² ]
As x→∞, 1/x and 1/x² → 0.
= (3 - 0 + 0) / (2 + 0 - 0) = 3/2

---

**Q2.** 🟡 Evaluate $\lim_{n\to\infty} \frac{1+2+3+...+n}{n^2}$ **(3 marks)**

**Solution:**
Numerator is the sum of first n natural numbers = n(n+1)/2 = (n² + n)/2
Limit = lim(n→∞) (n² + n) / 2n²
Divide by n²:
= lim(n→∞) (1 + 1/n) / 2
As n→∞, 1/n → 0.
= (1 + 0) / 2 = 1/2

---

**Q3.** 🟡 ⭐ Evaluate $\lim_{x\to\infty} (\sqrt{x^2 + x + 1} - x)$ **(3 marks)**

**Solution:**
Multiply and divide by conjugate:
= lim(x→∞) [ (x² + x + 1) - x² ] / [ √(x² + x + 1) + x ]
= lim(x→∞) (x + 1) / [ √(x² + x + 1) + x ]
Divide top and bottom by x (which is √x² inside the root):
= lim(x→∞) (1 + 1/x) / [ √(1 + 1/x + 1/x²) + 1 ]
= (1 + 0) / (√(1+0+0) + 1) = 1/2

---

## Stage 6: JEE Mains Arena

**Q1.** $\lim_{x\to-\infty} \frac{\sqrt{4x^2 + 5x + 8}}{4x + 5}$ equals:
(a) $1/2$   <br> (b) $-1/2$   <br> (c) $1$   <br> (d) $-1$

<details>
<summary>Solution</summary>
Divide by x. Since x → -∞, x = -√x² inside the square root.
Numerator: √(4x² + 5x + 8) / x = -√(4 + 5/x + 8/x²)
Denominator: (4x + 5) / x = 4 + 5/x
Limit = lim(x→-∞) -√(4 + 0 + 0) / (4 + 0) = -2 / 4 = -1/2.
Answer: (b) 🔴 ⭐
</details>

---

**Q2.** Let $L = \lim_{x\to\infty} \left( \sqrt{x^2 + ax + a^2} - \sqrt{x^2 - ax + a^2} \right)$. Then $L$ equals:
(a) $a/2$   <br> (b) $a$   <br> (c) $2a$   <br> (d) $0$

<details>
<summary>Solution</summary>
Multiply by conjugate:
L = lim(x→∞) [ (x² + ax + a²) - (x² - ax + a²) ] / [ √(x² + ax + a²) + √(x² - ax + a²) ]
= lim(x→∞) 2ax / [ √(x² + ax + a²) + √(x² - ax + a²) ]
Divide by x:
= lim(x→∞) 2a / [ √(1 + a/x + a²/x²) + √(1 - a/x + a²/x²) ]
= 2a / (√1 + √1) = 2a / 2 = a.
Answer: (b) 🟡 ⭐
</details>

---

**Q3.** $\lim_{n\to\infty} \frac{1^2 + 2^2 + ... + n^2}{n^3}$ equals:
(a) $1/2$   <br> (b) $1/3$   <br> (c) $1/6$   <br> (d) $1$

<details>
<summary>Solution</summary>
Sum of squares = n(n+1)(2n+1)/6 = (2n³ + 3n² + n)/6.
Limit = lim(n→∞) (2n³ + 3n² + n) / (6n³)
Divide by n³:
= lim(n→∞) (2 + 3/n + 1/n²) / 6 = 2/6 = 1/3.
Answer: (b) 🟡
</details>

---

**Q4.** $\lim_{x\to\infty} \frac{e^x - e^{-x}}{e^x + e^{-x}}$ equals:
(a) $0$   <br> (b) $1$   <br> (c) $-1$   <br> (d) $\infty$

<details>
<summary>Solution</summary>
Divide by e^x (the dominant term as x→∞):
= lim(x→∞) [ 1 - e^{-2x} ] / [ 1 + e^{-2x} ]
Since e^{-2x} → 0 as x→∞:
= (1 - 0) / (1 + 0) = 1.
Answer: (b) 🟢
</details>

---

**Q5.** If $\lim_{x\to\infty} \left( \frac{x^2 - 1}{x + 1} - ax - b \right) = 2$, then:
(a) $a = 1, b = -3$   <br> (b) $a = 1, b = 2$   <br> (c) $a = 0, b = -2$   <br> (d) $a = 2, b = -1$

<details>
<summary>Solution</summary>
Simplify the fraction: (x² - 1)/(x + 1) = x - 1  (for x ≠ -1)
Limit = lim(x→∞) (x - 1 - ax - b) = lim(x→∞) [ x(1 - a) - (1 + b) ]
For the limit to be a finite number (2), the coefficient of x must be 0, otherwise it would blow up to ±∞.
So, 1 - a = 0 ⟹ a = 1.
Then the limit is simply -(1 + b) = 2.
-1 - b = 2 ⟹ b = -3.
Answer: (a) 🔴 ⭐
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
<br> **Assertion (A):** $\lim_{x\to\infty} \frac{\sin x}{x} = 0$<br>
<br> **Reason (R):** $\lim_{x\to\infty} \sin x = 0$

<details>
<summary>Solution</summary>
A is true: Bounded function divided by infinity gives 0 (Squeeze Theorem).
R is false: lim(x→∞) sin x does not exist; it oscillates between -1 and 1.
Answer: (c) 🟡 ⭐
</details>

---

**Q2.**
<br> **Assertion (A):** $\lim_{x\to-\infty} \frac{\sqrt{x^2+1}}{x} = -1$<br>
<br> **Reason (R):** For $x < 0$, $\sqrt{x^2} = -x$.

<details>
<summary>Solution</summary>
A is true: Divide numerator and denominator by x. For the numerator, we divide the inside of the root by x², but add a negative sign outside because x is negative. Result is -1.
R is true and is the exact algebraic justification.
Answer: (a) 🔴
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 $\lim_{x\to\infty} \frac{5x^2 - 3x}{2x^2 + 1} =$
   <br> (a) $5/2$   <br> (b) $0$   <br> (c) $\infty$   <br> (d) $2/5$

2. 🟢 $\lim_{x\to\infty} \frac{x^3 + 1}{x^4 + x^2} =$
   <br> (a) $1$   <br> (b) $0$   <br> (c) $\infty$   <br> (d) Does not exist

3. 🟡 ⭐ $\lim_{x\to-\infty} \frac{x}{\sqrt{x^2 + 1}} =$
   <br> (a) $1$   <br> (b) $-1$   <br> (c) $0$   <br> (d) Does not exist

4. 🟡 $\lim_{x\to\infty} (\sqrt{x+1} - \sqrt{x}) =$
   <br> (a) $1/2$   <br> (b) $1$   <br> (c) $0$   <br> (d) $\infty$

5. 🟡 $\lim_{x\to\infty} \frac{3^x + 4^x}{3^x - 4^x} =$
   <br> (a) $1$   <br> (b) $-1$   <br> (c) $0$   <br> (d) $\infty$

6. 🔴 $\lim_{x\to-\infty} \frac{3^x + 4^x}{3^x - 4^x} =$
   <br> (a) $1$   <br> (b) $-1$   <br> (c) $0$   <br> (d) $\infty$
   *(Hint: As $x \to -\infty$, $4^x \to 0$ and $3^x \to 0$. Which one goes to 0 slower?)*

7. 🟡 ⭐ $\lim_{n\to\infty} \frac{1+3+5+...+(2n-1)}{n^2} =$
   <br> (a) $1$   <br> (b) $1/2$   <br> (c) $2$   <br> (d) $0$

8. 🟡 $\lim_{x\to\infty} \frac{\cos 2x}{3x} =$
   <br> (a) $2/3$   <br> (b) $\infty$   <br> (c) $0$   <br> (d) Does not exist

9. 🔴 $\lim_{x\to\infty} x \left( \sqrt{x^2 + 1} - x \right) =$
   <br> (a) $1/2$   <br> (b) $1$   <br> (c) $0$   <br> (d) $\infty$

10. 🟡 $\lim_{x\to\infty} \frac{2x^2 + \sin x}{x^2 + \cos x} =$
    <br> (a) $2$   <br> (b) $1$   <br> (c) $0$   <br> (d) $\infty$

11. 🔴 ⭐ $\lim_{x\to\infty} \left( \sqrt{x^2 - 5x + 6} - x \right) =$
    <br> (a) $5/2$   <br> (b) $-5/2$   <br> (c) $5$   <br> (d) $0$

12. 🟡 $\lim_{x\to\infty} \frac{\ln x}{x} =$
    <br> (a) $1$   <br> (b) $0$   <br> (c) $\infty$   <br> (d) $e$

13. 🔴 $\lim_{x\to\infty} \frac{e^x + x^2}{e^{x+1} + x} =$
    <br> (a) $1$   <br> (b) $e$   <br> (c) $1/e$   <br> (d) $\infty$

14. 🟡 $\lim_{n\to\infty} \frac{n!}{(n+1)! - n!} =$
    <br> (a) $1$   <br> (b) $0$   <br> (c) $\infty$   <br> (d) $1/2$

15. 🔴 If $\lim_{x\to\infty} \frac{ax^2 + bx + 1}{x + 1} = 3$, then:
    <br> (a) $a=3, b=0$   <br> (b) $a=0, b=3$   <br> (c) $a=0, b=1$   <br> (d) Limit is impossible

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| 1 | a | 6 | a | 11 | b |
| 2 | b | 7 | a | 12 | b |
| 3 | b | 8 | c | 13 | c |
| 4 | c | 9 | a | 14 | b |
| 5 | b | 10 | a | 15 | b |

</details>

---

## What's Next?

You have officially conquered the three main branches of limits:
1. $x \to a$ ($0/0$ form with algebra)
2. Standard Limits (Trig, Exp, Log, $1^\infty$)
3. $x \to \infty$ (Dominance and Rationalization)

Now, we bring these tools to life. What was the point of evaluating all these $0/0$ limits? 

In **Chapter 4**, we'll return to the very first example we talked about: the speedometer. We'll use our limit skills to find the exact, instantaneous rate of change of any function. Welcome to the **Derivative from First Principles**.

**Key takeaway from Chapter 3:** Infinity is a battleground. The fastest-growing term dictates the outcome. And always respect the negative sign when $x \to -\infty$ goes inside a square root!
