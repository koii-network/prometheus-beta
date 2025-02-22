def find_mid_range_indices(sorted_list, range_value):
    """
    Find indices of elements within a given range of the middle value in a sorted list.
    
    Args:
        sorted_list (list): A sorted list of integers
        range_value (int): The range around the middle value to find indices for
    
    Returns:
        list: Indices of elements within the specified range of the middle value
    
    Raises:
        ValueError: If the input list is empty
    """
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the middle index
    mid_index = len(sorted_list) // 2
    mid_value = sorted_list[mid_index]
    
    # Find indices within the range
    result_indices = []
    for i, num in enumerate(sorted_list):
        if abs(num - mid_value) <= range_value:
            result_indices.append(i)
    
    return result_indices