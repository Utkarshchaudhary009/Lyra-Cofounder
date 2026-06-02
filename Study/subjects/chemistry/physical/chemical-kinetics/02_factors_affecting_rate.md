# Chapter 2: Factors Affecting Rate of Reaction
## Part I — Foundations

---

## 🎯 Stage 1: The Core Idea

### The Scene

Imagine a dark room where people are walking around randomly. Every time two people bump into each other with enough force, they high-five. The number of high-fives per minute is the **Rate of Reaction**.

How can you increase the number of high-fives per minute?
1. **Put more people in the room (Concentration):** More people = more crowded = more accidental bumps.
2. **Make everyone run instead of walk (Temperature):** They move faster, collide more often, and hit each other with more force.
3. **Bring people out of hiding (Surface Area):** If a group was huddled in a tight circle (a solid block), only the people on the outside could collide. If they spread out (powder), everyone can bump into others.
4. **Lower the force required for a high-five (Catalyst):** Tell them a gentle tap counts as a high-five. Suddenly, way more bumps qualify.

### The Five Major Factors

| Factor | Effect on Rate | Why it works (Microscopic View) |
|--------|----------------|---------------------------------|
| **1. Concentration of Reactants** | Rate increases | More reactant molecules per unit volume $\rightarrow$ increased frequency of collisions. |
| **2. Temperature** | Rate increases significantly | Molecules gain kinetic energy. Collisions happen more frequently AND more molecules possess energy greater than the threshold energy. |
| **3. Surface Area of Solid Reactants** | Rate increases | Finer particles (powdered form) expose more molecules to the surrounding reactants, increasing the collision area. |
| **4. Presence of a Catalyst** | Rate increases | Provides an alternative reaction pathway with a **lower Activation Energy ($E_a$)**, without being consumed itself. |
| **5. Nature of Reactants** | Varies | Reactions involving breaking of strong/many bonds are slower than those involving weak/few bonds. Ionic reactions in solution are usually extremely fast. |

> ⚠️ **Trap Alert:** Adding a positive catalyst does *not* increase the kinetic energy of molecules. It simply lowers the barrier they need to jump over.

---

## 🔬 Stage 2: The Formula Lab

While most of this chapter is conceptual, there are two key mathematical relationships you need to know now (we will dive deeper in Part IV):

### Formula 1: Temperature Coefficient ($\mu$)

For most thermal chemical reactions, the rate roughly **doubles or triples** for every $10^{\circ}\text{C}$ (or $10\text{ K}$) rise in temperature.

$$\text{Temperature Coefficient } (\mu) = \frac{\text{Rate constant at } T + 10}{\text{Rate constant at } T} \approx 2 \text{ to } 3$$

If the temperature increases by $\Delta T$, the new rate can be estimated as:
$$\text{New Rate} = \text{Old Rate} \times \mu^{\frac{\Delta T}{10}}$$
*(Assuming $\mu = 2$ if not given).*

### Formula 2: Partial Pressure (For Gases)

For gaseous reactions, **Partial Pressure** acts exactly like concentration. Compressing a gas (decreasing volume) increases its partial pressure, thereby increasing the rate of reaction.

---

## 🧱 Stage 3: Type-wise Mastery

---

### Type 1: The Temperature Multiplier

**The Pattern:** You are given an initial temperature and a final temperature. You must calculate how many times the rate of reaction increases.

#### Solved Example 2.1
**Q:** The velocity of a reaction is doubled for every $10^{\circ}\text{C}$ rise in temperature. If the temperature is raised from $20^{\circ}\text{C}$ to $60^{\circ}\text{C}$, by what factor does the reaction velocity increase? 🟡

**Solution:**
```
1. Identify the temperature coefficient (μ) = 2.
2. Find the total temperature rise (ΔT): 60 - 20 = 40°C.
3. Determine the number of 10-degree intervals: n = 40 / 10 = 4 intervals.
4. The rate multiplies by μ for every interval.
   Increase factor = μ^n = 2^4 = 16.

Answer: The rate increases 16 times.
```

#### Practice Questions — Type 1

