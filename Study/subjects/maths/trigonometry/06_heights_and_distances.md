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

2. 🟢 A tree 10 m high casts a shadow of length 10√3 m. Find the sun's altitude.

3. 🟡 A kite flying at a height of 75 m from the ground has a string of length 150 m. Find the angle the string makes with the ground.

4. 🟡 An observer 1.5 m tall is 30 m away from a tower. The angle of elevation of the top of the tower from his eye is 45°. Find the tower's height.

5. 🟡 From a point 100 m from the foot of a tower, the angle of elevation of its top is 60°. Find the tower's height.

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

7. 🟡 From the top of a 60 m tower, the angle of depression of the top and bottom of a building are 30° and 60°. Find the height of the building.

8. 🟡 A person observes the angle of elevation of the top of a tower from a point to be 45°. He moves 20 m towards the tower and the angle becomes 60°. Find the tower's height.

9. 🔴 ⭐ A flagstaff stands on top of a 10 m high tower. From a point on the ground, the angles of elevation of the top and bottom of the flagstaff are 45° and 30°. Find the height of the flagstaff.

10. 🔴 From an aeroplane flying at a height of 3000 m, the angles of depression of two points on the ground, 30° apart, are 45° and 30°. Find the aeroplane's distance from the points.

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

12. 🟡 The angle of elevation of a cloud from a point 60 m above a lake is 30° and the angle of depression of its reflection in the lake is 60°. Find the height of the cloud.

13. 🔴 A person standing on the bank of a river observes the angle of elevation of the top of a tree on the opposite bank as 60°. When he moves 40 m away from the bank, the angle becomes 30°. Find the river's width and tree's height.

14. 🔴 ⭐ The angle of elevation of a jet plane from a point on the ground is 60°. After 15 seconds, the angle changes to 30°. If the plane is flying at 3000√3 m, find its speed.

15. 🔴 From the top of a 75 m lighthouse, the angles of depression of two ships are 30° and 45°. If one ship is behind the other, find the distance between them.

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

17. 🟡 A 7 m tall pole stands on the ground. From a point on the ground, the angles of elevation of the top and bottom of a flagstaff on the pole are 60° and 45°. Find the flagstaff's height.

18. 🔴 Two ships are sailing in the sea on either side of a lighthouse. The angles of depression from the top of the 100 m lighthouse are 45° and 30°. Find the distance between the ships.

19. 🔴 ⭐ From an aeroplane 2000 m above the sea, the angles of depression of two rocks on the same line are 30° and 60°. Find the distance between the rocks.

20. 🔴 The angle of elevation of the top of a tower from the foot of a building is 60° and the angle of elevation of the top of the building from the foot of the tower is 30°. If the tower is 60 m high, find the building's height.

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

22. 🟡 An observer 1.8 m tall stands 30 m from a chimney. The angle of elevation of the top of the chimney from his eye is 60°. Find the chimney's height.

23. 🟡 From the top of a 25 m building, the angle of depression of a car on a road is 60°. Find the distance of the car from the building.

24. 🔴 A man on the top of a 40 m building observes a car moving towards him. At an instant, the angle of depression is 45°. After 5 seconds, it becomes 60°. Find the speed of the car.

25. 🔴 ⭐ A ladder rests against a vertical wall at an inclination of 60° to the horizontal. Its foot is pulled away from the wall through a distance x so that its upper end slides 4 m down the wall, and the inclination becomes 30°. Find x and the ladder's length.

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

27. 🔴 ⭐ From a point, the angle of elevation of a tower is 30°. On walking 100 m towards the tower, the angle becomes 60°. Find the height.

28. 🔴 A vertical pole and a tower are on the same level ground. From the top of the pole, the angle of elevation of the top of the tower is 60° and the angle of depression of the foot is 30°. If the pole is 10 m high, find the tower's height.

29. 🔴 A man on a cliff observes a boat at an angle of depression of 30° which is approaching the shore. After 10 minutes, the angle becomes 60°. How much more time will the boat take to reach the shore?<br>

30. 🔴 ⭐ Two pillars of equal height stand on either side of a road 100 m wide. From a point on the road between them, the angles of elevation of their tops are 30° and 60°. Find the height of the pillars and the point's position.

---

## Stage 4: Type Mixer

1. 🟡 A tower is 50 m tall. From the top, the angles of depression of two cars on the ground are 30° and 45°. If the cars are on the same side of the tower, find the distance between them.

2. 🟡 From the top of a 60 m high building, the angle of depression of the top and bottom of a tower are 30° and 60°. Find the tower's height.

3. 🔴 ⭐ The angle of elevation of the top of a vertical tower from a point on the ground is 60°. From a point 40 m vertically above the first point, its angle of elevation is 30°. Find the tower's height and horizontal distance.

4. 🔴 From a point on a bridge across a river, the angles of depression of the banks on opposite sides are 30° and 60°. If the bridge is 12 m above the river, find the river's width.

5. 🔴 Two men on opposite sides of a 60 m high tower observe its top at angles 30° and 60°. Find the distance between the men.

