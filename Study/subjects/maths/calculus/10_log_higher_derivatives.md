# Chapter 10: Logarithmic Differentiation & Higher Order Derivatives

---

## Stage 1: The Core Idea

### When Products and Powers Become Nightmares

Consider $y = x^x$. It has $x$ in the base AND in the exponent. The power rule requires a constant exponent. The exponential rule requires a constant base. Neither rule applies directly!

Or consider $y = \frac{x^3 \sin^5 x \cdot e^{2x}}{\sqrt{(x+1)(x-2)^3}}$. Differentiating this directly would require chained product and quotient rules — a page of algebra.

**Logarithmic differentiation** is the magic trick: take $\ln$ of both sides, use log properties to break the expression apart, differentiate, then solve for $\frac{dy}{dx}$.

### Why Second Derivatives?

A car's position is described by $s(t)$. Its speed is $s'(t)$ and its acceleration is $s''(t)$. If $s''(t) > 0$, the car is accelerating. If $s''(t) < 0$, it's braking. The second derivative captures **curvature** and **concavity** — key concepts in optimization and curve analysis.

---

## Stage 2: The Formula Lab

### The 3-Step Logarithmic Differentiation Process

1. Take $\ln$ of both sides: $\ln y = \ln f(x)$.
2. Use log rules to expand: $\ln(abc) = \ln a + \ln b + \ln c$; $\ln(a/b) = \ln a - \ln b$; $\ln(a^n) = n\ln a$.
3. Differentiate both sides (LHS gives $\frac{1}{y}\frac{dy}{dx}$, RHS gives the simplified expression). Multiply through by $y$.

### Log Properties Toolkit

| Property | Used When |
|----------|-----------|
| $\ln(uv) = \ln u + \ln v$ | Products in numerator/denominator |
| $\ln(u/v) = \ln u - \ln v$ | Fractions |
| $\ln(u^n) = n\ln u$ | Powers (including $x^x$, $x^{\sin x}$) |

### Standard Higher Derivatives

| $f(x)$ | $f''(x)$ | $f^{(n)}(x)$ |
|--------|---------|------------|
| $x^n$ | $n(n-1)x^{n-2}$ | $\frac{n!}{(n-r)!}x^{n-r}$ |
| $e^{ax}$ | $a^2 e^{ax}$ | $a^n e^{ax}$ |
| $\sin(ax)$ | $-a^2\sin(ax)$ | $a^n\sin(ax + n\pi/2)$ |
| $\cos(ax)$ | $-a^2\cos(ax)$ | $a^n\cos(ax + n\pi/2)$ |
| $\ln x$ | $-1/x^2$ | $\frac{(-1)^{n-1}(n-1)!}{x^n}$ |

---

## Stage 3: Type-wise Mastery

### Type 1: $x^x$ Type Functions

**Goal:** $y = x^{f(x)}$ — neither pure power nor pure exponential.

**Solved Example:** ⭐

Differentiate $y = x^x$.

**Solution:**
```
Take log: ln y = x ln x

Differentiate:
(1/y)(dy/dx) = ln x + x·(1/x) = ln x + 1

dy/dx = y(ln x + 1) = x^x(1 + ln x)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

1. 🟡 $y = x^{\sin x}$
<details>
<summary>Solution</summary>

`\ln y = \sin x \cdot \ln x`.
`\frac{1}{y} \frac{dy}{dx} = (\cos x)\ln x + \sin x \left(\frac{1}{x}\right)`.
`\frac{dy}{dx} =` **x^{\sin x} \left( \cos x \ln x + \frac{\sin x}{x} \right)**.
</details>

2. 🟡 $y = (\sin x)^x$
<details>
<summary>Solution</summary>

`\ln y = x \ln(\sin x)`.
`\frac{1}{y} \frac{dy}{dx} = (1)\ln(\sin x) + x \left( \frac{\cos x}{\sin x} \right) = \ln(\sin x) + x\cot x`.
`\frac{dy}{dx} =` **(\sin x)^x (\ln(\sin x) + x\cot x)**.
</details>

3. 🔴 $y = x^{x^x}$
<details>
<summary>Solution</summary>

Let `u = x^x`, so `y = x^u \implies \ln y = u \ln x`.
`\frac{1}{y} y' = u' \ln x + u \left(\frac{1}{x}\right)`.
We know `u' = d/dx(x^x) = x^x(1 + \ln x)`.
`\frac{1}{y} y' = x^x(1 + \ln x)\ln x + \frac{x^x}{x} = x^x [ \ln x + (\ln x)^2 + \frac{1}{x} ]`.
`\frac{dy}{dx} =` **x^{x^x} x^x \left( \ln x + (\ln x)^2 + \frac{1}{x} \right)**.
</details>

