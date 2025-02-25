def arithmetic_sort(numbers):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    This function implements a sorting algorithm using basic arithmetic 
    without relying on built-in sorting functions.
    
    Args:
        numbers (list): A list of integers to be sorted.
    
    Returns:
        list: A new list with integers sorted in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(numbers) <= 1:
        return numbers.copy()
    
    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    # Create a copy to avoid modifying the original list
    arr = numbers.copy()
    n = len(arr)
    
    # Bubble sort using only arithmetic operations
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare and swap if needed using arithmetic comparisons
            if arr[j] > arr[j + 1]:
                # Swap using arithmetic operations
                arr[j] = arr[j] + arr[j + 1]
                arr[j + 1] = arr[j] - arr[j + 1]
                arr[j] = arr[j] - arr[j + 1]
    
    return arr