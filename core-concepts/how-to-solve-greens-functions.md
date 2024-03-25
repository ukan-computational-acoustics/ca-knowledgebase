# Monopoles and free space Green's Functions
Author: [Nick Ovenden](https://knowledgebase.acoustics.ac.uk/community/bios.html#nick-ovenden)

In a quiescent medium of constant sound speed $c$, any spherically symmetric time-harmonic source centred at a point $\mathbf{x_s}$ of angular frequency $\omega$ produces an externally outgoing 
acoustic field  of the form 

$$ p(\mathbf{x})=\mbox{Re} \left( \mathcal{S} \frac{e^{i\omega |\mathbf{x} - \mathbf{x_s}|/c}}{|\mathbf{x} - \mathbf{x_s}|} \right), $$

where $\mathcal{S}$ is a complex number representing the strength and phase of the source. As one might expect, this expression is the solution everywhere 
to the following PDE 

$$ \left(\nabla^2 + \frac{\omega^2}{c^2} \right) p = -4\pi \mathcal{S} \delta(\mathbf{x} -\mathbf{x_s}) $$

in an external unbounded domain with *no incoming* waves from infinity and where $\delta(\mathbf{x})$ is the delta-dirac function. 
  Setting $\mathcal{S}= -\frac{1}{4\pi}$ leads to the so-called *free-field* Green's 
  function 
  
  ```{math}
  :label: eq-green
  G_f(\mathbf{x},\mathbf{x_s})= -\frac{1}{4 \pi} \frac{e^{i\omega |\mathbf{x} - \mathbf{x_s}|/c}}{|\mathbf{x} - \mathbf{x_s}|},
  ```
  
  that solves 
  
  $$ \left(\nabla^2 + \frac{\omega^2}{c^2} \right) G_f = \delta(\mathbf{x} -\mathbf{x_s}) $$
  
  in an externally unbounded domain. 
