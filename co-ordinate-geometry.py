#Calculates things using Distance formula and section formula of co-ordinate geometry.
print("Distance formula or section formula? Enter 0 for distance formula and 1 for section formula.")
dissec=int(input(""))
A=list(map(int,input("\nEnter co-ordinates of A: ").strip().split(",")))[:2]
def rationalroot(n):
    if n%1==0:
        print(n)
    else:
        print("√",(n**2),sep="")
if dissec==0:
    B=list(map(int,input("\nEnter co-ordinates of B: ").strip().split(",")))[:2]
    x2x1=(A[0]-B[0])**2
    y2y1=(A[1]-B[1])**2
    distance=(x2x1+y2y1)**(1/2)
    print("The distance AB is:")
    rationalroot(distance)
elif dissec==1:
    def section(a1,a2,b1,b2):
        num=(a1*b2)+(a2*b1)
        den=b1+b2
        return (num/den)
    print("Is the value of B known? Y/N")
    bknown=input("")
    if bknown=="Y" or bknown=="y":
        B=list(map(int,input("\nEnter co-ordinates of B: ").strip().split(",")))[:2]
        print("Let the point P divide the line segment AB. Enter the ratio in which P divides AB.")
        m1=int(input("m1="))
        m2=int(input("m2="))
        x=section(A[0],B[0],m1,m2)
        y=section(A[1],B[1],m1,m2)
        print("The co-ordinates of P are:\n")
        print("(",x,",",y,")",sep="")
    else:
        print("Enter the value of point P which divides AB in a certain ratio m1:m2.")
        P=list(map(int,input("\nEnter co-ordinates of P: ").strip().split(",")))[:2]
        m1=int(input("m1="))
        m2=int(input("m2="))
        x2=((P[0]*m1)+((P[0]-A[0])*m2))/m1
        y2=((P[1]*m1)+((P[1]-A[1])*m2))/m1
        print("The co-ordinates of B are:\n")
        print("(",x2,",",y2,")",sep="")
else:
    print("Try again.")
