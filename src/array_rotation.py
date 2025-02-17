def rotate_array_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: A new array rotated to the left by n positions
    
    Raises:
        TypeError: If input is not a list
        ValueError: If n is negative
    """
    # Validate inputs
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation count must be an integer")
    
    if n < 0:
        raise ValueError("Rotation count cannot be negative")
    
    # Handle empty array or no rotation cases
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation count to be within array length
    n = n % len(arr)
    
    # Rotate the array
    return arr[n:] + arr[:n]