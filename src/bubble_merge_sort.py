def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    First, perform a partial Bubble Sort to partially order the list.
    Then, use Merge Sort to complete the sorting process.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    # If the list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr
    
    # Stage 1: Partial Bubble Sort (reduce inversions)
    n = len(arr)
    for i in range(min(5, n)):  # Limit bubble sort passes
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Stage 2: Merge Sort
    def merge(left, right):
        """Merge two sorted lists."""
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
    
    def merge_sort(arr):
        """Recursive merge sort implementation."""
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # Conquer (merge)
        return merge(left, right)
    
    # Complete sorting with Merge Sort
    return merge_sort(arr)