---

## Stage 5: Board Arsenal

**Q1.** 🟡 The angle of elevation of the top of a tower from a point 30 m away is 30°. Find the tower's height. **(2 marks)**

**Solution:**
```
tan 30° = h/30
h = 30 × 1/√3 = 30/√3 = 10√3 m
```

---

**Q2.** 🟡 A kite flying at a height of 60 m has a string of length 120 m. Find the angle the string makes with the ground. **(2 marks)**

**Solution:**
```
sin θ = 60/120 = 1/2
θ = 30°
```

---

**Q3.** 🟡 A ladder 20 m long makes an angle of 60° with the ground. Find the height of the window it reaches. **(3 marks)**

**Solution:**
```
sin 60° = h/20
h = 20 × √3/2 = 10√3 m
```

---

**Q4.** 🔴 ⭐ From the top of a 50 m building, the angle of depression of the top and bottom of another building are 30° and 60°. Find the other building's height. **(3 marks)**

**Solution:**
```
Let other building's height = h, distance between them = d

From top of 50 m building:
Depression to bottom = 60°: tan 60° = 50/d → d = 50/√3 m
Depression to top = 30°: tan 30° = (50 − h)/d
1/√3 = (50 − h)/(50/√3)
1/√3 = (50 − h)√3/50
50/3 = 50 − h → h = 50 − 50/3 = 100/3 = 33.33 m
```

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

2. 🟢 A tower 20 m high casts a shadow 20√3 m. The sun's altitude is:
   (a) 30°   (b) 45°   (c) 60°   (d) 15°

3. 🟡 A kite flying at 90 m has a 180 m string. The angle with the ground is:
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

4. 🟡 A ladder 10 m long reaches a window 5 m above ground. The ladder's angle with the ground is:
   (a) 30°   (b) 45°   (c) 60°   (d) 90°

5. 🟡 From a point 20 m from a tower, the angle of elevation is 60°. The tower's height is:
   (a) 20 m   (b) 20√3 m   (c) 20/√3 m   (d) 40 m

6. 🟡 The angle of depression of a car from a 30 m tower is 30°. The car is at:
   (a) 30 m   (b) 30√3 m   (c) 10√3 m   (d) 10 m

7. 🟡 A 1.5 m tall person is 30 m from a tower and sees its top at 45°. The tower's height is:
   (a) 30 m   (b) 31.5 m   (c) 28.5 m   (d) 45 m

8. 🟡 The angle of elevation changes from 45° to 60° when a person moves 20 m towards a tower. The tower's height is:
   (a) 20√3 m   (b) 10(3 + √3) m   (c) 20 m   (d) 30 m

9. 🟢 Which is the best instrument to measure angle of elevation?<br>
   (a) Compass   (b) Theodolite   (c) Barometer   (d) Thermometer

10. 🟡 The angle of elevation of the top of a tree from a point 25 m away is 45°. The tree's height is:
    (a) 25 m   (b) 25√3 m   (c) 25/√3 m   (d) 12.5 m

11. 🟡 From a 100 m lighthouse, the angle of depression of a boat is 30°. The boat is:
    (a) 100 m   (b) 100√3 m   (c) 50 m   (d) 200 m

12. 🟡 The sun's elevation when a 15 m pole casts a 5√3 m shadow is:
    (a) 30°   (b) 45°   (c) 60°   (d) 75°

13. 🟡 Two pillars of equal height are 60 m apart. From a point between them, their angles of elevation are 30° and 60°. Their height is:
    (a) 15 m   (b) 15√3 m   (c) 30 m   (d) 45 m

14. 🟡 From the top of a 30 m building, the angle of depression of a car is 30°. The car is:
    (a) 30√3 m   (b) 30 m   (c) 10√3 m   (d) 90 m

15. 🟡 A ladder makes 60° with the ground and its foot is 5 m from a wall. The ladder's length is:
    (a) 5 m   (b) 10 m   (c) 5√3 m   (d) 10√3 m

16. 🟡 A person moves 30 m towards a tower and the angle of elevation changes from 30° to 60°. The tower's height is:
    (a) 15√3 m   (b) 30√3 m   (c) 15 m   (d) 30 m

17. 🟡 The angle of elevation of the sun increases from 30° to 60°. The shadow becomes:
    (a) 1/3   (b) 1/2   (c) 2 times   (d) Same

18. 🟡 A 7 m tall flagstaff on a 20 m building. From a point, the elevation of the top is 60° and bottom is 45°. The distance is:
    (a) 20 m   (b) 27 m   (c) 7 m   (d) 20√3 m

19. 🟡 The angle of depression of the top of a 10 m pole from the top of a 50 m building is 30°. The distance is:
    (a) 40√3 m   (b) 40/√3 m   (c) 40 m   (d) 20√3 m

20. 🟡 From a point on a 10 m bridge, the angles of depression of opposite banks are 30° and 60°. The river's width is:
    (a) 40/√3 m   (b) 30/√3 m   (c) 20/√3 m   (d) 10/√3 m

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
