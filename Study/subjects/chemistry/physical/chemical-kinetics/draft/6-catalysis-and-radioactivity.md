# 6. Catalysis and Radioactivity

## 1. Key Concepts and Formulas

### Catalysis in Chemical Kinetics
While the physical properties of surfaces are discussed in Surface Chemistry, the kinetic impact of catalysts is essential for JEE Advanced.
* **Homogeneous Catalysis:** The catalyst and the reactants are in the same phase (e.g., gases or solutions). Example: Oxidation of $SO_2$ to $SO_3$ with $NO(g)$ as a catalyst. The catalyst participates in the intermediate steps and is regenerated.
* **Heterogeneous Catalysis:** The catalyst is in a different phase from the reactants (usually a solid catalyst acting on gaseous or liquid reactants). 
  * *Mechanism:* Involves diffusion of reactants to the surface, adsorption, chemical reaction on the surface, desorption of products, and diffusion away.
* **Properties of Solid Catalysts:**
  * **Activity:** The ability of a catalyst to increase the rate of a chemical reaction. It depends largely on the strength of chemisorption (must be strong enough to bind, but not so strong that the product gets immobilized).
  * **Selectivity:** The ability of a catalyst to direct a reaction to yield a particular product. For example, $CO$ and $H_2$ can yield methane over Ni, but methanol over $Cu/ZnO-Cr_2O_3$.
* **Enzyme Catalysis (Michaelis-Menten Concept):** Enzymes are highly specific biological catalysts. The reaction follows the lock-and-key mechanism:
  $$E + S \rightleftharpoons ES \rightarrow E + P$$
  At low substrate concentrations, the reaction is first order w.r.t substrate. At high substrate concentrations (saturation), the reaction becomes zero order because all enzyme active sites are occupied.

### Radioactivity and First-Order Kinetics
All radioactive decay processes strictly follow first-order kinetics. JEE frequently tests first-order kinetics using the terminology of nuclear chemistry.
* **Decay Constant ($\lambda$):** Analogous to the chemical rate constant ($k$). The unit is $\text{time}^{-1}$.
* **Activity ($A$ or $R$):** The rate of radioactive decay ($-\frac{dN}{dt}$). Activity is directly proportional to the number of radioactive nuclei present: $A = \lambda N$.
* **Integrated Rate Law:** 
  $$\lambda = \frac{1}{t} \ln\left(\frac{N_0}{N_t}\right) \quad \text{or} \quad N_t = N_0 e^{-\lambda t}$$
  where $N_0$ is the initial number of nuclei, and $N_t$ is the number of un-decayed nuclei remaining at time $t$. This equation can also be written in terms of Activity: $A_t = A_0 e^{-\lambda t}$.
* **Half-Life ($t_{1/2}$):** The time required for half the radioactive nuclei to decay.
  $$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$$
* **Average Life ($t_{avg}$ or $\tau$):** The expected lifetime of a radioactive nucleus. It is the reciprocal of the decay constant.
  $$t_{avg} = \frac{1}{\lambda} = 1.44 \times t_{1/2}$$
* **Common Fractions:** The amount remaining after $n$ half-lives is $\frac{N_0}{2^n}$.

---

## 2. Types of Questions Asked
* **Homogeneous vs Heterogeneous Mechanisms:** Identifying the type of catalysis or explaining the kinetic steps of surface adsorption.
* **Enzyme Saturation Limits:** Questions testing the conceptual transition of enzyme catalysis from first-order (low substrate) to zero-order (high substrate).
* **Radioactive Dating (e.g., Carbon-14):** Calculating the age of a sample using $t = \frac{2.303}{\lambda} \log\left(\frac{N_0}{N_t}\right)$ where the decay constant is derived from the given half-life.
* **Simultaneous Decay (Parallel Reactions):** A radioactive nucleus decaying by two different modes (e.g., alpha and beta emission). The effective decay constant is $\lambda_{net} = \lambda_1 + \lambda_2$.
* **Activity Scaling:** Finding the time taken for the activity of a sample to drop to a certain fraction of its original activity.

