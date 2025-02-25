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
    # Use the side parameter to get the leftmost matching index if there are duplicates
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
    
    # Length of the transformed string
    n = len(transformed_string)
    
    # Create the first column by sorting the transformed string
    first_column = sorted(transformed_string)
    
    # Create the LF mapping
    lf_mapping = [0] * n
    last_seen = {c: 0 for c in set(first_column)}
    
    for i in range(n):
        c = first_column[i]
        lf_mapping[i] = last_seen[c]
        last_seen[c] += 1
    
    # Reconstruct the original string
    result = []
    current_index = original_index
    
    for _ in range(n):
        # Add the first column character to result
        result.append(first_column[current_index])
        
        # Find the next index using the LF mapping
        current_index = lf_mapping[current_index]
    
    # Return the string without the sentinel character 
    # (The last character will be the sentinel '$')
    return ''.join(result[:-1])