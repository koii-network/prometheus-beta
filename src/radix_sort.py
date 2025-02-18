def radix_sort(arr):
    """
    Implement radix sort algorithm for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    if not arr:
        return []
    
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Radix sort only works with non-negative integers")
    
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

def counting_sort(arr, exp):
    """
    Helper function to perform counting sort on a specific digit.
    
    Args:
        arr (list): The list to be sorted.
        exp (int): The current digit place value (1, 10, 100, etc.).
    """
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