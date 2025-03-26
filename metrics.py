def average(data: list) -> float:
       if not data:
        return 0.0
''' Find the average of the list.
total_sum = all items in the list added together
count = number of items in the list
returns the average of the list rounded to 2 decimal points'''
data:list = [1, 2, 3, 4, 5]
total_sum = 0
count = 0
for num in data:
    total_sum += num
    count += 1
    
avg = total_sum / count
return round(avg, 2)


def find_maximum(data: list) -> float:
    """
    Find the maximum value in the list.

    data (list[int]): list of integers representing heart rate samples
    float: the maximum value in the list as a float
    returns the maximum of the list rounded to 2 decimal points
    """
    if not data:
        return 0.0
    
    max_value = data[0]  
    for number in data:
        if number > max_value:
            max_value = number
    
    return round(max_value, 2)
    

def variance(data: list) -> float:
    """
    Calculate the population variance of the list, rounded to 2 decimal points.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: the population variance rounded to 2 decimal places
    """
    if not data:
        return 0.0
    mean = sum(data) / len(data)
    var = sum((x - mean) ** 2 for x in data) / len(data)
    return round(var, 2)

def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    if not data:
        return 0.0
    return round(variance(data))
# Example usage:
heart_rates = []
print(standard_deviation(heart_rates))
