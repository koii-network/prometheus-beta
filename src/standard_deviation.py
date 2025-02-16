import math

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        float: The standard deviation of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric values.
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Check for numeric values
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the sum of squared differences
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    
    # Calculate variance and then standard deviation
    variance = squared_diff_sum / len(numbers)
    standard_dev = math.sqrt(variance)
    
    return standard_dev