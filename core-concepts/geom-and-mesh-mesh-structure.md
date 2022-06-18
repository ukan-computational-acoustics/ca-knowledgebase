# Mesh Structure


```{admonition} Alpha mode!
:class: tip
This page is in alpha mode. That means its content has not yet been thoroughly reviewed.

If you would like to contribute suggestions or corrections, please do so following the [guide for contributors](../about/contribute-contribute).
```

Most computational acoustics methods approximate a solution to some differential equation by breaking a domain down into small, simple units which are usually called _elements_.

There are two main categories of elements:-

* *Structured* elements are all the same shape and size within a domain. As a result, the same relationships hold across every element and solutions can usually be calculated relatively efficiently. Typically, elements will form a Cartesian grid, although this is not a requirement. It may be difficult to accurately represent curved surfaces with structured elements.
* *Unstructured* elements will have the same topology throughout a domain (e.g. all elements will be triangular or quadrilateral) but elements can vary in shape and size throughout the domain depending on the requirements of the problem. For example, many smaller elements can be included where more detail is required. As there is not a single description of element behaviour, calculations necessarily become more resource-intensive. 

The data used for simulation is also likely to be in one of the two formats. Image and volume data can be considered _structured_ formats (where pixels and voxels comprise the elements), and mesh data (probably the most common format for computational acoustics problems) is _unstructured_. We discuss meshes in more detail in the next section.

Different computational acoustics methods use different element types. FEM and BEM typically use unstructured elements, while FDTD uses structured elements, as illustrated in the figure below.

```{figure} geom-and-mesh-mesh-structure.JPG
---
name: element-types
---
Types of element in computational acoustics. Image produced by: [Jonathan Hargreaves](https://www.salford.ac.uk/our-staff/jonathan-hargreaves).
```
