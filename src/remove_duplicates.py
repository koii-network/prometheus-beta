def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while preserving the original order.
    
    Args:
        input_list (list): A list of integers to process.
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in input_list):
        raise TypeError("All list elements must be integers")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in input_list:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result