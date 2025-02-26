from collections import Counter
from typing import Dict, List

def count_word_frequencies(file_path: str) -> Dict[str, int]:
    """
    Read a text file and count the occurrences of each word.
    
    Args:
        file_path (str): Path to the text file containing comma and space-separated words.
    
    Returns:
        Dict[str, int]: A dictionary with words as keys and their frequencies as values,
                        sorted in descending order by frequency.
    
    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file is empty or contains invalid content.
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    try:
        # Read the file
        with open(file_path, 'r') as file:
            content = file.read().strip()
        
        # Check if file is empty
        if not content:
            raise ValueError("The file is empty")
        
        # Split words, handling potential multiple spaces or commas
        words = [word.strip() for word in content.replace(',', ' ').split()]
        
        # Count word frequencies and sort in descending order
        word_counts = Counter(words)
        return dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    
    except IOError:
        raise FileNotFoundError(f"Cannot read file: {file_path}")