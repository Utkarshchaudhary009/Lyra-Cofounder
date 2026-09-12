# Trigonometric Integrals — 07: Mixed Mastery

> **Final checklist:** Stop asking “Which chapter type is this?” and start asking “What is the easiest transformation from here to something I know?”

## The complete mental model

When a fresh integral appears, run the whole checklist:

### The 7-question scan

**1. What family is it?**

Sin/cos powers? Tan/sec? Cot/cosec? Fraction? Mixed?

**2. Is there a derivative pair already visible?**

Look for

$$\cos x\,dx,\quad \sin x\,dx,\quad \sec^2x\,dx,\quad \cosec^2x\,dx,\quad \sec x\tan x\,dx,\quad \cosec x\cot x\,dx.$$

**3. Can I choose `u` and preserve its derivative?**

**4. If the derivative is missing, can an identity create it?**

**5. Are odd/even powers telling me what to preserve?**

**6. Can I simplify the expression into a standard form?**

**7. After one transformation, does the integral look obvious?**

> **Golden rule:** Do not use a complicated method while a simpler structural move is available.

---

# Level 0 — Strategy only

For each question, identify the **first move**. Do not integrate yet.

### Question 1

$$\int \sin^5x\cos^2x\,dx$$

<details>
<summary>Answer</summary>

Sin-cos power family.

Sine has an odd power, so the first investigation is:

> Preserve one `sin x` and convert the remaining even sine power.

</details>

### Question 2

$$\int \frac{\cos x}{4+\sin x}\,dx$$

<details>
<summary>Answer</summary>

Derivative-pair pattern.

The denominator's derivative is `cos x`, so:

$$u=4+\sin x.$$

</details>

### Question 3

$$\int \sin^2x\,dx$$

<details>
<summary>Answer</summary>

Both the visible structure and derivative scan suggest no useful substitution pair.

First move: **power reduction**.

</details>

### Question 4

$$\int \frac{1-\cos^2x}{\sin x}\,dx$$

<details>
<summary>Answer</summary>

Simplify first:

$$1-\cos^2x=\sin^2x.$$

Then the integrand becomes `sin x`, which is standard.

</details>

---

# Level 1 — Guided mixed practice

### Question 5

Evaluate

$$\int \sin^3x\cos^4x\,dx.$$

<details>
<summary>Answer</summary>

Sine has odd power, so preserve one sine:

$$\int \sin^2x\cos^4x\sin x\,dx.$$

Convert

$$\sin^2x=1-\cos^2x.$$

Thus

$$\int(1-\cos^2x)\cos^4x\sin x\,dx.$$

Let

$$u=\cos x,\qquad du=-\sin x\,dx.$$

Then

$$-\int(1-u^2)u^4du$$

$$=-\int(u^4-u^6)du.$$

Therefore

$$\boxed{-\frac{\cos^5x}{5}+\frac{\cos^7x}{7}+C}.$$

</details>

### Question 6

Evaluate

$$\int \tan^3x\sec^2x\,dx.$$

<details>
<summary>Answer</summary>

The derivative pair is already present:

$$u=\tan x,\qquad du=\sec^2x\,dx.$$

Hence

$$\int u^3du=\boxed{\frac{\tan^4x}{4}+C}.$$

</details>

### Question 7

Evaluate

$$\int \frac{\sin x}{3-\cos x}\,dx.$$

<details>
<summary>Answer</summary>

Take

$$u=3-\cos x.$$

Then

$$du=\sin x\,dx.$$

So

$$\boxed{\ln|3-\cos x|+C}.$$

</details>

---

# Level 2 — Competing methods

### Question 8

Evaluate

$$\int \sin x\cos x\,dx.$$

<details>
<summary>Answer</summary>

Two reasonable methods exist.

**Method 1 — substitution:**

$$u=\sin x,\quad du=\cos x\,dx,$$

so

$$\boxed{\frac{\sin^2x}{2}+C}.$$

**Method 2 — identity:**

$$\sin x\cos x=\frac12\sin2x,$$

giving the same answer.

The lesson is not “memorise one method.” It is:

> Choose the route with the least unnecessary work.

</details>

### Question 9

Evaluate

$$\int \tan^2x\,dx.$$

<details>
<summary>Answer</summary>

Convert to a standard form:

$$\tan^2x=\sec^2x-1.$$

Therefore

$$\boxed{\tan x-x+C}.$$

</details>

### Question 10

Evaluate

$$\int \frac{\cos^2x}{\sin x}\,dx.$$

<details>
<summary>Answer</summary>

Simplify first:

$$\frac{\cos^2x}{\sin x}
=\frac{1-\sin^2x}{\sin x}
=\cosec x-\sin x.$$

Therefore

$$\boxed{\ln|\cosec x-\cot x|+\cos x+C}.$$

</details>

---

# Level 3 — No method is named

### Question 11

Evaluate

$$\int \frac{\sec^2x}{2+\tan x}\,dx.$$

<details>
<summary>Answer</summary>

The denominator is the inside function:

$$u=2+\tan x.$$

Since

$$du=\sec^2x\,dx,$$

we get

$$\boxed{\ln|2+\tan x|+C}.$$

</details>

### Question 12

Evaluate

$$\int \cos^5x\,dx.$$

<details>
<summary>Answer</summary>

Cosine has odd power, so preserve one cosine:

