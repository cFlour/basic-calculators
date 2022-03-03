#find the curved surface area of a cylinder
import math
r=float(input("Length of the radius? "))
h=float(input("Height of the cylinder?"))
pi=math.pi
CSA=round(2*pi*r*h,2)
BSA=round(2*pi*r*r,2)
TSA=CSA+LSA
print("CSA of the cylinder is",CSA)
print("BSA of the cylinder is",BSA)
print("TSA of the cylinder is",TSA)
print("BSA=Bottom Surface Area")
