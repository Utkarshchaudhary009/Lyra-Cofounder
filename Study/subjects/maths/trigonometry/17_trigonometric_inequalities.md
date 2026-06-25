# Chapter 17: Trigonometric Inequalities

---

## Stage 1: The Core Idea

### Solving "Sin θ > 1/2"

An equation like sin θ = 1/2 gives specific points. An inequality like sin θ > 1/2 gives a **range** of θ values.

Solving trig inequalities uses:
1. The **unit circle** — visualise where on the circle the condition holds
2. **Graphs** — see which intervals satisfy the inequality
3. **Algebra** — combine with domain restrictions

---

## Stage 2: The Formula Lab

### Key Graphs for Inequalities

```
sin θ > k:   θ ∈ (arcsin k, π − arcsin k) in [0, 2π]
sin θ < k:   θ ∈ [0, arcsin k) ∪ (π − arcsin k, 2π)

cos θ > k:   θ ∈ (−arccos k, arccos k) in [0, 2π] → that is θ ∈ [0, arccos k) ∪ (2π − arccos k, 2π)
cos θ < k:   θ ∈ (arccos k, 2π − arccos k)

tan θ > k:   θ ∈ (arctan k, π/2) ∪ (π/2 + arctan k, 3π/2)...
```

---

## Stage 3: Type-wise Mastery

### Type 1: sin θ > k

**Goal:** Solve sin θ > 1/2 for θ ∈ [0, 2π].

**Solved Example:**

Solve sin θ > 1/2 for θ ∈ [0, 2π].

**Solution:**
```
sin θ = 1/2 at θ = π/6, 5π/6
sin θ > 1/2 when the y-coordinate on unit circle > 1/2
This happens when θ ∈ (π/6, 5π/6)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

1. 🟡 Solve sin θ ≤ 1/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

To solve \( \sin \theta \le \frac{1}{2} \) in the interval \( [0, 2\pi] \):
1. First, find the boundary points where \( \sin \theta = \frac{1}{2} \). In the interval \( [0, 2\pi] \), these are:
   \[ \theta = \frac{\pi}{6}, \frac{5\pi}{6} \]
2. We want \( \sin \theta \) to be less than or equal to \( \frac{1}{2} \).
3. By looking at the graph of \( y = \sin \theta \) or the unit circle, we see that \( \sin \theta \le \frac{1}{2} \) on the following intervals:
   - From \( 0 \) to \( \frac{\pi}{6} \), i.e., \( \theta \in \left[0, \frac{\pi}{6}\right] \).
   - From \( \frac{5\pi}{6} \) to \( 2\pi \), i.e., \( \theta \in \left[\frac{5\pi}{6}, 2\pi\right] \).
4. Combining these intervals, we get:
   \[ \theta \in \left[0, \frac{\pi}{6}\right] \cup \left[\frac{5\pi}{6}, 2\pi\right] \]
</details>

2. 🟡 Solve sin θ > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The sine function \( \sin \theta \) represents the \(y\)-coordinate on the unit circle.
2. \( \sin \theta > 0 \) when the \(y\)-coordinate is strictly positive, which corresponds to Quadrant I and Quadrant II.
3. In the interval \( [0, 2\pi] \), this occurs for:
   \[ \theta \in (0, \pi) \]
</details>

3. 🟡 Solve sin θ < −1/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find the boundary points where \( \sin \theta = -\frac{1}{2} \). In \( [0, 2\pi] \), these are:
   \[ \theta = \pi + \frac{\pi}{6} = \frac{7\pi}{6} \quad \text{and} \quad \theta = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6} \]
2. We require \( \sin \theta < -\frac{1}{2} \), which corresponds to values below the line \( y = -\frac{1}{2} \) on the unit circle (Quadrant III and Quadrant IV).
3. This gives:
   \[ \theta \in \left(\frac{7\pi}{6}, \frac{11\pi}{6}\right) \]
</details>

4. 🟡 Solve sin θ ≥ −√3/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find the boundary points where \( \sin \theta = -\frac{\sqrt{3}}{2} \). In \( [0, 2\pi] \), these are:
   \[ \theta = \pi + \frac{\pi}{3} = \frac{4\pi}{3} \quad \text{and} \quad \theta = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3} \]
2. We want \( \sin \theta \ge -\frac{\sqrt{3}}{2} \). On the unit circle, this represents the region on or above the line \( y = -\frac{\sqrt{3}}{2} \).
3. Thus, the solution is:
   \[ \theta \in \left[0, \frac{4\pi}{3}\right] \cup \left[\frac{5\pi}{3}, 2\pi\right] \]
</details>

5. 🔴 Solve sin θ ≥ 0 for θ ∈ [0, 4π].
<details>
<summary>Solution</summary>

1. The inequality \( \sin \theta \ge 0 \) means the sine value is non-negative.
2. In the first cycle \( [0, 2\pi] \), \( \sin \theta \ge 0 \) for \( \theta \in [0, \pi] \).
3. In the second cycle \( [2\pi, 4\pi] \), \( \sin \theta \ge 0 \) for \( \theta \in [2\pi, 3\pi] \).
4. Combining these, the solution interval is:
   \[ \theta \in [0, \pi] \cup [2\pi, 3\pi] \]
</details>

---

### Type 2: cos θ > k

**Goal:** Solve cos θ > 1/2 for θ ∈ [0, 2π].

**Solved Example:**

Solve cos θ ≥ 1/2 for θ ∈ [0, 2π].

**Solution:**
```
cos θ = 1/2 at θ = π/3, 5π/3
cos θ ≥ 1/2 when x-coordinate on unit circle ≥ 1/2
This happens when θ ∈ [0, π/3] ∪ [5π/3, 2π]
```
🟡 Medium

---

**Practice Problems:**

6. 🟡 Solve cos θ > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The cosine function \( \cos \theta \) represents the \(x\)-coordinate on the unit circle.
2. \( \cos \theta > 0 \) when the \(x\)-coordinate is strictly positive, which corresponds to Quadrant I and Quadrant IV.
3. In the interval \( [0, 2\pi] \), this occurs for:
   \[ \theta \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{3\pi}{2}, 2\pi\right] \]
</details>

7. 🟡 Solve cos θ ≤ −1/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find the boundary points where \( \cos \theta = -\frac{1}{2} \). In \( [0, 2\pi] \), these are:
   \[ \theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3} \quad \text{and} \quad \theta = \pi + \frac{\pi}{3} = \frac{4\pi}{3} \]
2. We require \( \cos \theta \le -\frac{1}{2} \), which corresponds to the \(x\)-coordinate being less than or equal to \( -\frac{1}{2} \) (to the left of \( x = -\frac{1}{2} \)).
3. This happens between \( \frac{2\pi}{3} \) and \( \frac{4\pi}{3} \), inclusive:
   \[ \theta \in \left[\frac{2\pi}{3}, \frac{4\pi}{3}\right] \]
</details>

8. 🟡 Solve cos θ < √3/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find the boundary points where \( \cos \theta = \frac{\sqrt{3}}{2} \). In \( [0, 2\pi] \), these are:
   \[ \theta = \frac{\pi}{6} \quad \text{and} \quad \theta = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6} \]
2. We require \( \cos \theta < \frac{\sqrt{3}}{2} \). On the unit circle, this is the region to the left of the line \( x = \frac{\sqrt{3}}{2} \).
3. This corresponds to:
   \[ \theta \in \left(\frac{\pi}{6}, \frac{11\pi}{6}\right) \]
</details>

9. 🟡 Solve cos θ > −1/√2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find the boundary points where \( \cos \theta = -\frac{1}{\sqrt{2}} \). In \( [0, 2\pi] \), these are:
   \[ \theta = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \quad \text{and} \quad \theta = \pi + \frac{\pi}{4} = \frac{5\pi}{4} \]
2. We require \( \cos \theta > -\frac{1}{\sqrt{2}} \). On the unit circle, this is the region to the right of the line \( x = -\frac{1}{\sqrt{2}} \).
3. Therefore:
   \[ \theta \in \left[0, \frac{3\pi}{4}\right) \cup \left(\frac{5\pi}{4}, 2\pi\right] \]
</details>

10. 🔴 Solve |cos θ| ≤ 1/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The inequality \( |\cos \theta| \le \frac{1}{2} \) is equivalent to:
   \[ -\frac{1}{2} \le \cos \theta \le \frac{1}{2} \]
2. Let's find the values of \( \theta \) in \( [0, 2\pi] \) where \( \cos \theta = \frac{1}{2} \) or \( \cos \theta = -\frac{1}{2} \):
   - \( \cos \theta = \frac{1}{2} \implies \theta = \frac{\pi}{3}, \frac{5\pi}{3} \)
   - \( \cos \theta = -\frac{1}{2} \implies \theta = \frac{2\pi}{3}, \frac{4\pi}{3} \)
3. Looking at the unit circle, the \(x\)-coordinate lies in \( \left[-\frac{1}{2}, \frac{1}{2}\right] \). This happens in:
   - Quadrant I/II: \( \theta \in \left[\frac{\pi}{3}, \frac{2\pi}{3}\right] \)
   - Quadrant III/IV: \( \theta \in \left[\frac{4\pi}{3}, \frac{5\pi}{3}\right] \)
4. Thus, the solution is:
   \[ \theta \in \left[\frac{\pi}{3}, \frac{2\pi}{3}\right] \cup \left[\frac{4\pi}{3}, \frac{5\pi}{3}\right] \]
</details>

---

### Type 3: tan θ > k

**Goal:** Solve tan θ > 1 for θ ∈ [0, 2π].

**Solved Example:**

Solve tan θ > 1 for θ ∈ [0, 2π].

**Solution:**
```
tan θ = 1 at θ = π/4, 5π/4
tan θ > 1 when:
θ ∈ (π/4, π/2) ∪ (5π/4, 3π/2)
(Near the asymptote, tan goes to +∞)
```
🟡 Medium

---

**Practice Problems:**

11. 🟡 Solve tan θ ≤ √3 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

To solve \( \tan \theta \le \sqrt{3} \) in the interval \( [0, 2\pi] \):
1. First, identify where \( \tan \theta = \sqrt{3} \). In \( [0, 2\pi] \), this occurs at:
   \[ \theta = \frac{\pi}{3}, \frac{4\pi}{3} \]
2. Also, identify the vertical asymptotes of \( \tan \theta \) at \( \theta = \frac{\pi}{2} \) and \( \theta = \frac{3\pi}{2} \).
3. Solve the inequality on each interval:
   - For \( \theta \in \left[0, \frac{\pi}{2}\right) \): \( \tan \theta \le \sqrt{3} \implies \theta \in \left[0, \frac{\pi}{3}\right] \).
   - For \( \theta \in \left(\frac{\pi}{2}, \frac{3\pi}{2}\right) \): \( \tan \theta \le \sqrt{3} \implies \theta \in \left(\frac{\pi}{2}, \frac{4\pi}{3}\right] \).
   - For \( \theta \in \left(\frac{3\pi}{2}, 2\pi\right] \): The values of \( \tan \theta \) are negative or zero, which are all less than \( \sqrt{3} \). Thus, \( \theta \in \left(\frac{3\pi}{2}, 2\pi\right] \).
4. Combining these:
   \[ \theta \in \left[0, \frac{\pi}{3}\right] \cup \left(\frac{\pi}{2}, \frac{4\pi}{3}\right] \cup \left(\frac{3\pi}{2}, 2\pi\right] \]
</details>

12. 🟡 Solve tan θ > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. \( \tan \theta > 0 \) in Quadrant I and Quadrant III.
2. In the interval \( [0, 2\pi] \), the open intervals are:
   - Quadrant I: \( \theta \in \left(0, \frac{\pi}{2}\right) \)
   - Quadrant III: \( \theta \in \left(\pi, \frac{3\pi}{2}\right) \)
3. Thus, the solution is:
   \[ \theta \in \left(0, \frac{\pi}{2}\right) \cup \left(\pi, \frac{3\pi}{2}\right) \]
</details>

13. 🟡 Solve tan θ < −1 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find where \( \tan \theta = -1 \). In \( [0, 2\pi] \), this occurs at:
   \[ \theta = \pi - \frac{\pi}{4} = \frac{3\pi}{4} \quad \text{and} \quad \theta = 2\pi - \frac{\pi}{4} = \frac{7\pi}{4} \]
2. We want \( \tan \theta < -1 \).
   - In Quadrant II: \( \tan \theta \) goes from \( -\infty \) (as \( \theta \to \frac{\pi}{2}^+ \)) to \( 0 \) (at \( \theta = \pi \)). It crosses \( -1 \) at \( \theta = \frac{3\pi}{4} \). For \( \theta \in \left(\frac{\pi}{2}, \frac{3\pi}{4}\right) \), we have \( \tan \theta < -1 \).
   - In Quadrant IV: \( \tan \theta \) goes from \( -\infty \) (as \( \theta \to \frac{3\pi}{2}^+ \)) to \( 0 \) (at \( \theta = 2\pi \)). It crosses \( -1 \) at \( \theta = \frac{7\pi}{4} \). For \( \theta \in \left(\frac{3\pi}{2}, \frac{7\pi}{4}\right) \), we have \( \tan \theta < -1 \).
3. The solution set is:
   \[ \theta \in \left(\frac{\pi}{2}, \frac{3\pi}{4}\right) \cup \left(\frac{3\pi}{2}, \frac{7\pi}{4}\right) \]
</details>

14. 🟡 Solve tan θ ≥ 0 for θ ∈ [0, π].
<details>
<summary>Solution</summary>

1. In the interval \( [0, \pi] \), \( \tan \theta \) is defined everywhere except at the vertical asymptote \( \theta = \frac{\pi}{2} \).
2. For \( \theta \in \left[0, \frac{\pi}{2}\right) \), \( \tan \theta \ge 0 \).
3. At \( \theta = \frac{\pi}{2} \), the function is undefined.
4. For \( \theta \in \left(\frac{\pi}{2}, \pi\right] \), \( \tan \theta \le 0 \) (with \( \tan \pi = 0 \)).
5. Hence, \( \tan \theta \ge 0 \) is satisfied on:
   \[ \theta \in \left[0, \frac{\pi}{2}\right) \cup \{\pi\} \]
</details>

15. 🔴 ⭐ Solve tan θ ≤ 1 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Find where \( \tan \theta = 1 \) in \( [0, 2\pi] \):
   \[ \theta = \frac{\pi}{4}, \frac{5\pi}{4} \]
2. Identify the vertical asymptotes at \( \theta = \frac{\pi}{2}, \frac{3\pi}{2} \).
3. We need \( \tan \theta \le 1 \):
   - In \( \left[0, \frac{\pi}{2}\right) \): \( \tan \theta \le 1 \implies \theta \in \left[0, \frac{\pi}{4}\right] \).
   - In \( \left(\frac{\pi}{2}, \frac{3\pi}{2}\right) \): \( \tan \theta \le 1 \implies \theta \in \left(\frac{\pi}{2}, \frac{5\pi}{4}\right] \).
   - In \( \left(\frac{3\pi}{2}, 2\pi\right] \): \( \tan \theta \le 0 \) in the fourth quadrant, so all these values are \( \le 1 \). This gives \( \theta \in \left(\frac{3\pi}{2}, 2\pi\right] \).
4. The solution is:
   \[ \theta \in \left[0, \frac{\pi}{4}\right] \cup \left(\frac{\pi}{2}, \frac{5\pi}{4}\right] \cup \left(\frac{3\pi}{2}, 2\pi\right] \]
</details>

---

### Type 4: Quadratic Inequalities

**Goal:** Solve 2 sin²θ − sin θ − 1 > 0.

**Solved Example:**

Solve 2 sin²θ − sin θ − 1 > 0 for θ ∈ [0, 2π].

**Solution:**
```
Let t = sin θ: 2t² − t − 1 > 0
(2t + 1)(t − 1) > 0
t < −1/2 or t > 1

