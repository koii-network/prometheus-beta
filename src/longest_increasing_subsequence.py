def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Validate list contains only numbers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution
    n = len(arr)
    # Length of longest increasing subsequence ending at each index
    lengths = [1] * n
    # Previous index tracking for reconstruction
    prev_indices = [None] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            # If current element is greater and adding to subsequence increases length
            # or if length is same but current element is smaller (to get lexicographically smallest subsequence)
            if arr[i] > arr[j] and (lengths[i] < lengths[j] + 1 or 
                                    (lengths[i] == lengths[j] + 1 and arr[i] < arr[prev_indices[i]] if prev_indices[i] is not None else False)):
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
    
    # Find the index of the maximum length
    max_length = max(lengths)
    max_length_indices = [i for i, x in enumerate(lengths) if x == max_length]
    
    # Choose the lexicographically smallest subsequence
    max_length_index = min(max_length_indices, key=lambda i: arr[i])
    
    # Reconstruct the subsequence
    subsequence = []
    current_index = max_length_index
    while current_index is not None:
        subsequence.insert(0, arr[current_index])
        current_index = prev_indices[current_index]
    
    return subsequence