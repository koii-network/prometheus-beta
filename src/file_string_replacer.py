def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a string in a file.
    
    :param file_path: Path to the file to modify
    :param old_string: String to be replaced
    :param new_string: String to replace with
    :return: Number of replacements made
    :raises FileNotFoundError: If the file does not exist
    :raises IOError: If there are issues reading or writing the file
    """
    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            file_contents = file.read()
        
        # Count the number of replacements
        replacements_count = file_contents.count(old_string)
        
        # Replace the string
        modified_contents = file_contents.replace(old_string, new_string)
        
        # Write back to the file
        with open(file_path, 'w') as file:
            file.write(modified_contents)
        
        return replacements_count
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"Error processing the file: {e}")