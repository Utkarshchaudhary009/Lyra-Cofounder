# 📘 Chemical Equilibrium - Lecture 04 (Detailed Concepts)
*Comprehensive Study Notes for Deep Understanding*

---

## 📖 Introduction: What are we doing today?
In this lecture, we move from the **definition** of Equilibrium Constants ($K_c, K_p$) to their **application**. We will learn:
1.  How to **derive formula expressions** for $K$ for any chemical reaction.
2.  What **Degree of Dissociation ($\alpha$)** is and how it simplifies calculations.
3.  The specific **properties of $K$**—what makes it change and what doesn't.

---

## 1. Writing Expressions for Equilibrium Constants
The core skill in this chapter is the **ICE Method** (Initial, Change, Equilibrium). We use this to relate the starting amounts of reactants to their final Equilibrium state.

### 🧠 The General Technique (step-by-step)
1.  **Write the Balanced Equation.**
2.  **t = 0 (Initial):** Write down the initial moles given (usually $a$ for reactants, 0 for products).
3.  **t = eq (Equilibrium):** Define $x$ as the "moles reacted".
    *   Use stoichiometry to find moles of products formed.
    *   *Example:* If $2A \rightarrow 3B$ and $x$ moles of A react, then $\frac{3}{2}x$ moles of B are formed.
4.  **Convert to Concentration or Pressure:**
    *   For **$K_c$**: Divide equilibrium moles by Volume ($V$).
    *   For **$K_p$**: First find Mole Fraction ($\chi = \frac{n_{eq}}{n_{total}}$), then multiply by Total Pressure ($\chi \times P$).

---

### Phase 1: Homogeneous Gaseous Reactions

#### Case Study A: Dissociation of $PCl_5$ ($\Delta n_g > 0$)
*Description: One molecule breaks into two gases. The number of moles increases.*

**Step 1: The ICE Table**
| reaction | $PCl_5(g)$ | $\rightleftharpoons$ | $PCl_3(g)$ | $Cl_2(g)$ |
| :--- | :---: | :---: | :---: | :---: |
| **Initial (t=0)** | $a$ | | 0 | 0 |
| **Equilibrium (t=eq)**| $a - x$ | | $x$ | $x$ |

*   **Total Moles usually ($n_T$):** $(a-x) + x + x = a + x$

**Step 2: Deriving $K_c$**
*   $[PCl_5] = \frac{a-x}{V}$
*   $[PCl_3] = \frac{x}{V}$
*   $[Cl_2] = \frac{x}{V}$

$$K_c = \frac{[PCl_3][Cl_2]}{[PCl_5]} = \frac{(\frac{x}{V})(\frac{x}{V})}{(\frac{a-x}{V})} = \frac{x^2}{V(a-x)}$$

> **🤔 Conceptual Note:** Notice the $V$ in the denominator? This means if you **increase Volume** (dilute the gas), $K_c$ must stay constant, so the numerator ($x^2$) must increase.
> **Conclusion:** For $\Delta n_g > 0$, **Low Pressure / High Volume favors products.**

**Step 3: Deriving $K_p$**
*Total Pressure = P*
*   $p_{PCl5} = (\frac{a-x}{a+x})P$
*   $p_{PCl3} = (\frac{x}{a+x})P$
*   $p_{Cl2} = (\frac{x}{a+x})P$

$$K_p = \frac{p_{PCl3} \cdot p_{Cl2}}{p_{PCl5}} = \frac{(\frac{x}{a+x}P) (\frac{x}{a+x}P)}{(\frac{a-x}{a+x}P)}$$

$$K_p = \frac{x^2 P}{(a+x)(a-x)} = \frac{x^2 P}{a^2 - x^2}$$

---

#### Case Study B: Formation of HI ($\Delta n_g = 0$)
*Description: Moles of gaseous reactants equal moles of gaseous products.*

**Step 1: The ICE Table**
| reaction | $H_2(g)$ | $+$ | $I_2(g)$ | $\rightleftharpoons$ | $2HI(g)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Initial** | $a$ | | $b$ | | 0 |
| **Equilibrium** | $a - x$ | | $b - x$ | | $2x$ |

**Step 2: Deriving $K_c$**
$$K_c = \frac{[HI]^2}{[H_2][I_2]} = \frac{(\frac{2x}{V})^2}{(\frac{a-x}{V})(\frac{b-x}{V})}$$

$$K_c = \frac{4x^2 \cancel{V^{-2}}}{(a-x)(b-x) \cancel{V^{-2}}} = \frac{4x^2}{(a-x)(b-x)}$$

