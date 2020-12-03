bow_height = int(input("Enter a height: "))

while True:
  if bow_height%2 == 1 and bow_height >= 5:
      for i in range(1,bow_height+1,2):
          print("*" * i + " "*(2*bow_height - 2*i)+ "*"*i)
      for i in range(bow_height-2,0,-2):
          print("*" * i + " "*(2*bow_height - 2*i)+ "*"*i)
      break
  else:
    print("Enter number greater than 5 and only odd numbers")
  break
