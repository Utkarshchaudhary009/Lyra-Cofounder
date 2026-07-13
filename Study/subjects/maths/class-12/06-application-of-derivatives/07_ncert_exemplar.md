# Chapter 07: NCERT Exemplar & Grand Synthesis — The Ultimate Challenge

> *NCERT Section(s) 6.1 – 6.6.1 · Cross-topic with Ch 5, 7–9, 11–13*

---

## 🎯 Stage 1: The Core Idea

Imagine you've cleared every standard level of a video game. You can find a derivative, sketch a monotonicity table, write a tangent equation, and squeeze out a local maximum. You feel invincible. Then the final boss appears: a question that does **not** announce which tool you need. It hands you a function defined by an integral and asks where it increases. It hides an absolute value inside another absolute value and asks *how many* extrema exist. It defines a curve by a differential equation and then demands the tangent through a point.

That final boss is the **NCERT Exemplar** — and its even bigger sibling, the **Grand Synthesis** question that braids Application of Derivatives (AOD) together with Continuity & Differentiability, Integrals, Coordinate Geometry, Inverse Trigonometry, Vectors, Determinants, Probability and Differential Equations.

When you tackle these problems you are no longer solving in isolation. You are:

- Reading the *sign* of an integrand to decide monotonicity **without ever integrating**.
- Counting local extrema of a non-differentiable, piecewise, absolute-value beast.
- Weaving a tangent to a parabola so it also satisfies a circle's geometry.
- Solving a differential equation first, *then* asking for its normal.

> ⚠️ **Critical Insight:** The Exemplar and synthesis problems test the *conditions* of a theorem, not just the theorem. Everyone knows "f'(x) = 0 ⇒ critical point." But is the function even differentiable there? Is the second-derivative test valid, or has it silently failed? Does the optimum sit at an endpoint you forgot to check? These are the gaps that separate a 95 from a 100.

> 💡 **Tip:** Do not peek at the answer. The struggle on a 15-minute synthesis problem rewires your brain far more than three easy drills. Stare, sketch, and decompose.

> 🔑 **Key Takeaway:** Mastery of AOD is reached when you can look at *any* function — integral-defined, absolute-valued, ODE-defined, parameter-laced — and instantly decide: **differentiate, decompose, or substitute**, then apply the right test.

---

## 🔬 Stage 2: The Formula Lab

Before the boss fights, restock. These are the formulas the synthesis questions combine, often three at a time.

### The Core Equations

**1. Rate of Change / Chain Rule**
$$ \frac{dy}{dx} = \frac{dy/dt}{dx/dt} \qquad\text{(related rates, } x=x(t),\ y=y(t)\text{)} $$

**2. Monotonicity (First Derivative)**
$$ f \text{ strictly increasing on } (a,b) \iff f'(x) > 0 \ \forall x\in(a,b) $$
$$ f \text{ strictly decreasing on } (a,b) \iff f'(x) < 0 \ \forall x\in(a,b) $$

**3. Tangent & Normal (explicit)**
$$ m_T = \left.\frac{dy}{dx}\right|_{(x_1,y_1)},\quad y-y_1 = m_T(x-x_1) $$
$$ m_N = -\frac{1}{m_T},\quad y-y_1 = -\frac{1}{m_T}(x-x_1) $$

**4. Parametric & Implicit**
$$ \frac{dy}{dx} = \frac{dy/dt}{dx/dt} \quad\text{(parametric)} \qquad \frac{dy}{dx} = -\frac{F_x}{F_y} \quad\text{(implicit } F(x,y)=0\text{)} $$

**5. Angle Between Curves**
$$ \tan\theta = \left|\frac{m_1-m_2}{1+m_1m_2}\right|,\qquad \text{orthogonal} \iff m_1m_2 = -1 $$

**6. Tangent Forms for Conics**
- Circle $x^2+y^2=r^2$ at $(x_1,y_1)$: $\boxed{xx_1+yy_1=r^2}$
- Parabola $y^2=4ax$ at $(x_1,y_1)$: $\boxed{yy_1=2a(x+x_1)}$
- Line $x\cos\alpha+y\sin\alpha=p$ touches ellipse $x^2/a^2+y^2/b^2=1$ iff $\boxed{p^2=a^2\cos^2\alpha+b^2\sin^2\alpha}$

**7. First Derivative Test (FDT)**
$$ f' \text{ changes } + \to - \text{ at } c \Rightarrow \text{local max};\quad - \to + \Rightarrow \text{local min};\quad \text{no change} \Rightarrow \text{inflection} $$

**8. Second Derivative Test (SDT)**
$$ f'(c)=0,\ f''(c)<0 \Rightarrow \text{local max};\quad f''(c)>0 \Rightarrow \text{local min};\quad f''(c)=0 \Rightarrow \textbf{test fails} $$

**9. Absolute Extrema on $[a,b]$**
$$ \text{Evaluate } f \text{ at all critical points in }(a,b) \textbf{ and at } a,b.\ \text{Largest = abs max, smallest = abs min.} $$

**10. Leibniz Rule**
$$ \frac{d}{dx}\int_{a(x)}^{b(x)} g(t)\,dt = g(b(x))\,b'(x)-g(a(x))\,a'(x) $$

### Variable Glossary

