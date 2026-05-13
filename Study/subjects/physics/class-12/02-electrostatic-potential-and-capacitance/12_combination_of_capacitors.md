# Chapter 12: Combination of Capacitors

> *NCERT Section 2.13*

---

### The Story of the Circuit Designer's Dilemma

A circuit designer has a drawer full of identical $10 \mu F$ capacitors. Her client needs a $25 \mu F$ capacitor and a $4 \mu F$ capacitor. She doesn't have either. But she doesn't need them — because by combining her identical capacitors in the right configurations, she can build any capacitance she wants.

This is the practical power of series and parallel combinations. And it is the single most heavily tested topic in the entire capacitance chapter — both in Board exams and JEE Mains.

---

### Building the Concept: Parallel Combination

When capacitors are connected in **parallel**, they share the same voltage but accumulate different charges:

- Same $V$ across all capacitors
- Total charge: $Q = Q_1 + Q_2 + Q_3 + \ldots$
- Since $Q_i = C_i V$:

$$Q = C_1 V + C_2 V + \ldots = (C_1 + C_2 + \ldots) V$$

$$\boxed{C_{parallel} = C_1 + C_2 + C_3 + \ldots}$$

> **Mnemonic:** Parallel capacitors *add directly* (like resistors in series). The effective capacitance is always **larger** than any individual capacitance.

### Building the Concept: Series Combination

When capacitors are connected in **series**, the same charge flows through each, but the voltage divides:

- Same $Q$ on all capacitors
- Total voltage: $V = V_1 + V_2 + V_3 + \ldots$
- Since $V_i = Q/C_i$:

$$V = \frac{Q}{C_1} + \frac{Q}{C_2} + \ldots = Q\left(\frac{1}{C_1} + \frac{1}{C_2} + \ldots\right)$$

$$\boxed{\frac{1}{C_{series}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \ldots}$$

For two capacitors in series (a special, frequently used case):

$$C_{series} = \frac{C_1 C_2}{C_1 + C_2}$$

> **Mnemonic:** Series capacitors combine like *parallel resistors*. The effective capacitance is always **smaller** than the smallest individual capacitance.

#### The Inverse Relationship with Resistors

| | Capacitors | Resistors |
|--|:---------:|:---------:|
| **Parallel** | $C_{eq} = C_1 + C_2$ | $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$ |
| **Series** | $\frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2}$ | $R_{eq} = R_1 + R_2$ |

Capacitors are the *mirror image* of resistors. Whatever formula you use for resistors in series, use for capacitors in parallel, and vice versa.

---

### Checkpoint 1: Basic Combinations

**Problem 1:** Three capacitors of $2\mu F$, $3\mu F$, and $6\mu F$ are connected in parallel. Find the equivalent capacitance.

<details><summary><b>Solution</b></summary>

$C_{eq} = 2 + 3 + 6 = \textbf{11 μF}$
</details>

**Problem 2:** The same three capacitors are connected in series. Find $C_{eq}$.

<details><summary><b>Solution</b></summary>

$\frac{1}{C_{eq}} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6} = \frac{3 + 2 + 1}{6} = \frac{6}{6} = 1$

$C_{eq} = \textbf{1 μF}$
</details>

**Problem 3:** Two capacitors of $4\mu F$ and $12\mu F$ are in series. This combination is in parallel with a $6\mu F$ capacitor. Find the total $C_{eq}$.

<details><summary><b>Solution</b></summary>

Series part: $C_s = \frac{4 \times 12}{4 + 12} = \frac{48}{16} = 3\mu F$

Total (parallel with $6\mu F$): $C_{eq} = 3 + 6 = \textbf{9 μF}$
</details>

---

### Checkpoint 2: The Gauntlet — "The Charge Distribution Challenge"

*A student connects three capacitors ($C_1 = 2\mu F$, $C_2 = 3\mu F$, $C_3 = 6\mu F$) in series across a $120$ V battery.*

