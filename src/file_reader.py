def read_file_contents(file_path):
    """
    Read and return the contents of a file.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The contents of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are permission issues reading the file.
        IOError: For other I/O related errors when reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")