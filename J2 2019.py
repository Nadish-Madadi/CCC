L = int(input())
symbol = []
number = []

for i in range(L):
  x = input().split()
  number.append(int(x[0]))
  symbol.append(x[1])

for i in range(L):
  print(symbol[i]*number[i])
