def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, returns the subsequence. 
                                          If False, returns the length. Defaults to False.
    
    Returns:
        int or list: Length of LIS or the actual subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return arr if return_sequence else 1
    
    # Dynamic programming approach
    n = len(arr)
    # Stores the length of LIS ending at each index
    lengths = [1] * n
    # Stores the previous index for reconstructing the subsequence
    prev_indices = [-1] * n
    
    # Compute LIS lengths
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
    
    # Reconstruct the subsequence if required
    if return_sequence:
        subsequence = []
        current = max_index
        while current != -1:
            subsequence.append(arr[current])
            current = prev_indices[current]
        return list(reversed(subsequence))
    
    return max_length