# Trigonometric Integrals — 05: The Odd/Even Power Strategy

> **Checklist #5:** For products of powers of `sin` and `cos`, use odd/even powers to decide what to preserve and what to convert.

## The mental model

Consider

$$\int \sin^m x\cos^n x\,dx.$$

The powers are giving you information.

You are looking for one of the derivative pieces

$$\sin x\,dx \quad\text{or}\quad \cos x\,dx.$$

Then the other function's even powers can be converted using

$$\sin^2x+\cos^2x=1.$$

The classic strategy is:

- **Odd power of sine:** save one `sin x`; turn the remaining `sin²x` into `1 − cos²x`.
- **Odd power of cosine:** save one `cos x`; turn the remaining `cos²x` into `1 − sin²x`.
- **Both powers even:** there is no leftover single derivative factor, so power-reduction identities are usually better.

This is a strategy, not a law carved into stone. Always check the actual structure.

---

## Checklist #5

For

$$\int \sin^m x\cos^n x\,dx,$$

ask:

1. Is `m` odd?
2. Is `n` odd?
3. Which single factor should I preserve?
4. Can the rest become a polynomial in the chosen function?
5. If both are even, should I reduce the powers instead?

---

## Level 0 — Predict the move

### Question 1

For

$$\int \sin^5x\cos^2x\,dx,$$

which factor would you preserve: `sin x` or `cos x`?

<details>
<summary>Answer</summary>

Preserve **`sin x`** because the power of sine is odd.

Write

$$\sin^5x=\sin^4x\sin x=(\sin^2x)^2\sin x.$$

Then convert the even powers of sine into cosine terms.

</details>

### Question 2

For

$$\int \sin^2x\cos^7x\,dx,$$

which factor would you preserve?

<details>
<summary>Answer</summary>

Preserve **`cos x`** because the cosine power is odd.

</details>

### Question 3

For

$$\int \sin^4x\cos^6x\,dx,$$

would you immediately use the odd-power strategy?

<details>
<summary>Answer</summary>

No.

Both powers are even. There is no natural single `sin x` or `cos x` left to act as `du`.

So power-reduction identities are the more natural first investigation.

</details>

---

## Level 1 — One odd power

### Question 4

Evaluate

$$\int \sin^3x\cos^2x\,dx.$$

<details>
<summary>Answer</summary>

Sine has odd power, so preserve one sine:

$$\int \sin^2x\cos^2x\sin x\,dx.$$

Convert

$$\sin^2x=1-\cos^2x.$$

Then

$$\int (1-\cos^2x)\cos^2x\sin x\,dx.$$

Take

$$u=\cos x,\qquad du=-\sin x\,dx.$$

So

$$-\int (1-u^2)u^2du
= -\int(u^2-u^4)du.$$

Therefore

$$\boxed{-\frac{\cos^3x}{3}+\frac{\cos^5x}{5}+C}.$$

</details>

### Question 5

Evaluate

$$\int \sin^2x\cos^3x\,dx.$$

<details>
<summary>Answer</summary>

Cosine has odd power, so preserve one cosine:

$$\int\sin^2x\cos^2x\cos x\,dx.$$

Use

$$\cos^2x=1-\sin^2x.$$

Hence

$$\int\sin^2x(1-\sin^2x)\cos x\,dx.$$

Let

$$u=\sin x,\qquad du=\cos x\,dx.$$

Then

$$\int(u^2-u^4)du.$$

Thus

$$\boxed{\frac{\sin^3x}{3}-\frac{\sin^5x}{5}+C}.$$

</details>

---

## Level 2 — Higher powers

### Question 6

Evaluate

$$\int \sin^7x\cos^4x\,dx.$$

<details>
<summary>Answer</summary>

Save one sine:

$$\sin^7x=(\sin^2x)^3\sin x.$$

Convert

$$\sin^2x=1-\cos^2x.$$

So

$$\int(1-\cos^2x)^3\cos^4x\sin x\,dx.$$

Let

