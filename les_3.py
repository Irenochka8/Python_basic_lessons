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

print("Мій список")

my_list = [6, 9, 3, 4, 45, 78, 100]
if my_list == [] :
    print(my_list)
elif my_list [0:] :
    (my_list.insert(0, my_list[-1]))
    (my_list.pop (-1))
    print(my_list)

