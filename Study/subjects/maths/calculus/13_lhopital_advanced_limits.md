# Chapter 13: L'Hôpital's Rule & Advanced Limit Problems

---

## Stage 1: The Core Idea

### The Shortcut for Indeterminate Forms

In Chapters 1 and 2, you evaluated limits in $0/0$ form using factoring, rationalizing, and standard limit formulas. But what about $\lim_{x\to0} \frac{x - \sin x}{x^3}$? Factoring fails. Standard limits don't directly apply. The expansion method works, but it's long.

**L'Hôpital's Rule** gives an elegant shortcut:
> If $\lim_{x\to a} \frac{f(x)}{g(x)}$ is $\frac{0}{0}$ or $\frac{\infty}{\infty}$, then:
> $$\lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}$$
> **(provided the right-hand limit exists)**

In other words: **differentiate the top and bottom separately** (not as a quotient!), then try the limit again.

### The Critical Distinction

> ⚠️ **L'Hôpital's Rule is NOT the Quotient Rule.**

You do NOT use the quotient rule here. You differentiate $f(x)$ separately and $g(x)$ separately, then form a new fraction.

---

## Stage 2: The Formula Lab

### When to Apply L'Hôpital's Rule

| Indeterminate Form | How to Convert to $0/0$ or $\infty/\infty$ |
|-------------------|-------------------------------------------|
| $0/0$ | Apply directly |
| $\infty/\infty$ | Apply directly |
| $0 \cdot \infty$ | Rewrite as $\frac{0}{1/\infty} = \frac{0}{0}$ or $\frac{\infty}{1/0} = \frac{\infty}{\infty}$ |
| $\infty - \infty$ | Combine fractions or rationalize to get $0/0$ |
| $1^\infty$ | Write $y = f^g$, take $\ln$: $\ln y = g\ln f \to 0 \cdot \infty$, then convert |
| $0^0$ | Same as $1^\infty$: take $\ln$ |
| $\infty^0$ | Same as $1^\infty$: take $\ln$ |

### When NOT to Use L'Hôpital's Rule

| Situation | Reason |
|-----------|--------|
| $\lim_{x\to0} \frac{x+1}{x^2+1}$ gives $1/1$ | NOT indeterminate — just substitute directly! |
| Result doesn't simplify | Sometimes it's an infinite loop — use expansion instead |
| $\lim_{x\to\infty} \frac{x+\sin x}{x}$ | L'Hôpital gives $\frac{1+\cos x}{1}$ which oscillates — wrong to apply here. Use algebra: $1 + \sin(x)/x = 1+0 = 1$. |

---

## Stage 3: Type-wise Mastery

### Type 1: Direct Application — $0/0$ Form

**Goal:** Apply L'Hôpital once (or a few times until the form resolves).

**Solved Example:** ⭐

Find $\lim_{x\to0} \frac{x - \sin x}{x^3}$.

