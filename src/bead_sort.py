def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Bead sort (or gravity sort) is a natural sorting algorithm that works by 
    arranging beads on parallel rods, simulating gravity to sort them.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative numbers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Input must be a list of non-negative integers")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create the "rods" representing the beads
    rods = [[1 if x > k else 0 for x in arr] for k in range(max_num)]
    
    # Let the beads "fall" using gravity
    for rod in rods:
        beads = sum(rod)
        rod[:] = [1] * beads + [0] * (len(rod) - beads)
    
    # Reconstruct the sorted array
    return [sum(rod[i] for rod in rods) for i in range(len(arr))]