def read_file_line_by_line(file_path):
    """
    Read a file line by line and return its contents as a list of lines.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        list: A list of lines from the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
        TypeError: If the file_path is not a string.
    """
    # Validate input type
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    try:
        # Open the file and read lines
        with open(file_path, 'r') as file:
            # Read all lines, stripping trailing newline characters
            lines = [line.rstrip('\n') for line in file]
        
        return lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {str(e)}")