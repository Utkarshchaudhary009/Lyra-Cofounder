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
<details>
<summary>Solution</summary>

Let the angle opposite the side of length 5 be \(\theta\). 
- Opposite side (\(\text{opp}\)) = 5
- Since the right angle is between the sides of length 5 and 12, the adjacent side (\(\text{adj}\)) = 12
- Hypotenuse (\(\text{hyp}\)) = 13 (the longest side)

Now, we can find the six trigonometric ratios:
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{5}{13}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{12}{13}\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{5}{12}\)
- \(\text{cosec } \theta = \frac{\text{hyp}}{\text{opp}} = \frac{13}{5}\)
- \(\sec \theta = \frac{\text{hyp}}{\text{adj}} = \frac{13}{12}\)
- \(\cot \theta = \frac{\text{adj}}{\text{opp}} = \frac{12}{5}\)
</details>

2. 🟢 In ∆PQR, ∠Q = 90°, PQ = 7, QR = 24, PR = 25. Find sin P, cos P, tan P.
<details>
<summary>Solution</summary>

For angle \(P\):
- Opposite side is \(QR = 24\)
- Adjacent side is \(PQ = 7\)
- Hypotenuse is \(PR = 25\)

Using SOH CAH TOA:
- \(\sin P = \frac{\text{opp}}{\text{hyp}} = \frac{QR}{PR} = \frac{24}{25}\)
- \(\cos P = \frac{\text{adj}}{\text{hyp}} = \frac{PQ}{PR} = \frac{7}{25}\)
- \(\tan P = \frac{\text{opp}}{\text{adj}} = \frac{QR}{PQ} = \frac{24}{7}\)
</details>

3. 🟢 For the same triangle, find cosec R, sec R, cot R.
<details>
<summary>Solution</summary>

For angle \(R\):
- Opposite side is \(PQ = 7\)
- Adjacent side is \(QR = 24\)
- Hypotenuse is \(PR = 25\)

Using reciprocal ratios:
- \(\text{cosec } R = \frac{\text{hyp}}{\text{opp}} = \frac{PR}{PQ} = \frac{25}{7}\)
- \(\sec R = \frac{\text{hyp}}{\text{adj}} = \frac{PR}{QR} = \frac{25}{24}\)
- \(\cot R = \frac{\text{adj}}{\text{opp}} = \frac{QR}{PQ} = \frac{24}{7}\)
</details>

4. 🟡 In ∆XYZ, ∠Y = 90°, XY = a, YZ = b, XZ = c. Write all six ratios for ∠X.
<details>
<summary>Solution</summary>

For angle \(X\) in right-angled \(\Delta XYZ\):
- Opposite side (\(\text{opp}\)) = \(YZ = b\)
- Adjacent side (\(\text{adj}\)) = \(XY = a\)
- Hypotenuse (\(\text{hyp}\)) = \(XZ = c\)

The six ratios are:
- \(\sin X = \frac{\text{opp}}{\text{hyp}} = \frac{b}{c}\)
- \(\cos X = \frac{\text{adj}}{\text{hyp}} = \frac{a}{c}\)
- \(\tan X = \frac{\text{opp}}{\text{adj}} = \frac{b}{a}\)
- \(\text{cosec } X = \frac{\text{hyp}}{\text{opp}} = \frac{c}{b}\)
- \(\sec X = \frac{\text{hyp}}{\text{adj}} = \frac{c}{a}\)
- \(\cot X = \frac{\text{adj}}{\text{opp}} = \frac{a}{b}\)
</details>

5. 🟡 If sin θ = 3/5, can you find cos θ without a triangle?<br> What if θ is acute?<br>
<details>
<summary>Solution</summary>

Yes, we can find \(\cos \theta\) algebraically using the fundamental Pythagorean identity:
\[ \sin^2\theta + \cos^2\theta = 1 \]

Rearranging for \(\cos\theta\):
\[ \cos^2\theta = 1 - \sin^2\theta \]
\[ \cos\theta = \pm \sqrt{1 - \sin^2\theta} \]

Substituting \(\sin\theta = \frac{3}{5}\):
\[ \cos\theta = \pm \sqrt{1 - \left(\frac{3}{5}\right)^2} = \pm \sqrt{1 - \frac{9}{25}} = \pm \sqrt{\frac{16}{25}} = \pm \frac{4}{5} \]

If \(\theta\) is acute, it lies in the first quadrant where all basic trigonometric functions are positive. Therefore, we take the positive value:
\[ \cos\theta = \frac{4}{5} \]
</details>

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
<details>
<summary>Solution</summary>

Let \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{5}{13}\).
Since \(\theta\) is acute, we can construct a right triangle with:
- \(\text{Adjacent side} = 5\)
- \(\text{Hypotenuse} = 13\)

Using the Pythagorean theorem:
\[ \text{opp}^2 = \text{hyp}^2 - \text{adj}^2 = 13^2 - 5^2 = 169 - 25 = 144 \]
\[ \text{opp} = \sqrt{144} = 12 \]

Now we find the other ratios:
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{12}{13}\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{12}{5}\)
</details>

7. 🟡 If tan θ = 4/3, find sin θ and cos θ (θ acute).
<details>
<summary>Solution</summary>

Let \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{4}{3}\).
Since \(\theta\) is acute, we can construct a right triangle with:
- \(\text{Opposite side} = 4\)
- \(\text{Adjacent side} = 3\)

Using the Pythagorean theorem:
\[ \text{hyp}^2 = \text{opp}^2 + \text{adj}^2 = 4^2 + 3^2 = 16 + 9 = 25 \]
\[ \text{hyp} = \sqrt{25} = 5 \]

Now we find \(\sin\theta\) and \(\cos\theta\):
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{4}{5}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{3}{5}\)
</details>

8. 🟡 If cosec θ = √2, find cot θ and cos θ.
<details>
<summary>Solution</summary>

