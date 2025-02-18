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
    
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("List must contain only numeric elements")
    
    # Sort the list
    sorted_nums = sorted(numbers)
    
    # Find the median
    length = len(sorted_nums)
    mid = length // 2
    
    # If the list has an odd number of elements, return the middle element
    if length % 2 != 0:
        return float(sorted_nums[mid])
    
    # If the list has an even number of elements, return the average of the two middle elements
    return (sorted_nums[mid-1] + sorted_nums[mid]) / 2.0