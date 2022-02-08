#compound interest
P=float(input("Principal Amount? "))
N=float(input("Number of years? "))
R=float(input("Rate of interest? "))
CI=P*((1+(R/100))**N)-P
print("Compound interest=",CI)
