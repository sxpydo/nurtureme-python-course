# a function to declare 'x' to what data type is used as a variable
x = 0.749
print(type(x))

# What is a float?
# Float is a function converts the specified value into a floating point number.

# task 2: Create a calculator: Ask the user to enter two numbers. Find these two numbers' sum, difference, product, quotient, and remainder
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# calculate the sums by addition, subtraction and multipulcation
sum_addition = number1 + number2
subtraction = number1 - number2
multipulcation = number1 * number2
power = number1 ** number2

# handling division by zero for quotient and remainder
if number2 != 0:
    quotient = number1 / number2
    remainder = number1 % number2
else:
    quotient = "undefined"
    remainder = "undefined"

# display for results
print(f"\nResults:")
print(f"Sum: {sum_addition}")
print(f"Difference: {subtraction}")
print(f"Product: {multipulcation}")
print(f"Power: {power}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
# f = f-string (formatted literal string) - this allows you to embed expressions inside string literals, using curly braces {}


# task 3: Create a program that calculates the perimeter, area and volume of a rectangle with the following dimensions: length = 10cm, width = 5cm, height = 3cm
# Define the dimensions
length = 10  # cm
width = 5    # cm
height = 3   # cm

# calculate the perimeter
perimeter = 2 * (length + width)

# calculate the area
area = length * width

# calculate the volume
volume = length * width * height

# display the results
print(f"Rectangle Dimensions:")
print(f"Length: {length} cm")
print(f"Width: {width} cm")
print(f"Height: {height} cm")
print(f"\nCalculations:")
print(f"Perimeter: {perimeter} cm")
print(f"Area: {area} cm²")
print(f"Volume: {volume} cm³")