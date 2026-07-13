# Chapter 3: Vector Addition — The Geometry of Combining

> *NCERT: Class 11 Physics 4.3, 4.4 | Class 12 Maths 10.3*

---

## 🎯 Stage 1: The Core Idea

Imagine you are walking in a city. You walk 3 km East, and then 4 km North. Are you 7 km away from your starting point? If you calculate the shortest distance (the straight-line path), you are only 5 km away. This simple realization is the essence of vector addition. When quantities have direction, you cannot just add their magnitudes using simple arithmetic. You have to respect their directions. This is the **Triangle Law of Vector Addition**: if you arrange vectors head-to-tail, the net result (the **resultant**) is the vector drawn from the tail of the first to the head of the last.

Now, imagine a different scenario. A cart is stuck in the mud, and two horses are pulling it. Both horses are tied to the exact same point on the cart, but they are pulling in slightly different directions. How will the cart move? It won't move in the direction of horse A alone, nor horse B alone. It will move diagonally between them. This is the **Parallelogram Law of Vector Addition**: when two vectors start from the *same origin* (tail-to-tail), they form the adjacent sides of a parallelogram. The resultant is the diagonal passing through that common origin. 

In the vector world, $1 + 1$ rarely equals $2$. Depending on the angle between the vectors, adding two vectors of magnitude 1 could give you a resultant of 2 (if they point the same way), 0 (if they point in opposite directions), or anything in between.

> ⚠️ **Critical Insight:** The angle $\theta$ between two vectors is ALWAYS measured when they are joined **tail-to-tail** or **head-to-head**. If one vector's head touches another's tail, you must slide one forward along its line of action to find the true angle between them.

> 💡 **Tip:** The Triangle Law is perfect for *sequential* actions (like taking multiple displacements one after the other). The Parallelogram Law is perfect for *simultaneous* actions (like two forces pulling an object at the exact same time).

> 🔑 **Key Takeaway:** The resultant of two vectors $\vec{A}$ and $\vec{B}$ can never be greater than $A+B$ and can never be less than $|A-B|$. This range $[|A-B|, A+B]$ represents all possible answers depending on the angle!

If we have more than two vectors (e.g., walking 5 different paths in a row), we use the **Polygon Law**. You just keep connecting them head-to-tail. The final resultant is the vector from the very first tail to the very last head. If you end up exactly where you started, the resultant is zero (a closed polygon).

---

## 🔬 Stage 2: The Formula Lab

To calculate the magnitude and direction of the resultant without drawing scale diagrams, we use the analytical method derived from the Parallelogram Law.

**Magnitude of the Resultant ($R$):**
$$R = |\vec{R}| = \sqrt{A^2 + B^2 + 2AB \cos\theta}$$

**Direction of the Resultant ($\alpha$ from $\vec{A}$):**
$$\tan \alpha = \frac{B \sin\theta}{A + B \cos\theta}$$

**Variable Table:**

| Symbol | Meaning | Unit / Note |
| :--- | :--- | :--- |
| $A$ | Magnitude of the first vector $\vec{A}$ | Same as vector units (e.g., N, m/s) |
| $B$ | Magnitude of the second vector $\vec{B}$ | Same as vector units |
| $\theta$ | Angle between $\vec{A}$ and $\vec{B}$ | Degrees/Radians. Measured tail-to-tail. |
| $R$ | Magnitude of the Resultant $\vec{R}$ | Same as vector units |
| $\alpha$ | Angle the Resultant makes with vector $\vec{A}$ | Degrees/Radians |

**What this formula says:** 
The magnitude formula is a generalization of the Pythagorean theorem. If $\theta = 90^\circ$, the term $2AB\cos\theta$ becomes zero, and it perfectly collapses back to $R = \sqrt{A^2 + B^2}$. The extra term accounts for how much the vectors "help" or "hinder" each other based on their alignment. The direction formula splits $\vec{B}$ into components perpendicular to $\vec{A}$ ($B\sin\theta$) and parallel to $\vec{A}$ ($B\cos\theta$), and takes their ratio to find the tangent.

**Special Angle Cases:**

| Angle ($\theta$) | Condition | Resultant Magnitude ($R$) | Direction |
| :---: | :--- | :--- | :--- |
| **$0^\circ$** | Parallel (Same direction) | $R = A + B$ **(Maximum)** | Along both vectors |
| **$90^\circ$** | Perpendicular | $R = \sqrt{A^2 + B^2}$ | $\tan\alpha = B/A$ |
| **$180^\circ$** | Anti-parallel (Opposite) | $R = \|A - B\|$ **(Minimum)** | In direction of larger vector |

**The "Equal Vectors" Shortcut:**
When two vectors have the *exact same magnitude* ($A = B = x$), the formulas simplify beautifully. The resultant exactly bisects the angle between them ($\alpha = \theta/2$), and the magnitude is:
$$R = 2x \cos\left(\frac{\theta}{2}\right)$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Direct Formula Application ⭐
**Pattern:** "Given two magnitudes and the angle between them, find the resultant magnitude and direction."

**Solved Example** 🟢
> Two forces of $3 \text{ N}$ and $4 \text{ N}$ are acting on a body at an angle of $60^\circ$ to each other. Find the magnitude and direction of the resultant force.
<details><summary><b>Solution</b></summary>
Given: $A = 3 \text{ N}$, $B = 4 \text{ N}$, $\theta = 60^\circ$.
**Magnitude:**
$$R = \sqrt{A^2 + B^2 + 2AB \cos\theta}$$
$$R = \sqrt{3^2 + 4^2 + 2(3)(4) \cos 60^\circ}$$
$$R = \sqrt{9 + 16 + 24(1/2)}$$
$$R = \sqrt{25 + 12} = \sqrt{37} \approx 6.08 \text{ N}$$
**Direction ($\alpha$ with respect to 3 N force):**
$$\tan \alpha = \frac{B \sin\theta}{A + B \cos\theta}$$
$$\tan \alpha = \frac{4 \sin 60^\circ}{3 + 4 \cos 60^\circ}$$
$$\tan \alpha = \frac{4(\sqrt{3}/2)}{3 + 4(1/2)} = \frac{2\sqrt{3}}{3 + 2} = \frac{2\sqrt{3}}{5}$$
$$\alpha = \tan^{-1}\left(\frac{2\sqrt{3}}{5}\right)$$
</details>

