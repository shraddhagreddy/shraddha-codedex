# Write code below 💖
  
print("==================")
print("Area Calculator 📐")
print("==================")


print("choose one shape for the options")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape=int(input("which shape:"))

if(shape==1):
  base=int(input("Base:"))
  height=int(input("Height:"))
  area=(height*base)/2
  print(f'The area is {area}')
elif(shape==2):
  length=int(input("Length:"))
  width=int(input("Width:"))
  area=length*width
  print(f'The area is {area}')
elif(shape==3):
  side=int(input("Side:"))
  area=side**2
  print(f'The area is {area}')
elif(shape==4):
  radius=int(input("radius:"))
  area=3.14*(radius**2)
  print(f'The area is {area}')
else:
  print("error")