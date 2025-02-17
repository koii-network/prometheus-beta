import os
import pytest
from src.file_comparison import are_files_identical

def test_identical_files():
    # Create two identical test files
    with open('tests/test_file1.txt', 'w') as f1, open('tests/test_file2.txt', 'w') as f2:
        f1.write("Hello, world!")
        f2.write("Hello, world!")
    
    try:
        assert are_files_identical('tests/test_file1.txt', 'tests/test_file2.txt') == True
    finally:
        # Clean up test files
        os.remove('tests/test_file1.txt')
        os.remove('tests/test_file2.txt')

def test_different_files():
    # Create two different test files
    with open('tests/test_file1.txt', 'w') as f1, open('tests/test_file2.txt', 'w') as f2:
        f1.write("Hello, world!")
        f2.write("Hello, world!")
    
    try:
        assert are_files_identical('tests/test_file1.txt', 'tests/test_file2.txt') == True
        
        # Modify the second file
        with open('tests/test_file2.txt', 'w') as f2:
            f2.write("Hello, different world!")
        
        assert are_files_identical('tests/test_file1.txt', 'tests/test_file2.txt') == False
    finally:
        # Clean up test files
        os.remove('tests/test_file1.txt')
        os.remove('tests/test_file2.txt')

def test_nonexistent_file():
    # Test when a file does not exist
    with pytest.raises(FileNotFoundError):
        are_files_identical('tests/nonexistent1.txt', 'tests/nonexistent2.txt')