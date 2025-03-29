def average(data: list) -> float:
    if not data: #checks if the value is empty
        return []
    ''' Find the average of the list.
    total_sum = all items in the list added together
    count = number of items in the list
    returns the average of the list rounded to 2 decimal points'''
    total_sum = 0
    count = 0
    for num in data:
        total_sum += num
        count += 1
    
    avg = total_sum / count
    return round(avg, 2)


def maximum(data: list) -> int:
    """
    Find the maximum value in the list.
    int: the maximum value in the list as a integer.
    returns the maximum of the list as an integer.
    """
    if not data: #checks if the value is empty
        return []
    
    max_value = 0  
    for number in data:
        if number > max_value:
            max_value = number #if the number is greater than the max_value, the number becomes the new max_value
    
    return max_value
    

def variance(data: list) -> float:
    """
    Calculate the variance of the list.
    Returns: float, the variance rounded to 2 decimal points.
    """
    if not data:
        return []
    mean = sum(data) / len(data)
    var = sum((x - mean) ** 2 for x in data) / len(data)
    return round(var, 2)

def standard_deviation(data: list) -> float:
    """
    Calculate standard deviation.  
    Returns: float, the variance rounded to 2 decimal points.
    """
    if not data:
        return []
    return round((variance(data)) ** 0.5, 2)
