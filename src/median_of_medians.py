def median_of_medians(arr):
    """
    Implement the median of medians algorithm to find the kth smallest element in O(n) time.
    
    Args:
        arr (list): A list of comparable elements
    
    Returns:
        The median element of the input list
    
    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    def partition(arr, pivot):
        """
        Partition the array around the pivot element.
        
        Args:
            arr (list): The input list
            pivot (any): The pivot element to partition around
        
        Returns:
            tuple: Three lists - elements less than pivot, equal to pivot, and greater than pivot
        """
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return less, equal, greater
    
    def select(arr, k):
        """
        Recursively find the kth smallest element.
        
        Args:
            arr (list): The input list
            k (int): The index of the element to find (0-based)
        
        Returns:
            The kth smallest element
        """
        # Base case: if list is small, sort and return kth element
        if len(arr) <= 5:
            return sorted(arr)[k]
        
        # Divide the list into sublists of 5 elements
        sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
        
        # Find the median of each sublist
        medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
        
        # Recursively find the median of medians
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)//2]
        else:
            pivot = select(medians, len(medians)//2)
        
        # Partition the array around the pivot
        less, equal, greater = partition(arr, pivot)
        
        # Decide which partition to search
        if k < len(less):
            return select(less, k)
        elif k < len(less) + len(equal):
            return pivot
        else:
            return select(greater, k - len(less) - len(equal))
    
    # Return the median (middle element) of the list
    return select(arr, len(arr)//2)