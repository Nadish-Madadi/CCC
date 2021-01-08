game_one = (input("W or L: "))
game_two = (input("W or L: "))
game_three = (input("W or L: "))
game_four = (input("W or L: "))
game_five = (input("W or L: "))
game_six = (input("W or L: "))

games_list = []

games_list.extend((game_one, game_two, game_three, game_four, game_five, game_six))

if games_list.count("W") in range(1,3):
  print("3")
elif games_list.count("W") in range(3,5):
  print('2')
elif games_list.count("W") in range(5,7):
  print("1")
else:
  print("-1")
  
