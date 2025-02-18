import os
import pytest
import tempfile
import shutil

from src.file_merger import merge_files

def test_merge_files_basic():
    # Create temporary directory for test files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test input files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        output_path = os.path.join(temp_dir, 'merged.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write('Hello ')
        
        with open(file2_path, 'w') as f2:
            f2.write('World!')
        
        # Merge files
        result = merge_files([file1_path, file2_path], output_path)
        
        # Verify merge
        assert result == output_path
        with open(output_path, 'r') as merged:
            assert merged.read() == 'Hello World!'

def test_merge_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple test files
        files = []
        for i in range(3):
            file_path = os.path.join(temp_dir, f'file{i}.txt')
            with open(file_path, 'w') as f:
                f.write(f'Content {i}\n')
            files.append(file_path)
        
        output_path = os.path.join(temp_dir, 'merged_multi.txt')
        
        merge_files(files, output_path)
        
        with open(output_path, 'r') as merged:
            content = merged.read()
            assert 'Content 0' in content
            assert 'Content 1' in content
            assert 'Content 2' in content

def test_merge_files_empty_input():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'merged.txt')
        
        with pytest.raises(ValueError, match="No input files provided"):
            merge_files([], output_path)

def test_merge_files_no_output():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'file.txt')
        with open(file_path, 'w') as f:
            f.write('Test')
        
        with pytest.raises(ValueError, match="No output file specified"):
            merge_files([file_path], '')

def test_merge_files_nonexistent_input():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, 'merged.txt')
        
        with pytest.raises(FileNotFoundError):
            merge_files(['/path/to/nonexistent/file.txt'], output_path)

# Binary file merging test
def test_merge_binary_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create binary test files
        file1_path = os.path.join(temp_dir, 'file1.bin')
        file2_path = os.path.join(temp_dir, 'file2.bin')
        output_path = os.path.join(temp_dir, 'merged.bin')
        
        binary_data1 = b'\x00\x01\x02\x03'
        binary_data2 = b'\x04\x05\x06\x07'
        
        with open(file1_path, 'wb') as f1:
            f1.write(binary_data1)
        
        with open(file2_path, 'wb') as f2:
            f2.write(binary_data2)
        
        merge_files([file1_path, file2_path], output_path)
        
        with open(output_path, 'rb') as merged:
            assert merged.read() == binary_data1 + binary_data2