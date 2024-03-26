# Monopoles and free space Green's Functions
Author: [Nick Ovenden](https://knowledgebase.acoustics.ac.uk/community/bios.html#nick-ovenden), 
edits: [Andrew Gibbs](https://knowledgebase.acoustics.ac.uk/community/bios.html#andrew-gibbs)

In a quiescent three-dimensional medium of constant sound speed $c$, any spherically symmetric time-harmonic source centred at a point $\mathbf{x_s}$ produces an externally outgoing acoustic field  of the form 

$$ p(\mathbf{x})=\mbox{Re} \left( \mathcal{S} \frac{e^{\mathrm{i} k |\mathbf{x} - \mathbf{x_s}|}}{|\mathbf{x} - \mathbf{x_s}|} \right), $$

where $\mathcal{S}$ is a complex number representing the strength and phase of the source. As one might expect, this expression is the solution everywhere 
to the following PDE 

$$ \left(\Delta + k^2 \right) p = -4\pi \mathcal{S} \delta(\mathbf{x} -\mathbf{x_s}) $$

in an external unbounded domain with *no incoming* waves from infinity and where $\delta(\mathbf{x})$ is the delta-dirac function. 
  Setting $\mathcal{S}= -\frac{1}{4\pi}$ leads to the so-called *free-field* or *free-space* Green's 
  function 
  
  ```{math}
  :label: eq-green
  \Phi(\mathbf{x},\mathbf{x_s})= -\frac{1}{4 \pi} \frac{e^{i\omega |\mathbf{x} - \mathbf{x_s}|/c}}{|\mathbf{x} - \mathbf{x_s}|},
  ```
  
  that solves 
  
  $$ \left(\Delta + k^2 \right) \Phi = \delta(\mathbf{x} -\mathbf{x_s}) $$
  
  in an externally unbounded domain. 
