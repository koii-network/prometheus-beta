def read_file_contents(file_path):
    """
    Read and return the contents of a text file.
    
    Args:
        file_path (str): The path to the text file to be read.
    
    Returns:
        str: The contents of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file {file_path}: {str(e)}")