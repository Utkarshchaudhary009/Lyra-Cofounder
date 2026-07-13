# NCERT Class 12 Maths — Chapter 6: Application of Derivatives
## CURRICULUM RESEARCH MAP (Board + JEE Mains + JEE Advanced)
### Purpose: Writer briefing only. NO chapter content written here.

> How to use: Each sub-chapter below gives the NCERT learning objective, the must-know formula bank, 4–8 distinct QUESTION TYPES to author, the most common exam traps, and 2–3 competency/case-study framing ideas. Pull the question types into the chapter's drill/exercise banks.

---

## 00. CHAPTER-WIDE FRAME & EXAM WEIGHTAGE

**NCERT section skeleton (verbatim):**
- 6.1 Introduction
- 6.2 Rate of Change of Quantities
- 6.3 Increasing and Decreasing Functions
- 6.4 Tangents and Normals
- 6.5 Approximations
- 6.6 Maxima and Minima
  - 6.6.1 Maximum and Minimum Values of a Function in a Closed Interval

**CBSE Board weightage (typical):** ~5–6 marks standalone in the main paper, PLUS guaranteed appearance in Section E (case study, 4 marks) and often an MCQ/Assertion-Reason in Section A. Application of Derivatives is one of the highest-yield calculus chapters.

**2023–24 Board paper structure (per CBSE Additional Practice QP):**
- Section A: 18 MCQ + 2 Assertion-Reason, 1 mark each
- Section B: 5 VSA, 2 marks each
- Section C: 6 SA, 3 marks each
- Section D: 4 LA, 5 marks each
- Section E: 3 case-study/passage units, 4 marks each (sub-parts 1+1+2 or 2+2) — **AOD appears here frequently.**

**10-year PYQ hotspot ranking (most → least frequent):**
1. Maxima & Minima (local + absolute in closed interval) — appears every year, 4/5/6-mark.
2. Tangents & Normals — every year, 2/4-mark, plus MCQs.
3. Increasing/Decreasing functions — every year, 2/4-mark.
4. Rate of Change — every year, usually 2-mark or MCQ; easy marks.
5. Approximations (differentials) — nearly every year, 1–2 marks / VSA; sometimes folded into error-estimation case studies.

**Competency/case-study reality (post-2020):** Section E case studies are framed around real scenarios — water tank filling, ladder sliding, shadow length, manufacturing/cost optimization, garden fencing, cylindrical can cost, square/equilateral area growth. Writers MUST include at least one full case-study per sub-chapter theme.

