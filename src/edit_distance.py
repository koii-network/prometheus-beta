def compute_edit_distance(str1: str, str2: str) -> int:
    """
    Compute the minimum number of edits (insertions, deletions, or substitutions) 
    required to transform str1 into str2 using dynamic programming.

    Args:
        str1 (str): The source string
        str2 (str): The target string

    Returns:
        int: The minimum number of edits required

    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")

    # Handle empty string cases
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    # Create dynamic programming matrix
    # dp[i][j] represents the edit distance between str1[:i] and str2[:j]
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Initialize first row and column
    for i in range(len(str1) + 1):
        dp[i][0] = i
    for j in range(len(str2) + 1):
        dp[0][j] = j

    # Fill the dp matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of three operations:
                # 1. Insert: dp[i][j-1] + 1
                # 2. Delete: dp[i-1][j] + 1
                # 3. Substitute: dp[i-1][j-1] + 1
                dp[i][j] = 1 + min(
                    dp[i][j-1],      # Insert
                    dp[i-1][j],      # Delete
                    dp[i-1][j-1]     # Substitute
                )

    # Return the final edit distance
    return dp[len(str1)][len(str2)]