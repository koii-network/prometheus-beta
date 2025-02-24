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
        TypeError: If the list contains non-numeric values.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the variance (average of squared differences from the mean)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    # Return the square root of the variance (standard deviation)
    return math.sqrt(variance)