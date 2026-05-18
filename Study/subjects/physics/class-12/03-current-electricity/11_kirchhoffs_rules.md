# Chapter 11: Kirchhoff's Rules

> *NCERT Section 3.13*

---

## 🎯 Stage 1: The Core Idea

### When Ohm's Law Fails Us

Ohm's Law ($V=IR$) and the simple series/parallel formulas work great for single-loop circuits or clean combinations. But what happens when a circuit has multiple batteries connected in different branches, and wires crisscrossing everywhere forming a web?<br> You can't simply define what is in series and what is in parallel anymore.

To solve complex networks, Gustav Kirchhoff gave us two universally true rules. They are not new physics; they are simply the restatement of two fundamental conservation laws: **Conservation of Charge** and **Conservation of Energy**.

### Rule 1: The Junction Rule (KCL)
**"What goes in, must come out."**
Imagine a water pipe that splits into three smaller pipes. The amount of water entering the junction every second must exactly equal the amount of water leaving through the three pipes. Water doesn't pile up at the junction, and it isn't created out of nothing.
- **Physics translation:** The sum of currents entering a junction equals the sum of currents leaving it. ($\sum I = 0$)
- **Based on:** Conservation of Charge.

### Rule 2: The Loop Rule (KVL)
**"What goes up, must come down."**
Imagine walking on a hilly hiking trail that eventually loops back to where you started. No matter how many hills you climb (gaining elevation) or valleys you descend (losing elevation), when you return to your exact starting point, your net change in elevation is exactly zero.
- **Physics translation:** The algebraic sum of all potential differences (voltages) around any closed loop in a circuit is zero. ($\sum \Delta V = 0$)
- **Based on:** Conservation of Energy.

---

## 🔬 Stage 2: The Formula Lab

### 1. Kirchhoff's Current Law (KCL)

At any junction (node):
$$\sum I_{in} = \sum I_{out}$$
or
$$\sum I = 0 \text{ (with proper sign convention)}$$

*Convention:* Entering junction = Positive ($+$), Leaving junction = Negative ($-$).

### 2. Kirchhoff's Voltage Law (KVL)

Around any closed loop:
$$\sum \Delta V = 0$$

> 🔑 **THE FOOLPROOF SIGN CONVENTION FOR KVL:**
> 1. Draw your arbitrary "Loop Direction" (clockwise or counter-clockwise).
> 2. **For Batteries:** 
>    - If you walk through the battery from Negative to Positive (climbing the hill), $\Delta V = +\varepsilon$.
>    - If you walk through from Positive to Negative (falling down), $\Delta V = -\varepsilon$.
> 3. **For Resistors:**
>    - If your loop direction is *with* the current, you are sliding down the resistor. $\Delta V = -IR$.
>    - If your loop direction is *against* the current, you are walking upstream. $\Delta V = +IR$.

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Applying Junction Rule (KCL) ⭐

**Pattern:** "Given a junction with multiple wires, find the missing current."

**Solved Example** 🟢

> Four wires meet at a junction. Currents of $5\text{A}$ and $3\text{A}$ are entering the junction. A current of $2\text{A}$ is leaving. Find the magnitude and direction of the current in the fourth wire.

<details>
<summary><b>Solution</b></summary>

Let the unknown current be $I$. Let's assume it is leaving.
Sum of entering = Sum of leaving
$5 + 3 = 2 + I$
$8 = 2 + I \implies I = \mathbf{6\text{ A}}$.
Since $I$ is positive, our assumption was correct: $6\text{A}$ is **leaving** the junction.
</details>

**Practice:**

1. 🟢 A node has three wires. $I_1 = 10\text{A}$ (entering), $I_2 = -4\text{A}$ (entering). Find $I_3$ (leaving).

<details>
<summary><b>Answer</b></summary>

Note: $-4\text{A}$ entering is the same as $4\text{A}$ leaving.
Using the formula directly: $\sum I_{in} = \sum I_{out}$.
$10 + (-4) = I_3 \implies I_3 = \mathbf{6\text{ A}}$.
</details>

2. 🟡 In a circuit, current splits at node A into two branches carrying $2\text{A}$ and $3\text{A}$. These branches recombine at node B. What is the current leaving node B?<br>

<details>
<summary><b>Answer</b></summary>

At node B, the two branches are entering.
Sum entering B = $2 + 3 = 5\text{A}$.
Therefore, current leaving B = $\mathbf{5\text{ A}}$.
</details>

---

### Type 2: Single Loop KVL ⭐⭐

**Pattern:** "A single loop with multiple batteries and resistors. Find the current."

