# Chapter 6: Heights & Distances

---

## Stage 1: The Core Idea

### Measuring the Unmeasurable

How do you find the height of a mountain without climbing it?<br> The width of a river without swimming across it?<br>

The answer: **triangles**.

When you look at the top of a tall object, your line of sight makes an angle with the horizontal. Measure that angle + one distance, and trigonometry gives you everything else.

### Key Concepts

```
     ╱|  Top of object
    ╱  |
   ╱   |  height
  ╱ θ  |
 ───────
  distance (base)

θ = angle of elevation (looking UP)
```

```
  Top ╲
  of  ╲  θ
  obj ╲
       ╲
        ╲
         ───────
          
θ = angle of depression (looking DOWN)
```

**Angle of Elevation** — when you look UP from horizontal to see an object.
**Angle of Depression** — when you look DOWN from horizontal to see an object.

These two are **equal** (alternate interior angles) when the line of sight is the same.

---

## Stage 2: The Formula Lab

### The Basic Setup

```
tan θ = height / distance
height = distance × tan θ
distance = height / tan θ = height × cot θ
```

### Two-Triangle Problems

Sometimes you need two triangles to find the answer:

```
      ╱|╲
     ╱ | ╲
    ╱  |  ╲ h
   ╱α  |  β╲
  ─────┴──────
     d     x
```

Here you have two triangles sharing the same height h, with different base distances. This let you solve for both h and the unknown distance.

**Angle of depression = angle of elevation** (when lines are parallel).

---

## Stage 3: Type-wise Mastery

### Type 1: Direct Application — Single Object

**Goal:** Given distance and angle, find height (or vice versa).

**Solved Example:**

A tower casts a shadow 50 m long when the sun's elevation is 30°. Find the tower's height.

**Solution:**
```
tan 30° = h/50
1/√3 = h/50
h = 50/√3 = 50√3/3 ≈ 28.87 m
```
🟢 Easy ⭐ Must-Do

---

**Practice Problems:**

1. 🟢 A vertical pole casts a shadow 20 m long when the sun's altitude is 45°. Find the pole's height.
<details>
<summary>Solution</summary>

Let the height of the vertical pole be \( h \) meters.
The length of the shadow is given as \( 20\text{ m} \).
The angle of elevation of the sun (altitude) is \( 45^\circ \).

In the right-angled triangle formed by the pole, its shadow, and the line of sight to the sun:
\[
\tan(45^\circ) = \frac{\text{Height of the pole}}{\text{Length of the shadow}}
\]
Substituting the known values:
\[
1 = \frac{h}{20} \implies h = 20\text{ m}
\]

Thus, the height of the pole is \( 20\text{ m} \).
</details>

2. 🟢 A tree 10 m high casts a shadow of length 10√3 m. Find the sun's altitude.
<details>
<summary>Solution</summary>

Let the sun's altitude (angle of elevation) be \( \theta \).
The height of the tree is \( 10\text{ m} \).
The length of the shadow cast by the tree is \( 10\sqrt{3}\text{ m} \).

In the right-angled triangle formed:
\[
\tan \theta = \frac{\text{Height of the tree}}{\text{Length of the shadow}} = \frac{10}{10\sqrt{3}} = \frac{1}{\sqrt{3}}
\]
Since \( \tan(30^\circ) = \frac{1}{\sqrt{3}} \), we have:
\[
\theta = 30^\circ
\]

Thus, the sun's altitude is \( 30^\circ \).
</details>

3. 🟡 A kite flying at a height of 75 m from the ground has a string of length 150 m. Find the angle the string makes with the ground.
<details>
<summary>Solution</summary>

Let the angle that the string makes with the ground be \( \theta \).
The vertical height of the kite from the ground is \( 75\text{ m} \).
The length of the string (hypotenuse) is \( 150\text{ m} \).

In the right-angled triangle:
\[
\sin \theta = \frac{\text{Height}}{\text{Length of string}} = \frac{75}{150} = \frac{1}{2}
\]
Since \( \sin(30^\circ) = \frac{1}{2} \), we have:
\[
\theta = 30^\circ
\]

Thus, the angle the string makes with the ground is \( 30^\circ \).
</details>

4. 🟡 An observer 1.5 m tall is 30 m away from a tower. The angle of elevation of the top of the tower from his eye is 45°. Find the tower's height.
<details>
<summary>Solution</summary>

Let \( H \) be the total height of the tower.
The height of the observer is \( 1.5\text{ m} \).
The horizontal distance between the observer and the tower is \( 30\text{ m} \).

Let \( h \) be the height of the tower above the observer's eye level.
Therefore, the total height of the tower is:
\[
H = h + 1.5
\]
In the right-angled triangle formed above the eye level:
\[
\tan(45^\circ) = \frac{h}{30}
\]
Since \( \tan(45^\circ) = 1 \):
\[
1 = \frac{h}{30} \implies h = 30\text{ m}
\]
Therefore, the total height of the tower is:
\[
H = 30 + 1.5 = 31.5\text{ m}
\]
</details>

5. 🟡 From a point 100 m from the foot of a tower, the angle of elevation of its top is 60°. Find the tower's height.
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \).
The distance from the point to the foot of the tower is \( 100\text{ m} \).
The angle of elevation of the top of the tower is \( 60^\circ \).

In the right-angled triangle:
\[
\tan(60^\circ) = \frac{h}{100}
\]
Substituting \( \tan(60^\circ) = \sqrt{3} \):
\[
\sqrt{3} = \frac{h}{100} \implies h = 100\sqrt{3}\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 100 \times 1.732 = 173.2\text{ m}
\]

Thus, the tower's height is \( 100\sqrt{3}\text{ m} \) (or approximately \( 173.2\text{ m} \)).
</details>

---

### Type 2: Two Triangles — Same Side

**Goal:** Two angles of elevation from different distances give the same height.

**Solved Example:**

