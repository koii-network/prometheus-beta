def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a given string in a file.
    
    Args:
        file_path (str): Path to the file to modify
        old_string (str): The string to be replaced
        new_string (str): The string to replace with
    
    Returns:
        int: Number of replacements made
    
    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading or writing the file
    """
    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            file_contents = file.read()
        
        # Count the number of replacements
        replacements_count = file_contents.count(old_string)
        
        # Replace the string
        modified_contents = file_contents.replace(old_string, new_string)
        
        # Write the modified contents back to the file
        with open(file_path, 'w') as file:
            file.write(modified_contents)
        
        return replacements_count
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"Error processing file {file_path}: {str(e)}")