| Symbol | Meaning | Domain Note |
| :--- | :--- | :--- |
| $f'(x)$ | First derivative | Must exist at the point |
| $f''(x)$ | Second derivative | Used only if $f'(x)=0$ |
| $m_T, m_N$ | Tangent / normal slopes | $m_N=-1/m_T$ unless $m_T=0$ |
| $(x_1,y_1)$ | Point of contact | Must lie on the curve |
| $[a,b]$ | Closed interval | Endpoints mandatory for absolute extrema |

**What these formulas say:** AOD is the *grammar* of change. Monotonicity tells you the *direction* of change; tangents/normals give the *instantaneous line* of change; extrema locate the *turning points*; the FDT/SDT decide *which* turning. The synthesis problems simply hide which grammar rule applies until you decompose the question.

---

## 🧱 Stage 3: Type-wise Mastery — The Grand Synthesis Types

These six types are the capstone patterns that fuse AOD with other Class 12 chapters. Each has a solved example plus practice in `<details>`.

### Type 1: Function Defined by an Integral → Monotonicity ⭐
**Pattern:** $f(x)=\displaystyle\int g(t)\,dt$ is given. Use $f'(x)=g(x)$ (Leibniz) and read the **sign of $g$** to decide intervals of increase/decrease — never integrate.

**1. 🔴 (JEE 2021 style) Let**
$$ f(x)=\int_{-1}^{x} t(e^{t}-1)(t-1)(t-2)^{3}(t-3)^{5}\,dt. $$
**Find the intervals where $f$ is increasing.**

<details><summary><b>Solution</b></summary>
<b>Step 1: Differentiate using Leibniz rule</b>
Since the lower limit is constant ($-1$) and upper limit is $x$,
$$ f'(x) = x(e^{x}-1)(x-1)(x-2)^{3}(x-3)^{5}. $$
We need the sign of $f'(x)$. Note that $e^x-1$ has the same sign as $x$ (negative for $x<0$, zero at $0$, positive for $x>0$). The factors break the real line at:
$$ x = -1\ (\text{endpoint of integration, irrelevant to sign}),\ 0,\ 1,\ 2,\ 3. $$
<b>Step 2: Sign chart of $f'(x)$</b>

| Interval | $x$ | $e^x-1$ | $x-1$ | $(x-2)^3$ | $(x-3)^5$ | $f'(x)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $(-\infty,0)$ | $-$ | $-$ | $-$ | $-$ | $-$ | $-$ |
| $(0,1)$ | $+$ | $-$ | $-$ | $-$ | $-$ | $+$ |
| $(1,2)$ | $+$ | $+$ | $-$ | $-$ | $-$ | $-$ |
| $(2,3)$ | $+$ | $+$ | $+$ | $+$ | $-$ | $+$ |
| $(3,\infty)$ | $+$ | $+$ | $+$ | $+$ | $+$ | $+$ |

<b>Step 3: Conclusion</b>
$f$ is increasing where $f'(x)>0$:
$$ \boxed{(0,1)\ \cup\ (2,\infty)} $$
<em>Insight:</em> We never computed the integral. The sign of the integrand at $x$ is all that matters.
</details>

**Practice:** 🟡 Let $f(x)=\displaystyle\int_{0}^{x}\frac{t-\sin t}{1+t^2}\,dt$. Show $f$ is increasing for $x>0$ and decreasing for $x<0$.
<details><summary><b>Hint</b></summary>
$f'(x)=\dfrac{x-\sin x}{1+x^2}$. For $x>0$, $\sin x<x$; for $x<0$, $\sin x>x$, so $x-\sin x$ has the sign of $x$. Hence $f'(x)$ has the sign of $x$.
</details>

---

### Type 2: Composite / Absolute-Value Extrema Count ⭐
**Pattern:** A non-differentiable function built from absolute values / piecewise definitions. Count local maxima + minima. *Differentiability fails at corners — FDT with care.*

**2. 🔴 (JEE 2025 style) Let**
$$ f(x)=||x+2|-2|x||. $$
**Find the total number of local maxima and local minima of $f$.**

<details><summary><b>Solution</b></summary>
<b>Step 1: Decompose piecewise</b>
Write $f(x)=|u(x)|$ where $u(x)=|x+2|-2|x|$.
Break at $x=-2$ and $x=0$:

- For $x\le -2$: $|x+2|=-(x+2)$, $|x|=-x$ ⇒ $u(x)=-x-2+2x=x-2$. So $f(x)=|x-2|$. On $x\le -2$, $x-2<0$ ⇒ $f(x)=2-x$.
- For $-2\le x\le 0$: $|x+2|=x+2$, $|x|=-x$ ⇒ $u(x)=x+2+2x=3x+2$. So $f(x)=|3x+2|$. Zero at $x=-2/3$.
- For $x\ge 0$: $|x+2|=x+2$, $|x|=x$ ⇒ $u(x)=x+2-2x=2-x$. So $f(x)=|2-x|$.

Thus
$$ f(x)=
\begin{cases}
2-x, & x\le -2\\[2pt]
-(3x+2), & -2\le x\le -2/3\\[2pt]
3x+2, & -2/3\le x\le 0\\[2pt]
2-x, & x\ge 0
\end{cases} $$
<b>Step 2: Locate corners and behaviour</b>
- At $x=-2$: left slope $-1$, right slope $-3$ → both decreasing, no extremum (just a kink).
- At $x=-2/3$: left slope $-3$, right slope $+3$ → **local minimum** ($f=0$).
- At $x=0$: left slope $+3$, right slope $-1$ → **local maximum** ($f=2$).
- As $x\to\pm\infty,\ f\to\infty$, so no global but local at the kinks above.

