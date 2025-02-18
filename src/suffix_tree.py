class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = None
        self.end = None
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        """
        Construct a Suffix Tree using Ukkonen's algorithm.
        
        Args:
            text (str): Input text to build the suffix tree for
        """
        # Append a unique terminator to handle all suffixes
        self.text = text + '$'
        self.root = SuffixTreeNode()
        self.root.start = -1
        self.root.end = -1
        self.build_suffix_tree()
    
    def get_substring_end(self, node):
        """
        Helper method to get the end of a substring.
        
        Args:
            node (SuffixTreeNode): Node to get end for
        
        Returns:
            int: End index of the substring
        """
        return node.end if node.end is not None else len(self.text) - 1
    
    def string_length(self, node):
        """
        Calculate the length of the edge substring.
        
        Args:
            node (SuffixTreeNode): Node representing the edge
        
        Returns:
            int: Length of the edge substring
        """
        return self.get_substring_end(node) - node.start + 1
    
    def is_leaf(self, node):
        """
        Check if a node is a leaf node.
        
        Args:
            node (SuffixTreeNode): Node to check
        
        Returns:
            bool: True if node is a leaf, False otherwise
        """
        return len(node.children) == 0
    
    def get_substring(self, start, end):
        """
        Get substring of the text.
        
        Args:
            start (int): Start index
            end (int): End index
        
        Returns:
            str: Substring of the text
        """
        return self.text[start:end+1]
    
    def build_suffix_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm.
        """
        for i in range(len(self.text)):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for a given phase.
        
        Args:
            phase (int): Current phase of suffix tree construction
        """
        remaining = 1
        last_new_node = None
        current_node = self.root
        
        for j in range(phase + 1):
            key = self.text[j]
            
            if key not in current_node.children:
                # Create a new leaf node
                new_node = SuffixTreeNode()
                new_node.start = j
                new_node.end = phase
                current_node.children[key] = new_node
                
                if last_new_node is not None:
                    last_new_node.suffix_link = current_node
                    last_new_node = None
            else:
                # Walk down the tree
                next_node = current_node.children[key]
                
                # Skip/count algorithm
                walk_length = self.string_length(next_node)
                
                # If the current phase doesn't match the entire edge
                # we need to split the edge
                if phase - j + 1 < walk_length:
                    split_node = SuffixTreeNode()
                    split_node.start = next_node.start
                    split_node.end = next_node.start + phase - j
                    current_node.children[key] = split_node
                    
                    next_node.start += phase - j + 1
                    split_node.children[self.text[next_node.start]] = next_node
                    
                    # If we have a previously created node, link it
                    if last_new_node is not None:
                        last_new_node.suffix_link = split_node
                    last_new_node = split_node
                
                current_node = next_node
            
            remaining -= 1
    
    def find_substring(self, pattern):
        """
        Find all occurrences of a substring in the text.
        
        Args:
            pattern (str): Substring to search for
        
        Returns:
            list: Indices of substring occurrences
        """
        current_node = self.root
        
        # Traverse down the tree
        for char in pattern:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        
        # Collect all leaf nodes
        occurrences = []
        self._collect_leaf_indices(current_node, occurrences)
        return occurrences
    
    def _collect_leaf_indices(self, node, occurrences):
        """
        Collect indices of leaf nodes.
        
        Args:
            node (SuffixTreeNode): Current node
            occurrences (list): List to store indices
        """
        if self.is_leaf(node):
            occurrences.append(node.start)
        else:
            for child in node.children.values():
                self._collect_leaf_indices(child, occurrences)