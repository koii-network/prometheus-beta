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
    
    # Length of dynamic programming table
    n = len(arr)
    
    # Dynamic programming tables
    # lengths[i] stores the length of LIS ending at index i
    lengths = [1] * n
    
    # predecessors to track the actual subsequence
    predecessors = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
    
    # Find the index of the maximum length
    max_length_index = lengths.index(max(lengths))
    max_length = lengths[max_length_index]
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = predecessors[current]
    
    return max_length, subsequence