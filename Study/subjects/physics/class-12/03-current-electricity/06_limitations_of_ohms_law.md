# Chapter 6: Limitations of Ohm's Law (Non-Ohmic Devices)

> *NCERT Section 3.6*

---

## 🎯 Stage 1: The Core Idea

### The Rebellion Against the Straight Line

Ohm's Law ($V = IR$) suggests a perfectly obedient relationship: double the voltage, and the current doubles exactly. Plotting $V$ against $I$ gives a perfectly straight line passing through the origin. 

But nature isn't always that obedient. Many electrical components completely ignore Ohm's Law. These are called **Non-Ohmic Devices**. 

When a device disobeys Ohm's law, its $V-I$ graph is **not a straight line**. It might curve, it might depend on the direction of current, or it might even show current increasing while voltage *decreases*!

### The Three Ways to Break Ohm's Law

NCERT classifies the failure of Ohm's law into three distinct categories:

1. **V ceases to be proportional to I (The Curve):** 
   As current increases, the conductor gets hot. Its resistance increases, so the current doesn't rise as much as Ohm's law predicts. The graph bends. (Example: A standard incandescent light bulb filament).

2. **The relationship depends on the sign of V (The One-Way Street):** 
   If you apply $+5\text{ V}$, you get a huge current. If you reverse the battery to $-5\text{ V}$, you get almost zero current. The device cares about the *direction*. (Example: A semiconductor p-n junction diode).

3. **V is not unique for a given I (The Rollercoaster):** 
   There can be multiple different voltages that produce the exact same current. The graph goes up, then dips down, then goes up again. (Example: Gallium Arsenide - GaAs, used in high-speed electronics).

---

## 🔬 Stage 2: The Formula Lab

### Static vs. Dynamic Resistance

Since $V$ is not proportional to $I$ in non-ohmic devices, "Resistance" isn't a single constant number anymore. We have to define it in two ways:

#### 1. Static Resistance (DC Resistance)
The resistance at one specific operating point on the curve.
$$R_{static} = \frac{V}{I}$$
*This is just the ratio of coordinates at a single point on the graph.*

#### 2. Dynamic Resistance (AC Resistance) ⭐
The resistance for small changes in voltage and current. It's the reciprocal of the slope of the $I-V$ graph at a specific point.
$$R_{dynamic} = \frac{\Delta V}{\Delta I} = \frac{dV}{dI}$$
*If the graph is an $I-V$ curve (I on y-axis), $R_{dynamic} = 1 / \text{slope}$.*

---

## 🧱 Stage 3: Type-wise Mastery

### Type 1: Identifying Ohmic vs. Non-Ohmic Behavior

**Pattern:** "Given a graph or data, classify the device."

**Solved Example** 🟢

> The $V-I$ graph of a component is a straight line passing through the origin for voltages from $0\text{V}$ to $2\text{V}$, but bends towards the voltage axis for $V > 2\text{V}$. Is it ohmic?

<details>
<summary><b>Solution</b></summary>

A device is ohmic ONLY if the $V-I$ graph is a straight line through the origin for all applied voltages. Since the graph bends for $V > 2\text{V}$, the device is **non-ohmic**. The bending towards the voltage axis means it requires more voltage to push the same increment of current — its resistance is increasing (likely due to heating).
</details>

**Practice:**

1. 🟢 A student plots $V$ vs $I$ for a wire and gets a straight line passing through $(0,0)$. However, if the current is allowed to flow for 10 minutes before taking the reading, the point deviates from the line. Why?

<details>
<summary><b>Answer</b></summary>

Heating effect. Passing current for a long time increases the temperature of the wire, which increases its resistance, causing it to deviate from strict ohmic behavior (which assumes constant temperature).
</details>

2. 🟢 Look at an $I-V$ graph for a p-n junction diode. In forward bias, current shoots up after $0.7\text{ V}$. In reverse bias, current is almost zero. Which limitation of Ohm's law does this represent?

<details>
<summary><b>Answer</b></summary>

Limitation 2: The relation between $V$ and $I$ depends on the sign (direction) of $V$.
</details>

