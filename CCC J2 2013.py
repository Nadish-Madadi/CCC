word = input()
x = list(word)

for i in range(len(x)):
  if x[i] == "I" or x[i] == "O" or x[i] == "S" or x[i] == "H" or x[i] == "Z" or x[i] == "X" or x[i] == "N":
    y = "YES"
  else:
    y = "NO"

print(y)
