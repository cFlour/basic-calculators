#printing progressions
P=int(input("AP or GP? Press 1 for AP and 2 for GP."))
if P==1:
    print("For an Arithmetic Progression:a,a+d,a+2d,...")
    a=float(input("a="))
    d=float(input("d="))
    n=int(input("Number of terms="))
    print("The first",n,"terms of the AP are:")
    #taking m as the variable of a+d*m
    m=0
    while m<n:
        AP=a+(d*m)
        print(AP)
        m=m+1
if P==2:
    print("For a geometric progression: a,ar,ar^2,...")
    a=float(input("a="))
    r=float(input("r="))
    n=int(input("Number of terms="))
    #taking x as the variable of a*(r^x)
    x=0
    while x<n:
        GP=a*(r**x)
        print(GP)
        x=x+1
