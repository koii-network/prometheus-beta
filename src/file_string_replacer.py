def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of old_string with new_string in the specified file.
    
    Args:
        file_path (str): Path to the file to modify
        old_string (str): The string to be replaced
        new_string (str): The string to replace with
    
    Returns:
        int: Number of replacements made
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there are permission issues with the file
    """
    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            file_contents = file.read()
        
        # Count the number of occurrences before replacement
        replacements_count = file_contents.count(old_string)
        
        # Replace all occurrences
        modified_contents = file_contents.replace(old_string, new_string)
        
        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.write(modified_contents)
        
        return replacements_count
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to modify the file {file_path}.")