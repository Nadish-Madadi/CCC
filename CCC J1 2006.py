print("Welcome to Chip’s Fast Food Emporium")
input1 = int(input("Please enter a burger choice:"))
input2 = int(input("Please enter a side order choice:"))
input3 = int(input("Please enter a drink choice:"))
input4 = int(input("Please enter a dessert choice:"))

list1 = [461,431,420,0]
list2 = [100,57,70,0]
list3 = [130,160,118,0]
list4 = [167,266,75,0]

total = 0

if input1 == 1:
  total += list1[0]
if input1 == 2:
  total += list1[1]
if input1 == 3:
  total += list1[2]
if input1 == 4:
  total += list1[3]

if input2 == 1:
  total += list2[0]
if input2 == 2:
  total += list2[1]
if input2 == 3:
  total += list2[2]
if input2 == 4:
  total += list2[3]

if input3 == 1:
  total += list3[0]
if input3 == 2:
  total += list3[1]
if input3 == 3:
  total += list3[2]
if input3 == 4:
  total += list3[3]

if input4 == 1:
  total += list4[0]
if input4 == 2:
  total += list4[1]
if input4 == 3:
  total += list4[2]
if input4 == 4:
  total += list4[3]

print(f"Your total Calorie count is {total}.")
