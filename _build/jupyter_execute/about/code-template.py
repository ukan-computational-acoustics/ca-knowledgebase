#!/usr/bin/env python
# coding: utf-8

# # Tutorial template
# 
# Here is some short text about what the tutorial will cover.
# 
# _Include this note block at the top of every code page:_
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
# _All tutorials should have a prerequisites section; just say "none" if none are required.
# If the prerequisites exist on the knowledgebase, please include links to them.
# If the prerequisites do not exisit on the knowledgebase, raise a GitHub Issue to ensure they get added (it's preferable that all prerequisites be available on the knowledgebase, but we will relax this requirement while the site is in alpha)._
# 
# None.
# 
# ## Introduction
# 
# _Explain the background and details of the tutorial here._
# 
# 
# ## Setup
# 
# _You can include anything here that has been explained in previous lessions, load data, libraries, etc. Each notebook file should run without additional dependencies, so use this section to ensure all necessary setup is complete._
# 

# In[1]:


import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import numpy as np


# _Note that we recommend all tutorials include visual and audio output wherever possible._
# 
# ## Basic example
# 
# _The aim with all our tutorials is to introduce a basic working example as early as possible, so that new users can see the value right away. You can then introduce more details as you go on. See the [FDTD tutorial](../fdtd/tutorial1) for an example._

# In[2]:


# Simple example code


# ## More details
# 
# _Once you have introduced the basic example, you can begin to build upon it howevery you like. Try not to make these sections too long._
# 
# Here's some more details and code relating to a specific aspect.
# 

# In[3]:


# And here is some more code


# ## Embedding code, images, math...
# 
# There's lots of information about how to embed code, images, etc. into Jupyter Notebooks in the [Jupyter Books documentation](https://jupyterbook.org/file-types/notebooks.html). MyST markdown is used in both the `.md` and `.ipynb` files throughout the Jupyter Book. For more information about MyST markdown, check out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html), or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# The most common things you might want to do are embed images, like so:
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# Or $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# using LaTeX formatting, like so...
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# ## Summary
# 
# _Please include a few summary bullets describing the main take-aways from the tutorial._
# 
# * Bullet 1
# * Bullet 2
# * Bullet 3
