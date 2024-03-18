# The ideas behind the Boundary Element Method (BEM)
Author: [Andrew Gibbs](https://knowledgebase.acoustics.ac.uk/community/bios.html#andrew-gibbs)
## Introduction
### Physical intuition

Suppose we have an incoming acoustic wave $u^i$ and a scattering obstacle $\Omega$, and we want to determine the amplitude of the scattered acoustic field $u^s(x)$, i.e. how much sound has bounced back, at any point $x$ in the region surrounding the obstacle?

Physically, the idea of BEM may be interpreted as covering the obstacle in lots of tiny speakers. (Each microphone is analogy for the more officially-named _point source_ or the _Green's function_.) The aim of BEM is to solve a different problem; to adjust the volume on each speaker individually so that the combined amplitude of all of the microphones, if we were listening away from the obstacle, is the same as the scattered acoustic field $u^s$ in our original problem.

To solve the BEM problem, i.e. to fine tune the volume on each microphone, we must solve a problem on the surface of $\Omega$, rather than in the area surrounding $\Omega$. We will write $\partial\Omega$ to represent the surface. Practically this can be appealing, because this problem is usually simpler: in a lower spatial dimensions and on a bounded domain. For example, modelling scattering by a cube, most of the computational work will be done on the circumference on the square faces of the cube.

### Representation in terms of point sources

We will write $\Phi(x,y)$ to mean the point-source / Green's function / metaphorical speaker at point $y$ on $\partial \Omega$, observed at point $x$ on $\Omega$. Naturally we would expect $\Phi(x,y)$ to be a wave, and to get larger as $y$ moves towards $x$. 

It follow's from [Green's third identity](https://en.wikipedia.org/wiki/Green's_identities#Green's_third_identity) that

$$
u^s(x) = -\int_{\partial\Omega}\Phi(x,y)\frac{\partial u}{\partial n}(y)\ \mathrm{d}s(y) + \int_{\partial\Omega}\frac{\partial \Phi(x,y)}{\partial n(y)}u(y)\ \mathrm{d}s(y),
$$

$\Phi$ denotes the fundamental solution / point source / Green's function / figurative speaker:

$$
\Phi(x,y) := \left\{
\begin{array}{ll}
\frac{\mathrm{i}}{4}H^{(1)}_0(k|x-y|),&\quad \text{two dimensions},\\
{\exp({\mathrm{i}k|x-y|}})/({4\pi|x-y|}),&\quad \text{three dimensions},
\end{array}
\right.
$$

where $H^{(1)}_0$ is the [Hankel function](https://mathworld.wolfram.com/HankelFunctionoftheFirstKind.html) of the first kind order zero.

Here $x$ is some point away from the obstacle $\Omega$.
If we consider two types of speakers, $\Phi(x,y)$ and $\frac{\partial \Phi(x,y)}{\partial n(y)}$, then the above should be interpreted as a weighted sum of a large number of these point-sources/speakers, over the surface of the obstacle. Conveniently, the unknown density which weights these sources (i.e. the other term in the integrals), has been expressed in terms of our total field $u$.

Depending on boundary conditions, it may be possible to remove one of the two integrals above. For example, a sound-hard obstacle has boundary condition $u=0$ on $\partial\Omega$.

### The steps to the Boundary Element Method

1. Modify (1) to obtain an integral equation on the boundary $\partial \Omega$, where $u$ and/or $\frac{\partial u}{\partial n}$ on $\partial \Omega$ are the unknown quantities. This is called a _Boundary Integral Equation_ (BIE). At this point, no approximation has taken place.

2. Approximately solve the BIE, using a finite element method on the boundary. Hence the name _Boundary Element Method_.

3. Plug our approximation to $u$ and/or $\frac{\partial u}{\partial n}$ into the representation formula (1), to obtain an approximation to $u^s$ away from the boundary.

For the remainder of this document, we will describe each of these steps in more detail.

## Constructing a Boundary Integral Equation

We want to solve (1) for the unknown densities.

The next step is to move the problem onto the boundary $\partial \Omega$, so that $x$ and $y$ live on $\partial \Omega$, and then our original problem is reduced to an (arguably simpler) problem on $\partial \Omega$.

This process of _moving the problem onto the boundary_ is commonly referred to as a _trace_ (no relation to the matrix operation of the same name). There are three or four commonly used traces, which warrants a separate discussion in its own right. This can be skipped for now, and taken on trust.

<details>
<summary> Click here to show optional details on trace operators</summary>

### Trace operators
The simplest of the trace operators is the _Dirichlet_ trace $\gamma_D$, which can be interpreted physically as moving $x$ to the boundary $\partial\Omega$. This trace gives us

 $$
\gamma_Du^s(x) = -\int_{\partial\Omega}\Phi(x,y)\frac{\partial u}{\partial n}(y)\mathrm{d}s(y)
+
\int_{\partial\Omega}\frac{\partial\Phi(x,y)}{\partial n(y)}u(y)\mathrm{d}s(y) + \frac{1}{2}u(x),
 $$
 
 for $x$ on $\partial \Omega$. This is often compactly written as
 
 $$
\gamma_Du^s = S\frac{\partial u}{\partial n} - \left(D+\frac{1}{2}\mathcal{I}\right)u,\quad\text{on }\partial\Omega.
 $$

 The second most commonly used trace is the Neumann trace, which can be interpreted as moving $\nabla u$ onto $\partial\Omega$ (non-tangentially) and then taking the dot product with the normal derivative at this limit point. This gives us:

 $$
 \begin{align*}
\gamma_Nu^s(x) =& -\int_{\partial\Omega}\frac{\Phi(x,y)}{\partial n(x)}\frac{\partial u}{\partial n}(y)\mathrm{d}s(y)
+\frac{1}{2}\frac{\partial u}{\partial n}(x)\\
&+
\frac{\partial}{\partial n(x)}\int_{\partial\Omega}\frac{\partial\Phi(x,y)}{\partial n(y)}u(y)\mathrm{d}s(y)
\end{align*},\quad x\text{ on }\partial\Omega,
 $$
 
 which has the compact form
 
 $$
\gamma_N u^s = \left(-D'+\frac{1}{2}\mathcal{I}\right)\frac{\partial u}{\partial n} + Hu.
 $$
 
 Both of these trace equations can be used to construct our boundary integral equation which follows.
</details>


After taking a trace, we obtain an integral equation of the form

$$
\begin{equation}
(\chi\mathcal{I}+\mathcal{K})v(x) = f(x),\quad x\text{ on }\partial \Omega.
\end{equation}
$$

where our unknown $v$ depends on the boundary conditions, i.e. the material of $\Omega$ as follows:

$$
v = \left\{\begin{array}{ll}
{\partial u}/{\partial n}& \text{sound-soft / Dirichlet}\\
u&\text{sound-hard / Neumann}\\
({\partial u}/{\partial n}, u ) &\text{impedance / Robin}
\end{array}\right.
$$

In the third case, our unknown quantity $v$ is a vector of two unknown functions. For problems of scattering by thin screens/plates, the quantities above are replaced by their jump in value from either side of the screen. For example, $u$ would be replaced by $u^+-u^-$, where $u+$ and $u^-$ are respectively the limiting values of $u$ above and below the screen.

In (1) $\mathcal{I}$ denotes the identity operator, which maps a function to its self. Some BIEs will contain the identity operator in which case $\chi=\pm\frac{1}{2}$, more details follow below. If there are no identity terms, clearly $\chi=0$.

In (1) $\mathcal{K}$ is a _boundary integral operator_ (BIO), meaning it maps functions on the boundary $\partial \Omega$ to functions on $\partial \Omega$

$$
\mathcal{K}\psi(x) := \int_{\partial \Omega}K(x,y)\psi(y)\mathrm{d} s(y),
$$

where $K(x,y)$ is a known function called the _kernel_ (no relation to the computer component or algebraic objects of the same name) and will depend on the choice of trace taken, but in the simplest case, with Dirichlet BCs / sound-soft obstacle, $K=\Phi$.

Similarly, $f$ is known explicitly, and will depend on the choice of trace used and the incoming wave $u^i$. In the simplest case, we have $f = u^i$.

### BIE directory
 <!-- Some of these formulations are not well-posed at certain wavenumbers $k$, meaning that they may have multiple solutions. If our BIE is not well posed, then our BEM has no chance of being accurate! -->

This section contains a list of the formulations required for common acoustic scattering problems. Before we define these formulations, it is necessary to introduce the five main integral operators, their names are listed to the right:

$$
\begin{align*}
\mathcal{I}\psi(x) &= \psi(x),\quad&&\text{Identity}\\
S\psi(x) &= \int_{\partial\Omega}\Phi(x,y)\psi(y),\mathrm{d}s(y)\quad&&\text{Single Layer}\\
D\psi(x) &=\int_{\partial\Omega}\frac{\partial\Phi(x,y)}{\partial n(y)}\psi(y)\mathrm{d}s(y)\quad&&\text{Double Layer}\\
D'\psi(x) &=\int_{\partial\Omega}\frac{\partial\Phi(x,y)}{\partial n(x)}\psi(y)\mathrm{d}s
(y)\quad&&\text{Adjoint double Layer}\\
H\psi(x) &=\int_{\partial\Omega}\frac{\partial^2\Phi(x,y)}{\partial n(x)\partial n(y)}\psi(y)\mathrm{d}s
(y)\quad&&\text{Hypersingular}
\end{align*}
$$


For each type of problem solvable by BEM, the starting point is a relevant _boundary integral equation_, which makes use of some combination of the above operators. These can be derived using the trace identities in the above (optional) section.

 Depending on the shape of $\Omega$ and the boundary conditions, there may be one or many possible BIE formulations of the form (2). The appropriate formulations are given below, sometimes there are multiple formulations which could be used. The formulation can often be simplified when considering problems on thin screens/plates, by _volume_ we refer to more typical scattering obstacles such as polygons in two dimensions and tetrahedra in three dimensions. By plates/screens, we refer to obstacles which are _thin_ in one direction, for example a square plate in three dimensions. And as is explained in the table, certain formulations are not well-posed at certain wavenumbers $k$, meaning that they may have multiple solutions. If our BIE is not well posed, then the approximate problem we solve later has no chance!

| Material / BCs | Screen / volume | BIO $\mathcal{K}$ | RHS $f$ | Solvable? |
|----------------|-----------------|---------------|-----|-------------|
|Sound-soft / Dirichlet|Screen|  $S$ | $u^i$    |     Always        |
|                |  Volume |   $S$ | $u^i$    |      Not at certain $k$       |
|                | Volume |  $\frac{1}{2}\mathcal{I}+D'$   |$\frac{\partial u^i}{\partial n}$ |      Not at certain $k$       |
|| Volume | $\frac{1}{2}\mathcal{I}+D'-\mathrm{i}\eta S$ |$\frac{\partial u^i}{\partial n}-\mathrm{i}\eta u^i$ | If $\eta\neq0$
|Sound-Hard / Neumann | Screen | $H$ | $\frac{\partial u^i}{\partial n}$ | Always
|| Volume | $\frac{1}{2}\mathcal{I}-D$ | $u^i$ | Not at certain $k$
||Volume | $H$ | $\frac{\partial u^i}{\partial n}$ | Not at certain $k$
||Volume | $\frac{1}{2}\mathcal{I}-\mathcal{D}-\mathrm{i}\eta H$ |$u^i+\mathrm{i}\eta\frac{\partial u^i}{\partial n}$ | If $\eta\neq0$

Regarding the BIEs which are not valid _at certain_ $k$, you could consider yourself unlucky if you happened to encounter such a $k$ in practice, as they are rare; corresponding to eigenvalues of interior Laplace problems. The simple BIEs (with fewer operators in $\mathcal{K}$) are sometimes more popular in practice, because these bad wavenumbers $k$ are rare, and implementation is much easier.

The term $\eta$ is referred to as the _coupling parameter_, and can be chosen to be any non-zero real number to ensure the BIE is well posed. For example, in the Dirichlet case, the two equations which are ill-posed at certain $k$ values are never ill-posed at the same $k$ value. A classical idea is to _couple_ the equations via $\eta$, so that the coupled equation is well-posed for all $k$. In practice, a good choice is $\eta=k$.
<details>
<summary>
Impedance/Robin problems are considerably more complicated, click here for details.
</summary>

### Impedance on the screen
Now consider more general Impedance / Robin problems on the screen, with boundary conditions

$$
\gamma^\pm_N u\pm\lambda^\pm\gamma_D^\pm u = -(\gamma_N^\pm u^i\pm\lambda^\pm\gamma_D^\pm u^i),
$$

where $\gamma^\pm_D$ and $\gamma^\pm_N$ denote the Dirichlet and Neumann traces taken from above/below the screen, and $\lambda^pm$ are the impedance parameters describing the material. Here the boundary integral equation takes a matrix form, with

$$\mathcal{K} = \left[\begin{array}{ll} -\frac{1}{2}(\lambda^++\lambda^-)\mathcal{I}-2H&(\lambda^+-\lambda^-)S \\ \frac{1}{2}(\lambda^+-\lambda^-)\mathcal{I} & \mathcal{I}-(\lambda^++\lambda^-)S\end{array}\right]$$

and

$$
f = \left[\begin{array}{c}(\lambda^+-\lambda^-)\frac{\partial u^i}{\partial n}\\
(\lambda^--\lambda^+)u^i\end{array}
\right].
$$

This is uniquely solvable for $\lambda^++\lambda^-\neq0$.

</details>


## Constructing a Boundary Element Method (BEM)

The main aim of the BEM is to approximate $v_N$ by approximately solving (2), then plug this approximation into (1), to obtain an approximation for $u^s$. This is done by writing

$$
v(x)\approx v_N(x)=\sum_{n=1}^Nc_n\phi_n(x),
$$

where the $\phi_n$ are basis functions, for example piecewise linear, piecewise constants. Hence the name _Boundary Element Method_; we are implementing a finite element method on the boundary $\partial \Omega$. We then solve either the collocation or Galerkin problem.

<!-- Actually write the approximate $u^s$ -->

### Collocation BEM

The idea behind collocation is to force (2) to hold at $N$ _collocation points_ $x_1,\ldots,x_N$, on the surface $\partial \Omega$. This can be expressed as

$$
\sum_{n=1}^Nc_n(\chi\mathcal{I}+\mathcal{K})\phi_n(x_m) = f(x_m),\quad\text{for }m=1,\ldots,N,
$$

where the unknowns are the coefficients $c_n$. This is equivalent to solving the linear system:

$$
\left[\chi\phi_n(x_m)+\int_{\mathrm{supp}\ \phi_n}K(x_m,y)\phi_n(y)\mathrm{d} s(y)\right]_{n,m=1}^N
\left[c_n
\right]_{n=1}^N
=
\left[f(x_m)\right]_{m=1}^N.
$$

Collocation has the practical advantage over Galerkin (which will be summarised next) because there are only single integrals. However, there are few theoretical guarantees about the above linear system being well-conditioned, or even solvable, and little is known about the _best_ way to choose $x_m$. Here's a summary of what is known:

* Taking more collocation points than basis functions is known as _oversampling_. By doing this, and reformulating as a least-squares problem, one can often overcome the instabilities associated with collocation.
* Another technique is to supplement the linear system with some collocation points _inside_ of $\Omega$ satisfying a different equation, which follows from (1), noting that $u=0$ in $\Omega$. There are known as CHIEF points.
* When $\phi_n$ are piecewise linear functions, e.g. hat functions, choosing collocation points as the midpoints of $\mathrm{supp}\phi_n$ is actually a bad idea, and can lead to the linear system being unsolvable.

### Galerkin BEM

The idea behind Galerkin BEM is similar to Galerkin FEM, we force (2) to hold when integrate against each of our basis functions

$$
\sum_{n=1}^Nc_n\left<(\chi\mathcal{I}+\mathcal{K})\phi_n,\phi_m\right> = \left<f,\phi_m\right>,\quad\text{for }m=1,\ldots,N,
$$

where the unknowns are the coefficients $c_n$, and the triangular brackets denote the inner product 

$$\left<\psi,\varphi\right>=\int_{\partial\Omega}\psi(x)~\overline{\varphi}(x)~\mathrm{d}s(x).$$

This is equivalent to solving the linear system:

$$
\left[\chi\int_{\mathrm{supp}\phi_m}\phi_n(x)\overline{\phi_m}(x)\mathrm{d}s(x) + \int_{\mathrm{supp}\ \phi_m}\int_{\mathrm{supp}\ \phi_n}K(x,y)\phi_n(y)\overline{\phi_m}(x)\mathrm{d} s(y)\mathrm{d} s(x)\right]_{n,m=1}^N
\left[c_n
\right]_{n=1}^N
\\=
\left[\int_{\partial\Omega}f(x)\overline{\phi_m}(x)\mathrm{d}s(x)\right]_{m=1}^N.
$$

The only disadvantage of Galerkin (when compared against collocation) is the extra integral, and the double integral can be tricky to implement, especially on a two-dimensional surface, this will likely be an integral over four spatial variables.

Sometimes this can be worth it, because the system to solve is often much better behaved in practice. There are some theoretical guarantees about solvability and accuracy, which follow when the operator $\mathcal{K}$ satisfies the _coercivity_ property. For this reason, mathematicians often prefer Galerkin BEM, and engineers prefer collocation.

## Obtaining an approximate representation

Finally, we can plug our approximation $v_N$ in place of $u$ or $\frac{\partial u}{\partial n}$ in (1) to obtain our approximation to $u^s(x)$.

### Sound-soft/Dirichlet representation

Here we have $\phi_h\approx \frac{\partial u}{\partial n}$, so 

$$
\begin{equation}
u^s(x)\approx u^s_h(x) = -\int_{\partial\Omega}\Phi(x,y)v_N(y)\ \mathrm{d}s(y) = -\sum_{n=1}^Nc_n\int_{\partial\Omega}\Phi(x,y)\phi_n(y)\ \mathrm{d}s(y),
\end{equation}
$$

### Sound-hard/Neumann representation

Here we have $\phi_h\approx u$, so

$$
u^s(x)\approx u^s_h(x) = \int_{\partial\Omega}\frac{\partial \Phi(x,y)}{\partial n(y)}v_N\ \mathrm{d}s(y)
=\sum_{n=1}^Nc_n\int_{\partial\Omega}\frac{\partial \Phi(x,y)}{\partial n(y)}\phi_h(y)\ \mathrm{d}s(y),
$$

## Some final comments

### Comparison with FEM

The following table summarises the <span style="color:green">pros</span>  and <span style="color:red"> cons</span> of BEM, when compared against FEM for solving the same problem.

| Property | FEM | BEM | 
|----------------|-----------------|---------------|
|Spatial dimension of unknown| Same as original problem (with the exception of Trefftz DG  FEM)| <span style="color:green"> One less than original problem</span>
|Matrix| <span style="color:green"> Sparse</span> and large|  <span style="color:red"> Dense</span> and <span style="color:green">not so large</span> (due to lower spatial dimension)|
|Matrix entries | Smooth integrals | <span style="color:red"> Singular integrals</span>
| Size of unknown domain | <span style="color:red">Unbounded</span>, typically addressed using an artificial boundary, e.g. Perfectly Matched Layers | <span style="color:green">Bounded</span>, on the surface of $\Omega$
<!-- | Strong ellipticity / coercivity | In a non-standard norm | For screen problems, and star-shaped domains | -->

### Choice of quadrature
In the coded example in the next tutorial, we will use a one-point quadrature rule for our integrals, which is the most basic approximation conceivable. For smooth integrands $(m\neq n)$, [Gauss-Legendre quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature#Gauss–Legendre_quadrature) is very popular in practice, as this converges much faster. In higher dimensional integrals, a popular approach is to use Gauss quadrature in each direction. This is sub-optimal, cubature rules are the most efficient way to do this, but are rarely used in practice. 

For singular integrals $(m=n)$, grading can be used as a one-size-fits all approach. However, we often know the precise singular behaviour, so grading can be overkill. A more informed approach is that of singularity subtraction, where the singular part of the integrand is evaluated analytically, and the remaining part is evaluated using standard quadrature. A second informed approach is to use generalised Gaussian quadrature, which is designed to be accurate for integrals containing a certain type of singularity.

For singular double integrals, when the singularity is along the diagonal of the integration domain, the Duffy transform can be used to convert to two integrals over a square/cube/hypercube with singularities at the edges, making it more amenable to techniques for 1D singular integrals.

Quadrature is the main difficulty when implementing a BEM. If possible, use BEM software such as [bempp](https://bempp.com), where quadrature has been implemented carefully and efficiently. If you are hellbent on implementing your own BEM, get your quadrature routines from a colleague who has tried and tested them for similar problems, otherwise prepare yourself for several days/weeks/months of painful debugging.

### Summary

* Certain acoustic scattering problems can be reformulated as a problem on the boundary, where the unknown density determines the amplitude of lots of tiny sources/speakers
* BEMs are FEMs on the boundary/surface of the obstacle
* Certain BIEs and/or certain choices of collocation points can lead to numerical instabilities
* Implementing and understanding BEMs can be harder than FEMs, but there are computational advantages

<!-- References needed:
Further reading: Sauter & Schwab
ACTA numerica
Colton & Kress

Collocation:
The Wendland ones,
CHIEF points
-->

<!-- # Quadrature

One of the harder aspects of BEM, when compared against FEM, is the evaluation of singular integrals. These typically occur on (and possibly close to) the diagonal entries $m=n$ of the linear system of equations.

If you are coding your own BEM, it is strongly recommended that you avoid writing your own quadrature rules from scratch, because there are lots of special cases to consider, and lots of mistakes can occur!

I will list below a few techniques which I have found useful in the past:

### Graded quadrature

This is the most generally applicable form of quadrature for singularities.

### Duffy Transformation

This should be used in conjunction with any other method for singular quadrature. -->


<!-- Link to Nick O's Green's function stuff here -->

<!-- We will use a second type of source, which is the normal derivate $\frac{\partial \Phi(x,y)}{\partial n(y)}$, i.e. the derivative taken outwards from the boundary $\partial \Omega$. Summing up lots of these sources at every point $y$ on the surface $\partial \Omega$, we arrive at the representation

$$
u^s(x) = \int_{\partial\Omega}\Phi(x,y)\phi(y)\ \mathrm{d}s(y) + \int_{\partial\Omega}\frac{\partial \Phi(x,y)}{\partial n(y)}\psi(y)\ \mathrm{d}s(y).
$$

We have arrived So if we can determine (or approximate) $\phi$ and $\psi$, we can determine (or approximate) $u^s$. It actually follows from Green's 2nd identity that we can express $\phi$ and $\psi$ in -->

<!-- Add a mathematical derivation too, but make it hidden -->
