import heapq
from typing import Dict, List, Union

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data: bytes) -> Dict[int, int]:
    """Build frequency table for input bytes."""
    freq_table = {}
    for byte in data:
        freq_table[byte] = freq_table.get(byte, 0) + 1
    return freq_table

def build_huffman_tree(freq_table: Dict[int, int]) -> Node:
    """Build Huffman tree from frequency table."""
    heap = [Node(char=char, freq=freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root: Node, current_code: str = '', codes: Dict[int, str] = None) -> Dict[int, str]:
    """Generate Huffman codes from the Huffman tree."""
    if codes is None:
        codes = {}
    
    if root is None:
        return codes
    
    if root.char is not None:
        codes[root.char] = current_code
    
    generate_huffman_codes(root.left, current_code + '0', codes)
    generate_huffman_codes(root.right, current_code + '1', codes)
    
    return codes

def lzh_compress(data: bytes) -> bytes:
    """
    Implement LZH (Lempel-Ziv-Huffman) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not data:
        return b''
    
    # Lempel-Ziv sliding window compression
    window_size = 4096
    min_match_length = 3
    
    compressed = []
    current_pos = 0
    
    while current_pos < len(data):
        best_match_length = 0
        best_match_offset = 0
        
        # Search for the longest match in the sliding window
        search_start = max(0, current_pos - window_size)
        for offset in range(current_pos - search_start):
            match_length = 0
            while (current_pos + match_length < len(data) and 
                   data[current_pos - offset + match_length - 1] == data[current_pos + match_length] and 
                   match_length < 15):
                match_length += 1
            
            if match_length >= min_match_length and match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = offset + 1
        
        if best_match_length > 0:
            # Encode match: (offset, length)
            compressed.append((best_match_offset, best_match_length))
            current_pos += best_match_length
        else:
            # Encode literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    # Huffman encoding of compressed data
    freq_table = build_frequency_table(bytes(item if isinstance(item, int) else bytes([item[0], item[1]]) for item in compressed))
    huffman_tree = build_huffman_tree(freq_table)
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    # Encode with Huffman codes
    encoded_data = []
    for item in compressed:
        if isinstance(item, int):
            encoded_data.extend(huffman_codes[item])
        else:
            encoded_data.extend(huffman_codes[item[0]])
            encoded_data.extend(huffman_codes[item[1]])
    
    # Convert bit string to bytes
    result = bytearray()
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        byte = byte + ['0'] * (8 - len(byte))  # Pad to 8 bits
        result.append(int(''.join(byte), 2))
    
    return bytes(result)