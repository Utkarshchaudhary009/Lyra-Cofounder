# Chapter 2: Increasing and Decreasing Functions — Reading a Function's Behaviour

> *NCERT Section 6.3 | Class 12 Maths — Application of Derivatives*

---

## Stage 1: The Core Idea

### A Hill, a Valley, and a Flat Road — The Perfect Analogy

Imagine driving along a winding mountain road. At some stretches the road climbs — every step forward takes you **higher**. At other stretches it descends — every step forward takes you **lower**. And on the rare flat patch, your height doesn't change at all.

This is **monotonicity** in a nutshell. A function $f(x)$ is like that road:
- It is **increasing** when, as $x$ moves right, the value $f(x)$ goes **up** (the hill climb).
- It is **decreasing** when, as $x$ moves right, the value $f(x)$ goes **down** (the valley descent).
- It is **constant** on a stretch where $f(x)$ stays **flat**.

The first derivative $f'(x)$ is the **slope of the road** at each point. When the slope is positive, you are climbing (function increasing). When the slope is negative, you are descending (function decreasing). When the slope is zero, the road is locally flat (a peak, a trough, or a plateau).

### What "Increasing" Really Means — Conceptually

Let $f$ be defined on an interval $I$.

- **Strictly increasing** on $I$: if $x_1 < x_2 \implies f(x_1) < f(x_2)$ for all $x_1, x_2 \in I$. The graph always rises as you move right — never levels, never drops.
- **Increasing (non-decreasing)** on $I$: if $x_1 < x_2 \implies f(x_1) \le f(x_2)$. The graph rises or stays flat.
- **Strictly decreasing** / **decreasing**: same idea with the inequalities reversed.

> Warning: The words "increasing" and "strictly increasing" are NOT interchangeable in CBSE/JEE. An examiner who writes "strictly increasing" usually means $f'(x) > 0$, while plain "increasing" means $f'(x) \ge 0$. Read the word carefully.

> Tip: The derivative $f'(x)$ is the **instantaneous slope**. If $f'(x) > 0$ everywhere on $I$, the road is always climbing — so $f$ is strictly increasing. The converse is subtler (see the $x^3$ trap below).

> Key Takeaway: Monotonicity is decided by the **sign** of $f'(x)$, not its value. A tiny positive slope still means "increasing". A single zero of $f'(x)$ does not automatically break monotonicity.

### Slope vs. Behaviour — Comparison Table

| Sign of $f'(x)$ on interval | Behaviour of $f$ | Road analogy |
|---|---|---|
| $f'(x) > 0$ for all $x$ | Strictly increasing | Continuously climbing |
| $f'(x) \ge 0$ for all $x$ | Increasing (non-decreasing) | Climbing or flat |
| $f'(x) < 0$ for all $x$ | Strictly decreasing | Continuously descending |
| $f'(x) \le 0$ for all $x$ | Decreasing (non-increasing) | Descending or flat |
| $f'(x) = 0$ for all $x$ | Constant | Perfectly flat |
| $f'(x)$ changes sign | Neither (has turning points) | Hills and valleys |

> Classic Exam Trap: $f'(x) = 0$ at a single point does NOT mean the function stops being strictly increasing. Example: $f(x) = x^3$ has $f'(0) = 0$ but is **strictly increasing on the whole real line**. This counterexample appears in Assertion-Reason questions every cycle!

---

## Stage 2: The Formula Lab

### Core Criterion (First Derivative Test for Monotonicity)

For a function $f$ continuous on $[a,b]$ and differentiable in $(a,b)$:

