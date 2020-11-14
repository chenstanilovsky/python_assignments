def check_valid_row(row):
    # If row is more than 1 character, it cannot be valid
    if len(row) != 1:
        return False

    # If the ascii value of the row is within ('1' = 48 to '8' = 56)
    # then it is valid, otherwise false
    if ord(row) >= 49 and ord(row) <= 56:
        return True

    return False
    

def check_valid_column(column):
    # If column is more than 1 character, it cannot be valid
    if len(column) != 1:
        return False

    # if the ascii value of column is within ('A' = 65 to 'H' = 72)
    # then it is valid, otherwise false
    if(ord(column) >= 65 and ord(column) <= 72):
        return True

    return False
