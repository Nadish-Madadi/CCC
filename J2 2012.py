value_one = int(input("Enter the first depth reading: "))
value_two = int(input("Enter the second depth reading: "))
value_three = int(input("Enter the third depth reading: "))
value_four = int(input("Enter the fourth depth reading: "))


if value_one > 0 and value_two > 0 and value_three > 0 and value_four > 0:
    if value_one < value_two < value_three < value_four:
      print("Fish Rising")
    elif value_one > value_two > value_three > value_four:
      print("Fish Diving")
    elif value_one == value_two == value_three == value_four:
      print("Fish At Constant Depth")
    else:
      print("No Fish")
else:
  print("Please enter a positive values")
    
