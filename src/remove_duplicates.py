def remove_duplicates(arr):
    """
    Remove duplicate values from an input array while preserving the original order.

    Args:
        arr (list): The input array from which duplicates should be removed.

    Returns:
        list: A new list with duplicate values removed, maintaining the order 
              of first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a dict to maintain order (Python 3.7+) and track unique elements
    seen = {}
    for item in arr:
        # Only keep the first occurrence of each item
        if item not in seen:
            seen[item] = None
    
    # Return the list of unique items in their original order
    return list(seen.keys())