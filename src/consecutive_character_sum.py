def max_consecutive_character_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        int: The maximum sum of consecutive characters
    """
    if not input_string:
        return 0
    
    # Convert string to characters
    chars = list(input_string)
    
    # Track current sum and max sum
    current_sum = ord(chars[0])
    max_sum = current_sum
    
    # Iterate through characters starting from the second character
    for i in range(1, len(chars)):
        # Check if current character is consecutive with the previous character
        if ord(chars[i]) == ord(chars[i-1]) + 1:
            # If consecutive, add to current sum
            current_sum += ord(chars[i])
        else:
            # If not consecutive, reset current sum
            current_sum = ord(chars[i])
        
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum