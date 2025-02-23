from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    """
    Represents a node in the Huffman tree.
    
    Attributes:
        char (str): The character this node represents
        freq (int): Frequency of the character
        left (HuffmanNode): Left child node
        right (HuffmanNode): Right child node
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """
        Allow comparison for heapq sorting based on frequency.
        """
        return self.freq < other.freq

def build_frequency_dict(data):
    """
    Build a frequency dictionary for characters in the input data.
    
    Args:
        data (str): Input string to analyze
    
    Returns:
        dict: A dictionary of character frequencies
    """
    if not data:
        return {}
    return dict(Counter(data))

def build_huffman_tree(freq_dict):
    """
    Build a Huffman tree from the frequency dictionary.
    
    Args:
        freq_dict (dict): Dictionary of character frequencies
    
    Returns:
        HuffmanNode: Root of the Huffman tree
    """
    if not freq_dict:
        return None
    
    # Create a priority queue (min-heap) of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build the tree
    while len(heap) > 1:
        # Extract two nodes with lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        # Push the new node back to the heap
        heapq.heappush(heap, internal_node)
    
    return heap[0] if heap else None

def build_huffman_codes(root):
    """
    Generate Huffman codes for each character.
    
    Args:
        root (HuffmanNode): Root of the Huffman tree
    
    Returns:
        dict: Dictionary of characters and their Huffman codes
    """
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        """
        Recursively traverse the Huffman tree to generate codes.
        
        Args:
            node (HuffmanNode): Current node
            current_code (str): Current code path
        """
        if not node:
            return
        
        # Leaf node
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        # Recurse left with '0'
        if node.left:
            traverse(node.left, current_code + '0')
        
        # Recurse right with '1'
        if node.right:
            traverse(node.right, current_code + '1')
    
    traverse(root, '')
    return codes

def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str): Input string to encode
    
    Returns:
        tuple: (encoded_data, huffman_tree)
        - encoded_data (str): Binary string representation of encoded data
        - huffman_tree (dict): Huffman codes for each character
    """
    if not data:
        return '', {}
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    tree_root = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(tree_root)
    
    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, huffman_codes

def huffman_decode(encoded_data, huffman_codes):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Binary string to decode
        huffman_codes (dict): Huffman codes dictionary
    
    Returns:
        str: Decoded original data
    """
    if not encoded_data or not huffman_codes:
        return ''
    
    # Reverse the Huffman codes dictionary
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded_data = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ''
    
    # Ensure all bits were decoded
    if current_code:
        raise ValueError("Invalid encoded data: could not decode entire string")
    
    return ''.join(decoded_data)