x = int(input("Enter a x coordinate: "))
y = int(input("Enter a y coordinate: "))

#quad 1
if x >= 1 and x <= 1000 and y >= 1 and y <= 1000:
  print("1")
#quad 2
elif x <= -1 and x >= -1000 and y >= 1 and y <= 1000:
  print("2")
#quad 3
elif x <= -1 and x >= -1000 and y <= -1 and y >= -1000:
  print("3")
#quad 4
elif x >= 1 and x <= 1000 and y <= -1 and y >= -1000:
  print("4")
else:
  print("Please enter valid coordinates and ones that do not equal zero.")
  
