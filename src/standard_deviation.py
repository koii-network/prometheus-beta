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
    
    # Validate input is numeric
    try:
        # Ensure all elements can be converted to float
        numeric_numbers = []
        for num in numbers:
            # Try to convert each element, raising TypeError if not possible
            converted = float(num)
            numeric_numbers.append(converted)
        
        # If we get here, all elements are numeric
        numbers = numeric_numbers
    except (TypeError, ValueError):
        raise TypeError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (average of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    # Return square root of variance (standard deviation)
    return math.sqrt(variance)