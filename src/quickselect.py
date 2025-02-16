def quickselect(arr, k):
    """
    Implements the quickselect algorithm to find the kth smallest element in an unsorted list.
    
    Args:
        arr (list): A list of comparable elements
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of range or the input is invalid
    """
    # Validate inputs
    if not arr:
        raise ValueError("Input array cannot be empty")
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    def partition(left, right, pivot_index):
        """
        Partition the array around a pivot, returning the final pivot index
        """
        pivot = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        # Partition
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        
        return store_index
    
    def select(left, right):
        """
        Recursive quickselect implementation
        """
        # If the array contains only one element, return that element
        if left == right:
            return arr[left]
        
        # Select a random pivot_index between left and right
        import random
        pivot_index = random.randint(left, right)
        
        # Partition around the pivot
        pivot_index = partition(left, right, pivot_index)
        
        # The pivot is in its final sorted position
        if k - 1 == pivot_index:
            return arr[pivot_index]
        # If k is less than the pivot index, search left subarray
        elif k - 1 < pivot_index:
            return select(left, pivot_index - 1)
        # If k is greater than the pivot index, search right subarray
        else:
            return select(pivot_index + 1, right)
    
    # Call the recursive select function
    return select(0, len(arr) - 1)