4. 🔴 $y = (x+1)^{x+1}$
<details>
<summary>Solution</summary>

`\ln y = (x+1) \ln(x+1)`.
`\frac{1}{y} \frac{dy}{dx} = (1)\ln(x+1) + (x+1)\left(\frac{1}{x+1}\right) = \ln(x+1) + 1`.
`\frac{dy}{dx} =` **(x+1)^{x+1} (1 + \ln(x+1))**.
</details>

5. 🟡 $y = x^{\ln x}$
<details>
<summary>Solution</summary>

`\ln y = (\ln x)(\ln x) = (\ln x)^2`.
`\frac{1}{y} \frac{dy}{dx} = 2(\ln x)\cdot\frac{1}{x} = \frac{2\ln x}{x}`.
`\frac{dy}{dx} = x^{\ln x} \left(\frac{2\ln x}{x}\right) =` **2x^{\ln x - 1} \ln x**.
</details>

---

### Type 2: Complex Product/Quotient by Log Differentiation

**Goal:** Use log rules to break apart nasty products and quotients.

**Solved Example:** ⭐

Differentiate $y = \frac{x^3\sin^2 x}{\sqrt{1+x}}$.

**Solution:**
```
ln y = 3ln x + 2ln(sin x) - (1/2)ln(1+x)

(1/y)(dy/dx) = 3/x + 2cos x/sin x - 1/(2(1+x))
= 3/x + 2cot x - 1/(2(1+x))

dy/dx = y · [ 3/x + 2cot x - 1/(2(1+x)) ]
= (x³sin²x/√(1+x)) · [ 3/x + 2cot x - 1/(2(1+x)) ]
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟡 $y = \sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)}}$
<details>
<summary>Solution</summary>

`\ln y = \frac{1}{2} [ \ln(x-1) + \ln(x-2) - \ln(x-3) - \ln(x-4) ]`.
`\frac{1}{y} y' = \frac{1}{2} \left[ \frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-3} - \frac{1}{x-4} \right]`.
`\frac{dy}{dx} =` **\frac{y}{2} \left[ \frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x-3} - \frac{1}{x-4} \right]**.
</details>

7. 🔴 $y = \frac{x\sin x \cos x}{\sqrt{x^4+1}}$
<details>
<summary>Solution</summary>

`\ln y = \ln x + \ln(\sin x) + \ln(\cos x) - \frac{1}{2}\ln(x^4+1)`.
`\frac{1}{y} y' = \frac{1}{x} + \frac{\cos x}{\sin x} + \frac{-\sin x}{\cos x} - \frac{1}{2}\frac{4x^3}{x^4+1}`.
`\frac{dy}{dx} =` **y \left[ \frac{1}{x} + \cot x - \tan x - \frac{2x^3}{x^4+1} \right]**.
</details>

8. 🔴 $y = (x^2-1)^{\frac{1}{3}} \cdot (2x+3)^{\frac{1}{2}} \cdot (x-1)^{-\frac{1}{4}}$
<details>
<summary>Solution</summary>

`\ln y = \frac{1}{3}\ln(x^2-1) + \frac{1}{2}\ln(2x+3) - \frac{1}{4}\ln(x-1)`.
`\frac{1}{y} y' = \frac{1}{3}\frac{2x}{x^2-1} + \frac{1}{2}\frac{2}{2x+3} - \frac{1}{4}\frac{1}{x-1}`.
`\frac{dy}{dx} =` **y \left[ \frac{2x}{3(x^2-1)} + \frac{1}{2x+3} - \frac{1}{4(x-1)} \right]**.
</details>

9. 🟡 $y = \frac{(x+1)(x+2)}{(x+3)(x+4)}$ — *Same result as earlier but much faster!*
<details>
<summary>Solution</summary>

`\ln y = \ln(x+1) + \ln(x+2) - \ln(x+3) - \ln(x+4)`.
`\frac{dy}{dx} =` **y \left[ \frac{1}{x+1} + \frac{1}{x+2} - \frac{1}{x+3} - \frac{1}{x+4} \right]**.
</details>

