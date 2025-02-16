def median_of_medians(arr):
    """
    Implement the median of medians algorithm to find the kth smallest element.
    
    The algorithm guarantees O(n) worst-case time complexity for selection.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        The median of the input list
    
    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    def partition(lst, pivot):
        """
        Partition the list around the pivot element.
        
        Args:
            lst (list): List to partition
            pivot (any): Pivot element to partition around
        
        Returns:
            tuple: (less than pivot, equal to pivot, greater than pivot)
        """
        less = [x for x in lst if x < pivot]
        equal = [x for x in lst if x == pivot]
        greater = [x for x in lst if x > pivot]
        
        return less, equal, greater
    
    def select(lst, k):
        """
        Select the kth smallest element using median of medians algorithm.
        
        Args:
            lst (list): Input list
            k (int): Index of the element to select (0-based)
        
        Returns:
            The kth smallest element
        """
        # Base case for small lists
        if len(lst) <= 5:
            return sorted(lst)[k]
        
        # Divide the list into sublists of 5 elements
        sublists = [lst[i:i+5] for i in range(0, len(lst), 5)]
        
        # Find the median of each sublist
        medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
        
        # Recursively find the median of medians (pivot)
        pivot = select(medians, len(medians)//2)
        
        # Partition the list
        less, equal, greater = partition(lst, pivot)
        
        # Decide which partition to recurse on
        if k < len(less):
            return select(less, k)
        elif k < len(less) + len(equal):
            return pivot
        else:
            return select(greater, k - len(less) - len(equal))
    
    # Return the median (middle element)
    return select(arr, len(arr)//2)