def find_anagrams(word, word_list):
    """
    Find all anagrams of a given word within a list of words.

    Args:
        word (str): The target word to find anagrams for.
        word_list (list): A list of words to search for anagrams.

    Returns:
        list: A list of anagrams found in the word_list.

    Raises:
        ValueError: If the input word or word list is invalid.
    """
    # Validate inputs
    if not isinstance(word, str):
        raise ValueError("Input word must be a string")
    
    if not isinstance(word_list, list):
        raise ValueError("Word list must be a list")
    
    # Normalize the input word (lowercase, sorted characters)
    sorted_word = ''.join(sorted(word.lower()))
    
    # Find anagrams (excluding the original word)
    anagrams = [
        candidate.lower() for candidate in word_list 
        if ''.join(sorted(candidate.lower())) == sorted_word 
        and candidate.lower() != word.lower()
    ]
    
    return anagrams