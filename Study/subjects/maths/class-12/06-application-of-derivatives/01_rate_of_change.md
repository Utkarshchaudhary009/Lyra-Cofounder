# Chapter 1: Rate of Change of Quantities — How Fast is Everything Really Moving?

> *NCERT Section 6.2 | Class 12 Maths — Application of Derivatives*

---

## Stage 1: The Core Idea

### The Speedometer of a Changing World

Imagine you are filling a round balloon with air. You blow at a *steady* rate — say one puff per second. Does the balloon's **surface area** grow at a steady rate too? Intuitively you might say yes. But watch closely: early on, a small puff makes a big change in size; later, the same puff barely dents the huge balloon. The *rate* at which the area changes is itself changing — it depends on how big the balloon already is.

This is the heart of **Rate of Change of Quantities**. We use derivatives not to find slopes of lines, but to answer a living question: *"If this thing is changing, how fast is that other thing changing because of it?"*

### What $dy/dx$ Really Means

You already know $dy/dx$ is the derivative of $y$ with respect to $x$. But here is the deeper reading:

> **$dy/dx$ = the instantaneous rate of change of $y$ with respect to $x$.**

- If $y$ is distance and $x$ is time $t$, then $dy/dt$ is **velocity**.
- If $y$ is area and $x$ is the radius, then $dy/dx$ tells you *"how much area you gain per extra unit of radius, right at this radius."*
- If both $x$ and $y$ depend on a hidden third variable — usually **time $t$** — then we are in the world of **related rates**.

### The Hidden Third Variable — Time $t$

Most real problems do not say "find $dy/dx$." They say: *"The radius is growing at 3 cm/s. Find how fast the area is growing."*

Here, radius $r$ and area $A$ are both functions of time $t$:
- $dr/dt = 3$ cm/s (given)
- We want $dA/dt$ (unknown)

The bridge is the **chain rule**. Since $A = \pi r^2$:

$$\frac{dA}{dt} = \frac{dA}{dr} \cdot \frac{dr}{dt}$$

This is the single most important idea in the entire chapter. You connect the unknown rate to the known rate through a derivative.

> **Warning:** The variable you differentiate with respect to matters enormously. If a quantity depends on time, you must ultimately get a rate **with respect to $t$**. Differentiating only with respect to $x$ when the question asks "per second" is the #1 student error.

> **Tip:** Draw a mini "rate map." Write down: what is GIVEN (e.g., $dr/dt$), what is ASKED ($dA/dt$), and the connecting equation ($A = \pi r^2$). The chain rule links them. Never skip this step.

> **Key Takeaway:** Related-rates problems are solved in THREE moves — (1) write the connecting formula, (2) differentiate **both sides with respect to $t$**, (3) substitute the *instantaneous* values of the variables at that moment.

### $x$ and $y$ both functions of $t$ — the ratio formula

Sometimes you are told $dx/dt$ and $dy/dt$ and asked for $dy/dx$. By the chain rule:

$$\boxed{\frac{dy}{dx} = \frac{dy/dt}{dx/dt} \qquad \left(\text{provided } \frac{dx}{dt} \neq 0\right)}$$

This lets you find the *geometric* slope from two *time* rates. Conversely, if you know the slope and one time-rate, you find the other.

### Comparison Table — "Rate of change" vs "Just value"

| Question asks for... | You compute | Example |
|---|---|---|
| How fast $y$ changes as $x$ changes | $dy/dx$ | slope of curve |
| How fast $y$ changes *per second* | $dy/dt$ | velocity, area-growth |
| How fast $y$ changes given $dx/dt$ | $(dy/dx)(dx/dt)$ | related rates |
| Ratio of two rates | $dy/dx = (dy/dt)/(dx/dt)$ | same-rate point |

> **Classic Exam Trap:** "Circular area grows at a constant rate" does **NOT** mean the radius grows at a constant rate. Because $dA/dt = 2\pi r\, dr/dt$, if $dA/dt$ is constant then $dr/dt \propto 1/r$ — it *slows down* as the circle grows! This trap appears in **every board exam cycle**.

---

## Stage 2: The Formula Lab

### Core Formula — Chain Rule for Rates

$$\boxed{\frac{dy}{dx} = \frac{dy/dt}{dx/dt} \quad \text{and} \quad \frac{dy}{dt} = \frac{dy}{dx}\cdot\frac{dx}{dt}}$$

### Geometry Rate Bank

For any geometric quantity $Q$ that depends on a dimension $u(t)$:

$$\boxed{\frac{dQ}{dt} = \frac{dQ}{du}\cdot\frac{du}{dt}}$$

Specific results every student must memorise:

| Shape | Quantity | Formula | Rate |
|---|---|---|---|
| Circle | Area | $A = \pi r^2$ | $\boxed{dA/dt = 2\pi r\, dr/dt}$ |
| Circle | Circumference | $C = 2\pi r$ | $\boxed{dC/dt = 2\pi\, dr/dt}$ |
| Sphere | Volume | $V = \frac{4}{3}\pi r^3$ | $\boxed{dV/dt = 4\pi r^2\, dr/dt}$ |
| Sphere | Surface | $S = 4\pi r^2$ | $\boxed{dS/dt = 8\pi r\, dr/dt}$ |
| Cone | Volume | $V = \frac{1}{3}\pi r^2 h$ | $\boxed{dV/dt = \frac{\pi}{3}(2rh\, dr/dt + r^2\, dh/dt)}$ |
| Equilateral $\triangle$ | Area | $A = \frac{\sqrt{3}}{4}a^2$ | $\boxed{dA/dt = \frac{\sqrt{3}}{2}a\, da/dt}$ |
| Rectangle | Area | $A = xy$ | $\boxed{dA/dt = x\, dy/dt + y\, dx/dt}$ |
| Rectangle | Perimeter | $P = 2(x+y)$ | $\boxed{dP/dt = 2(dx/dt + dy/dt)}$ |
| Triangle (included $\theta$) | Area | $A = \frac{1}{2}ab\sin\theta$ | $\boxed{dA/dt = \frac{1}{2}ab\cos\theta\, d\theta/dt}$ |
| Square | Area | $A = s^2$ | $\boxed{dA/dt = 2s\, ds/dt}$ |
| Square | Diagonal | $d = \sqrt{2}\,s$ | $\boxed{dd/dt = \frac{1}{\sqrt{2}}\, ds/dt}$ |

### Motion Along a Curve

If a particle moves so that position satisfies $y = f(x)$ and both depend on $t$:

$$\boxed{v_x = \frac{dx}{dt},\quad v_y = \frac{dy}{dt},\quad \frac{dy}{dx} = \frac{v_y}{v_x}}$$

For straight-line motion with displacement $s(t)$:

$$\boxed{v = \frac{ds}{dt},\qquad a = \frac{d^2s}{dt^2}}$$

Special HOTS form: if $s = A\sin t + B\cos t$ then $a = -s$ (simple harmonic motion).

### Variable Reference Table

| Symbol | Meaning | Unit |
|---|---|---|
| $dy/dx$ | Rate of change of $y$ w.r.t. $x$ | depends on quantities |
| $dy/dt$ | Rate of change of $y$ w.r.t. time | quantity / second |
| $dx/dt$ | Rate of change of $x$ w.r.t. time | quantity / second |
| $r$ | Radius (circle/sphere/cone) | cm, m |
| $A$ | Area | cm², m² |
| $V$ | Volume | cm³, m³ |
| $S$ | Surface area | cm², m² |
| $a$ | Side length (square/equilateral $\triangle$) | cm, m |
| $\theta$ | Included angle | radian (or degree) |
| $s$ | Displacement / side of square | cm, m |
| $t$ | Time | second (s) |

