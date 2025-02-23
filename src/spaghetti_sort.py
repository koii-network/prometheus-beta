def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort algorithm.

    Spaghetti Sort (also known as Bead Sort) is a sorting algorithm that works 
    by simulating the physical arrangement of beads or spaghetti strands.

    Args:
        arr (list): A list of non-negative integers to be sorted.

    Returns:
        list: A new list with elements sorted in ascending order.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element is not a non-negative integer.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Check for non-negative integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If only one element, return it
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of "strands"
    max_num = max(arr)
    
    # Create the "abacus" representation
    abacus = [0] * (max_num + 1)
    
    # Count occurrences of each number
    for num in arr:
        abacus[num] += 1
    
    # Reconstruct the sorted list
    sorted_arr = []
    for num, count in enumerate(abacus):
        sorted_arr.extend([num] * count)
    
    return sorted_arr