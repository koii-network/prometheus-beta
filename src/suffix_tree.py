class SuffixTree:
    class Node:
        def __init__(self):
            self.children = {}
            self.suffix_link = None
            self.start = None
            self.end = None
            self.suffix_index = -1

    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text using Ukkonen's algorithm.
        
        Args:
            text (str): Input string to build the suffix tree for
        """
        self.text = text + '$'  # Add end marker
        self.root = self.Node()
        self.root.suffix_link = self.root
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """
        Construct the suffix tree using Ukkonen's algorithm
        """
        n = len(self.text)
        last_new_node = None
        global_end = [-1]
        root = self.root

        for i in range(n):
            global_end[0] = i
            last_new_node = self._extend_suffix_tree(root, last_new_node, i, global_end)

    def _extend_suffix_tree(self, root, last_new_node, phase, global_end):
        """
        Extend the suffix tree for a single phase
        """
        # Implementation of suffix tree extension
        last_internal_node = None

        for j in range(phase + 1):
            current_char = self.text[phase]
            current_node = root
            # Implement extension rule
            # Placeholder for detailed Ukkonen's algorithm extension

        return last_new_node

    def search(self, pattern):
        """
        Search for a pattern in the suffix tree
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern is found, False otherwise
        """
        if not pattern:
            return False

        current_node = self.root
        for char in pattern:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return True

    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        """
        occurrences = []
        current_node = self.root

        for char in pattern:
            if char not in current_node.children:
                return occurrences
            current_node = current_node.children[char]

        # Depth-first traversal to collect all occurrences
        def collect_indices(node):
            if node.suffix_index != -1:
                occurrences.append(node.suffix_index)
            for child in node.children.values():
                collect_indices(child)

        collect_indices(current_node)
        return occurrences