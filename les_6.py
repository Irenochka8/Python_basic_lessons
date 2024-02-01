# Task1
relatives_list = [{"name": "Sam", "age": 45}, {"name": "Nick", "age": 23}, {"name": "Sarah", "age": 7}, {"name": "Guliaaawah", "age": 18}, {"name": "Michael", "age": 7}, {"name": "Anastasiia", "age": 12}]
min_age_sorted = sorted(relatives_list, key=lambda x: x["age"])
min_age = min_age_sorted[0]["age"]
min_age_list = []
for person in relatives_list:
    if person["age"] == min_age:
        #print(person["name"])
        min_age_list.append(person["name"])
print(min_age_list)

len_name_sorted = sorted(relatives_list, key=lambda x: len(x["name"]))
max_name = len(len_name_sorted[-1]["name"])
max_len_names = []
for person in relatives_list:
    #print(person["name"])
    if len(person["name"]) == max_name:
        #print(person["name"])
        max_len_names.append(person["name"])
print(max_len_names)


relatives_list = [{"name": "Sam", "age": 45}, {"name": "Nick", "age": 23}, {"name": "Sarah", "age": 7}, {"name": "Guliaaawah", "age": 18}, {"name": "Michael", "age": 7}, {"name": "Anastasiia", "age": 12}]

all_ages = []

for person in relatives_list:
    all_ages.append(person['age'])
medium_ages = (round(sum(all_ages)/len(all_ages)))
print(medium_ages)

# Task2
my_dict_1 = {"name": "Sam",
             "age": "17",
             "hobby": "gym",
             "friend": "Iren"
             }
my_dict_2 = {"name": "Michael",
             "age": "23",
             "country": "Ukraine",
             "town": "Dynpro"
             }
key_both_dic = []
for key in my_dict_1:
    if key in my_dict_2:
        key_both_dic.append(key)
print(key_both_dic)

key_dic_1= []
for key in my_dict_1:
    if key not in my_dict_2:
        key_dic_1.append(key)
print(key_dic_1)

key_value_dic_1 = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        key_value_dic_1.update({key: value})
print(key_value_dic_1)

key_dic_1_2 = {}

for key, value in my_dict_1.items():
    if key not in my_dict_2:
        key_dic_1_2.update({key: [value]})

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        key_dic_1_2.update({key: [value]})

for key, value in my_dict_1.items():
    if key in my_dict_2:
        key_dic_1_2.update({key: [my_dict_1[key], my_dict_2[key]]})

print(key_dic_1_2)




