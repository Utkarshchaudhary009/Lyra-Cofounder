# Trigonometric Integrals — 04: Identities as Transformations

> **Checklist #4:** An identity is not a formula to deploy randomly. It is a machine for changing the shape of an integral.

## The mental model

Two expressions can look completely different and still be exactly equal.

For example,

$$1-\sin^2x=\cos^2x.$$

When integrating, the useful question is:

> **“Which form gives me the derivative or standard pattern I need?”**

So an identity is a **change of language**.

---

## The three transformation rules you need first

$$\sin^2x+\cos^2x=1$$

$$1+\tan^2x=\sec^2x$$

$$1+\cot^2x=\cosec^2x$$

Derived forms are often more useful:

$$1-\sin^2x=\cos^2x$$

$$\sec^2x-1=\tan^2x$$

$$\cosec^2x-1=\cot^2x.$$

---

## Checklist #4

Before using an identity, state the destination:

> “I am converting this part because I want __________.”

Typical destinations:

- create `sin x dx` or `cos x dx`;
- create `sec²x dx` or `cosec²x dx`;
- reduce a power;
- turn a mixed expression into one trig function;
- reach a standard integral.

If you cannot explain why the identity helps, **do not use it yet.**

---

## Level 0 — Transformation only

### Question 1

Rewrite

$$\sin^2x$$

in terms of `cos x`.

<details>
<summary>Answer</summary>

From

$$\sin^2x+\cos^2x=1,$$

we get

$$\boxed{\sin^2x=1-\cos^2x}.$$

</details>

### Question 2

Rewrite

$$\tan^2x$$

in terms of `sec x`.

<details>
<summary>Answer</summary>

$$1+\tan^2x=\sec^2x$$

gives

$$\boxed{\tan^2x=\sec^2x-1}.$$

</details>

### Question 3

Rewrite

$$\cot^2x$$

in terms of `cosec x`.

<details>
<summary>Answer</summary>

$$\boxed{\cot^2x=\cosec^2x-1}.$$

</details>

---

## Level 1 — Identity creates a derivative

### Question 4

Explain why

$$\cos^3x=\cos^2x\cos x$$

is useful while integrating.

<details>
<summary>Answer</summary>

Because it isolates

$$\cos x\,dx,$$

which is the derivative of `sin x`.

The remaining `cos²x` can then be converted using

$$\cos^2x=1-\sin^2x.$$

So the rewrite is useful because it **creates the substitution pair**.

</details>

### Question 5

Evaluate

$$\int \cos^3x\,dx.$$

<details>
<summary>Answer</summary>

Use the transformation with a clear destination: create `cos x dx`.

$$\int\cos^3x\,dx
=\int \cos^2x\cos x\,dx$$

$$=\int(1-\sin^2x)\cos x\,dx.$$

Let

$$u=\sin x,\qquad du=\cos x\,dx.$$

Then

$$\int(1-u^2)du=u-\frac{u^3}{3}+C.$$

Therefore

$$\boxed{\sin x-\frac{\sin^3x}{3}+C}.$$

</details>

---

## Level 2 — Identity chooses the integration language

### Question 6

Evaluate

$$\int \tan^2x\,dx.$$

<details>
<summary>Answer</summary>

Convert into a simpler standard form:

$$\tan^2x=\sec^2x-1.$$

Therefore

$$\int\tan^2x\,dx
=\int(\sec^2x-1)dx$$

$$=\boxed{\tan x-x+C}.$$

The identity was used not to create substitution, but to convert the integral into **known standard pieces**.

</details>

### Question 7

Evaluate

$$\int \cot^2x\,dx.$$

<details>
<summary>Answer</summary>

Use

$$\cot^2x=\cosec^2x-1.$$

Then

$$\int\cot^2x\,dx
=\int(\cosec^2x-1)dx$$

$$=\boxed{-\cot x-x+C}.$$

</details>

---

## Level 3 — Double-angle as a simplifier

Sometimes there is no useful substitution pair. Then **change the power itself**.

The key identities are

$$\sin^2x=\frac{1-\cos2x}{2},$$

$$\cos^2x=\frac{1+\cos2x}{2}.$$

### Question 8

Evaluate

$$\int \sin^2x\,dx.$$

<details>
<summary>Answer</summary>

There is no derivative pair worth forcing.

So reduce the power:

$$\int\sin^2x\,dx
=\frac12\int(1-\cos2x)dx.$$

Thus

$$=\frac{x}{2}-\frac12\cdot\frac{\sin2x}{2}+C.$$

Therefore

$$\boxed{\frac{x}{2}-\frac{\sin2x}{4}+C}.$$

</details>

### Question 9

Evaluate

$$\int \cos^2x\,dx.$$

<details>
<summary>Answer</summary>

Use

$$\cos^2x=\frac{1+\cos2x}{2}.$$

So

$$\boxed{\frac{x}{2}+\frac{\sin2x}{4}+C}.$$

</details>

---

## Level 4 — Transformation + substitution

### Question 10

Evaluate

$$\int \sin^2x\cos x\,dx.$$

<details>
<summary>Answer</summary>

Here the derivative pair is already visible:

$$u=\sin x,\qquad du=\cos x\,dx.$$

No identity is needed.

Therefore

$$\boxed{\frac{\sin^3x}{3}+C}.$$

This is important: **do not transform something that is already in the form you need.**

</details>

### Question 11

Evaluate

$$\int \sin^2x\cos^3x\,dx.$$

<details>
<summary>Answer</summary>

We want `cos x dx`, because

$$d(\sin x)=\cos x\,dx.$$

Save one cosine:

$$\int\sin^2x\cos^2x\cos x\,dx.$$

Transform

$$\cos^2x=1-\sin^2x.$$

Then

$$\int\sin^2x(1-\sin^2x)\cos x\,dx.$$

Let

$$u=\sin x.$$

Hence

$$\int(u^2-u^4)du
=\boxed{\frac{\sin^3x}{3}-\frac{\sin^5x}{5}+C}.$$

</details>

---

## The transformation sentence

Before using an identity, say mentally:

> **“I am changing ______ into ______ because I need ______.”**

Example:

> “I am changing `cos²x` into `1 − sin²x` because I need `sin x` as my substitution variable.”

That is the difference between **using an identity** and **understanding why the identity is being used**.