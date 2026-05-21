# Chapter 6: Chain Rule & Composite Functions

---

## Stage 1: The Core Idea

### The Russian Doll Problem

A Russian doll (Matryoshka) has a doll inside a doll inside a doll. When you open the outer doll, you reveal the next one. They're nested.

Composite functions work the same way: $y = \sin(x^2)$ has $x^2$ nested inside $\sin$. To differentiate it, you can't ignore the nesting — you have to **peel the layers**.

### The Gear Analogy

Imagine three gears connected in a chain:
- Gear A turns and drives Gear B
- Gear B turns and drives Gear C

If A turns at 2 rotations/sec and A drives B at 3× speed, and B drives C at 4× speed, then C turns at $2 \times 3 \times 4 = 24$ rotations/sec.

**The chain rule works identically**: you multiply the derivative of each "layer" together.

If $y = f(g(x))$, then:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$
where $u = g(x)$ is the "inner function".

---

## Stage 2: The Formula Lab

### The Chain Rule

If $y = f(u)$ and $u = g(x)$, then:
$$\frac{dy}{dx} = f'(u) \cdot g'(x) = f'(g(x)) \cdot g'(x)$$

In plain English: **Derivative of outer (keeping inner unchanged) × Derivative of inner.**

### The 3-Step Process

1. Identify the **outer function** and **inner function**.
2. Differentiate the outer function, leaving the inner function intact.
3. Multiply by the derivative of the inner function.

### Extended Chain Rule (Triple Nesting)

If $y = f(g(h(x)))$, then:
$$\frac{dy}{dx} = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

### Trap Warnings

| Trap | Example | Fix |
|------|---------|-----|
| Forgetting the inner derivative | $\frac{d}{dx}\sin(x^2) = \cos(x^2)$ ❌ | Must multiply by $2x$: $2x\cos(x^2)$ ✓ |
| Wrong identification of layers | $e^{x^2}$: outer is $e^u$, inner is $x^2$ | Not $e$ raised to $x$ then squared |
| Missing the chain in denominators | $\frac{d}{dx}\frac{1}{\sin x} = \frac{-1}{\sin^2 x}$ ❌ | Must multiply by $\cos x$: $\frac{-\cos x}{\sin^2 x}$ ✓ |

---

## Stage 3: Type-wise Mastery

### Type 1: Simple Chain Rule (One Layer)

**Goal:** Identify inner function, differentiate outer × inner.

**Solved Example:** ⭐

Differentiate $y = \sin(3x^2 + 1)$.

**Solution:**
```
Outer: sin(·)      → derivative: cos(·)
Inner: u = 3x² + 1 → du/dx = 6x

dy/dx = cos(3x² + 1) · 6x = 6x cos(3x² + 1)
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

1. 🟢 $y = (2x + 5)^4$
<details>
<summary>Solution</summary>

Outer function: `(\cdot)^4 \implies 4(\cdot)^3`. Inner function: `2x+5 \implies 2`.
`y' = 4(2x+5)^3 \cdot 2 =` **8(2x+5)^3**.
</details>

2. 🟢 $y = \cos(5x)$
<details>
<summary>Solution</summary>

Outer: `\cos(\cdot) \implies -\sin(\cdot)`. Inner: `5x \implies 5`.
`y' = -\sin(5x) \cdot 5 =` **-5\sin(5x)**.
</details>

3. 🟡 $y = e^{x^2 - 3x}$
<details>
<summary>Solution</summary>

Outer: `e^{(\cdot)} \implies e^{(\cdot)}`. Inner: `x^2 - 3x \implies 2x - 3`.
`y' = e^{x^2 - 3x} \cdot (2x - 3) =` **(2x - 3)e^{x^2 - 3x}**.
</details>

4. 🟡 $y = \ln(x^2 + 1)$
<details>
<summary>Solution</summary>

Outer: `\ln(\cdot) \implies \frac{1}{(\cdot)}`. Inner: `x^2 + 1 \implies 2x`.
`y' = \frac{1}{x^2 + 1} \cdot (2x) =` **\frac{2x}{x^2 + 1}**.
</details>

5. 🟡 $y = \sqrt{3x^2 - 4x + 1}$
<details>
<summary>Solution</summary>

Outer: `\sqrt{\cdot} \implies \frac{1}{2\sqrt{\cdot}}`. Inner: `3x^2 - 4x + 1 \implies 6x - 4`.
`y' = \frac{1}{2\sqrt{3x^2 - 4x + 1}} \cdot (6x - 4) = \frac{2(3x - 2)}{2\sqrt{3x^2 - 4x + 1}} =` **\frac{3x - 2}{\sqrt{3x^2 - 4x + 1}}**.
</details>

---

### Type 2: Power of a Function — $(f(x))^n$

**Goal:** Apply the chain rule to powers. Result: $n(f(x))^{n-1} \cdot f'(x)$.

**Solved Example:** ⭐

Differentiate $y = (x^2 + \sin x)^5$.

**Solution:**
```
Outer: (·)⁵ → 5(·)⁴
Inner: x² + sin x → 2x + cos x

dy/dx = 5(x² + sin x)⁴ · (2x + cos x)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

6. 🟢 $y = (x^3 - 1)^4$
<details>
<summary>Solution</summary>

`y' = 4(x^3 - 1)^3 \cdot \frac{d}{dx}(x^3 - 1) = 4(x^3 - 1)^3 \cdot (3x^2) =` **12x^2(x^3 - 1)^3**.
</details>

7. 🟡 $y = (e^x + x)^3$
<details>
<summary>Solution</summary>

`y' = 3(e^x + x)^2 \cdot \frac{d}{dx}(e^x + x) =` **3(e^x + x)^2 (e^x + 1)**.
</details>

8. 🟡 $y = \left(\frac{x-1}{x+1}\right)^3$ — *Chain rule + quotient rule for inner.*
<details>
<summary>Solution</summary>

Outer: `3(\frac{x-1}{x+1})^2`.
Inner derivative (quotient rule): `\frac{(1)(x+1) - (x-1)(1)}{(x+1)^2} = \frac{2}{(x+1)^2}`.
`y' = 3\left(\frac{x-1}{x+1}\right)^2 \cdot \frac{2}{(x+1)^2} =` **\frac{6(x-1)^2}{(x+1)^4}**.
</details>

9. 🔴 $y = (\sin x + \cos x)^{10}$
<details>
<summary>Solution</summary>

`y' = 10(\sin x + \cos x)^9 \cdot \frac{d}{dx}(\sin x + \cos x) =` **10(\sin x + \cos x)^9 (\cos x - \sin x)**.
</details>

10. 🔴 $y = (x + \sqrt{x})^{100}$
<details>
<summary>Solution</summary>

`y' = 100(x + \sqrt{x})^{99} \cdot \frac{d}{dx}(x + x^{1/2}) =` **100(x + \sqrt{x})^{99} \left(1 + \frac{1}{2\sqrt{x}}\right)**.
</details>

---

### Type 3: Exponential Chain — $e^{f(x)}$ and $a^{f(x)}$

**Goal:** Derivative of $e^{f(x)}$ is $e^{f(x)} \cdot f'(x)$.

**Solved Example:** ⭐

Differentiate $y = e^{\sin x}$.

**Solution:**
```
Outer: e^(·) → e^(·)
Inner: sin x → cos x

dy/dx = e^(sin x) · cos x
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

11. 🟢 $y = e^{3x}$
<details>
<summary>Solution</summary>

`y' = e^{3x} \cdot \frac{d}{dx}(3x) =` **3e^{3x}**.
</details>

12. 🟡 $y = e^{x^2 + 2x}$
<details>
<summary>Solution</summary>

`y' = e^{x^2 + 2x} \cdot \frac{d}{dx}(x^2 + 2x) =` **(2x + 2)e^{x^2 + 2x}**.
</details>

13. 🟡 $y = 2^{\cos x}$
<details>
<summary>Solution</summary>

Use formula `d/dx(a^u) = a^u \ln a \cdot u'`.
`y' = 2^{\cos x} \ln 2 \cdot (-\sin x) =` **-\sin x \cdot 2^{\cos x} \ln 2**.
</details>

14. 🔴 $y = e^{\sqrt{x^2 + 1}}$
<details>
<summary>Solution</summary>

Outer: `e^{(\cdot)}`. Middle: `\sqrt{\cdot}`. Inner: `x^2+1`.
`y' = e^{\sqrt{x^2+1}} \cdot \frac{1}{2\sqrt{x^2+1}} \cdot (2x) =` **\frac{x e^{\sqrt{x^2+1}}}{\sqrt{x^2+1}}**.
</details>

