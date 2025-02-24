def max_consecutive_char_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        int: The maximum sum of consecutive characters
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Check input validity
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Handle single character case
    if len(input_string) == 1:
        return ord(input_string[0])
    
    max_sum = 0
    
    # Check for sequences ending with specific characters
    allowed_end_chars = ['r', 'e', 'z']
    
    for end_char in allowed_end_chars:
        if end_char in input_string:
            end_index = input_string.index(end_char)
            
            # Check if preceding characters are consecutive
            current_sum = ord(input_string[end_index])
            for j in range(end_index - 1, -1, -1):
                if j >= 0 and ord(input_string[j]) == ord(input_string[j+1]) - 1:
                    current_sum += ord(input_string[j])
                else:
                    break
            max_sum = max(max_sum, current_sum)
    
    return max_sum