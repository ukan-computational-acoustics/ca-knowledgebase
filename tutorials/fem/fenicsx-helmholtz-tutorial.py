# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (DOLFINx complex)
#     language: python
#     name: python3-complex
# ---

# # The Helmholtz Equation with FEniCSx
# Authors: Stefano Tronci and Jørgen S. Dokken
#
# :::{note}
# You can run this code directly in your browser by clicking on the rocket logo ( <i class="fas fa-rocket"></i> ) at the top of the page, and clicking 'Binder'. This will open a Jupyter Notebook in a [Binder](https://mybinder.org/) environment which is set up to contain everything you need to run the code. **Don't forget to save a local copy if you make any changes!**
#
# If you prefer, you can download the Jupyter Notebook file to run locally, by clicking the download logo ( <i class="fas fa-download"></i> ) at the top of the page and selecting '.ipynb'.
#
# If you are new to using Jupyter Notebooks, [this guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) will help you get started.
# :::
#
# ## Prerequisites
#
# In order to be able to run the code presented in this tutorial you will need:
#
# * A working Python environment for your platform. For more information, refer to [the Python website](https://www.python.org/);
# * A working FEniCS installation within your Python environment. For more information, refer to [the FEniCSx documentation](https://docs.fenicsproject.org/dolfinx/main/python/installation);
# * The following Python packages installed in your environment:
#     * `numpy`;
#     * `pyvista`;
#     * `ipygany`;
#     
# A basic knowledge of Partial Differential Equations (PDEs) and FEM will be beneficial.
#
#
# ## Introduction
#
# This tutorial cover the basics on how to solve the Helmholtz equation with Neumann boundary conditions by using FEniCS.
#
# ### The Governing PDE
#
# #### Definitions
#
# We use the following symbols:
#
# * $\Omega$ denotes an open set of $\mathbb{R}^3$. $\partial \Omega$ denotes its boundary and $\overline{\Omega} \doteq \Omega \cup \partial \Omega$ it's closure. $\mathbf{x}$, a 3D vector, is the generic point in $\overline{\Omega}$.
# * $T$ denotes an open interval in $\mathbb{R}$ $t$ is the generic point in $T$.
# * We denote the laplace operator with $\nabla^2$.
# * We denote the Euclidean inner productwith $\cdot$.
#
# Note that we will index the components of vectors starting from $0$. This to be consistent with the Python programming language.
#
# $$ \mathbf{x} = \begin{bmatrix} x_{0} \\ x_{1} \\ x_{2} \end{bmatrix} \in \overline{\Omega}$$ 
#
#
# #### The Helmholtz Equation
#
# The lossless wave equation reads:
#
# $$
# \nabla^2 p\left(\mathbf{x},t\right) = \frac{1}{c^2}\frac{\partial^2 p\left(\mathbf{x},t\right)}{\partial t^2}
# $$
#
# Where $p = p \left(\mathbf{x},t\right)$ is the unknown pressure disturbance field, in Pascal. $p$ is defined in $\overline{\Omega} \times T$ and has complex values. $c$ is the phase speed of sound in the medium, in meters per second.
#
# We impose that the pressure field is a steady state harmonic field:
#
# $$
# p\left(\mathbf{x},t\right) = u\left(\mathbf{x}\right) \exp\left(j\omega t\right)
# $$
#
# Where $u$ is the unknown spatial part of the field. $u$ is defined in $\overline{\Omega}$ and has complex values. $j$ is the imaginary unit and $\omega$ is the angular frequncy of the field, in radians per second. If $\nu$ denotes the frequency in Hertz we have:
#
# $$ \omega = 2\pi\nu = kc$$
#
# With $k$ the wave number.
#
# By substituting into the wave equation we obtain the Helmholtz equation:
#
# $$
# \nabla^2 u\left(\mathbf{x}\right) + k^2\left(\mathbf{x}\right) = 0
# $$
#
# This is our governing PDE.
#
# #### Boundary Conditions
#
# The Helmholtz equation can be completed with Dirchlet, Neumann and Robin boundary conditions:
#
# * Dirchlet conditions are impose a specific value of $u$ on $\partial \Omega$.
# * Neumann conditions specify a normal particle velocity $\partial \Omega$.
# * Robin conditions specify an acoustic impedance on $\partial \Omega$ as well as an optional particle velocity.
#
# Whilst the Dirchlet conditions are the simplest to deal with we will focus on Neumann conditions in this tutorial. This because prescription of particle velocity is the most common boundary condition for simple simulations.
#
# Let $\partial \Omega_l$ denote a partition of $\partial \Omega$, with $l=0,1,2,\dots,L-1$, $L$ being the number of partitions. Let the complex valued function $w_l\left(\mathbf{x}\right)$ denote the prescribed normal component of the spatial part of the particle velocity field in $\partial \Omega _l$. Thanks to the Euler equation in frequency domain we have:
#
# $$
# \nabla u \left(\mathbf{x}\right) \cdot \hat{\mathbf{n}}\left(\mathbf{x}\right) = j\omega\rho w_l\left(\mathbf{x}\right) \text{ for } \mathbf{x} \in \partial \Omega_l, \space \forall \space l = 0, 1, 2, \dots, L - 1
# $$
#
# Where $\rho$ is the density of the medium and $\hat{\mathbf{n}}\left(\mathbf{x}\right)$ is the normal unit vector to $\partial \Omega$ in $\mathbf{x}$.
#
# We are now able to prescribe normal particle velocity at each value of the boundary. To simplify notation, we define the acoustic bounday fluxes $g_l\left(\mathbf{x}\right)$ as follows:
#
# $$
# g_l\left(\mathbf{x}\right) \doteq j\omega\rho w_l\left(\mathbf{x}\right)
# $$
#
# Hence, the equation bove reads:
#
# $$
# \nabla u \left(\mathbf{x}\right) \cdot \hat{\mathbf{n}}\left(\mathbf{x}\right) = g_l\left(\mathbf{x}\right) \text{ for } \mathbf{x} \in \partial \Omega_l, \space \forall \space l = 0, 1, 2, \dots, L - 1
# $$
#
# :::{note}
# Technically there is no need to partition $\partial \Omega$. One could have simply defined $w\left(\mathbf{x}\right)$ in $\partial \Omega$ and set it to the needed (eventual zero) values in the various parts of the boundary as needed. However it is easier to think in terms of partitions when working with FEniCS, as we will see.
# :::
#
# ### The Weak Form
#
# We need to convert our PDE into a weak form to solve our problem with FEniCS. This is done by recognising that $u$ is a vector of an appropriate Sobolev space. Then, another test function $\phi$ is taken from the Sobolev space, with the requirement of being $0$ on $\partial \Omega$. Multiplication of the governing PDE with $\phi$ and integration by parts lead to the weak form. The weak form reads:
#
# $$
# \int_\Omega \nabla u \cdot \nabla \phi^\star d\mathbf{x} - k^2 \int_\Omega u \phi^\star d\mathbf{x} = \sum_{l=0}^{L-1}\int_{\partial \Omega_l} g_l \phi^\star ds
# $$
#
# Where we simplified notation by dropping the functions arguments. $d\mathbf{x}$ denotes the volume element of $\Omega$ while $ds$ denotes the surface element in $\partial \Omega$. $\star$ denotes complex conjugation. Note that the equation above has the following form:
#
# $$
# a \left(u,\phi\right) = L\left(\phi\right)
# $$
#
# Where $a$ and $L$ are the bilinear and linear form respectively. FEniCS requires the specification of these two quantities.
#
# :::{note}
# The Neumann boundary conditions feature directly in the weak form. The same goes for Robin conditions. However, Dirchlet boundary conditions don't and are treated separately.
# :::
#
# ### More Details
#
# A similar tutorial for legacy FEniCS is presented at the links.
#
# * [Intro to FEniCS - Part 1](https://computational-acoustics.gitlab.io/website/posts/30-intro-to-fenics-part-1/).
# * [Intro to FEniCS - Part 2 ](https://computational-acoustics.gitlab.io/website/posts/31-intro-to-fenics-part-2/).
# * [Intro to FEniCS - Part 3 ](https://computational-acoustics.gitlab.io/website/posts/32-intro-to-fenics-part-3/).
#
# This tutorial focuses more on the code, whilst the ones above focus more on the derivation of the weak form.
#
# For more details about acoustics, FEniCS and computational methods the following books are recommended:
#
# * [Computational Acoustics of Noise Propagation in Fluids](https://link.springer.com/book/10.1007%2F978-3-540-77448-8).
# * [Solving PDEs in Python](https://link.springer.com/book/10.1007/978-3-319-52462-7).
# * [Fundamentals of Acoustics](https://www.wiley.com/en-gb/Fundamentals+of+Acoustics,+4th+Edition-p-9780471847892).
# * [The FEniCSx tutorial](https://jorgensd.github.io/dolfinx-tutorial/)
#
# ## Setup
#
# We now setup our simulation.
#
# First, we decide the shape of $\Omega$, then the properties of the medium and then the boundary conditions.
#
# ### Domain
#
# We choose a rectangular room with the following geometry:
#
# | Dimension | Symbol    | Value      |
# |-----------|-----------|------------|
# | Length    | $d_{x_0}$ | $4$ meters |
# | Width     | $d_{x_1}$ | $5$ meters |
# | Height    | $d_{x_2}$ | $3$ meters |
#
# Hence $\Omega = \left(0, d_{x_0} \right) \times \left(0, d_{x_1} \right) \times \left(0, d_{x_2} \right)$.
#
#
# ### Medium Properties
#
# We choose air at room temperature:
#
# | Property       | Symbol | Value                             |
# |----------------|--------|-----------------------------------|
# | Speed of Sound | $c$    | $343$ meters per second           |
# | Density        | $\rho$ | $1.205$ kilograms per cubic meter |
#
#
# ### Boundaries
#
# We partition $\partial \Omega$ in the $6$ walls of the room. We make $5$ of the rigid (normal particle velocity set to $0$) while we make one having uniform velocity.
#
# | Boundary Definition                                                                      | Particle Velocity Definition     |
# |------------------------------------------------------------------------------------------|---------------------------------------|
# | $ \partial \Omega_0 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_0 = 0 \right\} $ | $ w_l \left(\mathbf{x}\right) = 0 $ |
# | $ \partial \Omega_1 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_0 = d_{x_0} \right\} $ | $ w_l \left(\mathbf{x}\right) = 0 $ |
# | $ \partial \Omega_2 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_1 = 0 \right\} $ | $ w_l \left(\mathbf{x}\right) = 10 $ |
# | $ \partial \Omega_3 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_1 = d_{x_1} \right\} $ | $ w_l \left(\mathbf{x}\right) = 0 $ |
# | $ \partial \Omega_4 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_2 = 0 \right\} $ | $ w_l \left(\mathbf{x}\right) = 0 $ |
# | $ \partial \Omega_5 \doteq \left\{ \mathbf{x} \in \overline{\Omega} : x_2 = d_{x_2} \right\} $ | $ w_l \left(\mathbf{x}\right) = 0 $ |
#
# ### The Code
#
# All the ingredients are ready to put together the simulation.
#
# #### Importing the Needed Packages
#
# We start by importing what we need:

import numpy as np
import dolfinx
import ufl
from petsc4py import PETSc
import pyvista
from mpi4py import MPI

# #### Simulation Parameters
#
# We then define all the parameters:

# +
nu = 57.17  # Frequency of the Simulation, Hz
c = 343  # Speed of sound in air, m/s
rho = 1.205  # Density of air, kg/m^3
w = 10  # Velocity normal to boundary, for inflow Neumann condition, m/s
d_x0 = 4.  # Room size along x0, m
d_x1 = 5.  # Room size along x1, m
d_x2 = 3.  # Room size along x2, m
tol = 1e-10 # Tolerance for boundary condition definitions

omega = 2 * np.pi * nu  # Angular frequency, rad/s
k = omega / c  # Wave number, rad/m
# -

# #### Domain Definition and Meshing
#
# FEniCS solves our PDE through FEM. FEM makes use of two steps:
#
# * Derivation of the weak form;
# * Domain meshing;
#
# We already derived the weak form for our problem. Domain meshing is instead what allows to reach an approximate numerical solution for our PDE. Meshing means that $\Omega$ is cut into many non-overlapping subvolumes. We already mentioned how our uknown pressure spatial part $u$ is a vector in a Sobolev space. Through meshing we simplify this space to one that has _finite dimension_. This also transforms the integrals of the weak form in sums, which are then expressed as matrix-vector operations. We do not need to worry about these details: we specify the mesh and FEniCS will take care of the rest.
#
# FEM solutions converge to the actual PDE solution the finer the mesh and the higher the order. Each element of the mesh needs to be smaller than one tenth of the wavelenght for wave solutions to be satisfyingly accurate. Here we will match the element size to one 11-th of the wavelength:

s = c / (11 * nu)  # Element Size
n_x0 = np.intp(np.ceil(d_x0 / s))  # Number of elements for each direction
n_x1 = np.intp(np.ceil(d_x1 / s))
n_x2 = np.intp(np.ceil(d_x2 / s))

# Now it is the time do define the mesh. Since we have a rectangular room we use the `dolfinx.mesh.create_box` [function](https://docs.fenicsproject.org/dolfinx/main/python/generated/dolfinx.mesh.html?highlight=create_box#dolfinx.mesh.create_box):

mesh = dolfinx.mesh.create_box(
    MPI.COMM_WORLD,
    [[0, 0, 0],[d_x0, d_x1, d_x2]],
    [n_x0, n_x1, n_x2])

# We then define the element type as a second order Lagrange element. This means that whith each element we express the unknown field as a linear superposition of second order Lagrange polynomials. FEM finds an approximate solution to the PDE by finding the coefficients of this superposition.

P = ufl.FiniteElement("Lagrange", mesh.ufl_cell(), 2)

# #### Function Space
#
# Now we can go ahead and define a function space for the approximate solution.

V = dolfinx.fem.FunctionSpace(mesh, P)

# The formulation of the weak form in the simplified space is the same as in the original Sobolev space, except that the integrals reduce to sums. We do not need to worry about it as we simply need to specify the terms of the weak form.
#
# #### Bilinear Form 
#
# In this function space `V` we pickup a generic function `u` from the space `V`, which contains all the possible approximate solutions (i.e. the Trial Function). Then, we take any test function `phi` with which we formulate the weak form.