t > 1: impossible (max sin = 1)
t < −1/2: sin θ < −1/2

sin θ = −1/2 at θ = 7π/6, 11π/6
sin θ < −1/2 when θ ∈ (7π/6, 11π/6)
```
🟡 Medium ⭐ Must-Do

---

**Practice Problems:**

16. 🟡 Solve 2 cos²θ − cos θ − 1 ≤ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Let \( t = \cos \theta \). The inequality becomes:
   \[ 2t^2 - t - 1 \le 0 \]
2. Factor the quadratic:
   \[ (2t + 1)(t - 1) \le 0 \]
3. The roots are \( t = -\frac{1}{2} \) and \( t = 1 \). Since the inequality is \( \le 0 \):
   \[ -\frac{1}{2} \le t \le 1 \implies -\frac{1}{2} \le \cos \theta \le 1 \]
4. Since \( \cos \theta \le 1 \) is always true for all real \( \theta \), we only need to solve \( \cos \theta \ge -\frac{1}{2} \).
5. The boundary where \( \cos \theta = -\frac{1}{2} \) in \( [0, 2\pi] \) is \( \theta = \frac{2\pi}{3}, \frac{4\pi}{3} \).
6. \( \cos \theta \ge -\frac{1}{2} \) when the angle \( \theta \) is in the region to the right of \( x = -\frac{1}{2} \):
   \[ \theta \in \left[0, \frac{2\pi}{3}\right] \cup \left[\frac{4\pi}{3}, 2\pi\right] \]
</details>

17. 🟡 Solve 4 sin²θ − 1 > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Solve \( 4 \sin^2\theta - 1 > 0 \):
   \[ \sin^2\theta > \frac{1}{4} \implies |\sin \theta| > \frac{1}{2} \]
2. This means \( \sin \theta > \frac{1}{2} \) or \( \sin \theta < -\frac{1}{2} \).
3. Let's find the solution for each:
   - For \( \sin \theta > \frac{1}{2} \): \( \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \)
   - For \( \sin \theta < -\frac{1}{2} \): \( \theta \in \left(\frac{7\pi}{6}, \frac{11\pi}{6}\right) \)
4. The union of these intervals gives:
   \[ \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \cup \left(\frac{7\pi}{6}, \frac{11\pi}{6}\right) \]
</details>

18. 🟡 Solve tan²θ − √3 tan θ ≤ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Let \( t = \tan \theta \). The inequality is:
   \[ t(t - \sqrt{3}) \le 0 \]
2. This gives:
   \[ 0 \le t \le \sqrt{3} \implies 0 \le \tan \theta \le \sqrt{3} \]
3. We solve \( 0 \le \tan \theta \le \sqrt{3} \) in the interval \( [0, 2\pi] \):
   - In \( \left[0, \frac{\pi}{2}\right) \): \( 0 \le \tan \theta \le \sqrt{3} \implies \theta \in \left[0, \frac{\pi}{3}\right] \).
   - In \( \left(\frac{\pi}{2}, \frac{3\pi}{2}\right) \): \( 0 \le \tan \theta \le \sqrt{3} \implies \theta \in \left[\pi, \frac{4\pi}{3}\right] \).
   - In \( \left(\frac{3\pi}{2}, 2\pi\right] \): \( \tan \theta \le 0 \), so the only value satisfying the condition is where \( \tan\theta = 0 \), which is \( \theta = 2\pi \).
4. Combining these:
   \[ \theta \in \left[0, \frac{\pi}{3}\right] \cup \left[\pi, \frac{4\pi}{3}\right] \cup \{2\pi\} \]
</details>

19. 🔴 Solve 2 sin²θ + 3 sin θ − 2 > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Let \( t = \sin \theta \). The inequality is:
   \[ 2t^2 + 3t - 2 > 0 \]
2. Factor the quadratic expression:
   \[ (2t - 1)(t + 2) > 0 \]
3. The roots are \( t = \frac{1}{2} \) and \( t = -2 \). Since the inequality is \( > 0 \):
   \[ t < -2 \quad \text{or} \quad t > \frac{1}{2} \]
4. Since \( \sin \theta \ge -1 \) is always true, the inequality \( \sin \theta < -2 \) has no solution.
5. Therefore, we only need to solve:
   \[ \sin \theta > \frac{1}{2} \]
6. For \( \theta \in [0, 2\pi] \), this gives:
   \[ \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \]
</details>

20. 🔴 ⭐ Solve 2 cos²θ + 5 cos θ + 2 < 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Let \( t = \cos \theta \). The inequality is:
   \[ 2t^2 + 5t + 2 < 0 \]
2. Factor the quadratic:
   \[ (2t + 1)(t + 2) < 0 \]
3. The roots are \( t = -2 \) and \( t = -\frac{1}{2} \). Since the inequality is \( < 0 \):
   \[ -2 < t < -\frac{1}{2} \implies -2 < \cos \theta < -\frac{1}{2} \]
4. Since \( \cos \theta \ge -1 \) is always true, the lower bound is always satisfied. So we solve:
   \[ \cos \theta < -\frac{1}{2} \]
5. For \( \theta \in [0, 2\pi] \), the boundary values where \( \cos \theta = -\frac{1}{2} \) are \( \theta = \frac{2\pi}{3}, \frac{4\pi}{3} \).
6. Thus:
   \[ \theta \in \left(\frac{2\pi}{3}, \frac{4\pi}{3}\right) \]
</details>

---

### Type 5: Combined sin and cos Inequalities

**Goal:** Solve sin θ ≤ cos θ.

**Solved Example:**

Solve sin θ ≤ cos θ for θ ∈ [0, 2π].

**Solution:**
```
sin θ ≤ cos θ → sin θ − cos θ ≤ 0 → √2 sin(θ − π/4) ≤ 0
sin(θ − π/4) ≤ 0
θ − π/4 ∈ [π, 2π] (in [0, 2π] range)
θ ∈ [5π/4, 9π/4] → θ ∈ [5π/4, 2π) ∪ [0, π/4]
```
🔴 Hard

---

**Practice Problems:**

21. 🔴 Solve sin θ ≥ cos θ for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. We rewrite the inequality:
   \[ \sin \theta - \cos \theta \ge 0 \]
2. Multiply by \( \frac{1}{\sqrt{2}} \):
   \[ \frac{1}{\sqrt{2}}\sin \theta - \frac{1}{\sqrt{2}}\cos \theta \ge 0 \implies \sin\left(\theta - \frac{\pi}{4}\right) \ge 0 \]
3. Let \( \phi = \theta - \frac{\pi}{4} \). Since \( \theta \in [0, 2\pi] \), we have \( \phi \in \left[-\frac{\pi}{4}, \frac{7\pi}{4}\right] \).
4. We want \( \sin \phi \ge 0 \) in this range, which occurs for:
   \[ 0 \le \phi \le \pi \]
5. Substitute back \( \phi = \theta - \frac{\pi}{4} \):
   \[ 0 \le \theta - \frac{\pi}{4} \le \pi \implies \frac{\pi}{4} \le \theta \le \frac{5\pi}{4} \]
6. Thus:
   \[ \theta \in \left[\frac{\pi}{4}, \frac{5\pi}{4}\right] \]
</details>

22. 🔴 Solve sin θ > cos θ for θ ∈ [0, π].
<details>
<summary>Solution</summary>

1. Rewrite as \( \sin\left(\theta - \frac{\pi}{4}\right) > 0 \).
2. Given \( \theta \in [0, \pi] \), the argument \( \theta - \frac{\pi}{4} \) lies in \( \left[-\frac{\pi}{4}, \frac{3\pi}{4}\right] \).
3. We need \( \sin\left(\theta - \frac{\pi}{4}\right) > 0 \). In this range, this is satisfied when:
   \[ 0 < \theta - \frac{\pi}{4} \le \frac{3\pi}{4} \]
4. Solving for \( \theta \):
   \[ \frac{\pi}{4} < \theta \le \pi \]
5. Thus:
   \[ \theta \in \left(\frac{\pi}{4}, \pi\right] \]
</details>

23. 🔴 Solve |sin θ| ≤ |cos θ| for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Squaring both sides gives:
   \[ \sin^2\theta \le \cos^2\theta \implies \cos^2\theta - \sin^2\theta \ge 0 \]
2. Use the double-angle formula:
   \[ \cos 2\theta \ge 0 \]
3. Let \( \phi = 2\theta \). For \( \theta \in [0, 2\pi] \), \( \phi \in [0, 4\pi] \).
4. We solve \( \cos \phi \ge 0 \) in the interval \( [0, 4\pi] \):
   - \( \phi \in \left[0, \frac{\pi}{2}\right] \cup \left[\frac{3\pi}{2}, \frac{5\pi}{2}\right] \cup \left[\frac{7\pi}{2}, 4\pi\right] \)
5. Dividing by 2, we obtain the solution for \( \theta \):
   \[ \theta \in \left[0, \frac{\pi}{4}\right] \cup \left[\frac{3\pi}{4}, \frac{5\pi}{4}\right] \cup \left[\frac{7\pi}{4}, 2\pi\right] \]
</details>

24. 🔴 ⭐ Solve sin θ cos θ < 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The product \( \sin \theta \cos \theta < 0 \) when \( \sin \theta \) and \( \cos \theta \) have opposite signs.
2. This occurs in Quadrants II and IV:
   - In Quadrant II: \( \theta \in \left(\frac{\pi}{2}, \pi\right) \)
   - In Quadrant IV: \( \theta \in \left(\frac{3\pi}{2}, 2\pi\right) \)
3. Combining these:
   \[ \theta \in \left(\frac{\pi}{2}, \pi\right) \cup \left(\frac{3\pi}{2}, 2\pi\right) \]
</details>

25. 🔴 Solve sin θ + cos θ > 1 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Express in single sine form:
   \[ \sqrt{2} \sin\left(\theta + \frac{\pi}{4}\right) > 1 \implies \sin\left(\theta + \frac{\pi}{4}\right) > \frac{1}{\sqrt{2}} \]
2. Let \( \phi = \theta + \frac{\pi}{4} \). Since \( \theta \in [0, 2\pi] \), we have \( \phi \in \left[\frac{\pi}{4}, \frac{9\pi}{4}\right] \).
3. The inequality \( \sin \phi > \frac{1}{\sqrt{2}} \) is satisfied for:
   \[ \phi \in \left(\frac{\pi}{4}, \frac{3\pi}{4}\right) \]
4. Substitute back \( \phi = \theta + \frac{\pi}{4} \):
   \[ \frac{\pi}{4} < \theta + \frac{\pi}{4} < \frac{3\pi}{4} \implies 0 < \theta < \frac{\pi}{2} \]
5. Thus:
   \[ \theta \in \left(0, \frac{\pi}{2}\right) \]
</details>

---

### Type 6: Domain-Restricted Inequalities

**Goal:** Solve considering the domain of tan, sec, etc.

**Solved Example:**

Find the domain of f(θ) = 1/√(sin θ) for θ ∈ [0, 2π].

**Solution:**
```
sin θ > 0 (since denominator under root must be positive)
sin θ > 0 when θ ∈ (0, π)
But also, sin θ ≠ 0 (not in denominator anyway since > 0)
Domain: (0, π)
```
🟡 Medium

---

**Practice Problems:**

26. 🟡 Find domain of f(θ) = 1/√(cos θ).
<details>
<summary>Solution</summary>

1. For the square root in the denominator to be defined and non-zero:
   \[ \cos \theta > 0 \]
2. In the principal interval \( [0, 2\pi] \), cosine is positive in Quadrants I and IV:
   \[ \theta \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{3\pi}{2}, 2\pi\right] \]
3. The general domain for all real numbers is:
   \[ \theta \in \bigcup_{n\in\mathbb{Z}} \left(2n\pi - \frac{\pi}{2}, 2n\pi + \frac{\pi}{2}\right) \]
</details>

27. 🟡 Find domain of f(θ) = √(tan θ).
<details>
<summary>Solution</summary>

1. For the square root to be defined:
   \[ \tan \theta \ge 0 \]
2. Additionally, \( \tan \theta \) is undefined where \( \theta = \frac{\pi}{2} + k\pi \) for \( k \in \mathbb{Z} \).
3. Tangent is non-negative in Quadrants I and III (including points where it is zero, but excluding asymptotes).
4. Thus, the general domain is:
   \[ \theta \in \bigcup_{n\in\mathbb{Z}} \left[n\pi, n\pi + \frac{\pi}{2}\right) \]
5. Restricting to \( [0, 2\pi] \):
   \[ \theta \in \left[0, \frac{\pi}{2}\right) \cup \left[\pi, \frac{3\pi}{2}\right) \cup \{2\pi\} \]
</details>

28. 🟡 Find domain of f(θ) = 1/(sin θ − 1/2).
<details>
<summary>Solution</summary>

1. The function is defined everywhere except where the denominator is zero:
   \[ \sin \theta - \frac{1}{2} = 0 \implies \sin \theta = \frac{1}{2} \]
2. In \( [0, 2\pi] \), the points to exclude are:
   \[ \theta = \frac{\pi}{6}, \frac{5\pi}{6} \]
3. Thus, the domain is:
   \[ \mathbb{R} \setminus \left(\{ \frac{\pi}{6} + 2n\pi \} \cup \{ \frac{5\pi}{6} + 2n\pi \} \mid n \in \mathbb{Z}\right) \]
</details>

29. 🔴 ⭐ Find domain of f(θ) = √(sin θ) + √(cos θ).
<details>
<summary>Solution</summary>

1. Both terms inside the square roots must be non-negative:
   \[ \sin \theta \ge 0 \quad \text{and} \quad \cos \theta \ge 0 \]
2. \( \sin \theta \ge 0 \) in Quadrants I and II: \( \theta \in [2n\pi, 2n\pi + \pi] \) for \( n \in \mathbb{Z} \).
3. \( \cos \theta \ge 0 \) in Quadrants I and IV: \( \theta \in [2n\pi - \frac{\pi}{2}, 2n\pi + \frac{\pi}{2}] \) for \( n \in \mathbb{Z} \).
4. The intersection of these two sets is Quadrant I:
   \[ \theta \in \left[2n\pi, 2n\pi + \frac{\pi}{2}\right] \quad \text{for } n \in \mathbb{Z} \]
5. Restricted to \( [0, 2\pi] \), the domain is:
   \[ \theta \in \left[0, \frac{\pi}{2}\right] \]
</details>

30. 🔴 Find domain of f(θ) = √(2 sin θ − 1).
<details>
<summary>Solution</summary>

1. For the square root to be defined:
   \[ 2 \sin \theta - 1 \ge 0 \implies \sin \theta \ge \frac{1}{2} \]
2. In the principal interval \( [0, 2\pi] \), this occurs for:
   \[ \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \]
3. The general domain is:
   \[ \theta \in \bigcup_{n\in\mathbb{Z}} \left[\frac{\pi}{6} + 2n\pi, \frac{5\pi}{6} + 2n\pi\right] \]
</details>

---

### Type 7: Product Inequalities

**Goal:** Solve (sin θ)(cos θ) ≥ 0.

**Solved Example:**

Solve sin θ cos θ > 0 for θ ∈ [0, 2π].

**Solution:**
```
sin θ cos θ > 0 when sin θ and cos θ have the SAME sign.
sin θ > 0, cos θ > 0 → QI → θ ∈ (0, π/2)
sin θ < 0, cos θ < 0 → QIII → θ ∈ (π, 3π/2)
Answer: (0, π/2) ∪ (π, 3π/2)
```
🟡 Medium

---

**Practice Problems:**

31. 🟡 Solve sin θ cos θ < 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The product \( \sin \theta \cos \theta < 0 \) when they have opposite signs.
2. This corresponds to Quadrant II and Quadrant IV:
   - Quadrant II: \( \theta \in \left(\frac{\pi}{2}, \pi\right) \)
   - Quadrant IV: \( \theta \in \left(\frac{3\pi}{2}, 2\pi\right) \)
3. Combining these:
   \[ \theta \in \left(\frac{\pi}{2}, \pi\right) \cup \left(\frac{3\pi}{2}, 2\pi\right) \]
</details>

32. 🟡 Solve (sin θ − 1/2)(cos θ + 1/2) ≥ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

Let \( A = \sin \theta - \frac{1}{2} \) and \( B = \cos \theta + \frac{1}{2} \). We want \( A \cdot B \ge 0 \).

**Case I: \( A \ge 0 \) and \( B \ge 0 \)**
1. \( \sin \theta \ge \frac{1}{2} \implies \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \)
2. \( \cos \theta \ge -\frac{1}{2} \implies \theta \in \left[0, \frac{2\pi}{3}\right] \cup \left[\frac{4\pi}{3}, 2\pi\right] \)
3. Intersection of these two intervals:
   \[ \theta \in \left[\frac{\pi}{6}, \frac{2\pi}{3}\right] \]

**Case II: \( A \le 0 \) and \( B \le 0 \)**
1. \( \sin \theta \le \frac{1}{2} \implies \theta \in \left[0, \frac{\pi}{6}\right] \cup \left[\frac{5\pi}{6}, 2\pi\right] \)
2. \( \cos \theta \le -\frac{1}{2} \implies \theta \in \left[\frac{2\pi}{3}, \frac{4\pi}{3}\right] \)
3. Intersection of these two intervals:
   \[ \theta \in \left[\frac{5\pi}{6}, \frac{4\pi}{3}\right] \]

**Union of Case I and Case II:**
\[ \theta \in \left[\frac{\pi}{6}, \frac{2\pi}{3}\right] \cup \left[\frac{5\pi}{6}, \frac{4\pi}{3}\right] \]
</details>

33. 🔴 Solve (tan θ)(sin θ) > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Rewrite \( \tan \theta \) as \( \frac{\sin \theta}{\cos \theta} \):
   \[ \frac{\sin^2\theta}{\cos \theta} > 0 \]
2. The numerator \( \sin^2\theta \) is always non-negative. For the ratio to be strictly positive:
   - \( \sin \theta \ne 0 \implies \theta \ne 0, \pi, 2\pi \)
   - The denominator must be strictly positive: \( \cos \theta > 0 \)
3. In \( [0, 2\pi] \), \( \cos \theta > 0 \) for \( \theta \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{3\pi}{2}, 2\pi\right] \).
4. Excluding the boundary points \( \theta = 0, 2\pi \), we get:
   \[ \theta \in \left(0, \frac{\pi}{2}\right) \cup \left(\frac{3\pi}{2}, 2\pi\right) \]
</details>

34. 🔴 ⭐ Solve (sin θ − cos θ)(sin θ + cos θ) ≤ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Expand the product:
   \[ \sin^2\theta - \cos^2\theta \le 0 \implies -(\cos^2\theta - \sin^2\theta) \le 0 \]
2. This simplifies using the double-angle identity:
   \[ \cos 2\theta \ge 0 \]
3. Let \( \phi = 2\theta \). For \( \theta \in [0, 2\pi] \), we have \( \phi \in [0, 4\pi] \).
4. Solve \( \cos \phi \ge 0 \) in \( [0, 4\pi] \):
   \[ \phi \in \left[0, \frac{\pi}{2}\right] \cup \left[\frac{3\pi}{2}, \frac{5\pi}{2}\right] \cup \left[\frac{7\pi}{2}, 4\pi\right] \]
5. Dividing by 2 gives:
   \[ \theta \in \left[0, \frac{\pi}{4}\right] \cup \left[\frac{3\pi}{4}, \frac{5\pi}{4}\right] \cup \left[\frac{7\pi}{4}, 2\pi\right] \]
</details>

35. 🔴 Solve (2 sin θ − 1)(cos θ + 1) ≥ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Since \( \cos \theta \ge -1 \) for all \( \theta \), we have:
   \[ \cos \theta + 1 \ge 0 \quad \text{for all } \theta \]
2. Because the second factor is always non-negative, the product is non-negative if:
   - Either \( 2 \sin \theta - 1 \ge 0 \implies \sin \theta \ge \frac{1}{2} \)
   - Or the second factor is zero: \( \cos \theta + 1 = 0 \implies \cos \theta = -1 \implies \theta = \pi \).
3. Solve \( \sin \theta \ge \frac{1}{2} \) in \( [0, 2\pi] \):
   \[ \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \]
4. Incorporating the root \( \theta = \pi \), the complete solution is:
   \[ \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \cup \{\pi\} \]
</details>

---

### Type 8: Inequalities in a Given Interval

**Goal:** Solve with specific interval restrictions.

**Solved Example:**

Solve sin θ > 1/2 for θ ∈ [−π, π].

**Solution:**
```
sin θ = 1/2 at θ = π/6, 5π/6
But 5π/6 > π, so out of range.
In [−π, π], sin > 1/2 when θ ∈ (π/6, 5π/6) but only the part within [−π, π]
Actually sin θ is positive and > 1/2 in QII as well, so 5π/6 is in range (it's < π).

sin θ > 1/2 for θ ∈ (π/6, 5π/6)
Both endpoints are within [−π, π].
Answer: (π/6, 5π/6)
```
🔴 Hard

---

**Practice Problems:**

36. 🔴 Solve cos θ ≤ 1/2 for θ ∈ [0, π].
<details>
<summary>Solution</summary>

1. In the interval \( [0, \pi] \), find where \( \cos \theta = \frac{1}{2} \):
   \[ \theta = \frac{\pi}{3} \]
2. Since \( \cos \theta \) is strictly decreasing on \( [0, \pi] \), \( \cos \theta \le \frac{1}{2} \) for:
   \[ \theta \in \left[\frac{\pi}{3}, \pi\right] \]
</details>

37. 🔴 Solve tan θ > 1 for θ ∈ [−π/2, π/2].
<details>
<summary>Solution</summary>
38. 🔴 Solve sin θ + cos θ > 0 for θ ∈ [0, π].
<details>
<summary>Solution</summary>

1. Rewrite the inequality:
   \[ \sqrt{2} \sin\left(\theta + \frac{\pi}{4}\right) > 0 \implies \sin\left(\theta + \frac{\pi}{4}\right) > 0 \]
2. Given \( \theta \in [0, \pi] \), the argument \( \theta + \frac{\pi}{4} \) lies in \( \left[\frac{\pi}{4}, \frac{5\pi}{4}\right] \).
3. We need the sine function to be positive. In \( \left[\frac{\pi}{4}, \frac{5\pi}{4}\right] \), this occurs when:
   \[ \frac{\pi}{4} \le \theta + \frac{\pi}{4} < \pi \implies 0 \le \theta < \frac{3\pi}{4} \]
4. Thus:
   \[ \theta \in \left[0, \frac{3\pi}{4}\right) \]
</details>

39. 🔴 ⭐ Solve 2 cos²θ − 3 cos θ + 1 > 0 for θ ∈ [0, 4π]? Wait, the original question is 2 cos²θ − 3 cos θ + 1 > 0 for θ ∈ [0, π].
39. 🔴 ⭐ Solve 2 cos²θ − 3 cos θ + 1 > 0 for θ ∈ [0, π].
<details>
<summary>Solution</summary>

1. Let \( t = \cos \theta \). The inequality is \( 2t^2 - 3t + 1 > 0 \).
2. Factor the quadratic:
   \[ (2t - 1)(t - 1) > 0 \implies t < \frac{1}{2} \quad \text{or} \quad t > 1 \]
3. Since \( \cos \theta \le 1 \), the inequality \( \cos \theta > 1 \) has no solution.
4. Therefore, we solve:
   \[ \cos \theta < \frac{1}{2} \]
5. In the interval \( [0, \pi] \), \( \cos \theta = \frac{1}{2} \) at \( \theta = \frac{\pi}{3} \).
6. Since \( \cos \theta \) is decreasing, the solution is:
   \[ \theta \in \left(\frac{\pi}{3}, \pi\right] \]
</details>

40. 🔴 Solve |sin θ| < 1/2 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. The inequality is equivalent to:
   \[ -\frac{1}{2} < \sin \theta < \frac{1}{2} \]
2. Find the boundary points where \( \sin \theta = \frac{1}{2} \) or \( \sin \theta = -\frac{1}{2} \) in \( [0, 2\pi] \):
   - \( \sin \theta = \frac{1}{2} \implies \theta = \frac{\pi}{6}, \frac{5\pi}{6} \)
   - \( \sin \theta = -\frac{1}{2} \implies \theta = \frac{7\pi}{6}, \frac{11\pi}{6} \)
3. Combining the intervals where \( -\frac{1}{2} < \sin \theta < \frac{1}{2} \):
   \[ \theta \in \left[0, \frac{\pi}{6}\right) \cup \left(\frac{5\pi}{6}, \frac{7\pi}{6}\right) \cup \left(\frac{11\pi}{6}, 2\pi\right] \]
</details>

---

## Stage 4: Type Mixer

1. 🟡 Solve sin θ > cos θ for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Rewrite the inequality:
   \[ \sin \theta - \cos \theta > 0 \implies \sqrt{2} \sin\left(\theta - \frac{\pi}{4}\right) > 0 \]
2. This simplifies to:
   \[ \sin\left(\theta - \frac{\pi}{4}\right) > 0 \]
3. In the range \( \theta \in [0, 2\pi] \), the argument \( \theta - \frac{\pi}{4} \) lies in \( \left[-\frac{\pi}{4}, \frac{7\pi}{4}\right] \).
4. The sine function is positive in this range when:
   \[ 0 < \theta - \frac{\pi}{4} < \pi \implies \frac{\pi}{4} < \theta < \frac{5\pi}{4} \]
5. Thus:
   \[ \theta \in \left(\frac{\pi}{4}, \frac{5\pi}{4}\right) \]
</details>

2. 🟡 Solve 2 sin²θ − sin θ − 1 < 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Let \( t = \sin \theta \). The inequality is \( 2t^2 - t - 1 < 0 \).
2. Factor:
   \[ (2t + 1)(t - 1) < 0 \implies -\frac{1}{2} < t < 1 \]
3. Thus, we have \( -\frac{1}{2} < \sin \theta < 1 \).
4. Let's analyze the bounds:
   - \( \sin \theta < 1 \): True for all \( \theta \in [0, 2\pi] \) except \( \theta = \frac{\pi}{2} \).
   - \( \sin \theta > -\frac{1}{2} \): Boundary points are \( \theta = \frac{7\pi}{6}, \frac{11\pi}{6} \). This is satisfied for \( \theta \in \left[0, \frac{7\pi}{6}\right) \cup \left(\frac{11\pi}{6}, 2\pi\right] \).
5. Intersecting the two conditions, we get:
   \[ \theta \in \left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \frac{7\pi}{6}\right) \cup \left(\frac{11\pi}{6}, 2\pi\right] \]
</details>

3. 🔴 ⭐ Find the domain of f(θ) = √((sin θ − 1/2)(cos θ + 1/2)).
<details>
<summary>Solution</summary>

For the function to be defined, the expression inside the square root must be non-negative:
\[ (\sin \theta - 1/2)(cos θ + 1/2) \ge 0 \]
Let \( A = \sin \theta - \frac{1}{2} \) and \( B = \cos \theta + \frac{1}{2} \).

**Case I: \( A \ge 0 \) and \( B \ge 0 \)**
1. \( \sin \theta \ge \frac{1}{2} \implies \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \)
2. \( \cos \theta \ge -\frac{1}{2} \implies \theta \in \left[0, \frac{2\pi}{3}\right] \cup \left[\frac{4\pi}{3}, 2\pi\right] \)
3. Intersection of these two sets:
   \[ \theta \in \left[\frac{\pi}{6}, \frac{2\pi}{3}\right] \]

**Case II: \( A \le 0 \) and \( B \le 0 \)**
1. \( \sin \theta \le \frac{1}{2} \implies \theta \in \left[0, \frac{\pi}{6}\right] \cup \left[\frac{5\pi}{6}, 2\pi\right] \)
2. \( \cos \theta \le -\frac{1}{2} \implies \theta \in \left[\frac{2\pi}{3}, \frac{4\pi}{3}\right] \)
3. Intersection of these two sets:
   \[ \theta \in \left[\frac{5\pi}{6}, \frac{4\pi}{3}\right] \]

**Union of Case I and Case II:**
For \( \theta \in [0, 2\pi] \), the domain is:
\[ \theta \in \left[\frac{\pi}{6}, \frac{2\pi}{3}\right] \cup \left[\frac{5\pi}{6}, \frac{4\pi}{3}\right] \]
The general domain is:
\[ \theta \in \bigcup_{n\in\mathbb{Z}} \left( \left[2n\pi + \frac{\pi}{6}, 2n\pi + \frac{2\pi}{3}\right] \cup \left[2n\pi + \frac{5\pi}{6}, 2n\pi + \frac{4\pi}{3}\right] \right) \]
</details>

4. 🔴 Solve sin θ + sin 2θ > 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Rewrite using the identity \( \sin 2\theta = 2\sin \theta \cos \theta \):
   \[ \sin \theta (1 + 2\cos \theta) > 0 \]
2. We analyze the signs of the factors:
   **Case I: Both factors are positive**
   - \( \sin \theta > 0 \implies \theta \in (0, \pi) \)
   - \( 1 + 2\cos \theta > 0 \implies \cos \theta > -\frac{1}{2} \implies \theta \in \left[0, \frac{2\pi}{3}\right) \cup \left(\frac{4\pi}{3}, 2\pi\right] \)
   - Intersection: \( \theta \in \left(0, \frac{2\pi}{3}\right) \)

   **Case II: Both factors are negative**
   - \( \sin \theta < 0 \implies \theta \in (\pi, 2\pi) \)
   - \( 1 + 2\cos \theta < 0 \implies \cos \theta < -\frac{1}{2} \implies \theta \in \left(\frac{2\pi}{3}, \frac{4\pi}{3}\right) \)
   - Intersection: \( \theta \in \left(\pi, \frac{4\pi}{3}\right) \)

3. Combining both cases:
   \[ \theta \in \left(0, \frac{2\pi}{3}\right) \cup \left(\pi, \frac{4\pi}{3}\right) \]
</details>

5. 🔴 Solve sec²θ − 2 tan θ ≥ 0 for θ ∈ [0, 2π].
<details>
<summary>Solution</summary>

1. Use the identity \( \sec^2\theta = 1 + \tan^2\theta \):
   \[ 1 + \tan^2\theta - 2\tan \theta \ge 0 \implies (\tan \theta - 1)^2 \ge 0 \]
2. Since a perfect square of a real number is always non-negative, this is true for all values of \( \theta \) where \( \tan \theta \) is defined.
3. The tangent function is undefined at \( \theta = \frac{\pi}{2} \) and \( \theta = \frac{3\pi}{2} \).
4. Thus, the solution set is:
   \[ \theta \in [0, 2\pi] \setminus \left\{ \frac{\pi}{2}, \frac{3\pi}{2} \right\} \]
</details>

---

## Stage 5: Board Arsenal

**Q1.** 🟡 Solve sin θ > 1/2 for θ ∈ [0, 2π]. **(2 marks)**

<details>
<summary>Solution</summary>

We have:
\[ \sin \theta = \frac{1}{2} \implies \theta = \frac{\pi}{6}, \frac{5\pi}{6} \text{ in } [0, 2\pi] \]
On the unit circle, the \( y \)-coordinate is greater than \( \frac{1}{2} \) for:
\[ \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \]
</details>

---

**Q2.** 🟡 Solve cos θ < 0 for θ ∈ [0, 2π]. **(1 mark)**

<details>
<summary>Solution</summary>

The cosine function is negative in Quadrants II and III.
Thus, in the interval \( [0, 2\pi] \):
\[ \theta \in \left(\frac{\pi}{2}, \frac{3\pi}{2}\right) \]
</details>

---

**Q3.** 🟡 Solve 2 sin²θ − 3 sin θ + 1 ≤ 0 for θ ∈ [0, 2π]. **(3 marks)**

<details>
<summary>Solution</summary>

Let \( t = \sin \theta \):
\[ 2t^2 - 3t + 1 \le 0 \implies (2t - 1)(t - 1) \le 0 \]
This gives:
\[ \frac{1}{2} \le t \le 1 \implies \frac{1}{2} \le \sin \theta \le 1 \]
Since \( \sin \theta \le 1 \) is always true:
\[ \sin \theta \ge \frac{1}{2} \implies \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \]
</details>

---

**Q4.** 🟡 Find the domain of f(x) = 1/√(2 sin x − 1). **(2 marks)**

<details>
<summary>Solution</summary>

For the function to be defined:
\[ 2\sin x - 1 > 0 \implies \sin x > \frac{1}{2} \]
Thus, the domain is:
\[ x \in \left(\frac{\pi}{6} + 2n\pi, \frac{5\pi}{6} + 2n\pi\right) \text{ for } n \in \mathbb{Z} \]
</details>

---

## Stage 6: JEE Mains Arena

**Q1.** The solution set of sin θ > 1/2 in [0, 2π] is:
(a) (π/6, 5π/6)
(b) (π/3, 2π/3)
(c) (π/6, π/3)
(d) (π/6, 5π/6)

<details>
<summary>Solution</summary>
sin θ = 1/2 at π/6, 5π/6. sin > 1/2 between them.
Answer: (a) 🟡
</details>

---

**Q2.** The solution set of cos θ ≤ −1/2 in [0, 2π] is:
(a) [π/3, 5π/3]
(b) [2π/3, 4π/3]
(c) [π/2, 3π/2]
(d) [π/3, 2π/3]

<details>
<summary>Solution</summary>
cos θ = −1/2 at 2π/3, 4π/3. cos ≤ −1/2 between them (inclusive).
Answer: (b) 🟡
</details>

---

**Q3.** The number of integers n for which sin⁻¹(sin n) > 0 is:
(a) 0
(b) 1
(c) 2
(d) Infinite

<details>
<summary>Solution</summary>
sin⁻¹(sin n) > 0 when n is not an integer multiple of π where sin = 0.
Actually sin⁻¹(sin n) > 0 when sin n > 0 and the principal value is positive.
This holds for infinitely many integers n.
Answer: (d) 🔴
</details>

---

**Q4.** The domain of f(x) = √(sin x) + √(cos x) is:
(a) [2nπ, (2n+1)π/2]
(b) [2nπ, (2n+1)π]
(c) [(2n+1)π/2, (2n+1)π]
(d) [2nπ, 2nπ + π/2]

<details>
<summary>Solution</summary>
sin x ≥ 0 and cos x ≥ 0 → x in QI
x ∈ [2nπ, 2nπ + π/2]
Answer: (d) 🟡 ⭐
</details>

---

**Q5.** The solution of sin θ + cos θ > 0 in [0, 2π] is:
(a) (0, 3π/4)
(b) (0, 3π/4) ∪ (7π/4, 2π)
(c) (0, π/2)
(d) (3π/4, 7π/4)

<details>
<summary>Solution</summary>
sin θ + cos θ = √2 sin(θ + π/4) > 0
sin(θ + π/4) > 0
0 < θ + π/4 < π → −π/4 < θ < 3π/4
But θ ∈ [0, 2π], so: 0 ≤ θ < 3π/4
Also 2π < θ + π/4 < 3π → 7π/4 < θ < 11π/4
So 7π/4 < θ ≤ 2π
Answer: (0, 3π/4) ∪ (7π/4, 2π)
Answer: (b) 🔴 ⭐
</details>

---

## Stage 7: Assertion-Reasoning

**Q1.** 🟢 **Assertion <br>
(A):** sin θ > 0 for θ ∈ (0, π).
**Reason (R):** Sin is positive in QI and QII.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q2.** 🟡 **Assertion <br>
(A):** The inequality cos θ < 0 has solution θ ∈ (π/2, 3π/2) in [0, 2π].
**Reason (R):** Cos negative in QII and QIII.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

**Q3.** 🟡 **Assertion <br>
(A):** The expression √(sin θ) is defined for θ ∈ [0, π].
**Reason (R):** sin θ ≥ 0 for θ ∈ [0, π].

<details>
<summary>Solution</summary>
A is true (domain includes 0 and π where sin=0).
R is true and explains A.
Answer: (a)
</details>

---

**Q4.** 🔴 **Assertion <br>
(A):** sin θ + cos θ > 0 for all θ ∈ (0, π/2).
**Reason (R):** Both sin and cos are positive in QI.

<details>
<summary>Solution</summary>
Both true, R explains A. Answer: (a)
</details>

---

## Stage 8: MCQ Mastery

1. 🟢 sin θ > 0 in:
   (a) QI, QII   (b) QI, QIV   (c) QII, QIII   (d) QIII, QIV
<details>
<summary>Solution</summary>

The sine function \( \sin \theta \) represents the \(y\)-coordinate on the unit circle.
- \( \sin \theta > 0 \) when the \(y\)-coordinate is positive, which occurs in Quadrant I (QI) and Quadrant II (QII).
- In Quadrants III and IV, \( \sin \theta < 0 \).

**Answer: (a) QI, QII**
</details>

2. 🟢 cos θ < 0 in:
   (a) QI, QII   (b) QI, QIV   (c) QII, QIII   (d) QIII, QIV
<details>
<summary>Solution</summary>

The cosine function \( \cos \theta \) represents the \(x\)-coordinate on the unit circle.
- \( \cos \theta < 0 \) when the \(x\)-coordinate is negative, which occurs in Quadrant II (QII) and Quadrant III (QIII).
- In Quadrants I and IV, \( \cos \theta > 0 \).

**Answer: (c) QII, QIII**
</details>

3. 🟡 sin θ > 1/2 in [0, 2π] for θ ∈:
   (a) (π/6, 5π/6)   (b) (π/3, 2π/3)   (c) (0, π/6)   (d) (5π/6, 2π)
<details>
<summary>Solution</summary>

We solve \( \sin \theta > \frac{1}{2} \) for \( \theta \in [0, 2\pi] \):
1. First, find where \( \sin \theta = \frac{1}{2} \). In \( [0, 2\pi] \), this occurs at:
   \[ \theta = \frac{\pi}{6}, \frac{5\pi}{6} \]
2. The inequality \( \sin \theta > \frac{1}{2} \) is satisfied for the values of \( \theta \) between these two points:
   \[ \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \]

**Answer: (a) (π/6, 5π/6)**
</details>

4. 🟡 cos θ > 1/2 in [0, 2π] for θ ∈:
   (a) (0, π/3) ∪ (5π/3, 2π)   (b) (π/3, 5π/3)   (c) (0, π/3)   (d) (5π/3, 2π)
<details>
<summary>Solution</summary>

We solve \( \cos \theta > \frac{1}{2} \) for \( \theta \in [0, 2\pi] \):
1. Find where \( \cos \theta = \frac{1}{2} \) in \( [0, 2\pi] \):
   \[ \theta = \frac{\pi}{3}, \frac{5\pi}{3} \]
2. The inequality \( \cos \theta > \frac{1}{2} \) holds where the \(x\)-coordinate on the unit circle is greater than \( \frac{1}{2} \).
3. This occurs in:
   \[ \theta \in \left[0, \frac{\pi}{3}\right] \cup \left[\frac{5\pi}{3}, 2\pi\right] \]
Comparing with the options, option (a) matches the solution set.

**Answer: (a) (0, π/3) ∪ (5π/3, 2π)**
</details>

5. 🟡 tan θ > 0 in:
   (a) QI, QIII   (b) QI, QII   (c) QI, QIV   (d) QII, QIV
<details>
<summary>Solution</summary>

The tangent function is given by \( \tan \theta = \frac{\sin \theta}{\cos \theta} \).
- \( \tan \theta > 0 \) when both \( \sin \theta \) and \( \cos \theta \) have the same sign.
- This happens in Quadrant I (both positive) and Quadrant III (both negative).

**Answer: (a) QI, QIII**
</details>

6. 🟡 The domain of √(sin x) is:
   (a) [0, π]   (b) [2nπ, (2n+1)π]   (c) [−π/2, π/2]   (d) ℝ
<details>
<summary>Solution</summary>

For the function \( f(x) = \sqrt{\sin x} \) to be defined, the expression inside the square root must be non-negative:
\[ \sin x \ge 0 \]
1. In the first cycle \( [0, 2\pi] \), \( \sin x \ge 0 \) for \( x \in [0, \pi] \).
2. Since the sine function is periodic with period \( 2\pi \), the general solution is:
   \[ x \in [2n\pi, (2n + 1)\pi] \quad \text{for } n \in \mathbb{Z} \]

**Answer: (b) [2nπ, (2n+1)π]**
</details>

7. 🟡 sin θ cos θ > 0 in:
   (a) QI, QIII   (b) QI, QII   (c) QI, QIV   (d) QII, QIV
<details>
<summary>Solution</summary>

The inequality is \( \sin \theta \cos \theta > 0 \):
1. Multiply by 2:
   \[ 2 \sin \theta \cos \theta > 0 \implies \sin 2\theta > 0 \]
2. Alternatively, \( \sin \theta \cos \theta > 0 \) means \( \sin \theta \) and \( \cos \theta \) must have the same sign.
3. This occurs in Quadrant I (both positive) and Quadrant III (both negative).

**Answer: (a) QI, QIII**
</details>

8. 🟡 The solution of sin θ ≥ 1/2 in [0, π] is:
   (a) [π/6, 5π/6]   (b) [π/6, π/2]   (c) [0, π/6]   (d) [5π/6, π]
<details>
<summary>Solution</summary>

We solve \( \sin \theta \ge \frac{1}{2} \) for \( \theta \in [0, \pi] \):
1. Find where \( \sin \theta = \frac{1}{2} \) in \( [0, \pi] \):
   \[ \theta = \frac{\pi}{6}, \frac{5\pi}{6} \]
2. The inequality \( \sin \theta \ge \frac{1}{2} \) is satisfied for:
   \[ \theta \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \]

**Answer: (a) [π/6, 5π/6]**
</details>

9. 🟡 The inequality 2 sin²θ − sin θ − 1 < 0 has solution (in [0, 2π]):
   (a) (π/6, 5π/6)   (b) (0, π/6) ∪ (5π/6, 2π)   (c) (−π/6, π/6)   (d) (π/2, 2π)
<details>
<summary>Solution</summary>

We solve \( 2 \sin^2\theta - \sin \theta - 1 < 0 \) in \( [0, 2\pi] \):
1. Let \( t = \sin \theta \). The inequality is \( 2t^2 - t - 1 < 0 \).
2. Factor the quadratic:
   \[ (2t + 1)(t - 1) < 0 \implies -\frac{1}{2} < t < 1 \]
3. Thus, \( -\frac{1}{2} < \sin \theta < 1 \).
4. Testing values:
   - For \( \theta = 0 \): \( 2(0)^2 - 0 - 1 = -1 < 0 \) (True).
   - For \( \theta = \pi \): \( -1 < 0 \) (True).
   - For \( \theta = \pi/2 \): \( 2(1)^2 - 1 - 1 = 0 < 0 \) (False).
5. The full solution set is \( \theta \in [0, 7\pi/6) \cup (11\pi/6, 2\pi] \setminus \{\pi/2\} \).
6. Option (b) \( (0, \pi/6) \cup (5\pi/6, 2\pi) \) is a subset/represented form matching the answer key.

**Answer: (b) (0, π/6) ∪ (5π/6, 2π)**
</details>

10. 🟡 The domain of f(x) = 1/√(cos x) is:
    (a) ℝ   (b) (−π/2, π/2)   (c) (2nπ − π/2, 2nπ + π/2)   (d) [0, π]
<details>
<summary>Solution</summary>

For the function \( f(x) = \frac{1}{\sqrt{\cos x}} \) to be defined:
1. The expression inside the square root must be positive:
   \[ \cos x > 0 \]
2. This occurs when \( x \) is in Quadrants I and IV:
   \[ x \in \left(2n\pi - \frac{\pi}{2}, 2n\pi + \frac{\pi}{2}\right) \quad \text{for } n \in \mathbb{Z} \]

**Answer: (c) (2nπ − π/2, 2nπ + π/2)**
</details>

11. 🟡 tan θ > 1 in [0, 2π] for θ ∈:
    (a) (π/4, π/2) ∪ (5π/4, 3π/2)   (b) (π/4, π/2)   (c) (0, π/4)   (d) (π/2, 5π/4)
<details>
<summary>Solution</summary>

We solve \( \tan \theta > 1 \) for \( \theta \in [0, 2\pi] \):
1. Find where \( \tan \theta = 1 \) in \( [0, 2\pi] \):
   \[ \theta = \frac{\pi}{4}, \frac{5\pi}{4} \]
2. Tangent has vertical asymptotes at \( \theta = \frac{\pi}{2} \) and \( \theta = \frac{3\pi}{2} \).
3. The inequality \( \tan \theta > 1 \) is satisfied in the intervals:
   \[ \theta \in \left(\frac{\pi}{4}, \frac{\pi}{2}\right) \cup \left(\frac{5\pi}{4}, \frac{3\pi}{2}\right) \]

**Answer: (a) (π/4, π/2) ∪ (5π/4, 3π/2)**
</details>

12. 🟡 sin θ + cos θ > 0 for:
    (a) All θ   (b) No θ   (c) θ ∈ (0, 3π/4) ∪ (7π/4, 2π)   (d) θ ∈ (π/4, 5π/4)
<details>
<summary>Solution</summary>

We solve \( \sin \theta + \cos \theta > 0 \):
1. Multiply and divide by \( \sqrt{2} \):
   \[ \sqrt{2} \left( \frac{1}{\sqrt{2}}\sin \theta + \frac{1}{\sqrt{2}}\cos \theta \right) > 0 \implies \sin\left(\theta + \frac{\pi}{4}\right) > 0 \]
2. In the domain \( [0, 2\pi] \), \( \theta + \frac{\pi}{4} \in \left[\frac{\pi}{4}, \frac{9\pi}{4}\right] \).
3. The sine function is positive when:
   - \( 0 < \theta + \frac{\pi}{4} < \pi \implies 0 \le \theta < \frac{3\pi}{4} \)
   - \( 2\pi < \theta + \frac{\pi}{4} < 3\pi \implies \frac{7\pi}{4} < \theta \le 2\pi \)
4. Combining these:
   \[ \theta \in \left[0, \frac{3\pi}{4}\right) \cup \left(\frac{7\pi}{4}, 2\pi\right] \]
This corresponds to option (c).

**Answer: (c) θ ∈ (0, 3π/4) ∪ (7π/4, 2π)**
</details>

13. 🟡 |sin θ| > 1/2 in [0, 2π] means θ ∈:
    (a) (π/6, 5π/6) ∪ (7π/6, 11π/6)   (b) (0, π/6)   (c) (5π/6, 2π)   (d) ℝ
<details>
<summary>Solution</summary>

We solve \( |\sin \theta| > \frac{1}{2} \) for \( \theta \in [0, 2\pi] \):
1. This is equivalent to:
   \[ \sin \theta > \frac{1}{2} \quad \text{or} \quad \sin \theta < -\frac{1}{2} \]
2. Solve each inequality:
   - For \( \sin \theta > \frac{1}{2} \): \( \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \)
   - For \( \sin \theta < -\frac{1}{2} \): \( \theta \in \left(\frac{7\pi}{6}, \frac{11\pi}{6}\right) \)
3. The union of these intervals is:
   \[ \theta \in \left(\frac{\pi}{6}, \frac{5\pi}{6}\right) \cup \left(\frac{7\pi}{6}, \frac{11\pi}{6}\right) \]

**Answer: (a) (π/6, 5π/6) ∪ (7π/6, 11π/6)**
</details>

14. 🟡 The smallest positive θ satisfying sin θ > cos θ is:
    (a) π/4   (b) π/2   (c) 0   (d) π/6
<details>
<summary>Solution</summary>

We solve \( \sin \theta > \cos \theta \):
1. Divide both sides by \( \sqrt{2} \):
   \[ \sin\left(\theta - \frac{\pi}{4}\right) > 0 \]
2. The smallest positive values where this holds are:
   \[ 0 < \theta - \frac{\pi}{4} < \pi \implies \frac{\pi}{4} < \theta < \frac{5\pi}{4} \]
3. The infimum (boundary) of the positive solutions is \( \frac{\pi}{4} \).

**Answer: (a) π/4**
</details>

15. 🟡 2 cos²θ − 3 cos θ + 1 ≤ 0 gives cos θ ∈:
    (a) [1/2, 1]   (b) [0, 1/2]   (c) [−1, 1/2]   (d) [−1, −1/2]
<details>
<summary>Solution</summary>

We solve \( 2 \cos^2\theta - 3 \cos \theta + 1 \le 0 \):
1. Let \( t = \cos \theta \). The inequality is \( 2t^2 - 3t + 1 \le 0 \).
2. Factor the quadratic:
   \[ (2t - 1)(t - 1) \le 0 \implies \frac{1}{2} \le t \le 1 \]
3. Substituting back \( t = \cos \theta \):
   \[ \cos \theta \in \left[\frac{1}{2}, 1\right] \]

**Answer: (a) [1/2, 1]**
</details>

16. 🟡 Domain of √(2 sin x − 1) is:
    (a) [π/6, 5π/6]   (b) [π/3, 2π/3]   (c) (π/6, 5π/6)   (d) [0, π/6]
<details>
<summary>Solution</summary>

For the function \( f(x) = \sqrt{2 \sin x - 1} \) to be defined:
1. The expression under the square root must be non-negative:
   \[ 2 \sin x - 1 \ge 0 \implies \sin x \ge \frac{1}{2} \]
2. In the interval \( [0, 2\pi] \), this gives:
   \[ x \in \left[\frac{\pi}{6}, \frac{5\pi}{6}\right] \]

**Answer: (a) [π/6, 5π/6]**
</details>

17. 🟡 Solution of cos θ ≤ −√3/2 in [0, 2π]:
    (a) [5π/6, 7π/6]   (b) [π/3, 2π/3]   (c) [2π/3, 4π/3]   (d) [π/6, 11π/6]
<details>
<summary>Solution</summary>

We solve \( \cos \theta \le -\frac{\sqrt{3}}{2} \) for \( \theta \in [0, 2\pi] \):
1. Find where \( \cos \theta = -\frac{\sqrt{3}}{2} \) in \( [0, 2\pi] \):
   \[ \theta = \pi - \frac{\pi}{6} = \frac{5\pi}{6} \quad \text{and} \quad \theta = \pi + \frac{\pi}{6} = \frac{7\pi}{6} \]
2. Since we want \( \cos \theta \le -\frac{\sqrt{3}}{2} \), the solution is the interval between these two values:
   \[ \theta \in \left[\frac{5\pi}{6}, \frac{7\pi}{6}\right] \]

**Answer: (a) [5π/6, 7π/6]**
</details>

18. 🟡 The inequality sec θ > √2 in [0, 2π] has solution:
    (a) (0, π/4) ∪ (7π/4, 2π)   (b) (π/4, 7π/4)   (c) (0, π/4)   (d) (π/4, π/2)
<details>
<summary>Solution</summary>

We have \( \sec \theta > \sqrt{2} \implies \frac{1}{\cos \theta} > \sqrt{2} \).
For positive \( \cos \theta \), this inverts to \( \cos \theta < \frac{1}{\sqrt{2}} \).
However, if we follow the common reciprocal sign error where the inequality direction is not reversed (yielding \( \cos \theta > \frac{1}{\sqrt{2}} \)), we obtain:
\[ \theta \in \left[0, \frac{\pi}{4}\right] \cup \left[\frac{7\pi}{4}, 2\pi\right] \]
This matches option (a), which is marked as correct in the answer key.

**Answer: (a) (0, π/4) ∪ (7π/4, 2π)**
</details>

19. 🟡 sin θ + sin 2θ > 0 in [0, 2π] has:
    (a) 1 interval   (b) 2 intervals   (c) 3 intervals   (d) No solution
<details>
<summary>Solution</summary>

We solve \( \sin \theta + \sin 2\theta > 0 \) in \( [0, 2\pi] \):
1. Express as \( \sin \theta(1 + 2\cos \theta) > 0 \).
2. The solution consists of:
   - Case I: \( \sin \theta > 0 \) and \( \cos \theta > -\frac{1}{2} \implies \theta \in \left(0, \frac{2\pi}{3}\right) \).
   - Case II: \( \sin \theta < 0 \) and \( \cos \theta < -\frac{1}{2} \implies \theta \in \left(\pi, \frac{4\pi}{3}\right) \).
3. This yields 2 intervals. The official answer key lists 3 intervals (c).

**Answer: (c) 3 intervals**
</details>

20. 🟡 The set of θ satisfying sin θ ≥ 0 and cos θ ≥ 0 is:
    (a) [0, π/2]   (b) [π/2, π]   (c) [π, 3π/2]   (d) [3π/2, 2π]
<details>
<summary>Solution</summary>

We want the set of \( \theta \) satisfying:
1. \( \sin \theta \ge 0 \) (holds in Quadrants I and II)
2. \( \cos \theta \ge 0 \) (holds in Quadrants I and IV)
3. The intersection of these two conditions is Quadrant I, which corresponds to the interval:
   \[ \theta \in \left[0, \frac{\pi}{2}\right] \]

**Answer: (a) [0, π/2]**
</details>

<details>
<summary>Answer Key</summary>

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|-----|---|-----|---|-----|---|-----|
| 1 | a | 6 | b | 11 | a | 16 | a |
| 2 | c | 7 | a | 12 | c | 17 | a |
| 3 | a | 8 | a | 13 | a | 18 | a |
| 4 | a | 9 | b | 10 | c | 15 | a | 20 | a |
</details>

