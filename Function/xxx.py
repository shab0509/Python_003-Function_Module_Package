#4. Variable Length Parameters or Arguments





def findsum(name, *n, crs="PYTHON"):
    print("-----------------------")
    print("Person Name : {} and course: {} ".format(name,crs))
    print("-----------------------")

    s=0
    for v in n:
        print("\t{}".format(v))
        s=s+v
    else:
        print("-----------------------")
        print("\tSum ={} ".format(s))
        print("\tAvg ={} ".format(s/len(n)))
        print("-----------------------")
findsum("Shabi",10 )
findsum("Shabi",10,20)
findsum("Shabi",10,20,30)
findsum("Shabi",10,20,30,-10,12.4,crs="Java")



