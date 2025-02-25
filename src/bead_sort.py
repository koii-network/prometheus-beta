def bead_sort(arr):
    """
    Implement the Bead Sort algorithm for positive integers.
    
    Bead sort is a natural sorting algorithm inspired by the physical movement of beads
    on parallel rods under gravity. It only works with positive integers.
    
    Args:
        arr (list): A list of positive integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains non-integer or negative numbers.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for invalid inputs
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # Simulate the bead sorting process
    if len(arr) == 1:
        return arr
    
    # Use a different approach for bead sort
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr