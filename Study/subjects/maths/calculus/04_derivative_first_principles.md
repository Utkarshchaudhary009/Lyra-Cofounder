# Chapter 4: Derivative from First Principles

---

## Stage 1: The Core Idea

### The Zoom-In Principle

Look at a circle. It's perfectly curved. But if you zoom in on a tiny section of its edge, what does it look like? **A straight line.** 

Look at the surface of the Earth. It's a sphere. But because we are so small relative to it, the ground beneath our feet looks flat.

This is the secret of calculus: **If you zoom in close enough, every smooth curve looks like a straight line.** 

### From Average to Instantaneous

Remember the speedometer from Chapter 1?
If you drive from Delhi to Agra (200 km) in 4 hours, your **average speed** is $200 / 4 = 50 \text{ km/h}$.
But at exactly 2:15 PM, you might be doing $80 \text{ km/h}$. 

How do we calculate speed at *one instant*?
Speed is just the slope of the distance-time graph.
$$ \text{Slope} = \frac{y_2 - y_1}{x_2 - x_1} $$

If we want the slope at exactly one point $x$, we take a second point slightly further away at $x + h$. The distance between them is $h$.
$$ \text{Slope} = \frac{f(x+h) - f(x)}{(x+h) - x} = \frac{f(x+h) - f(x)}{h} $$

This is the slope of the **secant line** connecting two points. But we want the slope at *one* point (the **tangent line**). How do we do that? We slide the second point closer and closer to the first point. We let the distance $h$ shrink to zero.

### The Definition of the Derivative

The instantaneous rate of change (the derivative) is the limit of the average rate of change as the interval shrinks to zero:

$$ f'(x) = \lim_{h\to0} \frac{f(x+h) - f(x)}{h} $$

This is called the **First Principle of Differentiation**. It is the bridge between Limits and Derivatives. Every shortcut rule you will ever learn (power rule, product rule, chain rule) comes directly from this single formula.

---

## Stage 2: The Formula Lab

There is only one formula here, but it goes by many names.

