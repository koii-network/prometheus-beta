def read_text_file(file_path):
    """
    Read and return the contents of a text file.
    
    Args:
        file_path (str): Path to the text file to be read.
    
    Returns:
        str: Contents of the text file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are permission issues reading the file.
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
        raise IOError(f"An error occurred while reading {file_path}: {str(e)}")