**Practice:**
1. 🟢 Two forces of $5 \text{ N}$ and $12 \text{ N}$ act at an angle of $90^\circ$. Find their resultant magnitude.
<details><summary><b>Answer</b></summary>
$R = \sqrt{5^2 + 12^2 + 0} = \sqrt{25 + 144} = \sqrt{169} = 13 \text{ N}$.
</details>

2. 🟢 Find the resultant of two vectors of magnitudes $6 \text{ units}$ and $8 \text{ units}$ acting at an angle of $60^\circ$.
<details><summary><b>Answer</b></summary>
$R = \sqrt{6^2 + 8^2 + 2(6)(8)\cos 60^\circ} = \sqrt{36 + 64 + 48} = \sqrt{148} = 2\sqrt{37} \text{ units}$.
</details>

3. 🟢 Two forces of $10 \text{ N}$ each act at an angle of $120^\circ$. Find the magnitude of the resultant.
<details><summary><b>Answer</b></summary>
$R = \sqrt{100 + 100 + 200(-1/2)} = \sqrt{100} = 10 \text{ N}$.
</details>

4. 🟡 Two velocity vectors of $15 \text{ m/s}$ and $20 \text{ m/s}$ act at an angle of $53^\circ$. Find the resultant magnitude. ($\cos 53^\circ = 3/5$)
<details><summary><b>Answer</b></summary>
$R = \sqrt{225 + 400 + 2(15)(20)(3/5)} = \sqrt{625 + 360} = \sqrt{985} \approx 31.38 \text{ m/s}$.
</details>

5. 🟡 Find the angle the resultant makes with the $6 \text{ unit}$ vector in question 2.
<details><summary><b>Answer</b></summary>
$\tan \alpha = \frac{8 \sin 60^\circ}{6 + 8 \cos 60^\circ} = \frac{4\sqrt{3}}{6 + 4} = \frac{4\sqrt{3}}{10} = \frac{2\sqrt{3}}{5}$.
$\alpha = \tan^{-1}(2\sqrt{3}/5)$.
</details>

6. 🔴 Two forces $P$ and $Q$ act at an angle $\theta$. If $P = 3 \text{ N}$, $Q = 5 \text{ N}$ and $R = 7 \text{ N}$, find the angle $\theta$.
<details><summary><b>Answer</b></summary>
$R^2 = P^2 + Q^2 + 2PQ \cos\theta$
$49 = 9 + 25 + 2(3)(5)\cos\theta$
$49 = 34 + 30\cos\theta \implies 15 = 30\cos\theta \implies \cos\theta = 1/2$.
$\theta = 60^\circ$.
</details>

7. 🔴 Two vectors of magnitudes $3$ and $4$ give a resultant of magnitude $5$. What is the angle between them?
<details><summary><b>Answer</b></summary>
$5^2 = 3^2 + 4^2 \implies 25 = 25$. This happens only when $\cos\theta = 0$, so $\theta = 90^\circ$.
</details>


### Type 2: Maximum and Minimum Resultant ⭐
**Pattern:** "Given max and min values of resultant, or analyzing conditions for parallel/anti-parallel alignment."

**Solved Example** 🟡
> The maximum and minimum magnitudes of the resultant of two vectors are $17 \text{ units}$ and $7 \text{ units}$ respectively. If these two vectors act at right angles to each other, what is the magnitude of their resultant?
<details><summary><b>Solution</b></summary>
Let the magnitudes of the two vectors be $A$ and $B$.
Maximum resultant occurs at $\theta = 0^\circ$:
$R_{max} = A + B = 17$  --- (1)
Minimum resultant occurs at $\theta = 180^\circ$:
$R_{min} = |A - B| = 7$  --- (2)
Assuming $A > B$, adding (1) and (2) gives:
$2A = 24 \implies A = 12 \text{ units}$
Substituting $A$ in (1):
$12 + B = 17 \implies B = 5 \text{ units}$
When they act at right angles ($\theta = 90^\circ$):
$R = \sqrt{A^2 + B^2} = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13 \text{ units}$.
</details>

**Practice:**
1. 🟢 The maximum resultant of two forces is $20 \text{ N}$ and minimum is $4 \text{ N}$. Find the magnitudes of the forces.
<details><summary><b>Answer</b></summary>
$A + B = 20$
$A - B = 4$
Adding: $2A = 24 \implies A = 12 \text{ N}$.
$B = 8 \text{ N}$.
</details>

2. 🟢 Can the resultant of two vectors of magnitudes $5$ and $8$ be $2$?
<details><summary><b>Answer</b></summary>
$R_{max} = 13$, $R_{min} = |8-5| = 3$. The resultant must lie in $[3, 13]$.
Therefore, 2 is **not possible**.
</details>

3. 🟡 If the maximum resultant of two vectors is twice their minimum resultant, what is the ratio of their magnitudes?
<details><summary><b>Answer</b></summary>
$A + B = 2(A - B) \implies A + B = 2A - 2B \implies A = 3B$.
Ratio $A:B = 3:1$.
</details>

4. 🟡 Two forces have a maximum resultant of $P$ and minimum resultant of $Q$. Find the resultant when they are at $90^\circ$.
<details><summary><b>Answer</b></summary>
$A+B = P$, $A-B = Q$.
$A = (P+Q)/2$, $B = (P-Q)/2$.
$R^2 = A^2 + B^2 = \frac{(P+Q)^2}{4} + \frac{(P-Q)^2}{4} = \frac{2P^2 + 2Q^2}{4} = \frac{P^2+Q^2}{2}$.
$R = \sqrt{\frac{P^2+Q^2}{2}}$.
</details>

5. 🟡 Find the resultant of forces $10 \text{ N}$ and $15 \text{ N}$ acting in opposite directions.
<details><summary><b>Answer</b></summary>
Angle is $180^\circ$. $R = |10 - 15| = 5 \text{ N}$ in the direction of the $15 \text{ N}$ force.
</details>

6. 🔴 Two forces have magnitudes in the ratio $3:5$. If their maximum resultant is $24 \text{ N}$, find their minimum resultant.
<details><summary><b>Answer</b></summary>
Let forces be $3x$ and $5x$. Max resultant = $3x + 5x = 8x = 24 \implies x = 3$.
Forces are $9 \text{ N}$ and $15 \text{ N}$.
Min resultant = $|15 - 9| = 6 \text{ N}$.
</details>

7. 🔴 A particle is acted upon by two forces of $4 \text{ N}$ and $3 \text{ N}$. The resultant cannot be: (a) $1 \text{ N}$ (b) $5 \text{ N}$ (c) $7 \text{ N}$ (d) $8 \text{ N}$.
<details><summary><b>Answer</b></summary>
Range is $[|4-3|, 4+3] = [1, 7]$. Thus, $8 \text{ N}$ is impossible. Answer is (d).
</details>


### Type 3: Resultant of Equal Vectors ⭐
**Pattern:** "Two vectors of equal magnitude $F$ act at an angle $\theta$. Use $R = 2F \cos(\theta/2)$."

**Solved Example** 🟡
> Two equal forces have a resultant equal to either of the two forces. Find the angle between them.
<details><summary><b>Solution</b></summary>
Let the magnitude of the forces be $F$. Thus, $A = F$ and $B = F$.
The resultant also has magnitude $F$, so $R = F$.
Using the formula for equal vectors:
$$R = 2F \cos\left(\frac{\theta}{2}\right)$$
Substitute $R = F$:
$$F = 2F \cos\left(\frac{\theta}{2}\right)$$
$$\frac{1}{2} = \cos\left(\frac{\theta}{2}\right)$$
Since $\cos(60^\circ) = 1/2$, we have:
$$\frac{\theta}{2} = 60^\circ \implies \theta = 120^\circ$$
The angle between them is $120^\circ$. (This is a very important standard result to memorize!).
</details>

**Practice:**
1. 🟢 Find the resultant of two equal vectors of $10 \text{ units}$ each acting at $60^\circ$.
<details><summary><b>Answer</b></summary>
$R = 2(10)\cos(60^\circ/2) = 20\cos(30^\circ) = 20(\sqrt{3}/2) = 10\sqrt{3} \text{ units}$.
</details>

2. 🟢 Two equal forces act at an angle of $90^\circ$. If their resultant is $14.14 \text{ N}$, find the magnitude of each force. ($\sqrt{2} \approx 1.414$)
<details><summary><b>Answer</b></summary>
$R = \sqrt{F^2 + F^2} = F\sqrt{2}$.
$14.14 = F \times 1.414 \implies F = 10 \text{ N}$.
</details>

3. 🟡 At what angle should two equal forces act so that their resultant is $\sqrt{3}$ times either force?
<details><summary><b>Answer</b></summary>
$R = \sqrt{3}F$.
$2F\cos(\theta/2) = \sqrt{3}F \implies \cos(\theta/2) = \sqrt{3}/2 \implies \theta/2 = 30^\circ \implies \theta = 60^\circ$.
</details>

4. 🟡 Two equal vectors have a resultant equal to $\sqrt{2}$ times either vector. What is the angle between them?
<details><summary><b>Answer</b></summary>
$2F\cos(\theta/2) = \sqrt{2}F \implies \cos(\theta/2) = 1/\sqrt{2} \implies \theta/2 = 45^\circ \implies \theta = 90^\circ$.
</details>

5. 🔴 The resultant of two equal vectors makes an angle $\alpha$ with either vector. What is $\alpha$ in terms of the angle $\theta$ between the vectors?
<details><summary><b>Answer</b></summary>
For equal vectors, the resultant exactly bisects the angle. Thus $\alpha = \theta/2$.
</details>

6. 🔴 Two forces $F$ and $F$ act at an angle of $180^\circ$. Find their resultant using the equal vectors formula.
<details><summary><b>Answer</b></summary>
$R = 2F \cos(180^\circ/2) = 2F \cos(90^\circ) = 2F(0) = 0$. Matches $R_{min} = F-F=0$.
</details>

7. 🔴 If the sum of two unit vectors is also a unit vector, find the magnitude of their difference.
<details><summary><b>Answer</b></summary>
Magnitude of sum is $1$. $1 = \sqrt{1^2 + 1^2 + 2(1)(1)\cos\theta} \implies 1 = 2 + 2\cos\theta \implies \cos\theta = -1/2 \implies \theta = 120^\circ$.
Magnitude of difference = $\sqrt{1^2 + 1^2 - 2(1)(1)\cos 120^\circ} = \sqrt{2 - 2(-1/2)} = \sqrt{3}$.
</details>


### Type 4: Resultant is Perpendicular to One Vector ⭐
**Pattern:** "The resultant $\vec{R}$ is perpendicular to the smaller vector $\vec{A}$. We use $A + B\cos\theta = 0$ or Pythagorean approach."

**Solved Example** 🔴
> The resultant of two vectors $\vec{P}$ and $\vec{Q}$ is perpendicular to $\vec{P}$ and its magnitude is half of that of $\vec{Q}$. Find the angle between $\vec{P}$ and $\vec{Q}$.
<details><summary><b>Solution</b></summary>
Since $\vec{R}$ is perpendicular to $\vec{P}$, the angle $\alpha = 90^\circ$.
Using the direction formula:
$\tan 90^\circ = \frac{Q \sin\theta}{P + Q \cos\theta} \implies \infty = \frac{Q \sin\theta}{P + Q \cos\theta}$
This implies the denominator is zero:
$P + Q \cos\theta = 0 \implies \cos\theta = -\frac{P}{Q}$  --- (1)
Also, we are given $R = \frac{Q}{2}$.
Since $\vec{P}$, $\vec{R}$, and $\vec{Q}$ form a right-angled triangle (with $Q$ as hypotenuse):
$Q^2 = P^2 + R^2$
$Q^2 = P^2 + (Q/2)^2 = P^2 + Q^2/4$
$P^2 = Q^2 - Q^2/4 = \frac{3Q^2}{4}$
$P = \frac{\sqrt{3}Q}{2}$
Substitute $P$ in (1):
$\cos\theta = -\frac{\sqrt{3}Q/2}{Q} = -\frac{\sqrt{3}}{2}$
Therefore, $\theta = 150^\circ$.
</details>

