import pdb

# Method 1 for reading, and closing text files.
file = open('dad_jokes.txt', 'r') # opens the file
content = file.read() # reads the file and returns as a single string
print(content)
file.close() # need to close to free up resources and save any changes we may have made

pdb.set_trace()
