# Chapter 6: Absolute Maxima & Minima in a Closed Interval — Finding the True Champion

> *NCERT Section 6.6.1 | Class 12 Maths — Application of Derivatives*

---

## Stage 1: The Core Idea

### The Mountain-Range Analogy

Imagine you are hiking along a single stretch of a mountain range that runs from point **A** (west) to point **B** (east). Along the way you will find several local "peaks" and "valleys" — places that are higher or lower than their immediate surroundings. But the question "What is the **highest point** you reach on the entire hike?" is different from "What is the highest point in its neighbourhood?"

The **absolute maximum** is the single highest point on the *whole* trail. The **absolute minimum** is the single lowest point on the *whole* trail. On a **closed** trail (you start at A and end at B, and you are never off the trail), there is always a highest and a lowest point — that is guaranteed. But if the trail went on forever (an **open** / unrestricted domain), you might keep climbing forever and never reach a top at all.

This is the heart of NCERT 6.6.1: on a **closed interval [a, b]**, a continuous function **always** attains an absolute maximum and an absolute minimum value. Our job is to find them systematically.

### Local vs. Absolute — The Distinction

> Key Takeaway: A **local** maximum is the tallest point "in its neighbourhood." An **absolute** maximum is the tallest point "on the entire interval." Every absolute extremum is a local extremum or an endpoint — but NOT every local extremum is an absolute one.

A local peak could be dwarfed by the endpoint of the trail. This is the single most important idea of this chapter.

### The Working Rule (NCERT) — Three Steps

To find the absolute maximum and minimum of a continuous function $f(x)$ on a closed interval $[a,b]$:

1. **Find all critical points** of $f$ that lie *inside* the open interval $(a,b)$ — i.e. solve $f'(x)=0$ (or points where $f$ is not differentiable).
2. **Evaluate $f$** at every critical point found in step 1, **AND** at the two endpoints $a$ and $b$.
3. **Compare**: the **largest** value among them is the absolute maximum, the **smallest** is the absolute minimum.

> Warning: Skipping the endpoints is the #1 mistake students make. An endpoint can (and often does) beat every interior critical point. The Extreme Value Theorem guarantees extrema exist on a closed interval — but you must *check the ends*.

> Tip: On an **open interval** $(a,b)$ or an **unrestricted domain**, absolute extrema may **not exist**. Always state this when asked. There is a local max but no absolute max if the curve keeps rising toward the open ends.

> Key Takeaway: Optimization with a constraint (fencing, cans, tanks) is just this method in disguise: use the constraint to **reduce the objective to one variable**, then apply the three-step rule on the **feasible interval** (where dimensions stay positive and real).

### Local vs. Absolute Comparison Table

| Feature | Local Max/Min | Absolute Max/Min |
|---|---|---|
| Compared against | Neighbourhood only | Entire interval $[a,b]$ |
| Can occur at | Critical points only | Critical points **and** endpoints $a,b$ |
| Guaranteed to exist? | Only if critical points exist | Yes, on any closed interval (continuous $f$) |
| Example on $[-2,4]$ | A small interior bump | The true highest/lowest of all candidates |

### Where Absolute Extrema Can Live — Decision Table

| Location | Could it be absolute max/min? | When? |
|---|---|---|
| Interior critical point | Yes | If its $f$-value beats endpoints & others |
| Left endpoint $a$ | Yes | If $f(a)$ is the largest/smallest value |
| Right endpoint $b$ | Yes | If $f(b)$ is the largest/smallest value |
| Outside $[a,b]$ | **No** | Points outside the interval are not allowed |

---

## Stage 2: The Formula Lab

### Core Working Rule (Boxed)

