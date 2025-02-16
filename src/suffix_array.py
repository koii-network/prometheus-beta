def create_suffix_array(text):
    """
    Create a suffix array for the given text.
    
    A suffix array is a sorted array of all suffixes of a given string.
    
    Args:
        text (str): The input string to create suffix array for
    
    Returns:
        list: A list of indices representing the sorted suffixes
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty list
    if not text:
        return []
    
    # Create list of all suffixes with their original indices
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort suffixes lexicographically and extract original indices
    sorted_suffixes = sorted(suffixes, key=lambda x: x[0])
    
    # Return the original indices of sorted suffixes
    return [index for _, index in sorted_suffixes]

def find_substring(text, pattern):
    """
    Find all occurrences of a substring in a text using Suffix Array.
    
    Args:
        text (str): The text to search in
        pattern (str): The substring to search for
    
    Returns:
        list: Indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Type and input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # Create suffix array
    suffix_arr = create_suffix_array(text)
    
    # Binary search to find pattern in sorted suffixes
    results = []
    
    # Find first and last occurrences using binary search
    left, right = 0, len(suffix_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        suffix = text[suffix_arr[mid]:]
        
        # Compare the prefix of the suffix with the pattern
        if suffix.startswith(pattern):
            # Find leftmost and rightmost occurrences
            results.append(suffix_arr[mid])
            
            # Search left side for other occurrences
            l, r = left, mid - 1
            while l <= r:
                m = (l + r) // 2
                if text[suffix_arr[m]:].startswith(pattern):
                    results.append(suffix_arr[m])
                    r = m - 1
                else:
                    l = m + 1
            
            # Search right side for other occurrences
            l, r = mid + 1, right
            while l <= r:
                m = (l + r) // 2
                if text[suffix_arr[m]:].startswith(pattern):
                    results.append(suffix_arr[m])
                    l = m + 1
                else:
                    r = m - 1
            
            break
        
        # Adjust binary search
        elif pattern < suffix:
            right = mid - 1
        else:
            left = mid + 1
    
    # Return sorted unique indices
    return sorted(set(results))