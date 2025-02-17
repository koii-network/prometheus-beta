def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: The rotated array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If n is negative
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check n is non-negative
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    if n < 0:
        raise ValueError("Rotation amount cannot be negative")
    
    # Handle empty list or zero rotation
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation amount to be within list length
    n = n % len(arr)
    
    # Perform rotation
    return arr[n:] + arr[:n]