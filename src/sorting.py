def merge_sort(arr):
    """
    Sort an array of integers in non-decreasing order using Merge Sort algorithm.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new sorted list in non-decreasing order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Base case: if list is 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left (list): First sorted list.
        right (list): Second sorted list.
    
    Returns:
        list: A merged sorted list.
    """
    result = []
    i, j = 0, 0
    
    # Compare and merge elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left list, if any
    result.extend(left[i:])
    
    # Add remaining elements from right list, if any
    result.extend(right[j:])
    
    return result