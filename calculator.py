# Prompt user for input
num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Can't divide by zero"
else:
    result = "Error: Invalid operator"

# Display result
print(f"Result: {result}")