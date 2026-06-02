# 5. Complex First Order Reactions

## 1. Key Concepts and Formulas

### Parallel (Competing) First Order Reactions
* **Concept:** A reactant $A$ simultaneously undergoes two or more independent first-order pathways to yield different products (e.g., $A \xrightarrow{k_1} B$ and $A \xrightarrow{k_2} C$).
* **Differential Rate Laws:**
  * Rate of disappearance of $A$: $-\frac{d[A]}{dt} = k_1[A] + k_2[A] = (k_1 + k_2)[A]$
  * Rate of appearance of $B$ and $C$: $\frac{d[B]}{dt} = k_1[A]$ and $\frac{d[C]}{dt} = k_2[A]$
* **Net Rate Constant ($k_{net}$):** The overall rate constant is the sum of the individual rate constants: $k_{net} = k_1 + k_2$.
* **Integrated Rate Law:** $[A]_t = [A]_0 \cdot e^{-(k_1 + k_2)t}$.
* **Effective Half-Life:** Because rates are additive, the inverse of the overall half-life is the sum of the inverses of individual half-lives: 
  $$\frac{1}{(t_{1/2})_{net}} = \frac{1}{(t_{1/2})_1} + \frac{1}{(t_{1/2})_2}$$
* **Product Distribution (Fractional Yield):** The ratio of products formed is directly proportional to their respective rate constants:
  $$\frac{[C]_t}{[B]_t} = \frac{k_2}{k_1}$$
  * $\%\text{ Yield of } B = \left(\frac{k_1}{k_1 + k_2}\right) \times 100\%$
  * $\%\text{ Yield of } C = \left(\frac{k_2}{k_1 + k_2}\right) \times 100\%$
* **Overall Activation Energy ($E_{net}$):** For parallel paths, the net activation energy is the weighted average of individual activation energies:
  $$E_{net} = \frac{k_1 E_1 + k_2 E_2}{k_1 + k_2}$$

### Sequential (Consecutive) Reactions
* **Concept:** Reactions that proceed from reactants to final products through one or more intermediate stages (e.g., $A \xrightarrow{k_1} B \xrightarrow{k_2} C$).
* **Differential Rate Laws:**
  * $-\frac{d[A]}{dt} = k_1[A]$
  * $\frac{d[B]}{dt} = \text{Rate of formation} - \text{Rate of consumption} = k_1[A] - k_2[B]$
  * $\frac{d[C]}{dt} = k_2[B]$
* **Concentration Profile of Intermediate ($B$):** Solving the differential equations gives:
  $$[B]_t = \frac{k_1 [A]_0}{k_2 - k_1} \left[ e^{-k_1 t} - e^{-k_2 t} \right]$$
* **Time for Maximum Intermediate Concentration ($t_{max}$):** The time at which the concentration of the intermediate $B$ reaches its peak is found by setting $\frac{d[B]}{dt} = 0$:
  $$t_{max} = \frac{\ln(k_1 / k_2)}{k_1 - k_2}$$
* **Limiting Cases:**
  * **Case 1 ($k_1 \gg k_2$):** $A$ converts to $B$ very quickly. $B$ accumulates in the system and then slowly decays to $C$.
  * **Case 2 ($k_2 \gg k_1$):** $B$ converts to $C$ almost instantaneously upon formation. $B$ acts as a transient intermediate (Steady State), and its concentration remains close to zero.

### Multi-step Reaction Profiles and Composite Rate Constants
* **Rate Determining Step (RDS):** In a complex energy profile diagram plotting Potential Energy versus Progress of Reaction, the step with the highest activation energy ($E_a$) peak requires the maximum energy to proceed and is strictly the slowest step (the RDS). Conversely, the step with the smallest $E_a$ is the fastest.
* **Calculating $E_{net}$ from composite $k_{net}$:** If a multi-step reaction yields an overall rate constant derived from individual steps, apply the Arrhenius relationship directly to the powers.
  * *Example:* If $k_{net} = \frac{k_1 \cdot k_2^2}{k_3}$, then taking the Arrhenius substitution $k = Ae^{-E_a/RT}$ yields the relationship: $E_{net} = E_1 + 2E_2 - E_3$.

---

## 2. Types of Questions/Problems that Can Be Asked
* **Yield Percentage Calculations:** Given the individual rate constants of competing paths, calculate the fixed percentage or ratio in which the final products will form.
* **Effective Half-life Computations:** Deducing the total effective half-life of a reactant that decays via multiple parallel radioactive or chemical pathways.
* **Sequential Intermediate Identification:** Graphically identifying reactants, intermediates, and products based on their concentration-time curves (e.g., A strictly decays, C strictly rises, B rises then falls).
* **Time of Maximum Yield ($t_{max}$):** Calculating the exact time required to maximize the yield of an intermediate species in a sequential process.
* **Complex Activation Energy Computations:** Deriving the net activation energy ($E_{net}$) or pre-exponential factor ($A_{net}$) algebraically when an overall rate constant is expressed as a product or quotient of elementary rate constants.
* **Energy Profile Interpretations:** Giving students an energy profile and asking them to identify intermediate wells, fast/slow steps, or deduce whether the net reaction is endothermic or exothermic based on reactant/product baseline levels.

