# 4. Collision Theory and Temperature Dependence

## 1. Key Concepts and Formulas

### Collision Theory Postulates
* **Fundamental Basis:** For a chemical reaction to occur and products to be formed, reactant molecules must collide with one another.
* **Effective Collisions:** Not every collision leads to the formation of a product. Only "effective" collisions lead to a successful chemical reaction.
* **Dual Barriers:** For collisions to be effective, colliding molecules must overcome two specific barriers:
  1. **Energy Barrier:** Colliding molecules must possess an energy greater than or equal to a minimum required amount, known as the *threshold energy*.
  2. **Orientation Barrier:** The molecules must collide with the correct spatial orientation.
* **Collision Theory Equation:** The rate of a reaction can be expressed mathematically considering both barriers:
  $$k = P \cdot Z_{AB} \cdot e^{-E_a/RT}$$
  * $Z_{AB} =$ Collision Frequency (the total number of collisions between reactants $A$ and $B$ per second per unit volume).
  * $e^{-E_a/RT} =$ Fraction of molecules possessing energy equal to or greater than the threshold energy ($E_a$).
  * $P =$ Probability Factor or Steric Factor. It accounts for the fact that in a collision, molecules must be properly oriented for a reaction to occur.

### Temperature Coefficient (T.C.)
* **Definition:** The Temperature Coefficient is roughly defined as the ratio of the rate constants of a reaction at two temperatures differing by $10^\circ\text{C}$ (e.g., $k_{T+10} / k_T$). For most reactions, this value lies between 2 and 3.
* **Scaling Formula:** When the temperature is increased by a larger interval $\Delta T$, the new rate constant ($k_{new}$) can be found using:
  $$k_{new} = k_{old} \times (T.C.)^{\frac{\Delta T}{10}}$$

### Arrhenius Equation and Activation Energy ($E_a$)
* **Equation:** The quantitative dependence of the rate constant on temperature is given by the Arrhenius equation:
  $$k = A \cdot e^{-E_a / RT}$$
  * $k =$ Rate constant
  * $A =$ Arrhenius factor, pre-exponential factor, or frequency factor
  * $E_a =$ Activation energy (the extra energy required to cross the energy barrier)
  * $R =$ Universal gas constant
  * $T =$ Absolute temperature in Kelvin
  * $e^{-E_a / RT} =$ The Boltzmann factor, representing the fraction of molecules having energy more than or equal to the threshold energy
* **Common Trap (Units of A):** The unit of the pre-exponential factor $A$ is identical to the unit of the rate constant $k$, which is $(\text{conc})^{1-n}(\text{time})^{-1}$.
* **Logarithmic Forms and Graphical Interpretation:**
  * **Natural logarithm:** $\ln k = \ln A - \frac{E_a}{RT}$. A plot of $\ln k$ versus $1/T$ yields a straight line with a slope of $-\frac{E_a}{R}$.
  * **Base-10 logarithm:** $\log k = \log A - \frac{E_a}{2.303RT}$. A plot of $\log k$ versus $1/T$ yields a straight line with a slope of $-\frac{E_a}{2.303R}$.
* **Two-Temperature Formula:** To find activation energy from rate constants at two different temperatures (assuming $A$ and $E_a$ are independent of temperature):
  $$\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R} \left[ \frac{1}{T_1} - \frac{1}{T_2} \right]$$
* **Enthalpy Change ($\Delta H$):** The enthalpy of reaction is the difference between the forward and backward activation energies: $\Delta H = (E_a)_f - (E_a)_b$.
  * If $\Delta H > 0$, the reaction is endothermic.
  * If $\Delta H < 0$, the reaction is exothermic.
* **Micro-Reversibility and Equilibrium:** The equilibrium constant ($K_{eq}$) is the ratio of the forward and backward rate constants:
  $$K_{eq} = \frac{k_f}{k_b} = \frac{A_f e^{-(E_a)_f/RT}}{A_b e^{-(E_a)_b/RT}}$$
  Using $\Delta H = (E_a)_f - (E_a)_b$, this leads to the van't Hoff equation relating the equilibrium constant to temperature and standard enthalpy change.

