def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    First, partially sort the array using Bubble Sort to reduce the number of 
    inversions, then complete the sorting using Merge Sort.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    # If the list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr
    
    # Stage 1: Bubble Sort (partial sorting to reduce inversions)
    def bubble_sort_pass(lst):
        n = len(lst)
        for i in range(n):
            # Optimize by tracking if any swaps occurred
            swapped = False
            for j in range(0, n - i - 1):
                if lst[j] > lst[j + 1]:
                    # Swap elements
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    swapped = True
            
            # If no swapping occurred, array is already sorted
            if not swapped:
                break
        return lst
    
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
    
    def merge_sort(lst):
        """Recursive merge sort implementation."""
        # Base case: if list has 1 or fewer elements, it's already sorted
        if len(lst) <= 1:
            return lst
        
        # Divide the list into two halves
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        # Recursively sort both halves
        left = merge_sort(left)
        right = merge_sort(right)
        
        # Merge the sorted halves
        return merge(left, right)
    
    # Stage 1: Partial Bubble Sort to reduce inversions
    partially_sorted = bubble_sort_pass(arr.copy())
    
    # Stage 2: Complete sorting with Merge Sort
    return merge_sort(partially_sorted)