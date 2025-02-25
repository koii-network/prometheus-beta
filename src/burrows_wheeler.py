def burrows_wheeler_transform(input_string):
    """
    Perform the Burrows-Wheeler Transform on the input string.
    
    The Burrows-Wheeler Transform is a reversible string transformation used 
    in data compression algorithms. It rearranges the characters of a string 
    to improve compression efficiency.
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        tuple: A tuple containing:
            - The transformed string (Burrows-Wheeler Transform result)
            - The index of the original string in the sorted rotations
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Add a sentinel character to mark the end of string
    modified_string = input_string + '$'
    
    # Generate all rotations of the string
    rotations = [modified_string[i:] + modified_string[:i] for i in range(len(modified_string))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation to form the BWT
    transformed_string = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original string in the sorted rotations
    original_index = sorted_rotations.index(modified_string)
    
    return transformed_string, original_index

def inverse_burrows_wheeler_transform(transformed_string, original_index):
    """
    Reverse the Burrows-Wheeler Transform to recover the original string.
    
    Args:
        transformed_string (str): The Burrows-Wheeler transformed string
        original_index (int): The index of the original string in sorted rotations
    
    Returns:
        str: The original string before transformation
    
    Raises:
        TypeError: If inputs are of incorrect type
        ValueError: If transformed string is empty
    """
    # Input validation
    if not isinstance(transformed_string, str):
        raise TypeError("Transformed string must be a string")
    
    if not isinstance(original_index, int):
        raise TypeError("Original index must be an integer")
    
    if not transformed_string:
        raise ValueError("Transformed string cannot be empty")
    
    # Create lists for tracking
    n = len(transformed_string)
    first_column = sorted(transformed_string)
    
    # Create a mapping to track the next indices
    next_indices = [0] * n
    char_counts = {}
    
    # Compute the next indices
    for i in range(n):
        current_char = first_column[i]
        current_count = char_counts.get(current_char, 0)
        char_count_in_last = transformed_string.count(current_char)
        
        # Find the correct index for this character in the last column
        matches = [j for j in range(n) if transformed_string[j] == current_char]
        next_indices[i] = matches[current_count]
        
        char_counts[current_char] = current_count + 1
    
    # Reconstruct the original string
    result = []
    current_index = original_index
    
    for _ in range(n):
        result.append(first_column[current_index])
        current_index = next_indices[current_index]
    
    # Return the string without the sentinel character
    return ''.join(result[:-1])