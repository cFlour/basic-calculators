#solving linear and quadraticequations
print("Which type of equation is it?")
print("Type 1 if it is a linear. Type 2 if it is quadratic.")
type=int(input())
if type==1:
    print("Let the equation be ay+b=c, where y is the variable. Enter the values:")
    a1=float(input("a="))
    b1=float(input("b="))
    c1=float(input("c="))
    y1=(c1-b1)/a1
    print("The value of the variable y is",y1)
if type==2:
    print("Let the equation be of ax^2+bx+c=0. Enter the values:")
    a2=float(input("a="))
    b2=float(input("b="))
    c2=float(input("c="))
    d2=(b2*b2)-4*a2*c2
    if d2<0:
        print("There are no real roots for x.")
        e2=0-d2
        A=(0-b2+(e2**(1/2)))
        B=(0-b2-(e2**(1/2)))
        print("The imaginary roots for x are ",A,"i and ",B,"i",sep="")
    else:
        A=(0-b2+(d2**(1/2)))
        B=(0-b2-(d2**(1/2)))
        print("The values of x are",A,"and",B)
