# Trigonometric Integrals — 06: Simplify Until the Answer Has a Shape

> **Checklist #6:** When substitution and power patterns do not solve the integral directly, simplify it into a standard form.

## The mental model

A lot of integration is really **recognition after simplification**.

You may start with something that looks unfamiliar:

$$\frac{1-\cos x}{\sin x}.$$

But split it:

$$\frac{1}{\sin x}-\frac{\cos x}{\sin x}
=\cosec x-\cot x.$$

Now the integral has two standard pieces.

So ask:

> **“What familiar shape can I turn this into?”**

---

## Checklist #6

Use this order:

1. Look for an immediate derivative pair.
2. If that fails, simplify algebraically.
3. Use identities to reduce the number of different trig functions.
4. Split sums/differences when integration can then be done term-by-term.
5. Compare the result with known standard integrals.

Useful standard forms include

$$\int \tan x\,dx=\ln|\sec x|+C,$$

$$\int \cot x\,dx=\ln|\sin x|+C,$$

$$\int \sec x\,dx=\ln|\sec x+\tan x|+C,$$

$$\int \cosec x\,dx=\ln|\cosec x-\cot x|+C.$$

---

## Level 0 — Simplify the integrand

### Question 1

Simplify

$$\frac{\sin x}{\cos x}.$$

<details>
<summary>Answer</summary>

$$\frac{\sin x}{\cos x}=\boxed{\tan x}.$$

</details>

### Question 2

Simplify

$$\frac{1-\cos^2x}{\sin x}.$$

<details>
<summary>Answer</summary>

Using

$$1-\cos^2x=\sin^2x,$$

we get

$$\frac{\sin^2x}{\sin x}=\boxed{\sin x}.$$

</details>

### Question 3

Simplify

$$\frac{\sec^2x-1}{\tan x}.$$

<details>
<summary>Answer</summary>

Since

$$\sec^2x-1=\tan^2x,$$

we get

$$\boxed{\tan x}.$$

</details>

---

## Level 1 — Split into standard pieces

### Question 4

Evaluate

$$\int \frac{1-\cos x}{\sin x}\,dx.$$

<details>
<summary>Answer</summary>

Split the fraction:

$$\frac{1-\cos x}{\sin x}
=\cosec x-\cot x.$$

Thus

$$\int\cosec x\,dx-\int\cot x\,dx.$$

Using the standard forms,

$$\boxed{\ln|\cosec x-\cot x|-\ln|\sin x|+C}.$$

</details>

### Question 5

Evaluate

$$\int \frac{1+\sin x}{\cos x}\,dx.$$

<details>
<summary>Answer</summary>

Split:

$$\frac{1+\sin x}{\cos x}
=\sec x+\tan x.$$

Hence

$$\boxed{\ln|\sec x+\tan x|+\ln|\sec x|+C}.$$

</details>

---

## Level 2 — Rational-looking trig expressions

### Question 6

Evaluate

$$\int \frac{\sin x}{1-\cos x}\,dx.$$

<details>
<summary>Answer</summary>

This is a derivative-pair problem hidden in a fraction.

Take

$$u=1-\cos x.$$

Then

$$du=\sin x\,dx.$$

So

$$\int\frac{du}{u}=\boxed{\ln|1-\cos x|+C}.$$

</details>

### Question 7

Evaluate

$$\int \frac{\cos x}{1+\sin x}\,dx.$$

<details>
<summary>Answer</summary>

Take

$$u=1+\sin x.$$

Then

$$du=\cos x\,dx.$$

Therefore

$$\boxed{\ln|1+\sin x|+C}.$$

</details>

---

## Level 3 — Convert to one trig language

### Question 8

Evaluate

$$\int \frac{\sin^2x}{\cos x}\,dx.$$

<details>
<summary>Answer</summary>

Convert

$$\sin^2x=1-\cos^2x.$$

Then

$$\frac{\sin^2x}{\cos x}
=\sec x-\cos x.$$

Thus

$$\int\sec x\,dx-\int\cos x\,dx.$$

So

$$\boxed{\ln|\sec x+\tan x|-\sin x+C}.$$

</details>

### Question 9

Evaluate

$$\int \frac{\cos^2x}{\sin x}\,dx.$$

<details>
<summary>Answer</summary>

Use

$$\cos^2x=1-\sin^2x.$$

Then

$$\frac{\cos^2x}{\sin x}=\cosec x-\sin x.$$

Hence

$$\boxed{\ln|\cosec x-\cot x|+\cos x+C}.$$

</details>

---

## Level 4 — Recognise disguised standard forms

### Question 10

Evaluate

$$\int \frac{\sec x+\tan x}{\sec x}\,dx.$$

<details>
<summary>Answer</summary>

Split:

$$\frac{\sec x+\tan x}{\sec x}
=1+\frac{\tan x}{\sec x}
=1+\sin x.$$

Therefore

$$\boxed{x-\cos x+C}.$$

</details>

### Question 11

Evaluate

$$\int \frac{\tan x}{\sec x+1}\,dx.$$

<details>
<summary>Answer</summary>

Rewrite

$$\tan x=\frac{\sin x}{\cos x},\qquad
\sec x+1=\frac{1+\cos x}{\cos x}.$$

So

$$\frac{\tan x}{\sec x+1}
=\frac{\sin x}{1+\cos x}.$$

Now use

$$u=1+\cos x,\qquad du=-\sin x\,dx.$$

Therefore

$$\boxed{-\ln|1+\cos x|+C}.$$

</details>

---

## The standard-form reflex

When a trig integral looks ugly, do not panic and do not invent a new method immediately.

Ask:

> **Can I rewrite the ugly part as `tan`, `sec`, `cot`, `cosec`, `sin`, `cos`, or a derivative pair?**

A good integrator is often just a person who is very good at **making the integrand look familiar**.