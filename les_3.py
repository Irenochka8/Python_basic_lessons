print("Калькулятор")
number_n1 = float(input("Введіть перше число:"))
operation = input("Оберіть математичну дію (+, -, *, /):")
number_n2 = float(input("Введіть друге число:"))

if operation == "+":
    print(number_n1 + number_n2)

if operation == "-":
    print(number_n1 - number_n2)

if operation == "*":
    print(number_n1 * number_n2)

if operation == "/":
    if number_n2 == 0:
        print("Cannot be divided by zero")
    else:
        print(number_n1 / number_n2)



