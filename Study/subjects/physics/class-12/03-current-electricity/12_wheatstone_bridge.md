# Chapter 12: Wheatstone Bridge

> *NCERT Section 3.14*

---

## 🎯 Stage 1: The Core Idea

### The Diamond of Resistors

Imagine four resistors arranged in a diamond (or a square) shape. A battery connects to two opposite corners. A Galvanometer (a sensitive current detector) connects to the other two opposite corners.

This specific arrangement of four resistors ($P, Q, R, S$) is called a **Wheatstone Bridge**.

**The Magic Trick: "Balancing" the Bridge**
When current enters the diamond, it splits into two paths: the upper path and the lower path. 
Normally, some current will flow through the middle wire containing the galvanometer because the two paths have different voltage drops.

But, if you perfectly adjust the four resistors such that the voltage drops are proportional, the two middle corners will reach the **exact same electrical potential**.
Since water only flows downhill, and these two points are at the exact same "height," **no current flows through the middle wire.**

This state is called a **Balanced Wheatstone Bridge**. It is the most accurate way to measure an unknown resistance because it relies on a "null deflection" (reading exactly zero), which means the internal resistance of the battery or galvanometer won't affect the final result.

---

## 🔬 Stage 2: The Formula Lab

### The Balancing Condition

For a Wheatstone bridge with arms $P, Q, R, S$, and a galvanometer in the middle:

If the bridge is balanced ($I_g = 0$):
$$\frac{P}{Q} = \frac{R}{S}$$
*(or equivalently, $\frac{P}{R} = \frac{Q}{S}$)*

**What this means:** The ratio of the resistances in the upper arms equals the ratio of the resistances in the lower arms.

### The Beauty of a Balanced Bridge
If $\frac{P}{Q} = \frac{R}{S}$, then:
1. Current through the galvanometer is zero ($I_g = 0$).
2. The central resistor/galvanometer can be **completely removed** from the circuit for calculations.
3. The circuit simplifies drastically into $(P \text{ series } Q)$ parallel with $(R \text{ series } S)$.
   $R_{eq} = \frac{(P+Q)(R+S)}{(P+Q) + (R+S)}$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Checking for Balance and Finding Equivalent Resistance ⭐

**Pattern:** "Given a 5-resistor network, check if it's balanced and find $R_{eq}$."

**Solved Example** 🟢

> Five resistors are connected as a Wheatstone bridge. $P = 10\text{ } \Omega, Q = 20\text{ } \Omega, R = 30\text{ } \Omega, S = 60\text{ } \Omega$. A $50\text{ } \Omega$ galvanometer is in the middle. Find the equivalent resistance.

<details>
<summary><b>Solution</b></summary>

**Step 1: Check balance condition.**
Left ratio: $P/R = 10/30 = 1/3$.
Right ratio: $Q/S = 20/60 = 1/3$.
Since $1/3 = 1/3$, the **bridge is balanced**.

**Step 2: Remove the middle.**
The $50\text{ } \Omega$ resistor in the middle carries no current. Delete it.

**Step 3: Calculate $R_{eq}$.**
Top branch: $P + Q = 10 + 20 = 30\text{ } \Omega$.
Bottom branch: $R + S = 30 + 60 = 90\text{ } \Omega$.
These two branches are in parallel.
$R_{eq} = \frac{30 \times 90}{30 + 90} = \frac{2700}{120} = \mathbf{22.5\text{ } \Omega}$.
</details>

**Practice:**

1. 🟢 $P=2\text{ } \Omega, Q=4\text{ } \Omega, R=3\text{ } \Omega, S=6\text{ } \Omega$. The central resistor is $10\text{ } \Omega$. Is the bridge balanced?<br> Find $R_{eq}$.

<details>
<summary><b>Answer</b></summary>

$P/Q = 2/4 = 1/2$. $R/S = 3/6 = 1/2$. Balanced!
Delete middle. Top branch = $2+4=6\text{ } \Omega$. Bottom branch = $3+6=9\text{ } \Omega$.
$R_{eq} = (6 \times 9) / (6 + 9) = 54 / 15 = \mathbf{3.6\text{ } \Omega}$.
</details>

2. 🟡 Four identical resistors $R$ form the arms of a Wheatstone bridge. A fifth resistor $R$ is connected between the middle points. Find the equivalent resistance.

<details>
<summary><b>Answer</b></summary>

$R/R = R/R \implies 1 = 1$. It is balanced.
Delete the middle $R$.
Top branch = $R+R=2R$. Bottom branch = $R+R=2R$.
$R_{eq} = (2R \times 2R) / (2R + 2R) = 4R^2 / 4R = \mathbf{R}$.
</details>

3. 🟢 Five resistors are connected to form a Wheatstone bridge. $P = 5\text{ }\Omega$, $Q = 15\text{ }\Omega$, $R = 8\text{ }\Omega$, $S = 24\text{ }\Omega$. The galvanometer resistance is $12\text{ }\Omega$. Determine if the bridge is balanced and find the equivalent resistance between the input terminals.

<details>
<summary><b>Answer</b></summary>

The balance condition is:
$$\frac{P}{Q} = \frac{5}{15} = \frac{1}{3}$$
$$\frac{R}{S} = \frac{8}{24} = \frac{1}{3}$$
Since $\frac{P}{Q} = \frac{R}{S}$, the **bridge is balanced**.
No current flows through the $12\text{ }\Omega$ galvanometer; we can delete it.
The upper branch resistance is $P + Q = 5 + 15 = 20\text{ }\Omega$.
The lower branch resistance is $R + S = 8 + 24 = 32\text{ }\Omega$.
The equivalent resistance is:
$$R_{eq} = \frac{20 \times 32}{20 + 32} = \frac{640}{52} = \mathbf{\frac{160}{13}\text{ }\Omega \approx 12.31\text{ }\Omega}$$
</details>

4. 🟡 ⭐ In a Wheatstone bridge, the resistances of the four arms are $P = 3\text{ }\Omega$, $Q = 6\text{ }\Omega$, $R = 6\text{ }\Omega$, $S = 12\text{ }\Omega$. A galvanometer of resistance $8\text{ }\Omega$ is connected across the junctions of $P, Q$ and $R, S$. Find the equivalent resistance of the circuit.

<details>
<summary><b>Answer</b></summary>

Check balance:
$$\frac{P}{Q} = \frac{3}{6} = \frac{1}{2}$$
$$\frac{R}{S} = \frac{6}{12} = \frac{1}{2}$$
The bridge is balanced, so no current flows through the $8\text{ }\Omega$ galvanometer.
Remove the galvanometer. The upper branch resistance is $P + Q = 3 + 6 = 9\text{ }\Omega$.
The lower branch resistance is $R + S = 6 + 12 = 18\text{ }\Omega$.
The equivalent resistance is:
$$R_{eq} = \frac{9 \times 18}{9 + 18} = \frac{162}{27} = \mathbf{6\text{ }\Omega}$$
</details>

