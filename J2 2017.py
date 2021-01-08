n = int(input("Enter a number to start with: "))
k = int(input("Enter a number between 0 and 5 to shift the first number by: "))

a_list = [n]

for i in range(k):
  x = a_list[-1]*10
  a_list.append(x)

print(sum(a_list))
