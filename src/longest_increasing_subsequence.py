def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): A list of numbers.
    
    Returns:
        list: The longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming array to store lengths of increasing subsequences
    dp = [1] * n
    
    # Previous index array to track the subsequence
    prev = [-1] * n
    
    # Track the index of the maximum length subsequence
    max_length_index = 0
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length index if current subsequence is longer
        if dp[i] > dp[max_length_index]:
            max_length_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence