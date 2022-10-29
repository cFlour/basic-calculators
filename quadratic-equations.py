#finding quadratic roots ( human answers)
print("For a quadratic equation ax^2+bx+c=0:")
import math
c=float(input("c="))
b=float(input("b="))
a=float(input("a="))
D2=b**2-4*a*c
if D2>=0:
   D=math.sqrt(D2)
   if D%1==0:
      alpha=((0-b)+D)/(2*a)
      beta=((0-b)-D)/(2*a)
      print("The two roots are:",alpha,beta) 
   else:
      rootX=(-b)/(2*a)
      W=D2/(4*a*a)
      print("The two roots are:",rootX,"+- rt",W,sep="")
else:
   D=0-(math.sqrt(D2))
   B=(0-b)/(2*a)
   if D%1==0:
      d=D/(2*a)
      print("The two roots are:",B,"+-",d,"i",sep="")
   else:
      W=D2/(4*a*a)
      print("The two roots are:",B,"+- rt",W,"i",sep="")
