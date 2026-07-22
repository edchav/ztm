# translations = {"hello": "bonjour", "yes": "oui", "no": "non"}

# # hello_in_french = translations["hello"]

# # print(hello_in_french)

# translations["thank you"] = "merci"

# print(len(translations))

students_list = [ 

    ['Alice Doe', 20, [85, 90, 95]], 

    ['Bob Smith', 22, [88, 92, 90]], 

    ['Todd', 21, [80, 85, 78]] 

]


students_dict = { 

    'Alice Doe': {'age': 20, 'grades': [85, 90, 95]}, 

    'Bob Smith': {'age': 22, 'grades': [88, 92, 90]}, 

    'Todd': {'age': 21, 'grades': [80, 85, 78]} 

}

todd_age = students_dict['Todd']['age']

print(todd_age)

todd_grade_2 = students_dict['Todd']['grades'][1]

print(todd_grade_2)