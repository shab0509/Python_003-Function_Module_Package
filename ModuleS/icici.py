def simpleint():
    p = float(input("Enter Principal Amount : "))
    t = float(input("Enter Time : "))
    r = float(input("Enter Rate of Interest : "))

    si= (p*t*r)/100
    totamt = p + si
    print("_" * 40)
    print("Principal Amount : {}".format(p))
    print("Time : {}".format(t))
    print("Rate of Interest : {}".format(r))
    print("Simple Interest to pay : {}".format(si))
    print("Total Amount to pay : {} ".format(totamt))
    print("_"*40)