# 3. Experimental Monitoring of First Order Reactions

## 1. Key Concepts and Formulas
The experimental monitoring of first-order reactions involves tracking a measurable physical property (like pressure, volume, or optical rotation) that changes as the reaction progresses. Instead of explicitly finding concentrations, the standard first-order integrated rate equation $k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$ is adapted to substitute these physical properties directly.

### A. Gas Phase Reactions
* **Concept:** For reactions involving gases, progress is often monitored by measuring the total pressure of the system at constant volume.
* **Formula Derivation:** For a typical first-order reaction $A(g) \rightarrow B(g) + C(g)$, let the initial pressure of $A$ be $P_i$.
  * At $t=0$: Pressure of $A = P_i$, $B = 0$, $C = 0$. Total pressure $P_t = P_i$.
  * At time $t$: Pressure of $A = P_i - x$, $B = x$, $C = x$. Total pressure $P_t = (P_i - x) + x + x = P_i + x$.
  * Thus, $x = P_t - P_i$.
  * The partial pressure of the reactant $A$ at time $t$ is $P_A = P_i - x = P_i - (P_t - P_i) = 2P_i - P_t$.
* **Final Formula:** Substituting $P_i$ for initial concentration and $2P_i - P_t$ for concentration at time $t$ gives: 
  $$k = \frac{2.303}{t} \log\left(\frac{P_i}{2P_i - P_t}\right)$$
* **Alternative format using infinite time:** If $P_\infty$ is given instead of $P_i$, note that at $t=\infty$, $P_A = 0$, so $P_\infty = 2P_i$. The formula adapts to:
  $$k = \frac{1}{t} \ln\left[\frac{P_\infty}{2(P_\infty - P_t)}\right]$$

### B. Decomposition of Hydrogen Peroxide ($H_2O_2$)
* **Concept:** The decomposition $H_2O_2 \rightarrow H_2O + \frac{1}{2}O_2$ is monitored by taking out aliquots at different times and titrating them against potassium permanganate ($KMnO_4$). The volume of $KMnO_4$ consumed is directly proportional to the unreacted concentration of $H_2O_2$.
* **Formula:** 
  $$k = \frac{2.303}{t} \log\left(\frac{V_0}{V_t}\right)$$
  where $V_0$ is the volume of $KMnO_4$ consumed initially, and $V_t$ is the volume consumed at time $t$.
* **Alternative method:** Measuring the volume of $O_2$ gas collected. Here, $k = \frac{2.303}{t} \log\left(\frac{V_\infty}{V_\infty - V_t}\right)$.

### C. Hydrolysis of Esters
* **Concept:** The acid-catalyzed hydrolysis of an ester ($\text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O} \xrightarrow{H^+} \text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH}$) is monitored by titrating the reaction mixture against a base like NaOH. Since water is in vast excess, this is a pseudo-first-order reaction.
* **Formula Derivation:**
  * $V_0$ (volume of base at $t=0$) is proportional only to the constant catalyst concentration $[H^+]$.
  * $V_t$ (volume at time $t$) is proportional to $[H^+]$ plus the acetic acid formed ($x$).
  * $V_\infty$ (volume at $t=\infty$) is proportional to $[H^+]$ plus the maximum acetic acid formed ($a$).
  * Therefore, the initial ester amount $a \propto (V_\infty - V_0)$ and the remaining ester amount $(a - x) \propto (V_\infty - V_t)$.
* **Final Formula:** 
  $$k = \frac{2.303}{t} \log\left(\frac{V_\infty - V_0}{V_\infty - V_t}\right)$$
* **Trap:** The rate constant calculated here is the pseudo-first-order rate constant ($k_{app}$). The true third-order rate constant $k$ is related by $k_{app} = k[H^+][H_2O]$.

### D. Inversion of Cane Sugar (Sucrose)
* **Concept:** The hydrolysis of sucrose yields glucose and fructose ($\text{Sucrose} + \text{H}_2\text{O} \xrightarrow{H^+} \text{Glucose} + \text{Fructose}$). Sucrose and glucose are dextrorotatory (rotate plane-polarized light clockwise), while fructose is laevorotatory (anticlockwise). Because the laevo rotation of fructose is greater than the dextro rotation of glucose, the optical rotation of the solution shifts from dextro to laevo as the reaction proceeds (hence the term "inversion").
* **Formula:** 
  $$k = \frac{2.303}{t} \log\left(\frac{r_0 - r_\infty}{r_t - r_\infty}\right)$$
  where $r_0$, $r_t$, and $r_\infty$ are the angles of optical rotation at time zero, time $t$, and infinite time, respectively.

---

