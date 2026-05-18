# Chapter 3: Nernst Equation & Its Applications - Research Draft

## 1. Concept Details & Minute Details


### The Core Idea
Standard electrode potentials are measured under standard conditions (1M concentration, 1 atm pressure). However, in real-world batteries and cells, concentrations change as the reaction proceeds. The **Nernst Equation** relates the cell potential at non-standard conditions ($E_{cell}$) to the standard cell potential ($E^\circ_{cell}$), temperature, and the reaction quotient ($Q$).

### The Nernst Equation
For a general reduction reaction: $M^{n+}(aq) + ne^- \rightarrow M(s)$
$E = E^\circ - \frac{RT}{nF} \ln \frac{[M]}{[M^{n+}]}$
At 298 K (25°C), substituting the values of R, T, and F:
**$E_{cell} = E^\circ_{cell} - \frac{0.0591}{n} \log_{10} Q$**

### Applications of Nernst Equation
1. **Calculation of $E_{cell}$**: Finding EMF of a cell at any given concentration.
2. **Equilibrium Constant ($K_c$)**: At equilibrium, $E_{cell} = 0$ (the battery is dead) and $Q = K_c$.
   $E^\circ_{cell} = \frac{0.0591}{n} \log_{10} K_c$
3. **Gibbs Free Energy ($\Delta G$)**: Maximum useful work done by a Galvanic cell.
   $\Delta_r G = -nFE_{cell}$
   $\Delta_r G^\circ = -nFE^\circ_{cell}$

