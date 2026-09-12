# Trigonometric Integrals — 01: Identify the Family

> **Class 12 CBSE / NCERT mindset:** Before integrating, first identify what kind of creature is sitting in front of you.

## The mental model

Do **not** start by hunting for a formula.

Start with:

> **What is this integral mostly made of?**

For trigonometric integrals, most questions initially fall into a few families:

| What you see | First thought |
|---|---|
| Powers of `sin x` and `cos x` | Power-pattern check |
| Powers of `tan x` and `sec x` | Tangent/secant pattern |
| Powers of `cot x` and `cosec x` | Cotangent/cosecant pattern |
| A trig function with its derivative nearby | Substitution |
| A rational expression in one trig function | Try a useful substitution / identity |
| No obvious pattern | Simplify first |

The goal of this chapter is simple: **train your eyes before training your algebra.**

## Checklist #1 — Identify the family

For every question, say the family **before** doing any calculation.

1. Is it mainly `sin` and `cos`?
2. Mainly `tan` and `sec`?
3. Mainly `cot` and `cosec`?
4. Is there a function and its derivative together?
5. Is an identity likely to simplify it?

> **Rule:** Identification comes before manipulation.

---

## Level 0 — Just recognition

### Question 1

Identify the main family:

$$\int \sin^4 x\,dx$$

<details>
<summary>Answer</summary>

**Sin-cos power family.**

More specifically, it is a **power of sine** integral.

</details>

### Question 2

$$\int \tan^3x\sec^2x\,dx$$

<details>
<summary>Answer</summary>

**Tan-sec family.**

There is also a possible **derivative-pair/substitution** pattern because

$$\frac{d}{dx}(\tan x)=\sec^2x.$$

</details>

### Question 3

$$\int \frac{\sin x}{1+\cos x}\,dx$$

<details>
<summary>Answer</summary>

This is **not primarily a power problem**.

It is a **function + derivative** pattern because

$$\frac{d}{dx}(1+\cos x)=-\sin x.$$

So substitution should be considered first.

</details>

### Question 4

$$\int \cot^5x\cosec^2x\,dx$$

<details>
<summary>Answer</summary>

**Cot-cosec family**, with a derivative pair because

$$\frac{d}{dx}(\cot x)=-\cosec^2x.$$

</details>

---

## Level 1 — Choose the first door

For each integral, choose the **first** approach you would investigate.

### Question 5

$$\int \sin^3x\cos^2x\,dx$$

A. Integration by parts  
B. Power-pattern check  
C. Partial fractions  
D. Direct logarithm

<details>
<summary>Answer</summary>

**B. Power-pattern check.**

It is a product of powers of `sin x` and `cos x`. That tells us to inspect whether one power is odd/even before doing anything else.

</details>

### Question 6

$$\int \sec^4x\tan^3x\,dx$$

<details>
<summary>Answer</summary>

First investigate the **tan-sec power pattern**.

There is an odd power of `tan x`, so we should later look for a way to preserve one `tan x\sec x` pair or use a suitable identity/substitution.

</details>

### Question 7

$$\int \frac{2x+3}{5x^2+1}\,dx$$

<details>
<summary>Answer</summary>

This is actually **not a trigonometric integral**. It is a rational/function-derivative pattern.

The habit still matters: identify the structure before choosing a method.

</details>

---

## Level 2 — Multiple patterns

Some integrals have **more than one visible feature**. Your job is to rank them.

### Question 8

$$\int \tan^2x\sec^2x\,dx$$

<details>
<summary>Answer</summary>

Two things are visible:

- tan-sec family
- derivative pair `sec²x dx`

The **derivative pair is the stronger clue** because

$$d(\tan x)=\sec^2x\,dx.$$

So the natural first move is substitution.

</details>

### Question 9

$$\int \sin^2x\cos x\,dx$$

<details>
<summary>Answer</summary>

It belongs to the **sin-cos power family**, but the more useful clue is the derivative pair:

$$d(\sin x)=\cos x\,dx.$$

So substitution with `u = sin x` is more natural than using a power-reduction identity.

</details>

### Question 10

$$\int \sin^2x\,dx$$

<details>
<summary>Answer</summary>

There is no obvious derivative pair.

So the first thought should be **simplify using a trig identity**:

$$\sin^2x=\frac{1-\cos 2x}{2}.$$

</details>

---

## Skill checkpoint

Before moving to the next chapter, you should be able to say something like:

> “This is a sin-cos power problem.”

or

> “This has a derivative pair, so substitution is probably the cleanest first move.”

That one sentence is the beginning of good integration.

## The one-line muscle

For every new integral, force yourself to complete:

$$\boxed{\text{I notice ______, so my first investigation is ______.}}$$

You are not trying to solve yet.

You are training **pattern recognition**.