**Solution:**
```
Direct substitution: 0/0. Apply L'Hôpital:
= lim(x→0) (1 - cos x) / (3x²)     → still 0/0.

Apply again:
= lim(x→0) sin x / (6x)     → 0/0 still.

Apply again:
= lim(x→0) cos x / 6 = 1/6
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

1. 🟢 $\lim_{x\to0} \frac{e^x - 1}{x}$
<details>
<summary>Solution</summary>

Form: `0/0`. Apply L'Hôpital:
`= \lim_{x\to0} \frac{e^x}{1} = e^0 =` **1**.
</details>

2. 🟡 $\lim_{x\to0} \frac{\sin x - x\cos x}{x^3}$
<details>
<summary>Solution</summary>

Form: `0/0`. Apply L'Hôpital:
`= \lim_{x\to0} \frac{\cos x - (\cos x - x\sin x)}{3x^2} = \lim_{x\to0} \frac{x\sin x}{3x^2} = \lim_{x\to0} \frac{\sin x}{3x}`.
Form: `0/0`. Apply L'Hôpital again (or use standard limit `(\sin x)/x \to 1`):
`= \frac{1}{3} \cdot 1 =` **\frac{1}{3}**.
</details>

3. 🟡 $\lim_{x\to0} \frac{\ln(1+x)}{x}$
<details>
<summary>Solution</summary>

Form: `0/0`. Apply L'Hôpital:
`= \lim_{x\to0} \frac{1/(1+x)}{1} = \frac{1}{1+0} =` **1**.
</details>

4. 🔴 $\lim_{x\to0} \frac{x - \tan^{-1}x}{x^3}$
<details>
<summary>Solution</summary>

Form: `0/0`. Apply L'Hôpital:
`= \lim_{x\to0} \frac{1 - 1/(1+x^2)}{3x^2} = \lim_{x\to0} \frac{\frac{1+x^2-1}{1+x^2}}{3x^2} = \lim_{x\to0} \frac{x^2}{3x^2(1+x^2)}`.
Cancel `x^2`:
`= \lim_{x\to0} \frac{1}{3(1+x^2)} = \frac{1}{3(1+0)} =` **\frac{1}{3}**.
</details>

5. 🔴 $\lim_{x\to1} \frac{x^x - x}{x - 1 - \ln x}$
<details>
<summary>Solution</summary>

Form: `0/0`. `\frac{d}{dx}(x^x) = x^x(1+\ln x)`. Apply L'Hôpital:
`= \lim_{x\to1} \frac{x^x(1+\ln x) - 1}{1 - 0 - 1/x} = \lim_{x\to1} \frac{x^x(1+\ln x) - 1}{1 - 1/x}`.
At `x=1`, Num = `1(1+0)-1 = 0`, Den = `1-1 = 0`. Form `0/0` again.
Apply L'Hôpital again. Numerator derivative:
`\frac{d}{dx}[x^x(1+\ln x)] = x^x(1+\ln x) \cdot (1+\ln x) + x^x \cdot \frac{1}{x} = x^x[(1+\ln x)^2 + 1/x]`.
Denominator derivative: `1/x^2`.
`= \lim_{x\to1} \frac{x^x[(1+\ln x)^2 + 1/x]}{1/x^2} = \frac{1 \cdot [1^2 + 1]}{1} = \frac{2}{1} =` **2**.
</details>

---

### Type 2: $\infty/\infty$ Form

**Goal:** Apply L'Hôpital to resolve infinite-over-infinite forms.

**Solved Example:** ⭐

Find $\lim_{x\to\infty} \frac{\ln x}{x}$.

**Solution:**
```
Direct substitution: ∞/∞. Apply L'Hôpital:
= lim(x→∞) (1/x) / 1 = lim(x→∞) 1/x = 0
```
🟢 Easy ⭐ Must-Do

This confirms the hierarchy $\ln x \ll x$ from Chapter 3.

**Practice Problems:**

6. 🟢 $\lim_{x\to\infty} \frac{x^2}{e^x}$
<details>
<summary>Solution</summary>

Form: `\infty/\infty`. Apply L'Hôpital:
`= \lim_{x\to\infty} \frac{2x}{e^x}`. (Still `\infty/\infty`).
Apply again: `= \lim_{x\to\infty} \frac{2}{e^x} =` **0**.
</details>

7. 🟡 $\lim_{x\to\infty} \frac{x^n}{e^x}$ for any fixed $n$
<details>
<summary>Solution</summary>

Form: `\infty/\infty`. Applying L'Hôpital `n` times will differentiate `x^n` down to a constant `n!`.
The denominator will remain `e^x`.
`= \lim_{x\to\infty} \frac{n!}{e^x} =` **0**. (This proves exponentials always beat polynomials).
</details>

8. 🟡 $\lim_{x\to\infty} \frac{\ln^2 x}{x}$
<details>
<summary>Solution</summary>

Form: `\infty/\infty`. Apply L'Hôpital:
`= \lim_{x\to\infty} \frac{2(\ln x)(1/x)}{1} = \lim_{x\to\infty} \frac{2\ln x}{x}`. (Still `\infty/\infty`).
Apply again: `= \lim_{x\to\infty} \frac{2/x}{1} = \lim_{x\to\infty} \frac{2}{x} =` **0**.
</details>

9. 🔴 $\lim_{x\to\infty} \frac{e^x}{x^{100}}$ — *Apply 100 times, or recognize the pattern.*
<details>
<summary>Solution</summary>

Form: `\infty/\infty`. Applying L'Hôpital 100 times differentiates the denominator to a constant `100!`.
The numerator remains `e^x`.
`= \lim_{x\to\infty} \frac{e^x}{100!} =` **\infty**. (This proves exponentials always beat polynomials).
</details>

10. 🟡 $\lim_{x\to0^+} \frac{\ln x}{\cot x}$
<details>
<summary>Solution</summary>

Form: `-\infty/\infty`. Apply L'Hôpital:
`= \lim_{x\to0^+} \frac{1/x}{-\csc^2 x} = \lim_{x\to0^+} \frac{-\sin^2 x}{x}`.
`= -\lim_{x\to0^+} (\sin x) \cdot \left(\frac{\sin x}{x}\right) = -0 \cdot 1 =` **0**.
</details>

---

### Type 3: $0 \cdot \infty$ Form

**Goal:** Rewrite as a fraction and apply L'Hôpital.

**Solved Example:** ⭐

Find $\lim_{x\to0^+} x \ln x$.

**Solution:**
```
Form: 0 · (-∞). Rewrite:
= lim(x→0⁺) ln x / (1/x)     [now ∞/∞]
Apply L'Hôpital:
= lim(x→0⁺) (1/x) / (-1/x²)
= lim(x→0⁺) (1/x) · (-x²)
= lim(x→0⁺) (-x) = 0
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

