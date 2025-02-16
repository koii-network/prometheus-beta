def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        float: The median value of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric values.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Validate that all elements are numeric
    try:
        numeric_list = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_nums = sorted(numeric_list)
    length = len(sorted_nums)
    
    # Calculate median
    if length % 2 == 0:
        # If even number of elements, average the two middle values
        mid = length // 2
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    else:
        # If odd number of elements, return the middle value
        return sorted_nums[length // 2]