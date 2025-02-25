def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        tuple: A tuple containing:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence (list)
    """
    if not arr:
        return 0, []
    
    # Dynamic programming to track lengths
    n = len(arr)
    lengths = [1] * n  # Each element starts with a subsequence length of 1
    prev_indices = [-1] * n  # Track previous elements in the subsequence
    
    # Find the longest increasing subsequence length
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
        
        # Update max length and index if needed
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev_indices[current]
    
    return max_length, subsequence