> **🤔 Conceptual Note:** Look! The Volume ($V$) terms **cancelled out completely**.
> **Conclusion:** When $\Delta n_g = 0$, changing the Volume or Pressure has **NO EFFECT** on the number of moles at equilibrium. The state is independent of container size.

---

### Phase 2: Heterogeneous Equilibrium (Solids + Gases)

#### The Golden Rule
**Pure Solids and Pure Liquids have constant Active Mass (taken as Unity, 1).**
*Why? Density is constant, so concentration (moles/liter) doesn't change for a pure substance.*

#### Case Study: Decomposition of Limestone
$$CaCO_3(s) \rightleftharpoons CaO(s) + CO_2(g)$$

*   $CaCO_3$ is Solid $\rightarrow$ [Active Mass = 1]
*   $CaO$ is Solid $\rightarrow$ [Active Mass = 1]

**Expression:**
$$K_c = \frac{[CaO][CO_2]}{[CaCO_3]} = \frac{(1) [CO_2]}{(1)} \implies \mathbf{K_c = [CO_2]}$$

Similarly for Pressure:
$$\mathbf{K_p = P_{CO_2}}$$

---

## 2. Degree of Dissociation ($\alpha$)

This concept bridges the gap between theoretical moles and percentage reactions.

### What is $\alpha$?
It represents the **extent** of the reaction. $\alpha$ is the fraction of **1 mole** that dissociates.
*   If $\alpha = 0.5$, it means 50% of the reactant has broken down.
*   **Formula:** $\alpha = \frac{x}{a}$ (where $x$ is moles reacted, $a$ is initial moles).
*   **Relationship:** $\mathbf{x = a\alpha}$

### Rewriting $PCl_5$ expression using $\alpha$
Return to our $K_p$ formula for $PCl_5$, substitute $x = a\alpha$:

$$K_p = \frac{(a\alpha)^2 P}{a^2 - (a\alpha)^2} = \frac{a^2 \alpha^2 P}{a^2(1 - \alpha^2)}$$

$$K_p = \frac{\alpha^2 P}{1 - \alpha^2}$$

### ⚡ The "Negligible Alpha" Short-cut
In many problems, $\alpha$ is very small (e.g., $< 5\%$ or $< 0.05$).
*   If $\alpha \ll 1$, then subtraction $(1 - \alpha^2) \approx 1$.
*   The math becomes super easy:
    $$K_p \approx \alpha^2 P \quad \implies \quad \alpha = \sqrt{\frac{K_p}{P}}$$

*This tells us that for dissociation reactions, increasing Pressure ($P$) decreases Dissociation ($\alpha$).*

---

## 3. Characteristics of Equilibrium Constant (K)

Knowing what changes $K$ and what doesn't is critical for True/False questions.

### ❌ What DOES NOT change $K$:
1.  **Concentration:** Adding more reactant shifts the reaction forward to consume it, but the *ratio* ($K$) stays the same once equilibrium is re-established.
2.  **Pressure / Volume:** Same logic. The system adjusts ($Q$ changes), but $K$ remains a constant target.
3.  **Catalyst:** A catalyst lowers the activation energy for **both** forward and backward reactions equally. Equilibrium is reached *faster*, but the final position ($K$) is unchanged.

### ✅ What DOES change $K$:
1.  **Temperature ($T$):**
    *   This is the **only** physical parameter that changes $K$.
    *   *Endothermic ($\Delta H > 0$):* Heat is a reactant. Increasing $T$ pushes forward $\rightarrow K$ increases.
    *   *Exothermic ($\Delta H < 0$):* Heat is a product. Increasing $T$ pushes backward $\rightarrow K$ decreases.

2.  **Mode of Representation (Stoichiometry):**
    The value of $K$ depends on how you write the balanced equation.

    *   **Rule 1 (Reversal):**
        Reaction: $A \rightleftharpoons B \quad (K = 4)$
        Reverse: $B \rightleftharpoons A \quad (K' = \frac{1}{4} = 0.25)$

    *   **Rule 2 (Multiplication by 'n'):**
        Reaction: $A \rightleftharpoons B \quad (K)$
        Scaled: $2A \rightleftharpoons 2B \quad (K_{new} = K^2)$
        Halved: $\frac{1}{2}A \rightleftharpoons \frac{1}{2}B \quad (K_{new} = K^{1/2} = \sqrt{K})$

    *   **Rule 3 (Additivity):**
        If Reaction 3 = Reaction 1 + Reaction 2
        Then $K_3 = K_1 \times K_2$

---
*End of Detailed Concept Notes*
