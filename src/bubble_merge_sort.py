def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    First, performs a pass of Bubble Sort to partially order the list.
    Then applies Merge Sort to complete the sorting.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    """
    # If the list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Stage 1: Bubble Sort pass to partially order the list
    def bubble_sort_pass(arr):
        n = len(arr)
        for i in range(n):
            # Flag to optimize by stopping if no swaps occur
            swapped = False
            
            # Iterate through the unsorted portion
            for j in range(0, n - i - 1):
                # If the element found is greater than the next element, swap them
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no swapping occurred, list is already sorted
            if not swapped:
                break
        
        return arr
    
    # Stage 2: Merge Sort
    def merge_sort(arr):
        # Base case: if the list has 1 or fewer elements, it's already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide the list into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively sort both halves
        left = merge_sort(left)
        right = merge_sort(right)
        
        # Merge the sorted halves
        return merge(left, right)
    
    def merge(left, right):
        result = []
        l_idx, r_idx = 0, 0
        
        # Compare and merge elements from both lists
        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] <= right[r_idx]:
                result.append(left[l_idx])
                l_idx += 1
            else:
                result.append(right[r_idx])
                r_idx += 1
        
        # Add remaining elements from left list, if any
        result.extend(left[l_idx:])
        
        # Add remaining elements from right list, if any
        result.extend(right[r_idx:])
        
        return result
    
    # Stage 1: Perform Bubble Sort pass
    partially_sorted = bubble_sort_pass(arr.copy())
    
    # Stage 2: Apply Merge Sort to complete sorting
    return merge_sort(partially_sorted)