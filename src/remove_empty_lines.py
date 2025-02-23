def remove_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a given file.
    
    Args:
        input_file (str): Path to the input file to remove empty lines from.
        output_file (str, optional): Path to write the modified file. 
                                     If None, modifies the input file in-place.
    
    Returns:
        int: Number of empty lines removed
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except PermissionError:
        raise PermissionError(f"Permission denied when reading file: {input_file}")
    
    # Count and filter out empty lines
    empty_line_count = sum(1 for line in lines if line.strip() == '')
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Determine output destination
    target_file = output_file if output_file is not None else input_file
    
    # Write non-empty lines
    try:
        with open(target_file, 'w') as f:
            f.writelines(non_empty_lines)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to file: {target_file}")
    
    return empty_line_count