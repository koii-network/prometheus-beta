def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to calculate the average of.
    
    Returns:
        float: The average of the numbers.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    return sum(numbers) / len(numbers)