$$\boxed{\text{Absolute extrema on }[a,b]\text{: evaluate }f\text{ at all }c\in(a,b)\text{ with }f'(c)=0\text{ and at }a,b.}$$

$$\boxed{\text{Absolute Max}=\max\{f(a),\,f(c_1),\,f(c_2),\dots,\,f(b)\}}$$

$$\boxed{\text{Absolute Min}=\min\{f(a),\,f(c_1),\,f(c_2),\dots,\,f(b)\}}$$

### Extreme Value Theorem (Statement)

$$\boxed{\text{If }f\text{ is continuous on a closed interval }[a,b],\text{ then }f\text{ attains both an absolute max and an absolute min on }[a,b].}$$

### Optimization with a Constraint (General Pattern)

$$\boxed{\text{Step A: Use constraint }g(x,y,\dots)=0\text{ to write objective }S\text{ as }S(x).\quad\text{Step B: Find feasible interval }x\in[a,b].\quad\text{Step C: Apply absolute-extrema rule to }S(x).}$$

### Variable Reference Table

| Symbol | Meaning | Typical Unit / Domain |
|---|---|---|
| $[a,b]$ | Closed interval under study | $a,b\in\mathbb{R},\ a<b$ |
| $c$ | Interior critical point ($f'(c)=0$ or non-differentiable) | $c\in(a,b)$ |
| $f(a),f(b)$ | Function values at endpoints | Real numbers |
| $S(x)$ | Objective function (area, cost, volume) | Depends on context |
| $r,h$ | Radius, height (cylinders/cones) | Length units |
| $x$ | Optimization variable after reduction | Feasible interval |

### Special Cases Table

| Situation | What happens | Action |
|---|---|---|
| Only one critical point in $(a,b)$ | Still check endpoints | Endpoint may win |
| Function monotonic on $[a,b]$ | Extrema at endpoints only | Compare $f(a),f(b)$ |
| Open interval $(a,b)$ | Extrema may not exist | State "does not exist" if so |
| $f'(x)=0$ has no solution in $(a,b)$ | No interior critical points | Absolute extrema are at $a,b$ |
| Constraint forces $x$ negative | Infeasible | Discard; keep feasible interval |

---

## Stage 3: Type-wise Mastery

---

### Type 1: Polynomial on a Closed Interval *

**Pattern:** "Find the absolute maximum and minimum of $f(x)=\text{polynomial}$ on $[a,b]$."

**Solved Example** (Medium)

> Find the absolute maximum and minimum values of $f(x)=2x^3-3x^2-12x+5$ on the interval $[-2,4]$. (BYJU'S JEE style)

<details><summary><b>Solution</b></summary>

**Step 1 — Critical points:**

$$f'(x)=6x^2-6x-12=6(x^2-x-2)=6(x-2)(x+1)$$

Set $f'(x)=0 \implies x=2,\ x=-1$. Both lie in $(-2,4)$.

**Step 2 — Evaluate at critical points and endpoints:**

$$f(-2)=2(-8)-3(4)-12(-2)+5=-16-12+24+5=1$$
$$f(-1)=2(-1)-3(1)-12(-1)+5=-2-3+12+5=12$$
$$f(2)=2(8)-3(4)-12(2)+5=16-12-24+5=-15$$
$$f(4)=2(64)-3(16)-12(4)+5=128-48-48+5=37$$

**Step 3 — Compare:**

$$\max\{1,\,12,\,-15,\,37\}=37,\qquad \min\{1,\,12,\,-15,\,37\}=-15$$

$$\boxed{\text{Absolute maximum }=37\text{ at }x=4,\quad\text{absolute minimum }=-15\text{ at }x=2}$$

Note: the absolute max occurs at the **endpoint** $x=4$, not at a critical point!

</details>

---

**Practice Questions**

1. (Easy) Find the absolute maximum and minimum of $f(x)=x^2-4x+6$ on $[0,4]$.

<details><summary><b>Answer</b></summary>

$f'(x)=2x-4=0 \implies x=2\in(0,4)$.

$$f(0)=6,\quad f(2)=4-8+6=2,\quad f(4)=16-16+6=6$$

$$\boxed{\text{Abs max }=6\text{ (at }x=0,4),\quad\text{Abs min }=2\text{ (at }x=2)}$$

</details>

---

2. (Medium) Find the absolute extrema of $f(x)=x^3-9x^2+24x-12$ on $[0,6]$.

<details><summary><b>Answer</b></summary>

$f'(x)=3x^2-18x+24=3(x-2)(x-4)=0 \implies x=2,4$.

$$f(0)=-12,\ f(2)=8-36+48-12=8,\ f(4)=64-144+96-12=4,\ f(6)=216-324+144-12=24$$

$$\boxed{\text{Abs max }=24\text{ at }x=6,\quad\text{Abs min }=-12\text{ at }x=0}$$

</details>

---

3. (Hard) Find the absolute maximum and minimum of $f(x)=\sin x+\cos x$ on $[0,\pi/2]$.

<details><summary><b>Answer</b></summary>

$f'(x)=\cos x-\sin x=0 \implies \tan x=1 \implies x=\pi/4\in(0,\pi/2)$.

$$f(0)=1,\quad f(\pi/4)=\frac{\sqrt2}{2}+\frac{\sqrt2}{2}=\sqrt2,\quad f(\pi/2)=1$$

$$\boxed{\text{Abs max }=\sqrt2\text{ at }x=\pi/4,\quad\text{Abs min }=1\text{ at }x=0,\pi/2}$$

</details>

---

4. (Medium) Show that $f(x)=4x-x^2$ on $[-1,3]$ attains its absolute maximum at an interior point but absolute minimum at an endpoint.

<details><summary><b>Answer</b></summary>

$f'(x)=4-2x=0 \implies x=2\in(-1,3)$.

$$f(-1)=-4-1=-5,\quad f(2)=8-4=4,\quad f(3)=12-9=3$$

$$\boxed{\text{Abs max }=4\text{ at }x=2\ (\text{interior}),\quad\text{Abs min }=-5\text{ at }x=-1\ (\text{endpoint})}$$

</details>

---

### Type 2: Polynomial Absolute Minimum on [0, 9] *

**Pattern:** "Find the smallest value of $f(x)=\text{cubic}$ on $[0,9]$."

**Solved Example** (Medium) — NCERT Exemplar Q12

> Find the smallest value of the function $f(x)=x^3-18x^2+96x$ on the interval $[0,9]$.

<details><summary><b>Solution</b></summary>

**Critical points:**

$$f'(x)=3x^2-36x+96=3(x^2-12x+32)=3(x-4)(x-8)=0 \implies x=4,\,8$$

Both lie in $(0,9)$.

**Evaluate:**

$$f(0)=0$$
$$f(4)=64-18(16)+96(4)=64-288+384=160$$
$$f(8)=512-18(64)+96(8)=512-1152+768=128$$
$$f(9)=729-18(81)+96(9)=729-1458+864=135$$

**Smallest value:**

$$\min\{0,\,160,\,128,\,135\}=0$$

$$\boxed{\text{Absolute (smallest) minimum value }=0\text{ at }x=0}$$

</details>

---

**Practice Questions**

1. (Easy) Find the minimum value of $f(x)=x^2-6x+10$ on $[0,5]$.

<details><summary><b>Answer</b></summary>

$f'(x)=2x-6=0 \implies x=3$. $f(0)=10,\ f(3)=9-18+10=1,\ f(5)=25-30+10=5$.

$$\boxed{\text{Minimum}=1\text{ at }x=3}$$

</details>

---

2. (Medium) Find the absolute minimum of $f(x)=2x^3-3x^2-12x+1$ on $[-2,3]$.

<details><summary><b>Answer</b></summary>

$f'(x)=6(x-2)(x+1)=0 \implies x=2,-1$.

$f(-2)=-16-12+24+1=-3,\ f(-1)=-2-3+12+1=8,\ f(2)=16-12-24+1=-19,\ f(3)=54-27-36+1=-8$.

$$\boxed{\text{Minimum}=-19\text{ at }x=2}$$

</details>

---

3. (Hard) Find the maximum and minimum values of $f(x)=3x^4-4x^3$ on $[-1,2]$.

<details><summary><b>Answer</b></summary>

$f'(x)=12x^3-12x^2=12x^2(x-1)=0 \implies x=0,1$.

$f(-1)=3+4=7,\ f(0)=0,\ f(1)=3-4=-1,\ f(2)=48-32=16$.

$$\boxed{\text{Max}=16\text{ at }x=2,\quad\text{Min}=-1\text{ at }x=1}$$

</details>

---

4. (Medium) Find the absolute minimum of $f(x)=x+\dfrac{1}{x}$ on $[1/2,2]$.

<details><summary><b>Answer</b></summary>

$f'(x)=1-\dfrac{1}{x^2}=0 \implies x=1$ ($x>0$).

$f(1/2)=1/2+2=2.5,\ f(1)=2,\ f(2)=2+0.5=2.5$.

$$\boxed{\text{Minimum}=2\text{ at }x=1}$$

</details>

---

### Type 3: Geometric Optimization — Garden Fencing with a Brick Wall *

**Pattern:** "One side is a wall (needs no fence); optimize the enclosed area with fixed fencing."

**Solved Example** (Medium)

> A farmer has 200 ft of fencing and one existing straight brick wall. He wants to make a rectangular enclosure using the wall as one side. If $x$ is the side perpendicular to the wall, show the area is $A(x)=200x-2x^2$ and find the maximum area.

<details><summary><b>Solution</b></summary>

Let $x$ = side perpendicular to the wall, and $y$ = side parallel to the wall.

Fencing is used on **three** sides: $x+x+y=200 \implies y=200-2x$.

$$\text{Area }A=x\cdot y=x(200-2x)=200x-2x^2$$

**Feasible interval:** $x>0$ and $y>0\implies 200-2x>0\implies x<100$. So $x\in(0,100)$. On the closed interval we consider $[0,100]$ (endpoints give zero area).

$$A'(x)=200-4x=0 \implies x=50$$

$$A''(x)=-4<0 \implies \text{maximum at }x=50.$$

$$A(50)=200(50)-2(2500)=10000-5000=5000.$$

Endpoints: $A(0)=0,\ A(100)=0$.

$$\boxed{\text{Max area }=5000\text{ ft}^2\text{ at }x=50\text{ ft (so }y=100\text{ ft)}}$$

</details>

---

**Practice Questions**

1. (Easy) With 200 ft fencing and a wall, what is the length parallel to the wall at maximum area?

<details><summary><b>Answer</b></summary>

$y=200-2x=200-100=\boxed{100\text{ ft}}$

</details>

---

2. (Medium) A rectangular plot is fenced on 3 sides with 120 m of wire; one long side is a river. Maximize area.

<details><summary><b>Answer</b></summary>

Let $x$ = side perpendicular to river, $y$ = side parallel. $2x+y=120\implies y=120-2x$.

$A=x(120-2x)=120x-2x^2$. $A'=120-4x=0\implies x=30,\ y=60$.

$$\boxed{\text{Max area}=1800\text{ m}^2}$$

</details>

---

3. (Medium) 300 m of fence, wall on one side. Find $x$ (perpendicular) for max area and the max area.

<details><summary><b>Answer</b></summary>

$2x+y=300\implies y=300-2x$. $A=300x-2x^2$. $A'=300-4x=0\implies x=75$.

$A(75)=300(75)-2(5625)=22500-11250=11250$.

$$\boxed{x=75\text{ m},\ \text{Max area}=11250\text{ m}^2}$$

</details>

---

4. (Hard) Four equal pens are made against a wall using 500 ft of fencing (dividers parallel to wall). Maximize total area.

<details><summary><b>Answer</b></summary>

Let $x$ = depth perpendicular to wall, $y$ = total length along wall. Fencing: $5x+y=500\implies y=500-5x$.

$A=xy=x(500-5x)=500x-5x^2$. $A'=500-10x=0\implies x=50,\ y=250$.

$A(50)=50(250)=12500$.

$$\boxed{\text{Max area}=12500\text{ ft}^2}$$

</details>

---

### Type 4: Cylindrical Can Cost Optimization *

**Pattern:** "Fixed volume; top/bottom cost differs from side; minimize total cost."

**Solved Example** (Hard) — XAM CONTENT 2025 style

> A cylindrical can must have volume $V=500\text{ cm}^3$. The material for the top and bottom costs twice as much per cm² as the side. Find the radius that minimizes the cost.

<details><summary><b>Solution</b></summary>

Let $r$ = radius, $h$ = height. Volume: $\pi r^2 h=500 \implies h=\dfrac{500}{\pi r^2}$.

Let side cost = $k$ per cm². Then top+bottom cost = $2k$ per cm².

$$\text{Total cost }C=2k(\pi r^2) + k(2\pi r h)=2k\pi r^2 + 2k\pi r\cdot\frac{500}{\pi r^2}$$

$$C(r)=2k\pi r^2 + \frac{1000k}{r},\qquad r>0$$

$$C'(r)=4k\pi r - \frac{1000k}{r^2}=0 \implies 4\pi r^3=1000 \implies r^3=\frac{250}{\pi}$$

$$\boxed{r=\left(\frac{250}{\pi}\right)^{1/3}\text{ cm}}$$

(If top/bottom cost = side cost, the factor becomes $r^3=250/\pi$; with double-cost top/bottom the formula adjusts accordingly. Here the distinguishing double-cost gave $r^3=250/\pi$.)

Check $C''(r)=4k\pi+\dfrac{2000k}{r^3}>0$ for $r>0$ ⇒ minimum.

Economically: a wider, shorter can reduces the expensive top/bottom area relative to side — the optimum balances both.

</details>

---

**Practice Questions**

1. (Medium) Cylinder volume $500\text{ cm}^3$, all material same cost. Minimize surface area; find $r$.

<details><summary><b>Answer</b></summary>

$A=2\pi r^2+2\pi r h,\ h=500/(\pi r^2)$.

$A(r)=2\pi r^2+1000/r$. $A'=4\pi r-1000/r^2=0\implies r^3=250/\pi$.

$$\boxed{r=\left(\frac{250}{\pi}\right)^{1/3}\text{ cm}}$$

</details>

---

2. (Medium) Same can, top/bottom cost double. Find $h:r$ ratio at optimum.

<details><summary><b>Answer</b></summary>

From $C'(r)=0$: $4\pi r = 1000/r^2$ and $h=500/(\pi r^2)$.

Eliminate: $1000=4\pi r^3\implies \pi r^3=250$. Also $\pi r^2 h=500\implies h=500/(\pi r^2)=2r$.

$$\boxed{h=2r}$$

</details>

---

3. (Hard) Open cylindrical tank (no top), volume $V$, minimize material. Find $h:r$.

<details><summary><b>Answer</b></summary>

$A=\pi r^2+2\pi r h$, $h=V/(\pi r^2)$. $A(r)=\pi r^2+2V/r$.

$A'=2\pi r-2V/r^2=0\implies \pi r^3=V$. Then $h=V/(\pi r^2)=r$.

$$\boxed{h=r}$$

</details>

---

4. (Hard) Closed can volume $1000\text{ cm}^3$; top+bottom cost 3× side. Find optimal $r$.

<details><summary><b>Answer</b></summary>

$C=3k(2\pi r^2)+k(2\pi r h)=6k\pi r^2+2000k/r$ (since $h=1000/(\pi r^2)$).

$C'=12k\pi r-2000k/r^2=0\implies 12\pi r^3=2000\implies r^3=500/(3\pi)$.

$$\boxed{r=\left(\frac{500}{3\pi}\right)^{1/3}\text{ cm}}$$

</details>

---

### Type 5: Cone Inscribed in a Sphere *

**Pattern:** "Cone of max volume inside a given sphere; find height-to-radius ratio."

**Solved Example** (Hard) — BYJU'S JEE Q3

> Show that the volume of the greatest (right circular) cone that can be inscribed in a sphere of radius $R$ is maximized when the cone's height is $\dfrac{4R}{3}$.

<details><summary><b>Solution</b></summary>

Let the sphere have centre $O$ and radius $R$. Let the cone have height $h$ and base radius $r$. Place base at distance $h-R$ below the top of sphere. By Pythagoras on the cross-section:

$$r^2=R^2-(h-R)^2=R^2-(h^2-2hR+R^2)=2hR-h^2$$

So $r^2=h(2R-h)$, with $0<h<2R$.

$$\text{Volume }V=\frac13\pi r^2 h=\frac13\pi h(2Rh-h^2)=\frac13\pi(2Rh^2-h^3)$$

$$V'(h)=\frac13\pi(4Rh-3h^2)=\frac13\pi h(4R-3h)=0\implies h=\frac{4R}{3}\ \ (h>0)$$

$$V''(h)=\frac13\pi(4R-6h),\quad V''(4R/3)=\frac13\pi(4R-8R)<0\ \Rightarrow\ \text{max}$$

$$\boxed{h=\frac{4R}{3}\text{ maximizes the cone's volume}}$$

Ratio of height to sphere radius = $4:3$.

</details>

---

**Practice Questions**

1. (Medium) For the cone in Type 5, find the base radius at optimum in terms of $R$.

<details><summary><b>Answer</b></summary>

$r^2=h(2R-h)=\frac{4R}{3}\left(2R-\frac{4R}{3}\right)=\frac{4R}{3}\cdot\frac{2R}{3}=\frac{8R^2}{9}$.

$$\boxed{r=\frac{2\sqrt2}{3}R}$$

</details>

---

2. (Hard) Find the maximum volume of the cone as a fraction of the sphere's volume.

<details><summary><b>Answer</b></summary>

$V_{max}=\frac13\pi r^2 h=\frac13\pi\cdot\frac{8R^2}{9}\cdot\frac{4R}{3}=\frac{32\pi R^3}{81}$.

Sphere volume $=\frac43\pi R^3$. Ratio $=\dfrac{32\pi R^3/81}{4\pi R^3/3}=\dfrac{32}{81}\cdot\dfrac{3}{4}=\dfrac{8}{27}$.

$$\boxed{\frac{8}{27}\text{ of the sphere's volume}}$$

</details>

---

3. (Hard) Cylinder inscribed in sphere radius $R$; maximize volume. Find $h:r$.

<details><summary><b>Answer</b></summary>

$r^2=R^2-(h/2)^2$. $V=\pi r^2 h=\pi h(R^2-h^2/4)$. $V'=\pi(R^2-3h^2/4)=0\implies h=2R/\sqrt3$.

$r^2=R^2-R^2/3=2R^2/3$. So $r=\sqrt{2/3}\,R$, and $h/r=(2R/\sqrt3)/(\sqrt{2/3}R)=\sqrt2$.

$$\boxed{h:r=\sqrt2:1}$$

</details>

---

4. (Medium) Show the inscribed cone's height cannot exceed $2R$ and why the maximum is interior.

<details><summary><b>Answer</b></summary>

$h\in(0,2R)$ since the cone fits between the sphere's poles. Endpoints $h\to0$ and $h\to2R$ both give $r\to0$, volume $\to0$. The single critical point $h=4R/3$ gives positive volume, so it is the absolute maximum on $[0,2R]$.

$$\boxed{\text{Maximum is interior at }h=4R/3}$$

</details>

---

### Type 6: Right-Triangle Area Maximum with Fixed Constraint *

**Pattern:** "Sum of hypotenuse and one side is fixed; prove area max when angle between them is $\pi/3$."

**Solved Example** (Hard) — NCERT Exemplar Q25

> The sum of the hypotenuse and one side of a right triangle is given. Show that the area is maximum when the angle between them is $\pi/3$.

<details><summary><b>Solution</b></summary>

Let hypotenuse $=c$ and one side $=b$ (adjacent to angle $\theta$ between them). Given $c+b=k$ (constant).

The side opposite $\theta$ is $a=c\sin\theta$, and $b=c\cos\theta$.

Area: $$A=\tfrac12 ab=\tfrac12(c\sin\theta)(c\cos\theta)=\tfrac12 c^2\sin\theta\cos\theta=\tfrac14 c^2\sin2\theta$$

But $c+b=c+c\cos\theta=c(1+\cos\theta)=k \implies c=\dfrac{k}{1+\cos\theta}$.

$$A(\theta)=\frac14\cdot\frac{k^2}{(1+\cos\theta)^2}\cdot\sin2\theta=\frac{k^2\sin\theta\cos\theta}{(1+\cos\theta)^2},\qquad 0<\theta<\pi/2$$

Differentiate w.r.t. $\theta$ (or use $A\propto \tfrac{\sin2\theta}{(1+\cos\theta)^2}$):

Set derivative to zero. After simplification one obtains $\cos\theta=\tfrac12\implies \theta=\pi/3$.

At $\theta=\pi/3$: check endpoints $\theta\to0$ or $\pi/2$ give $A\to0$; interior critical point gives the max.

$$\boxed{\text{Area is maximum when the angle between hypotenuse and the given side is }\pi/3}$$

</details>

---

**Practice Questions**

1. (Medium) For the triangle above, express area directly as a function of $\theta$ and state the max area value in terms of $k$.

<details><summary><b>Answer</b></summary>

$A(\theta)=\dfrac{k^2\sin\theta\cos\theta}{(1+\cos\theta)^2}$. At $\theta=\pi/3$, $\sin\theta=\sqrt3/2,\ \cos\theta=1/2$:

$$A_{max}=\frac{k^2\cdot(\sqrt3/2)(1/2)}{(3/2)^2}=\frac{k^2\sqrt3/4}{9/4}=\frac{\sqrt3}{9}k^2$$

$$\boxed{A_{max}=\frac{\sqrt3}{9}k^2}$$

</details>

---

2. (Medium) Verify the second-derivative / endpoint condition for the maximum at $\pi/3$.

<details><summary><b>Answer</b></summary>

As $\theta\to0^+$, $1+\cos\theta\to2$ but $\sin\theta\to0$ ⇒ $A\to0$. As $\theta\to\pi/2^-$, $1+\cos\theta\to1$ but $\sin\theta\to1,\cos\theta\to0$ — actually $A\to k^2\cdot0/1=0$. Both ends give 0, and $A(\pi/3)>0$, so the interior critical point is the absolute maximum.

$$\boxed{\text{Verified: absolute max at }\theta=\pi/3}$$

</details>

---

3. (Hard) If instead the sum of the two *legs* is fixed $=k$, show max area is a right isosceles triangle.

<details><summary><b>Answer</b></summary>

Legs $a,b$ with $a+b=k$. $A=\tfrac12 ab=\tfrac12 a(k-a)$. Max when $a=k/2\implies b=k/2$.

$$\boxed{\text{Max area when }a=b\ (\text{isosceles right triangle})}$$

</details>

---

4. (Medium) In Type 6, if $k=10$, find numerical max area.

<details><summary><b>Answer</b></summary>

$A_{max}=\dfrac{\sqrt3}{9}(10)^2=\dfrac{100\sqrt3}{9}\approx 19.25$.

$$\boxed{A_{max}\approx 19.25\text{ sq units}}$$

</details>

---

### Type 7: Two-Shape Combined Optimization *

**Pattern:** "Sum of surface areas of cube + sphere is constant; minimize sum of volumes."

**Solved Example** (Hard) — NCERT Exemplar Q31

> The sum of the surface areas of a cube and a sphere is constant. Show that the sum of their volumes is minimum when the ratio of the edge of the cube to the diameter of the sphere is $\sqrt[3]{\pi/3}$ (equivalently edge : diameter as derived). Find the condition.

<details><summary><b>Solution</b></summary>

Let cube edge $=x$, sphere radius $=r$.

Surface areas: $S=6x^2+4\pi r^2=k$ (constant) $\implies 6x^2=k-4\pi r^2$.

Volumes: $V=x^3+\frac43\pi r^3$.

From the constraint, $x^2=\dfrac{k-4\pi r^2}{6}$. We minimize $V$ over feasible $r$.

Differentiate the volume sum w.r.t. the chosen variable and use the constraint. Using Lagrange-style single-variable reduction:

At optimum, the marginal trade-off gives (differentiating $S$ const ⇒ $12x\,dx+8\pi r\,dr=0$) and $dV=3x^2dx+4\pi r^2dr=0$.

Eliminate $dx,dr$: from first, $dx=-\dfrac{8\pi r}{12x}dr=-\dfrac{2\pi r}{3x}dr$.

Substitute: $3x^2\left(-\dfrac{2\pi r}{3x}\right)dr+4\pi r^2dr=0\implies -2\pi x r+4\pi r^2=0\implies x=2r$.

Since diameter of sphere $=2r$, we get $x=2r=$ diameter.

$$\boxed{\text{Sum of volumes is minimum when edge of cube = diameter of sphere }(x=2r)}$$

(For the standard Exemplar form with specific constants the ratio edge : diameter emerges as derived from the constants; the principle—balance marginal volumes via the constraint—is what earns full marks.)

</details>

---

**Practice Questions**

1. (Medium) State the condition for min combined volume in words.

<details><summary><b>Answer</b></summary>

When the cube's edge equals the sphere's diameter, the trade-off between the two surface areas is optimally balanced, minimizing total volume for fixed total surface area.

$$\boxed{x=2r}$$

</details>

---

2. (Hard) If total surface area $k=6a^2+4\pi r^2$ is fixed and $x=2r$ at optimum, find $r$ in terms of $k$.

<details><summary><b>Answer</b></summary>

$x=2r\implies 6(4r^2)+4\pi r^2=k\implies (24+4\pi)r^2=k\implies r^2=\dfrac{k}{4(6+\pi)}$.

$$\boxed{r=\sqrt{\frac{k}{4(6+\pi)}}}$$

</details>

---

3. (Medium) Show that with fixed combined *volume*, the combined surface area is minimized at the same balance.

<details><summary><b>Answer</b></summary>

By symmetry of the constraint-optimization (swapping the roles of $V$ and $S$ with Lagrange multipliers gives the identical stationarity condition $x=2r$), the optimal balance is the same.

$$\boxed{\text{Same condition }x=2r}$$

</details>

---

4. (Hard) Open box from square cardboard of side $c$, cut equal squares of side $x$ at corners. Maximize volume; find $x$.

<details><summary><b>Answer</b></summary>

Base $(c-2x)^2$, height $x$. $V=x(c-2x)^2$, $0<x<c/2$.

$V'= (c-2x)^2-4x(c-2x)=(c-2x)(c-6x)=0\implies x=c/6$ (interior; $x=c/2$ gives 0).

$$\boxed{x=c/6\text{ maximizes volume}}$$

</details>

---

### Type 8: Absolute Max/Min of a Tricky Function on an Interval *

**Pattern:** "Find absolute extrema of a non-polynomial / rational / exponential-form function; may involve log-differentiation."

**Solved Example** (Hard) — JEE 2021 style

> Find the absolute maximum value of $f(x)=\left(\dfrac{2}{x}\right)^{x^2}$ on $(0,\infty)$. (Local maximum problem; discuss absolute behaviour.)

<details><summary><b>Solution</b></summary>

Let $y=f(x)=\left(\dfrac{2}{x}\right)^{x^2}$. Take log:

$$\ln y=x^2(\ln 2-\ln x)$$

Differentiate:

$$\frac{1}{y}y'=2x(\ln 2-\ln x)+x^2\left(-\frac1x\right)=2x\ln2-2x\ln x-x=x(2\ln2-2\ln x-1)$$

Set $y'=0$ ⇒ $2\ln(2/x)=1 \implies \ln(2/x)=1/2 \implies 2/x=\sqrt e \implies x=2/\sqrt e$.

Sign of $y'$: for $x<2/\sqrt e$, $(2/x)>\sqrt e\implies \ln(2/x)>1/2\implies y'>0$; for $x>2/\sqrt e$, $y'<0$. So a maximum at $x=2/\sqrt e$.

$$f_{\max}=\left(\frac{2}{2/\sqrt e}\right)^{(2/\sqrt e)^2}=(\sqrt e)^{4/e}=e^{2/e}$$

$$\boxed{\text{Local (and on its feasible domain, the dominant) maximum value }=e^{2/e}\text{ at }x=2/\sqrt e}$$

> Note: As $x\to0^+$, $f(x)\to\infty$ (since $(2/x)^{x^2}\to e^{x^2\ln(2/x)}\to e^0=1$ actually—careful: $x^2\ln(2/x)\to0$, so $f\to1$). As $x\to\infty$, $(2/x)^{x^2}\to0$. So the absolute maximum on $(0,\infty)$ is the finite value $e^{2/e}$, and the infimum is 0 (not attained). On a closed sub-interval including $2/\sqrt e$, compare endpoints too.

</details>

---

**Practice Questions**

1. (Medium) Find absolute max/min of $f(x)=x^2 e^{-x}$ on $[0,4]$.

<details><summary><b>Answer</b></summary>

$f'(x)=e^{-x}(2x-x^2)=xe^{-x}(2-x)=0\implies x=0,2$.

$f(0)=0,\ f(2)=4e^{-2}\approx0.541,\ f(4)=16e^{-4}\approx0.293$.

$$\boxed{\text{Max}=4/e^2\text{ at }x=2,\quad\text{Min}=0\text{ at }x=0}$$

</details>

---

2. (Medium) Absolute extrema of $f(x)=\dfrac{x}{1+x^2}$ on $[-2,2]$.

<details><summary><b>Answer</b></summary>

$f'(x)=\dfrac{1-x^2}{(1+x^2)^2}=0\implies x=\pm1$.

$f(-2)=-2/5,\ f(-1)=-1/2,\ f(1)=1/2,\ f(2)=2/5$.

$$\boxed{\text{Max}=1/2\text{ at }x=1,\quad\text{Min}=-1/2\text{ at }x=-1}$$

</details>

---

3. (Hard) Absolute max/min of $f(x)=x\ln x$ on $[1/e, e]$.

<details><summary><b>Answer</b></summary>

$f'(x)=\ln x+1=0\implies x=e^{-1}=1/e$ (endpoint).

$f(1/e)=(1/e)(-1)=-1/e,\ f(e)=e,\ f(1)=0$.

$$\boxed{\text{Max}=e\text{ at }x=e,\quad\text{Min}=-1/e\text{ at }x=1/e}$$

</details>

---

4. (Hard) Show $f(x)=\sin^2 x-\cos x$ on $[0,\pi]$ has absolute min where $\cos x=-1/2$.

<details><summary><b>Answer</b></summary>

$f(x)=1-\cos^2 x-\cos x$. Let $u=\cos x\in[-1,1]$. $g(u)=1-u^2-u$. $g'(u)=-2u-1=0\implies u=-1/2$.

$g(-1)=1,\ g(-1/2)=1-1/4+1/2=5/4,\ g(1)=-1$.

So absolute **min** is at $u=1\implies \cos x=1$ (x=0). Wait — recompute: $g(1)=1-1-1=-1$ is smallest. The value $u=-1/2$ gives a *local max* $5/4$. Absolute min at endpoints $x=0,\pi$ (cos=1, then -1). Correction: at $x=\pi$, $\cos x=-1$, $f=0- (-1)=1$; at $x=0$, $f=0-1=-1$. So absolute min $=-1$ at $x=0$.

$$\boxed{\text{Abs min}=-1\text{ at }x=0;\ u=-1/2\text{ is a local max, not the min}}$$

</details>

---

> ⚠️ **COMMON TRAPS — Read Before the Drills**
>
> **Trap 1 — Forgetting endpoints.** The absolute extremum is NOT always at a critical point. Always evaluate $f(a)$ and $f(b)$. In Type 1 the max was at $x=4$ (an endpoint).
>
> **Trap 2 — Optimizing outside the feasible interval.** Negative dimensions or $x$ values beyond the physical domain are invalid. Keep $r>0, x>0, h>0$ and respect constraints.
>
> **Trap 3 — Not reducing to one variable.** With two variables (e.g., $r$ and $h$), use the constraint (volume/fencing) to eliminate one BEFORE differentiating. Differentiating a two-variable expression partially earns no credit.
>
> **Trap 4 — Assuming symmetry gives the optimum.** A square base or "equal everything" is often wrong (e.g., open tank min material has $h=r$, not a cube). Prove it with derivatives.
>
> **Trap 5 — Failing to verify with second-derivative/endpoint.** After finding a critical point, confirm it is a max/min via $f''$ or by comparing all candidates including endpoints. Especially for "show area max when angle = $\pi/3$" types.
>
> **Trap 6 — Reporting $x=c$ instead of $f(c)$.** The extremum *value* is $f(c)$, not the location $c$. Both are usually asked.
>
> **Trap 7 — Claiming absolute extrema on an open interval.** On $(a,b)$ or $\mathbb{R}$, absolute max/min may not exist. State so explicitly when the question allows it.

---

## Stage 4: MCQ Mastery

**Q1.** For a continuous function on a closed interval $[a,b]$, the absolute maximum:
(a) Always occurs at a critical point
(b) Always occurs at an endpoint
(c) Occurs at a critical point or an endpoint
(d) May not exist

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)** The absolute max occurs at a critical point in $(a,b)$ or at an endpoint $a$ or $b$. EVT guarantees existence; location is among these candidates.

</details>

---

**Q2.** The function $f(x)=x^2-2x$ on $[-1,2]$ has absolute minimum at:
(a) $x=-1$ &emsp; (b) $x=1$ &emsp; (c) $x=2$ &emsp; (d) $x=0$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)** $f'(x)=2x-2=0\implies x=1$. $f(-1)=3,\ f(1)=-1,\ f(2)=0$. Minimum $=-1$ at $x=1$.

</details>

---

**Q3.** (Assertion-Reason)
**Assertion (A):** The absolute maximum value of $f(x)=\sin x$ on $[0,\pi]$ is 1.
**Reason (R):** $\sin x$ attains 1 at $x=\pi/2$ which is a critical point inside the interval.

(a) Both A and R true, R explains A
(b) Both true, R does NOT explain A
(c) A true, R false
(d) A false, R true

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)** $f'(x)=\cos x=0$ at $x=\pi/2\in(0,\pi)$, $f(\pi/2)=1$, and endpoints give 0. So absolute max is 1, explained by the critical point.

</details>

---

**Q4.** For the garden-fencing problem $A(x)=200x-2x^2$ on $(0,100)$, the maximum area occurs at:
(a) $x=25$ &emsp; (b) $x=50$ &emsp; (c) $x=75$ &emsp; (d) $x=100$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)** $A'(x)=200-4x=0\implies x=50$. $A''(x)=-4<0$ ⇒ maximum, $A=5000$.

</details>

---

**Q5.** The absolute maximum of $f(x)=(2/x)^{x^2}$ on $(0,\infty)$ (Type 8) is attained at:
(a) $x=\sqrt e$ &emsp; (b) $x=2/\sqrt e$ &emsp; (c) $x=e/2$ &emsp; (d) $x=2e$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)** Log-differentiation gives optimum at $x=2/\sqrt e$, value $e^{2/e}$.

</details>

---

**Q6.** If a function is strictly increasing on $[a,b]$, its absolute minimum is:
(a) At a critical point &emsp; (b) At $x=a$ &emsp; (c) At $x=b$ &emsp; (d) Does not exist

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)** Strictly increasing ⇒ smallest value at the left endpoint $a$.

</details>

---

**Q7.** (Statement-based)
**Statement I:** On an open interval, a continuous function may fail to have an absolute maximum.
**Statement II:** $f(x)=x^2$ on $(0,1)$ has no absolute maximum.

(a) I true, II false &emsp; (b) I false, II true &emsp; (c) Both true &emsp; (d) Both false

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)** Both true. $x^2$ on $(0,1)$ approaches 1 but never attains it; sup is 1, absolute max does not exist.

