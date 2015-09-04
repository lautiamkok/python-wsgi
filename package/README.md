# Python Package

The main difference between a module and a package is that a package is a collection of modules AND it has an __init__.py file.

**notes**

1. __init__.py is for packages. A package contains a collection of related modules. If you just have a single module you want to use, you don't need to use __init__.py; just put the single .py file somewhere on the system path and you can import it.

2. In Python versions prior to 3.3, all packages were required to have an __init__.py file. Python 3.3 removed this requirement.

## Ref:

    * http://www.blog.pythonlibrary.org/2012/07/08/python-201-creating-modules-and-packages/
    * http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html
