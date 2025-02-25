def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.

    Args:
        file_path (str): Path to the file to search in.
        search_string (str): The string to search for.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If file_path or search_string is not a string.
        ValueError: If search_string is empty.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    # Check for empty search string
    if not search_string:
        raise ValueError("search_string cannot be empty")
    
    # Initialize results list
    matching_lines = []
    
    # Open and read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Enumerate to get line numbers (1-indexed)
            for line_number, line in enumerate(file, 1):
                # Check if search string is in the line
                if search_string in line:
                    matching_lines.append(line_number)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return matching_lines