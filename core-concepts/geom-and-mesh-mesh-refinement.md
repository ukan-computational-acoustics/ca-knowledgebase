# Meshes
Author: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves), [Amelia Gully](https://knowledgebase.acoustics.ac.uk/community/bios.html#amelia-gully)

```{admonition} Alpha mode!
:class: tip
This page is in alpha mode. That means its content has not yet been thoroughly reviewed.

If you would like to contribute suggestions or corrections, please do so following the [guide for contributors](../about/contribute-contribute).
```

The _mesh_ is a representation of a domain by [unstructured elements](element-types) and how the mesh is set up is a major factor in how accurate a simulation will be.

* *Element size*: smaller elements result in greater accuracy, at the expense of increased computational cost. The process of reducing the element size to increase accuracy is called "h-refinement" (see Figure below).

```{figure} geom-and-mesh-mesh-refinement.JPG
---
name: h-refinement
---
h-refinement. Image produced by: [COMSOL](https://www.comsol.com/model/tuning-fork-8499).
```

Mesh generation is an art in itself. Commercial CA software usually include proprietary mesh generation routines, whereas open-source solvers typically don't. Here are some open-source meshing solutions you might like to explore:

* [*Gmsh*: A three-dimensional finite element mesh generator with built-in pre- and post-processing facilities](https://gmsh.info/)
* [*MeshLab*: An open source system for processing and editing 3D triangular meshes](https://www.meshlab.net/)
* [*Salome MESH*: the mesh module of the SALOME open source platform for numerical simulation](https://www.salome-platform.org/?page_id=374)
