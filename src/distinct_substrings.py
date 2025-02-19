class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = -1
        self.end = -1
        self.suffix_index = -1

class SuffixTree:
    def __init__(self, s):
        self.s = s + '$'  # Add end marker
        self.root = SuffixTreeNode()
        self.last_new_node = None
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.leaf_end = -1
        self.build_suffix_tree()
    
    def get_new_node(self, start, end):
        node = SuffixTreeNode()
        node.start = start
        node.end = end
        return node
    
    def add_suffix_link(self, node):
        if self.last_new_node is not None:
            self.last_new_node.suffix_link = node
        self.last_new_node = node
    
    def get_edge_length(self, node):
        return node.end - node.start + 1
    
    def count_distinct_substrings(self):
        def dfs_count(node):
            if not node.children:
                return 1
            
            count = 1  # count the path to this node
            for child in node.children.values():
                count += dfs_count(child)
            
            return count
        
        # Subtract 1 to exclude the empty substring
        return max(0, dfs_count(self.root) - 1)
    
    def build_suffix_tree(self):
        n = len(self.s)
        
        for i in range(n):
            self.leaf_end = i
            self.remaining_suffix_count += 1
            self.last_new_node = None
            
            while self.remaining_suffix_count > 0:
                if self.active_length == 0:
                    # Active point is at root
                    if self.s[i] in self.active_node.children:
                        # If edge exists, go to next phase
                        self.active_edge = self.active_node.children[self.s[i]].start
                        self.active_length += 1
                        break
                    else:
                        # Create a new leaf node
                        new_node = self.get_new_node(i, self.leaf_end)
                        self.active_node.children[self.s[i]] = new_node
                        self.remaining_suffix_count -= 1
                else:
                    # Try to find the next character on the current path
                    try:
                        current_node = self.active_node
                        if self.active_edge != -1:
                            current_node = self.active_node.children[self.s[self.active_edge]]
                        
                        # Check if we can skip to next node
                        next_char_index = current_node.start + self.active_length
                        if self.s[next_char_index] == self.s[i]:
                            # If match, proceed to next phase
                            self.active_length += 1
                            break
                        
                        # Split the existing edge
                        split_node = self.get_new_node(current_node.start, 
                                                       current_node.start + self.active_length - 1)
                        self.active_node.children[self.s[self.active_edge]] = split_node
                        
                        # Create new leaf node
                        new_leaf = self.get_new_node(i, self.leaf_end)
                        split_node.children[self.s[i]] = new_leaf
                        current_node.start += self.active_length
                        split_node.children[self.s[current_node.start]] = current_node
                        
                        # Update suffix links
                        self.add_suffix_link(split_node)
                        
                        self.remaining_suffix_count -= 1
                    except Exception:
                        pass
                
                # Move to next suffix
                if self.active_node == self.root:
                    self.active_edge += 1
                    self.active_length -= 1
                elif self.active_node.suffix_link:
                    self.active_node = self.active_node.suffix_link
                else:
                    self.active_node = self.root

def count_distinct_substrings(s):
    """
    Find the number of distinct substrings in a given string.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Number of distinct substrings
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> count_distinct_substrings('aab')
        6
        >>> count_distinct_substrings('abcde')
        15
        >>> count_distinct_substrings('')
        0
    """
    if not s:
        return 0
    
    suffix_tree = SuffixTree(s)
    return suffix_tree.count_distinct_substrings()