11. 🟡 $\lim_{x\to0^+} x^2 \ln x$
<details>
<summary>Solution</summary>

Rewrite as `\infty/\infty`: `\lim_{x\to0^+} \frac{\ln x}{1/x^2}`.
Apply L'Hôpital:
`= \lim_{x\to0^+} \frac{1/x}{-2/x^3} = \lim_{x\to0^+} \frac{-x^2}{2} =` **0**.
</details>

12. 🟡 $\lim_{x\to\infty} x \sin(1/x)$
<details>
<summary>Solution</summary>

Rewrite as `0/0`: `\lim_{x\to\infty} \frac{\sin(1/x)}{1/x}`.
Apply L'Hôpital (or use standard limit `\sin u / u \to 1` as `u=1/x \to 0`):
`= \lim_{x\to\infty} \frac{\cos(1/x) \cdot (-1/x^2)}{-1/x^2} = \lim_{x\to\infty} \cos(1/x) = \cos(0) =` **1**.
</details>

13. 🔴 $\lim_{x\to0^+} \sqrt{x} \ln x$
<details>
<summary>Solution</summary>

Rewrite as `\infty/\infty`: `\lim_{x\to0^+} \frac{\ln x}{x^{-1/2}}`.
Apply L'Hôpital:
`= \lim_{x\to0^+} \frac{1/x}{-\frac{1}{2}x^{-3/2}} = \lim_{x\to0^+} (-2 x^{1/2}) = -2\sqrt{0} =` **0**.
</details>

14. 🔴 $\lim_{x\to\pi/2} (x - \pi/2)\tan x$
<details>
<summary>Solution</summary>

Rewrite as `0/0`: `\lim_{x\to\pi/2} \frac{x - \pi/2}{\cot x}`.
Apply L'Hôpital:
`= \lim_{x\to\pi/2} \frac{1}{-\csc^2 x} = \frac{1}{-\csc^2(\pi/2)} = \frac{1}{-1} =` **-1**.
</details>

15. 🔴 $\lim_{x\to0^+} (\cos x)^{1/x^2}$ — *This is $1^\infty$, use ln trick first.*
<details>
<summary>Solution</summary>

Let `y = (\cos x)^{1/x^2}`. `\ln y = \frac{\ln(\cos x)}{x^2}` (Form `0/0`).
Apply L'Hôpital to `\ln y`:
`\lim_{x\to0} \frac{\frac{1}{\cos x}(-\sin x)}{2x} = \lim_{x\to0} \frac{-\tan x}{2x} = -\frac{1}{2} \lim_{x\to0} \frac{\tan x}{x} = -\frac{1}{2}(1) = -\frac{1}{2}`.
Since `\ln y \to -1/2`, `y \to` **e^{-1/2}**.
</details>

---