**Problem 1:** Find the equivalent capacitance.

<details><summary><b>Solution</b></summary>

$\frac{1}{C_{eq}} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6} = 1$

$C_{eq} = \textbf{1 μF}$
</details>

**Problem 2:** What charge is stored on each capacitor?

<details><summary><b>Solution</b></summary>

In series, all capacitors have the same charge:

$Q = C_{eq} V = 1 \times 10^{-6} \times 120 = \textbf{120 μC on each}$
</details>

**Problem 3:** What is the voltage across each capacitor?

<details><summary><b>Solution</b></summary>

$V_1 = Q/C_1 = 120/2 = \textbf{60 V}$

$V_2 = Q/C_2 = 120/3 = \textbf{40 V}$

$V_3 = Q/C_3 = 120/6 = \textbf{20 V}$

Check: $60 + 40 + 20 = 120$ V ✓

Notice: the smallest capacitor has the largest voltage drop. In series, voltage distributes inversely with capacitance.
</details>

*She now disconnects the battery and connects a $4\mu F$ capacitor in parallel with $C_1$.*

**Problem 4:** What is the new voltage across the parallel combination?

<details><summary><b>Solution</b></summary>

$C_1$ had charge $120\mu C$ and $V_1 = 60$ V.

Adding $4\mu F$ in parallel: the charge $120\mu C$ now redistributes across the parallel combination of $C_1 (2\mu F)$ and $C_4 (4\mu F)$ — **but only if** they form a closed loop where charge can flow.

The total charge on the parallel pair remains $120\mu C$ (charge is conserved in the series branch).

$V_{new} = \frac{Q}{C_1 + C_4} = \frac{120}{2 + 4} = \textbf{20 V}$

The voltage across $C_1$ drops from 60 V to 20 V. The $4\mu F$ capacitor acquires charge $4 \times 20 = 80\mu C$, and $C_1$ retains $2 \times 20 = 40\mu C$. Total = $120\mu C$ ✓.
</details>

---

### Checkpoint 3: Complex Networks

**Problem 1:** Find the equivalent capacitance between points A and B for the following network: three $6\mu F$ capacitors connected as follows — one from A to a middle point M, one from M to B, and one directly from A to B.

<details><summary><b>Solution</b></summary>

The two capacitors from A→M→B are in **series**: $C_s = \frac{6 \times 6}{6 + 6} = 3\mu F$

This is in **parallel** with the direct A→B capacitor: $C_{eq} = 3 + 6 = \textbf{9 μF}$
</details>

**Problem 2:** Four identical capacitors of $C$ each are connected to form a square (one along each side). Find $C_{eq}$ between two adjacent corners.

<details><summary><b>Solution</b></summary>

Between adjacent corners A and B:
- Path 1 (direct): One capacitor, capacitance $C$
- Path 2 (around the other three sides): Three capacitors in series, $C_s = C/3$

These two paths are in parallel:

$C_{eq} = C + C/3 = \textbf{4C/3}$
</details>

**Problem 3:** In the same square, find $C_{eq}$ between two **diagonally opposite** corners.

<details><summary><b>Solution</b></summary>

Between diagonal corners A and C:
- Path 1 (via B): Two capacitors in series → $C/2$
- Path 2 (via D): Two capacitors in series → $C/2$

These two paths are in parallel:

$C_{eq} = C/2 + C/2 = \textbf{C}$
</details>

---

### Checkpoint 4: Redistribution of Charge

**Problem 1:** A $5\mu F$ capacitor is charged to $100$ V and then disconnected from the battery. It is then connected (positive to positive) to an uncharged $20\mu F$ capacitor. Find:

(a) The common potential  
(b) The charge on each capacitor  
(c) The energy before and after connection. Comment on the "lost" energy.

<details><summary><b>Solution</b></summary>

Initial charge: $Q_0 = C_1 V_0 = 5 \times 100 = 500\mu C$

