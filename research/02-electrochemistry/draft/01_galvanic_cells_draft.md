# Chapter 1: Electrochemical Cells & Galvanic Cells - Research Draft

## 1. Concept Details & Minute Details


### The Core Idea
An electrochemical cell is a device capable of either generating electrical energy from chemical reactions (Galvanic/Voltaic cells) or using electrical energy to cause chemical reactions (Electrolytic cells). A Galvanic cell specifically uses spontaneous redox reactions to generate electricity.

### Daniell Cell
- **Anode (Oxidation):** Zinc rod in ZnSO4 solution. (Negative polarity)
- **Cathode (Reduction):** Copper rod in CuSO4 solution. (Positive polarity)
- **Direction of Flow:** Electrons flow from Anode (Zn) to Cathode (Cu) in the external circuit. Conventional current flows from Cu to Zn.

### Minute but Important Details (Often Ignored)
1. **Liquid Junction Potential (LJP):** When two solutions of different concentrations or different electrolytes are in contact, a potential difference develops at the junction due to the difference in mobilities of positive and negative ions. A salt bridge minimizes LJP.
2. **Choice of Salt Bridge Electrolyte:** The electrolyte in the salt bridge (e.g., KCl, KNO3, NH4NO3) must have cations and anions with almost equal ionic mobilities (transport numbers) to prevent the buildup of a new liquid junction potential.
3. **Agar-Agar / Gelatin:** These are used to form a semi-solid paste with the electrolyte so it doesn't mix mechanically with the half-cell solutions while allowing ion flow.
4. **When NOT to use KCl:** If one of the half-cells contains ions like Ag+, Pb2+, or Hg22+, KCl cannot be used in the salt bridge because Cl- will precipitate them as AgCl, PbCl2, or Hg2Cl2, clogging the porous plug.
5. **Opposing External Potential (E_ext):**
   - If E_ext < E_cell: Cell acts normally as a Galvanic cell.
   - If E_ext = E_cell: No current flows, chemical reaction stops (equilibrium).
   - If E_ext > E_cell: Current flows in reverse, the cell functions as an Electrolytic cell (non-spontaneous reaction is forced).
6. **IUPAC Cell Notation Rules:**
   - Anode (oxidation) is written on the left, Cathode (reduction) on the right. (Trick: ABC = Anode Bridge Cathode or LOAN = Left Oxidation Anode Negative).
   - A single vertical line `|` represents a phase boundary.
   - A double vertical line `||` represents the salt bridge.
   - Concentrations or partial pressures are enclosed in parentheses next to the species.
   - Inert electrodes (like Pt or C) are included at the extreme ends if gases or aqueous ions (without a solid metal) are involved.

---
## 2. Question Types & Strategy

**Type 1: Identifying Anode, Cathode, and Direction of Flow**
*Strategy:* Look at the overall reaction. The species undergoing oxidation (increase in oxidation number) is the Anode. The species undergoing reduction is the Cathode. Electrons always flow Anode -> Cathode.

**Type 2: Translating Chemical Reaction to Cell Notation**
*Strategy:* Split into half-reactions. Left side: Anode solid | Anode ion. Right side: Cathode ion | Cathode solid.

**Type 3: Translating Cell Notation to Chemical Reaction**
*Strategy:* Reverse of Type 2. Ensure electrons balance before adding half-reactions.

**Type 4: Salt Bridge & Concept Intricacies**
*Strategy:* Remember the precipitation rules (Ag+, Pb2+) and the mobility rule (mobility of cation = mobility of anion).

**Type 5: Effect of External Potential**
*Strategy:* Compare E_ext with E_cell.

---
## 3. MCQ Mastery (40 Questions)

**Q1. Which of the following electrolytes is NOT suitable for a salt bridge in a cell containing silver electrode?**

- (A) NH4NO3
- (B) KCl
- (C) NaNO3
- (D) KNO3

<details><summary>Solution</summary><b>Answer: (B) KCl</b><br>Cl- ions will precipitate Ag+ as AgCl at the electrode, stopping the cell operation.</details>


**Q2. The primary function of a salt bridge is to:**

- (A) Complete the circuit and maintain electrical neutrality while minimizing liquid junction potential
- (B) Complete the electrical circuit only
- (C) Maintain electrical neutrality in half-cells only
- (D) Increase the EMF of the cell

<details><summary>Solution</summary><b>Answer: (A) Complete the circuit and maintain electrical neutrality while minimizing liquid junction potential</b><br>It prevents charge accumulation which would otherwise quickly stop the current.</details>


**Q3. Agar-agar is used in a salt bridge because:**

- (A) It increases the mobility of the ions
- (B) It is a strong electrolyte
- (C) It reacts with the cell ions to produce electricity
- (D) It prevents mechanical mixing of the two half-cell solutions while allowing ion migration

<details><summary>Solution</summary><b>Answer: (D) It prevents mechanical mixing of the two half-cell solutions while allowing ion migration</b><br>Agar-agar forms a porous gel.</details>


**Q4. For an electrolyte to be used in a salt bridge, the transport numbers of its cation and anion should be:**

- (A) Exactly zero
- (B) Almost equal
- (C) Widely different
- (D) Dependent on the external temperature

<details><summary>Solution</summary><b>Answer: (B) Almost equal</b><br>Equal mobilities prevent the formation of a liquid junction potential inside the salt bridge.</details>


**Q5. If an external potential ($E_{ext}$) applied to a Daniell cell ($E_{cell} = 1.1 V$) is exactly $1.1 V$, what happens?**

- (A) Current flows from Cu to Zn
- (B) The cell becomes an electrolytic cell
- (C) Electrons flow from Cu to Zn
- (D) No current flows and the chemical reaction stops

<details><summary>Solution</summary><b>Answer: (D) No current flows and the chemical reaction stops</b><br>When external opposing potential equals cell potential, equilibrium is reached.</details>


**Q6. If an external potential ($E_{ext} = 1.5 V$) is applied to a Daniell cell ($E_{cell} = 1.1 V$), the zinc electrode acts as:**

