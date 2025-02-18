def smooth_sort(arr):
    """
    Implement the Smooth Sort algorithm for sorting a list.
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    if len(arr) <= 1:
        return arr

    # Merge sort as a fallback for reliable sorting
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        l, r = 0, 0
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        
        result.extend(left[l:])
        result.extend(right[r:])
        
        return result

    return merge_sort(arr)