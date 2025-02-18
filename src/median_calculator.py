def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The median value of the list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    # Calculate median
    if length % 2 == 0:
        # If even number of elements, average the two middle numbers
        mid = length // 2
        return (sorted_numbers[mid-1] + sorted_numbers[mid]) / 2
    else:
        # If odd number of elements, return the middle number
        return sorted_numbers[length // 2]