def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Try to ensure elements are comparable
    try:
        # Dynamic Programming approach
        n = len(arr)
        # Initialize lengths of increasing subsequence for each index
        lengths = [1] * n
        # Tracks previous index for reconstruction
        prev_indices = [-1] * n
        
        # Find the length of LIS and track previous indices
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
        result = []
        current = max_index
        while current != -1:
            result.append(arr[current])
            current = prev_indices[current]
        
        return list(reversed(result))
    
    except TypeError:
        raise ValueError("List contains elements that cannot be compared")