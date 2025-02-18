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
            text (str): Input string to build the suffix tree for
        """
        self.text = text + '$'  # Adding end marker
        self.root = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm
        """
        n = len(self.text)
        for i in range(n):
            self._extend_suffix_tree(i)

    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for each character
        """
        last_new_node = None
        k = 0
        global_end = phase

        for j in range(phase + 1):
            k = self._update_tree(j, k, phase, global_end, last_new_node)

    def _update_tree(self, j, k, phase, global_end, last_new_node):
        """
        Core update function for suffix tree construction
        """
        current_node = self.root
        created_new_node = False
        
        while True:
            # If k is beyond the active point, break
            if k > phase:
                break

            # Find the current character
            current_char = self.text[k]

            # Traverse the tree to the appropriate node
            if current_node.children.get(current_char) is None:
                # Create a new leaf node if character doesn't exist
                new_node = SuffixTreeNode()
                new_node.start_index = k
                new_node.end_index = global_end
                new_node.suffix_index = phase
                current_node.children[current_char] = new_node
                
                # If a new internal node was created in the previous iteration, 
                # create a suffix link from it to the current node
                if last_new_node is not None:
                    last_new_node.suffix_link = current_node
                    last_new_node = None
                
                created_new_node = True

            else:
                # Follow the path that matches the current character
                next_node = current_node.children[current_char]
                edge_length = next_node.end_index - next_node.start_index + 1
                
                # If we can fully traverse the edge
                if k + edge_length <= phase + 1:
                    k += edge_length
                    current_node = next_node
                    continue

                # Partial match case
                match_char_index = next_node.start_index + (phase - k + 1)
                
                if self.text[match_char_index] == self.text[phase + 1]:
                    # Extension rule 3: Do nothing
                    break
                else:
                    # Split the edge and create a new internal node
                    split_node = SuffixTreeNode()
                    split_node.start_index = next_node.start_index
                    split_node.end_index = match_char_index - 1
                    
                    # Update original node
                    next_node.start_index = match_char_index
                    
                    # Link the nodes
                    current_node.children[current_char] = split_node
                    split_node.children[self.text[match_char_index]] = next_node
                    
                    # Create a new leaf node
                    new_leaf = SuffixTreeNode()
                    new_leaf.start_index = phase + 1
                    new_leaf.end_index = global_end
                    new_leaf.suffix_index = phase
                    split_node.children[self.text[phase + 1]] = new_leaf
                    
                    # Suffix link handling
                    if last_new_node is not None:
                        last_new_node.suffix_link = split_node
                    
                    last_new_node = split_node
                    created_new_node = True

            k += 1

        return k

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

        current_node = self.root
        i = 0

        while i < len(pattern):
            current_char = pattern[i]
            
            if current_char not in current_node.children:
                return False
            
            child_node = current_node.children[current_char]
            edge_length = child_node.end_index - child_node.start_index + 1
            
            # Check if we match the entire edge
            for j in range(edge_length):
                if i >= len(pattern):
                    return True
                
                if pattern[i] != self.text[child_node.start_index + j]:
                    return False
                
                i += 1
            
            current_node = child_node

        return True