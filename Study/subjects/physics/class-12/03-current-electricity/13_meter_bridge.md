# Chapter 13: Meter Bridge

> *NCERT Section 3.15 (Slide Wire Bridge)*

---

## 🎯 Stage 1: The Core Idea

### Wheatstone Bridge in Real Life

The Wheatstone bridge is a theoretical diamond on paper. A **Meter Bridge** (or Slide Wire Bridge) is the practical, real-world device built directly on that theory.

Instead of four separate resistors ($P, Q, R, S$), a meter bridge has:
1. **Resistance Box ($R$):** A box where you can plug in a known, exact resistance.
2. **Unknown Wire ($S$ or $X$):** The wire whose resistance you are trying to find.
3. **A $1\text{-meter}$ long constantan/manganin wire:** This single wire acts as the other two resistors ($P$ and $Q$). 

You slide a metal contact (the "jockey") along this $1\text{-meter}$ wire until the galvanometer reads zero. The jockey divides the $1\text{-meter}$ wire into two segments. The resistance of the left segment is $P$, and the right segment is $Q$. 
Because resistance is proportional to length ($R \propto L$), the ratio of lengths is exactly the ratio of resistances!

---

## 🔬 Stage 2: The Formula Lab

### The Balancing Formula

Let the total length of the wire be $100\text{ cm}$.
Let the balance point be found at length $l$ (in cm) from the left end.
- The left part of the wire has length $l$.
- The right part of the wire has length $(100 - l)$.

Using the Wheatstone balance condition:
$$\frac{R}{S} = \frac{R_{left\_wire}}{R_{right\_wire}}$$

Since resistance of uniform wire is proportional to length:
$$\frac{R}{S} = \frac{l}{100 - l}$$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $R$ | Known resistance (from Resistance Box on the left) | $\Omega$ |
| $S$ | Unknown resistance (on the right gap) | $\Omega$ |
| $l$ | Balancing length from the left end | $\text{cm}$ |

**To find the unknown $S$:**
$$S = R \left( \frac{100 - l}{l} \right)$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic Balancing Calculation ⭐

**Pattern:** "Given $R$ and balance point $l$, find unknown $S$."

**Solved Example** 🟢

> In a meter bridge experiment, the balance point is found to be at $40\text{ cm}$ from the left end. If the known resistance in the left gap is $10\text{ } \Omega$, find the unknown resistance in the right gap.

<details>
<summary><b>Solution</b></summary>

$l = 40\text{ cm}$. Therefore, $(100 - l) = 60\text{ cm}$.
Left resistance $R = 10\text{ } \Omega$. Right resistance = $S$.
$\frac{R}{S} = \frac{l}{100 - l}$
$\frac{10}{S} = \frac{40}{60} = \frac{2}{3}$
$2S = 30 \implies S = \mathbf{15\text{ } \Omega}$.
</details>

**Practice:**

1. 🟢 A meter bridge is balanced at $60\text{ cm}$ from the left. If the right gap has a resistance of $20\text{ } \Omega$, what is the resistance in the left gap?

<details>
<summary><b>Answer</b></summary>

$l = 60\text{ cm}$, $100-l = 40\text{ cm}$. $S = 20\text{ } \Omega$.
$R / 20 = 60 / 40 = 3 / 2$.
$R = 20 \times (3/2) = \mathbf{30\text{ } \Omega}$.
</details>

2. 🟢 In a meter bridge, the null point is found at a distance of $33.3\text{ cm}$ from A. If now a resistance of $12\text{ } \Omega$ is connected in parallel with $S$, the null point occurs at $50\text{ cm}$. Find the initial values of $R$ and $S$.

<details>
<summary><b>Answer</b></summary>

Case 1: $R/S = 33.3 / (100 - 33.3) = 33.3 / 66.7 \approx 1/2$.
So, $S = 2R$.

