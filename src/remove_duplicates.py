def remove_duplicates(input_list):
    """
    Remove duplicates from a given list while preserving the original order.
    
    Args:
        input_list (list): The input list that may contain duplicate elements.
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while maintaining order
    seen = set()
    unique_list = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list