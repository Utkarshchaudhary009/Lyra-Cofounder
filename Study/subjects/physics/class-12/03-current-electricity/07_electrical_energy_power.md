# Chapter 7: Electrical Energy & Power

> *NCERT Section 3.9*

---

## 🎯 Stage 1: The Core Idea

### Where Does the Energy Go?<br>

When a battery pushes electrons through a wire, it does **work**. The electric field accelerates the electrons, increasing their kinetic energy.

But wait—drift velocity is constant! If the electrons are constantly being accelerated by the field, why don't they keep getting faster and faster?<br> 

**The Collisions.** 
Electrons constantly smash into the heavy, vibrating positive ions of the metal lattice. In every collision, the electron loses its gained kinetic energy, transferring it to the ion. The ion vibrates harder, which means the metal **heats up**.

This is **Joule Heating**. The electrical energy provided by the battery is continuously converted into thermal energy (heat) in the resistor.

### Power: The Rate of Energy Drain

**Energy** is the total amount of "work" done. (e.g., How much battery you drained playing a game for 2 hours).
**Power** is how fast that energy is being drained *right now*. (e.g., A high-end 3D game drains 5% per minute, while reading an ebook drains 1% per minute).

- **Bulb Brightness:** A $100\text{ W}$ bulb is brighter than a $60\text{ W}$ bulb because it converts $100\text{ Joules}$ of electrical energy into heat/light *every single second*.

---

## 🔬 Stage 2: The Formula Lab

### 1. Electrical Power ($P$)

Power is the rate at which electrical potential energy is dissipated.

$$P = VI$$

Using Ohm's Law ($V=IR$), we get three forms of the power equation. **Knowing when to use which is the secret to solving all power problems:**

| Formula | When to use it?<br> |
|---------|----------------|
| **$P = VI$** | When Voltage and Current are known. |
| **$P = I^2R$** | **SERIES CIRCUITS:** Current ($I$) is constant. Use this to compare power of resistors in series. ($P \propto R$) |
| **$P = \frac{V^2}{R}$** | **PARALLEL CIRCUITS:** Voltage ($V$) is constant. Use this to compare power of resistors in parallel. ($P \propto \frac{1}{R}$) |

**Unit:** Watt ($\text{W}$) or Joule/second ($\text{J/s}$).

### 2. Electrical Energy ($E$ or $H$)

Energy (or Heat produced) is Power multiplied by Time.

$$H = P \times t = VIt = I^2Rt = \frac{V^2}{R}t$$

**Unit:** Joule ($\text{J}$).
**Commercial Unit:** Kilowatt-hour ($\text{kWh}$), also called "1 Unit" on your electricity bill.
$$1 \text{ kWh} = 1000 \text{ W} \times 3600 \text{ s} = 3.6 \times 10^6 \text{ J}$$

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Basic Power and Heat Calculations ⭐

**Pattern:** "Given $V, I, R, t$, find Power or Heat."

**Solved Example** 🟢

> An electric heater of resistance $20 \text{ } \Omega$ draws a current of $5\text{ A}$ from the mains. Calculate the rate at which heat is developed, and the total heat produced in 30 seconds.

<details>
<summary><b>Solution</b></summary>

"Rate at which heat is developed" = Power ($P$).
Since we know $I$ and $R$, use $P = I^2R$.
$P = (5)^2 \times 20 = 25 \times 20 = \mathbf{500\text{ W} \text{ (or J/s)}}$.

Total heat in $t = 30\text{ s}$:
$H = P \times t = 500 \times 30 = \mathbf{15,000\text{ J}}$ (or $15\text{ kJ}$).
</details>

**Practice:**

1. 🟢 A $12\text{ V}$ car battery is connected to a headlight of resistance $4\text{ } \Omega$. What is the power of the headlight?<br>

<details>
<summary><b>Answer</b></summary>

$P = V^2 / R = 144 / 4 = \mathbf{36\text{ W}}$.
</details>

2. 🟢 A current of $2\text{ A}$ flows through a $5\text{ } \Omega$ resistor for $10\text{ minutes}$. Calculate the heat generated.

<details>
<summary><b>Answer</b></summary>

