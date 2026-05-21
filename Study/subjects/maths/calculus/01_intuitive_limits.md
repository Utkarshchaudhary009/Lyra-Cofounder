# Chapter 1: The Idea of Limits

---

## Stage 1: The Core Idea

### The Speedometer Problem

You're driving a car. The speedometer reads 80 km/h. But what does that *mean*?

Speed = Distance ÷ Time. If you drive 80 km in 1 hour, your **average** speed is 80 km/h. But the speedometer doesn't show average speed — it shows your speed *right now*, at this exact instant.

Here's the paradox: at a single instant, you travel **zero distance** in **zero time**. So speed = 0/0. That's undefined!

Yet the speedometer *does* show a number. How?

**The answer is limits.**

Instead of asking "what is your speed at this instant?", we ask: "what does your speed *approach* as the time interval gets smaller and smaller?"

| Time interval | Distance covered | Average speed |
|--------------|-----------------|---------------|
| 1 hour | 80 km | 80 km/h |
| 1 minute | 1.334 km | 80.04 km/h |
| 1 second | 0.02222 km | 80.0 km/h |
| 0.001 second | 0.00002222 km | 80.0 km/h |
| → 0 | → 0 | → **80 km/h** |

As the time interval **approaches zero**, the average speed **approaches 80**. That's what the speedometer shows. That's a limit.

### What Is a Limit?

> **lim(x→a) f(x) = L** means: as x gets closer and closer to a (but never equals a), f(x) gets closer and closer to L.

**Critical insight:** A limit is about *approaching*, not *arriving*. We never plug in x = a. We ask: what value is f(x) heading towards?

### Left-Hand and Right-Hand Limits

Sometimes a function approaches *different* values from the left and right:

```
         |
    2 ───●        (value from left)
         |
    1    |   ○─── (value from right)
         |
    ─────┼─────
         a
```

- **Left-Hand Limit (LHL):** lim(x→a⁻) f(x) = value approached from the left
- **Right-Hand Limit (RHL):** lim(x→a⁺) f(x) = value approached from the right

> **The limit exists if and only if LHL = RHL.**

If LHL ≠ RHL, the limit **Does Not Exist (DNE)**.

### When Does a Limit NOT Exist?

| Case | Example | Why |
|------|---------|-----|
| LHL ≠ RHL | Jump in graph | Function approaches different values |
| Infinite oscillation | sin(1/x) near x = 0 | Keeps bouncing, never settles |
| Unbounded | 1/x² near x = 0 | Shoots to ∞ |

### The Big Distinction

| Question | About |
|----------|-------|
| What is f(a)? | The **value** of the function AT x = a |
| What is lim(x→a) f(x)? | What f(x) **approaches** NEAR x = a |

These can be different! A function can have:
- A limit at x = a but no value (hole in graph)
- A value at x = a but no limit (jump)
- Both, and they're equal (continuous — Chapter 7)
- Both, but they're different (removable discontinuity)

---

## Stage 2: The Formula Lab

### Limit Laws

If lim(x→a) f(x) = L and lim(x→a) g(x) = M, then:

| Law | Formula | Trap Warning |
|-----|---------|-------------|
| Sum | lim [f(x) + g(x)] = L + M | Both limits must exist individually |
| Difference | lim [f(x) − g(x)] = L − M | — |
| Product | lim [f(x) · g(x)] = L · M | — |
| Quotient | lim [f(x)/g(x)] = L/M | **Only if M ≠ 0** |
| Constant | lim [c · f(x)] = c · L | — |
| Power | lim [f(x)]ⁿ = Lⁿ | n must be a positive integer, or L > 0 |

### Direct Substitution

If f(x) is a polynomial or rational function and f(a) is defined:

> **lim(x→a) f(x) = f(a)**

This is the first method you try. If it gives a real number, you're done.

### Indeterminate Forms

When direct substitution gives one of these, you need more work:

| Form | Example | What to do |
|------|---------|-----------|
| **0/0** | lim(x→2) (x²−4)/(x−2) | Factor, rationalize, or use standard limits |
| **∞/∞** | lim(x→∞) (3x²+1)/(x²−5) | Divide by highest power |
| **∞ − ∞** | lim(x→0) (1/x − 1/sin x) | Combine fractions |
| **0 × ∞** | lim(x→0⁺) x · ln x | Rewrite as 0/0 or ∞/∞ |

> ⚠️ **Trap:** 0/0 does NOT mean the limit is 0. It means the limit is *undetermined* — it could be any number. You must simplify further.

### Squeeze (Sandwich) Theorem

If g(x) ≤ f(x) ≤ h(x) near x = a, and lim g(x) = lim h(x) = L, then lim f(x) = L.

```
  h(x) ──────╲╱──────  (upper bound)
  f(x) ──────╳──────   (squeezed)
  g(x) ──────╱╲──────  (lower bound)
              a
```

**Classic application:** lim(x→0) x² sin(1/x) = 0, because −x² ≤ x² sin(1/x) ≤ x².

---

## Stage 3: Type-wise Mastery

### Type 1: Limits by Direct Substitution

**Goal:** Evaluate limits where plugging in directly works.

**Solved Example:**

Find lim(x→3) (2x² − 5x + 1)

**Solution:**
```
Substitute x = 3:
= 2(9) − 5(3) + 1
= 18 − 15 + 1
= 4
```
🟢 Easy

**Practice Problems:**

1. 🟢 lim(x→2) (x³ − 3x + 7)
<details>
<summary>Solution</summary>

Substitute `x = 2`:
= 2³ − 3(2) + 7
= 8 − 6 + 7 = **9**
</details>

2. 🟢 lim(x→−1) (x² + 4x + 3)
<details>
<summary>Solution</summary>

Substitute `x = -1`:
= (-1)² + 4(-1) + 3
= 1 − 4 + 3 = **0**
</details>

3. 🟢 lim(x→0) (5x + cos 0) — *Hint: cos is continuous*
<details>
<summary>Solution</summary>

Substitute `x = 0`:
= 5(0) + cos(0)
= 0 + 1 = **1**
</details>

4. 🟢 lim(x→1) (x⁴ − 1)/(x − 1) — *Wait! Try substituting first. What happens?*
<details>
<summary>Solution</summary>

Substitute `x = 1`:
= (1⁴ − 1) / (1 − 1)
= **0/0** (Indeterminate form! This requires techniques from Type 2 or 4, substitution alone fails here.)
</details>

5. 🟢 lim(x→4) √x
<details>
<summary>Solution</summary>

Substitute `x = 4`:
= √4 = **2**
</details>

6. 🟢 lim(x→-2) (2x³ + x² - 5x + 3)
<details>
<summary>Solution</summary>

Substitute `x = -2`:
= 2(-8) + (-2)² - 5(-2) + 3
= -16 + 4 + 10 + 3 = **1**
</details>

7. 🟢 lim(x→π/4) (sin x + cos x)
<details>
<summary>Solution</summary>

Substitute `x = π/4`:
= sin(π/4) + cos(π/4)
= 1/√2 + 1/√2 = 2/√2 = **√2**
</details>

8. 🟢 lim(x→0) (e^x + cos x - 1)
<details>
<summary>Solution</summary>

Substitute `x = 0`:
= e⁰ + cos(0) - 1
= 1 + 1 - 1 = **1**
</details>

9. 🟢 lim(x→1) ln(2x)
<details>
<summary>Solution</summary>

Substitute `x = 1`:
= ln(2(1)) = **ln 2**
</details>

10. 🟢 lim(x→-3) (x² + 7x + 12)/(x + 4)
<details>
<summary>Solution</summary>

Substitute `x = -3`:
= ((-3)² + 7(-3) + 12) / (-3 + 4)
= (9 - 21 + 12) / 1
= 0 / 1 = **0**
</details>

11. 🟢 lim(x→0) (2x³ - 3x² + x + 7)
<details>
<summary>Solution</summary>

Substitute `x = 0`:
= 2(0)³ - 3(0)² + 0 + 7 = **7**
</details>

12. 🟢 lim(x→2) (x + 1)(x - 3)
<details>
<summary>Solution</summary>

Substitute `x = 2`:
= (2 + 1)(2 - 3)
= 3(-1) = **-3**
</details>

13. 🟢 lim(x→3) (x² + 1)/(x + 1)
<details>
<summary>Solution</summary>

Substitute `x = 3`:
= (3² + 1) / (3 + 1)
= 10 / 4 = **5/2**
</details>

14. 🟢 lim(x→0) 2^x
<details>
<summary>Solution</summary>

Substitute `x = 0`:
= 2⁰ = **1**
</details>

---

### Type 2: 0/0 Form — Factorization Method

**Goal:** When substitution gives 0/0, factor and cancel.

**Solved Example:** ⭐

Find lim(x→2) (x² − 4)/(x − 2)

**Solution:**
```
Direct substitution: (4 − 4)/(2 − 2) = 0/0 → Indeterminate!

Factor numerator: x² − 4 = (x − 2)(x + 2)

lim(x→2) (x − 2)(x + 2) / (x − 2)
= lim(x→2) (x + 2)       [cancel (x − 2), valid since x ≠ 2]
= 2 + 2
= 4
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

6. 🟢 ⭐ lim(x→3) (x² − 9)/(x − 3)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x² − 9 = (x−3)(x+3)
`lim(x→3) (x−3)(x+3)/(x−3) = lim(x→3) (x+3)`
= 3 + 3 = **6**
</details>

7. 🟢 lim(x→−1) (x² − 1)/(x + 1)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x² − 1 = (x−1)(x+1)
`lim(x→-1) (x−1)(x+1)/(x+1) = lim(x→-1) (x−1)`
= -1 - 1 = **-2**
</details>

8. 🟡 lim(x→1) (x³ − 1)/(x − 1) — *Use a³ − b³ = (a−b)(a²+ab+b²)*
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x³ − 1 = (x−1)(x² + x + 1)
`lim(x→1) (x−1)(x² + x + 1)/(x−1) = lim(x→1) (x² + x + 1)`
= 1² + 1 + 1 = **3**
</details>

9. 🟡 ⭐ lim(x→2) (x³ − 8)/(x² − 4)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x³ − 8 = (x−2)(x² + 2x + 4)
Factor denominator: x² − 4 = (x−2)(x+2)
`lim(x→2) (x−2)(x² + 2x + 4) / ((x−2)(x+2)) = lim(x→2) (x² + 2x + 4) / (x+2)`
= (4 + 4 + 4) / (2 + 2) = 12 / 4 = **3**
</details>

10. 🟡 lim(x→a) (x² − a²)/(x − a)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x² − a² = (x−a)(x+a)
`lim(x→a) (x−a)(x+a)/(x−a) = lim(x→a) (x+a)`
= a + a = **2a**
</details>

11. 🟡 ⭐ lim(x→-2) (x³ + 8)/(x + 2)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x³ + 8 = (x+2)(x² − 2x + 4)
`lim(x→-2) (x+2)(x² − 2x + 4)/(x+2) = lim(x→-2) (x² − 2x + 4)`
= (-2)² - 2(-2) + 4 = 4 + 4 + 4 = **12**
</details>

12. 🟡 lim(x→1) (x² - 3x + 2)/(x² - 5x + 4)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x² - 3x + 2 = (x-1)(x-2)
Factor denominator: x² - 5x + 4 = (x-1)(x-4)
`lim(x→1) (x-1)(x-2) / ((x-1)(x-4)) = lim(x→1) (x-2)/(x-4)`
= (1 - 2) / (1 - 4) = -1 / -3 = **1/3**
</details>

13. 🟡 ⭐ lim(x→0) (x³ - x)/(x² + x)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x(x² - 1) = x(x-1)(x+1)
Factor denominator: x(x + 1)
`lim(x→0) x(x-1)(x+1) / (x(x+1)) = lim(x→0) (x-1)`
= 0 - 1 = **-1**
</details>

14. 🟡 lim(x→2) (x² - 4)/(x³ - 8)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: (x-2)(x+2)
Factor denominator: (x-2)(x² + 2x + 4)
`lim(x→2) (x+2) / (x² + 2x + 4)`
= (2 + 2) / (4 + 4 + 4) = 4 / 12 = **1/3**
</details>

15. 🔴 lim(x→-1) (x³ + 1)/(x² + 3x + 2)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: x³ + 1 = (x+1)(x² - x + 1)
Factor denominator: x² + 3x + 2 = (x+1)(x+2)
`lim(x→-1) (x² - x + 1) / (x+2)`
= (1 - (-1) + 1) / (-1 + 2) = 3 / 1 = **3**
</details>

16. 🟡 lim(x→2) (x⁴ - 16)/(x³ - 8)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: (x²-4)(x²+4) = (x-2)(x+2)(x²+4)
Factor denominator: (x-2)(x² + 2x + 4)
`lim(x→2) (x+2)(x²+4) / (x² + 2x + 4)`
= (4)(8) / (4 + 4 + 4) = 32 / 12 = **8/3**
</details>

17. 🟡 ⭐ lim(x→0) (4x² - 9x)/(2x² + 3x)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor: `lim(x→0) x(4x - 9) / (x(2x + 3))`
= `lim(x→0) (4x - 9)/(2x + 3)`
= -9 / 3 = **-3**
</details>

18. 🟡 lim(x→4) (x² - 16)/(x³ - 64)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: (x-4)(x+4)
Factor denominator: (x-4)(x² + 4x + 16)
`lim(x→4) (x+4) / (x² + 4x + 16)`
= 8 / (16 + 16 + 16) = 8 / 48 = **1/6**
</details>

19. 🟡 lim(x→3) (x² - x - 6)/(x² - 4x + 3)
<details>
<summary>Solution</summary>

Direct sub gives 0/0.
Factor numerator: (x-3)(x+2)
Factor denominator: (x-3)(x-1)
`lim(x→3) (x+2) / (x-1)`
= (3+2) / (3-1) = **5/2**
</details>

---

### Type 3: 0/0 Form — Rationalization Method

**Goal:** When square roots create 0/0, multiply by conjugate.

**Solved Example:** ⭐

Find lim(x→0) (√(1+x) − 1)/x

**Solution:**
```
Substitution: (1 − 1)/0 = 0/0 → Indeterminate!

