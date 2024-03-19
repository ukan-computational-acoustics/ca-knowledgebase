# Editing in GitHub

This option is advisable if you only want to make changes to one or two files, and/or you are not comfortable using Git on your local machine.

1. Make a fork of the [knowledgebase repo](https://github.com/ukan-computational-acoustics/ca-knowledgebase). There is a button in the top-right corner that allows you to do this.
2. Navigate to the file you want to edit, or the folder to which you want to add  your own `.md` or `.ipynb` file.
3. If you have added a new file, you will need to add it to the `_toc.yml` file, to tell Jupyter where to put your file in the table of contents. [More information can be found here](https://jupyterbook.org/en/stable/structure/toc.html). If you do not do this, your file will be excluded from the build process.
4. Open a pull request from your branch to the main repository. You can do this by clicking the 'Contribute' button on the GitHub page for your branch.

5. We will then review your pull request. If we suggest changes, you can make these then push again to update the pull request. Once we're happy with your changes,
   we'll merge them and the knowledgebase website will update automatically.