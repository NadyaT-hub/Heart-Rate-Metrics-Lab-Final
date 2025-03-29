def filter_nondigits(data: list) -> list:
    '''
    this function filters out all non-digits and empty data from the input list and returns a new list with only digits, 
    converting them to integers
    '''
    filtered_data = []
    for i in data:
        j = i.strip()
        if j.isdigit():
                filtered_data.append(int(j))
    return filtered_data
