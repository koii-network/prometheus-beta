def delete_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a file.
    
    Args:
        input_file (str): Path to the input file
        output_file (str, optional): Path to the output file. 
                                     If not provided, modifies the input file in-place.
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # If no output file is specified, use input file for in-place modification
    if output_file is None:
        output_file = input_file
    
    # Read the input file
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Filter out empty lines (including lines with only whitespace)
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Write non-empty lines to the output file
    try:
        with open(output_file, 'w') as f:
            f.writelines(non_empty_lines)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to {output_file}")