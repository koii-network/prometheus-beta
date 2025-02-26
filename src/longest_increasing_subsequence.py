def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, return the actual subsequence.
                                          If False, return the length. Defaults to False.
    
    Returns:
        int or list: Length of the longest increasing subsequence or 
                     the actual subsequence, depending on return_sequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    
    Examples:
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80], return_sequence=True)
        [10, 22, 33, 50, 60, 80]
        >>> longest_increasing_subsequence([])
        0
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return [] if return_sequence else 0
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # Length of LIS
    n = len(arr)
    # Store lengths of increasing subsequences
    lengths = [1] * n
    # Store previous indices to reconstruct the sequence
    prev_indices = [None] * n
    
    # Dynamic Programming to find LIS length
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
                
                # Track the overall maximum length
                if lengths[i] > max_length:
                    max_length = lengths[i]
                    max_index = i
    
    # If only length is requested, return length
    if not return_sequence:
        return max_length
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current is not None:
        subsequence.insert(0, arr[current])
        current = prev_indices[current]
    
    return subsequence