Given \(\text{cosec } \theta = \sqrt{2} = \frac{\sqrt{2}}{1}\).
Since \(\text{cosec } \theta = \frac{\text{hyp}}{\text{opp}}\), we can set:
- \(\text{Hypotenuse} = \sqrt{2}\)
- \(\text{Opposite side} = 1\)

Using the Pythagorean theorem:
\[ \text{adj}^2 = \text{hyp}^2 - \text{opp}^2 = (\sqrt{2})^2 - 1^2 = 2 - 1 = 1 \]
\[ \text{adj} = 1 \]

For an acute angle \(\theta\):
- \(\cot \theta = \frac{\text{adj}}{\text{opp}} = \frac{1}{1} = 1\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{1}{\sqrt{2}}\)
</details>

9. 🟡 If sec θ = 25/7, find tan θ and sin θ.
<details>
<summary>Solution</summary>

Given \(\sec \theta = \frac{25}{7}\).
Since \(\sec \theta = \frac{\text{hyp}}{\text{adj}}\), we set:
- \(\text{Hypotenuse} = 25\)
- \(\text{Adjacent side} = 7\)

Using the Pythagorean theorem:
\[ \text{opp}^2 = \text{hyp}^2 - \text{adj}^2 = 25^2 - 7^2 = 625 - 49 = 576 \]
\[ \text{opp} = \sqrt{576} = 24 \]

Now find the ratios:
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{24}{7}\)
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{24}{25}\)
</details>

10. 🔴 If cot θ = 1/√3, find sin θ + cos θ.
<details>
<summary>Solution</summary>

Given \(\cot \theta = \frac{1}{\sqrt{3}}\).
Since \(\cot \theta = \frac{\text{adj}}{\text{opp}}\), we set:
- \(\text{Adjacent side} = 1\)
- \(\text{Opposite side} = \sqrt{3}\)

Using the Pythagorean theorem:
\[ \text{hyp}^2 = \text{opp}^2 + \text{adj}^2 = (\sqrt{3})^2 + 1^2 = 3 + 1 = 4 \]
\[ \text{hyp} = \sqrt{4} = 2 \]

For an acute angle \(\theta\):
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{\sqrt{3}}{2}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{1}{2}\)

Thus:
\[ \sin \theta + \cos \theta = \frac{\sqrt{3}}{2} + \frac{1}{2} = \frac{\sqrt{3} + 1}{2} \]
</details>

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
<details>
<summary>Solution</summary>

For angle \(R\), the adjacent side is \(QR = 8\text{ cm}\) and the hypotenuse is \(PR\).
Given:
\[ \cos R = \frac{\text{adj}}{\text{hyp}} = \frac{QR}{PR} = \frac{4}{5} \]

Substitute \(QR = 8\):
\[ \frac{8}{PR} = \frac{4}{5} \implies PR = \frac{8 \times 5}{4} = 10\text{ cm} \]

Now use the Pythagorean theorem to find \(PQ\) (the opposite side):
\[ PQ^2 = PR^2 - QR^2 = 10^2 - 8^2 = 100 - 64 = 36 \]
\[ PQ = \sqrt{36} = 6\text{ cm} \]

Thus, \(PR = 10\text{ cm}\) and \(PQ = 6\text{ cm}\).
</details>

12. 🟡 If tan θ = 2 and the opposite side is 10 cm, find the adjacent and hypotenuse.
<details>
<summary>Solution</summary>

Given:
\[ \tan \theta = \frac{\text{opp}}{\text{adj}} = 2 \]

Substitute \(\text{opposite side} = 10\text{ cm}\):
\[ \frac{10}{\text{adj}} = 2 \implies \text{adj} = \frac{10}{2} = 5\text{ cm} \]

Now use the Pythagorean theorem to find the hypotenuse:
\[ \text{hyp}^2 = \text{opp}^2 + \text{adj}^2 = 10^2 + 5^2 = 100 + 25 = 125 \]
\[ \text{hyp} = \sqrt{125} = 5\sqrt{5}\text{ cm} \]

Thus, the adjacent side is \(5\text{ cm}\) and the hypotenuse is \(5\sqrt{5}\text{ cm}\).
</details>

13. 🟡 sin θ = 1/2 and hypotenuse = 20 cm. Find the other two sides.
<details>
<summary>Solution</summary>

Given:
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{1}{2} \]

Substitute \(\text{hypotenuse} = 20\text{ cm}\):
\[ \frac{\text{opp}}{20} = \frac{1}{2} \implies \text{opp} = 10\text{ cm} \]

Now use the Pythagorean theorem to find the adjacent side:
\[ \text{adj}^2 = \text{hyp}^2 - \text{opp}^2 = 20^2 - 10^2 = 400 - 100 = 300 \]
\[ \text{adj} = \sqrt{300} = 10\sqrt{3}\text{ cm} \]

Thus, the other two sides are \(10\text{ cm}\) (opposite) and \(10\sqrt{3}\text{ cm}\) (adjacent).
</details>

14. 🔴 cosec θ = 2 and adjacent side = 5√3 cm. Find the opposite and hypotenuse.
<details>
<summary>Solution</summary>

Given \(\text{cosec } \theta = 2 \implies \sin \theta = \frac{1}{2}\).
Let \(\text{opposite side} = x\) and \(\text{hypotenuse} = 2x\).

Given \(\text{adjacent side} = 5\sqrt{3}\text{ cm}\).
Using the Pythagorean theorem:
\[ \text{hyp}^2 = \text{opp}^2 + \text{adj}^2 \]
\[ (2x)^2 = x^2 + (5\sqrt{3})^2 \]
\[ 4x^2 = x^2 + 25 \times 3 \]
\[ 3x^2 = 75 \implies x^2 = 25 \implies x = 5\text{ (since side length is positive)} \]