### Type 4: $\infty - \infty$ Form

**Goal:** Combine into a single fraction to get $0/0$ or $\infty/\infty$.

**Solved Example:** ⭐

Find $\lim_{x\to0} \left(\frac{1}{x} - \frac{1}{\sin x}\right)$.

**Solution:**
```
Form: ∞ - ∞. Combine:
= lim(x→0) (sin x - x)/(x sin x)     [0/0 now]

Apply L'Hôpital:
= lim(x→0) (cos x - 1)/(sin x + x cos x)     [still 0/0]

Apply again:
= lim(x→0) (-sin x)/(cos x + cos x - x sin x)
= (-0)/(1 + 1 - 0) = 0
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

16. 🟡 $\lim_{x\to0}\left(\frac{1}{x^2} - \cot^2 x\right)$
<details>
<summary>Solution</summary>

Combine fractions: `\lim_{x\to0} \left(\frac{1}{x^2} - \frac{\cos^2 x}{\sin^2 x}\right) = \lim_{x\to0} \frac{\sin^2 x - x^2\cos^2 x}{x^2\sin^2 x}`.
Using series expansions is much faster here: `\sin x \approx x - x^3/6 \implies \sin^2 x \approx x^2 - x^4/3`.
`x^2\cos^2 x \approx x^2(1-x^2/2)^2 \approx x^2(1 - x^2) = x^2 - x^4`.
Numerator: `(x^2 - x^4/3) - (x^2 - x^4) = \frac{2x^4}{3}`.
Denominator: `x^2(x^2) = x^4` (since `\sin^2 x \approx x^2`).
Limit = `\lim_{x\to0} \frac{2x^4/3}{x^4} =` **\frac{2}{3}**.
</details>

17. 🟡 $\lim_{x\to1}\left(\frac{x}{x-1} - \frac{1}{\ln x}\right)$
<details>
<summary>Solution</summary>

Combine: `\lim_{x\to1} \frac{x\ln x - x + 1}{(x-1)\ln x}` (Form `0/0`).
Apply L'Hôpital:
Num': `\ln x + x(1/x) - 1 = \ln x`.
Den': `1\cdot\ln x + (x-1)(1/x) = \ln x + 1 - 1/x`.
Limit = `\lim_{x\to1} \frac{\ln x}{\ln x + 1 - 1/x}` (Still `0/0`).
Apply L'Hôpital again:
Num'': `1/x`.
Den'': `1/x + 1/x^2`.
Limit = `\lim_{x\to1} \frac{1/x}{1/x + 1/x^2} = \frac{1}{1+1} =` **\frac{1}{2}**.
</details>

18. 🔴 $\lim_{x\to0}\left(\frac{1}{\sin x} - \frac{1}{\tan x}\right)$
<details>
<summary>Solution</summary>

Combine: `\lim_{x\to0} \left(\frac{1}{\sin x} - \frac{\cos x}{\sin x}\right) = \lim_{x\to0} \frac{1-\cos x}{\sin x}`.
Apply L'Hôpital:
`= \lim_{x\to0} \frac{\sin x}{\cos x} = \frac{0}{1} =` **0**.
</details>

19. 🔴 $\lim_{x\to\infty}(\sqrt{x^2+x} - x)$ — *Use algebraic method here, not L'Hôpital.*
<details>
<summary>Solution</summary>

Rationalize by multiplying by conjugate:
`\lim_{x\to\infty} \frac{(\sqrt{x^2+x} - x)(\sqrt{x^2+x} + x)}{\sqrt{x^2+x} + x} = \lim_{x\to\infty} \frac{(x^2+x) - x^2}{\sqrt{x^2+x} + x}`.
`= \lim_{x\to\infty} \frac{x}{\sqrt{x^2(1+1/x)} + x} = \lim_{x\to\infty} \frac{x}{x\sqrt{1+1/x} + x}`.
Divide by `x`:
`= \lim_{x\to\infty} \frac{1}{\sqrt{1+1/x} + 1} = \frac{1}{\sqrt{1+0} + 1} =` **\frac{1}{2}**.
</details>

20. 🔴 $\lim_{x\to0}\left(\csc x - \cot x\right)^2$
<details>
<summary>Solution</summary>

Note that `\csc x - \cot x = \frac{1}{\sin x} - \frac{1}{\tan x}`.
From Q18, we know `\lim_{x\to0} (\csc x - \cot x) = 0`.
So the limit of the square is `0^2 =` **0**.
</details>

---

### Type 5: $0^0$, $\infty^0$, $1^\infty$ Forms

**Goal:** Take $\ln$ of the expression to convert to $0/0$ or $\infty/\infty$.

**Solved Example:** ⭐

Find $\lim_{x\to0^+} x^x$.

**Solution:**
```
Form: 0^0. Let y = x^x. Take ln:
ln y = x ln x     [form 0·(-∞)]

