# TODO: Import necessary libraries
# HINT: You'll need 'pathlib' for handling paths and 'shutil' for high-level file operations


# TODO: Ask the user to specify a directory
# HINT: Use the input() function to get user input and convert it to a Path object


# TODO: Create a new directory within that directory, called "closet"
# HINT: You can create a new Path object by appending to an existing one, and use the mkdir() method to create the directory


# TODO: Create three sub-directories within closet: text_files, csv_files, and folders
# HINT: Similar to the previous step, create new Path objects and directories


# TODO: Start iterating over all the files and folders in the user-specified directory
# HINT: Use the iterdir() method of your Path object to get an iterator of all items in the directory


# TODO: Implement checks inside the loop to handle different items differently
# IMPORTANT: Sequence your if/elif/else conditions strategically. More specific conditions should come first so they aren't absorbed into more general conditions.
# HINT: You can use the is_file() and is_dir() methods to check if an item is a file or a directory


# TODO: Test whether an item being iterated over is the "closet" directory, to keep "closet" from being moved into itself
# HINT: If this condition is met, you can use the "continue" keyword to skip to the next iteration of the loop


# TODO: Move all the plaintext files (.txt) within the user-specified directory into the "text_files" sub-directory of closet
# HINT: Check the suffix of files using the suffix attribute of the Path object. Use shutil.move() to move files.


# TODO: Similarly, move all the csv files within the user-specified directory into the "csv_files" sub-directory of closet


# TODO: Delete any directories within the user-specified directory with the word "temp" as part of the name
# IMPORTANT: This condition should come before checking if an item is a directory at all. This way, 'temp' directories will be handled first and won't be moved.
# HINT: You can check if "temp" is in the name of a directory with the 'in' keyword. Use shutil.rmtree() to remove directories.


# TODO: Move all the remaining directories within the user-specified directory into the "folders" sub-directory of closet


# TODO: Move all the remaining files within the user-specified directory into closet


# TODO: Print feedback to the user, letting them know when the script is done