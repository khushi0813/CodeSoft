# Simple Calculator

# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Main program
print("Simple Calculator")

# User input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# User input for the operation choice
print("Choose an operation:")
print("add - Addition")
print("subtract - Subtraction")
print("multiply - Multiplication")
print("divide - Division")
operation = input("Enter the operation: ").lower()

# Perform the calculation
result = calculate(num1, num2, operation)

# Display the result
print(f"The result of {operation} between {num1} and {num2} is: {result}")

 