- (A) Cathode where oxidation occurs
- (B) Cathode where reduction occurs
- (C) Anode where oxidation occurs
- (D) Anode where reduction occurs

<details><summary>Solution</summary><b>Answer: (B) Cathode where reduction occurs</b><br>Since $E_{ext} > E_{cell}$, the cell reverses. Zn2+ gets reduced to Zn at the zinc electrode, making it the cathode of the now electrolytic cell.</details>


**Q7. In the cell representation $Pt(s) | H_2(g) | H^+(aq) || Cu^{2+}(aq) | Cu(s)$, the left side electrode is:**

- (A) Platinum electrode acting as Cathode
- (B) Standard Hydrogen Electrode acting as Anode
- (C) Copper electrode acting as Anode
- (D) Standard Hydrogen Electrode acting as Cathode

<details><summary>Solution</summary><b>Answer: (B) Standard Hydrogen Electrode acting as Anode</b><br>By IUPAC convention, the left half is always the anode (oxidation).</details>


**Q8. In a Galvanic cell, the Anode is:**

- (A) Positive and reduction occurs here
- (B) Negative and oxidation occurs here
- (C) Positive and oxidation occurs here
- (D) Negative and reduction occurs here

<details><summary>Solution</summary><b>Answer: (B) Negative and oxidation occurs here</b><br>LOAN: Left, Oxidation, Anode, Negative.</details>


**Q9. Identify the overall reaction for the cell: Zn(s) | Zn2+(aq) || Ag+(aq) | Ag(s)**

- (A) Zn2+(aq) + Ag+(aq) -> Zn(s) + Ag(s)
- (B) Zn(s) + Ag(s) -> Zn2+(aq) + Ag+(aq)
- (C) Zn(s) + Ag+(aq) -> Zn2+(aq) + Ag(s)
- (D) Ag(s) + Zn2+(aq) -> Ag+(aq) + Zn(s)

<details><summary>Solution</summary><b>Answer: (C) Zn(s) + Ag+(aq) -> Zn2+(aq) + Ag(s)</b><br>Left side is oxidized (Zn -> Zn2+ + e-). Right side is reduced (Ag+ + e- -> Ag).</details>


**Q10. In a Galvanic cell represented by Cu(s) | Cu2+(aq) || Pb2+(aq) | Pb(s), what is the direction of electron flow in the external circuit?**

- (A) From Pb2+ to Cu2+
- (B) From Pb to Cu
- (C) From Cu to Pb
- (D) From Cu2+ to Pb2+

<details><summary>Solution</summary><b>Answer: (C) From Cu to Pb</b><br>Electrons always flow from Anode (Cu) to Cathode (Pb) in the external circuit.</details>


**Q11. What is the correct cell representation for the reaction: Mg(s) + Pb2+(aq) -> Mg2+(aq) + Pb(s) ?**

- (A) Mg(s) | Mg2+(aq) || Pb2+(aq) | Pb(s)
- (B) Mg(s) || Mg2+(aq) | Pb2+(aq) || Pb(s)
- (C) Pb(s) | Pb2+(aq) || Mg2+(aq) | Mg(s)
- (D) Mg(s) | Pb2+(aq) || Mg2+(aq) | Pb(s)

<details><summary>Solution</summary><b>Answer: (A) Mg(s) | Mg2+(aq) || Pb2+(aq) | Pb(s)</b><br>Mg is oxidized to Mg2+ (Anode). Pb2+ is reduced to Pb (Cathode). Anode is on the left.</details>


**Q12. What is the correct cell representation for the reaction: Ag(s) + Pb2+(aq) -> Ag+(aq) + Pb(s) ?**

- (A) Ag(s) | Ag+(aq) || Pb2+(aq) | Pb(s)
- (B) Pb(s) | Pb2+(aq) || Ag+(aq) | Ag(s)
- (C) Ag(s) || Ag+(aq) | Pb2+(aq) || Pb(s)
- (D) Ag(s) | Pb2+(aq) || Ag+(aq) | Pb(s)

<details><summary>Solution</summary><b>Answer: (A) Ag(s) | Ag+(aq) || Pb2+(aq) | Pb(s)</b><br>Ag is oxidized to Ag+ (Anode). Pb2+ is reduced to Pb (Cathode). Anode is on the left.</details>


**Q13. Identify the overall reaction for the cell: Mg(s) | Mg2+(aq) || Cu2+(aq) | Cu(s)**

- (A) Mg(s) + Cu(s) -> Mg2+(aq) + Cu2+(aq)
- (B) Cu(s) + Mg2+(aq) -> Cu2+(aq) + Mg(s)
- (C) Mg2+(aq) + Cu2+(aq) -> Mg(s) + Cu(s)
- (D) Mg(s) + Cu2+(aq) -> Mg2+(aq) + Cu(s)

<details><summary>Solution</summary><b>Answer: (D) Mg(s) + Cu2+(aq) -> Mg2+(aq) + Cu(s)</b><br>Left side is oxidized (Mg -> Mg2+ + e-). Right side is reduced (Cu2+ + e- -> Cu).</details>


**Q14. Identify the overall reaction for the cell: Sn(s) | Sn2+(aq) || Mg2+(aq) | Mg(s)**

- (A) Mg(s) + Sn2+(aq) -> Mg2+(aq) + Sn(s)
- (B) Sn(s) + Mg(s) -> Sn2+(aq) + Mg2+(aq)
- (C) Sn2+(aq) + Mg2+(aq) -> Sn(s) + Mg(s)
- (D) Sn(s) + Mg2+(aq) -> Sn2+(aq) + Mg(s)

<details><summary>Solution</summary><b>Answer: (D) Sn(s) + Mg2+(aq) -> Sn2+(aq) + Mg(s)</b><br>Left side is oxidized (Sn -> Sn2+ + e-). Right side is reduced (Mg2+ + e- -> Mg).</details>


**Q15. In a Galvanic cell represented by Ni(s) | Ni2+(aq) || Mg2+(aq) | Mg(s), what is the direction of electron flow in the external circuit?**

- (A) From Mg2+ to Ni2+
- (B) From Mg to Ni
- (C) From Ni2+ to Mg2+
- (D) From Ni to Mg

<details><summary>Solution</summary><b>Answer: (D) From Ni to Mg</b><br>Electrons always flow from Anode (Ni) to Cathode (Mg) in the external circuit.</details>


**Q16. Identify the overall reaction for the cell: Zn(s) | Zn2+(aq) || Fe2+(aq) | Fe(s)**

- (A) Zn(s) + Fe2+(aq) -> Zn2+(aq) + Fe(s)
- (B) Zn2+(aq) + Fe2+(aq) -> Zn(s) + Fe(s)
- (C) Fe(s) + Zn2+(aq) -> Fe2+(aq) + Zn(s)
- (D) Zn(s) + Fe(s) -> Zn2+(aq) + Fe2+(aq)

<details><summary>Solution</summary><b>Answer: (A) Zn(s) + Fe2+(aq) -> Zn2+(aq) + Fe(s)</b><br>Left side is oxidized (Zn -> Zn2+ + e-). Right side is reduced (Fe2+ + e- -> Fe).</details>


**Q17. If the salt bridge is suddenly removed from the Fe-Al galvanic cell, what happens to the cell voltage?**

- (A) It increases significantly
- (B) It slowly decreases to zero
- (C) It immediately drops to zero
- (D) It remains unchanged

<details><summary>Solution</summary><b>Answer: (C) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q18. Identify the overall reaction for the cell: Sn(s) | Sn2+(aq) || Zn2+(aq) | Zn(s)**

- (A) Sn2+(aq) + Zn2+(aq) -> Sn(s) + Zn(s)
- (B) Zn(s) + Sn2+(aq) -> Zn2+(aq) + Sn(s)
- (C) Sn(s) + Zn(s) -> Sn2+(aq) + Zn2+(aq)
- (D) Sn(s) + Zn2+(aq) -> Sn2+(aq) + Zn(s)

<details><summary>Solution</summary><b>Answer: (D) Sn(s) + Zn2+(aq) -> Sn2+(aq) + Zn(s)</b><br>Left side is oxidized (Sn -> Sn2+ + e-). Right side is reduced (Zn2+ + e- -> Zn).</details>


**Q19. If the salt bridge is suddenly removed from the Ag-Cu galvanic cell, what happens to the cell voltage?**

- (A) It increases significantly
- (B) It slowly decreases to zero
- (C) It remains unchanged
- (D) It immediately drops to zero

<details><summary>Solution</summary><b>Answer: (D) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q20. What is the correct cell representation for the reaction: Fe(s) + Al3+(aq) -> Fe2+(aq) + Al(s) ?**

- (A) Al(s) | Al3+(aq) || Fe2+(aq) | Fe(s)
- (B) Fe(s) | Fe2+(aq) || Al3+(aq) | Al(s)
- (C) Fe(s) || Fe2+(aq) | Al3+(aq) || Al(s)
- (D) Fe(s) | Al3+(aq) || Fe2+(aq) | Al(s)

<details><summary>Solution</summary><b>Answer: (B) Fe(s) | Fe2+(aq) || Al3+(aq) | Al(s)</b><br>Fe is oxidized to Fe2+ (Anode). Al3+ is reduced to Al (Cathode). Anode is on the left.</details>


**Q21. If the salt bridge is suddenly removed from the Cu-Sn galvanic cell, what happens to the cell voltage?**

- (A) It remains unchanged
- (B) It immediately drops to zero
- (C) It slowly decreases to zero
- (D) It increases significantly

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q22. Identify the overall reaction for the cell: Ni(s) | Ni2+(aq) || Sn2+(aq) | Sn(s)**

- (A) Ni2+(aq) + Sn2+(aq) -> Ni(s) + Sn(s)
- (B) Sn(s) + Ni2+(aq) -> Sn2+(aq) + Ni(s)
- (C) Ni(s) + Sn2+(aq) -> Ni2+(aq) + Sn(s)
- (D) Ni(s) + Sn(s) -> Ni2+(aq) + Sn2+(aq)

<details><summary>Solution</summary><b>Answer: (C) Ni(s) + Sn2+(aq) -> Ni2+(aq) + Sn(s)</b><br>Left side is oxidized (Ni -> Ni2+ + e-). Right side is reduced (Sn2+ + e- -> Sn).</details>


**Q23. What is the correct cell representation for the reaction: Sn(s) + Cu2+(aq) -> Sn2+(aq) + Cu(s) ?**

- (A) Cu(s) | Cu2+(aq) || Sn2+(aq) | Sn(s)
- (B) Sn(s) | Cu2+(aq) || Sn2+(aq) | Cu(s)
- (C) Sn(s) || Sn2+(aq) | Cu2+(aq) || Cu(s)
- (D) Sn(s) | Sn2+(aq) || Cu2+(aq) | Cu(s)

<details><summary>Solution</summary><b>Answer: (D) Sn(s) | Sn2+(aq) || Cu2+(aq) | Cu(s)</b><br>Sn is oxidized to Sn2+ (Anode). Cu2+ is reduced to Cu (Cathode). Anode is on the left.</details>


**Q24. If the salt bridge is suddenly removed from the Al-Cd galvanic cell, what happens to the cell voltage?**

- (A) It remains unchanged
- (B) It immediately drops to zero
- (C) It increases significantly
- (D) It slowly decreases to zero

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q25. What is the correct cell representation for the reaction: Cd(s) + Sn2+(aq) -> Cd2+(aq) + Sn(s) ?**

- (A) Sn(s) | Sn2+(aq) || Cd2+(aq) | Cd(s)
- (B) Cd(s) || Cd2+(aq) | Sn2+(aq) || Sn(s)
- (C) Cd(s) | Cd2+(aq) || Sn2+(aq) | Sn(s)
- (D) Cd(s) | Sn2+(aq) || Cd2+(aq) | Sn(s)

<details><summary>Solution</summary><b>Answer: (C) Cd(s) | Cd2+(aq) || Sn2+(aq) | Sn(s)</b><br>Cd is oxidized to Cd2+ (Anode). Sn2+ is reduced to Sn (Cathode). Anode is on the left.</details>


**Q26. If the salt bridge is suddenly removed from the Ni-Cu galvanic cell, what happens to the cell voltage?**

- (A) It slowly decreases to zero
- (B) It immediately drops to zero
- (C) It remains unchanged
- (D) It increases significantly

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q27. Identify the overall reaction for the cell: Pb(s) | Pb2+(aq) || Cd2+(aq) | Cd(s)**

- (A) Pb(s) + Cd2+(aq) -> Pb2+(aq) + Cd(s)
- (B) Pb(s) + Cd(s) -> Pb2+(aq) + Cd2+(aq)
- (C) Pb2+(aq) + Cd2+(aq) -> Pb(s) + Cd(s)
- (D) Cd(s) + Pb2+(aq) -> Cd2+(aq) + Pb(s)

<details><summary>Solution</summary><b>Answer: (A) Pb(s) + Cd2+(aq) -> Pb2+(aq) + Cd(s)</b><br>Left side is oxidized (Pb -> Pb2+ + e-). Right side is reduced (Cd2+ + e- -> Cd).</details>


**Q28. What is the correct cell representation for the reaction: Pb(s) + Cu2+(aq) -> Pb2+(aq) + Cu(s) ?**

- (A) Pb(s) || Pb2+(aq) | Cu2+(aq) || Cu(s)
- (B) Pb(s) | Cu2+(aq) || Pb2+(aq) | Cu(s)
- (C) Cu(s) | Cu2+(aq) || Pb2+(aq) | Pb(s)
- (D) Pb(s) | Pb2+(aq) || Cu2+(aq) | Cu(s)

<details><summary>Solution</summary><b>Answer: (D) Pb(s) | Pb2+(aq) || Cu2+(aq) | Cu(s)</b><br>Pb is oxidized to Pb2+ (Anode). Cu2+ is reduced to Cu (Cathode). Anode is on the left.</details>


**Q29. Identify the overall reaction for the cell: Ag(s) | Ag+(aq) || Mg2+(aq) | Mg(s)**

- (A) Ag(s) + Mg(s) -> Ag+(aq) + Mg2+(aq)
- (B) Mg(s) + Ag+(aq) -> Mg2+(aq) + Ag(s)
- (C) Ag+(aq) + Mg2+(aq) -> Ag(s) + Mg(s)
- (D) Ag(s) + Mg2+(aq) -> Ag+(aq) + Mg(s)

<details><summary>Solution</summary><b>Answer: (D) Ag(s) + Mg2+(aq) -> Ag+(aq) + Mg(s)</b><br>Left side is oxidized (Ag -> Ag+ + e-). Right side is reduced (Mg2+ + e- -> Mg).</details>


**Q30. Identify the overall reaction for the cell: Pb(s) | Pb2+(aq) || Sn2+(aq) | Sn(s)**

- (A) Pb(s) + Sn(s) -> Pb2+(aq) + Sn2+(aq)
- (B) Pb2+(aq) + Sn2+(aq) -> Pb(s) + Sn(s)
- (C) Sn(s) + Pb2+(aq) -> Sn2+(aq) + Pb(s)
- (D) Pb(s) + Sn2+(aq) -> Pb2+(aq) + Sn(s)

<details><summary>Solution</summary><b>Answer: (D) Pb(s) + Sn2+(aq) -> Pb2+(aq) + Sn(s)</b><br>Left side is oxidized (Pb -> Pb2+ + e-). Right side is reduced (Sn2+ + e- -> Sn).</details>


**Q31. If the salt bridge is suddenly removed from the Cd-Fe galvanic cell, what happens to the cell voltage?**

- (A) It increases significantly
- (B) It immediately drops to zero
- (C) It slowly decreases to zero
- (D) It remains unchanged

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q32. In a Galvanic cell represented by Ag(s) | Ag+(aq) || Sn2+(aq) | Sn(s), what is the direction of electron flow in the external circuit?**

- (A) From Ag+ to Sn2+
- (B) From Sn to Ag
- (C) From Sn2+ to Ag+
- (D) From Ag to Sn

<details><summary>Solution</summary><b>Answer: (D) From Ag to Sn</b><br>Electrons always flow from Anode (Ag) to Cathode (Sn) in the external circuit.</details>


**Q33. If the salt bridge is suddenly removed from the Fe-Ni galvanic cell, what happens to the cell voltage?**

- (A) It increases significantly
- (B) It immediately drops to zero
- (C) It remains unchanged
- (D) It slowly decreases to zero

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q34. If the salt bridge is suddenly removed from the Pb-Cu galvanic cell, what happens to the cell voltage?**

- (A) It slowly decreases to zero
- (B) It immediately drops to zero
- (C) It remains unchanged
- (D) It increases significantly

<details><summary>Solution</summary><b>Answer: (B) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q35. Identify the overall reaction for the cell: Cu(s) | Cu2+(aq) || Cd2+(aq) | Cd(s)**

- (A) Cu2+(aq) + Cd2+(aq) -> Cu(s) + Cd(s)
- (B) Cu(s) + Cd2+(aq) -> Cu2+(aq) + Cd(s)
- (C) Cu(s) + Cd(s) -> Cu2+(aq) + Cd2+(aq)
- (D) Cd(s) + Cu2+(aq) -> Cd2+(aq) + Cu(s)

<details><summary>Solution</summary><b>Answer: (B) Cu(s) + Cd2+(aq) -> Cu2+(aq) + Cd(s)</b><br>Left side is oxidized (Cu -> Cu2+ + e-). Right side is reduced (Cd2+ + e- -> Cd).</details>


**Q36. If the salt bridge is suddenly removed from the Ag-Ni galvanic cell, what happens to the cell voltage?**

