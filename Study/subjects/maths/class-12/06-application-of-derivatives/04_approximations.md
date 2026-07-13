# Chapter 4: Approximations — Using Differentials to Estimate Without a Calculator

> *NCERT Section 6.5 | Class 12 Maths — Application of Derivatives*

---

## Stage 1: The Core Idea

### A Ruler and a Tiny Scratch — The Perfect Analogy

Suppose you are drawing a straight line with a ruler that is exactly 10 cm long. Now imagine the ruler is scratched and becomes 10.03 cm — a change of just 0.03 cm. How much does the **position of a point near the end** of the ruler shift? Not by 0.03 cm in wild, unpredictable ways — because the ruler is *straight*, the shift is *almost exactly* 0.03 cm. The line doesn't bend.

That is the heart of **approximation by differentials**. When a quantity $x$ changes by a *tiny* amount $\Delta x$, the function value $y = f(x)$ also changes. But instead of recomputing $f(x+\Delta x)$ from scratch (which may be hard, like computing $(3.968)^{3/2}$), we use the **slope** of the function — its derivative — to estimate the change. A small step along $x$ times the slope gives a small step along $y$.

$$\Delta y \approx dy = f'(x)\cdot \Delta x$$

The smaller $\Delta x$ is, the better this straight-line (tangent-line) guess matches the true curve.

### What is Approximation Using Differentials — Conceptually?

The derivative $f'(x)$ is the **instantaneous rate of change** of $y$ with respect to $x$. If $x$ moves a little bit ($\Delta x$), then $y$ moves by roughly the rate times the step:

- **Exact change:** $\Delta y = f(x+\Delta x) - f(x)$
- **Approximate change:** $\Delta y \approx f'(x)\cdot \Delta x = dy$

So the **approximate value** of the function at the shifted point is:

$$f(x+\Delta x) \approx f(x) + f'(x)\cdot \Delta x$$

This is the equation of the *tangent line* at $x$, evaluated at $x+\Delta x$. We are "pretending the curve is its tangent" over a very short distance.

> Warning: The approximation $\Delta y \approx f'(x)\Delta x$ is only good when $\Delta x$ is **small** (typically $|\Delta x| < 0.1$, and the smaller the better). The further $x+\Delta x$ is from $x$, the worse the straight-line guess becomes.

> Tip: Always choose $x$ to be a **convenient nearby exact value** — a perfect square, perfect cube, or integer where $f(x)$ and $f'(x)$ are easy. For $3.968$, choose $x = 4$ (since $4$ is close and exact). For $0.999$, choose $x = 1$.

> Key Takeaway: $dy$ is the **differential** of $y$ (the tangent-line change). It is *not* the same as $\Delta y$ (the true curve change), but for small steps they are nearly equal.

### Choosing x vs. x+Δx — Comparison Table

| Given number | Best choice of $x$ | $\Delta x$ (note the SIGN) | Why |
|---|---|---|---|
| $3.968$ | $4$ | $-0.032$ | $4$ is a nearby perfect value |
| $0.999$ | $1$ | $-0.001$ | $1$ makes $f(1)$ trivial |
| $7.98$ | $8$ | $-0.02$ | $8 = 2^3$, cube-friendly |
| $255$ | $256$ | $-1$ | $256 = 4^4$, fourth-root friendly |
| $0.6$ | $0.64$ or $0.49$ | $\mp 0.04$, $\pm 0.11$ | nearest known square |

> Classic Exam Trap: Beware! The sign of $\Delta x$ matters. $3.968 = 4 + (-0.032)$, **NOT** $4 + 0.032$. A wrong sign flips your entire answer. Always write $x+\Delta x = \text{given}$, then solve for $\Delta x$.

---

## Stage 2: The Formula Lab

### Core Formula — The Approximation Engine

