*Previous: [Chapter 1 — Scalars and Vectors ←](./01_scalars_and_vectors.md)*

# Chapter 2: Types of Vectors — Meet the Family

> *NCERT: Class 11 Physics 4.2 | Class 12 Maths 10.2*

---

## 🎯 Stage 1: The Core Idea

Welcome to the vector zoo! In mathematics and physics, vectors aren't just arrows on a page; they are mathematical objects that describe physical realities and geometric constraints. Imagine you are building a house. The command "move the brick 5 meters north" is a vector. The force you apply to the door handle to open it is also a vector. But they behave very differently. Moving a brick 5 meters north is the same regardless of whether you start in the living room or the kitchen. But pushing a door handle only works if you push *the handle*, not the wall next to it. 

Because vectors represent such a wide variety of physical quantities (displacements, velocities, forces, torques), we need to categorize them. This chapter is all about giving names to these different behaviors. By understanding the *types* of vectors, you equip yourself with the precise vocabulary needed to solve complex 3D geometry problems and mechanics equations.

Let's look at the two most special members of the vector family: the **Unit Vector** and the **Zero Vector**.

The **Unit Vector** is the purest expression of direction. Think of a standard vector as a combination of two things: "How much?" (Magnitude) and "Which way?" (Direction). If you strip away the "How much?" by scaling the vector down until its length is exactly 1, you are left with pure direction. It's the compass of the mathematical world. When you want to tell a force to point in a specific direction without changing its strength, you multiply it by a unit vector.

On the other extreme, we have the **Zero Vector** (or Null Vector). Imagine pushing a box with 10 Newtons of force to the left, while your friend pushes it with 10 Newtons to the right. The net force is zero. But force is a vector, so the answer must be a vector. Enter the zero vector! It has a magnitude of exactly 0. But what about its direction? Since it has no length, it can't point anywhere. Its direction is *arbitrary* or *indeterminate*. Geometrically, it is just a point.

Finally, we must distinguish between **Free Vectors** and **Bound (Localized) Vectors**.
- **Free Vectors:** Imagine drawing an arrow on a transparent sheet of plastic. You can slide that plastic sheet anywhere on your desk, and the arrow still points in the same direction with the same length. This is a free vector. In pure mathematics (like CBSE Class 12 Maths), almost all vectors are free vectors. You can translate them anywhere to make their tails touch.
- **Bound Vectors:** Now imagine that the arrow represents a finger pressing a button. If you slide the transparent sheet, the finger misses the button! The vector's effect depends entirely on its starting point. This is a bound vector.

> ⚠️ **Critical Insights**
> - A vector is NOT tied to a specific location in space unless explicitly stated (Bound Vector). You can move a free vector anywhere as long as you keep its magnitude and direction unchanged.
> - Two vectors are considered **Equal Vectors** only if they have the exact same magnitude AND the exact same direction. Having the same magnitude is not enough!

> 💡 **Tips**
> - Whenever a problem asks you for a vector in the "direction of" another vector, immediately think: "I need to find the unit vector!"
> - The zero vector ($\vec{0}$) is written with an arrow on top. Don't just write $0$ (the scalar number). They are mathematically different entities!

> 🔑 **Key Takeaways**
> - **Collinear vectors** do not need to lie on the exact same line. As long as they are parallel, they are collinear. (Hence they are also called parallel vectors).
> - **Unit vectors** have NO physical units (like meters or Newtons) and NO dimensions. They are pure, dimensionless pointers.

---

## 🔬 Stage 2: The Formula Lab

In this chapter, the math is light, but the definitions are heavy. Here are the core mathematical relationships you need to memorize.

### 1. The Unit Vector Formula
The formula to extract the pure direction from any vector $\vec{a}$ is:

$$ \hat{a} = \frac{\vec{a}}{|\vec{a}|} $$

| Symbol | Meaning | Unit / Type |
| :--- | :--- | :--- |
| $\hat{a}$ | Unit vector in the direction of $\vec{a}$ | Dimensionless (Pure direction) |
| $\vec{a}$ | The original vector | Depends on physical quantity |
| $|\vec{a}|$ | Magnitude of the original vector | Same as original vector |

**What this formula says:** 
"To find the unit vector $\hat{a}$, take the original vector $\vec{a}$ and divide it by its own length (magnitude). This scales the vector down to exactly 1 unit of length, preserving only its original direction."

### 2. The Collinearity Condition
For any two non-zero vectors $\vec{a}$ and $\vec{b}$, they are collinear (parallel) if and only if:

$$ \vec{a} = \lambda \vec{b} $$

| Symbol | Meaning | Condition |
| :--- | :--- | :--- |
| $\vec{a}, \vec{b}$ | The two vectors being compared | Must be non-zero vectors |
| $\lambda$ | A scalar multiplier (real number) | $\lambda \neq 0$ |

**What this formula says:**
"Two vectors are parallel if one is just a scaled-up, scaled-down, or reversed version of the other. If $\lambda > 0$, they are *like vectors* (same direction). If $\lambda < 0$, they are *unlike vectors* (opposite direction)."

### 3. The Coplanarity Condition (Scalar Triple Product)
Three vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ are coplanar (lie in the same plane) if their scalar triple product is zero:

$$ [\vec{a} \vec{b} \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = 0 $$

Alternatively, in determinant form, if $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$, $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$, and $\vec{c} = c_1\hat{i} + c_2\hat{j} + c_3\hat{k}$, they are coplanar if:

$$ \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix} = 0 $$

### The 12 Types of Vectors at a Glance

