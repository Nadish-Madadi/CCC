S = int(input("Small treats: "))
M = int(input("Medium treats: "))
L = int(input("Large treats: "))

happy_formula = ((1*S)+(2*M)+(3*L))

if happy_formula >= 10:
  print("happy")
elif happy_formula < 10:
  print("sad")
