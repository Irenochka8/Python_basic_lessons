#Task_1
sentence = input("login: ")
literal = '''!"#$%&'()*+,  -./:;<=>?@[\\]^`{|}~'''
kwlist = ["False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class",
          "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal",
          "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"]

result = "True"

for char in sentence:
    if char.isupper() or char.isspace() or char in literal:
        result = "False"
        break

if sentence in kwlist:
    result = "False"

if sentence[0].isdigit():
    result = "False"

if sentence.find("_")>1:
    result = "False"

print(result)

#Task_2
print("Калькулятор")

result = 0
while True:
    number_n1 = float(input("Введіть перше число:"))
    operation = input("Оберіть дію зі списку (+, -, *, /):")
    number_n2 = float(input("Введіть друге число:"))
    if operation not in ("+", "-", "*", "/"):
        result = "Wrong operation"
    if operation == "+":
        result = (number_n1 + number_n2)
    if operation == "-":
        result = (number_n1 - number_n2)
    if operation == "*":
        result = (number_n1 * number_n2)
    if operation == "/":
        if number_n2 == 0:
            result = ("Cannot be divided by zero")
        else:
            result = (number_n1 / number_n2)
    print(f"Результат дії = {result}")
    calc_exit = input("press y for continue or b for break: ")
    if calc_exit == "y":
        continue
    if calc_exit == "b":
        break










# if sentence.count('_') == 1:
#     result = "True"
# else:
#     sentence.count('_')<1
#     result = "False"

    # if sentence[0].isdigit():
    #     result = "False"
    # else:
    #     result = "True"




    # for text in sentence:
    #     if i in kwlist == sentence:
    #         result = "False"
    #     else:
    #         result = "True"
    #if sentence.find(literal):
    #    result = "False"
    #else:
    #    sentence.isalpha()
    #    result = "True"
    # for i in sentence:
    #     if i in kwlist:
    #     result = "False"
    # else:
    #     result = "True"