$$\boxed{f \text{ is strictly increasing on } I \iff f'(x) > 0 \quad \forall x \in I}$$

$$\boxed{f \text{ is increasing on } I \iff f'(x) \ge 0 \quad \forall x \in I}$$

$$\boxed{f \text{ is strictly decreasing on } I \iff f'(x) < 0 \quad \forall x \in I}$$

$$\boxed{f \text{ is decreasing on } I \iff f'(x) \le 0 \quad \forall x \in I}$$

$$\boxed{f \text{ is constant on } I \iff f'(x) = 0 \quad \forall x \in I}$$

### The Standard Procedure (5 Steps)

1. **Differentiate:** compute $f'(x)$.
2. **Find critical points:** solve $f'(x) = 0$ (and note where $f'(x)$ is undefined).
3. **Partition:** place critical points on the number line — they split the domain into sub-intervals.
4. **Sign chart:** test the sign of $f'(x)$ in each sub-interval (pick a sample point).
5. **Conclude:** $f$ increases where $f'(x) > 0$ (or $\ge 0$), decreases where $f'(x) < 0$ (or $\le 0$).

### Trigonometric Monotonicity — Needs Domain Restriction

| Function | Interval of strict increase | Interval of strict decrease |
|---|---|---|
| $\sin x$ | $(-\pi/2, \pi/2)$ | $(\pi/2, 3\pi/2)$ |
| $\cos x$ | $(\pi, 2\pi)$ | $(0, \pi)$ |
| $\tan x$ | $(-\pi/2, \pi/2)$ | — (never decreasing on its principal domain) |
| $\cot x$ | — | $(0, \pi)$ |

> Warning: $\sin x$ is NOT monotonic on $\mathbb{R}$! You must **restrict the domain** before claiming it increases or decreases. On $(0, 2\pi)$ it rises then falls.

### Variable Reference Table

| Symbol | Meaning | Notes |
|---|---|---|
| $f(x)$ | The function under study | Real-valued, usually differentiable |
| $f'(x)$ | First derivative | Instantaneous slope |
| $I$ | Interval of interest | Open, closed, or half-open |
| $c$ | Critical point | Where $f'(c)=0$ or $f'(c)$ DNE |
| $\ge$, $>$ | Non-strict vs strict | Changes the conclusion wording |

### Special Cases Table

| Function | Derivative | Verdict |
|---|---|---|
| $f(x) = x^3$ | $3x^2 \ge 0$, zero only at $x=0$ | Strictly increasing on $\mathbb{R}$ (counterexample!) |
| $f(x) = x^2$ | $2x$; $<0$ on $(-\infty,0)$, $>0$ on $(0,\infty)$ | Decreasing then increasing |
| $f(x) = e^x$ | $e^x > 0$ always | Strictly increasing on $\mathbb{R}$ |
| $f(x) = \tan x - x$ | $\sec^2 x - 1 = \tan^2 x \ge 0$ | Strictly increasing |
| $f(x) = 2x + \cos x$ | $2 - \sin x > 0$ always | Strictly increasing |

---

## Stage 3: Type-wise Mastery

---

### Type 1: Cubic Polynomial Intervals *

**Pattern:** Given $f(x) = ax^3 + bx^2 + cx + d$, find where it increases / decreases.

**Solved Example** (Medium) — Delhi 2014 pattern

> Find the intervals in which the function $f(x) = x^3 - 6x^2 + 9x + 15$ is (i) strictly increasing, (ii) strictly decreasing.

<details><summary><b>Solution</b></summary>

**Step 1 — Differentiate:**

$$f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x-1)(x-3)$$

**Step 2 — Critical points:** $f'(x) = 0 \implies x = 1,\; x = 3$.

**Step 3 — Sign chart:**

| Interval | Test point | Sign of $(x-1)$ | Sign of $(x-3)$ | $f'(x)$ | Behaviour |
|---|---|---|---|---|---|
| $(-\infty, 1)$ | $x=0$ | $-$ | $-$ | $+$ | Increasing |
| $(1, 3)$ | $x=2$ | $+$ | $-$ | $-$ | Decreasing |
| $(3, \infty)$ | $x=4$ | $+$ | $+$ | $+$ | Increasing |

$$\boxed{\text{Strictly increasing on } (-\infty,1) \cup (3,\infty), \quad \text{strictly decreasing on } (1,3)}$$

</details>

---

**Practice Questions**

1. (Easy) Find where $f(x) = 2x^3 - 3x^2 - 12x + 5$ is increasing.

<details><summary><b>Answer</b></summary>

$$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x-2)(x+1)$$

Critical points: $x = -1, 2$.

Sign chart: $f'(x)>0$ on $(-\infty,-1)\cup(2,\infty)$, $f'(x)<0$ on $(-1,2)$.

$$\boxed{\text{Increasing on } (-\infty,-1)\cup(2,\infty),\quad \text{decreasing on } (-1,2)}$$

</details>

---

2. (Medium) Show that $f(x) = x^3 + 3x$ is strictly increasing on $\mathbb{R}$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 3x^2 + 3 = 3(x^2+1) > 0 \quad \forall x \in \mathbb{R}$$

Since $f'(x) > 0$ everywhere, $f$ is strictly increasing on $\mathbb{R}$.

$$\boxed{\text{Strictly increasing on } \mathbb{R}}$$

</details>

---

3. (Medium) Find intervals of monotonicity of $f(x) = x^3 - 3x^2 + 3x - 100$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 3x^2 - 6x + 3 = 3(x-1)^2 \ge 0$$

$f'(x) = 0$ only at $x=1$ (isolated). So $f$ is strictly increasing on $\mathbb{R}$.

$$\boxed{\text{Strictly increasing on } \mathbb{R} \text{ (this is a translated } (x-1)^3\text{)}}$$

</details>

---

4. (Hard) For $f(x) = 2x^3 - 9x^2 + 12x + 5$, find the interval where $f$ is decreasing.

<details><summary><b>Answer</b></summary>

$$f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x-1)(x-2)$$

$f'(x) < 0$ between the roots: on $(1,2)$.

$$\boxed{\text{Decreasing on } (1,2)}$$

</details>

---

5. (Hard) Find the intervals of increase and decrease of $f(x) = (x-1)^3(x-2)^2$. (All India 2011C)

<details><summary><b>Answer</b></summary>

Use product rule:

$$f'(x) = 3(x-1)^2(x-2)^2 + (x-1)^3\cdot 2(x-2) = (x-1)^2(x-2)\big[3(x-2) + 2(x-1)\big]$$

$$= (x-1)^2(x-2)(3x-6+2x-2) = (x-1)^2(x-2)(5x-8)$$

Critical points: $x = 1$ (double root), $x = 8/5 = 1.6$, $x = 2$.

Sign chart (note $(x-1)^2 \ge 0$ always):

| Interval | $(x-1)^2$ | $(x-2)$ | $(5x-8)$ | $f'(x)$ | Behaviour |
|---|---|---|---|---|---|
| $(-\infty, 1)$ | $+$ | $-$ | $-$ | $+$ | Increasing |
| $(1, 1.6)$ | $+$ | $-$ | $-$ | $+$ | Increasing |
| $(1.6, 2)$ | $+$ | $-$ | $+$ | $-$ | Decreasing |
| $(2, \infty)$ | $+$ | $+$ | $+$ | $+$ | Increasing |

$$\boxed{\text{Increasing on } (-\infty,1.6),\quad \text{decreasing on } (1.6,2),\quad \text{increasing on } (2,\infty)}$$

(At $x=1$, $f'$ touches zero but does not change sign, so monotonicity continues.)

</details>

---

### Type 2: Higher-Degree Polynomial (x⁴) *

**Pattern:** $f(x)$ of degree 4 has three critical points → four intervals.

**Solved Example** (Medium) — Delhi 2014 pattern

> Find the intervals in which $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$ is increasing or decreasing.

<details><summary><b>Solution</b></summary>

$$f'(x) = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x-2)(x+1)$$

Critical points: $x = -1,\; 0,\; 2$.

Sign chart:

| Interval | $12x$ | $(x-2)$ | $(x+1)$ | $f'(x)$ | Behaviour |
|---|---|---|---|---|---|
| $(-\infty,-1)$ | $-$ | $-$ | $-$ | $-$ | Decreasing |
| $(-1, 0)$ | $-$ | $-$ | $+$ | $+$ | Increasing |
| $(0, 2)$ | $+$ | $-$ | $+$ | $-$ | Decreasing |
| $(2, \infty)$ | $+$ | $+$ | $+$ | $+$ | Increasing |

$$\boxed{\text{Increasing on } (-1,0)\cup(2,\infty),\quad \text{decreasing on } (-\infty,-1)\cup(0,2)}$$

</details>

---

**Practice Questions**

1. (Medium) Find monotonicity intervals of $f(x) = x^4 - 4x^3$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 4x^3 - 12x^2 = 4x^2(x-3)$$

Critical points: $x=0$ (double), $x=3$.

$4x^2 \ge 0$ always. So sign of $f'$ follows $(x-3)$.

$$\boxed{\text{Decreasing on } (-\infty,0)\cup(0,3),\quad \text{increasing on } (3,\infty)}$$

(At $x=0$, no sign change — monotonicity is unbroken.)

</details>

---

2. (Hard) For $f(x) = 6 - 12x + 9x^2 - 2x^3$, find where $f$ is increasing.

<details><summary><b>Answer</b></summary>

$$f'(x) = -12 + 18x - 6x^2 = -6(x^2 - 3x + 2) = -6(x-1)(x-2)$$

$f'(x) > 0 \iff (x-1)(x-2) < 0 \iff x \in (1,2)$.

$$\boxed{\text{Increasing on } (1,2),\quad \text{decreasing on } (-\infty,1)\cup(2,\infty)}$$

</details>

---

3. (Hard) Find intervals of $f(x) = x^4/4 - x^3/3 - x^2 + 2x - 1$.

<details><summary><b>Answer</b></summary>

$$f'(x) = x^3 - x^2 - 2x + 2 = x^2(x-1) - 2(x-1) = (x-1)(x^2 - 2) = (x-1)(x-\sqrt{2})(x+\sqrt{2})$$

Critical points: $x = -\sqrt{2},\; 1,\; \sqrt{2}$.

Sign chart (positive leading coeff, three real roots): $- + - +$.

$$\boxed{\text{Decreasing on } (-\infty,-\sqrt{2})\cup(1,\sqrt{2}),\quad \text{increasing on } (-\sqrt{2},1)\cup(\sqrt{2},\infty)}$$

</details>

---

### Type 3: Factored-Form Product *

**Pattern:** $f(x)$ given as a product of powers → product-rule derivative, then sign analysis (done in Practice Q5 of Type 1; here another example).

**Solved Example** (Medium)

> Find where $f(x) = (x+1)^3 (x-2)^2$ is increasing.

<details><summary><b>Solution</b></summary>

$$f'(x) = 3(x+1)^2(x-2)^2 + (x+1)^3\cdot 2(x-2)$$

$$= (x+1)^2(x-2)\big[3(x-2) + 2(x+1)\big] = (x+1)^2(x-2)(3x-6+2x+2)$$

$$= (x+1)^2(x-2)(5x-4)$$

Critical points: $x = -1$ (double), $x = 4/5 = 0.8$, $x = 2$.

$(x+1)^2 \ge 0$ always. Sign from $(x-2)(5x-4)$:

| Interval | $(x-2)$ | $(5x-4)$ | $f'(x)$ | Behaviour |
|---|---|---|---|---|
| $(-\infty, 0.8)$ | $-$ | $-$ | $+$ | Increasing |
| $(0.8, 2)$ | $-$ | $+$ | $-$ | Decreasing |
| $(2, \infty)$ | $+$ | $+$ | $+$ | Increasing |

$$\boxed{\text{Increasing on } (-\infty,0.8)\cup(2,\infty),\quad \text{decreasing on } (0.8,2)}$$

</details>

---

**Practice Questions**

1. (Medium) Find monotonicity intervals of $f(x) = (x-2)^4 (x+1)^3$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 4(x-2)^3(x+1)^3 + (x-2)^4\cdot 3(x+1)^2 = (x-2)^3(x+1)^2\big[4(x+1)+3(x-2)\big]$$

$$= (x-2)^3(x+1)^2(7x - 2)$$

Critical points: $x=-1$ (double), $x=2/7$, $x=2$.

$(x+1)^2 \ge 0$ always. Sign from $(x-2)^3(7x-2)$:

$$\boxed{\text{Increasing on } (2/7,2)\cup(2,\infty),\quad \text{decreasing on } (-\infty,-1)\cup(-1,2/7)}$$

</details>

---

### Type 4: Trigonometric Interval *

**Pattern:** $f(x) = \sin ax - \cos ax$ etc. on $0 < x < \pi$ → express derivative, find sign sub-intervals.

**Solved Example** (Medium) — Delhi 2016 pattern

> Find the intervals in which $f(x) = \sin 3x - \cos 3x$, $0 < x < \pi$, is strictly increasing or strictly decreasing.

<details><summary><b>Solution</b></summary>

$$f'(x) = 3\cos 3x + 3\sin 3x = 3(\cos 3x + \sin 3x)$$

Set $f'(x) = 0 \implies \cos 3x + \sin 3x = 0 \implies \tan 3x = -1$.

For $0 < x < \pi \implies 0 < 3x < 3\pi$.

$\tan\theta = -1$ at $\theta = 3\pi/4,\; 7\pi/4,\; 11\pi/4$ (within $(0,3\pi)$).

So $3x = 3\pi/4,\; 7\pi/4,\; 11\pi/4 \implies x = \pi/4,\; 7\pi/12,\; 11\pi/12$.

Sign of $f'(x) = 3\sqrt{2}\sin(3x + \pi/4)$ (since $\sin\alpha+\cos\alpha = \sqrt{2}\sin(\alpha+\pi/4)$):

At $x=0^+$, $3x+\pi/4 = \pi/4$, $\sin > 0 \implies f'>0$. Pattern alternates at each root.

$$\boxed{\text{Increasing on } \left(0,\frac{\pi}{4}\right)\cup\left(\frac{7\pi}{12},\frac{11\pi}{12}\right),\quad \text{decreasing on } \left(\frac{\pi}{4},\frac{7\pi}{12}\right)\cup\left(\frac{11\pi}{12},\pi\right)}$$

</details>

---

**Practice Questions**

1. (Medium) Find where $f(x) = \sin x - \cos x$ is increasing on $(0, 2\pi)$.

<details><summary><b>Answer</b></summary>

$$f'(x) = \cos x + \sin x = \sqrt{2}\sin\left(x+\frac{\pi}{4}\right)$$

$f'(x) > 0 \iff \sin(x+\pi/4) > 0 \iff x+\pi/4 \in (0,\pi)\cup(2\pi,3\pi)$ within domain.

$x \in (-\pi/4, 3\pi/4)\cup(7\pi/4, 11\pi/4) \cap (0,2\pi) = (0,3\pi/4)\cup(7\pi/4,2\pi)$.

$$\boxed{\text{Increasing on } \left(0,\frac{3\pi}{4}\right)\cup\left(\frac{7\pi}{4},2\pi\right),\quad \text{decreasing on } \left(\frac{3\pi}{4},\frac{7\pi}{4}\right)}$$

</details>

---

2. (Medium) Show $\cos^2 x$ is decreasing on $(0, \pi/2)$.

<details><summary><b>Answer</b></summary>

$$f'(x) = -2\cos x\sin x = -\sin 2x$$

On $(0,\pi/2)$, $2x\in(0,\pi) \implies \sin 2x > 0 \implies f'(x) < 0$.

$$\boxed{\text{Strictly decreasing on } (0,\pi/2)}$$

</details>

---

3. (Hard) Find intervals of monotonicity of $f(x) = 2\sin x + \cos 2x$ on $[0, 2\pi]$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 2\cos x - 2\sin 2x = 2\cos x - 4\sin x\cos x = 2\cos x(1 - 2\sin x)$$

$f'(x)=0 \implies \cos x = 0$ or $\sin x = 1/2 \implies x = \pi/2, 3\pi/2,\; \pi/6, 5\pi/6$.

Sign chart on $[0,2\pi]$ from factors $\cos x$ and $(1-2\sin x)$:

$$\boxed{\text{Increasing on } [0,\pi/6]\cup[\pi/2,5\pi/6]\cup[3\pi/2,2\pi],\quad \text{decreasing on } [\pi/6,\pi/2]\cup[5\pi/6,3\pi/2]}$$

</details>

---

### Type 5: "Neither Increasing nor Decreasing" Proof *

**Pattern:** Function is neither on an interval → show $f'$ takes both signs, then give the actual monotonicity intervals.

**Solved Example** (Medium) — Delhi 2014C pattern

> Show that the function $f(x) = x^2 - x + 1$ is neither strictly increasing nor strictly decreasing on $(-1, 1)$. Hence find the intervals where it is increasing and decreasing.

<details><summary><b>Solution</b></summary>

$$f'(x) = 2x - 1$$

On $(-1,1)$: $f'(x) = 0$ at $x = 1/2$.

- For $x \in (-1, 1/2)$: $2x - 1 < 0 \implies f'(x) < 0$ ⇒ decreasing.
- For $x \in (1/2, 1)$: $2x - 1 > 0 \implies f'(x) > 0$ ⇒ increasing.

Since $f$ decreases on part of $(-1,1)$ and increases on another part, it is **neither strictly increasing nor strictly decreasing** on the whole interval $(-1,1)$.

$$\boxed{\text{Decreasing on } (-1, 1/2),\quad \text{increasing on } (1/2, 1)}$$

</details>

---

**Practice Questions**

1. (Medium) Show $f(x) = x^3 - 3x$ is neither increasing nor decreasing on $(-2, 2)$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$$

On $(-2,2)$: $f'(x) = 0$ at $x = \pm 1$.

$f'(x) > 0$ on $(-2,-1)\cup(1,2)$, $f'(x) < 0$ on $(-1,1)$.

Behaviour changes sign ⇒ neither on $(-2,2)$.

$$\boxed{\text{Increasing on } (-2,-1)\cup(1,2),\quad \text{decreasing on } (-1,1)}$$

</details>

---

### Type 6: Parameter-Based Monotonicity *

**Pattern:** Find $k$ such that $f$ is increasing/decreasing on a given interval → set up $f'(x) \ge 0$ (or $\le 0$) inequality in $k$, solve.

**Solved Example** (Medium)

> Find the values of $k$ for which $f(x) = kx^3 - 3x^2 + 2x + 1$ is increasing on $\mathbb{R}$.

<details><summary><b>Solution</b></summary>

$$f'(x) = 3kx^2 - 6x + 2$$

For $f$ to be increasing on $\mathbb{R}$, we need $f'(x) \ge 0$ for all $x \in \mathbb{R}$.

This is a quadratic in $x$ with leading coefficient $3k$. For it to be non-negative for all $x$:
1. Leading coefficient $> 0$: $3k > 0 \implies k > 0$.
2. Discriminant $\le 0$: $D = (-6)^2 - 4(3k)(2) = 36 - 24k \le 0 \implies 24k \ge 36 \implies k \ge 3/2$.

Both conditions: $k > 0$ and $k \ge 3/2 \implies k \ge 3/2$.

$$\boxed{k \ge \frac{3}{2}}$$

</details>

---

**Practice Questions**

1. (Medium) Find $k$ if $f(x) = 2x^3 - 3kx^2 + 6x + 5$ is increasing on $\mathbb{R}$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 6x^2 - 6kx + 6$$

For increasing on $\mathbb{R}$, $f'(x) \ge 0$ for all $x$ ⇒ leading coeff $6>0$ (OK), $D \le 0$:

$$D = 36k^2 - 4(6)(6) = 36k^2 - 144 \le 0 \implies k^2 \le 4 \implies -2 \le k \le 2$$

$$\boxed{k \in [-2, 2]}$$

</details>

---

2. (Hard) Find $k$ such that $f(x) = \frac{kx+1}{x+k}$ is decreasing on $(0,\infty)$.

<details><summary><b>Answer</b></summary>

$$f'(x) = \frac{k(x+k) - (kx+1)(1)}{(x+k)^2} = \frac{kx + k^2 - kx - 1}{(x+k)^2} = \frac{k^2 - 1}{(x+k)^2}$$

For decreasing on $(0,\infty)$, need $f'(x) < 0$ for all $x>0$ (assuming denominator positive, i.e., $x+k \neq 0$):

$$k^2 - 1 < 0 \implies -1 < k < 1$$

Also require $x+k \neq 0$ on $(0,\infty)$ ⇒ $k \ge 0$ (else $x = -k > 0$ would be excluded). With the derivative condition already $-1<k<1$, and for domain valid on all $x>0$ we need $k \ge 0$.

$$\boxed{0 \le k < 1}$$

</details>

---

### Type 7: Prove a Function Is Always Increasing/Decreasing *

**Pattern:** Show $f'(x) > 0$ (or $< 0$) for all $x$ in the domain.

**Solved Example** (Medium) — Exemplar style

> Prove that $f(x) = \tan x - x$ is strictly increasing on $(0, \pi/2)$. Hence state its behaviour on $(-\pi/2, \pi/2)$.

<details><summary><b>Solution</b></summary>

$$f'(x) = \sec^2 x - 1 = \tan^2 x$$

For $x \in (0, \pi/2)$, $\tan x > 0 \implies \tan^2 x > 0 \implies f'(x) > 0$.

Hence $f$ is strictly increasing on $(0, \pi/2)$.

On $(-\pi/2, 0)$, $\tan x < 0$ but $\tan^2 x > 0$ still, so $f'(x) > 0$ there too. At $x=0$, $f'(0)=0$.

$$\boxed{\text{Strictly increasing on } \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)\text{ (with } f'(0)=0\text{ at one point)}}$$

</details>

---

**Practice Questions**

1. (Medium) Prove $f(x) = 2x + \cos x$ is strictly increasing on $\mathbb{R}$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 2 - \sin x$$

Since $-1 \le \sin x \le 1$, we have $2 - \sin x \ge 2 - 1 = 1 > 0$ for all $x$.

$$\boxed{f'(x) > 0 \ \forall x \in \mathbb{R} \implies \text{strictly increasing on } \mathbb{R}}$$

</details>

---

2. (Hard) Prove $f(x) = x - \sin x$ is increasing on $\mathbb{R}$.

<details><summary><b>Answer</b></summary>

$$f'(x) = 1 - \cos x \ge 0 \quad (\text{since } -1 \le \cos x \le 1)$$

$f'(x) = 0$ only when $\cos x = 1$, i.e., isolated points $x = 2n\pi$. Since $f'(x) \ge 0$ everywhere and zero only at isolated points, $f$ is strictly increasing on $\mathbb{R}$.

$$\boxed{\text{Strictly increasing on } \mathbb{R}}$$

</details>

---

3. (Hard) Prove $f(x) = \log(1+x) - \frac{x}{1+x}$ is increasing on $x > 0$.

<details><summary><b>Answer</b></summary>

$$f'(x) = \frac{1}{1+x} - \frac{(1+x) - x}{(1+x)^2} = \frac{1}{1+x} - \frac{1}{(1+x)^2} = \frac{(1+x)-1}{(1+x)^2} = \frac{x}{(1+x)^2}$$

For $x > 0$, both numerator and denominator are positive ⇒ $f'(x) > 0$.

$$\boxed{\text{Strictly increasing on } (0,\infty)}$$

</details>

---

## Stage 4: MCQ Mastery

**Q1.** The function $f(x) = x^3 - 3x$ is decreasing in the interval:

(a) $(-\infty, -1)$ &emsp; (b) $(-1, 1)$ &emsp; (c) $(1, \infty)$ &emsp; (d) $(-\infty, \infty)$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $(-1, 1)$**

$f'(x) = 3x^2 - 3 = 3(x-1)(x+1) < 0$ for $x \in (-1, 1)$.

</details>

---

**Q2.** If $f'(x) > 0$ for all $x \in (a,b)$, then $f$ is:

(a) Decreasing on $(a,b)$ &emsp; (b) Strictly increasing on $(a,b)$ &emsp; (c) Constant &emsp; (d) Neither

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Strictly increasing on $(a,b)$**

Positive derivative implies strictly increasing by the monotonicity theorem.

</details>

---

**Q3.** The function $f(x) = x^3$ is:

(a) Increasing only on $(0,\infty)$ &emsp; (b) Decreasing on $(-\infty,0)$ &emsp; (c) Strictly increasing on $\mathbb{R}$ &emsp; (d) Neither

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Strictly increasing on $\mathbb{R}$**

$f'(x) = 3x^2 \ge 0$, zero only at $x=0$ (isolated). So $f$ is strictly increasing everywhere. This is the classic $x^3$ counterexample.

</details>

---

**Q4.** $\sin x$ is strictly increasing on:

(a) $(0, \pi)$ &emsp; (b) $(\pi, 2\pi)$ &emsp; (c) $(-\pi/2, \pi/2)$ &emsp; (d) $(0, 2\pi)$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) $(-\pi/2, \pi/2)$**

$\frac{d}{dx}\sin x = \cos x > 0$ on $(-\pi/2, \pi/2)$. On $(0,\pi)$ it rises then falls. Always restrict the trig domain!

</details>

---

**Q5.** The function $f(x) = e^{-x}$ is:

(a) Increasing on $\mathbb{R}$ &emsp; (b) Decreasing on $\mathbb{R}$ &emsp; (c) Constant &emsp; (d) Neither

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Decreasing on $\mathbb{R}$**

$f'(x) = -e^{-x} < 0$ for all $x$. Exponential with negative exponent falls everywhere.

</details>

---

**Q6.** (Assertion-Reason Type)

**Assertion (A):** If $f'(x) > 0$ for all $x \in (a,b)$, then $f$ is strictly increasing on $(a,b)$.

**Reason (R):** A function with $f'(x) = 0$ at one point of an interval cannot be strictly increasing on that interval.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) A is true but R is false**

A is true (standard theorem). R is **false** — the counterexample is $f(x) = x^3$, which has $f'(0)=0$ yet is strictly increasing on all of $\mathbb{R}$. A single zero of the derivative does NOT break strict monotonicity.

</details>

---

**Q7.** (Assertion-Reason Type)

**Assertion (A):** $f(x) = 2x + \cos x$ is strictly increasing on $\mathbb{R}$.

**Reason (R):** $f'(x) = 2 - \sin x > 0$ for all $x \in \mathbb{R}$.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) Both A and R are true, and R is the correct explanation of A**

$f'(x) = 2 - \sin x \ge 1 > 0$ always, which directly proves strict increase.

</details>

---

**Q8.** (Statement-based) For $f(x) = x^4 - 4x^3$, which is correct?

(a) Increasing on $(0,3)$, decreasing on $(3,\infty)$
(b) Decreasing on $(-\infty,3)$ except 0, increasing on $(3,\infty)$
(c) Increasing on $(-\infty,0)$, decreasing on $(0,3)$
(d) Decreasing everywhere

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Decreasing on $(-\infty,3)$ except 0, increasing on $(3,\infty)$**

$f'(x) = 4x^2(x-3)$. Since $4x^2 \ge 0$, sign is governed by $(x-3)$: negative for $x<3$ (including through 0, where it only touches zero), positive for $x>3$.

</details>

---

**Q9.** (Graph Interpretation) A function has $f'(x) > 0$ on $(-\infty,-2)$ and $(1,\infty)$, and $f'(x) < 0$ on $(-2,1)$. Then:

(a) local max at $x=-2$, local min at $x=1$
(b) local min at $x=-2$, local max at $x=1$
(c) increasing everywhere
(d) constant on $(-2,1)$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) local max at $x=-2$, local min at $x=1$**

$f'$ changes $+\to-$ at $-2$ ⇒ local max; $-\to+$ at $1$ ⇒ local min. (Links to Chapter 5 extrema.)

</details>

---

**Q10.** (JEE-style Trap) The condition for $f(x) = \sin x - \cos x$ to be increasing on $(0,\pi)$ is:

(a) Always increasing &emsp; (b) Increasing only on $(0, 3\pi/4)$ &emsp; (c) Increasing on $(0,3\pi/4)$ and $(7\pi/4, \pi)$ &emsp; (d) Nowhere increasing on $(0,\pi)$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) Increasing only on $(0, 3\pi/4)$** on the domain $(0,\pi)$ — note $(7\pi/4, 2\pi)$ lies outside $(0,\pi)$. A classic trap of forgetting the stated domain.

</details>

---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 1 + 5 combined

Find the intervals in which $f(x) = x^3 - 6x^2 + 9x + 15$ is increasing, and show whether it is monotonic on $(0, 4)$.

<details><summary><b>Solution</b></summary>

$$f'(x) = 3(x-1)(x-3)$$

Increasing on $(-\infty,1)\cup(3,\infty)$; decreasing on $(1,3)$.

On $(0,4)$: it decreases on $(1,3)$ and increases on $(0,1)\cup(3,4)$. So it is **not** monotonic on $(0,4)$.

$$\boxed{\text{Not monotonic on }(0,4);\ \text{increasing on }(0,1)\cup(3,4),\ \text{decreasing on }(1,3)}$$

</details>

---

**Problem 2** (Medium) — Types 4 + 6 combined

Find $k$ such that $f(x) = \sin x - kx$ is decreasing on $(0, \pi/2)$.

<details><summary><b>Solution</b></summary>

$$f'(x) = \cos x - k$$

For decreasing on $(0,\pi/2)$, need $f'(x) \le 0$ for all $x \in (0,\pi/2)$:

$$\cos x - k \le 0 \implies k \ge \cos x \quad \forall x \in (0,\pi/2)$$

The maximum of $\cos x$ on $(0,\pi/2)$ is approached as $x\to 0^+$ and equals $1$. So we need $k \ge 1$.

$$\boxed{k \ge 1}$$

</details>

---

**Problem 3** (Hard) — Types 2 + 7 combined

Prove $f(x) = \log x - x + 1$ is increasing on $(0,1)$ and decreasing on $(1,\infty)$. Hence find its maximum value.

<details><summary><b>Solution</b></summary>

$$f'(x) = \frac{1}{x} - 1 = \frac{1-x}{x}$$

For $x > 0$ (domain of $\log x$), denominator $x > 0$.

- On $(0,1)$: $1-x > 0 \implies f'(x) > 0$ ⇒ increasing.
- On $(1,\infty)$: $1-x < 0 \implies f'(x) < 0$ ⇒ decreasing.

So $f$ attains its maximum at $x=1$: $f(1) = \log 1 - 1 + 1 = 0$.

$$\boxed{\text{Max value } = 0 \text{ at } x=1}$$

</details>

---

**Problem 4** (Hard — Competency-Based) — Types 1 + 5 + 6 combined

A graphing tool plots $f(x) = x^3 + kx^2 + 3x + 2$. The manufacturer claims it is "always rising" (strictly increasing) for a certain range of $k$. Determine all such $k$.

<details><summary><b>Solution</b></summary>

$$f'(x) = 3x^2 + 2kx + 3$$

For strictly increasing on $\mathbb{R}$, need $f'(x) \ge 0$ for all $x$ (zero at isolated points allowed), with leading coeff $3>0$:

$$D = (2k)^2 - 4(3)(3) = 4k^2 - 36 \le 0 \implies k^2 \le 9 \implies -3 \le k \le 3$$

$$\boxed{k \in [-3, 3]}$$

For these $k$, $f'(x) \ge 0$ everywhere and equals zero only at isolated points, so $f$ is strictly increasing on $\mathbb{R}$.

</details>

---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE pattern]**