## 2. Types of Questions/Problems Asked
* **Deriving Rate Constants from Titration Data:** Students are provided with a data table containing time and corresponding titrant volumes (like $KMnO_4$ or NaOH) or optical rotation degrees. They must substitute these directly into the specific property formula to find the rate constant $k$.
* **Predicting Fractional Completion:** Utilizing gas pressure or titration volumes to determine how much time it takes to reach a certain percentage of completion (e.g., $t_{99.9\%}$).
* **Comparing Catalytic Strength (Pseudo-First Order):** Examining how the pseudo-first-order rate constant changes when the concentration or type of acid catalyst is changed (e.g., strong vs. weak acid, or monoprotic HCl vs. diprotic $H_2SO_4$).
* **Product Volume Calculations:** Giving a half-life and calculating the expected volume of gas (like $O_2$) evolved after a specified time limit, requiring an understanding of fractional completion.

---

## 3. Example Questions with Step-by-Step Solutions

**Example 1: Decomposition of Hydrogen Peroxide**
*Question:* The decomposition of $H_2O_2$ in an aqueous solution follows first-order kinetics. To decompose a definite volume of $H_2O_2$, the volume of $KMnO_4$ required at $t=0$ minutes is $25\text{ ml}$ and at $t=10$ minutes is $20\text{ ml}$. Calculate the rate constant $k$. (Given $\log 5 = 0.7$)
*Solution:*
* Identify the relevant experimental formula for $H_2O_2$ decomposition: $k = \frac{2.303}{t} \log\left(\frac{a}{a-x}\right) = \frac{2.303}{t} \log\left(\frac{V_0}{V_t}\right)$.
* Substitute the given values: $V_0 = 25\text{ ml}$, $V_t = 20\text{ ml}$, $t = 10\text{ minutes}$.
  $k = \frac{2.303}{10} \log\left(\frac{25}{20}\right) = \frac{2.303}{10} \log(1.25)$
* Notice that $\log(1.25) = \log(5/4) = \log 5 - \log 4$. Since $\log 4 \approx 0.602$ and $\log 5 = 0.7$, $\log(1.25) \approx 0.7 - 0.6 = 0.1$.
  $k = \frac{2.303 \times 0.1}{10} = 0.02303\text{ min}^{-1}$ (approximated to $0.023\text{ min}^{-1}$)

**Example 2: Gas Phase Reaction**
*Question:* The integrated rate law equation for a first-order gas phase reaction $A(g) \rightarrow B(g) + C(g)$ is given by which expression? (Assume $P_i$ is initial pressure and $P_t$ is total pressure at time $t$)
*Solution:*
* Write the reaction and map the pressures: $A(g) \rightarrow B(g) + C(g)$
* At $t=0$, $P_{total} = P_i$. Pressures of $B$ and $C$ are 0.
* At $t=t$, pressure of $A$ drops by $x$, so $P_A = P_i - x$. Pressures of $B$ and $C$ are $x$.
* The total pressure $P_t = (P_i - x) + x + x = P_i + x$. Therefore, $x = P_t - P_i$.
* Find the remaining pressure of reactant $A$: $P_A = P_i - x = P_i - (P_t - P_i) = 2P_i - P_t$.
* Substitute $P_i$ (initial amount) and $P_A$ (amount at time $t$) into the first-order rate law:
  $$k = \frac{2.303}{t} \log\left(\frac{P_i}{2P_i - P_t}\right)$$

**Example 3: Pseudo-First Order Reaction Dependence**
*Question:* The hydrolysis of an ester is carried out separately in $0.05\text{ M HCl}$ and $0.05\text{ M H}_2\text{SO}_4$. Which of the following is true for the first-order rate constant of the reaction?
(A) $k_{HCl} > k_{H_2SO_4}$
(B) $k_{HCl} < k_{H_2SO_4}$
(C) $k_{HCl} = k_{H_2SO_4}$
*Solution:*
* Recognize that ester hydrolysis is acid-catalyzed, and its pseudo-first-order rate constant $k_{app}$ depends directly on the concentration of $H^+$ ions: $\text{Rate} = k_{app}[\text{Ester}]$, where $k_{app} \propto [H^+]$.
* Calculate $[H^+]$ for $0.05\text{ M HCl}$: Since HCl is a strong monoprotic acid, $[H^+] = 0.05\text{ M}$.
* Calculate $[H^+]$ for $0.05\text{ M H}_2\text{SO}_4$: Since $H_2SO_4$ is a strong diprotic acid, it releases twice the amount of protons: $[H^+] = 2 \times 0.05\text{ M} = 0.1\text{ M}$.
* Compare the resulting rate constants: Because $0.1\text{ M} > 0.05\text{ M}$, the apparent rate constant in $H_2SO_4$ will be greater.
* *Answer:* (B) $k_{HCl} < k_{H_2SO_4}$.

