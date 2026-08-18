file = open('dad_jokes.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    print(line)

# Preferred way of working w/ files
with open('dad_jokes.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())