u = ufl.TrialFunction(V)
phi = ufl.TestFunction(V)

# We are now ready to specify the bilinear form

k_sq = dolfinx.fem.Constant(mesh, PETSc.ScalarType(k**2))
a = ufl.inner(ufl.nabla_grad(u), ufl.nabla_grad(phi)) * ufl.dx \
            - k_sq * ufl.inner(u, phi) * ufl.dx


# :::{note}
# You should pay attention to the fact that we use `inner` and `nabla_grad`. For complex-valued problems you need to use `ufl.inner` and *always* have the `TestFunction` as the second argument. However, they will for vector fields. You should always pick the most appropriate function for your problem. For an overview, see [page 25](https://link.springer.com/content/pdf/10.1007%2F978-3-319-52462-7.pdf#%5B%7B%22num%22%3A302%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C666%2Cnull%5D) and [page 58](https://link.springer.com/content/pdf/10.1007%2F978-3-319-52462-7.pdf#%5B%7B%22num%22%3A430%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C666%2Cnull%5D) of [Solving PDEs in Python](https://link.springer.com/content/pdf/10.1007%2F978-3-319-52462-7.pdf) and the [UFL-documentation](https://fenics.readthedocs.io/projects/ufl/en/latest/manual/form_language.html?highlight=complex#complex-values)
# :::
#
#
# #### Boundary Conditions
#
# As we seen in the definition of the bilinear form `a` FEniCS does not have a symbol for integral. We specify instead the integration variable. Above we used `fenics.dx` which is the integration variable for the volume. If we had different submodules we could define custom `dx` values to specify integration within the subvolumes. We will do something along these lines to specify the boundaries.
#
# To tell FEniCS that we have 6 sub-boundaries we need to create 6 markers, that indicate what the coordinates of each region is.
#
# We then create a `MeshTag`, a collection of facets with different integers markers for each region.
#
# First, let's create the sub-domain markers.

# +
def BX0(x):
    return np.isclose(x[0], 0)

def BXL(x):
    return np.isclose(x[0], d_x0)

def BY0(x):
    return np.isclose(x[1], 0)

def BYL(x):
    return np.isclose(x[1], d_x1)

def BZ0(x):
    return np.isclose(x[2], 0)

def BZL(x):
    return np.isclose(x[2], d_x2)


# -

# We are using the `numpy` function [isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html) since we are dealing with the mesh coordinates, which is expressed as floating point values. This means that there might be small errors; a point `x[0]` can have the value `2.22e-16` instead of `0`.
#
# Now, we find all facets on the boundary of our mesh using [dolfinx.mesh.locate_entities_boundary](https://docs.fenicsproject.org/dolfinx/v0.4.1/python/generated/dolfinx.mesh.html?highlight=locate_entities_boundary#dolfinx.mesh.locate_entities_boundary)

