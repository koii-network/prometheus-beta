def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for lists with a known range of values.
    It works by creating 'pigeonholes' (buckets) for each possible value and placing 
    elements into these holes, then reconstructing the sorted list.
    
    Args:
        arr (list): A list of integers to be sorted
    
    Returns:
        list: A sorted list of integers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
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
    
    # Find the range of the input
    min_val = min(arr)
    max_val = max(arr)
    
    # Create pigeonholes (a range of buckets)
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    
    # Count occurrences of each number
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted list
    sorted_arr = []
    for i in range(range_size):
        # Add each number as many times as it appears
        while pigeonholes[i] > 0:
            sorted_arr.append(i + min_val)
            pigeonholes[i] -= 1
    
    return sorted_arr