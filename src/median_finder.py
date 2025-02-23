def find_median(numbers):
    """
    Find the median of a list of numbers.

    Args:
        numbers (list): A list of numbers to find the median of.

    Returns:
        float: The median value of the input list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_nums = sorted(numbers)
    
    # Find the median
    n = len(sorted_nums)
    mid = n // 2
    
    # If list length is odd, return middle element
    if n % 2 != 0:
        return float(sorted_nums[mid])
    
    # If list length is even, return average of two middle elements
    return (sorted_nums[mid-1] + sorted_nums[mid]) / 2.0