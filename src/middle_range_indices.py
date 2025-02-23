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
    list_length = len(sorted_list)
    mid_index = list_length // 2
    
    # Adjust for even and odd number of elements
    if list_length % 2 == 0:
        # For even length, choose the lower middle index
        mid_index -= 1
    
    # Calculate the range of indices to return
    start_index = max(0, mid_index - range_radius)
    end_index = min(list_length - 1, mid_index + range_radius)
    
    # Return the indices within the specified range
    return list(range(start_index, end_index + 1))