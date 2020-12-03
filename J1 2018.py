first_digit = int(input("First digit: "))
second_digit = int(input("Second digit: "))
third_digit = int(input("Third digit: "))
fourth_digit = int(input("Fourth digit: "))

if (first_digit == 8 or first_digit == 9) and (second_digit == third_digit) and (fourth_digit == 8 or fourth_digit == 9):
  print("Ignore")
else:
  print("Answer")
