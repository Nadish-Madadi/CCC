angle_a = int(input("Provide an angle for the first side: "))
angle_b = int(input("Provide an angle for the second side: "))
angle_c = int(input("Provide an angle for the third side: "))

angles_sum = angle_a + angle_b + angle_c

if angles_sum != 180:
    print("Error")
else:
    if angles_sum == 180:
        if angle_a == angle_b == angle_c:
            print("Equiallteral")
        elif angle_a == angle_b or angle_a == angle_c or angle_b == angle_c:
            print("Isoceles")
        else:
            print("Scalene")
            