Case 2: A $12\text{ } \Omega$ is in parallel with $S$. New right resistance $S' = \frac{12S}{12 + S}$.
New balance is $50\text{ cm}$.
$R / S' = 50 / 50 = 1 \implies R = S'$.
Substitute $S = 2R$ into $S'$:
$R = \frac{12(2R)}{12 + 2R}$
Divide by $R$: $1 = \frac{24}{12 + 2R} \implies 12 + 2R = 24 \implies 2R = 12 \implies \mathbf{R = 6\text{ } \Omega}$.
Since $S = 2R$, $\mathbf{S = 12\text{ } \Omega}$.
</details>

---

### Type 2: Swapping the Gaps ⭐⭐

**Pattern:** "If $R$ and $S$ are interchanged, what happens to the balance point?"

**Solved Example** 🟡

> A meter bridge has a balance point at $l = 30\text{ cm}$ from the left. If the resistors in the left and right gaps are interchanged, what will be the new balance point?

<details>
<summary><b>Solution</b></summary>

Initially: $\frac{R}{S} = \frac{30}{70}$.
When swapped, the left gap becomes $S$ and the right gap becomes $R$.
Let the new balance point be $l'$.
$\frac{S}{R} = \frac{l'}{100 - l'}$
Since $R/S = 30/70$, then $S/R = 70/30$.
$\frac{70}{30} = \frac{l'}{100 - l'} \implies l' = \mathbf{70\text{ cm}}$.
*(Shortcut: When resistors are swapped, the new balance point is exactly $(100 - l)$).*
</details>

**Practice:**

1. 🟡 In a meter bridge, the balance point is $l_1$. If the known and unknown resistances are interchanged, the balance point shifts by $20\text{ cm}$. If the known resistance was larger, find $l_1$.

<details>
<summary><b>Answer</b></summary>

Since known ($R$) is larger, initial $l_1$ must be $> 50\text{ cm}$. Let's say $l_1 = 50 + x$.
When swapped, new balance point $l_2 = 100 - l_1 = 100 - (50 + x) = 50 - x$.
Shift $= l_1 - l_2 = (50 + x) - (50 - x) = 2x$.
Given shift $= 20\text{ cm} \implies 2x = 20 \implies x = 10\text{ cm}$.
So $l_1 = 50 + 10 = \mathbf{60\text{ cm}}$.
</details>

2. 🟡 A resistance of $R\text{ } \Omega$ draws current from a potentiometer. The balance point is $l$. If $R$ and $S$ are interchanged in a meter bridge, it shifts by $10\text{ cm}$. If $R/S = 1.5$, find $l$.

<details>
<summary><b>Answer</b></summary>

$R/S = 1.5 = 3/2 \implies l / (100-l) = 3/2 \implies 2l = 300 - 3l \implies 5l = 300 \implies l = \mathbf{60\text{ cm}}$.
(The shift of $10\text{ cm}$ is extra information confirming $60 \rightarrow 40$).
</details>

---

### Type 3: End Corrections ⭐⭐⭐

**Pattern:** "The zero mark on the scale doesn't perfectly align with the start of the wire."

> 🔑 **THE MASTER TRICK:**
> In reality, the thick copper strips at the ends have *some* small resistance. This acts like extra length added to the ends of the wire.
> Let the end correction at the left end be $a$ (in cm) and at the right end be $b$ (in cm).
> Modified Formula: **$\frac{R}{S} = \frac{l + a}{100 - l + b}$**

**Solved Example** 🔴

> In a meter bridge, the balance point is at $40\text{ cm}$ when $R = 10\text{ } \Omega$ and $S = 15\text{ } \Omega$. When $R$ and $S$ are interchanged, the balance point is at $58\text{ cm}$. Find the end corrections $a$ and $b$.

<details>
<summary><b>Solution</b></summary>

Case 1 ($R=10, S=15, l=40$):
$\frac{10}{15} = \frac{40 + a}{60 + b} \implies \frac{2}{3} = \frac{40 + a}{60 + b}$
$120 + 2b = 120 + 3a \implies 2b = 3a \implies b = 1.5a$.

