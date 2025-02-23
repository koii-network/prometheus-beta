def remove_duplicates(arr):
    """
    Remove duplicate values from an array, preserving the original order.

    Args:
        arr (list): Input list that may contain duplicate values.

    Returns:
        list: A new list with duplicates removed, maintaining the order 
              of first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a list comprehension with a seen set to track unique elements
    seen = set()
    unique_list = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list