15. 🟡 $y = e^{e^x}$ — *Double exponential!*
<details>
<summary>Solution</summary>

Outer: `e^{(\cdot)}` with inner `u = e^x`.
`y' = e^{(e^x)} \cdot \frac{d}{dx}(e^x) =` **e^{e^x} \cdot e^x**.
*(Using exponent rules, this is also `e^{e^x + x}`)*
</details>

---

### Type 4: Logarithmic Chain — $\ln(f(x))$

**Goal:** Derivative of $\ln(f(x))$ is $\frac{f'(x)}{f(x)}$.

**Solved Example:** ⭐

Differentiate $y = \ln(x^2 + \cos x)$.

**Solution:**
```
Outer: ln(·) → 1/(·)
Inner: x² + cos x → 2x - sin x

dy/dx = (2x - sin x) / (x² + cos x)
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

16. 🟢 $y = \ln(3x + 5)$
<details>
<summary>Solution</summary>

`y' = \frac{1}{3x + 5} \cdot \frac{d}{dx}(3x + 5) =` **\frac{3}{3x + 5}**.
</details>

17. 🟡 $y = \ln(\sin x)$
<details>
<summary>Solution</summary>

`y' = \frac{1}{\sin x} \cdot \frac{d}{dx}(\sin x) = \frac{\cos x}{\sin x} =` **\cot x**.
</details>

18. 🟡 $y = \ln\left(\frac{x+1}{x-1}\right)$ — *Use log property: $\ln(a/b) = \ln a - \ln b$ first.*
<details>
<summary>Solution</summary>

Rewrite: `y = \ln(x+1) - \ln(x-1)`.
`y' = \frac{1}{x+1}(1) - \frac{1}{x-1}(1)`.
Common denominator: `y' = \frac{(x-1) - (x+1)}{(x+1)(x-1)} = \frac{-2}{x^2 - 1} =` **\frac{2}{1 - x^2}**.
</details>

19. 🔴 $y = \ln(\ln x)$
<details>
<summary>Solution</summary>

Outer: `\ln(\cdot)`. Inner: `\ln x`.
`y' = \frac{1}{\ln x} \cdot \frac{d}{dx}(\ln x) = \frac{1}{\ln x} \cdot \frac{1}{x} =` **\frac{1}{x\ln x}**.
</details>

20. 🔴 $y = x \ln\sqrt{x+1}$
<details>
<summary>Solution</summary>

Rewrite: `\ln\sqrt{x+1} = \ln((x+1)^{1/2}) = \frac{1}{2}\ln(x+1)`.
So `y = \frac{1}{2}x \ln(x+1)`.
Product rule: `y' = \frac{1}{2} \cdot \ln(x+1) + \frac{1}{2}x \cdot \frac{1}{x+1} =` **\frac{1}{2}\ln(x+1) + \frac{x}{2(x+1)}**.
</details>

---

### Type 5: Nested Chain Rule (Double Composition)

**Goal:** Apply the chain rule twice for functions like $y = e^{\sin(x^2)}$.

**Solved Example:** ⭐

Differentiate $y = \sin(e^{3x})$.

**Solution:**
```
Layer 1: sin(·) → cos(·), inner is e^{3x}
Layer 2: e^{3x} → 3e^{3x}

dy/dx = cos(e^{3x}) · 3e^{3x}
```
🔴 Hard ⭐ Must-Do

**Practice Problems:**

21. 🟡 $y = e^{\sin(x^2)}$
<details>
<summary>Solution</summary>

Outer: `e^{(\cdot)}`. Middle: `\sin(\cdot)`. Inner: `x^2`.
`y' = e^{\sin(x^2)} \cdot \cos(x^2) \cdot (2x) =` **2x e^{\sin(x^2)} \cos(x^2)**.
</details>

22. 🟡 $y = \ln(\cos x^2)$
<details>
<summary>Solution</summary>

Outer: `\ln(\cdot) \implies \frac{1}{\cdot}`. Middle: `\cos(\cdot) \implies -\sin(\cdot)`. Inner: `x^2 \implies 2x`.
`y' = \frac{1}{\cos x^2} \cdot (-\sin x^2) \cdot (2x) = -2x \frac{\sin x^2}{\cos x^2} =` **-2x\tan(x^2)**.
</details>

23. 🔴 $y = \cos^2(\sin x)$ — *Outer: $(\cdot)^2$, middle: $\cos(\cdot)$, inner: $\sin x$*
<details>
<summary>Solution</summary>

`y = [\cos(\sin x)]^2`.
Outer: `2(\cdot)^1`. Middle: `\cos \implies -\sin`. Inner: `\sin x \implies \cos x`.
`y' = 2[\cos(\sin x)]^1 \cdot [-\sin(\sin x)] \cdot [\cos x]`.
Use `2\sin A \cos A = \sin 2A`:
`y' =` **-\cos x \sin(2\sin x)**.
</details>

24. 🔴 $y = e^{e^{e^x}}$
<details>
<summary>Solution</summary>

Chain of exponentials:
Derivative of outer `e^{(\cdot)}` is itself.
`y' = e^{e^{e^x}} \cdot \frac{d}{dx}(e^{e^x})`.
`= e^{e^{e^x}} \cdot e^{e^x} \cdot \frac{d}{dx}(e^x) =` **e^{e^{e^x}} e^{e^x} e^x**.
</details>

25. 🔴 $y = \sqrt{\ln\sqrt{x}}$
<details>
<summary>Solution</summary>

Rewrite inner term: `\ln(x^{1/2}) = \frac{1}{2}\ln x`.
So `y = \sqrt{\frac{1}{2}\ln x} = \frac{1}{\sqrt{2}}(\ln x)^{1/2}`.
`y' = \frac{1}{\sqrt{2}} \cdot \frac{1}{2}(\ln x)^{-1/2} \cdot \frac{1}{x} = \frac{1}{2x\sqrt{2\ln x}}`.
Since `\sqrt{2\ln x} = 2\sqrt{\frac{1}{2}\ln x} = 2\sqrt{\ln\sqrt{x}}`,
`y' =` **\frac{1}{4x\sqrt{\ln\sqrt{x}}}**.
</details>

---

### Type 6: Chain Rule with Product/Quotient Rule

**Goal:** Combine chain rule with product or quotient rule.

**Solved Example:** ⭐

Differentiate $y = x^2 e^{\sin x}$.

**Solution:**
```
Product rule: u = x², v = e^{sin x}
u' = 2x
v' = e^{sin x} · cos x  [chain rule]

dy/dx = 2x e^{sin x} + x² e^{sin x} cos x
= x e^{sin x}(2 + x cos x)
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

26. 🟡 $y = x \ln(x^2 + 1)$
<details>
<summary>Solution</summary>

Product rule:
`y' = (1)\ln(x^2 + 1) + x \left(\frac{1}{x^2 + 1} \cdot 2x\right) =` **\ln(x^2 + 1) + \frac{2x^2}{x^2 + 1}**.
</details>

27. 🟡 $y = \frac{e^{2x}}{\sin 3x}$
<details>
<summary>Solution</summary>

Quotient rule (with chain rule on numerator and denominator):
`f = e^{2x} \implies f' = 2e^{2x}`
`g = \sin 3x \implies g' = 3\cos 3x`
`y' = \frac{(2e^{2x})(\sin 3x) - (e^{2x})(3\cos 3x)}{(\sin 3x)^2} =` **\frac{e^{2x}(2\sin 3x - 3\cos 3x)}{\sin^2 3x}**.
</details>

28. 🔴 $y = (x^2 + 1)^3 (x^3 + 2)^4$
<details>
<summary>Solution</summary>

Product rule with chain rule:
`f = (x^2+1)^3 \implies f' = 3(x^2+1)^2(2x) = 6x(x^2+1)^2`
`g = (x^3+2)^4 \implies g' = 4(x^3+2)^3(3x^2) = 12x^2(x^3+2)^3`
`y' = f'g + fg' = 6x(x^2+1)^2(x^3+2)^4 + 12x^2(x^2+1)^3(x^3+2)^3`.
Factor out GCF `6x(x^2+1)^2(x^3+2)^3`:
`= 6x(x^2+1)^2(x^3+2)^3 [ (x^3+2) + 2x(x^2+1) ] =` **6x(x^2+1)^2(x^3+2)^3 (3x^3 + 2x + 2)**.
</details>

29. 🔴 $y = \frac{\sqrt{x+1}}{(x-1)^2}$
<details>
<summary>Solution</summary>

Write as product: `y = (x+1)^{1/2} (x-1)^{-2}`.
`y' = \frac{1}{2}(x+1)^{-1/2}(1)(x-1)^{-2} + (x+1)^{1/2}(-2)(x-1)^{-3}(1)`.
Factor out `(x+1)^{-1/2}(x-1)^{-3}`:
`= (x+1)^{-1/2}(x-1)^{-3} [ \frac{1}{2}(x-1) - 2(x+1) ] = (x+1)^{-1/2}(x-1)^{-3} [ \frac{1}{2}x - \frac{1}{2} - 2x - 2 ]`.
`= (x+1)^{-1/2}(x-1)^{-3} [ -\frac{3}{2}x - \frac{5}{2} ] =` **\frac{-(3x + 5)}{2\sqrt{x+1}(x-1)^3}**.
*(Logarithmic differentiation is easier here!)*
</details>

30. 🔴 $y = x^2 \sin^2 x \cos^2 x$
<details>
<summary>Solution</summary>

Simplify first! `\sin x \cos x = \frac{1}{2}\sin 2x`.
`y = x^2 (\frac{1}{2}\sin 2x)^2 = \frac{1}{4}x^2 \sin^2(2x)`.
Product rule:
`y' = \frac{1}{4} [ 2x\sin^2(2x) + x^2 \cdot 2\sin(2x)\cos(2x)\cdot 2 ]`.
`= \frac{1}{2}x\sin^2(2x) + x^2\sin(2x)\cos(2x)`.
`=` **\frac{1}{2}x\sin(2x) [ \sin 2x + 2x\cos 2x ]**.
</details>

---

## Stage 4: Type Mixer

1. 🟡 Differentiate $y = e^x \sin(x^2)$. *[Product + Chain]*
<details>
<summary>Solution</summary>

Product rule: `f = e^x \implies f'=e^x`. `g = \sin(x^2) \implies g' = \cos(x^2)\cdot 2x`.
`y' = (e^x)\sin(x^2) + e^x(2x\cos(x^2)) =` **e^x [ \sin(x^2) + 2x\cos(x^2) ]**.
</details>

2. 🔴 Differentiate $y = \left(\frac{e^x - e^{-x}}{2}\right)^3$. *[Power chain on sinh x]*
<details>
<summary>Solution</summary>

Outer function: `(\cdot)^3`. Inner function: `\frac{e^x - e^{-x}}{2}`.
Inner derivative: `\frac{e^x - (-e^{-x})}{2} = \frac{e^x + e^{-x}}{2}`.
`y' = 3\left(\frac{e^x - e^{-x}}{2}\right)^2 \cdot \left(\frac{e^x + e^{-x}}{2}\right) =` **\frac{3}{8}(e^x - e^{-x})^2(e^x + e^{-x})**.
</details>

3. 🔴 Differentiate $y = \ln\left(\frac{\sqrt{x+1}}{(x-1)^2}\right)$. *[Log rule simplification then differentiate]*
<details>
<summary>Solution</summary>

Simplify first: `y = \ln((x+1)^{1/2}) - \ln((x-1)^2) = \frac{1}{2}\ln(x+1) - 2\ln(x-1)`.
Differentiate: `y' = \frac{1}{2(x+1)}(1) - \frac{2}{x-1}(1)`.
Common denominator: `\frac{(x-1) - 4(x+1)}{2(x+1)(x-1)} = \frac{-3x - 5}{2(x^2 - 1)} =` **-\frac{3x + 5}{2(x^2 - 1)}**.
</details>

4. 🔴 Differentiate $y = e^{x^2} \cos(x^2) \sin(x^2)$. *[Simplify, then chain + product]*
<details>
<summary>Solution</summary>

Simplify: `\cos(x^2)\sin(x^2) = \frac{1}{2}\sin(2x^2)`.
`y = \frac{1}{2} e^{x^2} \sin(2x^2)`.
Product rule: `f = \frac{1}{2}e^{x^2} \implies f' = x e^{x^2}`. `g = \sin(2x^2) \implies g' = \cos(2x^2)\cdot 4x`.
`y' = (x e^{x^2})\sin(2x^2) + (\frac{1}{2}e^{x^2})(4x\cos(2x^2)) =` **x e^{x^2} [ \sin(2x^2) + 2\cos(2x^2) ]**.
</details>

5. 🔴 If $y = (f(g(x)))^n$, express $\frac{dy}{dx}$ in terms of $f$, $g$, $f'$, $g'$.
<details>
<summary>Solution</summary>

Apply power rule, then chain rule twice:
1. Outer `(\cdot)^n \implies n(\cdot)^{n-1}`.
2. Middle `f(g(x)) \implies f'(g(x))`.
3. Inner `g(x) \implies g'(x)`.
`y' =` **n [f(g(x))]^{n-1} \cdot f'(g(x)) \cdot g'(x)**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Differentiate $y = e^{3x} \sin 2x$. **(3 marks)**

**Solution:**
Product rule: $u = e^{3x}, v = \sin 2x$
$u' = 3e^{3x}$ (chain); $v' = 2\cos 2x$ (chain)
$y' = 3e^{3x} \sin 2x + 2e^{3x} \cos 2x = e^{3x}(3\sin 2x + 2\cos 2x)$

---

**Q2.** 🟡 Differentiate $y = \ln\sqrt{\frac{1-x}{1+x}}$. **(3 marks)**

**Solution:**
$y = \frac{1}{2}\ln\frac{1-x}{1+x} = \frac{1}{2}[\ln(1-x) - \ln(1+x)]$
$y' = \frac{1}{2}\left[\frac{-1}{1-x} - \frac{1}{1+x}\right] = \frac{1}{2} \cdot \frac{-(1+x)-(1-x)}{(1-x)(1+x)} = \frac{1}{2} \cdot \frac{-2}{1-x^2} = \frac{-1}{1-x^2}$

---

**Q3.** 🔴 Differentiate $y = \frac{\sqrt{x-1} - \sqrt{x+1}}{\sqrt{x-1} + \sqrt{x+1}}$. **(4 marks)**

**Solution:**
Rationalise: multiply top and bottom by $(\sqrt{x-1} - \sqrt{x+1})$:
$y = \frac{(\sqrt{x-1} - \sqrt{x+1})^2}{(x-1) - (x+1)} = \frac{(x-1) - 2\sqrt{x^2-1} + (x+1)}{-2} = \frac{2x - 2\sqrt{x^2-1}}{-2} = \sqrt{x^2-1} - x$
$y' = \frac{x}{\sqrt{x^2-1}} - 1$

---

## Stage 6: JEE Mains Arena

**Q1.** If $y = \sin\left(\ln\frac{x^2+1}{x^2-1}\right)$, then $\frac{dy}{dx}$ at $x=2$ equals:
(a) $\frac{-8\cos(\ln(5/3))}{9}$   <br>(b) $\frac{8\cos(\ln(5/3))}{9}$   <br>(c) $\frac{-8}{9}$   <br>(d) $0$

<details>
<summary>Solution</summary>
Let u = ln((x²+1)/(x²-1)).
du/dx = [(x²-1)/(x²+1)] · [(x²-1)(2x) - (x²+1)(2x)] / (x²-1)²
= [(2x)(x²-1-x²-1)] / [(x²+1)(x²-1)]
= (2x)(-2) / (x⁴-1) = -4x/(x⁴-1)

dy/dx = cos(u) · (-4x/(x⁴-1))

At x=2: u = ln(5/3), -4(2)/(16-1) = -8/15.
dy/dx = cos(ln(5/3)) · (-8/15).
Answer: (a) (approximately) 🔴
</details>

---

**Q2.** If $f(x) = g(h(x))$ where $g(2) = 3$, $g'(2) = 4$, $h(1) = 2$, $h'(1) = 5$, then $f'(1) =$:
(a) $15$   <br>(b) $20$   <br>(c) $12$   <br>(d) $8$

<details>
<summary>Solution</summary>
f'(x) = g'(h(x)) · h'(x)
f'(1) = g'(h(1)) · h'(1) = g'(2) · 5 = 4 · 5 = 20.
Answer: (b) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.**
<br>**Assertion (A):** $\frac{d}{dx}\left[e^{\sin x}\right] = e^{\sin x} \cos x$
<br>**Reason (R):** The derivative of $e^{f(x)}$ is $e^{f(x)} \cdot f'(x)$ by the chain rule.

<details>
<summary>Solution</summary>
A is true: Outer = e^(·), inner = sin x, inner derivative = cos x.
R is true and correctly explains A.
Answer: (a) 🟢
</details>

---

**Q2.**
<br>**Assertion (A):** $\frac{d}{dx}[\ln(\sin x)] = \cot x$
<br>**Reason (R):** $\frac{d}{dx}[\ln(f(x))] = \frac{f'(x)}{f(x)}$, and $\frac{\cos x}{\sin x} = \cot x$.

<details>
<summary>Solution</summary>
A is true: derivative = cos x / sin x = cot x.
R is true and gives the exact derivation.
Answer: (a) 🟢 ⭐
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 $\frac{d}{dx}[\sin(5x^3)] = $
   <br>(a) $\cos(5x^3)$   <br>(b) $15x^2\cos(5x^3)$   <br>(c) $5\cos(5x^3)$   <br>(d) $-15x^2\sin(5x^3)$

2. 🟢 $\frac{d}{dx}[e^{4x-1}] = $
   <br>(a) $4e^{4x}$   <br>(b) $e^{4x-1}$   <br>(c) $4e^{4x-1}$   <br>(d) $(4x-1)e^{4x-2}$

3. 🟡 ⭐ $\frac{d}{dx}[(x^2+1)^{10}] = $
   <br>(a) $10(x^2+1)^9$   <br>(b) $20x(x^2+1)^9$   <br>(c) $10x(x^2+1)^9$   <br>(d) $20(x^2+1)^9$

4. 🟡 $\frac{d}{dx}[\ln(\tan x)] = $
   <br>(a) $\cot x$   <br>(b) $2\csc 2x$   <br>(c) $\sec^2 x$   <br>(d) $\tan x$

5. 🔴 $\frac{d}{dx}[\cos^3(e^x)] = $
   <br>(a) $-3\cos^2(e^x)\sin(e^x)$   <br>(b) $-3e^x\cos^2(e^x)\sin(e^x)$   <br>(c) $3e^x\cos^2(e^x)\sin(e^x)$   <br>(d) $3\cos^2(e^x)$

6. 🟡 $\frac{d}{dx}[\ln(\sec x + \tan x)] = $
   <br>(a) $\sec x \tan x + \sec^2 x$   <br>(b) $\sec x$   <br>(c) $\csc x$   <br>(d) $\tan x$

7. 🟡 ⭐ If $y = f(x^2)$ and $f'(x) = \sin x$, then $\frac{dy}{dx} = $
   <br>(a) $\sin(x^2)$   <br>(b) $2x\sin(x^2)$   <br>(c) $\cos(x^2)$   <br>(d) $2\sin(x)$

8. 🔴 $\frac{d}{dx}\left[\sqrt{\frac{1-x}{1+x}}\right] = $
   <br>(a) $\frac{-1}{(1+x)\sqrt{1-x^2}}$   <br>(b) $\frac{1}{\sqrt{1-x^2}}$   <br>(c) $\frac{-1}{\sqrt{1-x^2}}$   <br>(d) $\frac{1}{(1+x)\sqrt{1-x^2}}$

9. 🔴 ⭐ $\frac{d}{dx}[e^{\sqrt{\sin\sqrt{x}}}] = $
   <br>(a) $e^{\sqrt{\sin\sqrt{x}}}$   <br>(b) $\frac{e^{\sqrt{\sin\sqrt{x}}} \cos\sqrt{x}}{4\sqrt{x}\sqrt{\sin\sqrt{x}}}$   <br>(c) $\frac{e^{\sqrt{\sin\sqrt{x}}} \cos\sqrt{x}}{4\sqrt{x\sin\sqrt{x}}}$   <br>(d) None of above

10. 🟡 If $g(x) = f(2x+1)$, and $f'(x) = x^2$, then $g'(2) = $
    <br>(a) $4$   <br>(b) $25$   <br>(c) $50$   <br>(d) $100$

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans |
|---|-----|---|-----|
| 1 | b | 6 | b |
| 2 | c | 7 | b |
| 3 | b | 8 | a |
| 4 | b | 9 | c |
| 5 | b | 10 | c |

</details>

---

## What's Next?

You can now differentiate any explicit function of x. But what about the equation of a circle: $x^2 + y^2 = 25$? You can't write $y$ as a simple function of $x$. We need a new technique.

In **Chapter 7**, we tackle **Continuity** — the deep concept that asks not just whether a function has a value at a point, but whether it *flows* through that point without any jumps or breaks.