5. 🟡 Five resistors are connected such that $P = 4\text{ }\Omega$, $Q = 8\text{ }\Omega$, $R = 12\text{ }\Omega$, $S = 24\text{ }\Omega$. A resistor of $10\text{ }\Omega$ is connected in the galvanometer arm. If a potential difference of $6\text{ V}$ is applied across the bridge, calculate the total current drawn from the source.

<details>
<summary><b>Answer</b></summary>

Check balance:
$$\frac{P}{Q} = \frac{4}{8} = 0.5$$
$$\frac{R}{S} = \frac{12}{24} = 0.5$$
Since they are equal, the bridge is balanced. We remove the $10\text{ }\Omega$ central resistor.
Equivalent resistance of the top branch: $P + Q = 4 + 8 = 12\text{ }\Omega$.
Equivalent resistance of the bottom branch: $R + S = 12 + 24 = 36\text{ }\Omega$.
Total equivalent resistance $R_{eq}$ is:
$$R_{eq} = \frac{12 \times 36}{12 + 36} = \frac{432}{48} = 9\text{ }\Omega$$
Total current drawn is:
$$I = \frac{V}{R_{eq}} = \frac{6\text{ V}}{9\text{ }\Omega} = \mathbf{\frac{2}{3}\text{ A} \approx 0.67\text{ A}}$$
</details>

6. 🟡 In a balanced Wheatstone bridge, $P = 8\text{ }\Omega$, $Q = 12\text{ }\Omega$, $R = 4\text{ }\Omega$, and $S = 6\text{ }\Omega$. Calculate the equivalent resistance if a galvanometer of $15\text{ }\Omega$ is connected across the bridge.

<details>
<summary><b>Answer</b></summary>

Check balance:
$$\frac{P}{Q} = \frac{8}{12} = \frac{2}{3}$$
$$\frac{R}{S} = \frac{4}{6} = \frac{2}{3}$$
Since $\frac{P}{Q} = \frac{R}{S}$, the bridge is balanced and no current passes through the $15\text{ }\Omega$ galvanometer.
Removing the galvanometer leaves the upper branch ($P+Q = 8+12 = 20\text{ }\Omega$) and the lower branch ($R+S = 4+6 = 10\text{ }\Omega$) in parallel.
$$R_{eq} = \frac{20 \times 10}{20 + 10} = \frac{200}{30} = \mathbf{\frac{20}{3}\text{ }\Omega \approx 6.67\text{ }\Omega}$$
</details>

7. 🔴 ⭐ Five resistors are arranged in a Wheatstone bridge. $P = R_0$, $Q = 2R_0$, $R = 2R_0$, $S = 4R_0$. The galvanometer has a resistance of $5R_0$. Find the ratio of the equivalent resistance of this bridge to a single resistor $R_0$.

<details>
<summary><b>Answer</b></summary>

Check the balance condition:
$$\frac{P}{Q} = \frac{R_0}{2R_0} = \frac{1}{2}$$
$$\frac{R}{S} = \frac{2R_0}{4R_0} = \frac{1}{2}$$
Since the ratios are equal, the bridge is balanced. The $5R_0$ galvanometer does not carry any current and can be omitted.
The equivalent resistance of the top branch is $P + Q = R_0 + 2R_0 = 3R_0$.
The equivalent resistance of the bottom branch is $R + S = 2R_0 + 4R_0 = 6R_0$.
The combined equivalent resistance is:
$$R_{eq} = \frac{3R_0 \times 6R_0}{3R_0 + 6R_0} = \frac{18R_0^2}{9R_0} = 2R_0$$
The ratio of $R_{eq}$ to $R_0$ is:
$$\frac{R_{eq}}{R_0} = \frac{2R_0}{R_0} = \mathbf{2}$$
</details>

8. 🟢 In a bridge circuit, $P = 1.5\text{ }\Omega$, $Q = 3.0\text{ }\Omega$, $R = 4.5\text{ }\Omega$, and $S = 9.0\text{ }\Omega$. The galvanometer resistance is $100\text{ }\Omega$. Find the equivalent resistance.

<details>
<summary><b>Answer</b></summary>

Check balance:
$$\frac{P}{Q} = \frac{1.5}{3.0} = 0.5$$
$$\frac{R}{S} = \frac{4.5}{9.0} = 0.5$$
The bridge is balanced, so we remove the $100\text{ }\Omega$ galvanometer.
Upper arm resistance: $P+Q = 1.5 + 3.0 = 4.5\text{ }\Omega$.
Lower arm resistance: $R+S = 4.5 + 9.0 = 13.5\text{ }\Omega$.
Equivalent resistance:
$$R_{eq} = \frac{4.5 \times 13.5}{4.5 + 13.5} = \frac{60.75}{18} = \mathbf{3.375\text{ }\Omega}$$
</details>

---

### Type 2: Finding an Unknown Resistance ⭐⭐

**Pattern:** "The bridge is balanced. Find the value of one missing resistor."

**Solved Example** 🟡

> In a Wheatstone bridge, $P = 15\text{ } \Omega$, $Q = 10\text{ } \Omega$, $R = 3\text{ } \Omega$. What should be the value of $S$ so that the galvanometer shows zero deflection?<br>

<details>
<summary><b>Solution</b></summary>

Zero deflection means the bridge is balanced.
$\frac{P}{Q} = \frac{R}{S}$
$\frac{15}{10} = \frac{3}{S}$
$1.5 = \frac{3}{S} \implies S = \frac{3}{1.5} = \mathbf{2\text{ } \Omega}$.
</details>

**Practice:**

1. 🟢 $P=100\text{ } \Omega, Q=10\text{ } \Omega, R=X, S=5\text{ } \Omega$. The bridge is balanced. Find $X$.

<details>
<summary><b>Answer</b></summary>

$100 / 10 = X / 5$
$10 = X / 5 \implies X = \mathbf{50\text{ } \Omega}$.
</details>

2. 🟡 To balance a Wheatstone bridge, a resistance of $12\text{ } \Omega$ is needed in the S arm. However, the student only has an $18\text{ } \Omega$ resistor. What resistance should he connect in parallel with the $18\text{ } \Omega$ resistor to achieve balance?<br>

<details>
<summary><b>Answer</b></summary>

We need $S_{eq} = 12\text{ } \Omega$.
Let the required parallel resistor be $R_x$.
$\frac{1}{12} = \frac{1}{18} + \frac{1}{R_x}$
$\frac{1}{R_x} = \frac{1}{12} - \frac{1}{18} = \frac{3 - 2}{36} = \frac{1}{36}$
$R_x = \mathbf{36\text{ } \Omega}$.
</details>

