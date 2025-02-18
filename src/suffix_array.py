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
        list: Sorted indices of all occurrences of substring in s
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(s, str) or not isinstance(substring, str):
        raise TypeError("Both inputs must be strings")
    
    # Return empty list for empty substring
    if not substring:
        return []
    
    # Create suffix array
    suffix_arr = create_suffix_array(s)
    
    # Find all occurrences
    occurrences = []
    
    for suffix_idx in suffix_arr:
        # Check if the current suffix starts with the substring
        if s[suffix_idx:].startswith(substring):
            occurrences.append(suffix_idx)
    
    return sorted(occurrences)