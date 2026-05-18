# Board Questions Archive — Moving Charges and Magnetism
### Class 12 Physics | Chapter 4 | NCERT

---

> *"Mastering Previous Year Board Questions is the masterkey to scoring perfect marks in CBSE and State Board examinations. This compilation features authentic, highly repeated questions categorized by marks weightage with complete pedagogical solutions."*

---

## Master Table of Contents
1. [Very Short Answer Questions (1 Mark)](#very-short-answer-questions-1-mark)
2. [Short Answer Questions (2 Marks)](#short-answer-questions-2-marks)
3. [Short Answer Questions (3 Marks)](#short-answer-questions-3-marks)
4. [Long Answer Questions (5 Marks)](#long-answer-questions-5-marks)

---

## Very Short Answer Questions (1 Mark)

### Q 1.1 ⭐
State two essential properties of the material of the wire used for the suspension of the coil in a moving coil galvanometer.

<details>
<summary><b>Solution</b></summary>

The suspension wire in a moving coil galvanometer must possess the following two properties:
1. **Low Torsional Constant ($k$):** The restoring torque per unit twist must be as small as possible to ensure high current sensitivity ($\phi/I \propto 1/k$).
2. **High Tensile Strength & Non-brittle Nature:** The material must be highly conducting, non-brittle, and exhibit negligible elastic after-effect so that the coil returns exactly to zero deflection when the current is turned off.

> **Note:** **Phosphor-bronze** or **quartz** strips are standard materials used for this purpose.
</details>

---

### Q 1.2 ⭐
What will be the path of a charged particle moving directly along the direction of a uniform magnetic field?<br>

<details>
<summary><b>Solution</b></summary>

The path of the charged particle will remain a **straight line** (undeflected).

**Reasoning:**
The magnetic Lorentz force acting on a moving charge is given by:
$$\vec{F} = q(\vec{v} \times \vec{B}) \implies F = qvB\sin\theta$$

Since the particle moves parallel to the magnetic field line, the angle between its velocity vector $\vec{v}$ and the magnetic field $\vec{B}$ is $\theta = 0^\circ$.
$$F = qvB\sin 0^\circ = 0$$

With zero net force acting on it, the particle continues moving with uniform velocity along its initial straight path due to inertia.
</details>

---

### Q 1.3 ⭐⭐
Two wires of equal lengths are bent in the form of two separate loops. One of the loops is square-shaped whereas the other loop is circular. These are suspended in a uniform magnetic field and the same current is passed through them. Which loop will experience greater torque?<br> Give reasons.

<details>
<summary><b>Solution</b></summary>

The **circular loop** will experience a greater torque.

**Reasoning:**
The magnitude of torque experienced by a current-carrying loop in a uniform magnetic field is given by:
$$\tau = NIAB\sin\theta \implies \tau \propto A$$
*(assuming identical number of turns $N=1$, current $I$, magnetic field $B$, and orientation $\theta$)*

Let the total length of each wire be $L$.
- **For the Square Loop:** 
  $$\text{Perimeter} = 4a = L \implies a = \frac{L}{4}$$
  $$\text{Area } (A_s) = a^2 = \frac{L^2}{16} \approx 0.0625 L^2$$

- **For the Circular Loop:**
  $$\text{Circumference} = 2\pi r = L \implies r = \frac{L}{2\pi}$$
  $$\text{Area } (A_c) = \pi r^2 = \pi \left(\frac{L}{2\pi}\right)^2 = \frac{L^2}{4\pi} \approx 0.0796 L^2$$

Comparing the two areas, $A_c > A_s$. Since torque is directly proportional to the enclosed area, the circular loop experiences greater torque.
</details>

---

### Q 1.4 ⭐
A cyclotron is not suitable to accelerate light particles like electrons. Why?<br>

<details>
<summary><b>Solution</b></summary>

A cyclotron cannot accelerate electrons because of their **extremely small rest mass** ($m_e \approx 9.1 \times 10^{-31}\text{ kg}$).

**Reasoning:**
Due to their tiny mass, electrons gain extraordinarily high speeds (approaching the speed of light $c$) even at relatively small accelerating voltages. According to Einstein's special theory of relativity, as velocity $v$ approaches $c$, the relativistic mass of the electron increases rapidly:
$$m = \frac{m_0}{\sqrt{1 - \frac{v^2}{c^2}}}$$

The frequency of revolution of a particle inside the dees of a cyclotron is given by:
$$f = \frac{qB}{2\pi m}$$

As the mass $m$ increases, the frequency of revolution $f$ decreases. Consequently, the electrons fall out of step (resonance) with the alternating frequency of the applied high-frequency oscillator, preventing them from being accelerated further.
</details>

---

## Short Answer Questions (2 Marks)

### Q 2.1 ⭐⭐
An $\alpha$-particle and a proton are moving in the plane of the paper in a region where there is a uniform magnetic field $\vec{B}$ directed normal to the plane of the paper. If the two particles have equal linear momenta, what will be the ratio of the radii of their trajectories in the field?<br>

<details>
<summary><b>Solution</b></summary>

The radius of the circular trajectory of a charged particle moving perpendicular to a uniform magnetic field is given by balancing the magnetic Lorentz force with the required centripetal force:
$$qvB = \frac{mv^2}{r} \implies r = \frac{mv}{qB} = \frac{p}{qB}$$
where $p = mv$ is the linear momentum of the particle.

Since both the linear momentum $p$ and the magnetic field $B$ are identical for both particles:
$$r \propto \frac{1}{q}$$

Therefore, the ratio of the radius of the $\alpha$-particle ($r_\alpha$) to the radius of the proton ($r_p$) is:
$$\frac{r_\alpha}{r_p} = \frac{q_p}{q_\alpha}$$

Knowing that the charge of a proton is $q_p = e$ and the charge of an $\alpha$-particle (helium nucleus) is $q_\alpha = 2e$:
$$\frac{r_\alpha}{r_p} = \frac{e}{2e} = \frac{1}{2}$$

$$\boxed{r_\alpha : r_p = 1 : 2}$$
</details>

---

### Q 2.2 ⭐⭐
Write the expression for the force acting on a charged particle of charge $q$ moving with velocity $\vec{v}$ in the presence of a magnetic field $\vec{B}$. Show that in the presence of this force:
1. The kinetic energy of the particle does not change.
2. Its instantaneous power is zero.

<details>
<summary><b>Solution</b></summary>

The magnetic force acting on a moving charged particle is given by the Lorentz force formula:
$$\vec{F} = q(\vec{v} \times \vec{B})$$

#### 1. Constancy of Kinetic Energy:
From the properties of the vector cross product, the magnetic force $\vec{F}$ is always directed perpendicular to the instantaneous velocity vector $\vec{v}$ (and hence perpendicular to the infinitesimal displacement $d\vec{s}$).
$$\vec{F} \perp \vec{v} \implies \text{Angle } \theta = 90^\circ$$

The work done by the magnetic force over a small displacement $d\vec{s} = \vec{v} dt$ is:
$$dW = \vec{F} \cdot d\vec{s} = F \, ds \cos 90^\circ = 0$$

According to the **Work-Energy Theorem**, the net work done on a particle equals its change in kinetic energy:
$$W_{\text{net}} = \Delta K.E. \implies 0 = K.E._{\text{final}} - K.E._{\text{initial}}$$
Thus, the kinetic energy (and speed) of the particle remains completely unchanged.

#### 2. Instantaneous Power is Zero:
Instantaneous power $P$ delivered by a force is defined as the dot product of force and velocity:
$$P = \vec{F} \cdot \vec{v} = Fv \cos 90^\circ = 0$$
Hence, the magnetic field delivers zero power to the moving charge.
</details>

---

### Q 2.3 ⭐⭐
An electron of kinetic energy $25\text{ keV}$ moves perpendicular to the direction of a uniform magnetic field of $0.2\text{ millitesla}$. Calculate the time period of rotation of the electron in the magnetic field.

<details>
<summary><b>Solution</b></summary>

**1. Identify the given parameters:**
- Kinetic Energy ($K.E.$) = $25\text{ keV}$ *(Note: Time period is independent of speed/energy, so this value is extraneous data designed to test conceptual clarity!)*
- Magnetic field ($B$) = $0.2\text{ mT} = 0.2 \times 10^{-3}\text{ T}$
- Mass of electron ($m$) = $9.1 \times 10^{-31}\text{ kg}$
- Charge of electron ($q$) = $1.6 \times 10^{-19}\text{ C}$

**2. Formula for Time Period:**
The time taken to complete one full circular revolution is:
$$T = \frac{2\pi r}{v}$$
Substituting $r = \frac{mv}{qB}$:
$$T = \frac{2\pi m}{qB}$$

**3. Calculation:**
$$T = \frac{2 \times 3.1416 \times 9.1 \times 10^{-31}}{1.6 \times 10^{-19} \times 0.2 \times 10^{-3}}$$

$$T = \frac{57.177 \times 10^{-31}}{0.32 \times 10^{-22}} \approx 1.787 \times 10^{-7}\text{ seconds}$$

$$\boxed{T \approx 1.79 \times 10^{-7}\text{ s}}$$
</details>

---

### Q 2.4 ⭐⭐
It is desired to pass only $10\%$ of the total current through a galvanometer of resistance $90\ \Omega$. How much shunt resistance should be connected across the galvanometer?<br>

<details>
<summary><b>Solution</b></summary>

**1. Setup the circuit parameters:**
- Let the total main line current be $I$.
- Current required through the galvanometer: $I_g = 10\% \text{ of } I = 0.1 I$.
- Remaining current bypassing through the parallel shunt resistor: $I_s = I - I_g = I - 0.1 I = 0.9 I$.
- Galvanometer resistance ($G$) = $90\ \Omega$.
- Shunt resistance = $S$.

**2. Parallel Circuit Principle:**
Since the galvanometer and the shunt resistor are connected in parallel across the same two nodes, the potential drop across both branches must be exactly equal:
$$V_g = V_s \implies I_g \cdot G = I_s \cdot S$$

**3. Substitute values and solve for $S$:**
$$(0.1 I) \times 90 = (0.9 I) \times S$$

Dividing both sides by main current $I$:
$$9 = 0.9 S \implies S = \frac{9}{0.9} = 10\ \Omega$$

$$\boxed{S = 10\ \Omega}$$
A shunt resistance of $10\ \Omega$ must be connected in parallel across the galvanometer.
</details>

---

## Short Answer Questions (3 Marks)

### Q 3.1 ⭐⭐⭐
Derive an expression for the force acting on a straight current-carrying conductor placed in a uniform magnetic field. Name the rule which gives the direction of this force. State the condition under which this force is maximum and minimum.

<details>
<summary><b>Solution</b></summary>

#### Derivation of Force on a Conductor:
Consider a straight conducting rod of length $L$ and uniform cross-sectional area $A$, placed in a uniform magnetic field $\vec{B}$ at an angle $\theta$ to the field lines. Let a steady current $I$ flow through the conductor.

1. **Microscopic Force on a Single Electron:**
   If the free electrons drift with a velocity $\vec{v}_d$, the magnetic Lorentz force experienced by a single moving electron is:
   $$\vec{f} = -e(\vec{v}_d \times \vec{B})$$

2. **Total Number of Electrons in the Conductor:**
   Let $n$ be the free electron density (number of electrons per unit volume).
   $$\text{Total Volume} = A \cdot L$$
   $$\text{Total number of free electrons } (N) = n \cdot A \cdot L$$

3. **Total Force on the Conductor:**
   The total magnetic force $\vec{F}$ is the vector sum of forces acting on all individual charge carriers inside the segment:
   $$\vec{F} = N \cdot \vec{f} = (nAL)\left[-e(\vec{v}_d \times \vec{B})\right] = -neA L (\vec{v}_d \times \vec{B})$$

4. **Relating to Macroscopic Current:**
   We know the fundamental relation between electric current and drift velocity:
   $$I = neA v_d$$
   We can define a current-length vector $\vec{L}$ pointing in the direction of conventional current flow (opposite to the drift velocity of negative electrons, so $-v_d \hat{v}_d \propto \vec{L}$). Substituting this yields:
   $$\vec{F} = I(\vec{L} \times \vec{B})$$
   
   In scalar magnitude form:
   $$\boxed{F = I L B \sin\theta}$$

#### Direction Rule:
The direction of the force is perpendicular to the plane containing both $\vec{L}$ and $\vec{B}$, and is determined using **Fleming's Left-Hand Rule**:
> Stretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular to each other. If the **F**orefinger points along the Magnetic **F**ield ($\vec{B}$) and the **M**iddle finger points along the **C**urrent ($I$), then the **T**humb points in the direction of the Magnetic Force or **M**otion ($\vec{F}$).

#### Special Conditions:
- **Maximum Force:** Occurs when the conductor is oriented perpendicular to the magnetic field ($\theta = 90^\circ$).
  $$F_{\text{max}} = ILB \sin 90^\circ = ILB$$
- **Minimum Force:** Occurs when the conductor lies aligned parallel or antiparallel to the magnetic field ($\theta = 0^\circ \text{ or } 180^\circ$).
  $$F_{\text{min}} = ILB \sin 0^\circ = 0$$
</details>

---

### Q 3.2 ⭐⭐⭐
Two straight parallel current-carrying conductors are kept at a distance $r$ from each other in air. The direction of current in both conductors is the same. Find the magnitude and direction of the force between them. Hence define one ampere.

<details>
<summary><b>Solution</b></summary>

#### Derivation of Force Between Parallel Conductors:
Consider two infinitely long, straight, parallel conductors **Wire 1** and **Wire 2** separated by a perpendicular distance $r$, carrying steady currents $I_1$ and $I_2$ respectively in the same upward direction.

1. **Magnetic Field Produced by Wire 1 at Wire 2:**
   According to Ampere's Circuital Law, the current $I_1$ establishes a cylindrical magnetic field. The magnitude of the field $\vec{B}_1$ at the location of Wire 2 is:
   $$B_1 = \frac{\mu_0 I_1}{2\pi r}$$
   By the Right-Hand Grip Rule, the direction of $\vec{B}_1$ at Wire 2 points perpendicularly **into the plane of the paper** ($\otimes$).

2. **Force Experienced by Wire 2:**
   Wire 2 carrying current $I_2$ lies situated in this external magnetic field $\vec{B}_1$ at an angle $\theta = 90^\circ$. The force acting on a segment of length $L$ of Wire 2 is:
   $$F_2 = I_2 L B_1 \sin 90^\circ = I_2 L \left(\frac{\mu_0 I_1}{2\pi r}\right)$$
   
   Rearranging gives the force per unit length ($f = F/L$):
   $$\boxed{\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r}}$$

3. **Nature and Direction of Force:**
   Applying **Fleming's Left-Hand Rule** to Wire 2 (field $\vec{B}_1$ inwards, current $I_2$ upwards), the resulting force vector points horizontally **towards Wire 1** (to the left).
   By Newton's Third Law, Wire 1 experiences an equal and opposite force directed towards Wire 2. Thus, parallel currents flowing in the **same direction attract each other**.

#### Standard Definition of One Ampere:
Let $I_1 = I_2 = 1\text{ A}$ and the separation distance $r = 1\text{ m}$ in a vacuum. Substituting the value of $\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$:
$$\frac{F}{L} = \frac{(4\pi \times 10^{-7}) \times 1 \times 1}{2\pi \times 1} = 2 \times 10^{-7}\text{ N/m}$$

> **Official SI Definition:** **One Ampere** is defined as the value of that constant current which, if maintained in two straight parallel conductors of infinite length and negligible circular cross-section, placed one meter apart in a vacuum, would produce between these conductors a force equal to exactly $2 \times 10^{-7}\text{ Newtons per meter}$ of length.
</details>

---

### Q 3.3 ⭐⭐⭐
State Biot-Savart's law. Derive an expression for the magnetic field at the center of a circular coil of $N$-turns carrying current $I$.

<details>
<summary><b>Solution</b></summary>

#### Statement of Biot-Savart Law:
The Biot-Savart Law states that the magnetic field contribution $d\vec{B}$ at a point $P$ due to an infinitesimal current element $I d\vec{l}$ is directly proportional to the current $I$, the element length $dl$, the sine of the angle $\theta$ between the element vector and the position vector $\vec{r}$, and inversely proportional to the square of the distance $r$ from the element to the point.
$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I (d\vec{l} \times \hat{r})}{r^2} \implies dB = \frac{\mu_0}{4\pi} \frac{I dl \sin\theta}{r^2}$$
*(where $\mu_0/(4\pi) = 10^{-7}\text{ T}\cdot\text{m/A}$ is the magnetic constant in vacuum)*

#### Derivation of Field at Center of a Circular Loop:
Consider a circular conducting loop of radius $R$ carrying a steady current $I$. We wish to determine the total magnetic field $B$ at its geometric center $O$.

1. **Infinitesimal Element Contribution:**
   Choose a small current element $d\vec{l}$ along the circumference. The position vector $\vec{r}$ directed from the element to the center $O$ lies along the radius. Since the tangent to a circle is always perpendicular to its radius:
   $$d\vec{l} \perp \vec{r} \implies \theta = 90^\circ$$
   
   Applying the Biot-Savart formula:
   $$dB = \frac{\mu_0}{4\pi} \frac{I dl \sin 90^\circ}{R^2} = \frac{\mu_0 I}{4\pi R^2} dl$$

2. **Integration over the Complete Loop:**
   By the Right-Hand Grip Rule, the magnetic field vectors produced by all infinitesimal elements around the perimeter point in the exact same direction at the center (perpendicularly out of or into the plane). Thus, the total scalar field is simply the direct integral over the circumference:
   $$B = \int dB = \frac{\mu_0 I}{4\pi R^2} \int_{0}^{2\pi R} dl$$
   
   Evaluating the integral ($\int dl = \text{Circumference} = 2\pi R$):
   $$B = \frac{\mu_0 I}{4\pi R^2} (2\pi R) = \frac{\mu_0 I}{2R}$$

3. **Extension to a Multi-turn Coil:**
   If the circular coil consists of $N$ tightly wound identical turns, each turn contributes an equal magnetic field.
   $$\boxed{B = \frac{\mu_0 N I}{2R}}$$
</details>

---

### Q 3.4 ⭐⭐
What is a radial magnetic field?<br> How is it obtained in a moving coil galvanometer?<br>

<details>
<summary><b>Solution</b></summary>

#### Definition of a Radial Magnetic Field:
A **radial magnetic field** is a tailored magnetic field configuration where the magnetic field lines always point along the radius of the cylindrical region enclosing the rotating armature. 

**Operational Significance:** Regardless of the angular orientation of the coil as it deflects, the plane of the coil always remains perfectly parallel to the magnetic field lines. Consequently, the normal vector to the coil surface maintains a constant perpendicular angle ($\theta = 90^\circ$) relative to the field vector at all positions.
$$\tau = NIAB\sin 90^\circ = NIAB \implies \text{Torque becomes independent of rotation angle}$$
This structural design ensures a perfectly **linear scale** ($\phi \propto I$).

#### How it is Obtained Practically:
A radial magnetic field is engineered inside a moving coil galvanometer by combining two specific design elements:
1. **Concave Cylindrical Pole Pieces:** The permanent magnet pole pieces (North and South) are hollowed out and shaped into highly polished concave circular arcs.
2. **Stationary Soft Iron Core:** A highly permeable, unmagnetized soft iron cylindrical core is mounted symmetrically exactly at the center of the rotating coil (without touching the rotating frame). 

The high magnetic permeability of the soft iron core dramatically concentrates the magnetic lines of force, pulling them radially straight across the narrow air gap ensuring they cross the vertical arms of the coil at perfect right angles.
</details>

---

### Q 3.5 ⭐⭐
A closely wound solenoid $80\text{ cm}$ long has $5$ layers of windings of $400$ turns each. The diameter of the solenoid is $1.8\text{ cm}$. If the current carried is $8.0\text{ A}$, estimate the magnitude of $\vec{B}$ inside the solenoid near its centre.

<details>
<summary><b>Solution</b></summary>

**1. Extract Given Data:**
- Total length of solenoid ($L$) = $80\text{ cm} = 0.8\text{ m}$
- Diameter ($D$) = $1.8\text{ cm}$ *(Since $D \ll L$, the solenoid can be safely approximated as an ideal long solenoid where edge effects are negligible)*
- Total turns ($N$) = $\text{Layers} \times \text{Turns per layer} = 5 \times 400 = 2000\text{ turns}$
- Operating current ($I$) = $8.0\text{ A}$

**2. Calculate Turn Density ($n$):**
The number of turns per unit length along the axial core is:
$$n = \frac{N}{L} = \frac{2000}{0.8\text{ m}} = 2500\text{ turns/meter}$$

**3. Apply Ideal Solenoid Formula:**
The uniform axial magnetic field deep inside a long solenoid near its center is given by:
$$B = \mu_0 n I$$
Substituting the fundamental constants ($\mu_0 = 4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}$):
$$B = (4\pi \times 10^{-7}) \times 2500 \times 8.0$$

$$B = 4\pi \times 10^{-7} \times 20000 = 8\pi \times 10^{-3}\text{ Tesla}$$

Using $\pi \approx 3.14159$:
$$B \approx 8 \times 3.14159 \times 10^{-3} \approx 2.513 \times 10^{-2}\text{ T}$$

$$\boxed{B \approx 2.51 \times 10^{-2}\text{ T}}$$
</details>

---

### Q 3.6 ⭐⭐⭐
A square coil of side $10\text{ cm}$ consists of $20$ turns and carries a current of $12\text{ A}$. The coil is suspended vertically and the normal to the plane of the coil makes an angle of $30^\circ$ with the direction of a uniform horizontal magnetic field of magnitude $0.80\text{ T}$. What is the magnitude of torque experienced by the coil?<br>

<details>
<summary><b>Solution</b></summary>

**1. Extract Given Parameters:**
- Side length of square coil ($a$) = $10\text{ cm} = 0.1\text{ m}$
- Area of the coil ($A$) = $a^2 = (0.1)^2 = 0.01\text{ m}^2$
- Total number of turns ($N$) = $20$
- Current ($I$) = $12\text{ A}$
- Magnetic field strength ($B$) = $0.80\text{ T}$
- Angle between the **normal vector** to the coil and the magnetic field ($\theta$) = $30^\circ$

**2. Torque Formula:**
The vector torque on a magnetic dipole $\vec{M} = NIA\hat{n}$ in an external field is $\vec{\tau} = \vec{M} \times \vec{B}$. The scalar magnitude is:
$$\tau = NIAB\sin\theta$$

**3. Direct Substitution:**
$$\tau = 20 \times 12 \times 0.01 \times 0.80 \times \sin 30^\circ$$

Knowing that $\sin 30^\circ = 0.5$:
$$\tau = 2.4 \times 0.80 \times 0.5 = 1.92 \times 0.5 = 0.96\text{ N}\cdot\text{m}$$

$$\boxed{\tau = 0.96\text{ N}\cdot\text{m}}$$
The square coil experiences a deflecting torque of exactly $0.96\text{ N}\cdot\text{m}$.
</details>

---

## Long Answer Questions (5 Marks)

### Q 5.1 ⭐⭐⭐
1. Draw a neat, labelled diagram of a moving coil galvanometer. Explain its underlying working principle. Prove that when suspended in a radial magnetic field, the deflection of the coil is directly proportional to the current flowing through it.
2. Explain how a galvanometer with resistance $G$ and full-scale deflection current $I_g$ can be converted into a voltmeter of range $0$ to $V$ volts. Derive the expression for the required series resistance.

<details>
<summary><b>Solution</b></summary>

#### Part 1: The Moving Coil Galvanometer

**Working Principle:**
A moving coil galvanometer operates on the fundamental electrodynamic principle that a current-carrying loop placed in an external magnetic field experiences a mechanical deflecting torque.

**Labelled Structural Elements:**
- **Coil:** Tightly wound rectangular frame of insulated copper wire.
- **Suspension Strip:** Fine phosphor-bronze strip providing restoring torque and acting as the current lead-in.
- **Radial Magnets:** Concave soft-iron cylindrical pole pieces producing a radial field.
- **Core:** Symmetrical internal soft-iron cylinder enhancing field intensity.
- **Hairspring:** Lower helical spring providing the exit electrical terminal.
- **Mirror/Pointer:** Attached system to measure fine angular displacement.

```
       [Phosphor Bronze Suspension Strip]
                      |
                   (Mirror)
                      |
       /---------\    |    /---------\
      |           | +---+ |           |
      |  NORTH    | |(O)| |   SOUTH   |
      |  POLE     | |Core |  POLE     |
      | (Concave) | +---+ | (Concave) |
       \---------/    |    \---------/
                      |
              [Lower Hairspring]
```

**Proof of Linear Deflection Scale:**
Let the rectangular coil have length $L$, breadth $b$, and total turns $N$. Enclosed Area $A = L \cdot b$.
When a steady current $I$ passes through the coil, the vertical sides experience equal and opposite magnetic forces producing a deflecting couple.

In a **radial magnetic field**, the magnetic field lines remain parallel to the plane of the coil in all orientations. Therefore, the angle between the normal to the coil and the field vector is always $\theta = 90^\circ$.
$$\text{Deflecting Torque } (\tau_d) = NIAB\sin 90^\circ = NIAB$$

As the coil rotates through an angle $\phi$, the upper suspension wire twists, developing an internal elastic restoring torque. Let $k$ be the restoring torque per unit twist (torsional constant).
$$\text{Restoring Torque } (\tau_r) = k\phi$$

At mechanical equilibrium, the deflecting torque exactly balances the restoring torque:
$$\tau_d = \tau_r \implies NIAB = k\phi$$

Rearranging for the deflection angle $\phi$:
$$\phi = \left(\frac{NAB}{k}\right) I$$

Since the parameters $N, A, B,$ and $k$ are strictly constant for a manufactured instrument, we can define the **Galvanometer Constant** $G_c = \frac{k}{NAB}$.
$$\phi \propto I$$
Thus, the deflection angle is strictly proportional to the current, allowing the scale to be marked off in uniform, linear divisions.

---

#### Part 2: Conversion of Galvanometer into a Voltmeter

A voltmeter is designed to measure potential differences across circuit components. To avoid drawing substantial current from the circuit under test (which would alter the true voltage drop), an ideal voltmeter must possess an infinitely high internal resistance.

**Circuit Setup:**
To convert a sensitive galvanometer into a high-range voltmeter capable of reading up to $V$ volts, a highly stable **series resistance ($R$)** is connected directly in series with the galvanometer coil.

```
         R (High Series Resistor)       G (Galvanometer Coil)
  o------------[   ]--------------------------( ^ )------------o
  |+                                                      -|
  |<----------------------- V Volts ---------------------->|
```

**Derivation of Series Resistance Formula:**
Let $G$ be the internal resistance of the galvanometer coil.
Let $I_g$ be the maximum safe current required to drive the pointer to full-scale deflection.
When connected across a maximum test voltage $V$, the total series resistance of the combined instrument is:
$$R_{\text{total}} = R + G$$

By Ohm's Law, the total current flowing through the branch must be restricted exactly to $I_g$:
$$I_g = \frac{V}{R + G}$$

Rearranging to isolate the unknown series resistance $R$:
$$R + G = \frac{V}{I_g}$$

$$\boxed{R = \frac{V}{I_g} - G}$$

By selecting a high-precision resistor matching this exact theoretical value, the galvanometer scale can be successfully calibrated to read directly in volts.
</details>

---

### Q 5.2 ⭐⭐⭐
What is a cyclotron?<br> Explain its core working principle with a conceptual schematic diagram. Show mathematically that the frequency of revolution of a charged particle inside a cyclotron is completely independent of its velocity or orbital radius. Obtain the expression for the maximum kinetic energy attained by the accelerated ions.

<details>
<summary><b>Solution</b></summary>

#### Device Definition and Working Principle:
A **cyclotron** is a specialized particle accelerator utilized to accelerate heavy charged particles (such as protons, deuterons, and alpha particles) to extremely high kinetic energies.

**Core Operating Principle:** 
A charged particle can be systematically accelerated to highly energetic states by passing it repeatedly through a relatively moderate, alternating high-frequency electric field, while a strong, perpendicular static magnetic field forces the particle to travel in expanding circular orbits, ensuring it re-crosses the accelerating gap in perfect synchronization.

#### Conceptual Diagram:
```
           High Frequency Alternating Oscillator (H.F.O.)
                       |                   |
                       +---------+---------+
                                 |
           +---------------------+---------------------+
           |    Dee 1 (D1)       |       Dee 2 (D2)    |
           |   /-------------\   |      /-------------\   |
           |  |               |  |     |               |  |
           |  |    +--->------+  |     |  +------<---+ |  |
           |  |   /           |  | Gap |  |           \ |  |
           |  |  |     (S)----+--+-----+--+            || |
           |  |   \           |        |  |           / |  |
           |  |    +---<------+        |  +------>---+  | |
           |   \-------------/          \-------------/   |
           +---------------------------------------------+
               [Uniform Static Magnetic Field Perpendicular Outwards]
```

#### Mathematical Proof of Frequency Independence:
Consider a particle of mass $m$ and charge $q$ injected at the central source $S$. Inside the hollow metallic dees, the electric field is completely shielded ($E=0$), leaving only the perpendicular magnetic field $B$ active.

1. **Radius of Orbital Path:**
   The perpendicular magnetic field exerts a centripetal force driving the particle in a semicircle of radius $r$ at velocity $v$:
   $$qvB = \frac{mv^2}{r} \implies r = \frac{mv}{qB}$$

2. **Time Spent Inside a Single Dee:**
   The time $t$ required to complete exactly one semicircular transit inside a single dee is:
   $$t = \frac{\text{Semicircular Path Length}}{\text{Orbital Velocity}} = \frac{\pi r}{v}$$
   
   Substituting the radius relation into this time equation:
   $$t = \frac{\pi}{v} \left(\frac{mv}{qB}\right) = \frac{\pi m}{qB}$$

3. **Total Time Period and Cyclotron Frequency:**
   The total time period $T$ for one complete full circular orbit across both dees is:
   $$T = 2t = \frac{2\pi m}{qB}$$
   
   The rotational frequency of the particle (Cyclotron Frequency $f_c$) is the reciprocal of the time period:
   $$\boxed{f_c = \frac{1}{T} = \frac{qB}{2\pi m}}$$

**Crucial Deduction:** The velocity variable $v$ and radius variable $r$ have completely cancelled out of the final equation! As the particle gains speed crossing the electric gap, its orbital radius expands proportionally, ensuring the time spent inside the dees remains strictly constant. This guarantees permanent **resonance** with the fixed frequency of the driving oscillator.

#### Derivation of Maximum Kinetic Energy:
The particle reaches its maximum attainable velocity $v_{\text{max}}$ right at the outer perimeter of the dees, characterized by the maximum physical exit radius $R_{\text{max}}$.
$$v_{\text{max}} = \frac{q B R_{\text{max}}}{m}$$

The maximum kinetic energy of the emerging beam is:
$$K.E._{\text{max}} = \frac{1}{2} m v_{\text{max}}^2 = \frac{1}{2} m \left(\frac{q B R_{\text{max}}}{m}\right)^2$$

$$\boxed{K.E._{\text{max}} = \frac{q^2 B^2 R_{\text{max}}^2}{2m}}$$
</details>

---

### Q 5.3 ⭐⭐⭐
For a circular coil of radius $R$ and $N$ turns carrying current $I$, the magnitude of the magnetic field at a point on its central axis at a distance $x$ from its centre is given by:
$$B = \frac{\mu_0 I R^2 N}{2(x^2 + R^2)^{3/2}}$$

1. Show mathematically that this general formula reduces correctly to the standard expression for the magnetic field at the center of the coil.
2. **Helmholtz Coils Configuration:** Consider two identical parallel coaxial circular coils of equal radius $R$ and number of turns $N$, carrying equal currents in the same circulation direction, separated axially by a distance exactly equal to their radius $R$. Show that the magnetic field along the axis in the immediate vicinity of the midpoint between the two coils is nearly uniform.

<details>
<summary><b>Solution</b></summary>

#### Part 1: Reduction to Center Field
To determine the field exactly at the geometric center of the circular coil, the axial measurement distance $x$ is set to zero ($x = 0$).
Substituting $x = 0$ into the axial formula:
$$B_{\text{center}} = \frac{\mu_0 I R^2 N}{2(0^2 + R^2)^{3/2}} = \frac{\mu_0 I R^2 N}{2(R^2)^{3/2}} = \frac{\mu_0 I R^2 N}{2R^3}$$

Simplifying the powers of $R$:
$$\boxed{B_{\text{center}} = \frac{\mu_0 N I}{2R}}$$
This confirms complete mathematical agreement with the direct Biot-Savart derivation for a simple loop center.

---

#### Part 2: Uniformity of Field in Helmholtz Coils

**System Configuration Geometry:**
Let the common central axis lie along the X-axis. Place the origin exactly at the central midpoint between the two identical parallel coils.
- **Coil 1** is positioned at $x = -\frac{R}{2}$.
- **Coil 2** is positioned at $x = +\frac{R}{2}$.

Both coils carry parallel currents, meaning their magnetic field vectors point in the identical positive axial direction.

```
       Coil 1 (-R/2)          Midpoint (0)          Coil 2 (+R/2)
           |                       |                       |
           |                       |x=d                    |
  ---------+-----------------------+--*--------------------+--------- Axial core
           |<--------- R/2 -------->|<-------- R/2 -------->|
```

Let us evaluate the total superposed magnetic field at a nearby target point $P$ located at a small axial displacement $x = d$ from the central origin, where $d \ll R$.

1. **Distance Parameters from Point $P$ to Each Coil:**
   - Axial distance from Coil 1 to point $P$: $x_1 = \frac{R}{2} + d$
   - Axial distance from Coil 2 to point $P$: $x_2 = \frac{R}{2} - d$

2. **Field Contribution from Coil 1 ($B_1$):**
   $$B_1 = \frac{\mu_0 N I R^2}{2\left[\left(\frac{R}{2} + d\right)^2 + R^2\right]^{3/2}}$$
   Expanding the inner square term:
   $$\left(\frac{R}{2} + d\right)^2 + R^2 = \frac{R^2}{4} + d^2 + Rd + R^2 = \frac{5R^2}{4} + d^2 + Rd$$
   Since $d$ is extremely small compared to $R$ ($d \ll R$), the second-order infinitesimal term $d^2$ can be safely neglected:
   $$\approx \frac{5R^2}{4} + Rd = \frac{5R^2}{4} \left(1 + \frac{4d}{5R}\right)$$
   
   Substituting back into the field equation:
   $$B_1 \approx \frac{\mu_0 N I R^2}{2 \left(\frac{5R^2}{4}\right)^{3/2} \left(1 + \frac{4d}{5R}\right)^{3/2}} = \frac{\mu_0 N I R^2}{2 \left(\frac{5}{4}\right)^{3/2} R^3} \left(1 + \frac{4d}{5R}\right)^{-3/2}$$

3. **Field Contribution from Coil 2 ($B_2$):**
   Following the exact corresponding steps for distance $x_2 = \frac{R}{2} - d$:
   $$B_2 \approx \frac{\mu_0 N I R^2}{2 \left(\frac{5}{4}\right)^{3/2} R^3} \left(1 - \frac{4d}{5R}\right)^{-3/2}$$

4. **Superposition and Binomial Expansion:**
   The total magnetic field $B_{\text{total}}$ at point $P$ is the direct sum $B_1 + B_2$. Factoring out common constants:
   $$B_{\text{total}} = \frac{\mu_0 N I}{2R \left(\frac{5}{4}\right)^{3/2}} \left[\left(1 + \frac{4d}{5R}\right)^{-3/2} + \left(1 - \frac{4d}{5R}\right)^{-3/2}\right]$$
   
   Applying the first-order Binomial Approximation $(1 \pm \epsilon)^{-n} \approx 1 \mp n\epsilon$:
   $$\left(1 + \frac{4d}{5R}\right)^{-3/2} \approx 1 - \frac{3}{2}\left(\frac{4d}{5R}\right) = 1 - \frac{6d}{5R}$$
   $$\left(1 - \frac{4d}{5R}\right)^{-3/2} \approx 1 + \frac{3}{2}\left(\frac{4d}{5R}\right) = 1 + \frac{6d}{5R}$$
   
   Summing the two expanded bracketed terms:
   $$\left(1 - \frac{6d}{5R}\right) + \left(1 + \frac{6d}{5R}\right) = 2$$
   *(Notice how the positive and negative linear displacement terms containing $d$ cancel out perfectly!)*

5. **Final Uniform Field Evaluation:**
   $$B_{\text{total}} \approx \frac{\mu_0 N I}{2R \left(\frac{5}{4}\right)^{3/2}} \times 2 = \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R}$$
   
   Evaluating the numerical scaling factor:
   $$\left(\frac{4}{5}\right)^{3/2} = (0.8)^{1.5} \approx 0.7155 \approx 0.72$$

   $$\boxed{B_{\text{total}} \approx 0.72 \frac{\mu_0 N I}{R}}$$

**Conclusion:** Since the final expression contains no dependency on the variable displacement coordinate $d$, the axial magnetic field remains incredibly constant and uniform over a considerable spatial window centered between the two parallel coils.
</details>

---

*← [Back to Chapter Preface](../00_preface.md)*