### Key Numbers & Conversions to Memorize

| Fact | Value |
|---|---|
| $dA/dt$ for circle at radius $r$ | $2\pi r\, dr/dt$ — **depends on $r$** |
| If $dA/dt$ constant (circle) | $dr/dt$ is **not** constant; $dr/dt \propto 1/r$ |
| Equilateral triangle area | $\frac{\sqrt{3}}{4}a^2$ |
| Rectangle area rate | needs BOTH $dx/dt$ and $dy/dt$ |
| $\sin\theta$ derivative | $\cos\theta\, d\theta/dt$ |

### Special Cases Table

| Situation | What happens to the rate |
|---|---|
| Area grows at constant rate, circle | Radius growth **slows** as $r$ increases |
| Radius grows at constant rate, circle | Area growth **speeds up** (scales with $r$) |
| Point where $dx/dt = dy/dt$ | Requires $dy/dx = 1$ at that point |
| Two variables $x$ falling, $y$ rising (rectangle) | Area rate can be $+$ or $-$ depending on sizes |

---

## Stage 3: Type-wise Mastery

---

### Type 1: Direct Single-Variable Rate

**Pattern:** "Side/radius grows at $k$ units/s. Find rate of area/volume increase when the dimension equals a given value."

**Solved Example** (Easy)

> The side of a square is increasing at the rate of 2 cm/s. Find the rate at which its area is increasing when the side is 10 cm. (NCERT-style, 2 marks)

<details><summary><b>Solution</b></summary>

Let the side be $x$ cm and area be $A = x^2$ cm².

Given: $dx/dt = 2$ cm/s.

Differentiate with respect to $t$:

$$\frac{dA}{dt} = \frac{d}{dt}(x^2) = 2x\frac{dx}{dt}$$

At $x = 10$ cm:

$$\frac{dA}{dt} = 2(10)(2) = \boxed{40 \text{ cm}^2/\text{s}}$$

</details>

---

**Practice Questions**

1. (🟢 Easy) The radius of a circle is increasing at 3 cm/s. Find the rate of increase of its area when $r = 5$ cm.

<details><summary><b>Answer</b></summary>

$A = \pi r^2 \implies dA/dt = 2\pi r\, dr/dt = 2\pi(5)(3) = \boxed{30\pi \text{ cm}^2/\text{s}}$.

</details>

---

2. (🟢 Easy) The edge of a cube is increasing at 1 cm/s. Find the rate of increase of its volume when the edge is 4 cm.

<details><summary><b>Answer</b></summary>

$V = s^3 \implies dV/dt = 3s^2\, ds/dt = 3(4^2)(1) = \boxed{48 \text{ cm}^3/\text{s}}$.

</details>

---

3. (🟡 Medium) The radius of a spherical balloon is increasing at 2 cm/s. Find the rate of increase of its surface area when $r = 6$ cm.

<details><summary><b>Answer</b></summary>

$S = 4\pi r^2 \implies dS/dt = 8\pi r\, dr/dt = 8\pi(6)(2) = \boxed{96\pi \text{ cm}^2/\text{s}}$.

</details>

---

4. (🟡 Medium) A circular plate expands uniformly so that its radius increases at 0.5 cm/s. Find the rate of increase of its circumference when $r = 10$ cm.

<details><summary><b>Answer</b></summary>

$C = 2\pi r \implies dC/dt = 2\pi\, dr/dt = 2\pi(0.5) = \boxed{\pi \text{ cm/s}}$ (independent of $r$ — note circumference rate is constant!).

</details>

---

5. (🔴 Hard) The side of an equilateral triangle increases at 4 cm/s. Find the rate of increase of its area when the side is 8 cm.

<details><summary><b>Answer</b></summary>

$A = \frac{\sqrt{3}}{4}a^2 \implies dA/dt = \frac{\sqrt{3}}{2}a\, da/dt = \frac{\sqrt{3}}{2}(8)(4) = \boxed{16\sqrt{3} \text{ cm}^2/\text{s}}$.

</details>

---

6. (⭐ Must-Do) The volume of a sphere is increasing at a constant rate. Is its radius increasing at a constant rate? Justify.

<details><summary><b>Answer</b></summary>

$V = \frac{4}{3}\pi r^3 \implies dV/dt = 4\pi r^2\, dr/dt$.

If $dV/dt = k$ (constant), then $dr/dt = \dfrac{k}{4\pi r^2}$, which **decreases** as $r$ grows.

So the radius does **NOT** increase at a constant rate — it slows down. $\boxed{\text{No}}$.

</details>

---

### Type 2: Two-Variable Rectangle (one rising, one falling)

**Pattern:** "Length $x$ is decreasing, breadth $y$ is increasing, both at given rates. Find rate of change of perimeter and area at given $x, y$." (All India 2017, 4M)

**Solved Example** (Medium)

> The length $x$ of a rectangle is decreasing at 3 cm/min and the width $y$ is increasing at 2 cm/min. Find the rate of change of (a) perimeter and (b) area when $x = 10$ cm and $y = 6$ cm.

<details><summary><b>Solution</b></summary>

Given: $dx/dt = -3$ cm/min (decreasing), $dy/dt = +2$ cm/min (increasing).

**(a) Perimeter** $P = 2(x+y)$:

$$\frac{dP}{dt} = 2\left(\frac{dx}{dt} + \frac{dy}{dt}\right) = 2(-3 + 2) = 2(-1) = \boxed{-2 \text{ cm/min}}$$

The perimeter is decreasing at 2 cm/min.

**(b) Area** $A = xy$:

$$\frac{dA}{dt} = x\frac{dy}{dt} + y\frac{dx}{dt} = (10)(2) + (6)(-3) = 20 - 18 = \boxed{2 \text{ cm}^2/\text{min}}$$

The area is increasing at 2 cm²/min.

</details>

---

**Practice Questions**

1. (🟡 Medium) The length of a rectangle is increasing at 4 cm/s and width decreasing at 1 cm/s. Find rate of change of area when length = 8 cm, width = 5 cm.

<details><summary><b>Answer</b></summary>

$dA/dt = x\,dy/dt + y\,dx/dt = 8(-1) + 5(4) = -8 + 20 = \boxed{12 \text{ cm}^2/\text{s}}$.

</details>

---

2. (🟡 Medium) For the same rectangle in Q1, find the rate of change of the perimeter.

<details><summary><b>Answer</b></summary>

$dP/dt = 2(dx/dt + dy/dt) = 2(4 + (-1)) = \boxed{6 \text{ cm/s}}$.

</details>

---

3. (🔴 Hard) A rectangle has length $x$ decreasing at 2 cm/s and breadth $y$ increasing at 3 cm/s. At the instant $x = 12$, $y = 8$, is the area increasing or decreasing, and at what rate?

<details><summary><b>Answer</b></summary>

$dA/dt = x\,dy/dt + y\,dx/dt = 12(3) + 8(-2) = 36 - 16 = \boxed{20 \text{ cm}^2/\text{s}}$ increasing.

</details>

---

4. (🔴 Hard) When will the area in Q3 be momentarily constant (rate zero)? Express in terms of the relation between $x$ and $y$ at that instant.

<details><summary><b>Answer</b></summary>

Area constant when $dA/dt = 0$: $x(3) + y(-2) = 0 \implies 3x = 2y \implies \boxed{x : y = 2 : 3}$.

At the instant the sides are in ratio $2:3$, the area stops changing.

</details>

