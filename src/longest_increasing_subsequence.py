def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    A subsequence is a sequence that can be derived from an array by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming approach
    n = len(arr)
    # Lengths of increasing subsequences
    lengths = [1] * n
    # Previous indices to track the subsequence
    prev_indices = [-1] * n
    
    # Compute the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev_indices[i] = j
    
    # Find the index of the end of the longest subsequence
    max_length_index = lengths.index(max(lengths))
    
    # Reconstruct the subsequence
    subsequence = []
    while max_length_index != -1:
        subsequence.insert(0, arr[max_length_index])
        max_length_index = prev_indices[max_length_index]
    
    return subsequence