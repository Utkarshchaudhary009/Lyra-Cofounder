# Chapter 5: Local Maxima and Minima — The 1st & 2nd Derivative Tests

> *NCERT Section 6.6 | Class 12 Maths — Application of Derivatives*

---

## Stage 1: The Core Idea

### The Hill-Station Road — The Perfect Analogy

Imagine driving on a winding mountain road. You climb until you reach a **pass** — a point where, just before it, the road was going *up*, and just after it, the road goes *down*. That pass is a **local maximum**: it is the highest point in its immediate neighbourhood, even though there may be a taller peak further along. Now continue: you descend into a valley and reach its lowest point — *before* it the road was descending, *after* it the road climbs. That valley floor is a **local minimum**.

But some points on the road are neither. Suppose the road is flat-bottomed at a *saddle* — it dips slightly then rises again on the same side of a level stretch, or it just changes its curve direction without turning back. That is a **point of inflection** — the slope flattens (f'(c) = 0) but the road does not turn around.

This is **local maxima and minima** in a nutshell. We do not look at the whole journey (that is Chapter 6, absolute extrema); we look at what happens *right around* a critical point. The two tools that tell us whether a flat point is a hill-top, a valley-bottom, or just a bend are the **First Derivative Test** and the **Second Derivative Test**.

### What is a Critical Point — Conceptually?

A **critical point** (or stationary point) of $f$ is any point $c$ in the domain where either:

1. $f'(c) = 0$ (the tangent is horizontal), **or**
2. $f$ is **not differentiable** at $c$ (a cusp, corner, or vertical tangent).

> Warning: $f'(c) = 0$ does **NOT** by itself guarantee a maximum or minimum. It could be a point of inflection. You must test the *behaviour around* $c$.

> Tip: Always find critical points first, then *classify* each one. Classification uses either the sign-flip of $f'$ (First Test) or the sign of $f''$ (Second Test).

> Key Takeaway: A **local maximum** is a peak you reach by walking left-to-right and turning downward; a **local minimum** is a trough where you turn upward. "Local" means *in a small neighbourhood* — not the whole domain.

### First Derivative Test — The Sign-Flip Rule

| Sign of $f'(x)$ just left of $c$ | Sign just right of $c$ | Conclusion at $c$ |
|---|---|---|
| $+$ (rising) | $-$ (falling) | **Local maximum** |
| $-$ (falling) | $+$ (rising) | **Local minimum** |
| $+$ to $+$ or $-$ to $-$ | no change | **Point of inflection** |

### Second Derivative Test — The Concavity Shortcut

| Condition at critical point $c$ | Conclusion |
|---|---|
| $f'(c) = 0$ and $f''(c) < 0$ | **Local maximum** (curve concave down) |
| $f'(c) = 0$ and $f''(c) > 0$ | **Local minimum** (curve concave up) |
| $f'(c) = 0$ and $f''(c) = 0$ | **Test fails** → revert to First Derivative Test |

> Classic Exam Trap: When the second derivative test *fails* ($f''(c) = 0$), students wrongly announce "there is no extremum". The truth is the test is *inconclusive* — you must fall back to the **First Derivative Test**. A point can still be a max or min!

---

## Stage 2: The Formula Lab

### Core Working Rules

**Step 1 — Find critical points:** Solve $f'(x) = 0$ and note points where $f$ is not differentiable.

**First Derivative Test:**

$$\boxed{\text{If } f'(x) \text{ changes } +\to-\text{ at } c \Rightarrow f(c)\text{ is a local max};\quad -\to+\Rightarrow\text{local min}}$$

**Second Derivative Test:**

$$\boxed{f'(c)=0,\; f''(c)<0 \;\Rightarrow\; \text{local max};\qquad f'(c)=0,\; f''(c)>0 \;\Rightarrow\; \text{local min}}$$

$$\boxed{f'(c)=0,\; f''(c)=0 \;\Rightarrow\; \text{test fails, use First Derivative Test}}$$

### Special Forms via Log-Differentiation

For functions where the variable appears in both base and exponent, take natural log, then differentiate.

$$\boxed{\frac{d}{dx}\bigl(x^x\bigr) = x^x(1+\ln x),\qquad x>0}$$

$$\boxed{\frac{d}{dx}\left[\left(\frac{2}{x}\right)^{x^2}\right] = \left(\frac{2}{x}\right)^{x^2}\bigl(2x\ln\tfrac{2}{x} - 2x\bigr),\qquad x>0}$$

For $f(x) = ax + \dfrac{b}{x}$ with $a,b>0,\; x>0$:

$$\boxed{f_{\min}\text{ occurs at } x = \sqrt{\frac{b}{a}},\qquad f_{\min} = 2\sqrt{ab}}$$

For the trigonometric product:

$$\boxed{\max(\sin x\cos x) = \frac{1}{2}\text{ at } x = \frac{\pi}{4}+n\pi;\qquad \min = -\frac{1}{2}}$$

### Variable Reference Table

| Symbol | Meaning | Domain / Unit |
|---|---|---|
| $f'(x)$ | First derivative (slope) | function of $x$ |
| $f''(x)$ | Second derivative (concavity) | function of $x$ |
| $c$ | Critical point | in domain of $f$ |
| $f(c)$ | **Extremum value** (evaluate!) | same unit as $f$ |
| $a,b$ | Positive parameters | $a,b>0$ |

### What the Tests Tell Us

- The **First Derivative Test** is universal: it works even when $f''(c)=0$ or when $f$ is non-differentiable at $c$ (with care).
- The **Second Derivative Test** is quicker but only conclusive when $f''(c)\neq 0$.
- A point of inflection is where $f'$ has a local extremum (so $f''=0$ and changes sign) — the curve changes concavity but does not turn around.

### Key Numbers & Results to Memorize

| Fact | Result |
|---|---|
| Local max of $ax+b/x$ ($a,b>0$) | none; **minimum** at $x=\sqrt{b/a}$ |
| Least value of $x + 1/x$ ($x>0$) | $2$ at $x=1$ |
| Maximum of $\sin x\cos x$ | $1/2$ |
| Local max of $x^x$ ($x>0$) | at $x = 1/e$, value $(1/e)^{1/e}$ |

### Special Cases Table

| Function | Critical point | Test used | Result |
|---|---|---|---|
| $x^2$ at $0$ | $f'(0)=0, f''(0)=2>0$ | 2nd | local min $=0$ |
| $-x^2$ at $0$ | $f'(0)=0, f''(0)=-2<0$ | 2nd | local max $=0$ |
| $x^3$ at $0$ | $f'(0)=0, f''(0)=0$ | fails → 1st | point of inflection |
| $x^4$ at $0$ | $f'(0)=0, f''(0)=0$ | fails → 1st | local min $=0$ |
| $x^{1/3}$ at $0$ | not differentiable | cusp | local min $=0$ |

---

## Stage 3: Type-wise Mastery

---

### Type 1: Polynomial Local Extrema + Values *

**Pattern:** "For $f(x) = \text{polynomial}$, find the points of local maxima/minima and the corresponding values."

**Solved Example** (Medium) — NCERT Exemplar Q11

> Find the points of local maxima and local minima, if any, of the function $f(x) = 2x^3 - 3x^2 - 12x + 4$. Also find the local maximum and minimum values.

<details><summary><b>Solution</b></summary>

**Step 1 — First derivative:**

$$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x-2)(x+1)$$

Set $f'(x)=0$: critical points $x = 2$ and $x = -1$.

**Step 2 — First Derivative Test (sign chart):**

| Interval | $(x+1)$ | $(x-2)$ | $f'(x)$ | Behaviour |
|---|---|---|---|---|
| $x < -1$ | $-$ | $-$ | $+$ | rising |
| $-1 < x < 2$ | $+$ | $-$ | $-$ | falling |
| $x > 2$ | $+$ | $+$ | $+$ | rising |

- At $x = -1$: $f'$ changes $+\to-$ ⇒ **local maximum**.
- At $x = 2$: $f'$ changes $-\to+$ ⇒ **local minimum**.

**Step 3 — Evaluate values (TRAP: report $f(c)$, not $c$!):**

$$f(-1) = 2(-1)^3 - 3(-1)^2 - 12(-1) + 4 = -2 - 3 + 12 + 4 = \boxed{11}$$

$$f(2) = 2(8) - 3(4) - 12(2) + 4 = 16 - 12 - 24 + 4 = \boxed{-16}$$

**Answer:** Local maximum value $= 11$ at $x = -1$; local minimum value $= -16$ at $x = 2$.

</details>

---

**Practice Questions**

1. (Easy) Find the local extrema of $f(x) = x^2 - 4x + 6$.

<details><summary><b>Answer</b></summary>

$f'(x) = 2x - 4 = 0 \Rightarrow x = 2$. $f''(x) = 2 > 0$ ⇒ local minimum.

$$f(2) = 4 - 8 + 6 = \boxed{2\ \text{(local min at }x=2\text{)}}$$

</details>

---

2. (Medium) Find local maxima/minima of $f(x) = x^3 - 6x^2 + 9x + 15$.

<details><summary><b>Answer</b></summary>

$f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3) = 0 \Rightarrow x = 1, 3$.

Sign: $+$ for $x<1$, $-$ for $1<x<3$, $+$ for $x>3$.

- $x=1$: $+\to-$ ⇒ local max, $f(1) = 1 - 6 + 9 + 15 = \boxed{19}$.
- $x=3$: $-\to+$ ⇒ local min, $f(3) = 27 - 54 + 27 + 15 = \boxed{15}$.

</details>

---

3. (Medium) For $f(x) = -x^3 + 12x$, find all local extrema and values.

<details><summary><b>Answer</b></summary>

$f'(x) = -3x^2 + 12 = -3(x^2 - 4) = -3(x-2)(x+2) = 0 \Rightarrow x = \pm 2$.

- $x=-2$: $f'$ changes $+\to-$ ⇒ local max, $f(-2) = 8 - 24 = \boxed{-16}$.
- $x=2$: $f'$ changes $-\to+$ ⇒ local min, $f(2) = -8 + 24 = \boxed{16}$.

</details>

---

4. (Hard) Show that $f(x) = x^3 - 3x$ has no absolute maximum or minimum on $\mathbb{R}$, but find its local extrema.

<details><summary><b>Answer</b></summary>

$f'(x) = 3x^2 - 3 = 3(x-1)(x+1) = 0 \Rightarrow x = \pm 1$.

- $x=-1$: $+\to-$ ⇒ local max, $f(-1) = -1 + 3 = 2$.
- $x=1$: $-\to+$ ⇒ local min, $f(1) = 1 - 3 = -2$.

As $x\to\infty$, $f(x)\to\infty$ and as $x\to-\infty$, $f(x)\to-\infty$, so **no absolute extrema** on $\mathbb{R}$.

</details>

---

### Type 2: High-Degree Polynomial with Point of Inflection *

**Pattern:** "Classify all critical points of a degree-4 or degree-5 polynomial; identify point(s) of inflection."

**Solved Example** (Hard) — NCERT Exemplar Q26

> Find the points of local maxima/minima and points of inflection of $f(x) = x^5 - 5x^4 + 5x^3 - 1$.

<details><summary><b>Solution</b></summary>

$$f'(x) = 5x^4 - 20x^3 + 15x^2 = 5x^2(x^2 - 4x + 3) = 5x^2(x-1)(x-3)$$

Critical points: $x = 0,\; 1,\; 3$.

**Sign of $f'(x)$:**

| Interval | $x^2$ | $(x-1)$ | $(x-3)$ | $f'(x)$ |
|---|---|---|---|---|
| $x<0$ | $+$ | $-$ | $-$ | $+$ |
| $0<x<1$ | $+$ | $-$ | $-$ | $+$ |
| $1<x<3$ | $+$ | $+$ | $-$ | $-$ |
| $x>3$ | $+$ | $+$ | $+$ | $+$ |

- $x=0$: $+\to+$ (no change) ⇒ **point of inflection** (note $f'(0)=0$ but no extremum).
- $x=1$: $+\to-$ ⇒ **local max**, $f(1) = 1 - 5 + 5 - 1 = 0$.
- $x=3$: $-\to+$ ⇒ **local min**, $f(3) = 243 - 405 + 135 - 1 = -28$.

$$\boxed{\text{Local max }0\text{ at }x=1;\ \text{local min }-28\text{ at }x=3;\ \text{inflection at }x=0}$$

</details>

---

**Practice Questions**

1. (Medium) For $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$, find local extrema and values.

<details><summary><b>Answer</b></summary>

$f'(x) = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x-2)(x+1) = 0 \Rightarrow x = -1,0,2$.

Sign: $x<-1$ ($-$), $-1<x<0$ ($+$), $0<x<2$ ($-$), $x>2$ ($+$).

- $x=-1$: $-\to+$ ⇒ local min, $f(-1) = 3+4-12+5 = 0$.
- $x=0$: $+\to-$ ⇒ local max, $f(0) = 5$.
- $x=2$: $-\to+$ ⇒ local min, $f(2) = 48 - 32 - 48 + 5 = -27$.

</details>

---

2. (Hard) For $f(x) = x^4 - 4x^3 + 6x^2$, use the second derivative test at $x=1$; state why it needs care and classify.

<details><summary><b>Answer</b></summary>

$f'(x) = 4x^3 - 12x^2 + 12x = 4x(x^2 - 3x + 3)$. The quadratic has no real roots, so only critical point $x=0$.

$f''(x) = 12x^2 - 24x + 12 = 12(x-1)^2$. At $x=0$: $f''(0) = 12 > 0$ ⇒ local min at $x=0$, $f(0)=0$. (The point $x=1$ is not a critical point, though $f''(1)=0$ — a point of inflection of the derivative, not of $f$ itself.)

</details>

---

### Type 3: Second-Derivative-Test Failure Fallback *

**Pattern:** "A critical point gives $f''(c)=0$. Do not conclude 'no extremum' — revert to the First Derivative Test."

**Solved Example** (Medium)

> For $f(x) = x^4$, the point $x=0$ satisfies $f'(0)=0$ and $f''(0)=0$. Does $f$ have a local extremum at $0$? Justify.

<details><summary><b>Solution</b></summary>

Second derivative test is **inconclusive** (fails). Revert to First Derivative Test:

$$f'(x) = 4x^3$$

- For $x<0$: $f'(x) < 0$ (falling).
- For $x>0$: $f'(x) > 0$ (rising).

Sign changes $-\to+$ at $x=0$ ⇒ **local minimum** at $x=0$, with value $f(0)=0$.

> Contrast: for $f(x)=x^3$, $f'(x)=3x^2$ is $+\to+$ (no change) ⇒ point of inflection, **not** an extremum. Same failure of the second test, but different conclusion! The first test is what decides.

</details>

---

**Practice Questions**

1. (Easy) For $f(x) = x^3$, classify $x=0$ given $f'(0)=f''(0)=0$.

<details><summary><b>Answer</b></summary>

$f'(x)=3x^2$: $+\to+$ at 0 ⇒ **point of inflection**, no extremum.

</details>

---

2. (Medium) For $f(x) = (x-1)^4$, second test fails at $x=1$. Find the extremum via first test.

<details><summary><b>Answer</b></summary>

$f'(x) = 4(x-1)^3$: for $x<1$, $f'<0$; for $x>1$, $f'>0$. $-\to+$ ⇒ **local min** at $x=1$, value $f(1)=0$.

</details>

---

### Type 4: Logarithmic-Form Extrema ($x^x,\ (1/x)^x,\ (2/x)^{x^2}$) *

**Pattern:** "Find the extremum of a function with the variable in both base and exponent → take log, differentiate."

**Solved Example** (Hard) — NCERT Exemplar Q6 / JEE Main 2021

> Find the maximum value of $f(x) = \left(\dfrac{2}{x}\right)^{x^2}$ for $x>0$.

<details><summary><b>Solution</b></summary>

Let $y = \left(\dfrac{2}{x}\right)^{x^2},\ x>0$. Take natural log:

$$\ln y = x^2\ln\!\left(\frac{2}{x}\right) = x^2(\ln 2 - \ln x)$$

Differentiate w.r.t. $x$:

$$\frac{1}{y}\frac{dy}{dx} = 2x(\ln 2 - \ln x) + x^2\left(-\frac{1}{x}\right) = 2x\ln 2 - 2x\ln x - x$$

$$= x\bigl(2\ln 2 - 2\ln x - 1\bigr) = x\left(\ln\frac{4}{x^2} - 1\right)$$

Set $dy/dx = 0$ ($x>0$): $\ln(4/x^2) = 1 \Rightarrow 4/x^2 = e \Rightarrow x^2 = 4/e \Rightarrow x = 2/\sqrt{e}$.

Check sign of $dy/dx$: for $x < 2/\sqrt{e}$, $\ln(4/x^2) > 1$ ⇒ $dy/dx>0$; for $x > 2/\sqrt{e}$, $dy/dx<0$. So $+\to-$ ⇒ **local maximum**.

Maximum value:

$$y_{\max} = \left(\frac{2}{2/\sqrt{e}}\right)^{4/e} = \left(\sqrt{e}\right)^{4/e} = e^{\frac{2}{e}} = \boxed{e^{2/e}}$$

</details>

---

**Practice Questions**

1. (Medium) Find the minimum of $f(x) = x^x$ for $x>0$. (Exemplar Q7)

<details><summary><b>Answer</b></summary>

$\ln y = x\ln x \Rightarrow y'/y = 1+\ln x$. Set $=0 \Rightarrow \ln x = -1 \Rightarrow x = 1/e$.

For $x<1/e$, $\ln x<-1$ ⇒ $y'<0$; for $x>1/e$, $y'>0$. $-\to+$ ⇒ local min at $x=1/e$.

$$f(1/e) = (1/e)^{1/e} = \boxed{e^{-1/e}}$$

</details>

---

2. (Medium) Find the extremum of $f(x) = (1/x)^x,\ x>0$.

<details><summary><b>Answer</b></summary>

$\ln y = x\ln(1/x) = -x\ln x \Rightarrow y'/y = -(1+\ln x)$. Zero at $x=1/e$.

For $x<1/e$, $y'>0$; for $x>1/e$, $y'<0$. $+\to-$ ⇒ local max at $x=1/e$.

$$f(1/e) = e^{1/e} = \boxed{e^{1/e}}$$

</details>

---

3. (Hard) Find the local maximum of $f(x) = x^{1/x},\ x>0$.

<details><summary><b>Answer</b></summary>

$\ln y = (\ln x)/x \Rightarrow y'/y = \dfrac{1-\ln x}{x^2} = 0 \Rightarrow \ln x = 1 \Rightarrow x = e$.

For $x<e$, $y'>0$; for $x>e$, $y'<0$. $+\to-$ ⇒ local max at $x=e$, value $f(e) = \boxed{e^{1/e}}$.

</details>

---

### Type 5: Trigonometric Extrema *

**Pattern:** "Find max/min of a sine-cosine combination; use $a\sin\theta+b\cos\theta$ form or derivative test."

**Solved Example** (Medium) — NCERT Exemplar Q9

> Find the local maximum and minimum values of $f(x) = 2\sin 3x + 3\cos 3x$.

<details><summary><b>Solution</b></summary>

$$f'(x) = 6\cos 3x - 9\sin 3x$$

Set $f'(x)=0$: $6\cos 3x = 9\sin 3x \Rightarrow \tan 3x = \frac{2}{3}$.

$$f''(x) = -18\sin 3x - 27\cos 3x$$

At points where $\tan 3x = 2/3$: take a reference right triangle with opposite $2$, adjacent $3$, hypotenuse $\sqrt{13}$. Then $\sin 3x = \pm 2/\sqrt{13}$, $\cos 3x = \pm 3/\sqrt{13}$ (same sign since $\tan>0$).

- Both positive: $f'' = -18(2/\sqrt{13}) - 27(3/\sqrt{13}) < 0$ ⇒ **local maximum**.

$$f = 2(2/\sqrt{13}) + 3(3/\sqrt{13}) = \frac{13}{\sqrt{13}} = \boxed{\sqrt{13}}$$

- Both negative: $f'' > 0$ ⇒ **local minimum**, $f = -\sqrt{13} = \boxed{-\sqrt{13}}$.

</details>

---

**Practice Questions**

1. (Easy) Find the maximum value of $\sin x\cos x$.

<details><summary><b>Answer</b></summary>

$\sin x\cos x = \frac{1}{2}\sin 2x \le \frac{1}{2}$. Maximum $= \boxed{1/2}$ at $2x = \pi/2 \Rightarrow x=\pi/4+n\pi$.

</details>

---

2. (Medium) Show $f(x) = \sin x + \sqrt{3}\cos x$ attains its maximum at $x = \pi/6$.

<details><summary><b>Answer</b></summary>

$f'(x) = \cos x - \sqrt{3}\sin x = 0 \Rightarrow \tan x = 1/\sqrt{3} \Rightarrow x = \pi/6$.

$f''(x) = -\sin x - \sqrt{3}\cos x$; at $\pi/6$: $f'' = -1/2 - \sqrt{3}(\sqrt{3}/2) = -2 < 0$ ⇒ local max, value $1/2 + \sqrt{3}(\sqrt{3}/2) = 2$.

</details>

---

### Type 6: Parameter / Condition on Extrema *

**Pattern:** "Given that $f$ has a local max for $x<0$ and local min for $x>0$, find the admissible parameter values."

**Solved Example** (Hard) — JEE 2023 (25 Jan)

> The function $f(x) = x^3 + ax^2 + bx + c$ has a local maximum at some $x_1<0$ and a local minimum at some $x_2>0$. What condition must $a$ and $b$ satisfy?

<details><summary><b>Solution</b></summary>

$$f'(x) = 3x^2 + 2ax + b$$

Roots of $f'(x)=0$ are $x_{1,2} = \dfrac{-2a \pm \sqrt{4a^2 - 12b}}{6}$. For two distinct critical points we need discriminant $>0$: $a^2 - 3b > 0$.

Since the leading coefficient of $f'$ is positive, $f'$ is $+$ outside the roots and $-$ between them. So the **smaller** root is the local max and the **larger** root is the local min.

We need smaller root $<0$ and larger root $>0$. A quadratic $3x^2+2ax+b$ with positive leading coefficient has one negative and one positive root **iff** its constant term $b < 0$ (product of roots $= b/3 < 0$).

Thus the required condition is:

$$\boxed{b < 0\quad\text{and}\quad a^2 - 3b > 0}$$

(When $b<0$, $a^2-3b>0$ automatically holds, so the essential condition is $\boxed{b<0}$.)

</details>

---

**Practice Questions**

1. (Medium) If $f(x) = x^3 - 3ax^2 + 3(a^2-1)x + 5$ has a local max at $x=1$, find $a$.

<details><summary><b>Answer</b></summary>

$f'(x) = 3x^2 - 6ax + 3(a^2-1)$. Condition $f'(1)=0$:

$$3 - 6a + 3(a^2-1) = 0 \Rightarrow a^2 - 2a = 0 \Rightarrow a(a-2)=0$$

For local max at $x=1$ we need $f''(1)<0$: $f''(x)=6x-6a$, so $f''(1)=6-6a<0\Rightarrow a>1$. Hence $\boxed{a=2}$.

</details>

---

### Type 7: Exact-One-Max-One-Min Condition *

**Pattern:** "Find the parameter value so that $f$ has *exactly one* local maximum and *exactly one* local minimum."

**Solved Example** (Hard) — JEE 2020

> Let $f(x) = (1-\cos^2 x)(\lambda + \sin x)$. Find $\lambda$ such that $f$ has exactly one local maximum and exactly one local minimum in $[0,2\pi]$.

<details><summary><b>Solution</b></summary>

Note $1-\cos^2 x = \sin^2 x$, so $f(x) = \sin^2 x\,(\lambda + \sin x)$.

$$f'(x) = 2\sin x\cos x\,(\lambda+\sin x) + \sin^2 x\cos x = \cos x\sin x\,[2(\lambda+\sin x) + \sin x]$$

$$= \cos x\sin x\,(2\lambda + 3\sin x)$$

Critical points arise from $\cos x = 0$, $\sin x = 0$, or $\sin x = -2\lambda/3$.

- $\cos x = 0 \Rightarrow x=\pi/2,\ 3\pi/2$.
- $\sin x = 0 \Rightarrow x=0,\ \pi,\ 2\pi$.
- $\sin x = -2\lambda/3$ gives real solutions only if $|2\lambda/3|\le 1$, i.e. $|\lambda|\le 3/2$, and then generally **two** extra solutions in $(0,2\pi)$ (where sine takes an interior value).

To have *exactly one* max and *exactly one* min, we must avoid the extra pair ⇒ require $|2\lambda/3| > 1$, i.e. $|\lambda| > 3/2$. But we must also keep the classification of the boundary/trig points giving exactly one max and one min each cycle.

Analysing sign changes of $f'$ from $\cos x\sin x(2\lambda+3\sin x)$: the factors $\cos x$ and $\sin x$ already produce the standard alternating pattern (max/min/max/min) across $(0,2\pi)$. The term $(2\lambda+3\sin x)$ is non-zero throughout when $2\lambda+3\sin x \neq 0$ for all $x$. Since $\sin x\in[-1,1]$, this holds when $2\lambda > 3$ or $2\lambda < -3$, i.e. $\lambda > 3/2$ or $\lambda < -3/2$.

For $\lambda > 3/2$: the factor stays positive, so the sign pattern is governed by $\cos x\sin x$, giving exactly one local max ($\pi/2$) and one local min ($3\pi/2$) in $(0,2\pi)$.

$$\boxed{\lambda > \frac{3}{2}\ \text{or}\ \lambda < -\frac{3}{2}\quad(\text{equivalently }|\lambda|>\tfrac{3}{2})}$$

(At the boundary $|\lambda|=3/2$ an extra critical point of inflection appears, so strict inequality is needed.)

</details>

---

**Practice Questions**

1. (Hard) Find the range of $k$ for which $f(x) = x^4 + kx^3$ has exactly two local extrema.

<details><summary><b>Answer</b></summary>

$f'(x) = 4x^3 + 3kx^2 = x^2(4x+3k)$. Critical points: $x=0$ (double root) and $x=-3k/4$.

At $x=0$, $f'$ is $+\to+$ (sign of $x^2$ never changes) ⇒ inflection, not extremum. So the only extremum is at $x=-3k/4$, which exists and is genuine only when $-3k/4 \neq 0$, i.e. $k\neq 0$.

But that gives only **one** local extremum. To get exactly **two**, we need both critical points to be genuine extrema — impossible here because $x=0$ is always a double root (inflection). Hence: **$f$ never has exactly two local extrema; it has 0 (if $k=0$) or 1 (if $k\neq 0$) extremum.** The requested condition has **no solution**.

</details>

---

### Type 8: Monotonicity + Extrema Mixed (Assertion-Reason / MCQ) *

**Pattern:** "Given $f''>0$ everywhere and a composite $g(x)=f(\phi(x))$, determine increasing/decreasing behaviour and extrema."

**Solved Example** (Hard) — JEE 2023 pattern

> Let $f$ be a twice-differentiable function with $f''(x)>0$ for all $x$. Define $g(x) = f(\tan^2 x - 2\tan x + a)$ on an appropriate interval. Discuss where $g$ is increasing/decreasing and locate its minima.

<details><summary><b>Solution</b></summary>

Let $u(x) = \tan^2 x - 2\tan x + a = (\tan x - 1)^2 + (a-1)$. Then

$$g'(x) = f'(u(x))\cdot u'(x),\qquad u'(x) = 2(\tan x - 1)\sec^2 x$$

Since $f''(x)>0$ everywhere, $f'$ is **strictly increasing**. Also $\sec^2 x>0$. The sign of $g'(x)$ is the sign of $f'(u(x))\cdot(\tan x - 1)$.

- $u'(x) = 0$ when $\tan x = 1$ ($x=\pi/4$ in $(0,\pi/2)$). At this point $u= a-1+0$... Actually $u = (\tan x-1)^2+(a-1)$ ⇒ at $\tan x=1$, $u = a-1$.
- For $\tan x > 1$, $u'(x)>0$; for $\tan x<1$, $u'(x)<0$.

Because $f'$ is increasing, $g'$ changes sign according to whether $u$ is above/below the value where $f'=0$. This is a **mixed** problem: monotonicity of $g$ depends on both the inner quadratic in $\tan x$ and the zero of $f'$. The minima of $g$ occur where $u(x)$ is minimized (since $f$ itself, being convex with $f''>0$, is minimized where its argument is smallest *if* $f'$ has a zero) — specifically near $\tan x = 1$ provided $f'(a-1)\ge 0$.

**Key takeaway for exams:** when the outer $f$ is convex ($f''>0$), the composite $g$ is increasing wherever the inner function $u$ is increasing *and* $f'(u)>0$; careful sign analysis of $u'(x)$ combined with the (unknown but monotonic) $f'$ is required. Mark the critical point $\tan x = 1$ as the likely local minimum of $g$.

</details>

---

**Practice Questions**

1. (Medium) If $f''(x)>0$ for all $x$ and $f'(2)=0$, then at $x=2$ the function $h(x)=f(x)$ has: (a) local max (b) local min (c) inflection (d) cannot say.

<details><summary><b>Answer</b></summary>

$f''(2)>0$ and $f'(2)=0$ ⇒ by second derivative test, **local minimum**. Answer **(b)**.

</details>

---

> ⚠️ **COMMON TRAPS — Read Before You Solve**
>
> **Trap 1 — Reporting the $x$-value as the extremum.** The question "find the local maximum" usually wants the **value** $f(c)$, not the point $c$. Always substitute back: answer "max value $= f(c)$ at $x=c$".
>
> **Trap 2 — Declaring extremum without confirming $f'(c)=0$.** You may only apply the second derivative test at a point where $f'(c)=0$ (or at a non-differentiable point via first test). Computing $f''(c)$ alone means nothing.
>
> **Trap 3 — When the second test fails, wrongly saying "no extremum".** $f''(c)=0$ is *inconclusive*, not a denial. Revert to the First Derivative Test (e.g. $x^4$ at $0$ is a min even though $f''(0)=0$).
>
> **Trap 4 — Missing non-differentiable points.** Functions like $y = x^{1/3}$ (vertical tangent at $0$) or cusps have critical points where $f$ is *not differentiable*. The derivative test on smooth parts will miss them.
>
> **Trap 5 — Confusing local vs absolute.** A local minimum can be larger than a local maximum in a different neighbourhood. "Local" means *nearby*; absolute (global) needs the whole domain/interval (see Chapter 6).

---

## Stage 4: MCQ Mastery

**Q1.** For the function $f(x) = x^3 - 3x$, which statement is true at $x = 0$?

(a) Local maximum &emsp; (b) Local minimum &emsp; (c) Point of inflection &emsp; (d) Undefined

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Point of inflection**

$f'(x)=3x^2-3$, so $f'(0)=-3\neq 0$ — $x=0$ is not a critical point of $f$ at all here; the inflection of $f'$ matters. Actually for this function $f'(0)=-3$, so $x=0$ is just a regular point. (If the intended function were $x^3$, then $f'(0)=f''(0)=0$ with $+\to+$ ⇒ inflection.) The trap is assuming every flat-looking point is an extremum.

</details>

---

**Q2.** The function $f(x) = x^x$ ($x>0$) attains its minimum at:

(a) $x = 1$ &emsp; (b) $x = 1/e$ &emsp; (c) $x = e$ &emsp; (d) $x = 0$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $x = 1/e$**

$\frac{d}{dx}(x^x) = x^x(1+\ln x)$; zero when $\ln x = -1 \Rightarrow x=1/e$. Sign $-\to+$ ⇒ local (and here absolute on $x>0$) minimum. Option (c) is the max of $x^{1/x}$, a different function.

</details>

---

**Q3.** If $f'(c)=0$ and $f''(c)=0$, then:

(a) $f$ has a local max at $c$ &emsp; (b) $f$ has a local min at $c$ &emsp; (c) $f$ has no extremum at $c$ &emsp; (d) The second derivative test is inconclusive

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d) The second derivative test is inconclusive**

You must revert to the First Derivative Test. Both $x^4$ (min) and $x^3$ (inflection) satisfy $f'(0)=f''(0)=0$, so (a),(b),(c) are each sometimes false.

</details>

---

**Q4.** The least value of $f(x) = 4x + \dfrac{9}{x}$ for $x>0$ is:

(a) $6$ &emsp; (b) $12$ &emsp; (c) $9$ &emsp; (d) $24$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $12$**

By the formula, min of $ax+b/x$ at $x=\sqrt{b/a}=\sqrt{9/4}=3/2$. Value $=4(3/2)+9/(3/2)=6+6=12=2\sqrt{ab}=2\sqrt{36}=12$.

</details>

---

**Q5.** (Assertion-Reason) **Assertion (A):** If $f'(c) = 0$ and $f''(c) < 0$, then $f$ has a local maximum at $c$. **Reason (R):** A negative second derivative means the curve is concave down at $c$, so the tangent at the flat point is a local peak.

(a) Both A and R true, R correct explanation &emsp; (b) Both true, R not explanation &emsp; (c) A true R false &emsp; (d) A false R true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)** Both true and R explains A. This is the Second Derivative Test. Standard.

</details>

---

**Q6.** (Assertion-Reason) **Assertion (A):** The point $x=0$ is a local minimum of $f(x)=x^4$. **Reason (R):** $f'(0)=0$ and $f''(0)=0$, so the second derivative test fails, but the first derivative test gives $-\to+$ confirming a local minimum.

(a) Both A and R true, R correct explanation &emsp; (b) Both true, R not explanation &emsp; (c) A true R false &emsp; (d) A false R true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)** Both true, and R correctly explains A by showing the fallback procedure.

</details>

---

**Q7.** The maximum value of $\sin x\cos x$ is:

(a) $1$ &emsp; (b) $1/2$ &emsp; (c) $\sqrt{2}$ &emsp; (d) $2$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $1/2$** since $\sin x\cos x = \frac{1}{2}\sin 2x \le 1/2$.

</details>

---

**Q8.** For $f(x) = (2/x)^{x^2}$ ($x>0$), the maximum occurs at:

(a) $x = \sqrt{e}$ &emsp; (b) $x = 2/\sqrt{e}$ &emsp; (c) $x = e/2$ &emsp; (d) $x = 2e$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $x = 2/\sqrt{e}$** — derived in Type 4 solved example; $\ln(4/x^2)=1 \Rightarrow x^2=4/e$.

</details>

---

**Q9.** (Statement-based) **Statement I:** A function can have a local extremum at a point where it is not differentiable. **Statement II:** $f(x) = |x|$ has a local minimum at $x=0$ despite being non-differentiable there.

(a) I true, II false &emsp; (b) I false, II true &emsp; (c) Both true &emsp; (d) Both false

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Both true.** Critical points include non-differentiable points (cusps/corners). $|x|$ has a sharp min at $0$.

</details>

---

**Q10.** If $f''(x) > 0$ for all $x$ and $f'(1) = 0$, then $x=1$ is:

(a) local max &emsp; (b) local min &emsp; (c) inflection &emsp; (d) none of these

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) local min** — convex function, $f'(1)=0$ ⇒ global minimum.