**Solved Example** 🟡

> A loop contains a $10\text{V}$ battery (facing right), a $2\text{ } \Omega$ resistor, a $4\text{V}$ battery (facing left), and a $4\text{ } \Omega$ resistor, all in series. Find the current.

<details>
<summary><b>Solution</b></summary>

1. Assume current $I$ flows clockwise.
2. Let's walk clockwise starting from the bottom left corner.
3. Pass through $10\text{V}$ battery ($- \rightarrow +$): $+10$
4. Pass through $2\text{ } \Omega$ resistor (with current): $-2I$
5. Pass through $4\text{V}$ battery ($+ \rightarrow -$): $-4$
6. Pass through $4\text{ } \Omega$ resistor (with current): $-4I$
7. Set sum to zero:
   $+10 - 2I - 4 - 4I = 0$
   $6 - 6I = 0 \implies 6I = 6 \implies I = \mathbf{1\text{ A}}$.
</details>

**Practice:**

1. 🟢 A $12\text{V}$ battery (internal resistance $1\text{ } \Omega$) is connected to a $5\text{ } \Omega$ resistor. Use KVL to find the current.

<details>
<summary><b>Answer</b></summary>

Start at negative terminal, go clockwise with current $I$.
$+12 - I(1) - I(5) = 0$
$12 - 6I = 0 \implies I = \mathbf{2\text{ A}}$.
*(This is just $I = \varepsilon/(R+r)$ derived!)*
</details>

2. 🟡 Two batteries of $20\text{V}$ and $5\text{V}$ are connected in series opposing each other, with a $5\text{ } \Omega$ resistor. Find current.

<details>
<summary><b>Answer</b></summary>

Assume $I$ is driven by the $20\text{V}$ battery.
KVL: $+20 - 5I - 5 = 0$
$15 - 5I = 0 \implies I = \mathbf{3\text{ A}}$.
</details>

3. 🔴 Find the potential difference between two points A and B in a branch if you walk from A to B and pass through a $10\text{ } \Omega$ resistor carrying $2\text{A}$ (against your walking direction) and a $5\text{V}$ battery ($- \rightarrow +$).

<details>
<summary><b>Answer</b></summary>

$V_A + \sum \Delta V = V_B \implies V_A - V_B = -\sum \Delta V$.
Walking A to B:
Across resistor against current: $+ (2 \times 10) = +20\text{V}$.
Across battery ($- \rightarrow +$): $+5\text{V}$.
$V_A + 20 + 5 = V_B \implies V_B - V_A = \mathbf{25\text{ V}}$.
</details>

---

### Type 3: Two-Loop Networks ⭐⭐⭐

**Pattern:** "A figure-8 circuit with two loops. Solve for currents in branches."

> 🔑 **THE MASTER TRICK (Nodal Analysis Shortcut):**
> Setting up 3 simultaneous equations using KVL and KCL is tedious and prone to math errors.
> **Alternative (Nodal Analysis):**
> 1. Identify the common junction connecting the loops. Assume its potential is $x$ Volts.
> 2. Assume the other common junction is $0\text{V}$ (Ground).
> 3. Write KCL at the junction $x$: Assume all currents are LEAVING.
>    $\frac{x - V_1}{R_1} + \frac{x - V_2}{R_2} + \frac{x - V_3}{R_3} = 0$
> 4. Solve this single equation for $x$. Once you have $x$, you can find any current easily!

**Solved Example** 🔴

> Two loops share a middle branch. 
> Left branch: $10\text{V}$ battery, $2\text{ } \Omega$ resistor.
> Middle branch: $4\text{ } \Omega$ resistor.
> Right branch: $20\text{V}$ battery, $2\text{ } \Omega$ resistor.
> All batteries have negative terminals connected to the bottom wire. Find current in the middle branch.

<details>
<summary><b>Solution</b></summary>

**Using Nodal Analysis (The Fast Way):**
Let bottom wire be $0\text{V}$. Let top junction be $x$ Volts.
Sum of currents leaving junction $x$ is 0.
Current to left: $(x - 10) / 2$
Current down middle: $(x - 0) / 4$
Current to right: $(x - 20) / 2$

$\frac{x - 10}{2} + \frac{x}{4} + \frac{x - 20}{2} = 0$
Multiply entire equation by 4:
$2(x - 10) + x + 2(x - 20) = 0$
$2x - 20 + x + 2x - 40 = 0$
$5x - 60 = 0 \implies 5x = 60 \implies x = 12\text{V}$.