**(a)** Common potential (charge conserved):

$V = \frac{Q_{total}}{C_1 + C_2} = \frac{500}{5 + 20} = \textbf{20 V}$

**(b)** 
$Q_1 = C_1 V = 5 \times 20 = \textbf{100 μC}$

$Q_2 = C_2 V = 20 \times 20 = \textbf{400 μC}$

Check: $100 + 400 = 500\mu C$ ✓

**(c)** 
$U_{before} = \frac{1}{2} C_1 V_0^2 = \frac{1}{2} \times 5 \times 10^{-6} \times 10000 = \textbf{25 mJ}$

$U_{after} = \frac{1}{2}(C_1 + C_2)V^2 = \frac{1}{2} \times 25 \times 10^{-6} \times 400 = \textbf{5 mJ}$

Energy lost: $25 - 5 = \textbf{20 mJ}$. This energy was dissipated as **heat** in the connecting wires and as **electromagnetic radiation** during the transient current flow. Energy is always lost when charge redistributes between capacitors at different potentials.

General formula for energy loss: $\Delta U = \frac{1}{2} \frac{C_1 C_2}{C_1 + C_2}(V_1 - V_2)^2$

$\Delta U = \frac{1}{2} \times \frac{5 \times 20}{25} \times (100 - 0)^2 = \frac{1}{2} \times 4 \times 10000 = 20$ mJ ✓
</details>

---

### The Culmination: Synthesis

**Synthesis Problem:** Three capacitors $C_1 = 2\mu F$, $C_2 = 3\mu F$, $C_3 = 4\mu F$ are connected in series across a $180$ V battery.

(a) Find $C_{eq}$, total charge $Q$, and voltage across each.  
(b) The battery is disconnected. The three capacitors are then reconnected in parallel (positive plates together). Find the common voltage and the charge on each.  
(c) Calculate the total energy before (in series) and after (in parallel). Explain the difference.

<details><summary><b>Solution</b></summary>

**(a)**
$\frac{1}{C_{eq}} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{6 + 4 + 3}{12} = \frac{13}{12}$

$C_{eq} = \frac{12}{13} \mu F \approx 0.923\mu F$

$Q = C_{eq} V = \frac{12}{13} \times 180 = \frac{2160}{13} \approx 166.15\mu C$

Voltages:
$V_1 = Q/C_1 = 166.15/2 \approx \textbf{83.08 V}$

$V_2 = Q/C_2 = 166.15/3 \approx \textbf{55.38 V}$

$V_3 = Q/C_3 = 166.15/4 \approx \textbf{41.54 V}$

Check: $83.08 + 55.38 + 41.54 = 180$ V ✓

**(b)** When reconnected in parallel (all positive plates together), total charge is conserved:

$Q_{total} = Q_1 + Q_2 + Q_3 = 166.15 \times 3 = ?$

Wait — in series, **each** capacitor has charge $Q = 166.15\mu C$. So total charge on the positive plates = $166.15 + 166.15 + 166.15$? No!

In series, the charge is the **same** on each capacitor, not additive. When reconnected in parallel, we must think about what happens to the stored charge.

Actually, in the series configuration, each capacitor has $Q = 166.15\mu C$ on its positive plate and $-166.15\mu C$ on its negative plate. When we disconnect and reconnect in parallel (positive to positive, negative to negative), the total charge on the positive side is $3 \times 166.15 = 498.46\mu C$... **No!**

Let me reconsider. In a series chain, the outer plates of $C_1$ and $C_3$ have charge $+Q$ and $-Q$ respectively. The inner plates have charges that sum to zero in between. So the net charge available when reconnected is just $Q = 166.15\mu C$ on the positive end and $-Q$ on the negative end.

Actually, when disconnected from the battery: $C_1$ has $+Q$ on one plate and $-Q$ on the other; similarly for $C_2$ and $C_3$.