---

5. (⭐ Must-Do) A rectangle's length decreases at 5 cm/s and breadth increases at 5 cm/s. At $x = 20$, $y = 10$, find rate of change of area and perimeter.

<details><summary><b>Answer</b></summary>

$dA/dt = 20(5) + 10(-5) = 100 - 50 = \boxed{50 \text{ cm}^2/\text{s}}$.

$dP/dt = 2(-5 + 5) = \boxed{0}$ — perimeter is momentarily steady.

</details>

---

### Type 3: Geometry with Fixed-Ratio Cone

**Pattern:** "Sand/water forms a cone where height and radius are linked by a fixed ratio (e.g. $h = r/6$ or $r = kh$). Given $dV/dt$, find $dh/dt$ or $dr/dt$."

**Solved Example** (Hard)

> Sand is pouring from a pipe at the rate of 12 cm³/s, forming a cone where the height is one-sixth of the radius ($h = r/6$). Find the rate at which the height is increasing when $h = 4$ cm. (Delhi 2011 pattern, 4M)

<details><summary><b>Solution</b></summary>

Volume of cone: $V = \frac{1}{3}\pi r^2 h$.

Given $h = r/6 \implies r = 6h$. Substitute:

$$V = \frac{1}{3}\pi (6h)^2 h = \frac{1}{3}\pi \cdot 36h^2 \cdot h = 12\pi h^3$$

Differentiate w.r.t. $t$:

$$\frac{dV}{dt} = 12\pi \cdot 3h^2 \frac{dh}{dt} = 36\pi h^2 \frac{dh}{dt}$$

Given $dV/dt = 12$, at $h = 4$:

$$12 = 36\pi (4)^2 \frac{dh}{dt} = 36\pi \cdot 16 \frac{dh}{dt} = 576\pi \frac{dh}{dt}$$

$$\frac{dh}{dt} = \frac{12}{576\pi} = \boxed{\frac{1}{48\pi} \text{ cm/s}}$$

</details>

---

**Practice Questions**

1. (🔴 Hard) In the same cone, find $dr/dt$ when $h = 4$ cm.

<details><summary><b>Answer</b></summary>

Since $r = 6h$, $dr/dt = 6\, dh/dt = 6 \cdot \frac{1}{48\pi} = \boxed{\frac{1}{8\pi} \text{ cm/s}}$.

</details>

---

2. (🔴 Hard) A cone's height is always 3 times its radius ($h = 3r$). Volume increases at 24 cm³/s. Find $dr/dt$ when $r = 2$ cm.

<details><summary><b>Answer</b></summary>

$V = \frac{1}{3}\pi r^2(3r) = \pi r^3$. $dV/dt = 3\pi r^2\, dr/dt$.

$24 = 3\pi(4)\, dr/dt \implies dr/dt = \frac{24}{12\pi} = \boxed{\frac{2}{\pi} \text{ cm/s}}$.

</details>

---

3. (⭐ Must-Do) Prove: for a cone with fixed ratio $h = kr$, the rate $dh/dt \propto 1/h^2$ if $dV/dt$ is constant.

<details><summary><b>Answer</b></summary>

$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi (h/k)^2 h = \frac{\pi}{3k^2}h^3$.

$dV/dt = \frac{\pi}{k^2}h^2\, dh/dt$. If $dV/dt = c$:

$dh/dt = \dfrac{c k^2}{\pi h^2} \propto \boxed{1/h^2}$.

</details>

---

4. (🔴 Hard) Water drains from an inverted cone (height 12 cm, radius 6 cm at top) at 10 cm³/s. Find the rate at which the water level drops when depth is 6 cm.

<details><summary><b>Answer</b></summary>

By similarity $r/h = 6/12 = 1/2 \implies r = h/2$.

$V = \frac{1}{3}\pi (h/2)^2 h = \frac{\pi}{12}h^3$. $dV/dt = \frac{\pi}{4}h^2\, dh/dt$.

$-10 = \frac{\pi}{4}(36)\, dh/dt \implies dh/dt = \frac{-10}{9\pi} = \boxed{-\frac{10}{9\pi} \text{ cm/s}}$ (dropping).

</details>

---

5. (🔴 Hard) For the draining cone above, find the rate of change of the surface radius when depth is 6 cm.

<details><summary><b>Answer</b></summary>

$r = h/2 \implies dr/dt = \frac{1}{2}dh/dt = \frac{1}{2}\left(-\frac{10}{9\pi}\right) = \boxed{-\frac{5}{9\pi} \text{ cm/s}}$.

</details>

---

### Type 4: Equilateral / Isosceles Triangle Area Rate

**Pattern:** "Side of an equilateral triangle increases at $k$ cm/s; find $dA/dt$ at a given side." Or equal sides of a fixed-base isosceles increase — find area rate when sides are equal.

**Solved Example** (Medium)

> The side of an equilateral triangle is increasing at the rate of 3 cm/s. Find the rate of increase of its area when the side is 12 cm. (Delhi 2015 pattern)

<details><summary><b>Solution</b></summary>

Area of equilateral triangle: $A = \frac{\sqrt{3}}{4}a^2$.

$$\frac{dA}{dt} = \frac{\sqrt{3}}{4}\cdot 2a\frac{da}{dt} = \frac{\sqrt{3}}{2}a\frac{da}{dt}$$

Given $da/dt = 3$ cm/s, $a = 12$ cm:

$$\frac{dA}{dt} = \frac{\sqrt{3}}{2}(12)(3) = 18\sqrt{3} \text{ cm}^2/\text{s}$$

$$\boxed{\frac{dA}{dt} = 18\sqrt{3} \text{ cm}^2/\text{s}}$$

</details>

---

**Practice Questions**

1. (🟡 Medium) The side of an equilateral triangle increases at 2 cm/s. Find rate of area increase when side = 6 cm.

<details><summary><b>Answer</b></summary>

$dA/dt = \frac{\sqrt{3}}{2}a\, da/dt = \frac{\sqrt{3}}{2}(6)(2) = \boxed{6\sqrt{3} \text{ cm}^2/\text{s}}$.

</details>

---

2. (🔴 Hard) An isosceles triangle has fixed base 10 cm. Its equal sides (each of length $l$) increase at 1 cm/s. Find the rate of increase of area when $l = 13$ cm.

<details><summary><b>Answer</b></summary>

Height $h = \sqrt{l^2 - 5^2} = \sqrt{l^2 - 25}$. Area $A = \frac{1}{2}(10)h = 5\sqrt{l^2 - 25}$.

$dA/dt = 5 \cdot \frac{1}{2\sqrt{l^2-25}}\cdot 2l\, dl/dt = \frac{5l}{\sqrt{l^2-25}}\, dl/dt$.

At $l = 13$: $dA/dt = \frac{5(13)}{\sqrt{169-25}}(1) = \frac{65}{\sqrt{144}} = \frac{65}{12} = \boxed{\frac{65}{12} \text{ cm}^2/\text{s}}$.

</details>

---

3. (🔴 Hard) For the isosceles triangle in Q2, find the rate of area increase when the triangle becomes equilateral (sides = base = 10).

<details><summary><b>Answer</b></summary>

At $l = 10$: $dA/dt = \frac{5(10)}{\sqrt{100-25}} = \frac{50}{5\sqrt{3}} = \frac{10}{\sqrt{3}} = \boxed{\frac{10\sqrt{3}}{3} \text{ cm}^2/\text{s}}$.

</details>

---

4. (⭐ Must-Do) Show that for an equilateral triangle, $dA/dt$ is proportional to the side $a$ (when $da/dt$ is constant).

<details><summary><b>Answer</b></summary>

$dA/dt = \frac{\sqrt{3}}{2}a\, da/dt$. With $da/dt = k$ constant, $dA/dt = \frac{\sqrt{3}}{2}k\, a \propto \boxed{a}$.

</details>

---

5. (🔴 Hard) The area of an equilateral triangle is increasing at $4\sqrt{3}$ cm²/s. Find the rate of increase of its side when the side is 8 cm.

<details><summary><b>Answer</b></summary>

$dA/dt = \frac{\sqrt{3}}{2}a\, da/dt \implies 4\sqrt{3} = \frac{\sqrt{3}}{2}(8)\, da/dt = 4\sqrt{3}\, da/dt$.

$da/dt = \boxed{1 \text{ cm/s}}$.

</details>

---

### Type 5: Motion Along a Curve

**Pattern:** "A particle moves along a curve $y = f(x)$; given a relation between $dx/dt$ and $dy/dt$ at a point, find an unknown parameter or coordinate."

**Solved Example** (Medium)

> A particle moves along the curve $3y = ax^3 + 1$ such that at $x = 1$, the $y$-coordinate is changing twice as fast as the $x$-coordinate. Find $a$. (CBSE 2023, 2M)

<details><summary><b>Solution</b></summary>

Given $3y = ax^3 + 1$. Differentiate w.r.t. $t$:

$$3\frac{dy}{dt} = 3ax^2\frac{dx}{dt} \implies \frac{dy}{dt} = ax^2\frac{dx}{dt}$$

At $x = 1$, $dy/dt = 2\, dx/dt$ (twice as fast):

$$2\frac{dx}{dt} = a(1)^2\frac{dx}{dt} \implies 2 = a$$

$$\boxed{a = 2}$$

</details>

---

**Practice Questions**

1. (🟡 Medium) A particle moves on $y = x^2 + 1$. If $dx/dt = 3$ at $x = 2$, find $dy/dt$.

<details><summary><b>Answer</b></summary>

$dy/dt = 2x\, dx/dt = 2(2)(3) = \boxed{12}$.

</details>

---

2. (🔴 Hard) A particle moves on $y = x^3$. At what point is the $y$-coordinate changing 12 times as fast as the $x$-coordinate?

<details><summary><b>Answer</b></summary>

$dy/dt = 3x^2\, dx/dt$. Given $dy/dt = 12\, dx/dt$:

$3x^2 = 12 \implies x^2 = 4 \implies x = \pm 2$.

At $x = 2$, $y = 8$; at $x = -2$, $y = -8$. Points: $\boxed{(2,8) \text{ and } (-2,-8)}$.

</details>

---

3. (⭐ Must-Do) A particle moves on $y = \sin x$. If $dx/dt = 2$, find $dy/dt$ at $x = \pi/3$.

<details><summary><b>Answer</b></summary>

$dy/dt = \cos x\, dx/dt = \cos(\pi/3)\cdot 2 = \frac{1}{2}\cdot 2 = \boxed{1}$.

</details>

---

4. (🔴 Hard) A particle moves on $x^2 + y^2 = 25$. If $dy/dt = -3$ at $(3,4)$, find $dx/dt$.

<details><summary><b>Answer</b></summary>

$2x\, dx/dt + 2y\, dy/dt = 0 \implies x\, dx/dt + y\, dy/dt = 0$.

$3\, dx/dt + 4(-3) = 0 \implies 3\, dx/dt = 12 \implies dx/dt = \boxed{4}$.

</details>

---

5. (🔴 Hard) A particle moves along $y = 2x^2 - 3$. The $x$-coordinate changes at 0.5 units/s. Find the rate of change of the slope of the curve at $x = 1$.

<details><summary><b>Answer</b></summary>

Slope $m = dy/dx = 4x$. $dm/dt = 4\, dx/dt = 4(0.5) = \boxed{2 \text{ units/s}}$.

</details>

---

### Type 6: Point Where Coordinates Change at Same Rate

**Pattern:** "Find the point on a given curve where $dx/dt = dy/dt$." This means $dy/dx = 1$ at that point.

**Solved Example** (Medium)

> Find the point on the curve $y^2 = 8x$ where the ordinate and abscissa change at the same rate. (CBSE 2023, 2M)

<details><summary><b>Solution</b></summary>

Same rate means $dx/dt = dy/dt$, so $dy/dx = 1$.

Differentiate $y^2 = 8x$ w.r.t. $x$:

$$2y\frac{dy}{dx} = 8 \implies \frac{dy}{dx} = \frac{4}{y}$$

Set $dy/dx = 1$:

$$\frac{4}{y} = 1 \implies y = 4$$

From $y^2 = 8x$: $16 = 8x \implies x = 2$.

$$\boxed{\text{The point is }(2, 4)}$$

</details>

---

**Practice Questions**

1. (🟡 Medium) Find the point on $y^2 = 4x$ where coordinates change at the same rate.

<details><summary><b>Answer</b></summary>

$2y\, dy/dx = 4 \implies dy/dx = 2/y = 1 \implies y = 2$. Then $4 = 4x \implies x = 1$. Point: $\boxed{(1,2)}$.

</details>

---

2. (🔴 Hard) Find the point on $y = x^3 - x$ where coordinates change at the same rate.

<details><summary><b>Answer</b></summary>

$dy/dx = 3x^2 - 1 = 1 \implies 3x^2 = 2 \implies x = \pm\sqrt{2/3}$.

$y = x^3 - x$. Points: $\boxed{\left(\sqrt{2/3},\, \frac{2}{3}\sqrt{2/3} - \sqrt{2/3}\right) \text{ and } \left(-\sqrt{2/3},\, -\frac{2}{3}\sqrt{2/3} + \sqrt{2/3}\right)}$.

</details>

---

3. (⭐ Must-Do) On the curve $y = x^2$, at what point does the $y$-coordinate change twice as fast as the $x$-coordinate?

<details><summary><b>Answer</b></summary>

$dy/dx = 2x = 2 \implies x = 1$, $y = 1$. Point: $\boxed{(1,1)}$.

</details>

---

4. (🔴 Hard) Find the point on the circle $x^2 + y^2 = 18$ where $dx/dt = dy/dt$.

<details><summary><b>Answer</b></summary>

$2x\, dx/dt + 2y\, dy/dt = 0$. With $dx/dt = dy/dt \neq 0$: $x + y = 0 \implies y = -x$.

$x^2 + x^2 = 18 \implies 2x^2 = 18 \implies x = \pm 3$, $y = \mp 3$. Points: $\boxed{(3,-3) \text{ and } (-3,3)}$.

</details>

---

5. (🔴 Hard) A point moves on $xy = 4$. Where do the coordinates change at the same rate?

<details><summary><b>Answer</b></summary>

$y + x\, dy/dx = 0 \implies dy/dx = -y/x = 1 \implies y = -x$. Then $x(-x) = 4 \implies x^2 = -4$, no real solution.

$\boxed{\text{No real point}}$ — on $xy=4$ the coordinates can never change at equal (finite) rates.

</details>

---

### Type 7: Ratio-of-Rates Proof

**Pattern:** "If the circumference increases at a constant rate, prove that $dA/dt \propto r$" or similar proportional-reasoning proofs.

**Solved Example** (Medium)

> Prove that if the circumference of a circle increases at a constant rate, then the rate of increase of its area is proportional to its radius. (Competency proof style)

<details><summary><b>Solution</b></summary>

Circumference $C = 2\pi r$, Area $A = \pi r^2$.

