def find_second_highest(sorted_list):
    """
    Find the second highest value in a sorted list of integers.
    
    Args:
        sorted_list (list): A sorted list of integers in ascending or descending order.
    
    Returns:
        int or None: The second highest value, or None if the list has fewer than 2 elements.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-integer elements.
    """
    # Validate input type
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("List must contain only integers")
    
    # Check list length
    if len(sorted_list) < 2:
        return None
    
    # Handle sorted lists (either ascending or descending)
    if sorted_list == sorted(sorted_list):  # Ascending order
        return sorted_list[-2]
    else:  # Descending order
        return sorted_list[1]