### Minute but Important Details (Often Ignored)
1. **Solid/Liquid Activity:** The concentration of pure solids and pure liquids is taken as unity (1). If a gas is involved, its partial pressure in atm or bar is used.
2. **Value of 'n':** 'n' is the total number of moles of electrons transferred in the balanced overall cell reaction. If Anode gives 2e- and Cathode takes 3e-, the balanced equation transfers 6e-, so n=6.
3. **Concentration Cells:** A cell in which both electrodes are made of the same material but dipped in solutions of different concentrations. For such cells, $E^\circ_{cell} = 0$. Electrons flow from the less concentrated solution (Anode) to the more concentrated solution (Cathode). $E_{cell} = -\frac{0.0591}{n} \log \frac{C_1}{C_2}$ where $C_1$ (Anode) < $C_2$ (Cathode).
4. **Intensive vs Extensive:** Cell potential ($E$) is an intensive property (doesn't depend on stoichiometry multipliers). Gibbs Free Energy ($\Delta G$) is an extensive property. If you multiply a reaction by 2, $E^\circ$ remains the same, but $\Delta G^\circ$ doubles.

---
## 2. Question Types & Strategy

**Type 1: Calculating $E_{cell}$ at 298K**
*Strategy:* Find $E^\circ_{cell}$. Find $n$. Write the balanced equation to find $Q = \frac{[Product\ Ions]^{coeff}}{[Reactant\ Ions]^{coeff}}$. Apply the formula.

**Type 2: Calculating Equilibrium Constant ($K_c$)**
*Strategy:* Set $E_{cell} = 0$. Use $E^\circ_{cell} = \frac{0.0591}{n} \log K_c$. Be careful with antilog calculations.

**Type 3: Gibbs Free Energy ($\Delta G^\circ$)**
*Strategy:* Use $\Delta_r G^\circ = -nFE^\circ_{cell}$. Substitute $F = 96487 \approx 96500 C/mol$. The answer will be in Joules, convert to kJ if asked.

**Type 4: Concentration Cells**
*Strategy:* Identify it's a concentration cell. $E^\circ = 0$. The lower concentration is the anode, higher is cathode.

**Type 5: Finding unknown concentration**
*Strategy:* You are given $E_{cell}$ and $E^\circ_{cell}$. Work backward through the log to find the unknown concentration.

---
## 3. MCQ Mastery (40 Questions)

**Q1. For a Galvanic cell at equilibrium, which of the following is correct?<br>**

- <br>
(A) $E^\circ_{cell} = 0$, $\Delta G = 0$
- <br>
(B) $E_{cell} = 0$, $\Delta G = 0$
- <br>
(C)
 $E_{cell} = 0$, $\Delta G^\circ = 0$
- <br>
(D) $E^\circ_{cell} = 0$, $\Delta G^\circ = 0$

<details><summary>Solution</summary><b>Answer: <br>
(B) $E_{cell} = 0$, $\Delta G = 0$</b><br>At equilibrium, the cell stops working, so $E_{cell}$ becomes zero. Consequently, $\Delta G = -nFE_{cell} = 0$. $E^\circ_{cell}$ is a constant standard value.</details>


**Q2. In the Nernst equation for a metal electrode $M^{n+}/M$, if the concentration of $M^{n+}$ is increased, what happens to the electrode potential?<br>**

- <br>
(A) Becomes zero
- <br>
(B) Remains same
- <br>
(C)
 Increases
- <br>
(D) Decreases

<details><summary>Solution</summary><b>Answer: <br>
(C)
 Increases</b><br>Using $E = E^\circ - \frac{0.0591}{n} \log(1/[M^{n+}])$. If $[M^{n+}]$ increases, the log term decreases (becomes less negative or more positive), causing $E$ to increase.</details>


**Q3. Which of the following is an extensive property?<br>**

- <br>
(A) $\Delta_r G^\circ$
- <br>
(B) $E_{cell}$
- <br>
(C)
 Molar conductivity
- <br>
(D) $E^\circ_{cell}$

<details><summary>Solution</summary><b>Answer: <br>
(A) $\Delta_r G^\circ$</b><br>Gibbs free energy depends on the quantity of substance (stoichiometry). Cell potential is intensive.</details>


**Q4. For a concentration cell constructed with two hydrogen electrodes, the anode has $pH = 5$ and cathode has $pH = 3$. The EMF of the cell at 298 K is:**

- <br>
(A) -0.1182 V
- <br>
(B) 0.0295 V
- <br>
(C)
 0.1182 V
- <br>
(D) 0.0591 V

<details><summary>Solution</summary><b>Answer: <br>
(C)
 0.1182 V</b><br>Anode $[H^+] = 10^{-5}$, Cathode $[H^+] = 10^{-3}$. $E_{cell} = -0.0591 \log(10^{-5}/10^{-3}) = -0.0591 \log(10^{-2}) = 0.0591 \times 2 = 0.1182 V$.</details>


**Q5. To calculate $K_c$ using the Nernst equation, we require:**

- <br>
(A) Only $E^\circ_{cell}$ and $n$
- <br>
(B) Only temperature
- <br>
(C)
 Both $E_{cell}$ and $E^\circ_{cell}$
- <br>
(D) $E^\circ_{cell}$, $n$, and $T$

<details><summary>Solution</summary><b>Answer: <br>
(D) $E^\circ_{cell}$, $n$, and $T$</b><br>Formula is $E^\circ_{cell} = \frac{RT}{nF} \ln K_c$. At standard 298K, just $E^\circ_{cell}$ and $n$ are needed, but theoretically T is required if not at 298K. (Answer is C).</details>


**Q6. In a concentration cell made of two Ag electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Higher concentration
- <br>
(B) Zero concentration
- <br>
(C)
 Equal concentration
- <br>
(D) Lower concentration

<details><summary>Solution</summary><b>Answer: <br>
(D) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q7. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Mg(s)/Mg2+ and Zn2+/Zn(s)?<br>**

- <br>
(A) 2
- <br>
(B) Random 3
- <br>
(C)
 Random 2
- <br>
(D) 4

<details><summary>Solution</summary><b>Answer: <br>
(A) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 2, which is 2.</details>


**Q8. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Zn(s)/Zn2+ and Al3+/Al(s)?<br>**

- <br>
(A) 3
- <br>
(B) 6
- <br>
(C)
 5
- <br>
(D) 2

<details><summary>Solution</summary><b>Answer: <br>
(B) 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 3, which is 6.</details>


**Q9. For a hypothetical cell where n=2 and $E^\circ_{cell} = 1.0 V$, what is the standard Gibbs free energy change ($\Delta G^\circ$)?<br> (Given 1F = 96500 C)**

- <br>
(A) -193000.0 kJ/mol
- <br>
(B) 193.0 kJ/mol
- <br>
(C)
 -19300.0 kJ/mol
- <br>
(D) -193.0 kJ/mol

<details><summary>Solution</summary><b>Answer: <br>
(D) -193.0 kJ/mol</b><br>$\Delta G^\circ = -nFE^\circ_{cell} = -2 \times 96500 \times 1.0 = -193000.0 J/mol = -193.0 kJ/mol$.</details>


**Q10. In the Nernst equation for a cell where the reaction quotient $Q = 0.001$, what is the value of $\log Q$?<br>**

- <br>
(A) 1
- <br>
(B) -3
- <br>
(C)
 3
- <br>
(D) 0

<details><summary>Solution</summary><b>Answer: <br>
(B) -3</b><br>$\log_{10}(0.001) = -3$.</details>


**Q11. In the Nernst equation for a cell where the reaction quotient $Q = 0.001$, what is the value of $\log Q$?<br>**

- <br>
(A) 3
- <br>
(B) 0
- <br>
(C)
 1
- <br>
(D) -3

<details><summary>Solution</summary><b>Answer: <br>
(D) -3</b><br>$\log_{10}(0.001) = -3$.</details>


**Q12. In a concentration cell made of two Zn electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Equal concentration
- <br>
(B) Lower concentration
- <br>
(C)
 Higher concentration
- <br>
(D) Zero concentration

<details><summary>Solution</summary><b>Answer: <br>
(B) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q13. In the Nernst equation for a cell where the reaction quotient $Q = 0.001$, what is the value of $\log Q$?<br>**

- <br>
(A) 3
- <br>
(B) 0
- <br>
(C)
 -3
- <br>
(D) 1

<details><summary>Solution</summary><b>Answer: <br>
(C)
 -3</b><br>$\log_{10}(0.001) = -3$.</details>


**Q14. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Fe(s)/Fe2+ and Zn2+/Zn(s)?<br>**

- <br>
(A) Random 2
- <br>
(B) 2
- <br>
(C)
 Random 3
- <br>
(D) 4

<details><summary>Solution</summary><b>Answer: <br>
(B) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 2, which is 2.</details>


**Q15. In a concentration cell made of two Ag electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Zero concentration
- <br>
(B) Lower concentration
- <br>
(C)
 Equal concentration
- <br>
(D) Higher concentration

<details><summary>Solution</summary><b>Answer: <br>
(B) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q16. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Zn(s)/Zn2+ and Al3+/Al(s)?<br>**

- <br>
(A) 5
- <br>
(B) 2
- <br>
(C)
 3
- <br>
(D) 6

<details><summary>Solution</summary><b>Answer: <br>
(D) 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 3, which is 6.</details>


**Q17. In the Nernst equation for a cell where the reaction quotient $Q = 0.1$, what is the value of $\log Q$?<br>**

- <br>
(A) Random 3
- <br>
(B) 0
- <br>
(C)
 1
- <br>
(D) -1

<details><summary>Solution</summary><b>Answer: <br>
(D) -1</b><br>$\log_{10}(0.1) = -1$.</details>


**Q18. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ni(s)/Ni2+ and Al3+/Al(s)?<br>**

- <br>
(A) 3
- <br>
(B) 6
- <br>
(C)
 2
- <br>
(D) 5

<details><summary>Solution</summary><b>Answer: <br>
(B) 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 3, which is 6.</details>


**Q19. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Al(s)/Al3+ and Mg2+/Mg(s)?<br>**

- <br>
(A) 3
- <br>
(B) 2
- <br>
(C)
 6
- <br>
(D) 5

<details><summary>Solution</summary><b>Answer: <br>
(C)
 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 3 and 2, which is 6.</details>


**Q20. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Mg(s)/Mg2+ and Cu2+/Cu(s)?<br>**

- <br>
(A) 2
- <br>
(B) Random 3
- <br>
(C)
 4
- <br>
(D) Random 2

<details><summary>Solution</summary><b>Answer: <br>
(A) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 2, which is 2.</details>


**Q21. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Cu(s)/Cu2+ and Fe2+/Fe(s)?<br>**

- <br>
(A) 2
- <br>
(B) 4
- <br>
(C)
 Random 3
- <br>
(D) Random 2

<details><summary>Solution</summary><b>Answer: <br>
(A) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 2, which is 2.</details>


**Q22. For a hypothetical cell where n=3 and $E^\circ_{cell} = 1.0 V$, what is the standard Gibbs free energy change ($\Delta G^\circ$)?<br> (Given 1F = 96500 C)**

- <br>
(A) -289500.0 kJ/mol
- <br>
(B) -28950.0 kJ/mol
- <br>
(C)
 -289.5 kJ/mol
- <br>
(D) 289.5 kJ/mol

<details><summary>Solution</summary><b>Answer: <br>
(C)
 -289.5 kJ/mol</b><br>$\Delta G^\circ = -nFE^\circ_{cell} = -3 \times 96500 \times 1.0 = -289500.0 J/mol = -289.5 kJ/mol$.</details>


**Q23. In a concentration cell made of two Mg electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Higher concentration
- <br>
(B) Zero concentration
- <br>
(C)
 Lower concentration
- <br>
(D) Equal concentration

<details><summary>Solution</summary><b>Answer: <br>
(C)
 Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q24. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Cu(s)/Cu2+ and Fe2+/Fe(s)?<br>**

- <br>
(A) Random 2
- <br>
(B) 2
- <br>
(C)
 4
- <br>
(D) Random 3

<details><summary>Solution</summary><b>Answer: <br>
(B) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 2, which is 2.</details>


**Q25. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Cu(s)/Cu2+ and Al3+/Al(s)?<br>**

- <br>
(A) 2
- <br>
(B) 5
- <br>
(C)
 6
- <br>
(D) 3

<details><summary>Solution</summary><b>Answer: <br>
(C)
 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 3, which is 6.</details>


**Q26. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ag(s)/Ag1+ and Al3+/Al(s)?<br>**

- <br>
(A) 1
- <br>
(B) Random 3
- <br>
(C)
 3
- <br>
(D) 4

<details><summary>Solution</summary><b>Answer: <br>
(C)
 3</b><br>To balance the electrons, the half reactions must transfer the LCM of 1 and 3, which is 3.</details>


**Q27. In the Nernst equation for a cell where the reaction quotient $Q = 0.001$, what is the value of $\log Q$?<br>**

- <br>
(A) 1
- <br>
(B) 0
- <br>
(C)
 3
- <br>
(D) -3

<details><summary>Solution</summary><b>Answer: <br>
(D) -3</b><br>$\log_{10}(0.001) = -3$.</details>


**Q28. In a concentration cell made of two Ag electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Higher concentration
- <br>
(B) Equal concentration
- <br>
(C)
 Lower concentration
- <br>
(D) Zero concentration

<details><summary>Solution</summary><b>Answer: <br>
(C)
 Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q29. For a hypothetical cell where n=2 and $E^\circ_{cell} = 1.0 V$, what is the standard Gibbs free energy change ($\Delta G^\circ$)?<br> (Given 1F = 96500 C)**

- <br>
(A) -19300.0 kJ/mol
- <br>
(B) -193.0 kJ/mol
- <br>
(C)
 -193000.0 kJ/mol
- <br>
(D) 193.0 kJ/mol

<details><summary>Solution</summary><b>Answer: <br>
(B) -193.0 kJ/mol</b><br>$\Delta G^\circ = -nFE^\circ_{cell} = -2 \times 96500 \times 1.0 = -193000.0 J/mol = -193.0 kJ/mol$.</details>


**Q30. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ni(s)/Ni2+ and Ag1+/Ag(s)?<br>**

- <br>
(A) Random 3
- <br>
(B) 2
- <br>
(C)
 1
- <br>
(D) 3

<details><summary>Solution</summary><b>Answer: <br>
(B) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 1, which is 2.</details>


**Q31. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ni(s)/Ni2+ and Al3+/Al(s)?<br>**

- <br>
(A) 6
- <br>
(B) 5
- <br>
(C)
 3
- <br>
(D) 2

<details><summary>Solution</summary><b>Answer: <br>
(A) 6</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 3, which is 6.</details>


**Q32. In a concentration cell made of two Al electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Higher concentration
- <br>
(B) Lower concentration
- <br>
(C)
 Zero concentration
- <br>
(D) Equal concentration

<details><summary>Solution</summary><b>Answer: <br>
(B) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q33. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ag(s)/Ag1+ and Ni2+/Ni(s)?<br>**

- <br>
(A) 2
- <br>
(B) 1
- <br>
(C)
 Random 3
- <br>
(D) 3

<details><summary>Solution</summary><b>Answer: <br>
(A) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 1 and 2, which is 2.</details>


**Q34. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Cu(s)/Cu2+ and Ag1+/Ag(s)?<br>**

- <br>
(A) 1
- <br>
(B) 2
- <br>
(C)
 3
- <br>
(D) Random 3

<details><summary>Solution</summary><b>Answer: <br>
(B) 2</b><br>To balance the electrons, the half reactions must transfer the LCM of 2 and 1, which is 2.</details>


**Q35. In a concentration cell made of two Fe electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Equal concentration
- <br>
(B) Higher concentration
- <br>
(C)
 Lower concentration
- <br>
(D) Zero concentration

<details><summary>Solution</summary><b>Answer: <br>
(C)
 Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q36. In a concentration cell made of two Al electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Lower concentration
- <br>
(B) Higher concentration
- <br>
(C)
 Equal concentration
- <br>
(D) Zero concentration

<details><summary>Solution</summary><b>Answer: <br>
(A) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q37. What is the value of 'n' (number of electrons transferred) in the balanced cell reaction involving Ag(s)/Ag1+ and Al3+/Al(s)?<br>**

- <br>
(A) 4
- <br>
(B) 3
- <br>
(C)
 1
- <br>
(D) Random 3

<details><summary>Solution</summary><b>Answer: <br>
(B) 3</b><br>To balance the electrons, the half reactions must transfer the LCM of 1 and 3, which is 3.</details>


**Q38. In a concentration cell made of two Mg electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Lower concentration
- <br>
(B) Equal concentration
- <br>
(C)
 Zero concentration
- <br>
(D) Higher concentration

<details><summary>Solution</summary><b>Answer: <br>
(A) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


**Q39. For a hypothetical cell where n=2 and $E^\circ_{cell} = 1.0 V$, what is the standard Gibbs free energy change ($\Delta G^\circ$)?<br> (Given 1F = 96500 C)**

- <br>
(A) -193000.0 kJ/mol
- <br>
(B) -19300.0 kJ/mol
- <br>
(C)
 -193.0 kJ/mol
- <br>
(D) 193.0 kJ/mol

<details><summary>Solution</summary><b>Answer: <br>
(C)
 -193.0 kJ/mol</b><br>$\Delta G^\circ = -nFE^\circ_{cell} = -2 \times 96500 \times 1.0 = -193000.0 J/mol = -193.0 kJ/mol$.</details>


**Q40. In a concentration cell made of two Cu electrodes, the anode will be the electrode in the solution with:**

- <br>
(A) Zero concentration
- <br>
(B) Lower concentration
- <br>
(C)
 Higher concentration
- <br>
(D) Equal concentration

<details><summary>Solution</summary><b>Answer: <br>
(B) Lower concentration</b><br>To reach equilibrium, the cell tries to equalize the concentrations. It does this by oxidizing the metal in the less concentrated solution (Anode) to increase its concentration, and reducing the ions in the more concentrated solution (Cathode).</details>


--- 
## 4. Subjective & Numerical Mastery (100 Questions)

### Board Arsenal & JEE Foundations

**Q1.** For the cell reaction involving Fe and Ag, $E^\circ_{cell} = 1.24 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.24$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q2.** For the cell reaction involving Al and Fe, $E^\circ_{cell} = 1.22 V$ and $n = 6$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -6 \times 96500 \times 1.22$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q3.** Calculate the EMF of the following cell at 298 K:
$Al(s) | Al^3+ (0.026 M) || Ni^2+ (0.385 M) | Ni(s)$
Given: $E^\circ_{Al^3+/Al} = -1.66 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-1.66) = 1.41 V$
**2. $n$ value:** 6
**3. Nernst Eq:** $E_{cell} = 1.41 - \frac{0.0591}{6} \log \frac{[Al^3+]^{2}}{[Ni^2+]^{3}}$
Substitute $[Al^3+] = 0.026$ and $[Ni^2+] = 0.385$ and solve to get EMF.
</details>


**Q4.** Calculate the equilibrium constant ($K_c$) for the reaction between Al and Fe^2+ at 298 K. Given $E^\circ_{cell} = 1.22 V$ and $n = 6$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{6} \log K_c$
$\log K_c = \frac{1.22 \times 6}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q5.** Calculate the EMF of the following cell at 298 K:
$Fe(s) | Fe^2+ (0.062 M) || Ag^1+ (0.887 M) | Ag(s)$
Given: $E^\circ_{Fe^2+/Fe} = -0.44 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.44) = 1.24 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.24 - \frac{0.0591}{2} \log \frac{[Fe^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Fe^2+] = 0.062$ and $[Ag^1+] = 0.887$ and solve to get EMF.
</details>


**Q6.** Calculate the EMF of the concentration cell at 298 K:
$Fe(s) | Fe^2+ (0.027 M) || Fe^2+ (0.835 M) | Fe(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Fe^2+]_{anode}}{[Fe^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.027}{0.835}$.
Solve the log to get the positive EMF value.
</details>


**Q7.** Calculate the EMF of the following cell at 298 K:
$Mg(s) | Mg^2+ (0.058 M) || Ni^2+ (0.906 M) | Ni(s)$
Given: $E^\circ_{Mg^2+/Mg} = -2.36 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-2.36) = 2.11 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 2.11 - \frac{0.0591}{2} \log \frac{[Mg^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Mg^2+] = 0.058$ and $[Ni^2+] = 0.906$ and solve to get EMF.
</details>


**Q8.** For the cell reaction involving Mg and Cu, $E^\circ_{cell} = 2.70 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 2.70$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q9.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.026 M) || Al^3+ (0.798 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.026}{0.798}$.
Solve the log to get the positive EMF value.
</details>


