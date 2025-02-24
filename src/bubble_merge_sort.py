def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort techniques.
    
    The algorithm works in two stages:
    1. Partially sort the array using Bubble Sort to reduce large inversions
    2. Perform a Merge Sort to complete the sorting process
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Stage 1: Bubble Sort to reduce large inversions
    def bubble_sort_partial(arr):
        """Perform a partial Bubble Sort to reduce large inversions"""
        n = len(arr)
        for i in range(n // 2):  # Only perform a few passes
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    # Stage 2: Merge Sort
    def merge_sort(arr):
        """Perform Merge Sort to complete the sorting"""
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursive merge sort on both halves
        left = merge_sort(left)
        right = merge_sort(right)
        
        # Merge
        return merge(left, right)
    
    def merge(left, right):
        """Merge two sorted lists"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    # Main algorithm: Partial Bubble Sort followed by Merge Sort
    partially_sorted = bubble_sort_partial(arr.copy())
    return merge_sort(partially_sorted)