$$u=\cos x,\qquad du=-\sin x\,dx.$$

This becomes

$$-\int(1-u^2)^3u^4du.$$

Expand:

$$-\int(u^4-3u^6+3u^8-u^{10})du.$$

Therefore

$$\boxed{-\frac{u^5}{5}+\frac{3u^7}{7}-\frac{u^9}{3}+\frac{u^{11}}{11}+C}.$$

Substitute back:

$$\boxed{-\frac{\cos^5x}{5}+\frac{3\cos^7x}{7}-\frac{\cos^9x}{3}+\frac{\cos^{11}x}{11}+C}.$$

</details>

### Question 7

Evaluate

$$\int \sin^4x\cos^5x\,dx.$$

<details>
<summary>Answer</summary>

Save one cosine:

$$\int\sin^4x\cos^4x\cos x\,dx.$$

Convert

$$\cos^4x=(1-\sin^2x)^2.$$

Let

$$u=\sin x.$$

Then

$$\int u^4(1-u^2)^2du.$$

Expand:

$$\int(u^4-2u^6+u^8)du.$$

Hence

$$\boxed{\frac{\sin^5x}{5}-\frac{2\sin^7x}{7}+\frac{\sin^9x}{9}+C}.$$

</details>

---

## Level 3 — Both powers even

When both exponents are even, the derivative-pair strategy loses its advantage.

Use

$$\sin^2x=\frac{1-\cos2x}{2},\qquad
\cos^2x=\frac{1+\cos2x}{2}.$$

### Question 8

Evaluate

$$\int \sin^2x\cos^2x\,dx.$$

<details>
<summary>Answer</summary>

Use the product-to-double-angle relation obtained from the power identities:

$$\sin^2x\cos^2x
=\frac14\sin^22x.$$

Then

$$\int\sin^2x\cos^2x\,dx
=\frac14\int\sin^22x\,dx.$$

Now

$$\sin^22x=\frac{1-\cos4x}{2}.$$

Therefore

$$\frac18\int(1-\cos4x)dx
=\boxed{\frac{x}{8}-\frac{\sin4x}{32}+C}.$$

</details>

### Question 9

Evaluate

$$\int \sin^4x\,dx.$$

<details>
<summary>Answer</summary>

Both the power and its square are even, so reduce the power instead of forcing substitution.

Since

$$\sin^2x=\frac{1-\cos2x}{2},$$

we get

$$\sin^4x=\left(\frac{1-\cos2x}{2}\right)^2.$$

Expand and reduce `cos² 2x` again. The result is

$$\boxed{\frac{3x}{8}-\frac{\sin2x}{4}+\frac{\sin4x}{32}+C}.$$

</details>

---

## Level 4 — Mixed strategy decision

### Question 10

Which approach is more natural for

$$\int \sin^3x\cos^5x\,dx?$$

A. Power reduction immediately  
B. Preserve one sine  
C. Preserve one cosine  
D. Integration by parts

<details>
<summary>Answer</summary>

Both powers are odd, so **B and C are both possible**.

That is an important insight: the strategy is not always unique.

Choose the route that creates the simpler polynomial after substitution.

For this particular question, either route works cleanly.

</details>

### Question 11

Evaluate

$$\int \sin x\cos x\,dx.$$

<details>
<summary>Answer</summary>

There are multiple valid routes.

Using substitution:

$$u=\sin x,\qquad du=\cos x\,dx,$$

so

$$\boxed{\frac{\sin^2x}{2}+C}.$$

You could also use

$$\sin x\cos x=\frac12\sin2x,$$

which gives the same result.

Good solvers recognise that **multiple paths can lead to the same destination**.

</details>

---

## The decision table

| Powers of `sin`, `cos` | First investigation |
|---|---|
| One odd, one even | Preserve the odd one |
| Both odd | Either can work; compare simplicity |
| Both even | Power reduction |
| One factor is already a derivative pair | Use that pair first |

The goal is not to memorise “odd → this formula.”

The goal is to see **why parity tells you whether a derivative factor can be preserved.**