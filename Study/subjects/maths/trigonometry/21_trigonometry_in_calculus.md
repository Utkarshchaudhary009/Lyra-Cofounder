# Chapter 21: Trigonometry in Calculus

---

## Stage 1: The Core Idea

### Trigonometry Meets Calculus

In JEE Advanced, trigonometry is heavily used in calculus:
- **Limits**: lim_{x to 0} sin x/x = 1 — the most important trig limit
- **Differentiation**: derivatives of sin, cos, tan and inverses
- **Integration**: integrals of trig functions

Every calculus problem with trig uses the concepts from this book.

---

## Stage 2: The Formula Lab

### Standard Limits

```
lim_{x to 0} sin x/x = 1
lim_{x to 0} tan x/x = 1
lim_{x to 0} (1 - cos x)/x^2 = 1/2
lim_{x to 0} sin^{-1}x/x = 1
lim_{x to 0} tan^{-1}x/x = 1
```

### Derivatives

```
d/dx (sin x) = cos x
d/dx (cos x) = -sin x
d/dx (tan x) = sec^2 x
d/dx (cot x) = -cosec^2 x
d/dx (sec x) = sec x tan x
d/dx (cosec x) = -cosec x cot x

d/dx (sin^{-1}x) = 1/sqrt(1-x^2)
d/dx (cos^{-1}x) = -1/sqrt(1-x^2)
d/dx (tan^{-1}x) = 1/(1+x^2)
d/dx (cot^{-1}x) = -1/(1+x^2)
```

### Integrals

```
int sin x dx = -cos x + C
int cos x dx = sin x + C
int sec^2 x dx = tan x + C
int cosec^2 x dx = -cot x + C
int sec x tan x dx = sec x + C
int cosec x cot x dx = -cosec x + C
int tan x dx = ln|sec x| + C
int cot x dx = ln|sin x| + C
int sec x dx = ln|sec x + tan x| + C
int cosec x dx = ln|cosec x - cot x| + C
```

---

## Stage 3: Type-wise Mastery

### Type 1: Standard Limits with sin x/x

**Goal:** Evaluate limits using lim_{x to 0} sin x/x = 1.

**Solved Example:**

Evaluate lim_{x to 0} sin 3x / sin 5x.