| # | Question | Difficulty |
|---|----------|------------|
| 2.1a | If $\mu = 3$, how many times will the rate increase if temperature is raised from $25^{\circ}\text{C}$ to $45^{\circ}\text{C}$? | 🟢 |
| 2.1b | The rate of a reaction becomes 64 times its initial value when the temperature is increased from $30^{\circ}\text{C}$ to $90^{\circ}\text{C}$. Find the temperature coefficient. | 🟡 |
| 2.1c | A reaction takes 2 hours at $300\text{ K}$. If the temperature is raised to $320\text{ K}$, approximately how much time will it take to complete? (Assume $\mu = 2$). | 🔴 |
| 2.1d | The rate of a reaction becomes 8 times its original value when temperature is raised from $20^{\circ}\text{C}$ to $50^{\circ}\text{C}$. Find $\mu$. | 🟢 |
| 2.1e | At $27^{\circ}\text{C}$, a reaction takes 40 minutes. What will be the time taken at $57^{\circ}\text{C}$? (Assume $\mu = 2$) | 🟢 |
| 2.1f | A reaction has $\mu = 2$. Temperature is increased in two steps: first from $25^{\circ}\text{C}$ to $35^{\circ}\text{C}$, then from $35^{\circ}\text{C}$ to $55^{\circ}\text{C}$. What is the total increase in rate? | 🟡 |
| 2.1g | If the temperature coefficient is 2.5, by what factor does the rate increase when temperature rises from $30^{\circ}\text{C}$ to $60^{\circ}\text{C}$? | 🟡 |
| 2.1h | The rate of a reaction quadruples when temperature is increased from $25^{\circ}\text{C}$ to $45^{\circ}\text{C}$. At what temperature will the rate become 64 times its value at $25^{\circ}\text{C}$? | 🔴 |
| 2.1i | At $300\text{ K}$, a reaction takes 1 hour 40 minutes. At what temperature will it be completed in 6 minutes 15 seconds? (Assume $\mu = 2$) | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 1</summary>

**2.1a:**
- $\Delta T = 45 - 25 = 20^{\circ}\text{C}$. Number of intervals $n = 20/10 = 2$.
- Increase factor $= 3^2 = 9$ times.

**2.1b:**
- $\Delta T = 90 - 30 = 60^{\circ}\text{C}$. Number of intervals $n = 6$.
- $\mu^6 = 64$. Since $2^6 = 64$, the temperature coefficient $\mu = 2$.

**2.1c:**
- $\Delta T = 320 - 300 = 20\text{ K}$. Intervals $n = 2$.
- Rate becomes $2^2 = 4$ times faster.
- Time is inversely proportional to rate. Since the reaction is 4 times faster, it takes $1/4$th the time.
- New time $= 2\text{ hours} / 4 = 0.5\text{ hours}$ (or $30\text{ minutes}$).

**2.1d:**
- $\Delta T = 50 - 20 = 30^{\circ}\text{C}$. $n = 3$.
- $\mu^3 = 8 \Rightarrow \mu = 2$.

**2.1e:**
- $\Delta T = 57 - 27 = 30^{\circ}\text{C}$. $n = 3$.
- Rate becomes $2^3 = 8$ times faster.
- Time $= 40 / 8 = 5$ minutes.

**2.1f:**
- First step: $\Delta T = 10^{\circ}\text{C}$, factor $= 2^1 = 2$.
- Second step: $\Delta T = 20^{\circ}\text{C}$, factor $= 2^2 = 4$.
- Total increase $= 2 \times 4 = 8$ times.

**2.1g:**
- $\Delta T = 60 - 30 = 30^{\circ}\text{C}$. $n = 3$.
- Factor $= (2.5)^3 = 15.625 \approx 15.6$ times.

**2.1h:**
- $\mu^2 = 4 \Rightarrow \mu = 2$.
- Need $\mu^n = 64 \Rightarrow 2^n = 64 \Rightarrow n = 6$.
- $\Delta T = 6 \times 10 = 60^{\circ}\text{C}$.
- Final temperature $= 25 + 60 = 85^{\circ}\text{C}$.

**2.1i:**
- 1 hr 40 min $= 100$ min; 6 min 15 s $= 6.25$ min.
- Rate ratio $= 100 / 6.25 = 16$.
- $2^n = 16 \Rightarrow n = 4$.
- $\Delta T = 4 \times 10 = 40\text{ K}$.
- Final temperature $= 300 + 40 = 340\text{ K}$.
</details>

---

### Type 2: Conceptual Logic (Catalyst & Surface Area)

**The Pattern:** Qualitative questions testing your understanding of *why* catalysts or surface area change the rate.

#### Solved Example 2.2
**Q:** Why does powdered chalk react much faster with dilute HCl than a solid piece of chalk of the same mass? 🟢

**Solution:**
```
The powdered chalk has a significantly larger surface area compared to the solid lump.
Because the reaction between a solid and a liquid occurs only at the interface (surface), 
more surface area means more chalk molecules are exposed to the HCl molecules at any given time, 
leading to a higher frequency of collisions and a faster rate of reaction.
```

#### Practice Questions — Type 2

