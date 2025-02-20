def max_consecutive_characters_sum(input_string):
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
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize variables
    max_sum = 0
    current_sum = 0
    current_consecutive_chars = input_string[0]
    
    for i in range(len(input_string)):
        # If we're at the start or the current character is consecutive to the previous one
        if (i == 0) or (ord(input_string[i]) == ord(input_string[i-1]) + 1):
            current_sum += ord(input_string[i])
            current_consecutive_chars += input_string[i]
        else:
            # Reset sum and consecutive characters if not consecutive
            max_sum = max(max_sum, current_sum)
            current_sum = ord(input_string[i])
            current_consecutive_chars = input_string[i]
    
    # Check the last sequence
    max_sum = max(max_sum, current_sum)
    
    return max_sum