**Solution:**
```
= lim (3x * sin 3x/(3x)) / (5x * sin 5x/(5x))
= (3/5) * 1/1 = 3/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Evaluate lim_{x to 0} sin 2x / x.
<details>
<summary>Solution</summary>

We can write the limit by multiplying and dividing by 2:
\[
\lim_{x \to 0} \frac{\sin 2x}{x} = \lim_{x \to 0} \left( 2 \cdot \frac{\sin 2x}{2x} \right)
\]
Since \( \lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1 \), by setting \( \theta = 2x \) (as \( x \to 0 \implies 2x \to 0 \)):
\[
= 2 \cdot 1 = 2
\]
</details>

2. 🟡 Evaluate lim_{x to 0} tan 3x / sin 4x.
<details>
<summary>Solution</summary>

Divide both numerator and denominator by \( x \):
\[
\lim_{x \to 0} \frac{\tan 3x}{\sin 4x} = \lim_{x \to 0} \frac{\frac{\tan 3x}{x}}{\frac{\sin 4x}{x}}
\]
Multiply and divide the numerator by 3, and the denominator by 4 to form standard limits:
\[
= \lim_{x \to 0} \frac{3 \cdot \frac{\tan 3x}{3x}}{4 \cdot \frac{\sin 4x}{4x}} = \frac{3 \cdot \lim_{3x \to 0} \frac{\tan 3x}{3x}}{4 \cdot \lim_{4x \to 0} \frac{\sin 4x}{4x}}
\]
Using the standard limits \( \lim_{u \to 0} \frac{\tan u}{u} = 1 \) and \( \lim_{v \to 0} \frac{\sin v}{v} = 1 \):
\[
= \frac{3 \cdot 1}{4 \cdot 1} = \frac{3}{4}
\]
</details>

3. 🟡 Evaluate lim_{x to 0} (1 - cos 2x)/x^2.
<details>
<summary>Solution</summary>

Using the trigonometric double-angle identity \( 1 - \cos 2x = 2 \sin^2 x \):
\[
\lim_{x \to 0} \frac{1 - \cos 2x}{x^2} = \lim_{x \to 0} \frac{2 \sin^2 x}{x^2}
\]
Group the terms as a square of a standard limit:
\[
= 2 \cdot \left( \lim_{x \to 0} \frac{\sin x}{x} \right)^2 = 2 \cdot 1^2 = 2
\]
</details>

4. 🟡 Evaluate lim_{x to 0} (sin 5x - sin 3x)/x.
<details>
<summary>Solution</summary>

Split the limit into two separate standard limit expressions:
\[
\lim_{x \to 0} \frac{\sin 5x - \sin 3x}{x} = \lim_{x \to 0} \frac{\sin 5x}{x} - \lim_{x \to 0} \frac{\sin 3x}{x}
\]
Multiply and divide to match standard forms:
\[
= \lim_{x \to 0} \left( 5 \cdot \frac{\sin 5x}{5x} \right) - \lim_{x \to 0} \left( 3 \cdot \frac{\sin 3x}{3x} \right)
\]
\[
= 5(1) - 3(1) = 2
\]
</details>

5. 🔴 Evaluate lim_{x to 0} (sin x - x)/x^3.
<details>
<summary>Solution</summary>

Using the Taylor series expansion for \( \sin x \):
\[
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots
\]
Substitute this expansion into the limit:
\[
\text{lim}_{x \to 0} \frac{\left(x - \frac{x^3}{6} + \frac{x^5}{120} - \dots\right) - x}{x^3} = \lim_{x \to 0} \frac{-\frac{x^3}{6} + \frac{x^5}{120} - \dots}{x^3}
\]
Divide through by \( x^3 \):
\[
= \lim_{x \to 0} \left( -\frac{1}{6} + \frac{x^2}{120} - \dots \right) = -\frac{1}{6}
\]
*Alternative method (L'Hopital's Rule):*
Since the limit is in \( \frac{0}{0} \) form, differentiate numerator and denominator:
\[
\lim_{x \to 0} \frac{\sin x - x}{x^3} = \lim_{x \to 0} \frac{\cos x - 1}{3x^2}
\]
Differentiate again (still \( \frac{0}{0} \)):
\[
= \lim_{x \to 0} \frac{-\sin x}{6x} = -\frac{1}{6} \lim_{x \to 0} \frac{\sin x}{x} = -\frac{1}{6}
\]
</details>

---

### Type 2: L'Hopital's Rule with Trig

**Goal:** Use L'Hopital for 0/0 forms with trig.

**Solved Example:**

Evaluate lim_{x to 0} (1 - cos x)/x^2.

**Solution:**
Using L'Hopital or the known limit:
= lim_{x to 0} sin x/(2x) = (1/2) * lim sin x/x = 1/2
🟡 Medium

---

**Practice Problems:**

6. 🟡 Evaluate lim_{x to 0} (tan x - sin x)/x^3.
<details>
<summary>Solution</summary>

Rewrite \( \tan x \) as \( \frac{\sin x}{\cos x} \):
\[
\lim_{x \to 0} \frac{\tan x - \sin x}{x^3} = \lim_{x \to 0} \frac{\frac{\sin x}{\cos x} - \sin x}{x^3} = \lim_{x \to 0} \frac{\sin x(1 - \cos x)}{x^3 \cos x}
\]
Separate this expression into a product of standard limits:
\[
= \lim_{x \to 0} \left( \frac{\sin x}{x} \cdot \frac{1 - \cos x}{x^2} \cdot \frac{1}{\cos x} \right)
\]
Evaluate each limit individually:
- \( \lim_{x \to 0} \frac{\sin x}{x} = 1 \)
- \( \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2} \)
- \( \lim_{x \to 0} \frac{1}{\cos x} = 1 \)
Multiplying the results:
\[
= 1 \cdot \frac{1}{2} \cdot 1 = \frac{1}{2}
\]
</details>

7. 🟡 Evaluate lim_{x to 0} (sin^{-1}x)/x.
<details>
<summary>Solution</summary>

Since this is a \( \frac{0}{0} \) limit form, we apply L'Hopital's Rule:
Differentiate the numerator and the denominator:
\[
\lim_{x \to 0} \frac{\sin^{-1}x}{x} = \lim_{x \to 0} \frac{\frac{d}{dx}(\sin^{-1}x)}{\frac{d}{dx}(x)} = \lim_{x \to 0} \frac{\frac{1}{\sqrt{1-x^2}}}{1}
\]
As \( x \to 0 \), we evaluate directly:
\[
= \frac{1}{\sqrt{1-0^2}} = 1
\]
*Alternative method:*
Let \( \theta = \sin^{-1}x \implies x = \sin\theta \). As \( x \to 0 \), \( \theta \to 0 \).
\[
\lim_{x \to 0} \frac{\sin^{-1}x}{x} = \lim_{\theta \to 0} \frac{\theta}{\sin\theta} = \frac{1}{\lim_{\theta \to 0} \frac{\sin\theta}{\theta}} = 1
\]
</details>

8. 🔴 Evaluate lim_{x to pi/2} (1 - sin x)/(pi/2 - x)^2.
<details>
<summary>Solution</summary>

Let \( y = \frac{\pi}{2} - x \). As \( x \to \frac{\pi}{2} \), \( y \to 0 \).
Since \( x = \frac{\pi}{2} - y \), we have:
\[
\sin x = \sin\left(\frac{\pi}{2} - y\right) = \cos y
\]
The limit in terms of \( y \) becomes:
\[
\lim_{y \to 0} \frac{1 - \cos y}{y^2}
\]
This is a standard limit equal to \( \frac{1}{2} \).
Thus:
\[
\lim_{x \to \pi/2} \frac{1 - \sin x}{\left(\frac{\pi}{2} - x\right)^2} = \frac{1}{2}
\]
</details>

9. 🔴 ⭐ Evaluate lim_{x to 0} (x cos x - sin x)/x^3.
<details>
<summary>Solution</summary>

The limit is in the indeterminate form \( \frac{0}{0} \), so we apply L'Hopital's Rule:
Differentiate the numerator and the denominator with respect to \( x \):
- Numerator: \( \frac{d}{dx}(x \cos x - \sin x) = \cos x - x \sin x - \cos x = -x \sin x \)
- Denominator: \( \frac{d}{dx}(x^3) = 3x^2 \)
The limit simplifies to:
\[
\lim_{x \to 0} \frac{-x \sin x}{3x^2} = \lim_{x \to 0} \frac{-&sin x}{3x} = -\frac{1}{3} \cdot \lim_{x \to 0} \frac{\sin x}{x}
\]
Using the standard limit \( \lim_{x \to 0} \frac{\sin x}{x} = 1 \):
\[
= -\frac{1}{3} \cdot 1 = -\frac{1}{3}
\]
</details>

10. 🔴 Evaluate lim_{x to 0} (e^x - e^{-x} - 2 sin x)/x^3.
<details>
<summary>Solution</summary>

Since this is a \( \frac{0}{0} \) form, we apply L'Hopital's Rule:
Differentiating numerator and denominator:
\[
\lim_{x \to 0} \frac{e^x + e^{-x} - 2\cos x}{3x^2} \quad \left(\text{still } \frac{0}{0}\right)
\]
Apply L'Hopital's Rule a second time:
\[
\lim_{x \to 0} \frac{e^x - e^{-x} + 2\sin x}{6x} \quad \left(\text{still } \frac{0}{0}\right)
\]
Apply L'Hopital's Rule a third time:
\[
\lim_{x \to 0} \frac{e^x + e^{-x} + 2\cos x}{6}
\]
Evaluate directly by substituting \( x = 0 \):
\[
= \frac{e^0 + e^0 + 2\cos 0}{6} = \frac{1 + 1 + 2(1)}{6} = \frac{4}{6} = \frac{2}{3}
\]
</details>

---

### Type 3: Derivatives of sin, cos, tan

**Goal:** Differentiate basic trig functions.

**Solved Example:**

Find d/dx (x^2 sin x).

**Solution:**
Using product rule:
= 2x sin x + x^2 cos x
🟢 Easy

---

**Practice Problems:**

11. 🟢 Find d/dx (sin 3x).
<details>
<summary>Solution</summary>

Using the chain rule:
\[
\frac{d}{dx}(\sin 3x) = \cos 3x \cdot \frac{d}{dx}(3x) = \cos 3x \cdot 3 = 3 \cos 3x
\]
</details>

12. 🟢 Find d/dx (cos(x^2)).
<details>
<summary>Solution</summary>

Using the chain rule:
\[
\frac{d}{dx}(\cos(x^2)) = -\sin(x^2) \cdot \frac{d}{dx}(x^2) = -\sin(x^2) \cdot 2x = -2x \sin(x^2)
\]
</details>

13. 🟡 Find d/dx (tan x / x).
<details>
<summary>Solution</summary>

Using the quotient rule \( \frac{d}{dx}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2} \) with \( u = \tan x \) and \( v = x \):
- \( u' = \sec^2 x \)
- \( v' = 1 \)
Applying the formula:
\[
\frac{d}{dx}\left(\frac{\tan x}{x}\right) = \frac{(\sec^2 x)(x) - (\tan x)(1)}{x^2} = \frac{x \sec^2 x - \tan x}{x^2}
\]
</details>

14. 🟡 Find d/dx (sin x * cos x).
<details>
<summary>Solution</summary>

Using the identity \( \sin x \cos x = \frac{1}{2} \sin 2x \):
\[
\frac{d}{dx}(\sin x \cos x) = \frac{d}{dx}\left(\frac{1}{2} \sin 2x\right) = \frac{1}{2} \cdot \cos 2x \cdot 2 = \cos 2x
\]
*Alternative method (using product rule):*
\[
\frac{d}{dx}(\sin x \cos x) = \cos x \cos x + \sin x (-\sin x) = \cos^2 x - \sin^2 x = \cos 2x
\]
</details>

15. 🔴 ⭐ Find d/dx (sin^{-1}(x^2)).
<details>
<summary>Solution</summary>

Using the chain rule with \( u = x^2 \):
Since \( \frac{d}{du}(\sin^{-1}u) = \frac{1}{\sqrt{1 - u^2}} \):
\[
\frac{d}{dx}(\sin^{-1}(x^2)) = \frac{1}{\sqrt{1 - (x^2)^2}} \cdot \frac{d}{dx}(x^2) = \frac{1}{\sqrt{1 - x^4}} \cdot 2x = \frac{2x}{\sqrt{1 - x^4}}
\]
</details>

---

### Type 4: Derivatives of Inverse Trig

**Goal:** Differentiate inverse trig functions.

**Solved Example:**

Find d/dx (sin^{-1}(x/2)).

**Solution:**
```
Let y = sin^{-1}(x/2)
dy/dx = 1/sqrt(1 - (x/2)^2) * (1/2)
= 1/(2 sqrt(1 - x^2/4))
= 1/sqrt(4 - x^2)
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 Find d/dx (tan^{-1}(3x)).
<details>
<summary>Solution</summary>

