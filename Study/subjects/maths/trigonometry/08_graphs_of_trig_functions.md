# Chapter 8: Domain, Range & Graphs of Trig Functions

---

## Stage 1: The Core Idea

### Seeing the Waves

When you plot sin θ against θ, you get a smooth wave that repeats every 360° (2π). This wave is everywhere — sound, light, tides, seasons, music.

Each trig function has its own characteristic graph:
- **sin and cos**: smooth waves (amplitude = 1, period = 2π)
- **tan**: repeating vertical curves (period = π, has asymptotes)
- **cosec and sec**: reciprocal curves with asymptotes
- **cot**: decreasing curves with asymptotes

Understanding these graphs is essential for solving equations, finding ranges, and calculus.

---

## Stage 2: The Formula Lab

### Graphs Summary

| Function | Domain | Range | Period | Asymptotes |
|----------|--------|-------|--------|------------|
| sin x | All real numbers | [−1, 1] | 2π | None |
| cos x | All real numbers | [−1, 1] | 2π | None |
| tan x | x ≠ (2n+1)π/2 | All real numbers | π | x = (2n+1)π/2 |
| cosec x | x ≠ nπ | (−∞, −1] ∪ [1, ∞) | 2π | x = nπ |
| sec x | x ≠ (2n+1)π/2 | (−∞, −1] ∪ [1, ∞) | 2π | x = (2n+1)π/2 |
| cot x | x ≠ nπ | All real numbers | π | x = nπ |

### Key Properties

**sin x:**
- Starts at origin: sin 0 = 0
- Max at π/2 (1), min at 3π/2 (−1)
- Symmetric about origin (odd function)

**cos x:**
- Starts at 1: cos 0 = 1
- Max at 0, 2π; min at π
- Symmetric about y-axis (even function)

**tan x:**
- Zero at 0, π, 2π
- Goes to +∞ before asymptotes from left, −∞ from right

---

## Stage 3: Type-wise Mastery

### Type 1: Domain of a Trig Function

**Goal:** Find the domain of a given trigonometric expression.

**Solved Example:**

Find the domain of f(x) = 1/(sin x − 1).

**Solution:**
```
Denominator ≠ 0: sin x − 1 ≠ 0 → sin x ≠ 1
sin x = 1 at x = π/2, 5π/2, ...
Domain: x ≠ (4n+1)π/2 where n ∈ ℤ
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 What is the domain of sin x?<br>
<details>
<summary>Solution</summary>

The function \( f(x) = \sin x \) is defined for all real values of \( x \). There are no points where the function is undefined.

Therefore, the domain of \( \sin x \) is all real numbers, denoted as:
\[ \text{Domain} = \mathbb{R} \text{ or } (-\infty, \infty) \]
</details>

2. 🟡 What is the domain of tan x?<br>
<details>
<summary>Solution</summary>

Since \( \tan x = \frac{\sin x}{\cos x} \), the function is undefined when the denominator is zero:
\[ \cos x = 0 \]
The cosine function is zero at all odd multiples of \( \frac{\pi}{2} \):
\[ x = (2n + 1)\frac{\pi}{2} \quad \text{where } n \in \mathbb{Z} \]
Thus, the domain of \( \tan x \) is all real numbers except odd multiples of \( \frac{\pi}{2} \):
\[ \text{Domain} = \mathbb{R} \setminus \left\{ (2n+1)\frac{\pi}{2} \;\middle|\; n \in \mathbb{Z} \right\} \]
</details>

3. 🟡 What is the domain of sec x?<br>
<details>
<summary>Solution</summary>

Since \( \sec x = \frac{1}{\cos x} \), the function is undefined when the denominator is zero:
\[ \cos x = 0 \]
This occurs at odd multiples of \( \frac{\pi}{2} \):
\[ x = (2n+1)\frac{\pi}{2} \quad \text{where } n \in \mathbb{Z} \]
Thus, the domain is:
\[ \text{Domain} = \mathbb{R} \setminus \left\{ (2n+1)\frac{\pi}{2} \;\middle|\; n \in \mathbb{Z} \right\} \]
</details>

4. 🟡 Find the domain of f(x) = 2/(cos x − 1).
<details>
<summary>Solution</summary>

The function \( f(x) = \frac{2}{\cos x - 1} \) is undefined when the denominator is zero:
\[ \cos x - 1 = 0 \implies \cos x = 1 \]
The cosine function is equal to 1 at even multiples of \( \pi \):
\[ x = 2n\pi \quad \text{where } n \in \mathbb{Z} \]
Therefore, the domain is all real numbers except even multiples of \( \pi \):
\[ \text{Domain} = \mathbb{R} \setminus \{ 2n\pi \mid n \in \mathbb{Z} \} \]
</details>

5. 🔴 Find the domain of f(x) = 1/(sin x − 1/2).
<details>
<summary>Solution</summary>

The function is undefined when the denominator is zero:
\[ \sin x - \frac{1}{2} = 0 \implies \sin x = \frac{1}{2} \]
The principal value is \( x = \frac{\pi}{6} \). The general solution is:
\[ x = n\pi + (-1)^n\frac{\pi}{6} \quad \text{where } n \in \mathbb{Z} \]
Therefore, the domain is all real numbers except these values:
\[ \text{Domain} = \mathbb{R} \setminus \left\{ n\pi + (-1)^n\frac{\pi}{6} \;\middle|\; n \in \mathbb{Z} \right\} \]
</details>

---

### Type 2: Range of a Trig Function

**Goal:** Find the range of a given trigonometric expression.

**Solved Example:**

Find the range of f(x) = 3 sin x + 4.

**Solution:**
```
For sin x: range is [−1, 1]
3 sin x: range is [−3, 3]
3 sin x + 4: range is [1, 7]
Answer: [1, 7]
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 Find the range of f(x) = −2 cos x + 1.
<details>
<summary>Solution</summary>

We start with the basic inequality for the cosine function:
\[ -1 \le \cos x \le 1 \]
Multiply by \(-2\) (which reverses the inequalities):
\[ 2 \ge -2 \cos x \ge -2 \implies -2 \le -2 \cos x \le 2 \]
Now, add \( 1 \) to all parts of the inequality:
\[ -2 + 1 \le -2 \cos x + 1 \le 2 + 1 \]
\[ -1 \le f(x) \le 3 \]
Therefore, the range is \( [-1, 3] \).
</details>

7. 🟡 Find the range of f(x) = 5 − 3 sin x.
<details>
<summary>Solution</summary>

We start with the standard range of the sine function:
\[ -1 \le \sin x \le 1 \]
Multiply by \(-3\):
\[ 3 \ge -3 \sin x \ge -3 \implies -3 \le -3 \sin x \le 3 \]
Add \( 5 \) to each part:
\[ 5 - 3 \le 5 - 3 \sin x \le 5 + 3 \]
\[ 2 \le f(x) \le 8 \]
Therefore, the range of the function is \( [2, 8] \).
</details>

8. 🟡 Find the range of f(x) = 2 tan x + 1 (over its domain).
<details>
<summary>Solution</summary>

The range of the basic tangent function \( \tan x \) over its domain is all real numbers:
\[ -\infty < \tan x < \infty \]
Multiplying by \( 2 \) and adding \( 1 \) preserves this range:
\[ -\infty < 2\tan x + 1 < \infty \]
Therefore, the range of \( f(x) \) is \( (-\infty, \infty) \) (or \( \mathbb{R} \)).
</details>

