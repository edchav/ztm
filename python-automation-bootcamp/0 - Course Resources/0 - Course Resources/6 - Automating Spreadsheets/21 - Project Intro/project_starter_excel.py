# TODO 1: Import openpyxl.



# TODO 2: Import the Font and numbers classes from openpyxl.styles.
# HINT: Use the `from module import something` syntax to make it more convenient to work with the Font and numbers classes.



# TODO 3: Load the 'Employee Sales.xlsx' workbook.



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
    # HINT: You can access a particular worksheet by passing its name into a pair of square brackets, following the workbook object. E.g., `ws = wb['Sheet1']`.


    # TODO 4f: Access the ranges specified by the user.
    # HINT: You can access a specific range of cells by passing its address (as a string) into a pair of square brackets, following the worksheet object. E.g.,my_range = `ws['A1:Z100']`.


    # TODO 4g: Compare the dimensions of the two ranges and exit (break) the loop if they are the same.
    # HINT: Use the 'len' function to find the number of rows and columns in a range.


    # TODO 4h: If the dimensions of the two ranges are not identical, notify the user and continue the loop.



# TODO 5: Save the headers of the first range to a variable.
# HINT: If you have a list of lists, the first list can be accessed with index 0.



# TODO 6: Create an empty list to store data about the differences between the two target ranges.



# TODO 7: Loop through each row and column of the user-specified ranges (excluding headers) and store the differences in the list you created.
# NOTE: In openpyxl, a range is structured as a tuple of rows, with each row being a tuple of cells.

        # TODO 7a: Create a nested loop that iterates over each row and column of the ranges.
        # HINT: You can use Python's 'range' function to iterate over the rows and columns of range, by feeding it the number of rows in the outer tuple (outer loop), and the number of items in the inner tuples (inner loop).
        # HINT: Remember that in Python, you typically iterate over collections starting at index 0, but in this case, you want to exclude the header row, so start at index 1 for rows.


        # TODO 7b: For each cell in the range, get the corresponding cell from the other range.
        # HINT: To access an item in a nested list/tuple (a list/tuple within a list/tuple), you can use multiple indices. For example, to access the third item in the second list of a nested list, you would write: nested_list[1][2].


        # TODO 7c: Compare the value from the first cell with the value from the second cell. If they are not equal, it means there is a difference.
        # HINT: You can access the cell value by using the .value attribute on a cell object.


        # TODO 7d: If a difference is found, create a new list that includes the row number, column header, and value from the first range, and the non-matching value from the second range. This list represents a single difference.
        # HINT: To create a new list with several items, you can use the list literal syntax like this: [item1, item2, item3, item4].
        # HINT: You can fetch the column header value from the list you created in step 5, using one of the indices inside the loop.


        # TODO 7e: Append this new list (difference) to your main "differences" list. This way, at the end of the loops, the differences list should contain all differences between the two ranges.



# TODO 8: Create a new worksheet named 'Diffs' and store it in a variable.
# HINT: The create_sheet function can be used to create a new worksheet in a workbook.



# TODO 9: Write the differences to the new worksheet starting from cell A2.

    # TODO 9a: Define the cell range where you will write the differences as a text string.
    # HINT: This should be a rectangular area in your 'Diffs' worksheet that starts from cell 'A2' (to skip the header row) and extends down as many rows as the number of differences, and right 4 columns (for 'Row', 'Column', 'Value 1', 'Value 2').


    # TODO 9b: Fetch the range of cells in the cell range you just defined, into an object.
    # HINT: You can translate the text string you defined in step 9a into an actual range of cells, by passing it into a pair of square brackets after the worksheet object. E.g, `cell_range = ws[my_range]`.


    # TODO 9c: Loop over the rows in this range of cells.
    # HINT: Use the 'enumerate' function to track the index of the row in the current iteration of the loop.


    # TODO 9d: For each row, loop over the cells inside the row.
    # HINT: Remember that you can nest loops. Here, the outer loop is over the rows and the inner loop is over the cells in each row.
    # HINT: Again, use the 'enumerate' function to track the index of the row in the current iteration of the loop.


    # TODO 9e: Write the corresponding difference to each cell.
    # HINT: The differences are stored in the differences list of lists you created in step 7, and each difference is a list with 4 elements.
    # HINT: The dimensions of the differences list of lists, and the cell range you just accessed, should be the same.
    # HINT: This means you should be able to use the very same indices you're tracking inside the loop, to access a particular value from the differences list if lists, and then write it to the corresponding cell in the target range.



