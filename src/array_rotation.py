def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: A new array rotated to the left by n positions
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    if n < 0:
        raise ValueError("Rotation amount cannot be negative")
    
    # Handle edge cases
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation amount to be within array length
    n = n % len(arr)
    
    # Perform rotation
    return arr[n:] + arr[:n]