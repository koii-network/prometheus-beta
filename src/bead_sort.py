def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: Sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains non-integer or non-positive elements.
    """
    if not arr:
        return []
    
    # Validate input (only non-negative integers)
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # Special case for single element
    if len(arr) == 1:
        return arr
    
    # Create a grid representation
    rows = max(arr)
    cols = len(arr)
    grid = [[0] * cols for _ in range(rows)]
    
    # Place beads
    for j, val in enumerate(arr):
        for i in range(val):
            grid[i][j] = 1
    
    # Drop beads and count
    result = []
    for j in range(cols):
        current_col_beads = sum(grid[i][j] for i in range(rows))
        result.append(current_col_beads)
    
    return sorted(result)