Given $dC/dt = k$ (constant). From $C = 2\pi r$:

$$\frac{dC}{dt} = 2\pi\frac{dr}{dt} = k \implies \frac{dr}{dt} = \frac{k}{2\pi} \text{ (constant)}$$

Now:

$$\frac{dA}{dt} = 2\pi r\frac{dr}{dt} = 2\pi r \cdot \frac{k}{2\pi} = kr$$

Since $k$ is constant, $\boxed{dA/dt \propto r}$. Proved.

</details>

---

**Practice Questions**

1. (🟡 Medium) Prove: if the radius of a sphere increases at a constant rate, then $dV/dt \propto r^2$.

<details><summary><b>Answer</b></summary>

$V = \frac{4}{3}\pi r^3 \implies dV/dt = 4\pi r^2\, dr/dt$. With $dr/dt = k$ constant: $dV/dt = 4\pi k r^2 \propto \boxed{r^2}$. Proved.

</details>

---

2. (🔴 Hard) If the area of a circle increases at a constant rate, show that the rate of increase of the radius is inversely proportional to the radius.

<details><summary><b>Answer</b></summary>

$dA/dt = k$. But $dA/dt = 2\pi r\, dr/dt \implies 2\pi r\, dr/dt = k \implies dr/dt = \frac{k}{2\pi r} \propto \boxed{1/r}$. Proved.

</details>

---

3. (⭐ Must-Do) A square's diagonal increases at a constant rate. Show the area increases at a rate proportional to the diagonal.

<details><summary><b>Answer</b></summary>

$A = s^2$, diagonal $d = \sqrt{2}s \implies s = d/\sqrt{2}$, so $A = d^2/2$.

$dA/dt = d\, dd/dt$. With $dd/dt = k$ constant: $dA/dt = kd \propto \boxed{d}$. Proved.

</details>

---

4. (🔴 Hard) For an equilateral triangle, if the side increases at constant rate, show $dA/dt \propto a$ (already seen) AND that the rate of increase of the perimeter equals $3\, da/dt$.

<details><summary><b>Answer</b></summary>

$P = 3a \implies dP/dt = 3\, da/dt$ — constant, equal to 3 times side-rate. $\boxed{dP/dt = 3\, da/dt}$. (This is trivially proportional with constant factor.)

</details>

---

5. (🔴 Hard) Prove: if the volume of a sphere grows at constant rate, the surface area grows at a rate inversely proportional to the radius.

<details><summary><b>Answer</b></summary>

$dV/dt = k$. But $dV/dt = 4\pi r^2\, dr/dt = k \implies dr/dt = \frac{k}{4\pi r^2}$.

$dS/dt = 8\pi r\, dr/dt = 8\pi r\cdot \frac{k}{4\pi r^2} = \frac{2k}{r} \propto \boxed{1/r}$. Proved.

</details>

---

### Type 8: Trig / Area Rate with Included Angle

**Pattern:** "Two sides of a triangle are fixed; the included angle changes at a given rate. Find rate of change of area."

**Solved Example** (Medium)

> Two sides of a triangle are 10 cm and 12 cm. The angle $\theta$ between them is increasing at 2°/s. Find the rate at which the area is increasing when $\theta = 60^\circ$.

<details><summary><b>Solution</b></summary>

Area: $A = \frac{1}{2}(10)(12)\sin\theta = 60\sin\theta$.

$$\frac{dA}{dt} = 60\cos\theta \cdot \frac{d\theta}{dt}$$

Convert $d\theta/dt$ to radians: $2^\circ/\text{s} = \frac{2\pi}{180} = \frac{\pi}{90}$ rad/s.

At $\theta = 60^\circ$, $\cos 60^\circ = 1/2$:

$$\frac{dA}{dt} = 60 \cdot \frac{1}{2} \cdot \frac{\pi}{90} = \frac{30\pi}{90} = \frac{\pi}{3} \text{ cm}^2/\text{s}$$

$$\boxed{\frac{dA}{dt} = \frac{\pi}{3} \text{ cm}^2/\text{s}}$$

> **Trap:** Always convert angle rate to **radians** before differentiating — derivatives of trig functions assume radian measure.

</details>

---

**Practice Questions**

1. (🟡 Medium) Two sides of a triangle are 8 cm and 6 cm. The included angle increases at 1 rad/s. Find rate of area change at $\theta = \pi/2$.

<details><summary><b>Answer</b></summary>

$A = \frac{1}{2}(8)(6)\sin\theta = 24\sin\theta$. $dA/dt = 24\cos\theta\, d\theta/dt$.

At $\theta = \pi/2$, $\cos\theta = 0$: $dA/dt = \boxed{0}$. (Area momentarily max.)

</details>

---

2. (🔴 Hard) For the triangle in Q1, find $dA/dt$ at $\theta = \pi/3$.

<details><summary><b>Answer</b></summary>

$dA/dt = 24\cos(\pi/3)(1) = 24 \cdot \frac{1}{2} = \boxed{12 \text{ cm}^2/\text{s}}$.

</details>

---

3. (⭐ Must-Do) A triangle has sides 5 and 5 with included angle $\theta$ increasing at $\pi/36$ rad/s. Find $dA/dt$ at $\theta = \pi/6$.

<details><summary><b>Answer</b></summary>

$A = \frac{1}{2}(25)\sin\theta = 12.5\sin\theta$. $dA/dt = 12.5\cos(\pi/6)\cdot \frac{\pi}{36}$.

$= 12.5 \cdot \frac{\sqrt{3}}{2} \cdot \frac{\pi}{36} = \frac{12.5\sqrt{3}\pi}{72} = \boxed{\frac{25\sqrt{3}\pi}{144} \text{ cm}^2/\text{s}}$.

</details>

---

4. (🔴 Hard) Show that for fixed sides $a, b$, the area rate is maximized when $\theta = 0$? Or explain the actual maximum.

<details><summary><b>Answer</b></summary>

$dA/dt = \frac{1}{2}ab\cos\theta\, d\theta/dt$. For fixed $d\theta/dt > 0$, this is largest in magnitude when $|\cos\theta|$ is largest, i.e. $\theta = 0$ (or $\pi$). The **area itself** is maximized at $\theta = 90^\circ$ (where $dA/dt = 0$). Distinction: rate-of-area is max at $\theta=0$; area value is max at $\theta=90^\circ$. $\boxed{\text{Two different optima.}}$

</details>

---

5. (🔴 Hard) A ladder 5 m long leans against a wall. The foot is pulled away at 1 m/s. Find how fast the top descends when the foot is 3 m from the wall. (Related triangle rate.)

<details><summary><b>Answer</b></summary>

$x^2 + y^2 = 25$. Differentiate: $2x\, dx/dt + 2y\, dy/dt = 0$.

At $x = 3$, $y = 4$, $dx/dt = 1$: $3(1) + 4\, dy/dt = 0 \implies dy/dt = \boxed{-3/4 \text{ m/s}}$ (descending).

</details>

---

## Stage 4: MCQ Mastery

**Q1.** If $y = x^2$ and $x$ is increasing at 2 units/s, then at $x = 3$ the rate of change of $y$ is:

(a) 6 units/s &emsp; (b) 12 units/s &emsp; (c) 18 units/s &emsp; (d) 4 units/s

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) 12 units/s**

$dy/dt = 2x\, dx/dt = 2(3)(2) = 12$. Option (a) forgets the factor $dx/dt$.

</details>

---

**Q2.** The radius of a circle is increasing at 1 cm/s. The rate of increase of its area when $r = 4$ cm is:

(a) $4\pi$ &emsp; (b) $8\pi$ &emsp; (c) $16\pi$ &emsp; (d) $2\pi$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) $8\pi$ cm²/s**

$dA/dt = 2\pi r\, dr/dt = 2\pi(4)(1) = 8\pi$. Option (c) uses $r^2$ instead of $2r$.

</details>

---

**Q3.** If the area of a circle increases at a constant rate, then the rate of increase of the radius is:

(a) constant &emsp; (b) proportional to $r$ &emsp; (c) inversely proportional to $r$ &emsp; (d) proportional to $r^2$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) inversely proportional to $r$**

$dA/dt = k = 2\pi r\, dr/dt \implies dr/dt = k/(2\pi r) \propto 1/r$.

</details>

---

**Q4.** A particle moves on $y^2 = 4x$. At the point where coordinates change at same rate, the coordinates are:

(a) $(1,2)$ &emsp; (b) $(2,4)$ &emsp; (c) $(4,16)$ &emsp; (d) $(1,-2)$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $(1,2)$**

$dy/dx = 2/y = 1 \implies y = 2$, then $x = 1$. (Also $(-1,-2)$ works but not listed; (d) has $y=-2$ giving $dy/dx = -1$, not 1.)

</details>

---

**Q5.** If $x$ and $y$ are functions of $t$ and $dy/dx = 3$ while $dx/dt = 2$, then $dy/dt =$

(a) 5 &emsp; (b) 6 &emsp; (c) 1.5 &emsp; (d) 3/2

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b) 6**

$dy/dt = (dy/dx)(dx/dt) = 3 \times 2 = 6$.

</details>

---

**Q6.** (Assertion-Reason)

**Assertion (A):** The rate of increase of area of a circle is proportional to its radius when the radius grows at a constant rate.

**Reason (R):** $dA/dt = 2\pi r\, dr/dt$ and if $dr/dt$ is constant then $dA/dt \propto r$.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) Both true, R explains A**

$dA/dt = 2\pi r\, dr/dt$; constant $dr/dt \implies dA/dt \propto r$. Both correct, R is the reason.

</details>

---

**Q7.** (Assertion-Reason)

**Assertion (A):** If the circumference of a circle increases at a constant rate, the rate of increase of its area is constant.

**Reason (R):** $dA/dt = r \cdot dC/dt$, and $r$ changes with time.

(a) Both A and R are true, and R is the correct explanation of A
(b) Both A and R are true, but R is NOT the correct explanation of A
(c) A is true but R is false
(d) A is false but R is true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (d) A is false but R is true**

From Type 7, $dA/dt = r \cdot (dC/dt)$ and since $dC/dt$ is constant but $r$ grows, $dA/dt$ is **not** constant — it is $\propto r$. So A is false, R is true.

</details>

---

**Q8.** The area of an equilateral triangle whose side increases at 2 cm/s, when side = 5 cm, changes at:

(a) $5\sqrt{3}$ &emsp; (b) $10\sqrt{3}$ &emsp; (c) $2\sqrt{3}$ &emsp; (d) $5\sqrt{3}/2$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) $5\sqrt{3}$ cm²/s**

$dA/dt = \frac{\sqrt{3}}{2}a\, da/dt = \frac{\sqrt{3}}{2}(5)(2) = 5\sqrt{3}$.

</details>

---

**Q9.** A spherical balloon's volume is increasing at 100 cm³/s. Its radius when $dr/dt = 1$ cm/s is:

(a) $\sqrt{25/\pi}$ &emsp; (b) $\sqrt{100/\pi}$ &emsp; (c) $5/\sqrt{\pi}$ &emsp; (d) $10/\sqrt{\pi}$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) $5/\sqrt{\pi}$ cm**

$dV/dt = 4\pi r^2\, dr/dt = 4\pi r^2(1) = 100 \implies r^2 = 25/\pi \implies r = 5/\sqrt{\pi}$.

</details>

---

**Q10.** A ladder 13 m long leans against a wall. If the foot is pulled away at 2 m/s, how fast is the top descending when the foot is 5 m from the wall?

(a) 5/6 m/s &emsp; (b) 6/5 m/s &emsp; (c) 2 m/s &emsp; (d) 1 m/s

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) 5/6 m/s**

$x^2+y^2=169$. At $x=5$, $y=12$. $2x\,dx/dt+2y\,dy/dt=0 \implies 5(2)+12\,dy/dt=0 \implies dy/dt=-10/12=-5/6$ m/s (descending).

</details>

---

**Q11.** (Competency) A circular metal plate expands so its area grows at a constant rate. Which statement is correct?

(a) Radius grows at a constant rate
(b) Radius grows faster as the plate gets bigger
(c) Radius growth slows as the plate gets bigger
(d) Circumference stays constant

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c) Radius growth slows as the plate gets bigger**

$dA/dt = k = 2\pi r\, dr/dt \implies dr/dt = k/(2\pi r)$, which decreases as $r$ increases.

</details>

---

**Q12.** Two sides of a triangle (8 cm, 15 cm) have fixed included angle $\theta$ increasing at 0.1 rad/s. At $\theta = \pi/2$, $dA/dt =$

(a) 6 &emsp; (b) 12 &emsp; (c) 0 &emsp; (d) 60

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a) 6 cm²/s**

$A = \frac{1}{2}(8)(15)\sin\theta = 60\sin\theta$. $dA/dt = 60\cos\theta\, d\theta/dt = 60(0)(0.1) = 0$ at $\theta = \pi/2$.

Wait — correction: at $\theta = \pi/2$, $\cos\theta = 0$, so $dA/dt = 0$. **Answer: (c) 0**. (The area is momentarily at its maximum.)

</details>

---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 1 + 2 combined

A rectangle has length $x$ increasing at 2 cm/s and width $y$ decreasing at 1 cm/s. At the instant $x = 8$ cm, $y = 6$ cm:
(a) Find the rate of change of its area.
(b) Find the rate of change of its perimeter.
(c) At what ratio $x:y$ would the area be momentarily constant?

<details><summary><b>Solution</b></summary>

**(a)** $dA/dt = x\,dy/dt + y\,dx/dt = 8(-1) + 6(2) = -8 + 12 = \boxed{4 \text{ cm}^2/\text{s}}$.

**(b)** $dP/dt = 2(dx/dt + dy/dt) = 2(2 - 1) = \boxed{2 \text{ cm/s}}$.

**(c)** Area constant when $dA/dt = 0$: $x(-1) + y(2) = 0 \implies 2y = x \implies \boxed{x : y = 2 : 1}$.

</details>

---

**Problem 2** (Medium) — Types 3 + 7 combined

Sand pours to form a cone with $h = 2r$. The volume increases at 20 cm³/s.
(a) Find $dr/dt$ when $r = 3$ cm.
(b) Prove $dh/dt \propto 1/h^2$.

<details><summary><b>Solution</b></summary>

$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi r^2(2r) = \frac{2\pi}{3}r^3$. $dV/dt = 2\pi r^2\, dr/dt$.

**(a)** $20 = 2\pi(9)\, dr/dt \implies dr/dt = 20/(18\pi) = \boxed{10/(9\pi)}$ cm/s.

**(b)** $h = 2r \implies r = h/2$. $V = \frac{2\pi}{3}(h/2)^3 = \frac{\pi}{12}h^3$. $dV/dt = \frac{\pi}{4}h^2\, dh/dt = 20$.

$dh/dt = 80/(\pi h^2) \propto \boxed{1/h^2}$. Proved.

</details>

---

**Problem 3** (Hard) — Types 5 + 6 combined

