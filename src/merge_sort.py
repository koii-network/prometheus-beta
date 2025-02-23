def merge_sort(arr):
    """
    Implement the Merge Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains elements that cannot be compared.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
    
    Returns:
        list: A merged and sorted list.
    """
    merged = []
    left_index, right_index = 0, 0
    
    # Compare and merge elements from both lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from left list, if any
    merged.extend(left[left_index:])
    
    # Add remaining elements from right list, if any
    merged.extend(right[right_index:])
    
    return merged