**Notation for the derivative of $y = f(x)$:**
- $f'(x)$ (Newton's notation, read as "f prime of x")
- $\frac{dy}{dx}$ (Leibniz's notation, read as "d y by d x")
- $y'$
- $y_1$
- $\frac{d}{dx} [f(x)]$ (The operator notation: "Take the derivative of f(x)")

### The Standard Derivations

You must know how to derive these basic functions using first principles. 

**1. Derivative of $f(x) = x^n$**
$$ f'(x) = \lim_{h\to0} \frac{(x+h)^n - x^n}{h} $$
By binomial expansion: $(x+h)^n = x^n + nx^{n-1}h + \dots$
$$ f'(x) = \lim_{h\to0} \frac{(x^n + nx^{n-1}h + \dots) - x^n}{h} = \lim_{h\to0} \frac{h(nx^{n-1} + \dots)}{h} = nx^{n-1} $$

**2. Derivative of $f(x) = \sin x$**
$$ f'(x) = \lim_{h\to0} \frac{\sin(x+h) - \sin x}{h} $$
Use $\sin C - \sin D = 2\cos\left(\frac{C+D}{2}\right)\sin\left(\frac{C-D}{2}\right)$:
$$ f'(x) = \lim_{h\to0} \frac{2\cos(x + h/2)\sin(h/2)}{h} = \lim_{h\to0} \cos(x + h/2) \cdot \frac{\sin(h/2)}{h/2} = \cos x \cdot 1 = \cos x $$

**3. Derivative of $f(x) = e^x$**
$$ f'(x) = \lim_{h\to0} \frac{e^{x+h} - e^x}{h} = \lim_{h\to0} \frac{e^x(e^h - 1)}{h} = e^x \lim_{h\to0} \frac{e^h - 1}{h} = e^x \cdot 1 = e^x $$

> ⚠️ **Trap Warning:** When using first principles, NEVER substitute $h=0$ immediately. It will ALWAYS give you $0/0$. Your entire goal is to cancel the $h$ in the denominator algebraically.

---

## Stage 3: Type-wise Mastery

### Type 1: Polynomials and Linear Functions

**Goal:** Expand $f(x+h)$, cancel the original $f(x)$ terms, factor out $h$, and divide.

**Solved Example:** ⭐

Find the derivative of $f(x) = x^2 - 3x$ from first principles.

**Solution:**
```
1. Write f(x+h):
f(x+h) = (x+h)² - 3(x+h) = x² + 2xh + h² - 3x - 3h

2. Set up the limit:
f'(x) = lim(h→0) [ f(x+h) - f(x) ] / h
= lim(h→0) [ (x² + 2xh + h² - 3x - 3h) - (x² - 3x) ] / h

3. Cancel non-h terms:
= lim(h→0) [ 2xh + h² - 3h ] / h

4. Factor out h and cancel:
= lim(h→0) h(2x + h - 3) / h
= lim(h→0) (2x + h - 3)

5. Substitute h = 0:
= 2x + 0 - 3 = 2x - 3
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 Find $f'(x)$ for $f(x) = 5x + 2$
<details>
<summary>Solution</summary>

`f(x+h) = 5(x+h) + 2 = 5x + 5h + 2`.
`f'(x) = \lim(h→0) [ (5x + 5h + 2) - (5x + 2) ] / h`.
`= \lim(h→0) 5h / h = \lim(h→0) 5 =` **5**.
</details>

2. 🟢 Find $f'(x)$ for $f(x) = 3x^2$
<details>
<summary>Solution</summary>

`f(x+h) = 3(x+h)^2 = 3(x^2 + 2xh + h^2) = 3x^2 + 6xh + 3h^2`.
`f'(x) = \lim(h→0) [ (3x^2 + 6xh + 3h^2) - 3x^2 ] / h`.
`= \lim(h→0) (6xh + 3h^2) / h = \lim(h→0) h(6x + 3h) / h`.
`= \lim(h→0) (6x + 3h) =` **6x**.
</details>

3. 🟡 $\frac{d}{dx} (2x^2 + 4x - 1)$ from first principles.
<details>
<summary>Solution</summary>

`f(x+h) = 2(x+h)^2 + 4(x+h) - 1 = 2x^2 + 4xh + 2h^2 + 4x + 4h - 1`.
`f(x+h) - f(x) = 4xh + 2h^2 + 4h = h(4x + 2h + 4)`.
`f'(x) = \lim(h→0) h(4x + 2h + 4) / h = \lim(h→0) (4x + 2h + 4) =` **4x + 4**.
</details>

4. 🟡 Find the derivative of $f(x) = x^3$ from first principles.
<details>
<summary>Solution</summary>

`f(x+h) = (x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3`.
`f(x+h) - f(x) = 3x^2h + 3xh^2 + h^3 = h(3x^2 + 3xh + h^2)`.
`f'(x) = \lim(h→0) h(3x^2 + 3xh + h^2) / h = \lim(h→0) (3x^2 + 3xh + h^2) =` **3x^2**.
</details>

5. 🟡 Find $f'(x)$ for $f(x) = (x-1)^2$
<details>
<summary>Solution</summary>

`f(x+h) = (x+h-1)^2 = ((x-1) + h)^2 = (x-1)^2 + 2(x-1)h + h^2`.
`f(x+h) - f(x) = 2(x-1)h + h^2 = h(2(x-1) + h)`.
`f'(x) = \lim(h→0) h(2(x-1) + h) / h = \lim(h→0) (2x - 2 + h) =` **2(x-1)** or **2x-2**.
</details>

---

### Type 2: Rational Functions (Fractions)

**Goal:** Take a common denominator in the numerator to combine the fractions, then cancel $h$.

**Solved Example:** ⭐

Find the derivative of $f(x) = \frac{1}{x+2}$ from first principles.

**Solution:**
```
f(x+h) = 1 / (x+h+2)

f'(x) = lim(h→0) [ 1/(x+h+2) - 1/(x+2) ] / h

Common denominator:
= lim(h→0) [ (x+2 - (x+h+2)) / ((x+h+2)(x+2)) ] / h
= lim(h→0) [ -h / ((x+h+2)(x+2)) ] * (1/h)

Cancel h:
= lim(h→0) -1 / ((x+h+2)(x+2))

Substitute h = 0:
= -1 / ((x+2)(x+2)) = -1 / (x+2)²
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟢 Find $f'(x)$ for $f(x) = \frac{1}{x}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ 1/(x+h) - 1/x ] / h`.
Common denominator: `\lim(h→0) [ (x - (x+h)) / (x(x+h)) ] / h`.
`= \lim(h→0) [ -h / (x(x+h)) ] * (1/h) = \lim(h→0) -1 / (x(x+h))`.
Substitute `h=0`: **-1/x^2**.
</details>

7. 🟡 Find $f'(x)$ for $f(x) = \frac{2}{3x-1}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ 2/(3(x+h)-1) - 2/(3x-1) ] / h`.
Common denominator: `2 * \lim(h→0) [ (3x-1) - (3x+3h-1) ] / [ h(3x+3h-1)(3x-1) ]`.
`= 2 * \lim(h→0) [ -3h ] / [ h(3x+3h-1)(3x-1) ]`.
Cancel `h`: `2 * \lim(h→0) -3 / [ (3x+3h-1)(3x-1) ]`.
Substitute `h=0`: **-6 / (3x-1)^2**.
</details>

8. 🟡 Find $f'(x)$ for $f(x) = \frac{x}{x+1}$ — *Hint: $(x+h)/(x+h+1) - x/(x+1)$*
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ (x+h)/(x+h+1) - x/(x+1) ] / h`.
Common denominator: `[ (x+h)(x+1) - x(x+h+1) ] / [ h(x+h+1)(x+1) ]`.
Numerator expands to: `(x^2 + x + hx + h) - (x^2 + hx + x) = h`.
Limit: `\lim(h→0) h / [ h(x+h+1)(x+1) ] = \lim(h→0) 1 / [ (x+h+1)(x+1) ]`.
Substitute `h=0`: **1 / (x+1)^2**.
</details>

9. 🔴 Find $f'(x)$ for $f(x) = \frac{1}{x^2}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ 1/(x+h)^2 - 1/x^2 ] / h`.
Common denominator: `[ x^2 - (x+h)^2 ] / [ h x^2 (x+h)^2 ]`.
Numerator: `x^2 - (x^2 + 2xh + h^2) = -2xh - h^2 = -h(2x + h)`.
Limit: `\lim(h→0) -h(2x + h) / [ h x^2 (x+h)^2 ] = \lim(h→0) -(2x + h) / [ x^2 (x+h)^2 ]`.
Substitute `h=0`: `-2x / (x^2 * x^2) = -2x / x^4 =` **-2/x^3**.
</details>

