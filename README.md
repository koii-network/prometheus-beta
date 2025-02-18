# LZSS Compression Implementation

## Overview
This project implements the Lempel-Ziv-Storer-Szymanski (LZSS) compression algorithm in Python. 

## Features
- Compress and decompress data using the LZSS algorithm
- Configurable sliding window and look-ahead buffer sizes
- Supports bytes and string inputs
- Handles various input scenarios including empty, short, and repeated data

## Usage
```python
from src.lzss_compression import LZSSCompressor

# Create a compressor
compressor = LZSSCompressor()

# Compress data
data = "Hello, World!"
compressed = compressor.compress(data)

# Decompress data
decompressed = compressor.decompress(compressed)
print(decompressed)  # Outputs: Hello, World!
```

## Testing
Run tests using pytest:
```
pytest tests/test_lzss_compression.py
```