**Cross-cutting traps to warn writers about (chapter-wide):**
- Forgetting domain restrictions (e.g., x>0, trigonometric intervals).
- Using f'(x)≥0 vs f'(x)>0 — strict vs non-strict monotonicity wording in the question.
- Differentiating with respect to wrong variable (t vs x) in related rates.
- Forgetting to check endpoints in absolute max/min on a closed interval.
- Sign errors in first-derivative-test interval table.
- Confusing point of inflection with local extremum.
- Second-derivative test "fails" case (f'(c)=f''(c)=0) → must fall back to first-derivative test.

---

## 01. RATE OF CHANGE OF QUANTITIES (NCERT 6.2)

**NCERT objective:** Interpret dy/dx as the rate of change of y with respect to x; extend to related rates where x and y both depend on a third variable t (time). Compute how fast one quantity changes when another changes, including motion along curves and geometry (area, volume, perimeter) problems.

**Must-know formulas:**
- dy/dx = rate of change of y w.r.t. x.
- If x = f(t), y = g(t): dy/dx = (dy/dt)/(dx/dt) (chain rule).
- Related rates: differentiate the connecting equation w.r.t. t, substitute known instantaneous values.
- Geometry rates: dA/dt, dV/dt, dP/dt from A(x), V(x), P(x); e.g.:
  - Circle: A = πr² → dA/dt = 2πr·dr/dt; C = 2πr → dC/dt = 2π·dr/dt ⇒ dA/dt ∝ r.
  - Sphere: V = 4/3πr³ → dV/dt = 4πr²·dr/dt; S = 4πr² → dS/dt = 8πr·dr/dt.
  - Cone: V = 1/3πr²h (watch fixed-ratio constraints like h = r/6).
  - Equilateral triangle: A = √3/4 a² → dA/dt = √3/2 a·da/dt.
  - Rectangle: A = xy, P = 2(x+y) → dA/dt = x dy/dt + y dx/dt.
  - Triangle with included angle: A = 1/2 ab sinθ → dA/dt = 1/2 ab cosθ·dθ/dt.
- Motion: velocity v = ds/dt, acceleration a = d²s/dt²; s = A sin t + B cos t ⇒ a = −s (HOTS, CBSE 2024-25 competency Q).

**Question types (author 6–8):**
1. **Direct single-variable rate:** "Side of square grows at 2 cm/s; find rate of area increase when side = 10 cm." (NCERT/Board staple, 2M.)
2. **Two-variable rectangle (x falling, y rising):** given dx/dt and dy/dt, find rate of change of perimeter and area at given x,y. (All India 2017, 4M.)
3. **Geometry-with-fixed-ratio cone:** sand pours forming cone with h = r/6; given dV/dt find dh/dt. (Delhi 2011, 4M.)
4. **Equilateral/isosceles triangle area rate:** side increasing at k cm/s; find dA/dt at given side; or equal sides of fixed-base isosceles increasing — find area rate when sides equal. (Delhi 2015; CUET/HOTS.)
5. **Motion along a curve:** particle on 3y = ax³+1, dy/dt = 2·dx/dt at x=1, find a. (CBSE 2023, 2M.)
6. **Point on curve where coordinates change at same rate:** find point on y² = 8x where dx/dt = dy/dt. (CBSE 2023, 2M; also Hitbullseye MCQ set.)
7. **Ratio-of-rates proof:** "If circumference increases at constant rate, prove dA/dt ∝ r." (Competency proof style.)
8. **Trig/area rate with included angle:** rate of change of area of triangle with sides 10,12 as θ changes at θ=60°. (Hitbullseye MCQ.)

**Common traps:**
- Mixing up which quantity is increasing vs decreasing (sign of rate).
- Plugging t-values instead of the instantaneous x/y at that instant.
- Forgetting chain rule factor (e.g., dA/dt = 2πr dr/dt, not just dr/dt).
- Circular area growth: claim dA/dt constant; actually it scales with r.

**Competency / case-study framing ideas:**
- **Expanding circular metal plate:** area grows constantly; student must justify whether perimeter-growth rate is inversely proportional to radius. (CBSE 2024-25 CBQ Q9.)
- **Cylindrical water-tank capacity error:** radius measured with small error → approximate error in capacity. (CBSE 2024-25 CBQ Q3.)
- **Square garden diagonal growth:** diagonal increasing at 2 cm/s; find area growth rate. (CBSE 2024-25 CBQ Q1 — easy MCQ opener.)

---

## 02. INCREASING AND DECREASING FUNCTIONS (NCERT 6.3)

**NCERT objective:** Use the first derivative to determine intervals where a function is strictly increasing / strictly decreasing / neither. State and apply: f increasing on (a,b) iff f'(x) > 0; f decreasing iff f'(x) < 0; constant iff f'(x)=0. Handle polynomials, trigonometric, and rational functions; find monotonicity on a specified interval.

**Must-know formulas / results:**
- f increasing in interval ⇔ f'(x) ≥ 0 (strictly increasing ⇔ f'(x) > 0) for all x in interval; f differentiable.
- Theorem (NCERT Exemplar 6.1.5): continuous on [a,b], differentiable in (a,b); f increasing if f'(x)>0 each x, etc.
- Procedure: solve f'(x)=0 → critical points → partition real line → test sign of f'(x) in each sub-interval.
- Trigonometric monotonicity: sin x increasing on (−π/2, π/2); cos x decreasing on (0,π); etc. Requires restricting domain.
- f'(x) = 0 at isolated points does NOT break strict monotonicity (e.g., x³ has f'(0)=0 but is strictly increasing everywhere).