---

## 3. Example Questions with Step-by-Step Solutions

**Example 1: Enzyme Catalysis Kinetics**
*Question:* For an enzyme-catalyzed reaction, how does the order of reaction change with an increase in substrate concentration?
*Solution:*
* At low substrate concentrations, many active sites on the enzyme are empty. The rate is directly proportional to the substrate concentration (First Order).
* As substrate concentration increases, more active sites are filled.
* At very high substrate concentrations, all enzyme active sites are fully saturated. Adding more substrate cannot increase the rate further. The rate becomes independent of substrate concentration (Zero Order).

**Example 2: Average Life and Half-Life**
*Question:* The half-life of a radioactive isotope is $10\text{ years}$. What is its average life?
*Solution:*
* The relationship between average life ($\tau$) and half-life ($t_{1/2}$) is $\tau = 1.44 \times t_{1/2}$.
* Substitute the given half-life: $\tau = 1.44 \times 10 = 14.4\text{ years}$.

**Example 3: Carbon Dating**
*Question:* A piece of wood from an archaeological excavation has a $^{14}\text{C}$ activity of $4.0\text{ disintegrations/min per gram}$. Fresh wood has an activity of $16.0\text{ disintegrations/min per gram}$. If the half-life of $^{14}\text{C}$ is $5730\text{ years}$, find the age of the wood.
*Solution:*
* Recognize that activity $A$ is proportional to $N$. So, $A_0 = 16.0$ and $A_t = 4.0$.
* Calculate the number of half-lives passed. The activity dropped from 16 to 8 (1 half-life), and from 8 to 4 (2 half-lives).
* Since exactly 2 half-lives have passed, the age is $2 \times t_{1/2}$.
* $\text{Age} = 2 \times 5730 = 11460\text{ years}$.

---

## 4. Practice Questions

**Q1.** Which of the following statements is INCORRECT regarding solid catalysts?
(A) The activity of a catalyst depends on the strength of chemisorption.
(B) Selectivity is the ability of a catalyst to direct a reaction to yield a specific product.
(C) A heterogeneous catalyst increases the activation energy of the reaction.
(D) Reactants diffuse to the surface of the catalyst before adsorbing.

**Q2.** The decay constant of a radioactive isotope is $\lambda$. The time required for the activity to drop to $1/e$ of its initial value is:
(A) $\ln 2 / \lambda$
(B) $\lambda / 2.303$
(C) $1 / \lambda$
(D) $2 / \lambda$

**Q3.** A radioactive sample decays through two competing pathways with decay constants $\lambda_1 = 10^{-3}\text{ s}^{-1}$ and $\lambda_2 = 2 \times 10^{-3}\text{ s}^{-1}$. What is the effective half-life of the sample?
(A) $693\text{ s}$
(B) $231\text{ s}$
(C) $346\text{ s}$
(D) $1000\text{ s}$

**Answer Key for Practice Questions:**
* **Q1.** (C) (Explanation: Catalysts function by *lowering* the activation energy, not increasing it).
* **Q2.** (C) (Explanation: From $A_t = A_0 e^{-\lambda t}$, we want $A_t / A_0 = 1/e = e^{-1}$. Thus $e^{-\lambda t} = e^{-1} \implies \lambda t = 1 \implies t = 1/\lambda$. This time is exactly the average life).
* **Q3.** (B) (Explanation: For competing (parallel) pathways, $\lambda_{net} = \lambda_1 + \lambda_2 = 3 \times 10^{-3}\text{ s}^{-1}$. The effective half-life is $t_{1/2} = \frac{0.693}{\lambda_{net}} = \frac{0.693}{3 \times 10^{-3}} = 231\text{ s}$).
