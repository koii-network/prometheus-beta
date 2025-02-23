def remove_empty_lines(input_file, output_file=None):
    """
    Remove empty lines from a given file.

    Args:
        input_file (str): Path to the input file.
        output_file (str, optional): Path to the output file. 
                                    If not provided, modifies the input file in-place.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IOError: For other I/O related errors.
    """
    # Validate input file exists
    try:
        with open(input_file, 'r') as f:
            # Read lines, filtering out empty lines (including lines with only whitespace)
            non_empty_lines = [line for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except PermissionError:
        raise PermissionError(f"Permission denied when reading file: {input_file}")
    except IOError as e:
        raise IOError(f"Error reading file: {input_file}. {str(e)}")

    # Determine output file - use input file if no output specified
    target_file = output_file if output_file else input_file

    # Write non-empty lines to output file
    try:
        with open(target_file, 'w') as f:
            f.writelines(non_empty_lines)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to file: {target_file}")
    except IOError as e:
        raise IOError(f"Error writing to file: {target_file}. {str(e)}")