def find_second_highest(sorted_list):
    """
    Find the second highest value in a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers in ascending order.
    
    Returns:
        int or None: The second highest value, or None if the list 
                     does not have at least two unique elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if len(sorted_list) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Remove duplicates while preserving order
    unique_list = list(dict.fromkeys(sorted_list))
    
    # Check if there are at least two unique elements
    if len(unique_list) < 2:
        return None
    
    # Return the second to last element (second highest)
    return unique_list[-2]