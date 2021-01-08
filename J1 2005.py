daytime_minutes = int(input("Number of daytime minutes: "))
evening_minutes = int(input("Number of evening minutes: "))
weekend_minutes = int(input("Number of weekend minutes: "))

if daytime_minutes > 100:
  plan_a = ((daytime_minutes - 100)*0.25) + (0.15 * evening_minutes) + (0.20 * weekend_minutes)
  print(f"Plan A costs {plan_a}")
elif daytime_minutes <= 100:
  plan_a = (0.15 * evening_minutes) + (0.20 * weekend_minutes)
  print(f"Plan A costs {plan_a}")

if daytime_minutes > 250:
  plan_b = ((daytime_minutes - 250)*0.45) + (0.35 * evening_minutes) + (0.25 * weekend_minutes)
  plan_b = round(plan_b,2)
  print(f"Plan B costs {plan_b}")
elif daytime_minutes <= 250:
  plan_b = (0.35 * evening_minutes) + (0.25 * weekend_minutes)
  plan_b = round(plan_b,2)
  print(f"Plan B costs {plan_b}")

if plan_a > plan_b:
  print("Plan B is the cheapest")
elif plan_a < plan_b:
  print("Plan A is the cheapest")
else:
  print("Plan A and Plan B cost the same")
  
