# jason price
# 24sep2025
# P1HW2
# this program calculates and displays travel expenses 


# pseudocode detail algorithm
# 1-ask user for their budget
# 1a-ask user for travel destination
# 1b-ask user how much they will spend on gas
# 1c-ask user how much they will spend on accommodation
# 1d-ask user how much they will spend on food
# 2-add the three expenses together
# 3-subtract total expenses from budget
# 4-display travel details destination/initial budget/expenses/remaining balance

print("This program calculates and displays travel expenses\n")

# get user inputs
budget = int(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

# calc total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# print results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")
print("\nRemaining Balance:", remaining_balance)