Multiply by conjugate:
= lim (√(1+x) − 1)/x × (√(1+x) + 1)/(√(1+x) + 1)
= lim (1+x − 1) / [x(√(1+x) + 1)]
= lim x / [x(√(1+x) + 1)]
= lim 1/(√(1+x) + 1)
= 1/(1 + 1) = 1/2
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

11. 🟡 ⭐ lim(x→0) (√(1+x) − √(1−x))/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `(√(1+x) + √(1−x)) / (√(1+x) + √(1−x))`
Numerator becomes: `(1+x) - (1−x) = 2x`
`lim(x→0) 2x / (x(√(1+x) + √(1−x)))`
`= lim(x→0) 2 / (√(1+x) + √(1−x))`
= 2 / (√1 + √1) = 2 / 2 = **1**
</details>

12. 🟡 lim(x→0) (√(a+x) − √a)/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `(√(a+x) + √a) / (√(a+x) + √a)`
Numerator becomes: `(a+x) - a = x`
`lim(x→0) x / (x(√(a+x) + √a))`
`= lim(x→0) 1 / (√(a+x) + √a)`
= 1 / (√a + √a) = **1 / (2√a)**
</details>

13. 🟡 lim(x→4) (√x − 2)/(x − 4)
<details>
<summary>Solution</summary>

Factor denominator: `x - 4 = (√x - 2)(√x + 2)`
`lim(x→4) (√x - 2) / ((√x - 2)(√x + 2))`
`= lim(x→4) 1 / (√x + 2)`
= 1 / (√4 + 2) = 1 / (2 + 2) = **1/4**
</details>

14. 🔴 lim(x→0) (√(1+x) − √(1−x))/(∛(1+x) − 1)
<details>
<summary>Solution</summary>

Rationalize both numerator and denominator.
For numerator, multiply by `√(1+x) + √(1−x)`. Numerator becomes `2x`.
For denominator, use `a³ - b³ = (a-b)(a² + ab + b²)`.
Multiply by `(1+x)^(2/3) + (1+x)^(1/3) + 1`. Denominator becomes `(1+x) - 1 = x`.
`lim(x→0) [2x / (√(1+x) + √(1−x))] * [((1+x)^(2/3) + (1+x)^(1/3) + 1) / x]`
`= lim(x→0) 2 * ((1+x)^(2/3) + (1+x)^(1/3) + 1) / (√(1+x) + √(1−x))`
= 2 * (1 + 1 + 1) / (1 + 1) = 2 * 3 / 2 = **3**
</details>

15. 🟡 lim(x→1) (√x − 1)/(x − 1)
<details>
<summary>Solution</summary>

Factor denominator: `x - 1 = (√x - 1)(√x + 1)`
`lim(x→1) (√x - 1) / ((√x - 1)(√x + 1))`
`= lim(x→1) 1 / (√x + 1)`
= 1 / (√1 + 1) = **1/2**
</details>

16. 🟡 lim(x→0) (√(1+2x) - 1)/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(1+2x) + 1`
Numerator becomes: `1+2x - 1 = 2x`
`lim(x→0) 2x / (x(√(1+2x) + 1))`
`= lim(x→0) 2 / (√(1+2x) + 1)`
= 2 / (1 + 1) = **1**
</details>

17. 🟡 ⭐ lim(x→0) (√(4+x) - 2)/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(4+x) + 2`
Numerator becomes: `4+x - 4 = x`
`lim(x→0) x / (x(√(4+x) + 2))`
`= lim(x→0) 1 / (√(4+x) + 2)`
= 1 / (√4 + 2) = **1/4**
</details>

18. 🟡 lim(x→2) (√(x+2) - 2)/(x - 2)
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(x+2) + 2`
Numerator becomes: `x+2 - 4 = x-2`
`lim(x→2) (x-2) / ((x-2)(√(x+2) + 2))`
`= lim(x→2) 1 / (√(x+2) + 2)`
= 1 / (√4 + 2) = **1/4**
</details>

19. 🔴 ⭐ lim(x→0) (√(1+x+x²) - 1)/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(1+x+x²) + 1`
Numerator becomes: `1+x+x² - 1 = x+x² = x(1+x)`
`lim(x→0) x(1+x) / (x(√(1+x+x²) + 1))`
`= lim(x→0) (1+x) / (√(1+x+x²) + 1)`
= (1+0) / (√1 + 1) = **1/2**
</details>

20. 🟡 lim(x→1) (√(x²+3) - 2)/(x - 1)
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(x²+3) + 2`
Numerator becomes: `x²+3 - 4 = x²-1 = (x-1)(x+1)`
`lim(x→1) (x-1)(x+1) / ((x-1)(√(x²+3) + 2))`
`= lim(x→1) (x+1) / (√(x²+3) + 2)`
= (1+1) / (√4 + 2) = 2 / 4 = **1/2**
</details>

21. 🔴 lim(x→0) (√(1+sin x) - 1)/x
<details>
<summary>Solution</summary>

Multiply by conjugate: `√(1+sin x) + 1`
Numerator becomes: `1+sin x - 1 = sin x`
`lim(x→0) (sin x) / (x(√(1+sin x) + 1))`
We know `lim(x→0) (sin x)/x = 1`.
`= 1 * 1 / (√(1+0) + 1) = 1 * 1 / 2` = **1/2**
</details>

22. 🟡 lim(x→a) (√x - √a)/(x - a)
<details>
<summary>Solution</summary>

Factor denominator: `x - a = (√x - √a)(√x + √a)`
`lim(x→a) (√x - √a) / ((√x - √a)(√x + √a))`
`= lim(x→a) 1 / (√x + √a)`
= 1 / (√a + √a) = **1 / (2√a)**
</details>

23. 🟡 ⭐ lim(x→0) (√(1+x²) - 1)/(√(1+x) - 1)
<details>
<summary>Solution</summary>

Rationalize both:
Multiply by `(√(1+x²) + 1)(√(1+x) + 1)`
Numerator becomes: `(1+x² - 1) * (√(1+x) + 1) = x² * (√(1+x) + 1)`
Denominator becomes: `(1+x - 1) * (√(1+x²) + 1) = x * (√(1+x²) + 1)`
`lim(x→0) [x² * (√(1+x) + 1)] / [x * (√(1+x²) + 1)]`
`= lim(x→0) x * (√(1+x) + 1) / (√(1+x²) + 1)`
= 0 * (√1 + 1) / (√1 + 1) = 0 * 2 / 2 = **0**
</details>

24. 🟡 lim(x→0) (√(1+x) - √(1-x))/(√(1+2x) - √(1-2x))
<details>
<summary>Solution</summary>

Rationalize both:
Numerator difference of squares: `(1+x) - (1-x) = 2x`
Denominator difference of squares: `(1+2x) - (1-2x) = 4x`
`lim(x→0) [2x * (√(1+2x) + √(1-2x))] / [4x * (√(1+x) + √(1-x))]`
`= lim(x→0) [2 * (√(1+2x) + √(1-2x))] / [4 * (√(1+x) + √(1-x))]`
= [2 * (√1 + √1)] / [4 * (√1 + √1)] = (2 * 2) / (4 * 2) = 4 / 8 = **1/2**
</details>

---

### Type 4: Limits Using the Formula lim(x→a) (xⁿ − aⁿ)/(x − a) = naⁿ⁻¹

**Goal:** Apply the standard algebraic limit.

**Solved Example:**

Find lim(x→1) (x¹⁰ − 1)/(x − 1)

**Solution:**
```
This is exactly the form (xⁿ − aⁿ)/(x − a) with n = 10, a = 1.
= 10 × 1⁹ = 10
```
🟢 Easy ⭐ Must-Do

**Practice Problems:**

16. 🟢 ⭐ lim(x→2) (x⁵ − 32)/(x − 2)
<details>
<summary>Solution</summary>

This is the form `(xⁿ − aⁿ)/(x − a)` with `n = 5`, `a = 2`.
Formula `naⁿ⁻¹` = 5(2⁴) = 5(16) = **80**
</details>

17. 🟡 lim(x→1) (x⁴ − 1)/(x³ − 1) — *Split as two standard limits*
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-1)`:
`= lim(x→1) [(x⁴ - 1)/(x - 1)] / [(x³ - 1)/(x - 1)]`
Apply formula to both:
= (4 * 1³) / (3 * 1²) = **4/3**
</details>

18. 🟡 lim(x→3) (x⁴ − 81)/(x² − 9)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-3)`:
`= lim(x→3) [(x⁴ - 3⁴)/(x - 3)] / [(x² - 3²)/(x - 3)]`
Apply formula:
= (4 * 3³) / (2 * 3¹) = (4 * 27) / (2 * 3) = 108 / 6 = **18**
</details>

19. 🟡 lim(x→a) (x^(3/2) − a^(3/2))/(x − a) — *Works for fractional n too!*
<details>
<summary>Solution</summary>

This is the exact form `(xⁿ − aⁿ)/(x − a)` with `n = 3/2`.
Formula `naⁿ⁻¹` = (3/2)a^(3/2 - 1) = **(3/2)a^(1/2)** or **(3/2)√a**
</details>

20. 🔴 lim(x→1) (x^m − 1)/(x^n − 1)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-1)`:
`= lim(x→1) [(x^m - 1)/(x - 1)] / [(x^n - 1)/(x - 1)]`
Apply formula `k(1)^(k-1)`:
= m(1) / n(1) = **m/n**
</details>

21. 🟡 lim(x→2) (x⁶ - 64)/(x² - 4)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-2)`:
`= lim(x→2) [(x⁶ - 2⁶)/(x - 2)] / [(x² - 2²)/(x - 2)]`
Apply formula:
= (6 * 2⁵) / (2 * 2¹) = (6 * 32) / 4 = 192 / 4 = **48**
</details>

22. 🟡 ⭐ lim(x→1) (x⁵ - 1)/(x³ - 1)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-1)`:
`= lim(x→1) [(x⁵ - 1)/(x - 1)] / [(x³ - 1)/(x - 1)]`
Apply formula:
= (5 * 1⁴) / (3 * 1²) = **5/3**
</details>

23. 🟡 lim(x→a) (x⁴ - a⁴)/(x³ - a³)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-a)`:
`= lim(x→a) [(x⁴ - a⁴)/(x - a)] / [(x³ - a³)/(x - a)]`
Apply formula:
= (4a³) / (3a²) = **(4/3)a**
</details>

24. 🔴 lim(x→0) ((1+x)ⁿ - 1)/x
<details>
<summary>Solution</summary>

Let `t = 1+x`. As `x→0`, `t→1`. Also `x = t-1`.
Substitute into limit:
`= lim(t→1) (tⁿ - 1) / (t - 1)`
Apply formula:
= n(1)ⁿ⁻¹ = **n**
</details>

25. 🟡 lim(x→1) (x¹² - 1)/(x⁴ - 1)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-1)`:
`= lim(x→1) [(x¹² - 1)/(x - 1)] / [(x⁴ - 1)/(x - 1)]`
Apply formula:
= (12 * 1¹¹) / (4 * 1³) = 12 / 4 = **3**
</details>

