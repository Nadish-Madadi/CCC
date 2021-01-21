c1,c2,c3,c4 = map(int,input().split())

print(0, c1, c1+c2, c1+c2+c3, c1+c2+c3+c4)
print(0+c1, 0, c2, c2+c3, c2+c3+c4)
print(0+c1+c2, c2, 0, c3, c3+c4)
print(0+c1+c2+c3, c2+c3, c3, 0, c4)
print(0+c1+c2+c3+c4, c2+c3+c4, c3+c4, c4, 0)

