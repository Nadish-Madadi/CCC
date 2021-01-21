t1 = int(input())
t2 = int(input())

list1 = [t1,t2]

for i in range(10000):
  x = list1[-2] - list1[-1]
  list1.append(x)

  if list1[-1] > list1[-2]:
    print(len(list1))
    break
