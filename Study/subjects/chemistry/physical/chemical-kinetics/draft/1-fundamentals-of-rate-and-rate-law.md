# 1. Fundamentals of Rate and Rate Law

## 1. Key Concepts and Formulas

### Factors Affecting Rate of Reaction
* **Concentration:** Increasing the concentration of reactants increases the rate of reaction. This happens because the number of reactant molecules increases per unit volume, which subsequently increases the number of effective collisions.
* **Surface Area:** Increasing the surface area of the reactants increases the rate of reaction. This is particularly relevant for solid reactants or catalysts, where a finely divided or powdered form provides more area for collisions.
* **Temperature:** For most chemical reactions, the rate increases significantly with an increase in temperature. The Temperature Coefficient represents the ratio of rate constants at two temperatures differing by 10°C, typically lying between 2 and 3. Rising temperature increases the fraction of molecules possessing energy greater than or equal to the threshold energy.
* **Catalyst:** The addition of a positive catalyst provides an alternative pathway for the reaction with a lower activation energy ($E_a' < E_a$), thereby increasing the reaction rate without being consumed.

### Rate Law and Order of Reaction
* **Expressing Rate:** For a general reaction $aA + bB \rightarrow cC$, the Rate of Reaction (ROR) relates to the rates of disappearance of reactants and appearance of products divided by their stoichiometric coefficients: 
  $$ROR = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = \frac{1}{c}\frac{d[C]}{dt}$$
  *Trap:* Do not confuse the overall Rate of Reaction with the rate of disappearance (which is just $-\frac{d[A]}{dt}$) or the rate of appearance (which is just $\frac{d[C]}{dt}$).
* **Rate Law Equation:** An experimentally determined equation that relates the rate of reaction to the concentration of reactants. For $A + B \rightarrow \text{Product}$, the rate law is given by: 
  $$\text{Rate} = k[A]^a[B]^b$$
  where $k$ is the rate constant, $a$ is the order with respect to $A$, $b$ is the order with respect to $B$, and the overall order of the reaction is $n = a + b$.
* **Molecularity vs. Order:** For an elementary (single-step) reaction, the order is equal to its molecularity (the total number of reacting molecules). However, for multi-step (complex) reactions, there is no significance to overall molecularity; the overall order is strictly an experimentally determined value.
* **Reaction Mechanisms:** In a multi-step reaction, the slowest step is the rate-determining step. If the slow step contains an intermediate, its concentration must be replaced using the equilibrium constant ($K_{eq}$) from a preceding fast reversible step to find the final rate law.
* **Units of Rate Constant ($k$):** The unit of $k$ depends on the overall order ($n$) of the reaction and is determined by the formula: 
  $$\text{Unit of } k = (\text{mol L}^{-1})^{1-n} \text{ time}^{-1}$$
  * For zero-order ($n=0$): $\text{mol L}^{-1}\text{s}^{-1}$ or $\text{M s}^{-1}$
  * For first-order ($n=1$): $\text{s}^{-1}$

---

## 2. Types of Questions that Can Be Asked
* **Stoichiometric Rate Comparisons:** Given the rate of disappearance of one species, students must calculate the rate of appearance or disappearance of another species using the stoichiometric coefficients.
* **Deducing Order from Units:** Students are provided with the value and unit of a rate constant and must identify the overall order of the reaction purely from the units.
* **Initial Rate Method:** A data table with initial concentrations of reactants and initial rates is provided. Students must deduce the order with respect to each reactant and the overall rate law by observing how the rate scales when specific concentrations are doubled or halved.
* **Deriving Rate Laws from Mechanisms:** A multi-step reaction mechanism is given, usually comprising a fast equilibrium step and a slow step. Students must write the rate law based on the slow step and mathematically substitute any intermediate species.

---

## 3. Example Questions with Step-by-Step Solutions

**Example 1: Expressing Rates of Disappearance and Appearance**
*Question:* For the reaction $A \rightarrow B$, the concentration of reactant changes from $0.03\text{ M}$ to $0.02\text{ M}$ in $25\text{ minutes}$. Calculate the average rate of disappearance of $A$ and rate of reaction in $\text{M/minute}$ and $\text{M/second}$.
*Solution:*
* Rate in $\text{M/min}$: Rate of disappearance of $A = -\frac{\Delta[A]}{\Delta t} = -\left(\frac{0.02 - 0.03}{25}\right) = -\left(\frac{-0.01}{25}\right) = 4 \times 10^{-4}\text{ M/min}$
* Rate in $\text{M/sec}$: Convert time to seconds: $25\text{ min} \times 60\text{ sec/min} = 1500\text{ sec}$.
  $\text{Rate} = -\left(\frac{0.02 - 0.03}{1500}\right) = \frac{0.01}{1500} = 6.67 \times 10^{-6}\text{ M/sec}$

**Example 2: Determining Order from the Rate Constant Unit**
*Question:* For a reaction $3A \rightarrow \text{Product}$, the value of the rate constant is $3.5 \times 10^{-2}\text{ mol L}^{-1}\text{ sec}^{-1}$. Calculate the order of the reaction.
*Solution:*
* Use the general unit formula for rate constant: $(\text{mol L}^{-1})^{1-n} \text{ sec}^{-1}$.
* Equate it to the given unit: $(\text{mol L}^{-1})^{1-n} \text{ sec}^{-1} = \text{mol L}^{-1} \text{ sec}^{-1}$.
* Compare the powers: $1 - n = 1 \implies n = 0$.
* *Conclusion:* It is a zero-order reaction.

**Example 3: Deriving Rate Law from a Mechanism**
*Question:* The suggested mechanism for the reaction $\text{CHCl}_3(g) + \text{Cl}_2(g) \rightarrow \text{CCl}_4(g) + \text{HCl}(g)$ is:
* Step 1: $\text{Cl}_2 \rightleftharpoons 2\text{Cl}^\bullet$ (Fast, equilibrium constant $K_{eq} = k_1 / k_2$)
* Step 2: $\text{CHCl}_3 + \text{Cl}^\bullet \rightarrow \text{HCl} + \text{CCl}_3^\bullet$ (Slow, rate constant $k_3$)
* Step 3: $\text{CCl}_3^\bullet + \text{Cl}^\bullet \rightarrow \text{CCl}_4$ (Fast, rate constant $k_4$)
Find the rate law and overall order.
*Solution:*
* The rate of the reaction is determined by the slow step: $\text{Rate} = k_3[\text{CHCl}_3][\text{Cl}^\bullet]$
* Since $[\text{Cl}^\bullet]$ is an intermediate, find its value from the fast equilibrium step:
  $K_{eq} = \frac{[\text{Cl}^\bullet]^2}{[\text{Cl}_2]} = \frac{k_1}{k_2}$
  $[\text{Cl}^\bullet] = \left(\frac{k_1}{k_2}\right)^{1/2} [\text{Cl}_2]^{1/2}$
* Substitute $[\text{Cl}^\bullet]$ into the rate expression:
  $\text{Rate} = k_3 \left(\frac{k_1}{k_2}\right)^{1/2} [\text{CHCl}_3][\text{Cl}_2]^{1/2}$
* Combine constants into an overall rate constant ($k_{net}$):
  $\text{Rate} = k_{net}[\text{CHCl}_3]^1[\text{Cl}_2]^{1/2}$
* *Conclusion:* The overall order is $1 + 1/2 = 3/2$.

**Example 4: Order from Experimental Data**
*Question:* For a reaction $A + 2B \rightarrow 2C$, the following data was collected:
* Exp 1: $[A]=0.30\text{ M}, [B]=0.30\text{ M}, \text{Rate} = 0.10$
* Exp 2: $[A]=0.30\text{ M}, [B]=0.60\text{ M}, \text{Rate} = 0.40$
* Exp 3: $[A]=0.60\text{ M}, [B]=0.30\text{ M}, \text{Rate} = 0.20$
Find the rate law.
*Solution:*
* Assume $\text{Rate} = k[A]^x[B]^y$.
* Compare Exp 1 and 2: $[A]$ is constant, $[B]$ doubles ($0.30 \rightarrow 0.60$). The rate increases by 4 times ($0.10 \rightarrow 0.40$). Thus, $2^y = 4 \implies y = 2$.
* Compare Exp 1 and 3: $[B]$ is constant, $[A]$ doubles ($0.30 \rightarrow 0.60$). The rate increases by 2 times ($0.10 \rightarrow 0.20$). Thus, $2^x = 2 \implies x = 1$.
* *Conclusion:* The rate law is $\text{Rate} = k[A]^1[B]^2$.

---

## 4. Practice Questions

**Q1.** For the reaction $\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3$, how is the rate expressed in terms of disappearance and appearance of species?
(A) $\frac{d[\text{N}_2]}{3dt} = \frac{d[\text{H}_2]}{2dt} = \frac{d[\text{NH}_3]}{dt}$
(B) $-\frac{d[\text{N}_2]}{dt} = \frac{1}{3}\frac{d[\text{H}_2]}{dt} = \frac{1}{2}\frac{d[\text{NH}_3]}{dt}$
(C) $-\frac{d[\text{N}_2]}{dt} = -\frac{1}{3}\frac{d[\text{H}_2]}{dt} = \frac{1}{2}\frac{d[\text{NH}_3]}{dt}$
(D) $-\frac{d[\text{N}_2]}{dt} = -\frac{d[\text{H}_2]}{dt} = \frac{d[\text{NH}_3]}{dt}$

**Q2.** Units of rate constant of first and zero order reactions in terms of molarity (M) unit are, respectively:
(A) $\text{s}^{-1}, \text{M s}^{-1}$
(B) $\text{s}^{-1}, \text{M}$
(C) $\text{M s}^{-1}, \text{s}^{-1}$
(D) $\text{M}, \text{s}^{-1}$

**Q3.** The velocity of a reaction is doubled for every $10^\circ\text{C}$ rise in temperature. If the temperature is raised from $10^\circ\text{C}$ to $50^\circ\text{C}$, the reaction velocity increases by about:
(A) 12 times
(B) 16 times
(C) 32 times
(D) 50 times

**Q4.** Calculate the order of the reaction with respect to A and B from the following data:
| [A] ($\text{mol L}^{-1}$) | [B] ($\text{mol L}^{-1}$) | Rate ($\text{mol L}^{-1} \text{s}^{-1}$) |
| :--- | :--- | :--- |
| 0.05 | 0.05 | $1.2 \times 10^{-3}$ |
| 0.10 | 0.05 | $2.4 \times 10^{-3}$ |
| 0.05 | 0.10 | $1.2 \times 10^{-3}$ |
(A) 1 and 0
(B) 1 and 1
(C) 0 and 1
(D) None of these

**Answer Key for Practice Questions:**
* **Q1.** (C)
* **Q2.** (A) (The correct standard units matching first and zero order respectively are $\text{s}^{-1}$ and $\text{M s}^{-1}$).
* **Q3.** (B)
* **Q4.** (A)
