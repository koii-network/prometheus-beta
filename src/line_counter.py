def count_file_lines(file_path):
    """
    Count the number of lines in a given file.
    
    Args:
        file_path (str): Path to the file to be counted.
    
    Returns:
        int: Number of lines in the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Use list comprehension with readlines() and count the length
            return len(file.readlines())
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")