Find the intervals in which $f(x) = x^2 - 4x + 6$ is (i) strictly increasing, (ii) strictly decreasing.

<details><summary><b>Model Answer</b></summary>

$$f'(x) = 2x - 4 = 2(x-2)$$

$f'(x) > 0 \iff x > 2$; $f'(x) < 0 \iff x < 2$. **[2 marks]**

$$\boxed{\text{Increasing on } (2,\infty),\quad \text{decreasing on } (-\infty,2)}$$

</details>

---

**Q2. [3 marks — CBSE Board pattern]**

(a) Write the condition for a differentiable function $f$ to be strictly decreasing on an interval $I$. [1 mark]
(b) Find the intervals in which $f(x) = 2x^3 - 3x^2 - 36x + 7$ is strictly increasing. [2 marks]

<details><summary><b>Model Answer</b></summary>

**(a)** $f$ is strictly decreasing on $I$ if $f'(x) < 0$ for all $x \in I$. **[1 mark]**

**(b)** $f'(x) = 6x^2 - 6x - 36 = 6(x^2 - x - 6) = 6(x-3)(x+2)$.

$f'(x) > 0 \iff x < -2$ or $x > 3$. **[2 marks]**

$$\boxed{\text{Strictly increasing on } (-\infty,-2)\cup(3,\infty)}$$

