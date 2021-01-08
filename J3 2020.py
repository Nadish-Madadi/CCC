N = int(input())

x_lst = []
y_lst = []

for i in range(N):
  dots = input().split(',')
  x_lst.append(int(dots[0]))
  y_lst.append(int(dots[1]))

x_max = max(x_lst)
y_max = max(y_lst)
x_min = min(x_lst)
y_min = min(y_lst)

x_max += 1
y_max += 1
x_min -= 1
y_min -= 1

print(f"{x_min},{y_min}")
print(f"{x_max},{y_max}")