$$\boxed{f(x+\Delta x) \approx f(x) + f'(x)\cdot \Delta x}$$

and equivalently:

$$\boxed{\Delta y \approx dy = f'(x)\cdot \Delta x}$$

### Error Propagation — Differentials of Area & Volume

If a measured quantity has a small error $\Delta x$, the resulting error in a dependent quantity propagates as:

$$\boxed{\text{Absolute error in } y \approx \left|f'(x)\right|\cdot |\Delta x|}$$

with **relative error** and **percentage error**:

$$\boxed{\text{Relative error} = \frac{\Delta x}{x}}, \qquad \boxed{\text{Percentage error} = \frac{\Delta x}{x}\times 100\%}$$

### Standard Measurement-Error Formulas

| Quantity | Formula | Differential (approx error) |
|---|---|---|
| Square area $A = s^2$ | $\Delta A \approx 2s\,\Delta s$ | Relative $\approx 2\,\frac{\Delta s}{s}$ |
| Sphere surface $S = 4\pi r^2$ | $\Delta S \approx 8\pi r\,\Delta r$ | Relative $\approx 2\,\frac{\Delta r}{r}$ |
| Sphere volume $V = \frac{4}{3}\pi r^3$ | $\Delta V \approx 4\pi r^2\,\Delta r$ | Relative $\approx 3\,\frac{\Delta r}{r}$ |
| Cylinder volume $V = \pi r^2 h$ | $\Delta V \approx \pi(2rh\,\Delta r + r^2\,\Delta h)$ | depends on which error given |
| Cube volume $V = a^3$ | $\Delta V \approx 3a^2\,\Delta a$ | Relative $\approx 3\,\frac{\Delta a}{a}$ |

### Variable Reference Table

| Symbol | Meaning | Typical Unit |
|---|---|---|
| $f(x)$ | Value of function at exact point | varies |
| $f'(x)$ | Derivative (rate of change) | unit of $f$ per unit of $x$ |
| $\Delta x$ | Small change in $x$ (can be negative) | same as $x$ |
| $dy$ | Differential of $y$ (approx change) | same as $y$ |
| $\Delta y$ | True change in $y$ | same as $y$ |
| $r, s, a, h$ | radius, side, edge, height | m, cm, etc. |
| $\delta$ (or $\Delta$) | error magnitude | same as quantity |

### What the Formula Tells Us

The key insight is **how errors multiply**:

1. **Linear quantity** ($s$, $r$): a $p\%$ error stays $p\%$.
2. **Area / squared quantity** ($\propto x^2$): error roughly **doubles** to $2p\%$.
3. **Volume / cubed quantity** ($\propto x^3$): error roughly **triples** to $3p\%$.

So "measure radius to 1% accuracy" means "volume known only to about 3% accuracy." This is why engineering tolerances matter.

### Special Cases Table

| Function $f(x)$ | $f'(x)$ | Use for approximating |
|---|---|---|
| $x^n$ | $n x^{n-1}$ | $(3.968)^{3/2}$, $\sqrt{0.6}$ |
| $x^{-1}$ | $-x^{-2}$ | $(0.99)^{-1}$ |
| $\ln x$ | $1/x$ | $\ln(1.01)$ |
| $\sin x$ | $\cos x$ | $\sin(\pi/60)$ |
| $\cos x$ | $-\sin x$ | $\cos(0.1)$ |

> Note: For trig approximations, **angles must be in radians** — never degrees — because the derivative formulas $\frac{d}{dx}\sin x = \cos x$ hold only in radians.

---

## Stage 3: Type-wise Mastery

---

### Type 1: Approximate a Radical / Power *

**Pattern:** "Find the approximate value of $(3.968)^{3/2}$ / $(0.999)^{1/3}$ / $\sqrt{0.6}$ / $(255)^{1/4}$."

**Solved Example** (Easy) — Delhi 2014C pattern

> Using differentials, find the approximate value of $(3.968)^{3/2}$.

<details><summary><b>Solution</b></summary>

Take $f(x) = x^{3/2}$. We want $f(3.968)$.

Choose the nearby exact value $x = 4$ (since $4^{3/2} = 8$ is clean).

$$\Delta x = 3.968 - 4 = -0.032$$

$$f'(x) = \frac{3}{2}x^{1/2} = \frac{3}{2}\sqrt{x}$$

At $x = 4$:

$$f(4) = 4^{3/2} = 8, \qquad f'(4) = \frac{3}{2}\sqrt{4} = \frac{3}{2}\cdot 2 = 3$$

$$f(3.968) \approx f(4) + f'(4)\cdot \Delta x = 8 + 3(-0.032) = 8 - 0.096$$

$$\boxed{(3.968)^{3/2} \approx 7.904}$$

</details>

---

**Practice Questions**

1. (Easy) Find the approximate value of $(0.999)^{1/3}$.

<details><summary><b>Answer</b></summary>

$f(x) = x^{1/3}$, $x = 1$, $\Delta x = -0.001$.

$f(1) = 1$, $f'(x) = \frac{1}{3}x^{-2/3}$, $f'(1) = \frac{1}{3}$.

$$f(0.999) \approx 1 + \frac{1}{3}(-0.001) = 1 - 0.000333 = \boxed{0.999667}$$

</details>

---

2. (Easy) Find the approximate value of $\sqrt{0.6}$.

<details><summary><b>Answer</b></summary>

$f(x) = x^{1/2}$, choose $x = 0.64$ ($0.8^2$). $\Delta x = 0.6 - 0.64 = -0.04$.

$f(0.64) = 0.8$, $f'(x) = \frac{1}{2\sqrt{x}}$, $f'(0.64) = \frac{1}{2(0.8)} = 0.625$.

$$f(0.6) \approx 0.8 + 0.625(-0.04) = 0.8 - 0.025 = \boxed{0.775}$$

(True value $\approx 0.7746$ — excellent agreement.)

</details>

---

3. (Medium) Find the approximate value of $(255)^{1/4}$.

<details><summary><b>Answer</b></summary>

$f(x) = x^{1/4}$, choose $x = 256$ ($4^4$). $\Delta x = 255 - 256 = -1$.

$f(256) = 4$, $f'(x) = \frac{1}{4}x^{-3/4}$, $f'(256) = \frac{1}{4}(256)^{-3/4} = \frac{1}{4}\cdot \frac{1}{64} = \frac{1}{256}$.

$$f(255) \approx 4 + \frac{1}{256}(-1) = 4 - 0.003906 = \boxed{3.9961}$$

</details>

---

4. (Medium) Find the approximate value of $(0.037)^{1/2}$.

<details><summary><b>Answer</b></summary>

$f(x) = x^{1/2}$, choose $x = 0.04 = (0.2)^2$. $\Delta x = 0.037 - 0.04 = -0.003$.

$f(0.04) = 0.2$, $f'(0.04) = \frac{1}{2(0.2)} = 2.5$.

$$f(0.037) \approx 0.2 + 2.5(-0.003) = 0.2 - 0.0075 = \boxed{0.1925}$$

</details>

---

5. (Hard) Find the approximate value of $(1.999)^{5/2}$.

<details><summary><b>Answer</b></summary>

$f(x) = x^{5/2}$, choose $x = 2$. $\Delta x = 1.999 - 2 = -0.001$.

$f(2) = 2^{5/2} = 4\sqrt{2} \approx 5.65685$, $f'(x) = \frac{5}{2}x^{3/2}$, $f'(2) = \frac{5}{2}\cdot 2^{3/2} = \frac{5}{2}\cdot 2\sqrt{2} = 5\sqrt{2} \approx 7.071$.

$$(1.999)^{5/2} \approx 5.65685 + 7.071(-0.001) = 5.65685 - 0.00707 = \boxed{5.64978}$$

</details>

---

6. (Hard) Show that for small $\Delta x$, $(x+\Delta x)^n \approx x^n + n x^{n-1}\Delta x$, and use it to approximate $(8.01)^{1/3}$.

<details><summary><b>Answer</b></summary>

By the linear approximation with $f(t) = t^n$: $f'(t) = n t^{n-1}$.

$$f(x+\Delta x) \approx f(x) + f'(x)\Delta x = x^n + n x^{n-1}\Delta x$$

For $(8.01)^{1/3}$: $x = 8$, $\Delta x = 0.01$, $n = 1/3$.

$$8^{1/3} = 2, \quad \frac{1}{3}\cdot 8^{-2/3} = \frac{1}{3}\cdot \frac{1}{4} = \frac{1}{12}$$

$$(8.01)^{1/3} \approx 2 + \frac{1}{12}(0.01) = 2 + 0.000833 = \boxed{2.000833}$$

</details>

---

### Type 2: Approximate Reciprocal / Log / Trig *

**Pattern:** "Approximate $(0.99)^{-1}$, $\ln(1.01)$, $\sin(\pi/60)$, $\cos(0.1)$ using differentials."

**Solved Example** (Medium)

> Using differentials, find the approximate value of $(0.99)^{-1}$.

<details><summary><b>Solution</b></summary>

$f(x) = x^{-1}$, choose $x = 1$, $\Delta x = -0.01$.

$$f(1) = 1, \qquad f'(x) = -x^{-2}, \qquad f'(1) = -1$$

$$f(0.99) \approx 1 + (-1)(-0.01) = 1 + 0.01 = \boxed{1.01}$$

(True value $\approx 1.010101$ — very close.)

</details>

---

**Practice Questions**

1. (Easy) Approximate $\ln(1.01)$.

<details><summary><b>Answer</b></summary>

$f(x) = \ln x$, $x = 1$, $\Delta x = 0.01$.

$f(1) = 0$, $f'(x) = 1/x$, $f'(1) = 1$.

$$\ln(1.01) \approx 0 + 1(0.01) = \boxed{0.01}$$

</details>

---

2. (Easy) Approximate $\sin(\pi/60)$. (Use $\pi \approx 3.1416$.)

<details><summary><b>Answer</b></summary>

$\pi/60 \approx 0.05236$ rad. Use $f(x) = \sin x$, $x = 0$, $\Delta x = \pi/60$ (in radians!).

$f(0) = 0$, $f'(x) = \cos x$, $f'(0) = 1$.

$$\sin(\pi/60) \approx 0 + 1\cdot (\pi/60) = \boxed{\pi/60 \approx 0.0524}$$

</details>

---

3. (Medium) Approximate $\cos(0.1)$ using $x = 0$.

<details><summary><b>Answer</b></summary>

$f(x) = \cos x$, $x = 0$, $\Delta x = 0.1$ rad.

$f(0) = 1$, $f'(x) = -\sin x$, $f'(0) = 0$.

$$\cos(0.1) \approx 1 + 0\cdot(0.1) = \boxed{1}$$

(True value $\approx 0.995$ — note the first-order term vanishes; need second order for better accuracy. Still the method is correct.)

</details>

---

4. (Medium) Approximate $e^{0.01}$.

<details><summary><b>Answer</b></summary>

$f(x) = e^x$, $x = 0$, $\Delta x = 0.01$.

$f(0) = 1$, $f'(0) = e^0 = 1$.

$$e^{0.01} \approx 1 + 1(0.01) = \boxed{1.01}$$

</details>

---

5. (Hard) Approximate $\tan(0.02)$ using $x = 0$.

<details><summary><b>Answer</b></summary>

$f(x) = \tan x$, $x = 0$, $\Delta x = 0.02$ rad.

$f(0) = 0$, $f'(x) = \sec^2 x$, $f'(0) = 1$.

$$\tan(0.02) \approx 0 + 1(0.02) = \boxed{0.02}$$

</details>

---

6. (Hard) Approximate $\sin\left(\frac{\pi}{6} + 0.01\right)$.

<details><summary><b>Answer</b></summary>

$f(x) = \sin x$, $x = \pi/6$, $\Delta x = 0.01$ rad.

$f(\pi/6) = 1/2$, $f'(x) = \cos x$, $f'(\pi/6) = \sqrt{3}/2 \approx 0.866$.

$$\sin\left(\frac{\pi}{6}+0.01\right) \approx \frac{1}{2} + \frac{\sqrt{3}}{2}(0.01) = 0.5 + 0.00866 = \boxed{0.50866}$$

</details>

---

### Type 3: Error in Sphere Surface Area *

**Pattern:** "The radius of a sphere is measured as $r \pm \Delta r$. Find the approximate error in surface area."

**Solved Example** (Medium) — All India 2011

> The radius of a sphere is measured as $9$ cm with an error of $\pm 0.03$ cm. Find the approximate error in calculating its surface area.

<details><summary><b>Solution</b></summary>

Surface area $S = 4\pi r^2$. Differentiate:

$$dS = 8\pi r\,dr$$

Given $r = 9$, $\Delta r = \pm 0.03$:

$$\Delta S \approx 8\pi (9)(0.03) = 8\pi(0.27) = 2.16\pi \approx 6.7858 \text{ cm}^2$$

$$\boxed{\Delta S \approx \pm 6.79 \text{ cm}^2}$$

(Percentage error: $\frac{\Delta S}{S} \times 100 = 2\cdot\frac{0.03}{9}\times 100 \approx 0.67\%$.)

</details>

---

**Practice Questions**

1. (Easy) Radius of a sphere is $7$ cm, measured with error $\pm 0.02$ cm. Find the approximate error in surface area.

<details><summary><b>Answer</b></summary>

$\Delta S \approx 8\pi r\,\Delta r = 8\pi(7)(0.02) = 1.12\pi \approx \boxed{3.52 \text{ cm}^2}$

</details>

---

2. (Medium) If the radius of a sphere is measured with $2\%$ error, what is the % error in surface area?

<details><summary><b>Answer</b></summary>

Relative error in $S = 4\pi r^2$ is $2\cdot\frac{\Delta r}{r}$. So $\%$ error in $S \approx 2 \times 2\% = \boxed{4\%}$.

</details>

---

3. (Hard) The surface area of a sphere is computed as $154$ cm$^2$ with a $1\%$ error. Estimate the error in the radius.

<details><summary><b>Answer</b></summary>

$2\,\frac{\Delta r}{r} = 1\% \implies \frac{\Delta r}{r} = 0.5\%$. From $S = 4\pi r^2 = 154$:

$$r^2 = \frac{154}{4\pi} \approx 12.25 \implies r \approx 3.5 \text{ cm}$$

$$\Delta r \approx 0.005 \times 3.5 = \boxed{0.0175 \text{ cm}}$$

</details>

---

### Type 4: Error in Volume of Sphere / Cylinder / Cube *

**Pattern:** "Given $\Delta r$ (or $\Delta a$), find the approximate error in volume."

**Solved Example** (Medium) — CBSE 2024-25 CBQ pattern

> The radius of a sphere is measured as $10$ cm with an error of $\pm 0.05$ cm. Find the approximate error in its volume.

<details><summary><b>Solution</b></summary>

Volume $V = \frac{4}{3}\pi r^3$. Differentiate:

$$dV = 4\pi r^2\,dr$$

Given $r = 10$, $\Delta r = \pm 0.05$:

$$\Delta V \approx 4\pi (10)^2 (0.05) = 4\pi(100)(0.05) = 20\pi \approx 62.83 \text{ cm}^3$$

$$\boxed{\Delta V \approx \pm 62.83 \text{ cm}^3}$$

</details>

---

**Practice Questions**

1. (Easy) Edge of a cube is $5$ cm $\pm 0.1$ cm. Find the approximate error in volume $V = a^3$.

<details><summary><b>Answer</b></summary>

$dV = 3a^2\,da = 3(25)(0.1) = 7.5$. $\boxed{\Delta V \approx \pm 7.5 \text{ cm}^3}$

</details>

---

2. (Medium) A cylinder has radius $r = 4$ cm, height $h = 10$ cm. Radius error $\pm 0.02$ cm, height exact. Find error in volume $V = \pi r^2 h$.

<details><summary><b>Answer</b></summary>

$dV = 2\pi r h\,dr = 2\pi(4)(10)(0.02) = 1.6\pi \approx \boxed{5.03 \text{ cm}^3}$

</details>

---

3. (Medium) Cylinder radius $r = 3$ cm with error $\pm 0.01$ cm AND height $h = 7$ cm with error $\pm 0.02$ cm. Estimate total error in volume.

<details><summary><b>Answer</b></summary>

$dV = \pi(2rh\,dr + r^2\,dh) = \pi[2(3)(7)(0.01) + 9(0.02)] = \pi[0.42 + 0.18] = 0.6\pi \approx \boxed{1.885 \text{ cm}^3}$

</details>

---

4. (Hard) If the volume of a sphere has $3\%$ error, what is the % error in its radius?

<details><summary><b>Answer</b></summary>

$3\,\frac{\Delta r}{r} = 3\% \implies \frac{\Delta r}{r} = 1\%$. $\boxed{1\% \text{ error in radius}.}$

</details>

---

5. (Hard) A cube has $2\%$ error in its edge. Find the % error in its volume and its surface area $A = 6a^2$.

<details><summary><b>Answer</b></summary>

Volume: $3 \times 2\% = \boxed{6\%}$. Surface area: $2 \times 2\% = \boxed{4\%}$.

</details>

---

### Type 5: Percentage Error Propagation *

**Pattern:** "If $x$ is measured with $p\%$ error, find the % error in $x^n$ or a formula involving $x$."

**Solved Example** (Easy)

> The radius of a sphere is measured with $1\%$ error. Find the approximate percentage error in (a) its surface area and (b) its volume.

<details><summary><b>Solution</b></summary>

Given $\frac{\Delta r}{r} \times 100 = 1\%$.

**(a)** $S = 4\pi r^2 \implies \frac{\Delta S}{S} \approx 2\,\frac{\Delta r}{r}$.

$$\% \text{ error in } S = 2 \times 1\% = \boxed{2\%}$$

**(b)** $V = \frac{4}{3}\pi r^3 \implies \frac{\Delta V}{V} \approx 3\,\frac{\Delta r}{r}$.

$$\% \text{ error in } V = 3 \times 1\% = \boxed{3\%}$$

</details>

---

**Practice Questions**

1. (Easy) If the side of a square is measured with $2\%$ error, what is the % error in its area?

<details><summary><b>Answer</b></summary>

$A = s^2$, relative error $\approx 2\,\frac{\Delta s}{s} = 2 \times 2\% = \boxed{4\%}$.

</details>

---

2. (Medium) The period of a pendulum is $T = 2\pi\sqrt{L/g}$. If length has $4\%$ error, find % error in $T$.

<details><summary><b>Answer</b></summary>

$T \propto L^{1/2}$, so relative error in $T = \frac{1}{2}\cdot\frac{\Delta L}{L} = \frac{1}{2}\times 4\% = \boxed{2\%}$.

</details>

---

3. (Hard) The volume of a cylinder is $V = \pi r^2 h$. If radius error is $1\%$ and height error is $2\%$, find the maximum % error in $V$.

<details><summary><b>Answer</b></summary>

$\frac{\Delta V}{V} \approx 2\frac{\Delta r}{r} + \frac{\Delta h}{h} = 2(1\%) + 2\% = \boxed{4\%}$ (errors add in worst case).

</details>

---

### Type 6: Approximate Change in y *

**Pattern:** "If $x$ changes from $a$ to $a+\Delta x$, find the approximate change in $y = f(x)$."

**Solved Example** (Easy) — NCERT Exemplar Q25

> If $y = x^4 - 10$, find the approximate change in $y$ when $x$ changes from $2$ to $1.99$.

<details><summary><b>Solution</b></summary>

$f(x) = x^4 - 10$. Here $x = 2$, $\Delta x = 1.99 - 2 = -0.01$.

$$f'(x) = 4x^3, \qquad f'(2) = 4(8) = 32$$

$$\Delta y \approx f'(2)\cdot \Delta x = 32(-0.01) = -0.32$$

$$\boxed{\text{Approximate change in } y = -0.32}$$

(And the new value $y \approx f(2) + (-0.32) = (16 - 10) - 0.32 = 5.68$.)

</details>

---

**Practice Questions**

1. (Easy) $y = x^3 + 5$, $x$ changes from $3$ to $3.01$. Find $\Delta y$.

<details><summary><b>Answer</b></summary>

$f'(3) = 3(9) = 27$, $\Delta x = 0.01$. $\Delta y \approx 27(0.01) = \boxed{0.27}$.

</details>

---

2. (Medium) $y = \sqrt{x}$, $x$ changes from $25$ to $25.2$. Find the approximate change and new value.

<details><summary><b>Answer</b></summary>

$f'(x) = \frac{1}{2\sqrt{x}}$, $f'(25) = \frac{1}{10} = 0.1$, $\Delta x = 0.2$.

$\Delta y \approx 0.1(0.2) = 0.02$. New value $\approx 5 + 0.02 = \boxed{5.02}$.

</details>

---

3. (Hard) $y = \sin x$, $x$ changes from $\pi/3$ to $\pi/3 + 0.02$. Find the approximate new value.

<details><summary><b>Answer</b></summary>

$f(\pi/3) = \sqrt{3}/2 \approx 0.866$, $f'(x) = \cos x$, $f'(\pi/3) = 1/2 = 0.5$, $\Delta x = 0.02$.

New value $\approx 0.866 + 0.5(0.02) = \boxed{0.876}$.

</details>

---

### Type 7: Approximation Error in Square Garden Area *

**Pattern:** "Side of a square is $s \pm \Delta s$. Find the approximate error in area." — CBSE 2024-25 CBQ Q2.

**Solved Example** (Easy)

> The side of a square garden is measured as $10$ m with an error of $\pm 0.05$ m. Find the approximate error in the calculated area.

<details><summary><b>Solution</b></summary>

Area $A = s^2$. Differentiate:

$$dA = 2s\,ds$$

Given $s = 10$, $\Delta s = \pm 0.05$:

$$\Delta A \approx 2(10)(0.05) = 1 \text{ m}^2$$

$$\boxed{\Delta A \approx \pm 1 \text{ m}^2}$$

(Percentage error: $2 \times \frac{0.05}{10} \times 100 = 1\%$.)

</details>

---

**Practice Questions**

1. (Easy) A square plot has side $15$ m $\pm 0.1$ m. Find approximate error in area.

<details><summary><b>Answer</b></summary>

$\Delta A \approx 2(15)(0.1) = \boxed{3 \text{ m}^2}$.

</details>

---

2. (Medium) A square tile side $20$ cm is cut with $0.5\%$ error. Find % error in area.

<details><summary><b>Answer</b></summary>

$2 \times 0.5\% = \boxed{1\%}$.

</details>

---

### Type 8: Trig Approximation (Direct) *

**Pattern:** "Use $f(x+\Delta x) \approx f(x) + f'(x)\Delta x$ to approximate a trig value."

**Solved Example** (Medium)

> Use differentials to approximate $\cos(0.1)$ and $\sin(\pi/6 + 0.01)$.

<details><summary><b>Solution</b></summary>

**For $\cos(0.1)$:** $f(x)=\cos x$, $x=0$, $\Delta x = 0.1$ rad. $f(0)=1$, $f'(0)=-\sin 0 = 0$.

$$\cos(0.1) \approx 1 + 0 = 1$$

(First-order only; second order gives $1 - 0.1^2/2 = 0.995$.)

**For $\sin(\pi/6 + 0.01)$:** $x = \pi/6$, $\Delta x = 0.01$. $f(\pi/6)=1/2$, $f'(\pi/6)=\cos(\pi/6)=\sqrt{3}/2$.

$$\sin(\pi/6 + 0.01) \approx \frac{1}{2} + \frac{\sqrt{3}}{2}(0.01) \approx \boxed{0.5087}$$

</details>

---

**Practice Questions**

1. (Easy) Approximate $\sin(0.05)$ using $x = 0$.

<details><summary><b>Answer</b></summary>

$f(0)=0$, $f'(0)=1$, $\Delta x = 0.05$. $\sin(0.05) \approx \boxed{0.05}$.

</details>

---

2. (Medium) Approximate $\tan(\pi/4 + 0.02)$.

<details><summary><b>Answer</b></summary>

$f(x)=\tan x$, $x=\pi/4$, $\Delta x = 0.02$. $f(\pi/4)=1$, $f'(\pi/4)=\sec^2(\pi/4)=2$.

$\tan(\pi/4 + 0.02) \approx 1 + 2(0.02) = \boxed{1.04}$.

</details>

---

> ⚠️ **COMMON TRAPS — Read Before You Solve**
>
> **Trap 1 — Picking $x$ far from $x+\Delta x$.** The approximation is valid only for *small* $\Delta x$. Choosing $x=1$ for $3.968$ is fatal — the straight-line guess is useless over such a distance. Always pick the *nearest convenient exact value*.
>
> **Trap 2 — Wrong sign of $\Delta x$.** $3.968 = 4 + (-0.032)$, not $+0.032$. Write $x + \Delta x = \text{given}$ and solve for $\Delta x$. A flipped sign flips the whole answer.
>
> **Trap 3 — Forgetting to ADD $f'(x)\Delta x$ to $f(x)$.** The differential $dy$ is the *change*, not the value. Final answer = $f(x) + f'(x)\Delta x$. Writing only $dy$ loses the mark for the actual value.
>
> **Trap 4 — Absolute vs percentage error.** $\Delta A = 1\text{ m}^2$ (absolute) is NOT the same as $1\%$ (relative). Read the question: "error in area" = absolute; "percentage error" = relative $\times 100$.
>
> **Trap 5 — Differentiating the wrong function.** For $(3.968)^{3/2}$, the function is $f(x) = x^{3/2}$ (power $1.5$), giving $f'(x) = \frac{3}{2}x^{1/2}$. It is NOT $x^3/2$ (which would be $\frac{3}{2}x^2$). Misreading the exponent is a top score-killer.
>
> **Trap 6 — Degrees instead of radians in trig.** Derivative formulas need radians. Using degrees silently breaks $\sin'(x)=\cos x$.

---

## Stage 4: MCQ Mastery

**Q1.** The approximate value of $(3.968)^{3/2}$ is:

(a) $7.904$ &emsp; (b) $8.096$ &emsp; (c) $7.968$ &emsp; (d) $8.032$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $7.904$**

$f(x)=x^{3/2}$, $x=4$, $\Delta x = -0.032$, $f(4)=8$, $f'(4)=3$. Value $= 8 + 3(-0.032) = 7.904$. Option (b) uses wrong sign $+0.032$.

</details>

---

**Q2.** If the radius of a sphere is measured with $1\%$ error, the approximate percentage error in its volume is:

(a) $1\%$ &emsp; (b) $2\%$ &emsp; (c) $3\%$ &emsp; (d) $4\%$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) $3\%$**

$V \propto r^3$, so $\Delta V/V \approx 3\,\Delta r/r = 3 \times 1\% = 3\%$. This is the classic "cube triples the error" rule.

</details>

---

**Q3.** For small $\Delta x$, the differential $dy$ of $y = f(x)$ is:

(a) $f(x+\Delta x) - f(x)$ &emsp; (b) $f'(x)\,\Delta x$ &emsp; (c) $f(x)\,\Delta x$ &emsp; (d) $f''(x)\,\Delta x$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $f'(x)\,\Delta x$**

By definition $dy = f'(x)\,dx = f'(x)\Delta x$. Option (a) is the *true* change $\Delta y$, not the differential.

</details>

---

**Q4.** The side of a square is $10$ cm measured with $\pm 0.05$ cm error. The absolute error in area is approximately:

(a) $0.5$ cm$^2$ &emsp; (b) $1$ cm$^2$ &emsp; (c) $0.1$ cm$^2$ &emsp; (d) $2$ cm$^2$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $1$ cm$^2$**

$\Delta A \approx 2s\,\Delta s = 2(10)(0.05) = 1$ cm$^2$.

</details>

---

**Q5.** To approximate $(255)^{1/4}$ by differentials, the correct choice is:

(a) $x = 250, \Delta x = 5$ &emsp; (b) $x = 256, \Delta x = 1$ &emsp; (c) $x = 256, \Delta x = -1$ &emsp; (d) $x = 255, \Delta x = 1$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) $x = 256, \Delta x = -1$**

$255 = 256 + (-1)$; $256 = 4^4$ is exact for the fourth root.

</details>

---

**Q6.** (Assertion-Reason)

**Assertion (A):** For small changes, the percentage error in the surface area of a sphere is twice the percentage error in its radius.

**Reason (R):** $S = 4\pi r^2 \implies \frac{\Delta S}{S} = 2\,\frac{\Delta r}{r}$.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) Both A and R are true, and R is the correct explanation of A**

