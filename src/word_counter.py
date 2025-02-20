from collections import Counter

def analyze_word_frequency(file_path):
    """
    Read a text file with words separated by commas and spaces.
    Count occurrences of each word and return a sorted result.
    
    Args:
        file_path (str): Path to the input text file
    
    Returns:
        tuple: A tuple containing:
            - dict of word frequencies in descending order
            - total number of words
    """
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read().strip()
        
        # Handle empty file case
        if not content:
            return {}, 0
        
        # Split the content into words, removing extra whitespace
        words = [word.strip() for word in content.replace(',', ' ').split()]
        
        # Count word frequencies
        word_counts = Counter(words)
        
        # Sort the word counts in descending order
        sorted_word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
        
        return sorted_word_counts, len(words)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError:
        raise IOError(f"An error occurred while reading the file {file_path}.")