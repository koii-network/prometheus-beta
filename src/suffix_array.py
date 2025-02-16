def create_suffix_array(s):
    """
    Create a Suffix Array for the given string.
    
    A Suffix Array is an array of all suffixes of a string sorted in lexicographic order.
    
    Args:
        s (str): Input string to create suffix array for
    
    Returns:
        list: Suffix Array containing indices of suffixes in lexicographic order
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Create list of (suffix, original index) tuples
    suffixes = [(s[i:], i) for i in range(len(s))]
    
    # Sort suffixes lexicographically and extract original indices
    suffix_array = [index for suffix, index in sorted(suffixes)]
    
    return suffix_array

def find_substring(s, pattern):
    """
    Find all occurrences of a pattern in a string using Suffix Array.
    
    Args:
        s (str): Text to search in
        pattern (str): Pattern to search for
    
    Returns:
        list: Indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Validate inputs
    if not isinstance(s, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # Create suffix array
    suffix_array = create_suffix_array(s)
    
    # Binary search to find pattern in sorted suffixes
    results = []
    left, right = 0, len(suffix_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        suffix = s[suffix_array[mid]:]
        
        # Compare pattern with current suffix
        if suffix.startswith(pattern):
            # Find all matching indices
            results.append(suffix_array[mid])
            
            # Check for other matches on left side
            l = mid - 1
            while l >= 0 and s[suffix_array[l]:].startswith(pattern):
                results.append(suffix_array[l])
                l -= 1
            
            # Check for other matches on right side
            r = mid + 1
            while r < len(suffix_array) and s[suffix_array[r]:].startswith(pattern):
                results.append(suffix_array[r])
                r += 1
            
            break
        elif pattern < suffix:
            right = mid - 1
        else:
            left = mid + 1
    
    return sorted(results)