Using the chain rule:
\[
\frac{d}{dx}(\tan^{-1}(3x)) = \frac{1}{1 + (3x)^2} \cdot \frac{d}{dx}(3x) = \frac{1}{1 + 9x^2} \cdot 3 = \frac{3}{1 + 9x^2}
\]
</details>

17. 🟡 Find d/dx (cos^{-1}(1/x)).
<details>
<summary>Solution</summary>

Let \( y = \cos^{-1}(1/x) \).
Using the chain rule:
\[
\frac{dy}{dx} = -\frac{1}{\sqrt{1 - (1/x)^2}} \cdot \frac{d}{dx}\left(\frac{1}{x}\right)
\]
\[
= -\frac{1}{\sqrt{\frac{x^2 - 1}{x^2}}} \cdot \left(-\frac{1}{x^2}\right) = \frac{|x|}{\sqrt{x^2 - 1}} \cdot \frac{1}{x^2} = \frac{1}{|x|\sqrt{x^2 - 1}} \quad \text{for } |x| > 1
\]
*(Note: Since \( \cos^{-1}(1/x) = \sec^{-1}x \) for \( |x| \ge 1 \), this matches the standard derivative of \( \sec^{-1}x \).)*
</details>

18. 🟡 Find d/dx (sin^{-1}(2x/(1+x^2))).
<details>
<summary>Solution</summary>

Let \( x = \tan \theta \), where \( \theta \in (-\pi/2, \pi/2) \). Then:
\[
\frac{2x}{1+x^2} = \frac{2\tan\theta}{1+\tan^2\theta} = \sin 2\theta
\]
Assuming \( |x| < 1 \), we have \( \theta \in (-\pi/4, \pi/4) \implies 2\theta \in (-\pi/2, \pi/2) \).
Thus, the expression simplifies to:
\[
\sin^{-1}\left(\frac{2x}{1+x^2}\right) = \sin^{-1}(\sin 2\theta) = 2\theta = 2\tan^{-1}x
\]
Differentiating with respect to \( x \):
\[
\frac{d}{dx}\left(2\tan^{-1}x\right) = \frac{2}{1+x^2} \quad \text{for } |x| < 1
\]
*(Note: If \( |x| > 1 \), the derivative is \( -\frac{2}{1+x^2} \). The general derivative is \( \frac{2\text{ sgn}(1-x^2)}{1+x^2} \).)*
</details>

19. 🔴 ⭐ Find d/dx (tan^{-1}(x/(1+sqrt(1-x^2)))).
<details>
<summary>Solution</summary>

Let \( x = \sin\theta \) for \( \theta \in [-\pi/2, \pi/2] \).
Then \( \sqrt{1-x^2} = \sqrt{1-\sin^2\theta} = \cos\theta \) (since \( \cos\theta \ge 0 \) in this domain).
Simplify the expression inside the inverse tangent:
\[
\frac{x}{1+\sqrt{1-x^2}} = \frac{\sin\theta}{1+\cos\theta} = \frac{2\sin(\theta/2)\cos(\theta/2)}{2\cos^2(\theta/2)} = \tan(\theta/2)
\]
Thus:
\[
\tan^{-1}\left(\frac{x}{1+\sqrt{1-x^2}}\right) = \tan^{-1}\left(\tan\frac{\theta}{2}\right) = \frac{\theta}{2} = \frac{1}{2}\sin^{-1}x
\]
Differentiate with respect to \( x \):
\[
\frac{d}{dx}\left(\frac{1}{2}\sin^{-1}x\right) = \frac{1}{2\sqrt{1-x^2}}
\]
</details>

20. 🔴 Find d/dx (sec^{-1}(x^2)).
<details>
<summary>Solution</summary>

Using the chain rule:
Since \( \frac{d}{du}(\sec^{-1}u) = \frac{1}{|u|\sqrt{u^2-1}} \), let \( u = x^2 \) (note \( |x^2| = x^2 \)):
\[
\frac{d}{dx}(\sec^{-1}(x^2)) = \frac{1}{x^2\sqrt{(x^2)^2 - 1}} \cdot \frac{d}{dx}(x^2)
\]
\[
= \frac{1}{x^2\sqrt{x^4 - 1}} \cdot 2x = \frac{2}{x\sqrt{x^4 - 1}}
\]
</details>

---

### Type 5: Indefinite Integrals of Trig

**Goal:** Integrate basic trig expressions.

**Solved Example:**

Evaluate int (sin 2x + cos 3x) dx.

**Solution:**
```
= -(1/2) cos 2x + (1/3) sin 3x + C
```
🟢 Easy

---

**Practice Problems:**

21. 🟢 Evaluate int sin 4x dx.
<details>
<summary>Solution</summary>

Using the standard integral \( \int \sin(ax) \, dx = -\frac{1}{a}\cos(ax) + C \):
\[
\int \sin 4x \, dx = -\frac{1}{4} \cos 4x + C
\]
</details>

22. 🟢 Evaluate int sec^2(2x) dx.
<details>
<summary>Solution</summary>

Using the standard integral \( \int \sec^2(ax) \, dx = \frac{1}{a}\tan(ax) + C \):
\[
\int \sec^2(2x) \, dx = \frac{1}{2} \tan 2x + C
\]
</details>

23. 🟡 Evaluate int (sec x tan x + cosec^2 x) dx.
<details>
<summary>Solution</summary>

Integrating term by term:
\[
\int (\sec x \tan x + \csc^2 x) \, dx = \int \sec x \tan x \, dx + \int \csc^2 x \, dx
\]
Using the standard formulas \( \int \sec x \tan x \, dx = \sec x \) and \( \int \csc^2 x \, dx = -\cot x \):
\[
= \sec x - \cot x + C
\]
</details>

24. 🟡 Evaluate int tan^2 x dx. (Hint: tan^2 x = sec^2 x - 1)
<details>
<summary>Solution</summary>

