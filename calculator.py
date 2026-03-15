# calculator.py
print("===simple calculator===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("We can't divide by zero.")
