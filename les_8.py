# Task_1 Список перетворити в число, додати 1 і повернути списком

some_list = [1, 2, 1, 1]
def add_one(some_list):
    num_str = ""
    for digit in some_list:
        num_str += str(digit)
    number = int(num_str) + 1
    result_list = [int(num) for num in str(number)]
    return result_list
print(add_one(some_list))

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

# Task_2 Знайти унікальне число:

def find_unique_value(some_list):
    list_unique_numb = ""
    for i in some_list:
        if some_list.count(i) == 1:
            list_unique_numb = i
    return list_unique_numb
print(find_unique_value(some_list))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")