**Question types (author 6–8):**
1. **Cubic polynomial intervals:** f(x) = ax³+bx²+cx+d → factor f'(x), build sign chart, state increasing/decreasing intervals. (Delhi 2014; All India 2010; huge repeat frequency.)
2. **Higher-degree polynomial (x⁴):** f(x)=3x⁴−4x³−12x²+5 → three critical points, four intervals. (Delhi 2014.)
3. **Factored-form product:** f(x) = (x−1)³(x−2)² → product-rule derivative, sign analysis. (All India 2011C.)
4. **Trigonometric interval:** f(x)=sin3x−cos3x on 0<x<π → find strictly increasing/decreasing sub-intervals. (Delhi 2016.)
5. **"Neither increasing nor decreasing" proof:** show f(x)=x²−x+1 is neither on (−1,1), then give the actual intervals. (Delhi 2014C.)
6. **Parameter-based monotonicity:** find k such that f(x)=... is increasing/decreasing on given interval (f'(x)≥0 inequality in k).
7. **Prove a function is always increasing/decreasing:** e.g., f(x)=tan x − x always increases; f(x)=2x+cos x monotonic. (Exemplar MCQs 14, 18.)
8. **Assertion-Reason MCQ:** "f'(x)>0 on (a,b) ⇒ f strictly increasing" vs converse — test edge cases (x³ at 0).

**Common traps:**
- Writing "increasing" when derivative is only non-negative; wording matters (strict vs non-strict).
- Dropping the critical points from interval notation incorrectly (open vs closed brackets).
- Sign-chart arithmetic errors after factoring.
- Assuming f'(x)=0 somewhere means function is not monotonic (x³ counterexample).
- Forgetting to restrict trig domain before claiming monotonicity.

**Competency / case-study framing ideas:**
- **Function-nature from graph with parameter k:** given a sketch, decide increasing/decreasing/neither with unknown k. (CBSE 2024-25 CBQ Q4.)
- **Temperature/logistic growth model:** interpret f'(t) sign as "heating up vs cooling down" over time; student states intervals.
- **Profit/cost monotonicity:** given revenue R(x), decide for which production levels profit is rising — bridges to economics.

---

## 03. TANGENTS AND NORMALS (NCERT 6.4)

**NCERT objective:** Find slope of tangent (dy/dx at point), equation of tangent and normal to y=f(x) at (x₁,y₁); handle implicit curves, parametric curves, and the angle between two intersecting curves; tangent/normal parallel/perpendicular to given lines.

**Must-know formulas:**
- Slope of tangent m_T = dy/dx at (x₁,y₁); equation: y−y₁ = m_T(x−x₁).
- Slope of normal m_N = −1/m_T (if m_T≠0); equation: y−y₁ = −1/m_T (x−x₁).
- Horizontal tangent ⇔ dy/dx = 0; vertical tangent ⇔ dx/dy = 0 (dy/dx → ∞).
- Tangent equally inclined to axes ⇔ m_T = ±1; equal intercepts on axes ⇔ m_T = −1.
- Parametric: dy/dx = (dy/dt)/(dx/dt).
- Angle between curves = angle between tangents: tan θ = |(m₁−m₂)/(1+m₁m₂)|; orthogonal ⇔ m₁m₂ = −1.
- Tangent to standard conics: parabola y²=4ax ⇒ tangent at (x₁,y₁): yy₁=2a(x+x₁); circle x²+y²=r² ⇒ xx₁+yy₁=r².
- Lengths (JEE): tangent = |y|√(1+m²)/m, normal = |y|√(1+m²), subtangent = |y/m|, subnormal = |y m|.

**Question types (author 6–8):**
1. **Tangent/normal to explicit curve at a point:** y = f(x), compute m, write both equations. (NCERT basic.)
2. **Implicit curve:** x²+y²−2x−4y+1=0 → find tangent parallel to axes / normal. (Exemplar Q47, Q18.)
3. **Tangent equally inclined / equal intercepts:** find point(s) where m_T = ±1 or −1. (Exemplar Q14; JEE "equally inclined to axes".)
4. **Tangent parallel to a given line:** y = x³+3x²+5 tangent through origin / parallel to given line; find point. (JEE Main 2022, 2019, 2017 patterns.)
5. **Normal passes through external point / axis:** normal at point meets a given point; solve for point of contact. (JEE Main 2017 Offline; 2016 Offline normal through point.)
6. **Angle between two curves / orthogonal intersection:** y²=4x and x²+y²−6x+1=0 touch; or curves intersect orthogonally → find parameter. (Exemplar Q49, Q53; JEE 2016 y²=6x & 9x²+by²=16.)
7. **Parametric curve tangent:** x=t²+3t−8, y=2t²−2t−5 → slope at given t. (Exemplar Q21; JEE 2022 param curve.)
8. **Tangent to conic in standard form:** tangent to parabola/circle/ellipse at given point or with given slope; normal to y=tan x at (0,0). (Exemplar Q4, Q46, Q37 tangent condition x cosα+y sinα=p touches ellipse.)

**Common traps:**
- Normal slope when tangent slope = 0 (normal is vertical, equation x = x₁) and vice versa.
- Sign error in negative reciprocal.
- For implicit differentiation, dropping the y' term.
- Confusing "tangent equally inclined to axes" (m=±1) with "equal intercepts" (m=−1).
- Parametric: computing dy/dt ÷ dx/dt in wrong order.

**Competency / case-study framing ideas:**
- **Normal makes angle π/4 with +x-axis at (5,7):** find f'(5) and justify. (CBSE 2024-25 CBQ Q5 — reasoning style.)
- **Ladder sliding / shadow problem:** geometry gives implicit relation; find where tangent (or rate) matters — bridge to §01.
- **Curve touches another curve (tangency condition):** two given curves touch → find unknown parameter; framed as "do these machine-part profiles meet smoothly?"

---

## 04. APPROXIMATIONS (NCERT 6.5)

**NCERT objective:** Use differentials to find approximate values of functions and approximate errors in measurement (Δy ≈ dy = f'(x)·Δx). Apply to (i) approximate computation like (3.968)^(3/2), (ii) error estimation in area/volume given small measurement error.

**Must-know formulas:**
- Δy ≈ dy = f'(x)·Δx when Δx is small.
- f(x+Δx) ≈ f(x) + f'(x)·Δx.
- Relative error = Δx/x; percentage error = (Δx/x)·100; error propagation:
  - Sphere S = 4πr² → ΔS ≈ 8πr·Δr; V = 4/3πr³ → ΔV ≈ 4πr²·Δr.
  - Cylinder V = πr²h → ΔV ≈ π(2rh·Δr + r²·Δh).
  - Square area A = s² → ΔA ≈ 2s·Δs.
- Choose x = convenient nearby exact value (e.g., 4 for 3.968; 1 for 0.999; 8 for 7.98).

**Question types (author 6–8):**
1. **Approximate a radical/power:** (3.968)^(3/2), (0.999)^(1/3), √(0.6), (255)^(1/4), etc. (Delhi 2014C; NCERT Misc.)
2. **Approximate reciprocal/log:** (0.99)^−¹, log(1.01), sin(π/60) using linear approx.
3. **Error in sphere surface area:** r=9±0.03 → ΔS. (All India 2011.)
4. **Error in volume of sphere/cylinder/cube:** given Δr find ΔV or % error. (CBSE 2024-25 CBQ Q3 capacity error.)
5. **Percentage error propagation:** error in radius 1% → % error in area/volume.
6. **Approximate change in y:** y=x⁴−10, x: 2→1.99, find Δy. (Exemplar Q25.)
7. **Approx error in square garden area:** side 10 m ± 0.05 m → error in area. (CBSE 2024-25 CBQ Q2.)
8. **Trig approximation:** sin(π/6+0.01) or cos(0.1) using f(x+Δx)≈f(x)+f'(x)Δx.

**Common traps:**
- Picking x far from x+Δx (approximation invalid).
- Sign of Δx (3.968 = 4 + (−0.032), not +0.032).
- Using Δy = f'(x)Δx but forgetting to ADD to f(x).
- Confusing absolute error with percentage error.
- Differentiating wrong function (e.g., f(x)=x^(3/2), not x³/2).

**Competency / case-study framing ideas:**
- **Garden side measurement error:** side 10 m measured with ±0.05 m error → approximate area error. (CBSE 2024-25 CBQ Q2.)
- **Cylindrical tank radius error:** radius 2 m ± 0.05 m → error in capacity. (CBSE 2024-25 CBQ Q3.)
- **Manufacturing tolerance:** machined disk radius tolerance → % error in painted surface area; cost implication.

---

## 05. LOCAL MAXIMA AND MINIMA — 1st & 2nd DERIVATIVE TESTS (NCERT 6.6, up to 6.6.1 intro)

**NCERT objective:** Define local maxima/minima and critical points; apply First Derivative Test (sign change of f'(x)) and Second Derivative Test (f'(c)=0, f''(c)<0 max / >0 min; test fails if f''(c)=0). Identify points of inflection.

**Must-know formulas / working rules:**
- Critical point: c where f'(c)=0 or f not differentiable.
- First Derivative Test: f' changes + → − at c ⇒ local max; − → + ⇒ local min; no change ⇒ point of inflection.
- Second Derivative Test: f'(c)=0 and f''(c)<0 ⇒ local max; f''(c)>0 ⇒ local min; f''(c)=0 ⇒ test fails → use 1st test.
- Special forms: x^x, (1/x)^x, (2/x)^(x²) — take log then differentiate (Exemplar Q6, Q7; JEE 2021 (2/x)^(x²)).
- f(x)=ax+b/x (a,b>0,x>0) minimum at x=√(b/a) (Exemplar Q1).
- max of sin x cos x = 1/2 (Exemplar Q10).

**Question types (author 6–8):**
1. **Polynomial local extrema + values:** f(x)=2x³−3x²−12x+4 → critical points, classify, give max/min values. (Exemplar Q11; JEE 2018 M/m.)
2. **High-degree polynomial:** f(x)=x⁵−5x⁴+5x³−1 → local max/min + points of inflection. (Exemplar Q26.)
3. **Second-derivative-test failure fallback:** construct/use a case where f''(c)=0 → revert to first test (e.g., x⁴ at 0).
4. **Logarithmic-form extrema:** y = x^x, (1/x)^x, (2/x)^(x²) → log-differentiate. (Exemplar Q6,7; JEE Main 2021, 2022.)
5. **Trig extrema:** f(x)=2 sin3x+3 cos3x → max/min; or prove max of sin x+√3 cos x at x=π/6. (Exemplar Q9, Q41.)
6. **Parameter/condition on extrema:** f has local max for some x<0 and local min for x>0 → find parameter set (JEE 2023 25 Jan); or f'(1)=0 condition.
7. **Exact-one-max-one-min condition:** find λ so f(x)=(1−cos²x)(λ+sin x) has exactly one max and one min. (JEE 2020.)
8. **Monotonicity + extrema mixed (Assertion-Reason / MCQ):** f''>0 ∀x, g(x)=f(tan²x−2tan x+a) → increasing/decreasing intervals. (JEE 2026, 2023 patterns.)

**Common traps:**
- Reporting critical point x-value as the extremum value (must substitute back to get f(c)).
- Declaring min/max from f''(c) sign without first confirming f'(c)=0.
- When second test fails, wrongly concluding "no extremum" instead of reverting to first test.
- Missing points where f not differentiable (cusps, e.g., y=x^(1/5) vertical tangent at 0 — Exemplar Q28).
- Confusing local vs absolute (covered in §06).

**Competency / case-study framing ideas:**
- **Telephone-company profit:** base subscribers + fixed charge, churn above a price → find increase that maximizes profit. (Exemplar Q27 — classic optimization narrative.)
- **Open box from given cardboard area c²:** show max volume. (Exemplar Q29.)
- **Maximum slope of a curve:** y=−x³+3x²+9x−27 → point of maximum slope and its value. (Exemplar Q42/23; JEE 2021 "maximum slope".)

---

## 06. ABSOLUTE MAXIMA/MINIMA IN A CLOSED INTERVAL (NCERT 6.6.1)

**NCERT objective:** Find absolute (global) maximum and minimum of a continuous function on a closed interval [a,b]: evaluate f at all critical points inside (a,b) AND at endpoints a,b; the largest is absolute max, smallest absolute min. Apply to real optimization.

**Must-know formulas / working rule (NCERT Exemplar 6.1.8):**
- Step 1: find all critical points of f in [a,b]. Step 2: compute f at those points and at a,b. Step 3: largest = absolute max, smallest = absolute min.
- For an open interval or unrestricted domain, absolute extrema may not exist — must state if so.
- Optimization with constraint: express objective in one variable using the constraint, then apply absolute-extrema method on the feasible interval.

**Question types (author 6–8):**
1. **Polynomial on closed interval:** f(x)=2x³−3x²−12x+5 on [−2,4] → absolute max/min. (BYJU'S JEE Q2.)
2. **Polynomial absolute min on [0,9]:** x³−18x²+96x → smallest value. (Exemplar Q12.)
3. **Geometric optimization (rectangle/garden):** fixed fencing 200 ft with one brick wall → maximize area; find x and max area. (Study Rate case study; XAM CONTENT style.)
4. **Cylindrical can cost optimization:** fixed volume 500 cm³, top/bottom cost double → minimize cost; find r. (XAM CONTENT 2025 case study.)
5. **Cone in sphere / sphere-inscribed optimization:** ratio of height of max-volume cone inscribed in sphere to radius. (BYJU'S JEE Q3; classic JEE.)
6. **Right-triangle area max with constraint:** sum of hypotenuse and a side fixed → show area max when angle between them is π/3. (Exemplar Q25.)
7. **Two-shape combined optimization:** sum of surface areas of cube + sphere constant → ratio of edge to sphere diameter when sum of volumes min. (Exemplar Q31, Q34.)
8. **Absolute max/min of a tricky function on interval:** f(x) = (2/x)^(x²) on (0,∞) local max (JEE 2021); or absolute max/min of rational/trig on closed interval.

**Common traps:**
- Forgetting endpoints — local min inside may not be absolute min; endpoint can dominate.
- Optimizing outside the feasible interval (e.g., negative dimensions).
- Not reducing to one variable before differentiating.
- Assuming symmetry gives optimum without proof.
- For "show area max when angle = π/3" type, failing to verify second-derivative/endpoint.

**Competency / case-study framing ideas:**
- **Garden fencing with brick wall (200 ft):** maximize area, x = side perpendicular to wall → A(x)=200x−2x², max at x=50, area 5000. (Study Rate case study, full 5-part MCQ.)
- **Cylindrical can (V=500 cm³, top/bottom double cost):** minimize manufacturing cost → r=(125/π)^(1/3); interpret economically. (XAM CONTENT 2025.)
- **Open tank square base / box from cardboard:** minimize material for fixed volume, or maximize volume for fixed area. (Exemplar Q29; classic board 4–6 mark.)

---

## 07. NCERT EXEMPLAR & CROSS-TOPIC / MIXED GRAND SYNTHESIS

### 7A. NCERT Exemplar problem styles (per topic)
Exemplar has objective + VSA + SA + LA. Signature styles writers should mirror:
- **Fill-in-the-blank optimization:** "least value of ax+b/x (a,b>0,x>0) is ___"; "equation of normal to y=tan x at (0,0) is ___." (Exemplar Q1, Q4.)
- **MCQ on monotonicity/extrema:** tan x − x always increases; f(x)=2x+cos x has min at…; interval where 2x³+9x²+12x−1 decreases. (Exemplar Q14, Q18, Q19.)
- **"Curves touch each other" proofs:** y²=4x and x²+y²−6x+1=0 touch; xy=4 and x²+y²=8 touch; orthogonal intersection conditions. (Exemplar Q49, Q52, Q53.)
- **Tangent/normal to conic with parameter:** line x cosα+y sinα=p touches ellipse → condition. (Exemplar Q37.)
- **Long optimization narratives:** telephone profit, open box, rectangle revolved about side (max volume), cube+sphere, triangle on diameter. (Exemplar Q27–Q34.)
- **Local maxima/minima + inflection:** x⁵−5x⁴+5x³−1 full classification. (Exemplar Q26.)

### 7B. Cross-topic application matrix (combine AOD with other chapters)
Writers should seed these "grand synthesis" problems across the chapter:

| Paired topic | Concrete question pattern |
|---|---|
| **Continuity & Differentiability (Ch 5)** | f with absolute values / piecewise definitions → check differentiability then monotonicity & extrema (e.g., f(x)=||x+2|−2|x|| local min/max count — JEE 2025). |
| **Integrals / Area (Ch 7–8)** | f(x)=∫ g(t)dt given; deduce monotonicity from sign of integrand without integrating (JEE 2021); area optimization of revolved rectangle (Exemplar Q30). |
| **Coordinate Geometry (Ch 11, Ch 12)** | Tangent/normal to parabola y²=4ax, circle, ellipse, hyperbola; shortest distance between two curves (JEE Main Tangent&Normal, 2024 Jan 27); normal to parabola intersects circle (JEE 2019). |
| **Trigonometry / Inverse Trig (Ch 2)** | Monotonicity of tan⁻¹(sin x+cos x) on (0,π/4) (Exemplar Q43); maxima of a sin x + b cos x; prove max at specific angle. |
| **Vectors & 3D (Ch 10–11)** | Rate of change of distance between moving particles; optimization of box/parallelepiped dimensions; normal vector interpretation. |
| **Matrices/Determinants (Ch 3–4)** | Max value of a determinant-function f(x) (JEE 2021 max of 3×3 det with trig entries). |
| **Probability (Ch 13)** | Optimize expected profit / minimize expected cost (light bridge to §06 optimization). |
| **Differential Eqs (Ch 9)** | Slope-of-curve ODE given (dy/dx = F(x,y)) → find curve through a point, then tangent/normal (JEE 2022 slope-of-normal ODE, curve through (1,1)). |

### 7C. "Grand Synthesis" question types to author (4–6)
1. **Function defined by an integral:** f(x)=∫₋₁ˣ t(eᵗ−1)(t−1)(t−2)³(t−3)⁵ dt → monotonicity from integrand sign. (JEE pattern.)
2. **Composite/absolute-value extrema:** count local maxima+minima of a non-differentiable f. (JEE 2025.)
3. **Tangent + Conic + Circle combined:** normal to parabola at P passes through centre of a given circle → find P. (JEE 2019.)
4. **ODE-defined curve + tangent/normal:** given dy/dx as function of x,y and a point, find curve then equation of tangent/normal. (JEE 2022.)
5. **Determinant max:** maximize a 3×3 determinant whose entries are trig functions of x. (JEE 2021.)
6. **Multi-constraint geometric optimization:** two solids, fixed combined surface area → minimize combined volume; or cone-in-sphere. (Exemplar Q31/34; BYJU'S JEE Q3.)

### 7D. JEE Advanced-flavoured traps & styles (flag for HOTS boxes)
- Inequality proofs using monotonicity: prove f(x) ≥ g(x) by showing h=f−g is increasing on interval.
- Maxima/minima with constraints without Lagrange (use substitution + AM-GM).
- Functions where second-derivative test fails → first test mandatory.
- Parametric and implicit curves; tangent crossing the curve (tangent not necessarily non-crossing).
- "Greatest/least integer" or functional-equation extrema (f(x+y)=f(x)f(y) type → JEE Main Q6 style).
- Optimization where optimum is at boundary of domain (links §05 vs §06).

---

## 08. WRITER CHECKLIST (per sub-chapter deliverable)
For EACH of §01–§06 a writer must produce:
- [ ] 2–3 drill examples (NCERT-style, solved).
- [ ] 1 MCQ + 1 Assertion-Reason (board Section A style).
- [ ] 1 VSA (2M) + 1 SA (3–4M).
- [ ] 1 LA (5M) for §03/§05/§06.
- [ ] 1 competency/case-study unit (Section E style, 4M, 2–3 sub-parts) — use framing ideas above.
- [ ] 1 HOTS / JEE-Mains-level problem (tag difficulty).
- [ ] A "common traps" callout box using the traps listed.
- [ ] For §07: a mixed Grand-Synthesis exercise set (6+ problems) pulling 2+ topics from the matrix.

**PYQ year tags to cite in solutions where applicable:** Delhi 2011, All India 2011C, Delhi 2014, All India 2014C, Delhi 2015, All India 2017, Delhi 2016, CBSE 2018 C, CBSE 2023 (2M rate-of-change), CBSE 2024-25 competency bank. JEE: 2015–2026 sample years noted throughout.
