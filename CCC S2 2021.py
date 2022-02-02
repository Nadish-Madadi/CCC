m,n,k = int(input()),int(input()),int(input())
a = 0

r_list = [input() for i in range(k)]

outer_list = [[True] * n for i in range(m)]

while a < k:
  x = r_list[a].split(" ")
  x[1] = int(x[1])
  if x[0] == "R":
    for j in range(n):
      outer_list[x[1] - 1][j] = not (outer_list[x[1] - 1][j])
  elif x[0] == "C":
    for j in range(m):
      outer_list[j][x[1] - 1] = not (outer_list[j][x[1] - 1])
  a += 1

counter = sum([outer_list[i].count(False) for i in range(m)])

print(counter)