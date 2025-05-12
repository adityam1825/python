# Function for addition
def add_numbers(a, b):
    return a + b

# Function for subtraction
def subtract_numbers(a, b):
    return a - b

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+ or -): ")

# Performing the operation
if operation == '+':
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")
elif operation == '-':
    result = subtract_numbers(num1, num2)
    print(f"The difference is: {result}")
else:
    print("Invalid operation! Please enter '+' or '-'.")