**Practice:**
1. 🟡 The resultant of vectors $\vec{A}$ and $\vec{B}$ is perpendicular to $\vec{A}$. What is the condition for this to happen?
<details><summary><b>Answer</b></summary>
The denominator of the $\tan\alpha$ formula must be zero: $A + B\cos\theta = 0$.
</details>

2. 🟡 If resultant is perpendicular to $\vec{A}$, express $R$ in terms of $A$ and $B$ only.
<details><summary><b>Answer</b></summary>
From right triangle, $R^2 + A^2 = B^2 \implies R = \sqrt{B^2 - A^2}$.
</details>

3. 🔴 The resultant of two vectors of magnitudes $3$ and $5$ is perpendicular to the vector of magnitude $3$. Find the angle between them.
<details><summary><b>Answer</b></summary>
$A = 3$, $B = 5$.
$\cos\theta = -A/B = -3/5$.
$\theta = \cos^{-1}(-3/5) = 180^\circ - 53^\circ = 127^\circ$.
</details>

4. 🔴 The resultant of two vectors is perpendicular to the smaller vector and has magnitude equal to $8$. If the sum of magnitudes of vectors is $16$, find the magnitudes.
<details><summary><b>Answer</b></summary>
Let vectors be $A$ and $B$, $R \perp A \implies B^2 - A^2 = R^2 = 64$.
Given $A + B = 16$.
$(B-A)(B+A) = 64 \implies (B-A)(16) = 64 \implies B-A = 4$.
Solving $B+A=16$ and $B-A=4$: $2B = 20 \implies B=10$, $A=6$.
</details>

5. 🔴 Two forces have a resultant of $4 \text{ N}$ which is perpendicular to the smaller force. If the larger force is $5 \text{ N}$, what is the smaller force?
<details><summary><b>Answer</b></summary>
$R=4$, $B=5$.
$R^2 + A^2 = B^2 \implies 16 + A^2 = 25 \implies A^2 = 9 \implies A = 3 \text{ N}$.
</details>

6. 🔴 In the previous question, what is the angle between the two forces?
<details><summary><b>Answer</b></summary>
$\cos\theta = -A/B = -3/5 \implies \theta = 127^\circ$.
</details>

7. 🔴 If $A=B$, can the resultant ever be perpendicular to $A$?
<details><summary><b>Answer</b></summary>
$\cos\theta = -A/B = -A/A = -1 \implies \theta = 180^\circ$.
At $180^\circ$, resultant is zero, which has no specific direction. Thus, non-zero resultant cannot be perpendicular to $A$ if magnitudes are equal.
</details>


### Type 5: Working Backwards ⭐
**Pattern:** "Given resultant and angles, find the original vector components. Uses Sine Rule heavily."

**Solved Example** 🔴
> A force of $100 \text{ N}$ is resolved into two components such that one component is at $30^\circ$ to the force and the other is at $45^\circ$. Find the magnitudes of the components.
<details><summary><b>Solution</b></summary>
Let the resultant be $\vec{R}$ with $R = 100 \text{ N}$. It is composed of vectors $\vec{A}$ and $\vec{B}$.
Angle between $\vec{R}$ and $\vec{A}$ is $\alpha = 30^\circ$.
Angle between $\vec{R}$ and $\vec{B}$ is $\beta = 45^\circ$.
The total angle between $\vec{A}$ and $\vec{B}$ is $\theta = \alpha + \beta = 75^\circ$.
Using the Sine Rule on the vector triangle:
$$\frac{A}{\sin\beta} = \frac{B}{\sin\alpha} = \frac{R}{\sin(180^\circ - \theta)} = \frac{R}{\sin\theta}$$
To find $A$:
$$A = \frac{R \sin\beta}{\sin\theta} = \frac{100 \sin 45^\circ}{\sin 75^\circ} = \frac{100 (1/\sqrt{2})}{0.965} \approx 73.2 \text{ N}$$
To find $B$:
$$B = \frac{R \sin\alpha}{\sin\theta} = \frac{100 \sin 30^\circ}{\sin 75^\circ} = \frac{100 (0.5)}{0.965} \approx 51.8 \text{ N}$$
</details>

**Practice:**
1. 🟡 A resultant force of $50 \text{ N}$ makes angles of $30^\circ$ and $60^\circ$ with its two components. Find the components.
<details><summary><b>Answer</b></summary>
$\theta = 90^\circ$. Components are orthogonal.
$A = R \cos 30^\circ = 50(\sqrt{3}/2) = 25\sqrt{3} \text{ N}$.
$B = R \sin 30^\circ = 50(1/2) = 25 \text{ N}$.
</details>

2. 🟡 Can a force of $10 \text{ N}$ be resolved into two components of $20 \text{ N}$ and $30 \text{ N}$?
<details><summary><b>Answer</b></summary>
No. The resultant must lie between $|A-B|$ and $A+B$. Here $[|30-20|, 30+20] = [10, 50]$.
Wait, yes it can! The resultant $10$ is the minimum value when they act at $180^\circ$. So yes, if they act opposite.
</details>

3. 🔴 A vector $\vec{R}$ makes equal angles with two vectors $\vec{A}$ and $\vec{B}$ of which it is the sum. What can you say about $\vec{A}$ and $\vec{B}$?
<details><summary><b>Answer</b></summary>
Using Sine Rule: $A/\sin\alpha = B/\sin\alpha \implies A = B$. The magnitudes must be equal.
</details>

