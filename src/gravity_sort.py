def gravity_sort(arr):
    """
    Implement the gravity sort (Bead Sort) algorithm.
    
    Gravity sort works by simulating gravity on a set of beads arranged in rows,
    where each number is represented by a row of beads.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list sorted in ascending order.
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
        ValueError: If input contains negative numbers.
    
    Time Complexity: O(n * max(arr))
    Space Complexity: O(n * max(arr))
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if any(not isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if any(x < 0 for x in arr):
        raise ValueError("Input cannot contain negative numbers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of beads
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * max_num for _ in range(len(arr))]
    
    # Fill the beads representation
    for i, num in enumerate(arr):
        for j in range(num):
            beads[i][j] = 1
    
    # Let the beads "fall" by gravity
    for col in range(max_num):
        # Count total beads in this column
        total_beads = sum(row[col] for row in beads)
        
        # Drop the beads to the bottom
        for row in range(len(beads)):
            beads[row][col] = 1 if row >= len(beads) - total_beads else 0
    
    # Reconstruct the sorted array
    sorted_arr = []
    for row in beads:
        # Count the beads in each row (which represents the sorted number)
        num_beads = sum(row)
        sorted_arr.append(num_beads)
    
    return sorted_arr