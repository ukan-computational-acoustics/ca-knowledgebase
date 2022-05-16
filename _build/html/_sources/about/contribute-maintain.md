# For maintainers

This site runs using [Jupyter Books](https://jupyterbook.org/intro.html). If you have not used Jupyter Books before, please complete their [tutorial on creating your first book](https://jupyterbook.org/start/your-first-book.html) before contributing. Note that Windows users will need to use Python 3.7.

First ensure you have Jupyter Books installed:

```
pip install -U jupyter-book
```

In order to build the book, create your own fork of the [knowledgebase repository](https://github.com/agully1/agully1.github.io). Then clone this repository to a local repository on your machine (N.B. if you are new to git on the command line, consider completing the [Software Carpentry lesson on version control with git](https://swcarpentry.github.io/git-novice/)):

```
cd myreponame
git clone https://github.com/<your-username>/ca-knowledgebase.github.io
```

Then build the Jupyter Book (if you make multiple builds, it is recommended to clean up before each new build):

```
jupyter-book clean ca-knowledgebase.github.io/
jupyter-book build ca-knowledgebase.github.io/
```

You can inspect the created book by opening the local HTML files in `ca-knowledgebase.github.io/_build`. Once you're happy with them, push the new source files to the online repository:

```
cd ca-knowledgebase.github.io
git add ./*
git commit -m "add your message here"
git push
```

Now create a pull request from your repo to the main repo.

Any time an update is pushed to the main branch of the master repo, GitHub Actions will automatically update the `gh-pages` branch and publish the build files to [knowledgebase.acoustics.ac.uk](https://knowledgebase.acoustics.ac.uk/intro.html) as detailed in the [JupyterBook documentation](https://jupyterbook.org/publish/gh-pages.html#automatically-host-your-book-with-github-actions).