</details>

---

**Q3. [3 marks — Exemplar-level]**

Show that $f(x) = x^3 - 3x^2 + 3x - 100$ is increasing on $\mathbb{R}$.

<details><summary><b>Model Answer</b></summary>

$$f'(x) = 3x^2 - 6x + 3 = 3(x-1)^2$$

Since $(x-1)^2 \ge 0$ for all $x$, $f'(x) \ge 0$ everywhere, and $f'(x)=0$ only at $x=1$ (isolated point). **[3 marks]**

$$\boxed{\text{Hence } f \text{ is strictly increasing on } \mathbb{R}}$$

</details>

---

**Q4. [5 marks — Long Answer]**

(a) State the condition for $f$ to be strictly increasing on $I$. [1 mark]
(b) Find the intervals in which $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$ is increasing and decreasing. [3 marks]
(c) Write one function for which $f'(c)=0$ at some point $c$ yet $f$ is strictly increasing everywhere, justifying briefly. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** $f$ is strictly increasing on $I$ if $f'(x) > 0$ for all $x \in I$. **[1 mark]**

**(b)** $f'(x) = 12x(x-2)(x+1)$. Critical points: $-1, 0, 2$.

Sign chart: $f'>0$ on $(-1,0)\cup(2,\infty)$, $f'<0$ on $(-\infty,-1)\cup(0,2)$. **[3 marks]**

