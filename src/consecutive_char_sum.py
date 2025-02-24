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
    current_sum = 0
    consecutive_start = False
    
    for i in range(1, len(input_string)):
        # Check if characters are consecutive
        if ord(input_string[i]) == ord(input_string[i-1]) + 1:
            # First time seeing consecutive characters
            if not consecutive_start:
                current_sum = ord(input_string[i-1]) + ord(input_string[i])
                consecutive_start = True
            # Continuing consecutive sequence
            else:
                current_sum += ord(input_string[i])
        else:
            # Not consecutive, reset
            consecutive_start = False
            current_sum = 0
        
        # Update max sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum