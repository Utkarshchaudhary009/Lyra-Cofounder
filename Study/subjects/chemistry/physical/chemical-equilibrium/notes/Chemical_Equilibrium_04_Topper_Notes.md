# 🧪 Chemical Equilibrium - Lecture 04 (Topper's Notes)
*Arjuna JEE 2026 Batch | Physics Wallah*

---

## 📌 1. Expression of Equilibrium Constant ($K_c$ & $K_p$)

### A. General Method for Derivation
1.  Write initial moles at $t=0$.
2.  Write moles at equilibrium $t=t_{eq}$ using $x$ (moles dissociated/reacted).
3.  **For $K_c$:** Convert moles to concentration: $[\text{Conc}] = \frac{n}{V}$.
4.  **For $K_p$:** Convert moles to Partial Pressure: $p_i = \chi_i \cdot P_{total} = \frac{n_i}{n_{total}} \cdot P$.

### B. Case Studies (Important Derivations)

#### Type 1: $\Delta n_g > 0$ (Dissociation of $PCl_5$)
$$PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)$$
*   **Initial:** $a$ moles of $PCl_5$.
*   **Equilibrium:** $(a-x)$, $x$, $x$.
*   **Total Moles ($n_T$):** $a+x$

$$K_c = \frac{x^2}{V(a-x)} \quad \bigg| \quad K_p = \frac{x^2 P}{a^2 - x^2}$$

> **💡 Key Insight:** For $\Delta n_g > 0$, dissociation increases with Volume ($\uparrow$) and decreases with Pressure ($\downarrow$).

#### Type 2: $\Delta n_g = 0$ (Synthesis of $HI$)
$$H_2(g) + I_2(g) \rightleftharpoons 2HI(g)$$
*   **Initial:** $a$, $b$ moles.
*   **Equilibrium:** $(a-x)$, $(b-x)$, $2x$.

$$K_c = \frac{4x^2}{(a-x)(b-x)} \quad \bigg| \quad K_p = K_c$$
*(Volume and Total Pressure terms cancel out)*

> **💡 Key Insight:** When $\Delta n_g = 0$, $K_p = K_c$ and equilibrium position is **independent** of Volume and Pressure.

#### Type 3: Heterogeneous Equilibrium
$$CaCO_3(s) \rightleftharpoons CaO(s) + CO_2(g)$$
*   **Rule:** Pure solids and liquids have active mass = 1 (constant).

$$K_c = [CO_2] \quad \bigg| \quad K_p = P_{CO_2}$$

---

## 📌 2. Degree of Dissociation ($\alpha$)

**Definition:** The fraction of 1 mole that dissociates.
$$\alpha = \frac{\text{Moles Dissociated}}{\text{Initial Moles}} = \frac{x}{a} \implies x = a\alpha$$

### Derivation for $PCl_5$ using $\alpha$
Substituting $x = a\alpha$ into the $K_c$ expression:
$$K_c = \frac{(a\alpha)^2}{V(a - a\alpha)} = \frac{a \alpha^2}{V(1 - \alpha)}$$

