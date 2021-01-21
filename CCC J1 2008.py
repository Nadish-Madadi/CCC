weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = (weight/(height*height))

if bmi > 25:
  print("Overweight")
elif bmi >= 18.5 and bmi <= 25:
  print("Normal Weight")
elif bmi < 18.5:
  print("Underweight")
