def find_min_max(arr):
    """
    Find the highest and lowest numbers in an input array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        tuple: A tuple containing (lowest number, highest number)
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    return min(arr), max(arr)