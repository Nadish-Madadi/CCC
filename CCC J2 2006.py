m = int(input("Enter m: "))
n = int(input("Enter n: "))
final = 0


for i in range(1,m+1):
  for x in range(1,n+1):
    if i + x == 10:
      final += 1


if final == 1:
  print("There is 1 way to get the sum 10 ")
if final > 1:
  print(f"There are {final} ways to get the sum 10.")

