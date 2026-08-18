additional_lines = ['Stars up above,\n','Whisper words of love']

# allows to write multiple lines vs one line at a time (.write)
with open('poem.txt', 'a') as file:
    file.writelines(additional_lines)