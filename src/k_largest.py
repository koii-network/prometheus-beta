def k_largest(arr, k):
    """
    Returns the k largest elements from the input array.
    
    Args:
        arr (list): Input list of integers
        k (int): Number of largest elements to return
    
    Returns:
        list: k largest elements in descending order
    
    Raises:
        ValueError: If k is negative or larger than the array length
        TypeError: If inputs are not of the correct type
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Sort the array in descending order and return the first k elements
    return sorted(arr, reverse=True)[:k]