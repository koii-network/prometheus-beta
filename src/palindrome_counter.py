def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    A palindromic substring reads the same forwards and backwards,
    ignoring spaces and punctuation.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Number of palindromic substrings
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # If the string is empty, return 0
    if not cleaned_str:
        return 0
    
    count = 0
    n = len(cleaned_str)
    
    # Check palindromes of odd and even lengths
    for center in range(n):
        # Odd length palindromes
        left, right = center, center
        while left >= 0 and right < n and cleaned_str[left] == cleaned_str[right]:
            count += 1
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = center, center + 1
        while left >= 0 and right < n and cleaned_str[left] == cleaned_str[right]:
            count += 1
            left -= 1
            right += 1
    
    return count