def median_of_medians(arr):
    """
    Implement the median of medians algorithm to find the kth smallest element in O(n) time.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        The median of the input list
    
    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    def partition(arr, pivot):
        """
        Partition the array around the pivot, returning the pivot's final index.
        
        Args:
            arr (list): Input list to partition
            pivot: Pivot element to partition around
        
        Returns:
            int: Final index of the pivot
        """
        # Move pivot to end
        pivot_index = arr.index(pivot)
        arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
        
        # Partition
        store_index = 0
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[store_index], arr[-1] = arr[-1], arr[store_index]
        return store_index
    
    def select(arr, k):
        """
        Select the kth smallest element using median of medians algorithm.
        
        Args:
            arr (list): Input list
            k (int): Index of the element to select (0-based)
        
        Returns:
            The kth smallest element
        """
        # Base case for small lists
        if len(arr) <= 5:
            return sorted(arr)[k]
        
        # Divide into groups of 5 and find their medians
        medians = []
        for i in range(0, len(arr), 5):
            group = arr[i:i+5]
            medians.append(sorted(group)[len(group)//2])
        
        # Recursively find the median of medians (pivot)
        pivot = select(medians, len(medians)//2)
        
        # Partition around the pivot
        pivot_index = partition(arr, pivot)
        
        # Recursive select
        if k == pivot_index:
            return pivot
        elif k < pivot_index:
            return select(arr[:pivot_index], k)
        else:
            return select(arr[pivot_index+1:], k - pivot_index - 1)
    
    # Return the median (middle element)
    return select(arr.copy(), len(arr)//2)