def find_kth_smallest(arr, k):
    """
    Implement the median of medians algorithm to find the kth smallest element in an array.
    
    This algorithm provides a guaranteed O(n) worst-case time complexity for selection.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is invalid (less than 1 or greater than array length)
    """
    # Input validation
    if not arr:
        raise ValueError("Array cannot be empty")
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    def partition(arr, left, right, pivot_index):
        """
        Partition the array around a pivot.
        
        Args:
            arr (list): Input array
            left (int): Left index of subarray
            right (int): Right index of subarray
            pivot_index (int): Index of the pivot element
        
        Returns:
            int: Final position of the pivot element
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
    
    def select(arr, left, right, k):
        """
        Recursive selection algorithm using median of medians.
        
        Args:
            arr (list): Input array
            left (int): Left index of subarray
            right (int): Right index of subarray
            k (int): k-th smallest element to find
        
        Returns:
            The kth smallest element
        """
        # Base case: if array has less than 5 elements
        if right - left < 4:
            sorted_subarray = sorted(arr[left:right+1])
            return sorted_subarray[k-1]
        
        # Divide array into groups of 5
        def median_of_groups(arr, left, right):
            """Find median of medians of 5-element groups."""
            medians = []
            for i in range(left, right+1, 5):
                group = arr[i:min(i+5, right+1)]
                medians.append(sorted(group)[len(group)//2])
            return sorted(medians)[len(medians)//2]
        
        # Find pivot using median of medians
        pivot = median_of_groups(arr, left, right)
        pivot_index = arr.index(pivot, left, right+1)
        
        # Partition around pivot
        pivot_index = partition(arr, left, right, pivot_index)
        
        # Compute rank of pivot
        pivot_rank = pivot_index - left + 1
        
        # Compare k with pivot's rank
        if k == pivot_rank:
            return arr[pivot_index]
        elif k < pivot_rank:
            return select(arr, left, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, right, k - pivot_rank)
    
    # Create a copy of the array to avoid modifying the original
    arr_copy = arr.copy()
    return select(arr_copy, 0, len(arr_copy) - 1, k)