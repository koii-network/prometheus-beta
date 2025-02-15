def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein Distance (Edit Distance) between two strings.
    
    The Edit Distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into another.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The minimum number of edits required to transform str1 into str2
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, return length of the other string
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Create a matrix to store edit distances
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Initialize first row and column
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j
    
    # Fill the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                # Choose minimum of insert, delete, or substitute
                matrix[i][j] = 1 + min(
                    matrix[i-1][j],      # deletion
                    matrix[i][j-1],      # insertion
                    matrix[i-1][j-1]     # substitution
                )
    
    # Return the bottom-right cell which contains the edit distance
    return matrix[len(str1)][len(str2)]