3. 🟢 In a balanced Wheatstone bridge, $P = 18\text{ }\Omega$, $Q = 6\text{ }\Omega$, and $S = 5\text{ }\Omega$. Find the value of the unknown resistance $R$.

<details>
<summary><b>Answer</b></summary>

For a balanced Wheatstone bridge:
$$\frac{P}{Q} = \frac{R}{S}$$
Substitute the given values:
$$\frac{18}{6} = \frac{R}{5} \implies 3 = \frac{R}{5} \implies R = 3 \times 5 = \mathbf{15\text{ }\Omega}$$
</details>

4. 🟡 ⭐ In a Wheatstone bridge, the four arms have resistances $P = 12\text{ }\Omega$, $Q = 8\text{ }\Omega$, $R = 6\text{ }\Omega$, and $S = X$. When a resistor of $30\text{ }\Omega$ is connected in parallel with $S$, the bridge becomes balanced. Find the value of $X$.

<details>
<summary><b>Answer</b></summary>

The equivalent resistance of the $S$ arm is:
$$S_{eq} = \frac{30X}{30 + X}$$
For the bridge to be balanced:
$$\frac{P}{Q} = \frac{R}{S_{eq}} \implies \frac{12}{8} = \frac{6}{S_{eq}}$$
$$1.5 = \frac{6}{S_{eq}} \implies S_{eq} = \frac{6}{1.5} = 4\text{ }\Omega$$
Now set the expression for $S_{eq}$ equal to $4\text{ }\Omega$:
$$\frac{30X}{30 + X} = 4 \implies 30X = 120 + 4X \implies 26X = 120 \implies X = \frac{120}{26} = \mathbf{\frac{60}{13}\text{ }\Omega \approx 4.62\text{ }\Omega}$$
</details>

5. 🟡 Three arms of a Wheatstone bridge have resistances $P = 10\text{ }\Omega$, $Q = 20\text{ }\Omega$, and $R = 40\text{ }\Omega$. The fourth arm has resistance $S$, which consists of a resistor of unknown value $S_0$ in series with a $5\text{ }\Omega$ resistor. If the bridge is balanced, find the value of $S_0$.

<details>
<summary><b>Answer</b></summary>

For the bridge to be balanced:
$$\frac{P}{Q} = \frac{R}{S}$$
Here, $S = S_0 + 5$. Substituting the values:
$$\frac{10}{20} = \frac{40}{S_0 + 5} \implies 0.5 = \frac{40}{S_0 + 5}$$
$$S_0 + 5 = \frac{40}{0.5} = 80 \implies S_0 = 80 - 5 = \mathbf{75\text{ }\Omega}$$
</details>

6. 🟡 ⭐ A Wheatstone bridge is balanced with resistances $P = 10\text{ }\Omega$, $Q = 100\text{ }\Omega$, $R = 40\text{ }\Omega$, and $S = 400\text{ }\Omega$. If $P$ is changed to $11\text{ }\Omega$, what resistance must be connected in series with $R$ to restore balance?

<details>
<summary><b>Answer</b></summary>

Let the new resistance in the $R$ arm be $R' = R + \Delta R = 40 + \Delta R$.
For the bridge to be balanced:
$$\frac{P'}{Q} = \frac{R'}{S} \implies \frac{11}{100} = \frac{40 + \Delta R}{400}$$
Multiply both sides by $400$:
$$11 \times 4 = 40 + \Delta R \implies 44 = 40 + \Delta R \implies \Delta R = \mathbf{4\text{ }\Omega}$$
</details>

7. 🔴 In a Wheatstone bridge, $P = 1000\text{ }\Omega$, $Q = 100\text{ }\Omega$. The arm $R$ contains a standard variable resistance box, and $S$ is the unknown resistor. The bridge is balanced when $R$ is adjusted to $326\text{ }\Omega$. If $P$ and $Q$ are interchanged, the bridge is balanced when $R$ is adjusted to $3265\text{ }\Omega$. Find the true value of $S$ (taking the geometric mean to eliminate systematic ratio error).

<details>
<summary><b>Answer</b></summary>

Let the actual ratio be $k = P/Q \approx 10$.
In the first case:
$$S = \frac{Q}{P} R_1 = \frac{1}{k} (326)$$
In the second case, when $P$ and $Q$ are interchanged:
$$S = \frac{P}{Q} R_2 = k (3265)$$
Taking the geometric mean of the two measurements eliminates $k$:
$$S^2 = S \times S = \frac{1}{k} R_1 \times k R_2 = R_1 R_2$$
$$S = \sqrt{R_1 R_2} = \sqrt{326 \times 3265} = \sqrt{1064390} \approx \mathbf{1031.69\text{ }\Omega}$$
</details>

8. 🟢 Four resistors of resistances $P = 5\text{ }\Omega$, $Q = 10\text{ }\Omega$, $R = X$, and $S = 30\text{ }\Omega$ form a Wheatstone bridge. If the galvanometer shows zero current, calculate $X$.

<details>
<summary><b>Answer</b></summary>

Since the galvanometer current is zero, the bridge is balanced:
$$\frac{P}{Q} = \frac{R}{S}$$
Substitute the given values:
$$\frac{5}{10} = \frac{X}{30} \implies 0.5 = \frac{X}{30} \implies X = 0.5 \times 30 = \mathbf{15\text{ }\Omega}$$
</details>

---

### Type 3: Hidden Wheatstone Bridges ⭐⭐⭐

**Pattern:** "A circuit doesn't look like a diamond, but it actually is a Wheatstone bridge."

> 🔑 **THE MASTER TRICK:**
> Watch out for these common "Hidden" shapes:
> 1. **The 'A' Frame:** Looks like the letter A with a resistor crossing the middle.
> 2. **The Folded Square:** A square with diagonals. Pull the corners apart and it becomes a diamond!
> 3. **The Circle:** Five resistors forming a circle with a cross.
> 
> *Rule of thumb: If you see exactly 5 resistors and two input/output nodes, it is almost certainly a Wheatstone bridge.*

**Solved Example** 🔴

> A circuit has three resistors $R_1, R_2, R_3$ in series. A wire connects the start of $R_1$ to the end of $R_2$ with a resistor $R_4$. Another wire connects the end of $R_1$ to the end of $R_3$ with a resistor $R_5$. Is this a Wheatstone bridge?<br>

<details>
<summary><b>Solution</b></summary>

Yes! Draw the nodes.
Let Input be A (start of $R_1$). Let Output be B (end of $R_3$).
Let node C be between $R_1$ and $R_2$. Let node D be between $R_2$ and $R_3$.
$R_1$ is between A and C.
$R_2$ is between C and D. (This is the galvanometer arm!)
$R_3$ is between D and B.
$R_4$ is between A and D.
$R_5$ is between C and B.
If you redraw it, $R_2$ sits perfectly in the middle of the bridge formed by $R_1, R_4, R_5, R_3$.
If $R_1/R_4 = R_5/R_3$, then $R_2$ carries no current!
</details>

