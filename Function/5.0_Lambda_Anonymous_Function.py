# Anonymous Function are used for "performing instant operation".
# Instant Operation are nothing but used at a point of time and no longer needed.
# Anonymous function contains single executable statement but not multiple executable statement
# Anonymous function automatically returns the value (no need to use return statement)
# To define Anonymous function, we use a keyword called lambda and hence Anonymous function are called Lambda Function.
#Syntax
varname= lambda param-list: expression/statement


#prg 1

addop  = lambda x1,x2: x1+x2
x= addop(122,221)
print("After Add operation: {}".format(x))

#Prg 2

big = lambda a,b: a if a>b else b

x1= int(input("Enter First Number :"))
x2= int(input("Enter Second Number :"))
if(x1==x2):
    print("{} ,{} are equal".format(x1,x2))
else:
    y= big(x1,x2)
    print("Bigger Value is : {} ".format(y))