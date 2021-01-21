T = input()
S = input()
val = "False"

for i in range(len(S)):
  S = S[-1] + S[:-1]

  if S in T:
    val = "True"
    break

if val == "True": 
  print("yes")
else:
  print("no")
