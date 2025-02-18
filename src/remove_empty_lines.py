def remove_empty_lines(file_path):
    """
    Remove empty lines from a file and write the result back to the same file.
    
    Args:
        file_path (str): Path to the file to remove empty lines from.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are permission issues reading or writing the file.
    """
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove empty lines (lines that are just whitespace or newline characters)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Write back to the same file
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {file_path}.")