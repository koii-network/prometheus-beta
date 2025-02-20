def remove_duplicates(arr):
    """
    Remove duplicates from an array of integers while preserving the original order.
    
    Args:
        arr (list): An input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the first occurrence order
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result