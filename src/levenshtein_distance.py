def compute_levenshtein_distance(str1: str, str2: str) -> int:
    """
    Compute the Levenshtein distance between two strings using dynamic programming.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The minimum number of single-character edits (insertions, deletions, 
             or substitutions) required to transform str1 into str2
    
    Raises:
        TypeError: If input is not a string
    """
    # Input validation
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, the distance is the length of the other string
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Create a matrix to store edit distances
    # Dimensions are (len(str1) + 1) x (len(str2) + 1)
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Initialize first row and column
    for i in range(len(str1) + 1):
        dp[i][0] = i
    for j in range(len(str2) + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insertion, deletion, or substitution
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # deletion
                    dp[i][j-1],      # insertion
                    dp[i-1][j-1]     # substitution
                )
    
    # Return the bottom-right cell which contains the total edit distance
    return dp[len(str1)][len(str2)]