From a point P on the ground, the angle of elevation of the top of a 10 m tall building is 30°. After moving 20 m towards the building, the angle becomes 60°. Find the height of the building. (Wait — we already know it's 10 m. Let me use a proper example.)

From a point 40 m from the foot of a tower, the angle of elevation is 30°. From a point 20 m closer, the angle is 60°. Both measurements point to the same tower. Find the height.

**Solution:**
```
From first point: tan 30° = h/40 → h = 40/√3
From second point: tan 60° = h/20 → h = 20√3

These should be equal. Let me verify: 
40/√3 = 20√3 → 40 = 60 → ❌

This means the data is inconsistent (as expected — it's a contrived example).

Let's do a proper one:
```

A person observes the top of a tower from two points at distances x and y from the foot, with angles of elevation α and β respectively. If the two observations are at the same level, prove that h = (x − y)/(cot β − cot α).

**Solution:**
```
From first: cot α = x/h → x = h cot α
From second: cot β = y/h → y = h cot β
x − y = h(cot α − cot β) → h = (x − y)/(cot α − cot β)

Wait, let me fix: h = (x − y)/(cot α − cot β)
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 From the top of a building, the angle of depression of a car on the ground is 30°. If the car is 50 m from the building, find the height.
<details>
<summary>Solution</summary>

Let the height of the building be \( h \) meters.
The car is at a horizontal distance of \( 50\text{ m} \) from the building.
Since the angle of depression of the car from the top of the building is \( 30^\circ \), the angle of elevation of the top of the building from the car is also \( 30^\circ \) (alternate interior angles).

In the right-angled triangle:
\[
\tan(30^\circ) = \frac{h}{50}
\]
Substituting \( \tan(30^\circ) = \frac{1}{\sqrt{3}} \):
\[
\frac{1}{\sqrt{3}} = \frac{h}{50} \implies h = \frac{50}{\sqrt{3}} = \frac{50\sqrt{3}}{3}\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 28.87\text{ m}
\]

Thus, the height of the building is \( \frac{50\sqrt{3}}{3}\text{ m} \) (or approximately \( 28.87\text{ m} \)).
</details>

7. 🟡 From the top of a 60 m tower, the angle of depression of the top and bottom of a building are 30° and 60°. Find the height of the building.
<details>
<summary>Solution</summary>

Let the height of the tower be \( AB = 60\text{ m} \).
Let the building be \( CD \) of height \( h \), where \( D \) is the foot on the ground.
Let the horizontal distance between the tower and the building be \( d \).

1. From the top of the tower \( A \), the angle of depression of the bottom of the building \( D \) is \( 60^\circ \). This implies the angle of elevation of \( A \) from \( D \) is \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{AB}{BD} \implies \sqrt{3} = \frac{60}{d} \implies d = \frac{60}{\sqrt{3}} = 20\sqrt{3}\text{ m}
   \]

2. From the top of the tower \( A \), the angle of depression of the top of the building \( C \) is \( 30^\circ \).
   Let \( E \) be the point on the tower at the same horizontal level as the top of the building \( C \).
   Then the horizontal distance \( AE = d = 20\sqrt{3}\text{ m} \), and the vertical distance is \( AE = 60 - h \).
   In the right-angled triangle formed:
   \[
   \tan(30^\circ) = \frac{60 - h}{d} \implies \frac{1}{\sqrt{3}} = \frac{60 - h}{20\sqrt{3}}
   \]
   Cross-multiplying:
   \[
   60 - h = 20 \implies h = 40\text{ m}
   \]

Thus, the height of the building is \( 40\text{ m} \).
</details>

8. 🟡 A person observes the angle of elevation of the top of a tower from a point to be 45°. He moves 20 m towards the tower and the angle becomes 60°. Find the tower's height.
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \) meters.
Let the initial position of the observer be at a distance \( x \) meters from the foot of the tower.
From the first point, the angle of elevation is \( 45^\circ \):
\[
\tan(45^\circ) = \frac{h}{x} \implies 1 = \frac{h}{x} \implies x = h
\]

From the second point (after moving \( 20\text{ m} \) towards the tower), the distance is \( x - 20 \) and the angle of elevation is \( 60^\circ \):
\[
\tan(60^\circ) = \frac{h}{x - 20}
\]
Since \( \tan(60^\circ) = \sqrt{3} \) and \( x = h \):
\[
\sqrt{3} = \frac{h}{h - 20}
\]
Cross-multiplying:
\[
h\sqrt{3} - 20\sqrt{3} = h \implies h(\sqrt{3} - 1) = 20\sqrt{3}
\]
Solving for \( h \):
\[
h = \frac{20\sqrt{3}}{\sqrt{3} - 1} = \frac{20\sqrt{3}(\sqrt{3} + 1)}{3 - 1} = \frac{20(3 + \sqrt{3})}{2} = 10(3 + \sqrt{3})\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 10(3 + 1.732) = 47.32\text{ m}
\]

Thus, the height of the tower is \( 10(3 + \sqrt{3})\text{ m} \) (or approximately \( 47.32\text{ m} \)).
</details>

9. 🔴 ⭐ A flagstaff stands on top of a 10 m high tower. From a point on the ground, the angles of elevation of the top and bottom of the flagstaff are 45° and 30°. Find the height of the flagstaff.
<details>
<summary>Solution</summary>

Let the height of the tower be \( BC = 10\text{ m} \).
Let the flagstaff stand on top of the tower, represented by \( AB \) of height \( h \).
Let \( D \) be the observation point on the ground at a distance \( d \) from the base of the tower \( C \).

1. The bottom of the flagstaff is the top of the tower \( B \). The angle of elevation of \( B \) from \( D \) is \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{BC}{CD} = \frac{10}{d} \implies \frac{1}{\sqrt{3}} = \frac{10}{d} \implies d = 10\sqrt{3}\text{ m}
   \]

2. The top of the flagstaff is \( A \), with a total height above the ground of \( AC = BC + AB = 10 + h \).
   The angle of elevation of \( A \) from \( D \) is \( 45^\circ \):
   \[
   \tan(45^\circ) = \frac{AC}{CD} = \frac{10 + h}{d} \implies 1 = \frac{10 + h}{10\sqrt{3}}
   \]
   Solving for \( h \):
   \[
   10 + h = 10\sqrt{3} \implies h = 10\sqrt{3} - 10 = 10(\sqrt{3} - 1)\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   h \approx 10(1.732 - 1) = 7.32\text{ m}
   \]

Thus, the height of the flagstaff is \( 10(\sqrt{3} - 1)\text{ m} \) (or approximately \( 7.32\text{ m} \)).
</details>

10. 🔴 From an aeroplane flying at a height of 3000 m, the angles of depression of two points on the ground, 30° apart, are 45° and 30°. Find the aeroplane's distance from the points.
<details>
<summary>Solution</summary>

Let \( A \) be the position of the aeroplane at a vertical height of \( 3000\text{ m} \) above the ground.
Let the two points on the ground be \( P \) and \( Q \).
The angle of depression of \( P \) is \( 45^\circ \), which means the angle of elevation of the aeroplane from \( P \) is \( 45^\circ \).
The angle of depression of \( Q \) is \( 30^\circ \), which means the angle of elevation of the aeroplane from \( Q \) is \( 30^\circ \).

To find the straight-line (slant) distances from the aeroplane to each point:

1. For point \( P \) (with elevation \( 45^\circ \)):
   In the right-angled triangle formed by the aeroplane, its projection on the ground, and \( P \):
   \[
   \sin(45^\circ) = \frac{\text{Vertical Height}}{\text{Slant Distance } (AP)} \implies \frac{1}{\sqrt{2}} = \frac{3000}{AP} \implies AP = 3000\sqrt{2}\text{ m}
   \]
   Using \( \sqrt{2} \approx 1.414 \):
   \[
   AP \approx 3000 \times 1.414 = 4242\text{ m}
   \]

2. For point \( Q \) (with elevation \( 30^\circ \)):
   In the right-angled triangle formed by the aeroplane, its projection on the ground, and \( Q \):
   \[
   \sin(30^\circ) = \frac{\text{Vertical Height}}{\text{Slant Distance } (AQ)} \implies \frac{1}{2} = \frac{3000}{AQ} \implies AQ = 6000\text{ m}
   \]

Thus, the aeroplane's distances from the points are \( 3000\sqrt{2}\text{ m} \) (approx. \( 4242\text{ m} \)) and \( 6000\text{ m} \).
</details>

---

### Type 3: Height and Distance of Inaccessible Object

**Goal:** Find height when you cannot measure the horizontal distance directly.

**Solved Example:**

From a point, the angle of elevation of a tower is 30°. After walking 40 m towards the tower, the angle becomes 60°. Find the tower's height and the distance of the first point from the tower.

**Solution:**
```
Let height = h, distance from first point = d

From first: tan 30° = h/d → h = d/√3   ...(1)
From second: tan 60° = h/(d − 40) → h = (d − 40)√3   ...(2)

Equating: d/√3 = (d − 40)√3
d = 3(d − 40)
d = 3d − 120
2d = 120 → d = 60 m

From (1): h = 60/√3 = 20√3 m
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

11. 🟡 From a point, the angle of elevation of a tower is 45°. After moving 30 m towards the tower, it becomes 60°. Find the height.
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \) meters.
Let the initial distance of the point from the tower be \( d \) meters.

1. From the first point:
   \[
   \tan(45^\circ) = \frac{h}{d} \implies 1 = \frac{h}{d} \implies d = h
   \]

2. After moving \( 30\text{ m} \) closer to the tower, the distance is \( d - 30 \) meters:
   \[
   \tan(60^\circ) = \frac{h}{d - 30} \implies \sqrt{3} = \frac{h}{h - 30}
   \]
   Cross-multiplying:
   \[
   h\sqrt{3} - 30\sqrt{3} = h \implies h(\sqrt{3} - 1) = 30\sqrt{3}
   \]
   Solving for \( h \):
   \[
   h = \frac{30\sqrt{3}}{\sqrt{3} - 1} = \frac{30\sqrt{3}(\sqrt{3} + 1)}{3 - 1} = 15\sqrt{3}(\sqrt{3} + 1) = 15(3 + \sqrt{3})\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   h \approx 15(3 + 1.732) = 15 \times 4.732 = 70.98\text{ m}
   \]

Thus, the height of the tower is \( 15(3 + \sqrt{3})\text{ m} \) (or approximately \( 70.98\text{ m} \)).
</details>

12. 🟡 The angle of elevation of a cloud from a point 60 m above a lake is 30° and the angle of depression of its reflection in the lake is 60°. Find the height of the cloud.
<details>
<summary>Solution</summary>

Let \( H \) be the height of the cloud above the surface of the lake.
The observer is at a point \( P \), which is \( 60\text{ m} \) vertically above the lake.
Let the horizontal distance from the observer to the cloud be \( d \).

1. The cloud is at height \( H - 60 \) above the observer's horizontal eye level.
   Using the angle of elevation of \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{H - 60}{d} \implies d = (H - 60)\sqrt{3} \quad \text{--- (Equation 1)}
   \]

2. The reflection of the cloud is at a depth of \( H \) below the lake surface.
   Therefore, the depth of the reflection below the observer's horizontal eye level is \( H + 60 \).
   Using the angle of depression of \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{H + 60}{d} \implies d = \frac{H + 60}{\sqrt{3}} \quad \text{--- (Equation 2)}
   \]

3. Equating Equation 1 and Equation 2:
   \[
   (H - 60)\sqrt{3} = \frac{H + 60}{\sqrt{3}}
   \]
   Multiplying both sides by \( \sqrt{3} \):
   \[
   3(H - 60) = H + 60 \implies 3H - 180 = H + 60
   \]
   \[
   2H = 240 \implies H = 120\text{ m}
   \]

Thus, the height of the cloud is \( 120\text{ m} \).
</details>

13. 🔴 A person standing on the bank of a river observes the angle of elevation of the top of a tree on the opposite bank as 60°. When he moves 40 m away from the bank, the angle becomes 30°. Find the river's width and tree's height.
<details>
<summary>Solution</summary>

Let the width of the river be \( w \) meters, and the height of the tree on the opposite bank be \( h \) meters.

1. From the bank:
   \[
   \tan(60^\circ) = \frac{h}{w} \implies \sqrt{3} = \frac{h}{w} \implies h = w\sqrt{3} \quad \text{--- (Equation 1)}
   \]

2. From the point \( 40\text{ m} \) away from the bank:
   The total distance from the foot of the tree is \( w + 40 \) meters.
   \[
   \tan(30^\circ) = \frac{h}{w + 40} \implies \frac{1}{\sqrt{3}} = \frac{h}{w + 40} \implies h = \frac{w + 40}{\sqrt{3}} \quad \text{--- (Equation 2)}
   \]

3. Equating the two values of \( h \):
   \[
   w\sqrt{3} = \frac{w + 40}{\sqrt{3}}
   \]
   Multiplying by \( \sqrt{3} \):
   \[
   3w = w + 40 \implies 2w = 40 \implies w = 20\text{ m}
   \]
   Substituting \( w = 20 \) back into Equation 1:
   \[
   h = 20\sqrt{3}\text{ m} \approx 34.64\text{ m}
   \]

Thus, the width of the river is \( 20\text{ m} \) and the height of the tree is \( 20\sqrt{3}\text{ m} \) (or approximately \( 34.64\text{ m} \)).
</details>