From Type 3: lim(x→0⁺) x ln x = 0.
So lim(ln y) = 0.
Therefore: lim y = e^0 = 1.
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

21. 🟡 $\lim_{x\to\infty} x^{1/x}$ — $(\infty^0$ form$)$
<details>
<summary>Solution</summary>

Let `y = x^{1/x}`. Then `\ln y = \frac{1}{x}\ln x = \frac{\ln x}{x}`.
`\lim_{x\to\infty} \frac{\ln x}{x} = 0` (from Type 2, Q92).
So `\lim (\ln y) = 0 \implies \lim y = e^0 =` **1**.
</details>

22. 🟡 $\lim_{x\to0^+} (1+x)^{1/x}$ — $(1^\infty$ — but also equals $e$ via standard limit$)$
<details>
<summary>Solution</summary>

Let `y = (1+x)^{1/x}`. Then `\ln y = \frac{\ln(1+x)}{x}` (Form `0/0`).
Apply L'Hôpital: `\lim_{x\to0} \frac{1/(1+x)}{1} = 1`.
So `\lim (\ln y) = 1 \implies \lim y = e^1 =` **e**.
</details>

23. 🔴 $\lim_{x\to0^+} (\sin x)^{\tan x}$
<details>
<summary>Solution</summary>

Form: `0^0`. Let `y = (\sin x)^{\tan x}`.
`\ln y = \tan x \ln(\sin x) = \frac{\ln(\sin x)}{\cot x}` (Form `-\infty/\infty`).
Apply L'Hôpital:
`\lim_{x\to0^+} \frac{\frac{\cos x}{\sin x}}{-\csc^2 x} = \lim_{x\to0^+} (-\cos x \cdot \sin x) = 0`.
So `\lim (\ln y) = 0 \implies \lim y = e^0 =` **1**.
</details>

24. 🔴 $\lim_{x\to0^+} \left(\frac{1}{x}\right)^{\sin x}$ — $(\infty^0$ form$)$
<details>
<summary>Solution</summary>

Let `y = (1/x)^{\sin x}`.
`\ln y = \sin x \ln(1/x) = -\sin x \ln x`.
Rewrite: `= -\frac{\sin x}{x} (x \ln x)`.
We know `\lim_{x\to0} \frac{\sin x}{x} = 1` and `\lim_{x\to0^+} x \ln x = 0`.
So `\lim (\ln y) = -1 \cdot 0 = 0 \implies \lim y = e^0 =` **1**.
</details>

25. 🔴 ⭐ $\lim_{x\to1} x^{1/(1-x)}$
<details>
<summary>Solution</summary>

Form: `1^\infty`. Let `y = x^{1/(1-x)}`.
`\ln y = \frac{\ln x}{1-x}` (Form `0/0`).
Apply L'Hôpital:
`\lim_{x\to1} \frac{1/x}{-1} = -1`.
So `\lim (\ln y) = -1 \implies \lim y =` **1/e**.
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ $\lim_{x\to0} \frac{(1+x)^{1/x} - e}{x}$
<details>
<summary>Solution</summary>

