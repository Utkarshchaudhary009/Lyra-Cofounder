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
2. 🟡 Evaluate lim_{x to 0} tan 3x / sin 4x.
3. 🟡 Evaluate lim_{x to 0} (1 - cos 2x)/x^2.
4. 🟡 Evaluate lim_{x to 0} (sin 5x - sin 3x)/x.
5. 🔴 Evaluate lim_{x to 0} (sin x - x)/x^3.

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
7. 🟡 Evaluate lim_{x to 0} (sin^{-1}x)/x.
8. 🔴 Evaluate lim_{x to pi/2} (1 - sin x)/(pi/2 - x)^2.
9. 🔴 ⭐ Evaluate lim_{x to 0} (x cos x - sin x)/x^3.
10. 🔴 Evaluate lim_{x to 0} (e^x - e^{-x} - 2 sin x)/x^3.

---

### Type 3: Derivatives of sin, cos, tan

**Goal:** Differentiate basic trig functions.

**Solved Example:**

Find d/dx (x^2 sin x).

**Solution:**
```
Using product rule:
= 2x sin x + x^2 cos x
```
🟢 Easy

---

**Practice Problems:**

11. 🟢 Find d/dx (sin 3x).
12. 🟢 Find d/dx (cos(x^2)).
13. 🟡 Find d/dx (tan x / x).
14. 🟡 Find d/dx (sin x * cos x).
15. 🔴 ⭐ Find d/dx (sin^{-1}(x^2)).

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
17. 🟡 Find d/dx (cos^{-1}(1/x)).
18. 🟡 Find d/dx (sin^{-1}(2x/(1+x^2))).
19. 🔴 ⭐ Find d/dx (tan^{-1}(x/(1+sqrt(1-x^2)))).
20. 🔴 Find d/dx (sec^{-1}(x^2)).

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
22. 🟢 Evaluate int sec^2(2x) dx.
23. 🟡 Evaluate int (sec x tan x + cosec^2 x) dx.
24. 🟡 Evaluate int tan^2 x dx. (Hint: tan^2 x = sec^2 x - 1)
25. 🔴 ⭐ Evaluate int sec^4 x dx.

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
27. 🟡 Evaluate int tan x sec^2 x dx.
28. 🔴 Evaluate int sin^2 x cos^3 x dx.
29. 🔴 ⭐ Evaluate int sin^4 x dx using reduction.
30. 🔴 Evaluate int sec^3 x dx.

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
32. 🟡 Evaluate int_0^{pi/2} sin^2 x dx.
33. 🟡 ⭐ Evaluate int_0^{pi/2} cos^3 x dx.
34. 🔴 Evaluate int_0^{pi} x sin x dx.
35. 🔴 ⭐ Evaluate int_0^{pi/2} (sin x - cos x)/(sin x + cos x) dx.

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
37. 🟡 Find the minimum of f(x) = x + tan x for x in (0, pi/2).
38. 🔴 Find the maximum area of a rectangle inscribed in a semicircle of radius r.
39. 🔴 ⭐ Find the maximum of f(x) = sin^2 x + cos^4 x.
40. 🔴 A ladder of length L slides down a wall. Find the maximum area of the triangle formed by the ladder, wall, and floor.

---

## Stage 4: Type Mixer

1. 🟡 Evaluate lim_{x to 0} (sin 2x - 2 sin x)/x^3.

2. 🟡 Find dy/dx if y = tan^{-1}((sin x)/(1 + cos x)).

3. 🔴 ⭐ Evaluate int_0^{pi/2} sin^3 x cos^2 x dx.

4. 🔴 Find the maximum value of sin x + cos x + sin 2x in [0, pi/2].

5. 🔴 Evaluate int_0^{pi/2} sin x/(sin x + cos x) dx using the property int_0^a f(x) dx = int_0^a f(a-x) dx.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Evaluate lim_{x to 0} tan 2x / sin 3x. **(2 marks)**

**Solution:**
```
= lim (2x * tan 2x/(2x)) / (3x * sin 3x/(3x))
= (2/3) * 1/1 = 2/3
```

---

**Q2.** 🟡 Find d/dx (sin^{-1}(2x)). **(2 marks)**

**Solution:**
```
dy/dx = 1/sqrt(1 - 4x^2) * 2 = 2/sqrt(1 - 4x^2)
```

---

**Q3.** 🟡 Evaluate int sec^2(3x) dx. **(1 mark)**

**Solution:**
```
= (1/3) tan 3x + C
```

---

**Q4.** 🟡 ⭐ Evaluate int_0^{pi/2} sin^2 x dx. **(2 marks)**

**Solution:**
```
int sin^2 x dx = int (1-cos 2x)/2 dx = x/2 - sin 2x/4
From 0 to pi/2: (pi/4 - 0) - (0 - 0) = pi/4
```

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
(A): d/dx (sin x) = cos x.
Reason (R): This follows from the limit definition of derivative.

Both true, R explains A. Answer: (a)

---

**Q2.** 🟡 Assertion <br>
(A): int sec