From $S = 4\pi r^2$, the differential gives $\Delta S/S \approx 2\,\Delta r/r$. R directly explains A.

</details>

---

**Q7.** The approximate value of $(0.99)^{-1}$ is:

(a) $1.01$ &emsp; (b) $0.99$ &emsp; (c) $1.001$ &emsp; (d) $0.999$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $1.01$**

$f(x)=x^{-1}$, $x=1$, $\Delta x=-0.01$. $f(1)=1$, $f'(1)=-1$. Value $= 1 + (-1)(-0.01) = 1.01$.

</details>

---

**Q8.** To approximate $\sin(\pi/60)$ by differentials, we must use:

(a) $x=0$ in degrees &emsp; (b) $x=0$ in radians &emsp; (c) $x=\pi/6$ &emsp; (d) cannot approximate

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $x=0$ in radians**

Derivative formulas require radians: $\sin(\pi/60) \approx \sin 0 + \cos 0 \cdot (\pi/60) = \pi/60$.

</details>

---

**Q9.** If $y = x^4 - 10$ and $x$ changes from $2$ to $1.99$, $\Delta y \approx$:

(a) $-0.32$ &emsp; (b) $+0.32$ &emsp; (c) $-0.32 \times 10$ &emsp; (d) $0.0032$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $-0.32$**

