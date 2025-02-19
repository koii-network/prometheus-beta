def find_median_index(arr):
    """
    Find the median index or value in a sorted array of integers.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        float or int: 
        - If array length is odd, returns the middle index 
        - If array length is even, returns the average of the two middle indices
    
    Raises:
        ValueError: If input array is empty
    """
    if not arr:
        raise ValueError("Cannot find median of an empty array")
    
    # Get the length of the array
    n = len(arr)
    
    # If odd number of elements, return the middle index
    if n % 2 != 0:
        return n // 2
    
    # If even number of elements, return average of two middle indices
    return (n // 2 - 1 + n // 2) / 2