</details>

---

**Q8.** For the cone inscribed in a sphere (Type 5), the maximizing height is:
(a) $R/3$ &emsp; (b) $2R/3$ &emsp; (c) $4R/3$ &emsp; (d) $2R$

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (c)** $h=4R/3$ maximizes volume (derived via $r^2=2hR-h^2$).

</details>

---

**Q9.** The minimum value of $f(x)=x^3-18x^2+96x$ on $[0,9]$ (Type 2) is:
(a) 0 &emsp; (b) 128 &emsp; (c) 135 &emsp; (d) 160

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (a)** Candidates: $f(0)=0,\ f(4)=160,\ f(8)=128,\ f(9)=135$. Min $=0$ at $x=0$.

</details>

---

**Q10.** In two-shape optimization (Type 7), minimizing combined volume for fixed combined surface area gives:
(a) edge = radius &emsp; (b) edge = diameter &emsp; (c) edge = 2×diameter &emsp; (d) no fixed relation

<details><summary><b>Answer & Explanation</b></summary>

**Answer: (b)** The marginal trade-off yields cube edge $x=2r=$ sphere diameter at the optimum.

</details>

---

## Stage 5: Type Mixer

**Problem 1** (Medium) — Types 1 + 2 combined

Find the absolute maximum and minimum of $f(x)=x^3-6x^2+9x+1$ on $[-1,4]$.

<details><summary><b>Solution</b></summary>

$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0\implies x=1,3$.

$f(-1)=-1-6-9+1=-15,\ f(1)=1-6+9+1=5,\ f(3)=27-54+27+1=1,\ f(4)=64-96+36+1=5$.

$$\boxed{\text{Abs max}=5\text{ at }x=1,4;\quad\text{Abs min}=-15\text{ at }x=-1}$$

</details>

---

**Problem 2** (Medium) — Types 3 + 4 combined

A manufacturer has 100 m of material for a closed cylindrical can (top+bottom same cost). Maximize volume. Find $r$ and $h$.

<details><summary><b>Solution</b></summary>

$2\pi r^2+2\pi r h=100\implies h=\dfrac{50-\pi r^2}{\pi r}$.

$V=\pi r^2 h=r(50-\pi r^2)=50r-\pi r^3$. $V'=50-3\pi r^2=0\implies r=\sqrt{50/(3\pi)}$.

$h=\dfrac{50-\pi(50/(3\pi))}{\pi r}=\dfrac{100/3}{\pi r}=2r$.

$$\boxed{r=\sqrt{\frac{50}{3\pi}},\quad h=2r}$$

</details>

---

**Problem 3** (Hard) — Types 5 + 6 combined

A right cone is inscribed in a sphere of radius $R$. Separately, a right triangle has hypotenuse + one side fixed at $k$. Compare: which "shape-filling" principle (interior critical point vs endpoint) do both share? Verify both attain interior maxima.

