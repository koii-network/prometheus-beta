def gravity_sort(arr):
    """
    Implement the Gravity Sort (Bead Sort) algorithm.
    
    This algorithm works by simulating gravity acting on a set of beads 
    representing the input numbers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Gravity sort only works with non-negative integers")
    
    # If array is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * len(arr) for _ in range(max_num)]
    
    # Place beads for each number
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # Let gravity pull the beads down
    for row in range(max_num):
        # Count the number of beads in each column
        col_counts = [sum(beads[row][col] for row in range(max_num)) for col in range(len(arr))]
        
        # Redistribute beads from right to left
        beads_left = col_counts.copy()
        for i in range(len(arr) - 1, -1, -1):
            beads[row][i] = 1 if beads_left[i] > 0 else 0
            beads_left[i] -= 1
    
    # Count beads to reconstruct the sorted array
    sorted_arr = []
    for i in range(len(arr)):
        # Count beads in each column
        bead_count = sum(beads[row][i] for row in range(max_num))
        sorted_arr.append(bead_count)
    
    return sorted_arr