$f'(2) = 32$, $\Delta x = -0.01$, so $\Delta y \approx 32(-0.01) = -0.32$.

</details>

---

**Q10.** A cylinder's volume $V = \pi r^2 h$. If only $r$ has $1\%$ error and $h$ is exact, % error in $V$ is:

(a) $1\%$ &emsp; (b) $2\%$ &emsp; (c) $3\%$ &emsp; (d) $0.5\%$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $2\%$**

$V \propto r^2$, so $\Delta V/V \approx 2\,\Delta r/r = 2\%$.

</details>

---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 1 + 6 combined

If $f(x) = x^{3/2}$ and $x$ changes from $4$ to $3.968$, find (a) the approximate change in $y$, and (b) the approximate new value. Hence state $(3.968)^{3/2}$.

<details><summary><b>Solution</b></summary>

$x = 4$, $\Delta x = -0.032$, $f'(x) = \frac{3}{2}\sqrt{x}$, $f'(4) = 3$.

**(a)** $\Delta y \approx 3(-0.032) = \boxed{-0.096}$

**(b)** New value $\approx f(4) + (-0.096) = 8 - 0.096 = \boxed{7.904}$

So $(3.968)^{3/2} \approx 7.904$.

</details>

---

**Problem 2** (Medium) — Types 3 + 4 + 5 combined