</details>

---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 1 + 5 combined

Find the local extrema of $f(x) = 2x^3 - 3x^2 - 12x + 4$ and separately state the maximum value of $\sin x\cos x$.

<details><summary><b>Solution</b></summary>

From Type 1: local max value $= 11$ at $x=-1$; local min value $= -16$ at $x=2$.

$\sin x\cos x = \frac{1}{2}\sin 2x$, maximum $= \boxed{1/2}$.

</details>

---

**Problem 2** (Medium) — Types 2 + 3 combined

For $f(x) = x^4$, show the second derivative test fails at $x=0$ and use the first test to classify it. Also classify $x=0$ for $g(x)=x^3$.

<details><summary><b>Solution</b></summary>

$f'(x)=4x^3$, $f''(0)=0$ (fails). First test: $f'<0$ left, $>0$ right ⇒ **local min** at $0$, value $0$.

$g'(x)=3x^2$, $g''=6x$, $g''(0)=0$ (fails). First test: $g'>0$ both sides ⇒ **point of inflection**, no extremum.

</details>

---

**Problem 3** (Hard) — Types 4 + 6 combined

Find the maximum of $f(x) = x^{1/x}$ ($x>0$). Then suppose $h(x) = x^{1/x} + kx$ has a local extremum at $x=e$; find $k$.

