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
        Partition the array around a pivot, moving pivot to the end
        
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
        Recursive selection algorithm using median of medians
        
        Args:
            arr (list): Input array
            left (int): Left index of subarray
            right (int): Right index of subarray
            k (int): k-th smallest element to find
        
        Returns:
            The kth smallest element
        """
        # If the subarray has only one element, return it
        if left == right:
            return arr[left]
        
        # Choose pivot using median of medians method
        def choose_pivot(arr, left, right):
            # If less than 5 elements, find approximate median
            if right - left < 4:
                return (left + right) // 2
            
            # Divide into groups of 5, find medians
            for i in range(left, right+1, 5):
                # Sort each group of 5
                group = sorted(arr[i:min(i+5, right+1)])
                # Put median of each group in correct place
                median = group[len(group)//2]
                median_index = arr.index(median, i, min(i+5, right+1))
                
                # Swap to the front
                mid_index = (left + (right-left)//10) * 2
                arr[mid_index], arr[median_index] = arr[median_index], arr[mid_index]
            
            # Recursively find median of medians
            return (left + right) // 2
        
        # Choose pivot using median of medians
        pivot_index = choose_pivot(arr, left, right)
        
        # Partition around the pivot
        pivot_index = partition(arr, left, right, pivot_index)
        
        # Compute the rank of the pivot
        pivot_rank = pivot_index - left + 1
        
        # If k matches pivot's rank, return the pivot
        if k == pivot_rank:
            return arr[pivot_index]
        
        # If k is less than pivot's rank, search left subarray
        elif k < pivot_rank:
            return select(arr, left, pivot_index - 1, k)
        
        # If k is greater than pivot's rank, search right subarray
        else:
            return select(arr, pivot_index + 1, right, k - pivot_rank)
    
    # Use a copy of the array to preserve original
    arr_copy = arr.copy()
    return select(arr_copy, 0, len(arr_copy) - 1, k)