def gravity_sort(arr):
    """
    Implement the gravity sort (Bead sort) algorithm.
    
    Gravity sort works by simulating beads dropping under gravity,
    effectively sorting the input list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers or non-integer values.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for non-negative integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Input must be a list of non-negative integers")
    
    # Find the maximum number to determine the number of beads
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[1 if num > j else 0 for j in range(max_num)] for num in arr]
    
    # Simulate gravity
    for col in range(max_num):
        # Count beads in each column
        bead_count = sum(row[col] for row in beads)
        
        # Drop beads down
        for row in range(len(beads)):
            beads[row][col] = 1 if row < bead_count else 0
    
    # Convert back to sorted list
    return [sum(row) for row in beads]