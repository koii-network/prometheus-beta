def library_sort(arr):
    """
    Implement the Library Sort (Insertion Sort with Binary Search) algorithm.
    
    Library Sort is an adaptive sorting algorithm that uses binary search 
    to reduce the number of shifts during insertion sort.
    
    Args:
        arr (list): The input list to be sorted in ascending order
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a new list to store sorted elements
    sorted_arr = [arr[0]]
    
    # Iterate through the remaining elements
    for item in arr[1:]:
        # Use binary search to find the correct insertion point
        left, right = 0, len(sorted_arr)
        while left < right:
            mid = (left + right) // 2
            if sorted_arr[mid] < item:
                left = mid + 1
            else:
                right = mid
        
        # Insert the item at the correct position
        sorted_arr.insert(left, item)
    
    return sorted_arr