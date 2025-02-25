from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    """Represents a node in the Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """Allow comparison for heapq priority queue."""
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for the input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: Character frequency dictionary
    """
    if not data:
        return {}
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Build Huffman tree from frequency dictionary.
    
    Args:
        freq_dict (dict): Character frequency dictionary
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    """
    if not freq_dict:
        return None
    
    # Create heap of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0] if heap else None

def build_huffman_codes(root):
    """
    Generate Huffman codes for each character.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary of characters to their Huffman codes
    """
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        if not node:
            return
        
        # Leaf node
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        # Recursive traversal
        if node.left:
            traverse(node.left, current_code + "0")
        if node.right:
            traverse(node.right, current_code + "1")
    
    traverse(root, "")
    return codes

def compress(data):
    """
    Compress the input data using Huffman coding.
    
    Args:
        data (str): Input string to compress
    
    Returns:
        tuple: (compressed_data, huffman_tree_root)
    """
    if not data:
        return "", None
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    huffman_tree = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(huffman_tree)
    
    # Compress the data
    compressed_data = ''.join(huffman_codes[char] for char in data)
    
    return compressed_data, huffman_tree

def decompress(compressed_data, huffman_tree):
    """
    Decompress Huffman coded data.
    
    Args:
        compressed_data (str): Compressed binary string
        huffman_tree (HuffmanNode): Huffman tree root
    
    Returns:
        str: Decompressed original data
    """
    if not compressed_data or not huffman_tree:
        return ""
    
    # Traverse tree to decode
    decoded = []
    current = huffman_tree
    
    for bit in compressed_data:
        # Traverse down the tree
        current = current.left if bit == '0' else current.right
        
        # If leaf node found
        if current.char is not None:
            decoded.append(current.char)
            # Reset to root
            current = huffman_tree
    
    return ''.join(decoded)