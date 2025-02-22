def quickselect(arr, k):
    """
    Implement the quickselect algorithm to find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or the input is invalid
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    def partition(left, right):
        """Partition the array and return the pivot index."""
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def select(left, right):
        """Recursive helper to find the kth smallest element."""
        if left == right:
            return arr[left]
        
        pivot_index = partition(left, right)
        
        # Adjust k to be 0-based index
        k_index = k - 1
        
        if k_index == pivot_index:
            return arr[k_index]
        elif k_index < pivot_index:
            return select(left, pivot_index - 1)
        else:
            return select(pivot_index + 1, right)
    
    return select(0, len(arr) - 1)