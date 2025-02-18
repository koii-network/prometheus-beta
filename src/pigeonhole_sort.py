def pigeonhole_sort(arr):
    """
    Implement the pigeonhole sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for lists with a small range of values.
    It works by distributing elements into a set of "pigeonholes" and then collecting them back.
    
    Args:
        arr (list): The input list of integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find range of values
    min_val = min(arr)
    max_val = max(arr)
    
    # Create pigeonholes
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    
    # Count occurrences of each value
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct sorted array
    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * pigeonholes[i])
    
    return sorted_arr