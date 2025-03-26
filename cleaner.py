def filter_nondigits(data: list) -> list:
    '''
    this function filters out all non-digits from the input list and returns a new list with only digits
    '''
    filtered_data = []
    for i in data:
        if i.isdigit():
            filtered_data.append(int(i))
    return filtered_data