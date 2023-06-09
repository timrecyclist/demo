# demo

This repo is for demonstration purposes on how to create a package in Python.    
The video associated with it can be found in the Engineering folder on the Drive under the title "Merge Script Primer - making libraries in Python"   


NOTE: If you have python 3 is usually run by adding a 3 to the end of python
binaries. So you can use python3 python_file.py to run. Same for pip. Use pip3
install pandas for example to use python 3 stuff. Alternatively, you can alias
your .bashrc to automatically add the 3. Add this to .bashrc in your home
directory:   

`alias python=python3`    
`alias pip=pip3`   

Everything below says pip but really uses pip3.   


## Helpful links

Virtual Environments      
[Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)    
[Virtual Environments with pyenv](https://realpython.com/intro-to-pyenv/)    
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
    
Setuptools      
[Setuptools Quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)    

### TL;DR setuptools    

`pip install --upgrade setuptools`    

`pip install --upgrade build`

Create a pyproject.toml with the following    
>[build-system]     
>requires = ["setuptools"]   
>build-backend = "setuptools.build_meta"   
>
>[project]   
>name = "name-of-package"   
>version = "0.0.1"   
>dependencies = [   
>    "pandas",   
>    "requests"   
>]    


Follow the directory structure listed in Setuptools Quickstart or in this demo.   


You can then use    
`pip install --editable .`    
to create the package in development mode to avoid having to push and pip install again after making changes.    
When done, push to the repo and anyone can pip install from the repo.    



## Step by step    
Create your virtual environment. Using pyenv this looks like    
`pyenv virtualenv <name of virtual environment>`    

    
Activate it    
`pyenv activate <name of virtual environment>`

Upgrade pip, setuptools, and build    
`pip install --upgrade pip`    
`pip install --upgrade setuptools`    
`pip install --upgrade build`    
    
Make your module and save it in the directory structure of this repo (just the src and test directories).     
Then create your pyproject.toml file.      
    
Then make a requirements.txt via:    
`pip freeze > requirements.txt`    

    
    
Once that's done:    
`pip install --editable .`    
    
This will allow you to install your current directory as a package so that you can continue to work on it locally.   
Make changes, test, etc.   
For more on testing see: https://docs.python.org/3/library/unittest.html#test-cases    
Can also check out pytest: https://docs.pytest.org/en/7.3.x/   

   
   


    
When you are all finished push your changes to the repo. Anyone who would like to use your library can
then pip install it from a private repo they have access to via    
`pip install "git+https://<path to repo>"`    
or    
`pip install "git+ssh://<path to repo, but replace any : with />"`    


Don't forget to use [semantic versioning](https://semver.org/) to be able to mark different versions.   
    
     
### Potential Next Steps    
This is all unknown to me, but it's the general direction I'd head in from here.   
Goal - it would be great to automate testing for pull requests. I think these resources might help us do that:      
[Adding Shields to the repo for Testing/Code Coverage](https://shields.io/category/license)    
[Jenkins](https://www.jenkins.io/)    
[Travis CI](https://www.travis-ci.com/)       
   
Is this relevant to us? Don't know. We're not really building applications, but I think this can ensure our code runs the same on all machines.
[Docker](https://www.docker.com/)


