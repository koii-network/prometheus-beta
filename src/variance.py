def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values
    
    Returns:
        float: The variance of the input list
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All list elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (sum of squared differences from mean divided by list length)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return variance