import os
import pytest
from src.file_comparison import are_files_identical

def create_test_file(filename, content):
    """Helper function to create test files"""
    with open(filename, 'w') as f:
        f.write(content)

def test_identical_files():
    """Test that identical files return True"""
    try:
        create_test_file('test_file1.txt', 'Hello, World!')
        create_test_file('test_file2.txt', 'Hello, World!')
        
        assert are_files_identical('test_file1.txt', 'test_file2.txt') == True
    finally:
        # Clean up test files
        if os.path.exists('test_file1.txt'):
            os.remove('test_file1.txt')
        if os.path.exists('test_file2.txt'):
            os.remove('test_file2.txt')

def test_different_files():
    """Test that different files return False"""
    try:
        create_test_file('test_file1.txt', 'Hello, World!')
        create_test_file('test_file2.txt', 'Hello, Universe!')
        
        assert are_files_identical('test_file1.txt', 'test_file2.txt') == False
    finally:
        # Clean up test files
        if os.path.exists('test_file1.txt'):
            os.remove('test_file1.txt')
        if os.path.exists('test_file2.txt'):
            os.remove('test_file2.txt')

def test_non_existent_file():
    """Test that non-existent files raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        are_files_identical('non_existent_file1.txt', 'non_existent_file2.txt')

def test_different_sized_files():
    """Test files with different sizes return False"""
    try:
        create_test_file('test_file1.txt', 'Short')
        create_test_file('test_file2.txt', 'Longer content')
        
        assert are_files_identical('test_file1.txt', 'test_file2.txt') == False
    finally:
        # Clean up test files
        if os.path.exists('test_file1.txt'):
            os.remove('test_file1.txt')
        if os.path.exists('test_file2.txt'):
            os.remove('test_file2.txt')