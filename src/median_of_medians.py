def select_kth_smallest(arr, k):
    """
    Implements the median of medians algorithm to find the kth smallest element in an array.
    
    This algorithm provides a guaranteed O(n) worst-case time complexity for selection.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): 1-based index of the element to select (1 <= k <= len(arr))
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or input is invalid
    """
    # Validate inputs
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Base case for small arrays
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    # Divide the array into groups of 5
    def divide_into_groups(arr):
        return [arr[i:i+5] for i in range(0, len(arr), 5)]
    
    # Find median of medians
    def find_median(group):
        sorted_group = sorted(group)
        return sorted_group[len(sorted_group) // 2]
    
    # Recursively find the pivot
    def select_pivot(arr):
        # If array is small, return its median
        if len(arr) <= 5:
            return find_median(arr)
        
        # Divide into groups and find medians of each group
        groups = divide_into_groups(arr)
        medians = [find_median(group) for group in groups]
        
        # Recursively find the median of medians
        return select_pivot(medians)
    
    # Partition the array around the pivot
    def partition(arr, pivot):
        left = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return left, equal, right
    
    # Main selection algorithm
    def select(arr, k):
        # Base case
        if len(arr) <= 5:
            return sorted(arr)[k-1]
        
        # Select pivot using median of medians method
        pivot = select_pivot(arr)
        
        # Partition the array
        left, equal, right = partition(arr, pivot)
        
        # Determine which partition to recurse on
        if k <= len(left):
            return select(left, k)
        elif k > len(left) + len(equal):
            return select(right, k - len(left) - len(equal))
        else:
            return pivot
    
    # Call the recursive selection function
    return select(arr, k)