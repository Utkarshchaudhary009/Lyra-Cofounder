# Trigonometric Integrals — 02: Find the Derivative Pair

> **Checklist #2:** Before touching an identity, look for a function sitting beside its derivative.

## The mental model

Integration is the reverse of differentiation.

So when you see

$$\int f(g(x))g'(x)\,dx,$$

your eyes should notice:

$$g(x)\quad\text{and}\quad g'(x).$$

For trigonometric functions, the most important pairs are:

$$\frac{d}{dx}(\sin x)=\cos x$$

$$\frac{d}{dx}(\cos x)=-\sin x$$

$$\frac{d}{dx}(\tan x)=\sec^2x$$

$$\frac{d}{dx}(\cot x)=-\cosec^2x$$

$$\frac{d}{dx}(\sec x)=\sec x\tan x$$

$$\frac{d}{dx}(\cosec x)=-\cosec x\cot x.$$

The question is not merely **“Do I know these derivatives?”**

The question is:

> **“Can I spot one of these structures inside the integral?”**

---

## Checklist #2

For each integral:

1. Circle the function that could become `u`.
2. Look immediately beside it for its derivative.
3. Ignore harmless constants/signs for a moment.
4. Only then decide whether substitution is natural.

---

## Level 0 — Pure derivative pairs

### Question 1

$$\int \cos x\,dx$$

<details>
<summary>Answer</summary>

Because

$$\frac{d}{dx}(\sin x)=\cos x,$$

we can see the pair directly.

Therefore,

$$\boxed{\int \cos x\,dx=\sin x+C.}$$

</details>

### Question 2

$$\int \sin x\,dx$$

<details>
<summary>Answer</summary>

Since

$$\frac{d}{dx}(\cos x)=-\sin x,$$

we need a minus sign:

$$\boxed{\int \sin x\,dx=-\cos x+C.}$$

</details>

### Question 3

$$\int \sec^2x\,dx$$

<details>
<summary>Answer</summary>

$$\frac{d}{dx}(\tan x)=\sec^2x.$$

Hence

$$\boxed{\int \sec^2x\,dx=\tan x+C.}$$

</details>

---

## Level 1 — Spot the pair inside a product

### Question 4

$$\int \sin^4x\cos x\,dx$$

<details>
<summary>Answer</summary>

Look at

$$\sin^4x\quad\text{and}\quad \cos x\,dx.$$

Since

$$d(\sin x)=\cos x\,dx,$$

choose

$$u=\sin x.$$

Then

$$du=\cos x\,dx.$$

So

$$\int \sin^4x\cos x\,dx
=\int u^4du
=\boxed{\frac{\sin^5x}{5}+C}.$$

</details>

### Question 5

$$\int \cos^5x\sin x\,dx$$

<details>
<summary>Answer</summary>

Use

$$u=\cos x,\qquad du=-\sin x\,dx.$$

Therefore

$$\int \cos^5x\sin x\,dx
=-\int u^5du
=\boxed{-\frac{\cos^6x}{6}+C}.$$

</details>

### Question 6

$$\int \tan^7x\sec^2x\,dx$$

<details>
<summary>Answer</summary>

The pair is

$$\tan x\quad\text{with}\quad \sec^2x\,dx.$$

Take

$$u=\tan x,\qquad du=\sec^2x\,dx.$$

Then

$$\int u^7du=\boxed{\frac{\tan^8x}{8}+C}.$$

</details>

---

## Level 2 — The derivative is present but disguised

### Question 7

$$\int \frac{\sin x}{1+\cos x}\,dx$$

<details>
<summary>Answer</summary>

The important part is the denominator:

$$1+\cos x.$$

Its derivative is

$$-\sin x.$$

So choose

$$u=1+\cos x,$$

$$du=-\sin x\,dx.$$

Thus

$$\int \frac{\sin x}{1+\cos x}\,dx
=-\int \frac{du}{u}
=-\ln|u|+C.$$

Therefore

$$\boxed{-\ln|1+\cos x|+C}.$$

</details>

### Question 8

$$\int \frac{\sec^2x}{3+\tan x}\,dx$$

<details>
<summary>Answer</summary>

The denominator is

$$3+\tan x,$$

whose derivative is

$$\sec^2x.$$

So

$$u=3+\tan x,\qquad du=\sec^2x\,dx.$$

Hence

$$\boxed{\ln|3+\tan x|+C}.$$

</details>

---

## Level 3 — One extra constant

A constant multiple of the derivative is still the same pattern.

### Question 9

$$\int \sin(3x)\cos(3x)\,dx$$

<details>
<summary>Answer</summary>

Notice that

$$\frac{d}{dx}[\sin(3x)]=3\cos(3x).$$

The derivative is present up to a factor of `3`.

Take

$$u=\sin(3x),\qquad du=3\cos(3x)\,dx.$$

Therefore

$$\int \sin(3x)\cos(3x)\,dx
=\frac13\int u\,du
=\boxed{\frac{\sin^2(3x)}{6}+C}.$$

</details>

### Question 10

$$\int \frac{2x}{x^2+7}\,dx$$

<details>
<summary>Answer</summary>

The denominator's derivative is exactly the numerator:

$$\frac{d}{dx}(x^2+7)=2x.$$

So

$$u=x^2+7,\qquad du=2x\,dx.$$

Hence

$$\boxed{\ln|x^2+7|+C}.$$

The example is not trigonometric, but the **same pattern-recognition muscle** is being trained.

</details>

---

## Level 4 — Your eye must choose the right inside function

### Question 11

$$\int \frac{\cos x}{(2+\sin x)^4}\,dx$$

<details>
<summary>Answer</summary>

Choose the whole inside expression:

$$u=2+\sin x.$$

Then

$$du=\cos x\,dx.$$

So

$$\int u^{-4}du
=\frac{u^{-3}}{-3}+C.
$$

Therefore

$$\boxed{-\frac{1}{3(2+\sin x)^3}+C}.$$

</details>

### Question 12

$$\int \frac{\tan x\sec x}{5+\sec x}\,dx$$

<details>
<summary>Answer</summary>

The derivative of `sec x` is

$$\sec x\tan x.$$

That entire product is already present.

Take

$$u=5+\sec x.$$

Then

$$du=\sec x\tan x\,dx,$$

giving

$$\boxed{\ln|5+\sec x|+C}.$$

</details>

---

## The reflex to build

When your eyes see

$$\boxed{\frac{f'(x)}{f(x)}}$$

you should immediately think

$$\boxed{\ln|f(x)|+C}.$$

And when you see

$$\boxed{g(x)^n g'(x)}$$

you should think

$$\boxed{u=g(x)}.$$

This is the second major muscle of the book: **find the derivative pair before manipulating the expression.**