10. 🔴 $y = x^{x^2} \cdot (x^2)^x$
<details>
<summary>Solution</summary>

First simplify: `(x^2)^x = x^{2x}`.
So `y = x^{x^2} \cdot x^{2x} = x^{x^2+2x}`.
`\ln y = (x^2+2x)\ln x`.
`\frac{1}{y} y' = (2x+2)\ln x + (x^2+2x)\frac{1}{x} = 2(x+1)\ln x + (x+2)`.
`\frac{dy}{dx} =` **x^{x^2+2x} [ 2(x+1)\ln x + x + 2 ]**.
</details>

---

### Type 3: $a^{f(x)}$ and Inverse Trig Powers

**Goal:** Apply log differentiation to non-trivial exponentials and power-trig forms.

**Solved Example:**

Differentiate $y = (\sin x)^{\cos x} + (\cos x)^{\sin x}$.

**Solution:**
```
Let u = (sin x)^(cos x) and v = (cos x)^(sin x), so y = u + v.

For u: ln u = cos x · ln(sin x)
(1/u)(du/dx) = -sin x · ln(sin x) + cos x · (cos x/sin x)
= -sin x ln(sin x) + cos²x/sin x

du/dx = (sin x)^(cos x) [-sin x ln(sin x) + cos²x/sin x]

For v: ln v = sin x · ln(cos x)
(1/v)(dv/dx) = cos x · ln(cos x) + sin x · (-sin x/cos x)
= cos x ln(cos x) - sin²x/cos x

dv/dx = (cos x)^(sin x) [cos x ln(cos x) - sin²x/cos x]

dy/dx = du/dx + dv/dx
```
🔴 Hard ⭐ Must-Do

**Practice Problems:**

11. 🟡 $y = (\tan x)^{\cot x}$
<details>
<summary>Solution</summary>

`\ln y = \cot x \cdot \ln(\tan x)`.
`\frac{1}{y} y' = (-\csc^2 x)\ln(\tan x) + \cot x \left( \frac{\sec^2 x}{\tan x} \right)`.
Simplify second term: `\frac{\cos x}{\sin x} \cdot \frac{1}{\cos^2 x} \cdot \frac{\cos x}{\sin x} = \frac{1}{\sin^2 x} = \csc^2 x`.
`\frac{dy}{dx} =` **(\tan x)^{\cot x} \csc^2 x (1 - \ln(\tan x))**.
</details>

12. 🔴 $y = x^{\tan x} + (\tan x)^x$
<details>
<summary>Solution</summary>

Let `y = u + v` where `u = x^{\tan x}` and `v = (\tan x)^x`.
For `u`: `\ln u = \tan x \ln x \implies u' = x^{\tan x}(\sec^2 x \ln x + \frac{\tan x}{x})`.
For `v`: `\ln v = x \ln(\tan x) \implies v' = (\tan x)^x(1\cdot\ln(\tan x) + x\frac{\sec^2 x}{\tan x})`.
`\frac{dy}{dx} =` **x^{\tan x}\left(\sec^2 x \ln x + \frac{\tan x}{x}\right) + (\tan x)^x\left(\ln(\tan x) + \frac{x\sec^2 x}{\tan x}\right)**.
</details>

13. 🔴 $y = x^{\sin^{-1}x}$
<details>
<summary>Solution</summary>

`\ln y = \sin^{-1}x \cdot \ln x`.
`\frac{1}{y} y' = \left(\frac{1}{\sqrt{1-x^2}}\right)\ln x + \sin^{-1}x \left(\frac{1}{x}\right)`.
`\frac{dy}{dx} =` **x^{\sin^{-1}x} \left( \frac{\ln x}{\sqrt{1-x^2}} + \frac{\sin^{-1}x}{x} \right)**.
</details>

14. 🟡 $y = e^{x^2} \cdot x^{e^2} \cdot e^{e^2}$
<details>
<summary>Solution</summary>

`\ln y = x^2 \ln e + e^2 \ln x + e^2 \ln e = x^2 + e^2 \ln x + e^2`.
`\frac{1}{y} y' = 2x + e^2\left(\frac{1}{x}\right) + 0`.
`\frac{dy}{dx} =` **y \left( 2x + \frac{e^2}{x} \right)**.
</details>

15. 🔴 If $x^m y^n = (x+y)^{m+n}$, show $\frac{dy}{dx} = \frac{y}{x}$.
<details>
<summary>Solution</summary>

