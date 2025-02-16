def gravity_sort(arr):
    """
    Implement the gravity sort algorithm (also known as Bead Sort or Bucket Sort).
    
    This algorithm simulates gravity acting on a set of beads/elements, 
    where each element drops down as far as possible.
    
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
    
    # If the list is empty or has only one element, return it as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of "rows"
    max_num = max(arr)
    
    # Create a 2D representation of beads
    beads = [[0] * len(arr) for _ in range(max_num + 1)]
    
    # Place beads based on input array
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # Let gravity act - drop beads down
    sorted_arr = []
    for row in beads:
        # Count beads in each column and add to sorted array
        col_count = sum(row)
        sorted_arr.extend([col_count] * col_count)
    
    return sorted_arr