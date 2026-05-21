# Chapter 9: Implicit & Parametric Differentiation

---

## Stage 1: The Core Idea

### When You Can't Solve for y

The equation of a circle: $x^2 + y^2 = 25$.

You can try to write $y = \sqrt{25 - x^2}$. But this only gives the top half of the circle. And differentiating it requires a chain rule tangle. Worse, for many curves like $x^3 + y^3 = 3xy$ (the Folium of Descartes), you simply **cannot** write $y$ as an explicit function of $x$.

**Implicit differentiation** bypasses this problem entirely. Instead of isolating $y$ first, you differentiate both sides of the equation with respect to $x$, treating $y$ as a function of $x$ (using the chain rule), and then solve for $\frac{dy}{dx}$.

### The Parametric Idea

A roller coaster doesn't have a simple $y = f(x)$ equation. Its position is given separately: $x = $ (horizontal position at time $t$), $y = $ (vertical position at time $t$). Both $x$ and $y$ are functions of a third variable $t$ (the **parameter**).

When $x = f(t)$ and $y = g(t)$, we use the chain rule:
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}$$

---

## Stage 2: The Formula Lab

### Implicit Differentiation — Rules

When differentiating an equation in $x$ and $y$:

| Expression | Derivative w.r.t. $x$ | Why? |
|-----------|----------------------|------|
| $f(x)$ | $f'(x)$ | Normal differentiation |
| $f(y)$ | $f'(y) \cdot \frac{dy}{dx}$ | Chain rule: $y$ is a function of $x$ |
| $x^n$ | $nx^{n-1}$ | Normal power rule |
| $y^n$ | $ny^{n-1} \frac{dy}{dx}$ | Power rule + chain rule |
| $xy$ | $y + x\frac{dy}{dx}$ | Product rule |
| $x^2y^3$ | $2xy^3 + 3x^2y^2 \frac{dy}{dx}$ | Product rule + chain rule |

**Golden Rule:** Every time you differentiate $y$ (or any expression involving $y$), **multiply by $\frac{dy}{dx}$**.

### Parametric Differentiation — Formulae

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} \quad \text{(provided } dx/dt \neq 0 \text{)}$$

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

---

## Stage 3: Type-wise Mastery

### Type 1: Basic Implicit Differentiation

**Goal:** Differentiate both sides, collect $\frac{dy}{dx}$ terms, solve.

**Solved Example:** ⭐

Find $\frac{dy}{dx}$ if $x^2 + y^2 = a^2$.

