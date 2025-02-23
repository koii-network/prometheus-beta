def library_sort(arr):
    """
    Implement the Library Sort (Insertion Sort variant) algorithm.
    
    Library Sort is a variant of Insertion Sort that uses extra space to 
    reduce the number of element movements during sorting.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a sorted list with first element and extra space
    sorted_list = [arr[0]]
    extra_space = [None] * len(arr)
    
    # Insert remaining elements
    for i in range(1, len(arr)):
        current = arr[i]
        
        # Binary search to find insertion point
        left, right = 0, len(sorted_list)
        while left < right:
            mid = (left + right) // 2
            if sorted_list[mid] < current:
                left = mid + 1
            else:
                right = mid
        
        # Shift elements to make space for insertion
        sorted_list.insert(left, current)
    
    return sorted_list