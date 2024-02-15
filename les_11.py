#Task_1 generator prime numbers
def count_divider(n):           #функція для підрахунку дільників для числа
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
#print(count_divider(5))

def prime_generator(end):          #функція-генератор для діапазону чисел
    for i in range(2, end + 1):
        if count_divider(i) == 2:
            yield i

from inspect import isgenerator
gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

#Task_2 check for double number with bit operation
def is_even(digit):
    if digit & 1 == 0:
        return True
    else:
        return False
#print(is_even(5))
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')