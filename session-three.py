# Define the variable x and assign it a value
x = 10

# Define the value to compare x with
comparison_value = 5

# Compare x to the comparison_value and print the appropriate message
if x > comparison_value:
    print(f"x is greater than {comparison_value}.")
elif x < comparison_value:
    print(f"x is less than {comparison_value}.")
else:
    print(f"x is equal to {comparison_value}.")

# now, do similiar to compare two numbers
# Prompt the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter the second number: "))

# Compare the two numbers and print the result
if num1 > num2:
    print(f"The first number {num1} is greater than the second number {num2}.")
elif num1 < num2:
    print(f"The first number {num1} is less than the second number {num2}.")
else:
    print("Both numbers are equal.")   

# Task 1: Create a registration program
# Prompt the user to enter their name
name = input("Enter your name: ")
# Prompt the user to enter their city
city = input("Enter your city: ")

# Check if the user is from Leeds and print the appropriate message
if city.lower() == "leeds":
    print(f"Hello {name}. Thank you for registering with us!")
else:
    print(f"Sorry {name}, this service is not available in your city.")


# Task 2: Create a number guessing game
import random

# Generate a secret number between 1 and 100
secret_num = random.randint(1, 100)

# Prompt the user to enter a number between 1 and 99
user_guess = int(input("Enter a number between 1 and 99: "))

# Compare the user's guess with the secret number and provide feedback
if user_guess < secret_num:
    print("Your guess is too low.")
elif user_guess > secret_num:
    print("Your guess is too high.")
else:
    print("Congratulations! You are the winner!")
    print("The secret number is " + str(secret_num))

# Task 3: Ask a user to enter their age
# Prompt the user to enter their age
age = int(input("Please enter your age: "))

# Determine the age category and print the appropriate message
# Prompt the user to enter their age
age = int(input("Please enter your age: "))

# Determine the age category and print the appropriate message
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:  # Using 'and' to combine conditions
    print("You are an adult.")
else:
    print("You are an elder.")
