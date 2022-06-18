# Geometry and Meshing

## Authors:
[Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves)

```{warning}
This part of the site is currently under development. Its content is incomplete.
```

This page will discuss the differences between geometry and a mesh
It will also signpost the sub-pages.


## Geometry
* Exact definition of geometry (correct curvature etc.)
* Surface sections can be large w.r.t. wavelength
```{figure} geom-and-mesh-geom.png
---
name: Exhaust Muffler Geometry
---
Exhaust Muffler Geometry. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves). Produced using [COMSOL Multiphysics&trade;](https://www.comsol.com/)
```

## Mesh
* Approximate version of geometry
  * nodes ‘sampled’ from geometry then curvature of elements is interpolated
* Elements should be small w.r.t. wavelength
```{figure} geom-and-mesh-mesh.png
---
name: Exhaust Muffler Mesh
---
Exhaust Muffler Mesh. Image credit: [Jonathan Hargreaves](https://knowledgebase.acoustics.ac.uk/community/bios.html#jonathan-hargreaves). Produced using [COMSOL Multiphysics&trade;](https://www.comsol.com/)
```

```{note}
I have some cateye geometries & meshes created in Gmsh if we prefer to avoid COMSOL ones?
```