9. 🔴 Find the range of f(x) = 1/(sin x + 2).
<details>
<summary>Solution</summary>

We start with the range of the sine function:
\[ -1 \le \sin x \le 1 \]
Add \( 2 \) to all parts of the inequality to find the range of the denominator:
\[ -1 + 2 \le \sin x + 2 \le 1 + 2 \]
\[ 1 \le \sin x + 2 \le 3 \]
Since the denominator is strictly positive, taking the reciprocal reverses the inequality:
\[ \frac{1}{1} \ge \frac{1}{\sin x + 2} \ge \frac{1}{3} \]
\[ \frac{1}{3} \le f(x) \le 1 \]
Therefore, the range of \( f(x) \) is \( \left[\frac{1}{3}, 1\right] \).
</details>

10. 🔴 ⭐ Find the range of f(x) = sin²x − sin x + 1.
<details>
<summary>Solution</summary>

Let \( t = \sin x \). Since \( \sin x \) ranges from \(-1\) to \( 1 \), we have \( t \in [-1, 1] \).
The function becomes:
\[ g(t) = t^2 - t + 1 \]
We complete the square to analyze this quadratic function:
\[ g(t) = \left(t - \frac{1}{2}\right)^2 + \frac{3}{4} \]
The vertex of the parabola is at \( t = \frac{1}{2} \), which is inside our interval \( [-1, 1] \).
- **Minimum value:** Occurs at \( t = \frac{1}{2} \):
  \[ g\left(\frac{1}{2}\right) = 0 + \frac{3}{4} = \frac{3}{4} \]
- **Maximum value:** Occurs at the endpoint furthest from the vertex \( t = \frac{1}{2} \), which is \( t = -1 \):
  \[ g(-1) = (-1)^2 - (-1) + 1 = 3 \]
  (At \( t = 1 \), we have \( g(1) = 1^2 - 1 + 1 = 1 \)).

Therefore, the range of \( f(x) = \sin^2 x - \sin x + 1 \) is \( \left[\frac{3}{4}, 3\right] \).
</details>

---

### Type 3: Identifying Graphs — sin and cos

**Goal:** Match equations to graphs or sketch basic sin/cos curves.

**Solved Example:**

Sketch y = sin x from 0 to 2π. Label key points.

**Solution:**
```
x:    0    π/2    π    3π/2    2π
y:    0    1      0    −1      0

The curve starts at origin, goes up to 1, down through 0 to −1, back to 0.
```
🟢 Easy

---

**Practice Problems:**

11. 🟢 Sketch y = cos x from 0 to 2π.
<details>
<summary>Solution</summary>

To sketch \( y = \cos x \) from \( 0 \) to \( 2\pi \), we plot the five key points:
* At \( x = 0 \): \( y = \cos 0 = 1 \) (Maximum)
* At \( x = \frac{\pi}{2} \): \( y = \cos\frac{\pi}{2} = 0 \) (x-intercept)
* At \( x = \pi \): \( y = \cos\pi = -1 \) (Minimum)
* At \( x = \frac{3\pi}{2} \): \( y = \cos\frac{3\pi}{2} = 0 \) (x-intercept)
* At \( x = 2\pi \): \( y = \cos 2\pi = 1 \) (Maximum)

Connect these points with a smooth, bowl-shaped wave starting at \( 1 \), decreasing to a minimum of \( -1 \) at \( \pi \), and returning to \( 1 \) at \( 2\pi \).
</details>

12. 🟡 Sketch y = 2 sin x. What is its amplitude?<br>
<details>
<summary>Solution</summary>

For \( y = 2 \sin x \):
* **Amplitude:** The amplitude is the absolute value of the coefficient of the sine term:
  \[ \text{Amplitude} = |2| = 2 \]
* **Key Points from 0 to \( 2\pi \):**
  * At \( x = 0 \): \( y = 2 \sin 0 = 0 \)
  * At \( x = \frac{\pi}{2} \): \( y = 2 \sin\frac{\pi}{2} = 2 \)
  * At \( x = \pi \): \( y = 2 \sin\pi = 0 \)
  * At \( x = \frac{3\pi}{2} \): \( y = 2 \sin\frac{3\pi}{2} = -2 \)
  * At \( x = 2\pi \): \( y = 2 \sin 2\pi = 0 \)

**Sketch description:** This graph is a vertical stretch of \( y = \sin x \) by a factor of 2. It has the same x-intercepts as the standard sine wave, but its peaks are at \( y = 2 \) and its troughs are at \( y = -2 \).
</details>

13. 🟡 Sketch y = sin 2x. What is its period?<br>
<details>
<summary>Solution</summary>

For \( y = \sin 2x \):
* **Period:**
  \[ \text{Period} = \frac{2\pi}{|b|} = \frac{2\pi}{2} = \pi \]
* **Key Points for one full cycle (from 0 to \( \pi \)):**
  * At \( x = 0 \): \( y = \sin 0 = 0 \)
  * At \( x = \frac{\pi}{4} \): \( y = \sin\frac{\pi}{2} = 1 \)
  * At \( x = \frac{\pi}{2} \): \( y = \sin\pi = 0 \)
  * At \( x = \frac{3\pi}{4} \): \( y = \sin\frac{3\pi}{2} = -1 \)
  * At \( x = \pi \): \( y = \sin 2\pi = 0 \)

**Sketch description:** This graph is a horizontal compression of the standard sine wave by a factor of 2. It completes one full wave in the interval \( [0, \pi] \) instead of \( [0, 2\pi] \).
</details>

14. 🟡 Sketch y = sin x + 1. What is its range?<br>
<details>
<summary>Solution</summary>

For \( y = \sin x + 1 \):
* **Vertical Shift:** The graph of \( y = \sin x \) is shifted upward by 1 unit.
* **Range:**
  Since \( -1 \le \sin x \le 1 \), adding 1 gives:
  \[ -1 + 1 \le \sin x + 1 \le 1 + 1 \implies 0 \le y \le 2 \]
  So the range is \( [0, 2] \).
* **Key Points from 0 to \( 2\pi \):**
  * At \( x = 0 \): \( y = 0 + 1 = 1 \)
  * At \( x = \frac{\pi}{2} \): \( y = 1 + 1 = 2 \) (Maximum)
  * At \( x = \pi \): \( y = 0 + 1 = 1 \)
  * At \( x = \frac{3\pi}{2} \): \( y = -1 + 1 = 0 \) (Minimum)
  * At \( x = 2\pi \): \( y = 0 + 1 = 1 \)

**Sketch description:** The midline of the wave is at \( y = 1 \). The wave oscillates between \( 0 \) and \( 2 \), never going below the x-axis.
</details>

15. 🟡 Sketch y = |sin x| for 0 ≤ x ≤ 2π.
<details>
<summary>Solution</summary>

For \( y = |\sin x| \) from \( 0 \) to \( 2\pi \):
* **Effect of Absolute Value:** Any part of the graph of \( y = \sin x \) that lies below the x-axis (\( y < 0 \)) is reflected across the x-axis to become positive.
* **Interval breakdown:**
  * For \( 0 \le x \le \pi \): \( \sin x \ge 0 \), so \( y = \sin x \).
  * For \( \pi < x < 2\pi \): \( \sin x < 0 \), so \( y = -\sin x \) (positive arches).
* **Key Points:**
  * At \( x = 0, \pi, 2\pi \): \( y = 0 \)
  * At \( x = \frac{\pi}{2}, \frac{3\pi}{2} \): \( y = 1 \)

**Sketch description:** The graph consists of two identical upward arches (peaks of height 1 at \( \frac{\pi}{2} \) and \( \frac{3\pi}{2} \)) and meets the x-axis at \( 0 \), \( \pi \), and \( 2\pi \) with sharp corners (cusps) at \( x = \pi \).
</details>

---

### Type 4: Period of a Trig Function

**Goal:** Find the period of a given trigonometric expression.

**Formula:** For sin(ax + b) or cos(ax + b), period = 2π/|a|.
For tan(ax + b), period = π/|a|.

**Solved Example:**

Find the period of f(x) = sin 3x.

**Solution:**
```
Period = 2π/|3| = 2π/3
```
🟢 Easy

---

**Practice Problems:**

16. 🟢 Find the period of cos 2x.
<details>
<summary>Solution</summary>

For \( f(x) = \cos(bx) \), the formula for the period is:
\[ T = \frac{2\pi}{|b|} \]
Here, \( b = 2 \). Thus:
\[ T = \frac{2\pi}{2} = \pi \]
</details>

17. 🟢 Find the period of tan 4x.
<details>
<summary>Solution</summary>

For \( f(x) = \tan(bx) \), the fundamental period of the base function \( \tan x \) is \( \pi \). The period is given by:
\[ T = \frac{\pi}{|b|} \]
Here, \( b = 4 \). Thus:
\[ T = \frac{\pi}{4} \]
</details>

18. 🟡 Find the period of sin(x/2).
<details>
<summary>Solution</summary>

For \( f(x) = \sin(bx) \), the period is:
\[ T = \frac{2\pi}{|b|} \]
Here, \( b = \frac{1}{2} \). Thus:
\[ T = \frac{2\pi}{\frac{1}{2}} = 4\pi \]
</details>

19. 🟡 Find the period of |sin x|.
<details>
<summary>Solution</summary>

The standard sine function \( \sin x \) has a period of \( 2\pi \) because it goes positive, then negative, and repeats.
When we take the absolute value \( |\sin x| \), the negative half-cycle is reflected to look exactly like the positive half-cycle:
\[ |\sin(x + \pi)| = |-\sin x| = |\sin x| \]
Since \( \pi \) is the smallest positive value for which this relation holds:
\[ \text{Period} = \pi \]
</details>

20. 🔴 Find the period of sin 2x + cos 3x.
<details>
<summary>Solution</summary>

Let \( f(x) = \sin 2x + \cos 3x \).
* Period of \( f_1(x) = \sin 2x \):
  \[ T_1 = \frac{2\pi}{2} = \pi \]
* Period of \( f_2(x) = \cos 3x \):
  \[ T_2 = \frac{2\pi}{3} \]

The period of the sum of two periodic functions is the Least Common Multiple (LCM) of their individual periods:
\[ T = \text{LCM}(T_1, T_2) = \text{LCM}\left(\pi, \frac{2\pi}{3}\right) \]
To find the LCM of fractions \( \frac{\pi}{1} \) and \( \frac{2\pi}{3} \):
\[ \text{LCM}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\text{LCM}(a, c)}{\text{GCD}(b, d)} \]
Here:
* Numerators are \( \pi \) and \( 2\pi \); their LCM is \( 2\pi \).
* Denominators are \( 1 \) and \( 3 \); their GCD is \( 1 \).

Thus:
\[ T = \frac{2\pi}{1} = 2\pi \]
Therefore, the period of \( \sin 2x + \cos 3x \) is \( 2\pi \).
</details>

---

### Type 5: Amplitude and Phase Shift

**Goal:** Find amplitude, period, and phase shift of transformed trig functions.

**Form:** y = a sin(bx + c) + d
- Amplitude = |a|
- Period = 2π/|b|
- Phase shift = −c/b
- Vertical shift = d

**Solved Example:**

Find amplitude, period, and phase shift of y = 3 sin(2x − π/3) + 1.

**Solution:**
```
Amplitude = |3| = 3
Period = 2π/2 = π
Phase shift = −(−π/3)/2 = π/6 (shift right)
Vertical shift = 1
```
🟡 Medium

---

**Practice Problems:**

21. 🟡 y = 2 cos(3x + π/4). Find amplitude, period, phase shift.
<details>
<summary>Solution</summary>

Compare \( y = 2 \cos(3x + \pi/4) \) with the standard form \( y = a \cos(bx + c) \):
* \( a = 2 \)
* \( b = 3 \)
* \( c = \pi/4 \)

Now we calculate:
* **Amplitude:** \( |a| = |2| = 2 \)
* **Period:** \( \frac{2\pi}{|b|} = \frac{2\pi}{3} \)
* **Phase shift:** \( -\frac{c}{b} = -\frac{\pi/4}{3} = -\frac{\pi}{12} \) (which means a shift of \( \frac{\pi}{12} \) units to the left)
</details>

22. 🟡 y = −sin(x/2 − π/6). Find amplitude, period, phase shift.
<details>
<summary>Solution</summary>

Compare \( y = -\sin(x/2 - \pi/6) \) with the standard form \( y = a \sin(bx + c) \):
* \( a = -1 \)
* \( b = 1/2 \)
* \( c = -\pi/6 \)

Now we calculate:
* **Amplitude:** \( |a| = |-1| = 1 \)
* **Period:** \( \frac{2\pi}{|b|} = \frac{2\pi}{1/2} = 4\pi \)
* **Phase shift:** \( -\frac{c}{b} = -\frac{-\pi/6}{1/2} = \frac{\pi}{3} \) (which means a shift of \( \frac{\pi}{3} \) units to the right)
</details>

23. 🟡 y = 4 tan(2x − π/3). Find period and phase shift.
<details>
<summary>Solution</summary>

Compare \( y = 4 \tan(2x - \pi/3) \) with the standard tangent form \( y = a \tan(bx + c) \):
* \( a = 4 \)
* \( b = 2 \)
* \( c = -\pi/3 \)

Now we calculate:
* **Period:** For a tangent function, the fundamental period is \( \pi \), so:
  \[ \text{Period} = \frac{\pi}{|b|} = \frac{\pi}{2} \]
* **Phase shift:**
  \[ \text{Phase shift} = -\frac{c}{b} = -\frac{-\pi/3}{2} = \frac{\pi}{6} \quad (\text{shifted to the right}) \]
</details>

24. 🔴 y = 2 sin(πx + 1) + 3. Find amplitude, period, phase shift.
<details>
<summary>Solution</summary>

Compare \( y = 2 \sin(\pi x + 1) + 3 \) with the standard form \( y = a \sin(bx + c) + d \):
* \( a = 2 \)
* \( b = \pi \)
* \( c = 1 \)
* \( d = 3 \)

Now we calculate:
* **Amplitude:** \( |a| = 2 \)
* **Period:** \( \frac{2\pi}{|b|} = \frac{2\pi}{\pi} = 2 \)
* **Phase shift:** \( -\frac{c}{b} = -\frac{1}{\pi} \) (shifted \( \frac{1}{\pi} \) units to the left)
* **Vertical shift:** \( d = 3 \) (shifted upward by 3 units)
</details>

25. 🔴 ⭐ A sine wave has period π, amplitude 3, and passes through (0, 0). Write its equation.
<details>
<summary>Solution</summary>

The general equation for a sine wave is:
\[ y = A \sin(Bx - C) \]
We are given:
1. **Amplitude is 3:**
   \[ |A| = 3 \implies A = 3 \text{ or } A = -3 \]
2. **Period is \(\pi\):**
   \[ \text{Period} = \frac{2\pi}{|b|} = \pi \implies |b| = 2 \implies b = \pm 2 \]
   Usually, we take \( b > 0 \), so \( b = 2 \).
3. **Passes through \((0, 0)\):**
   Substituting \( (0,0) \) into \( y = A \sin(2x - C) \):
   \[ 0 = A \sin(-C) \implies \sin(-C) = 0 \implies C = 0, \pi, \dots \]
   Taking the simplest case where there is no phase shift (\( C = 0 \)):
   \[ y = 3 \sin(2x) \quad \text{or} \quad y = -3 \sin(2x) \]

Thus, a valid equation is \( y = 3 \sin(2x) \).
</details>

---

### Type 6: Maximum and Minimum from Graphs

**Goal:** Find max/min values of trig expressions using graph knowledge.

**Solved Example:**

Find the maximum and minimum of f(x) = 5 − 2 cos 3x.

**Solution:**
```
cos 3x ranges from −1 to 1
−2 cos 3x ranges from −2 to 2
f(x) ranges from (5 − 2) to (5 + 2) = [3, 7]
Max = 7, Min = 3
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 Max and min of f(x) = 3 + 4 sin x.
<details>
<summary>Solution</summary>

We know that:
\[ -1 \le \sin x \le 1 \]
Multiply all parts by 4:
\[ -4 \le 4 \sin x \le 4 \]
Add 3:
\[ 3 - 4 \le 3 + 4 \sin x \le 3 + 4 \]
\[ -1 \le f(x) \le 7 \]
* **Maximum value:** 7
* **Minimum value:** -1
</details>

27. 🟡 Max and min of f(x) = 1/(2 + sin x).
<details>
<summary>Solution</summary>

First find the range of the denominator \( 2 + \sin x \):
\[ -1 \le \sin x \le 1 \]
\[ 2 - 1 \le 2 + \sin x \le 2 + 1 \]
\[ 1 \le 2 + \sin x \le 3 \]
Now take the reciprocal (since the values are strictly positive, the inequality signs reverse):
\[ \frac{1}{1} \ge \frac{1}{2 + \sin x} \ge \frac{1}{3} \]
\[ \frac{1}{3} \le f(x) \le 1 \]
* **Maximum value:** 1 (attained when \( \sin x = -1 \))
* **Minimum value:** \( \frac{1}{3} \) (attained when \( \sin x = 1 \))
</details>

28. 🟡 Max and min of f(x) = 2 − 3 sin 2x.
<details>
<summary>Solution</summary>

The term \( \sin 2x \) ranges between \(-1\) and \(1\):
\[ -1 \le \sin 2x \le 1 \]
Multiply by \(-3\) (reversing the inequality direction):
\[ 3 \ge -3 \sin 2x \ge -3 \implies -3 \le -3 \sin 2x \le 3 \]
Add 2:
\[ 2 - 3 \le 2 - 3 \sin 2x \le 2 + 3 \]
\[ -1 \le f(x) \le 5 \]
* **Maximum value:** 5 (attained when \( \sin 2x = -1 \))
* **Minimum value:** -1 (attained when \( \sin 2x = 1 \))
</details>

29. 🔴 Max and min of f(x) = sin²x + cos²x. (Think first!)
<details>
<summary>Solution</summary>

By the fundamental Pythagorean trigonometric identity:
\[ \sin^2 x + \cos^2 x = 1 \]
This identity holds true for all real values of \( x \).
Therefore, \( f(x) \) is a constant function:
\[ f(x) = 1 \]
* **Maximum value:** 1
* **Minimum value:** 1
</details>

30. 🔴 ⭐ Max and min of f(x) = sin⁴x + cos⁴x.
<details>
<summary>Solution</summary>

We rewrite the expression using algebraic identities:
\[ \sin^4 x + \cos^4 x = (\sin^2 x + \cos^2 x)^2 - 2\sin^2 x\cos^2 x \]
Since \( \sin^2 x + \cos^2 x = 1 \):
\[ f(x) = 1 - 2\sin^2 x\cos^2 x \]
Use the double angle formula \( \sin 2x = 2\sin x\cos x \implies \sin x\cos x = \frac{\sin 2x}{2} \):
\[ f(x) = 1 - 2\left(\frac{\sin 2x}{2}\right)^2 = 1 - \frac{1}{2}\sin^2 2x \]
Now analyze the range of \( \sin^2 2x \):
\[ 0 \le \sin^2 2x \le 1 \]
Multiply by \( -\frac{1}{2} \):
\[ -\frac{1}{2} \le -\frac{1}{2}\sin^2 2x \le 0 \]
Add 1 to all parts:
\[ 1 - \frac{1}{2} \le 1 - \frac{1}{2}\sin^2 2x \le 1 \]
\[ \frac{1}{2} \le f(x) \le 1 \]
* **Maximum value:** 1 (when \( \sin^2 2x = 0 \))
* **Minimum value:** \(\frac{1}{2}\) (when \( \sin^2 2x = 1 \))
</details>

---

### Type 7: Solving Simple Equations from Graphs

**Goal:** Use graphs to find solutions of simple trig equations.

**Solved Example:**

Using the graph of y = sin x, find solutions of sin x = 1/2 in [0, 2π].

**Solution:**
```
sin x = 1/2 at x = π/6 and x = 5π/6 (from unit circle/graph)
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 Solve cos x = √3/2 in [0, 2π] using graph.
<details>
<summary>Solution</summary>

On the graph of \( y = \cos x \) for \( x \in [0, 2\pi] \), the line \( y = \frac{\sqrt{3}}{2} \) intersects the cosine wave at two points:
1. One in the first quadrant (\( 0 < x < \frac{\pi}{2} \)) where cosine is positive:
   \[ x = \frac{\pi}{6} \]
2. One in the fourth quadrant (\( \frac{3\pi}{2} < x < 2\pi \)) where cosine is also positive:
   Using the symmetry of the graph about \( 2\pi \) (or \( x = \pi \)):
   \[ x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6} \]

Thus, the solutions in \( [0, 2\pi] \) are:
\[ x = \frac{\pi}{6}, \frac{11\pi}{6} \]
</details>

32. 🟡 Solve tan x = 1 in [0, 2π] using graph.
<details>
<summary>Solution</summary>

On the graph of \( y = \tan x \) for \( x \in [0, 2\pi] \), the line \( y = 1 \) intersects the tangent curves at two points:
1. In the first quadrant (\( 0 < x < \frac{\pi}{2} \)):
   \[ x = \frac{\pi}{4} \]
2. In the third quadrant (\( \pi < x < \frac{3\pi}{2} \)):
   Since tangent has a period of \( \pi \), the next solution is:
   \[ x = \frac{\pi}{4} + \pi = \frac{5\pi}{4} \]

Thus, the solutions in \( [0, 2\pi] \) are:
\[ x = \frac{\pi}{4}, \frac{5\pi}{4} \]
</details>

33. 🟡 Solve sin x = 0 in [0, 4π] using graph.
<details>
<summary>Solution</summary>

On the graph of \( y = \sin x \), the curve crosses the x-axis (where \( \sin x = 0 \)) at all integer multiples of \( \pi \):
\[ x = n\pi \quad \text{where } n \in \mathbb{Z} \]
Within the interval \( [0, 4\pi] \), the values of \( x \) that satisfy this are:
\[ x = 0, \pi, 2\pi, 3\pi, 4\pi \]
</details>

34. 🟡 Solve cos x = −1/2 in [0, 2π] using graph.
<details>
<summary>Solution</summary>

