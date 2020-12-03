speed_limit = int(input("Enter an integer for the speed limit: "))
recorded_speed = int(input("Enter an integer for the recorded speed: "))

calculated_speed = recorded_speed - speed_limit

if calculated_speed <= 0:
    print("Congratulations, you are within the speed limit!")
    
elif calculated_speed in range(1,21):
    print(f"You are speeding and your fine is $100")
    
elif calculated_speed in range(21,32):
    print(f"You are speeding and your fine is $270")
    
elif calculated_speed >= 31:
    print(f"You are speeding and your fine is $500")
    
