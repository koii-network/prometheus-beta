def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, returns the actual subsequence. 
                                          If False, returns the length. Defaults to False.
    
    Returns:
        int or list: Length of the longest increasing subsequence, 
                     or the subsequence itself based on return_sequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-integer elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return [] if return_sequence else 0
    
    # Validate all elements are integers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be integers or floats")
    
    # Length of the array
    n = len(arr)
    
    # Dynamic programming to track LIS
    # dp[i] stores the length of LIS ending at index i
    dp = [1] * n
    
    # Previous index to track the actual subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # If only length is required
    if not return_sequence:
        return max_length
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.append(arr[current])
        current = prev[current]
    
    # Reverse to get correct order
    return list(reversed(subsequence))