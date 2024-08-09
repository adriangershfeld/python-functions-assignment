# Task 1: Create functions for each arithmetic operation.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible."      # fixed division by zero
    else:
        return a / b


# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. 
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.


while True:

    operation = input("Would you like to [A]dd, [S]ubtract, [M]ultiply, [D]ivide, or [Q]uit? ").upper()

    if operation == 'Q':
         print("Exiting Calculator!")
         break

    if operation in ['A', 'S', 'M', 'D']:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if operation == 'A':
                result = add(a, b)
            elif operation == 'S':
                result = subtract(a, b)
            elif operation == 'M':
                result = multiply(a, b)
            elif operation == 'D':
                result = divide(a, b)
            
            if isinstance(result, str):
                 print(result)          # fixed "The result is Division by zero is not possible."
            else:
                 print(f"The result is {result}")

        except ValueError:
            print("Invalid input. Please enter number values.")


    else:
                print("Invalid operation. Please choose again.")

