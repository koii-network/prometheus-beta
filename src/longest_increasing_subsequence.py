def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        tuple: A tuple containing:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence itself (list)
    """
    if not arr:
        return 0, []
    
    # Dynamic programming approach
    n = len(arr)
    # Length of LIS ending at each index
    lengths = [1] * n 
    # Previous index tracking for reconstruction
    prev_indices = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
        
        # Track the overall maximum
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