**Q10.** For the cell reaction involving Zn and Ni, $E^\circ_{cell} = 0.51 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.51$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q11.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.093 M) || Mg^2+ (0.171 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.093}{0.171}$.
Solve the log to get the positive EMF value.
</details>


**Q12.** Calculate the EMF of the concentration cell at 298 K:
$Fe(s) | Fe^2+ (0.099 M) || Fe^2+ (0.535 M) | Fe(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Fe^2+]_{anode}}{[Fe^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.099}{0.535}$.
Solve the log to get the positive EMF value.
</details>


**Q13.** Calculate the EMF of the following cell at 298 K:
$Mg(s) | Mg^2+ (0.089 M) || Zn^2+ (0.315 M) | Zn(s)$
Given: $E^\circ_{Mg^2+/Mg} = -2.36 V$ and $E^\circ_{Zn^2+/Zn} = -0.76 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.76 - (-2.36) = 1.60 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.60 - \frac{0.0591}{2} \log \frac{[Mg^2+]^{1}}{[Zn^2+]^{1}}$
Substitute $[Mg^2+] = 0.089$ and $[Zn^2+] = 0.315$ and solve to get EMF.
</details>


**Q14.** Calculate the EMF of the following cell at 298 K:
$Mg(s) | Mg^2+ (0.079 M) || Ni^2+ (0.708 M) | Ni(s)$
Given: $E^\circ_{Mg^2+/Mg} = -2.36 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-2.36) = 2.11 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 2.11 - \frac{0.0591}{2} \log \frac{[Mg^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Mg^2+] = 0.079$ and $[Ni^2+] = 0.708$ and solve to get EMF.
</details>


**Q15.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.07 M) || Zn^2+ (0.422 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.07}{0.422}$.
Solve the log to get the positive EMF value.
</details>


**Q16.** For the cell reaction involving Al and Ag, $E^\circ_{cell} = 2.46 V$ and $n = 3$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -3 \times 96500 \times 2.46$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q17.** For the cell reaction involving Mg and Ni, $E^\circ_{cell} = 2.11 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 2.11$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q18.** Calculate the EMF of the concentration cell at 298 K:
$Ni(s) | Ni^2+ (0.097 M) || Ni^2+ (0.259 M) | Ni(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Ni^2+]_{anode}}{[Ni^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.097}{0.259}$.
Solve the log to get the positive EMF value.
</details>


**Q19.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Ag^1+ at 298 K. Given $E^\circ_{cell} = 1.56 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.56 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q20.** Calculate the EMF of the following cell at 298 K:
$Ni(s) | Ni^2+ (0.098 M) || Ag^1+ (0.961 M) | Ag(s)$
Given: $E^\circ_{Ni^2+/Ni} = -0.25 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.25) = 1.05 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.05 - \frac{0.0591}{2} \log \frac{[Ni^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Ni^2+] = 0.098$ and $[Ag^1+] = 0.961$ and solve to get EMF.
</details>


**Q21.** For the cell reaction involving Fe and Ni, $E^\circ_{cell} = 0.19 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.19$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q22.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Zn^2+ at 298 K. Given $E^\circ_{cell} = 1.60 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.60 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q23.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.045 M) || Cu^2+ (0.365 M) | Cu(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.76) = 1.10 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.10 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Zn^2+] = 0.045$ and $[Cu^2+] = 0.365$ and solve to get EMF.
</details>


**Q24.** Calculate the equilibrium constant ($K_c$) for the reaction between Cu and Ag^1+ at 298 K. Given $E^\circ_{cell} = 0.46 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.46 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q25.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.008 M) || Cu^2+ (0.864 M) | Cu(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.76) = 1.10 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.10 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Zn^2+] = 0.008$ and $[Cu^2+] = 0.864$ and solve to get EMF.
</details>


**Q26.** For the cell reaction involving Zn and Ag, $E^\circ_{cell} = 1.56 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.56$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q27.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.04 M) || Zn^2+ (0.495 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.04}{0.495}$.
Solve the log to get the positive EMF value.
</details>


**Q28.** Calculate the EMF of the following cell at 298 K:
$Fe(s) | Fe^2+ (0.048 M) || Ag^1+ (0.428 M) | Ag(s)$
Given: $E^\circ_{Fe^2+/Fe} = -0.44 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.44) = 1.24 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.24 - \frac{0.0591}{2} \log \frac{[Fe^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Fe^2+] = 0.048$ and $[Ag^1+] = 0.428$ and solve to get EMF.
</details>


**Q29.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.046 M) || Mg^2+ (0.742 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.046}{0.742}$.
Solve the log to get the positive EMF value.
</details>


**Q30.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Ni^2+ at 298 K. Given $E^\circ_{cell} = 0.51 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.51 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q31.** For the cell reaction involving Cu and Ag, $E^\circ_{cell} = 0.46 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.46$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q32.** Calculate the EMF of the following cell at 298 K:
$Mg(s) | Mg^2+ (0.065 M) || Ag^1+ (0.172 M) | Ag(s)$
Given: $E^\circ_{Mg^2+/Mg} = -2.36 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-2.36) = 3.16 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 3.16 - \frac{0.0591}{2} \log \frac{[Mg^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Mg^2+] = 0.065$ and $[Ag^1+] = 0.172$ and solve to get EMF.
</details>


**Q33.** Calculate the equilibrium constant ($K_c$) for the reaction between Ni and Ag^1+ at 298 K. Given $E^\circ_{cell} = 1.05 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.05 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q34.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Fe^2+ at 298 K. Given $E^\circ_{cell} = 1.92 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.92 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q35.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.056 M) || Mg^2+ (0.158 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.056}{0.158}$.
Solve the log to get the positive EMF value.
</details>


