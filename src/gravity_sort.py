def gravity_sort(arr):
    """
    Implement the gravity sort (Bead sort) algorithm.
    
    Gravity sort works by simulating gravity acting on a set of beads.
    It works best with positive integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: Sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Gravity sort only works with non-negative integers")
    
    # If array is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * len(arr) for _ in range(max_num)]
    
    # Place beads representing the input numbers
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # Let gravity pull beads down
    for row in range(max_num):
        # Count beads in each column and move them down
        col_counts = [sum(beads[row][:]) for row in range(max_num)]
    
    # Reconstruct the sorted array by counting beads from bottom up
    sorted_arr = [0] * len(arr)
    for i in range(len(arr)):
        column_height = sum(beads[row][i] for row in range(max_num))
        sorted_arr[i] = column_height
    
    return sorted_arr