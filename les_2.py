#створюємо ввод даних (4х значне число) з клавіатури,далі виводимо в стовпчик по 1 цифрі
some_number=int(input("Введіть будь ласка будь яке 4-х значне число:"))
some_number_1=some_number//1000 #розряд тисяч
some_number_2=some_number//100%10 #розряд сотень
some_number_3=some_number//10%10 #розряд десятків
some_number_4=some_number%10 #розряд одиниць
print(some_number_1)
print(some_number_2)
print(some_number_3)
print(some_number_4)