26. 🟡 ⭐ lim(x→2) (x⁷ - 128)/(x⁵ - 32)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-2)`:
`= lim(x→2) [(x⁷ - 2⁷)/(x - 2)] / [(x⁵ - 2⁵)/(x - 2)]`
Apply formula:
= (7 * 2⁶) / (5 * 2⁴) = 7(64) / 5(16) = (7 * 4) / 5 = **28/5**
</details>

27. 🟡 lim(x→1) (x^(2/3) - 1)/(x^(1/3) - 1)
<details>
<summary>Solution</summary>

Divide numerator and denominator by `(x-1)`:
`= lim(x→1) [(x^(2/3) - 1)/(x - 1)] / [(x^(1/3) - 1)/(x - 1)]`
Apply formula:
= (2/3)(1) / (1/3)(1) = (2/3) / (1/3) = **2**
</details>

28. 🟢 lim(x→a) (xⁿ - aⁿ)/(x - a)
<details>
<summary>Solution</summary>

This is the standard formula itself!
= **naⁿ⁻¹**
</details>

29. 🔴 ⭐ lim(x→0) ((1+x)^m - (1+x)^n)/x
<details>
<summary>Solution</summary>

Split the fraction:
`= lim(x→0) [((1+x)^m - 1) - ((1+x)^n - 1)] / x`
`= lim(x→0) ((1+x)^m - 1)/x - lim(x→0) ((1+x)^n - 1)/x`
Using result from Q24:
= m - n = **m - n**
</details>

---

### Type 5: One-Sided Limits

**Goal:** Evaluate LHL and RHL separately.

**Solved Example:**

Find lim(x→0) |x|/x

**Solution:**
```
|x|/x = x/x = 1    when x > 0  (RHL)
|x|/x = −x/x = −1  when x < 0  (LHL)

LHL = −1 ≠ RHL = 1
∴ Limit Does Not Exist
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

21. 🟡 ⭐ lim(x→0) x/|x|
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `|x| = x`. So `x/x = 1`.
LHL: As `x → 0⁻`, `|x| = -x`. So `x/(-x) = -1`.
LHL ≠ RHL, so the limit **Does Not Exist (DNE)**.
</details>

22. 🟡 For f(x) = {2x+1, x<1 | 3, x≥1}, find lim(x→1) f(x)
<details>
<summary>Solution</summary>

RHL: As `x → 1⁺`, use `3`. Limit is `3`.
LHL: As `x → 1⁻`, use `2x+1`. Limit is `2(1)+1 = 3`.
LHL = RHL = 3, so the limit is **3**.
</details>

23. 🟡 lim(x→2) [x] where [x] is the greatest integer function
<details>
<summary>Solution</summary>

RHL: As `x → 2⁺` (e.g., 2.01), `[x] = 2`.
LHL: As `x → 2⁻` (e.g., 1.99), `[x] = 1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

24. 🔴 lim(x→0) sin(x)/|x|
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `|x| = x`. `lim(x→0⁺) sin(x)/x = 1`.
LHL: As `x → 0⁻`, `|x| = -x`. `lim(x→0⁻) sin(x)/(-x) = -1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

25. 🟡 lim(x→0⁺) ⌊1/x⌋ · x — *Think about what [1/x] does as x→0⁺*
<details>
<summary>Solution</summary>

Let `t = 1/x`. As `x → 0⁺`, `t → ∞`. The limit becomes `lim(t→∞) ⌊t⌋/t`.
Since `t - 1 < ⌊t⌋ ≤ t`, divide by `t`: `1 - 1/t < ⌊t⌋/t ≤ 1`.
By Squeeze Theorem, as `t → ∞`, `1 - 1/t → 1` and `1 → 1`.
So the limit is **1**.
</details>

26. 🟡 lim(x→0) (x + |x|)/(x - |x|)
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `|x| = x`. Expression is `(x+x)/(x-x) = 2x/0`, which is undefined. So RHL doesn't exist.
LHL: As `x → 0⁻`, `|x| = -x`. Expression is `(x-x)/(x - (-x)) = 0/(2x) = 0`.
Since RHL doesn't exist, the overall limit **Does Not Exist**.
</details>

27. 🟡 ⭐ For f(x) = { x², x < 0 | 2x, x ≥ 0 }, find lim(x→0) f(x)
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, use `2x`. Limit is `2(0) = 0`.
LHL: As `x → 0⁻`, use `x²`. Limit is `0² = 0`.
LHL = RHL = 0, so the limit is **0**.
</details>

28. 🟡 lim(x→1) |x-1|/(x-1)
<details>
<summary>Solution</summary>

RHL: As `x → 1⁺`, `|x-1| = x-1`. Limit is `(x-1)/(x-1) = 1`.
LHL: As `x → 1⁻`, `|x-1| = -(x-1)`. Limit is `-(x-1)/(x-1) = -1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

29. 🔴 lim(x→2) f(x) where f(x) = { [x], x < 2 | x, x ≥ 2 }
<details>
<summary>Solution</summary>

RHL: As `x → 2⁺`, use `x`. Limit is `2`.
LHL: As `x → 2⁻`, use `[x]`. For `x ∈ [1, 2)`, `[x] = 1`. Limit is `1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

30. 🟡 lim(x→0⁻) ⌊x⌋/x
<details>
<summary>Solution</summary>

As `x → 0⁻`, `x` is in `(-1, 0)`. Thus `⌊x⌋ = -1`.
The limit becomes `lim(x→0⁻) -1/x = -1/(0⁻) = +∞`.
So the limit is **+∞** (or does not exist).
</details>

31. 🟡 ⭐ lim(x→1) (x² + |x-1| - 1)/(x-1)
<details>
<summary>Solution</summary>

RHL: As `x → 1⁺`, `|x-1| = x-1`. Expression: `(x² + x - 2)/(x-1) = (x-1)(x+2)/(x-1) = x+2`. Limit is `1+2=3`.
LHL: As `x → 1⁻`, `|x-1| = -(x-1)`. Expression: `(x² - x)/(x-1) = x(x-1)/(x-1) = x`. Limit is `1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

32. 🟡 ⭐ lim(x→0) (|x+2| - |x-2|)/x
<details>
<summary>Solution</summary>

For `x` very close to 0 (e.g. in `(-1, 1)`):
`x+2 > 0` so `|x+2| = x+2`.
`x-2 < 0` so `|x-2| = -(x-2) = 2-x`.
Expression: `(x+2 - (2-x))/x = 2x/x = 2`.
The limit is **2**.
</details>

33. 🔴 If lim(x→0) f(x) = 1, evaluate lim(x→0) f(|x|)
<details>
<summary>Solution</summary>

Since `lim(x→0) f(x) = 1`, both LHL and RHL of `f(x)` are 1.
As `x → 0` (either from left or right), `|x| → 0⁺`.
So `lim(x→0) f(|x|)` is just the RHL of `f(x)` at 0, which is **1**.
</details>

34. 🟡 lim(x→0) (e^x - 1)/|x|
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `|x| = x`. `lim(x→0⁺) (e^x-1)/x = 1`.
LHL: As `x → 0⁻`, `|x| = -x`. `lim(x→0⁻) (e^x-1)/(-x) = -1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

---

### Type 6: Squeeze Theorem

**Goal:** Trap f(x) between two functions with the same limit.

**Solved Example:**

Find lim(x→0) x² sin(1/x)

**Solution:**
```
We know: −1 ≤ sin(1/x) ≤ 1 for all x ≠ 0.

Multiply by x² (positive):
−x² ≤ x² sin(1/x) ≤ x²

As x → 0: lim(−x²) = 0 and lim(x²) = 0

By Squeeze theorem: lim(x→0) x² sin(1/x) = 0
```
🟡 Medium ⭐ Must-Do

**Practice Problems:**

26. 🟡 ⭐ lim(x→0) x cos(1/x)
<details>
<summary>Solution</summary>

We know `-1 ≤ cos(1/x) ≤ 1`.
Multiply by `|x|`: `-|x| ≤ x cos(1/x) ≤ |x|`.
As `x → 0`, `-|x| → 0` and `|x| → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

27. 🟡 lim(x→∞) sin(x)/x
<details>
<summary>Solution</summary>

We know `-1 ≤ sin x ≤ 1`.
For `x > 0`, divide by `x`: `-1/x ≤ (sin x)/x ≤ 1/x`.
As `x → ∞`, `-1/x → 0` and `1/x → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

28. 🔴 lim(x→0) x² cos(1/x²)
<details>
<summary>Solution</summary>

We know `-1 ≤ cos(1/x²) ≤ 1`.
Multiply by `x²` (positive): `-x² ≤ x² cos(1/x²) ≤ x²`.
As `x → 0`, both bounds go to 0.
By Squeeze Theorem, the limit is **0**.
</details>

29. 🟡 lim(x→0) √x · sin(1/x) for x > 0
<details>
<summary>Solution</summary>

We know `-1 ≤ sin(1/x) ≤ 1`.
Multiply by `√x`: `-√x ≤ √x sin(1/x) ≤ √x`.
As `x → 0`, `-√x → 0` and `√x → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

30. 🔴 Prove lim(x→0) x · [1/x] = 1 using Squeeze — *Hint: use [y] ≤ y < [y]+1*
<details>
<summary>Solution</summary>

Let `y = 1/x`. The limit is `lim(y→∞) (1/y)⌊y⌋`.
We know `y - 1 < ⌊y⌋ ≤ y`.
Divide by `y` (for `y>0`): `1 - 1/y < ⌊y⌋/y ≤ 1`.
As `y → ∞`, `1 - 1/y → 1` and `1 → 1`.
By Squeeze Theorem, the limit is **1**.
</details>

31. 🟡 ⭐ lim(x→0) √(x³ + x²) sin(1/x)
<details>
<summary>Solution</summary>

Note `√(x³ + x²) = √x²(x+1) = |x|√(x+1)`.
`-1 ≤ sin(1/x) ≤ 1`. Multiply by `|x|√(x+1)` (which is positive).
`- |x|√(x+1) ≤ |x|√(x+1) sin(1/x) ≤ |x|√(x+1)`.
As `x → 0`, `|x|√(x+1) → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

32. 🟡 lim(x→∞) (cos x)/x²
<details>
<summary>Solution</summary>

`-1 ≤ cos x ≤ 1`. Divide by `x²`.
`-1/x² ≤ (cos x)/x² ≤ 1/x²`.
As `x → ∞`, both bounds go to 0.
By Squeeze Theorem, the limit is **0**.
</details>

33. 🔴 lim(x→0) x³ sin(1/x²) cos(1/x)
<details>
<summary>Solution</summary>

`-1 ≤ sin(1/x²) cos(1/x) ≤ 1`.
Multiply by `|x³|`. `-|x³| ≤ x³ sin(1/x²) cos(1/x) ≤ |x³|`.
As `x → 0`, `|x³| → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

34. 🟡 ⭐ lim(x→0) x⁴ cos(2/x)
<details>
<summary>Solution</summary>

`-1 ≤ cos(2/x) ≤ 1`. Multiply by `x⁴`.
`-x⁴ ≤ x⁴ cos(2/x) ≤ x⁴`.
As `x → 0`, `x⁴ → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

35. 🔴 lim(x→0) x · arcsin(1/x) — *Hint: |arcsin y| ≤ π/2 for |y| ≤ 1*
<details>
<summary>Solution</summary>

This limit is actually taken as `x → ∞`. Wait, if `x → 0`, `1/x → ∞` and `arcsin` is undefined!
Assuming the question meant `lim(x→∞) x * arcsin(1/x)`:
Let `t = 1/x`. As `x → ∞`, `t → 0`.
`lim(t→0) (1/t) arcsin(t) = lim(t→0) arcsin(t)/t`.
Let `u = arcsin(t)`. As `t → 0, u → 0`. `t = sin(u)`.
`lim(u→0) u / sin(u) = 1`. The limit is **1**.
</details>

36. 🟡 lim(x→0) xⁿ sin(1/x) for n > 0 — *Find condition for limit existence*
<details>
<summary>Solution</summary>

`-1 ≤ sin(1/x) ≤ 1`. Multiply by `|x|ⁿ`.
`- |x|ⁿ ≤ xⁿ sin(1/x) ≤ |x|ⁿ`.
For the limit to be 0 by Squeeze theorem, we need `|x|ⁿ → 0` as `x → 0`, which requires **n > 0**.
If `n = 0`, the limit does not exist (oscillation). If `n < 0`, it diverges.
So condition is **n > 0**.
</details>

37. 🟡 lim(x→0) (x² - x⁴) cos(1/x³)
<details>
<summary>Solution</summary>

`-1 ≤ cos(1/x³) ≤ 1`.
Multiply by `|x² - x⁴|`.
As `x → 0`, `|x² - x⁴| → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

38. 🔴 ⭐ lim(x→0) x³ cos(1/x) sin(1/x)
<details>
<summary>Solution</summary>

Use `sin(1/x) cos(1/x) = (1/2) sin(2/x)`.
We need `lim(x→0) (1/2) x³ sin(2/x)`.
`-1/2 ≤ (1/2) sin(2/x) ≤ 1/2`.
Multiply by `|x³|`, both bounds go to 0 as `x → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

39. 🟡 lim(x→0) (x² + x) cos(1/x)
<details>
<summary>Solution</summary>

`-1 ≤ cos(1/x) ≤ 1`. Multiply by `|x² + x|`.
As `x → 0`, `|x² + x| → 0`.
By Squeeze Theorem, the limit is **0**.
</details>

---

### Type 7: Limits of Piecewise Functions

**Goal:** Evaluate limits where the function has different definitions on different intervals.

**Solved Example:** ⭐

Find lim(x→2) f(x) where f(x) = { x² − 1, if x < 2 | 2x + 1, if x ≥ 2 }

**Solution:**
```
LHL: lim(x→2⁻) f(x) = lim(x→2⁻) (x² − 1) = 4 − 1 = 3
RHL: lim(x→2⁺) f(x) = lim(x→2⁺) (2x + 1) = 4 + 1 = 5

LHL = 3 ≠ RHL = 5
∴ Limit Does Not Exist
```
🟡 Medium ⭐ Must-Do

> ⚠️ **Trap:** Many students plug x = 2 into the "x ≥ 2" piece and declare the limit is 5. That gives f(2), NOT lim(x→2) f(x). For the limit, you MUST check both sides.

---

**Practice Problems:**

31. 🟢 f(x) = { 3x + 2, x < 1 | 5, x = 1 | 4x + 1, x > 1 }. Find lim(x→1) f(x).
<details>
<summary>Solution</summary>

RHL: As `x → 1⁺`, `f(x) = 4x + 1`. Limit = `4(1) + 1 = 5`.
LHL: As `x → 1⁻`, `f(x) = 3x + 2`. Limit = `3(1) + 2 = 5`.
LHL = RHL = 5, so the limit is **5**.
</details>

32. 🟡 ⭐ f(x) = { (x² − 9)/(x − 3), x ≠ 3 | 5, x = 3 }. Find lim(x→3) f(x). Does lim f(x) = f(3)?
<details>
<summary>Solution</summary>

For limit as `x → 3`, `x ≠ 3`. We use `(x² - 9)/(x - 3) = (x-3)(x+3)/(x-3) = x+3`.
Limit is `3 + 3 = 6`.
So `lim(x→3) f(x) = 6`.
Does lim f(x) = f(3)? `f(3) = 5`. Since `6 ≠ 5`, **No**.
</details>

33. 🟡 f(x) = { sin(x)/x, x < 0 | 1, x = 0 | (e^x − 1)/x, x > 0 }. Find lim(x→0) f(x). *[Preview of Ch 2 standard limits — try it!]*
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `f(x) = (e^x - 1)/x`. Standard limit `lim = 1`.
LHL: As `x → 0⁻`, `f(x) = (sin x)/x`. Standard limit `lim = 1`.
LHL = RHL = 1, so the limit is **1**.
</details>

34. 🟡 f(x) = { x + |x|, x < 0 | 2, x ≥ 0 }. Find lim(x→0) f(x).
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, limit is **2** (from definition).
LHL: As `x → 0⁻`, `|x| = -x`. So `f(x) = x - x = 0`. Limit is **0**.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

35. 🔴 f(x) = { (1 − cos x)/x², x ≠ 0 | k, x = 0 }. What value of k makes f continuous at 0? *[Just find the limit for now — continuity is Ch 7]*
<details>
<summary>Solution</summary>

We need `k = lim(x→0) f(x)`.
`lim(x→0) (1 - cos x)/x²`. Multiply by `(1 + cos x)/(1 + cos x)`.
`= lim(x→0) (1 - cos²x) / (x²(1 + cos x))`
`= lim(x→0) (sin²x / x²) * (1 / (1 + cos x))`
`= 1² * (1 / (1 + 1)) = 1/2`.
So **k = 1/2**.
</details>

36. 🟡 ⭐ f(x) = { (√(x+1)-1)/x, x ≠ 0 | 1/2, x = 0 }. Find lim(x→0) f(x).
<details>
<summary>Solution</summary>

For limit as `x → 0`, we use `(√(x+1) - 1)/x`.
Multiply by conjugate: `(√(x+1) + 1)`.
Numerator is `(x+1) - 1 = x`.
`lim(x→0) x / (x(√(x+1) + 1)) = lim(x→0) 1 / (√(x+1) + 1) = 1/2`.
Limit is **1/2**.
</details>

37. 🟡 f(x) = { ax + b, x < 2 | 5, x = 2 | 3x, x > 2 }. If lim(x→2) f(x) exists, find a and b.
<details>
<summary>Solution</summary>

RHL: As `x → 2⁺`, `f(x) = 3x`. Limit = `3(2) = 6`.
LHL: As `x → 2⁻`, `f(x) = ax + b`. Limit = `2a + b`.
For limit to exist, LHL = RHL: `2a + b = 6`.
Since we only know the limit exists, we can't find exact `a` and `b` unless the function is continuous (then `2a+b=6` and the limit would equal `f(2)=5`, but here RHL=6 ≠ 5, so the function can't be continuous).
The condition is **2a + b = 6**.
</details>

38. 🔴 f(x) = { x² + 1, x < 1 | 3x, 1 ≤ x < 3 | x² - 1, x ≥ 3 }. Find lim(x→1) f(x) and lim(x→3) f(x).
<details>
<summary>Solution</summary>

At x = 1:
LHL = `1² + 1 = 2`. RHL = `3(1) = 3`. Limit **Does Not Exist**.
At x = 3:
LHL = `3(3) = 9`. RHL = `3² - 1 = 8`. Limit **Does Not Exist**.
</details>

39. 🟡 f(x) = { |x|/x, x ≠ 0 | 0, x = 0 }. Find lim(x→0) f(x).
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `|x| = x`. `x/x = 1`.
LHL: As `x → 0⁻`, `|x| = -x`. `-x/x = -1`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

40. 🔴 ⭐ f(x) = { (x² - a²)/(x - a), x ≠ a | 2a, x = a }. Find lim(x→a) f(x). Does lim f(x) = f(a)?
<details>
<summary>Solution</summary>

`lim(x→a) (x² - a²)/(x - a) = lim(x→a) (x-a)(x+a)/(x-a) = lim(x→a) (x+a) = 2a`.
The limit is **2a**.
Does lim f(x) = f(a)? `f(a) = 2a`. Yes, **they are equal**.
</details>

41. 🟡 f(x) = { x + 2, x < -1 | x², -1 ≤ x ≤ 2 | 6 - x, x > 2 }. Find lim(x→-1) f(x) and lim(x→2) f(x).
<details>
<summary>Solution</summary>

At x = -1:
LHL = `-1 + 2 = 1`. RHL = `(-1)² = 1`.
LHL = RHL, limit is **1**.
At x = 2:
LHL = `2² = 4`. RHL = `6 - 2 = 4`.
LHL = RHL, limit is **4**.
</details>

42. 🟡 f(x) = { (x² + x - 2)/(x - 1), x ≠ 1 | 3, x = 1 }. Find lim(x→1) f(x). Is lim f(x) equal to f(1)?
<details>
<summary>Solution</summary>

For limit, `x ≠ 1`. `(x² + x - 2)/(x - 1) = (x-1)(x+2)/(x-1) = x+2`.
`lim(x→1) (x+2) = 1+2 = 3`.
The limit is **3**.
Is lim = f(1)? `f(1) = 3`. Yes, **they are equal**.
</details>

43. 🟡 ⭐ f(x) = { 2x + a, x < 0 | 3, x = 0 | bx + 4, x > 0 }. If lim(x→0) f(x) exists, find relation between a and b.
<details>
<summary>Solution</summary>

RHL = `b(0) + 4 = 4`.
LHL = `2(0) + a = a`.
For limit to exist, LHL = RHL.
So **a = 4** (b can be any real number).
</details>

44. 🔴 f(x) = { (sin x)/x, x < 0 | k, x = 0 | (√(1+x) - 1)/x, x > 0 }. Find k so that lim(x→0) f(x) exists.
<details>
<summary>Solution</summary>

