def rotate_array(arr, n):
    """
    Rotate an array to the right by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate right
    
    Returns:
        list: The rotated array
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(n, int):
        raise TypeError("Rotation positions must be an integer")
    if n < 0:
        raise ValueError("Rotation positions cannot be negative")
    
    # Handle empty array or zero rotation
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation to handle rotations larger than array length
    n = n % len(arr)
    
    # Perform rotation
    return arr[-n:] + arr[:-n]