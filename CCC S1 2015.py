list1 = []

for i in range(int(input())):
  x = int(input())
  if x == 0: list1.pop()
  else: list1.append(x)

print(sum(list1))