| # | Question | Difficulty |
|---|----------|------------|
| 2.2a | Does a positive catalyst increase the kinetic energy of the reacting molecules? Explain. | 🟡 |
| 2.2b | Coal dust explosions in mines are a major hazard, whereas a large lump of coal is difficult to ignite. Give a chemical reason. | 🟢 |
| 2.2c | Why does increasing the concentration of a reactant generally increase the rate of reaction? | 🟢 |
| 2.2d | A reaction between two ionic compounds in solution is almost instantaneous, while a reaction involving covalent bond breaking takes much longer. Name the factor responsible. | 🟢 |
| 2.2e | Both a catalyst and an increase in temperature increase the rate of a reaction. How does their mechanism differ? | 🟡 |
| 2.2f | Food spoils faster in summer than in winter. Explain using the concepts of temperature and rate of reaction. | 🟡 |
| 2.2g | "A catalyst does not affect the equilibrium constant of a reversible reaction." Is this statement true? Justify your answer. | 🔴 |
| 2.2h | Hydrogen gas reacts with iodine vapor at $400^{\circ}\text{C}$, while the precipitation of silver chloride from aqueous solutions occurs instantly at room temperature. Explain the difference in terms of the nature of reactants. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type 2</summary>

**2.2a:**
- No. A catalyst does NOT increase the kinetic energy of molecules (only temperature does that). It increases the rate by providing an alternative reaction pathway with a lower activation energy, meaning more molecules *already* have enough energy to react.

**2.2b:**
- Coal dust has a massively larger surface area per gram compared to a lump of coal. When dispersed in air, it exposes a huge number of carbon atoms to oxygen simultaneously, leading to an extremely fast reaction rate (an explosion).

**2.2c:**
- Increasing concentration increases the number of reactant molecules per unit volume. This leads to a higher collision frequency, which increases the number of effective collisions per unit time, thereby increasing the rate.

**2.2d:**
- The factor is the **Nature of Reactants**. Ionic reactions involve pre-existing ions that combine instantly via electrostatic attraction. Covalent reactions require bond breaking, which needs energy input, making them much slower.

**2.2e:**
- Temperature increases the **kinetic energy** of molecules, causing more collisions and a larger fraction of molecules to have energy $\geq E_a$.
- A catalyst **lowers the activation energy** by providing an alternative pathway — it does NOT increase kinetic energy of molecules.

**2.2f:**
- In summer, the higher temperature increases the average kinetic energy of molecules. More collisions occur, and a larger fraction of molecules possess energy $\geq E_a$. This speeds up the chemical reactions responsible for food spoilage.

**2.2g:**
- Yes, the statement is true. A catalyst lowers the activation energy for **both** the forward and reverse reactions equally. It speeds up the attainment of equilibrium but does not shift the equilibrium position. Since $K_{eq} = k_f/k_b$, and both rate constants increase by the same factor, $K_{eq}$ remains unchanged.

**2.2h:**
- The reaction $\text{H}_2 + \text{I}_2 \rightarrow 2\text{HI}$ involves breaking strong covalent bonds in $\text{H}_2$ and $\text{I}_2$, requiring high activation energy — hence it needs high temperature ($400^{\circ}\text{C}$).
- $\text{Ag}^+ + \text{Cl}^- \rightarrow \text{AgCl}$ is an ionic reaction in solution — no bonds need to be broken; oppositely charged ions attract instantly. This illustrates how the **nature of reactants** (covalent vs. ionic) drastically affects reaction rates.
</details>

---

## 🔀 Stage 4: Type Mixer

| # | Question | Types Used | Difficulty |
|---|----------|------------|------------|
| 2.M1 | For a gaseous reaction, the volume of the container is suddenly halved. Simultaneously, the temperature is raised by $20\text{ K}$. Qualitatively, what two factors are increasing the reaction rate? | T1 + Gas logic | 🟡 |
| 2.M2 | The concentration of a reactant is doubled and a catalyst is also added. Explain how each factor contributes to the increase in reaction rate. | Conc. + Catalyst | 🟢 |
| 2.M3 | A reaction is carried out at $30^{\circ}\text{C}$. The temperature is raised to $50^{\circ}\text{C}$ and simultaneously the solid reactant is powdered. Qualitatively analyze the combined effect on the rate. | T1 + Surface Area | 🟢 |
| 2.M4 | For a gaseous reaction at constant volume, the temperature is raised from $300\text{ K}$ to $330\text{ K}$. How does this affect both the collision frequency and the fraction of effective collisions? ($\mu = 2$) | T1 + Gas logic | 🟡 |
| 2.M5 | A catalyst lowers the activation energy of a reaction. The temperature is also increased by $20^{\circ}\text{C}$. Which factor has a greater impact — the catalyst or the temperature? (Qualitative comparison) | Catalyst + Temp | 🟡 |
| 2.M6 | A solid reactant is powdered and its concentration is effectively doubled by dissolving it. Explain the combined effect on reaction rate using collision theory. | Surface Area + Conc. | 🟡 |
| 2.M7 | For a reversible gaseous reaction, the volume is halved (doubling pressure), the temperature is raised by $30^{\circ}\text{C}$ ($\mu = 2$), and a catalyst is added. Compare the effects of all three factors on the forward and backward rates. | All factors | 🔴 |
| 2.M8 | A first-order reaction has $\mu = 2$. The temperature is raised from $27^{\circ}\text{C}$ to $57^{\circ}\text{C}$, and simultaneously the initial concentration of the reactant is tripled. By what factor does the initial rate increase? | Conc. + T1 | 🔴 |

