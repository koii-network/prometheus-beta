def read_file_contents(file_path):
    """
    Read and return the contents of a file.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The contents of the file as a string.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IsADirectoryError: If the path points to a directory instead of a file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IsADirectoryError:
        raise IsADirectoryError(f"{file_path} is a directory, not a file.")