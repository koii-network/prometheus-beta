def remove_empty_lines(file_path):
    """
    Remove empty lines from a given file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: Path to the modified file with empty lines removed.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are insufficient permissions to read/write the file.
    """
    try:
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Filter out empty lines (including lines with only whitespace)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Write the non-empty lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)
        
        return file_path
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify the file {file_path}.")