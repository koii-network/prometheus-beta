def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: A new array with elements rotated left by n positions
    
    Raises:
        TypeError: If input is not a list
        ValueError: If n is negative
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for negative rotation
    if n < 0:
        raise ValueError("Rotation positions must be non-negative")
    
    # Handle empty array or zero rotation
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation to handle cases where n > len(arr)
    n = n % len(arr)
    
    # Perform rotation
    return arr[n:] + arr[:n]