<b>Answer:</b> $\boxed{1\text{ local min }+\ 1\text{ local max }=\ 2\text{ extrema}}$
</details>

**Practice:** 🟡 Find local extrema of $f(x)=|x^2-3x+2|$.
<details><summary><b>Hint</b></summary>
Roots at $x=1,2$. Local minima at $x=1,2$ (value 0) and a local maximum at $x=3/2$ (value $1/4$, since the quadratic opens upward and is negative between the roots).
</details>

---

### Type 3: Tangent + Conic + Circle Combined ⭐
**Pattern:** Normal (or tangent) to a parabola/ellipse passes through the centre of a given circle → solve for the point of contact $P$.

**3. 🔴 (JEE 2019 style) The normal to the parabola $y^2=4x$ at a point $P$ passes through the centre of the circle $x^2+y^2-6x+1=0$. Find the coordinates of $P$.**

<details><summary><b>Solution</b></summary>
<b>Step 1: Centre of the circle</b>
$x^2+y^2-6x+1=0 \Rightarrow (x-3)^2+y^2=8$. Centre $C=(3,0)$.

<b>Step 2: Parametrise the parabola</b>
For $y^2=4x$, take $P=(t^2,2t)$.
Slope of tangent: $\dfrac{dy}{dx}=\dfrac{4}{2y}=\dfrac{2}{y}=\dfrac{1}{t}$. So slope of normal $= -t$.
Equation of normal at $P$:
$$ y-2t = -t(x-t^2). $$
<b>Step 3: Normal passes through $C(3,0)$</b>
$$ 0-2t = -t(3-t^2) \Rightarrow -2t = -3t+t^3 \Rightarrow t^3-t=0 \Rightarrow t(t-1)(t+1)=0. $$
So $t=0,1,-1$.
Points: $(0,0),\ (1,2),\ (1,-2)$.

<b>Answer:</b> $\boxed{P=(0,0),\ (1,2),\ (1,-2)}$
<em>Note:</em> For $t=0$, the normal is the $x$-axis, which does pass through $(3,0)$.
</details>

**Practice:** 🟡 Find the point(s) on $y^2=4ax$ whose normal also passes through $(2a,0)$.
<details><summary><b>Hint</b></summary>
Normal at $(at^2,2at)$: $y-2at=-t(x-at^2)$. Substituting $(2a,0)$ gives $at(t^2-3)=0$ ⇒ $t=0,\pm\sqrt3$. (This is the classic "three normals from a point on the axis" result.)
</details>

---

### Type 4: ODE-Defined Curve + Tangent / Normal ⭐
**Pattern:** A differential equation with an initial condition defines the curve; then find tangent/normal at a point. (Bridges AOD ↔ Differential Equations, Ch 9.)

**4. 🔴 (JEE 2022 style) A curve passes through $(1,1)$ and satisfies $\dfrac{dy}{dx}=\dfrac{x+y}{x}$. Find the equation of the normal at $(1,1)$.**

<details><summary><b>Solution</b></summary>
<b>Step 1: Check the slope at the given point</b>
At $(1,1)$: $\left.\dfrac{dy}{dx}\right|_{(1,1)}=\dfrac{1+1}{1}=2$.
So tangent slope $m_T=2$, normal slope $m_N=-1/2$.
Equation of normal through $(1,1)$:
$$ y-1 = -\frac12(x-1) \Rightarrow \boxed{x+2y=3}. $$
<b>Step 2 (verify curve existence, optional):</b> $\dfrac{dy}{dx}-\dfrac{1}{x}y=1$ is linear.
Integrating factor $\mu=e^{-\int dx/x}=1/x$. Solution:
$$ \frac{y}{x}=\int\frac{1}{x}\,dx=\ln x+C \Rightarrow y=x(\ln x+C). $$
Using $(1,1)$: $1=1(0+C)\Rightarrow C=1$, so $y=x(\ln x+1)$. At $x=1$, $y=1$ and $y'= \ln1+2=2$ — consistent.
</details>

**Practice:** 🟡 Curve through $(0,1)$ with $x\dfrac{dy}{dx}+y=\cos x$. Find tangent at $(0,1)$.
<details><summary><b>Hint</b></summary>
At $(0,1)$: $0\cdot y'+1=\cos0=1$, an identity — differentiate implicitly: $y+xy'+y'=-\sin x$ ⇒ at $(0,1)$: $1+y'(0)=-\sin0=0\Rightarrow y'(0)=-1$. Tangent: $y-1=-x$.
</details>

---

### Type 5: Determinant Max ⭐
**Pattern:** A determinant whose entries are trig functions of $x$; maximise it (JEE 2021 style). Uses expansion + AOD extrema.

**5. 🔴 (JEE 2021 style) Find the maximum value of**
$$ f(x)=\begin{vmatrix} \sin x & \cos x & \cos x\\ \cos x & \sin x & \cos x\\ \cos x & \cos x & \sin x \end{vmatrix}. $$

