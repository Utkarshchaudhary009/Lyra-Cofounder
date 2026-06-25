# Chapter 1: What Is Trigonometry?<br>

---

## Stage 1: The Core Idea

### The Problem That Started It All

Imagine you're an ancient Egyptian surveyor, standing at the edge of the Nile. On the other side stands a great pyramid. You need to know its height — but you cannot cross the river, let alone climb it with a measuring rope.

What do you do?<br>

You measure the **shadow**.

![img](https://via.placeholder.com/400x200?<br>text=Pyramid+shadow+triangle)

At a certain time of day, you measure:
- The length of the pyramid's shadow = 200 cubits
- The angle of the sun above the horizon = 42°

If you know how **angles and sides** of a triangle are related, you can compute the pyramid's height *without ever touching it*.

That's trigonometry. The word comes from Greek: **trigonon** (triangle) + **metron** (measure). It's the art of finding what you cannot measure directly, using what you *can* measure.

### What Trigonometry Really Is

Trigonometry answers three types of questions:

| Question Type | Example |
|--------------|---------|
| Given an angle, what's the ratio of sides?<br> | What is sin 30°?<br> |
| Given side ratios, what's the angle?<br> | If sin θ = 0.5, what is θ?<br> |
| Given some sides and angles, what are the rest?<br> | Find the height of that pyramid |

The entire subject is built on **one key idea**: in similar right triangles, the ratios of sides are constant for a given angle.

```
      ┌───┐
      │   │
      │   │
   opp│   │hyp
      │   │
      │   │
      └───┘
        adj

For a fixed angle θ:
   opp/hyp  is always the same number (call it sin θ)
   adj/hyp  is always the same number (call it cos θ)
   opp/adj  is always the same number (call it tan θ)
```

This single insight lets you measure mountains, navigate ships, design bridges, model sound waves, and even describe the orbit of planets.

### The Big Picture

Here's how this book will take you from zero to JEE-level mastery:

```
Part I (Class 10):  Right triangles → Ratios → Identities → Heights & Distances
                       ↓
Part II (Class 11):  Unit circle → All angles → Compound formulas → Equations
                       ↓
Part III (Class 12): Inverse trig → Properties → Composition
                       ↓
Part IV (JEE+):      Max/Min → Inequalities → Triangles → Series → Calculus
```

Right now, you're at the very start. You don't need to know any formulas yet. You just need to understand **one thing**:

> Trigonometry is the study of relationships between angles and side-ratios in triangles. Once you learn these relationships, you can solve problems that seem impossible at first glance.

---

## Stage 2: The Formula Lab

There are no new formulas in this chapter. But there's one essential tool you need to dust off before we begin.

### Pythagoras Theorem — The Foundation

In any right triangle:

```
        ┌───┐
     a  │   │  c
        │   │
        └───┘
           b

a² + b² = c²
```

Where **c** is always the **hypotenuse** (the side opposite the right angle).

**Trap to avoid:** The hypotenuse is ALWAYS the longest side. ALWAYS opposite the right angle. Students often mix up which side is c.

### Triangle Terminology

Before ratios make sense, you need to name the sides correctly relative to a given angle:

```
        ┌───┐
        │   │
opposite│   │ hypotenuse
        │   │
        └───┘
         adjacent

For angle θ (at the bottom-left corner):
  • Hypotenuse  = longest side (always opposite 90°)
  • Opposite    = side facing θ
  • Adjacent    = side next to θ (not the hypotenuse)
```

**Memory trick:** The opposite side is *across from* the angle. The adjacent side is *touching* the angle.

---

## Stage 3: Type-wise Mastery

### Type 1: Identifying Sides of a Right Triangle

**Goal:** Given a right triangle and a marked angle, correctly label opposite, adjacent, and hypotenuse.

**Solved Example:**

```
        A
        ┌───┐
        │   │
        │   │
        └───┘
     B      C
Angle marked at B

Identify the three sides relative to angle B.
```

**Solution:**
- Hypotenuse = AC (longest side, opposite the right angle at A)
- Opposite = AC (wait — this conflicts!)

Let me be clearer. Label vertices:

```
        A
        ┌───┐
        │   │
        │   │
     B  └───┘  C
```

Angle at B. Right angle at A.
- Hypotenuse = BC (opposite 90° at A)
- Opposite = AC (facing angle B)
- Adjacent = AB (touching angle B)

---

**Practice Problems:**

1. 🟢 
```
        P
        ┌───┐
        │   │
        │   │
     Q  └───┘  R
Angle at Q. Right angle at P.
Label the sides.
```
<details>
<summary>Solution</summary>

1. **Hypotenuse**: The hypotenuse is the side opposite the right angle. Here, the right angle is at vertex \( P \), so the side opposite to it is \( QR \).
2. **Opposite**: The opposite side is the side facing the marked angle. The marked angle is at vertex \( Q \), so the side opposite to it is \( PR \).
3. **Adjacent**: The adjacent side is the side next to the marked angle (other than the hypotenuse). The marked angle is at vertex \( Q \), so the adjacent side is \( PQ \).
</details>

2. 🟢
```
    X───┐
    │   │
    │   │
    └───┘
    Y   Z
Angle at Z. Right angle at Y.
Label the sides.
```
<details>
<summary>Solution</summary>

1. **Hypotenuse**: The hypotenuse is the side opposite the right angle. Here, the right angle is at vertex \( Y \), so the side opposite to it is \( XZ \).
2. **Opposite**: The opposite side is the side facing the marked angle. The marked angle is at vertex \( Z \), so the side opposite to it is \( XY \).
3. **Adjacent**: The adjacent side is the side next to the marked angle (other than the hypotenuse). The marked angle is at vertex \( Z \), so the adjacent side is \( YZ \).
</details>

3. 🟢 Draw any right triangle. Mark an acute angle. Label all three sides.
<details>
<summary>Solution</summary>

Let us draw a right-angled triangle \( \triangle ABC \) with:
- Right angle at vertex \( B \) (\( \angle B = 90^\circ \))
- Marked acute angle at vertex \( A \) (\( \angle A = \theta \))

Then, the sides are defined as follows:
- **Hypotenuse**: Side opposite the right angle \( \angle B \), which is \( AC \).
- **Opposite side relative to \( \theta \)**: Side facing \( \angle A \), which is \( BC \).
- **Adjacent side relative to \( \theta \)**: Side next to \( \angle A \) (excluding the hypotenuse), which is \( AB \).
</details>

4. 🟢 In a right triangle with vertices P, Q, R where ∠Q = 90° and angle is marked at P, which side is the opposite?<br>
<details>
<summary>Solution</summary>

In a right triangle \( \triangle PQR \):
- The right angle is at vertex \( Q \) (\( \angle Q = 90^\circ \)).
- The marked angle is at vertex \( P \).
- The opposite side is the side facing the marked angle. The side directly opposite to vertex \( P \) in \( \triangle PQR \) is \( QR \).

Therefore, the opposite side is **\( QR \)**.
</details>

5. 🟢 True or False: The adjacent side is always the shortest side.
<details>
<summary>Solution</summary>

**False.**
The adjacent side is not necessarily the shortest side. The relative lengths of the two legs (opposite and adjacent) depend entirely on the measure of the acute angle:
- If the marked angle is less than \( 45^\circ \), the opposite side is shorter than the adjacent side (so the adjacent side is longer).
- If the marked angle is greater than \( 45^\circ \), the opposite side is longer than the adjacent side (so the adjacent side is shorter).
- For example, in a \( 3 \text{ cm} - 4 \text{ cm} - 5 \text{ cm} \) right triangle, if the angle next to the \( 4\text{ cm} \) side is marked, the adjacent side is \( 4\text{ cm} \) and the opposite side is \( 3\text{ cm} \). Here, the adjacent side is longer than the opposite side.
</details>

---

### Type 2: Applying Pythagoras Theorem

**Goal:** Given two sides of a right triangle, find the third.

**Solved Example:**

A right triangle has legs of length 3 cm and 4 cm. Find the hypotenuse.

**Solution:**
```
a² + b² = c²
3² + 4² = c²
9 + 16 = c²
25 = c²
c = 5 cm
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

6. 🟢 ⭐ Find the hypotenuse when legs are 5 and 12.
<details>
<summary>Solution</summary>

Let the legs of the right triangle be \( a = 5 \) and \( b = 12 \).
Let the hypotenuse be \( c \).
According to the Pythagoras theorem:
\[
c^2 = a^2 + b^2
\]
Substituting the given values:
\[
c^2 = 5^2 + 12^2 = 25 + 144 = 169
\]
Taking the square root:
\[
c = \sqrt{169} = 13
\]
Thus, the hypotenuse is **13**.
</details>

7. 🟢 Find the missing leg when hypotenuse = 13 and one leg = 5.
<details>
<summary>Solution</summary>

Let the hypotenuse be \( c = 13 \), the given leg be \( a = 5 \), and the missing leg be \( b \).
According to the Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
Substituting the values:
\[
5^2 + b^2 = 13^2
\]
\[
25 + b^2 = 169
\]
\[
b^2 = 169 - 25 = 144
\]
Taking the square root:
\[
b = \sqrt{144} = 12
\]
Thus, the missing leg is **12**.
</details>

8. 🟡 A ladder 10 m long reaches a window 8 m above ground. How far is the ladder's foot from the wall?<br>
<details>
<summary>Solution</summary>

The ladder leaning against the wall forms a right triangle where:
- The ladder acts as the hypotenuse, \( c = 10\text{ m} \).
- The height of the window acts as the vertical leg, \( a = 8\text{ m} \).
- The distance from the ladder's foot to the wall acts as the horizontal leg, \( b \).

Using Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
\[
8^2 + b^2 = 10^2
\]
\[
64 + b^2 = 100
\]
\[
b^2 = 100 - 64 = 36
\]
Taking the square root:
\[
b = \sqrt{36} = 6\text{ m}
\]
Thus, the foot of the ladder is **\( 6\text{ m} \)** away from the wall.
</details>

9. 🟢 Find the diagonal of a rectangle 6 cm by 8 cm.
<details>
<summary>Solution</summary>

The diagonal of a rectangle splits it into two identical right-angled triangles, where the length and width of the rectangle serve as the legs of the right triangle.
Let:
- Leg \( a = 6\text{ cm} \)
- Leg \( b = 8\text{ cm} \)
- Diagonal (hypotenuse) = \( d \)

Applying Pythagoras theorem:
\[
d^2 = a^2 + b^2
\]
\[
d^2 = 6^2 + 8^2 = 36 + 64 = 100
\]
Taking the square root:
\[
d = \sqrt{100} = 10\text{ cm}
\]
Thus, the diagonal of the rectangle is **\( 10\text{ cm} \)**.
</details>

10. 🟡 A right triangle has hypotenuse 17 cm and one leg 15 cm. Find the other leg.
<details>
<summary>Solution</summary>

Let:
- Hypotenuse \( c = 17\text{ cm} \)
- Known leg \( a = 15\text{ cm} \)
- Unknown leg = \( b \)

By Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
\[
15^2 + b^2 = 17^2
\]
\[
225 + b^2 = 289
\]
\[
b^2 = 289 - 225 = 64
\]
Taking the square root:
\[
b = \sqrt{64} = 8\text{ cm}
\]
Thus, the other leg is **\( 8\text{ cm} \)**.
</details>

---

### Type 3: Checking If a Triangle Is Right-Angled

**Goal:** Given three side lengths, determine if they form a right triangle.

**Solved Example:**

Check if sides 7, 24, 25 form a right triangle.

**Solution:**
```
Check: longest² = sum of squares of other two?<br>
25² = 625
7² + 24² = 49 + 576 = 625
625 = 625 ✓
Yes, it's a right triangle.
```
🟢 Easy

---

**Practice Problems:**

11. 🟢 Check: 8, 15, 17
<details>
<summary>Solution</summary>

To determine if these sides form a right triangle, we check if the square of the longest side equals the sum of the squares of the other two sides.
- Longest side \( c = 17 \).
- Other two sides \( a = 8 \), \( b = 15 \).

Check:
\[
c^2 = 17^2 = 289
\]
\[
a^2 + b^2 = 8^2 + 15^2 = 64 + 225 = 289
\]
Since \( a^2 + b^2 = c^2 \), the triplet \( (8, 15, 17) \) satisfies the Pythagoras theorem.
Therefore, it **is** a right triangle.
</details>

12. 🟡 Check: 5, 6, 8
<details>
<summary>Solution</summary>

Identify the longest side as the potential hypotenuse:
- Longest side \( c = 8 \).
- Other sides \( a = 5 \), \( b = 6 \).

Calculate:
\[
c^2 = 8^2 = 64
\]
\[
a^2 + b^2 = 5^2 + 6^2 = 25 + 36 = 61
\]
Since \( 61 \neq 64 \) (\( a^2 + b^2 \neq c^2 \)), the triplet does not satisfy the Pythagoras theorem.
Therefore, it **is not** a right triangle.
</details>

13. 🟢 Check: 9, 40, 41
<details>
<summary>Solution</summary>

Identify the longest side:
- Longest side \( c = 41 \).
- Other sides \( a = 9 \), \( b = 40 \).

Check:
\[
c^2 = 41^2 = 1681
\]
\[
a^2 + b^2 = 9^2 + 40^2 = 81 + 1600 = 1681
\]
Since \( a^2 + b^2 = c^2 \), the triplet satisfies the Pythagoras theorem.
Therefore, it **is** a right triangle.
</details>

14. 🟢 Check: 12, 16, 20
<details>
<summary>Solution</summary>

Identify the longest side:
- Longest side \( c = 20 \).
- Other sides \( a = 12 \), \( b = 16 \).

Check:
\[
c^2 = 20^2 = 400
\]
\[
a^2 + b^2 = 12^2 + 16^2 = 144 + 256 = 400
\]
Since \( a^2 + b^2 = c^2 \), the triplet satisfies the Pythagoras theorem.
Therefore, it **is** a right triangle.
</details>

15. 🟡 A triangle has sides 10, 24, 26. Is it right-angled?<br>
<details>
<summary>Solution</summary>

Identify the longest side:
- Longest side \( c = 26 \).
- Other sides \( a = 10 \), \( b = 24 \).

Check:
\[
c^2 = 26^2 = 676
\]
\[
a^2 + b^2 = 10^2 + 24^2 = 100 + 576 = 676
\]
Since \( a^2 + b^2 = c^2 \), this triangle satisfies Pythagoras theorem.
Therefore, it **is** right-angled.
</details>

---

### Type 4: Pythagoras in Word Problems

**Goal:** Extract the right triangle from a real-world scenario and solve.

**Solved Example:**

A 15 m pole is tied to a peg on the ground using a rope from its top. If the peg is 9 m from the foot of the pole, find the rope length.

**Solution:**
```
Pole height = 15 m (vertical leg)
Distance from foot = 9 m (horizontal leg)
Rope = hypotenuse

h² = 15² + 9²
h² = 225 + 81
h² = 306
h = √306 = 3√34 ≈ 17.49 m
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟢 ⭐ A ship sails 30 km east, then 40 km north. How far is it from the starting point?<br>
<details>
<summary>Solution</summary>

The eastward and northward path of the ship forms two legs of a right triangle, because the directions East and North are perpendicular (\( 90^\circ \)).
- Eastward distance \( a = 30\text{ km} \)
- Northward distance \( b = 40\text{ km} \)
- Distance from start (hypotenuse) = \( c \)

By Pythagoras theorem:
\[
c^2 = a^2 + b^2
\]
\[
c^2 = 30^2 + 40^2 = 900 + 1600 = 2500
\]
Taking the square root:
\[
c = \sqrt{2500} = 50\text{ km}
\]
The ship is **\( 50\text{ km} \)** from its starting point.
</details>

17. 🟡 A ladder 25 m long reaches a window 20 m above ground. How far is its foot from the wall?<br>
<details>
<summary>Solution</summary>

The ladder leaning against the wall forms a right-angled triangle where:
- The ladder is the hypotenuse, \( c = 25\text{ m} \).
- The height of the window on the wall is one leg, \( a = 20\text{ m} \).
- The distance from the foot of the ladder to the wall is the other leg, \( b \).

By Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
\[
20^2 + b^2 = 25^2
\]
\[
400 + b^2 = 625
\]
\[
b^2 = 625 - 400 = 225
\]
Taking the square root:
\[
b = \sqrt{225} = 15\text{ m}
\]
The foot of the ladder is **\( 15\text{ m} \)** from the wall.
</details>

18. 🟡 Two poles of heights 6 m and 10 m stand on a ground. Find the distance between their tops if the distance between their feet is 3 m.
<details>
<summary>Solution</summary>

Let the two vertical poles be \( AB = 10\text{ m} \) and \( CD = 6\text{ m} \).
The distance between their feet on the ground is \( BD = 3\text{ m} \).

Draw a line from the top of the shorter pole \( C \) parallel to the ground to meet the taller pole \( AB \) at point \( E \). This forms a right-angled triangle \( \triangle AEC \), where:
- The horizontal leg \( CE = BD = 3\text{ m} \).
- The vertical leg \( AE = AB - BE = AB - CD = 10\text{ m} - 6\text{ m} = 4\text{ m} \).
- The hypotenuse \( AC \) is the distance between their tops.

Using Pythagoras theorem in \( \triangle AEC \):
\[
AC^2 = AE^2 + CE^2
\]
\[
AC^2 = 4^2 + 3^2 = 16 + 9 = 25
\]
Taking the square root:
\[
AC = \sqrt{25} = 5\text{ m}
\]
The distance between their tops is **\( 5\text{ m} \)**.
</details>

19. 🟡 A wire from the top of a 24 m pole to a peg on the ground is 25 m long. How far is the peg from the pole's foot?<br>
<details>
<summary>Solution</summary>

The vertical pole and the ground form a right angle:
- Height of the pole \( a = 24\text{ m} \).
- Length of the wire (hypotenuse) \( c = 25\text{ m} \).
- Distance from the peg to the foot of the pole \( b \).

By Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
\[
24^2 + b^2 = 25^2
\]
\[
576 + b^2 = 625
\]
\[
b^2 = 625 - 576 = 49
\]
Taking the square root:
\[
b = \sqrt{49} = 7\text{ m}
\]
The peg is **\( 7\text{ m} \)** from the foot of the pole.
</details>

20. 🟢 The diagonal of a square is 8√2 cm. Find its side.
<details>
<summary>Solution</summary>

Let the side of the square be \( s \).
The diagonal \( d \) splits the square into two right-angled isosceles triangles where the sides of the square are the legs and the diagonal is the hypotenuse.

Using Pythagoras theorem:
\[
s^2 + s^2 = d^2
\]
\[
2s^2 = (8\sqrt{2})^2 = 64 \times 2 = 128
\]
\[
s^2 = 64
\]
Taking the square root:
\[
s = 8\text{ cm}
\]
Thus, the side of the square is **\( 8\text{ cm} \)**.
</details>

---

## Stage 4: Type Mixer

1. 🟡 A right triangle has hypotenuse 13 and one leg 12. Find the other leg. Then find all three side ratios (opp/hyp, adj/hyp, opp/adj).
<details>
<summary>Solution</summary>

Let the hypotenuse be \( c = 13 \), one leg be \( b = 12 \), and the other leg be \( a \).
By Pythagoras theorem:
\[
a^2 + b^2 = c^2
\]
\[
a^2 + 12^2 = 13^2 \implies a^2 + 144 = 169
\]
\[
a^2 = 169 - 144 = 25 \implies a = 5
\]
The other leg has a length of **5**.

Next, we calculate the three side ratios (opposite/hypotenuse, adjacent/hypotenuse, opposite/adjacent). The values depend on which angle we select:

- **Case 1**: Relative to the angle \( \theta \) opposite to the leg of length 5:
  - Opposite = 5
  - Adjacent = 12
  - Hypotenuse = 13
  - \(\text{opp/hyp} = \frac{5}{13}\)
  - \(\text{adj/hyp} = \frac{12}{13}\)
  - \(\text{opp/adj} = \frac{5}{12}\)

- **Case 2**: Relative to the angle \( \phi \) opposite to the leg of length 12:
  - Opposite = 12
  - Adjacent = 5
  - Hypotenuse = 13
  - \(\text{opp/hyp} = \frac{12}{13}\)
  - \(\text{adj/hyp} = \frac{5}{13}\)
  - \(\text{opp/adj} = \frac{12}{5}\)
</details>

2. 🟡 Check if 11, 60, 61 can be sides of a right triangle. If yes, which side would be opposite the right angle?<br>
<details>
<summary>Solution</summary>

Let the potential hypotenuse (longest side) be \( c = 61 \) and the other two sides be \( a = 11 \) and \( b = 60 \).
We verify if they satisfy Pythagoras theorem:
\[
c^2 = 61^2 = 3721
\]
\[
a^2 + b^2 = 11^2 + 60^2 = 121 + 3600 = 3721
\]
Since \( a^2 + b^2 = c^2 \), the triplet satisfies the Pythagoras theorem. Thus, it **is** a right triangle.

In a right triangle, the side opposite the right angle is the hypotenuse. The hypotenuse is always the longest side.
Therefore, the side opposite the right angle is the side of length **61**.
</details>

3. 🔴 ⭐ A 10 m ladder leans against a wall with its foot 6 m from the wall. How high up the wall does it reach?<br> What is the distance from the top of the ladder to a point on the wall 2 m below it?<br>
<details>
<summary>Solution</summary>

**Part 1: How high up the wall does it reach?**
The ladder, ground, and wall form a right triangle:
- Hypotenuse (ladder length) \( c = 10\text{ m} \)
- Base leg (distance from wall) \( b = 6\text{ m} \)
- Vertical height leg \( h \)

Using Pythagoras theorem:
\[
h^2 + b^2 = c^2
\]
\[
h^2 + 6^2 = 10^2
\]
\[
h^2 + 36 = 100 \implies h^2 = 64 \implies h = 8\text{ m}
\]
So, the ladder reaches **\( 8\text{ m} \)** up the wall.

**Part 2: Distance from the top of the ladder to a point 2 m below it on the wall**
The top of the ladder is at a height of \( 8\text{ m} \) on the wall. A point on the wall 2 m below the top of the ladder is at a height of:
\[
8\text{ m} - 2\text{ m} = 6\text{ m}
\]
Since both the top of the ladder (on the wall) and the target point (also on the wall) lie along the exact same vertical wall line, the distance between them is the vertical distance:
\[
8\text{ m} - 6\text{ m} = 2\text{ m}
\]
So, the distance is **\( 2\text{ m} \)**.
</details>

4. 🟡 In triangle ABC, ∠B = 90°, AB = 8, BC = 15. Find AC. Then identify the opposite and adjacent sides for ∠C.
<details>
<summary>Solution</summary>

Given \( \triangle ABC \) with \( \angle B = 90^\circ \):
- The hypotenuse is \( AC \).
- The legs are \( AB = 8 \) and \( BC = 15 \).

By Pythagoras theorem:
\[
AC^2 = AB^2 + BC^2
\]
\[
AC^2 = 8^2 + 15^2 = 64 + 225 = 289
\]
Taking the square root:
\[
AC = \sqrt{289} = 17
\]

For the acute angle \( \angle C \):
- **Opposite side**: The side directly across from \( \angle C \), which is **\( AB \) (length = 8)**.
- **Adjacent side**: The side touching \( \angle C \) (excluding the hypotenuse), which is **\( BC \) (length = 15)**.
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟢 A right triangle has sides 3 cm, 4 cm, 5 cm. Identify the hypotenuse and verify Pythagoras theorem. **(2 marks)**

<details>
<summary>Solution</summary>

Hypotenuse = 5 cm (longest side)
3² + 4² = 9 + 16 = 25 = 5² ✓
</details>

---

**Q2.** 🟢 In a right triangle, the two legs are 15 cm and 20 cm. Find the length of the hypotenuse. **(2 marks)**

<details>
<summary>Solution</summary>

h² = 15² + 20² = 225 + 400 = 625
h = 25 cm
</details>

---

**Q3.** 🟡 ⭐ A ladder 13 m long reaches a window 12 m above ground. Find the distance of the foot of the ladder from the wall. **(3 marks)**

<details>
<summary>Solution</summary>

13² = 12² + d²
169 = 144 + d²
d² = 25
d = 5 m
</details>

---

**Q4.** 🟡 Two towers of height 12 m and 8 m stand on level ground. If the distance between their feet is 3 m, find the distance between their tops. **(3 marks)**

<details>
<summary>Solution</summary>

Height difference = 12 - 8 = 4 m
Horizontal distance = 3 m
Distance between tops² = 4² + 3² = 16 + 9 = 25
Distance = 5 m
</details>

---

## Stage 6: JEE Mains Arena

*Note: This chapter is foundational. JEE-level questions will begin from Chapter 3 onwards. Here we include simple MCQs to build exam temperament.*

**Q1.** The sides of a triangle are 6, 8, 10. Which of the following is true?<br>
(a) It is acute-angled
(b) It is right-angled
(c) It is obtuse-angled
(d) Cannot be determined

<details>
<summary>Solution</summary>
10² = 100, 6² + 8² = 36 + 64 = 100
Since 10² = 6² + 8², it satisfies Pythagoras theorem.
∴ It is right-angled.
Answer: (b) 🟢
</details>

---

**Q2.** The distance between the tops of two poles of heights 15 m and 10 m, placed 12 m apart on level ground, is:
(a) 13 m
(b) 15 m
(c) 17 m
(d) 12 m

<details>
<summary>Solution</summary>
Height difference = 15 - 10 = 5 m
Horizontal distance = 12 m
Distance² = 5² + 12² = 25 + 144 = 169
Distance = 13 m
Answer: (a) 🟢
</details>

---

**Q3.** If the diagonal of a square is 10√2 cm, its side is:
(a) 10 cm
(b) 5 cm
(c) 20 cm
(d) 15 cm

<details>
<summary>Solution</summary>
In a square of side a, diagonal = a√2
Given: a√2 = 10√2
∴ a = 10 cm
Answer: (a) 🟢
</details>

---

**Q4.** A man goes 24 m west and then 10 m north. His distance from the starting point is:
(a) 34 m
(b) 26 m
(c) 28 m
(d) 30 m

<details>
<summary>Solution</summary>
Distance² = 24² + 10² = 576 + 100 = 676
Distance = 26 m
Answer: (b) 🟢
</details>

---

**Q5.** The sides of a right triangle are in the ratio 3 : 4 : 5. If the perimeter is 36 cm, the longest side is:
(a) 9 cm
(b) 12 cm
(c) 15 cm
(d) 18 cm

<details>
<summary>Solution</summary>
Let sides be 3x, 4x, 5x
Perimeter = 3x + 4x + 5x = 12x = 36
x = 3
Longest side = 5x = 15 cm
Answer: (c) 🟢
</details>

---

## Stage 7: Assertion-Reasoning

**Directions:** For each question, choose:
(a) Both A and R are true and R is the correct explanation of A
(b) Both A and R are true but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

---

**Q1.** **Assertion <br>
(A):** In a right triangle with sides 5, 12, 13, the hypotenuse is 13.
**Reason (R):** The hypotenuse is the longest side of a right triangle.

<details>
<summary>Solution</summary>
A is true: 13 is indeed the longest side.
R is true: The hypotenuse is always the longest side.
R correctly explains why 13 is the hypotenuse.
Answer: (a) 🟢
</details>

---

**Q2.** **Assertion <br>
(A):** A triangle with sides 7, 24, 25 is right-angled.
**Reason (R):** For any right triangle, the sum of squares of two sides equals the square of the third.

<details>
<summary>Solution</summary>
A is true: 7² + 24² = 49 + 576 = 625 = 25²
R is true but incomplete — it must say "sum of squares of legs equals square of hypotenuse," not just "any two sides."
Answer: (c) 🟡
</details>

---

**Q3.** **Assertion <br>
(A):** In a right triangle, the side opposite the right angle is called the adjacent side.
**Reason (R):** Each side in a triangle has a specific name based on its position relative to the angle under consideration.

<details>
<summary>Solution</summary>
A is false: The side opposite the right angle is the hypotenuse, not the adjacent side.
R is true: Side names depend on which angle we're referencing.
Answer: (d) 🟢
</details>

---

**Q4.** **Assertion <br>
(A):** If a right triangle has legs 8 and 15, its hypotenuse is 17.
**Reason (R):** 8² + 15² = 289 = 17².

<details>
<summary>Solution</summary>
A is true: 8² + 15² = 64 + 225 = 289, √289 = 17
R is true and correctly explains A.
Answer: (a) 🟢
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The hypotenuse of a right triangle with sides 9 and 12 is:
   (a) 15   (b) 14   (c) 13   (d) 16
<details>
<summary>Solution</summary>

Let the legs of the right triangle be \( a = 9 \) and \( b = 12 \).
By Pythagoras theorem, the hypotenuse \( c \) is:
\[
c = \sqrt{a^2 + b^2} = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15
\]
Thus, the hypotenuse is 15.

**Answer: (a) 15**
</details>

2. 🟢 In a right triangle with right angle at B, the side opposite to ∠A is:
   (a) AB   (b) BC   (c) AC   (d) None
<details>
<summary>Solution</summary>

In right-angled triangle \( \triangle ABC \) with \( \angle B = 90^\circ \), the sides are \( AB \), \( BC \), and \( AC \).
The side opposite to \( \angle A \) is the side that does not contain vertex \( A \), which is \( BC \).

**Answer: (b) BC**
</details>

3. 🟢 Which of the following sets cannot be sides of a right triangle?<br>
   (a) 6, 8, 10   (b) 5, 12, 13   (c) 7, 8, 9   (d) 9, 40, 41
<details>
<summary>Solution</summary>

A set of three numbers can form the sides of a right triangle if the square of the largest number is equal to the sum of the squares of the other two numbers:
- (a) \( 6^2 + 8^2 = 36 + 64 = 100 = 10^2 \) (Forms a right triangle)
- (b) \( 5^2 + 12^2 = 25 + 144 = 169 = 13^2 \) (Forms a right triangle)
- (c) \( 7^2 + 8^2 = 49 + 64 = 113 \neq 9^2 = 81 \) (Cannot form a right triangle)
- (d) \( 9^2 + 40^2 = 81 + 1600 = 1681 = 41^2 \) (Forms a right triangle)

Therefore, 7, 8, 9 cannot form the sides of a right triangle.

**Answer: (c) 7, 8, 9**
</details>

4. 🟡 ⭐ A 26 m long ladder reaches a window 24 m above ground. The distance of its foot from the wall is:
   (a) 8 m   (b) 10 m   (c) 12 m   (d) 14 m
<details>
<summary>Solution</summary>

The ladder leaning against the wall forms a right triangle:
- Hypotenuse (ladder length) \( c = 26\text{ m} \)
- Vertical height \( a = 24\text{ m} \)
- Distance of foot from the wall \( b \)

Using Pythagoras theorem:
\[
a^2 + b^2 = c^2 \implies 24^2 + b^2 = 26^2
\]
\[
b^2 = 26^2 - 24^2 = (26 - 24)(26 + 24) = 2 \times 50 = 100
\]
\[
b = \sqrt{100} = 10\text{ m}
\]
The distance is 10 m.

**Answer: (b) 10 m**
</details>

5. 🟢 The perimeter of a right triangle with sides 8, 15, 17 is:
   (a) 30   (b) 40   (c) 35   (d) 45
<details>
<summary>Solution</summary>

The perimeter \( P \) of a triangle is the sum of its three sides:
\[
P = 8 + 15 + 17 = 40
\]

**Answer: (b) 40**
</details>

6. 🟢 In ∆ABC, ∠B = 90°, AB = 6, BC = 8. AC = ?<br>
   (a) 9   (b) 10   (c) 11   (d) 12
<details>
<summary>Solution</summary>

Since \( \angle B = 90^\circ \), \( AC \) is the hypotenuse.
By Pythagoras theorem:
\[
AC^2 = AB^2 + BC^2
\]
\[
AC^2 = 6^2 + 8^2 = 36 + 64 = 100
\]
Taking the square root:
\[
AC = \sqrt{100} = 10
\]

**Answer: (b) 10**
</details>

7. 🟢 The side opposite to the marked angle in a right triangle is called:
   (a) Hypotenuse   (b) Adjacent   (c) Opposite   (d) Base
<details>
<summary>Solution</summary>

By mathematical definition, in a right triangle:
- The side opposite to the right angle is called the hypotenuse.
- The side opposite to the marked angle is called the opposite side.
- The side adjacent to the marked angle (other than the hypotenuse) is called the adjacent side.

**Answer: (c) Opposite**
</details>

8. 🟡 If the diagonal of a rectangle is 25 cm and one side is 7 cm, the other side is:
   (a) 20 cm   (b) 24 cm   (c) 22 cm   (d) 18 cm
<details>
<summary>Solution</summary>

A diagonal \( d \) of a rectangle of sides \( a \) and \( b \) forms a right-angled triangle.
Given:
- Diagonal \( d = 25\text{ cm} \)
- One side \( a = 7\text{ cm} \)

Using Pythagoras theorem:
\[
a^2 + b^2 = d^2 \implies 7^2 + b^2 = 25^2
\]
\[
49 + b^2 = 625 \implies b^2 = 625 - 49 = 576
\]
Taking the square root:
\[
b = \sqrt{576} = 24\text{ cm}
\]
The other side is 24 cm.

**Answer: (b) 24 cm**
</details>

9. 🟢 ⭐ A ship travels 15 km east and 8 km north. Its distance from the start is:
   (a) 16 km   (b) 17 km   (c) 18 km   (d) 20 km
<details>
<summary>Solution</summary>

The eastward and northward paths are perpendicular. The distance from the starting point is the hypotenuse \( c \):
- Legs: \( a = 15\text{ km} \) and \( b = 8\text{ km} \)

Using Pythagoras theorem:
\[
c = \sqrt{a^2 + b^2} = \sqrt{15^2 + 8^2} = \sqrt{225 + 64} = \sqrt{289} = 17\text{ km}
\]

**Answer: (b) 17 km**
</details>

10. 🟡 For which of the following is Pythagoras theorem NOT satisfied?<br>
    (a) 3, 4, 5   (b) 1, 1, √2   (c) 1, 2, √5   (d) 2, 3, 4
<details>
<summary>Solution</summary>

We check if \( a^2 + b^2 = c^2 \) for the given sets where \( c \) is the largest side:
- (a) \( 3^2 + 4^2 = 9 + 16 = 25 = 5^2 \) (Satisfied)
- (b) \( 1^2 + 1^2 = 2 = (\sqrt{2})^2 \) (Satisfied)
- (c) \( 1^2 + 2^2 = 1 + 4 = 5 = (\sqrt{5})^2 \) (Satisfied)
- (d) \( 2^2 + 3^2 = 4 + 9 = 13 \neq 4^2 = 16 \) (Not satisfied)

Thus, Pythagoras theorem is not satisfied for 2, 3, 4.

**Answer: (d) 2, 3, 4**
</details>

11. 🟢 In a right triangle, the longest side is called:
    (a) Opposite   (b) Adjacent   (c) Hypotenuse   (d) Base
<details>
<summary>Solution</summary>

In any right-angled triangle, the hypotenuse is the side opposite the right (\( 90^\circ \)) angle, which is always the longest side.

**Answer: (c) Hypotenuse**
</details>

12. 🟡 Two poles 18 m and 10 m high have their feet 15 m apart. The distance between their tops is:
    (a) 15 m   (b) 17 m   (c) 20 m   (d) 25 m
<details>
<summary>Solution</summary>

Let the heights of the two poles be \( H_1 = 18\text{ m} \) and \( H_2 = 10\text{ m} \).
The horizontal distance between their feet is \( d_{feet} = 15\text{ m} \).

The difference in height between the two poles forms one leg of a right triangle:
\[
\text{Leg}_1 = 18 - 10 = 8\text{ m}
\]
The horizontal distance forms the other leg:
\[
\text{Leg}_2 = 15\text{ m}
\]
The straight-line distance between the tops of the poles is the hypotenuse \( x \):
\[
x = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17\text{ m}
\]
The distance between their tops is 17 m.

**Answer: (b) 17 m**
</details>

13. 🟡 The altitude of an equilateral triangle of side 2a is:
    (a) a√2   (b) a√3   (c) 2a   (d) a
<details>
<summary>Solution</summary>

Let the equilateral triangle be \( \triangle PQR \) with side length \( 2a \). Let \( PS \) be the altitude from vertex \( P \) to side \( QR \).
In an equilateral triangle, the altitude bisects the base. Thus:
\[
QS = SR = a
\]
\( \triangle PSQ \) is a right triangle with hypotenuse \( PQ = 2a \), base \( QS = a \), and vertical height \( PS \) (the altitude).

Using Pythagoras theorem:
\[
PS^2 + QS^2 = PQ^2 \implies PS^2 + a^2 = (2a)^2
\]
\[
PS^2 + a^2 = 4a^2 \implies PS^2 = 3a^2
\]
\[
PS = a\sqrt{3}
\]
Thus, the altitude is \( a\sqrt{3} \).

**Answer: (b) a√3**
</details>

14. 🟡 If the sides of a triangle are 13, 14, 15, is it right-angled?<br>
    (a) Yes   (b) No   (c) Cannot say   (d) Only if area is given
<details>
<summary>Solution</summary>

Let the sides be \( a = 13 \), \( b = 14 \), and the longest side \( c = 15 \).
We verify if \( a^2 + b^2 = c^2 \):
\[
13^2 + 14^2 = 169 + 196 = 365
\]
\[
15^2 = 225
\]
Since \( 365 \neq 225 \), the triangle does not satisfy the Pythagoras theorem and is not right-angled.

**Answer: (b) No**
</details>

15. 🟡 ⭐ A man walks 30 m south and then 40 m west. How far is he from start?<br>
    (a) 45 m   (b) 50 m   (c) 55 m   (d) 60 m
<details>
<summary>Solution</summary>

The directions South and West are perpendicular to each other.
Let the walking path represent the legs of a right triangle:
- Southward distance \( a = 30\text{ m} \)
- Westward distance \( b = 40\text{ m} \)

The straight-line distance from the starting point is the hypotenuse \( c \):
\[
c = \sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50\text{ m}
\]
He is 50 m from the starting point.

**Answer: (b) 50 m**
</details>

---

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | c |
| 2 | b | 7 | c | 12 | b |
| 3 | c | 8 | b | 13 | b |
| 4 | b | 9 | b | 14 | b |
| 5 | b | 10 | d | 15 | b |

</details>

---

## What's Next?<br>

In this chapter, you've understood **what trigonometry is** and refreshed the **Pythagoras theorem** — the mathematical foundation of everything that follows.

You also learned the language: **hypotenuse**, **opposite**, **adjacent**.

In **Chapter 2**, we'll learn how to measure angles in two different systems — degrees and radians — and why radians make all of higher mathematics possible.

**Key takeaway from Chapter 1:** Trigonometry is the art of finding what you cannot measure, using the relationships between angles and side-ratios. Everything else is built on this one idea.
