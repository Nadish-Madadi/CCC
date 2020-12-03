apple_three = int(input("# of Successful 3-point shots: "))
apple_two = int(input("# of Successful 2-point shots: "))
apple_one = int(input("# of Successful 1-point shots: "))
banana_three = int(input("# of Successful 3-point shots: "))
banana_two = int(input("# of Successful 2-point shots: "))
banana_one = int(input("# of Successful 1-point shots: "))

apple_total_score = ((3*apple_three)+(2*apple_two)+(1*apple_one))
banana_total_score = ((3*banana_three)+(2*banana_two)+(1*banana_one))

if apple_total_score > banana_total_score:
  print("A")
elif banana_total_score > apple_total_score:
  print("B")
elif apple_total_score == banana_total_score:
  print("T")
  