Let `f(x) = (1+x)^{1/x} = e^{\frac{1}{x}\ln(1+x)}`. We want `\lim_{x\to0} \frac{f(x)-e}{x}` (Form `0/0`).
Apply L'Hôpital: `= \lim_{x\to0} f'(x)`.
`f'(x) = f(x) \cdot \frac{d}{dx}\left[ \frac{\ln(1+x)}{x} \right] = f(x) \left[ \frac{\frac{x}{1+x} - \ln(1+x)}{x^2} \right] = f(x) \left[ \frac{x - (1+x)\ln(1+x)}{x^2(1+x)} \right]`.
As `x \to 0`, `f(x) \to e`. We need the limit of the bracket (Form `0/0`).
L'H on bracket: `\frac{1 - [1\cdot\ln(1+x) + (1+x)\frac{1}{1+x}]}{2x + 3x^2} = \frac{1 - \ln(1+x) - 1}{2x + 3x^2} = \frac{-\ln(1+x)}{2x+3x^2}` (Form `0/0`).
L'H again: `\frac{-\frac{1}{1+x}}{2+6x} \to \frac{-1}{2}` as `x \to 0`.
Limit = `e \cdot (-1/2) =` **-e/2**.
</details>

2. 🔴 $\lim_{x\to0^+} (\sin x)^x + x^{\sin x}$
<details>
<summary>Solution</summary>

Let `L_1 = \lim_{x\to0^+} (\sin x)^x`. `\ln L_1 = \lim x\ln(\sin x) = \lim \frac{\ln(\sin x)}{1/x} \xrightarrow{L'H} \lim \frac{\cot x}{-1/x^2} = \lim (-x\cos x)\frac{x}{\sin x} = 0 \cdot 1 = 0 \implies L_1 = e^0 = 1`.
Let `L_2 = \lim_{x\to0^+} x^{\sin x}`. `\ln L_2 = \lim \sin x \ln x = \lim \frac{\ln x}{\csc x} \xrightarrow{L'H} \lim \frac{1/x}{-\csc x\cot x} = \lim -\frac{\sin x}{x}\tan x = -1 \cdot 0 = 0 \implies L_2 = e^0 = 1`.
Limit = `L_1 + L_2 = 1 + 1 =` **2**.
</details>

3. 🔴 $\lim_{x\to\infty} \left(\frac{x+2}{x-1}\right)^x$
<details>
<summary>Solution</summary>

Rewrite the base: `\frac{x+2}{x-1} = 1 + \frac{3}{x-1}`.
Form is `1^\infty`. Use standard limit `\lim (1 + 1/u)^u = e`:
`= \lim_{x\to\infty} \left[ \left(1 + \frac{3}{x-1}\right)^{\frac{x-1}{3}} \right]^{\frac{3x}{x-1}}`.
The inner part goes to `e`.
The exponent `\frac{3x}{x-1} \to 3` as `x \to \infty`.
Limit = **e^3**.
</details>

4. 🔴 $\lim_{x\to0} \frac{x^2\sin(1/x)}{\tan x}$ — *Careful! Is L'Hôpital even applicable?*
<details>
<summary>Solution</summary>

Do **not** use L'Hôpital's rule. Differentiating the numerator produces a `\cos(1/x)` term which does not have a limit at 0 (it oscillates).
Instead, use basic limit properties:
`= \lim_{x\to0} \left( \frac{x}{\tan x} \cdot x\sin(1/x) \right)`.
We know `\lim \frac{x}{\tan x} = 1`.
And `x\sin(1/x) \to 0 \times (\text{bounded value between -1 and 1}) = 0` (Squeeze Theorem).
Limit = `1 \cdot 0 =` **0**.
</details>

5. 🔴 $\lim_{x\to0} \left(\frac{1}{\sin^2 x} - \frac{1}{x^2}\right)$
<details>
<summary>Solution</summary>

Combine: `\lim_{x\to0} \frac{x^2 - \sin^2 x}{x^2\sin^2 x}`.
Using Taylor series is easiest here: `\sin x \approx x - x^3/6 \implies \sin^2 x \approx x^2 - x^4/3`.
Numerator: `x^2 - (x^2 - x^4/3) = x^4/3`.
Denominator: `x^2(x^2) = x^4`.
Limit = `\lim_{x\to0} \frac{x^4/3}{x^4} =` **1/3**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Evaluate $\lim_{x\to0} \frac{e^x + e^{-x} - 2}{x^2}$ using L'Hôpital's rule. **(3 marks)**

