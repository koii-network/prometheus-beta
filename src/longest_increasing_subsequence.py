def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        tuple: A tuple containing two elements:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence (list)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return 0, []
    
    # Validate input contains only numbers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("List must contain only numeric elements")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming arrays
    # lengths[i] stores the length of LIS ending at index i
    lengths = [1] * n
    
    # prev stores the previous index in the LIS for each element
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
        
        # Update max length and max index
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return max_length, subsequence