$$\boxed{\text{Inc on }(-1,0)\cup(2,\infty),\ \text{dec on }(-\infty,-1)\cup(0,2)}$$

**(c)** $f(x) = x^3$: $f'(0)=0$ but $f'(x)=3x^2\ge 0$ everywhere (zero only at $0$), so $f$ is strictly increasing on $\mathbb{R}$. **[1 mark]**

</details>

---

**Q5. [4 marks — Competency-Based / Case Study] (Section E style)**

A logistics company models the **temperature** $T$ (in °C) inside a refrigerated truck over time $t$ (in hours) by

$$T(t) = \frac{1}{3}t^3 - 2t^2 + 3t + 4, \qquad t \ge 0$$

(a) Find $T'(t)$ and the critical times in the first 4 hours. [1 mark]
(b) Determine the time intervals in $(0,4)$ during which the temperature is **rising** (truck heating up) and **falling** (cooling down). [2 marks]
(c) State, with reason, whether $T(t)$ is strictly monotonic on $(0,4)$. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** $T'(t) = t^2 - 4t + 3 = (t-1)(t-3)$. Critical times: $t = 1$ h and $t = 3$ h. **[1 mark]**

**(b)** $T'(t) > 0$ on $(0,1)\cup(3,4)$ ⇒ rising; $T'(t) < 0$ on $(1,3)$ ⇒ falling. **[2 marks]**