| Type of Vector | Definition | Mathematical / Visual Condition |
| :--- | :--- | :--- |
| **Zero (Null) Vector** | Magnitude is 0, direction is indeterminate. | $\vec{0}$ (Initial & terminal points coincide) |
| **Unit Vector** | Magnitude is exactly 1. | $|\hat{a}| = 1$ |
| **Equal Vectors** | Same magnitude AND same direction. | $\vec{a} = \vec{b}$ |
| **Negative Vector** | Same magnitude, opposite direction. | $\vec{b} = -\vec{a}$ |
| **Like Vectors** | Same direction, different magnitudes. | $\vec{a} = k\vec{b}$ where $k > 0$ |
| **Unlike Vectors** | Opposite directions. | $\vec{a} = k\vec{b}$ where $k < 0$ |
| **Collinear (Parallel)** | Act along the same or parallel lines. | $\vec{a} = \lambda\vec{b}$ (Magnitude/direction don't matter) |
| **Coplanar Vectors** | Lie in the same plane or parallel planes. | $[\vec{a} \vec{b} \vec{c}] = 0$ (Any 2 vectors are always coplanar) |
| **Coinitial Vectors** | Start from the same initial point. | Tails are connected. |
| **Coterminous Vectors**| End at the same terminal point. | Heads are connected. |
| **Free Vectors** | Can be translated anywhere without change. | Default in mathematics. |
| **Bound Vectors** | Fixed initial point (cannot be translated). | Position vectors, forces at a point. |

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Identifying Vectors from Diagrams ⭐
**Pattern:** "Given a regular polygon or a grid, identify which vectors are equal, collinear, coinitial, etc."

**Solved Example** 🟡
> In a regular hexagon ABCDEF, identify all pairs of vectors formed by its sides that are:
> (i) Equal vectors
> (ii) Coinitial vectors
> (iii) Collinear but not equal
<details><summary><b>Solution</b></summary>
Let the vertices in order be A, B, C, D, E, F. 
The sides form vectors: $\vec{AB}, \vec{BC}, \vec{CD}, \vec{DE}, \vec{EF}, \vec{FA}$.

**Step 1: Analyze Equal Vectors**
In a regular hexagon, opposite sides are parallel and equal in length.
Because vectors require the *exact same direction*, we must look at parallel sides that point the same way.
$\vec{AB}$ and $\vec{ED}$ point in exactly opposite directions. So, $\vec{AB} = \vec{ED}$ is FALSE.
Actually, if we move around the perimeter ABCDEF, opposite sides are AB and DE. 
$\vec{AB} = -\vec{DE}$. Thus $\vec{AB}$ and $\vec{ED}$ are equal! 
Wait, let's visualize it carefully. If A is top-left and B is top-right, $\vec{AB}$ points right. D is bottom-right and E is bottom-left, so $\vec{DE}$ points left. Hence $\vec{ED}$ points right.
Yes! $\vec{AB} = \vec{ED}$.
Similarly, $\vec{BC} = \vec{FE}$ and $\vec{CD} = \vec{AF}$.
So equal vectors are: ($\vec{AB}, \vec{ED}$), ($\vec{BC}, \vec{FE}$), ($\vec{CD}, \vec{AF}$).

**Step 2: Analyze Coinitial Vectors**
Coinitial vectors start from the same point. From the given side vectors ($\vec{AB}, \vec{BC}, \vec{CD}, \vec{DE}, \vec{EF}, \vec{FA}$), no two start from the same point because they form a chain head-to-tail.
If we include diagonals like $\vec{AC}, \vec{AD}, \vec{AE}, \vec{AF}$, then they are coinitial with $\vec{AB}$ because they all start at A.

**Step 3: Collinear but not equal**
These are vectors along parallel lines but with opposite directions (or different lengths, though all sides here have same length).
Pairs are: ($\vec{AB}, \vec{DE}$), ($\vec{BC}, \vec{EF}$), ($\vec{CD}, \vec{FA}$).
</details>

**Practice:**
1. 🟢 In a square ABCD, which of the following pairs of vectors are equal: $\vec{AB}$ and $\vec{CD}$, or $\vec{AB}$ and $\vec{DC}$?
<details><summary><b>Answer</b></summary>
$\vec{AB}$ and $\vec{DC}$. In a square, side AB is parallel to DC. Since we go from A to B (say, left to right), the same direction on the bottom side is D to C (left to right). Therefore, $\vec{AB} = \vec{DC}$. ($\vec{AB}$ and $\vec{CD}$ are negative vectors of each other).
</details>

2. 🟢 A diagram shows vector $\vec{a}$ pointing North with length 5, and vector $\vec{b}$ pointing South with length 5. What type of vectors are they?
<details><summary><b>Answer</b></summary>
They are **Negative vectors** (or unlike parallel vectors). They have the same magnitude but exactly opposite directions. Mathematically, $\vec{a} = -\vec{b}$.
</details>

3. 🟢 Vectors $\vec{p}$ and $\vec{q}$ both start from the origin (0,0). What type of vectors are they?
<details><summary><b>Answer</b></summary>
**Coinitial vectors**. Since they share the same starting point (the origin), they are coinitial.
</details>

4. 🟡 In a parallelogram PQRS, identify a pair of coinitial vectors using the vertices.
<details><summary><b>Answer</b></summary>
From vertex P, the vectors $\vec{PQ}$ and $\vec{PS}$ both start at P. Thus, $\vec{PQ}$ and $\vec{PS}$ are coinitial vectors. Similarly, ($\vec{QP}, \vec{QR}$), ($\vec{RS}, \vec{RQ}$), and ($\vec{SP}, \vec{SR}$) are pairs of coinitial vectors.
</details>

5. 🟡 Is it possible for two vectors to be collinear but not equal? Give an example.
<details><summary><b>Answer</b></summary>
Yes. Vectors $\vec{a} = 2\hat{i}$ and $\vec{b} = 4\hat{i}$ are collinear (they act along the x-axis) but they have different magnitudes (2 and 4), so they are not equal. Another example is $\vec{a} = 2\hat{i}$ and $\vec{c} = -2\hat{i}$; they have the same magnitude but opposite directions.
</details>

6. 🔴 In a regular hexagon ABCDEF with center O, identify a vector equal to $\vec{AB}$ that starts from the center O.
<details><summary><b>Answer</b></summary>
In a regular hexagon, the distance from the center to any vertex is equal to the side length, and the segments from the center form equilateral triangles. The vector $\vec{OC}$ is parallel to $\vec{AB}$, points in the exact same direction, and has the same magnitude. Therefore, $\vec{AB} = \vec{OC}$. (Also $\vec{AB} = \vec{FO}$).
</details>

7. 🔴 You are given three vectors representing the adjacent edges of a cube meeting at a common corner. What two types of vectors do they represent?
<details><summary><b>Answer</b></summary>
1. **Coinitial vectors:** Since they all meet and start at the same common corner.
2. **Non-coplanar vectors:** Because they form the edges of a 3D solid, they cannot all lie in a single flat 2D plane. (Any two of them are coplanar, but all three together are not).
</details>

---

### Type 2: Finding Unit Vector in a Given Direction ⭐
**Pattern:** "Find the unit vector in the direction of vector $\vec{a}$, or find a vector of magnitude $M$ in the direction of $\vec{a}$."

**Solved Example** 🟡
> Find a vector of magnitude 7 units in the direction of the vector $\vec{a} = \hat{i} - 2\hat{j} + 2\hat{k}$.
<details><summary><b>Solution</b></summary>
**Step 1: Find the magnitude of the given vector.**
$|\vec{a}| = \sqrt{1^2 + (-2)^2 + 2^2}$
$|\vec{a}| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$

**Step 2: Find the unit vector $\hat{a}$.**
The unit vector represents the pure direction of $\vec{a}$.
$\hat{a} = \frac{\vec{a}}{|\vec{a}|} = \frac{\hat{i} - 2\hat{j} + 2\hat{k}}{3}$
$\hat{a} = \frac{1}{3}\hat{i} - \frac{2}{3}\hat{j} + \frac{2}{3}\hat{k}$

**Step 3: Multiply the unit vector by the desired magnitude.**
We want a vector $\vec{v}$ with magnitude 7 in the same direction.
$\vec{v} = 7 \hat{a} = 7 \left( \frac{1}{3}\hat{i} - \frac{2}{3}\hat{j} + \frac{2}{3}\hat{k} \right)$
$\vec{v} = \frac{7}{3}\hat{i} - \frac{14}{3}\hat{j} + \frac{14}{3}\hat{k}$
</details>

**Practice:**
1. 🟢 Find the unit vector in the direction of $\vec{a} = 3\hat{i} + 4\hat{j}$.
<details><summary><b>Answer</b></summary>
Magnitude $|\vec{a}| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5$.
Unit vector $\hat{a} = \frac{3\hat{i} + 4\hat{j}}{5} = \frac{3}{5}\hat{i} + \frac{4}{5}\hat{j}$.
</details>

2. 🟢 Find the unit vector in the direction of $\vec{b} = 2\hat{i} - \hat{j} + 2\hat{k}$.
<details><summary><b>Answer</b></summary>
Magnitude $|\vec{b}| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4+1+4} = \sqrt{9} = 3$.
Unit vector $\hat{b} = \frac{2\hat{i} - \hat{j} + 2\hat{k}}{3} = \frac{2}{3}\hat{i} - \frac{1}{3}\hat{j} + \frac{2}{3}\hat{k}$.
</details>

