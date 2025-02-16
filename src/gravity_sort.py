def gravity_sort(arr):
    """
    Implement the gravity sort (Bead sort) algorithm.
    
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
    
    # If the list is empty or has only one element, return it as-is
    if len(arr) <= 1:
        return arr
    
    # Find the maximum number to determine the number of beads
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[1 if num > j else 0 for j in range(max_num)] for num in arr]
    
    # Let the beads "fall" using gravity
    for j in range(max_num):
        # Count beads in each column
        column_sum = sum(row[j] for row in beads)
        
        # Update beads after "falling"
        for i in range(len(beads)):
            beads[i][j] = 1 if i < column_sum else 0
    
    # Convert back to original numbers
    sorted_arr = [sum(row) for row in beads]
    
    return sorted_arr