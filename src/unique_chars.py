def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers without using 
    built-in methods or unique character extraction data structures.
    
    Args:
        number_string (str): A string of numbers
    
    Returns:
        str: A string containing only the unique characters from the input
    """
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # Use a simple character tracking approach with a boolean array
    # We'll use a 10-element boolean array to track digits 0-9
    seen_chars = [False] * 10
    unique_result = ""
    
    # Iterate through each character in the input string
    for char in number_string:
        # Convert character to integer index
        try:
            index = int(char)
        except ValueError:
            raise ValueError(f"Invalid input: '{char}' is not a numeric character")
        
        # If this character hasn't been seen before, add it to result
        if not seen_chars[index]:
            seen_chars[index] = True
            unique_result += char
    
    return unique_result