**Q36.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.047 M) || Cu^2+ (0.492 M) | Cu(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.76) = 1.10 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.10 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Zn^2+] = 0.047$ and $[Cu^2+] = 0.492$ and solve to get EMF.
</details>


**Q37.** Calculate the EMF of the following cell at 298 K:
$Al(s) | Al^3+ (0.048 M) || Zn^2+ (0.845 M) | Zn(s)$
Given: $E^\circ_{Al^3+/Al} = -1.66 V$ and $E^\circ_{Zn^2+/Zn} = -0.76 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.76 - (-1.66) = 0.90 V$
**2. $n$ value:** 6
**3. Nernst Eq:** $E_{cell} = 0.90 - \frac{0.0591}{6} \log \frac{[Al^3+]^{2}}{[Zn^2+]^{3}}$
Substitute $[Al^3+] = 0.048$ and $[Zn^2+] = 0.845$ and solve to get EMF.
</details>


**Q38.** Calculate the EMF of the concentration cell at 298 K:
$Ni(s) | Ni^2+ (0.032 M) || Ni^2+ (0.762 M) | Ni(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Ni^2+]_{anode}}{[Ni^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.032}{0.762}$.
Solve the log to get the positive EMF value.
</details>


**Q39.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.046 M) || Mg^2+ (0.471 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.046}{0.471}$.
Solve the log to get the positive EMF value.
</details>


**Q40.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.041 M) || Zn^2+ (0.308 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.041}{0.308}$.
Solve the log to get the positive EMF value.
</details>


**Q41.** For the cell reaction involving Zn and Ni, $E^\circ_{cell} = 0.51 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.51$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q42.** For the cell reaction involving Mg and Ag, $E^\circ_{cell} = 3.16 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 3.16$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q43.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.065 M) || Al^3+ (0.83 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.065}{0.83}$.
Solve the log to get the positive EMF value.
</details>


**Q44.** Calculate the EMF of the following cell at 298 K:
$Cu(s) | Cu^2+ (0.061 M) || Ag^1+ (0.686 M) | Ag(s)$
Given: $E^\circ_{Cu^2+/Cu} = 0.34 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (0.34) = 0.46 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.46 - \frac{0.0591}{2} \log \frac{[Cu^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Cu^2+] = 0.061$ and $[Ag^1+] = 0.686$ and solve to get EMF.
</details>


**Q45.** Calculate the EMF of the following cell at 298 K:
$Fe(s) | Fe^2+ (0.051 M) || Ni^2+ (0.673 M) | Ni(s)$
Given: $E^\circ_{Fe^2+/Fe} = -0.44 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-0.44) = 0.19 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.19 - \frac{0.0591}{2} \log \frac{[Fe^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Fe^2+] = 0.051$ and $[Ni^2+] = 0.673$ and solve to get EMF.
</details>


**Q46.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.01 M) || Mg^2+ (0.492 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.01}{0.492}$.
Solve the log to get the positive EMF value.
</details>


**Q47.** For the cell reaction involving Al and Cu, $E^\circ_{cell} = 2.00 V$ and $n = 6$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -6 \times 96500 \times 2.00$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q48.** For the cell reaction involving Al and Zn, $E^\circ_{cell} = 0.90 V$ and $n = 6$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -6 \times 96500 \times 0.90$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q49.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Fe^2+ at 298 K. Given $E^\circ_{cell} = 0.32 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.32 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q50.** Calculate the EMF of the following cell at 298 K:
$Al(s) | Al^3+ (0.024 M) || Cu^2+ (0.382 M) | Cu(s)$
Given: $E^\circ_{Al^3+/Al} = -1.66 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-1.66) = 2.00 V$
**2. $n$ value:** 6
**3. Nernst Eq:** $E_{cell} = 2.00 - \frac{0.0591}{6} \log \frac{[Al^3+]^{2}}{[Cu^2+]^{3}}$
Substitute $[Al^3+] = 0.024$ and $[Cu^2+] = 0.382$ and solve to get EMF.
</details>


**Q51.** For the cell reaction involving Fe and Ni, $E^\circ_{cell} = 0.19 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.19$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q52.** Calculate the equilibrium constant ($K_c$) for the reaction between Fe and Ag^1+ at 298 K. Given $E^\circ_{cell} = 1.24 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.24 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q53.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.096 M) || Al^3+ (0.49 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.096}{0.49}$.
Solve the log to get the positive EMF value.
</details>


**Q54.** For the cell reaction involving Zn and Ag, $E^\circ_{cell} = 1.56 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.56$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q55.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Cu^2+ at 298 K. Given $E^\circ_{cell} = 1.10 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.10 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q56.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Ag^1+ at 298 K. Given $E^\circ_{cell} = 3.16 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{3.16 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q57.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.009 M) || Ag^1+ (0.229 M) | Ag(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.76) = 1.56 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.56 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Zn^2+] = 0.009$ and $[Ag^1+] = 0.229$ and solve to get EMF.
</details>


**Q58.** Calculate the EMF of the following cell at 298 K:
$Fe(s) | Fe^2+ (0.077 M) || Cu^2+ (0.351 M) | Cu(s)$
Given: $E^\circ_{Fe^2+/Fe} = -0.44 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.44) = 0.78 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.78 - \frac{0.0591}{2} \log \frac{[Fe^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Fe^2+] = 0.077$ and $[Cu^2+] = 0.351$ and solve to get EMF.
</details>


**Q59.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Ag^1+ at 298 K. Given $E^\circ_{cell} = 1.56 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.56 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q60.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.09 M) || Al^3+ (0.487 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.09}{0.487}$.
Solve the log to get the positive EMF value.
</details>


