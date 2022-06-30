# Glossary

A glossary of common terms used throughout the knowledgebase. 

```{glossary}

Absorbing boundary condition (ABC)
    Condition applied at the edges of a computational domain to eliminate (or minimise) reflections.
	
Boundary element method (BEM)
    A computational method for solving linear PDEs for which Green's functions can be calculated. BEM calculates a solution at the boundary of a domain, reducing the dimensionality of the problem. 

Courant–Friedrichs–Lewy (CFL) condition
    A necessary condition for convergence in analysing explicit time integration schemes. See [Core Concepts: CFL Condition](todo:add_link) for more details.

Explicit scheme
    An explicit time-stepping scheme is one where the solution at time step n+1 is calculated based on existing (known) values from time step n.
	
Finite difference time domain (FDTD) method
    A computational method for solving time-dependent PDEs which uses a regular grid to discretise a domain. As a time-domain method, FDTD simulations cover a wide frequency range in a single simulation run.
	
Finite element method (FEM)
    A computational method for solving PDEs by discretising a domain into smaller elements governed by simpler relationships, and combining the contribution of these elements to approximate the function across the whole domain. 

Homogeneous domain
    A homogeneous domain has the same material properties (e.g. density, speed of sound...) throughout the domain.
	
Heterogeneous domain
    A heterogeneous (or inhomogeneous) domain has material properties (e.g. density, speed of sound...) that vary throughout the domain.
	
Implicit scheme
    An implicit time-stepping scheme is one where the solution at time step n+1 is calculated using the (unknown) values at time step n+1, requiring the solution of an ODE.

Jupyter Book
    [Jupyter Book](https://jupyterbook.org/intro.html) is an open source project for building beautiful, publication-quality books and documents (like this one!) from computational material. 

Ordinary differential equation (ODE)
    An equation involving derivatives in a single variable (e.g. how an acoustic field varies with time).

Partial differential equation (PDE)
	An equation involving partial derivatives in multiple variables (e.g. how an acoustic field varies with time and multiple spatial dimensions). Most of the equations of interest in computational acoustics are PDEs.

Perfectly matched layer (PML)
    An artificial ABC with non-physical properties which vary gradually throughout the layer in order to ensure that no energy is reflected into the interior of the domain.
```

If you'd like to suggest a glossry item or add a definition, please click the <i class="fab fa-github"></i> GitHub logo at the top of this page and select <i class="fas fa-lightbulb"></i> Open Issue, and include the details there.
