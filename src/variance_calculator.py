import math

def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        float: The variance of the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list is empty.
    """
    # Type checking
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(numbers) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Check for numeric values
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All list elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (average of squared differences from the mean)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return variance