def read_file_contents(file_path):
    """
    Read and return the contents of a text file.
    
    Args:
        file_path (str): Path to the text file to be read.
    
    Returns:
        str: Contents of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IOError: For other I/O related errors.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")