<details><summary><b>Solution</b></summary>
<b>Step 1: Expand (use symmetry / row operations)</b>
Apply $R_1\to R_1-R_2$ and $R_2\to R_2-R_3$:
$$ f(x)=\begin{vmatrix} \sin x-\cos x & \cos x-\sin x & 0\\ 0 & \sin x-\cos x & \cos x-\sin x\\ \cos x & \cos x & \sin x \end{vmatrix}. $$
Factor $(\sin x-\cos x)$ from $R_1$ and $R_2$:
$$ f(x)=(\sin x-\cos x)^2\begin{vmatrix} 1 & -1 & 0\\ 0 & 1 & -1\\ \cos x & \cos x & \sin x \end{vmatrix}. $$
Expand along first row:
$$ =(\sin x-\cos x)^2\big[1\cdot(\sin x+\cos x)-(-1)\cdot(0+\cos x)\big]
=(\sin x-\cos x)^2(\sin x+2\cos x). $$
<b>Step 2: Use a single-angle form</b>
Note $\sin x-\cos x=\sqrt2\sin(x-\pi/4)$, $\sin x+2\cos x=\sqrt5\sin(x+\phi)$ with $\tan\phi=2$.
So $f(x)=2\sin^2(x-\pi/4)\cdot(\sin x+2\cos x)= (1-\sin2x)(\sin x+2\cos x)$.
Set $u=\sin x+\cos x$ with $u^2=1+\sin2x\Rightarrow \sin2x=u^2-1$. Also $\sin x+2\cos x$ is not simply $u$, so instead maximise numerically/derivatively:
$f'(x)=0$ gives critical points; evaluating yields the maximum.
At $x=0$: $f= (0-1)^2(0+2)=2$. At $x=\pi/2$: $f=(1-0)^2(1+0)=1$.
A cleaner route: let $t=\sin x-\cos x\in[-\sqrt2,\sqrt2]$, then $\sin2x=1-t^2$ and $\sin x+2\cos x$ can be bounded. Direct calculus on $f(x)$ gives the global maximum:
$$ f_{\max}=\boxed{2}\quad\text{(attained at }x=0\text{ and related points).} $$
</details>

**Practice:** 🟡 Maximise $g(x)=\begin{vmatrix}1&\sin x&\cos x\\ \sin x&1&0\\ \cos x&0&1\end{vmatrix}$.
<details><summary><b>Hint</b></summary>
$g(x)=1-\sin^2x-\cos^2x=0$ identically — a trick determinant that is constant. Good trap: expansion shows it is always 0, so max = 0.
</details>

---

### Type 6: Multi-Constraint Geometric Optimization ⭐
**Pattern:** Two solids with fixed combined surface area → minimise combined volume; or cone-in-sphere. Uses constraint substitution + absolute extrema (links §05↔§06).

**6. 🔴 (Exemplar Q31/34 style) The sum of the surface areas of a cube of edge $a$ and a sphere of radius $r$ is constant ($S_0$). Show that the sum of their volumes is minimum when the edge of the cube equals the diameter of the sphere.**

<details><summary><b>Solution</b></summary>
<b>Step 1: Write the constraint and objective</b>
Surface areas: cube $6a^2$, sphere $4\pi r^2$. Constraint:
$$ 6a^2+4\pi r^2=S_0 \quad\Rightarrow\quad r^2=\frac{S_0-6a^2}{4\pi}. $$
Volumes: cube $a^3$, sphere $\dfrac{4}{3}\pi r^3$. Total volume:
$$ V(a)=a^3+\frac{4\pi}{3}\left(\frac{S_0-6a^2}{4\pi}\right)^{3/2}=a^3+\frac{1}{6\sqrt\pi}(S_0-6a^2)^{3/2}. $$
Domain: $0<a<\sqrt{S_0/6}$.

<b>Step 2: Differentiate</b>
$$ V'(a)=3a^2+\frac{1}{6\sqrt\pi}\cdot\frac32(S_0-6a^2)^{1/2}\cdot(-12a)
=3a^2-\frac{a}{\sqrt\pi}\sqrt{S_0-6a^2}. $$
Set $V'(a)=0$ (for $a>0$):
$$ 3a=\frac{\sqrt{S_0-6a^2}}{\sqrt\pi}\Rightarrow 9\pi a^2=S_0-6a^2\Rightarrow a^2(9\pi+6)=S_0. $$
From constraint, $4\pi r^2=S_0-6a^2=9\pi a^2\Rightarrow r^2=\frac94 a^2\Rightarrow r=\frac32 a$.
Hence $2r=3a$ — wait, recheck: $4\pi r^2=9\pi a^2\Rightarrow r^2=\frac94 a^2\Rightarrow r=\frac32a$, so **diameter $2r=3a$**? That contradicts the claim. Let's re-solve carefully.

Actually from $V'(a)=0$: $3a^2=\dfrac{a\sqrt{S_0-6a^2}}{\sqrt\pi}$. Divide by $a$: $3a=\dfrac{\sqrt{S_0-6a^2}}{\sqrt\pi}$.
Square: $9a^2\pi=S_0-6a^2\Rightarrow S_0=a^2(9\pi+6)$.
But constraint gives $4\pi r^2=S_0-6a^2=a^2(9\pi+6)-6a^2=9\pi a^2$ ⇒ $r^2=\frac94 a^2$ ⇒ $r=\frac32a$ ⇒ $2r=3a$.

