def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a string in a file.
    
    Args:
        file_path (str): Path to the file to modify
        old_string (str): String to be replaced
        new_string (str): String to replace with
    
    Returns:
        bool: True if replacements were made, False otherwise
    
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there are issues reading or writing the file
    """
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Check if replacement is needed
        if old_string not in file_content:
            return False
        
        # Replace all occurrences
        modified_content = file_content.replace(old_string, new_string)
        
        # Write back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        return True
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error processing file {file_path}: {str(e)}")