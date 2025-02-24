def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the minimum number of operations (insert, delete, replace) 
    required to transform str1 into str2.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        int: Minimum number of edit operations
    """
    # Create a matrix to store edit distances
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of insert, delete, or replace
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # delete
                    dp[i][j-1],      # insert
                    dp[i-1][j-1]     # replace
                )
    
    return dp[m][n]