<details>
<summary>💡 Detailed Solutions for Type Mixer</summary>

**2.M1:**
- **Factor 1:** Halving the volume doubles the pressure (and concentration) of the gases, increasing collision frequency.
- **Factor 2:** Raising the temperature by $20\text{ K}$ increases the kinetic energy and fraction of effective collisions (roughly quadrupling the rate, assuming $\mu=2$). Both factors synergize to massively increase the rate.

**2.M2:**
- **Doubling concentration** doubles the number of molecules per unit volume, doubling collision frequency and thus the rate.
- **Adding a catalyst** lowers the activation energy, allowing more molecules to react per collision.
- Both act independently and their effects multiply.

**2.M3:**
- **Temperature rise** ($20^{\circ}\text{C}$): Assuming $\mu = 2$, rate increases by $2^2 = 4$ times due to higher kinetic energy and more effective collisions.
- **Powdering** increases surface area, exposing more reactant molecules to collisions.
- Combined effect: rate increases significantly more than either factor alone.

**2.M4:**
- **Collision frequency** increases because molecules move faster at higher temperature.
- **Fraction of effective collisions** also increases because more molecules have energy $\geq E_a$.
- With $\mu = 2$ and $\Delta T = 30\text{ K}$, $n = 3$, rate increases by $2^3 = 8$ times.
- Note: The concentration (pressure) does NOT change since volume is constant.

**2.M5:**
- A reduction in $E_a$ (e.g., from 80 to 60 kJ/mol) dramatically increases the fraction of molecules that can react — this is an exponential effect (orders of magnitude).
- A $20^{\circ}\text{C}$ rise with $\mu = 2$ gives a $4\times$ increase.
- Typically, a significant $E_a$ reduction has a much larger impact than a moderate temperature rise.

**2.M6:**
- **Powdering** increases surface area, exposing more solid molecules to collision with the other reactant.
- **Doubling concentration** of the dissolved reactant doubles the collision frequency in the solution phase.
- Both effects work simultaneously — more solid surface area $\times$ more dissolved reactant molecules = significantly increased rate.

**2.M7:**
- **Halving volume** doubles pressure (concentration) of ALL gaseous species — increases both forward and backward rates equally.
- **Temperature rise of $30^{\circ}\text{C}$** ($\mu = 2$): rate increases by $2^3 = 8$ times for both directions equally.
- **Catalyst** lowers $E_a$ for both forward and backward reactions equally — does not shift equilibrium.
- All three factors affect forward and backward rates proportionally, so equilibrium remains unchanged.

**2.M8:**
- For a first-order reaction, rate $\propto [\text{A}]$. Tripling $[\text{A}]$ triples the rate (factor of $3$).
- Temperature: $\Delta T = 57 - 27 = 30^{\circ}\text{C}$, $n = 3$, factor $= 2^3 = 8$.
- Combined factor $= 3 \times 8 = 24$. The initial rate increases 24 times.
</details>

---

## 📋 Stage 5: Board Arsenal

| # | Question | Difficulty |
|---|----------|------------|
| 2.B1 | List four factors which affect the rate of a chemical reaction. *(NCERT)* | 🟢 |
| 2.B2 | Explain the effect of a catalyst on the rate of a reaction using an energy profile diagram concept. | 🟡 |
| 2.B3 | Why are reactions between ionic compounds in aqueous solutions usually very fast? | 🟡 |
| 2.B4 | What is the temperature coefficient ($\mu$) of a reaction? What is its typical range for most chemical reactions? | 🟢 |
| 2.B5 | State and explain the effect of concentration on the rate of a reaction using the collision theory. | 🟢 |
| 2.B6 | Explain with the help of a Maxwell-Boltzmann distribution curve why even a small increase in temperature causes a large increase in reaction rate. | 🟡 |
| 2.B7 | Distinguish between collision frequency and effective collisions. Which one is directly affected by the presence of a catalyst? | 🟡 |
| 2.B8 | Why does the rate of most reactions roughly double for every $10^{\circ}\text{C}$ rise in temperature? Explain using the Arrhenius equation. | 🟡 |
| 2.B9 | Using collision theory, explain how concentration, temperature, and a catalyst each increase the rate of a reaction. Which of these factors increases the fraction of molecules with energy greater than the activation energy? | 🔴 |
| 2.B10 | Sketch a reaction profile (energy vs. reaction coordinate) showing the effect of (i) a catalyst and (ii) an increase in temperature. Clearly label the activation energies for both the catalyzed and uncatalyzed paths. | 🔴 |

