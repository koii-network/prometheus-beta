def find_middle_range_indices(sorted_list, range_radius=1):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        range_radius (int, optional): Number of elements to include on each side of the middle. 
                                      Defaults to 1.

    Returns:
        list: Indices of elements within the specified range of the middle value.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If inputs are not of the expected type.
    """
    # Validate inputs
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    if not isinstance(range_radius, int) or range_radius < 0:
        raise TypeError("Range radius must be a non-negative integer")
    
    # Determine the middle index
    mid_index = len(sorted_list) // 2
    
    # Calculate the range of indices to return
    start_index = max(0, mid_index - range_radius)
    end_index = min(len(sorted_list) - 1, mid_index + range_radius)
    
    # Return the indices within the specified range
    return list(range(start_index, end_index + 1))