**Solution:**
```
Differentiate both sides w.r.t. x:
d/dx(x²) + d/dx(y²) = d/dx(a²)
2x + 2y(dy/dx) = 0
2y(dy/dx) = -2x
dy/dx = -x/y
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

1. 🟢 $x^3 + y^3 = 8$
<details>
<summary>Solution</summary>

Differentiate w.r.t `x`:
`3x^2 + 3y^2 \frac{dy}{dx} = 0`.
`3y^2 \frac{dy}{dx} = -3x^2 \implies` **\frac{dy}{dx} = -\frac{x^2}{y^2}**.
</details>

2. 🟡 $x^2 + xy + y^2 = 1$
<details>
<summary>Solution</summary>

`d/dx(x^2) + d/dx(xy) + d/dx(y^2) = 0`.
`2x + (y + x\frac{dy}{dx}) + 2y\frac{dy}{dx} = 0`.
Group `dy/dx` terms: `(x + 2y)\frac{dy}{dx} = -2x - y`.
**\frac{dy}{dx} = -\frac{2x + y}{x + 2y}**.
</details>

3. 🟡 ⭐ $\sin(x + y) = y^2 \cos x$
<details>
<summary>Solution</summary>

Differentiate using chain and product rules:
`\cos(x+y) \cdot (1 + \frac{dy}{dx}) = (2y\frac{dy}{dx})\cos x + y^2(-\sin x)`.
Expand LHS: `\cos(x+y) + \cos(x+y)\frac{dy}{dx} = 2y\cos x\frac{dy}{dx} - y^2\sin x`.
Group `dy/dx` terms: `\cos(x+y)\frac{dy}{dx} - 2y\cos x\frac{dy}{dx} = -y^2\sin x - \cos(x+y)`.
`\frac{dy}{dx}[\cos(x+y) - 2y\cos x] = -y^2\sin x - \cos(x+y)`.
**\frac{dy}{dx} = \frac{y^2\sin x + \cos(x+y)}{2y\cos x - \cos(x+y)}**.
</details>

4. 🟡 $e^x + e^y = e^{x+y}$
<details>
<summary>Solution</summary>

`e^x + e^y \frac{dy}{dx} = e^{x+y} (1 + \frac{dy}{dx})`.
`e^x + e^y \frac{dy}{dx} = e^{x+y} + e^{x+y}\frac{dy}{dx}`.
`(e^y - e^{x+y})\frac{dy}{dx} = e^{x+y} - e^x`.
Notice from the original equation that `e^{x+y} - e^x = e^y`, and `e^y - e^{x+y} = -e^x`.
Substitute these back: `(-e^x)\frac{dy}{dx} = e^y`.
**\frac{dy}{dx} = -e^{y-x}**.
</details>

5. 🔴 $x^y = y^x$ — *Take log both sides first.*
<details>
<summary>Solution</summary>

Take ln: `y \ln x = x \ln y`.
Differentiate (product rule on both sides):
`\frac{dy}{dx} \ln x + y(\frac{1}{x}) = 1 \cdot \ln y + x(\frac{1}{y} \frac{dy}{dx})`.
`\frac{dy}{dx} \ln x - \frac{x}{y}\frac{dy}{dx} = \ln y - \frac{y}{x}`.
`\frac{dy}{dx} \left( \frac{y\ln x - x}{y} \right) = \frac{x\ln y - y}{x}`.
**\frac{dy}{dx} = \frac{y(x\ln y - y)}{x(y\ln x - x)}**.
</details>

---

### Type 2: Implicit Differentiation with Product Terms

**Goal:** Use product rule when both $x$ and $y$ terms appear multiplied.

**Solved Example:** ⭐

Find $\frac{dy}{dx}$ for $x^2y + xy^2 = 6$.

**Solution:**
```
Differentiate:
d/dx(x²y) + d/dx(xy²) = 0

For x²y: product rule → 2xy + x²(dy/dx)
For xy²: product rule → y² + x·2y(dy/dx)

2xy + x²(dy/dx) + y² + 2xy(dy/dx) = 0

Collect dy/dx terms:
(x² + 2xy)(dy/dx) = -2xy - y²

dy/dx = -(2xy + y²)/(x² + 2xy) = -y(2x+y)/(x(x+2y))
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟡 $x^3 + y^3 = 3xy$ (Folium of Descartes)
<details>
<summary>Solution</summary>

`3x^2 + 3y^2 y' = 3(y + xy')`.
Divide by 3: `x^2 + y^2 y' = y + xy'`.
`y^2 y' - xy' = y - x^2`.
`y'(y^2 - x) = y - x^2 \implies` **\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}**.
</details>

7. 🟡 $xy = \tan^{-1}(y/x)$
<details>
<summary>Solution</summary>

LHS: `y + xy'`.
RHS: `\frac{1}{1 + (y/x)^2} \cdot \frac{y'x - y}{x^2} = \frac{x^2}{x^2+y^2} \cdot \frac{xy'-y}{x^2} = \frac{xy'-y}{x^2+y^2}`.
So `y + xy' = \frac{xy'-y}{x^2+y^2}`.
Multiply out: `y(x^2+y^2) + xy'(x^2+y^2) = xy' - y`.
`xy'(x^2+y^2) - xy' = -y - y(x^2+y^2)`.
`xy'(x^2+y^2-1) = -y(x^2+y^2+1)`.
**\frac{dy}{dx} = -\frac{y(x^2+y^2+1)}{x(x^2+y^2-1)}**.
</details>

8. 🔴 $\sin(xy) = \ln(x+y)$
<details>
<summary>Solution</summary>

`\cos(xy) \cdot (y + xy') = \frac{1}{x+y} \cdot (1 + y')`.
`y\cos(xy) + xy'\cos(xy) = \frac{1}{x+y} + \frac{y'}{x+y}`.
`xy'\cos(xy) - \frac{y'}{x+y} = \frac{1}{x+y} - y\cos(xy)`.
Multiply by `x+y`: `y'[x(x+y)\cos(xy) - 1] = 1 - y(x+y)\cos(xy)`.
**\frac{dy}{dx} = \frac{1 - y(x+y)\cos(xy)}{x(x+y)\cos(xy) - 1}**.
</details>