4. 🔴 A force $F$ is resolved into two equal components. If the angle between the components is $120^\circ$, find the magnitude of each component.
<details><summary><b>Answer</b></summary>
$R = F$. For equal vectors at $120^\circ$, $R = A = B$. Thus each component is $F$.
</details>

5. 🔴 Given $\vec{R} = \vec{P} + \vec{Q}$. Angle between $\vec{R}$ and $\vec{P}$ is $\alpha$, and $\vec{R}$ and $\vec{Q}$ is $\beta$. If $P > Q$, compare $\alpha$ and $\beta$.
<details><summary><b>Answer</b></summary>
$P/\sin\beta = Q/\sin\alpha$. If $P > Q$, then $\sin\beta > \sin\alpha \implies \beta > \alpha$. The resultant is always closer to the larger vector.
</details>

6. 🔴 A weight of $100 \text{ N}$ is suspended by two strings making angles $30^\circ$ and $60^\circ$ with the horizontal. Find tensions in the strings.
<details><summary><b>Answer</b></summary>
The strings make $90^\circ$ with each other. The $100 \text{ N}$ balances them.
$T_1 = 100 \cos 60^\circ = 50 \text{ N}$, $T_2 = 100 \cos 30^\circ = 50\sqrt{3} \text{ N}$.
</details>

7. 🔴 Find the components of a $10 \text{ unit}$ vector along two directions making $45^\circ$ on either side of it.
<details><summary><b>Answer</b></summary>
Equal angles means equal magnitudes. $2A\cos(90^\circ/2) = 10 \implies 2A\cos 45^\circ = 10 \implies 2A(1/\sqrt{2}) = 10 \implies A\sqrt{2} = 10 \implies A = 5\sqrt{2}$.
</details>


### Type 6: Polygon Law & Equilibrium ⭐
**Pattern:** "Three or more vectors summing to zero, forming a closed polygon."

**Solved Example** 🟡
> Five forces of $10 \text{ N}$ each act at a point. The angle between any two consecutive forces is $72^\circ$. Find the resultant.
<details><summary><b>Solution</b></summary>
Since all forces are equal and equally spaced ($360^\circ / 5 = 72^\circ$), they can be represented by the sides of a regular pentagon taken in order.
According to the Polygon Law of Vector Addition, when vectors form a closed polygon taken in the same order, their resultant is ZERO.
Resultant = $0$.
</details>

**Practice:**
1. 🟢 Four equal vectors act at a point, angle between consecutive ones being $90^\circ$. Find resultant.
<details><summary><b>Answer</b></summary>
They form a closed square. Resultant = $0$.
</details>

2. 🟢 Can three vectors of magnitudes $3$, $4$, and $8$ produce zero resultant?
<details><summary><b>Answer</b></summary>
For zero resultant, they must form a closed triangle. The sum of any two sides must be $\ge$ the third. $3+4 = 7 < 8$. Triangle impossible. Resultant cannot be zero.
</details>

3. 🟡 Minimum number of unequal coplanar vectors required to produce zero resultant is:
<details><summary><b>Answer</b></summary>
Three. (Two must be equal and opposite to give zero, so if unequal, you need at least three).
</details>

4. 🟡 Minimum number of non-coplanar vectors required to produce zero resultant is:
<details><summary><b>Answer</b></summary>
Four. Three vectors not in the same plane can't form a closed 3D loop; you need a fourth to close the gap.
</details>

5. 🔴 $ABCDEF$ is a regular hexagon. Find the resultant of $\vec{AB} + \vec{BC} + \vec{CD} + \vec{DE} + \vec{EF}$.
<details><summary><b>Answer</b></summary>
By polygon law, the resultant is the closing side in opposite order: $\vec{AF}$.
</details>

6. 🔴 In regular hexagon $ABCDEF$ with center $O$, prove that $\vec{AB} + \vec{AC} + \vec{AD} + \vec{AE} + \vec{AF} = 6\vec{AO}$.
<details><summary><b>Answer</b></summary>
$\vec{AC} = \vec{AB} + \vec{BC}$. This is a standard proof.
$\vec{AB} + \vec{ED} = 0$, etc.
Actually, $\vec{AB} + \vec{AF} = \vec{AO}$. $\vec{AC} + \vec{AE} = \vec{AD} = 2\vec{AO}$.
Total = $\vec{AO} + 2\vec{AO} + 2\vec{AO}$ (since $\vec{AD} = 2\vec{AO}$) = $6\vec{AO}$.
</details>

7. 🔴 Three forces $P, Q, R$ keep a particle in equilibrium. What must be true about the triangle they form?
<details><summary><b>Answer</b></summary>
They must form a closed triangle when placed head-to-tail, and follow Lami's theorem (or Sine rule).
</details>


### Type 7: Properties & Proofs ⭐
**Pattern:** "Using Commutative ($\vec{A}+\vec{B}=\vec{B}+\vec{A}$) and Associative properties algebraically."

**Solved Example** 🟡
> Prove algebraically that vector addition is commutative: $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.
<details><summary><b>Solution</b></summary>
Consider a parallelogram $OPQR$.
Let $\vec{OP} = \vec{A}$ and $\vec{OS} = \vec{B}$.
By properties of a parallelogram, $PQ$ is parallel and equal to $OS$. So, $\vec{PQ} = \vec{B}$.
Similarly, $SQ$ is parallel and equal to $OP$. So, $\vec{SQ} = \vec{A}$.
In triangle $OPQ$: $\vec{OQ} = \vec{OP} + \vec{PQ} = \vec{A} + \vec{B}$
In triangle $OSQ$: $\vec{OQ} = \vec{OS} + \vec{SQ} = \vec{B} + \vec{A}$
Since both equal $\vec{OQ}$, we have:
$\vec{A} + \vec{B} = \vec{B} + \vec{A}$
Hence proved.
</details>

