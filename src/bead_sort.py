def bead_sort(arr):
    """
    Implement the Bead Sort algorithm (Gravity Sort) for positive integers.
    
    Bead Sort works by visualizing numbers as beads on parallel rods, 
    then letting gravity pull them down to create a sorted arrangement.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Bead sort only works with non-negative integers")
    
    # If input is empty or single element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rods
    max_num = max(arr)
    
    # Create the initial "abacus" representation
    # Each rod represents a potential bead position
    rods = [0] * max_num
    
    # Place beads on rods based on input numbers
    for num in arr:
        for i in range(num):
            rods[i] += 1
    
    # Collect sorted numbers from the rods
    sorted_arr = []
    for i in range(len(rods) - 1, -1, -1):
        sorted_arr.extend([i + 1] * rods[i])
    
    return sorted_arr