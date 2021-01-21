Y = int(input())
t = Y 
x = list(map(int, str(t)))

if len(x) == 1:
    e = Y + 1

if len(x) == 2:
  for i in range(100):
    t += 1
    x = list(map(int, str(t)))
    if x[0] != x[1]:
      e = t
      break

if len(x) == 3:
  for i in range(1000):
    t += 1
    x = list(map(int, str(t)))
    if x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
      e = t
      break

if len(x) == 4:
  for i in range(10000):
    t += 1
    x = list(map(int, str(t)))
    if x[0] != x[1] and x[0] != x[2] and x[0] != x[3] and x[1] != x[2] and x[1] != x[3] and x[2] != x[3]:
      e = t
      break

if len(x) >= 5:
  e = ""

print(e)
