def remove_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a file.
    
    Args:
        input_file (str): Path to the input file
        output_file (str, optional): Path to the output file. 
                                     If not provided, overwrites the input file.
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    try:
        # Read the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Filter out empty lines (lines that are just whitespace)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Determine output file path
        output_path = output_file if output_file else input_file
        
        # Write non-empty lines to the output file
        with open(output_path, 'w') as f:
            f.writelines(non_empty_lines)
        
        return len(lines) - len(non_empty_lines)  # Return number of empty lines removed
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except PermissionError:
        raise PermissionError(f"Permission denied when processing file: {input_file}")