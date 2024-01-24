#завдання 1:
#змінити список, щоб всі нулі були в кінці списку
value = [9, 0, 7, 31, 0, 45, 0, 45,0, 45, 0, 0, 96, 0]
for i in range(len(value)-1, -1, -1):
    if value[i] == 0:
        value.append(value.pop(i))
print(value)

#завдання 2:

my_range = [1, 3, 5]
if len(my_range)>0:
    my_range_1 = my_range[::2]
    print(sum(my_range_1)*my_range[-1])
else:
    print("0")


