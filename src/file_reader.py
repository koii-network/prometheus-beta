def read_file_contents(file_path):
    """
    Read and return the contents of a file.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The contents of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be read due to permissions.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IOError as e:
        raise IOError(f"An error occurred while reading {file_path}: {e}")