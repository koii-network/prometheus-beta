def min_sequence_edit_distance(original, target):
    """
    Determine the minimum number of insertions and removals required 
    to reconstruct the original sequence from the target sequence.
    
    Args:
        original (list): The original sequence to be reconstructed
        target (list): The sequence to transform
    
    Returns:
        int: Minimum number of insertions and removals needed
    """
    # Use Longest Common Subsequence (LCS) approach
    m, n = len(original), len(target)
    
    # Create a DP table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if original[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Length of Longest Common Subsequence
    lcs_length = dp[m][n]
    
    # Total edits = removals from original + insertions from target
    # Removals = elements in original not in LCS
    # Insertions = elements in target not in LCS
    removals = m - lcs_length
    insertions = n - lcs_length
    
    return removals + insertions