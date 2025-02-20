def remove_duplicates(arr):
    """
    Remove duplicates from an array of integers while preserving the original order.
    
    Args:
        arr (list): An input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the first occurrence order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate list contents
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("List must contain only integers")
    
    # Use a set to track seen values while preserving order
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result