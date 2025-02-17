def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted array of elements
        target: The element to find
    
    Returns:
        tuple: A tuple containing (first_occurrence_index, last_occurrence_index)
               Returns (-1, -1) if the element is not found
    """
    def binary_search_first(arr, target):
        left, right = 0, len(arr) - 1
        first_occurrence = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                first_occurrence = mid
                right = mid - 1  # Continue searching in the left half
            elif (isinstance(arr[mid], type(target)) and 
                  isinstance(arr[mid], (int, float, str)) and 
                  arr[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        
        return first_occurrence
    
    def binary_search_last(arr, target):
        left, right = 0, len(arr) - 1
        last_occurrence = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                last_occurrence = mid
                left = mid + 1  # Continue searching in the right half
            elif (isinstance(arr[mid], type(target)) and 
                  isinstance(arr[mid], (int, float, str)) and 
                  arr[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        
        return last_occurrence
    
    first = binary_search_first(arr, target)
    
    # If target is not found, return (-1, -1)
    if first == -1:
        return (-1, -1)
    
    last = binary_search_last(arr, target)
    
    return (first, last)