10. 🔴 Find $f'(x)$ for $f(x) = \frac{x-1}{x+1}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ (x+h-1)/(x+h+1) - (x-1)/(x+1) ] / h`.
Numerator of difference: `(x+h-1)(x+1) - (x-1)(x+h+1)`.
`= (x^2 + hx - x + x + h - 1) - (x^2 + hx + x - x - h - 1)`.
`= (x^2 + hx + h - 1) - (x^2 + hx - h - 1) = 2h`.
Limit: `\lim(h→0) 2h / [ h(x+h+1)(x+1) ] = \lim(h→0) 2 / [ (x+h+1)(x+1) ]`.
Substitute `h=0`: **2 / (x+1)^2**.
</details>

---

### Type 3: Functions with Square Roots

**Goal:** Multiply numerator and denominator by the conjugate to eliminate the square roots, then cancel $h$.

**Solved Example:** ⭐

Find the derivative of $f(x) = \sqrt{x}$ from first principles.

**Solution:**
```
f'(x) = lim(h→0) [ √(x+h) - √x ] / h

Multiply by conjugate:
= lim(h→0) [ √(x+h) - √x ] [ √(x+h) + √x ] / { h [ √(x+h) + √x ] }
= lim(h→0) [ (x+h) - x ] / { h [ √(x+h) + √x ] }
= lim(h→0) h / { h [ √(x+h) + √x ] }

Cancel h:
= lim(h→0) 1 / [ √(x+h) + √x ]

Substitute h = 0:
= 1 / [ √x + √x ] = 1 / (2√x)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟢 Find $f'(x)$ for $f(x) = \sqrt{x+3}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sqrt{x+h+3} - \sqrt{x+3} ] / h`.
Multiply by conjugate: `[ (x+h+3) - (x+3) ] / [ h(\sqrt{x+h+3} + \sqrt{x+3}) ]`.
`= \lim(h→0) h / [ h(\sqrt{x+h+3} + \sqrt{x+3}) ] = \lim(h→0) 1 / [ \sqrt{x+h+3} + \sqrt{x+3} ]`.
Substitute `h=0`: `1 / (\sqrt{x+3} + \sqrt{x+3}) =` **1 / (2\sqrt{x+3})**.
</details>

12. 🟡 Find $f'(x)$ for $f(x) = \sqrt{2x-1}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sqrt{2(x+h)-1} - \sqrt{2x-1} ] / h`.
Multiply by conjugate: `[ (2x+2h-1) - (2x-1) ] / [ h(\sqrt{2x+2h-1} + \sqrt{2x-1}) ]`.
`= \lim(h→0) 2h / [ h(\sqrt{2x+2h-1} + \sqrt{2x-1}) ]`.
Cancel `h`: `2 / ( \sqrt{2x+2h-1} + \sqrt{2x-1} )`.
Substitute `h=0`: `2 / (2\sqrt{2x-1}) =` **1 / \sqrt{2x-1}**.
</details>

13. 🟡 Find $f'(x)$ for $f(x) = \frac{1}{\sqrt{x}}$ — *Hint: Common denominator, then rationalize!*
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ 1/\sqrt{x+h} - 1/\sqrt{x} ] / h`.
Common denominator: `[ \sqrt{x} - \sqrt{x+h} ] / [ h\sqrt{x}\sqrt{x+h} ]`.
Multiply by conjugate `(\sqrt{x} + \sqrt{x+h})`:
Numerator: `x - (x+h) = -h`.
Limit: `\lim(h→0) -h / [ h\sqrt{x}\sqrt{x+h}(\sqrt{x} + \sqrt{x+h}) ]`.
Cancel `h` and substitute `h=0`:
`-1 / [ \sqrt{x}\sqrt{x}(\sqrt{x} + \sqrt{x}) ] = -1 / [ x * (2\sqrt{x}) ] =` **-1 / (2x\sqrt{x})**.
</details>

14. 🔴 Find $f'(x)$ for $f(x) = x\sqrt{x}$
<details>
<summary>Solution</summary>

Write `f(x) = x^{3/2}` or keep it as `x\sqrt{x}`. Using `x\sqrt{x}`:
`f'(x) = \lim(h→0) [ (x+h)\sqrt{x+h} - x\sqrt{x} ] / h`.
Multiply by conjugate: `[ (x+h)^3 - x^3 ] / [ h((x+h)\sqrt{x+h} + x\sqrt{x}) ]`.
Numerator: `(x^3 + 3x^2h + 3xh^2 + h^3) - x^3 = h(3x^2 + 3xh + h^2)`.
Cancel `h` and substitute `h=0`:
`3x^2 / [ x\sqrt{x} + x\sqrt{x} ] = 3x^2 / (2x\sqrt{x}) = (3/2) x / \sqrt{x} =` **(3/2)\sqrt{x}**.
*(Matches power rule: `3/2 x^{1/2}`)*
</details>

15. 🔴 Find $f'(x)$ for $f(x) = \sqrt{x^2 + 1}$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sqrt{(x+h)^2 + 1} - \sqrt{x^2 + 1} ] / h`.
Multiply by conjugate: `[ ((x+h)^2 + 1) - (x^2 + 1) ] / [ h(\sqrt{(x+h)^2+1} + \sqrt{x^2+1}) ]`.
Numerator: `(x^2 + 2xh + h^2 + 1) - (x^2 + 1) = h(2x + h)`.
Cancel `h` and substitute `h=0`:
`(2x + 0) / [ \sqrt{x^2+1} + \sqrt{x^2+1} ] = 2x / (2\sqrt{x^2+1}) =` **x / \sqrt{x^2+1}**.
</details>

---

### Type 4: Trigonometric Functions

**Goal:** Use sum/difference trigonometric formulas ($\sin C - \sin D$ or $\cos C - \cos D$) and standard trigonometric limits to evaluate.

**Solved Example:** ⭐

Find the derivative of $f(x) = \cos x$ from first principles.

**Solution:**
```
f'(x) = lim(h→0) [ \cos(x+h) - \cos x ] / h

Use cos C - cos D = -2 sin((C+D)/2) sin((C-D)/2):
= lim(h→0) [ -2 sin((2x+h)/2) sin(h/2) ] / h
= lim(h→0) -sin(x + h/2) * [ sin(h/2) / (h/2) ]

Apply standard limit lim(θ→0) sinθ/θ = 1:
= -sin(x + 0) * (1)
= -sin x
```
🔴 Hard ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Find $f'(x)$ for $f(x) = \sin 2x$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sin(2(x+h)) - \sin 2x ] / h`.
Use `\sin C - \sin D = 2\cos((C+D)/2)\sin((C-D)/2)`:
`= \lim(h→0) [ 2\cos(2x+h)\sin(h) ] / h`.
`= \lim(h→0) 2\cos(2x+h) * [\sin(h) / h]`.
As `h→0`, `\sin(h)/h → 1` and `2\cos(2x+h) → 2\cos 2x`.
Result: **2\cos 2x**.
</details>

17. 🔴 Find $f'(x)$ for $f(x) = \tan x$ — *Hint: Convert to $\sin/\cos$ and take common denominator.*
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \tan(x+h) - \tan x ] / h`.
Convert to sin/cos: `\lim(h→0) [ \frac{\sin(x+h)}{\cos(x+h)} - \frac{\sin x}{\cos x} ] / h`.
Common denominator: `\lim(h→0) [ \sin(x+h)\cos x - \cos(x+h)\sin x ] / [ h\cos(x+h)\cos x ]`.
Numerator is `\sin(A-B)` where `A=x+h, B=x`: `\sin(x+h - x) = \sin h`.
`= \lim(h→0) \frac{\sin h}{h} * \frac{1}{\cos(x+h)\cos x}`.
As `h→0`, `\sin h / h → 1`. Limit is `1 / (\cos x \cos x) = 1 / \cos^2 x =` **\sec^2 x**.
</details>

18. 🔴 Find $f'(x)$ for $f(x) = \cos 3x$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \cos(3(x+h)) - \cos 3x ] / h`.
Use `\cos C - \cos D = -2\sin((C+D)/2)\sin((C-D)/2)`:
`= \lim(h→0) [ -2\sin(3x + 3h/2)\sin(3h/2) ] / h`.
Multiply and divide by 3/2:
`= \lim(h→0) -2\sin(3x + 3h/2) * [ \sin(3h/2) / (3h/2) ] * (3/2)`.
Standard limit gives 1.
`= -2\sin(3x) * 1 * (3/2) =` **-3\sin 3x**.
</details>