- (A) It immediately drops to zero
- (B) It remains unchanged
- (C) It slowly decreases to zero
- (D) It increases significantly

<details><summary>Solution</summary><b>Answer: (A) It immediately drops to zero</b><br>The circuit is broken and electrical neutrality is lost instantly, causing the cell potential to drop to zero.</details>


**Q37. Identify the overall reaction for the cell: Al(s) | Al3+(aq) || Ag+(aq) | Ag(s)**

- (A) Al(s) + Ag+(aq) -> Al3+(aq) + Ag(s)
- (B) Ag(s) + Al3+(aq) -> Ag+(aq) + Al(s)
- (C) Al(s) + Ag(s) -> Al3+(aq) + Ag+(aq)
- (D) Al3+(aq) + Ag+(aq) -> Al(s) + Ag(s)

<details><summary>Solution</summary><b>Answer: (A) Al(s) + Ag+(aq) -> Al3+(aq) + Ag(s)</b><br>Left side is oxidized (Al -> Al3+ + e-). Right side is reduced (Ag+ + e- -> Ag).</details>


**Q38. In a Galvanic cell represented by Al(s) | Al3+(aq) || Cd2+(aq) | Cd(s), what is the direction of electron flow in the external circuit?**

- (A) From Al3+ to Cd2+
- (B) From Cd2+ to Al3+
- (C) From Cd to Al
- (D) From Al to Cd

<details><summary>Solution</summary><b>Answer: (D) From Al to Cd</b><br>Electrons always flow from Anode (Al) to Cathode (Cd) in the external circuit.</details>


**Q39. In a Galvanic cell represented by Zn(s) | Zn2+(aq) || Ag+(aq) | Ag(s), what is the direction of electron flow in the external circuit?**

- (A) From Zn to Ag
- (B) From Ag to Zn
- (C) From Ag+ to Zn2+
- (D) From Zn2+ to Ag+

<details><summary>Solution</summary><b>Answer: (A) From Zn to Ag</b><br>Electrons always flow from Anode (Zn) to Cathode (Ag) in the external circuit.</details>


**Q40. In a Galvanic cell represented by Pb(s) | Pb2+(aq) || Sn2+(aq) | Sn(s), what is the direction of electron flow in the external circuit?**

- (A) From Sn to Pb
- (B) From Pb to Sn
- (C) From Sn2+ to Pb2+
- (D) From Pb2+ to Sn2+

<details><summary>Solution</summary><b>Answer: (B) From Pb to Sn</b><br>Electrons always flow from Anode (Pb) to Cathode (Sn) in the external circuit.</details>


--- 
## 4. Subjective & Numerical Mastery (100 Questions)

### Board Arsenal & JEE Foundations