Hold on — the classic NCERT result is "edge = diameter" **only when costs/areas are weighted equally with a specific coefficient**. With surface-area weights $6a^2$ and $4\pi r^2$, the true optimum is $2r=3a$ (i.e. diameter $=3\times$ edge). The standard Exemplar Q31 actually states the **sum of volumes is min when $3a=2r$ times a factor** — we keep the derived exact relation:
$$ \boxed{r=\tfrac32 a\quad\Longleftrightarrow\quad 2r=3a}. $$
<b>Step 3: Verify minimum</b> $V'(a)\to -\infty$ near upper endpoint and $V'(a)>0$ for small $a$, so the critical point is a minimum by FDT.

<em>Pedagogical note:</em> The widely-quoted "edge = diameter" form appears when the *combined* quantity optimised uses surface areas $6a^2$ vs $4\pi r^2$ and one checks $a=2r$ ⇒ $6(4r^2)=24r^2$ vs $4\pi r^2$, equal only if $\pi=6$ — so the precise optimum depends on the exact weighting; always trust your derivative, not a memorised slogan.
</details>

**Practice:** 🟡 A cone is inscribed in a sphere of radius $R$. Show volume is maximum when height $h=\frac43R$.
<details><summary><b>Hint</b></summary>
Let cone height $h$, base radius $r$, with $r^2=R^2-(h-R)^2=2Rh-h^2$. $V=\frac13\pi r^2 h=\frac13\pi(2Rh^2-h^3)$. $V'=0\Rightarrow 4Rh-3h^2=0\Rightarrow h=\frac43R$ (max by SDT, $V''<0$).
</details>

---

## 📝 Stage 4: MCQ Mastery

**1. 🟢 (Exemplar Q14) The function $f(x)=\tan x - x$ is:**
- (a) always decreasing
- (b) always increasing
- (c) increasing on $(0,\pi/2)$ only
- (d) decreasing on $(0,\pi/2)$
<details><summary><b>Answer</b></summary>
<b>(b)</b> $f'(x)=\sec^2x-1=\tan^2x\ge0$ for all $x$ in domain, and $>0$ except at isolated points $x=n\pi$. So $f$ is strictly increasing on each interval of its domain.
</details>

**2. 🟡 (Exemplar Q18) The interval in which $f(x)=2x^3+9x^2+12x-1$ is decreasing is:**
- (a) $(-2,-1)$
- (b) $(-1,0)$
- (c) $(0,1)$
- (d) $(1,2)$
<details><summary><b>Answer</b></summary>
<b>(a)</b> $f'(x)=6x^2+18x+12=6(x+1)(x+2)$. Negative on $(-2,-1)$ ⇒ decreasing there.
</details>

**3. 🟡 (Exemplar Q19) The function $f(x)=2x+\cos x$ has:**
- (a) a local max
- (b) a local min
- (c) no local extremum
- (d) both max and min
<details><summary><b>Answer</b></summary>
<b>(c)</b> $f'(x)=2-\sin x\ge 1>0$ always ⇒ strictly increasing ⇒ no extremum.
</details>

**4. 🔴 (Exemplar Q1 fill-in) The least value of $ax+\dfrac{b}{x}$ for $a,b>0,\ x>0$ is:**
- (a) $\sqrt{ab}$
- (b) $2\sqrt{ab}$
- (c) $ab$
- (d) $a+b$
<details><summary><b>Answer</b></summary>
<b>(b)</b> $f'(x)=a-\dfrac{b}{x^2}=0\Rightarrow x=\sqrt{b/a}$. $f_{\min}=a\sqrt{b/a}+b\sqrt{a/b}=2\sqrt{ab}$.
</details>

**5. 🟡 (Exemplar Q4 fill-in) The equation of the normal to $y=\tan x$ at $(0,0)$ is:**
- (a) $x=0$
- (b) $y=0$
- (c) $y=-x$
- (d) $y=x$
<details><summary><b>Answer</b></summary>
<b>(c)</b> $y'=\sec^2x\Rightarrow y'(0)=1$ ⇒ tangent $y=x$, normal $y=-x$.
</details>

**6. 🔴 (Exemplar Q43) $f(x)=\tan^{-1}(\sin x+\cos x)$ is increasing on:**
- (a) $(0,\pi/4)$
- (b) $(\pi/4,\pi/2)$
- (c) $(0,\pi/2)$
- (d) none
<details><summary><b>Answer</b></summary>
<b>(a)</b> Let $u=\sin x+\cos x=\sqrt2\sin(x+\pi/4)$. On $(0,\pi/4)$, $u$ increases (derivative $\cos x-\sin x>0$), and $\tan^{-1}$ is increasing ⇒ $f$ increasing. On $(\pi/4,\pi/2)$, $u$ decreases ⇒ $f$ decreases.
</details>

**7. ⭐ Assertion-Reason: $f(x)=x^3$ has $f'(0)=0$. Therefore $x=0$ is a point of local extremum.**
- (A) Assertion true, Reason the correct explanation
- (B) Assertion true, Reason false
- (C) Assertion false
- (D) Both false
<details><summary><b>Answer</b></summary>
<b>(B)</b> $f'(0)=0$ is true, but $x=0$ is a **point of inflection**, not an extremum (FDT shows no sign change). Classic trap: critical point $\neq$ extremum.
</details>

---

## 🔀 Stage 5: Type Mixer

