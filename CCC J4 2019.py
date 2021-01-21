x = input()

y = list(x)
list1 = [[1,2],[3,4]]

for i in range(len(y)):
  if y[i] == 'H':
    list1[0][0], list1[1][0] = list1[1][0], list1[0][0]
    list1[0][1], list1[1][1] = list1[1][1], list1[0][1]
  if y[i] == 'V':
    list1[0][0], list1[0][1] = list1[0][1], list1[0][0]
    list1[1][0], list1[1][1] = list1[1][1], list1[1][0]

print(list1[0][0], list1[0][1])
print(list1[1][0], list1[1][1])

