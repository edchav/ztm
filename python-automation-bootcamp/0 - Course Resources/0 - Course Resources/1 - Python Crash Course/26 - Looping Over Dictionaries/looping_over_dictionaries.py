person = { 

    'name': 'Alice', 

    'age': 30, 

    'job': 'Engineer' 

}

# for key in person:
#   print(key)

# for value in person.values():
#   print(value)

for key, value in person.items():
  output = f'{key}: {value}'
  print(output)