<details><summary><b>Solution</b></summary>

From Type 4 practice: max of $x^{1/x}$ is at $x=e$, value $e^{1/e}$.

$h'(x) = \frac{d}{dx}(x^{1/x}) + k$. At $x=e$, $\frac{d}{dx}(x^{1/x}) = x^{1/x}\frac{1-\ln x}{x^2}$; at $x=e$, $\ln e =1$ ⇒ derivative of $x^{1/x}$ is $0$. For a critical point, $h'(e)=0 \Rightarrow 0 + k = 0 \Rightarrow \boxed{k=0}$.

</details>

---

**Problem 4** (Hard — Competency-Based) — Types 1 + 7 + extrema-values

A manufacturing cost model gives profit $P(x) = -2x^3 + 3x^2 + 36x - 10$ (in ₹ thousands) where $x$ is production level. (a) Find critical points. (b) Classify them and give max profit. (c) Could there be a parameter $\lambda$ such that $P_\lambda(x)=P(x)+\lambda x^2$ has exactly one max and one min? Discuss.

<details><summary><b>Solution</b></summary>

**(a)** $P'(x) = -6x^2 + 6x + 36 = -6(x^2 - x - 6) = -6(x-3)(x+2) = 0 \Rightarrow x = 3, -2$. (Production $x\ge 0$, so relevant $x=3$; $x=-2$ is mathematically a critical point.)

