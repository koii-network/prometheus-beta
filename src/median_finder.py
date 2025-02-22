def find_median(numbers):
    """
    Find the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        float: The median value of the input list
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If the input is not a list or contains non-numeric elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Check if all elements are numbers
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Find the middle index
    mid = len(sorted_numbers) // 2
    
    # If list length is odd, return middle element
    if len(sorted_numbers) % 2 != 0:
        return float(sorted_numbers[mid])
    
    # If list length is even, return average of two middle elements
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0