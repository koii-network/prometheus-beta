def process_word_list(file_path):
    """
    Read a text file containing words, remove duplicates, and return sorted unique words.
    
    Args:
        file_path (str): Path to the text file containing words
    
    Returns:
        list: A sorted list of unique words
    
    Raises:
        FileNotFoundError: If the specified file cannot be found
        IOError: If there's an issue reading the file
    """
    try:
        # Read the file and split into words
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, convert to lowercase to ensure unique matching
            words = [word.strip().lower() for word in file.readlines()]
        
        # Remove duplicates and sort alphabetically
        unique_sorted_words = sorted(set(words))
        
        return unique_sorted_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"Error reading the file: {e}")