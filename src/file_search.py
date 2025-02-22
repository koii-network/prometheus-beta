def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a given file.
    
    Args:
        file_path (str): Path to the file to search
        search_string (str): String to search for in the file
    
    Returns:
        list: A list of line numbers (1-indexed) where the string is found
    """
    try:
        with open(file_path, 'r') as file:
            # Read lines and enumerate to get line numbers
            lines = file.readlines()
            
            # Find lines containing the search string
            matches = [
                line_num + 1  # 1-indexed line numbers
                for line_num, line in enumerate(lines)
                if search_string in line
            ]
            
            return matches
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError:
        raise IOError(f"Error reading file: {file_path}")