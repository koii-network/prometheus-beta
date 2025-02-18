def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Bead sort (or gravity sort) works by simulating beads on parallel rods,
    where gravity pulls the beads down to create a sorted arrangement.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If the list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create rods (represented as a 2D list)
    rods = [[1 if x > i else 0 for x in arr] for i in range(max_num)]
    
    # Let the beads fall (gravity)
    for i in range(len(rods)):
        # Count the number of beads in each column
        column_sum = sum(rod[i] for rod in rods)
        
        # Drop the beads
        for j in range(len(arr)):
            rods[i][j] = 1 if j < column_sum else 0
    
    # Reconstruct the sorted array
    sorted_arr = [sum(rod[j] for rod in rods) for j in range(len(arr))]
    
    return sorted_arr