**Practice:**
1. 🟢 Is vector subtraction commutative?
<details><summary><b>Answer</b></summary>
No. $\vec{A} - \vec{B} = -(\vec{B} - \vec{A}) \neq \vec{B} - \vec{A}$.
</details>

2. 🟢 State the associative property of vector addition.
<details><summary><b>Answer</b></summary>
$(\vec{A} + \vec{B}) + \vec{C} = \vec{A} + (\vec{B} + \vec{C})$.
</details>

3. 🟡 If $\vec{A} + \vec{B} = \vec{C}$ and $A^2 + B^2 = C^2$, find the angle between $\vec{A}$ and $\vec{B}$.
<details><summary><b>Answer</b></summary>
$C^2 = A^2 + B^2 + 2AB\cos\theta$. Given $C^2 = A^2 + B^2$, so $2AB\cos\theta = 0 \implies \cos\theta = 0 \implies \theta = 90^\circ$.
</details>

4. 🟡 If $\vec{A} + \vec{B} = \vec{C}$ and $A + B = C$, find the angle between $\vec{A}$ and $\vec{B}$.
<details><summary><b>Answer</b></summary>
This implies maximum resultant. $\theta = 0^\circ$.
</details>

5. 🔴 If $|\vec{A} + \vec{B}| = |\vec{A} - \vec{B}|$, what is the angle between $\vec{A}$ and $\vec{B}$?
<details><summary><b>Answer</b></summary>
Squaring both sides: $A^2 + B^2 + 2AB\cos\theta = A^2 + B^2 - 2AB\cos\theta$
$4AB\cos\theta = 0 \implies \cos\theta = 0 \implies \theta = 90^\circ$.
</details>

6. 🔴 If $\vec{a}$, $\vec{b}$, $\vec{c}$ form a triangle taken in order, what is $\vec{a} + \vec{b} + \vec{c}$?
<details><summary><b>Answer</b></summary>
By polygon law for a closed loop, the sum is the zero vector, $\vec{0}$.
</details>

7. 🔴 Prove that for any two vectors, $|\vec{A} + \vec{B}| \le |\vec{A}| + |\vec{B}|$.
<details><summary><b>Answer</b></summary>
This is the Triangle Inequality. In a triangle formed by vectors, the length of the third side ($|\vec{A}+\vec{B}|$) is always less than or equal to the sum of the lengths of the other two sides.
</details>

---

## 🧱 Stage 4: MCQ Mastery

1. Two forces $F_1 = 5 \text{ N}$ and $F_2 = 10 \text{ N}$ act on a point. Which of the following CANNOT be their resultant?
(a) $4 \text{ N}$
(b) $8 \text{ N}$
(c) $12 \text{ N}$
(d) $15 \text{ N}$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
The resultant must be between $|10-5| = 5 \text{ N}$ and $10+5 = 15 \text{ N}$. $4 \text{ N}$ lies outside this range.
</details>

2. The resultant of two equal vectors acting at right angles to each other is $14.14 \text{ units}$. The magnitude of each vector is:
(a) $10$
(b) $14.14$
(c) $20$
(d) $5$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
$R = \sqrt{x^2 + x^2} = x\sqrt{2}$. So $14.14 = x(1.414) \implies x = 10$.
</details>

3. **Assertion (A):** The sum of two vectors can be zero.
**Reason (R):** If two vectors are equal in magnitude and opposite in direction, their sum is zero.
(a) Both A and R are true, and R is the correct explanation of A.
(b) Both A and R are true, but R is not the correct explanation.
(c) A is true but R is false.
(d) A is false but R is true.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
Perfectly describes the condition for minimum resultant $R = F - F = 0$ at $180^\circ$.
</details>

4. Three vectors of magnitudes $P, P$ and $\sqrt{2}P$ can produce zero resultant. The angles between them must be:
(a) $90^\circ, 135^\circ, 135^\circ$
(b) $60^\circ, 120^\circ, 180^\circ$
(c) $90^\circ, 90^\circ, 180^\circ$
(d) $45^\circ, 45^\circ, 90^\circ$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
To form a closed loop (triangle), they must form a right-angled isosceles triangle. The interior angles are $90^\circ, 45^\circ, 45^\circ$. The angles between the vectors (head-to-tail exterior angles) are $180^\circ-90^\circ=90^\circ$, $180^\circ-45^\circ=135^\circ$, and $135^\circ$.
</details>

5. If $\vec{A} + \vec{B} = \vec{C}$ and $A = \sqrt{3}, B = \sqrt{3}, C = 3$. Then angle between $\vec{A}$ and $\vec{B}$ is:
(a) $0^\circ$
(b) $30^\circ$
(c) $60^\circ$
(d) $90^\circ$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (c)**
Using $C^2 = A^2 + B^2 + 2AB\cos\theta$:
$9 = 3 + 3 + 2(3)\cos\theta$
$9 = 6 + 6\cos\theta \implies 3 = 6\cos\theta \implies \cos\theta = 1/2 \implies \theta = 60^\circ$.
</details>

6. Which law is used to find the resultant of more than two vectors?
(a) Triangle Law
(b) Parallelogram Law
(c) Polygon Law
(d) None of these
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (c)**
Polygon law is specifically the extension for $\ge 3$ vectors.
</details>

7. The angle between vector $\vec{A}$ and $\vec{B}$ is $60^\circ$. The ratio of magnitude of $|\vec{A}+\vec{B}|$ and $|\vec{A}-\vec{B}|$ if $A=B$ is:
(a) $\sqrt{3} : 1$
(b) $1 : \sqrt{3}$
(c) $1 : 2$
(d) $2 : 1$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
$|\vec{A}+\vec{B}| = 2A\cos(60^\circ/2) = 2A\cos 30^\circ = A\sqrt{3}$.
$|\vec{A}-\vec{B}|$ acts at $120^\circ$ effectively, so $= 2A\sin(60^\circ/2) = 2A\sin 30^\circ = A$.
Ratio is $\sqrt{3} : 1$.
</details>