Thus:
- \(\text{Opposite side} = 5\text{ cm}\)
- \(\text{Hypotenuse} = 2x = 10\text{ cm}\)
</details>

15. 🟡 In a right triangle, sec θ = √2 and adjacent side = 7 cm. Find the other sides.
<details>
<summary>Solution</summary>

Given:
\[ \sec \theta = \frac{\text{hyp}}{\text{adj}} = \sqrt{2} \]

Substitute \(\text{adjacent side} = 7\text{ cm}\):
\[ \frac{\text{hyp}}{7} = \sqrt{2} \implies \text{hyp} = 7\sqrt{2}\text{ cm} \]

Now use the Pythagorean theorem to find the opposite side:
\[ \text{opp}^2 = \text{hyp}^2 - \text{adj}^2 = (7\sqrt{2})^2 - 7^2 = 98 - 49 = 49 \]
\[ \text{opp} = \sqrt{49} = 7\text{ cm} \]

Thus, the other sides are the opposite side of length \(7\text{ cm}\) and the hypotenuse of length \(7\sqrt{2}\text{ cm}\).
</details>

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
<details>
<summary>Solution</summary>

Consider a right triangle with sides 5, 12, 13, where 13 is the hypotenuse. Let \(\theta\) be the angle opposite the side of length 5.
- \(\text{opp} = 5\)
- \(\text{adj} = 12\)
- \(\text{hyp} = 13\)

The ratios are:
\[ \sin \theta = \frac{5}{13}, \quad \cos \theta = \frac{12}{13} \]

Now calculate \(\sin^2\theta + \cos^2\theta\):
\[ \sin^2\theta + \cos^2\theta = \left(\frac{5}{13}\right)^2 + \left(\frac{12}{13}\right)^2 = \frac{25}{169} + \frac{144}{169} = \frac{169}{169} = 1 \]

Hence, \(\sin^2\theta + \cos^2\theta = 1\) is verified.
</details>

17. 🟢 Verify 1 + tan²θ = sec²θ for the same triangle.
<details>
<summary>Solution</summary>

Using the same 5-12-13 triangle and angle \(\theta\) opposite to side 5:
- \(\text{opp} = 5\), \(\text{adj} = 12\), \(\text{hyp} = 13\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{5}{12}\)
- \(\sec \theta = \frac{\text{hyp}}{\text{adj}} = \frac{13}{12}\)

Let's compute LHS and RHS:
- \(\text{LHS} = 1 + \tan^2\theta = 1 + \left(\frac{5}{12}\right)^2 = 1 + \frac{25}{144} = \frac{144 + 25}{144} = \frac{169}{144}\)
- \(\text{RHS} = \sec^2\theta = \left(\frac{13}{12}\right)^2 = \frac{169}{144}\)

Since \(\text{LHS} = \text{RHS} = \frac{169}{144}\), the identity is verified.
</details>

18. 🟡 Verify 1 + cot²θ = cosec²θ for an 8-15-17 triangle.
<details>
<summary>Solution</summary>

Consider a right triangle with sides 8, 15, 17, where 17 is the hypotenuse. Let \(\theta\) be the angle opposite to the side of length 8.
- \(\text{opp} = 8\), \(\text{adj} = 15\), \(\text{hyp} = 17\)
- \(\cot \theta = \frac{\text{adj}}{\text{opp}} = \frac{15}{8}\)
- \(\text{cosec } \theta = \frac{\text{hyp}}{\text{opp}} = \frac{17}{8}\)

Let's compute LHS and RHS:
- \(\text{LHS} = 1 + \cot^2\theta = 1 + \left(\frac{15}{8}\right)^2 = 1 + \frac{225}{64} = \frac{64 + 225}{64} = \frac{289}{64}\)
- \(\text{RHS} = \text{cosec}^2\theta = \left(\frac{17}{8}\right)^2 = \frac{289}{64}\)

Since \(\text{LHS} = \text{RHS} = \frac{289}{64}\), the identity is verified.
</details>

19. 🟡 If sin θ = a/c, cos θ = b/c, prove sin²θ + cos²θ = 1 using Pythagoras.
<details>
<summary>Solution</summary>

Let \(a\) be the side opposite to \(\theta\), \(b\) be the adjacent side, and \(c\) be the hypotenuse.
According to the Pythagorean theorem:
\[ a^2 + b^2 = c^2 \]

Now, substitute \(\sin \theta = \frac{a}{c}\) and \(\cos \theta = \frac{b}{c}\) into the expression:
\[ \sin^2\theta + \cos^2\theta = \left(\frac{a}{c}\right)^2 + \left(\frac{b}{c}\right)^2 \]
\[ = \frac{a^2}{c^2} + \frac{b^2}{c^2} \]
\[ = \frac{a^2 + b^2}{c^2} \]

Using the Pythagorean relation \(a^2 + b^2 = c^2\):
\[ \sin^2\theta + \cos^2\theta = \frac{c^2}{c^2} = 1 \]

Hence proved.
</details>

20. 🟡 If tan θ = 2, show that sin²θ + cos²θ = 1 using the triangle method.
<details>
<summary>Solution</summary>

Given \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{2}{1}\).
We can set:
- \(\text{Opposite side} = 2\)
- \(\text{Adjacent side} = 1\)

Using the Pythagorean theorem:
\[ \text{hyp}^2 = \text{opp}^2 + \text{adj}^2 = 2^2 + 1^2 = 4 + 1 = 5 \implies \text{hyp} = \sqrt{5} \]

Now find the ratios \(\sin\theta\) and \(\cos\theta\):
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{2}{\sqrt{5}} \]
\[ \cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{1}{\sqrt{5}} \]

Calculating \(\sin^2\theta + \cos^2\theta\):
\[ \sin^2\theta + \cos^2\theta = \left(\frac{2}{\sqrt{5}}\right)^2 + \left(\frac{1}{\sqrt{5}}\right)^2 = \frac{4}{5} + \frac{1}{5} = \frac{5}{5} = 1 \]

