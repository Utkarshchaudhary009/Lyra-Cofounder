# 2. Reaction Orders and Integrated Rate Laws

## 1. Key Concepts and Formulas

### Zero Order Reactions
* **Definition:** Reactions where the rate is independent of the reactant concentration. A zero-order reaction is never an elementary (single-step) reaction.
* **Differential Rate Law:** $-\frac{d[A]}{dt} = k[A]^0 = k$
* **Integrated Rate Law:** $[A]_0 - [A]_t = kt$, where $[A]_0$ is the initial concentration and $[A]_t$ is the concentration at time $t$.
* **Half-Life ($t_{1/2}$):** The time required for half of the reactant to be consumed. $t_{1/2} = \frac{[A]_0}{2k}$. Notice that the half-life is directly proportional to the initial concentration ($t_{1/2} \propto [A]_0$).
* **100% Completion Time:** $t_{100\%} = \frac{[A]_0}{k}$. Notably, $t_{100\%} = 2 \times t_{50\%}$.
* **Graphical Representations:**
  * $[A]_t$ vs $t$: A straight line with a negative slope equal to $-k$ and a y-intercept of $[A]_0$.
  * Rate vs time: A horizontal line parallel to the time axis.
  * $t_{1/2}$ vs $[A]_0$: A straight line passing through the origin with a slope of $\frac{1}{2k}$.
* **Examples:** Photochemical reactions (rate $\propto$ intensity of light) and decomposition of ammonia on a platinum surface.

### First Order Reactions
* **Differential Rate Law:** $-\frac{d[A]}{dt} = k[A]^1$
* **Integrated Rate Law:** $kt = \ln\left(\frac{[A]_0}{[A]_t}\right)$ or converting to base-10 logarithm, $k = \frac{2.303}{t} \log\left(\frac{[A]_0}{[A]_t}\right)$.
* **Exponential Form:** $[A]_t = [A]_0 e^{-kt}$.
* **Half-Life ($t_{1/2}$):** $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{k}$.
  * *Common Trap:* The half-life of a first-order reaction is entirely independent of the initial concentration.
* **Important Fractional Times:**
  * $t_{75\%} = 2 \times t_{50\%}$
  * $t_{87.5\%} = 3 \times t_{50\%}$
  * $t_{99.9\%} \approx 10 \times t_{50\%}$
* **Amount Remaining:** The concentration remaining after $n$ half-lives is given by $C_t = \frac{C_0}{2^n}$.
* **Graphical Representations:**
  * $\ln[A]_t$ vs $t$: A straight line with slope $-k$ and y-intercept $\ln[A]_0$.
  * $\log[A]_t$ vs $t$: A straight line with slope $-\frac{k}{2.303}$.

### Pseudo-First Order Reactions
* **Definition:** Reactions that are not truly of the first order but, under certain conditions, behave as first-order reactions. This typically happens when one of the reacting molecules is present in such large excess that its concentration remains essentially constant throughout the reaction.
* **Mechanism:** For a bimolecular reaction $A + B \rightarrow \text{Products}$ with rate $= k[A][B]$, if $[B] \gg [A]$, then $[B]$ is practically constant. The rate law becomes $\text{Rate} = k'[A]$, where $k' = k[B]$. The reaction exhibits first-order kinetics with an apparent (pseudo) rate constant $k'$.
* **Common Examples:**
  * **Hydrolysis of Esters:** $\text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O} \xrightarrow{H^+} \text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH}$. Here, water is the solvent and is in vast excess.
  * **Inversion of Cane Sugar (Sucrose):** $\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \xrightarrow{H^+} \text{C}_6\text{H}_{12}\text{O}_6 + \text{C}_6\text{H}_{12}\text{O}_6$. Again, water concentration is constant.

### Second and Third Order Reactions
* **Second Order Integrated Law:** $kt = \frac{1}{[A]_t} - \frac{1}{[A]_0}$
* **Second Order Half-Life:** $t_{1/2} = \frac{1}{k[A]_0}$
* **Third Order Integrated Law:** $kt = \frac{1}{2} \left[ \frac{1}{[A]_t^2} - \frac{1}{[A]_0^2} \right]$
* **Third Order Half-Life:** $t_{1/2} = \frac{3}{2k[A]_0^2}$

### General $n$-th Order Kinetics ($n \neq 1$)
* **Integrated Law:** $kt = \frac{1}{n-1} \left[ \frac{1}{[A]_t^{n-1}} - \frac{1}{[A]_0^{n-1}} \right]$
* **Half-Life Dependence:** $t_{1/2} \propto \frac{1}{[A]_0^{n-1}}$

---

## 2. Types of Questions Asked
* **Fractional Completion Comparisons:** Students are often asked to relate the time it takes to complete different percentages of a reaction (e.g., proving that $t_{99.9\%} = 10 \times t_{50\%}$ for first order).
* **Gas Phase Kinetics:** Utilizing total pressure and initial pressure to find the rate constant. Students must map stoichiometry to pressure changes over time.
* **Optical Rotation and Titration Data:** Calculating the first-order rate constant given volume of titrant consumed or angle of optical rotation at initial time, time $t$, and infinite time.
* **Graphical Interpretation:** Identifying the order of a reaction by analyzing the axes of a linear graph (e.g., recognizing that a linear plot of $1/[A]$ vs $t$ means second order, or a horizontal $t_{1/2}$ vs $[A]_0$ means first order).
* **General Order Computations:** Using the relationship $t_{1/2} \propto a^{1-n}$ to deduce the specific fractional or integer order of a reaction from a set of half-lives at different initial concentrations.

---

## 3. Specific Example Questions with Solutions

**Example 1: Calculating Remaining Concentration (Zero Order)**
*Question:* A zero-order reaction has an initial concentration of $0.6\text{ M}$. The rate constant $k$ for the reaction is $0.2\text{ M/s}$. How much time will it take for the concentration of the reactant to decrease to $0.2\text{ M}$?
*Solution:*
* Recall the integrated rate equation for a zero-order reaction: $[A]_0 - [A]_t = kt$
* Identify the given values: Initial concentration $[A]_0 = 0.6\text{ M}$, final concentration $[A]_t = 0.2\text{ M}$, and $k = 0.2\text{ M/s}$
* Substitute into the equation: $0.6 - 0.2 = 0.2 \times t$
* Solve for $t$: $0.4 = 0.2t \implies t = 2\text{ seconds}$

**Example 2: First Order Fractional Completion Relationships**
*Question:* For the first order reaction $A \rightarrow B$, the half life is $30\text{ minutes}$. Time taken for 75% completion is?
*Solution:*
* Recognize the standard relationship for first-order kinetics: the time taken for 75% completion ($t_{75\%}$ or $t_{3/4}$) is exactly twice the half-life ($t_{50\%}$ or $t_{1/2}$).
* Write the relationship: $t_{75\%} = 2 \times t_{1/2}$
* Substitute the given half-life: $t_{75\%} = 2 \times 30\text{ minutes}$
* Calculate the final answer: $60\text{ minutes}$

**Example 3: Gas Phase First Order Kinetics**
*Question:* Integrated rate law equation for a first order gas phase reaction $A(g) \rightarrow B(g) + C(g)$ is given by (where $P_i$ is initial pressure and $P_t$ is total pressure at time $t$).
*Solution:*
* Set up the stoichiometry at time $t=0$: Initial pressure of $A$ is $P_i$. Products $B$ and $C$ are 0.
* Set up the stoichiometry at time $t$: Pressure of $A$ decreases by $x$, so $P_A = P_i - x$. Pressures of $B$ and $C$ increase by $x$, so $P_B = x$ and $P_C = x$.
* Express total pressure ($P_t$): $P_t = (P_i - x) + x + x = P_i + x$.
* Solve for $x$ in terms of measurable quantities: $x = P_t - P_i$.
* Substitute $x$ back into the expression for $P_A$: $P_A = P_i - (P_t - P_i) = 2P_i - P_t$.
* Use the standard first-order integrated rate law: $k = \frac{2.303}{t} \log\left(\frac{P_0}{P_t}\right)$. Replace with pressures of $A$: 
  $$k = \frac{2.303}{t} \log\left(\frac{P_i}{2P_i - P_t}\right)$$

**Example 4: Deduce Order from Half-Life Relationship**
*Question:* $t_{1/2}$ of a reaction $A \rightarrow \text{Product}$ (order = $\frac{3}{2}$) is represented by $t_{1/2} \propto \frac{1}{[A_0]^m}$. The value of $m$ is?
*Solution:*
* Recall the general formula relating half-life to initial concentration for an $n$-th order reaction: $t_{1/2} \propto \frac{1}{[A]_0^{n-1}}$
* By comparing the given relation $t_{1/2} \propto \frac{1}{[A_0]^m}$ to the standard formula, we can establish that $m = n - 1$.
* Substitute the given reaction order $n = 3/2$ into the equation: $m = 3/2 - 1$.
* Simplify the fraction: $m = 0.5$.

---

## 4. Practice Questions

**Q1.** The half-life of a first order reaction is $10\text{ min}$. If initial amount is $0.08\text{ mol L}^{-1}$ and concentration at some instant is $0.01\text{ mol L}^{-1}$, then $t$ is:
(A) $10\text{ min}$ (B) $30\text{ min}$ (C) $20\text{ min}$ (D) $40\text{ min}$

**Q2.** Time required to decompose half of the substance for $n$-th order reaction is inversely proportional to:
(A) $a^{n+1}$ (B) $a^{n-1}$ (C) $a^{n-2}$ (D) $a^n$

**Q3.** What is the order of the reaction which obeys the expression $t_{1/2} = \frac{1}{k a}$?
(A) Zero (B) Third (C) First (D) Second

**Q4.** A graph plotted between $\log t_{50\%}$ vs $\log a$ is a straight horizontal line parallel to the x-axis. What conclusion can you draw from the given graph?
(A) $n=1, t_{1/2} = \frac{k}{a}$
(B) $n=2, t_{1/2} = \frac{1}{a}$
(C) $n=1, t_{1/2} = \frac{0.693}{k}$
(D) None of these

**Answer Key for Practice Questions:**
* **Q1.** (B) (Explanation: $0.08 \rightarrow 0.04 \rightarrow 0.02 \rightarrow 0.01$ takes 3 half-lives. $3 \times 10 = 30\text{ min}$.)
* **Q2.** (B)
* **Q3.** (D)
* **Q4.** (C) (Explanation: A horizontal line indicates $t_{1/2}$ is completely independent of initial concentration $a$, which is the defining hallmark of a 1st order reaction.)
