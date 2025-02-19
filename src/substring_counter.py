class SuffixTree:
    class Node:
        def __init__(self):
            self.children = {}
            self.suffix_link = None
            self.start = -1
            self.end = -1
            self.suffix_index = -1

    def __init__(self, s):
        self.s = s + '$'  # Termination character
        self.root = self.Node()
        self.last_new_node = None
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.remaining_suffix_count = 0
        self.leaf_end = -1
        self.build_suffix_tree()

    def new_node(self, start, end=None):
        node = self.Node()
        node.start = start
        node.end = end
        return node

    def extend_suffix_tree(self, phase):
        self.leaf_end = phase
        self.remaining_suffix_count += 1
        self.last_new_node = None

        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                if self.s[phase] in self.active_node.children:
                    self.active_edge = self.active_node.children[self.s[phase]].start
                    self.active_length += 1
                    break
                else:
                    self.active_node.children[self.s[phase]] = self.new_node(phase)
                    self.remaining_suffix_count -= 1

            else:
                try:
                    next_node = self.active_node.children[self.s[self.active_edge]]
                    if self.walk_down(next_node):
                        continue

                    if self.s[next_node.start + self.active_length] == self.s[phase]:
                        self.active_length += 1
                        break

                    split_node = self.new_node(next_node.start, 
                                               next_node.start + self.active_length - 1)
                    self.active_node.children[self.s[self.active_edge]] = split_node
                    split_node.children[self.s[phase]] = self.new_node(phase)
                    split_node.children[self.s[next_node.start + self.active_length]] = next_node
                    next_node.start += self.active_length

                    if self.last_new_node is not None:
                        self.last_new_node.suffix_link = split_node
                    self.last_new_node = split_node

                except KeyError:
                    self.active_node.children[self.s[phase]] = self.new_node(phase)
                    self.remaining_suffix_count -= 1

                self.remaining_suffix_count -= 1

            if self.active_node == self.root:
                if self.active_length > 0:
                    self.active_length -= 1
                    self.active_edge = phase - self.remaining_suffix_count + 1
            else:
                self.active_node = self.active_node.suffix_link if self.active_node.suffix_link else self.root

    def walk_down(self, current_node):
        if current_node.end - current_node.start > self.active_length:
            return False
        self.active_edge += current_node.end - current_node.start + 1
        self.active_length -= current_node.end - current_node.start + 1
        self.active_node = current_node
        return True

    def build_suffix_tree(self):
        for i in range(len(self.s)):
            self.extend_suffix_tree(i)

    def count_distinct_substrings(self):
        def count_substrings(node):
            count = 1  # Current node (or edge) represents a substring
            for child in node.children.values():
                count += count_substrings(child)
            return count

        # Subtract 1 to exclude the root and the termination character
        return count_substrings(self.root) - 1

def count_distinct_substrings(s):
    """
    Find the number of distinct substrings in the given string.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Number of distinct substrings
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s:
        return 0
    
    suffix_tree = SuffixTree(s)
    return suffix_tree.count_distinct_substrings()