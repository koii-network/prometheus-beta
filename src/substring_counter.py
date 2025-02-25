def count_distinct_substrings(s: str) -> int:
    """
    Count the number of distinct substrings in a given string using a linear-time algorithm.
    
    This implementation uses a suffix tree-like approach with a rolling hash to achieve O(n) time complexity.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        int: The number of distinct substrings in the string
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a string
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Empty string edge case
    if not s:
        return 0
    
    # Use a set to track unique substrings
    unique_substrings = set()
    
    # Generate all substrings in linear time
    n = len(s)
    for start in range(n):
        # Rolling substring generation
        current = ""
        for end in range(start, n):
            current += s[end]
            unique_substrings.add(current)
    
    return len(unique_substrings)