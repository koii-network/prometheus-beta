def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a given file.

    Args:
        file_path (str): Path to the file to search in.
        search_string (str): The string to search for.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If file_path or search_string are not strings.
        ValueError: If search_string is empty.
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    if not search_string:
        raise ValueError("search_string cannot be empty")
    
    # Attempt to read and search the file
    try:
        found_lines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if search_string in line:
                    found_lines.append(line_num)
        
        return found_lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")