19. 🔴 Find $f'(x)$ for $f(x) = x \sin x$ — *Hint: Use $x\sin x + h\sin x - x\sin x$*
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ (x+h)\sin(x+h) - x\sin x ] / h`.
Rewrite numerator: `x\sin(x+h) + h\sin(x+h) - x\sin x`.
Group terms: `x(\sin(x+h) - \sin x) + h\sin(x+h)`.
Divide by `h`:
`\lim(h→0) [ x * \frac{\sin(x+h) - \sin x}{h} + \frac{h\sin(x+h)}{h} ]`.
The first term is `x * (\text{derivative of } \sin x) = x\cos x`.
The second term is `\lim(h→0) \sin(x+h) = \sin x`.
Result: **x\cos x + \sin x**.
</details>

20. 🔴 Find $f'(x)$ for $f(x) = \sec x$
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sec(x+h) - \sec x ] / h`.
Convert to cos: `\lim(h→0) [ \frac{1}{\cos(x+h)} - \frac{1}{\cos x} ] / h`.
Common denominator: `\lim(h→0) [ \cos x - \cos(x+h) ] / [ h\cos x\cos(x+h) ]`.
Use `\cos C - \cos D`:
`\lim(h→0) [ -2\sin(x + h/2)\sin(-h/2) ] / [ h\cos x\cos(x+h) ]`.
Since `\sin(-h/2) = -\sin(h/2)`, negatives cancel.
`= \lim(h→0) \frac{\sin(h/2)}{h/2} * \frac{\sin(x + h/2)}{\cos x\cos(x+h)}`.
As `h→0`, limit is `1 * \frac{\sin x}{\cos x\cos x} = \frac{\sin x}{\cos^2 x} =` **\sec x \tan x**.
</details>

---

### Type 5: Derivative at a Specific Point ($x=a$)

**Goal:** Evaluate $f'(a) = \lim_{h\to0} \frac{f(a+h) - f(a)}{h}$ or $f'(a) = \lim_{x\to a} \frac{f(x) - f(a)}{x-a}$.

**Solved Example:**

Find the derivative of $f(x) = x^2 + 1$ at $x = 3$.

**Solution:**
```
Instead of finding f'(x) and then plugging in 3, we can plug in 3 from the start.
f'(3) = lim(h→0) [ f(3+h) - f(3) ] / h

f(3+h) = (3+h)² + 1 = 9 + 6h + h² + 1 = 10 + 6h + h²
f(3) = 3² + 1 = 10

f'(3) = lim(h→0) [ (10 + 6h + h²) - 10 ] / h
= lim(h→0) (6h + h²) / h
= lim(h→0) h(6 + h) / h
= lim(h→0) (6 + h) = 6
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

21. 🟢 Find the derivative of $f(x) = 4x - 7$ at $x = 2$.
<details>
<summary>Solution</summary>

`f'(2) = \lim(h→0) [ f(2+h) - f(2) ] / h`.
`f(2+h) = 4(2+h) - 7 = 8 + 4h - 7 = 1 + 4h`.
`f(2) = 4(2) - 7 = 1`.
`f'(2) = \lim(h→0) [ (1+4h) - 1 ] / h = \lim(h→0) 4h / h =` **4**.
</details>

22. 🟡 Find $f'(1)$ for $f(x) = \frac{1}{x^2}$ using first principles.
<details>
<summary>Solution</summary>

`f'(1) = \lim(h→0) [ f(1+h) - f(1) ] / h`.
`= \lim(h→0) [ \frac{1}{(1+h)^2} - 1 ] / h`.
Common denominator: `\lim(h→0) [ \frac{1 - (1+2h+h^2)}{(1+h)^2} ] / h`.
`= \lim(h→0) \frac{-2h - h^2}{h(1+h)^2} = \lim(h→0) \frac{-h(2+h)}{h(1+h)^2}`.
Cancel `h`: `\lim(h→0) \frac{-(2+h)}{(1+h)^2}`.
Substitute `h=0`: `-(2) / (1)^2 =` **-2**.
</details>

23. 🟡 Find the slope of the tangent to $y = \sqrt{x}$ at $x = 4$.
<details>
<summary>Solution</summary>

`f'(4) = \lim(h→0) [ \sqrt{4+h} - \sqrt{4} ] / h = \lim(h→0) [ \sqrt{4+h} - 2 ] / h`.
Multiply by conjugate: `\lim(h→0) [ (\sqrt{4+h} - 2)(\sqrt{4+h} + 2) ] / [ h(\sqrt{4+h} + 2) ]`.
`= \lim(h→0) [ (4+h) - 4 ] / [ h(\sqrt{4+h} + 2) ] = \lim(h→0) h / [ h(\sqrt{4+h} + 2) ]`.
Cancel `h` and substitute `h=0`: `1 / (\sqrt{4} + 2) = 1 / (2+2) =` **1/4**.
</details>

24. 🟡 Find $f'(\pi/2)$ for $f(x) = \sin x$ using first principles.
<details>
<summary>Solution</summary>

`f'(\pi/2) = \lim(h→0) [ \sin(\pi/2 + h) - \sin(\pi/2) ] / h`.
Since `\sin(\pi/2 + h) = \cos h` and `\sin(\pi/2) = 1`:
`= \lim(h→0) [ \cos h - 1 ] / h`.
Multiply by conjugate `(\cos h + 1)`:
`= \lim(h→0) [ \cos^2 h - 1 ] / [ h(\cos h + 1) ] = \lim(h→0) -\sin^2 h / [ h(\cos h + 1) ]`.
`= \lim(h→0) -(\frac{\sin h}{h}) * (\frac{\sin h}{\cos h + 1})`.
Substitute `h=0`: `-1 * (0 / 2) =` **0**.
</details>

25. 🔴 If $f(x) = |x|$, find $f'(0)$ using first principles. What happens to LHL and RHL?
<details>
<summary>Solution</summary>

`f'(0) = \lim(h→0) [ f(0+h) - f(0) ] / h = \lim(h→0) [ |h| - 0 ] / h = \lim(h→0) |h|/h`.
Right Hand Limit (RHL) as `h→0^+`: `h > 0 \implies |h| = h`. Limit is `h/h = 1`.
Left Hand Limit (LHL) as `h→0^-`: `h < 0 \implies |h| = -h`. Limit is `-h/h = -1`.
Since LHL ≠ RHL, the derivative **Does Not Exist**. (Sharp corner at `x=0`).
</details>

---

## Stage 4: Type Mixer

1. 🟡 Use first principles to differentiate $f(x) = \frac{x}{x-2}$ at $x = 3$.
<details>
<summary>Solution</summary>

`f(3) = 3/(3-2) = 3`.
`f(3+h) = (3+h) / (3+h-2) = (3+h) / (1+h)`.
`f'(3) = \lim(h→0) [ \frac{3+h}{1+h} - 3 ] / h`.
Common denominator: `\lim(h→0) [ \frac{(3+h) - 3(1+h)}{1+h} ] / h = \lim(h→0) \frac{3+h-3-3h}{h(1+h)} = \lim(h→0) \frac{-2h}{h(1+h)}`.
Cancel `h` and substitute `h=0`: `-2 / (1+0) =` **-2**.
</details>

2. 🔴 Find the derivative of $f(x) = e^{2x}$ from first principles.
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ e^{2(x+h)} - e^{2x} ] / h`.
Factor out `e^{2x}`: `\lim(h→0) [ e^{2x}(e^{2h} - 1) ] / h`.
Multiply and divide by 2: `\lim(h→0) e^{2x} * \frac{e^{2h} - 1}{2h} * 2`.
By standard limit `(e^u-1)/u \to 1`, this is `e^{2x} * 1 * 2 =` **2e^{2x}**.
</details>

3. 🔴 Find $f'(x)$ for $f(x) = \sqrt{x} \sin x$ by first principles.
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \sqrt{x+h}\sin(x+h) - \sqrt{x}\sin x ] / h`.
Add and subtract `\sqrt{x}\sin(x+h)`:
`= \lim(h→0) [ \frac{\sqrt{x+h}\sin(x+h) - \sqrt{x}\sin(x+h)}{h} + \frac{\sqrt{x}\sin(x+h) - \sqrt{x}\sin x}{h} ]`.
First part: `\lim(h→0) \sin(x+h) \frac{\sqrt{x+h} - \sqrt{x}}{h} = \sin x * (\text{deriv of } \sqrt{x}) = \sin x * \frac{1}{2\sqrt{x}}`.
Second part: `\sqrt{x} \lim(h→0) \frac{\sin(x+h) - \sin x}{h} = \sqrt{x} * (\text{deriv of } \sin x) = \sqrt{x}\cos x`.
Result: **\frac{\sin x}{2\sqrt{x}} + \sqrt{x}\cos x**.
</details>

4. 🟡 Determine the slope of the tangent line to the curve $y = 3/x^2$ at the point $(1, 3)$.
<details>
<summary>Solution</summary>

We need `f'(1)`. `f(1) = 3`.
`f'(1) = \lim(h→0) [ \frac{3}{(1+h)^2} - 3 ] / h`.
Common denominator: `\lim(h→0) [ \frac{3 - 3(1+h)^2}{(1+h)^2} ] / h = \lim(h→0) \frac{3 - 3(1+2h+h^2)}{h(1+h)^2}`.
`= \lim(h→0) \frac{-6h - 3h^2}{h(1+h)^2} = \lim(h→0) \frac{-h(6+3h)}{h(1+h)^2}`.
Cancel `h` and substitute `h=0`: `-(6) / (1)^2 =` **-6**.
</details>

5. 🔴 Find $f'(x)$ for $f(x) = \ln x$ from first principles. *[Hint: Use $\ln A - \ln B = \ln(A/B)$ and $\lim_{h\to0} \ln(1+h/x)/(h/x) = 1$]*
<details>
<summary>Solution</summary>

`f'(x) = \lim(h→0) [ \ln(x+h) - \ln x ] / h`.
Use log property: `\lim(h→0) \frac{1}{h} \ln(\frac{x+h}{x}) = \lim(h→0) \frac{1}{h} \ln(1 + \frac{h}{x})`.
To use standard limit, multiply and divide by `x` in the denominator:
`= \lim(h→0) \frac{1}{x} * \frac{\ln(1 + h/x)}{h/x}`.
Let `u = h/x`. As `h→0`, `u→0`. The limit `\frac{\ln(1+u)}{u}` is 1.
Result: `\frac{1}{x} * 1 =` **1/x**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the derivative of $f(x) = 2x^2 + 3x - 5$ from first principles. **(3 marks)**

