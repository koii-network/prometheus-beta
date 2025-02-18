def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Convert strings to lowercase to handle matching case-insensitively
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Initialize a matrix to store substring lengths
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Variables to track the maximum length and ending position
    max_length = 0
    end_position = 0
    
    # Compute the lengths of common substrings
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                
                # Update max length and end position
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_position = i
    
    # Extract the exact substring from the original input
    return str1[end_position - max_length:end_position] if max_length > 0 else ""