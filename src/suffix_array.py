def create_suffix_array(s):
    """
    Create a suffix array for the given string.
    
    A suffix array is a sorted array of all suffixes of a string.
    
    Args:
        s (str): Input string to create suffix array for
    
    Returns:
        list: Sorted array of suffix indices
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return []
    
    # Create list of suffixes with their original indices
    suffixes = [(s[i:], i) for i in range(len(s))]
    
    # Sort suffixes lexicographically 
    suffixes.sort()
    
    # Return only the indices of sorted suffixes
    return [suffix[1] for suffix in suffixes]

def find_substring(s, substring):
    """
    Find all occurrences of a substring in a string using suffix array.
    
    Args:
        s (str): Main string to search in
        substring (str): Substring to find
    
    Returns:
        list: Indices of all occurrences of substring in s
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If substring is empty
    """
    # Input validation
    if not isinstance(s, str) or not isinstance(substring, str):
        raise TypeError("Both inputs must be strings")
    
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    # Create suffix array
    suffix_arr = create_suffix_array(s)
    
    # Find all occurrences
    occurrences = []
    
    for i, suffix_idx in enumerate(suffix_arr):
        # Check if the current suffix starts with the substring
        if s[suffix_idx:].startswith(substring):
            occurrences.append(suffix_idx)
        
        # Optimization: Stop searching if we've gone past possible matches
        if len(s[suffix_idx:]) < len(substring):
            break
    
    return occurrences