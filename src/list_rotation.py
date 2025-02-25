def rotate_list(lst, k):
    """
    Rotate a list by k positions to the right.
    
    Args:
        lst (list): The input list to be rotated
        k (int): Number of positions to rotate the list to the right
    
    Returns:
        list: A new list rotated k positions to the right
    
    Raises:
        TypeError: If input is not a list or k is not an integer
        ValueError: If k is negative
    """
    # Validate inputs
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("Rotation amount must be an integer")
    
    if k < 0:
        raise ValueError("Rotation amount cannot be negative")
    
    # Handle empty list or no rotation cases
    if not lst or k == 0:
        return lst.copy()
    
    # Normalize k to be within list length
    k = k % len(lst)
    
    # Perform rotation
    return lst[-k:] + lst[:-k]