$$\boxed{\text{Rising on }(0,1)\cup(3,4);\ \text{falling on }(1,3)}$$

**(c)** No — $T'(t)$ changes sign (positive then negative then positive), so the temperature rises, then falls, then rises again. Hence **not strictly monotonic** on $(0,4)$. **[1 mark]**

</details>

---

## Stage 7: JEE Mains Arena

**Q1.** The function $f(x) = 2x^3 - 9x^2 + 12x + 5$ is:

(a) Increasing on $(1,2)$ &emsp; (b) Decreasing on $(1,2)$ &emsp; (c) Increasing on $\mathbb{R}$ &emsp; (d) Decreasing on $\mathbb{R}$

<details><summary><b>Answer</b></summary>

**Answer: (b) Decreasing on $(1,2)$**

$f'(x) = 6(x-1)(x-2) < 0$ for $x \in (1,2)$.

</details>

---

**Q2.** Let $f(x) = x^x$ ($x>0$). On which interval is $f$ decreasing?

(a) $(0, e)$ &emsp; (b) $(0, 1/e)$ &emsp; (c) $(1/e, \infty)$ &emsp; (d) $(1, \infty)$

<details><summary><b>Answer</b></summary>

**Answer: (b) $(0, 1/e)$**

$\log f = x\log x \implies f'/f = \log x + 1 \implies f'(x) = x^x(\log x + 1)$.

