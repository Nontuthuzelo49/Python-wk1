def calculator():
    # The user should be able to input two numbers, and then choose an operation to perform on the two numbers.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # The calculator should be able to add, subtract, multiply, and divide.
    operation = input("Choose an operation(+, -, *, /): ")

    # Perform the operation based on user input
    if operation == "+":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

    elif operation == "-":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

    elif operation == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

    elif operation == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
    else:
            print("Invalid operation")

calculator()
