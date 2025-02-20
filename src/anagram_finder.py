def find_anagrams(word, word_list):
    """
    Find all anagrams of a given word within a list of words.
    
    Args:
        word (str): The word to find anagrams for
        word_list (list): List of words to search for anagrams
    
    Returns:
        list: A list of anagrams found in the word_list
    """
    # Convert the input word to lowercase and sort its characters
    sorted_word = ''.join(sorted(word.lower()))
    
    # Find anagrams by comparing sorted characters
    # Exclude the original word from the results
    anagrams = [
        candidate for candidate in word_list 
        if ''.join(sorted(candidate.lower())) == sorted_word 
        and candidate.lower() != word.lower()
    ]
    
    return anagrams