**Solution:**
f'(x) = lim(h→0) [ (2(x+h)² + 3(x+h) - 5) - (2x² + 3x - 5) ] / h
= lim(h→0) [ 2(x²+2xh+h²) + 3x + 3h - 5 - 2x² - 3x + 5 ] / h
= lim(h→0) [ 4xh + 2h² + 3h ] / h
= lim(h→0) h(4x + 2h + 3) / h
= lim(h→0) (4x + 2h + 3) = 4x + 3

---

**Q2.** 🔴 Find the derivative of $f(x) = \cos x$ from first principles. **(4 marks)**

**Solution:**
f'(x) = lim(h→0) [ cos(x+h) - cos x ] / h
Using cos C - cos D = -2sin((C+D)/2)sin((C-D)/2):
= lim(h→0) [ -2sin(x + h/2) sin(h/2) ] / h
= lim(h→0) -sin(x + h/2) * [ sin(h/2) / (h/2) ]
As h→0, sin(h/2)/(h/2) → 1.
= -sin(x + 0) * 1 = -sin x.

---

**Q3.** 🟡 Find the derivative of $f(x) = \sqrt{3x+2}$ from first principles. **(3 marks)**

**Solution:**
f'(x) = lim(h→0) [ √(3(x+h)+2) - √(3x+2) ] / h
Rationalize:
= lim(h→0) [ 3(x+h)+2 - (3x+2) ] / [ h ( √(3x+3h+2) + √(3x+2) ) ]
= lim(h→0) 3h / [ h ( √(3x+3h+2) + √(3x+2) ) ]
= lim(h→0) 3 / ( √(3x+3h+2) + √(3x+2) )
= 3 / ( √(3x+2) + √(3x+2) ) = 3 / (2√(3x+2))

---

## Stage 6: JEE Mains Arena

*Note: In competitive exams, you never actually use first principles to solve a derivative—you use the shortcut rules (Chapter 6). However, JEE tests your understanding of the FIRST PRINCIPLE DEFINITION itself.*

**Q1.** The value of $\lim_{h\to0} \frac{e^{x+h} - e^x}{h}$ is:
(a) $e^h$   <br> (b) $e^x$   <br> (c) $0$   <br> (d) $1$

<details>
<summary>Solution</summary>
This limit is exactly the first principle definition of the derivative of f(x) = e^x.
d/dx (e^x) = e^x.
Answer: (b) 🟢
</details>

---

**Q2.** Let $f(x)$ be a differentiable function. Then $\lim_{x\to a} \frac{xf(a) - af(x)}{x - a}$ equals:
(a) $f(a) - af'(a)$   <br> (b) $af(a) - f'(a)$   <br> (c) $f'(a)$   <br> (d) $a f'(a)$

<details>
<summary>Solution</summary>
Add and subtract a·f(a) in the numerator:
= lim(x→a) [ xf(a) - af(a) + af(a) - af(x) ] / (x - a)
= lim(x→a) [ f(a)(x - a) - a(f(x) - f(a)) ] / (x - a)
Split the fraction:
= f(a) - a * lim(x→a) [ f(x) - f(a) ] / (x - a)
The second part is the definition of f'(a).
= f(a) - a·f'(a)
Answer: (a) 🔴 ⭐
</details>

---

**Q3.** If $f(a) = 2, f'(a) = 1, g(a) = -1, g'(a) = 2$, then $\lim_{x\to a} \frac{g(x)f(a) - g(a)f(x)}{x - a}$ is:
(a) $5$   <br> (b) $-5$   <br> (c) $1$   <br> (d) $0$

<details>
<summary>Solution</summary>
Add and subtract f(a)g(a):
= lim(x→a) [ f(a)(g(x) - g(a)) - g(a)(f(x) - f(a)) ] / (x - a)
= f(a)·g'(a) - g(a)·f'(a)
= 2(2) - (-1)(1) = 4 + 1 = 5.
Answer: (a) 🔴 ⭐
</details>

---

**Q4.** $\lim_{h\to0} \frac{f(x+h) - f(x-h)}{h}$ equals:
(a) $f'(x)$   <br> (b) $2f'(x)$   <br> (c) $0$   <br> (d) Does not exist

<details>
<summary>Solution</summary>
Add and subtract f(x):
= lim(h→0) [ f(x+h) - f(x) + f(x) - f(x-h) ] / h
= lim(h→0) [ f(x+h) - f(x) ] / h  +  lim(h→0) [ f(x) - f(x-h) ] / h
First limit is f'(x).
For second limit, let -h = k, then as h→0, k→0:
lim(k→0) [ f(x) - f(x+k) ] / (-k) = lim(k→0) [ f(x+k) - f(x) ] / k = f'(x).
Total = f'(x) + f'(x) = 2f'(x).
Answer: (b) 🟡
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
<br> **Assertion (A):** The derivative of $f(x) = |x|$ at $x=0$ does not exist.<br>
<br> **Reason (R):** The left-hand limit and right-hand limit of $\frac{f(0+h) - f(0)}{h}$ are not equal.

