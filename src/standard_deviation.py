import math

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to calculate standard deviation for.
    
    Returns:
        float: The standard deviation of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric values.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Validate input is numeric
    try:
        numbers = [float(x) for x in numbers]
    except (TypeError, ValueError):
        raise TypeError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (average of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    # Return square root of variance (standard deviation)
    return math.sqrt(variance)