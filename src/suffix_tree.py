class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start_index = -1
        self.end_index = -1
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text using Ukkonen's algorithm.
        
        Args:
            text (str): Input text to build the suffix tree for
        """
        self.text = text + '$'  # Add end marker
        self.root = SuffixTreeNode()
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm
        """
        n = len(self.text)
        
        # Extend the tree for each suffix
        for i in range(n):
            self._extend_suffix_tree(i)

    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for a given phase
        
        Args:
            phase (int): Current phase index
        """
        # Implementation of Ukkonen's algorithm extension rules
        last_new_node = None
        remaining = 0
        active_node = self.root
        active_edge = -1
        active_length = 0

        for j in range(phase + 1):
            remaining += 1
            while remaining > 0:
                # Find the current active point
                if active_length == 0:
                    active_edge = j
                
                # If current character doesn't exist in active node's children
                if active_edge not in active_node.children:
                    # Create a new leaf node
                    new_node = SuffixTreeNode()
                    new_node.start_index = j
                    new_node.end_index = phase
                    new_node.suffix_index = phase - remaining + 1
                    active_node.children[active_edge] = new_node
                    
                    # Create suffix link if last new node exists
                    if last_new_node is not None:
                        last_new_node.suffix_link = active_node
                        last_new_node = None
                else:
                    # Walk down the tree
                    next_node = active_node.children[active_edge]
                    edge_length = next_node.end_index - next_node.start_index + 1
                    
                    # If we need to walk down further
                    if active_length >= edge_length:
                        active_edge += edge_length
                        active_length -= edge_length
                        active_node = next_node
                        continue
                    
                    # Check if character matches
                    if self.text[next_node.start_index + active_length] == self.text[j]:
                        # Increment active length and stop
                        active_length += 1
                        break
                    
                    # Split the edge
                    split_node = SuffixTreeNode()
                    split_node.start_index = next_node.start_index
                    split_node.end_index = next_node.start_index + active_length - 1
                    active_node.children[active_edge] = split_node
                    
                    # Create a new leaf node
                    new_leaf = SuffixTreeNode()
                    new_leaf.start_index = j
                    new_leaf.end_index = phase
                    new_leaf.suffix_index = phase - remaining + 1
                    split_node.children[j] = new_leaf
                    
                    # Modify the original edge node
                    next_node.start_index += active_length
                    split_node.children[next_node.start_index] = next_node
                    
                    # Update suffix links
                    if last_new_node is not None:
                        last_new_node.suffix_link = split_node
                    last_new_node = split_node
                
                remaining -= 1
                
                # Update active point
                if active_node == self.root and active_length > 0:
                    active_length -= 1
                    active_edge = j - remaining + 1
                elif active_node != self.root:
                    active_node = active_node.suffix_link if active_node.suffix_link else self.root

    def search(self, pattern):
        """
        Search for a pattern in the suffix tree
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices where the pattern is found in the text
        """
        current_node = self.root
        i = 0
        
        while i < len(pattern):
            # If current character is not in children, pattern not found
            if pattern[i] not in current_node.children:
                return []
            
            current_node = current_node.children[pattern[i]]
            edge_length = current_node.end_index - current_node.start_index + 1
            
            # Check if the substring matches the edge
            substring = self.text[current_node.start_index:current_node.end_index + 1]
            j = 0
            while j < edge_length and i < len(pattern) and self.text[current_node.start_index + j] == pattern[i]:
                i += 1
                j += 1
            
            # If we haven't matched the full pattern, it's not in the tree
            if i < len(pattern):
                return []
        
        # Collect all suffixes in this subtree
        return self._collect_suffixes(current_node)

    def _collect_suffixes(self, node):
        """
        Collect all suffix indices in a subtree
        
        Args:
            node (SuffixTreeNode): Root of the subtree
        
        Returns:
            list: Suffix indices
        """
        suffixes = []
        
        # If it's a leaf node, return its suffix index
        if node.suffix_index != -1:
            suffixes.append(node.suffix_index)
        
        # Recursively collect suffixes from all children
        for child in node.children.values():
            suffixes.extend(self._collect_suffixes(child))
        
        return suffixes