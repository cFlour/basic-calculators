#fibonacci calculator
print("To find the n'th fibonacci number, please enter the value of n.")
n=int(input("n="))
#to simplify, we write (a=1+rt5)/2 and b= (1-rt5)/2
#rt5=root of 5
rt5=5**(1/2)
a=(1+rt5)/2
b=(1-rt5)/2
g=((a**n)-(b**n))/rt5
f=round(g,0)
print("The nth fibonacci number for n=",n," is ",f,end=".",sep="")
