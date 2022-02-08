#find the curved surface area of a cylinder
r=float(input("Length of the radius? "))
h=float(input("Height of the cylinder?"))
pi=22/7
CSA=2*pi*r*h
LSA=pi*r*r*2
TSA=CSA+LSA
print("CSA of the cylinder is",CSA)
print("LSA of the cylinder is",LSA)
print("TSA of the cylinder is",TSA)
