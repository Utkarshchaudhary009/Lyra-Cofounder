# Trigonometric Integrals — 03: Preserve the Derivative

> **Checklist #3:** When the derivative is missing, change the integral so the derivative appears.

## The mental model

A substitution works only when the differential fits.

Suppose you want

$$u=\sin x.$$

Then

$$du=\cos x\,dx.$$

So the dream is to find a `\cos x dx` somewhere in the integral.

But real questions often hide it. Your job is not to guess a new method; it is to **reshape the expression without changing its value**.

That is why identities matter.

---

## Checklist #3

When you spot a possible substitution but its derivative is missing:

1. Keep the useful factor needed for `du`.
2. Rewrite the remaining part using an identity.
3. Convert the whole integral into `u`.
4. Do not substitute until the differential really matches.

The key identities are

$$\sin^2x+\cos^2x=1,$$

$$1+\tan^2x=\sec^2x,$$

$$1+\cot^2x=\cosec^2x.$$

---

## Level 0 — See the missing piece

### Question 1

What is missing for the substitution `u = sin x` in

$$\int \sin^4x\,dx?$$

<details>
<summary>Answer</summary>

For

$$u=\sin x,$$

we need

$$du=\cos x\,dx.$$

The integral has no `\cos x dx`, so direct substitution is **not** ready.

We need another idea.

</details>

### Question 2

Can `u = cos x` work directly for

$$\int \cos^3x\,dx?$$

<details>
<summary>Answer</summary>

Not directly.

If

$$u=\cos x,$$

then

$$du=-\sin x\,dx,$$

but there is no `\sin x dx` present.

So we must **manufacture** the missing factor.

</details>

---

## Level 1 — Manufacture the derivative

### Question 3

Evaluate

$$\int \cos^3x\,dx.$$

<details>
<summary>Answer</summary>

Save one cosine:

$$\int \cos^3x\,dx
=\int \cos^2x\cos x\,dx.$$

Now use

$$\cos^2x=1-\sin^2x.$$

So

$$=\int (1-\sin^2x)\cos x\,dx.$$

Now the derivative pair exists:

$$u=\sin x,\qquad du=\cos x\,dx.$$

Therefore

$$\int (1-u^2)\,du
=u-\frac{u^3}{3}+C.$$

Hence

$$\boxed{\sin x-\frac{\sin^3x}{3}+C}.$$

</details>

### Question 4

Evaluate

$$\int \sin^3x\,dx.$$

<details>
<summary>Answer</summary>

Save one sine:

$$\sin^3x=\sin^2x\sin x.$$

Use

$$\sin^2x=1-\cos^2x.$$

Thus

$$\int \sin^3x\,dx
=\int (1-\cos^2x)\sin x\,dx.$$

Take

$$u=\cos x,\qquad du=-\sin x\,dx.$$

So

$$=-\int (1-u^2)du
=-u+\frac{u^3}{3}+C.$$

Therefore

$$\boxed{-\cos x+\frac{\cos^3x}{3}+C}.$$

</details>

---

## Level 2 — Tan/sec: preserve `sec²x`

For tangent, remember

$$\frac{d}{dx}(\tan x)=\sec^2x.$$

### Question 5

Evaluate

$$\int \tan^3x\,dx.$$

<details>
<summary>Answer</summary>

Save a `tan x` and convert the other two:

$$\tan^3x=\tan^2x\tan x.$$

Using

$$\tan^2x=\sec^2x-1,$$

we get

$$\int(\sec^2x-1)\tan x\,dx.$$

This expression is not yet the nicest substitution form because the derivative of `sec x` is `sec x tan x`, while the derivative of `tan x` is `sec²x`.

A cleaner route is to use

$$\tan^3x=\tan x(\sec^2x-1).$$

Then split:

$$\int \tan x\sec^2x\,dx-\int\tan x\,dx.$$

For the first term, `u = tan x`. For the second,

$$\int \tan x\,dx=-\ln|\cos x|+C.$$

Hence

$$\boxed{\frac{\tan^2x}{2}+\ln|\cos x|+C}.$$

</details>

### Question 6

Evaluate

$$\int \tan x\sec^2x\,dx.$$

<details>
<summary>Answer</summary>

The derivative is already present:

$$u=\tan x,\qquad du=\sec^2x\,dx.$$

Therefore

$$\boxed{\frac{\tan^2x}{2}+C}.$$

</details>

---

## Level 3 — Cot/cosec: preserve `cosec²x`

### Question 7

Evaluate

$$\int \cot^3x\,dx.$$

<details>
<summary>Answer</summary>

Write

$$\cot^3x=\cot^2x\cot x.$$

Use

$$\cot^2x=\cosec^2x-1.$$

Then

$$\int \cot x\cosec^2x\,dx-\int\cot x\,dx.$$

For the first term, take

$$u=\cot x,\qquad du=-\cosec^2x\,dx.$$

Hence

$$-\frac{\cot^2x}{2}-\int\cot x\,dx.$$

Since

$$\int\cot x\,dx=\ln|\sin x|+C,$$

we obtain

$$\boxed{-\frac{\cot^2x}{2}-\ln|\sin x|+C}.$$

</details>

### Question 8

Evaluate

$$\int \cot x\cosec^2x\,dx.$$

<details>
<summary>Answer</summary>

Immediately see

$$u=\cot x,\qquad du=-\cosec^2x\,dx.$$

Thus

$$\boxed{-\frac{\cot^2x}{2}+C}.$$

</details>

---

## Level 4 — Your turn to manufacture the right form

### Question 9

Evaluate

$$\int \sin^2x\cos^3x\,dx.$$

<details>
<summary>Answer</summary>

The power of cosine is odd, so save one cosine:

$$\int \sin^2x\cos^2x\cos x\,dx.$$

Convert

$$\cos^2x=1-\sin^2x.$$

Then

$$\int \sin^2x(1-\sin^2x)\cos x\,dx.$$

Now

$$u=\sin x,\qquad du=\cos x\,dx.$$

Therefore

$$\int (u^2-u^4)du
=\frac{u^3}{3}-\frac{u^5}{5}+C.$$

So

$$\boxed{\frac{\sin^3x}{3}-\frac{\sin^5x}{5}+C}.$$

</details>

### Question 10

Evaluate

$$\int \sin^4x\cos x\,dx.$$

<details>
<summary>Answer</summary>

The derivative pair is already visible:

$$u=\sin x,\qquad du=\cos x\,dx.$$

Hence

$$\boxed{\frac{\sin^5x}{5}+C}.$$

Notice the contrast with Question 9: **we only manufacture a derivative when one is actually missing.**

</details>

---

## The deeper habit

When you want `u`, ask:

> **“What must be left over so that `du` appears?”**

That single question turns many identity manipulations from memorised tricks into logical moves.