3. 🟡 A device exhibits a $V-I$ curve where current increases, then decreases, then increases again as voltage goes up. Give an example of such a material and state which limitation this is.

<details>
<summary><b>Answer</b></summary>

Example: Gallium Arsenide (GaAs) or a Tunnel Diode. 
Limitation 3: The relation between $V$ and $I$ is not unique (one current value can correspond to multiple voltage values).
</details>

4. 🟡 Are electrolytes (like NaCl solution) ohmic or non-ohmic conductors? Explain briefly.

<details>
<summary><b>Answer</b></summary>

**Non-ohmic**. The $V-I$ graph for electrolytes is not a straight line passing through the origin. They require a certain minimum voltage (back EMF due to polarization at electrodes) before steady current starts flowing.
</details>

---

### Type 2: Calculating Dynamic Resistance ⭐⭐

**Pattern:** "Given a curved $I-V$ graph or data points, find the dynamic resistance in a specific range."

**Solved Example** 🟡

> From the $I-V$ characteristic of a diode, the current is $10\text{ mA}$ at $V = 0.7\text{ V}$ and $20\text{ mA}$ at $V = 0.8\text{ V}$. Find the dynamic resistance in this region.

<details>
<summary><b>Solution</b></summary>

$V_1 = 0.7\text{ V}, I_1 = 10\text{ mA} = 10 \times 10^{-3}\text{ A}$
$V_2 = 0.8\text{ V}, I_2 = 20\text{ mA} = 20 \times 10^{-3}\text{ A}$

$\Delta V = 0.8 - 0.7 = 0.1\text{ V}$
$\Delta I = (20 - 10) \times 10^{-3} = 10 \times 10^{-3}\text{ A}$

$R_{dynamic} = \frac{\Delta V}{\Delta I} = \frac{0.1}{10 \times 10^{-3}} = \frac{0.1}{0.01} = \mathbf{10\text{ } \Omega}$
</details>

**Practice:**

1. 🟢 A non-ohmic device has current $I = 2\text{ A}$ at $V = 10\text{ V}$ and $I = 2.5\text{ A}$ at $V = 12\text{ V}$. Find its dynamic resistance in this voltage range.

<details>
<summary><b>Answer</b></summary>

$\Delta V = 12 - 10 = 2\text{ V}$
$\Delta I = 2.5 - 2 = 0.5\text{ A}$
$R_{dynamic} = \Delta V / \Delta I = 2 / 0.5 = \mathbf{4\text{ } \Omega}$
</details>

2. 🟢 For the same device in Q1, find its static resistance at exactly $V = 10\text{ V}$.

<details>
<summary><b>Answer</b></summary>

$R_{static} = V / I = 10 / 2 = \mathbf{5\text{ } \Omega}$ 
*(Notice how dynamic and static resistance are different!)*
</details>

3. 🟡 The current-voltage relation of a device is given by $I = (0.5 V^2)\text{ mA}$, where $V$ is in volts. Calculate the dynamic resistance at $V = 4\text{ V}$.

<details>
<summary><b>Answer</b></summary>

We need $R_{dynamic} = dV/dI = 1 / (dI/dV)$.
Given $I = 0.5 V^2 \times 10^{-3}\text{ A}$.
$dI/dV = 2 \times 0.5 \times V \times 10^{-3} = V \times 10^{-3}\text{ A/V}$.
At $V = 4\text{ V}$, $dI/dV = 4 \times 10^{-3}$.
$R_{dynamic} = 1 / (4 \times 10^{-3}) = 1000 / 4 = \mathbf{250\text{ } \Omega}$.
</details>

4. 🔴 A varistor has a characteristic $I = kV^3$. If its static resistance at $V = 10\text{ V}$ is $100\text{ } \Omega$, what is its dynamic resistance at $V = 10\text{ V}$?

<details>
<summary><b>Answer</b></summary>

