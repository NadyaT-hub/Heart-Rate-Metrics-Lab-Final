def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    if not data:  # Check to avoid division by zero
        return 0.0
    return round(sum(data) / len(data),2)

heart_rates = []
print(average(heart_rates))  


def maximum(data: list) -> float:
    """
    Find the maximum value in the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: the maximum value in the list as a float
    """
    if not data:
        return 0.0  # or you could raise an exception if preferred
    return round(float(max(data)), 2)
# Example usage:
heart_rates = []
print(maximum(heart_rates))
    

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
