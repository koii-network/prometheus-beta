def remove_duplicates(input_list):
    """
    Remove duplicates from a given list while preserving the original order.
    
    Args:
        input_list (list): The input list that may contain duplicate elements.
    
    Returns:
        list: A new list with duplicate elements removed, maintaining the order 
              of first occurrence of each unique element.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Use a seen set to track unique elements while preserving order
    unique_list = []
    seen = set()
    
    for item in input_list:
        # Only add the item if it hasn't been seen before
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    return unique_list