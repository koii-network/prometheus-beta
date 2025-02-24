def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the minimum number of operations (insert, delete, replace) 
    required to transform str1 into str2.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The minimum edit distance between str1 and str2
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # If either string is empty, return length of the other string
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Create a matrix to store edit distances
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Initialize first row and column
    for i in range(len(str1) + 1):
        dp[i][0] = i
    for j in range(len(str2) + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters are the same, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of insert, delete, or replace
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # deletion
                    dp[i][j-1],      # insertion
                    dp[i-1][j-1]     # replacement
                )
    
    # Return the bottom-right cell which contains the edit distance
    return dp[len(str1)][len(str2)]