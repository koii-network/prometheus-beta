def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an algorithm similar to counting sort that is efficient 
    when the range of input values is not significantly larger than the number of items.
    
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
    if len(arr) == 0:
        return arr
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the range of the input
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # Create pigeonholes (buckets)
    pigeonholes = [0] * range_size
    
    # Count occurrences of each number
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_size):
        # Add each number its counted number of times
        while pigeonholes[i] > 0:
            sorted_arr.append(i + min_val)
            pigeonholes[i] -= 1
    
    return sorted_arr