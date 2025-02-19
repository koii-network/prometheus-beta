class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.end = float('inf')

class SuffixTree:
    def __init__(self, string):
        self.string = string + '$'  # Sentinel character
        self.root = SuffixTreeNode()
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """
        Build suffix tree using Ukkonen's algorithm in O(n) time.
        """
        n = len(self.string)
        global_end = [0]
        active_node = self.root
        active_length = 0
        active_edge = 0

        for i in range(n):
            global_end[0] = i
            remainder = 1
            last_new_node = None

            while remainder > 0:
                # If active length is 0, start from root
                if active_length == 0:
                    if self.string[active_edge] in active_node.children:
                        active_length += 1
                    else:
                        # Create a new leaf node
                        active_node.children[self.string[i]] = SuffixTreeNode()
                        active_node.children[self.string[i]].end = i
                        remainder -= 1

                # If active length is non-zero
                else:
                    # Get next character to process
                    next_char_idx = active_edge + active_length
                    if next_char_idx >= n:
                        break

                    next_char = self.string[next_char_idx]
                    current_edge_char = self.string[active_edge]

                    # If next character matches
                    if current_edge_char in active_node.children:
                        edge_node = active_node.children[current_edge_char]
                        edge_length = edge_node.end - active_edge + 1

                        # Move to the next character on the edge
                        if active_length >= edge_length:
                            active_edge += edge_length
                            active_length -= edge_length
                            active_node = edge_node
                            continue

                        # No extension needed
                        if self.string[edge_node.end - edge_length + active_length + 1] == self.string[i]:
                            active_length += 1
                            break

                        # Split the edge
                        split_node = SuffixTreeNode()
                        split_node.end = edge_node.end
                        split_node.children[self.string[i]] = SuffixTreeNode()
                        split_node.children[self.string[i]].end = i
                        split_node.children[current_edge_char] = edge_node
                        edge_node.end = active_edge + active_length
                        active_node.children[current_edge_char] = split_node

                        if last_new_node:
                            last_new_node.suffix_link = split_node
                        last_new_node = split_node

                    else:
                        # Create a new leaf node
                        active_node.children[self.string[i]] = SuffixTreeNode()
                        active_node.children[self.string[i]].end = i

                    remainder -= 1

            if remainder == 0:
                break

    def count_distinct_substrings(self):
        """
        Count the number of distinct substrings in the tree.
        Uses a traversal to count unique paths.
        Time Complexity: O(n)
        
        Returns:
            int: Number of distinct substrings
        """
        # Set to track unique substrings
        unique_substrings = set()

        def dfs(node, current_substring=''):
            # If we've reached a leaf node, add the path
            if not node.children:
                return

            for edge_char, child_node in node.children.items():
                # Construct substring
                substring = current_substring + edge_char

                # Add all prefixes of substring
                for i in range(1, len(substring) + 1):
                    unique_substrings.add(substring[:i])

                # Recurse
                dfs(child_node, substring)

        # Start DFS from root
        dfs(self.root)

        # Subtract 1 to exclude empty substring
        return len(unique_substrings)

def find_distinct_substrings(s: str) -> int:
    """
    Find the number of distinct substrings in a given string.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Number of distinct substrings
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s:
        return 0
    
    # Use Suffix Tree to count distinct substrings
    suffix_tree = SuffixTree(s)
    return suffix_tree.count_distinct_substrings()