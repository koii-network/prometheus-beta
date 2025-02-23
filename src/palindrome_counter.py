def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    A palindromic substring reads the same forwards and backwards, 
    ignoring spaces and punctuation.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        int: The total number of palindromic substrings
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    """
    # Handle edge cases
    if not s:
        return 0
    
    # Expand around center approach
    def count_palindromes_around_center(left: int, right: int) -> int:
        """
        Count palindromes by expanding from a center.
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        
        Returns:
            int: Number of palindromes around this center
        """
        count = 0
        # Continue expanding while indices are valid and chars match
        while left >= 0 and right < len(s):
            # Skip non-alphanumeric characters
            while left >= 0 and not s[left].isalnum():
                left -= 1
            while right < len(s) and not s[right].isalnum():
                right += 1
            
            # Check if indices are still valid
            if left < 0 or right >= len(s):
                break
            
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                break
            
            # If we've found a palindrome
            count += 1
            
            # Move indices to expand
            left -= 1
            right += 1
        
        return count
    
    # Total palindrome count
    total_palindromes = 0
    
    # Check palindromes for each possible center
    for i in range(len(s)):
        # Odd length palindromes (single center)
        total_palindromes += count_palindromes_around_center(i, i)
        
        # Even length palindromes (between two centers)
        total_palindromes += count_palindromes_around_center(i, i+1)
    
    return total_palindromes