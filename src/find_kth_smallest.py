def find_kth_smallest(arr, k):
    """
    Find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is less than 1 or greater than the array length
        TypeError: If input is not a list or k is not an integer
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Validate k range
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    # Handle edge cases
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # Sort the array and return the kth smallest element
    # Note: k is 1-based, so we subtract 1 for 0-based indexing
    return sorted(arr)[k-1]