Use the trigonometric identity \( \tan^2 x = \sec^2 x - 1 \) to rewrite the integrand:
\[
\int \tan^2 x \, dx = \int (\sec^2 x - 1) \, dx
\]
Now integrate term by term:
\[
= \int \sec^2 x \, dx - \int 1 \, dx = \tan x - x + C
\]
</details>

25. 🔴 ⭐ Evaluate int sec^4 x dx.
<details>
<summary>Solution</summary>

Rewrite \( \sec^4 x \) as \( \sec^2 x \cdot \sec^2 x = (1 + \tan^2 x) \sec^2 x \):
\[
\int \sec^4 x \, dx = \int (1 + \tan^2 x) \sec^2 x \, dx
\]
Let \( u = \tan x \). Then \( du = \sec^2 x \, dx \).
Substituting these into the integral:
\[
\int (1 + u^2) \, du = u + \frac{u^3}{3} + C
\]
Substitute back \( u = \tan x \):
\[
= \tan x + \frac{1}{3}\tan^3 x + C
\]
</details>

---

### Type 6: Integration by Substitution

**Goal:** Use substitution to integrate trig functions.

**Solved Example:**

Evaluate int sin^3 x cos x dx.

**Solution:**
```
Let u = sin x, du = cos x dx
int u^3 du = u^4/4 + C = sin^4 x/4 + C
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 Evaluate int sin^5 x cos x dx.
<details>
<summary>Solution</summary>

Let \( u = \sin x \). Then \( du = \cos x \, dx \).
Substitute into the integral:
\[
\int \sin^5 x \cos x \, dx = \int u^5 \, du = \frac{u^6}{6} + C
\]
Substitute back \( u = \sin x \):
\[
= \frac{\sin^6 x}{6} + C
</details>

27. 🟡 Evaluate int tan x sec^2 x dx.
<details>
<summary>Solution</summary>

Let \( u = \tan x \). Then \( du = \sec^2 x \, dx \).
Substitute into the integral:
\[
\int \tan x \sec^2 x \, dx = \int u \, du = \frac{u^2}{2} + C
\]
Substitute back \( u = \tan x \):
\[
= \frac{\tan^2 x}{2} + C
\]
*(Note: Alternatively, letting \( u = \sec x \implies du = \sec x \tan x \, dx \) yields the equivalent result \( \frac{\sec^2 x}{2} + C' \).)*
</details>

28. 🔴 Evaluate int sin^2 x cos^3 x dx.
<details>
<summary>Solution</summary>

Rewrite \( \cos^3 x \) as \( \cos^2 x \cos x = (1 - \sin^2 x) \cos x \):
\[
\int \sin^2 x \cos^3 x \, dx = \int \sin^2 x (1 - \sin^2 x) \cos x \, dx
\]
Let \( u = \sin x \implies du = \cos x \, dx \).
Substituting these into the integral:
\[
\int u^2 (1 - u^2) \, du = \int (u^2 - u^4) \, du = \frac{u^3}{3} - \frac{u^5}{5} + C
\]
Substitute back \( u = \sin x \):
\[
= \frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C
\]
</details>

29. 🔴 ⭐ Evaluate int sin^4 x dx using reduction.
<details>
<summary>Solution</summary>

Use the double-angle formulas to reduce the powers of sine:
\[
\sin^2 x = \frac{1 - \cos 2x}{2}
\]
Squaring both sides:
\[
\sin^4 x = \left( \frac{1 - \cos 2x}{2} \right)^2 = \frac{1 - 2\cos 2x + \cos^2 2x}{4}
\]
Use the identity \( \cos^2 2x = \frac{1 + \cos 4x}{2} \) to reduce the remaining square term:
\[
\sin^4 x = \frac{1}{4} \left( 1 - 2\cos 2x + \frac{1 + \cos 4x}{2} \right) = \frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x
\]
Integrate term by term:
\[
\int \sin^4 x \, dx = \int \left( \frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x \right) \, dx
\]
\[
= \frac{3}{8}x - \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x + C
\]
</details>

30. 🔴 Evaluate int sec^3 x dx.
<details>
<summary>Solution</summary>

Let \( I = \int \sec^3 x \, dx \).
Use integration by parts: \( \int u \, dv = uv - \int v \, du \).
Let:
- \( u = \sec x \implies du = \sec x \tan x \, dx \)
- \( dv = \sec^2 x \, dx \implies v = \tan x \)
Then:
\[
I = \sec x \tan x - \int \tan x (\sec x \tan x) \, dx = \sec x \tan x - \int \sec x \tan^2 x \, dx
\]
Substitute the identity \( \tan^2 x = \sec^2 x - 1 \):
\[
I = \sec x \tan x - \int \sec x (\sec^2 x - 1) \, dx = \sec x \tan x - \int \sec^3 x \, dx + \int \sec x \, dx
\]
\[
I = \sec x \tan x - I + \ln|\sec x + \tan x|
\]
Add \( I \) to both sides:
\[
2I = \sec x \tan x + \ln|\sec x + \tan x|
\]
\[
I = \frac{1}{2}\sec x \tan x + \frac{1}{2}\ln|\sec x + \tan x| + C
\]
</details>

---

### Type 7: Definite Integrals of Trig

**Goal:** Evaluate definite integrals involving trig functions.

**Solved Example:**

Evaluate int_0^{pi/2} sin x dx.

**Solution:**
```
= [-cos x]_0^{pi/2}
= -(cos pi/2 - cos 0)
= -(0 - 1) = 1
```
🟢 Easy

---

**Practice Problems:**

31. 🟢 Evaluate int_0^{pi/4} sec^2 x dx.
<details>
<summary>Solution</summary>

The antiderivative of \( \sec^2 x \) is \( \tan x \):
\[
\int_0^{\pi/4} \sec^2 x \, dx = \left[ \tan x \right]_0^{\pi/4} = \tan\frac{\pi}{4} - \tan 0 = 1 - 0 = 1
\]
</details>

32. 🟡 Evaluate int_0^{pi/2} sin^2 x dx.
<details>
<summary>Solution</summary>

Let \( I = \int_0^{\pi/2} \sin^2 x \, dx \).
Apply the property \( \int_0^a f(x) \, dx = \int_0^a f(a-x) \, dx \):
\[
I = \int_0^{\pi/2} \sin^2\left(\frac{\pi}{2} - x\right) \, dx = \int_0^{\pi/2} \cos^2 x \, dx
\]
Add the two integrals:
\[
2I = \int_0^{\pi/2} (\sin^2 x + \cos^2 x) \, dx = \int_0^{\pi/2} 1 \, dx = [x]_0^{\pi/2} = \frac{\pi}{2}
\]
Dividing by 2 gives:
\[
I = \frac{\pi}{4}
\]
</details>

33. 🟡 ⭐ Evaluate int_0^{pi/2} cos^3 x dx.
<details>
<summary>Solution</summary>

Rewrite \( \cos^3 x \) as \( \cos^2 x \cos x = (1 - \sin^2 x)\cos x \):
\[
I = \int_0^{\pi/2} (1 - \sin^2 x)\cos x \, dx
\]
Let \( u = \sin x \implies du = \cos x \, dx \).
Limits:
- When \( x = 0 \implies u = 0 \).
- When \( x = \pi/2 \implies u = 1 \).
Substitute:
\[
I = \int_0^1 (1 - u^2) \, du = \left[ u - \frac{u^3}{3} \right]_0^1 = \left(1 - \frac{1}{3}\right) - 0 = \frac{2}{3}
\]
</details>

34. 🔴 Evaluate int_0^{pi} x sin x dx.
<details>
<summary>Solution</summary>

Use integration by parts: \( \int u \, dv = uv - \int v \, du \).
Let \( u = x \implies du = dx \) and \( dv = \sin x \, dx \implies v = -\cos x \).
\[
\int_0^{\pi} x \sin x \, dx = \left[ -x \cos x \right]_0^{\pi} - \int_0^{\pi} (-\cos x) \, dx
\]
Evaluate the first term:
\[
= (-\pi \cos\pi - 0) + \int_0^{\pi} \cos x \, dx = \pi + \left[ \sin x \right]_0^{\pi}
\]
Since \( \sin\pi = 0 \) and \( \sin 0 = 0 \):
\[
= \pi + (0 - 0) = \pi
\]
</details>

35. 🔴 ⭐ Evaluate int_0^{pi/2} (sin x - cos x)/(sin x + cos x) dx.
<details>
<summary>Solution</summary>

Let \( I = \int_0^{\pi/2} \frac{\sin x - \cos x}{\sin x + \cos x} \, dx \).
Apply the property \( \int_0^a f(x) \, dx = \int_0^a f(a-x) \, dx \):
\[
I = \int_0^{\pi/2} \frac{\sin(\pi/2 - x) - \cos(\pi/2 - x)}{\sin(\pi/2 - x) + \cos(\pi/2 - x)} \, dx
\]
Substitute \( \sin(\pi/2 - x) = \cos x \) and \( \cos(\pi/2 - x) = \sin x \):
\[
I = \int_0^{\pi/2} \frac{\cos x - \sin x}{\cos x + \sin x} \, dx = - \int_0^{\pi/2} \frac{\sin x - \cos x}{\sin x + \cos x} \, dx = -I
\]
Since \( I = -I \):
\[
2I = 0 \implies I = 0
\]
</details>

---

### Type 8: Application — Max/Min Using Derivatives

**Goal:** Use trig derivatives in optimization.

**Solved Example:**

Find the maximum of f(x) = sin x + cos x for x in [0, pi/2].

**Solution:**
```
f'(x) = cos x - sin x = 0
cos x = sin x
x = pi/4

