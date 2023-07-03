# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

while True:
    # Take user input for the numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the arithmetic operation (+, -, *, /): ")

    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"The difference between {num1} and {num2} is {result}")
    elif operation == '*':
        result = multiply(num1, num2)
        print(f"The product of {num1} and {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = divide(num1, num2)
            print(f"The division of {num1} by {num2} is {result}")
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Error: Invalid operation")
    
    # Ask if the user wants to continue calculating
    choice = input("Do you want to continue calculating? (Y/N): ")
    if choice == "N":
        break
    elif choice == "Y":
        continue
    else:
        print("Invalid choice, continuing with calculations...")
        continue


    