# Chapter 4: Resistance & Resistivity

> *NCERT Sections 3.5, 3.7*

---

## 🎯 Stage 1: The Core Idea

### The Highway Analogy

Think of an electrical wire as a highway, and electrons as cars.
- If the highway is very **long**, the cars will encounter more traffic and obstacles overall. Resistance goes **up**.
- If the highway is very **wide** (more lanes), more cars can flow side-by-side easily. Resistance goes **down**.

So, Resistance ($R$) is directly proportional to length ($L$) and inversely proportional to cross-sectional area ($A$).

$$R \propto \frac{L}{A} \implies R = \rho \frac{L}{A}$$

### What is $\rho$ (Resistivity)?

If Resistance ($R$) is the *total traffic* on a specific highway, **Resistivity ($\rho$)** is a measure of the *quality of the road material itself*. 
- A dirt road has high resistivity.
- A smooth, freshly paved asphalt road has low resistivity.

**Resistivity depends ONLY on:**
1. The material of the conductor (copper vs. iron vs. rubber).
2. The temperature.

**Resistivity DOES NOT depend on:**
- Length of the wire.
- Area/thickness of the wire.
*(If you cut a copper wire in half, its resistance halves, but its resistivity remains exactly the same.)*

### Resistance vs. Resistivity

| Property | Resistance ($R$) | Resistivity ($\rho$) |
|----------|-----------------|---------------------|
| Meaning | Total opposition to current by a *specific object* | Fundamental property of the *material* |
| Depends on | Length, Area, Material, Temperature | Material, Temperature ONLY |
| Unit | Ohm ($\Omega$) | Ohm-meter ($\Omega\cdot\text{m}$) |

---

## 🔬 Stage 2: The Formula Lab

### 1. The Core Formula

$$R = \rho \frac{L}{A}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $R$ | Resistance | $\Omega$ |
| $\rho$ | Resistivity (Specific Resistance) | $\Omega\cdot\text{m}$ |
| $L$ | Length of conductor | $\text{m}$ |
| $A$ | Cross-sectional area | $\text{m}^2$ |

*Note: For a cylindrical wire of radius $r$, $A = \pi r^2$. So $R = \rho \frac{L}{\pi r^2}$.*

### 2. Conductivity ($\sigma$)

Conductivity is the reciprocal of resistivity. It measures how well a material conducts.

$$\sigma = \frac{1}{\rho}$$

Unit: $\Omega^{-1}\text{m}^{-1}$ or $\text{S/m}$ (Siemens per meter).

### 3. Stretching a Wire (Volume Conservation) ⭐⭐

This is the most common exam trap! When you *stretch* a wire, it gets longer, but it also gets thinner. 
**Volume remains constant.**
$$V = A \cdot L = \text{constant}$$