f(pi/4) = sin(pi/4) + cos(pi/4) = sqrt(2)
Check endpoints: f(0) = 1, f(pi/2) = 1
Maximum = sqrt(2)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

36. 🟡 Find max of f(x) = 2 sin x + 3 cos x in [0, pi/2].
<details>
<summary>Solution</summary>

To find the critical points, differentiate \( f(x) \):
\[
f'(x) = 2 \cos x - 3 \sin x
\]
Set the derivative to 0:
\[
2 \cos x - 3 \sin x = 0 \implies \tan x = \frac{2}{3}
\]
Since \( x \in [0, \pi/2] \), there is a unique angle \( x \) satisfying \( \tan x = 2/3 \).
At this point, we construct a right triangle:
- \( \sin x = \frac{2}{\sqrt{2^2 + 3^2}} = \frac{2}{\sqrt{13}} \)
- \( \cos x = \frac{3}{\sqrt{2^2 + 3^2}} = \frac{3}{\sqrt{13}} \)
Evaluate \( f(x) \) at this critical point:
\[
f(x) = 2\left(\frac{2}{\sqrt{13}}\right) + 3\left(\frac{3}{\sqrt{13}}\right) = \frac{13}{\sqrt{13}} = \sqrt{13} \approx 3.61
\]
Evaluate \( f(x) \) at the boundaries of the interval \( [0, \pi/2] \):
- At \( x = 0 \): \( f(0) = 2(0) + 3(1) = 3 \)
- At \( x = \pi/2 \): \( f(\pi/2) = 2(1) + 3(0) = 2 \)
Comparing these values, the maximum value is \( \sqrt{13} \).
</details>

37. 🟡 Find the minimum of f(x) = x + tan x for x in (0, pi/2).
<details>
<summary>Solution</summary>

Differentiate \( f(x) \) with respect to \( x \):
\[
f'(x) = 1 + \sec^2 x
\]
Since \( \sec^2 x \ge 1 \) for all real \( x \), we have \( f'(x) \ge 2 > 0 \) for all \( x \in (0, \pi/2) \).
Because the first derivative is strictly positive, the function \( f(x) \) is strictly increasing on the interval \( (0, \pi/2) \).
Therefore, \( f(x) \) has no absolute minimum inside the open interval \( (0, \pi/2) \), but it approaches its infimum as \( x \) approaches the left boundary:
\[
\lim_{x \to 0^+} (x + \tan x) = 0
\]
Thus, the infimum of the function is 0, but no minimum is attained on the open interval.
</details>

38. 🔴 Find the maximum area of a rectangle inscribed in a semicircle of radius r.
<details>
<summary>Solution</summary>

Let the semicircle of radius \( r \) be defined by the equation \( x^2 + y^2 = r^2 \) for \( y \ge 0 \) centered at the origin.
Let the rectangle be symmetrically placed with its base along the x-axis, from \( -x \) to \( x \), and its top vertices touching the semicircle at \( (-x, y) \) and \( (x, y) \).
The base of the rectangle is \( 2x \), and its height is \( y \). The area is:
\[
A = 2xy
\]
Using polar coordinates, we set \( x = r \cos \theta \) and \( y = r \sin \theta \) for \( \theta \in [0, \pi/2] \):
\[
A = 2(r \cos \theta)(r \sin \theta) = r^2 (2 \sin \theta \cos \theta) = r^2 \sin 2\theta
\]
To maximize the area \( A \), we maximize \( \sin 2\theta \).
The maximum value of \( \sin 2\theta \) is 1, which occurs when \( 2\theta = \pi/2 \implies \theta = \pi/4 \).
Thus, the maximum area is:
\[
A_{\text{max}} = r^2
\]
</details>

39. 🔴 ⭐ Find the maximum of f(x) = sin^2 x + cos^4 x.
<details>
<summary>Solution</summary>

Express \( \cos^4 x \) in terms of \( \sin^2 x \):
\[
f(x) = \sin^2 x + (\cos^2 x)^2 = \sin^2 x + (1 - \sin^2 x)^2 = \sin^4 x - \sin^2 x + 1
\]
Let \( u = \sin^2 x \). Since \( x \) is real, \( u \in [0, 1] \).
Define the quadratic function \( g(u) \):
\[
g(u) = u^2 - u + 1 \quad \text{for } u \in [0, 1]
\]
This parabola opens upwards, and its vertex occurs at:
\[
u = -\frac{b}{2a} = \frac{1}{2}
\]
Evaluate \( g(u) \) at the vertex and the boundaries of the interval \( [0, 1] \):
- At \( u = \frac{1}{2} \): \( g(1/2) = (1/2)^2 - 1/2 + 1 = \frac{3}{4} \) (This is the minimum value)
- At \( u = 0 \): \( g(0) = 0 - 0 + 1 = 1 \)
- At \( u = 1 \): \( g(1) = 1 - 1 + 1 = 1 \)
Comparing these values, the maximum value of \( f(x) \) is 1.
</details>

40. 🔴 A ladder of length L slides down a wall. Find the maximum area of the triangle formed by the ladder, wall, and floor.
<details>
<summary>Solution</summary>

Let the vertical wall lie along the y-axis, and the floor lie along the x-axis.
The ladder of length \( L \) forms a right-angled triangle with the wall and floor.
Let the angle between the ladder and the floor be \( \theta \), where \( \theta \in [0, \pi/2] \).
The horizontal base of the triangle is \( L \cos \theta \), and the vertical height is \( L \sin \theta \).
The area \( A \) of this right triangle is:
\[
A = \frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2} (L \cos \theta)(L \sin \theta) = \frac{1}{4} L^2 (2 \sin \theta \cos \theta) = \frac{1}{4} L^2 \sin 2\theta
\]
To maximize \( A \), we maximize \( \sin 2\theta \).
The maximum value of \( \sin 2\theta \) is 1 (occurring when \( 2\theta = \pi/2 \implies \theta = \pi/4 \)).
Thus, the maximum area is:
\[
A_{\text{max}} = \frac{1}{4} L^2
\]
</details>

