def find_kth_smallest(arr, k):
    """
    Find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of numbers
        k (int): The kth smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is less than 1 or greater than the array length
        TypeError: If inputs are of incorrect type
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    # Use sorting method to find kth smallest
    sorted_arr = sorted(arr)
    return sorted_arr[k-1]