def bead_sort(arr):
    """
    Implement the Bead Sort (Gravity Sort) algorithm.
    
    Bead sort is a natural sorting algorithm that works similar to beads on an abacus
    falling under gravity. It only works for positive integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted
    
    Returns:
        list: A sorted list of integers in ascending order
    
    Raises:
        ValueError: If the input contains negative numbers
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # If input is empty or single element, return as is
    if len(arr) <= 1:
        return arr
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[1 if num > level else 0 for num in arr] for level in range(max_num)]
    
    # Let the beads fall (gravity)
    for level in range(max_num):
        # Count beads in each column
        col_counts = [sum(row[col] for row in beads) for col in range(len(arr))]
        
        # Reconstruct the rows after beads fall
        beads[level] = [1 if col_counts[col] > level else 0 for col in range(len(arr))]
    
    # Count non-zero beads in each column to get sorted values
    return [sum(row[col] for row in beads) for col in range(len(arr))]