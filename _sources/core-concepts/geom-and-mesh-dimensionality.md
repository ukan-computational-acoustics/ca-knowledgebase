# Dimensioanlity

## Authors:
[Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves)
[Amelia Gully](https://knowledgebase.acoustics.ac.uk/community/bios.html#amelia-gully)

```{warning}
This part of the site is currently under development. Its content is incomplete.
```

Will the mesh be set up in one, two or three dimensions? Waht about axisymmetry? The more dimensions, the greater the computational cost of your model. If your model is regular or symmetrical, you may be able to exploit this to reduce the problem size.

```{note}
For FEM & FDTD this modifies the PDE. For BEM, this modifies the Green's function. Compactness can be an issue for the latter.
```

### 1D

```{figure} geom-and-mesh-dimensionality-1D.png
---
name: 1D Geometry
---
1D Geometry. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves)
```
Decribe here what the image shows
* Domain is an interval
* Boundaries are points

### 2D

```{figure} geom-and-mesh-dimensionality-2D.png
---
name: 2D Geometry
---
2D Geometry. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves)
```
Decribe here what the image shows
* Domain is an area
* Boundary is a line

### 3D

```{figure} geom-and-mesh-dimensionality-3D.png
---
name: 3D Geometry
---
3D Geometry. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves). Depicts the [University of Salford Listening Room](https://acoustictesting.salford.ac.uk/acoustic-laboratories/listening-room/).
```
Decribe here what the image shows
* Domain is a volume
* Boundary is a surface


## Examples Computational Cost Savings - Meshing a Loudspeaker

### 2D Axisymmetric
```{figure} geom-and-mesh-meshing-axi2D.png
---
name: 2D Axisymmetric Mesh
---
2D Axisymmetric Mesh. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves). Produced using [Gmsh](https://gmsh.info/)
20 elements.

### Full 3D
```{figure} geom-and-mesh-meshing-3D.png
---
name: 3D  Mesh
---
3D Mesh. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves). Produced using [Gmsh](https://gmsh.info/)
2667 elements.
