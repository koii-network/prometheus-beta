def find_middle_range_indices(sorted_list, range_width):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        range_width (int): The number of indices to include on each side of the middle.

    Returns:
        list: Indices of elements within the specified range of the middle value.

    Raises:
        ValueError: If range_width is negative or the list is empty.
        TypeError: If inputs are not of the expected type.
    """
    # Validate inputs
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_width, int):
        raise TypeError("Range width must be an integer")
    
    if range_width < 0:
        raise ValueError("Range width cannot be negative")
    
    # Handle empty list
    if not sorted_list:
        return []
    
    # Calculate the middle index
    middle_index = len(sorted_list) // 2
    
    # Calculate the start and end of the range
    start_index = max(0, middle_index - range_width)
    end_index = min(len(sorted_list) - 1, middle_index + range_width)
    
    # Return indices within the range
    return list(range(start_index, end_index + 1))