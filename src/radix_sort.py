def radix_sort(arr):
    """
    Implements the radix sort algorithm for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Find the maximum number to know the number of digits
    max_num = max(arr) if arr else 0
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        # Perform counting sort on the current digit
        output = [0] * len(arr)
        count = [0] * 10
        
        # Store count of occurrences in count[]
        for i in range(len(arr)):
            index = arr[i] // exp
            count[index % 10] += 1
        
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build the output array
        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        # Copy the output array to arr[], so that arr[] now
        # contains sorted numbers according to current digit
        arr = output[:]
        
        # Move to next digit
        exp *= 10
    
    return arr