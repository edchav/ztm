# TODO 1: Import the gspread library



# TODO 2: Authenticate to the Google Sheets API using a service account



# TODO 3: Open the target spreadsheet using the gspread client
# HINT: Make sure you share the spreadsheet to your service account's email address



# TODO 4: Start a while loop in which you will prompt users to specify the target worksheets and ranges, until the two ranges have the same number of rows and columns.
# HINT: Use "while True:" to start an infinite loop. Make sure to include a break condition in the loop.

    # TODO 4a: Ask the user to enter the name of the worksheet where the first target range is located.
    # HINT: Use the 'input' function to get user input.


    # TODO 4b: Ask the user to enter the the address (in 'A1:B2' format) of the target range on the first worksheet.
    # HINT: Use the 'input' function to get user input.


    # TODO 4c: Ask the user to enter the name of the worksheet where the second target range is located.
    # HINT: Use the 'input' function to get user input


    # TODO 4d: Ask the user to enter the the address (in 'A1:B2' format) of the target range on the second worksheet.
    # HINT: Use the 'input' function to get user input.


    # TODO 4e: Access the worksheets specified by the user.
    # HINT: Use the 'worksheet' method of the spreadsheet object to target a particular worksheet. E.g., `ws = spreadsheet.worksheet('Sheet1')`.


    # TODO 4f: Access the ranges specified by the user.
    # HINT: Use the 'get' method of the worksheet object to fetch a range of cells in a specified range on a worksheet into a list of lists. E.g., `my_range = ws.get('A1:Z100')`.


    # TODO 4g: Compare the dimensions of the two ranges and exit (break) the loop if they are the same.
    # HINT: Use the 'len' function to find the number of rows and columns in a range.


    # TODO 4h: If the dimensions of the two ranges are not identical, notify the user and continue the loop.



# TODO 5: Save the headers of the first range to a variable.
# HINT: If you have a list of lists, the first list can be accessed with index 0.



# TODO 6: Create an empty list to store data about the differences between the two target ranges.



# TODO 7: Loop through each row and column of the ranges (excluding headers) and store the differences in the list you created.

    # TODO 7a: Create a nested loop that iterates over each row and column of the ranges.
    # HINT: You can use Python's 'range' function to iterate over the rows and columns of each list of lists, by feeding it the number of rows in the outer list (outer loop), and the number of items in the inner lists (inner loop).
    # HINT: Remember that in Python, you typically iterate over collections starting at index 0, but in this case, you want to exclude the header row, so start at index 1 for rows.


    # TODO 7b: For each cycle of the inner loop, fetch the corresponding values from the two ranges.
    # HINT: Remember, the "ranges" are represented as lists of lists, that also have the same number of rows and columns.
    # HINT: To access an item in a nested list/tuple (a list/tuple within a list/tuple), you can use multiple indices. For example, to access the third item in the second list of a nested list, you would write: nested_list[1][2].


    # TODO 7c: Compare the value from the first range with the corresponding value from the second range. If they are not equal, it means there is a difference.


    # TODO 7d: If the values are not equal, check if each cell value is a numeric value.
    # HINT: Use the 'isnumeric' method on the values. Remember that the 'get' method transforms all values into strings, so the values need to be converted to numbers before you can do arithmetic with them.


    # TODO 7e: If either value is numeric, convert it to an float.
    # HINT: Use the 'float' function to convert the string to an integer.


    # TODO 7f: If a difference was found in step 7c, create a new list that includes the row number, column header, and value from the first range, and the non-matching value from the second range. This list represents a single difference.
    # HINT: To create a new list containing several items, you can use the list literal syntax like this: [item1, item2, item3, item4].
    # HINT: You can fetch the column header value from the list you created in step 5, using one of the indices inside the loop.


    # TODO 7g: Append this new list (difference) to your main differences list. This way, at the end of the loops, the differences list should contain all differences between the two ranges.



# TODO 8: Create a new worksheet named 'Diffs' and store it in a variable.
# HINT: The 'add_worksheet' method on the spreadsheet object can be used to create a new worksheet.



