# Functions

#The Purpose of functions is that "To Perform Certain Operations
# and provides code re-usability"

#Def of functions
# Sub-Program of main function
# A Part of the main program

#Types of functions
# Pre-defined / Built-In Function : which are already defined in the Python Software
# for ex : print(),id,type()

# Programmer / User Defined Functions : which are defined by the Python Programmer for
# performing certain operation and code reusabilility for ex : sumop(), divop

# Syntax for defining functions:

def functionname(list of formal Parameters):
                statement_1
                statement_2
                statement_3
                statement_4



#PARAMETERS

# parameter are always used in functions definition
# We have 2 types of parameters :
# Formal Parameters / Variables
# Actual Parameters / Variables

#Formal parameter are used in function heading and they are used
# for storing input values coming from function call

#Local Parameter used in the function body and they are used
# for storing temporary result.


#ARGUMENTS
#Argument are also variables/parameter used in function call.

def sumop(a,b):
    c=a+b
    print(a,b,c)
x=10
y=20
sumop(x,y) # x,y are called Actual Arguments.