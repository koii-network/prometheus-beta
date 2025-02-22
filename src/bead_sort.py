def bead_sort(arr):
    """
    Implement the Bead Sort algorithm (Gravity Sort) for positive integers.
    
    Bead Sort is a natural sorting algorithm that works similarly to how beads 
    fall under gravity when arranged vertically.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * max_num for _ in range(len(arr))]
    
    # Place beads
    for i, num in enumerate(arr):
        for j in range(num):
            beads[i][j] = 1
    
    # Let beads fall
    for col in range(max_num):
        column_sum = 0
        for row in range(len(arr)):
            column_sum += beads[row][col]
            beads[row][col] = 0
        
        # Distribute beads from bottom up
        for row in range(len(arr) - 1, len(arr) - column_sum - 1, -1):
            beads[row][col] = 1
    
    # Convert back to sorted list
    sorted_arr = [sum(row) for row in beads]
    
    return sorted_arr