3. 🟢 What is the magnitude of the vector $\hat{i} + \hat{j} + \hat{k}$? Is it a unit vector?
<details><summary><b>Answer</b></summary>
Magnitude = $\sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$.
Since the magnitude is not exactly 1, it is **not** a unit vector.
</details>

4. 🟡 Find a vector in the direction of vector $\vec{p} = 5\hat{i} - \hat{j} + 2\hat{k}$ which has a magnitude of 8 units.
<details><summary><b>Answer</b></summary>
$|\vec{p}| = \sqrt{25 + 1 + 4} = \sqrt{30}$.
Unit vector $\hat{p} = \frac{5\hat{i} - \hat{j} + 2\hat{k}}{\sqrt{30}}$.
Required vector = $8\hat{p} = \frac{40}{\sqrt{30}}\hat{i} - \frac{8}{\sqrt{30}}\hat{j} + \frac{16}{\sqrt{30}}\hat{k}$.
</details>

5. 🟡 Let $\vec{a} = 2\hat{i} + 2\hat{j} - 5\hat{k}$ and $\vec{b} = 2\hat{i} + \hat{j} + 3\hat{k}$. Find the unit vector parallel to the resultant of vectors $\vec{a}$ and $\vec{b}$.
<details><summary><b>Answer</b></summary>
Resultant $\vec{R} = \vec{a} + \vec{b} = (2+2)\hat{i} + (2+1)\hat{j} + (-5+3)\hat{k} = 4\hat{i} + 3\hat{j} - 2\hat{k}$.
$|\vec{R}| = \sqrt{16 + 9 + 4} = \sqrt{29}$.
Unit vector $\hat{R} = \frac{4\hat{i} + 3\hat{j} - 2\hat{k}}{\sqrt{29}}$.
</details>

6. 🔴 Find the vector of magnitude 5 which is anti-parallel (opposite direction) to $\vec{v} = -3\hat{i} + 4\hat{j}$.
<details><summary><b>Answer</b></summary>
$|\vec{v}| = \sqrt{(-3)^2 + 4^2} = 5$.
Unit vector in direction of $\vec{v}$ is $\hat{v} = \frac{-3\hat{i} + 4\hat{j}}{5}$.
Anti-parallel means we multiply by $-5$ instead of $+5$.
Required vector = $-5 \times \hat{v} = -5 \times \left( \frac{-3\hat{i} + 4\hat{j}}{5} \right) = -(-3\hat{i} + 4\hat{j}) = 3\hat{i} - 4\hat{j}$.
</details>

7. 🔴 If $\hat{a} = c\hat{i} + \frac{1}{2}\hat{j} + \frac{1}{2}\hat{k}$ is a unit vector, find the value of $c$.
<details><summary><b>Answer</b></summary>
Since $\hat{a}$ is a unit vector, its magnitude must be exactly 1.
$|\hat{a}|^2 = 1 \implies c^2 + \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = 1$
$c^2 + \frac{1}{4} + \frac{1}{4} = 1 \implies c^2 + \frac{1}{2} = 1 \implies c^2 = \frac{1}{2}$
$c = \pm\frac{1}{\sqrt{2}}$.
</details>

---

### Type 3: Collinear vs Equal Vector Conditions ⭐
**Pattern:** "Find unknowns if two vectors are equal, or show that vectors are collinear by extracting a scalar multiple."

**Solved Example** 🔴
> Show that the points $A(1, 2, 7)$, $B(2, 6, 3)$, and $C(3, 10, -1)$ are collinear.
<details><summary><b>Solution</b></summary>
Points are collinear if they lie on the same straight line. This means the vector formed by A to B ($\vec{AB}$) must be parallel (collinear) to the vector formed by B to C ($\vec{BC}$).

**Step 1: Find vector $\vec{AB}$**
$\vec{AB} = (\text{Position of } B) - (\text{Position of } A)$
$\vec{AB} = (2-1)\hat{i} + (6-2)\hat{j} + (3-7)\hat{k} = \hat{i} + 4\hat{j} - 4\hat{k}$

**Step 2: Find vector $\vec{BC}$**
$\vec{BC} = (\text{Position of } C) - (\text{Position of } B)$
$\vec{BC} = (3-2)\hat{i} + (10-6)\hat{j} + (-1-3)\hat{k} = \hat{i} + 4\hat{j} - 4\hat{k}$

**Step 3: Check condition of collinearity ($\vec{a} = \lambda\vec{b}$)**
Here, $\vec{AB} = \vec{BC}$ (they are exactly equal, so $\lambda = 1$). 
Since $\vec{AB}$ and $\vec{BC}$ are parallel and share the common point $B$, the points $A, B$, and $C$ must lie on the exact same straight line. Hence, they are collinear.
</details>

**Practice:**
1. 🟢 Find the values of $x$ and $y$ so that the vectors $2\hat{i} + 3\hat{j}$ and $x\hat{i} + y\hat{j}$ are equal.
<details><summary><b>Answer</b></summary>
Two vectors are equal if and only if their corresponding scalar components are perfectly identical.
Therefore, $x = 2$ and $y = 3$.
</details>

2. 🟢 Are vectors $\vec{a} = \hat{i} + 2\hat{j}$ and $\vec{b} = 2\hat{i} + 4\hat{j}$ equal?
<details><summary><b>Answer</b></summary>
No. For vectors to be equal, their corresponding components must be exactly identical. Here $1 \neq 2$ and $2 \neq 4$. (They are collinear, however, because $\vec{b} = 2\vec{a}$).
</details>

3. 🟡 Show that the vectors $2\hat{i} - 3\hat{j} + 4\hat{k}$ and $-4\hat{i} + 6\hat{j} - 8\hat{k}$ are collinear.
<details><summary><b>Answer</b></summary>
Let $\vec{a} = 2\hat{i} - 3\hat{j} + 4\hat{k}$ and $\vec{b} = -4\hat{i} + 6\hat{j} - 8\hat{k}$.
Notice that we can factor out $-2$ from $\vec{b}$:
$\vec{b} = -2(2\hat{i} - 3\hat{j} + 4\hat{k}) = -2\vec{a}$.
Since $\vec{b} = \lambda\vec{a}$ (with $\lambda = -2$), the vectors are collinear.
</details>

4. 🟡 Find the value of $\lambda$ if the vectors $\hat{i} - \lambda\hat{j} + 3\hat{k}$ and $2\hat{i} - 6\hat{j} + 6\hat{k}$ are collinear.
<details><summary><b>Answer</b></summary>
For collinearity, ratios of components must be equal:
$\frac{1}{2} = \frac{-\lambda}{-6} = \frac{3}{6}$
$\frac{1}{2} = \frac{\lambda}{6}$
$\lambda = 3$.
</details>

5. 🟡 Two vectors have the same magnitude. Are they necessarily equal? Give a counter-example.
<details><summary><b>Answer</b></summary>
No. Equality requires both same magnitude AND same direction.
Counter-example: $\vec{a} = 3\hat{i} + 4\hat{j}$ (magnitude 5) and $\vec{b} = 4\hat{i} + 3\hat{j}$ (magnitude 5). They have the same length but point in completely different directions, so $\vec{a} \neq \vec{b}$.
</details>

6. 🔴 The position vectors of points P, Q, R are $2\hat{i}+\hat{j}-\hat{k}$, $3\hat{i}-2\hat{j}+\hat{k}$, and $\hat{i}+4\hat{j}-3\hat{k}$ respectively. Show that P, Q, R are collinear.
<details><summary><b>Answer</b></summary>
$\vec{PQ} = (3-2)\hat{i} + (-2-1)\hat{j} + (1-(-1))\hat{k} = \hat{i} - 3\hat{j} + 2\hat{k}$.
$\vec{PR} = (1-2)\hat{i} + (4-1)\hat{j} + (-3-(-1))\hat{k} = -\hat{i} + 3\hat{j} - 2\hat{k}$.
Here, $\vec{PR} = -1(\vec{PQ})$.
Since $\vec{PR} = \lambda\vec{PQ}$ and they share the common starting point P, the points P, Q, R are collinear.
</details>

7. 🔴 If $\vec{a}$ and $\vec{b}$ are non-collinear vectors, and $x\vec{a} + y\vec{b} = \vec{0}$, what can you say about scalars $x$ and $y$?
<details><summary><b>Answer</b></summary>
If $\vec{a}$ and $\vec{b}$ are non-collinear, they point in fundamentally different directions. The only way their linear combination can cancel out to yield the zero vector is if both scalars are zero. 
Therefore, $x = 0$ and $y = 0$. (This is a foundational property of linearly independent vectors).
</details>

---

### Type 4: Conceptual Definitions and Edge Cases ⭐
**Pattern:** "Tricky questions targeting the zero vector, unit vector dimensions, and theoretical definitions."

**Solved Example** 🟡
> **Assertion (A):** The zero vector has no specific direction.
> **Reason (R):** The magnitude of a zero vector is zero, so its initial and terminal points coincide.
> Evaluate the assertion and reason.
<details><summary><b>Solution</b></summary>
The zero vector ($\vec{0}$) is mathematically defined as a vector with zero magnitude. Because its initial point and terminal point are the exact same location in space, no "line segment" or arrow is formed. Without an arrow, it is physically impossible to define a direction. Therefore, its direction is considered arbitrary or indeterminate.
Both A and R are true, and R correctly explains A. 
**Answer: Both A and R are true and R is the correct explanation of A.**
</details>

**Practice:**
1. 🟢 What is the magnitude of the vector $\vec{A} - \vec{A}$?
<details><summary><b>Answer</b></summary>
The subtraction yields the zero vector $\vec{0}$. The magnitude of the zero vector is exactly $0$.
</details>

2. 🟢 True or False: A unit vector has a magnitude of 1 meter.
<details><summary><b>Answer</b></summary>
**False.** A unit vector is dimensionless. It has a magnitude of exactly 1 (a pure number), without any physical units. It is purely a directional pointer.
</details>

3. 🟡 If $\vec{a}$ is a non-zero vector, what is the geometric meaning of $\frac{\vec{a}}{|\vec{a}|}$?
<details><summary><b>Answer</b></summary>
It represents the unit vector $\hat{a}$, which geometrically gives the pure direction of vector $\vec{a}$ stripped of all magnitude or length information.
</details>

4. 🟡 Can the magnitude of a vector be negative? Why or why not?
<details><summary><b>Answer</b></summary>
No. Magnitude represents the geometric "length" of the vector, which is an absolute distance. It is calculated using the square root of a sum of squares ($\sqrt{x^2+y^2+z^2}$), which always yields a non-negative real number. 
</details>

5. 🔴 Are the vectors $\vec{a}$ and $-\vec{a}$ collinear? 
<details><summary><b>Answer</b></summary>
Yes. They lie on the same line (or parallel lines) but point in exactly opposite directions. Since $-\vec{a} = (-1)\vec{a}$, they satisfy the standard collinearity condition $\vec{b} = \lambda\vec{a}$ with $\lambda = -1$.
</details>

6. 🔴 Two vectors are parallel. Do they have to be equal? 
<details><summary><b>Answer</b></summary>
No. Parallel (collinear) vectors only share the same or opposite line of action. They can have wildly different magnitudes and can point in opposite directions. Equality requires exact same magnitude and exact same direction.
</details>

7. 🔴 If displacement is a vector, is "distance" the magnitude of the displacement vector?
<details><summary><b>Answer</b></summary>
Not always. Magnitude of displacement gives the shortest straight-line distance between the initial and final points. "Distance" (as a scalar) is the total path length traveled, which could be larger if the path is curved. They are only equal if the object moves in a perfectly straight line without ever turning back.
</details>

---

### Type 5: Coplanar, Free, Bound, and Sliding Vectors ⭐
**Pattern:** "Advanced categorizations used in 3D geometry and Physics mechanics."