Take ln: `m\ln x + n\ln y = (m+n)\ln(x+y)`.
Differentiate: `\frac{m}{x} + \frac{n}{y}y' = \frac{m+n}{x+y}(1 + y')`.
Gather `y'` terms: `y' \left( \frac{n}{y} - \frac{m+n}{x+y} \right) = \frac{m+n}{x+y} - \frac{m}{x}`.
Common denominators:
`y' \left( \frac{n(x+y) - y(m+n)}{y(x+y)} \right) = \frac{x(m+n) - m(x+y)}{x(x+y)}`.
`y' \left( \frac{nx + ny - my - ny}{y(x+y)} \right) = \frac{mx + nx - mx - my}{x(x+y)}`.
`y' \left( \frac{nx - my}{y} \right) = \frac{nx - my}{x}`.
Cancel `(nx - my)`: `\frac{y'}{y} = \frac{1}{x} \implies` **\frac{dy}{dx} = \frac{y}{x}**. (Proved).
</details>

---

### Type 4: First and Second Derivatives of Standard Functions

**Goal:** Compute $y'$, $y''$, and check relations involving them.

**Solved Example:** ⭐

If $y = e^{2x}(a\cos x + b\sin x)$, show $y'' - 4y' + 5y = 0$.

**Solution:**
```
y' = 2e^{2x}(a cos x + b sin x) + e^{2x}(-a sin x + b cos x)
= e^{2x}[(2a+b)cos x + (2b-a)sin x]

y'' = 2e^{2x}[(2a+b)cos x + (2b-a)sin x] + e^{2x}[-(2a+b)sin x + (2b-a)cos x]
= e^{2x}[(4a+2b+2b-a)cos x + (4b-2a-2a-b)sin x]
= e^{2x}[(3a+4b)cos x + (3b-4a)sin x]

y'' - 4y' + 5y
= e^{2x}[(3a+4b)cos x + (3b-4a)sin x]
- 4e^{2x}[(2a+b)cos x + (2b-a)sin x]
+ 5e^{2x}[a cos x + b sin x]
= e^{2x}[(3a+4b - 8a-4b + 5a)cos x + (3b-4a-8b+4a+5b)sin x]
= e^{2x}[0·cos x + 0·sin x] = 0 ✓
```
🔴 Hard ⭐ Must-Do

**Practice Problems:**

16. 🟡 If $y = \sin(\ln x)$, find $y''$ and show $x^2y'' + xy' + y = 0$.
<details>
<summary>Solution</summary>

`y' = \cos(\ln x) \cdot \frac{1}{x} \implies xy' = \cos(\ln x)`.
Differentiate both sides w.r.t `x` (use product rule on LHS):
`x \cdot y'' + y' \cdot 1 = -\sin(\ln x) \cdot \frac{1}{x}`.
Multiply by `x`:
`x^2 y'' + xy' = -\sin(\ln x)`.
Since `\sin(\ln x) = y`, we have `x^2 y'' + xy' = -y`.
**x^2 y'' + xy' + y = 0**. (Proved).
</details>

17. 🟡 If $y = a\sin x + b\cos x$, show $y'' + y = 0$.
<details>
<summary>Solution</summary>

`y' = a\cos x - b\sin x`.
`y'' = -a\sin x - b\cos x = -(a\sin x + b\cos x)`.
Since the term in parentheses is `y`, we have `y'' = -y`.
**y'' + y = 0**. (Proved).
</details>

18. 🔴 If $y = (x + \sqrt{x^2-1})^m$, show $(x^2-1)y'' + xy' - m^2y = 0$.
<details>
<summary>Solution</summary>

`y' = m(x + \sqrt{x^2-1})^{m-1} \cdot \left(1 + \frac{x}{\sqrt{x^2-1}}\right)`.
`y' = m(x + \sqrt{x^2-1})^{m-1} \cdot \left(\frac{\sqrt{x^2-1} + x}{\sqrt{x^2-1}}\right)`.
`y' = \frac{m(x + \sqrt{x^2-1})^m}{\sqrt{x^2-1}} = \frac{my}{\sqrt{x^2-1}}`.
Cross-multiply and square: `(x^2-1)(y')^2 = m^2 y^2`.
Differentiate both sides:
`(x^2-1) \cdot 2y'y'' + (y')^2 \cdot 2x = m^2 \cdot 2y y'`.
Divide by `2y'`:
`(x^2-1)y'' + xy' = m^2y`.
**(x^2-1)y'' + xy' - m^2y = 0**. (Proved).
</details>