$t = 10\text{ min} = 600\text{ s}$.
$H = I^2Rt = (2)^2 \times 5 \times 600 = 4 \times 5 \times 600 = \mathbf{12,000\text{ J}}$ (or $12\text{ kJ}$).
</details>

3. 🟡 An appliance is rated "$2000\text{ W}, 250\text{ V}$". Find its resistance and the safe current limit.

<details>
<summary><b>Answer</b></summary>

$P = V^2 / R \implies R = V^2 / P = (250 \times 250) / 2000 = 62500 / 2000 = \mathbf{31.25\text{ } \Omega}$.
$P = VI \implies I = P / V = 2000 / 250 = \mathbf{8\text{ A}}$.
</details>

4. 🟡 How many Joules are in $2.5\text{ kWh}$ of energy?<br>

<details>
<summary><b>Answer</b></summary>

$2.5 \times (3.6 \times 10^6) = \mathbf{9 \times 10^6\text{ J}}$.
</details>

---

### Type 2: Series vs Parallel Brightness Comparison ⭐⭐⭐

**Pattern:** "Two bulbs are rated $P_1$ and $P_2$. Which glows brighter in series?<br> Which glows brighter in parallel?<br>"

> 🔑 **THE MASTER TRICK:**
> 1. Find Resistance first! $R = V_{rated}^2 / P_{rated}$. (Lower rated power = Higher resistance).
> 2. **In Series:** Current $I$ is same. Use $P_{actual} = I^2R$. Higher $R$ dissipates more power. So, **Lower rated bulb glows brighter.**
> 3. **In Parallel:** Voltage $V$ is same. Use $P_{actual} = V^2/R$. Lower $R$ dissipates more power. So, **Higher rated bulb glows brighter.**

**Solved Example** 🔴

> Two bulbs rated $60\text{W}, 220\text{V}$ and $100\text{W}, 220\text{V}$ are connected in series across a $220\text{V}$ supply. Which will glow brighter?<br> What if they are connected in parallel?<br>

<details>
<summary><b>Solution</b></summary>

**Step 1: Compare Resistances**
$R \propto 1/P_{rated}$.
The $60\text{W}$ bulb has a **higher resistance** than the $100\text{W}$ bulb.

**Step 2: Series Connection**
Current is constant. Power dissipated $P = I^2R$.
Since $R_{60W} > R_{100W}$, the $60\text{W}$ bulb dissipates more power.
**Result:** $60\text{W}$ bulb glows brighter in series.

**Step 3: Parallel Connection**
Voltage is constant. Power dissipated $P = V^2/R$.
Since $R_{100W} < R_{60W}$, the $100\text{W}$ bulb dissipates more power.
**Result:** $100\text{W}$ bulb glows brighter in parallel (which is how house wiring works).
</details>

**Practice:**

1. 🟡 Three bulbs $40\text{W}, 60\text{W}, 100\text{W}$ (all rated $220\text{V}$) are connected in series. Rank them in order of brightness (dimmest to brightest).

<details>
<summary><b>Answer</b></summary>

In series, lower rated power = higher resistance = brighter.
Dimmest to brightest: **$100\text{W} < 60\text{W} < 40\text{W}$**.
</details>

2. 🟡 The same three bulbs are connected in parallel. Rank them in order of brightness.

<details>
<summary><b>Answer</b></summary>

In parallel, higher rated power = lower resistance = draws more current = brighter.
Dimmest to brightest: **$40\text{W} < 60\text{W} < 100\text{W}$**.
</details>

3. 🔴 A $25\text{W}, 220\text{V}$ bulb and a $100\text{W}, 220\text{V}$ bulb are connected in series across a $440\text{V}$ supply. What will happen?<br>

<details>
<summary><b>Answer</b></summary>

$R_{25} = 220^2 / 25 = 1936\text{ } \Omega$.
$R_{100} = 220^2 / 100 = 484\text{ } \Omega$.
Total resistance = $2420\text{ } \Omega$.
Current $I = V_{total} / R_{total} = 440 / 2420 = 2/11\text{ A}$.
Voltage across $25\text{W}$ bulb: $V_{25} = I \times R_{25} = (2/11) \times 1936 = 352\text{ V}$.
Voltage across $100\text{W}$ bulb: $V_{100} = I \times R_{100} = (2/11) \times 484 = 88\text{ V}$.
The $25\text{W}$ bulb is subjected to $352\text{ V}$ (way above its $220\text{ V}$ rating). **The $25\text{W}$ bulb will fuse.**
</details>

---

### Type 3: Actual Power at Different Voltage ⭐⭐

**Pattern:** "A device is rated $P_1, V_1$. It is operated at a different voltage $V_2$. Find actual power."

**Solved Example** 🟡

> An electric bulb is rated $100\text{W}, 200\text{V}$. What is the power consumed if it is operated on a $100\text{V}$ supply?<br>

<details>
<summary><b>Solution</b></summary>

**Step 1: Find Resistance (it never changes unless temperature shifts drastically)**
$R = \frac{V_{rated}^2}{P_{rated}} = \frac{200^2}{100} = \frac{40000}{100} = 400\text{ } \Omega$.

**Step 2: Find actual power at new voltage**
$P_{actual} = \frac{V_{actual}^2}{R} = \frac{100^2}{400} = \frac{10000}{400} = \mathbf{25\text{W}}$.

*Shortcut:* $P \propto V^2$ (for constant R). Voltage halved $\rightarrow$ Power becomes $(1/2)^2 = 1/4$th.
</details>

**Practice:**

1. 🟡 A heater rated $220\text{V}, 1000\text{W}$ is operated at $110\text{V}$. Find power consumed.

<details>
<summary><b>Answer</b></summary>

Voltage is halved ($220 \rightarrow 110$). Power becomes $1/4$th.
$P_{actual} = 1000 / 4 = \mathbf{250\text{W}}$.
</details>

2. 🟡 Two identical heaters, each rated $1000\text{W}, 220\text{V}$ are connected in series across $220\text{V}$. Find total power consumed.

<details>
<summary><b>Answer</b></summary>

In series, the $220\text{V}$ splits equally. Each heater gets $110\text{V}$.
Power of each = $(110/220)^2 \times 1000 = 250\text{W}$.
Total power = $250 + 250 = \mathbf{500\text{W}}$.
</details>

---

### Type 4: Heating Water / Calorimetry Mixer ⭐

**Pattern:** "Electrical heat $I^2Rt$ is used to heat water ($ms\Delta T$) or melt ice ($mL$)."

**Solved Example** 🔴

> An electric kettle has a resistance of $50\text{ } \Omega$. How long will it take to heat $1\text{ kg}$ of water from $20^\circ\text{C}$ to $100^\circ\text{C}$ if connected to a $200\text{V}$ supply?<br> (Specific heat of water = $4200\text{ J/kg}^\circ\text{C}$)

<details>
<summary><b>Solution</b></summary>

Heat required by water: $Q = ms\Delta T$
$Q = 1 \times 4200 \times (100 - 20) = 4200 \times 80 = 336,000\text{ J}$.

Electrical power of kettle: $P = V^2/R = (200)^2 / 50 = 40000 / 50 = 800\text{ W}$.

Heat supplied: $H = P \times t$
Equating the two: $800 \times t = 336,000$
$t = 336,000 / 800 = \mathbf{420\text{ seconds}}$ (or 7 minutes).
</details>

**Practice:**

1. 🔴 A $1\text{ kW}$ heater operates on $220\text{V}$. How much time will it take to melt $2\text{ kg}$ of ice at $0^\circ\text{C}$ into water at $0^\circ\text{C}$?<br> (Latent heat of fusion of ice = $3.36 \times 10^5\text{ J/kg}$).

<details>
<summary><b>Answer</b></summary>

Heat required to melt ice $Q = mL = 2 \times 3.36 \times 10^5 = 6.72 \times 10^5\text{ J}$.
Power $P = 1000\text{ W}$ (Voltage info isn't needed if we know actual power delivered).
$Pt = Q \implies 1000 \times t = 672000 \implies t = \mathbf{672\text{ s}}$ (11.2 min).
</details>

2. 🔴 ⭐ Two heater coils A and B boil a given volume of water in $t_1 = 10\text{ min}$ and $t_2 = 15\text{ min}$ respectively when connected separately across the same mains. Find the time taken if they are connected in (i) series, (ii) parallel.

<details>
<summary><b>Answer</b></summary>

Let required heat = $H$, mains voltage = $V$.
Resistance of coils: $R_1 = V^2 / P_1 = V^2 / (H/t_1)$ and $R_2 = V^2 / (H/t_2)$.

**(i) Series:** $R_{eq} = R_1 + R_2$.
Time $t_s = H / P_{series} = H / (V^2 / R_{eq}) = H \cdot R_{eq} / V^2$.
$t_s = \frac{H}{V^2} (R_1 + R_2) = \frac{H}{V^2} \left( \frac{V^2 t_1}{H} + \frac{V^2 t_2}{H} \right) = t_1 + t_2$.
$t_s = 10 + 15 = \mathbf{25\text{ min}}$.

**(ii) Parallel:** $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$.
Power in parallel $P_{par} = P_1 + P_2 \implies \frac{H}{t_p} = \frac{H}{t_1} + \frac{H}{t_2}$.
$\frac{1}{t_p} = \frac{1}{t_1} + \frac{1}{t_2} \implies t_p = \frac{t_1 t_2}{t_1 + t_2}$.
$t_p = (10 \times 15) / (10 + 15) = 150 / 25 = \mathbf{6\text{ min}}$.
*(Shortcut: Series time adds, Parallel time is "parallel resistor" formula!)*
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 A fuse wire limits current to $5\text{A}$. If a $1000\text{W}, 220\text{V}$ heater is connected in the circuit, can a $200\text{W}, 220\text{V}$ TV be operated simultaneously without blowing the fuse?<br>

<details>
<summary><b>Solution</b></summary>

Current drawn by heater $I_1 = P/V = 1000 / 220 \approx 4.54\text{ A}$.
Current drawn by TV $I_2 = P/V = 200 / 220 \approx 0.91\text{ A}$.
Total current in parallel (household wiring) = $4.54 + 0.91 = 5.45\text{ A}$.
Since $5.45\text{ A} > 5\text{ A}$ (fuse rating), the **fuse will blow**. They cannot be operated simultaneously.
</details>

**Q2.** 🔴 A battery of EMF $\varepsilon$ and internal resistance $r$ is connected across a variable external resistance $R$. Prove that the power dissipated in the external circuit is maximum when $R = r$. (This is the Maximum Power Transfer Theorem).

<details>
<summary><b>Solution</b></summary>

Current $I = \frac{\varepsilon}{R + r}$.
Power dissipated in $R$ is $P = I^2R = \frac{\varepsilon^2 R}{(R + r)^2}$.
To maximize $P$, set $dP/dR = 0$.
$\frac{d}{dR} \left[ \varepsilon^2 R (R + r)^{-2} \right] = 0$
$\varepsilon^2 \left[ 1 \cdot (R + r)^{-2} + R(-2)(R + r)^{-3} \right] = 0$
$\frac{1}{(R+r)^2} - \frac{2R}{(R+r)^3} = 0$
$R + r - 2R = 0 \implies r - R = 0 \implies \mathbf{R = r}$.
Maximum power $P_{max} = \frac{\varepsilon^2 r}{(2r)^2} = \mathbf{\frac{\varepsilon^2}{4r}}$.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 Why do the connecting wires in a circuit not get as hot as the heating element (like a toaster wire), even though the same current flows through both?<br> *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

In a series circuit, the current $I$ is the same everywhere. The heat produced is $H = I^2Rt$. Since heat produced is directly proportional to resistance ($H \propto R$), and the connecting wires (usually copper) have a very low resistance compared to the heating element (like nichrome), the heating element gets very hot while the connecting wires do not.
</details>

**Q2.** 🟡 Define electrical power. Show that power dissipated in a resistor is $V^2/R$. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Electrical Power:** It is the rate at which electrical energy is dissipated or consumed in an electrical circuit. 
Work done by the source in moving charge $dq$ in time $dt$ is $dW = V dq$.
Power $P = \frac{dW}{dt} = V \frac{dq}{dt} = VI$.
From Ohm's law, $I = V/R$.
Substituting $I$: $P = V \left(\frac{V}{R}\right) = \mathbf{\frac{V^2}{R}}$.
</details>

**Q3.** 🟡 A bulb is rated $40\text{W}, 220\text{V}$. Find the current drawn by it when connected to a $220\text{V}$ supply. Also find its resistance. If it is connected to a $110\text{V}$ supply, what will be its power consumption?<br> *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

Current $I = P/V = 40 / 220 = \mathbf{0.18\text{ A}}$.
Resistance $R = V^2 / P = (220)^2 / 40 = 48400 / 40 = \mathbf{1210\text{ } \Omega}$.
When connected to $110\text{V}$:
$P' = V'^2 / R = (110)^2 / 1210 = 12100 / 1210 = \mathbf{10\text{ W}}$.
*(Or simply: Voltage halved $\rightarrow$ Power becomes $1/4^{th}$ of $40\text{W} = 10\text{W}$).*
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ Three identical resistors $R_1, R_2$, and $R_3$ are connected as shown: $R_2$ and $R_3$ are in parallel, and this combination is in series with $R_1$. They are connected to a battery. The ratio of power dissipated in $R_1$ to that in $R_2$ is:

(a) 1:1 &emsp; (b) 2:1 &emsp; (c) 4:1 &emsp; (d) 1:4

<details>
<summary><b>Answer</b></summary>

Let total current be $I$. This current flows entirely through $R_1$.
So, power in $R_1$ is $P_1 = I^2 R$.
At the parallel junction, the current splits equally because $R_2 = R_3 = R$.
Current through $R_2$ is $I/2$.
Power in $R_2$ is $P_2 = (I/2)^2 R = I^2 R / 4$.
Ratio $P_1 : P_2 = I^2 R : (I^2 R / 4) = 1 : (1/4) = \mathbf{4:1}$.

**Answer: (c)**
</details>

**Q2.** 🔴 A resistor $R$ has power of dissipation $P$ with cell voltage $E$. The resistor is cut into $n$ equal parts and all parts are connected in parallel with the same cell. The new power dissipation is:

(a) $nP$ &emsp; (b) $P/n$ &emsp; (c) $n^2P$ &emsp; (d) $P/n^2$

<details>
<summary><b>Answer</b></summary>

Initial power $P = E^2 / R$.
When cut into $n$ parts, each part has resistance $R/n$.
When connected in parallel, $R_{eq} = (R/n) / n = R/n^2$.
New power $P' = E^2 / R_{eq} = E^2 / (R/n^2) = n^2 (E^2/R) = \mathbf{n^2 P}$.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ An electric cable of copper has just one wire of radius $9\text{ mm}$. Its resistance is $5\text{ } \Omega$. This single copper wire of cable is replaced by 6 different well-insulated copper wires each of radius $3\text{ mm}$. The total resistance of the cable will now be equal to:

(a) $7.5\text{ } \Omega$ &emsp; (b) $45\text{ } \Omega$ &emsp; (c) $90\text{ } \Omega$ &emsp; (d) $270\text{ } \Omega$

<details>
<summary><b>Answer</b></summary>

Initial wire: radius $R = 9\text{ mm}$. $A_1 = \pi (9)^2 = 81\pi$.
$Resistance = \rho L / 81\pi = 5\text{ } \Omega$.
New wire: radius $r = 3\text{ mm}$. $Area of one thin wire = \pi (3)^2 = 9\pi$.
Resistance of one thin wire $R_{thin} = \rho L / 9\pi$.
Notice that $\rho L / \pi = 5 \times 81 = 405$.
So $R_{thin} = 405 / 9 = 45\text{ } \Omega$.
We have 6 such wires in parallel.
$R_{eq} = R_{thin} / 6 = 45 / 6 = 7.5\text{ } \Omega$.

**Answer: (a)**
</details>

**Q4.** 🔴 A $220\text{V}, 1000\text{W}$ bulb is connected across a $110\text{V}$ mains supply. The power consumed will be:

(a) $1000\text{W}$ &emsp; (b) $750\text{W}$ &emsp; (c) $500\text{W}$ &emsp; (d) $250\text{W}$

<details>
<summary><b>Answer</b></summary>

$P \propto V^2$ (assuming constant resistance).
$V$ is halved ($220 \rightarrow 110$).
So $P$ becomes $(1/2)^2 = 1/4$th.
$P' = 1000 / 4 = \mathbf{250\text{W}}$.

**Answer: (d)**
</details>

---

*Next: [Chapter 8 — Combination of Resistors — Series & Parallel →](./08_series_parallel_resistors.md)*