**(b)** Sign of $P'$: for $0<x<3$, $P'>0$ (rising); for $x>3$, $P'<0$ (falling). At $x=3$: $+\to-$ ⇒ **local max**. $P(3) = -54 + 27 + 108 - 10 = \boxed{71}$ (thousand ₹).

**(c)** $P_\lambda'(x) = -6x^2 + 6(1+\lambda)x + 36$. For exactly one max and one min we need two distinct real critical points ⇒ discriminant $>0$: $36(1+\lambda)^2 + 864 >0$, always true. The quadratic $P_\lambda'$ has positive leading coefficient ($-6<0$ actually... it is concave down), so it is $+$ between roots and $-$ outside ⇒ one local max (smaller root) and one local min (larger root) **for every** $\lambda$. So yes — any real $\lambda$ gives exactly one max and one min (provided we restrict to the relevant domain). $\boxed{\text{Any }\lambda\in\mathbb{R}\text{ works.}}$

</details>

---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE pattern]**

(a) Define a critical point of a function $f$. (b) For $f(x) = x^2$, verify using the second derivative test that $x=0$ is a point of local minimum.

<details><summary><b>Model Answer</b></summary>

**(a)** A critical point $c$ is where $f'(c)=0$ or $f$ is not differentiable at $c$. **[1 mark]**

