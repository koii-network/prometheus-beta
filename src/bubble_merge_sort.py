def bubble_merge_sort(arr):
    """
    Custom sorting algorithm combining Bubble Sort and Merge Sort.
    
    First applies Bubble Sort to partially order the list,
    then uses Merge Sort for final efficient sorting.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Stage 1: Bubble Sort (partially order the list)
    def bubble_sort_pass(arr):
        n = len(arr)
        for i in range(n):
            # Flag to optimize - stop if no swaps occur
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no swapping occurred, list is already sorted
            if not swapped:
                break
        return arr
    
    # Stage 2: Merge Sort (final efficient sorting)
    def merge_sort(arr):
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively sort both halves
        left = merge_sort(left)
        right = merge_sort(right)
        
        # Merge
        return merge(left, right)
    
    def merge(left, right):
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
    
    # Execute both stages
    partially_sorted = bubble_sort_pass(arr.copy())
    return merge_sort(partially_sorted)