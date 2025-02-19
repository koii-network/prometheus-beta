import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    """Build frequency dictionary for characters in the input data."""
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1
    return freq

def build_huffman_tree(freq):
    """Build Huffman tree from frequency dictionary."""
    heap = [Node(char, count) for char, count in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(node, current_code='', codes=None):
    """Generate Huffman codes for each character."""
    if codes is None:
        codes = {}
    
    if node is None:
        return codes
    
    if node.char is not None:
        codes[node.char] = current_code
    
    build_huffman_codes(node.left, current_code + '0', codes)
    build_huffman_codes(node.right, current_code + '1', codes)
    
    return codes

def lzh_compress(data):
    """
    Implement LZH (Lempel-Ziv-Huffman) compression algorithm.
    
    Args:
        data (str or bytes): Input data to compress
    
    Returns:
        dict: Compressed data with Huffman codes and compressed binary string
    """
    if not data:
        return {'compressed_data': '', 'huffman_codes': {}}
    
    # Convert input to string if it's bytes
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    
    # Lempel-Ziv sliding window compression
    dictionary = {}
    result = []
    current_sequence = ''
    
    for char in data:
        current_sequence += char
        if current_sequence not in dictionary:
            dictionary[current_sequence] = len(dictionary)
            result.append(current_sequence[:-1] if len(current_sequence) > 1 else current_sequence)
            current_sequence = char
    
    if current_sequence:
        result.append(current_sequence)
    
    # Huffman encoding of compressed data
    freq = build_frequency_dict(result)
    huffman_tree = build_huffman_tree(freq)
    huffman_codes = build_huffman_codes(huffman_tree)
    
    # Convert to binary string
    compressed_data = ''.join(huffman_codes[item] for item in result)
    
    return {
        'compressed_data': compressed_data,
        'huffman_codes': huffman_codes
    }