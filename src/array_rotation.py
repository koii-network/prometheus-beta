def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: The rotated array
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    # Handle negative or zero rotation
    if n <= 0:
        return arr
    
    # Handle case where n is larger than array length
    n = n % len(arr) if arr else 0
    
    # Perform rotation
    return arr[n:] + arr[:n]