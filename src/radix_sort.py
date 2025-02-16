def radix_sort(arr):
    """
    Implement the Radix Sort algorithm for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: The sorted list of integers.
    
    Raises:
        ValueError: If the input contains negative numbers or non-integer values.
    """
    # Validate input
    if not arr:
        return arr
    
    # Check for negative numbers or non-integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Radix sort only works with non-negative integers")
    
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        # Perform counting sort based on the current digit
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