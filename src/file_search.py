def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.

    Args:
        file_path (str): Path to the file to be searched.
        search_string (str): The string to search for in the file.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
              Returns an empty list if the string is not found.

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
    
    # Validate search string
    if not search_string:
        raise ValueError("search_string cannot be empty")
    
    # Try to open and search the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Use list comprehension to find line numbers
            matching_lines = [
                line_num 
                for line_num, line in enumerate(file, 1) 
                if search_string in line
            ]
            
        return matching_lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")