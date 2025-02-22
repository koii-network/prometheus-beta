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
        Partition the array around the pivot element.
        
        Args:
            arr (list): Input list to partition
            pivot: Pivot element to partition around
        
        Returns:
            tuple: (less than pivot, equal to pivot, greater than pivot)
        """
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        
        return less, equal, greater
    
    def select(arr, k):
        """
        Select the kth smallest element using median of medians algorithm.
        
        Args:
            arr (list): Input list
            k (int): Index of the element to select (0-based)
        
        Returns:
            The kth smallest element
        """
        # Base case: if list is small, sort and return
        if len(arr) <= 5:
            return sorted(arr)[k]
        
        # Divide the list into groups of 5 and find their medians
        subgroups = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
        medians = [group[len(group)//2] for group in subgroups]
        
        # Recursively find the median of medians
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)//2]
        else:
            pivot = select(medians, len(medians)//2)
        
        # Partition the array around the pivot
        less, equal, greater = partition(arr, pivot)
        
        # Recurse on the appropriate sublist
        if k < len(less):
            return select(less, k)
        elif k < len(less) + len(equal):
            return pivot
        else:
            return select(greater, k - len(less) - len(equal))
    
    # Return the median (middle element)
    return select(arr, len(arr)//2)