def find_median_index(arr):
    """
    Find the median index or value in a sorted array of integers.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        If array length is odd: index of the median element
        If array length is even: average of the two middle elements
    
    Raises:
        ValueError: If input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Get the middle index
    mid = len(arr) // 2
    
    # If array length is odd, return the middle index
    if len(arr) % 2 != 0:
        return mid
    
    # If array length is even, return the average of the two middle elements
    return (arr[mid-1] + arr[mid]) / 2