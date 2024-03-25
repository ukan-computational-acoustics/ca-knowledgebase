# Dockerfile describing development builds of FEniCSx
#
# Authors:
# Jack S. Hale <jack.hale@uni.lu>
# Lizao Li <lzlarryli@gmail.com>
# Garth N. Wells <gnw20@cam.ac.uk>
# Jan Blechta <blechta@karlin.mff.cuni.cz>
# Jørgen S. Dokken <dokken92@gmail.com>

ARG ADIOS2_VERSION=2.8.1
ARG GMSH_VERSION=4_10_1
ARG HDF5_SERIES=1.12
ARG HDF5_PATCH=2
ARG KAHIP_VERSION=3.14
ARG NUMPY_VERSION=1.22.4
ARG PETSC_VERSION=3.17.2
ARG SLEPC_VERSION=3.17.1
ARG XTL_VERSION=0.7.4
ARG MPICH_VERSION=4.0.2
ARG OPENMPI_SERIES=4.1
ARG OPENMPI_PATCH=4
ARG DOLFINX_VERSION=v0.7.3
ARG FFCX_VERSION=v0.7.0
ARG BASIX_VERSION=v0.7.0
ARG UFL_VERSION=2023.2.0
ARG NANOBIND_VERSION=1.9.2
ARG PYTHON_VERSION=3.10

########################################

FROM ubuntu:22.04 as ca-knowledgebase
LABEL maintainer=""
LABEL description="Environment with all dependencies for the CA knowledgebase"

ARG GMSH_VERSION
ARG HDF5_SERIES
ARG HDF5_PATCH
ARG PETSC_VERSION
ARG SLEPC_VERSION
ARG ADIOS2_VERSION
ARG KAHIP_VERSION
ARG NUMPY_VERSION
ARG XTL_VERSION
ARG MPICH_VERSION
ARG OPENMPI_SERIES
ARG OPENMPI_PATCH
ARG DOLFINX_VERSION
ARG FFCX_VERSION
ARG BASIX_VERSION
ARG UFL_VERSION
ARG NANOBIND_VERSION

# Compiler optimisation flags for SLEPc and PETSc, all languages.
ARG PETSC_SLEPC_OPTFLAGS="-O2"
# PETSc and SLEPc number of make processes (--with-make-np)
ARG PETSC_SLEPC_MAKE_NP=2
# Turn on PETSc and SLEPc debugging. "yes" or "no".
ARG PETSC_SLEPC_DEBUGGING="no"

# MPI variant. "mpich"
ARG MPI="mpich"
ARG MPICH_CONFIGURE_OPTIONS="FCFLAGS=-fallow-argument-mismatch FFLAGS=-fallow-argument-mismatch --with-device=ch4:ofi"  # See https://github.com/pmodels/mpich/issues/5811

# Number of build threads to use with make
ARG BUILD_NP=2

WORKDIR /tmp

# Environment variables
ENV OPENBLAS_NUM_THREADS=1 \
    OPENBLAS_VERBOSE=0

# Install dependencies available via apt-get.
# - First set of packages are required to build and run FEniCS.
# - Second set of packages are recommended and/or required to build
#   documentation or tests.
# - Third set of packages are optional, but required to run gmsh
#   pre-built binaries.
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -qq update && \
    apt-get -yq --with-new-pkgs -o Dpkg::Options::="--force-confold" upgrade && \
    apt-get -y install \
    clang \
    cmake \
    g++ \
    gfortran \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-timer-dev \
    liblapack-dev \
    libopenblas-dev \
    libpugixml-dev \
    ninja-build \
    pkg-config \
    python3-dev \
    python3-pip \
    python3-setuptools && \
    #
    apt-get -y install \
    catch2 \
    clang-format \
    doxygen \
    git \
    graphviz \
    libeigen3-dev \
    valgrind \
    wget && \
    #
    apt-get -y install \
    libglu1 \
    libxcursor-dev \
    libxft2 \
    libxinerama1 \
    libfltk1.3-dev \
    libfreetype6-dev  \
    libgl1-mesa-dev \
    libocct-foundation-dev \
    libocct-data-exchange-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install MPI
