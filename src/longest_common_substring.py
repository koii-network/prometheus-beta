def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring, or an empty string if no common substring exists
    """
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Initialize matrix for dynamic programming
    m, n = len(str1), len(str2)
    # Matrix to store lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Fill the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # Extract and return the longest common substring
    return str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""