The equation is \( \cos x = -\frac{1}{2} \). Since the value is negative, the solutions lie in the second and third quadrants:
1. The reference angle where \( \cos\theta = \frac{1}{2} \) is \( \theta = \frac{\pi}{3} \).
2. In the second quadrant (\( \frac{\pi}{2} < x < \pi \)):
   \[ x = \pi - \frac{\pi}{3} = \frac{2\pi}{3} \]
3. In the third quadrant (\( \pi < x < \frac{3\pi}{2} \)):
   \[ x = \pi + \frac{\pi}{3} = \frac{4\pi}{3} \]

Thus, the solutions in \( [0, 2\pi] \) are:
\[ x = \frac{2\pi}{3}, \frac{4\pi}{3} \]
</details>

35. 🔴 Solve 2 sin x + 1 = 0 in [0, 2π] using graph.
<details>
<summary>Solution</summary>

First, solve for \( \sin x \):
\[ 2 \sin x + 1 = 0 \implies \sin x = -\frac{1}{2} \]
Since the value is negative, the solutions lie in the third and fourth quadrants:
1. The reference angle is \( \theta = \frac{\pi}{6} \) since \( \sin\frac{\pi}{6} = \frac{1}{2} \).
2. In the third quadrant (\( \pi < x < \frac{3\pi}{2} \)):
   \[ x = \pi + \frac{\pi}{6} = \frac{7\pi}{6} \]
3. In the fourth quadrant (\( \frac{3\pi}{2} < x < 2\pi \)):
   \[ x = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6} \]

Thus, the solutions in \( [0, 2\pi] \) are:
\[ x = \frac{7\pi}{6}, \frac{11\pi}{6} \]
</details>

---

### Type 8: Graph Transformations

**Goal:** Predict how a trig graph changes when the equation is transformed.

**Solved Example:**

How does y = sin(x − π/2) differ from y = sin x?<br>

**Solution:**
```
It shifts right by π/2.
In fact, sin(x − π/2) = −cos x (phase shift).
```
🟡 Medium

---

**Practice Problems:**

36. 🟡 How does y = sin x + 2 differ from y = sin x?<br>
<details>
<summary>Solution</summary>

The equation \( y = \sin x + 2 \) represents a **vertical shift** of the graph \( y = \sin x \) upwards by \( 2 \) units.
Every y-coordinate of the original graph is increased by 2, meaning:
* The midline shifts from \( y = 0 \) to \( y = 2 \).
* The range changes from \( [-1, 1] \) to \( [1, 3] \).
</details>

37. 🟡 How does y = 2 sin x differ from y = sin x?<br>
<details>
<summary>Solution</summary>

The equation \( y = 2 \sin x \) represents a **vertical stretch** of the graph \( y = \sin x \) by a factor of \( 2 \).
* The amplitude increases from \( 1 \) to \( 2 \).
* The range changes from \( [-1, 1] \) to \( [-2, 2] \).
* The x-intercepts remain unchanged.
</details>

38. 🟡 How does y = sin(−x) differ from y = sin x?<br>
<details>
<summary>Solution</summary>

The graph of \( y = \sin(-x) \) is a **reflection across the y-axis** of the graph of \( y = \sin x \).
Since sine is an odd function, \( \sin(-x) = -\sin x \), which means this is also equivalent to a **reflection across the x-axis**.
</details>

39. 🔴 Find the equation of a sine wave with amplitude 2, period π, shifted right by π/4, shifted up by 1.
<details>
<summary>Solution</summary>

We use the general transformed sine wave equation:
\[ y = a \sin(b(x - h)) + k \]
Where:
* \( a \) is the amplitude: \( a = 2 \)
* \( b \) is determined by the period: \( \text{Period} = \frac{2\pi}{b} = \pi \implies b = 2 \)
* \( h \) is the horizontal (phase) shift: shift right by \( \frac{\pi}{4} \implies h = \frac{\pi}{4} \)
* \( k \) is the vertical shift: shift up by \( 1 \implies k = 1 \)

Substituting these values in:
\[ y = 2 \sin\left(2\left(x - \frac{\pi}{4}\right)\right) + 1 \]
\[ y = 2 \sin\left(2x - \frac{\pi}{2}\right) + 1 \]
</details>

40. 🔴 ⭐ How does y = |cos x| differ from y = cos x?<br> Sketch both.
<details>
<summary>Solution</summary>

* **Difference:**
  For \( y = \cos x \), the values alternate between positive and negative, having a range of \( [-1, 1] \) and a period of \( 2\pi \).
  For \( y = |\cos x| \), any negative outputs (where the curve dips below the x-axis, specifically on intervals like \( \left(\frac{\pi}{2}, \frac{3\pi}{2}\right) \)) are reflected across the x-axis to become positive. Thus:
  * The range of \( y = |\cos x| \) is \( [0, 1] \).
  * The period of \( y = |\cos x| \) is \( \pi \) (half of the original period).

* **Sketch description:**
  * \( y = \cos x \): Starts at \( (0, 1) \), goes down to cross the x-axis at \( (\frac{\pi}{2}, 0) \), reaches a minimum at \( (\pi, -1) \), crosses the x-axis again at \( (\frac{3\pi}{2}, 0) \), and ends at \( (2\pi, 1) \).
  * \( y = |\cos x| \): Starts at \( (0, 1) \), goes down to the cusp at \( (\frac{\pi}{2}, 0) \), then bounces back up to a peak of \( 1 \) at \( (\pi, 1) \), goes down to a cusp at \( (\frac{3\pi}{2}, 0) \), and bounces back up to \( 1 \) at \( (2\pi, 1) \). It consists of repeated positive arches.
</details>

---

## Stage 4: Type Mixer

1. 🟡 Find the domain, range, and period of f(x) = 3 cos(2x − π/3) + 1.
<details>
<summary>Solution</summary>

We analyze the function \( f(x) = 3 \cos(2x - \pi/3) + 1 \):
1. **Domain:**
   Since the cosine function is defined for all real values of its input, there are no restrictions on \( x \).
   \[ \text{Domain} = \mathbb{R} \text{ or } (-\infty, \infty) \]
2. **Period:**
   The coefficient of \( x \) is \( b = 2 \).
   \[ \text{Period} = \frac{2\pi}{|b|} = \frac{2\pi}{2} = \pi \]
3. **Range:**
   We start with the range of the cosine function:
   \[ -1 \le \cos\left(2x - \frac{\pi}{3}\right) \le 1 \]
   Multiply by \( 3 \):
   \[ -3 \le 3\cos\left(2x - \frac{\pi}{3}\right) \le 3 \]
   Add \( 1 \) to all parts:
   \[ -3 + 1 \le f(x) \le 3 + 1 \]
   \[ -2 \le f(x) \le 4 \]
   So the Range is \( [-2, 4] \).
</details>

2. 🟡 Sketch y = 2 sin(x − π/4) for one period. Label max, min, and zeros.
<details>
<summary>Solution</summary>

We sketch \( y = 2 \sin(x - \pi/4) \) for one period:
1. **Analysis of transformations:**
   * **Amplitude:** \( 2 \) (oscillates between \( -2 \) and \( 2 \)).
   * **Period:** \( 2\pi \) (no horizontal stretching/compression).
   * **Phase Shift:** \( \frac{\pi}{4} \) units to the right.
2. **Determining the cycle interval:**
   One cycle begins at \( x = \frac{\pi}{4} \) and ends at \( x = \frac{\pi}{4} + 2\pi = \frac{9\pi}{4} \).
3. **Key points in the period \( \left[\frac{\pi}{4}, \frac{9\pi}{4}\right] \):**
   * **Starting Zero:** At \( x = \frac{\pi}{4} \):
     \[ y = 2 \sin(0) = 0 \implies \left(\frac{\pi}{4}, 0\right) \]
   * **Maximum:** At \( x = \frac{\pi}{4} + \frac{\pi}{2} = \frac{3\pi}{4} \):
     \[ y = 2 \sin\left(\frac{\pi}{2}\right) = 2 \implies \left(\frac{3\pi}{4}, 2\right) \]
   * **Middle Zero:** At \( x = \frac{\pi}{4} + \pi = \frac{5\pi}{4} \):
     \[ y = 2 \sin(\pi) = 0 \implies \left(\frac{5\pi}{4}, 0\right) \]
   * **Minimum:** At \( x = \frac{\pi}{4} + \frac{3\pi}{2} = \frac{7\pi}{4} \):
     \[ y = 2 \sin\left(\frac{3\pi}{2}\right) = -2 \implies \left(\frac{7\pi}{4}, -2\right) \]
   * **Ending Zero:** At \( x = \frac{\pi}{4} + 2\pi = \frac{9\pi}{4} \):
     \[ y = 2 \sin(2\pi) = 0 \implies \left(\frac{9\pi}{4}, 0\right) \]

**Sketch description:** A standard sine wave scaled to height 2 and shifted right by \( \frac{\pi}{4} \), passing through zero at \( \frac{\pi}{4} \), \( \frac{5\pi}{4} \), and \( \frac{9\pi}{4} \), peaking at \( \left(\frac{3\pi}{4}, 2\right) \), and bottoming out at \( \left(\frac{7\pi}{4}, -2\right) \).
</details>

3. 🔴 Find the range of f(x) = 2/(sin x − 3). (Hint: sin x − 3 is always negative or zero.)
<details>
<summary>Solution</summary>

We find the range of \( f(x) = \frac{2}{\sin x - 3} \):
1. Find the range of the denominator \( \sin x - 3 \):
   We know that:
   \[ -1 \le \sin x \le 1 \]
   Subtract \( 3 \) from all parts:
   \[ -1 - 3 \le \sin x - 3 \le 1 - 3 \]
   \[ -4 \le \sin x - 3 \le -2 \]
2. Take the reciprocal:
   Since all values in \( [-4, -2] \) are negative, taking the reciprocal reverses the inequality direction:
   \[ -\frac{1}{4} \ge \frac{1}{\sin x - 3} \ge -\frac{1}{2} \implies -\frac{1}{2} \le \frac{1}{\sin x - 3} \le -\frac{1}{4} \]
3. Multiply by \( 2 \):
   \[ 2\left(-\frac{1}{2}\right) \le \frac{2}{\sin x - 3} \le 2\left(-\frac{1}{4}\right) \]
   \[ -1 \le f(x) \le -\frac{1}{2} \]

Therefore, the range of \( f(x) \) is \( \left[-1, -\frac{1}{2}\right] \).
</details>

4. 🔴 ⭐ The function f(x) = a sin bx has amplitude 3 and period π. If f(π/6) = 3/2, find a and b.
<details>
<summary>Solution</summary>

Let's analyze the given conditions for the function \( f(x) = a \sin bx \):
1. **Amplitude is 3:**
   \[ |a| = 3 \implies a = \pm 3 \]
2. **Period is \(\pi\):**
   \[ \frac{2\pi}{|b|} = \pi \implies |b| = 2 \implies b = \pm 2 \]

Now let's check the given function value:
\[ f\left(\frac{\pi}{6}\right) = \frac{3}{2} \]
If we substitute \( a = 3 \) (or \( -3 \)) and \( b = 2 \) (or \( -2 \)) into the function:
* With \( a = 3, b = 2 \):
  \[ f\left(\frac{\pi}{6}\right) = 3 \sin\left(2 \cdot \frac{\pi}{6}\right) = 3 \sin\left(\frac{\pi}{3}\right) = 3 \left(\frac{\sqrt{3}}{2}\right) = \frac{3\sqrt{3}}{2} \neq \frac{3}{2} \]
* With other signs, we get \( \pm \frac{3\sqrt{3}}{2} \).

This indicates an inconsistency in the question's parameters. Let's look at the two logical ways to resolve this:

* **Case A: If we prioritize the given value \( f(\frac{\pi}{6}) = \frac{3}{2} \) and amplitude \( |a| = 3 \)**
  * Since \( a = \pm 3 \), let's choose \( a = 3 \).
  * Then \( 3 \sin\left(b \cdot \frac{\pi}{6}\right) = \frac{3}{2} \implies \sin\left(\frac{b\pi}{6}\right) = \frac{1}{2} \).
  * The smallest positive solution is \( \frac{b\pi}{6} = \frac{\pi}{6} \implies b = 1 \).
  * (In this case, the period of the function would be \( 2\pi \) instead of \( \pi \)).

* **Case B: If we prioritize the period \( \pi \) (so \( |b| = 2 \)) and the value \( f(\frac{\pi}{6}) = \frac{3}{2} \)**
  * Let \( b = 2 \). Then:
    \[ f\left(\frac{\pi}{6}\right) = a \sin\left(2 \cdot \frac{\pi}{6}\right) = a \sin\left(\frac{\pi}{3}\right) = a \frac{\sqrt{3}}{2} \]
  * We set this equal to \( \frac{3}{2} \):
    \[ a \frac{\sqrt{3}}{2} = \frac{3}{2} \implies a = \sqrt{3} \]
  * (In this case, the amplitude would be \( \sqrt{3} \approx 1.732 \) instead of \( 3 \)).
</details>

5. 🔴 Find the maximum and minimum of f(x) = sin x + cos x. (Hint: Write as √2 sin(x + π/4).)
<details>
<summary>Solution</summary>

We rewrite the expression \( f(x) = \sin x + \cos x \) using the linear combination formula:
\[ A \sin x + B \cos x = \sqrt{A^2 + B^2} \sin(x + \theta) \]
Here \( A = 1 \) and \( B = 1 \):
\[ \sqrt{A^2 + B^2} = \sqrt{1^2 + 1^2} = \sqrt{2} \]
Since \( \sin\frac{\pi}{4} = \frac{1}{\sqrt{2}} \) and \( \cos\frac{\pi}{4} = \frac{1}{\sqrt{2}} \), we can write:
\[ f(x) = \sqrt{2} \left( \frac{1}{\sqrt{2}}\sin x + \frac{1}{\sqrt{2}}\cos x \right) = \sqrt{2} \sin\left(x + \frac{\pi}{4}\right) \]
Now, we know the range of the sine function is \( [-1, 1] \):
\[ -1 \le \sin\left(x + \frac{\pi}{4}\right) \le 1 \]
Multiply by \( \sqrt{2} \):
\[ -\sqrt{2} \le \sqrt{2}\sin\left(x + \frac{\pi}{4}\right) \le \sqrt{2} \]
* **Maximum value:** \( \sqrt{2} \)
* **Minimum value:** \( -\sqrt{2} \)
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the period of f(x) = sin 4x + cos 2x. **(2 marks)**

<details>
<summary>Solution</summary>

Period of \(\sin 4x = \frac{2\pi}{4} = \frac{\pi}{2}\)

Period of \(\cos 2x = \frac{2\pi}{2} = \pi\)

