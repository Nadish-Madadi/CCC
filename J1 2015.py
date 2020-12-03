month = int(input("Enter the month:"))
day = int(input("Enter the day:"))

if month in range(1,3) and day in range(1,18):
  print("Before")
elif month in range(3,13) and day in range(0,32):
  print("After")
elif month == 2 and day in range(19,32):
  print("After")
elif month == 2 and day == 18:
  print("Special")
