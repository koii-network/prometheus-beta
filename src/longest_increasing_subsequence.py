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
        Specialized Longest Increasing Subsequence algorithm
        """
        n = len(arr)
        
        # Handle single element case
        if n == 1:
            return arr
        
        # Track all possible subsequences
        subsequences = []
        
        def backtrack(start_index, current_sub):
            """
            Recursive backtracking to find all increasing subsequences
            """
            # Add current subsequence to candidates if it's longer than what we have
            if not subsequences or len(current_sub) > len(subsequences[0]):
                subsequences.clear()
                subsequences.append(current_sub[:])
            elif len(current_sub) == len(subsequences[0]):
                # Lexicographically compare
                if current_sub < subsequences[0]:
                    subsequences.clear()
                    subsequences.append(current_sub[:])
            
            # Try to extend subsequence
            for i in range(start_index, n):
                if not current_sub or arr[i] > current_sub[-1]:
                    current_sub.append(arr[i])
                    backtrack(i + 1, current_sub)
                    current_sub.pop()
        
        # Start backtracking
        backtrack(0, [])
        
        return subsequences[0] if subsequences else []
    
    return find_lis(arr)