14. 🔴 ⭐ The angle of elevation of a jet plane from a point on the ground is 60°. After 15 seconds, the angle changes to 30°. If the plane is flying at 3000√3 m, find its speed.
<details>
<summary>Solution</summary>

Let the jet plane fly horizontally at a constant height \( H = 3000\sqrt{3}\text{ m} \).
Let \( O \) be the observation point on the ground.
Let the position of the plane at the start be \( P_1 \) and after 15 seconds be \( P_2 \).
Let \( M_1 \) and \( M_2 \) be the vertical projections of \( P_1 \) and \( P_2 \) on the ground, respectively.

1. In the right-angled triangle \( \triangle OM_1P_1 \) (angle of elevation \( 60^\circ \)):
   \[
   \tan(60^\circ) = \frac{P_1M_1}{OM_1} \implies \sqrt{3} = \frac{3000\sqrt{3}}{OM_1} \implies OM_1 = 3000\text{ m}
   \]

2. In the right-angled triangle \( \triangle OM_2P_2 \) (angle of elevation \( 30^\circ \)):
   \[
   \tan(30^\circ) = \frac{P_2M_2}{OM_2} \implies \frac{1}{\sqrt{3}} = \frac{3000\sqrt{3}}{OM_2} \implies OM_2 = 3000 \times 3 = 9000\text{ m}
   \]

3. The distance covered by the jet plane in 15 seconds is:
   \[
   d = M_1M_2 = OM_2 - OM_1 = 9000 - 3000 = 6000\text{ m}
   \]

4. The speed of the plane is:
   \[
   \text{Speed} = \frac{\text{Distance}}{\text{Time}} = \frac{6000\text{ m}}{15\text{ s}} = 400\text{ m/s}
   \]
   Converting this to km/h:
   \[
   400 \times \frac{18}{5} = 1440\text{ km/h}
   \]

Thus, the speed of the jet plane is \( 400\text{ m/s} \) (or \( 1440\text{ km/h} \)).
</details>

15. 🔴 From the top of a 75 m lighthouse, the angles of depression of two ships are 30° and 45°. If one ship is behind the other, find the distance between them.
<details>
<summary>Solution</summary>

Let \( AB = 75\text{ m} \) be the lighthouse.
Let the two ships be \( S_1 \) (closer) and \( S_2 \) (farther), situated on the same side of the lighthouse such that their angles of depression are \( 45^\circ \) and \( 30^\circ \) respectively.
This means the angles of elevation of \( A \) from \( S_1 \) and \( S_2 \) are \( 45^\circ \) and \( 30^\circ \).

1. In \( \triangle ABS_1 \):
   \[
   \tan(45^\circ) = \frac{AB}{BS_1} \implies 1 = \frac{75}{BS_1} \implies BS_1 = 75\text{ m}
   \]

2. In \( \triangle ABS_2 \):
   \[
   \tan(30^\circ) = \frac{AB}{BS_2} \implies \frac{1}{\sqrt{3}} = \frac{75}{BS_2} \implies BS_2 = 75\sqrt{3}\text{ m}
   \]

3. The distance between the ships is:
   \[
   S_1S_2 = BS_2 - BS_1 = 75\sqrt{3} - 75 = 75(\sqrt{3} - 1)\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   S_1S_2 \approx 75(1.732 - 1) = 75 \times 0.732 = 54.9\text{ m}
   \]

Thus, the distance between the ships is \( 75(\sqrt{3} - 1)\text{ m} \) (or approximately \( 54.9\text{ m} \)).
</details>

---

### Type 4: Two Objects — Same Observation Point

**Goal:** Compare heights/depths of two objects from one observation point.

**Solved Example:**

From the top of a 100 m tower, the angles of depression of two cars on the road on the same side of the tower are 30° and 45°. Find the distance between the cars.

**Solution:**
```
Let car 1 (closer) be at distance d₁: tan 45° = 100/d₁ → d₁ = 100 m
Let car 2 (farther) be at distance d₂: tan 30° = 100/d₂ → d₂ = 100√3 m

Distance between cars = d₂ − d₁ = 100√3 − 100 = 100(√3 − 1) m
```
🟡 Medium

---

**Practice Problems:**

16. 🟡 From the top of a 50 m cliff, the angles of depression of two boats in the sea are 30° and 60°. Find the distance between them.
<details>
<summary>Solution</summary>

Let \( AB = 50\text{ m} \) be the cliff.
Let the two boats be \( B_1 \) and \( B_2 \). We consider the primary case where both boats are on the same side of the cliff.
The angles of depression of \( B_1 \) (closer) and \( B_2 \) (farther) from the top \( A \) are \( 60^\circ \) and \( 30^\circ \). This corresponds to elevation angles of \( 60^\circ \) and \( 30^\circ \).

1. In \( \triangle ABB_1 \):
   \[
   \tan(60^\circ) = \frac{AB}{BB_1} \implies \sqrt{3} = \frac{50}{BB_1} \implies BB_1 = \frac{50}{\sqrt{3}}\text{ m}
   \]

2. In \( \triangle ABB_2 \):
   \[
   \tan(30^\circ) = \frac{AB}{BB_2} \implies \frac{1}{\sqrt{3}} = \frac{50}{BB_2} \implies BB_2 = 50\sqrt{3}\text{ m}
   \]

3. The distance between the boats is:
   \[
   B_1B_2 = BB_2 - BB_1 = 50\sqrt{3} - \frac{50}{\sqrt{3}} = \frac{150 - 50}{\sqrt{3}} = \frac{100}{\sqrt{3}}\text{ m}
   \]
   Multiplying numerator and denominator by \( \sqrt{3} \):
   \[
   B_1B_2 = \frac{100\sqrt{3}}{3}\text{ m} \approx 57.74\text{ m}
   \]
   *(Note: If the boats were on opposite sides of the cliff, the distance would be \( BB_2 + BB_1 = 50\sqrt{3} + \frac{50}{\sqrt{3}} = \frac{200\sqrt{3}}{3}\text{ m} \approx 115.47\text{ m}\).)*

Thus, the distance between the boats (on the same side) is \( \frac{100\sqrt{3}}{3}\text{ m} \) (or approximately \( 57.74\text{ m} \)).
</details>

17. 🟡 A 7 m tall pole stands on the ground. From a point on the ground, the angles of elevation of the top and bottom of a flagstaff on the pole are 60° and 45°. Find the flagstaff's height.
<details>
<summary>Solution</summary>

Let the pole be \( BC = 7\text{ m} \).
Let the flagstaff stand on top of the pole, represented by \( AB \) of height \( h \).
Let \( D \) be the observation point on the ground at a distance \( d \) from the base of the pole \( C \).

The bottom of the flagstaff is the top of the pole \( B \). The angle of elevation of \( B \) from \( D \) is \( 45^\circ \):
\[
\tan(45^\circ) = \frac{BC}{CD} = \frac{7}{d} \implies 1 = \frac{7}{d} \implies d = 7\text{ m}
\]

The top of the flagstaff is \( A \), with a total height above the ground of \( AC = 7 + h \). The angle of elevation of \( A \) from \( D \) is \( 60^\circ \):
\[
\tan(60^\circ) = \frac{AC}{CD} = \frac{7 + h}{d} \implies \sqrt{3} = \frac{7 + h}{7}
\]
Solving for \( h \):
\[
7\sqrt{3} = 7 + h \implies h = 7\sqrt{3} - 7 = 7(\sqrt{3} - 1)\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 7(1.732 - 1) = 7 \times 0.732 = 5.124\text{ m}
\]

Thus, the height of the flagstaff is \( 7(\sqrt{3} - 1)\text{ m} \) (or approximately \( 5.12\text{ m} \)).
</details>

18. 🔴 Two ships are sailing in the sea on either side of a lighthouse. The angles of depression from the top of the 100 m lighthouse are 45° and 30°. Find the distance between the ships.
<details>
<summary>Solution</summary>

Let the lighthouse be \( AB = 100\text{ m} \), where \( B \) is the base at sea level.
Let the two ships be \( S_1 \) and \( S_2 \), situated on opposite sides of the lighthouse.
The angles of depression of the ships from the top of the lighthouse \( A \) are \( 45^\circ \) and \( 30^\circ \bk \), which means the angles of elevation of \( A \) from \( S_1 \) and \( S_2 \) are \( 45^\circ \) and \( 30^\circ \), respectively.

1. In \( \triangle ABS_1 \):
   \[
   \tan(45^\circ) = \frac{AB}{BS_1} \implies 1 = \frac{100}{BS_1} \implies BS_1 = 100\text{ m}
   \]

2. In \( \triangle ABS_2 \):
   \[
   \tan(30^\circ) = \frac{AB}{BS_2} \implies \frac{1}{\sqrt{3}} = \frac{100}{BS_2} \implies BS_2 = 100\sqrt{3}\text{ m}
   \]

3. Since the ships are on opposite sides of the lighthouse, the total distance between them is:
   \[
   S_1S_2 = BS_1 + BS_2 = 100 + 100\sqrt{3} = 100(1 + \sqrt{3})\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   S_1S_2 \approx 100(1 + 1.732) = 100 \times 2.732 = 273.2\text{ m}
   \]

Thus, the distance between the ships is \( 100(1 + \sqrt{3})\text{ m} \) (or approximately \( 273.2\text{ m} \)).
</details>

19. 🔴 ⭐ From an aeroplane 2000 m above the sea, the angles of depression of two rocks on the same line are 30° and 60°. Find the distance between the rocks.
<details>
<summary>Solution</summary>

