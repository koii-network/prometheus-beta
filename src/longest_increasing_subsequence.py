def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution
    # Initialize lengths and predecessors
    n = len(arr)
    lengths = [1] * n  # Each element is at least a subsequence of length 1
    predecessors = [None] * n  # Track previous elements to reconstruct subsequence
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
    
    # Find the index of the maximum length subsequence
    max_length_index = lengths.index(max(lengths))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current is not None:
        subsequence.insert(0, arr[current])
        current = predecessors[current]
    
    return subsequence