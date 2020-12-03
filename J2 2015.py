emotion = input()

happy = emotion.count(":-)")
sad = emotion.count(":-(")

if happy > sad:
  print("happy")
elif sad > happy:
  print("sad")
elif happy == 0 and sad == 0:
  print("none")
elif happy == sad:
  print("unsure")