RUN wget http://www.mpich.org/static/downloads/${MPICH_VERSION}/mpich-${MPICH_VERSION}.tar.gz && \
    tar xfz mpich-${MPICH_VERSION}.tar.gz  && \
    cd mpich-${MPICH_VERSION}  && \
    ./configure ${MPICH_CONFIGURE_OPTIONS} && \
    make -j${BUILD_NP} install; \
    ldconfig && \
    rm -rf /tmp/*

# Install Python packages (via pip)
# Install numpy via pip. Exclude binaries to avoid conflicts with libblas
# - First set of packages are required to build and run DOLFINx Python.
# - Second set of packages are recommended and/or required to build
#   documentation or run tests.
RUN pip3 install --no-binary="numpy" --no-cache-dir cffi mpi4py numba numpy==${NUMPY_VERSION} scipy && \
    pip3 install --no-cache-dir cppimport flake8 isort jupytext matplotlib mypy myst-parser nanobind==${NANOBIND_VERSION} pytest pytest-xdist sphinx sphinx_rtd_theme

# Install KaHIP
RUN wget -nc --quiet https://github.com/kahip/kahip/archive/v${KAHIP_VERSION}.tar.gz && \
    tar -xf v${KAHIP_VERSION}.tar.gz && \
    cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DNONATIVEOPTIMIZATIONS=on -B build-dir -S KaHIP-${KAHIP_VERSION} && \
    cmake --build build-dir && \
    cmake --install build-dir && \
    rm -rf /tmp/*

# Install HDF5
RUN wget -nc --quiet https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-${HDF5_SERIES}/hdf5-${HDF5_SERIES}.${HDF5_PATCH}/src/hdf5-${HDF5_SERIES}.${HDF5_PATCH}.tar.gz && \
    tar xfz hdf5-${HDF5_SERIES}.${HDF5_PATCH}.tar.gz && \
    cd hdf5-${HDF5_SERIES}.${HDF5_PATCH} && \
    ./configure --prefix=/usr/local --enable-parallel --enable-shared --enable-static=no && \
    make -j${BUILD_NP} install && \
    rm -rf /tmp/*


# Install ADIOS2
RUN wget -nc --quiet https://github.com/ornladios/ADIOS2/archive/v${ADIOS2_VERSION}.tar.gz -O adios2-v${ADIOS2_VERSION}.tar.gz && \
    mkdir -p adios2-v${ADIOS2_VERSION} && \
    tar -xf adios2-v${ADIOS2_VERSION}.tar.gz -C adios2-v${ADIOS2_VERSION} --strip-components 1 && \
    cmake -G Ninja -DADIOS2_USE_HDF5=on -DADIOS2_USE_Fortran=off -DBUILD_TESTING=off -DADIOS2_BUILD_EXAMPLES=off -DADIOS2_USE_ZeroMQ=off -B build-dir -S ./adios2-v${ADIOS2_VERSION} && \
    cmake --build build-dir && \
    cmake --install build-dir && \
    rm -rf /tmp/*

# Install GMSH
RUN git clone -b gmsh_${GMSH_VERSION} --single-branch --depth 1 https://gitlab.onelab.info/gmsh/gmsh.git && \
    cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DENABLE_BUILD_DYNAMIC=1  -DENABLE_OPENMP=1 -B build-dir -S gmsh && \
    cmake --build build-dir && \
    cmake --install build-dir && \
    rm -rf /tmp/*

ENV PYTHONPATH=/usr/local/lib:$PYTHONPATH

# Install PETSc and petsc4py with complex types
ENV PETSC_DIR=/usr/local/petsc SLEPC_DIR=/usr/local/slepc
RUN apt-get -qq update && \
    apt-get -y install bison flex && \
    wget -nc --quiet http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-lite-${PETSC_VERSION}.tar.gz -O petsc-${PETSC_VERSION}.tar.gz && \
    mkdir -p ${PETSC_DIR} && tar -xf petsc-${PETSC_VERSION}.tar.gz -C ${PETSC_DIR} --strip-components 1 && \
    cd ${PETSC_DIR} && \
    # Complex, 32-bit int
    python3 ./configure \
    PETSC_ARCH=linux-gnu-complex-32 \
    --COPTFLAGS="${PETSC_SLEPC_OPTFLAGS}" \
    --CXXOPTFLAGS="${PETSC_SLEPC_OPTFLAGS}" \
    --FOPTFLAGS="${PETSC_SLEPC_OPTFLAGS}" \
    --with-make-np=${PETSC_SLEPC_MAKE_NP} \
    --with-64-bit-indices=no \
    --with-debugging=${PETSC_SLEPC_DEBUGGING} \
    --with-fortran-bindings=no \
    --with-shared-libraries \
    --download-hypre \
    --download-metis \
    --download-mumps \
    --download-ptscotch \
    --download-scalapack \
    --download-suitesparse \
    --download-superlu \
    --download-superlu_dist \
    --with-scalar-type=complex && \
    make PETSC_DIR=/usr/local/petsc PETSC_ARCH=linux-gnu-complex-32 ${MAKEFLAGS} all && \
    # Install petsc4py
    cd src/binding/petsc4py && \
    PETSC_ARCH=linux-gnu-complex-32 pip3 install --no-cache-dir . && \
    # Cleanup
    apt-get -y purge bison flex && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf \
    ${PETSC_DIR}/**/tests/ \
    ${PETSC_DIR}/**/obj/ \
    ${PETSC_DIR}/**/externalpackages/  \
    ${PETSC_DIR}/CTAGS \
    ${PETSC_DIR}/RDict.log \
    ${PETSC_DIR}/TAGS \
    ${PETSC_DIR}/docs/ \
    ${PETSC_DIR}/share/ \
    ${PETSC_DIR}/src/ \
    ${PETSC_DIR}/systems/ \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install SLEPc
