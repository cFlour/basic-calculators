#inputs
import math
r=float(input("Length of the radius? "))
pi=math.pi
#surface area
SA=round(4*pi*r*r,2)
#volume
v=round((4/3)*pi*r*r*r,2)
#output
print("Surface area is",SA)
print("Volume is",v)