At $V=10\text{ V}$, $R_{static} = V/I = 100 \implies I = V/100 = 10/100 = 0.1\text{ A}$.
Since $I = kV^3$, we have $0.1 = k(10)^3 \implies k = 0.1/1000 = 10^{-4}$.
So $I = 10^{-4} V^3$.
Now find dynamic resistance: $dI/dV = 3 \times 10^{-4} V^2$.
At $V=10\text{ V}$, $dI/dV = 3 \times 10^{-4} \times 100 = 0.03\text{ A/V}$.
$R_{dynamic} = 1 / (dI/dV) = 1 / 0.03 = 100/3 = \mathbf{33.3\text{ } \Omega}$.
*(Dynamic resistance is exactly 1/3 of static resistance here!)*
</details>

---

### Type 3: Negative Differential Resistance ⭐⭐

**Pattern:** "Identify regions on a graph where dynamic resistance is negative."

**Solved Example** 🟡

> The $I-V$ characteristic of a material shows current peaking at $V = 5\text{ V}$ ($I = 10\text{ mA}$) and then dropping to $I = 4\text{ mA}$ at $V = 15\text{ V}$. What is the nature of dynamic resistance between $5\text{ V}$ and $15\text{ V}$?

<details>
<summary><b>Solution</b></summary>

In the region from $V = 5\text{ V}$ to $V = 15\text{ V}$, the voltage *increases* ($\Delta V$ is positive), but the current *decreases* ($\Delta I$ is negative).
$R_{dynamic} = \frac{+10\text{ V}}{-6\text{ mA}} = -1667\text{ } \Omega$.
The dynamic resistance is **negative**. This is called the **Negative Resistance Region**, utilized in oscillator circuits.
</details>

**Practice:**

1. 🟡 In a GaAs $I-V$ curve, there is a linear region, a peak, a valley, and a second rise. In which region is the dynamic resistance negative?

<details>
<summary><b>Answer</b></summary>

Between the **peak and the valley**. Here, as voltage increases, current decreases, making $\Delta I / \Delta V$ negative.
</details>

2. 🔴 If a device operates in the negative dynamic resistance region, what happens to the current if a small positive voltage pulse is added to the steady DC bias?

<details>
<summary><b>Answer</b></summary>

Since $\Delta V$ is positive and $R_{dynamic}$ is negative, $\Delta I = \Delta V / R_{dynamic}$ will be **negative**. The current will actually **decrease** temporarily when the voltage is bumped up!
</details>

---

## 🔀 Stage 4: Type Mixer

**Q1.** 🔴 You are given three $V-I$ graphs:
(A) A straight line through the origin.
(B) A curve passing through the origin but bending towards the V-axis.
(C) A curve that passes through the origin, has a peak, then dips before rising again.
Identify the possible materials/devices for each graph and their Ohmic/Non-Ohmic nature.

<details>
<summary><b>Solution</b></summary>

(A) **Ohmic**. Material: Copper wire, standard resistor (at constant temperature).
(B) **Non-Ohmic (Type 1)**. Material: Bulb filament (heats up, resistance increases).
(C) **Non-Ohmic (Type 3)**. Material: Gallium Arsenide (GaAs) or tunnel diode.
</details>

**Q2.** 🔴 ⭐ A thermistor has a resistance that drops exponentially with temperature: $R = A e^{B/T}$. If a constant voltage $V$ is applied across it, initially the current is $I_0$. As the thermistor heats up due to the current, what happens to the $V-I$ curve? Is it ohmic?

<details>
<summary><b>Solution</b></summary>

1. It is **non-ohmic** because resistance is not constant; it depends on the temperature, which in turn depends on the current ($I^2R$ heating).
2. As current passes, the thermistor heats up ($T$ increases).
3. As $T$ increases, $R$ decreases exponentially.
4. Since $R$ decreases, the current $I$ increases even more for the same $V$.
5. The $V-I$ curve will bend sharply towards the $I$-axis (unlike a metal bulb filament which bends towards the $V$-axis). If plotted as $I$ vs $V$, the slope increases dramatically.
</details>

---

## 📋 Stage 5: Board Arsenal

**Q1.** 🟢 What are non-ohmic devices? Give two examples. *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

Devices or materials that do not obey Ohm's law are called non-ohmic devices. For such devices, the voltage-current ($V-I$) graph is not a straight line passing through the origin.
**Examples:** Semiconductor diode, Gallium Arsenide (GaAs), transistor, light bulb filament (over wide temperature ranges).
</details>

