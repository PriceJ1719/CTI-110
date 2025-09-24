# jason price
# 23sep2025
# P1HW1
# program that calculates exponents and performs addition - subtraction

# -----Calculating Exponenets----
print("-----Calculating Exponenets----\n")

# get user input for base and exponent
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

# perform exponent calculation
result = base ** exponent

# display result
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# -----dddition and subtraction----
print("-----Addition and Subtraction----\n")

# get user inputs for addition and subtraction
start_value = int(input("Enter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
subtract_value = int(input("Enter an integer to subtract: "))

# perform math
final_result = start_value + add_value - subtract_value

# display result
print(f"\n{start_value} + {add_value} - {subtract_value} is equal to {final_result}")
