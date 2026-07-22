# TODO 1: Import the necessary libraries
# Hint: You will need the 'requests' library to make HTTP requests and the 'html' library to unescape HTML entities. Also, import the 'csv' library to write to a CSV file.


# TODO 2: Prompt the user to enter the number of trivia questions they'd like to see
# Hint: Use the 'input' function and store the result in a variable.


# TODO 3: Prompt the user to specify the difficulty of the questions (easy/medium/hard)
# Hint: Use the 'input' function again and store this result in another variable.


# TODO 4: Define the API endpoint in a variable
# Hint: The API URL is 'https://opentdb.com/api.php'.


# TODO 5: Set up the request parameters in another variable
# Hint: Define a dictionary for the parameters with keys for 'amount', 'difficulty', and 'category'. The 'category' value should be set to "18" for technology.


# TODO 6: Make a GET request to the trivia API using the requests library
# Hint: Use the 'get' method of the 'requests' library. Pass in the API URL, request headers accepting JSON, and the parameters dictionary.


# TODO 7: Parse the JSON response and extract the trivia data
# Hint: Use the 'json' method of the response object to get the data. Focus on the 'results' key.


# TODO 8: Initialize a list to hold question and answer pairs
# Hint: Start with a header row with 'Question' and 'Answer'.


# TODO 9: Loop through the trivia data and process each question
# Hint: For each item in the data, unescape the HTML entities in the question and answer using 'html.unescape'.
# If the question type is 'boolean', prepend "True or False? " to the question.


# TODO 10: Append each question and its correct answer to the list as a new row
# Hint: Create a sublist for each question and answer pair, then append it to your main list.


# TODO 11: Write the question and answer pairs to a CSV file named "tech trivia.csv"
# Hint: Open the file in write mode with 'newline' set to an empty string.
# Use the 'writer' method of the 'csv' library to create a CSV writer object.
# Write the rows to the file using 'writerows'.
