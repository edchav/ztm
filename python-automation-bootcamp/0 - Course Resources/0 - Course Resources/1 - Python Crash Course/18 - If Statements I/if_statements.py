# if False:
#   print("I'm true!")

cities = ["New York", "Los Angeles", "Chicago", "Seattle", "Phoenix"]

user_city = input('Please enter the name of your city: ')

if user_city not in cities:
  response = f"Yes, {user_city} is in our list of cities, so you get a discount!"
  print(response)
else:
  print("Sorry, no discount for you!")