# Building this site

This site runs using [Jupyter Books](https://jupyterbook.org/intro.html). If you have not used Jupyter Books before, please complete their
[tutorial on creating your first book](https://jupyterbook.org/start/your-first-book.html) before contributing. Note that Windows users will need to use Python 3.7.

First ensure you have Jupyter Books installed:

```bash
pip install -U jupyter-book
```

You can build the Jupyter Book by navigating to the root folder of the knowledgebase repo then running
(if you make multiple builds, it is recommended to clean up before each new build):

```bash
jupyter-book clean .
jupyter-book build .
```

You can inspect the created book by opening the local HTML files in `ca-knowledgebase/_build`.

## Building this side inside the Docker image

If you do not have all the software used in the knowledgebase installed locally, you can build the book inside the [knowledgebase Docker image](contribute-docker).
You can launch this docker image by running the following commands in the root directory of the repo:
```bash
docker pull caknowledgebase/caknowledgebase:main
docker run -ti -p 8888:8888 -v $(pwd):/mnt/knowledgebase caknowledgebase/caknowledgebase:main
```

You will then be given a link to follow to open the Jupyter lab that the image runs. Once you've opened the lab, click 'Terminal' (under 'Other') then run:
```bash
cd /mnt/knowledgebase
```

You can then build the Jupyter book by running the same Jupyter book commands as above.
