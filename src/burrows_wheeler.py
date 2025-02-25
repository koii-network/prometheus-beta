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
    
    # Create the first and last column of the transformation table
    length = len(transformed_string)
    
    # Count the occurrences of each character
    char_counts = {}
    for char in transformed_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Create the first column (sorted characters)
    first_column = sorted(transformed_string)
    
    # Create a next array for tracking
    next_array = [0] * length
    char_positions = {char: 0 for char in set(first_column)}
    
    for i in range(length):
        current_char = first_column[i]
        next_array[i] = char_positions[current_char]
        char_positions[current_char] += 1
    
    # Reconstruct the original string
    result = []
    current_index = original_index
    
    for _ in range(length):
        result.append(first_column[current_index])
        current_index = next_array[current_index]
    
    # Remove the sentinel character and return the original string
    return ''.join(result[:-1])