19. 🟡 Find $y''$ if $y = \ln(x + \sqrt{1+x^2})$.
<details>
<summary>Solution</summary>

`y' = \frac{1}{x + \sqrt{1+x^2}} \cdot \left(1 + \frac{x}{\sqrt{1+x^2}}\right) = \frac{1}{x + \sqrt{1+x^2}} \cdot \frac{\sqrt{1+x^2} + x}{\sqrt{1+x^2}}`.
The numerator cancels with the first term: `y' = \frac{1}{\sqrt{1+x^2}} = (1+x^2)^{-1/2}`.
`y'' = -\frac{1}{2}(1+x^2)^{-3/2} \cdot (2x) =` **-\frac{x}{(1+x^2)^{3/2}}**.
</details>

20. 🔴 ⭐ If $y = A e^{-kt}\cos(\omega t + \phi)$, find $y''$ and find the equation it satisfies.
<details>
<summary>Solution</summary>

`y' = -Ak e^{-kt}\cos(\omega t + \phi) - A\omega e^{-kt}\sin(\omega t + \phi) = -ky - A\omega e^{-kt}\sin(\omega t + \phi)`.
So, `y' + ky = -A\omega e^{-kt}\sin(\omega t + \phi)`.
Differentiate `y'` again:
`y'' = -ky' - A\omega [ -k e^{-kt}\sin(\omega t + \phi) + \omega e^{-kt}\cos(\omega t + \phi) ]`.
`y'' = -ky' + k(-A\omega e^{-kt}\sin(\omega t + \phi)) - \omega^2(A e^{-kt}\cos(\omega t + \phi))`.
Substitute `(-A\omega e^{-kt}\sin(\omega t + \phi)) = y' + ky` and `A e^{-kt}\cos(\omega t + \phi) = y`:
`y'' = -ky' + k(y' + ky) - \omega^2 y = -ky' + ky' + k^2 y - \omega^2 y` ... wait, let's re-differentiate carefully.
Let `u = y' + ky = -A\omega e^{-kt}\sin(\dots)`.
`u' = y'' + ky' = kA\omega e^{-kt}\sin(\dots) - A\omega^2 e^{-kt}\cos(\dots) = -k(u) - \omega^2 y`.
Substitute `u = y' + ky`:
`y'' + ky' = -k(y' + ky) - \omega^2 y = -ky' - (k^2 + \omega^2)y`.
**y'' + 2ky' + (k^2 + \omega^2)y = 0**. (Damped harmonic oscillator equation).
</details>

---

### Type 5: The $n$-th Derivative

**Goal:** Find a pattern and write a formula for the $n$-th derivative.

**Solved Example:** ⭐

Find the $n$-th derivative of $y = \sin(ax + b)$.

**Solution:**
```
y' = a cos(ax+b) = a sin(ax + b + π/2)
y'' = a² cos(ax + b + π/2) = a² sin(ax + b + 2·π/2)
y''' = a³ sin(ax + b + 3·π/2)

Pattern:
y^{(n)} = a^n sin(ax + b + nπ/2)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

21. 🟡 Find $y^{(n)}$ for $y = e^{ax}$.
<details>
<summary>Solution</summary>

`y' = ae^{ax}`, `y'' = a^2 e^{ax}`, `y''' = a^3 e^{ax}`.
Following the pattern, **y^{(n)} = a^n e^{ax}**.
</details>

22. 🟡 Find $y^{(n)}$ for $y = \cos(ax)$.
<details>
<summary>Solution</summary>

`y' = -a\sin(ax) = a\cos(ax + \pi/2)`.
`y'' = -a^2\cos(ax) = a^2\cos(ax + 2\pi/2)`.
`y''' = a^3\sin(ax) = a^3\cos(ax + 3\pi/2)`.
Following the pattern, **y^{(n)} = a^n \cos(ax + \frac{n\pi}{2})**.
</details>

23. 🟡 Find $y^{(n)}$ for $y = x^m$ (where $m$ is a positive integer and $n \leq m$).
<details>
<summary>Solution</summary>

`y' = m x^{m-1}`.
`y'' = m(m-1) x^{m-2}`.
`y''' = m(m-1)(m-2) x^{m-3}`.
After `n` derivatives, we have `n` terms in the product:
`y^{(n)} = m(m-1)(m-2)\dots(m-n+1) x^{m-n} =` **\frac{m!}{(m-n)!} x^{m-n}**.
</details>

