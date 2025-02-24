def longest_common_subsequence(seq1: str, seq2: str) -> str:
    """
    Find the Longest Common Subsequence (LCS) between two sequences.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        seq1 (str): First input sequence
        seq2 (str): Second input sequence
    
    Returns:
        str: The longest common subsequence
    
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        'ADH'
        >>> longest_common_subsequence("", "ABC")
        ''
        >>> longest_common_subsequence("ABC", "")
        ''
    """
    # Handle edge cases of empty sequences
    if not seq1 or not seq2:
        return ''
    
    # Create a matrix to store LCS lengths
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs.append(seq1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the reversed LCS (since we built it backwards)
    return ''.join(reversed(lcs))