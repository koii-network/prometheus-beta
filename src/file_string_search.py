def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.
    
    Args:
        file_path (str): Path to the file to be searched
        search_string (str): String to search for in the file
    
    Returns:
        list: A list of line numbers (1-indexed) where the string is found
    
    Raises:
        FileNotFoundError: If the specified file does not exist
        TypeError: If file_path or search_string are not strings
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    # Check if file exists
    try:
        with open(file_path, 'r') as file:
            # Search through file lines
            matches = []
            for line_num, line in enumerate(file, 1):
                if search_string in line:
                    matches.append(line_num)
            
            return matches
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")