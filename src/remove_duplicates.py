def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while maintaining the original order.
    
    Args:
        input_list (list): A list of integers to remove duplicates from.
    
    Returns:
        list: A new list with duplicates removed, preserving the original order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements efficiently
    seen = set()
    result = []
    
    for item in input_list:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result