Hence shown.
</details>

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
<details>
<summary>Solution</summary>

We are given the equation:
\[ 5 \sin \theta = 12 \cos \theta \]

Divide both sides by \(5 \cos \theta\) (assuming \(\cos \theta \neq 0\)):
\[ \frac{\sin \theta}{\cos \theta} = \frac{12}{5} \]

Since \(\tan \theta = \frac{\sin \theta}{\cos \theta}\):
\[ \tan \theta = \frac{12}{5} \]
</details>

22. 🟡 If tan θ = √3, find (sin θ + cos θ)/(sin θ − cos θ).
<details>
<summary>Solution</summary>

We are looking for the value of:
\[ \frac{\sin \theta + \cos \theta}{\sin \theta - \cos \theta} \]

Divide both the numerator and the denominator by \(\cos \theta\):
\[ \frac{\frac{\sin \theta}{\cos \theta} + 1}{\frac{\sin \theta}{\cos \theta} - 1} = \frac{\tan \theta + 1}{\tan \theta - 1} \]

Substitute \(\tan \theta = \sqrt{3}\):
\[ \frac{\sqrt{3} + 1}{\sqrt{3} - 1} \]

Rationalize the denominator by multiplying the numerator and denominator by \((\sqrt{3} + 1)\):
\[ \frac{(\sqrt{3} + 1)^2}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{3 + 2\sqrt{3} + 1}{3 - 1} = \frac{4 + 2\sqrt{3}}{2} = 2 + \sqrt{3} \]
</details>

23. 🟡 If sec θ = 2, find (1 − sin θ)/(1 + sin θ).
<details>
<summary>Solution</summary>

Given \(\sec \theta = 2 \implies \cos \theta = \frac{1}{2}\).
For an acute angle \(\theta\), \(\cos \theta = \frac{1}{2}\) implies \(\theta = 60^\circ\).
Therefore:
\[ \sin \theta = \sin 60^\circ = \frac{\sqrt{3}}{2} \]

Now substitute \(\sin \theta\) into the expression:
\[ \frac{1 - \sin \theta}{1 + \sin \theta} = \frac{1 - \frac{\sqrt{3}}{2}}{1 + \frac{\sqrt{3}}{2}} = \frac{2 - \sqrt{3}}{2 + \sqrt{3}} \]

Rationalizing the denominator:
\[ \frac{(2 - \sqrt{3})^2}{(2 + \sqrt{3})(2 - \sqrt{3})} = \frac{4 - 4\sqrt{3} + 3}{4 - 3} = 7 - 4\sqrt{3} \]
</details>

24. 🔴 If 2 sin θ = 3 cos θ, find sin²θ + cos²θ. (Trick question?<br> Why?<br>)
<details>
<summary>Solution</summary>

Yes, this is a trick question. Regardless of the given relationship \(2\sin\theta = 3\cos\theta\), the fundamental Pythagorean identity holds for any angle \(\theta\):
\[ \sin^2\theta + \cos^2\theta = 1 \]

So no calculations of \(\sin\theta\) or \(\cos\theta\) are required. The answer is simply 1.
</details>

25. 🟡 If cot θ = 1, find sin θ cos θ.
<details>
<summary>Solution</summary>

Given \(\cot \theta = 1 \implies \tan \theta = 1\).
For an acute angle \(\theta\), \(\tan \theta = 1 \implies \theta = 45^\circ\).

Substitute \(\theta = 45^\circ\):
- \(\sin \theta = \sin 45^\circ = \frac{1}{\sqrt{2}}\)
- \(\cos \theta = \cos 45^\circ = \frac{1}{\sqrt{2}}\)

Thus:
\[ \sin \theta \cos \theta = \frac{1}{\sqrt{2}} \times \frac{1}{\sqrt{2}} = \frac{1}{2} \]
</details>

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
<details>
<summary>Solution</summary>

Using the complementary angle identity \(\sin \theta = \cos(90^\circ - \theta)\):
\[ \sin 45^\circ = \cos(90^\circ - 45^\circ) = \cos 45^\circ = \frac{1}{\sqrt{2}} \]
</details>

27. 🟢 If tan 60° = √3, find cot 30°.
<details>
<summary>Solution</summary>

Using the complementary relationship \(\cot \theta = \tan(90^\circ - \theta)\):
\[ \cot 30^\circ = \tan(90^\circ - 30^\circ) = \tan 60^\circ = \sqrt{3} \]
</details>

28. 🟡 Prove that sin(90° − θ) = cos θ using a right triangle.
<details>
<summary>Solution</summary>

Consider a right-angled triangle \(ABC\) with \(\angle B = 90^\circ\).
Let \(\angle C = \theta\). Since the sum of angles in a triangle is \(180^\circ\), the other acute angle is:
\[ \angle A = 90^\circ - \theta \]

With respect to \(\angle C = \theta\):
- Adjacent side (\(\text{adj}\)) = \(BC\)
- Hypotenuse (\(\text{hyp}\)) = \(AC\)
\[ \cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{BC}{AC} \]

With respect to \(\angle A = 90^\circ - \theta\):
- Opposite side (\(\text{opp}\)) = \(BC\)
- Hypotenuse (\(\text{hyp}\)) = \(AC\)
\[ \sin(90^\circ - \theta) = \frac{\text{opp}}{\text{hyp}} = \frac{BC}{AC} \]

Comparing the two equations:
\[ \sin(90^\circ - \theta) = \cos \theta \]
Hence proved.
</details>

29. 🟡 If sec θ = cosec 60°, find θ.
<details>
<summary>Solution</summary>

Using the complementary relationship \(\sec \theta = \text{cosec}(90^\circ - \theta)\):
\[ \text{cosec}(90^\circ - \theta) = \text{cosec } 60^\circ \]

