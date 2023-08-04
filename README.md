Introduction
============

What is TDSCHA?
---------------------

Time-Dependent Self-Consistent Harmonic Approximation (TDSCHA) is a python library to ...




What can I do with tdscha?
---------------------------


[...]


How to install
==============

The TDSCHA is part of the SSCHA packages: CellConstructor and python-sscha.
In this guide, we refer to the installation of tdscha.

Installation from pip
---------------------

As for the SSCHA code, also TDSCHA is distributed on PyPi

.. code-block:: console

   pip install tdscha

Alternatively, the code to compute Raman and IR spectrum can be downloaded from GitHub at
[https://github.com/SSCHAcode/tdscha]

To install the github code, that enables the MPI parallelization also without the JULIA speedup, you can use:

.. code-block:: console

    git clone https://github.com/SSCHAcode/tdscha.git
    cd tdscha
    MPICC=mpicc python setup.py install

where mpicc is a valid mpi c compiler (the specification of MPICC can be dropped, but parallelization will not be available aside for the julia mode discussed below).

JULIA speedup enhancement
^^^^^^^^^^^^^^^^^^^^^^^^^

The TDSCHA code exploits JULIA to speedup the calculation by a factor of 10x-15x
with the same number of processors.

To have it working, download and install julia from [https://julialang.org/downloads/].
Alternatively, to install julia on linux we can employ juliaup:

.. code-block:: console

    curl -fsSL https://install.julialang.org | sh

Hit enter when asked to install julia.

To use julia, either open a new terminal, or hit:

.. code-block:: console

    source ~/.bashrc


Then, open a terminal and type ``julia``. Inside the julia prompt, type ``]``
The prompt should change color and display the julia version ending with ``pkg>``

Install the required julia libraries

.. code-block:: console

    pkg> add SparseArrays, LinearAlgebra, InteractiveUtils, PyCall

This should install the required libraries.
press backspace to return to the standard julia prompt and exit with

.. code-block:: console

   julia> exit()

Then, install the python bindings for julia with

.. code-block:: console

   pip install julia

Now, you should be able to exploit the julia speedup in the TDSCHA calculations.
It is not required to install julia before TDSCHA, it can also be done in a later moment.


MPI Parallelization
^^^^^^^^^^^^^^^^^^^

MPI parallelization is not necessary, however
you may like to configure it in practical calculation to further speedup the code.
For production runs, it is suggested to combine the mpi parallelization with
the julia speedup.

The TDSCHA code exploits the mpi parallelization using mpi4py,
This assumes that you have a MPI C compiler installed.
This is done by installing the library ``openmpi-bin`` which we installed in the requirements.

You can now install mpi4py

.. code-block:: console

   pip install mpi4py


The parallelization is automatically enabled in the julia version and if mpi4py is available.
However, to run the parallel code without the julia speedup, you need to recompile the code
from the github repository as (not the version installed with pip)

.. code-block:: console

   MPICC=mpicc python setup.py install

e sure that at the end of the installation no error are displayed, and the write
PARALLEL ENVIRONMENT DECTECTED SUCCESFULLY is displayed.
Note that, if using the julia enhanced version, the last command is not required, and you can install only mpi4py.

Installation from source
------------------------

Once all the dependences of the codes are satisfied, you can unzip the source code downloaded from the website.
Then run, inside the directory that contains the setup.py script, the following command:

.. code-block:: console

   python setup.py install


As for the pip installation, you may append the --user option to install the package only for the user (without requiring administrator powers).


Install with Intel FORTRAN compiler
-----------------------------------

The setup.py script works automatically with the GNU FORTRAN compiler. However, due to some differences in linking lapack,
to use the intel compiler you need to edit a bit the setup.py script:

In this case, you need to delete the lapack linking from the
setup.py and include the -mkl as linker option.
Note that you must force to use the same liker compiler as the one used for the compilation.

Install with a specific compiler path
-------------------------------------

This can be achieved by specifying the environment variables on which setup.py relies:

1. CC (C compiler)
2. FC (Fortran compiler)
3. LDSHARED (linking)

If we want to use a custom compiler in /path/to/fcompiler we may run the setup as:

.. code-block:: console

   FC=/path/to/fcompiler LDSHARED=/path/to/fcompiler python setup.py install



A specific setup.py script is provided to install it easily in FOSS clusters.


Quick start
===========
