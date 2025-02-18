def quickselect(arr, k):
    """
    Implements the quickselect algorithm to find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The kth smallest element to find (1-based index)
    
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
        """
        Partition the array using the rightmost element as pivot.
        
        Args:
            left (int): Left index of the subarray
            right (int): Right index of the subarray
        
        Returns:
            int: The partition index
        """
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def select(left, right):
        """
        Recursive quickselect implementation.
        
        Args:
            left (int): Left index of the subarray
            right (int): Right index of the subarray
        
        Returns:
            The kth smallest element
        """
        if left == right:
            return arr[left]
        
        # Adjust k to be 0-indexed
        pivot_index = partition(left, right)
        
        if k - 1 == pivot_index:
            return arr[pivot_index]
        elif k - 1 < pivot_index:
            return select(left, pivot_index - 1)
        else:
            return select(pivot_index + 1, right)
    
    return select(0, len(arr) - 1)