8. The resultant of two vectors of magnitudes $3$ units and $4$ units is $\sqrt{37}$. The angle between them is:
(a) $30^\circ$
(b) $60^\circ$
(c) $90^\circ$
(d) $120^\circ$
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (b)**
$37 = 9 + 16 + 24\cos\theta \implies 12 = 24\cos\theta \implies \cos\theta = 1/2 \implies \theta = 60^\circ$.
</details>

9. **Statement I:** The resultant of two vectors acts along the bisector of the angle between them if they have equal magnitudes.
**Statement II:** The formula for direction $\tan\alpha = \frac{B\sin\theta}{A+B\cos\theta}$ reduces to $\tan(\theta/2)$ when $A=B$.
(a) Both statements are correct.
(b) Statement I is correct, II is incorrect.
(c) Statement I is incorrect, II is correct.
(d) Both are incorrect.
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
When $A=B$, $\tan\alpha = \frac{\sin\theta}{1+\cos\theta} = \frac{2\sin(\theta/2)\cos(\theta/2)}{2\cos^2(\theta/2)} = \tan(\theta/2)$. Thus $\alpha = \theta/2$.
</details>

10. A person walks $10 \text{ m}$ North, then $20 \text{ m}$ East, then $10\sqrt{2} \text{ m}$ South-West. His net displacement is:
(a) $10 \text{ m}$ East
(b) $10 \text{ m}$ West
(c) $10\sqrt{2} \text{ m}$ North
(d) Zero
<details><summary><b>Answer & Explanation</b></summary>
**Answer: (a)**
North vector: $10\hat{j}$. East vector: $20\hat{i}$.
SW vector is at $225^\circ$: $10\sqrt{2}(-\frac{1}{\sqrt{2}}\hat{i} - \frac{1}{\sqrt{2}}\hat{j}) = -10\hat{i} - 10\hat{j}$.
Sum = $(20 - 10)\hat{i} + (10 - 10)\hat{j} = 10\hat{i} + 0\hat{j} = 10 \text{ m}$ East.
</details>

---

## 🔀 Stage 5: Type Mixer

**Problem 1: Kinematics + Vector Addition**
A boat crosses a river with a velocity of $8 \text{ km/h}$ relative to the water. If the water flows at a speed of $6 \text{ km/h}$, what is the resultant velocity of the boat relative to the bank if it heads strictly perpendicular to the river flow?
<details><summary><b>Solution</b></summary>
Let the river flow be $\vec{V}_r = 6 \text{ km/h}$ (along x-axis).
The boat's velocity relative to water is $\vec{V}_{bw} = 8 \text{ km/h}$ (along y-axis).
The angle between them is $90^\circ$.
Resultant velocity $\vec{V}_b = \vec{V}_{bw} + \vec{V}_r$.
$|\vec{V}_b| = \sqrt{8^2 + 6^2 + 0} = \sqrt{64 + 36} = \sqrt{100} = 10 \text{ km/h}$.
Direction: $\tan\alpha = 8/6 = 4/3 \implies \alpha = 53^\circ$ with the flow of the river.
</details>

**Problem 2: Dynamics + Max/Min Resultant**
Two forces whose magnitudes are in the ratio $3:5$ give a resultant of $28 \text{ N}$. If the angle of their inclination is $60^\circ$, find the magnitude of each force, and state what their maximum possible resultant would be.
<details><summary><b>Solution</b></summary>
Let forces be $3x$ and $5x$. $\theta = 60^\circ$. $R = 28$.
$R^2 = (3x)^2 + (5x)^2 + 2(3x)(5x)\cos 60^\circ$
$28^2 = 9x^2 + 25x^2 + 30x^2(1/2)$
$784 = 34x^2 + 15x^2 = 49x^2$
$x^2 = 784/49 = 16 \implies x = 4$.
Forces are $12 \text{ N}$ and $20 \text{ N}$.
Maximum possible resultant = $12 + 20 = 32 \text{ N}$.
</details>

**Problem 3: Multiple vectors + Polygon Law Logic**
Three forces $F_1, F_2, F_3$ act on a body. $F_1 = 5 \text{ N}$ East, $F_2 = 12 \text{ N}$ North. What must be the magnitude and direction of $F_3$ to keep the body in equilibrium?
<details><summary><b>Solution</b></summary>
For equilibrium, $\vec{F}_1 + \vec{F}_2 + \vec{F}_3 = 0 \implies \vec{F}_3 = -(\vec{F}_1 + \vec{F}_2)$.
Resultant of $F_1$ and $F_2$ is $\vec{R} = \sqrt{5^2 + 12^2} = 13 \text{ N}$.
Direction of $\vec{R}$ is $\tan\theta = 12/5$ (North of East).
Therefore, $\vec{F}_3$ must be $13 \text{ N}$ exactly opposite to this direction (South of West) to balance it out.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1 (3 Marks):** State the Parallelogram Law of Vector Addition. Derive the expression for the magnitude of the resultant vector.
<details><summary><b>Model Answer</b></summary>
**Statement:** If two vectors acting at a point are represented in magnitude and direction by the two adjacent sides of a parallelogram drawn from a point, their resultant is given by the diagonal of the parallelogram passing through that point.
**Derivation:** 
1. Let $\vec{A}$ and $\vec{B}$ be represented by sides $OP$ and $OS$ of parallelogram $OPQS$.
2. Drop a perpendicular $QN$ on the extended line $OP$.
3. In right $\triangle QNP$, $PN = B\cos\theta$ and $QN = B\sin\theta$.
4. In right $\triangle ONQ$, $OQ^2 = ON^2 + QN^2$.
5. $R^2 = (A + B\cos\theta)^2 + (B\sin\theta)^2$.
6. $R^2 = A^2 + B^2\cos^2\theta + 2AB\cos\theta + B^2\sin^2\theta$.
7. $R^2 = A^2 + B^2(\sin^2\theta + \cos^2\theta) + 2AB\cos\theta$.
8. $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$.
</details>

