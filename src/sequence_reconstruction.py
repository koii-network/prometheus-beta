def min_sequence_edits(original, modified):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct an original sequence from a given array.
    
    Args:
        original (list): The original sequence
        modified (list): The modified sequence
    
    Returns:
        int: Minimum number of edits (insertions and removals) needed
    """
    # Use Longest Common Subsequence (LCS) to find the minimum edits
    m, n = len(original), len(modified)
    
    # Create a 2D table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if original[i-1] == modified[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # The minimum number of edits is the total length of sequences 
    # minus twice the length of the longest common subsequence
    lcs_length = dp[m][n]
    min_edits = (m - lcs_length) + (n - lcs_length)
    
    return min_edits