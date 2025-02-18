def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.
    
    Args:
        file_path (str): Path to the file to search
        search_string (str): String to search for in the file
    
    Returns:
        list: A list of line numbers (1-indexed) where the string is found
    
    Raises:
        FileNotFoundError: If the file does not exist
        TypeError: If file_path or search_string is not a string
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    # Initialize results list
    results = []
    
    try:
        with open(file_path, 'r') as file:
            # Enumerate lines to get line numbers
            for line_number, line in enumerate(file, 1):
                if search_string in line:
                    results.append(line_number)
        
        return results
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")