---

## 3. Example Questions with Step-by-Step Solutions

**Example 1: Fractional Yield in a Parallel Reaction**
*Question:* A substance undergoes first-order decomposition following two parallel reactions:
Path 1: $A \rightarrow B$ with $k_1 = 1.26 \times 10^{-4}\text{ s}^{-1}$
Path 2: $A \rightarrow C$ with $k_2 = 3.8 \times 10^{-5}\text{ s}^{-1}$
What are the percentage distributions of $B$ and $C$?
*Solution:*
* Convert constants to the same power for easy addition:
  $k_1 = 12.6 \times 10^{-5}\text{ s}^{-1}$
  $k_2 = 3.8 \times 10^{-5}\text{ s}^{-1}$
* Find $k_{net}$: $k_{net} = k_1 + k_2 = (12.6 + 3.8) \times 10^{-5} = 16.4 \times 10^{-5}\text{ s}^{-1}$.
* Calculate the percentage of $B$: $\%B = \left(\frac{k_1}{k_{net}}\right) \times 100 = \left(\frac{12.6}{16.4}\right) \times 100 \approx 76.83\%$.
* Calculate the percentage of $C$: $\%C = \left(\frac{k_2}{k_{net}}\right) \times 100 = \left(\frac{3.8}{16.4}\right) \times 100 \approx 23.17\%$.

**Example 2: Overall Activation Energy from a Complex Rate Law**
*Question:* Consider a complex reaction taking place in three steps with rate constants $k_1$, $k_2$, and $k_3$. The overall rate constant $k_{net}$ is given by the expression $k_{net} = \left(\frac{k_1 \cdot k_3}{k_2}\right)^{1/2}$. If the activation energies of the three steps are $60\text{ kJ/mol}$, $30\text{ kJ/mol}$, and $10\text{ kJ/mol}$ respectively, find the overall activation energy ($E_{net}$).
*Solution:*
* Write the relationship for $k_{net}$: $k_{net} = \left(\frac{k_1 \cdot k_3}{k_2}\right)^{1/2}$.
* Substitute the Arrhenius equation ($k = Ae^{-E_a/RT}$) into the expression:
  $A_{net} e^{-E_{net}/RT} = \left( \frac{A_1 e^{-E_1/RT} \cdot A_3 e^{-E_3/RT}}{A_2 e^{-E_2/RT}} \right)^{1/2}$
* Equate the powers of $e$ corresponding to the activation energies:
  $-\frac{E_{net}}{RT} = \frac{1}{2} \left( -\frac{E_1}{RT} - \frac{E_3}{RT} - \left(-\frac{E_2}{RT}\right) \right)$
* Simplify the activation energy relationship: $E_{net} = \frac{1}{2}(E_1 + E_3 - E_2)$.
* Substitute the given values ($E_1 = 60$, $E_2 = 30$, $E_3 = 10$):
  $E_{net} = \frac{1}{2}(60 + 10 - 30) = \frac{1}{2}(40) = 20\text{ kJ/mol}$.

**Example 3: Effective Half-Life of Competing Reactions**
*Question:* A molecule undergoes two independent first-order reactions whose respective half-lives are $12\text{ minutes}$ and $3\text{ minutes}$. If both reactions are occurring simultaneously, then the time taken for 50% consumption of the reactant is?
*Solution:*
* Recognize that this is a parallel reaction where the net decay rate is the sum of the individual decay rates.
* Use the relation for net effective half-life: $\frac{1}{(t_{1/2})_{net}} = \frac{1}{(t_{1/2})_1} + \frac{1}{(t_{1/2})_2}$
* Substitute the given half-lives: $\frac{1}{(t_{1/2})_{net}} = \frac{1}{12} + \frac{1}{3}$.
* Find a common denominator to add the fractions: $\frac{1}{12} + \frac{4}{12} = \frac{5}{12}$.
* Invert to find the overall half-life (which is the time taken for 50% consumption): $(t_{1/2})_{net} = \frac{12}{5} = 2.4\text{ minutes}$.