Case 2 ($R=15, S=10, l=58$):
$\frac{15}{10} = \frac{58 + a}{42 + b} \implies \frac{3}{2} = \frac{58 + a}{42 + b}$
$126 + 3b = 116 + 2a$
Substitute $b = 1.5a$:
$126 + 3(1.5a) = 116 + 2a \implies 126 + 4.5a = 116 + 2a$
$2.5a = -10 \implies a = -4\text{ cm}$.
$b = 1.5(-4) = -6\text{ cm}$.
*(Negative end corrections mean the scale zero is actually past the physical start of the wire!)*
</details>

**Practice:**

1. 🔴 A meter bridge has end corrections $1\text{ cm}$ and $2\text{ cm}$ at the A (left) and B (right) ends respectively. If $R = 15\text{ } \Omega$ and $S = 10\text{ } \Omega$, what is the actual reading $l$ on the scale?

<details>
<summary><b>Answer</b></summary>

$\frac{R}{S} = \frac{l + a}{100 - l + b}$
$\frac{15}{10} = \frac{l + 1}{100 - l + 2} \implies 1.5 = \frac{l + 1}{102 - l}$
$1.5(102 - l) = l + 1$
$153 - 1.5l = l + 1$
$152 = 2.5l \implies l = 152 / 2.5 = \mathbf{60.8\text{ cm}}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A resistance $R_1$ is connected in the left gap of a meter bridge and $R_2$ in the right gap. The balance point is at $40\text{ cm}$ from the left. Now a resistance of $10\text{ } \Omega$ is connected in series with $R_1$, and the balance point shifts by $10\text{ cm}$. Find $R_1$ and $R_2$.

<details>
<summary><b>Solution</b></summary>

Case 1: $R_1 / R_2 = 40 / 60 = 2 / 3 \implies R_2 = 1.5 R_1$.
Case 2: $R_1$ is increased to $(R_1 + 10)$. Since the left resistance increased, the balance point must shift to the right to maintain ratio.
New $l = 40 + 10 = 50\text{ cm}$.
$\frac{R_1 + 10}{R_2} = \frac{50}{50} = 1 \implies R_1 + 10 = R_2$.
Substitute $R_2 = 1.5 R_1$:
$R_1 + 10 = 1.5 R_1 \implies 0.5 R_1 = 10 \implies \mathbf{R_1 = 20\text{ } \Omega}$.
$R_2 = 1.5(20) = \mathbf{30\text{ } \Omega}$.
</details>

**Q2.** 🔴 ⭐ An unknown resistance $X$ is to be determined using resistances $R_1, R_2$ or $R_3$. Their corresponding null points are A, B and C. Find which of the given null points provides the most accurate reading and why?
(Assume $R_1 < X, R_2 \approx X, R_3 > X$).

<details>
<summary><b>Solution</b></summary>

A meter bridge is most accurate and sensitive when the null point is near the **center of the wire** ($50\text{ cm}$ mark).
This minimizes percentage errors in measuring $l$ and $(100-l)$, and minimizes the effect of end corrections.
To get the null point near $50\text{ cm}$, the ratio $R/S$ should be roughly $1$.
Therefore, we should choose the known resistance $R_2$ which is approximately equal to $X$.
The null point **B** (corresponding to $R_2$) provides the most accurate reading.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 What is the principle of a meter bridge? Which material is used for the meter bridge wire and why? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. **Principle:** It works on the principle of a balanced Wheatstone bridge ($\frac{P}{Q} = \frac{R}{S}$).
2. **Material:** Constantan or Manganin.
3. **Why:** They have a high resistivity (so the wire has measurable resistance) and a very low temperature coefficient of resistance ($\alpha \approx 0$), so the wire's resistance doesn't change significantly when heated by the current.
</details>

**Q2.** 🟡 Why are the connections between resistors in a meter bridge made of thick copper strips? *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

Thick copper strips have very low electrical resistance. This minimizes any extra, unaccounted resistance in the circuit, ensuring that the lengths $l$ and $(100-l)$ accurately represent the resistances $P$ and $Q$.
</details>

**Q3.** 🟡 Why is it advised to obtain the balance point near the middle of the wire ($50\text{ cm}$ mark)? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. It makes the bridge most sensitive to small changes in resistance.
2. The percentage error in measurement of lengths $l$ and $(100-l)$ is minimized.
3. It minimizes the error due to end corrections (the resistance of the copper strips at the ends).
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ In a meter bridge experiment, null point is obtained at $20\text{ cm}$ from one end of the wire when resistance $X$ is balanced against another resistance $Y$. If $X < Y$, then where will be the new position of the null point from the same end, if one decides to balance a resistance of $4X$ against $Y$?