**Q2.** 🟡 State three distinct ways in which Ohm's law can fail for certain materials. *(3 marks)*

<details>
<summary><b>Model Answer</b></summary>

1. **Non-linearity:** $V$ ceases to be proportional to $I$ (e.g., $V-I$ curve bends due to heating of a conductor).
2. **Direction dependence:** The relation between $V$ and $I$ depends on the sign of $V$. Reversing the polarity of voltage does not produce a current of the same magnitude (e.g., p-n junction diode).
3. **Non-uniqueness:** The relation between $V$ and $I$ is not unique; a single value of current can correspond to more than one value of voltage (e.g., Gallium Arsenide exhibits a negative resistance region).
</details>

**Q3.** 🟡 Define dynamic resistance. How is it calculated from an $I-V$ graph? *(2 marks)*

<details>
<summary><b>Model Answer</b></summary>

**Dynamic resistance** is defined as the ratio of a small change in voltage ($\Delta V$) to the corresponding small change in current ($\Delta I$) in a non-ohmic device at a particular operating point.
$R_{dynamic} = \frac{\Delta V}{\Delta I}$
From an $I-V$ graph (current on y-axis, voltage on x-axis), the dynamic resistance at any point is the **reciprocal of the slope** of the tangent to the curve at that point.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q1.** 🟡 ⭐ The $I-V$ characteristics of a non-linear device is given by $I = aV^2 + bV$, where $a$ and $b$ are constants. The dynamic resistance of the device at $V = V_0$ is:

(a) $\frac{1}{aV_0 + b}$ &emsp; (b) $\frac{1}{2aV_0 + b}$ &emsp; (c) $2aV_0 + b$ &emsp; (d) $\frac{V_0}{aV_0^2 + bV_0}$

<details>
<summary><b>Answer</b></summary>

Dynamic resistance $R_{dyn} = \left(\frac{dI}{dV}\right)^{-1}$.
Given $I = aV^2 + bV$.
Differentiating w.r.t $V$:
$\frac{dI}{dV} = 2aV + b$
At $V = V_0$, $\frac{dI}{dV} = 2aV_0 + b$.
Therefore, $R_{dyn} = \frac{1}{2aV_0 + b}$.

**Answer: (b)**
*(Option D is the static resistance! Don't fall for it.)*
</details>

**Q2.** 🔴 A semiconductor device is connected in a series circuit with a battery and a resistor. If the polarity of the battery is reversed, the current in the circuit drops by a factor of $10^4$. Which limitation of Ohm's law does this device primarily exhibit?

(a) Non-uniqueness of $V-I$ curve
(b) Saturation of drift velocity
(c) Dependence of $V-I$ relation on the sign of $V$
(d) Temperature dependence of resistivity

<details>
<summary><b>Answer</b></summary>

The device permits current easily in one direction but blocks it almost entirely when the voltage is reversed. This indicates that the current magnitude heavily depends on the **polarity (sign) of the applied voltage**. This is the classic characteristic of a diode.

**Answer: (c)**
</details>

**Q3.** 🔴 ⭐ Which of the following graphs best represents the $V-I$ characteristics of a light bulb filament?
*(Assume V on x-axis, I on y-axis)*

(a) Straight line passing through origin
(b) Curve bending upwards (slope increasing)
(c) Curve bending downwards (slope decreasing)
(d) S-shaped curve passing through origin

<details>
<summary><b>Answer</b></summary>

As voltage ($V$) increases across a bulb filament, the current ($I$) increases.
This causes $I^2R$ heating, which raises the temperature of the tungsten filament.
For metals, as temperature rises, resistance ($R$) increases.
Since $I = V/R$, as $R$ gets larger, the current $I$ grows *more slowly* than the voltage $V$.
On an $I$ vs $V$ graph, the slope is $1/R$. Since $R$ increases, the slope must **decrease**.
The graph bends downwards towards the $V$-axis.

**Answer: (c)**
</details>

---

*Next: [Chapter 7 — Electrical Energy & Power →](./07_electrical_energy_power.md)*
