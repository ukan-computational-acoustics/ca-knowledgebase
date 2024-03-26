# Acoustic Boundary Conditions
Author: [Huiqing Wang](https://knowledgebase.acoustics.ac.uk/community/bios.html#huiqing-wang)

Acoustic boundary conditions are necessary components in the simulation of sound within a given open or closed environment. They define how sound waves interact with surfaces and obstacles, which is crucial for accurate modeling in computational acoustics. They help in determining how sound waves reflect, absorb, or transmit at these boundaries. Implementing realistic boundary conditions is key to ensuring that numerical simulations closely mirror real-world acoustics. This page provides an overview of the different types of acoustic boundary conditions, their practical implementation, and their applications in computational acoustics.

## Understanding Boundaries

Boundaries in acoustics can be physical, like the walls of a room, or virtual, such as the limits of a simulated environment. The choice of boundary conditions affects the fidelity of the simulation and can greatly influence the results of acoustic analyses.

By the end of this section, you will have a clearer understanding of the different types of acoustic boundary conditions and their applications in computational models. 

## Importance of Accurate Boundary Conditions

Accurate boundary conditions are essential for:

- Ensuring the reliability of simulation results.
- Predicting acoustic performance in real-world scenarios.
- Optimizing designs for acoustic spaces like concert halls, auditoriums, and open-plan offices.

## Types of Acoustic Boundary Conditions

Acoustic boundary conditions are categorized based on their interaction with sound waves. The proper application of these types is crucial for realistic acoustic modeling.

### Absorbing/Non-reflecting Boundaries

These boundaries aim to emulate open space by allowing sound waves to pass through without reflection. They are critical in preventing false echoes in computational domains.

### Hard Boundaries

These simulate the echo effect of sound waves bouncing off hard surfaces. They are commonly implemented in models representing enclosed spaces such as rooms.

### Impedance Boundaries

Boundary conditions that characterize acoustic properties of surface materials by relating the acoustic pressure $p$ to the normal component of the particle velocity $v_n$ on the boundaries. 

### Periodic Boundaries

For modeling repetitive structures, periodic boundaries ensure the sound wave pattern is consistent across the model's unit cells.

### Symmetry Boundaries

Applied to symmetric models, these boundaries assume a mirror image of the sound field, reducing computational complexity and resource requirements.



## Practical Implementation

The translation of mathematical formulations of acoustic boundary conditions into practical computational models is a crucial step in computational acoustics. Here, we outline how to implement these conditions in simulations effectively.

### Implementing Boundary Conditions in Models

Implementing boundary conditions typically involves the following steps:

1. Identify the type of boundary condition relevant to the simulation scenario.
2. Translate the mathematical expressions of the boundary conditions into the discretized form compatible with the numerical method being used, such as Finite Element Method (FEM) or Finite Difference Time Domain (FDTD).
3. Apply the discretized boundary conditions at the appropriate points in the computational domain, ensuring that they are consistent with the overall physical model.

### Common Pitfalls and How to Avoid Them

- **Reflections from Boundaries**: Care must be taken to ensure that artificial reflections do not occur from the boundaries, unless they are part of the physical scenario being modeled.
- **Mismatched Impedance**: When dealing with impedance boundaries, it is essential to match the impedance accurately to prevent the generation of spurious reflections or transmission errors.
- **Numerical Instability**: Incorrect implementation of boundary conditions can lead to numerical instability. This can be mitigated by verifying the stability of the algorithm through convergence tests.

### Tips for Effective Implementation

- Always validate your model against known analytical solutions or experimental data to ensure that the boundary conditions are correctly implemented.
- Use visualization tools to monitor the behavior of the acoustic field near the boundaries to detect any anomalies that might indicate problems with the boundary condition implementation. A starightforward test case of single reflection can be used to verify the boundary condition implementation.

## Applications in Computational Acoustics

The correct application of acoustic boundary conditions is vital for a range of computational acoustics simulations. This section showcases their importance and provides insights into their practical utility.


### Room Acoustics 
Sound absorption along surfaces of various objects inside a room has a major influence on the acoustics of the room. Therefore, in room acoustics simulations, boundary conditions are crucial for accurately predicting the room acoustic parameters (*e.g.*, reverberation time) in enclosed spaces. In various room acoustic modeling techniques, the boundary conditions that represent the sound absorption properties of materials can be characterized in terms of either the acoustic surface impedance, the sound absorption coefficient or the plane-wave reflection coefficient. These quantities in general vary with the frequency and the angle of incidence. The absorption coefficient is usually used in geometrical acoustics models, while the acoustic surface impedance comes into play in wave-based methods (*e.g.*, FEM, BEM, FDTD, DG, *etc.*) through the imposition of boundary conditions.

Suppose the outward normal vector to the boundary surface is denoted as $\boldsymbol n$. At a given angular frequency $\omega$, the normalized surface impedance $Z_s$, is defined as the ratio of the complex sound pressure $P(\omega)$ and the particle velocity component normal to the surface $V_n(\omega)=\boldsymbol V(\omega)\cdot \boldsymbol n$,  divided by the characteristic impedance of air, *i.e.,* 

$$
\begin{equation}
	Z_s(\omega)=\frac{1}{\rho_0 c_0}\frac{P(\omega)}{V_n(\omega)}.
\end{equation}
$$

In the time domain,  above relation can be expressed as:

$$
\begin{equation}
	p(t)={\rho_0 c_0}\int_{-\infty}^{\infty} z_s(t-\tau)v_n(\tau)\mathrm{d}\tau,
\end{equation}
$$

where $z_s(t)$ is the inverse Fourier transform  of $Z_s(\omega)$, and the same holds for $p(t)$ and $v_n(t)$.

The impedance model has to satisfy three necessary conditions in the frequency domain in order to be physically admissible, as proposed by Rienstra {cite}`rienstra2006impedance`:

-  Causality condition:  the present states must be time-updated based on the past and present states. In other words, the response of the system is supposed to be zero before it is simulated. Mathematically, it indicates that $Z_s(\omega)$ is analytic and non-zero in $\mathrm{Im}(\omega) <0$;
-  Reality condition: $p(t), v_n(t)$ and $z(t)$ must be real-valued quantities. In other words, $Z_s^*(\omega)=Z_s(-\omega)$, where the superscript $*$ denotes the complex conjugate;
- Passivity condition: the reflecting  surfaces absorb energy rather than generate it. Consequently, $\mathrm{Re}\big(Z_s(\omega)\big)\geq 0$ must hold for all frequencies.

The physical admissibility of some popular semi-empirical impedance models are discussed in {cite}`dragna2014physically`.

The physics behind the reflection of sound waves is well described by Snell's law. However, the fact that surface impedance values vary with the incidence angle of the impinging sound wave, which is referred to as extendedly reacting behavior, poses great challenges to numerical modeling. To deal with this issue, a general approach is to couple the sound propagation between the boundary materials and the air, by explicitly solving the governing equations inside the materials. However, this coupling approach, which requires problem-dependent treatments, suffers from the extra computational cost of modeling the boundary materials {cite}`wang2023extended`. 

### Outdoor Sound Propagation
In outdoor sound propagation simulations, the boundary conditions are crucial for accurately predicting the sound pressure levels in the far field. The use of non-reflecting boundary conditions is essential to prevent spurious reflections that can distort the results. In outdoor sound propagation models, the boundary conditions are typically implemented as absorbing boundaries that attenuate the sound waves as they propagate away from the source. This helps in simulating the dissipation of sound energy over distance and predicting the sound levels at different locations in the outdoor environment.
To be finished.

### Aeroacoustics
In aeroacoustics simulations, the boundary conditions play a critical role in capturing the noise generated by moving objects, such as aircraft or vehicles. The accurate representation of the boundaries is essential for predicting the noise levels generated by these objects and assessing their impact on the surrounding environment. In aeroacoustics models, the boundary conditions are often implemented as impedance boundaries that account for the acoustic properties of the surfaces and the surrounding medium. This helps in simulating the noise generated by the moving objects and predicting the sound levels at different locations in the vicinity of the objects.
To be finished.


## Advanced Topics

Diving deeper into acoustic boundary conditions, we may encounter scenarios where standard approaches may not suffice. 

### Non-linear Boundary Conditions

Non-linear boundary conditions come into play when dealing with sound levels that induce non-linear behaviors in the medium or at the boundary, such as:

- **Shock Waves**: Where the pressure changes are so rapid and intense that linear approximations fail.
- **High-Intensity Acoustic Fields**: Common in ultrasonic applications, where the medium's response is no longer linearly related to the input sound field.

### Time-dependent and Frequency-dependent Conditions

Some boundary conditions change over time or vary with frequency, which is critical for:

- **Time-Variant Surfaces**: Such as moving boundaries in machinery or biological tissues in medical acoustics simulations.
- **Frequency-Selective Surfaces**: Used in the design of acoustic filters and barriers that behave differently at various frequencies.

