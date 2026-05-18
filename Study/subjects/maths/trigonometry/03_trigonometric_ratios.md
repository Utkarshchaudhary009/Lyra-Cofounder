# Chapter 3: Trigonometric Ratios in Right Triangles

---

## Stage 1: The Core Idea

### From Similar Triangles to Ratios

Take any right triangle with an acute angle θ. Now draw a bigger one with the same angle — scaled up by 2×. The sides are longer, but the **ratios** of corresponding sides are identical.

```
Small triangle:  opp=3, adj=4, hyp=5
Large triangle:  opp=6, adj=8, hyp=10

opp/hyp = 3/5 = 6/10 = 0.6    ← Same!
adj/hyp = 4/5 = 8/10 = 0.8    ← Same!
opp/adj = 3/4 = 6/8 = 0.75    ← Same!
```

This is the **core idea of trigonometry**: for a fixed angle, these ratios never change — no matter how big or small the triangle.

These fixed ratios have names:

| Name | Ratio | Abbreviation |
|------|-------|-------------|
| Sine of θ | opposite / hypotenuse | sin θ |
| Cosine of θ | adjacent / hypotenuse | cos θ |
| Tangent of θ | opposite / adjacent | tan θ |
| Cosecant of θ | hypotenuse / opposite | cosec θ |
| Secant of θ | hypotenuse / adjacent | sec θ |
| Cotangent of θ | adjacent / opposite | cot θ |

### The Memory Trick — SOH CAH TOA

```
SOH  →  Sine = Opposite / Hypotenuse
CAH  →  Cosine = Adjacent / Hypotenuse
TOA  →  Tangent = Opposite / Adjacent
```

The other three are just reciprocals:
- cosec θ = 1 / sin θ
- sec θ = 1 / cos θ
- cot θ = 1 / tan θ

---

## Stage 2: The Formula Lab

### The Six Ratios

For a right triangle with angle θ:

```
        ┌───┐
        │   │
   opp  │   │  hyp
        │   │
        └───┘
          adj

sin θ = opp/hyp       cosec θ = hyp/opp
cos θ = adj/hyp       sec θ   = hyp/adj
tan θ = opp/adj       cot θ   = adj/opp
```

**Trap to avoid:** tan θ = sin θ / cos θ (not cos θ / sin θ). Remember TOA: Tangent = Opposite/Adjacent.

### Quotient Identities

```
tan θ = sin θ / cos θ
cot θ = cos θ / sin θ
```

### Reciprocal Identities

```
cosec θ = 1 / sin θ
sec θ   = 1 / cos θ
cot θ   = 1 / tan θ
```

---

## Stage 3: Type-wise Mastery

### Type 1: Finding Ratios from Triangle Sides

**Goal:** Given a right triangle with labelled sides, write all six trig ratios for a marked angle.

**Solved Example:**

In triangle ABC, ∠B = 90°, AB = 3, BC = 4, AC = 5. Find all six trig ratios for ∠C.

**Solution:**
```
For ∠C:
  opposite side = AB = 3
  adjacent side = BC = 4
  hypotenuse   = AC = 5

sin C = opp/hyp = 3/5          cosec C = 5/3
cos C = adj/hyp = 4/5          sec C   = 5/4
tan C = opp/adj = 3/4          cot C   = 4/3
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 In a right triangle with sides 5, 12, 13 (right angle between 5 and 12), find all six ratios for the angle opposite the side of length 5.

2. 🟢 In ∆PQR, ∠Q = 90°, PQ = 7, QR = 24, PR = 25. Find sin P, cos P, tan P.

3. 🟢 For the same triangle, find cosec R, sec R, cot R.

4. 🟡 In ∆XYZ, ∠Y = 90°, XY = a, YZ = b, XZ = c. Write all six ratios for ∠X.

5. 🟡 If sin θ = 3/5, can you find cos θ without a triangle?<br> What if θ is acute?<br>

---

### Type 2: Finding One Ratio from Another

**Goal:** Given one trig ratio, find the others using Pythagoras.

**Solved Example:**

If sin θ = 3/5 and θ is acute, find cos θ and tan θ.

**Solution:**
```
sin θ = opp/hyp = 3/5
Let opp = 3k, hyp = 5k

