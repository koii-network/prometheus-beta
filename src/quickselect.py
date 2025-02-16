def quickselect(arr, k):
    """
    Implements the quickselect algorithm to find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    def partition(left, right):
        """
        Partition the array using the rightmost element as pivot.
        
        Args:
            left (int): Left index of the subarray
            right (int): Right index of the subarray
        
        Returns:
            int: Final position of the pivot
        """
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def select(left, right, k_smallest):
        """
        Recursive helper function to find kth smallest element.
        
        Args:
            left (int): Left index of the subarray
            right (int): Right index of the subarray
            k_smallest (int): k-th smallest element to find
        
        Returns:
            The kth smallest element
        """
        # If the array has only one element, return that element
        if left == right:
            return arr[left]
        
        # Partition the array and get the pivot's final position
        pivot_index = partition(left, right)
        
        # Adjust k to be 0-based for comparisons
        k_adjusted = k_smallest - 1
        
        # Compare the pivot index with k
        if k_adjusted == pivot_index:
            return arr[pivot_index]
        elif k_adjusted < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
    
    # Call the recursive helper function with initial parameters
    return select(0, len(arr) - 1, k)