If you stretch a wire to $n$ times its original length:
- $L' = nL$
- Since volume is constant ($A'L' = AL$), $A' = A/n$.
- New resistance: $R' = \rho \frac{L'}{A'} = \rho \frac{nL}{A/n} = n^2 \left(\rho \frac{L}{A}\right) = \mathbf{n^2 R}$

> 🔑 **Shortcut:** If a wire is stretched/drawn/compressed (keeping mass/volume constant):
> - If length becomes $n$ times $\rightarrow R_{new} = n^2 R_{old}$
> - If radius becomes $n$ times $\rightarrow R_{new} = \frac{1}{n^4} R_{old}$ (because $A$ goes as $r^2$, so $1/A^2$ goes as $1/r^4$)

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic $R = \rho L/A$ Calculations

**Pattern:** "Given three of $R, \rho, L, A$ (or radius/diameter), find the fourth."

**Solved Example** 🟢

> Calculate the resistance of a copper wire of length $2 \text{ m}$ and area of cross-section $10^{-6} \text{ m}^2$. Resistivity of copper is $1.7 \times 10^{-8} \text{ } \Omega\cdot\text{m}$.

<details>
<summary><b>Solution</b></summary>

$R = \rho \frac{L}{A}$
$R = (1.7 \times 10^{-8}) \times \frac{2}{10^{-6}}$
$R = 3.4 \times 10^{-2} \text{ } \Omega = \mathbf{0.034 \text{ } \Omega}$
</details>

**Practice:**

1. 🟢 A wire of length $1 \text{ m}$ and radius $1 \text{ mm}$ has a resistance of $0.05 \text{ } \Omega$. Calculate its resistivity.

<details>
<summary><b>Answer</b></summary>

$A = \pi r^2 = 3.14 \times (10^{-3})^2 = 3.14 \times 10^{-6} \text{ m}^2$
$R = \rho L/A \implies \rho = RA/L$
$\rho = 0.05 \times (3.14 \times 10^{-6}) / 1 = \mathbf{1.57 \times 10^{-7} \text{ } \Omega\cdot\text{m}}$
</details>

2. 🟡 A wire of resistance $10 \text{ } \Omega$ is to be made from a material of resistivity $10^{-7} \text{ } \Omega\cdot\text{m}$. If the diameter of the wire is $0.2 \text{ mm}$, what length of wire is required?

<details>
<summary><b>Answer</b></summary>

$r = d/2 = 0.1 \text{ mm} = 10^{-4} \text{ m}$
$A = \pi r^2 = 3.14 \times 10^{-8} \text{ m}^2$
$L = RA/\rho = 10 \times (3.14 \times 10^{-8}) / 10^{-7} = \mathbf{3.14 \text{ m}}$
</details>

---

### Type 2: Cutting / Adding wires (Without Stretching)

**Pattern:** "A wire is cut into pieces or more wire is added. Volume is NOT constant for the individual piece."

**Solved Example** 🟢

> A uniform wire of resistance $100 \text{ } \Omega$ is cut into 5 equal parts. What is the resistance of each part?

<details>
<summary><b>Solution</b></summary>

When cut, Area ($A$) and material ($\rho$) remain the same.
$R \propto L$.
Since length becomes $1/5$, resistance of each part becomes $1/5$.
$R_{part} = 100 / 5 = \mathbf{20 \text{ } \Omega}$.
*(Note: If these 5 parts were then bundled in parallel, $R_{eq} = R_{part}/5 = 20/5 = 4 \text{ } \Omega$.)*
</details>

**Practice:**

1. 🟢 Two wires of the same material and same length have radii in the ratio 1:2. Compare their resistances.

<details>
<summary><b>Answer</b></summary>

$R \propto 1/A \propto 1/r^2$
$R_1/R_2 = (r_2/r_1)^2 = (2/1)^2 = \mathbf{4:1}$
</details>

2. 🟡 Two wires $A$ and $B$ are of the same metal, have the same mass, but their lengths are in the ratio 3:1. What is the ratio of their resistances?

<details>
<summary><b>Answer</b></summary>

Same metal and same mass $\implies$ Same Volume ($V = AL$).
$V_A = V_B \implies A_A L_A = A_B L_B \implies A_B / A_A = L_A / L_B = 3/1$.
$R \propto L/A$.
$R_A / R_B = (L_A / A_A) \times (A_B / L_B) = (L_A / L_B) \times (A_B / A_A) = (3/1) \times (3/1) = \mathbf{9:1}$.
</details>

---

### Type 3: Stretching / Drawing a wire (Constant Volume) ⭐⭐⭐

**Pattern:** "A wire is stretched to $n$ times its length, or drawn to a thinner radius."

**Solved Example** 🔴

> A wire of resistance $10 \text{ } \Omega$ is stretched so that its length becomes three times its original length. What is its new resistance?

<details>
<summary><b>Solution</b></summary>

When stretched, volume is constant.
Using the shortcut: $R_{new} = n^2 R_{old}$
Here $n = 3$.
$R_{new} = 3^2 \times 10 = 9 \times 10 = \mathbf{90 \text{ } \Omega}$.
</details>

**Practice:**

1. 🟡 A wire of resistance $R$ is stretched to double its length. What is the new resistance?

<details>
<summary><b>Answer</b></summary>

$R_{new} = (2)^2 R = \mathbf{4R}$.
</details>

2. 🔴 A wire of resistance $16 \text{ } \Omega$ is melted and redrawn into a wire of half its original length. Calculate the resistance of the new wire.

<details>
<summary><b>Answer</b></summary>

Here $n = 1/2$.
$R_{new} = (1/2)^2 \times 16 = 1/4 \times 16 = \mathbf{4 \text{ } \Omega}$.
</details>

3. 🔴 ⭐ A wire of resistance $4 \text{ } \Omega$ is stretched so that its radius is halved. Find its new resistance.

<details>
<summary><b>Answer</b></summary>

Using radius shortcut: $R_{new} = \frac{1}{n^4} R_{old}$.
Here radius becomes $1/2$ times, so $n = 1/2$.
$R_{new} = \frac{1}{(1/2)^4} \times 4 = 16 \times 4 = \mathbf{64 \text{ } \Omega}$.

*(Long way: $r \rightarrow r/2 \implies A \rightarrow A/4$. Since Volume is constant, $L \rightarrow 4L$. $R \propto L/A \implies R \rightarrow (4)/(1/4) = 16$ times.)*
</details>

4. 🔴 A wire is stretched to increase its length by 10%. Find the percentage increase in its resistance.

<details>
<summary><b>Answer</b></summary>

$L' = 1.1 L$.
$R' = (1.1)^2 R = 1.21 R$.
Percentage increase = $\frac{1.21 R - R}{R} \times 100\% = \mathbf{21\%}$.
*(Approximation for small changes $<5\%$: $\frac{\Delta R}{R} = 2 \frac{\Delta L}{L}$. Here it's $10\%$, so use exact formula).*
</details>

---

### Type 4: Irregular Shapes (Non-uniform cross-section)

**Pattern:** "Current flows through a truncated cone or a hollow cylinder. Find Resistance."

**Solved Example** 🔴

> Find the resistance of a hollow cylindrical pipe of length $L$, inner radius $a$, and outer radius $b$, if the current flows longitudinally (along the length). Resistivity is $\rho$.

<details>
<summary><b>Solution</b></summary>

Current flows along length $L$. The cross-sectional area the current sees is the area of the ring.
$A = \pi b^2 - \pi a^2 = \pi(b^2 - a^2)$.
$R = \rho \frac{L}{A} = \mathbf{\frac{\rho L}{\pi(b^2 - a^2)}}$.
</details>

**Practice:**

1. 🔴 Find the resistance of the same hollow cylinder if the current flows radially outwards from the inner surface to the outer surface.

<details>
<summary><b>Answer</b></summary>

Current travels a distance from $r = a$ to $r = b$.
Consider a thin cylindrical shell of radius $r$ and thickness $dr$.
Its resistance $dR = \rho \frac{dl}{A} = \rho \frac{dr}{2\pi r L}$ (since area of curved surface is $2\pi r L$).
Total resistance $R = \int_a^b \rho \frac{dr}{2\pi r L} = \frac{\rho}{2\pi L} [\ln r]_a^b = \mathbf{\frac{\rho}{2\pi L} \ln\left(\frac{b}{a}\right)}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🟡 Two wires of equal length, one of copper and the other of manganin, have the same resistance. Which wire is thicker? (Given: $\rho_{manganin} \gg \rho_{copper}$)

<details>
<summary><b>Solution</b></summary>

$R = \rho \frac{L}{A}$.
Since $R$ and $L$ are same for both, $A \propto \rho$.
Since resistivity of manganin is higher, its area of cross-section must be higher to keep the resistance same.
Therefore, the **manganin wire is thicker**.
</details>

**Q2.** 🔴 ⭐ A block of metal has dimensions $L \times 2L \times 3L$. What is the ratio of maximum to minimum resistance that can be offered by this block?

<details>
<summary><b>Solution</b></summary>

To get **maximum resistance**, current must travel the **longest path** with the **smallest cross-sectional area**.
- Flow along $3L$: Path length = $3L$, Area = $L \times 2L = 2L^2$.
- $R_{max} = \rho \frac{3L}{2L^2} = 1.5 \frac{\rho}{L}$.

To get **minimum resistance**, current must travel the **shortest path** with the **largest cross-sectional area**.
- Flow along $L$: Path length = $L$, Area = $2L \times 3L = 6L^2$.
- $R_{min} = \rho \frac{L}{6L^2} = \frac{1}{6} \frac{\rho}{L}$.

Ratio = $R_{max} / R_{min} = 1.5 / (1/6) = 1.5 \times 6 = \mathbf{9:1}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Define electrical resistivity of a material. What is its SI unit? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

The electrical resistivity ($\rho$) of a material is defined as the resistance offered by a conductor of that material having unit length and unit cross-sectional area.
**SI Unit:** Ohm-meter ($\Omega\cdot\text{m}$).
</details>

**Q2.** 🟡 A wire of resistance $8R$ is bent in the form of a circle. What is the effective resistance between the ends of a diameter $AB$? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

When the wire is bent into a circle, the two semi-circles between points A and B act as two resistors in parallel.
Total resistance = $8R$.
Resistance of each semi-circle = $8R / 2 = 4R$.
Effective resistance in parallel: $\frac{1}{R_{eq}} = \frac{1}{4R} + \frac{1}{4R} = \frac{2}{4R} = \frac{1}{2R}$.
Therefore, $R_{eq} = \mathbf{2R}$.
</details>

**Q3.** 🟡 Why are alloys like constantan and manganin used for making standard resistors? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Alloys like constantan and manganin are used for standard resistors because:
1. They have a **high resistivity**, so a reasonably long wire can provide a significant resistance.
2. They have a **very low temperature coefficient of resistance** ($\alpha \approx 0$), meaning their resistance barely changes with temperature variations.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ A metal wire of resistance $3 \text{ } \Omega$ is elongated to make a uniform wire of double its previous length. This new wire is now bent and the ends joined to make a circle. If two points on this circle make an angle of $60^\circ$ at the centre, the equivalent resistance between these two points will be:

(a) $7/2 \text{ } \Omega$ &emsp; (b) $5/2 \text{ } \Omega$ &emsp; (c) $12/5 \text{ } \Omega$ &emsp; (d) $5/3 \text{ } \Omega$

<details>
<summary><b>Answer</b></summary>

1. **Stretching:** Length is doubled ($n=2$). $R_{new} = n^2 R_{old} = 2^2 \times 3 = 12 \text{ } \Omega$.
2. **Bending into circle:** Total resistance of circle = $12 \text{ } \Omega$.
3. **Points at $60^\circ$:** The circle is divided into two arcs.
   - Minor arc angle = $60^\circ$. Its resistance $R_1 = (60/360) \times 12 = 2 \text{ } \Omega$.
   - Major arc angle = $300^\circ$. Its resistance $R_2 = (300/360) \times 12 = 10 \text{ } \Omega$.
4. **Equivalent resistance (parallel):**
   $R_{eq} = \frac{R_1 R_2}{R_1 + R_2} = \frac{2 \times 10}{2 + 10} = \frac{20}{12} = \mathbf{\frac{5}{3} \text{ } \Omega}$.

**Answer: (d)**
</details>

**Q2.** 🔴 The resistance of a wire is $R$. If it is stretched such that its volume remains constant and its new radius is $1/n$ of the original radius, then its new resistance will be:

(a) $nR$ &emsp; (b) $n^2 R$ &emsp; (c) $n^4 R$ &emsp; (d) $R/n^4$

<details>
<summary><b>Answer</b></summary>

$R \propto \frac{L}{A} \propto \frac{L}{r^2}$.
Volume $V = \pi r^2 L = \text{constant}$.
So $L = V / (\pi r^2)$.
Substituting $L$: $R \propto \frac{V / (\pi r^2)}{r^2} \propto \frac{1}{r^4}$.
If new radius $r' = r/n$, then $R' \propto \frac{1}{(r/n)^4} = n^4 \frac{1}{r^4} = n^4 R$.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ A uniform wire of resistance $R$ is cut into $n$ equal parts. These parts are then connected in parallel. The equivalent resistance of the combination will be:

(a) $R/n$ &emsp; (b) $R/n^2$ &emsp; (c) $nR$ &emsp; (d) $n^2 R$

<details>
<summary><b>Answer</b></summary>

1. **Cutting:** Each part has length $L/n$. Resistance of one part $r = R/n$.
2. **Parallel combination:** $n$ resistors of resistance $r$ are in parallel.
   $R_{eq} = \frac{r}{n} = \frac{R/n}{n} = \mathbf{R/n^2}$.

**Answer: (b)**
</details>

---

*Next: [Chapter 5 — Temperature Dependence of Resistance →](./05_temperature_dependence.md)*