For acute angle \(\theta\):
\[ 90^\circ - \theta = 60^\circ \implies \theta = 30^\circ \]
</details>

30. 🟡 If sin 2θ = cos 3θ, find θ (both acute).
<details>
<summary>Solution</summary>

Using the complementary relationship \(\cos 3\theta = \sin(90^\circ - 3\theta)\):
\[ \sin 2\theta = \sin(90^\circ - 3\theta) \]

Since \(2\theta\) and \(90^\circ - 3\theta\) are acute angles:
\[ 2\theta = 90^\circ - 3\theta \]
\[ 5\theta = 90^\circ \implies \theta = 18^\circ \]
</details>

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
<details>
<summary>Solution</summary>

Let the right triangle have sides \(3x\), \(4x\), and \(5x\). The hypotenuse is the longest side, \(5x\).
Let the acute angles be:
- \(\alpha\) (opposite the side of length \(3x\))
- \(\beta\) (opposite the side of length \(4x\))

For angle \(\alpha\):
- \(\text{opp} = 3x\), \(\text{adj} = 4x\), \(\text{hyp} = 5x\)
- \(\sin \alpha = \frac{3}{5}\)
- \(\cos \alpha = \frac{4}{5}\)
- \(\tan \alpha = \frac{3}{4}\)
- \(\text{cosec } \alpha = \frac{5}{3}\)
- \(\sec \alpha = \frac{5}{4}\)
- \(\cot \alpha = \frac{4}{3}\)

For angle \(\beta\):
- \(\text{opp} = 4x\), \(\text{adj} = 3x\), \(\text{hyp} = 5x\)
- \(\sin \beta = \frac{4}{5}\)
- \(\cos \beta = \frac{3}{5}\)
- \(\tan \beta = \frac{4}{3}\)
- \(\text{cosec } \beta = \frac{5}{4}\)
- \(\sec \beta = \frac{5}{3}\)
- \(\cot \beta = \frac{3}{4}\)
</details>

32. 🟡 Sides in ratio 7 : 24 : 25. Find tan of the smaller acute angle.
<details>
<summary>Solution</summary>

The smaller angle is always opposite the smaller side. Here, the sides are in the ratio 7 : 24 : 25.
The smallest side corresponds to the ratio value 7. Let \(\theta\) be the angle opposite to this side.
- \(\text{opp} = 7x\)
- \(\text{adj} = 24x\)
- \(\text{hyp} = 25x\)

Thus:
\[ \tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{7x}{24x} = \frac{7}{24} \]
</details>

33. 🟡 Sides in ratio 8 : 15 : 17. Find sec and cosec of the larger acute angle.
<details>
<summary>Solution</summary>

The larger acute angle is opposite the larger leg (which is \(15x\) since \(15 > 8\)). Let this angle be \(\phi\).
- \(\text{opp} = 15x\)
- \(\text{adj} = 8x\)
- \(\text{hyp} = 17x\)

Thus:
- \(\sec \phi = \frac{\text{hyp}}{\text{adj}} = \frac{17x}{8x} = \frac{17}{8}\)
- \(\text{cosec } \phi = \frac{\text{hyp}}{\text{opp}} = \frac{17x}{15x} = \frac{17}{15}\)
</details>

34. 🔴 The legs of a right triangle are in ratio 1 : √3. Find the acute angles.
<details>
<summary>Solution</summary>

Let the legs of the right triangle be \(x\) and \(\sqrt{3}x\).
Let \(\theta\) be the angle opposite the shorter leg \(x\).
\[ \tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{x}{\sqrt{3}x} = \frac{1}{\sqrt{3}} \]

Since \(\theta\) is an acute angle:
\[ \theta = 30^\circ \]

The other acute angle is the complement:
\[ 90^\circ - \theta = 90^\circ - 30^\circ = 60^\circ \]

The acute angles are \(30^\circ\) and \(60^\circ\).
</details>

35. 🔴 ⭐ If the sides of a right triangle are in AP (arithmetic progression), find the ratio of its sides.
<details>
<summary>Solution</summary>

Let the sides of the right triangle in arithmetic progression (AP) be \(a - d\), \(a\), and \(a + d\) where \(a > 0\) and \(d \ge 0\).
The hypotenuse is the longest side, which is \(a + d\).

By the Pythagorean theorem:
\[ (a - d)^2 + a^2 = (a + d)^2 \]
\[ a^2 - 2ad + d^2 + a^2 = a^2 + 2ad + d^2 \]
\[ a^2 - 4ad = 0 \]
\[ a(a - 4d) = 0 \]

Since the side length \(a\) must be positive (\(a > 0\)):
\[ a = 4d \]

Substituting \(a = 4d\) back into the expressions for the sides:
- First leg: \(a - d = 4d - d = 3d\)
- Second leg: \(a = 4d\)
- Hypotenuse: \(a + d = 4d + d = 5d\)

Therefore, the ratio of the sides is:
\[ 3d : 4d : 5d = 3 : 4 : 5 \]
</details>

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
<details>
<summary>Solution</summary>

Let \(\theta\) be the angle the ramp makes with the ground.
- The ramp itself is the hypotenuse: \(\text{hyp} = 5\text{ m}\).
- The height is the opposite side: \(\text{opp} = 3\text{ m}\).

Using the Pythagorean theorem, the adjacent side (horizontal base) is:
\[ \text{adj} = \sqrt{\text{hyp}^2 - \text{opp}^2} = \sqrt{5^2 - 3^2} = 4\text{ m} \]

Now compute the ratios:
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{3}{5}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{4}{5}\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{3}{4}\)
</details>

37. 🟡 A guy wire 13 m long from the top of a pole to a peg on the ground is at an angle θ with the pole. If the peg is 5 m from the foot of the pole, find sin θ.
<details>
<summary>Solution</summary>

Let the vertical pole and ground form a right triangle where the guy wire is the hypotenuse: \(\text{hyp} = 13\text{ m}\).
The angle \(\theta\) is formed with the *pole*, meaning the pole is the adjacent side and the ground is the opposite side.
The peg is at the opposite side: \(\text{opp} = 5\text{ m}\).

By definition:
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{5}{13} \]
</details>

38. 🔴 ⭐ From the top of a 20 m building, the angle of depression of a car is θ where tan θ = 4/3. Find the distance of the car from the building.
<details>
<summary>Solution</summary>

Let the height of the building be \(\text{opp} = 20\text{ m}\).
By alternate interior angles, the angle of elevation from the car to the top of the building is also \(\theta\).
Let the distance from the car to the building be \(x\text{ (adjacent side)}\).

Given:
\[ \tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{20}{x} = \frac{4}{3} \]

Solving for \(x\):
\[ 4x = 60 \implies x = 15\text{ m} \]

Thus, the distance of the car from the building is \(15\text{ m}\).
</details>

39. 🔴 A kite flying at a height of 60 m has a string of length 100 m at an angle θ with the horizontal. Find sin θ and cos θ.
<details>
<summary>Solution</summary>

- Height of the kite (opposite side) = \(60\text{ m}\)
- Length of the string (hypotenuse) = \(100\text{ m}\)
- Angle with the horizontal = \(\theta\)

Using the Pythagorean theorem, the adjacent side (horizontal distance) is:
\[ \text{adj} = \sqrt{\text{hyp}^2 - \text{opp}^2} = \sqrt{100^2 - 60^2} = \sqrt{10000 - 3600} = \sqrt{6400} = 80\text{ m} \]

Now compute the ratios:
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{60}{100} = \frac{3}{5}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{80}{100} = \frac{4}{5}\)
</details>

40. 🟡 A river is crossed by a bridge of length 50 m at an angle θ to the bank. If the width of the river is 30 m, find sin θ.
<details>
<summary>Solution</summary>

The width of the river represents the perpendicular distance between the banks, which is the side opposite to the angle \(\theta\):
- \(\text{opp} = 30\text{ m}\)
- The length of the bridge is the hypotenuse: \(\text{hyp} = 50\text{ m}\)

Therefore:
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{30}{50} = \frac{3}{5} \]
</details>

---

## Stage 4: Type Mixer

1. 🟡 If sin θ = 5/13, find cos θ and tan θ. Then find sin(90° − θ).
<details>
<summary>Solution</summary>

Given \(\sin \theta = \frac{5}{13} = \frac{\text{opp}}{\text{hyp}}\).
Construct a right triangle with opposite side = 5 and hypotenuse = 13.
Using the Pythagorean theorem:
\[ \text{adj} = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = 12 \]

Now calculate:
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{12}{13}\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{5}{12}\)

For \(\sin(90^\circ - \theta)\), we use the complementary angle identity:
\[ \sin(90^\circ - \theta) = \cos \theta = \frac{12}{13} \]
</details>

2. 🟡 In a right triangle, tan θ = 3/4 and hypotenuse = 15. Find all sides and all six ratios for θ.
<details>
<summary>Solution</summary>

Given \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{3}{4}\).
Let \(\text{opp} = 3k\) and \(\text{adj} = 4k\).
By the Pythagorean theorem:
\[ \text{hyp} = \sqrt{(3k)^2 + (4k)^2} = 5k \]

Since the hypotenuse is 15:
\[ 5k = 15 \implies k = 3 \]

Now calculate the side lengths:
- \(\text{Opposite side} = 3(3) = 9\)
- \(\text{Adjacent side} = 4(3) = 12\)
- \(\text{Hypotenuse} = 15\)

The six ratios for \(\theta\) are:
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{9}{15} = \frac{3}{5}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{12}{15} = \frac{4}{5}\)
- \(\tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{9}{12} = \frac{3}{4}\)
- \(\text{cosec } \theta = \frac{\text{hyp}}{\text{opp}} = \frac{15}{9} = \frac{5}{3}\)
- \(\sec \theta = \frac{\text{hyp}}{\text{adj}} = \frac{15}{12} = \frac{5}{4}\)
- \(\cot \theta = \frac{\text{adj}}{\text{opp}} = \frac{12}{9} = \frac{4}{3}\)
</details>

3. 🔴 If 7 sin²θ + 3 cos²θ = 4, find tan θ.
<details>
<summary>Solution</summary>

Given equation:
\[ 7 \sin^2\theta + 3 \cos^2\theta = 4 \]

We split \(7\sin^2\theta\) into \(4\sin^2\theta + 3\sin^2\theta\):
\[ 4 \sin^2\theta + 3 \sin^2\theta + 3 \cos^2\theta = 4 \]
\[ 4 \sin^2\theta + 3(\sin^2\theta + \cos^2\theta) = 4 \]

Since \(\sin^2\theta + \cos^2\theta = 1\):
\[ 4 \sin^2\theta + 3(1) = 4 \]
\[ 4 \sin^2\theta = 1 \implies \sin^2\theta = \frac{1}{4} \implies \sin \theta = \pm\frac{1}{2} \]

Assuming \(\theta\) is acute:
\[ \sin \theta = \frac{1}{2} \implies \theta = 30^\circ \]

Thus:
\[ \tan \theta = \tan 30^\circ = \frac{1}{\sqrt{3}} \]
*(If \(\theta\) can be in any quadrant, \(\tan\theta = \pm \frac{1}{\sqrt{3}}\).)*
</details>

4. 🔴 ⭐ In a right triangle, the sides are in the ratio 1 : 2 : √5. Find sin θ and cos θ for the smallest angle. Also verify sin²θ + cos²θ = 1.
<details>
<summary>Solution</summary>