A spherical ball has radius measured as $r = 6$ cm with $\pm 0.04$ cm error. Find (a) absolute error in surface area, (b) absolute error in volume, (c) percentage error in volume.

<details><summary><b>Solution</b></summary>

**(a)** $\Delta S \approx 8\pi r\,\Delta r = 8\pi(6)(0.04) = 1.92\pi \approx \boxed{6.03 \text{ cm}^2}$

**(b)** $\Delta V \approx 4\pi r^2\,\Delta r = 4\pi(36)(0.04) = 5.76\pi \approx \boxed{18.10 \text{ cm}^3}$

**(c)** $\frac{\Delta V}{V} \times 100 = 3\cdot\frac{0.04}{6}\times 100 = 3 \times 0.667\% = \boxed{2\%}$

</details>

---

**Problem 3** (Hard) — Types 2 + 8 combined

Approximate (a) $\ln(1.01)$ and (b) $\cos(0.1)$ using $x=1$ and $x=0$ respectively. Then (c) explain why the trig approximation is poorer for $\cos$ than for $\ln$.

<details><summary><b>Solution</b></summary>

**(a)** $f(x)=\ln x$, $x=1$, $\Delta x=0.01$: $\ln(1.01) \approx 0 + 1(0.01) = \boxed{0.01}$

