def bead_sort(arr):
    """
    Implement the bead sort algorithm for positive integers.
    
    Args:
        arr (list): A list of positive integers to be sorted.
    
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
    
    # Create the abacus representation
    abacus = []
    for num in arr:
        # Create a row with a number of beads equal to the input number
        abacus.append([1] * num + [0] * (max_num - num))
    
    # Perform the "gravity" operation
    for col in range(max_num):
        column_sum = sum(row[col] for row in abacus)
        
        # Drop the beads from top to bottom
        for row in range(len(abacus)):
            abacus[row][col] = 1 if column_sum > row else 0
    
    # Reconstruct the sorted list
    result = []
    for row in abacus:
        result.append(sum(row))
    
    return result