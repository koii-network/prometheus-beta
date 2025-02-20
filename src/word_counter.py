from collections import Counter
from typing import Dict, Tuple

def count_words(file_path: str) -> Tuple[Dict[str, int], int]:
    """
    Read a text file and count word occurrences.
    
    Args:
        file_path (str): Path to the text file containing comma and space-separated words.
    
    Returns:
        Tuple containing:
        - Dictionary of word counts in descending order
        - Total number of words in the file
    
    Raises:
        FileNotFoundError: If the specified file cannot be found
        ValueError: If the file is empty
    """
    # Read the file
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if file is empty
    if not content:
        raise ValueError("The file is empty")
    
    # Split words, handling comma and space separators
    words = [word.strip() for word in content.replace(',', ' ').split()]
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Sort word counts in descending order
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_word_counts, len(words)