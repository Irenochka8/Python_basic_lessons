relatives_list = [{"name": "Sam", "age": 45}, {"name": "Nick", "age": 23}, {"name": "Sarah", "age": 7}, {"name": "Guliaaawah", "age": 18}, {"name": "Michael", "age": 7}, {"name": "Anastasiia", "age": 12}]
# min_age_sorted = sorted(relatives_list, key=lambda x: x["age"])
# min_age = min_age_sorted[0]["age"]
# min_age_list = []
# for person in relatives_list:
#     if person["age"] == min_age:
#         #print(person["name"])
#         min_age_list.append(person["name"])
# print(min_age_list)
#
# len_name_sorted = sorted(relatives_list, key=lambda x: len(x["name"]))
# max_name = len(len_name_sorted[-1]["name"])
# max_len_names = []
# for person in relatives_list:
#     #print(person["name"])
#     if len(person["name"]) == max_name:
#         #print(person["name"])
#         max_len_names.append(person["name"])
# print(max_len_names)

#all_ages = sum(relatives_list[0:]["age"])
medium_ages = []

for person in relatives_list:
    all_ages = person.get("age")
    [medium_ages] = sum(person.get("age"))/len(person.get("age"))

    medium_ages.append(person["age"])
print(medium_ages)





    #print(min_age["age"])
#relatives_list_sorted = {}
#for person in relatives_list:
#    relatives_list_sorted = sorted(relatives_list, key=lambda x: x["age"])
    #print(relatives_list_sorted)
#    min_age = []
    #print(min_age)
    # min_age.append(relatives_list_sorted.pop(0))
    #print(min_age)

    # if value in min_age == value in relatives_list_sorted:
    #     print(min_age["name"])

#print(min_age_relative) ---всі дані про наймолодшого
# print(age_relative["name"])#---тільки ім'я
# while relatives_list_sorted[0]["age"] == relatives_list_sorted[1:]["age"]:
#     min_age_few.append(relatives_list_sorted.pop(0))
#     sorted(relatives_list_sorted, key=lambda x: x["age"])
#     if relatives_list_sorted[0]["age"] == relatives_list_sorted[1:]["age"]:
#         min_age_few.append(relatives_list_sorted.pop(0))


        # min_age["age"] == relatives_list_sorted[0]:
        # print(min_age_few["name"])




# for person in relatives_list_sorted:
#     if person["age"] == relatives_list_sorted[0]:
#         min_age = relatives_list_sorted[0:]
#         print(min_age_few)
#     else:
#         print(min_age)

# for item in relatives_list_sorted:
#     if item == relatives_list_sorted[0]:
#         min_age_relative.pop(item)
#         print((min_age_relative)+(min_age_relative.pop(item)))
#     if value in relatives_list_sorted["age"[0]] == value in relatives_list_sorted["age"[1:]]:
#         print(min_age_relative)

#for person in relatives_list:
#     relatives_list_sorted = sorted(relatives_list, key=lambda x: x["age"])
#     min_age = relatives_list_sorted[0]
#     print(min_age["name"])
# if relatives_list_sorted[0]["age"] == relatives_list_sorted[1:]["age"]:
#     relatives_list_sorted = sorted(relatives_list_sorted, key=lambda x: x["age"])
#     print(relatives_list_sorted["name"])

