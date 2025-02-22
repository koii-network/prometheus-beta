def library_sort(arr):
    """
    Implement the Library Sort algorithm.
    
    Library Sort is a sorting algorithm that creates a larger array with gaps 
    to minimize the number of moves during sorting.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create an expanded array with gaps (roughly 2x the size of input)
    expanded_size = len(arr) * 2
    sorted_arr = [None] * expanded_size
    
    # Insert the first element
    sorted_arr[0] = arr[0]
    
    # Insert remaining elements
    for i in range(1, len(arr)):
        # Binary search to find the correct insertion point
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if sorted_arr[mid] is None or arr[i] > sorted_arr[mid]:
                left = mid + 1
            else:
                right = mid
        
        # Shift elements to make space if needed
        while left < expanded_size and sorted_arr[left] is not None:
            left += 1
        
        # Insert the element
        sorted_arr[left] = arr[i]
    
    # Remove None values and return the sorted list
    return [x for x in sorted_arr if x is not None]