**Solution:**
$0/0$ form.
$= \lim \frac{e^x - e^{-x}}{2x}$ → $0/0$ again.
$= \lim \frac{e^x + e^{-x}}{2} = \frac{1+1}{2} = 1$.

---

**Q2.** 🔴 Evaluate $\lim_{x\to0^+} x^{\sin x}$. **(4 marks)**

**Solution:**
Let $y = x^{\sin x}$. $\ln y = \sin x \cdot \ln x$.
$\lim_{x\to0^+} \sin x \cdot \ln x = \lim_{x\to0^+} \frac{\ln x}{1/\sin x} = \lim \frac{1/x}{-\cos x/\sin^2 x} = \lim \frac{-\sin^2 x}{x\cos x}$
$= \lim \frac{-\sin x \cdot \sin x/x}{\cos x} = \frac{-0 \cdot 1}{1} = 0$.
$\therefore \lim y = e^0 = 1$.

---

## Stage 6: JEE Mains Arena

**Q1.** $\lim_{x\to0} \frac{\tan x - \sin x}{x^3}$ using L'Hôpital's:
<br>(a) $1/3$   <br>(b) $1/2$   <br>(c) $1$   <br>(d) $0$

<details>
<summary>Solution</summary>
Apply L'Hôpital 3 times (0/0 each time):
= lim (sec²x - cos x)/(3x²) → (1-1)/0 = 0/0 still
= lim (2sec²x tan x + sin x)/(6x) → 0/0
= lim (2·2sec²x·tan²x + 2sec⁴x + cos x)/6 at x=0
= (0 + 2 + 1)/6 = 3/6 = 1/2.
Answer: (b) 🔴 ⭐
</details>

---

**Q2.** $\lim_{x\to1} \frac{x^x - x}{x\ln x - x + 1}$ equals:
<br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) Does not exist

<details>
<summary>Solution</summary>
Both numerator and denominator = 0 at x=1. Apply L'Hôpital:
Numerator: d/dx(x^x - x) = x^x(1+ln x) - 1
Denominator: d/dx(x ln x - x + 1) = ln x + 1 - 1 = ln x

At x=1: Numerator = 1(1+0)-1 = 0. Denominator = 0. Still 0/0!
Apply again: Num'' = d/dx[x^x(1+ln x) - 1] = (1+ln x)² x^x + x^x/x = x^x[(1+ln x)² + 1/x]
Den'' = 1/x.
At x=1: Num'' = 1[(1)² + 1] = 2. Den'' = 1.
Limit = 2/1 = 2.
Answer: (c) 🔴 ⭐
</details>

---

**Q3.** $\lim_{x\to0} \left(\frac{a^x + b^x + c^x}{3}\right)^{2/x}$ equals:
<br>(a) $abc$   <br>(b) $(abc)^{2/3}$   <br>(c) $a+b+c$   <br>(d) $e^{a+b+c}$

<details>
<summary>Solution</summary>
This is 1^∞ form (at x=0, base = (a^0+b^0+c^0)/3 = 1).
Let y = [(a^x+b^x+c^x)/3]^{2/x}
ln y = (2/x)·ln[(a^x+b^x+c^x)/3] → 0·... form as x→0

Apply L'Hôpital to lim(x→0) 2ln[(a^x+b^x+c^x)/3]/x:
Numerator derivative: 2(a^x ln a + b^x ln b + c^x ln c)/(a^x+b^x+c^x)
At x=0: 2(ln a + ln b + ln c)/3 = (2/3)ln(abc)

So ln y → (2/3)ln(abc) = ln((abc)^{2/3}).
y = (abc)^{2/3}.
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** $\lim_{x\to0} \frac{x+\sin x}{x-\sin x}$ cannot be found using L'Hôpital's rule.
<br>**Reason (R):** The limit is not of $0/0$ or $\infty/\infty$ form.

<details>
<summary>Solution</summary>
A is false: Substitution gives 0/0 (both num and den → 0). L'Hôpital CAN be applied.
R is false: It IS in 0/0 form.
Answer: (d) — Both false. 🟡
</details>

---

**Q2.**
<br>**Assertion (A):** $\lim_{x\to\infty} \frac{x+\sin x}{x}$ should NOT be computed using L'Hôpital's rule.
<br>**Reason (R):** Applying L'Hôpital gives $\frac{1+\cos x}{1}$, which does not have a limit (oscillates). But dividing by $x$ shows the limit is 1.

