def table():
    n = int(input("Enter any number : "))
    if (n<=0):
        print("{} i invalid input".format(n))
    else:
        print("_"*50)
        print("Mul Table for : {} ".format(n))
        print("_"*50)

        for i in range(1,11):
            print("\t {} X {} = {}".format(n,i,n*i))
        else:
            print("_" * 50)