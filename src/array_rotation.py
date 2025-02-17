def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: A new rotated array
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative or if n is larger than array length
    """
    # Check input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    # Handle edge cases
    if not arr:  # Empty list
        return arr
    
    # Normalize rotation amount
    n = n % len(arr) if n >= 0 else raise ValueError("Rotation amount cannot be negative")
    
    # Perform rotation and return new list
    return arr[n:] + arr[:n]