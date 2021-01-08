# Name: Nadish Madadi
# Date: October 18, 2020
# Purpose: To create a trident using asterisks
# FileName: CCC J1 2003.py

# user input to acquire data on line length, space length, and handle length of trident
tine_length = int(input("Enter line length: "))
tine_spacing = int(input("Enter line spacing: "))
handle_length = int(input("Enter handle length: "))

# assign the amount of spaces needed
spacing = " " * tine_spacing

# for loop to create asterisks with spaces in between, in other words to create the prongs
for i in range(tine_length):
    print("*", "*", "*", sep=spacing)

# assign the number of spaces to find the length necessary for the middle line
middle_line = 3 + len(spacing * 2)

# prints the middle line of asterisks
print("*" * middle_line)

# for loop to create the trident handle
# aligns the asterisks to the middle by using the same spacing as before and adding an extra space
# extra space to make up for the missing asterisk at the beginning
for f in range(handle_length):
    print(spacing + " *")
