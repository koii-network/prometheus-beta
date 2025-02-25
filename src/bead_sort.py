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
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create a 2D representation of beads
    rods = [[1 if x > j else 0 for x in arr] for j in range(max_num)]
    
    # Let the beads "fall" by collapsing columns
    for j in range(max_num):
        # Count beads in each column
        col_sum = sum(rod[j] for rod in rods)
        
        # Reconstruct the column from bottom up
        for rod_index in range(len(rods)):
            rods[rod_index][j] = 1 if rod_index < col_sum else 0
    
    # Extract sorted values
    return [sum(rod) for rod in zip(*rods)]