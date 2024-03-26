# Finite Difference
Authors: [Amelia Gully](https://knowledgebase.acoustics.ac.uk/community/bios.html#amelia-gully)

```{warning}
This part of the site is currently under development.
```

The finite difference (FD) approach is a way of approximating a solution to a partial differential equation (PDE). In a differential equation, we have a differential term. Recall that a differential term describes a _gradient_, calculated over infinitestimally-small steps (i.e. XX tends to XX). A finite difference is a way of approximating the gradient by using steps of a known, finite size instead. We can then use this as an approximation to the true solution.

In acoustics, we are often dealing with the _wave equation_, so we will use this as an example here. The wave equation describes how acoustic pressure varies as a function of time (t) and space (x,y,z). For simplicity, let us consider only 1D wave propagation here, so spatial position is described by a single variable, x.

## Equation to approximate
The 1D wave equation is constructed as follows:

XX

We will solve this by using a _finite difference_ approach to the differential terms. Therefore we replace XX by XX, and XX by XX. In doing this, we no longer require differentiation, and we can easily calculate an approximate solution given initial and boundary conditions.

## Types of finite difference
We can use different kinds of "steps" to approximate our gradient, depending on the requirements of the problem. The simplest approach - and one that it is safe to use if you have no requirements otherwise - is the _central_ difference. 

(TODO: include wikimedia image here)

## Further reading

(TODO add)
