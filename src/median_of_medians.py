def median_of_medians(arr):
    """
    Implement the median of medians algorithm to find the kth smallest element.
    
    The algorithm provides a guaranteed O(n) worst-case time complexity for selection.
    
    Args:
        arr (list): A list of comparable elements
    
    Returns:
        The median of the input array
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    def partition(arr, pivot):
        """
        Partition the array around the pivot element.
        
        Args:
            arr (list): The array to partition
            pivot: The pivot element
        
        Returns:
            tuple: Lists of elements less than, equal to, and greater than the pivot
        """
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        
        return less, equal, greater
    
    def select(arr, k):
        """
        Find the kth smallest element using median of medians algorithm.
        
        Args:
            arr (list): The input array
            k (int): The index of the element to find (0-based)
        
        Returns:
            The kth smallest element
        """
        # Base case for small arrays
        if len(arr) <= 5:
            return sorted(arr)[k]
        
        # Divide the array into groups of 5
        groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
        
        # Find the median of each group
        medians = [sorted(group)[len(group)//2] for group in groups]
        
        # Recursively find the median of medians
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)//2]
        else:
            pivot = select(medians, len(medians)//2)
        
        # Partition the array
        less, equal, greater = partition(arr, pivot)
        
        # Recursive cases
        if k < len(less):
            return select(less, k)
        elif k < len(less) + len(equal):
            return pivot
        else:
            return select(greater, k - len(less) - len(equal))
    
    # Calculate the correct median index
    k = (len(arr) - 1) // 2
    return select(arr, k)