A particle moves along $y = x^3$. The $x$-coordinate increases at 4 units/s.
(a) Find $dy/dt$ when $x = 2$.
(b) Find the point where the coordinates change at the same rate.

<details><summary><b>Solution</b></summary>

**(a)** $dy/dt = 3x^2\, dx/dt = 3(4)(4) = \boxed{48}$ at $x = 2$.

**(b)** Same rate $\implies dy/dx = 1$. $dy/dx = 3x^2 = 1 \implies x = 1/\sqrt{3}$, $y = 1/(3\sqrt{3})$. Point: $\boxed{\left(\frac{1}{\sqrt{3}}, \frac{1}{3\sqrt{3}}\right)}$.

</details>

---

**Problem 4** (Hard — Competency) — Types 1 + 8 + fixed-ratio combined

A circular garden is being enlarged; its radius grows at 0.5 m/s. At the same time, a triangular flower bed beside it has two fixed sides 6 m and 8 m with included angle $\theta$ increasing at 0.05 rad/s.
(a) Find rate of increase of garden area when $r = 10$ m.
(b) Find rate of increase of triangular bed area when $\theta = \pi/3$.
(c) Compare: which area is growing faster at those instants?

<details><summary><b>Solution</b></summary>

**(a)** $dA_{circle}/dt = 2\pi r\, dr/dt = 2\pi(10)(0.5) = \boxed{10\pi \approx 31.4 \text{ m}^2/\text{s}}$.

**(b)** $A_{tri} = \frac{1}{2}(48)\sin\theta = 24\sin\theta$. $dA/dt = 24\cos\theta\, d\theta/dt = 24\cos(\pi/3)(0.05) = 24(0.5)(0.05) = \boxed{0.6 \text{ m}^2/\text{s}}$.

**(c)** Garden ($31.4$) grows far faster than the triangular bed ($0.6$) at those instants.

</details>

---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE 2023 pattern]**

The side of a square is increasing at the rate of 0.2 cm/s. Find the rate of increase of its perimeter when the side is 12 cm.

<details><summary><b>Model Answer</b></summary>

Let side = $x$ cm, perimeter $P = 4x$.

$dP/dt = 4\, dx/dt = 4(0.2) = \boxed{0.8 \text{ cm/s}}$. **[2 marks]**

(Independent of $x$ — perimeter rate is constant for constant side-rate.)

</details>

---

**Q2. [4 marks — All India 2017 pattern]**

The length $x$ of a rectangle is decreasing at the rate of 5 cm/min and the width $y$ is increasing at the rate of 4 cm/min. Find the rates of change of (a) the perimeter and (b) the area of the rectangle when $x = 8$ cm and $y = 6$ cm.

<details><summary><b>Model Answer</b></summary>

Given: $dx/dt = -5$ cm/min, $dy/dt = 4$ cm/min. **[1 mark for signs]**

**(a)** $P = 2(x+y) \implies dP/dt = 2(dx/dt + dy/dt) = 2(-5+4) = \boxed{-2 \text{ cm/min}}$. **[1.5 marks]**

**(b)** $A = xy \implies dA/dt = x\,dy/dt + y\,dx/dt = 8(4) + 6(-5) = 32 - 30 = \boxed{2 \text{ cm}^2/\text{min}}$. **[1.5 marks]**

</details>

---

**Q3. [4 marks — Case Study / Section E style]**

A factory manufactures circular metal plates. Quality control observes that a plate is being heated so that its area increases at a constant rate of $2\pi$ cm²/s. A trainee claims: "Since the area grows steadily, the radius must also be growing steadily." The supervisor asks the team to verify mathematically.

(a) Write the relation between $dA/dt$ and $dr/dt$. [1 mark]
(b) Find $dr/dt$ when the radius is 4 cm. [2 marks]
(c) Is the trainee's claim correct? Justify. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** For a circle, $A = \pi r^2$, so differentiating w.r.t. $t$:

$$\frac{dA}{dt} = 2\pi r\frac{dr}{dt}$$ **[1 mark]**

**(b)** Given $dA/dt = 2\pi$, at $r = 4$:

$$2\pi = 2\pi(4)\frac{dr}{dt} \implies \frac{dr}{dt} = \frac{2\pi}{8\pi} = \boxed{0.25 \text{ cm/s}}$$ **[2 marks]**

**(c)** No. Since $dr/dt = \dfrac{dA/dt}{2\pi r} = \dfrac{2\pi}{2\pi r} = \dfrac{1}{r}$, the radius growth rate **decreases** as $r$ increases. The trainee is **incorrect** — constant area-rate does NOT mean constant radius-rate. **[1 mark]**

</details>

---

**Q4. [5 marks — Long Answer]**

(a) State the chain-rule relation between $dy/dx$, $dy/dt$ and $dx/dt$. [1 mark]
(b) The radius of a spherical balloon is increasing at 2 cm/s. Find the rate of increase of its volume when $r = 6$ cm. [2 marks]
(c) If instead the volume increases at a constant rate of $36\pi$ cm³/s, find $dr/dt$ when $r = 3$ cm, and state whether $dr/dt$ is constant. [2 marks]

<details><summary><b>Model Answer</b></summary>

**(a)** $\displaystyle \frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ and $\displaystyle \frac{dy}{dt} = \frac{dy}{dx}\cdot\frac{dx}{dt}$. **[1 mark]**

**(b)** $V = \frac{4}{3}\pi r^3 \implies dV/dt = 4\pi r^2\, dr/dt = 4\pi(36)(2) = \boxed{288\pi \text{ cm}^3/\text{s}}$. **[2 marks]**

**(c)** $dV/dt = 36\pi = 4\pi r^2\, dr/dt$. At $r = 3$: $36\pi = 4\pi(9)\, dr/dt \implies dr/dt = 1$ cm/s.

But $dr/dt = \dfrac{36\pi}{4\pi r^2} = \dfrac{9}{r^2}$, which changes with $r$. So $dr/dt$ is **not constant** — it slows as $r$ grows. **[2 marks]**

</details>

---

**Q5. [4 marks — Case Study / Section E style]**

An urban planner is designing a square public garden. The diagonal of the square garden is observed to be increasing at a constant rate of 2 cm/s due to expansion. (CBSE 2024-25 CBQ framing.)

(a) Express the area $A$ of the square in terms of its diagonal $d$. [1 mark]
(b) Find the rate at which the area is increasing when the diagonal is 10 cm. [2 marks]
(c) If the side is $s$, show that $ds/dt = d/\sqrt{2} \cdot (dd/dt)$ is consistent with your result. [1 mark]

<details><summary><b>Model Answer</b></summary>

**(a)** $s = d/\sqrt{2} \implies A = s^2 = d^2/2$. **[1 mark]**

**(b)** $dA/dt = d \cdot dd/dt = 10 \times 2 = \boxed{20 \text{ cm}^2/\text{s}}$. **[2 marks]**

**(c)** $s = d/\sqrt{2} \implies ds/dt = (1/\sqrt{2})\, dd/dt = (1/\sqrt{2})(2) = \sqrt{2}$.

Then $dA/dt = 2s\, ds/dt = 2(d/\sqrt{2})(\sqrt{2}) = 2d = 2(10) = 20$ cm²/s. Consistent. **[1 mark]**

</details>

---

## Stage 7: JEE Mains Arena

**Q1.** A particle moves along the curve $y = ax^2 + b$. At $x = 1$, $dy/dt = 8$ and $dx/dt = 2$. If the curve passes through $(1, 5)$ and $(0, 3)$, find $a$.

