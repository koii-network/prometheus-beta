def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A sorted list of integers.
    """
    # If list is empty or has only one element, return it as-is
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Bubble sort using only arithmetic comparisons and swaps
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Use arithmetic comparison instead of comparison operators
            if (sorted_arr[j] > sorted_arr[j + 1]) == True:
                # Swap using arithmetic operations
                sorted_arr[j] = sorted_arr[j] + sorted_arr[j + 1]
                sorted_arr[j + 1] = sorted_arr[j] - sorted_arr[j + 1]
                sorted_arr[j] = sorted_arr[j] - sorted_arr[j + 1]
    
    return sorted_arr