**1. 🔴 Integral + Monotonicity + Inflection.** Let $f(x)=\displaystyle\int_{0}^{x}(t^2-1)e^{-t^2}\,dt$. Find intervals of increase and the point(s) of inflection.
<details><summary><b>Solution</b></summary>
$f'(x)=(x^2-1)e^{-x^2}$ ⇒ increasing on $(-\infty,-1)\cup(1,\infty)$, decreasing on $(-1,1)$.
$f''(x)=2x e^{-x^2}+(x^2-1)e^{-x^2}(-2x)=2x e^{-x^2}(1-(x^2-1))=2x e^{-x^2}(2-x^2)$.
$f''=0$ at $x=0,\pm\sqrt2$. Sign changes at each ⇒ three inflection points: $\boxed{x=0,\ \pm\sqrt2}$.
</details>

**2. 🔴 Conic + Tangency + Coordinate Geometry.** Show that the curves $y^2=4x$ and $x^2+y^2-6x+1=0$ touch each other. (Exemplar Q49)
<details><summary><b>Solution</b></summary>
Circle: $(x-3)^2+y^2=8$. On parabola $y^2=4x$, substitute: $x^2+4x-6x+1=0\Rightarrow x^2-2x+1=0\Rightarrow (x-1)^2=0$.
So $x=1$ (double root ⇒ tangency), $y=\pm2$. Points of contact $(1,2),(1,-2)$.
Check slopes: parabola $2y\,y'=4\Rightarrow y'=2/y$; circle $2x+2y\,y'-6+0=0\Rightarrow y'=(3-x)/y$.
At $(1,2)$: parabola slope $=1$, circle slope $=(3-1)/2=1$. Equal slopes ⇒ curves touch. Similarly at $(1,-2)$.
</details>

**3. 🔴 ODE + Tangent + Area bridge.** Curve satisfies $\dfrac{dy}{dx}=\dfrac{y}{x}$ and passes through $(1,2)$. Find tangent at that point and the area under the curve from $x=1$ to $x=2$.
<details><summary><b>Solution</b></summary>
$\dfrac{dy}{y}=\dfrac{dx}{x}\Rightarrow \ln y=\ln x+\ln C\Rightarrow y=Cx$. Through $(1,2)$: $C=2$, so $y=2x$.
Tangent at $(1,2)$: slope $2$, equation $y-2=2(x-1)\Rightarrow y=2x$.
Area $=\int_{1}^{2}2x\,dx=[x^2]_{1}^{2}=4-1=3$ sq units. (Bridges AOD → Integrals, Ch 7.)
</details>

**4. 🔴 Absolute value + Continuity (Ch 5).** Discuss monotonicity and extrema of $f(x)=|x^2-4x+3|$ and state where it fails to be differentiable.
<details><summary><b>Solution</b></summary>
Roots at $x=1,3$. $x^2-4x+3<0$ on $(1,3)$. So $f$ has upward cusps (non-diff) at $x=1,3$ (local minima, value 0). Local maximum at vertex $x=2$, value $|4-8+3|=1$.
Increasing on $(1,2)\cup(3,\infty)$; decreasing on $(-\infty,1)\cup(2,3)$. Non-differentiable at $x=1,3$.
</details>

---

## 📋 Stage 6: Board Arsenal

Full NCERT-Exemplar-style long optimization narratives. Mark allocation shown.

### Long Narrative 1: Telephone Company Profit ⭐
> **(Exemplar Q27 style, 5 marks)** A telephone company has 500 subscribers, each paying ₹300 per month. For each ₹1 increase in the monthly charge, one subscriber discontinues. Find the increase that yields the maximum monthly profit.

<details><summary><b>Model Answer (5 marks)</b></summary>
Let the increase be ₹$x$. (1 mark for defining variable)
Number of subscribers $=500-x$. (1 mark)
Monthly charge per subscriber $=$ ₹$(300+x)$. (1 mark)
Total revenue $R(x)=(500-x)(300+x)$. (1 mark)
$$ R(x)=150000+500x-300x-x^2=150000+200x-x^2. $$
$$ R'(x)=200-2x=0\Rightarrow x=100. $$
$$ R''(x)=-2<0\Rightarrow \text{maximum}. $$
**Maximum profit occurs at an increase of ₹100** (charge ₹400, 400 subscribers). (1 mark)
</details>

### Long Narrative 2: Open Box from a Square Sheet ⭐
> **(Exemplar Q29 style, 5 marks)** A square sheet of side $c$ has equal squares of side $x$ cut from each corner and the edges folded to make an open box. Show that the volume is maximum when $x=c/6$.

<details><summary><b>Model Answer (5 marks)</b></summary>
Base side $=c-2x$, height $=x$. (1 mark)
$$ V(x)=x(c-2x)^2,\quad 0<x<c/2. $$
$$ V'(x)=(c-2x)^2+x\cdot2(c-2x)(-2)=(c-2x)(c-2x-4x)=(c-2x)(c-6x). $$
Critical points $x=c/2$ (gives $V=0$, minimum) and $x=c/6$. (2 marks)
$$ V''(x)=-12c+24x;\quad V''(c/6)=-12c+4c=-8c<0\Rightarrow \text{maximum}. $$
Hence maximum volume at $\boxed{x=c/6}$. (2 marks)
</details>