**Example 4: Calculating Intermediates in Parallel Reactions**
*Question:* In a parallel reaction, $A \xrightarrow{k_1} B$ and $A \xrightarrow{k_2} C$, the initial concentration of $A$ is $8\text{ M}$. If the ratio of rate constants is $\frac{k_2}{k_1} = \frac{2}{1}$, what are the concentrations of $B$ and $C$ when $A$ is 25% consumed?
*Solution:*
* Find the amount of $A$ that has reacted at $t_{25\%}$: $\text{Amount reacted} = 25\% \text{ of } 8\text{ M} = 0.25 \times 8 = 2\text{ M}$.
* Let the concentration of $B$ formed be $x$ and $C$ formed be $y$. The total reacted $A$ equals the sum of products formed: $x + y = 2$.
* The ratio of products formed at any time is equal to the ratio of their rate constants: $\frac{[C]}{[B]} = \frac{y}{x} = \frac{k_2}{k_1} = \frac{2}{1}$.
* Substitute $y = 2x$ into the first equation: $x + 2x = 2 \implies 3x = 2 \implies x = \frac{2}{3}\text{ M}$.
* Solve for $y$: $y = 2(\frac{2}{3}) = \frac{4}{3}\text{ M}$.
* *Final Concentrations:* $[B] = \frac{2}{3}\text{ M}$ and $[C] = \frac{4}{3}\text{ M}$.

---

## 4. Practice Questions

**Q1.** For the parallel reactions $A \xrightarrow{k_1} B$ and $A \xrightarrow{k_2} C$, starting with initial concentration of $A$ as $C_{A0}$ and initially $B$ and $C$ are absent. Which of the following is correct regarding the concentrations $C_A, C_B, C_C$ at any time $t$?
(A) $C_A + C_B + C_C = C_{A0}$
(B) $\frac{dC_A}{dt} + \frac{dC_B}{dt} + \frac{dC_C}{dt} = 0$
(C) $\frac{C_C}{C_B} = \frac{k_2}{k_1}$
(D) All of the above

**Q2.** Reactant A converts to product D through the given sequential mechanism:
Step 1: $A \rightarrow B$ (slow; $\Delta H = \text{+ve}$)
Step 2: $B \rightarrow C$ (fast; $\Delta H = \text{-ve}$)
Step 3: $C \rightarrow D$ (fast; $\Delta H = \text{-ve}$)
If the overall net reaction has an evolution of heat, which of the following is true for the energy profile diagram?
(A) The peak for $A \rightarrow B$ is higher than the other peaks.
(B) The well for $B$ is lower than the baseline of $A$.
(C) The final baseline of $D$ is higher than the baseline of $A$.
(D) The peak for $C \rightarrow D$ represents the rate-determining step.

**Q3.** The reaction $A + B \rightarrow D + E$ takes place sequentially as follows:
$A + B \xrightarrow{k_1} 2C$
$C + B \xrightarrow{k_2} 2D$
$C + A \xrightarrow{k_3} 2E$
The rate of disappearance of $C$ ($-\frac{d[C]}{dt}$) is given by:
(A) $k_1[A][B] - k_2[C][B] - k_3[C][A]$
(B) $-2k_1[A][B] + k_2[C][B] + k_3[C][A]$
(C) $2k_1[A][B] - k_2[C][B] - k_3[C][A]$
(D) $k_2[C][B] + k_3[C][A]$

**Q4.** Starting with only reactant A, it undergoes parallel decomposition:
$A \xrightarrow{k_1} 3B$
$A \xrightarrow{k_2} 4C$
The ratio of the rate of production of $B$ to the rate of production of $C$ is:
(A) Independent of time
(B) Independent of temperature
(C) Dependent on $[A]_0$
(D) Both (A) and (C)

**Answer Key for Practice Questions:**
* **Q1.** (D) (Explanation: Mass is conserved so sum equals initial amount. Since it's a closed system, the sum of rates of changes is zero. And product distribution directly maps to rate constant ratios).
* **Q2.** (A) (Explanation: The slow step is the Rate Determining Step, corresponding strictly to the highest activation energy peak. Because Step 1 is endothermic, $B$ sits higher than $A$. The net evolution of heat dictates $D$ sits lower than $A$).
* **Q3.** (B) (Explanation: $\frac{d[C]}{dt} = \text{Rate of Formation} - \text{Rate of Disappearance}$. Formation is $2 \times k_1[A][B]$ due to the stoichiometric coefficient 2. Disappearance is $k_2[C][B] + k_3[C][A]$. So $-\frac{d[C]}{dt} = -(\text{Formation} - \text{Disappearance}) = -2k_1[A][B] + k_2[C][B] + k_3[C][A]$).
* **Q4.** (A) (Explanation: $\frac{d[B]}{dt} = 3k_1[A]$ and $\frac{d[C]}{dt} = 4k_2[A]$. Their ratio is $\frac{3k_1}{4k_2}$, which relies strictly on constants and cancels out $[A]$, making it completely independent of time).
