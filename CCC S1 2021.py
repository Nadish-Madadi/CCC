wood = int(input())

empty_list = []

bases = input().split(" ")
heights = input().split(" ")

bases = [int(i) for i in bases] 

heights = [int(i) for i in heights] 


for i in range(wood):
  A = 0.5*(bases[i] + bases[i+1])*(heights[i])
  empty_list.append(A)
  i += 1

print(sum(empty_list))


'''
Right-Trapeziod Formula:

A = 0.5(a+b)(h)

'''