X0_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BX0)
X0_values = np.full_like(X0_facets, 1)
XL_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BXL)
XL_values = np.full_like(XL_facets, 2)
Y0_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BY0)
Y0_values = np.full_like(Y0_facets, 3)
YL_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BYL)
YL_values = np.full_like(YL_facets, 4)
Z0_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BZ0)
Z0_values = np.full_like(Z0_facets, 5)
ZL_facets = dolfinx.mesh.locate_entities_boundary(mesh, mesh.topology.dim-1, BZL)
ZL_values = np.full_like(ZL_facets, 6)
facets = np.hstack([X0_facets, XL_facets, Y0_facets, YL_facets, Z0_facets, ZL_facets])
values = np.hstack([X0_values, XL_values, Y0_values, YL_values, Z0_values, ZL_values])
sort_order = np.argsort(facets)

# Next we make the collection of facets and values

facet_tags = dolfinx.mesh.meshtags(mesh, mesh.topology.dim-1, facets[sort_order], values[sort_order])

# Now that this is done we can define the custom integration variables `ds` for our boundary. `ds` will return the measure for each different boundary if we use, as input, the ID for that boundary. For example, `ds(5)` will return the integration variable for the `bz0` boundary. Note that we apply a non-zero velocity to `by0`, which has ID `3`.

ds = ufl.Measure('ds', domain=mesh, subdomain_data=facet_tags)

# Now we simply need to define the acoustic fluxes. We need two: one for the rigid walls and one for the active walls

# +
# The flux is 0 for all rigid walls
g_rig = dolfinx.fem.Constant(mesh, PETSc.ScalarType(0))

# The flux is this for the active walls
g_in = dolfinx.fem.Constant(mesh, 1j * omega * rho * w)
# -

# #### Linear Form 
# We create the linear form, by splitting the boundary integral into the 6 regions.

L = ufl.inner(g_rig, phi)*ds((1,2,4,5,6)) + ufl.inner(g_in, phi)*ds(3)

# #### Solution
#
# Now that we have both the bilinear form `a` and the linear form `L` properly defined it is easy to solve for the approximate PDE solution. We create a function to hold the discrete solution `uh` with a new function from `V` in which we want to store our result. Then, we create a `dolfinx.fem.LinearProblem` class, that sets up all the structures need to solve the linear algebra problem.

uh = dolfinx.fem.Function(V)
problem = dolfinx.fem.petsc.LinearProblem(a, L, u=uh)

# We next call `problem.solve()` to solve the PDE.

problem.solve()

# #### Visualizing Results
#
# `u` contains the real and imaginary parts of the field. We visualize each of them separatly.

pyvista.set_jupyter_backend("pythreejs")
p_mesh = pyvista.UnstructuredGrid(*dolfinx.plot.create_vtk_mesh(mesh, mesh.topology.dim))
pyvista_cells, cell_types, geometry = dolfinx.plot.create_vtk_mesh(V)
grid = pyvista.UnstructuredGrid(pyvista_cells, cell_types, geometry)
grid.point_data["u_real"] = uh.x.array.real
grid.point_data["u_imag"] = uh.x.array.imag
grid.set_active_scalars("u_real")

# +
p_real = pyvista.Plotter()
p_real.add_text("uh real", position="upper_edge", font_size=14, color="black")
p_real.add_mesh(grid, show_edges=True, style="points", point_size=25)
p_real.add_mesh(p_mesh, show_edges=True, style="wireframe")
if not pyvista.OFF_SCREEN:
    p_real.show()

with dolfinx.io.VTXWriter(mesh.comm, "output.bp", [uh]) as vtx:
    vtx.write(0.0)

# +
p_imag = pyvista.Plotter()

grid.set_active_scalars("u_imag")
p_imag.add_mesh(p_mesh, show_edges=True, style="wireframe")
p_imag.add_text("uh imag", position="upper_edge", font_size=14, color="black")
p_imag.add_mesh(grid, show_edges=True, style="points", point_size=25)
if not pyvista.OFF_SCREEN:
    p_imag.show()

# -

# ### A Comment About the Solution
#
# You have probably noticed that the real part of the solution is pretty much 0 everywhere. This is to be expected because:
#
# * The material is lossless;
# * The flux is purely imaginary;