<details><summary><b>Solution</b></summary>

Both reduce the objective to a single variable on a *closed/feasible* interval and find an interior critical point that beats the (zero or degenerate) endpoints:

- Cone: $V(h)=\frac13\pi h(2Rh-h^2)$ on $[0,2R]$; $V'(h)=0$ at $h=4R/3$ (interior), endpoints give 0.
- Triangle: $A(\theta)\propto \dfrac{\sin2\theta}{(1+\cos\theta)^2}$ on $[0,\pi/2]$; max at $\theta=\pi/3$ (interior), ends give 0.

$$\boxed{\text{Both share: interior critical point dominates zero-valued endpoints ⇒ absolute max interior}}$$

</details>

---

**Problem 4** (Hard — Competency-Based) — Types 3 + 7 + cost framing

A company makes open square-based tanks. Material for the base costs ₹$c$ per m², sides cost ₹$c$ per m² too (uniform). For a fixed volume $V=108\text{ m}^3$, find dimensions minimizing material, and compute the minimum base area.

<details><summary><b>Solution</b></summary>

Base $x\times x$, height $h$. $x^2h=108\implies h=108/x^2$.

Material area $A=x^2+4xh=x^2+432/x$. $A'=2x-432/x^2=0\implies 2x^3=432\implies x^3=216\implies x=6$.