**Practice:**

1. 🟡 Five resistors of $10\text{ } \Omega$ each are arranged to form a pentagon. A battery is connected across two adjacent corners. Is it a Wheatstone bridge?<br>

<details>
<summary><b>Answer</b></summary>

**No.** A Wheatstone bridge requires two nodes for input/output and two nodes for the middle bridge. A pentagon across adjacent corners doesn't fit the topological structure of a bridge. It's just a series-parallel circuit.
</details>

2. 🔴 Six resistors form the edges of a tetrahedron. You measure resistance across any one edge. Can you use Wheatstone bridge symmetry here?<br>

<details>
<summary><b>Answer</b></summary>

**Yes!** If you measure across edge AB, the other two nodes C and D form the "middle" arm of the bridge. The edge CD will act as the galvanometer arm. Due to symmetry, the bridge is balanced, and no current flows through CD. You can remove edge CD and solve it easily.
</details>

3. 🟡 ⭐ Five identical resistors, each of resistance $R$, are connected in the form of a letter "A", where the horizontal crossbar represents one resistor and the others form the two legs. A battery is connected across the bottom ends of the legs. Find the equivalent resistance.

<details>
<summary><b>Answer</b></summary>

Let the bottom terminals be A and B. The top vertex is C. The endpoints of the crossbar are D (on leg AC) and E (on leg BC).
The resistors are:
- $R_{AD} = R$
- $R_{DC} = R$
- $R_{CE} = R$
- $R_{EB} = R$
- $R_{DE} = R$ (the crossbar)
We want to find $R_{eq}$ between A and B. This is a Wheatstone bridge configuration!
The ratio of upper-left to lower-left is $R_{CD}/R_{DA} = R/R = 1$.
The ratio of upper-right to lower-right is $R_{CE}/R_{EB} = R/R = 1$.
Since the ratios are equal, the bridge is balanced. No current flows through the crossbar resistor $R_{DE}$.
Removing $R_{DE}$ leaves two branches in parallel between A and B via C:
- Branch 1: $R_{AC} = R_{AD} + R_{DC} = R + R = 2R$.
- Branch 2: $R_{BC} = R_{BE} + R_{EC} = R + R = 2R$.
Therefore, the equivalent resistance is:
$$R_{eq} = \frac{2R \times 2R}{2R + 2R} = \mathbf{R}$$
</details>

4. 🟡 A network of five resistors is connected across nodes A and B. $R_{AC} = 6\text{ }\Omega$, $R_{AD} = 3\text{ }\Omega$, $R_{CB} = 12\text{ }\Omega$, $R_{DB} = 6\text{ }\Omega$, and $R_{CD} = 8\text{ }\Omega$. Find the equivalent resistance between A and B.

<details>
<summary><b>Answer</b></summary>

This is a Wheatstone bridge where:
- Input is A, Output is B.
- Internal nodes are C and D.
- $P = R_{AC} = 6\text{ }\Omega$, $Q = R_{CB} = 12\text{ }\Omega$
- $R = R_{AD} = 3\text{ }\Omega$, $S = R_{DB} = 6\text{ }\Omega$
- Central arm $G = R_{CD} = 8\text{ }\Omega$
Check balance:
$$\frac{R_{AC}}{R_{CB}} = \frac{6}{12} = 0.5$$
$$\frac{R_{AD}}{R_{DB}} = \frac{3}{6} = 0.5$$
Since the ratios are equal, the bridge is balanced. No current flows through $R_{CD}$.
Remove $R_{CD}$.
The upper branch resistance is $R_{AC} + R_{CB} = 6 + 12 = 18\text{ }\Omega$.
The lower branch resistance is $R_{AD} + R_{DB} = 3 + 6 = 9\text{ }\Omega$.
The equivalent resistance is:
$$R_{eq} = \frac{18 \times 9}{18 + 9} = \frac{162}{27} = \mathbf{6\text{ }\Omega}$$
</details>

5. 🟡 ⭐ Five capacitors, each of capacitance $C$, are connected in a Wheatstone bridge style. A battery of voltage $V$ is connected across the terminals. What is the equivalent capacitance of the network?

<details>
<summary><b>Answer</b></summary>

The balance condition for a capacitive bridge is:
$$\frac{C_1}{C_2} = \frac{C_3}{C_4}$$
Since all capacitors have capacitance $C$, $\frac{C}{C} = \frac{C}{C} = 1$. The bridge is balanced.
No charge flows through the diagonal capacitor. We can remove it.
The remaining network consists of two branches in parallel, each containing two capacitors in series:
- Series capacitance of branch 1: $C_s = \frac{C \times C}{C + C} = 0.5C$.
- Series capacitance of branch 2: $C_s = 0.5C$.
The total equivalent capacitance of these two parallel branches is:
$$C_{eq} = 0.5C + 0.5C = \mathbf{C}$$
</details>

6. 🔴 A square loop ABCD is made of a uniform wire of resistance per unit length $\lambda$. A diagonal wire BD of the same material and thickness is connected. If a potential difference is applied across the opposite corners A and C, find the equivalent resistance of the network. Let the side length of the square be $L$.

<details>
<summary><b>Answer</b></summary>

Let's find the resistances of the sections:
- Resistance of side AB = $R_{AB} = \lambda L$
- Resistance of side BC = $R_{BC} = \lambda L$
- Resistance of side AD = $R_{AD} = \lambda L$
- Resistance of side DC = $R_{DC} = \lambda L$
- Resistance of diagonal BD = $R_{BD} = \lambda (\sqrt{2} L)$
The battery is connected across A and C.
This forms a bridge where:
- Input is A, Output is C.
- Internal nodes are B and D.
- The branches are $R_{AB}, R_{BC}, R_{AD}, R_{DC}$.
- The diagonal resistor $R_{BD}$ acts as the galvanometer arm.
Let's check the balance condition:
$$\frac{R_{AB}}{R_{BC}} = \frac{\lambda L}{\lambda L} = 1$$
$$\frac{R_{AD}}{R_{DC}} = \frac{\lambda L}{\lambda L} = 1$$
Since the ratios are equal, the bridge is balanced. No current flows through the diagonal wire BD.
We can remove the diagonal wire BD.
The equivalent resistance is the parallel combination of the top branch (ABC) and bottom branch (ADC):
- Top branch resistance = $R_{AB} + R_{BC} = 2\lambda L$.
- Bottom branch resistance = $R_{AD} + R_{DC} = 2\lambda L$.
$$R_{eq} = \frac{2\lambda L \times 2\lambda L}{2\lambda L + 2\lambda L} = \mathbf{\lambda L}$$
</details>