Let the aeroplane be at point \( A \), at a vertical height of \( 2000\text{ m} \) above sea level.
Let the two rocks be \( R_1 \) and \( R_2 \). We calculate for both scenarios: when the rocks are on the same side, and when they are on opposite sides of the aeroplane.

1. Find the distances from the vertical projection of the plane on the water surface \( B \):
   - For the rock with an angle of depression of \( 60^\circ \) (closer rock \( R_1 \)):
     \[
     \tan(60^\circ) = \frac{AB}{BR_1} \implies \sqrt{3} = \frac{2000}{BR_1} \implies BR_1 = \frac{2000}{\sqrt{3}}\text{ m}
     \]
   - For the rock with an angle of depression of \( 30^\circ \) (farther rock \( R_2 \)):
     \[
     \tan(30^\circ) = \frac{AB}{BR_2} \implies \frac{1}{\sqrt{3}} = \frac{2000}{BR_2} \implies BR_2 = 2000\sqrt{3}\text{ m}
     \]

2. **Case A: Rocks are on the same side**
   The distance between them is:
   \[
   R_1R_2 = BR_2 - BR_1 = 2000\sqrt{3} - \frac{2000}{\sqrt{3}} = \frac{6000 - 2000}{\sqrt{3}} = \frac{4000}{\sqrt{3}}\text{ m} \approx 2309.4\text{ m}
   \]

3. **Case B: Rocks are on opposite sides**
   The distance between them is:
   \[
   R_1R_2 = BR_2 + BR_1 = 2000\sqrt{3} + \frac{2000}{\sqrt{3}} = \frac{6000 + 2000}{\sqrt{3}} = \frac{8000}{\sqrt{3}}\text{ m} \approx 4618.8\text{ m}
   \]

Thus, the distance between the rocks is \( \frac{4000}{\sqrt{3}}\text{ m} \) (approx. \( 2309.4\text{ m} \)) if they are on the same side, and \( \frac{8000}{\sqrt{3}}\text{ m} \) (approx. \( 4618.8\text{ m} \)) if they are on opposite sides.
</details>

20. 🔴 The angle of elevation of the top of a tower from the foot of a building is 60° and the angle of elevation of the top of the building from the foot of the tower is 30°. If the tower is 60 m high, find the building's height.
<details>
<summary>Solution</summary>

Let the tower be \( AB = 60\text{ m} \).
Let the building be \( CD = h \) meters.
Let the horizontal distance between the tower and the building be \( BD = d \).

1. From the foot of the building \( D \), the angle of elevation of the top of the tower \( A \) is \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{AB}{BD} \implies \sqrt{3} = \frac{60}{d} \implies d = \frac{60}{\sqrt{3}} = 20\sqrt{3}\text{ m}
   \]

2. From the foot of the tower \( B \), the angle of elevation of the top of the building \( C \) is \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{CD}{BD} \implies \frac{1}{\sqrt{3}} = \frac{h}{d} \implies h = \frac{d}{\sqrt{3}}
   \]
   Substituting the value of \( d \):
   \[
   h = \frac{20\sqrt{3}}{\sqrt{3}} = 20\text{ m}
   \]

Thus, the height of the building is \( 20\text{ m} \).
</details>

---

### Type 5: Angle of Depression Applications

**Goal:** Use angle of depression in real-world problems.

**Solved Example:**

From the top of a 30 m building, the angle of depression of a car on the road is 30°. How far is the car from the building?<br>

**Solution:**
```
Angle of depression = angle of elevation from car = 30°
tan 30° = 30/d
1/√3 = 30/d
d = 30√3 m
```
🟢 Easy

---

**Practice Problems:**

21. 🟢 From a 45 m tower, the angle of depression of an object on the ground is 45°. Find the object's distance.
<details>
<summary>Solution</summary>

Let the distance of the object from the foot of the tower be \( d \) meters.
The height of the tower is \( 45\text{ m} \).
The angle of depression of the object from the top of the tower is \( 45^\circ \), which means the angle of elevation of the top of the tower from the object is \( 45^\circ \).

In the right-angled triangle:
\[
\tan(45^\circ) = \frac{\text{Height}}{\text{Distance}} \implies 1 = \frac{45}{d} \implies d = 45\text{ m}
\]

Thus, the distance of the object from the foot of the tower is \( 45\text{ m} \).
</details>

22. 🟡 An observer 1.8 m tall stands 30 m from a chimney. The angle of elevation of the top of the chimney from his eye is 60°. Find the chimney's height.
<details>
<summary>Solution</summary>

Let the total height of the chimney be \( H \) meters.
The height of the observer is \( 1.8\text{ m} \).
The observer stands at a horizontal distance of \( 30\text{ m} \) from the chimney.

Let \( h \) be the height of the chimney above the observer's horizontal eye level.
\[
H = h + 1.8
\]
In the right-angled triangle formed above the observer's eye level:
\[
\tan(60^\circ) = \frac{h}{30} \implies \sqrt{3} = \frac{h}{30} \implies h = 30\sqrt{3}\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 30 \times 1.732 = 51.96\text{ m}
\]
Now, add the observer's height to find the total height:
\[
H = 51.96 + 1.8 = 53.76\text{ m}
\]

Thus, the height of the chimney is \( 30\sqrt{3} + 1.8\text{ m} \) (or approximately \( 53.76\text{ m} \)).
</details>

23. 🟡 From the top of a 25 m building, the angle of depression of a car on a road is 60°. Find the distance of the car from the building.
<details>
<summary>Solution</summary>

Let \( d \) be the distance of the car from the foot of the building.
The height of the building is \( 25\text{ m} \).
Since the angle of depression of the car from the top of the building is \( 60^\circ \), the angle of elevation of the top of the building from the car is also \( 60^\circ \).

In the right-angled triangle:
\[
\tan(60^\circ) = \frac{\text{Height}}{\text{Distance}} \implies \sqrt{3} = \frac{25}{d}
\]
Solving for \( d \):
\[
d = \frac{25}{\sqrt{3}} = \frac{25\sqrt{3}}{3}\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
d \approx \frac{25 \times 1.732}{3} \approx 14.43\text{ m}
\]

Thus, the distance of the car from the building is \( \frac{25\sqrt{3}}{3}\text{ m} \) (or approximately \( 14.43\text{ m} \)).
</details>

24. 🔴 A man on the top of a 40 m building observes a car moving towards him. At an instant, the angle of depression is 45°. After 5 seconds, it becomes 60°. Find the speed of the car.
<details>
<summary>Solution</summary>

Let the height of the building be \( AB = 40\text{ m} \).
Let the initial position of the car be \( C \) (depression angle \( 45^\circ \)) and the final position after 5 seconds be \( D \) (depression angle \( 60^\circ \)).
Let the distance of \( C \) and \( D \) from the foot of the building \( B \) be \( d_1 \) and \( d_2 \) respectively.

1. In \( \triangle ABC \) (angle of elevation \( 45^\circ \)):
   \[
   \tan(45^\circ) = \frac{AB}{BC} \implies 1 = \frac{40}{d_1} \implies d_1 = 40\text{ m}
   \]

2. In \( \triangle ABD \) (angle of elevation \( 60^\circ \)):
   \[
   \tan(60^\circ) = \frac{AB}{BD} \implies \sqrt{3} = \frac{40}{d_2} \implies d_2 = \frac{40}{\sqrt{3}}\text{ m}
   \]

3. The distance traveled by the car in 5 seconds is:
   \[
   CD = d_1 - d_2 = 40 - \frac{40}{\sqrt{3}} = 40\left(1 - \frac{1}{\sqrt{3}}\right) = \frac{40(\sqrt{3} - 1)}{\sqrt{3}}\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   CD \approx 40 \times \left(1 - 0.577\right) = 40 \times 0.423 = 16.92\text{ m}
   \]

4. The speed of the car is:
   \[
   \text{Speed} = \frac{\text{Distance}}{\text{Time}} = \frac{16.92\text{ m}}{5\text{ s}} \approx 3.38\text{ m/s}
   \]
   Or in exact terms:
   \[
   \text{Speed} = 8\left(1 - \frac{1}{\sqrt{3}}\right)\text{ m/s} = \frac{8(3 - \sqrt{3})}{3}\text{ m/s}
   \]

Thus, the speed of the car is \( \frac{8(3-\sqrt{3})}{3}\text{ m/s} \) (or approximately \( 3.38\text{ m/s} \)).
</details>

25. 🔴 ⭐ A ladder rests against a vertical wall at an inclination of 60° to the horizontal. Its foot is pulled away from the wall through a distance x so that its upper end slides 4 m down the wall, and the inclination becomes 30°. Find x and the ladder's length.
<details>
<summary>Solution</summary>

Let the length of the ladder be \( L \) meters.
Let the wall be represented by the vertical line and the ground by the horizontal line.

**Initial Position:**
- Angle of inclination to the horizontal is \( 60^\circ \).
- Let the initial height reached on the wall be \( h_1 \) and the distance of its foot from the wall be \( y_1 \).
\[
h_1 = L\sin(60^\circ) = \frac{L\sqrt{3}}{2}
\]
\[
y_1 = L\cos(60^\circ) = \frac{L}{2}
\]

**Final Position:**
- The top of the ladder slides \( 4\text{ m} \) down the wall, so the new height is \( h_2 = h_1 - 4 = \frac{L\sqrt{3}}{2} - 4 \).
- The foot is pulled away by \( x \) meters, so the new distance from the wall is \( y_2 = y_1 + x = \frac{L}{2} + x \).
- The new angle of inclination is \( 30^\circ \).
\[
h_2 = L\sin(30^\circ) \implies \frac{L\sqrt{3}}{2} - 4 = \frac{L}{2}
\]
Solving for \( L \):
\[
\frac{L\sqrt{3}}{2} - \frac{L}{2} = 4 \implies L(\sqrt{3} - 1) = 8 \implies L = \frac{8}{\sqrt{3} - 1}\text{ m}
\]
Rationalizing the denominator:
\[
L = \frac{8(\sqrt{3} + 1)}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{8(\sqrt{3} + 1)}{3 - 1} = 4(\sqrt{3} + 1)\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
L \approx 4(1.732 + 1) = 4 \times 2.732 = 10.93\text{ m}
\]

