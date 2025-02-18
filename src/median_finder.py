def find_median(numbers):
    """
    Find the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The median of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    # Calculate median
    if length % 2 == 0:
        # Even number of elements, take average of two middle numbers
        mid = length // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # Odd number of elements, take middle number
        return sorted_numbers[length // 2]