7. 🟡 Five resistors are connected in a bridge circuit. The nodes are labeled 1, 2, 3, and 4. The resistors are connected as: $R_{12} = 5\text{ }\Omega$, $R_{23} = 10\text{ }\Omega$, $R_{34} = 8\text{ }\Omega$, $R_{14} = 4\text{ }\Omega$, and $R_{24} = 12\text{ }\Omega$. Terminals 1 and 3 are connected to a $20\text{ V}$ battery. Determine if the bridge is balanced and find the current through $R_{24}$.

<details>
<summary><b>Answer</b></summary>

Let's trace the bridge:
- Input node: 1, Output node: 3.
- Internal nodes: 2 and 4.
- $P = R_{12} = 5\text{ }\Omega$, $Q = R_{23} = 10\text{ }\Omega$.
- $R = R_{14} = 4\text{ }\Omega$, $S = R_{34} = 8\text{ }\Omega$.
- The central arm is $R_{24} = 12\text{ }\Omega$.
Check balance:
$$\frac{P}{Q} = \frac{5}{10} = 0.5$$
$$\frac{R}{S} = \frac{4}{8} = 0.5$$
Since the ratios are equal, the bridge is balanced. The potential at node 2 is equal to the potential at node 4 ($V_2 = V_4$).
Therefore, the current through $R_{24}$ is **0 A**.
</details>

8. 🔴 Five resistors are connected between terminals X and Y. Two parallel lines of resistors are crossed by a bridge resistor. $R_1 = 3\text{ }\Omega$, $R_2 = 9\text{ }\Omega$, $R_3 = 2\text{ }\Omega$, $R_4 = 6\text{ }\Omega$, and the bridge resistor is $R_5 = 5\text{ }\Omega$. If the input voltage is $12\text{ V}$, calculate the equivalent resistance and the total current.

<details>
<summary><b>Answer</b></summary>

Check balance:
$$\frac{R_1}{R_2} = \frac{3}{9} = \frac{1}{3}$$
$$\frac{R_3}{R_4} = \frac{2}{6} = \frac{1}{3}$$
Since $\frac{R_1}{R_2} = \frac{R_3}{R_4}$, the bridge is balanced and $R_5$ is removed.
Upper branch: $R_{top} = R_1 + R_2 = 3 + 9 = 12\text{ }\Omega$.
Lower branch: $R_{bottom} = R_3 + R_4 = 2 + 6 = 8\text{ }\Omega$.
Equivalent resistance:
$$R_{eq} = \frac{12 \times 8}{12 + 8} = \frac{96}{20} = \mathbf{4.8\text{ }\Omega}$$
Total current drawn:
$$I = \frac{V}{R_{eq}} = \frac{12\text{ V}}{4.8\text{ }\Omega} = \mathbf{2.5\text{ A}}$$
</details>

---

## 🧱 Stage 4: MCQ Mastery

**Q1.** In a Wheatstone bridge experiment, a student closes the galvanometer key ($K_g$) before closing the battery key ($K_b$). What is the most likely consequence of this action?

(a) The bridge cannot be balanced.
(b) A large self-induced back-EMF can cause a sudden kick in the galvanometer, potentially damaging it.
(c) The sensitivity of the bridge increases.
(d) The equivalent resistance of the bridge changes.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Due to self-induction in the resistive arms (which always have some residual inductance), when the battery key is closed, the current takes a small but finite time to reach its steady value. If the galvanometer key is already closed, this transient current will flow through the galvanometer, causing a violent deflection ("kick") that can damage the delicate coil suspension. Therefore, the battery key $K_b$ must always be closed first, and then the galvanometer key $K_g$ after the current has stabilized.
</details>

**Q2.** A Wheatstone bridge is balanced with four resistors $P$, $Q$, $R$, and $S$. If the temperature of the resistor $P$ increases due to continuous current flow, how will the balance point change? (Assume all resistors are made of metallic conductors).

(a) The balance point remains unchanged because temperature has no effect on resistance.
(b) The bridge will become unbalanced, and to restore balance, the resistance of $Q$ must be increased or $S$ must be decreased.
(c) The bridge will become unbalanced, and to restore balance, the resistance of $R$ must be increased.
(d) Both (b) and (c) are correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

As the temperature of the metallic resistor $P$ increases, its resistance increases ($P' > P$). The balancing condition $\frac{P}{Q} = \frac{R}{S}$ is violated because $\frac{P'}{Q} > \frac{R}{S}$. To restore balance, we must either increase the denominator $Q$ (making the left ratio smaller), increase the numerator $R$ (making the right ratio larger), or decrease the denominator $S$ (making the right ratio larger). Thus, both options (b) and (c) are valid methods to restore balance.
</details>

**Q3.** In a balanced Wheatstone bridge, the galvanometer and the battery are interchanged. The new balancing condition will:

(a) depend on the internal resistance of the battery.
(b) depend on the resistance of the galvanometer.
(c) remain exactly the same as the original balancing condition.
(d) become the reciprocal of the original condition.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The original balancing condition is $\frac{P}{Q} = \frac{R}{S}$, which is equivalent to $\frac{P}{R} = \frac{Q}{S}$. When the battery and galvanometer are interchanged, the galvanometer is connected across the terminals previously connected to the battery, and the battery is connected across the terminals previously connected to the galvanometer. The balance condition for this new configuration is $\frac{P}{R} = \frac{Q}{S}$, which mathematically simplifies to the same relation $\frac{P}{Q} = \frac{R}{S}$. Therefore, the balance condition is completely unaffected by the swap.
</details>

**Q4.** Statement I: A Wheatstone bridge is most sensitive when all the four resistances $P, Q, R,$ and $S$ are of the same order of magnitude.
Statement II: The galvanometer in a Wheatstone bridge always shows maximum deflection when its resistance is equal to the equivalent resistance of the rest of the bridge.

