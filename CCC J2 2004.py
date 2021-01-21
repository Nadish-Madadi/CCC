import math
X = int(input("Enter the current year: \n"))
Y = int(input("Enter a future year: \n"))
total_increment = math.floor(((Y-X)/60))
count = 0;

print(f"All positions change in year {X}")
for i in range(0, (Y-X)+1):
  while count < total_increment:
    X = X + 60
    print(f"All positions change in year {X}")
    count = count + 1