<details>
<summary>Solution</summary>
A is true: |x| has a sharp corner at x=0, so it's not differentiable there.
R is true: LHD = lim(h→0⁻) |h|/h = -1. RHD = lim(h→0⁺) |h|/h = 1. Since LHD ≠ RHD, derivative DNE.
R correctly explains A.
Answer: (a) 🟡 ⭐
</details>

---

**Q2.**
<br> **Assertion (A):** $f'(a) = \lim_{x\to a} \frac{f(x) - f(a)}{x - a}$ is an equivalent definition of the derivative.<br>
<br> **Reason (R):** Substituting $h = x - a$ transforms $\lim_{h\to0} \frac{f(a+h) - f(a)}{h}$ into the expression in A.

<details>
<summary>Solution</summary>
A is true: Both are valid definitions of the derivative at x=a.
R is true: If h = x - a, then x = a + h. As h→0, x→a. The transformation is perfectly valid.
Answer: (a) 🟢
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The derivative of a constant function $f(x) = c$ from first principles evaluates to:
   <br> (a) $c$   <br> (b) $x$   <br> (c) $0$   <br> (d) $1$

2. 🟢 If $f(x) = x^3$, the first step in finding $f'(x)$ from first principles is:
   <br> (a) $3x^2$   <br> (b) $\lim_{h\to0} \frac{(x+h)^3 - x^3}{h}$   <br> (c) $(x+h)^3$   <br> (d) $\lim_{x\to0} x^3$

3. 🟡 $\lim_{h\to0} \frac{\sin(\pi/6 + h) - \sin(\pi/6)}{h}$ evaluates to:
   <br> (a) $\sin(\pi/6)$   <br> (b) $\cos(\pi/6)$   <br> (c) $0$   <br> (d) $1$

4. 🟡 ⭐ The expression $\lim_{x\to 2} \frac{x^4 - 16}{x - 2}$ represents the derivative of:
   <br> (a) $x^4$ at $x=2$   <br> (b) $x^2$ at $x=4$   <br> (c) $16x$ at $x=2$   <br> (d) $x^4 - 16$ at $x=0$

5. 🟡 In finding the derivative of $\sqrt{x}$ by first principles, the crucial algebraic step is:
   <br> (a) Factoring   <br> (b) Rationalizing the numerator   <br> (c) Expanding binomially   <br> (d) Using L'Hopital's rule

6. 🔴 $\lim_{h\to0} \frac{\ln(x+h) - \ln x}{h}$ equals:
   <br> (a) $\ln x$   <br> (b) $e^x$   <br> (c) $1/x$   <br> (d) $0$

7. 🟡 ⭐ If $f(x) = x|x|$, then $f'(0)$ is:
   <br> (a) $0$   <br> (b) $1$   <br> (c) $-1$   <br> (d) Does not exist
   *(Hint: Use the definition $\lim_{h\to0} \frac{h|h| - 0}{h}$)*

8. 🔴 Let $f(x) = x \sin(1/x)$ for $x \neq 0$ and $f(0) = 0$. Using first principles, $f'(0)$ is:
   <br> (a) $0$   <br> (b) $1$   <br> (c) Does not exist   <br> (d) $\infty$

9. 🟡 The slope of the tangent to $f(x) = \frac{1}{x+1}$ at $x=1$ is:
   <br> (a) $1/4$   <br> (b) $-1/4$   <br> (c) $1/2$   <br> (d) $-1/2$

10. 🟡 $\lim_{x\to a} \frac{xf(a) - af(x)}{x - a} = $
    <br> (a) $f(a) - af'(a)$   <br> (b) $af(a) - f'(a)$   <br> (c) $a f'(a)$   <br> (d) $0$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| 1 | c | 5 | b | 9 | b |
| 2 | b | 6 | c | 10 | a |
| 3 | b | 7 | a | | |
| 4 | a | 8 | c | | |

</details>

---

## What's Next?

First principles are beautiful because they explain *why* derivatives work. But they are long, tedious, and error-prone. Imagine using first principles on $f(x) = \frac{\sqrt{x} \sin x}{e^x}$. It would take pages of algebra!

Mathematicians realized that by applying the first principles limit to general functions (like $f(x) \cdot g(x)$), they could derive **shortcut rules** that work every time.

In **Chapter 5**, we will drop the limits entirely and learn the **Rules of Differentiation**: the Power Rule, Product Rule, Quotient Rule, and Chain Rule basics. You will learn to differentiate in seconds what used to take 5 minutes.

**Key takeaway from Chapter 4:** Every derivative is just the slope of a line between two points, where the distance between the points shrinks to zero. All calculus is built on this one limit!
