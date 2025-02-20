def max_consecutive_substring_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        int: The maximum sum of consecutive characters
    
    Raises:
        ValueError: If input is not a string
    """
    # Validate input
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    # If string is empty, return 0
    if not input_string:
        return 0
    
    # Convert characters to their numeric values
    char_values = [ord(char) for char in input_string]
    
    # Track max sum and current sum
    max_sum = current_sum = char_values[0]
    
    for i in range(1, len(char_values)):
        # Check if current character is consecutive with previous character
        if char_values[i] == char_values[i-1] + 1:
            current_sum += char_values[i]
        else:
            # Reset current sum to current character value
            current_sum = char_values[i]
        
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum