while True:
  p_value = int(input("Please provide a value for P: "))
  if p_value > 10**7:
    print("Please enter a value for P within 10**7 number of infections")
  else:
    break
while True:
  n_value = int(input("Please provide a value for N: "))
  if n_value > p_value:
    print("Please provide a value for N smaller than P")
  else:
    break
while True:
  r_value = int(input("Please provide a value for R: "))
  if r_value > 10:
    print("Provide a value for R below 10")
  else:
    break

print("\n")

print(f"Cap off value for number of infections: {p_value}")
print(f"Number of people infected on Day 0: {n_value}")
print(f"Number of people infected on Day 1: {r_value}")

mylist = [n_value]
while sum(mylist) <= p_value:
  mylist_x_r_value = mylist[-1]*r_value
  mylist.append(mylist_x_r_value)

  if sum(mylist) > p_value:
    break

result = len(mylist) - 1
print(result)