<details>
<summary>Solution</summary>
A is true: L'Hôpital fails here because the derivative-ratio limit doesn't exist (cos x oscillates).
R is true and gives both the failure mode and the correct method.
Answer: (a) 🔴 ⭐
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 L'Hôpital's rule applies when the limit is of the form:
   <br>(a) Any fraction   <br>(b) $0/0$ or $\infty/\infty$ only   <br>(c) $0/\infty$ only   <br>(d) Any limit equal to 0

2. 🟡 $\lim_{x\to0} \frac{\ln(1+x^2)}{x^2} =$
   <br>(a) $0$   <br>(b) $1$   <br>(c) $\infty$   <br>(d) $1/2$

3. 🟡 ⭐ $\lim_{x\to0^+} x^x =$
   <br>(a) $0$   <br>(b) $1$   <br>(c) $e$   <br>(d) $\infty$

4. 🟡 $\lim_{x\to\infty} \frac{x^3}{e^x} =$
   <br>(a) $\infty$   <br>(b) $3$   <br>(c) $1$   <br>(d) $0$

5. 🔴 ⭐ $\lim_{x\to0} \frac{x - \sin x}{x^3} =$
   <br>(a) $0$   <br>(b) $1/3$   <br>(c) $1/6$   <br>(d) $1/2$

6. 🟡 $\lim_{x\to1} x^{1/(1-x)} =$
   <br>(a) $0$   <br>(b) $e$   <br>(c) $1/e$   <br>(d) $\infty$

7. 🔴 $\lim_{x\to0} \frac{1 - \cos x}{x\sin x} =$
   <br>(a) $0$   <br>(b) $1/2$   <br>(c) $1$   <br>(d) $2$

8. 🔴 ⭐ $\lim_{x\to0} \left(\frac{1}{x} - \frac{1}{e^x - 1}\right) =$
   <br>(a) $0$   <br>(b) $1$   <br>(c) $1/2$   <br>(d) $-1/2$

9. 🔴 $\lim_{x\to\infty} \frac{\ln x}{\sqrt{x}} =$
   <br>(a) $0$   <br>(b) $1$   <br>(c) $2$   <br>(d) $\infty$

10. 🟡 Which of the following is NOT an indeterminate form?
    <br>(a) $1^\infty$   <br>(b) $0/0$   <br>(c) $1/0$   <br>(d) $\infty - \infty$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | b | 6 | c |
| 2 | b | 7 | b |
| 3 | b | 8 | c |
| 4 | d | 9 | a |
| 5 | c | 10 | c |

</details>

---

## Congratulations! 🎉

You have completed the **Continuity & Differentiation Mastery Book**!

### What You've Mastered:

**Part I — Limits (Class 11):**
- Ch 1: Intuitive Limits — LHL, RHL, 0/0, Squeeze
- Ch 2: Standard Limits — Trig, Exp, Log, 1^∞
- Ch 3: Limits at Infinity — Dominant terms, Rationalization
- Ch 4: Derivative from First Principles — The limit definition
- Ch 5: Rules of Differentiation — Power, Product, Quotient
- Ch 6: Chain Rule — Composite function differentiation

**Part II — Continuity & Differentiability (Class 12):**
- Ch 7: Continuity — 3 conditions, types of discontinuity, IVT
- Ch 8: Differentiability — LHD/RHD, piecewise, functional equations
- Ch 9: Implicit & Parametric — Curves without explicit y = f(x)
- Ch 10: Logarithmic & Higher Derivatives — x^x type, nth derivatives
- Ch 11: Special Functions — Inverse trig, |f(x)|, substitution tricks

**Part III — JEE Level (Advanced):**
- Ch 12: Mean Value Theorems — Rolle's, LMVT, inequalities
- Ch 13: L'Hôpital's Rule — All indeterminate forms resolved

### What's Next in Your Journey?

The natural next step after differentiation is **Integration** (the reverse process), which requires all the tools you've built here. Additionally, the study of **Maxima, Minima, and Curve Sketching** uses derivatives directly.