LCM of \(\frac{\pi}{2}\) and \(\pi\) is \(\pi\).

Therefore, Period = \(\pi\).
</details>

---

**Q2.** 🟡 Find the range of f(x) = 2 sin²x + 3. **(2 marks)**

<details>
<summary>Solution</summary>

We know that:
\[ 0 \le \sin^2 x \le 1 \]

Multiply by 2:
\[ 0 \le 2\sin^2 x \le 2 \]

Add 3:
\[ 3 \le 2\sin^2 x + 3 \le 5 \]

Therefore, the range is \( [3, 5] \).
</details>

---

**Q3.** 🟡 If y = 3 sin(2x + π/6) − 2, find amplitude, period, phase shift. **(3 marks)**

<details>
<summary>Solution</summary>

Comparing the function with \( y = a \sin(bx + c) + d \):
* \( a = 3 \)
* \( b = 2 \)
* \( c = \frac{\pi}{6} \)
* \( d = -2 \)

Calculations:
* **Amplitude:** \( |a| = 3 \)
* **Period:** \( \frac{2\pi}{|b|} = \frac{2\pi}{2} = \pi \)
* **Phase shift:** \( -\frac{c}{b} = -\frac{\pi/6}{2} = -\frac{\pi}{12} \) (i.e., \( \frac{\pi}{12} \) units to the left)
* **Vertical shift:** \( d = -2 \) (i.e., 2 units downward)
</details>

---

**Q4.** 🔴 Sketch the graph of y = 2 cos(x − π/3) for 0 ≤ x ≤ 2π. Label key points. **(3 marks)**

<details>
<summary>Solution</summary>

For \( y = 2 \cos(x - \pi/3) \):
* **Amplitude:** 2
* **Period:** \( 2\pi \)
* **Phase shift:** \( \frac{\pi}{3} \) units to the right

Key points in \( [0, 2\pi] \):
* **Maximum:** occurs when \( \cos(x - \pi/3) = 1 \implies x - \pi/3 = 0 \implies x = \frac{\pi}{3} \), where \( y = 2 \).
* **Minimum:** occurs when \( \cos(x - \pi/3) = -1 \implies x - \pi/3 = \pi \implies x = \frac{4\pi}{3} \), where \( y = -2 \).
* **Zeros:** occur when \( \cos(x - \pi/3) = 0 \implies x - \pi/3 = \frac{\pi}{2}, \frac{3\pi}{2} \implies x = \frac{5\pi}{6}, \frac{11\pi}{6} \).
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** The period of f(x) = sin(πx/2) is:
(a) 2
(b) 4
(c) π
(d) 2π

<details>
<summary>Solution</summary>
Period = 2π/(π/2) = 4
Answer: (b) 🟢
</details>

---

**Q2.** The range of f(x) = 2 + 3 sin x is:
(a) [−1, 5]
(b) [−1, 3]
(c) [2, 5]
(d) [−1, 5]

<details>
<summary>Solution</summary>
3 sin x ∈ [−3, 3]
f(x) ∈ [−1, 5]
Answer: (a) 🟢 ⭐
</details>

---

**Q3.** The number of solutions of sin x = x/10 in [0, 2π] is:
(a) 1
(b) 2
(c) 3
(d) 4

<details>
<summary>Solution</summary>
Sketch y = sin x and y = x/10.
At x = 0: sin 0 = 0, x/10 = 0 (intersect)
At x = π: sin π = 0, x/10 = π/10 ≈ 0.314 (sin above line)
At x = 2π: sin 2π = 0, x/10 = 0.628 (line above sin)
Three intersections: at 0, between 0 and π, between π and 2π.
Answer: (c) 🔴 ⭐
</details>

---

**Q4.** Which of the following is an even function?<br>
(a) sin x
(b) cos x
(c) tan x
(d) cosec x

<details>
<summary>Solution</summary>
cos(−x) = cos x, so cos x is even.
Answer: (b) 🟢
</details>

---

**Q5.** The amplitude of y = 2 sin(3x + π/4) is:
(a) 2
(b) 3
(c) π/4
(d) 1

<details>
<summary>Solution</summary>
Amplitude = |coefficient of sin| = 2
Answer: (a) 🟢
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** The range of sin x is [−1, 1].
**Reason (R):** On the unit circle, y-coordinate ranges from −1 to 1.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** tan x has period π.
**Reason (R):** tan(x + π) = tan x for all x in its domain.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The function f(x) = sin x is odd.
**Reason (R):** For all x, sin(−x) = −sin x.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** The function f(x) = sin x + cos x has amplitude √2.
**Reason (R):** sin x + cos x = √2 sin(x + π/4).

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The domain of sin x is:
   (a) [−1, 1]   (b) ℝ   (c) ℝ − {π/2}   (d) [0, ∞)
<details>
<summary>Solution</summary>

The sine function \( f(x) = \sin x \) is defined for all real numbers \( x \). There are no values where it is undefined.

**Answer: (b) ℝ**
</details>

2. 🟢 The range of cos x is:
   (a) ℝ   (b) [−1, 1]   (c) [0, 1]   (d) (−1, 1)
<details>
<summary>Solution</summary>

For any real number \( x \), the value of \( \cos x \) lies between \(-1\) and \(1\), inclusive:
\[ -1 \le \cos x \le 1 \]

**Answer: (b) [−1, 1]**
</details>

3. 🟢 The period of sin x is:
   (a) π   (b) 2π   (c) π/2   (d) 4π
<details>
<summary>Solution</summary>

The sine function is periodic with a fundamental period of \( 2\pi \) because:
\[ \sin(x + 2\pi) = \sin x \]
and \( 2\pi \) is the smallest positive value for which this holds for all \( x \).

**Answer: (b) 2π**
</details>

4. 🟢 The period of tan x is:
   (a) π   (b) 2π   (c) π/2   (d) 4π
<details>
<summary>Solution</summary>

The tangent function repeats its values every \( \pi \) radians:
\[ \tan(x + \pi) = \tan x \]
Thus, the period of \( \tan x \) is \( \pi \).

**Answer: (a) π**
</details>

5. 🟡 The period of sin 3x is:
   (a) π   (b) 2π/3   (c) π/3   (d) 6π
<details>
<summary>Solution</summary>

For a function of the form \( f(x) = \sin(bx) \), the period is given by:
\[ T = \frac{2\pi}{|b|} \]
Here \( b = 3 \), so:
\[ T = \frac{2\pi}{3} \]

**Answer: (b) 2π/3**
</details>

6. 🟡 The amplitude of 3 sin x + 4 cos x is:
   (a) 3   (b) 4   (c) 5   (d) 7
<details>
<summary>Solution</summary>

An expression of the form \( A \sin x + B \cos x \) can be rewritten as:
\[ \sqrt{A^2 + B^2} \sin(x + \theta) \]
The amplitude is \( \sqrt{A^2 + B^2} \).
Here \( A = 3 \) and \( B = 4 \):
\[ \text{Amplitude} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \]

**Answer: (c) 5**
</details>

7. 🟡 The range of f(x) = 1 + sin x is:
   (a) [0, 2]   (b) [−1, 1]   (c) [0, 1]   (d) [1, 2]
<details>
<summary>Solution</summary>

Since \( -1 \le \sin x \le 1 \):
Add 1 to all parts:
\[ 1 - 1 \le 1 + \sin x \le 1 + 1 \]
\[ 0 \le f(x) \le 2 \]

**Answer: (a) [0, 2]**
</details>