**Q2 (2 Marks):** Under what condition is the magnitude of the resultant of two vectors equal to the sum of their magnitudes?
<details><summary><b>Model Answer</b></summary>
The magnitude of the resultant is equal to the sum of their magnitudes when the two vectors are parallel and act in the same direction.
Mathematically, $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. 
For $R = A + B$, $(A+B)^2 = A^2 + B^2 + 2AB\cos\theta \implies 2AB = 2AB\cos\theta \implies \cos\theta = 1 \implies \theta = 0^\circ$.
</details>

**Q3 (3 Marks):** The sum and difference of two vectors $\vec{A}$ and $\vec{B}$ are perpendicular to each other. Prove that the vectors have equal magnitudes.
<details><summary><b>Model Answer</b></summary>
If $(\vec{A} + \vec{B})$ is perpendicular to $(\vec{A} - \vec{B})$, their dot product is zero.
$(\vec{A} + \vec{B}) \cdot (\vec{A} - \vec{B}) = 0$
$\vec{A}\cdot\vec{A} - \vec{A}\cdot\vec{B} + \vec{B}\cdot\vec{A} - \vec{B}\cdot\vec{B} = 0$
$A^2 - B^2 = 0$
$A^2 = B^2 \implies |\vec{A}| = |\vec{B}|$.
Hence proved, their magnitudes are equal.
</details>

**Q4 (2 Marks):** A force of $5 \text{ N}$ acts on a particle along a direction making an angle of $60^\circ$ with vertical. Find its vertical component.
<details><summary><b>Model Answer</b></summary>
Let the force be $F = 5 \text{ N}$. Angle with vertical $\theta = 60^\circ$.
Vertical component = $F \cos\theta = 5 \cos 60^\circ = 5 \times (1/2) = 2.5 \text{ N}$.
</details>

---

## 🚀 Stage 7: JEE Mains Arena

1. Two forces $P$ and $Q$, of magnitude $2F$ and $3F$, respectively, are at an angle $\theta$ with each other. If the force $Q$ is doubled, then their resultant also gets doubled. Then, the angle $\theta$ is:
&emsp;(a) $30^\circ$
&emsp;(b) $60^\circ$
&emsp;(c) $90^\circ$
&emsp;(d) $120^\circ$
<details><summary><b>Answer</b></summary>
**Answer: (d)**
Initial Resultant $R_1^2 = (2F)^2 + (3F)^2 + 2(2F)(3F)\cos\theta = 13F^2 + 12F^2\cos\theta$.
New force $Q' = 6F$. New Resultant $R_2 = 2R_1$.
$R_2^2 = 4R_1^2 = (2F)^2 + (6F)^2 + 2(2F)(6F)\cos\theta = 40F^2 + 24F^2\cos\theta$.
Equating: $4(13F^2 + 12F^2\cos\theta) = 40F^2 + 24F^2\cos\theta$.
$52 + 48\cos\theta = 40 + 24\cos\theta$.
$24\cos\theta = -12 \implies \cos\theta = -1/2 \implies \theta = 120^\circ$.
</details>

2. The resultant of two vectors $\vec{u}$ and $\vec{v}$ is perpendicular to $\vec{u}$. If $|\vec{v}| = \sqrt{2}|\vec{u}|$, then the angle between $\vec{u}$ and $\vec{v}$ is:
&emsp;(a) $135^\circ$
&emsp;(b) $120^\circ$
&emsp;(c) $150^\circ$
&emsp;(d) $45^\circ$
<details><summary><b>Answer</b></summary>
**Answer: (a)**
Condition for perpendicular resultant: $u + v\cos\theta = 0$.
$\cos\theta = -u/v$.
Given $v = \sqrt{2}u$, so $\cos\theta = -u/(\sqrt{2}u) = -1/\sqrt{2}$.
$\theta = 135^\circ$.
</details>

3. Let $|\vec{A}_1| = 3$, $|\vec{A}_2| = 5$ and $|\vec{A}_1 + \vec{A}_2| = 5$. The value of $(2\vec{A}_1 + 3\vec{A}_2) \cdot (3\vec{A}_1 - 2\vec{A}_2)$ is:
&emsp;(a) $-118.5$
&emsp;(b) $-106.5$
&emsp;(c) $-112.5$
&emsp;(d) $-115.5$
<details><summary><b>Answer</b></summary>
**Answer: (a)**
First, find $\vec{A}_1 \cdot \vec{A}_2$.
$|\vec{A}_1 + \vec{A}_2|^2 = A_1^2 + A_2^2 + 2(\vec{A}_1 \cdot \vec{A}_2) = 25$.
$9 + 25 + 2(\vec{A}_1 \cdot \vec{A}_2) = 25 \implies 2(\vec{A}_1 \cdot \vec{A}_2) = -9 \implies \vec{A}_1 \cdot \vec{A}_2 = -4.5$.
Expand the expression:
$= 6A_1^2 - 4(\vec{A}_1 \cdot \vec{A}_2) + 9(\vec{A}_1 \cdot \vec{A}_2) - 6A_2^2$
$= 6A_1^2 + 5(\vec{A}_1 \cdot \vec{A}_2) - 6A_2^2$
$= 6(9) + 5(-4.5) - 6(25)$
$= 54 - 22.5 - 150 = -118.5$.
</details>

4. Three forces start acting simultaneously on a particle moving with velocity $\vec{v}$. These forces are represented in magnitude and direction by the three sides of a triangle $ABC$ taken in order. What will be the new velocity of the particle?
&emsp;(a) Less than $\vec{v}$
&emsp;(b) Greater than $\vec{v}$
&emsp;(c) Remains $\vec{v}$
&emsp;(d) Becomes zero
<details><summary><b>Answer</b></summary>
**Answer: (c)**
Since the forces are represented by the three sides of a triangle taken in order, their resultant is zero by the Polygon Law of Vector Addition.
Net force = 0, so acceleration = 0. The particle continues to move with the same uniform velocity $\vec{v}$.
</details>

---

*Next: [Chapter 4 — Vector Subtraction →](./04_vector_subtraction.md)*