### Catalysts
* **Function:** A positive catalyst increases the reaction rate by providing an alternative pathway with a lower activation energy ($E_a' < E_a$).
* **Equal Rate Condition:** If a catalyzed reaction at temperature $T'$ operates at the same rate as the uncatalyzed reaction at temperature $T$, then:
  $$\frac{E_a}{T} = \frac{E_a'}{T'}$$
* **Key Insight:** A catalyst lowers the activation energy of both the forward and backward reactions by the exact same amount. Therefore, it does not alter the enthalpy change ($\Delta H$) or the overall thermodynamics of the reaction.

### Thermodynamic vs. Kinetic Stability
* **Kinetic Stability:** Governed by the activation energy ($E_a$). A high activation energy peak means the reaction is slow, rendering the reactant "kinetically stable". The step with the highest activation energy is the slowest step (Rate Determining Step).
* **Thermodynamic Stability:** Governed by the enthalpy ($\Delta H$). The species situated in the lowest potential energy well is the most thermodynamically stable.

---

## 2. Types of Questions/Problems that Can Be Asked
* **Rate Scaling using T.C.:** Given the Temperature Coefficient and an initial rate, calculating the new rate after a specific temperature increase (e.g., $30^\circ\text{C}$ to $60^\circ\text{C}$).
* **Graphical Analysis of Arrhenius Equation:** Extracting the activation energy ($E_a$) or frequency factor ($A$) from the slope and intercept of $\ln k$ vs. $1/T$ or $\log k$ vs. $1/T$ graphs.
* **Two-Temperature Arrhenius Calculations:** Calculating the activation energy when given rate constants at two different temperatures, or finding the temperature required to reach a specific rate constant.
* **Catalyzed vs. Uncatalyzed Rate Comparisons:** Equating rate constants to find the required temperature to achieve the same rate with a catalyst, or calculating the drop in activation energy.
* **Energy Profile Diagram Deductions:** Analyzing multi-step reaction mechanisms graphically to identify the slowest step (highest peak), fastest step (lowest peak), intermediates, and overall endothermic/exothermic nature.
* **Theoretical/Assertion-Reasoning:** Evaluating statements about whether activation energy depends on temperature, the units of Arrhenius parameters, or the effect of a catalyst on thermodynamic stability.

---

## 3. Example Questions with Step-by-Step Solutions

**Example 1: Scaling Rate using Temperature Coefficient**
*Question:* If the rate constant of a reaction at $30^\circ\text{C}$ is $a\text{ sec}^{-1}$, then find out the rate constant at $60^\circ\text{C}$. (Given: Temperature Coefficient = 2)
*Solution:*
* Identify the change in temperature ($\Delta T$): $60^\circ\text{C} - 30^\circ\text{C} = 30$
* Use the scaling formula: $k_{new} = k_{old} \times (T.C.)^{\frac{\Delta T}{10}}$
* Substitute the values: $k_{60^\circ\text{C}} = a \times (2)^{\frac{30}{10}} = a \times (2)^3$
* Calculate final value: $k_{60^\circ\text{C}} = 8a\text{ sec}^{-1}$

**Example 2: Arrhenius Equation Graph and Two-Temperature Form**
*Question:* For the reaction $aA + bB \rightarrow cC + dD$, the plot of $\log k$ vs $1/T$ is a straight line with a slope of $-10000\text{ K}$. The temperature at which the rate constant of the reaction is $10^{-4}\text{ s}^{-1}$ is _____ K. (Given: The rate constant of the reaction is $10^{-5}\text{ s}^{-1}$ at $500\text{ K}$)
*Solution:*
* Relate slope to $E_a$: For a $\log k$ vs $1/T$ plot, $\text{slope} = -\frac{E_a}{2.303R}$. Thus, $\frac{E_a}{2.303R} = 10000$.
* Set up the two-temperature equation: $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R} \left[ \frac{1}{T_1} - \frac{1}{T_2} \right]$
* Substitute known values ($k_1 = 10^{-5}$, $T_1 = 500\text{ K}$, $k_2 = 10^{-4}$, $T_2 = ?$):
  $\log\left(\frac{10^{-4}}{10^{-5}}\right) = 10000 \left[ \frac{1}{500} - \frac{1}{T_2} \right]$
* Simplify the log term: $\log(10) = 1$
* Solve for $T_2$: 
  $1 = 10000 \left[ \frac{1}{500} - \frac{1}{T_2} \right]$
  $0.0001 = 0.002 - \frac{1}{T_2}$
  $\frac{1}{T_2} = 0.002 - 0.0001 = 0.0019$
  $T_2 = \frac{1}{0.0019} \approx 526\text{ K}$