**Q61.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.065 M) || Ni^2+ (0.236 M) | Ni(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-0.76) = 0.51 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.51 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Zn^2+] = 0.065$ and $[Ni^2+] = 0.236$ and solve to get EMF.
</details>


**Q62.** For the cell reaction involving Fe and Ag, $E^\circ_{cell} = 1.24 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.24$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q63.** Calculate the EMF of the following cell at 298 K:
$Ni(s) | Ni^2+ (0.051 M) || Cu^2+ (0.428 M) | Cu(s)$
Given: $E^\circ_{Ni^2+/Ni} = -0.25 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.25) = 0.59 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.59 - \frac{0.0591}{2} \log \frac{[Ni^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Ni^2+] = 0.051$ and $[Cu^2+] = 0.428$ and solve to get EMF.
</details>


**Q64.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Zn^2+ at 298 K. Given $E^\circ_{cell} = 1.60 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.60 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q65.** For the cell reaction involving Fe and Cu, $E^\circ_{cell} = 0.78 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.78$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q66.** For the cell reaction involving Ni and Cu, $E^\circ_{cell} = 0.59 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.59$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q67.** Calculate the EMF of the following cell at 298 K:
$Fe(s) | Fe^2+ (0.066 M) || Ni^2+ (0.877 M) | Ni(s)$
Given: $E^\circ_{Fe^2+/Fe} = -0.44 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-0.44) = 0.19 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.19 - \frac{0.0591}{2} \log \frac{[Fe^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Fe^2+] = 0.066$ and $[Ni^2+] = 0.877$ and solve to get EMF.
</details>


**Q68.** Calculate the EMF of the following cell at 298 K:
$Ni(s) | Ni^2+ (0.029 M) || Ag^1+ (0.6 M) | Ag(s)$
Given: $E^\circ_{Ni^2+/Ni} = -0.25 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.25) = 1.05 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.05 - \frac{0.0591}{2} \log \frac{[Ni^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Ni^2+] = 0.029$ and $[Ag^1+] = 0.6$ and solve to get EMF.
</details>


**Q69.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.06 M) || Mg^2+ (0.831 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.06}{0.831}$.
Solve the log to get the positive EMF value.
</details>


**Q70.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.007 M) || Al^3+ (0.493 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.007}{0.493}$.
Solve the log to get the positive EMF value.
</details>


**Q71.** For the cell reaction involving Ni and Ag, $E^\circ_{cell} = 1.05 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.05$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q72.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.039 M) || Zn^2+ (0.554 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.039}{0.554}$.
Solve the log to get the positive EMF value.
</details>


**Q73.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.041 M) || Al^3+ (0.183 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.041}{0.183}$.
Solve the log to get the positive EMF value.
</details>


**Q74.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Ni^2+ at 298 K. Given $E^\circ_{cell} = 2.11 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{2.11 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q75.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.074 M) || Ni^2+ (0.794 M) | Ni(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-0.76) = 0.51 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.51 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Zn^2+] = 0.074$ and $[Ni^2+] = 0.794$ and solve to get EMF.
</details>


**Q76.** For the cell reaction involving Al and Fe, $E^\circ_{cell} = 1.22 V$ and $n = 6$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -6 \times 96500 \times 1.22$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q77.** Calculate the equilibrium constant ($K_c$) for the reaction between Fe and Ni^2+ at 298 K. Given $E^\circ_{cell} = 0.19 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.19 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q78.** For the cell reaction involving Al and Fe, $E^\circ_{cell} = 1.22 V$ and $n = 6$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -6 \times 96500 \times 1.22$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q79.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Fe^2+ at 298 K. Given $E^\circ_{cell} = 1.92 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.92 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q80.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Ag^1+ at 298 K. Given $E^\circ_{cell} = 1.56 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{1.56 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q81.** Calculate the EMF of the following cell at 298 K:
$Al(s) | Al^3+ (0.022 M) || Ag^1+ (0.434 M) | Ag(s)$
Given: $E^\circ_{Al^3+/Al} = -1.66 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-1.66) = 2.46 V$
**2. $n$ value:** 3
**3. Nernst Eq:** $E_{cell} = 2.46 - \frac{0.0591}{3} \log \frac{[Al^3+]^{1}}{[Ag^1+]^{3}}$
Substitute $[Al^3+] = 0.022$ and $[Ag^1+] = 0.434$ and solve to get EMF.
</details>


**Q82.** For the cell reaction involving Mg and Zn, $E^\circ_{cell} = 1.60 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 1.60$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q83.** Calculate the equilibrium constant ($K_c$) for the reaction between Mg and Ni^2+ at 298 K. Given $E^\circ_{cell} = 2.11 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{2.11 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q84.** Calculate the EMF of the following cell at 298 K:
$Mg(s) | Mg^2+ (0.018 M) || Ag^1+ (0.703 M) | Ag(s)$
Given: $E^\circ_{Mg^2+/Mg} = -2.36 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-2.36) = 3.16 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 3.16 - \frac{0.0591}{2} \log \frac{[Mg^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Mg^2+] = 0.018$ and $[Ag^1+] = 0.703$ and solve to get EMF.
</details>


**Q85.** Calculate the equilibrium constant ($K_c$) for the reaction between Al and Zn^2+ at 298 K. Given $E^\circ_{cell} = 0.90 V$ and $n = 6$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{6} \log K_c$
$\log K_c = \frac{0.90 \times 6}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q86.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.095 M) || Al^3+ (0.572 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.095}{0.572}$.
Solve the log to get the positive EMF value.
</details>


**Q87.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.009 M) || Zn^2+ (0.545 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.009}{0.545}$.
Solve the log to get the positive EMF value.
</details>


**Q88.** Calculate the EMF of the following cell at 298 K:
$Ni(s) | Ni^2+ (0.003 M) || Cu^2+ (0.458 M) | Cu(s)$
Given: $E^\circ_{Ni^2+/Ni} = -0.25 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.25) = 0.59 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.59 - \frac{0.0591}{2} \log \frac{[Ni^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Ni^2+] = 0.003$ and $[Cu^2+] = 0.458$ and solve to get EMF.
</details>


**Q89.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.05 M) || Ni^2+ (0.949 M) | Ni(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Ni^2+/Ni} = -0.25 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.25 - (-0.76) = 0.51 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.51 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Ni^2+]^{1}}$
Substitute $[Zn^2+] = 0.05$ and $[Ni^2+] = 0.949$ and solve to get EMF.
</details>


**Q90.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.042 M) || Ag^1+ (0.269 M) | Ag(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Ag^1+/Ag} = 0.8 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.8 - (-0.76) = 1.56 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.56 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Ag^1+]^{2}}$
Substitute $[Zn^2+] = 0.042$ and $[Ag^1+] = 0.269$ and solve to get EMF.
</details>


**Q91.** For the cell reaction involving Fe and Ni, $E^\circ_{cell} = 0.19 V$ and $n = 2$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -2 \times 96500 \times 0.19$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q92.** Calculate the EMF of the concentration cell at 298 K:
$Zn(s) | Zn^2+ (0.015 M) || Zn^2+ (0.641 M) | Zn(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Zn^2+]_{anode}}{[Zn^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.015}{0.641}$.
Solve the log to get the positive EMF value.
</details>


**Q93.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.014 M) || Fe^2+ (0.398 M) | Fe(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Fe^2+/Fe} = -0.44 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.44 - (-0.76) = 0.32 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 0.32 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Fe^2+]^{1}}$
Substitute $[Zn^2+] = 0.014$ and $[Fe^2+] = 0.398$ and solve to get EMF.
</details>


**Q94.** Calculate the EMF of the following cell at 298 K:
$Al(s) | Al^3+ (0.035 M) || Zn^2+ (0.339 M) | Zn(s)$
Given: $E^\circ_{Al^3+/Al} = -1.66 V$ and $E^\circ_{Zn^2+/Zn} = -0.76 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = -0.76 - (-1.66) = 0.90 V$
**2. $n$ value:** 6
**3. Nernst Eq:** $E_{cell} = 0.90 - \frac{0.0591}{6} \log \frac{[Al^3+]^{2}}{[Zn^2+]^{3}}$
Substitute $[Al^3+] = 0.035$ and $[Zn^2+] = 0.339$ and solve to get EMF.
</details>


**Q95.** Calculate the equilibrium constant ($K_c$) for the reaction between Fe and Ni^2+ at 298 K. Given $E^\circ_{cell} = 0.19 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.19 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q96.** Calculate the EMF of the concentration cell at 298 K:
$Al(s) | Al^3+ (0.093 M) || Al^3+ (0.137 M) | Al(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{3} \log \frac{[Al^3+]_{anode}}{[Al^3+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{3} \log \frac{0.093}{0.137}$.
Solve the log to get the positive EMF value.
</details>


**Q97.** Calculate the EMF of the concentration cell at 298 K:
$Mg(s) | Mg^2+ (0.037 M) || Mg^2+ (0.348 M) | Mg(s)$

<details><summary>Solution</summary>
For a concentration cell, $E^\circ_{cell} = 0 V$.
$E_{cell} = -\frac{0.0591}{2} \log \frac{[Mg^2+]_{anode}}{[Mg^2+]_{cathode}}$
$E_{cell} = -\frac{0.0591}{2} \log \frac{0.037}{0.348}$.
Solve the log to get the positive EMF value.
</details>


**Q98.** Calculate the equilibrium constant ($K_c$) for the reaction between Zn and Ni^2+ at 298 K. Given $E^\circ_{cell} = 0.51 V$ and $n = 2$.

<details><summary>Solution</summary>
At equilibrium, $E_{cell} = 0$.
$E^\circ_{cell} = \frac{0.0591}{2} \log K_c$
$\log K_c = \frac{0.51 \times 2}{0.0591}$
Calculate the antilog to find $K_c$.
</details>


**Q99.** For the cell reaction involving Al and Ag, $E^\circ_{cell} = 2.46 V$ and $n = 3$. Calculate the standard Gibbs free energy change $\Delta_r G^\circ$. (1F = 96500 C/mol)

<details><summary>Solution</summary>
$\Delta_r G^\circ = -nFE^\circ_{cell}$
$\Delta_r G^\circ = -3 \times 96500 \times 2.46$
Multiply to get the answer in Joules/mol. Divide by 1000 for kJ/mol.
</details>


**Q100.** Calculate the EMF of the following cell at 298 K:
$Zn(s) | Zn^2+ (0.057 M) || Cu^2+ (0.345 M) | Cu(s)$
Given: $E^\circ_{Zn^2+/Zn} = -0.76 V$ and $E^\circ_{Cu^2+/Cu} = 0.34 V$.

<details><summary>Solution</summary>
**1. $E^\circ_{cell}$:** $E^\circ_{cathode} - E^\circ_{anode} = 0.34 - (-0.76) = 1.10 V$
**2. $n$ value:** 2
**3. Nernst Eq:** $E_{cell} = 1.10 - \frac{0.0591}{2} \log \frac{[Zn^2+]^{1}}{[Cu^2+]^{1}}$
Substitute $[Zn^2+] = 0.057$ and $[Cu^2+] = 0.345$ and solve to get EMF.
</details>