**Solved Example** 🔴
> Check whether the vectors $\vec{a} = \hat{i} + 3\hat{j} + \hat{k}$, $\vec{b} = 2\hat{i} - \hat{j} - \hat{k}$, and $\vec{c} = 7\hat{j} + 3\hat{k}$ are coplanar.
<details><summary><b>Solution</b></summary>
Three vectors are coplanar if their scalar triple product (the determinant of their components) is zero.

**Step 1: Set up the determinant.**
$D = \begin{vmatrix} 1 & 3 & 1 \\ 2 & -1 & -1 \\ 0 & 7 & 3 \end{vmatrix}$
*(Note: $\vec{c}$ has no $\hat{i}$ component, so we write 0).*

**Step 2: Expand the determinant along the first row.**
$D = 1((-1)(3) - (-1)(7)) - 3((2)(3) - (-1)(0)) + 1((2)(7) - (-1)(0))$
$D = 1(-3 + 7) - 3(6 - 0) + 1(14 - 0)$
$D = 1(4) - 3(6) + 14$
$D = 4 - 18 + 14 = 0$

**Step 3: Conclusion.**
Since the determinant is zero, the three vectors are linearly dependent and lie in the exact same plane. They are coplanar.
</details>

**Practice:**
1. 🟢 How many minimum vectors are always guaranteed to be coplanar?
<details><summary><b>Answer</b></summary>
Any **two** vectors are always coplanar. You can always pass a flat 2D plane through any two intersecting lines (by translating their tails together). Coplanarity only becomes a question when there are three or more vectors.
</details>

2. 🟢 A force of 10N is applied to a specific hinge on a door to rotate it. Is this force a free vector or a bound vector?
<details><summary><b>Answer</b></summary>
It is a **bound vector** (or localized vector). Its effect (torque) depends entirely on its specific point of application (the hinge). If you translate the force to the middle of the door, it will have a drastically different physical effect.
</details>

3. 🟡 A vector $\vec{v}$ represents the uniform velocity of wind blowing across a flat field. Is this a free vector or a bound vector?
<details><summary><b>Answer</b></summary>
It is a **free vector**. The wind velocity is the same everywhere in the field. You can represent it with an arrow anywhere on your map, and it holds the exact same meaning.
</details>

4. 🟡 Find the value of $x$ for which the vectors $\vec{a} = 2\hat{i} - \hat{j} + \hat{k}$, $\vec{b} = \hat{i} + 2\hat{j} - 3\hat{k}$, and $\vec{c} = 3\hat{i} + x\hat{j} + 5\hat{k}$ are coplanar.
<details><summary><b>Answer</b></summary>
Set the determinant to zero:
$\begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -3 \\ 3 & x & 5 \end{vmatrix} = 0$
$2(10 + 3x) - (-1)(5 + 9) + 1(x - 6) = 0$
$20 + 6x + 14 + x - 6 = 0$
$7x + 28 = 0 \implies 7x = -28 \implies x = -4$.
</details>

5. 🔴 Are the points $A(1, 2, -1)$, $B(2, 3, 1)$, $C(3, -1, 2)$ and $D(4, 0, 4)$ coplanar? (Hint: Form three vectors from a common point).
<details><summary><b>Answer</b></summary>
Form vectors starting from A: $\vec{AB}, \vec{AC}, \vec{AD}$.
$\vec{AB} = \hat{i} + \hat{j} + 2\hat{k}$
$\vec{AC} = 2\hat{i} - 3\hat{j} + 3\hat{k}$
$\vec{AD} = 3\hat{i} - 2\hat{j} + 5\hat{k}$
Check determinant:
$\begin{vmatrix} 1 & 1 & 2 \\ 2 & -3 & 3 \\ 3 & -2 & 5 \end{vmatrix} = 1(-15+6) - 1(10-9) + 2(-4+9) = 1(-9) - 1(1) + 2(5) = -9 - 1 + 10 = 0$.
Since the vectors $\vec{AB}, \vec{AC}, \vec{AD}$ are coplanar, the points A, B, C, D all lie on the exact same plane. They are coplanar points.
</details>

6. 🔴 What is a "Sliding Vector"? Give a mechanics example.
<details><summary><b>Answer</b></summary>
A sliding vector is one whose point of application can be moved anywhere along its *line of action* without changing its external effect on a rigid body. 
**Example:** Pushing a block with a stick from behind (force applied at back) has the same translational effect as pulling it with a string from the front (force applied at front), as long as the line of action is identical.
</details>

7. 🔴 If $\vec{a}, \vec{b}, \vec{c}$ are non-coplanar vectors, can any vector $\vec{r}$ in 3D space be written as their linear combination?
<details><summary><b>Answer</b></summary>
Yes. If three vectors are non-coplanar, they break out of the 2D plane and form a full basis for 3D space. Any vector $\vec{r}$ can be uniquely expressed as $\vec{r} = x\vec{a} + y\vec{b} + z\vec{c}$ for some scalars $x, y, z$. (This is exactly why we use $\hat{i}, \hat{j}, \hat{k}$ as our standard basis, since they are mutually perpendicular and non-coplanar!).
</details>

---

## 🧱 Stage 4: MCQ Mastery

**1. A vector having magnitude zero and an arbitrary direction is called:**
(a) Unit Vector
(b) Equal Vector
(c) Null Vector
(d) Free Vector
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (c) Null Vector**
Explanation: A vector with zero magnitude is called a null or zero vector ($\vec{0}$). Because it has no length, it doesn't "point" anywhere, so its direction is considered arbitrary or undefined.
</details>

**2. Which of the following is true for two equal vectors?**
(a) They must have the same magnitude only.
(b) They must have the same direction only.
(c) They must have both the same magnitude and the same direction.
(d) They must have the same initial point.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (c)**
Explanation: Equality of vectors is a strict condition. $\vec{a} = \vec{b}$ implies both $|\vec{a}| = |\vec{b}|$ and they point in the exact same direction. They do *not* need the same initial point (unless they are bound vectors).
</details>

**3. The vectors $2\hat{i} + 3\hat{j} - \hat{k}$ and $-4\hat{i} - 6\hat{j} + 2\hat{k}$ are:**
(a) Equal
(b) Collinear
(c) Coplanar but not collinear
(d) Orthogonal (perpendicular)
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (b) Collinear**
Explanation: Let $\vec{a} = 2\hat{i} + 3\hat{j} - \hat{k}$ and $\vec{b} = -4\hat{i} - 6\hat{j} + 2\hat{k}$.
Notice that $\vec{b} = -2(2\hat{i} + 3\hat{j} - \hat{k}) = -2\vec{a}$. Since $\vec{b} = \lambda\vec{a}$, they are collinear (specifically, unlike parallel vectors).
</details>

**4. Assertion (A): The unit vector of a given vector has the same unit (e.g., meters or Newtons) as the original vector.**
**Reason (R): Unit vector is calculated by dividing a vector by its own magnitude.**
(a) Both A and R are true and R is the correct explanation of A.
(b) Both A and R are true but R is NOT the correct explanation of A.
(c) A is true but R is false.
(d) A is false but R is true.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (d)**
Explanation: The assertion is false. A unit vector has NO physical units. Because you divide the vector (e.g., $10\text{ m North}$) by its magnitude ($10\text{ m}$), the units cancel out, leaving just the pure dimensionless direction. The reason is true; $\hat{a} = \vec{a}/|\vec{a}|$.
</details>

**5. Any two non-zero, non-collinear vectors are always:**
(a) Coinitial
(b) Coplanar
(c) Equal
(d) Perpendicular
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (b) Coplanar**
Explanation: In 3D space, any two vectors can always be contained within a single flat plane (you can translate them so their tails touch, defining a plane). 
</details>

**6. If $\vec{a} = \hat{i} + \hat{j}$, what is the unit vector $\hat{a}$?**
(a) $\hat{i} + \hat{j}$
(b) $\frac{1}{2}\hat{i} + \frac{1}{2}\hat{j}$
(c) $\frac{1}{\sqrt{2}}\hat{i} + \frac{1}{\sqrt{2}}\hat{j}$
(d) $\sqrt{2}\hat{i} + \sqrt{2}\hat{j}$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (c)**
Explanation: $|\vec{a}| = \sqrt{1^2 + 1^2} = \sqrt{2}$. Unit vector = $\frac{\vec{a}}{|\vec{a}|} = \frac{\hat{i} + \hat{j}}{\sqrt{2}} = \frac{1}{\sqrt{2}}\hat{i} + \frac{1}{\sqrt{2}}\hat{j}$.
</details>

**7. Statement I: If two vectors have the same magnitude, they must be equal.**
**Statement II: If two vectors are equal, they must have the same magnitude.**
(a) Both Statements are true.
(b) Both Statements are false.
(c) Statement I is true, Statement II is false.
(d) Statement I is false, Statement II is true.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (d)**
Explanation: Statement I is a classic trap. Vectors with the same magnitude can point in different directions, so they aren't necessarily equal. Statement II is fundamentally true; equality requires identical magnitude and direction.
</details>

**8. Which of the following conditions implies that vectors $\vec{x}$ and $\vec{y}$ are collinear?**
(a) $\vec{x} \cdot \vec{y} = 0$
(b) $\vec{x} + \vec{y} = \vec{0}$
(c) $\vec{x} = k\vec{y}$ for some scalar $k \neq 0$
(d) Both (b) and (c)
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (d) Both (b) and (c)**
Explanation: Condition (c) is the standard algebraic definition of collinearity. Condition (b) implies $\vec{x} = -\vec{y}$, which means they are anti-parallel (unlike parallel), so they are also collinear. Condition (a) implies they are perpendicular.
</details>

**9. For a localized (bound) vector, which of the following is fixed and cannot be changed?**
(a) Magnitude
(b) Direction
(c) Initial point
(d) All of the above
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (d)**
Explanation: A bound vector is completely fixed in space. Its magnitude and direction are fixed, and most importantly, its initial point (point of application) is completely anchored and cannot be translated freely.
</details>

**10. Three vectors $\vec{a}$, $\vec{b}$, $\vec{c}$ form the sides of a triangle in order (head of first to tail of second, etc). Which of the following is true?**
(a) They are equal vectors.
(b) Their sum is the zero vector.
(c) They are collinear.
(d) They are unit vectors.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (b)**
Explanation: If vectors form a closed polygon taken in the same continuous order, you start at a point and return exactly to that same point. The net displacement is zero. Hence $\vec{a} + \vec{b} + \vec{c} = \vec{0}$.
</details>

---

## 🔀 Stage 5: Type Mixer

**Problem 1: Hexagon Mechanics**
Let $ABCDEF$ be a regular hexagon with center $O$. Prove that $\vec{AB} + \vec{AC} + \vec{AD} + \vec{AE} + \vec{AF} = 6\vec{AO}$.
<details><summary><b>Solution</b></summary>
In a regular hexagon, the center $O$ bisects the main diagonals. 
Let's express everything in terms of vectors originating from the center O. 
For any point P, $\vec{AP} = \vec{AO} + \vec{OP}$.
$\vec{AB} = \vec{AO} + \vec{OB}$
$\vec{AC} = \vec{AO} + \vec{OC}$
$\vec{AD} = \vec{AO} + \vec{OD}$
$\vec{AE} = \vec{AO} + \vec{OE}$
$\vec{AF} = \vec{AO} + \vec{OF}$

Summing them all together:
Sum $= 5\vec{AO} + (\vec{OB} + \vec{OC} + \vec{OD} + \vec{OE} + \vec{OF})$

Since $O$ is the geometric center of symmetry, the vectors pointing from $O$ to all six vertices are perfectly balanced and sum to the zero vector:
$\vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} + \vec{OE} + \vec{OF} = \vec{0}$
So, $(\vec{OB} + \vec{OC} + \vec{OD} + \vec{OE} + \vec{OF}) = -\vec{OA} = \vec{AO}$.

Substituting this back into our original sum:
Sum $= 5\vec{AO} + \vec{AO} = 6\vec{AO}$.
*(This beautifully combines equal vectors, coinitial vector expansion, and the concept of zero net sum).*
</details>

**Problem 2: The Collinear Unit Trap**
Vectors $\vec{a} = 2\hat{i} + p\hat{j} + \hat{k}$ and $\vec{b} = -4\hat{i} + 6\hat{j} + q\hat{k}$ are collinear. Find the values of $p$ and $q$, and then find the unit vector in the direction of $\vec{a}$.
<details><summary><b>Solution</b></summary>
**Step 1: Find $p$ and $q$ using collinearity.**
For collinear vectors, corresponding components are strictly proportional:
$\frac{2}{-4} = \frac{p}{6} = \frac{1}{q}$
$-\frac{1}{2} = \frac{p}{6} \implies 2p = -6 \implies p = -3$.
$-\frac{1}{2} = \frac{1}{q} \implies q = -2$.

**Step 2: Write vector $\vec{a}$ and find its unit vector.**
Substitute $p = -3$:
$\vec{a} = 2\hat{i} - 3\hat{j} + \hat{k}$.
Magnitude $|\vec{a}| = \sqrt{2^2 + (-3)^2 + 1^2} = \sqrt{4 + 9 + 1} = \sqrt{14}$.
Unit vector $\hat{a} = \frac{\vec{a}}{|\vec{a}|} = \frac{1}{\sqrt{14}}(2\hat{i} - 3\hat{j} + \hat{k})$.
</details>