When connected in parallel (positive plates together):
$Q_{total} = Q + Q + Q = 3Q = 3 \times 166.15 = 498.46\mu C$

Hmm, this is the correct interpretation: each capacitor individually holds $Q$. When all positive plates are tied together and all negative plates are tied together, the total charge is $3Q$.

$V_{common} = \frac{Q_{total}}{C_1 + C_2 + C_3} = \frac{498.46}{2 + 3 + 4} = \frac{498.46}{9} \approx \textbf{55.38 V}$

Individual charges:
$Q_1' = C_1 V = 2 \times 55.38 = \textbf{110.77 μC}$

$Q_2' = C_2 V = 3 \times 55.38 = \textbf{166.15 μC}$

$Q_3' = C_3 V = 4 \times 55.38 = \textbf{221.54 μC}$

Check: $110.77 + 166.15 + 221.54 = 498.46\mu C$ ✓

**(c)**
$U_{series} = \frac{1}{2}C_{eq}V^2 = \frac{1}{2} \times \frac{12}{13} \times 10^{-6} \times (180)^2 = \frac{1}{2} \times 0.923 \times 10^{-6} \times 32400$

$U_{series} = \textbf{14.95 mJ}$

$U_{parallel} = \frac{1}{2}(C_1 + C_2 + C_3)V_{common}^2 = \frac{1}{2} \times 9 \times 10^{-6} \times (55.38)^2$

$U_{parallel} = \frac{1}{2} \times 9 \times 10^{-6} \times 3067 = \textbf{13.80 mJ}$

Energy lost: $14.95 - 13.80 = \textbf{1.15 mJ}$

This energy is dissipated as heat in the wires during the transient redistribution of charges.
</details>

---

## Question Bank — Chapter 12

### Section A: MCQs (15 Questions)

**Q1.** When capacitors are connected in parallel, which quantity is the same for all?

(a) Charge &emsp; (b) Voltage &emsp; (c) Energy &emsp; (d) Capacitance

<details><summary><b>Answer</b></summary>**(b)** Parallel: same voltage across all capacitors.</details>

---

**Q2.** When capacitors are connected in series, which quantity is the same for all?

(a) Voltage &emsp; (b) Capacitance &emsp; (c) Charge &emsp; (d) Energy

<details><summary><b>Answer</b></summary>**(c)** Series: same charge on all capacitors.</details>

---

**Q3.** The equivalent capacitance of $2\,\mu F$ and $3\,\mu F$ in series is:

(a) $5\,\mu F$ &emsp; (b) $1\,\mu F$ &emsp; (c) $1.2\,\mu F$ &emsp; (d) $6\,\mu F$

<details><summary><b>Answer</b></summary>**(c)** $C = 2\times3/(2+3) = 6/5 = 1.2\,\mu F$.</details>

---

**Q4.** The equivalent capacitance of $2\,\mu F$ and $3\,\mu F$ in parallel is:

(a) $1.2\,\mu F$ &emsp; (b) $5\,\mu F$ &emsp; (c) $6\,\mu F$ &emsp; (d) $0.83\,\mu F$

<details><summary><b>Answer</b></summary>**(b)** $C = 2+3 = 5\,\mu F$.</details>

---

**Q5.** In a series combination of capacitors, the voltage is maximum across:

(a) The largest capacitor &emsp; (b) The smallest capacitor &emsp; (c) All capacitors equally &emsp; (d) The middle capacitor

<details><summary><b>Answer</b></summary>**(b)** $V = Q/C$. Same $Q$; smallest $C$ gives largest $V$.</details>

---

**Q6.** The effective capacitance of $n$ identical capacitors each of $C$ in series is:

(a) $nC$ &emsp; (b) $C/n$ &emsp; (c) $C$ &emsp; (d) $n^2C$

<details><summary><b>Answer</b></summary>**(b)** $1/C_{eq} = n/C \Rightarrow C_{eq} = C/n$.</details>

---

