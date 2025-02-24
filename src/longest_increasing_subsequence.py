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
    
    # Dynamic Programming approach with more comprehensive subsequence tracking
    n = len(arr)
    # lengths[i] is the length of the LIS ending at index i
    lengths = [1] * n
    # Stores the index of the previous element in the LIS
    prev_indices = [-1] * n
    
    # Track the best overall subsequence
    max_length = 1
    max_index = 0
    
    # Compute optimal subsequence
    for i in range(1, n):
        for j in range(i):
            # If current element is greater and including it creates a longer subsequence
            if arr[i] > arr[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    prev_indices[i] = j
                
                # Update overall best subsequence
                if lengths[i] > max_length:
                    max_length = lengths[i]
                    max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev_indices[current]
    
    return subsequence