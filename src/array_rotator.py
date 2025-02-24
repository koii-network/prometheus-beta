def rotate_array(arr, n):
    """
    Rotate an array to the right by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate right
    
    Returns:
        list: A new array rotated to the right by n positions
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    # Handle edge cases
    if not arr:  # Empty list
        return []
    
    if n < 0:
        raise ValueError("Rotation amount cannot be negative")
    
    # Normalize rotation amount to be within array length
    effective_rotation = n % len(arr)
    
    # Perform rotation
    return arr[-effective_rotation:] + arr[:-effective_rotation]