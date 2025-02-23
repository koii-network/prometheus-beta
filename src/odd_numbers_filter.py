def filter_odd_numbers(numbers):
    """
    Returns a list containing only the odd numbers from the input array.

    Args:
        numbers (list): An input list of numbers to filter.

    Returns:
        list: A new list containing only the odd numbers from the input list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Filter and return only odd numbers
    return [num for num in numbers if isinstance(num, int) and num % 2 != 0]