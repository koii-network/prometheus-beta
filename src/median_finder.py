def find_median(numbers):
    """
    Find the median of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The median value of the input list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric values.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All list elements must be numeric")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    # Calculate median
    if length % 2 == 0:
        # Even number of elements: average of two middle values
        mid = length // 2
        return (sorted_numbers[mid-1] + sorted_numbers[mid]) / 2
    else:
        # Odd number of elements: middle value
        return sorted_numbers[length // 2]