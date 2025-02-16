def find_longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store substring lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    end_index = 0
    
    # Dynamic programming to find longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # Return the longest common substring
    return str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""