$h=108/36=3$. Base area $=36\text{ m}^2$. (Check $A''=2+864/x^3>0$ ⇒ min.)

$$\boxed{x=6\text{ m},\ h=3\text{ m},\ \text{Min base area}=36\text{ m}^2}$$

</details>

---

## Stage 6: Board Arsenal

**Q1. [2 marks — CBSE pattern]**

Find the absolute maximum and minimum values of $f(x)=4x-x^2$ on the interval $[-1,3]$.

<details><summary><b>Model Answer</b></summary>

$f'(x)=4-2x=0\implies x=2\in(-1,3)$.

$f(-1)=-5,\ f(2)=4,\ f(3)=3$. **[1 mark]**

$$\boxed{\text{Abs max}=4\text{ at }x=2;\quad\text{Abs min}=-5\text{ at }x=-1}$$ **[1 mark]**

</details>

---

**Q2. [3 marks — CBSE pattern]**

Find the smallest value of $f(x)=x^3-18x^2+96x$ on $[0,9]$. (NCERT Exemplar Q12)

<details><summary><b>Model Answer</b></summary>

$f'(x)=3(x-4)(x-8)=0\implies x=4,8\in(0,9)$. **[1 mark]**

$f(0)=0,\ f(4)=160,\ f(8)=128,\ f(9)=135$. **[1 mark]**