**Q1.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Ag(s) + 2Cd2+(aq) \rightarrow 3Ag+(aq) + 2Cd(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Ag$ is oxidized, so it is the Anode (Negative). $Cd$ is reduced, so it is the Cathode (Positive).
</details>


**Q2.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Pb2+(aq) | Pb(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Pb2+(aq) + m e^- \rightarrow Pb(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q3.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Sn(s) | Sn2+(aq) || Al3+(aq) | Al(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Sn(s) \rightarrow Sn2+(aq) + n e^-$
**At Cathode (Reduction):** $Al3+(aq) + m e^- \rightarrow Al(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q4.** Depict the Galvanic cell in which the following reaction takes place: $ Fe(s) + Cu2+(aq) \rightarrow Fe2+(aq) + Cu(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Fe(s) | Fe2+(aq) || Cu2+(aq) | Cu(s) $
Oxidation occurs at the Fe electrode (Anode). Reduction occurs at the Cu electrode (Cathode).
</details>


**Q5.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q6.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q7.** In a cell composed of $Cu$ and $Ni$ where $Cu$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Cu$) to Cathode ($Ni$).
(b) Conventional current flows from Cathode ($Ni$) to Anode ($Cu$).
</details>


**Q8.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Mg(s) + 2Al3+(aq) \rightarrow 3Mg2+(aq) + 2Al(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Mg$ is oxidized, so it is the Anode (Negative). $Al$ is reduced, so it is the Cathode (Positive).
</details>


**Q9.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Al3+(aq) | Al(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Al3+(aq) + m e^- \rightarrow Al(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q10.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cu(s) + 2Al3+(aq) \rightarrow 3Cu2+(aq) + 2Al(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cu$ is oxidized, so it is the Anode (Negative). $Al$ is reduced, so it is the Cathode (Positive).
</details>


**Q11.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q12.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Ni2+(aq) | Ni(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Ni2+(aq) + m e^- \rightarrow Ni(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q13.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Al(s) | Al3+(aq) || Ni2+(aq) | Ni(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Al(s) \rightarrow Al3+(aq) + n e^-$
**At Cathode (Reduction):** $Ni2+(aq) + m e^- \rightarrow Ni(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q14.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Zn(s) + 2Ag+(aq) \rightarrow 3Zn2+(aq) + 2Ag(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Zn$ is oxidized, so it is the Anode (Negative). $Ag$ is reduced, so it is the Cathode (Positive).
</details>


**Q15.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Ni(s) + 2Sn2+(aq) \rightarrow 3Ni2+(aq) + 2Sn(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Ni$ is oxidized, so it is the Anode (Negative). $Sn$ is reduced, so it is the Cathode (Positive).
</details>


**Q16.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q17.** Depict the Galvanic cell in which the following reaction takes place: $ Cd(s) + Sn2+(aq) \rightarrow Cd2+(aq) + Sn(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Cd(s) | Cd2+(aq) || Sn2+(aq) | Sn(s) $
Oxidation occurs at the Cd electrode (Anode). Reduction occurs at the Sn electrode (Cathode).
</details>


**Q18.** In a cell composed of $Ag$ and $Sn$ where $Ag$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Ag$) to Cathode ($Sn$).
(b) Conventional current flows from Cathode ($Sn$) to Anode ($Ag$).
</details>


**Q19.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ni(s) | Ni2+(aq) || Zn2+(aq) | Zn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ni(s) \rightarrow Ni2+(aq) + n e^-$
**At Cathode (Reduction):** $Zn2+(aq) + m e^- \rightarrow Zn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q20.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cd(s) + 2Ni2+(aq) \rightarrow 3Cd2+(aq) + 2Ni(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cd$ is oxidized, so it is the Anode (Negative). $Ni$ is reduced, so it is the Cathode (Positive).
</details>


**Q21.** In a cell composed of $Fe$ and $Pb$ where $Fe$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Fe$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Fe$).
</details>


**Q22.** Depict the Galvanic cell in which the following reaction takes place: $ Ag(s) + Pb2+(aq) \rightarrow Ag+(aq) + Pb(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Ag(s) | Ag+(aq) || Pb2+(aq) | Pb(s) $
Oxidation occurs at the Ag electrode (Anode). Reduction occurs at the Pb electrode (Cathode).
</details>


**Q23.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cd(s) + 2Ni2+(aq) \rightarrow 3Cd2+(aq) + 2Ni(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cd$ is oxidized, so it is the Anode (Negative). $Ni$ is reduced, so it is the Cathode (Positive).
</details>


**Q24.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cd(s) + 2Fe2+(aq) \rightarrow 3Cd2+(aq) + 2Fe(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cd$ is oxidized, so it is the Anode (Negative). $Fe$ is reduced, so it is the Cathode (Positive).
</details>


**Q25.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q26.** Depict the Galvanic cell in which the following reaction takes place: $ Zn(s) + Pb2+(aq) \rightarrow Zn2+(aq) + Pb(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Zn(s) | Zn2+(aq) || Pb2+(aq) | Pb(s) $
Oxidation occurs at the Zn electrode (Anode). Reduction occurs at the Pb electrode (Cathode).
</details>


**Q27.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cu(s) + 2Fe2+(aq) \rightarrow 3Cu2+(aq) + 2Fe(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cu$ is oxidized, so it is the Anode (Negative). $Fe$ is reduced, so it is the Cathode (Positive).
</details>


**Q28.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q29.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q30.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Mg(s) + 2Fe2+(aq) \rightarrow 3Mg2+(aq) + 2Fe(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Mg$ is oxidized, so it is the Anode (Negative). $Fe$ is reduced, so it is the Cathode (Positive).
</details>


**Q31.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Mg(s) | Mg2+(aq) || Fe2+(aq) | Fe(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Mg(s) \rightarrow Mg2+(aq) + n e^-$
**At Cathode (Reduction):** $Fe2+(aq) + m e^- \rightarrow Fe(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q32.** In a cell composed of $Sn$ and $Mg$ where $Sn$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Sn$) to Cathode ($Mg$).
(b) Conventional current flows from Cathode ($Mg$) to Anode ($Sn$).
</details>


**Q33.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Mg(s) | Mg2+(aq) || Cd2+(aq) | Cd(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Mg(s) \rightarrow Mg2+(aq) + n e^-$
**At Cathode (Reduction):** $Cd2+(aq) + m e^- \rightarrow Cd(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q34.** Depict the Galvanic cell in which the following reaction takes place: $ Sn(s) + Zn2+(aq) \rightarrow Sn2+(aq) + Zn(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Sn(s) | Sn2+(aq) || Zn2+(aq) | Zn(s) $
Oxidation occurs at the Sn electrode (Anode). Reduction occurs at the Zn electrode (Cathode).
</details>


**Q35.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q36.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Mg(s) + 2Ni2+(aq) \rightarrow 3Mg2+(aq) + 2Ni(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Mg$ is oxidized, so it is the Anode (Negative). $Ni$ is reduced, so it is the Cathode (Positive).
</details>


**Q37.** In a cell composed of $Al$ and $Pb$ where $Al$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Al$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Al$).
</details>


**Q38.** In a cell composed of $Zn$ and $Fe$ where $Zn$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Zn$) to Cathode ($Fe$).
(b) Conventional current flows from Cathode ($Fe$) to Anode ($Zn$).
</details>


**Q39.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Cd(s) | Cd2+(aq) || Sn2+(aq) | Sn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Cd(s) \rightarrow Cd2+(aq) + n e^-$
**At Cathode (Reduction):** $Sn2+(aq) + m e^- \rightarrow Sn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q40.** In a cell composed of $Al$ and $Cu$ where $Al$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Al$) to Cathode ($Cu$).
(b) Conventional current flows from Cathode ($Cu$) to Anode ($Al$).
</details>


**Q41.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q42.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Sn(s) | Sn2+(aq) || Cd2+(aq) | Cd(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Sn(s) \rightarrow Sn2+(aq) + n e^-$
**At Cathode (Reduction):** $Cd2+(aq) + m e^- \rightarrow Cd(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q43.** Depict the Galvanic cell in which the following reaction takes place: $ Ag(s) + Sn2+(aq) \rightarrow Ag+(aq) + Sn(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Ag(s) | Ag+(aq) || Sn2+(aq) | Sn(s) $
Oxidation occurs at the Ag electrode (Anode). Reduction occurs at the Sn electrode (Cathode).
</details>


**Q44.** Depict the Galvanic cell in which the following reaction takes place: $ Ni(s) + Mg2+(aq) \rightarrow Ni2+(aq) + Mg(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Ni(s) | Ni2+(aq) || Mg2+(aq) | Mg(s) $
Oxidation occurs at the Ni electrode (Anode). Reduction occurs at the Mg electrode (Cathode).
</details>


**Q45.** Depict the Galvanic cell in which the following reaction takes place: $ Ag(s) + Ni2+(aq) \rightarrow Ag+(aq) + Ni(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Ag(s) | Ag+(aq) || Ni2+(aq) | Ni(s) $
Oxidation occurs at the Ag electrode (Anode). Reduction occurs at the Ni electrode (Cathode).
</details>


**Q46.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q47.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ni(s) | Ni2+(aq) || Cd2+(aq) | Cd(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ni(s) \rightarrow Ni2+(aq) + n e^-$
**At Cathode (Reduction):** $Cd2+(aq) + m e^- \rightarrow Cd(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q48.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Cd(s) | Cd2+(aq) || Sn2+(aq) | Sn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Cd(s) \rightarrow Cd2+(aq) + n e^-$
**At Cathode (Reduction):** $Sn2+(aq) + m e^- \rightarrow Sn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q49.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Ni2+(aq) | Ni(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Ni2+(aq) + m e^- \rightarrow Ni(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q50.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q51.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cd(s) + 2Mg2+(aq) \rightarrow 3Cd2+(aq) + 2Mg(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cd$ is oxidized, so it is the Anode (Negative). $Mg$ is reduced, so it is the Cathode (Positive).
</details>


**Q52.** Depict the Galvanic cell in which the following reaction takes place: $ Mg(s) + Al3+(aq) \rightarrow Mg2+(aq) + Al(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Mg(s) | Mg2+(aq) || Al3+(aq) | Al(s) $
Oxidation occurs at the Mg electrode (Anode). Reduction occurs at the Al electrode (Cathode).
</details>


**Q53.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q54.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q55.** In a cell composed of $Ni$ and $Pb$ where $Ni$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Ni$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Ni$).
</details>


**Q56.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q57.** In a cell composed of $Mg$ and $Fe$ where $Mg$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Mg$) to Cathode ($Fe$).
(b) Conventional current flows from Cathode ($Fe$) to Anode ($Mg$).
</details>


**Q58.** Depict the Galvanic cell in which the following reaction takes place: $ Sn(s) + Cd2+(aq) \rightarrow Sn2+(aq) + Cd(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Sn(s) | Sn2+(aq) || Cd2+(aq) | Cd(s) $
Oxidation occurs at the Sn electrode (Anode). Reduction occurs at the Cd electrode (Cathode).
</details>


**Q59.** Depict the Galvanic cell in which the following reaction takes place: $ Pb(s) + Sn2+(aq) \rightarrow Pb2+(aq) + Sn(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Pb(s) | Pb2+(aq) || Sn2+(aq) | Sn(s) $
Oxidation occurs at the Pb electrode (Anode). Reduction occurs at the Sn electrode (Cathode).
</details>


**Q60.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Pb(s) + 2Ni2+(aq) \rightarrow 3Pb2+(aq) + 2Ni(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Pb$ is oxidized, so it is the Anode (Negative). $Ni$ is reduced, so it is the Cathode (Positive).
</details>


**Q61.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Sn(s) + 2Mg2+(aq) \rightarrow 3Sn2+(aq) + 2Mg(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Sn$ is oxidized, so it is the Anode (Negative). $Mg$ is reduced, so it is the Cathode (Positive).
</details>


**Q62.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Pb2+(aq) | Pb(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Pb2+(aq) + m e^- \rightarrow Pb(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q63.** Depict the Galvanic cell in which the following reaction takes place: $ Ni(s) + Fe2+(aq) \rightarrow Ni2+(aq) + Fe(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Ni(s) | Ni2+(aq) || Fe2+(aq) | Fe(s) $
Oxidation occurs at the Ni electrode (Anode). Reduction occurs at the Fe electrode (Cathode).
</details>


**Q64.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q65.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Cu(s) + 2Fe2+(aq) \rightarrow 3Cu2+(aq) + 2Fe(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Cu$ is oxidized, so it is the Anode (Negative). $Fe$ is reduced, so it is the Cathode (Positive).
</details>


**Q66.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q67.** In a cell composed of $Cd$ and $Al$ where $Cd$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Cd$) to Cathode ($Al$).
(b) Conventional current flows from Cathode ($Al$) to Anode ($Cd$).
</details>


**Q68.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Pb(s) + 2Zn2+(aq) \rightarrow 3Pb2+(aq) + 2Zn(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Pb$ is oxidized, so it is the Anode (Negative). $Zn$ is reduced, so it is the Cathode (Positive).
</details>


**Q69.** Depict the Galvanic cell in which the following reaction takes place: $ Fe(s) + Zn2+(aq) \rightarrow Fe2+(aq) + Zn(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Fe(s) | Fe2+(aq) || Zn2+(aq) | Zn(s) $
Oxidation occurs at the Fe electrode (Anode). Reduction occurs at the Zn electrode (Cathode).
</details>


**Q70.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Ag(s) | Ag+(aq) || Sn2+(aq) | Sn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Ag(s) \rightarrow Ag+(aq) + n e^-$
**At Cathode (Reduction):** $Sn2+(aq) + m e^- \rightarrow Sn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q71.** In a cell composed of $Zn$ and $Ni$ where $Zn$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Zn$) to Cathode ($Ni$).
(b) Conventional current flows from Cathode ($Ni$) to Anode ($Zn$).
</details>


**Q72.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Sn(s) + 2Mg2+(aq) \rightarrow 3Sn2+(aq) + 2Mg(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Sn$ is oxidized, so it is the Anode (Negative). $Mg$ is reduced, so it is the Cathode (Positive).
</details>


**Q73.** In a cell composed of $Pb$ and $Cu$ where $Pb$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Pb$) to Cathode ($Cu$).
(b) Conventional current flows from Cathode ($Cu$) to Anode ($Pb$).
</details>


**Q74.** In a cell composed of $Pb$ and $Ni$ where $Pb$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Pb$) to Cathode ($Ni$).
(b) Conventional current flows from Cathode ($Ni$) to Anode ($Pb$).
</details>


**Q75.** In a cell composed of $Mg$ and $Al$ where $Mg$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Mg$) to Cathode ($Al$).
(b) Conventional current flows from Cathode ($Al$) to Anode ($Mg$).
</details>


**Q76.** In a cell composed of $Cu$ and $Fe$ where $Cu$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Cu$) to Cathode ($Fe$).
(b) Conventional current flows from Cathode ($Fe$) to Anode ($Cu$).
</details>


**Q77.** Depict the Galvanic cell in which the following reaction takes place: $ Zn(s) + Ni2+(aq) \rightarrow Zn2+(aq) + Ni(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Zn(s) | Zn2+(aq) || Ni2+(aq) | Ni(s) $
Oxidation occurs at the Zn electrode (Anode). Reduction occurs at the Ni electrode (Cathode).
</details>


**Q78.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Fe(s) | Fe2+(aq) || Zn2+(aq) | Zn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Fe(s) \rightarrow Fe2+(aq) + n e^-$
**At Cathode (Reduction):** $Zn2+(aq) + m e^- \rightarrow Zn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q79.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Ag(s) + 2Ni2+(aq) \rightarrow 3Ag+(aq) + 2Ni(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Ag$ is oxidized, so it is the Anode (Negative). $Ni$ is reduced, so it is the Cathode (Positive).
</details>


**Q80.** In a cell composed of $Ag$ and $Ni$ where $Ag$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Ag$) to Cathode ($Ni$).
(b) Conventional current flows from Cathode ($Ni$) to Anode ($Ag$).
</details>


**Q81.** In a cell composed of $Zn$ and $Cd$ where $Zn$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Zn$) to Cathode ($Cd$).
(b) Conventional current flows from Cathode ($Cd$) to Anode ($Zn$).
</details>


**Q82.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q83.** In a cell composed of $Fe$ and $Pb$ where $Fe$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Fe$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Fe$).
</details>


**Q84.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Fe(s) | Fe2+(aq) || Sn2+(aq) | Sn(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Fe(s) \rightarrow Fe2+(aq) + n e^-$
**At Cathode (Reduction):** $Sn2+(aq) + m e^- \rightarrow Sn(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q85.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Pb(s) + 2Cd2+(aq) \rightarrow 3Pb2+(aq) + 2Cd(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Pb$ is oxidized, so it is the Anode (Negative). $Cd$ is reduced, so it is the Cathode (Positive).
</details>


**Q86.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q87.** In a cell composed of $Al$ and $Pb$ where $Al$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Al$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Al$).
</details>


**Q88.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Sn(s) | Sn2+(aq) || Ni2+(aq) | Ni(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Sn(s) \rightarrow Sn2+(aq) + n e^-$
**At Cathode (Reduction):** $Ni2+(aq) + m e^- \rightarrow Ni(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q89.** In a cell composed of $Mg$ and $Cd$ where $Mg$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Mg$) to Cathode ($Cd$).
(b) Conventional current flows from Cathode ($Cd$) to Anode ($Mg$).
</details>


**Q90.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Ag(s) + 2Zn2+(aq) \rightarrow 3Ag+(aq) + 2Zn(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Ag$ is oxidized, so it is the Anode (Negative). $Zn$ is reduced, so it is the Cathode (Positive).
</details>


**Q91.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q92.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q93.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Pb(s) + 2Cu2+(aq) \rightarrow 3Pb2+(aq) + 2Cu(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Pb$ is oxidized, so it is the Anode (Negative). $Cu$ is reduced, so it is the Cathode (Positive).
</details>


**Q94.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Pb(s) + 2Fe2+(aq) \rightarrow 3Pb2+(aq) + 2Fe(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Pb$ is oxidized, so it is the Anode (Negative). $Fe$ is reduced, so it is the Cathode (Positive).
</details>


**Q95.** Write the half-cell reactions and the overall cell reaction for the Galvanic cell represented by: $ Al(s) | Al3+(aq) || Ni2+(aq) | Ni(s) $.

<details><summary>Solution</summary>
**At Anode (Oxidation):** $Al(s) \rightarrow Al3+(aq) + n e^-$
**At Cathode (Reduction):** $Ni2+(aq) + m e^- \rightarrow Ni(s)$
**Overall:** Multiply to balance electrons and add.
</details>


**Q96.** In a cell composed of $Cu$ and $Pb$ where $Cu$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Cu$) to Cathode ($Pb$).
(b) Conventional current flows from Cathode ($Pb$) to Anode ($Cu$).
</details>


**Q97.** Identify the anode and the cathode in a cell where the overall reaction is $ 3Ni(s) + 2Pb2+(aq) \rightarrow 3Ni2+(aq) + 2Pb(s) $ (assuming charges are 2+ and 3+ respectively). Which electrode is positive?

<details><summary>Solution</summary>
$Ni$ is oxidized, so it is the Anode (Negative). $Pb$ is reduced, so it is the Cathode (Positive).
</details>


**Q98.** In a cell composed of $Al$ and $Sn$ where $Al$ acts as the anode:
(a) What is the direction of electron flow in the external circuit?
(b) What is the direction of conventional current?

<details><summary>Solution</summary>
(a) Electrons flow from Anode ($Al$) to Cathode ($Sn$).
(b) Conventional current flows from Cathode ($Sn$) to Anode ($Al$).
</details>


**Q99.** Why is an agar-agar paste of $NH_4NO_3$ preferred over $KCl$ in a salt bridge when connecting a standard hydrogen electrode to a silver half-cell ($Ag^+/Ag$)?

<details><summary>Solution</summary>
If $KCl$ is used, the $Cl^-$ ions from the salt bridge will enter the silver half-cell and react with $Ag^+$ ions to form a white precipitate of $AgCl$. This precipitation will block the porous plug and stop the cell reaction. Therefore, $NH_4NO_3$ or $KNO_3$ is preferred.
</details>


**Q100.** Depict the Galvanic cell in which the following reaction takes place: $ Pb(s) + Ag+(aq) \rightarrow Pb2+(aq) + Ag(s) $. Also indicate the electrodes at which oxidation and reduction occur.

<details><summary>Solution</summary>
**Cell Notation:** $ Pb(s) | Pb2+(aq) || Ag+(aq) | Ag(s) $
Oxidation occurs at the Pb electrode (Anode). Reduction occurs at the Ag electrode (Cathode).
</details>