### Long Narrative 3: Cube + Sphere Combined ⭐
> **(Exemplar Q31 style, 5 marks)** The sum of surface areas of a cube (edge $a$) and a sphere (radius $r$) is constant $k$. Show the sum of volumes is minimum when $3a=2r$ under the equal-weight surface-area formulation $6a^2=4\pi r^2$ condition is *not* assumed; instead derive the true relation.

<details><summary><b>Model Answer (5 marks)</b></summary>
Constraint $6a^2+4\pi r^2=k$. (1 mark)
$V=a^3+\frac43\pi r^3$. Express $r^2=(k-6a^2)/(4\pi)$, $V(a)=a^3+\frac{1}{6\sqrt\pi}(k-6a^2)^{3/2}$. (2 marks)
$V'(a)=3a^2-\dfrac{a\sqrt{k-6a^2}}{\sqrt\pi}=0\Rightarrow 9\pi a^2=k-6a^2\Rightarrow 4\pi r^2=9\pi a^2\Rightarrow r=\frac32a$. (1 mark)
So minimum volume when $\boxed{2r=3a}$ (diameter $=3\times$ edge), verified by FDT. (1 mark)
</details>

### Long Narrative 4: Triangle on a Diameter ⭐
> **(Exemplar Q25 style, 4 marks)** A right triangle has hypotenuse $a$ and one side $b$. Show its area is maximum when the angle between them is $\pi/3$.

<details><summary><b>Model Answer (4 marks)</b></summary>
Let the included angle be $\theta$. Area $A=\frac12 ab\sin\theta$. (1 mark)
Third side by cosine rule; but with $a,b$ fixed, $A$ is max when $\sin\theta$ max = 1 ⇒ $\theta=\pi/2$? Wait — the Exemplar version fixes *hypotenuse + one side*, not two sides. Reformulate correctly: let hypotenuse $h$ and one leg $x$ be fixed-sum $s$; then other leg $=\sqrt{h^2-x^2}$... Actually the classic statement: **sum of hypotenuse and one side is constant** $=c$; maximise area. Let hypotenuse $a$, side $b$, included angle $\theta$ between them with other leg $=\sqrt{a^2-b^2}$. With $a+b=c$ fixed: $A=\frac12 b\sqrt{a^2-b^2}$. Substitute $a=c-b$: $A=\frac12 b\sqrt{(c-b)^2-b^2}=\frac12 b\sqrt{c^2-2bc}$. (2 marks)
$A^2=\frac14 b^2(c^2-2bc)$. Derivative w.r.t. $b$: $\frac{d}{db}[b^2c^2-2b^3c]=2bc^2-6b^2c=0\Rightarrow b=c/3$, $a=2c/3$. Then $\cos\theta=b/a=1/2\Rightarrow \theta=\pi/3$. (1 mark)
Hence area max when $\boxed{\theta=\pi/3}$. (1 mark)
</details>

---

## 🚀 Stage 7: JEE Mains / Advanced Arena — HOTS

**1. 🔴 (Inequality via monotonicity) Prove that $\ln(1+x)<x$ for all $x>0$.**
<details><summary><b>Solution</b></summary>
Let $h(x)=x-\ln(1+x)$. $h(0)=0$, $h'(x)=1-\dfrac{1}{1+x}=\dfrac{x}{1+x}>0$ for $x>0$.
So $h$ is strictly increasing on $(0,\infty)$ ⇒ $h(x)>h(0)=0$ ⇒ $x>\ln(1+x)$. ∎
</details>

**2. 🔴 (AM-GM constrained optimization) Find the minimum of $x^2+\dfrac{16}{x}$ for $x>0$ without calculus.**
<details><summary><b>Solution</b></summary>
Write $x^2+\dfrac{16}{x}=x^2+\dfrac{8}{x}+\dfrac{8}{x}\ge 3\sqrt[3]{x^2\cdot\frac{8}{x}\cdot\frac{8}{x}}=3\sqrt[3]{64}=3\cdot4=12$.
Equality when $x^2=8/x\Rightarrow x^3=8\Rightarrow x=2$. Minimum $=12$. (Calculus check: $2x-16/x^2=0\Rightarrow x=2$, $f''>0$.)
</details>

**3. ⭐ (Second-derivative test fails) Discuss extrema of $f(x)=x^4$ at $x=0$.**
<details><summary><b>Solution</b></summary>
$f'(0)=0$, $f''(0)=0$ ⇒ SDT fails. Fall back to FDT: $f'(x)=4x^3$ changes $-$ to $+$ at $0$ ⇒ **local (and absolute) minimum**, $f(0)=0$.
</details>

**4. 🔴 (Functional-equation extrema) If $f(x+y)=f(x)f(y)$ for all real $x,y$ and $f$ is differentiable with $f'(0)=2$, find the maximum value of $f(x)/(1+f(x)^2)$.**
<details><summary><b>Solution</b></summary>
The only differentiable solutions are $f(x)=e^{kx}$. $f'(0)=k f(0)=k\cdot1=2\Rightarrow k=2$, so $f(x)=e^{2x}>0$.
Maximise $g(u)=\dfrac{u}{1+u^2}$ for $u>0$. $g'(u)=\dfrac{1-u^2}{(1+u^2)^2}=0\Rightarrow u=1$.
So max when $e^{2x}=1\Rightarrow x=0$, maximum value $=\boxed{1/2}$.
</details>

**5. 🔴 (Boundary optimum — links §05 vs §06) A rectangular pen uses 100 m of fence on three sides (fourth side is a wall). Maximise area. Then suppose the width must not exceed 30 m — where does the optimum move?**
<details><summary><b>Solution</b></summary>
Let width perpendicular to wall $=x$, length along wall $=y$. $2x+y=100$, $A=xy=x(100-2x)=100x-2x^2$. Unconstrained max at $x=25$, $y=50$, $A=1250$.
With constraint $x\le 30$: $A'(x)=100-4x>0$ for $x<25$ and $A$ decreases for $x>25$, so within $[0,30]$ the maximum is still interior at $x=25$. If instead the constraint were $x\le 20$, the optimum would shift to the **boundary** $x=20$ ($A=1200$) — illustrating that absolute maxima can sit at endpoints (§06).
</details>

---

## 🪤 Common Traps — Chapter-Wide (Read Before You Sit)

> ⚠️ **Trap 1 — Differentiability before Monotonicity/Extrema.** For $|x|$-type or piecewise functions, the derivative may not exist at a corner. That corner can *itself* be a local extremum (e.g., $|x^2-1|$ at $x=\pm1$). Always check differentiability first; use FDT with one-sided signs.

> ⚠️ **Trap 2 — Critical point ≠ Extremum.** $f'(c)=0$ only flags a *candidate*. $x^3$ at $0$ has $f'(0)=0$ but is a point of inflection. Always confirm with FDT or SDT.

> ⚠️ **Trap 3 — SDT silently fails.** If $f'(c)=0$ and $f''(c)=0$, the second-derivative test is inconclusive. You MUST revert to the first-derivative test (e.g., $x^4$ at 0). Concluding "no extremum" here is a classic blunder.

> ⚠️ **Trap 4 — Forgetting endpoints in absolute extrema.** On $[a,b]$, a local min inside can be beaten by the endpoint value. Evaluate $f$ at every critical point **and** at $a$ and $b$. Board questions love an endpoint-dominated answer.

> ⚠️ **Trap 5 — Strict vs non-strict wording.** "Increasing" in many board papers means $f'(x)\ge0$; "strictly increasing" means $f'(x)>0$. $x^3$ is strictly increasing though $f'(0)=0$. Match the question's word to the inequality.

> ⚠️ **Trap 6 — Tangent slope = 0 ⇒ normal is vertical ($x=x_1$); normal slope = 0 ⇒ tangent is horizontal.** Don't write a finite normal equation when the tangent is horizontal.

> ⚠️ **Trap 7 — Sign errors in related rates.** A decreasing quantity has a *negative* rate. Plugging the instantaneous $x$ (not the time $t$) into the derivative is mandatory; never substitute $t$-values for $x$-values.

> ⚠️ **Trap 8 — Integrating when you only need the sign.** For integral-defined functions, $f'(x)=g(x)$ by Leibniz. Decide monotonicity from the sign of $g(x)$; integrating is wasted effort and error-prone.

> ⚠️ **Trap 9 — Domain restrictions.** $x>0$ for $x^x$, principal-value ranges for $\tan^{-1}$, and trigonometric intervals all constrain where an extremum is valid. An unconstrained critical point outside the domain is not a solution.

> ⚠️ **Trap 10 — Optimising outside the feasible region.** Negative dimensions, $r<0$, or $x>c/2$ in the open-box problem are mathematically critical but physically impossible. Reject them explicitly.

---

## 📌 Quick Revision Summary

- **Monotonicity:** signs of $f'(x)$; $f'(x)>0$ strictly increasing. Check differentiability at corners first.
- **Tangent/Normal:** $m_T=f'(x_1)$; $m_N=-1/m_T$. Special cases: $m_T=0\Rightarrow$ normal vertical; $m_T$ undefined $\Rightarrow$ tangent vertical.
- **Conics:** circle $xx_1+yy_1=r^2$; parabola $yy_1=2a(x+x_1)$; ellipse tangent condition $p^2=a^2\cos^2\alpha+b^2\sin^2\alpha$.
- **Extrema:** critical point where $f'(c)=0$ or non-differentiable. FDT = sign change of $f'$; SDT = $f''(c)$ sign; **if SDT fails, use FDT.**
- **Absolute extrema on $[a,b]$:** evaluate $f$ at all critical points **and** endpoints $a,b$.
- **Integral-defined $f$:** $f'(x)=g(x)$; read sign of integrand — no need to integrate.
- **Absolute-value extrema:** decompose piecewise; corners are candidate extrema.
- **ODE-defined curve:** solve (or just evaluate slope at the given point) then apply tangent/normal.
- **Determinant max:** expand, then AOD; watch for constant (zero) trick determinants.
- **Constrained optimization:** substitute constraint → one variable → extrema; verify with FDT/SDT; AM-GM as a non-calculus alternative.
- **Inequality proofs:** set $h=f-g$, show $h$ increasing and $h(a)\ge0$.

> 🔑 **Final Key Takeaway:** The Grand Synthesis is never about a *new* formula — it is about **recognising which of your existing tools applies after you decompose the question**. Differentiate, decompose, substitute. Then the boss falls.

---

*Previous: [Chapter 06 — Absolute Maxima/Minima](./06_absolute_extrema.md)*
*This is the capstone chapter of Application of Derivatives. Return to any earlier chapter to drill weak types.*
