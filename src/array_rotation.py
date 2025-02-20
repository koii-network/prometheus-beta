def rotate_array(arr, n):
    """
    Rotate an array to the right by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate the array to the right
    
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
    
    # Handle empty array or zero rotation case
    if not arr or n == 0:
        return arr.copy()
    
    # Normalize rotation amount to be within array length
    n = n % len(arr)
    
    # Perform rotation by slicing
    return arr[-n:] + arr[:-n]