def remove_duplicates(input_array):
    """
    Remove duplicate values from an array while preserving the original order.
    
    Args:
        input_array (list): The input list that may contain duplicate values.
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen values while preserving order
    seen = set()
    return [x for x in input_array if not (x in seen or seen.add(x))]