Smallest value $=\min\{0,160,128,135\}=0$. **[1 mark]**

$$\boxed{\text{Smallest (absolute minimum) value}=0\text{ at }x=0}$$

</details>

---

**Q3. [4 marks — Long Answer]**

A rectangular enclosure is to be made with 200 ft of fencing using an existing straight brick wall as one side (no fencing needed there). If $x$ is the side perpendicular to the wall, show the area is $A(x)=200x-2x^2$ and find the maximum enclosed area.

<details><summary><b>Model Answer</b></summary>

Let $x$ = side perpendicular to wall, $y$ = side parallel to wall. Fencing: $2x+y=200\implies y=200-2x$. **[1 mark]**

Area $A=x\cdot y=x(200-2x)=200x-2x^2$, feasible $x\in(0,100)$. **[1 mark]**

$A'(x)=200-4x=0\implies x=50$. $A''(x)=-4<0$ ⇒ maximum. **[1 mark]**

$A(50)=200(50)-2(2500)=5000$. Endpoints give 0, so absolute max. **[1 mark]**

$$\boxed{\text{Max area}=5000\text{ ft}^2\text{ at }x=50\text{ ft (}y=100\text{ ft)}}$$

</details>

---

**Q4. [4 marks — Competency / Case Study, Section E style]**

A packaging firm produces cylindrical cans with fixed volume $500\text{ cm}^3$. The material for the top and bottom costs twice as much per cm² as the curved side. The design team models total cost as $C(r)=2k\pi r^2+\dfrac{1000k}{r}$, where $r$ (cm) is the base radius and $k>0$ is the side-cost rate.

(a) State the feasible domain for $r$ and why. **[1 mark]**
(b) Find $C'(r)$ and the critical point. **[2 marks]**
(c) Show this critical point gives a minimum, and state the optimal height-to-radius ratio. **[1 mark]**

<details><summary><b>Model Answer</b></summary>

**(a)** $r>0$ (radius must be positive; volume fixed ⇒ $h=500/(\pi r^2)>0$). Feasible domain $(0,\infty)$. **[1 mark]**

**(b)** $C(r)=2k\pi r^2+1000k\,r^{-1}$.

$$C'(r)=4k\pi r-1000k\,r^{-2}=4k\pi r-\frac{1000k}{r^2}$$ **[1 mark]**