**Example 3: Comparing Catalyzed and Uncatalyzed Reactions**
*Question:* For a reaction $A \rightarrow \text{Product}$, it was found that $E_a$ is decreased by $30\text{ kJ/mol}$ in the presence of a catalyst. If the uncatalyzed reaction occurs at $700\text{ K}$ and the catalyzed reaction occurs at $500\text{ K}$ with the rate remaining unchanged, what is the activation energy for the catalyzed reaction? (Assume pre-exponential factor is the same)
*Solution:*
* Establish the condition for equal rate constants ($k_{cat} = k$): $\frac{E_a}{T_{uncat}} = \frac{E_a'}{T_{cat}}$
* Set up the relationship between activation energies: $E_a' = E_a - 30$
* Substitute values into the equality: $\frac{E_a}{700} = \frac{E_a - 30}{500}$
* Solve for $E_a$ (uncatalyzed): $5E_a = 7(E_a - 30) \implies 5E_a = 7E_a - 210 \implies 2E_a = 210 \implies E_a = 105\text{ kJ/mol}$
* Calculate $E_a'$ (catalyzed): $E_a' = 105 - 30 = 75\text{ kJ/mol}$

**Example 4: Interpreting Energy Profile Diagrams**
*Question:* Reactant $A$ converts to product $D$ through the given mechanism (with the net evolution of heat):
Step 1: $A \rightarrow B$ (slow; $\Delta H = \text{+ve}$)
Step 2: $B \rightarrow C$ (fast; $\Delta H = \text{-ve}$)
Step 3: $C \rightarrow D$ (fast; $\Delta H = \text{-ve}$)
Which energy profile diagram correctly represents this?
*Solution:*
* Overall Reaction: "Net evolution of heat" means the overall process is exothermic ($\Delta H_{net} < 0$). Therefore, the final product $D$ must be placed at a lower energy level than the initial reactant $A$.
* Step 1 ($A \rightarrow B$): This is the "slow" step, meaning it is the rate-determining step. It must have the highest activation energy peak. Also, $\Delta H$ is positive, so intermediate $B$ sits in an energy well higher than $A$.
* Step 2 and 3 ($B \rightarrow C$ and $C \rightarrow D$): These are "fast" steps, so their activation energy peaks must be significantly shorter than the first peak. Because both have a negative $\Delta H$, intermediate $C$ is lower in energy than $B$, and product $D$ is lower in energy than $C$.
* (In a multiple-choice setting, you would look for the graph matching these specific peak heights and well depths).

---

## 4. Practice Questions

**Q1.** The rate constant of a reaction increases by five times on an increase in temperature from $27^\circ\text{C}$ to $52^\circ\text{C}$. The value of activation energy in $\text{kJ mol}^{-1}$ is _______ (Rounded-off to the nearest integer). [Given: $R = 8.314\text{ J K}^{-1}\text{mol}^{-1}$]
(A) 52
(B) 216
(C) 105
(D) 30

**Q2.** Consider plots of $\log k$ vs $1/T$ for three different reactions (1, 2, and 3). Line 1 is the steepest, Line 2 is moderately steep, and Line 3 has the gentlest slope. The correct order of activation energies ($E_a$) of these reactions is:
(A) $E_{a1} > E_{a2} > E_{a3}$
(B) $E_{a2} > E_{a1} > E_{a3}$
(C) $E_{a3} > E_{a2} > E_{a1}$
(D) $E_{a1} = E_{a2} = E_{a3}$

**Q3.** Consider the following statements related to temperature dependence of rate constants. Identify the correct statements:
A. The Arrhenius equation holds true only for an elementary homogenous reaction.
B. The unit of A is the same as that of k in Arrhenius equation.
C. At a given temperature, a low activation energy means a fast reaction.
D. A and $E_a$ as used in Arrhenius equation depend on temperature.
Choose the correct answer from the options given below:
(A) A, C and D Only
(B) B, D and E Only
(C) B and C Only
(D) A and B Only

**Q4.** For $A_2 + B_2 \rightleftharpoons 2AB$, $E_a$ for forward and backward reactions are 180 and $200\text{ kJ mol}^{-1}$ respectively. If a catalyst lowers $E_a$ for both reactions by $100\text{ kJ mol}^{-1}$. Which of the following statements is correct?
(A) Catalyst does not alter the Gibbs energy change of a reaction.
(B) Catalyst can cause non-spontaneous reactions to occur.
(C) The enthalpy change for the reaction is $+20\text{ kJ mol}^{-1}$.
(D) The enthalpy change for the catalysed reaction is different from that of uncatalysed reaction.

**Answer Key for Practice Questions:**
* **Q1.** (A) 52 (Explanation: Use the two-temperature formula converting to Kelvin: $300\text{ K}$ and $325\text{ K}$. $\log(5) = \frac{E_a}{2.303 \times 8.314} \left[ \frac{1}{300} - \frac{1}{325} \right]$. Solving gives $E_a \approx 51.5\text{ kJ/mol}$, rounded to 52).
* **Q2.** (A) $E_{a1} > E_{a2} > E_{a3}$ (Explanation: The slope of $\log k$ vs $1/T$ is $-E_a / 2.303R$. A steeper slope corresponds directly to a larger magnitude of Activation Energy).
* **Q3.** (C) B and C Only (Explanation: Arrhenius applies to complex reactions as well (ruling out A). $A$ and $E_a$ are considered independent of temperature in this context (ruling out D). The unit of $A$ matches $k$, and low $E_a$ implies a higher fraction of effective collisions and thus a faster reaction).
* **Q4.** (A) Catalyst does not alter the Gibbs energy change of a reaction. (Explanation: A catalyst lowers the activation energy barrier for both the forward and backward paths simultaneously and equally, meaning thermodynamic properties like $\Delta H$ and $\Delta G$ remain completely unchanged).
