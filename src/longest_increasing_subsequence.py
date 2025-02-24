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
    
    # Handles complex LIS scenarios
    def generate_subsequences(arr):
        """Generate potential subsequences"""
        n = len(arr)
        # Dynamic programming to track potential subsequences
        dp = [[[] for _ in range(n)] for _ in range(n)]
        
        # Initialize single-element subsequences
        for i in range(n):
            dp[i][i] = [arr[i]]
        
        # Build subsequences
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                for k in range(start, end):
                    # If we can extend a subsequence
                    if arr[end] > arr[k]:
                        for sub in dp[start][k]:
                            if arr[end] > sub[-1]:
                                candidate = sub + [arr[end]]
                                # Prefer longer or more interesting subsequences
                                if (len(candidate) > len(dp[start][end]) or 
                                    (len(candidate) == len(dp[start][end]) and 
                                     candidate[-1] < dp[start][end][-1])):
                                    dp[start][end] = candidate
        
        # Find the best subsequence
        best_sub = max((sub for row in dp for sub in row if sub), 
                       key=lambda x: (len(x), -x[-1]), 
                       default=[])
        return best_sub
    
    return generate_subsequences(arr)