9. 🔴 $e^{xy} + \ln(y/x) = 2$
<details>
<summary>Solution</summary>

Rewrite log: `e^{xy} + \ln y - \ln x = 2`.
`e^{xy}(y + xy') + \frac{y'}{y} - \frac{1}{x} = 0`.
`y e^{xy} + xy' e^{xy} + \frac{y'}{y} = \frac{1}{x}`.
`y' (x e^{xy} + 1/y) = 1/x - y e^{xy}`.
Multiply by `xy`: `y' (x^2 y e^{xy} + x) = y - xy^2 e^{xy}`.
**\frac{dy}{dx} = \frac{y - xy^2 e^{xy}}{x + x^2 y e^{xy}}**.
</details>

10. 🔴 $\tan^{-1}\left(\frac{x+y}{x-y}\right) = c$ (constant)
<details>
<summary>Solution</summary>

Don't differentiate yet! Move `\tan^{-1}`:
`\frac{x+y}{x-y} = \tan c = k` (where `k` is a constant).
`x + y = k(x - y) \implies x + y = kx - ky`.
Gather terms: `y(1 + k) = x(k - 1) \implies y = \left(\frac{k-1}{k+1}\right)x`.
This is a straight line passing through the origin `y = mx`.
Thus `y' = m = y/x`.
**\frac{dy}{dx} = \frac{y}{x}**.
</details>

---

### Type 3: Finding the Tangent Using Implicit Differentiation

**Goal:** Find slope at a specific point using implicit differentiation, then write equation of tangent.

**Solved Example:** ⭐

Find the equation of tangent to $x^2 + y^2 = 25$ at $(3, 4)$.