<details>
<summary>💡 Detailed Solutions for Board Arsenal</summary>

**2.B1:**
1. Concentration of reactants
2. Temperature of the system
3. Presence of a catalyst
4. Surface area of solid reactants (and nature of reactants)

**2.B2:**
- A catalyst provides an alternative reaction pathway that requires a lower activation energy ($E_a$). Because the energy barrier is lower, a much larger fraction of the reactant molecules possess enough energy to cross the barrier and turn into products, thereby increasing the rate.

**2.B3:**
- Ionic compounds in aqueous solutions already exist as free ions. There are no covalent bonds that need to be broken before the reaction can occur. The oppositely charged ions simply attract each other instantly, making the reaction extremely fast.

**2.B4:**
- The temperature coefficient ($\mu$) is the ratio of the rate constant at $T + 10\text{ K}$ to that at $T\text{ K}$: $\mu = k_{T+10}/k_T$.
- For most thermal reactions, $\mu$ lies in the range of 2 to 3.

**2.B5:**
- Increasing concentration increases the number of reactant molecules per unit volume.
- According to collision theory, this leads to a higher collision frequency (more collisions per unit time), which increases the number of effective collisions, thereby increasing the rate of reaction.

**2.B6:**
- The Maxwell-Boltzmann distribution shows the spread of molecular kinetic energies.
- At a higher temperature, the curve flattens and shifts to the right.
- Even a small temperature increase causes a significant increase in the area under the curve beyond $E_a$ (the fraction of molecules with sufficient energy).
- Since this fraction appears in the Arrhenius equation exponentially ($e^{-E_a/RT}$), the rate increases substantially.

**2.B7:**
- **Collision frequency ($Z$)** is the total number of collisions per unit time. It depends on concentration and temperature.
- **Effective collisions** are those with sufficient energy and proper orientation to lead to product formation.
- A catalyst directly increases the fraction of effective collisions by lowering $E_a$, allowing more collisions to have sufficient energy.

**2.B8:**
- According to the Arrhenius equation, $k = Ae^{-E_a/RT}$, the exponential term is highly sensitive to temperature changes when $E_a$ is large relative to $RT$.
- For typical $E_a$ values ($\approx 50\text{ kJ/mol}$), a $10^{\circ}\text{C}$ rise near room temperature approximately doubles $k$.
- This is why the temperature coefficient is approximately 2 for many reactions.

**2.B9:**
- **Concentration** increases collision frequency (more molecules per unit volume).
- **Temperature** increases both collision frequency (faster molecules) AND the fraction of molecules with $E \geq E_a$ (kinetic energy distribution shifts right).
- **Catalyst** lowers $E_a$, which increases the fraction of effective collisions.
- Temperature is the only factor that increases the fraction of molecules with $E \geq E_a$ (by shifting the distribution). A catalyst lowers the threshold $E_a$, so more of the existing molecules qualify.

**2.B10:**
- (i) **Catalyst:** Draw the energy profile with reactants, products, and the activation energy hump. Show a second, lower-energy pathway (dashed curve) with a lower peak — this is the catalyzed path. Label $E_a(\text{uncatalyzed})$ and $E_a(\text{catalyzed})$.
- (ii) **Temperature:** The energy profile itself does NOT change. Instead, the Maxwell-Boltzmann distribution superimposed on it changes — at higher $T$, more molecules populate higher energy levels, increasing the fraction above $E_a$.
- Key point: Temperature affects the distribution of molecular energies, not the activation barrier itself.
</details>

---

## 🚀 Stage 6: JEE Mains Arena

**Q2.J1 🟡**
The rate of a reaction doubles when the temperature changes from $300\text{ K}$ to $310\text{ K}$. By what factor will the rate of reaction change if the temperature is increased from $300\text{ K}$ to $340\text{ K}$?
<br>
(A) 4 <br>
(B) 8 <br>
(C) 16 <br>
(D) 32

**Q2.J2 🟡**
Which of the following statements is INCORRECT regarding a positive catalyst?
<br>
(A) It provides a new reaction path. <br>
(B) It lowers the activation energy. <br>
(C) It increases the average kinetic energy of the reacting molecules. <br>
(D) It does not alter the enthalpy change ($\Delta H$) of the reaction.

**Q2.J3 🟢**
At $27^{\circ}\text{C}$, a reaction takes 80 minutes. Assuming $\mu = 2$, the time taken for the same reaction at $57^{\circ}\text{C}$ will be:
<br>
(A) 5 minutes <br>
(B) 10 minutes <br>
(C) 20 minutes <br>
(D) 40 minutes

**Q2.J4 🟢**
Which of the following factors does NOT affect the rate of a chemical reaction?
<br>
(A) Temperature <br>
(B) Catalyst <br>
(C) Molecular mass of product <br>
(D) Surface area of solid reactant

**Q2.J5 🟡**
The rate of a gaseous reaction becomes 27 times when the volume of the container is reduced to one-third. What is the order of the reaction with respect to the gaseous reactant?
<br>
(A) 0 <br>
(B) 1 <br>
(C) 2 <br>
(D) 3

**Q2.J6 🟡**
When a catalyst is added to a reversible reaction at equilibrium:
<br>
(A) Only the forward rate increases <br>
(B) Only the backward rate increases <br>
(C) Both forward and backward rates increase equally <br>
(D) The equilibrium constant increases

**Q2.J7 🟡**
For a reaction, $\mu = 2.8$. The temperature is increased from $25^{\circ}\text{C}$ to $55^{\circ}\text{C}$. The approximate increase in rate is:
<br>
(A) 8.4 times <br>
(B) 12.5 times <br>
(C) 22.0 times <br>
(D) 5.6 times

**Q2.J8 🔴**
At $300\text{ K}$, a first-order reaction takes 30 minutes for 50% completion. At $320\text{ K}$, it takes 1 minute 52.5 seconds for 50% completion. The temperature coefficient is:
<br>
(A) 2 <br>
(B) 3 <br>
(C) 4 <br>
(D) 5

**Q2.J9 🔴**
Consider the following statements regarding collision theory:
<br>
I. Every collision results in product formation.
<br>
II. Molecules must have energy $\geq E_a$ for an effective collision.
<br>
III. Proper orientation of molecules is necessary for reaction.
<br>
Which of the above is/are correct?
<br>
(A) I and II only <br>
(B) II and III only <br>
(C) I and III only <br>
(D) I, II, and III

**Q2.J10 🔴**
A reaction has rate constants $k_1$ at $300\text{ K}$ and $k_2$ at $320\text{ K}$. If $k_2/k_1 = 6.25$, the value of the temperature coefficient is:
<br>
(A) 2.0 <br>
(B) 2.5 <br>
(C) 3.0 <br>
(D) 3.5

<details>
<summary>💡 Full Solutions — JEE Mains Arena</summary>

**2.J1 → Answer: (C)**
- The temperature coefficient $\mu = 2$.
- $\Delta T = 340 - 300 = 40\text{ K}$.
- $n = 40 / 10 = 4$.
- Factor $= 2^4 = 16$.

**2.J2 → Answer: (C)**
- Only temperature increases average kinetic energy. A catalyst simply lowers the threshold required.

**2.J3 → Answer: (B)**
- $\Delta T = 57 - 27 = 30^{\circ}\text{C}$, $n = 3$.
- Rate becomes $2^3 = 8$ times faster.
- Time $= 80/8 = 10$ minutes.

**2.J4 → Answer: (C)**
- Molecular mass of the product does not affect the rate. Rate depends on concentration of reactants, temperature, catalyst, and surface area.

**2.J5 → Answer: (D)**
- Volume reduced to $1/3$, so concentration increases 3 times.
- Rate increases $3^x = 27 = 3^3$, so $x = 3$. The reaction is third order with respect to the gaseous reactant.

**2.J6 → Answer: (C)**
- A catalyst lowers $E_a$ for both forward and backward reactions equally. The equilibrium constant remains unchanged.

**2.J7 → Answer: (C)**
- $\Delta T = 55 - 25 = 30^{\circ}\text{C}$, $n = 3$.
- Factor $= (2.8)^3 = 21.952 \approx 22.0$ times.

**2.J8 → Answer: (C)**
- At $300\text{ K}$: $t_{1/2} = 30$ min $= 1800$ s.
- At $320\text{ K}$: $t_{1/2} = 1\text{ min }52.5\text{ s} = 112.5$ s.
- Rate ratio: $1800 / 112.5 = 16$.
- $\Delta T = 320 - 300 = 20\text{ K}$, $n = 2$.
- $\mu^2 = 16 \Rightarrow \mu = 4$.

**2.J9 → Answer: (B)**
- I is false: Not every collision results in product formation — only effective collisions do.
- II is true: Molecules need energy $\geq E_a$ for effective collisions.
- III is true: Proper orientation is necessary for bond formation.

