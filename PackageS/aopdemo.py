
import sys
from aopmenu import aopmenu
from aopoperations import *

while(True):
    aopmenu()
    ch = int(input("Enter Your Choice : "))
    if(ch==1):
        addop()
    elif(ch==2):
        subop()
    elif(ch==3):
        mulop()
    elif(ch==4):
        divop()
    elif(ch==5):
        mod_divop()
    elif(ch==6):
        expop()
    elif(ch==7):
        print("Thanks for the AOP Call!")
        sys.exit()
else:
    print("Your Selection Operation is incorrect")


print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Division")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")