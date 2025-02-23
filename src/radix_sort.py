def radix_sort(arr):
    """
    Implement the radix sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element is not a non-negative integer.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check if all elements are non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Find the maximum number to know the number of digits
    def get_max(arr):
        return max(arr) if arr else 0
    
    # Do counting sort for every digit
    def counting_sort(arr, exp):
        n = len(arr)
        
        # Initialize output and count arrays
        output = [0] * n
        count = [0] * 10
        
        # Store count of occurrences in count[]
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        # Copy the output array to arr[], so that arr[] now
        # contains sorted numbers according to current digit
        for i in range(n):
            arr[i] = output[i]
    
    # Find the maximum number to know number of digits
    max_num = get_max(arr)
    
    # Do counting sort for every digit
    # exp is 10^i where i is current digit number
    exp = 1
    while max_num // exp > 0:
        # Deep copy to avoid modifying original list
        sorted_arr = arr.copy()
        counting_sort(sorted_arr, exp)
        arr = sorted_arr
        exp *= 10
    
    return arr