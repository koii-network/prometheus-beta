def pigeonhole_sort(arr):
    """
    Implement the pigeonhole sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for a known range of integers.
    It works by creating 'pigeonholes' (buckets) and distributing elements into these holes,
    then collecting them back in order.
    
    Args:
        arr (list): A list of integers to be sorted
    
    Returns:
        list: A sorted list of integers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if not arr:
        return []
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the range of the input
    min_val = min(arr)
    max_val = max(arr)
    
    # Create pigeonholes
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    
    # Count occurrences of each number
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Collect elements back into sorted array
    sorted_arr = []
    for i in range(range_size):
        while pigeonholes[i] > 0:
            sorted_arr.append(i + min_val)
            pigeonholes[i] -= 1
    
    return sorted_arr