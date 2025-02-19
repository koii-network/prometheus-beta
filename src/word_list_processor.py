def process_word_list(file_path):
    """
    Read a text file, remove duplicate words, and return a sorted list of unique words.
    
    Args:
        file_path (str): Path to the text file containing words
    
    Returns:
        list: Sorted list of unique words
    
    Raises:
        FileNotFoundError: If the specified file cannot be found
        IOError: If there's an issue reading the file
    """
    try:
        # Read the file and strip whitespace from each line
        with open(file_path, 'r') as file:
            words = [word.strip() for word in file.readlines()]
        
        # Remove duplicates and sort alphabetically
        unique_sorted_words = sorted(set(words))
        
        return unique_sorted_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")