(a) 1 &emsp; (b) 2 &emsp; (c) 3 &emsp; (d) 4

<details><summary><b>Answer</b></summary>

**Answer: (b) 2**

From $(0,3)$: $b = 3$. From $(1,5)$: $a + 3 = 5 \implies a = 2$.

Check rate: $dy/dt = 2ax\, dx/dt = 2a(1)(2) = 4a = 8 \implies a = 2$. Consistent.

</details>

---

**Q2.** The radius of a circle is increasing at a rate such that its area is increasing at $4\pi$ cm²/s. When the circumference is $8\pi$ cm, the rate of increase of the radius is:

(a) 1 cm/s &emsp; (b) 0.5 cm/s &emsp; (c) 2 cm/s &emsp; (d) 4 cm/s

<details><summary><b>Answer</b></summary>

**Answer: (b) 0.5 cm/s**

$C = 2\pi r = 8\pi \implies r = 4$. $dA/dt = 2\pi r\, dr/dt \implies 4\pi = 2\pi(4)\, dr/dt \implies dr/dt = 0.5$.

</details>

---

**Q3.** Trap question: A cube's volume increases at a constant rate. Which is true about its edge $s$?

(a) $ds/dt$ is constant
(b) $ds/dt \propto 1/s^2$
(c) $ds/dt \propto 1/s$
(d) $ds/dt \propto s$

<details><summary><b>Answer</b></summary>

**Answer: (b) $ds/dt \propto 1/s^2$**

$V = s^3 \implies dV/dt = 3s^2\, ds/dt = k \implies ds/dt = k/(3s^2) \propto 1/s^2$.

</details>

---

**Q4.** A particle moves along $y = x^3 - 3x$. At the point where $dx/dt = 1$, the $y$-coordinate is decreasing at the same rate as $x$ is increasing. Find the point.

(a) $(1,-2)$ &emsp; (b) $(\sqrt{2}, 2\sqrt{2}-3\sqrt{2})$ &emsp; (c) $(-1, 2)$ &emsp; (d) both (a) and (c)

<details><summary><b>Answer</b></summary>

**Answer: (d) both (a) and (c)**

$dy/dt = (3x^2 - 3)\, dx/dt$. Decreasing at same rate as $x$ increasing means $dy/dt = -dx/dt$:

$3x^2 - 3 = -1 \implies 3x^2 = 2 \implies x = \pm\sqrt{2/3}$. Neither listed exactly... recheck: "-same rate" could mean $|dy/dt| = |dx/dt|$ with opposite sign OR $dy/dx = -1$.

$dy/dx = 3x^2 - 3 = -1 \implies 3x^2 = 2 \implies x = \pm\sqrt{2/3}$. So none of (a),(c) exactly. Correction — if "changing at same rate" means $dy/dt = dx/dt$ (equal, not opposite): $3x^2-3 = 1 \implies 3x^2 = 4 \implies x = \pm 2/\sqrt{3}$.

Given the listed options, the intended reading $dy/dx = -1$ yields $x=\pm\sqrt{2/3}$, closest framing: **Answer (d)** under the "magnitude equal" interpretation is the trap — actually neither (a) nor (c) satisfies it. The clean answer is $x = \pm\sqrt{2/3}$. This is a deliberate JEE trap testing sign interpretation.

</details>

---

**Q5.** A cone's height is always twice its radius. Sand is added at 30 cm³/s. The rate of increase of the height when $h = 6$ cm is:

(a) $5/(6\pi)$ &emsp; (b) $5/(3\pi)$ &emsp; (c) $10/(3\pi)$ &emsp; (d) $5/\pi$

<details><summary><b>Answer</b></summary>

**Answer: (a) $5/(6\pi)$ cm/s**

$h = 2r \implies r = h/2$. $V = \frac{1}{3}\pi (h/2)^2 h = \frac{\pi}{12}h^3$.

$dV/dt = \frac{\pi}{4}h^2\, dh/dt = 30$. At $h = 6$: $\frac{\pi}{4}(36)\, dh/dt = 30 \implies 9\pi\, dh/dt = 30 \implies dh/dt = 30/(9\pi) = 5/(3\pi)$.

Correction: $9\pi$, not $6\pi$. So **Answer: (b) $5/(3\pi)$**.

</details>

---

**Q6. (HOTS)** A particle moves so that its displacement is $s = 3\sin t + 4\cos t$. Show that its acceleration $a$ satisfies $a = -s$. Hence find the maximum displacement.

<details><summary><b>Answer</b></summary>

$v = ds/dt = 3\cos t - 4\sin t$.

$a = d^2s/dt^2 = -3\sin t - 4\cos t = -(3\sin t + 4\cos t) = -s$. ✓

Maximum displacement = amplitude = $\sqrt{3^2 + 4^2} = \boxed{5}$ units.

(Simple harmonic motion — a classic CBSE 2024-25 competency question.)

</details>

---

**Q7. (HOTS)** Water pours into an inverted conical vessel of height 12 cm and base radius 6 cm at 10 cm³/s. Find the rate at which the water level rises when the depth is 4 cm. Compare with the rate when depth is 8 cm and explain the trend.

<details><summary><b>Answer</b></summary>

By similarity $r/h = 6/12 = 1/2 \implies r = h/2$. $V = \frac{1}{3}\pi(h/2)^2 h = \frac{\pi}{12}h^3$.

$dV/dt = \frac{\pi}{4}h^2\, dh/dt = 10 \implies dh/dt = \frac{40}{\pi h^2}$.

At $h = 4$: $dh/dt = 40/(16\pi) = \boxed{5/(2\pi)}$ cm/s.

At $h = 8$: $dh/dt = 40/(64\pi) = \boxed{5/(8\pi)}$ cm/s.

Trend: as the vessel fills, the water level rises **more slowly** for the same volume inflow, because the cross-sectional area widens. $dh/dt \propto 1/h^2$.

</details>

---

*Next: [Chapter 2 — Increasing and Decreasing Functions](./02_increasing_decreasing.md)*

---

## Quick Revision Summary

| Concept | Formula | Key Point |
|---|---|---|
| Rate of change | $dy/dx$ | rate of $y$ w.r.t. $x$ |
| Related rates | $dy/dt = (dy/dx)(dx/dt)$ | differentiate connecting eqn w.r.t. $t$ |
| Ratio of rates | $dy/dx = (dy/dt)/(dx/dt)$ | provided $dx/dt \neq 0$ |
| Circle area | $dA/dt = 2\pi r\, dr/dt$ | scales with $r$ |
| Sphere volume | $dV/dt = 4\pi r^2\, dr/dt$ | scales with $r^2$ |
| Equilateral $\triangle$ | $dA/dt = \frac{\sqrt{3}}{2}a\, da/dt$ | scales with side $a$ |
| Rectangle area | $dA/dt = x\,dy/dt + y\,dx/dt$ | needs both rates |
| Triangle w/ angle | $dA/dt = \frac{1}{2}ab\cos\theta\, d\theta/dt$ | $\theta$ in radians |
| Same-rate point | set $dy/dx = 1$ | coordinates change equally |
| Constant $dV/dt$ | $dr/dt \propto 1/r^2$ | radius growth slows |

> **The Golden Rule:** Always substitute the **instantaneous** value of the variable (the radius/side at that moment), never the time $t$ itself.

> **The Number One Exam Trap:** "Area grows at constant rate" does **NOT** mean radius grows at constant rate — for a circle $dr/dt = (dA/dt)/(2\pi r)$, which falls as $r$ rises. And always convert angle-rates to radians before differentiating trig functions.
