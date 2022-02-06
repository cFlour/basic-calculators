#this is a basic addition, multiplication, subtraction, division, exponents, percentage and root calculator.
a=input("First number? ")
o=input("Operation? ")
b=input("Second number? ")
if o=="+":
  print(float(a)+float(b))
if o=="-":
  print(float(a)-float(b))
if o=="*":
  print(float(a)*float(b))
if o=="/":
  print(float(a)/float(b))
if o=="^":
  print(float(a)/float(b))
if o=="%":
	print(float(a)*100/float(b),"%",sep="")
if o=="√":
	print(float(a)**(1/float(b)))