Let the sides be \(x\), \(2x\), and \(\sqrt{5}x\). Since \(\sqrt{5} \approx 2.236\), the longest side is \(\sqrt{5}x\), which is the hypotenuse.
The smallest angle \(\theta\) is opposite the shortest side, \(x\).
- \(\text{opp} = x\)
- \(\text{adj} = 2x\)
- \(\text{hyp} = \sqrt{5}x\)

Calculate \(\sin\theta\) and \(\cos\theta\):
- \(\sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{x}{\sqrt{5}x} = \frac{1}{\sqrt{5}}\)
- \(\cos \theta = \frac{\text{adj}}{\text{hyp}} = \frac{2x}{\sqrt{5}x} = \frac{2}{\sqrt{5}}\)

Verify the identity:
\[ \sin^2\theta + \cos^2\theta = \left(\frac{1}{\sqrt{5}}\right)^2 + \left(\frac{2}{\sqrt{5}}\right)^2 = \frac{1}{5} + \frac{4}{5} = \frac{5}{5} = 1 \]

Hence verified.
</details>

5. 🟡 A vertical pole of height h casts a shadow of length 2h. Find the angle of elevation of the sun.
<details>
<summary>Solution</summary>

Let \(\theta\) be the angle of elevation of the sun.
The pole is vertical, forming the opposite side of length \(h\).
The shadow is cast on the ground, forming the adjacent side of length \(2h\).

Using the tangent ratio:
\[ \tan \theta = \frac{\text{opp}}{\text{adj}} = \frac{h}{2h} = \frac{1}{2} \]

Thus, the angle of elevation is:
\[ \theta = \tan^{-1}\left(\frac{1}{2}\right) \approx 26.57^\circ \]
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 In ∆ABC, ∠B = 90°, AB = 6, BC = 8. Find sin A, cos A, and tan A. **(2 marks)**

<details>
<summary>Solution</summary>

```
AC = √(6² + 8²) = 10
sin A = BC/AC = 8/10 = 4/5
cos A = AB/AC = 6/10 = 3/5
tan A = BC/AB = 8/6 = 4/3
```
</details>

---

**Q2.** 🟡 If sec θ = 13/5, find the values of other trig ratios. **(3 marks)**

<details>
<summary>Solution</summary>

```
sec θ = hyp/adj = 13/5
Let hyp = 13k, adj = 5k
opp² = 169k² − 25k² = 144k²
opp = 12k

sin θ = 12/13, cos θ = 5/13, tan θ = 12/5
cosec θ = 13/12, cot θ = 5/12
```
</details>

---

**Q3.** 🟡 If tan θ = 4/3, find the value of (sin θ − cos θ)/(sin θ + cos θ). **(3 marks)**

<details>
<summary>Solution</summary>

```
tan θ = 4/3 → sin θ = 4k, cos θ = 3k (by triangle method)
(sin θ − cos θ)/(sin θ + cos θ) = (4k − 3k)/(4k + 3k) = k/7k = 1/7
```
</details>

---

**Q4.** 🟡 If sin θ = 3/5, find tan θ and sec θ. Also verify sec²θ − tan²θ = 1. **(3 marks)**

<details>
<summary>Solution</summary>

```
sin θ = 3/5 → opp = 3, hyp = 5, adj = 4
tan θ = 3/4, sec θ = 5/4
sec²θ − tan²θ = 25/16 − 9/16 = 16/16 = 1 ✓
```
</details>

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
<details>
<summary>Solution</summary>

By definition, in a right-angled triangle, the sine of an angle \(\theta\) is the ratio of the side opposite to the angle to the hypotenuse:
\[ \sin \theta = \frac{\text{opposite}}{\text{hypotenuse}} \]

**Answer: (a) opp/hyp**
</details>

2. 🟢 tan 30° equals:
   (a) 1/√3   (b) √3   (c) 1   (d) 0
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \tan 30^\circ = \frac{1}{\sqrt{3}} \]

**Answer: (a) 1/√3**
</details>

3. 🟢 cot θ is the reciprocal of:
   (a) sin θ   (b) cos θ   (c) tan θ   (d) sec θ
<details>
<summary>Solution</summary>

By the reciprocal identities:
\[ \cot \theta = \frac{1}{\tan \theta} \]
Therefore, cotangent is the reciprocal of tangent.

**Answer: (c) tan θ**
</details>

4. 🟡 If sin θ = 4/5, cos θ = ?<br>
   (a) 3/5   (b) 5/4   (c) 4/3   (d) 3/4
<details>
<summary>Solution</summary>

Using the identity \(\sin^2\theta + \cos^2\theta = 1\):
\[ \cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{4}{5}\right)^2 = 1 - \frac{16}{25} = \frac{9}{25} \]

For acute angle \(\theta\):
\[ \cos \theta = \frac{3}{5} \]

**Answer: (a) 3/5**
</details>

5. 🟡 If tan θ = 1, then θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

From the standard values of tangent:
\[ \tan 45^\circ = 1 \implies \theta = 45^\circ \]

**Answer: (b) 45°**
</details>

6. 🟢 Which is true for any acute θ?<br>
   (a) sin θ > 1   (b) sin θ < 0   (c) 0 < sin θ < 1   (d) sin θ = 0
<details>
<summary>Solution</summary>

For any acute angle \(\theta\) (where \(0^\circ < \theta < 90^\circ\)), the opposite side is always positive and strictly less than the hypotenuse. Thus, the ratio lies between 0 and 1:
\[ 0 < \sin \theta < 1 \]

**Answer: (c) 0 < sin θ < 1**
</details>

7. 🟡 If 2 sin θ = √3, then θ = ?<br>
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Given:
\[ 2 \sin \theta = \sqrt{3} \implies \sin \theta = \frac{\sqrt{3}}{2} \]

For an acute angle \(\theta\):
\[ \theta = 60^\circ \]

**Answer: (c) 60°**
</details>

8. 🟡 sin(90° − 30°) equals:
   (a) sin 30°   (b) cos 30°   (c) tan 30°   (d) 1