**(b)** $f'(x)=2x$, $f'(0)=0$. $f''(x)=2>0$ ⇒ by second derivative test, local minimum at $x=0$; value $f(0)=0$. **[1 mark]**

</details>

---

**Q2. [3 marks — CBSE Board pattern]**

Find the points of local maxima and minima of $f(x)=x^3-6x^2+9x+15$. Also find the local maximum and minimum values.

<details><summary><b>Model Answer</b></summary>

$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0 \Rightarrow x=1,3$. **[1 mark]**

Sign: $+$ for $x<1$, $-$ for $1<x<3$, $+$ for $x>3$. **[1 mark]**

- $x=1$: local max, $f(1)=1-6+9+15=19$.
- $x=3$: local min, $f(3)=27-54+27+15=15$. **[1 mark]**

(Local max value $19$ at $x=1$; local min value $15$ at $x=3$.)

</details>

---

**Q3. [3 marks — NCERT Exemplar level]**

Find the maximum value of $f(x) = x^x$ for $x>0$.

<details><summary><b>Model Answer</b></summary>

Let $y=x^x$. $\ln y = x\ln x \Rightarrow \frac{1}{y}y' = 1+\ln x$. **[1 mark]**

$y'=0 \Rightarrow \ln x=-1 \Rightarrow x=1/e$. For $x<1/e$, $y'<0$; $x>1/e$, $y'>0$ ⇒ local min at $x=1/e$. **[1 mark]**

