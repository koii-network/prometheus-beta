"""
Module for processing word lists from text files.

This module provides functionality to read a text file, remove duplicate words,
and return a sorted list of unique words.
"""

def process_word_list(file_path):
    """
    Read a text file, remove duplicate words, and return a sorted unique list.

    Args:
        file_path (str): Path to the text file containing words.

    Returns:
        list: A sorted list of unique words.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        IOError: If there's an issue reading the file.
        TypeError: If file_path is not a string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Read the file and process words
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, convert to lowercase
            words = [word.strip().lower() for word in file.readlines()]
            
            # Remove duplicates and sort
            unique_words = sorted(set(words))
            
            return unique_words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")