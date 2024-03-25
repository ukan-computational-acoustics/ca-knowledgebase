# Acoustics PDEs
Author: [Andrew Gibbs](https://knowledgebase.acoustics.ac.uk/community/bios.html#andrew-gibbs)

<!-- ```{warning}
This part of the site is currently under development. Its content is incomplete.
``` -->

<!-- This page will talk through what a PDE is, either via a couple of very simple examples or some external links.
Mass on a spring is the classic one to discuss but there are others.
Riding a bike or driving a car? Just got input force, inertia and drag then - not stiffness. Would lead to point that PDEs have to 2nd order to be oscillatory, if that's something we want to get into. -->

```{warning}
We assume a basic familiarity with the concept of a partial differential equation (PDE). We will not spend time explaining this, as there are plenty of free resources available online. For example, [Wikipedia](https://en.wikipedia.org/wiki/Partial_differential_equation), [MathWorld](https://mathworld.wolfram.com/PartialDifferentialEquation.html), or this video series by [3blue1brown](https://www.youtube.com/watch?v=p_di4Zn4wz4&list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6).
```

## The Acoustic Wave Equation

The fundamental PDE we consider, and the starting point for many of technical discussions which follow, is the *Wave Equation*:
```{math}
:label: eq-wave-eq
\frac{\partial^2}{\partial t^2}U(x,t) - c^2\Delta U(x,t) = 0,
```
where $\Delta:=\sum_{j=1}^d \frac{\partial}{\partial x_j}$, $d$ is the number of dimensions, and $c$ is the speed of sound.

In one dimension, this equation can be derived from fundamental mechanical principles: by treating air molecules as tiny particles connected by [vibrating springs](https://en.wikipedia.org/wiki/Wave_equation#From_Hooke's_law), or by considering a [vibrating string](https://math.libretexts.org/Bookshelves/Differential_Equations/Differential_Equations_(Chasnov)/09%3A_Partial_Differential_Equations/9.02%3A_Derivation_of_the_Wave_Equation). Alternatively, the acoustic wave equation can be derived from Euler's equation, by treating the air as an inviscid fluid, and imposing further physical assumptions {cite}`CoKr:19`.

Any acoustic wave $U$ will satisfy {eq}`eq-wave-eq`. To turn this into a problem we can solve (with a unique solution), we must specify initial and/or boundary conditions. For example:
* $U(x,0)=f(x)$ for known $f$ may describe a wave some initial time, and we may want to model how this evolves for $t>0$. This is an *initial condition*.
* $U(X,t)=0$ for some $(d-1)$-dimensional set $X$ describes a *sound-soft boundary condition*.
* More information about boundary conditions is given [here](how-define-problem-acoustics-pdes).

## The Helmholtz Equation

In many applications, the source of the sound can be assumed to be consistent. For example, when modelling acoustic noise from a source like a building site or motorway, we may only be interested in times when the noise is emanating consistently from the source. This leads to a simplification of {eq}`eq-wave-eq` where the unknown does not depend on time.

Mathematically, this can be achieved by assuming a time-harmonic solution to the Wave Equation {eq}`eq-wave-eq`, specifically: $U(x,t) = u(x) \mathrm{e}^{-\mathrm{i}\omega t}$ where $\mathrm{i}:=\sqrt{-1}$ and $\omega>0$.
 From this we obtain the Helmholtz equation
```{math}
:label: eq-helmholtz
\Delta u(x) + k^2 u(x) = 0.
```
Here $k:=\omega/c$ is the *wavenumber*.
<!-- At this stage, there are two main ways to solve the scattering problem. In the opinion of this author, the first is more common in acoustics problems. -->

As for the Wave Equation, we may impose boundary conditions for the unknown $u$ to be uniquely determined. It is this boundary value problem (BVP) that we will solve.

Instead of formulating as a BVP, the Helmholtz Equation {eq}`eq-helmholtz` may represent scattering by *inhomogenous media*, where $k$ is variable inside of some bounded region. This is sometimes referred to as a *transmission* problem. To the author's best knowledge, such problems are less common in acoustic modelling; at the time of writing this Knowledgebase does not contain any examples of this type.