Current in middle branch = $x / 4 = 12 / 4 = \mathbf{3\text{ A}}$ (downwards).
*(Try solving this with KVL loops and 3 equations. This nodal method is infinitely faster!)*
</details>

**Practice:**

1. 🔴 Same circuit as above, but right battery is reversed (positive terminal connected to bottom wire). Find current in middle branch.

<details>
<summary><b>Answer</b></summary>

Bottom wire = $0\text{V}$. Top junction = $x$.
Right battery now provides $-20\text{V}$ relative to ground.
$\frac{x - 10}{2} + \frac{x}{4} + \frac{x - (-20)}{2} = 0$
Multiply by 4:
$2(x - 10) + x + 2(x + 20) = 0$
$2x - 20 + x + 2x + 40 = 0$
$5x + 20 = 0 \implies x = -4\text{V}$.
Middle current = $x / 4 = -4 / 4 = -1\text{A}$.
Magnitude is $\mathbf{1\text{ A}}$ (flowing upwards).
</details>

2. 🔴 In a 2-loop circuit, left branch has $5\text{V}$ and $1\text{ } \Omega$, right branch has $10\text{V}$ and $1\text{ } \Omega$. Middle branch is just a plain wire ($0\text{ } \Omega$). Find current in the middle wire.

<details>
<summary><b>Answer</b></summary>

If the middle branch has no resistance, it connects the top and bottom junctions directly.
This means the top and bottom junctions are at the SAME potential. $x = 0$.
The $5\text{V}$ battery is short-circuited through the middle wire. Left current = $5/1 = 5\text{A}$ (up).
The $10\text{V}$ battery is short-circuited through the middle wire. Right current = $10/1 = 10\text{A}$ (up).
By KCL at the top node: Current leaving down the middle wire = $5\text{A} + 10\text{A} = \mathbf{15\text{ A}}$.
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A network is shaped like a triangle ABC. AB has a $2\text{V}$ cell (positive at A) and $1\text{ } \Omega$ resistor. BC has a $1\text{V}$ cell (positive at B) and $1\text{ } \Omega$ resistor. CA has a $1\text{ } \Omega$ resistor. Find current in branch CA.

<details>
<summary><b>Solution</b></summary>

Let's use Nodal Analysis. Let Node C be $0\text{V}$.
Node B is connected to C via $1\text{V}$ battery (positive at B) and $1\text{ } \Omega$. Let voltage at A be $V_A$ and B be $V_B$.
Actually, since it's a single loop, KVL is faster!
Assume clockwise current $I$.
Start at C, go to A, B, back to C.
Path C $\rightarrow$ A: $-I(1)$
Path A $\rightarrow$ B: $-2 - I(1)$ (opposing battery)
Path B $\rightarrow$ C: $-1 - I(1)$ (opposing battery)
Sum = 0: $-I - 2 - I - 1 - I = 0 \implies -3I - 3 = 0 \implies I = -1\text{A}$.
Current is $1\text{A}$ counter-clockwise.
Branch CA current is $\mathbf{1\text{ A}}$ from A to C.
</details>

**Q2.** 🔴 ⭐ An infinite grid of $1\text{ } \Omega$ resistors forms a 2D mesh. What is the equivalent resistance between two adjacent nodes A and B?<br>
*(This is a classic famous physics puzzle!)*

<details>
<summary><b>Solution</b></summary>

Use superposition and KCL.
1. Inject $1\text{A}$ at node A. By symmetry, it splits equally 4 ways. Current from A to B is $1/4\text{ A}$.
2. Extract $1\text{A}$ at node B. By symmetry, it comes equally from 4 ways. Current from A to B is $1/4\text{ A}$.
3. Superimpose both cases (inject $1\text{A}$ at A, extract $1\text{A}$ at B). Total current flowing directly through the resistor connecting A and B is $1/4 + 1/4 = 1/2\text{ A}$.
Since the total current entering the system is $1\text{A}$, and the direct path takes $0.5\text{A}$, the voltage difference $V_{AB} = I_{branch} \times R = 0.5 \times 1 = 0.5\text{V}$.
Equivalent Resistance $R_{eq} = V_{AB} / I_{total} = 0.5 / 1 = \mathbf{0.5\text{ } \Omega}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 State Kirchhoff's two rules for electrical networks. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. **Junction Rule (KCL):** The algebraic sum of currents meeting at any junction in a circuit is zero ($\sum I = 0$). This implies total current entering equals total current leaving.
2. **Loop Rule (KVL):** The algebraic sum of changes in potential around any closed loop involving resistors and cells in the circuit is zero ($\sum \Delta V = 0$).
</details>