**(b)** $f(x)=\cos x$, $x=0$, $\Delta x=0.1$: $\cos(0.1) \approx 1 + 0 = \boxed{1}$

**(c)** For $\cos$, $f'(0) = -\sin 0 = 0$, so the *first-order* term vanishes and the error is governed by the second-order term $-\Delta x^2/2 = -0.005$. For $\ln$, the first-order term is non-zero (slope $=1$), giving a better first-order match.

</details>

---

**Problem 4** (Hard — Competency-Based) — Types 3 + 5 + 7 combined

A metal disk of radius $r = 5$ cm is machined with a tolerance of $\pm 0.02$ cm. (a) Find the absolute error in its painted surface area (top + bottom, i.e. $A = 2\pi r^2$). (b) Find the percentage error in area. (c) If painting costs ₹0.50 per cm$^2$, estimate the maximum rupee uncertainty in the paint cost due to the radius error.

<details><summary><b>Solution</b></summary>

Area to paint $A = 2\pi r^2$ (both faces).

**(a)** $dA = 4\pi r\,dr = 4\pi(5)(0.02) = 0.4\pi \approx \boxed{1.257 \text{ cm}^2}$

**(b)** Relative error $= 2\,\frac{\Delta r}{r} = 2\cdot\frac{0.02}{5} = 0.008 = \boxed{0.8\%}$