**Example 4: Calculating Gas Volumes from Half-life**
*Question:* The half-life for the first-order decomposition of $H_2O_2$ is $30\text{ minutes}$. If the volume of $O_2$ collected is $100\text{ ml}$ after a long time (infinite time), then what is the volume of $O_2$ collected at the same temperature and pressure after $60\text{ minutes}$?
*Solution:*
* Identify the number of half-lives passed. Time $t = 60\text{ minutes}$, which is exactly 2 half-lives ($2 \times 30\text{ minutes}$).
* In a first-order reaction, after 2 half-lives, the reaction is 75% complete (or 3/4 of the reactant is consumed).
* The final volume of gas at infinite time ($V_\infty = 100\text{ ml}$) corresponds to 100% decomposition of $H_2O_2$.
* Therefore, the volume of $O_2$ collected after 75% decomposition will simply be 75% of the maximum possible volume.
* $V_t = 0.75 \times 100\text{ ml} = 75\text{ ml}$.

---

## 4. Practice Questions

**Q1.** The reaction $A(g) \rightarrow B(g) + C(g)$ is a first-order reaction. The reaction was started with reactant A only. The total pressure of the system at time $t$ is $P_t$ and at infinite time is $P_\infty$. Which of the following expressions is correct for the rate constant $k$?
(A) $k = \frac{1}{t} \ln\left(\frac{P_t}{2(P_\infty - P_t)}\right)$
(B) $k = \frac{1}{t} \ln\left(\frac{P_t}{P_\infty}\right)$
(C) $k = \frac{1}{t} \ln\left(\frac{P_\infty}{2(P_\infty - P_t)}\right)$
(D) $k = \frac{1}{t} \ln\left(\frac{P_\infty - P_t}{P_\infty}\right)$

**Q2.** In the inversion of cane sugar, $\text{Sucrose} \rightarrow \text{Glucose} + \text{Fructose}$, the reaction can be tracked via optical rotation. Initially, the solution is dextrorotatory, but it eventually becomes laevorotatory. What causes this change in direction?
(A) Sucrose and Glucose are laevorotatory.
(B) The laevo rotation of fructose is greater than the dextro rotation of glucose.
(C) The dextro rotation of glucose is greater than the laevo rotation of fructose.
(D) All formed products are laevorotatory.

**Q3.** In a pseudo-first-order hydrolysis of an ester in water, the following ester concentration data was obtained:
* At $t=0\text{ min}$, $[\text{Ester}] = 0.55\text{ M}$
* At $t=30\text{ min}$, $[\text{Ester}] = 0.31\text{ M}$
* At $t=60\text{ min}$, $[\text{Ester}] = 0.17\text{ M}$
Calculate the average rate of reaction between the time interval of 30 minutes to 60 minutes.
(A) $4.67 \times 10^{-3}\text{ M/min}$
(B) $1.98 \times 10^{-2}\text{ M/min}$
(C) $2.44 \times 10^{-3}\text{ M/min}$
(D) $8.00 \times 10^{-3}\text{ M/min}$

**Q4.** The thermal decomposition of $N_2O_5(g)$ at constant volume forms $2N_2O_4(g) + O_2(g)$. At $t=0$, total pressure is $0.6\text{ atm}$. The rate constant is given as $4.606 \times 10^{-2}\text{ s}^{-1}$. This implies the reaction can be modelled similarly to standard gas-phase monitoring equations. For $A(g) \rightarrow 2B(g) + C(g)$, how is the reactant pressure $P_A$ at time $t$ expressed in terms of total pressure $P_t$ and initial pressure $P_i$?
(A) $P_A = 2P_i - P_t$
(B) $P_A = \frac{3P_i - P_t}{2}$
(C) $P_A = P_t - P_i$
(D) $P_A = \frac{P_i - P_t}{2}$

**Answer Key for Practice Questions:**
* **Q1.** (C) (Explanation: At $t=\infty$, $P_\infty = 2P_i \implies P_i = P_\infty/2$. The remaining pressure of A at time $t$ is $2P_i - P_t = P_\infty - P_t$. Substituting these into $\ln(P_i/P_A)$ yields $\ln\left(\frac{P_\infty/2}{P_\infty - P_t}\right) = \ln\left(\frac{P_\infty}{2(P_\infty - P_t)}\right)$)
* **Q2.** (B)
* **Q3.** (A) (Explanation: Average rate $= -\frac{\Delta[\text{Ester}]}{\Delta t} = -\frac{0.17 - 0.31}{60 - 30} = \frac{0.14}{30} \approx 4.67 \times 10^{-3}\text{ M/min}$)
* **Q4.** (B) (Explanation: Initial $= P_i$. At time $t$, $P_A = P_i - x$. Products are $2x$ and $x$. $P_t = (P_i - x) + 2x + x = P_i + 2x \implies x = \frac{P_t - P_i}{2}$. Therefore, $P_A = P_i - \left(\frac{P_t - P_i}{2}\right) = \frac{3P_i - P_t}{2}$)