**Q2.** 🟡 On which conservation laws are Kirchhoff's junction rule and loop rule based?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

- Kirchhoff's Junction Rule is based on the **Law of Conservation of Charge** (charge cannot accumulate at a junction).
- Kirchhoff's Loop Rule is based on the **Law of Conservation of Energy** (the net work done in moving a charge around a closed loop is zero).
</details>

**Q3.** 🟡 Use Kirchhoff's rules to find the potential difference across the $5\text{ } \Omega$ resistor.
*(Imagine a standard 2-loop figure-8 circuit with specific values, requiring the setup of two loop equations).* *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

*(Generic steps to get full marks on a board exam, even if you know the nodal shortcut):*
1. Draw the circuit diagram and clearly label the direction of assumed currents ($I_1, I_2, I_3$) in different branches.
2. Apply KCL at a junction: e.g., $I_3 = I_1 + I_2$.
3. Apply KVL to Loop 1: Write the equation following the sign convention clearly.
4. Apply KVL to Loop 2: Write the second equation.
5. Solve the simultaneous equations to find the required current.
6. Calculate potential difference $V = IR$.
*(Examiners look for the KVL equations primarily).*
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ In a circuit, 5 branches meet at a node. The currents in 4 branches are $1\text{A}, 2\text{A}, 3\text{A}$, and $-4\text{A}$. What is the current in the 5th branch, assuming all are taken with the same sign convention (e.g., all entering)?<br>

(a) $2\text{A}$ &emsp; (b) $-2\text{A}$ &emsp; (c) $10\text{A}$ &emsp; (d) $-10\text{A}$

<details>
<summary><b>Answer</b></summary>

By KCL, $\sum I = 0$.
$1 + 2 + 3 + (-4) + I_5 = 0$
$6 - 4 + I_5 = 0 \implies 2 + I_5 = 0 \implies I_5 = \mathbf{-2\text{ A}}$.

**Answer: (b)**
</details>

**Q2.** 🔴 Consider a circuit with two batteries $\varepsilon_1 = 20\text{V}, r_1 = 1\text{ } \Omega$ and $\varepsilon_2 = 10\text{V}, r_2 = 2\text{ } \Omega$ connected in parallel across a resistor $R = 5\text{ } \Omega$. The current through $R$ is:

(a) $2\text{A}$ &emsp; (b) $2.5\text{A}$ &emsp; (c) $2.94\text{A}$ &emsp; (d) $3\text{A}$

<details>
<summary><b>Answer</b></summary>

We can use Nodal Analysis. Let the bottom junction be $0\text{V}$ and top be $x$.
KCL at top node (sum of currents leaving = 0):
$\frac{x - 20}{1} + \frac{x - 10}{2} + \frac{x - 0}{5} = 0$
Multiply by 10 to clear denominators:
$10(x - 20) + 5(x - 10) + 2x = 0$
$10x - 200 + 5x - 50 + 2x = 0$
$17x = 250 \implies x = 250/17 \approx 14.7\text{V}$.
Current through $R = x / 5 = (250/17) / 5 = 50 / 17 \approx \mathbf{2.94\text{ A}}$.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ In the given circuit, what is the potential difference between points A and B?<br>
*(Assume A is top node, B is bottom node. Left branch has $10\text{V}$ battery, middle has $2\text{ } \Omega$, right has $5\text{V}$ battery).*

(a) $10\text{V}$ &emsp; (b) $5\text{V}$ &emsp; (c) $0\text{V}$ &emsp; (d) Cannot be determined

<details>
<summary><b>Answer</b></summary>

If the batteries in the left and right branches have NO internal resistance (ideal batteries), then the potential difference between the top and bottom nodes is strictly locked by the batteries.
Wait—if you have a $10\text{V}$ ideal battery and a $5\text{V}$ ideal battery in parallel, this violates KVL! ($\sum V$ around the outer loop would be $10 - 5 = 5 \neq 0$).
Such a circuit is **theoretically impossible** (or would result in infinite current melting the wires).
In reality, batteries always have internal resistance. If $r$ is given, use nodal analysis. If it's literally ideal batteries in parallel, it's a paradox/trick question.

*Assuming the question meant they are in series in a single loop:*
Current $I = (10 - 5) / 2 = 2.5\text{A}$.
$V_{AB} = \mathbf{5\text{ V}}$ (across the $2\text{ } \Omega$ resistor).

**Answer: (Depends on exact diagram)**
</details>

---

*Next: [Chapter 12 — Wheatstone Bridge →](./12_wheatstone_bridge.md)*
