def burrows_wheeler_transform(input_text):
    """
    Perform the Burrows-Wheeler Transform on the input text.
    
    The Burrows-Wheeler Transform is a critical step in data compression 
    that rearranges the characters of a text to improve compression efficiency.
    
    Args:
        input_text (str): The input string to transform
    
    Returns:
        tuple: A tuple containing the Burrows-Wheeler transformed string 
               and the index of the original rotation
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Validate input
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string")
    
    if not input_text:
        raise ValueError("Input string cannot be empty")
    
    # Add terminator character (typically '$')
    text = input_text + '$'
    
    # Generate all rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original input in the sorted rotations
    original_index = sorted_rotations.index(text)
    
    return bwt_result, original_index

def inverse_burrows_wheeler_transform(bwt_input):
    """
    Perform the inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt_input (tuple): A tuple containing the Burrows-Wheeler transformed 
                           string and the original index
    
    Returns:
        str: The original text before transformation
    
    Raises:
        TypeError: If input is not a tuple or invalid type
        ValueError: If input is invalid
    """
    # Validate input
    if not isinstance(bwt_input, tuple) or len(bwt_input) != 2:
        raise TypeError("Input must be a tuple of (bwt_string, original_index)")
    
    bwt_text, original_index = bwt_input
    
    if not isinstance(bwt_text, str) or not bwt_text:
        raise ValueError("Burrows-Wheeler text must be a non-empty string")
    
    # Create first and last columns
    first_column = sorted(bwt_text)
    n = len(bwt_text)
    
    # Create next array
    next_arr = [0] * n
    # Auxiliary array to handle duplicate characters
    char_count = {}
    
    for i in range(n):
        char = first_column[i]
        if char not in char_count:
            char_count[char] = 0
        # Find the correct occurrence of this character in the first column
        for j in range(n):
            if bwt_text[j] == char and char_count[char] == 0:
                next_arr[i] = j
                break
        char_count[char] += 1
    
    # Reconstruct the original text
    result = []
    current = original_index
    
    for _ in range(n):
        result.append(bwt_text[current])
        current = next_arr[current]
    
    # Reverse and convert to string, remove terminator
    original = ''.join(reversed(result))[:-1]
    
    return original