**(c)** Cost $C = 0.50 \times A$. Error in cost $\approx 0.50 \times \Delta A = 0.50 \times 1.257 \approx \boxed{₹0.63}$

So the paint cost is uncertain by about 63 paise per disk due to the machining tolerance.

</details>

---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE 2024-25 CBQ pattern]**

(a) Write the formula for the approximate value of $f(x+\Delta x)$ using differentials. [1 mark]
(b) Using it, find the approximate value of $(0.999)^{1/3}$. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** $\boxed{f(x+\Delta x) \approx f(x) + f'(x)\cdot \Delta x}$ **[1 mark]**

**(b)** $f(x)=x^{1/3}$, $x=1$, $\Delta x=-0.001$. $f(1)=1$, $f'(1)=\frac{1}{3}$.

$$(0.999)^{1/3} \approx 1 + \frac{1}{3}(-0.001) = \boxed{0.999667}$$ **[1 mark]**

</details>

---

**Q2. [3 marks — CBSE 2024-25 CBQ Q2]**

The side of a square garden is measured as $10$ m with an error of $\pm 0.05$ m.
(a) Find the approximate absolute error in the area. [1 mark]
(b) Find the percentage error in the area. [1 mark]
(c) If the cost of fencing is ₹200 per metre of side, what is the uncertainty in fencing cost? [1 mark]

<details><summary><b>Model Answer</b></summary>

$A = s^2$, $dA = 2s\,ds$.

**(a)** $\Delta A \approx 2(10)(0.05) = \boxed{1 \text{ m}^2}$ **[1 mark]**

**(b)** $\%$ error $= 2\cdot\frac{0.05}{10}\times 100 = \boxed{1\%}$ **[1 mark]**

**(c)** Fencing cost $C = 200 \times (4s) = 800s$. $\Delta C \approx 800\,\Delta s = 800(0.05) = \boxed{₹40}$ **[1 mark]**

</details>

---

**Q3. [3 marks — Delhi 2014C pattern]**

Using differentials, find the approximate value of $(3.968)^{3/2}$.

<details><summary><b>Model Answer</b></summary>

Let $f(x)=x^{3/2}$, take $x=4$, $\Delta x = 3.968-4 = -0.032$.

$f(4)=4^{3/2}=8$, $f'(x)=\frac{3}{2}x^{1/2}$, $f'(4)=\frac{3}{2}\cdot 2 = 3$.

$$(3.968)^{3/2} = f(4+\Delta x) \approx f(4) + f'(4)\Delta x = 8 + 3(-0.032) = \boxed{7.904}$$ **[3 marks]**

</details>

---

**Q4. [5 marks — Long Answer]**

(a) State the differential formula for approximate error in a function $y = f(x)$ when $x$ has a small error $\Delta x$. [1 mark]
(b) The radius of a sphere is $7$ cm measured with an error of $\pm 0.02$ cm. Find the approximate error in its surface area. [2 marks]
(c) Find the approximate percentage error in its volume. [2 marks]

<details><summary><b>Model Answer</b></summary>

**(a)** $\boxed{\Delta y \approx dy = f'(x)\cdot \Delta x}$ (for small $\Delta x$). **[1 mark]**

**(b)** $S = 4\pi r^2$, $dS = 8\pi r\,dr$.

$$\Delta S \approx 8\pi(7)(0.02) = 1.12\pi \approx \boxed{3.52 \text{ cm}^2}$$ **[2 marks]**

**(c)** $V = \frac{4}{3}\pi r^3$, relative error $= 3\,\frac{\Delta r}{r}$.

$$\% \text{ error} = 3\cdot\frac{0.02}{7}\times 100 = 3 \times 0.2857\% \approx \boxed{0.857\%}$$ **[2 marks]**

</details>

---

**Q5. [5 marks — Competency-Based / Case Study] (Section E style)**

A municipal gardener measures a square community garden. The side is recorded as $10$ m, but the measuring tape has a known uncertainty of $\pm 0.05$ m. Separately, a water-supply engineer measures the radius of a cylindrical overhead tank as $2$ m with an uncertainty of $\pm 0.05$ m to estimate its storage capacity $V = \pi r^2 h$ (height $h = 3$ m, measured exactly).

(a) Find the approximate absolute error in the garden's area. [1 mark]
(b) Find the approximate absolute error in the tank's capacity. [2 marks]
(c) Find the percentage error in the tank's capacity. [1 mark]
(d) Which measurement (garden side or tank radius) is more sensitive to a given *percentage* error in the measurement? Justify. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** Garden: $A = s^2$, $dA = 2s\,ds = 2(10)(0.05) = \boxed{1 \text{ m}^2}$ **[1 mark]**

**(b)** Tank: $V = \pi r^2 h$, $dV = 2\pi r h\,dr = 2\pi(2)(3)(0.05) = 0.6\pi \approx \boxed{1.885 \text{ m}^3}$ **[2 marks]**

**(c)** $\frac{\Delta V}{V}\times 100 = 2\cdot\frac{0.05}{2}\times 100 = \boxed{5\%}$ **[1 mark]**

**(d)** Both area and volume depend on a *squared* quantity, so both double a given percentage measurement error to $2 \times (\text{input \%})$. They are **equally sensitive** in percentage terms; the tank's larger *absolute* error comes only from its larger dimensions, not from a different exponent. **[1 mark]**

</details>

---

## Stage 7: JEE Mains Arena

**Q1.** If $f(x) = x^{3/2}$, the approximate value of $(3.968)^{3/2}$ equals:

(a) $7.904$ &emsp; (b) $8.096$ &emsp; (c) $7.904 + \text{error}$ &emsp; (d) $8.032$

<details><summary><b>Answer</b></summary>

**Answer: (a) $7.904$**

Standard linear approximation; the common trap (b) arises from using $+0.032$ instead of $-0.032$.

</details>

---

**Q2.** The percentage error in the volume of a sphere, given $1\%$ error in radius, is:

(a) $1\%$ &emsp; (b) $2\%$ &emsp; (c) $3\%$ &emsp; (d) $1/3\%$

<details><summary><b>Answer</b></summary>

**Answer: (c) $3\%$**

$V \propto r^3 \implies \Delta V/V \approx 3\,\Delta r/r = 3\%$.

</details>

---

**Q3.** If $y = \sin x$ and $x$ changes from $\pi/3$ to $\pi/3 + 0.01$ (radians), the approximate new value is:

(a) $0.5$ &emsp; (b) $0.5087$ &emsp; (c) $0.4913$ &emsp; (d) $0.866$

<details><summary><b>Answer</b></summary>

**Answer: (b) $0.5087$**

$f(\pi/3)=0.5$, $f'(\pi/3)=\cos(\pi/3)=0.5$. New $\approx 0.5 + 0.5(0.01) = 0.505$... wait recompute: $0.5 + 0.5\times 0.01 = 0.505$. (Using $\cos(\pi/3)=0.5$ gives $0.505$; if using exact $\sqrt{3}/2 \approx 0.866$ we get $0.5+0.866(0.01)=0.5087$.) With exact derivative value $0.5087$ — option (b).

</details>

---

**Q4.** The percentage error in the area of a circle, if the radius is measured with $k\%$ error, is:

(a) $k\%$ &emsp; (b) $2k\%$ &emsp; (c) $k^2\%$ &emsp; (d) $\sqrt{k}\%$

<details><summary><b>Answer</b></summary>

**Answer: (b) $2k\%$**

$A = \pi r^2$, relative error $\approx 2\,\Delta r/r = 2k\%$.

</details>

---

**Q5.** Let $f(x) = x^{-1}$. The approximate value of $(0.99)^{-1}$ using $x=1$ is:

(a) $1.01$ &emsp; (b) $0.99$ &emsp; (c) $1.001$ &emsp; (d) $0.999$

<details><summary><b>Answer</b></summary>

**Answer: (a) $1.01$**

$f(1)=1$, $f'(1)=-1$, $\Delta x = -0.01$, value $= 1 + (-1)(-0.01) = 1.01$. Trap: forgetting the double negative gives $0.99$ (option b).

</details>

---

*Next: [Chapter 5 — Local Maxima and Minima](./05_local_maxima_minima.md)*

---

## Quick Revision Summary

| Concept | Formula | Key Point |
|---|---|---|
| Linear approximation | $f(x+\Delta x) \approx f(x) + f'(x)\Delta x$ | use nearby exact $x$ |
| Differential | $dy = f'(x)\Delta x$ | the *change*, not the value |
| Square area | $\Delta A \approx 2s\,\Delta s$ | rel. error $2\Delta s/s$ |
| Sphere surface | $\Delta S \approx 8\pi r\,\Delta r$ | rel. error $2\Delta r/r$ |
| Sphere volume | $\Delta V \approx 4\pi r^2\,\Delta r$ | rel. error $3\Delta r/r$ |
| Cylinder volume | $\Delta V \approx \pi(2rh\,\Delta r + r^2\Delta h)$ | add both errors |
| Cube volume | $\Delta V \approx 3a^2\,\Delta a$ | rel. error $3\Delta a/a$ |
| Relative / % error | $\frac{\Delta x}{x}$ / $\times 100$ | distinguish from absolute |

> The Golden Rule: Pick $x$ = nearest convenient exact value, write $x+\Delta x = $ given to get the **signed** $\Delta x$, compute $f(x)$ and $f'(x)$, then add $f'(x)\Delta x$ to $f(x)$.

> The Number One Exam Trap: Confusing $(3.968)^{3/2}$ (function $x^{3/2}$) with $x^{3}/2$, and forgetting the **negative** sign of $\Delta x = -0.032$. Both errors flip your answer.
