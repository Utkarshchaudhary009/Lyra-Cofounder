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

3. 🟢 Draw any right triangle. Mark an acute angle. Label all three sides.

4. 🟢 In a right triangle with vertices P, Q, R where ∠Q = 90° and angle is marked at P, which side is the opposite?<br>

5. 🟢 True or False: The adjacent side is always the shortest side.

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
7. 🟢 Find the missing leg when hypotenuse = 13 and one leg = 5.
8. 🟡 A ladder 10 m long reaches a window 8 m above ground. How far is the ladder's foot from the wall?<br>
9. 🟢 Find the diagonal of a rectangle 6 cm by 8 cm.
10. 🟡 A right triangle has hypotenuse 17 cm and one leg 15 cm. Find the other leg.

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
12. 🟡 Check: 5, 6, 8
13. 🟢 Check: 9, 40, 41
14. 🟢 Check: 12, 16, 20
15. 🟡 A triangle has sides 10, 24, 26. Is it right-angled?<br>

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
17. 🟡 A ladder 25 m long reaches a window 20 m above ground. How far is its foot from the wall?<br>
18. 🟡 Two poles of heights 6 m and 10 m stand on a ground. Find the distance between their tops if the distance between their feet is 3 m.
19. 🟡 A wire from the top of a 24 m pole to a peg on the ground is 25 m long. How far is the peg from the pole's foot?<br>
20. 🟢 The diagonal of a square is 8√2 cm. Find its side.

---

## Stage 4: Type Mixer

1. 🟡 A right triangle has hypotenuse 13 and one leg 12. Find the other leg. Then find all three side ratios (opp/hyp, adj/hyp, opp/adj).

2. 🟡 Check if 11, 60, 61 can be sides of a right triangle. If yes, which side would be opposite the right angle?<br>

3. 🔴 ⭐ A 10 m ladder leans against a wall with its foot 6 m from the wall. How high up the wall does it reach?<br> What is the distance from the top of the ladder to a point on the wall 2 m below it?<br>

4. 🟡 In triangle ABC, ∠B = 90°, AB = 8, BC = 15. Find AC. Then identify the opposite and adjacent sides for ∠C.

---

## Stage 5: Board Arsenal

**Q1.** 🟢 A right triangle has sides 3 cm, 4 cm, 5 cm. Identify the hypotenuse and verify Pythagoras theorem. **(2 marks)**

**Solution:**
Hypotenuse = 5 cm (longest side)
3² + 4² = 9 + 16 = 25 = 5² ✓

---

**Q2.** 🟢 In a right triangle, the two legs are 15 cm and 20 cm. Find the length of the hypotenuse. **(2 marks)**

**Solution:**
h² = 15² + 20² = 225 + 400 = 625
h = 25 cm

---

**Q3.** 🟡 ⭐ A ladder 13 m long reaches a window 12 m above ground. Find the distance of the foot of the ladder from the wall. **(3 marks)**

**Solution:**
13² = 12² + d²
169 = 144 + d²
d² = 25
d = 5 m

---

**Q4.** 🟡 Two towers of height 12 m and 8 m stand on level ground. If the distance between their feet is 3 m, find the distance between their tops. **(3 marks)**

**Solution:**
Height difference = 12 - 8 = 4 m
Horizontal distance = 3 m
Distance between tops² = 4² + 3² = 16 + 9 = 25
Distance = 5 m

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

2. 🟢 In a right triangle with right angle at B, the side opposite to ∠A is:
   (a) AB   (b) BC   (c) AC   (d) None

3. 🟢 Which of the following sets cannot be sides of a right triangle?<br>
   (a) 6, 8, 10   (b) 5, 12, 13   (c) 7, 8, 9   (d) 9, 40, 41

4. 🟡 ⭐ A 26 m long ladder reaches a window 24 m above ground. The distance of its foot from the wall is:
   (a) 8 m   (b) 10 m   (c) 12 m   (d) 14 m

5. 🟢 The perimeter of a right triangle with sides 8, 15, 17 is:
   (a) 30   (b) 40   (c) 35   (d) 45

6. 🟢 In ∆ABC, ∠B = 90°, AB = 6, BC = 8. AC = ?<br>
   (a) 9   (b) 10   (c) 11   (d) 12

7. 🟢 The side opposite to the marked angle in a right triangle is called:
   (a) Hypotenuse   (b) Adjacent   (c) Opposite   (d) Base

8. 🟡 If the diagonal of a rectangle is 25 cm and one side is 7 cm, the other side is:
   (a) 20 cm   (b) 24 cm   (c) 22 cm   (d) 18 cm

9. 🟢 ⭐ A ship travels 15 km east and 8 km north. Its distance from the start is:
   (a) 16 km   (b) 17 km   (c) 18 km   (d) 20 km

10. 🟡 For which of the following is Pythagoras theorem NOT satisfied?<br>
    (a) 3, 4, 5   (b) 1, 1, √2   (c) 1, 2, √5   (d) 2, 3, 4

11. 🟢 In a right triangle, the longest side is called:
    (a) Opposite   (b) Adjacent   (c) Hypotenuse   (d) Base

12. 🟡 Two poles 18 m and 10 m high have their feet 15 m apart. The distance between their tops is:
    (a) 15 m   (b) 17 m   (c) 20 m   (d) 25 m

13. 🟡 The altitude of an equilateral triangle of side 2a is:
    (a) a√2   (b) a√3   (c) 2a   (d) a

14. 🟡 If the sides of a triangle are 13, 14, 15, is it right-angled?<br>
    (a) Yes   (b) No   (c) Cannot say   (d) Only if area is given

15. 🟡 ⭐ A man walks 30 m south and then 40 m west. How far is he from start?<br>
    (a) 45 m   (b) 50 m   (c) 55 m   (d) 60 m

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
