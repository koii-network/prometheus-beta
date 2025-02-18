class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = -1
        self.end = -1
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text using Ukkonen's algorithm.
        
        Args:
            text (str): The input text to build the suffix tree for.
        """
        self.text = text + '$'  # Append end marker
        self.root = SuffixTreeNode()
        self.root.suffix_link = self.root
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """
        Build the Suffix Tree using Ukkonen's algorithm.
        """
        n = len(self.text)
        last_new_node = None
        global_end = -1
        
        for i in range(n):
            global_end += 1
            remaining = 0
            last_new_node = None
            
            for j in range(len(str(i))):
                remaining += 1
                
                # Inner loop logic to insert suffixes
                while remaining > 0:
                    # Find the current node and edge we're working on
                    current_node = self._find_node(i, j)
                    
                    # If no node found, create a new leaf node
                    if current_node is None:
                        new_node = SuffixTreeNode()
                        new_node.start = i
                        new_node.end = global_end
                        
                        # Add the new node to the tree
                        self._add_node(j, new_node)
                        
                        # Update suffix links
                        if last_new_node is not None:
                            last_new_node.suffix_link = new_node
                        last_new_node = new_node
                    
                    remaining -= 1
        
    def _find_node(self, current_pos, j):
        """
        Find the appropriate node for inserting a new suffix.
        
        Args:
            current_pos (int): Current position in the text
            j (int): Current phase
        
        Returns:
            SuffixTreeNode or None: The node to insert at
        """
        # Placeholder for node finding logic
        return None

    def _add_node(self, j, node):
        """
        Add a node to the suffix tree.
        
        Args:
            j (int): Current phase
            node (SuffixTreeNode): Node to add
        """
        # Placeholder for node addition logic
        pass

    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): The pattern to search for
        
        Returns:
            bool: True if pattern is found, False otherwise
        """
        current_node = self.root
        
        for char in pattern:
            if char not in current_node.children:
                return False
            
            current_node = current_node.children[char]
        
        return True

    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): The pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        """
        occurrences = []
        current_node = self.root
        
        for char in pattern:
            if char not in current_node.children:
                return occurrences
            
            current_node = current_node.children[char]
        
        # Collect all leaf nodes under the current node
        self._collect_leaf_indices(current_node, occurrences)
        
        return occurrences

    def _collect_leaf_indices(self, node, occurrences):
        """
        Recursively collect leaf node indices.
        
        Args:
            node (SuffixTreeNode): Current node
            occurrences (list): List to store occurrence indices
        """
        if node.suffix_index != -1:
            occurrences.append(node.suffix_index)
        
        for child in node.children.values():
            self._collect_leaf_indices(child, occurrences)