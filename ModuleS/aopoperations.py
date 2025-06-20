def readvalue(op):
    a=float(input("Enter First Value for {} :".format(op)))
    b=float(input("Enter First Value for {} :".format(op)))
    return a,b

def addop():
    a,b=readvalue("Addition")
    print("Sum {},{} = {}".format(a,b,a+b))

def subop():
    a,b=readvalue("Substraction")
    print("Sum {},{} = {}".format(a,b,a-b))

def mulop():
    a,b=readvalue("Multiplication")
    print("Sum {},{} = {}".format(a,b,a*b))

def divop():
    a,b=readvalue("Division")
    print("Sum {},{} = {}".format(a,b,a/b))

def mod_divop():
    a,b=readvalue("Modulo Division")
    print("Sum {},{} = {}".format(a,b,a%b))

def expop():
    a,b=readvalue("Exponentiation")
    print("Sum {},{} = {}".format(a,b,a**b))