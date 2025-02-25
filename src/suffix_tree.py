class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    This data structure allows for fast substring search and pattern matching
    with O(m) construction time and O(m + k) search time, where m is the length 
    of the input string and k is the length of the search pattern.
    """
    
    class Node:
        """
        Internal node class representing a node in the Suffix Tree.
        
        Attributes:
            children (dict): Dictionary of child nodes
            suffix_link (Node, optional): Link to another node for optimization
            start (int): Starting index of the edge label
            end (int): Ending index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            """
            Initialize a new Node.
            
            Args:
                start (int, optional): Starting index of the edge label. Defaults to -1.
                end (int, optional): Ending index of the edge label. Defaults to -1.
            """
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
        
        def edge_length(self):
            """
            Calculate the length of the edge label.
            
            Returns:
                int: Length of the edge label
            """
            return self.end - self.start + 1
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree
        
        Raises:
            ValueError: If input text is empty or not a string
        """
        # Validate input
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        if not text:
            raise ValueError("Input text cannot be empty")
        
        # Append terminator to ensure all suffixes are unique
        self.text = text + '$'
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Construct the Suffix Tree using Ukkonen's algorithm.
        
        Implements an efficient O(m) construction algorithm.
        """
        # Variables to track tree construction
        active_node = self.root
        active_length = 0
        active_edge = -1
        remainder = 0
        
        # Extend the tree for each character
        for i, char in enumerate(self.text):
            remainder += 1
            last_new_node = None
            
            while remainder > 0:
                # Create new node if no active edge
                if active_length == 0:
                    active_edge = i
                
                # If the current character is not found in children
                if char not in active_node.children:
                    # Create a new leaf node
                    new_leaf = self.Node(start=i, end=len(self.text)-1)
                    active_node.children[char] = new_leaf
                    
                    # Update the last internal node's suffix link
                    if last_new_node:
                        last_new_node.suffix_link = active_node
                        last_new_node = None
                
                else:
                    # Follow the edge
                    next_node = active_node.children[char]
                    edge_length = next_node.edge_length()
                    
                    # If we can walk down the tree
                    if active_length < edge_length:
                        # Check if the next character matches
                        if self.text[next_node.start + active_length] == char:
                            # Increment active length
                            active_length += 1
                            break
                        
                        # Split the edge
                        split_node = self.Node(start=next_node.start, 
                                               end=next_node.start + active_length - 1)
                        active_node.children[char] = split_node
                        
                        # Create a new leaf and connect
                        new_leaf = self.Node(start=i, end=len(self.text)-1)
                        split_node.children[char] = new_leaf
                        next_node.start += active_length
                        split_node.children[self.text[next_node.start]] = next_node
                        
                        # Handle suffix link
                        if last_new_node:
                            last_new_node.suffix_link = split_node
                        last_new_node = split_node
                    
                    else:
                        # Move to the next node and adjust active point
                        active_node = next_node
                        active_edge = active_edge + edge_length
                        active_length -= edge_length
                        continue
                
                # Decrement remainder and adjust active point if needed
                remainder -= 1
                if active_node == self.root and active_length > 0:
                    active_edge += 1
                    active_length -= 1
                elif active_node != self.root:
                    active_node = active_node.suffix_link or self.root
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: List of starting indices where the pattern is found
        
        Raises:
            ValueError: If pattern is empty or not a string
        """
        # Validate input
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        if not pattern:
            raise ValueError("Pattern cannot be empty")
        
        # Find the node representing the pattern (if it exists)
        current = self.root
        i = 0
        
        while i < len(pattern):
            # Find the child corresponding to the current character
            if pattern[i] not in current.children:
                return []  # Pattern not found
            
            # Follow the appropriate edge
            child = current.children[pattern[i]]
            edge_start = child.start
            edge_end = child.end
            edge_index = edge_start
            
            # Compare characters along the edge
            while edge_index <= edge_end and i < len(pattern):
                if self.text[edge_index] != pattern[i]:
                    return []  # Pattern does not match
                
                edge_index += 1
                i += 1
            
            # If we fully traversed the pattern
            if i == len(pattern):
                return self._collect_leaf_indices(child)
            
            # Move to the next node
            current = child
        
        return []
    
    def _collect_leaf_indices(self, node):
        """
        Collect all leaf indices under a given node.
        
        Args:
            node (Node): Starting node to collect indices from
        
        Returns:
            list: List of starting indices of suffixes
        """
        indices = []
        
        # If it's a leaf, return its index
        if not node.children:
            return [node.start]
        
        # Recursively collect indices from children
        for child in node.children.values():
            indices.extend(self._collect_leaf_indices(child))
        
        return indices