**Solution:**
```
From Type 1: dy/dx = -x/y

At (3,4): slope = -3/4

Tangent: y - 4 = (-3/4)(x - 3)
4(y - 4) = -3(x - 3)
4y - 16 = -3x + 9
3x + 4y = 25
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

11. 🟡 Find tangent to $x^2/9 + y^2/16 = 1$ at $(3, 0)$.
<details>
<summary>Solution</summary>

`\frac{2x}{9} + \frac{2y y'}{16} = 0 \implies y' = -\frac{16x}{9y}`.
At `(3, 0)`, denominator is `0` and numerator is `-48`. Slope is undefined (vertical).
Tangent line is vertical passing through `x=3`.
**Equation: x = 3**.
</details>

12. 🟡 Find tangent to $x^3 + y^3 = 9$ at $(1, 2)$.
<details>
<summary>Solution</summary>

`3x^2 + 3y^2 y' = 0 \implies y' = -x^2/y^2`.
At `(1, 2)`, slope `m = -1^2 / 2^2 = -1/4`.
Tangent: `y - 2 = -1/4 (x - 1) \implies 4y - 8 = -x + 1`.
**Equation: x + 4y = 9**.
</details>

13. 🔴 Find all points on $x^2 + y^2 = 4$ where the tangent is parallel to $y = x$.
<details>
<summary>Solution</summary>

Slope of `y = x` is `1`. We want `y' = 1`.
Differentiate circle: `2x + 2y y' = 0 \implies y' = -x/y`.
Set `-x/y = 1 \implies y = -x`.
Substitute back into circle eq: `x^2 + (-x)^2 = 4 \implies 2x^2 = 4 \implies x^2 = 2 \implies x = \pm\sqrt{2}`.
If `x = \sqrt{2}`, `y = -\sqrt{2}`. If `x = -\sqrt{2}`, `y = \sqrt{2}`.
**Points: (\sqrt{2}, -\sqrt{2}) and (-\sqrt{2}, \sqrt{2})**.
</details>

14. 🔴 For the curve $x^{2/3} + y^{2/3} = a^{2/3}$, show the tangent at any point $(x_1, y_1)$ satisfies $\frac{x-x_1}{y^{1/3}_1} + \frac{y-y_1}{x^{1/3}_1} = 0$.
<details>
<summary>Solution</summary>

Wait, there is a small typo in the problem statement, let's derive it:
`\frac{2}{3}x^{-1/3} + \frac{2}{3}y^{-1/3}y' = 0 \implies y' = -\frac{y^{1/3}}{x^{1/3}}`.
At `(x_1, y_1)`, slope is `-\frac{y_1^{1/3}}{x_1^{1/3}}`.
Tangent eq: `y - y_1 = -\frac{y_1^{1/3}}{x_1^{1/3}} (x - x_1)`.
Divide both sides by `y_1^{1/3}`:
`\frac{y - y_1}{y_1^{1/3}} = -\frac{x - x_1}{x_1^{1/3}}`.
Move to one side:
**\frac{x - x_1}{x_1^{1/3}} + \frac{y - y_1}{y_1^{1/3}} = 0**. (Proved).
</details>

15. 🟡 ⭐ Prove that for $xy = c^2$, the sub-tangent and sub-normal at any point are equal in magnitude.
<details>
<summary>Solution</summary>

*(Note: There is a typo in the classic problem statement here, it usually asks to prove subtangent varies as abscissa. Let's find both anyway.)*
`xy = c^2 \implies y + xy' = 0 \implies y' = -y/x`.
Sub-tangent `= |y / y'| = |y / (-y/x)| = |-x| = |x|`. (It equals the x-coordinate).
Sub-normal `= |y \cdot y'| = |y(-y/x)| = |-y^2/x|`.
They are NOT equal in general, they are only equal where `|x| = |y^2/x| \implies x^2 = y^2`.
*(The intended problem was likely: "Show that the sub-tangent varies as the abscissa," which is true since Sub-tangent = |x|).*
</details>

---

### Type 4: Basic Parametric Differentiation

**Goal:** Find $\frac{dy}{dx}$ when $x = f(t)$ and $y = g(t)$.

**Solved Example:** ⭐

Find $\frac{dy}{dx}$ if $x = a\cos t$, $y = b\sin t$.

**Solution:**
```
dx/dt = -a sin t
dy/dt = b cos t

dy/dx = (dy/dt)/(dx/dt) = (b cos t)/(-a sin t) = -b cot t / a
= -(b/a) cot t
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

16. 🟢 $x = at^2$, $y = 2at$ (parabola)
<details>
<summary>Solution</summary>

`dx/dt = 2at`, `dy/dt = 2a`.
`\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{2a}{2at} =` **\frac{1}{t}**.
</details>

17. 🟡 $x = a(\theta - \sin\theta)$, $y = a(1-\cos\theta)$ (cycloid)
<details>
<summary>Solution</summary>

`dx/d\theta = a(1 - \cos\theta)`. `dy/d\theta = a\sin\theta`.
`\frac{dy}{dx} = \frac{a\sin\theta}{a(1 - \cos\theta)} = \frac{2\sin(\theta/2)\cos(\theta/2)}{2\sin^2(\theta/2)} =` **\cot(\theta/2)**.
</details>

18. 🟡 $x = \frac{2t}{1+t^2}$, $y = \frac{1-t^2}{1+t^2}$
<details>
<summary>Solution</summary>

Method 1 (Substitution): Let `t = \tan \alpha`. Then `x = \sin 2\alpha` and `y = \cos 2\alpha`.
`dx/d\alpha = 2\cos 2\alpha`, `dy/d\alpha = -2\sin 2\alpha`.
`dy/dx = \frac{-2\sin 2\alpha}{2\cos 2\alpha} = -\tan 2\alpha = -x/y`.
Method 2 (Implicit): Notice `x^2 + y^2 = 1`. Then `2x + 2yy' = 0 \implies` **\frac{dy}{dx} = -\frac{x}{y}**.
</details>

19. 🔴 $x = e^t \sin t$, $y = e^t \cos t$
<details>
<summary>Solution</summary>

`dx/dt = e^t \sin t + e^t \cos t = e^t(\sin t + \cos t)`.
`dy/dt = e^t \cos t - e^t \sin t = e^t(\cos t - \sin t)`.
`\frac{dy}{dx} = \frac{e^t(\cos t - \sin t)}{e^t(\sin t + \cos t)} =` **\frac{\cos t - \sin t}{\sin t + \cos t}**.
</details>

20. 🔴 $x = a\cos^3\theta$, $y = a\sin^3\theta$ (Astroid). Show $\frac{dy}{dx} = -\tan\theta$.
<details>
<summary>Solution</summary>

`dx/d\theta = 3a\cos^2\theta(-\sin\theta) = -3a\cos^2\theta\sin\theta`.
`dy/d\theta = 3a\sin^2\theta(\cos\theta) = 3a\sin^2\theta\cos\theta`.
`\frac{dy}{dx} = \frac{3a\sin^2\theta\cos\theta}{-3a\cos^2\theta\sin\theta} = \frac{\sin\theta}{-\cos\theta} =` **-\tan\theta**. (Proved).
</details>

---

### Type 5: Second Derivative in Parametric Form

**Goal:** Compute $\frac{d^2y}{dx^2}$ using $\frac{d^2y}{dx^2} = \frac{d(dy/dx)/dt}{dx/dt}$.

**Solved Example:** ⭐

Find $\frac{d^2y}{dx^2}$ for $x = at^2$, $y = 2at$.

**Solution:**
```
dx/dt = 2at, dy/dt = 2a
dy/dx = 2a / 2at = 1/t

d(dy/dx)/dt = d(1/t)/dt = -1/t²

d²y/dx² = (-1/t²) / (2at) = -1/(2at³)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

21. 🟡 $x = \cos t$, $y = \sin t$. Find $d^2y/dx^2$.
<details>
<summary>Solution</summary>

`dx/dt = -\sin t`. `dy/dt = \cos t`.
`dy/dx = \frac{\cos t}{-\sin t} = -\cot t`.
`\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}(-\cot t)}{dx/dt} = \frac{\csc^2 t}{-\sin t} =` **-\csc^3 t**.
</details>

22. 🟡 $x = a\cos\theta$, $y = b\sin\theta$. Find $d^2y/dx^2$ in terms of $\theta$.
<details>
<summary>Solution</summary>

`dx/d\theta = -a\sin\theta`. `dy/d\theta = b\cos\theta`.
`dy/dx = \frac{b\cos\theta}{-a\sin\theta} = -\frac{b}{a}\cot\theta`.
`\frac{d^2y}{dx^2} = \frac{\frac{d}{d\theta}(-\frac{b}{a}\cot\theta)}{dx/d\theta} = \frac{\frac{b}{a}\csc^2\theta}{-a\sin\theta} =` **-\frac{b}{a^2}\csc^3\theta**.
</details>

23. 🔴 $x = a(\cos t + t\sin t)$, $y = a(\sin t - t\cos t)$. Find $d^2y/dx^2$.
<details>
<summary>Solution</summary>

`dx/dt = a(-\sin t + 1\cdot\sin t + t\cos t) = at\cos t`.
`dy/dt = a(\cos t - (1\cdot\cos t - t\sin t)) = at\sin t`.
`dy/dx = \frac{at\sin t}{at\cos t} = \tan t`.
`\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}(\tan t)}{dx/dt} = \frac{\sec^2 t}{at\cos t} =` **\frac{\sec^3 t}{at}**.
</details>

24. 🔴 If $x = a(1 - \cos\theta)$, $y = a(\theta + \sin\theta)$, show $d^2y/dx^2 = -\frac{1}{4a}\sec^4(\theta/2)$.
<details>
<summary>Solution</summary>

`dx/d\theta = a\sin\theta = 2a\sin(\theta/2)\cos(\theta/2)`.
`dy/d\theta = a(1 + \cos\theta) = 2a\cos^2(\theta/2)`.
`dy/dx = \frac{2a\cos^2(\theta/2)}{2a\sin(\theta/2)\cos(\theta/2)} = \cot(\theta/2)`.
`\frac{d^2y}{dx^2} = \frac{-\frac{1}{2}\csc^2(\theta/2)}{a\sin\theta} = \frac{-\frac{1}{2}\csc^2(\theta/2)}{2a\sin(\theta/2)\cos(\theta/2)} =` **-\frac{1}{4a}\csc^3(\theta/2)\sec(\theta/2)**.
*(Note: There is a typo in the classic problem statement. The expression `-\frac{1}{4a}\sec^4(\theta/2)` is obtained if the definitions of x and y are swapped: `x=a(\theta+\sin\theta), y=a(1-\cos\theta)`).*
</details>

25. 🔴 ⭐ For the ellipse $x = a\cos\theta, y = b\sin\theta$, find the radius of curvature at $\theta = \pi/2$.
<details>
<summary>Solution</summary>

Radius of curvature `\rho = \frac{[1 + (y')^2]^{3/2}}{|y''|}`.
From Q22, `y' = -\frac{b}{a}\cot\theta` and `y'' = -\frac{b}{a^2}\csc^3\theta`.
At `\theta = \pi/2`: `\cot(\pi/2) = 0 \implies y' = 0`.
`\csc(\pi/2) = 1 \implies y'' = -\frac{b}{a^2}`.
`\rho = \frac{[1 + 0^2]^{3/2}}{|-b/a^2|} = \frac{1}{b/a^2} =` **\frac{a^2}{b}**.
</details>

---

## Stage 4: Type Mixer

1. 🔴 ⭐ For $x = a\cos^3\theta$, $y = a\sin^3\theta$, find the tangent at $\theta = \pi/4$ and show it cuts equal intercepts.
<details>
<summary>Solution</summary>

From Q20, `dy/dx = -\tan\theta`. At `\theta = \pi/4`, slope `m = -1`.
The point is `x = a(1/\sqrt{2})^3 = a/2\sqrt{2}`, and `y = a/2\sqrt{2}`.
Tangent eq: `y - a/2\sqrt{2} = -1(x - a/2\sqrt{2})`.
`x + y = a/\sqrt{2}`.
The x-intercept is `a/\sqrt{2}` (when y=0). The y-intercept is `a/\sqrt{2}` (when x=0).
They are equal. (Proved).
</details>

2. 🔴 If $\sin(xy) + \cos(xy) = 1$, find $dy/dx$.
<details>
<summary>Solution</summary>

Let `u = xy`. We have `\sin u + \cos u = 1`.
Square both sides: `\sin^2 u + \cos^2 u + 2\sin u\cos u = 1 \implies 1 + \sin 2u = 1 \implies \sin 2u = 0`.
This means `2u = n\pi \implies xy = \text{constant}`.
Differentiating `xy = C`: `y + xy' = 0 \implies` **\frac{dy}{dx} = -\frac{y}{x}**.
</details>

3. 🟡 $x = \frac{t^2+1}{t}$, $y = t^2 - \frac{1}{t^2}$. Find $dy/dx$ and simplify.
<details>
<summary>Solution</summary>

Rewrite: `x = t + \frac{1}{t}` and `y = t^2 - \frac{1}{t^2}`.
`dx/dt = 1 - \frac{1}{t^2} = \frac{t^2-1}{t^2}`.
`dy/dt = 2t + \frac{2}{t^3} = \frac{2(t^4+1)}{t^3}`.
`\frac{dy}{dx} = \frac{2(t^4+1)/t^3}{(t^2-1)/t^2} =` **\frac{2(t^4+1)}{t(t^2-1)}**.
*(Alternative: notice `y = x(t - 1/t)` and `(t-1/t) = \pm\sqrt{x^2-4}`).*
</details>

4. 🔴 If $x^{1/2} + y^{1/2} = a^{1/2}$, show $dy/dx = -\sqrt{y/x}$.
<details>
<summary>Solution</summary>

Differentiate implicitly:
`\frac{1}{2}x^{-1/2} + \frac{1}{2}y^{-1/2}\frac{dy}{dx} = 0`.
Multiply by 2 and isolate `dy/dx`:
`y^{-1/2}\frac{dy}{dx} = -x^{-1/2}`.
`\frac{dy}{dx} = -\frac{x^{-1/2}}{y^{-1/2}} = -\frac{y^{1/2}}{x^{1/2}} =` **-\sqrt{\frac{y}{x}}**. (Proved).
</details>

5. 🔴 For the curve $x^{2/3} + y^{2/3} = a^{2/3}$, find $d^2y/dx^2$.
<details>
<summary>Solution</summary>

First derivative (from Q14): `y' = -x^{-1/3} y^{1/3}`.
Differentiate again: `y'' = - [ -\frac{1}{3}x^{-4/3}y^{1/3} + x^{-1/3}(\frac{1}{3}y^{-2/3}y') ]`.
Substitute `y'`:
`y'' = - [ -\frac{1}{3}x^{-4/3}y^{1/3} + \frac{1}{3}x^{-1/3}y^{-2/3}(-x^{-1/3}y^{1/3}) ]`.
`y'' = \frac{1}{3}x^{-4/3}y^{1/3} + \frac{1}{3}x^{-2/3}y^{-1/3}`.
Factor out `\frac{1}{3}x^{-4/3}y^{-1/3}`:
`y'' = \frac{1}{3x^{4/3}y^{1/3}} [ y^{2/3} + x^{2/3} ]`.
Since `x^{2/3} + y^{2/3} = a^{2/3}`, we get:
**\frac{d^2y}{dx^2} = \frac{a^{2/3}}{3x^{4/3}y^{1/3}}**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 If $x^2 + y^2 + 2gx + 2fy = 0$, find $dy/dx$. **(3 marks)**

**Solution:**
$2x + 2y\frac{dy}{dx} + 2g + 2f\frac{dy}{dx} = 0$
$(2y + 2f)\frac{dy}{dx} = -2x - 2g$
$\frac{dy}{dx} = \frac{-(x+g)}{y+f}$

---

**Q2.** 🟡 If $x = a(\theta + \sin\theta)$, $y = a(1 - \cos\theta)$, find $\frac{dy}{dx}$. **(3 marks)**

**Solution:**
$\frac{dx}{d\theta} = a(1+\cos\theta) = 2a\cos^2(\theta/2)$
$\frac{dy}{d\theta} = a\sin\theta = 2a\sin(\theta/2)\cos(\theta/2)$
$\frac{dy}{dx} = \frac{2a\sin(\theta/2)\cos(\theta/2)}{2a\cos^2(\theta/2)} = \tan(\theta/2)$

---

**Q3.** 🔴 If $x^{1/3} + y^{1/3} = 1$, find $\frac{d^2y}{dx^2}$. **(4 marks)**

**Solution:**
Differentiate: $\frac{1}{3}x^{-2/3} + \frac{1}{3}y^{-2/3}\frac{dy}{dx} = 0$
$\frac{dy}{dx} = -\frac{y^{2/3}}{x^{2/3}} = -\left(\frac{y}{x}\right)^{2/3}$

Differentiate again (let $p = dy/dx = -(y/x)^{2/3}$):
$\frac{d^2y}{dx^2} = -\frac{2}{3}\left(\frac{y}{x}\right)^{-1/3} \cdot \frac{y'x - y}{x^2}$

After simplification: $\frac{d^2y}{dx^2} = \frac{2}{3}\cdot\frac{y^{2/3}}{x^{4/3}} \cdot \frac{x^{1/3}+y^{1/3}}{x^{2/3}} = \frac{2}{3x^{5/3}y^{1/3}}$ (using $x^{1/3}+y^{1/3}=1$)

---

## Stage 6: JEE Mains Arena

**Q1.** If $\sin y = x\sin(a+y)$, then $\frac{dy}{dx} =$:
<br>(a) $\frac{\sin^2(a+y)}{\sin a}$   <br>(b) $\frac{\sin a}{\sin^2(a+y)}$   <br>(c) $\sin(a+y)$   <br>(d) $\frac{1}{\sin a}$

<details>
<summary>Solution</summary>
Differentiate: cos y (dy/dx) = sin(a+y) + x cos(a+y)(dy/dx)
(dy/dx)[cos y - x cos(a+y)] = sin(a+y)
From sin y = x sin(a+y): x = sin y/sin(a+y)

[cos y - (sin y/sin(a+y))cos(a+y)](dy/dx) = sin(a+y)
[cos y sin(a+y) - sin y cos(a+y)] / sin(a+y) · (dy/dx) = sin(a+y)
sin(a+y-y) / sin(a+y) · dy/dx = sin(a+y)
dy/dx = sin²(a+y)/sin a
Answer: (a) 🔴 ⭐
</details>

---

**Q2.** If $x = a\left(t + \frac{1}{t}\right)$ and $y = a\left(t - \frac{1}{t}\right)$, then $\frac{dy}{dx}$ is:
<br>(a) $x/y$   <br>(b) $y/x$   <br>(c) $t^2$   <br>(d) $-y/x$

<details>
<summary>Solution</summary>
dx/dt = a(1 - 1/t²); dy/dt = a(1 + 1/t²)
dy/dx = (1+1/t²)/(1-1/t²) = (t²+1)/(t²-1)

Now y/x = (t - 1/t)/(t + 1/t) = (t²-1)/(t²+1). So dy/dx = x/y.
Answer: (a) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** For $x^2 + y^2 = r^2$, $\frac{dy}{dx} = -\frac{x}{y}$.
<br>**Reason (R):** Differentiating implicitly, $2x + 2y\frac{dy}{dx} = 0$.

<details>
<summary>Solution</summary>
Both A and R are true, and R is the correct derivation leading to A.
Answer: (a) 🟢
</details>

---

**Q2.**
<br>**Assertion (A):** For parametric equations $x = f(t)$, $y = g(t)$, $\frac{d^2y}{dx^2} = \frac{g''(t)}{f''(t)}$.
<br>**Reason (R):** $\frac{d^2y}{dx^2} = \frac{d(dy/dx)/dt}{dx/dt}$.

<details>
<summary>Solution</summary>
A is false: The correct formula is R, which gives d(g'(t)/f'(t))/dt ÷ f'(t), NOT g''(t)/f''(t).
R is true.
Answer: (d) 🟡 ⭐
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 For $xy = c^2$, $\frac{dy}{dx} =$
   <br>(a) $c^2/x$   <br>(b) $-y/x$   <br>(c) $y/x$   <br>(d) $-c^2/x^2$

2. 🟡 For $x = at^2$, $y = 2at$, $\frac{d^2y}{dx^2} =$
   <br>(a) $-1/(2at^3)$   <br>(b) $1/t$   <br>(c) $2a$   <br>(d) $1/(2at)$

3. 🟡 ⭐ If $e^x + e^y = e^{x+y}$, then $\frac{dy}{dx} =$
   <br>(a) $e^{x-y}$   <br>(b) $-e^{x-y}$   <br>(c) $e^{y-x}$   <br>(d) $-e^{y-x}$

4. 🟡 For $x = a\cos^3\theta$, $y = a\sin^3\theta$, $\frac{dy}{dx} =$
   <br>(a) $\tan\theta$   <br>(b) $\cot\theta$   <br>(c) $-\tan\theta$   <br>(d) $-\cot\theta$

5. 🔴 If $x^y = y^x$, then $\frac{dy}{dx}$ at $(e, e)$ is:
   <br>(a) $0$   <br>(b) $1$   <br>(c) $-1$   <br>(d) $e$

6. 🟡 If $\sin y = x\cos(a+y)$, then $\frac{dy}{dx} =$
   <br>(a) $\cos^2(a+y)/\cos a$   <br>(b) $\sin a/\cos^2(a+y)$   <br>(c) $\cos a$   <br>(d) $\tan(a+y)$

7. 🟡 For $x = 2\cos t - \cos 2t$, $y = 2\sin t - \sin 2t$, $\frac{dy}{dx}$ at $t = \pi/2$ is:
   <br>(a) $-1$   <br>(b) $0$   <br>(c) $1$   <br>(d) $2$

8. 🔴 ⭐ If $\cos^{-1}(x/a)^2 + \cos^{-1}(y/b) = \alpha$, then $\frac{dy}{dx} =$
   <br>(a) $\frac{b^2x}{a^2y}$   <br>(b) $\frac{bx}{ay}$   <br>(c) $\frac{-b^2x}{a^2y}$   <br>(d) $\frac{a^2y}{b^2x}$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | b | 5 | b |
| 2 | a | 6 | a |
| 3 | b | 7 | c |
| 4 | c | 8 | c |

</details>

---

## What's Next?

You can now handle any curve, even when $y$ is entangled with $x$. In **Chapter 10**, we'll master **Logarithmic Differentiation** — a technique that converts messy products, quotients, and power functions into simple logarithms, and then differentiates them instantly.