(a) $50\text{ cm}$ &emsp; (b) $80\text{ cm}$ &emsp; (c) $40\text{ cm}$ &emsp; (d) $70\text{ cm}$

<details>
<summary><b>Answer</b></summary>

Given $X < Y$. Since $l = 20\text{ cm}$, the ratio is $20/80 = 1/4$.
This means $X/Y = 1/4 \implies Y = 4X$.
Now we balance $4X$ against $Y$.
Ratio $= (4X) / Y = (4X) / (4X) = 1$.
So $\frac{l'}{100 - l'} = 1 \implies l' = 100 - l' \implies 2l' = 100 \implies l' = \mathbf{50\text{ cm}}$.

**Answer: (a)**
</details>

**Q2.** 🔴 The resistance of a wire is $R$ ohm. If it is melted and stretched to $n$ times its original length, its new resistance will be:
*(Wait, this is a Ch 4 concept! Sometimes JEE mixes basic concepts into instrument questions. Let's see how it applies to a meter bridge gap).*
If this new wire is placed in the left gap of a meter bridge and $R$ in the right gap, the balance point $l$ is:

(a) $\frac{n}{n+1} \times 100$ &emsp; (b) $\frac{n^2}{n^2+1} \times 100$ &emsp; (c) $\frac{1}{n^2+1} \times 100$ &emsp; (d) $\frac{1}{n+1} \times 100$

<details>
<summary><b>Answer</b></summary>

When stretched to $n$ times length, volume is constant. New resistance $R' = n^2 R$.
Left gap = $n^2 R$. Right gap = $R$.
$\frac{n^2 R}{R} = \frac{l}{100 - l} \implies n^2 = \frac{l}{100 - l}$
$100 n^2 - l n^2 = l \implies 100 n^2 = l(1 + n^2) \implies l = \mathbf{\frac{100 n^2}{n^2 + 1}}$.

**Answer: (b)**
</details>

**Q3.** 🔴 ⭐ In a meter bridge, the wire of length $1\text{m}$ has a non-uniform cross-section such that the variation of its resistance $R$ with length $l$ is $dR/dl \propto 1/\sqrt{l}$. Two equal resistances are connected as shown. The galvanometer has zero deflection when the jockey is at point P. What is the length AP?

(a) $0.2\text{ m}$ &emsp; (b) $0.25\text{ m}$ &emsp; (c) $0.3\text{ m}$ &emsp; (d) $0.35\text{ m}$

<details>
<summary><b>Answer</b></summary>

Since the left and right gaps have equal resistances ($R_{left} = R_{right}$), for the bridge to be balanced, the resistance of the wire segment AP must equal the resistance of PB.
$R_{AP} = R_{PB}$.
Given $dR = k \frac{dl}{\sqrt{l}} = k l^{-1/2} dl$.
Resistance of length $x$: $R(x) = \int_0^x k l^{-1/2} dl = k [2 l^{1/2}]_0^x = 2k\sqrt{x}$.
Let AP = $x$. Then PB = $1 - x$ (since total length is $1\text{m}$).
$R_{AP} = 2k\sqrt{x}$.
$R_{PB} = \text{Total Resistance} - R_{AP} = 2k\sqrt{1} - 2k\sqrt{x} = 2k(1 - \sqrt{x})$.
Equating them: $2k\sqrt{x} = 2k(1 - \sqrt{x})$
$\sqrt{x} = 1 - \sqrt{x} \implies 2\sqrt{x} = 1 \implies \sqrt{x} = 1/2$.
Squaring both sides: $x = 1/4\text{ m} = \mathbf{0.25\text{ m}}$.
*(This is a phenomenal JEE Advanced style question testing integration!)*

**Answer: (b)**
</details>

---

*Next: [Chapter 14 — Potentiometer →](./14_potentiometer.md)*
