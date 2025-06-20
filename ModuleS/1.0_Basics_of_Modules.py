# We know that functions concept meant for performing certain operation and provides code re-usability
# within the same program but not able to provide code-reusabitlity across the programs.
# To overcome this we use modules
# The purpose of modules concept is that to provide code reusability across the programs.


#def:
# A module is a collection of variables(Global Variables), Functions and Classes.
# In Python Programming we have two types of modules:
  1. Pre-Defined Modules : These Modules are already developed by Python Software Developers
                           and available in Python Software and whose role is to deal with
                           universal requirement. Ex: Built-ins, functools, calendar, math ,cmath

  2. Programmer-Defined Modules : These Modules are developed by Python Language Programmers and
                                  available in Python project and whose role is to deal with common requirement.
                                Ex: Banking, Mathformula


#Creating Programmer Defined Module
#Creating Programmer defined module is nothing but
  a> Define the variable with values(Global Variables)
  b> Defining the functions for performing common operations
    Save the above on some filename with an extension .py(FileName.py)
    Hence Filename.py compiled version(Filename.cpython-310.pyc) is treated as module name.
    Once the module is created , whose name is placed within a folder which is created automatically by python env.

# Approach For Re-using Modules

Two Approaches to re-use the modules, they are :
    1> By using import statement
    2> By using from ......import statement

1> By using import statement (Prg belongs to :icici.py,mathsinof.py,multable.py,s1.py,s2.py )

Here "import" is an keyword.
Import statement is used for importing or accessing the information about modules
(Variable ,Functions and Classes) of one program into another program.

syntax 1: import ModuleName
syntax 2: import Modulename as aliasname
syntax 3: import modulename1,modulename2, ...... modulenameN
syntax 4: import modulename1 as aliasname1,modulename2 as aliasname2,....modulenameN as aliasnameN
syntax 5: Syntax for accessing Variables, Function names and Class names
          ModuleName.VariableName
          ModuleName.FunctionName
          ModuleName.ClassName

2> By using from.......import statement (Prg belongs to : aopemnu.py,aopoperations.py,aopdemo.py)

Here 'from' and 'import' are the keywords
It is used for importing or accesing the information about modules(Variable,Functions and Classes) of one program into
another program and we can access the variables,function and classes directly without using module name.

Syntax 1: from ModuleName import VariableName,FunctionName,ClassName
Syntax 2: from ModuleName import VariableName as aliasname1,FunctionName as aliasname2, Classname as aliasname3
Synatx 3: from modulename import *      (But Not Recommended)

Note :
The Module concept provide the code reusability acrossthe programs, provided the program is available in th same folder,
But not provide code reusability across the folder/drive/env/networks/machine.

To get code reusability across the folder/drive/env/networks/machine, we must go for "PACKAGES"