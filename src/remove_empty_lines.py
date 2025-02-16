def remove_empty_lines(input_file, output_file=None):
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
        IOError: If there are issues reading or writing files
    """
    try:
        # Read the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines (including lines with only whitespace)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Determine the output file
        target_file = output_file if output_file else input_file
        
        # Write non-empty lines back to the file
        with open(target_file, 'w') as f:
            f.writelines(non_empty_lines)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except IOError as e:
        raise IOError(f"Error processing file: {e}")