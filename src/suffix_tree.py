class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search operations with 
    time complexity close to O(m), where m is the length of the search pattern.
    """
    
    class Node:
        """
        Represents a node in the Suffix Tree.
        
        Attributes:
            children (dict): Dictionary of child nodes
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
            suffix_index (int): Index of the suffix
        """
        def __init__(self, start=-1, end=-1, suffix_index=-1):
            self.children = {}
            self.start = start
            self.end = end
            self.suffix_index = suffix_index
    
    def __init__(self, text):
        """
        Initialize the Suffix Tree.
        
        Args:
            text (str): Input string to build the suffix tree
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Builds the Suffix Tree by adding all suffixes.
        """
        # Add each suffix as a path in the tree
        for i in range(len(self.text)):
            self._add_suffix(i)
    
    def _add_suffix(self, start_index):
        """
        Add a suffix to the tree.
        
        Args:
            start_index (int): Starting index of the suffix
        """
        suffix = self.text[start_index:]
        current = self.root
        
        # Trace/create the path for the current suffix
        for j, char in enumerate(suffix):
            # If no child exists for this character, create a new leaf node
            if char not in current.children:
                leaf = self.Node(start=start_index+j, end=len(self.text)-1, suffix_index=start_index)
                current.children[char] = leaf
                break
            
            # If child exists, we might need to split the edge
            child = current.children[char]
            edge_length = child.end - child.start + 1
            
            # Check how much of the suffix matches the current edge
            for k in range(edge_length):
                if suffix[j+k] != self.text[child.start + k]:
                    # Split the edge
                    split_node = self.Node(start=child.start, end=child.start+k-1)
                    current.children[char] = split_node
                    
                    # Create new leaf for the remainder of the suffix
                    leaf = self.Node(start=start_index+j+k, end=len(self.text)-1, suffix_index=start_index)
                    split_node.children[suffix[j+k]] = leaf
                    
                    # Adjust the existing child
                    child.start += k
                    split_node.children[self.text[child.start]] = child
                    break
                
                # If we reach the end of the current edge and still matching
                if j+k+1 == len(suffix):
                    break
            else:
                # Fully matched current edge, move to next node
                current = current.children[char]
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern is found, False otherwise
        """
        if not pattern:
            return False
        
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            child = current.children[char]
            
            # Check if pattern matches the edge label
            edge_length = child.end - child.start + 1
            for i in range(min(edge_length, len(pattern))):
                if self.text[child.start + i] != pattern[i]:
                    return False
            
            current = child
            pattern = pattern[edge_length:]
            
            if not pattern:
                return True
        
        return False
    
    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        """
        if not pattern:
            return []
        
        # First find the node representing the pattern
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            child = current.children[char]
            
            # Check if pattern matches the edge label
            edge_length = child.end - child.start + 1
            for i in range(min(edge_length, len(pattern))):
                if self.text[child.start + i] != pattern[i]:
                    return []
            
            current = child
            pattern = pattern[edge_length:]
            
            if not pattern:
                break
        
        # Collect all leaf nodes under this subtree
        occurrences = []
        def collect_suffixes(node):
            if node.suffix_index != -1:
                occurrences.append(node.suffix_index)
            for child in node.children.values():
                collect_suffixes(child)
        
        collect_suffixes(current)
        return occurrences