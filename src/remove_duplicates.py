def remove_duplicates(input_list):
    """
    Remove duplicate values from a list while preserving the original order of unique elements.
    
    Args:
        input_list (list): A list of integers to process.
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order of first occurrence.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([10, 20, 30, 20, 10, 40, 50])
        [10, 20, 30, 40, 50]
    """
    # Type checking
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("List must contain only integers")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in input_list:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result