---

## Stage 4: Type Mixer

1. 🟡 Evaluate lim_{x to 0} (sin 2x - 2 sin x)/x^3.
<details>
<summary>Solution</summary>

Using the double-angle identity \( \sin 2x = 2 \sin x \cos x \):
\[
\text{lim}_{x \to 0} \frac{\sin 2x - 2 \sin x}{x^3} = \lim_{x \to 0} \frac{2 \sin x \cos x - 2 \sin x}{x^3} = \lim_{x \to 0} \frac{-2 \sin x (1 - \cos x)}{x^3}
\]
Rewrite the expression to use standard limit forms:
\[
= -2 \lim_{x \to 0} \left( \frac{\sin x}{x} \cdot \frac{1 - \cos x}{x^2} \right)
\]
Substitute the standard limit values \( \lim_{x \to 0} \frac{\sin x}{x} = 1 \) and \( \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2} \):
\[
= -2 \cdot (1) \cdot \left( \frac{1}{2} \right) = -1
\]
</details>

2. 🟡 Find dy/dx if y = tan^{-1}((sin x)/(1 + cos x)).
<details>
<summary>Solution</summary>

Simplify the argument of the inverse tangent using half-angle formulas:
- \( \sin x = 2 \sin(x/2) \cos(x/2) \)
- \( 1 + \cos x = 2 \cos^2(x/2) \)
Substituting these:
\[
\frac{\sin x}{1 + \cos x} = \frac{2 \sin(x/2) \cos(x/2)}{2 \cos^2(x/2)} = \tan\left(\frac{x}{2}\right)
\]
Thus, the function simplifies to:
\[
y = \tan^{-1}\left(\tan\frac{x}{2}\right) = \frac{x}{2}
\]
Differentiate with respect to \( x \):
\[
\frac{dy}{dx} = \frac{1}{2}
\]
</details>

3. 🔴 ⭐ Evaluate int_0^{pi/2} sin^3 x cos^2 x dx.
<details>
<summary>Solution</summary>

Write the integrand as \( \sin^3 x \cos^2 x = \sin^2 x \cos^2 x \sin x = (1 - \cos^2 x)\cos^2 x \sin x \).
The integral is:
\[
\int_0^{\pi/2} (1 - \cos^2 x)\cos^2 x \sin x \, dx
\]
Let \( u = \cos x \implies du = -\sin x \, dx \).
Change of limits:
- When \( x = 0 \implies u = 1 \).
- When \( x = \pi/2 \implies u = 0 \).
Substitute and reverse the limits to absorb the negative sign:
\[
= \int_0^1 (1 - u^2) u^2 \, du = \int_0^1 (u^2 - u^4) \, du = \left[ \frac{u^3}{3} - \frac{u^5}{5} \right]_0^1 = \frac{1}{3} - \frac{1}{5} = \frac{2}{15}
\]
</details>

4. 🔴 Find the maximum value of sin x + cos x + sin 2x in [0, pi/2].
<details>
<summary>Solution</summary>

Let \( t = \sin x + \cos x \).
Squaring both sides:
\[
t^2 = \sin^2 x + \cos^2 x + 2 \sin x \cos x = 1 + \sin 2x \implies \sin 2x = t^2 - 1
\]
For \( x \in [0, \pi/2] \), we can express \( t \) as:
\[
t = \sqrt{2} \sin\left(x + \frac{\pi}{4}\right)
\]
Since \( x \in [0, \pi/2] \implies x + \frac{\pi}{4} \in [\pi/4, 3\pi/4] \).
In this interval, \( \sin(x+\pi/4) \in [\frac{1}{\sqrt{2}}, 1] \), so the range of \( t \) is:
\[
t \in [1, \sqrt{2}]
\]
Now substitute \( t \) and \( \sin 2x \) into the original expression:
\[
g(t) = t + (t^2 - 1) = t^2 + t - 1 \quad \text{for } t \in [1, \sqrt{2}]
\]
This is a quadratic function opening upwards. The vertex occurs at \( t = -1/2 \), meaning \( g(t) \) is strictly increasing on the interval \( [1, \sqrt{2}] \).
The maximum value occurs at the right endpoint \( t = \sqrt{2} \):
\[
g(\sqrt{2}) = (\sqrt{2})^2 + \sqrt{2} - 1 = 1 + \sqrt{2}
\]
</details>

5. 🔴 Evaluate int_0^{pi/2} sin x/(sin x + cos x) dx using the property int_0^a f(x) dx = int_0^a f(a-x) dx.
<details>
<summary>Solution</summary>

Let \( I = \int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx \).
Apply the property \( \int_0^a f(x) \, dx = \int_0^a f(a-x) \, dx \):
\[
I = \int_0^{\pi/2} \frac{\sin(\pi/2 - x)}{\sin(\pi/2 - x) + \cos(\pi/2 - x)} \, dx = \int_0^{\pi/2} \frac{\cos x}{\cos x + \sin x} \, dx
\]
Adding the two equations:
\[
2I = \int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx + \int_0^{\pi/2} \frac{\cos x}{\sin x + \cos x} \, dx = \int_0^{\pi/2} \frac{\sin x + \cos x}{\sin x + \cos x} \, dx
\]
\[
2I = \int_0^{\pi/2} 1 \, dx = [x]_0^{\pi/2} = \frac{\pi}{2} \implies I = \frac{\pi}{4}
\]
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Evaluate lim_{x to 0} tan 2x / sin 3x. **(2 marks)**

<details>
<summary>Solution</summary>

