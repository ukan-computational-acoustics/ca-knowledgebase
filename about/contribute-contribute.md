# Contributing material to the site

The source code of this knowledgebase can be found on [Github](https://github.com/ukan-computational-acoustics/ca-knowledgebase). The site is hosted
using GitHub pages, and will automatically rebuild after every change to the main branch.

If you are new to using GitHub, you may find our [getting started with GitHub guide](contribute-github) useful.

The site has maintainers who review issues and pull requests or encourage others to do so. The maintainers are community volunteers, and have final
say over what gets merged into the knowledgebase. Pull requests must receive at least one 'approval' before they can be merged.

The majority of this guide is written in markdown (`.md`) and Jupyter notebook (`.ipynb`) files. Jupyter Books use MyST which is an extension of basic
markdown syntax. See their [MyST cheatsheet](https://jupyterbook.org/reference/cheatsheet.html) for information about formatting. Markdown pages do not
contain executable content, whereas the notebook files do. See the Jupyter Books
[guide on writing executable content](https://jupyterbook.org/content/executable/index.html) for more information about notebooks. 

The structure and configuration of the book are determined by the YAML files `_toc.yml` and `_config.yml`. Don't edit these unless you know what you're doing!

If you are contributing a tutorial, please use the tutorial template provided. This can be found at
https://github.com/ukan-computational-acoustics/ca-knowledgebase/blob/main/about/code-template.ipynb.
You can see what this template looks like when turned into a section of the knowledgebase by viewing [this tutorial template page](code-template).

Once you have contributed to the knowledgebase, please add yourself to the [author biographies](commubity/bios.md) page.

```{warning}
If making changes via pull requests, only changes to markdown (`.md`), Jupyter notebook (`.ipynb`), and YAML (`.yml`) files will be accepted. Do not make edits to
HTML content, or any other content in the `gh-pages` branch, as these are automatically overwritten whenever the book is edited and rebuilt. 
```

By contributing, you agree that we may redistribute your work under our license. In exchange, we will address your issues and/or assess your change proposal as
promptly as we can, and help you become a member of our community. Everyone involved in the Computational Acoustics Knowledgebase agrees to abide by our
[code of conduct](../CODE_OF_CONDUCT).