<details>
<summary>Solution</summary>

Using the complementary angle identity \(\sin(90^\circ - \theta) = \cos \theta\):
\[ \sin(90^\circ - 30^\circ) = \cos 30^\circ \]

**Answer: (b) cos 30°**
</details>

9. 🟢 Which identity is correct?<br>
   (a) sin²θ + cos²θ = 0   (b) sin²θ + cos²θ = 1   (c) sin²θ + cos²θ = −1   (d) sinθ + cosθ = 1
<details>
<summary>Solution</summary>

The fundamental Pythagorean identity is:
\[ \sin^2\theta + \cos^2\theta = 1 \]

**Answer: (b) sin²θ + cos²θ = 1**
</details>

10. 🟡 If sec θ = 2, cos θ = ?<br>
    (a) 2   (b) 1/2   (c) 1   (d) √3
<details>
<summary>Solution</summary>

Since cosine is the reciprocal of secant:
\[ \cos \theta = \frac{1}{\sec \theta} = \frac{1}{2} \]

**Answer: (b) 1/2**
</details>

11. 🟡 In a 3-4-5 triangle, sin of the angle opposite side 3 is:
    (a) 3/5   (b) 4/5   (c) 3/4   (d) 4/3
<details>
<summary>Solution</summary>

In a 3-4-5 triangle, the hypotenuse is 5 (longest side).
Let \(\theta\) be the angle opposite the side of length 3:
- \(\text{opp} = 3\)
- \(\text{hyp} = 5\)
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{3}{5} \]

**Answer: (a) 3/5**
</details>

12. 🟡 cos 45° equals:
    (a) 1/2   (b) 1/√2   (c) √3/2   (d) √3
<details>
<summary>Solution</summary>

From the standard trigonometric table:
\[ \cos 45^\circ = \frac{1}{\sqrt{2}} \]

**Answer: (b) 1/√2**
</details>

13. 🟡 If tan θ = √3, θ = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

From the standard trigonometric table for tangent:
\[ \tan 60^\circ = \sqrt{3} \implies \theta = 60^\circ \]

**Answer: (c) 60°**
</details>

14. 🟡 If sin θ = cos θ, then θ = ?<br>
    (a) 30°   (b) 45°   (c) 60°   (d) 0°
<details>
<summary>Solution</summary>

Given \(\sin \theta = \cos \theta\). Divide by \(\cos\theta\):
\[ \tan \theta = 1 \]

For an acute angle \(\theta\):
\[ \theta = 45^\circ \]

**Answer: (b) 45°**
</details>

15. 🟢 cosec θ = ?<br>
    (a) 1/sin θ   (b) 1/cos θ   (c) 1/tan θ   (d) sin θ
<details>
<summary>Solution</summary>

By the reciprocal identity, cosecant is the reciprocal of sine:
\[ \text{cosec } \theta = \frac{1}{\sin \theta} \]

**Answer: (a) 1/sin θ**
</details>

16. 🟡 If 4 tan θ = 3, then sin θ = ?<br>
    (a) 3/5   (b) 4/5   (c) 3/4   (d) 5/3
<details>
<summary>Solution</summary>

Given:
\[ 4 \tan \theta = 3 \implies \tan \theta = \frac{3}{4} = \frac{\text{opp}}{\text{adj}} \]

Let \(\text{opp} = 3\) and \(\text{adj} = 4\). Then:
\[ \text{hyp} = \sqrt{3^2 + 4^2} = 5 \]

Hence:
\[ \sin \theta = \frac{\text{opp}}{\text{hyp}} = \frac{3}{5} \]

**Answer: (a) 3/5**
</details>

17. 🟡 For acute θ, the minimum value of sin θ is:
    (a) 0   (b) 1   (c) −1   (d) 1/2
<details>
<summary>Solution</summary>

For acute angles \(0^\circ < \theta < 90^\circ\), the value of \(\sin \theta\) ranges between 0 and 1. Taking the lower limit as \(\theta \to 0^\circ\), the minimum value of \(\sin \theta\) is 0.

**Answer: (a) 0**
</details>

18. 🟡 sin²30° + cos²30° = ?<br>
    (a) 0   (b) 1/2   (c) 1   (d) 3/4
<details>
<summary>Solution</summary>

By the Pythagorean identity \(\sin^2\theta + \cos^2\theta = 1\), for any angle \(\theta\):
\[ \sin^2 30^\circ + \cos^2 30^\circ = 1 \]

**Answer: (c) 1**
</details>

19. 🟡 If sin A = 3/5 and cos A = 4/5, then tan A = ?<br>
    (a) 3/4   (b) 4/3   (c) 5/3   (d) 5/4
<details>
<summary>Solution</summary>

Using the quotient identity:
\[ \tan A = \frac{\sin A}{\cos A} = \frac{3/5}{4/5} = \frac{3}{4} \]

**Answer: (a) 3/4**
</details>

20. 🟡 The value of sin 60° cos 30° + sin 30° cos 60° is:
    (a) 0   (b) 1/2   (c) 1   (d) √3/2
<details>
<summary>Solution</summary>

Substitute the standard trigonometric values:
- \(\sin 60^\circ = \frac{\sqrt{3}}{2}\)
- \(\cos 30^\circ = \frac{\sqrt{3}}{2}\)
- \(\sin 30^\circ = \frac{1}{2}\)
- \(\cos 60^\circ = \frac{1}{2}\)

Calculate the expression:
\[ \sin 60^\circ \cos 30^\circ + \sin 30^\circ \cos 60^\circ = \left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) \]
\[ = \frac{3}{4} + \frac{1}{4} = 1 \]

*(Note: We can also use the angle sum formula \(\sin(A+B) = \sin A\cos B + \cos A\sin B\), which gives \(\sin(60^\circ + 30^\circ) = \sin 90^\circ = 1\).)*

**Answer: (c) 1**
</details>

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
