# TODO 1: Import the Python regular expressions module



# TODO 2: Define your regular expressions

# TODO 2a: Write a regex for North American-style phone numbers, where numbers may be separated by a dash or space, and the first group can optionally be inside parentheses.
# Hints:
# To match either a dash or space, you can use a pair square brackets.
# Special characters such as parentheses or dash need to be escaped using a backslash, like \( or \).
# Remember, to make a character optional, you can follow it with a question mark.



# TODO 2b: Write a regex for email addresses that consists of alphanumeric characters (or a dot), an "@" symbol, more alphanumeric characters, a dot, and either "com", "net", or "org".
# Hints:
# Alphanumeric characters can be represented with the special character '\w'.
# You can specify one or more instances of the preceding character with the "+" quantifier.
# Since the dot is a special character, you'll need to escape it with a backslash in both cases.
# For the domain endings, you can use parentheses to group them together and a pipe symbol for either-or matching.



# TODO 2c: Write a regex for website addresses, which look like email addresses but do not have the "@" symbol. The website should either start with the beginning of the string, or after another word.
# Hints:
# You can use the caret character to represent the start of string "anchor". For matching a space, you can use the special character "\s".
# Then you can pair these two characters inside a pair of parentheses - separated by a pipe symbol - so that one or the other is matched at the beginning of the match.
# Since you shouldn't include the start anchor/space character as part of the actual website you write to the file, you'll want to enclose the rest of the regex in another group.



# TODO 3: Open and read the provided example file
# Hint: Use a 'with' statement to open the file in read mode. Assign the content of the file to a variable.



# TODO 4: Use the findall method to find all matches for each regular expression in the contents of the file



# TODO 5: Process the matches and append each unique match to its respective list, along with a newline character
# Hints:
# Initialize an empty list for each set of matches.
# Loop through each match produced in 'TODO 4'.
# Add a newline character (\n) to the end of each match, then append it to its corresponding list ONLY if it's not already in the list.
# You can use "not in" to test whether an item is already in the list.
# If the regular expression you pass into 'findall' includes groups, your target match may be nested inside a tuple, inside of a list.



# TODO 6: Write each list of matches to a new text file
# Open a file in write mode, and then use the 'writelines' method to write the list of matches to the file.
