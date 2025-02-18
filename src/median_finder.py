def find_median(numbers):
    """
    Find the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The median value of the list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Cannot find median of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All list elements must be numeric")
    
    # Sort the list
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    
    # Calculate median
    if length % 2 == 0:
        # Even number of elements: average of two middle numbers
        mid_right = length // 2
        mid_left = mid_right - 1
        return (sorted_nums[mid_left] + sorted_nums[mid_right]) / 2
    else:
        # Odd number of elements: middle number
        return sorted_nums[length // 2]