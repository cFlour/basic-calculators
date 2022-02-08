#to find the unknowwn value from the r, h & l values of a cone
print("Which two of r,h,l are given? r is the radius, l is the slant height and h is the height. ")
x=input("Please don't use any spaces while specifying, just seperate by commas. Also while specifying, put r first, h next and l at last. ")
if x=="r,l":
  r=float(input("Value of r? "))
  l=float(input("Value of l? "))
  h=(l**2-r**2)**(1/2)
  print(h)
if x=="r,h":
  r=float(input("Value of r? "))
  h=float(input("Value of h? "))
  l=(r**2+h**2)**(1/2)
  print (l)
if x=="h,l":
  h=float(input("Value of h? "))
  l=float(input("Value of l? "))
  r=(l**2-h**2)**(1/2)
  print(r)
