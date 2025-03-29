def filter_nondigits(data: list) -> list:
    '''
    this function filters out all non-digits and empty data from the input list and returns a new list with only digits, 
    converting them to integers
    '''
    filtered_data = []
    for i in data:
        j = i.strip() # removes empty spaces
        if j.isdigit(): # filters digits
                filtered_data.append(int(j)) # adds filtered digits to a new list, converts them to integers
    return filtered_data
