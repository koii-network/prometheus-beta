def find_median_index(arr):
    """
    Find the median index or value in a sorted array of integers.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        int or float: The median index for odd-length arrays,
                      or the average of two middle elements for even-length arrays
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Get the length of the array
    n = len(arr)
    
    # If array has odd number of elements, return the middle index
    if n % 2 != 0:
        return n // 2
    
    # If array has even number of elements, return average of two middle indices
    mid_right = n // 2
    mid_left = mid_right - 1
    
    return (mid_left + mid_right) / 2