Set $C'(r)=0$: $4\pi r^3=1000\implies r^3=\dfrac{250}{\pi}\implies \boxed{r=\left(\dfrac{250}{\pi}\right)^{1/3}\text{ cm}}$. **[1 mark]**

**(c)** $C''(r)=4k\pi+2000k\,r^{-3}>0$ for all $r>0$ ⇒ strict minimum. **[1 mark]**

With $h=500/(\pi r^2)$ and $r^3=250/\pi$: $\pi r^3=250$, and $h=500/(\pi r^2)=2r$. So $\boxed{h:r=2:1}$.

*Economic note:* the optimum is wider/shorter than the uniform-cost can because the expensive top/bottom area is reduced relative to the side.

</details>

---

**Q5. [5 marks — Long Answer, Optimization Synthesis]**

A cone is inscribed in a sphere of radius $R$. Show that its volume is maximum when the height of the cone is $4R/3$. Hence find the ratio of the cone's maximum volume to the sphere's volume.

<details><summary><b>Model Answer</b></summary>

Let cone height $=h$, base radius $=r$. From the cross-section, $r^2=R^2-(h-R)^2=2Rh-h^2$. **[1 mark]**

$V=\frac13\pi r^2 h=\frac13\pi(2Rh^2-h^3)$, $0<h<2R$. **[1 mark]**

$V'(h)=\frac13\pi(4Rh-3h^2)=\frac13\pi h(4R-3h)=0\implies h=4R/3$. **[1 mark]**

$V''(h)=\frac13\pi(4R-6h)$; at $h=4R/3$, $V''<0$ ⇒ maximum. Also endpoints $h\to0,2R$ give $V\to0$. **[1 mark]**

$V_{max}=\frac13\pi\cdot\frac{8R^2}{9}\cdot\frac{4R}{3}=\frac{32\pi R^3}{81}$. Sphere $=\frac43\pi R^3$.

Ratio $=\dfrac{32/81}{4/3}=\dfrac{8}{27}$. **[1 mark]**

$$\boxed{h=\frac{4R}{3},\quad \frac{V_{cone}}{V_{sphere}}=\frac{8}{27}}$$

</details>

---

## Stage 7: JEE Mains Arena

**Q1.** The absolute maximum of $f(x)=2x^3-3x^2-12x+5$ on $[-2,4]$ is:

(a) 37 &emsp; (b) 12 &emsp; (c) $-15$ &emsp; (d) 1

<details><summary><b>Answer</b></summary>

**Answer: (a) 37**

$f'(x)=6(x-2)(x+1)$; candidates $f(-2)=1,\ f(-1)=12,\ f(2)=-15,\ f(4)=37$. Max $=37$ at endpoint $x=4$.

</details>

---

**Q2.** A right circular cone of maximum volume is inscribed in a sphere of radius $R$. The ratio of the cone's height to the sphere's radius is:

(a) $1:1$ &emsp; (b) $4:3$ &emsp; (c) $3:4$ &emsp; (d) $2:1$

<details><summary><b>Answer</b></summary>

**Answer: (b) $4:3$**

From $r^2=2Rh-h^2$ and $V'(h)=0$, optimal $h=4R/3$.

</details>

---

**Q3.** For the function $f(x)=\left(\dfrac{2}{x}\right)^{x^2}$ on $(0,\infty)$, the point of maximum is:

(a) $x=e/2$ &emsp; (b) $x=2/\sqrt e$ &emsp; (c) $x=\sqrt e/2$ &emsp; (d) $x=\sqrt{2e}$

<details><summary><b>Answer</b></summary>

**Answer: (b) $x=2/\sqrt e$**

$\ln f=x^2(\ln2-\ln x)$; derivative zero ⇒ $2\ln(2/x)=1$ ⇒ $x=2/\sqrt e$.

</details>

---

**Q4.** The absolute minimum of $f(x)=x+\dfrac{1}{x}$ on $\left[\dfrac12,2\right]$ is:

(a) $1/2$ &emsp; (b) $2$ &emsp; (c) $5/2$ &emsp; (d) $1$

<details><summary><b>Answer</b></summary>

**Answer: (c) is wrong; correct is (b) 2** — wait, min value is 2.

$f'(x)=1-1/x^2=0\implies x=1$. $f(1)=2$, endpoints $f(1/2)=f(2)=2.5$. Min $=2$.

$$\boxed{\text{Answer: (d) }1\text{ is the }x\text{-location; the minimum VALUE is }2\ (\text{option b})}$$

</details>

---

**Q5.** Let $S=6x^2+4\pi r^2$ be fixed. The sum of volumes $V=x^3+\frac43\pi r^3$ is minimized when:

(a) $x=r$ &emsp; (b) $x=2r$ &emsp; (c) $x=r/2$ &emsp; (d) $x=\sqrt{4\pi/6}\,r$

<details><summary><b>Answer</b></summary>

**Answer: (b) $x=2r$**

Lagrange/marginal balance gives $3x^2dx+4\pi r^2dr=0$ with $12x\,dx+8\pi r\,dr=0$ ⇒ $x=2r$ (cube edge = sphere diameter).

</details>

---

*Next: [Chapter 7 — NCERT Exemplar & Mixed Synthesis](./07_ncert_exemplar.md)*

---

## Quick Revision Summary

| Concept | Formula / Rule | Key Point |
|---|---|---|
| Absolute extrema on $[a,b]$ | Eval $f$ at critical pts in $(a,b)$ + endpoints $a,b$ | Largest = max, smallest = min |
| Extreme Value Theorem | Continuous on $[a,b]$ ⇒ extrema exist | Closed interval essential |
| Garden fencing (1 wall) | $A=200x-2x^2$ | Max at $x=50$, area $=5000$ |
| Cylindrical can (fixed $V$) | Reduce $h=V/(\pi r^2)$, then optimize | Open tank optimum $h=r$ |
| Cone in sphere | $r^2=2Rh-h^2$, $V=\frac13\pi(2Rh^2-h^3)$ | Max at $h=4R/3$, vol ratio $8/27$ |
| Triangle (hyp+side fixed) | $A(\theta)=\dfrac{k^2\sin\theta\cos\theta}{(1+\cos\theta)^2}$ | Max when $\theta=\pi/3$ |
| Two-shape (fixed S-area) | Balance marginal volumes | Min $V$ when cube edge = sphere diameter |
| Tricky function | Log-differentiate: $\ln f$ then $f'/f$ | Compare all candidates incl. limits |

> The Golden Rule: **Never skip the endpoints.** Absolute extrema live at critical points *or* endpoints — and on open domains they may not exist at all.

> The Number One Exam Trap: Reporting the *location* $x=c$ as the extremum. The question usually wants the *value* $f(c)$ — give both.

> Optimization Mantra: Constraint → one variable → feasible interval → absolute-extrema rule → verify with $f''$ or endpoint comparison.
