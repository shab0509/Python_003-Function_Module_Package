# Program One

a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

def sumop(a,b):
    c=a+b
    print(c)

sumop(a,b)

# Program Two

a= int(input("Enter First Number : "))
b= int(input("Enter Second Number : "))

def sumop(a,b):
    c=a+b
    print("_"*40)
    print("The sum of {} and {} is {}".format(a,b,c))
    print("_"*40)
    return(c)
print("_"*40)
x=sumop(a,b)

# Program Three

def sumop():
    x1 = float(input("Enter First Number: "))
    x2 = float(input("Enter Second Number: "))
    x3 = x1+x2
    print("The sum of {} and {} is {}".format(x1,x2,x3))
    return x1,x2,x3

n1,n2,result =sumop()




