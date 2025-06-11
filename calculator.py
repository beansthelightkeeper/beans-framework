# calculator.py

def calculate():
    print("Simple Calculator: BEANZ HANDELZ PYTHONS")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

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
            print("❌ Cannot divide by zero.")
            return
    else:
        print("❌ Invalid operator.")
        return

    print(f"Result: {result}")

calculate()