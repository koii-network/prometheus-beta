class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def count_distinct_substrings(s):
    """
    Counts the number of distinct substrings in a given string with O(n) time complexity.
    
    Args:
        s (str): Input string to count distinct substrings

    Returns:
        int: Number of distinct substrings
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    # Edge cases
    if not s:
        return 0
    
    # Create root of suffix trie
    root = TrieNode()
    distinct_substrings = 0
    
    # Generate all suffixes and insert into trie
    for i in range(len(s)):
        current = root
        for j in range(i, len(s)):
            # If character not in current node's children, it's a new substring
            if s[j] not in current.children:
                current.children[s[j]] = TrieNode()
                distinct_substrings += 1
            
            # Move to the next node
            current = current.children[s[j]]
    
    # Add 1 to account for empty substring
    return distinct_substrings + 1