RUN wget -nc --quiet https://gitlab.com/slepc/slepc/-/archive/v${SLEPC_VERSION}/slepc-v${SLEPC_VERSION}.tar.gz && \
    mkdir -p ${SLEPC_DIR} && tar -xf slepc-v${SLEPC_VERSION}.tar.gz -C ${SLEPC_DIR} --strip-components 1 && \
    cd ${SLEPC_DIR} && \
    export PETSC_ARCH=linux-gnu-complex-32 && \
    python3 ./configure && \
    make && \
    # Install slepc4py
    cd src/binding/slepc4py && \
    PETSC_ARCH=linux-gnu-complex-32 pip3 install --no-cache-dir . && \
    rm -rf ${SLEPC_DIR}/CTAGS ${SLEPC_DIR}/TAGS ${SLEPC_DIR}/docs ${SLEPC_DIR}/src/ ${SLEPC_DIR}/**/obj/ ${SLEPC_DIR}/**/test/ && \
    rm -rf /tmp/*

# CMake build type for DOLFINx C++ build. See CMake documentation.
ARG DOLFINX_CMAKE_BUILD_TYPE="RelWithDebInfo"
# Extra CMake C++ compiler flags for DOLFINx C++ build.
ARG DOLFINX_CMAKE_CXX_FLAGS

# Install the components of FEniCSx
RUN git clone -b ${UFL_VERSION} --single-branch --depth 1 https://github.com/fenics/ufl.git && \
    git clone -b ${BASIX_VERSION} --single-branch --depth 1 https://github.com/fenics/basix.git && \
    git clone -b ${FFCX_VERSION} --single-branch --depth 1 https://github.com/fenics/ffcx.git && \
    cd basix && cmake -G Ninja -DCMAKE_BUILD_TYPE=${DOLFINX_CMAKE_BUILD_TYPE} -DCMAKE_CXX_FLAGS=${DOLFINX_CMAKE_CXX_FLAGS} -B build-dir -S ./cpp && \
    cmake --build build-dir && \
    cmake --install build-dir && \
    python3 -m pip install ./python && \
    cd ../ufl && pip3 install --no-cache-dir . && \
    cd ../ffcx && pip3 install --no-cache-dir . && \
    cd ../ && pip3 install --no-cache-dir ipython

RUN git clone -b ${DOLFINX_VERSION} --single-branch --depth 1 https://github.com/fenics/dolfinx.git && \
    cd dolfinx && \
    mkdir -p build-complex && \
    cd build-complex && \
    PETSC_ARCH=linux-gnu-complex-32 cmake -G Ninja -DCMAKE_INSTALL_PREFIX=/usr/local/dolfinx-complex -DCMAKE_BUILD_TYPE=${DOLFINX_CMAKE_BUILD_TYPE} -DCMAKE_CXX_FLAGS=${DOLFIN_CMAKE_CXX_FLAGS} ../cpp && \
    ninja install && \
    . /usr/local/dolfinx-complex/lib/dolfinx/dolfinx.conf && \
    cd ../python && \
    CXXFLAGS=${DOLFINX_CMAKE_CXX_FLAGS} PETSC_ARCH=linux-gnu-complex-32 pip3 install -v --target /usr/local/dolfinx-complex/lib/python${PYTHON_VERSION}/dist-packages --no-dependencies --no-cache-dir .


ENV PKG_CONFIG_PATH=/usr/local/dolfinx-complex/lib/pkgconfig:$PKG_CONFIG_PATH \
    PETSC_ARCH=linux-gnu-complex-32 \
    PYTHONPATH=/usr/local/dolfinx-complex/lib/python${PYTHON_VERSION}/dist-packages:$PYTHONPATH \
    LD_LIBRARY_PATH=/usr/local/dolfinx-complex/lib:$LD_LIBRARY_PATH

########################################

# Install jupyter
RUN pip3 install --upgrade --no-cache-dir jupyter jupyterlab jupytext jupyter-book

# pyvista dependencies from apt
RUN apt-get -qq update && \
    apt-get -y install libgl1-mesa-dev xvfb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# pyvista dependencies from pip. Only compatible with x86-64 (amd64).
# matplotlib improves plotting quality with better color maps and properly rendering colorbars.
# ipygany and pythreejs makes plotting in notebooks interactive
RUN dpkgArch="$(dpkg --print-architecture)"; \
    case "$dpkgArch" in amd64) \
    # pip3 install --no-cache-dir pyvista==${PYVISTA_VERSION} ;; \
    pip3 install --find-links https://wheels.pyvista.org/ pyvista ;; \
    esac; \
    pip3 install --no-cache-dir matplotlib ipygany pythreejs

RUN jupyter nbextension enable --py --sys-prefix ipygany

WORKDIR /root

EXPOSE 8888/tcp
ENV SHELL /bin/bash
ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]
