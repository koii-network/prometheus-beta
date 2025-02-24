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
    
    # We'll check every possible starting character
    for start in range(len(input_string)):
        current_sum = ord(input_string[start])
        for j in range(start + 1, len(input_string)):
            if ord(input_string[j]) == ord(input_string[j-1]) + 1:
                current_sum += ord(input_string[j])
            else:
                break
        max_sum = max(max_sum, current_sum)
    
    return max_sum