$f'(x) < 0 \iff \log x + 1 < 0 \iff \log x < -1 \iff x < 1/e$.

</details>

---

**Q3.** The set of values of $k$ for which $f(x) = kx^3 - 3x^2 + 2x + 1$ is increasing on $\mathbb{R}$ is:

(a) $k \ge 3/2$ &emsp; (b) $k \le 3/2$ &emsp; (c) $k > 0$ &emsp; (d) $k \ge 1$

<details><summary><b>Answer</b></summary>

**Answer: (a) $k \ge 3/2$**

$f'(x) = 3kx^2 - 6x + 2 \ge 0\ \forall x$ requires $k>0$ and discriminant $36 - 24k \le 0 \implies k \ge 3/2$.

</details>

---

**Q4.** If $f(x) = \sin 3x - \cos 3x$, $0 < x < \pi$, the function is strictly decreasing in:

(a) $(\pi/4, 7\pi/12)$ &emsp; (b) $(0, \pi/4)$ &emsp; (c) $(7\pi/12, 11\pi/12)$ &emsp; (d) $(11\pi/12, \pi)$

<details><summary><b>Answer</b></summary>

**Answer: (a) $(\pi/4, 7\pi/12)$**

From Type 4 solved example: decreasing on $(\pi/4, 7\pi/12)$ and $(11\pi/12, \pi)$. Option (a) matches.

