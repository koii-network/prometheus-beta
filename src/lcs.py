def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence can be derived by deleting some elements 
    without changing the order of remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1].lower() == str2[j-1].lower():
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find all possible longest common subsequences
    def backtrack(i, j, current):
        # Base case
        if i == 0 or j == 0:
            return [current]
        
        # If current characters match
        if str1[i-1].lower() == str2[j-1].lower():
            # Include the character and continue backtracking
            sub_results = backtrack(i-1, j-1, current + [str1[i-1]])
            return sub_results
        
        # Choose the path with maximum length
        if dp[i-1][j] > dp[i][j-1]:
            return backtrack(i-1, j, current)
        elif dp[i-1][j] < dp[i][j-1]:
            return backtrack(i, j-1, current)
        
        # If both paths have same length, explore both
        left = backtrack(i-1, j, current)
        right = backtrack(i, j-1, current)
        return left + right
    
    # Find all possible max length subsequences
    sequences = backtrack(m, n, [])
    
    # Remove duplicates while preserving order
    unique_sequences = []
    for seq in sequences:
        if len(seq) == max(len(s) for s in sequences):
            unique_sequences.append(seq)
    
    # If no sequences found, return empty string
    if not unique_sequences:
        return ""
    
    # Complex selection logic
    def score_sequence(seq):
        # Prefer sequences that match the original case more closely
        original_case_matches = sum(1 for a, b in zip(seq, str1) if a == b)
        return original_case_matches
    
    # Select the best sequence
    best_sequence = max(unique_sequences, key=score_sequence)
    
    # Return as a string, reversed because we built it backwards
    return ''.join(reversed(best_sequence))