**Finding \( x \):**
Using the horizontal relationship in the final position:
\[
y_2 = L\cos(30^\circ) \implies y_1 + x = \frac{L\sqrt{3}}{2}
\]
Substitute \( y_1 = \frac{L}{2} \):
\[
\frac{L}{2} + x = \frac{L\sqrt{3}}{2} \implies x = \frac{L(\sqrt{3} - 1)}{2}
\]
Substitute \( L = \frac{8}{\sqrt{3} - 1} \):
\[
x = \frac{8}{\sqrt{3} - 1} \times \frac{\sqrt{3} - 1}{2} = 4\text{ m}
\]

Thus, the distance the foot is pulled, \( x \bk \), is \( 4\text{ m} \) and the length of the ladder is \( 4(\sqrt{3} + 1)\text{ m} \) (or approximately \( 10.93\text{ m} \)).
</details>

---

### Type 6: Multiple Elevation Angles

**Goal:** Problems involving more than two observations.

**Solved Example:**

A person observes the top of a 75 m tower from a point P at angle 30°. He moves a certain distance towards the tower and observes at 45°, then further to observe at 60°. Find the distances between successive observation points.

**Solution:**
```
At P: tan 30° = 75/d₁ → d₁ = 75√3 m
At Q (closer): tan 45° = 75/d₂ → d₂ = 75 m
At R (closest): tan 60° = 75/d₃ → d₃ = 75/√3 = 25√3 m

PQ = d₁ − d₂ = 75√3 − 75 = 75(√3 − 1) m
QR = d₂ − d₃ = 75 − 25√3 = 25(3 − √3) m
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 A person observes a tower from three points. The angles of elevation are 30°, 45°, and 60° at distances d₁, d₂, d₃ respectively. If d₁ − d₂ = 50 m, find h.
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \).
The horizontal distances of the three observation points from the foot of the tower are \( d_1 \), \( d_2 \), and \( d_3 \).

1. For angle \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{h}{d_1} \implies d_1 = h\sqrt{3}
   \]
2. For angle \( 45^\circ \):
   \[
   \tan(45^\circ) = \frac{h}{d_2} \implies d_2 = h
   \]
3. For angle \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{h}{d_3} \implies d_3 = \frac{h}{\sqrt{3}}
   \]

We are given that \( d_1 - d_2 = 50\text{ m} \):
\[
h\sqrt{3} - h = 50 \implies h(\sqrt{3} - 1) = 50
\]
Solving for \( h \):
\[
h = \frac{50}{\sqrt{3} - 1} = \frac{50(\sqrt{3} + 1)}{3 - 1} = 25(\sqrt{3} + 1)\text{ m}
\]
Using \( \sqrt{3} \approx 1.732 \):
\[
h \approx 25(1.732 + 1) = 25 \times 2.732 = 68.3\text{ m}
\]

Thus, the height of the tower \( h \) is \( 25(\sqrt{3} + 1)\text{ m} \) (or approximately \( 68.3\text{ m} \)).
</details>

27. 🔴 ⭐ From a point, the angle of elevation of a tower is 30°. On walking 100 m towards the tower, the angle becomes 60°. Find the height.
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \) meters.
Let the initial distance of the point from the foot of the tower be \( d \) meters.

1. From the first point:
   \[
   \tan(30^\circ) = \frac{h}{d} \implies d = h\sqrt{3}
   \]

2. From the second point (after walking \( 100\text{ m} \) towards the tower):
   The new distance is \( d - 100 \).
   \[
   \tan(60^\circ) = \frac{h}{d - 100} \implies \sqrt{3} = \frac{h}{h\sqrt{3} - 100}
   \]
   Cross-multiplying:
   \[
   3h - 100\sqrt{3} = h \implies 2h = 100\sqrt{3} \implies h = 50\sqrt{3}\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   h \approx 50 \times 1.732 = 86.6\text{ m}
   \]

Thus, the height of the tower is \( 50\sqrt{3}\text{ m} \) (or approximately \( 86.6\text{ m} \)).
</details>

28. 🔴 A vertical pole and a tower are on the same level ground. From the top of the pole, the angle of elevation of the top of the tower is 60° and the angle of depression of the foot is 30°. If the pole is 10 m high, find the tower's height.
<details>
<summary>Solution</summary>

Let the pole be \( AB = 10\text{ m} \).
Let the tower be \( CD \) of height \( H \).
Both stand on the same horizontal ground \( BD \).

1. From the top of the pole \( A \bk \), the angle of depression of the foot of the tower \( D \) is \( 30^\circ \). This means the angle of elevation of \( A \) from \( D \) is \( 30^\circ \).
   In the right-angled triangle \( \triangle ABD \):
   \[
   \tan(30^\circ) = \frac{AB}{BD} \implies \frac{1}{\sqrt{3}} = \frac{10}{BD} \implies BD = 10\sqrt{3}\text{ m}
   \]

2. Let \( E \) be the point on the tower \( CD \) at the same vertical height as \( A \).
   Then \( ED = AB = 10\text{ m} \bk \bk \), and the horizontal distance \( AE = BD = 10\sqrt{3}\text{ m} \).
   From \( A \), the angle of elevation of the top of the tower \( C \) is \( 60^\circ \).
   In \( \triangle CAE \):
   \[
   \tan(60^\circ) = \frac{CE}{AE} \implies \sqrt{3} = \frac{CE}{10\sqrt{3}} \implies CE = 10\sqrt{3} \times \sqrt{3} = 30\text{ m}
   \]

3. The total height of the tower is:
   \[
   H = CE + ED = 30 + 10 = 40\text{ m}
   \]

Thus, the height of the tower is \( 40\text{ m} \).
</details>

29. 🔴 A man on a cliff observes a boat at an angle of depression of 30° which is approaching the shore. After 10 minutes, the angle becomes 60°. How much more time will the boat take to reach the shore?<br>
<details>
<summary>Solution</summary>

Let the height of the cliff be \( h \) and the constant speed of the boat be \( v \).
Let \( d_1 \) be the initial distance of the boat from the foot of the cliff, and \( d_2 \) be the distance after 10 minutes.

1. From the initial observation (depression angle \( 30^\circ \)):
   \[
   \tan(30^\circ) = \frac{h}{d_1} \implies d_1 = h\sqrt{3}
   \]

2. From the second observation (depression angle \( 60^\circ \)):
   \[
   \tan(60^\circ) = \frac{h}{d_2} \implies d_2 = \frac{h}{\sqrt{3}}
   \]

3. The distance covered by the boat in 10 minutes is:
   \[
   \Delta d = d_1 - d_2 = h\sqrt{3} - \frac{h}{\sqrt{3}} = \frac{3h - h}{\sqrt{3}} = \frac{2h}{\sqrt{3}}
   \]

4. The speed \( v \) of the boat is:
   \[
   v = \frac{\text{Distance}}{\text{Time}} = \frac{2h / \sqrt{3}}{10} = \frac{h}{5\sqrt{3}}\text{ units per minute}
   \]

5. The remaining distance to reach the shore is \( d_2 = \frac{h}{\sqrt{3}} \).
   The time taken to cover this remaining distance is:
   \[
   \text{Time} = \frac{\text{Remaining Distance}}{\text{Speed}} = \frac{h / \sqrt{3}}{h / (5\sqrt{3})} = 5\text{ minutes}
   \]

Thus, the boat will take \( 5\text{ more minutes} \) to reach the shore.
</details>

30. 🔴 ⭐ Two pillars of equal height stand on either side of a road 100 m wide. From a point on the road between them, the angles of elevation of their tops are 30° and 60°. Find the height of the pillars and the point's position.
<details>
<summary>Solution</summary>

Let the height of each pillar be \( h \) meters.
Let the width of the road be \( 100\text{ m} \).
Let the observation point be \( P \) on the road.
Let \( P \) be at a distance of \( x \) meters from the foot of the pillar with a \( 60^\circ \) elevation angle, and \( 100 - x \) meters from the foot of the pillar with a \( 30^\circ \) elevation angle.

1. For the first pillar (elevation \( 60^\circ \)):
   \[
   \tan(60^\circ) = \frac{h}{x} \implies \sqrt{3} = \frac{h}{x} \implies h = x\sqrt{3} \quad \text{--- (Equation 1)}
   \]

2. For the second pillar (elevation \( 30^\circ \)):
   \[
   \tan(30^\circ) = \frac{h}{100 - x} \implies \frac{1}{\sqrt{3}} = \frac{h}{100 - x} \implies h = \frac{100 - x}{\sqrt{3}} \quad \text{--- (Equation 2)}
   \]

3. Equating Equation 1 and Equation 2:
   \[
   x\sqrt{3} = \frac{100 - x}{\sqrt{3}}
   \]
   Multiplying by \( \sqrt{3} \):
   \[
   3x = 100 - x \implies 4x = 100 \implies x = 25\text{ m}
   \]
   So the point is located at \( 25\text{ m} \) from the first pillar and \( 75\text{ m} \) from the second pillar.

4. Find the height \( h \):
   \[
   h = 25\sqrt{3}\text{ m} \approx 43.3\text{ m}
   \]

Thus, the height of the pillars is \( 25\sqrt{3}\text{ m} \) (approx. \( 43.3\text{ m} \)), and the point is \( 25\text{ m} \) from the pillar with a \( 60^\circ \) elevation (or \( 75\text{ m} \) from the pillar with a \( 30^\circ \) elevation).
</details>

---

## Stage 4: Type Mixer

1. 🟡 A tower is 50 m tall. From the top, the angles of depression of two cars on the ground are 30° and 45°. If the cars are on the same side of the tower, find the distance between them.
<details>
<summary>Solution</summary>

Let the height of the tower be \( AB = 50\text{ m} \).
Let the two cars be \( C_1 \) (closer) and \( C_2 \) (farther) on the same side of the tower.
The angles of depression from the top of the tower \( A \) are \( 45^\circ \) and \( 30^\circ \), which means the angles of elevation of \( A \) from \( C_1 \) and \( C_2 \) are \( 45^\circ \) and \( 30^\circ \) respectively.

1. In \( \triangle ABC_1 \):
   \[
   \tan(45^\circ) = \frac{AB}{BC_1} \implies 1 = \frac{50}{BC_1} \implies BC_1 = 50\text{ m}
   \]

2. In \( \triangle ABC_2 \):
   \[
   \tan(30^\circ) = \frac{AB}{BC_2} \implies \frac{1}{\sqrt{3}} = \frac{50}{BC_2} \implies BC_2 = 50\sqrt{3}\text{ m}
   \]

3. The distance between the cars is:
   \[
   C_1C_2 = BC_2 - BC_1 = 50\sqrt{3} - 50 = 50(\sqrt{3} - 1)\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   C_1C_2 \approx 50(1.732 - 1) = 50 \times 0.732 = 36.6\text{ m}
   \]

Thus, the distance between the cars is \( 50(\sqrt{3} - 1)\text{ m} \) (or approximately \( 36.6\text{ m} \)).
</details>

2. 🟡 From the top of a 60 m high building, the angle of depression of the top and bottom of a tower are 30° and 60°. Find the tower's height.
<details>
<summary>Solution</summary>

Let the building be \( AB = 60\text{ m} \).
Let the tower be \( CD = h \) meters.
Let the distance between their bases be \( BD = d \).

1. From the top of the building \( A \), the angle of depression of the base of the tower \( D \) is \( 60^\circ \). This means the angle of elevation of \( A \) from \( D \) is \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{AB}{BD} \implies \sqrt{3} = \frac{60}{d} \implies d = \frac{60}{\sqrt{3}} = 20\sqrt{3}\text{ m}
   \]

2. Let \( E \) be the point on the building \( AB \) at the same level as the top of the tower \( C \).
   The horizontal distance is \( AE = BD = d = 20\sqrt{3}\text{ m} \).
   The height of the top of the building above \( E \) is \( AE = 60 - h \).
   The angle of depression of the top of the tower \( C \) from \( A \) is \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{AE}{EC} \implies \frac{1}{\sqrt{3}} = \frac{60 - h}{20\sqrt{3}}
   \]
   Solving for \( h \):
   \[
   60 - h = 20 \implies h = 40\text{ m}
   \]

Thus, the height of the tower is \( 40\text{ m} \).
</details>

3. 🔴 ⭐ The angle of elevation of the top of a vertical tower from a point on the ground is 60°. From a point 40 m vertically above the first point, its angle of elevation is 30°. Find the tower's height and horizontal distance.
<details>
<summary>Solution</summary>

Let the height of the vertical tower be \( H \) meters and the horizontal distance to the tower from the observation line be \( d \) meters.
Let the first point on the ground be \( P_1 \).
Let the second point, \( 40\text{ m} \) vertically above \( P_1 \), be \( P_2 \).

1. From \( P_1 \) (elevation \( 60^\circ \)):
   \[
   \tan(60^\circ) = \frac{H}{d} \implies \sqrt{3} = \frac{H}{d} \implies H = d\sqrt{3} \quad \text{--- (Equation 1)}
   \]

2. From \( P_2 \) (elevation \( 30^\circ \)):
   The vertical height to the top of the tower above \( P_2 \)'s level is \( H - 40 \).
   \[
   \tan(30^\circ) = \frac{H - 40}{d} \implies \frac{1}{\sqrt{3}} = \frac{H - 40}{d} \implies d = (H - 40)\sqrt{3} \quad \text{--- (Equation 2)}
   \]

3. Substituting Equation 1 into Equation 2:
   \[
   \frac{H}{\sqrt{3}} = (H - 40)\sqrt{3}
   \]
   Multiplying by \( \sqrt{3} \):
   \[
   H = 3(H - 40) \implies H = 3H - 120 \implies 2H = 120 \implies H = 60\text{ m}
   \]
   Now, find the horizontal distance \( d \):
   \[
   d = \frac{H}{\sqrt{3}} = \frac{60}{\sqrt{3}} = 20\sqrt{3}\text{ m} \approx 34.64\text{ m}
   \]

Thus, the tower's height is \( 60\text{ m} \) and the horizontal distance is \( 20\sqrt{3}\text{ m} \) (or approx. \( 34.64\text{ m} \)).
</details>

4. 🔴 From a point on a bridge across a river, the angles of depression of the banks on opposite sides are 30° and 60°. If the bridge is 12 m above the river, find the river's width.
<details>
<summary>Solution</summary>

Let the point on the bridge be \( P \), situated at a vertical height of \( h = 12\text{ m} \) above the river bed.
Let \( O \) be the point directly below \( P \) on the river surface.
Let the two banks on opposite sides of the river be \( A \) and \( B \).
The angles of depression of \( A \) and \( B \) from \( P \) are \( 30^\circ \) and \( 60^\circ \) respectively.
This means the angles of elevation of \( P \) from \( A \) and \( B \) are \( 30^\circ \) and \( 60^\circ \).

1. In the right-angled triangle \( \triangle POA \):
   \[
   \tan(30^\circ) = \frac{PO}{OA} \implies \frac{1}{\sqrt{3}} = \frac{12}{OA} \implies OA = 12\sqrt{3}\text{ m}
   \]

2. In the right-angled triangle \( \triangle POB \):
   \[
   \tan(60^\circ) = \frac{PO}{OB} \implies \sqrt{3} = \frac{12}{OB} \implies OB = \frac{12}{\sqrt{3}} = 4\sqrt{3}\text{ m}
   \]

3. The total width of the river is:
   \[
   AB = OA + OB = 12\sqrt{3} + 4\sqrt{3} = 16\sqrt{3}\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   AB \approx 16 \times 1.732 = 27.71\text{ m}
   \]

Thus, the width of the river is \( 16\sqrt{3}\text{ m} \) (or approximately \( 27.71\text{ m} \bk \)).
</details>

5. 🔴 Two men on opposite sides of a 60 m high tower observe its top at angles 30° and 60°. Find the distance between the men.
<details>
<summary>Solution</summary>

Let the tower be \( AB = 60\text{ m} \), where \( B \) is the foot on the ground.
Let the two men be at points \( P \) and \( Q \) on opposite sides of the tower.
The angles of elevation of the top of the tower \( A \) from \( P \) and \( Q \) are \( 30^\circ \) and \( 60^\circ \) respectively.

1. In \( \triangle ABP \):
   \[
   \tan(30^\circ) = \frac{AB}{BP} \implies \frac{1}{\sqrt{3}} = \frac{60}{BP} \implies BP = 60\sqrt{3}\text{ m}
   \]

2. In \( \triangle ABQ \):
   \[
   \tan(60^\circ) = \frac{AB}{BQ} \implies \sqrt{3} = \frac{60}{BQ} \implies BQ = \frac{60}{\sqrt{3}} = 20\sqrt{3}\text{ m}
   \]

3. The distance between the two men is:
   \[
   PQ = BP + BQ = 60\sqrt{3} + 20\sqrt{3} = 80\sqrt{3}\text{ m}
   \]
   Using \( \sqrt{3} \approx 1.732 \):
   \[
   PQ \approx 80 \times 1.732 = 138.56\text{ m}
   \]

Thus, the distance between the two men is \( 80\sqrt{3}\text{ m} \) (or approximately \( 138.56\text{ m} \)).
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 The angle of elevation of the top of a tower from a point 30 m away is 30°. Find the tower's height. **(2 marks)**

<details>
<summary>Solution</summary>

```
tan 30° = h/30
h = 30 × 1/√3 = 30/√3 = 10√3 m
```
</details>

---

**Q2.** 🟡 A kite flying at a height of 60 m has a string of length 120 m. Find the angle the string makes with the ground. **(2 marks)**

<details>
<summary>Solution</summary>

```
sin θ = 60/120 = 1/2
θ = 30°
```
</details>

---

**Q3.** 🟡 A ladder 20 m long makes an angle of 60° with the ground. Find the height of the window it reaches. **(3 marks)**

<details>
<summary>Solution</summary>

```
sin 60° = h/20
h = 20 × √3/2 = 10√3 m
```
</details>

---

**Q4.** 🔴 ⭐ From the top of a 50 m building, the angle of depression of the top and bottom of another building are 30° and 60°. Find the other building's height. **(3 marks)**

<details>
<summary>Solution</summary>

Let other building's height = h, distance between them = d

From top of 50 m building:
Depression to bottom = 60°: tan 60° = 50/d → d = 50/√3 m
Depression to top = 30°: tan 30° = (50 − h)/d
1/√3 = (50 − h)/(50/√3)
1/√3 = (50 − h)√3/50
50/3 = 50 − h → h = 50 − 50/3 = 100/3 = 33.33 m
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** A tower subtends an angle α at a point on the same level as its foot. At a second point h m above the first, the angle of depression of the foot of the tower is β. The tower's height is:
(a) h cot α / tan β
(b) h tan α / cot β
(c) h tan α tan β/(tan β − tan α)
(d) None

<details>
<summary>Solution</summary>
Let tower height = H, distance = d
From first: tan α = H/d → d = H cot α
From second point: tan β = d/h → d = h tan β
H cot α = h tan β
H = h tan β tan α
Answer: (b) 🔴 ⭐
</details>

---

**Q2.** From a point on the ground, the angles of elevation of the bottom and top of a transmission tower fixed at the top of a 20 m high building are 45° and 60°. Find the tower's height.
(a) 20(√3 − 1) m
(b) 20√3 m
(c) 20(√3 + 1) m
(d) 15√3 m

<details>
<summary>Solution</summary>
tan 45° = 20/d → d = 20 m
tan 60° = (20 + h)/20
√3 = (20 + h)/20
20 + h = 20√3 → h = 20(√3 − 1) m
Answer: (a) 🟡 ⭐
</details>

---

**Q3.** The angle of elevation of a cloud from a point h m above a lake is α and the angle of depression of its reflection is β. The cloud's height is:
(a) h(tan β + tan α)/(tan β − tan α)
(b) h(tan β − tan α)/(tan β + tan α)
(c) h sin(β − α)/sin(β + α)
(d) h cos(β − α)/cos(β + α)

<details>
<summary>Solution</summary>
Let cloud height from lake = x m, observer at h m above lake.
For cloud: tan α = (x − h)/d → d = (x − h) cot α
For reflection: tan β = (x + h)/d → d = (x + h) cot β
(x − h) cot α = (x + h) cot β
(x − h) tan β = (x + h) tan α
x tan β − h tan β = x tan α + h tan α
x(tan β − tan α) = h(tan β + tan α)
x = h(tan β + tan α)/(tan β − tan α)
Answer: (a) 🔴 ⭐
</details>

---

**Q4.** A person standing on the bank of a river observes that the angle subtended by a tree on the opposite bank is 60°. When he retreats 40 m from the bank, he finds the angle to be 30°. The river's width is:
(a) 20 m
(b) 30 m
(c) 40 m
(d) 60 m

<details>
<summary>Solution</summary>
Let width = w, tree height = h
From bank: tan 60° = h/w → h = w√3
From 40 m back: tan 30° = h/(w + 40)
1/1/√3 = w√3/(w + 40)  <-- wait, cot 30 = √3, tan 30 = 1/√3.
1/√3 = w√3/(w + 40)
w + 40 = 3w → 2w = 40 → w = 20 m
Answer: (a) 🟡 ⭐
</details>

---

**Q5.** A vertical tower stands on a horizontal plane and is surmounted by a vertical flagstaff of height h. At a point on the plane, the angles of elevation of the bottom and top of the flagstaff are α and β respectively. The tower's height is:
(a) h tan α/(tan β − tan α)
(b) h/(tan β − tan α)
(c) h tan α cot β
(d) h sin α/(sin β − sin α)

<details>
<summary>Solution</summary>
Let tower height = H, distance = d
tan α = H/d → d = H cot α
tan β = (H + h)/d → d = (H + h) cot β
H cot α = (H + h) cot β
H cos α/sin α = (H + h) cos β/sin β
Cross-multiply and solve: H = h tan α/(tan β − tan α)
Answer: (a) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** The angle of elevation and angle of depression for the same line of sight are equal.
**Reason (R):** They are alternate interior angles formed by parallel lines.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** If a tower casts a shadow equal to its height, the sun's altitude is 45°.
**Reason (R):** tan θ = height/shadow = 1 → θ = 45°.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The angle of depression can be greater than 90°.
**Reason (R):** Angle of depression is measured from the horizontal downward.

<details>
<summary>Solution</summary>
A is false: angle of depression is between 0° and 90°.
R is true: it's measured from horizontal downward.
Answer: (d)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** If the sun's altitude changes from 30° to 60°, the shadow of a tower becomes one-third of its original length.
**Reason (R):** Shadow length = h × cot θ, and cot 60° = cot 30°/3.

<details>
<summary>Solution</summary>
At 30°: shadow₁ = h cot 30° = h√3
At 60°: shadow₂ = h cot 60° = h/√3
shadow₂/shadow₁ = (h/√3)/(h√3) = 1/3. True.
R: cot 60° = 1/√3 and cot 30°/3 = √3/3 = 1/√3. So R is true and explains A.
Answer: (a) 🔴
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 The angle of elevation of the sun when a 10 m pole casts a 10 m shadow is:
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Let the angle of elevation of the sun be \( \theta \).
The height of the pole is \( 10\text{ m} \) and the length of the shadow is \( 10\text{ m} \).
\[
\tan \theta = \frac{\text{Height}}{\text{Shadow}} = \frac{10}{10} = 1
\]
Since \( \tan(45^\circ) = 1 \), we have \( \theta = 45^\circ \).

**Answer: (b) 45°**
</details>

2. 🟢 A tower 20 m high casts a shadow 20√3 m. The sun's altitude is:
   (a) 30°   (b) 45°   (c) 60°   (d) 15°
<details>
<summary>Solution</summary>

Let the altitude of the sun be \( \theta \).
The height of the tower is \( 20\text{ m} \) and the length of the shadow is \( 20\sqrt{3}\text{ m} \).
\[
\tan \theta = \frac{\text{Height}}{\text{Shadow}} = \frac{20}{20\sqrt{3}} = \frac{1}{\sqrt{3}}
\]
Since \( \tan(30^\circ) = \frac{1}{\sqrt{3}} \), we have \( \theta = 30^\circ \).

**Answer: (a) 30°**
</details>

3. 🟡 A kite flying at 90 m has a 180 m string. The angle with the ground is:
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Let the angle with the ground be \( \theta \).
The height of the kite is \( 90\text{ m} \) and the length of the string is \( 180\text{ m} \).
\[
\sin \theta = \frac{\text{Height}}{\text{Length of string}} = \frac{90}{180} = \frac{1}{2}
\]
Since \( \sin(30^\circ) = \frac{1}{2} \), we have \( \theta = 30^\circ \).

**Answer: (a) 30°**
</details>

4. 🟡 A ladder 10 m long reaches a window 5 m above ground. The ladder's angle with the ground is:
   (a) 30°   (b) 45°   (c) 60°   (d) 90°
<details>
<summary>Solution</summary>

Let the angle of the ladder with the ground be \( \theta \).
The length of the ladder (hypotenuse) is \( 10\text{ m} \) and the height of the window is \( 5\text{ m} \).
\[
\sin \theta = \frac{\text{Height}}{\text{Length of ladder}} = \frac{5}{10} = \frac{1}{2}
\]
Since \( \sin(30^\circ) = \frac{1}{2} \), we have \( \theta = 30^\circ \).

**Answer: (a) 30°**
</details>

5. 🟡 From a point 20 m from a tower, the angle of elevation is 60°. The tower's height is:
   (a) 20 m   (b) 20√3 m   (c) 20/√3 m   (d) 40 m
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \).
The distance from the point to the foot of the tower is \( 20\text{ m} \) and the angle of elevation is \( 60^\circ \).
\[
\tan(60^\circ) = \frac{h}{20} \implies \sqrt{3} = \frac{h}{20} \implies h = 20\sqrt{3}\text{ m}
\]

**Answer: (b) 20√3 m**
</details>

6. 🟡 The angle of depression of a car from a 30 m tower is 30°. The car is at:
   (a) 30 m   (b) 30√3 m   (c) 10√3 m   (d) 10 m
<details>
<summary>Solution</summary>

Let the distance of the car from the base of the tower be \( d \).
The height of the tower is \( 30\text{ m} \) and the angle of depression is \( 30^\circ \).
\[
\tan(30^\circ) = \frac{30}{d} \implies \frac{1}{\sqrt{3}} = \frac{30}{d} \implies d = 30\sqrt{3}\text{ m}
\]

**Answer: (b) 30√3 m**
</details>

7. 🟡 A 1.5 m tall person is 30 m from a tower and sees its top at 45°. The tower's height is:
   (a) 30 m   (b) 31.5 m   (c) 28.5 m   (d) 45 m
<details>
<summary>Solution</summary>

Let the total height of the tower be \( H \) and the height of the tower above the observer's eye level be \( h \).
The distance to the tower is \( 30\text{ m} \).
\[
\tan(45^\circ) = \frac{h}{30} \implies 1 = \frac{h}{30} \implies h = 30\text{ m}
\]
The total height is:
\[
H = h + 1.5 = 30 + 1.5 = 31.5\text{ m}
\]

**Answer: (b) 31.5 m**
</details>

8. 🟡 The angle of elevation changes from 45° to 60° when a person moves 20 m towards a tower. The tower's height is:
   (a) 20√3 m   (b) 10(3 + √3) m   (c) 20 m   (d) 30 m
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \) and the initial distance be \( d \).
1. From the first point:
   \[
   \tan(45^\circ) = \frac{h}{d} \implies d = h
   \]
2. From the second point (after moving \( 20\text{ m} \) closer):
   \[
   \tan(60^\circ) = \frac{h}{d - 20} \implies \sqrt{3} = \frac{h}{h - 20}
   \]
   Cross-multiplying:
   \[
   h\sqrt{3} - 20\sqrt{3} = h \implies h(\sqrt{3} - 1) = 20\sqrt{3}
   \]
   Solving for \( h \):
   \[
   h = \frac{20\sqrt{3}}{\sqrt{3} - 1} = \frac{20\sqrt{3}(\sqrt{3} + 1)}{3 - 1} = 10(3 + \sqrt{3})\text{ m}
   \]

**Answer: (b) 10(3 + √3) m**
</details>

9. 🟢 Which is the best instrument to measure angle of elevation?<br>
   (a) Compass   (b) Theodolite   (c) Barometer   (d) Thermometer
<details>
<summary>Solution</summary>

A **theodolite** is a precision optical instrument used for measuring angles between designated visible points in the horizontal and vertical planes (used extensively in land surveying).

**Answer: (b) Theodolite**
</details>

10. 🟡 The angle of elevation of the top of a tree from a point 25 m away is 45°. The tree's height is:
    (a) 25 m   (b) 25√3 m   (c) 25/√3 m   (d) 12.5 m
<details>
<summary>Solution</summary>

Let the height of the tree be \( h \).
The distance from the observation point to the foot of the tree is \( 25\text{ m} \) and the angle of elevation is \( 45^\circ \).
\[
\tan(45^\circ) = \frac{h}{25} \implies 1 = \frac{h}{25} \implies h = 25\text{ m}
\]

**Answer: (a) 25 m**
</details>

11. 🟡 From a 100 m lighthouse, the angle of depression of a boat is 30°. The boat is:
    (a) 100 m   (b) 100√3 m   (c) 50 m   (d) 200 m
<details>
<summary>Solution</summary>

Let the horizontal distance of the boat from the lighthouse be \( d \).
The height of the lighthouse is \( 100\text{ m} \) and the angle of depression is \( 30^\circ \).
\[
\tan(30^\circ) = \frac{100}{d} \implies \frac{1}{\sqrt{3}} = \frac{100}{d} \implies d = 100\sqrt{3}\text{ m}
\]

**Answer: (b) 100√3 m**
</details>

12. 🟡 The sun's elevation when a 15 m pole casts a 5√3 m shadow is:
    (a) 30°   (b) 45°   (c) 60°   (d) 75°
<details>
<summary>Solution</summary>

Let the angle of elevation of the sun be \( \theta \).
The height of the pole is \( 15\text{ m} \) and the length of the shadow is \( 5\sqrt{3}\text{ m} \).
\[
\tan \theta = \frac{\text{Height}}{\text{Shadow}} = \frac{15}{5\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3}
\]
Since \( \tan(60^\circ) = \sqrt{3} \), we have \( \theta = 60^\circ \).

**Answer: (c) 60°**
</details>

13. 🟡 Two pillars of equal height are 60 m apart. From a point between them, their angles of elevation are 30° and 60°. Their height is:
    (a) 15 m   (b) 15√3 m   (c) 30 m   (d) 45 m
<details>
<summary>Solution</summary>

Let the height of both pillars be \( h \).
Let the point on the ground be at distance \( x \) from the pillar with an angle of elevation of \( 60^\circ \).
Then the distance from the point to the other pillar (elevation \( 30^\circ \)) is \( 60 - x \).

1. For the first pillar:
   \[
   \tan(60^\circ) = \frac{h}{x} \implies h = x\sqrt{3}
   \]
2. For the second pillar:
   \[
   \tan(30^\circ) = \frac{h}{60 - x} \implies h = \frac{60 - x}{\sqrt{3}}
   \]
3. Equating both expressions for \( h \):
   \[
   x\sqrt{3} = \frac{60 - x}{\sqrt{3}} \implies 3x = 60 - x \implies 4x = 60 \implies x = 15\text{ m}
   \]
4. Calculate \( h \):
   \[
   h = 15\sqrt{3}\text{ m}
   \]

**Answer: (b) 15√3 m**
</details>

14. 🟡 From the top of a 30 m building, the angle of depression of a car is 30°. The car is:
    (a) 30√3 m   (b) 30 m   (c) 10√3 m   (d) 90 m
<details>
<summary>Solution</summary>

Let the distance of the car from the foot of the building be \( d \).
The height of the building is \( 30\text{ m} \) and the angle of depression is \( 30^\circ \).
\[
\tan(30^\circ) = \frac{30}{d} \implies \frac{1}{\sqrt{3}} = \frac{30}{d} \implies d = 30\sqrt{3}\text{ m}
\]

**Answer: (a) 30√3 m**
</details>

15. 🟡 A ladder makes 60° with the ground and its foot is 5 m from a wall. The ladder's length is:
    (a) 5 m   (b) 10 m   (c) 5√3 m   (d) 10√3 m
<details>
<summary>Solution</summary>

Let the length of the ladder (hypotenuse) be \( L \).
The foot of the ladder is at a distance of \( 5\text{ m} \) from the wall (base).
The angle of inclination with the ground is \( 60^\circ \).
\[
\cos(60^\circ) = \frac{\text{Base}}{\text{Hypotenuse}} = \frac{5}{L}
\]
Since \( \cos(60^\circ) = \frac{1}{2} \):
\[
\frac{1}{2} = \frac{5}{L} \implies L = 10\text{ m}
\]

**Answer: (b) 10 m**
</details>

16. 🟡 A person moves 30 m towards a tower and the angle of elevation changes from 30° to 60°. The tower's height is:
    (a) 15√3 m   (b) 30√3 m   (c) 15 m   (d) 30 m
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \) and the initial distance be \( d \).
1. From the first point:
   \[
   \tan(30^\circ) = \frac{h}{d} \implies d = h\sqrt{3}
   \]
2. From the second point (after moving \( 30\text{ m} \) closer):
   \[
   \tan(60^\circ) = \frac{h}{d - 30} \implies \sqrt{3} = \frac{h}{h\sqrt{3} - 30}
   \]
   Cross-multiplying:
   \[
   3h - 30\sqrt{3} = h \implies 2h = 30\sqrt{3} \implies h = 15\sqrt{3}\text{ m}
   \]

**Answer: (a) 15√3 m**
</details>

17. 🟡 The angle of elevation of the sun increases from 30° to 60°. The shadow becomes:
    (a) 1/3   (b) 1/2   (c) 2 times   (d) Same
<details>
<summary>Solution</summary>

Let the height of the tower be \( h \).
1. The length of the shadow when the sun's elevation is \( 30^\circ \):
   \[
   s_1 = h \cot(30^\circ) = h\sqrt{3}
   \]
2. The length of the shadow when the sun's elevation is \( 60^\circ \):
   \[
   s_2 = h \cot(60^\circ) = \frac{h}{\sqrt{3}}
   \]
3. Comparing the two shadows:
   \[
   \frac{s_2}{s_1} = \frac{h/\sqrt{3}}{h\sqrt{3}} = \frac{1}{3}
   \]
   Therefore, the shadow becomes \( \frac{1}{3} \) (one-third) of its original length.

**Answer: (a) 1/3**
</details>

18. 🟡 A 7 m tall flagstaff on a 20 m building. From a point, the elevation of the top is 60° and bottom is 45°. The distance is:
    (a) 20 m   (b) 27 m   (c) 7 m   (d) 20√3 m
<details>
<summary>Solution</summary>

Let \( d \) be the horizontal distance of the observation point from the foot of the building.
The building is \( 20\text{ m} \) tall, and the bottom of the flagstaff is the top of the building.
The angle of elevation of the bottom of the flagstaff is \( 45^\circ \):
\[
\tan(45^\circ) = \frac{\text{Height of building}}{\text{Distance}} \implies 1 = \frac{20}{d} \implies d = 20\text{ m}
\]

**Answer: (a) 20 m**
</details>

19. 🟡 The angle of depression of the top of a 10 m pole from the top of a 50 m building is 30°. The distance is:
    (a) 40√3 m   (b) 40/√3 m   (c) 40 m   (d) 20√3 m
<details>
<summary>Solution</summary>

Let \( d \) be the horizontal distance between the building and the pole.
The height of the building is \( 50\text{ m} \) and the height of the pole is \( 10\text{ m} \).
The difference in their heights is:
\[
\Delta h = 50 - 10 = 40\text{ m}
\]
Since the angle of depression of the top of the pole from the top of the building is \( 30^\circ \), we have:
\[
\tan(30^\circ) = \frac{\Delta h}{d} \implies \frac{1}{\sqrt{3}} = \frac{40}{d} \implies d = 40\sqrt{3}\text{ m}
\]

**Answer: (a) 40√3 m**
</details>

20. 🟡 From a point on a 10 m bridge, the angles of depression of opposite banks are 30° and 60°. The river's width is:
    (a) 40/√3 m   (b) 30/√3 m   (c) 20/√3 m   (d) 10/√3 m
<details>
<summary>Solution</summary>

Let the bridge be at a height of \( h = 10\text{ m} \) above the river.
Let the two banks on opposite sides be at distances \( d_1 \) and \( d_2 \) from the point directly below the bridge.
1. For the bank with depression angle \( 30^\circ \):
   \[
   \tan(30^\circ) = \frac{10}{d_1} \implies d_1 = 10\sqrt{3}\text{ m}
   \]
2. For the bank with depression angle \( 60^\circ \):
   \[
   \tan(60^\circ) = \frac{10}{d_2} \implies d_2 = \frac{10}{\sqrt{3}}\text{ m}
   \]
3. The width of the river is:
   \[
   W = d_1 + d_2 = 10\sqrt{3} + \frac{10}{\sqrt{3}} = \frac{30 + 10}{\sqrt{3}} = \frac{40}{\sqrt{3}}\text{ m}
   \]

**Answer: (a) 40/√3 m**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 6 | b | 11 | b | 16 | a |
| 2 | a | 7 | b | 12 | c | 17 | a |
| 3 | a | 8 | b | 13 | b | 18 | a |
| 4 | a | 9 | b | 14 | a | 19 | a |
| 5 | b | 10 | a | 15 | b | 20 | a |

</details>
