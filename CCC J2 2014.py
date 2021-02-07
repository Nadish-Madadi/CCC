V = int(input())
votes = input()
x = list(votes)

if x.count("A") > x.count("B"):
  print("A")
if x.count("B") > x.count("A"):
  print("B")
if x.count("A") == x.count("B"):
  print("Tie")