**2.J10 → Answer: (B)**
- $\Delta T = 320 - 300 = 20\text{ K}$, $n = 2$.
- $\mu^2 = 6.25 \Rightarrow \mu = 2.5$.
</details>

---

## Key Takeaways from Chapter 2

| Factor | Mechanism of action |
|--------|---------------------|
| Concentration | More particles $\rightarrow$ more collisions |
| Temperature | More kinetic energy $\rightarrow$ harder collisions + more particles cross $E_a$ |
| Catalyst | Provides new path $\rightarrow$ lower $E_a$ |

---

## 🧠 Stage 7: Statement & Assertion-Reasoning

| # | Question | Difficulty |
|---|----------|------------|
| 2.S1 | **Assertion (A):** The rate of a reaction increases with an increase in temperature.<br>**Reason (R):** The number of effective collisions increases because a larger fraction of molecules possess energy greater than the activation energy. | 🟢 |
| 2.S2 | **Assertion (A):** Powdered zinc reacts faster with HCl than a solid block of zinc.<br>**Reason (R):** Powdering the zinc decreases its activation energy. | 🟡 |
| 2.S3 | **Assertion (A):** A catalyst increases the rate of reaction but does not participate in it.<br>**Reason (R):** The catalyst is regenerated completely at the end of the reaction. | 🟡 |
| 2.S4 | **Assertion (A):** Increasing the concentration of reactants increases the rate of reaction.<br>**Reason (R):** The activation energy decreases with increasing concentration. | 🟢 |
| 2.S5 | **Assertion (A):** Reactions between ionic compounds in aqueous solution are extremely fast.<br>**Reason (R):** Ionic reactions involve breaking of strong covalent bonds. | 🟢 |
| 2.S6 | **Assertion (A):** The temperature coefficient for most reactions lies between 2 and 3.<br>**Reason (R):** For every $10^{\circ}\text{C}$ rise in temperature, the average kinetic energy of molecules approximately doubles. | 🟡 |
| 2.S7 | **Assertion (A):** A catalyst does not change the equilibrium constant of a reversible reaction.<br>**Reason (R):** A catalyst lowers the activation energy for both forward and backward reactions by the same amount. | 🟡 |
| 2.S8 | **Assertion (A):** A lump of coal burns slowly while coal dust explodes.<br>**Reason (R):** Coal dust has a much larger surface area exposed to oxygen, which increases the collision frequency. | 🟡 |
| 2.S9 | **Assertion (A):** In gaseous reactions, increasing pressure by reducing volume at constant temperature increases the rate of reaction.<br>**Reason (R):** The concentration of gaseous reactants increases when volume is decreased, leading to more frequent collisions. | 🔴 |

<details>
<summary>💡 Detailed Explanations for Stage 7</summary>

**2.S1 → Answer: (A)**
- Both are true and R is the exact microscopic reason for A.

**2.S2 → Answer: (C)**
- A is true (more surface area).
- R is false. Powdering increases surface area, it does NOT change the activation energy (only a catalyst does that).

**2.S3 → Answer: (A)**
- Both are true and R explains why it is considered "not consumed" overall, even though it may temporarily form intermediate bonds during the reaction.

**2.S4 → Answer: (C)**
- A is true (higher concentration $\rightarrow$ more collisions $\rightarrow$ faster rate).
- R is false. Increasing concentration does NOT decrease activation energy. Activation energy is an intrinsic property of the reaction.

**2.S5 → Answer: (C)**
- A is true.
- R is false. Ionic reactions involve pre-existing ions in solution; no covalent bonds need to be broken.

**2.S6 → Answer: (C)**
- A is true. $\mu$ is empirically found to be 2–3 for most thermal reactions.
- R is false. Average kinetic energy is proportional to absolute temperature ($KE \propto T$). A $10^{\circ}\text{C}$ rise from $300\text{ K}$ to $310\text{ K}$ increases KE by only $310/300 \approx 1.033$ times, not double.

**2.S7 → Answer: (A)**
- Both A and R are true, and R is the correct explanation of A.
- A catalyst affects both forward and backward rates equally, so $K_{eq} (= k_f/k_b)$ remains unchanged.

**2.S8 → Answer: (A)**
- Both A and R are true, and R is the correct explanation of A.
- Coal dust has a much larger surface area, exposing more carbon atoms to oxygen per unit time. This increases the collision frequency, dramatically accelerating the combustion rate.

**2.S9 → Answer: (A)**
- Both A and R are true, and R is the correct explanation of A.
- Decreasing volume at constant temperature increases the concentration (partial pressure) of gaseous reactants, leading to higher collision frequency and faster rate.
</details>

---

## 🏆 Stage 8: MCQ Mastery

