# The knowledgebase Docker image
The knowledgebase Docker image is a Docker image that includes all the software used in the knowledgebase's tutorials and runs a Jupyter lab.
You can run this Docker image by running:

```bash
docker pull caknowledgebase/caknowledgebase:main
docker run -ti -p 8888:8888 caknowledgebase/caknowledgebase:main
```

You will then be shown a link to follow to open the Jupyter lab.

## The structure of the Dockerfile
The Dockerfile can be found in the [docker folder](https://github.com/ukan-computational-acoustics/ca-knowledgebase/tree/main/docker).
(This should not be confused with the much smaller Dockerfile in the root folder of this repo. This smaller Dockfile only exists to make the Binder
links on the knowledgebase website work.)

The Dockerfile includes commands to install various pieces of software that are used in the knowledgebase's tutorials. A large number of version variables
are set at the top of the file. These can be updated when new versions of software are released to update the Dockerfile without having to make large changes.

### Adding your library to the Dockerfile
The easiest way to add your library to the Dockerfile is to first make the library installable with pip (or another package manager). It
can then be added to the Dockerfile by adding the line
```
RUN pip3 install *YOUR_LIBRARY*
```

If your library is not installable with a package manager, you may need to add more to the Dockerfile. For example, Gmsh is installed using the following lines:
```
RUN git clone -b gmsh_${GMSH_VERSION} --single-branch --depth 1 https://gitlab.onelab.info/gmsh/gmsh.git && \
    cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DENABLE_BUILD_DYNAMIC=1  -DENABLE_OPENMP=1 -B build-dir -S gmsh && \
    cmake --build build-dir && \
    cmake --install build-dir && \
    rm -rf /tmp/*
```
The `\` characters at the end of the first four lines allow the run command to continue past linebreaks. After installing the library, all the files in
the `tmp` directory are deleted: this helps minimise the size of the Docker image by removing unnecessary source files.

If you want to experiment with your library in the knowledgebase before adding it to the Dockerfile, you can add a command something like
this to the first cell of your Jupyter notebook:
```
pip3 install *YOUR_LIBRARY*
```

## Rebuilding the Docker image
When the Dockerfile is changed in a pull request or on the main branch, GitHub will automatically rebuild the Docker image. This takes a long time
(around 1-2 hours) so it will take a while for and changes that involve a change to the Docker file to appear online.

## Getting help
The Docker image and the GitHub actions surrounding it were set up by [Matthew Scroggs](community/bios.html#matthew-scroggs) and
[Jørgen S. Dokken](../community/bios#jorgen-s-dokken). If you encounter any problems with the Docker set up, please
[open an issue on GitHub](https://github.com/ukan-computational-acoustics/ca-knowledgebase/issues/new) and tag Matthew and/or Jørgen.
