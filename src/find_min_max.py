def find_min_max(numbers):
    """
    Find the highest and lowest numbers in an input array.
    
    Args:
        numbers (list): A list of numbers to analyze
    
    Returns:
        tuple: A tuple containing (lowest_number, highest_number)
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If the list contains non-numeric elements
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    try:
        lowest = min(numbers)
        highest = max(numbers)
        return (lowest, highest)
    except TypeError:
        raise TypeError("All elements in the list must be numeric")