**Q2.M1 🟢**
The role of a catalyst is to change:
<br>
(A) Gibbs energy of reaction <br>
(B) Enthalpy of reaction <br>
(C) Activation energy of reaction <br>
(D) Equilibrium constant

**Q2.M2 🟡**
For a reaction, the temperature coefficient is 2.5. If the temperature is raised by $30^{\circ}\text{C}$, the rate of reaction increases by approximately:
<br>
(A) 7.5 times <br>
(B) 15.6 times <br>
(C) 6.25 times <br>
(D) 10 times

**Q2.M3 🟢**
For a gaseous reaction, if the volume of the container is reduced, the rate increases because:
<br>
(A) Temperature increases <br>
(B) Concentration of gases increases <br>
(C) Catalyst is formed <br>
(D) Activation energy decreases

**Q2.M4 🟢**
Which of the following forms will react fastest with dilute HCl?
<br>
(A) One large piece of marble <br>
(B) Two medium pieces of marble <br>
(C) Marble powder <br>
(D) All at the same rate

**Q2.M5 🟡**
If $\mu = 2$, the temperature at which the rate of a reaction at $27^{\circ}\text{C}$ becomes 32 times is:
<br>
(A) $47^{\circ}\text{C}$ <br>
(B) $57^{\circ}\text{C}$ <br>
(C) $67^{\circ}\text{C}$ <br>
(D) $77^{\circ}\text{C}$

**Q2.M6 🟡**
A catalyst increases the rate of a reaction by:
<br>
(A) Increasing the kinetic energy of molecules <br>
(B) Decreasing the enthalpy of the reaction <br>
(C) Providing an alternative path with lower activation energy <br>
(D) Increasing the collision frequency

**Q2.M7 🟡**
Reactions between covalent compounds are generally slower than ionic reactions because:
<br>
(A) Covalent compounds have lower molecular masses <br>
(B) Covalent bond breaking requires significant energy <br>
(C) Covalent compounds are always insoluble <br>
(D) Ionic compounds are always concentrated

**Q2.M8 🔴**
For a reaction, the temperature coefficient is 2. The rate at $50^{\circ}\text{C}$ is $R$. What is the rate at $30^{\circ}\text{C}$?
<br>
(A) $R/2$ <br>
(B) $R/4$ <br>
(C) $R/8$ <br>
(D) $R/16$

**Q2.M9 🔴**
Consider the following statements:
<br>
(i) A catalyst changes the Gibbs energy of a reaction.
<br>
(ii) Temperature affects both collision frequency and fraction of effective collisions.
<br>
(iii) Surface area affects only the pre-exponential factor ($A$) in the Arrhenius equation.
<br>
Which are correct?
<br>
(A) (i) and (ii) only <br>
(B) (ii) and (iii) only <br>
(C) (i) and (iii) only <br>
(D) (i), (ii), and (iii)

<details>
<summary>💡 Full Solutions — MCQ Mastery</summary>

**2.M1 → Answer: (C)**
- A catalyst only changes the activation energy. Thermodynamics ($\Delta G$, $\Delta H$, $K_{eq}$) remain completely unaffected.

**2.M2 → Answer: (B)**
- $n = 30/10 = 3$. Factor $= (2.5)^3 = 15.625$.

**2.M3 → Answer: (B)**
- Reducing volume increases the concentration (partial pressure) of gaseous reactants, which increases collision frequency and thus the rate.

**2.M4 → Answer: (C)**
- Marble powder has the largest surface area, exposing the most CaCO$_3$ molecules to HCl, resulting in the fastest reaction.

**2.M5 → Answer: (D)**
- $\mu^n = 32 = 2^5 \Rightarrow n = 5$. $\Delta T = 5 \times 10 = 50^{\circ}\text{C}$.
- Temperature $= 27 + 50 = 77^{\circ}\text{C}$.

**2.M6 → Answer: (C)**
- A catalyst provides an alternative path with lower $E_a$. It does NOT increase KE, change $\Delta H$, or increase collision frequency.

**2.M7 → Answer: (B)**
- Covalent bond breaking requires significant energy (high $E_a$). Ionic reactions involve pre-existing ions that combine without bond breaking, making them much faster.

**2.M8 → Answer: (B)**
- $\Delta T = 50 - 30 = 20^{\circ}\text{C}$, $n = 2$.
- Rate at $30^{\circ}\text{C} = R / 2^2 = R/4$.

**2.M9 → Answer: (B)**
- (i) False: A catalyst does NOT change $\Delta G$ of the reaction.
- (ii) True: Temperature increases both collision frequency and the fraction of molecules with $E \geq E_a$.
- (iii) True: Surface area affects the frequency factor $A$, not $E_a$.
</details>
