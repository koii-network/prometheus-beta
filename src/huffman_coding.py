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
    """Build frequency dictionary for input data."""
    return Counter(data)

def build_huffman_tree(freq_dict):
    """Build Huffman tree from frequency dictionary."""
    # Handle single character case
    if len(freq_dict) == 1:
        char, freq = list(freq_dict.items())[0]
        root = HuffmanNode(None, freq)
        root.left = HuffmanNode(char, freq)
        return root

    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def build_huffman_codes(root):
    """Generate Huffman codes from the Huffman tree."""
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        if not node:
            return
        
        # Handle single character case
        if node.left and node.left.char is not None and not node.right:
            codes[node.left.char] = "0"
            return
        
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")
    
    traverse(root, "")
    return codes

def huffman_encode(data):
    """Encode data using Huffman coding."""
    if not data:
        return "", {}
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    huffman_tree = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    huffman_codes = build_huffman_codes(huffman_tree)
    
    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, huffman_codes

def huffman_decode(encoded_data, huffman_codes):
    """Decode Huffman encoded data."""
    if not encoded_data or not huffman_codes:
        return ""
    
    # Handle single character case
    if len(huffman_codes) == 1:
        char = list(huffman_codes.keys())[0]
        # Repeat the character according to the number of code bits
        return char * (len(encoded_data) // len(list(huffman_codes.values())[0]))
    
    # Reverse the Huffman codes dictionary
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded_data = []
    current_code = ""
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""
    
    if current_code:
        raise ValueError("Invalid encoded data")
    
    return ''.join(decoded_data)