# TODO 9: Use the 'update' method to write headers to cells A1:E1 of the new worksheet. Your header values should be 'Row', 'Column', 'Value 1', 'Value 2', and 'Delta'.
# HINT: Remember that when you're using the 'update' method to write multiple values to a range of cells, you need to pass it a list of lists as its second argument (even if your data is only 1-dimensional).



# TODO 10: Write the differences to the new worksheet starting from cell A2.

    # TODO 10a: Define the cell range where you will write the differences as a text string.
    # HINT: This should be a rectangular area in your 'Diffs' worksheet that starts from cell 'A2' (to skip the header row) and extends down as many rows as the number of differences, and right 4 columns (for 'Row', 'Column', 'Value 1', 'Value 2').
    # HINT: You can use text concatenation to construct this text string dynamically; remember, your target range has the same number of rows as your "differences" list of lists does!


    # TODO 10b: Use the 'update' method to write your "differences" list of lists to the range of cells you just defined.



# TODO 11: Write formulas to calculate the percentage difference between Value 1 and Value 2 for each row where both are numbers.
# HINT: You can write a formula to a cell with cell.value = '=FORMULA'.

    # TODO 11a: Create a blank list to hold your formula strings.


    # TODO 11b: Loop over the rows in your "differences" list of lists. For each row, capture the corresponding row number of the worksheet you'll be writing formulas to, in a variable.
    # HINT: The 'enumerate' function can be used in the for loop to get both the index and the value.
    # HINT: You will need to modify the index generated by 'enumerate' to derive the corresponding row number in the worksheet.


    # TODO 11c: Test whether BOTH of the cell values in a given row of your "differences" list of lists (the 3rd and 4th values in each list) have 'float' datatypes. IF so, steps 11d through 11f should also be completed.
    # HINT: You can use the following code to test if a value is either a 'float': `if type(value) == float`.


    # TODO 11d: Generate the addresses of the cells that contain the two values you're comparing. These are in the 'C' and 'D' columns of the current row.
    # HINT: You can dynamically generate a cell address by concatenating the column letter with the row number as a string. For example: 'C' + str(row_number).


    # TODO 11e: Write the formula to calculate the absolute percentage difference into the first cell of the current row. This formula will use the ABS and AVERAGE Google Sheets functions.
    # HINT: Construct the formula via string concatenation, in the same way that you dynamically constructed cell and range addresses previously.
    # HINT: The Google Sheets formula for the absolute difference between two values is `=ABS(val1 - val2)/AVERAGE(val1, val2)`
    # HINT: Remember to include the '=' sign as part of your formula string.


    # TODO 11f: Enclose the formula string within a list (as the list's only item), then append this list to the "formulas" list you created in step 11a.
    # NOTE: We'll be using the 'update' method to write the "formulas" list to a range of cells, so that list needs to be structured as a list of lists (even though it's a single column of data).


    # TODO 11g: If the two values you tested in step 11e were NOT both floats, simply append an empty list to your "formulas" list of lists.


    # TODO 11h: Define the range that the formulas will be written to. This is a column range in your 'Diffs' worksheet where you will write the percentage differences. The range starts from cell 'E2' (to skip the header) and extends down as many rows as the number of differences.
    # HINT: Again, you can generate a cell address by concatenating the column letter ('E') with the row number as a string.
    # HINT: Remember to use str() function to convert the row number to a string before concatenation. For example: 'E' + str(row_number).


    # TODO 11i: Write list of lists containing your formula strings to the range you defined in the previous step.
    # HINT: Use the 'update' method, passing in 'raw=False' as an optional third argument (so your text strings are written as actual formulas, and not simple values).


    # TODO 11j: Format the cells in the formula range to have a red font color and a percentage number format.
    # HINT: Use the 'format' method on the worksheet object to do this.
    # HINT: Below is a dictionary you can pass to the 'format' method to define the required styles:

    {
        "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 0.0,
                "blue": 0.0
            }
        },
        "numberFormat": {
            "type": "PERCENT"
        }
    }