adj² = hyp² − opp² = 25k² − 9k² = 16k²
adj = 4k

cos θ = adj/hyp = 4/5
tan θ = opp/adj = 3/4
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

6. 🟡 If cos θ = 5/13, find sin θ and tan θ (θ acute).

7. 🟡 If tan θ = 4/3, find sin θ and cos θ (θ acute).

8. 🟡 If cosec θ = √2, find cot θ and cos θ.

9. 🟡 If sec θ = 25/7, find tan θ and sin θ.

10. 🔴 If cot θ = 1/√3, find sin θ + cos θ.

---

### Type 3: Finding Sides Using a Given Ratio

**Goal:** Use a given trig ratio to find unknown side lengths.

**Solved Example:**

In ∆ABC, ∠B = 90°, ∠C = θ, sin θ = 3/5, and AB = 9 cm. Find AC and BC.

**Solution:**
```
sin θ = opp/hyp = AB/AC = 3/5
9/AC = 3/5
AC = 9 × 5/3 = 15 cm

BC² = AC² − AB² = 225 − 81 = 144
BC = 12 cm
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 In ∆PQR, ∠Q = 90°, cos R = 4/5, QR = 8 cm. Find PR and PQ.

12. 🟡 If tan θ = 2 and the opposite side is 10 cm, find the adjacent and hypotenuse.

13. 🟡 sin θ = 1/2 and hypotenuse = 20 cm. Find the other two sides.

14. 🔴 cosec θ = 2 and adjacent side = 5√3 cm. Find the opposite and hypotenuse.

15. 🟡 In a right triangle, sec θ = √2 and adjacent side = 7 cm. Find the other sides.

---

### Type 4: Verifying Trigonometric Identities (Simple)

**Goal:** Use side lengths to verify that identities hold.

**Solved Example:**

For the triangle with sides 3, 4, 5 and angle θ opposite side 3, verify that sin²θ + cos²θ = 1.

**Solution:**
```
sin θ = 3/5, cos θ = 4/5
sin²θ + cos²θ = (9/25) + (16/25) = 25/25 = 1 ✓
```
🟢 Easy

---

**Practice Problems:**

16. 🟢 Verify sin²θ + cos²θ = 1 for a 5-12-13 triangle.

17. 🟢 Verify 1 + tan²θ = sec²θ for the same triangle.

18. 🟡 Verify 1 + cot²θ = cosec²θ for an 8-15-17 triangle.

19. 🟡 If sin θ = a/c, cos θ = b/c, prove sin²θ + cos²θ = 1 using Pythagoras.

20. 🟡 If tan θ = 2, show that sin²θ + cos²θ = 1 using the triangle method.

---

### Type 5: Expressing Ratios in Simplest Form

**Goal:** Simplify trig ratio expressions using triangle side relationships.

**Solved Example:**

If 3 sin θ = 4 cos θ, find tan θ.

**Solution:**
```
3 sin θ = 4 cos θ
sin θ / cos θ = 4/3
tan θ = 4/3
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

21. 🟡 If 5 sin θ = 12 cos θ, find tan θ.

22. 🟡 If tan θ = √3, find (sin θ + cos θ)/(sin θ − cos θ).

23. 🟡 If sec θ = 2, find (1 − sin θ)/(1 + sin θ).

24. 🔴 If 2 sin θ = 3 cos θ, find sin²θ + cos²θ. (Trick question?<br> Why?<br>)

25. 🟡 If cot θ = 1, find sin θ cos θ.

---

### Type 6: Finding Ratios of Complementary Angles

**Goal:** Understand how ratios change when θ → 90° − θ.

**Key relationship:**
```
sin(90° − θ) = cos θ
cos(90° − θ) = sin θ
tan(90° − θ) = cot θ
```

