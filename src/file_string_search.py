def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a given file.
    
    Args:
        file_path (str): Path to the file to search
        search_string (str): String to search for in the file
    
    Returns:
        list: Line numbers (1-indexed) where the string is found
    
    Raises:
        FileNotFoundError: If the file does not exist
        TypeError: If inputs are not strings
    """
    if not isinstance(file_path, str) or not isinstance(search_string, str):
        raise TypeError("Both file_path and search_string must be strings")
    
    try:
        with open(file_path, 'r') as file:
            # Use enumerate to track line numbers, starting from 1
            matching_lines = [
                line_num + 1 
                for line_num, line in enumerate(file) 
                if search_string in line
            ]
        
        return matching_lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")