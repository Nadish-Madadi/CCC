lower_limit = int(input("Enter lower limit of range \n"))
upper_limit = int(input("Enter upper limit of range \n"))
count = 0

for i in range(lower_limit, upper_limit + 1):
  rsa = 0
  for j in range(1, i + 1):
    if i % j == 0:
      rsa += 1
  if rsa == 4:
    count += 1

print(f"The number of RSA numbers between {lower_limit} and {upper_limit} is {count}")

