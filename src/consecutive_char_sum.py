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
    
    max_sum = current_sum = 0
    
    for i in range(len(input_string)):
        # First character in a potential consecutive sequence
        if i == 0 or ord(input_string[i]) != ord(input_string[i-1]) + 1:
            current_start = ord(input_string[i])
            current_sum = current_start
        else:
            # Continue the consecutive sequence
            current_sum += ord(input_string[i])
        
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum