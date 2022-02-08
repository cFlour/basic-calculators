#simple interest
P=float(input("Principal Amount? "))
N=float(input("Number of years? "))
R=float(input("Rate of interest? "))
I=P*N*R/100
print("The simple interest on the amount of",P,"for",N,"years at",R,"percent interest is",I,"and the total amount is",P+I)