**Problem 3: Unknown Plane Equation (Coplanar Vectors)**
Find $\lambda$ such that the four points $A(3, 2, 1)$, $B(4, \lambda, 5)$, $C(4, 2, -2)$, and $D(6, 5, -1)$ are coplanar.
<details><summary><b>Solution</b></summary>
**Step 1: Form 3 coinitial vectors from point A.**
$\vec{AB} = (4-3)\hat{i} + (\lambda-2)\hat{j} + (5-1)\hat{k} = \hat{i} + (\lambda-2)\hat{j} + 4\hat{k}$
$\vec{AC} = (4-3)\hat{i} + (2-2)\hat{j} + (-2-1)\hat{k} = \hat{i} + 0\hat{j} - 3\hat{k}$
$\vec{AD} = (6-3)\hat{i} + (5-2)\hat{j} + (-1-1)\hat{k} = 3\hat{i} + 3\hat{j} - 2\hat{k}$

**Step 2: Apply coplanar condition (Determinant = 0).**
$\begin{vmatrix} 1 & \lambda-2 & 4 \\ 1 & 0 & -3 \\ 3 & 3 & -2 \end{vmatrix} = 0$
Expanding along the second row (because it has a convenient zero):
$-1((\lambda-2)(-2) - 12) + 0 - (-3)(1(3) - 3(\lambda-2)) = 0$
$-1(-2\lambda + 4 - 12) + 3(3 - 3\lambda + 6) = 0$
$2\lambda + 8 + 3(9 - 3\lambda) = 0$
$2\lambda + 8 + 27 - 9\lambda = 0$
$-7\lambda + 35 = 0 \implies 7\lambda = 35 \implies \lambda = 5$.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1 (1 Mark). Define a zero vector and state its direction.**
<details><summary><b>Model Answer</b></summary>
A zero vector (or null vector) is a vector whose magnitude is exactly zero, which occurs when its initial and terminal points coincide. It is denoted by $\vec{0}$. Because it has no length, it cannot point in any specific way; therefore, its direction is indeterminate or arbitrary.
</details>

**Q2 (1 Mark). Write two vectors having the same magnitude but different directions.**
<details><summary><b>Model Answer</b></summary>
Let $\vec{a} = \hat{i} + \hat{j}$ and $\vec{b} = \hat{i} - \hat{j}$.
Magnitude of $\vec{a} = \sqrt{1^2+1^2} = \sqrt{2}$.
Magnitude of $\vec{b} = \sqrt{1^2+(-1)^2} = \sqrt{2}$.
Both have the same magnitude ($\sqrt{2}$) but their directions are completely different (they point into different quadrants).
</details>

**Q3 (2 Marks). Find the unit vector in the direction of vector $\vec{a} = 2\hat{i} + 3\hat{j} + \hat{k}$. (CBSE)**
<details><summary><b>Model Answer</b></summary>
**Step 1:** Find the magnitude of $\vec{a}$.
$|\vec{a}| = \sqrt{2^2 + 3^2 + 1^2} = \sqrt{4 + 9 + 1} = \sqrt{14}$. [1/2 mark]
**Step 2:** Apply the unit vector formula.
$\hat{a} = \frac{\vec{a}}{|\vec{a}|}$ [1/2 mark]
$\hat{a} = \frac{2\hat{i} + 3\hat{j} + \hat{k}}{\sqrt{14}} = \frac{2}{\sqrt{14}}\hat{i} + \frac{3}{\sqrt{14}}\hat{j} + \frac{1}{\sqrt{14}}\hat{k}$. [1 mark]
</details>

**Q4 (2 Marks). Show that the vectors $\vec{A} = 2\hat{i} - 3\hat{j} + 4\hat{k}$ and $\vec{B} = -4\hat{i} + 6\hat{j} - 8\hat{k}$ are collinear. (CBSE)**
<details><summary><b>Model Answer</b></summary>
Vectors are collinear if they can be written as $\vec{A} = \lambda\vec{B}$.
We have $\vec{B} = -4\hat{i} + 6\hat{j} - 8\hat{k}$.
Factoring out $-2$, we get:
$\vec{B} = -2(2\hat{i} - 3\hat{j} + 4\hat{k})$ [1 mark]
$\vec{B} = -2\vec{A}$. 
Since $\vec{B}$ is a scalar multiple of $\vec{A}$ (here $\lambda = -2$), the vectors $\vec{A}$ and $\vec{B}$ are collinear. [1 mark]
</details>

**Q5 (4 Marks). If points $A(1, -2, -8)$, $B(5, 0, -2)$ and $C(11, 3, 7)$ are collinear, find the ratio in which B divides AC.**
<details><summary><b>Model Answer</b></summary>
**Step 1: Find vectors $\vec{AB}$ and $\vec{BC}$.**
$\vec{AB} = (5-1)\hat{i} + (0-(-2))\hat{j} + (-2-(-8))\hat{k} = 4\hat{i} + 2\hat{j} + 6\hat{k}$ [1 mark]
$\vec{BC} = (11-5)\hat{i} + (3-0)\hat{j} + (7-(-2))\hat{k} = 6\hat{i} + 3\hat{j} + 9\hat{k}$ [1 mark]
**Step 2: Find relationship to prove collinearity.**
Notice that $\vec{AB} = 2(2\hat{i} + \hat{j} + 3\hat{k})$ and $\vec{BC} = 3(2\hat{i} + \hat{j} + 3\hat{k})$.
Therefore, $\frac{\vec{AB}}{2} = \frac{\vec{BC}}{3} \implies \vec{AB} = \frac{2}{3}\vec{BC}$.
Since they share point B and are parallel, they are collinear. [1 mark]
**Step 3: Find the ratio.**
The ratio of the lengths is $|\vec{AB}| : |\vec{BC}|$.
Since $\vec{AB} = \frac{2}{3}\vec{BC}$, $|\vec{AB}| = \frac{2}{3}|\vec{BC}|$.
Therefore, $|\vec{AB}| / |\vec{BC}| = 2/3$.
B divides AC in the ratio $2:3$. [1 mark]
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**1. Let $\vec{a}, \vec{b}$ and $\vec{c}$ be three non-zero vectors such that no two of them are collinear and $(\vec{a} \times \vec{b}) \times \vec{c} = \frac{1}{3}|\vec{b}||\vec{c}|\vec{a}$. If $\theta$ is the angle between vectors $\vec{b}$ and $\vec{c}$, then a value of $\sin\theta$ is:**
&emsp;(a) $\frac{2\sqrt{2}}{3}$
&emsp;(b) $\frac{-\sqrt{2}}{3}$
&emsp;(c) $\frac{2}{3}$
&emsp;(d) $\frac{-2\sqrt{3}}{3}$
<details><summary><b>Answer</b></summary>
*(Note: This problem combines collinearity logic with the Vector Triple Product formula from later stages)*
**Answer: (a) $\frac{2\sqrt{2}}{3}$**
Explanation: Using the standard Vector Triple Product formula: $(\vec{a} \times \vec{b}) \times \vec{c} = (\vec{a}\cdot\vec{c})\vec{b} - (\vec{b}\cdot\vec{c})\vec{a}$.
Given this expression equals $\frac{1}{3}|\vec{b}||\vec{c}|\vec{a}$.
So, $(\vec{a}\cdot\vec{c})\vec{b} - (\vec{b}\cdot\vec{c})\vec{a} = \frac{1}{3}|\vec{b}||\vec{c}|\vec{a}$.
Since $\vec{a}$ and $\vec{b}$ are strictly non-collinear, we can directly compare their coefficients.
Coefficient of $\vec{b}$ on left must equal coefficient on right (which is 0) $\implies \vec{a}\cdot\vec{c} = 0$.
Coefficient of $\vec{a}$ gives: $-(\vec{b}\cdot\vec{c}) = \frac{1}{3}|\vec{b}||\vec{c}|$.
Using dot product definition: $-|\vec{b}||\vec{c}|\cos\theta = \frac{1}{3}|\vec{b}||\vec{c}| \implies \cos\theta = -\frac{1}{3}$.
We need $\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \frac{1}{9}} = \sqrt{\frac{8}{9}} = \frac{2\sqrt{2}}{3}$.
</details>

**2. If $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = 4\hat{i} + 3\hat{j} + 4\hat{k}$, and $\vec{c} = \hat{i} + \alpha\hat{j} + \beta\hat{k}$ are linearly dependent (coplanar) vectors and $|\vec{c}| = \sqrt{3}$, then which of the following is true?**
&emsp;(a) $\alpha = 1, \beta = -1$
&emsp;(b) $\alpha = 1, \beta = \pm 1$
&emsp;(c) $\alpha = -1, \beta = \pm 1$
&emsp;(d) $\alpha = \pm 1, \beta = 1$
<details><summary><b>Answer</b></summary>
**Answer: (d) $\alpha = \pm 1, \beta = 1$**
Explanation: Coplanar (linearly dependent) vectors have a scalar triple product determinant of 0:
$\begin{vmatrix} 1 & 1 & 1 \\ 4 & 3 & 4 \\ 1 & \alpha & \beta \end{vmatrix} = 0$
Expanding along row 1: $1(3\beta - 4\alpha) - 1(4\beta - 4) + 1(4\alpha - 3) = 0$
$3\beta - 4\alpha - 4\beta + 4 + 4\alpha - 3 = 0$
$-\beta + 1 = 0 \implies \beta = 1$.
Now we use the magnitude condition $|\vec{c}| = \sqrt{3}$:
$\sqrt{1^2 + \alpha^2 + \beta^2} = \sqrt{3}$
Substitute $\beta = 1$: $1 + \alpha^2 + 1^2 = 3 \implies \alpha^2 = 1 \implies \alpha = \pm 1$.
Therefore, $\beta = 1$ and $\alpha = \pm 1$.
</details>

**3. Let $\hat{a}$ and $\hat{b}$ be two unit vectors. If the vectors $\vec{c} = \hat{a} + 2\hat{b}$ and $\vec{d} = 5\hat{a} - 4\hat{b}$ are perpendicular to each other, then the angle between $\hat{a}$ and $\hat{b}$ is:**
&emsp;(a) $\frac{\pi}{6}$
&emsp;(b) $\frac{\pi}{2}$
&emsp;(c) $\frac{\pi}{3}$
&emsp;(d) $\frac{\pi}{4}$
<details><summary><b>Answer</b></summary>
**Answer: (c) $\frac{\pi}{3}$**
Explanation: Perpendicular vectors always have a dot product of zero.
$(\hat{a} + 2\hat{b}) \cdot (5\hat{a} - 4\hat{b}) = 0$
$5(\hat{a}\cdot\hat{a}) - 4(\hat{a}\cdot\hat{b}) + 10(\hat{b}\cdot\hat{a}) - 8(\hat{b}\cdot\hat{b}) = 0$.
Since $\hat{a}$ and $\hat{b}$ are defined as unit vectors, $\hat{a}\cdot\hat{a} = |\hat{a}|^2 = 1$ and $\hat{b}\cdot\hat{b} = 1$. Let $\theta$ be the angle between them, so $\hat{a}\cdot\hat{b} = |\hat{a}||\hat{b}|\cos\theta = (1)(1)\cos\theta = \cos\theta$.
$5(1) + 6\cos\theta - 8(1) = 0$
$6\cos\theta - 3 = 0 \implies \cos\theta = \frac{1}{2} \implies \theta = \frac{\pi}{3}$ (or $60^\circ$).
</details>

**4. A vector $\vec{r}$ of magnitude $3\sqrt{2}$ units makes equal angles with the coordinate axes. Which of the following could be $\vec{r}$?**
&emsp;(a) $3(\hat{i} + \hat{j} + \hat{k})$
&emsp;(b) $\sqrt{6}(\hat{i} + \hat{j} + \hat{k})$
&emsp;(c) $\sqrt{2}(\hat{i} + \hat{j} + \hat{k})$
&emsp;(d) $2(\hat{i} + \hat{j} + \hat{k})$
<details><summary><b>Answer</b></summary>
**Answer: (b) $\sqrt{6}(\hat{i} + \hat{j} + \hat{k})$**
Explanation: If a vector makes strictly equal angles with all three coordinate axes, its direction cosines are equal: $\cos^2\alpha + \cos^2\alpha + \cos^2\alpha = 1 \implies 3\cos^2\alpha = 1 \implies \cos\alpha = \pm\frac{1}{\sqrt{3}}$.
The pure unit vector in this direction is $\hat{r} = \frac{1}{\sqrt{3}}\hat{i} + \frac{1}{\sqrt{3}}\hat{j} + \frac{1}{\sqrt{3}}\hat{k}$.
The required vector is built by scaling the unit vector: $\vec{r} = |\vec{r}|\hat{r} = 3\sqrt{2} \left( \frac{1}{\sqrt{3}}\hat{i} + \frac{1}{\sqrt{3}}\hat{j} + \frac{1}{\sqrt{3}}\hat{k} \right) = \frac{3\sqrt{2}}{\sqrt{3}}(\hat{i} + \hat{j} + \hat{k})$.
Simplifying the fraction: $\frac{3\sqrt{2}}{\sqrt{3}} = \sqrt{3}\sqrt{2} = \sqrt{6}$.
So, $\vec{r} = \sqrt{6}(\hat{i} + \hat{j} + \hat{k})$.
</details>

---

*Next: [Chapter 3 — Vector Addition →](./03_vector_addition.md)*