# TODO 10: Write headers to the new worksheet.

    # TODO 10a: Define the header row. This is the first row of your 'Diffs' worksheet, i.e., 'A1:E1'.


    # TODO 10b: Define your header labels in a list. These will be the strings: 'Row', 'Column', 'Value 1', 'Value 2', 'Delta'.


    # TODO 10c: Loop over the cells in the header row, writing the corresponding values from your header labels list to those cells.
    # HINT: This works just like writing the differences list of lists to a range of cells - as you did in step 9 - but slightly simpler (1D vs 2D).
    # HINT: Remember that even in a 1D range of cells, the single cell value per each row will still be contained within a tuple. As such, you'll have to index into the tuple to extract the value.



# TODO 11: Write formulas to calculate the percentage difference between Value 1 and Value 2 for each row where both are numbers.
# HINT: You can write a formula to a cell with cell.value = '=FORMULA'

    # TODO 11a: Define the range for the formulas. This is a column range in your 'Diffs' worksheet where you will write the percentage differences. The range starts from cell 'E2' (to skip the header) and extends down as many rows as the number of differences.
    # HINT: You can generate a cell address by concatenating the column letter ('E') with the row number as a string.
    # HINT: Remember to use str() function to convert the row number to a string before concatenation. For example: 'E' + str(row_number).


    # TODO 11b: Loop over the rows in your formula range.


    # TODO 11c: For each row, get the current row number (you'll use this to reference other cells in the same row). Note that the row number here should correspond to the row number in Excel you're writing the formula to.
    # HINT: The 'enumerate' function can be used in the for loop to get both the index and the value.
    # HINT: You will need to modify the index generated by 'enumerate' to derive the corresponding row number in the worksheet.


    # TODO 11d: Generate the addresses of the cells that contain the two values you're comparing. These are in the 'C' and 'D' columns of the current row.
    # HINT: Again, you can generate a cell address by concatenating the column letter with the row number as a string. For example: 'C' + str(row_number).


    # TODO 11e: Test whether BOTH cells have either 'int' or 'float' datatypes. IF so, steps 11f through 11h should also be completed.
    # HINT: You can use the following code to test if a value is either an 'int' or a 'float': `if type(value) in (int, float)`


    # TODO 11e: Write the formula to calculate the absolute percentage difference into the first cell of the current row. This formula will use the ABS and AVERAGE Excel functions.
    # HINT: Construct the formula via string concatenation, in the same way that you dynamically constructed cell and range addresses previously.
    # HINT: The Excel formula for the absolute difference between two values is `=ABS(val1 - val2)/AVERAGE(val1, val2)`
    # HINT: Remember to include the '=' sign as part of your formula string.


    # TODO 11f: Write the formula to the corresponding cell of the formula range you defined.
    # HINT: Since you're writing data to a 1D range of cells, this should work much like when you wrote your list of header labels to the first row of the new worksheet.


    # TODO 11g: Format the cell with the formula to have a red font color and a percentage number format.
    # HINT: The 'styles' module of the openpyxl library provides Font and numbers classes for this purpose.
    # HINT: The hex value for the color red is 'FF0000'.
    # HINT: You can format the value in a cell as a percentage using the 'numbers' class, as follows: `cell.number_format = numbers.FORMAT_PERCENTAGE`.



# TODO 12: Save the workbook

