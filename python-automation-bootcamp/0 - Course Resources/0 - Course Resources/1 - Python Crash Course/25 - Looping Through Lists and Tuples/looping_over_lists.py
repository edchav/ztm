#my_list = ["eagle", 42, "soccer", 3.14, "mountain", "Paris", 2023, 0.99, "guitar", "rainbow"]
my_list = ("eagle", 42, "soccer", 3.14, "mountain", "Paris", 2023, 0.99, "guitar", "rainbow")

numeric_values = []

for item in my_list:
  if type(item) == int or type(item) == float:
    numeric_values.append(item)

print(numeric_values)