# TODO 1: Import the necessary modules and functions
    # TODO 1a: Import the `dotenv` module to load environment variables from a '.env' file.

    # TODO 1b: Import the `OpenAI` class from the 'openai' module to interact with OpenAI's GPT-3.5 model.


# TODO 2: Load environment variables
    # TODO 2a: Load the environment variables from a '.env' file using the 'dotenv_values' function.

    # TODO 2b: Assign the loaded variables to a dictionary named 'env_vars'.


# TODO 3: Initialize an instance of the OpenAI client, passing in the API key obtained from the 'env_vars' dictionary as an argument.


# TODO 4: Define the initial user prompt
    # TODO 4a: Request input from the user to ask a question to "Bruno", the virtual manager.

    # TODO 4b: Concatenate a string to the user's response - before it is sent to the API - specifying that the response should be limited to a single paragraph.


# TODO 5: Define the conversation setup
    # TODO 5a: Define a list named 'messages' containing two dictionaries representing the roles and contents of the initial conversation.
    # Hint: The first dictionary should represent the 'system' role, describing Bruno's character.
    # Hint: The second dictionary should contain the 'user' role with the user's initial prompt.


# TODO 6: Implement the conversation loop
    # TODO 6a: Create an infinite loop to handle the conversation.

    # TODO 6b: Inside the loop, use the 'chat.completions.create' method of the OpenAI client to generate responses.
    # Hint: You should be able to get the code for the `chat.completions.create` method call from the OpenAI playground.


# TODO 7: Process and print the API's response
    # TODO 7a: Retrieve the response from the OpenAI API's output and store it in a variable.
    # Hint: The code to do this follows the format `response.choices[0].message.content`

    # TODO 7b: Print the API's response.


# TODO 8: Append a new dictionary to the 'messages' list, with the 'assistant' role and the API's response as content.


# TODO 9: Prompt the user to respond to Bruno, OR to type "thanks" to exit the conversation loop.


# TODO 10: IF the user's reply is 'thanks', break out of the conversation loop.


# TODO 11: If the loop does not break, append the user's reply to the 'messages' list, with the 'user' role.
# Hint: Ensure to use the correct variable for the user's reply in the appended dictionary.
