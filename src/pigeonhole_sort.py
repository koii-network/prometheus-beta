def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for lists with a small range of values.
    It works by creating 'pigeonholes' (buckets) for each possible value and distributing 
    the input elements into these holes, then collecting them back in order.
    
    Args:
        arr (list): The input list of comparable elements to be sorted.
    
    Returns:
        list: A new sorted list with the same elements as the input.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    
    Time Complexity: O(n + range)
    Space Complexity: O(n + range)
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    try:
        # Find the range of the input
        min_val = min(arr)
        max_val = max(arr)
    except TypeError:
        raise ValueError("List contains incomparable elements")
    
    # Create pigeonholes (buckets)
    range_val = max_val - min_val + 1
    holes = [[] for _ in range(range_val)]
    
    # Distribute input into pigeonholes
    for num in arr:
        holes[num - min_val].append(num)
    
    # Collect elements from pigeonholes
    sorted_arr = []
    for hole in holes:
        sorted_arr.extend(hole)
    
    return sorted_arr