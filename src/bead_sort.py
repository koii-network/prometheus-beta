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
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create the abacus representation as a vertical list of columns
    # Each column represents a rod with the number of beads
    rods = [0] * max_num
    
    # Drop beads on each rod based on the input values
    for value in arr:
        for j in range(value):
            rods[j] += 1
    
    # Reconstruct the sorted list
    result = []
    for i in range(len(arr)):
        # Find how many rods have a valid bead at this level
        result.append(sum(1 for rod in rods if rod > i))
    
    return result