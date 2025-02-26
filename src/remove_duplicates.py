def remove_duplicates(input_list):
    """
    Remove duplicate values from a list of integers while maintaining original order.
    
    Args:
        input_list (list): A list of integers to remove duplicates from.
    
    Returns:
        list: A new list with duplicates removed, preserving the original order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are integers
    if not all(isinstance(x, int) for x in input_list):
        raise TypeError("All list elements must be integers")
    
    # Use dict.fromkeys to preserve order and remove duplicates
    # This is an efficient approach that maintains original order
    return list(dict.fromkeys(input_list))