def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values
    
    Returns:
        float: The variance of the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric values
        ValueError: If the input list is empty
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (sum of squared differences from mean divided by n)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return variance