**🔥 The Approximation Trick:**
If dissociation is very small ($\alpha \ll 1$), then $(1 - \alpha) \approx 1$.
$$K_c \approx \frac{a \alpha^2}{V} \implies \alpha \propto \sqrt{V} \propto \frac{1}{\sqrt{C}}$$
*(Similar to Ostwald's Dilution Law)*

---

## 📌 3. Characteristics of Equilibrium Constant ($K$)

| Factor | Effect on $K$ | Note |
| :--- | :--- | :--- |
| **Concentration** | ❌ No Change | Shifts reaction quotient ($Q$), not $K$. |
| **Pressure/Volume** | ❌ No Change | Shifts equilibrium position only. |
| **Catalyst** | ❌ No Change | Speeds up forward & backward rates equally. |
| **Inert Gas** | ❌ No Change | Doesn't affect $K$ value. |
| **Temperature** | ✅ **CHANGES** | The **ONLY** physical factor that changes $K$. |
| **Stoichiometry** | ✅ **CHANGES** | Depends on how you balance the reaction. |

### Mathematical Rules for $K$ (Stoichiometry)

1.  **Reverse Reaction:** 
    $$A \rightleftharpoons B \ (K) \implies B \rightleftharpoons A \ (K' = 1/K)$$
2.  **Multiply by $n$:**
    $$A \rightleftharpoons B \ (K) \implies nA \rightleftharpoons nB \ (K'' = K^n)$$
3.  **Add Reactions:**
    $$Rxn_1 + Rxn_2 = Rxn_{final} \implies K_{final} = K_1 \times K_2$$

---

## 📝 4. Selected Top Solved Examples

### Example 1: Finding Equilibrium Moles (Page 9)
**Q:** Reaction $A + B \rightleftharpoons 2C$. Initial moles: $A=2, B=3$. If $K_c=4$ at 400K, find moles of C at equilibrium.

**Solution:**
1.  Equation: $A + B \rightleftharpoons 2C$
2.  t=eq: $(2-x) \quad (3-x) \quad 2x$
3.  Since $\Delta n_g=0$, Volume cancels out.
    $$4 = \frac{(2x)^2}{(2-x)(3-x)}$$
    Take square root of both sides:
    $$2 = \frac{2x}{\sqrt{(2-x)(3-x)}} \rightarrow \text{Wait, complete square not valid for denominator.}$$
    *Correction:* $2 = \frac{2x}{\dots}$ NO, solve quadratic or check perfect square.
    Actually, let's look at the notes solution logic:
    $$4 = \frac{4x^2}{(2-x)(3-x)} \implies (2-x)(3-x) = x^2$$
    $$6 - 2x - 3x + x^2 = x^2 \implies 6 - 5x = 0 \implies x = 1.2$$
4.  Moles of C = $2x = 2(1.2) = \mathbf{2.4}$

### Example 2: Calculating $K_c$ (Page 10)
**Q:** $H_2 + I_2 \rightleftharpoons 2HI$. Initial: 15 mol $H_2$, 5.2 mol $I_2$. At eq, [HI] moles = 10. Find $K_c$.

**Solution:**
1.  $2HI$ formed = $2x = 10 \implies x = 5$.
2.  Eq moles $H_2 = 15 - 5 = 10$.
3.  Eq moles $I_2 = 5.2 - 5 = 0.2$.
4.  $$K_c = \frac{[HI]^2}{[H_2][I_2]} = \frac{(10/V)^2}{(10/V)(0.2/V)} = \frac{100}{2} = \mathbf{50}$$

### Example 3: $K_p$ & Degree of Dissociation (Page 21)
**Q:** $N_2O_3(g) \rightleftharpoons NO(g) + NO_2(g)$. Total Pressure = $P$. Degree of dissociation $\alpha = 50\% (0.5)$. Find $K_p$.

**Solution:**
1.  Moles at eq: $N_2O_3 \propto (1-\alpha)$, $NO \propto \alpha$, $NO_2 \propto \alpha$.
2.  Total moles $\propto 1 + \alpha$.
3.  Partial Pressures: 
    *   $P_{N2O3} = \frac{1-\alpha}{1+\alpha}P$
    *   $P_{products} = \frac{\alpha}{1+\alpha}P$
4.  Formula for this type ($\Delta n_g=1$):
    $$K_p = \frac{\alpha^2 P}{1 - \alpha^2}$$
5.  Plug $\alpha = 0.5$:
    $$K_p = \frac{(0.5)^2 P}{1 - 0.25} = \frac{0.25 P}{0.75} = \mathbf{\frac{P}{3}}$$

### Example 4: Scaling K (Page 30)
**Q:** $N_2 + O_2 \rightleftharpoons 2NO$ has constant $K$.
Find constant for $\frac{1}{2}N_2 + \frac{1}{2}O_2 \rightleftharpoons NO$.

**Solution:**
*   The target reaction is the original multiplied by $\frac{1}{2}$.
*   New Constant $K' = K^{1/2} = \mathbf{\sqrt{K}}$.
