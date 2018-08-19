from numpy.distutils.core import setup, Extension


# Compile the fortran SCHA modules
SCHAModules = Extension(name = "SCHAModules", 
                        sources = ["SCHAModules/module_stochastic.f90",
                                   "SCHAModules/module_new_thermodynamic.f90",
                                   "SCHAModules/module_anharmonic.f90"],
                        libraries = ["lapack", "blas"],
                        extra_f90_compile_args = ["-cpp"])


# Prepare the compilation of the Python Conde
setup( name = "python-sscha",
       version = "0.1",
       description = "Python implementation of the sscha code",
       author = "Lorenzo Monacelli",
       url = "https://github.com/mesonepigreco/python-sscha",
       packages = ["sscha"],
       package_dir = {"sscha": "Modules"},
       install_requires = ["numpy", "ase", "scipy", "cellconstructor", "lapack", "blas"],
       ext_modules = [SCHAModules],
       license = "GPLv3"
       )

def readme():
    with open("README.md") as f:
        return f.read()