$$\int\cos^4x\cos x\,dx.$$

Convert

$$\cos^2x=1-\sin^2x,$$

so

$$\cos^4x=(1-\sin^2x)^2.$$

Take

$$u=\sin x,\qquad du=\cos x\,dx.$$

Then

$$\int(1-u^2)^2du
=\int(1-2u^2+u^4)du.$$

Therefore

$$\boxed{\sin x-\frac{2\sin^3x}{3}+\frac{\sin^5x}{5}+C}.$$

</details>

### Question 13

Evaluate

$$\int \sin^4x\,dx.$$

<details>
<summary>Answer</summary>

Both the power pattern and substitution scan say: do **not** force a derivative pair.

Use

$$\sin^2x=\frac{1-\cos2x}{2}.$$

Then

$$\sin^4x=\left(\frac{1-\cos2x}{2}\right)^2.$$

After expanding and reducing `cos²2x`,

$$\boxed{\frac{3x}{8}-\frac{\sin2x}{4}+\frac{\sin4x}{32}+C}.$$

</details>

---

# Level 4 — NCERT-to-JEE transition

These are designed to test **choice of route**, not just algebra.

### Question 14

Evaluate

$$\int \frac{\sin x}{1+\cos x}\,dx.$$

<details>
<summary>Answer</summary>

Two useful observations exist:

$$u=1+\cos x$$

gives

$$du=-\sin x\,dx.$$

Hence

$$\boxed{-\ln|1+\cos x|+C}.$$

The key is noticing the denominator before trying identities.

</details>

### Question 15

Evaluate

$$\int \frac{1+\sin x}{\cos x}\,dx.$$

<details>
<summary>Answer</summary>

Simplify first:

$$\frac{1+\sin x}{\cos x}=\sec x+\tan x.$$

Then integrate standard forms:

$$\boxed{\ln|\sec x+\tan x|+\ln|\sec x|+C}.$$

</details>

### Question 16

Evaluate

$$\int \frac{\tan x}{1+\sec x}\,dx.$$

<details>
<summary>Answer</summary>

Rewrite in sine/cosine:

$$\frac{\tan x}{1+\sec x}
=\frac{\sin x}{1+\cos x}.$$

Now use

$$u=1+\cos x,\qquad du=-\sin x\,dx.$$

Therefore

$$\boxed{-\ln|1+\cos x|+C}.$$

The hard part was not integration. It was **choosing the useful representation**.

</details>

---

# Level 5 — Final challenge set

Do these without looking at the answer until you have written down your planned method.

### Question 17

$$\int \sin^3x\cos^3x\,dx$$

<details>
<summary>Answer</summary>

Both powers are odd, so either factor can be preserved. Preserve one sine:

$$\sin^3x\cos^3x
=\sin^2x\cos^3x\sin x.$$

Use

$$\sin^2x=1-\cos^2x,$$

then `u = cos x`.

So

$$-\int(1-u^2)u^3du
=-\int(u^3-u^5)du.$$

Hence

$$\boxed{-\frac{\cos^4x}{4}+\frac{\cos^6x}{6}+C}.$$

</details>

### Question 18

$$\int \frac{\cos x}{(2+\sin x)^5}\,dx$$

<details>
<summary>Answer</summary>

Derivative pair:

$$u=2+\sin x,\qquad du=\cos x\,dx.$$

Then

$$\int u^{-5}du
=-\frac{1}{4u^4}+C.$$

Therefore

$$\boxed{-\frac{1}{4(2+\sin x)^4}+C}.$$

</details>

### Question 19

$$\int \frac{1-\sin^2x}{\cos x}\,dx$$

<details>
<summary>Answer</summary>

Simplify the numerator:

$$1-\sin^2x=\cos^2x.$$

So

$$\frac{\cos^2x}{\cos x}=\cos x.$$

Therefore

$$\boxed{\sin x+C}.$$

This is a reminder that **simplification can beat every fancy technique**.

</details>

### Question 20

$$\int \sin^2x\cos^2x\,dx$$

<details>
<summary>Answer</summary>

Both powers are even, so use power reduction.

$$\sin^2x\cos^2x=\frac14\sin^22x.$$

Then

$$\sin^22x=\frac{1-\cos4x}{2}.$$

Thus

$$\boxed{\frac{x}{8}-\frac{\sin4x}{32}+C}.$$

</details>

---

# The final exam-room algorithm

When the clock is running, compress the whole book into this:

$$\boxed{
\begin{array}{c}
\text{IDENTIFY}\
\downarrow\\
\text{DERIVATIVE PAIR?}\
\downarrow\\
\text{PRESERVE / MANUFACTURE }du\
\downarrow\\
\text{ODD-EVEN POWER CHECK}\
\downarrow\\
\text{IDENTITY / SIMPLIFY}\
\downarrow\\
\text{STANDARD FORM}
\end{array}}
$$

## The one question that prevents random solving

Before every serious step, ask:

> **“What do I want the integral to look like next?”**

That question is the real skill.

You are not memorising a bag of tricks. You are learning to **reshape a problem until the answer becomes visible**.

---

## Mastery test

You are ready to leave this book when, for a fresh integral, you can do three things **before calculating**:

1. Name the visible structure.
2. Predict the first transformation.
3. Explain why that transformation helps.

If you can do those three, the algebra becomes the easy part.
