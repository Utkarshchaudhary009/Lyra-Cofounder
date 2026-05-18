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
2. 🟡 What is the domain of tan x?<br>
3. 🟡 What is the domain of sec x?<br>
4. 🟡 Find the domain of f(x) = 2/(cos x − 1).
5. 🔴 Find the domain of f(x) = 1/(sin x − 1/2).

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
7. 🟡 Find the range of f(x) = 5 − 3 sin x.
8. 🟡 Find the range of f(x) = 2 tan x + 1 (over its domain).
9. 🔴 Find the range of f(x) = 1/(sin x + 2).
10. 🔴 ⭐ Find the range of f(x) = sin²x − sin x + 1.

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
12. 🟡 Sketch y = 2 sin x. What is its amplitude?<br>
13. 🟡 Sketch y = sin 2x. What is its period?<br>
14. 🟡 Sketch y = sin x + 1. What is its range?<br>
15. 🟡 Sketch y = |sin x| for 0 ≤ x ≤ 2π.

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
17. 🟢 Find the period of tan 4x.
18. 🟡 Find the period of sin(x/2).
19. 🟡 Find the period of |sin x|.
20. 🔴 Find the period of sin 2x + cos 3x.

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
22. 🟡 y = −sin(x/2 − π/6). Find amplitude, period, phase shift.
23. 🟡 y = 4 tan(2x − π/3). Find period and phase shift.
24. 🔴 y = 2 sin(πx + 1) + 3. Find amplitude, period, phase shift.
25. 🔴 ⭐ A sine wave has period π, amplitude 3, and passes through (0, 0). Write its equation.

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
27. 🟡 Max and min of f(x) = 1/(2 + sin x).
28. 🟡 Max and min of f(x) = 2 − 3 sin 2x.
29. 🔴 Max and min of f(x) = sin²x + cos²x. (Think first!)
30. 🔴 ⭐ Max and min of f(x) = sin⁴x + cos⁴x.

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
32. 🟡 Solve tan x = 1 in [0, 2π] using graph.
33. 🟡 Solve sin x = 0 in [0, 4π] using graph.
34. 🟡 Solve cos x = −1/2 in [0, 2π] using graph.
35. 🔴 Solve 2 sin x + 1 = 0 in [0, 2π] using graph.

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
37. 🟡 How does y = 2 sin x differ from y = sin x?<br>
38. 🟡 How does y = sin(−x) differ from y = sin x?<br>
39. 🔴 Find the equation of a sine wave with amplitude 2, period π, shifted right by π/4, shifted up by 1.
40. 🔴 ⭐ How does y = |cos x| differ from y = cos x?<br> Sketch both.

---

## Stage 4: Type Mixer

1. 🟡 Find the domain, range, and period of f(x) = 3 cos(2x − π/3) + 1.

2. 🟡 Sketch y = 2 sin(x − π/4) for one period. Label max, min, and zeros.

3. 🔴 Find the range of f(x) = 2/(sin x − 3). (Hint: sin x − 3 is always negative or zero.)

4. 🔴 ⭐ The function f(x) = a sin bx has amplitude 3 and period π. If f(π/6) = 3/2, find a and b.

5. 🔴 Find the maximum and minimum of f(x) = sin x + cos x. (Hint: Write as √2 sin(x + π/4).)

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Find the period of f(x) = sin 4x + cos 2x. **(2 marks)**

**Solution:**
```
Period of sin 4x = π/2
Period of cos 2x = π
LCM of π/2 and π = π
Period = π
```

---

**Q2.** 🟡 Find the range of f(x) = 2 sin²x + 3. **(2 marks)**

**Solution:**
```
sin²x ∈ [0, 1]
2 sin²x ∈ [0, 2]
f(x) ∈ [3, 5]
```

---

**Q3.** 🟡 If y = 3 sin(2x + π/6) − 2, find amplitude, period, phase shift. **(3 marks)**

**Solution:**
```
Amplitude = 3
Period = 2π/2 = π
Phase shift = −π/12 (left)
Vertical shift = −2
```

---

**Q4.** 🔴 Sketch the graph of y = 2 cos(x − π/3) for 0 ≤ x ≤ 2π. Label key points. **(3 marks)**

**Solution:**
```
Max at x = π/3, y = 2
Min at x = 4π/3, y = −2
Zero at x = 5π/6 and x = 11π/6
```

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

2. 🟢 The range of cos x is:
   (a) ℝ   (b) [−1, 1]   (c) [0, 1]   (d) (−1, 1)

3. 🟢 The period of sin x is:
   (a) π   (b) 2π   (c) π/2   (d) 4π

4. 🟢 The period of tan x is:
   (a) π   (b) 2π   (c) π/2   (d) 4π

5. 🟡 The period of sin 3x is:
   (a) π   (b) 2π/3   (c) π/3   (d) 6π

6. 🟡 The amplitude of 3 sin x + 4 cos x is:
   (a) 3   (b) 4   (c) 5   (d) 7

7. 🟡 The range of f(x) = 1 + sin x is:
   (a) [0, 2]   (b) [−1, 1]   (c) [0, 1]   (d) [1, 2]

8. 🟡 tan x is undefined at:
   (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 2π

9. 🟡 cos x = 0 at:
   (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 2π

10. 🟡 sin x attains its maximum at:
    (a) x = 0   (b) x = π/2   (c) x = π   (d) x = 3π/2

11. 🟡 An odd function satisfies:
    (a) f(−x) = f(x)   (b) f(−x) = −f(x)   (c) f(−x) = 0   (d) f(x) = 0

12. 🟡 sec x has asymptotes where:
    (a) sin x = 0   (b) cos x = 0   (c) tan x = 0   (d) cot x = 0

13. 🟡 The range of cosec x is:
    (a) [−1, 1]   (b) ℝ   (c) (−∞, −1] ∪ [1, ∞)   (d) [0, ∞)

14. 🟡 The period of |sin x| is:
    (a) π   (b) 2π   (c) π/2   (d) 4π

15. 🟡 The phase shift of y = sin(x − π/3) is:
    (a) π/3 left   (b) π/3 right   (c) π/6 left   (d) π/6 right

16. 🟡 The vertical shift of y = 2 cos x + 3 is:
    (a) 2   (b) 3   (c) 5   (d) −3

17. 🟡 sin x + cos x can be written as:
    (a) √2 sin(x + π/4)   (b) √2 cos(x + π/4)   (c) 2 sin(x + π/4)   (d) sin(x + π/4)

18. 🟡 The number of times sin x attains 1 in [0, 2π] is:
    (a) 0   (b) 1   (c) 2   (d) infinite

19. 🟡 The range of f(x) = 2 sin²x − 1 is:
    (a) [−1, 1]   (b) [0, 1]   (c) [−2, 0]   (d) [−1, 0]

20. 🟡 Which function has range ℝ?<br>
    (a) sin x   (b) cos x   (c) tan x   (d) sec x

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