</details>

---

**Q5.** The function $f(x) = \frac{x}{\log x}$ ($x>1$) is increasing for:

(a) $x > e$ &emsp; (b) $1 < x < e$ &emsp; (c) $x > 1$ &emsp; (d) $x < e$

<details><summary><b>Answer</b></summary>

**Answer: (a) $x > e$**

$$f'(x) = \frac{\log x - 1}{(\log x)^2}$$

$f'(x) > 0 \iff \log x > 1 \iff x > e$.

</details>

---

*Next: [Chapter 3 — Tangents and Normals](./03_tangents_normals.md)*

---

## Quick Revision Summary

| Concept | Criterion | Key Point |
|---|---|---|
| Strictly increasing | $f'(x) > 0$ | Road always climbing |
| Increasing (non-strict) | $f'(x) \ge 0$ | Climbing or flat |
| Strictly decreasing | $f'(x) < 0$ | Road always descending |
| Decreasing (non-strict) | $f'(x) \le 0$ | Descending or flat |
| Constant | $f'(x) = 0$ | Flat road |
| Procedure | Solve $f'(x)=0$ → critical points → sign chart | Partition then test |
| $x^3$ counterexample | $f'(0)=0$ but strictly increasing | One zero doesn't break monotonicity |
| Trig | Restrict domain first | $\sin x$ not monotonic on $\mathbb{R}$ |

> The Golden Rule: Monotonicity is the **sign** of $f'(x)$. Strict vs non-strict wording decides $>$ vs $\ge$.

> The Number One Exam Trap: $f'(c)=0$ at a single point does NOT make the function non-monotonic — always check whether the sign of $f'$ actually changes across $c$.

---

> 🪤 **Common Traps — Read Before the Exam**
>
> ⚠️ **Trap 1 — Strict vs non-strict wording:** "increasing" ⇒ $f'(x)\ge 0$; "strictly increasing" ⇒ $f'(x)>0$. Match the wording to the inequality.
>
> ⚠️ **Trap 2 — Open vs closed brackets:** Intervals of increase/decrease are written with **open** brackets around critical points (since monotonicity is a property on intervals, and the derivative is zero at the critical point). Writing $[1,3]$ for a decreasing interval is technically sloppy.
>
> ⚠️ **Trap 3 — Sign-chart arithmetic:** After factoring, pick a clean test point in each sub-interval. A sign error in one factor flips the whole conclusion. Always tabulate factors separately.
>
> ⚠️ **Trap 4 — The $x^3$ counterexample:** $f'(0)=0$ does NOT imply "not strictly increasing". Check if the sign of $f'(x)$ actually changes across the point. It doesn't for $x^3$, $(x-1)^3$, etc.
>
> ⚠️ **Trap 5 — Forgetting trig domain restriction:** Never claim $\sin x$ or $\cos x$ is monotonic on all of $\mathbb{R}$. Restrict to the given interval first, then solve $f'(x)=0$ within it.
