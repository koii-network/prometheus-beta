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
        TypeError: If the list contains non-numeric elements.
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the sum of squared differences
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    
    # Calculate variance
    variance = squared_diff_sum / len(numbers)
    
    # Return standard deviation (square root of variance)
    return math.sqrt(variance)