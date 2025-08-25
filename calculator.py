message= "Hello there this is my personal calculator, it asks you for the value and operation (+,-,*,/) then it does it's magic"
print(message)

num1=float(input("Input the first number?"))
num2=float(input("Input the second number?"))
operation=input("Enter the operation (+,-,*,/)?")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("Error")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
