# Create a variable to track the row number
row = 1

# Loop for nine rows
while row < 10:

    # Create a variable to track the column number that resets for each row
    column = 1

    # Create a blank string variable
    string = ""

    # Loop for each number in the row
    while column <= row:

        # Add the next number onto the row
        string += str(column)

        # Go to the next column
        column += 1

    # Print the full row
    print(string)

    # Go to the next row
    row += 1
