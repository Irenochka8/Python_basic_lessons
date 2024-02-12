#Task_1 make generator func

def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    for i in range(end):
        yield begin
        begin = func(begin)
gen = some_gen(2, 4, pow)
from inspect import isgenerator

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

#Task_2 check for double number

def is_even(digit):
    if digit % 2 == 0:
        return True
    else:
        return False
print(is_even(5))
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')