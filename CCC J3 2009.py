ottawa = int(input())
y = list(str(ottawa))


for i in range(len(y)):
  y[i] = int(y[i])

'''
Ottawa : 0 difference
Victoia : -300 difference
Edmonton : -200 difference
Winnipeg : -100 difference
Toronto : 0 difference
Halifax : +100 difference
St. John’s : +130 difference
'''

if len(y) >= 1 and len(y) <= 2:

  if ottawa >= 0 and ottawa <= 30:

    print(f"{ottawa} in Ottawa")
    print(f"{abs(2400 + (ottawa - 300))} in Victoria")
    print(f"{abs(2400 + (ottawa - 200))} in Edmonton")
    print(f"{abs(2400 + (ottawa - 100))} in Winnipeg")
    print(f"{ottawa} in Toronto")
    print(f"{ottawa + 100} in Halifax")
    print(f"{ottawa + 130} in St. John's")


#checks if second last number is 0,1,2 and in between 0 and 9 or if second last number is 3 and last number is 0
if len(y) >= 2 and len(y) <= 4:
  if (y[-2] == 0 or y[-2] == 1 or y[-2] == 2 and y[-1] in range(0,10)) or (y[-2] == 3 and y[-1] == 0):
    
    if ottawa >= 2300 and ottawa <= 2359:
      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{abs(2360 - (ottawa + 100))} in Halifax")
      print(f"{abs(2360 - (ottawa + 130))} in St. John's")

    if ottawa >= 2230 and ottawa <= 2259:
      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{abs(2360-(ottawa + 130))} in St. John's")

    if ottawa >= 300 and ottawa <= 2229:

      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      if y[-2] == 3 and y[-1] == 0:
        print(f"{ottawa + 170} in St. John's")
      else:
        print(f"{ottawa + 130} in St. John's")

    if ottawa >= 200 and ottawa <= 259:
      print(f"{ottawa} in Ottawa")
      print(f"{abs(2400 + (ottawa - 300))} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 130} in St. John's")

    if ottawa >= 100 and ottawa <= 159:
      print(f"{ottawa} in Ottawa")
      print(f"{abs(2400 + (ottawa - 300))} in Victoria")
      print(f"{abs(2400 + (ottawa - 200))} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 130} in St. John's")
    
    
  #checks second last number if 3,4,5 and if last number between 0 and 9
  if ((y[-2] == 3 and y[-1] in range(1,10)) or y[-2] == 4 or y[-2] == 5 and y[-1] in range(0,10)):

    if ottawa >= 31 and ottawa <= 59:

      print(f"{ottawa} in Ottawa")
      print(f"{abs(2400 + (ottawa - 300))} in Victoria")
      print(f"{abs(2400 + (ottawa - 200))} in Edmonton")
      print(f"{abs(2400 + (ottawa - 100))} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 170} in St. John's")

    if ottawa >= 100 and ottawa <= 159:
      print(f"{ottawa} in Ottawa")
      print(f"{abs(2400 + (ottawa - 300))} in Victoria")
      print(f"{abs(2400 + (ottawa - 200))} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 170} in St. John's")
    
    if ottawa >= 200 and ottawa <= 259:
      print(f"{ottawa} in Ottawa")
      print(f"{abs(2400 + (ottawa - 300))} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 170} in St. John's")

    if ottawa >= 300 and ottawa <= 2229:

      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{ottawa + 170} in St. John's")

    if ottawa >= 2230 and ottawa <= 2259:
      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{ottawa + 100} in Halifax")
      print(f"{abs(2360-(ottawa + 130))} in St. John's")

    if ottawa >= 2300 and ottawa <= 2359:
      print(f"{ottawa} in Ottawa")
      print(f"{ottawa - 300} in Victoria")
      print(f"{ottawa - 200} in Edmonton")
      print(f"{ottawa - 100} in Winnipeg")
      print(f"{ottawa} in Toronto")
      print(f"{abs(2360 - (ottawa + 100))} in Halifax")
      print(f"{abs(2360 - (ottawa + 130))} in St. John's")
