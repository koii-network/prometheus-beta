def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the maximum length and ending position
    max_length = 0
    end_index = 0
    
    # Fill the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Only match if chars are exactly the same (case-sensitive)
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # Return the longest common substring
    # If no match found, return empty string
    return str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""