**Solved Example:**

If sin 30° = 1/2, find cos 60°.

**Solution:**
```
cos 60° = sin(90° − 60°) = sin 30° = 1/2
```
🟢 Easy

---

**Practice Problems:**

26. 🟢 If cos 45° = 1/√2, find sin 45°.

27. 🟢 If tan 60° = √3, find cot 30°.

28. 🟡 Prove that sin(90° − θ) = cos θ using a right triangle.

29. 🟡 If sec θ = cosec 60°, find θ.

30. 🟡 If sin 2θ = cos 3θ, find θ (both acute).

---

### Type 7: Finding Ratios When Two Sides Are in Ratio

**Goal:** Work with triangles where sides are given in ratio form.

**Solved Example:**

The sides of a right triangle are in the ratio 5 : 12 : 13. Find sin θ and cos θ for the smallest acute angle.

**Solution:**
```
Smallest angle is opposite the smallest side (5).
sin θ = 5/13, cos θ = 12/13
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 Sides in ratio 3 : 4 : 5. Find all six ratios for both acute angles.

32. 🟡 Sides in ratio 7 : 24 : 25. Find tan of the smaller acute angle.

33. 🟡 Sides in ratio 8 : 15 : 17. Find sec and cosec of the larger acute angle.

34. 🔴 The legs of a right triangle are in ratio 1 : √3. Find the acute angles.

35. 🔴 ⭐ If the sides of a right triangle are in AP (arithmetic progression), find the ratio of its sides.

---

### Type 8: Word Problems Using Trig Ratios

**Goal:** Set up trig ratios from real-world descriptions.

**Solved Example:**

A ladder leaning against a wall makes an angle θ with the ground. If the ladder is 10 m long and reaches 8 m up the wall, find sin θ and cos θ.

**Solution:**
```
sin θ = opp/hyp = 8/10 = 4/5
cos θ = adj/hyp = (√(100−64))/10 = 6/10 = 3/5
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

36. 🟡 A ramp of length 5 m rises to a height of 3 m. Find sin, cos, tan of the angle it makes with the ground.

37. 🟡 A guy wire 13 m long from the top of a pole to a peg on the ground is at an angle θ with the pole. If the peg is 5 m from the foot of the pole, find sin θ.

38. 🔴 ⭐ From the top of a 20 m building, the angle of depression of a car is θ where tan θ = 4/3. Find the distance of the car from the building.

39. 🔴 A kite flying at a height of 60 m has a string of length 100 m at an angle θ with the horizontal. Find sin θ and cos θ.

40. 🟡 A river is crossed by a bridge of length 50 m at an angle θ to the bank. If the width of the river is 30 m, find sin θ.

---

## Stage 4: Type Mixer

1. 🟡 If sin θ = 5/13, find cos θ and tan θ. Then find sin(90° − θ).

2. 🟡 In a right triangle, tan θ = 3/4 and hypotenuse = 15. Find all sides and all six ratios for θ.

3. 🔴 If 7 sin²θ + 3 cos²θ = 4, find tan θ.

4. 🔴 ⭐ In a right triangle, the sides are in the ratio 1 : 2 : √5. Find sin θ and cos θ for the smallest angle. Also verify sin²θ + cos²θ = 1.

5. 🟡 A vertical pole of height h casts a shadow of length 2h. Find the angle of elevation of the sun.

---

## Stage 5: Board Arsenal

**Q1.** 🟢 In ∆ABC, ∠B = 90°, AB = 6, BC = 8. Find sin A, cos A, and tan A. **(2 marks)**

**Solution:**
```
AC = √(6² + 8²) = 10
sin A = BC/AC = 8/10 = 4/5
cos A = AB/AC = 6/10 = 3/5
tan A = BC/AB = 8/6 = 4/3
```

---

**Q2.** 🟡 If sec θ = 13/5, find the values of other trig ratios. **(3 marks)**

