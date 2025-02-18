def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Args:
        arr (list): A list of positive integers to be sorted.
    
    Returns:
        list: Sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains non-positive integers.
    """
    if not arr:
        return []
    
    # Validate input (only positive integers)
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create the "abacus" or bead frame
    beads = [[1 if x > j else 0 for x in arr] for j in range(max_num)]
    
    # Let the beads "fall" by gravity
    for i in range(max_num):
        # Count beads in each column
        bead_count = sum(row[i] for row in beads)
        
        # Drop beads to the bottom
        for j in range(len(arr)):
            beads[i][j] = 1 if bead_count > j else 0
    
    # Reconstruct the sorted array
    return [sum(row) for row in zip(*beads)]