Multiply and divide by \( 2x \) in the numerator and \( 3x \) in the denominator:
\[
\lim_{x \to 0} \frac{\tan 2x}{\sin 3x} = \lim_{x \to 0} \frac{2x \cdot \frac{\tan 2x}{2x}}{3x \cdot \frac{\sin 3x}{3x}}
\]
\[
= \frac{2}{3} \cdot \frac{\lim_{2x \to 0} \frac{\tan 2x}{2x}}{\lim_{3x \to 0} \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}
\]
</details>

---

**Q2.** 🟡 Find d/dx (sin^{-1}(2x)). **(2 marks)**

<details>
<summary>Solution</summary>

Using the chain rule:
\[
\frac{d}{dx}(\sin^{-1}(2x)) = \frac{1}{\sqrt{1 - (2x)^2}} \cdot \frac{d}{dx}(2x) = \frac{2}{\sqrt{1 - 4x^2}}
\]
</details>

---

**Q3.** 🟡 Evaluate int sec^2(3x) dx. **(1 mark)**

<details>
<summary>Solution</summary>

Using the standard integration formula \( \int \sec^2(ax) \, dx = \frac{1}{a} \tan(ax) + C \):
\[
\int \sec^2(3x) \, dx = \frac{1}{3} \tan 3x + C
\]
</details>

---

**Q4.** 🟡 ⭐ Evaluate int_0^{pi/2} sin^2 x dx. **(2 marks)**

<details>
<summary>Solution</summary>

Using the identity \( \sin^2 x = \frac{1 - \cos 2x}{2} \):
\[
\int_0^{\pi/2} \sin^2 x \, dx = \int_0^{\pi/2} \frac{1 - \cos 2x}{2} \, dx
\]
\[
= \left[ \frac{x}{2} - \frac{\sin 2x}{4} \right]_0^{\pi/2} = \left( \frac{\pi}{4} - \frac{\sin \pi}{4} \right) - \left( 0 - \frac{\sin 0}{4} \right) = \frac{\pi}{4}
\]
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** lim_{x to 0} sin 5x / sin 3x equals:
(a) 5/3
(b) 3/5
(c) 1
(d) 0

<details><summary>Solution</summary>
= (5/3) * (sin 5x/5x)/(sin 3x/3x) = 5/3
Answer: (a) Green
</details>

---

**Q2.** The derivative of sin(cos x) is:
(a) cos(cos x) * (-sin x)
(b) cos(-sin x)
(c) cos(cos x)
(d) -sin(cos x) * sin x

<details><summary>Solution</summary>
Chain rule: d/dx sin(cos x) = cos(cos x) * (-sin x)
Answer: (a) Yellow
</details>

---

**Q3.** int_0^{pi/2} cos x dx equals:
(a) 0
(b) 1
(c) -1
(d) pi/2

<details><summary>Solution</summary>
int_0^{pi/2} cos x dx = [sin x]_0^{pi/2} = 1 - 0 = 1
Answer: (b) Green
</details>

---

**Q4.** The value of int sec x (sec x + tan x) dx is:
(a) tan x + sec x + C
(b) sec x - tan x + C
(c) tan x - sec x + C
(d) sec x + C

<details><summary>Solution</summary>
int (sec^2 x + sec x tan x) dx = tan x + sec x + C
Answer: (a) Yellow
</details>

---

**Q5.** lim_{x to 0} (1 - cos 2x)/(x sin x) equals:
(a) 0
(b) 1
(c) 2
(d) 1/2

<details><summary>Solution</summary>
1 - cos 2x = 2 sin^2 x
= lim 2 sin^2 x/(x sin x) = lim 2 sin x/x = 2
Answer: (c) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 Assertion <br>
(A): d/dx (sin x) = cos x. <br>
Reason (R): This follows from the limit definition of derivative.

<details>
<summary>Solution</summary>

Both true, R explains A.

**Answer: (a)**
</details>

---

**Q2.** 🟡 Assertion <br>
(A): \( \int \sec x \, dx = \ln|\sec x + \tan x| + C \). <br>
Reason (R): \( \frac{d}{dx} (\ln|\sec x + \tan x|) = \sec x \).

<details>
<summary>Solution</summary>

Let \( y = \ln|\sec x + \tan x| \).
Differentiating both sides with respect to \( x \):
\[
\frac{dy}{dx} = \frac{1}{\sec x + \tan x} \cdot \frac{d}{dx}(\sec x + \tan x) = \frac{\sec x \tan x + \sec^2 x}{\sec x + \tan x} = \frac{\sec x(\tan x + \sec x)}{\sec x + \tan x} = \sec x
\]
By the definition of antiderivative, since the derivative of the right side is the integrand, the integration formula is correct. Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).

**Answer: (a)**
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The value of \( \lim_{x \to 0} \frac{1 - \cos 4x}{x^2} \) is:
   (a) 2   (b) 4   (c) 8   (d) 16
<details>
<summary>Solution</summary>

Using the standard limit \( \lim_{u \to 0} \frac{1 - \cos u}{u^2} = \frac{1}{2} \):
Let \( u = 4x \). As \( x \to 0 \), \( u \to 0 \).
Multiply and divide by 16:
\[
\lim_{x \to 0} \frac{1 - \cos 4x}{x^2} = 16 \cdot \lim_{4x \to 0} \frac{1 - \cos 4x}{(4x)^2} = 16 \cdot \frac{1}{2} = 8
\]

**Answer: (c) 8**
</details>

2. 🟢 The derivative of \( \cos(\sin x) \) with respect to \( x \) is:
   (a) \( -\sin(\sin x) \cos x \)   (b) \( -\sin(\cos x) \)   (c) \( \cos(\cos x) \sin x \)   (d) \( -\sin x \cos x \)
<details>
<summary>Solution</summary>

Let \( y = \cos(\sin x) \).
Using the chain rule:
\[
\frac{dy}{dx} = -\sin(\sin x) \cdot \frac{d}{dx}(\sin x) = -\sin(\sin x) \cos x
\]

**Answer: (a) -\sin(\sin x) \cos x**
</details>

3. 🟡 The value of \( \lim_{x \to 0} \frac{\tan x - \sin x}{x^3} \) is:
   (a) 1/2   (b) 1   (c) 2   (d) 0
<details>
<summary>Solution</summary>

Express \( \tan x \) as \( \frac{\sin x}{\cos x} \):
\[
\lim_{x \to 0} \frac{\tan x - \sin x}{x^3} = \lim_{x \to 0} \frac{\sin x (1 - \cos x)}{x^3 \cos x}
\]
Separate into standard limits:
\[
= \lim_{x \to 0} \left( \frac{\sin x}{x} \right) \cdot \lim_{x \to 0} \left( \frac{1 - \cos x}{x^2} \right) \cdot \lim_{x \to 0} \left( \frac{1}{\cos x} \right)
\]
\[
= 1 \cdot \frac{1}{2} \cdot 1 = \frac{1}{2}
\]

**Answer: (a) 1/2**
</details>

