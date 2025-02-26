from collections import Counter
from typing import Dict, List

def count_word_frequencies(file_path: str) -> Dict[str, int]:
    """
    Read a text file and count the frequencies of words.

    Args:
        file_path (str): Path to the text file containing comma and space-separated words.

    Returns:
        Dict[str, int]: A dictionary of word frequencies sorted in descending order.
        
    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file is empty or contains invalid content.
    """
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read().strip()
        
        # Check if file is empty
        if not content:
            raise ValueError("The file is empty.")
        
        # Split the content by comma and space, and remove any extra whitespace
        words = [word.strip() for word in content.split(',')]
        
        # Remove any empty strings
        words = [word for word in words if word]
        
        # Count word frequencies
        word_counts = Counter(words)
        
        # Sort by frequency in descending order
        return dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    
    except IOError:
        raise FileNotFoundError(f"Could not read file: {file_path}")
    except Exception as e:
        raise ValueError(f"Error processing file: {str(e)}")

def get_total_word_count(file_path: str) -> int:
    """
    Get the total number of words in the file.

    Args:
        file_path (str): Path to the text file containing comma and space-separated words.

    Returns:
        int: Total number of words in the file.
    """
    word_frequencies = count_word_frequencies(file_path)
    return sum(word_frequencies.values())