(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Statement I is true because when all four resistances are comparable, a small fractional change in the unknown resistance produces the maximum possible potential difference across the galvanometer, leading to the highest sensitivity. Statement II is also true (a direct consequence of the Jacobi Maximum Power Transfer Theorem, where matching the source resistance to the load resistance maximizes power transfer to the galvanometer), but it is not the physical explanation of why comparable branch resistances lead to high bridge sensitivity.
</details>

**Q5.** In the circuit of a balanced Wheatstone bridge, if the galvanometer is replaced by a high-resistance voltmeter:

(a) the voltmeter will read a non-zero voltage because it draws current.
(b) the voltmeter will read zero because the potential difference between the two junctions is zero.
(c) the bridge will become unbalanced.
(d) the equivalent resistance of the bridge will decrease.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

In a balanced Wheatstone bridge, the potential at the two junctions connected to the galvanometer branch is exactly equal ($V_c = V_d$). Replacing the galvanometer with a voltmeter (regardless of its internal resistance) does not change this fact because no current flows through that path, and the potential difference remains exactly zero. Thus, the voltmeter will read $0\text{ V}$.
</details>

**Q6.** Assertion: In a Wheatstone bridge, if a copper wire is used to connect the galvanometer instead of a high-resistance wire, the sensitivity of the bridge increases.
Reason: Copper has a very low resistivity, which minimizes the resistance of the galvanometer branch and increases the current through the galvanometer for a given deflection.

(a) Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.
(b) Both Assertion and Reason are true, but Reason is not the correct explanation of Assertion.
(c) Assertion is true, but Reason is false.
(d) Both Assertion and Reason are false.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

The sensitivity of a Wheatstone bridge is determined by the physical parameters of the galvanometer coil (number of turns, magnetic field) and the ratios/values of $P, Q, R,$ and $S$. Replacing connecting wires in the galvanometer branch with copper does not change the sensitivity of the bridge, as the resistance of connecting wires is already negligibly small. The reason is also false because the current through the galvanometer at balance is zero anyway, and near balance, it is dominated by the galvanometer's own coil resistance ($R_g \approx 10\text{ }\Omega$ to $100\text{ }\Omega$), not the connecting wires.
</details>

**Q7.** Under what condition will a Wheatstone bridge show "null deflection" regardless of the EMF of the battery?

(a) Only when the battery has zero internal resistance.
(b) When the temperature of the surroundings is kept at $0^\circ\text{C}$.
(c) When the ratio of the resistances of the adjacent arms are equal ($PS = QR$).
(d) When the galvanometer resistance is extremely high.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

The balance condition $\frac{P}{Q} = \frac{R}{S}$ can be cross-multiplied to give $PS = QR$. When this condition is satisfied, the potential difference between the galvanometer terminals is zero, which means $I_g = 0$. This holds true regardless of the EMF of the battery, as the ratio of potentials remains balanced at all supply voltages.
</details>

**Q8.** A Wheatstone bridge has four arms with resistances $P = 10\text{ }\Omega$, $Q = 100\text{ }\Omega$, $R = 40\text{ }\Omega$, and $S = 400\text{ }\Omega$. A galvanometer of resistance $15\text{ }\Omega$ is connected. To increase the sensitivity of the bridge, which of the following changes is most effective?

(a) Change all resistances to approximately $10\text{ }\Omega$ or $15\text{ }\Omega$.
(b) Change $Q$ to $1000\text{ }\Omega$ and $S$ to $4000\text{ }\Omega$.
(c) Replace the galvanometer with a $150\text{ }\Omega$ galvanometer.
(d) Increase the EMF of the battery to a very high value like $1000\text{ V}$.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

A Wheatstone bridge is most sensitive when all four arms have resistances of the same order of magnitude, and these resistances are comparable to the galvanometer resistance. Currently, the resistances range from $10\text{ }\Omega$ to $400\text{ }\Omega$. Making all of them comparable (around $10\text{ }\Omega$ to $15\text{ }\Omega$) maximizes the deflection of the galvanometer for a given fractional change in the unknown resistance.
</details>

**Q9.** In a Wheatstone bridge, the ratio arms $P$ and $Q$ are made equal. The bridge is balanced by adjusting $R$ to $50\text{ }\Omega$. If $P$ and $Q$ are now changed such that $P = 2Q$, what must be the new value of $R$ to maintain balance with the same unknown resistance $S$?

(a) $25\text{ }\Omega$
(b) $50\text{ }\Omega$
(c) $100\text{ }\Omega$
(d) $200\text{ }\Omega$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

Initially, $\frac{P}{Q} = 1$, which means $\frac{R}{S} = 1 \implies S = R = 50\text{ }\Omega$.
In the second case, $P = 2Q$, so the ratio $\frac{P}{Q} = 2$.
To maintain balance:
$$\frac{P}{Q} = \frac{R'}{S} \implies 2 = \frac{R'}{50} \implies R' = 2 \times 50 = \mathbf{100\text{ }\Omega}$$
</details>

**Q10.** What is the primary advantage of the null-deflection method in a Wheatstone bridge over a deflection method (using a voltmeter/ammeter)?

(a) It is faster to take measurements.
(b) It does not require any calibration of the galvanometer scale.
(c) The measurement is independent of the resistance of the galvanometer and the internal resistance of the battery.
(d) Both (b) and (c) are correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

In a null method, since the galvanometer current is zero at balance, its resistance does not enter the balance equation. Furthermore, since no current is drawn, there is no loading effect, and the measurement is independent of the internal resistance of the battery. Additionally, we only need to detect the zero point, meaning a calibrated scale on the galvanometer is unnecessary, eliminating scale calibration errors.
</details>

**Q11.** Statement I: An AC Wheatstone bridge (operated with an alternating current source) can be balanced using only resistors.
Statement II: AC bridges can also measure capacitance and inductance by replacing resistors with capacitors and inductors, provided both magnitude and phase conditions are balanced.

(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Statement I is true because if the bridge arms consist of pure resistances, the voltage drops remain in phase, and the balance condition is identical to the DC case: $\frac{P}{Q} = \frac{R}{S}$. Statement II is also true: AC bridges (like De Sauty's or Maxwell's bridge) use capacitors or inductors and require balancing both the magnitude and phase of the complex impedances ($\frac{Z_1}{Z_2} = \frac{Z_3}{Z_4}$). However, Statement II does not explain Statement I; it is a generalization of the concept.
</details>

**Q12.** In a Wheatstone bridge, the resistances of the four arms are $P = 10\text{ }\Omega$, $Q = 10\text{ }\Omega$, $R = 10\text{ }\Omega$, and $S = 11\text{ }\Omega$. The battery has an EMF of $2\text{ V}$ and zero internal resistance. The potential difference across the galvanometer (connected between the junction of $P, Q$ and the junction of $R, S$) is approximately:

(a) $0\text{ V}$
(b) $0.05\text{ V}$
(c) $0.1\text{ V}$
(d) $0.5\text{ V}$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Let the battery terminals be at potentials $2\text{ V}$ and $0\text{ V}$.
The junction between $P$ and $Q$ is C:
$$V_C = 2 \times \frac{Q}{P+Q} = 2 \times \frac{10}{20} = 1.0\text{ V}$$
The junction between $R$ and $S$ is D:
$$V_D = 2 \times \frac{S}{R+S} = 2 \times \frac{11}{10+11} = 2 \times \frac{11}{21} \approx 1.0476\text{ V}$$
The potential difference across the galvanometer is:
$$|V_C - V_D| = |1.0 - 1.0476| = 0.0476\text{ V} \approx \mathbf{0.05\text{ V}}$$
</details>

**Q13.** A Wheatstone bridge is set up to measure an unknown resistance $S$. During the measurement, the student notices that the galvanometer needle deflects to the left when the variable resistor $R$ is $100\text{ }\Omega$, and to the right when $R$ is $101\text{ }\Omega$. This indicates that:

(a) The bridge is defective.
(b) The true value of $R$ for balance lies between $100\text{ }\Omega$ and $101\text{ }\Omega$.
(c) The galvanometer has a zero error.
(d) The battery is discharged.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

Since the deflection direction reverses when $R$ goes from $100\text{ }\Omega$ to $101\text{ }\Omega$, the point of zero deflection (balance point) must lie between these two values. The student can interpolate or use a finer adjustment (like a slide-wire or fractional resistance box) to find the exact balance.
</details>

**Q14.** In an unbalanced Wheatstone bridge, the current through the galvanometer is zero when:

(a) the galvanometer resistance is infinite.
(b) the battery EMF is zero.
(c) the bridge is made of superconducting wires.
(d) Both (a) and (b) are correct.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (d)**

The galvanometer current is $I_g = \frac{V_C - V_D}{R_g + R_{th}}$, where $V_C - V_D$ is the open-circuit potential difference and $R_{th}$ is the Thevenin equivalent resistance.
- If $R_g \to \infty$ (open circuit), $I_g \to 0$ even if $V_C - V_D \neq 0$.
- If the battery EMF is $0$, then all node potentials are $0$, so $V_C - V_D = 0$, leading to $I_g = 0$.
Thus, both (a) and (b) are correct.
</details>

**Q15.** When a Wheatstone bridge is balanced, the current drawn from the battery is:

(a) zero, because the bridge is balanced.
(b) determined only by the sum of $P, Q, R, S$.
(c) independent of the galvanometer resistance.
(d) maximum, because the galvanometer is shorted.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

At balance, the current flowing through the galvanometer branch is exactly zero. Thus, the galvanometer behaves as an open circuit for the rest of the network. The equivalent resistance of the bridge is $R_{eq} = \frac{(P+Q)(R+S)}{P+Q+R+S}$, which is independent of the galvanometer's resistance $R_g$. Consequently, the total current drawn from the battery, $I = \frac{V}{R_{eq} + r}$, is also completely independent of $R_g$.
</details>

**Q16.** Statement I: If the battery key is kept closed for a long time in a Wheatstone bridge, the balancing condition might drift.
Statement II: The resistance of metallic resistors increases with temperature due to Joule heating ($I^2 R t$).

(a) Both Statement I and Statement II are true, and Statement II is the correct explanation of Statement I.
(b) Both Statement I and Statement II are true, but Statement II is not the correct explanation of Statement I.
(c) Statement I is true, but Statement II is false.
(d) Statement I is false, but Statement II is true.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

When the battery key is kept closed for a long time, current flows continuously through the resistors, producing Joule heat ($H = I^2 R t$). Since different arms have different resistances and heat dissipation rates, their temperatures rise unequally. For metallic conductors, resistance increases with temperature. This unequal change in resistances drifts the ratio $\frac{P}{Q}$ away from $\frac{R}{S}$, causing the balance point to drift. Thus, Statement II is the correct explanation of Statement I.
</details>

**Q17.** A Wheatstone bridge is balanced. The resistor in the arm $P$ is doubled, and the resistor in the arm $Q$ is halved. To re-balance the bridge:

(a) the resistor $R$ must be quadrupled.
(b) the resistor $S$ must be quadrupled.
(c) the resistor $R$ must be doubled.
(d) the resistor $S$ must be doubled.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

Initially, $\frac{P}{Q} = \frac{R}{S}$.
In the new state:
$$\frac{P'}{Q'} = \frac{2P}{Q/2} = 4 \left(\frac{P}{Q}\right)$$
To restore balance, the new ratio of the other two arms, $\frac{R'}{S'}$, must also be 4 times the original ratio $\frac{R}{S}$.
If we keep $S' = S$, we must have $R' = 4R$. Therefore, the resistor $R$ must be quadrupled.
</details>

**Q18.** In a Wheatstone bridge, the galvanometer has a shunt resistance connected across it during the initial stages of balancing. The purpose of this shunt is to:

(a) increase the sensitivity of the bridge.
(b) protect the galvanometer from damage by limiting the current flowing through it when the bridge is far from balance.
(c) make the balance point independent of the battery EMF.
(d) bypass the high resistance of the battery.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (b)**

When the bridge is far from balance, the potential difference across the galvanometer branch can be large, resulting in a high current that could burn out the sensitive galvanometer coil or bend its needle. A low-value shunt resistor is connected in parallel with the galvanometer to bypass most of the current. Once the bridge is nearly balanced (deflection is small), the shunt is disconnected to allow maximum sensitivity for final balancing.
</details>

**Q19.** An unknown resistance $X$ is measured using a Wheatstone bridge. If the known resistances $P$ and $Q$ are $10\text{ }\Omega$ and $100\text{ }\Omega$ respectively, and the bridge balances when $R = 25.4\text{ }\Omega$, the value of $X$ is:

(a) $2.54\text{ }\Omega$
(b) $25.4\text{ }\Omega$
(c) $254\text{ }\Omega$
(d) $0.254\text{ }\Omega$

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (c)**

For the balanced bridge, the relationship is:
$$\frac{P}{Q} = \frac{R}{X} \implies \frac{10}{100} = \frac{25.4}{X}$$
$$0.1 = \frac{25.4}{X} \implies X = \frac{25.4}{0.1} = \mathbf{254\text{ }\Omega}$$
</details>

**Q20.** Assertion: A Wheatstone bridge cannot be used to measure very low resistances (e.g., less than $1\text{ }\Omega$) accurately.
Reason: For low resistances, the resistance of the connecting copper wires and contact resistances become comparable to the resistance being measured, introducing significant errors.

(a) Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.
(b) Both Assertion and Reason are true, but Reason is not the correct explanation of Assertion.
(c) Assertion is true, but Reason is false.
(d) Both Assertion and Reason are false.

<details>
<summary><b>Answer & Explanation</b></summary>

**Answer: (a)**

The contact resistance at terminals and the resistance of the connecting leads in a standard Wheatstone bridge setup are typically between $0.01\text{ }\Omega$ and $0.1\text{ }\Omega$. When measuring a very low resistance (less than $1\text{ }\Omega$), these lead and contact resistances are added directly to the arm resistance, causing a very high percentage error in the final balance equation. Thus, the assertion is true, and the reason is the correct explanation.
</details>

---

## 🔀 Stage 5: Type Mixer

**Q1.** 🔴 In a Wheatstone bridge, $P = 10\text{ } \Omega, Q = 20\text{ } \Omega, R = 15\text{ } \Omega, S = 30\text{ } \Omega$. A $10\text{V}$ battery is connected. What is the current drawn from the battery?<br> What is the current through the $P$ resistor?<br>

<details>
<summary><b>Solution</b></summary>

$P/R = 10/15 = 2/3$. $Q/S = 20/30 = 2/3$. Bridge is balanced.
Top branch = $P+Q = 30\text{ } \Omega$. Bottom branch = $R+S = 45\text{ } \Omega$.
$R_{eq} = (30 \times 45) / (30 + 45) = 1350 / 75 = \mathbf{18\text{ } \Omega}$.
Total current $I = V / R_{eq} = 10 / 18 = \mathbf{0.55\text{ A}}$.

The voltage across the top branch is $10\text{V}$.
Current through $P$ = Current through top branch = $V / (P+Q) = 10 / 30 = \mathbf{0.33\text{ A}}$.
</details>

**Q2.** 🔴 ⭐ An unbalanced Wheatstone bridge has $P = 10\text{ } \Omega, Q = 5\text{ } \Omega, R = 5\text{ } \Omega, S = 10\text{ } \Omega$, and $G = 10\text{ } \Omega$. Find $R_{eq}$.

<details>
<summary><b>Solution</b></summary>

$P/Q = 2$, but $R/S = 0.5$. **Unbalanced.** You cannot delete $G$.
You must use Kirchhoff's rules (or delta-star transform if you know it).
Using Nodal Analysis: Let bottom corner be $0\text{V}$, top corner be $V$. Let left node be $x$ and right node be $y$.
KCL at $x$: $\frac{x-V}{10} + \frac{x-0}{5} + \frac{x-y}{10} = 0 \implies (x-V) + 2x + (x-y) = 0 \implies 4x - y = V$.
KCL at $y$: $\frac{y-V}{5} + \frac{y-0}{10} + \frac{y-x}{10} = 0 \implies 2(y-V) + y + (y-x) = 0 \implies -x + 4y = 2V$.
Solve for $x$ and $y$: Multiply first eq by 4: $16x - 4y = 4V$. Add to second: $15x = 6V \implies x = 0.4V$.
$y = 4x - V = 1.6V - V = 0.6V$.
Total current leaving top node $I = \frac{V-x}{10} + \frac{V-y}{5} = \frac{V-0.4V}{10} + \frac{V-0.6V}{5} = \frac{0.6V}{10} + \frac{0.4V}{5} = 0.06V + 0.08V = 0.14V$.
$R_{eq} = V / I = 1 / 0.14 = 100 / 14 = \mathbf{50/7 \text{ } \Omega \approx 7.14\text{ } \Omega}$.
</details>

---

## 📋 Stage 6: Board Arsenal

**Q1.** 🟢 What is the principle of a Wheatstone bridge?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

A Wheatstone bridge is an arrangement of four resistances ($P, Q, R, S$) used to determine an unknown resistance. Its principle is based on the **null deflection method**. When the bridge is balanced ($P/Q = R/S$), the potential difference between the opposite junctions is zero, and no current flows through the galvanometer connected between them.
</details>

**Q2.** 🟡 Why is the Wheatstone bridge method considered more accurate than measuring voltage and current separately to find resistance?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. It is a **null method** (galvanometer reading is zero at balance). Therefore, the internal resistance of the galvanometer and the battery do not affect the result.
2. It relies only on the ratios of known resistances, eliminating errors caused by measuring instruments like voltmeters and ammeters which can draw some current and skew readings.
</details>

**Q3.** 🟡 In a Wheatstone bridge, what happens to the balance point if the positions of the battery and the galvanometer are interchanged?<br> *(1 mark)*

<details>
<summary><b>Model Answer</b></summary>

The balance point **remains unchanged**. The bridge remains balanced ($P/R = Q/S$ is mathematically equivalent to $P/Q = R/S$).
</details>

---

## 🚀 Stage 7: JEE Mains Arena

**Q1.** 🟡 ⭐ In a Wheatstone bridge, all four arms have equal resistance $R$. If the resistance of the galvanometer arm is also $R$, the equivalent resistance of the combination as seen by the battery is:

(a) $R/2$ &emsp; (b) $R$ &emsp; (c) $2R$ &emsp; (d) $R/4$

<details>
<summary><b>Answer</b></summary>

Since all arms are $R$, $R/R = R/R$. The bridge is perfectly balanced.
The galvanometer resistance does not matter because no current flows through it.
Remove the galvanometer. Top branch = $R+R=2R$. Bottom branch = $R+R=2R$.
Parallel combination: $(2R)/2 = \mathbf{R}$.

**Answer: (b)**
</details>

**Q2.** 🔴 The four arms of a Wheatstone bridge have resistances $10\text{ } \Omega, 10\text{ } \Omega, 10\text{ } \Omega$ and $20\text{ } \Omega$. A galvanometer of $15\text{ } \Omega$ resistance is connected across the diagonal. Is the bridge balanced?<br> If not, what will be the qualitative direction of current through the galvanometer?<br>

<details>
<summary><b>Answer</b></summary>

Let $P=10, Q=10, R=10, S=20$.
$P/Q = 10/10 = 1$. $R/S = 10/20 = 0.5$.
$1 \neq 0.5$, so the bridge is **unbalanced**.
Let the battery be connected to left ($0\text{V}$) and right ($V$) nodes.
Top node $x$ is formed by $P$ and $Q$. $V_x = V(Q/(P+Q)) = V(10/20) = 0.5V$. (Assuming galvanometer draws negligible current initially to find potential difference).
Bottom node $y$ is formed by $R$ and $S$. $V_y = V(S/(R+S)) = V(20/30) = 0.67V$.
Since $V_y > V_x$, current flows from **y to x (bottom to top)** through the galvanometer.

**Answer: Unbalanced; Current flows from the junction of R,S to the junction of P,Q.**
</details>

**Q3.** 🔴 ⭐ Which of the following is true about the sensitivity of a Wheatstone bridge?<br>

(a) It is highest when all four resistances are roughly equal.
(b) It is highest when the galvanometer resistance is zero.
(c) It is independent of the battery EMF.
(d) It increases if we use very high resistances for $P$ and $Q$.

<details>
<summary><b>Answer</b></summary>

A Wheatstone bridge is most sensitive (gives the largest galvanometer deflection for a small unbalance) when the resistances in all four arms are **of the same order of magnitude** ($P \approx Q \approx R \approx S$). If the ratio is extreme (e.g., $1000 : 1$), a small change in the unknown resistor will barely move the galvanometer needle, making precise measurement difficult.

**Answer: (a)**
</details>

---

*Next: [Chapter 13 — Meter Bridge →](./13_meter_bridge.md)*