LHL: `lim(x→0⁻) (sin x)/x = 1`.
RHL: `lim(x→0⁺) (√(1+x) - 1)/x`. Multiply by conjugate: `(1+x-1) / (x(√(1+x)+1)) = 1 / (√(1+x)+1)`. Limit is `1/2`.
LHL = 1, RHL = 1/2.
Since LHL ≠ RHL, the limit **cannot exist for any value of k**.
(Wait, if a question says "Find k so that limit exists", the limit doesn't depend on k. The question is a trick or means "find k so f is continuous", but since limit doesn't exist, it can't be continuous either. Answer: **No such k exists**).
</details>

---

### Type 8: Limits Involving Greatest Integer Function [x]

**Goal:** Handle the floor function, which creates jumps at every integer.

**Key Fact:** [x] = greatest integer ≤ x.
- [2.7] = 2, [3] = 3, [−1.3] = −2, [0.99] = 0

**Solved Example:** ⭐

Find lim(x→3) [x]

**Solution:**
```
LHL: As x → 3⁻ (like 2.9, 2.99, 2.999...), [x] = 2
RHL: As x → 3⁺ (like 3.01, 3.001...), [x] = 3

LHL = 2 ≠ RHL = 3
∴ Limit Does Not Exist
```
🟡 Medium ⭐ Must-Do

> 💡 **Key Pattern:** lim(x→n) [x] **never exists** when n is an integer (always a jump). But lim(x→a) [x] **does exist** when a is NOT an integer.

---

**Practice Problems:**

36. 🟢 Find lim(x→2.5) [x]
<details>
<summary>Solution</summary>

For `x` near 2.5 (e.g. 2.49 or 2.51), `[x] = 2`.
Since the value is constant near 2.5, the limit is **2**.
</details>

37. 🟡 ⭐ Find lim(x→0) [x]. State LHL and RHL separately.
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺` (e.g. 0.01), `[x] = 0`. Limit is `0`.
LHL: As `x → 0⁻` (e.g. -0.01), `[x] = -1`. Limit is `-1`.
LHL ≠ RHL, so limit **Does Not Exist**.
</details>

38. 🟡 Find lim(x→1⁻) [x] and lim(x→1⁺) [x]
<details>
<summary>Solution</summary>

As `x → 1⁻` (e.g. 0.99), `[x] = 0`. LHL is **0**.
As `x → 1⁺` (e.g. 1.01), `[x] = 1`. RHL is **1**.
</details>

39. 🔴 Find lim(x→0) x[1/x] — *Hint: For x > 0, use [y] ≤ y < [y]+1 with y = 1/x*
<details>
<summary>Solution</summary>

Let `y = 1/x`. Then we want `lim(y→∞) ⌊y⌋/y` (RHL) and `lim(y→-∞) ⌊y⌋/y` (LHL).
From `y - 1 < ⌊y⌋ ≤ y`, dividing by `y` (for `y > 0`): `1 - 1/y < ⌊y⌋/y ≤ 1`. Squeeze theorem gives `1` as `y → ∞`.
For `y < 0`, dividing by `y` flips inequality: `1 - 1/y > ⌊y⌋/y ≥ 1`. Squeeze theorem gives `1` as `y → -∞`.
Since LHL = RHL = 1, the limit is **1**.
</details>

40. 🔴 ⭐ Find lim(x→0⁺) [1/x] · x². Does the Squeeze theorem help here?
<details>
<summary>Solution</summary>

Let `y = 1/x`. The limit is `lim(y→∞) ⌊y⌋/y²`.
We know `y - 1 < ⌊y⌋ ≤ y`.
Divide by `y²` (positive): `1/y - 1/y² < ⌊y⌋/y² ≤ 1/y`.
As `y → ∞`, `1/y - 1/y² → 0` and `1/y → 0`.
By Squeeze Theorem, the limit is **0**. Yes, Squeeze theorem helps!
</details>

41. 🟡 ⭐ Find lim(x→2.5) [x] + lim(x→2.5) [x+0.5]
<details>
<summary>Solution</summary>

First limit: As `x → 2.5`, `[x] = 2`.
Second limit: As `x → 2.5`, `x+0.5 → 3`. We must check LHL and RHL!
RHL: `x = 2.51`, `x+0.5 = 3.01`, so `[x+0.5] = 3`.
LHL: `x = 2.49`, `x+0.5 = 2.99`, so `[x+0.5] = 2`.
Since the second limit does not exist, the sum **Does Not Exist**.
</details>

42. 🟡 Find lim(x→1) [x²]
<details>
<summary>Solution</summary>

RHL: As `x → 1⁺` (e.g. 1.1), `x² > 1`, so `[x²] = 1`.
LHL: As `x → 1⁻` (e.g. 0.9), `x² < 1`, so `[x²] = 0`.
LHL ≠ RHL, so the limit **Does Not Exist**.
</details>

43. 🔴 Find lim(x→0) x[1/x] using the inequality [y] ≤ y < [y]+1
<details>
<summary>Solution</summary>

This is the exact same problem as Q39.
We use `1/x - 1 < [1/x] ≤ 1/x`.
Multiply by `x` (assume `x > 0` for RHL): `1 - x < x[1/x] ≤ 1`. As `x → 0⁺`, limit is 1.
Multiply by `x` (assume `x < 0` for LHL): `1 - x > x[1/x] ≥ 1`. As `x → 0⁻`, limit is 1.
Thus the limit is **1**.
</details>

44. 🟡 Find lim(x→0⁻) x⌈x⌉ — *⌈x⌉ = smallest integer ≥ x*
<details>
<summary>Solution</summary>
As `x → 0⁻` (e.g. -0.01), `x` is between `-1` and `0`.
The ceiling function `⌈x⌉` is the smallest integer `≥ x`, which is `0`.
So for `x ∈ (-1, 0)`, `x⌈x⌉ = x(0) = 0`.
The limit is **0**.
</details>

45. 🟡 ⭐ Find lim(x→0⁺) x²[1/x²]
<details>
<summary>Solution</summary>

Let `y = 1/x²`. As `x → 0⁺`, `y → ∞`.
The expression becomes `⌊y⌋/y`.
Using `y - 1 < ⌊y⌋ ≤ y`, we divide by `y`: `1 - 1/y < ⌊y⌋/y ≤ 1`.
As `y → ∞`, the bounds approach 1.
The limit is **1**.
</details>

46. 🔴 Find lim(x→0) [x]²/|x|
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `[x] = 0`. So `0²/x = 0`. Limit is 0.
LHL: As `x → 0⁻`, `[x] = -1`. So `(-1)²/(-x) = -1/x`. As `x → 0⁻`, `-1/x → +∞`.
LHL ≠ RHL, limit **Does Not Exist** (diverges).
</details>

47. 🟡 Find lim(x→3) x[x] for x near 3
<details>
<summary>Solution</summary>

RHL: As `x → 3⁺`, `[x] = 3`. Expression is `x(3) = 3x`. Limit is `3(3) = 9`.
LHL: As `x → 3⁻`, `[x] = 2`. Expression is `x(2) = 2x`. Limit is `2(3) = 6`.
LHL ≠ RHL, limit **Does Not Exist**.
</details>

48. 🔴 ⭐ Find lim(x→0) [x]·sin(πx) — *Hint: consider values just above and below 0*
<details>
<summary>Solution</summary>

RHL: As `x → 0⁺`, `[x] = 0`. Expression is `0 * sin(πx) = 0`. Limit is 0.
LHL: As `x → 0⁻`, `[x] = -1`. Expression is `-1 * sin(πx) = -sin(πx)`. As `x → 0`, `sin(0) = 0`, so `-0 = 0`.
LHL = RHL = 0. The limit is **0**.
</details>

49. 🟡 Find lim(x→0⁺) (1 - [x])/x
<details>
<summary>Solution</summary>

As `x → 0⁺`, `[x] = 0`.
The expression becomes `(1 - 0)/x = 1/x`.
As `x → 0⁺`, `1/x → +∞`.
The limit is **+∞** (or does not exist).
</details>

---

### Type 9: Limits by Substitution (x = a + h, h → 0)

**Goal:** Simplify tough limits by shifting the variable so it approaches 0 instead of a.

**Solved Example:**

Find lim(x→1) (x⁷ − 1)/(x − 1) using substitution.

**Solution:**
```
Let x = 1 + h, so as x → 1, h → 0.

x⁷ − 1 = (1+h)⁷ − 1

By binomial expansion: (1+h)⁷ = 1 + 7h + 21h² + ... 
So (1+h)⁷ − 1 = 7h + 21h² + ...

x − 1 = h

lim(h→0) (7h + 21h² + ...)/h
= lim(h→0) (7 + 21h + ...) = 7
```
🟡 Medium

> 💡 **When to use this:** When the point of approach is messy (like x → π/4 or x → √2), substitution to h → 0 often simplifies algebra dramatically.

---

**Practice Problems:**

41. 🟢 lim(x→2) (x³ − 8)/(x − 2) using h = x − 2
<details>
<summary>Solution</summary>

Let `h = x - 2`, so `x = 2 + h`. As `x → 2`, `h → 0`.
Substitute: `((2+h)³ - 8) / h = (8 + 12h + 6h² + h³ - 8) / h = (12h + 6h² + h³)/h`.
Factor `h`: `h(12 + 6h + h²)/h = 12 + 6h + h²`.
Limit as `h → 0` is `12 + 0 + 0 =` **12**.
</details>

42. 🟡 lim(x→1) (√x − 1)/(x − 1) using h = x − 1 — *Express √(1+h) ≈ 1 + h/2 for small h*
<details>
<summary>Solution</summary>

Let `h = x - 1`, so `x = 1 + h`. As `x → 1`, `h → 0`.
Substitute: `(√(1+h) - 1) / h`.
Using binomial expansion: `√(1+h) = (1+h)^(1/2) ≈ 1 + (1/2)h + ...`
So numerator is `1 + h/2 + ... - 1 = h/2 + ...`
Limit: `(h/2)/h =` **1/2**.
</details>

43. 🟡 lim(x→π/2) (cos x)/(x − π/2) using h = x − π/2 — *cos(π/2 + h) = −sin h*
<details>
<summary>Solution</summary>

Let `h = x - π/2`, so `x = π/2 + h`. As `x → π/2`, `h → 0`.
Substitute: `cos(π/2 + h) / h`.
Use trig identity: `cos(π/2 + h) = -sin(h)`.
Limit: `lim(h→0) -sin(h)/h = -1 * lim(sin h / h) = -1 * 1 =` **-1**.
</details>

44. 🔴 lim(x→a) (x^(1/3) − a^(1/3))/(x − a) using h = x − a
<details>
<summary>Solution</summary>

Let `h = x - a`, so `x = a + h`. As `x → a`, `h → 0`.
Substitute: `((a+h)^(1/3) - a^(1/3)) / h`.
Factor out `a`: `[a^(1/3)(1 + h/a)^(1/3) - a^(1/3)] / h = a^(1/3) * [(1 + h/a)^(1/3) - 1] / h`.
Binomial expansion of `(1 + h/a)^(1/3) ≈ 1 + (1/3)(h/a)`.
Numerator becomes `a^(1/3) * [1 + h/(3a) - 1] = a^(1/3) * h/(3a)`.
Limit: `a^(1/3) * h/(3a) / h = a^(1/3) / (3a) =` **(1/3)a^(-2/3)**.
</details>

45. 🟡 lim(x→0) ((1+x)^n − 1)/x using binomial expansion — *Result: n*
<details>
<summary>Solution</summary>

Binomial expansion: `(1+x)ⁿ = 1 + nx + [n(n-1)/2]x² + ...`
Numerator: `(1 + nx + ... ) - 1 = nx + x²(...)`
Limit: `(nx + x²(...)) / x = n + x(...)`.
As `x → 0`, limit is **n**.
</details>

46. 🟡 ⭐ lim(x→π) (sin x)/(x - π) using h = x - π
<details>
<summary>Solution</summary>

Let `h = x - π`, so `x = π + h`. As `x → π`, `h → 0`.
Substitute: `sin(π + h) / h`.
Use trig identity: `sin(π + h) = -sin(h)`.
Limit: `lim(h→0) -sin(h)/h = -1 * 1 =` **-1**.
</details>

47. 🟡 lim(x→1) (x^(1/3) - 1)/(x^(1/2) - 1) using h = x - 1
<details>
<summary>Solution</summary>

Let `h = x - 1`, so `x = 1 + h`. As `x → 1`, `h → 0`.
Substitute: `((1+h)^(1/3) - 1) / ((1+h)^(1/2) - 1)`.
Use binomial expansions:
Num: `1 + (1/3)h + ... - 1 ≈ (1/3)h`
Den: `1 + (1/2)h + ... - 1 ≈ (1/2)h`
Limit: `((1/3)h) / ((1/2)h) = (1/3)/(1/2) =` **2/3**.
</details>

48. 🔴 lim(x→π/2) (1 - sin x)/((π/2 - x)²) using h = x - π/2
<details>
<summary>Solution</summary>

Let `h = x - π/2`, so `x = π/2 + h`. As `x → π/2`, `h → 0`.
Denominator: `(π/2 - (π/2 + h))² = (-h)² = h²`.
Numerator: `1 - sin(π/2 + h) = 1 - cos(h)`.
Limit: `lim(h→0) (1 - cos h)/h²`.
Multiply by conjugate `(1 + cos h)`: `sin²h / (h²(1 + cos h))`.
Since `lim (sin²h/h²) = 1` and `lim 1/(1+cos h) = 1/2`.
Limit is `1 * (1/2) =` **1/2**.
</details>

49. 🟡 lim(x→0) ((1+x)^(1/3) - 1)/((1+x)^(1/2) - 1) using binomial expansion
<details>
<summary>Solution</summary>

This is very similar to Q47 but the limit is at `x=0`.
Let's apply binomial expansion directly:
Num: `(1+x)^(1/3) ≈ 1 + (1/3)x + ...`
Den: `(1+x)^(1/2) ≈ 1 + (1/2)x + ...`
Expression: `(1 + (1/3)x - 1) / (1 + (1/2)x - 1) = ((1/3)x) / ((1/2)x) =` **2/3**.
</details>

50. 🔴 ⭐ lim(x→a) (x^m - a^m)/(x^n - a^n) using h = x - a
<details>
<summary>Solution</summary>

Let `h = x - a`, so `x = a + h`. As `x → a`, `h → 0`.
Num: `(a+h)^m - a^m = a^m(1 + h/a)^m - a^m = a^m[1 + m(h/a) + ... - 1] ≈ a^m * m(h/a) = a^(m-1) * mh`.
Den: `(a+h)^n - a^n = a^n(1 + h/a)^n - a^n = a^n[1 + n(h/a) + ... - 1] ≈ a^n * n(h/a) = a^(n-1) * nh`.
Limit: `[a^(m-1) * mh] / [a^(n-1) * nh] = (m/n) * a^(m-1 - (n-1)) =` **(m/n) * a^(m-n)**.
</details>

51. 🟡 lim(x→π/6) (sin x - 1/2)/(x - π/6) using h = x - π/6
<details>
<summary>Solution</summary>

Let `h = x - π/6`, so `x = π/6 + h`.
Num: `sin(π/6 + h) - 1/2 = sin(π/6)cos(h) + cos(π/6)sin(h) - 1/2 = (1/2)cos(h) + (√3/2)sin(h) - 1/2`.
Den: `h`.
Expression: `[(1/2)(cos h - 1) + (√3/2)sin(h)] / h`.
Split limit: `(1/2) * lim((cos h - 1)/h) + (√3/2) * lim((sin h)/h)`.
We know `lim((cos h - 1)/h) = 0` and `lim((sin h)/h) = 1`.
Result: `(1/2)(0) + (√3/2)(1) =` **√3/2**.
</details>

52. 🟡 lim(x→0) ((1+2x)^n - 1)/x using binomial expansion
<details>
<summary>Solution</summary>

Binomial expansion: `(1+2x)^n ≈ 1 + n(2x) + ...`
Numerator: `1 + 2nx - 1 = 2nx + x²(...)`.
Limit: `(2nx)/x =` **2n**.
</details>

53. 🔴 lim(x→π/3) (2cos x - 1)/(x - π/3) using h = x - π/3
<details>
<summary>Solution</summary>

Let `h = x - π/3`, so `x = π/3 + h`.
Num: `2cos(π/3 + h) - 1 = 2[cos(π/3)cos(h) - sin(π/3)sin(h)] - 1 = 2[(1/2)cos(h) - (√3/2)sin(h)] - 1 = cos(h) - √3 sin(h) - 1`.
Den: `h`.
Expression: `[(cos h - 1) - √3 sin(h)] / h`.
Split limit: `lim((cos h - 1)/h) - √3 lim(sin h / h) = 0 - √3(1) =` **-√3**.
</details>

54. 🟡 lim(x→1) (x² - 2x + 1)/(x³ - 1) using h = x - 1
<details>
<summary>Solution</summary>

Let `h = x - 1`, so `x = 1 + h`.
Num: `x² - 2x + 1 = (x - 1)² = h²`.
Den: `x³ - 1 = (1+h)³ - 1 = (1 + 3h + 3h² + h³) - 1 = 3h + 3h² + h³`.
Expression: `h² / (3h + 3h² + h³)`. Factor out `h`: `h / (3 + 3h + h²)`.
As `h → 0`, limit is `0 / 3 =` **0**.
</details>

---

### Type 10: Finding Unknown Constants from Limit Conditions

**Goal:** Given that a limit exists (or equals a specific value), find the unknown constant.

**Solved Example:** ⭐

If lim(x→1) (x² + ax + b)/(x − 1) exists, find a + b.

**Solution:**
```
For the limit to exist and not be ±∞, the numerator must also → 0
when x → 1 (otherwise we'd have nonzero/0 = ±∞).

So: 1 + a + b = 0  →  a + b = −1

But we need more: for 0/0 to resolve, (x − 1) must be a factor of x² + ax + b.

x² + ax + b = (x − 1)(x + c) for some c.
Expanding: x² + (c − 1)x − c
Compare: a = c − 1, b = −c

From a + b = −1: (c − 1) + (−c) = −1 ✓ (consistent for any c)

The limit equals: lim(x→1) (x − 1)(x + c)/(x − 1) = 1 + c

So a + b = −1 (the answer), and the limit value depends on c.
```
🔴 Hard ⭐ Must-Do

> ⚠️ **Golden Rule:** If lim(x→a) f(x)/g(x) exists and g(a) = 0, then f(a) MUST also be 0. Otherwise the limit would be ±∞ or DNE.

---

**Practice Problems:**

46. 🟡 ⭐ If lim(x→2) (x² − 3x + k)/(x − 2) exists, find k.
<details>
<summary>Solution</summary>

Denominator goes to 0 as `x → 2`. For limit to exist, numerator must also go to 0.
So `2² - 3(2) + k = 0`.
`4 - 6 + k = 0 ⟹ k = 2`.
The value is **k = 2**.
</details>

47. 🟡 If lim(x→−1) (x² + x + a)/(x + 1) = 5, find a. Then find the limit.
<details>
<summary>Solution</summary>

Denom goes to 0. Num must go to 0 at `x = -1`: `(-1)² + (-1) + a = 0 ⟹ 1 - 1 + a = 0 ⟹ a = 0`.
So `a = 0`.
Limit: `lim(x→-1) (x² + x)/(x + 1) = lim(x→-1) x(x + 1)/(x + 1) = lim(x→-1) x = -1`.
Wait, the problem says the limit is 5, but our calculation gives -1!
Let's re-read: "If lim... = 5". If `a=0`, the limit is -1. So the limit CANNOT be 5.
Perhaps the problem has a typo, but based on the rules, **a = 0, and the limit is actually -1 (contradicting the "equals 5" part)**.
</details>

48. 🔴 If lim(x→1) (ax² + bx + 2)/(x − 1) exists, and equals 3, find a and b.
<details>
<summary>Solution</summary>

Denom goes to 0. Num must go to 0 at `x = 1`: `a(1)² + b(1) + 2 = 0 ⟹ a + b = -2 ⟹ b = -a - 2`.
Substitute `b`: `lim(x→1) (ax² - (a+2)x + 2)/(x-1)`.
Factor numerator: `a x² - ax - 2x + 2 = ax(x-1) - 2(x-1) = (x-1)(ax - 2)`.
Limit: `lim(x→1) (x-1)(ax - 2)/(x-1) = a(1) - 2 = a - 2`.
We are given limit = 3. So `a - 2 = 3 ⟹ a = 5`.
Then `b = -5 - 2 = -7`.
Values are **a = 5, b = -7**.
</details>

49. 🔴 ⭐ If lim(x→0) (sin 2x + ax + bx³)/x³ is finite, find a. *[Preview: uses sin 2x ≈ 2x − (4x³/3) for small x]*
<details>
<summary>Solution</summary>

Expansion: `sin 2x ≈ 2x - (2x)³/6 = 2x - 8x³/6 = 2x - 4x³/3`.
Expression: `(2x - 4x³/3 + ax + bx³) / x³ = ((2+a)x + (b - 4/3)x³) / x³ = (2+a)/x² + (b - 4/3)`.
For this to be finite as `x → 0`, the `1/x²` term must vanish.
So `2 + a = 0 ⟹ a = -2`.
Value is **a = -2**. (Limit would be `b - 4/3`).
</details>

50. 🟡 If lim(x→3) (x² + px − 12)/(x − 3) exists, find p and the limit value.
<details>
<summary>Solution</summary>

Num must go to 0 at `x = 3`: `3² + 3p - 12 = 0 ⟹ 9 + 3p - 12 = 0 ⟹ 3p = 3 ⟹ p = 1`.
Substitute `p = 1`: `lim(x→3) (x² + x - 12)/(x-3) = lim(x→3) (x-3)(x+4)/(x-3) = 3+4 = 7`.
Values: **p = 1, limit = 7**.
</details>

51. 🟡 ⭐ If lim(x→-2) (x² + px - 2)/(x + 2) exists, find p and the limit value.
<details>
<summary>Solution</summary>

Num must go to 0 at `x = -2`: `(-2)² - 2p - 2 = 0 ⟹ 4 - 2p - 2 = 0 ⟹ 2p = 2 ⟹ p = 1`.
Substitute `p = 1`: `lim(x→-2) (x² + x - 2)/(x+2) = lim(x→-2) (x+2)(x-1)/(x+2) = -2-1 = -3`.
Values: **p = 1, limit = -3**.
</details>

52. 🔴 If lim(x→3) (x² + ax + b)/(x - 3) = 5, find a and b.
<details>
<summary>Solution</summary>

Num goes to 0 at `x = 3`: `9 + 3a + b = 0 ⟹ b = -3a - 9`.
Substitute `b`: `x² + ax - 3a - 9 = x² - 9 + a(x - 3) = (x-3)(x+3) + a(x-3) = (x-3)(x+3+a)`.
Limit: `lim(x→3) (x-3)(x+3+a)/(x-3) = 3+3+a = 6+a`.
Given limit is 5: `6 + a = 5 ⟹ a = -1`.
Then `b = -3(-1) - 9 = 3 - 9 = -6`.
Values: **a = -1, b = -6**.
</details>

53. 🔴 ⭐ If lim(x→0) (√(1+x) - (1 + ax))/x² is finite, find a. Then evaluate the limit.
<details>
<summary>Solution</summary>

Use binomial expansion: `√(1+x) = 1 + x/2 - x²/8 + ...`
Expression: `(1 + x/2 - x²/8 - 1 - ax) / x² = ((1/2 - a)x - x²/8) / x² = (1/2 - a)/x - 1/8`.
For limit to be finite, the `1/x` term must vanish.
So `1/2 - a = 0 ⟹ a = 1/2`.
The limit is the remaining constant term, which is **-1/8**.
Values: **a = 1/2, limit = -1/8**.
</details>

54. 🟡 If lim(x→2) (x³ - 8)/(x² + kx - 8) exists and is finite, find k.
<details>
<summary>Solution</summary>

Num goes to 0 as `x → 2`.
Wait! Denominator can be anything. But if denom is 0, limit could be DNE.
Let's check denom at `x=2`: `4 + 2k - 8 = 2k - 4`.
If `2k - 4 ≠ 0`, limit is `0 / (2k - 4) = 0`, which exists and is finite.
If `2k - 4 = 0` (i.e. `k = 2`), then denom goes to 0. `x² + 2x - 8 = (x-2)(x+4)`.
Limit would be `lim(x→2) (x-2)(x²+2x+4) / ((x-2)(x+4)) = (4+4+4)/(2+4) = 12/6 = 2`.
The problem says "exists and is finite". It is finite for ANY k (except if `2k - 4 = 0` and the factors didn't cancel, but they do cancel).
Actually, the question might mean "is a non-zero finite value" or "If denom is 0". If `k=2`, limit is 2. For all other `k`, limit is 0. Both are finite.
Assuming the intended "typical" problem where it forces `0/0`: **k = 2**.
</details>

55. 🔴 If lim(x→1) (x⁴ + ax³ + bx² + cx + d)/(x - 1)³ is finite, find a + b + c + d.
<details>
<summary>Solution</summary>

For the limit to be finite, `(x-1)³` must be a factor of the numerator `P(x)`.
So `P(1) = 0`, `P'(1) = 0`, and `P''(1) = 0`.
From `P(1) = 0`, we get `1 + a + b + c + d = 0 ⟹ a + b + c + d = -1`.
The question only asked for `a + b + c + d`, which is simply **-1**.
</details>

56. 🟡 If lim(x→0) (√(1+ax) - √(1-ax))/x = 4, find a.
<details>
<summary>Solution</summary>

Rationalize numerator: multiply by `(√(1+ax) + √(1-ax))`.
Numerator becomes `(1+ax) - (1-ax) = 2ax`.
`lim(x→0) 2ax / (x(√(1+ax) + √(1-ax))) = 2a / (√1 + √1) = 2a / 2 = a`.
Given limit is 4, so **a = 4**.
</details>

57. 🔴 ⭐ If lim(x→b) (x⁴ - b⁴)/(x² - 3bx + 2b²) exists and is finite (b ≠ 0), find the limit.
<details>
<summary>Solution</summary>

Num: `(x-b)(x+b)(x²+b²)`. Denom: `x² - 3bx + 2b² = (x-b)(x-2b)`.
`lim(x→b) (x-b)(x+b)(x²+b²) / ((x-b)(x-2b))`.
Cancel `(x-b)`: `lim(x→b) (x+b)(x²+b²) / (x-2b)`.
Substitute `x = b`: `(2b)(2b²) / (-b) = 4b³ / -b = -4b²`.
The limit is **-4b²**.
</details>

58. 🟡 If lim(x→2) (ax² + b)/(x - 2) = 4, find a and b.
<details>
<summary>Solution</summary>

Num must go to 0 at `x = 2`: `4a + b = 0 ⟹ b = -4a`.
Substitute `b`: `lim(x→2) (ax² - 4a)/(x-2) = lim(x→2) a(x-2)(x+2)/(x-2) = a(2+2) = 4a`.
Given limit is 4: `4a = 4 ⟹ a = 1`.
Then `b = -4(1) = -4`.
Values: **a = 1, b = -4**.
</details>

59. 🔴 ⭐ If lim(x→1) (x³ + 2x² + ax + b)/(x - 1)² exists and is finite, find a and b.
<details>
<summary>Solution</summary>

Numerator `P(x)` must have `(x-1)²` as a factor. So `P(1) = 0` and `P'(1) = 0`.
`P(1) = 1 + 2 + a + b = 0 ⟹ a + b = -3`.
`P'(x) = 3x² + 4x + a`. `P'(1) = 3 + 4 + a = 0 ⟹ a = -7`.
Then `b = -3 - (-7) = 4`.
Values: **a = -7, b = 4**.
</details>

---

## Stage 4: Type Mixer

1. 🟡 Find lim(x→1) (x³ − 1)/(√x − 1). *[Combines Type 2 + Type 3]*
<details>
<summary>Solution</summary>

Rationalize denom: multiply by `(√x + 1)`. Denom becomes `x - 1`.
`lim(x→1) (x³ - 1)(√x + 1) / (x - 1) = lim(x→1) (x-1)(x²+x+1)(√x+1) / (x-1)`.
Cancel `(x-1)`: `(x²+x+1)(√x+1)`. At `x=1`: `(3)(2) =` **6**.
</details>

2. 🔴 ⭐ Define f(x) = {(x²−4)/(x−2), x≠2 | k, x=2}. Find k so lim(x→2) f(x) = f(2). *[Type 2 + Type 5]*
<details>
<summary>Solution</summary>

Limit: `lim(x→2) (x-2)(x+2)/(x-2) = lim(x→2) (x+2) = 4`.
To have `lim f(x) = f(2)`, we need `k =` **4**.
</details>

3. 🔴 Find lim(x→0) (√(1+x²) − 1)/x². Then use Squeeze to show x²sin(1/x)/(√(1+x²)−1) → 0. *[Type 3 + Type 6]*
<details>
<summary>Solution</summary>

First limit: Rationalize `(√(1+x²) − 1)(√(1+x²) + 1) / (x²(√(1+x²) + 1)) = x² / (x²(√(1+x²) + 1)) = 1 / (√(1+x²) + 1)`. Limit is `1/2`.
So as `x → 0`, `x² / (√(1+x²) - 1) → 2`.
Second expression: `[x² / (√(1+x²) - 1)] * sin(1/x)`.
Since `|sin(1/x)| ≤ 1`, and the first factor approaches 2... Wait, `x²sin(1/x)` goes to 0. `0/(1/2) = 0`.
Limit is **0**.
</details>

4. 🟡 lim(x→4) (x^(3/2) − 8)/(x − 4). *[Type 3 or Type 4]*
<details>
<summary>Solution</summary>

Using standard formula `(xⁿ - aⁿ)/(x - a)` with `n=3/2, a=4`.
`n aⁿ⁻¹ = (3/2) * 4^(1/2) = (3/2) * 2 =` **3**.
</details>

5. 🔴 lim(x→0) (|x+1| − |x−1|)/x. *[Type 5, consider cases]*
<details>
<summary>Solution</summary>

For `x` very close to 0 (e.g. in `(-1, 1)`):
`x+1 > 0` so `|x+1| = x+1`.
`x-1 < 0` so `|x-1| = -(x-1) = 1-x`.
Expression: `(x+1 - (1-x))/x = 2x/x = 2`.
Limit is **2**.
</details>

6. 🔴 ⭐ f(x) = { (x²+ax−6)/(x−2), x≠2 | b, x=2 }. If lim(x→2) f(x) exists and equals f(2), find a and b. *[Type 7 + Type 10]*
<details>
<summary>Solution</summary>

Limit exists, so numerator must go to 0 at `x=2`: `4 + 2a - 6 = 0 ⟹ 2a - 2 = 0 ⟹ a = 1`.
Substitute `a=1`: `lim(x→2) (x² + x - 6)/(x - 2) = lim (x-2)(x+3)/(x-2) = 5`.
Limit is 5, so `b = 5`.
Values: **a = 1, b = 5**.
</details>

7. 🔴 Find lim(x→0⁺) x · [1/x] + lim(x→0) x²sin(1/x). *[Type 8 + Type 6]*
<details>
<summary>Solution</summary>

First limit (from Q39/43): `lim(x→0⁺) x[1/x] = 1`.
Second limit (from Q28/Type 6): `lim(x→0) x²sin(1/x) = 0` (by Squeeze).
Sum is `1 + 0 =` **1**.
</details>

8. 🟡 Use substitution h = x − π/4 to find lim(x→π/4) (√2 − 2cos x)/(4x − π). *[Type 9 + trig]*
<details>
<summary>Solution</summary>

Let `h = x - π/4`, so `x = π/4 + h`.
Denominator: `4(π/4 + h) - π = 4h`.
Numerator: `√2 - 2cos(π/4 + h) = √2 - 2[cos(π/4)cos(h) - sin(π/4)sin(h)] = √2 - 2[(1/√2)cos(h) - (1/√2)sin(h)] = √2 - √2 cos(h) + √2 sin(h) = √2(1 - cos h) + √2 sin(h)`.
Expression: `[√2(1 - cos h) + √2 sin(h)] / 4h = (√2/4) * (1 - cos h)/h + (√2/4) * (sin h)/h`.
Limit: `(√2/4)(0) + (√2/4)(1) =` **√2/4**.
</details>

9. 🟡 ⭐ Find lim(x→2) (x⁴ - 16)/(√(x+2) - 2). *[Type 4 + Type 3]*
<details>
<summary>Solution</summary>

Rationalize denominator: `(√(x+2) + 2)`. Denom becomes `x+2 - 4 = x-2`.
Numerator is `(x⁴ - 16)(√(x+2) + 2)`.
Expression: `(x⁴ - 16)/(x - 2) * (√(x+2) + 2)`.
Limit of first part: `4(2)³ = 32`.
Limit of second part: `√4 + 2 = 4`.
Total limit: `32 * 4 =` **128**.
</details>

10. 🔴 Find lim(x→0) (√(1+x+x²) - √(1-x+x²))/x. *[Type 3 + Type 5]*
<details>
<summary>Solution</summary>

Rationalize numerator: `(1+x+x²) - (1-x+x²) = 2x`.
Expression: `2x / [x(√(1+x+x²) + √(1-x+x²))]`.
Cancel `x`: `2 / (√(1+x+x²) + √(1-x+x²))`.
Limit: `2 / (√1 + √1) = 2/2 =` **1**.
</details>

11. 🟡 If lim(x→0) (√(1+ax) - 1)/x = 2, find a. *[Type 3 + Type 10]*
<details>
<summary>Solution</summary>

Rationalize: `(1+ax - 1) / [x(√(1+ax) + 1)] = ax / [x(√(1+ax) + 1)] = a / (√(1+ax) + 1)`.
Limit: `a / 2 = 2 ⟹ a =` **4**.
</details>

12. 🔴 ⭐ lim(x→1) ((x⁵ - 1)/(x-1) - (x⁴ - 1)/(x-1))/(x-1). *[Type 4 + Type 2]*
<details>
<summary>Solution</summary>

Combine fractions: `(x⁵ - x⁴) / (x-1)² = x⁴(x-1) / (x-1)² = x⁴ / (x-1)`.
As `x → 1`, limit is `1/0 = ∞`. (Wait, let me re-read).
Expression: `[ (x⁵-1 - (x⁴-1)) / (x-1) ] / (x-1) = (x⁵ - x⁴) / (x-1)² = x⁴(x-1) / (x-1)² = x⁴ / (x-1)`.
As `x → 1`, limit is **Does Not Exist** (or ∞).
</details>

13. 🟡 ⭐ lim(x→0) x·[1/x²] — *Use inequality [y] ≤ y < [y]+1 with y = 1/x²* *[Type 6 + Type 8]*
<details>
<summary>Solution</summary>

`1/x² - 1 < [1/x²] ≤ 1/x²`.
Multiply by `x` (for `x>0`): `1/x - x < x[1/x²] ≤ 1/x`. As `x → 0⁺`, limit is `+∞`.
Multiply by `x` (for `x<0`): `1/x - x > x[1/x²] ≥ 1/x`. As `x → 0⁻`, limit is `-∞`.
Limit **Does Not Exist**.
</details>

14. 🔴 lim(x→0⁺) (√(x+1) - 1)/|x|. *[Type 3 + Type 5]*
<details>
<summary>Solution</summary>

For `x → 0⁺`, `|x| = x`.
Limit is `lim(x→0⁺) (√(x+1) - 1)/x`.
Rationalize: `x / [x(√(x+1) + 1)] = 1 / (√(x+1) + 1)`.
Limit is `1/2`.
</details>

15. 🟡 f(x) = { (x³ - 8)/(x - 2), x ≠ 2 | k, x = 2 }. Find k so that lim(x→2) f(x) = f(2). *[Type 2 + Type 7]*
<details>
<summary>Solution</summary>

Limit: `lim(x→2) (x-2)(x²+2x+4)/(x-2) = 12`.
We need `f(2) = k = 12`.
</details>

16. 🔴 ⭐ lim(x→0) (sin x - x cos x)/(x³). *[Trig expansion — Preview: sin x ≈ x - x³/6, cos x ≈ 1 - x²/2]* *[Type 4 + Series]*
<details>
<summary>Solution</summary>

`sin x ≈ x - x³/6`. `cos x ≈ 1 - x²/2`.
`x cos x ≈ x - x³/2`.
Numerator: `(x - x³/6) - (x - x³/2) = -x³/6 + x³/2 = 3x³/6 - x³/6 = 2x³/6 = x³/3`.
Limit: `(x³/3) / x³ =` **1/3**.
</details>

17. 🟡 lim(x→4) (x^(3/2) - 8)/(√x - 2). *[Type 4 + Type 3]*
<details>
<summary>Solution</summary>

Let `y = √x`. As `x → 4`, `y → 2`.
Expression: `(y³ - 8)/(y - 2)`.
Limit: `3(2)² =` **12**.
</details>

18. 🔴 lim(x→0) (1/x - cot x). *[∞−∞ form: combine fractions]* *[Type 2 + algebraic manipulation]*
<details>
<summary>Solution</summary>

`1/x - (cos x)/(sin x) = (sin x - x cos x) / (x sin x)`.
Using expansions: Num is `(x - x³/6) - (x - x³/2) = x³/3`. Denom is `x(x - x³/6) ≈ x²`.
So `(x³/3) / x² = x/3`.
As `x → 0`, limit is **0**.
</details>

19. 🟡 lim(x→0) (√(2-x²) - √2)/x². *[Type 3]*
<details>
<summary>Solution</summary>

Rationalize: `((2-x²) - 2) / [x²(√(2-x²) + √2)] = -x² / [x²(...)] = -1 / (√(2-x²) + √2)`.
Limit: `-1 / (√2 + √2) =` **-1/(2√2)**.
</details>

20. 🔴 ⭐ If lim(x→1) (x⁴ + ax² + b)/(x - 1) = 6, find a and b. *[Type 10 + Type 2]*
<details>
<summary>Solution</summary>

Num must go to 0 at `x = 1`: `1 + a + b = 0 ⟹ b = -a - 1`.
Substitute `b`: `x⁴ + ax² - a - 1 = (x⁴ - 1) + a(x² - 1) = (x²-1)(x²+1) + a(x²-1) = (x²-1)(x² + 1 + a) = (x-1)(x+1)(x² + 1 + a)`.
Limit: `lim(x→1) (x+1)(x² + 1 + a) = 2(1 + 1 + a) = 2(a+2) = 2a + 4`.
Given limit is 6: `2a + 4 = 6 ⟹ 2a = 2 ⟹ a = 1`.
Then `b = -1 - 1 = -2`.
Values: **a = 1, b = -2**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 Evaluate lim(x→3) (x² − 9)/(x − 3). **(2 marks)**

**Solution:**
= lim(x→3) (x−3)(x+3)/(x−3) = lim(x→3) (x+3) = 6

---

**Q2.** 🟢 Evaluate lim(x→0) (√(1+x) − 1)/x. **(2 marks)**

**Solution:**
Rationalize: multiply by (√(1+x)+1)/(√(1+x)+1)
= lim x/[x(√(1+x)+1)] = 1/(1+1) = 1/2

---

**Q3.** 🟡 ⭐ Evaluate lim(x→1) (x¹⁵ − 1)/(x¹⁰ − 1). **(3 marks)**

**Solution:**
= lim(x→1) [(x¹⁵−1)/(x−1)] / [(x¹⁰−1)/(x−1)]
= 15·1¹⁴ / 10·1⁹ = 15/10 = 3/2

---

**Q4.** 🟡 Show that lim(x→0) x²sin(1/x) = 0. **(3 marks)**

**Solution:**
−1 ≤ sin(1/x) ≤ 1 ⟹ −x² ≤ x²sin(1/x) ≤ x²
lim(x→0) (−x²) = lim(x→0) x² = 0
By Squeeze theorem, lim(x→0) x²sin(1/x) = 0.

---

**Q5.** 🟡 Find lim(x→2) (x³ − 8)/(x² − 4). **(3 marks)**

**Solution:**
= (x−2)(x²+2x+4) / (x−2)(x+2)
= lim(x→2) (x²+2x+4)/(x+2) = (4+4+4)/(4) = 12/4 = 3

---

**Q6.** 🟡 ⭐ Evaluate lim(x→0) (√(1+2x) - √(1-2x))/x. **(3 marks)**

**Solution:**
Rationalize: (1+2x-1+2x)/[x(√(1+2x)+√(1-2x))] = 4x/[x(√(1+2x)+√(1-2x))] = 4/(1+1) = 2

---

**Q7.** 🟡 Evaluate lim(x→2) (x⁴ - 16)/(x³ - 8). **(3 marks)**

**Solution:**
x⁴-16 = (x-2)(x+2)(x²+4), x³-8 = (x-2)(x²+2x+4)
= lim(x→2) (x+2)(x²+4)/(x²+2x+4) = (4)(8)/(4+4+4) = 32/12 = 8/3

---

**Q8.** 🔴 ⭐ Evaluate lim(x→0) (√(1+x) - 1 - x/2)/x². **(4 marks)**

**Solution:**
Let f(x) = (√(1+x) - 1 - x/2)/x². Multiply numerator and denominator by (√(1+x)+1+x/2):
= [1+x - (1+x/2)²] / [x²(√(1+x)+1+x/2)]
= [1+x - (1+x+x²/4)] / [x²(√(1+x)+1+x/2)]
= [-x²/4] / [x²(√(1+x)+1+x/2)]
= -1/[4(√(1+x)+1+x/2)] → -1/[4(1+1)] = -1/8

---

**Q9.** 🟡 Evaluate lim(x→3) |x-3|/(x-3) if it exists. **(2 marks)**

**Solution:**
LHL: x→3⁻, |x-3| = -(x-3), so limit = -(x-3)/(x-3) = -1
RHL: x→3⁺, |x-3| = x-3, so limit = (x-3)/(x-3) = 1
LHL ≠ RHL, so limit does not exist.

---

**Q10.** 🟡 ⭐ Evaluate lim(x→0) x² cos(1/x) + x sin(1/x). **(3 marks)**

**Solution:**
By Squeeze: -x² ≤ x²cos(1/x) ≤ x² → 0
-|x| ≤ x sin(1/x) ≤ |x| → 0
Sum = 0 + 0 = 0

---

**Q11.** 🔴 Evaluate lim(x→1) (x¹⁰⁰ - 1)/(x⁵⁰ - 1). **(3 marks)**

**Solution:**
= [100·1⁹⁹]/[50·1⁴⁹] = 100/50 = 2

---

**Q12.** 🟡 For what value of k does lim(x→0) (sin 3x + kx)/x³ exist? Find the limit. **(4 marks)**

**Solution:**
sin 3x = 3x - (27x³)/6 + ... = 3x - (9x³)/2 + ...
(sin 3x + kx)/x³ = (3x+kx)/x³ - 9/2 = (3+k)/x² - 9/2
For the limit to be finite: 3+k = 0 → k = -3
Then limit = -9/2.

---

**Q13.** 🟡 ⭐ Evaluate lim(x→0) (x·[1/x])². **(3 marks)**

**Solution:**
For x > 0: 1/x - 1 < [1/x] ≤ 1/x
Multiply by x > 0: 1 - x < x[1/x] ≤ 1
By Squeeze: lim(x→0⁺) x[1/x] = 1
Similarly: lim(x→0⁻) x[1/x] = 1
Thus lim(x→0) x[1/x] = 1, and its square = 1² = 1.

---

**Q14.** 🟡 Evaluate lim(x→π/2) (cos x)/(π - 2x). **(3 marks)**

**Solution:**
Let h = x - π/2, so h → 0.
cos(π/2 + h) = -sin h
π - 2x = π - 2(π/2 + h) = -2h
lim(h→0) (-sin h)/(-2h) = lim(h→0) sin h/(2h) = 1/2

---

**Q15.** 🔴 ⭐ Find a and b such that lim(x→0) (√(1+x) - (1+ax+bx²))/x³ exists and is finite. **(4 marks)**

**Solution:**
Binomial expansion: √(1+x) = 1 + x/2 - x²/8 + x³/16 - ...
√(1+x) - (1+ax+bx²) = (1/2 - a)x + (-1/8 - b)x² + (1/16)x³ + ...
For the limit to exist as x → 0, coefficients of x and x² must vanish:
a = 1/2, b = -1/8
Then limit = 1/16.

---

## Stage 6: JEE Mains Arena

**Q1.** lim(x→0) (√(1+x) − √(1−x))/x equals:
(a) 0   (b) 1/2   (c) 1   (d) 2

<details>
<summary>Solution</summary>
Rationalize: multiply by (√(1+x)+√(1−x))/(√(1+x)+√(1−x))
= (1+x−1+x)/[x(√(1+x)+√(1−x))]
= 2x/[x(√(1+x)+√(1−x))]
= 2/(√1+√1) = 2/2 = 1
Answer: (c) 🟡 ⭐
</details>

---

**Q2.** lim(x→1) (x^m − 1)/(x^n − 1) equals:
(a) m/n   (b) n/m   (c) mn   (d) 1

<details>
<summary>Solution</summary>
= [m·1^(m−1)] / [n·1^(n−1)] = m/n
Answer: (a) 🟢 ⭐
</details>

---

**Q3.** lim(x→0) |sin x|/x equals:
(a) 1   (b) −1   (c) 0   (d) Does not exist

<details>
<summary>Solution</summary>
RHL: x→0⁺, |sin x| = sin x, so sin x/x → 1
LHL: x→0⁻, |sin x| = −sin x, so −sin x/x. Let x = −h, h→0⁺:
= −sin(−h)/(−h) = sin h/h → 1? No!
Actually: |sin x|/x = (−sin x)/x when x<0 (since sin x < 0 for x < 0, |sin x| = −sin x)
= −(sin x/x) → −1
LHL = −1 ≠ RHL = 1 → DNE
Answer: (d) 🟡
</details>

---

**Q4.** If lim(x→2) (x^n − 2^n)/(x − 2) = 80, then n equals:
(a) 3   (b) 4   (c) 5   (d) 6

<details>
<summary>Solution</summary>
n · 2^(n−1) = 80
Try n = 5: 5 · 2⁴ = 5 · 16 = 80 ✓
Answer: (c) 🟡 ⭐
</details>

---

**Q5.** lim(x→0) (√(a+x) − √(a−x))/x equals:
(a) 1/√a   (b) 1/(2√a)   (c) 2/√a   (d) √a

<details>
<summary>Solution</summary>
Rationalize: × (√(a+x)+√(a−x))/(√(a+x)+√(a−x))
= (a+x−a+x)/[x(√(a+x)+√(a−x))]
= 2x/[x(√(a+x)+√(a−x))]
= 2/(√a + √a) = 2/(2√a) = 1/√a
Answer: (a) 🟡
</details>

---

**Q6.** lim(x→2) (x³ - 8)/(x² - 3x + 2) equals:
(a) 6   (b) 12   (c) 0   (d) ∞

<details>
<summary>Solution</summary>
x³-8 = (x-2)(x²+2x+4), x²-3x+2 = (x-2)(x-1)
Cancel (x-2): lim(x→2) (x²+2x+4)/(x-1) = (4+4+4)/(1) = 12
Answer: (b) 🟡 ⭐
</details>

---

**Q7.** lim(x→0) (√(1+2x) - 1)/(√(1+x) - 1) equals:
(a) 0   (b) 1   (c) 2   (d) 1/2

<details>
<summary>Solution</summary>
Rationalize both: [2x/(√(1+2x)+1)] / [x/(√(1+x)+1)] = 2(√(1+x)+1)/(√(1+2x)+1) → 2(2)/(2) = 2
Answer: (c) 🟡
</details>

---

**Q8.** lim(x→0) x·⌊1/x⌋ (where ⌊⌋ is greatest integer) equals:
(a) 0   (b) 1   (c) DNE   (d) ∞

<details>
<summary>Solution</summary>
For x > 0: 1/x - 1 < ⌊1/x⌋ ≤ 1/x → 1 - x < x⌊1/x⌋ ≤ 1
By Squeeze: lim(x→0⁺) x⌊1/x⌋ = 1
Similarly from the left: lim(x→0⁻) x⌊1/x⌋ = 1
Thus limit = 1.
Answer: (b) 🟡 ⭐
</details>

---

**Q9.** lim(x→0) (1 - cos 2x)/x² equals:
(a) 0   (b) 1   (c) 2   (d) 4

<details>
<summary>Solution</summary>
1 - cos 2x = 2sin²x
(2sin²x)/x² = 2(sin x/x)² → 2(1)² = 2
Answer: (c) 🟡
</details>

---

**Q10.** If lim(x→0) (√(a+x) - √a)/x = 1/(2√a), then a can be:
(a) any positive real   (b) any real   (c) a = 0 only   (d) any integer

<details>
<summary>Solution</summary>
The formula holds for any a > 0 where √a is defined as real.
Answer: (a) 🟢
</details>

---

**Q11.** lim(x→0) (|x+1| - |x-1|)/x equals:
(a) 0   (b) 1   (c) 2   (d) DNE

<details>
<summary>Solution</summary>
For x near 0: |x+1| = x+1 (positive), |x-1| = -(x-1) = 1-x (since x-1 < 0)
So (x+1-(1-x))/x = (2x)/x = 2
Answer: (c) 🟡
</details>

---

**Q12.** lim(x→1) (x¹⁸ - 1)/(x¹² - 1) equals:
(a) 3/2   (b) 2/3   (c) 18/12   (d) 1

<details>
<summary>Solution</summary>
= [18·1¹⁷]/[12·1¹¹] = 18/12 = 3/2
Answer: (a) 🟢 ⭐
</details>

---

**Q13.** lim(x→0) ln(1+x)/x equals:
(a) 0   (b) 1   (c) e   (d) ∞

<details>
<summary>Solution</summary>
This is a standard limit: lim(x→0) ln(1+x)/x = 1
Answer: (b) 🟡 ⭐
</details>

---

**Q14.** If lim(x→a) (x³ - a³)/(x - a) = lim(x→2) (x² + 3x - 10)/(x - 2), then a equals:
(a) 1   (b) √(7/3)   (c) 3   (d) 5

<details>
<summary>Solution</summary>
Left: 3a²
Right: x²+3x-10 = (x-2)(x+5), so limit = 2+5 = 7
3a² = 7 → a = √(7/3)
Answer: (b) 🔴 ⭐
</details>

---

**Q15.** lim(x→0) x sin(1/x) + x² cos(1/x²) equals:
(a) 0   (b) 1   (c) DNE   (d) ∞

<details>
<summary>Solution</summary>
First term: -|x| ≤ x sin(1/x) ≤ |x| → 0 by Squeeze
Second term: -x² ≤ x² cos(1/x²) ≤ x² → 0 by Squeeze
Sum = 0
Answer: (a) 🟡 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Directions:** Choose:
(a) Both A and R are true and R is the correct explanation of A
(b) Both A and R are true but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

---

**Q1.** **Assertion (A):** lim(x→2) (x²−4)/(x−2) = 4, even though (x²−4)/(x−2) is undefined at x=2.
**Reason (R):** A limit at x = a depends on the behaviour of f(x) *near* a, not *at* a.

<details>
<summary>Solution</summary>
A is true: After cancellation, limit = 4.
R is true and correctly explains why: limits don't require the function to be defined at the point.
Answer: (a) 🟢 ⭐
</details>

---

**Q2.** **Assertion (A):** lim(x→0) sin(1/x) does not exist.
**Reason (R):** sin(1/x) oscillates infinitely as x → 0.

<details>
<summary>Solution</summary>
A is true: The function keeps oscillating between −1 and 1 and never settles.
R is true and is the correct explanation — infinite oscillation prevents convergence.
Answer: (a) 🟡
</details>

---

**Q3.** **Assertion (A):** lim(x→0) x·sin(1/x) = 0.
**Reason (R):** sin(1/x) = 0 when x → 0.

<details>
<summary>Solution</summary>
A is true: By Squeeze theorem, −|x| ≤ x sin(1/x) ≤ |x|, so limit = 0.
R is false: sin(1/x) does NOT equal 0 as x → 0; it oscillates.
Answer: (c) 🟡 ⭐
</details>

---

**Q4.** **Assertion (A):** lim(x→0) |x|/x does not exist.
**Reason (R):** LHL = −1 and RHL = 1.

<details>
<summary>Solution</summary>
A is true: The limit DNE because left and right limits differ.
R is true and correctly explains why.
Answer: (a) 🟢
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 lim(x→5) (x² − 25)/(x − 5) =
   (a) 5   (b) 10   (c) 25   (d) 0

2. 🟢 lim(x→0) (3x² + 2x)/x =
   (a) 0   (b) 2   (c) 3   (d) 5

3. 🟡 ⭐ lim(x→1) (x³ − 1)/(x − 1) =
   (a) 1   (b) 2   (c) 3   (d) 0

4. 🟡 lim(x→0) (√(4+x) − 2)/x =
   (a) 1/2   (b) 1/4   (c) 1   (d) 4

5. 🟢 lim(x→2) 5 =
   (a) 5   (b) 2   (c) 10   (d) 0

6. 🟡 lim(x→0) (√(1+x) − √(1−x))/x =
   (a) 0   (b) 1/2   (c) 1   (d) 2

7. 🟡 ⭐ If lim(x→a) (x⁵ − a⁵)/(x − a) = 405, then a =
   (a) 1   (b) 2   (c) 3   (d) 4

8. 🟢 lim(x→0) x/|x| from the right =
   (a) 1   (b) −1   (c) 0   (d) DNE

9. 🟡 lim(x→0) x² cos(1/x) =
   (a) DNE   (b) 1   (c) 0   (d) −1

10. 🟢 lim(x→3) (x − 3)/(x² − 9) =
    (a) 1/6   (b) 6   (c) 0   (d) ∞

11. 🟡 lim(x→4) (x^(3/2) − 8)/(x − 4) =
    (a) 2   (b) 3   (c) 3/2   (d) 4

12. 🟡 ⭐ lim(x→0) (1/x − 1/(x+x²)) =
    (a) 0   (b) 1   (c) −1   (d) ∞

13. 🔴 lim(x→0) (√(1+x²) − 1)/x² =
    (a) 0   (b) 1/2   (c) 1   (d) 2

14. 🟡 lim(x→1) (x⁴ − 1)/(x² − 1) =
    (a) 1   (b) 2   (c) 4   (d) 0

15. 🟡 ⭐ lim(x→0⁺) √x · sin(1/x) =
    (a) 1   (b) 0   (c) DNE   (d) ∞

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| 1 | b | 6 | c | 11 | b |
| 2 | b | 7 | c | 12 | b |
| 3 | c | 8 | a | 13 | b |
| 4 | b | 9 | c | 14 | b |
| 5 | a | 10 | a | 15 | b |

</details>

---

## What's Next?

In this chapter, you built the **intuition** for limits — what they mean, when they exist, and how to evaluate basic ones using factorization, rationalization, the xⁿ−aⁿ formula, and the Squeeze theorem.

In **Chapter 2**, we'll tackle the powerful **standard limits** involving trigonometric, exponential, and logarithmic functions — the tools that unlock 70% of all limit problems in JEE.

**Key takeaway from Chapter 1:** A limit asks "where is f(x) heading?" not "where is f(x)?". The limit can exist even when the function is undefined. And when you get 0/0, it's not an answer — it's an invitation to dig deeper.
