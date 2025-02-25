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
            # If 5 or fewer elements, just find median
            if right - left < 5:
                sorted_subarray = sorted(arr[left:right+1])
                return arr.index(sorted_subarray[len(sorted_subarray)//2])
            
            # Divide into groups of 5, find median of medians
            medians = []
            for i in range(left, right+1, 5):
                group = arr[i:min(i+5, right+1)]
                median = sorted(group)[len(group)//2]
                medians.append(median)
            
            # Recursively find median of medians
            if len(medians) <= 5:
                median_of_medians = sorted(medians)[len(medians)//2]
            else:
                median_of_medians = select(medians, 0, len(medians)-1, len(medians)//2)
            
            return arr.index(median_of_medians)
        
        # Choose pivot using median of medians
        pivot_index = choose_pivot(arr, left, right)
        
        # Partition around the pivot
        pivot_index = partition(arr, left, right, pivot_index)
        
        # The pivot is in its final sorted position
        if k == pivot_index - left + 1:
            return arr[pivot_index]
        
        # If k is less than pivot's position, recurse on left subarray
        elif k < pivot_index - left + 1:
            return select(arr, left, pivot_index - 1, k)
        
        # If k is greater, recurse on right subarray
        else:
            return select(arr, pivot_index + 1, right, k - (pivot_index - left + 1))
    
    # Call the recursive selection function
    return select(arr.copy(), 0, len(arr) - 1, k)