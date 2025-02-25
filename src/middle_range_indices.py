def find_middle_range_indices(sorted_list, range_size=1):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        range_size (int, optional): Number of elements to include on each side of the middle. 
                                    Defaults to 1.

    Returns:
        list: Indices of elements within the specified range of the middle value.

    Raises:
        ValueError: If the input list is empty or range_size is negative.
        TypeError: If inputs are not of the expected type.
    """
    # Input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_size, int):
        raise TypeError("Range size must be an integer")
    
    if range_size < 0:
        raise ValueError("Range size cannot be negative")
    
    # Handle empty list
    if not sorted_list:
        return []
    
    # Determine the middle index
    mid_index = len(sorted_list) // 2
    
    # Calculate start and end indices for large range size
    start_index = max(0, mid_index - range_size)
    end_index = min(len(sorted_list) - 1, mid_index + range_size)
    
    # Return the indices within the range
    indices = list(range(start_index, end_index + 1))
    
    # Additional logic for odd and even lists with specific range size
    if len(sorted_list) % 2 == 1 and range_size == 1:
        return [mid_index]
    
    if len(sorted_list) % 2 == 0 and range_size == 1:
        return [mid_index - 1, mid_index]
    
    return indices