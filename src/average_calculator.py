def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to calculate the average for.
    
    Returns:
        float: The average of the numbers.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric elements.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError("All elements must be numeric")