**Q7.** The effective capacitance of $n$ identical capacitors each of $C$ in parallel is:

(a) $nC$ &emsp; (b) $C/n$ &emsp; (c) $C$ &emsp; (d) $n^2C$

<details><summary><b>Answer</b></summary>**(a)** $C_{eq} = nC$.</details>

---

**Q8.** A $4\,\mu F$ charged to $100$ V and $6\,\mu F$ charged to $50$ V are connected (positive to positive). The common potential is:

(a) $70$ V &emsp; (b) $80$ V &emsp; (c) $150$ V &emsp; (d) $75$ V

<details><summary><b>Answer</b></summary>**(a)** $V = (Q_1+Q_2)/(C_1+C_2) = (400+300)/10 = 700/10 = 70$ V.</details>

---

**Q9.** In a series combination, the capacitor that stores the maximum energy is:

(a) The largest &emsp; (b) The smallest &emsp; (c) All store equal energy &emsp; (d) The middle one

<details><summary><b>Answer</b></summary>**(b)** $U = Q^2/(2C)$. Same $Q$; smallest $C$ gives largest $U$.</details>

---

**Q10.** In a parallel combination, the capacitor that stores maximum charge is:

(a) The smallest &emsp; (b) The largest &emsp; (c) All store equal charge &emsp; (d) The middle one

<details><summary><b>Answer</b></summary>**(b)** $Q = CV$. Same $V$; largest $C$ gives largest $Q$.</details>

---

**Q11.** Energy is lost when two charged capacitors are connected because:

(a) Capacitance changes &emsp; (b) Charge is lost &emsp; (c) Current flows and heats the wire &emsp; (d) Potential doubles

<details><summary><b>Answer</b></summary>**(c)** During charge redistribution, current flows through the connecting wires/internal resistance, dissipating energy as heat.</details>

---

**Q12.** Three capacitors $1\,\mu F$, $2\,\mu F$, $3\,\mu F$ in series. The total capacitance is:

(a) $6\,\mu F$ &emsp; (b) $0.545\,\mu F$ &emsp; (c) $1\,\mu F$ &emsp; (d) $1.5\,\mu F$

<details><summary><b>Answer</b></summary>**(b)** $1/C = 1+1/2+1/3 = 11/6 \Rightarrow C = 6/11 = 0.545\,\mu F$.</details>

---

**Q13.** After a charged capacitor is connected to an uncharged capacitor (positive to positive), the total energy:

(a) Increases &emsp; (b) Decreases &emsp; (c) Remains same &emsp; (d) Doubles

<details><summary><b>Answer</b></summary>**(b)** Energy is always lost during charge redistribution (dissipated as heat). Total energy decreases.</details>

---

**Q14.** In the formula for energy lost during redistribution: $\Delta U = \frac{1}{2}\frac{C_1C_2}{C_1+C_2}(V_1-V_2)^2$, the energy is zero when:

(a) $C_1 = C_2$ &emsp; (b) $V_1 = V_2$ &emsp; (c) $Q_1 = Q_2$ &emsp; (d) $C_1 >> C_2$

<details><summary><b>Answer</b></summary>**(b)** No energy is lost if the capacitors are already at the same potential ($V_1 = V_2$) — no charge flows.</details>

---

**Q15.** The ratio of charge on $C_1$ to charge on $C_2$ when connected in parallel to a battery is:

(a) $C_1/C_2$ &emsp; (b) $C_2/C_1$ &emsp; (c) $1:1$ &emsp; (d) $(C_1+C_2)/2$

<details><summary><b>Answer</b></summary>**(a)** Parallel: same $V$. $Q_1 = C_1V$, $Q_2 = C_2V$. $Q_1/Q_2 = C_1/C_2$.</details>

---

### Section B: Short Answer Questions

**Q16.** Three capacitors ($3\,\mu F$, $6\,\mu F$, $6\,\mu F$) are connected in series to $120$ V. Find $C_{eq}$, $Q$, and $V$ across each.

