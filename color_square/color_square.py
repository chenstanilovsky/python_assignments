import InputCheck as ic

def print_color(row, column):
    # if the row is invalid
    if not ic.check_valid_row(row):
        print("Invalid row entry")
        return

    # if the column is invalid
    if not ic.check_valid_column(column):
        print("Invalid column entry")
        return
    # How does this part work?
    # For the rows we get numbers 1-8
    # For the columns we get letters which coorespond with numbers 1-8

    # when the row and column number are the same parity (both even or both odd) the square is black
    # when the row and column number are opposite parity (one even one odd) the square is white

    # The lowest valid column is 'A', its ascii value which we get with ord('A') is 65
    # 65 is odd meaning the first column's ascii value has the same parity as the number one
    # as we increase the ascii value, we get the same pattern: 65 odd, 66 even, 67 odd, 68 even
    # as we would if we started counting from 1: 1 odd, 2 even, 3 odd, 4 even, ....

    # Taking ord(column) % 2 determines if it is odd or even
    # If both row and column's ascii are odd, then the square is black
    # If they have opposite parity the square is white

    if(ord(column) % 2 == int(row) % 2):
        print("The square at {}{} is Black".format(column, row))
    else:
        print("The square at {}{} is White".format(column, row))


def main():
    # Read in column and covert to uppercase for consistency
    print("Please enter a column (a-h)")
    column = input("> ")
    column = column.upper()

    # Read in row
    print("Please enter a row (1-8)")
    row = input("> ")

    print_color(row, column)

if __name__ == "__main__":
    main()





