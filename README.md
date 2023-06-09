# demo

This repo is for demonstration purposes on how to create a package in Python.
NOTE: If you have python 3 is usually run by adding a 3 to the end of python
binaries. So you can use python3 python_file.py to run. Same for pip. Use pip3
install pandas for example to use python 3 stuff. Alternatively, you can alias
your .bashrc to automatically add the 3. Add this to .bashrc in your home
directory:

`alias python=python3`
`alias pip=pip3`

Everything below says pip but really uses pip3.


Helpful links

Virtual Environments
[venv (default)](https://docs.python.org/3/library/venv.html)
[Pyenv (recommended)](https://realpython.com/intro-to-pyenv/)

Installing Library from GitHub
[mCoding](https://youtu.be/r-wwMk5faXo)

Unit Testing
[unittest (default)](https://docs.python.org/3/library/unittest.html#test-cases)
[pytest](https://docs.pytest.org/en/7.3.x/)

Type Checking (optional, but should probably do)
[Python Type Checking](https://realpython.com/python-type-checking/)
[MyPy](https://mypy.readthedocs.io/en/stable/)

[Setuptools Quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
TL;DR
`pip install --upgrade setuptools`
`pip install --upgrade build`

Create a pyproject.toml with the following
`
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "name-of-package"
version = "0.0.1"
dependencies = [
    "pandas",
    "requests"
]
`
Follow the directory structure listed in Setuptools Quickstart or in this demo

mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
|   # README.rst or README.md (a nice description of your package)
|   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
└── mypackage
    ├── __init__.py
    └── ... (other Python files)

Alternatively
mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
|   # README.rst or README.md (a nice description of your package)
|   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
└── src
|   | - mypackage
|       ├── __init__.py
|       └── ... (other Python files)
└── tests
    | - testing stuff

If using this setup, add the following to your pyproject.toml
`
[tool.setuptools.packages.find]
where = ["src"]
`


You can then use 
`pip install --editable .`
in development to avoid having to push and pip install again after making changes.


## Step by step
Create your virtual environment. Using pyenv this looks like
pyenv virtualenv <name of virtual environment>

Activate it
`pyenv activate <name of virtual environment>`

Upgrade pip, setuptools, and build
`pip install --upgrade pip`
`pip install --upgrade setuptools`
`pip install --upgrade build`

Make your module and save it in the directory structure above. Then create your
pyproject.toml file.

You can then continue to develop your package as you'd like. When finished,
make a requirements.txt via:
`pip freeze > requirements.txt`

Once that's done:
`pip install --editable .`


Then push your changes to the repo. Anyone who would like to use your library can
then pip install it from a private repo they have access to via

`pip install "git+https://<path to repo>"`
or
`pip install "git+ssh://<path to repo, but replace any : with />"`

Don't forget to use [semantic versioning](https://semver.org/)

