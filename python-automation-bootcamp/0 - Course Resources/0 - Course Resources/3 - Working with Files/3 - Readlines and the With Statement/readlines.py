with open('dad_jokes.txt','r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())