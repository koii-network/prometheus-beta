def remove_empty_lines(file_path):
    """
    Remove empty lines from a given file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: Path to the modified file with empty lines removed.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing the file.
        TypeError: If file_path is not a string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove empty lines (lines that are just whitespace or newline)
        non_empty_lines = [line for line in lines if line.strip()]

        # Write non-empty lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)

        return file_path

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")