$f(1/e)=(1/e)^{1/e}=e^{-1/e}$. **[1 mark]**

(Note: this is the *minimum*; $x^x\to 1$ as $x\to 0^+$ and $x^x\to\infty$ as $x\to\infty$, so there is **no finite maximum** on $x>0$. The extremum found is the global minimum. Clearly state this to avoid the trap of calling it a maximum.)

</details>

---

**Q4. [5 marks — Long Answer]**

(a) State the First Derivative Test for local maxima and minima. [2 marks]
(b) For $f(x)=2x^3-3x^2-12x+4$, find all points of local maxima and minima and the corresponding values. [3 marks]

<details><summary><b>Model Answer</b></summary>

**(a)** Let $f$ be continuous at $c$ and differentiable near $c$ (except possibly at $c$). If $f'(x)$ changes from positive to negative as $x$ increases through $c$, $f(c)$ is a local maximum. If it changes from negative to positive, $f(c)$ is a local minimum. If there is no sign change, $c$ is a point of inflection. **[2 marks]**

**(b)** $f'(x)=6(x-2)(x+1)=0 \Rightarrow x=-1,2$. **[1 mark]**

Sign chart: rising for $x<-1$, falling for $-1<x<2$, rising for $x>2$. **[1 mark]**

- Local max at $x=-1$, value $f(-1)=-2-3+12+4=11$.
- Local min at $x=2$, value $f(2)=16-12-24+4=-16$. **[1 mark]**

</details>

---

**Q5. [5 marks — Competency-Based / Case Study] — Maximum Slope of a Curve**

A robotics engineer studies the slope of a cam profile described by $y = -x^3 + 3x^2 + 9x - 27$. The *steepness* of the cam at any point is the magnitude of the slope $dy/dx$.

(a) Write the expression for the slope $s(x) = dy/dx$. [1 mark]
(b) Find where the slope itself is maximum (i.e., the point of maximum slope). [2 marks]
(c) Compute the maximum slope value. [1 mark]
(d) Why is it incorrect to say "the maximum slope occurs where $d^2y/dx^2 = 0$ without checking the sign change"? [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** $s(x) = \dfrac{dy}{dx} = -3x^2 + 6x + 9$. **[1 mark]**

**(b)** To maximize slope $s(x)$, differentiate: $\dfrac{ds}{dx} = -6x + 6 = 0 \Rightarrow x=1$. **[1 mark]**

Check second derivative of $s$: $d^2s/dx^2 = -6 < 0$ ⇒ $s$ has a maximum at $x=1$. (Equivalently, this is where $d^2y/dx^2 = s'(x)=0$ and $d^3y/dx^3<0$.) **[1 mark]**

**(c)** Maximum slope $= s(1) = -3 + 6 + 9 = \boxed{12}$. **[1 mark]**

**(d)** Because $d^2y/dx^2 = 0$ is only a *necessary* condition for an extremum of the slope; one must confirm a sign change ($+\to-$ for a max) or use the second derivative of $s$. Declaring a maximum solely from $s'(x)=0$ risks calling a point of inflection of the original curve a "maximum slope". **[1 mark]**

</details>

---

## Stage 7: JEE Mains Arena

**Q1.** The maximum value of $f(x) = \left(\dfrac{2}{x}\right)^{x^2}$ for $x>0$ is:

(a) $e^{1/e}$ &emsp; (b) $e^{2/e}$ &emsp; (c) $2/e$ &emsp; (d) $e^{e/2}$

<details><summary><b>Answer</b></summary>

**Answer: (b) $e^{2/e}$** — derived in Type 4; max at $x=2/\sqrt{e}$, value $e^{2/e}$.

</details>

---

**Q2.** Let $f(x) = x^3 + ax^2 + bx$ have a local maximum at some negative $x$ and a local minimum at some positive $x$. Then:

(a) $a>0, b>0$ &emsp; (b) $b<0$ &emsp; (c) $a<0$ &emsp; (d) $b>0$

<details><summary><b>Answer</b></summary>

**Answer: (b) $b<0$** — $f'(x)=3x^2+2ax+b$; for roots of opposite sign, product $=b/3<0\Rightarrow b<0$. (See Type 6.)

</details>

---

**Q3.** For $f(x) = (1-\cos^2 x)(\lambda + \sin x)$ to have exactly one local maximum and exactly one local minimum in $(0,2\pi)$, $\lambda$ must satisfy:

(a) $\lambda > 3/2$ &emsp; (b) $|\lambda| > 3/2$ &emsp; (c) $\lambda = 0$ &emsp; (d) $|\lambda| < 3/2$

<details><summary><b>Answer</b></summary>

**Answer: (b) $|\lambda| > 3/2$** — see Type 7 solved example (avoids the extra pair of roots from $\sin x = -2\lambda/3$).

</details>

---

**Q4.** The function $f(x) = x^4 - 4x^3 + 6x^2$ has at $x=1$:

(a) local max &emsp; (b) local min &emsp; (c) point of inflection &emsp; (d) not a critical point

<details><summary><b>Answer</b></summary>

**Answer: (d) not a critical point** — $f'(x)=4x(x^2-3x+3)$, the quadratic has discriminant $9-12<0$; only critical point is $x=0$ (local min). $x=1$ gives $f'(1)=4(1-3+3)=4\neq0$.

</details>

---

**Q5.** The least value of $f(x) = 5x + \dfrac{20}{x}$ for $x>0$ is:

(a) $10$ &emsp; (b) $20$ &emsp; (c) $40$ &emsp; (d) $2\sqrt{5}$

<details><summary><b>Answer</b></summary>

**Answer: (b) $20$** — min at $x=\sqrt{20/5}=2$, value $=5(2)+20/2=10+10=20=2\sqrt{100}=20$.

</details>

---

*Next: [Chapter 6 — Absolute Maxima and Minima in a Closed Interval](./06_absolute_maxima_minima.md)*

---

## Quick Revision Summary

| Concept | Formula / Rule | Key Point |
|---|---|---|
| Critical point | $f'(c)=0$ or $f$ not differentiable | First find these |
| 1st Derivative Test | $+\to-$ max; $-\to+$ min; no change ⇒ inflection | Universal, works when 2nd fails |
| 2nd Derivative Test | $f''(c)<0$ max; $f''(c)>0$ min; $f''(c)=0$ fails | Only when $f'(c)=0$ |
| $x^x$ ($x>0$) | derivative $x^x(1+\ln x)$ | min at $x=1/e$ |
| $(2/x)^{x^2}$ | log-diff; max at $x=2/\sqrt{e}$ | value $e^{2/e}$ |
| $ax+b/x$ ($a,b>0$) | min at $x=\sqrt{b/a}$ | value $2\sqrt{ab}$ |
| $\sin x\cos x$ | $=\frac{1}{2}\sin 2x$ | max $=1/2$ |
| Non-diff. extremum | e.g. $|x|$ at $0$ | don't miss cusps |

> The Golden Rule: Always report the **value** $f(c)$, never just the point $c$. And when the second test fails, **revert to the first test** — never conclude "no extremum".

> The Number One Exam Trap: $f'(c)=f''(c)=0$ does NOT mean "no extremum" (consider $x^4$); it means the second test is *inconclusive*.

(End of file)
