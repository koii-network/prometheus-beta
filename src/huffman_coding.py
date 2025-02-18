from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for the input data.
    
    Args:
        data (str): Input string to compress
    
    Returns:
        dict: Dictionary of character frequencies
    """
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Build Huffman tree from frequency dictionary.
    
    Args:
        freq_dict (dict): Dictionary of character frequencies
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    """
    # Create priority queue of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node with two children
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        heapq.heappush(heap, internal_node)
    
    return heap[0] if heap else None

def build_huffman_codes(root):
    """
    Generate Huffman codes from the Huffman tree.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary of Huffman codes for each character
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
        
        # Traverse left with '0'
        if node.left:
            traverse(node.left, current_code + '0')
        
        # Traverse right with '1'
        if node.right:
            traverse(node.right, current_code + '1')
    
    traverse(root, '')
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
        return '', None
    
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
    Decompress the data using the Huffman tree.
    
    Args:
        compressed_data (str): Compressed binary string
        huffman_tree (HuffmanNode): Root of the Huffman tree
    
    Returns:
        str: Decompressed original data
    """
    if not compressed_data or not huffman_tree:
        return ''
    
    # Traverse the tree to decode
    decompressed = []
    current_node = huffman_tree
    
    for bit in compressed_data:
        # Traverse based on the bit
        current_node = current_node.left if bit == '0' else current_node.right
        
        # If leaf node found
        if current_node.char is not None:
            decompressed.append(current_node.char)
            current_node = huffman_tree
    
    return ''.join(decompressed)