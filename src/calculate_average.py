def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values
    
    Returns:
        float: The average of the input numbers
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If the list contains non-numeric values
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate and return the average
    return sum(numbers) / len(numbers)