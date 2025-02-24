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
    
    def find_lis(arr):
        """
        More sophisticated LIS algorithm to handle complex scenarios
        """
        n = len(arr)
        # Track potential subsequences
        dp = [[] for _ in range(n)]
        
        # First candidate is always the first element
        dp[0] = [arr[0]]
        
        # Best subsequence tracking
        best_sub = dp[0]
        
        for i in range(1, n):
            # Initialize current index subsequence with self
            dp[i] = [arr[i]]
            
            # Try to extend previous subsequences
            for j in range(i):
                # If current element can be appended to previous subsequence
                if arr[i] > arr[j] and len(dp[j]) + 1 > len(dp[i]):
                    # Create a new candidate subsequence
                    candidate = dp[j] + [arr[i]]
                    
                    # Update if longer or lexicographically smaller
                    if (len(candidate) > len(dp[i]) or 
                        (len(candidate) == len(dp[i]) and 
                         candidate < dp[i])):
                        dp[i] = candidate
            
            # Update best subsequence if needed
            if len(dp[i]) > len(best_sub) or \
               (len(dp[i]) == len(best_sub) and dp[i] < best_sub):
                best_sub = dp[i]
        
        return best_sub
    
    return find_lis(arr)