<details><summary><b>Answer</b></summary>

$1/C_{eq} = 1/3+1/6+1/6 = 2/6+1/6+1/6 = 4/6 \Rightarrow C_{eq} = 1.5\,\mu F$

$Q = C_{eq}V = 1.5\times10^{-6}\times120 = 180\,\mu C$

$V_1 = 180/3 = 60$ V, $V_2 = V_3 = 180/6 = 30$ V. Check: $60+30+30 = 120$ V ✓
</details>

---

**Q17.** Find $C_{eq}$ between terminals A and B: three $6\,\mu F$ capacitors, one from A to B, one from A to midpoint M, one from M to B.

<details><summary><b>Answer</b></summary>

A→M→B: two capacitors in series → $C_s = 6\times6/(6+6) = 3\,\mu F$

In parallel with A→B capacitor: $C_{eq} = 3+6 = \mathbf{9\,\mu F}$
</details>

---

**Q18.** A $10\,\mu F$ capacitor charged to $200$ V and $20\,\mu F$ at $100$ V are connected positive-to-positive. Find the common potential and energy lost.

<details><summary><b>Answer</b></summary>

$V = (C_1V_1+C_2V_2)/(C_1+C_2) = (10\times200+20\times100)/30 = 4000/30 = 133.3$ V

$\Delta U = \frac{1}{2}\frac{C_1C_2}{C_1+C_2}(V_1-V_2)^2 = \frac{1}{2}\times\frac{200}{30}\times(100)^2 = \frac{1}{2}\times\frac{200}{30}\times10^4 = \mathbf{33.3\,mJ}$
</details>

---

**Q19.** In a series combination of $4\,\mu F$ and $6\,\mu F$ connected to $100$ V, find the voltage and energy stored in each capacitor.

<details><summary><b>Answer</b></summary>

$C_{eq} = 24/10 = 2.4\,\mu F$; $Q = 2.4\times10^{-6}\times100 = 240\,\mu C$

$V_1 = 240/4 = 60$ V; $V_2 = 240/6 = 40$ V ✓ ($60+40 = 100$ V)

$U_1 = Q^2/(2C_1) = (240)^2/(2\times4) = 7200\,\mu J = 7.2$ mJ

$U_2 = Q^2/(2C_2) = (240)^2/(2\times6) = 4800\,\mu J = 4.8$ mJ
</details>

---

**Q20.** Can a $5\,\mu F$ capacitor be made using only $10\,\mu F$ capacitors? Show the arrangement.

<details><summary><b>Answer</b></summary>

Yes. Connect two $10\,\mu F$ capacitors in series:

$C_{eq} = 10\times10/(10+10) = \mathbf{5\,\mu F}$

Alternatively, take three in parallel (30 μF) and combine with one in series: $30\times10/(30+10) = 7.5$ μF... more complex.

The simplest: **two in series = 5 μF**.
</details>

---

**Q21.** A $5\,\mu F$ capacitor is charged to $100$ V and disconnected. It is then connected to an uncharged $15\,\mu F$. Find: (a) common potential, (b) charge on each, (c) energy lost.

<details><summary><b>Answer</b></summary>

**(a)** $V = Q_{total}/(C_1+C_2) = 500/(5+15) = \mathbf{25\,V}$

**(b)** $Q_1 = 5\times25 = 125\,\mu C$; $Q_2 = 15\times25 = 375\,\mu C$

**(c)** $U_i = \frac{1}{2}\times5\times10^{-6}\times10^4 = 25\,mJ$

$U_f = \frac{1}{2}\times20\times10^{-6}\times625 = 6.25\,mJ$

$\Delta U = 25-6.25 = \mathbf{18.75\,mJ}$
</details>

---

**Q22.** Four identical capacitors of $C = 3\,\mu F$ are arranged in a square. Find $C_{eq}$ between (a) adjacent corners, (b) diagonal corners.

