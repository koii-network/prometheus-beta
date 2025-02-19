def find_middle_range_indices(sorted_list, range_percentage=0.2):
    """
    Find indices of elements within a range of the middle value in a sorted list.
    
    Args:
        sorted_list (list): A sorted list of integers
        range_percentage (float, optional): Percentage of range around middle value. Defaults to 0.2.
    
    Returns:
        list: Indices of elements within the specified range of the middle value
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If inputs are not of the correct type
    """
    # Input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    if not isinstance(range_percentage, (int, float)) or range_percentage < 0 or range_percentage > 1:
        raise ValueError("Range percentage must be a float between 0 and 1")
    
    # Find the middle value
    n = len(sorted_list)
    mid_index = n // 2
    mid_value = sorted_list[mid_index]
    
    # Calculate range boundaries
    half_range = mid_value * range_percentage
    lower_bound = mid_value - half_range
    upper_bound = mid_value + half_range
    
    # Find indices within the range
    range_indices = [
        index for index, value in enumerate(sorted_list) 
        if lower_bound <= value <= upper_bound
    ]
    
    return range_indices