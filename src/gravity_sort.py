def gravity_sort(arr):
    """
    Implement the gravity sort (bead sort) algorithm.
    
    Gravity sort works by simulating gravity acting on a set of beads,
    where each bead represents a number in the input array.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Gravity sort only works with non-negative integers")
    
    # If array is empty or has only one element, return it
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of beads
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * max_num for _ in range(len(arr))]
    
    # Place beads based on input array
    for i, num in enumerate(arr):
        for j in range(num):
            beads[i][j] = 1
    
    # Let the beads "fall" by gravity
    for col in range(max_num):
        # Count beads in each column
        col_sum = sum(beads[row][col] for row in range(len(arr)))
        
        # Drop the beads to the bottom
        for row in range(len(arr) - col_sum, len(arr)):
            beads[row][col] = 1
        for row in range(len(arr) - col_sum):
            beads[row][col] = 0
    
    # Reconstruct the sorted array
    sorted_arr = []
    for row in range(len(arr)):
        # Count the number of beads in each row
        num_beads = sum(beads[row])
        sorted_arr.append(num_beads)
    
    return sorted_arr