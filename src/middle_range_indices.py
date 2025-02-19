def find_middle_range_indices(sorted_list, range_width):
    """
    Find indices of elements within a given range of the middle value in a sorted list.
    
    Args:
        sorted_list (list): A sorted list of integers
        range_width (int): The width of the range around the middle value
    
    Returns:
        list: Indices of elements within the specified range of the middle value
    
    Raises:
        ValueError: If range_width is negative or list is empty
    """
    if not sorted_list:
        raise ValueError("Cannot find middle range in an empty list")
    
    if range_width < 0:
        raise ValueError("Range width must be non-negative")
    
    # Calculate the middle index
    mid_index = len(sorted_list) // 2
    mid_value = sorted_list[mid_index]
    
    # Find the range of indices
    indices = []
    for i, value in enumerate(sorted_list):
        if abs(value - mid_value) <= range_width:
            indices.append(i)
    
    return indices