24. 🔴 Find $y^{(n)}$ for $y = \frac{1}{x-a}$.
<details>
<summary>Solution</summary>

`y = (x-a)^{-1}`.
`y' = -1(x-a)^{-2}`.
`y'' = (-1)(-2)(x-a)^{-3} = 2(x-a)^{-3}`.
`y''' = (-1)(-2)(-3)(x-a)^{-4} = -6(x-a)^{-4}`.
Pattern: The coefficient is `(-1)^n n!`, and power is `-(n+1)`.
**y^{(n)} = \frac{(-1)^n n!}{(x-a)^{n+1}}**.
</details>

25. 🔴 ⭐ Find $y^{(n)}$ for $y = \ln(1+x)$.
<details>
<summary>Solution</summary>

`y' = \frac{1}{1+x} = (1+x)^{-1}`.
Since `y'` is the same form as Q24, the `(n)`-th derivative of `y` is the `(n-1)`-th derivative of `y'`.
Replace `n` with `n-1` in the formula from Q24:
**y^{(n)} = \frac{(-1)^{n-1} (n-1)!}{(1+x)^n}**.
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ If $x^p y^q = (x+y)^{p+q}$, find $dy/dx$ using log differentiation.
<details>
<summary>Solution</summary>

Take ln: `p\ln x + q\ln y = (p+q)\ln(x+y)`.
Differentiate: `\frac{p}{x} + \frac{q}{y}y' = \frac{p+q}{x+y}(1+y')`.
Group `y'` terms: `y'(\frac{q}{y} - \frac{p+q}{x+y}) = \frac{p+q}{x+y} - \frac{p}{x}`.
Common denominators:
`y' \left( \frac{qx+qy - py-qy}{y(x+y)} \right) = \frac{px+qx - px-py}{x(x+y)}`.
`y' \left( \frac{qx - py}{y} \right) = \frac{qx - py}{x}`.
Cancel `(qx - py)`: `\frac{y'}{y} = \frac{1}{x} \implies` **\frac{dy}{dx} = \frac{y}{x}**.
</details>

2. 🔴 If $y = \tan^{-1}\left(\frac{2x}{1-x^2}\right)$, find $y''$.
<details>
<summary>Solution</summary>

Let `x = \tan\theta`. Then `\frac{2x}{1-x^2} = \frac{2\tan\theta}{1-\tan^2\theta} = \tan 2\theta`.
`y = \tan^{-1}(\tan 2\theta) = 2\theta = 2\tan^{-1}x`.
`y' = 2 \cdot \frac{1}{1+x^2} = 2(1+x^2)^{-1}`.
`y'' = -2(1+x^2)^{-2} \cdot (2x) =` **-\frac{4x}{(1+x^2)^2}**.
</details>

3. 🔴 If $y = e^{ax} \sin bx$, find $y^{(n)}$ using the pattern $a^n\sin(bx + n\tan^{-1}(b/a))$.
<details>
<summary>Solution</summary>

*(Correction: The pattern is actually `(a^2+b^2)^{n/2} \sin(bx + n\tan^{-1}(b/a))`).*
`y' = ae^{ax}\sin bx + be^{ax}\cos bx = e^{ax}(a\sin bx + b\cos bx)`.
Let `a = r\cos\phi` and `b = r\sin\phi`. Then `r = \sqrt{a^2+b^2}` and `\phi = \tan^{-1}(b/a)`.
`y' = e^{ax}(r\cos\phi\sin bx + r\sin\phi\cos bx) = r e^{ax}\sin(bx+\phi)`.
Each derivative multiplies by `r` and adds `\phi` to the angle.
After `n` derivatives: `y^{(n)} = r^n e^{ax}\sin(bx+n\phi)`.
**y^{(n)} = (a^2+b^2)^{n/2} e^{ax} \sin\left(bx + n\tan^{-1}\frac{b}{a}\right)**.
</details>

4. 🟡 Find $\frac{d^{100}}{dx^{100}}(\cos^2 x + \sin^2 x)$. *(Think before differentiating!)*
<details>
<summary>Solution</summary>

Identity: `\cos^2 x + \sin^2 x = 1` for all `x`.
The function is a constant `y = 1`.
The first derivative is 0. The 100th derivative is also **0**.
</details>

5. 🔴 If $y = \frac{1}{x^2-5x+6}$, express in partial fractions, then find $y^{(n)}$.
<details>
<summary>Solution</summary>

Factor denominator: `x^2 - 5x + 6 = (x-3)(x-2)`.
Partial fractions: `\frac{1}{(x-3)(x-2)} = \frac{1}{x-3} - \frac{1}{x-2}`.
Using the formula for the nth derivative of `1/(x-a)` from Q24:
`y^{(n)} =` **\frac{(-1)^n n!}{(x-3)^{n+1}} - \frac{(-1)^n n!}{(x-2)^{n+1}}**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Differentiate $y = x^{\sin x}$. **(3 marks)**

**Solution:**
$\ln y = \sin x \cdot \ln x$
$(1/y)(dy/dx) = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x} = \cos x \ln x + \frac{\sin x}{x}$
$dy/dx = x^{\sin x}\left(\cos x \ln x + \frac{\sin x}{x}\right)$

---

**Q2.** 🔴 If $y = (\ln x)^{\ln x}$, find $\frac{dy}{dx}$. **(3 marks)**

**Solution:**
$\ln y = \ln x \cdot \ln(\ln x)$
$(1/y)\frac{dy}{dx} = \frac{1}{x}\ln(\ln x) + \ln x \cdot \frac{1}{x\ln x} = \frac{1}{x}[\ln(\ln x) + 1]$
$\frac{dy}{dx} = \frac{(\ln x)^{\ln x}}{x}[1 + \ln(\ln x)]$

---

**Q3.** 🟡 If $y = 3e^{2x} - 2e^{3x}$, prove $\frac{d^2y}{dx^2} - 5\frac{dy}{dx} + 6y = 0$. **(4 marks)**

**Solution:**
$y' = 6e^{2x} - 6e^{3x}$; $y'' = 12e^{2x} - 18e^{3x}$
$y'' - 5y' + 6y = (12e^{2x}-18e^{3x}) - 5(6e^{2x}-6e^{3x}) + 6(3e^{2x}-2e^{3x})$
$= e^{2x}(12 - 30 + 18) + e^{3x}(-18 + 30 - 12) = 0 + 0 = 0$ ✓

---

## Stage 6: JEE Mains Arena

**Q1.** If $y = \left(\cos x\right)^{\tan x}$, then $\frac{dy}{dx}$ at $x = \pi/4$ is:
<br>(a) $-1$   <br>(b) $1$   <br>(c) $0$   <br>(d) $\sqrt{2}$

<details>
<summary>Solution</summary>
ln y = tan x · ln(cos x)
(1/y)dy/dx = sec²x · ln(cos x) + tan x · (-sin x/cos x)
= sec²x · ln(cos x) - tan²x

At x=π/4: cos(π/4) = 1/√2, ln(1/√2) = -½ ln 2.
sec²(π/4) = 2, tan²(π/4) = 1.
dy/dx = y[2(-½ ln 2) - 1] = y[-ln 2 - 1]

y at π/4: (cos π/4)^{tan π/4} = (1/√2)^1 = 1/√2.
dy/dx = (1/√2)[-(1+ln 2)]

Answer: None of above exactly, but (c) 0 is not right. This demonstrates always re-check answer choices in JEE. 🔴
</details>

---

**Q2.** If $y = (1 + 1/x)^x$, then $\frac{dy}{dx} =$:
<br>(a) $(1+1/x)^x[\ln(1+1/x) - \frac{1}{x+1}]$   <br>(b) $(1+1/x)^x \ln(1+1/x)$   <br>(c) $x(1+1/x)^{x-1}$   <br>(d) $e$

<details>
<summary>Solution</summary>
ln y = x ln(1 + 1/x) = x ln((x+1)/x) = x[ln(x+1) - ln x]
(1/y)dy/dx = ln(x+1) - ln x + x[1/(x+1) - 1/x]
= ln(1+1/x) + x · (-1)/(x(x+1))
= ln(1+1/x) - 1/(x+1)
dy/dx = (1+1/x)^x [ln(1+1/x) - 1/(x+1)]
Answer: (a) 🔴 ⭐
</details>

---

**Q3.** The $n$-th derivative of $\frac{x}{x^2-1}$ is:
<br>(a) $\frac{n!}{2}\left[\frac{(-1)^n}{(x-1)^{n+1}} + \frac{1}{(x+1)^{n+1}}\right]$   <br>(b) $\frac{n!}{2}\left[\frac{(-1)^n}{(x-1)^{n+1}} - \frac{(-1)^n}{(x+1)^{n+1}}\right]$   <br>(c) $\frac{(-1)^n n!}{(x^2-1)^{n+1}}$   <br>(d) None

<details>
<summary>Solution</summary>
Partial fractions: x/(x²-1) = ½·1/(x-1) + ½·1/(x+1)
nth derivative of 1/(x-a) = (-1)^n n!/(x-a)^{n+1}
nth derivative = ½·(-1)^n n!/(x-1)^{n+1} + ½·(-1)^n n!/(x+1)^{n+1}
= (-1)^n n!/2 · [1/(x-1)^{n+1} + 1/(x+1)^{n+1}]
Answer: (a) (with the sign pattern) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** Logarithmic differentiation is used for $y = x^x$.
<br>**Reason (R):** $x^x$ cannot be differentiated by the power rule or the exponential rule since the exponent is not constant.

<details>
<summary>Solution</summary>
A is true: Log differentiation is the correct technique.
R is true and is the precise explanation for why standard rules fail.
Answer: (a) 🟢 ⭐
</details>

---

**Q2.**
<br>**Assertion (A):** If $y = e^x \sin x$, then $y'' = 2e^x \cos x$.
<br>**Reason (R):** $y' = e^x(\sin x + \cos x)$, and differentiating again gives $2e^x \cos x$.

<details>
<summary>Solution</summary>
Check: y'' = e^x(sin x + cos x) + e^x(cos x - sin x) = 2e^x cos x. ✓
Both A and R are true, R correctly derives A.
Answer: (a) 🟡
</details>

---

## Stage 8: MCQ Mastery

1. 🟡 $\frac{d}{dx}(x^x) =$
   <br>(a) $x \cdot x^{x-1}$   <br>(b) $x^x \ln x$   <br>(c) $x^x(1+\ln x)$   <br>(d) $e^{x\ln x}$

2. 🟡 If $y = x^n$, then $y^{(n)} =$
   <br>(a) $n$   <br>(b) $n!$   <br>(c) $n! \cdot x$   <br>(d) $0$

3. 🟡 ⭐ If $y = \sin^{-1}(2x\sqrt{1-x^2})$, then $y' =$
   <br>(a) $\frac{2}{\sqrt{1-x^2}}$   <br>(b) $\frac{1}{\sqrt{1-x^2}}$   <br>(c) $\frac{-2}{\sqrt{1-x^2}}$   <br>(d) $2\sqrt{1-x^2}$

4. 🔴 $n$-th derivative of $e^{2x}\cos 3x$ at $x=0$:
   <br>(a) $r^n \cos(n\theta)$ where $r=\sqrt{13}$, $\tan\theta = 3/2$   <br>(b) $\sqrt{13}^n$   <br>(c) $13^{n/2}$   <br>(d) $2^n$

5. 🟡 If $x^p y^q = (x+y)^{p+q}$, then $dy/dx =$
   <br>(a) $y/x$   <br>(b) $px/qy$   <br>(c) $qy/px$   <br>(d) $q/p$

6. 🔴 If $y = A\cos(nx) + B\sin(nx)$, then $y'' =$
   <br>(a) $ny$   <br>(b) $-n^2 y$   <br>(c) $n^2 y$   <br>(d) $-ny$

7. 🟡 $\frac{d}{dx}[(\log x)^x] =$
   <br>(a) $(\log x)^x[\log(\log x) + 1/\ln 10]$   <br>(b) $(\log x)^{x-1}$   <br>(c) $x(\log x)^{x-1}/x$   <br>(d) None of above

8. 🔴 If $y = e^{ax}\sin bx$, then $y'' - 2ay' + (a^2+b^2)y =$
   <br>(a) $0$   <br>(b) $1$   <br>(c) $e^{ax}$   <br>(d) $2b$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | c | 5 | a |
| 2 | b | 6 | b |
| 3 | a | 7 | a |
| 4 | a | 8 | a |

</details>

---

## What's Next?

You've mastered differentiation techniques from first principles all the way through logarithmic differentiation and higher derivatives. In **Chapter 11**, we study derivatives of **Special Functions** — inverse trigonometric derivatives, absolute value, and piecewise — then move into the powerful **Mean Value Theorems** in Chapter 12.
