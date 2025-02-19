def find_second_highest(sorted_list):
    """
    Find the second highest value in a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers in ascending or descending order.
    
    Returns:
        int or None: The second highest value, or None if the list has fewer than 2 elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Check input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Check list content
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("List must contain only integers")
    
    # Handle lists with fewer than 2 elements
    if len(sorted_list) < 2:
        return None
    
    # For sorted lists (either ascending or descending)
    if len(set(sorted_list)) < 2:
        return None
    
    # For ascending sorted list
    if sorted_list == sorted(sorted_list):
        return sorted_list[-2]
    
    # For descending sorted list
    return sorted_list[1]