rounds = int(input())
random_list_1 = []
random_list_2 = []

Antonia = 100
David = 100


for i in range(rounds):
  A = list( map( int, input().split()))
  random_list_1.append(A[0])
  random_list_2.append(A[1])


for j in range(rounds):
  if random_list_1[j] > random_list_2[j]:
    David = David - random_list_1[j]
  if random_list_2[j] > random_list_1[j]:
    Antonia = Antonia - random_list_2[j]
  if random_list_1[j] == random_list_2[j]:
    David = David
    Antonia = Antonia
  
print(Antonia)
print(David)
