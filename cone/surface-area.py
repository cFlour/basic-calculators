#input
r=float(input("Radius length? "))
l=float(input("Slant height length? "))
pi=22/7
#calculation
CSA=pi*r*l
LSA=pi*r*r
TSA=CSA+LSA
print("CSA=",CSA,",","LSA=",LSA,",","TSA=",TSA,".",sep="")