<details><summary><b>Answer</b></summary>

**(a) Adjacent:** Direct path = $C = 3\,\mu F$; Other 3 in series = $C/3 = 1\,\mu F$. Parallel: $C_{eq} = 3+1 = \mathbf{4\,\mu F}$

**(b) Diagonal:** Two paths, each with 2 in series = $C/2 = 1.5\,\mu F$. Parallel: $C_{eq} = 1.5+1.5 = \mathbf{3\,\mu F}$
</details>

---

### Section C: Long Answer / JEE-Level

**Q23–Q30:** Combination and redistribution problems.

**Q23.** Two capacitors $C_1 = 8\,\mu F$ (charged to $120$ V) and $C_2 = 4\,\mu F$ (charged to $60$ V) are connected with plates of opposite polarity joined. Find the common potential and energy lost.

<details><summary><b>Answer</b></summary>

When opposite polarities are joined, charges partially cancel:

$Q_{net} = C_1V_1 - C_2V_2 = 8\times120 - 4\times60 = 960 - 240 = 720\,\mu C$

$V = Q_{net}/(C_1+C_2) = 720/12 = \mathbf{60\,V}$

$U_i = \frac{1}{2}\times8\times10^{-6}\times14400 + \frac{1}{2}\times4\times10^{-6}\times3600 = 57.6\,mJ + 7.2\,mJ = 64.8\,mJ$

$U_f = \frac{1}{2}\times12\times10^{-6}\times3600 = 21.6\,mJ$

Energy lost $= 64.8 - 21.6 = \mathbf{43.2\,mJ}$
</details>

---

**Q24.** Find $C_{eq}$ for a ladder network of alternating series and parallel $C$'s (3 stages) where each series = $C$ and each shunt = $C$.

<details><summary><b>Answer</b></summary>

Working from the right:

Stage 3 (rightmost): $C_p = C$ (last parallel capacitor)

Stage 3 series: $C_s = C\times C/(C+C) = C/2$ (series with $C_p$)

After stage 3: effective $= C + C/2 = 3C/2$

Stage 2: $C_{s2} = C\times(3C/2)/(C+3C/2) = 3C^2/2 \div 5C/2 = 3C/5$

After stage 2: $C + 3C/5 = 8C/5$

Stage 1: $C_{eq} = C\times(8C/5)/(C+8C/5) = 8C^2/5 \div 13C/5 = 8C/13$

$C_{eq} = \mathbf{8C/13}$
</details>

---

**Q25.** Design a capacitor network using $2\,\mu F$, $3\,\mu F$, $6\,\mu F$, and $12\,\mu F$ that gives $4\,\mu F$ effective capacitance.

<details><summary><b>Answer</b></summary>

Try: $6\,\mu F$ and $12\,\mu F$ in series: $6\times12/18 = 4\,\mu F$ ✓

Or: $2\,\mu F$ and $3\,\mu F$ and $6\,\mu F$ in series: $1/(1/2+1/3+1/6) = 1/(3/6+2/6+1/6) = 1/(1) = 1\,\mu F$ (not 4).

Simplest: **$6\,\mu F$ and $12\,\mu F$ in series** gives exactly $4\,\mu F$.
</details>

---

**Q26.** Three capacitors are in series ($C_1 = 2\,\mu F$, $C_2 = 4\,\mu F$, $C_3 = 6\,\mu F$) with $120$ V battery. Find the voltage ratio $V_1:V_2:V_3$.

<details><summary><b>Answer</b></summary>

Same charge on all. $V = Q/C$, so $V \propto 1/C$.

$V_1:V_2:V_3 = 1/C_1:1/C_2:1/C_3 = 1/2:1/4:1/6 = 6:3:2$

Actual: $C_{eq} = 12/11\,\mu F$; $Q = 12/11\times120 = 1440/11\,\mu C$

$V_1 = 720/11 = 65.5$ V, $V_2 = 360/11 = 32.7$ V, $V_3 = 240/11 = 21.8$ V

Ratio $= 720:360:240 = 6:3:2$ ✓
</details>

---

**Q27.** Show that energy is always lost when two capacitors at different potentials are connected.

<details><summary><b>Answer</b></summary>

Before: $U_i = \frac{1}{2}C_1V_1^2 + \frac{1}{2}C_2V_2^2$

After: $V_f = (C_1V_1+C_2V_2)/(C_1+C_2)$

$U_f = \frac{1}{2}(C_1+C_2)V_f^2$

Energy lost: $\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1C_2(V_1-V_2)^2}{C_1+C_2}$

Since $C_1, C_2 > 0$ and $(V_1-V_2)^2 \geq 0$: $\Delta U \geq 0$ always.

$\Delta U = 0$ only when $V_1 = V_2$ (no charge redistribution). When $V_1 \neq V_2$, energy is necessarily lost.
</details>

---

**Q28.** $n$ identical capacitors are first connected in series, then all charged to $V$. Then reconnected in parallel. Find the final voltage and the common voltage.

<details><summary><b>Answer</b></summary>

In series: $C_{series} = C/n$. Charge: $Q = C_{series}\times V = CV/n$. Each capacitor has charge $Q = CV/n$.

In parallel: Total charge = $n\times Q = n\times CV/n = CV$. $C_{parallel} = nC$.

$V_{final} = CV/(nC) = \mathbf{V/n}$

The voltage decreases by factor $n$.
</details>

---

**Q29.** A $2\,\mu F$ and $3\,\mu F$ in series are connected to $100$ V. A dielectric ($K = 2$) is then inserted in the $2\,\mu F$ (battery stays connected). Find the new charge distribution.

<details><summary><b>Answer</b></summary>

New $C_1' = K\times C_1 = 2\times2 = 4\,\mu F$; $C_2 = 3\,\mu F$ (unchanged)

New series: $C_{eq}' = 4\times3/(4+3) = 12/7\,\mu F$

$Q' = C_{eq}'\times V = 12/7\times10^{-6}\times100 = \mathbf{171.4\,\mu C}$

Both $C_1'$ and $C_2$ have this charge: $Q_1' = Q_2' = 171.4\,\mu C$

(Previously: $C_{eq} = 6/5 = 1.2\,\mu F$, $Q = 120\,\mu C$)
</details>

---

**Q30.** Two capacitors form a circuit: $C_1 = 5\,\mu F$ and $C_2 = 20\,\mu F$ in parallel across a $100$ V battery. After disconnection, they are reconnected in series (+ to -). Find the new voltage distribution.

<details><summary><b>Answer</b></summary>

After parallel charging: $Q_1 = 5\times100 = 500\,\mu C$, $Q_2 = 20\times100 = 2000\,\mu C$

When reconnected in series (+ to -), the inner plates (originally + on $C_1$ and - on $C_2$) are connected. Their charges cancel partially:

Net charge available: For ideal wires, the inner connected plates redistribute charge. Let final charge = $q$.

$q = (Q_1-0)$ for $C_1$ and... This is a complex redistribution. The final result requires:

Outer plates: $C_1$ outer $(+500)$, $C_2$ outer $(+2000)$ → these are the "terminals".

Inner plates cancel: the inner junction can hold net charge $(500-2000) = -1500\,\mu C$ redistributing to zero by charge flowing.

Final charge: $q = (Q_1 + Q_2)/(C_1 + C_2)\times...$: actually for series reconnection with opposite polarity, $q = (C_2V_2-C_1V_1)/(C_1+C_2) = (2000-500)/25 = 60\,\mu C$... (detailed analysis gives $V_1 = q/C_1 = 60/5 = 12$ V, $V_2 = q/C_2 = 60/20 = 3$ V)
</details>

---

*Next: [Chapter 13 — Energy Stored in a Capacitor →](./13_energy_stored_capacitor.md)*
