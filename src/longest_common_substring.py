def find_longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring, or empty string if no common substring exists
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Dynamic Programming approach to find longest common substring
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    
    # Extract and return the longest common substring
    return str1[end_index - max_length:end_index]