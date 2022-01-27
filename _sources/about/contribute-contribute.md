# Contributing material to the site

If you choose to contribute, you may want to look at [How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github). In brief:

1. The published copy of the knowledgebase is in the main branch of the repository (so that GitHub will regenerate it automatically). Please create all branches from that, and merge the main repository's main branch into your main branch before starting work. Please do not work directly in your main branch, since that will make it difficult for you to work on other contributions.

2. We use [GitHub flow](https://guides.github.com/introduction/flow/) to manage changes:
    1. Create a new branch in your desktop copy of this repository for each significant change.
    2. Commit the change in that branch.
    3. Push that branch to your fork of this repository on GitHub.
    4. Submit a pull request from that branch to the main repository.
    5. If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.
	
The site has maintainers who review issues and pull requests or encourage others to do so. The maintainers are community volunteers, and have final say over what gets merged into the knowledgebase.

The majority of this guide is written in markdown (`.md`) and Jupyter notebook (`.ipynb`) files. Jupyter Books use MyST which is an extension of basic markdown syntax. See their [MyST cheatsheet](https://jupyterbook.org/reference/cheatsheet.html) for information about formatting. Markdown pages do not contain executable content, whereas the notebook files do. See the Jupyter Books [guide on writing executable content](https://jupyterbook.org/content/executable/index.html) for more information about notebooks. 

The structure and configuration of the book are determined by the YAML files `_toc.yml` and `_config.yml`. Don't edit these unless you know what you're doing!

If you are contributing a tutorial, please use the [tutorial template](code-template) provided.

```{warning}
If making changes via pull requests, only changes to markdown (`.md`), Jupyter notebook (`.ipynb`), and YAML (`.yml`) files will be accepted. Do not make edits to HTML content, or any other content in the `_build` folder or in the `gh-pages` branch, as these are automatically overwritten whenever the book is edited and rebuilt. 
```

By contributing, you agree that we may redistribute your work under our license. In exchange, we will address your issues and/or assess your change proposal as promptly as we can, and help you become a member of our community. Everyone involved in the Computational Acoustics Knowledgebase agrees to abide by our [code of conduct](code-of-conduct).