#input
import math
r=float(input("Radius length? "))
l=float(input("Slant height length? "))
pi=math.pi
#calculation
CSA=round(pi*r*l,2)
LSA=round(pi*r*r,2)
TSA=CSA+LSA
print("CSA=",CSA,",","LSA=",LSA,",","TSA=",TSA,".",sep="")
