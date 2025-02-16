def remove_empty_lines(file_path):
    """
    Remove empty lines from a file.
    
    Args:
        file_path (str): Path to the input file.
    
    Returns:
        bool: True if lines were removed, False otherwise.
    """
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove empty lines (including lines with only whitespace)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Check if any lines were removed
        lines_removed = len(lines) != len(non_empty_lines)
        
        # Write back to the file
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)
        
        return lines_removed
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to modify {file_path}.")
    except IOError as e:
        raise IOError(f"An error occurred while processing the file: {e}")