**Solution:**
```
sec θ = hyp/adj = 13/5
Let hyp = 13k, adj = 5k
opp² = 169k² − 25k² = 144k²
opp = 12k

sin θ = 12/13, cos θ = 5/13, tan θ = 12/5
cosec θ = 13/12, cot θ = 5/12
```

---

**Q3.** 🟡 If tan θ = 4/3, find the value of (sin θ − cos θ)/(sin θ + cos θ). **(3 marks)**

**Solution:**
```
tan θ = 4/3 → sin θ = 4k, cos θ = 3k (by triangle method)
(sin θ − cos θ)/(sin θ + cos θ) = (4k − 3k)/(4k + 3k) = k/7k = 1/7
```

---

**Q4.** 🟡 If sin θ = 3/5, find tan θ and sec θ. Also verify sec²θ − tan²θ = 1. **(3 marks)**

**Solution:**
```
sin θ = 3/5 → opp = 3, hyp = 5, adj = 4
tan θ = 3/4, sec θ = 5/4
sec²θ − tan²θ = 25/16 − 9/16 = 16/16 = 1 ✓
```

---

## Stage 6: JEE Mains Arena

**Q1.** If sin θ = 3/5 and θ is acute, then cos θ + tan θ equals:
(a) 4/5
(b) 37/20
(c) 31/20
(d) 3/4

<details>
<summary>Solution</summary>
sin θ = 3/5 → opp = 3, hyp = 5, adj = 4
cos θ = 4/5, tan θ = 3/4
cos θ + tan θ = 4/5 + 3/4 = (16+15)/20 = 31/20
Answer: (c) 🟡
</details>

---

**Q2.** If 3 cot θ = 4, find (2 sin θ − 3 cos θ)/(2 sin θ + 3 cos θ).
(a) 1/3
(b) −1/3
(c) 1
(d) −1

<details>
<summary>Solution</summary>
cot θ = 4/3 → tan θ = 3/4 → sin θ = 3k, cos θ = 4k
(2(3k) − 3(4k))/(2(3k) + 3(4k)) = (6k − 12k)/(6k + 12k) = −6k/18k = −1/3
Answer: (b) 🟡 ⭐
</details>

---

**Q3.** If tan θ = a/b, then (a sin θ − b cos θ)/(a sin θ + b cos θ) equals:
(a) (a² − b²)/(a² + b²)
(b) (a² + b²)/(a² − b²)
(c) 1
(d) 0

<details>
<summary>Solution</summary>
tan θ = a/b → sin θ = a/√(a²+b²), cos θ = b/√(a²+b²)
a sin θ = a²/√(a²+b²), b cos θ = b²/√(a²+b²)
(a sin θ − b cos θ)/(a sin θ + b cos θ) = (a² − b²)/(a² + b²)
Answer: (a) 🔴
</details>

---

**Q4.** If sin θ + sin²θ = 1, then cos²θ + cos⁴θ equals:
(a) 2
(b) 1
(c) 0
(d) −1

<details>
<summary>Solution</summary>
sin θ + sin²θ = 1
sin θ = 1 − sin²θ = cos²θ
Now, cos²θ + cos⁴θ = sin θ + sin²θ = 1
Answer: (b) 🔴 ⭐
</details>

---

**Q5.** The value of (sin⁴θ + cos⁴θ) for an acute angle θ is always:
(a) = 1
(b) ≤ 1
(c) ≥ 1
(d) < 1

<details>
<summary>Solution</summary>
sin⁴θ + cos⁴θ = (sin²θ)² + (cos²θ)²
= (sin²θ + cos²θ)² − 2 sin²θ cos²θ
= 1 − 2 sin²θ cos²θ
Since sin²θ cos²θ ≥ 0, sin⁴θ + cos⁴θ ≤ 1
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin 30° = cos 60°.
**Reason (R):** sin(90° − θ) = cos θ.

<details>
<summary>Solution</summary>
Both A and R are true, and R correctly explains A.
Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** If tan θ = 1, then sec θ = √2.
**Reason (R):** sec²θ = 1 + tan²θ.

<details>
<summary>Solution</summary>
A is true: sec²θ = 1 + 1 = 2 → sec θ = √2 (θ acute)
R is true and correctly explains A.
Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** sin θ = 5/7 is possible for some acute angle θ.
**Reason (R):** For an acute angle, sin θ can be any value between 0 and 1.

<details>
<summary>Solution</summary>
A is true (since 5/7 < 1), R is true and explains A.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** If sec θ = 1/2 for some angle θ, then θ cannot be acute.
**Reason (R):** sec θ = 1/cos θ, and for acute angles, cos θ ≤ 1, so sec θ ≥ 1.

<details>
<summary>Solution</summary>
A is true: sec θ = 1/2 means cos θ = 2, impossible since cos ≤ 1.
R is true: for acute θ, 0 < cos θ ≤ 1, so sec θ ≥ 1.
R correctly explains A.
Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin θ in a right triangle equals:
   (a) opp/hyp   (b) adj/hyp   (c) opp/adj   (d) hyp/opp

2. 🟢 tan 30° equals:
   (a) 1/√3   (b) √3   (c) 1   (d) 0

3. 🟢 cot θ is the reciprocal of:
   (a) sin θ   (b) cos θ   (c) tan θ   (d) sec θ

4. 🟡 If sin θ = 4/5, cos θ = ?<br>
   (a) 3/5   (b) 5/4   (c) 4/3   (d) 3/4

5. 🟡 If tan θ = 1, then θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

6. 🟢 Which is true for any acute θ?<br>
   (a) sin θ > 1   (b) sin θ < 0   (c) 0 < sin θ < 1   (d) sin θ = 0

7. 🟡 If 2 sin θ = √3, then θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

8. 🟡 sin(90° − 30°) equals:
   (a) sin 30°   (b) cos 30°   (c) tan 30°   (d) 1

9. 🟢 Which identity is correct?<br>
   (a) sin²θ + cos²θ = 0   (b) sin²θ + cos²θ = 1   (c) sin²θ + cos²θ = −1   (d) sinθ + cosθ = 1

10. 🟡 If sec θ = 2, cos θ = ?<br>
    (a) 2   (b) 1/2   (c) 1   (d) √3

11. 🟡 In a 3-4-5 triangle, sin of the angle opposite side 3 is:
    (a) 3/5   (b) 4/5   (c) 3/4   (d) 4/3

12. 🟡 cos 45° equals:
    (a) 1/2   (b) 1/√2   (c) √3/2   (d) √3

13. 🟡 If tan θ = √3, θ = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 90°

14. 🟡 If sin θ = cos θ, then θ = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 0°

15. 🟢 cosec θ = ?<br>
    (a) 1/sin θ   (b) 1/cos θ   (c) 1/tan θ   (d) sin θ

16. 🟡 If 4 tan θ = 3, then sin θ = ?<br>
    (a) 3/5   (b) 4/5   (c) 3/4   (d) 5/3

17. 🟡 For acute θ, the minimum value of sin θ is:
    (a) 0   (b) 1   (c) −1   (d) 1/2

18. 🟡 sin²30° + cos²30° = ?<br>
    (a) 0   (b) 1/2   (c) 1   (d) 3/4

19. 🟡 If sin A = 3/5 and cos A = 4/5, then tan A = ?<br>
    (a) 3/4   (b) 4/3   (c) 5/3   (d) 5/4

20. 🟡 The value of sin 60° cos 30° + sin 30° cos 60° is:
    (a) 0   (b) 1/2   (c) 1   (d) √3/2

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | c | 11 | a | 16 | a |
| 2 | a | 7 | c | 12 | b | 17 | a |
| 3 | c | 8 | b | 13 | c | 18 | c |
| 4 | a | 9 | b | 14 | b | 19 | a |
| 5 | b | 10 | b | 15 | a | 20 | c |

</details>
