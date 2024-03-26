# Tutorial: 1D FEM Model of an Impedance Tube
Author: [Jonathan Hargreaves](https://www.salford.ac.uk/our-staff/jonathan-hargreaves)

This tutorial aims to introduce the basic concepts of FEM for the simplest acoustic model possible: 1D propagation of sound in a tube. This model has the benefit of being grounded in reality too - it simulates the acoustic behaviour in an <b>Impedance Tube</b>, as are used to measure the acoustic properties of materials. This measurement processes is standardised in ISO 10534-1:1996.

Our model will be simpler than the real thing, however:
* We'll assume that pressure and [particle velocity](https://en.wikipedia.org/wiki/Particle_velocity) are invariant over the cross-section of the tube, i.e., the possibility of circumferential or radial variation is ignored. This means we can model the system as a 1D interval - it's only argument is position $x$ along the tube;
* We will ignore structural transmission in the tube - this will be a model solely of the acoustic waves in the air in the tube;
* We won't model the interior of the absorption material - we will instead represent it by a boundary admittance.

Being 1D, the model is sufficiently simple that we can easily write out the equations, draw diagrams of the interpolation functions, and plot results. You will also see how this leads to a matrix equation, with predictable sparsity patterns, which we'll then solve to find the solution to the problem. This is a set of pressure coefficients at the mesh nodes, which are interpolated over the intervening elements to give a solution everywhere.

We will do this both for driven behaviour at a user-defined frequency (a <i>Frequency Response</i> study) and to find the undriven natural modes of the tube (an <i>eigenfrequency study</i>). Finally, we will compare the FEM solution to an analytical model so we can compute the RMS error and study solution convergence.

```{attention} Attention
There's a Matlab version of this sat on the Mural board. Someone needs to convert the Matlab to Numpy and re-write the tutorials as markdown. There is a comprehensive background theory document that you'll probably want to integrate too, possibly as an appendix. This markdown file will need to be converted into a Jupyter Notebook. 
```
