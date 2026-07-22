# TODO 1: Import the necessary libraries (csv, datetime)


# TODO 2: Define the product_data dictionary with product IDs, names, and unit prices


# TODO 3: Read the "product_sales.txt" file and store the product IDs in a list
# Hint: Use the built-in 'open' function to open the file, and the 'readlines' method to read its lines into a list.


# TODO 4: Loop through the list of product IDs
# Hint: A 'for' loop can be used to iterate over the list.


# TODO 5: Append lists containing the data points for each product ID to a "list of lists" outside the loop
    # TODO 5.1: Create a current_date variable outside the loop and set it equal to today's date
    # Hint: Use the 'datetime.date.today()' from the 'datetime' library to get the current date.


    # TODO 5.2: Create a counter variable outside the loop, and set it to 1


    # TODO 5.3: Strip the newline characters off the end of the product IDs, and fetch them into their own variable
    # Hint: The 'strip' method can be used to remove newline characters.


    # TODO 5.4: Fetch product name and unit price from the product_data dictionary, and assign those values to variables inside the loop


    # TODO 5.5: Create a list consisting of the current date, sale ID, product ID, product name, and unit price


    # TODO 5.6: Create another list outside the loop


    # TODO 5.7: Append the list inside the loop containing the data points we just compiled, to the "list of lists" outside the loop


    # TODO 5.8: Increment the counter variable, so it increases by 1 for every iteration of the loop


# TODO 6: Write the sales data (the list of lists) to a new CSV file called "product_sales.csv"
    # TODO 6.1: Open the CSV file in write mode
    # Hint: Use the 'open' function with the mode parameter set to 'w', and the newline parameter set to an empty string.


    # TODO 6.2: Create a CSV writer object
    # Hint: Use the 'writer' method of the 'csv' library.


    # TODO 6.3: Write appropriate headers to the CSV file
    # Hint: The 'writerow' method of the CSV writer can be used to write a row to the CSV file.


    # TODO 6.5: Write the sales data (i.e., the list of lists) to the CSV file
    # Hint: The 'writerows' method of the CSV writer can be used to write multiple rows to the CSV file at one time.