4. 🟡 The derivative of \( \tan^{-1}\left(\frac{\cos x - \sin x}{\cos x + \sin x}\right) \) is:
   (a) 1   (b) -1   (c) 1/2   (d) -1/2
<details>
<summary>Solution</summary>

Simplify the inner expression by dividing the numerator and the denominator by \( \cos x \):
\[
\frac{\cos x - \sin x}{\cos x + \sin x} = \frac{1 - \tan x}{1 + \tan x} = \tan\left(\frac{\pi}{4} - x\right)
\]
Thus:
\[
y = \tan^{-1}\left(\tan\left(\frac{\pi}{4} - x\right)\right) = \frac{\pi}{4} - x
\]
Differentiate with respect to \( x \):
\[
\frac{dy}{dx} = -1
\]

**Answer: (b) -1**
</details>

5. 🟡 The integral \( \int \frac{dx}{1 + \cos x} \) is equal to:
   (a) \( \tan(x/2) + C \)   (b) \( \frac{1}{2} \tan(x/2) + C \)   (c) \( -\cot(x/2) + C \)   (d) \( 2 \tan(x/2) + C \)
<details>
<summary>Solution</summary>

Using the identity \( 1 + \cos x = 2 \cos^2(x/2) \):
\[
\int \frac{dx}{1 + \cos x} = \int \frac{dx}{2 \cos^2(x/2)} = \frac{1}{2} \int \sec^2(x/2) \, dx
\]
Using the formula \( \int \sec^2(au) \, du = \frac{1}{a}\tan(au) + C \):
\[
= \frac{1}{2} \cdot \left[ \frac{\tan(x/2)}{1/2} \right] + C = \tan(x/2) + C
\]

**Answer: (a) \tan(x/2) + C**
</details>

6. 🟡 The derivative of \( \sin^{-1}\left(\frac{2x}{1+x^2}\right) \) at \( x = 2 \) is:
   (a) 2/5   (b) -2/5   (c) 1/5   (d) -1/5
<details>
<summary>Solution</summary>

Let \( y = \sin^{-1}\left(\frac{2x}{1+x^2}\right) \).
Since \( |x| > 1 \) (here \( x = 2 \)), we use the simplification:
\[
y = \pi - 2\tan^{-1}x \quad \text{for } x > 1
\]
Differentiating with respect to \( x \):
\[
\frac{dy}{dx} = -\frac{2}{1+x^2}
\]
At \( x = 2 \):
\[
\left.\frac{dy}{dx}\right|_{x=2} = -\frac{2}{1+2^2} = -\frac{2}{5}
\]

**Answer: (b) -2/5**
</details>

7. 🟡 The value of \( \int_0^{\pi/2} \sin^3 x \, dx \) is:
   (a) 2/3   (b) 1/3   (c) 4/3   (d) 1
<details>
<summary>Solution</summary>

Write the integrand as \( \sin^3 x = (1 - \cos^2 x)\sin x \).
Let \( u = \cos x \implies du = -\sin x \, dx \).
Limits:
- At \( x = 0 \implies u = 1 \).
- At \( x = \pi/2 \implies u = 0 \).
The integral becomes:
\[
\int_1^0 (1 - u^2)(-du) = \int_0^1 (1 - u^2) \, du = \left[ u - \frac{u^3}{3} \right]_0^1 = 1 - \frac{1}{3} = \frac{2}{3}
\]

**Answer: (a) 2/3**
</details>

8. 🟡 The maximum value of \( 3\sin x + 4\cos x + 5 \) is:
   (a) 10   (b) 12   (c) 8   (d) 5
<details>
<summary>Solution</summary>

The maximum value of the expression \( a\sin x + b\cos x \) is \( \sqrt{a^2 + b^2} \).
For \( 3\sin x + 4\cos x \), the maximum value is:
\[
\sqrt{3^2 + 4^2} = \sqrt{25} = 5
\]
Adding the constant term 5, the maximum value of the entire expression is:
\[
5 + 5 = 10
\]

**Answer: (a) 10**
</details>

9. 🔴 The definite integral \( \int_0^{\pi} \sin^2 x \cos^4 x \, dx \) is equal to:
   (a) \( \pi/16 \)   (b) \( \pi/32 \)   (c) \( \pi/8 \)   (d) \( 3\pi/16 \)
<details>
<summary>Solution</summary>

Using symmetry about \( x = \pi/2 \) (since \( \sin(\pi-x) = \sin x \) and \( \cos(\pi-x) = -\cos x \implies \cos^4(\pi-x) = \cos^4 x \)):
\[
I = \int_0^{\pi} \sin^2 x \cos^4 x \, dx = 2 \int_0^{\pi/2} \sin^2 x \cos^4 x \, dx
\]
Using Wallis' formula for \( m = 2, n = 4 \):
\[
\int_0^{\pi/2} \sin^2 x \cos^4 x \, dx = \frac{(2-1)!! (4-1)!!}{(2+4)!!} \cdot \frac{\pi}{2} = \frac{1!! \cdot 3!!}{6!!} \cdot \frac{\pi}{2}
\]
Since \( 1!! = 1 \), \( 3!! = 3 \cdot 1 = 3 \), and \( 6!! = 6 \cdot 4 \cdot 2 = 48 \):
\[
= \frac{1 \cdot 3}{48} \cdot \frac{\pi}{2} = \frac{3\pi}{96} = \frac{\pi}{32}
\]
Thus:
\[
I = 2 \cdot \frac{\pi}{32} = \frac{\pi}{16}
\]

**Answer: (a) \pi/16**
</details>

10. 🔴 The minimum value of \( f(x) = \sec x + \csc x \) in the interval \( (0, \pi/2) \) is:
    (a) 2   (b) \( \sqrt{2} \)   (c) \( 2\sqrt{2} \)   (d) 4
<details>
<summary>Solution</summary>

Let \( f(x) = \sec x + \csc x \) for \( x \in (0, \pi/2) \).
Differentiating:
\[
f'(x) = \sec x \tan x - \csc x \cot x = \frac{\sin x}{\cos^2 x} - \frac{\cos x}{\sin^2 x} = \frac{\sin^3 x - \cos^3 x}{\sin^2 x \cos^2 x}
\]
Set \( f'(x) = 0 \implies \sin^3 x = \cos^3 x \implies \tan^3 x = 1 \implies \tan x = 1 \).
For \( x \in (0, \pi/2) \), this gives \( x = \frac{\pi}{4} \).
Since \( f'(x) < 0 \) for \( x < \pi/4 \) and \( f'(x) > 0 \) for \( x > \pi/4 \), \( x = \pi/4 \) is the global minimum.
Evaluating \( f(x) \) at \( x = \pi/4 \):
\[
f(pi/4) = \sec\left(\frac{\pi}{4}\right) + \csc\left(\frac{\pi}{4}\right) = \sqrt{2} + \sqrt{2} = 2\sqrt{2}
\]

**Answer: (c) 2\sqrt{2}**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | c   | 6 | b   |
| 2 | a   | 7 | a   |
| 3 | a   | 8 | a   |
| 4 | b   | 9 | a   |
| 5 | a   | 10| c   |

</details>
