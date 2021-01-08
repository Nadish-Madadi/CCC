w1, w2, w3, w4 = map(int, input("Enter four values: ").split())
x1, x2, x3, x4 = map(int, input("Enter four values: ").split())
y1, y2, y3, y4 = map(int, input("Enter four values: ").split())
z1, z2, z3, z4 = map(int, input("Enter four values: ").split())

list1 = []
list2 = []
list3 = []
list4 = []

list1.extend((w1, w2, w3, w4))
list2.extend((x1, x2, x3, x4))
list3.extend((y1, y2, y3, y4))
list4.extend((z1, z2, z3, z4))

if (w1+ w2+ w3+ w4) == (x1 + x2 + x3 + x4) == (y1 + y2 + y3 + y4) == (z1 + z2 + z3 + z4) == (w1 + x1 + y1 + z1) == (w2 + x2 + y2 + z2) == (w3 + x3 + y3 + z3) == (w4 + x4 + y4 + z4):
  print("magic")
else:
  print("not magic")
  