8. 🟡 tan x is undefined at:
   (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 2π
<details>
<summary>Solution</summary>

\( \tan x = \frac{\sin x}{\cos x} \).
This is undefined when \( \cos x = 0 \).
Among the options, \( \cos(\frac{\pi}{2}) = 0 \).
Therefore, \( \tan x \) is undefined at \( x = \frac{\pi}{2} \).

**Answer: (b) x = π/2**
</details>

9. 🟡 cos x = 0 at:
   (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 2π
<details>
<summary>Solution</summary>

The cosine function is zero at all odd multiples of \( \frac{\pi}{2} \).
Looking at the options, \( \cos(\frac{\pi}{2}) = 0 \).

**Answer: (b) x = π/2**
</details>

10. 🟡 sin x attains its maximum at:
    (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 3π/2
<details>
<summary>Solution</summary>

The maximum value of \( \sin x \) is \( 1 \).
Looking at the given options:
* \( \sin 0 = 0 \)
* \( \sin(\frac{\pi}{2}) = 1 \) (Maximum)
* \( \sin\pi = 0 \)
* \( \sin(\frac{3\pi}{2}) = -1 \) (Minimum)

**Answer: (b) x = π/2**
</details>

11. 🟡 An odd function satisfies:
    (a) f(−x) = f(x)   (b) f(−x) = −f(x)   (c) f(−x) = 0   (d) f(x) = 0
<details>
<summary>Solution</summary>

By definition:
* A function is **even** if \( f(-x) = f(x) \) for all \( x \) in its domain.
* A function is **odd** if \( f(-x) = -f(x) \) for all \( x \) in its domain.

**Answer: (b) f(−x) = −f(x)**
</details>

12. 🟡 sec x has asymptotes where:
    (a) sin x = 0   (b) cos x = 0   (c) tan x = 0   (d) cot x = 0
<details>
<summary>Solution</summary>

Since \( \sec x = \frac{1}{\cos x} \), the function has vertical asymptotes where the denominator is zero, i.e., where \( \cos x = 0 \).

**Answer: (b) cos x = 0**
</details>

13. 🟡 The range of cosec x is:
    (a) [−1, 1]   (b) ℝ   (c) (−∞, −1] ∪ [1, ∞)   (d) [0, ∞)
<details>
<summary>Solution</summary>

Since \( \operatorname{cosec} x = \frac{1}{\sin x} \) and \( -1 \le \sin x \le 1 \) (with \( \sin x \neq 0 \)):
* When \( 0 < \sin x \le 1 \), we have \( \operatorname{cosec} x \ge 1 \).
* When \( -1 \le \sin x < 0 \), we have \( \operatorname{cosec} x \le -1 \).
Thus, the range is \( (-\infty, -1] \cup [1, \infty) \).

**Answer: (c) (−∞, −1] ∪ [1, ∞)**
</details>

14. 🟡 The period of |sin x| is:
    (a) π   (b) 2π   (c) π/2   (d) 4π
<details>
<summary>Solution</summary>

The standard sine function \( \sin x \) has period \( 2\pi \).
Taking the absolute value reflects the negative parts across the x-axis, making both half-cycles positive and identical. Thus, it repeats every \( \pi \) radians:
\[ |\sin(x + \pi)| = |-\sin x| = |\sin x| \]

**Answer: (a) π**
</details>

15. 🟡 The phase shift of y = sin(x − π/3) is:
    (a) π/3 left   (b) π/3 right   (c) π/6 left   (d) π/6 right
<details>
<summary>Solution</summary>

A function of the form \( y = \sin(x - h) \) represents a horizontal shift of \( h \) units:
* If \( h > 0 \), the shift is to the right.
* If \( h < 0 \), the shift is to the left.
Here, \( h = \frac{\pi}{3} \), which is positive. So the phase shift is \( \frac{\pi}{3} \) units to the right.

**Answer: (b) π/3 right**
</details>

16. 🟡 The vertical shift of y = 2 cos x + 3 is:
    (a) 2   (b) 3   (c) 5   (d) −3
<details>
<summary>Solution</summary>

Comparing \( y = 2 \cos x + 3 \) to the standard vertical transformation form \( y = a \cos x + d \):
The term \( d = 3 \) represents the vertical shift.
Thus, the graph is shifted vertically upwards by 3 units.

**Answer: (b) 3**
</details>

17. 🟡 sin x + cos x can be written as:
    (a) √2 sin(x + π/4)   (b) √2 cos(x + π/4)   (c) 2 sin(x + π/4)   (d) sin(x + π/4)
<details>
<summary>Solution</summary>

We rewrite \( \sin x + \cos x \) by multiplying and dividing by \( \sqrt{1^2 + 1^2} = \sqrt{2} \):
\[ \sin x + \cos x = \sqrt{2} \left( \frac{1}{\sqrt{2}}\sin x + \frac{1}{\sqrt{2}}\cos x \right) \]
Since \( \cos\frac{\pi}{4} = \frac{1}{\sqrt{2}} \) and \( \sin\frac{\pi}{4} = \frac{1}{\sqrt{2}} \), we can use the sum formula for sine \( \sin(A+B) = \sin A\cos B + \cos A\sin B \):
\[ \sin x + \cos x = \sqrt{2} \left( \sin x \cos\frac{\pi}{4} + \cos x \sin\frac{\pi}{4} \right) = \sqrt{2} \sin\left(x + \frac{\pi}{4}\right) \]

**Answer: (a) √2 sin(x + π/4)**
</details>

18. 🟡 The number of times sin x attains 1 in [0, 2π] is:
    (a) 0   (b) 1   (c) 2   (d) infinite
<details>
<summary>Solution</summary>

In the interval \( [0, 2\pi] \), \( \sin x = 1 \) only at the single value \( x = \frac{\pi}{2} \).
Therefore, the function attains 1 exactly 1 time.

**Answer: (b) 1**
</details>

19. 🟡 The range of f(x) = 2 sin²x − 1 is:
    (a) [−1, 1]   (b) [0, 1]   (c) [−2, 0]   (d) [−1, 0]
<details>
<summary>Solution</summary>

Using the double-angle identity:
\[ \cos 2x = 1 - 2\sin^2 x \implies 2\sin^2 x - 1 = -\cos 2x \]
Since the range of \( -\cos 2x \) is the same as the range of \( \cos 2x \), which is \( [-1, 1] \), the range of the function is \( [-1, 1] \).
Alternatively:
\[ 0 \le \sin^2 x \le 1 \]
Multiply by 2:
\[ 0 \le 2\sin^2 x \le 2 \]
Subtract 1:
\[ -1 \le 2\sin^2 x - 1 \le 1 \]

**Answer: (a) [−1, 1]**
</details>

20. 🟡 Which function has range ℝ?<br>
    (a) sin x   (b) cos x   (c) tan x   (d) sec x
<details>
<summary>Solution</summary>

Let's check the ranges of the functions:
* \( \sin x \): range is \( [-1, 1] \)
* \( \cos x \): range is \( [-1, 1] \)
* \( \tan x \): range is \( (-\infty, \infty) \) (all real numbers, \( \mathbb{R} \))
* \( \sec x \): range is \( (-\infty, -1] \cup [1, \infty) \)

**Answer: (c) tan x**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | c | 11 | b | 16 | b |
| 2 | b | 7 | a | 12 | b | 17 | a |
| 3 | b | 8 | b | 13 | c | 18 | b |
| 4 | a | 9 | b | 14 | a | 19 | a |
| 5 | b | 10 | b | 15 | b | 20 | c |

</details>
