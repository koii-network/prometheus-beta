def read_file_contents(file_path):
    """
    Read and return the contents of a text file.
    
    Args:
        file_path (str): The path to the text file to be read.
    
    Returns:
        str: The contents of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the file cannot be read due to permission issues.
        IOError: For other input/output related errors.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file {file_path}: {str(e)}")