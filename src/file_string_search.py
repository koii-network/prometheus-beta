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
    
    # Initialize list to store matching line numbers
    matching_lines = []
    
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            # Enumerate lines to get both line number and content
            for line_number, line in enumerate(file, 1):
                # Check if search string is in the line
                if search_string in line:
                    matching_lines.append(line_number)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return matching_lines